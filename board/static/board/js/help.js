$(document).ready(function() {
    $("h3").each(function() {
        $("#catalog").append("<a href='#" +
            this.id +
            "'>"+
            this.innerHTML +
            "</a><br/>");
    });
});
