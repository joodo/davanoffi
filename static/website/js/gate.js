var size;
var selectedColor;

$(document).ready(function () {
    ajaxInit();

    $("#mask").hide();

    w = window.innerWidth;
    h = window.innerHeight;

    var img = new Image();
    img.src = img_src;
    img.onload = function () {
        var c = document.getElementById("canvas");
        c.width = img.width;
        c.height = img.height;
        c.getContext("2d").drawImage(img, 0, 0, img.width, img.height);

        paintBucketApp.init(c);
    }
});

function ajaxInit() {
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
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function colorSelected(color) {
    if (selectedColor == color) {
        return;
    }
    if (selectedColor != null) {
        selectedColor.style.borderColor = "black";
    }
    selectedColor = color;
    //color.style.borderColor = color.style.backgroundColor;

    var regexp = /[0-9]{0,3}/g;
    var re = color.style.backgroundColor.match(regexp);
    for(var i=0;i<re.length;i++){
        if(re[i]==""){
            re.splice(i,1);
            i--;
        }
    }

    paintBucketApp.setColor(parseInt(re[0]), parseInt(re[1]), parseInt(re[2]));
}

function fillColor(event) {
    var mouseX = event.pageX - document.getElementById("canvas").offsetLeft
        mouseY = event.pageY - document.getElementById("canvas").offsetTop
    paintBucketApp.paintAt(mouseX, mouseY);
}

function mouseover(div) {
    div.style.borderColor = "white";
}

function mouseout(div) {
    if (selectedColor !== div) {
        div.style.borderColor = "black";
    }
}

function musicswitch()
{
    var t = document.getElementById("bgmusic");

    if (t.paused)
    {
        t.play();
    }
    else
    {
        t.pause();
    }
}

function setCookie(c_name,value,expiredays)
{
	var exdate=new Date()
	exdate.setDate(exdate.getDate()+expiredays)
	document.cookie=c_name+ "=" +escape(value)+
	((expiredays==null) ? "" : ";expires="+exdate.toGMTString())+"; path=/";
}
