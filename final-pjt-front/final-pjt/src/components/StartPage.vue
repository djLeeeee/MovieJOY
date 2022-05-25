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
              <div v-if="!isLoginOpen" class="not-login-Box">
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
        isLoginOpen: false,
        isSignupOpen: false,
        credentials: {
          username: '',
          password: '',
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

      onLoginOpen: function () {
        this.isLoginOpen = !this.isLoginOpen
        this.credentials.username = ''
        this.credentials.password = ''
      },

      onSignupOpen: function () {
        this.isSignupOpen = !this.isSignupOpen
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
            const kakao_account = res.kakao_account;
            const nickname = kakao_account.profile.nickname
            const username = nickname + "FromKAKAO"
            const password = "kakaosocialuser1"
            const credentials = {
              username,
              password,
              password1: password,
              password2: password,
            }
            console.log(drf.accounts.profile(username))
            axios({
              url: drf.accounts.profile(username),
              method: 'get'
            })
            .then(res => {
              console.log("success")
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
    background-image: url('@/assets/main_dark.jpg');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    width: 100%;
    object-fit: fill;
    height: 55rem;
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
    position: absolute;
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
    background-color: rgba(0, 0, 0, 0.459);
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

  .login-box {
    position: absolute;
  }

  .login-box .user-box {
    position: relative;
    margin-left: 2rem;
  }

  .login-box .user-box input {
    width: 100%;
    padding: 10px 0;
    font-size: 1.5rem;
    color: #fff;
    margin-bottom: 30px;
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

  .login-box .user-box input:focus ~ label,
  .login-box .user-box input:valid ~ label {
    top: -20px;
    left: 0;
    color: #00d8e4;
    font-size: 1rem;
  }

  .login-buttons {
    display: flex;
    justify-content: flex-start;
    margin-left: 1rem;
    margin-top: 2rem;
    font-size: 1.5rem;
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
