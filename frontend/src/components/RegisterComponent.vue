<template>
<div>
<h1> Register </h1>

<input type="email" name="email" v-model="email" placeholder="email"/>
<br/>

<input type="password" name="password" v-model="password" placeholder="password"/>
<br/>

<button> Register </button>
</div>
</template>

<script>
import AuthService from '@/services/AuthService'
export default {
  data () {
    return {
      email: '',
      password: ''
    }
  },
  watch: {
    email (value) {
      console.log('email has changed', value)
    }
  },
  methods: {
    async register () {
      const response = await AuthService.register({
        email: this.email,
        password: this.password
      })
      console.log(response)
    }
  }
}
</script>

<style scoped>
</style>
