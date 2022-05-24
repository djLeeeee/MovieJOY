<template>
  <div class="movie-review-section">
    <p class="review-text">Reviews</p>
    <ReviewItem v-if="reviewed" :review="myreview"/>
    <div id="review-input-box" v-else>
      <div class="first-line">
        <div class="star-rate-box">
          <i data-id="1" class="fa-solid fa-star"></i>
          <i data-id="2" class="fa-solid fa-star"></i>
          <i data-id="3" class="fa-solid fa-star"></i>
          <i data-id="4" class="fa-solid fa-star"></i>
          <i data-id="5" class="fa-solid fa-star"></i>
        </div>
      </div>
    </div>
    <div>
      <ReviewList :reviews="reviews" />
    </div>
  </div>
</template>

<script>
import ReviewItem from '@/components/ReviewItem.vue'
import ReviewList from '@/components/ReviewList.vue'
import axios from 'axios'
import drf from '@/api/drf'
import { mapGetters } from 'vuex'

export default {
  name: "MovieDetailReview",
  components: {
    ReviewItem,
    ReviewList,
  },
  props: {
    movieId: Number,
  },
  data: function () {
    return {
      reviewed: false,
      reviews: [],
      myreview: '',
    }
  },
  computed: {
    ...mapGetters(['authHeader'])
  },
  created () {
    axios({
      url: drf.movies.movie(this.movieId),
      method: 'get',
    })
    .then(res => {
      this.reviews = res.data.reviews
      axios({
        url: drf.accounts.currentUserInfo(),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => {
        const userId = res.data.pk
        this.reviews.map(review => {
          if (review.user.id === userId) {
            this.reviewed = true
            this.myreview = review
          }
        })
        if (this.reviewed) {
          
          const idx = this.reviews.indexOf(this.myreview)
          this.reviews.splice(idx, 1)
        }
      })
    })
  }
}
</script>

<style>
.movie-review-section {
  width: 100%;
  margin: 1rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.star-rate-box {
  display: flex;
  justify-content: flex-start;
}

.review-text {
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
}
</style>