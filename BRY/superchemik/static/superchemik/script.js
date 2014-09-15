
//var parsed = JSON.parse(page_json);
//var page_now = parsed.page_num
//var page_now = '2';

var user_screen_width = screen.width;

$(document).ready(function(){
    if (user_screen_width < 1280) {
        $('img').css('width', '98%');
        $('img').css('height', '98%');
    }
    if (user_screen_width > 1280) {
        $('body').css('width','1270px');
    }

    // page now
    $('#'+page_now).addClass('nav_a_hover');
    
    
    // czytaj komiks / komentarze
    $('.bar a').mouseenter(function(){
            $(this).css('color','black');
        });

    $('.bar a').mouseleave(function(){
            $(this).css('color','white');
        });
    
    
    // wybierz strone
    $('.navigation a').mouseenter(function(){
        $(this).addClass('nav_a_hover');
        });

        
    $('.navigation a').mouseleave(function(){
        if (this.id !== page_now) {
            $(this).addClass('nav_a');
            }
        });
    

    // strona komentarza
    $('.data a').mouseenter(function(){
        $(this).addClass('page_n_hover');
        });

        
    $('.data a').mouseleave(function(){
        $(this).addClass('page_n');
        });
    
    });