<template>
  <div>
    <h1>movie Comment</h1>
      <div v-for="comment in comments" :key="comment.id">
        <div v-if="isUpdate">  
          <p>작성자 : {{ comment.user.username }}</p>
          <p>내용 : {{ comment.content }}</p>
          <star-rating :star-size="25" :border-width="2" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" 
          :rating="comment.rating" :read-only="true" :inline="true" :increment="0.5"></star-rating>
          <br>
          <div class="mt-2" v-if="comment.user.username === $store.state.username">
            <button class="btn btn-success mx-1" @click="updateToggle(comment.content, comment.rating)">수정</button>
            <button class="btn btn-danger mx-1" @click="deleteComment(comment.id)">삭제</button>
          </div>
        </div>
        <form v-else @submit.prevent="updateComment(comment.id)">
          <div class="input-group mb-3 ">
            <input type="text" class="text-white bg-dark form-control" v-model="currentContent"
            aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
            <star-rating :border-width="3" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
              :inline="true" :increment="0.5" :star-size="30" :show-rating="false" v-model="currentRating"></star-rating>
            <button type="submit" class="mx-1 rounded btn bg-success text-white" id="inputGroup-sizing-default">
              작성</button>
            <button @click="updateToggle('', '')" type="submit" class=" btn rounded bg-secondary mx-1 text-white" id="inputGroup-sizing-default">
            취소</button>
          </div>
        </form>

        <hr>
      </div>
      <form v-if="!isComment" @submit.prevent="createComment()">
        <div class="input-group mb-3 ">
          <input type="text" class="text-white bg-dark form-control" v-model="content"
          aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
          <star-rating :border-width="3" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
            :inline="true" :increment="0.5" :star-size="30" :show-rating="false" v-model="rating"></star-rating>
          <button type="submit" class="mx-1 btn bg-primary text-white" id="inputGroup-sizing-default">
            작성</button>
        </div>
      </form>
      <h3 v-else>이미 리뷰를 작성했습니다.</h3>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

export default {
  name: 'MovieComment',
  props: {
    movieComments: Array,
    movieId: Number
  },
  components: {
    StarRating
  },
  data() {
    return {
      comments: [],
      content: null,
      rating: null,
      userCommentId: null,
      total: 0,
      isUpdate: true,

      currentContent: null,
      currentRating: null,

    }
  },
  methods: {
    getstart() {
      this.comments = this.movieComments
    },
    createComment() {
      if (!this.content || !this.rating) {
        return alert('평점과 내용을 입력하세요!')
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movieId}/comments/`,
        data: {
          content: this.content,
          rating: this.rating
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}` 
        }
      })
      .then(res => {
        this.comments.push(res.data)
        this.content = null
        this.rating = null
        this.comments.forEach(comment => {
          this.total += comment.rating
        })
        if (this.total === 0.0) {
          this.$emit('rating', 0.0)
          return
        } 
        this.$emit('rating', (this.total/this.comments.length).toFixed(1))
      })
      .catch(error => {
        console.log(error)
      })
    },
    updateToggle(content, rating) {
      this.isUpdate = !this.isUpdate
      this.currentContent = content
      this.currentRating = rating
    },
    updateComment(commentId) {
      if (!this.currentContent || !this.currentRating) {
        return alert('평점과 내용을 입력하세요!')
      }
      console.log(this.currentContent, this.currentRating)
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movies/comment/comment_fix/${commentId}/`,
        data: {
          content: this.currentContent,
          rating: this.currentRating
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}` 
        }
      })
      .then(res => {
        console.log(res.data)
        this.comments = this.comments.map(comment => {
          if (comment.id == commentId) {
            comment = res.data
          }
          return comment
        })
        this.currentContent = null
        this.currentRating = null
        this.total = 0.0
        this.comments.forEach(comment => {
          this.total += comment.rating
        })
        if (this.total === 0) {
          this.$emit('rating', 0.0)
          return
        } 
        this.$emit('rating', (this.total/this.comments.length).toFixed(1))
        this.updateToggle()
      })
      .catch(error => {
        console.log(error)
      })
    },
    deleteComment(commentId) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/comment/comment_fix/${commentId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}` 
        }
      })
      .then(res => {
        console.log(res)
        this.comments = this.comments.filter(comment => {
          return comment.id != commentId
        })
        this.currentContent = null
        this.currentRating = null
        this.total = 0
        this.comments.forEach(comment => {
          this.total += comment.rating
        })
        if (this.total === 0) {
          this.$emit('rating', 0)
          return
        } 
        this.$emit('rating', (this.total/this.comments.length).toFixed(1))
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created() {
    this.getstart()
  },
  computed: {
    isComment() {
      return this.comments.some(comment => {
        return comment.user.username === this.$store.state.username
      })
    },
  }
}
</script>

<style >

</style>