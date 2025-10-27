# BAB II  
# LANDASAN TEORI

## 2.1 Landasan Teori

### 2.1.1 Business Intelligence

Business Intelligence (BI) merupakan istilah umum yang mencakup aplikasi, infrastruktur, tools, dan praktik terbaik yang memungkinkan akses dan analisis informasi untuk meningkatkan dan mengoptimalkan keputusan dan kinerja organisasi (Turban et al., 2021). Menurut Davenport (2020), Business Intelligence adalah seperangkat teknologi dan proses yang menggunakan data untuk memahami dan menganalisis performa bisnis guna mendorong perencanaan strategis yang lebih baik.

Antonius (2023) mendefinisikan Business Intelligence sebagai proses pengumpulan data mentah, pengolahan data menjadi informasi, dan transformasi informasi menjadi pengetahuan yang dapat digunakan untuk pengambilan keputusan bisnis. Dalam konteks UMKM, BI berfungsi sebagai alat untuk mengubah data operasional sehari-hari menjadi insight yang actionable untuk meningkatkan daya saing bisnis.

Komponen utama dalam sistem Business Intelligence menurut Turban et al. (2021) meliputi:

1. **Data Warehouse**: Repositori terpusat yang menyimpan data historis dari berbagai sumber untuk keperluan analisis dan pelaporan.

2. **Business Analytics**: Kumpulan teknik analisis yang digunakan untuk mengeksplorasi data, mengidentifikasi pola, dan membuat prediksi.

3. **Data Visualization**: Presentasi data dalam bentuk visual seperti grafik, chart, dan dashboard untuk memudahkan pemahaman dan interpretasi.

4. **Performance Management**: Sistem untuk memantau dan mengelola kinerja organisasi berdasarkan Key Performance Indicators (KPI).

5. **User Interface**: Antarmuka yang memungkinkan pengguna berinteraksi dengan sistem BI untuk mengakses informasi dan melakukan analisis.

Menurut Howson (2021), implementasi Business Intelligence yang sukses harus memenuhi beberapa prinsip kunci:

- **Relevansi**: Informasi yang disajikan harus relevan dengan kebutuhan bisnis dan mendukung pengambilan keputusan strategis.

- **Akurasi**: Data harus akurat, konsisten, dan dapat dipercaya sebagai dasar pengambilan keputusan.

- **Ketepatan Waktu**: Informasi harus tersedia tepat waktu ketika dibutuhkan untuk pengambilan keputusan.

- **Aksesibilitas**: Informasi harus mudah diakses oleh stakeholder yang berwenang melalui interface yang user-friendly.

- **Actionability**: Insight yang dihasilkan harus dapat ditindaklanjuti dan memberikan nilai tambah bagi organisasi.

Dalam konteks perusahaan skala kecil seperti SATRIAMART, implementasi BI dapat membantu dalam beberapa area kritis:

1. **Analisis Penjualan**: Memahami tren penjualan, produk terlaris, dan performa channel penjualan.

2. **Manajemen Inventory**: Optimasi stok produk berdasarkan demand forecasting dan analisis perputaran barang.

3. **Customer Relationship Management**: Memahami karakteristik pelanggan, pola pembelian, dan segmentasi untuk targeted marketing.

4. **Analisis Profitabilitas**: Evaluasi margin keuntungan per produk, per kategori, dan per channel untuk optimasi pricing strategy.

5. **Marketing Effectiveness**: Mengukur ROI kampanye pemasaran dan mengidentifikasi channel marketing yang paling efektif.

### 2.1.2 Dashboard dan Key Performance Indicator

Dashboard adalah alat visualisasi yang menyajikan informasi penting dan Key Performance Indicators (KPI) dalam satu layar untuk memudahkan monitoring dan analisis kinerja bisnis (Howson, 2021). Dashboard yang efektif harus menyajikan informasi yang paling relevan dengan cara yang mudah dipahami, memungkinkan pengguna untuk mengidentifikasi masalah dan peluang dengan cepat.

