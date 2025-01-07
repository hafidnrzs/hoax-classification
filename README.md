# Hoax Classification

Project klasifikasi berita hoax bahasa Indonesia menggunakan machine learning. Terdapat antarmuka pengguna untuk memasukkan teks narasi dan mendapatkan prediksi apakah narasi tersebut hoax atau tidak.

## Project Structure

```
hoax-classification
├── app.py               # File utama aplikasi Streamlit
├── models
│   └── model.py         # Implementasi model klasifikasi
├── data
│   └── dataset.csv      # Dataset training dan testing
├── requirements.txt     # Dependency Python untuk proyek
└── README.md            # Dokumentasi proyek
```

## Cara Install

1. Clone repository

2. Install package yang dibutuhkan:
   ```
   pip install -r requirements.txt
   ```

## Penggunaan

Untuk menjalankan aplikasi Streamlit, jalankan perintah berikut:

```
streamlit run app.py
```

Buka browser dan masukkan URL `http://localhost:8501` untuk mengakses aplikasi.
