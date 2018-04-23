'use strict';
$(document).ready(function () {
    // ========================Jqvmaps=====================

    // World map
    $('#world-map-gdp').vectorMap({
        map: 'world_en',
        backgroundColor: '#eaeaea',
        color: '#ffffff',
        hoverOpacity: 0.7,
        selectedColor: '#EF6F6C',
        values: sample_data,
        scaleColors:['#feEda0','#ff6491'],
        normalizeFunction: 'polynomial',
        onRegionClick: function(element, code, region)
        {
            var message = 'You clicked "'
                + region
                + '" which has the code: '
                + code.toUpperCase();

            alert(message);
        }
    });
    // End of world map

    // Russia map
    $('#russia_map').vectorMap({
        map: 'russia_en',
        backgroundColor: '#eaeaea',
        color: '#ff9933',
        selectedColor: '#EF6F6C',
        hoverColor: '#4fb7fe',
        onRegionClick: function(element, code, region)
        {
            var message = 'You clicked "'
                + region
                + '" which has the code: '
                + code.toUpperCase();

            alert(message);
        }
    });
    // End of russia map

    // Usa map
    $('#usa_map').vectorMap({
        map: 'usa_en',
        backgroundColor: '#eaeaea',
        color: '#4fb7fe',
        selectedColor: '#EF6F6C',
        hoverColor: '#ff9933',
        colors: {
            mo: '#EF6F6C',
            fl: '#00cc99',
            or: '#0fb0c0'
        },
        onRegionClick: function(element, code, region)
        {
            var message = 'You clicked "'
                + region
                + '" which has the code: '
                + code.toUpperCase();

            alert(message);
        }
    });
    // End of usa map

    // Canada map
    $('#canada_map').vectorMap({
        map: 'canada_en',
        backgroundColor: '#eaeaea',
        color: '#347dff',
        selectedColor: '#EF6F6C',
        hoverColor: '#ff9933',
        onRegionClick: function(element, code, region)
        {
            var message = 'You clicked "'
                + region
                + '" which has the code: '
                + code.toUpperCase();

            alert(message);
        }
    });
    // End of canada map

    // Europe map
    $('#europe_map').vectorMap({
        map: 'europe_en',
        backgroundColor: '#eaeaea',
        color: '#00cc99',
        selectedColor: '#EF6F6C',
        hoverColor: '#ff9933',
        onRegionClick: function(element, code, region)
        {
            var message = 'You clicked "'
                + region
                + '" which has the code: '
                + code.toUpperCase();

            alert(message);
        }
    });
    // End of europe map

    $("#menu-toggle,.toggle-right").on("click",function(e) {
        setTimeout(function(){
            $(window).trigger('resize');
        },250);
    });
});