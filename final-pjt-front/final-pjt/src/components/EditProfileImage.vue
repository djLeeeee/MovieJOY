<template>
  <div>
    <h2>Choose the profile image</h2>
    <div id="img-list">
      <div v-for="(num, idx) in imageOption" :key="idx">
        <img :src="require(`@/assets/profile_img/img_${ num }.png`)" :data-id="num" @click="selectImage" alt="" />
      </div>
    </div>
    <div class="profile-img-buttons">
      <button @click="submitImgOption" class="btn authenticate-btn">Submit</button>
      <button @click="closeEditProfile" class="btn authenticate-btn">Close</button>
    </div>
  </div>
</template>

<script>
import _ from "lodash"
import axios from 'axios'
import drf from '@/api/drf'
import { mapGetters } from 'vuex'

export default {
  name: 'EditProfileImage',
  data: function () {
    return {
      selectedImgNumber: 0,
      imageOption: _.range(1, 25)
    }
  },
  computed: {
    ...mapGetters(['authHeader']),
  },
  methods: {
    closeEditProfile: function () {
      this.$emit('close-edit-profile')
    },
    selectImage: function (event) {
      const selected = event.target
      this.selectedImgNumber = selected.dataset.id
    },
    submitImgOption: function () {
      if (this.selectedImgNumber === 0) {
        this.closeEditProfile()
        return
      }
      axios({
        url: drf.accounts.imageUpdate(this.selectedImgNumber),
        method: 'post',
        headers: this.authHeader
      })
      .then(this.closeEditProfile())
    }
  }
}
</script>

<style>
.profile-img-buttons .authenticate-btn {
  margin-top: 0.5rem;
	color: rgb(51, 51, 51);
}

.profile-img-buttons .authenticate-btn:hover {
	color: #00666bec;
}
</style>