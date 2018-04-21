"use strict";
$(document).ready(function(){
    $(window).on("load",function() {
        $('.preloader img').fadeOut();
        $('.preloader').fadeOut(1000);
    });
    $(".unlock").on("click",function () {
        $(".lock_show").show();
        $(".unlock").hide();
    });
    $(".lock_background3").backstretch([
        "assets/img/login2.png"
        , "assets/img/login13.jpg"
        , "assets/img/login10.png"
    ], {duration: 3000, fade: 750});
    $("#lockscreen_validator").bootstrapValidator({
        fields: {
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