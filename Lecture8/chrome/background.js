window.addEventListener('mouseup', e => {
    chrome.storage.sync.set({text: window.getSelection().toString()}, function() {
        console.log("captured text: " + window.getSelection().toString());
    });
});