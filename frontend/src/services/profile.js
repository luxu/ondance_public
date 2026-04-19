import { api } from 'boot/axios'

export const profileService = {
  get() {
    return api.get('/profile/')
  },

  update(data) {
    const isFormData = data instanceof FormData
    return api.patch('/profile/', data, {
      headers: isFormData ? { 'Content-Type': undefined } : {},
    })
  },

  adminList({ role = null, search = '' } = {}) {
    const params = {}
    if (role) params.role = role
    if (search) params.search = search
    return api.get('/admin/users/', { params })
  },
}
