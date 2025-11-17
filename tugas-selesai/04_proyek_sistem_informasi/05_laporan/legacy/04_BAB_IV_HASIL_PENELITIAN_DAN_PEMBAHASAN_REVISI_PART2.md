# BAB IV (Lanjutan)  
# HASIL PENELITIAN DAN PEMBAHASAN - PART 2

## 4.3. DESKRIPSI PRODUK / SERVIS

Berikut ini adalah deskripsi umum (*high-level*) mengenai produk atau layanan yang dihasilkan dari proyek ini:

### 4.3.1 Tujuan Proyek

Tujuan proyek ini adalah membangun sistem informasi berbasis web yang dapat memberikan informasi yang berkaitan dengan manajemen pemesanan dan terapi hipnoterapi CUR-HEART, mencakup:

- Informasi lengkap tentang layanan terapi yang ditawarkan
- Profil terapis dengan spesialisasi dan jadwal ketersediaan
- Sistem pemesanan online yang mudah dan cepat
- Manajemen sesi terapi dan dokumentasi klien
- Pembayaran online yang aman dan terintegrasi
- Dasbor analitik untuk pengambilan keputusan

### 4.3.2 Pengguna Sistem

Sistem ini memiliki 3 tipe pengguna utama dengan hak akses berbeda. Sistem yang dibangun harus mampu:

**A. Untuk Klien:**
- Menampilkan informasi jumlah layanan, terapis, dan testimoni
- Menampilkan informasi layanan terbaru dan terapis unggulan
- Memberikan kemampuan pemesanan layanan secara online 24/7
- Menampilkan riwayat pemesanan dan sesi terapi
- Menyediakan sistem pembayaran yang aman dan mudah
- Menampilkan kemajuan terapi dan catatan sesi (yang dibagikan)

**B. Untuk Terapis:**
- Manajemen jadwal dan ketersediaan secara mandiri
- Melihat daftar klien dan detail pemesanan hari ini
- Mendokumentasikan sesi terapi dengan formulir terstruktur
- Mengakses riwayat lengkap klien untuk kontinuitas perawatan
- Melihat dasbor pendapatan dan statistik kinerja
- Memperbarui profil dan pengaturan notifikasi

**C. Untuk Admin:**
- Pemantauan pemesanan waktu nyata dengan pelacakan status
- Manajemen pengguna (klien, terapis, admin)in)
- Manajemen layanan (operasi CRUD)
- Laporan keuangan dan analitik:
  - Total pemesanan dan pendapatan
  - Rincian per layanan dan terapis
  - Trend pemesanan bulanan
- Approval dan verifikasi terapis baru
- System settings dan configuration

### 4.3.3 Fitur Utama Sistem

**A. Modul Public Website**
- Landing page dengan informasi bisnis
- Katalog layanan terapi lengkap dengan deskripsi
- Direktori terapis dengan profil dan rating
- Blog/artikel tentang kesehatan mental
- FAQ dan halaman bantuan
- Formulir kontak

**B. Modul Autentikasi**
- Autentikasi multi-peran (Klien, Terapis, Admin)
- Registrasi dengan validasi email
- Login dengan fitur ingat saya
- Lupa kata sandi & atur ulang kata sandi
- Social login (Google, Facebook) - opsional

**C. Modul Pemesanan**
- Wizard pemesanan 4 langkah:
  1. Pilih layanan terapi
  2. Pilih terapis (atau penugasan otomatis)
  3. Pilih tanggal & waktu
  4. Konfirmasi & pembayaran
