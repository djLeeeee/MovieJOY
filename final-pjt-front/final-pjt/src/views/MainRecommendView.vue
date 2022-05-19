<template>
  <div>
    <TheNavbar />
    This is our main page.
  </div>
</template>

<script>
  import TheNavbar from '@/components/TheNavbar.vue'

  export default {
    name: 'MainRecommendationView',
    components: { 
      TheNavbar, 
    },
  }
</script>

<style>

</style>