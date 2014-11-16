$(document).ready(function() {
    var MAX_LEVEL = 100;
    var gauge = new JustGage({
        id: "gauge",
        value: 0,
        min: 0,
        max: MAX_LEVEL,
        title: "-",
    });
    
    function updateArousalLevel(level) {
        $("#arousalLevel").text(level);

        // set background color
        //r = (level / MAX_LEVEL) * 255;
        //g = ((MAX_LEVEL - level) / MAX_LEVEL) * 255;
        //$("body").css("background-color", "rgb("+ Math.floor(r) + "," + Math.floor(g) + "," + "0)");

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
