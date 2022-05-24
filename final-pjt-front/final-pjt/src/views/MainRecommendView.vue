<template>
  <div>
    <div id="logo-box">
      <main>Movie JOY</main>
      <p class="main-page-text">Movie Recommendation In 3 Ways</p>
    </div>
    <div id="recommend-buttons">
      <a href="#" @click="selectMovie(0)">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Popular of TMDB
      </a>
      <a href="#" @click="selectMovie(1)">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Choice of Genre
      </a>
      <a href="#" @click="selectMovie(2)">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Review of Genre
      </a>
    </div>
    <div>
      <MovieList :movies="selectedMovies" />
    </div>
  </div>
</template>

<script>
  import drf from '@/api/drf'
  import { mapGetters } from 'vuex'
  import MovieList from "@/components/MovieList"
  import axios from 'axios'

  export default {
    name: 'MainRecommendationView',
    data: function () {
      return {
        selectedMovies: [],
        moviesBy3Way: {},
        selectMovieCategory: -1,
      }
    },
    components: { 
      MovieList,
    },
    methods: {
      selectMovie: function (category) {
        this.selectedMovies = this.moviesBy3Way[category]
        const logoBox = document.querySelector('#logo-box')
        logoBox.setAttribute('style', 'margin: 0vh;')
      }
    },
    computed: {
      ...mapGetters(['authHeader'])
    },
    created () {
      axios({
        url: drf.movies.recommendByTMDB(),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => {
        this.moviesBy3Way[0] = res.data
      })

      axios({
        url: drf.movies.recommendByLikeGenres(),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => {
        this.moviesBy3Way[1] = res.data
      })

      axios({
        url: drf.movies.recommendByReviews(),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => {
        this.moviesBy3Way[2] = res.data
      })
    }
  }
</script>

<style>
@font-face {
  src: url("https://www.axis-praxis.org/fonts/webfonts/MetaVariableDemo-Set.woff2")
    format("woff2");
  font-family: "Meta";
  font-style: normal;
  font-weight: normal;
}

#logo-box {
  margin-top: 20vh;
  transition: 0.8s;
}

main {
  transition: all 0.5s;
  -webkit-text-stroke: 4px #d6f4f4;
  font-variation-settings: "wght" 900, "ital" 1;
  font-size: 7rem;
  text-align: center;
  color: transparent;
  font-family: "Meta", sans-serif;
  text-shadow: 7px 7px 7px #00d7e2ec,
    10px 1px 0px #161491c2,
    15px 15px 0px #80179bcc;
  cursor: pointer;
}

main:hover {
  font-variation-settings: "wght" 100, "ital" 0;
  text-shadow: none;
}

.main-page-text {
  margin-top: 1rem;
  color: rgba(255, 255, 255, 0.911);
  font-size: 2rem;
  text-align: center;
  font-family: "Meta", sans-serif;
  text-shadow: 4px 4px 5px #00d7e2e5;
}

#recommend-buttons {
  margin-top: 2rem;
}

#recommend-buttons button {
  /* border: 2px solid; */
  font: inherit;
  line-height: 1;
  margin: 0.5em;
  padding: 1em 2em;
  /* border-radius: 100px; */
  transition: 0.5s;
  width: 200px;
  color: white;
  margin: 1rem;
  background: none;
}

.pulse:hover, 
.pulse:focus {
  animation: pulse 1s;
  box-shadow: 0 0 0 2em transparent;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 #d6f4f4; }
}


/* genre-select-btn */
#recommend-buttons a{
  position: relative;
  display: inline-block;
  padding: 15px 20px;
  margin: 0.8rem;
  color: #03e9f4;
  text-decoration: none;
  text-transform: uppercase;
  transition: 0.5s;
  letter-spacing: 4px;
  overflow: hidden;
  font-size: 0.9rem; 
}
#recommend-buttons a:focus{
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4,
                0 0 25px #03e9f4,
                0 0 50px #03e9f4,
                0 0 200px #03e9f4;
     -webkit-box-reflect:below 1px linear-gradient(transparent, #0005);
}

#recommend-buttons a:hover span{
    position: absolute;
    display: block;
}
#recommend-buttons a span:nth-child(1){
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
#recommend-buttons a span:nth-child(2){
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
#recommend-buttons a span:nth-child(3){
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


#recommend-buttons a span:nth-child(4){
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

</style>