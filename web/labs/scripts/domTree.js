var isRunning = false;
var idnum = 0;
function highlight(event){
  var tgtid = event.target.id;
  console.log(idnum);
  console.log(tgtid);
  if(tgtid == "bs-example-navbar-collapse-1")
    tgtid = 0
  else{
    document.getElementById(idnum).style.border = "";
  }
  idnum = tgtid - 1;
  if(isRunning == false){
    console.log(idnum);
    setInterval(call, 700);
    isRunning = true;
  }
}
function call() {
  if (idnum >= 0 && idnum <= 15)
    document.getElementById(idnum).style.border = "";
  if(idnum >= 15){
    console.log("waiting for next click");
  }
  else {
    idnum ++;
    document.getElementById(idnum).style.border = "thick solid yellow";
  }
}
