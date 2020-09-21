<template>
  <div class="container">
    <div v-if="ownTargets.length !== 0">
      <h1 class="owntarget-title">あなたの目標です。毎日進捗を管理しましょう。</h1>
      <div
        v-for="target in ownTargets"
        :key="target.slug"
        class="container target-container mb-2 p-3"
      >
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
        <hr />
        <p>目標設定日：{{ target.created_at }}</p>
        <p>
          <span class="mr-4">頑張れ：{{ target.likes_count }}件</span>
          コメント：
          <router-link
            :to="{ name: 'target', params: {slug: target.slug } }"
          >{{ target.comment_count }}件</router-link>
        </p>
        <div v-if="target.done_comment != null">
          <p>{{ target.done_comment }}</p>
        </div>
        <div v-else>
          <TargetDoneComment :slug="target.slug" class="mb-3" />
        </div>
        <TargetActions :slug="target.slug" />
      </div>
    </div>
    <div v-else>
      <div class="mt-5 mb-5">
        <h1>まだ目標が設定されていません</h1>
        <h2>
          <router-link :to="{ name: 'target-editor' }">こちら</router-link>から目標を設定しましょう
        </h2>
      </div>
    </div>
  </div>
</template> 

<script>
import { apiService } from "@/common/api.service.js";
import TargetActions from "@/components/TargetActions.vue";
import TargetDoneComment from "@/components/TargetDoneComment.vue";

export default {
  name: "OwnTarget",
  data() {
    return {
      targets: [],
      ownTargets: [],
      requestUser: null
    };
  },
  components: {
    TargetActions,
    TargetDoneComment
  },
  methods: {
    getTarget() {
      let endpoint = "/api/targets/";
      apiService(endpoint).then(data => {
        this.targets.push(...data.results);
        this.ownTarget();
      });
    },
    ownTarget() {
      this.targets.filter(target => {
        if (target.author === this.requestUser) {
          this.ownTargets.push(target);
        }
      });
    }
  },
  created() {
    document.title = "Own Target";
    this.requestUser = window.localStorage.getItem("username");
    this.getTarget();
  }
};
</script>

<style scoped>
.owntarget-title {
  text-align: center;
}
.target-container {
  border: 1px solid;
}
</style>