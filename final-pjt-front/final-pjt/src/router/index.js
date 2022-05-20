import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MainRecommendView from '../views/MainRecommendView.vue'
import SearchView from '../views/SearchView.vue'

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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