Menurut Few (2013) dalam Turban et al. (2021), dashboard yang baik memiliki karakteristik sebagai berikut:

1. **Simple**: Menampilkan informasi tanpa kompleksitas yang tidak perlu, fokus pada data yang paling penting.

2. **Communicative**: Menyampaikan informasi dengan jelas dan mudah dipahami oleh target audience.

3. **Relevant**: Menampilkan informasi yang relevan dengan kebutuhan bisnis dan konteks pengambilan keputusan.

4. **Timely**: Menyajikan informasi yang up-to-date dan real-time atau near-real-time.

5. **Actionable**: Memberikan insight yang dapat ditindaklanjuti untuk perbaikan kinerja bisnis.

Key Performance Indicator (KPI) adalah metrik kuantitatif yang mencerminkan faktor kesuksesan kritis suatu organisasi (Antonius, 2023). KPI digunakan untuk mengukur pencapaian tujuan strategis dan memberikan indikasi tentang performa bisnis. Karakteristik KPI yang baik mengikuti prinsip SMART:

- **Specific**: Jelas dan spesifik dalam mengukur aspek tertentu dari bisnis.
- **Measurable**: Dapat diukur secara kuantitatif dengan data yang tersedia.
- **Achievable**: Realistis dan dapat dicapai dengan sumber daya yang ada.
- **Relevant**: Relevan dengan tujuan strategis organisasi.
- **Time-bound**: Memiliki periode waktu pengukuran yang jelas.

Dalam konteks SATRIAMART, KPI yang relevan mencakup:

**KPI Penjualan**:
- Total Revenue (pendapatan total)
- Growth Rate (tingkat pertumbuhan)
- Average Order Value/AOV (nilai rata-rata transaksi)
- Number of Transactions (jumlah transaksi)

**KPI Produk**:
- Best Selling Products (produk terlaris)
- Profit Margin per Product (margin keuntungan per produk)
- Inventory Turnover Rate (tingkat perputaran stok)
- Stock-out Frequency (frekuensi kehabisan stok)

**KPI Pelanggan**:
- Customer Acquisition Cost/CAC (biaya akuisisi pelanggan)
- Customer Lifetime Value/CLV (nilai lifetime pelanggan)
- Repeat Purchase Rate (tingkat pembelian ulang)
- Customer Satisfaction Score (skor kepuasan pelanggan)

**KPI Operasional**:
- Order Fulfillment Time (waktu penyelesaian pesanan)
- Order Completion Rate (tingkat penyelesaian pesanan)
- Cancellation Rate (tingkat pembatalan)

**KPI Finansial**:
- Gross Profit (laba kotor)
- Net Profit (laba bersih)
- Profit Margin (margin keuntungan)
- Return on Investment/ROI (tingkat pengembalian investasi)

**KPI Marketing**:
- Marketing ROI (ROI pemasaran)
- Conversion Rate (tingkat konversi)
- Cost per Acquisition (biaya per akuisisi)

### 2.1.3 Proses ETL (Extract, Transform, Load)

ETL merupakan proses fundamental dalam Business Intelligence yang terdiri dari tiga tahap: Extract (ekstraksi), Transform (transformasi), dan Load (pemuatan) data dari sumber ke data warehouse atau sistem analitik (Turban et al., 2021).

**1. Extract (Ekstraksi)**

Proses ekstraksi melibatkan pengambilan data dari berbagai sumber seperti database transaksional, file spreadsheet, API, atau sistem eksternal lainnya. Menurut Valentinus (2017), tahap ekstraksi harus memperhatikan:

- Identifikasi sumber data yang relevan
- Validasi ketersediaan dan aksesibilitas data
- Penentuan frequency extract (batch atau real-time)
- Handling data yang berubah atau bertambah

Dalam konteks SATRIAMART, sumber data meliputi:
- Data transaksi penjualan dari sistem pencatatan manual
- Data produk dari katalog internal
- Data pelanggan dari database kontak
- Data biaya dari pencatatan keuangan
- Data marketing dari platform media sosial

