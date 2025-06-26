"""
Mesin inferensi untuk sistem pakar konsultasi ekonomi pribadi.
File ini berisi fungsi-fungsi untuk melakukan inferensi berdasarkan
gejala ekonomi yang dipilih oleh pengguna.
Implementasi tanpa PyKnow untuk menghindari masalah kompatibilitas.
"""
from .knowledge_base import EconomicExpert, GEJALA, MASALAH

def diagnose(selected_gejala):
    """
    Melakukan diagnosis berdasarkan gejala yang dipilih.
    
    Args:
        selected_gejala: List kode gejala yang dipilih pengguna
        
    Returns:
        Dictionary hasil diagnosis yang berisi informasi masalah ekonomi atau
        pesan jika tidak ada yang teridentifikasi
    """
    # Inisialisasi sistem pakar ekonomi
    expert = EconomicExpert()
    
    # Melakukan diagnosis
    issues_found = expert.diagnose(selected_gejala)
    
    # Hasil diagnosis
    if issues_found:
        return {
            'status': 'success',
            'issues': issues_found
        }
    else:
        return {
            'status': 'not_found',
            'message': 'Tidak dapat mendiagnosis masalah ekonomi berdasarkan gejala yang dipilih. Mohon pilih lebih banyak gejala atau konsultasikan dengan konsultan keuangan.'
        }

def get_all_symptoms():
    """
    Mendapatkan semua gejala ekonomi yang tersedia.
    
    Returns:
        Dictionary gejala dengan kode dan deskripsi
    """
    return GEJALA

def get_all_issues():
    """
    Mendapatkan semua masalah ekonomi yang tersedia.
    
    Returns:
        Dictionary masalah dengan informasi lengkap
    """
    return MASALAH