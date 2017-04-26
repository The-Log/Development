var express = require("express");
var app = express();
var http = require("http").Server(app);
var path = require('path');
var io = require("socket.io")(http)

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

io.on("connection", function(socket){
  console.log(socket);
  socket.on("YOUR_EVENT", function(data){
    console.log(data);
  });
});
// app.set('port', (process.env.PORT || 8080));
app.listen(8080, function () {
  console.log('hosted on: http://localhost:8080');
});
