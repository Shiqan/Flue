var config = require('../config')
if (!process.env.NODE_ENV) {
  process.env.NODE_ENV = JSON.parse(config.build.env.NODE_ENV)
}
var express = require('express')
var path = require('path')
var serveStatic = require('serve-static')

var port = process.env.PORT || config.dev.port
app = express()

console.log(__dirname)
console.log(path.join(__dirname, 'dist'))
app.use(serveStatic(path.join(__dirname, '../dist')))

console.log('> Starting server...')
var server = app.listen(port)
console.log('> Listening at ' + port + '\n')
