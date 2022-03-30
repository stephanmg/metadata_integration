const express = require("express")
const bodyParser = require("body-parser")
const cors = require("cors")
const morgan = require("morgan")
const { response } = require("express")
const axios = require("axios")
const app = express()
const api = require('./api.js')

// TODO: Get rid of CORS
// TODO: Use some tool to create documentation for REST API
////////////////////////////////////////////////////////////////////////////////
// WEB APPLICATION SETUP
////////////////////////////////////////////////////////////////////////////////
app.use(morgan("combined"))
app.use(bodyParser.json())
app.use(cors())

////////////////////////////////////////////////////////////////////////////////
// WEB APPLICATION START
////////////////////////////////////////////////////////////////////////////////
app.listen(process.env.PORT || 8181, "localhost")

// TODO: Implement and contact to actual database (rdflib or mongodb)
////////////////////////////////////////////////////////////////////////////////
/// PUBLIC REST API
////////////////////////////////////////////////////////////////////////////////
app.get('/api/query/statistics/Files', (_, res) => {
    res.send({message: 'Count', count:1337})
})

app.get('/api/query/statistics/Projects', (_, res) => {
    res.send({message: 'Count', count:31331337})
})

app.get('/api/query/statistics/Usage', (_, res) => {
    res.send({message: 'Count', count:-100})
})

app.get('/api/query/statistics/MyGDP', (_, res) => {
    /// TODO: populate with real json data from myjsondata.json of graph 
    /// representation from backend (rdflib), then in frontend populate
    /// the D3ViewVariant graph view or create a better graph view... 
    /// can be general for SPARQL queries (CONSTRUCT) returning a triple
    /// store data set
    //res.send({message: 'Count', count:0})
    res.send(fake_data2)
})

// TODO: Not real JSON but array of javascript objects! need json!
fake_data2 = [
{ country: 'P01', value: 5 },
{ country: 'P02', value: 13.4 },
{ country: 'P03', value: 4.0 },
{ country: 'P08', value: 4.9 },
{ country: 'P14', value: 2.8 }
]

fake_data = `
{
  "nodes":[
		{"name":"node1","group":1},
		{"name":"node2","group":2},
		{"name":"node3","group":2},
		{"name":"node4","group":3}
	],
	"links":[
		{"source":2,"target":1,"weight":1},
		{"source":0,"target":2,"weight":3}
	]
}
`
app.get('/api/query/statistics/Graph', (_, res) => {
    res.send(fake_data)
})

////////////////////////////////////////////////////////////////////////////////
// INTERNAL USAGE OF REST API FOR WEB APPLICATION
////////////////////////////////////////////////////////////////////////////////
app.post('/register', (req, res) => {
    res.send({ message: `User ${req.body.email} was registered!`})
})

app.post('/query', (req, res) => {
    var type = req.body.queryType;

    if (type == 'MyGDP') {
      axios.get(`http://localhost:8181/api/query/statistics/${type}`).then(function (myrespo) {
        res.send(myrespo.data)
      })
    } else if (type == 'Graph') {
      axios.get(`http://localhost:8181/api/query/statistics/${type}`).then(function (myrespo) {
        res.send(myrespo.data)
        })
    } else {
        axios.get(`http://localhost:8181/api/query/statistics/${type}`).then(function (myrespo) {
            res.send({ message: `Statistics of ${req.body.queryType} have been requested`, 
              mydata: myrespo.data.count})})
    }
})
