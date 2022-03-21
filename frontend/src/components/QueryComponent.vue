<template>
<div>
<h1> Query metadata database </h1>

  <select id="queryType" name="queryType" form="queryType" v-model="queryType">
  <option value="Files"> Number of files </option>
  <option value="Usage"> Data usage </option>
  <option value="Projects"> List of active projects </option>
  </select>

<button @click="query"> Query now </button>

<div class="response" v-html="message"/>

</div>
</template>

<script>
import QueryService from '@/services/QueryService'
export default {
  data () {
    return {
      message: null,
      queryType: 'Files'
    }
  },
  methods: {
    async query () {
      const response = await QueryService.query({
        queryType: this.queryType // TODO: pack message into this as query string...
      })
      console.log('query in component:')
      console.log(this.queryType)
      console.log(response.data)
      this.message = response.data.mydata
    }
  }
}
</script>

<style scoped>
.response {
  color:  green;
}
</style>