**2. Transform (Transformasi)**

Transformasi adalah proses pembersihan, validasi, dan pengolahan data mentah menjadi format yang sesuai untuk analisis. Proses transformasi mencakup:

- **Data Cleaning**: Menghapus duplikasi, menangani missing values, memperbaiki format data yang tidak konsisten.

- **Data Validation**: Memastikan data memenuhi kriteria kualitas dan akurasi yang ditetapkan.

- **Data Integration**: Menggabungkan data dari berbagai sumber dengan konsistensi schema dan format.

- **Data Aggregation**: Melakukan agregasi data untuk keperluan analisis summary (misalnya total penjualan per bulan).

- **Data Enrichment**: Menambahkan informasi tambahan atau calculated fields untuk memperkaya dataset.

Menurut Antonius (2023), kualitas data sangat menentukan kualitas insight yang dihasilkan. Oleh karena itu, proses transformasi harus dilakukan dengan cermat untuk memastikan data yang akurat dan konsisten.

**3. Load (Pemuatan)**

Tahap load melibatkan pemuatan data yang sudah ditransformasi ke dalam data warehouse atau sistem analitik. Metode load yang umum digunakan:

- **Full Load**: Memuat seluruh dataset dari awal, biasanya untuk initial load.

- **Incremental Load**: Memuat hanya data yang baru atau berubah sejak load terakhir, lebih efisien untuk data yang besar.

- **Real-time Load**: Memuat data secara real-time atau near-real-time untuk kebutuhan monitoring real-time.

Dalam implementasi dashboard SATRIAMART menggunakan Looker Studio, proses ETL dilakukan dengan:

1. **Extract**: Data diekstrak dari sistem pencatatan internal SATRIAMART dan dikumpulkan dalam format CSV.

2. **Transform**: Data dibersihkan dan ditransformasi menggunakan spreadsheet tools dan Python untuk memastikan konsistensi format, menangani missing values, dan membuat calculated fields.

3. **Load**: Data hasil transformasi diupload ke Google Sheets sebagai data source untuk Looker Studio.

### 2.1.4 Looker Studio sebagai Tools Business Intelligence

Looker Studio (sebelumnya Google Data Studio) adalah platform Business Intelligence berbasis cloud yang disediakan oleh Google untuk membuat laporan dan dashboard interaktif (Google, 2023). Looker Studio memungkinkan pengguna untuk mengkoneksikan berbagai sumber data, melakukan transformasi data, membuat visualisasi, dan berbagi dashboard dengan stakeholder.

**Keunggulan Looker Studio:**

1. **Gratis**: Platform ini dapat digunakan secara gratis tanpa biaya lisensi, sangat cocok untuk UMKM dengan budget terbatas.

2. **User-Friendly**: Interface drag-and-drop yang intuitif memudahkan pembuatan dashboard tanpa memerlukan coding.

3. **Integrasi Data**: Mendukung integrasi dengan 100+ data connector termasuk Google Sheets, Google Analytics, BigQuery, MySQL, PostgreSQL, dan layanan cloud lainnya.

4. **Kolaborasi**: Memungkinkan kolaborasi real-time dan sharing dashboard dengan akses yang dapat dikontrol.

5. **Interaktif**: Dashboard yang dibuat memiliki fitur interaktif seperti filter, date range selector, dan drill-down.

6. **Responsive**: Dashboard secara otomatis responsive dan dapat diakses dari berbagai devices.

7. **Customizable**: Mendukung custom branding, warna, font, dan layout sesuai kebutuhan organisasi.

**Komponen Utama Looker Studio:**

1. **Data Source**: Koneksi ke sumber data yang akan digunakan dalam dashboard.

2. **Report/Dashboard**: Canvas untuk membuat dan mengatur visualisasi data.

3. **Charts**: Berbagai jenis visualisasi seperti bar chart, line chart, pie chart, table, scorecard, geo map, dll.

