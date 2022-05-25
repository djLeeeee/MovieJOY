<template>
  <div id="app">
    <TheNavbar id="navbar-component" v-if="isLoggedIn" />
    <div id="router-box">
      <transition name="slide" mode="out-in">
        <router-view/>
      </transition>
    </div>
    <TheUnderNavbar v-if="isLoggedIn" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TheNavbar from '@/components/TheNavbar'
import TheUnderNavbar from '@/components/TheUnderNavbar'

export default {
  components: {
    TheNavbar,
    TheUnderNavbar,
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
  padding-bottom: 5rem;;
  position: relative;
  top: 0px;
}

@font-face {
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

body.modal-open {
  overflow: hidden;
}

#router-box {
  width: 100vw;
  position: relative;
  top: 0px;
}

.slide-enter-from,
.slide-leave-active {
  transition: opacity 1s, transform 1s;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translateX(-30%);
}

.fade-enter-active {
  transition: opacity .5s;
  transition-delay: .5s;
}
.fade-leave-active {
  transition: opacity .5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
