<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
    <FooterComponent />
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import FooterComponent from "@/components/Footer";
import NavbarComponent from "@/components/Navbar";

export default {
  name: "App",
  components: {
    FooterComponent,
    NavbarComponent
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
    }
  },
  created() {
    this.setUserInfo();
  }
};
</script>

<style>
html,
body {
  height: 100%;
  font-family: "Playfair Display", serif;
  background-color: #f5f5f5;
}
.btn:focus {
  box-shadow: none !important;
}
</style>
