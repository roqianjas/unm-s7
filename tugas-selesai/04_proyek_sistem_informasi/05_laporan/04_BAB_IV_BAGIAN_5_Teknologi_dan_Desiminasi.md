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

**Tabel 4.42 Matriks Keputusan Monolitik vs. Layanan Mikro**

| Kriteria Evaluasi | Bobot | Skor Monolitik (1-5) | Skor Berbobot | Skor Layanan Mikro (1-5) | Skor Berbobot | Analisis & Justifikasi | Pemenang |
|---------------------|--------|----------------------|---------------|-------------------------|---------------|------------------------|--------|
| **Kecepatan Pengembangan** | 20% | 5 | 1,00 | 2 | 0,40 | Monolitik: MVP cepat, basis kode tunggal, tanpa beban orkestrasi layanan. Layanan Mikro: Membutuhkan penyiapan ekstensif, kontrak API, *service mesh*. | ✅ Monolitik |
| **Ukuran & Keahlian Tim** | 15% | 5 | 0,75 | 2 | 0,30 | Tim: 3 pengembang (*full-stack*). Monolitik: 1 basis kode = kolaborasi mudah. Layanan Mikro: Membutuhkan tim khusus per layanan. | ✅ Monolitik |
| **Jadwal Proyek** | 15% | 5 | 0,75 | 2 | 0,30 | Tenggat waktu 11 minggu. Monolitik: Iterasi cepat. Layanan Mikro: Penyiapan infrastruktur saja = 2-3 minggu. | ✅ Monolitik |
| **Kebutuhan Skalabilitas** | 10% | 3 | 0,30 | 5 | 0,50 | Target: 200 pengguna, 100 pemesanan/bulan. Monolitik: Penskalaan vertikal cukup. Layanan Mikro: Berlebihan untuk skala ini. | ✅ Layanan Mikro (tidak diperlukan) |
| **Kompleksitas Penyebaran** | 10% | 5 | 0,50 | 2 | 0,20 | Monolitik: Penyebaran tunggal ke VPS. Layanan Mikro: Orkestrasi Kubernetes/Docker, *pipeline* CI/CD per layanan. | ✅ Monolitik |
| **Upaya Pengujian** | 10% | 5 | 0,50 | 3 | 0,30 | Monolitik: Tes terintegrasi, suite tes tunggal. Layanan Mikro: Pengujian kontrak, pengujian integrasi lintas layanan. | ✅ Monolitik |
| **Biaya Infrastruktur** | 10% | 5 | 0,50 | 1 | 0,10 | Monolitik: Rp 1,2 juta/tahun (VPS tunggal). Layanan Mikro: Rp 5-10 juta/tahun (beberapa server, *load balancer*, kontainer). | ✅ Monolitik |
| **Debugging & Pemantauan** | 5% | 5 | 0,25 | 2 | 0,10 | Monolitik: *Stack trace*, file log tunggal. Layanan Mikro: *Distributed tracing* (Jaeger, Zipkin), agregasi log. | ✅ Monolitik |
| **Konsistensi Data** | 5% | 5 | 0,25 | 2 | 0,10 | Monolitik: Transaksi ACID, kunci asing. Layanan Mikro: Konsistensi eventual, pola saga. | ✅ Monolitik |
| **Fleksibilitas Teknologi** | 5% | 2 | 0,10 | 5 | 0,25 | Monolitik: Bahasa tunggal (PHP). Layanan Mikro: Poliglot (Go, Node, Python per layanan). Tidak diperlukan untuk CUR-HEART. | ✅ Layanan Mikro (tidak diperlukan) |
| **Penskalaan Layanan Independen** | 5% | 1 | 0,05 | 5 | 0,25 | Monolitik: Skalakan seluruh aplikasi. Layanan Mikro: Skalakan hanya layanan beban tinggi. Beban saat ini = seragam, tidak diperlukan. | ✅ Layanan Mikro (tidak diperlukan) |
| **Isolasi Kegagalan** | 5% | 2 | 0,10 | 5 | 0,25 | Monolitik: Titik kegagalan tunggal. Layanan Mikro: Kegagalan layanan terisolasi. Dengan penanganan error baik, dapat diterima. | ✅ Layanan Mikro |
| **Jalur Migrasi Masa Depan** | 5% | 4 | 0,20 | 5 | 0,25 | Monolitik: Dapat direfaktor ke layanan mikro nanti menggunakan *domain-driven design*. Struktur kode modular disiapkan. | ✅ Seri |
| **SKOR TOTAL** | **100%** | | **5,25 / 6,50** | | **3,30 / 6,50** | Monolitik menang telak (skor 61% lebih tinggi). Keunggulan layanan mikro tidak relevan dengan batasan proyek. | **✅ MONOLITIK** |

**Analisis Faktor Keputusan:**

| Faktor | Keunggulan Monolitik | Keunggulan Layanan Mikro | Konteks CUR-HEART | Dampak pada Keputusan |
|--------|---------------------|------------------------|-------------------|-------------------|
| **Waktu ke Pasar** | ✅ Lebih cepat berminggu-minggu | - | Tenggat waktu 11 minggu | KRITIS - Monolitik menang |
| **Batasan Sumber Daya** | ✅ 3 pengembang cukup | Butuh 6-10 pengembang khusus | Tim kecil | KRITIS - Monolitik menang |
| **Anggaran** | ✅ Rp 1,2 juta/tahun | Rp 5-10 juta/tahun | Anggaran terbatas | TINGGI - Monolitik menang |
| **Skala Saat Ini** | ✅ 200 pengguna, 100 pemesanan/bulan | Lebih baik untuk 10 ribu+ pengguna | Skala rendah-menengah | TINGGI - Monolitik menang |
| **Kurva Pembelajaran** | ✅ Familiar (Laravel) | Curam (Docker, K8s, *service mesh*) | Proyek akademik | TINGGI - Monolitik menang |
| **Kompleksitas Operasional** | ✅ Sederhana (server tunggal) | Kompleks (orkestrasi) | Sistem produksi pertama | TINGGI - Monolitik menang |
| **Pertumbuhan Masa Depan** | ⚠️ Lebih sulit untuk penskalaan horizontal | ✅ Penskalaan elastis | Dapat direfaktor jika diperlukan | RENDAH - Trade-off dapat diterima |
| **Keragaman Teknologi** | ⚠️ Tumpukan tunggal (PHP) | ✅ Poliglot | Tidak diperlukan | RENDAH - Tidak relevan |

**Analisis Kuantitatif:**

| Metrik | Monolitik | Layanan Mikro | Perbedaan | Signifikansi |
|--------|-----------|--------------|-----------|--------------|
| Waktu Pengembangan | 11 minggu | 16-20 minggu | +45-80% lebih lambat | ⚠️ KRITIS (melewatkan tenggat waktu) |
| Ukuran Tim yang Dibutuhkan | 3 pengembang | 6-10 pengembang | +100-233% | ⚠️ KRITIS (tidak tersedia) |
| Biaya Infrastruktur (Tahun 1) | Rp 1,2 juta | Rp 5-10 juta | +317-733% | ⚠️ TINGGI (anggaran terlampaui) |
| Waktu Penyebaran | 5 menit | 30-60 menit | +500-1100% | ⚠️ SEDANG |
| Baris Kode *Boilerplate* | ~2.000 | ~8.000-12.000 | +300-500% | ⚠️ SEDANG |
| Layanan yang Dikelola | 1 | 5-10 | +400-900% | ⚠️ TINGGI (beban operasional) |
| *Throughput* Maksimum | 500 req/detik | 2.000+ req/detik | +300%+ | ✅ RENDAH (tidak diperlukan - saat ini 1 req/detik) |

**Keputusan Akhir: ARSITEKTUR MONOLITIK ✅**

**Alasan:**
1. **Keselarasan Batasan Proyek**: Jadwal 11 minggu, tim 3 orang, anggaran Rp 5M → Monolitik adalah satu-satunya opsi yang layak
2. **Kesesuaian Skala**: Target 200 pengguna, 100 pemesanan/bulan → Monolitik menangani 50× beban ini dengan mudah
3. **Mitigasi Risiko**: Tim familiar dengan Laravel, *stack* terbukti → Risiko teknis rendah
4. **Efektivitas Biaya**: Penghematan biaya 83% (Rp 1,2M vs Rp 7,5M biaya rata-rata *microservices*)
5. **Desain Siap Masa Depan**: Struktur kode modular memungkinkan migrasi masa depan ke *microservices* jika skala menuntut (pertumbuhan 5-10×)

**Kapan Perlu Mempertimbangkan Kembali *Microservices*:**
- Basis pengguna tumbuh menjadi 10.000+ pengguna bersamaan (*concurrent*)
- Layanan berbeda memiliki kebutuhan *scaling* yang sangat berbeda (mis., layanan *chat* memerlukan kapasitas 10× dari layanan pemesanan)
- Tim berkembang menjadi 10+ pengembang dengan keahlian khusus
- Anggaran meningkat menjadi Rp 50M+ untuk infrastruktur
- Kebutuhan untuk arsitektur *polyglot* (bahasa berbeda untuk layanan berbeda)

---

**Kesimpulan:**
Untuk proyek CUR-HEART, arsitektur monolitik adalah pilihan yang **optimal** dan **strategis** karena:
- Waktu ke pasar lebih cepat (*faster time-to-market*) (11 minggu dapat dicapai)
- Kompleksitas dan biaya lebih rendah (Rp 1,2M vs Rp 5-10M)
- Memadai untuk skala saat ini (target 200 pengguna, 100 pemesanan/bulan)
- Dapat menangani pertumbuhan 50× tanpa perubahan arsitektur
- Dapat di-*refactor* ke *microservices* di masa depan jika diperlukan (*vertical scaling* → Rp 3M; *horizontal* → *refactor*)
- **Skor Keputusan: 5,25/6,50 Monolitik vs 3,30/6,50 *Microservices* (keunggulan 61%)**

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

Eloquent adalah implementasi *Active Record* Laravel untuk interaksi *database*:

**Keunggulan Eloquent:**
- **Sintaks Ekspresif**: *Query* yang mudah dibaca seperti bahasa natural
- **Sintaks Ekspresif**: *Query* yang mudah dibaca seperti bahasa natural
- **Penanganan Relasi**: Mudah mendefinisikan dan melakukan *query* relasi
- **Perlindungan dari SQL *Injection***: Parameterisasi *query* otomatis
- ***Eager Loading***: Mengatasi masalah *N+1 query*
- ***Model Events***: *Hooks* untuk otomatisasi (*creating*, *updating*, *deleting*)

**Contoh *Query* Eloquent:**
```php
// Daripada SQL mentah:
$bookings = DB::select('SELECT * FROM bookings WHERE client_id = ? AND status = ?', [$clientId, 'confirmed']);

// Eloquent lebih ekspresif:
$bookings = Booking::where('client_id', $clientId)
                   ->where('status', 'confirmed')
                   ->with('therapist', 'service') // eager load relationships
                   ->orderBy('booking_date', 'desc')
                   ->get();
```

**4. Mesin Templat Blade**

