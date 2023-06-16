<template>
  <div class="bg-gray pb-5">
    <h1 style="padding: 30px;">HIVE 추천 영화</h1>
    <PosterSlide :movies="movies?.user_data" :num="1"/>
    <h1 style="padding: 30px;">죽기전 꼭봐야하는 영화</h1>
    <PosterSlide :movies="movies?.weight_data" :num="2"/>
    <h1 style="padding: 30px;">오늘 이거 어때요?</h1>
    <PosterSlide :movies="movies?.random_data" :num="3"/>
  </div>
</template>


<script>
import axios from 'axios'
// import { Carousel } from "@fancyapps/ui/dist/carousel/carousel.esm.js";
// import "@fancyapps/ui/dist/carousel/carousel.css";
import PosterSlide from '@/components/PosterSlide.vue';

export default {
  name: 'MovieView',
  components: {
    PosterSlide,
  },
  data() {
    return {
      API_URL: 'http://localhost:8000',
      movies: {}
    }
  },
  methods: {
    movieList(){
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        this.movies = res.data
      })
      .catch(error => {
        console.log(error)
      })
    },
    gotoDetail(movieId) {
      this.$router.push({name: 'MovieDetailView', params: {movieId: `${movieId}`}})
    }
  },
  computed: {
    isMovie() {
      return this.movies.length != 0
    }
  },
  created() {
    this.movieList()
  }
}
</script>

<style>
</style>
