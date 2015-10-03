window.onload = function () {
    var from = document.referrer;
    /*if (from.indexOf("joodo.chinacloudsites.cn/ilove.html") < 0) {
        window.location.href = "http://joodo.chinacloudsites.cn/ilove.html"
    }*/
    $("#content").css("top", $(window).width() * 1.8 + "px");

	$(document).ready(function () {
		$("#mask").height($(document).height())
		$("#mask").fadeOut(3500, function () {
			alert("拥抱我。");
		});
	})
}
