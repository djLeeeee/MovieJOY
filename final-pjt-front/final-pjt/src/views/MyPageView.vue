<template>
	<div id="mypage-flex">
		<div id="mypage-box">
			<div id="mypage-nav">
				<button @click="nowOpen" id="my-profile" class="my-profile page-open">My Profile</button>
				<button @click="nowOpen" id="like-movies">Like Movies</button>
				<button @click="onSettingsOpen">Settings</button>
			</div>
			<div v-if="nowOpenPage === 'my-profile'" id="profile-box">
				<div class="user-info-box">

					<div>
						<form method="post" enctype="multipart/form-data">
						<input ref="image" @change="uploadImg()" type="file" id="chooseFile" name="chooseFile" accept="image/*">
						</form>
						<img :src="imageSrc" alt="">
					</div>
					<div class="profile-info">
						<p>User Nickname</p>
						<p>Favorite Genres</p>
					</div>
				</div>
				<div class="user-review-box">
					<h3>My Reviews</h3>
					<div class="reviews-box">
						<p>웅냥냥냥</p>	
						<p>웅냥냥냥</p>	
						<p>웅냥냥냥</p>	
						<p>웅냥냥냥</p>	
					</div>	
				</div>
			</div>
			<div v-if="nowOpenPage === 'like-movies'">
				무비지롱롱롱롱
			</div>
		</div>
		<transition name="fade">
			<div v-if="isSettingsOpen" id="settings-box">
				<h2>Settings</h2>
				<div class="user-box">
					<input type="text" name="">
					<label>NickName</label>
				</div>
				<div id="genre-box">
					<h6 class="choose-text">Choose your favorite genres</h6>
					<div class="genre-buttons">
						<button class="raise" data-id="878">SF</button>
						<button class="raise" data-id="10770">TV영화</button>
						<button class="raise" data-id="10751">가족</button>
						<button class="raise" data-id="27">공포</button>
						<button class="raise" data-id="99">다큐멘터리</button>
						<button class="raise" data-id="18">드라마</button>
						<button class="raise" data-id="10749">로맨스</button>
						<button class="raise" data-id="12">모험</button>
						<button class="raise" data-id="9648">미스터리</button>
						<button class="raise" data-id="80">범죄</button>
						<button class="raise" data-id="37">서부</button>
						<button class="raise" data-id="53">스릴러</button>
						<button class="raise" data-id="16">애니메이션</button>
						<button class="raise" data-id="28">액션</button>
						<button class="raise" data-id="36">역사</button>
						<button class="raise" data-id="10402">음악</button>
						<button class="raise" data-id="10752">전쟁</button>
						<button class="raise" data-id="35">코미디</button>
						<button class="raise" data-id="14">판타지</button>
					</div>
					<div class="settings-buttons">
						<button class="btn authenticate-btn">Submit</button>
						<button @click="onSettingsOpen" class="btn authenticate-btn">Close</button>
					</div>
				</div>
			</div>
		</transition>	
	</div>	
</template>

<script>
  export default {
    name: 'MyPageView',
    components: { 

    },
		data: function () {
			return {
				nowOpenPage: 'my-profile',
				isSettingsOpen: false,
				imageSrc: '',
			}
		},
		created () {
			this.imageSrc = './assets/base_profile_img.jpeg'
		},
		methods: {
			nowOpen: function (event) {
				const onClickPage = event.target.id
				console.log(onClickPage)
				this.nowOpenPage = onClickPage
			},
			onSettingsOpen: function () {
				this.isSettingsOpen = !this.isSettingsOpen
			},
			uploadImg() {
				var image = this.$refs['image'].files
				const url = URL.createObjectURL(image)
				this.imageSrc = url
				console.log(this.imageSrc)
			}
		}
  }
</script>


<style>

#mypage-flex {
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
}

#mypage-box {
	margin-top: 5vh;
	position: absolute;
	width: 50rem;
	height: 40rem;
	background: rgba(0, 0, 0, 0.753);
	box-sizing: border-box;
	box-shadow: 0 15px 25px rgba(0,0,0,.6);
	transition: .8s;
	color: white;
}

#mypage-nav {
	display: flex;
	position: relative;
	bottom: 30px;
}

#mypage-nav button {
	border: none;
	width: 150px;
	height: 40px;
	background: rgba(0, 0, 0, 0.753);
	color: white;
}

#mypage-nav button:hover,
#mypage-nav button:focus {
	color: #00d9e4;
}

#settings-box {
	position: relative;
	top: 6rem;
	width: 6rem;
	width: 450px;
	height: 620px;
	padding: 40px;
	background: rgba(197, 197, 197, 0.911);
	box-sizing: border-box;
	box-shadow: 0 15px 25px rgba(0,0,0,.6);
	overflow: auto;
}

#profile-box {
	padding: 1rem;
	height: 100%;
}

.user-info-box {
	height: 50%;
	width: 100%;
	display: flex;
}

.user-info-box img {
	width: 300px;
	height: 300px;
	border-radius: 300px;
	margin-left: 1rem;
	transition: .8s;
	box-shadow: 4px 4px 4px #00d9e4af,
		4px 1px 1px #161491c2,
    7px 7px 3px #80179bcc;
}

.profile-info {
	margin-left: 2rem;
	text-align: start;
	font-size: 1.5rem;
	margin-top: 2rem;
}

.user-review-box {
	height: 230px;
	width: 100%;
	margin-top: 1.5rem;
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	transition: .8s;
}

.reviews-box {
	background-color: #00d9e44b;
	height: 100%;
	width: 100%;
	text-align: start;
	border-radius: 10px;
	padding: 0.5rem;
	overflow: auto;
}

#settings-box h2 {
	margin: 0 0 30px;
	padding: 0;
	color: rgb(51, 51, 51);
	text-align: center;
}

#settings-box .user-box {
	position: relative;
	margin-top: 0.5rem;
}

#settings-box .user-box input {
	width: 100%;
	padding: 10px 0;
	font-size: 1.2rem;
	color: rgb(51, 51, 51);
	margin-bottom: 30px;
	border: none;
	border-bottom: 1px solid rgb(51, 51, 51);
	outline: none;
	background: transparent;
}

#settings-box .user-box label {
	position: absolute;
	padding: 10px 0;
	top: -20px;
	left: 0;
	color: #00666bec;
	font-size: 1rem;
}

#settings-box .choose-text {
  color: rgb(51, 51, 51);
}

#settings-box .genre-buttons .raise:hover,
#settings-box .genre-buttons .raise-focus {
  font-size: 0.9rem;
  box-shadow: 0 0.5em 0.5em -0.4em #00666bec;
  border: 2px solid #00666bec;
  transform: translateY(-0.25em);
  background-color: #3d3d3d38;
  font-weight: bold;
  color: #00666bec;
  transition: all .5s;
}

.settings-buttons .authenticate-btn {
  margin-top: 0.5rem;
	color: rgb(51, 51, 51);
}

.settings-buttons .authenticate-btn:hover {
	color: #00666bec;
}

#settings-box .genre-buttons button {
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


@media ( max-width: 830px ) {
	#mypage-box {
		margin-top: 15vh;
		width: 500px;
		height: 500px;
	}

	.user-info-box img {
		width: 200px;
		height: 200px;
	}

	.user-review-box {
		height: 170px;
	}

	.profile-info {
		margin-left: 2rem;
		text-align: start;
		font-size: 1rem;
		margin-top: 2rem;
	}
}
</style>
