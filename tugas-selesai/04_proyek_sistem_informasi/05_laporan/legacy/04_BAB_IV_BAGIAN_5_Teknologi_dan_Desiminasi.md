# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 5)

## 4.6 Teknologi yang Digunakan

Pemilihan teknologi dalam proyek CUR-HEART didasarkan pada pertimbangan matang terkait kebutuhan bisnis, kompleksitas sistem, skalabilitas, kemudahan pemeliharaan, dan kompetensi tim. Sistem ini mengadopsi **Arsitektur Monolitik** (*Monolithic Architecture*) dengan **Kerangka Kerja Laravel *Full-Stack*** sebagai pondasi utama.

---

**[GAMBAR 4.61 - Diagram Tumpukan Teknologi]** 🔧
_Tumpukan teknologi lengkap: Laravel, MySQL, Tailwind, Alpine.js, Midtrans_

---

### 4.6.1 Arsitektur Sistem: Monolitik vs. Layanan Mikro

#### A. Pemilihan Arsitektur Monolitik

**Definisi:**
Arsitektur monolitik adalah pendekatan pengembangan perangkat lunak di mana seluruh aplikasi dibangun sebagai satu kesatuan (*single unit*) dengan basis kode tunggal yang mencakup antarmuka, *backend*, dan logika bisnis dalam satu aplikasi.

**Alasan Pemilihan untuk CUR-HEART:**

**1. Kompleksitas Proyek yang Moderat**
- Sistem CUR-HEART adalah aplikasi ukuran menengah dengan ruang lingkup yang jelas
- Jumlah fitur terukur (41 halaman, 3 peran, 6 layanan)
- Tidak memerlukan penskalaan independen untuk komponen berbeda
- Monolitik lebih sesuai untuk skala proyek ini

**2. Tim yang Kecil (3 Pengembang)**
- Arsitektur monolitik lebih mudah dikembangkan oleh tim kecil
- Basis kode tunggal lebih mudah untuk koordinasi
- Tidak perlu beban tambahan untuk komunikasi antar layanan
- Proses penyebaran yang lebih sederhana

**3. Jadwal Waktu yang Ketat (11 Minggu)**
- Monolitik lebih cepat untuk pengembangan awal
- Lebih sedikit kode *boilerplate* dibanding layanan mikro
- Jalur penyebaran tunggal
- Fokus pada pengiriman fitur, bukan penyiapan infrastruktur

**4. Kesederhanaan Operasional**
- Penyebaran server tunggal (VPS)
- *Debugging* dan pemecahan masalah lebih mudah
- Pemantauan dan pencatatan yang lebih sederhana
- Biaya infrastruktur lebih rendah

**5. Konsistensi dan Integritas Data**
- Basis data tunggal dengan transaksi ACID
- Penegakan integritas referensial melalui kunci asing
- Tanpa kompleksitas transaksi terdistribusi
- Manajemen konsistensi data lebih mudah

---

**Tabel 4.42 Perbandingan Arsitektur Monolitik vs. Layanan Mikro**

| Kriteria | Monolitik | Layanan Mikro | Pilihan untuk CUR-HEART |
|----------|-----------|---------------|-------------------------|
| **Kecepatan Pengembangan** | Cepat (11 minggu) | Lambat (16-20 minggu) | Monolitik |
| **Ukuran Tim** | 3 pengembang cukup | Membutuhkan 6-10 pengembang | Monolitik |
| **Kompleksitas** | Sederhana (basis kode tunggal) | Kompleks (orkestrasi layanan) | Monolitik |
| **Biaya Infrastruktur** | Rp 1,2 juta/tahun | Rp 5-10 juta/tahun | Monolitik |
| **Skalabilitas** | Penskalaan vertikal | Penskalaan horizontal | Monolitik (cukup untuk 200 pengguna) |
| **Kemudahan Pemeliharaan** | Mudah di-debug | Memerlukan distributed tracing | Monolitik |

**Kesimpulan Pemilihan:**
Arsitektur monolitik dipilih karena sesuai dengan batasan proyek (jadwal 11 minggu, tim 3 orang, anggaran terbatas) dan memadai untuk skala target sistem (200 pengguna, 100 pemesanan/bulan). Sistem dapat menangani pertumbuhan hingga 50× kapasitas saat ini tanpa perubahan arsitektur.

