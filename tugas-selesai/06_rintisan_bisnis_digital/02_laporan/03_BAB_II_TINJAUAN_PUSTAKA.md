# BAB II
# TINJAUAN PUSTAKA

## 2.1. Tinjauan Pustaka

### 2.1.1. Konsep Dasar Aplikasi

#### A. Sistem Informasi

Menurut O'Brien & Marakas (2021), sistem informasi adalah kombinasi terorganisir dari orang, perangkat keras, perangkat lunak, jaringan komunikasi, dan sumber daya data yang mengumpulkan, mengubah, dan menyebarkan informasi dalam organisasi dengan tiga aktivitas dasar: input, processing, dan output.

#### B. Aplikasi Berbasis Web

Menurut Pressman & Maxim (2020), aplikasi berbasis web memiliki karakteristik aksesibilitas tinggi, platform independent, mudah di-update, dan skalabilitas tinggi. CUR-HEART dikembangkan menggunakan Laravel (backend), Blade + Tailwind CSS (frontend), MySQL (database), dan Nginx (web server).

#### C. Framework Laravel

Laravel adalah framework PHP open-source dengan pola MVC yang menyediakan fitur Eloquent ORM, Blade Templating, Routing, Middleware, Migration, Validation, dan Security (Otwell, 2023). Laravel dipilih karena ekosistem matang, dokumentasi lengkap, dan komunitas besar.

#### D. Database Management System (DBMS)

Menurut Elmasri & Navathe (2021), DBMS adalah software untuk membuat, mengelola, dan mengakses database dengan mekanisme DDL, DML, kontrol akses, backup/recovery, dan integritas data. MySQL dipilih karena open-source, performa tinggi, dukungan ACID, dan kompatibilitas dengan Laravel.

#### E. Tailwind CSS

Tailwind CSS adalah utility-first CSS framework yang memungkinkan membangun desain custom, responsive design, dan konsistensi melalui design system (Wathan, 2023). Tailwind dipilih karena fleksibilitas tinggi, file size kecil, dan integrasi sempurna dengan Laravel.

### 2.1.2. Metode Problem Solving

#### A. Design Thinking

Design Thinking adalah pendekatan human-centered untuk inovasi yang terdiri dari 5 tahapan: Empathize (memahami pengguna), Define (mendefinisikan masalah), Ideate (menghasilkan ide solusi), Prototype (membuat prototipe), dan Test (menguji dengan pengguna) (Brown, 2019). Design Thinking dipilih karena user-centric, iteratif, dan mengurangi risiko kegagalan produk.

#### B. Lean Startup Methodology

Menurut Ries (2011), Lean Startup menekankan Build-Measure-Learn Loop, Validated Learning, Innovation Accounting, dan Pivot or Persevere. Prinsip ini diterapkan melalui validasi asumsi, pengembangan MVP, iterasi berdasarkan feedback, dan pengukuran success metrics.

### 2.1.3. Business Model Canvas (BMC)

Business Model Canvas adalah strategic management tool untuk mengembangkan model bisnis baru atau mendokumentasikan model bisnis yang sudah ada. Menurut Osterwalder & Pigneur (2010), BMC terdiri dari 9 building blocks:

**1. Customer Segments (Segmen Pelanggan)**
Kelompok orang atau organisasi yang ingin dijangkau dan dilayani. Segmentasi berdasarkan kebutuhan, perilaku, atau karakteristik lain yang memerlukan value proposition berbeda.

**2. Value Propositions (Proposisi Nilai)**
Bundel produk dan layanan yang menciptakan nilai untuk customer segment tertentu. Menjawab pertanyaan: "Masalah apa yang kita selesaikan?" dan "Kebutuhan apa yang kita penuhi?"

**3. Channels (Saluran)**
Bagaimana perusahaan berkomunikasi dan menjangkau customer segments untuk menyampaikan value proposition. Mencakup awareness, evaluation, purchase, delivery, dan after-sales.

**4. Customer Relationships (Hubungan Pelanggan)**
Jenis hubungan yang dibangun dengan customer segments. Bisa berupa personal assistance, self-service, automated services, communities, atau co-creation.

**5. Revenue Streams (Aliran Pendapatan)**
Uang yang dihasilkan dari setiap customer segment. Bisa berupa asset sale, usage fee, subscription fee, lending/renting/leasing, licensing, brokerage fee, atau advertising.

