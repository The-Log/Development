function click(e){
  console.log("xd");
  chrome.tabs.query({currentWindow:true, active:true}, function(tabs)){
    console.log("background.js : clicked!");
    alert("Hey kys.")
  }
}
chrome.browserAction.onClicked.addListener(click);
