// Toggle between adding and removing the "active" class to the hamburger icon
document.querySelector('.hamburger').addEventListener('click', function() {
    this.classList.toggle('active');
});




// Generate random data
function generateRandomData(count) {
    const data = [];
    for (let i = 0; i < count; i++) {
        data.push(Math.floor(Math.random() * 100));
    }
    return data;
}

// Bar Chart
const barChartCanvas = document.getElementById('barChartCanvas');
new Chart(barChartCanvas, {
    type: 'bar',
    data: {
        labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'],
        datasets: [{
            label: 'Bar Chart',
            data: generateRandomData(5),
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
            borderWidth: 1
        }]
    },
    options: {}
});

// Pie Chart
const pieChartCanvas = document.getElementById('pieChartCanvas');
new Chart(pieChartCanvas, {
    type: 'pie',
    data: {
        labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'],
        datasets: [{
            data: generateRandomData(5),
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                'rgba(255, 206, 86, 0.6)',
                'rgba(75, 192, 192, 0.6)',
                'rgba(153, 102, 255, 0.6)',
            ]
        }]
    },
    options: {}
});

// Line Chart
const lineChartCanvas = document.getElementById('lineChartCanvas');
new Chart(lineChartCanvas, {
    type: 'line',
    data: {
        labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'],
        datasets: [{
            label: 'Line Chart',
            data: generateRandomData(5),
            borderColor: 'rgba(255, 99, 132, 0.6)',
            borderWidth: 2,
            fill: false
        }]
    },
    options: {}
});

// Doughnut Chart
const doughnutChartCanvas = document.getElementById('doughnutChartCanvas');
new Chart(doughnutChartCanvas, {
    type: 'doughnut',
    data: {
        labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'],
        datasets: [{
            data: generateRandomData(5),
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                'rgba(255, 206, 86, 0.6)',
                'rgba(75, 192, 192, 0.6)',
                'rgba(153, 102, 255, 0.6)',
            ]
        }]
    },
    options: {}
});



// JavaScript to handle scrolling when the button is clicked
document.addEventListener("DOMContentLoaded", function() {
    const scrollRightButton = document.getElementById("scrollRightButton");
    const mapContainer = document.querySelector(".map-container");

    scrollRightButton.addEventListener("click", function() {
        mapContainer.scrollLeft += 100; // Adjust scroll amount as needed
    });
});









