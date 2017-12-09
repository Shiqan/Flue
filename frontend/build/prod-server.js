var express = require('express')
var path = require('path')
var serveStatic = require('serve-static')

var port = process.env.PORT || 8080
app = express()

console.log(__dirname)
console.log(path.join(__dirname, 'dist'))
app.use(serveStatic(path.join(__dirname, '../dist')))

console.log('> Starting server...')
var server = app.listen(port)
console.log('> Listening at ' + port + '\n')
