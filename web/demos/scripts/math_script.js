function clicked() {
  console.log("Button was clicked");
  var first = document.getElementById("first");
  var second = document.getElementById("second");
  var v1 = first.value;
  var v2 = second.value;
  var product = v1 * v2;
  document.getElementById("outputDiv").innerHTML = product;
}
