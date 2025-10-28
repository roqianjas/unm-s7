# BAB II  
# LANDASAN TEORI

## 2.1 Landasan Teori

### 2.1.1 Business Intelligence

*Business Intelligence* (BI) merupakan istilah umum yang mencakup aplikasi, infrastruktur, perangkat, dan praktik terbaik yang memungkinkan akses dan analisis informasi untuk meningkatkan dan mengoptimalkan keputusan dan kinerja organisasi (Turban et al., 2021). Menurut Davenport (2020), Business Intelligence adalah seperangkat teknologi dan proses yang menggunakan data untuk memahami dan menganalisis performa bisnis guna mendorong perencanaan strategis yang lebih baik.

Antonius (2023) mendefinisikan Business Intelligence sebagai proses pengumpulan data mentah, pengolahan data menjadi informasi, dan transformasi informasi menjadi pengetahuan yang dapat digunakan untuk pengambilan keputusan bisnis. Dalam konteks UMKM, BI berfungsi sebagai alat untuk mengubah data operasional sehari-hari menjadi wawasan yang dapat ditindaklanjuti untuk meningkatkan daya saing bisnis.

Komponen utama dalam sistem Business Intelligence menurut Turban et al. (2021) meliputi:

1. **Data Warehouse**: Repositori terpusat yang menyimpan data historis dari berbagai sumber untuk keperluan analisis dan pelaporan.

2. **Business Analytics**: Kumpulan teknik analisis yang digunakan untuk mengeksplorasi data, mengidentifikasi pola, dan membuat prediksi.

3. **Data Visualization**: Presentasi data dalam bentuk visual seperti grafik, diagram, dan dashboard untuk memudahkan pemahaman dan interpretasi.

4. **Performance Management**: Sistem untuk memantau dan mengelola kinerja organisasi berdasarkan Key Performance Indicator (KPI).

5. **User Interface**: Antarmuka yang memungkinkan pengguna berinteraksi dengan sistem BI untuk mengakses informasi dan melakukan analisis.

Menurut Howson (2021), implementasi Business Intelligence yang sukses harus memenuhi beberapa prinsip kunci:

- **Relevansi**: Informasi yang disajikan harus relevan dengan kebutuhan bisnis dan mendukung pengambilan keputusan strategis.

- **Akurasi**: Data harus akurat, konsisten, dan dapat dipercaya sebagai dasar pengambilan keputusan.

- **Ketepatan Waktu**: Informasi harus tersedia tepat waktu ketika dibutuhkan untuk pengambilan keputusan.

- **Aksesibilitas**: Informasi harus mudah diakses oleh pemangku kepentingan yang berwenang melalui antarmuka yang mudah digunakan.

- **Dapat Ditindaklanjuti**: Wawasan yang dihasilkan harus dapat ditindaklanjuti dan memberikan nilai tambah bagi organisasi.

Dalam konteks perusahaan skala kecil seperti SATRIAMART, implementasi BI dapat membantu dalam beberapa area kritis:

1. **Analisis Penjualan**: Memahami kecenderungan penjualan, produk terlaris, dan performa saluran penjualan.

2. **Manajemen Persediaan**: Optimasi stok produk berdasarkan peramalan permintaan dan analisis perputaran barang.

3. **Manajemen Hubungan Pelanggan**: Memahami karakteristik pelanggan, pola pembelian, dan segmentasi untuk pemasaran yang tertarget.

4. **Analisis Profitabilitas**: Evaluasi margin keuntungan per produk, per kategori, dan per saluran untuk optimasi strategi penetapan harga.

5. **Efektivitas Pemasaran**: Mengukur ROI kampanye pemasaran dan mengidentifikasi saluran pemasaran yang paling efektif.

### 2.1.2 Dashboard dan Key Performance Indicator

*Dashboard* adalah alat visualisasi yang menyajikan informasi penting dan Key Performance Indicators (KPI) dalam satu layar untuk memudahkan pemantauan dan analisis kinerja bisnis (Howson, 2021). Dashboard yang efektif harus menyajikan informasi yang paling relevan dengan cara yang mudah dipahami, memungkinkan pengguna untuk mengidentifikasi masalah dan peluang dengan cepat.

Menurut Few (2013) dalam Turban et al. (2021), dashboard yang baik memiliki karakteristik sebagai berikut:

