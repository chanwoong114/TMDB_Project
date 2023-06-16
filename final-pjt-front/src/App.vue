<template>
  
  <div id="app">
    <div class="bg-gray" >
      <div>
        <header class="navbar bg-navb navbar-expand-lg fixed-top" style="opacity: 1;" >
          
          <div class="container"><a class="navbar-brand pe-sm-3 with-outline" :href="`http://localhost:8080/`">
            <img src="./assets/logo.png"  alt="Logo" width="50" height="50">
            HIVE
          </a>
          <!-- 검색 -->
          
          
          <div class="form-check form-switch mode-switch order-lg-2 me-3 me-lg-4 ms-auto" data-bs-toggle="mode">
            <input class="form-check-input" type="checkbox" id="theme-mode" v-model="darkMode" @click="toggleDarkMode()">
            <label class="form-check-label" for="theme-mode"><i class="ai-sun fs-lg"></i></label>
            <label class="form-check-label" for="theme-mode"><i class="ai-moon fs-lg"></i></label>
          </div>
          
          <!-- 로그인버튼 -->
          <!-- 로그인이면 마이페이지 아니면 로그인 -->
          <div v-if="!isLogin" class="btn btn-success btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex " target="_blank" rel="noopener" >
            <i class="ai-login fs-xl me-2 ms-n1"></i><router-link class="nav-link" to="/login">로그인</router-link>
          </div>
          <div v-if="isLogin" class="btn btn-success btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex"  target="_blank" rel="noopener" >
            <i class="ai-login fs-xl me-2 ms-n1"></i><router-link class="nav-link" to="/favorites">마이페이지</router-link>
          </div>

          
          <!-- 영화추천 -->
          <nav class="collapse navbar-collapse" id="navbarNav" >
            <ul class="navbar-nav navbar-nav-scroll me-auto " style="--ar-scroll-height: 520px;">
              <li class="nav-item dropdown "><a class="nav-link dropdown-toggle active with-outline" href="#" data-bs-toggle="dropdown" aria-expanded="false">영화</a>
                <div class="dropdown-menu overflow-hidden p-0 ">
                  <div class="d-lg-flex bg-white">
                    <div class="mega-dropdown-column pt-1 pt-lg-3 pb-lg-4">
                      <ul class="list-unstyled mb-0">
                        
                        <li><router-link class="dropdown-item with-outline" to="/movies">영화추천</router-link>
                          <span class="mega-dropdown-column position-absolute top-0 end-0 h-100 bg-size-cover bg-repeat-0 zindex-2 opacity-0" style="background-image: url(assets/img/megamenu/영화추천1.png)"></span></li>
                        <li><router-link class="dropdown-item with-outline" to="/genre">장르별 영화</router-link>
                          <span class="mega-dropdown-column position-absolute top-0 end-0 h-100 bg-size-cover bg-repeat-0 zindex-2 opacity-0" style="background-image: url(assets/img/megamenu/장르별.png)"></span></li>  
                        </ul>
                      </div>
                      <div class="mega-dropdown-column position-relative border-start zindex-3"></div>
                    </div>
                  </div>
                </li>
                  <!-- 게시판,마이페이지 -->
                  <li class="nav-item"><router-link class="nav-link with-outline" to="/community">게시판</router-link></li>
                  <!-- <li class="nav-item"><a class="nav-link" href="docs/getting-started.html">마이페이지</a></li> -->
                </ul>
                <!-- 검색 돋보기 -->
                <form class="d-flex ms-auto">
                  <button class="btn btn-outline-success" type="submit" @click="gotoSearch">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                      <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                    </svg>
                  </button>
                </form>
              </nav>
            </div>
        </header>
        <!-- 네브바-->
        
        <!-- 네브바2 -->
        <header class="position-relative navbar bg-gray navbar-expand-lg" style="opacity: 0;" >
          
          <div class="container"><a class="navbar-brand pe-sm-3" :href="`http://localhost:8080/movies`">
            <img src="./assets/bighive.png"  alt="Logo" width="35" height="32">
            HIVE
            </a>
            <div class="form-check form-switch mode-switch order-lg-2 me-3 me-lg-4 ms-auto" data-bs-toggle="mode">
              <input class="form-check-input" type="checkbox" id="theme-mode" v-model="darkMode" @click="toggleDarkMode()">
              <label class="form-check-label" for="theme-mode"><i class="ai-sun fs-lg"></i></label>
              <label class="form-check-label" for="theme-mode"><i class="ai-moon fs-lg"></i></label>
            </div>

            <!-- 로그인버튼 -->
            <!-- 로그인이면 마이페이지 아니면 로그인 -->
            <div v-if="!isLogin" class="btn btn-success btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex" target="_blank" rel="noopener" >
            <router-link class="nav-link" to="/login"><i class="ai-login fs-xl me-2 ms-n1"></i>로그인</router-link>
            </div>
            <div v-if="isLogin" class="btn btn-success btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex"  target="_blank" rel="noopener" >
            <router-link class="nav-link" :to="{name: 'FavoritesView'}">
            <i class="ai-login fs-xl me-2 ms-n1"></i>마이페이지</router-link>
            </div>
         
         
            <!-- 영화추천 -->
            <nav class="collapse navbar-collapse" id="navbarNav" >
              <ul class="navbar-nav navbar-nav-scroll me-auto " style="--ar-scroll-height: 520px;">
                <li class="nav-item dropdown "><a class="sex nav-link dropdown-toggle active" href="#" data-bs-toggle="dropdown" aria-expanded="false">영화</a>
                  <div class="dropdown-menu overflow-hidden p-0 ">
                    <div class="d-lg-flex bg-white">
                      <div class="mega-dropdown-column pt-1 pt-lg-3 pb-lg-4">
                        <ul class="list-unstyled mb-0">
                          <li><router-link class="sex dropdown-item" to="/movies">영화추천</router-link>
                            <span class="mega-dropdown-column position-absolute top-0 end-0 h- bg-size-cover bg-repeat-0 rounded-3 rounded-start-0" style="background-image: url(assets/img/megamenu/bee.png)"></span></li>
                          <li><router-link class="sex dropdown-item" to="/genre">장르별 영화</router-link>
                            <span class="mega-dropdown-column position-absolute top-0 end-0 h-100 bg-size-cover bg-repeat-0 zindex-2 opacity-0" style="background-image: url(assets/img/megamenu/C.png)"></span></li>  
                        </ul>
                      </div>
                      <div class="mega-dropdown-column position-relative border-start zindex-3"></div>
                    </div>
                  </div>
                </li>
                
     
                
                
                <!-- 게시판,마이페이지 -->
                <li class="nav-item"><router-link class="nav-link" to="/community">게시판</router-link></li>
                <!-- <li class="nav-item"><a class="nav-link" href="docs/getting-started.html">마이페이지</a></li> -->
              </ul>
            
            </nav>
          </div>
        </header>
      </div>
    </div>
    <router-view style="min-height: 90vh" class="pt-2 pb-2"/>
    
    <footer class="footer py-2 fixed-bottom">
      <div class="container text-center py-3">
        <span class="text-muted"> 123213213131 </span>
        <a class="nav-link d-inline p-0" style="color:black;" href="#" target="_blank">Team HIVE</a>
      </div>
    </footer>
  </div>
