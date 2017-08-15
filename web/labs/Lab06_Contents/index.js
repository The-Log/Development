var express = require("express");
var app = express();
var http = require("http").Server(app);
var path = require('path');
var io = require("socket.io")(http);
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('chatlog.db');

var cLog = [];
var moves = 0;
var game = []

app.use("/media",  express.static(path.join(__dirname, '/media')));
app.use("/css",  express.static(path.join(__dirname, '/css')));
app.use("/js", express.static(path.join(__dirname, '/js')));
app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

db.all("SELECT u, m FROM log", function(err, rows) {
    rows.forEach(function (row) {
        console.log(row.u +": "+row.m);
        cLog.push(row.u +": "+ row.m)
    })
});

io.on("connection", function(socket){
  // console.log(socket);
  socket.emit("connection", {chatLog:cLog});
  socket.on("buttonFromClient", function(data){
    u = data["username"];
    m = data["message"];
    s = u + ": " + m;
    cLog.push(s);
    console.log(s);
    var stmt = db.prepare("INSERT INTO log VALUES (?, ?)");
    stmt.run(u, m);
    io.emit("sendBack", {chatLog:cLog});
  });
  socket.on("move",function(data){
    for (var i = 0; i < game.length; i++) {
      if (game[i].username == data.username) {
        console.log("Not allowed!");
        return;
      }
    }
    if (moves >= 1) {
      console.log(data.username +": "+ data.move);
      game.push(data);
      console.log(game);
      s = displayWinner(game) + " wins!";
      console.log(s);
      io.emit("endGame", {game: game, winner: s});
      game = []
      moves = 0;
    }
    else {
      console.log(data.username +": "+ data.move);
      game.push(data);
      moves++;
    }
  });
});

function displayWinner(game){
  move0 = game[0].move;
  move1 = game[1].move;
  var stmt = db.prepare("INSERT INTO games VALUES (?, ?, ?, ?)");
  stmt.run(game[0].username, move0, game[1].username, move1);
  if ((move0 == 'rock' && move1 == 'scissors') || (move0 == 'paper' && move1 == 'rock') || (move0 == 'scissors' && move1 == 'paper')) {
    return game[0].username
  }
  if ((move1 == 'rock' && move0 == 'scissors') || (move1 == 'paper' && move0 == 'rock') || (move1 == 'scissors' && move0 == 'paper')) {
    return game[1].username
  }
  else {
    return "No one";
  }
}

// app.set('port', (process.env.PORT || 8080));
http.listen(8080, function(){
  console.log('hosted on: http://localhost:8080');
})