1. **Sederhana**: Menampilkan informasi tanpa kompleksitas yang tidak perlu, fokus pada data yang paling penting.

2. **Komunikatif**: Menyampaikan informasi dengan jelas dan mudah dipahami oleh target audiens.

3. **Relevan**: Menampilkan informasi yang relevan dengan kebutuhan bisnis dan konteks pengambilan keputusan.

4. **Tepat Waktu**: Menyajikan informasi yang terkini dan real-time atau mendekati real-time.

5. **Dapat Ditindaklanjuti**: Memberikan wawasan yang dapat ditindaklanjuti untuk perbaikan kinerja bisnis.

Key Performance Indicator (KPI) adalah metrik kuantitatif yang mencerminkan faktor kesuksesan kritis suatu organisasi (Antonius, 2023). KPI digunakan untuk mengukur pencapaian tujuan strategis dan memberikan indikasi tentang performa bisnis. Karakteristik KPI yang baik mengikuti prinsip SMART:

- **Specific**: Jelas dan spesifik dalam mengukur aspek tertentu dari bisnis.
- **Measurable**: Dapat diukur secara kuantitatif dengan data yang tersedia.
- **Achievable**: Realistis dan dapat dicapai dengan sumber daya yang ada.
- **Relevant**: Relevan dengan tujuan strategis organisasi.
- **Time-bound**: Memiliki periode waktu pengukuran yang jelas.

Dalam konteks SATRIAMART, KPI yang relevan mencakup:

**KPI Penjualan**:
- Total Revenue
- Growth Rate
- Average Order Value (AOV)
- Number of Transactions

**KPI Produk**:
- Best Selling Products
- Profit Margin per Product
- Inventory Turnover Rate
- Stock-out Frequency

**KPI Pelanggan**:
- Customer Acquisition Cost (CAC)
- Customer Lifetime Value (CLV)
- Repeat Purchase Rate
- Customer Satisfaction Score

**KPI Operasional**:
- Order Fulfillment Time
- Order Completion Rate
- Cancellation Rate

**KPI Finansial**:
- Gross Profit
- Net Profit
- Profit Margin
- Return on Investment (ROI)

**KPI Pemasaran**:
- Marketing ROI
- Conversion Rate
- Cost per Acquisition

### 2.1.3 Proses ETL (Extract, Transform, Load)

ETL merupakan proses fundamental dalam Business Intelligence yang terdiri dari tiga tahap: Extract (ekstraksi), Transform (transformasi), dan Load (pemuatan) data dari sumber ke data warehouse atau sistem analitik (Turban et al., 2021).

**1. Extract (Ekstraksi)**

Proses ekstraksi melibatkan pengambilan data dari berbagai sumber seperti database transaksional, file spreadsheet, API, atau sistem eksternal lainnya. Menurut Valentinus (2017), tahap ekstraksi harus memperhatikan:

- Identifikasi sumber data yang relevan
- Validasi ketersediaan dan aksesibilitas data
- Penentuan frekuensi ekstraksi (batch atau real-time)
- Penanganan data yang berubah atau bertambah

Dalam konteks SATRIAMART, sumber data meliputi:
- Data transaksi penjualan dari sistem pencatatan manual
- Data produk dari katalog internal
- Data pelanggan dari database kontak
- Data biaya dari pencatatan keuangan
- Data pemasaran dari platform media sosial

**2. Transform (Transformasi)**

Transformasi adalah proses pembersihan, validasi, dan pengolahan data mentah menjadi format yang sesuai untuk analisis. Proses transformasi mencakup:

- **Data Cleaning**: Menghapus duplikasi, menangani nilai yang hilang, memperbaiki format data yang tidak konsisten.

- **Data Validation**: Memastikan data memenuhi kriteria kualitas dan akurasi yang ditetapkan.

- **Data Integration**: Menggabungkan data dari berbagai sumber dengan konsistensi skema dan format.

- **Data Aggregation**: Melakukan agregasi data untuk keperluan analisis ringkasan (misalnya total penjualan per bulan).

- **Data Enrichment**: Menambahkan informasi tambahan atau field kalkulasi untuk memperkaya dataset.

Menurut Antonius (2023), kualitas data sangat menentukan kualitas insight yang dihasilkan. Oleh karena itu, proses transformasi harus dilakukan dengan cermat untuk memastikan data yang akurat dan konsisten.

**3. Load (Pemuatan)**

