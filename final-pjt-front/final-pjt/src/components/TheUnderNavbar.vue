<template>
  <div id="underNavbar"> 
    <nav class="menu">
      <input type="checkbox" href="#" class="menu-open" name="menu-open" id="menu-open" />
      <label class="menu-open-button" for="menu-open">
        <img :src="require(`@/assets/profile_img/img_${ profile_image }.png`)" alt="">
      </label>

      <a @click="logout()" class="menu-item logout-color"> <i class="fa-solid fa-arrow-right-from-bracket"></i> </a>
      <router-link class="menu-item profile-color" to="/mypage">
         <a href="#" class="profile-color-sub"> <i class="fa-solid fa-user"></i> </a>
      </router-link>
      <a @click="moveToTop" class="menu-item scroll-up-color"><i class="fa-solid fa-arrow-up"></i> </a>
    </nav>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapGetters } from 'vuex'
import drf from '@/api/drf'

export default {
  name: 'TheUndernavbar',
  data: function () {
    return {
      profile_image: 1
    }
  },
  methods: {
    ...mapActions(['logout']),
    moveToTop: function () {
      window.scrollTo({top: 0, behavior: 'smooth'})
    }
  },
  computed: {
    ...mapGetters(['authHeader'])
  },
  created () {
    axios({
      url: drf.accounts.myProfile(),
      method: 'get',
      headers: this.authHeader
    })
    .then(res =>
      this.profile_image = res.data.profile_image
    )
  },
  updated () {
    axios({
      url: drf.accounts.myProfile(),
      method: 'get',
      headers: this.authHeader
    })
    .then(res =>
      this.profile_image = res.data.profile_image
    )
  }
}
</script>

<style>

a {
   color: inherit;
}

.menu-item,
.menu-open-button {
   background: #EEEEEE;
   border-radius: 100%;
   width: 60px;
   height: 60px;
   margin-left: -20px;
   position: absolute;
   color: #FFFFFF;
   align-items: center;
   text-align: center;
   line-height: 65px;
   -webkit-transform: translate3d(0, 0, 0);
   transform: translate3d(0, 0, 0);
   -webkit-transition: -webkit-transform ease-out 200ms;
   transition: -webkit-transform ease-out 200ms;
   transition: transform ease-out 200ms;
   transition: transform ease-out 200ms, -webkit-transform ease-out 200ms;
}

.menu-open {
   display: none;
}

.menu {
  position: fixed;
  bottom: 0;
  right: 1rem;
  width: 80px;
  height: 80px;
  text-align: center;
  box-sizing: border-box;
  font-size: 26px;
}

.menu-item:hover {
   background: #EEEEEE;
   color: #3290B1;
}

.menu-open-button {
   z-index: 2;
   -webkit-transition-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1.275);
   transition-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1.275);
   -webkit-transition-duration: 400ms;
   transition-duration: 400ms;
   -webkit-transform: scale(1.1, 1.1) translate3d(0, 0, 0);
   transform: scale(1.1, 1.1) translate3d(0, 0, 0);
   cursor: pointer;
   box-shadow: 3px 3px 0 0 rgba(0, 0, 0, 0.14);
}

.menu-open-button img {
   border-radius: 100%;
   width: 61px;
   height: 61px;
   margin-bottom: 10px;
}


.menu-open-button:hover {
   -webkit-transform: scale(1.2, 1.2) translate3d(0, 0, 0);
   transform: scale(1.2, 1.2) translate3d(0, 0, 0);
}

.menu-open:checked + .menu-open-button {
   -webkit-transition-timing-function: linear;
   transition-timing-function: linear;
   -webkit-transition-duration: 200ms;
   transition-duration: 200ms;
   -webkit-transform: scale(0.8, 0.8) translate3d(0, 0, 0);
   transform: scale(0.8, 0.8) translate3d(0, 0, 0);
}

.menu-open:checked ~ .menu-item {
   -webkit-transition-timing-function: cubic-bezier(0.935, 0, 0.34, 1.33);
   transition-timing-function: cubic-bezier(0.935, 0, 0.34, 1.33);
}

.menu-open:checked ~ .menu-item:nth-child(3) {
   transition-duration: 180ms;
   -webkit-transition-duration: 180ms;
   -webkit-transform: translate3d(0.08361px, -70px, 0);
   transform: translate3d(0.08361px, -70px, 0);
}

.menu-open:checked ~ .menu-item:nth-child(4) {
   transition-duration: 280ms;
   -webkit-transition-duration: 280ms;
   -webkit-transform: translate3d(0.08361px, -140px, 0);
   transform: translate3d(0.08361px, -140px, 0);
}

.menu-open:checked ~ .menu-item:nth-child(5) {
   transition-duration: 380ms;
   -webkit-transition-duration: 380ms;
   -webkit-transform: translate3d(0.08361px, -210px, 0);
   transform: translate3d(0.08361px, -210px, 0);
}



.logout-color {
   background-color: #e63f7fda;
   box-shadow: 3px 3px 0 0 rgba(0, 0, 0, 0.14);
   text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.12);
}

.logout-color:hover {
   color: #e63f7fda;
   text-shadow: none;
}

.profile-color {
   background-color: #5fac61d8;
   box-shadow: 3px 3px 0 0 rgba(0, 0, 0, 0.14);
   text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.12);
}

.profile-color:hover,
.profile-color-sub:hover {
   color: #5fac61d8;
   text-shadow: none;
}

.scroll-up-color {
   background-color: #1ea4d4e3;
   box-shadow: 3px 3px 0 0 rgba(0, 0, 0, 0.14);
   text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.12);
}

.scroll-up-color:hover {
   color: #1ea4d4e3;
   text-shadow: none;
}

.credit {
   margin: 24px 20px 120px 0;
   text-align: right;
   color: #EEEEEE;
}

.credit a {
   padding: 8px 0;
   color: #C49CDE;
   text-decoration: none;
   transition: all 0.3s ease 0s;
}

.credit a:hover {
   text-decoration: underline;
}
</style>