- Pengecekan ketersediaan waktu nyatayata
- Tipe sesi: Daring/*Online*/Luring/*Offline*
- Dukungan kode promo
- Email konfirmasi pemesanan

**D. Modul Pembayaran**
- Integrasi *payment gateway* Midtrans
- Beragam metode pembayaran:
  - Kartu kredit/debit
  - Transfer bank
  - Dompet digital (GoPay, OVO, Dana) Dana)
- Verifikasi pembayaran otomatis
- Pembuatan faktur (PDF)
- Riwayat pembayaran dan pelacakan status

**E. Modul Dasbor Klien**
- Ikhtisar: Sesi mendatang, sesi selesai, total jam
- Janji Temu Saya: Daftar, detail, jadwal ulang, batalkan
- Pelacakan Kemajuan: Grafik visual dan metrik
- Pesan: Obrolan dengan terapis
- Profile & settings

**F. Modul Dasbor Terapis**
- Jadwal hari ini dengan hitungan mundur
- Daftar klien dan detail
- Formulir dokumentasi sesi dengan *rich text editor*
- Riwayat sesi dan arsip catatan
- Pengaturan ketersediaan (jam kerja, waktu libur)
- Dasbor pendapatan
- Manajemen profil

**G. Modul Dasbor Admin**
- Kartu statistik: Pengguna, pemesanan, pendapatan, kesehatan sistem
- Grafik: Tren pendapatan, pertumbuhan pengguna, layanan teratasayanan teratas
- Manajemen pengguna (CRUD, menyetujui terapis)
- Manajemen pemesanan (lihat, edit, batalkan, pengembalian dana)
- Manajemen layanan (CRUD)
- Laporan keuangan (ekspor Excel/PDF)
- Pengaturan sistem

**H. Modul Notifikasi**
- Notifikasi email:
  - Konfirmasi pemesanan
  - Pembayaran berhasil
  - Pengingat sesi (H-1, H-0)
  - Notifikasi pembatalan
- Notifikasi dalam aplikasi
- Pengingat SMS (pengembangan mendatang)

**I. Modul Pelaporan**
- Laporan pemesanan: Harian, mingguan, bulanan
- Laporan pendapatan: Per layanan, per terapis
- Laporan aktivitas pengguna
- Format ekspor: PDF, Excel, CSV

### 4.3.4 Arsitektur Sistem

Sistem dibangun dengan arsitektur **MVC (*Model-View-Controller*)** menggunakan *framework* Laravel:

```
┌──────────────────────────────────────────────┐
│              LAPISAN PRESENTASI              │
│  (Views - Blade Templates + Tailwind CSS)    │
│  - Halaman publik                            │
│  - Dasbor klien                              │
│  - Dasbor terapis                            │
│  - Dasbor admin                              │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│              LAPISAN APLIKASI                │
│         (Controllers + Middleware)           │
│  - AuthController                            │
│  - BookingController                         │
│  - PaymentController                         │
│  - DashboardController                       │
│  - AdminController                           │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│            LAPISAN LOGIKA BISNIS             │
│         (Models + Services + Events)         │
│  - Model User, Therapist, Client             │
│  - Model Service, Booking, Payment           │
│  - Model Session, Review                     │
│  - Aturan bisnis & validasi                  │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│            LAPISAN AKSES DATA                │
│       (Eloquent ORM + MySQL Database)        │
│  - 16 tabel ternormalisasi (3NF)             │
│  - Migrations & seeders                      │
│  - Relationships & constraints               │
└──────────────────────────────────────────────┘
```

### 4.3.5 Desain Basis Data

Sistem menggunakan 16 tabel utama:

1. **users** - Data pengguna universal
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
13. **messages** - Obrolan antara klien-terapis
14. **promo_codes** - Kode promo diskon
15. **audit_logs** - Log aktivitas untuk audit
16. **system_settings** - Konfigurasi sistem

Normalisasi: **Third Normal Form (3NF)** untuk menghindari redundansi dan anomali data.

### 4.3.6 Peran dan Hak Akses Pengguna

**A. Tamu**
- Lihat: Halaman utama, layanan, terapis, blog
- Aksi: Registrasi, login, kontak

**B. Klien**
- Lihat: Semua izin tamu + dasbor, pemesanan, kemajuan, pesan
- Aksi: Pesan layanan, lakukan pembayaran, jadwal ulang/batalkan, beri ulasan, obrolan

**C. Terapis**
- Lihat: Dasbor, jadwal, klien, sesi, pendapatan
- Aksi: Atur ketersediaan, dokumentasi sesi, lihat riwayat klien, obrolan, perbarui profil

**D. Administrator**
- Lihat: Semua data (pengguna, pemesanan, pembayaran, laporan)
- Aksi: CRUD penuh pada semua sumber daya, menyetujui terapis, membuat laporan, pengaturan sistem

### 4.3.7 Keamanan Sistem

**A. Autentikasi & Otorisasi**
- *Hashing* kata sandi dengan *bcrypt*
- Manajemen sesi dengan Laravel
- Perlindungan CSRF untuk semua formulir
- Kontrol akses berbasis peran (*Role-Based Access Control*/RBAC)

