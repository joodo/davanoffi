$(document).ready(function() {
    $('#id_music').change(file_field_changed);
    $('#id_image').change(file_field_changed);
});

function file_field_changed() {
    var txt = this.value;
    var field = $(this).parent();
    var name = field.children(".file_name");

    if (name.text() == "") {
        field.animate({
            width: "300px",
            color: "white",
        }, "normal", function () {
            name.text(txt);
        });
    } else {
        name.text(txt);
    }
}
