import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { CssViews } from '@/constants'


const cssRoutes: RouteRecordRaw[] = []

CssViews.forEach(item => {
  cssRoutes.push({
    path: item.path,
    name: item.name,
    component: () => import(`@/views/css/${item.path}.vue`)
  })
})



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: () => import('@/layout/index.vue'),
      redirect: '/',
      children: [
        {
          path: '/',
          name: 'home',
          component: HomeView
        },
        {
          path: '/about',
          name: 'about',
          // route level code-splitting
          // this generates a separate chunk (About.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('../views/AboutView.vue')
        },
        {
          path: '/light',
          name: 'light',
          // route level code-splitting
          // this generates a separate chunk (About.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('@/views/light/LightView.vue')
        },
        {
          path: '/css',
          name: 'css',
          // route level code-splitting
          // this generates a separate chunk (About.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('@/views/css/index.vue'),
          children: cssRoutes
        }
      ]
    },
  ]
})

export default router
