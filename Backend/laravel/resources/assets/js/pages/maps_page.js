'use strict';
$(document).ready(function() {
    $("#menu-toggle").on("click", function() {
        setTimeout(function() {
            basicmap.refresh();
            markermap.refresh();
            styledmap.refresh();
            maptypes.refresh();
            search_placemap.refresh();
            routemap.refresh();
        }, 500);
    });
    // ==========basic map=============
    var $gmap = $(".gmap");
    $gmap.css("height", "300px");
    var basicmap = new GMaps({
        div: "#gmap-top",
        lat: -33.865,
        lng: 151.2,
        zoom: 15,
        zoomControl: true,
        zoomControlOpt: {
            style: "SMALL",
            position: "TOP_LEFT"
        },
        disableDefaultUI: !0,
        // scrollwheel: !1
    });
    // =============basic map=============
    // ========map markers=============================
    var markers = [{
        lat: -12.043333,
        lng: -77.028333,
        title: "Marker #1",
        animation: google.maps.Animation.DROP,
        infoWindow: {
            content: "<strong>Marker #1: HTML Content</strong>"
        }
    }, {
        lat: -12.000000,
        lng: -77.000000,
        title: "Marker #2",
        animation: google.maps.Animation.DROP,
        infoWindow: {
            content: "<strong>Marker #2: HTML Content</strong>"
        }
    }, {
        lat: -20,
        lng: 85,
        title: "Marker #3",
        animation: google.maps.Animation.DROP,
        infoWindow: {
            content: "<strong>Marker #3: HTML Content</strong>"
        }
    }, {
        lat: -20,
        lng: -110,
        title: "Marker #4",
        animation: google.maps.Animation.DROP,
        infoWindow: {
            content: "<strong>Marker #4: HTML Content</strong>"
        }
    }];
    var markermap = new GMaps({
        div: "#gmap-markers",
        lat: -12.043333,
        lng: -77.028333,
        zoom: 10,
        zoomControl: true,
        zoomControlOpt: {
            style: "SMALL",
            position: "TOP_LEFT"
        },
        // scrollwheel: !1
    });
    markermap.addMarkers(markers);
    // ========================map markers===================
    // ==============styled map=============
    var styledmap = new GMaps({
        div: "#gmap-styled",
        lat: 41.895465,
        lng: 12.482324,
        zoom: 5,
        zoomControl: true,
        zoomControlOpt: {
            style: "SMALL",
            position: "TOP_LEFT"
        },
        panControl: true,
        streetViewControl: false,
        mapTypeControl: false,
        overviewMapControl: false
    });
    var styles = [{
        stylers: [
            { hue: "#00ffe6" },
            { saturation: -20 }
        ]
    }, {
        featureType: "road",
        elementType: "geometry",
        stylers: [
            { lightness: 100 },
            { visibility: "simplified" }
        ]
    }, {
        featureType: "road",
        elementType: "labels",
        stylers: [
            { visibility: "off" }
        ]
    }];
    styledmap.addStyle({
        styles: styles,
        mapTypeId: "maps_style"
    });

    styledmap.setStyle("maps_style");
    // ================styled map==================
    // ==============map types============
    var maptypes = new GMaps({
        el: '#gmap-types',
        lat: -12.043333,
        lng: -77.028333,
        mapTypeControlOptions: {
            mapTypeIds: ["terrain", "osm", "cloudmade","hybrid","satellite"]
        }
    });
    maptypes.addMapType("osm", {
        getTileUrl: function(coord, zoom) {
            return "http://tile.openstreetmap.org/" + zoom + "/" + coord.x + "/" + coord.y + ".png";
        },
        tileSize: new google.maps.Size(256, 256),
        name: "OpenStreetMap",
        maxZoom: 18
    });
    maptypes.addMapType("cloudmade", {
        getTileUrl: function(coord, zoom) {
            return "http://b.tile.cloudmade.com/8ee2a50541944fb9bcedded5165f09d9/1/256/" + zoom + "/" + coord.x + "/" + coord.y + ".png";
        },
        tileSize: new google.maps.Size(256, 256),
        name: "CloudMade",
        maxZoom: 18
    });
    maptypes.setMapTypeId("osm");
    // ================map types========================
    // ============================================adv maps js=============================
    // var map1;
    // =====================search place====================    
    var search_placemap = new GMaps({
        div: '#map1',
        lat: 43.654438,
        lng: -79.380699,
        zoom: 3
    });
    $('#geocoding_form').on("submit",function(e) {
        e.preventDefault();
        GMaps.geocode({
            address: $('#address').val().trim(),
            callback: function(results, status) {
                if (status == 'OK') {
                    var latlng = results[0].geometry.location;
                    search_placemap.setCenter(latlng.lat(), latlng.lng());
                    search_placemap.addMarker({
                        lat: latlng.lat(),
                        lng: latlng.lng()
                    });
                }
            }
        });
    });
    // ============search places=============

    var routemap;
    // =============search route============================
    var route;

    $('#forward').attr('disabled', 'disabled');
    $('#back').attr('disabled', 'disabled');
    $('#get_route').on("click",function(e) {
        e.preventDefault();

        var origin = routemap.markers[0].getPosition();
        var destination = routemap.markers[routemap.markers.length - 1].getPosition();

        routemap.getRoutes({
            origin: [origin.lat(), origin.lng()],
            destination: [destination.lat(), destination.lng()],
            travelMode: 'driving',
            callback: function(e) {
                route = new GMaps.Route({
                    map: routemap,
                    route: e[0],
                    strokeColor: '#000',
                    strokeOpacity: 0.5,
                    strokeWeight: 10
                });
                $('#forward').removeAttr('disabled');
                $('#back').removeAttr('disabled');
            }
        });
        $('#forward').on("click",function(e) {
            e.preventDefault();
            route.forward();

            if (route.step_count < route.steps_length)
                $('#steps').append('<li>' + route.steps[route.step_count].instructions + '</li>');
        });
        $('#back').on("click",function(e) {
            e.preventDefault();
            route.back();

            if (route.step_count >= 0)
                $('#steps').find('li').last().remove();
        });
    });
    routemap = new GMaps({
        div: '#map',
        lat: 40.758895,
        lng: -73.985131,
        zoom: 14,
        click: function(e) {
            routemap.addMarker({
                lat: e.latLng.lat(),
                lng: e.latLng.lng()
            });
        }
    });
    // ===========search route======================

});
