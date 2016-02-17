function buttonClicked(e) {
    if (e.innerHTML == "回应…") {
        e.innerHTML = "好了。"
        $("#form_fields").slideDown();
        $("#field_toggle").show("normal");
    } else {
        onSubmit();
    }
}

$(document).ready(function() {
    $("textarea").attr("placeholder", "你的回应。");
})