</template>
<script>
export default {
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    darkMode() {
      return this.$store.getters.isDarkMode
    }
  },
  methods:{
    toggleDarkMode() {
      this.$store.dispatch('toggleDarkMode')

      if (this.$store.state.darkMode) {
        // 다크 모드 클래스를 추가
        document.body.classList.add('dark-mode')
      } else {
        // 다크 모드 클래스를 제거
        document.body.classList.remove('dark-mode')
      }
    },
   
    gotoLogin() {
      this.$router.push({name: 'LogInView'})
    },

    gotoSearch(){
      this.$router.push({name: 'SearchView'})
    },

    gotoHome() {
      this.$router.push({name: 'HomeView'})
    }
    
  },
  created() {
    if (this.$store.state.darkMode) {
        // 다크 모드 클래스를 추가
        document.body.classList.add('dark-mode')
      } else {
        // 다크 모드 클래스를 제거
        document.body.classList.remove('dark-mode')
      }
  }
  // watch: {
  //   $route() {
  //     window.scrollTo(0, 0);
  //   },
  // },
}
</script>
<style>


  @import url("//fonts.googleapis.com/earlyaccess/nanumgothic.css" );
  input[type=password] {
    font-family:"Nanum Gothic", sans-serif !important;
    color: black;
  }
  @font-face {
    font-family: 'dohyeon';
    src: url('../public/font/BMDOHYEON_ttf.ttf');
  }

  @font-face {
    font-family: 'jua';
    src: url('../public/font/BMJUA_ttf.ttf');
  }