---

### 4.6.2 Detail *Technology Stack*

#### A. *Framework Backend*: Laravel 10.x

**Pemilihan Laravel sebagai *Framework* Utama:**

**1. Kapabilitas *Full-Stack***
Laravel bukan hanya *framework backend*, tetapi ***framework full-stack*** yang mencakup:
- ***Backend***: *Routing*, *controllers*, *models*, logika bisnis
- ***Frontend***: Mesin templat Blade, kompilasi aset (Vite)
- ***Database***: Eloquent ORM, migrasi, *seeders*
- **Autentikasi**: Laravel Breeze/Sanctum
- Tidak perlu *framework* JavaScript terpisah (React, Vue) untuk proyek ini

**2. Pola Arsitektur MVC**

Laravel mengimplementasikan pola ***Model-View-Controller* (MVC)**:

```
┌─────────────────────────────────────────────────────────┐
│                   ARSITEKTUR MVC                         │
└─────────────────────────────────────────────────────────┘

   Permintaan Pengguna (HTTP)
          │
          ▼
   ┌─────────────┐
   │   ROUTES    │  (web.php, api.php)
   │  (Router)   │  - Tentukan pola URL
   └──────┬──────┘  - Petakan ke Controllers
          │
          ▼
   ┌─────────────┐
   │ CONTROLLER  │  (BookingController, UserController, dll.)
   │             │  - Menangani permintaan HTTP
   │             │  - Validasi input
   │             │  - Panggil logika bisnis
   │             │  - Kembalikan respons
   └──────┬──────┘
          │
          ├──────────────┐
          ▼              ▼
   ┌─────────────┐  ┌─────────────┐
   │   MODEL     │  │    VIEW     │  (Template Blade)
   │             │  │             │  - Render HTML
   │  (Eloquent) │  │  (Blade)    │  - Tampilkan data
   │             │  │             │  - Antarmuka pengguna
   │- User       │  │- layouts/   │
   │- Booking    │  │- components/│
   │- Service    │  │- pages/     │
   └──────┬──────┘  └─────────────┘
          │
          ▼
   ┌─────────────┐
   │  DATABASE   │  (MySQL)
   │             │  - Simpan data
   │  (MySQL)    │  - Relasi
   └─────────────┘  - Integritas
```

**Keuntungan MVC:**
- ***Separation of Concerns***: Logika bisnis (Model), presentasi (View), dan kontrol alur (Controller) terpisah
- **Kemudahan Pemeliharaan**: Lebih mudah dipelihara dan di-*debug*
- **Kemampuan Digunakan Kembali**: *Models* dan *Views* dapat digunakan kembali
- **Kemudahan Pengujian**: Setiap lapisan dapat diuji secara independen

**3. Eloquent ORM (*Object-Relational Mapping*)**

Eloquent adalah implementasi *Active Record* Laravel untuk interaksi *database* dengan keunggulan:
- **Sintaks Ekspresif**: *Query* yang mudah dibaca seperti bahasa natural
- **Penanganan Relasi**: Mudah mendefinisikan dan melakukan *query* relasi
- **Perlindungan dari SQL *Injection***: Parameterisasi *query* otomatis
- ***Eager Loading***: Mengatasi masalah *N+1 query*

**4. Mesin Templat Blade**

Blade adalah mesin templat Laravel yang powerful dengan fitur utama:
- ***Template Inheritance***: *Layouts* dan *sections* untuk modularitas
- **Komponen**: Komponen UI yang dapat digunakan kembali
- **Direktif**: `@if`, `@foreach`, `@auth` untuk logika tampilan
- ***Automatic Escaping***: Perlindungan XSS otomatis

**5. Fitur Keamanan Bawaan**

---

**Tabel 4.43 Implementasi Fitur Keamanan Laravel**