**B. Keamanan Data**
- HTTPS untuk semua komunikasi
- Pencegahan *SQL injection* (Eloquent ORM)
- Pencegahan XSS (*Blade escaping*)
- Enkripsi untuk data sensitif (rekam medis)

**C. Keamanan Pembayaran**
- Sesuai PCI-DSS (melalui Midtrans)
- Tidak ada data kartu kredit disimpan secara lokal
- Dukungan 3D Secure

**D. Kepatuhan**
- UU Perlindungan Data Pribadi (UU PDP)
- Arsitektur siap GDPR
- Kebijakan retensi data (cadangan 30 hari)

### 4.3.8 Kinerja dan Skalabilitas

**A. Optimasi Kinerja**
- Pengindeksan basis data pada kueri yang sering digunakan
- *Caching* Laravel (*config*, *route*, *view cache*)
- *Lazy loading* untuk relasi Eloquent
- CDN untuk aset statis (pengembangan mendatang)

**B. Skalabilitas**
- Siap penskalaan horizontal (*load balancer* + beberapa server)
- Replikasi basis data (*master-slave*)
- Pekerja antrian untuk pekerjaan latar belakang
- Sesi tanpa keadaan (siap untuk *clustering*)

**Target Metrik:**
- Waktu muat halaman: < 2 detik
- Pengguna bersamaan: 100+
- Waktu aktif: ≥ 99,5%
- Waktu kueri basis data: < 100ms (rata-rata)

---

### 4.3.9 Pelaksanaan Proyek (Desain Sistem)

Pelaksanaan proyek merupakan fase implementasi dari perencanaan yang telah dibuat. Pada fase ini dilakukan desain sistem yang mencakup perancangan basis data, pemodelan UML, dan desain antarmuka pengguna.

#### 4.3.9.1 Use Case Diagram

Use Case Diagram menggambarkan interaksi antara aktor (pengguna) dengan sistem, serta fungsionalitas yang dapat dilakukan oleh masing-masing aktor.

**[GAMBAR 4.3 - Use Case Diagram Sistem Informasi CUR-HEART]**

**Aktor dalam Sistem:**

1. **Tamu** - Pengunjung situs web yang belum masuk
2. **Klien** - Pengguna terdaftar yang menggunakan layanan terapi
3. **Terapis** - Praktisi hipnoterapi yang memberikan layanan
4. **Admin** - Administrator sistem yang mengelola seluruh sistem
5. ***Payment Gateway*** - Sistem eksternal untuk pemrosesan pembayaran

**Use Cases Utama:**

**Untuk Tamu:**
- Melihat halaman beranda
- Melihat daftar layanan terapi
- Melihat profil terapis
- Registrasi akun baru
- Masuk ke sistem

**Untuk Klien:**
- Melihat jadwal terapis yang tersedia
- Membuat pemesanan layanan terapi
- Memilih terapis dan waktu sesi
- Melakukan pembayaran daring
- Melihat riwayat pemesanan
- Melihat riwayat sesi terapi
- Perbarui profil
- Membatalkan/jadwal ulang pemesanan (dengan syarat)

