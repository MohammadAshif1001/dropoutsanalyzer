<div class="owl-carousel owl-theme" id="slider" style=margin-top:1em;>
    <div class="item">
        <img src="include/Img/1.png" class="d-block w-100">
    </div>
    <div class="item">
        <img src="include/Img/2.png" class="d-block w-100">
    </div>
    <div class="item">
        <img src="include/Img/3.png" class="d-block w-100">
    </div>
    <div class="item">
        <img src="include/Img/4.png" class="d-block w-100">
    </div>
</div>


</div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js"></script>

<script>
$(document).ready(function() {
    $('#slider.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        autoplay: true,
        dots: false,
        autoplayTimeout: 3000,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 3
            }
        }
    });
});
</script>
<script>
$(document).ready(function() {
    $('#pro_slider.owl-carousel').owlCarousel({
        loop: true,
        nav: false,
        autoplay: true,
        dots: false,
        autoplayTimeout: 3000,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    });
});
</script>
<!-- Carousel End -->