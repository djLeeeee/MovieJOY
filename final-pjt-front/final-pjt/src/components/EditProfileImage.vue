<template>
  <div>
    <h5>Choose the profile image</h5>
    <div id="img-list" class="row">
      <div class="col" v-for="(num, idx) in imageOption" :key="idx">
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
  props: {
    userProfileImage: Number
  },
  computed: {
    ...mapGetters(['authHeader']),
  },
  mounted () {
    const userImage = document.querySelector(`img[data-id="${this.userProfileImage}"]`)
    userImage.classList.add('img-active')
    this.selectedImgNumber = this.userProfileImage
  },
  methods: {
    closeEditProfile: function () {
      this.$emit('close-edit-profile')
    },
    selectImage: function (event) {
      const nowActive = document.querySelector(`img[data-id="${this.selectedImgNumber}"]`)
      nowActive.classList.remove('img-active')

      const selected = event.target
      selected.classList.add('img-active')
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

#img-list {
  display: flex;
  
}

#img-list div img {
  width: 80px;
  height: 80px;
  border-radius: 100%;
  margin: 10px;
}

#img-list div img:hover {
  transform: scale(1.2);
  border: solid 3px #00666bec;
  transition: .3s;
}

.img-active {
  transform: scale(1.2);
  border: solid 3px #00666bec;
  box-shadow: 3px 3px 7px rgba(0, 0, 0, 0.548);
  transition: .3s;
}

.profile-img-buttons {
  margin-top: 1rem;
}
</style>