**6. Key Resources (Sumber Daya Utama)**
Aset penting yang diperlukan untuk membuat model bisnis berfungsi. Bisa berupa physical, intellectual, human, atau financial resources.

**7. Key Activities (Aktivitas Utama)**
Hal-hal penting yang harus dilakukan perusahaan untuk membuat model bisnis berfungsi. Bisa berupa production, problem solving, atau platform/network.

**8. Key Partnerships (Kemitraan Utama)**
Jaringan supplier dan partner yang membuat model bisnis berfungsi. Motivasi partnership: optimization and economy of scale, reduction of risk and uncertainty, atau acquisition of particular resources and activities.

**9. Cost Structure (Struktur Biaya)**
Semua biaya yang dikeluarkan untuk mengoperasikan model bisnis. Bisa berupa cost-driven (fokus minimalisasi biaya) atau value-driven (fokus value creation).

BMC dipilih untuk CUR-HEART karena:
- Memberikan gambaran holistik model bisnis dalam satu halaman
- Memudahkan komunikasi dengan stakeholders
- Memfasilitasi diskusi dan brainstorming
- Membantu identifikasi area yang perlu diperbaiki
- Framework yang proven dan widely adopted

### 2.1.4. Pitch Deck

Pitch deck adalah presentasi singkat yang menjelaskan gambaran umum tentang rencana bisnis kepada calon investor, partner, atau stakeholders. Menurut Kawasaki (2015), pitch deck yang efektif harus mengikuti "10/20/30 Rule":
- 10 slides maksimal
- 20 menit durasi presentasi
- 30 point minimum font size

Struktur pitch deck yang ideal:
1. **Problem**: Masalah yang ingin diselesaikan
2. **Solution**: Solusi yang ditawarkan
3. **Market Opportunity**: Ukuran dan potensi pasar
4. **Product**: Demo atau screenshot produk
5. **Traction**: Bukti validasi (users, revenue, partnerships)
6. **Business Model**: Bagaimana menghasilkan uang
7. **Competition**: Landscape kompetitor dan diferensiasi
8. **Team**: Orang-orang di balik bisnis
9. **Financials**: Proyeksi keuangan 3-5 tahun
10. **Ask**: Berapa funding yang dibutuhkan dan untuk apa

Pitch deck CUR-HEART dirancang untuk:
- Menarik investor seed funding
- Meyakinkan partner strategis (rumah sakit, perusahaan)
- Presentasi di kompetisi startup
- Marketing material untuk stakeholders

## 2.2. Penelitian Terkait

Berikut adalah beberapa penelitian terkait yang menjadi referensi dalam pengembangan sistem informasi CUR-HEART:

### 2.2.1. Penelitian 1: Sistem Informasi Manajemen Klinik Kesehatan Mental

**Judul**: "Perancangan Sistem Informasi Manajemen Klinik Kesehatan Mental Berbasis Web"  
**Penulis**: Andini, R., & Budiman, A. (2022)  
**Jurnal**: Jurnal Kesehatan Mental Indonesia, Vol. 8, No. 2  
**Sinta**: Sinta 2

**Ringkasan**:
Penelitian ini mengembangkan sistem informasi untuk mengelola operasional klinik kesehatan mental yang mencakup pendaftaran pasien, rekam medis elektronik, penjadwalan konsultasi, dan pelaporan. Sistem dikembangkan menggunakan PHP dan MySQL dengan metode waterfall.

**Hasil**:
- Meningkatkan efisiensi pendaftaran pasien sebesar 65%
- Mengurangi waktu pencarian rekam medis dari 15 menit menjadi 2 menit
- Tingkat kepuasan pengguna mencapai 85%
- Mengurangi kesalahan data sebesar 78%

**Persamaan dengan CUR-HEART**:
- Sama-sama sistem informasi untuk layanan kesehatan mental
- Menggunakan teknologi web-based
- Fokus pada efisiensi operasional dan dokumentasi

**Perbedaan dengan CUR-HEART**:
- CUR-HEART fokus pada hipnoterapi, bukan konseling umum
- CUR-HEART menggunakan framework modern (Laravel) vs PHP native
- CUR-HEART memiliki fitur reservasi online dan payment gateway
- CUR-HEART menggunakan metode Design Thinking vs Waterfall
- CUR-HEART memiliki model bisnis digital yang komprehensif (BMC)

