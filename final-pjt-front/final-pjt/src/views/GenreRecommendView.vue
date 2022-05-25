<template>
  <div @click="genreClose" id="genre-recommend-box">
    <div id="genre-select-box">
      <p class="genre-main-text">Search the movie by genres</p>
      <p class="genre-text">Recommend 12 movies of your choice.</p>
      <a @click="onSelect" href="#">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Select Genre
      </a>
    </div>
    <div @click="genreClose" id="genre-movie-box">
      <h3 style="color: white;">{{ selectedGenre }}</h3>
      <MovieList :movies="selectedMovies"/>
    </div>
    <transition name="fade"> 
      <div v-if="isSelect" class="genre-buttons" id="genre-box">
        <p class="genre-box-text">Genres</p>
        <button v-for="(data, idx) in moviesByGenre" :key="idx" @click="selectGenre(idx), onSelect()" class="raise">
            <span>{{ data['genre_name'] }}</span>
        </button>
      </div>
    </transition>
  </div>
</template>

<script>
  import axios from 'axios'
  import drf from '@/api/drf'
  import { mapGetters } from 'vuex'
  import MovieList from "@/components/MovieList"
  import router from '@/router'

  export default {
    name: 'GenreRecommendView',
    components: { 
      MovieList,
    },
    data: function () {
      return {
        isSelect: false,
        genres: [
          {
            'id': 37,
            'name': '서부',
          },
          {
            'id': 10752,
            'name': '전쟁',
          },
          {
            'id': 53,
            'name': '스릴러',
          },
          {
            'id': 10770,
            'name': 'TV 영화',
          },
          {
            'id': 878,
            'name': 'SF',
          },
          {
            'id': 10749,
            'name': '로맨스',
          },
          {
            'id': 9648,
            'name': '미스터리',
          },
          {
            'id': 10402,
            'name': '음악',
          },
          {
            'id': 27,
            'name': '공포',
          },
          {
            'id': 36,
            'name': '역사',
          },
          {
            'id': 14,
            'name': '판타지',
          },
          {
            'id': 10751,
            'name': '가족',
          },
          {
            'id': 18,
            'name': '드라마',
          },
          {
            'id': 99,
            'name': '다큐멘터리',
          },
          {
            'id': 80,
            'name': '범죄',
          },
          {
            'id': 16,
            'name': '애니메이션',
          },
          {
            'id': 12,
            'name': '모험',
          },
          {
            'id': 28,
            'name': '액션',
          },
          {
            'id': 35,
            'name': '코미디',
          }
        ],
        moviesByGenre: [],
        selectedMovies: [],
        selectedGenre: '',
      }
    },
    computed: {
      ...mapGetters(['authHeader', 'isLoggedIn'])
    },
    methods: {
      selectGenre: function (idx) {
        this.selectedMovies = this.moviesByGenre[idx].movies
        this.selectedGenre = this.moviesByGenre[idx].genre_name
        const genreSelectBox = document.querySelector('#genre-select-box')
        genreSelectBox.setAttribute('style', 'margin: 0vh;')
      },
      onSelect: function () {
        this.isSelect = !this.isSelect
      },
      genreClose: function (event) {
        if(event.target.id === "genre-recommend-box" || 
          event.target.id === "genre-movie-box") {
          this.isSelect = false
        }
      }
    },
    created () {
      this.genres.map(genre => {
        axios({
          url: drf.movies.recommendByGenre(genre['id']),
          method: 'get',
          headers: this.authHeader 
        })
        .then(res => {
          const data = {
            genre_name: genre['name'],
            movies: res.data
          }
          this.moviesByGenre.push(data)
        })
      })
    },
    mounted () {
      if (! this.isLoggedIn) {
          router.push({ name: 'home' })
      }
    }
  }
</script>

<style>
#genre-recommend-box {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
}

#genre-select-box {
  padding: 2rem;
  margin-top: 30vh;
  transition: 0.8s;
}

#genre-recommend-box #genre-box {
  position: relative;
  top: 10rem;
  width: 6rem;
  width: 450px;
  height: 450px;
  padding: 50px;
  background: rgba(0, 0, 0, 0.753);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0,0,0,.6);
  overflow: auto;
}

#genre-movie-box {
  position: absolute;
  margin-top: 250px;
  margin-bottom: 5rem;
}

.genre-box-text {
  color: white;
  font-size: 1rem;
}

.genre-buttons button {
  background: none;
  border: 2px solid;
  /* font: inherit; */
  line-height: 1;
  margin: 0.5em;
  padding: 0.5em;
  color: white;
  font-size: 0.9rem;
  transition: all .5s;
}

.page-open {
  color: #01a8b1;
  scale: 1.1;
}


.genre-buttons .raise:hover,
.genre-buttons .raise-focus {
  font-size: 0.9rem;
  box-shadow: 0 0.5em 0.5em -0.4em #01a8b1;
  border: 2px solid #01a8b1a1;
  transform: translateY(-0.25em);
  background-color: #01a8b138;
  font-weight: bold;
  color: #00d7e2ec;
  transition: all .5s;
}

#genre-select-box {
  position: absolute;
}

/* genre-select-btn */
#genre-select-box a{
    position: relative;
    display: inline-block;
    padding: 15px 20px;

    color: #03e9f4;
    text-decoration: none;
    text-transform: uppercase;
    transition: 0.5s;
    letter-spacing: 4px;
    overflow: hidden;
    font-size: 0.9rem;
   
}
#genre-select-box a:hover{
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4,
                0 0 25px #03e9f4,
                0 0 50px #03e9f4,
                0 0 200px #03e9f4;
     -webkit-box-reflect:below 1px linear-gradient(transparent, #0005);
}

#genre-select-box a span{
    position: absolute;
    display: block;
}
#genre-select-box a span:nth-child(1){
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg,transparent,#03e9f4);
    animation: animate1 1s linear infinite;
}
@keyframes animate1{
    0%{
        left: -100%;
    }
    50%,100%{
        left: 100%;
    }
}
#genre-select-box a span:nth-child(2){
    top: -100%;
    right: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(180deg,transparent,#03e9f4);
    animation: animate2 1s linear infinite;
    animation-delay: 0.25s;
}
@keyframes animate2{
    0%{
        top: -100%;
    }
    50%,100%{
        top: 100%;
    }
}
#genre-select-box a span:nth-child(3){
    bottom: 0;
    right: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(270deg,transparent,#03e9f4);
    animation: animate3 1s linear infinite;
    animation-delay: 0.50s;
}
@keyframes animate3{
    0%{
        right: -100%;
    }
    50%,100%{
        right: 100%;
    }
}


#genre-select-box a span:nth-child(4){
    bottom: -100%;
    left: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(360deg,transparent,#03e9f4);
    animation: animate4 1s linear infinite;
    animation-delay: 0.75s;
}
@keyframes animate4{
    0%{
        bottom: -100%;
    }
    50%,100%{
        bottom: 100%;
    }
}

.genre-main-text {
	color: white;
	font-size: 2rem;
}

.genre-text {
	color: rgba(255, 255, 255, 0.753);
	margin-bottom: 2rem;
}

.fade-enter-active {
  transition: opacity .5s;
}
.fade-leave-active {
  transition: opacity .5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>