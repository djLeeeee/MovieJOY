<template>
  <div id="search-box">
    <div class="flexbox">
			<div class="search">
				<p class="search-main-text">Search the movie title</p>
				<p class="search-text">Click on search icon, then type your keyword.</p>
				<div>
					<input type="text" placeholder="Search . . ." required>
				</div>
			</div>
		</div>
  </div>
</template>

<script>
export default {
  name: 'SearchView',
}
</script>

<style>
#search-box {
	padding: 2rem;
}

.flexbox {
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