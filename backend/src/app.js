const express = require("express")
const bodyParser = require("body-parser")
const cors = require("cors")
const morgan = require("morgan")
const { response } = require("express")
const axios = require("axios")
const app = express()

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

// TODO: Implement and connect with actual database
/// TODO: All functionality used here should be extracted into an API class first / utility  class
/// e.g. in a separate js file / module
  
//const helper1 = () => {/* */};
//const helper2 = () => {/* */};

//export default {
// helper1,
//  helper2
//};

////////////////////////////////////////////////////////////////////////////////
/// PUBLIC REST API
////////////////////////////////////////////////////////////////////////////////
app.get('/api/query/statistics/Files', (_, res) => {
    res.send({message: 'Count', count:1337})
})

app.get('/api/query/statistics/Project', (_, res) => {
    res.send({message: 'Count', count:31331337})
})

app.get('/api/query/statistics/Usage', (_, res) => {
    res.send({message: 'Count', count:-100})
})

////////////////////////////////////////////////////////////////////////////////
// INTERNAL REST API FOR WEB APPLICATION
////////////////////////////////////////////////////////////////////////////////
app.post('/register', (req, res) => {
    res.send({ message: `User ${req.body.email} was registered!`})
})

app.post('/query', (req, res) => {
    var type = req.body.queryType;
    var myresult = 0;
    switch (type) {
        case 'Files':
            myresult = 111;
            break;
        case 'Projects':
            myresult = 1000;
            break
    }

    axios.get(`http://localhost:8181/api/query/statistics/${type}`).then(function (myrespo) {
        res.send({ message: `Statistics of ${req.body.queryType} have been requested`, 
              mydata: myrespo.data.count})
    })
})
