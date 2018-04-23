'use strict';
$(document).ready(function () {
    // fontawesome
    $('#icon-search').on("input", function() {
        $(".fa-icon").each(function() {
            var regex = new RegExp($("#icon-search").val().trim().toLowerCase());
            var x = $(this).clone().children().remove().end().text();
            var res = x.match(regex, "i");
            if (res == null) {
                $(this).hide();
            } else {
                $(this).show();
            }
        });
        return false;
    });

    // Themify icons
    $('#icon-search2').on("input", function() {
        $(".themify_icon").each(function() {
            var regex = new RegExp($("#icon-search2").val().trim().toLowerCase());
            var y = $(this).clone().children().remove().end().text();
            var res = y.match(regex, "i");
            if (res == null) {
                $(this).hide();
            } else {
                $(this).show();
            }
        });
        return false;
    });

    // Glyph icons
    $('#icon-search3').on("input", function() {
        $(".ion_icon").each(function() {
            var regex = new RegExp($("#icon-search3").val().trim().toLowerCase());
            var z = $(this).clone().children().remove().end().text();
            var res = z.match(regex, "i");
            if (res == null) {
                $(this).hide();
            } else {
                $(this).show();
            }
        });
    });
    return false;
});