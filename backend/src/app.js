const express = require("express")
const bodyParser = require("body-parser")
const cors = require("cors")
const morgan = require("morgan")

const app = express()
app.use(morgan("combined"))
app.use(bodyParser.json())
app.use(cors())

app.listen(process.env.PORT || 8181, "localhost")

// API Endpoints
/// TODO: Design REST API 
app.post('/register', (req, res) => {
    res.send({ message: `User ${req.body.email} was registered!`})
})