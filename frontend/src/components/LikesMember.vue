<template>
  <div>
    <div v-for="user in LikesMember" :key="user" class="">
      <p>{{ user }}</p>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "LikesMemberComponent",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  methods: {
    getTarget() {
      let endpoint = "/api/targets/";
      apiService(endpoint).then(data => {
        this.targets.push(...data.results);
        this.ownTarget();
      });
    }
  }
};
</script>

<style scoped></style>
