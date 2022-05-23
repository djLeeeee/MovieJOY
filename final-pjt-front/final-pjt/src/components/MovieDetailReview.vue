<template>
  <div class="movie-review-section">
    <p>This is a review section of the movie.</p>
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
  width: 30%;
  margin: 1rem;
}

</style>