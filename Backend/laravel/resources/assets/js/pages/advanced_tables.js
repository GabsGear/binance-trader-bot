'use strict';
$(document).ready(function(){
    // Scroll - horizontal and Vertical Scroll Table
    $('#example').DataTable( {
        "scrollY": 200,
        "scrollX": true
    });
    //End of Scroll - horizontal and Vertical Scroll Table

    // advanced Table

    var table = $('#example_demo').DataTable({
        "dom": "<'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-responsive't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>"
    });
    var $example_demo= $('#example_demo tbody');
    $example_demo.on( 'mouseenter', 'td', function () {
        var colIdx = table.cell(this).index().column;
        $( table.cells().nodes() ).removeClass( 'highlight' );
        $( table.column( colIdx ).nodes() ).addClass( 'highlight' );
        return false;
    } );
    $example_demo.on( 'mouseleave','td', function () {
        $( table.cells().nodes() ).removeClass( 'highlight' );
        return false;
    } );

    $example_demo.on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
        $('#del_button').on('click', function () {
            table.row('#example_demo tbody .selected').remove().draw( false );
            return false;
        } );
        return false;
    } );
    // End of advanced Table
    $(".dataTables_wrapper").removeClass("form-inline");
});