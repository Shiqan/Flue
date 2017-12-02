import Vue from 'vue'
import Router from 'vue-router'
import PlayerPage from '@/pages/Player'
import MatchPage from '@/pages/Match'
import Meta from 'vue-meta'

Vue.use(Meta)
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: PlayerPage
    },
    {
      path: '/:package',
      component: PlayerPage
    },
    {
      path: '/test',
      name: 'Match history',
      component: MatchPage
    },
    {
      path: '/test/:package',
      component: MatchPage
    }
  ]
})