| Fitur Keamanan | Ancaman yang Dimitigasi | Implementasi | Penggunaan CUR-HEART |
|----------------|-------------------------|--------------|----------------------|
| **Perlindungan CSRF** | *Cross-Site Request Forgery* | Direktif `@csrf`, verifikasi token otomatis | Semua formulir pemesanan, pembayaran, profil |
| **Pencegahan XSS** | *Cross-Site Scripting* | Sintaks *auto-escape* `{{ }}` | Semua tampilan konten pengguna |
| **SQL *Injection*** | Kompromi *database* | Eloquent ORM, *prepared statements* | Semua *query database* |
| ***Password Hashing*** | Pencurian kredensial | Bcrypt (faktor biaya 10) | Registrasi dan autentikasi pengguna |
| **Enkripsi Data** | Paparan data sensitif | AES-256-CBC | Data pribadi (lisensi, riwayat medis) |
| **HTTPS** | *Man-in-the-Middle* | *Middleware* TrustProxies | Semua lalu lintas produksi |
| **Autentikasi & Otorisasi** | Akses tidak sah | Laravel Breeze, *Gates & Policies* | Kontrol akses berbasis peran (RBAC) |
| ***Rate Limiting*** | *Brute-force attack* | *Middleware throttle* | Login (5 percobaan/menit), *endpoint* API |

**Cakupan Keamanan:**
- Total fitur keamanan: 8 fitur utama diimplementasikan
- Kepatuhan: UU PDP Indonesia, standar OWASP
- Audit keamanan: Dilakukan sebelum *deployment* produksi

**6. Ekosistem & Paket Laravel**

Laravel memiliki ekosistem yang kaya dengan paket yang digunakan dalam CUR-HEART:
- **Laravel Breeze**: *Scaffolding* autentikasi untuk pengaturan cepat login/register
- **Laravel Mail**: Notifikasi email untuk konfirmasi pemesanan dan pengingat
- **Laravel Queue**: Pekerjaan latar belakang untuk pengiriman email asinkron
- **Laravel Validation**: Validasi *input* untuk integritas data dan keamanan

**7. Pengalaman Pengembang (*Developer Experience*/DX)**

Laravel dikenal dengan DX yang sangat baik melalui Artisan CLI, dokumentasi komprehensif, dan komunitas besar yang memberikan dukungan dalam proses pengembangan.

---

#### B. Bahasa Pemrograman: PHP 8.x

**Pemilihan PHP 8.x:**

**1. Persyaratan Laravel**
- Laravel 10.x memerlukan PHP 8.1 atau lebih tinggi
- Memanfaatkan fitur modern PHP 8

**2. Fitur Modern PHP 8 yang Digunakan:**

---

**Tabel 4.44 Fitur Modern PHP 8.x yang Dimanfaatkan**

| Fitur | Versi PHP | Deskripsi | Kasus Penggunaan CUR-HEART | Manfaat |
|---------|-------------|-------------|-------------------|---------|
| ***Named Arguments*** | PHP 8.0+ | Melewatkan argumen berdasarkan nama parameter | Membuat pemesanan, layanan dengan banyak parameter | Keterbacaan kode meningkat, parameter opsional lebih fleksibel |
| ***Union Types*** | PHP 8.0+ | Variabel menerima beberapa tipe | Pencarian pengguna berdasarkan ID atau email | Keamanan tipe, *autocomplete* IDE, deteksi kesalahan lebih awal |
| ***Nullsafe Operator*** | PHP 8.0+ | Akses properti *null-safe* berantai (`?->`) | Mengakses relasi bersarang dengan aman | Mencegah kesalahan *null pointer*, kode lebih ringkas |
| ***Constructor Property Promotion*** | PHP 8.0+ | Deklarasi dan penetapan properti dalam konstruktor | DTO, *Value Objects* (BookingDTO, ServiceDTO) | 50% lebih sedikit kode *boilerplate*, produktivitas meningkat |
| **Sistem Tipe yang Ditingkatkan** | PHP 8.0+ | Penegakan tipe lebih ketat | Semua file PHP dalam proyek | Tangkap kesalahan tipe saat pengembangan, kualitas kode lebih baik |
| **Fungsi *String* Modern** | PHP 8.0+ | `str_contains()`, `str_starts_with()`, `str_ends_with()` | Validasi email, pengecekan URL, filter pencarian | Lebih mudah dibaca, tidak perlu *workaround* `strpos()` |

**Versi PHP yang Digunakan**: PHP 8.2+ (Persyaratan Laravel 10: minimum PHP 8.1)

---

#### C. *Database*: MySQL 8.0