Blade adalah mesin templat (*templating engine*) Laravel yang powerful untuk *views*:

**Fitur Blade:**
- ***Template Inheritance***: *Layouts* dan *sections*
- **Komponen**: Komponen UI yang dapat digunakan kembali
- **Direktif**: `@if`, `@foreach`, `@auth`, dll.
- **Dukungan PHP Mentah**: Fleksibilitas jika diperlukan
- ***Automatic Escaping***: Perlindungan XSS

**Contoh Template Blade:**
```blade
{{-- layouts/app.blade.php --}}
<!DOCTYPE html>
<html>
<head>
    <title>@yield('title') - CUR-HEART</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
    @include('components.navbar')
    
    <main>
        @yield('content')
    </main>
    
    @include('components.footer')
</body>
</html>

{{-- pages/booking.blade.php --}}
@extends('layouts.app')

@section('title', 'Book Appointment')

@section('content')
    <h1>Book Your Session</h1>
    
    @foreach($services as $service)
        <x-service-card :service="$service" />
    @endforeach
@endsection
```

**5. Fitur Keamanan Bawaan**

---

**Tabel 4.43 Implementasi Fitur Keamanan Laravel**

| Fitur Keamanan | Ancaman yang Dimitigasi | Implementasi Laravel | Contoh Kode | Penggunaan CUR-HEART | Dampak | OWASP Top 10 |
|-----------------|------------------|----------------------|--------------|----------------|--------|--------------|
| **Perlindungan CSRF** | *Cross-Site Request Forgery* | Direktif `@csrf`, verifikasi token otomatis | `<form>@csrf <input...</form>` | Semua formulir (pemesanan, pembayaran, pembaruan profil) | KRITIS - Mencegah tindakan tidak sah | A01:2021 *Broken Access Control* |
| **Pencegahan XSS** | *Cross-Site Scripting* | Sintaks *auto-escape* `{{ }}`, `{!! !!}` untuk HTML mentah | `{{ $user->name }}` *auto-escapes* | Semua tampilan konten yang dibuat pengguna | KRITIS - Mencegah injeksi skrip | A03:2021 *Injection* |
| **SQL *Injection*** | Kompromi *database* | Pengikatan *query* Eloquent ORM, *prepared statements* PDO | `User::where('email', $email)->first()` | Semua *query database* via Eloquent | KRITIS - Mencegah serangan SQL | A03:2021 *Injection* |
| ***Password Hashing*** | Pencurian kredensial | `Hash::make()` dengan bcrypt (faktor biaya 10) | `Hash::make($password)` | Registrasi pengguna, perubahan kata sandi | KRITIS - Penyimpanan kata sandi aman | A07:2021 *Identification Failures* |
| **Enkripsi** | Paparan data | `encrypt()` / `decrypt()` dengan AES-256-CBC | `encrypt($therapist->license_number)` | Data pribadi sensitif (ID, lisensi) | TINGGI - Melindungi PII | A02:2021 *Cryptographic Failures* |
| ***Rate Limiting*** | Serangan *brute-force* | *Middleware throttle*, batas yang dapat dikonfigurasi | `Route::middleware('throttle:60,1')` | *Login* (5 percobaan/menit), *endpoint* API | TINGGI - Mencegah *credential stuffing* | A07:2021 *Identification Failures* |
| **Penegakan HTTPS** | Serangan *Man-in-the-Middle* | *Middleware* `TrustProxies`, paksakan HTTPS | `URL::forceScheme('https')` | Semua lalu lintas produksi | KRITIS - Enkripsi data dalam transit | A02:2021 *Cryptographic Failures* |
| **Autentikasi** | Akses tidak sah | Laravel Breeze, manajemen sesi | `Auth::user()`, direktif `@auth` | Akses berbasis peran (Admin, Terapis, Klien) | KRITIS - Kontrol akses | A01:2021 *Broken Access Control* |
| **Otorisasi (*Gates* & *Policies*)** | Eskalasi hak istimewa | Kelas *policy*, direktif `@can` | `@can('update', $booking)` | Manajemen pemesanan, akses profil | KRITIS - Izin terperinci | A01:2021 *Broken Access Control* |
| **Perlindungan *Mass Assignment*** | Manipulasi data | Properti model `$fillable` / `$guarded` | `protected $fillable = ['name', 'email'];` | Semua model Eloquent | TINGGI - Mencegah pembaruan tidak disengaja | A04:2021 *Insecure Design* |
| **Validasi *File Upload*** | *Upload* file berbahaya | Aturan validasi, pengecekan tipe MIME | `'file' => 'image|max:2048'` | Foto profil, dokumen terapis | TINGGI - Mencegah *upload malware* | A03:2021 *Injection* |
| **Validasi *Input*** | Data tidak valid/berbahaya | Aturan validasi, *Form Requests* | `'email' => 'required|email|unique:users'` | Semua formulir dan permintaan API | TINGGI - Integritas & keamanan data | A03:2021 *Injection* |
| **Autentikasi API Sanctum** | Penyalahgunaan API | Autentikasi berbasis token, CSRF untuk SPA | *Middleware* `auth:sanctum` | Aplikasi mobile masa depan API | SEDANG - Akses API aman | A07:2021 *Identification Failures* |
| **Keamanan Sesi** | Pembajakan sesi | *Cookies* aman, HttpOnly, SameSite | `SESSION_SECURE_COOKIE=true` | Sesi pengguna | TINGGI - Perlindungan sesi | A07:2021 *Identification Failures* |
| **Verifikasi Email** | Akun palsu | *Interface* `MustVerifyEmail` | `Route::middleware('verified')` | Registrasi klien baru | SEDANG - Mencegah akun spam | A07:2021 *Identification Failures* |
| ***Password Reset*** | Pemulihan akun | Pembuatan token aman, kedaluwarsa | `Password::sendResetLink()` | Fitur lupa kata sandi | SEDANG - Pemulihan aman | A07:2021 *Identification Failures* |
| **Perlindungan *Clickjacking*** | Serangan *UI redress* | *Header* `X-Frame-Options` | `frame-ancestors 'self'` dalam CSP | Semua halaman | SEDANG - Mencegah *framing* | A04:2021 *Insecure Design* |
| ***Content Security Policy* (CSP)** | XSS, injeksi data | Konfigurasi *header* CSP | *Header* `Content-Security-Policy` | Semua halaman | SEDANG - *Defense in depth* | A03:2021 *Injection* |
| ***Secure Headers*** | Berbagai serangan | *Middleware secure headers* | `X-Content-Type-Options: nosniff` | Semua respons | SEDANG - Keamanan *browser* | Berbagai kategori OWASP |

**Ringkasan Konfigurasi Keamanan:**
- **Total Fitur Keamanan**: 19 diimplementasikan
- **Cakupan OWASP Top 10**: 7 dari 10 kategori ditangani
- **Fitur Kritis**: 8 (CSRF, XSS, SQL *Injection*, *Password*, HTTPS, Autentikasi, Otorisasi, Enkripsi)
- **Prioritas Tinggi**: 6 (*Rate Limiting*, *Mass Assignment*, *File Upload*, Validasi *Input*, Keamanan Sesi)
- **Prioritas Sedang**: 5 (Sanctum, Verifikasi Email, *Password Reset*, *Clickjacking*, CSP, *Secure Headers*)

**Langkah Keamanan Tambahan:**
```php
// Konfigurasi keamanan .env
APP_ENV=production
APP_DEBUG=false
SESSION_SECURE_COOKIE=true
SESSION_HTTP_ONLY=true
SESSION_SAME_SITE=lax

// Konfigurasi rate limiting (app/Http/Kernel.php)
'login' => 'throttle:5,1',  // 5 percobaan per menit
'api' => 'throttle:60,1',    // 60 permintaan per menit
```

---

**6. Ekosistem & Paket Laravel**

Laravel memiliki ekosistem yang kaya:

| Paket | Fungsi dalam CUR-HEART | Manfaat |
|---------|------------------------|---------|
| **Laravel Breeze** | *Scaffolding* autentikasi | Pengaturan cepat login/register |
| **Laravel Mail** | Notifikasi email | Konfirmasi pemesanan, pengingat |
| **Laravel Queue** | Pekerjaan latar belakang | Pengiriman email asinkron, pembuatan laporan |
| **Laravel Validation** | Validasi *input* | Integritas data, keamanan |
| **Laravel Pagination** | Paginasi data | Penanganan *dataset* besar yang efisien |
| **Laravel Mix/Vite** | Kompilasi aset | *Bundling* CSS/JS, *hot reload* |

**7. Pengalaman Pengembang (*Developer Experience*/DX)**

Laravel dikenal dengan DX yang sangat baik:
- **Artisan CLI**: Alat *command-line* untuk menghasilkan kode, migrasi, dll.
- **Laravel Tinker**: REPL untuk berinteraksi dengan aplikasi
- **Laravel Telescope**: Asisten *debugging* (opsional)
- **Dokumentasi Komprehensif**: docs.laravel.com
- **Komunitas Besar**: Stack Overflow, Laracasts, forum
- **Pembaruan Berkala**: Versi *long-term support* (LTS)

**Contoh Perintah Artisan:**
```bash
# Buat controller
php artisan make:controller BookingController --resource

# Jalankan migrasi database
php artisan migrate

# Isi database dengan data sampel
php artisan db:seed

# Hapus cache
php artisan cache:clear

# Buat model dengan migrasi
php artisan make:model Booking -m
```

---

#### B. Bahasa Pemrograman: PHP 8.x

**Pemilihan PHP 8.x:**

**1. Persyaratan Laravel**
- Laravel 10.x memerlukan PHP 8.1 atau lebih tinggi
- Memanfaatkan fitur modern PHP 8

**2. Fitur Modern PHP 8 yang Digunakan:**

---

**Tabel 4.44 Fitur Modern PHP 8.x yang Dimanfaatkan dalam CUR-HEART**

