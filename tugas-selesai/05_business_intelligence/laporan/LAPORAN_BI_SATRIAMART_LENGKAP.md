# PERANCANGAN *DASHBOARD BUSINESS INTELLIGENCE* INTERAKTIF UNTUK MENDUKUNG KEPUTUSAN BISNIS PADA SATRIAMART



## MAKALAH

Diajukan untuk memenuhi salah satu tugas kelompok mata kuliah *Business Intelligence*



Nama Anggota Kelompok : 

1. Roki Anjas (11250066)
2. Fahruroji (11250085)
3. Susanto (11250068)



Kelas: 11.7C.12 





**PROGRAM STUDI INFORMATIKA**

**UNIVERSITAS NUSA MANDIRI**

**JAKARTA**

**2025**





## KATA PENGANTAR

Puji syukur kepada Tuhan Yang Maha Esa atas segala rahmat dan karunia-Nya sehingga penyusun dapat menyelesaikan laporan tugas akhir yang berjudul 

"Perancangan *Dashboard Business Intelligence* Interaktif untuk Mendukung Keputusan Bisnis pada SATRIAMART" dengan baik. 

Laporan ini disusun untuk memenuhi tugas akhir mata kuliah *Business Intelligence* II (Kode 493) Program Studi Sistem Informasi, Fakultas Teknologi Informasi, Universitas Nusa Mandiri. Tujuan dari penyusunan laporan ini adalah untuk mengaplikasikan konsep *Business Intelligence* dalam merancang *dashboard* interaktif yang dapat memberikan wawasan data untuk mendukung pengambilan keputusan bisnis pada perusahaan skala kecil. 

Penyusun menyadari bahwa penyelesaian laporan ini tidak lepas dari bantuan berbagai pihak. Oleh karena itu, penyusun mengucapkan terima kasih kepada: Bapak Ridan Nurfalah, M.Kom, selaku dosen pengampu mata kuliah *Business Intelligence* II yang telah memberikan bimbingan dan arahan selama proses pembelajaran. 

Pihak SATRIAMART yang telah memberikan izin dan kesempatan untuk menjadikan perusahaannya sebagai objek penelitian. Rekan-rekan kelompok yang telah bekerja sama dengan baik dalam menyelesaikan tugas ini. Semua pihak yang tidak dapat disebutkan satu per satu yang telah membantu dalam penyelesaian laporan ini. Penyusun menyadari bahwa laporan ini masih jauh dari sempurna. 

Oleh karena itu, penyusun mengharapkan kritik dan saran yang membangun demi perbaikan di masa mendatang. Semoga laporan ini dapat bermanfaat bagi pengembangan ilmu *Business Intelligence* khususnya dalam penerapannya pada Usaha Mikro, Kecil, dan Menengah (UMKM) di Indonesia. 



Jakarta, Desember 2025 





Penyusun

## ABSTRAK

**Roki Anjas (11250066), Fahruroji (11250085), Susanto (11250068)**

**"Perancangan *Dashboard Business Intelligence* Interaktif Untuk Mendukung Keputusan Bisnis Pada Satriamart"**



*Business Intelligence* (BI) merupakan pendekatan sistematis untuk mengumpulkan, menganalisis, dan menyajikan informasi bisnis guna mendukung pengambilan keputusan yang lebih baik. Penelitian ini bertujuan merancang dan mengimplementasikan *dashboard Business Intelligence* interaktif menggunakan *Looker Studio* untuk SATRIAMART, perusahaan skala kecil yang bergerak di bidang dekorasi dan aksesoris akrilik, dengan memberikan visualisasi data penjualan, produk, pelanggan, dan keuangan secara *real-time* dan interaktif. Metodologi yang digunakan meliputi analisis kebutuhan pengguna, identifikasi *Key Performance Indicators* (KPI), proses *Extract-Transform-Load* (ETL) data, perancangan *layout dashboard*, implementasi menggunakan *Looker Studio*, serta pengujian dan evaluasi terhadap data transaksi penjualan, produk, pelanggan, riwayat stok, biaya operasional, dan kampanye pemasaran selama periode 12 bulan (Januari-Desember 2025). Hasil penelitian menunjukkan *dashboard Business Intelligence* yang dikembangkan mampu menyajikan informasi bisnis secara komprehensif melalui berbagai visualisasi seperti *bar chart, line chart, pie chart, table*, dan *scorecard* dalam tujuh halaman utama: *Executive Summary, Sales Analysis, Product Performance, Customer Analysis, Operational Metrics, Financial Analysis*, dan *Marketing Performance*. Implementasi *dashboard* memberikan manfaat praktis bagi SATRIAMART berupa peningkatan efisiensi analisis data, pengambilan keputusan yang lebih cepat dan akurat, identifikasi peluang bisnis baru, serta optimasi strategi pemasaran dan operasional. Penelitian ini membuktikan bahwa teknologi *Business Intelligence* dapat diterapkan secara efektif pada perusahaan skala kecil dengan biaya terjangkau menggunakan *platform cloud-based* seperti *Looker Studio*. 


**Kata kunci:** *Business Intelligence*, *Dashboard* Interaktif, *Looker Studio*, Visualisasi Data, Indikator Kinerja Utama, UMKM, Analisis Data.
## DAFTAR TABEL

Tabel 2.1 Distribusi Produk Berdasarkan Kategori ........................................................... 

Tabel 2.2 Distribusi Pelanggan Berdasarkan Segmen ....................................................... 

Tabel 2.3 Distribusi Masalah Kualitas Data per File .........................................................  

Tabel 2.4 Perbandingan Kualitas Data Sebelum dan Sesudah Pembersihan .................... 

Tabel 2.5 Key Performance Indicators (KPI) per Dashboard ............................................ 

Tabel 3.1 Analisis Harga vs Volume Penjualan ................................................................ 

Tabel 3.2 Segmentasi Pelanggan vs Nilai Rata-rata Pesanan ............................................ 

Tabel 3.3 Waktu Penyelesaian vs Kepuasan Pelanggan ................................................... 

Tabel 3.4 ROI Kampanye Pemasaran per Platform .......................................................... 

Tabel 3.5 Komponen Visualisasi Executive Dashboard .................................................... 

Tabel 3.6 Komponen Visualisasi Sales Analysis ............................................................... 

Tabel 3.7 Komponen Visualisasi Product Performance .................................................... 

Tabel 3.8 Komponen Visualisasi Customer Analysis ........................................................ 

Tabel 3.9 Komponen Visualisasi Financial Analysis ........................................................ 

Tabel 3.10 Komponen Visualisasi Operations & Inventory ................................................ 

Tabel 3.11 Komponen Visualisasi Marketing Performance ................................................ 

Tabel 4.1 Ringkasan KPI Dashboard SATRIAMART ......................................................... 



## DAFTAR GAMBAR

Gambar 2.1 Proses ETL (Extract, Transform, Load) ......................................................... 

Gambar 2.2 Arsitektur Dashboard Business Intelligence ................................................... 

Gambar 2.3 Contoh Data Mentah dengan Masalah Kualitas Data ..................................... 

Gambar 2.4 Contoh Data Bersih Setelah Proses Cleaning ................................................. 

Gambar 3.1 Executive Dashboard - Overview Bisnis ........................................................ 

Gambar 3.2 Sales Analysis Dashboard .............................................................................. 

Gambar 3.3 Product Performance Dashboard .................................................................... 

Gambar 3.4 Customer Analysis Dashboard ....................................................................... 

Gambar 3.5 Financial Analysis Dashboard ........................................................................ 

Gambar 3.6 Operations & Inventory Dashboard ................................................................ 

Gambar 3.7 Marketing Performance Dashboard ................................................................ 

Gambar 3.8 Contoh Fitur Interaktif - Filter Controls ........................................................ 

Gambar 3.9 Contoh Fitur Interaktif - Drill-down .............................................................. 

Gambar 4.1 Alur Implementasi Dashboard Business Intelligence ..................................... 



# BAB I

# PENDAHULUAN

## 1.1. Latar Belakang Masalah

Dalam era digital saat ini, data telah menjadi aset penting bagi setiap organisasi bisnis, termasuk Usaha Mikro, Kecil, dan Menengah (UMKM). 

Ketersediaan data yang melimpah dari berbagai sumber seperti transaksi penjualan, interaksi pelanggan, dan operasional bisnis memberikan peluang besar bagi perusahaan untuk mengoptimalkan kinerja bisnis mereka. Namun, data mentah yang belum diolah tidak akan memberikan nilai tambah tanpa adanya proses analisis yang tepat. Di sinilah peran *Business Intelligence* (BI) menjadi sangat penting. *Business Intelligence* merupakan seperangkat teknologi, aplikasi, dan praktik untuk pengumpulan, integrasi, analisis, dan presentasi informasi bisnis (Turban et al., 2021). Tujuan utama BI adalah untuk mendukung pengambilan keputusan bisnis yang lebih baik melalui penyediaan informasi yang akurat, relevan, dan tepat waktu. Dengan implementasi BI yang tepat, perusahaan dapat mengidentifikasi peluang bisnis baru, mendeteksi masalah operasional sejak dini, memahami perilaku pelanggan, dan mengoptimalkan strategi pemasaran. 

SATRIAMART merupakan perusahaan skala kecil yang bergerak di bidang dekorasi dan aksesoris akrilik dengan produk unggulan berupa nomor rumah akrilik, papan petunjuk ( *signage*), papan nama, dan berbagai aksesoris dekorasi khusus. Berlokasi di Depok, Jawa Barat, SATRIAMART melayani pelanggan dari wilayah Jabodetabek dan sekitarnya melalui berbagai saluran penjualan seperti *Instagram, WhatsApp, platform* pasar daring ( *marketplace*), dan penjualan langsung.

Seperti halnya UMKM pada umumnya, SATRIAMART menghadapi tantangan dalam mengelola dan menganalisis data bisnis yang terus bertambah setiap harinya. Saat ini, SATRIAMART belum memiliki sistem informasi terintegrasi untuk melakukan analisis data secara komprehensif. Proses pengambilan keputusan masih dilakukan secara manual berdasarkan intuisi dan pengalaman, tanpa dukungan analisis data yang sistematis. Kondisi ini menyebabkan beberapa permasalahan seperti kesulitan dalam mengidentifikasi produk yang paling laris, ketidakpastian dalam merencanakan stok produk, 



minimnya pemahaman terhadap karakteristik dan preferensi pelanggan, serta kurangnya evaluasi terhadap efektivitas saluran penjualan dan kampanye pemasaran. *Dashboard Business Intelligence* interaktif dapat menjadi solusi untuk mengatasi permasalahan tersebut. *Dashboard* merupakan alat visualisasi data yang menyajikan informasi penting dalam bentuk grafik, diagram, dan indikator kinerja yang mudah dipahami (Howson, 2021). Dengan *dashboard*, manajemen dapat memantau kinerja bisnis secara *real-time*, mengidentifikasi *trend*, dan membuat keputusan berdasarkan data yang akurat. *Dashboard* yang interaktif juga memungkinkan pengguna untuk melakukan eksplorasi data lebih dalam melalui fitur *filter*, *drill-down*, dan *cross-filtering*. *Looker Studio* (sebelumnya dikenal sebagai *Google* Data Studio) merupakan *platform Business Intelligence* berbasis cloud yang disediakan oleh *Google* secara gratis. *Platform* ini memungkinkan pengguna untuk membuat *dashboard* interaktif dengan mudah tanpa memerlukan keahlian pemrograman yang mendalam. *Looker Studio* mendukung integrasi dengan berbagai sumber data termasuk *Google Sheets, Google Analytics, database* *SQL*, dan layanan *cloud* lainnya. Kemudahan penggunaan, biaya yang terjangkau (gratis), dan fitur kolaborasi yang baik menjadikan *Looker Studio* pilihan yang tepat untuk implementasi BI pada UMKM seperti SATRIAMART. 

Berdasarkan latar belakang tersebut, penelitian ini bertujuan untuk merancang dan mengimplementasikan *dashboard Business Intelligence* interaktif menggunakan *Looker* Studio untuk SATRIAMART. *Dashboard* yang dikembangkan diharapkan dapat memberikan wawasan yang bernilai bagi manajemen dalam mengambil keputusan strategis terkait pengembangan produk, strategi pemasaran, pengelolaan pelanggan, dan optimasi operasional bisnis. 

Penelitian ini juga diharapkan dapat menjadi referensi bagi UMKM lain dalam mengadopsi teknologi *Business Intelligence* untuk meningkatkan daya saing bisnis mereka. 





## 1.2. Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian ini adalah sebagai berikut: 

1. Bagaimana merancang *dashboard Business Intelligence* interaktif yang sesuai dengan kebutuhan bisnis SATRIAMART? 

2. *Visualisasi* data apa saja yang efektif untuk menyajikan informasi penjualan, produk, pelanggan, dan keuangan SATRIAMART? 

3. Wawasan bisnis apa yang dapat dihasilkan dari analisis data SATRIAMART menggunakan *dashboard Business Intelligence*? 

4. Bagaimana implementasi *dashboard Business Intelligence* dapat mendukung pengambilan keputusan bisnis pada SATRIAMART? 

5. Apa rekomendasi strategis yang dapat diberikan berdasarkan hasil analisis data untuk meningkatkan performa bisnis SATRIAMART? 



## 1.3. Tujuan

Tujuan dari penelitian ini adalah:

1. Merancang dan mengimplementasikan *dashboard Business Intelligence* interaktif untuk SATRIAMART menggunakan Looker Studio. 

2. Mengidentifikasi *Key Performance Indicators* (KPI) yang relevan dengan bisnis SATRIAMART untuk diintegrasikan dalam *dashboard*. 

3. Menganalisis data transaksi penjualan, produk, pelanggan, dan keuangan untuk menghasilkan wawasan bisnis yang bernilai. 

4. Menyajikan informasi bisnis melalui *visualisasi* data yang efektif dan mudah dipahami oleh pengguna. 

5. Memberikan rekomendasi strategis berdasarkan hasil analisis data untuk optimasi bisnis SATRIAMART. 

6. Mendemonstrasikan bahwa teknologi *Business Intelligence* dapat diterapkan secara efektif pada perusahaan skala kecil dengan biaya terjangkau. 





## 1.4. Manfaat

### 1.4.1. Manfaat Bagi SATRIAMART

1. Peningkatan Efisiensi Analisis Data : SATRIAMART dapat menganalisis data bisnis dengan lebih cepat dan efisien melalui *dashboard* yang terintegrasi dibandingkan dengan metode manual. 

2. Pengambilan Keputusan Berbasis Data : Manajemen dapat membuat keputusan bisnis yang lebih akurat dan terukur berdasarkan *insight* dari data, bukan hanya berdasarkan intuisi. 

3. Identifikasi Peluang Bisnis : *Dashboard* membantu mengidentifikasi produk terlaris, segmen pelanggan potensial, dan saluran penjualan paling efektif untuk optimasi strategi bisnis. 

4. *Monitoring* Kinerja *Real-Time*: Manajemen dapat memantau kinerja bisnis secara *real-time* dan merespons perubahan pasar dengan lebih cepat. 

5. Optimasi *Inventory*: Dengan analisis data penjualan dan stok, SATRIAMART dapat mengoptimalkan manajemen *inventory* dan mengurangi risiko *overstock* atau *stockout*. 

6. Evaluasi Efektivitas Marketing: *Dashboard* marketing *performance* memungkinkan evaluasi *Return on Investment* (ROI) kampanye *marketing* untuk alokasi *budget* yang lebih efektif. 

7. Peningkatan *Customer Satisfaction*: Dengan pemahaman yang lebih baik tentang karakteristik dan preferensi pelanggan, SATRIAMART dapat memberikan layanan yang lebih personal dan meningkatkan *customer satisfaction*. 

### 1.4.2. Manfaat Bagi Penyusun

1. Penerapan Ilmu *Business Intelligence*: Penyusun dapat mengaplikasikan konsep dan teori *Business Intelligence* yang telah dipelajari dalam kasus nyata. 

2. Peningkatan Kompetensi Teknis: Penyusun memperoleh pengalaman praktis dalam menggunakan perangkat *Business Intelligence* seperti *Looker Studio, Google Sheets*, dan teknik analisis data. 



3. Pengembangan *Soft Skills*: Penyusun mengembangkan kemampuan *problem solving*, *analytical thinking*, dan *communication skills* melalui proses penelitian dan presentasi. 

4. *Portfolio Project*: Hasil penelitian ini dapat menjadi *portfolio* yang bernilai untuk keperluan akademis maupun profesional. 

5. Pemahaman Bisnis UMKM: Penyusun memperoleh wawasan tentang tantangan dan peluang bisnis pada sektor UMKM khususnya di bidang dekorasi dan aksesoris. 

6. Kontribusi Sosial: Penyusun berkontribusi dalam membantu UMKM mengadopsi teknologi digital untuk peningkatan daya saing bisnis. 

## 1.5. Ruang Lingkup

Untuk menjaga fokus penelitian dan memastikan hasil yang optimal, ruang lingkup penelitian ini dibatasi sebagai berikut:

