<template>
  <div id="review-item-box">
    <div id="review-writer-info-box">
      <img src="@/assets/base_profile_img.jpeg" alt="">
      <div class="writer-info">
        <div class="star-box">
          <i :id="reviewStarPath" data-id="1" class="fa-solid fa-star"></i>
          <i :id="reviewStarPath" data-id="2" class="fa-solid fa-star"></i>
          <i :id="reviewStarPath" data-id="3" class="fa-solid fa-star"></i>
          <i :id="reviewStarPath" data-id="4" class="fa-solid fa-star"></i>
          <i :id="reviewStarPath" data-id="5" class="fa-solid fa-star"></i>
        </div>
        <p>{{ review.user.nickname || review.user.username }}</p>
      </div>
    </div>
    <div style="color: white;">
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
#review-item-box {
  margin-bottom: 2rem;
  padding-left: 0.2rem;
}

#review-writer-info-box {
  display: flex;
  flex-direction: row;
  vertical-align: center;
}

#review-writer-info-box img {
  width: 50px;
  height: 50px;
  border-radius: 50px;
  margin-top: 3px;
}

.writer-info {
  display: flex;
  flex-direction: column;
}

.writer-info p {
  color: white; 
  font-size: 0.8rem; 
  text-align: left;
  margin-left: 10px;
}

.star-box {
  display: flex;
  justify-content: flex-start;
  margin: 0.5rem;
}
</style>