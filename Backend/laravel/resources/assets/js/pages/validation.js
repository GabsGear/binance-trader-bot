'use strict';
$(document).ready(function() {
    $('#clear').on('click', function() {
        $('#tryitForm1,  #tryitForm').bootstrapValidator("resetForm");
    });

    $('#tryitForm1').bootstrapValidator({
        fields: {
            firstName: {
                validators: {
                    notEmpty: {
                        message: 'Enter the user name'
                    }
                }
            },
            address1: {
                validators: {
                    notEmpty: {
                        message: 'Enter your address'
                    }
                }
            },
            password: {
                validators: {

                    notEmpty: {
                        message: 'Enter the password'
                    }
                }
            },
            confirmpassword: {
                validators: {
                    notEmpty: {
                        message: 'Confirm the password'
                    },
                    identical: {
                        field: 'password',
                        message: 'Please enter the same password as above'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Enter the email address'
                    },
                    regexp: {
                        regexp: /^\S+@\S{1,}\.\S{1,}$/,
                        message: 'The input is not a valid email address'
                    }
                }
            },
            cell: {
                validators: {
                    notEmpty: {
                        message: 'Enter the phone number'
                    },
                    regexp: {
                        regexp: /^[0-9]{10}$/,
                        message: 'The phone number can only consist of numbers with 10 digits'
                    }
                }
            },
            city: {
                validators: {
                    notEmpty: {
                        message: 'City is required'
                    }
                }
            },
            gender: {
                validators: {
                    notEmpty: {
                        message: 'Gender is required'
                    }
                }
            },
            pincode: {
                validators: {
                    notEmpty: {
                        message: 'Pincode number is required'
                    },
                    regexp: {
                        regexp: /^(\+?1-?)?(\([0-9]\d{2}\)|[0-9]\d{2})-?[0-9]\d{2}$/,
                        message: 'Enter valid Pincode number'
                    }
                }
            },
            activate: {
                validators: {
                    notEmpty: {
                        message: 'You have to activate your account'
                    }
                }
            },
            check_active: {
                validators: {
                    notEmpty: {
                        message: 'You have to active your account'
                    }
                }
            },
            terms: {
                validators: {
                    notEmpty: {
                        message: 'You have to accept the terms and policies'
                    }
                }
            }
        },
        submitHandler: function(form) {
            if ($('#tryitForm1').valid()) {
                console.log("now we enable the submit button!");
            }
        }
    }).on('success.form.bv', function(e) {
        e.preventDefault();
        swal({
            title: "Success.",
            text: "Successfully Added",
            type: "success",
            allowOutsideClick: false
        }).then(function() {
            location.reload();
        });
    });

    $('#tryitForm').bootstrapValidator({
        fields: {
            firstName: {
                validators: {
                    notEmpty: {
                        message: 'Enter the user name'
                    }
                }
            },
            address1: {
                validators: {
                    notEmpty: {
                        message: 'Enter your address'
                    }
                }
            },
            password: {
                validators: {

                    notEmpty: {
                        message: 'Enter the password'
                    }
                }
            },
            confirmpassword: {
                validators: {
                    notEmpty: {
                        message: 'Confirm the password'
                    },
                    identical: {
                        field: 'password',
                        message: 'Please enter the same password as above'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Enter the email address'
                    },
                    regexp: {
                        regexp: /^\S+@\S{1,}\.\S{1,}$/,
                        message: 'The input is not a valid email address'
                    }
                }
            },
            cell: {
                validators: {
                    notEmpty: {
                        message: 'Enter the phone number'
                    },
                    regexp: {
                        regexp: /^[0-9]{10}$/,
                        message: 'The phone number can only consist of numbers with 10 digits'
                    }
                }
            },
            city: {
                validators: {
                    notEmpty: {
                        message: 'City is required'
                    }
                }
            },
            gender: {
                validators: {
                    notEmpty: {
                        message: 'Gender is required'
                    }
                }
            },
            pincode: {
                validators: {
                    notEmpty: {
                        message: 'Pincode number is required'
                    },
                    regexp: {
                        regexp: /^(\+?1-?)?(\([0-9]\d{2}\)|[0-9]\d{2})-?[0-9]\d{2}$/,
                        message: 'Enter valid Pincode number'
                    }
                }
            },
            activate: {
                validators: {
                    notEmpty: {
                        message: 'You have to activate your account'
                    }
                }
            },
            check_active: {
                validators: {
                    notEmpty: {
                        message: 'You have to active your account'
                    }
                }
            },
            terms: {
                validators: {
                    notEmpty: {
                        message: 'You have to accept the terms and policies'
                    }
                }
            }
        },
        submitHandler: function(form) {
            if ($('#tryitForm').valid()) {
                console.log("now we enable the submit button!");
            }
        }
    });
});