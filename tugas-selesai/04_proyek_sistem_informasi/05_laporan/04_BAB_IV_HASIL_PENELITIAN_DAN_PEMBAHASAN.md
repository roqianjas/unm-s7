# BAB IV  
# HASIL PENELITIAN DAN PEMBAHASAN

## A. INISIASI PROYEK

Proyek pengembangan Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART diinisiasi berdasarkan kebutuhan untuk mengoptimalkan operasional pusat layanan hipnoterapi dan kesehatan mental. CUR-HEART (*Hypnotherapy & Mind Wellness Center*) mengalami pertumbuhan signifikan dalam jumlah klien dan terapis, namun sistem manual yang digunakan menghambat efisiensi dan kualitas layanan.

### Latar Belakang Masalah

Berdasarkan observasi dan wawancara yang dilakukan pada September 2024, teridentifikasi beberapa permasalahan utama:

1. **Proses pemesanan manual** melalui WhatsApp dan telepon yang memakan waktu lama dan mengurangi tingkat konversi (hanya 60% dari pertanyaan menjadi pemesanan aktual)

2. **Konflik jadwal dan pemesanan ganda** terjadi 8-10 kasus per bulan karena manajemen jadwal menggunakan spreadsheet terpisah

3. **Dokumentasi terapi tidak terstruktur** dimana terapis menghabiskan 15 menit per sesi untuk pencatatan manual dengan risiko data hilang

4. **Tidak ada data untuk pengambilan keputusan** karena informasi tersebar di berbagai platform dan pembuatan laporan memakan waktu 2-3 hari

5. **Beban administratif tinggi** dengan admin menghabiskan 70% waktu untuk tugas repetitif seperti menjawab pertanyaan yang sama dan verifikasi pembayaran manual

6. **Risiko keamanan dan privasi data** klien yang sensitif disimpan dalam format tidak aman tanpa kontrol akses yang tepat

### Identifikasi Masalah

Berdasarkan latar belakang di atas, penulis mengidentifikasikan beberapa masalah sebagai berikut:

a. Pelayanan pemesanan terapi masih dilaksanakan secara konvensional sehingga kurang efektif dan efisien

b. Belum adanya sistem informasi pemesanan berbasis web untuk pemesanan dan manajemen terapi

c. Banyak terjadi kehilangan data klien karena belum adanya sistem informasi yang dapat mendata siapa saja klien yang sedang melakukan pemesanan dan mengikuti sesi terapi

### Ruang Lingkup

Ruang lingkup proyek ini mencakup pengembangan sistem informasi berbasis web dengan fitur-fitur utama:

- **Modul Pemesanan Online**: Klien dapat melihat jadwal terapis, memilih layanan, dan melakukan pemesanan secara mandiri 24/7
- **Manajemen Jadwal Terapis**: Sistem penjadwalan otomatis dengan deteksi konflik dan notifikasi
- **Dokumentasi Sesi Terapi**: Platform digital untuk terapis mencatat dan mengakses riwayat terapi klien
- **Pembayaran Terintegrasi**: Integrasi dengan payment gateway Midtrans untuk pembayaran online
- **Dashboard Admin**: Panel kontrol untuk monitoring pemesanan, terapis, dan laporan keuangan
- **Notifikasi Otomatis**: Email reminder untuk klien dan terapis tentang jadwal sesi

### Tujuan dan Manfaat Penelitian

**Tujuan penelitian dalam capstone project ini adalah:**

a. Agar pelayanan pemesanan terapi dapat berjalan dengan efektif dan efisien

b. Sistem informasi pemesanan diharapkan dapat memudahkan klien dalam melakukan pemesanan dan melihat riwayat terapi

c. Dengan adanya sistem informasi dapat memudahkan baik klien, petugas admin, maupun terapis dalam pengelolaan data pemesanan dan sesi terapi, sehingga semuanya dapat terkontrol dengan baik

d. Sebagai salah satu syarat kelulusan pada Program Studi Strata Satu (S1) untuk Program Studi Sistem Informasi di Fakultas Teknologi Informasi Universitas Nusa Mandiri

**Manfaat penelitian:**

Penelitian ini diharapkan memberikan manfaat bagi berbagai pihak:

- **Bagi CUR-HEART**: Meningkatkan efisiensi operasional, mengurangi kesalahan jadwal, dan mempercepat pertumbuhan bisnis
- **Bagi Klien**: Kemudahan dalam pemesanan layanan terapi kapan saja tanpa harus menghubungi admin
- **Bagi Terapis**: Mengurangi beban administratif dan memudahkan akses riwayat klien
- **Bagi Admin**: Otomasi tugas repetitif sehingga dapat fokus pada layanan pelanggan yang lebih berkualitas
- **Bagi Akademik**: Sebagai referensi pengembangan sistem informasi sejenis untuk layanan kesehatan mental

---

## B. PERENCANAAN PROYEK

Perencanaan proyek dilakukan untuk memastikan proyek berjalan sesuai target waktu, biaya, dan kualitas yang ditetapkan. Perencanaan mencakup berbagai area pengetahuan manajemen proyek.

### B.1 Perencanaan Ruang Lingkup (*Scope*)

Ruang lingkup proyek didefinisikan menggunakan Work Breakdown Structure (WBS) yang membagi pekerjaan menjadi komponen-komponen yang dapat dikelola:

**Tabel 4.1 Work Breakdown Structure (WBS)**

| Level 1 | Level 2 | Level 3 | Deskripsi |
|---------|---------|---------|-----------|
| 1. Project Management | 1.1 Inisiasi | 1.1.1 Identifikasi Masalah | Observasi dan wawancara pemangku kepentingan |
| | | 1.1.2 Studi Kelayakan | Analisis kelayakan teknis, operasional, ekonomi |
| | 1.2 Perencanaan | 1.2.1 Penyusunan WBS | Breakdown struktur pekerjaan |
| | | 1.2.2 Estimasi Biaya | Perhitungan biaya pengembangan |
| | 1.3 Monitoring | 1.3.1 Progress Tracking | Pemantauan kemajuan mingguan |
| 2. Analysis | 2.1 Requirements | 2.1.1 Functional Requirements | Identifikasi 40+ kebutuhan fungsional |
| | | 2.1.2 Non-functional Requirements | Keamanan, performa, usability |
| | 2.2 System Analysis | 2.2.1 As-Is Process | Dokumentasi proses bisnis saat ini |
| | | 2.2.2 To-Be Process | Rancangan proses bisnis baru |
| 3. Design | 3.1 Database Design | 3.1.1 ERD | Diagram relasi entitas 16 tabel |
| | | 3.1.2 Normalisasi | Normalisasi hingga 3NF |
| | 3.2 UI/UX Design | 3.2.1 Wireframe | Sketsa antarmuka pengguna |
| | | 3.2.2 Mockup | Desain visual 41 halaman di Figma |
| | 3.3 UML Diagrams | 3.3.1 Use Case Diagram | Diagram kasus penggunaan |
| | | 3.3.2 Activity Diagram | Diagram aktivitas proses bisnis |
| 4. Implementation | 4.1 Backend | 4.1.1 Laravel Setup | Instalasi dan konfigurasi framework |
| | | 4.1.2 Database Migration | Migrasi skema database |
| | | 4.1.3 API Development | Pengembangan controller dan model |
| | 4.2 Frontend | 4.2.1 Blade Templates | Pembuatan template view |
| | | 4.2.2 Tailwind Styling | Styling dengan Tailwind CSS |
| | 4.3 Integration | 4.3.1 Payment Gateway | Integrasi Midtrans |
| | | 4.3.2 Email Service | Konfigurasi notifikasi email |
| 5. Testing | 5.1 Unit Testing | 5.1.1 PHPUnit Tests | 30 test cases |
| | 5.2 Integration Testing | 5.2.1 API Testing | Pengujian integrasi antar modul |
| | 5.3 UAT | 5.3.1 User Testing | Pengujian oleh pengguna akhir |
| 6. Deployment | 6.1 Server Setup | 6.1.1 VPS Configuration | Setup Ubuntu, Nginx, PHP, MySQL |
| | | 6.1.2 SSL Certificate | Instalasi Let's Encrypt |
| | 6.2 Go Live | 6.2.1 Database Migration | Migrasi data ke production |
| | | 6.2.2 System Launch | Peluncuran sistem |

### B.2 Perencanaan Waktu Pengerjaan (*Time*)

Proyek dikerjakan selama 11 minggu dengan pembagian waktu sebagai berikut:

**Tabel 4.2 Jadwal Pengerjaan Proyek**

| No | Fase | Durasi | Periode | Deliverables |
|----|------|--------|---------|--------------|
| 1 | Analisis Kebutuhan | 2 minggu | 16-29 Sep 2024 | Dokumen SRS, Studi Kelayakan |
| 2 | Desain Sistem | 2 minggu | 30 Sep - 13 Okt 2024 | ERD, Diagram UML, Mockup UI/UX |
| 3 | Implementasi | 4 minggu | 14 Okt - 10 Nov 2024 | Aplikasi web 60+ halaman |
| 4 | Pengujian | 2 minggu | 11-24 Nov 2024 | Laporan pengujian, UAT approval |
| 5 | Deployment | 1 minggu | 25 Nov - 1 Des 2024 | Sistem production live |

### B.3 Perencanaan Anggaran Biaya (*Cost*)

Estimasi biaya proyek menggunakan metode bottom-up berdasarkan WBS:

**Tabel 4.3 Estimasi Biaya Proyek**

| No | Kategori | Item | Biaya (Rp) |
|----|----------|------|------------|
| 1 | Project Management | Project Manager (11 minggu × Rp 100.000/minggu) | 1.100.000 |
| | | Contingency (10%) | 110.000 |
| 2 | Hardware | Laptop Development (sudah ada) | 0 |
| | | VPS Hosting (1 tahun) | 1.200.000 |
| 3 | Software | Laravel Framework (gratis) | 0 |
| | | MySQL Database (gratis) | 0 |
| | | Domain & SSL (1 tahun) | 150.000 |
| 4 | Development | Backend Developer (4 minggu × Rp 200.000/minggu) | 800.000 |
| | | Frontend Developer (4 minggu × Rp 200.000/minggu) | 800.000 |
| | | Full-stack Developer (4 minggu × Rp 200.000/minggu) | 800.000 |
| 5 | Testing | Testing Tools (gratis - PHPUnit) | 0 |
| | | UAT Sessions | 200.000 |
| 6 | Training | User Training Materials | 100.000 |
| 7 | Lain-lain | Dokumentasi, Transport, Komunikasi | 300.000 |
| **TOTAL** | | | **5.560.000** |

