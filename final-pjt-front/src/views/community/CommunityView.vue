<template>
  <div class="bg-gray pb-3">

    <div class="board-list">
      <!-- 게시글생성 버튼 -->
      <div class="common-buttons pt-2 ">
        <button type="button" class="w3-button w3-round w3-blue-gray" @click="createArticle()">글쓰기</button>
      </div>

      <div class="container pt-2 pb-lg-5 pb-md-4 pb-2 my-5">
          <!-- 게시글 네브바 -->
          <div class="row align-items-center gy-2 mb-4 pb-1 pb-sm-2 pb-lg-3 ">
            <div class="col-lg-5 ">
              <h1 class="mb-lg-0 ">&nbsp;게시판</h1>
            </div>
            <div class="col-xl-2 offset-xl-1 col-lg-3 col-sm-5 ">
              <select v-model="searchSelected" class="form-select">
                <option :value="true">제목</option>
                <option :value="false" >작성자</option>
              </select>
            </div>
            <div class="col-lg-4 col-sm-7">
              <div class="position-relative"><i style="color:gray" class="ai-search position-absolute top-50 start-0 translate-middle-y ms-3"></i>
                <input class="form-control ps-5" v-model.trim="searchWord" type="search" placeholder="내용을 입력하세요">
              </div>
            </div>
          </div>

          <!-- 게시글들 -->
          <article class="board-article row p-5 g-0 mb-4" v-for="(row, idx) in pageArticle" :key="idx">
          
            
            <a class="col-sm-5 col-lg-4 bg-repeat-0 bg-size-cover bg-position-center rounded-5" href="#" v-on:click="gotoArticle(row.id)"  style="background-color: gray; min-height: 2rem; position: relative;">
              <img class="position-absolute top-0 start-0 h-100 w-100 rounded-5" :src="`http://127.0.0.1:8000${row.user.profile}`" alt="">
            </a>
            <div class="col-sm-7 col-lg-8">
              <div class="pt-4 pb-sm-4 ps-sm-4 pe-lg-4">
                <h3>No.{{ idx+1 + 5*(currentPage-1) }}</h3>
                <h3 class="zoom" v-on:click="gotoArticle(row.id)"><a :href="row.url">제목 : {{ row.title }}</a></h3>
                <p class="zoom d-sm-none d-md-block" @click="gotoUser(row.user.username)">작성자 : {{ row.user.username }}</p>
                <p>등록일자 {{ row.updated_at.slice(0, 10) }}</p>
                <p>댓글 {{ row.comment_counts }}</p>
              </div>
            </div>
          </article>
    
          <div class="row gy-3 align-items-center mt-lg-5 pt-2 pt-md-3 pt-lg-0 mb-md-2 mb-xl-4">
            <div class="col col-md-4 col-6 order-md-1 order-1">
              
            </div>
       
            <div class="col col-md-4 col-6 order-md-3 order-2">
              <nav aria-label="Page navigation">
                <ul class="pagination pagination-sm justify-content-center">
                  <li  :class="{'visually-hidden': currentPage==1}" ><span class="page-link" @click="pageSwitch(1)" >First</span></li>
                  <li v-for="(page, index) in pageidx" :key="index" :class="{'active': currentPage===page, 'visually-hidden': (page > currentPage + 2 || page < currentPage - 2)}" ><span class="page-link" @click="pageSwitch(page)">{{ page }}</span></li>
                  <li  :class="{'visually-hidden': currentPage==pageidx}" ><span class="page-link" @click="pageSwitch(pageidx)">Last</span></li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
      
   
    <!-- Subscription-->
    
  </div>
</template>





<script>
export default {
  name: 'CommunityView',
  created() {
    this.$store.dispatch('getArticles')
    console.log(this.$store.getters.getArticles)
  },
  data() { //변수생성
    return {
      searchSelected: true,
      searchWord: '',

      currentPage: 1,
    }
  },
  methods: {
    createArticle() {
      this.$router.push({name: 'CreateArticle'})
    },
    gotoArticle(articleId) {
      this.$router.push({name: 'communityDetail', params: {'articleId': articleId}})
    },
    gotoUser(username) {
      if ( username === this.$store.state.username) {
        this.$router.push({name: 'FavoritesView'})
      } else {
        this.$router.push({name: 'UserPage', params: {'username': username}})
      }
    },
    pageSwitch(page) {
      this.currentPage = page
      window.scrollTo(0, 0)
    }
  },
  computed: {
    articles() {
      if (this.searchWord.length == 0) {
        return this.$store.getters.getArticles
      }
      if (this.searchSelected) {
        return this.$store.getters.getArticles.filter(article => {
          console.log(article.title.includes(this.searchWord), this.searchWord)
          return article.title.includes(this.searchWord)
        })
      } else {
        return this.$store.getters.getArticles.filter(article => {
          return article.user.username.includes(this.searchWord)
        })
      }
    },
    pageidx() {
      return parseInt((this.articles.length+4)/5)
    },
    pageArticle() {
      return this.articles.filter((article, index) => {
        return parseInt((index)/5+1) === this.currentPage
      })
    }
  }
}
</script>

<style>
  .board-list {
    border: solid var(--ar-gray-900);
    width: 1000px;
    margin: auto;
    border-radius: 20px;
  }
  .board-article{
    border: solid var(--ar-gray-900);
    border-radius: 20px;
  }

  .board-detail {
      width: 768px;
      margin: auto;
      text-align: left;
  }

  .board-contents {
      padding: 12px 8px;
      border-bottom: 1px solid var(--ar-gray-900);
  }

  .common-buttons {
      padding: 8px;
      text-align: right;
  }

  .zoom:hover {
    transform: scale(1.2);
    transition: 0.7s;
  }
  
</style>