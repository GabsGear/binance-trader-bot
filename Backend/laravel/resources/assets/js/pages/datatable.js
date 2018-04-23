'use strict';
$(document).ready(function() {
    TableAdvanced.init();
    $(".dataTables_scrollHeadInner .table").addClass("table-responsive");
    $("#sample_5_wrapper table").removeClass("table-responsive");
    $(".dataTables_wrapper .dt-buttons .btn").addClass('btn-secondary').removeClass('btn-default');
    $(".dataTables_wrapper").removeClass("form-inline");
});
var TableAdvanced = function() {
    // ===============table 1====================
    var initTable1 = function() {
        var table = $('#sample_1');
        /* Table tools samples: https://www.datatables.net/release-datatables/extras/TableTools/ */
        /* Set tabletools buttons and button container */
        table.DataTable({
            dom: "Bflr<'table-responsive't><'row'<'col-md-5 col-12'i><'col-md-7 col-12'p>>",
            buttons: [
                'copy', 'csv', 'print'
            ]
        });
        var tableWrapper = $('#sample_1_wrapper'); // datatable creates the table wrapper by adding with id {your_table_id}_wrapper
        tableWrapper.find('.dataTables_length select').select2(); // initialize select2 dropdown
    }
    // ===============table 1===============
    // ====================table 4===============
    var initTable4 = function() {
        var table = $('#sample_4');

        /* Formatting function for row expanded details */
        function fnFormatDetails(oTable, nTr) {
            var aData = oTable.fnGetData(nTr);
            var sOut = '<table>';
            sOut += '<tr><td>Name:</td><td>' + aData[1] + '</td></tr>';
            sOut += '<tr><td>Age:</td><td>' + aData[2] + '</td></tr>';
            sOut += '<tr><td>Location:</td><td>' + aData[3] + '</td></tr>';
            sOut += '<tr><td>Contact:</td><td>' + aData[4] + '</td></tr>';
            sOut += '<tr><td>Email:</td><td>' + aData[5] + '</td></tr>';
            sOut += '<tr><td>Others:</td><td>Could provide a link here</td></tr>';
            sOut += '</table>';
            return sOut;
        }
        /*
         * Insert a 'details' column to the table
         */
        var nCloneTh = document.createElement('th');
        nCloneTh.className = "table-checkbox";

        var nCloneTd = document.createElement('td');
        nCloneTd.innerHTML = '<span class="row-details row-details-close"></span>';

        table.find('thead tr').each(function() {
            this.insertBefore(nCloneTh, this.childNodes[0]);
        });

        table.find('tbody tr').each(function() {
            this.insertBefore(nCloneTd.cloneNode(true), this.childNodes[0]);
        });

        var oTable = table.dataTable({
            "dom": "<'row'<'col-md-6 col-12'l><'col-md-6 col-12'f>r><'table-responsive't><'row'<'col-md-5 col-12'i><'col-md-7 col-12'p>>", // datatable layout without  horizobtal scroll
            "columnDefs": [{
                "orderable": false,
                "targets": [0]
            }],
            "order": [
                [1, 'asc']
            ],
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5
        });

        var tableWrapper = $('#sample_4_wrapper'); // datatable creates the table wrapper by adding with id {your_table_jd}_wrapper
        var tableColumnToggler = $('#sample_4_column_toggler');

        /* modify datatable control inputs */
        tableWrapper.find('.dataTables_length select').select2(); // initialize select2 dropdown

        /* Add event listener for opening and closing details
         * Note that the indicator for showing which row is open is not controlled by DataTables,
         * rather it is done here
         */
        table.on('click', ' tbody td .row-details', function() {
            var nTr = $(this).parents('tr')[0];
            if (oTable.fnIsOpen(nTr)) {
                /* This row is already open - close it */
                $(this).addClass("row-details-close").removeClass("row-details-open");
                oTable.fnClose(nTr);
            } else {
                /* Open this row */
                $(this).addClass("row-details-open").removeClass("row-details-close");
                oTable.fnOpen(nTr, fnFormatDetails(oTable, nTr), 'details');
            }
            return false;
        });

        /* handle show/hide columns*/
        $('input[type="checkbox"]', tableColumnToggler).on("change",function() {
            /* Get the DataTables object again - this is not a recreation, just a get of the object */
            var iCol = parseInt($(this).attr("data-column"));
            var bVis = oTable.fnSettings().aoColumns[iCol].bVisible;
            oTable.fnSetColumnVis(iCol, (bVis ? false : true));
            return false;
        });
    }
    // =======================table4==================
    // ==================table5===================
    var initTable5 = function() {

        var table = $('#sample_5');

        /* Fixed header extension: http://datatables.net/extensions/scroller/ */

        var oTable = table.dataTable({
            "dom": "<'row'<'col-md-6 col-12'l><'col-md-6 col-12'f>r>t<'row'<'col-md-5 col-12'i><'col-md-7 col-12'p>>", // datatable layout without  horizobtal scroll
            "scrollY": "200",
            "deferRender": true,
            "paging": false,
            "order": [
                [0, 'asc']
            ],
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "All"] // change per page values here
            ],
            "pageLength": 15 // set the initial value
        });


        var tableWrapper = $('#sample_5_wrapper'); // datatable creates the table wrapper by adding with id {your_table_jd}_wrapper
        tableWrapper.find('.dataTables_length select').select2(); // initialize select2 dropdown
    }
    // ===================table 5========================
    // ==================table 6=======================
    var initTable6 = function() {
        var table = $('#sample_6');
        /* Fixed header extension: http://datatables.net/extensions/keytable/ */
        var oTable = table.dataTable({
            "dom": "<'row'<'col-md-6 col-12'l><'col-md-6 col-12'f>r><'table-responsive't><'row'<'col-md-5 col-12'i><'col-md-7 col-12'p>>",
            "order": [
                [0, 'asc']
            ],
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "All"] // change per page values here
            ],
            "pageLength": 5 // set the initial value,
        });
        var oTableColReorder = new $.fn.dataTable.ColReorder(oTable);
        var tableWrapper = $('#sample_6_wrapper'); // datatable creates the table wrapper by adding with id {your_table_jd}_wrapper
        tableWrapper.find('.dataTables_length select').select2(); // initialize select2 dropdown
    }
    var initTable7 = function() {
        var table = $('#row_details');
        /* Fixed header extension: http://datatables.net/extensions/keytable/ */
        var oTable = table.dataTable({
            "dom": "<'row'<'col-md-6 col-12'l><'col-md-6 col-12'f>r><'table-responsive't><'row'<'col-md-5 col-12'i><'col-md-7 col-12'p>>",
            "ordering": false,
            "info": false,
            "searching": false
        });
        var tableWrapper = $('#row_details_wrapper'); // datatable creates the table wrapper by adding with id {your_table_jd}_wrapper
        tableWrapper.find('.dataTables_length select').select2(); // initialize select2 dropdown
    }
    // =====================table 6======================
    return {
        //main function to initiate the module
        init: function() {
            if (!jQuery().dataTable) {
                return;
            }
            initTable1();
            initTable4();
            initTable5();
            initTable6();
            initTable7();
        }
    };
}();

