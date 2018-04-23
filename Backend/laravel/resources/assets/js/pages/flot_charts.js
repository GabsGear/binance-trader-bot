'use strict';
$(document).ready(function () {
    // Spline line chart
    function showTooltipStats(x, y, contents) {
        $('<div id="tooltip" class="tooltipflot">' + contents + '</div>').css({
            position: 'absolute',
            display: 'none',
            top: y + 5,
            left: x + 5
        }).appendTo("body").fadeIn(200);
    }

    var sales = [
        [0, 10],
        [2.5, 23],
        [5, 15],
        [7.5, 25],
        [8.5, 28],
        [9.5, 25],
        [11, 15],
        [13.5, 20],
        [16, 10]
    ];
    var profit = [
        [0, 20],
        [2, 12],
        [5, 22],
        [7.5, 13],
        // [4, 20],
        [10.5, 25],
        [12.5, 12],
        [15, 22],
        [16, 15]
    ];
    var basicflot= $("#basicflot");
    var plot = $.plot(basicflot, [{
        data: sales,
        label: "Sales",
        color: "#4fb7fe"
    }, {
        data: profit,
        label: "Profit",
        color: "#EF6F6C",
        opacity: "1"
    }], {
        series: {
            lines: {
                show: false
            },
            splines: {
                show: true,
                tension: 0.4,
                lineWidth: 1,
                fill: 0.4
            },
            points: {
                radius: 0,
                show: true
            },
            shadowSize: 2
        },
        legend: {
            container: '#basicFlotLegend1',
            noColumns: 0
        },
        grid: {
            hoverable: true,
            clickable: true,
            borderColor: '#ddd',
            borderWidth: 0,
            labelMargin: 5,
            backgroundColor: '#fff'
        },
        colors: ["#4fb7fe", "#EF6F6C"],
        xaxis: {},
        yaxis: {
            ticks: 4
        }
    });

    var previousPoint1 = null;
    basicflot.on("bind","plothover", function(event, pos, item) {
        $("#x").text(pos.x.toFixed(2));
        $("#y").text(pos.y.toFixed(2));

        if (item) {
            if (previousPoint1 != item.dataIndex) {
                previousPoint1 = item.dataIndex;

                $("#tooltip").remove();
                var x = item.datapoint[0].toFixed(2),
                    y = item.datapoint[1].toFixed(2);

                showTooltipStats(item.pageX, item.pageY,
                    item.series.label + " on " + parseInt(x) + " = " + parseInt(y));
            }

        } else {
            $("#tooltip").remove();
            previousPoint1 = null;
        }

    });

    basicflot.on("bind","plotclick", function(event, pos, item) {
        if (item) {
            plot.highlight(item.series, item.datapoint);
        }
    });

    //line chart start


    var d1, d2, data, Options;

    d1 = [
        [1262304000000, 100], [1264982400000,560], [1267401600000, 1605], [1270080000000, 1129],
        [1272672000000, 2163], [1275350400000, 1905], [1277942400000, 2002], [1280620800000, 2917],
        [1283299200000, 2700], [1285891200000, 2700], [1288569600000, 2100], [1291161600000, 2700]
    ];

    d2 = [
        [1262304000000, 434], [1264982400000,232], [1267401600000, 875], [1270080000000, 553],
        [1272672000000, 975], [1275350400000, 1379], [1277942400000, 789], [1280620800000, 1026],
        [1283299200000, 1240], [1285891200000, 1892], [1288569600000, 1147], [1291161600000, 2256]
    ];

    data = [{
        label: "Total visitors",
        data: d1,
        color: "#0fb0c0"
    }, {
        label: "Total Sales",
        data: d2,
        color: "#ff9933"
    }];

    Options = {
        xaxis: {
            min: (new Date(2009, 12, 1)).getTime(),
            max: (new Date(2010, 11, 2)).getTime(),
            mode: "time",
            tickSize: [1, "month"],
            monthNames: ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
            tickLength: 0
        },
        yaxis: {

        },
        series: {
            lines: {
                show: true,
                fill: false,
                lineWidth: 2
            },
            points: {
                show: true,
                radius: 4.5,
                fill: true,
                fillColor: "#ffffff",
                lineWidth: 2
            }
        },
        grid: {
            hoverable: true,
            clickable: false,
            borderWidth: 0
        },
        legend: {
            container: '#basicFlotLegend',
            show: true
        },

        tooltip: true,
        tooltipOpts: {
            content: '%s: %y'
        }

    };


    var holder = $('#line-chart');

    if (holder.length) {
        $.plot(holder, data, Options );
    }

//line chart end

//start bar chart
    var d1 = [["1", 100],["2", 80],["3", 66],["4", 48],["5", 68],["6", 48],["7",66],["8", 80],["9", 64],["10", 48],["11",64],["12",100]];
    $.plot("#bar-chart", [{
        data: d1,
        label: "Project",
        color: "#0fb0c0"
    }], {
        series: {
            bars: {
                align: "center",
                lineWidth: 0,
                show: !0,
                barWidth: .6,
                fill: .9
            }
        },
        grid: {
            borderColor: "#ddd",
            borderWidth: 1,
            hoverable: !0
        },
        legend: {
            container: '#basicFlotLegend2',
            show: true
        },
        tooltip: true,
        tooltipOpts: {
            content: '%s: %y'
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
//end bar chart

//start bar stack
    var d11 = [["Jan", 130],["Feb",63],["Mar", 104],["Apr", 54],["May", 92],["Jun", 150],["Jul", 50],["Aug", 80],["Sep",120],["Oct", 91],["Nov", 79],["Dec", 112]];
    var d12 = [["Jan", 58],["Feb", 30],["Mar", 46],["Apr", 35],["May", 55],["Jun", 46],["Jul", 20],["Aug", 50],["Sep", 50],["Oct", 40],["Nov", 35],["Dec", 57]];
    $.plot("#bar-chart-stacked", [{
        data: d11,
        label: "New Visitor",
        color: "#4fb7fe"
    },{
        data: d12,
        label: "Returning Visitor",
        color: "#0fb0c0"
    }], {
        series: {
            stack: !0,
            bars: {
                align: "center",
                lineWidth: 0,
                show: !0,
                barWidth: .6,
                fill: .9
            }
        },
        grid: {
            borderColor: "#ddd",
            borderWidth: 1,
            hoverable: !0
        },
        legend: {
            container: '#basicFlotLegend3',
            show: true
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
//end bar chart stack
//donut
    var datax = [{
        label: "Profile",
        data: 150,
        color: '#4fb7fe'
    }, {
        label: "Facebook ",
        data: 130,
        color: '#00cc99'
    }, {
        label: "Twitter ",
        data: 190,
        color: '#0fb0c0'
    }, {
        label: "Google+",
        data: 180,
        color: '#EF6F6C'
    }, {
        label: "Linkedin",
        data: 120,
        color: '#ff9933'
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


    var data = [],
        series = Math.floor(Math.random() * 6) + 3;

    for (var i = 0; i < series; i++) {
        data[i] = {
            label: "Series" + (i + 1),
            data: Math.floor(Math.random() * 100) + 1
        }
    }
    $.plot("#placeholdertranslabel", data, {
        series: {
            pie: {
                show: true,
                radius: 1,
                label: {
                    show: true,
                    radius: 1,
                    formatter:labelFormatter,
                    background: {
                        opacity: 0.8
                    }
                }
            }
        },
        legend: {
            show: false
        },
        colors: [ '#00cc99', '#4fb7fe', '#347dff', '#ff9933', '#0fb0c0']
    });

    $("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
    function labelFormatter(label, series) {
        return "<div style='font-size:8pt; text-align:center; padding:2px; color:white;'>" + label + "<br/>" + Math.round(series.percent) + "%</div>";
    }
//end of transparent label pie charts

    var data = [],
        series = Math.floor(Math.random() * 6) + 3;

    for (var i = 0; i < series; i++) {
        data[i] = {
            label: "Series" + (i + 1),
            data: Math.floor(Math.random() * 100) + 1
        }
    }
    $.plot('#placeholdertiltedpie', data, {
        series: {
            pie: {
                show: true,
                radius: 1,
                tilt: 0.5,
                label: {
                    show: true,
                    radius: 1,
                    formatter: labelFormatter,
                    background: {
                        opacity: 0.8
                    }
                },
                combine: {
                    color: "#999",
                    threshold: 0.1
                }
            }
        },
        legend: {
            show: false
        },
        colors: [ '#00cc99', '#4fb7fe', '#0fb0c0', '#ff9933', '#347dff']
    });

    $("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
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

// up control widget
    var updateInterval = 50;

// setup plot
    var options = {
        colors: ["#4fb7fe"],
        series: {
            shadowSize: 0,
            lines: {
                show: true,
                fill: true,
                fillColor: {
                    colors: [{
                        opacity: 0.5
                    }, {
                        opacity: 0.5
                    }]
                }
            }
        },
        yaxis: {
            min: 0,
            max: 90
        },
        xaxis: {
            show: false
        },
        grid: {
            backgroundColor: '#fff',
            borderWidth: 1,
            borderColor: '#fff'
        }
    };

    var plot4 = $.plot($("#realtime"), [getRandomData()], options);

    function update() {
        plot4.setData([getRandomData()]);
        // since the axes don't change, we don't need to call plot.setupGrid()
        plot4.draw();
        setTimeout(update, updateInterval);
    }
    update();
//start area chart
    var da1 = [["Jan", 50],["Feb", 75],["Mar", 60],["Apr", 100],["May", 60],["Jun", 80],["Jul", 40]];
    var da2 = [["Jan", 20],["Feb", 40],["Mar", 30],["Apr", 40],["May", 15],["Jun", 25],["Jul", 10]];
    $.plot("#area-chart", [{
        data: da1,
        label: "Product 1",
        color: "#00cc99"
    },{
        data: da2,
        label: "product 2",
        color: "#ff9933"
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
//start spline area chart
    var ds1 = [["Jan", 35],["Feb", 38],["Mar", 36.7],["Apr", 35],["May", 37],["Jun", 39],["Jul", 35]];
    var ds2 = [["Jan", 36],["Feb", 34],["Mar", 35],["Apr", 38],["May", 35],["Jun", 34],["Jul", 37]];
    $.plot("#chart-spline", [{
        data: ds1,
        label: "product 1",
        color: "#0fb0c0"
    },{
        data: ds2,
        label: "product 2",
        color: "#ff9933"
    }], {
        series: {
            lines: {
                show: !1
            },
            splines: {
                show: !0,
                tension: .4,
                lineWidth: 2,
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
});
