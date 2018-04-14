'use strict';
$(document).ready(function(){
    // Ratings
    $('.rating').rating({
        size:'sm'
    });
    $('#input-3').rating({
        step: 1,
        size: 'sm',
        starCaptions: { 1: 'Poor', 2: 'Average', 3: 'Good', 4: 'Very Good', 5: 'Excellent' },
        starCaptionClasses: { 1: 'text-danger', 2: 'text-warning', 3: 'text-info', 4: 'text-primary', 5: 'text-success' }
    });
    // End of rating

    // Starrability
    var updateCounter = function (rating) {
        $(this).next(".counter").text(rating);
    };
    $("#rateYo").rateYo({
        rating: 3.6
    });
    $("#rateYo_width").rateYo({
        starWidth: "40px",
        rating:2
    });
    $("#rateYo_normalfill").rateYo({
        normalFill: "#A0A0A0"
    });
    $("#rateYo_ratedfill").rateYo({
        ratedFill: "#EF6F6C",
        rating: 2.7
    });
    $("#rateYo_multicolor").rateYo({
        rating    : 1.6,
        spacing   : "5px",
        multiColor: {

            "startColor": "#00cc99",
            "endColor"  : "#EF6F6C"
        }
    });
    $("#rateYo_numstars").rateYo({
        rating:2.6,
        numStars: 7
    });
    $("#rateYo_maxval").rateYo({
        maxValue: 1,
        numStars: 1,
        rating: getRandomRating(0, 1),
        onSet: updateCounter,
        onChange: updateCounter,
        starWidth: "32px"
    });
    $("#rateYo_precission").rateYo({
        precision: 2,
        rating: getRandomRating(),
        onSet: updateCounter,
        onChange: updateCounter
    });
    $("#rateYo_rating").rateYo({
        rating: "50%",
        precision: 0,
        onSet: updateCounter,
        onChange: updateCounter
    });
    $("#rateYo_halfstar").rateYo({
        rating: 1.5,
        halfStar: true
    });
    // End of starrability

    // Advanced starrability
    $("#rateYo_fullstar").rateYo({
        rating: 2,
        fullStar: true
    });
    $("#rateYo_readonly").rateYo({
        rating: 3.2,
        readOnly: true
    });
    $("#rateYo_spacing").rateYo({
        rating: 3.2,
        spacing: "10px",
        onSet: updateCounter,
        onChange: updateCounter
    });

    $("#rateYo_rtl").rateYo({
        rating: 3.2,
        rtl: true,
        onSet: updateCounter,
        onChange: updateCounter
    });
    $("#rateYo_onset").rateYo({
        onSet: function (rating, rateYoInstance) {
            swal({
                title: "Rating is set to: " + rating,
                confirmButtonColor: '#4fb7fe'
            }).done();
        }
    });
    $("#rateYo_onchange").rateYo({
        rating:3.2,
        onSet: updateCounter,
        onChange: function (rating, rateYoInstance) {
            $(this).next().text(rating);
        }
    });
    var $rateYo = $("#rateYo_rate").rateYo({
        rating:2.2
    });

    $("#get_rating").on("click",function () {

        /* get rating */
        var rating = $rateYo.rateYo("rating");
        swal({
            title: "Its " + rating + " Yo!",
            confirmButtonColor: '#4fb7fe'
        }).done();
    });

    $("#set_rating").on("click",function () {
        /* set rating */
        var rating = getRandomRating();
        $rateYo.rateYo("rating", rating);
        return false;
    });
    var $rateYo1 = $("#rateYo_destroy").rateYo({
        rating:3.2
    });
    $("#destroy").on("click",function () {
        $rateYo1.rateYo("destroy");
        return false;
    });
    $("#initialize").on("click",function () {
        $rateYo1.rateYo();
        return false;
    });
    function getRandomRating (min, max) {

        min = min || 0;
        max = max || 5;

        var randomRating = parseFloat(((Math.random())*max).toFixed(2));

        randomRating = randomRating < min? min : randomRating;

        return randomRating;
    }
    // Advanced starrability
});
