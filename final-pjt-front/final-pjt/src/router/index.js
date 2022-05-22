import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MainRecommendView from '../views/MainRecommendView.vue'
import SearchView from '../views/SearchView.vue'
import MyPageView from '../views/MyPageView.vue'
import GenreRecommendView from '../views/GenreRecommendView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/recommend',
    name: 'mainrecommend',
    component: MainRecommendView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MyPageView
  },
  {
    path: '/recommend/genre',
    name: 'genrerecommend',
    component: GenreRecommendView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