4. **Controls**: Elemen interaktif seperti date range picker, dropdown filter, checkbox filter untuk eksplorasi data.

5. **Parameters**: Variabel yang dapat digunakan untuk membuat calculated fields atau logic kondisional.

6. **Calculated Fields**: Field yang dibuat dari kombinasi atau transformasi fields yang sudah ada.

**Jenis Visualisasi dalam Looker Studio:**

1. **Scorecard**: Menampilkan single metric value, cocok untuk KPI utama.

2. **Time Series Chart**: Line chart untuk menampilkan tren data over time.

3. **Bar Chart**: Menampilkan perbandingan nilai across categories.

4. **Pie/Donut Chart**: Menampilkan proporsi atau komposisi dari keseluruhan.

5. **Table**: Menampilkan data dalam format tabel dengan opsi sorting dan pagination.

6. **Geo Map**: Visualisasi data berdasarkan lokasi geografis.

7. **Combo Chart**: Kombinasi line chart dan bar chart untuk membandingkan metrics dengan skala berbeda.

8. **Bullet Chart**: Menampilkan actual value vs target value.

9. **Scatter Plot**: Menampilkan hubungan antara dua variabel numerik.

Pemilihan Looker Studio untuk implementasi dashboard SATRIAMART didasarkan pada beberapa pertimbangan:

- **Zero Cost**: Tidak ada biaya lisensi sehingga sustainable untuk UMKM.
- **Cloud-based**: Tidak memerlukan infrastruktur server sendiri.
- **Easy Integration**: Integrasi mudah dengan Google Sheets sebagai data source.
- **Collaborative**: Memudahkan sharing dan kolaborasi dengan tim.
- **Learning Curve**: Relatif mudah dipelajari dibandingkan tools enterprise seperti Tableau atau Power BI.

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

Data transaksi penjualan mencatat setiap transaksi yang terjadi, meliputi ID transaksi, tanggal dan waktu transaksi, ID pelanggan, ID produk, jumlah item, harga satuan, subtotal, diskon, biaya custom, biaya ongkir, total pembayaran, metode pembayaran, status pembayaran, status pesanan, channel penjualan, catatan pesanan, waktu pengerjaan, rating pelanggan, dan tanggal selesai.

Total transaksi yang dianalisis sebanyak 320 transaksi selama 12 bulan dengan total revenue Rp 111.976.550.

**3. Data Master Pelanggan**

Data pelanggan mencakup informasi demografis dan behavioral dari pelanggan SATRIAMART, meliputi ID pelanggan, nama lengkap, nomor telepon, email, alamat lengkap, kota, provinsi, kode pos, jenis pelanggan (Individu/Bisnis/Reseller), segmen (Retail/UMKM/Korporat), tanggal registrasi, total transaksi, total nilai pembelian, status, dan sumber awal pelanggan.

Total pelanggan yang tercatat sebanyak 180 pelanggan dengan distribusi:
- Individu/Retail: 108 pelanggan (60%)
- Bisnis/UMKM: 54 pelanggan (30%)
- Reseller/Korporat: 18 pelanggan (10%)

**4. Data Riwayat Stok**

Data riwayat stok mencatat pergerakan stok produk setiap bulan, meliputi ID stok, tanggal, ID produk, stok awal, stok masuk (pembelian/produksi), stok keluar (penjualan), stok akhir, jenis transaksi, dan keterangan.

**5. Data Biaya Operasional**

Data biaya operasional mencatat pengeluaran bisnis, meliputi ID biaya, tanggal, kategori biaya (Bahan Baku, Marketing, Operasional, Transportasi, Utilitas), sub-kategori, nominal, keterangan, dan metode pembayaran.

**6. Data Marketing Campaign**

Data kampanye pemasaran mencatat aktivitas marketing, meliputi ID campaign, nama campaign, platform (Instagram, Facebook, Google Ads, TikTok), tanggal mulai, tanggal selesai, budget, reach, engagement, conversion, revenue generated, dan ROI.

### 2.2.2 Sumber Data

