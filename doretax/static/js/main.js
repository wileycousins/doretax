jQuery.event.add(window, 'resize', resize);
jQuery.event.add(window, 'load', init);
jQuery.event.add(window, 'unload', leave);

//Current page = loc
var loc;
var isMobile = false;
var fadeDelay = 300;

//Checking for mobile browser
if (navigator.userAgent.match(/Android/i) ||
navigator.userAgent.match(/webOS/i) ||
navigator.userAgent.match(/iPhone/i) ||
navigator.userAgent.match(/iPod/i)) {
    isMobile = true;
}

function leave(event){
    event.preventDefault();
    window.setTimeout(function(){
        $('.center').animate({
            opacity: 0
        }, fadeDelay);
    }, 10);
}

function init(){
    resize();
    //Current page = loc
    loc = window.location + "";
    loc = loc.split('/');
    loc = loc[loc.length - 1];
    $('a:not(.no-link)').unbind('click');
    $('a:not(.no-link)').bind('click', function(event){
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
        window.setTimeout(function(data){
            $.get(nextPage, function(data){
				var title = $('title').text();
				title = title.split('|');
				console.log(title[0]+title[1]);
				title[0] = $(data).find('#hidden-title').text();
				$('title').text(title[0]+title[1]);
                $('.center').html($(data).find('.center').html());
                $('.center').animate({
                    opacity: 1
                }, fadeDelay);
				init();
            });
        }, fadeDelay);
    });
}

function resize(){
    $('#nav').height($('div.right').height() - 20);
}
