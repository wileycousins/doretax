jQuery.event.add(window, 'resize', resize);
jQuery.event.add(window, 'load', init);
jQuery.event.add(window, 'unload', leave);

//Current page = loc
var loc;
var isMobile = false;
var fadeDelay = 600;
var changing = false;

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
        $('.center').stop().animate({
            opacity: 0
        }, fadeDelay);
    }, 10);
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
            $('.center').stop().animate({
                opacity: 0
            }, fadeDelay);
            window.setTimeout(function(){
                $.get('/get/' + tmploc, function(data){
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
            }, fadeDelay);
        }
        else {
            window.setTimeout("watchURLChange();", 80);
        }
    }
}

function resize(){
    $('#nav').height($('div.right').height() - 20);
}

function init(){
    resize();
    //Current page = loc
    loc = window.location + "";
    loc = loc.split('/');
    loc = loc[loc.length - 1];
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
            $.get('/get' + nextPage, function(data){
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
            },'getting a page');
        }, fadeDelay);
    });
    watchURLChange();
}
