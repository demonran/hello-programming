import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'


const cssRoutes = [
  {
    path: 'translucent-borders',
    name: 'translucent-borders',
    component: () => import('@/views/css/LearnCss.vue')
  },
  {
    path: 'multiple-borders',
    name: 'multiple-borders',
    component: () => import('@/views/css/MultipleBorder.vue')
  }
]


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
})

export default router
