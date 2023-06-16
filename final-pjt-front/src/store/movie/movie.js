import axios from "axios"
import index from "../index.js"

const movie = {
  state: {
    rated_movies: [],
  },
  getters: {
    likeCount(state) {
      return state.rated_movies.length
    },
    likeMovies(state) {
      return state.rated_movies
    }
  },
  mutations: {
    IS_LIKE(state, data) {
      if (!data[1]) {
        state.rated_movies = state.rated_movies.filter(movie => {
          return movie != data[0]
        })
      } else {
        state.rated_movies.push(data[0])
      }
    },
    LOAD_USER_DATA(state, data) {
      data.forEach(movie => {
        state.rated_movies.push(movie.id)
      })
    }
  },
  actions: {
    movieLike(context, payload) {
      console.log(context)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${payload[0]}/like/`,
        headers: {
          Authorization: `Token ${index.state.token}`
        }
      })
      .then(res => {
        console.log(res)
        context.commit('IS_LIKE', payload)
      })
      .catch(error => {
        error
      })
    },
    loadUserData(context, Token) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/mypage/`,
        headers: {
          Authorization: `Token ${Token}`
        }
      })
      .then(res => {
        console.log(res.data)
        context.commit('LOAD_USER_DATA', res.data.rated_movies)
        context.commit('SAVE_LIKE_USERS', res.data.followings)
      })
      .catch(err => {
        console.log(err)
      })
    },
    clearAll(context) {
      context.state.rated_movies.forEach(movieId => {
        context.dispatch('movieLike', [movieId, false])
      })
    }
  },
}

export default movie
