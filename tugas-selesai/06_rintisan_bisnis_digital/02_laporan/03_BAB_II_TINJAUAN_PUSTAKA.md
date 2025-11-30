# BAB II
# TINJAUAN PUSTAKA

## 2.1. Tinjauan Pustaka

### 2.1.1. Konsep Dasar Aplikasi

#### A. Sistem Informasi

Menurut O'Brien & Marakas (2021), sistem informasi adalah kombinasi terorganisir dari orang, perangkat keras, perangkat lunak, jaringan komunikasi, dan sumber daya data yang mengumpulkan, mengubah, dan menyebarkan informasi dalam organisasi dengan tiga aktivitas dasar yaitu masukan, pemrosesan, dan keluaran.

#### B. Aplikasi Berbasis Web

Menurut Pressman & Maxim (2020), aplikasi berbasis web memiliki karakteristik:
- Aksesibilitas tinggi melalui browser
- Tidak bergantung pada platform
- Mudah diperbarui dan dipelihara
- Skalabilitas tinggi untuk pertumbuhan pengguna

CUR-HEART dikembangkan menggunakan Laravel untuk backend, Blade dan Tailwind CSS untuk frontend, MySQL untuk basis data, dan Nginx sebagai server web.

#### C. Framework Laravel

Laravel adalah kerangka kerja PHP sumber terbuka dengan pola MVC (Otwell, 2023). Fitur utama Laravel meliputi:
- Eloquent ORM untuk manajemen basis data
- Blade Templating untuk tampilan
- Routing dan Middleware untuk keamanan
- Migration untuk version control database
- Validation dan Security bawaan

Laravel dipilih karena ekosistem yang matang, dokumentasi lengkap, dan komunitas yang besar.

#### D. Database Management System (DBMS)

Menurut Elmasri & Navathe (2021), DBMS adalah perangkat lunak untuk membuat, mengelola, dan mengakses basis data. MySQL dipilih karena bersifat sumber terbuka, performa tinggi, dukungan ACID, dan kompatibilitas dengan Laravel.

#### E. Tailwind CSS

Tailwind CSS adalah kerangka kerja CSS berbasis utilitas (Wathan, 2023). Tailwind dipilih karena fleksibilitas tinggi, ukuran berkas kecil, dan integrasi sempurna dengan Laravel.

### 2.1.2. Metode Problem Solving

#### A. Design Thinking

Design Thinking adalah pendekatan berpusat pada manusia untuk inovasi yang terdiri dari 5 tahapan yaitu Empathize (berempati dengan pengguna), Define (mendefinisikan masalah), Ideate (menghasilkan ide solusi), Prototype (membuat prototipe), dan Test (menguji dengan pengguna) (Brown, 2019). Design Thinking dipilih karena berpusat pada pengguna, bersifat iteratif, dan mengurangi risiko kegagalan produk.

#### B. Lean Startup Methodology

Menurut Ries (2011), Lean Startup menekankan siklus Bangun-Ukur-Pelajari, pembelajaran tervalidasi, akuntansi inovasi, dan keputusan untuk berputar atau bertahan. Prinsip ini diterapkan melalui validasi asumsi, pengembangan produk minimum yang layak, iterasi berdasarkan umpan balik, dan pengukuran metrik keberhasilan.

### 2.1.3. Business Model Canvas (BMC)

Business Model Canvas adalah alat manajemen strategis untuk mengembangkan model bisnis baru atau mendokumentasikan model bisnis yang sudah ada. Menurut Osterwalder & Pigneur (2010), BMC terdiri dari 9 blok bangunan:

1. **Customer Segments (Segmen Pelanggan)**: Kelompok orang atau organisasi yang ingin dijangkau dan dilayani

2. **Value Propositions (Proposisi Nilai)**: Kumpulan produk dan layanan yang menciptakan nilai untuk segmen pelanggan

3. **Channels (Saluran)**: Cara perusahaan berkomunikasi dan menjangkau segmen pelanggan

4. **Customer Relationships (Hubungan Pelanggan)**: Jenis hubungan yang dibangun dengan segmen pelanggan

