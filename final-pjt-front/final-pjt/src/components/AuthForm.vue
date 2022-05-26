<template>
  <div id="all-auth-box">
    <div id="auth-box">
      <div v-if="isAuth" class="phone-box">
        <div class="phonenum-box">
          <input type="text" name="phonenum" v-model="inputPhoneNumber">
          <label for="phonenum">Phone Number (비밀번호 변경은 추가 인증이 필요합니다.)</label>
          <button @click="submitPhoneNumber()" class="btn btn-link auth-box-btn">Send</button>
        </div>
      </div>
      <div v-else class="phone-box">
        <input type="text" name="phonenum" v-model="inputPhoneNumber">
        <label for="phonenum">Phone Number</label>
        <button @click="submitPhoneNumber()" class="btn btn-link auth-box-btn">Send</button>
      </div>
      <div v-if="activeAuthNumForm" class="phone-box">
        <input type="text" name="authnum" v-model="inputauthNumber">
        <label for="authnum">Auth Number</label>
        <button @click="submitAuthNumber()" class="btn btn-link auth-box-btn">Submit</button>
      </div>
      <div v-if="activePasswordChangeForm" class="phone-box">
        <input type="password" v-model="password1">
        <label>Password</label>
      </div>
      <div v-if="activePasswordChangeForm" class="phone-box">
        <input type="password" v-model="password2">
        <label>Password Confirm</label>
        <button @click="submitChangedPassword(password1, password2)" class="btn btn-link auth-box-btn">Submit</button>
      </div>
    </div>
  </div>
</template>

<script>
import drf from '@/api/drf'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: "AuthForm",
  props: {
    phonenumber: String
  },
  data: function () {
    return {
      inputPhoneNumber: '',
      isAuth: true,
      activeAuthNumForm: false,
      inputauthNumber: '',
      activePasswordChangeForm: false,
      password1: '',
      password2: '',
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
    },
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
#all-auth-box {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  margin-top: 3rem;
}

#auth-box::-webkit-scrollbar {
  width: 10px;
  background: #00d9e400;
}

#auth-box::-webkit-scrollbar-thumb {
  background-color: #00d9e444;
  border-radius: 10px;
}


#auth-box h2 {
  margin: 0 0 30px;
  padding: 0;
  color: #fff;
  text-align: center;
}

#auth-box .phone-box {
  position: relative;
  margin-top: 0.5rem;
}

#auth-box .phone-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 1.2rem;
  color: #fff;
  margin-bottom: 30px;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}

#auth-box .phone-box label {
  position: absolute;
  top:5;
  left: 0;
  padding: 10px 0;
  font-size: 1.2rem;
  color: #fff;
  pointer-events: none;
  transition: .5s;
}

#auth-box .phone-box input:focus ~ label,
#auth-box .phone-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: #01a8b1;
  font-size: 0.8rem;
}

.auth-box-btn {
  text-decoration: none;
  color: white;
  font-size: 1.3rem;
  border: none;
}
</style>