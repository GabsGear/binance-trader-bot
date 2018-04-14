'use strict';
$(document).ready(function() {
// spark line bar-charts
    $("#sparklinebar").sparkline([7413, 7560, 8000, 7852, 7524, 7142, 7943, 7421, 7743, 7354, 7618, 7390, 7512, 7685, 7835, 7645, 7390], {
        type: 'bar',
        height: '40',
        barWidth: 4,
        barColor: '#4fb7fe',
        barSpacing: 2
    });
    $("#sparklinebar1").sparkline([73, 76, 75, 74, 76, 73, 76, 75, 74, 76, 73, 71, 75, 77, 74, 73, 76], {
        type: 'bar',
        height: '40',
        barWidth: 4,
        barColor: '#d39d5f',
        barSpacing: 2
    });
// end of sparkline charts
//start area chart
    var da1 = [["Jan", 50], ["Feb", 80], ["Mar", 60], ["Apr", 90], ["May", 60], ["Jun", 80], ["Jul", 80]];
    var da2 = [["Jan", 20], ["Feb", 40], ["Mar", 30], ["Apr", 40], ["May", 30], ["Jun", 30], ["Jul", 50]];
    $.plot("#area-chart", [{
        data: da1,
        label: "Product 1",
        color: "#2ca02c"
    }, {
        data: da2,
        label: "product 2",
        color: "#ec6a49"
    }], {
        series: {
            lines: {
                show: !0,
                fill: .8
            },
            points: {
                show: !0,
                radius: 4
            }
        },
        grid: {
            borderColor: "#ddd",
            borderWidth: 1,
            hoverable: !0
        },
        tooltip: !0,
        tooltipOpts: {
            content: "%x : %y",
            defaultTheme: false
        },
        xaxis: {
            tickColor: "#ddd",
            mode: "categories"
        },
        yaxis: {
            tickColor: "#ddd"
        },
        shadowSize: 0
    });
    //end  area chart


    /*server load */
    var data = [],
        totalPoints = 300;

    function getRandomData() {
        if (data.length > 0)
            data = data.slice(1);

        // do a random walk
        while (data.length < totalPoints) {
            var prev = data.length > 0 ? data[data.length - 1] : 50;
            var y = prev + Math.random() * 10 - 5;
            if (y < 0)
                y = 0;
            if (y > 100)
                y = 100;
            data.push(y);
        }

        // zip the generated y values with the x values
        var res = [];
        for (var i = 0; i < data.length; ++i)
            res.push([i, data[i]])
        return res;
    }

    // setup control widget
    var updateInterval = 50;

    // setup plot
    var options = {
        colors: ["#DBDBDB"],
        series: {
            shadowSize: 0,
            lines: {
                show: true,
                fill: true,
                fillColor: {
                    colors: [{
                        opacity: 0.7
                    }, {
                        opacity: 0.7
                    }]
                }
            }
        },
        yaxis: {
            min: 0,
            max: 200

        },
        xaxis: {
            min: 0,
            max: 200
        },
        grid: {
            backgroundColor: '#fff',
            borderWidth: 0,
            borderColor: '#000'
        }
    };

    var plot4 = $.plot($("#chart3"), [getRandomData()], options);

    function update() {
        plot4.setData([getRandomData()]);
        // since the axes don't change, we don't need to call plot.setupGrid()
        plot4.draw();
        setTimeout(update, updateInterval);
    }

    update();


    //donut
    var datax = [{
        label: "Profile",
        data: 50,
        color: '#558000'
    }, {
        label: "Facebook ",
        data: 30,
        color: '#18bc9c'
    }, {
        label: "Twitter ",
        data: 90,
        color: '#0fb0c0'
    }, {
        label: "Google+",
        data: 80,
        color: '#00cc99'
    }, {
        label: "Linkedin",
        data: 110,
        color: '#77b300'
    }];

    $.plot($("#donut"), datax, {
        series: {
            pie: {
                innerRadius: 0.5,
                show: true
            }
        },
        legend: {
            show: false
        },
        grid: {
            hoverable: true
        },
        tooltip: true,
        tooltipOpts: {
            content: "%p.0%, %s"
        }

    });

    /* sparkline chart */
    $("#sparklineline").sparkline([5, 36, 17, 49, 19, 45, 13, 48, 82, 24, 66, 17], {
        type: 'line',
        width: '100%',
        height: '50 ',
        lineColor: '#9678dc',
        fillColor: '#DDD5F0',
        lineWidth: 1,
        spotColor: '#f89a14',
        minSpotColor: '#f89a14',
        maxSpotColor: '#f89a14',
        highlightSpotColor: '#ca0002',
        highlightLineColor: '#F0F0F0',
        drawNormalOnTop: true
    });

    $("#sparklineline2").sparkline([5, 36, 17, 49, 19, 45, 13, 48, 82, 24, 66, 17], {
        type: 'line',
        width: '100%',
        height: '50 ',
        lineColor: '#3498db',
        fillColor: '#C5E5FA',
        lineWidth: 1,
        spotColor: '#f89a14',
        minSpotColor: '#f89a14',
        maxSpotColor: '#f89a14',
        highlightSpotColor: '#ca0002',
        highlightLineColor: '#F0F0F0',
        drawNormalOnTop: true
    });

    var options = {
        useEasing: false,
        useGrouping: false,
        separator: ',',
        decimal: '.'
    }


    // $(function () {
        /* Toastr notifications */

        var i = -1;
        var toastCount = 0;
        var $toastlast;

        var shortCutFunction = "info";
        var msg = "Thanks for checking our theme!";
        var title = "Welcome! <h4>Micheal</h4>";
        var $showDuration = 1000;
        var $hideDuration = 1000;
        var $timeOut = 5000;
        var $extendedTimeOut = 1000;
        var $showEasing = "swing";
        var $hideEasing = "linear";
        var $showMethod = "fadeIn";
        var $hideMethod = "fadeOut";
        var toastIndex = toastCount++;
        toastr.options = {
            closeButton: $('#closeButton').prop('checked'),
            debug: $('#debugInfo').prop('checked'),
            positionClass: 'toast-top-right',
            onclick: null
        };
        if ($('#addBehaviorOnToastClick').prop('checked')) {
            toastr.options.onclick = function () {
                alert('You can perform some custom action after a toast goes away');
            };
        }
        if ($showDuration.length) {
            toastr.options.showDuration = $showDuration;
        }
        if ($hideDuration.length) {
            toastr.options.hideDuration = $hideDuration;
        }
        if ($timeOut.length) {
            toastr.options.timeOut = $timeOut;
        }
        if ($extendedTimeOut.length) {
            toastr.options.extendedTimeOut = $extendedTimeOut;
        }
        if ($showEasing.length) {
            toastr.options.showEasing = $showEasing;
        }
        if ($hideEasing.length) {
            toastr.options.hideEasing = $hideEasing;
        }
        if ($showMethod.length) {
            toastr.options.showMethod = $showMethod;
        }
        if ($hideMethod.length) {
            toastr.options.hideMethod = $hideMethod;
        }
        $("#toastrOptions").text("Command: toastr[" + shortCutFunction + "](\"" + msg + (title ? "\", \"" + title : '') + "\")\n\ntoastr.options = " + JSON.stringify(toastr.options, null, 2));
        var $toast = toastr[shortCutFunction](msg, title); // Wire up an event handler to a button in the toast, if it exists
        $toastlast = $toast;

    // });
});