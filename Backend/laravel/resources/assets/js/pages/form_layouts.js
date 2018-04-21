'use strict';
$(document).ready(function() {
    $(".signin_radio1").on("click", function() {
        $(".form_lay_email1").html("Username ");
        $(".user_icon_change1 .fa-envelope").replaceWith('<i class="fa fa-user"></i>');
        $(".form_lay_input1").replaceWith('<input type="text" class="form-control form_lay_input1" name="Username" placeholder="Username">')
    });
    $(".signin_radio2").on("click", function() {
        $(".form_lay_email1").html("E-mail");
        $(".user_icon_change1 .fa-user").replaceWith('<i class="fa fa-envelope"></i>');
        $(".form_lay_input1").replaceWith('<input type="text" class="form-control form_lay_input1" name="Email" placeholder="E-mail">')
    });
    $(".signin_radio3").on("click", function() {
        $(".form_lay_email2").html("Username ");
        $(".user_icon_change2 .fa-envelope").replaceWith('<i class="fa fa-user"></i>');
        $(".form_lay_input2").replaceWith('<input type="text" class="form-control form_lay_input2" name="username" placeholder="Username">')
    });
    $(".signin_radio4").on("click", function() {
        $(".form_lay_email2").html("E-mail");
        $(".user_icon_change2 .fa-user").replaceWith('<i class="fa fa-envelope"></i>');
        $(".form_lay_input2").replaceWith('<input type="text" class="form-control form_lay_input2" name="email" placeholder="E-mail">')
    });
    $(".layout_btn_prevent").on("click", function(e) {
        e.preventDefault();
    });
    $("#otp_validation").bootstrapValidator({
        fields: {
            digits_only: {
                validators: {
                    notEmpty: {
                        message: 'Enter digits only'
                    },
                    regexp: {
                        regexp: /^\d{10}$/,
                        message: 'Enter a 10 digits number'
                    }
                }
            }

        }
    });
    if ($('#onetime_password').val().length > 0) {
        $("#confirm_tel").prop("disabled", false);
    } else {
        $("#confirm_tel").prop("disabled", true);
    }
    $("#onetime_password").intlTelInput({
        utilsScript: "assets/vendors/intl-tel-input/js/utils.js"
    });
    $('#confirm_tel').on('click', function(e) {
        e.preventDefault();
        swal.queue([{
            title: 'OTP Notification',
            confirmButtonText: 'Show my OTP',
            currentProgressStep: 0,
            showLoaderOnConfirm: true,
            preConfirm: function() {
                return new Promise(function(resolve) {
                    swal.insertQueueStep("4568");
                    resolve();
                });
            }
        }]).done();
    });
});
