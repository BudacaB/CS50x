let button = document.getElementById('read');

button.onclick = function() {
    chrome.storage.sync.get('text', function(data) {
        var synth = window.speechSynthesis;
        var msg = new SpeechSynthesisUtterance(data.text);
        synth.speak(msg);
        var r = setInterval(function () {
            synth.resume();
        }, 14000);
    });
};