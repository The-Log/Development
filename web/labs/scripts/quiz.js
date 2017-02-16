time = 120;
function timer()
{
  time = time-1;
  if (time <= 0)
  {
     alert('Game over');
     reset();
     return;
  }
  document.getElementById("timer").innerHTML= time + " secs";
}

function reset() {
  time = 120;
  clearTimeout(counter);
  document.getElementById("timer").innerHTML= time + " secs";
}

var richPeople = [
  "Bill Gates",
  "Amancio Ortega",
  "Warren Buffet",
  "Carlos Slim",
  "Jeff Bezos",
  "Mark Zuckerberg",
  "Larry Ellison",
  "Micheal Bloomberg",
  "Charles Koch",
  "David Koch"
]
