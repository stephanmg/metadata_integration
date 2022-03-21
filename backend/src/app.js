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

////////////////////////////////////////////////////////////////////////////////
// INTERNAL USAGE OF REST API FOR WEB APPLICATION
////////////////////////////////////////////////////////////////////////////////
app.post('/register', (req, res) => {
    res.send({ message: `User ${req.body.email} was registered!`})
})

app.post('/query', (req, res) => {
    var type = req.body.queryType;
    axios.get(`http://localhost:8181/api/query/statistics/${type}`).then(function (myrespo) {
        res.send({ message: `Statistics of ${req.body.queryType} have been requested`, 
              mydata: myrespo.data.count})
    })
})
