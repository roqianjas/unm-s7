# BAB IV (Lanjutan)  
# HASIL PENELITIAN DAN PEMBAHASAN - PART 3

## 4.4. FAKTOR PENENTU KEBERHASILAN

Keberhasilan implementasi Sistem Informasi CUR-HEART ditentukan oleh berbagai faktor yang saling berkaitan. Faktor-faktor ini dibagi menjadi Faktor Kunci Keberhasilan (*Key Success Factors*/KSF), Faktor Kritis Keberhasilan (*Critical Success Factors*/CSF), dan Indikator Kinerja Utama (*Key Performance Indicators*/KPI).

### 4.4.1 Faktor Kunci Keberhasilan (*Key Success Factors*/KSF)

Faktor Kunci Keberhasilan adalah faktor-faktor kunci yang mendukung pencapaian tujuan proyek secara umum.

#### A. Faktor Teknologi

**1. Stabilitas dan Keandalan Sistem**
- Sistem harus mampu beroperasi 24/7 dengan *uptime* minimal 99,5%
- Waktu respons halaman tidak lebih dari 2 detik
- Optimasi *query database* untuk menangani pengguna bersamaan (*concurrent users*)
- Cadangan (*backup*) otomatis harian untuk keamanan data

**2. Antarmuka yang Mudah Digunakan**
- Desain UI/UX yang intuitif dan mudah dipahami
- Desain responsif (*responsive design*) untuk semua perangkat (desktop, tablet, mobile)
- Konsistensi bahasa desain menggunakan sistem desain (*design system*)
- Standar aksesibilitas (WCAG 2.1 Level AA)

**3. Keamanan Data**
- Enkripsi data sensitif (kata sandi/*password*, rekam medis/*medical records*)
- HTTPS untuk semua komunikasi
- Autentikasi dan otorisasi yang kuat
- Kepatuhan terhadap UU PDP (Perlindungan Data Pribadi)

**4. Skalabilitas**
- Arsitektur yang dapat menangani pertumbuhan pengguna
- Normalisasi basis data untuk efisiensi penyimpanan (*storage*)
- Mekanisme *caching* untuk optimasi kinerja

#### B. Faktor Manusia

**1. Kompetensi Tim Pengembang**
- Penguasaan *framework* Laravel dan pemrograman PHP
- Pemahaman desain basis data dan MySQL
- Kemampuan pengembangan *frontend* (HTML, CSS, JavaScript, Tailwind)
- Pengetahuan kontrol versi/*version control* (Git)

**2. Komitmen Pemangku Kepentingan**
- Dukungan penuh dari manajemen CUR-HEART
- Keterlibatan aktif pemilik dalam pengumpulan kebutuhan
- Umpan balik konstruktif dari terapis dan admin
- Kesediaan untuk pengujian dan UAT (*User Acceptance Testing*)

**3. Tingkat Adopsi Pengguna**
- Pelatihan yang memadai untuk terapis dan admin
- Panduan pengguna yang komprehensif
- Dukungan teknis yang responsif
- Manajemen perubahan yang efektif

#### C. Faktor Manajemen Proyek

**1. Perencanaan yang Matang**
- Ruang lingkup yang jelas dan terukur
- Jadwal yang realistis (11 minggu)
- Alokasi sumber daya yang optimal
- Strategi mitigasi risiko yang efektif

**2. Komunikasi yang Efektif**
- Pertemuan rutin mingguan (*weekly standup*)
- Dokumentasi yang jelas
- Pelacakan kemajuan dengan diagram Gantt (*Gantt chart*)
- Pelacakan isu dan penyelesaian

**3. Jaminan Kualitas**
- Pengujian sistematis di setiap fase
- Tinjauan kode dan pemrograman berpasangan (*pair programming*)
- Pelacakan bug dan prioritas perbaikan
- Perbaikan berkelanjutan berdasarkan umpan balik

### 4.4.2 Faktor Kritis Keberhasilan (*Critical Success Factors*/CSF)

Faktor Kritis Keberhasilan adalah faktor-faktor yang **HARUS** dipenuhi agar proyek berhasil.

**CSF 1: Ketersediaan dan Keandalan Sistem**
- Target: Waktu aktif (*uptime*) ≥ 99,5%, Waktu respons < 2 detik
- Dapat menangani minimal 100 pengguna bersamaan
- Tidak ada kehilangan data dalam kondisi normal

