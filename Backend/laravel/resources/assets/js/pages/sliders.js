'use strict';
$(document).ready(function () {
    $("#example_1").ionRangeSlider({
        min: 0,
        max: 5000,
        type: 'double',
        prefix: "$",
        maxPostfix: "+",
        prettify: false,
        hasGrid: true
    });
    $("#example_2").ionRangeSlider({
        min: 1000,
        max: 100000,
        from: 30000,
        to: 90000,
        type: 'double',
        step: 500,
        postfix: " &euro;",
        hasGrid: true
    });
    $("#example_3").ionRangeSlider({
        min: 0,
        max: 10,
        type: 'single',
        step: 0.1,
        postfix: " carats",
        prettify: false,
        hasGrid: true
    });
    $("#example_4").ionRangeSlider({
        min: -50,
        max: 50,
        from: 0,
        type: 'single',
        step: 1,
        postfix: "°",
        prettify: false,
        hasGrid: true
    });
    $("#example_5").ionRangeSlider({
        values: [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"
        ],
        type: 'single',
        hasGrid: true
    });
    $("#example_6").ionRangeSlider({
        min: 10000,
        max: 100000,
        step: 100,
        postfix: " light years",
        type:'double',
        from: 55000,
        to:65000,
        hideMinMax: false,
        hideFromTo: true
    });
    $("#example_7").ionRangeSlider({
        min: 10000,
        max: 100000,
        step: 100,
        postfix: " light years",
        from: 55000,
        hideMinMax: true,
        hideFromTo: false
    });

    // Bootstrap slider
    $('#ex1Slider').slider({
        formater: function(value) {
            return 'Current value: ' + value;
        }
    });

    /* Example 2 */
    $("#bootstrap_slider2").slider({});

    /* Example 3 */
    var RGBChange = function() {
        $('#RGB_color').css('background', 'rgb(' + r.getValue() + ',' + g.getValue() + ',' + b.getValue() + ')')
    };

    var r = $('#red').slider()
        .on('slide', RGBChange)
        .data('slider');
    var g = $('#green').slider()
        .on('slide', RGBChange)
        .data('slider');
    var b = $('#blue').slider()
        .on('slide', RGBChange)
        .data('slider');
    /* Example 5 */
    $("#bootstrap_slider5").slider();
    $("#destroyEx5Slider").on("click",function() {
        $("#bootstrap_slider5").slider('destroy');
    });

    /* Example 6 */
    $("#bootstrap_slider6").slider();
    $("#bootstrap_slider6").on('slide', function(slideEvt) {
        $("#ex6SliderVal").text(slideEvt.value);
    });

    /* Example 7 */
    $("#bootstrap_slider7").slider();
    $("#ex7-enabled").on("click",function() {
        if (this.checked) {
            $("#bootstrap_slider7").slider("enable");
            $("#enable_text").text('Disable');
            $("#slider_enabled").text('Enabled Slider');
        } else {
            $("#bootstrap_slider7").slider("disable");
            $("#enable_text").text('Enable');
            $("#slider_enabled").text('Disabled Slider');
        }
    });

    /* Example 8 */
    $("#bootstrap_slider8").slider({
        tooltip: 'always'
    });

    /* Example 9 */
    $("#bootstrap_slider9").slider({
        step: 0.01,
        value: 8.115
    });
    $("#bootstrap_slider10").slider();
    $(".slider").on("mouseenter mouseleave",function(){
        $(this).find(".tooltip.tooltip-main").toggleClass("show").removeClass("in");
    });
});