<template>
  <div>
    <nav class="navbar navbar-expand-md">
      <div class="container-fluid">
          <div class="navbar-brand" href="#">
            <router-link to="/recommend">
              <p>Movie JOY</p>
            </router-link>
          </div>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <i class="fa-solid fa-bars navbar-toggler-icon"></i>
        </button>
      </div>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
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
              <router-link to="/release">
                <p>Release</p>
              </router-link>
            </div>
          </li>
          <li class="nav-item" style="text-align:center;">
            <div class="nav-link">
              <router-link to="/search">
                <!-- <p class="fa-solid fa-magnifying-glass"></p> -->
                <p>Search</p>
              </router-link>
            </div>
          </li>
        </ul>
      </div>
    </nav>
  </div>
  
</template>

<script>
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
  position: fixed-top;
  /* background-color: rgba(0, 0, 0, 0.432); */
}

.navbar-toggler-icon {
  color: white;
}

.navbar-brand {
  animation: neon1 1.5s ease-in-out infinite alternate;
  font-size: 2rem;
  font-weight: bold;
  color: rgb(255, 255, 255);
  margin-left: 0.5rem;
  text-decoration: none;
  transition: .3s;
}

.navbar-brand:hover,
.navbar-brand a:hover,
.navbar-brand a:focus {
  color: rgb(255, 255, 255);
  transform: scale(1.1);
}

.navbar-brand a {
  text-decoration: none;
}

@keyframes neon1 {
  from {
    text-shadow: 0 0 2px rgba(255, 255, 255, 0.575), 0 0 4px rgba(255, 255, 255, 0.671), 0 0 6px rgba(255, 255, 255, 0.726), 0 0 8px #00adb9,
      0 0 10px #0066aa, 0 0 12px #bd0153, 0 0 14px #4c00c7, 0 0 16px #00adb9;
  }
  to {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.747), 0 0 10px rgba(255, 255, 255, 0.651), 0 0 15px rgba(255, 255, 255, 0.644), 0 0 20px #00adb9,
      0 0 35px #0066aa, 0 0 40px #bd0153, 0 0 50px #4c00c7, 0 0 75px #00adb9;
  }
}

.navbar-nav {
  margin-right: 2rem;
  word-break : nowrap;
  margin-top: 20px;
}

.form-control {
  width: 10rem;
  height: 1.5rem;
}

.nav-link {
  display: flex;
  justify-content: center;
  font-size: 1rem;
  color: white;
  margin: 0.3rem;
  transition: .3s;
}

.nav-link a {
  color: white;
  text-decoration: none;
}

.nav-link a:hover,
.nav-link a:focus {
  color: #00d8e4;
  transform: scale(1.1);
}

.nav-link:hover,
.nav-link:focus {
  color: #00d8e4;
  transform: scale(1.1);
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