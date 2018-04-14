'use strict';
$(document).ready(function() {
    new WOW().init();
    $(window).on("load",function() {
        $('.preloader img').fadeOut();
        $('.preloader').fadeOut(1000);
    });
    $('#register_valid').bootstrapValidator({
        fields: {
            UserName: {
                validators: {
                    notEmpty: {
                        message: 'The user name is required and cannot be empty'
                    }
                }
            },
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
            },
            confirmpassword: {
                validators: {
                    notEmpty: {
                        message: 'The confirm password is required and can\'t be empty'
                    },
                    identical: {
                        field: 'password',
                        message: 'Please enter the same password as above'
                    }
                }
            },
            phone: {
                validators: {
                    notEmpty: {
                        message: 'Please enter valid phone number'
                    },
                    regexp: {
                        regexp: /^[0-9]{10}$/,
                        message: 'The phone number can only consist of numbers with 10 digits'
                    }
                }
            },
            check: {
                validators: {
                    notEmpty: {
                        message: 'Check on the field'
                    }
                }
            }
        }
    });
});