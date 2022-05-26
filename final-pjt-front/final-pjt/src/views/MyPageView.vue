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
					<img :src="require(`@/assets/profile_img/img_${ user.profile_image }.png`)" alt="" />
					<button @click="onEditProfileImage" class="btn btn-link modal-btn">
						<i class="fa-solid fa-camera"></i>
					</button>
					<div class="profile-info">
						<p class="nickname-text">{{ user.nickname || user.username }}</p>
						<p style="font-weight: bold; padding: 0px;">Favorite Genres</p>
            <GenresName :likeGenres="likeGenres" />
					</div>
				</div>
				<div class="user-review-box">
					<h3>My Reviews</h3>
					<div class="reviews-box">
						<UserReviewItem v-for="(review, idx) in user.reviews" :key="idx" :review="review" />
					</div>	
				</div>
			</div>
			<div v-if="nowOpenPage === 'like-movies'" id="user-like-dislike-box">
				<div class="like-box">
					<h3 class="like-dislike-label">Like Movies</h3>
					<div class="like-dislike-box">
						<div v-for="(movie, idx) in user.like_movies" :key="idx" >
              <LikeMovieName :movie="movie" />
						</div>
					</div>
				</div>
				<div class="dislike-box">
					<h3 class="like-dislike-label">No Interest Movies</h3>
					<div class="like-dislike-box">
						<div v-for="(movie, idx) in user.dislike_movies" :key="idx" >
              <LikeMovieName :movie="movie" />
						</div>
					</div>
				</div>
			</div>
		</div>
		<transition name="fade">
			<div v-if="isSettingsOpen" id="settings-box">
				<SettingsInput :userNickname="user.nickname" :userUsername="user.username" :likeGenres="likeGenres" @edit-profile-data="submitProfileData" @close-settings="onSettingsOpen" />
			</div>
		</transition>	
		<transition name="fade">
			<div v-if="isProfileImageOpen" id="edit-profile-box">
				<EditProfileImage :userProfileImage="userProfileImage" @close-edit-profile="onEditProfileImage" />
			</div>
		</transition>
	</div>	
</template>

<script>
  import axios from 'axios'
  import drf from '@/api/drf'
  import { mapGetters } from 'vuex'
  import SettingsInput from '@/components/SettingsInput.vue'
	import UserReviewItem from '@/components/UserReviewItem.vue'
  import LikeMovieName from '@/components/LikeMovieName.vue'
  import EditProfileImage from '@/components/EditProfileImage.vue'
  import GenresName from '@/components/GenresName.vue'

  export default {
    name: 'MyPageView',
    components: { 
      SettingsInput,
      UserReviewItem,
      LikeMovieName,
			EditProfileImage,
      GenresName,
    },
		data: function () {
			return {
				nowOpenPage: 'my-profile',
				isSettingsOpen: false,
				isProfileImageOpen: false,
				imageSrc: '',
        user: {profile_image: 1},
				userProfileImage: 0,
        likeGenres: [],
			}
		},
		created () {
      axios({
        url: drf.accounts.myProfile(),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => {
        this.user = res.data
        this.likeGenres = res.data.like_genres
        this.userProfileImage = this.user.profile_image
      })
		},
		methods: {
			nowOpen: function (event) {
				const onClickPage = event.target.id
				this.nowOpenPage = onClickPage
			},
			onSettingsOpen: function () {
        if (this.isSettingsOpen) {
          this.inputNickname = this.user.nickname
        }
				this.isSettingsOpen = !this.isSettingsOpen
			},
			onEditProfileImage: function () {
				this.isProfileImageOpen = !this.isProfileImageOpen
			},
      submitProfileData (data, nicknameData) {
        axios({
          url: drf.accounts.myProfile(),
          method: 'post',
          headers: this.authHeader,
          data: {
            'nickname': nicknameData
          }
        })
        .then(() => {
          this.user.nickname = this.inputNickname
          data.map(genreId => {
            axios({
              url: drf.movies.likeGenre(genreId),
              method: "post",
              headers: this.authHeader,
            })
          })
          this.refresh()
        })
      },
      refresh () {
        this.$router.go()
      }  
		},
    computed: {
      ...mapGetters(['authHeader']),
    },
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
	bottom: 40px;
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

#settings-box,
#edit-profile-box {
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

#user-like-dislike-box {
  text-align: start;
  padding: 1rem;
	height: 100%;
	display: flex;

}

.like-box,
.dislike-box {
	width: 50%;
	padding: 0.5rem;
}


.like-dislike-label {
  margin-bottom: 0.5rem;
	margin-left: 0.5rem;
}

.like-dislike-box {
	border: solid 7px #00d9e44b;
	height: 31rem;
	width: 100%;
	text-align: start;
	border-radius: 10px;
	padding: 0.5rem;
	overflow: auto;
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
	border: solid 7px #00d9e44b;
	border-radius: 10px;
	padding: 0.5rem;
}

.reviews-box {
	/* background-color: #00d9e44b; */
	/* border: solid 7px #00d9e44b; */
	height: 100%;
	width: 100%;
	text-align: start;
	border-radius: 10px;
	padding: 0.5rem;
	overflow: auto;
}

.user-like-dislike-box {
  padding: 1rem;
	padding-top: 0px;
	width: 100%;
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

.nickname-text {
	font-size: 2rem;
	font-weight: bold;
	/* text-transform: uppercase; */
	background: linear-gradient(to right, #30CFD0 0%, #330867 100%);
	text-shadow: 2px 2px rgba(240, 255, 255, 0.233);
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
}

.modal-dialog {
	margin-top: 20vh;
	color: rgb(51, 51, 51);
	border-radius: 0px;
}

.modal-header,
.modal-footer {
	height: 2.5rem;
	padding: 0px;
	padding: 0.5rem;
}

.modal-footer button {
	text-decoration: none;
	color: rgb(51, 51, 51);
	padding: 0px;
	margin: 0px;
	font-size: 1rem;
}

.modal-footer button:hover,
.modal-footer button:focus,
.modal-header button:hover,
.modal-header button:focus {
	transform: scale(1.1);
	color: #00949c;
	border: none;
}


.modal-btn {
	position: relative;
	font-size: 1.8rem;
	width: 60px;
	height: 60px;
	background-color: rgb(243, 243, 243);
	border-radius: 70px;
	transition: .8s;
	text-align: center;
	text-decoration: none;
}

.modal-btn:hover,
.modal-btn:focus {
	transform: scale(1.1);
	background-color: rgb(243, 243, 243)
}

.modal-btn i {
	margin-top: 8px;
	color: black;
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

	.modal-btn {
		position: relative;
		font-size: 1rem;
		width: 30px;
		height: 30px;
		border-radius: 30px;
		display: flex;
		justify-content: center;
	}

	.modal-btn i {
		margin-top: 0px;
	}

	.nickname-text {
		font-size: 1.5rem;
	}

	#user-like-dislike-box {
		flex-direction: column;
	}

	.like-box,
	.dislike-box {
		width: 100%;
	}

	.like-dislike-box {
		height: 160px;
	}
}
</style>
