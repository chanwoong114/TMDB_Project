<template>
  <div class="bg-gray">

    <!-- <form @submit.prevent="login">
      <label for="username"></label><br>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> </label><br>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
    <button @click="gotoSignup()">Sign Up</button> -->

      <!-- Page content-->
      <div class="d-lg-flex position-relative bg-gray">
        <!-- Sign in form-->
        
        <div class="board-list d-flex flex-column align-items-center mx-auto w-lg-50 h-100 px-3 px-lg-5">
          <div class="card-lifted overflow-hidden rounded-3 "><img class="d-dark-mode-none" src="../assets/logo.png"><img class="d-none d-dark-mode-block" src="../assets/logo.png"></div>
      
          <h1>로그인</h1>
          <div class="w-100 mt-auto" style="max-width: 526px;">
            
            <form class="needs-validation" novalidate @submit.prevent="login()">
              <div class="pb-3 mb-3">
        
                <div class="position-relative"><i class="fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
                  <input class="form-control form-control-lg ps-5" type="email" v-model="username" placeholder="아이디" required>
                </div>
              </div>
              <div class="mb-4">
                <div class="position-relative"><i class=" fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
                  <div class="password-toggle">
                    <input class="form-control form-control-lg ps-5"  type="password" v-model="password" placeholder="비밀번호" required>
                  </div>
                </div>
              </div>
              
              <button class="btn btn-lg btn-success  w-100 mb-4" type="submit">로그인</button>
              <button class="btn btn-lg btn-success w-100 mb-4" type="submit" @click="gotoSignup()">회원가입</button>
              
            </form>
          </div>
          <!-- Copyright-->
          <p class="w-100 fs-sm pt-5 mt-auto mb-5" style="max-width: 526px;"><span class="text-muted">&copy; Made by</span><a class="nav-link d-inline-block p-0 ms-1" href="https://createx.studio/" target="_blank" rel="noopener">TEAM HIVE</a></p>
        </div>
        <!-- Cover image-->
        <!-- <div class="w-50 bg-size-cover bg-repeat-0 bg-position-center" style="background-image: url(assets/hive.png);"></div> -->
      </div>
   
     
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    },
    gotoSignup() {
      this.$router.push({name: 'SignUpView'})
    }
  },
  
}
</script>
<style scoped>
.board-list {
    border: solid var(--ar-gray-900);
    border-radius: 20px;
    margin: 5px;
    
  }
img {
    position: relative;
    z-index: -1;
}

</style>