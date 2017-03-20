console.log("Loaded");

$("#input").on('keyup', function (e) {
    if (e.keyCode == 13) {
        sendRequest();
        console.log("xd");
    }
});

function sendRequest(){
    //get the current zip code from input
    var input = "" + $("#input").val();
    if(input == "Snowshal" || input == "Snowshal Reddy" || input == "Boshal"|| input == "Boshal Reddy"){
        input = "Adolf Hitler";
    }
    var inFormated = input.split(' ').join('%20');
    console.log(inFormated);
    //call ajax
    var myURL = "http://api.wolframalpha.com/v2/query"
    var inputData={
        appid: "?appid=GHAVTU-GJGRU5393J",
        input: "&input=" + inFormated,
        output: "&output=json"
    }
    var newURL = myURL + inputData.appid + inputData.input +inputData.output;
    console.log(newURL);
    $.ajax({
        url:newURL,
        success:function(data){
            displayResult(data);
        },
        dataType: "jsonp"
    })
}

function displayResult(obj){
  document.getElementById("results").style.visibility = "visible";
  if ("pods" in obj.queryresult == false) {
    $("#results").html("Could not find answer! Try something else.");
    return;
  }
  $("#results").html("Output:");
  console.log(obj.queryresult.pods);
  for (var i = 0; i < obj.queryresult.pods.length; i++) {
    var myDiv = document.createElement("DIV");
    myDiv.setAttribute("id", "result" + i);
    myDiv.setAttribute("lang", "latex")
    myDiv.style.padding = "15px"
    $('#results').append(myDiv);
    var temp = obj.queryresult.pods[i].subpods[0].plaintext;
    var image = new Image();
    image.src = obj.queryresult.pods[i].subpods[0].img.src;
    image.alt = temp;
    $("#result" + i).html(image);
  }
  $("#results").fadeOut(500).fadeIn(500);
}
