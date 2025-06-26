"""
Basis Pengetahuan Sistem Pakar Konsultasi Ekonomi
Metode: Certainty Factor (CF)
Dikembangkan untuk mendiagnosis permasalahan keuangan pribadi secara valid dan akurat.
"""

# ------------------ DAFTAR GEJALA ------------------
GEJALA = {
    'G01': 'Pendapatan tidak mencukupi kebutuhan dasar',
    'G02': 'Kesulitan membayar cicilan atau utang',
    'G03': 'Tidak memiliki tabungan atau dana darurat',
    'G04': 'Pengeluaran bulanan lebih besar dari pemasukan',
    'G05': 'Kesulitan mengatur anggaran bulanan',
    'G06': 'Investasi tidak menghasilkan keuntungan atau merugi',
    'G07': 'Penggunaan kartu kredit untuk kebutuhan pokok',
    'G08': 'Tidak memiliki rencana pensiun atau masa tua',
    'G09': 'Minim pemahaman produk keuangan & investasi',
    'G10': 'Sering terlambat membayar tagihan bulanan',
    'G11': 'Tidak memiliki asuransi (kesehatan, jiwa, aset)',
    'G12': 'Terpengaruh inflasi secara signifikan',
    'G13': 'Tidak memiliki pendapatan tetap',
    'G14': 'Ketergantungan pada pinjaman online',
    'G15': 'Tidak pernah mencatat keuangan pribadi',
}

# ------------------ DAFTAR MASALAH EKONOMI ------------------
MASALAH = {
    'E01': {
        'nama': 'Manajemen Keuangan Buruk',
        'penyebab': 'Kurangnya literasi finansial dan kebiasaan buruk dalam pengelolaan uang.',
        'deskripsi': 'Pengeluaran tidak terkendali, tidak adanya pencatatan keuangan, dan kesulitan mengatur anggaran.',
        'solusi': 'Mulai mencatat pengeluaran, evaluasi kebiasaan konsumsi, buat anggaran bulanan realistis.'
    },
    'E02': {
        'nama': 'Krisis Keuangan Pribadi',
        'penyebab': 'Pendapatan rendah atau beban utang tinggi tanpa perencanaan.',
        'deskripsi': 'Tidak mampu memenuhi kebutuhan pokok dan membayar utang secara teratur.',
        'solusi': 'Buat skala prioritas, cari sumber pendapatan tambahan, dan restrukturisasi utang.'
    },
    'E03': {
        'nama': 'Ketidaksiapan Finansial Jangka Panjang',
        'penyebab': 'Tidak adanya tabungan, dana pensiun, atau asuransi sebagai proteksi.',
        'deskripsi': 'Rentan menghadapi kejadian tak terduga, tidak siap pensiun.',
        'solusi': 'Mulai menabung, siapkan dana darurat, investasikan pada instrumen aman, dan miliki asuransi.'
    },
    'E04': {
        'nama': 'Rendahnya Literasi Keuangan',
        'penyebab': 'Kurang pengetahuan soal keuangan & produk investasi.',
        'deskripsi': 'Rentan penipuan, sulit membuat keputusan finansial, tidak memahami risiko investasi.',
        'solusi': 'Ikuti pelatihan, baca buku keuangan, konsultasi dengan perencana keuangan bersertifikat.'
    },
    'E05': {
        'nama': 'Kecanduan Utang Konsumtif',
        'penyebab': 'Gaya hidup tinggi tidak sesuai pemasukan, sering berutang untuk konsumsi.',
        'deskripsi': 'Susah lepas dari pinjaman online, kartu kredit, dan cicilan.',
        'solusi': 'Kurangi konsumsi non-esensial, lunasi utang konsumtif, dan ubah gaya hidup.'
    }
}

# ------------------ ATURAN DIAGNOSIS (RULES) ------------------
# Setiap aturan menghubungkan gejala-gejala ke suatu masalah dengan nilai CF
RULES = [
    {
        'id': 'R01',
        'gejala': ['G01', 'G04', 'G05', 'G15'],
        'masalah': 'E01',
        'certainty': 0.85
    },
    {
        'id': 'R02',
        'gejala': ['G01', 'G02', 'G10', 'G14', 'G13'],
        'masalah': 'E02',
        'certainty': 0.92
    },
    {
        'id': 'R03',
        'gejala': ['G03', 'G08', 'G11'],
        'masalah': 'E03',
        'certainty': 0.87
    },
    {
        'id': 'R04',
        'gejala': ['G09', 'G06', 'G12'],
        'masalah': 'E04',
        'certainty': 0.82
    },
    {
        'id': 'R05',
        'gejala': ['G02', 'G07', 'G14', 'G04'],
        'masalah': 'E05',
        'certainty': 0.9
    }
]

# ------------------ KELAS UNTUK AKSES BASIS PENGETAHUAN ------------------

class EconomicExpert:
    def __init__(self):
        self.gejala = GEJALA
        self.masalah = MASALAH
        self.rules = RULES

    def get_gejala(self):
        return self.gejala

    def get_masalah(self):
        return self.masalah

    def get_rules(self):
        return self.rules


# ------------------ KELAS SISTEM PAKAR ------------------
class EconomicExpert:
    def __init__(self):
        self.rules = RULES
        self.issues = MASALAH
        self.symptoms = GEJALA

    def diagnose(self, selected_symptoms):
        """
        Fungsi utama diagnosis berdasarkan gejala terpilih dan perhitungan Certainty Factor.
        """
        results = []
        for rule in self.rules:
            matched = set(rule['gejala']) & set(selected_symptoms)
            if matched:
                match_ratio = len(matched) / len(rule['gejala'])
                cf = round(rule['certainty'] * match_ratio, 4)
                if cf >= 0.5:  # Threshold diagnosis layak tampil
                    issue_code = rule['masalah']
                    issue_data = self.issues[issue_code]
                    results.append({
                        'kode': issue_code,
                        'nama': issue_data['nama'],
                        'penyebab': issue_data['penyebab'],
                        'deskripsi': issue_data['deskripsi'],
                        'solusi': issue_data['solusi'],
                        'certainty': round(cf * 100, 2)
                    })

        # Urutkan hasil berdasarkan nilai CF tertinggi
        results.sort(key=lambda x: x['certainty'], reverse=True)

        # Filter hasil unik
        unique_results = []
        seen = set()
        for result in results:
            if result['kode'] not in seen:
                unique_results.append(result)
                seen.add(result['kode'])

        return unique_results
