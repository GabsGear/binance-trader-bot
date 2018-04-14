"use strict";
$(document).ready(function() {
    // swiper
    var swiper = new Swiper('.widget_swiper', {
        centeredSlides: true,
        autoplay: 2000,
        loop: true,
        autoplayDisableOnInteraction: false


    });
    var swiper2 = new Swiper('.widget_swiper2', {
        autoplay: 2000,
        loop: true,
        slidesPerView: 3,
        spaceBetween: 10,
        autoplayDisableOnInteraction: false
    });
    // End of swiper

    $(".wrapper").on("resize", function() {
        setTimeout(function() {
            swiper.update();
            swiper2.update();
        }, 400);
    });

    // Default time
    var timenow = moment().format("h:mm");

    $(".conversation-list").slimscroll({
        height: "360px",
        size: '5px',
        opacity: 0.2
    });
    // End of default time

    // Chat
    $("form#main_input_box").on("submit",function(event) {
        event.preventDefault();
        var scrollTo_int = $(".conversation-list").prop('scrollHeight') + 'px';
        $(".conversation-list").append('<li class="clearfix odd m-t-25"><div class="chat-avatar"><img src="img/widget_image3.jpg" alt="male"><i>' + timenow + '</i></div><div class="conversation-text"><div class="ctext-wrap"><i>Me</i><p>' + $("#custom_textbox").val() + '</p></div></div></li>');
        $("#custom_textbox").val('');
        $(".conversation-list").slimscroll({ scrollTo: scrollTo_int });
    });
    // End of chat

    var options = {
        useEasing: true,
        useGrouping: true,
        decimal: '.',
        prefix: '',
        suffix: ''
    };
    new CountUp("widget_count1", 0, 2436, 0, 2.5, options).start();
    new CountUp("widget_count2", 0, 8569, 0, 2.5, options).start();
    new CountUp("widget_count3", 0, 4859, 0, 2.5, options).start();
    new CountUp("widget_count4", 0, 32568, 0, 2.5, options).start();
    new CountUp("fb_count", 0, 60, 0, 2.5, options).start();
    new CountUp("twitter_count", 0, 25, 0, 2.5, options).start();
    new CountUp("gplus_count", 0, 15, 0, 2.5, options).start();
    new CountUp("followers_count", 0, 962, 0, 2.5, options).start();
    new CountUp("comments_count", 0, 649, 0, 2.5, options).start();
    new CountUp("likes_count", 0, 4236, 0, 2.5, options).start();
    $(".custom_textbox").on("keypress", function(e) {
        if (e.which === 32 && !this.value.length)
            e.preventDefault();
    });


});
