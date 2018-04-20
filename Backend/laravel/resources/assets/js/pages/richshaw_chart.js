//-------------------Line and Toggling chart----------------
'use strict';
$(document).ready(function() {
    //---- Line chart---------------

    var seriesData3 = [
        [],
        [],
        []
    ];
    var random3 = new Rickshaw.Fixtures.RandomData(150);

    for (var i = 0; i < 150; i++) {
        random3.addData(seriesData3);
    }
    var graph3 = new Rickshaw.Graph({
        element: document.querySelector("#chart3"),
        renderer: 'line',
        series: [{
            color: "#4fb7fe",
            data: seriesData3[0],
            name: 'New York'
        }, {
            color: "#ff9933",
            data: seriesData3[1],
            name: 'London'
        }, {
            color: "#ed7669",
            data: seriesData3[2],
            name: 'Tokyo'
        }]
    });
    // End of line chart

    var seriesData1 = [
        [],
        [],
        []
    ];
    var random1 = new Rickshaw.Fixtures.RandomData(150);

    for (var i = 0; i < 150; i++) {
        random1.addData(seriesData1);
    }
    var graph1 = new Rickshaw.Graph({
        element: document.getElementById("chart_1"),

        renderer: 'line',
        series: [{
            color: "#4fb7fe",
            data: seriesData1[0],
            name: 'New York'
        }, {
            color: "#ed7669",
            data: seriesData1[1],
            name: 'London'
        }, {
            color: "#00cc99",
            data: seriesData1[2],
            name: 'Tokyo'
        }]
    });

    graph1.render();

    var legend_1 = document.querySelector('#legend_1');

    var Hover = Rickshaw.Class.create(Rickshaw.Graph.HoverDetail, {

        render: function(args) {

            legend_1.innerHTML = args.formattedXValue;

            args.detail.sort(function(a, b) {
                return a.order - b.order }).forEach(function(d) {

                var line = document.createElement('div');
                line.className = 'line';

                var swatch = document.createElement('div');
                swatch.className = 'swatch';
                swatch.style.backgroundColor = d.series.color;

                var label = document.createElement('div');
                label.className = 'label';
                label.innerHTML = d.name + ": " + d.formattedYValue;

                line.appendChild(swatch);
                line.appendChild(label);

                legend_1.appendChild(line);

                var dot = document.createElement('div');
                dot.className = 'dot';
                dot.style.top = graph1.y(d.value.y0 + d.value.y) + 'px';
                dot.style.borderColor = d.series.color;

                this.element.appendChild(dot);

                dot.className = 'dot active';

                this.show();

            }, this);
        }
    });

    var hover = new Hover({ graph: graph1 });


    //------------------Multiple Renderers Chart---------

    var seriesData2 = [
        [],
        [],
        [],
        [],
        []
    ];
    var random2 = new Rickshaw.Fixtures.RandomData(50);

    for (var i = 0; i < 75; i++) {
        random2.addData(seriesData2);
    }

    var graph2 = new Rickshaw.Graph({
        element: document.getElementById("chart2"),
        renderer: 'multi',

        dotSize: 5,
        series: [{
            name: 'temperature',
            data: seriesData2.shift(),
            color: '#8acbe8',
            renderer: 'stack'
        }, {
            name: 'heat index',
            data: seriesData2.shift(),
            color: '#e6f1d0',
            renderer: 'stack'
        }, {
            name: 'dewpoint',
            data: seriesData2.shift(),
            color: '#0fb0c0',
            renderer: 'scatterplot'
        }, {
            name: 'pop',
            data: seriesData2.shift().map(function(d) {
                return { x: d.x, y: d.y / 4 } }),
            color: '#ff9933',
            renderer: 'bar'
        }, {
            name: 'humidity',
            data: seriesData2.shift().map(function(d) {
                return { x: d.x, y: d.y * 1.5 } }),
            renderer: 'line',
            color: '#347dff'
        }]
    });

    var slider2 = new Rickshaw.Graph.RangeSlider.Preview({
        graph: graph2,
        element: document.querySelector('#slider2')
    });

    var axes = new Rickshaw.Graph.Axis.Time({ graph: graph2 });

    graph2.render();

    var detail = new Rickshaw.Graph.HoverDetail({
        graph: graph2
    });

    var legend_chart2 = new Rickshaw.Graph.Legend({
        graph: graph2,
        element: document.querySelector('#legend_chart2')
    });

    var highlighter = new Rickshaw.Graph.Behavior.Series.Highlight({
        graph: graph2,
        legend: legend_chart2,
        disabledColor: function() {
            return 'rgba(0, 0, 0, 0.2)' }
    });

    var highlighter = new Rickshaw.Graph.Behavior.Series.Toggle({
        graph: graph2,
        legend: legend_chart2
    });


    //---------------Log and Absolute Scale Chart---------------


    var random = new Rickshaw.Fixtures.RandomData(12 * 60 * 60);

    var series = [
        []
    ];

    for (var i = 0; i < 300; i++) {
        random.addData(series);
    }
    var data = series[0]

    var min = Number.MAX_VALUE;
    var max = Number.MIN_VALUE;
    for (i = 0; i < series[0].length; i++) {
        min = Math.min(min, series[0][i].y);
        max = Math.max(max, series[0][i].y);
    }

    var logScale = d3.scale.log().domain([min / 4, max]);
    var linearScale = d3.scale.linear().domain([min, max]).range(logScale.range());
    var graph = new Rickshaw.Graph({
        element: document.getElementById("chart"),
        renderer: 'line',
        series: [{
            color: '#0fb0c0',
            data: JSON.parse(JSON.stringify(data)),
            name: 'Log View',
            scale: logScale
        }, {
            color: '#ed7669',
            data: JSON.parse(JSON.stringify(data)),
            name: 'Linear View',
            scale: linearScale
        }]
    });
    new Rickshaw.Graph.HoverDetail({
        graph: graph
    });

    graph.render();
    //.......................Scaled Series Chart-------------

    var data, graph, i, max, min, point, random, scales, series, _i, _j, _k, _l, _len, _len1, _len2, _ref;

    data = [
        [],
        []
    ];

    random = new Rickshaw.Fixtures.RandomData(12 * 60 * 60);

    for (i = _i = 0; _i < 100; i = ++_i) {
        random.addData(data);
    }

    scales = [];

    _ref = data[1];
    for (_j = 0, _len = _ref.length; _j < _len; _j++) {
        point = _ref[_j];
        point.y *= point.y;
    }

    for (_k = 0, _len1 = data.length; _k < _len1; _k++) {
        series = data[_k];
        min = Number.MAX_VALUE;
        max = Number.MIN_VALUE;
        for (_l = 0, _len2 = series.length; _l < _len2; _l++) {
            point = series[_l];
            min = Math.min(min, point.y);
            max = Math.max(max, point.y);
        }
        if (_k === 0) {
            scales.push(d3.scale.linear().domain([min, max]).nice());
        } else {
            scales.push(d3.scale.pow().domain([min, max]).nice());
        }
    }

    var graph5 = new Rickshaw.Graph({
        element: document.getElementById("chart_5"),
        renderer: 'line',
        series: [{
            color: '#4fb7fe',
            data: data[0],
            name: 'Series A',
            scale: scales[0]
        }, {
            color: '#ff9933',
            data: data[1],
            name: 'Series B',
            scale: scales[1]
        }]
    });
    new Rickshaw.Graph.Axis.Time({
        graph: graph5
    });

    new Rickshaw.Graph.HoverDetail({
        graph: graph5
    });

    graph5.render();

    //-------------Simple Animation chart------------------

    var tv = 250;
    var graph6 = new Rickshaw.Graph({
        element: document.getElementById("chart_6"),

        renderer: 'line',
        series: new Rickshaw.Series.FixedDuration([{ name: 'one' }], undefined, {
            timeInterval: tv,
            maxDataPoints: 100,
            timeBase: new Date().getTime() / 1000
        })
    });

    graph6.render();

    var i = 0;
    var iv = setInterval(function() {

        var data = { one: Math.floor(Math.random() * 40) + 120 };

        var randInt = Math.floor(Math.random() * 100);
        data.two = (Math.sin(i++/ 40) + 4) * (randInt + 400);
        data.three = randInt + 300;

        graph6.series.addData(data); graph6.render();

    }, tv);


    function resize() {
        graph3.configure({ width: $("#chart3").width() });
        graph3.render();
        graph6.configure({ width: $("#chart_6").width() });
        graph6.render();
        graph2.configure({ width: $("#chart2").width() });
        graph2.render();
        graph.configure({ width: $("#chart").width() });
        graph.render();
        graph5.configure({ width: $("#chart_5").width() });
        graph5.render();
        graph1.configure({ width: $("#chart_1").width() });
        graph1.render();
    }
    $("#menu-toggle, .toggle-right").on("click", function() {
        setTimeout(function() {
            resize();
        }, 400);
    });
    $(window).on("resize", function() {
        resize();
    });
    graph3.render();
    var hoverDetail = new Rickshaw.Graph.HoverDetail({
        graph: graph3
    });
    var legend_chart3 = new Rickshaw.Graph.Legend({
        graph: graph3,
        element: document.getElementById('legend_chart3')
    });
    var shelving = new Rickshaw.Graph.Behavior.Series.Toggle({
        graph: graph3,
        legend: legend_chart3
    });
    var axes3 = new Rickshaw.Graph.Axis.Time();
    axes3.render();
});