5. **Revenue Streams (Aliran Pendapatan)**: Uang yang dihasilkan dari setiap segmen pelanggan

6. **Key Resources (Sumber Daya Utama)**: Aset penting yang diperlukan untuk membuat model bisnis berfungsi

7. **Key Activities (Aktivitas Utama)**: Hal-hal penting yang harus dilakukan perusahaan

8. **Key Partnerships (Kemitraan Utama)**: Jaringan pemasok dan mitra yang membuat model bisnis berfungsi

9. **Cost Structure (Struktur Biaya)**: Semua biaya yang dikeluarkan untuk mengoperasikan model bisnis

BMC dipilih untuk CUR-HEART karena memberikan gambaran holistik model bisnis dalam satu halaman, memudahkan komunikasi dengan pemangku kepentingan, dan merupakan kerangka kerja yang terbukti efektif.

### 2.1.4. Pitch Deck

Pitch deck adalah presentasi singkat yang menjelaskan gambaran umum tentang rencana bisnis kepada calon investor, mitra, atau pemangku kepentingan. Menurut Kawasaki (2015), pitch deck yang efektif harus mengikuti aturan 10/20/30:
- Maksimal 10 slide
- Durasi presentasi 20 menit
- Ukuran huruf minimal 30 poin

Struktur pitch deck yang ideal mencakup:
1. Problem - masalah yang ingin diselesaikan
2. Solution - solusi yang ditawarkan
3. Market Opportunity - ukuran dan potensi pasar
4. Product - demo atau tangkapan layar produk
5. Traction - bukti validasi
6. Business Model - cara menghasilkan uang
7. Competition - lanskap kompetitor dan diferensiasi
8. Team - orang-orang di balik bisnis
9. Financials - proyeksi keuangan 3-5 tahun
10. Ask - jumlah pendanaan yang dibutuhkan

Pitch deck CUR-HEART dirancang untuk menarik investor pendanaan awal, meyakinkan mitra strategis, dan presentasi di kompetisi startup.

## 2.2. Penelitian Terkait

Berikut adalah penelitian terkait yang menjadi referensi dalam pengembangan sistem informasi CUR-HEART:

### 2.2.1. Penelitian 1: Sistem Informasi Manajemen Klinik Kesehatan Mental

Judul: "Perancangan Sistem Informasi Manajemen Klinik Kesehatan Mental Berbasis Web" oleh Andini, R., & Budiman, A. (2022) yang dipublikasikan di Jurnal Kesehatan Mental Indonesia, Vol. 8, No. 2 (Sinta 2).

Penelitian ini mengembangkan sistem informasi untuk mengelola operasional klinik kesehatan mental yang mencakup pendaftaran pasien, rekam medis elektronik, penjadwalan konsultasi, dan pelaporan menggunakan PHP dan MySQL dengan metode waterfall. Hasil penelitian menunjukkan peningkatan efisiensi pendaftaran pasien sebesar 65%, pengurangan waktu pencarian rekam medis dari 15 menit menjadi 2 menit, tingkat kepuasan pengguna 85%, dan pengurangan kesalahan data sebesar 78%.

Persamaan dengan CUR-HEART adalah sama-sama sistem informasi untuk layanan kesehatan mental berbasis web dengan fokus pada efisiensi operasional dan dokumentasi. Perbedaan dengan CUR-HEART adalah CUR-HEART fokus pada hipnoterapi dengan kerangka kerja modern Laravel, memiliki fitur reservasi daring dan gerbang pembayaran, menggunakan metode Design Thinking, serta memiliki model bisnis digital yang komprehensif menggunakan BMC.

### 2.2.2. Penelitian 2: Platform Digital untuk Layanan Terapi Online

Judul: "Pengembangan Platform Digital untuk Layanan Terapi Psikologi Online di Indonesia" oleh Prasetyo, D., & Wijaya, K. (2023) yang dipublikasikan di Jurnal Sistem Informasi Bisnis, Vol. 13, No. 1 (Sinta 2).

