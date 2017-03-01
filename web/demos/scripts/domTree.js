function clickFunction(event) {
  console.log(event);
  var tgt = event.target;
  console.log(tgt);
  children = tgt.children
  console.log(children);
}
