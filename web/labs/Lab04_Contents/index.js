var express = require('express');
var app = express();
var cheerio =  require("cheerio");
var request = require("request");
var path = require('path');
var natural = require("natural");
  TfIdf = natural.TfIdf,
  nounInflector = new natural.NounInflector();
  tfidf = new TfIdf();
var pos = require('pos');

var NGrams = natural.NGrams;
var stopWords = require('stopwords').english;
require('events').EventEmitter.prototype._maxListeners = 100;

var tempURL = "https://www.gutenberg.org/files/84/84-h/84-h.htm";//"https://www.gutenberg.org/files/1342/1342-h/1342-h.htm";
var url = tempURL;
var book = "";

var charsToSig = new Map();

request(url, function(error, response, html){
  if(!error && response.statusCode == 200){
    var $ = cheerio.load(html);
    $("p").each(function(ix, element) {
      if (typeof element.children[0].data != 'undefined') {
        var cleanData = element.children[0].data.replace(/(\r\n|\n|\r|\t|    )/gm,"");
        // console.log(cleanData);
        if (cleanData.length > 0) {
           book = book + cleanData;
        }
      }
    })

    book = book.replace(/[.,\/#!?$%\^&\*;:{}=\_`~()’"“”]/g,"");
    book = book.replace(/[-—]/g," ");
    // book = book.toLowerCase();

    var words = new pos.Lexer().lex(book);
    var tagger = new pos.Tagger();
    var taggedWords = tagger.tag(words);

    importantWords = "";

    for (var i = 0; i < taggedWords.length; i++) {
      var taggedWord = taggedWords[i];
      var word = taggedWord[0];
      var tag = taggedWord[1];
      if (tag == ('NNS')) {
        word = nounInflector.singularize(word)
      }
      if(tag == 'NNP' && !word.startsWith('Mr') && !word.startsWith('Miss')){
        if(charsToSig.has(word)){
          var freq = charsToSig.get(word) + 1;
          charsToSig.set(word, freq)
        }
        else{
          var freq = 1;
          charsToSig.set(word, freq)
        }
      }
    }

    a = [];
    for(var x of charsToSig)
      a.push(x);

    a.sort(function(x, y) {
      return y[1] - x[1];
    });

    // console.log(a);
    characters = "";
    for (var i = 0; i < 5; i++) {
      if (i < 4) {
        characters += a[i][0] + ", "
      }
      else {
        characters += "and " + a[i][0] + "."
      }
    }

    console.log("The 5 most significant/locations characters are: " + characters);

    diagramBook = NGrams.bigrams(book);
    trigramBook = NGrams.trigrams(book);
  }
});

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function (req, res) {
  res.sendFile('index.html');
});

app.listen(8080, function () {
  console.log('hosted on: http://localhost:8080');
});
