"use strict";
$(document).ready(function() {
    $(window).on("load",function() {
        $('.preloader img').fadeOut();
        $('.preloader').fadeOut(1000);
    });
    function move404() {
        $('#animate').animate({ 'left': '+=10%' }, 3500).delay(100)
            .animate({ 'left': '-=10%' }, 3500, function() {
                setTimeout(move404, 1000);
            });
    }
    move404();
});