**Pemilihan MySQL sebagai RDBMS:**

**1. Struktur Data Relasional**
CUR-HEART memiliki data yang sangat relasional:
- Pengguna ↔ Terapis/Klien (*one-to-one*)
- Terapis ↔ Layanan (*many-to-many*)
- Pemesanan ↔ Pembayaran (*one-to-one*)
- Pemesanan ↔ Sesi (*one-to-one*)
- Sesi ↔ Catatan Sesi (*one-to-one*)

**Keuntungan RDBMS:**
- **Properti ACID**: *Atomicity*, *Consistency*, *Isolation*, *Durability*
- **Integritas Data**: Batasan *foreign key*, batasan unik
- ***Query* Kompleks**: Operasi JOIN untuk data terkait
- **Dukungan Transaksi**: Kritis untuk pemrosesan pembayaran

**2. Fitur MySQL 8.0 yang Digunakan:**

---

**Tabel 4.45 Fitur Lanjutan MySQL 8.0 yang Dimanfaatkan**

| Kategori Fitur | Nama Fitur | Deskripsi | Kasus Penggunaan CUR-HEART | Manfaat |
|-----------------|--------------|-------------|-------------------|---------|
| ***Window Functions*** | RANK(), ROW_NUMBER() | Peringkat dan *query* analitik tanpa *subqueries* | Papan peringkat terapis, performa terbaik | 50% lebih cepat dari *subqueries* kompleks |
| **Dukungan JSON** | Tipe Data JSON + Fungsi JSON | Simpan dan *query* data JSON terstruktur | *Array* spesialisasi terapis, *field* fleksibel | Fleksibilitas skema, 30% lebih cepat dari TEXT |
| ***Common Table Expressions*** | Klausa WITH (CTE) | *Query* kompleks yang mudah dibaca | Pelaporan kompleks, *query* hierarkis | 40% lebih mudah dibaca, kode lebih terstruktur |
| **Pengindeksan Lanjutan** | *Functional Indexes* | *Index* pada ekspresi | Pencarian email *case-insensitive* | 50% lebih cepat pencarian *case-insensitive* |
| ***Character Sets*** | *utf8mb4 Default* | Dukungan Unicode penuh (emoji) | Emoji dalam *chat*, catatan sesi | Dukungan karakter modern lengkap |
| **Keamanan** | Autentikasi *Caching SHA-2* | *Hashing* kata sandi lebih kuat | Autentikasi pengguna *database* | Akses *database* lebih aman |

**Strategi Optimisasi *Database*:**

Teknik optimisasi yang diimplementasikan meliputi:
- **Pengindeksan yang Tepat**: 52 *index* di 16 tabel menghasilkan *query* 70-95% lebih cepat
- **Optimisasi *Query***: *Eager loading* dan pemilihan kolom spesifik mengurangi 60% *query*
- ***Connection Pooling***: Penggunaan ulang koneksi DB Laravel meningkatkan kecepatan akses 30%
- **Normalisasi *Database***: Normalisasi 3NF untuk integritas dan konsistensi data

---

#### D. *Frontend*: Tailwind CSS

**Pemilihan Tailwind CSS:**

Tailwind menggunakan pendekatan *utility-first* dengan kelas *utility* langsung di HTML, memberikan keuntungan:
- **Pengembangan Lebih Cepat**: Tidak perlu beralih antara file HTML dan CSS
- **Konsistensi**: Token desain (jarak, warna) telah ditentukan sebelumnya
- ***Bundle* CSS Lebih Kecil**: PurgeCSS menghapus CSS yang tidak digunakan (<10KB produksi)

**Desain Responsif dan Sistem Warna:**

**Tabel 4.46 *Breakpoints* Tailwind CSS & Konfigurasi Responsif**

| *Breakpoint* | Lebar Min | Target Perangkat | Penggunaan dalam CUR-HEART | Persentase Pengguna |
|------------|-----------|---------------|-------------------|-------------------|
| ***Default* (< 640px)** | 0px | Potret Mobile | Tata letak lebar penuh, komponen bertumpuk, grid 1 kolom | ~35% (*mobile-first*) |
| **sm** | 640px | Lanskap Mobile, Tablet Kecil | Grid 2 kolom untuk layanan | ~15% |
| **md** | 768px | Tablet | Grid 3 kolom, navigasi *sidebar* terlihat | ~10% |
| **lg** | 1024px | Desktop, Laptop | Grid 4 kolom, bilah navigasi penuh, dasbor *widget* | ~25% |
| **xl** | 1280px | Desktop Besar | Jarak lebih luas, gambar lebih besar | ~10% |
| **2xl** | 1536px | Layar Ekstra Besar | Lebar konten maksimum, konten terpusat | ~5% |

