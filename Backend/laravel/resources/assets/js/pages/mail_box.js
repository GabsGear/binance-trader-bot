'use strict';
$(document).ready(function () {
    // =====================Mail Inbox===================
    $('#inbox_leftmenu').delay(9000).addClass('sidebar-left-hidden');
    $('.custom-control-input').hide();
    $(".select-all").on("change",function () {
        $(".mail tr td [type='checkbox']").prop('checked', $(this).prop("checked"));
        if ($(this).prop("checked")) {
            $(".mail .tab-content .active table tr").addClass("mail_tr_background");
        } else {
            $(".mail .tab-content .active table tr").removeClass("mail_tr_background");
        }
        return false;
    });
    $("#primary2,#social2,#promotions2").on('click', function () {
        $("input:checkbox").prop('checked', false);
        $(".mail .tab-content .active table tr").removeClass("mail_tr_background");
    });
    $(".select-all1,.select-all1 span").on('click', function () {
        $(".select-all").prop('checked', true);
        $(".mail tr td [type='checkbox']").prop('checked', true);
        $(".mail .tab-content .active table tr").addClass("mail_tr_background");
    });
    $("#select-none").on('click', function () {
        $("input:checkbox").prop('checked', false);
        $(".mail .tab-content .active table tr").removeClass("mail_tr_background")
    });
    $('.mail tr td [type="checkbox"]').on('change', function () {
        var chkall=0;
        $(this).closest('tr').toggleClass("mail_tr_background");
        $('.mail tr td [type="checkbox"]').each(function () {
            if ($(this).prop("checked")) {
            } else {
                chkall=1;
                return;
            }
        });
        if(chkall==1){
            $(".select-all").prop("checked", false);
        }else{
            $(".select-all").prop("checked", true);
        }
    });
    $("#refresh_inbox").on('click', function () {
        $(location).attr('href', 'mail_inbox');
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
    });
    $(".sent_to_mailview").on("click",function () {
        $(location).attr('href','mail_view');
        return false;
    });
    // ===================Mail Compose==================

    $(".mail_compose_wysi textarea").wysihtml5();
    $(".mail_view_wysi textarea").wysihtml5();
    $(".wysihtml5-toolbar .btn-group:eq(1) a:first-child").addClass("fa fa-list");
    $(".wysihtml5-toolbar .btn-group:eq(1) a:nth-child(2)").addClass("fa fa-th-list");
    $(".wysihtml5-toolbar .btn-group:eq(1) a:nth-child(3)").addClass("fa fa-align-left");
    $(".wysihtml5-toolbar .btn-group:eq(1) a:nth-child(4)").addClass("fa fa-align-right");
    $(".wysihtml5-toolbar li:nth-child(5) span").addClass("fa fa-share");
    $(".wysihtml5-toolbar li:nth-child(6) span").addClass("fa fa-picture-o");
    $(".wysihtml5-toolbar li:first-child a:first-child").removeClass('btn-default').addClass('btn-secondary');
    $(".wysihtml5-toolbar li:nth-child(2) a,.wysihtml5-toolbar li:nth-child(3) a,.wysihtml5-toolbar li:nth-child(4) a,.wysihtml5-toolbar li:nth-child(5) a,.wysihtml5-toolbar li:nth-child(6) a").removeClass('btn-default').addClass('btn-secondary');
    $("[data-wysihtml5-command='formatBlock'] span").removeClass("glyphicon glyphicon-quote").addClass("fa fa-quote-left");
    // ====================Mail View===========================
    $(".mail_view_wysi").hide();
    $("#view_reply1").on('click',function () {
        $("#forward_to,#view_reply2,#view_reply3").hide();
        $(this).hide();
        $(".mail_view_wysi").show();
        return false;
    });
    $("#view_reply2").on('click',function () {
        $("#view_reply1,#view_reply2,#view_reply3").hide();
        $(".mail_view_wysi").show();
        return false;
    });
    $("#view_reply1").on("click",function () {
        $("#goto_sent_page").on("click",function () {
            $(location).attr("href","mail_sent");
            return false;
        })
    });
});