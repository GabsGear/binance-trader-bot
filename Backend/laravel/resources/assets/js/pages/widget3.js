"use stict";
$(document).ready(function () {
    var options = {
        useEasing: true,
        useGrouping: true,
        decimal: '.',
        prefix: '',
        suffix: ''
    };
    new CountUp("orders_countup", 0, 1425, 0, 5.0, options).start();
    new CountUp("revenue_countup", 0, 600, 0, 5.0, options).start();
    new CountUp("products_countup", 0, 2100, 0, 5.0, options).start();
    new CountUp("sold_countup", 0, 1025, 0, 5.0, options).start();

    var imgHeight=$(".left_align_img").height();
    $(".left_image").css("height",imgHeight);
});