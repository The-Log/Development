var WordPOS = require('wordpos'),
    wordpos = new WordPOS();

wordpos.getNouns('Darcey sucked me off.', function(result){
    console.log(result);
});
// [ 'little', 'angry', 'frightened' ]

wordpos.isAdjective('awesome', function(result){
    console.log(result);
});
