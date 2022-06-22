import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Home from '@/components/Home'
import UserInfo from '@/components/UserInfo'
import Relation from '@/components/Relation'
import Statuses from '@/components/Statuses'
import Comments from '@/components/Comments'
import NotFound from '@/components/NotFound'
import Echarts from '@/components/Echarts'
import Start from '@/components/Start'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/home',  // 路径
      name: 'Home',
      component: Home, // component是指组件  import引用login.vue地址
      children: [
        {
          path: 'start',
          component: Start         
        },
        {
          path: 'user',
          component: UserInfo
        },
        {
          path: 'relation',
          component: Relation
        },
        {
          path: 'statuses',
          component: Statuses
        },
        {
          path: 'comments',
          component: Comments
        },
        {
          path: 'echarts',
          component: Echarts
        }
      ]
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})
