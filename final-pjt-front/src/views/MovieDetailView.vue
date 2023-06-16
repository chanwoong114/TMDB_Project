<template>
  <div>

    <div style="position: relative">
      <div style="min-height: 80vh; ">
        <div v-if="URL" id="area" style="">
          <iframe id="video" v-if="isURL" :src="`https://youtube.com/embed/?autoplay=1&mute=1&controls=0&playlist=${URL}&loop=1`" frameborder="0"
          style="position: absolute; top:-5%; left: 0%; z-index: -2;" ></iframe>
        </div>
        <div class="container video-container" >
          <div class="row" >
            <div class="col-md-6 col-12" style="color: white;" >
              <h1 style="text-align: start; color: white;" >{{ movie?.title }}</h1>
              <br>
              <div class="row">
                <img class="col-md-4 col-2"  :src="`https://image.tmdb.org/t/p/original/${movie?.poster_path}`" width="50%" alt="">
                <div class="col-8">
                  <p style="color: white;">평점 : {{ rating }}</p>
                  <p style="color: white;">좋아요 수 : {{ likeCount }}</p>
                
                  <div @click="movieLike">
                    <svg style="color: tomato;" v-if="liked" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-suit-heart-fill" viewBox="0 0 16 16">
                      <path d="M4 1c2.21 0 4 1.755 4 3.92C8 2.755 9.79 1 12 1s4 1.755 4 3.92c0 3.263-3.234 4.414-7.608 9.608a.513.513 0 0 1-.784 0C3.234 9.334 0 8.183 0 4.92 0 2.755 1.79 1 4 1z"/>
                    </svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-suit-heart" viewBox="0 0 16 16">
                      <path d="m8 6.236-.894-1.789c-.222-.443-.607-1.08-1.152-1.595C5.418 2.345 4.776 2 4 2 2.324 2 1 3.326 1 4.92c0 1.211.554 2.066 1.868 3.37.337.334.721.695 1.146 1.093C5.122 10.423 6.5 11.717 8 13.447c1.5-1.73 2.878-3.024 3.986-4.064.425-.398.81-.76 1.146-1.093C14.446 6.986 15 6.131 15 4.92 15 3.326 13.676 2 12 2c-.777 0-1.418.345-1.954.852-.545.515-.93 1.152-1.152 1.595L8 6.236zm.392 8.292a.513.513 0 0 1-.784 0c-1.601-1.902-3.05-3.262-4.243-4.381C1.3 8.208 0 6.989 0 4.92 0 2.755 1.79 1 4 1c1.6 0 2.719 1.05 3.404 2.008.26.365.458.716.596.992a7.55 7.55 0 0 1 .596-.992C9.281 2.049 10.4 1 12 1c2.21 0 4 1.755 4 3.92 0 2.069-1.3 3.288-3.365 5.227-1.193 1.12-2.642 2.48-4.243 4.38z"/>
                    </svg>
                  </div>
                  <br>
                  <p style="color: white;">줄거리 : {{ movie?.overview }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>

    
    <div class="bg-gray" style="text-align: center; " >
      <div class="container pt-5 pb-5" >
          <span style="font-size:xx-large;">
            <span id="pointer" @click="selectContentToggle(0)" :class="{'selected': selectContent===0}">연관 추천 영화</span> &nbsp;
            <span><strong>|</strong></span>&nbsp;&nbsp;
            <span id="pointer" @click="selectContentToggle(1)" :class="{'selected': selectContent===1}">출연진</span>&nbsp;
            <span><strong>|</strong></span>&nbsp;&nbsp;
            <span id="pointer" @click="selectContentToggle(2)" :class="{'selected': selectContent===2}">리뷰</span>
          </span>
          <h3 v-if="selectContent===0 && movie?.recommend_movies.length === 0">관련 영화가 없습니다...</h3>
          <div v-if="selectContent===0" class="row row-cols-3 row-cols-md-6 g-2 mx-auto pt-5">
            <div class="col container"  v-for="(recommendMovie, index) in movie?.recommend_movies" :key="index">
              <MovieDetailItem  :movie="recommendMovie"/>
            </div>
          </div>
      
          
          <div class="d-flex-column justify-content-between" v-if="selectContent===1">
            <h4 class="text-start">감독</h4>
            <br>
            <div style="width: 16%;">
              <a class="personBox" href="" data-fancybox @click="trigger('crew', movie?.crew_ids.id)" style="width: 16%;" data-src="#crew-content">
                <img id="personimg" :src="`https://image.tmdb.org/t/p/original/${movie?.crew_ids.profile_path}`" width="200" class="rounded-2" alt="">
                <p id="personP">{{ movie?.crew_ids.name }}</p>
              </a>
              <div id="crew-content" style="display:none;width:70%;">
                <h1 style="color:black;">{{ movie?.crew_ids.name }}</h1>
                <br>
                <br>
                <h3 style="color:black;">제작한 영화</h3>
                <div id="cardbox" class="row mx-auto">
                  <MovieDetailItem class="col-2 rounded" v-for="(crewMovie, index) in personMovie" :key="index" :movie="crewMovie"/>
                </div>
              </div>
            </div>
            <br>

            <h4 class="text-start">출연진</h4>
            <br>
            <div class="row text-start" >
              <div class="col" v-for="cast in movie?.cast_ids" :key="cast?.id">
                <a class="personBox" href="" data-fancybox @click="trigger('cast', cast?.id)" :data-src="`#${cast?.id}`">
                  <img id="personimg" :src="`https://image.tmdb.org/t/p/original/${cast?.profile_path}`" width="200" class="rounded-2" alt="">
                  <p id="personP">{{ cast?.name }}</p>
                </a>
                <div :id="cast.id" style="display:none;width:70%;">
                  <h1 style="color:black;">{{ cast?.name }}</h1>
                  <br>
                  <br>
                  <h3 style="color:black;">참여한 영화</h3>
                  <div class="row">
                    <div class="col-2" v-for="(castMovie, index) in personMovie" :key="index">
                      <MovieDetailItem class="rounded" :movie="castMovie"/>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="pt-5" v-if="selectContent===2">
            <MovieComment :movieComments="movie?.comments" :movieId="movie?.id"
            @rating="ratingSet"/>
          </div>
          
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import MovieDetailItem from '@/components/MovieDetailComponent/MovieDetailItem.vue';
import axios from 'axios';
import MovieComment from '../components/MovieDetailComponent/MovieComment.vue';


export default {
  name: 'MovieDetailView',
  components: {
    MovieDetailItem,
    MovieComment,
  },
  data() {
    return {
      movie: null,
      personMovie: null,
      API_URL: 'http://127.0.0.1:8000',
      liked: null, 
      likeCount: null,
      URL: 'N7uu8v34HU8',
      selectContent: 0,
      rating: 0,
      isURL: false
    }
  },
  methods: {
    loadMovieDetail() {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/${this.$route.params.movieId}/`
      })
      .then(res => {
        this.movie = res.data
        this.likeCount = res.data.Like_users_count
        this.rating = res.data.comments_rating.toFixed(1)
      })
      .catch(error => {
        console.log(error)
      })
    },
    gotoDetail(movieId) {
      this.$router.push({name: 'MovieDetailView', params: {movieId: `${movieId}`}})
    },
    trigger(job, id) {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/${job}/${id}/`,
      })
      .then(res => {
        this.personMovie = res.data
        console.log(this.personMovie)
      })
      .catch(error => {
        console.log(error)
      })
    },
    reload() {
      this.$router.go(this.$router.currentRoute)
    },
    loadUrl() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.movieId}/videos?language=ko-KR/`,
        params: {
          api_key: 'c0277ff053c36cf743bb896821c5f0f1'
        }
      })
      .then(res => {
        if (res.data.results.length > 0) {
          this.URL = res.data.results[0].key
        }
        res.data.results.forEach(result => {
          if (result.type=="Trailer") {
            this.URL = result.key
          }
        })
        this.isURL = true
      })
      .catch(error => {
        console.log(error)
      })
    },
    movieLike() {
      this.$store.dispatch('movieLike', [this.movie.id, !this.liked])
      if (this.liked) {
        this.likeCount -= 1
      } else {
        this.likeCount += 1
      }
      this.liked = !this.liked
  
    },
    isLike() {
      this.liked = this.$store.state.movie.rated_movies.includes(parseInt(`${this.$route.params.movieId}`))
    },
    selectContentToggle(num) {
      this.selectContent = num
    },
    ratingSet(num) {
      this.rating = num
    }
  },
  created() {
    this.loadMovieDetail()
    this.loadUrl()
    this.isLike()
    
  },
  mounted() {
  },
}
</script>

<style scoped>
  /* #posterimg {
    position: absolute;
    left: 0%;
    z-index: 1;
    opacity: 0.2;
  }

  div {
    z-index: 2;
  }

  a {
    z-index: 2;
  } */



</style>