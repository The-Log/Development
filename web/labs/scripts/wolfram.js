console.log("Loaded");
function sendRequest(){
    //get the current zip code from input
    var input = "" + $("#input").val();
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
            console.log(data.queryresult.pods[1].subpods[0]);
        },
        dataType: "jsonp"
    })
}

function displayResult(obj){
  document.getElementById("results").style.visibility = "visible";
  if ("pods" in obj.queryresult == false) {
    console.log("xd");
    $("#results").html("Could not find answer! Try something else.");
    return;
  }
  $("#results").html("Output:");
  for (var i = 0; i < obj.queryresult.pods.length; i++) {
    var myDiv = document.createElement("DIV");
    myDiv.setAttribute("id", "result" + i);
    myDiv.style.padding = "15px"
    $('#results').append(myDiv);
    var temp = obj.queryresult.pods[i].subpods[0].img;
    var image = new Image();
    image.src = temp.src;
    $("#result" + i).html(image);
  }
  console.log(image);
}
