var express = require('express')
var app = express()
var cheerio =  require("cheerio");
var request = require("request");
var path = require('path');
var natural = require("natural");
  TfIdf = natural.TfIdf,
  tfidf = new TfIdf();
var wordnet = new natural.WordNet();

var stopWords = new Set(['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours\tourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', "versus", "total", "factors", "controlled", "repair", "cancer", "randomized", "study", "outcomes", "reconstruction", "safety", "open", "analysis", 'meta-analysis”', '“comparison', '“the', 'study”', "cancer:", "clinical", "Mr", "Mrs", "she", "he", "though", "Mr", "done—done", "will", "dear", "no", "one", "soon", "good", "miss", "two", "however", "ever", "us", "three", "four", "five", "six", "seven", "eight"]);

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function (req, res) {
  res.sendFile('index.html');
})

var tempURL = "https://www.gutenberg.org/files/1342/1342-h/1342-h.htm";
var url = tempURL;
var book = "";
request(url, function(error, response, html){
  if(!error && response.statusCode == 200){
    var $ = cheerio.load(html);
    $("p").each(function(ix, element) {
      var cleanData = element.children[0].data.replace(/(\r\n|\n|\r|\t|    )/gm,"");
      if (cleanData.length > 0) {
         book = book + cleanData;
      }
    })

    book = book.replace(/[.,\/#!?$%\^&\*;:{}=\_`~()’"“”]/g,"");
    book = book.replace(/[-—]/g," ");
    book = book.toLowerCase();


    tfidf.addDocument(book);

    var l = tfidf.listTerms(0);

    stopWords.forEach(function(entry){
      for (var i = 0; i < l.length; i++) {
        if (l[i].term.toLowerCase() == entry || l[i].term.length <= 4) {
          l.splice(i, i+1);
        }
      }
    });

    for (var i = 0; i < 10; i++) {
      console.log(l[i].term + ': ' + l[i].tfidf);
    }
  }
});

app.listen(8080, function () {
  console.log('hosted on: http://localhost:8080');
});
