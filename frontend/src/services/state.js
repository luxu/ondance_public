import { api } from 'boot/axios'

export const stateService = {
  list(search) {
    return api.get('/states/', { params: search ? { search } : {} })
  }
}
