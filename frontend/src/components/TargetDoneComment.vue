<template>
  <div>
    <hr />
    <p>目標が終了したら、以下からコメントを書きましょう</p>
    <div v-if="showForm">
      <form class="card" @submit.prevent="onSubmit">
        <p class="card-header px-3">この目標を終了する</p>
        <div class="card-block">
          <textarea
            type="text"
            rows="3"
            v-model="doneCommentBody"
            class="form-control"
            placeholder="目標達成に役立ったこと、有益だったこと、その他、同じような目標を持つ人にアドバイスを送りましょう"
          ></textarea>
        </div>
        <div class="card-footer px-3">
          <button type="submit" class="btn btn-sm btn-success">終了コメントを送信する</button>
        </div>
      </form>
    </div>
    <div v-else>
      <button class="btn btn-sm btn-outline-success" @click="showForm = true">目標を終了する</button>
    </div>
    <p v-if="error" class="error mt-2">{{ error }}</p>
    <hr />
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "TargetDoneComment",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      doneCommentBody: null,
      error: null,
      showForm: false
    };
  },
  methods: {
    onSubmit() {
      if (this.doneCommentBody) {
        let endpoint = `/api/targets/${this.slug}/`;
        apiService(endpoint, "PATCH", {
          done_comment: this.doneCommentBody
        }).then((this.doneCommentBody = null));
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "空白があります";
      }
    }
  }
};
</script>

<style scoped>
.error {
  font-weight: bold;
  color: red;
}
</style>