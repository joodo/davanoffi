$(document).ready(function() {
    $("div.content").each(function() {
        $("#catalog").append("<a href='#' div_id='"+
			this.id+
			"'>"+
            $(this).attr("title") +
            "</a><br/>");
    });

	$("#catalog a").click(titleClicked);
});

function titleClicked() {
	if ($(this).hasClass("actived")) {
		return;
	}

	$(".content").hide();
	$("#catalog a").removeClass("actived");

	div_id = $(this).attr("div_id");
	$("#"+div_id).show();
	$(this).addClass("actived");
}
