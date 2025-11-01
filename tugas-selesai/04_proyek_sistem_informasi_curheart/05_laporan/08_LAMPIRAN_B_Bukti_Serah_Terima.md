# LAMPIRAN B
# BUKTI SERAH TERIMA PRODUK

---

## B.1 BERITA ACARA SERAH TERIMA PRODUK

**BERITA ACARA**  
**SERAH TERIMA SISTEM INFORMASI CUR-HEART**

Nomor: 045/BA-ST/CURHEART/XI/2024

---

Pada hari **Jumat**, tanggal **1 November 2024**, pukul **14:00 WIB**, bertempat di **Kantor CUR-HEART**, Jl. Mampang Prapatan Raya No. 88, Jakarta Selatan 12790, telah dilaksanakan Serah Terima Produk Sistem Informasi CUR-HEART dari Tim Proyek Capstone Program Studi Sistem Informasi Universitas Nusa Mandiri kepada Pihak CUR-HEART.

---

### PIHAK PERTAMA (YANG MENYERAHKAN)

**Tim Proyek Capstone - Universitas Nusa Mandiri**

1. **Roki Anjas**
   - NIM: 11250066
   - Jabatan: Project Manager
   - Email: roki.anjas@students.nusamandiri.ac.id
   - Telepon: +62 812-1111-0066

2. **Susanto**
   - NIM: 11250068
   - Jabatan: Frontend Developer
   - Email: susanto@students.nusamandiri.ac.id
   - Telepon: +62 812-2222-0068

3. **Fahruroji**
   - NIM: 11250085
   - Jabatan: Full-stack Developer
   - Email: fahruroji@students.nusamandiri.ac.id
   - Telepon: +62 812-3333-0085

**Dosen Pembimbing**:
- **Rani Irma Handayani, M.Kom**
- NIDN: 0328068201
- Email: rani.handayani@nusamandiri.ac.id

---

### PIHAK KEDUA (YANG MENERIMA)

**CUR-HEART (Hypnotherapy & Mind Wellness Center)**

1. **Dr. Sarah Wellness**
   - Jabatan: Owner & Founder
   - Email: sarah@cur-heart.com
   - Telepon: +62 812-3456-7890

2. **Michael Ananda, CHt**
   - Jabatan: Head Therapist
   - Email: michael@cur-heart.com
   - Telepon: +62 812-3456-7891

3. **Rina Kusuma**
   - Jabatan: Admin & Customer Service
   - Email: rina@cur-heart.com
   - Telepon: +62 812-3456-7892

---

### BARANG/PRODUK YANG DISERAHKAN

Pihak Pertama menyerahkan kepada Pihak Kedua berupa **Sistem Informasi CUR-HEART** dengan spesifikasi sebagai berikut:

#### 1. SISTEM APLIKASI WEB

**A. Spesifikasi Teknis**

| Komponen | Deskripsi |
|----------|-----------|
| **Nama Sistem** | Sistem Informasi CUR-HEART |
| **Versi** | 1.0.0 (Release) |
| **Framework** | Laravel 10.x (PHP) |
| **Database** | MySQL 8.0 |
| **Frontend** | Blade Templates + Tailwind CSS + JavaScript |
| **Arsitektur** | Monolithic Web Application (MVC Pattern) |
| **Lisensi** | Proprietary (Milik CUR-HEART) |

**B. URL Akses**

- **Production**: https://curheart-demo.nusamandiri.ac.id (temporary)
- **Final Production**: https://cur-heart.com (setelah domain setup)

**C. Fitur Utama yang Diserahkan** (Total: 40 Fitur)

**Modul Public (8 Fitur)**:
1. ✅ Landing Page dengan Hero Section
2. ✅ About Us - Profil Perusahaan
3. ✅ Services - 6 Layanan Hypnotherapy
4. ✅ Service Detail Pages
5. ✅ Therapists Directory - 8 Terapis
6. ✅ Therapist Profile Pages
7. ✅ Blog/Articles (15 artikel kesehatan mental)
8. ✅ Contact Form & Location Map

**Modul Authentication (6 Fitur)**:
9. ✅ User Registration (Client & Therapist)
10. ✅ Login Multi-role (Client, Therapist, Admin)
11. ✅ Logout
12. ✅ Forgot Password
13. ✅ Reset Password via Email
14. ✅ Email Verification

**Modul Client Dashboard (10 Fitur)**:
15. ✅ Client Dashboard Overview
16. ✅ Browse & Search Services
17. ✅ View Therapist Profiles & Ratings
18. ✅ 4-Step Booking Process (Service → Therapist → Schedule → Payment)
19. ✅ Payment Integration (Midtrans Gateway)
20. ✅ Booking Confirmation & Notification
21. ✅ My Appointments (Upcoming & Past)
22. ✅ Appointment Detail & Reschedule
23. ✅ Progress Tracking dengan Chart
24. ✅ Messages/Chat dengan Terapis

**Modul Therapist Dashboard (10 Fitur)**:
25. ✅ Therapist Dashboard Overview
26. ✅ Schedule Management (Calendar View)
27. ✅ Availability Settings (Working Hours)
28. ✅ Client List Management
29. ✅ Client Profile View (Medical History, Session History)
30. ✅ Session Room (Video Call Placeholder)
31. ✅ Session Notes Input (SOAP Format)
32. ✅ Session History & Timeline
33. ✅ Earnings Report & Chart
34. ✅ Profile Management

**Modul Admin Dashboard (6 Fitur)**:
35. ✅ Admin Dashboard dengan Metrics
36. ✅ User Management (CRUD: Clients, Therapists, Admins)
37. ✅ Booking Management (All Bookings dengan Filter)
38. ✅ Payment Management & Verification
39. ✅ Financial Reports (Revenue, Expenses, Profit)
40. ✅ System Settings (SMTP, Payment Gateway, General)

**D. Total Halaman Sistem**: 41 Halaman (sesuai mockup)

---

#### 2. SOURCE CODE & DOKUMENTASI TEKNIS

**A. Repository Source Code**

| Item | Deskripsi |
|------|-----------|
| **Platform** | GitHub (Private Repository) |
| **URL** | https://github.com/roqianjas/curheart-laravel |
| **Access** | Owner CUR-HEART telah di-invite sebagai collaborator |
| **Branch** | `main` (production), `development` (untuk future updates) |
| **Total Commits** | 247 commits |
| **Total Files** | 350+ files |
| **Lines of Code** | ~25,000 lines (termasuk Blade templates) |

