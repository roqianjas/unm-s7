# BAB I  
# PENDAHULUAN

## 1.1 Latar Belakang Masalah

Kesehatan mental telah menjadi isu kesehatan global yang mendesak di abad ke-21. Berdasarkan data Riset Kesehatan Dasar (Riskesdas) Kementerian Kesehatan RI tahun 2023, prevalensi gangguan kesehatan mental di Indonesia mencapai 20% dari total populasi atau sekitar 1 dari 5 orang. Fenomena ini dipicu oleh tekanan pekerjaan, ketidakstabilan ekonomi pascapandemi, gangguan digital, serta stigma sosial yang masih tinggi terhadap gangguan kesehatan mental.

Indonesia memiliki rasio psikiater dan psikolog yang sangat rendah (1:200.000), jauh di bawah standar WHO (1:100.000). Layanan kesehatan mental konvensional seringkali memiliki waktu tunggu lama, biaya tinggi, lokasi tidak mudah diakses, serta proses administrasi rumit. Di tengah keterbatasan ini, hipnoterapi (*hypnotherapy*) sebagai metode terapi alternatif mulai mendapat perhatian sebagai solusi efektif dan efisien.

Penelitian ilmiah membuktikan hipnoterapi memiliki tingkat keberhasilan 75-85% dalam mengatasi gangguan kecemasan, lebih tinggi dibandingkan terapi kognitif-perilaku konvensional (60-70%), dengan durasi terapi lebih singkat (6-8 sesi vs 12-20 sesi). CUR-HEART (*Hypnotherapy & Mind Wellness Center*) hadir sebagai pusat layanan terapi kesehatan mental yang mengintegrasikan pendekatan hipnoterapi modern dengan nilai spiritualitas dan humanisme.

Namun, CUR-HEART menghadapi tantangan manajerial: (1) proses pemesanan manual via telepon/WhatsApp menyebabkan kesalahpahaman dan pemesanan ganda; (2) manajemen jadwal terapis menggunakan spreadsheet tidak efisien dan rawan kesalahan; (3) dokumentasi catatan terapi menggunakan kertas/Word terpisah menyulitkan pencarian riwayat; (4) tidak ada sistem pelacakan kemajuan klien yang terstruktur; (5) klien tidak memiliki platform layanan mandiri (*self-service*); (6) kesulitan dalam analisis data operasional dan pengambilan keputusan strategis; (7) sistem pembayaran manual rawan kesalahan dan kehilangan transaksi; (8) risiko keamanan dan privasi data tinggi.

Pengembangan sistem informasi manajemen pemesanan dan terapi berbasis web menggunakan Laravel Framework menjadi solusi untuk mengotomatisasi proses bisnis, meningkatkan akurasi data, memfasilitasi komunikasi, serta menyediakan dasbor pemantauan untuk pengambilan keputusan berbasis data. Sistem ini dirancang dengan 41 halaman antarmuka mencakup halaman publik, autentikasi, dan dasbor untuk klien, terapis, dan admin, menggunakan pendekatan SDLC Waterfall dengan desain responsif mobile-first.

## 1.2 Identifikasi Masalah

Berdasarkan analisis kondisi eksisting melalui observasi, wawancara dengan pemangku kepentingan, dan studi dokumentasi proses bisnis, teridentifikasi permasalahan utama:

1. **Proses Pemesanan Tidak Efisien**: Komunikasi manual via WhatsApp menyebabkan tingkat konversi hanya 60%, tidak ada transparansi informasi terapis dan layanan, klien tidak dapat membandingkan sebelum memutuskan.

2. **Ketiadaan Sistem Manajemen Jadwal Terpadu**: Penjadwalan manual menyebabkan konflik jadwal, tidak ada sistem pemblokiran tanggal untuk cuti, ketimpangan beban kerja antar terapis.

3. **Dokumentasi Tidak Terstruktur**: Catatan terapi terpisah-pisah, sulit diakses, tidak ada templat standar, risiko kehilangan data tinggi, tidak ada sistem pencadangan.

4. **Tidak Ada Pelacakan Kemajuan Klien**: Klien tidak dapat melihat perkembangan terapi, tidak ada data terukur untuk evaluasi keberhasilan, sulit identifikasi klien yang perlu perhatian khusus.

5. **Keterbatasan Akses Informasi Klien**: Tidak ada platform self-service, klien bergantung penuh pada admin, tidak dapat melakukan penjadwalan ulang mandiri.

6. **Kesulitan Pengambilan Keputusan**: Tidak ada laporan otomatis, analisis manual memakan waktu, tidak ada business intelligence untuk optimasi operasional.

7. **Sistem Pembayaran Tidak Terpadu**: Verifikasi manual, rekonsiliasi sulit, tidak ada variasi metode pembayaran digital, pelacakan status pembayaran sulit.

8. **Risiko Keamanan Data Tinggi**: Tidak ada enkripsi, akses tidak terkontrol, tidak ada jejak audit, tidak patuh regulasi perlindungan data pribadi (UU No. 27 Tahun 2022).

Dampak kumulatif: penurunan efisiensi operasional, potensi kehilangan pendapatan, risiko reputasi, terhambatnya skalabilitas bisnis, hilangnya peluang optimasi.

## 1.3 Ruang Lingkup

### 1.3.1 Ruang Lingkup Sistem

Sistem informasi CUR-HEART mencakup:

**Modul Utama:**
1. **Manajemen Pengguna**: Registrasi, autentikasi multi-peran (Admin, Terapis, Klien), profil pengguna, kontrol akses berbasis peran (RBAC).

2. **Manajemen Layanan**: CRUD layanan terapi, kategori layanan, harga dan durasi, deskripsi detail, gambar layanan.

3. **Manajemen Pemesanan**: Alur pemesanan 4 langkah (pilih layanan → pilih terapis → pilih jadwal → pembayaran), kalender ketersediaan real-time, konfirmasi otomatis, notifikasi email/SMS.

4. **Manajemen Jadwal Terapis**: Pengaturan ketersediaan (hari, jam operasional, jadwal berulang), pemblokiran tanggal cuti, visualisasi kalender, pencegahan konflik jadwal.

5. **Manajemen Sesi Terapi**: Dokumentasi catatan terapi terstruktur, templat berdasarkan jenis layanan, riwayat sesi per klien, pelacakan kemajuan dengan metrik (skala kecemasan, frekuensi sesi).

6. **Sistem Pembayaran**: Integrasi payment gateway (Midtrans), multiple payment methods (Virtual Account, E-wallet, QRIS, Kartu Kredit), verifikasi otomatis, invoice digital.

7. **Dasbor Analitik**: Dasbor Admin (metrik bisnis komprehensif), Dasbor Terapis (jadwal, klien, pendapatan), Dasbor Klien (riwayat pemesanan, progress tracking).

8. **Manajemen Konten**: Halaman informatif (About, Services, Blog), FAQ, Privacy Policy, Terms & Conditions.

### 1.3.2 Ruang Lingkup Teknologi

**Backend:**
- Framework: Laravel 10.x (PHP 8.2)
- Database: MySQL 8.0
- Authentication: Laravel Sanctum
- Payment Gateway: Midtrans API

**Frontend:**
- Blade Templating Engine
- Tailwind CSS 3.x
- Alpine.js (interaktivitas ringan)
- Responsive Design (Mobile-first)

**Infrastructure:**
- Web Server: Nginx/Apache
- Hosting: VPS (Niagahoster/AWS)
- Version Control: Git/GitHub
- Deployment: Manual/CI-CD

### 1.3.3 Ruang Lingkup Pengguna

**Tiga Peran Pengguna:**

1. **Admin**: Manajemen seluruh sistem, users, bookings, services, laporan keuangan, pengaturan sistem.

2. **Terapis**: Manajemen jadwal pribadi, lihat klien assigned, buat catatan sesi, lihat pendapatan, kelola profil.

3. **Klien**: Booking layanan, lihat riwayat pemesanan, tracking progress, komunikasi dengan terapis, kelola profil.

### 1.3.4 Batasan Sistem

1. **Tidak mencakup video conferencing** untuk sesi online (menggunakan tools eksternal seperti Zoom/Google Meet).
2. **Tidak ada aplikasi mobile native** (responsive web only).
3. **Tidak ada integrasi dengan Electronic Health Record (EHR)** eksternal.
4. **Tidak ada sistem inventory** untuk produk fisik atau merchandise.
5. **Tidak ada multi-language support** (Bahasa Indonesia only).
6. **Tidak ada sistem loyalty/membership** dengan poin reward.
7. **Tidak mencakup AI/ML** untuk rekomendasi terapis atau prediksi.
8. **Tidak ada forum/komunitas** untuk klien.

## 1.4 Tujuan dan Manfaat Penelitian

### 1.4.1 Tujuan Penelitian

**Tujuan Umum:**
Mengembangkan sistem informasi manajemen pemesanan dan terapi berbasis web untuk meningkatkan efisiensi operasional dan kualitas layanan CUR-HEART.

**Tujuan Khusus:**
1. Menganalisis proses bisnis eksisting dan kebutuhan sistem CUR-HEART.
2. Merancang arsitektur sistem, database, dan antarmuka pengguna yang user-friendly.
3. Mengimplementasikan sistem menggunakan Laravel Framework dengan fitur komprehensif.
4. Melakukan pengujian fungsional, usability, dan performance untuk memastikan kualitas.
5. Menghasilkan dokumentasi lengkap untuk pemeliharaan dan pengembangan.

### 1.4.2 Manfaat Penelitian

**Bagi CUR-HEART:**
- Efisiensi operasional meningkat 40%
- Pengurangan kesalahan administrasi 60%
- Peningkatan konversi pemesanan dari 60% ke 85%
- Data terpusat untuk business intelligence
- Skalabilitas untuk pertumbuhan bisnis

**Bagi Terapis:**
- Manajemen jadwal otomatis
- Akses mudah ke riwayat klien
- Tracking kinerja dan pendapatan
- Dokumentasi terstruktur
- Fokus pada layanan terapi, bukan administrasi

**Bagi Klien:**
- Kemudahan booking 24/7
- Transparansi informasi layanan dan terapis
- Self-service portal
- Tracking progress terapi
- Pengalaman pengguna lebih baik

**Bagi Akademik:**
- Model referensi pengembangan sistem informasi kesehatan mental
- Kontribusi literatur tentang implementasi Laravel di sektor healthcare
- Studi kasus SDLC Waterfall dalam proyek nyata
- Dokumentasi best practices untuk mahasiswa

**Bagi Masyarakat:**
- Peningkatan akses layanan kesehatan mental
- Mengurangi stigma melalui kemudahan akses digital
- Model sistem yang dapat diadopsi pusat terapi lain
- Kontribusi pada digitalisasi layanan kesehatan Indonesia
