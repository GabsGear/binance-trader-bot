'use strict';
$(document).ready(function() {
    $('#popup-validation').validationEngine();
    Admire.formValidation();
    $(".error_color").append('<br/>');
    $(".form_val_popup_dp1").datepicker({
        todayHighlight: true,
        format: 'yyyy-mm-dd',
        autoclose: true
    });
    $(".form_val_popup_dp2").datepicker({
        todayHighlight: true,
        format: 'yyyy-mm-dd',
        autoclose: true
    });
    $('.form_val_popup_dp3').datepicker({
        todayHighlight: true,
        format: 'yyyy-mm-dd',
        autoclose: true
    }).on("changeDate", function() {
        $('#form_block_validator').bootstrapValidator('revalidateField', 'date_inline');
    });
    $('.form_val_popup_dp4').datepicker({
        todayHighlight: true,
        format: 'yyyy-mm-dd',
        autoclose: true
    }).on("changeDate", function() {
        $('#form_inline_validator').bootstrapValidator('revalidateField', 'birthday');
    });
    $(':contains(* Invalid email address)').remove('.formErrorContent');
    $('#form_block_validator').bootstrapValidator({
        fields: {
            Name2: {
                validators: {
                    notEmpty: {
                        message: 'Enter your name'
                    }
                }
            },
            Email2: {
                validators: {
                    regexp: {
                        regexp: /^\S+@\S{1,}\.\S{1,}$/,
                        message: 'The input is not a valid email address.'
                    },
                    notEmpty: {
                        message: 'The email address is required'
                    }
                }
            },
            Password2: {
                validators: {
                    notEmpty: {
                        message: 'Please provide a password'
                    }
                }
            },
            Confirmpassword2: {
                validators: {
                    notEmpty: {
                        message: 'Confirm the password.'
                    },
                    identical: {
                        field: 'Password2',
                        message: 'Please enter the same password as above'
                    }
                }
            },
            date_inline: {
                validators: {
                    notEmpty: {
                        message: 'Date is required and can not be empty'
                    }
                }
            },
            Url2: {
                validators: {
                    notEmpty: {
                        message: 'Enter valid url.'
                    }
                }
            },
            digits_only: {
                validators: {
                    notEmpty: {
                        message: 'This field is required.'
                    },
                    regexp: {
                        regexp: /^\d+$/,
                        message: 'Contains digits only.'
                    }
                }
            },
            Range: {
                validators: {
                    notEmpty: {
                        message: 'Enter digits between 5 to 16.'
                    },
                    between: {
                        min: 5,
                        max: 16,
                        message: 'Please enter a value between 5 and 16.'
                    },
                    regexp: {
                        regexp: /^\d+$/,
                        message: 'The value is not an integer'
                    }
                }
            },
            activate: {
                validators: {
                    notEmpty: {
                        message: 'You have to accept the terms and conditions'
                    }
                }
            }
        }
    });
    $('#form_inline_validator').bootstrapValidator({
        framework: 'bootstrap',
        fields: {
            Name3: {
                validators: {
                    notEmpty: {
                        message: 'Enter your name'
                    }
                }
            },
            Email3: {
                validators: {
                    notEmpty: {
                        message: 'The email address is required'
                    },
                    regexp: {
                        regexp: /^\S+@\S{1,}\.\S{1,}$/,
                        message: 'The input is not a valid email address.'
                    }
                }
            },
            Password3: {
                validators: {
                    notEmpty: {
                        message: 'Please provide a password'
                    }
                }
            },
            Confirmpassword3: {
                validators: {
                    notEmpty: {
                        message: 'The confirm password is required and can\'t be empty.'
                    },
                    identical: {
                        field: 'Password3',
                        message: 'Please enter the same password as above'
                    }
                }
            },

            Url3: {
                validators: {
                    notEmpty: {
                        message: 'Enter valid url.'
                    }
                }
            },
            Minsize3: {
                validators: {
                    notEmpty: {
                        message: 'Enter min 3 characters.'
                    },
                    regexp: {
                        regexp: /^\S.{2,}$/,
                        message: 'Please enter at least 3 characters and should not start with space.'
                    }
                }
            },
            Maxsize3: {
                validators: {
                    notEmpty: {
                        message: 'Enter max 6 characters'
                    },
                    regexp: {
                        regexp: /^\S.{0,5}$/,
                        message: 'Should not be more than 6 characters and should not start with space.'
                    }
                }
            },

            MinNum: {
                validators: {
                    notEmpty: {
                        message: 'Enter the minimum number 3.'
                    },
                    greaterThan: {
                        value: 3,
                        message: 'Please enter a value greater than or equal to 3.'
                    },
                    regexp: {
                        regexp: /^\d+$/,
                        message: 'The value is not an integer'
                    }
                }
            },
            maxNum: {
                validators: {
                    notEmpty: {
                        message: 'Enter maximum number 16.'
                    },
                    lessThan: {
                        value: 16,
                        message: 'Please enter a value less than or equal to 16.'
                    },
                    regexp: {
                        regexp: /^\d+$/,
                        message: 'The value is not an integer'
                    }

                }
            },
            birthday: {
                validators: {
                    notEmpty: {
                        message: 'Date is required and can not be empty'
                    }
                }
            }
        }
    });
});
