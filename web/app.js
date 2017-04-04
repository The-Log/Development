var express = require('express')
var app = express()
var path = require('path');

app.use(express.static(path.join(__dirname, 'labs')));//grabs all of my labs folder including CSS and JS

app.get('/', function (req, res) {
  res.sendFile('index.html');//sends the top level index file
})

app.listen(8080, function () {   //process.env.PORT, process.env.IP //change to this for c9 usage
  console.log('hosted on: http://localhost:8080'); // host
});