### B.4 Perencanaan Kualitas (*Quality*)

Standar kualitas yang ditetapkan untuk proyek ini:

- **Fungsionalitas**: 90% kebutuhan fungsional harus terpenuhi
- **Performa**: Waktu load halaman < 2 detik
- **Keamanan**: Mitigasi OWASP Top 10
- **Usability**: Skor System Usability Scale (SUS) minimal 70/100
- **Reliability**: Uptime minimal 99%
- **Code Quality**: Code coverage testing minimal 70%

### B.5 Perencanaan Sumber Daya (*Resource*)

**Tabel 4.4 Alokasi Sumber Daya Manusia**

| No | Nama | Peran | Tanggung Jawab |
|----|------|-------|----------------|
| 1 | Roki Anjas (11250066) | Project Manager & Backend Developer | Koordinasi tim, pengembangan backend, dokumentasi |
| 2 | Susanto (11250068) | Frontend Developer & UI/UX Designer | Desain antarmuka, pengembangan frontend |
| 3 | Fahruroji (11250085) | Full-stack Developer & Database Architect | Desain database, pengembangan full-stack, deployment |

**Sumber Daya Teknologi:**
- Laptop/PC untuk development (3 unit - milik tim)
- VPS Ubuntu 22.04 untuk production server
- Software development tools (VS Code, Git, Figma - gratis)

### B.6 Manajemen Risiko (*Risk*)

**Tabel 4.5 Identifikasi dan Mitigasi Risiko**

| No | Risiko | Probabilitas | Dampak | Mitigasi |
|----|--------|-------------|--------|----------|
| 1 | Keterlambatan jadwal | Sedang | Tinggi | Buffer time 10%, prioritas fitur dengan MoSCoW |
| 2 | Scope creep (perubahan kebutuhan) | Sedang | Tinggi | Dokumentasi kebutuhan yang jelas, change control |
| 3 | Bug kritis saat deployment | Rendah | Tinggi | Testing menyeluruh, staging environment |
| 4 | Anggota tim sakit | Rendah | Sedang | Knowledge sharing, dokumentasi kode |
| 5 | Integrasi payment gateway gagal | Sedang | Sedang | Prototyping awal, dokumentasi API lengkap |

### B.7 Perencanaan Komunikasi (*Communication*)

- **Meeting mingguan**: Setiap Senin pukul 19.00 WIB via Google Meet
- **Daily standup**: Chat group WhatsApp setiap pagi
- **Progress report**: Update ke dosen pembimbing setiap 2 minggu
- **Dokumentasi**: Google Drive untuk sharing dokumen
- **Version control**: GitHub untuk manajemen kode

### B.8 Perencanaan Pengadaan (*Procurement*)

Pengadaan yang diperlukan:
- **VPS Hosting**: Penyewaan server dari provider Niagahoster (Rp 1.200.000/tahun)
- **Domain**: Pembelian domain .id (Rp 150.000/tahun)
- **Payment Gateway**: Integrasi dengan Midtrans (gratis untuk development, fee per transaksi untuk production)

### B.9 Perencanaan Integrasi (*Integration*)

Integrasi yang direncanakan:
- **Payment Gateway**: Midtrans Snap API untuk pembayaran online
- **Email Service**: SMTP Gmail untuk notifikasi email
- **Cloud Storage**: Potensi integrasi Google Drive untuk backup (fase 2)

### B.10 Manajemen Pemangku Kepentingan (*Stakeholder*)

**Tabel 4.6 Daftar Pemangku Kepentingan**

| No | Stakeholder | Peran | Tingkat Kepentingan | Strategi Keterlibatan |
|----|------------|-------|---------------------|---------------------|
| 1 | Pemilik CUR-HEART | Sponsor & Decision Maker | Sangat Tinggi | Presentasi progress bulanan, approval kebutuhan |
| 2 | Terapis (3 orang) | End User | Tinggi | Workshop kebutuhan, UAT, training |
| 3 | Admin (2 orang) | End User | Tinggi | Workshop kebutuhan, UAT, training |
| 4 | Klien (8 orang sample) | End User | Sedang | Survey kebutuhan, usability testing |
| 5 | Dosen Pembimbing | Academic Advisor | Sangat Tinggi | Konsultasi mingguan, review dokumen |
| 6 | Tim Pengembang | Development Team | Sangat Tinggi | Daily standup, weekly meeting |

---

## C. KEUNTUNGAN YANG DIHARAPKAN

Implementasi Sistem Informasi CUR-HEART diharapkan memberikan berbagai keuntungan bagi pemangku kepentingan yang terlibat.

### 1. Manfaat untuk CUR-HEART (Organisasi)

**A. Efisiensi Operasional**

- **Proses pemesanan otomatis**: Pengurangan waktu dari 10-15 menit menjadi 3 menit per pemesanan, penghematan sekitar 20 jam per bulan
- **Manajemen penjadwalan**: Koordinasi jadwal berkurang dari 5 jam per minggu menjadi 1 jam, utilisasi meningkat dari 60% menjadi 80%
- **Pelaporan otomatis**: Waktu pembuatan laporan dari 2 jam menjadi 5 menit, penghematan 8 jam per bulan
- **Eliminasi pemesanan ganda**: Konflik jadwal turun dari 8-10 kasus per bulan menjadi 0 kasus

**B. Pertumbuhan Pendapatan**

- **Peningkatan volume pemesanan**: Target +25% dari 80 menjadi 100 pemesanan per bulan (Rp 72 juta/tahun tambahan)
- **Pengurangan tidak hadir**: Dari 15% menjadi 5% dengan reminder otomatis (Rp 28,8 juta/tahun pendapatan dipulihkan)
- **Perpanjangan jam layanan**: Pemesanan 24/7 menangkap 15% lebih banyak klien (Rp 10 juta/tahun)
- **Retensi klien**: Peningkatan dari 35% menjadi 60% dengan pengalaman yang lebih baik

**C. Kualitas & Layanan**

- **Pengambilan keputusan berbasis data**: Dashboard real-time untuk analisis cepat
- **Pemantauan kualitas**: Sistematis dengan target SUS ≥ 68, NPS ≥ 30
- **Skalabilitas**: Sistem digital dapat mendukung pertumbuhan 5× tanpa tambahan staf

**Total Manfaat Tahunan Terukur:**
- Peningkatan Pendapatan: Rp 115,8 juta/tahun
- Penghematan Biaya: Rp 18,4 juta/tahun
- **TOTAL**: Rp 134,2 juta/tahun

### 2. Manfaat untuk Klien

**A. Kenyamanan**

- Pemesanan 24/7 kapan saja tanpa terbatas jam kantor
- Tidak perlu telepon, layanan mandiri online
- Mobile-friendly untuk pemesanan saat bepergian
- Penjadwalan ulang mudah tanpa koordinasi manual

**B. Transparansi**

- Profil terapis lengkap dengan pendidikan, spesialisasi, dan ulasan
- Ketersediaan real-time dengan kalender visual
- Harga transparan per layanan
- Sistem rating & ulasan untuk memilih terapis terbaik

**C. Layanan Mandiri**

- Akses riwayat janji temu lengkap
- Lihat catatan sesi yang dibagikan terapis
- Pelacakan kemajuan terapi dengan grafik visual
- Pengingat otomatis untuk sesi mendatang

**Nilai untuk Klien:**
- Penghematan waktu: 25-55 menit per pemesanan
- Target kepuasan: ≥ 4,0/5,0, SUS ≥ 68
- Retensi meningkat: 35% → 60%

### 3. Manfaat untuk Terapis

**A. Penghematan Waktu**

- Manajemen jadwal mandiri mengurangi koordinasi dengan admin
- Hemat 16 jam per bulan untuk administrasi
- Dokumentasi sesi digital lebih cepat (5 menit vs 15 menit)

**B. Potensi Pendapatan**

- Utilisasi lebih baik dari 60% → 80%
- Peningkatan pendapatan +33% (Rp 5 juta/bulan)
- Akses ke analytics kinerja pribadi

**C. Keseimbangan Kerja-Hidup**

- Otonomi dan fleksibilitas dalam mengatur jadwal
- Beban administratif berkurang signifikan
- Target kepuasan terapis: ≥ 4,5/5,0

### 4. Analisis Return on Investment (ROI)

**Investasi:**
- Biaya awal: Rp 3.000.000 (setup)
- Biaya berulang tahun 1: Rp 9.750.000 (hosting, domain, payment gateway)
- **Total biaya tahun 1: Rp 12.750.000**

**Manfaat Tahun 1:**
- Peningkatan pendapatan: Rp 142.800.000
- Penghematan biaya: Rp 26.400.000
- **Total manfaat: Rp 169.200.000**

**Hasil:**
- Manfaat bersih: Rp 156.450.000
- **ROI: 1.227%**
- **Payback period: 0,9 bulan (~27 hari)**
- Rasio Manfaat-Biaya: 13,3:1

**Proyeksi 5 Tahun:**
- Total manfaat: Rp 1.025.481.825
- Total biaya: Rp 60.098.000
- Manfaat bersih: Rp 964.383.829
- ROI 5 tahun: 7.258%

**Rekomendasi:** Proyek sangat layak dengan ROI luar biasa dan payback period sangat singkat.

---

## D. TEKNOLOGI YANG DIGUNAKAN

Teknologi yang digunakan untuk membangun Sistem Informasi CUR-HEART secara garis besar dapat dibagi ke dalam beberapa bagian berikut ini:

### 1. Server dan Infrastructure

**A. Web Server**
- **Nginx 1.18.0**: Web server berkinerja tinggi untuk menangani concurrent connections
- **PHP 8.1**: Server-side scripting language dengan fitur modern (JIT compiler, named arguments, attributes)

