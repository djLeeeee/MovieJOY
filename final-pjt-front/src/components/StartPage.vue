<template>
  <div id="main-box">
    <transition name="fade">
      <div v-if="!isSignupOpen" id="authenticate-box-flex">
        <div id="authenticate-box">
          <transition name="fade">
            <div v-if="isLoginOpen" class="login-box">
              <div class="user-box">
                <input v-model="credentials.username" type="text" name="" required />
                <label>Username</label>
              </div>
              <div class="user-box">
                <input @keypress.enter="login(credentials)" v-model="credentials.password" type="password" name="" required />
                <label>Password</label>
              </div>
              <div class="login-buttons">
                <button @click.prevent="login(credentials)" class="btn authenticate-btn">Submit</button>
                 <button @click="onLoginOpen(), clearErrorList()" class="btn authenticate-btn">Back</button>
                <button @click="kakaoLogin()" class="btn authenticate-btn">
                  <img src="@/assets/kakao-icon.png" class="kakao-icon" alt="kakao-icon">
                </button>                
              </div>
              <div class="find-buttons">
                  <button class="btn" @click="onFindIdOpen">Find ID</button>
                  <button class="btn" @click="onFindPwOpen">Find PW</button>
                </div>
              <div class="login-error-box" v-if="loginAuthError">
                <div v-for="(errors, field) in loginAuthError" :key="field">
                  <p v-for="(error, idx) in errors" :key="idx">
                    {{ error }}
                  </p>
                </div>
              </div>
            </div>
          </transition>
          <transition name="fade">
            <div v-if="isFindIdOpen" class="find-box">
              <div class="user-id-auth-box">
                <input v-model="inputPhoneNumber" @keypress.enter="submitPhoneNumber" type="text" name="" required />
                <label>User Phone Number</label>
              </div>  
              <p style="margin-left: 2rem; font-size: .9rem;">인증한 핸드폰 번호를 "-" 없이 입력해주세요</p>
              <div class="user-id-auth-box" style="margin-top: 1rem; margin-bottom: 1rem;">
                <input v-model="vertificationCode" @keypress.enter="submitAuthNumber" type="text" name="" required />
                <label>Vertification Code</label>
              </div>
              <div>
                <button style="margin-left: 1.2rem;" class="btn authenticate-btn">Submit</button>
                <button @click="onFindIdOpen" class="btn authenticate-btn">Back</button>
              </div>
            </div>
          </transition>
          <transition name="fade">
            <div v-if="isFindPwOpen" class="find-box">
              <div class="user-box">
                <input v-model="credentials.username" type="text" name="" required />
                <label>Username</label>
              </div>  
              <div class="user-box">
                <input v-model="inputPhoneNumber" @keypress.enter="submitPhoneNumber" type="text" name="" required />
                <label>User Phone Number</label>
              </div>  
              <p style="margin-left: 2rem; font-size: .9rem;">인증한 등록한 핸드폰 번호를 "-" 없이 입력해주세요</p>
              <div class="user-box">
                <input v-model="vertificationCode" @keypress.enter="submitAuthNumberPW" type="text" name="" required />
                <label>Vertification Code</label>
              </div>
              <div>
                <button style="margin-left: 1.2rem;" class="btn authenticate-btn">Submit</button>
                <button @click="onFindPwOpen" class="btn authenticate-btn">Back</button>
              </div>
            </div>
          </transition>
          <transition name="fade">
            <div v-if="isChangePwOpen" class="find-box">
              <div class="user-id-auth-box">
                <input v-model="newPW" type="text" name="" required />
                <label>New Password</label>
              </div>
              <div class="user-id-auth-box" style="margin-top: 1rem; margin-bottom: 1rem;">
                <input v-model="newPWConfirm" @keypress.enter="submitNewPW" type="text" name="" required />
                <label>Password Confirm</label>
              </div>
              <div>
                <button @click="submitNewPW" style="margin-left: 1.2rem;" class="btn authenticate-btn">Submit</button>
                <button @click="onChangePwOpen" class="btn authenticate-btn">Back</button>
              </div>
            </div>
          </transition>
          <transition name="fade">
              <div v-if="isMainOpen" class="not-login-Box">
                <div class="wrapper">
                  <h1 class="typing-message">Find the movie U want.</h1>
                </div>
                <div class="ahthenticate-btn-box">
                  <button @click="onLoginOpen" class="btn authenticate-btn" style="margin-left: 1.5rem">Login</button>
                  <button @click="onSignupOpen" class="btn authenticate-btn">Signup</button>
                </div>
              </div>
          </transition>      
        </div>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="isSignupOpen" id="signup-box-flex">
        <SignupPage @signup-close="onSignupOpen(), clearErrorList()" />
      </div>
    </transition>
  </div>
