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
**Sumber data**: 

Dataset yang digunakan berasal dari perusahaan Jaya Jaya Maju, sebuah organisasi multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan di berbagai wilayah operasionalnya.
Data ini mencakup informasi demografis dan pekerjaan karyawan, seperti usia, pendapatan, masa kerja, dan status pekerjaan. Dataset ini digunakan untuk menganalisis berbagai faktor yang memengaruhi tingkat attrition (keluarnya karyawan) di perusahaan tersebut.

Dataset dapat diakses melalui:
https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee
 
**Setup environment**:  

Proyek ini membutuhkan Java Runtime Environment (JRE) dan file metabase.jar untuk menjalankan dashboard secara lokal. Selain itu, untuk bagian analisis data, diperlukan Python beserta dependensi yang terinstal melalui virtual environment.

**Setup Python Environment**

Pastikan kamu sudah menginstall Python dan pip di komputer kamu.
Untuk memudahkan manajemen paket, gunakan virtual environment. Berikut contoh menggunakan pipenv:

1. **Install pipenv jika belum terinstal**

```bash
pip install pipenv
```

2. **Inisialisasi environment & install dependensi dari Pipfile**
```bash
pipenv install
```

3. **Masuk ke dalam virtual environment**
```bash
pipenv shell
```

4. **Jika menggunakan requirements.txt, jalankan perintah berikut setelah masuk virtual environment:**
```bash
pip install -r requirements.txt
```

**Setup Java Environment dan Menjalankan Business Dashboard**

Dashboard dijalankan menggunakan Metabase yang memerlukan Java Runtime Environment (JRE).

1. **Menjalankan `notebook.ipynb`**  
   - Pastikan dependensi, packages, dan library yang dibutuhkan sudah tersedia (lihat file `requirements.txt` untuk detail dependensi).  
   - Jalankan seluruh isi file `notebook.ipynb` menggunakan Google Colab atau Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.

2. **Menjalankan Dashboard**:  
   Untuk melihat isi dashboard secara langsung, dapat menggunakan **Metabase** dengan menjalankan file `metabase.jar` pada terminal atau command prompt.

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

**Menjalankan File Prediksi pada streamlit**

```bash
streamlit run app.py
```
---

## Business Dashboard

