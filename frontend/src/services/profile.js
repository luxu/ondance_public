import { api } from 'boot/axios'

export const profileService = {
  get() {
    return api.get('/profile/')
  },

  update(data) {
    return api.patch('/profile/', data)
  },
}
