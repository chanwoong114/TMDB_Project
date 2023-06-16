import axios from "axios"
import store from "../index.js"
import router from "@/router/index.js"

const community = {
  state: {
    articles: []
  },
  getters: {
    getArticles(state) {
      return state.articles
    }
  },
  mutations: {
    GET_ARTICLES(state, data) {
      state.articles = data
    },
    CREATE_ARTICLES(state, data) {
      // state.articles.unshift(data)
      console.log(state, data)
    },
    UPDATE_ARTICLES(state, data) {
      state.articles = state.articles.map(article => {
        if (article.id === data.id) {
          article = data
        }
        return article
      })
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/`,
        headers:{
          Authorization:`Token ${store.state.token}`
        }
      })
      .then((res) => {
      // console.log(res, context)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createArticle(context, payload) {
      const title = payload.title
      const content = payload.content

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/articles/`,
        headers:{
          Authorization:`Token ${store.state.token}`
        },
        data: { title, content }
      })
      .then((res) => {
        console.log(res, context)
        // context.commit('CREATE_ARTICLES', res.data)
        router.push({name: 'communityDetail', params: {articleId: res.data.id}})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteArticle(context, payload) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/articles/${payload}/`,
        headers:{
          Authorization:`Token ${store.state.token}`
        },
      })
      .then((res) => {
        console.log(res, context)
        router.push({name: 'community'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    articleList() {
      router.push({name: 'community'})
    },
    updateArtiecle(context, payload) {
      const title = payload.title
      const content = payload.content
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/articles/${payload.id}/`,
        headers:{
          Authorization:`Token ${store.state.token}`
        },
        data: { title, content }
      })
      .then((res) => {
      // console.log(res, context)
        context.commit('UPDATE_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}

export default community
