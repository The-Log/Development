var express = require("express");
var app = express();
var http = require("http").Server(app);
var path = require('path');
var io = require("socket.io")(http);
var cLog = [];

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

io.on("connection", function(socket){
  // console.log(socket);
  socket.emit("connection", {chatLog:cLog});
  socket.on("buttonFromClient", function(data){
    u = data["username"];
    m = data["message"];
    s = u + " says: " + m;
    cLog.push(s);
    console.log(s);
    io.emit("sendBack", {chatLog:cLog});
  });
});
// app.set('port', (process.env.PORT || 8080));
http.listen(8080, function(){
  console.log('hosted on: http://localhost:8080');
})
