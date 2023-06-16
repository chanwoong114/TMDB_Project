<template>
  <div class="bg-gray">
    <div class="board-detail">
      <h1>글 수정</h1>
      <form @submit.prevent="updateArtiecle">
        <div class="board-contents">
          <input type="text" v-model="title" class="w3-input w3-border" placeholder="제목을 입력해주세요.">
        </div>
        <div class="board-contents">
          <textarea id="" cols="30" rows="10" v-model="content" 
          placeholder="내용을 입력해주세요." class="w3-input w3-border" style="resize: none;">
          </textarea>
        </div>
        <div class="common-buttons">
          <button type="submit" class="w3-button w3-round w3-blue-gray" v-on:click="updateArtiecle">저장</button>&nbsp;
          <button type="button" class="w3-button w3-round w3-gray" v-on:click="articleList">목록</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'UpdateArticle',
  data() {
    return {
      requestBody: this.$route.query,
      idx: this.$route.query.idx,

      title: null,
      content: null,
    }
  },
  methods: {
    updateArtiecle() {
      const title = this.title
      const content = this.content

      this.$store.dispatch('updateArtiecle', { title, content, id: this.$route.params.articleId })
      
      delete this.requestBody.idx
      this.$router.push({name: 'communityDetail', params: {articleId: this.$route.params.articleId}})
    },
    articleList() {
      delete this.requestBody.idx
      this.$router.push({name: 'community'})
    },
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
        this.title = res.data.title
        this.content = res.data.content
      })
      .catch((err) => {
        if (err.message.indexOf('Network Error') > -1) {
          alert('네트워크가 원활하지 않습니다.\n잠시 후 다시 시도해주세요.')
        }
      })
    }
  },
  created() {
    this.getArticle()
  }
}
</script>

<style>

</style>