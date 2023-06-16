<template>
  <div class="bg-gray">
    <div class="container">
      <br>
      <h1>영화 검색</h1>
      <div class="pb-3 mb-3">
        
        <div class="position-relative">
          <input class="form-control form-control-lg ps-5" type="email" v-model.trim="searchWord" placeholder="제목을 입력하세요" required>
        </div>
      </div>
      <br><br><br><br>
      <div>
        <h3>{{ searchWord }} 을/를 검색한 결과입니다.</h3>
        <div class="row row-cols-6">
          <MovieDetailItem class="col" v-for="movie in searchMovie" :key="movie.id" :movie="movie"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailItem from '@/components/MovieDetailComponent/MovieDetailItem.vue'

export default {
  name: 'SearchView',
  components: {
    MovieDetailItem
  },
  data() {
    return {
      movies: [],
      searchWord: '',
    }
  },
  methods: {
    getmovies() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/all/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        console.log(res.data)
        this.movies = res.data
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created() {
    this.getmovies()
  },
  computed: {
    searchMovie() {
      if (this.searchWord.length < 1) {
        return []
      } else
      return this.movies.filter(movie => {
        return movie.title.includes(this.searchWord)
      })
    }
  }
}
</script>

<style>

</style>