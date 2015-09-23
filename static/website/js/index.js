var midwidth, midheight;

window.onload = function () {
    midwidth = window.innerWidth / 2;
    midheight = window.innerHeight / 2;

    $("#photo").css("left", midwidth + "px");
    $("#photo").css("top", midheight - $("#photo").height() / 2 + "px");

    $("#smile").css("left", "100px");
    $("#smile").css("top", midheight - $("#photo").height() / 2 - 15 + "px");
    $("#love").css("left", midwidth - 200 + "px");
    $("#love").css("top", midheight - 100 + "px");
    $("#secret").css("left", midwidth / 2 + "px");
    $("#secret").css("top", midheight + $("#photo").height() / 2 - 50 + "px");
}

function musicswitch()
{
    var t = document.getElementById("bgmusic");

    if (t.paused)
    {
        t.play();
    }
    else
    {
        t.pause();
    }
}
