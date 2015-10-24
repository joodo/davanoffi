$(document).ready(function () {
    $("li.post").mouseover(postMouseOver);
    $("li.post").mouseleave(postMouseLeave);
});

function buttonClicked(e) {
    if (e.innerHTML == "回应…") {
        e.innerHTML = "好了。"
        $("#form_fields").slideDown();
        $("#field_toggle").show("normal");
    } else {
        onSubmit();
    }
}
