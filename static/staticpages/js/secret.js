var size;
var selectedColor;

$(document).ready(function () {
    $("#mask").hide();

    w = window.innerWidth;
    h = window.innerHeight;

    var c = document.getElementById("canvas");
    size = w < h ? w : h;
    c.width = size;
    c.height = size;

    var cxt = c.getContext("2d");
    var img = new Image();
    img.src = "/static/staticpages/img/owl.png";
	//alert(img.src)
    img.onload = function () {
        cxt.drawImage(img, 0, 0, size, size);

        paintBucketApp.init(c);
    }
});

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
    var mouseX = event.pageX - document.getElementById("canvas").offsetLeft,
        mouseY = event.pageY - document.getElementById("canvas").offsetTop;
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