**B. Struktur Source Code**

```
curheart-laravel/
├── app/                        # Application Logic
│   ├── Http/
│   │   ├── Controllers/       # 25 Controllers
│   │   ├── Middleware/        # 8 Middleware
│   │   └── Requests/          # 40 Form Requests
│   ├── Models/                # 16 Eloquent Models
│   └── Services/              # 12 Service Classes
├── database/
│   ├── migrations/            # 25 Migration Files
│   └── seeders/               # 10 Seeder Files
├── resources/
│   ├── views/                 # 41 Blade Templates
│   ├── css/                   # Tailwind CSS
│   └── js/                    # JavaScript Modules
├── routes/
│   └── web.php               # 65 Routes
├── config/                    # Configuration Files
├── public/                    # Public Assets
└── tests/                     # 55 Test Cases
```

**C. Dokumentasi Teknis yang Diserahkan**

1. ✅ **Installation Guide** (10 halaman)
   - System requirements
   - Step-by-step installation
   - Configuration setup
   - Troubleshooting

2. ✅ **Developer Documentation** (50 halaman)
   - Architecture overview
   - Database schema & ERD
   - Code structure explanation
   - API documentation (internal)
   - Security implementation
   - Performance optimization tips

3. ✅ **Deployment Guide** (15 halaman)
   - Server requirements
   - Deployment steps
   - SSL certificate setup
   - Domain configuration
   - Backup & recovery procedures

4. ✅ **Maintenance Guide** (12 halaman)
   - Routine maintenance tasks
   - Database backup procedures
   - Update & upgrade procedures
   - Security checklist
   - Performance monitoring

**Format**: PDF + Markdown (dalam repository)

---

#### 3. DATABASE & DATA

**A. Database Schema**

| Komponen | Detail |
|----------|--------|
| **Database Name** | `curheart_db` |
| **DBMS** | MySQL 8.0 |
| **Total Tables** | 16 tables |
| **Total Columns** | 180+ columns |
| **Indexing** | Optimized dengan 25 indexes |
| **Relasi** | 22 foreign key relationships |

**Daftar Tabel**:
1. `users` - Data pengguna (clients, therapists, admins)
2. `roles` - Role-based access control
3. `services` - Layanan hypnotherapy
4. `therapists` - Profil terapis (extended from users)
5. `clients` - Profil klien (extended from users)
6. `bookings` - Data booking appointment
7. `sessions` - Data sesi terapi
8. `session_notes` - Catatan sesi terapis
9. `payments` - Data pembayaran
10. `schedules` - Jadwal terapis
11. `availability` - Ketersediaan waktu terapis
12. `messages` - Chat antara client-therapist
13. `reviews` - Rating & review dari client
14. `blog_posts` - Artikel blog
15. `notifications` - Notifikasi sistem
16. `system_settings` - Pengaturan sistem

**B. Sample Data yang Diserahkan**

| Tabel | Jumlah Records |
|-------|----------------|
| `users` | 50 records (25 clients, 8 therapists, 3 admins, 14 test users) |
| `services` | 6 records (layanan hypnotherapy) |
| `therapists` | 8 records |
| `bookings` | 120 records (sample data 3 bulan) |
| `sessions` | 95 records |
| `payments` | 118 records |
| `reviews` | 45 records |
| `blog_posts` | 15 articles |
| `messages` | 200+ messages |

**C. File SQL yang Diserahkan**

1. ✅ **curheart_schema.sql** (350 lines)
   - DDL (Data Definition Language)
   - CREATE TABLE statements
   - Indexes & constraints

2. ✅ **curheart_sample_data.sql** (2,500 lines)
   - DML (Data Manipulation Language)
   - INSERT statements dengan sample data

3. ✅ **curheart_backup_template.sql**
   - Template untuk backup routine

**Format**: SQL file (UTF-8 encoded)

---

#### 4. USER MANUAL & PANDUAN PENGGUNA

**A. User Manual Client** (25 halaman)

**Konten**:
- Pendahuluan sistem
- Cara registrasi & login
- Panduan booking sesi terapi (step-by-step dengan screenshot)
- Cara melakukan pembayaran
- Cara melihat appointment & progress
- Cara berkomunikasi dengan terapis
- FAQ & troubleshooting
- Contact support

**Format**: PDF (full color, dengan screenshot)

---

**B. User Manual Therapist** (30 halaman)

**Konten**:
- Dashboard overview
- Cara mengelola jadwal & availability
- Cara menerima & mengelola booking
- Panduan pelaksanaan sesi terapi
- Cara input session notes (SOAP format)
- Cara melihat client profile & history
- Cara mengelola earnings
- FAQ & troubleshooting

**Format**: PDF (full color, dengan screenshot)

---

**C. User Manual Admin** (35 halaman)

**Konten**:
- Dashboard overview
- Cara mengelola users (CRUD operations)
- Cara mengelola bookings & payments
- Cara generate financial reports
- Cara konfigurasi system settings
- Backup & restore procedures
- Security best practices
- FAQ & troubleshooting

**Format**: PDF (full color, dengan screenshot)

---

#### 5. TRAINING & KNOWLEDGE TRANSFER

**A. Training Session yang Telah Dilakukan**

**Training 1: Admin & Owner**
- **Tanggal**: 28 Oktober 2024
- **Durasi**: 3 jam
- **Peserta**: Dr. Sarah Wellness (Owner), Rina Kusuma (Admin)
- **Materi**: 
  - System overview
  - Admin dashboard usage
  - User management
  - Booking & payment management
  - Financial reports
  - System settings & configuration
- **Dokumentasi**: ✅ Slide presentasi (PDF, 45 slides), Video recording (MP4, 3 jam)

**Training 2: Therapists**
- **Tanggal**: 29 Oktober 2024
- **Durasi**: 2.5 jam
- **Peserta**: 8 Terapis CUR-HEART
- **Materi**:
  - Therapist dashboard overview
  - Schedule & availability management
  - Handling bookings
  - Session notes input
  - Client management
- **Dokumentasi**: ✅ Slide presentasi (PDF, 35 slides), Video recording (MP4, 2.5 jam)