### 2.2.2. Penelitian 2: Platform Digital untuk Layanan Terapi Online

**Judul**: "Pengembangan Platform Digital untuk Layanan Terapi Psikologi Online di Indonesia"  
**Penulis**: Prasetyo, D., & Wijaya, K. (2023)  
**Jurnal**: Jurnal Sistem Informasi Bisnis, Vol. 13, No. 1  
**Sinta**: Sinta 2

**Ringkasan**:
Penelitian ini mengembangkan platform marketplace yang menghubungkan psikolog dengan klien untuk sesi terapi online via video call. Platform mencakup fitur booking, payment, video conference, dan rating/review. Menggunakan teknologi Node.js, React, dan MongoDB.

**Hasil**:
- Meningkatkan aksesibilitas layanan terapi sebesar 120%
- Mengurangi biaya operasional psikolog sebesar 40%
- Tingkat konversi booking mencapai 72%
- User retention rate 68% setelah 3 bulan

**Persamaan dengan CUR-HEART**:
- Platform digital untuk layanan terapi
- Fitur booking dan payment online
- Fokus pada aksesibilitas dan efisiensi

**Perbedaan dengan CUR-HEART**:
- CUR-HEART fokus pada hipnoterapi, bukan psikologi umum
- CUR-HEART untuk satu center (B2C), bukan marketplace (B2B2C)
- CUR-HEART menggunakan Laravel vs Node.js/React
- CUR-HEART memiliki fitur dokumentasi sesi yang lebih detail
- CUR-HEART terintegrasi dengan model bisnis offline dan online

### 2.2.3. Penelitian 3: Implementasi Business Model Canvas pada Startup Healthtech

**Judul**: "Implementasi Business Model Canvas pada Startup Healthtech: Studi Kasus Halodoc"  
**Penulis**: Santoso, B., & Lestari, P. (2022)  
**Jurnal**: Jurnal Manajemen dan Kewirausahaan, Vol. 24, No. 2  
**Sinta**: Sinta 2

**Ringkasan**:
Penelitian ini menganalisis penerapan Business Model Canvas pada startup healthtech Halodoc dan bagaimana BMC membantu dalam pengembangan strategi bisnis dan fundraising. Penelitian menggunakan metode kualitatif dengan studi kasus.

**Hasil**:
- BMC efektif untuk visualisasi model bisnis healthtech
- Memudahkan identifikasi key partnerships dengan rumah sakit dan apotek
- Membantu pivot dari telemedicine ke health ecosystem
- Mempercepat proses fundraising dengan value proposition yang jelas

**Persamaan dengan CUR-HEART**:
- Sama-sama menggunakan BMC untuk perencanaan bisnis
- Fokus pada sektor healthtech
- Mengintegrasikan layanan online dan offline

**Perbedaan dengan CUR-HEART**:
- Halodoc adalah marketplace, CUR-HEART adalah single provider
- Skala bisnis berbeda (unicorn vs startup)
- CUR-HEART fokus pada niche market (hipnoterapi)
- CUR-HEART mengintegrasikan BMC dengan pengembangan sistem informasi

### 2.2.4. Penelitian 4: User Experience Design untuk Aplikasi Kesehatan Mental

**Judul**: "User Experience Design untuk Aplikasi Kesehatan Mental: Pendekatan Design Thinking"  
**Penulis**: Kusuma, A., & Rahman, F. (2023)  
**Jurnal**: Jurnal Desain Komunikasi Visual, Vol. 11, No. 1  
**Sinta**: Sinta 3

**Ringkasan**:
Penelitian ini menggunakan metode Design Thinking untuk merancang user experience aplikasi kesehatan mental yang fokus pada empati, privasi, dan kemudahan penggunaan. Melibatkan 30 responden dalam user testing.

**Hasil**:
- Design Thinking efektif untuk memahami kebutuhan pengguna yang sensitif
- Prinsip empati dan privasi meningkatkan trust pengguna
- Usability score meningkat dari 62 menjadi 84 setelah iterasi
- User engagement meningkat 45%

**Persamaan dengan CUR-HEART**:
- Sama-sama menggunakan Design Thinking
- Fokus pada UX untuk aplikasi kesehatan mental
- Menekankan privasi dan keamanan data

