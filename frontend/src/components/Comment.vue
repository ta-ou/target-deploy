<template>
  <div>
    <p class="text-muted">
      <strong>{{ comment.author }}</strong>
      &#8901; {{ comment.created_at }}
    </p>
    <p>{{ comment.body }}</p>
    <div v-if="isCommentAuthor">
      <button class="btn btn-sm btn-outline-danger" @click="triggerDeleteComment">Delete</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentComponent",
  props: {
    comment: {
      type: Object,
      required: true
    },
    requestUser: {
      type: String,
      required: true
    }
  },
  computed: {
    isCommentAuthor() {
      return this.comment.author === this.requestUser;
    }
  },
  methods: {
    triggerDeleteComment() {
      this.$emit("delete-comment", this.comment);
    }
  }
};
</script>
