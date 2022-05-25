<template>
  <div id="user-review-item">
    <div class="star-box">
      <i :id="reviewStarPath" data-id="1" class="fa-solid fa-star"></i>
      <i :id="reviewStarPath" data-id="2" class="fa-solid fa-star"></i>
      <i :id="reviewStarPath" data-id="3" class="fa-solid fa-star"></i>
      <i :id="reviewStarPath" data-id="4" class="fa-solid fa-star"></i>
      <i :id="reviewStarPath" data-id="5" class="fa-solid fa-star"></i>
    </div>
    <p @click="isModalViewed=true, showModal()">{{ review.movie.name }}</p>
    <ModalView v-if="isModalViewed" @close-modal="isModalViewed=false">
      <MovieDetail :movieId="review.movie.tmdb_movie_id"/>
    </ModalView>
  </div>
</template>

<script>
import ModalView from "@/components/ModalView.vue"
import MovieDetail from "@/components/MovieDetail.vue"

export default {
  name: 'UserReviewItem',
  props: {
    review: Object,
  },
  data: function () {
    return {
      isModalViewed: false,
    }
  },
  components: {
    ModalView,
    MovieDetail,
  },
  computed:{
    reviewStarPath: function () {
      return `review-${ this.review.id }-star`
    }
  },
  mounted () {
    const stars = document.querySelectorAll(`#${ this.reviewStarPath }`)
    for (let star of stars) {        
      if (star.dataset.id <= this.review.score) {
        star.style.color = '#01a8b1c4'
      } else {
        star.style.color = "rgba(240, 248, 255, 0.562)"
      }
    }
  },
  methods: {
    showModal () {
      document.body.classList.add("modal-open");
    },
  }
}
</script>

<style>
#user-review-item {
  display: flex;
  vertical-align: center;
}

#user-review-item p {
  font-size: 1.2rem;
  margin-top: 5px;
}

@media ( max-width: 830px ) {
  #user-review-item p {
  font-size: 1rem;
  margin-top: 5px;
  }

  .fa-star {
    font-size: 1rem;
  }
}

</style>