**Training 3: Hands-on Practice**
- **Tanggal**: 30 Oktober 2024
- **Durasi**: 4 jam
- **Peserta**: Semua stakeholder (owner, admin, 8 therapists)
- **Materi**:
  - Praktik langsung menggunakan sistem
  - Role-playing scenarios
  - Q&A session
  - Troubleshooting common issues
- **Dokumentasi**: ✅ Training notes (PDF, 8 halaman), Foto dokumentasi (20 foto)

---

**B. Knowledge Transfer Documents**

1. ✅ **Training Materials Package** (folder digital)
   - Slide presentasi (3 set)
   - Video recordings (3 videos, total 9.5 jam)
   - Cheat sheets (5 PDF)
   - Quick reference guides (3 PDF)

2. ✅ **FAQ Document** (15 halaman)
   - 50 pertanyaan paling umum dengan jawaban
   - Troubleshooting guide
   - Best practices

---

#### 6. TESTING REPORTS & QUALITY ASSURANCE

**A. Testing Reports yang Diserahkan**

1. ✅ **Unit Testing Report** (5 halaman)
   - 25 test cases: All PASSED ✅
   - Code coverage: 75%
   - Execution time: 2.5 seconds

2. ✅ **Feature Testing Report** (8 halaman)
   - 30 test cases: All PASSED ✅
   - Integration testing results
   - Execution time: 15.2 seconds

3. ✅ **User Acceptance Testing (UAT) Report** (12 halaman)
   - 15 scenarios tested with stakeholders
   - Success rate: 93.3% ✅
   - Feedback & improvements implemented
   - Sign-off dari stakeholders

4. ✅ **Performance Testing Report** (10 halaman)
   - Google Lighthouse Score: 92/100 (Performance)
   - Load testing: 100 concurrent users handled smoothly
   - Average response time: 245ms
   - Optimization recommendations

5. ✅ **Security Assessment Report** (25 halaman)
   - OWASP Top 10 compliance: All PASSED ✅
   - Vulnerability scanning results
   - Penetration testing summary
   - Security hardening checklist

**Format**: PDF (dengan charts dan screenshots)

---

#### 7. DEPLOYMENT & HOSTING INFORMATION

**A. Production Environment Details**

| Komponen | Spesifikasi |
|----------|-------------|
| **Server Type** | VPS (Virtual Private Server) |
| **Provider** | Digital Ocean |
| **Location** | Singapore (SG1 Datacenter) |
| **OS** | Ubuntu 22.04 LTS |
| **Web Server** | Nginx 1.22 |
| **PHP** | 8.2 |
| **Database** | MySQL 8.0 |
| **Memory** | 4GB RAM |
| **Storage** | 80GB SSD |
| **Bandwidth** | 4TB/month |
| **IP Address** | 128.199.xxx.xxx (akan diserahkan) |
| **SSL Certificate** | Let's Encrypt (Auto-renew enabled) |
| **Backup** | Daily automatic backup (7-day retention) |

**B. Domain & DNS**

| Item | Detail |
|------|--------|
| **Domain** | cur-heart.com (akan diserahkan ownership) |
| **Registrar** | Namecheap / Niagahoster |
| **DNS Provider** | Cloudflare (untuk CDN & security) |
| **Email** | info@cur-heart.com, support@cur-heart.com |

**C. Access Credentials** (diserahkan dalam amplop tertutup)

- ✅ Server SSH access (root & sudo user)
- ✅ Database credentials (root & app user)
- ✅ Domain registrar account
- ✅ Cloudflare account
- ✅ Email admin access
- ✅ Payment gateway (Midtrans) credentials

---

#### 8. INTELLECTUAL PROPERTY & LICENSE

**A. Hak Kepemilikan**

Pihak Pertama (Tim Proyek) menyerahkan **SELURUH HAK KEPEMILIKAN** (Intellectual Property Rights) Sistem Informasi CUR-HEART kepada Pihak Kedua (CUR-HEART) dengan ketentuan:

1. ✅ Source code menjadi **MILIK PENUH** CUR-HEART
2. ✅ CUR-HEART berhak memodifikasi, mengembangkan, atau mengalihkan sistem tanpa izin Tim Proyek
3. ✅ CUR-HEART berhak menggunakan sistem untuk keperluan komersial
4. ✅ Tim Proyek **TIDAK** berhak menjual atau mendistribusikan source code kepada pihak lain
5. ✅ Tim Proyek **DIIZINKAN** menggunakan sistem sebagai portfolio dengan blur identitas data sensitif

**B. License Agreement**

- **Lisensi**: Proprietary (Full ownership by CUR-HEART)
- **Durasi**: Selamanya (perpetual license)
- **Batasan**: Source code tidak boleh dipublikasikan tanpa izin tertulis CUR-HEART

**Dokumen**:
- ✅ Surat Perjanjian Pengalihan Hak Cipta (bermaterai)

---

#### 9. WARRANTY & SUPPORT

**A. Warranty Period**

Pihak Pertama memberikan **GARANSI** kepada Pihak Kedua dengan ketentuan:

| Jenis Garansi | Durasi | Cakupan |
|---------------|--------|---------|
| **Bug Fixing** | 3 bulan (1 Nov 2024 - 31 Jan 2025) | Gratis perbaikan bugs yang ditemukan dalam penggunaan normal |
| **Technical Support** | 3 bulan | Konsultasi via WhatsApp/Email (response time: 1x24 jam) |
| **Minor Updates** | 3 bulan | Update keamanan & bug fixes |
| **Training Support** | 1 bulan | Follow-up training jika diperlukan |

**Catatan**:
- Feature baru atau major updates **TIDAK** termasuk dalam garansi
- Kerusakan akibat modifikasi oleh pihak ketiga **TIDAK** termasuk garansi

**B. Post-Warranty Support** (Opsional)

Setelah periode garansi habis, CUR-HEART dapat memperpanjang support dengan skema:
- **Monthly Retainer**: Rp 2.000.000/bulan (technical support + minor updates)
- **Hourly Rate**: Rp 250.000/jam (untuk feature development)
- **Annual Maintenance**: Rp 20.000.000/tahun (full support + updates)

---

#### 10. ADDITIONAL DELIVERABLES

**A. Marketing Materials**

1. ✅ **Video Promosi** (2 menit 30 detik)
   - Platform: YouTube, Instagram, TikTok
   - Format: MP4 (1080p)
   - Konten: Feature highlights, benefits, call-to-action

