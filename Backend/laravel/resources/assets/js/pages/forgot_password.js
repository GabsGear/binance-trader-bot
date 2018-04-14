"use stict";
$(document).ready(function(){
    new WOW().init();
    $('#login_validator1').bootstrapValidator({
        fields: {
            email_modal: {
                validators: {
                    notEmpty: {
                        message: 'enter your valid email'
                    },
                    regexp: {
                        regexp: /^\S+@\S{1,}\.\S{1,}$/,
                        message: 'The input is not a valid email address'
                    }
                }
            }
        }
    });
    validate();
    function validate() {
        if ($('.email_forgot').val() > 0) {
            $(".submit_email").prop("disabled", false);
        } else {
            $(".submit_email").prop("disabled", true);
        }
    }
});