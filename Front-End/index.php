<?php
include_once("include/header.php");
?>

<style>
.map-data-section {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 50vh;
    /* Adjust this value as needed */
    background-color: #f0f0f0;
    margin: 0.5em;
}

/* Container for map and data */
.map-data-container {
    max-width: 100%;
    width: 100%;
    padding: 20px;
    box-sizing: border-box;
    text-align: center;
    background-color: white;

}

/* Map container */
.map-container {
    /* Your existing styles for .map-container */
    overflow-x: hidden;
    /* Hide horizontal overflow */
    position: relative;
    box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 2px, rgba(0, 0, 0, 0.07) 0px 2px 4px, rgba(0, 0, 0, 0.07) 0px 4px 8px, rgba(0, 0, 0, 0.07) 0px 8px 16px, rgba(0, 0, 0, 0.07) 0px 16px 32px, rgba(0, 0, 0, 0.07) 0px 32px 64px;
}

.scroll-button {
    position: absolute;
    right: 10px;
    /* Adjust the position as needed */
    top: 50%;
    /* Center vertically */
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    padding: 5px 10px;
    border: none;
    cursor: pointer;
}

/* Style the scroll button when hovered */
.scroll-button:hover {
    background-color: rgba(0, 0, 0, 0.7);
}

/* Media query for mobile view */
@media (max-width: 768px) {
    .map-container {
        overflow-x: scroll;
        /* Enable horizontal scroll for mobile */
    }
}

/* Media query for mobile view */
@media (max-width: 768px) {
    .map-data-section {
        min-height: auto;
        /* Reset the minimum height */
        overflow: visible;
        /* Show content that may be hidden */
    }

    .map-data-container {
        padding: 10px;
    }
}
</style>
<!-- Img Slider 
-->
<div class="slider">
    <?php
    include_once("include/slider.php");
    ?>
</div>


<!-- Main Data Section -->

<section class="data-section">
    <div class="curved-background" style="height: 10vh; display: flex; justify-content: center; align-items: center;">
        <div class="curved-background__curved">
            <h1 style="text-align: center;">
                <strong>Dropout's Data Analysis</strong>
            </h1>
        </div>
    </div>


    <div class="data-container">
        <!-- Bar Chart -->
        <div class="graph" id="barChart">
            <canvas id="barChartCanvas"></canvas>
        </div>

        <!-- Pie Chart -->
        <div class="graph" id="pieChart">
            <canvas id="pieChartCanvas"></canvas>
        </div>

        <!-- Line Chart -->
        <div class="graph" id="lineChart">
            <canvas id="lineChartCanvas"></canvas>
        </div>

        <!-- Doughnut Chart -->
        <div class="graph" id="doughnutChart">
            <canvas id="doughnutChartCanvas"></canvas>
        </div>
    </div>
</section>


<!-- Map Data Section -->
<div class="curved-background" style="height: 10vh; display: flex; justify-content: center; align-items: center;">
    <div class="curved-background__curved">
        <h1 style="text-align: center;">
            <strong>Map-Wise Data</strong>
        </h1>
    </div>
</div>

<section class="map-data-section">
    <div class="map-data-container">
        <div class="map-container">

            <div class="curved-background"
                style="height: 10vh; display: flex; justify-content: center; align-items: center;">
                <div class="curved-background__curved">
                    <div class="tomap-container">

                    </div>
                </div>
            </div>
            <?php
            include_once("map.php");
            ?>
        </div>


    </div>

    <button class="scroll-button" id="scrollRightButton">Scroll Right</button>
    </div>
</section>
<!-- Map Data Section End-->



<!-- Profile Section-->
<div class="curved-background" style="height: 10vh; display: flex; justify-content: center; align-items: center;">
    <div class="curved-background__curved">
        <h1 style="text-align: center;">
            <strong>Profile's</strong>
        </h1>
    </div>
</div>

<div class=" owl-carousel owl-theme" id="pro_slider" style=margin-top:1em;>
    <div class="item">
        <div class="card">
            <img src="include/profile-img/img1.jpg" alt="John" style="width:100%">
            <h1>Pallav Rai</h1>
            <p class="title">CEO & Founder, Trenzcart.com</p>
            <p>Khwaja Moinudin Chisti Language University</p>
            <a href="https://github.com/pallavrai"><i class="fab fa-github"></i></a>
            <a href="#"><i class="fa fa-twitter"></i></a>
            <a href="#"><i class="fa fa-linkedin"></i></a>
            <a href="#"><i class="fa fa-facebook"></i></a>
            <p><button>Contact</button></p>
        </div>
    </div>
    <div class="item">
        <div class="card">
            <img src="include/profile-img/img.jpg" alt="John" style="width:100%">
            <h1>Mohammad Ashif</h1>
            <p class="title">CEO & Founder, CashJila.com</p>
            <p>Khwaja Moinudin Chisti Language University</p>
            <a href="https://github.com/MohammadAshif1001"><i class="fab fa-github"></i></a>
            <a href="#"><i class="fa fa-twitter"></i></a>
            <a href="#"><i class="fa fa-linkedin"></i></a>
            <a href="#"><i class="fa fa-facebook"></i></a>
            <p><button>Contact</button></p>
        </div>
    </div>
    <div class="item">
        <div class="card">
            <img src="include/profile-img/img3.jpg" alt="John" style="width:100%">
            <h1>Uknown</h1>
            <p class="title">CEO & Founder, xyz.com</p>
            <p>Khwaja Moinudin Chisti Language University</p>
            <a href="https://github.com/MohammadAshif1001"><i class="fab fa-github"></i></a>
            <a href="#"><i class="fa fa-twitter"></i></a>
            <a href="#"><i class="fa fa-linkedin"></i></a>
            <a href="#"><i class="fa fa-facebook"></i></a>
            <p><button>Contact</button></p>
        </div>
    </div>
</div>






<!-- Carousel End -->



<!-- Footer -->
<div class=" footer">
    <?php
    include_once("include/footer.php");
    ?>
</div>