Sumber data dalam penelitian ini berasal dari sistem pencatatan internal SATRIAMART yang telah disimulasikan dan diolah untuk keperluan pembelajaran dan analisis Business Intelligence. Data bersifat representatif dan mengikuti pola bisnis yang realistis untuk UMKM di bidang dekorasi dan aksesoris.

Sumber data spesifik meliputi:

1. **Sistem Pencatatan Penjualan**: Data transaksi penjualan dicatat dari nota penjualan, invoice, dan riwayat order dari berbagai channel (WhatsApp, Instagram, Marketplace, Offline).

2. **Database Produk**: Informasi produk dikelola dalam katalog digital yang mencakup spesifikasi lengkap setiap produk.

3. **Database Pelanggan**: Data pelanggan dikumpulkan dari form pemesanan, kontak WhatsApp/Instagram, dan riwayat transaksi.

4. **Pencatatan Keuangan**: Data biaya operasional berasal dari pencatatan pengeluaran bulanan yang dikelola oleh bagian keuangan.

5. **Laporan Marketing**: Data kampanye pemasaran diperoleh dari analytics platform media sosial (Instagram Insights, Facebook Ads Manager, Google Analytics).

Data yang telah dikumpulkan kemudian diolah dan disimpan dalam format CSV untuk memudahkan proses ETL dan integrasi dengan Looker Studio melalui Google Sheets.

### 2.2.3 Proses Pembersihan Data

Pembersihan data (data cleaning) merupakan tahap kritis dalam memastikan kualitas data yang akan dianalisis. Proses pembersihan data yang dilakukan dalam penelitian ini meliputi:

**1. Handling Missing Values**

- Identifikasi field yang memiliki missing values
- Untuk field numerik, missing values diganti dengan nilai 0 atau rata-rata tergantung konteks
- Untuk field categorical, missing values diganti dengan kategori "Unknown" atau "Other"
- Untuk field yang critical, record dengan missing values dihapus

**2. Duplicate Removal**

- Identifikasi dan hapus transaksi duplikat berdasarkan ID transaksi
- Validasi duplikasi pelanggan berdasarkan nomor telepon atau email
- Pastikan setiap record memiliki unique identifier

**3. Data Type Conversion**

- Konversi field tanggal ke format DATE yang standard (YYYY-MM-DD)
- Konversi field numerik (harga, jumlah) ke tipe NUMBER
- Konversi field categorical ke tipe STRING
- Validasi format email dan nomor telepon

**4. Outlier Detection**

- Identifikasi nilai ekstrim pada field harga, jumlah item, dan total pembayaran
- Validasi apakah outlier merupakan error atau valid business case
- Handle outlier dengan removal atau transformation sesuai konteks

**5. Standardisasi Format**

- Standarisasi format nama (proper case: huruf pertama kapital)
- Standarisasi format alamat dan kota
- Standarisasi kategori dan sub-kategori produk
- Standarisasi status pesanan dan status pembayaran

**6. Consistency Check**

- Validasi konsistensi antara subtotal dengan harga satuan × jumlah item
- Validasi total pembayaran = subtotal - diskon + biaya custom + ongkir
- Validasi tanggal selesai >= tanggal transaksi
- Validasi stok akhir = stok awal + stok masuk - stok keluar

### 2.2.4 Transformasi Data

Setelah data dibersihkan, dilakukan transformasi untuk memperkaya dataset dan memudahkan analisis. Proses transformasi yang dilakukan meliputi:

**1. Calculated Fields**

Membuat field baru hasil perhitungan:
- Profit = Harga Jual - Harga Modal
- Profit Margin = (Profit / Harga Jual) × 100%
- Discount Amount = Subtotal × Discount Percentage / 100
- Net Revenue = Total Pembayaran - COGS
- Average Order Value = Total Revenue / Number of Transactions

**2. Date Dimensions**

