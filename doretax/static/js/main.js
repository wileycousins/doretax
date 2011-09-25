jQuery.event.add(window, 'resize', resize);
jQuery.event.add(window, 'load', init);

//Current page = loc
var loc;
var isMobile = false;

//Checking for mobile browser
if (navigator.userAgent.match(/Android/i) ||
navigator.userAgent.match(/webOS/i) ||
navigator.userAgent.match(/iPhone/i) ||
navigator.userAgent.match(/iPod/i)) {
    isMobile = true;
}

function init(){
	resize();
    //Current page = loc
    loc = window.location + "";
    loc = loc.split('/');
    loc = loc[loc.length - 1];
}

function resize(){
	$('#nav').height($('div.right').height() - 20);
}
