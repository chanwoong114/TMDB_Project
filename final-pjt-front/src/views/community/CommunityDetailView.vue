<template>
  <div class="bg-gray">
    <div class="board-detail">
      <div class="common-buttons">
        <span v-if="article.user.username===$store.state.username">
          <button type="button" class="w3-button w3-round w3-blue-gray" @click="articleUpdate">수정</button>&nbsp;
          <button type="button" class="w3-button w3-round w3-red" @click="articleDelete">삭제</button>&nbsp;
        </span>
        <button type="button" class="w3-button w3-round w3-gray" @click="articleList">목록</button>
      </div>
      <div class="board-contents">
        <h3>{{ article.title }}</h3>
        <div>
          <strong class="w3-large">작성자 : {{ article.user.username }}</strong>
          <br>
          <span>작성일자 {{ article.updated_at.slice(0, 10) }}</span>
        </div>
      </div>
      <div class="board-contents">
        <span>내용 : {{ article.content }}</span>
      </div>
      <div class="board-contents">
        <CommentView :articleId="article.id" :comments="article.comments"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentView from '@/components/community/CommentView.vue'

export default {
  name: 'CommunityDetailView',
  components: {
    CommentView
  },
  data() { //변수생성
    return {
      requestBody: this.$route.query,
      idx: this.$route.query.idx,

      article: []
    }
  },
  mounted() {
    this.getArticle()
  },
  methods: {
    getArticle() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/${this.$route.params.articleId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        if (err.message.indexOf('Network Error') > -1) {
          alert('네트워크가 원활하지 않습니다.\n잠시 후 다시 시도해주세요.')
        }
      })
    },
    articleList() {
      delete this.requestBody.idx
      this.$router.push({name: 'community'})
    },
    articleUpdate() {
      this.$router.push({name: 'UpdateArticle', params: {articleId: this.$route.params.articleId}})
    },
    articleDelete() {
      if (!confirm("삭제하시겠습니까?")) return

      this.$store.dispatch('deleteArticle', this.$route.params.articleId)
    }
  }
  }
</script>


<style>
  .underbar {
    border-bottom: 1px solid var(--ar-gray-900);
  }
  div {
    color: var(--ar-gray-900);
  }
</style>