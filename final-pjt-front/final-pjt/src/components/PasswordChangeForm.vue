<template>
  <div>
    <div>
      <input type="password" v-model="password1">
      <label for="">Password</label>
    </div>
    <div>
      <input type="password" v-model="password2">
      <label for="">Password Confirm</label>
    </div>
    <button @click="submitChangedPassword(password1, password2)">Submit</button>
  </div>
</template>

<script>
import drf from '@/api/drf'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: "PasswordChangeForm",
  data: function () {
    return {
      password1: '',
      password2: '',
    }
  },
  computed: {
    ...mapGetters(['authHeader']),
  },
  methods: {
    submitChangedPassword (new_password1, new_password2) {
      axios({
        url: drf.accounts.changePassword(),
        method: "post",
        headers: this.authHeader,
        data: {
          new_password1,
          new_password2
        }
      })
      .then(res => {
        console.log(res)
        alert("변경 성공")
        return
      })
      .catch(res => {
        console.log(res)
        alert("변경 실패")
        return
      })
    }
  }
}
</script>

<style>

</style>