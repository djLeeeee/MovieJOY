<template>
  <div class="movie-review-section">
    <p class="review-text">Reviews</p>
    <div v-if="reviewed">
      <ReviewItem  :review="myreview"/>
      <button @mousedown="editReview()">수정</button>
      <button @click="deleteReview()">삭제</button>
    </div>
    <div id="review-input-box" v-else>
      <div class="first-line">
        <div class="star-rate-box">
          <i :id="reviewIdPath" data-id="1" class="fa-solid fa-star" @click="selectStar"></i>
          <i :id="reviewIdPath" data-id="2" class="fa-solid fa-star" @click="selectStar"></i>
          <i :id="reviewIdPath" data-id="3" class="fa-solid fa-star" @click="selectStar"></i>
          <i :id="reviewIdPath" data-id="4" class="fa-solid fa-star" @click="selectStar"></i>
          <i :id="reviewIdPath" data-id="5" class="fa-solid fa-star" @click="selectStar"></i>
        </div>
      </div>
      <div>
        <input v-model="myreview.content" type="text" name="" class="review-content-input-box" required />
        <button @click="submitReview()">제출</button>
      </div>
    </div>
    <div>
      <ReviewList v-if="othersreviewed" :reviews="reviews" />
      <div v-else>리뷰가 없습니다!</div>
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
      othersreviewed: false,
      reviews: [],
      myreview: {
        'content': '',
        'score': 0,
      },
    }
  },
  methods: {
    deleteReview () {
      axios({
        url: drf.movies.review_ud(this.movieId, this.myreview.id),
        method: 'delete',
        headers: this.authHeader
      })
      this.reviewed = false
      this.myreview = {
        'content': '',
        'score': 0,         
      }
    },
    editReview () {
      this.reviewed = false
    },
    updateStar () {
      const stars = document.querySelectorAll(`#movie-${ this.movieId }-review`)
      for (let star of stars) {        
        if (star.dataset.id <= this.myreview.score) {
          star.style.color = '#01a8b1c4'
        } else {
          star.style.color = "rgba(240, 248, 255, 0.562)"
        }
      }
    },
    submitReview () {
      if ( this.myreview.score === 0 || this.myreview.content === '' ) {
        alert('올바른 값을 입력해주세요!')
        return
      }
      axios({
        url: drf.movies.reviews(this.movieId),
        method: 'post',
        headers: this.authHeader,
        data: {
          content: this.myreview.content,
          score: this.myreview.score,
        }
      })
      .then(res => {
        this.myreview = res.data
        this.reviewed = true
      })
    },
    selectStar: function (event) {
      const selectScore = event.target.dataset.id
      this.myreview.score = selectScore
      const stars = document.querySelectorAll(`#movie-${ this.movieId }-review`)
      for (let star of stars) {
        if (star.dataset.id <= selectScore) {
          star.style.color = '#01a8b1c4'
        } else {
          star.style.color = "rgba(240, 248, 255, 0.562)"
        }
      }
    },
  },
  computed: {
    ...mapGetters(['authHeader']),
    reviewIdPath: function () {
      return `movie-${ this.movieId }-review`
    }
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
        if (this.reviews.length > 0) {
          this.othersreviewed = true
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

.review-input-box {
  width: 80%;
}
</style>