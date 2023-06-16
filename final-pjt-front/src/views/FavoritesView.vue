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
                  <div class="pb-2 pb-lg-0 mb-4 mb-lg-5">
                    <img id="profileimg" class="d-block rounded-circle mb-2" :src="`http://127.0.0.1:8000${user?.profile}`" 
                    data-fancybox data-src="#profile" width="80">
                    <div id="profile" style="display:none;width:70%; color:black;">
                      <h2 style="color:black;">프로필 변경</h2>
                      <div class="row">
                        <div class="col-4">
                          <img class="d-block rounded-circle mb-2" width="80" :src="`http://127.0.0.1:8000${user.profile}`">
                        </div>
                        <div class="col-7 row">
                          <img id="changeimg" class="col-2 d-block rounded mb-2 mx-2 px-3" width="100%" v-for="(image, index) in images" :key="index" 
                          :src="`http://127.0.0.1:8000/media/accounts/${image}.png`" @click="isSelect(image)" :class="{'isSelected': selectimg===image}">
                        </div>
                        
                        <div>
                          <button class="btn btn-success" @click="change_profile">프로필 변경</button>
                        </div>
                      </div>
                    </div>

                    <h3 class="h5 mb-1">{{ user.username }}</h3>
                    <p class="fs-sm text-muted mb-0">팔로잉 : {{ user.followings_count }}</p>
                    <p class="fs-sm text-muted mb-0"> 팔로워 : {{ user.follower_count }}</p>
                  </div>
                  <nav class="nav flex-column pb-2 pb-lg-4 mb-3">
                    <h4 class="fs-xs fw-medium text-muted text-uppercase pb-1 mb-2">Account</h4>
                      <span class="nav-link fw-semibold py-2 px-0" @click="changePassword"><i class="ai-settings fs-5 opacity-60 me-2"></i>Password Change</span>
                  </nav>
                  <div class="hr-container">
                    <hr>
                  </div>
                  <nav class="nav flex-column">
                    <a class="nav-link fw-semibold py-2 px-0" @click="signOut" href="">
                    <i class="ai-logout fs-5 opacity-60 me-2"></i>Sign out</a>

                    <a class="nav-link fw-semibold py-2 px-0" style="color:orangered;" @click="deleteUser" href="">
                    <i class="ai-delete fs-5 opacity-60 me-2"></i>회원 탈퇴</a>
                  </nav>
                </div>
              </div>
            </div>
          </aside>
          <!-- Page content-->
          <div class="col-lg-9 pt-4 pb-2 pb-sm-4">
            <div class="d-flex align-items-center mb-4">
              <h1 class="h2 mb-0">관심있는 영화 <span class='fs-base fw-normal text-muted'>{{ likeMovies.length }}개</span></h1>
              <button class="btn btn-sm btn-outline-danger ms-auto" type="button" @click="clearAll"><i class="ai-trash ms-n1 me-2"></i>Clear all</button>
            </div>
            <div class="card border-0 py-1 p-md-2 p-xl-3 p-xxl-4">
              <div class="card-body pb-4">
                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
                  <!-- Item-->
                  <div class="col pb-2 pb-sm-3" v-for="movie in likeMovies" :key="movie.id">
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
  data() {
    return {
      user: null,
      images: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      selectimg: null,
    }
  },
  components: {
    MovieDetailItem
  },
  methods: {
    getUserInfo() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/mypage/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        console.log(res.data)
        this.user = res.data
      })
      .catch(error => {
        console.log(error)
      })
    },
    gotoDetail(movieId) {
      this.$router.push({name: 'MovieDetailView', params: {movieId: `${movieId}`}})
    },
    clearAll() {
      this.$store.dispatch('clearAll')
    },
    signOut() {
      if (!confirm("로그아웃 하시겠습니까?")) return
      this.$store.dispatch('signOut')
    },
    deleteUser() {
      if (!confirm("회원탈퇴 하시겠습니까?")) return
      this.$store.dispatch('deleteUser')
    },
    changePassword() {
      this.$router.push({name: 'ChangePassword'})
    },
    isSelect(imgId) {
      if (this.selectimg === imgId) {
        this.selectimg = null
        return
      }

      this.selectimg = imgId
    },
    change_profile() {
      if (!this.selectimg) {
        alert('바꿀 이미지를 선택해주세요')
      } 

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/profile_change/${this.selectimg}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        console.log(res)
        this.$router.go(this.$router.currentRoute)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created() {
    this.getUserInfo()
  },
  computed: {
    likeMovies() {
      return this.user.rated_movies.filter(movie => {
        return this.$store.getters.likeMovies.includes(movie.id)
      })
    }
  }
}
</script>

<style>
  #profileimg:hover {
    border: 2px solid white;
    margin-bottom: 4px;
  }

  #changeimg:hover {
    border: 2px solid black;
    margin-bottom: 4px;
  }

  .isSelected {
    border: 2px solid black;
    margin-bottom: 4px;
  }
  .hr-container {
  margin-right: 100px;
}
</style>