import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior: () => ({ left: 0, top: 0 })
})

router.beforeEach((to) => {
  const token = localStorage.getItem('access_token')

  if (!to.meta.guest && !token) {
    return '/login'
  }

  if (token && to.meta.guest && (to.name === 'login' || to.name === 'register')) {
    return '/courses/initial'
  }

  return true
})

export default router
