var isRunning = false;
var idnum = 0;
function highlight(event){
  var tgtid = event.target.id;
  console.log(idnum);
  document.getElementById(idnum).style.border = "";
  idnum = tgtid - 1;
  if(isRunning == false){
    console.log(idnum);
    setInterval(call, 1000);
    isRunning = true;
  }
}
function call() {
  if (idnum >= 0 && idnum <= 14)
    document.getElementById(idnum).style.border = "";
  if(idnum >= 14){
    console.log("waiting for next click");
  }
  else {
    idnum ++;
    document.getElementById(idnum).style.border = "thick solid yellow";
  }
}