Penelitian ini mengembangkan platform pasar digital yang menghubungkan psikolog dengan klien untuk sesi terapi daring melalui panggilan video, mencakup fitur pemesanan, pembayaran, konferensi video, dan penilaian menggunakan teknologi Node.js, React, dan MongoDB. Hasil penelitian menunjukkan peningkatan aksesibilitas layanan terapi sebesar 120%, pengurangan biaya operasional psikolog sebesar 40%, tingkat konversi pemesanan 72%, dan tingkat retensi pengguna 68% setelah 3 bulan.

Persamaan dengan CUR-HEART adalah sama-sama platform digital untuk layanan terapi dengan fitur pemesanan dan pembayaran daring serta fokus pada aksesibilitas dan efisiensi. Perbedaan dengan CUR-HEART adalah CUR-HEART fokus pada hipnoterapi untuk satu pusat layanan (B2C) bukan pasar digital (B2B2C), menggunakan Laravel, memiliki fitur dokumentasi sesi yang lebih detail, dan terintegrasi dengan model bisnis luring dan daring.

### 2.2.3. Penelitian 3: Implementasi Business Model Canvas pada Startup Healthtech

Judul: "Implementasi Business Model Canvas pada Startup Healthtech: Studi Kasus Halodoc" oleh Santoso, B., & Lestari, P. (2022) yang dipublikasikan di Jurnal Manajemen dan Kewirausahaan, Vol. 24, No. 2 (Sinta 2).

Penelitian ini menganalisis penerapan Business Model Canvas pada startup teknologi kesehatan Halodoc dan bagaimana BMC membantu dalam pengembangan strategi bisnis dan penggalangan dana menggunakan metode kualitatif dengan studi kasus. Hasil penelitian menunjukkan BMC efektif untuk visualisasi model bisnis teknologi kesehatan, memudahkan identifikasi kemitraan utama dengan rumah sakit dan apotek, membantu perubahan arah dari telemedicine ke ekosistem kesehatan, dan mempercepat proses penggalangan dana dengan proposisi nilai yang jelas.

Persamaan dengan CUR-HEART adalah sama-sama menggunakan BMC untuk perencanaan bisnis di sektor teknologi kesehatan dengan integrasi layanan daring dan luring. Perbedaan dengan CUR-HEART adalah Halodoc merupakan pasar digital dengan skala unicorn sedangkan CUR-HEART adalah penyedia tunggal yang fokus pada pasar khusus hipnoterapi dan mengintegrasikan BMC dengan pengembangan sistem informasi.

### 2.2.4. Penelitian 4: User Experience Design untuk Aplikasi Kesehatan Mental

Judul: "User Experience Design untuk Aplikasi Kesehatan Mental: Pendekatan Design Thinking" oleh Kusuma, A., & Rahman, F. (2023) yang dipublikasikan di Jurnal Desain Komunikasi Visual, Vol. 11, No. 1 (Sinta 3).

Penelitian ini menggunakan metode Design Thinking untuk merancang pengalaman pengguna aplikasi kesehatan mental yang fokus pada empati, privasi, dan kemudahan penggunaan dengan melibatkan 30 responden dalam pengujian pengguna. Hasil penelitian menunjukkan Design Thinking efektif untuk memahami kebutuhan pengguna yang sensitif, prinsip empati dan privasi meningkatkan kepercayaan pengguna, skor kegunaan meningkat dari 62 menjadi 84 setelah iterasi, dan keterlibatan pengguna meningkat 45%.

Persamaan dengan CUR-HEART adalah sama-sama menggunakan Design Thinking dengan fokus pada pengalaman pengguna untuk aplikasi kesehatan mental serta menekankan privasi dan keamanan data. Perbedaan dengan CUR-HEART adalah CUR-HEART mencakup seluruh aspek bisnis bukan hanya pengalaman pengguna, memiliki 3 tipe pengguna (klien, terapis, admin), dan mengintegrasikan desain pengalaman pengguna dengan sistem informasi lengkap.

Berdasarkan analisis penelitian terkait, dapat disimpulkan bahwa digitalisasi layanan kesehatan mental terbukti meningkatkan efisiensi dan aksesibilitas, Business Model Canvas efektif untuk perencanaan bisnis teknologi kesehatan, Design Thinking cocok untuk pengembangan produk yang berpusat pada pengguna, integrasi teknologi web modern meningkatkan pengalaman pengguna, dan fokus pada privasi dan keamanan data sangat penting untuk aplikasi kesehatan mental.