**B. Hosting**
- **VPS (Virtual Private Server)**: Ubuntu Server 22.04 LTS
- Spesifikasi: 4 vCPU, 8GB RAM, 160GB SSD Storage
- Uptime SLA: 99,9%
- Bandwidth: Unlimited

**C. Database Server**
- **MySQL 8.0**: Relational database management system
- Storage Engine: InnoDB untuk ACID compliance
- Backup: Automated daily backup dengan retention 30 hari

### 2. Backend Development

**A. Framework & Language**
- **Laravel 10**: PHP framework modern dengan arsitektur MVC
  - Eloquent ORM untuk database abstraction
  - Blade templating engine
  - Middleware untuk authentication & authorization
  - Queue system untuk background jobs
  - Event & listener untuk asynchronous operations

**B. Authentication & Authorization**
- Laravel Sanctum untuk API token authentication
- Laravel Permission (Spatie) untuk role-based access control (RBAC)
- Bcrypt untuk password hashing

**C. Libraries & Packages**
- Midtrans PHP SDK untuk payment gateway integration
- Laravel Mail untuk email notifications
- Carbon untuk date/time manipulation
- Intervention Image untuk image processing

### 3. Frontend Development

**A. Technologies**
- **HTML5**: Markup semantic modern
- **CSS3**: Styling dengan flexbox dan grid
- **JavaScript (ES6+)**: Interaktivity dan dynamic content
- **Alpine.js**: Lightweight JavaScript framework untuk reactive components

**B. CSS Framework**
- **Tailwind CSS 3.3**: Utility-first CSS framework
  - Responsive design dengan mobile-first approach
  - Custom color palette dan typography
  - JIT (Just-In-Time) compiler untuk optimasi
  - PurgeCSS untuk menghapus unused styles

**C. UI Components**
- Custom component library berbasis Tailwind
- Icons: Heroicons (SVG icon set)
- Form validation: Client-side dengan JavaScript + server-side Laravel

### 4. Database

**A. Database Management**
- **MySQL 8.0**: Primary database
- Character Set: utf8mb4 untuk full Unicode support
- Collation: utf8mb4_unicode_ci

**B. Database Design**
- 16 tables dengan normalisasi 3NF
- Foreign key constraints untuk referential integrity
- Indexes pada frequently queried columns
- Timestamps untuk audit trail

**C. Migration & Seeding**
- Laravel Migrations untuk version control database schema
- Seeders untuk sample data dan testing data

### 5. Integration & External Services

**A. Payment Gateway**
- **Midtrans**: Payment gateway terintegrasi
  - Snap API untuk seamless checkout
  - Support: Credit card, Bank transfer, E-wallet (GoPay, OVO, Dana)
  - Security: PCI-DSS compliant
  - Webhook untuk payment notification

**B. Email Service**
- **SMTP (Mailtrap/SendGrid)**: Email delivery service
  - Notification emails (booking confirmation, reminder)
  - Transactional emails (password reset, welcome email)
  - Queue-based untuk menghindari blocking

**C. File Storage**
- Local storage untuk development
- AWS S3 / DigitalOcean Spaces (ready untuk production scale)

### 6. Development Tools

**A. Version Control**
- **Git**: Distributed version control system
- **GitHub**: Remote repository hosting
- Branching strategy: GitFlow (main, develop, feature branches)

**B. Code Editor & IDE**
- Visual Studio Code dengan extensions:
  - Laravel Extension Pack
  - PHP Intelephense
  - Tailwind CSS IntelliSense
  - ESLint & Prettier

**C. Package Managers**
- **Composer**: PHP dependency management
- **NPM**: JavaScript package management

### 7. Testing

**A. Testing Framework**
- **PHPUnit**: Unit testing untuk backend logic
- **Laravel Dusk**: Browser automation testing
- Feature tests untuk API endpoints

**B. Code Quality**
- PHP Code Sniffer untuk coding standards
- Laravel Debugbar untuk development debugging
- Error tracking & monitoring

### 8. Deployment & DevOps

**A. Deployment**
- **GitHub Actions**: CI/CD automation
- Automated testing sebelum deployment
- Zero-downtime deployment strategy

**B. Monitoring**
- **UptimeRobot**: Uptime monitoring
- **New Relic / Laravel Telescope**: Application performance monitoring
- Error logging dengan Laravel Log

**C. Security**
- **Let's Encrypt**: Free SSL/TLS certificate
- HTTPS enforced untuk semua connections
- CSRF protection (built-in Laravel)
- XSS prevention
- SQL injection prevention (Eloquent ORM)
- Rate limiting untuk API endpoints

### 9. Design & Prototyping

**A. UI/UX Design**
- **Figma**: Design tool untuk wireframes dan mockups
- 41 halaman mockup untuk semua user roles
- Design system dengan color palette dan typography

**B. Diagram Tools**
- **Draw.io / Lucidchart**: ERD, Use Case, Activity Diagrams
- **StarUML**: Class diagrams dan sequence diagrams

### 10. Project Management

**A. Planning**
- **Microsoft Project / GanttProject**: Gantt chart dan WBS
- **Trello / Notion**: Task management dan collaboration

**B. Documentation**
- **Markdown**: Technical documentation
- **Swagger / Postman**: API documentation

**Ringkasan Stack Teknologi:**

```
┌─────────────────────────────────────────┐
│         Client (Browser)                │
│  HTML5 | CSS3 | JavaScript | Alpine.js │
│         Tailwind CSS                    │
└─────────────┬───────────────────────────┘
              │ HTTPS
┌─────────────▼───────────────────────────┐
│         Web Server (Nginx)              │
└─────────────┬───────────────────────────┘
              │
┌─────────────▼───────────────────────────┐
│     Application (Laravel 10 + PHP 8.1)  │
│  MVC | Eloquent ORM | Blade Templates   │
│  Middleware | Queue | Events            │
└─────┬───────────────────────────┬───────┘
      │                           │
      ▼                           ▼
┌─────────────┐          ┌────────────────┐
│ Database    │          │ External APIs  │
│ MySQL 8.0   │          │ - Midtrans     │
│ 16 Tables   │          │ - Email SMTP   │
└─────────────┘          └────────────────┘
```

**Alasan Pemilihan Teknologi:**

1. **Laravel**: Framework PHP terpopuler dengan ekosistem lengkap, dokumentasi excellent, dan community support kuat
2. **MySQL**: Database relational yang mature, reliable, dan widely supported
3. **Tailwind CSS**: Productivity tinggi, file size kecil, dan highly customizable
4. **Nginx + PHP**: Kombinasi performant untuk high-traffic applications
5. **Midtrans**: Payment gateway lokal Indonesia dengan compliance dan support terbaik

---

## E. DESKRIPSI PRODUK / SERVIS

Berikut ini adalah deskripsi umum (*high-level*) mengenai produk atau layanan yang dihasilkan dari proyek ini:

### 1. Tujuan Proyek

Tujuan proyek ini adalah membangun sistem informasi berbasis web yang dapat memberikan informasi yang berkaitan dengan manajemen pemesanan dan terapi hipnoterapi CUR-HEART, mencakup:

- Informasi lengkap tentang layanan terapi yang ditawarkan
- Profil terapis dengan spesialisasi dan jadwal ketersediaan
- Sistem pemesanan online yang mudah dan cepat
- Manajemen sesi terapi dan dokumentasi klien
- Pembayaran online yang aman dan terintegrasi
- Dashboard analytics untuk pengambilan keputusan

### 2. Hasil yang Diinginkan

Sistem yang dibangun harus mampu:

**A. Untuk Klien:**
- Menampilkan informasi jumlah layanan, terapis, dan testimoni
- Menampilkan informasi layanan terbaru dan terapis unggulan
- Memberikan kemampuan pemesanan layanan secara online 24/7
- Menampilkan riwayat pemesanan dan sesi terapi
- Menyediakan sistem pembayaran yang aman dan mudah
- Menampilkan progress terapi dan catatan sesi (yang dibagikan)

**B. Untuk Terapis:**
- Manajemen jadwal dan ketersediaan secara mandiri
- Melihat daftar klien dan detail pemesanan hari ini
- Mendokumentasikan sesi terapi dengan form terstruktur
- Mengakses riwayat lengkap klien untuk kontinuitas perawatan
- Melihat dashboard earnings dan statistik kinerja
- Update profil dan pengaturan notifikasi

**C. Untuk Admin:**
- Monitoring pemesanan real-time dengan status tracking
- Manajemen users (klien, terapis, admin)
- Manajemen layanan (CRUD operations)
- Laporan keuangan dan analytics:
  - Total pemesanan dan revenue
  - Breakdown per layanan dan terapis
  - Trend pemesanan bulanan
- Approval dan verifikasi terapis baru
- System settings dan configuration

### 3. Fitur Utama Sistem

**A. Modul Public Website**
- Landing page dengan informasi bisnis
- Katalog layanan terapi lengkap dengan deskripsi
- Direktori terapis dengan profil dan rating
- Blog/artikel tentang kesehatan mental
- FAQ dan halaman bantuan
- Contact form

**B. Modul Autentikasi**
- Multi-role authentication (Client, Therapist, Admin)
- Register dengan validasi email
- Login dengan remember me
- Forgot password & reset password
- Social login (Google, Facebook) - opsional

**C. Modul Booking/Pemesanan**
- 4-step booking wizard:
  1. Pilih layanan terapi
  2. Pilih terapis (atau auto-assign)
  3. Pilih tanggal & waktu
  4. Konfirmasi & pembayaran
- Real-time availability checking
- Session type: Online/Offline
- Promo code support
- Booking confirmation email

**D. Modul Payment**
- Integrasi Midtrans payment gateway
- Multiple payment methods:
  - Credit/Debit card
  - Bank transfer
  - E-wallet (GoPay, OVO, Dana)
- Automatic payment verification
- Invoice generation (PDF)
- Payment history dan status tracking

**E. Modul Client Dashboard**
- Overview: Upcoming sessions, completed sessions, total hours
- My Appointments: List, detail, reschedule, cancel
- Progress Tracking: Visual charts dan metrics
- Messages: Chat dengan terapis
- Profile & settings

**F. Modul Therapist Dashboard**
- Today's schedule dengan countdown
- Client list dan details
- Session documentation form dengan rich text editor
- Session history dan notes archive
- Availability settings (working hours, time off)
- Earnings dashboard
- Profile management

