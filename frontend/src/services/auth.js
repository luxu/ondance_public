import { api } from 'boot/axios'

export const authService = {
  login(credentials) {
    return api.post('/token/', credentials)
  },

  refresh(refreshToken) {
    return api.post('/token/refresh/', { refresh: refreshToken })
  },

  logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  }
}
