import { api } from 'boot/axios'

export const cityService = {
  list(params) {
    return api.get('/cities/', { params })
  },

  create(data) {
    return api.post('/cities/', data)
  }
}
