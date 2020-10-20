<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <router-link :to="{ name: 'home' }" class="navbar-brand"
      >Target Management</router-link
    >
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link
            :to="{ name: 'home' }"
            class="nav-link btn btn-sm btn-outline-dark"
            >ホーム画面</router-link
          >
        </li>
        <li class="nav-item ml-1">
          <router-link
            :to="{ name: 'own-target' }"
            class="nav-link btn btn-sm btn-outline-dark"
            >自分の目標</router-link
          >
        </li>
        <li class="nav-item ml-1">
          <router-link
            :to="{ name: 'target-editor' }"
            class="nav-link btn btn-sm btn-outline-dark"
            >目標を設定</router-link
          >
        </li>
        <li class="nav-item ml-1">
          <a
            class="nav-link btn btn-sm btn-outline-dark"
            href="/accounts/logout/"
            >ログアウト</a
          >
        </li>
        <li class="nav-item dropdown">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            メニューを開く
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link
              :to="{ name: 'home' }"
              class="dropdown-item btn btn-sm btn-outline-dark"
              >ホーム画面</router-link
            >
            <router-link
              :to="{ name: 'own-target' }"
              class="dropdown-item btn btn-sm btn-outline-dark"
              >自分の目標</router-link
            >
            <router-link
              :to="{ name: 'target-editor' }"
              class="dropdown-item btn btn-sm btn-outline-dark"
              >目標を設定</router-link
            >
            <a
              class="dropdown-item btn btn-sm btn-outline-dark"
              href="/accounts/logout/"
              >ログアウト</a
            >
          </div>
        </li>
        <li class="nav-item">
          <a
            class="nav-link disabled"
            href="#"
            tabindex="-1"
            aria-disabled="true"
            >閉じる</a
          >
        </li>
      </ul>
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