<template>
  <div class="bg-gray">
    <main class="page-wrapper">
      <!-- Page content-->
      <div class="d-lg-flex position-relative">
        <!-- Sign in form-->
        
        <div class="d-flex flex-column align-items-center mx-auto w-lg-50 h-100 px-3 px-lg-5 pt-5">
          <img src="../../assets/bighive.png" style="z-index: 1" alt="Logo" width="200" height="200">
          <h1>HIVE</h1>
          <h1>비밀번호 변경</h1>
          <div class="w-100 mt-auto" style="max-width: 526px;">
            
            <form class="needs-validation" novalidate @submit.prevent="changePassword()">
              <!-- <div class="pb-3 mb-3">
        
                <div class="position-relative"><i class="ai-mail fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
                  <input class="form-control form-control-lg ps-5" type="password" v-model="currentPassword" placeholder="현재 비밀번호" required>
                </div>
              </div> -->
              <div class="mb-4">
                <div class="position-relative"><i class="ai-lock-closed fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
                  <div class="password-toggle">
                    <input class="form-control form-control-lg ps-5" type="password" v-model="password1" placeholder="새로운 비밀번호" required>
                  </div>
                </div>
              </div>
              <div class="mb-4">
                <div class="position-relative"><i class="ai-lock-closed fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
                  <div class="password-toggle">
                    <input class="form-control form-control-lg ps-5" type="password" v-model="password2" placeholder="새로운 비밀번호 확인" required>
                  </div>
                </div>
              </div>
              <button class="btn btn-lg btn-success  w-100 mb-4" type="submit">비밀번호 변경</button>
            </form>
          </div>
        </div>
        <!-- Cover image-->
        <!-- <div class="w-50 bg-size-cover bg-repeat-0 bg-position-center" style="background-image: url(assets/hive.png);"></div> -->
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'ChangePassword',
  data() {
    return {
      currentPassword: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    changePassword() {
      const new_password1 = this.password1
      const new_password2 = this.password2

      this.$store.dispatch('changePassword', { new_password1, new_password2 })
    }
  }
}
</script>

<style scoped>
  img {
      position: relative;
      z-index: -1;
  }
</style>