<template>
  <div class="bg-gray">
    <div class="container">
      <br>
      <div>
        <button class="btn btn-danger" @click="AllToggle">Clear All</button>
      </div>
      <br>
      <span v-for="genreId in genreIds" :key="genreId.id">
        <button v-if="!isSelect(genreId.id)" class="btn btn-light btn-border-light mx-2 my-2" @click="genreSelect(genreId.id), getGenreMovie()">{{ genreId.name }}</button>
        <button v-if="isSelect(genreId.id)" class="btn btn-primary btn-border-light mx-2 my-2" @click="genreSelect(genreId.id), getGenreMovie()">{{ genreId.name }}</button>
      </span>

      <div class="row">
        <div class="col-2" v-for="movie in movies" :key="movie.id">
          <MovieDetailItem :movie="movie"/>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import MovieDetailItem from '@/components/MovieDetailComponent/MovieDetailItem.vue';

export default {
  components: {
    MovieDetailItem
  },
  data (){
    return {
      genreIds: [
        { id: 12, name: '모험'},
        { id: 14, name: '판타지'},
        { id: 16, name: '애니메이션'},
        { id: 18, name: '드라마'},
        { id: 27, name: '공포'},
        { id: 28, name: '액션'},
        { id: 35, name: '코미디'},
        { id: 36, name: '역사'},
        { id: 37, name: '서부'},
        { id: 53, name: '스릴러'},
        { id: 80, name: '범죄'},
        { id: 99, name: '다큐멘터리'},
        { id: 878, name: 'SF'},
        { id: 9648, name: '미스터리'},
        { id: 10402, name: '음악'},
        { id: 10749, name: '로맨스'},
        { id: 10751, name: '가족'},
        { id: 10752, name: '전쟁'},
        { id: 10770, name: 'TV 영화'},
      ],
      genres: [],
      movies: [],
    }
  },
  methods: {
    genreSelect(genreId) {
      if (this.genres.includes(genreId)) {
        this.genres.pop(this.genres.findIndex(element => {
          element == genreId}))
      } else {
        this.genres.push(genreId)
      }
      console.log(this.genres)
    },
    isSelect(genreId) {
      return this.genres.includes(genreId)
    },
    getGenreMovie() {
      if (this.genres.length == 0) {
        this.movies = []
      }

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/genre/`,
        params: {
          'genre': `${this.genres}`
        }
      })
      .then(res => {
        console.log(res)
        this.movies = res.data
      })
      .catch(error => {
        console.log(error)
      })
    },
    AllToggle() {
      this.genres = []
      this.getGenreMovie()
    }
  },
}
</script>

<style>

</style>