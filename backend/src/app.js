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
		{"id":"P01","group":1},
		{"id":"P02","group":2},
		{"id":"P03","group":3},
		{"id":"P04","group":4},
		{"id":"P05","group":5},
		{"id":"P06","group":6},
		{"id":"P07","group":7},
		{"id":"P08","group":8},
		{"id":"P09","group":9},
		{"id":"P10","group":10},
		{"id":"P11","group":11},
		{"id":"P12","group":12},
		{"id":"P13","group":13},
		{"id":"P14","group":14},
		{"id":"P15","group":15},
		{"id":"P16","group":16},
		{"id":"P17","group":17},
		{"id":"P18","group":18}
	],
	"links":[
		{"source":"P01","target":"P03","value":1},
		{"source":"P02","target":"P04","value":3},
		{"source":"P03","target":"P04","value":10},
		{"source":"P01","target":"P04","value":20},
		{"source":"P05","target":"P04","value":1},
		{"source":"P06","target":"P04","value":1},
		{"source":"P06","target":"P04","value":1},
		{"source":"P07","target":"P02","value":1},
		{"source":"P06","target":"P03","value":1},
		{"source":"P04","target":"P07","value":1},
		{"source":"P01","target":"P18","value":1},
		{"source":"P01","target":"P17","value":1},
		{"source":"P07","target":"P09","value":1},
		{"source":"P07","target":"P12","value":1},
		{"source":"P07","target":"P18","value":1},
		{"source":"P07","target":"P13","value":5},
		{"source":"P17","target":"P14","value":3},
		{"source":"P17","target":"P15","value":1},
		{"source":"P12","target":"P08","value":10},
		{"source":"P12","target":"P10","value":1},
		{"source":"P10","target":"P16","value":1},
		{"source":"P16","target":"P11","value":5}
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
