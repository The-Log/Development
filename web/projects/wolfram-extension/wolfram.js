console.log("Loaded");
$("#input").on('keyup', function (e) {
    if (e.keyCode == 13) {
        sendRequest();
        console.log("xd");
    }
});

$("#select").on('click',sendRequest);

function sendRequest(){
    //get the current zip code from input
    var input = "" + $("#input").val();
    if(input == "Snowshal" || input == "Snowshal Reddy" || input == "Boshal"|| input == "Boshal Reddy"){
        input = "Adolf Hitler";
    }
    var inFormated = input.split(' ').join('%20');
    var inFormated = input.split('+').join('plus');

    console.log(inFormated);
    //call ajax
    var myURL = "https://api.wolframalpha.com/v2/query"
    var inputData={
        appid: "?appid=RJK7TT-LX4QXPHE4A",
        input: "&input=" + inFormated,
        output: "&output=json"
    }
    var newURL = myURL + inputData.appid + inputData.input +inputData.output;
    console.log(newURL);
    // $.ajax({
    //     url:newURL,
    //     success:function(data){
    //         displayResult(data);
    //     },
    //     dataType: "jsonp"
    // })
    $.getJSON(newURL, function(data){
      console.log(data);
      displayResult(data);
    })
}

function displayResult(obj){
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
  document.getElementById("results").style.visibility = "visible";
  $("#results").fadeOut(500).fadeIn(500);
}
