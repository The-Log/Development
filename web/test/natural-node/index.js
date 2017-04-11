var natural = require('natural'),
    TfIdf = natural.TfIdf,
    tfidf = new TfIdf();
var wordnet = new natural.WordNet();

var doc = "With the Gardiners, they were always on the most intimate terms. Darcy, as  well as Elizabeth, really loved them; and they were both ever sensible of  the warmest gratitude towards the persons who, by bringing her into  Derbyshire, had been the means of uniting them."
var doc2 = "Lady Catherine was extremely indignant on the marriage of her nephew; and  as she gave way to all the genuine frankness of her character in her reply  to the letter which announced its arrangement, she sent him language so  very abusive, especially of Elizabeth, that for some time all intercourse  was at an end. But at length, by Elizabeth’s persuasion, he was prevailed  on to overlook the offence, and seek a reconciliation; and, after a little  further resistance on the part of his aunt, her resentment gave way,  either to her affection for him, or her curiosity to see how his wife  conducted herself; and she condescended to wait on them at Pemberley, in  spite of that pollution which its woods had received, not merely from the  presence of such a mistress, but the visits of her uncle and aunt from the  city."
var docArray = doc.split(" ")
tfidf.addDocument(doc);
tfidf.addDocument(doc2);
docArray.forEach(function(entry) {
  var entry = entry.replace(/(\r\n|\n|\r|\t| )/gm,"");
  entry = entry.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()“"]/g,"");
  // console.log([entry]);
  if (entry.length > 0 ) {
    wordnet.lookup(entry, function(results) {
        results.forEach(function(result) {
            console.log(entry + " : " + result.pos);
        });
    });
  }
});

// if (result.pos.startsWith("n")) {
  // tfidf.tfidfs(entry, function(i, measure) {
  //   if (measure > 0) {
  //     console.log(entry + " is " + measure);
  //   }
  // })
// }
