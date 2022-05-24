<template>
  <div class="profile-genre-buttons">
    <button @click="onSelectGenre()" class="raise" data-id="878">SF</button>
    <button @click="onSelectGenre()" class="raise" data-id="10770">TV영화</button>
    <button @click="onSelectGenre()" class="raise" data-id="10751">가족</button>
    <button @click="onSelectGenre()" class="raise" data-id="27">공포</button>
    <button @click="onSelectGenre()" class="raise" data-id="99">다큐멘터리</button>
    <button @click="onSelectGenre()" class="raise" data-id="18">드라마</button>
    <button @click="onSelectGenre()" class="raise" data-id="10749">로맨스</button>
    <button @click="onSelectGenre()" class="raise" data-id="12">모험</button>
    <button @click="onSelectGenre()" class="raise" data-id="9648">미스터리</button>
    <button @click="onSelectGenre()" class="raise" data-id="80">범죄</button>
    <button @click="onSelectGenre()" class="raise" data-id="37">서부</button>
    <button @click="onSelectGenre()" class="raise" data-id="53">스릴러</button>
    <button @click="onSelectGenre()" class="raise" data-id="16">애니메이션</button>
    <button @click="onSelectGenre()" class="raise" data-id="28">액션</button>
    <button @click="onSelectGenre()" class="raise" data-id="36">역사</button>
    <button @click="onSelectGenre()" class="raise" data-id="10402">음악</button>
    <button @click="onSelectGenre()" class="raise" data-id="10752">전쟁</button>
    <button @click="onSelectGenre()" class="raise" data-id="35">코미디</button>
    <button @click="onSelectGenre()" class="raise" data-id="14">판타지</button>
  </div>
</template>

<script>
export default {
  name: 'GenreButton',
  props: {
    likeGenres: Array,
  },
  mounted () {
    this.likeGenres.map(genreId => {
      const genreBtn = document.querySelector(`button[data-id="${genreId}"]`)
      genreBtn.classList.add('raise-focus')
    })
  },
  methods: {
    onSelectGenre: function (event) {
      const genreBtn = event.target
      if (!genreBtn.classList.contains('raise-focus')) {
        genreBtn.classList.add('raise-focus')
      } else {
        genreBtn.classList.remove('raise-focus')
      }
    }
  }
}
</script>

<style>
/* .profile-genre-buttons button {
  width: 6rem;
  background: none;
  border: 2px solid;
  font: inherit;
  line-height: 1;
  margin: 0.5em;
  padding: 0.5em;
  color: rgb(51, 51, 51);
  font-size: 0.9rem;
  transition: all .5s;
}

.profile-genre-buttons .raise:hover,
.profile-genre-buttons .raise-focus {
  font-size: 0.9rem;
  box-shadow: 0 0.5em 0.5em -0.4em #01a8b1;
  border: 2px solid #01a8b1a1;
  transform: translateY(-0.25em);
  background-color: #01a8b138;
  font-weight: bold;
  color: #00d7e2ec;
  transition: all .5s;
} */
</style>