$(document).ready( function(){
  (function($){
    $.fn.setCursorToTextEnd = function() {
      var $initialVal = this.val();
      this.val($initialVal);
    };
  })(jQuery);
  var data = ""
  $("table").on("click", ".editable", function(e) {
    e.stopPropagation();
    $("body").find(".text_donot_save").click();
    data = $(this).text();
    var a = "<div class='editable_table_text form-group editable_table form-inline'><input type='text' class='form-control input_text' value='" + $(this).text() + "'>" +
        "<button class='btn btn-primary text_save'><i class='fa fa-check text-white'></i></button>" +
        "<button class='btn btn-danger text_donot_save'><i class='fa fa-close text-white'></i></button></div>"
    $(this).removeClass("editable");
    $(this).html(a);
    $(this).find("input[type='text']").focus().setCursorToTextEnd();
  });
  $("table").on("click", ".text_save", function() {
    var x = $(".input_text").val();
    $(this).closest("span").addClass("editable").text(x);
  });
  $("table").on("click", ".text_donot_save", function() {
    $(this).closest("span").addClass("editable").text(data);
  });
  $('#users').on("click", ".editable_table_text", function(event) {
    event.stopPropagation();
  });
  $("html").on("click",function() {
    $("body").find(".text_donot_save").click();
  });
  $(".icon-arrow-left").replaceWith("<i class='fa fa-arrow-left arrow_padding text-white'></i>");
  $(".icon-arrow-right").replaceWith("<i class='fa fa-arrow-right arrow_padding text-white'></i>");
  var cTime = new Date(), month = cTime.getMonth()+1, year = cTime.getFullYear();

    theMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    theDays = ["S", "M", "T", "W", "T", "F", "S"];
    events = [
      [
        "5/"+month+"/"+year, 
        'Meet a friend', 
        '#', 
        '#fb6b5b', 
        'Contents here'
      ],
      [
        "8/"+month+"/"+year, 
        'Meeting with CEO', 
        '#', 
        '#ffba4d', 
        'Contents here'
      ],
      [
        "18/"+month+"/"+year, 
        'Milestone release', 
        '#', 
        '#ffba4d', 
        'Contents here'
      ],
      [
        "19/"+month+"/"+year, 
        'A link', 
        '/admire', 
        '#cccccc'
      ]
    ];

    $('#calendar_mini').calendar({
        months: theMonths,
        days: theDays,
        events: events,
        popover_options:{
            placement: 'top',
            html: true
        }
    });
  $('[data-original-title="A link"]').replaceWith('<a data-original-title="A link" href="#" rel="tooltip">19</a>');
  $("#calendar_mini .icon-arrow-right").replaceWith('<i class="fa fa-arrow-right text-white arrow_padding" aria-hidden="true"></i>')
  $("#calendar_mini .icon-arrow-left").replaceWith('<i class="fa fa-arrow-left text-white arrow_padding" aria-hidden="true"></i>')
});