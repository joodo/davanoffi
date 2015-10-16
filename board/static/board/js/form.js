$(document).ready(function() {
    $('#id_music').change(fileFieldChanged);
    $('#id_image').change(fileFieldChanged);
    $(".clear_button").click(clearField);
});

function fileFieldChanged() {
    var txt = this.value;
    var field = $(this).parent();
    var name = field.children(".file_name");

    if (txt == "") {
        field.animate({
            width: "40px",
            color: "#808080",
        }, "normal", function () {
            name.text(txt);
        });
    } else {
        if (name.text() == "") {
            field.animate({
                width: "400px",
                color: "white",
            }, "normal", function () {
                name.text(txt);
            });
        } else {
            name.text(txt);
        }
    }
}

function clearField() {
    input = $(this).parent().children("input");
    input.val("");
    input.change();
}
