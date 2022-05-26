<template>
  <div id="search-box">
    <div class="search-flex">
			<div class="search">
				<p class="search-main-text">Search the movie title</p>
				<p class="search-text">Click on search icon, then type your keyword.</p>
				<div>
					<input @focus="onSearch" @blur="onSearch" @keypress.enter="submitKeyword" class="input-bar" v-model="inputKeyword" type="text" placeholder="Search . . ." required>
        </div>  
        <button @mouseenter="onVoice" v-if="isSearch" class="btn btn-link on-voice-btn">
          <i class="fa-solid fa-microphone"></i>
        </button>
			</div>
		</div>
    <div>
      <MovieList :movies="movies" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from "@/components/MovieList"
import router from '@/router'
import { mapGetters } from 'vuex'

export default {
  name: 'SearchView',
  components: {
    MovieList,
  },
  data: function () {
    return {
      inputKeyword: '',
      isSearch: false,
      movies: []
    }
  },
  computed: {
      ...mapGetters(['isLoggedIn'])
  },
  methods: {
    onSearch: function () {
      if (!this.inputKeyword) {
        this.isSearch = !this.isSearch
      }
    },
    onFocus: function () {
      const searchInput = document.querySelector('.input-bar')
      searchInput.focus()
    },
    onVoice: function () {
      window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
      const recognition = new window.SpeechRecognition();
      recognition.interimResults = false;
      recognition.lang = 'ko-KR'; 

      let p = ''
    
      recognition.addEventListener('result', e => {
      const transcript = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('');

        p = transcript;
        this.inputKeyword += p

        if (e.results[0].isFinal) {
          p = ' '
          this.inputKeyword += p
        }
      });    

      recognition.start();
    },
    submitKeyword: function (keyword_input) {
      keyword_input = this.inputKeyword

      const params = {
        'api_key': '52962731aacacff3f5f9da655947bff6',
        'query': keyword_input,
        'region': 'KR',
        'language': 'ko',
      }

      axios.get('https://api.themoviedb.org/3/search/movie',  {params,})
      .then(res => {
        this.movies = res.data.results
      })

      const searchBox = document.querySelector('#search-box')
      searchBox.setAttribute('style', 'margin: 0vh;')
    }
  },
  mounted () {
    if (! this.isLoggedIn) {
      router.push({ name: 'home' })
    }
  },
}
</script>

<style>
#search-box {
  margin-top: 30vh;
  transition: 0.8s;
}

.search-flex {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.search {
  margin: 20px;
}

.search > h3 {
  font-weight: normal;
}

.search > h1,
.search > h3 {
  color: white;
  margin-bottom: 15px;
  text-shadow: 0 1px #505050;
}

.search > div {
  display: inline-block;
  position: relative;
  filter: drop-shadow(0 1px #0091c2);
}

.search > div:after {
  content: "";
  background: white;
  width: 4px;
  height: 10px;
  position: absolute;
  top: 22px;
	right: 0px;
  transform: rotate(135deg);
}

.search > div > input {
  color: white;
  font-size: 16px;
  background: transparent;
  width: 30px;
  height: 30px;
  padding: 10px;
  border: solid 2px white;
  outline: none;
  border-radius: 35px;
  transition: width 0.5s;
}

.search > div > input::placeholder {
  color: #efefef;
  opacity: 0;
  transition: opacity 150ms ease-out;
}

.search > div > input:focus::placeholder {
  opacity: 1;
}

.search > div > input:focus,
.search > div > input:not(:placeholder-shown) {
  width: 350px;
}

.search-main-text {
	color: white;
	font-size: 2rem;
}

.search-text {
	color: rgba(255, 255, 255, 0.753);
	margin-bottom: 2rem;
}

.on-voice-btn {
  color: white;
  position: relative;
  top: 3px;
  transition: .3s;
}

.on-voice-btn:hover,
.on-voice-btn:focus {
  color: #01a8b1;
  transform: scale(1.2);
}
</style>