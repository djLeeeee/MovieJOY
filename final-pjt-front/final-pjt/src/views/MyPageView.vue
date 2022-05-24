<template>
	<div id="mypage-flex">
		<div id="mypage-box">
			<div id="mypage-nav">
				<button @click="nowOpen" id="my-profile" class="my-profile page-open">My Profile</button>
				<button @click="nowOpen" id="like-movies">Like Movies</button>
			</div>
			<div v-if="nowOpenPage === 'my-profile'" class="profile-box">
				<div class="user-info-box">
					<img src="@/assets/base_profile_img.jpeg" alt="">
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
			}
		},
		methods: {
			nowOpen: function (event) {
				const onClickPage = event.target.id
				console.log(onClickPage)
				this.nowOpenPage = onClickPage
			} 
		}
  }
</script>


<style>
#mypage-flex {
	width: 100vw;
	height: 100vh;
	display: flex;
	justify-content: center;
}

#mypage-box {
	margin-top: 5vh;
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


.profile-box {
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
	height: 250px;
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