Tahap pemuatan melibatkan pemuatan data yang sudah ditransformasi ke dalam data warehouse atau sistem analitik. Metode pemuatan yang umum digunakan:

- **Full Load**: Memuat seluruh dataset dari awal, biasanya untuk pemuatan awal.

- **Incremental Load**: Memuat hanya data yang baru atau berubah sejak pemuatan terakhir, lebih efisien untuk data yang besar.

- **Real-time Load**: Memuat data secara real-time atau mendekati real-time untuk kebutuhan monitoring real-time.

Dalam implementasi dashboard SATRIAMART menggunakan Looker Studio, proses ETL dilakukan dengan:

1. **Extract**: Data diekstrak dari sistem pencatatan internal SATRIAMART dan dikumpulkan dalam format CSV.

2. **Transform**: Data dibersihkan dan ditransformasi menggunakan spreadsheet dan Python untuk memastikan konsistensi format, menangani nilai yang hilang, dan membuat calculated fields.

3. **Load**: Data hasil transformasi diupload ke Google Sheets sebagai data source untuk Looker Studio.

### 2.1.4 Looker Studio sebagai Tools Business Intelligence

Looker Studio (sebelumnya Google Data Studio) adalah platform Business Intelligence berbasis cloud yang disediakan oleh Google untuk membuat laporan dan dashboard interaktif (Google, 2023). Looker Studio memungkinkan pengguna untuk menghubungkan berbagai data source, melakukan transformasi data, membuat visualisasi, dan sharing dashboard dengan stakeholder.

**Keunggulan Looker Studio:**

1. **Gratis**: Platform ini dapat digunakan secara gratis tanpa biaya lisensi, sangat cocok untuk UMKM dengan anggaran terbatas.

2. **Mudah Digunakan**: Antarmuka drag-and-drop yang intuitif memudahkan pembuatan dashboard tanpa memerlukan pemrograman.

3. **Integrasi Data**: Mendukung integrasi dengan lebih dari 100 konektor data termasuk Google Sheets, Google Analytics, BigQuery, MySQL, PostgreSQL, dan layanan cloud lainnya.

4. **Kolaborasi**: Memungkinkan kolaborasi real-time dan berbagi dashboard dengan kontrol akses yang dapat diatur.

5. **Interaktif**: Dashboard yang dibuat memiliki fitur interaktif seperti filter, pemilih rentang tanggal, dan drill-down.

6. **Responsif**: Dashboard secara otomatis responsif dan dapat diakses dari berbagai perangkat.

7. **Dapat Disesuaikan**: Mendukung penyesuaian branding, warna, font, dan layout sesuai kebutuhan organisasi.

**Komponen Utama Looker Studio:**

1. **Data Source**: Koneksi ke sumber data yang akan digunakan dalam dashboard.

2. **Report/Dashboard**: Kanvas untuk membuat dan mengatur visualisasi data.

3. **Charts**: Berbagai jenis visualisasi seperti bar chart, line chart, pie chart, table, scorecard, geo map, dan lain-lain.

4. **Controls**: Elemen interaktif seperti pemilih rentang tanggal, filter dropdown, filter checkbox untuk eksplorasi data.

5. **Parameters**: Variabel yang dapat digunakan untuk membuat calculated fields atau logika kondisional.

6. **Calculated Fields**: Field yang dibuat dari kombinasi atau transformasi field yang sudah ada.

**Jenis Visualisasi dalam Looker Studio:**

1. **Scorecard**: Menampilkan nilai metrik tunggal, cocok untuk KPI utama.

2. **Time Series Chart**: Grafik garis untuk menampilkan tren data sepanjang waktu.

3. **Bar Chart**: Menampilkan perbandingan nilai antar kategori.

4. **Pie/Donut Chart**: Menampilkan proporsi atau komposisi dari keseluruhan.

5. **Table**: Menampilkan data dalam format tabel dengan opsi pengurutan dan paginasi.

6. **Geo Map**: Visualisasi data berdasarkan lokasi geografis.

7. **Combo Chart**: Kombinasi grafik garis dan bar chart untuk membandingkan metrik dengan skala berbeda.

8. **Bullet Chart**: Menampilkan nilai aktual versus target.

9. **Scatter Plot**: Menampilkan hubungan antara dua variabel numerik.

Pemilihan Looker Studio untuk implementasi dashboard SATRIAMART didasarkan pada beberapa pertimbangan:

