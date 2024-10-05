import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  // ? We are redirecting to different pages based on role.

  {
    path: '/',
    redirect: 'home',
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/views/Home.vue'),

    meta: {
      layout: 'content',
    },
  },
  {
    path: '/addons',
    name: 'Addons',
    component: () => import('@/views/Addons.vue'),

    meta: {
      layout: 'content',
    },
  },

  {
    path: '/error-404',
    name: 'error-404',
    component: () => import('@/views/Error404.vue'),
    meta: {
      layout: 'blank',
      resource: 'Public',
    },
  },

  {
    path: '*',
    redirect: 'error-404',
  },

]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

const routerModules = require.context('../../addons/apps', true, /frontend\/router\.js$/)

const allAddonRoutes = routerModules.keys().map(routeKey => {
  return routerModules(routeKey).default
})

// Flatten the array, since each module can export an array of routes
const flattenedRoutes = [].concat(...allAddonRoutes)

// Assuming you've already set up the Vue Router:
router.addRoutes(flattenedRoutes)

export default router
