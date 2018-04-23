"use strict";
$(document).ready(function () {
    $(window).on("load",function() {
        $('.preloader img').fadeOut();
        $('.preloader').fadeOut(1000);
    });
    var textfield = $("input[name=user]");
    $('#index_submit').on('click',function(e) {
        e.preventDefault();
        //little validation just to check username
        if (textfield.val() != "") {
            //$("body").scrollTo("#output");
            $("#output").addClass("alert alert-success animated fadeInUp").html("Welcome back Micheal").removeClass('alert-danger');
            $("input").css({
                "height":"0",
                "padding":"0",
                "margin":"0",
                "opacity":"0"
            });
            //change button text
            $(".locked").addClass("hidden");
            $(".unlocked").removeClass("hidden");
            $('button[type="submit"]').html("CONTINUE")
                .removeClass("btn-primary")
                .addClass("btn-success").on("click",function(){
                window.location.href = 'index';
            });

            //show avatar
            $(".avatar").css({
                "background-image": "url('assets/img/admin.jpg')"
            });
        } else {
            //remove success mesage replaced with error message
            $("#output").removeClass(' alert alert-success').addClass("alert alert-danger animated fadeInUp").html("Sorry Enter Your Password ");
        }
        return false;

    });
});