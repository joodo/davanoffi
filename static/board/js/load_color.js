function loadColor(background, content, title, anchor) {
    background = background || "#101010";
    content = content || "white";
    title = title || "#808080";
    anchor = anchor || "cadetblue";

    $("a").css("color", anchor);

    $("body, .detail_link div").css("background-color", background);

    $("body, .content, textarea, input").css("color", content);
    $(".button").css("border-color", content);

    $("li, .tag, .paginator a, .file_upload").css("color", title);
    $(".segment, textarea, input, .file_upload, .header").css("border-color", title);

    $(".paginator a").hover(function() {
        $(this).css("color", content);
    }, function() {
        $(this).css("color", title);
    });
    $(".button, .clear_button").hover(function() {
        $(this).css("color", background);
        $(this).css("background-color", content);
    }, function() {
        $(this).css("color", content);
        $(this).css("background-color", background);
    });
    $("textarea, input").focus(function() {
        $(this).css("border-color", content);
    });
    $("textarea, input").blur(function() {
        $(this).css("border-color", title);
    });
}