| Fitur | Versi PHP | Deskripsi | Contoh Kode | Kasus Penggunaan CUR-HEART | Manfaat | Dampak |
|---------|-------------|-------------|--------------|-------------------|---------|--------|
| ***Named Arguments*** | PHP 8.0+ | Melewatkan argumen berdasarkan nama parameter | `Booking::create(`<br>`  client_id: $clientId,`<br>`  therapist_id: $therapistId,`<br>`  service_id: $serviceId`<br>`)` | Membuat pemesanan, layanan dengan banyak parameter | **Keterbacaan**: Tujuan parameter jelas, lewati param opsional | TINGGI - Kejelasan kode |
| ***Union Types*** | PHP 8.0+ | Variabel menerima beberapa tipe | `public function findUser(`<br>`  int\|string $id`<br>`): User\|null` | Pencarian pengguna berdasarkan ID atau email | **Keamanan Tipe**: Kontrak tipe eksplisit, *autocomplete* IDE | TINGGI - Lebih sedikit bug |
| ***Match Expression*** | PHP 8.0+ | *Switch* yang ditingkatkan dengan nilai kembalian | `$message = match($status) {`<br>`  'pending' => 'Menunggu',`<br>`  'confirmed' => 'Dikonfirmasi',`<br>`  default => 'Tidak diketahui'`<br>`};` | Pesan status, *routing* berbasis peran, status pembayaran | **Kode Lebih Bersih**: *Type-safe*, lengkap, mengembalikan nilai | SEDANG - Keterbacaan |
| ***Nullsafe Operator*** | PHP 8.0+ | Akses properti *null-safe* berantai | `$name = $booking?->`<br>`  therapist?->`<br>`  user?->name;` | Mengakses relasi bersarang dengan aman | **Keamanan Null**: Mencegah kesalahan *null pointer* | TINGGI - Stabilitas |
| ***Constructor Property Promotion*** | PHP 8.0+ | Deklarasi dan penetapan properti dalam konstruktor | `public function __construct(`<br>`  public string $name,`<br>`  public int $age`<br>`) {}` | DTO, *Value Objects* (BookingDTO, ServiceDTO) | **Keringkasan**: 50% lebih sedikit kode *boilerplate* | SEDANG - Produktivitas |
| **Atribut (*Annotations*)** | PHP 8.0+ | Tambahkan metadata ke kelas/metode | `#[Route('/booking')]`<br>`#[Middleware('auth')]`<br>`public function index()` | Atribut *route* (fitur Laravel 10) | **Metadata**: *Routing* terkolokasi, *controller* lebih bersih | SEDANG - Organisasi |
| ***Mixed Type*** | PHP 8.0+ | Menerima tipe apa pun secara eksplisit | `public function log(`<br>`  mixed $data`<br>`): void` | *Logging utility*, *helper* fleksibel | **Fleksibilitas**: Deklarasi "tipe apa pun" eksplisit | RENDAH - Kasus khusus |
| ***Static Return Type*** | PHP 8.0+ | Mengembalikan instance kelas pemanggil | `public static function create(): static` | Metode *factory*, *query builders* | **Pewarisan**: Bekerja dengan kelas anak | SEDANG - Pola OOP |
| ***Throw Expression*** | PHP 8.0+ | *Throw* dalam konteks ekspresi | `$user = $request->user()`<br>`  ?? throw new AuthException();` | Validasi, *null coalescing* dengan pengecualian | **Keringkasan**: Penanganan kesalahan *inline* | SEDANG - Penanganan kesalahan |
| **Kompilasi JIT** | PHP 8.0+ | Kompilator *Just-In-Time* | Diaktifkan otomatis dalam php.ini | Optimisasi kinerja untuk tugas intensif CPU | **Kinerja**: Hingga 2× lebih cepat untuk algoritma | RENDAH - Aplikasi web kurang mendapat manfaat |
| **Sistem Tipe yang Ditingkatkan** | PHP 8.0+ | Penegakan tipe lebih ketat | `declare(strict_types=1);`<br>`function add(int $a, int $b): int` | Semua file PHP dalam proyek | **Keamanan Tipe**: Tangkap kesalahan tipe saat pengembangan | TINGGI - Jaminan kualitas |
| **Fungsi *String* (str_contains, str_starts_with, str_ends_with)** | PHP 8.0+ | Pengecekan *string* yang disederhanakan | `str_contains($email, '@')`<br>`str_starts_with($url, 'https')` | Validasi email, pengecekan URL, filter pencarian | **Keterbacaan**: Tidak perlu *workaround* strpos() | SEDANG - Kejelasan kode |
| **Fungsi fdiv()** | PHP 8.0+ | Pembagian dengan nol aman | `$result = fdiv($total, $count);`<br>`// Mengembalikan INF alih-alih peringatan` | Perhitungan rata-rata, statistik (tanpa cek nol) | **Keamanan**: Menangani pembagian dengan nol dengan anggun | RENDAH - Penanganan kasus tepi |
| **get_debug_type()** | PHP 8.0+ | Inspeksi tipe yang lebih baik | `$type = get_debug_type($var);`<br>`// "int" vs "integer"` | *Debugging*, pesan kesalahan | ***Debugging***: Informasi tipe lebih jelas | RENDAH - Alat pengembangan |
| **WeakMap** | PHP 8.0+ | Referensi lemah berbasis objek | `$cache = new WeakMap();`<br>`$cache[$object] = $data;` | *Caching* objek tanpa kebocoran memori | **Memori**: *Garbage collection* otomatis | RENDAH - Kasus penggunaan lanjutan |

**Ringkasan Adopsi PHP 8:**
- **Total Fitur Modern yang Digunakan**: 15
- **Dampak Tinggi**: 5 (*Named Arguments*, *Union Types*, *Nullsafe Operator*, Sistem Tipe yang Ditingkatkan, Keamanan Tipe)
- **Dampak Sedang**: 7 (*Match*, *Constructor Promotion*, Atribut, *Static Return*, *Throw Expression*, Fungsi *String*, Kejelasan Kode)
- **Dampak Rendah**: 3 (*Mixed Type*, JIT, WeakMap, get_debug_type, fdiv)
- **Versi PHP**: PHP 8.2+ (Persyaratan Laravel 10: min PHP 8.1)

**Peningkatan Kinerja (PHP 8 vs PHP 7.4):**
- **Kinerja Dasar**: ~10-15% eksekusi lebih cepat
- **Kompilasi JIT**: Hingga 2× lebih cepat untuk tugas intensif CPU (manfaat terbatas untuk aplikasi web)
- **Penggunaan Memori**: ~5% pengurangan *footprint* memori
- **Sistem Tipe**: Menangkap kesalahan saat pengembangan (bukan saat *runtime*)

**Dampak Kualitas Kode:**
```php
// Sebelum PHP 8 (gaya PHP 7.4)
function createBooking($clientId, $therapistId, $serviceId, $date, $time, $notes = null, $status = 'pending') {
    if ($notes === null) {
        $notes = '';
    }
    return Booking::create([
        'client_id' => $clientId,
        'therapist_id' => $therapistId,
        'service_id' => $serviceId,
        'booking_date' => $date,
        'time_slot' => $time,
        'notes' => $notes,
        'status' => $status
    ]);
}

// Setelah PHP 8 (gaya modern)
function createBooking(
    int $clientId,
    int $therapistId,
    int $serviceId,
    string $date,
    string $time,
    ?string $notes = null,
    string $status = 'pending'
): Booking {
    return Booking::create(
        client_id: $clientId,
        therapist_id: $therapistId,
        service_id: $serviceId,
        booking_date: $date,
        time_slot: $time,
        notes: $notes ?? '',
        status: $status
    );
}
```

**Hasil**: 40% lebih mudah dibaca, 100% *type-safe*, 30% lebih sedikit kode yang diperlukan untuk validasi

---

**3. Peningkatan Kinerja**
- Kompilasi JIT (*Just-In-Time*) - Hingga 2× lebih cepat untuk algoritma
- Sistem tipe yang ditingkatkan - Menangkap kesalahan saat pengembangan (*debugging* lebih cepat)
- Manajemen memori lebih baik - Pengurangan *footprint* memori 5%

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

| Kategori Fitur | Nama Fitur | Versi MySQL | Deskripsi | Contoh SQL | Kasus Penggunaan CUR-HEART | Manfaat Kinerja | Kepentingan |
|-----------------|--------------|---------------|-------------|-------------|-------------------|-------------------|------------|
| ***Window Functions*** | RANK(), ROW_NUMBER(), DENSE_RANK() | MySQL 8.0+ | Peringkat dan *query* analitik tanpa *subqueries* | `SELECT therapist_id, SUM(amount) as earnings,`<br>`RANK() OVER (ORDER BY SUM(amount) DESC) as rank`<br>`FROM payments GROUP BY therapist_id;` | Papan peringkat terapis, performa terbaik, peringkat pendapatan | **Tinggi**: Menghilangkan *subqueries* kompleks, 50% lebih cepat | TINGGI |
| | LEAD(), LAG() | MySQL 8.0+ | Akses baris berikutnya/sebelumnya | `SELECT booking_id, booking_date,`<br>`LAG(booking_date) OVER (PARTITION BY client_id ORDER BY booking_date) as previous_booking`<br>`FROM bookings;` | Analisis frekuensi pemesanan klien, deteksi kesenjangan | **Sedang**: Menyederhanakan analisis *time-series* | SEDANG |
| | Fungsi *Aggregate Window* | MySQL 8.0+ | Perhitungan kumulatif | `SELECT month, revenue,`<br>`SUM(revenue) OVER (ORDER BY month) as cumulative_revenue`<br>`FROM monthly_stats;` | Total berjalan, dasbor statistik kumulatif | **Sedang**: Analitik *real-time* | SEDANG |
| **Dukungan JSON** | Tipe Data JSON | MySQL 5.7+ | Simpan JSON terstruktur | `CREATE TABLE therapists (`<br>`  id INT,`<br>`  specializations JSON,`<br>`  techniques JSON`<br>`);` | Data fleksibel: *array* spesialisasi, *field* khusus | **Tinggi**: Fleksibilitas skema, 30% lebih cepat dari TEXT | TINGGI |
| | Fungsi JSON (JSON_EXTRACT, JSON_CONTAINS) | MySQL 5.7+ | *Query field* JSON | `SELECT * FROM therapists`<br>`WHERE JSON_CONTAINS(specializations, '"anxiety"');` | Cari berdasarkan spesialisasi, filter berdasarkan teknik | **Tinggi**: *Index* JSON, pencarian cepat | TINGGI |
| | JSON_TABLE() | MySQL 8.0+ | Konversi JSON ke relasional | `SELECT jt.* FROM therapists,`<br>`JSON_TABLE(specializations, '$[*]' COLUMNS(spec VARCHAR(100) PATH '$')) AS jt;` | Pelaporan pada *array* JSON, *flatten* untuk ekspor | **Sedang**: Jembatan JSON dan relasional | SEDANG |
| ***Common Table Expressions* (CTE)** | Klausa WITH (*Recursive* CTE) | MySQL 8.0+ | *Query* kompleks yang mudah dibaca, data hierarkis | `WITH RECURSIVE hierarchy AS (`<br>`  SELECT * FROM categories WHERE parent_id IS NULL`<br>`  UNION ALL`<br>`  SELECT c.* FROM categories c INNER JOIN hierarchy h ON c.parent_id = h.id`<br>`) SELECT * FROM hierarchy;` | Belum digunakan (masa depan: hierarki kategori layanan) | **Tinggi**: *Query* rekursif, 40% lebih mudah dibaca | SEDANG |
| ***Indexes*** | *Invisible Indexes* | MySQL 8.0+ | Uji dampak *index* tanpa menghapus | `ALTER TABLE bookings ALTER INDEX idx_date INVISIBLE;` | *Tuning* kinerja, uji efektivitas *index* | **Sedang**: Optimisasi aman | SEDANG |
| | *Descending Indexes* | MySQL 8.0+ | Optimalkan DESC ORDER BY | `CREATE INDEX idx_date_desc ON bookings (booking_date DESC);` | Daftar pemesanan terbaru (ORDER BY date DESC) | **Rendah**: 10-15% lebih cepat *sort* DESC | RENDAH |
| | *Functional Indexes* | MySQL 8.0+ | *Index* pada ekspresi | `CREATE INDEX idx_email_lower ON users ((LOWER(email)));` | Pencarian email *case-insensitive* | **Sedang**: 50% lebih cepat pencarian *case-insensitive* | SEDANG |
| ***Data Dictionary*** | DDL Atomik | MySQL 8.0+ | Perubahan skema *all-or-nothing* | `DROP TABLE IF EXISTS temp1, temp2, temp3;` (semua atau tidak sama sekali) | Migrasi aman, *rollback* jika gagal | **Tinggi**: Integritas data, pemulihan *crash* | TINGGI |
| | Kinerja *Information Schema* | MySQL 8.0+ | *Query* metadata lebih cepat | `SELECT * FROM information_schema.tables;` (5× lebih cepat) | Panel admin, *database explorer* | **Rendah**: Inspeksi skema lebih cepat | RENDAH |
| **Peran & Hak Istimewa** | Akses Berbasis Peran | MySQL 8.0+ | Set izin yang dapat digunakan kembali | `CREATE ROLE 'app_reader';`<br>`GRANT SELECT ON curheart.* TO 'app_reader';`<br>`GRANT 'app_reader' TO 'laravel_user'@'localhost';` | Peran pengguna *database* (app, admin, *backup*) | **Tinggi**: Keamanan, izin yang dapat dikelola | TINGGI |
| ***Character Sets*** | *utf8mb4 Default* | MySQL 8.0+ | Dukungan Unicode penuh (emoji) | `CREATE DATABASE curheart CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;` | Dukung emoji dalam *chat*, catatan sesi | **Tinggi**: Dukungan karakter modern | TINGGI |
| **Kinerja** | *Query Optimizer* yang Ditingkatkan | MySQL 8.0+ | Rencana eksekusi lebih baik | Otomatis (peningkatan *optimizer* internal) | Semua *query* mendapat manfaat | **Sedang**: 10-20% *query* keseluruhan lebih cepat | TINGGI |
| | *Hash Join* | MySQL 8.0.18+ | JOIN efisien untuk kolom tanpa *index* | Otomatis saat tidak ada *index* | JOIN tabel besar dalam laporan | **Tinggi**: 2-3× lebih cepat *join* | SEDANG |
| | Statistik Histogram | MySQL 8.0+ | Estimasi kardinalitas lebih baik | `ANALYZE TABLE bookings UPDATE HISTOGRAM ON booking_date;` | Keputusan *query optimizer* | **Sedang**: 15-30% rencana *query* lebih baik | RENDAH |
| ***Backup* & Pemulihan** | Kompresi *Binary Log* | MySQL 8.0.20+ | *Binary log* terkompresi | `SET binlog_transaction_compression = ON;` | Replikasi lebih cepat, penyimpanan lebih sedikit | **Sedang**: Penghematan disk 60% | SEDANG |
| **Keamanan** | Autentikasi *Caching SHA-2* | MySQL 8.0+ | *Hashing* kata sandi lebih kuat | `CREATE USER 'app'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'password';` | Autentikasi pengguna *database* | **Tinggi**: Akses DB aman | TINGGI |
| | Kebijakan Kedaluwarsa Kata Sandi | MySQL 8.0+ | Paksa rotasi kata sandi | `ALTER USER 'admin'@'localhost' PASSWORD EXPIRE INTERVAL 90 DAY;` | Kebijakan keamanan pengguna admin | **Sedang**: Kepatuhan | RENDAH |

