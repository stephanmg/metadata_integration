<template>
<div>
<h3> {{title}} </h3>
<h4> Compiled on {{date}} </h4>
<div id='gdpview'/>
</div>
</template>

<style scoped>
#gdpview {
  font-size: xx-small;
}
</style>

<style>
div.tooltip {
  position: absolute;
  text-align: center;
  width: 80px;
  height: 28px;
  padding: 2px;
  color: black;
  font: 12px sans-serif;
  border: 0px;
  border-radius: 8px;
  pointer-events: none;
}
</style>

<script>
import * as d3 from 'd3'

export default {
  name: 'D3View',
  props: {
    title: String,
    real_data: Array,
    date: String
  },
  data () {
    return {
      gdp: this.real_data
    }
  },
  mounted () {
    this.generateArc()
  },
  methods: {
    generateArc () {
      const w = 1000
      const h = 1000

      const svg = d3
        .select('#gdpview')
        .append('svg')
        .attr('width', w)
        .attr('height', h)
      console.log(this.title)
      console.log(this.real_data)
      console.log('gdps!')
      console.log(this.gdp)
      const sortedGDP = this.gdp.sort((a, b) => (a.value > b.value ? 1 : -1))
      const color = d3.scaleOrdinal(d3.schemeDark2)

      const maxGDP = d3.max(sortedGDP, o => o.value)

      const angleScale = d3
        .scaleLinear()
        .domain([0, maxGDP])
        .range([0, 1.5 * Math.PI])

      const arc = d3
        .arc()
        .innerRadius((d, i) => (i + 1) * 10.25)
        .outerRadius((d, i) => (i + 2) * 10.25)
        .startAngle(angleScale(0))
        .endAngle(d => angleScale(d.value))

      const g = svg.append('g')

      var dict = {}

      // Define the div for the tooltip
      var div = d3.select('body').append('div')
        .attr('class', 'tooltip')

      g.selectAll('path')
        .data(sortedGDP)
        .enter()
        .append('path')
        .attr('d', arc)
        .attr('fill', (d, i) => { dict[d.country] = color(i); return color(i) })
        .attr('stroke', '#FFF')
        .attr('stroke-width', '1px')
        .on('mouseover', function (event, d) {
          d3.select(this)
            .attr('opacity', 0.5)
          div.transition()
            .duration(200)
            .style('opacity', 0.9)
          div.html(d.country + '<br/>' + d.value + ' GiB')
            .style('left', (event.pageX) + 'px')
            .style('top', (event.pageY - 28) + 'px')
            .style('background', dict[d.country])
        })
        .on('mouseout', function (event, d) {
          d3.select(this)
            .attr('opacity', 1.0)
          div.transition()
            .duration(500)
            .style('opacity', 0)
        })
      g.selectAll('text')
        .data(this.gdp)
        .enter()
        .append('text')
        .text(d => `${d.country} -  ${d.value} [GiB]`)
        .attr('x', -150)
        .attr('dy', -8)
        .attr('y', (d, i) => -(i + 1) * 10.25)

      g.attr('transform', 'translate(400,300)')
    }
  }
}
</script>
