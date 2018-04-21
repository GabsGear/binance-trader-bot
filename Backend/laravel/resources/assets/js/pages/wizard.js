'use strict';
$(document).ready(function() {
    $("#commentForm").bootstrapValidator({
        fields: {
            username: {
                validators: {
                    notEmpty: {
                        message: 'The User name is required'
                    }
                },
                required: true,
                minlength: 3
            },
            password: {
                validators: {
                    notEmpty: {
                        message: 'The password is required'
                    }
                }
            },
            confirm: {
                validators: {
                    notEmpty: {
                        message: 'Confirm Password is required'
                    },
                    identical: {
                        field: 'password'
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
            val_first_name: {
                validators: {
                    notEmpty: {
                        message: 'The first name is required '
                    }
                }
            },
            lname: {
                validators: {
                    notEmpty: {
                        message: 'The last name is required '
                    }
                }
            },
            gender: {
                validators: {
                    notEmpty: {
                        message: 'Please select a gender'
                    }
                }
            },
            val_address: {
                validators: {
                    notEmpty: {
                        message: 'The address is required '
                    }
                }
            },

            password3: {
                validators: {
                    notEmpty: {
                        message: 'Password is required'
                    }
                },
                required: true,
                minlength: 3
            },
            val_age: {
                validators: {
                    notEmpty: {
                        message:'Age is required and between 18 to 100'

                    },
                    digits: {
                        message:'Enter only digits '
                    },
                    greaterThan: {
                        value: 18,
                        message:'The age should be greater than or equal to 18 '
                    },
                    lessThan: {
                        value: 100,
                        message:'The age should be less than or equal to 100 '
                    }

                }
            },
            phone1: {
                validators: {
                    notEmpty: {
                        message: 'The home number is required'
                    },
                    regexp: {
                        regexp: /^(\+?1-?)?(\([2-9]\d{2}\)|[2-9]\d{2})-?[2-9]\d{2}-?\d{4}$/,
                        message: 'Enter valid phone number'
                    }
                }
            },
            phone2: {
                validators: {
                    notEmpty: {
                        message: 'The personal number is required'
                    },
                    regexp: {
                        regexp: /^(\+?1-?)?(\([2-9]\d{2}\)|[2-9]\d{2})-?[2-9]\d{2}-?\d{4}$/,
                        message: 'Enter valid phone number'
                    }
                }
            },
            phone3: {
                validators: {
                    notEmpty: {
                        message: 'Alternate number is required'
                    },
                    different: {
                        field: 'phone1',
                        message: 'The alternate number must be different from Home number'
                    },
                    regexp: {
                        regexp: /^(\+?1-?)?(\([2-9]\d{2}\)|[2-9]\d{2})-?[2-9]\d{2}-?\d{4}$/,
                        message: 'Enter valid phone number'
                    }
                }
            },
            acceptTerms:{
                validators:{
                    notEmpty:{
                        message: 'The checkbox must be checked'
                    }
                }
            }
        }
    });

    $('#acceptTerms').on('ifChanged', function(event){
        $('#commentForm').bootstrapValidator('revalidateField', $('#acceptTerms'));
    });
    $('#rootwizard').bootstrapWizard({
        'tabClass': 'nav nav-pills',
        'onNext': function(tab, navigation, index) {
            var $validator = $('#commentForm').data('bootstrapValidator').validate();
            if($validator.isValid()){
                // alert('fd');
                $(".userprofile_tab1").addClass("tab_clr");
                $(".userprofile_tab2").addClass("tab_clr");
            }
            return $validator.isValid();
        },
        'onPrevious': function(tab, navigation, index) {
            $(".userprofile_tab2").removeClass("tab_clr");
        },
        onTabClick: function(tab, navigation, index) {
            return false;
        },
        onTabShow: function(tab, navigation, index) {
            var $total = navigation.find('li').length;
            var $current = index+1;
            var $percent = ($current/$total) * 100;
            var $rootwizard= $('#rootwizard');
            // If it's the last tab then hide the last button and show the finish instead
            if($current >= $total) {
                $rootwizard.find('.pager .next').hide();
                $rootwizard.find('.pager .finish').show();
                $rootwizard.find('.pager .finish').removeClass('disabled');
            } else {
                $rootwizard.find('.pager .next').show();
                $rootwizard.find('.pager .finish').hide();
            }
            $('#rootwizard .finish').on("click",function() {
                var $validator = $('#commentForm').data('bootstrapValidator').validate();
                if ($validator.isValid()) {
                    $('#myModal').modal('show');
                    return $validator.isValid();
                    $rootwizard.find("a[href='#tab1']").tab('show');
                }
            });

        }});
    $('#rootwizard_no_val').bootstrapWizard({'tabClass': 'nav nav-pills'});

    $(".user2, .finish_tab, .next_btn1").on("click", function(){
        $(".userprofile_tab").addClass("tab_clr");
    });
    $(".user1, .previous_btn2").on("click", function(){
        $(".userprofile_tab").removeClass("tab_clr");
    });
    $(".finish_tab, .next_btn2").on("click", function(){
        $(".profile_tab").addClass("tab_clr");
    });
    $(".user2, .previous_btn3").on("click", function(){
        $(".profile_tab").removeClass("tab_clr");
    });
    $(".user1").on('click',function () {
        $(".user2 a span").removeClass("tab_clr");
    });
    $(".general_number").on('keyup',function () {
        if (/\D/g.test(this.value)) {
            this.value = this.value.replace(/\D/g,'')
        }
    });
});

