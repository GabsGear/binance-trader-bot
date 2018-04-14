'use strict';
$(document).ready(function(){
// Transform origin example
$('#transform-origin-example').on('click', function() {
    var transform_origin_example= $('#transform-origin-example');
    var elementWidth = transform_origin_example.outerWidth();
    transform_origin_example.snabbt({
        fromRotation: [0, 0, 0],
        rotation: [0, 2 * Math.PI, 0],
        transformOrigin: [elementWidth / 2, 0, 0],
        perspective: 400
    });
});

// Transform origin example
$('#transform-origin-example-2').on('click', function() {
    var transform_origin_example2= $('#transform-origin-example-2');
    var elementWidth = transform_origin_example2.outerWidth();
    transform_origin_example2.snabbt({
        rotation: [0, Math.PI, 0],
        transformOrigin: [elementWidth / 2, 0, 0],
        perspective: 400,
        duration: 300,
        easing: 'ease'
    }).snabbt({
        fromPosition: [2 * elementWidth, 0, 0],
        position: [2 * elementWidth, 0, 0],
        fromRotation: [0, -Math.PI, 0],
        rotation: [0, 0, 0],
        transformOrigin: [-elementWidth / 2, 0, 0],
        perspective: 400,
        duration: 300,
        easing: 'ease'
    }).snabbt({
        fromRotation: [0, 0, 0],
        fromPosition: [2 * elementWidth, 0, 0],
        position: [0, 0, 0],
        duration: 300,
        easing: 'ease'
    });
});
// Value feed example
$('#value-feed-example').on('click', function() {
    $('#value-feed-example').snabbt({
        valueFeeder: function(value, matrix) {
            var x = Math.sin(value * Math.PI);
            return matrix.rotateZ(Math.sin(6 * value * Math.PI)).translate(x * 200, 0, 0);
        },
        duration: 1000
    });
});
// Easings
var easingDemos = document.querySelectorAll('.easing-demo');
var container;
for (var i = 0; i < easingDemos.length; ++i) {
    container = easingDemos[i];
    var easingName = container.attributes['data-easing-name'];
    var element = container.children[0];
    container.addEventListener('click', function(_container, _element, _easingName) {
        var containerWidth = _container.offsetWidth;
        var elementWidth = _element.offsetWidth;
        snabbt(_element, {
            fromPosition: [0, 0, 0],
            position: [containerWidth - elementWidth, 0, 0],
            easing: _easingName.value,
            duration: 5000
        });
    }.bind(null, container, element, easingName));
}
});