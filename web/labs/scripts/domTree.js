var l = [];
var temp = 0;
var target, parent, counter;
var isRunning = false;
function highlight2(event){
  if(isRunning == true){
    isRunning = false;
    element = null;
    l = [];
  }
  temp = 0;
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
    counter = setInterval(dfs, 700);
    return;
  }
}

function dfs(){
  console.log(l);
  var element = l.pop();
  if(target.parentElement.parentElement.nextElementSibling != null && l.indexOf(target.parentElement.parentElement.nextElementSibling ) <= -1 && temp == 0){ //add target's parents sibling
    l.push(target.parentElement.parentElement.nextElementSibling);
  }
  if(target.parentElement.nextElementSibling != null && l.indexOf(target.parentElement.nextElementSibling) <= -1 && temp == 0){ //add targets parents' parent's sibling
    l.push(target.parentElement.nextElementSibling);
  }
  temp = 1;
  if(l.length == 0 && element.children.length == 0 && element.nextElementSibling == null){ //end test
    element.style.border = "thick solid yellow";
    var counter2 = setInterval(function() {
      element.style.border = "";
    }, 700);
    clearTimeout(counter);
    isRunning = false;
    return;
  }
  if (element.nextElementSibling != null && l.indexOf(element.nextElementSibling) <= -1) //add sibling
    l.push(element.nextElementSibling);
  for (var i = element.children.length - 1; i >= 0; i--) {
    console.log(element.children[i]);
    if(element.children[i].tagName == "DIV" && l.indexOf(element.children[i]) <= -1){ //add children
      l.push(element.children[i]);
    }
  }
  element.style.border = "thick solid yellow"; //change border
  var counter2 = setInterval(function() {
    element.style.border = "";
    clearTimeout(counter2)
  }, 700);
}
