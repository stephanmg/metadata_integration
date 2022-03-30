<template>
<div>
<div id='arc' />
</div>
</template>

<script>
import * as d3 from 'd3'

export default {
  name: 'GraphView',
  props: {
    title: String,
    real_data: Object
  },
  data () {
    return {
      data: this.real_data
    }
  },
  mounted () {
    this.generateArc()
  },
  methods: {
    generateArc () {
      const w = 960
      const h = 500

      const svg = d3
        .select('#arc')
        .append('svg')
        .attr('width', w)
        .attr('height', h)

      console.log('BLUUUUUUUBBBBB')
      /// TODO: WHy do we have to do this... json stringifx and parse..
      // this.real_data = JSON.parse(JSON.stringify(this.data))
      console.log(JSON.parse(JSON.stringify(this.data)))
      // var force = d3.layout.force() // layout not available, why?
      var force = d3.forceSimulation(JSON.parse(JSON.stringify(this.data)).nodes).force() // layout not available, why?
        .gravity(0.05)
        .distance(100)
        .charge(-100)
        .size([w, h])

      console.log('data before force')
      console.log(this.real_data.nodes)
      force.nodes(this.real_data.nodes)
        .links(this.real_data.links)
        .start()

      var link = svg.selectAll('.link')
        .data(this.real_data.links)
        .enter().append('line')
        .attr('class', 'link')
        .style('stroke-width', function (d) { return Math.sqrt(d.weight) })

      var node = svg.selectAll('.node')
        .data(this.data.nodes)
        .enter().append('g')
        .attr('class', 'node')
        .call(force.drag)

      node.append('circle')
        .attr('r', '5')

      node.append('text')
        .attr('dx', 12)
        .attr('dy', '.35em')
        .text(function (d) { return d.name })

      force.on('tick', function () {
        link.attr('x1', function (d) { return d.source.x })
          .attr('y1', function (d) { return d.source.y })
          .attr('x2', function (d) { return d.target.x })
          .attr('y2', function (d) { return d.target.y })

        node.attr('transform', function (d) {
          return 'translate(' + d.x + ',' + d.y + ')'
        })
      })
    }
  }
}
</script>
