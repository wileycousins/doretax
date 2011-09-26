jQuery.event.add(window, 'resize', resize);
jQuery.event.add(window, 'load', init);
jQuery.event.add(window, 'unload', leave);

//Current page = loc
var loc;
var isMobile = false;
var isIE = false;
var fadeDelay = 1500;
var changing = false;

//Checking for mobile browser
if (navigator.userAgent.match(/Android/i) ||
navigator.userAgent.match(/webOS/i) ||
navigator.userAgent.match(/iPhone/i) ||
navigator.userAgent.match(/iPod/i)) {
    isMobile = true;
}

if (jQuery.browser.msie) {
    isIE = true;
}

function animateOut(){
    $('#main').css('overflow', 'hidden');
    $('.center').stop().animate({
        left: 3000
    }, fadeDelay);
}

function leave(event){
    event.preventDefault();
    window.setTimeout(function(){
        animateOut();
    }, 10);
}

function animateIn(loc){
	$('.current-page').removeClass('current-page');
	if(loc == '/'){
        var id = '#home';
    }
    else{
		var id = '#'+loc.replace('/','');
    }
	$(id).children().addClass('current-page');
    $.get('/get' + loc, function(data){
        var title = $($(data)[0]).text();
        $('title').text(title);
        var html = '';
        data = $(data);
        for (var i = 0; i < $(data).length; i++) {
            var id = $(data[i]).attr('id');
            if (id == 'content') {
                html += $(data[i]).html();
            }
        }
        $('.center').html(html);
        $('.center').css('left', -2000);
        $('.center').stop().animate({
            left: 0
        }, fadeDelay);
        window.setTimeout("$('#main').css('overflow','visible');", fadeDelay);
        init();
    });
}

function watchURLChange(){
    var tmploc = window.location + "";
    tmploc = tmploc.split('/');
    tmploc = tmploc[tmploc.length - 1];
    if (changing) {
        window.setTimeout("watchURLChange();", fadeDelay * 5);
    }
    else {
        if (loc !== tmploc) {
            animateOut();
            window.setTimeout(function(){
                animateIn('/' + tmploc);
            }, fadeDelay);
        }
        else {
            window.setTimeout("watchURLChange();", 80);
        }
    }
}

function resize(){
	if($('.right').height() + 225 > $('#main').height()){
	   if(isIE)
		  $('#main').height($('.right').height() + 250);
	   else
	      $('#main').height($('.right').height() + 225);
	}
    $('#nav').height($('div.right').height() - 20);
}

function init(){
    resize();
    if (isIE) {
		if(!navigator.userAgent.match('MSIE 9.0')){
			$('#image-banner').width(1000);
		}
//		if (jQuery.browser.msie.version) {
        $('.gradient-gray').removeClass('gradient-gray');
		$('#footer').removeClass('gradient-gray');
        $('.gradient-body').removeClass('gradient-body');
        $('body').add('div').addClass('ie');
    }
    //Current page = loc
    loc = window.location + "";
    loc = loc.split('/');
    loc = loc[loc.length - 1];
	if(loc == ''){
		var id = '#home';
	}
	else{
		var id = '#'+loc;
	}
	$(id).children().addClass('current-page');
    $('a:not(.no-link)').unbind('click');
    $('a:not(.no-link)').bind('click', function(event){
        changing = true;
        window.setTimeout("changing = false;", fadeDelay * 3);
        leave(event);
        nextPage = $(this).attr('href');
        if (nextPage == '') {
            nextPage = 'home';
        }
        if (Modernizr.history) {
            var stateObject = nextPage;
            window.history.pushState(stateObject, "Dor&eacute; Tax", nextPage);
        }
        else {
            window.location.href = nextPage;
        }
        window.setTimeout(function(){
            animateIn(nextPage);
        }, fadeDelay / 3);
    });
    watchURLChange();
}
