var l = [];
var target, parent, counter;
var isRunning = false;
function highlight2(event){
  if(isRunning == true){
    isRunning = false;
    element = null;
    l = [];
  }
  if(target == null)
    console.log("Out of area");
  clearTimeout(counter);
  target = event.target;
  parent = target;
  while(target.tagName != "DIV"){
    target = target.parentElement;
  }
  l.push(target);
  if(isRunning == false){
    isRunning = true;
    clearTimeout(counter);
    counter = setInterval(call2, 700);
    return;
  }
}

function call2(){
  console.log(l);
  var element = l.pop();
  if(l.length == 0 && element.children.length == 0 && element.nextElementSibling == null){
    element.style.border = "thick solid yellow";
    var counter2 = setInterval(function() {
      element.style.border = "";
    }, 700);
    clearTimeout(counter);
    isRunning = false;
    return;
  }
  if (element.nextElementSibling != null && l.indexOf(element.nextElementSibling) <= -1)
    l.push(element.nextElementSibling);
  for (var i = element.children.length - 1; i >= 0; i--) {
    console.log(element.children[i]);
    if(element.children[i].tagName == "DIV" && l.indexOf(element.children[i]) <= -1){
      l.push(element.children[i]);
    }
  }
  element.style.border = "thick solid yellow";
  var counter2 = setInterval(function() {
    element.style.border = "";
    clearTimeout(counter2)
  }, 700);
}

  // function call2() {
  //   element.style.border = "";
  //   if(element.children.length > 0){
  //     for (var i = 0; i < target.children.length; i++) {
  //       if(element.children[i].tagName == "DIV"){
  //         element = element.children[i];
  //         break;
  //       }
  //     }
  //   }
  //   else if(element.children.length == 0 && element.nextElementSibling != null){
  //     element = element.nextElementSibling;
  //     element.style.border = "thick solid yellow";
  //   }
  //   else if (element.parentElement.parentElement.nextElementSibling !=null){
  //     element = element.parentElement.parentElement.nextElementSibling;
  //     element.style.border = "thick solid yellow";
  //   }
  //   element.style.border = "thick solid yellow";
  //   counter2 = setInterval(function() {
  //     element.style.border = "";
  //     clearTimeout(counter2);
  //   }, 700);
  //   clearTimeout(counter);
  //   isRunning = false;
  //   return;
  // }

  // var isRunning = false;
  // var idnum = 0;
  // function highlight(event){
  //   for (var i = 0; i < 15; i++) {
  //     document.getElementById(i).style.border = "";
  //   }
  //   var tgtid = event.target.id;
  //   console.log(idnum);
  //   console.log(tgtid);
  //   if(tgtid == "bs-example-navbar-collapse-1")
  //     tgtid = 0
  //   else{
  //     document.getElementById(idnum).style.border = "";
  //   }
  //   idnum = tgtid - 1;
  //   if(isRunning == false){
  //     console.log(idnum);
  //     setInterval(call, 700);
  //     isRunning = true;
  //   }
  // }
  // function call() {
  //   if (idnum >= 0 && idnum <= 15)
  //     document.getElementById(idnum).style.border = "";
  //   if(idnum >= 15){
  //     console.log("waiting for next click");
  //   }
  //   else {
  //     idnum ++;
  //     document.getElementById(idnum).style.border = "thick solid yellow";
  //   }
  // }



  // if(target.children.length == 0){
  //   element = target.nextSibling
  //   element.style.border = "thick solid yellow";
  // }
  // if (target.children.length > 0){
  //   for (var i = 0; i < target.children.length; i++) {
  //     if(target.children[i].tagName == "DIV"){
  //       element = target.children[i]
  //       element.style.border = "thick solid yellow";
  //       return;
  //     }
  //   }
  // }
