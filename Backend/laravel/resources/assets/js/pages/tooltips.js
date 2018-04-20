"use strict";
$(document).ready(function () {
    $('[data-toggle="popover"]').popover();

//        Advanced tooltips
    $(".tipso").tipso();
    $(".tipso_tiny").tipso({
        size:'tiny'
    });
    $(".tipso_small").tipso({
        size:'small'
    });
    $(".tipso_default").tipso();
    $(".tipso_large").tipso({
        size:'large'
    });
    $(".tipso_pageload").tipso("show");
    $('.hover-tipso-tooltip').tipso({
        tooltipHover: true
    });
    $('.update-tipso').on('click', function(e){
        $('.update').tipso('update', 'content', 'This is updated tooltip');
        e.preventDefault();
    });
    $('.update-tipso-input').on('click', function(e){
        var content = $('.tipso-content').val();
        $('.update-tipso-content').tipso('update', 'content', content);
        e.preventDefault();
    });
    $(".tipso_fadeIn").tipso({
        animationIn: 'fadeIn',
        animationOut: 'fadeOut'
    });
    $(".tipso_fadeInDown").tipso({
        animationIn: 'fadeInDown',
        animationOut: 'fadeOutUp'
    });
    $(".tipso_fadeInLeft").tipso({
        animationIn: 'fadeInLeft',
        animationOut: 'fadeOutRight'
    });
    $(".tipso_fadeInRightBig").tipso({
        animationIn: 'fadeInRightBig',
        animationOut: 'fadeOutLeftBig'
    });
    $(".tipso_bounceIn").tipso({
        animationIn: 'bounceIn',
        animationOut: 'bounceOut'
    });
    $(".tipso_bounceInDown").tipso({
        animationIn: 'bounceInDown',
        animationOut: 'bounceOutUp'
    });
    $(".tipso_bounceInLeft").tipso({
        animationIn: 'bounceInLeft',
        animationOut: 'bounceOutRight'
    });
    $(".tipso_zoomIn").tipso({
        animationIn: 'zoomIn',
        animationOut: 'zoomOut'
    });
    $(".tipso_zoomInDown").tipso({
        animationIn: 'zoomInDown',
        animationOut: 'zoomOutUp'
    });
    $(".tipso_hinge").tipso({
        animationIn: 'hinge',
        animationOut: 'rollOut'
    });
    $(".tipso_lightSpeedIn").tipso({
        animationIn: 'lightSpeedIn',
        animationOut: 'lightSpeedOut'
    });
    $(".tipso_flipInX").tipso({
        animationIn: 'flipInX',
        animationOut: 'flipOutY'
    });
    $(".tipso_rubberBand").tipso({
        animationIn: 'rubberBand',
        animationOut: 'wobble'
    });
});