Ekstraksi komponen tanggal untuk analisis temporal:
- Year, Month, Quarter dari tanggal transaksi
- Day of Week (Senin-Minggu)
- Week of Year
- Is Weekend (TRUE/FALSE)
- Month Name (Januari-Desember)

**3. Categorical Grouping**

Membuat kategori baru untuk analisis segmentasi:
- Price Range: Low (< 100K), Medium (100K-300K), High (> 300K)
- Customer Value Segment: Low, Medium, High berdasarkan total pembelian
- Order Size: Small (1 item), Medium (2-3 items), Large (> 3 items)
- Geographic Region: Depok, Jakarta, Tangerang-Bekasi, Other

**4. Aggregation**

Membuat summary data untuk dashboard:
- Total Revenue per Month
- Total Transactions per Product Category
- Average Rating per Product
- Total Customers per City
- Total Campaign Budget per Platform

**5. Joining Tables**

Menggabungkan data dari multiple tables:
- Join Transaksi dengan Master Produk untuk mendapatkan kategori dan harga modal
- Join Transaksi dengan Master Pelanggan untuk mendapatkan informasi demografis
- Join Transaksi dengan Riwayat Stok untuk analisis inventory turnover

**6. Data Enrichment**

Menambahkan informasi tambahan:
- Customer Lifetime Value (CLV) = Total Nilai Pembelian Pelanggan
- Recency = Selisih hari dari transaksi terakhir
- Frequency = Jumlah transaksi pelanggan
- Monetary = Total spending pelanggan
- RFM Score untuk segmentasi pelanggan

## 2.3 Metode Perancangan

### 2.3.1 Analisis Kebutuhan Pengguna

Tahap awal dalam perancangan dashboard adalah memahami kebutuhan pengguna. Analisis kebutuhan dilakukan melalui diskusi dengan stakeholder SATRIAMART untuk mengidentifikasi:

**1. User Personas**

Identifikasi tiga kelompok pengguna utama:
- **Owner/Top Management**: Membutuhkan high-level overview, KPI summary, dan strategic insights
- **Marketing Manager**: Membutuhkan analisis kampanye, customer segmentation, dan channel performance
- **Operations Manager**: Membutuhkan analisis inventory, fulfillment metrics, dan operational efficiency

**2. Information Requirements**

Untuk setiap user persona, diidentifikasi informasi yang dibutuhkan:
- Metrics apa yang paling penting untuk dimonitor?
- Visualisasi apa yang paling efektif untuk menyajikan informasi?
- Seberapa detail level informasi yang dibutuhkan?
- Seberapa sering informasi perlu diupdate?

**3. Decision Support Needs**

Identifikasi keputusan bisnis yang perlu didukung oleh dashboard:
- Produk mana yang harus diprioritaskan untuk produksi?
- Channel marketing mana yang paling efektif?
- Segmen pelanggan mana yang paling profitable?
- Kapan timing terbaik untuk promosi?

**4. Constraints & Limitations**

Identifikasi batasan dalam implementasi:
- Budget: Menggunakan free tools (Looker Studio, Google Sheets)
- Technical Skills: User memiliki basic computer skills, tidak familiar dengan tools advanced
- Data Availability: Data tersedia dalam format spreadsheet
- Update Frequency: Manual update, tidak real-time

### 2.3.2 Identifikasi Key Performance Indicators

Berdasarkan analisis kebutuhan, diidentifikasi KPI yang relevan untuk setiap area bisnis:

**KPI Penjualan (Sales KPIs)**:
- Total Revenue: Total pendapatan dari seluruh transaksi
- Number of Transactions: Jumlah transaksi yang terjadi
- Average Order Value (AOV): Rata-rata nilai per transaksi
- Growth Rate: Tingkat pertumbuhan revenue month-over-month
- Sales per Channel: Revenue dari setiap channel penjualan
- Sales per Product Category: Revenue dari setiap kategori produk