2. ✅ **X-Banner Design** (60 x 160 cm)
   - Format: PDF print-ready (300 dpi)
   - Konten: System overview dengan infografis

**B. Presentation Deck**

- ✅ **Slide Presentasi Final** (20 slides)
- Format: PowerPoint (.pptx) + PDF
- Konten: Executive summary, features, benefits, ROI

---

### KESEPAKATAN DAN PERSETUJUAN

Dengan ditandatanganinya Berita Acara ini, maka:

1. ✅ Pihak Pertama telah **MENYERAHKAN** seluruh produk, dokumentasi, dan hak kepemilikan kepada Pihak Kedua dalam kondisi **LENGKAP dan BERFUNGSI** dengan baik.

2. ✅ Pihak Kedua telah **MENERIMA** seluruh produk, dokumentasi, dan hak kepemilikan dari Pihak Pertama dan menyatakan **PUAS** dengan kondisi produk yang diserahkan.

3. ✅ Pihak Kedua **MELEPASKAN** Pihak Pertama dari segala tuntutan terkait pengembangan sistem setelah masa garansi berakhir (kecuali ada perjanjian perpanjangan support).

4. ✅ Pihak Pertama **BERHAK** menggunakan proyek ini sebagai **PORTFOLIO** untuk keperluan akademik dan profesional dengan ketentuan:
   - Data sensitif (nama klien, data pribadi, data keuangan) harus di-blur atau diganti dengan dummy data
   - Logo dan nama CUR-HEART dapat ditampilkan
   - Source code tidak boleh dipublikasikan tanpa izin tertulis

5. ✅ Kedua belah pihak sepakat bahwa serah terima ini telah dilakukan dengan **SUKARELA** tanpa paksaan dari pihak manapun.

---

### DAFTAR CHECKLIST SERAH TERIMA

| No | Item yang Diserahkan | Status | Keterangan |
|----|---------------------|--------|------------|
| 1 | Sistem Aplikasi Web (41 halaman) | ✅ Lengkap | Production URL + credentials |
| 2 | Source Code (GitHub Repository) | ✅ Lengkap | Access granted to owner |
| 3 | Database Schema + Sample Data | ✅ Lengkap | SQL files provided |
| 4 | User Manual (Client, Therapist, Admin) | ✅ Lengkap | 3 PDF files (90 pages total) |
| 5 | Technical Documentation | ✅ Lengkap | Installation, Developer, Deployment, Maintenance guides |
| 6 | Training Materials | ✅ Lengkap | Slides, videos, cheat sheets |
| 7 | Testing Reports (UAT, Performance, Security) | ✅ Lengkap | 5 comprehensive reports |
| 8 | Server Access & Credentials | ✅ Lengkap | Sealed envelope delivered |
| 9 | Domain & DNS Setup | ✅ Lengkap | Ownership transfer documents |
| 10 | IP Transfer Agreement | ✅ Lengkap | Signed and notarized |
| 11 | Video Promosi & X-Banner | ✅ Lengkap | Digital files provided |
| 12 | Presentation Deck | ✅ Lengkap | PPTX + PDF |
| 13 | Backup Files (Full System) | ✅ Lengkap | External HDD 1TB + Google Drive |
| 14 | Warranty Letter | ✅ Lengkap | 3 months coverage |
| 15 | Support Contact Information | ✅ Lengkap | WhatsApp Group created |

**Total Item**: 15 items  
**Status**: ✅ **100% LENGKAP**

---

### LAMPIRAN FOTO DOKUMENTASI SERAH TERIMA

1. ✅ Foto tim proyek dengan stakeholder CUR-HEART (5 foto)
2. ✅ Foto penyerahan dokumen & external HDD (3 foto)
3. ✅ Foto demo sistem kepada owner & staff (8 foto)
4. ✅ Foto bersama saat penandatanganan (2 foto)
5. ✅ Foto plakat/certificate of appreciation (jika ada)

**Total**: 18+ foto dokumentasi

---

Demikian Berita Acara Serah Terima ini dibuat dengan sebenar-benarnya dan ditandatangani oleh kedua belah pihak dalam keadaan sadar dan tanpa paksaan.

Jakarta, 1 November 2024

---

**PIHAK PERTAMA (YANG MENYERAHKAN)**

**Tim Proyek Capstone UNM**

[Tanda Tangan]  
**Roki Anjas** (11250066)  
Project Manager  
**Materai 10.000**

[Tanda Tangan]  
**Susanto** (11250068)  
Frontend Developer  
**Materai 10.000**

[Tanda Tangan]  
**Fahruroji** (11250085)  
Full-stack Developer  
**Materai 10.000**

**Mengetahui,**

**Dosen Pembimbing**

[Tanda Tangan]  
**Rani Irma Handayani, M.Kom**  
NIDN: 0328068201  
**Materai 10.000**

---

**PIHAK KEDUA (YANG MENERIMA)**

**CUR-HEART**

[Tanda Tangan + Stempel Perusahaan]  
**Dr. Sarah Wellness**  
Owner & Founder CUR-HEART  
**Materai 10.000**

[Tanda Tangan]  
**Michael Ananda, CHt**  
Head Therapist  
**Materai 10.000**

[Tanda Tangan]  
**Rina Kusuma**  
Admin & Customer Service  
**Materai 10.000**

---

**Saksi-saksi:**

**Saksi 1:**

[Tanda Tangan]  
**[Nama Saksi 1]**  
[Jabatan]

**Saksi 2:**

[Tanda Tangan]  
**[Nama Saksi 2]**  
[Jabatan]

---

## B.2 SURAT PERNYATAAN PENERIMAAN PRODUK

**SURAT PERNYATAAN PENERIMAAN PRODUK**

Yang bertanda tangan di bawah ini:

**Nama**: Dr. Sarah Wellness  
**NIK**: 3174xxxxxxxxxx  
**Jabatan**: Owner & Founder  
**Nama Perusahaan**: CUR-HEART (Hypnotherapy & Mind Wellness Center)  
**Alamat**: Jl. Mampang Prapatan Raya No. 88, Jakarta Selatan 12790  
**Telepon**: +62 812-3456-7890  
**Email**: sarah@cur-heart.com

Dengan ini menyatakan bahwa:

1. Saya/kami telah **MENERIMA** produk Sistem Informasi CUR-HEART dari Tim Proyek Capstone (Roki Anjas, Susanto, Fahruroji) Program Studi Sistem Informasi Universitas Nusa Mandiri pada tanggal **1 November 2024**.

