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
        this.trailerURL = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAHsAsQMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABAUCAwYBB//EADMQAAICAQMBBAgEBwAAAAAAAAABAgMEERIhMQUiUbETFBU0QWFxkjIzUnMjQmJygZGh/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/APrYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA15FjppnYq5WbVrtiKLq8iqNtT1g/8AnyZnKWyLm+kU5cfI52Gf6LLd2PVsrn+OrdxIDoJ2VwellkIPwlJIQsrm9IThJ6a6RkmUWXiSyprJwt18LXz+qD8GRZ1ZGHZGcoTqmuYtoDqgVNfa17odssPWEeJTjLReXzLSElOEZR10kk1qBkAAAAAAAAAAAAAAAAAAAAAAADXke73fty8jkvgdbke72/2S8jkl0As7rfZee4UJuChFWQctd705+hLx6vTJwhOV+Dcn+Ll0y6/UhOzHza4esWujIhHa7NNYzS6a+DPK7q+z7IvGyPWE/wAyO3bFr5ARFfbCiWOp6VN6uKXU6jH92p/bj5HP5uLFVrJxHux5cPnmt+DL/G93p/bj5AbQAAAAAAAAAAAAAAAAAAAAAGLnBOScopxWr56LxPVz0ANJrRpNPh6kH2Th6/gn95O3R3OOq3LlrXlHoED2Rh/on949kYX6J/eTwBWW4ksDW7Di7KtNLqZPXdEn49td1ELKfy2u7x0+Q9YpVqr9PWrNdFDet3+jNLRaJaJLoB6AYucVOMHJKUtXGLfL06+YGQAAAAAAAAAAAAAAAAAApO1cHItycu/Hg3N4qqitVpYnu3R+vKaNlVGas6p7bUlOPeVn8NVbNHFx167tX08OS3AFTk4mRZ2jZOEbFVOVClKE9usVu3cp6/FEeON2jVjS2+sSslQ091rb3KzjTV9dmvgXwA5fLeXi4C9anfHu3KpK3bLdxsb72r4+GrLHFozl2rKy2d3oedvxg46LRPvddf6f8ltouOOnQ9AracO9Zmbfu2b7d1alCL3dyKT16rkiUU59cYzlXlNQdMpwnapSskm97jz0fHHH0L0AUHq3aMqJTayY2xrk64q7+f0ja150fd06m/GxsldrRuurue30ydjs1g05LZtWvHC8EXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/2Q=="
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