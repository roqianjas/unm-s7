# BAB IV (Lanjutan)  
# HASIL PENELITIAN DAN PEMBAHASAN - PART 3

## 4.4. FAKTOR PENENTU KEBERHASILAN

Keberhasilan implementasi Sistem Informasi CUR-HEART ditentukan oleh berbagai faktor yang saling berkaitan. Faktor-faktor ini dibagi menjadi Faktor Kunci Keberhasilan (*Key Success Factors*/KSF), Faktor Kritis Keberhasilan (*Critical Success Factors*/CSF), dan Indikator Kinerja Utama (*Key Performance Indicators*/KPI).

### 4.4.1 Faktor Kunci Keberhasilan (*Key Success Factors*/KSF)

Faktor Kunci Keberhasilan adalah faktor-faktor kunci yang mendukung pencapaian tujuan proyek secara umum.

#### A. Faktor Teknologi

**1. Stabilitas dan Keandalan Sistem**
- Sistem harus mampu beroperasi 24/7 dengan uptime minimal 99,5%
- Waktu respons halaman tidak lebih dari 2 detik
- Optimasi query database untuk menangani concurrent users
- Backup otomatis harian untuk keamanan data

**2. Antarmuka yang Mudah Digunakan**
- Desain UI/UX yang intuitif dan mudah dipahami
- Responsive design untuk semua perangkat (desktop, tablet, mobile)
- Konsistensi bahasa desain menggunakan design system
- Standar aksesibilitas (WCAG 2.1 Level AA)

**3. Keamanan Data**
- Enkripsi data sensitif (password, medical records)
- HTTPS untuk semua komunikasi
- Autentikasi dan otorisasi yang kuat
- Kepatuhan terhadap UU PDP (Perlindungan Data Pribadi)

**4. Skalabilitas**
- Arsitektur yang dapat menangani pertumbuhan pengguna
- Normalisasi database untuk efisiensi storage
- Caching mechanism untuk optimasi performa

#### B. Faktor Manusia

**1. Kompetensi Tim Pengembang**
- Penguasaan Laravel framework dan PHP programming
- Pemahaman database design dan MySQL
- Kemampuan frontend development (HTML, CSS, JavaScript, Tailwind)
- Pengetahuan version control (Git)

**2. Komitmen Stakeholder**
- Dukungan penuh dari manajemen CUR-HEART
- Keterlibatan aktif pemilik dalam requirement gathering
- Feedback konstruktif dari terapis dan admin
- Kesediaan untuk testing dan UAT

**3. Tingkat Adopsi Pengguna**
- Pelatihan yang memadai untuk terapis dan admin
- User guide yang komprehensif
- Technical support yang responsif
- Change management yang efektif

#### C. Faktor Manajemen Proyek

**1. Perencanaan yang Matang**
- Scope yang jelas dan terukur
- Timeline yang realistis (11 minggu)
- Alokasi resource yang optimal
- Risk mitigation strategy yang efektif

**2. Komunikasi yang Efektif**
- Meeting rutin (weekly standup)
- Dokumentasi yang jelas
- Progress tracking dengan Gantt chart
- Issue tracking dan resolution

**3. Quality Assurance**
- Testing sistematis di setiap fase
- Code review dan pair programming
- Bug tracking dan prioritas fix
- Continuous improvement berdasarkan feedback

### 4.4.2 Faktor Kritis Keberhasilan (*Critical Success Factors*/CSF)

Faktor Kritis Keberhasilan adalah faktor-faktor yang **HARUS** dipenuhi agar proyek berhasil.

**CSF 1: Ketersediaan dan Keandalan Sistem**
- Target: Uptime ≥ 99,5%, Response time < 2 detik
- Dapat menangani minimal 100 concurrent users
- Zero data loss dalam kondisi normal

**CSF 2: Keamanan dan Privasi Data**
- Zero security breach atau unauthorized access
- Semua data sensitif terenkripsi
- HTTPS implementation untuk semua pages
- RBAC (Role-Based Access Control) berfungsi dengan baik

**CSF 3: Adopsi dan Kepuasan Pengguna**
- Minimal 70% klien menggunakan sistem untuk booking
- Skor kepuasan pengguna ≥ 4,0 dari 5,0
- System Usability Scale (SUS) Score ≥ 68
- Tingkat adopsi terapis 100%

**CSF 4: Integrasi dengan Proses Bisnis**
- 100% booking melalui sistem (tidak ada lagi manual)
- Pengurangan beban kerja administratif minimal 50%
- Pengurangan booking error hingga 90%
- Laporan dapat dihasilkan dalam 5 menit

**CSF 5: Kepatuhan Anggaran dan Timeline**
- Penyelesaian proyek dalam 11 minggu (± 1 minggu toleransi)
- Biaya aktual tidak melebihi 110% budget (Rp 5,5 juta)
- Semua deliverables selesai sesuai scope

### 4.4.3 Indikator Kinerja Utama (*Key Performance Indicators*/KPI)

KPI adalah metrik terukur untuk memantau keberhasilan sistem setelah deployment.

