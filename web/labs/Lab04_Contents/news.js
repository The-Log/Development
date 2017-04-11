var express = require('express')
var app = express()
var cheerio =  require("cheerio");
var request = require("request");
var path = require('path');
var natural = require("natural");
  TfIdf = natural.TfIdf,
  tfidf = new TfIdf();
var wordnet = new natural.WordNet();
require('events').EventEmitter.prototype._maxListeners = 100;

var stopWords = require('stopwords').english;

// console.log(stopWords);

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function (req, res) {
  res.sendFile('index.html');
})

var tempURL = "http://www.nytimes.com"; //"https://www.gutenberg.org/files/1342/1342-h/1342-h.htm";
var url = tempURL;
var book = "";
var numDocs = 0;
request(url, function(error, response, html){
  if(!error && response.statusCode == 200){
    var $ = cheerio.load(html);
    $("a").each(function(ix, element) {
      //console.log(element.attribs.href);
      suburl = element.attribs.href
      if (suburl.startsWith("http")) {
        examine(suburl);
        console.log(tfidf);
      }
    });
  }
});

function examine(url, callback) {
  var page_contents = ""
  request(url, function(error, response, html){
    if(!error && response.statusCode == 200){
      var $ = cheerio.load(html);
      $("p").each(function(ix, element) {
        if (typeof element.children[0] != 'undefined' && typeof element.children[0].data != 'undefined') {
          var cleanData = element.children[0].data.replace(/(\r\n|\n|\r|\t|    )/gm,"");
          // console.log(cleanData);
          cleanData = cleanData.toLowerCase();
          if (!cleanData.startsWith("by") && cleanData.length > 0) {
            cleanData = cleanData.replace(/[-—]/g," ");
            cleanData = cleanData.replace(/[1234567890]/g," ");
            page_contents += cleanData;
          }
        }
      })
      callback(page_contents);
    }
  });
}

app.listen(8080, function () {
  console.log('hosted on: http://localhost:8080');
});
