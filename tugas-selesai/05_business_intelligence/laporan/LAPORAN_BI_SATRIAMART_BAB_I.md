# PERANCANGAN DASHBOARD BUSINESS INTELLIGENCE INTERAKTIF UNTUK MENDUKUNG KEPUTUSAN BISNIS PADA SATRIAMART

![Logo Universitas Nusa Mandiri]

**LAPORAN TUGAS AKHIR**

Diajukan untuk memenuhi salah satu tugas kelompok mata kuliah  
**Business Intelligence II**

**Disusun Oleh:**

1. Nama Lengkap - NIM
2. Nama Lengkap - NIM  
3. Nama Lengkap - NIM
4. Nama Lengkap - NIM

**PROGRAM STUDI SISTEM INFORMASI**  
**FAKULTAS TEKNOLOGI INFORMASI**  
**UNIVERSITAS NUSA MANDIRI**  
**JAKARTA**  
**2025**

---

# KATA PENGANTAR

Puji syukur kepada Tuhan Yang Maha Esa atas segala rahmat dan karunia-Nya sehingga penyusun dapat menyelesaikan laporan tugas akhir yang berjudul "Perancangan Dashboard Business Intelligence Interaktif untuk Mendukung Keputusan Bisnis pada SATRIAMART" dengan baik.

Laporan ini disusun untuk memenuhi tugas akhir mata kuliah Business Intelligence II (Kode 493) Program Studi Sistem Informasi, Fakultas Teknologi Informasi, Universitas Nusa Mandiri. Tujuan dari penyusunan laporan ini adalah untuk mengaplikasikan konsep Business Intelligence dalam merancang dashboard interaktif yang dapat memberikan wawasan data untuk mendukung pengambilan keputusan bisnis pada perusahaan skala kecil.

Penyusun menyadari bahwa penyelesaian laporan ini tidak lepas dari bantuan berbagai pihak. Oleh karena itu, penyusun mengucapkan terima kasih kepada:

1. Bapak Ridan Nurfalah, M.Kom, selaku dosen pengampu mata kuliah Business Intelligence II yang telah memberikan bimbingan dan arahan selama proses pembelajaran.
2. Pihak SATRIAMART yang telah memberikan izin dan kesempatan untuk menjadikan perusahaannya sebagai objek penelitian.
3. Rekan-rekan kelompok yang telah bekerja sama dengan baik dalam menyelesaikan tugas ini.
4. Semua pihak yang tidak dapat disebutkan satu per satu yang telah membantu dalam penyelesaian laporan ini.

Penyusun menyadari bahwa laporan ini masih jauh dari sempurna. Oleh karena itu, penyusun mengharapkan kritik dan saran yang membangun demi perbaikan di masa mendatang. Semoga laporan ini dapat bermanfaat bagi pengembangan ilmu Business Intelligence khususnya dalam penerapannya pada Usaha Mikro, Kecil, dan Menengah (UMKM) di Indonesia.

Jakarta, Oktober 2025

Penyusun

---

# ABSTRAK

*Business Intelligence* (BI) merupakan pendekatan sistematis untuk mengumpulkan, menganalisis, dan menyajikan informasi bisnis guna mendukung pengambilan keputusan yang lebih baik. Penelitian ini bertujuan untuk merancang dan mengimplementasikan dashboard Business Intelligence interaktif menggunakan Looker Studio untuk SATRIAMART, sebuah perusahaan skala kecil yang bergerak di bidang dekorasi dan aksesoris akrilik. Dashboard dirancang untuk memberikan visualisasi data penjualan, produk, pelanggan, dan keuangan secara real-time dan interaktif.

Metodologi yang digunakan meliputi analisis kebutuhan pengguna, identifikasi Key Performance Indicators (KPI), proses Extract-Transform-Load (ETL) data, perancangan layout dashboard, implementasi menggunakan Looker Studio, serta pengujian dan evaluasi. Data yang digunakan mencakup data transaksi penjualan, data produk, data pelanggan, riwayat stok, biaya operasional, dan kampanye pemasaran selama periode 12 bulan (November 2024 - Oktober 2025).

