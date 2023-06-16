<template>
  <div class="bg-gray">
    <!-- <div class="box">
    <h1>회원 가입</h1>
    <form @submit.prevent="signUp">
      <label for="username" style="text-align: left;">아이디</label>
      <br>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> 비밀번호</label>
      <br>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> 비밀번호 확인 </label>
      <br>
      <input type="password" id="password2" v-model="password2">
      <br>
      <input type="submit" value="SignUp">
      
    </form>
    </div> -->
  <main class="page-wrapper">
  <!-- Page content-->
  <div class=" d-lg-flex position-relative bg-gray">
    <!-- Sign in form-->
    
    <div class="board-list d-flex flex-column align-items-center mx-auto w-lg-50 h-100 px-3 px-lg-5"> 
      <div class="card-lifted overflow-hidden rounded-3"><img class="d-dark-mode-none" src="../assets/logo.png"><img class="d-none d-dark-mode-block" src="../assets/logo.png"></div>
      <H1>회원가입</H1>
      <div class="w-100 mt-auto" style="max-width: 526px;">
        <form class="needs-validation" @submit.prevent="signUp" novalidate>
          <div class="pb-3 mb-3">
            <div class="position-relative"><i class="ai-mail fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
              <input class="form-control form-control-lg ps-5" v-model="username" type="email" placeholder="아이디" required>
            </div>
          </div>
          <div class="mb-4">
            <div style="color:gray" class="position-relative"><i  class="ai-lock-closed fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
              <div class="password-toggle">
                <input class="form-control form-control-lg ps-5" v-model="password1" type="password" placeholder="비밀번호" required>
                <label class="password-toggle-btn" aria-label="Show/hide password">
                  <input class="password-toggle-check" type="checkbox"><span class="password-toggle-indicator"></span>
                </label>
              </div>
            </div>
          </div>
          <div class="mb-4">
            <div class="position-relative"><i class="ai-lock-closed fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
              <div class="password-toggle">
                <input class="form-control form-control-lg ps-5" v-model="password2" type="password" placeholder="비밀번호확인" required>
                <label class="password-toggle-btn" aria-label="Show/hide password">
                  <input class="password-toggle-check" type="checkbox"><span class="password-toggle-indicator"></span>
                </label>
              </div>
            </div>
          </div>
          <button class="btn btn-lg btn-success w-100 mb-4" type="submit" value="SignUp">회원가입</button>
          <!-- 그냥 띄우기만 ! -->
            </form>
          </div>
          <!-- Copyright-->
          <p class="w-100 fs-sm pt-5 mt-auto mb-5" style="max-width: 526px;"><span class="text-muted">&copy; Made by</span><a class="nav-link d-inline-block p-0 ms-1" href="#" target="_blank" rel="noopener">TEAM HIVE</a></p>
        </div>
        <!-- 사진 넣을려면 -->
        <!-- <div class="w-50 bg-size-cover bg-repeat-0 bg-position-center" style="background-image: url(assets/groot.jpg);"></div> -->
      </div>
    </main>
  </div>
</template>

<script>
// import router from '@/router'

export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)

    },
 
  
  }
}
</script>
<style scoped>
img {
    position: relative;
    z-index: -5;
}
.board-list {
    border: solid var(--ar-gray-900);
    border-radius: 20px;
    margin: 5px;
    
  }
</style>