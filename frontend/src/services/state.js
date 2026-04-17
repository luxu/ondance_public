import { api } from 'boot/axios'

export const stateService = {
  list(params) {
    return api.get('/states/', { params: { page_size: 100, ...params } })
  }
}