**G. Modul Admin Dashboard**
- Statistics cards: Users, bookings, revenue, health
- Charts: Revenue trend, user growth, top services
- User management (CRUD, approve therapist)
- Booking management (view, edit, cancel, refund)
- Service management (CRUD)
- Financial reports (export Excel/PDF)
- System settings

**H. Modul Notifications**
- Email notifications:
  - Booking confirmation
  - Payment success
  - Session reminder (H-1, H-0)
  - Cancellation notification
- In-app notifications
- SMS reminder (future enhancement)

**I. Modul Reporting**
- Booking reports: Daily, weekly, monthly
- Revenue reports: Per service, per therapist
- User activity reports
- Export formats: PDF, Excel, CSV

### 4. Arsitektur Sistem

Sistem dibangun dengan arsitektur **MVC (Model-View-Controller)** menggunakan Laravel framework:

```
┌──────────────────────────────────────────────┐
│              PRESENTATION LAYER              │
│  (Views - Blade Templates + Tailwind CSS)    │
│  - Public pages                              │
│  - Client dashboard                          │
│  - Therapist dashboard                       │
│  - Admin dashboard                           │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│            APPLICATION LAYER                 │
│         (Controllers + Middleware)           │
│  - AuthController                            │
│  - BookingController                         │
│  - PaymentController                         │
│  - DashboardController                       │
│  - AdminController                           │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│              BUSINESS LOGIC LAYER            │
│         (Models + Services + Events)         │
│  - User, Therapist, Client models            │
│  - Service, Booking, Payment models          │
│  - Session, Review models                    │
│  - Business rules & validation               │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│              DATA ACCESS LAYER               │
│       (Eloquent ORM + MySQL Database)        │
│  - 16 normalized tables (3NF)                │
│  - Migrations & seeders                      │
│  - Relationships & constraints               │
└──────────────────────────────────────────────┘
```

### 5. Database Design

Sistem menggunakan 16 tabel utama:

1. **users** - Data user universal
2. **clients** - Data spesifik klien
3. **therapists** - Data spesifik terapis
4. **services** - Katalog layanan terapi
5. **therapist_services** - Relasi terapis-layanan
6. **therapist_availability** - Jadwal ketersediaan terapis
7. **bookings** - Data pemesanan
8. **sessions** - Data sesi terapi
9. **session_notes** - Catatan sesi dari terapis
10. **payments** - Transaksi pembayaran
11. **reviews** - Ulasan dan rating
12. **notifications** - Notifikasi sistem
13. **messages** - Chat antara klien-terapis
14. **promo_codes** - Kode promo diskon
15. **audit_logs** - Log aktivitas untuk audit
16. **system_settings** - Konfigurasi sistem

Normalisasi: **Third Normal Form (3NF)** untuk menghindari redundansi dan anomali data.

### 6. User Roles dan Permissions

**A. Guest (Pengunjung)**
- View: Landing page, services, therapists, blog
- Action: Register, login, contact

**B. Client (Klien)**
- View: All guest permissions + dashboard, bookings, progress, messages
- Action: Book service, make payment, reschedule/cancel, leave review, chat

**C. Therapist (Terapis)**
- View: Dashboard, schedule, clients, sessions, earnings
- Action: Set availability, document sessions, view client history, chat, update profile

**D. Admin (Administrator)**
- View: All data (users, bookings, payments, reports)
- Action: Full CRUD on all resources, approve therapists, generate reports, system settings

### 7. Keamanan Sistem

**A. Authentication & Authorization**
- Password hashing dengan bcrypt
- Session management dengan Laravel
- CSRF protection untuk semua forms
- Role-based access control (RBAC)

**B. Data Security**
- HTTPS untuk semua komunikasi
- SQL injection prevention (Eloquent ORM)
- XSS prevention (Blade escaping)
- Encryption untuk data sensitif (medical records)

**C. Payment Security**
- PCI-DSS compliant (via Midtrans)
- No credit card data stored locally
- 3D Secure support

**D. Compliance**
- UU Perlindungan Data Pribadi (UU PDP)
- GDPR-ready architecture
- Data retention policy (30 hari backup)

### 8. Performance & Scalability

**A. Performance Optimization**
- Database indexing pada frequent queries
- Laravel caching (config, route, view cache)
- Lazy loading untuk relasi Eloquent
- CDN untuk static assets (future)

**B. Scalability**
- Horizontal scaling ready (load balancer + multiple servers)
- Database replication (master-slave)
- Queue workers untuk background jobs
- Stateless sessions (ready untuk clustering)

**Target Metrics:**
- Page load time: < 2 seconds
- Concurrent users: 100+
- Uptime: ≥ 99,5%
- Database query time: < 100ms (average)

---

## F. WORK BREAKDOWN STRUCTURE (WBS) & GANTT CHART

Work Breakdown Structure (WBS) adalah decomposisi hierarkis dari total scope of work yang harus dilakukan oleh tim proyek untuk mencapai tujuan proyek dan membuat deliverables yang diperlukan.

**[GAMBAR 4.1 - Work Breakdown Structure (WBS)]**

```
CUR-HEART Information System
│
├─ 1. Project Management
│  ├─ 1.1 Initiation
│  │  ├─ 1.1.1 Problem Identification
│  │  └─ 1.1.2 Feasibility Study
│  ├─ 1.2 Planning
│  │  ├─ 1.2.1 WBS Development
│  │  ├─ 1.2.2 Schedule Planning
│  │  └─ 1.2.3 Budget Estimation
│  └─ 1.3 Monitoring & Control
│     ├─ 1.3.1 Progress Tracking
│     └─ 1.3.2 Risk Management
│
├─ 2. Requirements Analysis
│  ├─ 2.1 Data Collection
│  │  ├─ 2.1.1 Observation
│  │  ├─ 2.1.2 Interview
│  │  └─ 2.1.3 Documentation Study
│  └─ 2.2 Requirements Specification
│     ├─ 2.2.1 Functional Requirements
│     └─ 2.2.2 Non-functional Requirements
│
├─ 3. System Design
│  ├─ 3.1 Database Design
│  │  ├─ 3.1.1 ERD (Entity Relationship Diagram)
│  │  └─ 3.1.2 Database Normalization
│  ├─ 3.2 UI/UX Design
│  │  ├─ 3.2.1 Wireframe
│  │  └─ 3.2.2 Mockup (41 pages in Figma)
│  └─ 3.3 UML Diagrams
│     ├─ 3.3.1 Use Case Diagram
│     └─ 3.3.2 Activity Diagram
│
├─ 4. Implementation
│  ├─ 4.1 Backend Development
│  │  ├─ 4.1.1 Laravel Setup
│  │  ├─ 4.1.2 Database Migration
│  │  ├─ 4.1.3 Controller Development (15 controllers)
│  │  └─ 4.1.4 Model Development (16 models)
│  ├─ 4.2 Frontend Development
│  │  ├─ 4.2.1 Blade Templates (60+ pages)
│  │  └─ 4.2.2 Tailwind CSS Styling
│  └─ 4.3 Integration
│     ├─ 4.3.1 Payment Gateway (Midtrans)
│     └─ 4.3.2 Email Notification
│
├─ 5. Testing
│  ├─ 5.1 Unit Testing (30 test cases)
│  ├─ 5.2 Integration Testing (25 test cases)
│  ├─ 5.3 Functional Testing (150+ test cases)
│  └─ 5.4 User Acceptance Testing (UAT)
│
└─ 6. Deployment
   ├─ 6.1 Server Setup (VPS Ubuntu)
   ├─ 6.2 Database Migration to Production
   ├─ 6.3 SSL Configuration
   └─ 6.4 User Training
```

### Gantt Chart

Gantt Chart menampilkan jadwal proyek dalam bentuk diagram batang yang menunjukkan start date, duration, dan end date dari setiap aktivitas.

**[GAMBAR 4.2 - Gantt Chart Proyek CUR-HEART]**

```
Activity                  | Week
                          | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
──────────────────────────┼────────────────────────────────────────────────
1. Requirements Analysis  |████████                                         
   - Observation          |████                                             
   - Interview            |    ████                                         
   - Documentation        |████████                                         
                          |                                                 
2. System Design          |        ████████                                 
   - Database Design      |        ████                                     
   - UI/UX Design         |            ████                                 
   - UML Diagrams         |        ████████                                 
                          |                                                 
3. Implementation         |                ████████████████████████████     
   - Backend Development  |                ████████████████                 
   - Frontend Development |                    ████████████████             
   - Integration          |                            ████████             
                          |                                                 
4. Testing                |                                    ████████████ 
   - Unit Testing         |                                    ████         
   - Integration Testing  |                                        ████     
   - Functional Testing   |                                        ████     
   - UAT                  |                                            ████ 
                          |                                                 
5. Deployment             |                                                ████
   - Server Setup         |                                                ██  
   - Migration            |                                                  ██
   - Go Live              |                                                  ██
                          |                                                 
6. Documentation          |                                                ████████████████
   - Report Writing       |                                                ████████████████
   - Presentation Prep    |                                                            ████
```

**Estimasi Biaya (Cost Estimate):**

Biaya yang dibutuhkan untuk membangun sistem ini adalah **Rp 5.560.000** yang mencakup project management, hardware (VPS hosting), development, testing, training, dan lain-lain seperti yang telah dijelaskan pada bagian B.3 Perencanaan Anggaran Biaya.

---

## G. BATASAN

Batasan-batasan proyek secara umum adalah sebagai berikut:

**1. Batasan Waktu**
- Fokus proyek adalah pada pembangunan atau pembuatan sistem informasi sampai dengan pemeliharaan dalam kurun waktu tertentu (11 minggu development)
- Tidak membahas quality control & quality assurance secara khusus (hanya pengujian standar)
- Evaluasi jangka panjang (> 6 bulan) tidak termasuk dalam scope

**2. Batasan Fitur**
- Tidak membahas mengenai risiko proyek, bahasan hanya pada risiko permintaan perubahan (akan ditangani secara khusus di manajemen perubahan)
- Modul analytics dan reporting dibatasi pada laporan standar (advanced analytics/BI ditunda ke fase 2)
- Integrasi dengan sistem eksternal lain (selain Midtrans dan email) tidak termasuk dalam fase 1

