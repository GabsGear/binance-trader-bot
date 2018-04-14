"use strict";
$(document).ready(function() {
    $("#visitsspark-chart").sparkline([209, 210, 209, 210, 210, 211, 212, 210, 210, 211, 213, 212, 211, 210, 212, 211, 210, 212], {
        type: 'line',
        width: '100%',
        height: '48',
        lineColor: '#4fb7fe',
        fillColor: '#e7f5ff',
        tooltipSuffix: 'Users'
    });
    function spark_sales() {
        var barParentdiv = $('#salesspark-chart').closest('div');
        var barCount = [209, 210, 209, 210, 210, 211, 212, 210, 210, 211, 213, 212, 211, 210, 212, 211, 210, 212];
        var barSpacing = 2;
        $("#salesspark-chart").sparkline(barCount, {
            type: 'bar',
            width: '100%',
            barWidth: (barParentdiv.width() - (barCount.length * barSpacing)) / barCount.length,
            height: '48',
            barSpacing: barSpacing,
            barColor: '#9bd5ff',
            tooltipSuffix: ' Sales'
        });
        $('#salesspark-chart').sparkline([209, 210, 209, 210, 210, 211, 212, 210, 210, 211, 213, 212, 211, 210, 212, 211, 210, 212],
            {
                composite: true,
                fillColor: false,
                width: "100%",
                spotColor: '#f0ad4e',
                lineColor: '#EF6F6C',
                tooltipSuffix: ' Sales'
            });

    }

    spark_sales();


    function spark_loader() {
        var lpoints = [];
        for (var i = 0; i < 20; i++) {
            var load = 5 + parseInt(Math.random() * 90 - 5);
            if (load < 25) {
                load = 25;
            }
            if (load > 100) {
                load = 90;
            }
            lpoints.push(load);
        }
        $('#mousespeed').sparkline(lpoints, {
            type: 'line',
            height: "48px",
            width: "100%",
            lineColor: '#4fb7fe',
            fillColor: '#e7f5ff',
            tooltipSuffix: ' Comments'
        });
        setTimeout(spark_loader, 1800);
    }

    spark_loader();


    function spark_sales1() {
        var barParentdiv = $('#rating').closest('div');
        var barCount = [1, 2, 3, 2, 5, 3, 5, 6, 5, 6, 5, 7, 8, 8, 6, 7, 4, 3, 5, 4, 2, 3, 5, 3, 2, 1];
        var barSpacing = 2;
        $("#rating").sparkline(barCount, {
            type: 'bar',
            width: '100%',
            barWidth: (barParentdiv.width() - (barCount.length * barSpacing)) / barCount.length,
            height: '50',
            barSpacing: barSpacing,
            barColor: '#9bd5ff',
            tooltipSuffix: ' Rating'
        });
    }

    spark_sales1();

//   flip js

    $("#top_widget1, #top_widget2, #top_widget3, #top_widget4").flip({
        axis: 'x',
        trigger: 'hover'
    });


    var options = {
        useEasing: true,
        useGrouping: true,
        decimal: '.',
        prefix: '',
        suffix: ''
    };
    new CountUp("widget_countup1", 0, 3250, 0, 5.0, options).start();
    new CountUp("widget_countup2", 0, 1140, 0, 5.0, options).start();
    new CountUp("widget_countup3", 0, 85, 0, 7.0, options).start();
    new CountUp("widget_countup4", 0, 8, 0, 9.0, options).start();


//=================================main chart================================

// Chartist
    var Chartist1 = new Chartist.Line('#chart1', {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        series: [{
            label: 'Views',
            data: [{meta: 'Views', value: 4},
                {meta: 'Views', value: 6},
                {meta: 'Views', value: 4},
                {meta: 'Views', value: 7},
                {meta: 'Views', value: 4},
                {meta: 'Views', value: 6},
                {meta: 'Views', value: 3},
                {meta: 'Views', value: 7},
                {meta: 'Views', value: 3},
                {meta: 'Views', value: 6},

                {meta: 'Views', value: 4},
                {meta: 'Views', value: 6}]
        },

            {
                label: 'Sales',
                data: [{meta: 'Sales', value: 1},
                    {meta: 'Sales', value: 3},
                    {meta: 'Sales', value: 1},
                    {meta: 'Sales', value: 4},
                    {meta: 'Sales', value: 1},
                    {meta: 'Sales', value: 3},
                    {meta: 'Sales', value: 1},
                    {meta: 'Sales', value: 3},
                    {meta: 'Sales', value: 1},
                    {meta: 'Sales', value: 4},
                    {meta: 'Sales', value: 1},
                    {meta: 'Sales', value: 3}]
            }]
    }, {
        height: 300,
        fullWidth: true,
        low: 0,
        high: 7,
        showArea: true,
        axisY: {
            onlyInteger: true,
            offset: 20
        }
        ,
        plugins: [
            Chartist.plugins.tooltip()
        ]
    });

    Chartist1.on('draw', function (data) {


        if (data.type === 'point') {
            data.element.animate({
                y1: {
                    begin: 100 * data.index,
                    dur: 2000,
                    from: data.y + 1000,
                    to: data.y,
                    easing: Chartist.Svg.Easing.easeOutQuint
                },
                y2: {
                    begin: 100 * data.index,
                    dur: 2000,
                    from: data.y + 1000,
                    to: data.y,
                    easing: Chartist.Svg.Easing.easeOutQuint
                }
            });
        }

        if (data.type === 'line' || data.type === 'area') {
            data.element.animate({
                d: {
                    begin: 2000 * data.index,
                    dur: 2000,
                    from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
                    to: data.path.clone().stringify(),
                    easing: Chartist.Svg.Easing.easeOutQuint
                }
            });
        }
    });


//===============================coding docs desingi=====================================

    $('#myStat').circliful({
        animationStep: 5,
        fillColor: '#4fb7fe',
        foregroundBorderWidth: 5,
        percent: 40
    });
    $('#myStat2').circliful({
        animationStep: 5,
        fillColor: '#00cc99',
        foregroundBorderWidth: 5,
        percent: 60
    });
    $('#myStat3').circliful({
        animationStep: 5,
        fillColor: '#ff9933',
        foregroundBorderWidth: 5,
        percent: 75
    });


    //server load
    var flot2 = function() {
        // We use an inline data source in the example, usually data would
        // be fetched from a server
        var data = [],
            totalPoints = 100;

        function getRandomData() {
            if (data.length > 0)
                data = data.slice(1);
            // Do a random walk
            while (data.length < totalPoints) {
                var prev = data.length > 0 ? data[data.length - 1] : 50,
                    y = prev + Math.random() * 10 - 5;
                if (y < 0) {
                    y = 0;
                } else if (y > 100) {
                    y = 100;
                }
                data.push(y);
            }
            // Zip the generated y values with the x values
            var res = [];
            for (var i = 0; i < data.length; ++i) {
                res.push([i, data[i]])
            }
            return res;
        }
        var plot2 = $.plot("#order_realtime", [getRandomData()], {
            series: {
                shadowSize: 0 // Drawing is faster without shadows
            },
            yaxis: {
                min: 0,
                max: 100
            },
            xaxis: {
                show: false
            },
            colors: ["#22BAA0"],
            legend: {
                show: false
            },
            grid: {
                color: "#AFAFAF",
                hoverable: true,
                borderWidth: 0,
                backgroundColor: '#FFF'},
            tooltip: true,
            tooltipOpts: {
                content: "Y: %y",
                defaultTheme: false
            }
        });

        function update() {
            plot2.setData([getRandomData()]);
            plot2.draw();
            setTimeout(update, 30);
        }
        update();
    };
    flot2();



    //server load
    var flot3 = function() {
        // We use an inline data source in the example, usually data would
        // be fetched from a server
        var data = [],
            totalPoints = 100;

        function getRandomData() {
            if (data.length > 0)
                data = data.slice(1);
            // Do a random walk
            while (data.length < totalPoints) {
                var prev = data.length > 0 ? data[data.length - 1] : 50,
                    y = prev + Math.random() * 10 - 5;
                if (y < 0) {
                    y = 0;
                } else if (y > 100) {
                    y = 100;
                }
                data.push(y);
            }
            // Zip the generated y values with the x values
            var res = [];
            for (var i = 0; i < data.length; ++i) {
                res.push([i, data[i]])
            }
            return res;
        }
        var plot3 = $.plot("#sale_realtime", [getRandomData()], {
            series: {
                shadowSize: 0 // Drawing is faster without shadows
            },
            yaxis: {
                min: 0,
                max: 100
            },
            xaxis: {
                show: false
            },
            colors: ["#4fb7fe"],
            legend: {
                show: false
            },
            grid: {
                color: "#AFAFAF",
                hoverable: true,
                borderWidth: 0,
                backgroundColor: '#FFF'},
            tooltip: true,
            tooltipOpts: {
                content: "Y: %y",
                defaultTheme: false
            }
        });

        function update() {
            plot3.setData([getRandomData()]);
            plot3.draw();
            setTimeout(update, 30);
        }
        update();
    };
    flot3();




    //server load
    var flot4 = function() {
        // We use an inline data source in the example, usually data would
        // be fetched from a server
        var data = [],
            totalPoints = 100;

        function getRandomData() {
            if (data.length > 0)
                data = data.slice(1);
            // Do a random walk
            while (data.length < totalPoints) {
                var prev = data.length > 0 ? data[data.length - 1] : 50,
                    y = prev + Math.random() * 10 - 5;
                if (y < 0) {
                    y = 0;
                } else if (y > 100) {
                    y = 100;
                }
                data.push(y);
            }
            // Zip the generated y values with the x values
            var res = [];
            for (var i = 0; i < data.length; ++i) {
                res.push([i, data[i]])
            }
            return res;
        }
        var plot4 = $.plot("#users_realtime", [getRandomData()], {
            series: {
                shadowSize: 0 // Drawing is faster without shadows
            },
            yaxis: {
                min: 0,
                max: 100
            },
            xaxis: {
                show: false
            },
            colors: ["#ff9933"],
            legend: {
                show: false
            },
            grid: {
                color: "#AFAFAF",
                hoverable: true,
                borderWidth: 0,
                backgroundColor: '#FFF'},
            tooltip: true,
            tooltipOpts: {
                content: "Y: %y",
                defaultTheme: false
            }
        });

        function update() {
            plot4.setData([getRandomData()]);
            plot4.draw();
            setTimeout(update, 30);
        }
        update();
    };
    flot4();
    // ==================================monthly up laod=================================

    $("#test-circle").circliful({
        animation: 1,
        animationStep: 1,
        foregroundBorderWidth: 15,
        backgroundBorderWidth: 15,
        percent: 75,
        textSize: 28,
        textStyle: 'font-size: 12px;',
        textColor: '#666',
        multiPercentage: 1,
        percentages: [10, 20, 30]
    });

    function spark_sales_upload() {
        var barParentdiv = $('#monthly_upload').closest('div');
        var barCount = [71, 72, 73, 72, 75, 73, 75, 76, 75, 76, 75, 77, 78, 78, 76, 77, 74, 73, 75, 74, 72, 73, 75, 74, 73, 72, 71];
        var barSpacing = 2;
        $("#monthly_upload").sparkline(barCount, {
            type: 'bar',
            width: '100%',
            barWidth: (barParentdiv.width() - (barCount.length * barSpacing)) / barCount.length,
            height: '50',
            barSpacing: barSpacing,
            barColor: '#4FB7FE',
            tooltipSuffix: '%'
        });
    }
    spark_sales_upload();

    $(window).on('resize', function () {
        Chartist1.update();
        spark_sales();
        spark_sales1();
        spark_sales_upload();

    });
});