2. Produk yang diserahkan meliputi:
   - ✅ Sistem Aplikasi Web CUR-HEART (41 halaman, fully functional)
   - ✅ Source code lengkap dengan dokumentasi
   - ✅ Database schema dan sample data
   - ✅ User manual untuk 3 role (Client, Therapist, Admin)
   - ✅ Technical documentation (Installation, Developer, Deployment guides)
   - ✅ Training materials dan video recordings
   - ✅ Testing reports (UAT, Performance, Security)
   - ✅ Server access & credentials
   - ✅ Domain & DNS setup
   - ✅ Intellectual Property transfer documents
   - ✅ Video promosi & X-Banner design
   - ✅ Warranty letter (3 bulan)

3. Saya/kami telah **MENGECEK** dan **MENGUJI** sistem yang diserahkan dan menyatakan bahwa sistem tersebut:
   - ✅ Berfungsi dengan **BAIK dan NORMAL**
   - ✅ Sesuai dengan **REQUIREMENT** yang telah disepakati
   - ✅ Telah melalui **USER ACCEPTANCE TESTING (UAT)** dengan hasil memuaskan
   - ✅ **SIAP DIGUNAKAN** untuk operasional CUR-HEART

4. Saya/kami telah menerima **TRAINING** yang memadai dari Tim Proyek dan merasa **KOMPETEN** untuk mengoperasikan sistem.

5. Saya/kami **PUAS** dengan kualitas produk yang diserahkan dan menyatakan bahwa Tim Proyek telah menyelesaikan tugasnya dengan **BAIK dan PROFESIONAL**.

6. Saya/kami memberikan **TESTIMONI** sebagai berikut:

   > "Tim Proyek telah mengembangkan Sistem Informasi CUR-HEART dengan sangat profesional. Sistem yang dihasilkan sangat user-friendly, sesuai dengan kebutuhan kami, dan sangat membantu operasional bisnis kami. Proses booking yang tadinya manual dan memakan waktu, kini menjadi otomatis dan efisien. Dashboard yang informatif memudahkan kami dalam monitoring bisnis. Kami sangat puas dan merekomendasikan tim ini untuk proyek-proyek lainnya."
   >
   > — Dr. Sarah Wellness, Owner CUR-HEART

7. Saya/kami memberikan **IZIN** kepada Tim Proyek untuk:
   - ✅ Menggunakan proyek ini sebagai **PORTFOLIO** akademik dan profesional
   - ✅ Mempublikasikan **SCREENSHOT** sistem dengan blur data sensitif
   - ✅ Mempublikasikan **LOGO dan NAMA** CUR-HEART dalam portfolio
   - ✅ Menggunakan **TESTIMONI** ini dalam keperluan promosi akademik
   - ❌ **TIDAK DIIZINKAN** mempublikasikan source code tanpa izin tertulis

8. Surat pernyataan ini dibuat dengan **SEBENAR-BENARNYA** tanpa paksaan dari pihak manapun untuk dapat digunakan sebagaimana mestinya.

Demikian surat pernyataan ini saya buat dengan penuh kesadaran dan tanggung jawab.

Jakarta, 1 November 2024

**Yang Membuat Pernyataan,**

[Tanda Tangan + Stempel Perusahaan]

**Dr. Sarah Wellness**  
Owner & Founder CUR-HEART

**Materai 10.000**

---

## B.3 SURAT PENGALIHAN HAK CIPTA (IP TRANSFER)

**SURAT PERJANJIAN**  
**PENGALIHAN HAK KEKAYAAN INTELEKTUAL**  
**(INTELLECTUAL PROPERTY TRANSFER AGREEMENT)**

Nomor: 046/SP-HAKI/CURHEART/XI/2024

---

Pada hari **Jumat**, tanggal **1 November 2024**, bertempat di Jakarta, telah dibuat dan ditandatangani Surat Perjanjian Pengalihan Hak Kekayaan Intelektual oleh dan antara:

### PIHAK PERTAMA (PENGALIH HAK)

**Tim Proyek Capstone - Universitas Nusa Mandiri**

1. **Roki Anjas** (NIM: 11250066)
2. **Susanto** (NIM: 11250068)
3. **Fahruroji** (NIM: 11250085)

Selanjutnya disebut sebagai **"PIHAK PERTAMA"**

### PIHAK KEDUA (PENERIMA HAK)

**Nama Perusahaan**: CUR-HEART (Hypnotherapy & Mind Wellness Center)  
**Diwakili oleh**: Dr. Sarah Wellness (Owner & Founder)  
**Alamat**: Jl. Mampang Prapatan Raya No. 88, Jakarta Selatan 12790

Selanjutnya disebut sebagai **"PIHAK KEDUA"**

---

### PASAL 1: OBJEK PENGALIHAN

Pihak Pertama dengan ini mengalihkan seluruh Hak Kekayaan Intelektual (Intellectual Property Rights) atas **Sistem Informasi CUR-HEART** kepada Pihak Kedua, yang meliputi:

1. **Source Code** aplikasi web (frontend & backend)
2. **Database Design** (ERD, schema, structure)
3. **UI/UX Design** (mockups, design system, visual elements)
4. **Documentation** (technical, user manuals, guides)
5. **Brand Assets** terkait sistem (logo app, icons, graphics)
6. **Algorithms & Logic** yang dikembangkan khusus untuk sistem
7. **Trade Secrets** terkait implementasi bisnis logic

---

### PASAL 2: RUANG LINGKUP PENGALIHAN

1. Pengalihan hak bersifat **PENUH dan MUTLAK** (full and exclusive transfer).
2. Pihak Kedua berhak untuk:
   - ✅ Menggunakan sistem untuk keperluan komersial
   - ✅ Memodifikasi dan mengembangkan sistem
   - ✅ Mengalihkan kepemilikan kepada pihak ketiga (jika perusahaan dijual)
   - ✅ Mendaftarkan hak cipta atas nama perusahaan
3. Pihak Pertama **TIDAK BERHAK** untuk:
   - ❌ Menjual atau mendistribusikan source code kepada pihak lain
   - ❌ Mengembangkan sistem serupa untuk kompetitor
   - ❌ Mengklaim kepemilikan setelah pengalihan

---