- **Tanpa Biaya**: Tidak ada biaya lisensi sehingga berkelanjutan untuk UMKM.
- **Berbasis Cloud**: Tidak memerlukan infrastruktur server sendiri.
- **Integrasi Mudah**: Integrasi mudah dengan Google Sheets sebagai sumber data.
- **Kolaboratif**: Memudahkan berbagi dan kolaborasi dengan tim.
- **Mudah Dipelajari**: Relatif mudah dipelajari dibandingkan tools enterprise seperti Tableau atau Power BI.

## 2.2 Data dan Sumber Data

### 2.2.1 Jenis Data

Data yang digunakan dalam penelitian ini mencakup berbagai aspek bisnis SATRIAMART selama periode 12 bulan (November 2024 - Oktober 2025). Jenis data yang dikumpulkan meliputi:

**1. Data Master Produk**

Data produk mencakup informasi lengkap tentang produk yang dijual oleh SATRIAMART, termasuk ID produk, nama produk, kategori (Nomor Rumah, Signage, Papan Nama, Aksesoris Dekorasi), sub-kategori, ukuran, warna, harga jual, harga modal, stok tersedia, material, finishing, berat, deskripsi, status, dan tanggal dibuat/update.

Total produk yang dianalisis sebanyak 50 produk dengan distribusi:
- Nomor Rumah Akrilik: 15 produk (30%)
- Signage Akrilik: 10 produk (20%)
- Papan Nama Akrilik: 10 produk (20%)
- Aksesoris Dekorasi: 15 produk (30%)

**2. Data Transaksi Penjualan**

Data transaksi penjualan mencatat setiap transaksi yang terjadi, meliputi ID transaksi, tanggal dan waktu transaksi, ID pelanggan, ID produk, jumlah item, harga satuan, subtotal, diskon, biaya khusus, biaya ongkir, total pembayaran, metode pembayaran, status pembayaran, status pesanan, saluran penjualan, catatan pesanan, waktu pengerjaan, rating pelanggan, dan tanggal selesai.

Total transaksi yang dianalisis sebanyak 320 transaksi selama 12 bulan dengan total pendapatan Rp 111.976.550.

**3. Data Master Pelanggan**

Data pelanggan mencakup informasi demografis dan perilaku dari pelanggan SATRIAMART, meliputi ID pelanggan, nama lengkap, nomor telepon, email, alamat lengkap, kota, provinsi, kode pos, jenis pelanggan (Individu/Bisnis/Reseller), segmen (Retail/UMKM/Korporat), tanggal registrasi, total transaksi, total nilai pembelian, status, dan sumber awal pelanggan.

Total pelanggan yang tercatat sebanyak 180 pelanggan dengan distribusi:
- Individu/Retail: 108 pelanggan (60%)
- Bisnis/UMKM: 54 pelanggan (30%)
- Reseller/Korporat: 18 pelanggan (10%)

**4. Data Riwayat Stok**

Data riwayat stok mencatat pergerakan stok produk setiap bulan, meliputi ID stok, tanggal, ID produk, stok awal, stok masuk (pembelian/produksi), stok keluar (penjualan), stok akhir, jenis transaksi, dan keterangan.

**5. Data Biaya Operasional**

Data biaya operasional mencatat pengeluaran bisnis, meliputi ID biaya, tanggal, kategori biaya (Bahan Baku, Pemasaran, Operasional, Transportasi, Utilitas), sub-kategori, nominal, keterangan, dan metode pembayaran.

**6. Data Kampanye Pemasaran**

Data kampanye pemasaran mencatat aktivitas pemasaran, meliputi ID kampanye, nama kampanye, platform (Instagram, Facebook, Google Ads, TikTok), tanggal mulai, tanggal selesai, anggaran, jangkauan, keterlibatan, konversi, pendapatan yang dihasilkan, dan ROI.

### 2.2.2 Sumber Data

Sumber data dalam penelitian ini berasal dari sistem pencatatan internal SATRIAMART yang telah disimulasikan dan diolah untuk keperluan pembelajaran dan analisis Business Intelligence. Data bersifat representatif dan mengikuti pola bisnis yang realistis untuk UMKM di bidang dekorasi dan aksesoris.

Sumber data spesifik meliputi:

1. **Sistem Pencatatan Penjualan**: Data transaksi penjualan dicatat dari nota penjualan, faktur, dan riwayat pesanan dari berbagai saluran (WhatsApp, Instagram, Marketplace, Penjualan Langsung).

2. **Database Produk**: Informasi produk dikelola dalam katalog digital yang mencakup spesifikasi lengkap setiap produk.

3. **Database Pelanggan**: Data pelanggan dikumpulkan dari formulir pemesanan, kontak WhatsApp/Instagram, dan riwayat transaksi.

4. **Pencatatan Keuangan**: Data biaya operasional berasal dari pencatatan pengeluaran bulanan yang dikelola oleh bagian keuangan.

5. **Laporan Pemasaran**: Data kampanye pemasaran diperoleh dari platform analitik media sosial (Instagram Insights, Facebook Ads Manager, Google Analytics).

Data yang telah dikumpulkan kemudian diolah dan disimpan dalam format CSV untuk memudahkan proses ETL dan integrasi dengan Looker Studio melalui Google Sheets.

### 2.2.3 Proses Pembersihan Data

Pembersihan data merupakan tahap kritis dalam memastikan kualitas data yang akan dianalisis. Proses pembersihan data yang dilakukan dalam penelitian ini meliputi:

**1. Penanganan Nilai Kosong**

- Identifikasi kolom yang memiliki nilai kosong
- Untuk kolom numerik, nilai kosong diganti dengan nilai 0 atau rata-rata tergantung konteks
- Untuk kolom kategorikal, nilai kosong diganti dengan kategori "Tidak Diketahui" atau "Lainnya"
- Untuk kolom yang kritis, baris dengan nilai kosong dihapus

**2. Penghapusan Duplikasi**

- Identifikasi dan hapus transaksi duplikat berdasarkan ID transaksi
- Validasi duplikasi pelanggan berdasarkan nomor telepon atau email
- Pastikan setiap data memiliki pengenal unik

**3. Konversi Tipe Data**

- Konversi kolom tanggal ke format standar (YYYY-MM-DD)
- Konversi kolom numerik (harga, jumlah) ke tipe angka
- Konversi kolom kategorikal ke tipe teks
- Validasi format email dan nomor telepon

**4. Deteksi Pencilan**

- Identifikasi nilai ekstrim pada kolom harga, jumlah, dan total pembayaran
- Validasi apakah pencilan merupakan kesalahan atau kasus bisnis yang valid
- Tangani pencilan dengan penghapusan atau transformasi sesuai konteks

**5. Standarisasi Format**

- Standarisasi format nama (huruf kapital di awal kata)
- Standarisasi format alamat dan kota
- Standarisasi kategori dan sub-kategori produk
- Standarisasi status pesanan dan status pembayaran

**6. Pemeriksaan Konsistensi**

- Validasi konsistensi antara subtotal dengan harga satuan × jumlah
- Validasi total pembayaran = subtotal - diskon + biaya tambahan + ongkir
- Validasi tanggal selesai >= tanggal transaksi
- Validasi stok akhir = stok awal + stok masuk - stok keluar

### 2.2.4 Transformasi Data

Setelah data dibersihkan, dilakukan transformasi untuk memperkaya dataset dan memudahkan analisis. Proses transformasi yang dilakukan meliputi:

**1. Calculated Fields**

Membuat kolom baru hasil perhitungan:
- Profit = Harga Jual - Harga Modal
- Profit Margin = (Profit / Harga Jual) × 100%
- Jumlah Diskon = Subtotal × Persentase Diskon / 100
- Pendapatan Bersih = Total Pembayaran - Harga Pokok Penjualan
- Nilai Rata-rata Pesanan = Total Pendapatan / Jumlah Transaksi

**2. Dimensi Tanggal**

Ekstraksi komponen tanggal untuk analisis temporal:
- Tahun, Bulan, Kuartal dari tanggal transaksi
- Hari dalam Minggu (Senin-Minggu)
- Minggu dalam Tahun
- Akhir Pekan (Ya/Tidak)
- Nama Bulan (Januari-Desember)

**3. Pengelompokan Kategori**

Membuat kategori baru untuk analisis segmentasi:
- Rentang Harga: Rendah (< 100K), Menengah (100-300K), Tinggi (> 300K)
- Segmen Nilai Pelanggan: Rendah, Menengah, Tinggi berdasarkan total pembelian
- Ukuran Pesanan: Kecil (1 item), Menengah (2-3 items), Besar (> 3 items)
- Wilayah Geografis: Depok, Jakarta, Tangerang-Bekasi, Lainnya

