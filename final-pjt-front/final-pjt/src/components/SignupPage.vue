<template>
  <div @click="signupClose" id="all-box">
    <div id="signup-box">
      <h2 style="margin-top: 50px;">SignUp</h2>
       <div class="signup-error-box" v-if="signupAuthError">
        <div v-for="(errors, field) in signupAuthError" :key="field">
          <p v-for="(error, idx) in errors" :key="idx">
            {{ error }}
          </p>
        </div>
      </div>
      <div class="user-box">
        <input v-model="payload.credentials.username" type="text" name="" required />
        <label>Username</label>
      </div>
      <div class="user-box">
        <input v-model="payload.credentials.password1" type="password" name="" required />
        <label>Password</label>
      </div>
      <div class="user-box">
        <input v-model="payload.credentials.password2" type="password" name="" required />
        <label>Password Confirm</label>
      </div>
      <div class="user-box">
        <input type="text" name="" required />
        <label>Phone Number</label>
      </div>
      <div id="genre-box">
        <h6 class="choose-text">Choose your favorite genres</h6>
        <div class="genre-buttons">
          <button @click="onSelectGenre" class="raise" data-id="878">SF</button>
          <button @click="onSelectGenre" class="raise" data-id="10770">TV영화</button>
          <button @click="onSelectGenre" class="raise" data-id="10751">가족</button>
          <button @click="onSelectGenre" class="raise" data-id="27">공포</button>
          <button @click="onSelectGenre" class="raise" data-id="99">다큐멘터리</button>
          <button @click="onSelectGenre" class="raise" data-id="18">드라마</button>
          <button @click="onSelectGenre" class="raise" data-id="10749">로맨스</button>
          <button @click="onSelectGenre" class="raise" data-id="12">모험</button>
          <button @click="onSelectGenre" class="raise" data-id="9648">미스터리</button>
          <button @click="onSelectGenre" class="raise" data-id="80">범죄</button>
          <button @click="onSelectGenre" class="raise" data-id="37">서부</button>
          <button @click="onSelectGenre" class="raise" data-id="53">스릴러</button>
          <button @click="onSelectGenre" class="raise" data-id="16">애니메이션</button>
          <button @click="onSelectGenre" class="raise" data-id="28">액션</button>
          <button @click="onSelectGenre" class="raise" data-id="36">역사</button>
          <button @click="onSelectGenre" class="raise" data-id="10402">음악</button>
          <button @click="onSelectGenre" class="raise" data-id="10752">전쟁</button>
          <button @click="onSelectGenre" class="raise" data-id="35">코미디</button>
          <button @click="onSelectGenre" class="raise" data-id="14">판타지</button>
        </div>
      </div>
      <div class="signup-buttons">
        <button @click="signup(payload), moveToTop()" class="btn authenticate-btn">Submit</button>
        <button @click="onSignupClose()" class="btn authenticate-btn">Back</button>
      </div>
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'SignupPage',
    data: function () {
      return {
        payload: {
          genres: [],
          credentials: {
            username: '',
            password1: '',
            password2: '',
          },
      }}
    },
    computed: {
      ...mapGetters(['signupAuthError'])
    },
    methods: {
      ...mapActions(['signup']),
      onSignupClose: function () {
        this.$emit('signup-close')
      },
      signupClose: function (event) {
        if (event.target.id === 'all-box') {
          this.$emit('signup-close')
        }
      },
      moveToTop: function () {
        const signupDiv = document.querySelector('#signup-box')
        signupDiv.scrollTo({top: 0, behavior: 'smooth'})
      },
      onSelectGenre: function (event) {
        const genreId = event.target.dataset.id
        const genreBtn = event.target
        if (!genreBtn.classList.contains('raise-focus')) {
          genreBtn.classList.add('raise-focus')
          this.payload.genres.push(genreId)
        } else {
          genreBtn.classList.remove('raise-focus')
          const idx = this.payload.genres.indexOf(genreId)
          this.payload.genres.splice(idx, 1)
        }
      }
    }
  }
</script>

<style>
#all-box {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
}

#signup-box {
  position: relative;
  top: 10rem;
  width: 450px;
  height: 450px;
  padding: 50px;
  background: rgba(0, 0, 0, 0.753);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0,0,0,.6);
  overflow: auto;
}

#signup-box::-webkit-scrollbar {
  width: 10px;
  background: #00d9e400;
}

#signup-box::-webkit-scrollbar-thumb {
  background-color: #00d9e444;
  border-radius: 10px;
}



#signup-box h2 {
  margin: 0 0 30px;
  padding: 0;
  color: #fff;
  text-align: center;
}

#signup-box .user-box {
  position: relative;
  margin-top: 0.5rem;
}

#signup-box .user-box input {
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

#signup-box .user-box label {
  position: absolute;
  top:0;
  left: 0;
  padding: 10px 0;
  font-size: 1.2rem;
  color: #fff;
  pointer-events: none;
  transition: .5s;
}

#signup-box .user-box input:focus ~ label,
#signup-box .user-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: #01a8b1;
  font-size: 0.8rem;
}

.choose-text {
  color: white;
}

.genre-buttons .raise:hover,
.genre-buttons .raise-focus {
  font-size: 0.9rem;
  box-shadow: 0 0.5em 0.5em -0.4em #01a8b1;
  border: 2px solid #01a8b1a1;
  transform: translateY(-0.25em);
  background-color: #01a8b138;
  font-weight: bold;
  color: #00d7e2ec;
  transition: all .5s;
}

.signup-buttons {
  margin-top: 0.5rem;
}

.genre-buttons button {
  width: 6rem;
  background: none;
  border: 2px solid;
  font: inherit;
  line-height: 1;
  margin: 0.5em;
  padding: 0.5em;
  color: white;
  font-size: 0.9rem;
  transition: all .5s;
}

.signup-error-box {
  text-align: start;
  color: white;
  font-size: 0.8rem;
}

</style>