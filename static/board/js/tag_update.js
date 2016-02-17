$(document).ready(function() {
    $("#save").click(function() {
        console.log("sss");
        $("form").submit();
    });
    $("#cancle").click(function() {
        history.go(-1);
    })
    $("input[type='color']").change(colorChanged);

    colorChanged();
});

function colorChanged() {
    loadColor($("#id_background_color").val(),
            $("#id_content_text_color").val(),
            $("#id_title_text_color").val(),
            $("#id_anchor_text_color").val());
}