### PASAL 3: HAK PENGGUNAAN UNTUK PORTFOLIO

Meskipun hak telah dialihkan secara penuh, Pihak Kedua memberikan **IZIN TERBATAS** kepada Pihak Pertama untuk:

1. ✅ Menggunakan proyek sebagai **PORTFOLIO** akademik dan profesional
2. ✅ Mempublikasikan **SCREENSHOT** sistem dengan ketentuan:
   - Data pribadi klien harus di-blur atau diganti dummy data
   - Data keuangan harus di-hide atau diganti dummy data
   - Logo dan nama CUR-HEART dapat ditampilkan
3. ✅ Menyebutkan nama perusahaan dalam CV, LinkedIn, dan platform profesional
4. ❌ **TIDAK DIIZINKAN** mempublikasikan source code di platform publik (GitHub public, dll) tanpa izin tertulis

---

### PASAL 4: KOMPENSASI

Sebagai kompensasi atas pengalihan hak ini, disepakati:

1. Pengalihan hak ini merupakan bagian dari **TUGAS AKADEMIK** (Capstone Project) yang dilakukan Tim Proyek untuk memenuhi persyaratan kelulusan.

2. Pihak Kedua telah memberikan **AKSES dan DATA** yang diperlukan untuk pengerjaan proyek.

3. Tidak ada kompensasi finansial yang diperjanjikan untuk pengalihan hak ini, namun Pihak Kedua bersedia memberikan:
   - ✅ **Surat Rekomendasi** untuk Tim Proyek (jika diminta)
   - ✅ **Testimoni** untuk keperluan akademik
   - ✅ **Reference Letter** untuk keperluan profesional

---

### PASAL 5: GARANSI DAN JAMINAN

1. Pihak Pertama menjamin bahwa:
   - ✅ Sistem adalah **KARYA ASLI** tanpa unsur plagiasi
   - ✅ Tidak ada **KLAIM PIHAK KETIGA** atas sistem
   - ✅ Source code tidak melanggar **LISENSI** pihak lain (kecuali open source dengan lisensi yang diizinkan)

2. Pihak Pertama memberikan **GARANSI TERBATAS** selama 3 bulan untuk bug fixing dan technical support.

---

### PASAL 6: KERAHASIAAN

Kedua belah pihak sepakat untuk menjaga kerahasiaan:
- Data bisnis CUR-HEART (keuangan, strategi, data klien)
- Informasi teknis sistem (security implementation, API keys, credentials)
- Detail perjanjian ini (kecuali untuk keperluan audit atau legal)

Pelanggaran kerahasiaan dapat dikenakan sanksi sesuai hukum yang berlaku.

---

### PASAL 7: PENYELESAIAN SENGKETA

1. Apabila terjadi perselisihan atau perbedaan pendapat, akan diselesaikan secara **MUSYAWARAH**.
2. Jika musyawarah tidak mencapai kesepakatan, akan diselesaikan melalui **MEDIASI**.
3. Jika mediasi gagal, akan diselesaikan melalui **ARBITRASE** atau Pengadilan Negeri Jakarta Selatan.

---

### PASAL 8: LAIN-LAIN

1. Perjanjian ini dibuat dalam **2 (dua) rangkap** asli, masing-masing bermaterai cukup dan memiliki kekuatan hukum yang sama.
2. Perjanjian ini berlaku sejak ditandatangani dan bersifat **MENGIKAT** bagi para pihak.
3. Perubahan atau amandemen perjanjian ini harus dibuat secara tertulis dan ditandatangani oleh kedua belah pihak.

---

Demikian Surat Perjanjian ini dibuat dan ditandatangani oleh kedua belah pihak dalam keadaan sadar, sehat jasmani dan rohani, serta tanpa paksaan dari pihak manapun.

Jakarta, 1 November 2024

---

**PIHAK PERTAMA (PENGALIH HAK)**

[Tanda Tangan]  
**Roki Anjas** (11250066)  
**Materai 10.000**

[Tanda Tangan]  
**Susanto** (11250068)  
**Materai 10.000**

[Tanda Tangan]  
**Fahruroji** (11250085)  
**Materai 10.000**

**Mengetahui,**

**Dosen Pembimbing**

[Tanda Tangan]  
**Rani Irma Handayani, M.Kom**  
NIDN: 0328068201  
**Materai 10.000**

---

**PIHAK KEDUA (PENERIMA HAK)**

[Tanda Tangan + Stempel Perusahaan]  
**Dr. Sarah Wellness**  
Owner & Founder CUR-HEART  
**Materai 10.000**

---

**Saksi-saksi:**

**Saksi 1 (dari Pihak Pertama):**

[Tanda Tangan]  
**[Nama Dosen/Staff UNM]**  
**Materai 10.000**

**Saksi 2 (dari Pihak Kedua):**

[Tanda Tangan]  
**Michael Ananda, CHt**  
Head Therapist CUR-HEART  
**Materai 10.000**

---

## B.4 WARRANTY LETTER (SURAT GARANSI)

**SURAT GARANSI PRODUK**

Nomor: 047/SG/CURHEART/XI/2024

---

Yang bertanda tangan di bawah ini:

**Nama**: Roki Anjas  
**NIM**: 11250066  
**Jabatan**: Project Manager  
**Program Studi**: Sistem Informasi  
**Universitas**: Nusa Mandiri  
**Alamat**: [Alamat]  
**Telepon**: +62 812-1111-0066  
**Email**: roki.anjas@students.nusamandiri.ac.id

Bertindak untuk dan atas nama **Tim Proyek Capstone** (Roki Anjas, Susanto, Fahruroji), dengan ini memberikan **GARANSI** atas produk **Sistem Informasi CUR-HEART** yang telah diserahkan kepada **CUR-HEART** (Hypnotherapy & Mind Wellness Center) dengan ketentuan sebagai berikut:

---

### 1. PERIODE GARANSI

| Jenis Garansi | Periode | Berlaku Sampai |
|---------------|---------|----------------|
| **Bug Fixing** | 3 bulan | 31 Januari 2025 |
| **Technical Support** | 3 bulan | 31 Januari 2025 |
| **Minor Updates** | 3 bulan | 31 Januari 2025 |
| **Training Follow-up** | 1 bulan | 30 November 2024 |

---

### 2. CAKUPAN GARANSI

#### A. Bug Fixing (Gratis)

