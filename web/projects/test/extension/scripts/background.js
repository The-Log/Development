chrome.browserAction.onClicked.addListener(function(tab) {
  console.log("xd")
  chrome.tabs.executeScript(null, {
    file: "replace.js"
  });
});
