<template>
  <div class="mt-2">
    <div v-if="target" class="container">
      <p>
        ユーザー名：
        <span class="mr-3">{{ target.author }}</span>
        目標設定日：
        <span>{{ target.created_at }}</span>
      </p>
      <h1>目標：{{ target.target }}</h1>
      <h1>理由：{{ target.target_reason }}</h1>
      <h1>期限：{{ target.target_term }}</h1>
      <br />
      <h2 class="mt-1">その為に、毎日以下3つを実行する</h2>
      <ul>
        <li>
          <h2>{{ target.small_target_1 }}</h2>
        </li>
        <li>
          <h2>{{ target.small_target_2 }}</h2>
        </li>
        <li>
          <h2>{{ target.small_target_3 }}</h2>
        </li>
      </ul>
      <div v-if="target.done_comment != null">
        <hr />
        <p>この目標はすでに終了しました</p>
        <p>{{ target.done_comment }}</p>
      </div>
      <div v-if="isTargetAuthor">
        <TargetDoneComment v-if="target.done_comment === null" :slug="target.slug" class="mb-3" />
        <TargetActions :slug="target.slug" />
      </div>
      <div v-else>
        <button
          class="btn btn-sm"
          @click="toggleLike"
          :class="{'btn-danger': userLikedTarget, 'btn-outline-danger': !userLikedTarget}"
        >頑張れ：{{likesCounter}}件</button>
        <hr />
        <div v-if="userHasCommented">
          <p class="comment-added">既にコメント済みです</p>
        </div>
        <div v-else-if="showForm">
          <form class="card" @submit.prevent="onSubmit">
            <div class="card-header px-3">この目標にコメントする</div>
            <div class="card-block">
              <textarea
                rows="3"
                v-model="newCommentBody"
                class="form-control"
                placeholder="comment"
              ></textarea>
            </div>
            <div class="card-footer px-3">
              <button type="submit" class="btn btn-sm btn-outline-success">コメントを送信する</button>
            </div>
          </form>
          <p v-if="error" class="error mt-2">{{ error }}</p>
        </div>
        <div v-else>
          <button class="btn btn-sm btn-outline-success" @click="showForm = true">この目標にコメントする</button>
        </div>
      </div>
    </div>
    <div v-else class="container">
      <h1>目標が見つかりません</h1>
    </div>
    <div v-if="target" class="container">
      <hr />
      <CommentComponent
        v-for="(comment, index) in comments"
        :comment="comment"
        :requestUser="requestUser"
        :key="index"
        @delete-comment="deleteComment"
      />
      <div class="my-4">
        <p v-show="loadingComments">ローディング中</p>
        <button
          v-show="next"
          @click="getTargetComments"
          class="btn btn-sm btn-outline-success"
        >もっと見る</button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import CommentComponent from "@/components/Comment.vue";
import TargetActions from "@/components/TargetActions.vue";
import TargetDoneComment from "@/components/TargetDoneComment.vue";

export default {
  name: "Target",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    CommentComponent,
    TargetActions,
    TargetDoneComment
  },
  data() {
    return {
      target: {},
      comments: [],
      newCommentBody: null,
      error: null,
      userHasCommented: false,
      showForm: false,
      next: null,
      loadingComments: false,
      requestUser: null,
      userLikedTarget: false,
      likesCounter: null
    };
  },
  computed: {
    isTargetAuthor() {
      return this.target.author === this.requestUser;
    }
  },
  methods: {
    getTargetData() {
      let endpoint = `/api/targets/${this.slug}/`;
      apiService(endpoint).then(data => {
        if (data) {
          this.target = data;
          this.userHasCommented = data.user_has_commented;
          this.userLikedTarget = data.user_has_voted;
          this.likesCounter = data.likes_count;
        } else {
          this.target = null;
        }
      });
    },
    getTargetComments() {
      let endpoint = `/api/targets/${this.slug}/comments/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingComments = true;
      apiService(endpoint).then(data => {
        this.comments.push(...data.results);
        this.loadingComments = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
    onSubmit() {
      if (this.newCommentBody) {
        let endpoint = `/api/targets/${this.slug}/comment/`;
        apiService(endpoint, "POST", { body: this.newCommentBody }).then(
          data => {
            this.comments.unshift(data);
          }
        );
        this.newCommentBody = null;
        this.showForm = false;
        this.userHasCommented = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "空白があります";
      }
    },
    async deleteComment(comment) {
      let endpoint = `/api/comments/${comment.id}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$delete(this.comments, this.comments.indexOf(comment));
        this.userHasCommented = false;
      } catch (err) {
        console.log(err);
      }
    },
    toggleLike() {
      this.userLikedTarget === false ? this.likeAnswer() : this.unLikeAnswer();
    },
    likeAnswer() {
      this.userLikedTarget = true;
      this.likesCounter += 1;
      let endpoint = `/api/targets/${this.slug}/like/`;
      apiService(endpoint, "POST");
    },
    unLikeAnswer() {
      this.userLikedTarget = false;
      this.likesCounter -= 1;
      let endpoint = `/api/targets/${this.slug}/like/`;
      apiService(endpoint, "DELETE");
    }
  },
  created() {
    this.getTargetData();
    this.getTargetComments();
    this.requestUser = window.localStorage.getItem("username");
    document.title = "Target";
  }
};
</script>

<style scoped>
.comment-added {
  font-weight: bold;
  color: green;
}
.error {
  font-weight: bold;
  color: red;
}
</style>