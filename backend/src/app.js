const express = require("express")
const bodyParser = require("body-parser")
const cors = require("cors")
const morgan = require("morgan")
const res = require("express/lib/response")

const app = express()
app.use(morgan("combined"))
app.use(bodyParser.json())
app.use(cors())

app.listen(process.env.PORT || 8181, "localhost")

app.get('/register', (req, res) => {
    res.send({ message: `User ${req.body.email} was registered!`})
})