'use strict';
$(document).ready(function(){
    // Donut chart
    var data1 = {
        series: [20, 20, 40, 20, 15, 40, 15],
        labels: [1, 2, 3, 4, 5, 6, 7]
    };
    var options1 = {
        donut: true,
        showLabel: false
    };
    var chart= new Chartist.Pie('#animated_chart', data1, options1);
    chart.on('draw', function(data) {
        if(data.type === 'slice') {
            var pathLength = data.element._node.getTotalLength();

            data.element.attr({
                'stroke-dasharray': pathLength + 'px ' + pathLength + 'px'
            });

            var animationDefinition = {
                'stroke-dashoffset': {
                    id: 'anim' + data.index,
                    dur: 500,
                    from: -pathLength + 'px',
                    to:  '0px',
                    easing: Chartist.Svg.Easing.easeOutQuint,
                    fill: 'freeze'
                }
            };

            if(data.index !== 0) {
                animationDefinition['stroke-dashoffset'].begin = 'anim' + (data.index - 1) + '.end';
            }

            data.element.attr({
                'stroke-dashoffset': -pathLength + 'px'
            });

            data.element.animate(animationDefinition, false);
        }
    });

    chart.on('created', function() {
        if(window.__anim21278907124) {
            clearTimeout(window.__anim21278907124);
            window.__anim21278907124 = null;
        }
        window.__anim21278907124 = setTimeout(chart.update.bind(chart), 5000);
    });

    // End of donut chart

    // Stacked bar chart
    var chart1= new Chartist.Bar('#stacked_chart', {
        labels: ['Q1', 'Q2', 'Q3', 'Q4'],
        series: [
            [300000, 200000, 800000, 300000],
            [500000, 700000, 300000, 300000],
            [800000, 200000, 400000, 300000]
        ]
    }, {
        stackBars: true,
        axisY: {
            labelInterpolationFnc: function(value) {
                return (value / 1000) + 'k';
            }
        }
    });
    chart1.on('draw', function(data) {
        if(data.type === 'bar') {
            data.element.attr({
                style: 'stroke-width: 30px'
            });
        }
    });

    // End of stacked bar chart

    // Peak circles Bi-Pplar Bar Chart
    var chart3 = new Chartist.Bar('#draw_events', {
        labels: ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10'],
        series: [
            [1, 2, 4, 8, 6, -2, -1, -4, -6, -2]
        ]
    }, {
        high: 10,
        low: -10,
        axisX: {
            labelInterpolationFnc: function(value, index) {
                return index % 2 === 0 ? value : null;
            }
        }
    });

    chart3.on('draw', function(data) {
        if(data.type === 'bar') {
            data.group.append(new Chartist.Svg('circle', {
                cx: data.x2,
                cy: data.y2,
                r: Math.abs(Chartist.getMultiValue(data.value)) * 2 + 2
            }, 'ct-slice-pie'));
        }
    });
    // End of Peak circles Bi-Pplar Bar Chart

    // Smil animation
    var data4 = {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        series: [
            [12, 9, 7, 8, 5, 9, 12, 8, 5, 3, 4, 6],
            [4,  8, 12, 8, 3, 5, 5, 10, 4, 12, 5, 5],
            [5,  3, 4, 5, 6, 3, 3, 4, 5, 6, 3, 4],
            [3,  4, 5, 6, 4, 6, 4, 5, 6, 3, 6, 3]
        ]
    };
    var options4 = {
        low: 0
    };
    var chart4= new Chartist.Line('#smil_animation', data4, options4);

// Let's put a sequence number aside so we can use it in the event callbacks
    var seq = 0,
        delays = 50,
        durations = 500;

// Once the chart is fully created we reset the sequence
    chart4.on('created', function() {
        seq = 0;
    });

// On each drawn element by Chartist we use the Chartist.Svg API to trigger SMIL animations
    chart4.on('draw', function(data) {
        seq++;

        if(data.type === 'line') {
            // If the drawn element is a line we do a simple opacity fade in. This could also be achieved using CSS3 animations.
            data.element.animate({
                opacity: {
                    // The delay when we like to start the animation
                    begin: seq * delays ,
                    // Duration of the animation
                    dur: durations,
                    // The value where the animation should start
                    from: 0,
                    // The value where it should end
                    to: 1
                }
            });
        } else if(data.type === 'label' && data.axis === 'x') {
            data.element.animate({
                y: {
                    begin: seq * delays,
                    dur: durations,
                    from: data.y + 100,
                    to: data.y,
                    // We can specify an easing function from Chartist.Svg.Easing
                    easing: 'easeOutQuart'
                }
            });
        } else if(data.type === 'label' && data.axis === 'y') {
            data.element.animate({
                x: {
                    begin: seq * delays,
                    dur: durations,
                    from: data.x - 100,
                    to: data.x,
                    easing: 'easeOutQuart'
                }
            });
        } else if(data.type === 'point') {
            data.element.animate({
                x1: {
                    begin: seq * delays,
                    dur: durations,
                    from: data.x - 10,
                    to: data.x,
                    easing: 'easeOutQuart'
                },
                x2: {
                    begin: seq * delays,
                    dur: durations,
                    from: data.x - 10,
                    to: data.x,
                    easing: 'easeOutQuart'
                },
                opacity: {
                    begin: seq * delays,
                    dur: durations,
                    from: 0,
                    to: 1,
                    easing: 'easeOutQuart'
                }
            });
        } else if(data.type === 'grid') {
            // Using data.axis we get x or y which we can use to construct our animation definition objects
            var pos1Animation = {
                begin: seq * delays,
                dur: durations,
                from: data[data.axis.units.pos + '1'] - 30,
                to: data[data.axis.units.pos + '1'],
                easing: 'easeOutQuart'
            };

            var pos2Animation = {
                begin: seq * delays,
                dur: durations,
                from: data[data.axis.units.pos + '2'] - 100,
                to: data[data.axis.units.pos + '2'],
                easing: 'easeOutQuart'
            };

            var animations = {};
            animations[data.axis.units.pos + '1'] = pos1Animation;
            animations[data.axis.units.pos + '2'] = pos2Animation;
            animations['opacity'] = {
                begin: seq * delays,
                dur: durations,
                from: 0,
                to: 1,
                easing: 'easeOutQuart'
            };

            data.element.animate(animations);
        }
    });

// For the sake of the example we update the chart every time it's created with a delay of 10 seconds

    chart4.on('created', function() {
        if(window.__exampleAnimateTimeout) {
            clearTimeout(window.__exampleAnimateTimeout);
            window.__exampleAnimateTimeout = null;
        }
        window.__exampleAnimateTimeout = setTimeout(chart.update.bind(chart), 12000);
    });

    // End of smil animation

    // Path animation
    var data5 = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        series: [
            [1, 7, 3, 2, 4, 3],
            [2, 3, 2, 8, 6, 2],
            [5, 4, 3, 5, 1, 0.5]
        ]
    };
    var options5 = {
        low: 0,
        showArea: true,
        showPoint: false,
        fullWidth: true
    };
    var chart5= new Chartist.Line('#path_animation', data5, options5);

    chart5.on('draw', function(data) {
        if(data.type === 'line' || data.type === 'area') {
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
    // En dof path animation

    // Multi line labels
    var data6 = {
        labels: ['First quarter of the year', 'Second quarter of the year', 'Third quarter of the year', 'Fourth quarter of the year'],
        series: [
            [60000, 40000, 80000, 70000],
            [40000, 30000, 70000, 65000],
            [8000, 3000, 10000, 6000]
        ]
    };
    var options6 = {
        seriesBarDistance: 10,
        axisX: {
            offset: 60
        },
        axisY: {
            offset: 80,
            labelInterpolationFnc: function(value) {
                return value + ' CHF'
            },
            scaleMinSpace: 30
        }
    };
    var chart6= new Chartist.Bar('#multi_line', data6, options6);
    // End of multi line labels

    $("#menu-toggle, .toggle-right").on("click", function () {
        setTimeout(function () {
            new Chartist.Pie('#animated_chart', data1, options1);
            var chart1= new Chartist.Bar('#stacked_chart', {
                labels: ['Q1', 'Q2', 'Q3', 'Q4'],
                series: [
                    [300000, 200000, 800000, 300000],
                    [500000, 700000, 300000, 300000],
                    [800000, 200000, 400000, 300000]
                ]
            }, {
                stackBars: true,
                axisY: {
                    labelInterpolationFnc: function(value) {
                        return (value / 1000) + 'k';
                    }
                }
            });
            chart1.on('draw', function(data) {
                if(data.type === 'bar') {
                    data.element.attr({
                        style: 'stroke-width: 30px'
                    });
                }
            });
            var chart3 = new Chartist.Bar('#draw_events', {
                labels: ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10'],
                series: [
                    [1, 2, 4, 8, 6, -2, -1, -4, -6, -2]
                ]
            }, {
                high: 10,
                low: -10,
                axisX: {
                    labelInterpolationFnc: function(value, index) {
                        return index % 2 === 0 ? value : null;
                    }
                }
            });
            chart3.on('draw', function(data) {
                if(data.type === 'bar') {
                    data.group.append(new Chartist.Svg('circle', {
                        cx: data.x2,
                        cy: data.y2,
                        r: Math.abs(Chartist.getMultiValue(data.value)) * 2 + 2
                    }, 'ct-slice-pie'));
                }
            });
            new Chartist.Line('#smil_animation', data4, options4);
            new Chartist.Line('#path_animation', data5, options5);
            new Chartist.Bar('#multi_line', data6, options6);
        }, 500);
    });



});