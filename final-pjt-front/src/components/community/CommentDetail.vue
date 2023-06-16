<template>
  <div>
    <div v-if="updateCheck" class="input-group mb-3 ">
      <input type="text" class="form-control" v-model="content"
      aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
      <span @click="updateComment" class="btn bg-success mx-1 text-white" 
      id="inputGroup-sizing-default">수정</span>
      <span @click="updateToggle" class="btn bg-secondary mx-1 text-white" 
      id="inputGroup-sizing-default">취소</span>
    </div>
    <span v-if="!updateCheck" class="underbar d-flex justify-content-between" >
      <span>
        내용 : {{ comment.content }}
      </span>
      <span>
        작성자 : {{ comment.user.username }}
        <span v-if="comment.user.username === $store.state.username">
          <span class="btn btn-success mx-1" @click="updateToggle()">수정</span>
          <span class="btn btn-danger mx-1" @click="deleteComment()">삭제</span>
        </span>
      </span>
    </span>
  </div>
</template>

<script>

export default {
  name: 'CommentDetail',
  props: {
    comment: Object,
  },
  data() {
    return {
      updateCheck: false,
      content: '',
    }
  },
  methods: {
    deleteComment() {
      this.$store.dispatch('deleteComment', this.comment.id)
    },
    updateComment() {
      this.$store.dispatch('updateComment', [this.comment.id, this.content])
      this.content = ''
      this.updateCheck = !this.updateCheck
    },
    updateToggle() {
      this.updateCheck = !this.updateCheck
    }
  },
  created() {
    this.content = this.comment.content
  }
}
</script>

<style>

</style>