$(document).ready(function() {
    $('#id_music').change(fileFieldChanged);
    $('#id_image').change(fileFieldChanged);
    $(".clear_button").click(clearField);
    $("#progress_mask").hide();
});

function fileFieldChanged() {
    var txt = this.value;
    var field = $(this).parent();
    var name = field.children(".file_name");

    if (txt == "") {
        field.animate({
            width: "40px",
            color: "#808080",
                borderTopColor: "#808080",
                borderBottomColor: "#808080",
                borderLeftColor: "#808080",
                borderRightColor: "#808080",
        }, "normal", function () {
            name.text(txt);
        });
    } else {
        if (name.text() == "") {
            field.animate({
                width: "400px",
                color: "white",
                borderTopColor: "white",
                borderBottomColor: "white",
                borderLeftColor: "white",
                borderRightColor: "white",
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

function onSubmit() {
    if ($("#id_content").val()=="" && $("#id_title").val()=="") {
        alert("写点什么？");
        return;
    }

    if ($("#id_image").val()=="" && $("#id_music").val()=="") {
        $("form").submit();
    } else {
        ajaxSubmit();
    }
}

function ajaxSubmit() {
    progressBarInit();

    var formData = new FormData($("form")[0]);
    $.ajax({
        url: ".",
        type: 'POST',
        xhr: function() {  // custom xhr
            myXhr = $.ajaxSettings.xhr();
            if(myXhr.upload){ // check if upload property exists
                myXhr.upload.addEventListener('progress',progressHandlingFunction, false); // for handling the progress of the upload
            }
            else {
                alert("myXhr:"+myXhr)
            }
            return myXhr;
        },
        success: completeHandler,
        //beforeSend: beforeSendHandler,
        //error: errorHandler,
        data: formData,
        // Options to tell JQuery not to process data or worry about content-type
        cache: false,
        contentType: false,
        processData: false
    });
}

var suit_count, suit_total
function progressBarInit() {
    console.log("dsdsds")
    $("#progress_mask").fadeIn();

    var bar_width = $("#suits").width();
    suit_total = parseInt(bar_width / 30) - 2;
    suit_count = 1;
    var start_x = (bar_width - suit_total * 30) / 2 + 30;

    $("#suits").css("paddingLeft", parseInt(start_x) + "px");
}

function completeHandler() {
    suit_count++;

    var src = image_url + "suit" + (suit_count%4+1) +".png";
    var ele = $("<img src='" + src + "' style='display:none; width:30px;' />");

    $("#suits").append(ele);
    ele.fadeIn(2500, function(){
        window.location.href = success_url;
    });
}

function progressHandlingFunction(e){
    if(e.lengthComputable){
        while (parseInt(e.loaded * suit_total / e.total) > suit_count) {
            suit_count++;
            //alert("" + e.loaded + e.total + suit_total)

            var src = image_url + "suit" + (suit_count%4+1) +".png";
            var ele = $("<img src='" + src + "' style='display:none; width:30px;' />");

            $("#suits").append(ele);
            ele.fadeIn(1000);
        }
    }
    else {
        alert("e:"+e);
    }
}

function onLoad() {
}

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