</template>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script>
  import axios from 'axios'
  import SignupPage from "./SignupPage.vue"
  import { mapActions, mapGetters } from 'vuex'
  import drf from '@/api/drf'
  import router from '@/router'

  export default {
    name: 'StartPage',
    components: {
      SignupPage,
    },
    data: function () {
      return {
        isMainOpen: true,
        isLoginOpen: false,
        isSignupOpen: false,
        isFindIdOpen: false,
        isFindPwOpen: false,
        isChangePwOpen: false,
        inputPhoneNumber: '',
        phoneNumber: '',
        vertificationCode: '',
        newPW: '',
        newPWConfirm: '',
        credentials: {
          'username': '',
          'password': '',
        },
      }
    },
    mounted () {
      if (this.isLoggedIn) {
        router.push({ name: 'mainrecommend' })
      }
    },
    computed: {
      ...mapGetters(['loginAuthError', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['login', 'signup', 'clearErrorList', 'logout']),
  
      submitPhoneNumber: function () {
        axios({
          url: drf.accounts.smsauth(this.inputPhoneNumber),
          method: "post",
          data: this.credentials,
        })
        .then(res => {
          console.log(res)
          this.phoneNumber = this.inputPhoneNumber
          this.inputPhoneNumber = "인증번호 발송 완료"
        })
        .catch(err => {
          console.log(err)
          alert("해당 전화번호 정보를 찾을 수 없습니다.")
        })
      },

      submitAuthNumber: function () {
        axios({
          url: drf.accounts.smsdoauth(this.phoneNumber, this.vertificationCode),
          method: "post",
          data: this.credentials,
        })
        .then(res => {
          console.log(res)
          alert(`아이디는 ${res.data.username} 입니다.`)
          this.inputPhoneNumber = this.phoneNumber
          this.vertificationCode = ''
          this.isLoginOpen = true
          this.isFindIdOpen = false
          this.credentials.username = res.data.username
        })
        .catch(err => {
          console.log(err)
          alert("5분 안에 알맞은 인증 번호를 입력하세요.")
        })
      },

      submitAuthNumberPW: function () {
        axios({
          url: drf.accounts.smsdoauth(this.phoneNumber, this.vertificationCode),
          method: "put",
          data: this.credentials,
        })
        .then(res => {
          console.log(res)
          this.inputPhoneNumber = this.phoneNumber
          this.vertificationCode = ''
          this.isChangePwOpen = true
          this.isFindPwOpen = false
        })
        .catch(err => {
          if (err.response['status'] === 404) {
            alert("존재하지 않는 유저 정보입니다.")
          } else if (err.response['status'] === 400) {
            alert("올바르지 않은 인증 번호입니다.")
          } else if (err.response['status'] === 406) {
            alert("시간 초과입니다. 새로 인증 번호를 발급 받으세요")
          } else {
            alert("예기치 못한 에러가 발생했습니다. 페이지를 새로 고침하세요.")
          }
        })
      },

      submitNewPW: function () {
        if (this.newPW === this.newPWConfirm) {
          axios({
            url: drf.accounts.newPassword(),
            method: 'put',
            data: {
              'username': this.credentials.username,
              'password': this.newPW,
            }
          })
          .then(res => {
            console.log(res)
            alert("변경 성공! 변경된 정보로 로그인을 진행하세요.")
            this.onChangePwOpen()
          })
          .catch(err => {
            if (err.response['status'] === 404) {
              alert("인증 정보가 만료되었습니다. 전화번호 인증을 다시 진행해주세요.")
            } else if (err.response['status'] === 406) {
              alert("이전 비밀번호로는 변경 불가합니다.")
            } else {
              alert("사용할 수 없는 비밀번호입니다. 다시 입력하세요.")
            }
          })
        } else {
          alert("비밀번호와 비밀번호 확인이 일치하지 않습니다.")
        }
      },

      onLoginOpen: function () {
        this.isLoginOpen = !this.isLoginOpen
        this.isMainOpen = !this.isMainOpen
        this.credentials.username = ''
        this.credentials.password = ''
      },

      onSignupOpen: function () {
        this.isSignupOpen = !this.isSignupOpen
      },

      onFindIdOpen: function () {
        this.isLoginOpen = !this.isLoginOpen
        this.isFindIdOpen = !this.isFindIdOpen
      },

      onFindPwOpen: function () {
        this.isLoginOpen = !this.isLoginOpen
        this.isFindPwOpen = !this.isFindPwOpen
      },

      onChangePwOpen: function () {
        this.isChangePwOpen = false
        this.isLoginOpen = true
      },

      kakaoLogin: function () {
        window.Kakao.Auth.login({
          scope: 'profile_nickname',
          success: this.getKakaoAccount,
        })
      },

      getKakaoAccount: function () {
        window.Kakao.API.request({
          url: '/v2/user/me',
          success: res => {
            const kakao_account = res.kakao_account
            const kakao_id = res.id
            const nickname = kakao_account.profile.nickname
            const username = nickname + kakao_id
            const password = "kakaosocialuser1"
            const credentials = {
              username,
              password,
              password1: password,
              password2: password,
            }
            axios({
              url: drf.accounts.profile(username),
              method: 'get'
            })
            .then(res => {
              this.login(credentials)
            })
            .catch(res => {
              console.log("error")
              const payload = {
                  genres: [],
                  credentials,
                }
              this.signup(payload)
              }
            )
          },
          fail: error => {
            alert(error)
          }
        })
      }
    }
  }
</script>

<style>
@font-face {
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

  #main-box {
    background-image: url('https://images.unsplash.com/photo-1539035104074-dee66086b5e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjI0MX0&auto=format&fit=crop&w=2550&q=80');
    /* background-image: url('@/assets/main_dark.jpg'); */
    background-size: 100vw 100vh;
    background-repeat: no-repeat;
    width: 100%;
    height: 100vh;
    position: absolute;
    font-family: 'GmarketSansMedium'
  }

  #authenticate-box-flex {
    width: 100%;
    height: 100%;
    display: flex;
    color: white;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    position: fixed-top;
  }

  #signup-box-flex {
    width: 100%;
    height: 100vh;
    display: flex;
    justify-items: center;
    position: relative;
  }

  #authenticate-box {
    width: 100%;
    display: flex;
    height: 20rem;
    flex-direction: column;
    align-items: flex-start;
    background-color: rgba(0, 0, 0, 0.678);
    justify-content: center;
  }

  .ahthenticate-btn-box {
    display: flex;
    justify-content: flex-start;
  }

  .authenticate-btn {
    text-decoration: none;
    color: white;
    font-size: 1.3rem;
    border: none;
  }

  .authenticate-btn:hover {
    transform: scale(1.1);
    /* background-color: rgba(255, 255, 255, 0.329); */
    color: #00d8e4;
  }

  .authenticate-btn:active {
    color: #00d8e4;
  }

  .wrapper {
    /*This part is important for centering*/
    display: grid;
    place-items: left;
    margin-left: 2rem;
  }

  .typing-message {
    width: 100%;
    animation: typing 2s steps(22), blink .5s step-end infinite alternate;
    white-space: nowrap;
    overflow: hidden;
    border-right: 3px solid;
    font-size: 2.3em;
  }

  @keyframes typing {
    from {
      width: 0;
    }
  }
      
  @keyframes blink {
    50% {
      border-color: transparent;
    }
  }

  .login-box,
  .find-box {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .login-box .user-box,
  .find-box .user-box {
    position: relative;
    margin-left: 2rem;
  }

  .find-box .user-id-auth-box {
    position: relative;
    margin-left: 2rem;
  }

  .login-box .user-box input {
    width: 100%;
    padding: 10px 0;
    font-size: 1.5rem;
    color: #fff;
    margin-bottom: 20px;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    background: transparent;
  }

  .find-box .user-id-auth-box input,
  .find-box .user-box input {
    width: 100%;
    padding: 10px 0;
    font-size: 1.2rem;
    color: #fff;
    margin-bottom: 20px;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    background: transparent;
  }

  .login-box .user-box label {
    position: absolute;
    top:0;
    left: 0;
    padding: 10px 0;
    font-size: 1.5rem;
    color: #fff;
    pointer-events: none;
    transition: .5s;
  }

  .find-box .user-id-auth-box label,
  .find-box .user-box label {
    position: absolute;
    top:0;
    left: 0;
    padding: 15px 0;
    font-size: 1.2rem;
    color: #fff;
    pointer-events: none;
    transition: .5s;
  }

  .login-box .user-box input:focus ~ label,
  .login-box .user-box input:valid ~ label {
    top: -20px;
    left: 0;
    color: #00d8e4;
    font-size: 1rem;
  }

  .find-box .user-box input:focus ~ label,
  .find-box .user-box input:valid ~ label {
    top: -20px;
    left: 0;
    color: #00d8e4;
    font-size: .7rem;
  }

  .find-box .user-id-auth-box input:focus ~ label,
  .find-box .user-id-auth-box input:valid ~ label {
    top: -20px;
    left: 0;
    color: #00d8e4;
    font-size: .7rem;
  }

  .login-buttons {
    display: flex;
    justify-content: flex-start;
    margin-top: 2rem;
    font-size: 1.5rem;
    margin-left: 1rem;
  }

  .find-buttons {
    display: flex;
    justify-content: flex-start;
    margin-left: 1rem;
  }

  .find-buttons button {
    border: none;
    color: rgba(255, 255, 255, 0.678);
    font-size: .9rem;
    transition: .3s;
  }

  .find-buttons button:hover,
  .find-buttons button:focus {
    color: #00d8e4;
    transform: scale(1.1);
  }

  .fade-enter-active {
    transition: opacity .5s;
    transition-delay: .5s;
  }
  .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter,
  .fade-leave-to {
    opacity: 0;
  }

  .login-error-box {
    margin-left: 2rem;
    text-align: start;
    width: 30rem;
    position: absolute;
    top: 170px
  }

  .kakao-icon {
    height: 2.5rem;
  }

  .kakao-icon:hover {
    content: url('@/assets/kakao-icon-hover.png');
  }
</style>