**KPI Produk (Product KPIs)**:
- Top 10 Best Selling Products: Produk dengan jumlah penjualan tertinggi
- Revenue per Product: Pendapatan yang dihasilkan setiap produk
- Profit Margin per Product: Margin keuntungan setiap produk
- Inventory Turnover Rate: Kecepatan perputaran inventory
- Stock-out Frequency: Frekuensi kehabisan stok

**KPI Pelanggan (Customer KPIs)**:
- Total Customers: Jumlah total pelanggan
- New Customers: Jumlah pelanggan baru per periode
- Repeat Customer Rate: Persentase pelanggan yang melakukan pembelian ulang
- Customer Lifetime Value (CLV): Nilai total pembelian pelanggan
- Customer Satisfaction Score: Rata-rata rating dari pelanggan

**KPI Operasional (Operational KPIs)**:
- Order Fulfillment Time: Rata-rata waktu penyelesaian pesanan
- Order Completion Rate: Persentase pesanan yang selesai
- Cancellation Rate: Persentase pesanan yang dibatalkan
- On-time Delivery Rate: Persentase pesanan yang selesai tepat waktu

**KPI Finansial (Financial KPIs)**:
- Gross Revenue: Total pendapatan kotor
- Total Costs: Total biaya operasional
- Net Profit: Laba bersih
- Profit Margin: Persentase margin keuntungan
- Cost per Transaction: Biaya rata-rata per transaksi

**KPI Marketing (Marketing KPIs)**:
- Marketing ROI: Return on Investment dari kampanye marketing
- Conversion Rate per Channel: Tingkat konversi setiap channel
- Cost per Acquisition (CPA): Biaya untuk acquire satu pelanggan baru
- Campaign Reach: Jangkauan kampanye marketing
- Engagement Rate: Tingkat engagement di media sosial

### 2.3.3 Persiapan Data (ETL)

Proses ETL untuk dashboard SATRIAMART dilakukan dengan langkah-langkah berikut:

**1. Extract (Ekstraksi)**
- Kumpulkan data mentah dari berbagai sumber (pencatatan penjualan, inventory, keuangan)
- Export data ke format CSV
- Validasi kelengkapan data

**2. Transform (Transformasi)**
- Data cleaning: hapus duplikat, handle missing values, fix format inconsistencies
- Data transformation: buat calculated fields, extract date dimensions, categorization
- Data enrichment: tambahkan derived metrics (profit, margin, RFM score)
- Data aggregation: buat summary tables untuk performance optimization

**3. Load (Pemuatan)**
- Upload CSV files ke Google Sheets
- Buat separate sheets untuk setiap table (master_produk, master_pelanggan, transaksi_penjualan, dll)
- Setup proper naming convention dan structure
- Validate data integrity setelah upload

**4. Data Source Setup di Looker Studio**
- Connect Looker Studio ke Google Sheets
- Setup data source untuk setiap sheet
- Configure field types (date, number, text)
- Create blended data sources untuk join multiple tables

### 2.3.4 Perancangan Layout Dashboard

Layout dashboard dirancang mengikuti prinsip-prinsip visual hierarchy dan best practices dashboard design:

**1. Dashboard Structure**

Dashboard terdiri dari 7 halaman (pages):
- Page 1: Executive Summary / Overview
- Page 2: Sales Analysis
- Page 3: Product Performance
- Page 4: Customer Analysis
- Page 5: Operational Metrics
- Page 6: Financial Analysis
- Page 7: Marketing Performance

**2. Visual Hierarchy**

Setiap page mengikuti struktur:
- **Header**: Logo, judul dashboard, filter controls
- **KPI Cards**: 4-6 scorecard menampilkan key metrics di bagian atas
- **Primary Visualizations**: 2-3 chart utama yang menjawab pertanyaan bisnis paling penting
- **Secondary Visualizations**: Chart detail dan supporting information
- **Footer**: Last update timestamp, data source info

**3. Color Scheme**

