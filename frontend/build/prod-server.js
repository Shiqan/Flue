var express = require('express')
var path = require('path')
var serveStatic = require('serve-static')
app = express()
// handle fallback for HTML5 history API
app.use(require('connect-history-api-fallback')())

app.use(serveStatic(__dirname)+"/frontend/dist")
var port = process.env.PORT || 5000
var server = app.listen(port)
console.log('> Starting server...')
console.log('> Listening at ' + port + '\n')
