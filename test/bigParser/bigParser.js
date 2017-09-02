const Grid = require('bigparser')
var searchTerm = ""
var bigparser = new Grid("2018ankurm@gmail.com", "BigBarserBandhi", '5998a0e1eead21301bfe5c5e', function(){
    bigparser.getRows({'rowCount': '4', 'search':{"target": [searchTerm]}, columns:["Source","Weight"]}, function(rows){ console.log(rows);});
});