#app {
  font-family: 'jua';
  /* style="--ar-gray-900: var(--ar-gray-900); color: var(--ar-gray-900);" */
  
}

nav {
  padding: 20px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: black;
}

.hive {
  width: 130px;
  height: 90px;
}
h1 {
  font-family: 'jua';
}

h2 {
  font-family: 'jua';
}

h3 {
  font-family: 'jua';
}

.navcolor{
  color: var(--ar-teal)!important;
}

h4 {
  font-family: 'jua';
}

  input[type=password]::placeholder {
    font-family: "jua"; 
  }

#video-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1; /* Ensure the video is behind the content */
}
  #zoom {
    position: relative;
    border-radius: 3%;
  }

  #zoom:hover {
    transform: scale(2);
    transition: 0.5s;
    z-index: 1;
    border-radius: 3%;
  }
  
  .card-img {
    height: 100%;
    object-fit: cover;
  }

  .backgroundimg {
    border-radius: 5%;
    height: 100%
  }

  #zoom:hover > .backgroundimg {
    opacity: 0.3;
  }

  .mainimg {
    position: absolute;
    opacity: 0;
    display: none;
  }

  #movieInfo {
    position: absolute;
    opacity: 0;
    display: none;
  }

  #title {
    position: absolute;
    opacity: 0;
    display: none;
  }

  #zoom:hover > .mainimg {
    display: inline;
    opacity: 1;
    width: 40%;
    top: 15%;
    left: 10%
  }

  #zoom:hover > #movieInfo {
    display: inline;
    opacity: 1;
    top: 15%;
    left: 60%;
    font-size: 4px;
    color: #fff;
  }

  #zoom:hover > #title {
    display: inline;
    opacity: 1;
    top: 90%;
    text-align: center;
    width: 60%;
    font-size: 8px;
    left: 20%;
    color: #FFD963;
    font-weight: bold;
  }

  #liked {
    display: none;
    position: absolute;
    opacity: 0;
  }

  #zoom:hover > #liked {
    display: inline;
    opacity: 1;
    top: 70%;
    text-align: center;
    width: 60%;
    font-size: 8px;
    left: 20%;
  }
  .with-outline {
  text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
}
  #zoom:hover > #liked:active {
    transform: scale(1.2);
    transition: 0.3s;
  }

  #pointer {
    cursor: pointer;
  }

  footer {
    height: 3%;
  }

  .bg-navb {
    background: rgb(54, 54, 54) !important;
    opacity: 1 !important;
  }

  .dark-mode .bg-navb {
    background: white !important;
    opacity: 1 !important;
  }

  .dark-mode .navtext {
    color: white;
  }

  .personBox {
    position: relative;
  }

  .personBox:hover #personimg {
    opacity: 0.5;
    border: 2px solid;
    border-color:white;
    margin-bottom: 2px;
  }

  .personBox:hover #cardbox {
    opacity: 1;
  }

  #personP {
    display: none;
    color: white;
  }

  .personBox:hover #personP {
    position: absolute;
    left: 8%;
    top: 0%;
    display: inline;
  }

  #area {
  /* absolute는 부모가 relative일 때 부모를 따라간다. */
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 비율 */
  position: absolute; 
  top:0%; 
  left: 0%; 
  z-index: -1;
  }

  #video {
    position: absolute;
    width: 100%; /* 부모에 맞게 꽉 채운다. */
    height: 100%;
    opacity: 0.5;
  }

  .selected {
    color: #FFD963;
    font-weight: bold;
  }
  .video-container {
  position: absolute;
  top: 18%;
  left: 50px; /* Adjust this value as needed */
  transform: translateY(-50%);
}
  
</style>
