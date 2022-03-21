import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import RegisterComponent from '@/components/RegisterComponent'
import QueryComponent from '@/components/QueryComponent'

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
