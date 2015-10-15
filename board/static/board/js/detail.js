function buttonClicked(e) {
    if (e.innerHTML == "回应…") {
        e.innerHTML = "好了。"
        $("#form_fields").slideDown();
    } else {
        onSubmit();
    }
}