![Business Dashboard](https://github.com/user-attachments/assets/12c69f37-16a3-48e4-bd73-8a62cc3952d4)

Hasil dari analisis dan model prediktif dapat divisualisasikan dalam bentuk dashboard untuk membantu tim HR memantau dan memahami attrition secara real-time. Berikut adalah elemen-elemen yang dapat disertakan dalam dashboard:

**1. Ringkasan Karyawan**:
Menampilkan metrik-metrik kunci terkait tenaga kerja perusahaan:

- **Rata-rata Usia**: 37.06 tahun
- **Jumlah Total Karyawan**: 1.058 orang
- **Jumlah Job Role**: 9 jenis peran
- **Jumlah Departemen**: 3 divisi
- **Rata-rata Lama Bekerja (YearsAtCompany)**: 7,07 tahun
- **Rata-rata Kepuasan Kerja (JobSatisfaction)**: 2,75 poin
  
Tujuan: Memberikan overview cepat terhadap struktur dan kondisi umum tenaga kerja.

**2. Tingkat Resign Berdasarkan Gender**:
Visualisasi ini membandingkan tingkat attrition (keluar) antara laki-laki dan perempuan.
- **Laki-Laki**: 17,42%
- **Perempuan**: 16,21%
  
Tujuan: melihat apakah ada pola tertentu terkait gender dalam keputusan untuk keluar dari perusahaan.

**3. Attrition per Departemen**:
Grafik ini menampilkan:
- Jumlah total pegawai per departemen
- Jumlah pegawai yang resign
- Tingkat attrition per departemen

Contoh:
- Sales memiliki attrition rate tertinggi: 20,69%
- Research & Development: 15,26%
- Human Resources: 15,79%
  
Tujuan: Visual ini berguna untuk mengetahui divisi mana yang paling rentan terhadap turnover.

**4. Pengaruh Work-Life Balance terhadap Resign**:
Menjelaskan hubungan antara skor work-life balance (skala 1–4) dengan jumlah karyawan yang keluar.
- Mengelompokkan attrition berdasarkan tingkat work-life balance (skala 1–4).
- Tingkat 3 menunjukkan jumlah tertinggi karyawan keluar (94 orang), diikuti oleh tingkat 2 dan 4.
  
Tujuan: Ini bisa membantu HR mengevaluasi kebijakan fleksibilitas kerja dan keseimbangan hidup karyawan.

**5. Rata-Rata Pendapatan: Karyawan Aktif vs Resign**:
Grafik ini membandingkan rata-rata pendapatan bulanan antara:
- Karyawan yang masih aktif
- Karyawan yang sudah resign
Hasilnya menunjukkan:
   - Karyawan yang resign memiliki rata-rata gaji lebih rendah ($4.872) dibanding yang tetap bertahan ($6.982).
  
Tujuan: Melihat apakah pendapatan berkorelasi dengan attrition—menarik karena yang resign justru bergaji lebih tinggi.

**6. Attrition Berdasarkan Job Role**:
Menampilkan total pegawai dan tingkat attrition di setiap jenis peran pekerjaan:
- Role Sales Representative mencatat attrition tertinggi (43.1%), meskipun jumlah karyawannya sedikit.
  
Tujuan: Menggali peran kerja mana yang paling tidak stabil secara retensi.

## Tujuan Dashboard:
- Memberikan gambaran menyeluruh dan interaktif tentang kondisi SDM perusahaan.
- Mengidentifikasi faktor-faktor utama penyebab attrition, baik dari segi demografi, departemen, pendapatan, hingga persepsi work-life balance.
- Memberikan insight visual yang mudah dipahami untuk manajer dan tim HR.
- Mendukung pengambilan keputusan strategis oleh tim HR untuk menekan tingkat keluar masuk karyawan dan meningkatkan retensi.
- Menjadi acuan data-driven untuk strategi rekrutmen, kompensasi, dan pengembangan karyawan ke depan.

## Menjalankan Sistem Machine Learning

Untuk menjalankan prototype sistem machine learning yang telah dibuat, ikuti langkah-langkah berikut ini:
> **Link Akses Dashboard**: [Lihat di StreamlitOnline](https://aditiaprabowo3-business-dashboard-app-julqkf.streamlit.app/)

![prediksi impement](https://github.com/user-attachments/assets/8d5654d5-2bd9-4fd4-8e10-5f35914055dc)
dengan prototype machine learning ini perusahaan dapat **meningkatkan retensi karyawan, mengurangi biaya rekrutmen, serta menciptakan lingkungan kerja yang lebih stabil dan produktif.**

Untuk menjalankan proyek HR Analytics ini secara lokal, silakan ikuti panduan berikut:

### Clone Repository

Clone repositori ke komputer lokal Anda menggunakan perintah berikut:

```bash
git clone https://github.com/aditiaprabowo3/Business-Dashboard.git
cd Business-Dashboard
python -m venv env
venv\Scripts\activate
pip install -r requirements.txt

```
### Menjalankan Prediksi pada streamlit
```bash
streamlit run app.py
```

## Conclusion
Melalui analisis data dan visualisasi interaktif dalam bentuk business dashboard, beberapa insight penting berhasil diperoleh:
- Berdasarkan tingkat Resign pada Gender, Laki-laki sedikit lebih dominan melakukan resign dibanding perempuan.
- Sebagian besar karyawan masih aktif, namun tingkat attrition tetap perlu diwaspadai.
- Beberapa job role menunjukkan attrition yang lebih tinggi, perlu perhatian khusus (misalnya: Sales dan HR).
- Karyawan yang resign memiliki rata-rata pendapatan lebih rendah dibanding yang bertahan.
- Rata-rata usia karyawan 37 tahun, dengan rata-rata masa kerja 7 tahun — menunjukkan dominasi karyawan berpengalaman.
- Karyawan dengan skor work-life balance 2 sampai 3 paling banyak keluar, ini menandakan mereka kurang puas dengan keseimbangan antara pekerjaan dan kehidupan pribadi.

### Rekomendasi Action Items untuk Perusahaan
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
1. **Kurangi Lembur Berlebihan**:
   - Berikan program kerja fleksibel untuk meningkatkan keseimbangan kerja-hidup.
2. **Kaji Skala Gaji**:
   - Sesuaikan gaji karyawan agar kompetitif di pasar dan berikan insentif tambahan.
3. **Perkuat Retensi Karyawan Baru**:
   - Implementasikan program onboarding dan mentoring untuk karyawan dengan masa kerja pendek.
4. **Meningkatkan program pelatihan dan pengembangan karier**
   - Khususnya untuk karyawan di bidang atau peran yang memiliki tingkat attrition tinggi, seperti Sales dan HR, untuk meningkatkan loyalitas dan keinginan bertahan.
5. **Mengoptimalkan penggunaan dashboard secara berkala**
   - Agar manajer HR dapat terus memantau indikator kunci dan segera mengambil tindakan jika ada tren negatif yang muncul.
