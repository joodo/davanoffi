$(document).ready(function() {
    setInterval("textChanged();", 1000);
    $(window).resize(resize);
    resize();
})

function resize() {
    var h = $(window).height();
    $("textarea").height(h - 150);
}

function textChanged() {
    var l = $("textarea").val().length;
    var alpha = saw(l, 200) / 160.0 - 0.2;
    $("#cheshire").animate({"opacity": alpha});
}

function saw(x, l) {
    return Math.abs((x+l) % (2*l) - l);
}
