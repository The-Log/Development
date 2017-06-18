//06-12-2017, Ankur Mishra & Cameron Mukerjee
var express = require("express");
var app = express();
var http = require("http").Server(app);
var path = require('path');
var cheerio =  require("cheerio");
var request = require("request");
var io = require("socket.io")(http);
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('priceHistory.db');

app.use("/media",  express.static(path.join(__dirname, '/media')));
app.use("/css",  express.static(path.join(__dirname, '/css')));
app.use("/js", express.static(path.join(__dirname, '/js')));
app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});
app.get('/search', function(req, res) {
  res.sendFile(__dirname + '/search.html');
});

http.listen(8080, function(){
    console.log("Server started.");
})

io.on("connection", function(socket){
  // console.log(socket);
  socket.on("sendQuery", function(data){
    var query = data.query;
    console.log(query);
    searchWalmart(query, socket);
    //searchAmazon(query)
  });
});

var walmart_key = "d9n2yn9pym46wzajadrvdv7k";
var walmart = require('walmart')(walmart_key);
var searchQuery = "iphone";
var productMap = {};


function searchWalmart(query, socket){
  productMap = {};
  walmart.stores.search(100, query).then(function(data) {
    for (var i = 0; i < data.count; i++) {
      console.log(data.results[i].name);
      // console.log(data.results[i].price.priceInCents / 100);
      // console.log(data.results[i].images.largeUrl);
      // console.log("https://www.walmart.com" + data.results[i].walmartCanonicalUrl)
      // console.log(data.results[i]);
      productMap[data.results[i].name] = [data.results[i].price.priceInCents / 100, data.results[i].images.largeUrl, "https://www.walmart.com" + data.results[i].walmartCanonicalUrl ]
      // console.log();
    }
    console.log(productMap);
    socket.emit("productMap", {pm:productMap})
  });
}