**Untuk Terapis:**
- Melihat jadwal sesi terapi hari ini dan minggu ini
- Melihat detail pemesanan klien
- Mengatur ketersediaan jadwal
- Mendokumentasikan sesi terapi (catatan sesi)
- Melihat riwayat klien
- Memperbarui status sesi (selesai/dibatalkan)
- Melihat pendapatan

**Untuk Admin:**
- Mengelola data layanan terapi
- Mengelola data terapis
- Mengelola data klien
- Melihat semua pemesanan
- Konfirmasi pembayaran manual (jika ada)
- Membuat laporan (pemesanan, keuangan, kinerja)
- Pemantauan sistem

**Untuk *Payment Gateway*:**
- Memproses pembayaran
- Mengirim notifikasi status pembayaran
- Verifikasi transaksi

#### 4.3.9.2 Activity Diagram

Activity Diagram menggambarkan alur aktivitas dalam sistem untuk berbagai proses bisnis.

**a. Activity Diagram Proses Pemesanan Terapi oleh Klien**

**[GAMBAR 4.4 - Activity Diagram Pemesanan Terapi]**

Alur proses pemesanan terapi:
1. Klien login ke sistem
2. Klien memilih layanan terapi yang diinginkan
3. Sistem menampilkan daftar terapis dan jadwal yang tersedia
4. Klien memilih terapis dan waktu sesi
5. Sistem memeriksa ketersediaan jadwal
   - Jika tidak tersedia: Tampilkan pesan kesalahan, kembali ke pemilihan jadwal
   - Jika tersedia: Lanjut ke langkah berikutnya
6. Klien mengisi informasi tambahan (keluhan, catatan)
7. Sistem menampilkan ringkasan pemesanan dan total biaya
8. Klien konfirmasi pemesanan
9. Sistem membuat catatan pemesanan dengan status "Pending Payment"
10. Sistem alihkan ke *payment gateway* (Midtrans)
11. Klien melakukan pembayaran
12. *Payment gateway* memproses transaksi
    - Jika gagal: Perbarui status menjadi "Payment Failed", kirim notifikasi
    - Jika berhasil: Perbarui status menjadi "Paid", lanjut
13. Sistem mengirim email konfirmasi ke klien
14. Sistem mengirim notifikasi ke terapis terkait
15. Sistem mengirim email pengingat 1 hari sebelum sesi
16. Selesai

**b. Activity Diagram Dokumentasi Sesi Terapi oleh Terapis**

**[GAMBAR 4.5 - Activity Diagram Dokumentasi Sesi Terapi]**

Alur proses dokumentasi sesi terapi:
1. Terapis login ke sistem
2. Terapis melihat daftar sesi hari ini
3. Terapis memilih sesi yang sudah dilaksanakan
4. Sistem menampilkan formulir dokumentasi sesi
5. Terapis mengisi dokumentasi:
   - Teknik yang digunakan
   - Observasi kondisi klien
   - Kemajuan yang dicapai
   - Catatan penting
   - Rekomendasi sesi berikutnya
6. Terapis menyimpan dokumentasi
7. Sistem validasi data
   - Jika tidak valid: Tampilkan pesan kesalahan, kembali ke formulir
   - Jika valid: Simpan ke basis data
8. Sistem perbarui status sesi menjadi "Completed"
9. Sistem mencatat waktu dokumentasi
10. Dokumentasi tersimpan dan dapat diakses untuk sesi berikutnya
11. Selesai

**c. Activity Diagram Generate Laporan oleh Admin**

**[GAMBAR 4.6 - Activity Diagram Generate Laporan]**

Alur proses membuat laporan:
1. Admin masuk ke sistem
2. Admin mengakses menu laporan
3. Admin memilih jenis laporan (pemesanan, keuangan, kinerja terapis, klien)
4. Admin memilih periode (tanggal mulai - tanggal selesai)
5. Admin memilih penyaring tambahan (terapis tertentu, layanan tertentu, dll)
6. Admin klik tombol "Generate Laporan"
7. Sistem mengambil data dari basis data sesuai kriteria
8. Sistem memproses dan menghitung statistik
9. Sistem menampilkan laporan dalam format tabel dan grafik
10. Admin dapat melihat, ekspor (PDF/Excel), atau cetak langsung
11. Selesai