Kami akan memperbaiki **GRATIS** bugs yang ditemukan dengan kriteria:
- ✅ Bug yang menyebabkan sistem tidak berfungsi (critical/high severity)
- ✅ Bug yang menyebabkan data error atau loss
- ✅ Bug pada fitur-fitur utama (booking, payment, dashboard)
- ✅ Bug yang muncul dalam penggunaan **NORMAL** sesuai user manual

**Tidak Termasuk Garansi**:
- ❌ Bug akibat modifikasi oleh pihak ketiga
- ❌ Bug akibat penggunaan tidak sesuai user manual
- ❌ Bug akibat force majeure (server down, hack, dll)
- ❌ Perubahan requirement atau penambahan fitur baru

**Response Time**:
- Critical bugs: **1x24 jam** (working days)
- High priority: **2x24 jam**
- Medium priority: **3x24 jam**
- Low priority: **5x24 jam**

---

#### B. Technical Support (Gratis)

Kami menyediakan **KONSULTASI TEKNIS** via:
- WhatsApp: Group support (sudah dibuat)
- Email: support.curheart@students.nusamandiri.ac.id
- Video call: By appointment (max 2 jam/minggu)

**Cakupan Support**:
- ✅ Cara penggunaan sistem
- ✅ Troubleshooting masalah umum
- ✅ Konsultasi konfigurasi
- ✅ Panduan backup & restore
- ✅ Best practices penggunaan

**Response Time**: **1x24 jam** (working days)

---

#### C. Minor Updates (Gratis)

Kami akan memberikan **UPDATE GRATIS** untuk:
- ✅ Security patches (jika ditemukan vulnerability)
- ✅ Bug fixes (sesuai ketentuan di atas)
- ✅ Laravel framework updates (minor version)
- ✅ PHP version compatibility updates

**Tidak Termasuk**:
- ❌ Feature updates/enhancements
- ❌ Major version upgrades
- ❌ UI/UX redesign
- ❌ Database structure changes

---

#### D. Training Follow-up (Gratis)

Untuk 1 bulan pertama (Nov 2024), kami menyediakan:
- ✅ Follow-up training session (max 2 sessions @ 2 jam)
- ✅ Q&A session via video call
- ✅ Additional training materials jika diperlukan

---

### 3. PROSEDUR KLAIM GARANSI

Untuk mengklaim garansi, Pihak CUR-HEART dapat:

**Step 1**: Laporkan masalah via WhatsApp Group atau Email dengan format:
```
Subject: [BUG REPORT] Judul Masalah
- Deskripsi masalah:
- Langkah untuk reproduce:
- Screenshot/video (jika ada):
- Tingkat urgensi: Critical/High/Medium/Low
```

**Step 2**: Tim kami akan merespon dalam **1x24 jam** (working days) dengan:
- Konfirmasi penerimaan laporan
- Analisis masalah
- Estimasi waktu perbaikan

**Step 3**: Perbaikan dilakukan:
- Remote access (via Anydesk/Teamviewer)
- Push update ke server
- Testing bersama

**Step 4**: Konfirmasi penyelesaian dari CUR-HEART

---

### 4. BATASAN GARANSI

Garansi ini **TIDAK BERLAKU** untuk:

1. ❌ Kerusakan akibat **FORCE MAJEURE** (bencana alam, perang, server provider down, dll)
2. ❌ Kerusakan akibat **MODIFIKASI** oleh pihak ketiga tanpa koordinasi dengan kami
3. ❌ Kerusakan akibat **HUMAN ERROR** (salah hapus data, salah konfigurasi, dll)
4. ❌ Kerusakan akibat **HACKING/CYBER ATTACK** (kami sudah implement security best practices, tapi tidak menjamin 100% aman)
5. ❌ Kerusakan akibat **SERVER/HOSTING ISSUE** (downtime, slow performance karena server overload, dll)
6. ❌ **FEATURE REQUEST** atau perubahan requirement
7. ❌ **MAJOR UPDATES** (upgrade Laravel major version, database migration besar, dll)

---

### 5. POST-WARRANTY SUPPORT (OPSIONAL)

Setelah periode garansi habis (setelah 31 Januari 2025), CUR-HEART dapat memperpanjang support dengan skema **BERBAYAR**:

| Paket | Biaya | Cakupan |
|-------|-------|---------|
| **Monthly Retainer** | Rp 2.000.000/bulan | Technical support + bug fixes + minor updates |
| **Hourly Rate** | Rp 250.000/jam | On-demand support atau feature development |
| **Annual Maintenance** | Rp 20.000.000/tahun | Full support + updates + 1 major feature/year |

**Note**: Harga di atas dapat dinegosiasikan.

---

### 6. KONTAK SUPPORT

**WhatsApp Group**: CUR-HEART Support (sudah dibuat)

**Email**: support.curheart@students.nusamandiri.ac.id

**Contact Person**:
1. Roki Anjas (PM): +62 812-1111-0066
2. Susanto (Frontend): +62 812-2222-0068
3. Fahruroji (Backend): +62 812-3333-0085

**Working Hours**: Senin - Jumat, 09:00 - 17:00 WIB  
**Emergency Contact**: Available via WhatsApp (response time may vary)

---

### 7. PERNYATAAN PENUTUP

Dengan ditandatanganinya Surat Garansi ini, maka:

1. Tim Proyek berkomitmen untuk memberikan support terbaik dalam periode garansi.
2. CUR-HEART memahami batasan dan cakupan garansi yang diberikan.
3. Kedua belah pihak sepakat untuk berkomunikasi dengan baik dalam penyelesaian masalah.

Demikian Surat Garansi ini dibuat dengan sebenar-benarnya untuk dapat digunakan sebagaimana mestinya.

Jakarta, 1 November 2024

---

**Yang Memberikan Garansi,**

[Tanda Tangan]  
**Roki Anjas** (11250066)  
Project Manager  
Tim Proyek Capstone  
**Materai 10.000**

**Mengetahui,**

**Dosen Pembimbing**

[Tanda Tangan]  
**Rani Irma Handayani, M.Kom**  
NIDN: 0328068201  
**Materai 10.000**

---

**Yang Menerima Garansi,**

[Tanda Tangan + Stempel Perusahaan]  
**Dr. Sarah Wellness**  
Owner & Founder CUR-HEART  
**Materai 10.000**

---

## B.5 FOTO DOKUMENTASI SERAH TERIMA

