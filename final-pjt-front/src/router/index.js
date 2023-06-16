import Vue from 'vue'
import VueRouter from 'vue-router'
// import MovieView from '../views/MovieView.vue'
import HomeView from '../views/HomeView.vue'
import GenreView from '../views/GenreView.vue'
import FavoritesView from '../views/FavoritesView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import CommunityView from '@/views/community/CommunityView'
import NotFound from '@/views/404NotFound'
import SearchView from '@/views/SearchView'
import CommunityDetailView from '@/views/community/CommunityDetailView'
import CreateArticle from '@/views/community/CreateArticle'
import UpdateArticle from '@/views/community/UpdateArticle'
import UserPage from '@/views/userpage/UserPage'
import ChangePassword from '@/views/userpage/ChangePassword'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'MovieView',
    // component:MovieView
    component:()=> import('../views/MovieView.vue')
  },
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/genre',
    name: 'GenreView',
    component: GenreView
  },
  {
    path: '/favorites',
    name: 'FavoritesView',
    component: FavoritesView
  },
  {
    path: '/movies/:movieId/detail',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
    beforeEnter(to, from, next) {
      if(store.state.token) {
        alert('이미 로그인 되어있습니다.')
        next({name: 'MovieView'})
      } else {
        next()
      }
    }
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView,
    beforeEnter(to, from, next) {
      if(store.state.token) {
        alert('이미 로그인 되어있습니다.')
        next({name: 'MovieView'})
      } else {
        next()
      }
    }
  },
  
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },

  {
    path: '/userpage/:username/detail',
    name: 'UserPage',
    component: UserPage,
  },
  
  {
    path: '/password',
    name: 'ChangePassword',
    component: ChangePassword
  },

  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },

  {
    path: '/community/:articleId/detail',
    name: 'communityDetail',
    component: CommunityDetailView
  },

  {
    path: '/community/create',
    name: 'CreateArticle',
    component: CreateArticle
  },

  {
    path: '/community/:articleId/update',
    name: 'UpdateArticle',
    component: UpdateArticle
  },
  
  {
    path: '/404',
    name: '404NotFound',
    component: NotFound
  },
  
  {
    path: '*',
    redirect: '/404'
  },
  
]
const router = new VueRouter({
  mode: 'history',
  scrollBehavior() { 
    return { x: 0, y: 0 } 
  },
  base: process.env.BASE_URL,
  routes
})

export default router

router.beforeEach((to, from, next) => {
  const isLoggedIn =  store.getters.isLogin
  const authPage = ['HomeView', 'SignUpView','LogInView']
  const isAuth = !authPage.includes(to.name)
  // 로그인이 필요한 페이지에 접근하려고 할 때
  if (isAuth && !isLoggedIn) {
    alert('로그인하세요')
    next({ name: 'LogInView' }); // HomeView로 리디렉션합니다.
    
  } else {
    next(); // 정상적으로 다음 단계로 진행합니다.
  }
});

