jQuery.event.add(window, 'resize', resize);
jQuery.event.add(window, 'load', init);
jQuery.event.add(window, 'unload', leave);

//Current page = loc
var loc;
var isMobile = false;
var isIE = false;
var fadeDelay = 600;
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
        opacity: 0
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
    if (loc == '/') {
        var id = '#home';
    }
    else {
        var id = '#' + loc.replace('/', '');
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
        $('.center').stop().animate({
            opacity: 1
        }, fadeDelay);
        init();
    });
}

function submitContactForm() {
    $('#form-feedback > h2').html('');
    if($('#name').val() == '' || $('#name').val().search(/[ ]+/g) == 0) {
        $('#name').focus();
        $('#form-feedback > h2').html('A name is a required...<br/>I need to call you something other than friend.');
    } else if($('#email').val() == '') {
        $('#email').focus();
        $('#form-feedback > h2').html('An email address is required...<br/>I need to be able to respond to you.');
    } else if($('#email').val().split('@').length < 2) {
        $('#email').focus();
        $('#form-feedback > h2').html('Sorry but that email is not valid...');
    } else if($('#email').val().split('@')[1].split('.').length < 2) {
        $('#email').focus();
        $('#form-feedback > h2').html('Sorry but that email is not valid...');
    } else if($('#comments').val() == '' || $('#comments').val() == 'Message*') {
        $('#comment').focus();
        $('#form-feedback > h2').html("A message is required...<br/>I need to know what I'll be helping you with.");
    } else {
        $('#send').trigger('mouseover');
        $('#send').unbind();
        $.post('/submit-contact-form', $('#contact-form-id').serialize(), function(data) {
            $('#form-feedback > h2').text(data);
        });
    }
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
    var diff = 10;
    if ($('.right').height() + diff > $('#main').height()) {
        if (isIE) 
            $('#main').height($('.right').height() + diff + 25);
        else 
            $('#main').height($('.right').height() + diff);
    }
    $('#nav').height($('div.right').height() - 290);
}

function smoothScroll(){
	var pos = $(document).scrollTop();
	var delta = 100;
    if (pos > 179) {
        window.setTimeout(function(){
			if (pos - delta < 179){
				delta = pos - 179;
			}
			$(document).scrollTop(pos - delta);
			window.setTimeout("smoothScroll();", 10);
		}, 20);
    }
}

function init(){
    resize();
    if (isIE) {
        if (!navigator.userAgent.match('MSIE 9.0')) {
            $('#image-banner').width(1000);
        }
        //		if (jQuery.browser.msie.version) {
        $('.gradient-gray').removeClass('gradient-gray');
        $('#footer').removeClass('gradient-gray');
        $('.gradient-body').removeClass('gradient-body');
        $('body').add('div').addClass('ie');
		//Contact page stuff
		$('#name').val('Name*');
        $('#name').bind('focus', function() {
            if($(this).val() == 'Name*')
                $(this).val('');
        });
        $('#name').bind('blur', function() {
            if($(this).val() == '')
                $(this).val('Name*');
        });
        $('#email').val('Email*');
        $('#email').bind('focus', function() {
            if($(this).val() == 'Email*')
                $(this).val('');
        });
        $('#email').bind('blur', function() {
            if($(this).val() == '')
                $(this).val('Email*');
        });
        $('#telephone').val('Phone');
        $('#telephone').bind('focus', function() {
            if($(this).val() == 'Phone')
                $(this).val('');
        });
        $('#telephone').bind('blur', function() {
            if($(this).val() == '')
                $(this).val('Phone');
        });
        $('#comments').bind('blur', function() {
            if($(this).val() == '')
                $(this).val('Message*');
        });
    }
	$('#send').click(function() {
        submitContactForm();
    });
    $('input').add('#comments').blur(function() {
        if($(this).val().search(/^[ \t]+/g) == 0)
            $(this).val($(this).val().replace(/^[ \t]+/g, ''));
    });
    $('#contact-form-id').submit(function() {
        submitContactForm();
    });
    $('#comments').val('Message*');
    $('#comments').bind('focus', function() {
        if($(this).val() == 'Message*')
            $(this).val('');
    });
    var sendTrans = 250;
    $('#send').bind('mouseover', function() {
        $('#send > img:first').stop().animate({
            opacity : 0
        }, sendTrans);
        $('#send > img:last').stop().animate({
            opacity : 1
        }, sendTrans);
    });
    $('#send').bind('mouseleave', function() {
        $('#send > img:first').stop().animate({
            opacity : 1
        }, sendTrans);
        $('#send > img:last').stop().animate({
            opacity : 0
        }, sendTrans);
    });
    //Current page = loc
    loc = window.location + "";
    loc = loc.split('/');
    loc = loc[loc.length - 1];
    if (loc == '') {
        var id = '#home';
    }
    else {
        var id = '#' + loc;
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
            if ($(this).attr('class') == 'bottom-link') {
                smoothScroll();
            }
        }
        else {
            window.location.href = nextPage;
        }
        window.setTimeout(function(){
            animateIn(nextPage);
        }, fadeDelay / 1.5);
    });
    watchURLChange();
}
