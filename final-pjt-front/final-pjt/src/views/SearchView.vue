<template>
  <div id="search-box">
    <div class="search-flex">
			<div class="search">
				<p class="search-main-text">Search the movie title</p>
				<p class="search-text">Click on search icon, then type your keyword.</p>
				<div>
					<input @keyup.enter="submitKeyword" v-model="inputKeyword" type="text" placeholder="Search . . ." required>
				</div>
			</div>
		</div>
    <div>
      <MovieList v-if="movies" :movies="movies" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from "@/components/MovieList"

export default {
  name: 'SearchView',
  components: {
    MovieList,
  },
  data: function () {
    return {
      inputKeyword: '',
      movies: []
    }
  },
  methods: {
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
        console.log(this.movies)
        if (!this.movies.length) {
          alert('검색 결과가 없습니다')
        }
      })

      const searchBox = document.querySelector('#search-box')
      searchBox.setAttribute('style', 'margin: 0vh;')
    }
  }
}
</script>

<style>
#search-box {
	padding: 2rem;
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
</style>