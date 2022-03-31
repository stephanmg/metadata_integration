<template>
<div>
<h3> {{title}} </h3>
<h4> Compiled on {{date}} </h4>
<div id='gdpview' />
</div>
</template>

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
      const w = 500
      const h = 500

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
        .innerRadius((d, i) => (i + 1) * 25)
        .outerRadius((d, i) => (i + 2) * 25)
        .startAngle(angleScale(0))
        .endAngle(d => angleScale(d.value))

      const g = svg.append('g')

      g.selectAll('path')
        .data(sortedGDP)
        .enter()
        .append('path')
        .attr('d', arc)
        .attr('fill', (d, i) => color(i))
        .attr('stroke', '#FFF')
        .attr('stroke-width', '1px')
        .on('mouseenter', function () {
          d3.select(this)
            .transition()
            .duration(200)
            .attr('opacity', 0.5)
        })
        .on('mouseout', function () {
          d3.select(this)
            .transition()
            .duration(200)
            .attr('opacity', 1)
        })

      g.selectAll('text')
        .data(this.gdp)
        .enter()
        .append('text')
        .text(d => `${d.country} -  ${d.value} [GiB]`)
        .attr('x', -150)
        .attr('dy', -8)
        .attr('y', (d, i) => -(i + 1) * 25)

      g.attr('transform', 'translate(200,300)')
    }
  }
}
</script>
