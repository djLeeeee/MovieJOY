<template>
  <div class="movie-info-section">
    <div class="trailer-container">
      <iframe :src="trailerURL" frameborder="0"></iframe>
    </div>
    <section class="information-container">
        <h2 class="movie-title">{{ movie.name }}</h2>
        <div class="score-like-button-box">
          <h2 class="movie-score">{{ movie.vote_average }}</h2>
          <h2 class="movie-button">
            <i class="fa-solid fa-heart-circle-plus" id="movie-normal-button" v-if='normal' @click='movielike(), normal=false, like=true'/>
            <i class="fa-solid fa-heart-circle-check" id="movie-like-button" v-if='like' @click='movielike(), like=false, dislike=true'/>
            <i class="fa-solid fa-heart-circle-xmark" id="movie-dislike-button" v-if='dislike' @click='movielike(), dislike=false, normal=true'/>
          </h2>
        </div>
    </section>
    <div class="overview-container">
      {{ movie.overview }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'
import { mapGetters } from 'vuex'

export default {
  name: "MovieDetailInfoSection",
  props: {
    movieId: Number,
    movieName: String,
  },
  data: function () {
    return {
      trailerURL: '',
      movie: {},
      like: false,
      dislike: false,
      normal: false,
    }
  },
  methods: {
    movielike () {
      axios({
        url: drf.movies.likeMovie(this.movieId),
        method: 'post',
        headers: this.authHeader
      })
    },
  },
  computed: {
    ...mapGetters(['authHeader'])
  },
  created () {
    axios({
      url: `https://api.themoviedb.org/3/movie/${this.movieId}/videos`,
      method: 'get',
      params: {
        'api_key': '52962731aacacff3f5f9da655947bff6',
        'region': 'KR',
        'language': 'ko',
      }
    })
    .then(res => {
      if (res.data.results[0]) {
        this.trailerURL = 'https://www.youtube.com/embed/' + res.data.results[0]['key']
      }
      else {
        console.log(this.movieName)
        const API_KEY = 'AIzaSyCJ83Db4TiQbjAQ9V2Nqg8ClYPueu01YOc'
        const API_URL = 'https://www.googleapis.com/youtube/v3/search'
        const params = {
          key: API_KEY,
          part: 'snippet',
          q: this.movieName,
          type: 'video',
        }
        axios.get(API_URL, {params,})
        .then(res => {
          const selected = res.data.items[0]
          this.trailerURL = `https://www.youtube.com/embed/${selected.id.videoId}`
        })
      }
    })

    axios({
      url: drf.movies.movie(this.movieId),
      method: 'get',
    })
    .then(res => {
      this.movie = res.data
      axios({
        url: drf.accounts.currentUserInfo(),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => {
        const userId = res.data.pk
        const like_users = this.movie.like_users
        const dislike_users = this.movie.dislike_users
        if (like_users.includes(userId)) {
          this.like = true
        } else if (dislike_users.includes(userId)) {
          this.dislike = true
        } else {
          this.normal = true
        }
      })
    })
  }
}
</script>

<style>

.movie-info-section {
  margin: 1rem;
}

.trailer-container {
  position: relative;
  padding-top: 50%;
}

.trailer-container > iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%
}

.information-container  {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.movie-title {
  text-align: left;
  color: white;
  font-weight: bold;
}

.score-like-button-box {
  display: flex;
}

.movie-score {
  color: white;
  font-weight: bold;
  margin-right: 1rem;
}

#movie-normal-button {
  text-align: center;
  color: white;
}

#movie-like-button {
  text-align: center;
  color: crimson;
}

#movie-dislike-button {
  text-align: center;
  color: rgb(70, 70, 70);
}

.overview-container {
  margin-top: 1rem;
  text-align: left;
  color: white;
}
</style>