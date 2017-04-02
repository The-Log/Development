var express = require('express')
var app = express()
var path = require('path');

app.use(express.static(path.join(__dirname, 'public')));

app.get('*', function (req, res) {

  res.sendfile('index.html')
})

app.listen(8080, function () {
  console.log('hosted on: http://localhost:8080');
});
