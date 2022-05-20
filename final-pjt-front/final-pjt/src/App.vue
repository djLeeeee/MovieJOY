<template>
  <div id="app">
    <TheNavbar v-if="isLoggedIn" />
    <div id="router-box">
      <router-view/>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TheNavbar from '@/components/TheNavbar'

export default {
  components: {
    TheNavbar
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>


<style>

#app {
  font-family: 'GmarketSansMedium';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

@font-face {
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>
