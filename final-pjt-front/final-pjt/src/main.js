import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';

Vue.prototype.$axios = axios; //prototype에 axios 추가

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
