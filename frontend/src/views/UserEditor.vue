<template>
  <div class="container mt-3">
    <h1 class="mb-3">ユーザー情報を変更する</h1>
    <form @submit.prevent="onSubmit">
      <div class="mt-4 col-md-6">
        <p class="mb-0">新しいユーザーネーム</p>
        <input
          type="text"
          v-model.trim="username"
          class="form-control"
          maxlength="20"
        />
        <span>{{ username.length }}/20文字</span>
      </div>
      <div>
          <p class="mb-0">ユーザーアイコン</p>
      </div>
</template>

