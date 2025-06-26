document.addEventListener('DOMContentLoaded', function () {
    // Ambil elemen canvas dan baca data JSON dari atribut
    const canvas = document.getElementById('diagnosisChart');
    const labels = JSON.parse(canvas.dataset.labels);
    const values = JSON.parse(canvas.dataset.values);
    const levels = JSON.parse(canvas.dataset.levels);

    // Map level ke warna yang diinginkan
    const levelColors = {
        high:   '#dc3545', // merah
        medium: '#fd7e14', // jingga
        low:    '#20c997'  // hijau
    };
    // Susun array warna untuk setiap slice berdasarkan level masing-masing
    const colors = levels.map(lv => levelColors[lv.toLowerCase()] || '#6c757d');

    // Inisialisasi Chart.js
    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: colors,
                borderColor: '#ffffff',
                borderWidth: 2,
                hoverOffset: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            aspectRatio: 1,
            cutout: '60%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { boxWidth: 12, padding: 12, font: { size: 13 } }
                },
                tooltip: {
                    padding: 8,
                    titleFont: { size: 15 },
                    bodyFont: { size: 13 },
                    callbacks: {
                        label: ctx => `${ctx.label}: ${ctx.parsed}%`
                    }
                }
            },
            layout: { padding: { top: 12, bottom: 12 } }
        }
    });

    // Set tanggal otomatis
    const dateEl = document.getElementById('current-date');
    if (dateEl) {
        dateEl.textContent = new Date().toLocaleDateString('id-ID', {
            day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Jakarta'
        });
    }
});

// Fungsi unduh & share
function downloadPDF() {
    alert('Fitur unduh PDF akan segera tersedia');
}
function shareResult() {
    if (navigator.share) {
        navigator.share({
            title: 'Hasil Konsultasi Ekonomi Pribadi',
            text: 'Lihat hasil konsultasi ekonomi pribadi saya',
            url: window.location.href
        });
    } else {
        navigator.clipboard.writeText(window.location.href)
            .then(() => alert('Link berhasil disalin ke clipboard'));
    }
}
