function postMouseOver(e) {
    $(e).find("div.detail_link").show();
}

function postMouseLeave(e) {
    $(e).find("div.detail_link").hide();
}

function opacityChange(e, o) {
    $(e).stop(true);
    $(e).animate({opacity: o}, "slow");
}