**4. Agregasi Data**

Membuat ringkasan data untuk dashboard:
- Total Pendapatan per Bulan
- Total Transaksi per Kategori Produk
- Rata-rata Rating per Produk
- Total Pelanggan per Kota
- Total Anggaran Kampanye per Platform

**5. Penggabungan Tabel**

Menggabungkan data dari beberapa tabel:
- Gabungkan Transaksi dengan Master Produk untuk mendapatkan kategori dan harga modal
- Gabungkan Transaksi dengan Master Pelanggan untuk mendapatkan informasi demografis
- Gabungkan Transaksi dengan Riwayat Stok untuk analisis perputaran persediaan

**6. Pengayaan Data**

Menambahkan informasi tambahan:
- Customer Lifetime Value (CLV) = Total Nilai Pembelian Pelanggan
- Recency = Jumlah hari sejak transaksi terakhir
- Frequency = Jumlah transaksi pelanggan
- Monetary = Total pengeluaran pelanggan
- Skor RFM untuk segmentasi pelanggan

## 2.3 Metode Perancangan

### 2.3.1 Analisis Kebutuhan Pengguna

Tahap awal dalam perancangan dashboard adalah memahami kebutuhan pengguna. Analisis kebutuhan dilakukan melalui diskusi dengan pemangku kepentingan SATRIAMART untuk mengidentifikasi:

**1. Profil Pengguna**

Identifikasi tiga kelompok pengguna utama:
- **Pemilik/Manajemen Puncak**: Membutuhkan gambaran tingkat tinggi, ringkasan KPI, dan wawasan strategis
- **Manajer Pemasaran**: Membutuhkan analisis kampanye, segmentasi pelanggan, dan kinerja saluran
- **Manajer Operasional**: Membutuhkan analisis persediaan, metrik penyelesaian, dan efisiensi operasional

**2. Kebutuhan Informasi**

Untuk setiap profil pengguna, diidentifikasi informasi yang dibutuhkan:
- Metrik apa yang paling penting untuk dipantau?
- Visualisasi apa yang paling efektif untuk menyajikan informasi?
- Seberapa detail tingkat informasi yang dibutuhkan?
- Seberapa sering informasi perlu diperbarui?

**3. Kebutuhan Dukungan Keputusan**

Identifikasi keputusan bisnis yang perlu didukung oleh dashboard:
- Produk mana yang harus diprioritaskan untuk produksi?
- Saluran pemasaran mana yang paling efektif?
- Segmen pelanggan mana yang paling menguntungkan?
- Kapan waktu terbaik untuk promosi?

**4. Batasan dan Keterbatasan**

Identifikasi batasan dalam implementasi:
- Anggaran: Menggunakan tools gratis (Looker Studio, Google Sheets)
- Keterampilan Teknis: Pengguna memiliki keterampilan komputer dasar, tidak familiar dengan tools tingkat lanjut
- Ketersediaan Data: Data tersedia dalam format spreadsheet
- Frekuensi Pembaruan: Pembaruan manual, tidak real-time

### 2.3.2 Identifikasi Key Performance Indicators

Berdasarkan analisis kebutuhan, diidentifikasi KPI yang relevan untuk setiap area bisnis:

**KPI Penjualan**:
- Total Revenue: Total pendapatan dari seluruh transaksi
- Number of Transactions: Jumlah transaksi yang terjadi
- Average Order Value (AOV): Rata-rata nilai per transaksi
- Growth Rate: Tingkat pertumbuhan pendapatan bulan ke bulan
- Sales by Channel: Pendapatan dari setiap saluran penjualan
- Sales by Product Category: Pendapatan dari setiap kategori produk

**KPI Produk**:
- Top 10 Best Selling Products: Produk dengan jumlah penjualan tertinggi
- Revenue per Product: Pendapatan yang dihasilkan setiap produk
- Profit Margin per Product: Margin keuntungan setiap produk
- Inventory Turnover Rate: Kecepatan perputaran persediaan
- Stock-out Frequency: Frekuensi kehabisan stok

