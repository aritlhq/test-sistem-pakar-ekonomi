"""
Modul utilitas untuk sistem pakar ekonomi.
Berisi fungsi-fungsi untuk memformat data dan hasil diagnosis.
"""

def format_symptoms_list(symptoms_dict):
    """
    Format daftar gejala sebagai HTML untuk ditampilkan di form.
    
    Args:
        symptoms_dict: Dictionary gejala
        
    Returns:
        String HTML dengan checkbox untuk setiap gejala
    """
    html = ""
    for code, description in symptoms_dict.items():
        html += f"""
        <div class="form-check mb-2">
            <input class="form-check-input" type="checkbox" name="gejala" id="{code}" value="{code}">
            <label class="form-check-label" for="{code}">
                {description}
            </label>
        </div>
        """
    return html

def format_diagnosis_result(result):
    """
    Format hasil diagnosis sebagai HTML.
    
    Args:
        result: Dictionary hasil diagnosis dari fungsi diagnose()
        
    Returns:
        String HTML dengan hasil diagnosis
    """
    html = ""
    
    if result['status'] == 'success':
        for index, issue in enumerate(result['issues']):
            html += f"""
            <div class="card mb-4">
                <div class="card-header bg-primary text-white">
                    <h5 class="mb-0">Diagnosis #{index+1}: {issue['nama']} (Kepastian: {issue['certainty']}%)</h5>
                </div>
                <div class="card-body">
                    <h6 class="card-subtitle mb-2 text-muted">Penyebab:</h6>
                    <p>{issue['penyebab']}</p>
                    
                    <h6 class="card-subtitle mb-2 text-muted">Deskripsi:</h6>
                    <p>{issue['deskripsi']}</p>
                    
                    <h6 class="card-subtitle mb-2 text-muted">Solusi yang Disarankan:</h6>
                    <p>{issue['solusi']}</p>
                </div>
            </div>
            """
    else:
        html = f"""
        <div class="alert alert-warning">
            <h5>Hasil Tidak Ditemukan</h5>
            <p>{result['message']}</p>
        </div>
        """
    
    return html