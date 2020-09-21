<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand">Target Management</router-link>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link :to="{ name: 'home' }" class="btn btn-sm btn-outline-dark">ホーム画面</router-link>
          </li>
          <li class="nav-item ml-1">
            <router-link :to="{ name: 'own-target' }" class="btn btn-sm btn-outline-dark">自分の目標</router-link>
          </li>
          <li class="nav-item ml-1">
            <router-link :to="{ name: 'target-editor' }" class="btn btn-sm btn-outline-dark">目標を設定</router-link>
          </li>
          <li class="nav-item ml-1">
            <a class="btn btn-sm btn-outline-dark" href="/accounts/logout/">ログアウト</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  name: "NavbarComponent"
};
</script>
<style scoped>
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}
.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>