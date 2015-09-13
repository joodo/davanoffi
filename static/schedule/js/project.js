var timer

function tick() {
	var s = parseInt($('#workSecond').val()) + 1
	if (s < 60) {
		$('#workSecond').val( s<10 ? "0"+s : s)
		return;
	}
	
	$('#workSecond').val("00")
	var m = parseInt($('#workMinute').val()) + 1
	if (m === 60 || m === 30) {
		$('#beep')[0].play()
	}
	if (m < 60) {
		$('#workMinute').val( m<10 ? "0"+m : m)
		return;
	}
	
	$('#workMinute').val("00")
	var h = parseInt($('#workHour').val()) + 1
	$('#workHour').val( h<10 ? "0"+h : h)
}