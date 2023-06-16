<template>
  <div class="bg-gray">
    <div class="board-detail pt-5">
      <h1>글 작성</h1>
      <form @submit.prevent="createArtiecle">
        <div class="board-contents">
          <input type="text" v-model="title" class="w3-input w3-border" placeholder="제목을 입력해주세요.">
        </div>
        <div class="board-contents">
          <textarea id="" cols="30" rows="10" v-model="content" 
          placeholder="내용을 입력해주세요." class="w3-input w3-border" style="resize: none;">
          </textarea>
        </div>
        <div class="common-buttons">
          <button type="submit" class="w3-button w3-round w3-blue-gray">저장</button>&nbsp;
          <button type="button" class="w3-button w3-round w3-gray" v-on:click="articleList">목록</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreateArticle',
  data() {
    return {
      requestBody: this.$route.query,
      idx: this.$route.query.idx,

      title: null,
      content: null,
    }
  },
  methods: {
    createArtiecle() {
      const title = this.title
      const content = this.content

      this.$store.dispatch('createArticle', { title, content })
    },
    articleList() {
      delete this.requestBody.idx
      this.$router.push({name: 'community'})
    },
  }
}
</script>

<style>

</style>