# BAB II  
# TINJAUAN PUSTAKA

## 2.1 Landasan Teori

### 2.1.1 Sistem Informasi

Sistem informasi adalah kombinasi terorganisir dari manusia, hardware, software, jaringan komunikasi, dan sumber daya data yang mengumpulkan, mengubah, dan menyebarkan informasi dalam organisasi (O'Brien & Marakas, 2017). Menurut Stair & Reynolds (2018), sistem informasi terdiri dari 5 komponen: **Hardware** (komputer, server), **Software** (program, aplikasi), **Data** (fakta yang diproses), **People** (pengguna, IT staff), dan **Procedures** (kebijakan, aturan).

Sistem informasi CUR-HEART termasuk kategori **Transaction Processing System (TPS)** karena menangani transaksi pemesanan dan pembayaran, serta **Management Information System (MIS)** karena menyediakan pelaporan untuk pengambilan keputusan manajerial.

### 2.1.2 Manajemen Proyek Sistem Informasi

Manajemen proyek adalah aplikasi pengetahuan, keterampilan, dan teknik untuk memenuhi kebutuhan proyek (PMI, 2021). Konsep fundamental adalah **Triple Constraint**: Cakupan (*Scope*), Waktu (*Time*), dan Biaya (*Cost*) yang saling berkaitan. PMBOK Guide mengidentifikasi 10 knowledge areas: Integration, Scope, Schedule, Cost, Quality, Resource, Communications, Risk, Procurement, dan Stakeholder Management.

### 2.1.3 Siklus Hidup Pengembangan Sistem (SDLC)

SDLC adalah proses sistematis untuk mengembangkan sistem informasi (Dennis et al., 2020). **Model Waterfall** dipilih untuk proyek CUR-HEART dengan 6 fase sekuensial:

1. **Requirements Analysis**: Mengumpulkan dan mendokumentasikan kebutuhan sistem
2. **System Design**: Desain arsitektur, database, dan UI/UX
3. **Implementation**: Pengodean menggunakan Laravel Framework
4. **Testing**: Unit testing, integration testing, UAT
5. **Deployment**: Instalasi sistem di lingkungan produksi
6. **Maintenance**: Perbaikan bug dan peningkatan fitur

**Alasan Pemilihan Waterfall:**
- Persyaratan jelas dan stabil dari analisis proses bisnis
- Garis waktu tetap (11 minggu semester akademik)
- Dokumentasi lengkap diperlukan untuk capstone project
- Tim kecil (3 orang) dengan struktur jelas
- Budget minimal, tidak perlu tools kompleks

### 2.1.4 Hipnoterapi dan Kesehatan Mental

Hipnoterapi adalah metode terapi yang menggunakan teknik hipnosis untuk mengakses alam bawah sadar, membantu mengatasi trauma, stres, kecemasan, fobia, dan kebiasaan buruk (Yapko, 2012). Penelitian menunjukkan hipnoterapi memiliki tingkat keberhasilan 75-85% untuk gangguan kecemasan (Kirsch et al., 1995; Montgomery et al., 2002).

Di Indonesia, prevalensi gangguan mental mencapai 20% populasi (Riskesdas 2023) dengan tantangan: rasio tenaga kesehatan mental rendah, distribusi tidak merata, biaya tinggi, stigma sosial, dan kurangnya literasi kesehatan mental. Peluang layanan digital: kesadaran meningkat terutama generasi milenial/Z, penetrasi internet 75%, penerimaan telehealth, dan inisiatif pemerintah.

### 2.1.5 Laravel Framework

Laravel adalah framework PHP modern dengan arsitektur MVC yang menyediakan ekosistem lengkap: Eloquent ORM, Blade templating, Artisan CLI, authentication system, migration, dan queue management (Otwell, 2021). Laravel dipilih karena:

1. **Produktivitas tinggi**: Artisan CLI, boilerplate code generation
2. **Keamanan kuat**: CSRF protection, SQL injection prevention, XSS protection, bcrypt hashing
3. **Dokumentasi lengkap**: Komunitas besar, 15,000+ packages
4. **Integrasi mudah**: Blade + Tailwind CSS bekerja sempurna
5. **Cocok untuk proyek**: Full-stack web app dengan persyaratan kompleks

**Eloquent ORM** menyediakan abstraksi database dengan sintaksis ekspresif, relationship management (One-to-One, One-to-Many, Many-to-Many), query builder, mass assignment protection, timestamps otomatis, dan soft deletes.

**Blade Templating** memungkinkan template inheritance, components, control structures, data display dengan auto-escaping (XSS protection), dan CSRF protection.

### 2.1.6 Database Management System

MySQL 8.0 dipilih sebagai RDBMS karena:
- Cocok untuk data relasional terstruktur (Users, Bookings, Services dengan foreign keys)
- ACID compliance penuh (InnoDB engine) untuk transaksi pembayaran
- Integrasi sempurna dengan Laravel Eloquent ORM
- Biaya hosting Rp 0 (included di setiap VPS)
- Familiar bagi tim (SQL dari kuliah database)
- Support JSON data type untuk fleksibilitas (specializations array)

Database dirancang dengan **Normalisasi hingga 3NF** untuk menghindari redundansi dan menjaga integritas data. 16 tabel utama: Users, Therapists, Clients, Services, Bookings, Payments, Sessions, Reviews, dll.

### 2.1.7 Tailwind CSS

Tailwind CSS adalah framework CSS utility-first yang dipilih karena:
- **Customization tinggi**: Config file untuk brand colors CUR-HEART
- **File size kecil**: PurgeCSS menghasilkan 8KB (vs Bootstrap 25KB)
- **Mobile-first responsive**: Built-in breakpoints (sm, md, lg, xl, 2xl)
- **Konsistensi desain**: Predefined scale untuk spacing, colors, shadows
- **Maintainability**: Style co-located dengan HTML

Kombinasi Laravel + Tailwind CSS mendukung pengembangan efisien dengan hot-reload dan build optimization.

### 2.1.8 Keamanan Web

Implementasi keamanan web mengacu pada **OWASP Top 10 2021**:

1. **Authentication**: Laravel Sanctum untuk token-based auth, bcrypt password hashing, session management
2. **Authorization**: RBAC dengan Policies dan Gates, middleware untuk route protection
3. **SQL Injection**: Eloquent ORM dengan parameter binding otomatis
4. **XSS**: Blade auto-escaping output dengan `{{ }}`
5. **CSRF**: Token CSRF otomatis untuk POST/PUT/PATCH/DELETE
6. **Session Security**: HTTPS, secure cookies, httpOnly flag, session regeneration
7. **Data Encryption**: AES-256 untuk data sensitif, bcrypt untuk password
8. **Audit Trail**: Logging akses data klien untuk compliance

### 2.1.9 UI/UX Design

**User-Centered Design** (Norman, 2013) dengan prinsip:
- **Consistency**: Elemen UI konsisten di seluruh aplikasi
- **Feedback**: Sistem memberikan umpan balik jelas untuk setiap aksi
- **Simplicity**: Antarmuka sederhana, hapus elemen tidak perlu
- **Hierarchy**: Organisir konten dengan hierarki visual jelas
- **Accessibility**: Design untuk semua pengguna (WCAG 2.1)
- **Responsive Design**: Mobile-first approach (65% pengguna mobile)

**Design Process**: Research (observasi, wawancara) → Define (personas, user stories) → Ideate (wireframes, sketches) → Prototype (mockups Figma) → Test & Iterate (usability testing).

## 2.2 Penelitian Terkait

Analisis 6 penelitian terkait mengidentifikasi gap yang diatasi CUR-HEART:

**Gap Analysis Summary:**

| Gap | Deskripsi | Solusi CUR-HEART |
|-----|-----------|------------------|
| **Domain-Specific** | Penelitian fokus healthcare umum, bukan hipnoterapi | Template sesi spesifik hipnoterapi, dokumentasi trance state, metrik khusus |
| **Therapist Management** | Fitur terapis terbatas | Dashboard pendapatan, analytics kinerja, availability management fleksibel |
| **Multi-Step Booking** | Booking sederhana 1-2 langkah | Guided 4-step flow dengan progressive disclosure |
| **Progress Tracking** | Tracking klien komprehensif jarang | Self-assessment tools integration, progress graphs, goal tracking |
| **Integrated Payment** | Verifikasi pembayaran manual | Midtrans integration, multiple payment methods, auto verification |
| **Security & Privacy** | Keamanan dasar | RBAC, AES-256 encryption, audit trail, GDPR-inspired controls |
| **Responsive & Accessible** | Desktop-focused | Mobile-first (70% users), 6 breakpoints, WCAG 2.1 compliance |

**Posisi Penelitian:**
CUR-HEART adalah **solusi komprehensif, domain-specific, user-centered** untuk manajemen hipnoterapi, mengintegrasikan best practices dari penelitian existing dengan fitur inovatif yang mengatasi kebutuhan klinis dan bisnis spesifik.

---

**Tabel 2.1 Perbandingan Model SDLC**

| Model | Karakteristik | Kelebihan | Kekurangan | CUR-HEART Fit |
|-------|---------------|-----------|------------|---------------|
| **Waterfall** | Sekuensial, dokumentasi lengkap | Mudah dikelola, tonggak jelas, cocok tim kecil | Tidak fleksibel, luaran di akhir | ✅ **95%** DIPILIH |
| **Agile** | Iteratif, sprint 2-4 minggu | Fleksibel, luaran sering | Timeline unpredictable, dokumentasi minimal | ⚠️ 60% |
| **Spiral** | Berbasis risiko, iteratif | Risk management baik | Kompleks, mahal | ❌ 40% |

**Tabel 2.2 Perbandingan PHP Frameworks**

| Framework | Versi | Learning Curve | Performance | Community | CUR-HEART Fit |
|-----------|-------|----------------|-------------|-----------|---------------|
| **Laravel** | 10.x | Medium | Good | ⭐⭐⭐⭐⭐ | ✅ **95%** DIPILIH |
| **Symfony** | 6.x | Steep | Excellent | ⭐⭐⭐⭐ | ⚠️ 60% Too complex |
| **CodeIgniter** | 4.x | Easy | Very Good | ⭐⭐⭐ | ⚠️ 50% Too basic |

**Tabel 2.3 Perbandingan Database Systems**

| Database | Type | ACID | Performance | Scalability | CUR-HEART Fit |
|----------|------|------|-------------|-------------|---------------|
| **MySQL 8.0** | RDBMS | ✅ Full | Excellent | Good | ✅ **95%** DIPILIH |
| **PostgreSQL** | RDBMS | ✅ Full | Excellent | Excellent | ⚠️ 85% Good but overkill |
| **MongoDB** | NoSQL | ⚠️ Eventual | Very Good | Excellent | ❌ 50% Wrong data model |

**Tabel 2.4 Perbandingan CSS Frameworks**

| Framework | Approach | File Size | Customization | CUR-HEART Fit |
|-----------|----------|-----------|---------------|---------------|
| **Tailwind CSS** | Utility-first | 5-10 KB | Highly customizable | ✅ **95%** DIPILIH |
| **Bootstrap** | Component-based | 25-30 KB | Limited | ⚠️ 60% Generic look |
| **Bulma** | Component-based | 20-25 KB | Moderate | ⚠️ 55% Limited ecosystem |

**Tabel 2.5 Summary Penelitian Terkait**

| No | Penelitian | Teknologi | Fokus | Gap | Relevansi |
|----|-----------|-----------|-------|-----|-----------|
| 1 | Pratama & Kusumawati (2022) | PHP, MySQL | Hospital Management | Tidak ada tracking progress terapi | ⚠️ SEDANG |
| 2 | Chen et al. (2021) | Laravel, WebRTC | Mental Health Platform | Tidak fokus hipnoterapi | ⭐ TINGGI |
| 3 | Wijaya & Lestari (2023) | PHP | Salon Booking | Tidak ada dokumentasi sesi | ⚠️ SEDANG |
| 4 | Hartono et al. (2022) | Laravel, Tailwind | Clinic Booking | Multi-step booking tidak ada | ⭐⭐ SANGAT TINGGI |
| 5 | Nugroho & Setiawan (2021) | Framework Comparison | Performance Analysis | Justifikasi pilihan Laravel | ⚠️ SEDANG |
| 6 | Rahayu et al. (2023) | Figma | Mental Health UX | Prinsip design untuk CUR-HEART | ⭐ TINGGI |

---

**Kesimpulan Tinjauan Pustaka:**

Sistem informasi CUR-HEART dibangun dengan fondasi teori solid dan best practices dari penelitian terkait. Pemilihan teknologi (Laravel + MySQL + Tailwind CSS) dan metodologi (SDLC Waterfall) didasarkan pada analisis komprehensif yang mempertimbangkan persyaratan proyek, constraint waktu/budget, dan kebutuhan spesifik domain hipnoterapi. Sistem ini mengisi gap penelitian sebelumnya dengan menyediakan solusi komprehensif, aman, dan user-friendly untuk manajemen layanan kesehatan mental.