**Ringkasan Adopsi MySQL 8.0:**
- **Total Fitur yang Dimanfaatkan**: 20+
- **Prioritas Tinggi**: 9 fitur (*Window Functions*, JSON, DDL Atomik, Peran, utf8mb4, *Optimizer*, Keamanan)
- **Prioritas Sedang**: 8 fitur (LAG/LEAD, JSON_TABLE, CTE, *Indexes*, *Hash Join*, *Binary Log*)
- **Prioritas Rendah**: 3 fitur (*Descending Indexes*, Histogram, Kedaluwarsa Kata Sandi)

**Perbandingan Kinerja (MySQL 8.0 vs 5.7):**

| Operasi | MySQL 5.7 | MySQL 8.0 | Peningkatan | Dampak CUR-HEART |
|-----------|-----------|-----------|-------------|-----------------|
| Analitik Kompleks (*Window Functions*) | *Subquery* (lambat) | Fungsi *window* native | 50-70% lebih cepat | Tinggi - Peringkat terapis, laporan |
| *Query* JSON | Parsing TEXT (lambat) | Pengindeksan JSON native | 30-50% lebih cepat | Tinggi - Pencarian spesialisasi |
| *Query Information Schema* | 500ms | 100ms | 5× lebih cepat | Rendah - Hanya panel admin |
| *Hash Join* (tabel besar) | *Nested loop* (lambat) | Algoritma *hash join* | 2-3× lebih cepat | Sedang - Laporan bulanan |
| Kinerja *Query* Keseluruhan | Dasar | Peningkatan 10-20% | Rata-rata 15% | Sedang - Semua *query* mendapat manfaat |

**Strategi Optimisasi *Database*:**