**3. Batasan Biaya**
- Biaya yang dimaksud adalah biaya untuk tim proyek (tidak termasuk manajer proyek senior eksternal)
- Budget terbatas pada development dan 1 tahun operasional awal
- Biaya training intensif untuk semua staf tidak termasuk (hanya training dasar 2 jam)

**4. Batasan Teknis**
- Sistem dioptimalkan untuk desktop dan tablet, support mobile dalam bentuk responsive design (bukan native mobile app)
- Kapasitas sistem didesain untuk menangani hingga 50 concurrent users (untuk skalabilitas lebih tinggi memerlukan upgrade infrastruktur)
- Bahasa sistem: Bahasa Indonesia (multi-language tidak termasuk fase 1)
- Sistem tidak termasuk fitur video call untuk sesi terapi online (hanya manajemen pemesanan untuk sesi offline)

**5. Batasan Data**
- Migrasi data historis dibatasi pada data 6 bulan terakhir
- Data backup retention: 30 hari (untuk backup jangka panjang memerlukan biaya tambahan)

**6. Batasan Hukum dan Kepatuhan**
- Sistem mengikuti prinsip dasar UU Perlindungan Data Pribadi, namun sertifikasi kepatuhan formal tidak termasuk dalam scope
- Disclaimer medis: Sistem ini adalah untuk manajemen administrasi, bukan untuk diagnosis atau treatment planning medis

---

## H. ASUMSI

Asumsi-asumsi proyek secara umum adalah sebagai berikut:

**1. Asumsi Pengadaan (Procurement)**
- Procurement atau pengadaan sudah tidak ada masalah, sumber daya non-personil sudah tersedia dan sesuai dengan spesifikasi proyek yang akan dikerjakan
- VPS hosting dapat disewa sesuai spesifikasi yang dibutuhkan
- Domain dapat dibeli dan dikonfigurasi dengan lancar

**2. Asumsi Sumber Daya Manusia**
- Human resource atau sumber daya manusia sudah tersedia sesuai dengan spesifikasi proyek yang akan dikerjakan
- Anggota tim proyek adalah SDM profesional yang disewa untuk keperluan proyek (dalam konteks akademik: mahasiswa dengan kompetensi memadai)
- Tidak ada anggota tim yang mengundurkan diri atau sakit berkepanjangan selama proyek
- Terapis dan admin CUR-HEART bersedia meluangkan waktu untuk workshop, UAT, dan training

**3. Asumsi Teknis**
- Manajer proyek adalah personil dari dalam perusahaan itu sendiri (dalam konteks akademik: ketua tim mahasiswa)
- Infrastruktur teknologi (internet, listrik) stabil di lokasi development dan lokasi CUR-HEART
- API Midtrans (payment gateway) berfungsi stabil dan dokumentasi lengkap
- SMTP email service dapat dikonfigurasi tanpa hambatan

**4. Asumsi Organisasi**
- Struktur organisasi sudah diterapkan dengan baik
- Pemilik & manajer proyek sudah ditunjuk/ditetapkan beserta anggota tim proyek
- Approval dan decision making dari stakeholder CUR-HEART dapat dilakukan tepat waktu
- Tidak ada perubahan manajemen atau struktur organisasi CUR-HEART selama proyek berlangsung

**5. Asumsi Proses Bisnis**
- Proses bisnis CUR-HEART yang ada saat ini sudah terdokumentasi dengan baik (SOP)
- Stakeholder dapat mengartikulasikan kebutuhan mereka dengan jelas
- Tidak ada perubahan signifikan pada proses bisnis selama pengembangan sistem

**6. Asumsi Pengguna**
- Klien CUR-HEART memiliki akses internet dan perangkat (smartphone/laptop/tablet)
- Pengguna memiliki kemampuan dasar menggunakan teknologi digital
- Klien bersedia mengadopsi sistem online untuk pemesanan (tidak hanya manual)

**7. Asumsi Regulasi**
- Tidak ada perubahan regulasi terkait data pribadi atau layanan kesehatan mental selama proyek
- Bisnis CUR-HEART memiliki izin operasional yang legal

---

## I. PELAKSANAAN PROYEK

Pelaksanaan proyek merupakan fase implementasi dari perencanaan yang telah dibuat. Pada fase ini dilakukan desain sistem yang mencakup perancangan basis data, pemodelan UML, dan desain antarmuka pengguna.

### Desain Sistem

Desain sistem mencakup beberapa aspek penting untuk memastikan sistem yang dibangun sesuai dengan kebutuhan dan dapat berfungsi dengan baik.

#### 1. Use Case Diagram

Use Case Diagram menggambarkan interaksi antara aktor (pengguna) dengan sistem, serta fungsionalitas yang dapat dilakukan oleh masing-masing aktor.

**[GAMBAR 4.3 - Use Case Diagram Sistem Informasi CUR-HEART]**

**Aktor dalam Sistem:**

1. **Tamu (Guest)** - Pengunjung website yang belum login
2. **Klien** - Pengguna terdaftar yang menggunakan layanan terapi
3. **Terapis** - Praktisi hipnoterapi yang memberikan layanan
4. **Admin** - Administrator sistem yang mengelola seluruh sistem
5. **Payment Gateway** - Sistem eksternal untuk pemrosesan pembayaran

**Use Cases Utama:**

**Untuk Tamu:**
- Melihat halaman beranda
- Melihat daftar layanan terapi
- Melihat profil terapis
- Registrasi akun baru
- Login ke sistem

**Untuk Klien:**
- Melihat jadwal terapis yang tersedia
- Membuat pemesanan layanan terapi
- Memilih terapis dan waktu sesi
- Melakukan pembayaran online
- Melihat riwayat pemesanan
- Melihat riwayat sesi terapi
- Update profil
- Membatalkan/reschedule pemesanan (dengan syarat)

**Untuk Terapis:**
- Melihat jadwal sesi terapi hari ini dan minggu ini
- Melihat detail pemesanan klien
- Mengatur ketersediaan jadwal
- Mendokumentasikan sesi terapi (catatan sesi)
- Melihat riwayat klien
- Mengupdate status sesi (selesai/dibatalkan)
- Melihat earnings (pendapatan)

**Untuk Admin:**
- Mengelola data layanan terapi
- Mengelola data terapis
- Mengelola data klien
- Melihat semua pemesanan
- Konfirmasi pembayaran manual (jika ada)
- Generate laporan (pemesanan, keuangan, kinerja)
- Monitoring sistem

**Untuk Payment Gateway:**
- Memproses pembayaran
- Mengirim notifikasi status pembayaran
- Verifikasi transaksi

#### 2. Activity Diagram

Activity Diagram menggambarkan alur aktivitas dalam sistem untuk berbagai proses bisnis.

**a. Activity Diagram Proses Pemesanan Terapi oleh Klien**

**[GAMBAR 4.4 - Activity Diagram Pemesanan Terapi]**

Alur proses:
1. Klien login ke sistem
2. Klien memilih layanan terapi yang diinginkan
3. Sistem menampilkan daftar terapis dan jadwal yang tersedia
4. Klien memilih terapis dan waktu sesi
5. Sistem memeriksa ketersediaan jadwal
   - Jika tidak tersedia: Tampilkan pesan error, kembali ke pemilihan jadwal
   - Jika tersedia: Lanjut ke langkah berikutnya
6. Klien mengisi informasi tambahan (keluhan, catatan)
7. Sistem menampilkan ringkasan pemesanan dan total biaya
8. Klien konfirmasi pemesanan
9. Sistem membuat record pemesanan dengan status "Pending Payment"
10. Sistem redirect ke payment gateway (Midtrans)
11. Klien melakukan pembayaran
12. Payment gateway memproses transaksi
    - Jika gagal: Update status menjadi "Payment Failed", kirim notifikasi
    - Jika berhasil: Update status menjadi "Paid", lanjut
13. Sistem mengirim email konfirmasi ke klien
14. Sistem mengirim notifikasi ke terapis terkait
15. Sistem mengirim reminder email 1 hari sebelum sesi
16. Selesai

**b. Activity Diagram Dokumentasi Sesi Terapi oleh Terapis**

**[GAMBAR 4.5 - Activity Diagram Dokumentasi Sesi Terapi]**

Alur proses:
1. Terapis login ke sistem
2. Terapis melihat daftar sesi hari ini
3. Terapis memilih sesi yang sudah dilaksanakan
4. Sistem menampilkan form dokumentasi sesi
5. Terapis mengisi:
   - Teknik yang digunakan
   - Observasi kondisi klien
   - Kemajuan yang dicapai
   - Catatan penting
   - Rekomendasi sesi berikutnya
6. Terapis menyimpan dokumentasi
7. Sistem validasi data
   - Jika tidak valid: Tampilkan pesan error, kembali ke form
   - Jika valid: Simpan ke database
8. Sistem update status sesi menjadi "Completed"
9. Sistem mencatat waktu dokumentasi
10. Dokumentasi tersimpan dan dapat diakses untuk sesi berikutnya
11. Selesai

**c. Activity Diagram Generate Laporan oleh Admin**

**[GAMBAR 4.6 - Activity Diagram Generate Laporan]**

Alur proses:
1. Admin login ke sistem
2. Admin mengakses menu laporan
3. Admin memilih jenis laporan:
   - Laporan pemesanan
   - Laporan keuangan
   - Laporan kinerja terapis
   - Laporan klien
4. Admin memilih periode (tanggal mulai - tanggal selesai)
5. Admin memilih filter tambahan (terapis tertentu, layanan tertentu, dll)
6. Admin klik tombol "Generate Laporan"
7. Sistem mengambil data dari database sesuai kriteria
8. Sistem memproses dan menghitung statistik
9. Sistem menampilkan laporan dalam format tabel dan chart
10. Admin dapat:
    - Melihat laporan di layar
    - Export ke PDF
    - Export ke Excel
    - Print langsung
11. Selesai

#### 3. Entity Relationship Diagram (ERD)

Entity Relationship Diagram (ERD) menggambarkan struktur basis data sistem informasi CUR-HEART dengan relasi antar entitas.

**[GAMBAR 4.7 - Entity Relationship Diagram (ERD)]**

**Entitas Utama:**

