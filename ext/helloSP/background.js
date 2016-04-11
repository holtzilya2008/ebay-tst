
chrome.browserAction.onClicked.addListener(function(tab) {
  // No tabs or host permissions needed!
  alert('clicked!!');
  console.log('Turning ' + tab.url + ' red!');
  chrome.tabs.executeScript({
    code: 'document.body.style.backgroundColor="red"'
  });
});
