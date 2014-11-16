$(document).ready(function() {
    function updateArousalLevel(level) {
        $("#arousalLevel").text(level);

        // set background color
        r = (level / 10) * 255;
        g = ((10 - level) / 10) * 255;

        $("body").css("background-color", "rgb("+ Math.floor(r) + "," + Math.floor(g) + "," + "0)");
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
    setInterval(mainLoop, 250);
});