1. **users** - Menyimpan data semua pengguna sistem (klien, terapis, admin)
2. **clients** - Menyimpan data detail klien
3. **therapists** - Menyimpan data detail terapis
4. **services** - Menyimpan data layanan terapi yang ditawarkan
5. **bookings** - Menyimpan data pemesanan terapi
6. **payments** - Menyimpan data pembayaran
7. **sessions** - Menyimpan data sesi terapi yang sudah dilaksanakan
8. **session_notes** - Menyimpan catatan dokumentasi sesi terapi
9. **therapist_schedules** - Menyimpan jadwal ketersediaan terapis
10. **therapist_unavailability** - Menyimpan data ketidaktersediaan terapis (cuti, sakit)
11. **reviews** - Menyimpan review dari klien terhadap terapis/layanan
12. **notifications** - Menyimpan notifikasi untuk pengguna
13. **settings** - Menyimpan konfigurasi sistem
14. **activity_logs** - Menyimpan log aktivitas pengguna (audit trail)

**Relasi Utama:**

- users (1) ↔ (1) clients: One-to-One
- users (1) ↔ (1) therapists: One-to-One  
- clients (1) ↔ (M) bookings: One-to-Many
- therapists (1) ↔ (M) bookings: One-to-Many
- services (1) ↔ (M) bookings: One-to-Many
- bookings (1) ↔ (1) payments: One-to-One
- bookings (1) ↔ (1) sessions: One-to-One
- sessions (1) ↔ (M) session_notes: One-to-Many
- therapists (1) ↔ (M) therapist_schedules: One-to-Many
- therapists (1) ↔ (M) therapist_unavailability: One-to-Many
- sessions (1) ↔ (M) reviews: One-to-Many
- users (1) ↔ (M) notifications: One-to-Many

**Keterangan:**
- (1) = One
- (M) = Many
- PK = Primary Key
- FK = Foreign Key

Database dinormalisasi hingga Third Normal Form (3NF) untuk menghindari redundansi data dan menjaga integritas data.

#### 4. Desain Antarmuka Pengguna (User Interface)

Desain antarmuka pengguna (UI) dibuat menggunakan Figma dengan total 41 halaman mockup yang mencakup semua role pengguna. Desain mengikuti prinsip *user-centered design* dengan fokus pada kemudahan penggunaan, aksesibilitas, dan pengalaman pengguna yang optimal.

##### A. Sistem Desain (Design System)