#### 4.3.9.3 Entity Relationship Diagram (ERD)

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
11. **reviews** - Menyimpan ulasan dari klien terhadap terapis/layanan
12. **notifications** - Menyimpan notifikasi untuk pengguna
13. **settings** - Menyimpan konfigurasi sistem
14. **activity_logs** - Menyimpan log aktivitas pengguna (jejak audit)

**Relasi Utama:**

- users (1) ↔ (1) clients: *One-to-One*
- users (1) ↔ (1) therapists: *One-to-One*  
- clients (1) ↔ (M) bookings: *One-to-Many*
- therapists (1) ↔ (M) bookings: *One-to-Many*
- services (1) ↔ (M) bookings: *One-to-Many*
- bookings (1) ↔ (1) payments: *One-to-One*
- bookings (1) ↔ (1) sessions: *One-to-One*
- sessions (1) ↔ (M) session_notes: *One-to-Many*
- therapists (1) ↔ (M) therapist_schedules: *One-to-Many*
- therapists (1) ↔ (M) therapist_unavailability: *One-to-Many*
- sessions (1) ↔ (M) reviews: *One-to-Many*
- users (1) ↔ (M) notifications: *One-to-Many*

**Keterangan:**
- (1) = One
- (M) = Many
- PK = Primary Key
- FK = Foreign Key

Database dinormalisasi hingga Third Normal Form (3NF) untuk menghindari redundansi data dan menjaga integritas data.

#### 4.3.9.4 Desain Antarmuka Pengguna (UI/UX)

Desain antarmuka pengguna (UI) dibuat menggunakan Figma dengan total 41 halaman mockup yang mencakup semua peran pengguna. Desain mengikuti prinsip *user-centered design* dengan fokus pada kemudahan penggunaan, aksesibilitas, dan pengalaman pengguna yang optimal.

##### A. Sistem Desain (*Design System*)

