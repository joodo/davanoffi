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

function onSubmit(type) {
	if (type == "text") {
		$("#text_content").val($("#text_content").val().replace(/<[^>]+>/g,""))
		if ($("#text_content").val() == "") {
			alert("说点什么吧。")
			return
		}

		$("#text").submit()
		return;
	}
	
	if ($("#"+type+" [name=content]").val() == "") {
		alert("传点什么吧。")
		return
	}
	
	progressBarInit()
	
	var formData = new FormData($("#"+type)[0]);
	
	$.ajax({
		url: post_url,  //server script to process data
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
		// Ajax�¼�
		success: completeHandler,
		//beforeSend: beforeSendHandler,
		//error: errorHandler,
		// Form����
		data: formData,
		// Options to tell JQuery not to process data or worry about content-type
		cache: false,
		contentType: false,
		processData: false
	});
}

var suit_count, suit_total
function progressBarInit() {
	$("#progress_mask").fadeIn()
	
	var bar_width = $("#suits").width()
	suit_total = parseInt(bar_width / 30) - 2
	suit_count = 1
	var start_x = (bar_width - suit_total * 30) / 2 + 30
	
	$("#suits").css("paddingLeft", parseInt(start_x) + "px")
}

function completeHandler() {
	suit_count++;
	
	var src = "/static/blog/img/suit" + (suit_count%4+1) +".png"
	var ele = $("<img src='" + src + "' style='display:none; width:30px;' />")
	
	$("#suits").append(ele)
	ele.fadeIn(2500, function(){
		window.location.href = index_url
	})
}

function progressHandlingFunction(e){
	if(e.lengthComputable){
		while (parseInt(e.loaded * suit_total / e.total) > suit_count) {
			suit_count++;
			//alert("" + e.loaded + e.total + suit_total)
			
			var src = "/static/blog/img/suit" + (suit_count%4+1) +".png"
			var ele = $("<img src='" + src + "' style='display:none; width:30px;' />")
			
			$("#suits").append(ele)
			ele.fadeIn(1000)
		}
	}
	else {
		alert("e:"+e)
	}
}

var current_form

function onLoad() {
	onResize()
	
	current_form = $("form#text")
	$("#progress_mask").hide()
}

function onResize() {
	$(".wrap").height($(window).height())
}

function onTypeChange(type) {
	if (current_form !== $("form#" + type)) {
		current_form.hide()
		current_form = $("form#" + type)
		current_form.show()
	}
}
