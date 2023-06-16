<template>
  <div>
    <h3>댓글 작성</h3>
    <div class="input-group">
      <input type="text" class="form-control" v-model="content"
      aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
      <span @click="createComment" class="mx-1 btn bg-primary text-white" id="inputGroup-sizing-default">작성</span>
    </div>

    <hr>
    <CommentDetail v-for="comment in commentList" :key="comment.id"
    :comment="comment"/>
    <!-- <span>
      내용 : {{ comment.content }}
    </span>
    <span>
      작성자 : {{ comment.user.username }}
      <span v-if="comment.user.username === $store.state.username">
        <span class="btn btn-success" @click="updateComment(comment.id)">수정</span>
        <span class="btn btn-danger" @click="deleteComment(comment.id)">삭제</span>
      </span>
    </span> -->
  </div>
</template>

<script>
import CommentDetail from './CommentDetail.vue'

export default {
  name: 'CommunityView',
  components: {
    CommentDetail
  },
  props: {
    articleId: Number,
    comments: Array
  },
  data() {
    return {
      content: '',
    }
  },
  methods: {
    createComment() {
      this.$store.dispatch('createComment', this.content)
      this.content = ''
    },
  },
  computed: {
    commentList() {
      return this.$store.getters.getComments
    }
  },
  mounted() {
    this.$store.dispatch('save_comments', [this.comments, this.articleId])
  }
}
</script>

<style>
  
</style>