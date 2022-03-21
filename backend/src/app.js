const express = require("express")
const bodyParser = require("body-parser")
const cors = require("cors")
const morgan = require("morgan")
const { response } = require("express")
const axios = require("axios")

const app = express()
app.use(morgan("combined"))
app.use(bodyParser.json())
app.use(cors())

app.listen(process.env.PORT || 8181, "localhost")

// API Endpoints
/// TODO: Design REST API (prefix with api/)
app.post('/register', (req, res) => {
    res.send({ message: `User ${req.body.email} was registered!`})
})

//
//app.post('/logout', (req, res) => {
//
//})

//
//app.post('/login', (req, res) => {
//
//})

////////////////////////////////////////////////////////////////////////////////
/// PUBLIC REST API
////////////////////////////////////////////////////////////////////////////////
app.get('/api/query', (req, res) => {
    switch (req.query) {
        case 'statistics?type=file':
            res.send({message: 'Files', count: 10})
            break
    }
    res.send({message: 'Count', count:1337})
    // TODO: Implement (and connect with actual database!)
})

////////////////////////////////////////////////////////////////////////////////
/// INTERNAL API
////////////////////////////////////////////////////////////////////////////////
app.post('/query', (req, res) => {
    var type = req.body.queryType;
    var myresult = 0;
    switch (type) {
        case 'Files':
            myresult = 111;
            console.log('DETECTED FILES!!!')
            break;
        case 'Projects':
            myresult = 1000;
            break
    }

    /// HANDLE request from INTERNAL API for Frontend
    axios.get('http://localhost:8181/api/query').then(function (myrespo) {
        console.log("foo!!!")
        console.log(myrespo.data.count)
        res.send({ message: `Statistics of ${req.body.queryType} have been requested`, 
              mydata: myrespo.data.count})
    })

})