**KPI Pelanggan**:
- Total Customers: Jumlah total pelanggan
- New Customers: Jumlah pelanggan baru per periode
- Repeat Customer Rate: Persentase pelanggan yang melakukan pembelian ulang
- Customer Lifetime Value (CLV): Nilai total pembelian pelanggan
- Customer Satisfaction Score: Rata-rata rating dari pelanggan

**KPI Operasional**:
- Order Fulfillment Time: Rata-rata waktu penyelesaian pesanan
- Order Completion Rate: Persentase pesanan yang selesai
- Cancellation Rate: Persentase pesanan yang dibatalkan
- On-Time Delivery Rate: Persentase pesanan yang selesai tepat waktu

**KPI Finansial**:
- Gross Revenue: Total pendapatan kotor
- Total Costs: Total biaya operasional
- Net Profit: Laba bersih
- Profit Margin: Persentase margin keuntungan
- Cost per Transaction: Biaya rata-rata per transaksi

**KPI Pemasaran**:
- Marketing ROI: Return on investment dari kampanye pemasaran
- Conversion Rate by Channel: Tingkat konversi setiap saluran
- Cost per Acquisition (CPA): Biaya untuk memperoleh satu pelanggan baru
- Campaign Reach: Jangkauan kampanye pemasaran
- Engagement Rate: Tingkat keterlibatan di media sosial

### 2.3.3 Persiapan Data (ETL)

Proses ETL untuk dashboard SATRIAMART dilakukan dengan langkah-langkah berikut:

**1. Extract (Ekstraksi)**
- Kumpulkan data mentah dari berbagai sumber (catatan penjualan, persediaan, keuangan)
- Ekspor data ke format CSV
- Validasi kelengkapan data

**2. Transform (Transformasi)**
- Pembersihan data: hapus duplikasi, tangani nilai kosong, perbaiki inkonsistensi format
- Transformasi data: buat calculated fields, ekstrak dimensi tanggal, kategorisasi
- Pengayaan data: tambahkan metrik turunan (profit, margin, skor RFM)
- Agregasi data: buat tabel ringkasan untuk optimasi kinerja

**3. Load (Pemuatan)**
- Unggah file CSV ke Google Sheets
- Buat sheet terpisah untuk setiap tabel (master_product, master_customer, sales_transactions, dll)
- Terapkan konvensi penamaan dan struktur yang tepat
- Validasi integritas data setelah pengunggahan

**4. Pengaturan Data Source di Looker Studio**
- Hubungkan Looker Studio ke Google Sheets
- Atur data sources untuk setiap sheet
- Konfigurasi tipe kolom (tanggal, angka, teks)
- Buat blended data sources untuk menggabungkan beberapa tabel

### 2.3.4 Perancangan Layout Dashboard

Layout dashboard dirancang mengikuti prinsip-prinsip hierarki visual dan praktik terbaik desain dashboard:

**1. Struktur Dashboard**

Dashboard terdiri dari 7 halaman:
- Halaman 1: Executive Summary / Ringkasan Keseluruhan
- Halaman 2: Analisis Penjualan
- Halaman 3: Kinerja Produk
- Halaman 4: Analisis Pelanggan
- Halaman 5: Metrik Operasional
- Halaman 6: Analisis Keuangan
- Halaman 7: Kinerja Pemasaran

**2. Hierarki Visual**

Setiap halaman mengikuti struktur:
- **Header**: Logo, judul dashboard, kontrol filter
- **Kartu KPI**: 4-6 scorecard menampilkan metrik kunci di bagian atas
- **Visualisasi Utama**: 2-3 grafik utama yang menjawab pertanyaan bisnis paling penting
- **Visualisasi Pendukung**: Grafik detail dan informasi pendukung
- **Footer**: Waktu pembaruan terakhir, informasi sumber data

**3. Skema Warna**

Pemilihan warna konsisten dengan identitas brand SATRIAMART:
- Primer: #2E7D32 (Hijau) untuk metrik positif, pendapatan
- Sekunder: #FFC107 (Kuning) untuk sorotan, penekanan
- Aksen: #1976D2 (Biru) untuk informasi sekunder
- Latar Belakang: #F5F5F5 (Abu-abu Muda) untuk latar belakang
- Teks: #212121 (Abu-abu Gelap) untuk teks yang mudah dibaca
- Peringatan: #D32F2F (Merah) untuk metrik negatif, peringatan

**4. Tipografi**

