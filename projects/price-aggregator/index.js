function sendRequest(){
    //get the current zip code from input
    var input = "" + $("#input").val();
    var inFormated = input.split(' ').join('%20');
    console.log(inFormated);
    //call ajax
    var url = "http://api.wolframalpha.com/v2/query"
    var inputData={
        callname:  "FindPopularItems",
        appid: "&appid=GHAVTU-GJGRU5393J",
        responseencoding: "JSON",
        version: 713
    }
    $.ajax({
        url:url,
        success:function(data){
            displayResult(data);
        },
        data:inputData
    })
}

functi
