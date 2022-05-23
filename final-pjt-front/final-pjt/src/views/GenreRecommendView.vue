<template>
  <div id="genre-reccomend-box">
    <div class="genre-buttons" id="genre-box">
      <button v-for="(data, idx) in moviesByGenre" :key="idx" @click="selectGenre(idx)" class="raise">
          <span>{{ data['genre_name'] }}</span>
      </button>
    </div>
    <div id="genre-movie-box">
      <h3 style="color: white;">{{ selectedGenre }}</h3>
      <MovieList :movies="selectedMovies"/>
    </div> 
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
      MovieList,
    },
    data: function () {
      return {
        windowWidth: window.innerWidth,
        smallBox: false,
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
    mounted() {
          window.addEventListener('resize', this.handleResize);
    },
    beforeDestroy() {
          window.removeEventListener('resize', this.handleResize);
    },
    computed: {
      ...mapGetters(['authHeader'])
    },
    methods: {
      selectGenre: function (idx) {
        this.selectedMovies = this.moviesByGenre[idx].movies
        this.selectedGenre = this.moviesByGenre[idx].genre_name
      },
      handleResize: function () {
        this.windowWidth = window.innerWidth;
        if (this.windowWidth < 1200) {
          this.smallBox = true
        } else {
          this.smallBox = false
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
  }
</script>

<style>
#genre-reccomend-box {
  display: flex;
  justify-content: center;
}

#genre-box {
  margin-top: 5rem;
  width: 450px;
  height: 100%;
}

.genre-buttons button {
  width: 6rem;
  background: none;
  border: 2px solid;
  font: inherit;
  line-height: 1;
  margin: 0.5em;
  padding: 0.5em;
  color: white;
  font-size: 0.9rem;
  transition: all .5s;
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
</style>