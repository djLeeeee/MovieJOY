<template>
  <div>
    <div class="star-box">
      <i :id="reviewStarPath" data-id="1" class="fa-solid fa-star"></i>
      <i :id="reviewStarPath" data-id="2" class="fa-solid fa-star"></i>
      <i :id="reviewStarPath" data-id="3" class="fa-solid fa-star"></i>
      <i :id="reviewStarPath" data-id="4" class="fa-solid fa-star"></i>
      <i :id="reviewStarPath" data-id="5" class="fa-solid fa-star"></i>
      {{ review.user.username }}
    </div>
    <div>
      {{ review.content }}
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewItem",
  props: {
    review: Object,
  },
  computed:{
    reviewStarPath: function () {
      return `review-${ this.review.id }-star`
    }
  },
  mounted () {
    const stars = document.querySelectorAll(`#${ this.reviewStarPath }`)
    for (let star of stars) {        
      if (star.dataset.id <= this.review.score) {
        star.style.color = '#01a8b1c4'
      } else {
        star.style.color = "rgba(240, 248, 255, 0.562)"
      }
    }
  },
  updated () {
    const stars = document.querySelectorAll(`#${ this.reviewStarPath }`)
    for (let star of stars) {        
      if (star.dataset.id <= this.review.score) {
        star.style.color = '#01a8b1c4'
      } else {
        star.style.color = "rgba(240, 248, 255, 0.562)"
      }
    }
  }
}
</script>

<style>

</style>