**Perbedaan dengan CUR-HEART**:
- CUR-HEART mencakup seluruh aspek bisnis, bukan hanya UX
- CUR-HEART memiliki 3 tipe pengguna (klien, terapis, admin)
- CUR-HEART mengintegrasikan UX design dengan sistem informasi lengkap

**Kesimpulan dari Penelitian Terkait**:

Berdasarkan analisis penelitian terkait, dapat disimpulkan bahwa:
1. Digitalisasi layanan kesehatan mental terbukti meningkatkan efisiensi dan aksesibilitas
2. Business Model Canvas efektif untuk perencanaan bisnis healthtech
3. Design Thinking cocok untuk pengembangan produk yang user-centric
4. Integrasi teknologi web modern (Laravel, payment gateway) meningkatkan user experience
5. Fokus pada privasi dan keamanan data sangat penting untuk aplikasi kesehatan mental

CUR-HEART mengambil best practices dari penelitian-penelitian tersebut dan mengintegrasikannya dalam satu solusi komprehensif yang mencakup model bisnis, sistem informasi, dan user experience design.

## 2.3. Teori Pendukung

### 2.3.1. Pengujian Aplikasi

#### A. Black Box Testing

Black Box Testing adalah metode pengujian software yang menguji fungsionalitas aplikasi tanpa melihat struktur internal atau kode program. Menurut Pressman & Maxim (2020), Black Box Testing fokus pada:
- Input yang diberikan ke sistem
- Output yang dihasilkan sistem
- Apakah output sesuai dengan spesifikasi requirements

**Teknik Black Box Testing**:
1. **Equivalence Partitioning**: Membagi input menjadi kelas-kelas yang valid dan invalid
2. **Boundary Value Analysis**: Menguji nilai batas dari input
3. **Decision Table Testing**: Menguji kombinasi input yang berbeda
4. **State Transition Testing**: Menguji perubahan state sistem
5. **Use Case Testing**: Menguji berdasarkan skenario penggunaan

**Keuntungan Black Box Testing**:
- Tidak memerlukan pengetahuan programming
- Dapat dilakukan oleh tester independen
- Fokus pada perspektif pengguna
- Efisien untuk sistem yang besar

**Penerapan pada CUR-HEART**:
Black Box Testing digunakan untuk menguji:
- Fungsionalitas reservasi (input data klien, pilih layanan, pilih jadwal)
- Proses pembayaran (integrasi Midtrans)
- Autentikasi dan otorisasi (login, register, forgot password)
- CRUD operations (create, read, update, delete)
- Validasi form dan error handling
- Notifikasi email

#### B. White Box Testing

White Box Testing adalah metode pengujian yang menguji struktur internal, desain, dan kode program. Menurut Myers et al. (2021), White Box Testing mencakup:
- Testing semua independent paths
- Testing semua logical decisions (true/false)
- Testing semua loops
- Testing internal data structures

**Teknik White Box Testing**:
1. **Statement Coverage**: Setiap statement dieksekusi minimal sekali
2. **Branch Coverage**: Setiap branch (if-else) dieksekusi
3. **Path Coverage**: Setiap possible path dieksekusi
4. **Condition Coverage**: Setiap kondisi boolean diuji

**Penerapan pada CUR-HEART**:
White Box Testing digunakan untuk menguji:
- Unit testing untuk setiap function/method
- Code coverage minimal 70%
- Testing business logic (perhitungan harga, validasi jadwal)
- Testing database queries (Eloquent ORM)
- Testing middleware (authentication, authorization)

#### C. Usability Testing

Usability Testing adalah metode untuk mengevaluasi seberapa mudah user interface digunakan. Menurut Nielsen (2020), usability memiliki 5 komponen:
1. **Learnability**: Seberapa mudah pengguna menyelesaikan tugas pertama kali
2. **Efficiency**: Seberapa cepat pengguna menyelesaikan tugas
3. **Memorability**: Seberapa mudah pengguna mengingat cara menggunakan sistem
4. **Errors**: Berapa banyak error yang dibuat pengguna
5. **Satisfaction**: Seberapa menyenangkan menggunakan sistem

**Metode Usability Testing**:
- **Think Aloud Protocol**: Pengguna berbicara saat menggunakan sistem
- **Task Analysis**: Mengukur waktu dan tingkat keberhasilan tugas
- **Questionnaire**: System Usability Scale (SUS), CSUQ, QUIS
- **A/B Testing**: Membandingkan dua versi desain

