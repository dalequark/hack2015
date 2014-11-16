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

    function updateArousalLevel(level) {
        $("#arousalLevel").text(level);

        // set background color
        //r = (level / MAX_LEVEL) * 255;
        //g = ((MAX_LEVEL - level) / MAX_LEVEL) * 255;
        //$("body").css("background-color", "rgb("+ Math.floor(r) + "," + Math.floor(g) + "," + "0)");

        // put the call to yoyoyoyoyoyoyoyoyoyoyo() wherever you want there to be a yo
        if (level > 95) {
            yoyoyoyoyoyoyo();
        }
        
        gauge.refresh(level);
    }

    function updatePicture() {
        $("#image").attr("src", "http://10.9.167.106:8080/shot.jpg");
    }

    function mainLoop() {
        $.get("./arousallevel/", function(data) {
            updateArousalLevel(data);
        });
        updatePicture();
    }

    // main loop, omg this is so hacky doe
    mainLoop();
  //  setInterval(mainLoop, 250);

    var num = null;
    $(".btn-group > button.btn").on("click", function(){
      num = this.innerHTML;
      alert("Value is " + num);
    });
});
