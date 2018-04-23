'use strict';
$(document).ready(function() {

    // Just guage charts
    window.onload = function() {
        var gauge1 = new JustGage({
            id: "gauge1",
            relativeGaugeSize: true,
            value: getRandomInt(0, 100),
            min: 0,
            max: 100,
            decimals: 0,
            valueFontFamily: "Source Sans Pro, sans-serif",
            levelColors: ["#4fb7fe"],
            counter: true
        });

        var gauge2 = new JustGage({
            id: "gauge2",
            relativeGaugeSize: true,
            value: getRandomInt(0, 100),
            min: 0,
            max: 100,
            humanFriendly: false,
            valueFontFamily: "Source Sans Pro, sans-serif",
            decimals: 0,
            levelColors: ["#00cc99"],
            counter: true
        });

        var gauge3 = new JustGage({
            id: "gauge3",
            relativeGaugeSize: true,
            value: getRandomInt(0, 100),
            min: 0,
            max: 100,
            valueFontFamily: "Source Sans Pro, sans-serif",
            levelColors: ["#347dff"],
            decimals: 1,
            counter: true
        });

        var gauge4 = new JustGage({
            id: "gauge4",
            relativeGaugeSize: true,
            value: getRandomInt(0, 100),
            min: 0,
            max: 100,
            decimals: 0,
            levelColors: ["#EF6F6C"],
            valueFontFamily: "Source Sans Pro, sans-serif",
            counter: true
        });

        setInterval(function() {
            gauge1.refresh(getRandomInt(50, 100));
            gauge2.refresh(getRandomInt(50, 100));
            gauge3.refresh(getRandomInt(0, 50));
            gauge4.refresh(getRandomInt(0, 50));
        }, 2500);
    };
    // End of just guage charts

    // stacked area chart
    var chart = c3.generate({
        bindto: '#chart2',
        data: {
            columns: [
                ['data1', 30, 300, 100, 400, 150, 300],
                ['data2', 300, 130, 350, 130, 300, 80]
            ],
            type: 'bar',
            colors: {
                data1: '#0fb0c0',
                data2: '#4fb7fe',
                data3: '#00cc99'
            },
            color: function(color, d) {
                return d.id && d.id === 'data3' ? d3.rgb(color) : color;
            }
        }
    });
    setTimeout(function() {
        chart.transform('area-spline', 'data1');
    }, 1000);

    setTimeout(function() {
        chart.transform('area-spline', 'data2');
    }, 2000);

    setTimeout(function() {
        chart.transform('bar');
    }, 3000);

    setTimeout(function() {
        chart.transform('area-spline');
    }, 4000);
    // End of stacked area chart

    // Scatter plot
    var chart3 = c3.generate({
        bindto: '#chart3',
        data: {
            columns: [
                ["setosa", 2, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5, 2.0, 1.9, 2.1, 2.0, 2.4, 2.3, 1.8, 2.2, 2.3, 1.5, 2.3, 2.0, 2.0, 1.8, 2.1, 1.8, 1.8, 1.8, 2.1, 1.6, 1.9, 2.0, 2.2, 1.5, 1.4, 2.3, 2.4, 1.8, 1.8, 2.1, 2.4, 2.3, 1.9, 2.3, 2.5, 2.3, 1.9, 2.0, 2.3, 1.8],
                ["versicolor", 1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4, 1.0, 1.5, 1.0, 1.4, 1.3, 1.4, 1.5, 1.0, 1.5, 1.1, 1.8, 1.3, 1.5, 1.2, 1.3, 1.4, 1.4, 1.7, 1.5, 1.0, 1.1, 1.0, 1.2, 1.6, 1.5, 1.6, 1.5, 1.3, 1.3, 1.3, 1.2, 1.4, 1.2, 1.0, 1.3, 1.2, 1.3, 1.3, 1.1, 1.3]
            ],
            type: 'scatter'
        },
        axis: {
            x: {
                label: 'Sepal.Width',
                tick: {
                    fit: false
                }
            },
            y: {
                label: 'Petal.Width'
            }
        }
    });

    // End of Scatter plot

    // Donut chart
    var chart1 = c3.generate({
        bindto: '#chart1',
        data: {
            columns: [
                ['data1', 30],
                ['data2', 120]
            ],
            type: 'donut'
        },
        donut: {
            title: "Iris Petal Width"
        },
        color: {
            pattern: ['#4fb7fe', '#00cc99', '#347dff', '#ff9933', '#69B3BF']
        }
    });

    setTimeout(function() {
        chart1.load({
            columns: [
                ["setosa", 0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2, 0.4, 0.4, 0.3, 0.3, 0.3, 0.2, 0.4, 0.2, 0.5, 0.2, 0.2, 0.4, 0.2, 0.2, 0.2, 0.2, 0.4, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.6, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2],
                ["versicolor", 1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4, 1.0, 1.5, 1.0, 1.4, 1.3, 1.4, 1.5, 1.0, 1.5, 1.1, 1.8, 1.3, 1.5, 1.2, 1.3, 1.4, 1.4, 1.7, 1.5, 1.0, 1.1, 1.0, 1.2, 1.6, 1.5, 1.6, 1.5, 1.3, 1.3, 1.3, 1.2, 1.4, 1.2, 1.0, 1.3, 1.2, 1.3, 1.3, 1.1, 1.3],
                ["virginica", 2.5, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5, 2.0, 1.9, 2.1, 2.0, 2.4, 2.3, 1.8, 2.2, 2.3, 1.5, 2.3, 2.0, 2.0, 1.8, 2.1, 1.8, 1.8, 1.8, 2.1, 1.6, 1.9, 2.0, 2.2, 1.5, 1.4, 2.3, 2.4, 1.8, 1.8, 2.1, 2.4, 2.3, 1.9, 2.3, 2.5, 2.3, 1.9, 2.0, 2.3, 1.8]
            ]
        });
    }, 1500);

    setTimeout(function() {
        chart1.unload({
            ids: 'data1'
        });
        chart1.unload({
            ids: 'data2'
        });
    }, 2500);
    // End of donut chart

    // Line chart
    var chart4 = c3.generate({
        bindto: '#chart4',
        data: {
            columns: [
                ['data1', 30, 200, 100, 400, 150, 250],
                ['data2', 50, 20, 10, 40, 15, 25]
            ],
            axes: {
                data1: 'y',
                data2: 'y2'
            }
        },
        axis: {
            y2: {
                show: true
            }
        }
    });

    setTimeout(function() {
        chart4.axis.max(500);
    }, 1000);

    setTimeout(function() {
        chart4.axis.min(-500);
    }, 2000);

    setTimeout(function() {
        chart4.axis.max({ y: 600, y2: 100 });
    }, 3000);

    setTimeout(function() {
        chart4.axis.min({ y: -600, y2: -100 });
    }, 4000);

    setTimeout(function() {
        chart4.axis.range({ max: 1000, min: -1000 });
    }, 5000);

    setTimeout(function() {
        chart4.axis.range({ max: { y: 600, y2: 100 }, min: { y: -100, y2: 0 } });
    }, 6000);

    setTimeout(function() {
        chart4.axis.max({ x: 10 });
    }, 7000);

    setTimeout(function() {
        chart4.axis.min({ x: -10 });
    }, 8000);

    setTimeout(function() {
        chart4.axis.range({ max: { x: 5 }, min: { x: 0 } });
    }, 9000);

    // En dof line chart

    $(".wrapper").on("resize", function() {
        setTimeout(function() {
            chart.resize();
            chart1.resize();
            chart3.resize();
            chart4.resize();
        }, 500);
    });
});
