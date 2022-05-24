<template>
  <div>
    {{ review.score }}
    {{ review.user.username }}
    {{ review.content }}
  </div>
</template>

<script>
export default {
  name: "ReviewItem",
  props: {
    review: Object,
  }
}
</script>

<style>

</style>