$(document).ready(function() {
    $(window).resize(resize);
    resize();
})

function resize() {
    var h = $(window).height();
    $("textarea").height(h - 150);
}