Pemilihan warna konsisten dengan branding SATRIAMART:
- Primary: #2E7D32 (Green) untuk positive metrics, revenue
- Secondary: #FFC107 (Gold/Yellow) untuk highlights, emphasis
- Accent: #1976D2 (Blue) untuk secondary information
- Background: #F5F5F5 (Light Gray) untuk background
- Text: #212121 (Dark Gray) untuk readable text
- Alert: #D32F2F (Red) untuk negative metrics, warnings

**4. Typography**

- Headers: Roboto Bold, 18-24pt untuk judul section
- Body: Roboto Regular, 10-12pt untuk labels dan text
- Numbers/Metrics: Roboto Medium, 14-16pt untuk angka KPI
- Font family konsisten across all pages

**5. Spacing & Layout**

- Consistent grid system dengan 12-column layout
- Spacing: 8px/16px/24px untuk consistency
- Margins: 24px pada tepi dashboard
- Card spacing: 16px antar visualizations
- Group related visualizations dengan background color

### 2.3.5 Implementasi di Looker Studio

Implementasi dashboard dilakukan dengan langkah-langkah sebagai berikut:

**1. Setup Data Sources**
- Create data sources untuk setiap Google Sheets table
- Configure field properties (type, aggregation)
- Create calculated fields untuk derived metrics
- Setup data blending untuk join tables

**2. Create Dashboard Pages**
- Buat 7 pages sesuai struktur yang dirancang
- Set page navigation dengan dropdown atau tabs
- Configure page-level filters

**3. Add Visualizations**
- Tambahkan scorecard untuk KPI metrics
- Buat time series chart untuk trend analysis
- Buat bar chart untuk categorical comparison
- Buat pie chart untuk composition analysis
- Buat table untuk detailed data
- Buat geo map untuk geographic analysis

**4. Add Interactive Controls**
- Date range picker untuk filter periode
- Dropdown filters untuk kategori, channel, status
- Checkbox filters untuk multiple selection
- Configure filter scope (page-level atau report-level)

**5. Styling & Formatting**
- Apply color scheme konsisten
- Set font styles dan sizes
- Add borders dan shadows untuk visual depth
- Configure number formatting (currency, percentage)
- Add tooltips untuk additional context

**6. Testing**
- Test interactivity (filters, drill-down)
- Test data accuracy
- Test performance (loading time)
- Test responsive design pada berbagai devices
- UAT (User Acceptance Testing) dengan stakeholder

### 2.3.6 Pengujian dan Evaluasi

Tahap pengujian dan evaluasi dilakukan untuk memastikan dashboard memenuhi requirements dan berfungsi dengan baik:

**1. Functional Testing**
- Validasi akurasi data dan calculations
- Test semua interactive controls (filters, date pickers)
- Verify cross-filtering antar visualizations
- Test drill-down functionality
- Validate data refresh mechanism

**2. Performance Testing**
- Measure loading time untuk setiap page
- Test dengan volume data yang berbeda
- Optimize queries yang lambat
- Test concurrent users (multiple users akses bersamaan)

**3. Usability Testing**
- Test dengan actual users (stakeholder SATRIAMART)
- Observe user behavior dan pain points
- Collect feedback tentang ease of use
- Identify areas untuk improvement
- Iterate design based on feedback

**4. Compatibility Testing**
- Test pada berbagai browser (Chrome, Firefox, Safari, Edge)
- Test pada berbagai devices (desktop, tablet, mobile)
- Test pada berbagai screen resolutions
- Verify responsive design

**5. Data Quality Validation**
- Cross-check metrics dengan source data
- Validate calculated fields dengan manual calculation
- Verify aggregations dan filters
- Check untuk data anomalies

**6. Business Value Evaluation**
- Evaluate apakah dashboard menjawab business questions
- Assess actionability dari insights yang dihasilkan
- Measure time saved dibandingkan manual analysis
- Collect stakeholder satisfaction feedback

Hasil evaluasi digunakan untuk iterative improvement dashboard hingga mencapai tingkat kepuasan optimal dari pengguna.

---

*[Lanjutan ke BAB III akan mencakup pembahasan implementasi detail, screenshot dashboard, dan analisis insight]*
