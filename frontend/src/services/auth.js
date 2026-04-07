import { api } from 'boot/axios'

const ACCESS_TOKEN_KEY = 'access_token'
const REFRESH_TOKEN_KEY = 'refresh_token'

function saveTokens(data = {}) {
  const access = data.access ?? data.access_token ?? ''
  const refresh = data.refresh ?? data.refresh_token ?? ''

  if (access) {
    localStorage.setItem(ACCESS_TOKEN_KEY, access)
  }

  if (refresh) {
    localStorage.setItem(REFRESH_TOKEN_KEY, refresh)
  }

  return { access, refresh }
}

function clearTokens() {
  localStorage.removeItem(ACCESS_TOKEN_KEY)
  localStorage.removeItem(REFRESH_TOKEN_KEY)
}

export const authService = {
  login(credentials) {
    return api.post('/token/', credentials).then((response) => {
      saveTokens(response.data)
      return response
    })
  },

  register(userData) {
    return api.post('/register/', userData)
  },

  refresh(refreshToken) {
    return api.post('/token/refresh/', { refresh: refreshToken }).then((response) => {
      saveTokens(response.data)
      return response
    })
  },

  getAccessToken() {
    return localStorage.getItem(ACCESS_TOKEN_KEY)
  },

  getRefreshToken() {
    return localStorage.getItem(REFRESH_TOKEN_KEY)
  },

  logout() {
    clearTokens()
  }
}
