<template>
  <div class="movie-review-section">
    <p class="review-text">Reviews</p>
    <div id="review-input-box">
      <div class="first-line">
        <div class="star-rate-box">
            <i data-id="1" class="fa-solid fa-star"></i>
            <i data-id="2" class="fa-solid fa-star"></i>
            <i data-id="3" class="fa-solid fa-star"></i>
            <i data-id="4" class="fa-solid fa-star"></i>
            <i data-id="5" class="fa-solid fa-star"></i>
          </div> 
        <button>Submit</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieDetailReview",
  props: {
    movieId: Number,
  },
}
</script>

<style>
.movie-review-section {
  width: 100%;
  margin: 0.5rem;
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