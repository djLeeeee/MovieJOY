const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'MOVIES/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    movie: TMDBMovieId => HOST + MOVIES + `${TMDBMovieId}/`,
    likeArticle: TMDBMovieId => HOST + MOVIES + `${TMDBMovieId}/` + 'like/',
    reviews: TMDBMovieId => HOST + MOVIES + `${TMDBMovieId}/` + 'reviews/',
    review_ud: (TMDBMovieId, reviewPk) => HOST + MOVIES + `${TMDBMovieId}/` + 'reviews/' + `${reviewPk}/`,
    likeGenre: TMDBGenreId => HOST + MOVIES + `${TMDBGenreId}/` + 'genre/',
  },
}
