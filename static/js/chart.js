document.addEventListener("DOMContentLoaded", function () {
    fetch("/api/statistik")
        .then(response => response.json())
        .then(data => {
            // Tren Chart
            const ctxTren = document.getElementById("trendsChart").getContext("2d");
            new Chart(ctxTren, {
                type: 'line',
                data: {
                    labels: data.tren.labels,
                    datasets: [{
                        label: 'Jumlah Kasus',
                        data: data.tren.values,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgb(75, 192, 192)',
                        borderWidth: 2,
                        tension: 0.3,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            });

            // Distribusi Chart
            const ctxDistribusi = document.getElementById("distributionChart").getContext("2d");
            new Chart(ctxDistribusi, {
                type: 'pie',
                data: {
                    labels: data.distribusi.labels,
                    datasets: [{
                        data: data.distribusi.values,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.6)',
                            'rgba(54, 162, 235, 0.6)',
                            'rgba(255, 206, 86, 0.6)',
                            'rgba(75, 192, 192, 0.6)'
                        ]
                    }]
                },
                options: {
                    responsive: true
                }
            });
        })
        .catch(error => console.error("Gagal mengambil data statistik:", error));
});
