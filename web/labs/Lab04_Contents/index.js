var cheerio =  require("cheerio");
var request = require("request");

var url = "http://www.sciencedirect.com/science/journal/00396060";
request(url, function(error, response, html){
  if(!error && response.statusCode == 200){
    var $ = cheerio.load(html);
    $("a").each(function(ix, element) {
      if(element.attribs['data-url'] != undefined && element.attribs['data-url'].startsWith("http"))
        url = element.attribs['data-url'];
        request(url, function(error, response, body){
          if(!error && response.statusCode == 200){
            var $ = cheerio.load(body);
            if(!body.startsWith("\n")){
              console.log([$('div')['4'].children[1].children[0]]);
              console.log("");
            }
          }
        });
    });
  }
});
// var dataURL = "http://www.sciencedirect.com/science/preview/abstract?_rdoc=36&_origin=PublicationdataURL&_srch=hubEid(1-s2.0-S0039606017X00032)&_ct=39&_zone=rslt_list_item&_fmt=full&_pii=S0039606016306389&_issn=00396060&_tab=afr&absLinks=y&md5=79f7add4a145c7e2ae1f7d970408baba"
// request(dataURL, function(error, response, body){
//   if(!error && response.statusCode == 200){
//     var $ = cheerio.load(body);
//     console.log(body);
//     console.log($('div')['4'].children[1].children[0].data);
//   }
// });
