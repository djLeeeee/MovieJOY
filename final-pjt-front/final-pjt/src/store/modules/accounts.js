import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {

  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    profile: {},
    loginAuthError: null,
    signupAuthError: null,
  },
  
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    loginAuthError: state => state.loginAuthError,
    signupAuthError: state => state.signupAuthError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_LOGIN_AUTH_ERROR: (state, error) => state.loginAuthError = error,
    SET_SIGNUP_AUTH_ERROR: (state, error) => state.signupAuthError = error,
    CLEAR_ERROR_LIST: (state) => { 
      state.loginAuthError = null  
      state.signupAuthError = null
    }
  },

  actions: {
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'mainrecommend' })
        })
        .catch(err => {
          commit('SET_LOGIN_AUTH_ERROR', err.response.data)
        })
    },

    signup({ getters, commit, dispatch }, {credentials, genres}) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          genres.map(genreId => {
            axios({
              url: drf.movies.likeGenre(genreId),
              method: 'post',
              headers: getters.authHeader
            })
          })
          router.push({ name: 'mainrecommend' })
        })
        .catch(err => {
          commit('SET_SIGNUP_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch }) {
      console.log('카카오개샛키')
      // window.Kakao.init('e5ff1659f2da5db0ab6fc8f99cd0733d')
      // window.Kakao.isInitialized()
      window.Kakao.Auth.logout()
      if (!window.Kakao.Auth.getAccessToken()) {
        axios({
          url: drf.accounts.logout(),
          method: 'post',
          headers: getters.authHeader,
        })
          .then(() => {
            dispatch('removeToken')
            router.push({ name: 'home' })
          })
          .error(err => {
            console.error(err.response)
          })
      }
      router.push({ name: 'home' })

    },

    clearErrorList ({ commit }) {
      commit('CLEAR_ERROR_LIST')
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_CURRENT_USER', res.data))
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'home' })
            }
          })
      }
    },

    fetchProfile({ commit, getters }, { username }) {
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
    },
  },
}
