<template>
  <div>
    This is a movie recommendation by genre page.
    <div v-for="(data, idx) in moviesByGenre" :key="idx">
      <button @click="selectGenre(idx)">{{ data['genre_name'] }}</button>
    </div>
    <p>{{ selectedGenreName }}</p>
    <MovieList :movies="selectedMovies"/>
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

</style>