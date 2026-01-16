# Proyek Analisis Data: Bike Sharing Dataset

## Informasi Umum

* **Nama**: Andi Bachdar
* **Email**: [andibahdar44@gmail.com](mailto:andibahdar44@gmail.com)
* **ID Dicoding**: andibahdar
* **Dataset**: Bike Sharing Dataset (day.csv)

---

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis data terhadap Bike Sharing Dataset guna memahami pola penggunaan sepeda berdasarkan faktor waktu, musim, dan jenis hari (hari kerja vs akhir pekan).
Hasil analisis disajikan dalam bentuk **notebook analisis data** serta **dashboard interaktif menggunakan Streamlit**.

---

## Struktur Direktori

```
submission/
├── dashboard/
│   ├── dashboard.py
│   └── day.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt (opsional, jika deploy Streamlit Cloud)
```

---

## Tahapan Analisis Data

1. **Data Gathering**
   Menggunakan dataset `day.csv` dari Bike Sharing Dataset.

2. **Assessing Data**
   Pemeriksaan struktur data, tipe data, dan missing value menggunakan `info()`, `isna()`, dan `describe()`.

3. **Cleaning Data**

   * Konversi kolom kategori (`season`, `weathersit`, `workingday`) dari kode numerik menjadi label kategorikal.
   * Konversi kolom `dteday` menjadi format datetime.
   * Tidak dilakukan penghapusan data karena dataset tidak memiliki missing value.

4. **Exploratory Data Analysis (EDA)**
   Eksplorasi tren peminjaman sepeda berdasarkan waktu, musim, dan jenis hari.

5. **Visualization & Explanatory Analysis**
   Visualisasi untuk menjawab pertanyaan bisnis yang telah ditentukan.

6. **Dashboard**
   Penyajian hasil analisis dalam bentuk dashboard interaktif menggunakan Streamlit.

---

## Cara Menjalankan Dashboard (Local)

1. Aktifkan virtual environment:

   ```
   source venv/bin/activate
   ```

2. Install dependency:

   ```
   pip install -r requirements.txt
   ```

3. Masuk ke folder dashboard:

   ```
   cd dashboard
   ```

4. Jalankan dashboard:

   ```
   streamlit run dashboard.py
   ```

5. Dashboard dapat diakses melalui browser pada:

   ```
   http://localhost:8501
   ```

---

## Insight Utama

* Musim **Summer** dan **Fall** menunjukkan rata-rata peminjaman sepeda tertinggi.
* Musim **Winter** memiliki tingkat peminjaman terendah akibat kondisi cuaca.
* Hari kerja memiliki peminjaman yang lebih stabil dan cenderung lebih tinggi dibandingkan akhir pekan.
* Akhir pekan menunjukkan variasi penggunaan yang lebih besar, mengindikasikan aktivitas rekreasi.

---

## Kesimpulan

Analisis ini menunjukkan bahwa faktor musim dan jenis hari sangat memengaruhi pola penggunaan layanan bike sharing. Informasi ini dapat dimanfaatkan untuk perencanaan operasional, promosi musiman, dan pengambilan keputusan bisnis berbasis data.