- Judul: Roboto Bold, 18-24pt untuk judul bagian
- Isi: Roboto Regular, 10-12pt untuk label dan teks
- Angka/Metrik: Roboto Medium, 14-16pt untuk angka KPI
- Font family konsisten di semua halaman

**5. Jarak & Tata Letak**

- Sistem grid konsisten dengan layout 12-kolom
- Padding: 8px/16px/24px untuk konsistensi
- Margin: 24px pada tepi dashboard
- Jarak kartu: 16px antar visualisasi
- Kelompokkan visualisasi terkait dengan warna latar belakang

### 2.3.5 Implementasi di Looker Studio

Implementasi dashboard dilakukan dengan langkah-langkah sebagai berikut:

**1. Pengaturan Data Source**
- Buat data sources untuk setiap tabel Google Sheets
- Konfigurasi properti kolom (tipe, agregasi)
- Buat calculated fields untuk metrik turunan
- Atur data blending untuk menggabungkan tabel

**2. Pembuatan Halaman Dashboard**
- Buat 7 halaman sesuai struktur yang dirancang
- Atur navigasi halaman dengan menu dropdown atau tabs
- Konfigurasi filter tingkat halaman

**3. Penambahan Visualisasi**
- Tambahkan scorecard untuk metrik KPI
- Buat time series charts untuk analisis tren
- Buat bar charts untuk perbandingan kategorikal
- Buat pie charts untuk analisis komposisi
- Buat tabel untuk data detail
- Buat geo maps untuk analisis geografis

**4. Kontrol Interaktif**
- Pemilih rentang tanggal untuk filter periode
- Filter dropdown untuk kategori, saluran, status
- Filter checkbox untuk pemilihan ganda
- Konfigurasi cakupan filter (tingkat halaman atau laporan)

**5. Styling & Formatting**
- Terapkan skema warna yang konsisten
- Atur gaya dan ukuran font
- Tambahkan border dan shadow untuk kedalaman visual
- Konfigurasi format angka (mata uang, persentase)
- Tambahkan tooltips untuk konteks tambahan

**6. Pengujian**
- Uji interaktivitas (filter, drill-down)
- Uji akurasi data
- Uji kinerja (waktu loading)
- Uji desain responsif pada berbagai perangkat
- User Acceptance Testing (UAT) dengan pemangku kepentingan

### 2.3.6 Pengujian dan Evaluasi

Tahap pengujian dan evaluasi dilakukan untuk memastikan dashboard memenuhi kebutuhan dan berfungsi dengan baik:

**1. Pengujian Fungsional**
- Validasi akurasi data dan perhitungan
- Uji semua kontrol interaktif (filter, pemilih tanggal)
- Verifikasi cross-filtering antar visualisasi
- Uji fungsi drill-down
- Validasi mekanisme refresh data

**2. Pengujian Kinerja**
- Ukur waktu loading untuk setiap halaman
- Uji dengan volume data yang berbeda
- Optimalkan query yang lambat
- Uji pengguna konkuren (beberapa pengguna mengakses bersamaan)

**3. Pengujian Kegunaan**
- Uji dengan pengguna sebenarnya (pemangku kepentingan SATRIAMART)
- Amati perilaku pengguna dan titik kesulitan
- Kumpulkan feedback tentang kemudahan penggunaan
- Identifikasi area untuk perbaikan
- Iterasi desain berdasarkan feedback

**4. Pengujian Kompatibilitas**
- Uji pada berbagai browser (Chrome, Firefox, Safari, Edge)
- Uji pada berbagai perangkat (desktop, tablet, mobile)
- Uji pada resolusi layar yang berbeda
- Verifikasi desain responsif

**5. Validasi Kualitas Data**
- Cross-check metrik dengan data sumber
- Validasi calculated fields dengan perhitungan manual
- Verifikasi agregasi dan filter
- Periksa anomali data

**6. Evaluasi Nilai Bisnis**
- Evaluasi apakah dashboard menjawab pertanyaan bisnis
- Nilai kemampuan tindak lanjut dari wawasan yang dihasilkan
- Ukur waktu yang dihemat dibandingkan analisis manual
- Kumpulkan feedback kepuasan pemangku kepentingan

Hasil evaluasi digunakan untuk perbaikan iteratif dashboard hingga mencapai tingkat kepuasan optimal dari pengguna.

---

*[Lanjutan ke BAB III akan mencakup pembahasan implementasi detail, tangkapan layar dashboard, dan analisis wawasan]*
