import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/views/HelloWorld'
import RegisterComponent from '@/views/RegisterComponent'
import QueryComponent from '@/views/QueryComponent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
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
