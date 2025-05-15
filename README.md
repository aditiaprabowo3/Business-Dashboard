# Proyek Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di seluruh negeri. Walaupun telah berkembang pesat, perusahaan menghadapi tantangan signifikan dalam mengelola karyawan, terutama tingginya **attrition rate** atau tingkat keluar karyawan. Dengan angka attrition yang melebihi **10%**, perusahaan mulai merasakan dampak negatif seperti:
- **Biaya Rekrutmen Tinggi**: Berdasarkan karakteristik perusahaan yang memiliki lebih dari 1.000 karyawan, biaya yang dikeluarkan untuk proses rekrutmen dan pelatihan karyawan baru meningkat seiring tingginya angka pergantian karyawan. Hal ini mencakup biaya iklan lowongan kerja, seleksi, onboarding, dan pelatihan.
- **Penurunan Produktivitas**: Tingginya pergantian karyawan menyebabkan hilangnya pengalaman dan keterampilan yang dibutuhkan untuk mencapai target bisnis. Data dalam dataset seperti **YearsAtCompany** dan **YearsWithCurrManager** dapat membantu mengukur kontribusi pengalaman terhadap produktivitas.
- **Penurunan Kepuasan Karyawan**: Indikator kepuasan seperti **Job Satisfaction**, **Work-Life Balance**, dan **Environment Satisfaction** dalam dataset menunjukkan pentingnya mengidentifikasi ketidakpuasan lebih awal untuk mencegah gelombang keluar karyawan.

Manajemen HR di Jaya Jaya Maju menyadari pentingnya memahami faktor-faktor penyebab attrition agar dapat menyusun strategi yang tepat untuk **meningkatkan retensi karyawan** dan **mengurangi attrition rate** secara signifikan.

### Permasalahan Bisnis
Permasalahan bisnis yang akan diselesaikan melalui proyek ini adalah:
1. **Mengidentifikasi faktor-faktor utama yang mempengaruhi attrition rate** di perusahaan, baik dari segi demografis, kepuasan kerja, maupun metrik finansial.
2. **Mengukur tingkat kepuasan karyawan** berdasarkan parameter seperti **Job Satisfaction**, **Work-Life Balance**, dan **Environment Satisfaction**.
3. **Menentukan pola perilaku karyawan yang cenderung keluar**, seperti pengaruh jarak rumah ke kantor, lembur berlebihan (OverTime), dan pendapatan karyawan.
4. **Menyediakan alat bantu berupa business dashboard** yang memudahkan manajemen HR memantau dan menganalisis faktor-faktor penyebab attrition secara berkala.

Dengan menyelesaikan permasalahan ini, perusahaan diharapkan dapat:
- Mengurangi **attrition rate** dengan mengambil langkah pencegahan yang tepat.
- Menyusun program retensi yang lebih efektif.
- Meningkatkan kepuasan kerja dan produktivitas karyawan.

### Cakupan Proyek
Proyek ini mencakup:
1. **Eksplorasi dan Pemahaman Data**: Analisis dataset `employee_data.csv` untuk memahami karakteristik karyawan dan distribusi attrition.
2. **Data Preparation**: Membersihkan dan memproses data agar siap digunakan untuk analisis lebih lanjut.
3. **Analisis Faktor Penyebab Attrition**:
   - Analisis korelasi antara variabel seperti pendapatan, lembur, tingkat kepuasan, dan jarak rumah.
   - Visualisasi tren dan pola attrition di berbagai departemen, level pekerjaan, dan usia karyawan.
4. **Pembuatan Business Dashboard**: Visualisasi data dalam bentuk dashboard yang mudah dipahami untuk memantau faktor penyebab attrition.
5. **Kesimpulan dan Rekomendasi**: Menarik kesimpulan dari hasil analisis dan memberikan rekomendasi praktis untuk mengurangi attrition.

### Persiapan
**Sumber data**: Dataset yang digunakan adalah [Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) sesuai instruksi submission.
**Setup environment**:  
Proyek ini membutuhkan **Java Runtime Environment (JRE)** dan file **`metabase.jar`** untuk menjalankan dashboard secara lokal.

