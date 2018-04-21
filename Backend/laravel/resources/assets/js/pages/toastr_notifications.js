'use strict';
$(document).ready(function() {
    var i = -1;
    var toastCount = 0;
    var $toastlast;

    var getMessage = function() {
        var msgs = ['My name is Inigo Montoya. You killed my father. Prepare to die!',
            '<div><input class="input-small" value="textbox"/>&nbsp;<a href="http://johnpapa.net" target="_blank">This is a hyperlink</a></div><div><button type="button" id="okBtn" class="btn btn-primary">Close me</button><button type="button" id="surpriseBtn" class="btn" style="margin: 0 8px 0 8px">Surprise me</button></div>',
            'Are you the six fingered man?',
            'Inconceivable!',
            'I do not think that means what you think it means.',
            'Have fun storming the castle!'
        ];
        i++;
        if (i === msgs.length) {
            i = 0;
        }

        return msgs[i];
    };
    $( "[value^='toast-bottom']").on('change', function (event) {
        $("#showMethod option:eq(2)").text("slideUp");
        $("#hideMethod option:eq(2)").text("slideDown");
    });
    $("[value^='toast-top']").on("change", function(event) {
        $("#showMethod option:eq(2)").text("slideDown");
        $("#hideMethod option:eq(2)").text("slideUp");
    });
    $("#toastrOptions").hide();
    $('#showtoast').on("click",function() {
        $("#toastrOptions").show();
        var shortCutFunction = $("#toastTypeGroup input:radio:checked").val();
        var msg = $('#message').val();
        var title = $('#title').val() || '';
        var $showDuration = $('#showDuration');
        var $hideDuration = $('#hideDuration');
        var $timeOut = $('#timeOut');
        var $extendedTimeOut = $('#extendedTimeOut');
        var $showEasing = $('#showEasing');
        var $hideEasing = $('#hideEasing');
        var $showMethod = $('#showMethod');
        var $hideMethod = $('#hideMethod');
        var toastIndex = toastCount++;

        toastr.options = {
            closeButton: $('#closeButton').prop('checked'),
            debug: $('#debugInfo').prop('checked'),
            positionClass: $('#positionGroup input:radio:checked').val() || 'toast-top-right',
            onclick: null
        };


        if ($('#addBehaviorOnToastClick').prop('checked')) {
            toastr.options.onclick = function() {
                alert('You can perform some custom action after a toast goes away');
            };
        }

        if ($showDuration.val().length) {
            toastr.options.showDuration = $showDuration.val();
        }

        if ($hideDuration.val().length) {
            toastr.options.hideDuration = $hideDuration.val();
        }

        if ($timeOut.val().length) {
            toastr.options.timeOut = $timeOut.val();
        }

        if ($extendedTimeOut.val().length) {
            toastr.options.extendedTimeOut = $extendedTimeOut.val();
        }

        if ($showEasing.val().length) {
            toastr.options.showEasing = $showEasing.val();
        }

        if ($hideEasing.val().length) {
            toastr.options.hideEasing = $hideEasing.val();
        }

        if ($showMethod.val().length) {
            toastr.options.showMethod = $showMethod.val();
        }

        if ($hideMethod.val().length) {
            toastr.options.hideMethod = $hideMethod.val();
        }

        if (!msg) {
            msg = getMessage();
        }

        $("#toastrOptions").text("Command: toastr[" + shortCutFunction + "](\"" + msg + (title ? "\", \"" + title : '') + "\")\n\ntoastr.options = " + JSON.stringify(toastr.options, null, 2));

        var $toast = toastr[shortCutFunction](msg, title); // Wire up an event handler to a button in the toast, if it exists
        $toastlast = $toast;
        if ($toast.find('#okBtn').length) {
            $toast.delegate('#okBtn', 'click', function() {
                alert('you clicked me. i was toast #' + toastIndex + '. goodbye!');
                $toast.remove();
            });
        }
        if ($toast.find('#surpriseBtn').length) {
            $toast.delegate('#surpriseBtn', 'click', function() {
                alert('Surprise! you clicked me. i was toast #' + toastIndex + '. You could perform an action here.');
            });
        }
    });

    function getLastToast() {
        return $toastlast;
    }
    $('#clearlasttoast').on("click",function() {
        toastr.clear(getLastToast());
    });
    $('#cleartoasts').on("click",function() {
        toastr.clear();
    });
});
// Notifications
var classicLayout = false;
var portfolioKeyword;
var $container, $blog_container;
window.anim = {};
window.anim.open = 'flipInX';
window.anim.close = 'flipOutX';
(function($) {
    $(function() {
        $('#anim-open').on('change', function(e) {
            window.anim.open = $(this).val();
        });
        $('#anim-close').on('change', function(e) {
            window.anim.close = $(this).val();
        });
        $('.runner').on('click', function(e) {
            var notes = [];
            notes['alert'] = 'Best check yo self, you\'re not looking too good.';
            notes['error'] = 'Change a few things up and try submitting again.';
            notes['success'] = 'You successfully read this important alert message.';
            notes['information'] = 'This alert needs your attention, but it\'s not super important.';
            notes['warning'] = '<strong>Warning!</strong> <br /> Best check yo self, you\'re not looking too good.';
            notes['confirm'] = 'Do you want to continue?';
            e.preventDefault();
            var self = $(this);
            if (self.data('layout') == 'inline') {
                $(self.data('custom')).noty({
                    text: notes[self.data('type')],
                    type: self.data('type'),
                    theme: 'relax',
                    dismissQueue: true,
                    animation: {
                        open: {
                            height: 'toggle'
                        },
                        close: {
                            height: 'toggle'
                        },
                        easing: 'swing',
                        speed: 500
                    },
                    buttons: (self.data('type') != 'confirm') ? false : [{
                        addClass: 'btn btn-primary',
                        text: 'Ok',
                        onClick: function($noty) {
                            $noty.close();
                            $(self.data('custom')).noty({
                                force: true,
                                text: 'You clicked "Ok" button',
                                type: 'success'
                            });
                        }
                    }, {
                        addClass: 'btn btn-danger',
                        text: 'Cancel',
                        onClick: function($noty) {
                            $noty.close();
                            $(self.data('custom')).noty({
                                force: true,
                                text: 'You clicked "Cancel" button',
                                type: 'error'
                            });
                        }
                    }]
                });
                return false;
            }
            noty({
                text: notes[self.data('type')],
                type: self.data('type'),
                theme: 'relax',
                dismissQueue: true,
                layout: self.data('layout'),
                animation: {
                    open: {
                        height: 'toggle'
                    },
                    close: {
                        height: 'toggle'
                    },
                    easing: 'swing',
                    speed: 500
                },
                buttons: (self.data('type') != 'confirm') ? false : [{
                    addClass: 'btn btn-primary',
                    text: 'Ok',
                    onClick: function($noty) {
                        $noty.close();
                        noty({
                            force: true,
                            theme: 'relax',
                            animation: {

                                open: {
                                    height: 'toggle'
                                },
                                close: {
                                    height: 'toggle'
                                },
                                easing: 'swing',
                                speed: 500
                            },
                            text: 'You clicked "Ok" button',
                            type: 'success',
                            layout: self.data('layout')
                        });
                    }
                }, {
                    addClass: 'btn btn-danger',
                    text: 'Cancel',
                    onClick: function($noty) {
                        $noty.close();
                        noty({
                            force: true,
                            theme: 'relax',
                            animation: {

                                open: {
                                    height: 'toggle'
                                },
                                close: {
                                    height: 'toggle'
                                },
                                easing: 'swing',
                                speed: 500
                            },
                            text: 'You clicked "Cancel" button',
                            type: 'error',
                            layout: self.data('layout')
                        });
                    }
                }]
            });
            return false;
        });
    });

})(jQuery);