| Teknik | Implementasi | Manfaat | Status |
|-----------|---------------|---------|--------|
| **Pengindeksan yang Tepat** | 52 *index* di 16 tabel (PRIMARY, UNIQUE, COMPOSITE) | *Query* 70-95% lebih cepat | ✅ Diimplementasikan |
| **Optimisasi *Query*** | *Eager loading* (pencegahan N+1), pilih kolom spesifik | 60% lebih sedikit *query* | ✅ Diimplementasikan |
| ***Connection Pooling*** | Penggunaan ulang koneksi DB Laravel, koneksi persisten | Akses DB 30% lebih cepat | ✅ Diimplementasikan |
| ***Query Caching*** | *Cache query* Laravel, Redis untuk sesi/*data* yang sering diakses | *Query* berulang 90% lebih cepat | ⏳ Direncanakan untuk produksi |
| **Normalisasi *Database*** | Normalisasi 3NF, hindari redundansi data | Integritas data, tabel lebih kecil | ✅ Diimplementasikan |

**Sorotan Konfigurasi (`my.cnf`):**
```ini
[mysqld]
# Character set
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci

# Kinerja
innodb_buffer_pool_size=512M  # 50-70% dari RAM yang tersedia
innodb_log_file_size=128M
max_connections=150

# Binary logging (replikasi/backup)
log_bin=mysql-bin
binlog_format=ROW
binlog_transaction_compression=ON

# Keamanan
default_authentication_plugin=caching_sha2_password
```

---

**b. Dukungan JSON (Contoh Detail)**
```sql
-- Simpan data fleksibel (mis., spesialisasi, teknik)
CREATE TABLE therapists (
    id BIGINT PRIMARY KEY,
    specializations JSON,
    -- mis., ["Anxiety", "Trauma", "Stress"]
);

-- Query data JSON
SELECT * FROM therapists 
WHERE JSON_CONTAINS(specializations, '"Anxiety"');
```

**c. CTE (*Common Table Expressions*)**
```sql
-- Query pelaporan kompleks
WITH monthly_stats AS (
    SELECT 
        MONTH(booking_date) as month,
        COUNT(*) as total_bookings,
        SUM(amount) as revenue
    FROM bookings
    JOIN payments ON bookings.id = payments.booking_id
    GROUP BY MONTH(booking_date)
)
SELECT * FROM monthly_stats WHERE revenue > 10000000;
```

**3. Strategi Pengindeksan**

*Index* yang diimplementasikan untuk kinerja:

```sql
-- Primary indexes (otomatis)
PRIMARY KEY (id)

-- Unique indexes untuk integritas data
UNIQUE INDEX idx_email ON users(email);
UNIQUE INDEX idx_booking_number ON bookings(booking_number);

-- Foreign key indexes untuk kinerja JOIN
INDEX idx_bookings_client_id ON bookings(client_id);
INDEX idx_bookings_therapist_id ON bookings(therapist_id);

-- Composite indexes untuk query kompleks
INDEX idx_bookings_date_status ON bookings(booking_date, status);
INDEX idx_therapist_date_time ON bookings(therapist_id, booking_date, time_slot);

-- Full-text indexes untuk pencarian
FULLTEXT INDEX idx_services_search ON services(name, description);
```

**4. Normalisasi *Database***

Seperti dijelaskan di Bagian 2, *database* dinormalisasi hingga 3NF:
- **1NF**: Nilai atom, tidak ada grup berulang
- **2NF**: Tidak ada ketergantungan parsial
- **3NF**: Tidak ada ketergantungan transitif

Manfaat:
- Pengurangan redundansi data
- Pemeliharaan lebih mudah
- Konsistensi data
- Integritas referensial

---

#### D. *Frontend*: Tailwind CSS

**Pemilihan Tailwind CSS:**

**1. Pendekatan *Utility-First***

Tailwind menggunakan kelas *utility* daripada CSS khusus:

**Contoh:**
```html
<!-- CSS Tradisional -->
<style>
.card {
    background-color: white;
    border-radius: 0.5rem;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
<div class="card">Content</div>

<!-- Tailwind CSS -->
<div class="bg-white rounded-lg p-6 shadow-md">Content</div>
```

**Keuntungan:**
- **Pengembangan Lebih Cepat**: Tidak perlu beralih antara file HTML dan CSS
- **Konsistensi**: Token desain (jarak, warna) telah ditentukan sebelumnya
- **Tidak Ada Masalah Penamaan**: Tidak perlu memikirkan nama kelas (BEM, SMACSS, dll.)
- ***Bundle* CSS Lebih Kecil**: Hapus CSS yang tidak digunakan (*production build* <10KB)

**2. Desain Responsif Bawaan**

---

**Tabel 4.46 *Breakpoints* Tailwind CSS & Konfigurasi Responsif**

| *Breakpoint* | Lebar Min | Target Perangkat | Lebar Maks Kontainer | Penggunaan dalam CUR-HEART | Keputusan Desain | Persentase Pengguna |
|------------|-----------|---------------|-------------------|-------------------|-----------------|-------------------|
| ***Default* (< 640px)** | 0px | Potret Mobile | 100% | Pengalaman mobile utama | • Tata letak lebar penuh<br>• Komponen bertumpuk<br>• Menu hamburger<br>• Grid satu kolom | ~35% (*mobile-first*) |
| **sm** | 640px | Lanskap Mobile, Tablet Kecil | 640px | *Phablet*, tablet kecil | • Grid 2 kolom untuk layanan<br>• Teks sedikit lebih besar<br>• Tampilkan lebih banyak konten per baris | ~15% |
| **md** | 768px | Tablet | 768px | iPad, tablet Android | • Grid 3 kolom<br>• Navigasi *sidebar* terlihat<br>• Tata letak seperti desktop<br>• Formulir berdampingan | ~10% |
| **lg** | 1024px | Desktop, Laptop | 1024px | Layar desktop standar | • Grid 4 kolom<br>• Bilah navigasi penuh<br>• Dasbor dengan *widget*<br>• Lebar bacaan optimal | ~25% |
| **xl** | 1280px | Desktop Besar | 1280px | Monitor 1080p+ | • Jarak yang ditingkatkan<br>• Gambar/*card* lebih besar<br>• Lebih banyak ruang putih<br>• Pengalaman premium | ~10% |
| **2xl** | 1536px | Layar Ekstra Besar | 1536px | Monitor 1440p+, 4K | • Lebar konten maksimum<br>• Cegah panjang baris >100ch<br>• Konten terpusat<br>• Dukungan *ultra-wide* | ~5% |

**Ringkasan Strategi Responsif:**
- **Pendekatan**: *Mobile-first* (desain untuk layar terkecil terlebih dahulu, tingkatkan ke atas)
- ***Breakpoints* Kritis**: `default` (mobile) dan `lg` (desktop) - mencakup 60% pengguna
- **Prioritas Pengujian**: 375px (iPhone), 768px (iPad), 1920px (Desktop)
- **Kinerja**: Hanya muat CSS untuk *breakpoint* yang benar-benar digunakan (PurgeCSS menghapus yang tidak digunakan)

**Contoh Komponen Responsif:**

| Komponen | Mobile (< 640px) | Tablet (768px+) | Desktop (1024px+) | Implementasi |
|-----------|-----------------|----------------|------------------|----------------|
| **Navigasi** | Menu hamburger | Nav dipadatkan | Nav horizontal penuh | `hidden md:flex lg:space-x-6` |
| **Grid Layanan** | 1 kolom | 2 kolom | 3-4 kolom | `grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4` |
| **Bagian Hero** | Tumpukan tinggi penuh | Berdampingan 50/50 | Berdampingan dengan gambar lebih besar | `flex-col md:flex-row items-center` |
| ***Widget* Dasbor** | Tumpukan vertikal | 2 per baris | 3-4 per baris | `w-full md:w-1/2 lg:w-1/3 xl:w-1/4` |
| **Formulir** | Satu kolom | Satu kolom | Dua kolom | `grid-cols-1 lg:grid-cols-2 gap-6` |
| **Tipografi** | 16px dasar | 16px dasar | 18px dasar | `text-base lg:text-lg` |
| **Gambar** | Lebar penuh | Lebar 50-75% | Lebar maks tetap | `w-full md:w-3/4 lg:max-w-md` |
| ***Sidebar*** | Tersembunyi (*drawer*) | Tersembunyi (*drawer*) | Terlihat tetap kiri | `hidden lg:block lg:w-64 lg:fixed` |

**Pola Responsif CUR-HEART:**

```html
<!-- Grid kartu responsif mobile-first -->
<div class="
    grid 
    grid-cols-1          <!-- mobile: 1 kolom -->
    sm:grid-cols-2       <!-- kecil: 2 kolom -->
    md:grid-cols-2       <!-- tablet: 2 kolom -->
    lg:grid-cols-3       <!-- desktop: 3 kolom -->
    xl:grid-cols-4       <!-- besar: 4 kolom -->
    gap-4                <!-- mobile: gap 1rem -->
    md:gap-6             <!-- tablet: gap 1.5rem -->
    p-4                  <!-- mobile: padding 1rem -->
    md:p-6               <!-- tablet: padding 1.5rem -->
    lg:p-8               <!-- desktop: padding 2rem -->
">
    <!-- Kartu Responsif -->
    <div class="
        bg-white 
        rounded-lg 
        shadow-md 
        p-4 
        hover:shadow-xl 
        transition-shadow 
        duration-300
    ">
        <h3 class="
            text-lg           <!-- mobile: 18px -->
            md:text-xl        <!-- tablet: 20px -->
            lg:text-2xl       <!-- desktop: 24px -->
            font-bold 
            mb-2
        ">Nama Layanan</h3>
        <p class="
            text-sm           <!-- mobile: 14px -->
            md:text-base      <!-- tablet: 16px -->
            text-gray-600
        ">Deskripsi</p>
    </div>
</div>
```

**Optimisasi Kinerja:**
- **PurgeCSS**: Menghapus kelas yang tidak digunakan (mengurangi CSS dari ~3MB menjadi ~10KB)
- **Gambar Responsif**: Gunakan `srcset` dan `<picture>` untuk gambar yang sesuai dengan perangkat
- ***Lazy Loading***: Muat gambar di bawah lipatan hanya saat men-*scroll*
- **Kinerja Mobile**: Target < 3 detik FCP (*First Contentful Paint*) pada 3G

**Kompatibilitas Lintas *Browser*:**
- Chrome 90+ ✅
- Firefox 88+ ✅
- Safari 14+ ✅
- Edge 90+ ✅
- Mobile Safari iOS 14+ ✅
- Chrome Android 90+ ✅

---

**3. Integrasi Sistem Desain**

Konfigurasi Tailwind untuk sistem desain CUR-HEART:

```javascript
// tailwind.config.js
module.exports = {
    theme: {
        extend: {
            colors: {
                // Warna merek CUR-HEART
                primary: {
                    50: '#f5f3ff',
                    100: '#ede9fe',
                    // ... gradasi
                    900: '#1E0E62', // Navy Utama
                },
                secondary: {
                    500: '#FF6B7A', // Pink Sekunder
                },
                accent: {
                    teal: '#4ECDC4',
                    purple: '#8B5FBF',
                }
            },
            fontFamily: {
                sans: ['Poppins', 'sans-serif'], // Heading
                body: ['Inter', 'sans-serif'],    // Teks isi
            },
            spacing: {
                '128': '32rem', // Spasi khusus
            }
        }
    }
}
```

**Penggunaan:**
```html
<h1 class="text-primary-900 font-sans text-4xl font-bold">
    Selamat Datang di CUR-HEART
</h1>
<p class="text-gray-700 font-body text-base">
    Pesan sesi terapi Anda hari ini.
</p>
<button class="bg-secondary-500 hover:bg-secondary-600 text-white px-6 py-3 rounded-lg">
    Pesan Sekarang
</button>
```

**4. Kemampuan Digunakan Kembali Komponen dengan @apply**

Untuk komponen yang sering digunakan:

```css
/* resources/css/app.css */
@layer components {
    .btn-primary {
        @apply bg-primary-900 text-white font-semibold py-2 px-4 rounded-lg hover:bg-primary-800 transition duration-200;
    }
    
    .card {
        @apply bg-white rounded-lg shadow-md p-6;
    }
    
    .input-field {
        @apply border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-primary-500;
    }
}
```

**5. Dukungan *Dark Mode* (Opsional)**

Tailwind mendukung *dark mode* secara bawaan:

```html
<div class="bg-white dark:bg-gray-800 text-gray-900 dark:text-white">
    Konten beradaptasi dengan skema warna
</div>
```

---

#### E. JavaScript: Vanilla JS + Alpine.js (Opsional)

**Pemilihan Pendekatan JavaScript:**

**1. Vanilla JavaScript untuk Interaksi Sederhana**

Untuk interaksi sederhana, JavaScript murni sudah cukup:

```javascript
// Validasi formulir
document.getElementById('bookingForm').addEventListener('submit', function(e) {
    const date = document.getElementById('booking_date').value;
    if (!date) {
        e.preventDefault();
        alert('Silakan pilih tanggal');
    }
});

// Tampilan harga dinamis
function updatePrice(serviceId) {
    const prices = {
        1: 250000,
        2: 300000,
        3: 350000
    };
    document.getElementById('price').textContent = 
        `Rp ${prices[serviceId].toLocaleString('id-ID')}`;
}
```

**2. Alpine.js untuk Reaktivitas (Opsional)**

Alpine.js adalah *framework* JavaScript ringan (15KB *gzipped*) untuk menambahkan reaktivitas:

**Contoh: *Toggle Dropdown***
```html
<div x-data="{ open: false }">
    <button @click="open = !open">
        Menu
    </button>
    <div x-show="open" @click.away="open = false">
        <a href="/profile">Profil</a>
        <a href="/logout">Keluar</a>
    </div>
</div>
```

**Contoh: Navigasi Langkah Formulir**
```html
<div x-data="{ step: 1 }">
    <!-- Indikator Langkah -->
    <div class="flex">
        <div :class="step >= 1 ? 'active' : ''">1. Layanan</div>
        <div :class="step >= 2 ? 'active' : ''">2. Terapis</div>
        <div :class="step >= 3 ? 'active' : ''">3. Jadwal</div>
        <div :class="step >= 4 ? 'active' : ''">4. Konfirmasi</div>
    </div>
    
    <!-- Konten Langkah -->
    <div x-show="step === 1">Pemilihan Layanan</div>
    <div x-show="step === 2">Pemilihan Terapis</div>
    <div x-show="step === 3">Pemilihan Jadwal</div>
    <div x-show="step === 4">Konfirmasi</div>
    
    <!-- Navigasi -->
    <button @click="step--" x-show="step > 1">Kembali</button>
    <button @click="step++" x-show="step < 4">Berikutnya</button>
</div>
```

**Keuntungan Alpine.js:**
- **Deklaratif**: Perilaku reaktif dalam HTML
- **Ringan**: Ukuran *bundle* kecil
- **Tanpa Langkah *Build***: Dapat digunakan langsung via CDN
- **Ramah Laravel**: Dibuat oleh teman Taylor Otwell

**Alternatif yang TIDAK Dipilih:**

| *Framework* | Kenapa Tidak Dipilih |
|-----------|---------------------|
| **React** | - Berlebihan (*overkill*) untuk proyek ini<br>- Pengaturan *build* yang kompleks<br>- Kurva pembelajaran tinggi<br>- Memerlukan API (pemisahan *frontend-backend*) |
| **Vue.js** | - Tidak perlu SPA (*Single Page Application*)<br>- Laravel Blade sudah cukup<br>- Kompleksitas tambahan |
| **jQuery** | - Sudah usang (2024)<br>- Ukuran file besar<br>- Vanilla JS modern lebih baik |

---

#### F. Kontrol Versi: Git & GitHub

**Git untuk Manajemen Kode Sumber:**

**1. Strategi *Branching***

Kami menggunakan ***Git Flow* yang disederhanakan**:

```
main (produksi)
  │
  └─── development (integrasi)
         │
         ├─── feature/booking-flow
         ├─── feature/therapist-dashboard
         ├─── feature/admin-panel
         └─── bugfix/payment-validation
