time = 240;
var score = 0;
var isRunning = false;
function disableText(){
  document.getElementById("input").style.visibility = "hidden";
}
function startTimer(){
  if(isRunning == false){
    counter = setInterval(decrementTime, 1000);
    document.getElementById("input").style.visibility = "visible";
    isRunning = true;
  }
}
function decrementTime()
{
  time = time-1;
  if (time <= 0)
  {
     alert('Game over. You got: ' + score + "/" + richPeople.length);
     reset();
     return;
  }
  document.getElementById("timer").innerHTML= time + " secs";
}

function pause() {
  clearTimeout(counter);
  isRunning = false;
  document.getElementById("input").style.visibility = "hidden";
}

function reset() {
  time = 240;
  score = 0;
  clearTimeout(counter);
  document.getElementById("input").style.visibility = "hidden";
  document.getElementById("timer").innerHTML= time + " secs";
  isRunning = false;
  for (var i = 0; i < richPeople.length; i++) {
    document.getElementById("rich" + [i+1]).innerHTML= "";
  }
}

function check(){
  var in1 = document.getElementById("input");
  var i;
  for(i = 0; i < richPeople.length; i++){
    if (richPeople[i].toLowerCase() == in1.value.toLowerCase()){
      document.getElementById("rich" + [i+1]).innerHTML= richPeople[i];
      document.getElementById("input").value = "";
      score =  score + 1;
      if(score == richPeople.length){
        alert("You won!");
        reset();
      }
    }
    console.log(score);
  }
}

var richPeople = [
  "Bill Gates",
  "Amancio Ortega",
  "Jeff Bezos",
  "Vladimir Putin",
  "Warren Buffet",
  "Carlos Slim",
  "Mark Zuckerberg",
  "Ingvar Kamprad",
  "Larry Ellison",
  "Charles Koch",
  "David Koch",
  "Larry Page",
  "Sergey Brin",
  "Micheal Bloomberg",
  "Liliane Bettencourt",
  "Bernard Arnault",
  "Christy Walton",
  "Sam Walton",
  "Jim Walton",
  "King of Thailand"
];