Hasil penelitian menunjukkan bahwa dashboard Business Intelligence yang dikembangkan mampu menyajikan informasi bisnis secara komprehensif melalui berbagai visualisasi seperti bar chart, line chart, pie chart, table, dan scorecard. Dashboard terdiri dari tujuh halaman utama yang mencakup Executive Summary, Sales Analysis, Product Performance, Customer Analysis, Operational Metrics, Financial Analysis, dan Marketing Performance. Wawasan yang dihasilkan mencakup identifikasi produk terlaris, pola penjualan musiman, segmentasi pelanggan, analisis profitabilitas per kategori produk, dan evaluasi efektivitas saluran penjualan.

Implementasi dashboard Business Intelligence ini memberikan manfaat praktis bagi SATRIAMART dalam bentuk peningkatan efisiensi analisis data, pengambilan keputusan yang lebih cepat dan akurat, identifikasi peluang bisnis baru, serta optimasi strategi pemasaran dan operasional. Penelitian ini membuktikan bahwa teknologi Business Intelligence dapat diterapkan secara efektif pada perusahaan skala kecil dengan biaya yang relatif terjangkau menggunakan platform cloud-based seperti Looker Studio.

**Kata kunci**: Business Intelligence, Dashboard Interaktif, Looker Studio, Visualisasi Data, Indikator Kinerja Utama, UMKM, Analisis Data, SATRIAMART.

---

# DAFTAR ISI

HALAMAN JUDUL
KATA PENGANTAR
ABSTRAK
DAFTAR ISI
DAFTAR GAMBAR
DAFTAR TABEL
DAFTAR LAMPIRAN

**BAB I PENDAHULUAN**
1.1 Latar Belakang Masalah
1.2 Rumusan Masalah
1.3 Tujuan
1.4 Manfaat
1.5 Ruang Lingkup

**BAB II LANDASAN TEORI**
2.1 Landasan Teori
    2.1.1 Business Intelligence
    2.1.2 Dashboard dan Key Performance Indicator
    2.1.3 Proses ETL (Extract, Transform, Load)
    2.1.4 Looker Studio sebagai Perangkat Business Intelligence
2.2 Data dan Sumber Data
    2.2.1 Jenis Data
    2.2.2 Sumber Data
    2.2.3 Proses Pembersihan Data
    2.2.4 Transformasi Data
2.3 Metode Perancangan
    2.3.1 Analisis Kebutuhan Pengguna
    2.3.2 Identifikasi Key Performance Indicators
    2.3.3 Persiapan Data (ETL)
    2.3.4 Perancangan Layout Dashboard
    2.3.5 Implementasi di Looker Studio
    2.3.6 Pengujian dan Evaluasi

**BAB III PEMBAHASAN**
3.1 Proses Analisa Data
    3.1.1 Analisis Data Transaksi Penjualan
    3.1.2 Identifikasi Pola dan Tren
    3.1.3 Hubungan Antar Variabel
3.2 Visualisasi Data pada Proses Business Intelligence
    3.2.1 Tren Penjualan
    3.2.2 Performa Produk
    3.2.3 Analisis Pelanggan
    3.2.4 Analisis Wilayah
    3.2.5 Pemilihan Jenis Visualisasi
3.3 Hasil Perancangan Dashboard Interaktif
    3.3.1 Executive Summary
    3.3.2 Sales Analysis
    3.3.3 Product Performance
    3.3.4 Customer Analysis
    3.3.5 Operational Metrics
    3.3.6 Financial Analysis
    3.3.7 Marketing Performance
3.4 Analisis dan Interpretasi
    3.4.1 Interpretasi Hasil Visualisasi
    3.4.2 Implikasi terhadap Strategi Bisnis
    3.4.3 Potensi Peningkatan Performa

**BAB IV PENUTUP**
4.1 Kesimpulan
4.2 Saran

**DAFTAR PUSTAKA**

**LAMPIRAN**

---

# BAB I  
# PENDAHULUAN

## 1.1 Latar Belakang Masalah

Dalam era digital saat ini, data telah menjadi aset penting bagi setiap organisasi bisnis, termasuk Usaha Mikro, Kecil, dan Menengah (UMKM). Ketersediaan data yang melimpah dari berbagai sumber seperti transaksi penjualan, interaksi pelanggan, dan operasional bisnis memberikan peluang besar bagi perusahaan untuk mengoptimalkan kinerja bisnis mereka. Namun, data mentah yang belum diolah tidak akan memberikan nilai tambah tanpa adanya proses analisis yang tepat. Di sinilah peran *Business Intelligence* (BI) menjadi sangat penting.