1. Menjalankan `notebook.ipynb`  
   - Pastikan dependensi, packages, dan library yang dibutuhkan sudah tersedia (lihat file `requirements.txt` untuk detail dependensi).  
   - Jalankan seluruh isi file `notebook.ipynb` menggunakan Google Colab atau Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.

2. **Menjalankan Dashboard**:  
   Untuk melihat isi dashboard secara langsung, dapat menggunakan **Metabase** dengan menjalankan file `metabase.jar`.

   - Pastikan Java Runtime sudah terinstall. Cek dengan perintah:  
     ```bash
     java -version
     ```

     Kalau belum ada, install Java dari:
     https://www.java.com/en/download/

   - Unduh file `metabase.jar` dari:  
     https://www.metabase.com/start/jar.html

   - Buka terminal (Mac/Linux) atau Command Prompt (Windows), lalu pindah ke folder tempat `metabase.jar` berada.

     Contoh:  
     - Windows:  
       ```cmd
       cd C:\Users\username\Downloads\metabase
       ```  
     - Mac/Linux:  
       ```bash
       cd /Users/username/Downloads/metabase
       ```

   - Setelah masuk ke dalam folder yang menyimpan metabase.jar, Jalankan Metabase dengan perintah:  
     ```bash
     java -jar metabase.jar
     ```

   - Buka browser dan akses:  
     ```
     http://localhost:3000
     ```
     
   - Login ke Metabase menggunakan username dan password berikut:
     ```
     username: root@mail.com
     password: root123
     ```

---

## Business Dashboard
Hasil dari analisis dan model prediktif dapat divisualisasikan dalam bentuk dashboard untuk membantu tim HR memantau dan memahami attrition secara real-time. Berikut adalah elemen-elemen yang dapat disertakan dalam dashboard:
1. **Tren Attrition**:
   - Distribusi attrition berdasarkan fitur seperti **OverTime**, **MonthlyIncome**, dan **YearsAtCompany**.
2. **Feature Importance**:
   - Visualisasi kontribusi fitur utama seperti **OverTime_Yes** dan **MonthlyIncome** terhadap risiko attrition.
3. **Prediksi Risiko**:
   - Menampilkan daftar karyawan dengan risiko tinggi berdasarkan hasil prediksi model XGBoost.

 ### Tutorial Mengakses Dashboard
 **Menggunakan Metabase**
 1. Buka aplikasi Metabase di browser Anda (Menggunakan Docker)
 2. Username dan Password untuk masuk ke Metabase:
    username:`root@mail.com`
    password: `root123`

## Conclusion
Proyek ini berhasil mencapai tujuan utama yaitu:
1. **Mengidentifikasi faktor utama penyebab attrition**:
   - Faktor terpenting adalah lembur berlebihan (**OverTime**), pendapatan rendah (**MonthlyIncome**), dan masa kerja pendek.
2. **Membangun model prediktif yang akurat**:
   - Model XGBoost memberikan performa terbaik dengan **accuracy 84.94%** dan metrik lainnya yang tinggi.
3. **Memberikan rekomendasi actionable**:
   - Tim HR dapat mengimplementasikan kebijakan untuk mengurangi lembur, menyesuaikan skala gaji, dan memperkuat retensi karyawan baru.

### Rekomendasi Action Items untuk Perusahaan
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
1. **Kurangi Lembur Berlebihan**:
   - Berikan program kerja fleksibel untuk meningkatkan keseimbangan kerja-hidup.
2. **Kaji Skala Gaji**:
   - Sesuaikan gaji karyawan agar kompetitif di pasar dan berikan insentif tambahan.
3. **Perkuat Retensi Karyawan Baru**:
   - Implementasikan program onboarding dan mentoring untuk karyawan dengan masa kerja pendek.
4. **Gunakan Model Prediktif**:
   - Integrasikan model XGBoost untuk memonitor risiko secara real-time melalui dashboard HR.
