  chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
     var url = tabs[0].url;
     create(url);

});
function create(a){
  a=a.replace("https","http");
  $('#message').html("Downloading...");
  if(a.indexOf("youtube")!=-1&&a.indexOf("watch")!=-1){

    $.ajax({
        url:'http://127.0.0.1:5000/download',
        data:{
          url:a
        },
        type:"POST",
        dataType:"json",


    });

  }
  else{
    $('#message').html("We are not watching a video in YouTube");
  }
}
