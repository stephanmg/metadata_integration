import Vue from 'vue'
import Router from 'vue-router'
import HomeComponent from '@/views/HomeComponent'
import RegisterComponent from '@/views/RegisterComponent'
import QueryComponent from '@/views/QueryComponent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeComponent
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterComponent
    },
    {
      path: '/query',
      name: 'Query',
      component: QueryComponent
    }
  ],
  mode: 'history'
})
