function saveSettings(event){
	var e = document.getElementById("quality");
	var theValue = e.options[e.selectedIndex].value;
	var text = e.options[e.selectedIndex].text;
	chrome.storage.sync.set({'quality': theValue}, function() {
          // Notify that we saved.
          var status=document.getElementById('status');
          status.innerHTML="Settings saved: Quality value is " + text;
          console.log("Settings saved");
        });
}
function  getSettings(event){
	chrome.storage.local.get('quality',function(result){
		var d= document.getElementById('d');
		d.innerHTML=JSON.stringify(result);
	});
}
var testButton=document.getElementById('test');
testButton.addEventListener('click',getSettings);

var saveButton=document.getElementById('save');
saveButton.addEventListener('click',saveSettings);