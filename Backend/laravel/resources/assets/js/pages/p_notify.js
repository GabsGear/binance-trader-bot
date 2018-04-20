'use strict';
$(document).ready(function() {
    function dyn_notice() {
        var percent = 0;
        var notice = new PNotify({
            text: "Please Wait",
            type: 'info',
            icon: 'fa fa-spinner fa-spin',
            hide: false,
            buttons: {
                closer: false,
                sticker: false
            },
            opacity: .75,
            shadow: false,
            width: "170px"
        });

        setTimeout(function () {
            notice.update({title: false});
            var interval = setInterval(function () {
                percent += 2;
                var options = {
                    text: percent + "% complete."
                };
                if (percent == 80)
                    options.title = "Almost There";
                if (percent >= 100) {
                    window.clearInterval(interval);
                    options.title = "Done!";
                    options.type = "success";
                    options.hide = true;
                    options.buttons = {
                        closer: true,
                        sticker: true
                    };
                    options.icon = 'fa fa-check';
                    options.opacity = 1;
                    options.shadow = true;
                    options.width = PNotify.prototype.options.width;
                }
                notice.update(options);
            }, 120);
        }, 2000);
    }

    function fake_load() {
        var cur_value = 1,
            progress;

        // Make a loader.
        var loader = new PNotify({
            title: "Creating series of tubes",
            text: '<div class="progress progress-striped active" style="margin:0">\
    <div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0">\
        <span class="sr-only">0%</span>\
    </div>\
</div>',
            //icon: 'fa fa-moon-o fa-spin',
            icon: 'fa fa-cog fa-spin',
            hide: false,
            buttons: {
                closer: false,
                sticker: false
            },
            history: {
                history: false
            },
            before_open: function (notice) {
                progress = notice.get().find("div.progress-bar");
                progress.width(cur_value + "%").attr("aria-valuenow", cur_value).find("span").html(cur_value + "%");
                // Pretend to do something.
                var timer = setInterval(function () {
                    if (cur_value == 70) {
                        loader.update({title: "Aligning discrete worms", icon: "fa fa-circle-o-notch fa-spin"});
                    }
                    if (cur_value == 80) {
                        loader.update({title: "Connecting end points", icon: "fa fa-refresh fa-spin"});
                    }
                    if (cur_value == 90) {
                        loader.update({title: "Dividing and conquering", icon: "fa fa-spinner fa-spin"});
                    }
                    if (cur_value >= 100) {
                        // Remove the interval.
                        window.clearInterval(timer);
                        loader.remove();
                        return;
                    }
                    cur_value += 1;
                    progress.width(cur_value + "%").attr("aria-valuenow", cur_value).find("span").html(cur_value + "%");
                }, 65);
            }
        });
    }

    // Basic notifications

    $(".notify_desktop").on("click", function () {
        PNotify.desktop.permission();
        new PNotify({
            title: 'Desktop Info',
            text: 'If you\'ve given me permission, I\'ll appear as a desktop notification. If you haven\'t, I\'ll still appear as a regular PNotify notice.',
            type: 'info',
            desktop: {
                desktop: true
            }
        }).get().on("click",function (e) {
            if ($('.ui-pnotify-closer, .ui-pnotify-sticker, .ui-pnotify-closer *, .ui-pnotify-sticker *').is(e.target))
                return;
            alert('Hey! You clicked the desktop notification!');
        });
        return false;
    });
    $(".notify_desktopsuccess").on("click", function () {
        PNotify.desktop.permission();
        new PNotify({
            title: 'Desktop Success',
            text: 'If you\'ve given me permission, I\'ll appear as a desktop notification. If you haven\'t, I\'ll still appear as a regular PNotify notice.',
            type: 'success',
            desktop: {
                desktop: true
            }
        }).get().on("click",function (e) {
            if ($('.ui-pnotify-closer, .ui-pnotify-sticker, .ui-pnotify-closer *, .ui-pnotify-sticker *').is(e.target))
                return;
            alert('Hey! You clicked the desktop notification!');
        });
        return false;
    });
    $(".notify_dyn_notice").on("click", function () {
        dyn_notice();
        return false;
    });
    $(".notify_regerror").on("click", function () {
        new PNotify({
            title: 'Oh No!',
            text: 'Something terrible happened.',
            type: 'error'
        });
        return false;
    });
    $(".notify_formnotice").on("click", function () {
        var notice = new PNotify({
            text: $('#form_notice').html(),
            icon: false,
            width: 'auto',
            hide: false,
            type: 'warning',
            buttons: {
                closer: false,
                sticker: false
            },
            insert_brs: false
        });
        notice.get().find('form.pf-form').on('click', '[name=cancel]', function () {
            notice.remove();
        }).on("submit",function () {
            var username = $(this).find('input[name=username]').val();
            if (!username) {
                alert('Please provide a username.');
                return false;
            }
            notice.update({
                title: 'Welcome',
                text: 'Successfully logged in as ' + username,
                icon: true,
                width: PNotify.prototype.options.width,
                hide: true,
                buttons: {
                    closer: true,
                    sticker: true
                },
                type: 'success'
            });
            return false;
        });
        return false;
    });
    $(".notify_regularinfo").on("click", function () {
        new PNotify({
            title: 'New Thing',
            text: 'Just to let you know, something happened.',
            type: 'info'
        });
        return false;
    });

    // End of basic notifications

    // Animated notifications
    $(".notify_fromtop").on("click", function () {
        new PNotify({
            title: 'From the top! Effect',
            text: 'I use effects from Animate.css. Such smooth CSS3 transitions make me feel like better.',
            type: 'warning',
            animate: {
                animate: true,
                in_class: 'slideInDown',
                out_class: 'slideOutUp'
            }
        });
        return false;
    });
    $(".notify_zoom").on("click", function () {
        new PNotify({
            title: 'Zoom Effect',
            text: 'I use effects from Animate.css. Such smooth CSS3 transitions make me feel like better.',
            type: 'info',
            animate: {
                animate: true,
                in_class: 'zoomInLeft',
                out_class: 'zoomOutRight'
            }
        });
        return false;
    });
    $(".notify_zippy").on("click", function () {
        new PNotify({
            title: 'Zippy Effect',
            text: 'I use effects from Animate.css. Such smooth CSS3 transitions make me feel like better.',
            type: 'error',
            animate: {
                animate: true,
                in_class: 'bounceInLeft',
                out_class: 'bounceOutRight'
            }
        });
        return false;
    });
    $(".notify_off_handle").on("click", function () {
        new PNotify({
            title: 'Off the handle Effect',
            text: 'I use effects from Animate.css. Such smooth CSS3 transitions make me feel like better.',
            type: 'success',
            animate: {
                animate: true,
                in_class: 'bounceInDown',
                out_class: 'hinge'
            }
        });
        return false;
    });
    $(".notify_cards").on("click", function () {
        new PNotify({
            title: 'Shuffling cards Effect',
            text: 'I use effects from Animate.css. Such smooth CSS3 transitions make me feel like better.',
            type: 'info',
            animate: {
                animate: true,
                in_class: 'rotateInDownLeft',
                out_class: 'rotateOutUpRight'
            }
        });
        return false;
    });
    // End of animated notifications

    $(".notify_bignotice").on("click", function () {
        new PNotify({
            title: 'Big Notice',
            text: 'Check me out! I\'m tall and wide, even though my text isn\'t.',
            width: '500px',
            min_height: '400px',
            type: 'error'
        });
        return false;
    });

    // Own animation style
    $(".notify_btn").on("click", function () {
        var animate_in = $('#animate_in').val(),
            animate_out = $('#animate_out').val();
        new PNotify({
            title: 'Animate.css Effect',
            text: 'I use effects from Animate.css. Such smooth CSS3 transitions make me feel like better.',
            animate: {
                animate: true,
                in_class: animate_in,
                out_class: animate_out
            }
        });
        return false;
    });
    // End of Own animation style

    // Attension seekers
    $(".notify_bounce").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'success',
            after_init: function (notice) {
                notice.attention('bounce');
            }
        });
        return false;
    });
    $(".notify_flash").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'warning',
            after_init: function (notice) {
                notice.attention('flash');
            }
        });
        return false;
    });
    $(".notify_pulse").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'info',
            after_init: function (notice) {
                notice.attention('pulse');
            }
        });
        return false;
    });
    $(".notify_rubberband").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'error',
            after_init: function (notice) {
                notice.attention('rubberBand');
            }
        });
        return false;
    });
    $(".notify_shake").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'success',
            after_init: function (notice) {
                notice.attention('rubberBand');
            }
        });
        return false;
    });
    $(".notify_swing").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'warning',
            after_init: function (notice) {
                notice.attention('swing');
            }
        });
        return false;
    });
    $(".notify_tada").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'info',
            after_init: function (notice) {
                notice.attention('tada');
            }
        });
        return false;
    });
    $(".notify_wobble").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'error',
            after_init: function (notice) {
                notice.attention('wobble');
            }
        });
        return false;
    });
    $(".notify_jello").on("click", function () {
        new PNotify({
            title: 'Attention Seeker',
            text: 'Click the button to see how you can highlight the notice with the Animate module:&lt;br&gt;',
            type: 'success',
            after_init: function (notice) {
                notice.attention('jello');
            }
        });
        return false;
    });
    //End of  Attension seekers

    // Confirm Module Confirmation dialogs and prompts
    $(".notify_confirm_dialog").on("click", function () {
        new PNotify({
            title: 'Confirmation Needed',
            text: 'Are you sure?',
            icon: 'fa fa-question-circle',
            hide: false,
            type: 'success',
            confirm: {
                confirm: true
            },
            buttons: {
                closer: false,
                sticker: false
            },
            history: {
                history: false
            }
        }).get().on('pnotify.confirm', function () {
            swal('Ok cool').done();
        }).on('pnotify.cancel', function () {
            swal('Oh ok. Chicken, I see.').done();

        });
        return false;
    });
    $(".notify_modal_dialog").on("click", function () {
        new PNotify({
            title: 'Confirmation Needed',
            text: 'Are you sure?',
            icon: 'fa fa-question-circle',
            hide: false,
            type: 'info',
            confirm: {
                confirm: true
            },
            buttons: {
                closer: false,
                sticker: false
            },
            history: {
                history: false
            },
            addclass: 'stack-modal',
            stack: {'dir1': 'down', 'dir2': 'right', 'modal': true}
        }).get().on('pnotify.confirm', function () {
            swal('Ok cool').done();
        }).on('pnotify.cancel', function () {
            swal('Oh ok. Chicken, I see.').done();
        });
        return false;
    });
    $(".notify_custom_buttons").on("click", function () {
        new PNotify({
            title: 'Choose a Side',
            text: 'You have three options to choose from.',
            icon: 'fa fa-question-circle',
            hide: false,
            type: 'error',
            confirm: {
                confirm: true,
                buttons: [
                    {
                        text: 'Fries',
                        addClass: 'btn-primary',
                        click: function (notice) {
                            notice.update({
                                title: 'You\'ve Chosen a Side',
                                text: 'You want fries.',
                                icon: true,
                                type: 'info',
                                hide: true,
                                confirm: {
                                    confirm: false
                                },
                                buttons: {
                                    closer: true,
                                    sticker: true
                                }
                            });
                        }
                    },
                    {
                        text: 'Mash',
                        click: function (notice) {
                            notice.update({
                                title: 'You\'ve Chosen a Side',
                                text: 'You want mashed potatoes.',
                                icon: true,
                                type: 'info',
                                hide: true,
                                confirm: {
                                    confirm: false
                                },
                                buttons: {
                                    closer: true,
                                    sticker: true
                                }
                            });
                        }
                    },
                    {
                        text: 'Fruit',
                        click: function (notice) {
                            notice.update({
                                title: 'You\'ve Chosen a Side',
                                text: 'You want fruit.',
                                icon: true,
                                type: 'info',
                                hide: true,
                                confirm: {
                                    confirm: false
                                },
                                buttons: {
                                    closer: true,
                                    sticker: true
                                }
                            });
                        }
                    }
                ]
            },
            buttons: {
                closer: false,
                sticker: false
            },
            history: {
                history: false
            }
        });
        return false;
    });
    $(".notify_alert_button").on("click", function () {
        new PNotify({
            title: 'You Will Receive a Side',
            text: 'You have no choice.',
            icon: 'fa fa-info-circle',
            hide: false,
            type: 'warning',
            confirm: {
                confirm: true,
                buttons: [
                    {
                        text: 'Ok',
                        addClass: 'btn-primary',
                        click: function (notice) {
                            notice.remove();
                        }
                    },
                    null
                ]
            },
            buttons: {
                closer: false,
                sticker: false
            },
            history: {
                history: false
            }
        });
        return false;
    });
    $(".notify_prompt_dialog").on("click", function () {
        new PNotify({
            title: 'Input Needed',
            text: 'What side would you like?',
            icon: 'fa fa-question-circle',
            hide: false,
            type: 'success',
            confirm: {
                prompt: true
            },
            buttons: {
                closer: false,
                sticker: false
            },
            history: {
                history: false
            }
        }).get().on('pnotify.confirm', function(e, notice, val){
            notice.cancelRemove().update({
                title: 'You\'ve Chosen a Side', text: 'You want '+$('<div/>').text(val).html()+'.', icon: true, type: 'info', hide: true,
                confirm: {
                    prompt: false
                },
                buttons: {
                    closer: true,
                    sticker: true
                }
            });
        }).on('pnotify.cancel', function(e, notice){
            notice.cancelRemove().update({
                title: 'You Don\'t Want a Side', text: 'No soup for you!', icon: true, type: 'info', hide: true,
                confirm: {
                    prompt: false
                },
                buttons: {
                    closer: true,
                    sticker: true
                }
            });
        });
        return false;
    });
    $(".notify_multiprompt_dialog").on("click", function () {
        new PNotify({
            title: 'Input Needed',
            text: 'Write me a poem, please.',
            icon: 'fa fa-question-circle',
            hide: false,
            type: 'error',
            confirm: {
                prompt: true,
                prompt_multi_line: true,
                prompt_default: 'Roses are red,\nViolets are blue,\n'
            },
            buttons: {
                closer: false,
                sticker: false
            },
            history: {
                history: false
            }
        }).get().on('pnotify.confirm', function(e, notice, val){
            notice.cancelRemove().update({
                title: 'Your Poem', text: $('<div/>').text(val).html(), icon: true, type: 'info', hide: true,
                confirm: {
                    prompt: false
                },
                buttons: {
                    closer: true,
                    sticker: true
                }
            });
        }).on('pnotify.cancel', function(e, notice){
            notice.cancelRemove().update({
                title: 'You Don\'t Like Poetry', text: 'Roses are dead,\nViolets are dead,\nI suck at gardening.', icon: true, type: 'info', hide: true,
                confirm: {
                    prompt: false
                },
                buttons: {
                    closer: true,
                    sticker: true
                }
            });
        });
        return false;
    });
    // End of Confirm Module Confirmation dialogs and prompts

    // Callbacks Module Manipulate the notice during its lifecycle
    $(".notify_callback").on("click", function () {
        var dont_alert = function(){};
        new PNotify({
            title: 'I\'m Here',
            text: 'I have a callback for each of my events. I\'ll call all my callbacks while I change states.',
            before_init: function(opts){
                alert('I\'m called before the notice initializes. I\'m passed the options used to make the notice. I can modify them. Watch me replace the word callback with tire iron!');
                opts.text = opts.text.replace(/callback/g, 'tire iron');
            },
            after_init: function(notice){
                alert('I\'m called after the notice initializes. I\'m passed the PNotify object for the current notice: '+notice+'\n\nThere are more callbacks you can assign, but this is the last notice you\'ll see. Check the code to see them all.');
            },
            before_open: function(notice){
                var source_note = 'Return false to cancel opening.';
                dont_alert('I\'m called before the notice opens. I\'m passed the PNotify object for the current notice: '+notice);
            },
            after_open: function(notice){
                dont_alert('I\'m called after the notice opens. I\'m passed the PNotify object for the current notice: '+notice);
            },
            before_close: function(notice, timer_hide){
                var source_note = 'Return false to cancel close. Use PNotify.queueRemove() to set the removal timer again.';
                dont_alert('I\'m called before the notice closes. I\'m passed the PNotify object for the current notice: '+notice);
                dont_alert('I also have an argument called timer_hide, which is true if the notice was closed because the timer ran down. Value: '+timer_hide);
            },
            after_close: function(notice, timer_hide){
                dont_alert('I\'m called after the notice closes. I\'m passed the PNotify object for the current notice: '+notice);
                dont_alert('I also have an argument called timer_hide, which is true if the notice was closed because the timer ran down. Value: '+timer_hide);
            }
        });
        return false;
    });
    $(".notify_callback1").on("click", function () {
        new PNotify({
            title: 'Notice',
            text: 'Right now I\'m a notice.',
            before_close: function (notice) {
                notice.update({
                    title: 'Error',
                    text: 'Uh oh. Now I\'ve become an error.',
                    type: 'error',


                    before_close: function (notice) {
                        notice.update({
                            title: 'Success',
                            text: 'I fixed the error!',
                            type: 'success',
                            before_close: function (notice) {
                                notice.update({
                                    title: 'Info',
                                    text: 'Everything\'s cool now.',
                                    type: 'info',
                                    before_close: null

                                });
                                notice.attention('swing');
                                notice.queueRemove();
                                return false;
                            }
                        });
                        notice.attention('swing');
                        notice.queueRemove();
                        return false;
                    }
                });
                notice.attention('swing');
                notice.queueRemove();

                return false;
            }
        });
        return false;
    });
    // End of Callbacks Module Manipulate the notice during its lifecycle

    PNotify.prototype.options.styling = "fontawesome";
});