### Galeri Foto Serah Terima Produk

**Tanggal**: 1 November 2024  
**Lokasi**: Kantor CUR-HEART, Jakarta Selatan  
**Fotografer**: Tim Dokumentasi UNM

---

**Keterangan Foto** (18 foto):

1. **Foto 01**: Tim Proyek tiba di kantor CUR-HEART (group photo di depan entrance)
2. **Foto 02**: Sesi pembukaan acara serah terima (semua peserta duduk di ruang meeting)
3. **Foto 03**: Presentasi overview sistem oleh Roki Anjas (PM) kepada stakeholder
4. **Foto 04**: Demo live sistem oleh Susanto (Frontend Developer) di laptop
5. **Foto 05**: Demo admin dashboard oleh Fahruroji (Full-stack Developer)
6. **Foto 06**: Owner (Dr. Sarah) mencoba sistem langsung di laptop
7. **Foto 07**: Terapis mencoba therapist dashboard (hands-on testing)
8. **Foto 08**: Admin (Rina) mencoba admin panel
9. **Foto 09**: Penyerahan dokumentasi lengkap (bundel buku user manual + technical docs)
10. **Foto 10**: Penyerahan external HDD 1TB berisi backup sistem
11. **Foto 11**: Penyerahan amplop berisi credentials & access (sealed envelope)
12. **Foto 12**: Penandatanganan Berita Acara Serah Terima oleh Tim Proyek
13. **Foto 13**: Penandatanganan Berita Acara oleh Owner CUR-HEART
14. **Foto 14**: Penandatanganan Surat Pengalihan Hak Cipta
15. **Foto 15**: Jabat tangan antara PM (Roki) dan Owner (Dr. Sarah) - simbolis serah terima
16. **Foto 16**: Group photo seluruh peserta dengan dokumen yang sudah ditandatangani
17. **Foto 17**: Foto bersama dengan plakat/certificate of appreciation (jika ada)
18. **Foto 18**: Foto santai di ruang terapi CUR-HEART (closing)

**Format**: JPEG (High Resolution, 300 dpi)  
**Lokasi File**: `/lampiran_b_dokumentasi/foto_serah_terima/`

---

## B.6 LAMPIRAN PENDUKUNG

### Daftar File yang Diserahkan dalam External HDD 1TB

```
CURHEART_BACKUP_FULL_20241101/
│
├── 01_sistem_aplikasi/
│   ├── source_code/
│   │   └── curheart-laravel.zip (full source code)
│   ├── database/
│   │   ├── curheart_schema.sql
│   │   ├── curheart_sample_data.sql
│   │   └── curheart_full_backup_20241101.sql
│   └── deployment/
│       ├── server_configuration.txt
│       └── deployment_checklist.pdf
│
├── 02_dokumentasi/
│   ├── user_manuals/
│   │   ├── user_manual_client_id.pdf
│   │   ├── user_manual_therapist_id.pdf
│   │   └── user_manual_admin_id.pdf
│   ├── technical_docs/
│   │   ├── installation_guide.pdf
│   │   ├── developer_documentation.pdf
│   │   ├── deployment_guide.pdf
│   │   └── maintenance_guide.pdf
│   └── training_materials/
│       ├── slides/ (3 sets)
│       ├── videos/ (3 videos, 9.5 jam total)
│       └── cheat_sheets/ (5 PDF)
│
├── 03_testing_reports/
│   ├── unit_testing_report.pdf
│   ├── feature_testing_report.pdf
│   ├── uat_report.pdf
│   ├── performance_testing_report.pdf
│   └── security_assessment_report.pdf
│
├── 04_visual_assets/
│   ├── screenshots/ (41 PNG files)
│   ├── videos/
│   │   ├── curheart_demo_full.mp4
│   │   └── curheart_highlights.mp4
│   ├── design_system/
│   │   └── [design system files]
│   └── marketing/
│       ├── xbanner_design.pdf
│       └── presentation_deck.pptx
│
├── 05_legal_documents/
│   ├── berita_acara_serah_terima.pdf
│   ├── surat_pernyataan_penerimaan.pdf
│   ├── ip_transfer_agreement.pdf
│   ├── warranty_letter.pdf
│   └── surat_keterangan_riset.pdf
│
└── README.txt (petunjuk akses semua file)
```

**Total Size**: ~50 GB  
**Format HDD**: NTFS (Windows & Mac compatible)  
**Backup Cloud**: Google Drive (shared dengan owner CUR-HEART)

---

## B.7 KESIMPULAN LAMPIRAN B

Dengan dilampirkannya semua dokumen serah terima di atas, maka:

1. ✅ **PROSES SERAH TERIMA** telah dilakukan secara **RESMI dan LENGKAP** pada tanggal 1 November 2024.

2. ✅ **SELURUH PRODUK** (sistem, dokumentasi, source code, database, training materials) telah diserahkan dalam kondisi **LENGKAP dan BERFUNGSI**.

3. ✅ **PIHAK CUR-HEART** telah menerima produk dengan **PUAS** dan menyatakan sistem siap digunakan untuk operasional.

4. ✅ **HAK KEPEMILIKAN INTELEKTUAL** telah dialihkan secara **PENUH dan RESMI** kepada CUR-HEART.

5. ✅ **GARANSI 3 BULAN** telah diberikan untuk bug fixing dan technical support.

6. ✅ **DOKUMENTASI LENGKAP** (foto, video, surat-surat) telah tersimpan dengan baik sebagai bukti.

---

**Lampiran B ini merupakan bukti SAH dan RESMI bahwa proses serah terima produk Capstone Project "Sistem Informasi CUR-HEART" telah dilakukan dengan baik, benar, dan sesuai prosedur.**

---

Jakarta, 1 November 2024

**Tim Proyek Capstone**

[Tanda Tangan]  
**Roki Anjas** (11250066) - Project Manager

[Tanda Tangan]  
**Susanto** (11250068) - Frontend Developer

[Tanda Tangan]  
**Fahruroji** (11250085) - Full-stack Developer

**Mengetahui,**

**Dosen Pembimbing**

[Tanda Tangan]  
**Rani Irma Handayani, M.Kom**  
NIDN: 0328068201

**Diterima oleh,**

[Tanda Tangan + Stempel]  
**Dr. Sarah Wellness**  
Owner CUR-HEART

---

**[END OF LAMPIRAN B]**
