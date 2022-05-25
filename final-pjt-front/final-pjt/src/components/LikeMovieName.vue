<template>
  <div>
    <div @click="isModalViewed=true, showModal()">{{ movie.name }}</div>
    <ModalView v-if="isModalViewed" @close-modal="isModalViewed=false">
      <MovieDetail :movieId="movie.tmdb_movie_id"/>
    </ModalView>
  </div>
</template>

<script>
import ModalView from "@/components/ModalView.vue"
import MovieDetail from "@/components/MovieDetail.vue"


export default {
  name: 'LikeMovieName',
  props: {
    movie: Object
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
    },
  }
}
</script>

<style>

</style>