### 1.5.1. Batasan Data

1. Periode Data : Data yang dianalisis mencakup periode 12 bulan dari Januari 2025 hingga Desember 2025. 

2. Jenis Data : Data yang digunakan dalam penelitian ini mencakup master produk (50 produk), master pelanggan (180 pelanggan), transaksi penjualan (320 transaksi), riwayat stok (450 record), biaya operasional (144 record), dan kampanye pemasaran (36 kampanye) sepanjang tahun 2025.

3. Sumber Data : Data bersumber dari sistem pencatatan internal SATRIAMART yang telah diolah dan disimulasikan untuk keperluan pembelajaran. 

4. Cakupan Geografis: Analisis fokus pada pelanggan di wilayah Jabodetabek dan sekitarnya sebagai pasar utama SATRIAMART. 

### 1.5.2. Batasan Fitur Dashboard

1. *Platform*: *Dashboard* dikembangkan menggunakan *Looker Studio* (*Google Data Studio*) sebagai *platform Business Intelligence*. 



2. Jumlah Halaman: *Dashboard* terdiri dari 7 halaman utama yang mencakup *Executive Summary*, *Sales Analysis*, *Product Performance*, *Customer Analysis*, *Operational Metrics*, *Financial Analysis*, dan *Marketing Performance*. 

3. *Interaktivitas*: Fitur interaktif mencakup date *filter*, *category filter*, *channel filter*, dan *cross-filtering* antar *visualisasi*. 

4. *Visualisasi*: Jenis *visualisasi* yang digunakan meliputi *scorecard*, *bar chart*, *line chart*, *pie chart*, *combo chart*, *table*, dan *geo map*. 

5. *Real-Time Update* : *Dashboard* tidak terintegrasi dengan sistem *real-time*, pembaruan data dilakukan secara manual melalui upload ke *Google Sheets*. 

### 1.5.3. Batasan Analisis

1. Fokus Analisis: Analisis difokuskan pada aspek *sales*, *product*, *customer*, *operational*, *financial*, dan *marketing*. 

2. Metode Analisis : Analisis menggunakan metode *descriptive* dan *exploratory*, tidak mencakup *predictive analytics* atau *machine learning*. 

3. *Customer Segmentation* : Segmentasi pelanggan dilakukan berdasarkan RFM ( *Recency, Frequency, Monetary*) dan karakteristik demografis dasar. 

4. *Profitability Analysis* : Analisis *profitabilitas* dihitung berdasarkan selisih harga jual dan *cost,* belum mencakup alokasi *overhead cost* secara detail. 

### 1.5.4. Batasan Implementasi

1. *User*: *Dashboard* dirancang untuk digunakan oleh manajemen dan tim operasional SATRIAMART, tidak mencakup akses untuk *customer eksternal*. 

2. *Data Security*: Implementasi menggunakan sharing link dengan *restricted access*, tidak mencakup sistem *authentication* dan *authorization* yang kompleks. 

3. *Scalability*: *Dashboard* dirancang untuk volume data skala kecil hingga menengah, belum dioptimasi untuk volume data *enterprise-level*. 

4. *System Integration*: *Dashboard* tidak terintegrasi dengan sistem *Enterprise Resource Planning* (ERP), *Customer Relationship Management* (CRM), atau *sistem enterprise* lainnya, data dikelola secara terpisah di *Google Sheets*. 





# BAB II

# LANDASAN TEORI

## 2.1. Konsep Dasar *Business Intelligence*

Pada BAB II ini akan membahas tentang teori yang berkaitan dengan Perancangan Dashboard Bussines Intelligence yang akan dibuat. 

*Business Intelligence* (BI) merupakan istilah umum yang mencakup aplikasi, infrastruktur, perangkat, dan praktik terbaik yang memungkinkan akses dan analisis informasi untuk meningkatkan dan mengoptimalkan keputusan dan kinerja organisasi. (Turban et al., 2021). 



Menurut Davenport (2020), *Business Intelligence* adalah seperangkat teknologi dan proses yang menggunakan data untuk memahami dan menganalisis performa bisnis guna mendorong perencanaan strategis yang lebih baik. 

*“Business Intelligence* sebagai proses pengumpulan data mentah, pengolahan data menjadi informasi, dan transformasi informasi menjadi pengetahuan yang dapat digunakan untuk pengambilan keputusan bisnis.” Antonius (2023) Dalam konteks UMKM, BI berfungsi sebagai alat untuk mengubah data operasional sehari-hari menjadi wawasan yang dapat ditindaklanjuti untuk meningkatkan daya saing bisnis. 

Komponen utama dalam sistem *Business Intelligence* menurut Turban et al. (2021) meliputi : 

1. Data *Warehouse*: Repositori terpusat yang menyimpan data historis dari berbagai sumber untuk keperluan analisis dan pelaporan. 

2. *Business Analytics*: Kumpulan teknik analisis yang digunakan untuk mengeksplorasi data, mengidentifikasi pola, dan membuat prediksi. 

3. Data *Visualization*: Presentasi data dalam bentuk visual seperti grafik, diagram, dan dashboard untuk memudahkan pemahaman dan interpretasi. 

4. *Performance Management*: Sistem untuk memantau dan mengelola kinerja organisasi berdasarkan *Key Performance Indicator* (KPI). 



5. *User Interface*: Antarmuka yang memungkinkan pengguna berinteraksi dengan sistem BI untuk mengakses informasi dan melakukan analisis. 

Menurut Howson (2021), implementasi *Business Intelligence* yang sukses harus memenuhi beberapa prinsip kunci : 

• Relevansi : Informasi yang disajikan harus relevan dengan kebutuhan bisnis dan mendukung pengambilan keputusan strategis. 

• Akurasi: Data harus akurat, konsisten, dan dapat dipercaya sebagai dasar pengambilan keputusan. 

• Ketepatan Waktu: Informasi harus tersedia tepat waktu ketika dibutuhkan untuk pengambilan keputusan. 

• Aksesibilitas: Informasi harus mudah diakses oleh pemangku kepentingan yang berwenang melalui antarmuka yang mudah digunakan. 

• Dapat Ditindaklanjuti: Wawasan yang dihasilkan harus dapat ditindaklanjuti dan memberikan nilai tambah bagi organisasi. 

Dalam konteks perusahaan skala kecil seperti SATRIAMART, implementasi BI dapat membantu dalam beberapa area kritis : 

1. Analisis Penjualan: Memahami kecenderungan penjualan, produk terlaris, dan performa saluran penjualan. 

2. Manajemen Persediaan: Optimasi stok produk berdasarkan peramalan permintaan dan analisis perputaran barang. 

3. Manajemen Hubungan Pelanggan: Memahami karakteristik pelanggan, pola pembelian, dan segmentasi untuk pemasaran yang tertarget. 

4. Analisis Profitabilitas: Evaluasi margin keuntungan per produk, per kategori, dan per saluran untuk optimasi strategi penetapan harga. 

5. Efektivitas Pemasaran: Mengukur ROI kampanye pemasaran dan mengidentifikasi saluran pemasaran yang paling efektif. 



### 2.1.1. *Dashboard* dan *Key Performance Indicator*

*Dashboard* adalah alat visualisasi yang menyajikan informasi penting dan *Key Performance Indicators* (KPI) dalam satu layar untuk memudahkan pemantauan dan analisis kinerja bisnis (Howson, 2021). *Dashboard* yang efektif harus menyajikan informasi yang paling relevan dengan cara yang mudah 



dipahami, memungkinkan pengguna untuk mengidentifikasi masalah dan peluang dengan cepat. 

Menurut Few (2013) dalam Turban et al. (2021), *dashboard* yang baik memiliki karakteristik sebagai berikut: 

1. Sederhana: Menampilkan informasi tanpa kompleksitas yang tidak perlu, fokus pada data yang paling penting. 

2. Komunikatif: Menyampaikan informasi dengan jelas dan mudah dipahami oleh target audiens. 

3. Relevan: Menampilkan informasi yang relevan dengan kebutuhan bisnis dan konteks pengambilan keputusan. 

4. Tepat Waktu: Menyajikan informasi yang terkini dan *real-time* atau mendekati *real-time*. 

5. Dapat Ditindaklanjuti: Memberikan wawasan yang dapat ditindaklanjuti untuk perbaikan kinerja bisnis. 

*Key Performance Indicator* (KPI) adalah metrik kuantitatif yang mencerminkan faktor kesuksesan kritis suatu organisasi (Antonius, 2023). KPI digunakan untuk mengukur pencapaian tujuan strategis dan memberikan indikasi tentang performa bisnis. Karakteristik KPI yang baik mengikuti prinsip SMART: 

• *Specific* : Jelas dan spesifik dalam mengukur aspek tertentu dari bisnis. 

• *Measurable*: Dapat diukur secara kuantitatif dengan data yang tersedia. 

• *Achievable*: Realistis dan dapat dicapai dengan sumber daya yang ada. 

• *Relevant* : Relevan dengan tujuan strategis organisasi. 

• *Time-bound*: Memiliki periode waktu pengukuran yang jelas. 

Dalam konteks SATRIAMART, KPI yang relevan mencakup:

**KPI Penjualan:** 

• Total *Revenue*

• *Growth Rate*

• *Average Order Value* (AOV) 

• *Number of Transactions*

**KPI Produk:** 

• *Best Selling Products*

• *Profit Margin per Product*



• *Inventory Turnover Rate*

• *Stock-out Frequency*

**KPI Pelanggan:** 

• *Customer Acquisition Cost* (CAC) 

• *Customer Lifetime Value* (CLV) 

• *Repeat Purchase Rate*

• *Customer Satisfaction Score*

**KPI Operasional:**

• *Order Fulfillment Time*

• *Order Completion Rate*

• *Cancellation Rate*

**KPI Finansial:** 

• *Gross Profit*

• *Net Profit*

• *Profit Margin*

• *Return on Investment* (ROI) 

**KPI Pemasaran:** 

• *Marketing ROI*

• *Conversion Rate*

• *Cost per Acquisition*

### 2.1.2. Proses ETL (*Extract, Transform, Load*)

ETL merupakan proses fundamental dalam Business Intelligence yang terdiri dari tiga tahap: *Extract* (ekstraksi), *Transform* (transformasi), dan *Load* (pemuatan) data dari sumber ke data *warehouse* atau sistem analitik (Turban et al., 2021). 

**1. *Extract* (Ekstraksi)**

Proses ekstraksi melibatkan pengambilan data dari berbagai sumber seperti database transaksional, *file spreadsheet*, API, atau sistem *eksternal* lainnya. 

Menurut Valentinus (2017), tahap ekstraksi harus memperhatikan: 

• Identifikasi sumber data yang relevan 

• Validasi ketersediaan dan aksesibilitas data 



• Penentuan frekuensi ekstraksi ( *batch* atau *real-time*) 

• Penanganan data yang berubah atau bertambah 

Dalam konteks SATRIAMART, sumber data meliputi: 

• Data transaksi penjualan dari sistem pencatatan manual 

• Data produk dari katalog internal 

• Data pelanggan dari database kontak 

• Data biaya dari pencatatan keuangan 

• Data pemasaran dari platform media sosial 

**2. *Transform* (Transformasi)**

Transformasi adalah proses pembersihan, validasi, dan pengolahan data mentah menjadi format yang sesuai untuk analisis. Proses transformasi mencakup: 

• Data *Cleaning*: Menghapus duplikasi, menangani nilai yang hilang, memperbaiki format data yang tidak konsisten. 

• Data *Validation*: Memastikan data memenuhi kriteria kualitas dan akurasi yang ditetapkan. 

• Data *Integration*: Menggabungkan data dari berbagai sumber dengan konsistensi skema dan format. 

• Data *Aggregation*: Melakukan agregasi data untuk keperluan analisis ringkasan (misalnya total penjualan per bulan). 

• Data *Enrichment*: Menambahkan informasi tambahan atau *field* kalkulasi untuk memperkaya dataset. 

Menurut Antonius (2023), kualitas data sangat menentukan kualitas *insight* yang dihasilkan. Oleh karena itu, proses transformasi harus dilakukan dengan cermat untuk memastikan data yang akurat dan konsisten. 

**3. *Load* (Pemuatan)**

Tahap pemuatan melibatkan pemuatan data yang sudah ditransformasi ke dalam data *warehouse* atau sistem analitik. Metode pemuatan yang umum digunakan: 

• *Full Load*: Memuat seluruh dataset dari awal, biasanya untuk pemuatan awal. 



• *Incremental Load*: Memuat hanya data yang baru atau berubah sejak pemuatan terakhir, lebih efisien untuk data yang besar. 

• *Real-time Load*: Memuat data secara *real-time* atau mendekati *real-time* untuk kebutuhan *monitoring real-time*. 

Dalam implementasi *dashboard* SATRIAMART menggunakan *Looker Studio*, proses ETL dilakukan dengan : 

1. *Extract*: Data diekstrak dari sistem pencatatan internal SATRIAMART dan dikumpulkan dalam format CSV. 

2. *Transform*: Data dibersihkan dan ditransformasi menggunakan *spreadsheet* dan *Python* untuk memastikan konsistensi format, menangani nilai yang hilang, dan membuat *calculated fields*. 

3. *Load*: Data hasil transformasi diupload ke *Google Sheets* sebagai data *source* untuk *Looker Studio*. 



### 2.1.3. *Looker Studio* sebagai Perangkat *Business Intelligence*

*Looker Studio* (sebelumnya *Google Data Studio*) adalah *platform Business Intelligence* berbasis *cloud* yang disediakan oleh *Google* untuk membuat laporan dan *dashboard* interaktif (Google, 2023). *Looker Studio* memungkinkan pengguna untuk menghubungkan berbagai data *source*, melakukan transformasi data, membuat visualisasi, dan *sharing dashboard* dengan *stakeholder*. 

Keunggulan *Looker Studio*:

1. Gratis: *Platform* ini dapat digunakan secara gratis tanpa biaya lisensi, sangat cocok untuk UMKM dengan anggaran terbatas. 

2. Mudah Digunakan: Antarmuka *drag-and-drop* yang intuitif memudahkan pembuatan *dashboard* tanpa memerlukan pemrograman. 

3. Integrasi Data: Mendukung integrasi dengan lebih dari 100 konektor data termasuk *Google Sheets*, *Google Analytics*, *BigQuery*, *MySQL*, *PostgreSQL*, dan layanan *cloud* lainnya. 

4. Kolaborasi: Memungkinkan kolaborasi *real-time* dan berbagi *dashboard* dengan kontrol akses yang dapat diatur. 

5. Interaktif: *Dashboard* yang dibuat memiliki fitur interaktif seperti filter, pemilih rentang tanggal, dan *drill-down*. 



6. Responsif: *Dashboard* secara otomatis responsif dan dapat diakses dari berbagai perangkat. 

7. Dapat Disesuaikan: Mendukung penyesuaian *branding*, warna, *font*, dan *layout* sesuai kebutuhan organisasi. 

Komponen Utama *Looker Studio*:

1. Data *Source*: Koneksi ke sumber data yang akan digunakan dalam *dashboard*. 

2. *Report/Dashboard*: Kanvas untuk membuat dan mengatur visualisasi data. 

3. *Charts*: Berbagai jenis visualisasi seperti *bar chart*, *line chart*, *pie chart*, *table*, *scorecard*, *geo map*, dan lain-lain. 

4. *Controls*: Elemen interaktif seperti pemilih rentang tanggal, *filter dropdown*, *filter checkbox* untuk eksplorasi data. 

5. *Parameters*: Variabel yang dapat digunakan untuk membuat *calculated fields* atau logika kondisional. 

6. *Calculated Fields*: *Field* yang dibuat dari kombinasi atau transformasi *field* yang sudah ada. 

Jenis Visualisasi dalam *Looker Studio*:

1. *Scorecard*: Menampilkan nilai metrik tunggal, cocok untuk KPI utama. 

2. *Time Series Chart*: Grafik garis untuk menampilkan *tren* data sepanjang waktu. 

3. *Bar Chart*: Menampilkan perbandingan nilai antar kategori. 

4. *Pie/Donut Chart*: Menampilkan proporsi atau komposisi dari keseluruhan. 

5. *Table*: Menampilkan data dalam format tabel dengan opsi pengurutan dan paginasi. 

6. *Geo Map*: Visualisasi data berdasarkan lokasi geografis. 

7. *Combo Chart*: Kombinasi grafik garis dan *bar chart* untuk membandingkan metrik dengan skala berbeda. 

8. *Bullet Chart*: Menampilkan nilai aktual versus target. 

9. *Scatter Plot*: Menampilkan hubungan antara dua variabel numerik. 





Pemilihan *Looker Studio* untuk implementasi *dashboard* SATRIAMART didasarkan pada beberapa pertimbangan : 

• Tanpa Biaya: Tidak ada biaya lisensi sehingga berkelanjutan untuk UMKM. 

• Berbasis *Cloud*: Tidak memerlukan infrastruktur *server* sendiri. 

