<template>
<div>
<h1> Query metadata database </h1>

  <select id="queryType" name="queryType" form="queryType" v-model="queryType">
  <option value="Files"> Number of files </option>
  <option value="Usage"> Data usage </option>
  <option value="Projects"> List of active projects </option>
  </select>
<br/>
<br/>
  <textarea name="textArea" id="textArea" v-model="textArea"> SPARQL query here... </textarea>
  <br/>
  <br/>
  <!-- TODO add a response element here -->

<button @click="query"> Query now </button>

<br/>
<br/>
<div class="response" v-html="message"/>

</div>
</template>

<script>
import QueryService from '@/services/QueryService'
export default {
  data () {
    return {
      message: null,
      queryType: 'Files',
      textArea: 'SPARQL query goes here...'
    }
  },
  methods: {
    async query () {
      const response = await QueryService.query({
        queryType: this.queryType // TODO: pack message into this as query string from SPARQL query
      })
      console.log('query in component:')
      console.log(this.queryType)
      console.log(response.data)
      console.log(this.textArea)
      // TODO: Depending on queryType / JSON data being sent, parse data for appropriate plotting etc.
      /// can use created() and mounted() to create figures as bar charts or as a graph...
      /// Data visualization potentially will take the most work here...
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
