import { computed, ref } from 'vue'
import { authService } from 'src/services/auth'

const accessToken = ref(localStorage.getItem('access_token') || '')
const refreshToken = ref(localStorage.getItem('refresh_token') || '')

function parseJwt(token) {
  if (!token) return null
  const payload = token.split('.')[1]
  if (!payload) return null

  try {
    const decoded = atob(payload.replace(/-/g, '+').replace(/_/g, '/'))
    return JSON.parse(decodeURIComponent(
      decoded
        .split('')
        .map((c) => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    ))
  } catch {
    return null
  }
}

const user = computed(() => parseJwt(accessToken.value))
const isAuthenticated = computed(() => !!accessToken.value)

function saveTokens(tokens = {}) {
  const access = tokens.access ?? tokens.access_token ?? ''
  const refresh = tokens.refresh ?? tokens.refresh_token ?? ''

  if (access) {
    accessToken.value = access
    localStorage.setItem('access_token', access)
  }

  if (refresh) {
    refreshToken.value = refresh
    localStorage.setItem('refresh_token', refresh)
  }
}

function clearTokens() {
  accessToken.value = ''
  refreshToken.value = ''
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
}

async function login(credentials) {
  const response = await authService.login(credentials)
  saveTokens(response.data)
  return response
}

async function logout() {
  authService.logout()
  clearTokens()
}

async function refresh() {
  const refreshTokenValue = refreshToken.value || localStorage.getItem('refresh_token')
  if (!refreshTokenValue) {
    clearTokens()
    return null
  }

  const response = await authService.refresh(refreshTokenValue)
  saveTokens(response.data)
  return response
}

export function useAuth() {
  return {
    isAuthenticated,
    user,
    accessToken,
    refreshToken,
    login,
    logout,
    refresh,
    clearTokens,
    saveTokens
  }
}