• Integrasi Mudah: Integrasi mudah dengan *Google Sheets* sebagai sumber data. 

• Kolaboratif: Memudahkan berbagi dan kolaborasi dengan tim. 

• Mudah Dipelajari: *Relatif* mudah dipelajari dibandingkan perangkat *enterprise* seperti *Tableau* atau *Power BI*. 



## 2.2. Data dan Sumber Data

### 2.2.1. Jenis Data

Data yang digunakan dalam penelitian ini mencakup berbagai aspek bisnis SATRIAMART selama periode 12 bulan (Januari 2025 - Desember 2025). Jenis data yang dikumpulkan meliputi: 

**1. Data Master Produk**

Data produk mencakup informasi lengkap tentang produk yang dijual oleh SATRIAMART, termasuk ID produk, nama produk, kategori (Nomor Rumah, *Signage*, Papan Nama, Aksesoris Dekorasi), *sub*-kategori, ukuran, warna, harga jual, harga modal, stok tersedia, material, *finishing*, berat, deskripsi, status, dan tanggal dibuat/ *update*. 

Total produk yang dianalisis sebanyak 50 produk dengan distribusi sebagai berikut:

**Tabel 2.1** Distribusi Produk Berdasarkan Kategori

| **Kategori** | **Jumlah Produk** | **Persentase** |
|--------------|-------------------|----------------|
| Nomor Rumah Akrilik | 15 | 30% |
| Signage Akrilik | 10 | 20% |
| Papan Nama Akrilik | 10 | 20% |
| Aksesoris Dekorasi | 15 | 30% |
| **Total** | **50** | **100%** |

*Sumber: Data Master Produk SATRIAMART, 2025* 

**2. Data Transaksi Penjualan**

Data transaksi penjualan mencatat setiap transaksi yang terjadi, meliputi ID transaksi, tanggal dan waktu transaksi, ID pelanggan, ID produk, jumlah item, harga satuan, subtotal, diskon, biaya khusus, biaya ongkir, total pembayaran, metode pembayaran, status pembayaran, status pesanan, saluran penjualan, catatan pesanan, waktu pengerjaan, rating pelanggan, dan tanggal selesai. 

Total transaksi yang dianalisis sebanyak 320 transaksi selama 12 bulan dengan total pendapatan Rp 111.976.550. 

**3. Data Master Pelanggan**

Data pelanggan mencakup informasi demografis dan perilaku dari pelanggan SATRIAMART, meliputi ID pelanggan, nama lengkap, nomor telepon, *email*, alamat lengkap, kota, provinsi, kode pos, jenis pelanggan (Individu/Bisnis/ *Reseller*), segmen (Retail/UMKM/Korporat), tanggal registrasi, total transaksi, total nilai pembelian, status, dan sumber awal pelanggan. 

Total pelanggan yang tercatat sebanyak 180 pelanggan dengan distribusi sebagai berikut:

**Tabel 2.2** Distribusi Pelanggan Berdasarkan Segmen

| **Segmen Pelanggan** | **Jumlah** | **Persentase** |
|----------------------|------------|----------------|
| Individu/Retail | 108 | 60% |
| Bisnis/UMKM | 54 | 30% |
| Reseller/Korporat | 18 | 10% |
| **Total** | **180** | **100%** |

*Sumber: Data Master Pelanggan SATRIAMART, 2025* 

**4. Data Riwayat Stok**

Data riwayat stok mencatat pergerakan stok produk setiap bulan, meliputi ID stok, tanggal, ID produk, stok awal, stok masuk (pembelian/produksi), stok keluar (penjualan), stok akhir, jenis transaksi, dan keterangan. 

**5. Data Biaya Operasional**

Data biaya operasional mencatat pengeluaran bisnis, meliputi ID biaya, tanggal, kategori biaya (Bahan Baku, Pemasaran, Operasional, Transportasi, Utilitas), sub-kategori, nominal, keterangan, dan metode pembayaran. 

**6. Data Kampanye Pemasaran**

Data kampanye pemasaran mencatat aktivitas pemasaran, meliputi ID kampanye, nama kampanye, *platform* (I *nstagram, Facebook, Google Ads,* *TikTok*), tanggal mulai, tanggal selesai, anggaran, jangkauan, keterlibatan, konversi, pendapatan yang dihasilkan, dan ROI. 

### 2.2.2. Sumber Data

Sumber data dalam penelitian ini berasal dari sistem pencatatan internal SATRIAMART yang telah disimulasikan dan diolah untuk keperluan pembelajaran dan analisis *Business Intelligence*. Data bersifat representatif dan mengikuti pola bisnis yang realistis untuk UMKM di bidang dekorasi dan aksesoris. 

Sumber data spesifik meliputi : 



1. Sistem Pencatatan Penjualan: Data transaksi penjualan dicatat dari nota penjualan, faktur, dan riwayat pesanan dari berbagai saluran (*WhatsApp*, *Instagram*, *Marketplace*, Penjualan Langsung). 

2. *Database* Produk: Informasi produk dikelola dalam katalog digital yang mencakup spesifikasi lengkap setiap produk. 