Business Intelligence merupakan seperangkat teknologi, aplikasi, dan praktik untuk pengumpulan, integrasi, analisis, dan presentasi informasi bisnis (Turban et al., 2021). Tujuan utama BI adalah untuk mendukung pengambilan keputusan bisnis yang lebih baik melalui penyediaan informasi yang akurat, relevan, dan tepat waktu. Dengan implementasi BI yang tepat, perusahaan dapat mengidentifikasi peluang bisnis baru, mendeteksi masalah operasional sejak dini, memahami perilaku pelanggan, dan mengoptimalkan strategi pemasaran.

SATRIAMART merupakan perusahaan skala kecil yang bergerak di bidang dekorasi dan aksesoris akrilik dengan produk unggulan berupa nomor rumah akrilik, papan petunjuk (*signage*), papan nama, dan berbagai aksesoris dekorasi khusus. Berlokasi di Depok, Jawa Barat, SATRIAMART melayani pelanggan dari wilayah Jabodetabek dan sekitarnya melalui berbagai saluran penjualan seperti Instagram, WhatsApp, platform pasar daring (*marketplace*), dan penjualan langsung. Seperti halnya UMKM pada umumnya, SATRIAMART menghadapi tantangan dalam mengelola dan menganalisis data bisnis yang terus bertambah setiap harinya.

Saat ini, SATRIAMART belum memiliki sistem informasi terintegrasi untuk melakukan analisis data secara komprehensif. Proses pengambilan keputusan masih dilakukan secara manual berdasarkan intuisi dan pengalaman, tanpa dukungan analisis data yang sistematis. Kondisi ini menyebabkan beberapa permasalahan seperti kesulitan dalam mengidentifikasi produk yang paling laris, ketidakpastian dalam merencanakan stok produk, minimnya pemahaman terhadap karakteristik dan preferensi pelanggan, serta kurangnya evaluasi terhadap efektivitas saluran penjualan dan kampanye pemasaran.

Dashboard Business Intelligence interaktif dapat menjadi solusi untuk mengatasi permasalahan tersebut. Dashboard merupakan alat visualisasi data yang menyajikan informasi penting dalam bentuk grafik, diagram, dan indikator kinerja yang mudah dipahami (Howson, 2021). Dengan dashboard, manajemen dapat memantau kinerja bisnis secara real-time, mengidentifikasi trend, dan membuat keputusan berdasarkan data yang akurat. Dashboard yang interaktif juga memungkinkan pengguna untuk melakukan eksplorasi data lebih dalam melalui fitur filter, drill-down, dan cross-filtering.

Looker Studio (sebelumnya dikenal sebagai Google Data Studio) merupakan platform Business Intelligence berbasis cloud yang disediakan oleh Google secara gratis. Platform ini memungkinkan pengguna untuk membuat dashboard interaktif dengan mudah tanpa memerlukan keahlian pemrograman yang mendalam. Looker Studio mendukung integrasi dengan berbagai sumber data termasuk Google Sheets, Google Analytics, database SQL, dan layanan cloud lainnya. Kemudahan penggunaan, biaya yang terjangkau (gratis), dan fitur kolaborasi yang baik menjadikan Looker Studio pilihan yang tepat untuk implementasi BI pada UMKM seperti SATRIAMART.

Berdasarkan latar belakang tersebut, penelitian ini bertujuan untuk merancang dan mengimplementasikan dashboard Business Intelligence interaktif menggunakan Looker Studio untuk SATRIAMART. Dashboard yang dikembangkan diharapkan dapat memberikan wawasan yang bernilai bagi manajemen dalam mengambil keputusan strategis terkait pengembangan produk, strategi pemasaran, pengelolaan pelanggan, dan optimasi operasional bisnis. Penelitian ini juga diharapkan dapat menjadi referensi bagi UMKM lain dalam mengadopsi teknologi Business Intelligence untuk meningkatkan daya saing bisnis mereka.

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian ini adalah sebagai berikut:

1. Bagaimana merancang dashboard Business Intelligence interaktif yang sesuai dengan kebutuhan bisnis SATRIAMART?

