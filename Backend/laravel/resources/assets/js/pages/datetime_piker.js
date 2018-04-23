'use strict';
$(document).ready(function () {
    Admire.formGeneral();

    // Date picker
    $('#dp1').datepicker({
        format: 'dd-mm-yyyy',
        todayHighlight: true,
        autoclose: true,
        orientation:"bottom"
    });
    $('#dp2').datepicker({
        todayHighlight: true,
        autoclose: true,
        orientation:"bottom"
    });
    $('#dp3').datepicker({
        todayHighlight: true,
        autoclose: true,
        orientation:"bottom"
    });
    $("#dtBox").DateTimePicker();
    $('#dpYears').datepicker({
        todayHighlight: true,
        autoclose: true,
        orientation:"bottom"
    });
    $('#dpMonths').datepicker({
        todayHighlight: true,
        autoclose: true,
        startView: "months",
        minViewMode: "months",
        orientation:"bottom"
    });
    // End of datepicker

    // Date range picker
    $('#date_range').daterangepicker({
        autoUpdateInput: false,
        locale: {
            cancelLabel: 'Clear'
        }
    });
    $('#date_range').on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format('MM/DD/YYYY') + ' - ' + picker.endDate.format('MM/DD/YYYY'));
        return false;
    });

    $('#date_range').on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
        return false;
    });
    $('#reservation').daterangepicker({
        autoUpdateInput: false,
        locale: {
            cancelLabel: 'Clear'
        }
    });

    $('#reservation').on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
        return false;
    });

    $('#reservation').on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
        return false;
    });
    $('#reportrange').daterangepicker({
            autoUpdateInput: false,
            locale: {
                cancelLabel: 'Clear'
            },
            ranges: {
                'Today': [moment(), moment()],
                'Yesterday': [moment().subtract('days', 1), moment().subtract('days', 1)],
                'Last 7 Days': [moment().subtract('days', 6), moment()],
                'Last 30 Days': [moment().subtract('days', 29), moment()],
                'This Month': [moment().startOf('month'), moment().endOf('month')],
                'Last Month': [moment().subtract('month', 1).startOf('month'), moment().subtract('month', 1).endOf('month')]
            }
        },
        function(start, end) {
            $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        });
    $('#reportrange').on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
        return false;
    });

    $('#reportrange').on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
        return false;
    });
    // End of date range picker
    // Color picker
    $('#cp1').colorpicker({
        format: 'hex'
    });
    $('#cp-2').colorpicker({
        format:'rgba',
        align:'top'
    });
    $('#cp3').colorpicker();
    $('#cp4').colorpicker().on('changeColor', function(ev) {
        $('#colorPickerBlock').css('background-color', ev.color.toHex());
        return false;
    });
    $("#cp4").on("click",function () {
        $("#cp4").css('color','#fff');
        return false;
    });
    // End of color picker

    // Time picker
    $('#timepicker_default').timepicker();
    $('#basic_time_picker').timepicker();
    $('#setTimeExample').timepicker();
    $('#setTimeButton').on('click', function (){
        $('#setTimeExample').timepicker('setTime', new Date());
        $('#setTimeButton').css('color','#fff');
    });
    // End of time picker

    // Clockpicker
    $('.clockpicker1').clockpicker({
        donetext: 'Done',
        placement: 'top'
    });
    $('.clockpicker2').clockpicker();
    var input = $('#single_input1').clockpicker({
        align: 'left',
        autoclose: true,
        'default': 'now'
    });
    $('#check_minutes').on("click",function(e){
        e.stopPropagation();
        input.clockpicker('show')
            .clockpicker('toggleView', 'minutes');
        $('#check_minutes').css('color','#fff');
    });
    $('#single_input2').clockpicker({
        donetext: 'Done'
    });
    // End of clock picker

});