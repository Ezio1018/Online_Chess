
import Vue from 'vue'
import Router from 'vue-router'
import home from '../components/home.vue'
import game from '@/components/game'
import login from '@/components/login'
import chessboard from '@/components/chessboard'
import firsthop from '@/components/firsthop'
import lobby from '@/components/lobby'




Vue.use(Router)
export default new Router({
  routes: [
    {path: '/', redirect: '/login'},
    {path: '/login', component: login},
    {
      path: '/home',
      component: home,
      redirect: '/firsthop',
      children: [
        {path: '/firsthop', component: firsthop},
        {path: '/chessboard', component: chessboard},
        {path: '/game', component: game},
        {path: '/lobby', component: lobby},
      ]
    }
  ]
}
)