2. Visualisasi data apa saja yang efektif untuk menyajikan informasi penjualan, produk, pelanggan, dan keuangan SATRIAMART?

3. Wawasan bisnis apa yang dapat dihasilkan dari analisis data SATRIAMART menggunakan dashboard Business Intelligence?

4. Bagaimana implementasi dashboard Business Intelligence dapat mendukung pengambilan keputusan bisnis pada SATRIAMART?

5. Apa rekomendasi strategis yang dapat diberikan berdasarkan hasil analisis data untuk meningkatkan performa bisnis SATRIAMART?

## 1.3 Tujuan

Tujuan dari penelitian ini adalah:

1. Merancang dan mengimplementasikan dashboard Business Intelligence interaktif untuk SATRIAMART menggunakan Looker Studio.

2. Mengidentifikasi Key Performance Indicators (KPI) yang relevan dengan bisnis SATRIAMART untuk diintegrasikan dalam dashboard.

3. Menganalisis data transaksi penjualan, produk, pelanggan, dan keuangan untuk menghasilkan wawasan bisnis yang bernilai.

4. Menyajikan informasi bisnis melalui visualisasi data yang efektif dan mudah dipahami oleh pengguna.

5. Memberikan rekomendasi strategis berdasarkan hasil analisis data untuk optimasi bisnis SATRIAMART.

6. Mendemonstrasikan bahwa teknologi Business Intelligence dapat diterapkan secara efektif pada perusahaan skala kecil dengan biaya terjangkau.

## 1.4 Manfaat

### 1.4.1 Manfaat bagi SATRIAMART

1. **Peningkatan Efisiensi Analisis Data**: SATRIAMART dapat menganalisis data bisnis dengan lebih cepat dan efisien melalui dashboard yang terintegrasi dibandingkan dengan metode manual.

2. **Pengambilan Keputusan Berbasis Data**: Manajemen dapat membuat keputusan bisnis yang lebih akurat dan terukur berdasarkan insight dari data, bukan hanya berdasarkan intuisi.

3. **Identifikasi Peluang Bisnis**: Dashboard membantu mengidentifikasi produk terlaris, segmen pelanggan potensial, dan saluran penjualan paling efektif untuk optimasi strategi bisnis.

4. **Monitoring Kinerja Real-Time**: Manajemen dapat memantau kinerja bisnis secara real-time dan merespons perubahan pasar dengan lebih cepat.

5. **Optimasi Inventory**: Dengan analisis data penjualan dan stok, SATRIAMART dapat mengoptimalkan manajemen inventory dan mengurangi risiko overstock atau stockout.

6. **Evaluasi Efektivitas Marketing**: Dashboard marketing performance memungkinkan evaluasi Return on Investment (ROI) kampanye marketing untuk alokasi budget yang lebih efektif.

7. **Peningkatan Customer Satisfaction**: Dengan pemahaman yang lebih baik tentang karakteristik dan preferensi pelanggan, SATRIAMART dapat memberikan layanan yang lebih personal dan meningkatkan customer satisfaction.

### 1.4.2 Manfaat bagi Penyusun

1. **Penerapan Ilmu Business Intelligence**: Penyusun dapat mengaplikasikan konsep dan teori Business Intelligence yang telah dipelajari dalam kasus nyata.

2. **Peningkatan Kompetensi Teknis**: Penyusun memperoleh pengalaman praktis dalam menggunakan perangkat Business Intelligence seperti Looker Studio, Google Sheets, dan teknik analisis data.

3. **Pengembangan Soft Skills**: Penyusun mengembangkan kemampuan problem solving, analytical thinking, dan communication skills melalui proses penelitian dan presentasi.

4. **Portfolio Project**: Hasil penelitian ini dapat menjadi portfolio yang bernilai untuk keperluan akademis maupun profesional.

5. **Pemahaman Bisnis UMKM**: Penyusun memperoleh wawasan tentang tantangan dan peluang bisnis pada sektor UMKM khususnya di bidang dekorasi dan aksesoris.

6. **Kontribusi Sosial**: Penyusun berkontribusi dalam membantu UMKM mengadopsi teknologi digital untuk peningkatan daya saing bisnis.

## 1.5 Ruang Lingkup

