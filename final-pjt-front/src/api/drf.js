const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    myProfile: () => HOST + ACCOUNTS + 'profile/',
    imageUpdate: imgNum => HOST + ACCOUNTS + 'profile_image/' + `${imgNum}/`,
    smsauth: phoneNum => HOST + ACCOUNTS + 'sms_auth/' + `${phoneNum}/`,
    smsdoauth: (phoneNum, authNum) => HOST + ACCOUNTS + 'sms_auth/' + `${phoneNum}/` + `${authNum}/`,
    changePassword: () => HOST + ACCOUNTS + 'password/change/',
    newPassword: () => HOST + ACCOUNTS + 'sms_auth/' + 'password/update/',
  },
  movies: {
    movie: TMDBMovieId => HOST + MOVIES + `${TMDBMovieId}/`,
    likeMovie: TMDBMovieId => HOST + MOVIES + `${TMDBMovieId}/` + 'like/',
    reviews: TMDBMovieId => HOST + MOVIES + `${TMDBMovieId}/` + 'reviews/',
    review_ud: (TMDBMovieId, reviewPk) => HOST + MOVIES + `${TMDBMovieId}/` + 'reviews/' + `${reviewPk}/`,
    likeGenre: TMDBGenreId => HOST + MOVIES + `${TMDBGenreId}/` + 'genre/',
    recommendByGenre: TMDBGenreId => HOST + MOVIES + `${TMDBGenreId}/` + 'recommendation/',
    recommendByLikeGenres:  () => HOST + MOVIES + 'genres/recommendation/',
    recommendByReviews: () => HOST + MOVIES + 'reviews/recommendation/',
    recommendByTMDB: () => HOST + MOVIES + 'tmdb/recommendation/',
    upComingMovie: () => HOST + MOVIES + 'tmdb/upcomming/',
    nowPlayingMovie: () => HOST + MOVIES + 'tmdb/nowplaying/',
  },
}
