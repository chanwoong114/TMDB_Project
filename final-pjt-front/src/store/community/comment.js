import axios from "axios"
import store from "../index.js"
// import router from "@/router/index.js"

const comment = {
  state: {
    comments: [],
    articleId: null,
  },
  getters: {
    getComments(state) {
      return state.comments
    }
  },
  mutations: {
    SAVE_COMMENTS(state, data) {
      state.comments = data[0]
      state.articleId = data[1]
    },
    DELETE_COMMENT(state, commentId) {
      state.comments = state.comments.filter(comment => {
        return comment.id != commentId
      })
    },
    CREATE_COMMENT(state, comment) {
      state.comments.push(comment)
    },
    UPDATE_COMMENT(state, commentData) {
      state.comments = state.comments.map(comment => {
        if (comment.id === commentData.id) {
          comment = commentData
        }
        return comment
      })
    }
  },
  actions: {
    save_comments(context, data) {
      context.commit('SAVE_COMMENTS', data)
    },
    createComment(context, content) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/articles/${context.state.articleId}/`,
        data: { content },
        headers: {
          Authorization: `Token ${store.state.token}`
        }
      })
      .then(res => {
        console.log(res)
        context.commit('CREATE_COMMENT', res.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    deleteComment(context, commentId) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/articles/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${store.state.token}`
        }
      })
      .then(res => {
        console.log(res)
        context.commit('DELETE_COMMENT', commentId)
      })
      .catch(error => {
        console.log(error)
      })
    },
    updateComment(context, payload) {
      const commentId = payload[0]
      const content = payload[1]

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/articles/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${store.state.token}`
        },
        data: { content }
      })
      .then(res => {
        console.log(res)
        context.commit('UPDATE_COMMENT', res.data)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
}

export default comment
