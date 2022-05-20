<template>
  <div class="flip-card-container row row-cols-2 row-cols-md-3 row-cols-lg-4 row-cols-xxl-6 g-4" style="--hue: 220">
    <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'movieList',
  components: {
    MovieCard
  },
  props: {
    movies: Array,
  }
}
</script>

<style>
.flip-card-container {
  width: 100%;
  height: 100%;
}

</style>

