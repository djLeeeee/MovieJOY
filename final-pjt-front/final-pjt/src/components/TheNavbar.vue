<template>
  <div>
    <nav class="navbar navbar-expand-md">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Project</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item" style="text-align:center;">
            <div class="nav-link">
              <router-link to="/search">
                <p class="fa-solid fa-magnifying-glass"></p>
              </router-link>
            </div>
          </li>
          <li class="nav-item" style="text-align:center;">
            <div class="nav-link">
              <router-link to="/recommend">
                <p>Home</p>
              </router-link>
            </div>
          </li>
          <li class="nav-item" style="text-align:center;">
            <div class="nav-link">
              <router-link to="/recommend/genre">
                <p>Genre</p>
              </router-link>
            </div>
          </li>
          <li class="nav-item" style="text-align:center;">
            <div class="nav-link">
              <router-link to="/mypage">
                <p>MyPage</p>
              </router-link>
            </div>
          </li>
          
          <!-- 로그아웃 버튼 -->
          <li>
            <button @click="logout()">Logout</button>
          </li>
        </ul>
      </div>
    </nav>
  </div>
  
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'TheNavbar',
    data: function () {
      return {
        onSearch: false,
        windowWidth: window.innerWidth,
      }
    },
    mounted() {
          window.addEventListener('resize', this.handleResize);
    },
    beforeDestroy() {
          window.removeEventListener('resize', this.handleResize);
    },
    methods: {
      ...mapActions(['logout']),
      searchStatus: function () {
        if (this.windowWidth >= 768) {
          this.onSearch = !this.onSearch}
      },
      handleResize: function () {
        this.windowWidth = window.innerWidth;
        if (this.windowWidth < 768) {
          this.onSearch = true
        }
      }
    }
  }
</script>

<style>
.navbar {
  position: sticky;
  background-color: rgba(0, 0, 0, 0.432);
}

.navbar-brand {
  color: white
}

.navbar-nav {
  margin-right: 2rem;
  word-break : nowrap;
}

.form-control {
  width: 10rem;
  height: 1.5rem;
}

.nav-link {
  display: flex;
  justify-content: center;
  font-size: 0.9rem;
  color: white;
}

a {
  color: white;
  text-decoration: none;
}

a:hover,
a:focus {
  color: #00d8e4;
  transform: scale(1.1);
}

.nav-link:hover,
.nav-link:focus {
  color: #00d8e4;
  transform: scale(1.1);
}

.search-btn {
  padding: 0px;
  margin-left: 0.5rem;
  transition: 1s;
}

.fa-magnifying-glass {
  text-decoration: none;
}

.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(3px);
  opacity: 0;
}

</style>