CUR-HEART mengambil praktik terbaik dari penelitian-penelitian tersebut dan mengintegrasikannya dalam satu solusi komprehensif yang mencakup model bisnis, sistem informasi, dan desain pengalaman pengguna.

## 2.3. Teori Pendukung

### 2.3.1. Pengujian Aplikasi

#### A. Black Box Testing

Black Box Testing adalah metode pengujian perangkat lunak yang menguji fungsionalitas aplikasi tanpa melihat struktur internal atau kode program. Menurut Pressman & Maxim (2020), Black Box Testing fokus pada masukan yang diberikan ke sistem, keluaran yang dihasilkan sistem, dan kesesuaian keluaran dengan spesifikasi kebutuhan.

Teknik Black Box Testing meliputi Equivalence Partitioning (membagi masukan menjadi kelas valid dan tidak valid), Boundary Value Analysis (menguji nilai batas masukan), Decision Table Testing (menguji kombinasi masukan berbeda), State Transition Testing (menguji perubahan kondisi sistem), dan Use Case Testing (menguji berdasarkan skenario penggunaan).

Keuntungan Black Box Testing adalah tidak memerlukan pengetahuan pemrograman, dapat dilakukan oleh penguji independen, fokus pada perspektif pengguna, dan efisien untuk sistem yang besar. Penerapan pada CUR-HEART meliputi pengujian fungsionalitas reservasi, proses pembayaran dengan integrasi Midtrans, autentikasi dan otorisasi, operasi CRUD, validasi formulir dan penanganan kesalahan, serta notifikasi surel.

#### B. White Box Testing

White Box Testing adalah metode pengujian yang menguji struktur internal, desain, dan kode program. Menurut Myers et al. (2021), White Box Testing mencakup pengujian semua jalur independen, semua keputusan logis, semua perulangan, dan struktur data internal.

Teknik White Box Testing meliputi Statement Coverage (setiap pernyataan dieksekusi minimal sekali), Branch Coverage (setiap cabang dieksekusi), Path Coverage (setiap jalur yang mungkin dieksekusi), dan Condition Coverage (setiap kondisi boolean diuji). Penerapan pada CUR-HEART meliputi pengujian unit untuk setiap fungsi atau metode dengan cakupan kode minimal 70%, pengujian logika bisnis seperti perhitungan harga dan validasi jadwal, pengujian kueri basis data menggunakan Eloquent ORM, serta pengujian middleware untuk autentikasi dan otorisasi.

#### C. Usability Testing

Usability Testing adalah metode untuk mengevaluasi seberapa mudah antarmuka pengguna digunakan. Menurut Nielsen (2020), kegunaan memiliki 5 komponen yaitu Learnability (kemudahan pengguna menyelesaikan tugas pertama kali), Efficiency (kecepatan pengguna menyelesaikan tugas), Memorability (kemudahan pengguna mengingat cara menggunakan sistem), Errors (jumlah kesalahan yang dibuat pengguna), dan Satisfaction (kepuasan menggunakan sistem).

Metode Usability Testing meliputi Think Aloud Protocol (pengguna berbicara saat menggunakan sistem), Task Analysis (mengukur waktu dan tingkat keberhasilan tugas), Questionnaire seperti System Usability Scale (SUS), dan A/B Testing (membandingkan dua versi desain). Penerapan pada CUR-HEART meliputi pengujian kegunaan dengan 15 responden (5 klien, 5 terapis, 5 admin), menggunakan kuesioner System Usability Scale (SUS), dengan target tingkat penyelesaian tugas minimal 90% dan skor SUS minimal 70/100.

### 2.3.2. Peralatan Pendukung

#### A. Figma