3. *Database* Pelanggan: Data pelanggan dikumpulkan dari formulir pemesanan, kontak *WhatsApp*/*Instagram*, dan riwayat transaksi. 

4. Pencatatan Keuangan: Data biaya operasional berasal dari pencatatan pengeluaran bulanan yang dikelola oleh bagian keuangan. 

5. Laporan Pemasaran: Data kampanye pemasaran diperoleh dari platform analitik media sosial (*Instagram Insights*, *Facebook Ads Manager*, *Google Analytics*). 

Data yang telah dikumpulkan kemudian diolah dan disimpan dalam format CSV untuk memudahkan proses ETL (*Extract, Transform, Load*) dan integrasi dengan *Looker Studio* melalui *Google Sheets*.

**Proses ETL (*Extract, Transform, Load*)**

Proses ETL merupakan tahapan fundamental dalam implementasi *Business Intelligence* yang terdiri dari tiga fase utama sebagaimana digambarkan pada Gambar 2.1:

1. **Extract (Ekstraksi)**: Data mentah diekstrak dari berbagai sumber pencatatan internal SATRIAMART dan dikumpulkan dalam format CSV. Data mentah ini masih mengandung berbagai masalah kualitas data seperti *missing values*, format tidak konsisten, dan duplikasi.

2. **Transform (Transformasi)**: Data mentah dibersihkan dan ditransformasi menggunakan kombinasi *Microsoft Excel* dan *Google Sheets* untuk memastikan konsistensi format, menangani nilai yang hilang, standarisasi kapitalisasi, dan membuat *calculated fields*. Proses transformasi menghasilkan data bersih yang siap untuk analisis.

3. **Load (Pemuatan)**: Data hasil transformasi di-*upload* ke *Google Sheets* sebagai *data source* untuk *Looker Studio*. *Google Sheets* berfungsi sebagai *data warehouse* yang menyediakan koneksi *real-time* dengan *dashboard*.

*[Gambar 2.1 Proses ETL (Extract, Transform, Load) akan ditampilkan di sini]*

Arsitektur lengkap sistem *Business Intelligence* SATRIAMART dapat dilihat pada Gambar 2.2.

*[Gambar 2.2 Arsitektur Dashboard Business Intelligence akan ditampilkan di sini]* 

## 2.2.3. Kualitas Data dan Proses Pembersihan

Kualitas data merupakan faktor kritis yang menentukan keakuratan analisis dan keandalan *dashboard Business Intelligence*. Analisis awal terhadap data mentah menunjukkan bahwa dari 158 baris data yang dikumpulkan, terdapat 38 masalah kualitas data (24%) yang harus ditangani sebelum data dapat digunakan untuk analisis.

**Masalah Kualitas Data yang Ditemukan:**

Masalah kualitas data yang teridentifikasi meliputi: *missing values* (53%), format tidak konsisten (39%), inkonsistensi kapitalisasi (32%), data tidak realistis (11%), dan duplikasi data (3%). Masalah-masalah ini tersebar di seluruh dataset dengan tingkat keparahan yang bervariasi, sebagaimana ditunjukkan pada Tabel 2.3.

**Tabel 2.3** Distribusi Masalah Kualitas Data per File

| **File** | **Total Baris** | **Jumlah Masalah** | **Persentase Masalah** |
|----------|-----------------|-------------------|------------------------|
| Master Produk | 20 | 8 | 40% |
| Master Pelanggan | 20 | 7 | 35% |
| Transaksi Penjualan | 20 | 3 | 15% |
| Riwayat Stok | 40 | 4 | 10% |
| Biaya Operasional | 30 | 6 | 20% |
| Marketing Campaign | 28 | 10 | 36% |
| **Total** | **158** | **38** | **24%** |

*Sumber: Analisis Data Mentah SATRIAMART, 2025*

Dari Tabel 2.3 dapat dilihat bahwa file Master Produk memiliki persentase masalah tertinggi (40%) dan file Riwayat Stok memiliki persentase masalah terendah (10%).

*[Gambar 2.3 Contoh Data Mentah dengan Masalah Kualitas Data akan ditampilkan di sini]*

**Metode Pembersihan Data:**

Proses pembersihan data dilakukan secara sistematis menggunakan pendekatan *data quality management* yang mencakup enam tahapan utama:

1. **Penanganan *Missing Values***: Nilai kosong ditangani dengan strategi yang disesuaikan dengan konteks bisnis. Untuk kolom numerik, nilai kosong diisi dengan nilai 0 atau rata-rata kategori. Untuk kolom kategorikal, nilai kosong diisi dengan nilai default atau placeholder yang sesuai.

2. **Penghapusan Duplikasi**: Identifikasi dan penghapusan data duplikat dilakukan berdasarkan *primary key* untuk memastikan setiap record memiliki pengenal unik.

3. **Standarisasi Format**: Semua format data distandarisasi, terutama format tanggal ke ISO 8601 (YYYY-MM-DD), format nama ke *Title Case*, dan format status ke *Proper Case*.

4. **Validasi Tipe Data**: Konversi dan validasi tipe data dilakukan untuk memastikan kolom numerik berisi angka, kolom tanggal berisi format tanggal yang valid, dan kolom teks berisi string yang konsisten.

5. **Deteksi dan Koreksi Anomali**: Nilai-nilai yang tidak realistis atau ekstrim diidentifikasi dan divalidasi terhadap logika bisnis, kemudian dikoreksi atau dihapus sesuai kebutuhan.

6. **Validasi Konsistensi**: Pemeriksaan konsistensi matematis dilakukan untuk memastikan perhitungan seperti total pembayaran, stok akhir, dan profit margin sesuai dengan formula bisnis yang benar.

**Hasil Pembersihan:**

Setelah proses pembersihan, kualitas data meningkat signifikan sebagaimana ditunjukkan pada Tabel 2.4.

**Tabel 2.4** Perbandingan Kualitas Data Sebelum dan Sesudah Pembersihan

| **Metrik Kualitas** | **Sebelum Pembersihan** | **Sesudah Pembersihan** |
|---------------------|-------------------------|-------------------------|
| Data Completeness | 87% | 100% |
| Format Consistency | 90% | 100% |
| Duplicate Records | 1 record | 0 record |
| Data Accuracy | 96% | 100% |
| Ready for Analysis | Tidak | Ya |

*Sumber: Hasil Proses ETL, 2025*

Dari Tabel 2.4 terlihat peningkatan signifikan pada semua metrik kualitas data. Data bersih kemudian disimpan dalam folder terpisah dan siap digunakan sebagai sumber data untuk *dashboard*.

*[Gambar 2.4 Contoh Data Bersih Setelah Proses Cleaning akan ditampilkan di sini]* 

### 2.2.4. *Transformasi* Data 

Setelah data dibersihkan, dilakukan transformasi untuk memperkaya dataset dan memudahkan analisis. Proses transformasi yang dilakukan meliputi : 

**1. *Calculated Fields***

Membuat kolom baru hasil perhitungan : 

• Profit = Harga Jual - Harga Modal 

• Profit Margin = (Profit / Harga Jual) × 100% 

• Jumlah Diskon = Subtotal × Persentase Diskon / 100 

• Pendapatan Bersih = Total Pembayaran - Harga Pokok Penjualan 

• Nilai Rata-rata Pesanan = Total Pendapatan / Jumlah Transaksi

**2. Dimensi Tanggal**

Ekstraksi komponen tanggal untuk analisis *temporal* : 



• Tahun, Bulan, Kuartal dari tanggal transaksi 

• Hari dalam Minggu (Senin-Minggu) 

• Minggu dalam Tahun 

• Akhir Pekan (Ya/Tidak) 

• Nama Bulan (Januari-Desember) 

**3. Pengelompokan Kategori**

Membuat kategori baru untuk analisis segmentasi : 

• Rentang Harga : Rendah (< 100K), Menengah (100-300K), Tinggi (> 300K) 

• Segmen Nilai Pelanggan : Rendah, Menengah, Tinggi berdasarkan total pembelian 

• Ukuran Pesanan : Kecil (1 item), Menengah (2-3 items), Besar (> 3 

items) 

• Wilayah Geografis : Depok, Jakarta, Tangerang-Bekasi, Lainnya 

**4. *Agregasi* Data**

Membuat ringkasan data untuk *dashboard*: 

• Total Pendapatan per Bulan 

• Total Transaksi per Kategori Produk 

• Rata-rata Rating per Produk 

• Total Pelanggan per Kota 

• Total Anggaran Kampanye per *Platform* 

**5. Penggabungan Tabel**

Menggabungkan data dari beberapa tabel : 

• Gabungkan Transaksi dengan *Master* Produk untuk mendapatkan kategori dan harga modal 

• Gabungkan Transaksi dengan *Master* Pelanggan untuk mendapatkan informasi demografis 

• Gabungkan Transaksi dengan Riwayat Stok untuk analisis perputaran persediaan 

**6. Pengayaan Data**

Menambahkan informasi tambahan: 

• *Customer Lifetime Value* (CLV) = Total Nilai Pembelian Pelanggan 



• *Recency* = Jumlah hari sejak transaksi terakhir 

• *Frequency* = Jumlah transaksi pelanggan 

• *Monetary* = Total pengeluaran pelanggan 

• Skor RFM untuk segmentasi pelanggan 



## 2.3. Metode Perancangan

### 2.3.1. Analisis Kebutuhan Pengguna

Tahap awal dalam perancangan *dashboard* adalah memahami kebutuhan pengguna. Analisis kebutuhan dilakukan melalui diskusi dengan pemangku kepentingan SATRIAMART untuk mengidentifikasi: 

**1. Profil Pengguna**

Identifikasi tiga kelompok pengguna utama: 

• Pemilik/Manajemen Puncak: Membutuhkan gambaran tingkat tinggi, ringkasan KPI, dan wawasan strategis 

• Manajer Pemasaran: Membutuhkan analisis kampanye, segmentasi pelanggan, dan kinerja saluran 

• Manajer Operasional: Membutuhkan analisis persediaan, metrik penyelesaian, dan efisiensi operasional 

**2. Kebutuhan Informasi**

Untuk setiap profil pengguna, diidentifikasi informasi yang dibutuhkan : 

• Metrik apa yang paling penting untuk dipantau? 

• Visualisasi apa yang paling efektif untuk menyajikan informasi? 

• Seberapa detail tingkat informasi yang dibutuhkan? 

• Seberapa sering informasi perlu diperbarui? 

**3. Kebutuhan Dukungan Keputusan**

Identifikasi keputusan bisnis yang perlu didukung oleh *dashboard* : 

• Produk mana yang harus diprioritaskan untuk produksi? 

• Saluran pemasaran mana yang paling efektif?

• Segmen pelanggan mana yang paling menguntungkan? 

• Kapan waktu terbaik untuk promosi? 

**4. Batasan dan Keterbatasan**

Identifikasi batasan dalam implementasi : 

• Anggaran : Menggunakan *tools* gratis ( *Looker Studio*, *Google Sheets*) 

• Keterampilan Teknis : Pengguna memiliki keterampilan komputer dasar, tidak familiar dengan tools tingkat lanjut 

• Ketersediaan Data : Data tersedia dalam *format spreadsheet* 

• Frekuensi Pembaruan : Pembaruan manual, tidak *real-time* 

### 2.3.2. Identifikasi Key Performance Indicators (KPI)

Berdasarkan analisis kebutuhan, diidentifikasi KPI yang relevan untuk setiap area bisnis : 

**KPI Penjualan:** 

• Total *Revenue*: Total pendapatan dari seluruh transaksi 

• *Number of Transactions* : Jumlah transaksi yang terjadi 

• *Average Order Value* (AOV) : Rata-rata nilai per transaksi 

• *Growth Rate* : Tingkat pertumbuhan pendapatan bulan ke bulan 

• *Sales by Channel* : Pendapatan dari setiap saluran penjualan 

• *Sales by Product Category* : Pendapatan dari setiap kategori produk 

**KPI Produk:**

• *Top 10 Best Selling Products* : Produk dengan jumlah penjualan tertinggi 

• *Revenue per Product* : Pendapatan yang dihasilkan setiap produk 

• *Profit Margin* per *Product* : Margin keuntungan setiap produk 

• *Inventory Turnover Rate* : Kecepatan perputaran persediaan 

• *Stock-out Frequency* : Frekuensi kehabisan stok 

**KPI Pelanggan:** 

• Total *Customers* : Jumlah total pelanggan 

• *New Customers* : Jumlah pelanggan baru per periode 

• *Repeat Customer Rate* : *Persentase* pelanggan yang melakukan pembelian ulang 

• *Customer Lifetime Value* (CLV) : Nilai total pembelian pelanggan 

• *Customer Satisfaction Score* : Rata-rata rating dari pelanggan

**KPI Operasional:** 

• *Order Fulfillment Time* : Rata-rata waktu penyelesaian pesanan 

• *Order Completion Rate* : Persentase pesanan yang selesai 

• *Cancellation Rate* : Persentase pesanan yang dibatalkan 


• *On-Time Delivery Rate* : Persentase pesanan yang selesai tepat waktu 

**KPI Finansial:**

• *Gross Revenue* : Total pendapatan kotor 

• *Total Costs* : Total biaya operasional 

• *Net Profit* : Laba bersih 

• *Profit Margin* : Persentase margin keuntungan 

• *Cost per Transaction* : Biaya rata-rata per transaksi 

**KPI Pemasaran:** 

• Marketing ROI : Return on investment dari kampanye pemasaran 

• *Conversion Rate by Channel*: Tingkat konversi setiap saluran 

• *Cost per Acquisition* (CPA) : Biaya untuk memperoleh satu pelanggan baru 

• *Campaign Reach* : Jangkauan kampanye pemasaran 

• *Engagement Rate* : Tingkat keterlibatan di media sosial 

Untuk memberikan gambaran yang lebih jelas, KPI-KPI utama yang diimplementasikan dalam setiap halaman dashboard dirangkum dalam Tabel 2.5 berikut:

**Tabel 2.5** Key Performance Indicators (KPI) per Dashboard

| **Halaman Dashboard** | **KPI 1** | **KPI 2** | **KPI 3** | **KPI 4** |
|----------------------|-----------|-----------|-----------|-----------|
| Executive Summary | Total Revenue | Total Transactions | Avg Order Value | Total Customers |
| Sales Analysis | Gross Sales | Net Sales | Total Discounts | Shipping Revenue |
| Product Performance | Total Products | Inventory Value | Avg Profit Margin | Low Stock Items |
| Customer Analysis | Total Customers | Avg Customer Value | Repeat Customer Rate | Avg Rating |
| Financial Analysis | Total Revenue | Total Costs (COGS) | Gross Profit | Net Profit Margin |
| Operations & Inventory | Total Stock In | Total Stock Out | Stock Turnover Rate | Net Stock Change |
| Marketing Performance | Total Campaigns | Total Budget | Average ROI | Total Reach |

*Sumber: Analisis Kebutuhan Pengguna, 2025*

Tabel 2.5 menunjukkan bahwa setiap halaman dashboard memiliki 4 KPI utama yang relevan dengan tujuan analisis masing-masing halaman, memberikan fokus yang jelas untuk pemantauan kinerja bisnis.

### 2.3.3. Persiapan Data (ETL)

Proses ETL untuk dashboard SATRIAMART dilakukan dengan langkah-langkah berikut : 

**1. *Extract* (Ekstraksi)**

• Kumpulkan data mentah dari berbagai sumber (catatan penjualan, persediaan, keuangan) 

• Ekspor data ke format CSV 

• Validasi kelengkapan data 

**2. *Transform* (Transformasi)**

• Pembersihan data : hapus duplikasi, tangani nilai kosong, perbaiki inkonsistensi format 

• Transformasi data : buat *calculated fields*, ekstrak dimensi tanggal, kategorisasi 

• Pengayaan data : tambahkan metrik turunan (profit, margin, skor RFM) 

• Agregasi data : buat tabel ringkasan untuk optimasi kinerja 

**3. *Load* (Pemuatan)**

• Unggah file CSV ke *Google Sheets*

• Buat sheet terpisah untuk setiap tabel ( *master* \_ *product*, *master* \_ *custome* r, *sales* \_ *transactions*, dll) 

• Terapkan konvensi penamaan dan struktur yang tepat 

• Validasi integritas data setelah pengunggahan 

**4. Pengaturan *Data Source* di *Looker Studio***

• Hubungkan *Looker Studio* ke *Google Sheets* 

• Atur data *sources* untuk setiap *sheet* 

• Konfigurasi tipe kolom (tanggal, angka, teks) 

• Buat *blended* data *sources* untuk menggabungkan beberapa tabel 

### 2.3.4. Perancangan *Layout Dashboard*

*Layout dashboard* dirancang mengikuti prinsip-prinsip hierarki visual dan praktik terbaik desain *dashboard* : 

**1. Struktur *Dashboard***

*Dashboard* terdiri dari 7 halaman : 

• Halaman 1 : SATRIAMART Business Intelligence Dashboard (Executive Dashboard)

• Halaman 2 : Sales Analysis

• Halaman 3 : Product Performance

• Halaman 4 : Customer Analysis

• Halaman 5 : Financial Analysis

• Halaman 6 : Operations & Inventory Management

• Halaman 7 : Marketing Performance 

**2. *Hierarki* Visual**

Setiap halaman mengikuti struktur : 

• *Header* : Logo, judul *dashboard*, kontrol *filter*

• *Kartu KPI*: 4-6 *scorecard* menampilkan metrik kunci di bagian atas 

• *Visualisasi Utama*: 2-3 grafik utama yang menjawab pertanyaan bisnis paling penting 

• *Visualisasi Pendukung*: Grafik detail dan informasi pendukung 

• *Footer*: Waktu pembaruan terakhir, informasi sumber data 

**3. Skema Warna**

Pemilihan warna konsisten dengan identitas brand SATRIAMART: 

• **Primer**: \#a02d33 (Merah SATRIAMART) untuk header, KPI cards utama, dan elemen penting

• **Sekunder**: \#ee5d26 (Orange SATRIAMART) untuk aksen, highlight, dan elemen pendukung

• **Netral**: \#FFFFFF (Putih) untuk background cards dan area konten

• **Background**: \#F5F5F5 (Abu-abu Muda) untuk background halaman

• **Text**: \#212121 (Abu-abu Gelap) untuk teks utama yang mudah dibaca

• **Success**: \#22C55E (Hijau) untuk indikator positif dan pertumbuhan

• **Warning**: \#FB923C (Orange) untuk peringatan dan perhatian 

**4. Tipografi**

• Judul : *Roboto Bold*, 18-24pt untuk judul bagian 

• Isi : *Roboto Regular*, 10-12pt untuk label dan teks 

• Angka/Metrik : *Roboto Medium*, 14-16pt untuk angka KPI 

• *Font family* konsisten di semua halaman 

**5. Jarak & Tata Letak** 

• Sistem grid konsisten dengan layout 12-kolom 

• Padding : 8px/16px/24px untuk konsistensi 

• Margin : 24px pada tepi dashboard 

• Jarak kartu : 16px antar visualisasi 

• Kelompokkan visualisasi terkait dengan warna latar belakang 

### 2.3.5. *Implementasi* di *Looker Studio*

*Implementasi dashboard* dilakukan dengan langkah-langkah sistematis sebagaimana ditampilkan pada Gambar 4.1.

*[Gambar 4.1 Alur Implementasi Dashboard di Looker Studio akan ditampilkan di sini]*

Langkah-langkah implementasi adalah sebagai berikut : 

**1. Pengaturan *Data Source***

• Buat *data sources* untuk setiap tabel *Google Sheets* 

• Konfigurasi properti kolom (tipe, agregasi) 

• Buat *calculated fields* untuk metrik turunan 

• Atur data *blending* untuk menggabungkan tabel 

**2. Pembuatan Halaman *Dashboard***

• Buat 7 halaman sesuai struktur yang dirancang 

• Atur navigasi halaman dengan menu *dropdown* atau *tabs* 

• Konfigurasi filter tingkat halaman 

**3. Penambahan Visualisasi**

• Tambahkan *scorecard* untuk metrik KPI 

• Buat *time series charts* untuk analisis tren 

• Buat *bar charts* untuk perbandingan kategorikal 

• Buat *pie charts* untuk analisis komposisi 

• Buat tabel untuk data detail 

• Buat *geo maps* untuk analisis geografis 

**4. Kontrol Interaktif**

Fitur interaktif yang diimplementasikan untuk meningkatkan eksplorasi data sebagaimana ditampilkan pada Gambar 3.8.

*[Gambar 3.8 Fitur Interaktif Dashboard akan ditampilkan di sini]*

• Pemilih rentang tanggal untuk *filter* periode 

• *Filter dropdown* untuk kategori, saluran, status 

• *Filter checkbox* untuk pemilihan ganda 

• Konfigurasi cakupan *filter* (tingkat halaman atau laporan) 

**5. *Styling* & *Formatting***

• Terapkan skema warna yang konsisten 

• Atur gaya dan ukuran *font* 

• Tambahkan border dan shadow untuk kedalaman visual 

• Konfigurasi *format* angka (mata uang, *persentase*) 

• Tambahkan *tooltips* untuk konteks tambahan 

**6. Pengujian**

• Uji interaktivitas ( *filter*, *drill-down*) 

• Uji akurasi data 

• Uji kinerja (waktu loading) 

• Uji desain responsif pada berbagai perangkat 

• *User Acceptance Testing* (UAT) dengan pemangku kepentingan 

### 2.3.6. Pengujian dan Evaluasi

Tahap pengujian dan evaluasi dilakukan untuk memastikan dashboard memenuhi kebutuhan dan berfungsi dengan baik : 

**1. Pengujian Fungsional**

Pengujian fungsional mencakup validasi fitur interaktif sebagaimana ditampilkan pada Gambar 3.9.

*[Gambar 3.9 Pengujian Fitur Drill-Down dan Cross-Filtering akan ditampilkan di sini]*

• Validasi akurasi data dan perhitungan 

• Uji semua kontrol interaktif ( *filter*, pemilih tanggal) 

• Verifikasi *cross-filtering* antar visualisasi 

• Uji fungsi *drill-down* 

• Validasi *mekanisme refresh* data 

**2. Pengujian Kinerja**

• Ukur waktu *loading* untuk setiap halaman 

• Uji dengan volume data yang berbeda 

• Optimalkan *query* yang lambat 

• Uji pengguna konkuren (beberapa pengguna mengakses bersamaan) 

**3. Pengujian Kegunaan**

• Uji dengan pengguna sebenarnya (pemangku kepentingan SATRIAMART) 

• Amati perilaku pengguna dan titik kesulitan 

• Kumpulkan *feedback* tentang kemudahan penggunaan 

• Identifikasi area untuk perbaikan 

• Iterasi desain berdasarkan *feedback*

**4. Pengujian Kompatibilitas**

• Uji pada berbagai *browser (Chrome, Firefox, Safari, Edge)* 

• Uji pada berbagai perangkat *(desktop, tablet, mobile)* 

• Uji pada *resolusi* layar yang berbeda 

• Verifikasi desain *responsif* 

**5. Validasi Kualitas Data**

• *Cross-check* metrik dengan data sumber 

• Validasi *calculated fields* dengan perhitungan manual 

• Verifikasi agregasi dan *filter* 

• Periksa anomali data 

**6. Evaluasi Nilai Bisnis**

• Evaluasi apakah *dashboard* menjawab pertanyaan bisnis 

• Nilai kemampuan tindak lanjut dari wawasan yang dihasilkan 

• Ukur waktu yang dihemat dibandingkan analisis manual 

• Kumpulkan *feedback* kepuasan pemangku kepentingan Hasil evaluasi digunakan untuk perbaikan *iteratif dashboard* hingga mencapai tingkat kepuasan optimal dari pengguna. 





# BAB III

# PEMBAHASAN

## 3.1. Proses Analisa Data

## 3.1.1. Analisis Data Transaksi Penjualan

Analisis data transaksi penjualan SATRIAMART dilakukan terhadap 320 

transaksi selama periode 12 bulan (Januari 2025 - Desember 2025). Data transaksi mencakup informasi lengkap mengenai produk yang dibeli, pelanggan, jumlah pembelian, harga, diskon, biaya tambahan, dan status pesanan. 

Temuan Utama dari Analisis Transaksi:

1. Total Pendapatan: Pendapatan total yang dihasilkan selama periode 12 bulan mencapai Rp 111.976.550 dengan rata-rata pendapatan bulanan sebesar Rp 9.331.379. 

2. Nilai Rata-rata Pesanan : Nilai rata-rata per transaksi adalah Rp 349.926, menunjukkan bahwa SATRIAMART berhasil menjual produk dengan nilai transaksi yang cukup tinggi. 

3. Distribusi Bulanan: Terdapat variasi signifikan dalam jumlah transaksi per bulan. Bulan dengan transaksi tertinggi adalah Desember 2025 (38 transaksi), Juni 2025 (36 transaksi), dan Juli 2025 (35 transaksi). Sementara bulan dengan transaksi terendah adalah Februari 2025 (17 transaksi) dan September 2025 (16 transaksi). 

4. Identifikasi Musim Puncak: Analisis menunjukkan bahwa SATRIAMART mengalami musim puncak pada : 

• Desember: Didorong oleh periode liburan Natal dan Tahun Baru 

• Juni-Juli : Didorong oleh periode libur sekolah dan Hari Raya Idul Fitri 

• Januari : Efek pasca-liburan dan awal tahun 

5. Kinerja Saluran: Dari analisis saluran penjualan, ditemukan bahwa: 

• *WhatsApp* adalah saluran paling dominan dengan kontribusi 45% dari total transaksi 

• *Instagram* menyumbang 30% transaksi 

• *Platform* pasar daring (Tokopedia, Shopee) menyumbang 15% 

• Penjualan langsung/rujukan menyumbang 10% 

6. Preferensi Metode Pembayaran : Metode pembayaran yang paling banyak digunakan adalah Transfer Bank (55%), diikuti oleh Dompet Digital (30%), dan Bayar di Tempat (15%). 

7. Tingkat Penyelesaian Pesanan: Dari 320 transaksi, 85% berhasil diselesaikan dan diterima pelanggan, 8% masih dalam proses, dan 7% dibatalkan. Tingkat penyelesaian 85% menunjukkan kinerja operasional yang baik. 

8. Kepuasan Pelanggan: Dari pesanan yang selesai, rata-rata penilaian pelanggan adalah 4,5 dari 5, dengan 85% pelanggan memberikan penilaian 4 atau 5 bintang. 

## 3.1.2. Identifikasi Pola dan Tren

Dari analisis data, berhasil diidentifikasi beberapa pola dan kecenderungan penting : 

**1. Pola Musiman**

Analisis tren menunjukkan pola musiman yang jelas : 

• Kuartal 4 (Okt-Des): Musim puncak dengan peningkatan transaksi menjelang akhir tahun 

• Kuartal 1 (Jan-Mar): Musim tinggi di awal tahun, kemudian menurun di Februari 

• Kuartal 2 (Apr-Jun) : Peningkatan bertahap menuju puncak di Juni 

• Kuartal 3 (Jul-Sep): Stabil di Juli-Agustus, menurun di September Pemahaman pola musiman ini membantu SATRIAMART dalam : 

• Perencanaan persediaan untuk mengantisipasi permintaan puncak 

• Penjadwalan kampanye pemasaran di waktu yang tepat 

• Persiapan kapasitas produksi dan penyelesaian pesanan 

**2. Pola Harian dan Mingguan**

Analisis transaksi berdasarkan hari menunjukkan : 

• Akhir Pekan (Sabtu-Minggu) : 35% dari total transaksi terjadi di akhir pekan 

• Hari Kerja: 65% transaksi terjadi di hari kerja 

• Jam Sibuk: Transaksi paling banyak terjadi pada jam 10:00-14:00 (siang) dan 19:00-21:00 (malam) 

Wawasan ini berguna untuk : 

• Penjadwalan tim layanan pelanggan untuk jam sibuk 

• Waktu optimal untuk mengunggah konten di media sosial 

• Penjadwalan kampanye iklan untuk jangkauan maksimum 

**3. Kinerja Kategori Produk**

Analisis performa per kategori produk menunjukkan : 

• Nomor Rumah Akrilik: Kategori paling populer dengan 35% dari total pendapatan 

• Papan Nama: Kontribusi 28% pendapatan, populer di segmen bisnis 

• Papan Petunjuk: Kontribusi 23% pendapatan, barang bernilai tinggi 

• Aksesoris Dekorasi: Kontribusi 14% pendapatan, volume tinggi tapi bernilai rendah 

**4. Analisis Titik Harga** 

Analisis harga menunjukkan : 

• Produk dengan harga Rp 100.000 - Rp 300.000 paling banyak terjual (40% transaksi) 

• Produk kelas bawah (< Rp 100.000) menghasilkan volume tinggi tapi margin rendah 

• Produk kelas atas (> Rp 300.000) menghasilkan margin tinggi tapi volume rendah 

**5. Pola Perilaku Pelanggan**

Analisis perilaku pelanggan menunjukkan : 

• 55% pelanggan hanya melakukan satu kali pembelian (pembeli sekali) 

• 30% pelanggan melakukan pembelian ulang 2-3 kali 

• 15% pelanggan adalah pelanggan setia dengan 4\+ transaksi Tingkat pembelian ulang yang masih rendah mengindikasikan potensi untuk meningkatkan retensi pelanggan melalui program loyalitas atau pemasaran tindak lanjut. 

**6. Konsentrasi Geografis**

Analisis geografis menunjukkan konsentrasi pelanggan : 

• Depok (lokasi bisnis) : 40% pelanggan 

• Jakarta Selatan : 20% pelanggan 

• Tangerang : 15% pelanggan 

• Bekasi : 10% pelanggan 

• Wilayah lain : 15% pelanggan 

Konsentrasi yang tinggi di Jabodetabek (85%) mengindikasikan penetrasi pasar yang baik di area lokal, namun juga menunjukkan peluang ekspansi ke wilayah lain. 

## 3.1.3. Hubungan Antar Variabel

Analisis korelasi antar variabel mengungkapkan beberapa hubungan yang menarik : 

**1. Harga *vs* Volume Penjualan** 

Analisis menunjukkan korelasi negatif antara harga produk dan volume penjualan sebagaimana ditampilkan pada Tabel 3.1.

**Tabel 3.1** Analisis Harga vs Volume Penjualan

| **Rentang Harga** | **Rata-rata Volume/Bulan** | **Kategori Produk** | **Margin Profit** | **Profitabilitas** |
|-------------------|----------------------------|---------------------|-------------------|--------------------|
| < Rp 100.000 | 8-10 unit | Nomor Rumah Kecil | 35% | Sedang |
| Rp 100.000 - Rp 300.000 | 4-6 unit | Nomor Rumah Premium, Papan Nama | 45% | Tinggi |
| > Rp 300.000 | 1-3 unit | Papan Petunjuk, Custom | 40% | Sedang |

*Sumber: Analisis Data Penjualan, 2025*

Dari Tabel 3.8 terlihat bahwa meskipun produk murah memiliki volume tinggi, produk kelas menengah (Rp 100.000 - Rp 300.000) memberikan keseimbangan terbaik antara volume dan margin keuntungan. 

**2. Segmentasi Pelanggan vs Nilai Rata-rata Pesanan**

Analisis menunjukkan perbedaan signifikan dalam nilai rata-rata pesanan antar segmen pelanggan sebagaimana ditampilkan pada Tabel 3.2.

**Tabel 3.2** Segmentasi Pelanggan vs Nilai Rata-rata Pesanan

| **Segmen Pelanggan** | **Nilai Rata-rata Pesanan** | **Frekuensi Pembelian** | **Produk Favorit** | **Kontribusi Revenue** |
|----------------------|-----------------------------|-------------------------|--------------------|-----------------------|
| Bisnis/UMKM | Rp 485.000 | 2-3x/tahun | Papan Petunjuk, Papan Nama Khusus | 38% |
| Reseller | Rp 420.000 | 4-5x/tahun | Nomor Rumah Premium, Mix Produk | 35% |
| Individu/Ritel | Rp 285.000 | 1-2x/tahun | Nomor Rumah, Aksesoris Kecil | 27% |

*Sumber: Analisis Segmentasi Pelanggan, 2025*

Dari Tabel 3.9 terlihat bahwa pelanggan bisnis memiliki nilai pesanan tertinggi dan berkontribusi paling besar terhadap revenue meskipun frekuensi pembeliannya lebih rendah. 

**3. Saluran vs Tingkat Konversi**

Analisis tingkat konversi per saluran menunjukkan : 

• Rujukan/Langsung: Tingkat konversi tertinggi (60%), faktor kepercayaan tinggi 

• *WhatsApp*: Tingkat konversi 45%, interaksi personal 



• *Instagram*: Tingkat konversi 25%, keterlibatan tinggi tapi konversi moderat 

• *Marketplace*: Tingkat konversi 20%, persaingan tinggi 

**4. Diskon *vs* Nilai Pesanan** 

Analisis menunjukkan : 

• 20% transaksi mendapatkan diskon (5%-20%) 

• Transaksi dengan diskon memiliki nilai pesanan 15% lebih tinggi 

• Diskon efektif untuk mendorong pembelian dalam jumlah lebih besar 

**5. Waktu Penyelesaian *vs* Kepuasan Pelanggan**

Terdapat korelasi positif antara kecepatan penyelesaian dengan penilaian pelanggan sebagaimana ditampilkan pada Tabel 3.3.

**Tabel 3.3** Waktu Penyelesaian vs Kepuasan Pelanggan

| **Waktu Penyelesaian** | **Rata-rata Rating** | **Jumlah Pesanan** | **% Repeat Order** | **Tingkat Kepuasan** |
|------------------------|----------------------|--------------------|--------------------|----------------------|
| 1-3 hari | 4,8 / 5,0 | 145 pesanan | 68% | Sangat Puas |
| 4-5 hari | 4,5 / 5,0 | 125 pesanan | 52% | Puas |
| > 5 hari | 4,0 / 5,0 | 50 pesanan | 35% | Cukup Puas |

*Sumber: Analisis Kepuasan Pelanggan, 2025*

Dari Tabel 3.10 terlihat bahwa penyelesaian cepat (1-3 hari) menghasilkan rating tertinggi dan tingkat repeat order yang jauh lebih baik, menjadikannya faktor krusial dalam kepuasan pelanggan. 

**6. ROI Kampanye Pemasaran *vs Platform*** 

Analisis ROI kampanye menunjukkan performa yang berbeda untuk setiap platform sebagaimana ditampilkan pada Tabel 3.4.

**Tabel 3.4** ROI Kampanye Pemasaran per Platform

| **Platform** | **ROI Rata-rata** | **Total Budget** | **Revenue Generated** | **Cost per Acquisition** | **Efektivitas** |
|--------------|-------------------|------------------|-----------------------|--------------------------|----------------|
| Instagram Ads | 280% | Rp 8.500.000 | Rp 23.800.000 | Rp 125.000 | Sangat Tinggi |
| Facebook Ads | 250% | Rp 7.200.000 | Rp 18.000.000 | Rp 145.000 | Tinggi |
| Google Ads | 180% | Rp 5.800.000 | Rp 10.440.000 | Rp 180.000 | Sedang |
| Konten Organik | 450% | Rp 1.200.000 | Rp 5.400.000 | Rp 45.000 | Sangat Tinggi |

*Sumber: Analisis Marketing Performance, 2025*

Dari Tabel 3.11 terlihat bahwa Instagram Ads memberikan ROI tertinggi untuk iklan berbayar, sementara konten organik memiliki efisiensi biaya terbaik dengan CPA terendah. 

• Iklan *Google*: ROI rata-rata 220%, penargetan spesifik 

• Konten Organik: ROI 350%, hemat biaya tapi jangkauan terbatas 

## 3.2. Visualisasi Data pada *Dashboard Business Intelligence*

### 3.2.1. Tren Penjualan

Untuk menganalisis tren penjualan, digunakan kombinasi visualisasi : 

**1. Grafik Garis : Tren Pendapatan Sepanjang Waktu** 

Grafik garis digunakan untuk menampilkan tren pendapatan bulanan selama 12 bulan. Visualisasi ini memungkinkan identifikasi : 

• Pola pertumbuhan atau penurunan pendapatan 

• Musim puncak dan musim sepi 

• Tingkat pertumbuhan bulan ke bulan 

• Anomali atau nilai ekstrim 



Alasan Pemilihan: Grafik garis efektif untuk menampilkan data *time series* dan memudahkan identifikasi tren serta pola musiman. 

**2. Grafik Gabungan : Pendapatan vs Jumlah Transaksi**

Grafik gabungan (kombinasi batang dan garis) digunakan untuk membandingkan : 

• Total pendapatan (grafik batang) - sumbu kiri 

• Jumlah transaksi (grafik garis) - sumbu kanan 

Wawasan: Visualisasi ini mengungkapkan bahwa peningkatan pendapatan tidak selalu diikuti oleh peningkatan jumlah transaksi, mengindikasikan variasi dalam Nilai Rata-rata Pesanan. 

**3. Peta Panas: Penjualan Berdasarkan Hari dan Jam** 

Peta panas digunakan untuk menampilkan intensitas transaksi berdasarkan: 

• Baris: Hari dalam Minggu (Senin - Minggu) 

• Kolom: Jam dalam Hari (00:00 - 23:00) 

• Intensitas Warna: Jumlah Transaksi 

Wawasan : Peta panas menunjukkan jam sibuk yang jelas (10-14 dan 19-21) dan hari dengan aktivitas tertinggi (Jumat-Sabtu). 

**4. Grafik Batang : Pendapatan Berdasarkan Saluran** 

Grafik batang horizontal menampilkan kontribusi pendapatan dari setiap saluran penjualan, diurutkan dari tertinggi ke terendah. 

Wawasan: *WhatsApp* dan Instagram mendominasi dengan total 75% dari pendapatan, mengindikasikan fokus pemasaran yang tepat. 

### 3.2.2. Performa Produk

Analisis performa produk divisualisasikan melalui : 

**1. Grafik Batang: 10 Produk Teratas Berdasarkan Pendapatan**

Grafik batang horizontal menampilkan 10 produk dengan pendapatan tertinggi. 

Temuan:

• Papan petunjuk LED dan Papan Nama Premium mendominasi 10 teratas 

• 20% produk menghasilkan 60% pendapatan (prinsip Pareto) 

• Produk khusus cenderung masuk pendapatan teratas 





**2. Grafik Batang : 10 Produk Teratas Berdasarkan Jumlah Terjual**

Berbeda dengan pendapatan, grafik ini menampilkan produk dengan volume penjualan tertinggi. 

Temuan:

• Produk berharga rendah seperti Papan Nama Meja dan Bingkai Foto masuk volume teratas 

• Volume tinggi tidak selalu berarti pendapatan tinggi 

**3. Grafik Gelembung: Harga vs Volume Penjualan vs Margin Laba** 

Grafik gelembung multi-dimensi menampilkan : 

• Sumbu-X : Harga 

• Sumbu-Y : Volume Penjualan 

• Ukuran Gelembung : Total Pendapatan 

• Warna Gelembung : Margin Laba 

Wawasan: Grafik ini membantu identifikasi produk optimal dalam hal harga, volume, dan profitabilitas. 

**4. Grafik Batang Bertumpuk : Komposisi Pendapatan Berdasarkan Kategori**
Grafik batang bertumpuk menampilkan komposisi pendapatan dari 4 kategori produk sepanjang waktu. 

Wawasan: Menunjukkan kontribusi konsisten dari Nomor Rumah dan Papan Nama, sementara Papan Petunjuk berfluktuasi (berbasis proyek). 

**5. Tabel : Kartu Skor Kinerja Produk** 

Tabel detail menampilkan metrik untuk setiap produk : 

• Nama Produk 

• Kategori 

• Unit Terjual 

• Total Pendapatan 

• Margin Laba 

• Status Stok 

• Tingkat Pertumbuhan 

Fungsi: Tabel ini digunakan untuk analisis *drill-down* dan referensi detail.



### 3.2.3. Analisis Pelanggan

Analisis pelanggan divisualisasikan dengan : 

**1. Diagram Lingkaran : Segmentasi Pelanggan**

Diagram lingkaran menampilkan proporsi pelanggan berdasarkan : 

• Jenis Pelanggan : Individu (60%), Bisnis (30%), Pemasok Kembali (10%) 

Alasan Pemilihan: Diagram lingkaran efektif untuk menampilkan komposisi dan proporsi dari keseluruhan. 

**2. Grafik Batang: 10 Pelanggan Teratas Berdasarkan Total Nilai Pembelian**

Grafik batang horizontal menampilkan 10 pelanggan dengan total nilai pembelian tertinggi. 

Wawasan: 10% pelanggan teratas menghasilkan 40% pendapatan, mengindikasikan pentingnya retensi pelanggan bernilai tinggi. 

**3. Grafik Garis: Tren Akuisisi Pelanggan**

Grafik garis menampilkan jumlah pelanggan baru yang terakuisisi setiap bulan. 

Wawasan : Akuisisi pelanggan meningkat setelah kampanye pemasaran dan program rujukan. 

**4. Grafik Corong : Segmentasi RFM**

Grafik corong menampilkan distribusi pelanggan berdasarkan skor RFM : 

• *Champions* ( *Recency, Frequency, Monetary* Tinggi): 15% 

• Loyal Customers ( *66LLL6666YT6Y5 * Tinggi): 20% 

• At Risk (Recency Rendah, Frequency, Monetary Tinggi): 10% 

• New Customers (Recency Tinggi, Frequency, Monetary Rendah): 25% 

• Lost Customers (Recency, Frequency, Monetary Rendah): 30% 



Fungsi: Segmentasi RFM membantu pemasaran tertarget dan strategi retensi pelanggan. 

### 3.2.4. Analisis Wilayah

Analisis distribusi geografis pelanggan dan penjualan : 

**Grafik Batang : Pendapatan Berdasarkan Kota** 

Grafik batang horizontal menampilkan kontribusi pendapatan dari setiap kota. 

Ranking:

1. Depok : Rp 44.790.620 (40%) 

2. Jakarta Selatan : Rp 22.395.310 (20%) 

3. Tangerang : Rp 16.796.483 (15%) 

4. Bekasi : Rp 11.197.655 (10%) 

5. Lainnya : Rp 16.796.482 (15%) 

3. Tabel : Metrik Kinerja Geografis 

Tabel menampilkan metrik per kota : 

• Jumlah Pelanggan 

• Jumlah Transaksi 

• Total Pendapatan 

• Nilai Rata-rata Pesanan 

• Tingkat Pertumbuhan 

Wawasan : Depok dan Jakarta memiliki nilai rata-rata pesanan tertinggi, sementara kota lain memiliki ruang untuk pertumbuhan. 





### 3.2.5. Pemilihan Jenis Visualisasi 
Pemilihan jenis visualisasi dilakukan berdasarkan prinsip-prinsip praktik terbaik visualisasi data : 

**1. Kartu Skor/Kartu KPI**

• Digunakan untuk : Menampilkan nilai metrik tunggal (Total Pendapatan, Total Pelanggan, Nilai Rata-rata Pesanan) 

• Keunggulan: Menyoroti metrik penting, mudah dipahami, menarik perhatian 

• Implementasi: Di bagian atas setiap halaman dashboard 

**2. Grafik Garis**

• Digunakan untuk : Data time series, analisis tren 

• Keunggulan : Mudah identifikasi tren, tingkat pertumbuhan, pola musiman 

• Kasus Penggunaan : Tren pendapatan, tren akuisisi pelanggan, tren penjualan 

**3. Grafik Batang (Vertikal/Horizontal)** 

• Digunakan untuk: Perbandingan antar kategori 

• Keunggulan: Mudah membandingkan nilai, peringkat jelas 

• Kasus Penggunaan: Top produk, pendapatan per kategori, penjualan per saluran 

**4. Diagram Lingkaran/Donat** 

• Digunakan untuk: Menampilkan komposisi/proporsi (< 6 kategori) 

• Keunggulan: Representasi visual persentase 

• Kasus Penggunaan: Segmentasi pelanggan, campuran kategori, distribusi metode pembayaran 

**5. Grafik Gabungan (Batang \+ Garis)**

• Digunakan untuk: Membandingkan dua metrik dengan skala berbeda 

• Keunggulan: Menampilkan hubungan antara dua variabel 

• Kasus Penggunaan: Pendapatan *vs* jumlah transaksi, biaya *vs* laba 

**6. Tabel**

• Digunakan untuk: Data terperinci, analisis *drill-down* 

• Keunggulan : Menampilkan beberapa metrik, dapat diurutkan, dapat disaring 

• Kasus Penggunaan: Daftar produk dengan beberapa metrik, detail transaksi 

**7. Peta Geografis**

• Digunakan untuk: Analisis distribusi geografis 

• Keunggulan : Representasi visual data spasial 

• Kasus Penggunaan: Distribusi pelanggan, penjualan per wilayah 

**8. Peta Panas**

• Digunakan untuk: Menampilkan intensitas dalam dua dimensi 

• Keunggulan : Mengidentifikasi pola, periode puncak 

• Kasus Penggunaan: Penjualan per hari/jam, korelasi produk 

**9. Diagram Sebar** 

• Digunakan untuk: Menampilkan hubungan antara dua variabel 

• Keunggulan: Mengidentifikasi korelasi, *outlier*, kelompok 

• Kasus Penggunaan: Harga *vs* volume, nilai pelanggan *vs* frekuensi 

**10. Grafik Corong**

• Digunakan untuk: Menampilkan tahapan dalam proses dengan konversi 

• Keunggulan : Memvisualisasikan titik penurunan 

• Kasus Penggunaan: Corong penjualan, tahapan siklus hidup pelanggan 

### 3.2.6. Prinsip Pemilihan Visualisasi: 

1. Sesuaikan Grafik dengan Tipe Data: Kategorikal → Batang/Lingkaran, Temporal → Garis, Geografis → Peta 

2. Pertimbangkan Audiens: Grafik sederhana untuk eksekutif, grafik detail untuk analis 

3. Batasi Kompleksitas: Maksimal 5-7 kategori per grafik untuk keterbacaan 4. Gunakan Warna dengan Tujuan: Skema warna konsisten, soroti data penting 

5. Berikan Konteks: Tambahkan judul, label, anotasi untuk kejelasan 6. Aktifkan Interaktivitas: *Filter, tooltip, drill-down* untuk eksplorasi 



## 3.3. Hasil Perancangan *Dashboard* Interaktif 
*Dashboard Business Intelligence* SATRIAMART dirancang dengan 7 halaman utama yang saling terintegrasi dan dapat diakses melalui menu navigasi. 

Setiap halaman memiliki fokus analisis yang spesifik untuk mendukung pengambilan keputusan di area berbeda. 



### 3.3.1. SATRIAMART Business Intelligence Dashboard (Executive Dashboard)

Halaman pertama *dashboard* menyajikan gambaran menyeluruh tentang performa bisnis untuk manajemen puncak, sebagaimana ditampilkan pada Gambar 3.1.

*[Gambar 3.1 Executive Dashboard - Overview Bisnis akan ditampilkan di sini]*

Tujuan Halaman : Memberikan gambaran tingkat tinggi tentang performa bisnis secara keseluruhan untuk manajemen puncak. 

Komponen Utama:

**1. Bagian Kepala**

• Logo SATRIAMART 

• Judul : "Dashboard Business Intelligence SATRIAMART" 

• Filter Rentang Tanggal (seluruh periode : Jan 2025 - Des 2025) 

• Pembaruan Terakhir : 6 Desember 2025 

**2. Kartu KPI (4 kartu utama)**

• Total Revenue: Menampilkan total pendapatan dengan indikator persentase perubahan dibanding periode sebelumnya. Warna merah/hijau menunjukkan tren positif atau negatif.

• Total Transactions: Menampilkan jumlah transaksi dengan indikator pertumbuhan. Membantu memantau volume penjualan.

• Avg Order Value: Menampilkan nilai rata-rata per pesanan dengan indikator perubahan. Metrik penting untuk mengukur efektivitas *upselling* dan *cross-selling*.

• Total Customers: Menampilkan jumlah pelanggan unik dengan indikator pertumbuhan basis pelanggan.

*Catatan: Nilai aktual pada dashboard bersifat dinamis dan berubah sesuai filter tanggal yang dipilih pengguna.* 

**3. Visualisasi Utama**

**A. Revenue Trend (Grafik Garis)** 

• Menampilkan tren pendapatan sepanjang periode dengan garis yang menunjukkan fluktuasi bulanan
• Memungkinkan identifikasi pola musiman dan periode puncak penjualan
• Fitur interaktif: Tooltip menampilkan detail pendapatan saat kursor diarahkan ke titik data

**B. Sales by Channel (Diagram Donat)** 

• Menampilkan distribusi penjualan berdasarkan saluran (WhatsApp, Instagram, Marketplace, Offline)
• Menggunakan warna berbeda untuk setiap saluran agar mudah dibedakan
• Menampilkan persentase kontribusi setiap saluran terhadap total penjualan
• Wawasan: Membantu mengidentifikasi saluran penjualan paling efektif

**C. Category Performance (Diagram Donat)** 

• Menampilkan distribusi pendapatan berdasarkan kategori produk (Papan Nama, Signage, Nomor Rumah, Aksesoris Dekorasi)
• Membantu memahami produk mana yang paling berkontribusi terhadap pendapatan
• Wawasan: Berguna untuk strategi *inventory* dan fokus pemasaran 

4. **Visualisasi Pendukung**

A. **Payment Methods (Grafik Batang Horizontal)**

• Menampilkan distribusi metode pembayaran yang digunakan pelanggan
• Membantu memahami preferensi pembayaran untuk optimasi proses checkout

B. **Order Status (Diagram Donat)**

• Menampilkan status pesanan (Diterima vs Selesai)
• Membantu monitoring efisiensi operasional dan *fulfillment rate*

C. **Top 10 Products by Revenue (Tabel)**

• Menampilkan 10 produk dengan pendapatan tertinggi
• Kolom: Nama Produk, Kategori, Revenue, Units Sold, Avg Price
• Membantu identifikasi produk *best-seller* untuk strategi *inventory* dan promosi

Komponen lengkap visualisasi Executive Dashboard dapat dilihat pada Tabel 3.5.

**Tabel 3.5** Komponen Visualisasi Executive Dashboard

| **Komponen** | **Jenis Visualisasi** | **Tujuan** |
|--------------|----------------------|------------|
| Total Revenue | KPI Card | Monitoring pendapatan total |
| Total Transactions | KPI Card | Monitoring volume transaksi |
| Avg Order Value | KPI Card | Monitoring nilai rata-rata pesanan |
| Total Customers | KPI Card | Monitoring basis pelanggan |
| Revenue Trend | Line Chart | Analisis tren pendapatan |
| Sales by Channel | Donut Chart | Distribusi saluran penjualan |
| Category Performance | Donut Chart | Performa kategori produk |
| Payment Methods | Horizontal Bar Chart | Preferensi metode pembayaran |
| Order Status | Donut Chart | Status pesanan |
| Top 10 Products | Table | Produk terlaris |

*Sumber: Desain Dashboard, 2025* 

### 3.3.2. Sales Analysis

Halaman kedua *dashboard* menyajikan analisis mendalam tentang performa penjualan, sebagaimana ditampilkan pada Gambar 3.2.

*[Gambar 3.2 Sales Analysis Dashboard akan ditampilkan di sini]*

Tujuan Halaman: Analisis mendalam tentang performa penjualan untuk monitoring dan optimasi strategi penjualan.

Komponen Utama:

1. **Kartu KPI Penjualan (4 kartu)**

• **Gross Sales**: Menampilkan total penjualan kotor sebelum diskon dengan indikator pertumbuhan
• **Net Sales**: Menampilkan total penjualan bersih setelah diskon dengan indikator perubahan
• **Total Discounts**: Menampilkan total diskon yang diberikan dengan indikator persentase
• **Shipping Revenue**: Menampilkan total pendapatan dari biaya pengiriman dengan indikator pertumbuhan

2. **Visualisasi Utama**

A. **Channel Performance (Tabel)**
• Menampilkan performa setiap saluran penjualan: WhatsApp, Instagram, Marketplace, Offline
• Kolom: Sales Channel, Transactions, Revenue, Avg Order Value, AOV (Calculated)
• Membantu identifikasi saluran paling efektif dan efisien

B. **Sales by Day of Week (Bar Chart Horizontal)**
• Menampilkan distribusi penjualan berdasarkan hari dalam seminggu
• Membantu identifikasi pola penjualan harian untuk optimasi operasional dan *staffing*
• Wawasan: Membantu perencanaan promosi dan kampanye di hari-hari tertentu

3. **Visualisasi Pendukung**

A. **Monthly Sales Comparison (Combo Chart)**
• Menampilkan perbandingan penjualan bulanan dengan line chart untuk Revenue dan bar chart untuk Transactions
• Membantu identifikasi tren dan pola *seasonality*
• Fitur interaktif untuk *drill-down* ke detail bulanan

B. **Transaction Status Breakdown (Stacked Bar Chart)**
• Menampilkan distribusi status transaksi: Diterima vs Selesai
• Membantu monitoring efisiensi *fulfillment* dan identifikasi bottleneck operasional

C. **Recent Transactions (Tabel Detail)**
• Menampilkan transaksi terbaru dengan informasi lengkap
• Kolom: Transaction ID, Date, Time, Customer, Product, Channel, Status, Total Amount
• Fitur: Sortable, searchable, paginated untuk eksplorasi data detail
• Membantu monitoring transaksi *real-time* dan identifikasi pola pembelian

**Tabel 3.6** Komponen Visualisasi Sales Analysis

| **Komponen** | **Jenis Visualisasi** | **Tujuan** |
|--------------|----------------------|------------|
| Gross Sales | KPI Card | Monitoring penjualan kotor |
| Net Sales | KPI Card | Monitoring penjualan bersih |
| Total Discounts | KPI Card | Monitoring total diskon |
| Shipping Revenue | KPI Card | Monitoring pendapatan pengiriman |
| Channel Performance | Table | Analisis performa saluran |
| Sales by Day of Week | Horizontal Bar Chart | Pola penjualan harian |
| Monthly Sales Comparison | Combo Chart | Perbandingan penjualan bulanan |
| Transaction Status | Stacked Bar Chart | Status transaksi |
| Recent Transactions | Table | Transaksi terbaru |

*Sumber: Desain Dashboard, 2025*

### 3.3.3. Product Performance

Halaman ketiga *dashboard* menyajikan analisis mendalam tentang performa produk, sebagaimana ditampilkan pada Gambar 3.3.

*[Gambar 3.3 Product Performance Dashboard akan ditampilkan di sini]*

Tujuan Halaman: Analisis mendalam tentang performa produk untuk manajemen *inventory* dan strategi produk.

Komponen Utama:

**1. Kartu KPI Produk (4 kartu)**

• **Total Products**: Menampilkan jumlah total produk aktif dalam katalog
• **Inventory Value**: Menampilkan nilai total *inventory* berdasarkan harga modal
• **Avg Profit Margin**: Menampilkan rata-rata margin keuntungan dari semua produk
• **Low Stock Items**: Menampilkan jumlah produk dengan stok rendah yang perlu *restock*

**2. Visualisasi Utama**

A. **Category Analysis (Tabel dengan Bar Chart)**
• Menampilkan performa setiap kategori produk
• Kolom: Kategori, Revenue, Product Count, Units Sold, Avg Price, Avg Profit Margin
• Membantu identifikasi kategori yang paling menguntungkan

B. **Top 10 Best Sellers (Grafik Batang Horizontal)**
• Menampilkan 10 produk dengan penjualan tertinggi berdasarkan unit terjual
• Membantu identifikasi produk populer untuk strategi *inventory*

C. **Bottom 10 Slow Movers (Grafik Batang Horizontal)**
• Menampilkan 10 produk dengan penjualan terendah
• Membantu identifikasi produk yang perlu promosi atau dihentikan

3. **Visualisasi Pendukung**

A. **Price Range Distribution (Grafik Batang)**
• Menampilkan distribusi produk berdasarkan rentang harga
• Membantu memahami positioning produk di pasar

B. **Stock Level (Diagram Pie)**
• Menampilkan distribusi stok: Low (0-10), Medium (10-20), High (>20)
• Membantu monitoring kesehatan *inventory*

C. **Product Catalog (Tabel Detail)**
• Menampilkan katalog lengkap produk dengan informasi: Nama, Kategori, Sub-Kategori, Price, Cost, Margin %, Stocks
• Fitur: Sortable, searchable, paginated

**Tabel 3.7** Komponen Visualisasi Product Performance

| **Komponen** | **Jenis Visualisasi** | **Tujuan** |
|--------------|----------------------|------------|
| Total Products | KPI Card | Monitoring jumlah produk aktif |
| Inventory Value | KPI Card | Monitoring nilai inventory |
| Avg Profit Margin | KPI Card | Monitoring margin keuntungan |
| Low Stock Items | KPI Card | Monitoring produk stok rendah |
| Category Analysis | Table with Bar Chart | Analisis performa kategori |
| Top 10 Best Sellers | Horizontal Bar Chart | Produk terlaris |
| Bottom 10 Slow Movers | Horizontal Bar Chart | Produk lambat terjual |
| Price Range Distribution | Bar Chart | Distribusi rentang harga |
| Stock Level | Pie Chart | Distribusi level stok |
| Product Catalog | Table | Katalog produk lengkap |

*Sumber: Desain Dashboard, 2025* 

**6. Wawasan Utama:**

• "20% produk menghasilkan 60% pendapatan (Pareto)" 

• "Produk khusus memiliki margin 65% vs standar 40%" 

• "8 produk perlu perhatian (pergerakan lambat)" 

• "Kategori Nomor Rumah memiliki tingkat perputaran tertinggi" 

### 3.3.4. Customer Analysis

Halaman keempat *dashboard* menyajikan analisis karakteristik dan perilaku pelanggan, sebagaimana ditampilkan pada Gambar 3.4.

*[Gambar 3.4 Customer Analysis Dashboard akan ditampilkan di sini]*

Tujuan Halaman: Memahami karakteristik dan perilaku pelanggan untuk strategi *customer relationship management* yang lebih efektif.

Komponen Utama:

1. **Kartu KPI Pelanggan (4 kartu)**

• **Total Customers**: Menampilkan jumlah total pelanggan unik dengan indikator pertumbuhan
• **Avg Customer Value**: Menampilkan nilai rata-rata per pelanggan dengan indikator perubahan
• **Repeat Sales**: Menampilkan persentase pelanggan yang melakukan pembelian berulang
• **Avg Rating**: Menampilkan rata-rata rating kepuasan pelanggan dari semua transaksi

2. **Visualisasi Utama**

A. **RFM Segmentation (Pie Chart)**
• Menampilkan distribusi pelanggan berdasarkan segmentasi RFM (Recency, Frequency, Monetary)
• Segmen: Champions, Loyal, At Risk, New, Lost
• Membantu identifikasi pelanggan yang perlu perhatian khusus dan strategi retensi

B. **Geographic Distribution (Tabel dengan Bar Chart)**
• Menampilkan distribusi pelanggan berdasarkan kota
• Kolom: City, Customers, Revenue, Avg Order Value
• Membantu identifikasi pasar potensial dan peluang ekspansi geografis

3. **Visualisasi Pendukung**

A. **Customer Type Distribution (Donut Chart)**
• Menampilkan distribusi pelanggan berdasarkan tipe: Individu, Bisnis, Reseller
• Membantu memahami komposisi basis pelanggan untuk strategi marketing yang tertarget

B. **Source Channel Distribution (Bar Chart Horizontal)**
• Menampilkan distribusi pelanggan berdasarkan sumber akuisisi: Instagram, WhatsApp, TikTok, Marketplace, Website, Referral
• Membantu evaluasi efektivitas setiap channel untuk akuisisi pelanggan baru

C. **Top 20 Customers (Tabel Detail)**
• Menampilkan 20 pelanggan dengan nilai transaksi tertinggi
• Kolom: Customer Name, City, Type, Transactions, Total Spent, Avg Order
• Membantu identifikasi *high-value customers* untuk program VIP atau loyalitas khusus

D. **Customer Database (Tabel Lengkap)**
• Menampilkan database pelanggan lengkap dengan informasi detail
• Kolom: Name, Email, Phone, City, Transactions, Total Spent, Avg Order
• Fitur: Sortable, searchable, filterable untuk manajemen data pelanggan

**Tabel 3.8** Komponen Visualisasi Customer Analysis

| **Komponen** | **Jenis Visualisasi** | **Tujuan** |
|--------------|----------------------|------------|
| Total Customers | KPI Card | Monitoring jumlah pelanggan |
| Avg Customer Value | KPI Card | Monitoring nilai rata-rata pelanggan |
| Repeat Sales | KPI Card | Monitoring pembelian berulang |
| Avg Rating | KPI Card | Monitoring kepuasan pelanggan |
| RFM Segmentation | Pie Chart | Segmentasi pelanggan |
| Geographic Distribution | Table with Bar Chart | Distribusi geografis |
| Customer Type Distribution | Donut Chart | Distribusi tipe pelanggan |
| Source Channel Distribution | Horizontal Bar Chart | Distribusi sumber akuisisi |
| Top 20 Customers | Table | Pelanggan bernilai tinggi |
| Customer Database | Table | Database pelanggan lengkap |

*Sumber: Desain Dashboard, 2025* 

### 3.3.5. Financial Analysis

Halaman kelima *dashboard* menyajikan analisis keuangan komprehensif, sebagaimana ditampilkan pada Gambar 3.5.

*[Gambar 3.5 Financial Analysis Dashboard akan ditampilkan di sini]*

Tujuan Halaman: Analisis keuangan komprehensif untuk monitoring profitabilitas dan kesehatan finansial bisnis.

Komponen Utama:

1. **Kartu KPI Finansial (4 kartu)**

• **Total Revenue**: Menampilkan total pendapatan dengan indikator pertumbuhan
• **COGS (Cost of Goods Sold)**: Menampilkan total biaya pokok penjualan
• **Gross Profit**: Menampilkan laba kotor (Revenue - COGS)
• **Operational Costs**: Menampilkan total biaya operasional

2. **Visualisasi Utama**

A. **Revenue vs Profit Trend (Combo Chart)**
• Menampilkan tren pendapatan (bar) dan laba (line) sepanjang waktu
• Membantu monitoring profitabilitas dan identifikasi periode dengan margin rendah

B. **Gross Profit Margin Trend (Line Chart)**
• Menampilkan tren persentase margin laba kotor
• Membantu evaluasi efisiensi operasional

3. **Visualisasi Pendukung**

A. **Operational Costs Breakdown (Pie Chart)**
• Menampilkan komposisi biaya: Bahan Baku, Operasional, Marketing, Transportasi, Utilitas
• Membantu identifikasi area pengeluaran terbesar

B. **Revenue Composition (Stacked Bar Chart)**
• Menampilkan komposisi pendapatan: Custom Services vs Shipping
• Membantu memahami sumber pendapatan

C. **Expense Details (Tabel)**
• Menampilkan detail pengeluaran: Date, Category, Sub-Category, Description, Amount
• Fitur: Sortable, filterable, searchable

**Tabel 3.9** Komponen Visualisasi Financial Analysis

| **Komponen** | **Jenis Visualisasi** | **Tujuan** |
|--------------|----------------------|------------|
| Total Revenue | KPI Card | Monitoring total pendapatan |
| COGS | KPI Card | Monitoring biaya pokok penjualan |
| Gross Profit | KPI Card | Monitoring laba kotor |
| Operational Costs | KPI Card | Monitoring biaya operasional |
| Revenue vs Profit Trend | Combo Chart | Tren pendapatan dan laba |
| Gross Profit Margin Trend | Line Chart | Tren margin laba kotor |
| Operational Costs Breakdown | Pie Chart | Komposisi biaya operasional |
| Revenue Composition | Stacked Bar Chart | Komposisi pendapatan |
| Expense Details | Table | Detail pengeluaran |

*Sumber: Desain Dashboard, 2025*

### 3.3.6. Operations & Inventory Management

Halaman keenam *dashboard* menyajikan monitoring pergerakan stok dan efisiensi operasional, sebagaimana ditampilkan pada Gambar 3.6.

*[Gambar 3.6 Operations & Inventory Management Dashboard akan ditampilkan di sini]*

Tujuan Halaman: Monitoring pergerakan stok dan efisiensi operasional *warehouse*.

Komponen Utama:

1. **Kartu KPI Operasional (4 kartu)**

• **Total Stock In**: Menampilkan total unit yang masuk ke *inventory*
• **Total Stock Out**: Menampilkan total unit yang keluar (terjual)
• **Stock Turnover Rate**: Menampilkan rasio perputaran stok
• **Net Stock Change**: Menampilkan perubahan bersih *inventory*

2. **Visualisasi Utama**

A. **Stock Movement Trend (Combo Chart)**
• Menampilkan tren stok masuk (bar hijau) dan stok keluar (bar merah)
• Membantu monitoring pola pergerakan *inventory*

B. **Transaction Type Distribution (Donut Chart)**
• Menampilkan distribusi jenis transaksi: Penjualan vs Pembelian
• Membantu memahami aktivitas *warehouse*

3. **Visualisasi Pendukung**

A. **Stock Level by Category (Bar Chart Horizontal)**
• Menampilkan rata-rata level stok per kategori produk
• Membantu identifikasi kategori yang perlu *restock*

B. **Low Stock Alert Table**
• Menampilkan produk dengan stok rendah yang perlu perhatian
• Kolom: Product Name, Category, Stock Available, Stock Value

C. **Stock Movement History (Tabel Detail)**
• Menampilkan riwayat pergerakan stok: Date, Product, Transaction Type, Stock In, Stock Out, Final Stock
• Membantu audit dan tracking *inventory*

**Tabel 3.10** Komponen Visualisasi Operations & Inventory Management

| **Komponen** | **Jenis Visualisasi** | **Tujuan** |
|--------------|----------------------|------------|
| Total Stock In | KPI Card | Monitoring stok masuk |
| Total Stock Out | KPI Card | Monitoring stok keluar |
| Stock Turnover Rate | KPI Card | Monitoring perputaran stok |
| Net Stock Change | KPI Card | Monitoring perubahan stok |
| Stock Movement Trend | Combo Chart | Tren pergerakan stok |
| Transaction Type Distribution | Donut Chart | Distribusi jenis transaksi |
| Stock Level by Category | Horizontal Bar Chart | Level stok per kategori |
| Low Stock Alert Table | Table | Produk stok rendah |
| Stock Movement History | Table | Riwayat pergerakan stok |

*Sumber: Desain Dashboard, 2025*

### 3.3.7. Marketing Performance

Halaman ketujuh *dashboard* menyajikan evaluasi efektivitas kampanye pemasaran, sebagaimana ditampilkan pada Gambar 3.7.

*[Gambar 3.7 Marketing Performance Dashboard akan ditampilkan di sini]*

Tujuan Halaman: Evaluasi efektivitas kampanye pemasaran dan ROI untuk optimasi alokasi *budget*.

Komponen Utama:

1. **Kartu KPI Marketing (4 kartu)**

• **Total Campaigns**: Menampilkan jumlah total kampanye yang dijalankan
• **Total Budget**: Menampilkan total *budget* marketing yang dialokasikan
• **Average ROI**: Menampilkan rata-rata *Return on Investment* dari semua kampanye
• **Total Reach**: Menampilkan total jangkauan audiens dari semua kampanye

2. **Visualisasi Utama**

A. **Campaign ROI Comparison (Bar Chart Horizontal)**
• Menampilkan perbandingan ROI dari berbagai kampanye
• Diurutkan dari ROI tertinggi ke terendah
• Membantu identifikasi kampanye paling efektif

B. **Platform by Budget (Pie Chart)**
• Menampilkan distribusi *budget* berdasarkan platform: Google Ads, Facebook, TikTok, Instagram
• Membantu evaluasi alokasi *budget* per platform

3. **Visualisasi Pendukung**

A. **Campaign Performance Over Time (Combo Chart)**
• Menampilkan tren *budget*, *revenue generated*, dan *campaign profit* sepanjang waktu
• Membantu monitoring efektivitas marketing secara temporal

B. **Platform Performance (Tabel)**
• Menampilkan performa per platform: Campaigns, Total Spend, Total Reach, Total Engagement, Total Conversions, Total Revenue, Avg ROI
• Membantu perbandingan efektivitas antar platform

C. **Top Performing Campaigns (Tabel Detail)**
• Menampilkan kampanye terbaik: Campaign Name, Platform, Start Date, End Date, Budget, Reach, Engagement, Conversion, Revenue, ROI
• Membantu identifikasi *best practices* untuk kampanye future

**Tabel 3.11** Komponen Visualisasi Marketing Performance

| **Komponen** | **Jenis Visualisasi** | **Tujuan** |
|--------------|----------------------|------------|
| Total Campaigns | KPI Card | Monitoring jumlah kampanye |
| Total Budget | KPI Card | Monitoring budget marketing |
| Average ROI | KPI Card | Monitoring ROI rata-rata |
| Total Reach | KPI Card | Monitoring jangkauan audiens |
| Campaign ROI Comparison | Horizontal Bar Chart | Perbandingan ROI kampanye |
| Platform by Budget | Pie Chart | Distribusi budget per platform |
| Campaign Performance Over Time | Combo Chart | Tren performa kampanye |
| Platform Performance | Table | Performa per platform |
| Top Performing Campaigns | Table | Kampanye terbaik |

*Sumber: Desain Dashboard, 2025*

**Catatan**: 

• Setiap halaman dashboard dilengkapi dengan filter interaktif untuk eksplorasi data yang lebih mendalam
• Visualisasi dirancang responsif dan dapat diakses dari berbagai perangkat
• Warna dan desain konsisten mengikuti *branding* SATRIAMART 

## 3.4. Analisis dan Interpretasi

### 3.4.1. Interpretasi Hasil Visualisasi

Berdasarkan *dashboard* yang telah dibuat, berikut interpretasi hasil visualisasi utama:

**1. Pola Penjualan dan Seasonality**

*Dashboard* menunjukkan pola pertumbuhan pendapatan yang fluktuatif dengan puncak yang jelas pada periode tertentu sepanjang tahun. Pola ini mengindikasikan *seasonality* yang kuat, di mana permintaan meningkat menjelang liburan akhir tahun, periode libur sekolah, dan *event* khusus lainnya. Pemahaman pola musiman ini memungkinkan SATRIAMART untuk melakukan perencanaan *inventory* dan alokasi sumber daya yang lebih efektif.

**2. Performa Kategori Produk**

Analisis kategori produk mengungkapkan bahwa produk dengan nilai tinggi seperti Papan Nama dan Signage premium cenderung memberikan kontribusi pendapatan yang signifikan meskipun volume penjualan lebih rendah dibanding produk dengan harga lebih terjangkau. Hal ini konsisten dengan konsep *value-based selling* di mana fokus pada produk *high-margin* menghasilkan profitabilitas lebih baik. Kategori Nomor Rumah dan Papan Nama menunjukkan performa konsisten sebagai produk inti bisnis.

**3. Karakteristik dan Perilaku Pelanggan**

Analisis segmentasi pelanggan menunjukkan distribusi yang beragam dengan konsentrasi geografis yang tinggi di wilayah Jabodetabek. Segmentasi berdasarkan jenis pelanggan (Individu, Bisnis, Reseller) menunjukkan bahwa pelanggan bisnis memiliki nilai transaksi rata-rata yang lebih tinggi dibanding pelanggan individu. Hal ini mengindikasikan peluang untuk mengembangkan strategi pemasaran yang lebih tertarget untuk segmen B2B.

**4. Efektivitas Saluran Penjualan**

Analisis saluran penjualan menunjukkan bahwa platform komunikasi langsung seperti WhatsApp dan Instagram mendominasi transaksi. Hal ini menunjukkan bahwa pendekatan personal dan percakapan masih sangat efektif untuk produk *customizable* seperti yang dijual SATRIAMART. Konten visual di Instagram terbukti penting untuk produk dekorasi yang memerlukan visualisasi sebelum pembelian.

**5. Profitabilitas dan Kesehatan Finansial**

Analisis finansial menunjukkan margin laba yang sehat dengan rata-rata di atas 45%. Komposisi biaya operasional didominasi oleh bahan baku dan biaya produksi, yang merupakan karakteristik normal untuk bisnis manufaktur skala kecil. Monitoring tren margin laba membantu identifikasi periode dengan efisiensi operasional yang perlu ditingkatkan.

**6. Efektivitas Kampanye Marketing**

Analisis ROI kampanye pemasaran menunjukkan variasi yang signifikan antar platform dan jenis kampanye. Kampanye dengan konten visual dan *engagement* tinggi cenderung menghasilkan ROI yang lebih baik. Platform media sosial menunjukkan efektivitas yang baik untuk *brand awareness* dan konversi, terutama untuk target pasar yang lebih muda dan *tech-savvy*. 

### 3.4.2. Implikasi terhadap Strategi Bisnis SATRIAMART

Berdasarkan analisis data melalui *dashboard Business Intelligence*, berikut implikasi strategis yang dapat diterapkan:

**1. Optimasi Manajemen Inventory**

Pemahaman pola *seasonality* memungkinkan SATRIAMART untuk melakukan perencanaan *inventory* yang lebih akurat. Peningkatan produksi dan stok dapat dilakukan menjelang periode puncak, sementara pengurangan *inventory* di periode sepi membantu optimasi *cash flow* dan mengurangi biaya penyimpanan. Implementasi sistem *just-in-time* untuk produk dengan permintaan stabil dapat meningkatkan efisiensi operasional.

**2. Pengembangan Strategi Produk**

Analisis menunjukkan bahwa produk *custom* memiliki margin yang lebih tinggi dibanding produk standar. Strategi yang dapat diterapkan meliputi:
• Mendorong kustomisasi melalui *pricing incentive* dan kemudahan proses desain
• Menyoroti opsi kustomisasi dalam materi *marketing*
• Mengembangkan *product line* premium untuk segmen pasar yang lebih tinggi
• Fokus pada produk dengan *profit margin* tinggi untuk meningkatkan profitabilitas

**3. Peningkatan Retensi Pelanggan**

Data menunjukkan peluang signifikan untuk meningkatkan *repeat purchase rate*. Strategi retensi yang dapat diimplementasikan meliputi:
• Program loyalitas dengan sistem *reward points*
• *Follow-up marketing* melalui WhatsApp dan email setelah pembelian
• Penawaran eksklusif untuk pelanggan setia
• Personalisasi komunikasi berdasarkan riwayat pembelian
• *Customer service* yang responsif untuk meningkatkan kepuasan

**4. Optimasi Alokasi Budget Marketing**

Analisis ROI kampanye memberikan wawasan untuk alokasi *budget* yang lebih efektif:
• Prioritaskan platform dengan ROI tertinggi untuk kampanye berbayar
• Pertahankan kehadiran di semua saluran untuk *brand awareness*
• Fokus pada konten visual berkualitas tinggi untuk Instagram dan TikTok
• Manfaatkan WhatsApp untuk komunikasi personal dan *closing* penjualan
• Evaluasi dan optimasi kampanye secara berkala berdasarkan data performa

**5. Strategi Pricing dan Bundling**

Analisis harga dan volume penjualan menunjukkan peluang untuk:
• Implementasi strategi *bundling* untuk meningkatkan *average order value*
• *Dynamic pricing* berdasarkan permintaan dan *seasonality*
• Penawaran paket untuk pelanggan bisnis dan *reseller*
• *Value-based pricing* untuk produk *custom* dengan kompleksitas tinggi

**6. Ekspansi Geografis**

Dengan konsentrasi tinggi di Jabodetabek, terdapat peluang ekspansi ke wilayah lain:
• Kemitraan dengan *reseller* di kota-kota besar lainnya
• Optimasi *marketplace* untuk jangkauan nasional
• Strategi *shipping* yang kompetitif untuk wilayah di luar Jabodetabek 

### 3.4.3. Potensi Peningkatan Performa

Berdasarkan analisis *dashboard*, terdapat beberapa area dengan potensi peningkatan performa yang signifikan:

**1. Peningkatan Customer Retention**

*Dashboard* menunjukkan peluang untuk meningkatkan *repeat purchase rate* melalui:
• Implementasi program loyalitas dengan sistem *reward points* yang menarik
• *Follow-up* komunikasi melalui WhatsApp dan email setelah pembelian
• Penawaran eksklusif dan diskon untuk pelanggan setia
• Personalisasi rekomendasi produk berdasarkan riwayat pembelian
• *Customer engagement* melalui konten edukatif dan inspiratif

**2. Ekspansi Jangkauan Pasar**

Dengan konsentrasi geografis yang tinggi di Jabodetabek, terdapat peluang ekspansi:
• Penetrasi ke kota-kota tier 2 melalui *marketplace* dan *reseller*
• Optimasi SEO dan *online presence* untuk jangkauan organik nasional
• Kemitraan strategis dengan *interior designer* dan kontraktor di berbagai kota
• Pengembangan sistem *shipping* yang efisien untuk wilayah luar Jabodetabek

**3. Optimasi Average Order Value**

Strategi untuk meningkatkan nilai transaksi rata-rata meliputi:
• *Product bundling* yang menarik (contoh: nomor rumah + papan nama)
• Implementasi *recommendation system* pada proses checkout
• *Upselling* produk premium dengan nilai tambah yang jelas
• *Cross-selling* produk komplementer dengan saran "*complete the look*"
• Penawaran *free shipping* untuk pembelian di atas nilai tertentu

**4. Peningkatan Conversion Rate**

Untuk mengurangi *cancellation rate* dan meningkatkan konversi:
• Peningkatan *product visualization* dengan foto berkualitas tinggi dan *mockup* 3D
• Komunikasi yang jelas tentang *timeline* produksi dan pengiriman
• *Better expectation management* melalui deskripsi produk yang detail
• Proses pemesanan yang lebih *user-friendly* dan transparan
• *Customer service* yang responsif untuk menjawab pertanyaan sebelum pembelian

**5. Efisiensi Operasional**

Peluang peningkatan efisiensi operasional meliputi:
• Optimasi proses produksi untuk produk dengan permintaan tinggi
• Implementasi sistem *inventory management* yang lebih baik
• Pengurangan *lead time* untuk meningkatkan kepuasan pelanggan
• Standardisasi proses untuk produk populer tanpa mengurangi kualitas
• Pelatihan tim untuk meningkatkan produktivitas

**6. Optimasi Marketing ROI**

Berdasarkan analisis performa kampanye:
• Fokus pada platform dan jenis konten dengan ROI tertinggi
• A/B testing untuk optimasi *creative* dan *messaging*
• Retargeting pelanggan yang pernah mengunjungi tapi belum membeli
• Kolaborasi dengan *micro-influencer* yang relevan dengan target pasar
• Pengembangan konten *user-generated* untuk meningkatkan *trust*

# BAB IV

# PENUTUP

## 4.1. Kesimpulan

Berdasarkan hasil perancangan dan implementasi *Dashboard Business* *Intelligence* interaktif untuk SATRIAMART menggunakan Looker Studio, dapat disimpulkan beberapa hal sebagai berikut : 

**1. Keberhasilan Implementasi *Dashboard***

*Dashboard Business Intelligence* interaktif telah berhasil dirancang dan diimplementasikan dengan 7 halaman utama yang mencakup Executive Dashboard, Sales Analysis, Product Performance, Customer Analysis, Financial Analysis, Operations & Inventory Management, dan Marketing Performance. *Dashboard* dapat diakses secara *online*, responsif di berbagai perangkat, dan memiliki fitur interaktif yang memudahkan eksplorasi data. 

**2. Efektivitas Visualisasi Data** 

Pemilihan jenis visualisasi yang tepat (kartu skor, grafik garis, grafik batang, diagram lingkaran, peta geografis, peta panas, dan tabel) terbukti efektif dalam menyajikan informasi bisnis yang kompleks menjadi mudah dipahami. Setiap visualisasi dipilih berdasarkan karakteristik data dan tujuan analisis, mengikuti praktik terbaik dalam visualisasi data. 

**3. Wawasan Bisnis yang Bernilai** 

*Dashboard* berhasil menghasilkan wawasan bisnis yang dapat ditindaklanjuti, antara lain : 

• Identifikasi pola *seasonality* dengan periode puncak penjualan yang jelas sepanjang tahun
• Platform komunikasi langsung (WhatsApp dan Instagram) terbukti menjadi saluran paling efektif untuk produk *customizable*
• Distribusi pendapatan mengikuti prinsip Pareto dimana sebagian kecil produk menghasilkan mayoritas pendapatan
• Produk *custom* memiliki margin laba yang lebih tinggi dibanding produk standar
• Peluang peningkatan *customer retention* melalui program loyalitas dan *follow-up marketing*
• Konsentrasi geografis yang tinggi di Jabodetabek menunjukkan peluang ekspansi ke wilayah lain 





**4. Indikator Kinerja Utama (KPI)**

KPI yang berhasil diidentifikasi dan diintegrasikan dalam *dashboard* mencakup berbagai aspek bisnis sebagaimana ditampilkan pada Tabel 4.1.

**Tabel 4.1** Ringkasan Indikator Kinerja Utama (KPI) Dashboard

| **Kategori KPI** | **Indikator** | **Tujuan Monitoring** |
|------------------|---------------|----------------------|
| **KPI Penjualan** | Total Revenue | Monitoring performa penjualan |
| | Total Transactions | Monitoring volume transaksi |
| | Average Order Value | Monitoring nilai rata-rata pesanan |
| | Growth Rate | Monitoring pertumbuhan bisnis |
| **KPI Produk** | Total Products | Monitoring jumlah produk aktif |
| | Inventory Value | Monitoring nilai inventory |
| | Average Profit Margin | Monitoring margin keuntungan |
| | Low Stock Items | Monitoring produk stok rendah |
| **KPI Pelanggan** | Total Customers | Monitoring basis pelanggan |
| | Repeat Purchase Rate | Monitoring pembelian berulang |
| | Customer Lifetime Value | Monitoring nilai pelanggan |
| | Customer Segmentation | Monitoring segmentasi pelanggan |
| **KPI Operasional** | Stock In/Out | Monitoring pergerakan stok |
| | Stock Turnover Rate | Monitoring perputaran stok |
| | Fulfillment Rate | Monitoring tingkat pemenuhan |
| | Order Completion Time | Monitoring waktu penyelesaian |
| **KPI Keuangan** | Total Revenue | Monitoring pendapatan total |
| | COGS | Monitoring biaya pokok penjualan |
| | Gross Profit | Monitoring laba kotor |
| | Operational Costs | Monitoring biaya operasional |
| **KPI Marketing** | Total Campaigns | Monitoring jumlah kampanye |
| | Marketing Budget | Monitoring budget marketing |
| | Average ROI | Monitoring ROI rata-rata |
| | Total Reach | Monitoring jangkauan audiens |

*Sumber: Analisis Dashboard, 2025*

**5. Dukungan Pengambilan Keputusan**

*Dashboard* terbukti dapat mendukung pengambilan keputusan bisnis di berbagai area : 

• Perencanaan Persediaan: Data pola musiman membantu perencanaan stok untuk mengantisipasi permintaan puncak 

• Pengembangan Produk: Wawasan tentang produk terlaris dan produk margin tinggi mendukung strategi pengembangan produk 

• Strategi Pemasaran: Analisis ROI per saluran membantu optimasi alokasi anggaran pemasaran 

• Manajemen Pelanggan: Segmentasi RFM memungkinkan pemasaran tertarget dan strategi retensi pelanggan 

• Strategi Harga: Analisis harga *vs* volume membantu penetapan harga optimal 

**6. Kelayakan *Business Intelligence* untuk UMKM**

Penelitian ini membuktikan bahwa teknologi *Business Intelligence* dapat diimplementasikan secara efektif pada perusahaan skala kecil seperti SATRIAMART dengan:

• Tanpa Biaya: Menggunakan perangkat gratis (*Looker Studio*, *Google Sheets*) 

• Implementasi Mudah: Proses implementasi relatif mudah tanpa memerlukan keahlian teknis tinggi 

• Dampak Tinggi: *Dashboard* memberikan nilai signifikan dalam mendukung pengambilan keputusan berbasis data 

• Dapat Ditingkatkan: Solusi dapat ditingkatkan seiring pertumbuhan bisnis

**7. Proses ETL yang Sistematis**

Implementasi proses *Extract-Transform-Load* (ETL) yang sistematis menghasilkan data yang berkualitas dan siap untuk analisis. Proses pembersihan data, transformasi, dan agregasi memastikan akurasi dan konsistensi informasi yang disajikan dalam *dashboard*. 

**8. Manfaat Praktis untuk SATRIAMART** 

*Dashboard Business Intelligence* memberikan manfaat konkret : 

• Efisiensi waktu analisis dari manual (jam) menjadi instan (detik) 

• Visibilitas waktu nyata terhadap kinerja bisnis 

• Identifikasi proaktif terhadap masalah operasional 

• Wawasan berbasis data untuk strategi pertumbuhan 

• Patokan untuk memantau kemajuan dan pencapaian 

**9. *Platform Looker Studio***

*Looker Studio* terbukti menjadi pilihan yang tepat untuk implementasi *Business Intelligence* pada UMKM karena : 

• Antarmuka pengguna yang intuitif dan mudah digunakan 

• Integrasi mudah dengan *Google Sheets* 

• Fitur kolaborasi dan berbagi yang baik 

• Pemeliharaan dan pembaruan yang minimal 

• Dukungan komunitas dan dokumentasi yang lengkap 

**10. Hasil Pembelajaran**

Penelitian ini memberikan pembelajaran bahwa kesuksesan implementasi *Business Intelligence* tidak hanya bergantung pada teknologi, tetapi juga pada: 

• Pemahaman yang baik terhadap konteks bisnis dan kebutuhan pengguna 

• Kualitas data sebagai fondasi analisis 

• Pemilihan visualisasi yang tepat untuk menyampaikan wawasan 

• Perbaikan berulang berdasarkan umpan balik pengguna 



## 4.2. Saran

Berdasarkan hasil penelitian dan implementasi *Dashboard Business Intelligence* untuk SATRIAMART, penyusun memberikan saran sebagai berikut:

### 4.2.1. Saran untuk SATRIAMART

**1. Optimasi Penggunaan *Dashboard***

• Pelatihan Pengguna: Lakukan pelatihan berkala untuk semua pengguna dashboard agar dapat memaksimalkan fitur-fitur interaktif yang tersedia. 

• Tinjauan Berkala : Jadwalkan tinjauan *dashboard* secara berkala (mingguan/bulanan) untuk pemantauan KPI dan identifikasi hal-hal yang perlu ditindaklanjuti. 

• Budaya Berbasis Data: Budayakan pengambilan keputusan berbasis data, bukan hanya intuisi. Dorong tim untuk selalu merujuk ke dashboard sebelum membuat keputusan strategis. 

**2. Strategi Peningkatan Pendapatan** 

• **Fokus pada Produk High-Margin**: Prioritaskan pemasaran dan produksi untuk produk *custom* yang memiliki margin laba lebih tinggi dibanding produk standar.

• **Perencanaan Musiman**: Manfaatkan wawasan tentang pola *seasonality* untuk merencanakan kampanye pemasaran dan pengadaan stok menjelang periode puncak.

• **Optimasi Saluran**: Alokasikan lebih banyak sumber daya ke platform komunikasi langsung yang terbukti paling efektif untuk konversi penjualan.

**3. Strategi Retensi Pelanggan**

• **Program Loyalitas**: Implementasikan program loyalitas dengan sistem *reward points* untuk meningkatkan *repeat purchase rate* dan *customer lifetime value*.

• **Pemasaran Tertarget**: Gunakan segmentasi pelanggan untuk melakukan pemasaran yang lebih personal dan relevan dengan kebutuhan setiap segmen.

• **Kampanye Re-engagement**: Buat kampanye khusus untuk pelanggan yang sudah lama tidak bertransaksi dengan penawaran menarik dan komunikasi personal. 

**4. Ekspansi Geografis**

• Perluasan *Marketplace*: Perluas kehadiran di *marketplace* yang menjangkau kota-kota besar di luar Jabodetabek (Bandung, Surabaya, Semarang). 

• Kemitraan *Reseller* : Bangun jaringan reseller di wilayah yang belum tercakup untuk mengurangi biaya logistik. 

• Pemasaran Lokal: Sesuaikan konten pemasaran untuk target audiens di berbagai wilayah geografis. 

**5. Peningkatan Operasional**

• **Pengurangan Cancellation Rate**: Tingkatkan visualisasi produk dengan foto berkualitas tinggi dan *mockup* 3D, serta komunikasi yang lebih jelas tentang *timeline* produksi.

• **Optimasi Lead Time**: Optimasi proses produksi untuk mengurangi waktu penyelesaian pesanan, mengingat korelasi positif antara pengiriman cepat dan kepuasan pelanggan.

• **Kontrol Kualitas**: Pertahankan standar kualitas tinggi karena kepuasan pelanggan merupakan keunggulan kompetitif yang penting.

**6. Pengembangan Produk** 

• **Perluasan Produk Custom**: Tingkatkan varian produk *custom* karena memiliki margin yang lebih tinggi dan permintaan yang kuat dari segmen premium.

• **Product Bundling**: Buat paket *bundling* yang menarik untuk meningkatkan *average order value* dan memberikan nilai lebih kepada pelanggan.

• **Inovasi Berkelanjutan**: Kembangkan produk-produk inovatif berdasarkan *feedback* pelanggan, analisis tren pasar, dan data performa produk dari *dashboard*. 

### 4.2.2. Saran untuk Pengembangan *Dashboard*

**1. Integrasi Data Waktu Nyata**

• *Pipeline* Data Otomatis: Implementasikan pipeline ETL otomatis agar data terupdate otomatis tanpa pengunggahan manual. 

• Integrasi API: Integrasikan dashboard dengan API dari *marketplace*, media sosial, dan payment *gateway* untuk data waktu nyata. 

• Notifikasi Otomatis: Setup notifikasi otomatis untuk peringatan ketika KPI mencapai ambang batas tertentu. 



**2. Analitik Lanjutan**

• Analitik Prediktif: Tambahkan fitur analitik prediktif untuk peramalan permintaan dan prediksi penjualan menggunakan *machine learning*. 

• Analisis Kohort: Implementasikan analisis kohort untuk memahami perilaku pelanggan lebih mendalam. 

• Model Atribusi: Kembangkan model atribusi untuk memahami perjalanan pelanggan melalui berbagai titik sentuh. 

**3. Peningkatan Interaktivitas**

• Kemampuan *Drill-Down*: Tambahkan lebih banyak fitur drill-down untuk analisis eksplorasi. 

• Peringatan Kustom: Implementasikan peringatan yang dapat dikonfigurasi pengguna untuk memantau KPI kritis. 

• Fitur Perbandingan : Tambahkan fitur untuk membandingkan periode (tahun-ke-tahun, bulan-ke-bulan, *vs* target). 

**4. Optimasi *Mobile***

• Aplikasi *Mobile*: Kembangkan aplikasi mobile khusus atau optimalkan tampilan *mobile* untuk akses yang lebih mudah. 

• Notifikasi *Push*: Implementasikan notifikasi push untuk pembaruan metrik penting. 

• Akses *Offline*: Aktifkan akses *offline* untuk melihat data *dashboard* yang tersimpan dalam *cache*. 

**5. Fitur Kolaborasi**

• Komentar: Tambahkan fitur komentar pada visualisasi untuk kolaborasi tim. 

• Anotasi : Izinkan pengguna untuk menambahkan anotasi pada grafik untuk menyoroti kejadian penting. 

• Berbagi Wawasan: Buat fitur untuk berbagi wawasan spesifik melalui email atau aplikasi pesan. 

### 4.2.3. Saran untuk Penelitian Lanjutan

**1. Implementasi pada UMKM Lain**

• Replikasi implementasi *Dashboard Business Intelligence* pada UMKM di sektor berbeda untuk validasi metodologi. 

• Kembangkan kerangka kerja atau template yang dapat disesuaikan untuk berbagai jenis bisnis. 

• Buat studi kasus untuk menunjukkan praktik terbaik implementasi *Business Intelligence* di UMKM. 

**2. Implementasi Analitik Lanjutan**

• Penelitian tentang implementasi analitik prediktif untuk peramalan permintaan menggunakan *machine learning*. 

• Kembangkan sistem rekomendasi untuk saran produk berdasarkan perilaku pelanggan. 

• Implementasikan analisis sentimen dari ulasan pelanggan dan sebutan di media sosial. 

**3. Studi ROI**

• Lakukan studi *longitudinal* untuk mengukur ROI aktual dari *implementasi Dashboard Business Intelligence*. 

• Kuantifikasi penghematan waktu, peningkatan pendapatan, pengurangan biaya sebagai hasil dari keputusan berbasis data. 

• Bandingkan kinerja sebelum dan sesudah implementasi Business Intelligence dengan kelompok kontrol. 

**4. Perbandingan Platform**

• Studi komparatif antara *Looker Studio vs* *platform Business Intelligence* lain ( *Power BI, Tableau, Metabase*) untuk konteks UMKM. 

• Evaluasi pertukaran dalam hal biaya, fitur, kemudahan penggunaan, dan skalabilitas. 

• Berikan rekomendasi untuk pemilihan *platform* berdasarkan ukuran dan kebutuhan bisnis. 

**5. Integrasi dengan Sistem Lain**

• Penelitian tentang integrasi *Dashboard Business* *Intelligence* dengan sistem *ERP, CRM*, atau *platform e-commerce.* 

• Kembangkan konektor atau middleware untuk integrasi yang mulus. 

• Studi tentang tantangan dan praktik terbaik dalam integrasi sistem. 

### 4.2.4. Saran Umum

**1. Tata Kelola Data**

• Tetapkan kebijakan tata kelola data untuk memastikan kualitas, keamanan, dan privasi data. 

• Definisikan peran dan tanggung jawab untuk manajemen data. 

• Implementasikan pemantauan kualitas data dan audit berkala. 

**2. Manajemen Perubahan**

• Persiapkan strategi manajemen perubahan ketika mengimplementasikan perangkat *Business Intelligence* dalam organisasi. 

• Atasi resistensi terhadap perubahan melalui komunikasi dan pelatihan. 

• Rayakan pencapaian cepat untuk membangun momentum dan adopsi. 

**3. Peningkatan Berkelanjutan**

• Dashboard bukan produk akhir, tetapi dokumen hidup yang perlu peningkatan berkelanjutan. 

• Kumpulkan umpan balik berkala dari pengguna dan lakukan iterasi berdasarkan kebutuhan. 

• Tetap terupdate dengan tren dan praktik terbaik terbaru dalam Business Intelligence dan visualisasi data. 

**4. Pengembangan Keterampilan**

• Investasikan dalam pelatihan dan pengembangan keterampilan untuk tim dalam bidang analitik data. 

• Dorong literasi data di seluruh organisasi, tidak hanya tim teknis. 

• Bangun keahlian internal untuk keberlanjutan dan kurangi ketergantungan pada konsultan eksternal. 

**5. Dokumentasi**

• Pertahankan dokumentasi komprehensif tentang sumber data, perhitungan, dan asumsi. 

• Buat panduan pengguna dan tutorial video untuk memfasilitasi onboarding. 

• Dokumentasikan pembelajaran dan praktik terbaik untuk berbagi pengetahuan. 





# DAFTAR PUSTAKA

Turban et al., (2021). Business Intelligence merupakan seperangkat teknologi, aplikasi, dan praktik untuk pengumpulan, integrasi, analisis, dan presentasi informasi bisnis 

Howson, (2021). Dashboard merupakan alat visualisasi data yang menyajikan informasi penting dalam bentuk grafik, diagram, dan indikator kinerja yang mudah dipahami 

Turban et al., (2021) *Business Intelligence* (BI) merupakan istilah umum yang mencakup aplikasi, infrastruktur, perangkat, dan praktik terbaik yang memungkinkan akses dan analisis informasi untuk meningkatkan dan mengoptimalkan keputusan dan kinerja organisasi.