**Tabel 4.8 - Key Performance Indicators (KPI)**

| Kategori | Nama KPI | Target | Frekuensi Monitoring |
|----------|----------|--------|---------------------|
| **Kinerja Sistem** | Uptime Sistem | ≥ 99,5% | Real-time |
| | Response Time | ≤ 2 detik | Mingguan |
| | Error Rate | ≤ 0,5% | Harian |
| **Keamanan** | Security Vulnerabilities | 0 critical | Bulanan |
| | Data Breach Incidents | 0 | Real-time |
| **Adopsi Pengguna** | Total Registered Users | 200 dalam 3 bulan | Bulanan |
| | Monthly Active Users | 150 (75%) | Bulanan |
| | Booking Conversion Rate | ≥ 60% | Mingguan |
| **Transaksi** | Total Bookings/Month | 100 bookings | Bulanan |
| | Payment Success Rate | ≥ 95% | Mingguan |
| | Revenue/Month | Rp 30 juta | Bulanan |
| **Kepuasan** | User Satisfaction Score | ≥ 4,0/5,0 | Per booking |
| | Net Promoter Score | ≥ 30 | Triwulanan |
| | SUS Score | ≥ 68 | Triwulanan |
| **Efisiensi** | Avg Booking Time | ≤ 3 menit | Mingguan |
| | Admin Workload Reduction | ≥ 50% | Bulanan |
| | Report Generation Time | ≤ 5 menit | Bulanan |

---

## 4.5. KEUNTUNGAN YANG DIHARAPKAN

Implementasi Sistem Informasi CUR-HEART diharapkan memberikan berbagai keuntungan bagi pemangku kepentingan yang terlibat.

### 4.5.1 Manfaat untuk CUR-HEART (Organisasi)

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

### 4.5.2 Manfaat untuk Klien

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

### 4.5.3 Manfaat untuk Terapis

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

### 4.5.4 Analisis Return on Investment (ROI)

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

## 4.6. TEKNOLOGI YANG DIGUNAKAN

Teknologi yang digunakan untuk membangun Sistem Informasi CUR-HEART secara garis besar dapat dibagi ke dalam beberapa bagian berikut ini:

### 4.6.1 Server dan Infrastructure

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

**D. Version Control**
- **Git & GitHub**: Source code management dan collaboration

### 4.6.2 Backend Development

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

### 4.6.3 Frontend Development

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

### 4.6.4 Database Management

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

### 4.6.5 Integration & External Services

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

### 4.6.6 Development Tools

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

### 4.6.7 Testing

**A. Testing Framework**
- **PHPUnit**: Unit testing untuk backend logic
- **Laravel Dusk**: Browser automation testing
- Feature tests untuk API endpoints

**B. Code Quality**
- PHP Code Sniffer untuk coding standards
- Laravel Debugbar untuk development debugging
- Error tracking & monitoring

### 4.6.8 Deployment & DevOps

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

### 4.6.9 Design & Prototyping

**A. UI/UX Design**
- **Figma**: Design tool untuk wireframes dan mockups
- 41 halaman mockup untuk semua user roles
- Design system dengan color palette dan typography

**B. Diagram Tools**
- **Draw.io / Lucidchart**: ERD, Use Case, Activity Diagrams
- **StarUML**: Class diagrams dan sequence diagrams

### 4.6.10 Project Management

**A. Planning**
- **Microsoft Project / GanttProject**: Gantt chart dan WBS
- **Trello / Notion**: Task management dan collaboration

**B. Documentation**
- **Markdown**: Technical documentation
- **Swagger / Postman**: API documentation

### 4.6.11 Ringkasan Stack Teknologi

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

### 4.6.12 Alasan Pemilihan Teknologi

**Tabel 4.9 - Justifikasi Pemilihan Teknologi**

| Teknologi | Alasan Pemilihan |
|-----------|------------------|
| **Laravel 10** | Framework PHP terpopuler dengan ekosistem lengkap, dokumentasi excellent, community support kuat, dan fitur bawaan yang komprehensif |
| **MySQL 8.0** | Database relational yang mature, reliable, widely supported, dan gratis (open source) |
| **Tailwind CSS** | Productivity tinggi, file size kecil setelah purge, highly customizable, dan rapid prototyping |
| **Nginx + PHP 8.1** | Kombinasi performant untuk high-traffic applications dengan memory footprint rendah |
| **Midtrans** | Payment gateway lokal Indonesia dengan compliance dan support terbaik, mendukung berbagai metode pembayaran lokal |
| **Alpine.js** | Lightweight alternative untuk Vue/React, cocok untuk aplikasi yang tidak terlalu complex |
| **Figma** | Industry standard untuk UI/UX design dengan collaboration features yang excellent |
| **GitHub** | Version control hosting paling populer dengan CI/CD integration yang mudah |

---

_Catatan: BAB IV Part 3 ini merupakan lanjutan dari Part 2. Untuk bagian 4.7 Desiminasi Proyek, lihat Part 4._

---

