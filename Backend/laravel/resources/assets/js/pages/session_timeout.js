'use strict';
jQuery(document).ready(function() {
    // initialize session timeout settings
    $.sessionTimeout({
        title: 'Session Timeout Notification',
        message: 'Your session is about to expire.',
        keepAliveUrl: 'session_timeout.php',
        redirUrl: 'lockscreen.php',
        logoutUrl: 'login.php',
        warnAfter: 5000, //warn after 5 seconds
        redirAfter: 10000 //redirect after 10 secons
    });
});