**Palet Warna:**
- **Primary**: Teal (#0D9488) - Menenangkan, profesional, penyembuhan
- **Secondary**: Purple (#9333EA) - Spiritual, transformasi
- **Accent**: Orange (#F59E0B) - Energi, optimisme
- **Neutral**: Skala abu-abu dari #F9FAFB hingga #111827
- **Success**: Green (#10B981)
- **Warning**: Yellow (#F59E0B)
- **Error**: Red (#EF4444)

**Tipografi:**
- **Heading**: Inter (*Sans-serif*) - Modern, bersih, mudah dibaca
- **Body**: Inter (*Sans-serif*)
- **Ukuran Font**: H1 (36px), H2 (30px), H3 (24px), Body (16px), Small (14px)

**Prinsip Desain:**
- Desain bersih dan minimal
- Spasi yang konsisten (skala spasi Tailwind)
- Desain responsif dengan pendekatan *mobile-first*
- Aksesibilitas: Rasio kontras warna minimal 4,5:1
- Hierarki visual yang jelas
- Navigasi yang intuitif

**[GAMBAR 4.8 - Sistem Desain: Color Palette & Typography]**

##### B. Mockup Halaman Utama

Sistem memiliki **41 halaman mockup** yang terbagi dalam beberapa kategori:

**1. Halaman Publik (12 halaman):**

**[GAMBAR 4.9 - Mockup Landing Page]**
- **Landing Page**: Hero section, layanan terapi, featured therapists, testimoni klien, blog posts

**[GAMBAR 4.10 - Mockup Halaman Tentang Kami]**
- **Halaman Tentang Kami**: Kisah kami, visi & misi, nilai inti, profil tim, sertifikasi

**[GAMBAR 4.11 - Mockup Katalog Layanan]**
- **Katalog Layanan**: Filter & pencarian, grid layanan dengan kartu detail

**[GAMBAR 4.12 - Mockup Detail Layanan]**
- **Detail Layanan**: Hero, navigasi tab (ikhtisar/manfaat/proses/FAQ), terapis yang direkomendasikan, ulasan

**[GAMBAR 4.13 - Mockup Direktori Terapis]**
- **Direktori Terapis**: Pencarian, filter spesialisasi/rating/pengalaman, grid terapis

**[GAMBAR 4.14 - Mockup Profil Terapis]**
- **Profil Terapis**: Bio lengkap, pendidikan & sertifikasi, layanan & harga, kalender ketersediaan, ulasan klien

**[GAMBAR 4.15 - Mockup Daftar Blog]**
- **Daftar Blog**: Artikel unggulan, pencarian, filter kategori, grid artikel blog, bilah samping

**[GAMBAR 4.16 - Mockup Detail Blog]**
- **Detail Blog**: Konten artikel, metadata, berbagi media sosial, artikel terkait, bagian komentar

**[GAMBAR 4.17 - Mockup Hubungi Kami]**
- **Hubungi Kami**: Formulir, info kontak, Google Maps, tautan media sosial

**[GAMBAR 4.18 - Mockup FAQ]**
- **FAQ**: Pencarian, tab kategori, daftar akordion dengan umpan balik

**[GAMBAR 4.19 - Mockup Kebijakan Privasi]**
- **Kebijakan Privasi**: Daftar isi, bagian terstruktur, sorotan penting

**[GAMBAR 4.20 - Mockup Syarat & Ketentuan]**
- **Syarat & Ketentuan**: Daftar isi, klausul bernomor untuk referensi legal

**2. Halaman Autentikasi (4 halaman):**

**[GAMBAR 4.21 - Mockup Login]**
- **Login**: Layar terpisah dengan ilustrasi, email & kata sandi, ingat saya, login sosial media

**[GAMBAR 4.22 - Mockup Registrasi]**
- **Registrasi**: Pilihan tipe pengguna (Klien/Terapis), formulir berbeda per peran, kotak centang syarat

**[GAMBAR 4.23 - Mockup Lupa Kata Sandi]**
- **Lupa Kata Sandi**: Formulir sederhana, kirim tautan reset, status berhasil

**[GAMBAR 4.24 - Mockup Reset Kata Sandi]**
- **Reset Kata Sandi**: Kata sandi baru, konfirmasi kata sandi, pengukur kekuatan kata sandi

**3. Dashboard Klien (10 halaman):**

**[GAMBAR 4.25 - Mockup Dasbor Klien - Dasbor Utama]**
- **Dasbor Utama**: Sambutan, statistik cepat, janji temu berikutnya, sesi mendatang, ikhtisar kemajuan

**[GAMBAR 4.26 - Mockup Pemesanan Langkah 1 - Pilih Layanan]**
- **Pemesanan Langkah 1**: Pemilihan layanan dengan kartu layanan

**[GAMBAR 4.27 - Mockup Pemesanan Langkah 2 - Pilih Terapis]**
- **Pemesanan Langkah 2**: Pilih terapis dengan profil dan rating

**[GAMBAR 4.28 - Mockup Pemesanan Langkah 3 - Pilih Jadwal]**
- **Pemesanan Langkah 3**: Pemilih tanggal & waktu dengan ketersediaan waktu nyata

**[GAMBAR 4.29 - Mockup Pemesanan Langkah 4 - Konfirmasi & Pembayaran]**
- **Pemesanan Langkah 4**: Konfirmasi & pembayaran dengan ringkasan pemesanan

**[GAMBAR 4.30 - Mockup Pemesanan Berhasil]**
- **Pemesanan Berhasil**: Selamat, detail pemesanan, langkah selanjutnya, tombol aksi

**[GAMBAR 4.31 - Mockup Janji Temu Saya]**
- **Janji Temu Saya**: Tab (mendatang/lampau/dibatalkan), filter & urutkan, kartu janji temu

**[GAMBAR 4.32 - Mockup Detail Janji Temu]**
- **Detail Janji Temu**: Info pemesanan, info pembayaran, catatan sesi, aksi jadwal ulang/batalkan

**[GAMBAR 4.33 - Mockup Dasbor Kemajuan]**
- **Dasbor Kemajuan**: Skor kesehatan, kehadiran sesi, tujuan & pencapaian, pelacakan suasana hati

**[GAMBAR 4.34 - Mockup Pesan (Obrolan)]**
- **Pesan (Obrolan)**: Daftar percakapan, area obrolan aktif, indikator mengetik

**4. Dashboard Terapis (10 halaman):**

**[GAMBAR 4.35 - Mockup Dasbor Terapis - Dasbor Utama]**
- **Dasbor Utama**: Sesi hari ini, metrik kunci, ikhtisar pendapatan, ulasan klien

**[GAMBAR 4.36 - Mockup Manajemen Jadwal]**
- **Manajemen Jadwal**: Tampilan kalender (hari/minggu/bulan), blok janji temu, waktu libur

**[GAMBAR 4.37 - Mockup Pengaturan Ketersediaan]**
- **Pengaturan Ketersediaan**: Jam kerja per hari, durasi sesi, jendela pemesanan, tanggal khusus

**[GAMBAR 4.38 - Mockup Daftar Klien]**
- **Daftar Klien**: Cari & filter, kartu klien dengan statistik, aksi massal

**[GAMBAR 4.39 - Mockup Tampilan Profil Klien]**
- **Tampilan Profil Klien**: Ikhtisar, riwayat sesi, catatan & observasi, kemajuan & tujuan, berkas

**[GAMBAR 4.40 - Mockup Ruang Sesi]**
- **Ruang Sesi**: Konferensi video dengan timer, bilah kontrol, panel catatan

**[GAMBAR 4.41 - Mockup Formulir Catatan Sesi]**
- **Formulir Catatan Sesi**: Penilaian, ringkasan sesi, catatan kemajuan, tugas rumah, templat

**[GAMBAR 4.42 - Mockup Riwayat Sesi]**
- **Riwayat Sesi**: Total sesi, cari & filter, tabel sesi, analitik

**[GAMBAR 4.43 - Mockup Dasbor Pendapatan]**
- **Dasbor Pendapatan**: Saldo, grafik pendapatan, transaksi, penarikan, pengaturan pembayaran

**[GAMBAR 4.44 - Mockup Edit Profil]**
- **Edit Profil**: Tab untuk dasar/profesional/tentang/pendidikan/layanan/media/pengaturan

**5. Dashboard Admin (5 halaman):**

**[GAMBAR 4.45 - Mockup Dasbor Admin - Dasbor Utama]**
- **Dasbor Utama**: Metrik kunci, grafik pendapatan, pemesanan terbaru, pertumbuhan pengguna, peringatan sistem

**[GAMBAR 4.46 - Mockup Manajemen Pengguna]**
- **Manajemen Pengguna**: Tab (semua/klien/terapis/admin/tertunda), tabel pengguna, aksi massal

**[GAMBAR 4.47 - Mockup Manajemen Pemesanan]**
- **Manajemen Pemesanan**: Ringkasan statistik, tab (semua/mendatang/lampau/tertunda/dibatalkan/sengketa), tabel pemesanan

**[GAMBAR 4.48 - Mockup Laporan Keuangan]**
- **Laporan Keuangan**: Ringkasan pendapatan, grafik, tabel transaksi, penarikan, pengembalian dana, analitik

**[GAMBAR 4.49 - Mockup Pengaturan Sistem]**
- **Pengaturan Sistem**: Navigasi kategori, umum/pemesanan/pembayaran/email/keamanan/kebijakan/integrasi/lanjutan

##### C. Fitur Desain Unggulan

**Desain Responsif:**
- Pendekatan *mobile-first* dengan *breakpoints* optimal
- Adaptif untuk desktop (1920px), tablet (768px), dan mobile (375px)
- *Touch-friendly* untuk perangkat mobile (min 44x44px *tap targets*)

**Aksesibilitas:**
- Memenuhi standar *WCAG 2.1 Level AA*
- Rasio kontras warna minimal 4.5:1 untuk teks normal
- Dukungan navigasi keyboard
- Ramah *screen reader* dengan label *ARIA* yang tepat
- Indikator fokus yang jelas

**Pengalaman Pengguna:**
- Pola navigasi konsisten di semua halaman
- Tombol *call-to-action* yang jelas dengan hierarki
- Status pemuatan dan *skeleton screens*
- Status kesalahan dengan pesan membantu
- Status berhasil dengan aksi selanjutnya yang jelas
- Status kosong dengan panduan

**Desain Visual:**
- Spasi konsisten menggunakan skala spasi Tailwind (unit dasar 4px)
- Hierarki tipografi yang jelas
- Ikonografi menggunakan Heroicons (SVG)
- Gambar dengan foto dan ilustrasi berkualitas tinggi
- Interaksi mikro untuk pengalaman menyenangkan (*hover states*, transisi, animasi)

**Desain Formulir:**
- Label dan *placeholder* yang jelas
- Validasi sebaris dengan pesan kesalahan yang membantu
- Indikator kemajuan untuk formulir multi-langkah
- Simpan otomatis draf untuk formulir panjang
- Indikator bidang wajib (*)

**Visualisasi Data:**
- Grafik menggunakan *Chart.js*/*ApexCharts*
- Palet ramah buta warna
- *Tooltips* interaktif
- Responsif untuk berbagai ukuran layar
- Kemampuan ekspor (PNG, SVG, PDF)

##### D. Prototype Interaktif

**[LINK - Figma Prototype: https://figma.com/proto/curheart...]**

Prototipe interaktif telah dibuat di Figma dengan fitur:
- Navigasi *click-through* antar halaman
- *Hover states* dan interaksi mikro
- Simulasi validasi formulir
- Pratinjau responsif untuk berbagai perangkat
- Anotasi untuk *developer handoff*
- Spesifikasi desain (spasi, warna, tipografi)
- Pustaka komponen untuk dapat digunakan kembali

##### E. Design Handoff

Dokumentasi lengkap untuk pengembang mencakup:
- **Pustaka Komponen**: 50+ komponen yang dapat digunakan kembali (tombol, kartu, formulir, modal, tabel)
- **Token Desain**: Warna, tipografi, spasi, bayangan, *border-radius*
- **Ekspor Aset**: Ikon (SVG), gambar (WebP/PNG), ilustrasi (SVG)
- **Spesifikasi**: Detail spasi, ukuran, dan posisi
- **Catatan Pengembang**: Panduan implementasi, dependensi, kasus tepi
- **Daftar Periksa Aksesibilitas**: Persyaratan aksesibilitas per komponen

---

**Ringkasan Desain UI/UX:**

Total **41 halaman mockup** yang mencakup seluruh perjalanan pengguna dari 4 peran berbeda (Tamu, Klien, Terapis, Admin). Semua mockup dirancang dengan prinsip:

✅ **Responsif**: Adaptif untuk desktop, tablet, dan mobile  
✅ **Aksesibilitas**: Memenuhi standar *WCAG 2.1 AA*  
✅ **Konsistensi**: Mengikuti sistem desain yang telah ditetapkan  
✅ **Ramah Pengguna**: Intuitif dan mudah digunakan  
✅ **Profesional**: Mencerminkan kredibilitas layanan kesehatan mental

Desain telah melalui beberapa iterasi berdasarkan umpan balik dari pemangku kepentingan dan *usability testing* dengan sampel pengguna.

---