**Penerapan pada CUR-HEART**:
- Usability testing dengan 15 responden (5 klien, 5 terapis, 5 admin)
- Menggunakan System Usability Scale (SUS) questionnaire
- Task completion rate minimal 90%
- Target SUS score minimal 70/100

### 2.3.2. Peralatan Pendukung

#### A. Figma

Figma adalah cloud-based design tool untuk UI/UX design, prototyping, dan collaboration. Menurut dokumentasi Figma (2023), keunggulan Figma:
- **Real-time Collaboration**: Multiple designers dapat bekerja bersamaan
- **Cloud-based**: Tidak perlu install software, akses dari browser
- **Prototyping**: Membuat interactive prototype tanpa coding
- **Design System**: Component library untuk konsistensi desain
- **Developer Handoff**: Inspect mode untuk developer

**Penerapan pada CUR-HEART**:
- Membuat 66 halaman mockup untuk semua user roles
- Membuat design system (colors, typography, components)
- Membuat interactive prototype untuk user testing
- Collaboration dengan stakeholders untuk feedback
- Export assets untuk development

#### B. PlantUML

PlantUML adalah tool untuk membuat UML diagram menggunakan plain text. Mendukung berbagai jenis diagram:
- Use Case Diagram
- Class Diagram
- Activity Diagram
- Sequence Diagram
- State Diagram
- Component Diagram

**Keunggulan PlantUML**:
- Text-based, mudah version control dengan Git
- Cepat membuat diagram tanpa drag-and-drop
- Konsisten styling
- Export ke berbagai format (PNG, SVG, PDF)

**Penerapan pada CUR-HEART**:
- Use Case Diagram untuk menggambarkan interaksi user-system
- Activity Diagram untuk proses bisnis (reservasi, dokumentasi sesi, generate report)
- Sequence Diagram untuk alur komunikasi antar komponen

#### C. dbdiagram.io

dbdiagram.io adalah tool untuk membuat Entity Relationship Diagram (ERD) menggunakan DSL (Domain Specific Language). Keunggulan:
- Simple syntax untuk define tables dan relationships
- Auto-layout yang rapi
- Export ke SQL, PDF, PNG
- Collaboration features

**Penerapan pada CUR-HEART**:
- Membuat ERD dengan 16 tabel
- Mendefinisikan relationships (one-to-one, one-to-many, many-to-many)
- Export ke SQL untuk database migration
- Dokumentasi struktur database

#### D. Git & GitHub

Git adalah distributed version control system untuk tracking changes dalam source code. GitHub adalah platform hosting untuk Git repositories dengan fitur collaboration.

**Keunggulan Git & GitHub**:
- Version control untuk semua file (code, documentation, design)
- Branching strategy untuk parallel development
- Pull request untuk code review
- Issue tracking untuk bug dan feature requests
- GitHub Actions untuk CI/CD

**Penerapan pada CUR-HEART**:
- Repository untuk source code Laravel
- Repository untuk documentation
- Branching strategy: main, develop, feature branches
- Commit message convention untuk clarity
- GitHub Projects untuk project management

#### E. Postman

Postman adalah platform untuk API development dan testing. Fitur utama:
- API request builder
- Collection untuk organize requests
- Environment variables
- Automated testing
- API documentation

**Penerapan pada CUR-HEART**:
- Testing API endpoints (authentication, booking, payment)
- Membuat collection untuk semua API routes
- Automated testing untuk regression testing
- Documentation untuk frontend developer

#### F. Laravel Debugbar

Laravel Debugbar adalah package untuk debugging Laravel application. Menampilkan informasi:
- Queries yang dieksekusi
- Execution time
- Memory usage
- Route information
- View data

**Penerapan pada CUR-HEART**:
- Debugging performance issues
- Optimasi database queries
- Monitoring memory usage
- Profiling application

#### G. MySQL Workbench

MySQL Workbench adalah visual tool untuk database design, development, dan administration. Fitur:
- Visual database design (ERD)
- SQL development
- Database administration
- Performance monitoring

**Penerapan pada CUR-HEART**:
- Visual design database schema
- Query optimization
- Database backup dan restore
- Performance tuning

Dengan teori pendukung dan peralatan yang tepat, pengembangan sistem informasi CUR-HEART dapat dilakukan secara efisien, terstruktur, dan menghasilkan produk berkualitas tinggi yang memenuhi kebutuhan pengguna dan standar industri.
