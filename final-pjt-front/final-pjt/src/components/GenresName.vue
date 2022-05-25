<template>
  <div>
    <div style="margin-left: 10px;" v-for="(genre, idx) in likeGenres" :key="idx">
      {{ genre.name }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'GenresName',
  props: {
    likeGenres: Array
  }
}
</script>

<style>

</style>