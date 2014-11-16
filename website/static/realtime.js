$(document).ready(function() {

    var MAX_LEVEL = 100;
    var gauge = new JustGage({
        id: "gauge",
        value: 0,
        min: 0,
        max: MAX_LEVEL,
        title: "-",
    });

    // http://docs.justyo.co/v1.0/docs/yoall
    // sends yo to all subscribers;
    // to subscribe, simply "yo" at arousr
    // so this is definitely rate-limited, just an FYI
    function yoyoyoyoyoyoyo() {
        var http = new XMLHttpRequest();
        var url = "https://api.justyo.co/yoall/";
        var params = "api_token=ab28cb22-50ae-4d42-a21c-e9983a39f3e6";
        http.open("POST", url, true);

        http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        http.setRequestHeader("Content-length", params.length);
        http.setRequestHeader("Connection", "close");

        http.onreadystatechange = function() {
            if(http.readyState == 4 && http.status == 200) {
                alert(http.responseText);
            }
        }
        http.send(params);
    }

    document.update = updateArousalLevel;
    function updateArousalLevel(level) {

        // set background color
        //r = (level / MAX_LEVEL) * 255;
        //g = ((MAX_LEVEL - level) / MAX_LEVEL) * 255;

        gauge.refresh(level);
    }

    function updatePicture() {
        $("#image").attr("src", "http://10.9.167.106:8080/shot.jpg");
    }

    function mainLoop() {
        $.get("./getarousallevel", function(data) {
            console.log("Got data " + data);
            updateArousalLevel(data);
        });
        $.get("./isaroused", function(data) {
          console.log("Got data " + data);
            if(data == "True"){
              setAlarmColor();
              updatePicture();
              setInterval(setNormalColor, 80);
              yoyoyoyoyoyoyo()
            }

        });
        //updatePicture();
    }

    function setNormalColor(){
      $("body").css("background-color", '#B1B0B3');
    }
    function setAlarmColor(){
      $("body").css("background-color", '#DF8700');
    }

    // main loop, omg this is so hacky doe
    mainLoop();
    setInterval(mainLoop, 250);

});
