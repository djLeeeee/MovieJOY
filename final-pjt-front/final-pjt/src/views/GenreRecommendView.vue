<template>
  <div id="genre-reccomend-box">
    This is a movie recommendation by genre page.
    <div id="genre-box" class="row row-cols-5 row-cols-md-6 row-cols-lg-8 row-cols-xl-10 g-1">
      <div v-for="(data, idx) in moviesByGenre" :key="idx">
        <button @click="selectGenre(idx)" class="col custom-btn btn-12 bubbly-button">
          <span>Click!</span>
          <span>{{ data['genre_name'] }}</span>
        </button>
      </div>
    </div>
    <div id="genre-movie-box">
      <MovieList :movies="selectedMovies"/>
    </div>
    <p>{{ selectedGenreName }}</p>
    
  </div>
</template>

<script>
  import axios from 'axios'
  import drf from '@/api/drf'
  import { mapGetters } from 'vuex'
  import MovieList from "@/components/MovieList"

  export default {
    name: 'GenreRecommendView',
    components: { 
      MovieList
    },
    data: function () {
      return {
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
        selectedGenreName: '',
      }
    },
    computed: {
      ...mapGetters(['authHeader'])
    },
    methods: {
      selectGenre: function (idx) {


        this.selectedMovies = this.moviesByGenre[idx].movies
        this.selectedGenreName = this.moviesByGenre[idx].genre_name
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
    }
  }
</script>

<style>
#genre-reccomend-box {
  padding: 2rem;
}

#genre-box {
  display: flex;
}

.custom-btn {
  width: 130px;
  height: 40px;
  color: #fff;
  border-radius: 5px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  outline: none;
}

.btn-12{
  position: relative;
  right: 20px;
  bottom: 20px;
  border:none;
  box-shadow: none;
  width: 130px;
  height: 40px;
  line-height: 42px;
  -webkit-perspective: 230px;
  perspective: 230px;
}
.btn-12 span {
  display: block;
  position: absolute;
  width: 130px;
  height: 40px;
  border-radius: 5px;
  margin:0;
  text-align: center;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all .3s;
  transition: all .3s;
}

.btn-12 span:nth-child(1) {
  -webkit-transform: rotateX(90deg);
  -moz-transform: rotateX(90deg);
  transform: rotateX(90deg);
  -webkit-transform-origin: 50% 50% -20px;
  -moz-transform-origin: 50% 50% -20px;
  transform-origin: 50% 50% -20px;
  color: #00d7e2ec;
}

.btn-12 span:nth-child(2) {
  -webkit-transform: rotateX(0deg);
  -moz-transform: rotateX(0deg);
  transform: rotateX(0deg);
  -webkit-transform-origin: 50% 50% -20px;
  -moz-transform-origin: 50% 50% -20px;
  transform-origin: 50% 50% -20px;
}

.btn-12:hover span:nth-child(1) {
  -webkit-transform: rotateX(0deg);
  -moz-transform: rotateX(0deg);
  transform: rotateX(0deg);
}

.btn-12:hover span:nth-child(2) {
 color: transparent;
  -webkit-transform: rotateX(-90deg);
  -moz-transform: rotateX(-90deg);
  transform: rotateX(-90deg);
}
</style>