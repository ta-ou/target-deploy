<template>
  <div>
    <div class="container">
      <div v-for="target in targets" :key="target.slug" class="mt-3">
        <p class="mb-2">
          ユーザー名：
          <span class="mr-3">{{ target.author }}</span>
          目標設定日：
          <span>{{ target.created_at }}</span>
        </p>
        <h2>
          <router-link
            :to="{ name: 'target', params: {slug: target.slug } }"
            class="target-link"
          >{{ target.target }}</router-link>
        </h2>
        <p class="mt-2">
          <span class="mr-4">頑張れ：{{ target.likes_count }}件</span>
          <span class="mr-4">コメント：{{ target.comment_count }}件</span>
          <span>
            状況：
            <span v-if="target.done_comment != null">終了済</span>
            <span v-else>継続中</span>
          </span>
        </p>
        <hr />
      </div>
      <div class="my-4">
        <p v-show="loadingTargets">ローディング中</p>
        <button v-show="next" @click="getTargets" class="btn btn-sm btn-outline-success">もっと見る</button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "Home",
  data() {
    return {
      targets: [],
      next: null,
      loadingTargets: false
    };
  },
  methods: {
    getTargets() {
      let endpoint = "/api/targets/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingTargets = true;
      apiService(endpoint).then(data => {
        this.targets.push(...data.results);
        this.loadingTargets = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    }
  },
  created() {
    this.getTargets();
    document.title = "Home";
  }
};
</script>

<style scoped>
.target-link {
  font-weight: bold;
  color: black;
}
.target-link:hover {
  color: #7a848f;
  text-decoration: none;
}
</style>