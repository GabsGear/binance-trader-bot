"use strict";
$(document).ready(function () {
    // fixed header
    var top = $("#top");
    function scroll_fixtop() {
        var rightHeightTop=$(window).height() - top.height();
        $(".request_scrollable").css("height", rightHeightTop)
    }
    scroll_fixtop();
    $(window).on("resize",function () {
        scroll_fixtop();
    });
        // Fixed menu
        function fixed_menu_scroll() {
            if($("body").hasClass("fixedNav_position")){
                var leftHeight=$(window).height()-$("#top").height();
                $('.left_scrolled').css("height",leftHeight);
                $('.left_scrolled').jScrollPane({
                    autoReinitialise: true,
                    autoReinitialiseDelay: 100
                });
            }else{
                var leftHeight=$(window).height();
                $('.left_scrolled').css("height",leftHeight);
                $('.left_scrolled').jScrollPane({
                    autoReinitialise: true,
                    autoReinitialiseDelay: 100
                });
            }
        }
        fixed_menu_scroll();
        $(window).on("resize", function () {
            fixed_menu_scroll();
        });
});