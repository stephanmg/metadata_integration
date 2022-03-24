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
  <!-- TODO: use v-for element -->
  <!-- depening on textArea or queryType decide which component to insert in v-for loop -->
  <!-- should get a response from query service with data + expected plot type -->
  <!-- depening on plot type will insert a vue component as reponse to the query -->
  <!-- TODO: Need to decide which plots we want to offer in the frontend, then -->
  <!-- will need to provide backend functionality 1) query db 2) format data to json 
    and transmit data with plot type to frontend, which then in turn will insert the
    appropritate vue component with d3js potentially
  -->


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
      /// TODO: pass data to vue component via props (array of data or json)
      /// for this use v-for and store into this QueryComponent.vue the plotting component
      /// then iterate (over 1 element array) with v-for and insert the component
      /// Use a switch statement to determine which component to be added for showing the plot
      /// backend should produce correct json data and then send it to the frontend, which
      /// only has to actually plot the json data (each plottype has another plotting component vue)
    }
  }
}
</script>

<style scoped>
.response {
  color:  green;
}
</style>
