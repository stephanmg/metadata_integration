<template>
	<div>
		<div id="data_viz" />
	</div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "D3ViewVariant",
  data() {
    return {
      gdp: [
        {country: "USA", value: 20.5 },
        {country: "China", value: 13.4 },
        {country: "Germany", value: 4.0 },
        {country: "Japan", value: 4.9 },
        {country: "France", value: 2.8 }
      ]
    };
  },
    mounted() {
    this.generateArc();
  },
  methods: {
    generateArc() {

		// set the dimensions and margins of the graph
var margin = {top: 500, right: 30, bottom: 30, left: 80},
  width = 800 - margin.left - margin.right,
  height = 800 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

d3.json("http://localhost:8080/myjsondata.json", function(err, data) {
		if (err) {
		console.log("error!")
		} else {
		console.log(data)
		}

	// Initialize the links
  var link = svg
    .selectAll("line")
    .data(data.links)
    .enter()
    .append("line")
      .style("stroke", "#aaa")

  // Initialize the nodes
  var node = svg
    .selectAll("circle")
    .data(data.nodes)
    .enter()
    .append("circle")
      .attr("r", 15)
      .style("fill", "#69b3a2")

		var label = svg.append("g")
      .attr("class", "labels")
      .selectAll("text")
      .data(data.nodes)
      .enter().append("text")
        .attr("class", "label")
        .text(function(d) { return d.id; });


 //  elemEnter.append("text")
//		.attr("dx", function(d){return -20})
//		.text(function(d) { return d.label})


  // Let's list the force we wanna apply on the network
  var simulation = d3.forceSimulation(data.nodes)                 // Force algorithm is applied to data.nodes
      .force("link", d3.forceLink()                               // This force provides links between nodes
            .id(function(d) { return d.id; })                     // This provide  the id of a node
            .links(data.links)                                    // and this the list of links
      )
      .force("charge", d3.forceManyBody().strength(-400))         // This adds repulsion between nodes. Play with the -400 for the repulsion strength
      .force("center", d3.forceCenter(width / 2, height / 2))     // This force attracts nodes to the center of the svg area
      .on("end", ticked);

  // This function is run at each iteration of the force algorithm, updating the nodes position.
  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
         .attr("cx", function (d) { return d.x+6; })
         .attr("cy", function(d) { return d.y-6; });

    label
    	.attr("x", function(d) { return d.x; })
        .attr("y", function (d) { return d.y; })
         .style("font-size", "20px").style("fill", "#4393c3");
  }
	});
	}
  }
}
</script>