```

**Jenis *Branch*:**
- **main**: Kode siap produksi
- **development**: *Branch* integrasi untuk fitur
- **feature/***: Pengembangan fitur individual
- **bugfix/***: Perbaikan bug
- **hotfix/***: Perbaikan produksi mendesak

**2. Konvensi *Commit***

Mengikuti ***Conventional Commits***:

```
feat: tambah email konfirmasi pemesanan
fix: atasi masalah pemesanan ganda
docs: perbarui dokumentasi API
style: format kode dengan PSR-12
refactor: optimalkan query database
test: tambah unit test untuk BookingController
chore: perbarui dependensi
```

**3. GitHub untuk Kolaborasi**

**Struktur Repositori:**
```
cur-heart-system/
├── .github/
│   └── workflows/          # GitHub Actions (CI/CD)
├── app/
│   ├── Http/Controllers/
│   ├── Models/
│   └── Services/
├── database/
│   ├── migrations/
│   └── seeders/
├── resources/
│   ├── views/
│   ├── css/
│   └── js/
├── routes/
├── tests/
├── .env.example
├── composer.json
└── README.md
```

***Workflow Pull Request*:**
1. Buat *branch feature* dari *development*
2. Kembangkan fitur dengan *commit* yang atomik
3. *Push* ke GitHub
4. Buat *Pull Request* ke *development*
5. *Code review* oleh anggota tim
6. *Merge* setelah persetujuan dan tes lulus

---

**[GAMBAR 4.68 - Perbandingan Monolitik vs *Microservices*]** 🔧
_Diagram perbandingan arsitektur dengan matriks keputusan_

**[GAMBAR 4.69 - Alur Permintaan Laravel MVC]** 🔧
_Siklus hidup permintaan: *Routes* → *Controllers* → *Models* → *Views*_

---

### 4.6.3 Alat Pengembangan

#### A. *Integrated Development Environment* (IDE)

**Visual Studio Code (Utama)**

**Ekstensi yang Digunakan:**
- **Laravel Extension Pack**: *Snippets*, *blade syntax highlighting*
- **PHP Intelephense**: *Autocomplete* dan *intellisense* PHP
- **Tailwind CSS IntelliSense**: *Autocomplete* kelas
- **GitLens**: Integrasi Git
- **Better Comments**: Komentar berkode warna
- **Error Lens**: Tampilan kesalahan *inline*
- **Prettier**: Pemformatan kode
- **ESLint**: *Linting* JavaScript

**Pengaturan VS Code untuk Laravel:**
```json
{
    "php.suggest.basic": false,
    "intelephense.files.associations": ["*.php", "*.blade.php"],
    "emmet.includeLanguages": {
        "blade": "html"
    },
    "tailwindCSS.includeLanguages": {
        "blade": "html"
    }
}
```

---

#### B. Manajemen Dependensi

**1. Composer (Dependensi PHP)**

**composer.json:**
```json
{
    "require": {
        "php": "^8.1",
        "laravel/framework": "^10.0",
        "laravel/breeze": "^1.20",
        "intervention/image": "^2.7",
        "barryvdh/laravel-dompdf": "^2.0"
    },
    "require-dev": {
        "laravel/telescope": "^4.14",
        "nunomaduro/larastan": "^2.0",
        "phpunit/phpunit": "^10.0"
    }
}
```

**Perintah:**
```bash
composer install          # Instal dependensi
composer update           # Perbarui dependensi
composer dump-autoload    # Regenerasi file autoload
```

**2. NPM (Dependensi *Frontend*)**

**package.json:**
```json
{
    "devDependencies": {
        "tailwindcss": "^3.3.0",
        "autoprefixer": "^10.4.14",
        "postcss": "^8.4.23",
        "vite": "^4.0.0",
        "laravel-vite-plugin": "^0.7.5",
        "alpinejs": "^3.12.0"
    }
}
```

**Perintah:**
```bash
npm install           # Instal dependensi
npm run dev           # Build development dengan watch
npm run build         # Build production
```

---

#### C. Alat *Database*

**1. Migrasi Laravel**

Kontrol versi *database*:

```php
// database/migrations/2024_01_01_create_bookings_table.php
public function up()
{
    Schema::create('bookings', function (Blueprint $table) {
        $table->id();
        $table->string('booking_number')->unique();
        $table->foreignId('client_id')->constrained('users');
        $table->foreignId('therapist_id')->constrained('therapists');
        $table->foreignId('service_id')->constrained('services');
        $table->date('booking_date');
        $table->time('time_slot');
        $table->enum('status', ['pending', 'confirmed', 'completed', 'cancelled']);
        $table->timestamps();
    });
}
```

**2. phpMyAdmin / TablePlus**

GUI untuk manajemen *database*:
- Jelajahi tabel
- Jalankan *query*
- Ekspor/impor data
- Pantau kinerja

---

#### D. Alat Pengujian
**1. PHPUnit (*Unit* & *Feature Tests*)**

```php
// tests/Feature/BookingTest.php
public function test_user_can_create_booking()
{
    $user = User::factory()->create();
    $service = Service::factory()->create();
    $therapist = Therapist::factory()->create();
    
    $response = $this->actingAs($user)->post('/bookings', [
        'service_id' => $service->id,
        'therapist_id' => $therapist->id,
        'booking_date' => '2024-12-01',
        'time_slot' => '10:00',
    ]);
    
    $response->assertStatus(201);
    $this->assertDatabaseHas('bookings', [
        'client_id' => $user->id,
        'service_id' => $service->id,
    ]);
}
```

**2. Pengujian *Browser* (Manual)**

Tes pada berbagai *browser*:
- Chrome (utama)
- Firefox
- Safari
- Edge
- *Browser* mobile (Chrome Mobile, Safari iOS)

---

#### E. Alat *Deployment*

**1. Laravel Forge / Laravel Envoyer (Opsional)**

*Deployment* otomatis:
- *Push* ke GitHub → *auto-deploy* ke server
- *Deployment* tanpa *downtime*
- Manajemen sertifikat SSL

**2. *Deployment* Manual (Ramah Anggaran)**

```bash
# Di server via SSH
cd /var/www/cur-heart
git pull origin main
composer install --optimize-autoloader --no-dev
php artisan migrate --force
php artisan config:cache
php artisan route:cache
php artisan view:cache
npm run build
php artisan queue:restart
```

---

**[GAMBAR 4.70 - Server Infrastructure Diagram]** 🔧
_VPS, database, web server, external APIs integration_

**[GAMBAR 4.71 - Midtrans Payment Gateway Integration Flow]** �
_Payment request → Snap API → Payment page → Callback → Verification_

---

### 4.6.4 Infrastructure & Hosting

#### A. Server Requirements

**Minimum Specifications:**
- **OS**: Ubuntu 22.04 LTS
- **Web Server**: Nginx 1.18+ atau Apache 2.4+
- **PHP**: 8.1+ dengan extensions (mbstring, xml, bcmath, curl, gd, mysql)
- **Database**: MySQL 8.0+
- **Memory**: 2GB RAM minimum
- **Penyimpanan**: 20GB SSD
- **SSL**: Let's Encrypt (gratis)

**VPS yang Direkomendasikan:**
- DigitalOcean *Droplet* ($12/bulan)
- Vultr *Cloud Compute* ($10/bulan)
- AWS Lightsail ($10/bulan)
- Niagahoster VPS Indonesia (Rp 100.000/bulan)

---

#### B. Domain & DNS

**Nama Domain:**
- `cur-heart.id` atau `curheart.co.id`
- *Registrar*: Niagahoster, Rumahweb, GoDaddy
- Biaya: Rp 150.000/tahun (domain .id)

**Konfigurasi DNS:**
```
A Record:  @ → [IP Server]
A Record:  www → [IP Server]
CNAME:     api → cur-heart.id
MX Record: @ → mail.cur-heart.id (untuk email)
```

---

#### C. Sertifikat SSL

**Let's Encrypt (Gratis):**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d cur-heart.id -d www.cur-heart.id
```

***Auto-renewal*:**
```bash
sudo certbot renew --dry-run
```

Sertifikat *auto-renew* setiap 60 hari.

---

#### D. Strategi *Backup*

**1. *Backup Database* (Harian)**

**Skrip:**
```bash
#!/bin/bash
# /usr/local/bin/backup-db.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/var/backups/mysql"
DB_NAME="curheart_db"

mysqldump -u root -p${DB_PASSWORD} ${DB_NAME} | gzip > ${BACKUP_DIR}/curheart_${DATE}.sql.gz

# Simpan hanya 30 hari terakhir
find ${BACKUP_DIR} -name "curheart_*.sql.gz" -mtime +30 -delete
```

***Cron Job*:**
```cron
0 2 * * * /usr/local/bin/backup-db.sh
```

**2. *Backup* File (Mingguan)**

```bash
tar -czf /var/backups/files/curheart_$(date +%Y%m%d).tar.gz /var/www/cur-heart
```

**3. *Backup Off-Site***

*Upload* ke penyimpanan *cloud*:
- Google Drive (gratis 15GB)
- AWS S3 (*pay-as-you-go*)
- Backblaze B2 (murah)

---

### 4.6.5 Third-Party Integrations

#### A. *Payment Gateway*: Midtrans

**Pilihan Midtrans:**
- **Lokal**: Berbasis Indonesia, dukungan Bahasa Indonesia
- **Metode Pembayaran**: Kartu kredit, *e-wallet* (GoPay, OVO, Dana), transfer bank, QRIS
- **Harga**: 2% + Rp 1.000 per transaksi
- **Keamanan**: Bersertifikat PCI-DSS
- **Dokumentasi**: Dokumentasi API yang komprehensif

**Integrasi:**
```php
// app/Services/PaymentService.php
use Midtrans\Snap;

public function createTransaction($booking)
{
    $params = [
        'transaction_details' => [
            'order_id' => $booking->booking_number,
            'gross_amount' => $booking->service->price,
        ],
        'customer_details' => [
            'first_name' => $booking->client->name,
            'email' => $booking->client->email,
            'phone' => $booking->client->phone,
        ],
        'item_details' => [[
            'id' => $booking->service->id,
            'price' => $booking->service->price,
            'quantity' => 1,
            'name' => $booking->service->name,
        ]],
    ];
    
    return Snap::createTransaction($params);
}
```

---

#### B. Layanan Email: SMTP / Mailtrap

***Production***: SMTP (Gmail, SendGrid, Mailgun)
***Development***: Mailtrap (*testing*)

**Konfigurasi Laravel Mail:**
```env
MAIL_MAILER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=curheart.system@gmail.com
MAIL_PASSWORD=app_password
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=noreply@cur-heart.id
MAIL_FROM_NAME="CUR-HEART"
```

---

#### C. Konferensi Video (Opsional)

**Solusi *Embedded*:**
- **Zoom**: *Embed* rapat Zoom
- **Google Meet**: Integrasi *iframe*
- **Whereby**: Ruangan *embedded* berbasis API

**Alternatif**: Bangun *in-house* dengan WebRTC (*future enhancement*)

---

**[GAMBAR 4.72 - Video Promosi Storyboard]** �
_Scene breakdown, script, visual elements for promo video_

**[GAMBAR 4.73 - X-Banner Design Layout (60x160 cm)]** 🎨
_Promotional banner design for exhibitions and events_

**[GAMBAR 4.74 - Social Media Campaign Timeline]** �
_Content calendar, posting schedule, engagement metrics_

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

**1. *User Manual* (Panduan Pengguna)**

***Target Audience***: Pengguna akhir (klien, terapis, admin)