**CSF 2: Keamanan dan Privasi Data**
- Tidak ada pelanggaran keamanan atau akses tidak sah
- Semua data sensitif terenkripsi
- Implementasi HTTPS untuk semua halaman
- *RBAC* (*Role-Based Access Control*) berfungsi dengan baik

**CSF 3: Adopsi dan Kepuasan Pengguna**
- Minimal 70% klien menggunakan sistem untuk pemesanan
- Skor kepuasan pengguna ≥ 4,0 dari 5,0
- Skor SUS (*System Usability Scale*) ≥ 68
- Tingkat adopsi terapis 100%

**CSF 4: Integrasi dengan Proses Bisnis**
- 100% pemesanan melalui sistem (tidak ada lagi manual)
- Pengurangan beban kerja administratif minimal 50%
- Pengurangan kesalahan pemesanan hingga 90%
- Laporan dapat dihasilkan dalam 5 menit

**CSF 5: Kepatuhan Anggaran dan Jadwal**
- Penyelesaian proyek dalam 11 minggu (± 1 minggu toleransi)
- Biaya aktual tidak melebihi 110% anggaran (Rp 5,5 juta)
- Semua luaran selesai sesuai ruang lingkup

### 4.4.3 Indikator Kinerja Utama (*Key Performance Indicators*/KPI)

KPI adalah metrik terukur untuk memantau keberhasilan sistem setelah penerapan.

**Tabel 4.8 - Key Performance Indicators (KPI)**

| Kategori | Nama KPI | Target | Frekuensi Pemantauan |
|----------|----------|--------|---------------------|
| **Kinerja Sistem** | Waktu Aktif Sistem (*Uptime*) | ≥ 99,5% | Waktu nyata (*real-time*) |
| | Waktu Respons | ≤ 2 detik | Mingguan |
| | Tingkat Galat (*Error Rate*) | ≤ 0,5% | Harian |
| **Keamanan** | Kerentanan Keamanan (*Security Vulnerabilities*) | 0 kritis | Bulanan |
| | Insiden Pelanggaran Data (*Data Breach Incidents*) | 0 | Waktu nyata (*real-time*) |
| **Adopsi Pengguna** | Total Pengguna Terdaftar | 200 dalam 3 bulan | Bulanan |
| | Pengguna Aktif Bulanan (*Monthly Active Users*) | 150 (75%) | Bulanan |
| | Tingkat Konversi Pemesanan (*Conversion Rate*) | ≥ 60% | Mingguan |
| **Transaksi** | Total Pemesanan/Bulan | 100 pemesanan | Bulanan |
| | Tingkat Keberhasilan Pembayaran (*Payment Success Rate*) | ≥ 95% | Mingguan |
| | Pendapatan/Bulan | Rp 30 juta | Bulanan |
| **Kepuasan** | Skor Kepuasan Pengguna | ≥ 4,0/5,0 | Per pemesanan |
| | Skor NPS (*Net Promoter Score*) | ≥ 30 | Triwulanan |
| | Skor SUS (*System Usability Scale*) | ≥ 68 | Triwulanan |
| **Efisiensi** | Rata-rata Waktu Pemesanan | ≤ 3 menit | Mingguan |
| | Pengurangan Beban Kerja Admin | ≥ 50% | Bulanan |
| | Waktu Pembuatan Laporan | ≤ 5 menit | Bulanan |

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
- **Pengurangan tidak hadir**: Dari 15% menjadi 5% dengan pengingat otomatis (Rp 28,8 juta/tahun pendapatan dipulihkan)
- **Perpanjangan jam layanan**: Pemesanan 24/7 menangkap 15% lebih banyak klien (Rp 10 juta/tahun)
- **Retensi klien**: Peningkatan dari 35% menjadi 60% dengan pengalaman yang lebih baik

**C. Kualitas & Layanan**

- **Pengambilan keputusan berbasis data**: Dasbor waktu nyata untuk analisis cepat
- **Pemantauan kualitas**: Sistematis dengan target SUS ≥ 68, NPS ≥ 30
- **Skalabilitas**: Sistem digital dapat mendukung pertumbuhan 5× tanpa tambahan staf