Untuk menjaga fokus penelitian dan memastikan hasil yang optimal, ruang lingkup penelitian ini dibatasi sebagai berikut:

### 1.5.1 Batasan Data

1. **Periode Data**: Data yang dianalisis mencakup periode 12 bulan dari November 2024 hingga Oktober 2025.

2. **Jenis Data**: Data yang digunakan meliputi:
   - Data master produk (50 produk)
   - Data master pelanggan (180 pelanggan)
   - Data transaksi penjualan (320 transaksi)
   - Data riwayat stok
   - Data biaya operasional
   - Data kampanye pemasaran

3. **Sumber Data**: Data bersumber dari sistem pencatatan internal SATRIAMART yang telah diolah dan disimulasikan untuk keperluan pembelajaran.

4. **Cakupan Geografis**: Analisis fokus pada pelanggan di wilayah Jabodetabek dan sekitarnya sebagai pasar utama SATRIAMART.

### 1.5.2 Batasan Fitur Dashboard

1. **Platform**: Dashboard dikembangkan menggunakan Looker Studio (Google Data Studio) sebagai platform Business Intelligence.

2. **Jumlah Halaman**: Dashboard terdiri dari 7 halaman utama yang mencakup Executive Summary, Sales Analysis, Product Performance, Customer Analysis, Operational Metrics, Financial Analysis, dan Marketing Performance.

3. **Interaktivitas**: Fitur interaktif mencakup date filter, category filter, channel filter, dan cross-filtering antar visualisasi.

4. **Visualisasi**: Jenis visualisasi yang digunakan meliputi scorecard, bar chart, line chart, pie chart, combo chart, table, dan geo map.

5. **Real-Time Update**: Dashboard tidak terintegrasi dengan sistem real-time, pembaruan data dilakukan secara manual melalui upload ke Google Sheets.

### 1.5.3 Batasan Analisis

1. **Fokus Analisis**: Analisis difokuskan pada aspek sales, product, customer, operational, financial, dan marketing.

2. **Metode Analisis**: Analisis menggunakan metode descriptive dan exploratory, tidak mencakup predictive analytics atau machine learning.

3. **Customer Segmentation**: Segmentasi pelanggan dilakukan berdasarkan RFM (Recency, Frequency, Monetary) dan karakteristik demografis dasar.

4. **Profitability Analysis**: Analisis profitabilitas dihitung berdasarkan selisih harga jual dan cost, belum mencakup alokasi overhead cost secara detail.

### 1.5.4 Batasan Implementasi

1. **User**: Dashboard dirancang untuk digunakan oleh manajemen dan tim operasional SATRIAMART, tidak mencakup akses untuk customer eksternal.

2. **Data Security**: Implementasi menggunakan sharing link dengan restricted access, tidak mencakup sistem authentication dan authorization yang kompleks.

3. **Scalability**: Dashboard dirancang untuk volume data skala kecil hingga menengah, belum dioptimasi untuk volume data enterprise-level.

4. **System Integration**: Dashboard tidak terintegrasi dengan sistem Enterprise Resource Planning (ERP), Customer Relationship Management (CRM), atau sistem enterprise lainnya, data dikelola secara terpisah di Google Sheets.

---

*[Lanjutan BAB II, BAB III, dan BAB IV akan dibuat dalam file terpisah karena keterbatasan panjang]*

---

# Catatan untuk BAB II - IV

Silakan lanjutkan pembuatan konten untuk:

## BAB II - LANDASAN TEORI
- Teori Business Intelligence (dari Turban, Davenport, Howson)
- Teori Dashboard dan KPI
- Proses ETL
- Looker Studio
- Data dan Sumber Data
- Metode Perancangan

## BAB III - PEMBAHASAN  
- Proses Analisa Data SATRIAMART
- Visualisasi Data dengan contoh screenshot
- Hasil Perancangan Dashboard (7 pages)
- Analisis dan Interpretasi Insight

## BAB IV - PENUTUP
- Kesimpulan
- Saran untuk pengembangan

---

**Format Dokumen:**
- Margin: Kiri 4cm, Kanan/Atas/Bawah 2,5cm
- Font: Times New Roman 12pt
- Spasi: 1,5
- Numbering: Auto-generate di MS Word
- Referensi: Menggunakan Mendeley (APA Style)
