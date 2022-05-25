<template>
  <div>
    <h2>Choose the profile image</h2>
    <div id="img-list">

    </div>
    <div class="profile-img-buttons">
      <button class="btn authenticate-btn">Submit</button>
      <button @click="closeEditProfile" class="btn authenticate-btn">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EditProfileImage',
  methods: {
    closeEditProfile: function () {
      this.$emit('close-edit-profile')
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