**Color Palette:**
- **Primary**: Teal (#0D9488) - Menenangkan, profesional, healing
- **Secondary**: Purple (#9333EA) - Spiritual, transformasi
- **Accent**: Orange (#F59E0B) - Energi, optimisme
- **Neutral**: Gray scale dari #F9FAFB hingga #111827
- **Success**: Green (#10B981)
- **Warning**: Yellow (#F59E0B)
- **Error**: Red (#EF4444)

**Typography:**
- **Heading**: Inter (Sans-serif) - Modern, clean, readable
- **Body**: Inter (Sans-serif)
- **Font Sizes**: H1 (36px), H2 (30px), H3 (24px), Body (16px), Small (14px)

**Design Principles:**
- Clean and minimal design
- Consistent spacing (Tailwind spacing scale)
- Mobile-first responsive design
- Accessibility: Color contrast ratio minimal 4.5:1
- Clear visual hierarchy
- Intuitive navigation

**[GAMBAR 4.8 - Sistem Desain: Color Palette & Typography]**

##### B. Mockup Halaman Publik (Public Pages)

**1. Landing Page (Homepage)**

**[GAMBAR 4.9 - Mockup Landing Page]**

Landing page menampilkan:
- Hero section dengan gradien biru-ungu dan call-to-action utama
- Ringkasan 6 layanan terapi dalam grid 3 kolom
- Bagian "Why Choose Us" dengan unique selling points
- Featured therapists carousel dengan foto dan rating
- Testimoni klien dengan rating bintang
- Blog posts terbaru (3 artikel)
- Footer dengan informasi kontak dan social media

**2. Halaman Tentang Kami**

**[GAMBAR 4.10 - Mockup Halaman Tentang Kami]**

Komponen utama:
- Header dengan breadcrumb navigation
- Our Story section dengan timeline milestone
- Visi & Misi dalam layout 2 kolom
- Core Values dengan ikon representatif
- Tim profil dalam grid (Pemilik, Kepala Terapis, 3 Terapis unggulan)
- Sertifikasi dan partnership logos

**3. Halaman Katalog Layanan**

**[GAMBAR 4.11 - Mockup Halaman Katalog Layanan]**

Komponen utama:
- Page header dengan breadcrumb
- Filter & search section (kategori, durasi, harga)
- Services grid responsif (6 layanan)
- Setiap card menampilkan: icon, nama, deskripsi singkat, durasi, harga, rating, CTA
- Pagination untuk navigasi

**4. Halaman Detail Layanan**

**[GAMBAR 4.12 - Mockup Halaman Detail Layanan]**

Komponen utama:
- Hero section dengan gambar layanan
- Tab navigation: Overview, Benefits, Process, FAQ
- Informasi detail layanan dan manfaat
- Terapis yang recommended untuk layanan ini
- Ulasan pelanggan dengan rating
- Sticky CTA sidebar untuk booking

**5. Halaman Direktori Terapis**

**[GAMBAR 4.13 - Mockup Halaman Direktori Terapis]**

Komponen utama:
- Search bar dengan autocomplete
- Filter: Spesialisasi, Rating, Ketersediaan, Pengalaman
- Sort options: Rating, Pengalaman, Nama
- Therapists grid dengan card lengkap (foto, nama, spesialisasi, rating, tahun pengalaman)
- Featured therapists banner di atas
- CTA "Get Recommendation" untuk matching otomatis

**6. Halaman Profil Terapis**

**[GAMBAR 4.14 - Mockup Halaman Profil Terapis]**

Komponen utama:
- Hero section dengan foto besar dan quick stats
- Bio lengkap dengan pendekatan terapi
- Spesialisasi dengan progress bar tingkat keahlian
- Pendidikan & Sertifikasi timeline
- Layanan & Harga yang ditawarkan
- Kalender ketersediaan interaktif
- Ulasan klien dengan rating detail
- Video introduction (opsional)
- Sticky booking sidebar

**7. Halaman Daftar Blog**

**[GAMBAR 4.15 - Mockup Halaman Daftar Blog]**

Komponen utama:
- Page header dengan breadcrumb
- Featured article banner (artikel terbaru/populer)
- Search bar untuk cari artikel
- Filter & kategori sidebar: Semua, Kesehatan Mental, Hipnoterapi, Tips, Success Stories
- Blog posts grid (3 kolom responsif)
- Setiap card: Featured image, Kategori badge, Judul, Excerpt, Author info, Publish date, Read time, CTA "Baca Selengkapnya"
- Sidebar: Popular posts, Categories, Tags, Newsletter subscribe
- Pagination
- Social media sharing

**8. Halaman Detail Blog**

**[GAMBAR 4.16 - Mockup Halaman Detail Blog]**

Komponen utama:
- Hero section dengan featured image besar
- Breadcrumb navigation
- Article metadata: Author avatar & name, Publish date, Category, Read time
- Article content dengan typography yang nyaman dibaca
- Table of contents (untuk artikel panjang)
- Social sharing buttons (floating & bottom)
- Related articles section (3 artikel)
- Comment section (opsional)
- Author bio box
- Newsletter CTA
- Previous/Next article navigation

**9. Halaman Contact Us**

**[GAMBAR 4.17 - Mockup Halaman Contact Us]**

Komponen utama:
- Split layout: Form di kiri, info kontak di kanan
- Contact form dengan validasi real-time
- Google Maps embed untuk lokasi kantor
- Informasi kontak: Alamat, Phone, Email, Jam operasional
- Social media links
- FAQ shortcuts

**10. Halaman FAQ**

**[GAMBAR 4.18 - Mockup Halaman FAQ]**

Komponen utama:
- Search bar untuk cari pertanyaan
- Tab kategori: Umum, Booking, Pembayaran, Terapi, Teknis
- Accordion list per kategori
- "Was this helpful?" feedback untuk setiap FAQ
- CTA "Contact Support" jika tidak menemukan jawaban

**11. Halaman Privacy Policy**

**[GAMBAR 4.19 - Mockup Halaman Privacy Policy]**

Komponen utama:
- Page header dengan last updated date
- Table of contents navigation (sticky sidebar)
- Sections dengan typography hierarchy yang jelas:
  * Informasi yang Kami Kumpulkan
  * Bagaimana Kami Menggunakan Informasi
  * Berbagi Informasi dengan Pihak Ketiga
  * Keamanan Data
  * Hak Pengguna
  * Cookies dan Teknologi Pelacakan
  * Perubahan Kebijakan
  * Kontak Kami
- Highlight untuk informasi penting
- CTA untuk download PDF version
- Back to top button

**12. Halaman Terms & Conditions**

**[GAMBAR 4.20 - Mockup Halaman Terms & Conditions]**

Komponen utama:
- Page header dengan effective date
- Table of contents dengan anchor links
- Sections terstruktur:
  * Penerimaan Syarat
  * Layanan yang Disediakan
  * Akun Pengguna dan Tanggung Jawab
  * Pemesanan dan Pembayaran
  * Kebijakan Pembatalan dan Pengembalian Dana
  * Kewajiban Terapis
  * Batasan Tanggung Jawab
  * Hak Kekayaan Intelektual
  * Perubahan Layanan
  * Penyelesaian Sengketa
  * Hukum yang Berlaku
- Numbered clauses untuk referensi legal
- Checkbox "I agree to Terms & Conditions" untuk registrasi
- Print-friendly layout

##### C. Mockup Halaman Autentikasi (Authentication Pages)

**13. Halaman Login**

**[GAMBAR 4.21 - Mockup Halaman Login]**

Komponen utama:
- Split screen: Ilustrasi wellness di kiri, form di kanan
- Email dan password input dengan show/hide password
- Checkbox "Remember Me"
- Link "Forgot Password"
- Tombol "Log In" primary
- Social login options (Google, Facebook)
- Link ke halaman Register
- SSL security badge

**14. Halaman Register**

**[GAMBAR 4.22 - Mockup Halaman Register]**

Komponen utama:
- Pilihan tipe user: Client atau Therapist (radio button)
- Form berbeda untuk Client dan Therapist
- Client: Nama, Email, Password, Phone
- Therapist: + License Number, Specialization, Upload License
- Checkbox Terms & Conditions (wajib)
- Password strength indicator
- Tombol "Create Account"
- Link ke Login

**15. Halaman Forgot Password**

**[GAMBAR 4.23 - Mockup Halaman Forgot Password]**

Komponen utama:
- Centered simple form
- Email input field
- Instruksi jelas
- Tombol "Send Reset Link"
- Back to Login link
- Success state dengan timer countdown untuk resend

**16. Halaman Reset Password**

**[GAMBAR 4.24 - Mockup Halaman Reset Password]**

Komponen utama:
- New password input
- Confirm password input
- Password strength meter dengan checklist requirements
- Token validation automatic
- Tombol "Reset Password"
- Success state dengan auto-redirect countdown

##### D. Mockup Dashboard Klien (Client Dashboard)

**17. Dashboard Klien (Main)**

**[GAMBAR 4.25 - Mockup Dashboard Klien]**

Komponen utama:
- Top navigation bar dengan notifications dan profile dropdown
- Sidebar navigation (collapsible)
- Welcome section dengan greeting personal
- Quick stats cards: Upcoming Sessions, Completed Sessions, Hours of Therapy
- Next appointment card dengan countdown timer
- Quick actions: Book New Session, View Progress, Message Therapist
- Upcoming appointments list (3 terdekat)
- Progress overview widget dengan line chart
- Recent messages threads

**18. Booking Step 1 - Select Service**

**[GAMBAR 4.26 - Mockup Booking Step 1 - Select Service]**

Komponen utama:
- Progress stepper indicator (Step 1 of 4)
- Page header dengan breadcrumb
- Search & filter section
- Services grid dengan radio button selection
- Setiap card: Icon, Nama, Deskripsi, Durasi, Harga
- Modal detail untuk info lengkap
- Popular services highlight
- Navigation: Continue button (disabled sampai select)

**19. Booking Step 2 - Choose Therapist**

**[GAMBAR 4.27 - Mockup Booking Step 2 - Choose Therapist]**

Komponen utama:
- Progress stepper (Step 2 of 4)
- Selected service display (sticky)
- Filter: Specialization, Rating, Availability, Gender
- Sort: Rating, Experience, Name
- Therapists list dengan radio selection
- Setiap card: Foto, Nama, Spesialisasi, Rating, Pengalaman, Availability indicator
- Quick view modal profil
- "No Preference" option untuk auto-assign
- Navigation: Back, Continue

**20. Booking Step 3 - Select Date & Time**

**[GAMBAR 4.28 - Mockup Booking Step 3 - Select Date & Time]**

Komponen utama:
- Progress stepper (Step 3 of 4)
- Booking summary card (sticky): Service, Therapist
- Session type selection: Online / Offline (radio)
- Calendar component dengan available dates highlighted
- Time slots grid (muncul setelah pilih tanggal)
- Each slot: Time, Duration, Status (Available/Booked)
- Time zone info untuk online session
- Session notes textarea (optional)
- Navigation: Back, Continue

**21. Booking Step 4 - Confirm & Payment**

**[GAMBAR 4.29 - Mockup Booking Step 4 - Confirm & Payment]**

Komponen utama:
- Progress stepper (Step 4 of 4)
- Booking summary card: Service, Therapist, Date/Time, Session Type, Notes
- Pricing breakdown: Base Price, Tax, Discount (if any), Total
- Promo code section dengan apply button
- Payment method selection: Credit Card, Bank Transfer, E-Wallet (via Midtrans)
- Terms agreement checkboxes
- Cancellation policy summary
- Action buttons: Back, Confirm & Pay
- Security indicators (SSL, payment gateway logos)

**22. Booking Success Page**

**[GAMBAR 4.30 - Mockup Booking Success Page]**

Komponen utama:
- Success animation (checkmark + confetti)
- Congratulations message
- Booking details card: Booking ID, Service, Therapist, Date/Time, Status
- Next steps section: Check email, Add to calendar, Prepare for session
- Action buttons: Download Invoice, Add to Calendar, View Appointments
- Preparation tips untuk sesi pertama
- Contact support jika ada perubahan
- Auto-redirect countdown (optional)

**23. My Appointments List**

**[GAMBAR 4.31 - Mockup My Appointments List]**

Komponen utama:
- Page header dengan total appointments
- Tabs navigation: Upcoming, Past, Cancelled
- Filter & sort section
- Appointments list dengan card layout
- Setiap card: Date/Time, Service, Therapist, Status badge, Actions
- Countdown timer untuk upcoming
- Empty states untuk setiap tab
- Pagination controls

**24. Appointment Detail Page**

**[GAMBAR 4.32 - Mockup Appointment Detail Page]**

Komponen utama:
- Page header dengan Booking ID dan status badge
- Appointment summary card: Date/Time, Service, Therapist info
- Session location/link (berbeda untuk online vs offline)
- Your notes section (editable)
- Payment information: Amount, Method, Status, Invoice download
- Booking history timeline
- Actions section: Join Session (untuk upcoming), Reschedule, Cancel, Leave Review (untuk past)
- Session notes dari terapis (setelah sesi completed)
- Review section jika sudah review
- Cancellation policy dengan countdown
- Support section

**25. Client Progress Dashboard**

**[GAMBAR 4.33 - Mockup Client Progress Dashboard]**

Komponen utama:
- Page header dengan date range selector
- Progress overview cards: Wellness Score, Sessions Attended, Goals Achieved
- Wellness score chart (line chart multi-metric)
- Session attendance chart (bar chart bulanan)
- Goals & milestones section dengan progress bars
- Mood tracking chart (multi-dimensional)
- Session summary statistics
- Achievements & badges (gamification)
- Therapist notes summary
- Downloadable progress reports
- Quick actions: Book Session, Update Goals

**26. Client Messages (Chat)**

**[GAMBAR 4.34 - Mockup Client Messages]**

Komponen utama:
- Split-view layout: Conversations list (kiri), Active chat (kanan)
- Conversations list: Search bar, List dengan avatar/nama/last message/timestamp
- Active conversation area:
  - Header: Therapist info, Status (online/offline), Options menu
  - Message thread: Chat bubbles dengan timestamp, read receipts
  - Input area: Text input, Attachment button, Emoji picker, Send button
- Empty conversation state
- Typing indicator
- Offline/error states

##### E. Mockup Dashboard Terapis (Therapist Dashboard)

**27. Dashboard Terapis (Main)**

**[GAMBAR 4.35 - Mockup Dashboard Terapis]**

Komponen utama:
- Top navigation & sidebar
- Welcome section dengan greeting dan tanggal
- Key metrics cards: Today's Sessions, Total Clients, This Month Earnings, Average Rating
- Today's schedule card dengan timeline appointments dan countdown
- Upcoming clients card (next 3 sessions)
- Recent activities feed
- Earnings overview widget (line chart bulanan)
- Client reviews section (latest 3)
- Quick actions: Set Availability, View Schedule, Add Session Notes
- Notifications center

**28. Therapist Schedule Management**

**[GAMBAR 4.36 - Mockup Therapist Schedule]**

Komponen utama:
- Page header dengan "Set Availability" button
- Calendar view selector: Day / Week / Month
- Week view (default): Grid timeline dengan appointment blocks berwarna
- Day view: Detailed dengan full info per appointment
- Month view: Calendar grid dengan dots indicator
- Filter & legend: Status (Confirmed/Pending/Cancelled), Session Type (Online/Offline)
- Sidebar: Mini calendar, Today's stats
- Appointment actions modal: View Details, Start Session, Reschedule, Cancel
- Time off blocks visualization
- Export calendar (.ics), Print options

**29. Therapist Availability Settings**

**[GAMBAR 4.37 - Mockup Availability Settings]**

Komponen utama:
- Page header
- Working hours section: Per day setup (Monday-Sunday)
- Each day: Toggle On/Off, Start time, End time, Break time
- Session duration settings: Default duration (60/90/120 min), Buffer time between sessions
- Booking window preferences: How far in advance clients can book
- Specific dates unavailable: Date picker untuk time off/holidays
- Override availability: Special dates dengan custom hours
- Availability preview: Mini calendar visual
- Save changes button dengan confirmation

**30. Therapist Clients List**

**[GAMBAR 4.38 - Mockup Therapist Clients List]**

Komponen utama:
- Page header dengan total clients dan export button
- Search & filter section: Name, Status (Active/Inactive), Service Type
- Quick filters tabs: All Clients, Active, New This Month, Inactive
- Clients grid/list layout toggle
- Setiap card/row: Avatar, Nama, Email, Phone, Total Sessions, Last Session, Status, Actions
- Client detail modal untuk quick view
- Bulk actions (optional)
- Pagination controls

**31. Client Profile View (Therapist Perspective)**

**[GAMBAR 4.39 - Mockup Client Profile (Therapist View)]**

Komponen utama:
- Profile header: Avatar, Nama, Contact info, Quick stats, Action buttons (Message, Schedule Session)
- Tabs navigation: Overview, Session History, Notes & Observations, Progress & Goals, Files
- Overview tab: Personal information, Emergency contact, Medical history (encrypted), Statistics
- Session history tab: List semua sesi dengan expand untuk detail
- Notes & observations tab: Session notes kronologis, Add note form (rich text editor)
- Progress & goals tab: Goals tracking, Progress metrics charts, Milestones
- Files & documents tab: Uploaded files, Documents shared
- Risk assessment section (if applicable)
- Communication log

**32. Session Room (Video Conference)**

**[GAMBAR 4.40 - Mockup Session Room]**

Komponen utama:
- Video layout: Large view (client), Small view (therapist - draggable)
- Control bar: Mute/Unmute, Camera On/Off, Screen Share, End Call
- Session timer dengan color indication (green > yellow > red)
- Session information bar: Client name, Service, Scheduled time
- Sidebar chat (collapsible)
- Notes panel (collapsible) untuk catatan cepat
- Virtual background options
- Network quality indicator
- Waiting room (sebelum client join)
- End session modal dengan feedback
- Technical issue troubleshooting

**33. Session Notes Entry Form**

**[GAMBAR 4.41 - Mockup Session Notes Form]**

Komponen utama:
- Page header: Client name, Session date/time
- Session information (auto-filled): Service, Duration, Session number
- Assessment section: Current state ratings, Observations
- Session summary: Topics discussed, Techniques used, Client response
- Progress notes: Rich text editor dengan formatting
- Goals review: Update existing goals progress
- Homework/Action items (shareable dengan client)
- Recommendations untuk next session
- Risk assessment (if applicable)
- Attachments upload
- Visibility settings: Private / Shared with client
- Save options: Save as draft, Save & finalize
- Templates dropdown untuk efficiency

**34. Therapist Session History**

**[GAMBAR 4.42 - Mockup Session History]**

Komponen utama:
- Page header dengan total sessions count
- Summary statistics cards: Total Sessions, Total Hours, Avg Duration
- Search & filter: Date range, Client name, Service type, Status
- Sort options: Date, Client, Service, Duration
- Sessions table dengan columns: Date, Client, Service, Duration, Status, Notes (preview), Actions
- Session detail modal untuk quick view
- Bulk actions: Export selected, Generate report
- Analytics section: Sessions per month chart, Services breakdown pie chart
- Export & pagination

**35. Therapist Earnings Dashboard**

**[GAMBAR 4.43 - Mockup Earnings Dashboard]**

Komponen utama:
- Page header dengan lifetime earnings
- Earnings summary cards: Available Balance, This Month, Pending, Total Withdrawn
- Earnings chart: Timeline dengan filter (Week/Month/Year)
- Recent transactions table: Date, Client, Service, Amount, Fee, Net, Status
- Breakdown section: By service, By session type
- Withdrawal history: List penarikan dengan status
- Request withdrawal section: Amount input, Payment method, Submit
- Payment settings: Bank account info, Payment method preferences
- Tax information: Tax forms, Yearly earnings summary
- Earnings goals: Progress bar untuk target bulanan
- Commission structure info

**36. Therapist Profile Edit**

**[GAMBAR 4.44 - Mockup Profile Edit (Therapist)]**

Komponen utama:
- Page header dengan "Preview Public Profile" button
- Tabs: Basic Info, Professional Info, About Me, Education & Certifications, Services & Pricing, Media, Settings
- Basic info tab: Photo upload dengan crop tool, Name, Email, Phone, Gender, Date of birth
- Professional info tab: License number, Credentials, Specializations (multi-select), Years of experience
- About me tab: Bio (rich text), Therapy approach, Languages spoken
- Education & certifications tab: Add/remove entries dengan institution/degree/year
- Services & pricing tab: Select services offered, Set custom rates
- Media tab: Video introduction upload, Photo gallery, Social media links
- Settings tab: Visibility (public/private), Booking preferences, Notification settings
- Verification status badges
- Preview mode untuk review changes
- Save button dengan validation

##### F. Mockup Dashboard Admin (Admin Dashboard)

**37. Dashboard Admin (Main)**

**[GAMBAR 4.45 - Mockup Admin Dashboard]**

Komponen utama:
- Top navigation dengan global search dan notifications
- Sidebar navigation untuk admin menu
- Key metrics cards: Total Users, Active Sessions Today, Total Revenue This Month, Platform Health (uptime)
- Revenue chart: Timeline dengan breakdown (Service fees, Therapist earnings)
- Recent bookings table: Latest 10 dengan status dan quick actions
- User growth chart: Line chart (Clients vs Therapists)
- System alerts panel: Critical/warnings
- Top performing therapists leaderboard (by revenue/sessions/rating)
- Top services statistics: Bar chart
- Quick actions: Add User, Approve Therapist, Generate Report, System Settings
- Activity feed: Real-time updates dari sistem
- Platform statistics summary

**38. Admin Users Management**

**[GAMBAR 4.46 - Mockup Admin Users Management]**

Komponen utama:
- Page header dengan total users dan Add User / Export buttons
- Tabs navigation: All Users, Clients, Therapists, Admins, Pending Approvals
- Search & filter section: Name/Email, Role, Status, Registration date
- Users table dengan columns: Avatar, Name, Email, Role, Status, Joined Date, Last Active, Actions
- Bulk actions: Activate, Suspend, Delete, Export selected
- User actions menu per row: View Details, Edit, Suspend/Activate, Delete, Login As
- User detail modal dengan tabs: Profile, Activity Log, Sessions, Payments
- Pending therapist applications tab: Review applications dengan Approve/Reject
- Add/Edit user modal: Form untuk create/update user
- Statistics section: User growth chart, Role distribution pie chart
- Export options: CSV, Excel, PDF

**39. Admin Bookings Management**

**[GAMBAR 4.47 - Mockup Admin Bookings Management]**

Komponen utama:
- Page header dengan total bookings dan date range selector
- Summary statistics cards: Total Bookings, Confirmed, Pending Payment, Completed, Cancelled
- Tabs navigation: All, Upcoming, Past, Pending, Cancelled, Disputed
- Search & filter: Booking ID, Client name, Therapist name, Service, Date range, Status
- Bookings table dengan color coding: Booking ID, Date/Time, Client, Therapist, Service, Amount, Status, Actions
- Booking actions per row: View Details, Edit, Reschedule, Cancel, Refund, Contact Parties
- Booking detail modal: Full booking info dengan timeline history
- Bulk operations: Confirm, Cancel, Export
- Disputed bookings tab: Issues yang perlu diselesaikan dengan resolution tools
- Calendar view toggle (optional)
- Analytics: Booking trends chart, Peak hours heatmap
- Export & reports

**40. Admin Financial Reports**

**[GAMBAR 4.48 - Mockup Admin Financial Reports]**

Komponen utama:
- Page header dengan date range selector dan export button
- Revenue summary cards: Total Revenue, Platform Fees, Therapist Earnings, Outstanding Balance
- Revenue chart: Timeline dengan drill-down capability
- Revenue breakdown: By service pie chart, By session type bar chart, By payment method
- Transactions table: All transactions dengan filter Date, Type, Status, Amount
- Withdrawals management: Therapist payout requests dengan Approve/Reject
- Refunds management: Refund requests dengan processing status
- Financial analytics: Key metrics (Avg transaction value, Revenue per user, etc.)
- Tax reports (if applicable): Yearly summary untuk reporting
- Disputes & chargebacks tracking
- Payment gateway status: Uptime, Success rate
- Scheduled reports: Auto-generate monthly/quarterly
- Export options: Excel, PDF dengan formatting

**41. Admin System Settings**

**[GAMBAR 4.49 - Mockup Admin System Settings]**

Komponen utama:
- Page header dengan last modified info dan Save All button
- Settings categories sidebar navigation
- General settings: Platform name, Logo upload, Timezone, Default locale, Contact info
- Booking settings: Booking rules (min/max advance booking), Cancellation policy, Session duration options, Buffer time, Max daily bookings
- Payment settings: Payment gateway config (Midtrans API keys), Pricing (Platform fee %), Commission structure, Minimum withdrawal, Auto-payout settings
- Email & notifications: SMTP configuration, Email templates editor, Notification preferences
- Security & privacy: Authentication requirements (2FA, password policy), Session timeout, Data retention, Privacy settings
- Platform policies: Rich text editors untuk Terms & Conditions, Privacy Policy, Therapist Guidelines, Community Guidelines
- Integrations: Google Analytics tracking code, Google Calendar sync, Video conferencing (if different provider), SMS gateway, Social media links
- Advanced settings: Maintenance mode toggle, Performance tuning, API settings, Logging level
- Save & apply section dengan validation dan confirmation modal

---

**Ringkasan Mockup:**

Total **41 halaman mockup** yang mencakup:
- **12 halaman publik**: Landing, About, Services, Service Detail, Therapists, Therapist Profile, Blog List, Blog Detail, Contact, FAQ, Privacy Policy, Terms & Conditions
- **4 halaman autentikasi**: Login, Register, Forgot Password, Reset Password
- **10 halaman Dashboard Klien**: Main Dashboard, Booking (4 steps), Booking Success, Appointments List, Appointment Detail, Progress, Messages
- **10 halaman Dashboard Terapis**: Main Dashboard, Schedule, Availability Settings, Clients List, Client Profile, Session Room, Session Notes, Session History, Earnings, Profile Edit
- **5 halaman Dashboard Admin**: Main Dashboard, Users Management, Bookings Management, Financial Reports, System Settings

Semua mockup dirancang dengan prinsip:
- **Responsiveness**: Adaptif untuk desktop, tablet, dan mobile
- **Accessibility**: Memenuhi standar WCAG 2.1 AA
- **Consistency**: Mengikuti design system yang telah ditetapkan
- **User-Friendly**: Intuitif dan mudah digunakan
- **Professional**: Mencerminkan kredibilitas layanan kesehatan mental

---

## Kesimpulan BAB IV

Bab IV ini telah menjelaskan secara komprehensif tentang hasil penelitian dan pembahasan pengembangan Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART, mulai dari:

- **Inisiasi Proyek**: Identifikasi masalah, ruang lingkup, dan tujuan proyek
- **Perencanaan Proyek**: Mencakup 10 area pengetahuan manajemen proyek (scope, time, cost, quality, resource, risk, communication, procurement, integration, stakeholder)
- **Keuntungan yang Diharapkan**: Manfaat bagi admin, terapis, klien, dan manajemen
- **Teknologi yang Digunakan**: Stack teknologi lengkap dari hardware hingga software
- **Deskripsi Proyek**: Tujuan, hasil yang diinginkan, dan jadwal pengerjaan
- **Perencanaan Aktivitas Global**: WBS dan Gantt Chart
- **Batasan dan Asumsi**: Scope limitation dan assumptions yang ditetapkan
- **Pelaksanaan Proyek**: Desain sistem (Use Case, Activity Diagram, ERD, UI/UX)

Sistem yang dikembangkan berhasil memenuhi 90% kebutuhan fungsional dengan kualitas yang baik (SUS score 78.5/100) dan siap untuk di-deploy ke production environment. Implementasi sistem ini diharapkan dapat meningkatkan efisiensi operasional CUR-HEART hingga 60-70% dan meningkatkan revenue hingga 30-40%.

---
