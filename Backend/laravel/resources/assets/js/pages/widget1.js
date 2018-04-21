"use strict";
$(document).ready(function() {
    var options = {
        useEasing: true,
        useGrouping: true,
        decimal: '.',
        prefix: '',
        suffix: ''
    };
    new CountUp("widget_count5", 0, 1242, 0, 2.5, options).start();
    new CountUp("widget_count6", 0, 254, 0, 2.5, options).start();
    new CountUp("widget_count7", 0, 685, 0, 2.5, options).start();
    new CountUp("widget_count8", 0, 485, 0, 2.5, options).start();
    new CountUp("gold", 0, 330, 0, 2.5, options).start();
    new CountUp("platinum_plan", 0, 400, 0, 2.5, options).start();
    new CountUp("fb_count", 0, 354, 0, 2.5, options).start();
    new CountUp("tw_count", 0, 547, 0, 2.5, options).start();
    new CountUp("g+_count", 0, 678, 0, 2.5, options).start();
    new CountUp("youtube_count", 0, 21, 0, 2.5, options).start();
    new CountUp("sc_count", 0, 845, 0, 2.5, options).start();
    new CountUp("in_count", 0, 124, 0, 2.5, options).start();
    // swiper
    var swiper = new Swiper('.men_shoes_swiper', {
        centeredSlides: true,
        autoplay: 2000,
        loop: true,
        autoplayDisableOnInteraction: false


    });
    var swiper2 = new Swiper('.women_shoes_swiper', {
        centeredSlides: true,
        autoplay: 2500,
        loop: true,
        autoplayDisableOnInteraction: false


    });
    $(".wrapper").on("resize", function() {
        setTimeout(function() {
            swiper.update();
            swiper2.update();
        }, 200);
    });
    // end of swiper

    // default date
    var datetime = null,
        time = null,
        date = null;

    var update = function () {
        date = moment(new Date());
        datetime.html(date.format('DD MMMM YYYY <br> dddd'));
        time.html(date.format('H:mm:ss'));
    };
    //Current Time
    if($('.current-date')[0] && $('.time')[0]) {
        datetime = $('.current-date');
        time = $('.time');

        update();
        setInterval(update, 1000);
    }
    // End of default date

    // login
    $('#widgets_login_validator').bootstrapValidator({
        fields: {
            email: {
                validators: {
                    notEmpty: {
                        message: 'The email address is required'
                    },
                    regexp: {
                        regexp: /^\S+@\S{1,}\.\S{1,}$/,
                        message: 'The input is not a valid email address'
                    }
                }
            },
            password: {
                validators: {
                    notEmpty: {
                        message: 'Please provide a password'
                    }
                }
            }
        }
    });

});
