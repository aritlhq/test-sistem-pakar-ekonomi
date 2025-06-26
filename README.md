# 📊 Sistem Pakar Ekonomi

Proyek ini adalah aplikasi web sederhana berbasis **Flask (Python)** yang dirancang untuk menerapkan konsep sistem pakar dalam konteks ekonomi. Aplikasi ini dapat diakses melalui browser dan menampilkan antarmuka berbasis HTML, CSS, dan JavaScript.

Kelompok 1:
- Hanif Maulana Ar Rasyid - [Github](https://github.com/manap01)
- Muhammad Faqih Alharits - [Github](https://github.com/aritlhq) 
- Firza Aditiya Ardiansah - [Github](https://github.com/firzaaditiya)
- Rifky Firmansyah - [Github](https://github.com/Rifkyyyyyyyy)
- .... (2 orang sisanya pada afk)

## 📁 Struktur Proyek

```
SISTEM-PAKAR-EKONOMI/
├── env/                # Virtual environment (jangan diubah)
├── expert_system/      # Logika sistem pakar (Python)
├── static/             # File statis seperti CSS, JS, dan gambar
├── templates/          # File HTML (template Jinja2)
├── .idea/              # Konfigurasi IDE (opsional)
```

## ✅ Prasyarat

Pastikan Anda telah menginstal:

* **Python 3.8+**
* **pip** (biasanya sudah terpasang bersama Python)

## 🛠️ Langkah Instalasi

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek secara lokal:

### 1. Clone repositori

```bash
git clone https://github.com/aritlhq/test-sistem-pakar-ekonomi
cd test-sistem-pakar-ekonomi
```

### 2. Aktifkan Virtual Environment

Jika direktori `env/` sudah ada, aktifkan environment:

#### 💻 Windows:

```bash
.\env\Scripts\activate
```

#### 🐧 Linux / 🖥️ MacOS:

```bash
source env/bin/activate
```

> Jika belum ada, buat environment baru:

```bash
python -m venv env
source env/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

> Jika file `requirements.txt` belum tersedia, install manual:

```bash
pip install flask
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`.

## 🧠 Fitur Utama

* Antarmuka web berbasis Flask
* Struktur modular menggunakan template dan static folder
* Logika sistem pakar dapat dikembangkan di folder `expert_system/`

## 👨‍💻 Kontribusi

Silakan fork dan buat pull request jika ingin mengembangkan fitur baru atau memperbaiki bug.

---

Jika kamu ingin saya buatkan juga isi file `app.py`, `requirements.txt`, atau struktur modular lainnya, tinggal beri tahu saja!
