import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'
// import { useAuthStore } from 'stores/auth'

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior: () => ({ left: 0, top: 0 })
})

// router.beforeEach(async (to) => {
//   const auth = useAuthStore()
//   if (to.meta.guest) return auth.isAuthenticated ? auth.homeRoute : true
//   if (to.name === '404') return true
//   if (!auth.isAuthenticated) return '/login'
//   if (!auth.user) await auth.fetchMe()
//   if (to.meta.role && auth.user?.role !== to.meta.role) return auth.homeRoute
//   return true
// })

export default router
