'use strict';
$(document).ready(function () {
    $(".select_all_mail").on("change",function () {
        $(".mail_sent_all tr td [type='checkbox']").prop('checked', $(this).prop("checked"));
        if ($(this).prop("checked")) {
            $(".mail_sent_all table tr").addClass("mail_tr_background");
        } else {
            $(".mail_sent_all table tr").removeClass("mail_tr_background");
        }
    });
    $("#primary2,#social2,#promotions2").on('click', function () {
        $("input:checkbox").prop('checked', false);
        $(".mail_sent_all table tr").removeClass("mail_tr_background");
    });
    $(".select-all1").on('click', function () {
        $(".select_all_mail").prop('checked', true);
        $(".mail_sent_all tr td [type='checkbox']").prop('checked', true);
        $(".mail_sent_all table tr").addClass("mail_tr_background");
    });
    $("#select-none").on('click', function () {
        $("input:checkbox").prop('checked', false);
        $(".mail_sent_all table tr").removeClass("mail_tr_background")
    });
    $('.mail_sent_all tr td [type="checkbox"]').on('change', function () {
        var chkall=0;
        $(this).closest('tr').toggleClass("mail_tr_background");
        $('.mail_sent_all tr td [type="checkbox"]').each(function () {
            if ($(this).prop("checked")) {
            } else {
                chkall=1;
                return;
            }
        });
        if(chkall==1){
            $(".select_all_mail").prop("checked", false);
        }else{
            $(".select_all_mail").prop("checked", true);
        }
    });
    $("#refresh_sent").on('click', function () {
        $(location).attr('href', 'mail_sent.html');
        return false;
    });
    $("#refresh_spam").on('click', function () {
        $(location).attr('href', 'mail_spam.html');
        return false;
    });
    $("#refresh_trash").on('click', function () {
        $(location).attr('href', 'mail_trash.html');
        return false;
    });
    $("#refresh_draft").on('click', function () {
        $(location).attr('href', 'mail_draft.html');
        return false;
    });
    $('.mail tr td .fa-star').on('click', function () {
        $(this).toggleClass("text-warning");
        return false;
    });
    $('.contact_scroll').css('height',480);
    $('.contact_scroll').jScrollPane({
        autoReinitialise: true,
        autoReinitialiseDelay: 100
    });
    $(".starred_mail").hide();
    $("#more_items").on('click',function () {
        $(".starred_mail").slideToggle();
        $("#more_items").find('.fa-angle-down,.fa-angle-up').toggleClass("fa-angle-up").toggleClass("fa-angle-down");
        return false;
    });
});
