$(document).ready(function() {
    $('#id_music').change(file_field_changed);
    $('#id_image').change(file_field_changed);
});

function file_field_changed() {
    var field = $(this).parent();
    var name = field.children(".file_name");

    if (name.text() == "") {
        field.animate({
            width: "300px",
            color: "white",
        }, "normal", function () {
            alert('dfs')
            name.text(this.value);
        });
    } else {
        name.text(this.value);
    }
}