Figma adalah alat desain berbasis cloud untuk desain antarmuka pengguna, pembuatan prototipe, dan kolaborasi. Menurut dokumentasi Figma (2023), keunggulan Figma meliputi kolaborasi waktu nyata yang memungkinkan banyak desainer bekerja bersamaan, berbasis cloud tanpa perlu instalasi perangkat lunak, pembuatan prototipe interaktif tanpa pengkodean, sistem desain dengan pustaka komponen untuk konsistensi, dan mode inspeksi untuk pengembang.

Penerapan pada CUR-HEART meliputi pembuatan 66 halaman mockup untuk semua peran pengguna, pembuatan sistem desain (warna, tipografi, komponen), pembuatan prototipe interaktif untuk pengujian pengguna, kolaborasi dengan pemangku kepentingan untuk umpan balik, dan ekspor aset untuk pengembangan.

#### B. PlantUML

PlantUML adalah alat untuk membuat diagram UML menggunakan teks biasa yang mendukung berbagai jenis diagram seperti Use Case Diagram, Class Diagram, Activity Diagram, Sequence Diagram, State Diagram, dan Component Diagram. Keunggulan PlantUML adalah berbasis teks sehingga mudah dikontrol versi dengan Git, cepat membuat diagram tanpa drag-and-drop, gaya yang konsisten, dan ekspor ke berbagai format (PNG, SVG, PDF).

Penerapan pada CUR-HEART meliputi Use Case Diagram untuk menggambarkan interaksi pengguna dengan sistem, Activity Diagram untuk proses bisnis seperti reservasi, dokumentasi sesi, dan pembuatan laporan, serta Sequence Diagram untuk alur komunikasi antar komponen.

#### C. dbdiagram.io

dbdiagram.io adalah alat untuk membuat Entity Relationship Diagram (ERD) menggunakan Domain Specific Language (DSL) dengan keunggulan sintaks sederhana untuk mendefinisikan tabel dan relasi, tata letak otomatis yang rapi, ekspor ke SQL, PDF, dan PNG, serta fitur kolaborasi. Penerapan pada CUR-HEART meliputi pembuatan ERD dengan 16 tabel, pendefinisian relasi (satu-ke-satu, satu-ke-banyak, banyak-ke-banyak), ekspor ke SQL untuk migrasi basis data, dan dokumentasi struktur basis data.

#### D. Git & GitHub

Git adalah sistem kontrol versi terdistribusi untuk melacak perubahan dalam kode sumber, sedangkan GitHub adalah platform hosting untuk repositori Git dengan fitur kolaborasi. Keunggulan Git dan GitHub meliputi kontrol versi untuk semua berkas (kode, dokumentasi, desain), strategi percabangan untuk pengembangan paralel, pull request untuk tinjauan kode, pelacakan isu untuk bug dan permintaan fitur, serta GitHub Actions untuk CI/CD.

Penerapan pada CUR-HEART meliputi repositori untuk kode sumber Laravel dan dokumentasi, strategi percabangan (main, develop, feature branches), konvensi pesan commit untuk kejelasan, dan GitHub Projects untuk manajemen proyek.

#### E. Postman

Postman adalah platform untuk pengembangan dan pengujian API dengan fitur utama meliputi pembuat permintaan API, koleksi untuk mengorganisir permintaan, variabel lingkungan, pengujian otomatis, dan dokumentasi API. Penerapan pada CUR-HEART meliputi pengujian titik akhir API (autentikasi, pemesanan, pembayaran), pembuatan koleksi untuk semua rute API, pengujian otomatis untuk pengujian regresi, dan dokumentasi untuk pengembang frontend.

#### F. Laravel Debugbar

Laravel Debugbar adalah paket untuk debugging aplikasi Laravel yang menampilkan informasi seperti kueri yang dieksekusi, waktu eksekusi, penggunaan memori, informasi rute, dan data tampilan. Penerapan pada CUR-HEART meliputi debugging masalah kinerja, optimasi kueri basis data, pemantauan penggunaan memori, dan profiling aplikasi.

Dengan teori pendukung dan peralatan yang tepat, pengembangan sistem informasi CUR-HEART dapat dilakukan secara efisien, terstruktur, dan menghasilkan produk berkualitas tinggi yang memenuhi kebutuhan pengguna dan standar industri.
