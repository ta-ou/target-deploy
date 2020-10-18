<template>
  <div class="container mt-3">
    <h1 class="mb-3">達成したい目標を設定しましょう</h1>
    <form @submit.prevent="onSubmit">
      <div class="mt-4 col-md-6">
        <p class="mb-0">達成したい目標は何ですか</p>
        <input
          type="text"
          v-model.trim="target"
          class="form-control"
          placeholder="TOEIC 900点以上"
          maxlength="20"
        />
        <span>{{ target.length }}/20文字</span>
      </div>
      <div class="mt-3 col-md-6">
        <p class="mb-0">その目標を達成したい理由は何ですか</p>
        <input
          type="text"
          v-model.trim="target_reason"
          class="form-control"
          placeholder="海外担当になりたい為"
          maxlength="20"
        />
        <span>{{ target_reason.length }}/20文字</span>
      </div>
      <div class="mt-3 mb-3 col-md-8">
        <p class="mb-0">目標達成期限はいつですか</p>
        <vuejs-datepicker
          format="yyyy年MM月dd日"
          :language="ja"
          v-model="target_term"
          placeholder="期限を選んで下さい"
          :disabled-dates="disabledDates"
        ></vuejs-datepicker>
      </div>
      <div mt-3>
        <h2>
          上記の目標を達成する為に、
          <br />以下の条件を満たす毎日の行動目標を3つ立てましょう
        </h2>
        <ul>
          <li>具体的かつ客観的にする為、数字を使おう</li>
          <li>1日毎に達成・未達成の振り返りが出来るものにしよう</li>
          <li>継続すれば目標が達成出来るものにしよう</li>
        </ul>
      </div>
      <div class="mt-3 col-md-6">
        <p class="mb-0">行動目標１</p>
        <input
          type="text"
          v-model.trim="small_target_1"
          class="form-control"
          placeholder="10個単語を覚える"
          maxlength="20"
        />
        <span>{{ small_target_1.length }}/20文字</span>
      </div>
      <div class="mt-3 col-md-6">
        <p class="mb-0">行動目標２</p>
        <input
          type="text"
          v-model.trim="small_target_2"
          class="form-control"
          placeholder="30分リスニングする"
          maxlength="20"
        />
        <span>{{ small_target_2.length }}/20文字</span>
      </div>
      <div class="mt-3 col-md-6">
        <p class="mb-0">行動目標３</p>
        <input
          type="text"
          v-model.trim="small_target_3"
          class="form-control"
          placeholder="5ページ参考書を読む"
          maxlength="20"
        />
        <span>{{ small_target_3.length }}/20文字</span>
      </div>
      <br />
      <p v-if="error" class="muted mt-2 error">{{ error }}</p>
      <button type="submit" class="btn btn-outline-dark ml-3">登録</button>
    </form>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { ja } from "vuejs-datepicker/dist/locale";
import vuejsDatepicker from "vuejs-datepicker";
import moment from "moment";

export default {
  name: "TargetEditor",
  data() {
    return {
      target: "",
      target_reason: "",
      target_term: "",
      small_target_1: "",
      small_target_2: "",
      small_target_3: "",
      error: null,
      ja: ja,
      disabledDates: {
        to: new Date()
      }
    };
  },
  components: {
    "vuejs-datepicker": vuejsDatepicker
  },
  methods: {
    onSubmit() {
      if (
        !this.target ||
        !this.target_reason ||
        !this.target_term ||
        !this.small_target_1 ||
        !this.small_target_2 ||
        !this.small_target_3
      ) {
        this.error = "未入力の項目があります";
      } else {
        let endpoint = "/api/targets/";
        let method = "POST";
        apiService(endpoint, method, {
          target: this.target,
          target_reason: this.target_reason,
          target_term: moment(this.target_term).format("YYYY年MM月DD日"),
          small_target_1: this.small_target_1,
          small_target_2: this.small_target_2,
          small_target_3: this.small_target_3
        }).then(this.$router.push("/owntarget"));
      }
    }
  },
  created() {
    document.title = "Create Target";
  }
};
</script>

<style scoped>
.error {
  color: red;
  font-size: 1.5rem;
}
</style>
