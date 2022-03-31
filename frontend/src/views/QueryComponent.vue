
<template>
<div>
<h1> Query metadata database </h1>
  <select id="queryType" name="queryType" form="queryType" v-model="queryType">
  <option value="Files"> Number of files </option>
  <option value="Usage"> Data usage </option>
  <option value="Projects"> List of active projects </option>
  <option value="MyGDP"> D3 View example </option>
  <option value="Graph"> D3 Graph example </option>
  </select>
<br/>
<br/>

<button @click="query"> Add plot </button>
<button @click="unquery"> Remove plot </button>

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
    appropritate vue component with d3js potentially-->

<button @click="queryFreeText"> Query now </button>

<br/>
<br/>
<br/>
<br/>
<template v-for="(child, index) in cards">
 <!--<template v_if="cards"> -->
 <!-- abc {{child['card-type']}}-->
 <!-- {{index}}-->
  <component :is="child['card-type']" :key="index" :title="child.card.title" :real_data="child.card.real_data" :date='child.card.date'/>
 <!--<component v-bind:is="MyComponent"> -->
 <!--</component>-->
 <!--<d-3-view> </d-3-view>-->
</template>

<br/>
<br/>
<h3> Response from backend </h3>
<div class="response" v-html="message"/>
</div>
</template>

<script>
import QueryService from '@/services/QueryService'
import D3View from '@/components/D3View.vue'
import GraphView from '@/components/GraphView.vue'
// import D3ViewVariant from './D3ViewVariant.vue'

import Vue from 'vue'
Vue.component('card1', {
  template: '<div> Card: <span style="background-color:blue"> {{title}} </span> </div>',
  props: ['title']
})

Vue.component('card2', {
  template: '<div> Card2: <span style="background-color:red"> {{title}} </span> </div>',
  props: ['title']
})

Vue.component('card3', {
  template: '<div> Card3: <span style="background-color:yellow"> {{title}} </span> </div>',
  props: ['title']
})

export default {
  components: {
    D3View, GraphView
    // D3ViewVariant
  },
  data () {
    return {
      message: null,
      queryType: 'Files',
      textArea: 'SPARQL query goes here...',
      cards: [
        // {'card1': {'title': 'Card 1'}, 'card-type': 'card1'}
      ],
      real_data: [] // JSON data from QueryService response
    }
  },
  methods: {
    async query () {
      const response = await QueryService.query({
        // TODO: pack message (from SPARQL freetext query textarea above)
        // into this as query string (queryString) from SPARQL query in
        // addition to the query type if queryType is textArea
        queryType: this.queryType
      })
      console.log('query in component:')
      console.log(this.queryType)
      var repodata = response.data
      console.log('repodata')
      console.log(repodata)
      console.log(this.real_data)
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
      console.log('push card!')
      // this.cards.push({'card1': {'title': 'Card 1'}, 'card-type': 'card1'})
      // this.cards.push({'card1': {'title': 'Card 1'}, 'card-type': 'card1'})
      var today = new Date()
      var dd = String(today.getDate()).padStart(2, '0')
      var mm = String(today.getMonth() + 1).padStart(2, '0')
      var yyyy = today.getFullYear()
      today = mm + '/' + dd + '/' + yyyy
      switch (this.queryType) {
        case 'Files':
          console.log('I am there!!!')
          this.cards.push({'card': {'title': 'I am a new card!'}, 'card-type': 'card2'})
          break
        case 'MyGDP':
          console.log('stringify')
          console.log(response.data)
          /// TODO: don't use eval, might be harmful depending on where data comes from, only for delevoping right now
          // eslint-disable-next-line
          this.cards.push({'card': {'real_data': eval(response.data), 'title': 'Usage statistics', 'date': today}, 'card-type': 'D3View'})
          console.log('I am here!!!')
          console.log(this.real_data)
          break
        case 'Graph':
          console.log('real data?')
          console.log(response.data.nodes)
          console.log('real data?')
          /// Dynamically insert components...
          this.cards.push({'card': {'real_data': response.data, 'title': 'Project dependencies', 'date': today}, 'card-type': 'GraphView'})
          break
        default:
          this.cards.push({'card': {'title': `I am a new card! (from query type ${this.queryType})`}, 'card-type': 'card1'})
      }
      console.log(this.cards)
    },
    unquery () {
      this.cards.pop()
    },
    queryFreeText () {
      // TODO: implement this (SPARQL CONSTRUCT queries)
      // TODO: Need visual gui (with vuetify maybe?) to construct queries
      // (for this need ontology / controlled vocabulary to create the components
      // in drop down menus!)
    }
  }
}
</script>

<style scoped>
.response {
  color:  green;
}
</style>
