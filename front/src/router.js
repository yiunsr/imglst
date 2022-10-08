import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from './views/MainPage.vue'
import FaceLandmark from './views/FaceLandmark.vue'
import MorphingPage from './views/MorphingPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainPage
  },
  {
    path: '/facelandmark',
    name: 'facelandmark',
    component: FaceLandmark
  },
  {
    path: '/morphing',
    name: 'morphing',
    component: MorphingPage
  },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router