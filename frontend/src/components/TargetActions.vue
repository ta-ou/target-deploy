<template>
  <div>
    <button class="btn btn-sm btn-outline-danger" @click="deleteTarget">目標を削除</button>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "TargetActions",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  methods: {
    async deleteTarget() {
      let endpoint = `/api/targets/${this.slug}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$router.push("/");
      } catch (err) {
        console.log(err);
      }
    }
  }
};
</script>