**Total Manfaat Tahunan Terukur:**
- Peningkatan Pendapatan: Rp 115,8 juta/tahun
- Penghematan Biaya: Rp 18,4 juta/tahun
- **TOTAL**: Rp 134,2 juta/tahun

### 4.5.2 Manfaat untuk Klien

**A. Kenyamanan**

- Pemesanan 24/7 kapan saja tanpa terbatas jam kantor
- Tidak perlu telepon, layanan mandiri daring
- Ramah perangkat seluler untuk pemesanan saat bepergian
- Penjadwalan ulang mudah tanpa koordinasi manual

**B. Transparansi**

- Profil terapis lengkap dengan pendidikan, spesialisasi, dan ulasan
- Ketersediaan waktu nyata dengan kalender visual
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

### 4.5.4 Analisis Laba atas Investasi (*Return on Investment*/ROI)

**Investasi:**
- Biaya awal: Rp 3.000.000 (pengaturan/*setup*)
- Biaya berulang tahun 1: Rp 9.750.000 (*hosting*, domain, *payment gateway*)
- **Total biaya tahun 1: Rp 12.750.000**

**Manfaat Tahun 1:**
- Peningkatan pendapatan: Rp 142.800.000
- Penghematan biaya: Rp 26.400.000
- **Total manfaat: Rp 169.200.000**

**Hasil:**
- Manfaat bersih: Rp 156.450.000
- **ROI: 1.227%**
- **Periode pengembalian (*payback period*): 0,9 bulan (~27 hari)**
- Rasio Manfaat-Biaya: 13,3:1

**Proyeksi 5 Tahun:**
- Total manfaat: Rp 1.025.481.825
- Total biaya: Rp 60.098.000
- Manfaat bersih: Rp 964.383.829
- ROI 5 tahun: 7.258%

**Rekomendasi:** Proyek sangat layak dengan ROI luar biasa dan periode pengembalian (*payback period*) sangat singkat.

---

## 4.6. TEKNOLOGI YANG DIGUNAKAN

Teknologi yang digunakan untuk membangun Sistem Informasi CUR-HEART secara garis besar dapat dibagi ke dalam beberapa bagian berikut ini:

### 4.6.1 Server dan Infrastruktur

**A. *Web Server***
- **Nginx 1.18.0**: *Web server* berkinerja tinggi untuk menangani koneksi bersamaan (*concurrent connections*)
- **PHP 8.1**: Bahasa pemrograman sisi server (*server-side scripting language*) dengan fitur modern (kompilator *JIT*, argumen bernama/*named arguments*, atribut/*attributes*)

**B. *Hosting***
- **VPS (*Virtual Private Server*)**: Ubuntu Server 22.04 LTS
- Spesifikasi: 4 vCPU, 8GB RAM, 160GB Penyimpanan SSD (*SSD Storage*)
- SLA Waktu Aktif (*Uptime SLA*): 99,9%
- *Bandwidth*: Tidak terbatas (*Unlimited*)

**C. Server Basis Data**
- **MySQL 8.0**: Sistem manajemen basis data relasional
- *Storage Engine*: InnoDB untuk kepatuhan *ACID*
- *Backup*: Cadangan otomatis harian dengan retensi 30 hari

**D. Kontrol Versi**
- **Git & GitHub**: Manajemen kode sumber dan kolaborasi

### 4.6.2 Backend Development

**A. *Framework* & Bahasa**
- **Laravel 10**: *Framework* PHP modern dengan arsitektur MVC
  - *Eloquent ORM* untuk abstraksi basis data
  - *Blade templating engine*
  - *Middleware* untuk autentikasi & otorisasi
  - Sistem antrian untuk pekerjaan latar belakang
  - *Event* & *listener* untuk operasi asinkron

**B. Autentikasi & Otorisasi**
- Laravel Sanctum untuk autentikasi token API
- Laravel Permission (Spatie) untuk kontrol akses berbasis peran/*role-based access control* (RBAC)
- Bcrypt untuk *hashing* kata sandi

**C. Pustaka (*Libraries*) & Paket (*Packages*)**
- Midtrans PHP SDK untuk integrasi *payment gateway*
- Laravel Mail untuk notifikasi email
- Carbon untuk manipulasi tanggal/waktu
- Intervention Image untuk pemrosesan gambar

### 4.6.3 Pengembangan *Frontend*

**A. Teknologi**
- **HTML5**: *Markup* semantik modern
- **CSS3**: *Styling* dengan *flexbox* dan *grid*
- **JavaScript (ES6+)**: Interaktivitas dan konten dinamis
- **Alpine.js**: *Framework* JavaScript ringan untuk komponen reaktif

**B. *Framework* CSS**
- **Tailwind CSS 3.3**: *Framework* CSS berbasis utilitas (*utility-first*)
  - Desain responsif dengan pendekatan *mobile-first*
  - Palet warna dan tipografi kustom
  - Kompilator *JIT* (*Just-In-Time*) untuk optimasi
  - *PurgeCSS* untuk menghapus *styles* yang tidak digunakan

**C. Komponen UI**
- Pustaka komponen kustom berbasis Tailwind
- Ikon: Heroicons (set ikon SVG)
- Validasi formulir: Sisi klien (*client-side*) dengan JavaScript + sisi server (*server-side*) Laravel

### 4.6.4 Manajemen Basis Data

**A. Manajemen Basis Data**
- **MySQL 8.0**: Basis data utama
- Set Karakter (*Character Set*): utf8mb4 untuk dukungan Unicode penuh
- *Collation*: utf8mb4_unicode_ci

**B. Desain Basis Data**
- 16 tabel dengan normalisasi 3NF
- Batasan kunci asing (*foreign key*) untuk integritas referensial
- Indeks pada kolom yang sering di-*query*
- *Timestamps* untuk jejak audit

**C. Migrasi & *Seeding***
- Laravel *Migrations* untuk kontrol versi skema basis data
- *Seeders* untuk data sampel dan data pengujian

### 4.6.5 Integrasi & Layanan Eksternal

**A. *Payment Gateway***
- **Midtrans**: *Payment gateway* terintegrasi
  - *Snap API* untuk proses pembayaran (*checkout*) yang mulus
  - Dukungan: Kartu kredit, Transfer bank, Dompet digital (GoPay, OVO, Dana)
  - Keamanan: Memenuhi standar *PCI-DSS*
  - *Webhook* untuk notifikasi pembayaran

**B. Layanan Email**
- **SMTP (Mailtrap/SendGrid)**: Layanan pengiriman email
  - Email notifikasi (konfirmasi pemesanan, pengingat)
  - Email transaksional (reset kata sandi, email selamat datang)
  - Berbasis antrian untuk menghindari pemblokiran

**C. Penyimpanan Berkas**
- Penyimpanan lokal untuk pengembangan
- AWS S3 / DigitalOcean Spaces (siap untuk skala produksi)

### 4.6.6 Peralatan Pengembangan

**A. Kontrol Versi**
- **Git**: Sistem kontrol versi terdistribusi
- **GitHub**: *Hosting* repositori jarak jauh
- Strategi percabangan (*branching*): *GitFlow* (*main*, *develop*, *feature branches*)

**B. Editor Kode & IDE**
- Visual Studio Code dengan ekstensi:
  - Laravel Extension Pack
  - PHP Intelephense
  - Tailwind CSS IntelliSense
  - ESLint & Prettier

**C. Manajer Paket**
- **Composer**: Manajemen dependensi PHP
- **NPM**: Manajemen paket JavaScript

### 4.6.7 Pengujian

**A. *Framework* Pengujian**
- **PHPUnit**: Pengujian unit (*unit testing*) untuk logika *backend*
- **Laravel Dusk**: Pengujian otomasi peramban (*browser*)
- Pengujian fitur untuk titik akhir (*endpoint*) API

**B. Kualitas Kode**
- PHP Code Sniffer untuk standar pengodean
- Laravel Debugbar untuk pengawakutuan (*debugging*) pengembangan
- Pelacakan kesalahan (*error tracking*) & pemantauan (*monitoring*)

### 4.6.8 Penerapan (*Deployment*) & *DevOps*

**A. Penerapan (*Deployment*)**
- **GitHub Actions**: Otomasi CI/CD
- Pengujian otomatis sebelum penerapan
- Strategi penerapan tanpa *downtime* (*zero-downtime deployment*)

**B. Pemantauan (*Monitoring*)**
- **UptimeRobot**: Pemantauan waktu aktif (*uptime monitoring*)
- **New Relic / Laravel Telescope**: Pemantauan kinerja aplikasi (*application performance monitoring*)
- Pencatatan kesalahan (*error logging*) dengan Laravel Log

**C. Keamanan**
- **Let's Encrypt**: Sertifikat SSL/TLS gratis
- HTTPS ditegakkan untuk semua koneksi
- Perlindungan CSRF (bawaan Laravel)
- Pencegahan XSS
- Pencegahan injeksi SQL (*SQL injection*) (Eloquent ORM)
- Pembatasan laju (*rate limiting*) untuk titik akhir (*endpoint*) API

### 4.6.9 Desain & Pembuatan Prototipe

**A. Desain UI/UX**
- **Figma**: Peralatan desain untuk *wireframes* dan *mockups*
- 41 halaman *mockup* untuk semua peran pengguna
- Sistem desain dengan palet warna dan tipografi

**B. Peralatan Diagram**
- **Draw.io / Lucidchart**: ERD, *Use Case*, Diagram Aktivitas
- **StarUML**: Diagram kelas dan diagram sekuens

### 4.6.10 Manajemen Proyek

**A. Perencanaan**
- **Microsoft Project / GanttProject**: Diagram Gantt dan WBS
- **Trello / Notion**: Manajemen tugas dan kolaborasi

**B. Dokumentasi**
- **Markdown**: Dokumentasi teknis
- **Swagger / Postman**: Dokumentasi API

### 4.6.11 Ringkasan Stack Teknologi

```
┌─────────────────────────────────────────┐
│         Klien (Peramban)                │
│  HTML5 | CSS3 | JavaScript | Alpine.js │
│         Tailwind CSS                    │
└─────────────┬───────────────────────────┘
              │ HTTPS
┌─────────────▼───────────────────────────┐
│         Web Server (Nginx)              │
└─────────────┬───────────────────────────┘
              │
┌─────────────▼───────────────────────────┐
│     Aplikasi (Laravel 10 + PHP 8.1)     │
│  MVC | Eloquent ORM | Blade Templates   │
│  Middleware | Queue | Events            │
└─────┬───────────────────────────┬───────┘
      │                           │
      ▼                           ▼
┌─────────────┐          ┌────────────────┐
│ Basis Data  │          │ API Eksternal  │
│ MySQL 8.0   │          │ - Midtrans     │
│ 16 Tabel    │          │ - Email SMTP   │
└─────────────┘          └────────────────┘
```

### 4.6.12 Alasan Pemilihan Teknologi

**Tabel 4.9 - Justifikasi Pemilihan Teknologi**

| Teknologi | Alasan Pemilihan |
|-----------|------------------|
| **Laravel 10** | *Framework* PHP terpopuler dengan ekosistem lengkap, dokumentasi sangat baik, dukungan komunitas kuat, dan fitur bawaan yang komprehensif |
| **MySQL 8.0** | Basis data relasional yang matang, andal, didukung luas, dan gratis (*open source*) |
| **Tailwind CSS** | Produktivitas tinggi, ukuran berkas kecil setelah *purge*, sangat dapat disesuaikan (*highly customizable*), dan pembuatan prototipe cepat (*rapid prototyping*) |
| **Nginx + PHP 8.1** | Kombinasi berkinerja tinggi untuk aplikasi lalu lintas tinggi (*high-traffic applications*) dengan jejak memori rendah (*memory footprint*) |
| **Midtrans** | *Payment gateway* lokal Indonesia dengan kepatuhan (*compliance*) dan dukungan terbaik, mendukung berbagai metode pembayaran lokal |
| **Alpine.js** | Alternatif ringan untuk Vue/React, cocok untuk aplikasi yang tidak terlalu kompleks |
| **Figma** | Standar industri untuk desain UI/UX dengan fitur kolaborasi yang sangat baik |
| **GitHub** | *Hosting* kontrol versi paling populer dengan integrasi CI/CD yang mudah |

---

_Catatan: BAB IV Part 3 ini merupakan lanjutan dari Part 2. Untuk bagian 4.7 Desiminasi Proyek, lihat Part 4._

---