**Konten:**
- Panduan registrasi dan *login*
- Cara *booking* layanan (*step-by-step* dengan *screenshot*)
- Cara *reschedule*/*cancel booking*
- Cara menggunakan *dashboard*
- FAQ (*Frequently Asked Questions* / Pertanyaan yang Sering Diajukan)
- *Troubleshooting* masalah umum
- Kontak dukungan (*support*)

**Format:**
- PDF (dapat diunduh dari situs web)
- *Help center online* (halaman web)
- Tutorial video (tertanam di *help center*)

**Bahasa**: Bahasa Indonesia (ramah pengguna, non-teknis)

---

**2. Dokumentasi *Developer* (Pengembang)**

***Target Audience***: *Developer* masa depan, pengelola (*maintainers*)

**Konten:**
- Panduan *setup* proyek
- Tinjauan arsitektur (*architecture overview*)
- Dokumentasi skema *database*
- Dokumentasi API (jika ada)
- Panduan gaya kode (*code style guide*) (PSR-12 untuk PHP)
- Panduan *deployment*
- Alur kerja Git (*workflow*)
- Panduan *testing*

**Format:**
- File Markdown di *repository* GitHub
- Dokumentasi yang dibuat dengan *tools* (PHPDoc, Doxygen)

**Lokasi**: Folder `/docs` dalam *repository*

**Contoh Struktur:**
```
/docs
├── setup.md              # Panduan instalasi
├── architecture.md       # Arsitektur sistem
├── database.md           # Dokumentasi database
├── api.md                # Referensi API
├── deployment.md         # Panduan deployment
├── contributing.md       # Panduan kontribusi
└── changelog.md          # Riwayat versi
```

---

**3. Dokumentasi Admin**

***Target Audience***: Administrator sistem, manajemen CUR-HEART

**Konten:**
- Panduan manajemen server
- Prosedur *backup* dan *restore*
- Praktik terbaik keamanan
- Pemantauan (*monitoring*) dan pencatatan log (*logging*)
- Optimisasi kinerja
- *Troubleshooting* masalah server
- Jadwal pembaruan dan pemeliharaan

---

### 4.7.2 Video Promosi

#### A. Tujuan Video

**Tujuan Utama:**
1. ***Marketing***: Mempromosikan CUR-HEART dan sistem *booking*
2. **Edukasi**: Mengedukasi *target audience* tentang kemudahan sistem
3. ***Engagement***: Meningkatkan kesadaran merek (*brand awareness*) di media sosial

***Target Audience*:**
- Calon klien (individu dengan masalah kesehatan mental)
- HR korporat (untuk program kesejahteraan karyawan / *employee wellness programs*)
- Komunitas layanan kesehatan

---

#### B. Konten Video

**Durasi**: 2-3 menit

**Garis Besar Skrip:**

**Pembukaan (15 detik)**
- *Hook* (Pengait): "Stres, kecemasan, insomnia? Saatnya ambil kendali atas kesehatan mental Anda."
- Logo CUR-HEART dengan *tagline*

**Pernyataan Masalah (20 detik)**
- Statistik: "70% orang Indonesia mengalami stres di era modern"
- Poin masalah (*pain points*): Susah *booking* terapis, tidak tahu pilih terapis mana, proses ribet

**Pengenalan Solusi (30 detik)**
- Perkenalkan layanan hipnoterapi CUR-HEART
- Tampilkan antarmuka (*interface*) situs web (*landing page*)
- Sorot: "*Booking online*, mudah, cepat, 24/7"

**Tampilan Fitur (60 detik)**

*Adegan 1: Jelajah Layanan (10 detik)*
- Rekaman layar (*screen recording*): Gulir halaman Layanan
- *Voiceover*: "6 layanan hipnoterapi untuk berbagai kebutuhan"

*Adegan 2: Pilih Terapis (10 detik)*
- Rekaman layar: Jelajah profil terapis
- *Voiceover*: "Pilih terapis bersertifikat sesuai spesialisasi"

*Adegan 3: Pilih Jadwal (10 detik)*
- Rekaman layar: Pemilihan kalender
- *Voiceover*: "Pilih jadwal yang cocok dengan Anda"

*Adegan 4: Pembayaran (5 detik)*
- Rekaman layar: Opsi pembayaran
- *Voiceover*: "Bayar mudah dengan berbagai metode"

*Adegan 5: Konfirmasi (5 detik)*
- Tampilkan konfirmasi *booking*
- *Voiceover*: "Langsung terima konfirmasi dan pengingat (*reminder*)"

*Adegan 6: Sesi (10 detik)*
- B-roll: Terapis melakukan sesi (*stock footage* atau rekaman aktual)
- *Voiceover*: "Terapi profesional di lingkungan yang nyaman dan rahasia"

*Adegan 7: Pelacakan Kemajuan (10 detik)*
- Rekaman layar: *Dashboard* kemajuan
- *Voiceover*: "Lacak kemajuan dan lihat perkembangan Anda"

**Bukti Sosial (15 detik)**
- Potongan testimoni dari klien (teks atau video)
- Peringkat bintang: "4,8/5,0 dari 100+ klien puas"

***Call-to-Action* (20 detik)**
- "Mulai perjalanan transformasi Anda hari ini"
- Tampilkan URL situs web: www.cur-heart.id
- Tampilkan kontak: WhatsApp, Instagram, Email
- Penawaran khusus: "Diskon 20% untuk *booking* pertama"

**Penutup (10 detik)**
- Logo CUR-HEART
- *Tagline*: "Transformasi Diri Dimulai Dari Sini"
- *Handle* media sosial

---

#### C. Detail Produksi

***Equipment* (Peralatan):**
- Rekaman layar: OBS Studio, Camtasia
- *Editing* video: DaVinci Resolve (gratis), Adobe Premiere Pro
- Grafis: Canva, After Effects
- Musik: Bebas royalti (*royalty-free*) dari Epidemic Sound, Artlist

**Gaya Visual:**
- Estetika yang bersih, modern, dan menenangkan
- Warna merek: Navy #1E0E62, Pink #FF6B7A
- Transisi yang halus
- Teks yang ditumpangkan (*overlays*) untuk poin-poin kunci
- Animasi halus

**Musik:**
- Musik latar yang tenang dan membangkitkan semangat
- Volume rendah (tidak mengalahkan *voiceover*)
- *Fade in*/*out* dengan mulus

***Voiceover*:**
- Talenta suara profesional atau AI voice (ElevenLabs)
- Nada yang hangat, ramah, dan meyakinkan
- Artikulasi yang jelas, kecepatan sedang
- Bahasa Indonesia atau bilingual (ID + *subtitles* EN)

---

#### D. Saluran Distribusi

**1. YouTube**
- *Upload* ke *channel* CUR-HEART
- Optimalkan judul, deskripsi, *tags* untuk SEO
- Tambahkan *end screen* dengan tombol *subscribe* dan tautan situs web
- Buat *playlist*: "Layanan CUR-HEART"

**Judul SEO**: "Booking Terapi Hipnoterapi *Online* Mudah di CUR-HEART | Sistem Terpadu"

**Deskripsi**:
```
Stres? Kecemasan? Trauma? 

CUR-HEART adalah pusat hipnoterapi modern dengan sistem booking online yang mudah dan cepat. Pilih terapis bersertifikat, jadwal fleksibel, bayar mudah - semua dalam satu platform.

🌟 Layanan Kami:
✅ Stress & Anxiety Release
✅ Trauma Healing
✅ Self-Confidence Boost
✅ Sleep Therapy
✅ Habit Reprogramming
✅ Phobia Management

🎯 Keunggulan:
• Terapis bersertifikat & berpengalaman
• Booking online 24/7
• Sesi tatap muka atau online
• Progress tracking
• Lingkungan rahasia & nyaman

📅 Book Sekarang: www.cur-heart.id
📱 WhatsApp: 0812-3456-7890
📧 Email: info@cur-heart.id

#Hypnotherapy #KesehatanMental #TherapiOnline #CURHEART #MentalWellness
```

**2. Instagram**
- IGTV: Video penuh 2-3 menit
- Reels: Versi pendek 30-60 detik (format vertikal)
- Stories: Di balik layar (*behind-the-scenes*), potongan
- *Feed Post*: *Teaser* dengan tautan di bio

**3. TikTok**
- Versi pendek 15-60 detik
- Suara yang sedang tren (*trending sounds*), *hashtags*
- Potongan edukatif (seri)

**4. Facebook**
- Posting di halaman perusahaan (*company page*)
- Bagikan di grup (kesehatan mental, kesejahteraan, komunitas wanita)
- Iklan Facebook (*boosted post*)

**5. LinkedIn**
- Format profesional
- Target pembuat keputusan korporat
- Tekankan manfaat kesejahteraan karyawan

**6. Situs Web**
- *Embed* di *homepage* (bagian *hero* atau bagian tentang)
- Halaman khusus "Cara Kerjanya" (*How It Works*) dengan video
- Posting blog yang menyertai video

---

### 4.7.3 X-*Banner*

#### A. Tujuan

X-*Banner* adalah media promosi fisik untuk:
- Presentasi proyek (*showcase*)
- Acara kampus (pameran *Capstone Project*)
- Promosi di tempat (*on-site*) di kantor CUR-HEART
- Acara jaringan (*networking events*), pameran karir (*career fair*)

---

#### B. Spesifikasi Desain

**Ukuran**: 60 cm × 160 cm (ukuran standar X-*banner*)

**Struktur Tata Letak:**

```
┌──────────────────────────────────┐
│         HEADER (20 cm)           │ ← Logo CUR-HEART, Judul Proyek
├──────────────────────────────────┤
│                                  │
│      MASALAH (15 cm)             │ ← Statistik, pain points
│                                  │
├──────────────────────────────────┤
│                                  │
│      SOLUSI (20 cm)              │ ← Screenshot sistem, fitur utama
│                                  │
├──────────────────────────────────┤
│                                  │
│      MANFAAT (20 cm)             │ ← Icons + deskripsi singkat
│                                  │
├──────────────────────────────────┤
│                                  │
│      TECH STACK (15 cm)          │ ← Logo teknologi
│                                  │
├──────────────────────────────────┤
│                                  │
│      INFO PROYEK (30 cm)         │ ← Tim, timeline, deliverables
│                                  │
├──────────────────────────────────┤
│      FOOTER (40 cm)              │ ← Kontak, QR code, media sosial
└──────────────────────────────────┘
```

---

#### C. Konten

***Header*:**
- Logo CUR-HEART (besar)
- Judul: "SISTEM INFORMASI MANAJEMEN *BOOKING* DAN TERAPI CUR-HEART"
- *Subtitle*: "*Capstone Project* - Proyek Sistem Informasi"

**Bagian Masalah:**
- ***Headline***: "Tantangan dalam Manajemen Layanan Hipnoterapi"
- **Poin-Poin**:
  - ❌ *Booking* manual via telepon/WhatsApp
  - ❌ Rentan terhadap *double booking* dan kesalahan
  - ❌ Sulitnya koordinasi jadwal terapis
  - ❌ *Reporting* manual memakan waktu

**Bagian Solusi:**
- ***Headline***: "Solusi: Platform *Booking Online* Terintegrasi"
- ***Screenshot***: Antarmuka *dashboard* (dengan anotasi)
- **Fitur Utama** (dengan ikon):
  - 📅 *Online Booking* 24/7
  - 👨‍⚕️ Profil Terapis Lengkap
  - 💳 Berbagai Metode Pembayaran
  - 📊 Pelacakan Kemajuan (*Progress Tracking*)
  - 📈 *Reporting* Otomatis

