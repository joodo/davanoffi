$(document).ready(function () {
    $("li.post").mouseover(postMouseOver);
    $("li.post").mouseleave(postMouseLeave);
});

function postMouseOver() {
    $(this).find("div.detail_link").show();
}

function postMouseLeave() {
    $(this).find("div.detail_link").hide();
}

function opacityChange(e, o) {
    $(e).stop(true);
    $(e).animate({opacity: o}, "slow");
}
