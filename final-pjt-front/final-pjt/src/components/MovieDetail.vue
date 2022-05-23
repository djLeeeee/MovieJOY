<template>
  <div>
    <section id="movie-detail-section">
      <MovieDetailInfoSection :movieId="movieId" />
      <MovieDetailReview :movieId="movieId" />
    </section>
  </div>
</template>

<script>
import MovieDetailInfoSection from "@/components/MovieDetailInfoSection.vue"
import MovieDetailReview from "@/components/MovieDetailReview.vue"

export default {
  props: {
    movieId: Number,
  },
  components: {
    MovieDetailInfoSection,
    MovieDetailReview,
  },
}
</script>

<style>
#movie-detail-section {
  display: flex;
}
</style>