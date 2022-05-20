import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';
import store from './store'
// import './style/style.scss'

Vue.prototype.$axios = axios; //prototype에 axios 추가

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

window.Kakao.init('e5ff1659f2da5db0ab6fc8f99cd0733d')
