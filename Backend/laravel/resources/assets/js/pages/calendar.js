"use strict";
$(document).ready(function() {
    /* initialize the external events
     -----------------------------------------------------------------*/
    function ini_events(ele) {
        ele.each(function() {

            var eventObject = {
                title: $.trim($(this).text())
            };

            $(this).data('eventObject', eventObject);

            // make the event draggable using jQuery UI
            $(this).draggable({
                zIndex: 1070,
                revert: true,
                revertDuration: 0
            });
        });
    }
    ini_events($('#external-events div.external-event'));
    var evt_obj;

    /* initialize the calendar */
    //Date for the calendar events (dummy data)
    var date = new Date();
    var d = date.getDate(),
        m = date.getMonth(),
        y = date.getFullYear();
    $('#calendar').fullCalendar({
        displayEventTime: false,
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        buttonText: {
            prev: "",
            next: "",
            today: 'today',
            month: 'M',
            week: 'W',
            day: 'D'
        },
        //Random events
        events: [{
            title: 'Team Out',
            start: new Date(y, m, 2),
            backgroundColor: "#ff9933"
        }, {
            title: 'Client Meeting',
            start: new Date(y, m, d - 2),
            end: new Date(y, m, d - 5),
            backgroundColor: "#ff6666"
        }, {
            title: 'Repeating Event',
            start: new Date(y, m, 6),
            backgroundColor: "#347dff"
        }, {
            title: 'Birthday Party',
            start: new Date(y, m, 12),
            backgroundColor: "#00cc99"
        }, {
            title: 'Product Seminar',
            start: new Date(y, m, 16),
            backgroundColor: "#4fb7fe"
        }, {
            title: 'Anniversary Celebrations',
            start: new Date(y, m, 26),
            backgroundColor: "#ff6666"
        }, {
            title: 'Client Meeting',
            start: new Date(y, m, 10),
            backgroundColor: "#00cc99"
        }],
        eventClick: function(calEvent, jsEvent, view) {
            evt_obj=calEvent;
            $("#event_title").val(evt_obj.title);
            currColor=evt_obj.backgroundColor;
            colorChooser.css({
                "background-color": evt_obj.backgroundColor,
                "border-color": evt_obj.backgroundColor
            }).html('type <span class="caret"></span>');
            $('#evt_modal').modal('show').on("shown.bs.modal",function(){
                $("#event_title").focus();
            }).on("hidden.bs.modal",function () {
                evt_obj="";
            });
            $(".text_save").on("click",function () {
                evt_obj.title=$("#event_title").val();
                evt_obj.backgroundColor=currColor;
                $('#calendar').fullCalendar('updateEvent', evt_obj);
                setTimeout(setpopover,100);
            });
        },
        editable: true,
        droppable: true,
        drop: function(date, allDay) {

            // retrieve the dropped element's stored Event Object
            var originalEventObject = $(this).data('eventObject');

            // we need to copy it, so that multiple events don't have a reference to the same object
            var copiedEventObject = $.extend({}, originalEventObject);
            var $calendar_badge= $(".calendar_badge");
            // assign it the date that was reported
            copiedEventObject.start = date;
            copiedEventObject.allDay = allDay;
            copiedEventObject.backgroundColor = $(this).css("background-color");
            copiedEventObject.borderColor = $(this).css("border-color");

            $('#calendar').fullCalendar('renderEvent', copiedEventObject, true);
            $calendar_badge.text(parseInt($calendar_badge.text()) + 1);
            // is the "remove after drop" checkbox checked?
            if ($('#drop-remove').is(':checked')) {
                $(this).remove();
            }
            setpopover();
        },
        eventDrop: function() {
            setTimeout(setpopover,100);
        },
        eventResize:function() {
            setTimeout(setpopover,100);
        }
    });

    /* ADDING EVENTS */
    var currColor = "#737373"; //default
    //Color chooser button
    var colorChooser = $(".color-chooser-btn");
    $(".color-chooser > a").on('click',function(e) {
        e.preventDefault();
        //Save color
        currColor = $(this).css("background-color");
        //Add color effect to button
        colorChooser
            .css({
                "background-color": currColor,
                "border-color": currColor
            })
            .html($(this).text() + ' <span class="caret"></span>');
    });
    $("#add-new-event").on('click',function(e) {
        e.preventDefault();
        //Get value and make sure it is not null
        var $newevent= $("#new-event");
        var val = $newevent.val();
        if (val.length == 0) {
            return;
        }

        //Create event
        var event = $("<div />");
        event.css({
            "background-color": currColor,
            "border-color": currColor,
            "color": "#fff"
        }).addClass("external-event");
        event.html(val).append(' <i class="fa fa-times event-clear" aria-hidden="true"></i>');
        $('#external-events').prepend(event);

        //Add draggable funtionality
        ini_events(event);

        //Remove event from text input
        $newevent.val("");
    });
    $("body").on("click", "#external-events .event-clear", function() {
        $(this).closest(".external-event").remove();
        return false;
    });
    $(".modal-dialog [data-dismiss='modal']").on('click', function() {
        $("#new-event").replaceWith('<input type="text" id="new-event" class="form-control" placeholder="Event">');
    });

    function setpopover() {
        $(".fc-month-view").find(".fc-event-container a").each(function() {
            $(this).popover({
                placement: 'top',
                html: true,
                content: $(this).text(),
                trigger: 'hover'
            });
        });
        $(".fc-month-button").on('click',function () {
            $(".fc-event-container a").each(function() {
                $(this).popover({
                    placement: 'top',
                    html: true,
                    content: $(this).text(),
                    trigger: 'hover'
                });
            });
            return false;
        })
    }
    $(".fc-center").find('h2').css('font-size', '18px');
    setpopover();
});