<template>
  <div class="bg-gray">
    <div class="container py-5 mt-4 mt-lg-5 mb-lg-4 my-xl-5">
      <div class="row pt-sm-2 pt-lg-0">
        <!-- 프로필 바 사진은 992px)-->
        <aside class="col-lg-3 pe-lg-4 pe-xl-5 mt-n3">
          <div class="position-lg-sticky top-0">
            <div class="d-none d-lg-block" style="padding-top: 105px;"></div>
            <div class="offcanvas-lg offcanvas-start" id="sidebarAccount">
              <button class="btn-close position-absolute top-0 end-0 mt-3 me-3 d-lg-none" type="button" data-bs-dismiss="offcanvas" data-bs-target="#sidebarAccount"></button>
              <div class="offcanvas-body">
                <div class="pb-2 pb-lg-0 mb-4 mb-lg-5"><img class="d-block rounded-circle mb-2" :src="`http://127.0.0.1:8000${user?.profile}`" width="80">
                  <h3 class="h5 mb-1">{{ user?.username }}</h3>
                  <p class="fs-sm text-muted mb-0">팔로잉 : {{ user?.followings_count }}</p>
                  <p class="fs-sm text-muted mb-0"> 팔로워 : {{ follower_count }}</p>
                  <br>
                  <span type="button" v-if="!isFollow" @click="follow" class="fs-sm btn btn-outline-primary py-2 px-0 " style="width: 50%;">
                    팔로우
                  </span>
                  <span v-else @click="follow" class="fs-sm btn btn-outline-danger py-2 px-0 " style="width: 50%;">
                    언팔로우
                  </span>
                </div>
              </div>
            </div>
          </div>
        </aside>
        <!-- Page content-->
        <div class="col-lg-9 pt-4 pb-2 pb-sm-4">
          <div class="d-flex align-items-center mb-4">
            <h1 class="h2 mb-0">관심있는 영화 <span class='fs-base fw-normal text-muted'>{{ user?.rated_movies.length }}개</span></h1>
          </div>
          <div class="card border-0 py-1 p-md-2 p-xl-3 p-xxl-4">
            <div class="card-body pb-4">
              <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
                
                <div class="col pb-2 pb-sm-3" v-for="movie in user?.rated_movies" :key="movie.id">
                  <MovieDetailItem :movie="movie" />
                  <div class="d-flex mb-1">
                    <h3 class="h6 mb-0"><a href="#">{{ movie.title }}</a></h3>
                    <div class="d-flex ps-2 mt-n1 ms-auto">
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailItem from '@/components/MovieDetailComponent/MovieDetailItem.vue'

export default {
  name: 'UserPage',
  components: {
    MovieDetailItem
  },
  data() {
    return {
      user: null,
      follower_count: null,
    }
  },
  methods: {
    getUserInfo() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/username/${this.$route.params.username}/`,
        headers: `Token ${this.$store.state.token}`
      })
      .then(res => {
        console.log(res)
        this.user = res.data
        this.follower_count = res.data.follower_count
      })
      .catch(error => {
        console.log(error)
      })
    },
    gotoDetail(movieId) {
      this.$router.push({name: 'MovieDetailView', params: {movieId: `${movieId}`}})
    },
    follow() {
      if (this.$store.state.username == this.user.username) return

      if (this.$store.state.likeUsers.includes(this.user.id)) {
        this.follower_count -= 1
      } else {
        this.follower_count += 1
      }

      this.$store.dispatch('follow', this.user.id)
    }
  },
  created() {
    this.getUserInfo()
  },
  computed: {
    isFollow() {
      return this.$store.state.likeUsers.includes(this.user.id)
    }
  }
}
</script>

<style scoped>

</style>