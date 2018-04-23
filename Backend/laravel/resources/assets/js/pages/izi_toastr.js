"use strict";
$(document).ready(function () {
    $("#title").on("click",function () {
        iziToast.show({
            title: 'title'
        });
        return false;
    });
    $("#message").on("click",function () {
        iziToast.show({
            message: 'message',
            rtl:true
        });
        return false;
    });
    $("#basic").on("click",function () {
        iziToast.show({
            title: 'Hey',
            message: 'What would you like to add?',
            position: 'bottomLeft'
        });
        return false;
    });
    $("#btn_info").on("click",function () {
        iziToast.info({
            title: 'Hello',
            message: 'Welcome!',
            position: 'bottomLeft',
            rtl:true
        });
        return false;
    });
    $("#btn_success").on("click",function () {
        iziToast.success({
            title: 'OK',
            message: 'Successfully inserted record!',
            position: 'bottomCenter'
        });
        return false;
    });
    $("#btn_warning").on("click",function () {
        iziToast.warning({
            title: 'Caution',
            message: 'You forgot important data'
        });
        return false;
    });
    $("#btn_error").on("click",function () {
        iziToast.error({
            title: 'Error',
            message: 'Illegal operation',
            position: 'topCenter'
        });
        return false;
    });
    $("#btn_show").on("click",function () {
        iziToast.show({
            color: 'dark',
            icon: 'fa fa-user',
            title: 'Hey',
            message: 'Welcome!',
            position: 'center',
            progressBarColor: 'rgb(0, 255, 184)',
            buttons: [
                ['<button>Ok</button>', function (instance, toast) {
                    alert("Hello world!");
                }],
                ['<button>Close</button>', function (instance, toast) {
                    instance.hide({ transitionOut: 'fadeOutUp' }, toast);
                }]
            ]
        });
        return false;
    });
    $("#alert_primary").on("click",function () {
        iziToast.show({
            title: 'Primary',
            message: 'What would you like to add?',
            color:'#4fb7fe'
        });
        return false;
    });
    $("#alert_success").on("click",function () {
        iziToast.show({
            title: 'Success',
            message: 'What would you like to add?',
            color:'#00cc99',
            position: 'bottomCenter'
        });
        return false;
    });
    $("#alert_info").on("click",function () {
        iziToast.show({
            title: 'Info',
            message: 'What would you like to add?',
            color:'#347dff',
            position: 'bottomLeft'
        });
        return false;
    });
    $("#alert_warning").on("click",function () {
        iziToast.show({
            title: 'Warning',
            message: 'What would you like to add?',
            color:'#ff9933',
            position: 'topLeft'
        });
        return false;
    });
    $("#alert_danger").on("click",function () {
        iziToast.show({
            title: 'Danger',
            message: 'What would you like to add?',
            color:'#ff6666',
            position: 'topCenter'
        });
        return false;
    });
    $("#alert_mint").on("click",function () {
        iziToast.show({
            title: 'Mint',
            message: 'What would you like to add?',
            color:'#0fb0c0',
            position: 'topRight'
        });
        return false;
    });
    $("#font_icon").on("click",function () {
        iziToast.show({
            icon:'fa fa-user',
            title:'Icon'
        });
        return false;
    });
    $("#icon_color").on("click",function () {
        iziToast.show({
            title:'Icon color',
            message:'Showing icon color',
            icon:'fa fa-user',
            iconColor:'#4fb7fe',
            position:'topLeft'
        });
        return false;
    });
    $("#toast_image").on("click",function () {
        iziToast.show({
            title:'Image',
            message:'Showing image',
            image:'img/admin.jpg',
            position:'topRight'
        });
        return false;
    });
    $("#image_width").on("click",function () {
        iziToast.show({
            title:'Image Width',
            message:'Showing image width',
            image:'img/admin.jpg',
            imageWidth:100,
            position:'bottomLeft',
            layout:'2'
        });
        return false;
    });
    $("#zindex").on("click",function () {
        iziToast.show({
            title:'Zindex',
            message:'Showing zindex of toastr',
            zindex:999
        });
        return false;
    });
    $("#layout1").on("click",function () {
        iziToast.show({
            title:'Layout small',
            message:'Showing small layout of toastr',
            layout:1,
            position:'center'
        });
        return false;
    });
    $("#layout2").on("click",function () {
        iziToast.show({
            title:'Layout medium',
            message:'Showing medium layout of toastr',
            layout:2,
            position:'topCenter'
        });
        return false;
    });
    $("#balloon").on("click",function () {
        iziToast.show({
            title:'balloon',
            message:'Showing balloon of toastr',
            position:'topLeft',
            balloon:true
        });
        return false;
    });
    $("#close_false").on("click",function () {
        iziToast.show({
            title:'Not closed',
            message:'Showing toast does not close',
            close:false,
            position:'bottomLeft'
        });
        return false;
    });
    $("#rtl").on("click",function () {
        iziToast.show({
            title:'Rtl',
            message:'Right to left toastr',
            rtl:true,
            position:'topRight'
        });
        return false;
    });
    $("#center").on("click",function () {
        iziToast.show({
            title:'center',
            message:'Showing the toastr in center',
            position: 'center'
        });
        return false;
    });
    $("#bottomLeft").on("click",function () {
        iziToast.show({
            title:'bottomLeft',
            message:'Showing the toastr in bottom left',
            position: 'bottomLeft'
        });
        return false;
    });
    $("#bottomRight").on("click",function () {
        iziToast.show({
            title:'bottomRight',
            message:'Showing the toastr in bottom right',
            position: 'bottomRight'
        });
        return false;
    });
    $("#topLeft").on("click",function () {
        iziToast.show({
            title:'topLeft',
            message:'Showing the toastr in top left',
            position: 'topLeft'
        });
        return false;
    });
    $("#top_right").on("click",function () {
        iziToast.show({
            title:'Top right',
            message:'Showing the toastr in top right',
            position: 'topRight'
        });
        return false;
    });
    $("#center_bottom").on("click",function () {
        iziToast.show({
            title:'Center bottom',
            message:'Showing the toastr in center bottom',
            position: 'bottomCenter'
        });
        return false;
    });
    $("#center_top").on("click",function () {
        iziToast.show({
            title:'Center top',
            message:'Showing the toastr in center top',
            position: 'topCenter'
        });
        return false;
    });
    $("#target").on("click",function () {
        iziToast.show({
            title:'Target',
            message:'Showing the toastr target',
            target: '.target_section'
        });
        return false;
    });
    $("#timeout").on("click",function () {
        iziToast.show({
            title:'Timeout',
            message:'Toastr timeout set to 100000',
            timeout:100000,
            position:'topCenter'
        });
        return false;
    });
    $("#pauseon_hover").on("click",function () {
        iziToast.show({
            title:'Pause on hover',
            message:'When you hovered on toastr progressbar stops',
            pauseOnHover: true,
            position:'topRight'
        });
        return false;
    });
    $("#reset_hover").on("click",function () {
        iziToast.show({
            title:'reset on hover',
            message:'When you hovered on toastr progressbar resets',
            resetOnHover: true,
            position:'topLeft'
        });
        return false;
    });
    $("#progress_bar").on("click",function () {
        iziToast.show({
            title:'Without Progressbar',
            message:'Toastr without progressbar',
            progressBar: false
        });
        return false;
    });
    $("#progress_bar_color").on("click",function () {
        iziToast.show({
            title:'Progressbar with color',
            message:'Showing toastr with colored progressbar',
            progressBarColor: '#4fb7fe',
            position:'bottomCenter'
        });
        return false;
    });
    $("#animate_inside").on("click",function () {
        iziToast.show({
            title:'Animate',
            message:'Toastr with inside animation',
            animateInside: true,
            position:'bottomLeft'
        });
        return false;
    });
    $("#animate_inside_false").on("click",function () {
        iziToast.show({
            title:'Animate',
            message:'Toastr without inside animation',
            animateInside: false,
            position:'center'
        });
        return false;
    });
    $("#buttons").on("click",function () {
        iziToast.show({
            title:'Buttons',
            message:'Showing toastr with buttons',
            position:'topLeft',
            buttons: [
                ['<button>Photo</button>', function (instance, toast) {

                }],
                ['<button>Video</button>', function (instance, toast) {

                }],
                ['<button>Text</button>', function (instance, toast) {

                }],
            ]
        });
        return false;
    });
    $("#fadeIn").on("click",function () {
        iziToast.show({
            title:'fadeIn',
            message:'Showing toastr with fadeIn',
            transitionIn: 'fadeIn',
            position:'center'
        });
        return false;
    });
    $("#fadeInUp").on("click",function () {
        iziToast.show({
            title:'fadeInUp',
            message:'Showing toastr with fadeInUp',
            transitionIn: 'fadeInUp',
            position:'topCenter'
        });
        return false;
    });
    $("#fadeInDown").on("click",function () {
        iziToast.show({
            title:'fadeInDown',
            message:'Showing toastr with fadeInDown',
            transitionIn: 'fadeInDown',
            position:'bottomCenter'
        });
        return false;
    });
    $("#fadeInLeft").on("click",function () {
        iziToast.show({
            title:'fadeInLeft',
            message:'Showing toastr with fadeInLeft',
            transitionIn: 'fadeInLeft',
            position:'bottomLeft'
        });
        return false;
    });
    $("#fadeInRight").on("click",function () {
        iziToast.show({
            title:'fadeInRight',
            message:'Showing toastr with fadeInRight',
            transitionIn: 'fadeInRight',
            position:'bottomRight'
        });
        return false;
    });
    $("#bounceInUp").on("click",function () {
        iziToast.show({
            title:'bounceInUp',
            message:'Showing toastr with bounceInUp',
            transitionIn: 'bounceInUp',
            position:'topCenter'
        });
        return false;
    });
    $("#bounceInDown").on("click",function () {
        iziToast.show({
            title:'bounceInDown',
            message:'Showing toastr with bounceInDown',
            transitionIn: 'bounceInDown',
            position:'bottomCenter'
        });
        return false;
    });
    $("#bounceInLeft").on("click",function () {
        iziToast.show({
            title:'bounceInLeft',
            message:'Showing toastr with bounceInLeft',
            transitionIn: 'bounceInLeft',
            position:'topLeft'
        });
        return false;
    });
    $("#bounceInRight").on("click",function () {
        iziToast.show({
            title:'bounceInRight',
            message:'Showing toastr with bounceInRight',
            transitionIn: 'bounceInRight',
            position:'topRight'
        });
        return false;
    });
    $("#fadeOut").on("click",function () {
        iziToast.show({
            title:'fadeOut',
            message:'Showing toastr with fadeOut',
            transitionOut: 'fadeOut',
            position:'center',
            balloon:true
        });
        return false;
    });
    $("#fadeOutUp").on("click",function () {
        iziToast.show({
            title:'fadeOutUp',
            message:'Showing toastr with fadeOutUp',
            transitionOut: 'fadeOutUp',
            position:'topCenter',
            balloon:true
        });
        return false;
    });
    $("#fadeOutDown").on("click",function () {
        iziToast.show({
            title:'fadeOutDown',
            message:'Showing toastr with fadeOutDown',
            transitionOut: 'fadeOutDown',
            position:'bottomCenter',
            balloon:true
        });
        return false;
    });
    $("#fadeOutLeft").on("click",function () {
        iziToast.show({
            title:'fadeOutLeft',
            message:'Showing toastr with fadeOutLeft',
            transitionOut: 'fadeOutLeft',
            position:'topLeft',
            balloon:true
        });
        return false;
    });
    $("#fadeOutRight").on("click",function () {
        iziToast.show({
            title:'fadeOutRight',
            message:'Showing toastr with fadeOutRight',
            transitionOut: 'fadeOutRight',
            balloon:true
        });
        return false;
    });
});