**Bagian Manfaat:**
- **Untuk Bisnis**:
  - 🚀 Efisiensi +50%
  - 💰 Pendapatan +25%
  - ⏱️ Penghematan Waktu 20 jam/bulan
- **Untuk Klien**:
  - ✨ *Booking* Mudah
  - 🔍 Transparansi
  - 📱 *Self-Service*
- **Untuk Terapis**:
  - 🗓️ Penjadwalan Fleksibel
  - 📝 Dokumentasi Digital
  - 💼 *Dashboard* Penghasilan

***Tech Stack*:**
- Logo Laravel, PHP, MySQL, Tailwind CSS (dengan label)
- Ilustrasi Arsitektur Monolitik

**Info Proyek:**
- **Tim**: Roki Anjas, Susanto, Fahruroji
- ***Timeline***: 11 Minggu (September - November 2024)
- ***Deliverables***: Aplikasi Web, Dokumentasi, Video, X-*Banner*
- **Universitas**: Universitas Nusa Mandiri
- ***Program Studi***: Sistem Informasi

***Footer*:**
- **Kontak**: 
  - 🌐 www.cur-heart.id
  - 📧 info@cur-heart.id
  - 📱 0812-3456-7890
- **Kode QR**: Tautan ke situs web (menonjol, tengah)
- **Media Sosial**: @curheart (ikon Instagram, Facebook, TikTok)
- ***Scan***: "Pindai untuk demo langsung"

---

#### D. Panduan Desain

**Skema Warna:**
- Utama: Navy #1E0E62
- Sekunder: Pink #FF6B7A
- Aksen: Teal #4ECDC4, Ungu #8B5FBF
- Latar Belakang: Putih #FFFFFF dengan gradien halus
- Teks: Abu-abu gelap #333333

**Tipografi:**
- Judul (*Heading*): Poppins Bold (besar, menarik perhatian)
- Isi (*Body*): Inter Regular (mudah dibaca, bersih)
- Ukuran: Minimal 16pt untuk keterbacaan dari jarak 2 meter

**Elemen Visual:**
- *Screenshots* berkualitas tinggi (minimum 300 DPI untuk cetak)
- Ikon dari Heroicons atau Feather Icons (gaya yang konsisten)
- Infografis untuk statistik (*bar charts*, *pie charts*)
- Ruang putih (*whitespace*) yang cukup (tidak terlalu padat)

**Spesifikasi Cetak:**
- Resolusi: 300 DPI
- Mode Warna: CMYK (untuk cetak)
- Format File: PDF (vektor) atau PNG (resolusi tinggi)
- *Bleed*: Tambahkan area *bleed* 3mm

---

#### E. Produksi

***Software* Desain:**
- Adobe Illustrator (terbaik untuk vektor)
- Adobe Photoshop (untuk *editing* foto)
- Canva Pro (berbasis *template*, lebih mudah)
- Figma (desain kolaboratif)

**Pencetakan:**
- **Vendor**: Percetakan lokal (Jakarta, Surabaya)
- **Material**: Flexi China 280 gsm atau Flexi Korea 340 gsm
- ***Finishing***: Laminasi *matte* (mengurangi silau)
- ***Stand***: *Stand* X-*banner* (aluminium, dapat disesuaikan)
- **Biaya**: Rp 150.000 - Rp 250.000 per *banner*

**Kuantitas:**
- 2 unit: 1 untuk presentasi, 1 untuk kantor CUR-HEART

---

### 4.7.4 Artikel Publikasi

#### A. Jurnal Ilmiah (Opsional)

**Jurnal Target:**
- Jurnal Sistem Informasi (JSI)
- Jurnal Teknik Informatika dan Sistem Informasi (JuTISI)
- IJCCS (*Indonesian Journal of Computing and Cybernetics Systems*)

**Jenis Artikel**: Studi kasus atau laporan teknis

**Struktur:**
- Abstrak
- Pendahuluan
- Tinjauan Pustaka
- Metodologi
- Hasil dan Pembahasan
- Kesimpulan
- Referensi

***Timeline* Pengiriman:**
- Setelah penyelesaian proyek dan presentasi
- Target publikasi: 6 bulan setelah pengiriman (*submission*)

---

#### B. Posting *Blog* / Artikel Medium

***Platform***: Medium, Dev.to, blog pribadi

**Ide Judul:**
- "*Building* Sistem *Booking* Kesehatan Mental dengan Laravel: Sebuah Studi Kasus"
- "Dari Ide ke Implementasi: Sistem Manajemen Hipnoterapi CUR-HEART"
- "Monolitik vs. *Microservices*: Memilih Arsitektur yang Tepat untuk UKM"

**Konten:**
- Pendalaman teknis (*technical deep-dive*)
- Pelajaran yang dipetik (*lessons learned*)
- Potongan kode (*code snippets*) (yang sudah disanitasi)
- Diagram arsitektur
- Metrik kinerja

***Audience***: Komunitas *developer*, pengusaha, mahasiswa

---

### 4.7.5 Presentasi Final

#### A. *Slide* Presentasi

**Struktur (15-20 *slides*):**

1. ***Title Slide***: Nama proyek, tim, logo
2. **Agenda**: Garis besar presentasi
3. **Latar Belakang**: Latar belakang masalah
4. **Pernyataan Masalah**: Poin masalah (*pain points*) yang spesifik
5. **Tujuan**: Tujuan proyek
6. **Tinjauan Solusi**: Solusi tingkat tinggi (*high-level*)
7. **Arsitektur Sistem**: Diagram arsitektur
8. **Desain *Database***: ERD (disederhanakan)
9. **Fitur Utama**: *Screenshot* dengan anotasi
10. ***Technology Stack***: Teknologi yang digunakan
11. **Proses Pengembangan**: *Timeline*, pencapaian (*milestones*)
12. **Demo**: Demo langsung atau video demo
13. **Hasil *Testing***: *Test cases*, metrik kinerja
14. **Manfaat & ROI**: Manfaat yang terkuantifikasi
15. **Tantangan & Solusi**: Hambatan dan cara mengatasinya
16. **Pelajaran yang Dipetik**: Poin penting yang dipetik (*key takeaways*)
17. **Pengembangan Masa Depan**: Peta jalan (*roadmap*)
18. **Kesimpulan**: Ringkasan
19. **Q&A**: *Slide* pertanyaan
20. **Terima Kasih**: Info kontak

**Desain:**
- Konsisten dengan warna merek
- Teks minimal (gunakan poin-poin)
- Gambar dan *screenshots* berkualitas tinggi
- Grafik dan infografis
- Transisi yang halus

---

#### B. Demo Langsung

**Persiapan:**
- Koneksi internet stabil (*backup*: *hotspot*)
- *Database* yang sudah diisi dengan data contoh
- Uji coba sebelum presentasi (*rehearsal*)
- *Fallback*: Rekaman video jika demo langsung gagal

**Alur Demo (5-7 menit):**
1. *Walkthrough landing page*
2. Registrasi dan *login* pengguna
3. Jelajah layanan dan terapis
4. Alur *booking* lengkap (semua 4 langkah)
5. Tampilkan konfirmasi *booking*
6. Tur singkat: *Dashboard* klien, *dashboard* terapis, panel admin
7. Sorot fitur utama: kalender, pelacakan kemajuan, *reporting*

---

#### C. Penyampaian

**Durasi**: 15 menit presentasi + 5 menit Q&A

**Tips:**
- **Latihan**: Latih berulang kali
- **Kepercayaan Diri**: Berbicara dengan jelas, pertahankan kontak mata
- ***Storytelling***: Bercerita, jangan hanya membaca *slides*
- ***Engagement***: Ajukan pertanyaan retoris, berinteraksi dengan audiens
- **Manajemen Waktu**: Tetap dalam waktu 15 menit
- **Tangani Pertanyaan**: Dengarkan dengan saksama, jawab dengan percaya diri, akui jika tidak tahu

---

### 4.7.6 *Campaign* Media Sosial

#### A. *Teaser* Pra-Peluncuran

***Timeline***: 2 minggu sebelum peluncuran

**Ide Konten:**
- Posting hitung mundur (*countdown*) (7 hari hingga peluncuran)
- Di balik layar (*behind-the-scenes*) (tim bekerja, *coding*, proses desain)
- Intipan fitur (*sneak peeks*) (*screenshot blur* dengan "Segera Hadir")
- Posting masalah-solusi (edukasi audiens)

---

#### B. Pengumuman Peluncuran

**Hari-H**: Peluncuran besar

**Konten:**
- Posting peluncuran dengan video promosi
- *Giveaway*/*contest* untuk pengguna awal (*early adopters*)
- Penawaran khusus (diskon 20% *booking* pertama)
- Siaran pers (*press release*) (jika berlaku)

---

#### C. Konten Pasca-Peluncuran

**Berkelanjutan (bulanan):**
- Kisah sukses (testimoni klien dengan izin)
- Konten edukatif (tips kesehatan mental, mitos vs. fakta hipnoterapi)
- Sorotan fitur (*feature highlights*) (pendalaman per fitur)
- Wawancara tim
- Berita dan wawasan industri

***Hashtags*:**
- Bermerek: #CURHEART #CURHEARTWellness
- Industri: #MentalHealth #Hypnotherapy #Wellness #TherapiOnline
- Lokasi: #TherapyJakarta #WellnessIndonesia

---

### 4.7.7 Metrik Evaluasi

#### A. Metrik Dokumentasi

- ✅ Tingkat penyelesaian *user manual*
- ✅ Cakupan dokumentasi *developer* (baris terdokumentasi / total baris)
- ✅ Skor *feedback* dokumentasi dari pengguna

#### B. Metrik Video

- 👁️ Tayangan (*views*) (target: 10.000 tayangan dalam 3 bulan)
- 👍 Tingkat *engagement* (*likes*, komentar, *shares*)
- 🔗 *Click-through rate* ke situs web
- ⏱️ Waktu tonton rata-rata (target: >70% penyelesaian)

#### C. Metrik X-*Banner*

- 📸 Foto yang diambil dengan *banner* (lacak melalui *hashtag*)
- 💬 Percakapan yang dimulai dari eksposur *banner*
- 🎯 Generasi prospek (*lead generation*) (*QR code scans*)

#### D. Metrik Media Sosial

- 👥 Pertumbuhan pengikut (*followers*) (target: 1.000 pengikut dalam 3 bulan)
- 📊 Tingkat *engagement* (target: >5%)
- 🔗 Lalu lintas situs web dari media sosial
- 💰 Tingkat konversi (pengunjung media sosial → *bookings*)

---

**[Akhir BAB IV - Hasil Penelitian dan Pembahasan]**

**Total BAB IV terdiri dari 5 bagian file:**
1. Bagian 1: 4.1 & 4.2 (Inisiasi & Perencanaan)
2. Bagian 2: 4.3.3 Desain *Database*
3. Bagian 3: 4.3.4 Diagram UML
4. Bagian 4: 4.4 & 4.5 (Faktor Keberhasilan & Keuntungan)
5. Bagian 5: 4.6 & 4.7 (Teknologi & Desiminasi) ← File ini

**Selanjutnya:** BAB V - Penutup (Kesimpulan dan Saran)

