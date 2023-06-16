import Vue from 'vue'
import Vuex from 'vuex'
import movie from '@/store/movie/movie'
import community from '@/store/community/community.js'
import comment from '@/store/community/comment.js'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
import swal from 'sweetalert';

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    darkMode: false,
    movies: [
    ],
    token: null,
    username:null,
    likeUsers: []
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    isDarkMode(state) {
      return state.darkMode
    }
  },
  mutations: {
    // signup & login -> 완료하면 토큰 발급
    SAVE_TOKEN(state, token) {
      state.token = token
      console.log(token)
      router.push({name : 'MovieView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    SAVE_USERNAME(state, username) {
      state.username = username;
    },
    SAVE_LIKE_USERS(state, data){
      data.forEach(userInfo => {
        state.likeUsers.push(userInfo.id)
      })
    },
    IS_FOLLOW(state, data) {
      console.log(data)
      if (data.follow) {
        state.likeUsers.push(data.id)
      } else {
        state.likeUsers = state.likeUsers.filter(userId => {
          return userId != data.id
        })
      }
    },
    TOGGLE_MODE(state) {
      state.darkMode = !state.darkMode
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      console.log(payload)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
          context.commit('SAVE_USERNAME', username)
          swal("Success!", "회원 가입이 완료되었습니다.", "success");
        })
        .catch((err) => {
          console.log(err)
          swal("Nope!", "올바른 정보를 입력하세요", "error");
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      console.log(payload)
      axios({
        
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.commit('SAVE_USERNAME', username)
          context.dispatch('loadUserData', res.data.key)
          swal("Success!", "로그인이 완료되었습니다.", "success");
        })
        .catch((err) => {
          console.log(err)
          swal("Nope!", "올바른 정보를 입력하세요", "error");
        })
      },
      signOut(context) {
      swal("Success!", "로그아웃이 완료되었습니다.", "success");
      console.log(context)
      router.push({name: 'HomeView'})
      window.localStorage.clear();
    },
    deleteUser(context) {
      console.log(context.state.token)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/delete/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
      alert('회원탈퇴가 성공적으로 완료되었습니다.')
      router.push({name: 'HomeView'})
      window.localStorage.clear();
    },
    changePassword(context, payload) {
      const new_password1 = payload.new_password1
      const new_password2 = payload.new_password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
        data: {
          new_password1, new_password2
        }
      })
      .then(res => {
        console.log(res)
        alert('비밀번호 변경이 성공적으로 완료되었습니다.')
        router.push({name: 'MovieView'})
      })
      .catch(error => {
        console.log(error)
      })
    },
    follow(context, userId) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${userId}/follow/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then(res => {
        console.log(res)
        context.commit('IS_FOLLOW', res.data)
      })
      .catch(error => {
        console.log(error)
        alert(error.response.data)
        return
      })
    },
    toggleDarkMode(context) {
      context.commit('TOGGLE_MODE')
    },
  },
  modules: {
    movie,
    community,
    comment,
  },
})