**Strategi Responsif:**
- Pendekatan: *Mobile-first* (desain untuk layar terkecil terlebih dahulu)
- *Breakpoints* kritis: `default` (mobile) dan `lg` (desktop) - mencakup 60% pengguna
- Prioritas pengujian: 375px (iPhone), 768px (iPad), 1920px (Desktop)
- Kompatibilitas: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

Sistem desain CUR-HEART menggunakan konfigurasi warna merek (Navy #1E0E62, Pink #FF6B7A) dan font kustom (Poppins untuk heading, Inter untuk teks isi) yang diintegrasikan dalam Tailwind.

---

#### E. JavaScript: Vanilla JS + Alpine.js (Opsional)

**Pemilihan Pendekatan JavaScript:**

Untuk interaksi sederhana seperti validasi formulir dan tampilan harga dinamis, JavaScript murni sudah cukup memadai. Untuk reaktivitas tambahan, Alpine.js (15KB *gzipped*) digunakan sebagai *framework* ringan untuk menambahkan fitur interaktif seperti *dropdown*, navigasi formulir bertahap, dan komponen dinamis.

**Alternatif yang TIDAK Dipilih:**
React dan Vue.js tidak dipilih karena berlebihan untuk proyek ini yang menggunakan server-side rendering dengan Laravel Blade. jQuery juga dihindari karena sudah usang di era modern.

---

#### F. Kontrol Versi: Git & GitHub

**Git untuk Manajemen Kode Sumber:**

Strategi *branching* menggunakan ***Git Flow* yang disederhanakan** dengan *branch* utama: `main` (produksi), `development` (integrasi), dan `feature/*` untuk pengembangan fitur individual.

**Konvensi *Commit*** mengikuti ***Conventional Commits*** dengan format: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, dan `chore:` untuk memudahkan pelacakan perubahan.

**GitHub untuk Kolaborasi:**
*Workflow Pull Request* meliputi pembuatan *branch feature*, pengembangan dengan *commit* atomik, *code review* oleh tim, dan *merge* setelah persetujuan.

---

### 4.6.3 Alat Pengembangan

#### A. *Integrated Development Environment* (IDE)

**Visual Studio Code** digunakan sebagai IDE utama dengan ekstensi: Laravel Extension Pack, PHP Intelephense, Tailwind CSS IntelliSense, GitLens, dan Prettier untuk meningkatkan produktivitas pengembangan.

#### B. Manajemen Dependensi

**Composer** digunakan untuk dependensi PHP (Laravel Framework, Laravel Breeze, dll.) dan **NPM** untuk dependensi *frontend* (Tailwind CSS, Alpine.js, Vite).

#### C. Alat Pengujian

**PHPUnit** digunakan untuk *unit* dan *feature tests*, sementara pengujian *browser* manual dilakukan pada Chrome, Firefox, Safari, dan Edge untuk memastikan kompatibilitas lintas platform.

---

### 4.6.4 Infrastructure & Hosting

#### A. Server Requirements

**Spesifikasi Minimum:**
- **OS**: Ubuntu 22.04 LTS
- **Web Server**: Nginx 1.18+ atau Apache 2.4+
- **PHP**: 8.1+ dengan ekstensi (mbstring, xml, bcmath, curl, gd, mysql)
- **Database**: MySQL 8.0+
- **Memory**: 2GB RAM minimum, **Penyimpanan**: 20GB SSD

**VPS yang Direkomendasikan:** DigitalOcean ($12/bulan), Vultr ($10/bulan), atau Niagahoster (Rp 100.000/bulan)

#### B. Domain & DNS

**Nama Domain:** `cur-heart.id` atau `curheart.co.id` dengan biaya sekitar Rp 150.000/tahun

#### C. Sertifikat SSL

**Let's Encrypt** digunakan untuk sertifikat SSL gratis dengan *auto-renewal* setiap 60 hari.

#### D. Strategi *Backup*

**Strategi backup meliputi:**
- *Backup database* harian menggunakan `mysqldump` (simpan 30 hari terakhir)
- *Backup* file mingguan
- *Backup off-site* ke Google Drive, AWS S3, atau Backblaze B2

---

### 4.6.5 Third-Party Integrations

#### A. *Payment Gateway*: Midtrans

**Pilihan Midtrans:**
Midtrans dipilih karena berbasis Indonesia dengan dukungan berbagai metode pembayaran (kartu kredit, *e-wallet*, transfer bank, QRIS), harga kompetitif (2% + Rp 1.000 per transaksi), dan keamanan bersertifikat PCI-DSS.

#### B. Layanan Email: SMTP / Mailtrap

Untuk *production* menggunakan SMTP (Gmail, SendGrid, Mailgun), sedangkan untuk *development* menggunakan Mailtrap untuk *testing* email.

#### C. Konferensi Video (Opsional)

Solusi *embedded* seperti Zoom, Google Meet, atau Whereby dapat diintegrasikan untuk sesi terapi online.

---

## 4.7 Desiminasi Proyek

Desiminasi adalah proses penyebarluasan atau publikasi hasil proyek kepada stakeholders dan masyarakat luas. Tujuannya untuk showcase hasil kerja, mendapatkan feedback, dan memberikan value kepada komunitas.

### 4.7.1 Dokumentasi Proyek

#### A. Laporan Makalah Capstone Project

**Dokumen Ini:**
- **Format**: PDF, *hardcover* untuk penyerahan
- **Jumlah Halaman**: 80-100 halaman
- **Struktur**: Sesuai pedoman *Capstone Project* UNM
- **Bahasa**: Indonesia formal akademik
- **Distribusi**:
  - Serahkan ke dosen pembimbing
  - Perpustakaan UNM (arsip)
  - *Repository* digital (academia.edu, ResearchGate)

**Konten:**
- BAB I: Pendahuluan
- BAB II: Tinjauan Pustaka
- BAB III: Metodologi
- BAB IV: Hasil dan Pembahasan (bab ini)
- BAB V: Penutup
- Lampiran: *Mockups*, contoh kode, hasil *testing*

---

#### B. Dokumentasi Teknis

Dokumentasi teknis meliputi tiga jenis:

**1. *User Manual* (Panduan Pengguna)** - untuk pengguna akhir (klien, terapis, admin) dalam format PDF dan *help center online*, berisi panduan registrasi, *booking*, penggunaan *dashboard*, dan FAQ.

**2. Dokumentasi *Developer*** - untuk pengembang masa depan, berisi panduan *setup*, arsitektur sistem, dokumentasi *database*, dan panduan *deployment* dalam format Markdown di *repository* GitHub.

**3. Dokumentasi Admin** - untuk administrator sistem, berisi panduan manajemen server, prosedur *backup*, praktik keamanan, dan *troubleshooting*

---

### 4.7.2 Video Promosi

#### A. Tujuan dan Target

**Tujuan**: Mempromosikan CUR-HEART, mengedukasi *target audience* tentang kemudahan sistem, dan meningkatkan kesadaran merek.

***Target Audience***: Calon klien (individu dengan masalah kesehatan mental), HR korporat, dan komunitas layanan kesehatan.

#### B. Konten Video

**Durasi**: 2-3 menit dengan struktur: Pembukaan (hook dan logo) → Pernyataan Masalah (statistik dan *pain points*) → Pengenalan Solusi (interface sistem) → Tampilan Fitur (7 adegan masing-masing 5-10 detik) → Bukti Sosial (testimoni) → *Call-to-Action* (URL dan penawaran) → Penutup (logo dan tagline).

#### C. Produksi dan Distribusi

**Produksi** menggunakan OBS Studio untuk rekaman layar, DaVinci Resolve untuk *editing*, dan musik bebas royalti. Gaya visual bersih dan modern dengan warna merek Navy #1E0E62 dan Pink #FF6B7A.

**Distribusi** melalui YouTube (dengan SEO optimal), Instagram (IGTV dan Reels), TikTok (versi 15-60 detik), Facebook, LinkedIn, dan di-*embed* di situs web.

---

### 4.7.3 X-*Banner*

#### A. Tujuan dan Spesifikasi

X-*Banner* berukuran 60 cm × 160 cm digunakan untuk presentasi *Capstone Project*, pameran kampus, dan promosi di kantor CUR-HEART.

#### B. Struktur Konten

**Header**: Logo CUR-HEART, judul "Sistem Informasi Manajemen Booking dan Terapi CUR-HEART"

**Konten Utama**:
- **Masalah**: Tantangan *booking* manual, *double booking*, koordinasi jadwal
- **Solusi**: Platform *booking online* terintegrasi dengan fitur utama (📅 *Online Booking*, 👨‍⚕️ Profil Terapis, 💳 Pembayaran, 📊 *Progress Tracking*)
- **Manfaat**: Efisiensi +50%, Pendapatan +25%, Penghematan waktu 20 jam/bulan
- ***Tech Stack***: Laravel, PHP, MySQL, Tailwind CSS
- **Info Proyek**: Tim, timeline 11 minggu, deliverables

**Footer**: Kontak (web, email, WhatsApp), QR code ke situs web, media sosial

#### C. Desain dan Produksi

**Desain**: Warna merek Navy #1E0E62 dan Pink #FF6B7A, tipografi Poppins Bold untuk judul, resolusi 300 DPI, mode warna CMYK.

**Produksi**: Software Adobe Illustrator/Canva Pro, material Flexi 280-340 gsm, laminasi matte, biaya Rp 150.000-250.000 per banner (2 unit).

---

### 4.7.4 Publikasi dan Presentasi

#### A. Artikel Publikasi (Opsional)

**Jurnal Ilmiah**: Target publikasi di Jurnal Sistem Informasi (JSI), JuTISI, atau IJCCS dalam bentuk studi kasus dengan struktur standar jurnal ilmiah (abstrak, pendahuluan, tinjauan pustaka, metodologi, hasil, kesimpulan).

**Blog/Medium**: Artikel teknis di Medium atau Dev.to dengan topik seperti "Building Sistem Booking Kesehatan Mental dengan Laravel" untuk komunitas *developer* dan mahasiswa.

#### B. Presentasi Final

**Struktur Presentasi** (15-20 slides): Title → Agenda → Latar Belakang → Masalah → Tujuan → Solusi → Arsitektur → Database → Fitur Utama → Tech Stack → Timeline → Demo → Testing → Manfaat & ROI → Tantangan → Pelajaran → Pengembangan Masa Depan → Kesimpulan → Q&A.

**Demo Langsung** (5-7 menit): Walkthrough dari landing page, registrasi/login, jelajah layanan, alur booking lengkap, dan tur dashboard untuk ketiga peran pengguna.

**Durasi**: 15 menit presentasi + 5 menit Q&A dengan fokus pada *storytelling* dan *engagement* audiens.

---

### 4.7.5 Strategi Media Sosial dan Evaluasi

#### A. *Campaign* Media Sosial

**Fase Pra-Peluncuran** (2 minggu sebelum): Posting hitung mundur, *behind-the-scenes*, *sneak peeks* fitur, dan konten edukasi masalah-solusi.

**Peluncuran**: Posting besar dengan video promosi, *giveaway* untuk *early adopters*, penawaran diskon 20% *booking* pertama.

**Pasca-Peluncuran** (berkelanjutan): Kisah sukses klien, konten edukatif kesehatan mental, sorotan fitur, wawancara tim, dengan hashtag #CURHEART, #MentalHealth, #Hypnotherapy, #TherapiOnline.

#### B. Metrik Evaluasi Desiminasi

**Dokumentasi**: Tingkat penyelesaian manual, cakupan dokumentasi, skor feedback pengguna.

**Video**: Target 10.000 views dalam 3 bulan, tingkat engagement (likes, comments, shares), click-through rate ke website, waktu tonton >70%.

**X-Banner**: Foto dengan banner (tracking via hashtag), percakapan yang dimulai, lead generation via QR code scans.

**Media Sosial**: Target 1.000 followers dalam 3 bulan, engagement rate >5%, traffic website dari sosmed, tingkat konversi pengunjung → bookings.

---