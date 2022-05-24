<template>
 <div class="col">
  <ModalView v-if="isModalViewed" @close-modal="isModalViewed=false">
    <MovieDetail :movieId="this.movie.id || this.movie.tmdb_movie_id"/>
  </ModalView>
  <div class="flip-card" @click="isModalViewed=true, showModal()">
    <div class="card-front">
      <figure>
        <div class="img-bg"></div>
        <img :src="posterPath" :alt="movie.title">
      </figure>
    </div>

    <div class="card-back">
      <figure>
        <div class="img-bg"></div>
        <img :src="posterPath" :alt="movie.title">
      </figure>

      <ul class="card-ul">
        <li>{{ movie.title || movie.name }}</li>
        <div class="star-box">
          <i :id="idPath" data-id="1" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="2" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="3" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="4" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="5" class="fa-solid fa-star"></i>
        </div>
      </ul>
    </div>
  </div>
 </div>
</template>

<script>
import ModalView from "@/components/ModalView.vue"
import MovieDetail from "@/components/MovieDetail.vue"

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  components: {
    ModalView,
    MovieDetail,
  },
  data: function () {
    return {
      isModalViewed: false,
    }
  },
  methods: {
    showModal () {
      document.body.classList.add("modal-open");
    }
  },
  computed: {
    posterPath: function () {
      const poster_path = this.movie.poster_path
      return `https://image.tmdb.org/t/p/original/${poster_path}`
    },
    idPath: function () {
      return `movie-${ this.movie.id || this.movie.tmdb_movie_id }`
    }
  },
  mounted() {
    const voteAverage = Math.round(this.movie.vote_average / 2)
    const stars = document.querySelectorAll(`#movie-${ this.movie.id || this.movie.tmdb_movie_id }`)
    for(let star of stars) {
      const num = star.dataset.id
      if(voteAverage - num >= 0) {
        star.style.color = '#01a8b1c4'
      } 
    }
  },
  updated() {
    const voteAverage = Math.round(this.movie.vote_average / 2)
    const stars = document.querySelectorAll(`#movie-${ this.movie.id || this.movie.tmdb_movie_id }`)
    for(let star of stars) {
      const num = star.dataset.id
      if(voteAverage - num >= 0) {
        star.style.color = '#01a8b1c4'
      } else {
        star.style.color = 'rgba(240, 248, 255, 0.562)'
      }
    }
  }
}

</script>

<style>
.flip-card {
  width: 15rem;
  height: 20rem;
  position: relative;
  transform-style: preserve-3d;
  transition: .3s .1s;
}

.flip-card:hover,
.flip-card:focus {
  transform: rotateY(180deg);
}

.card-front,
.card-back {
  width: 100%;
  height: 100%;
  border-radius: 24px;

  background: var(--dark);
  position: absolute;
  top: 0;
  left: 0;
  overflow: hidden;

  backface-visibility: hidden;

  display: flex;
  justify-content: center;
  align-items: center;
}

/* .card-front */
.card-front {
  transform: rotateY(0deg);
  z-index: 2;
}

/* .card-back */
.card-back {
  transform: rotateY(180deg);
  z-index: 1;
}

/* figure */
figure {
  z-index: -1;
}

/* figure, .img-bg */
figure,
.img-bg {
  position: absolute;
  top: 0;
  left: 0;

  width: 100%;
  height: 100%;
}

/* img */
.flip-card img {
  width: 100%;
  height: 100%;
  border-radius: 24px;
}


/* .img-bg */

.card-back .img-bg {
  background: rgba(0, 0, 0, 0.493);
}



.card-ul {
  list-style: none;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-right: 2rem;
}


.card-ul li {
  width: 100%;
  margin-top: 12px;
  padding-bottom: 12px;
  font-size: 1.5rem;
  text-shadow: rgba(255, 255, 255, 0.308) 1px 1px;
  text-align: center;
  position: relative;
}

.fa-star {
  text-shadow: rgba(155, 155, 155, 0.418) 1px 1px;
  font-size: 1.2rem;
  color: rgba(240, 248, 255, 0.562);
}
</style>