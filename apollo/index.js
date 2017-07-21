var express = require('express')
var mongoose = require('mongoose')
var bodyParser = require('body-parser')

var app = express()

app.use(bodyParser.urlencoded())
app.use(bodyParser.json())
app.use(express.static(__dirname + '/client'))

console.log('Start')

app.get('/home', function(req, res) {
    res.sendfile('./client/index-react.html')
})

app.listen(3000)