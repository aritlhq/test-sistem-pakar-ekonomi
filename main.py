from flask import Flask, render_template, request, redirect, url_for, jsonify
from expert_system.knowledge_base import GEJALA
from expert_system.inference_engine import diagnose, get_all_symptoms
from expert_system.utils import format_diagnosis_result, format_symptoms_list

app = Flask(__name__)


@app.route('/')
def index():
    """
    Menampilkan halaman utama dengan form untuk memilih gejala ekonomi.
    """
    gejala = get_all_symptoms()
    gejala_html = format_symptoms_list(gejala)
    return render_template('index.html', gejala_html=gejala_html)


@app.route('/diagnose', methods=['POST'])
def perform_diagnosis():
    """
    Melakukan analisis masalah ekonomi berdasarkan gejala yang dipilih.
    """
    selected_gejala = request.form.getlist('gejala')
    if not selected_gejala:
        return redirect(url_for('index'))

    # Panggil mesin inferensi
    diagnosis_result = diagnose(selected_gejala)

    # Format HTML untuk tampilan quick preview
    result_html = format_diagnosis_result(diagnosis_result)

    # Mapping kode gejala ke deskripsi
    selected_symptoms = [GEJALA[code] for code in selected_gejala if code in GEJALA]

    # Siapkan struktur diagnosis default
    diagnosis = {
        "main_issue": "Tidak Diketahui",
        "certainty": 0,
        "description": "Tidak ada deskripsi tersedia.",
        "recommendations": [],
        "conditions": []
    }

    # Jika ada hasil diagnosa, bangun data untuk template
    if diagnosis_result.get('status') == 'success' and diagnosis_result.get('issues'):
        issues = diagnosis_result['issues']
        main = issues[0]
        # Susun list kondisi dengan level berdasarkan persentase
        conditions = []
        for issue in issues:
            pct = issue['certainty']
            if pct >= 75:
                lvl = 'High'
            elif pct >= 50:
                lvl = 'Medium'
            else:
                lvl = 'Low'
            conditions.append({
                'name': issue['nama'],
                'value': pct,
                'level': lvl
            })
        # Susun rekomendasi
        recommendations = [main['solusi']]

        diagnosis = {
            'main_issue': main['nama'],
            'certainty': main['certainty'],
            'description': main['deskripsi'],
            'recommendations': recommendations,
            'conditions': conditions
        }

    return render_template(
        'result.html',
        result_html=result_html,
        selected_symptoms=selected_symptoms,
        diagnosis=diagnosis
    )


@app.route('/konsultasi')
def konsultasi():
    """
    Menampilkan halaman konsultasi ekonomi.
    """
    return render_template('konsultasi.html')


@app.route('/tentang')
def tentang():
    """
    Menampilkan halaman tentang sistem pakar ekonomi.
    """
    return render_template('tentang.html')


@app.route('/api/statistik')
def api_statistik():
    """
    API dummy untuk data statistik. Sebaiknya ambil dari database.
    """
    data = {
        'tren': {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei'],
            'values': [5, 10, 8, 15, 12]
        },
        'distribusi': {
            'labels': ['Inflasi', 'Pengangguran', 'Utang', 'Tabungan Rendah'],
            'values': [12, 7, 5, 10]
        }
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
