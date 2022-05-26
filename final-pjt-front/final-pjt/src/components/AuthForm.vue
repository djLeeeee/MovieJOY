<template>
  <div>
    <h3>This is auth form</h3>
    <div>
      <div v-if="isAuth">
        <div>
          <input type="text" name="phonenum" v-model="inputPhoneNumber" disabled>
          <label for="phonenum">Phone Number</label>
          <button @click="submitPhoneNumber()">Send</button>
        </div>
        <div>전화번호 인증 완료</div>
      </div>
      <div v-else>
        <input type="text" name="phonenum" v-model="inputPhoneNumber">
        <label for="phonenum">Phone Number</label>
        <button @click="submitPhoneNumber()">Send</button>
      </div>
      <div v-if="activeAuthNumForm">
        <input type="text" name="authnum" v-model="inputauthNumber">
        <label for="authnum">Auth Number</label>
        <button @click="submitAuthNumber()">Submit</button>
      </div>
      <div v-if="activePasswordChangeForm">
        <div>인증 성공!</div>
        <PasswordChangeForm />
      </div>
    </div>
  </div>
</template>

<script>
import drf from '@/api/drf'
import { mapGetters } from 'vuex'
import axios from 'axios'
import PasswordChangeForm from '@/components/PasswordChangeForm.vue'

export default {
  name: "AuthForm",
  props: {
    phonenumber: String
  },
  components: {
    PasswordChangeForm
  },
  data: function () {
    return {
      inputPhoneNumber: '',
      isAuth: true,
      activeAuthNumForm: false,
      inputauthNumber: '',
      activePasswordChangeForm: false,
    }
  },
  created () {
    if (this.phonenumber === '0') {
      this.isAuth = false
    } else {
      this.inputPhoneNumber = this.phonenumber
    }
  },
  computed: {
    ...mapGetters(['authHeader']),
  },
  methods: {
    submitPhoneNumber: function () {
      axios({
        url: drf.accounts.smsauth(this.inputPhoneNumber),
        method: "post",
        headers: this.authHeader
      })
      .then(res => {
        this.activeAuthNumForm = true
        console.log(res)
        return
      })
      .catch(res => {
        console.log(res)
        this.activeAuthNumForm = false
        alert("이미 인증 정보가 존재하는 번호입니다!")
        return
      })
    },
    submitAuthNumber: function () {
      const method = this.isAuth ? "PUT" : "post"
      axios({
        url: drf.accounts.smsdoauth(this.inputPhoneNumber, this.inputauthNumber),
        method: method,
        headers: this.authHeader
      })
      .then(res => {
        console.log(res)
        this.activePasswordChangeForm = true
        return
      })
      .catch(res => {
        console.log(res)
        this.activePasswordChangeForm = false
        alert("5분 안에 알맞은 인증 번호를 입력하세요.")
        return
      })
    }
  }
}
</script>

<style>

</style>