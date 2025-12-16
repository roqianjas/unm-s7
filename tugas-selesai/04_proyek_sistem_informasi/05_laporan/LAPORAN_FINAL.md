## CUR-HEART: INOVASI SISTEM INFORMASI LAYANAN

## TERAPI MENTAL BERBASIS DIGITAL

## MAKALAH

Diajukan untuk memenuhi salah satu tugas kelompok mata kuliah Proyek Sistem
Informasi

```
Nama Anggota Kelompok :
```
1. Roki Anjas 11250066
2. Fahruroji 11250085
3. Susanto 11250068

```
Kelas: 11.7C.
```
## PROGRAM STUDI INFORMATIKA

## UNIVERSITAS NUSA MANDIRI

## JAKARTA

## 2025


```
ii
```
## KATA PENGANTAR

Puji syukur kami panjatkan kepada Tuhan Yang Maha Esa atas segala rahmat
dan karunia-Nya sehingga kami dapat menyelesaikan laporan _Capstone Project_
dengan judul "CUR-HEART: Inovasi Sistem Informasi Layanan Terapi Mental
Berbasis Digital" sebagai salah satu syarat untuk menyelesaikan Program Studi
Strata Satu (S1) Sistem Informasi di Fakultas Teknologi Informasi Universitas
Nusa Mandiri.
Proyek ini bertujuan untuk mengembangkan sistem informasi berbasis web
yang dapat meningkatkan efisiensi dan efektivitas operasional layanan hipnoterapi
di CUR-HEART ( _Hypnotherapy & Mind Wellness Center)._ Dengan memanfaatkan
teknologi informasi, kami berupaya memberikan solusi komprehensif untuk
permasalahan manajemen reservasi, penjadwalan, dokumentasi terapi, dan
pembayaran yang selama ini dilakukan secara manual.
Kami menyadari bahwa laporan ini masih jauh dari sempurna. Oleh karena
itu penyusun mengucapkan terima kasih kepada : Ibu Ika Kurniawati, M.Kom,
selaku dosen pengampu mata kuliah Proyek Sistem Informasi yang telah
memberikan bimbingan dan arahan selama proses pembelajaran.
Kami sangat mengharapkan kritik dan saran yang membangun dari berbagai
pihak untuk perbaikan di masa mendatang. Kami berharap penelitian ini dapat
memberikan manfaat, khususnya bagi CUR-HEART dalam mengoptimalkan
layanan terapi kesehatan mental, serta bagi akademisi dan praktisi yang tertarik
dalam bidang sistem informasi layanan kesehatan.
Akhir kata, kami mengucapkan terima kasih kepada semua pihak yang telah
membantu dalam penyelesaian proyek ini. Semoga laporan ini dapat memberikan
kontribusi positif bagi perkembangan sistem informasi kesehatan mental di
Indonesia.

```
Jakarta, 16 Desember 2025
```
```
Penyusun
```

```
iii
```
## ABSTRAK

**Roki Anjas ( 11250066 ), Fahruroji ( 11250085 ), Susanto ( 11250068 ) “CUR-
HEART: Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital”.**

CUR-HEART ( _Hypnotherapy & Mind Wellness Center_ ) menghadapi tantangan
operasional akibat sistem manual yang tidak efisien, meliputi proses reservasi
dengan tingkat konversi hanya 60%, konflik jadwal 8-10 kasus per bulan,
dokumentasi tidak terstruktur, dan risiko keamanan data. Penelitian ini bertujuan
mengembangkan sistem informasi berbasis web menggunakan framework Laravel
dengan pendekatan _System Development Life Cycle_ (SDLC) model _Waterfall_.
Metodologi meliputi inisiasi, perencanaan, pelaksanaan (analisis kebutuhan,
perancangan, implementasi, pengujian, deployment), pemantauan, dan penutupan
proyek. Analisis kebutuhan mengidentifikasi 40+ kebutuhan fungsional melalui
wawancara dengan 14 responden. Perancangan menggunakan ERD dengan 16
entitas dinormalisasi hingga 3NF, diagram UML, dan 66 halaman maket _UI/UX_.
Implementasi menghasilkan aplikasi web dengan 8 modul utama: autentikasi,
informasi publik, reservasi otomatis, dasbor klien, dasbor terapis, dasbor admin,
integrasi pembayaran Midtrans, dan notifikasi email. Teknologi yang digunakan:
_Laravel 10, MySQL 8.0, Tailwind CSS, dan VPS Ubuntu_. Pengujian mencapai
100% pass rate untuk 12 skenario kritis UAT dengan skor SUS 80,5/100 (kategori
_Excellent_ /A).
Dampak bisnis terukur meliputi peningkatan efisiensi operasional 60%,
peningkatan kapasitas reservasi 25%, peningkatan pendapatan 31% (Rp26,45 juta
menjadi Rp34,72 juta/bulan), eliminasi 100% reservasi ganda, peningkatan retensi
klien dari 65% menjadi 85%, dan ROI 1.743% dalam proyeksi 5 tahun dengan
periode payback 20 hari. Sistem ini membuktikan bahwa transformasi digital
layanan terapi mental dapat diimplementasikan dengan metodologi tepat, teknologi
sesuai, dan pendekatan _user-centered_ , menghasilkan nilai bisnis signifikan.

**Kata kunci:** **_Sistem Informasi, Layanan Terapi Mental, Hipnoterapi, Laravel,
Transformasi Digital, Manajemen Reservasi, SDLC Waterfall, ROI_**


```
iv
```
## DAFTAR ISI

Halaman
Lembar Judul Makalah .......................................................................................... i
Kata Pengantar .................................................................................................... ii
Abstrak ................................................................................................................. iii
Daftar Isi ................................................................................................................ iv
Daftar Gambar ...................................................................................................... vi
Daftar Tabel .......................................................................................................... ix
Daftar Lampiran ................................................................................................... x
Daftar Simbol ....................................................................................................... xi

**BAB 1 PENDAHULUAN ................................................................................... 1**
1.1. Latar Belakang ................................................................................ 1
1.2. Identifikasi Masalah ....................................................................... 2
1.3. Ruang Lingkup ................................................................................ 3
1.4. Tujuan dan Manfaat Penelitian ........................................................ 5
1.4.1. Tujuan Penelitian ................................................................... 5
1.4.2. Manfaat Penelitian ................................................................ 5

**BAB II TINJAUAN PUSTAKA ....................................................................... 7**
2.1. Landasan Teori ................................................................................ 7
2.1.1. Sistem Informasi ................................................................... 9
2.1.2. Inovasi Layanan Terapi Berbasis Digital ........................... 10
2.1.3. Siklus Hidup Pengembangan Sistem SDLC ...................... 11
2.1.4. Hipnoterapi dan Kesehatan Mental .................................... 15
2.1.5. Kerangka Kerja Laravel ..................................................... 17
2.1.6. Database Management System .......................................... 19
2 .1.7. Tailwind CSS ..................................................................... 20
2.1.8. Keamanan Web .................................................................. 20
2.2. Penelitian Terkait .......................................................................... 21

**BAB III METODOLOGI PENELITIAN** ..................................................... 24
3.1. Tahapan Penelitian ..................................................................... 24
3.2. Tempat dan Waktu Penelitian .................................................... 26
3.2.1. Tempat Penelitian ............................................................ 26
3.2.2. Waktu Penelitian ............................................................. 26
3.3. Subjek Penelitian ........................................................................ 27
3.3.1. Populasi ............................................................................ 27
3.3.2. Sampel dan Teknik Pengambilan Sampel ....................... 27
3.4_._ Teknik Pengumpulan Data .......................................................... 29
3.4.1. Observasi .......................................................................... 29
3.4.2. Wawancara ...................................................................... 29
3.4.3. Studi Pustaka ................................................................... 30
3.4.4. Kuisoner .......................................................................... 31


## v


```
vi
```
## DAFTAR GAMBAR




ix

## DAFTAR TABEL

- BAB IV HASIL PENELITIAN DAN PEMBAHASAN
   - 4.1. Inisiasi Proyek
      - 4.1.1. Latar Belakang Masalah
      - 4.1.2. Identifikasi Masalah
      - 4 .1.3. Ruang Lingkup
      - 4.1.4. Tujuan dan Manfaat Penelitian
   - 4.2. Perencanaan Proyek
      - 4.2.1. Perencanaan Ruang Lingkup
      - 4.2.2. Perencanaan Waktu Pengerjaan
      - 4.2.3. Perencanaan Anggaran Biaya
      - 4.2.4. Perencanaan Kualitas
      - 4.2.5. Perencanaan Sumber Daya
      - 4.2.6. Manajemen Risiko
      - 4.2.7. Perencanaan Komunikasi
      - 4.2.8. Perencanaan Pengadaan
      - 4.2.9. Perencaan Integrasi
      - 4.2.10. Manajemen Pemangku Kepentingan
      - 4.2.11. Batasan Proyek
      - 4.2.12. Asumsi Proyek
   - 4.3. Deskripsi Produk / Servis
      - 4.3.1. Tujuan Proyek
      - 4.3.2. Pengguna Sistem
      - 4.3.3. Fitur Utama Sistem
      - 4.3.4. Arsitektur Sistem
      - 4.3.5. Desain Basis Data
      - 4.3.6. Peran dan Hak Akses Pengguna
      - 4.3.7. Keamanan Sistem
      - 4.3.8. Kinerja dan Skalabilitas
      - 4.3.9. Pelaksanaan Proyek
   - 4.4. Faktor Penentu Keberhasilan
   - 4.5. Keuntungan Yang Diharapkan
   - 4.6. Teknologi Yang Digunakan
   - 4.7. Pengujian dan Validasi Sistem
   - 4.8. Deseminasi Proyek
- BAB V PENUTUP
   - 5.1. Kesimpulan
   - 4.2. Saran
- DAFTAR RIWAYAT HIDUP
- LAMPIRAN - LAMPIRAN
- Gambar II. 1Komponen Sistem Informasi Manajemen Halaman
- Gambar II. 2 Pola Perputaran dari Sistem Development Life Cycle
- Gambar II. 3 Metode Waterfall
- Gambar III. 1 Tahapan Penelitian
- Gambar IV. 1 Framework Laravel
- Gambar IV. 2 Use Case Diagram Sistem Informasi CUR-HEART
- Gambar IV. 3 Activity Diagram Reservasi Terapi
- Gambar IV. 4 Activity Diagram Dokumentasi Sesi Terapi
- Gambar IV. 5 Activity Diagram Generate Laporan
- Gambar IV. 6 Activity Diagram Generate Laporan
- Gambar IV. 7 Mockup Landing Page
- Gambar IV. 8 Mockup Halaman Tentang Kami
- Gambar IV. 9 Mockup Katalog Layanan
- Gambar IV. 10 Mockup Detail Layanan
- Gambar IV. 11 Mockup Direktori Terapis
- Gambar IV. 12 Mockup Profil Terapis
- Gambar IV. 13 Mockup Daftar Blog
- Gambar IV. 14 Mockup Detail Blog
- Gambar IV. 15 Mockup Hubungi Kami
- Gambar IV. 16 Mockup FAQ
- Gambar IV. 17 Mockup Kebijakan Privasi
- Gambar IV. 18 Mockup Syarat & Ketentuan
- Gambar IV. 19 Mockup Login
- Gambar IV. 20 Mockup Registrasi Klien
- Gambar IV. 21 Mockup Registrasi Terapis
- Gambar IV. 22 Mockup Lupa Kata Sandi
- Gambar IV. 23 Mockup Reset Kata Sandi
- Gambar IV. 24 Mockup Dasbor Klien
- Gambar IV. 25 Mockup Reservasi Langkah 1 - Pilih Layanan
- Gambar IV. 26 Mockup Reservasi Langkah 2 - Pilih Terapis
- Gambar IV. 27 Mockup Reservasi Langkah 3 - Pilih Jadwal vii
- Gambar IV. 28 Mockup Reservasi Langkah 4 - Konfirmasi & Pembayaran
- Gambar IV. 29 Mockup Reservasi Berhasil
- Gambar IV. 30 Mockup Janji Temu
- Gambar IV. 31 Mockup Detail Janji Temu
- Gambar IV. 32 Mockup Dasbor Kemajuan
- Gambar IV. 33 Mockup Pesan
- Gambar IV. 34 Mockup Pengaturan Klien
- Gambar IV. 35 Mockup Notifikasi Klien
- Gambar IV. 36 Mockup Dasbor Terapis - Dasbor Utama
- Gambar IV. 37 Mockup Manajemen Jadwal
- Gambar IV. 38 Mockup Pengaturan Ketersediaan
- Gambar IV. 39 Mockup Daftar Klien
- Gambar IV. 40 Mockup Tampilan Profil Klien
- Gambar IV. 41 Mockup Ruang Sesi
- Gambar IV. 42 Mockup Formulir Catatan Sesi
- Gambar IV. 43 Mockup Riwayat Sesi
- Gambar IV. 44 Mockup Dasbor Pendapatan
- Gambar IV. 45 Mockup Edit Profil Terapis
- Gambar IV. 46 Mockup Pengaturan Terapis
- Gambar IV. 47 Mockup Pesan Terapis
- Gambar IV. 48 Mockup Notifikasi Terapis
- Gambar IV. 49 Mockup Dasbor Admin - Dasbor Utama
- Gambar IV. 50 Mockup Manajemen Reservasi
- Gambar IV. 51 Mockup Manajemen Pengguna
- Gambar IV. 52 Mockup Laporan Keuangan
- Gambar IV. 53 Mockup Pengaturan Sistem
- Gambar IV. 54 Mockup Notifikasi Admin
- Gambar IV. 55 Mockup Pesan Admin
- Gambar IV. 56 Mockup Detail Pengguna
- Gambar IV. 57 Mockup Edit Pengguna
- Gambar IV. 58 Mockup Detail Reservasi
- Gambar IV. 59 Mockup Manajemen Transaksi viii
- Gambar IV. 60 Mockup Manajemen Penarikan
- Gambar IV. 61 Mockup Detail Penarikan
- Gambar IV. 62 Mockup Log Aktivitas
- Gambar IV. 63 Mockup Laporan & Analitik
- Gambar IV. 64 Mockup Manajemen Ulasan
- Gambar IV. 65 Mockup Manajemen Promo
- Gambar IV. 66 Mockup Verifikasi Terapis
- Gambar IV. 67 Mockup Editor Blog
- Gambar IV. 68 Mockup Manajemen Konten Blog
- Gambar IV. 69 Mockup Editor FAQ
- Gambar IV. 70 Mockup Manajemen Konten FAQ
- Gambar IV. 71 Mockup Editor Layanan
- Gambar IV. 72 Mockup Manajemen Konten Layanan
- Gambar IV. 73 Mockup Editor Promo
- Gambar IV. 74 Ringkasan Stack Teknologi
- Tabel III. 1 Jadwal Penelitan Halaman
- Tabel III. 2 Distribusi Sampel Penelitian
- Tabel III. 3 Daftar Narasumber Wawancara
- Tabel IV. 1 Work Breakdown Structure (WBS)
- Tabel IV. 2 Gantt Chart
- Tabel IV. 3 Jadwal Pengerjaan Proyek
- Tabel IV. 4 Estimasi Biaya Proyek
- Tabel IV. 5 Estimasi Biaya Operasional Tahunan
- Tabel IV. 6 Alokasi Sumber Daya Manusia
- Tabel IV. 7 Identifikasi dan Mitigasi Risiko
- Tabel IV. 8 Matriks Perencanaan Komunikasi
- Tabel IV. 9 Daftar Pengadaan
- Tabel IV. 10 Daftar Pemangku Kepentingan
- Tabel IV. 11 Key Performance Indicators (KPI)
- Tabel IV. 12 Cakupan Pengujian Fungsional Prototipe
- Tabel IV. 13 Profil Responden Pengujian SUS
- Tabel IV. 14 Pertanyaan Kuesioner SUS
- Tabel IV. 15 Hasil Skor SUS per Responden
- Tabel IV. 16 Skor SUS Berdasarkan Kategori Pengguna
- Tabel IV. 17 Rata-rata Skor per Pertanyaan SUS
- Tabel IV. 18 Skenario dan Hasil UAT
- Tabel IV. 19 Acceptance Criteria
- Tabel IV. 20 Luaran Desiminasi Proyek


```
x
```
## DAFTAR LAMPIRAN

Halaman
Lampiran A Prototipe CUR-HEART ................................................................. 171
Lampiran B Hasil _System Usability Scale_ (SUS) _..............................................._ 172


```
xi
```
## DAFTAR SIMBOL

## Simbol Entity Relationship Diagram (ERD)

## NO GAMBAR NAMA KETERANGAN

## 1^ Entity

```
Simbol yang menyatakan himpunan
entitas ini bisa berupa : suatu elemen
lingkungan, sumber daya, atau
transaksi, yang begitu pentingnya
bagi perusahaan sehingga
didokumentasikan dengan data.
```
```
2
Attribute
```
```
Simbol terminal ini untuk
menunjukkan nama-nama atribut
yang ada pada entity.
```
##### 3

## Primary Key

```
Attribute
```
```
Simbol atribut yang digaris bawahi,
berfungsi sebagai key (kunci) di
antara nama-nama atribut yang ada
pada suatu entity.
```
##### 4

```
Relationship
```
```
Simbol ini menyatakan relasi ini
digunakan untuk menunjukkan
hubungan yang ada antara entity
yang satu dengan entity yang
lainnya.
```
```
5 Link
```
```
Simbol berupa garis ini digunakan
sebagai penghubung antara entity
dengan atributnya dan himpunan
entitas dengan himpunan relasi.
```

##### 1

##### BAB I

##### PENDAHULUAN

**1.1. Latar Belakang Masalah**

Di era ekonomi modern saat ini tanpa disadari menuntut masyarakat untuk
terus bekerja dengan harapan bisa memenuhi semua kebutuhan pokok dan
kebutuhan sosial yang tinggi berujuan mencapai kepentingan personal branding
atau sering dikenal dengan _Flexing_. Fenomena ini dipicu oleh tekanan pekerjaan,
ketidakstabilan ekonomi dan gangguan digital (Sosial Media). Pengaruh ekonomi
modern saat ini memberikan dampak yang cukup signifikan meningkat oleh
kesehatan mental dan menjadi isu kesehatan global yang mendesak di abad ke-21.
Kesehatan mental merupakan terwujudnya keselarasan yang sungguh-sungguh
antara fungsi kejiwaan yang menciptakan penyesuaian diri antara manusia oleh
dirinya sendiri dan lingkunganya [1].
Indonesia memiliki rasio psikiater dan psikolog yang sangat rendah
(1:200.000), jauh di bawah standar WHO (1:100.000). Layanan kesehatan mental
konvensional seringkali memiliki waktu tunggu lama, biaya tinggi, lokasi tidak
mudah diakses, serta proses administrasi rumit. Di tengah keterbatasan ini,
hipnoterapi ( _hypnotherapy_ ) sebagai metode terapi alternatif mulai mendapat
perhatian sebagai solusi efektif dan efisien.
CUR-HEART ( _Hypnotherapy & Mind Wellness Center_ ) hadir sebagai pusat
layanan terapi kesehatan mental yang mengintegrasikan pendekatan hipnoterapi
modern dengan nilai spiritualitas dan humanisme. Namun, CUR-HEART
menghadapi tantangan manajerial: (1) proses pemesanan manual via
telepon/ _WhatsApp_ menyebabkan kesalahpahaman dan pemesanan ganda; (2)
manajemen jadwal terapis menggunakan _spreadsheet_ tidak efisien dan rawan
kesalahan; (3) dokumentasi catatan terapi menggunakan kertas/ _Word_ terpisah
menyulitkan pencarian riwayat; (4) tidak ada sistem pelacakan kemajuan klien yang
terstruktur; (5) klien tidak memiliki _platform_ layanan mandiri ( _self-service_ ); (6)
kesulitan dalam analisis data operasional dan pengambilan keputusan strategis; (7)
sistem pembayaran manual rawan kesalahan dan kehilangan transaksi; (8) risiko
keamanan dan privasi data tinggi.


Pengembangan sistem informasi manajemen pemesanan dan terapi berbasis
web menggunakan _Laravel Framework_ menjadi solusi untuk mengotomatisasi
proses bisnis, meningkatkan akurasi data, memfasilitasi komunikasi, serta
menyediakan dasbor pemantauan untuk pengambilan keputusan berbasis data.
Sistem ini dirancang dengan 41 halaman antarmuka mencakup halaman publik,
autentikasi, dan dasbor untuk klien, terapis, dan admin, menggunakan pendekatan
SDLC _Waterfall_ dengan desain responsif _mobile-first_.

**1.2. Identifikasi Masalah**
Berdasarkan analisis kondisi eksisting melalui observasi, wawancara dengan
pemangku kepentingan, dan studi dokumentasi proses bisnis, teridentifikasi
permasalahan utama :

1. Proses Pemesanan Tidak Efisien : Komunikasi manual via _WhatsApp_
    menyebabkan tingkat konversi hanya 60%, tidak ada transparansi informasi
    terapis dan layanan, klien tidak dapat membandingkan sebelum
    memutuskan.
2. Ketiadaan Sistem Manajemen Jadwal Terpadu : Penjadwalan manual
    menyebabkan konflik jadwal, tidak ada sistem pemblokiran tanggal untuk
    cuti, ketimpangan beban kerja antar terapis.
3. Dokumentasi Tidak Terstruktur : Catatan terapi terpisah-pisah, sulit diakses,
    tidak ada templat standar, risiko kehilangan data tinggi, tidak ada sistem
    pencadangan.
4. Tidak Ada Pelacakan Kemajuan Klien : Klien tidak dapat melihat
    perkembangan terapi, tidak ada data terukur untuk evaluasi keberhasilan,
    sulit identifikasi klien yang perlu perhatian khusus.
5. Keterbatasan Akses Informasi Klien : Tidak ada platform _self-service_ , klien
    bergantung penuh pada admin, tidak dapat melakukan penjadwalan ulang
    mandiri.
6. Kesulitan Pengambilan Keputusan : Tidak ada laporan otomatis, analisis
    manual memakan waktu, tidak ada _business intelligence_ untuk optimasi
    operasional.


7. Sistem Pembayaran Tidak Terpadu : Verifikasi manual, rekonsiliasi sulit,
    tidak ada variasi metode pembayaran digital, pelacakan status pembayaran
    sulit.
8. Risiko Keamanan Data Tinggi : Tidak ada enkripsi, akses tidak terkontrol,
    tidak ada jejak audit, tidak patuh regulasi perlindungan data pribadi (UU
    No. 27 Tahun 2022).
Dampak kumulatif : penurunan efisiensi operasional, potensi kehilangan
pendapatan, risiko reputasi, terhambatnya skalabilitas bisnis, hilangnya peluang
optimasi.

**1.3. Ruang Lingkup
1.3.1. Ruang Lingkup Sistem**
Sistem informasi CUR-HEART mencakup :
Modul Utama :

1. Manajemen Pengguna : Registrasi, autentikasi multi-peran (Admin,
    Terapis, Klien), profil pengguna, kontrol akses berbasis peran (RBAC).
2. Manajemen Layanan : CRUD layanan terapi, kategori layanan, harga dan
    durasi, deskripsi detail, gambar layanan.
3. Manajemen Pemesanan : Alur pemesanan 4 langkah (pilih layanan → pilih
    terapis → pilih jadwal → pembayaran), kalender ketersediaan real-time,
    konfirmasi otomatis, notifikasi email/SMS.
4. Manajemen Jadwal Terapis : Pengaturan ketersediaan (hari, jam
    operasional, jadwal berulang), pemblokiran tanggal cuti, visualisasi
    kalender, pencegahan konflik jadwal.
5. Manajemen Sesi Terapi **:** Dokumentasi catatan terapi terstruktur, templat
    berdasarkan jenis layanan, riwayat sesi per klien, pelacakan kemajuan
    dengan metrik (skala kecemasan, frekuensi sesi).
6. Sistem Pembayaran : Integrasi payment gateway (Midtrans), multiple
    _payment methods_ ( _Virtual Account_ , _E-wallet, QRIS_ , Kartu Kredit),
    verifikasi otomatis, _invoice_ digital.


7. Dasbor Analitik **:** Dasbor Admin (metrik bisnis komprehensif), Dasbor
    Terapis (jadwal, klien, pendapatan), Dasbor Klien (riwayat pemesanan,
    progress tracking).
8. Manajemen Konten : Halaman informatif (About, Services, Blog), FAQ,
    Privacy Policy, Terms & Conditions.
**1.3.2. Ruang Lingkup Teknologi**
a. _Backend_ :
- _Framework : Laravel_ 10.x (PHP 8.2)
- _Database : MySQL_ 8.
- _Authentication : Laravel Sanctum_
- _Payment Gateway_ : Midtrans API
b. _Frontend_ **:**
- _Blade Templating Engine_
- _Tailwind_ CSS 3.x
- _Alpine.js_ (interaktivitas ringan)
- _Responsive Design_ (Mobile-first)
c. _Infrastructure_ **:**
- _Web Server_ : _Nginx_ / _Apache_
- _Hosting_ : VPS ( _Niagahoster_ /AWS)
- _Version Control_ : _Git/GitHub_
- _Deployment_ : Manual/CI-CD
**1.3.3. Ruang Lingkup Pengguna**
a. Tiga Peran Pengguna :
1. Admin : Manajemen seluruh sistem, _users, bookings, services_ , laporan
keuangan, pengaturan sistem.
2. Terapis : Manajemen jadwal pribadi, lihat klien assigned, buat catatan
sesi, lihat pendapatan, kelola profil.
3. Klien : Reservasi layanan, lihat riwayat pemesanan, tracking _progress_ ,
komunikasi dengan terapis, kelola profil.
**1.3.4. Batasan Sistem**
1. Tidak mencakup video _conferencing_ untuk sesi online (menggunakan _tools_
eksternal seperti _Zoom_ / _Google Meet_ ).


2. Tidak ada aplikasi _mobile native_ ( _responsive web only_ ).
3. Tidak ada integrasi dengan _Electronic Health Record_ (EHR) _eksternal_.
4. Tidak ada sistem _inventory_ untuk produk fisik atau _merchandise_.
5. Tidak ada _multi-language support_ (Bahasa Indonesia).
6. Tidak ada sistem _loyalty_ /membership dengan poin _reward_.
7. Tidak mencakup AI/ML untuk rekomendasi terapis atau prediksi.
8. Tidak ada forum/komunitas untuk klien.

**1.4. Tujuan dan Manfaat Penelitian
1.4.1. Tujuan Penelitian
Tujuan Umum :** Mengembangkan CUR-HEART: Inovasi Sistem
Informasi Layanan Terapi Mental Berbasis Digital untuk meningkatkan efisiensi
operasional dan kualitas layanan CUR-HEART.
**Tujuan Khusus :**

1. Menganalisis proses bisnis eksisting dan kebutuhan sistem CUR-HEART.
2. Merancang arsitektur sistem, _database,_ dan antarmuka pengguna yang _user-_
    _friendly_.
3. Mengimplementasikan sistem menggunakan _Laravel Framework_ dengan
    fitur komprehensif.
4. Melakukan pengujian fungsional, _usability_ , dan _performance_ untuk
    memastikan kualitas.
5. Menghasilkan dokumentasi lengkap untuk pemeliharaan dan
    pengembangan.
**1.4.2. Manfaat Penelitian
a. Bagi CUR-HEART :**
1) Efisiensi operasional meningkat 40%
2) Pengurangan kesalahan administrasi 60%
3) Peningkatan konversi pemesanan dari 60% ke 85%
4) Data terpusat untuk _business intelligence_
5) Skalabilitas untuk pertumbuhan bisnis
**b. Bagi Terapis :**
1) Manajemen jadwal otomatis


2) Akses mudah ke riwayat klien
3) _Tracking_ kinerja dan pendapatan
4) Dokumentasi terstruktur
5) Fokus pada layanan terapi, bukan administrasi
**c. Bagi Klien :**
1) Kemudahan _booking_ 24/
2) Transparansi informasi layanan dan terapis
3) _Self-service_ portal
4) _Tracking progress_ terapi
5) Pengalaman pengguna lebih baik
**d. Bagi Akademik :**
1) Model referensi pengembangan sistem informasi kesehatan mental
2) Kontribusi literatur tentang implementasi Laravel di sektor _healthcare_
3) Studi kasus SDLC _Waterfall_ dalam proyek nyata
4) Dokumentasi _best practices_ untuk mahasiswa
**e. Bagi Masyarakat :**
1) Peningkatan akses layanan kesehatan mental
2) Mengurangi stigma melalui kemudahan akses digital
3) Model sistem yang dapat diadopsi pusat terapi lain
4) Kontribusi pada digitalisasi layanan kesehatan Indonesia


##### 7

##### BAB II

##### TINJAUAN PUSTAKA

**2.1. Landasan Teori**
A. Pengertian Sistem Informasi
Sistem merupakan kumpulan kelompok atau perangkat yang mempunyai
hubungan antara satu unsur dengan lainnya berfungsi dalam mencapai suatu
tujuan tertentu bersama [2].
Sistem adalah kumpulan prosedur kerja yang terjalin erat yang bekerja
bersama sebagai satu jaringan demi menyelesaikan suatu kegiatan atau mencapai
sasaran akhir tertentu [3].
Informasi adalah sekumpulan fakta yang terhimpun diolah menjadi data
yang memiliki nilai yang dapat digunakan oleh siapapun yang membutuhkan
data tersebut dalam mengambil keputusan maupun untuk ilmu pengetahuan[3].
Informasi adalah aset non-fisik yang krusial yang digunakan manajemen
untuk menjalankan dan mengarahkan perusahaan [4].
Sistem Informasi adalah seluruh bagian teknologi dan prosedur yang
disatukan sepenuhnya untuk mengelola data agar perusahaan atau organisasi
selalu dapat menyajikan informasi yang akurat dari data yang telah diproses dan
disimpan [5].
Sistem Informasi adalah susunan komponen yang saling terkait yang
berfungsi untuk menghimpun, memproses, menyimpan, dan menyebarluaskan
data dan informasi [6].
Fungsi Sistem Informasi :

1. Sistem memastikan adanya standar kualitas yang tinggi dan kompetensi
    yang memadai dalam mengelola sistem informasi itu sendiri, dilakukan
    melalui pemikiran yang kritis dan terstruktur.
2. Kemampuan sistem dalam menyediakan mutu (kualitas) serta pengalaman
    yang diperlukan untuk menjalankan pengelolaan sistem informasi dengan
    cara yang logis dan penuh analisis.
3. Menyediakan kemampuan untuk menganalisis situasi guna mengurangi
    potensi kerugian yang berasal dari aspek ekonomi.


4. Menyediakan kemudahan akses yang baik bagi semua penggunanya.
5. Dapat membantu organisasi atau perusahaan mencapai sasarannya dengan
    lebih cepat, berkat adanya data pendukung yang terjamin kebenarannya [7].

Dalam konteks proyek ini, CUR-HEART: Inovasi Sistem Informasi
Layanan Terapi Mental Berbasis Digital termasuk kategori Sistem Pemrosesan
Transaksi (TPS) karena menangani transaksi pemesanan, pembayaran, dan
dokumentasi sesi terapi, serta Sistem Informasi Manajemen (MIS) karena
menyediakan pelaporan dan analitik untuk mendukung pengambilan keputusan
manajerial.

```
B. Manfaat Sistem Informasi
Manfaat sistem informasi antara lain sebagai berikut ini :
```
1. Menyediakan kemudahan akses data yang disajikan secara akurat dan tepat
    waktu bagi pengguna, sehingga pengguna dapat mengaksesnya tanpa
    memerlukan pihak perantara.
2. Memastikan ketersediaan mutu serta keahlian yang memadai dalam
    mengoperasikan sistem informasi dengan pendekatan yang kritis.
3. Mendukung pengembangan proses perencanaan yang lebih efektif.
4. Menentukan keahlian dan keterampilan apa saja yang dibutuhkan untuk
    mendukung operasional sistem informasi.
5. Memungkinkan organisasi menetapkan investasi yang akan difokuskan
    pada pengembangan dan pemanfaatan sistem informasi.
6. Mampu memprediksi dan menganalisis dampak atau konsekuensi finansial
    (ekonomi) yang mungkin timbul dari penerapan sistem informasi dan
    teknologi baru.
7. Meningkatkan daya guna atau efisiensi dalam fase aplikasi, pengembangan,
    dan pemeliharaan sistem.
8. Mampu mengolah transaksi, mengurangi biaya operasional, dan
    menghasilkan pendapatan sebagai produk atau layanan utama perusahaan
    [8].


**2.1.1. Sistem Informasi Manajemen**
A. Pengertian Sistem Informasi Manajemen
Manajemen yaitu menggabungkan sistematis dan kreatifitas dalam
merealisasikan tugas-tugas yang telah ditetapkan, dengan mengandalkan
pelaksanaan oleh pihak lain [9].
Manajemen adalah suatu proses rangkaian yang terdiri dari perencanaan,
pengorganisasian, kepemimpinan dan pengendalian dalam pengunaan semua
sumber daya yang dimiliki dalam mencapai tujuan yang telah ditentukan sesuai
dengan target [9].
Sistem Informasi Manajemen yaitu susunan terstruktur dari berbagai
komponen yang saling terkait, bekerja sama untuk menghasilkan data yang
kemudian dimanfaatkan oleh pihak manajemen perusahaan [9].
Sistem Informasi Manajemen adalah suatu sistem yang yang digunakan
untuk menyediakan informasi yang efektif dalam mendukung pengambilan
keputusan kegiatan manajemen [10].
B. Komponen Sistem Informasi Manajemen Secara Fisik
Komponen sistem informasi manajemen secara fisik yaitu seluruh perangkat
dan peralatan fisik digunakan untuk mengoperasikan sistem informasi
manajemen. Komponen terdiri atas :

1. Perangkat Keras ( _Hardweare_ ) : perangkat yang digunakan secara fisik
    seperti komputer dan alat yang dibutuhkan.
2. Perangkat Lunak ( _Software_ ) : serangkaian instruksi yang dapat memproses
    data ke perangkat keras.
3. Basis Data _(Database)_ : kumpulan-kumpulan hubungan tabel dan
    komponen lain, yang melakukan penyimpanan data-data.
4. Prosedur pengoperasian : susunan aturan petunjuk untuk menggunakan
    sistem informasi berbasis komputer.
5. Personalian pengoperasian ( _Brainware_ ) : ahli komputer, manajer,
    pengguna, penganalisis, penyusun program, manajer basis data, dan jabatan
    yang berkaitan dengan memanfaatkan sistem informasi komputer.
6. Komunikasi data dan jaringan computer [11].


```
Sumber : Gede et al.,2022^
Gambar II. 1 Komponen Sistem Informasi Manajemen
C. Fungsi DBMS ( Database Management System )
Mengidentifikasikan terdiri dari beberapa fungsi DBMS yang digunakan
dalam mengatur data dalam sistem antara lain :
```
1. Manajemen penjagaan integritas data
2. Diimplementasikan menjadi kamus data
3. Menampilkan _interface_ dalam komunikasi
4. Peralihan dan sajian data-data
5. Keamanan data-data
6. Bisa mengakses lebih dari satu pengguna ( _multi access_ )
7. Penyimpanan data-data ( _Data Storage Management_ )
8. Tersedia prosedur _Recovery_ dan _Backup_
9. Menyediakan akses bahasa dan pemrograman dan manajemen [11].
**2.1.2. Inovasi Layanan Terapi Kesehatan Mental Berbasis Digital**
A. Pengertian Layanan Terapi
_Telemedicene_ adalah layanan berbasis teknologi yang bertujuan untuk
memudahkan konsultasi kesehatan dari jarak jauh. Telemedicene juga disebut
sebagai penyedia layanan secara jarak jaruh oleh para professional kesehatan
mental seperti psikolog yang menggunakan digital teknologi informasi dan
komunikasi [12].


```
Terapi realitas adalah sistem yang memfokuskan pada tingkah laku saat ini
dan melakukan penerimaan serta tanggung jawab pribadi. Terapis mempunyai
fungsi sebagai mediator yang mengonfrontasikan klien menggunakan cara
yang bisa membantu klien bisa menghadapi masalah dan memenuhi kebutuhan
tanpa merugikan dirinya sendiri dan orang lain [13].
Teknik yang digunakan dalam terapi realitas yaitu Teknik WDEP antara
lain:
```
1. W = _Wants_ (Keinginan) dalam hal ini klien memberikan eksplorasi dalam
    segi kehidupan termasuk hal diinginkan.
2. D = _Doing and Direction_ (Tindakan dan Arah) hal ini mencakup empat
    komponen eksplorasi antara lain : tindakan, pikiran, perasaan dan fisiologi.
3. E = _Evaluation_ (Evaluasi) memberikan evaluasi pada klien.
4. P = _Plannning_ (Rencana) memberikan bantuan pada klien untuk tindakan
    rencana [14].
**2.1.3. Siklus Hidup Pengembangan Sistem (** **_System Development Life
Cycle/SDLC_** **)**
A. Pengertian SDLC
    _System Development Life Cycle_ atau SDLC merupakan metode proses
pembangunan sistem informasi [15]. Metode ini terdapat tahapan-tahapan yaitu
: perencanaan, analisis, perancangan, implementasi, pengujian dan pemiliharaan.
Metode SDLC biasanya digunakan di dalam sitem informasi seperti _Waterfall_
dan _Prototype_.
_System Development Life Cycle_ (SDLC) adalah salah satu metode
pengembangan sistem informasi yang terkenal pertama kali sistem informasi
dikembangkan [16].
Tahapan yang terdapat pada SDLC yaitu :
1. _Investigate_
2. _Analyze_
3. _Design_
4. _Implement_
5. _Maintainance[17]_


Sumber : Irpan et al.,202 4

## Gambar II. 2 Pola Perputaran dari Sistem Development Life Cycle

B. Metode Air Terjun ( _Waterfall_ )
Waterfall adalah model pengembangan aplikasi yang masuk ke dalam
_classic life cycle_ (siklus hidup klasik), dimana metode ini menekankan pada fase
berurutan dan sistematis. Pengembangan model ini dapat digambarkan seperti
air terjun, karena setiap tahapnya dikerjakan secara berurutan mulai dari atas
sampai ke bawah [18].
Metode _Waterfall_ adalah metode pengembangan sistem yang tertata dan
terstrukur yang setiap tahapan dilakukan secara bertahap dan tidak bisa
dilanjutkan sampai setiap tahapan sebelumnya selesai [19].

```
Sumber : Fachri B et al.,202 4
```
## Gambar II. 3 Metode Waterfall


- Tahapan Metode Air Terjun ( _Waterfall)_ :
    1. Perencanaan Konsep ( _Requirements Analysis_ ) :
       Tahapan ini dilakukan analisis untuk melakukan pemahaman kebutuhan
dan permintaan yang tepat dari pelanggan dan pengumpulan data dapat
dilakukan dengan wawancara langsung kepada yang mempunyai
kepentingan. Setelah itu mendapatkan hasil analisis kebutuhan sistem yang
berkaitan dengan persyaratan perangkat lunak dan sesuai spesifikasi
kebutuhan dalam sistem baik dokumentasi sesuai kualifikasi kebutuhan
pengembangan perangkat lunak.
    2. Pemodelan Sistem ( _System Design_ ) :
       Tahapan ini merupakan analisis kebutuhan sistem yang sebelumnya
sudah dibuat namun dituangkan menjadi sebuah desai sistem yang
selanjutnya dilakukan proses pengkodean.
    3. Implementasi ( _Implementation_ ) :
       Tahapan ini melakukan proses coding atau pengkodean untuk
menerjemahkan desain sistem menjadi aplikasi.
    4. Pengujian ( _Testing_ ) :
       Sistem yang sudah selesai dibuat selanjutnya akan diuji untuk melihat
keberhasilan sistem, menentukan kinerja dan optimasi apakah sudah sesuai
dengan kebutuhan.
    5. Pemeliharaan ( _Maintenance_ ) :
       Tahap ini dilakukan untuk melakukan pemeliharaan sistem apabila
menemukan _error_ atau _bug_ [20]
- Kelebihan Model Air Terjun ( _Waterfall_ ) :
    1. Persyaratan harus sudah ditentukan semua di awal, sebelum melakukan
       pembuatan program.
    2. Sistem ini bagus karena mempunyai cara kerja yang teratur sehingga
       kualitas perangkat lunak akan terjaga.
    3. Urutan kerja yang jelas dan masuk akal sehingga dapat membantu
       menghindari kesalahan yang besar sejak perancangan awal dibuat.
    4. Jumlah total proyek bisa diperkirakan dengan akurasi tepat, apabila
       tidak ada masalah.


5. Proses ini menentukan dengan pasti kapan pekerjaan dimulai dan kapan
    pekerjaan selesai [21].
- Kekurangan Model Air Terjun ( _Waterfall_ ):
1. Tidak bisa melakukan perubahan ditengah kondisi jalannya proyek
2. Jika terjadi perubahan yang diperlukan maka proyek harus diinisiasi dari
tahap awal. Dalam hal ini dapat menimbulkan tambahan biaya anggaran
bagi organisasi
3. Kualitas dapat dinilai eksklusif oleh pengguna secara langsung pada
tahap akhir
4. Produk yang dihasilkan tidak cepat selesai harus menunggu sampai
tahapan selesai
5. Mempunyai resiko yang besar apabila project tertunda peluncuran karena
bisa mempengaruhi kebutuhan klien yang bisa berubah [21].

Dalam proyek CUR-HEART: Inovasi Sistem Informasi Layanan Terapi
Mental Berbasis Digital ini, model Air Terjun dipilih karena :
a. Persyaratan sudah cukup jelas dan stabil berdasarkan analisis proses
bisnis yang ada
b. Cakupan proyek terdefinisi dengan baik dan tidak diharapkan ada
perubahan signifikan
c. Proyek memiliki garis waktu yang tetap (semester akademik)
d. Dokumentasi lengkap diperlukan untuk keperluan akademik (Proyek
Akhir/ _Capstone Project_ )
e. Tim pengembang relatif kecil dan terstruktur

```
C. Model SDLC Lainnya ( Comparison )
Selain Waterfall, terdapat beberapa model SDLC lain yang populer
seperti Agile , Spiral, V-Model, RAD, dan, DevOps. Namun, model Waterfall
dipilih untuk proyek CUR-HEART dengan pertimbangan berikut:
```
1. Persyaratan Jelas dan Stabil : Kebutuhan sistem sudah teridentifikasi dengan
    baik melalui analisis bisnis CUR-HEART


2. Garis Waktu Tetap : Proyek dibatasi waktu semester akademik (11 minggu)
    sehingga memerlukan perencanaan yang terukur
3. Dokumentasi Lengkap : Kebutuhan akademik memerlukan dokumentasi
    komprehensif di setiap fase
4. Tim Kecil dan Terstruktur : Pengembangan dilakukan oleh tim kecil dengan
    struktur jelas, cocok dengan model sekuensial
5. Skala Proyek Sesuai : Sistem dengan kompleksitas menengah yang tidak
    memerlukan iterasi _sprint_ berulang

**2.1.4. Hipnoterapi dan Kesehatan Mental**
A. Pengertian Hipnoterapi
Hipnoterapi ( _hypnotherapy_ ) adalah bentuk psikoterapi komplementer yang
menggunakan teknik hipnosis untuk membantu individu relaksasi yang
mendalam untuk mencapai perubahan positif dalam pikiran, perasaan, dan
perilaku. Dalam keadaan ini, klien menjadi lebih terbuka terhadap saran yang
diberikan oleh terapis. Hal ini memungkinkan akses ke pikiran bawah sadar di
mana kepercayaan, kenangan, dan emosi disimpan. Hipnoterapi fokus pada
modifikasi dan pemahaman perilaku emosi yang berasal dari pikiran bawah
sadar yang biasanya menjadi akar dari berbagai gangguan psikologis pola pikir,
trauma, kecemasan, fobia dan kebiasan yang _negative_ [22].

```
B. Efektivitas Hipnoterapi
Berbagai penelitian ilmiah telah membuktikan efektivitas hipnoterapi dalam
menangani berbagai kondisi psikologis :
1) Adanya penurunan signifikan melalui tingkat ansietas klien menerima
intervensi Hipnoterapi dan Neuro Linguistic Programming (NPL)
menggunakan analisis Wilcoxon Signed Rank Test yang terdapat skor
negative ranks sebanyak 10 terdiri dari nilai Z ( score ) = -2,972 dan
signifikasi p ( value ) = 0,003. Tidak ditemukan positive ranks , hasilnya tidak
menunjukkan adanya peningkatan gejala ansietas setelah melakukan
intervensi. Dalam hal ini merupakan bukti pengamatan dengan pendekatan
hipnoterapi dan NPL memiliki dampak klinis yang signifikan dan konsisten
```

dalam mengurangi gejala ansietas.
2) Hipnoterapi bertujuan pada pencapaian kondisi _trance terapeutik_ yang
memungkinkan klien mengakses memori emosional seperti traumatis atau
kecemasan untuk penataan kembali [23].

C. Kesehatan Mental di Indonesia
Kesehatan mental memiliki peran cukup penting untuk masalah kesehatan
setiap manusia. Walaupun, seseorang yang mempunyai kesehatan mental yang
baik tidak bebas dari berbagai macam gangguan mental yang kerap terjadi.
Gangguan mental merupakan keadaan emosi yang mengidentifikasikan
individu mengalami perubahan yang mungkin dapat berkembang menjadi
keadaan tidak normal (patalogis) apabila terus berkelanjutan [24].

1. Faktor-faktor yang mempengaruhi :
    a. Faktor biologis : Riwayat keluarga dengan gangguan mental,
       hormonal dan kondisi medis tertentu
    b. Faktor psikologis : Terkait keperibadian, pengalaman trauma dan
       perilaku mengatasi masalah ( _coping behavior_ ) yang kurang efektif
    c. Faktor sosial : Media sosial, kecanduan digital, dinamika kelurga, dan
       kurangnya dukungan sosial dari orang-orang terdekat
    d. Faktor biologis, psikologis dan sosial : Pandemi COVID- 19 [25].
2. Tantangan dalam Layanan Kesehatan Mental :
a. Tingkat kesadaran dan stigma yang masih banyak merasa ragu untuk
melakukan pencarian bantuan professional karena takut dihakimi dan
bahkan dicemooh oleh orang lain
b. Penggunaan digitalisasi dalam kesehatan mental memudahkan dalam
konsultasi namun khawatir tentang interaksi personal dalam terapi
secara online yang bisa mempengaruhi efektivitas sesi perawatan
c. Kurangnya adanya partisipasi dan dukungan sosial seperti keluarga,
teman atau komunitas positif dalam mengatasi masalah tentang
kesehatan mental yang dialami setiap individu
d. Inovasi digital terapi kesehatan mental sangat memudahkan untuk
mengakses informasi dan dukungan kesehatan mental tetapi ada


```
beberapa kalangan yang mempunyai keterbatasan dalam akses
internet seperti didaerah terpencil [26].
```
3. Peluang Layanan Kesehatan Mental Digital :
    a. _Telemedicine_ memudahkan klien mendapatkan layanan konsultasi
       tanpa batasan jarak dan geografis dan aplikasi starup kesehatan
       berbasis digitalisasi di eropa meningkat sebesar 45% dari 5 tahun
       terakhir
    b. Pemberdayaan kewirausahaan digital / _startup_ dapat membantu misi
       sosial dan menjebatani antara inovasi teknologi dengan kesejahteraan
       masyarakat luas melalui komunitas berbasis digital
    c. Pertumbuhan digital kesehatan tidak hanya memperkuat bidang
       kesehatan saja tetapi dapat menciptakan ekosistem kewirausahaan /
       _start-up_ sehingga memberikan peluang pekerjaan untuk masyarakat
       luas dalam bidang teknologi. Dalam riset laporan Statista 2024 nilai
       pasar global digital health mengalami pertumbuhan tahunan sebesar
       15% dan Kawasan Asia Tenggara mengalami lebih cepat
       pertumbuhan karena tingginya penggunaan internet dan kebutuhan
       layanan kesehetan yang semakin mudah dan efisien [27].

**2.1.5. Kerangka Kerja Laravel (** **_Laravel Framework_** **)**
A. Pengertian Kerangka Kerja Laravel dan Perbandingan Kerangka Kerja PHP
_Framework_ diartikan sebagai kerangka kerja. Framework adalah
menyediakan kerangka kerja untuk membuat sebuah sistem yang tidak harus
merancang sistem dari awal [28].
Laravel adalah kerangka kerja PHP sumber terbuka ( _open-source_ ) yang
dirancang mengikuti arsitektur _Model-View-Controller_ (MVC) yang
digunakan untuk membangun aplikasi _website_ [28].
Laravel dipilih sebagai kerangka kerja pengembangan untuk CUR-HEART
karena beberapa keunggulan dibandingkan alternatif lain
( _Symfony_ , _CodeIgniter_ , _Yii_ , _Slim_ ) :


1. Kecepatan Pengembangan : Fitur bawaan seperti Artisan CLI, _Eloquent_
    _ORM_ , dan sistem autentikasi mempercepat pengembangan hingga 40%
    dibanding framework minimal
2. Kurva Pembelajaran : Dokumentasi komprehensif dan komunitas besar (1
    juta+ pengembang) mempermudah pembelajaran
3. Fitur Lengkap : _Full-stack framework_ dengan _Blade templating, routing_ ,
    _middleware_ , dan _queue system_ tanpa perlu _library eksternal_
4. Keamanan Bawaan : _CSRF protection, XSS prevention, password hashing_
    ( _bcrypt_ ), dan enkripsi data
5. Ekosistem Kuat : 15,000+ package di _Packagist_ dan _resource_ pembelajaran
    seperti _Laracasts_
6. Skalabilitas : Mendukung pengembangan API untuk aplikasi mobile masa
    depan dengan _Laravel Sanctum_
B. Fitur Utama Laravel
    Fitur-fitur modern Laravel membantu _developer_ dalam membuat aplikasi
[29]:
1. Arsitektur MVC ( _Model-View-Controller_ ) :
a. Model : Merepresentasikan data dan logika bisnis, berinteraksi
dengan basis data melalui Eloquent ORM
b. View : Menyajikan data kepada pengguna menggunakan mesin
templat Blade
c. _Controller_ : Perantara antara Model dan View, menangani logika
alur aplikasi
2. _Eloquent ORM_ **:**
a. Pemetaan Relasi-Objek untuk interaksi basis data dengan sintaksis
ekspresif
b. Manajemen relasi (satu-ke-satu, satu-ke-banyak, banyak-ke-banyak)
c. Fitur keamanan seperti perlindungan _mass assignment_ dan
penghapusan lunak
3. Mesin Template Blade **:**
a. Pewarisan templat untuk ketergunaan ulang kode
b. Perlindungan XSS otomatis


```
c. Struktur kontrol yang bersih (@if, @foreach, @while)
d. Direktif autentikasi dan otorisasi
```
4. Fitur Keamanan Bawaan **:**
    a. Autentikasi dan otorisasi berbasis peran
    b. Perlindungan CSRF _(Cross-Site Request Forgery)_
    c. Perlindungan XSS _(Cross-Site Scripting)_
    d. Hashing kata sandi dengan Bcrypt/Argon2
    e. Enkripsi data sensitif
5. Migrasi & Pembenihan Basis Data **:**
    a. Kontrol versi basis data untuk pengelolaan skema
    b. Pembuatan data sampel untuk pengembangan dan pengujian
6. Artisan CLI **:**
a. Perangkat baris perintah untuk otomasi tugas pengembangan
b. Pembuatan kode boilerplate ( _controller_ , model, _migration_ )

**_2.1.6. Database Management System_**
A. Pengertian Basis Data ( _Database_ )
Basis Data ( _Database_ ) adalah sekumpulan data yang saling berhubungan
yang disimpan secara bersamaan tanpa pengulangan yang tidak perlu dalam
memenuhi berbagai macam kebutuhan [30]. _Database Management System_
merupakan kumpulan-kumpulan program aplikasi yang digunakan dalam
membuat dan mengelola _database_ [31].
_B. MySQL
MySQL_ adalah peerangkat lunak manajemen database yang relasional,
_MySQL_ merupakan database open source yang sekarang telah diakuisisi oleh
Oracle [32]
Alasan Pemilihan MySQL untuk CUR-HEART:

1. Kesesuaian Struktur Data **:** Data sistem CUR-HEART bersifat relasional
    dengan hubungan yang jelas antara entitas
    ( _Users_ , _Bookings_ , _Services_ , _Payments_ )
2. Dukungan Laravel : _MySQL_ adalah basis data default Laravel dengan
    integrasi Eloquent ORM yang optimal


3. Transaksi ACID : Mesin InnoDB menyediakan kepatuhan ACID penuh
    untuk keamanan data keuangan dan pemesanan
4. Biaya : Gratis dan tersedia di semua penyedia hosting tanpa biaya tambahan
5. Komunitas : Komunitas RDBMS terbesar dengan dokumentasi luas dan
    dukungan pemecahan masalah
6. Kinerja : Sangat baik untuk operasi JOIN, agregasi, dan strategi
    pengindeksan yang dibutuhkan sistem
Fitur MySQL 8.0 yang Digunakan :
- _Window Functions_ untuk pelaporan dan analitik
- Tipe data JSON untuk fleksibilitas data semi-terstruktur
- _Common Table Expressions_ (CTE) untuk kueri kompleks
- Pencarian teks lengkap InnoDB
- Replikasi dan _binary logs_ untuk cadangan data
**_2.1.7. Tailwind CSS_**
_Tailwind CSS_ adalah _CSS framework_ yang memberikan tawaran konsep
baru dengan konsep utility awal dimana tidak perlu lagi memperpedulikan panjang
nama kelas untuk komponen HTML[33].
**2.1.8. Keamanan Web (** **_Web Security_** **)**
Keamanan merupakan hal yang paling mutlak yang harus dilakukan apabila
adanya pertukaran informasi di ranah publik. Keamanan Website adalah sebuah
aktivitas yang melindungi informasi dan data [34].


**2.2. Penelitian Terkait**
Beberapa penelitian terkait yang relevan dengan pengembangan Cur-Heart:
Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital telah dilakukan
sebelumnya. Penelitian-penelitian ini menjadi referensi dan landasan untuk
identifikasi dari proyek CUR-HEART.
**2.2.1. Penelitian tentang Sistem Informasi Kesehatan**
A. Penelitian 1 :
Judul Penelitian : Perancangan Sistem Informasi Pengaduan RSUD Dr.
Soedarsono Pasuruan Berbasis _Website_ Dengan Menggunakan Metode
_Waterfall_
Penulis : Nirma Dwi Wulansari, Gita Indah Marthasari, Briansyah Setio
Wiyono
Jurnal : REPOSITOR, Vol. 5, No. 3, Agustus 2023
Ringkasan Penelitian :
Penelitian ini merupakan pengembangan sistem informasi berbasis _website_
untuk pengaduan pelayanan di RSUD dr. R. Soedarsono Kota Pasuruan.
Pengaduan sebelumnya masih dilakukan secara manual, seperti _face to face_ atau
menggunakan kotak saran, yang dianggap tidak praktis.
Relevansi dengan Proyek CUR-HEART
Penelitian ini relevan sebagai studi pustaka karena :

1. Metodologi sama : Penelitian ini menggunakan metode Air Terjun
    ( _Waterfall_ ), yang memberikan referensi proses dan tahapan
    pengembangan yang sistematis dan sekuensial.
2. Sistem berbasis _Web_ di Sektor Kesehatan : Penelitian ini berfokus pada
    pengembangan sistem berbasis _website_ di lingkungan Rumah Sakit
    Umum, yang memberikan contoh implementasi teknologi informasi
    dalam pelayanan kesehatan.
3. Pengembangan Fitur Pengaduan/Saran Pasien : Meskipun fokus utama
    proyek CUR-HEART adalah terapi, penelitian ini menyediakan model
    fungsional untuk mengelola masukan dan umpan balik dari pengguna
    (pasien), yang dapat diadaptasi untuk fitur umpan balik klien terapi.


4. Pengguna Terpisah : Penelitian ini membagi akses dan peran yang jelas
    untuk berbagai hak akse seperti Kabid Pengembangan, Staf Pengaduan,
    Dokter, Staf Poli Klinik, dan Pasien, yang dapat menjadi model dalam
    merancang peran pengguna (admin, terapis, klien) dalam sistem terapi
    mental.
B. Penelitian 2 :
Judul Penelitian : Sistem Informasi Pelayanan Jasa Cuci dan _Custom_ Sepatu
Berbasis _Web_ (Studi Kasus: _Good and Beast Shoes_ )
Penulis : Farras Raihan Al-Ayyubi
Jurnal : Technologia, Vol 13, No. 1, Januari 2022
Ringkasan Penelitian
Penelitian ini bertujuan membuat sistem informasi pelayanan jasa cuci dan
_custom_ sepatu berbasis _web_ yang terkomputerisasi untuk usaha _Good and Beast
Shoes_. Sebelumnya, penyediaan informasi dan pemesanan masih dilakukan
secara manual melalui media sosial, _mouth to mouth_ pelanggan, _WhatsApp,_ dan
transaksi pembayaran tunai.
Tujuan utama dari sistem ini adalah mempermudah pengelolaan data,
menampilkan informasi, melakukan, dan menerima pemesanan, serta
mempermudah transaksi pembayaran secara _online_**.**
Hasil penelitian menunjukkan bahwa sistem dibuat menggunakan bahasa
pemrograman _PHP_ dengan basis data _MySQL_. Sistem yang dihasilkan dapat
membantu proses pemesanan, pengelolaan data, dan transaksi pembayaran,
sehingga lebih efektif dan mengurangi proses manual.
Relevansi dengan Proyek Anda
Penelitian ini memiliki relevansi meskipun berasal dari sektor non-kesehatan,
terutama dalam hal pengembangan sistem berbasis jasa layanan :
1. Sistem Pemesanan Jasa Berbasis _Web_ : Penelitian ini memberikan model
implementasi untuk layanan jasa (pemesanan layanan dan _custom_ sepatu)
Proses pemesanan layanan di sini memiliki kemiripan alur dengan pemesanan
layanan terapi: pemilihan layanan ( _fast clean_ - > jenis terapi).


2. Pengelolaan Status : Sistem ini mengelola status pemesanan (sudah dibayar ->
    diproses -> selesai), yang merupakan fitur penting untuk melacak status sesi
    terapi/layanan di sistem Anda.
C. Penelitian 3 :
    Judul Penelitian : Perancangan UI/UX Aplikasi Kesehatan Mental
Menggunakan Metode _Design Thinking_ Studi Kasus Mahasiswa Kost UHAMKA
Penulis : Irgieawan Rahmat Azhar, Nur Chalik Azhar
Jurnal : JATI (Jurnal Mahasiswa Teknik Informatika), Vol. 9 No. 3, Juni 2025
Ringkasan Penelitian
Penelitian ini bertujuan merancang prototipe antarmuka pengguna ( _UI/UX_ )
berbasis _mobile_ yang secara spesifik menargetkan kesehatan mental mahasiswa
kost. Populasi ini dianggap rentan karena pola hidup tidak sehat dan kesulitan
menjaga keseimbangan fisik dan mental.
Metode Pengembangan yang digunakan adalah _Design Thinking_. Tahapannya
meliputi _Empathize_ , _Define_ , _Ideate_ , _Prototype_ , dan _Test_.
Fitur Utama Prototipe yang dihasilkan meliputi :
- Layanan konsultasi _online_ dengan psikiater dan psikolog
- Edukasi kesehatan
- Ruang diskusi/komunitas untuk berbagi cerita
Kesimpulan penelitian menyatakan bahwa aplikasi ini berpotensi
meningkatkan aksesibilitas layanan kesehatan mental, mengatasi hambatan
finansial dan stigma.

Relevansi dengan Proyek CUR-HEART
Penelitian ini memiliki relevansi yang sangat tinggi dan komprehensif untuk sistem
CUR-HEART karena:

1. Fokus Kesehatan Mental & Konsultasi O _nline_ : Penelitian ini membahas
    langsung perancangan UI/UX untuk layanan konsultasi _online_ dari sistem
    terapi CUR-HEART.
2. Metodologi Alternatif : Penelitian ini menggunakan Design Thinking, yang
    merupakan pendekatan _human-centered_ dan dapat berfungsi sebagai
    alternatif atau pendukung metodologi _Waterfall_ (yang digunakan pada studi
    1 dan 2) untuk fase _discovery_ dan _design_ pada proyek CUR-HEART.


##### 24

##### BAB III

##### METODOLOGI PENELITIAN

**3.1 Tahapan Penelitan**
Penelitian dan pengembangan sistem informasi manajemen pemesanan dan
terapi CUR-HEART menggunakan pendekatan **_System Development Life
Cycle_** **(SDLC)** dengan model **_Waterfall_**. Model ini dipilih karena karakteristik
proyek yang memiliki kebutuhan jelas, waktu yang tetap (semester akademik), dan
memerlukan dokumentasi yang komprehensif untuk keperluan akademik. Tahapan
penelitian terdiri dari lima fase utama yang dilaksanakan secara berurutan dengan
keluaran yang terdefinisi jelas di setiap fase.

```
Inisiasi
Proyek
```
```
Perencanaan
Proyek
```
```
Pelaksanaan
Proyek
```
```
Pemantauan &
Pengendalian Proyek
```
```
Penutupan
Proyek
```
## Gambar III. 1 Tahapan Penelitian


Uraian tahapan penelitian sebagai berikut :

**1. Inisiasi Proyek**
    Tahapan ini dimulai dengan mengidentifikasi permasalahan yang dihadapi
CUR-HEART dalam manajemen pemesanan dan terapi, menentukan tujuan
proyek, mengidentifikasi pemangku kepentingan, serta menyusun _project charter_
sebagai dokumen otorisasi formal untuk memulai proyek.
**2. Perencanaan Proyek**
    Tahapan perencanaan mencakup penyusunan ruang lingkup proyek ( _scope_ ),
penjadwalan waktu pengerjaan ( _timeline_ ), estimasi anggaran biaya, perencanaan
kualitas, identifikasi sumber daya yang dibutuhkan, analisis risiko, perencanaan
komunikasi, dan strategi pengadaan ( _procurement_ ).
**3. Pelaksanaan Proyek**
    Tahapan pelaksanaan merupakan fase inti pengembangan sistem yang terdiri
    dari :
       a. Analisis kebutuhan sistem melalui observasi, wawancara, dan studi
          dokumentasi
       b. Perancangan sistem meliputi desain basis data, desain antarmuka pengguna,
          dan diagram UML
       c. Implementasi sistem menggunakan _framework Laravel_ dengan bahasa
          pemrograman PHP
       d. Pengujian sistem secara menyeluruh untuk memastikan kualitas dan
          kesesuaian dengan kebutuhan
       e. _Deployment_ sistem ke lingkungan produksi
**4. Pemantauan dan Pengendalian Proyek**
    Tahapan ini dilakukan paralel dengan pelaksanaan proyek untuk memastikan
proyek berjalan sesuai rencana. Aktivitas meliputi pemantauan progres pengerjaan,
pengendalian perubahan ruang lingkup, pengendalian kualitas _deliverables_ , dan
pengelolaan risiko yang muncul selama pengerjaan.
**5. Penutupan Proyek**
    Tahapan akhir mencakup serah terima sistem ( _handover_ ) kepada klien,
penyusunan dokumentasi lengkap (manual pengguna, dokumentasi teknis),


evaluasi pencapaian tujuan proyek, _lessons learned_ , dan pelepasan sumber daya tim
proyek.

**3.2. Tempat dan Waktu Penelitian
3.2.1. Tempat Penelitian**
Penelitian dan pengembangan CUR-HEART: Inovasi Sistem Informasi
Layanan Terapi Mental Berbasis Digital ini dilaksanakan di beberapa lokasi sebagai
berikut :

**1. CUR-HEART (** **_Hypnotherapy & Mind Wellness Center_** **)**
    a. Alamat : Jl. Raya Cilodong No. 88, Depok, Jawa Barat
    b. Kegiatan : Observasi proses bisnis, wawancara dengan pemangku
       kepentingan, dan pengujian penerimaan pengguna ( _User Acceptance_
       _Testing_ )
**2. Universitas Nusa Mandiri - Kampus Margonda**
    a. Alamat : Jl. Margonda Raya No. 100, Pondok Cina, Depok, Jawa Barat
    b. Kegiatan : Pengembangan sistem, konsultasi dengan dosen pembimbing,
       dan koordinasi tim proyek
**3. Secara Daring (** **_Remote/Online_** **)**
    a. Kegiatan: Pengembangan sistem, dokumentasi, pengujian, dan koordinasi
       tim melalui platform kolaborasi daring
**3.2.2. Waktu Penelitian**
Penelitian ini dilaksanakan selama satu semester akademik dengan rentang
waktu sebagai berikut :
**Tabel III. 1** Jadwal Penelitan
**No Kegiatan Waktu Pelaksanaan**

```
1 Inisiasi dan Analisis Kebutuhan Minggu 1-2 (16-29 September 202 5 )
```
```
2 Perancangan Sistem Minggu 3Oktober 202-4 (30 September 5 ) -^13
```

```
No Kegiatan Waktu Pelaksanaan
```
```
3 Implementasi Sistem Minggu 5November 202-8 (14 Oktober 5 ) -^10
```
```
4 Pengujian Sistem Minggu 9-10 (11-24 November 202 5 )
```
```
5 Deployment dan Evaluasi Minggu 11 (25 November Desember 202 5 ) -^1
```
```
6 Penyusunan Laporan Minggu 12-15 (2-29 Desember 202 5 )
```
**Total durasi penelitian adalah 15 minggu (16 September - 29 Desember 202 5 )**

**3.3. Subjek Penelitian**
Subjek penelitian dalam pengembangan CUR-HEART: Inovasi Sistem
Informasi Layanan Terapi Mental Berbasis Digital terdiri dari pemangku
kepentingan yang terlibat langsung dalam penggunaan sistem. Penelitian ini
menggunakan metode _sampling purposive (non-probabilitas)_ dimana partisipan
dipilih berdasarkan kriteria tertentu yang relevan dengan tujuan penelitian.
**3.3.1. Populasi**
Populasi dalam penelitian ini adalah seluruh pengguna potensial CUR-
HEART: Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital yang
terdiri dari :

1. Pemilik dan manajemen CUR-HEART
2. Terapis yang bekerja di CUR-HEART
3. Staf administrasi dan _customer service_
4. Klien yang menggunakan layanan terapi CUR-HEART
5. Calon klien potensial yang membutuhkan layanan terapi kesehatan mental
    **3.3.2. Sampel dan Teknik Pengambilan Sampel**
       Penelitian ini menggunakan teknik **_purposive_** **sampling** (pengambilan
sampel bertujuan) dimana sampel dipilih secara sengaja berdasarkan karakteristik
dan kriteria tertentu yang sesuai dengan kebutuhan penelitian.


## Tabel III. 2 Distribusi Sampel Penelitian

```
No Kategori Sampel Jumlah
```
```
Kriteria
Pemilihan
```
```
Peran dalam
Penelitian
```
##### 1

```
Pemilik/
Manajemen 1 orang^
```
```
Pengambil
keputusan,
memahami visi
bisnis
```
```
Memberikan
kebutuhan
bisnis,
validasi
sistem
```
```
2 Terapis 3 orang
```
```
Berpengalaman
minimal 1
tahun, pengguna
aktif sistem
```
```
Memberikan
kebutuhan
fungsional,
pengujian
sistem
```
```
3 Staf Admin/CS 2 orang
```
```
Mengelola
pemesanan dan
administrasi
harian
```
```
Memberikan
proses bisnis
existing ,
pengujian
```
```
4 Klien Aktif 5 orang
```
```
Pernah
menggunakan
layanan
minimal 2 kali
```
```
Memberikan
feedback
kebutuhan
klien, UAT
```
```
5 Calon Klien 3 orang
```
```
Berminat
menggunakan
layanan terapi
```
```
Pengujian
usability dari
perspektif
user baru
Total 14 orang
```
Teknik pengambilan sampel menggunakan **_purposive sampling_** dengan
pertimbangan :


1. Sampel dipilih berdasarkan pengetahuan dan pengalaman mereka terhadap
    proses bisnis CUR-HEART
2. Mewakili berbagai peran pengguna dalam sistem (admin, terapis, klien)
3. Dapat memberikan informasi yang mendalam dan relevan untuk
    pengembangan sistem
4. Bersedia berpartisipasi dalam wawancara, observasi, dan pengujian sistem

**3.4. Teknik Pengumpulan Data**
Pengumpulan data dalam penelitian ini menggunakan pendekatan _multi-
metode_ untuk memastikan pemahaman yang komprehensif terhadap kebutuhan
sistem dan validasi dari berbagai perspektif. Teknik pengumpulan data yang
digunakan meliputi observasi, wawancara, studi pustaka, dan kuesioner.
**3.4.1. Observasi**
Observasi dilakukan untuk memahami proses bisnis aktual yang berjalan di
CUR-HEART dan mengidentifikasi permasalahan yang terjadi dalam operasional
sehari-hari. Observasi dilakukan secara langsung di lokasi CUR-HEART dengan
mengamati:

1. Proses pemesanan layanan terapi melalui _WhatsApp_ dan telepon
2. Proses penjadwalan terapis dan manajemen waktu
3. Interaksi antara staf administrasi dengan klien
4. Proses pencatatan data klien dan dokumentasi sesi terapi
5. Proses pembayaran dan pembuatan laporan
    Hasil observasi didokumentasikan dalam catatan lapangan ( _field notes_ ) dan
digunakan sebagai dasar untuk menyusun diagram proses bisnis ( _as-is process_ )
yang menggambarkan kondisi sebelum implementasi sistem.
**3.4.2. Wawancara**
Wawancara semi-terstruktur dilakukan untuk mendapatkan informasi
mendalam dari pemangku kepentingan mengenai kebutuhan, harapan, dan kendala
yang dihadapi dalam sistem yang sedang berjalan. Wawancara dilakukan kepada :


## Tabel III. 3 Daftar Narasumber Wawancara

```
No Narasumber Jumlah Tujuan Wawancara
```
```
1 Pemilik CUR-
HEART
```
```
1 orang Memahami visi bisnis, target, dan
ekspektasi terhadap sistem
```
(^2) Terapis 2 orang
Mengidentifikasi kebutuhan untuk
manajemen jadwal dan dokumentasi
sesi terapi
(^3) Staf Admin/CS 1 orang Memahami proses pemesanan,
pembayaran, dan administrasi
(^4) Klien 2 orang Menggali pengalaman pemesanan dan
ekspektasi terhadap sistem online
Wawancara dilakukan dengan durasi 30-60 menit per narasumber dan
didokumentasikan dalam bentuk transkrip wawancara. Hasil wawancara dianalisis
untuk mengidentifikasi kebutuhan fungsional dan non-fungsional sistem.
**3.4.3. Studi Pustaka**
Studi pustaka dilakukan untuk membangun landasan teoritis dan memahami
_best practice_ dalam pengembangan sistem informasi sejenis. Sumber pustaka yang
digunakan meliputi :

1. Jurnal ilmiah tentang sistem informasi manajemen pelayanan kesehatan
2. Buku referensi tentang rekayasa perangkat lunak dan manajemen proyek
3. Dokumentasi teknis _framework Laravel_ dan teknologi terkait
4. Penelitian terdahulu tentang sistem pemesanan dan manajemen terapi
5. Standar dan regulasi terkait keamanan data kesehatan
    Studi pustaka menghasilkan tinjauan literatur yang disajikan dalam BAB II dan
menjadi dasar dalam perancangan dan pengembangan sistem.


```
3.4.4. Kuesioner
Kuesioner digunakan untuk mengumpulkan data kuantitatif dari sampel
yang lebih luas dan mengukur tingkat kepuasan serta kegunaan sistem. Kuesioner
dibagikan dalam dua tahap:
```
1. Kuesioner Analisis Kebutuhan
    a. Diberikan kepada calon pengguna sistem ( 5 responden)
    b. Bertujuan mengidentifikasi fitur yang dibutuhkan dan prioritasnya
    c. Mengukur kesiapan pengguna terhadap sistem digital
2. Kuesioner Evaluasi Sistem ( _System Usability Scale_ /SUS)
    a. Diberikan kepada partisipan pengujian setelah menggunakan sistem ( 5
       responden)
    b. Mengukur tingkat kegunaan sistem dengan metode SUS
    c. Mengidentifikasi area perbaikan untuk pengembangan selanjutnya
       Hasil kuesioner dianalisis secara deskriptif dan statistik untuk mendukung
pengambilan keputusan dalam pengembangan sistem.


##### 32

## BAB IV HASIL PENELITIAN DAN PEMBAHASAN

### 4.1. Inisiasi Proyek

Proyek pengembangan CUR-HEART: Inovasi Sistem Informasi Layanan
Terapi Mental Berbasis Digital diinisiasi berdasarkan kebutuhan untuk
mengoptimalkan operasional pusat layanan hipnoterapi dan kesehatan mental.
CUR-HEART ( _Hypnotherapy & Mind Wellness Center_ ) mengalami pertumbuhan
signifikan dalam jumlah klien dan terapis, namun sistem manual yang digunakan
menghambat efisiensi dan kualitas layanan.

#### 4.1.1. Latar Belakang Masalah

Berdasarkan observasi dan wawancara yang dilakukan pada September
2025 , teridentifikasi beberapa permasalahan utama :

1. Proses pemesanan manual melalui _WhatsApp_ dan telepon yang memakan
    waktu lama dan mengurangi tingkat konversi (hanya 60% dari pertanyaan
    menjadi pemesanan aktual)
2. Konflik jadwal dan pemesanan ganda terjadi 8-10 kasus per bulan karena
    manajemen jadwal menggunakan _spreadsheet_ terpisah
3. Dokumentasi terapi tidak terstruktur dimana terapis menghabiskan 15 menit
    per sesi untuk pencatatan manual dengan risiko data hilang
4. Tidak ada data untuk pengambilan keputusan karena informasi tersebar di
    berbagai platform dan pembuatan laporan memakan waktu 2-3 hari
5. Beban administratif tinggi dengan admin menghabiskan 70% waktu untuk
    tugas repetitif seperti menjawab pertanyaan yang sama dan verifikasi
    pembayaran manual
6. Risiko keamanan dan privasi data klien yang sensitif disimpan dalam format
    tidak aman tanpa kontrol akses yang tepat

#### 4.1.2. Identifikasi Masalah

Berdasarkan latar belakang di atas, penulis mengidentifikasikan beberapa
masalah sebagai berikut :
a. Pelayanan pemesanan terapi masih dilaksanakan secara konvensional sehingga
kurang efektif dan efisien


```
b. Belum adanya sistem informasi pemesanan berbasis web untuk pemesanan dan
manajemen terapi
c. Banyak terjadi kehilangan data klien karena belum adanya sistem informasi
yang dapat mendata siapa saja klien yang sedang melakukan pemesanan dan
mengikuti sesi terapi
```
#### 4 .1.3. Ruang Lingkup

Ruang lingkup proyek ini mencakup pengembangan sistem informasi
berbasis web dengan fitur-fitur utama :

1. Modul Pemesanan Online : Klien dapat melihat jadwal terapis, memilih
    layanan, dan melakukan pemesanan secara mandiri 24/7
2. Manajemen Jadwal Terapis : Sistem penjadwalan otomatis dengan deteksi
    konflik dan notifikasi
3. Dokumentasi Sesi Terapi : Platform digital untuk terapis mencatat dan
    mengakses riwayat terapi klien
4. Pembayaran Terintegrasi : Integrasi dengan _payment gateway_ Midtrans untuk
    pembayaran online
5. _Dashboard_ Admin : Panel kontrol untuk pemantauan pemesanan, terapis, dan
    laporan keuangan
6. Notifikasi Otomatis : Pengingat email untuk klien dan terapis tentang jadwal
    sesi

#### 4.1.4. Tujuan dan Manfaat Penelitian

```
A. Tujuan penelitian dalam capstone project ini adalah:
a. Agar pelayanan pemesanan terapi dapat berjalan dengan efektif dan
efisien
b. Sistem informasi pemesanan diharapkan dapat memudahkan klien
dalam melakukan pemesanan dan melihat riwayat terapi
c. Dengan adanya sistem informasi dapat memudahkan baik klien,
petugas admin, maupun terapis dalam pengelolaan data pemesanan dan
sesi terapi, sehingga semuanya dapat terkontrol dengan baik
d. Sebagai salah satu syarat kelulusan pada Program Studi Strata Satu (S1)
untuk Program Studi Sistem Informasi di Fakultas Teknologi Informasi
Universitas Nusa Mandiri
```

B. Manfaat penelitian :
Penelitian ini diharapkan memberikan manfaat bagi berbagai pihak :
a. Bagi CUR-HEART : Meningkatkan efisiensi operasional, mengurangi
kesalahan jadwal, dan mempercepat pertumbuhan bisnis
b. Bagi Klien : Kemudahan dalam pemesanan layanan terapi kapan saja tanpa
harus menghubungi admin
c. Bagi Terapis : Mengurangi beban administratif dan memudahkan akses
riwayat klien
d. Bagi Admin : Otomasi tugas repetitif sehingga dapat fokus pada layanan
pelanggan yang lebih berkualitas
e. Bagi Akademik : Sebagai referensi pengembangan sistem informasi sejenis
untuk layanan kesehatan mental

### 4.2. Perencanaan Proyek

```
Perencanaan proyek dilakukan untuk memastikan proyek berjalan sesuai
target waktu, biaya, dan kualitas yang ditetapkan. Perencanaan mencakup berbagai
area pengetahuan manajemen proyek yang telah diidentifikasi mencakup ruang
lingkup ( scope ), waktu ( time ), biaya ( cost ), kualitas ( quality ), sumber daya
( resource ), risiko ( risk ), komunikasi ( communication ), pengadaan ( procurement ),
integrasi ( integration ), serta manajemen pemangku kepentingan ( stakeholder ).
```
#### 4.2.1. Perencanaan Ruang Lingkup

```
Ruang lingkup proyek didefinisikan menggunakan Work Breakdown
Structure (WBS) yang membagi pekerjaan menjadi komponen-komponen yang
dapat dikelola. WBS proyek ini mencakup 6 fase utama dengan total lebih dari
40 work packages yang terdistribusi ke dalam aktivitas-aktivitas terstruktur.
```

## Tabel IV. 1 Work Breakdown Structure (WBS)

```
Level 1 Level 2 Level 3 Deskripsi
```
1. _Project
Management_

```
1.1 Inisiasi
```
##### 1.1.1

```
Identifikasi
Masalah
```
```
Observasi dan
wawancara pemangku
kepentingan
```
```
1.1.2 Studi
Kelayakan
```
```
Analisis kelayakan
teknis, operasional,
ekonomi
```
##### 1.2

```
Perencanaan
```
##### 1.2.1

```
Penyusunan
WBS
```
```
Rincian struktur
pekerjaan
```
```
1.2.2
Estimasi
Biaya
```
```
Perhitungan biaya
pengembangan
```
```
1.3
Monitoring
```
##### 1.3.1

```
Progress
Tracking
```
```
Pemantauan kemajuan
mingguan
```
2. Analysis

##### 2.1

```
Requirements
```
##### 2.1.1

```
Functional
Requiremen
ts
```
```
Identifikasi 40+
kebutuhan fungsional
```
```
2.1.2 Non-
functional
Requiremen
ts
```
```
Keamanan, kinerja,
kegunaan
```
```
2.2 System
Analysis
```
```
2.2.1 As-Is
Process
```
```
Dokumentasi proses
bisnis saat ini
2.2.2 To-Be
Process
```
```
Rancangan proses bisnis
baru
```
3. _Design_ 3.1 _DesignDatabase_

```
3.1.1 ERD Diagram relasi entitas 16 tabel
```
```
3.1.2
Normalisasi Normalisasi hingga 3NF^
```

```
Level 1 Level 2 Level 3 Deskripsi
```
##### 3.2 UI/UX

```
Design
```
##### 3.2.1

```
Wireframe
```
```
Sketsa antarmuka
pengguna
3.2.2
Mockup
```
```
Desain visual 41
halaman di Figma
```
##### 3.3 UML

```
Diagrams
```
```
3.3.1 Use
Case
Diagram
```
```
Diagram kasus
penggunaan
```
```
3.3.2
Activity
Diagram
```
```
Diagram aktivitas proses
bisnis
```
##### 4.

_Implementati
on_

```
4.1 Backend
```
##### 4.1.1

```
Laravel
Setup
```
```
Instalasi dan
konfigurasi framework
```
```
4.1.2
Database
Migration
```
```
Migrasi skema basis data
```
```
4.1.3 API
Developme
nt
```
```
Pengembangan controlle
r dan model
```
```
4.2 Frontend
```
```
4.2.1 Blade
Templates Pembuatan templat^ view^
4.2.2
Tailwind
Styling
```
```
Styling dengan Tailwind
CSS
```
```
4.3 Integration
```
##### 4.3.1

```
Payment
Gateway
```
```
Integrasi Midtrans
```
```
4.3.2 Email
Service
```
```
Konfigurasi notifikasi
email
```
5. _Testing_ 5.1 _TestingUnit_ 5.1.1 PHPUnit _Tests_^30 _test cases_


```
Level 1 Level 2 Level 3 Deskripsi
5.2 Integration
Testing
```
##### 5.2.1 API

```
Testing
```
```
Pengujian integrasi antar
modul
```
```
5.3 UAT 5.3.1 TestingUser Pengujian oleh pengguna akhir
```
##### 6.

```
Deployment
```
```
6.1 Server
Setup
```
##### 6.1.1 VPS

```
Configurati
on
```
```
Pengaturan Ubuntu,
Nginx, PHP, MySQL
```
```
6.1.2 SSL
Certificate Instalasi Let's Encrypt^
```
```
6.2 Go Live
```
##### 6.2.1

```
Database
Migration
```
```
Migrasi data ke produksi
```
```
6.2.2
System
Launch
```
```
Peluncuran sistem
```
**Gantt Chart :**
_Gantt Chart_ menampilkan jadwal proyek dalam bentuk diagram batang yang
menunjukkan tanggal mulai, durasi, dan tanggal selesai dari setiap aktivitas.


##### 38

```
Activity Week^
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20 21 22 23 24 25
```
_1. Requirements_
    _Analysis_
       a. _Observation_
       b. _Interview_
       c. _Documentation
2. System Design_
    a. _Database_
       _Design_
    b. _UI/UX Design_
    c. _UML_
       _Diagrams
3. Implementation_
    _a. Backend_
       _Development_
    _b. Frontend_
       _Development_
    c. _Integration_

## Tabel IV. 2 Gantt Chart


##### 39

_Activity_ (^) 1 2 3 4 5 6 7 8 9 10 11 12 13 _Week_ 14^ 15 16 18 19 20 21 22 23 24 25

_4. Testing_
    a. _Unit Testing_
    b. _Integration_
       _Testing_
    c. _Functional_
       _Testing_
    d. _UAT
5. Deployment_
    a. _Server Setup_
    b. _Migration_
    c. _Go Live
6. Documentation_
    a. _Report Writing_
    b. _Presentation_
       _Prep_


#### 4.2.2. Perencanaan Waktu Pengerjaan

Proyek dikerjakan selama 16 minggu (4 bulan) dengan pembagian waktu
sebagai berikut :

## Tabel IV. 3 Jadwal Pengerjaan Proyek

```
No Fase Durasi Periode Luaran
```
```
1 Analisis Kebutuhan 2 minggu 16202 - 29 Sep 5 Dokumen SRS, Studi Kelayakan
```
```
2 Desain
Sistem
```
```
2 minggu 30 Sep -^13
Okt 202 5
```
```
ERD, Diagram
UML, Mockup
UI/UX
```
```
3 Implementasi 4 minggu 14 Okt -^10
Nov 202 5
```
```
Aplikasi web 60+
halaman
```
```
4 Pengujian 2 minggu 11 - 24 Nov
2025
```
```
Laporan pengujian,
persetujuan UAT
```
```
5 Deployment 1 minggu 25 Nov -^1
Des 202 5
```
```
Sistem produksi
aktif
```
```
6 Dokumentasi 5 minggu
```
```
Paralel
dengan semua
fase
```
```
Laporan akhir,
manual, presentasi
```

#### 4.2.3. Perencanaan Anggaran Biaya

```
A. Estimasi biaya proyek menggunakan metode bottom-up berdasarkan WBS:
```
## Tabel IV. 4 Estimasi Biaya Proyek

**No Kategori Item Biaya (Rp)**

```
1 Project Management
```
```
Project Manager (16 minggu × Rp
750.000/minggu) 12.000.000^
Contingency Reserve (10%) 1.200.000
```
```
2 Hardware
```
```
Laptop Development (sudah ada) 0
VPS Hosting Cloud (1 tahun -
4vCPU, 8GB RAM) 3.600.000^
```
```
3 Software
```
```
Laravel Framework (gratis) 0
MySQL Database (gratis) 0
Domain .id & SSL (1 tahun) 350.000
Figma Pro (untuk UI/UX Design -
3 bulan) 450.000^
```
```
4 Development
```
```
Backend Developer (8 minggu ×
Rp 2.500.000/minggu) 20.000.000^
Frontend Developer (8 minggu ×
Rp 2.200.000/minggu) 17.600.000^
Full-stack Developer (8 minggu ×
Rp 2.500.000/minggu) 20.000.000^
```
```
5 Testing
```
```
Testing Tools & QA (PHPUnit,
Selenium) 500.000^
UAT Sessions & User Testing (5
sesi) 1.500.000^
Security Audit & Penetration
Testing 2.500.000^
```
```
6 Training User Training Materials & Documentation 800.000
```

```
No Kategori Item Biaya (Rp)
```
```
Training Sessions (Admin,
Terapis, Klien) 1.200.000^
```
```
7 Integration
```
```
Payment Gateway Setup
(Midtrans) 500.000^
Email Service Setup
(SMTP/SendGrid) 300.000^
```
```
8 Lain-lain
```
```
Dokumentasi Teknis & User
Manual 1.000.000^
Transport & Koordinasi 800.000
Komunikasi & Meeting Tools 500.000
TOTAL 86.800.000
```
```
Catatan Biaya:
```
1. Biaya tenaga kerja disesuaikan dengan standar pasar 2025 untuk developer
    profesional
2. _Project Manager_ : Rp 750.000/minggu (setara Rp 3 juta/bulan)
3. _Backend/Full-stack Developer_ : Rp 2.500.000/minggu (setara Rp 10
    juta/bulan)
4. _Frontend Developer_ : Rp 2.200.000/minggu (setara Rp 8,8 juta/bulan)
5. VPS Cloud dengan spesifikasi memadai untuk production (4vCPU, 8GB
    RAM, 160GB SSD)
6. Termasuk biaya _security audit_ dan _penetration testing_ untuk keamanan data
    klien
B. Estimasi Biaya Berulang Tahunan (Biaya Operasional) **:**

## Tabel IV. 5 Estimasi Biaya Operasional Tahunan

```
No Item Biaya/Tahun (Rp)
```
```
1
```
```
VPS Hosting Cloud (4vCPU, 8GB
RAM) 3.600.000^
```

**No Item Biaya/Tahun (Rp)**

2 _Domain & SSL renewal_ 350.000

3 _Payment Gateway Fee (2,9% + Rp
2.000 per transaksi)_

```
~8.400.000 (estimasi 120
transaksi/bulan)
```
4 _Email Service (SendGrid/SMTP)_ 600.000

5 _Backup & Storage (Cloud Backup)_ 1.200.000

6 _Monitoring & Security Tools_ 1.500.000

7 Pemeliharaan & Dukungan Teknis 6.000.000

8 _Software Updates & Patches_ 1.200.000

```
TOTAL 22.850.000
```
#### 4.2.4. Perencanaan Kualitas

```
Standar kualitas yang ditetapkan untuk proyek ini:
A. Standar Kualitas Fungsional :
```
1. Fungsionalitas : Minimal 90% kebutuhan fungsional harus terpenuhi
    dan berfungsi dengan baik
2. Akurasi : 100% akurasi dalam perhitungan pembayaran, penjadwalan,
    dan pelaporan
3. Kelengkapan : Semua modul utama (pemesanan, pembayaran, dasbor)
    harus tersedia
4. Interoperabilitas : Integrasi Midtrans dan layanan email berfungsi tanpa
    galat
B. Standar Kualitas Non-Fungsional :
1. Performa :
a) Waktu muat halaman < 2 detik (rata-rata)
b) Waktu respons API < 500ms untuk 95% permintaan
c) Waktu kueri basis data < 100ms (rata-rata)


2. Keamanan :
    a) Mitigasi kerentanan OWASP Top 10
    b) _Hashing_ kata sandi dengan _bcrypt_
    c) HTTPS untuk semua komunikasi
    d) Pencegahan _SQL injection_ ( _Eloquent ORM_ )
3. Usabilitas :
    a) Skor _System Usability Scale_ (SUS) minimal 70/100
    b) Tingkat kepuasan pengguna minimal 4/5
    c) Tingkat penyelesaian tugas ≥ 90%
4. Keandalan :
    a) Waktu aktif minimal 99% (maksimal waktu mati 7,2 jam/bulan)
    b) Waktu Rata-rata Antar Kegagalan ( _Mean Time Between_
       _Failures_ /MTBF) > 720 jam
    c) Tujuan Waktu Pemulihan ( _Recovery Time Objective_ /RTO) < 4 jam
5. Kemudahan Pemeliharaan :
    a) Cakupan pengujian kode minimal 70%
    b) Skor kualitas kode (CodeClimate) ≥ B
    c) Dokumentasi lengkap ( _inline comments_ , README, dokumentasi
       API)

#### 4.2.5. Perencanaan Sumber Daya

```
A. Sumber Daya Manusia :
```
## Tabel IV. 6 Alokasi Sumber Daya Manusia

**No Nama Peran Tanggung Jawab Alokasi
Waktu**

1 Roki Anjas (11250066)

```
Project
Manager &
Backend
Developer
```
```
Koordinasi tim,
pengembangan
backend ,
dokumentasi
```
##### 40

```
jam/minggu
```
2 Susanto
(11250068)

```
Frontend
Developer &
```
```
Desain
antarmuka,
```
##### 35

```
jam/minggu
```

**No Nama Peran Tanggung Jawab Alokasi Waktu**

```
UI/UX
Designer
```
```
pengembangan
frontend
```
##### 3

```
Fahruroji
(11250085)
```
```
Full-stack
Developer &
Database
Architect
```
```
Desain database,
pengembangan
full-stack ,
deployment
```
##### 35

```
jam/minggu
```
```
B. Sumber Daya Teknologi :
```
1. Perangkat Keras Pengembangan :
    a) Laptop/PC untuk pengembangan (3 unit - milik tim)
    b) VPS Ubuntu 22.04 LTS untuk server produksi
    c) Spesifikasi VPS: 4 vCPU, 8GB RAM, 160GB SSD
2. Perangkat Lunak Pengembangan :
    a) IDE: _Visual Studio Code_ (gratis)
    b) Kontrol Versi: Git & GitHub (gratis)
    c) Desain: Figma ( _free tier_ )
    d) _Framework_ : Laravel 10 ( _open source_ )
    e) Basis Data: MySQL 8.0 ( _open source_ )
    f) _Framework_ CSS: Tailwind CSS ( _open source_ )
C. Sumber Daya Infrastruktur :
1. Domain & Sertifikat SSL
2. Layanan email (SMTP)
3. Akun _payment gateway_ (Midtrans)


##### 46

**4.2.6. Manajemen Risiko (** **_Risk_** **)**
Identifikasi, analisis, dan strategi mitigasi risiko proyek :

## Tabel IV. 7 Identifikasi dan Mitigasi Risiko

```
No Risiko Probabilitas Dampak Skor Risiko Mitigasi Owner
```
```
1 Keterlambatan Jadwal Sedang Tinggi 12 Waktu penyangga 10%, dengan MoSCoW, daily standup^ prioritas fitur PM
```
##### 2

```
Scope
creep (perubahan
kebutuhan)
```
```
Sedang Tinggi 12
```
```
Dokumentasi kebutuhan yang jelas,
proses kontrol perubahan, persetujuan
formal
```
##### PM

```
3 Bug kritis
saat deployment
```
```
Rendah Tinggi 6 Pengujian menyeluruh,^ staging
environment , rencana rollback
```
```
Tim Dev
```
```
4 Anggota tim
sakit/tidak tersedia
```
```
Rendah Sedang 4 Berbagi pengetahuan, dokumentasi
kode, pair programming
```
##### PM

```
5 Integrasi^ payment
gateway gagal
```
```
Sedang Sedang 6 Prototyping^ awal, dokumentasi API
lengkap, pengujian sandbox
```
```
Backend
Dev
```

##### 47

```
No Risiko Probabilitas Dampak Skor Risiko Mitigasi Owner
```
```
6 Kehilangan data Rendah Tinggi 6
```
```
Cadangan otomatis harian, retensi 30
hari, rencana pemulihan bencana
```
##### DB

```
Architect
```
```
7 Pelanggaran keamanan Rendah Sangat Tinggi 8
```
```
Audit keamanan, penetration testing ,
mengikuti pedoman
OWASP
```
```
Tim Dev
```
```
8 Masalah kinerja Sedang Sedang 6
```
```
Load testing , database indexing ,
strategi caching
```
```
Full-
stack
Dev
```
**Catatan Skor Risiko :**

1. Probabilitas : Rendah (1), Sedang (2), Tinggi (3)
2. Dampak : Rendah (2), Sedang (4), Tinggi (6), Sangat Tinggi (8)
3. Skor Risiko = Probabilitas × Dampak


##### 48

**4.2.7. Perencanaan Komunikasi (** **_Communication_** **)**
Strategi komunikasi untuk memastikan informasi mengalir dengan efektif kepada seluruh pemangku kepentingan proyek.

## Tabel IV. 8 Matriks Perencanaan Komunikasi

```
No
```
```
Jenis
Komunikasi
```
```
Pemangku
Kepentingan Frekuensi^ Media^ Durasi^ Tujuan^
A. KOMUNIKASI INTERNAL TIM
```
```
1 Daily Standup Tim Proyek (3 orang) Harian (Pagi) WhatsApp Group 15 menit Update progress identifikasi blocker^ harian,
```
```
2 Weekly Team Meeting Tim Proyek (3 orang) Mingguan (Senin 19.00) Google Meet 1 - 2 jam
```
```
Review progress , demo fitur,
planning minggu depan, risk
review
```
```
3 Code Review Developer Setiap^ Pull
Request
```
```
GitHub Sesuai
kebutuhan
```
```
Jaminan kualitas kode,
knowledge sharing
B. KOMUNIKASI PEMANGKU KEPENTINGAN
```

##### 49

**No**

```
Jenis
Komunikasi
```
```
Pemangku
Kepentingan Frekuensi^ Media^ Durasi^ Tujuan^
```
4

```
Laporan
Kemajuan
```
```
Dosen
Pembimbing Dua mingguan^
```
```
Email +
Pertemuan 30 - 60 menit^
```
```
Update progress , konsultasi
masalah, approval milestone
```
5 Pertemuan
Klien

```
Pemilik CUR-
HEART
```
```
Dua mingguan Google Meet^ /
Tatap Muka
```
```
1 - 2 jam Validasi kebutuhan, demo
progress, feedback
```
6 Sesi UAT Pengguna CUR-
HEART

```
3 kali (Fase
Testing )
```
```
Tatap Muka 2 - 3 jam Pengujian sistem,
pengumpulan feedback
```
**C. DOKUMENTASI & KOLABORASI**

7 Dokumentasi
Proyek

```
Tim &
Stakeholder
```
```
Berkelanjutan Google Drive - Repositori dokumen
(laporan, SOP, manual)
```
8 Dokumentasi
Teknis

```
Developer Berkelanjutan GitHub Wiki - Dokumentasi API, arsitektur,
deployment
```
9 _Knowledge
Base_

```
Tim Proyek Berkelanjutan Notion - Catatan meeting, keputusan,
lessons learned
```

##### 50

```
No
```
```
Jenis
Komunikasi
```
```
Pemangku
Kepentingan Frekuensi^ Media^ Durasi^ Tujuan^
```
```
10
```
```
Kolaborasi
Desain
```
```
Designer &
Developer
```
```
Sesuai
kebutuhan Figma^ -^
```
```
Review dan approval desain
UI/UX
```
Alat Komunikasi yang Digunakan :

1. _WhatsApp_ : Komunikasi cepat dan koordinasi harian
2. _Google Meet_ : Pertemuan virtual dan presentasi
3. _Email_ : Komunikasi formal dan laporan resmi
4. _GitHub_ : Kolaborasi kode dan _code review_
5. _Figma_ : Kolaborasi desain _UI/UX_
6. _Google Drive_ : Penyimpanan dan berbagi dokumen
7. _Notion_ : Manajemen pengetahuan dan catatan


**4.2.8. Perencanaan Pengadaan (** **_Procurement_** **)**
Pengadaan barang dan jasa yang diperlukan :

## Tabel IV. 9 Daftar Pengadaan

```
NO Item Vendor Biaya Waktu PIC
```
```
1 VPS
Hosting
```
```
Niagahost
er
```
```
Rp
1.200.000/tahun
```
```
Minggu 8 Fahru
roji
```
```
2 Domain .id Niagahost
er
```
```
Rp
150.000/tahun
```
```
Minggu 8 Fahru
roji
```
```
3 SSL
Certificate
```
```
Let's
Encrypt
```
```
Gratis Minggu 8 Fahru
roji
```
```
4 Payment
Gateway
```
```
Midtrans
```
```
Gratis (dev),
2,9% + Rp
2.000 (prod)
```
```
Minggu 6 Roki
```
```
5 Email Service
```
```
Gmail
SMTP /
SendGrid
```
```
Gratis ( limited) Minggu 7 Roki
```
```
Proses Pengadaan :
```
1. Identifikasi kebutuhan
2. Pemilihan & perbandingan vendor
3. Persetujuan dari sponsor
4. _Purchase order_
5. Pengiriman & verifikasi
6. Pembayaran
7. Dokumentasi
**4.2.9. Perencanaan Integrasi (** **_Integration_** **)**
Integrasi sistem dengan layanan eksternal :
A. Integrasi _Payment Gateway_ (Midtrans) :
    1. Metode : _Snap API_ untuk _checkout_ yang mulus


2. Metode Pembayaran : Kartu kredit/debit, Transfer bank, Dompet digital
    (GoPay, OVO, Dana)
3. Keamanan : Memenuhi _PCI-DSS_ , dukungan _3D Secure_
4. _Webhook_ : Untuk notifikasi pembayaran waktu nyata
5. Waktu : Minggu 6-7 (implementasi + pengujian)
B. Integrasi Layanan Email :
1. Penyedia : Gmail SMTP / _SendGrid_
2. Kasus Penggunaan :
a. Email selamat datang saat registrasi
b. Email verifikasi
c. Konfirmasi pemesanan
d. Notifikasi pembayaran
e. Pengingat sesi (H-1, H-0)
f. Reset kata sandi
3. Waktu : Minggu 7- 8
C. Integrasi Masa Depan (Fase 2) :
1. Notifikasi SMS via _Twilio_
2. Penyimpanan _cloud_ ( _Google Drive_ / AWS S3)
3. Konferensi video ( _Zoom API_ )
4. _Analytics_ ( _Google Analytics_ )


##### 53

**4.2.10. Manajemen Pemangku Kepentingan (** **_Stakeholder_** **)**
Identifikasi dan strategi keterlibatan pemangku kepentingan:

## Tabel IV. 10 Daftar Pemangku Kepentingan

```
No
```
```
Pemangku
Kepentingan Peran^ Kepentingan^ Kekuasaan^ Minat^ Strategi^
```
```
1 Pemilik CURHEART -
```
```
Sponsor
&
Pengambil
Keputusan
```
```
Sangat Tinggi Tinggi Tinggi Kelola Erat: Presentasi kemajuan bulanan, persetujuan kebutuhan
```
```
2 Terapis (3 orang)
```
```
Pengguna
Akhir Tinggi^ Sedang^ Tinggi^
```
```
Tetap Berinformasi: Lokakarya
kebutuhan, UAT, pelatihan
```
```
3 Admin (2 orang)
```
```
Pengguna
Akhir Tinggi^ Sedang^ Tinggi^
```
```
Tetap Berinformasi: Lokakarya
kebutuhan, UAT, pelatihan
```

##### 54

```
No Pemangku
Kepentingan
```
```
Peran Kepentingan Kekuasaan Minat Strategi
```
```
4 Klien (8 orang sample) Pengguna Akhir Sedang Rendah Sedang Pantau: Survei kebutuhan, pengujian kegunaan
```
```
5 Dosen Pembimbing Penasihat Akademik Sangat Tinggi Tinggi Tinggi Kelola Erat: Konsultasi mingguan, tinjauan dokumen
```
```
6 Tim Pengembang
```
```
Tim
Pengemba
ngan
```
```
Sangat Tinggi Tinggi Tinggi Kelola Erat:^ Daily standup ,
pertemuan mingguan
```
Strategi Keterlibatan :

1. Kelola Erat : Kekuasaan tinggi, minat tinggi - keterlibatan intensif dan pembaruan berkala
2. Tetap Berinformasi : Kekuasaan rendah, minat tinggi - informasi berkala, masukan didengarkan
3. Jaga Kepuasan : Kekuasaan tinggi, minat rendah - pembaruan penting, minta persetujuan
4. Pantau : Kekuasaan rendah, minat rendah - komunikasi minimal, pemantauan


#### 4.2.11. Batasan Proyek

```
Batasan-batasan proyek yang telah disepakati:
A. Batasan Waktu :
```
1. Fokus proyek pada pembangunan sistem informasi dalam kurun waktu
    16 minggu (4 bulan)
2. Tidak membahas kontrol kualitas & jaminan kualitas secara khusus
    (hanya pengujian standar)
3. Evaluasi jangka panjang (> 6 bulan) tidak termasuk dalam ruang
    lingkup
B. Batasan Fitur :
1. Tidak membahas mengenai risiko proyek secara mendalam, fokus
hanya pada risiko permintaan perubahan
2. Modul analitik dan pelaporan dibatasi pada laporan standar (analitik
lanjutan/ _BI_ ditunda ke fase 2)
3. Integrasi dengan sistem eksternal lain (selain Midtrans dan email) tidak
termasuk dalam fase 1
C. Batasan Biaya :
1. Biaya yang dimaksud adalah biaya untuk tim proyek (tidak termasuk
manajer proyek senior eksternal)
2. Anggaran terbatas pada pengembangan dan 1 tahun operasional awal
3. Biaya pelatihan intensif untuk semua staf tidak termasuk (hanya
pelatihan dasar 2 jam)
D. Batasan Teknis :
1. Sistem dioptimalkan untuk desktop dan tablet, dukungan mobile dalam
bentuk _responsive design_ (bukan aplikasi mobile _native_ )
2. Kapasitas sistem didesain untuk menangani hingga 50 pengguna
bersamaan
3. Bahasa sistem: Bahasa Indonesia (multi-bahasa tidak termasuk fase 1)
4. Sistem tidak termasuk fitur panggilan video untuk sesi terapi daring
E. Batasan Data :
1. Migrasi data historis dibatasi pada data 6 bulan terakhir


2. Retensi cadangan data: 30 hari (untuk cadangan jangka panjang
    memerlukan biaya tambahan)
F. Batasan Hukum :
1. Sistem mengikuti prinsip dasar UU Perlindungan Data Pribadi, namun
sertifikasi kepatuhan formal tidak termasuk
2. Penyangkalan medis : Sistem untuk manajemen administrasi, bukan
untuk diagnosis medis

#### 4.2.12. Asumsi Proyek

```
Asumsi-asumsi yang mendasari perencanaan proyek :
A. Asumsi Pengadaan :
```
1. Pengadaan sudah tidak ada masalah, sumber daya non-personil tersedia
    sesuai spesifikasi
2. VPS hosting dapat disewa sesuai spesifikasi yang dibutuhkan
3. Domain dapat dibeli dan dikonfigurasi dengan lancar
B. Asumsi Sumber Daya Manusia :
1. Sumber daya manusia sudah tersedia sesuai dengan spesifikasi proyek
2. Anggota tim adalah SDM profesional (mahasiswa dengan kompetensi
memadai)
3. Tidak ada anggota tim yang mengundurkan diri atau sakit
berkepanjangan selama proyek
4. Terapis dan admin CUR-HEART bersedia meluangkan waktu untuk
lokakarya, UAT, dan pelatihan
C. Asumsi Teknis :
1. Manajer proyek adalah personil dari dalam tim (ketua tim mahasiswa)
2. Infrastruktur teknologi (internet, listrik) stabil di lokasi pengembangan
dan CUR-HEART
3. API Midtrans berfungsi stabil dengan dokumentasi lengkap
4. Layanan email SMTP dapat dikonfigurasi tanpa hambatan
D. Asumsi Organisasi :
1. Struktur organisasi CUR-HEART sudah diterapkan dengan baik
2. Pemilik & manajer proyek sudah ditunjuk beserta anggota tim


3. Persetujuan dan pengambilan keputusan dari pemangku kepentingan
    dapat dilakukan tepat waktu
4. Tidak ada perubahan manajemen atau struktur organisasi selama
    proyek
E. Asumsi Proses Bisnis :
1. Proses bisnis CUR-HEART yang ada saat ini sudah terdokumentasi
dengan baik
2. Pemangku kepentingan dapat mengartikulasikan kebutuhan mereka
dengan jelas
3. Tidak ada perubahan signifikan pada proses bisnis selama
pengembangan
F. Asumsi Pengguna :
1. Klien CUR-HEART memiliki akses internet dan perangkat
(smartphone/laptop/tablet)
2. Pengguna memiliki kemampuan dasar menggunakan teknologi digital
3. Klien bersedia mengadopsi sistem online untuk pemesanan
G. Asumsi Regulasi :
1. Tidak ada perubahan regulasi terkait data pribadi atau layanan
kesehatan mental selama proyek
2. Bisnis CUR-HEART memiliki izin operasional yang legal

### 4.3. Deskripsi Produk / Servis

Berikut ini adalah deskripsi umum ( _high-level_ ) mengenai produk atau layanan
yang dihasilkan dari proyek ini :

#### 4.3.1. Tujuan Proyek

Tujuan proyek ini adalah membangun sistem informasi berbasis web yang
dapat memberikan informasi yang berkaitan dengan manajemen pemesanan dan
terapi hipnoterapi CUR-HEART, mencakup :

1. Informasi lengkap tentang layanan terapi yang ditawarkan
2. Profil terapis dengan spesialisasi dan jadwal ketersediaan
3. Sistem pemesanan online yang mudah dan cepat
4. Manajemen sesi terapi dan dokumentasi klien


5. Pembayaran online yang aman dan terintegrasi
6. Dasbor analitik untuk pengambilan keputusan

#### 4.3.2. Pengguna Sistem

Sistem ini memiliki 3 tipe pengguna utama dengan hak akses berbeda.
Sistem yang dibangun harus mampu :
A. Untuk Klien :

1. Menampilkan informasi jumlah layanan, terapis, dan testimoni
2. Menampilkan informasi layanan terbaru dan terapis unggulan
3. Memberikan kemampuan pemesanan layanan secara online 24/7
4. Menampilkan riwayat pemesanan dan sesi terapi
5. Menyediakan sistem pembayaran yang aman dan mudah
6. Menampilkan kemajuan terapi dan catatan sesi (yang dibagikan)
B. Untuk Terapis :
1. Manajemen jadwal dan ketersediaan secara mandiri
2. Melihat daftar klien dan detail pemesanan hari ini
3. Mendokumentasikan sesi terapi dengan formulir terstruktur
4. Mengakses riwayat lengkap klien untuk kontinuitas perawatan
5. Melihat dasbor pendapatan dan statistik kinerja
6. Memperbarui profil dan pengaturan notifikasi
C. Untuk Admin :
1. Pemantauan pemesanan waktu nyata dengan pelacakan status
2. Manajemen pengguna (klien, terapis, admin)in)
3. Manajemen layanan (operasi CRUD)
4. Laporan keuangan dan analitik :
a) Total pemesanan dan pendapatan
b) Rincian per layanan dan terapis
c) Trend pemesanan bulanan
5. Approval dan verifikasi terapis baru
6. System settings dan configuration

#### 4.3.3. Fitur Utama Sistem

```
A. Modul Public Website
```
1. _Landing page_ dengan informasi bisnis


2. Katalog layanan terapi lengkap dengan deskripsi
3. Direktori terapis dengan profil dan rating
4. Blog/artikel tentang kesehatan mental
5. FAQ dan halaman bantuan
6. Formulir kontak
B. Modul Autentikasi
1. Autentikasi multi-peran (Klien, Terapis, Admin)
2. Registrasi dengan validasi email
3. _Login_ dengan fitur ingat saya
4. Lupa kata sandi & atur ulang kata sandi
5. _Social login_ ( _Google, Facebook_ ) - opsional
C. Modul Pemesanan
1. _Wizard_ pemesanan 4 langkah:
a) Pilih layanan terapi
b) Pilih terapis (atau penugasan otomatis)
c) Pilih tanggal & waktu
d) Konfirmasi & pembayaran
2. Pengecekan ketersediaan waktu nyatayata
3. Tipe sesi: Daring/ _Online_ /Luring/ _Offline_
4. Dukungan kode promo
5. Email konfirmasi pemesanan
D. Modul Pembayaran
1. Integrasi _payment gateway_ Midtrans
2. Beragam metode pembayaran :
a) Kartu kredit/debit
b) Transfer bank
c) Dompet digital (GoPay, OVO, Dana) Dana)
3. Verifikasi pembayaran otomatis
4. Pembuatan faktur (PDF)
5. Riwayat pembayaran dan pelacakan status
E. Modul Dasbor Klien
1. Ikhtisar : Sesi mendatang, sesi selesai, total jam


2. Janji Temu Saya: Daftar, detail, jadwal ulang, batalkan
3. Pelacakan Kemajuan : Grafik visual dan metrik
4. Pesan : Obrolan dengan terapis
5. Profile & settings
F. Modul Dasbor Terapis
1. Jadwal hari ini dengan hitungan mundur
2. Daftar klien dan detail
3. Formulir dokumentasi sesi dengan _rich text editor_
4. Riwayat sesi dan arsip catatan
5. Pengaturan ketersediaan (jam kerja, waktu libur)
6. Dasbor pendapatan
7. Manajemen profil
G. Modul Dasbor Admin
1. Kartu statistic : Pengguna, pemesanan, pendapatan, kesehatan sistem
2. Grafik : Tren pendapatan, pertumbuhan pengguna, layanan
teratasayanan teratas
3. Manajemen pengguna (CRUD, menyetujui terapis)
4. Manajemen pemesanan (lihat, edit, batalkan, pengembalian dana)
5. Manajemen layanan (CRUD)
6. Laporan keuangan ( _ekspor Excel_ /PDF)
7. Pengaturan sistem
H. Modul Notifikasi
1. Notifikasi email :
a) Konfirmasi pemesanan
b) Pembayaran berhasil
c) Pengingat sesi (H-1, H-0)
d) Notifikasi pembatalan
2. Notifikasi dalam aplikasi
3. Pengingat SMS (pengembangan mendatang)
I. Modul Pelaporan
1. Laporan pemesanan : Harian, mingguan, bulanan
2. Laporan pendapatan : Per layanan, per terapis


3. Laporan aktivitas pengguna
4. Format _ekspor_ : PDF, _Excel_ , CSV

#### 4.3.4. Arsitektur Sistem

Sistem dibangun dengan arsitektur **MVC (** **_Model-View-
Controller_** **)** menggunakan _framework_ Laravel :

```
LAPISAN PRESANTASI
( Views – Blade Templates + Tailwind CSS)
```
- _Halaman public_
- _Dasbor klien_
- _Dasbor terapis_
- _Dasbor admin_

##### LAPISAN APLIKASI

```
( Controllers + Middleware)
```
- _AuthController_
- _BookingController_
- _PaymentController_
- _DasboardController_
- _AdminController_

##### LAPISAN LOGIKA BISNIS

```
(Models + Services + Events)
```
- _Model User, Therapist, Client_
- _Model Service, Booking, Payment_
- _Model Session, Review_
- Aturan bisnis & Validasi

##### LAPISAN AKSES DATA

```
( Eloquent ORM + MySQL Database )
```
- 16 tabel ternomalisasi (3NF)
- _Migrations & senders_
- _Relationships & constraints_

## Gambar IV. 1 Framework Laravel


#### 4.3.5. Desain Basis Data

```
Sistem menggunakan 16 tabel utama :
```
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
    Normalisasi : **Third Normal Form (3NF)** untuk menghindari redundansi
dan anomali data.

#### 4.3.6. Peran dan Hak Akses Pengguna

```
A. Tamu
```
1. Lihat: Halaman utama, layanan, terapis, blog
2. Aksi: Registrasi, login, kontak
B. Klien
1. Lihat: Semua izin tamu + dasbor, pemesanan, kemajuan, pesan
2. Aksi: Pesan layanan, lakukan pembayaran, jadwal ulang/batalkan, beri
ulasan, obrolan
C. Terapis
1. Lihat: Dasbor, jadwal, klien, sesi, pendapatan
2. Aksi: Atur ketersediaan, dokumentasi sesi, lihat riwayat klien, obrolan,
perbarui profil


```
D. Administrator
```
1. Lihat: Semua data (pengguna, pemesanan, pembayaran, laporan)
2. Aksi: CRUD penuh pada semua sumber daya, menyetujui terapis,
    membuat laporan, pengaturan sistem

#### 4.3.7. Keamanan Sistem

```
A. Autentikasi & Otorisasi
```
1. _Hashing_ kata sandi dengan _bcrypt_
2. Manajemen sesi dengan Laravel
3. Perlindungan CSRF untuk semua formulir
4. Kontrol akses berbasis peran ( _Role-Based Access Control_ /RBAC)
B. Keamanan Data
1. HTTPS untuk semua komunikasi
2. Pencegahan _SQL injection_ (Eloquent ORM)
3. Pencegahan XSS ( _Blade escaping_ )
4. Enkripsi untuk data sensitif (rekam medis)
C. Keamanan Pembayaran
1. Sesuai PCI-DSS (melalui Midtrans)
2. Tidak ada data kartu kredit disimpan secara lokal
3. Dukungan 3D Secure
D. Kepatuhan
1. UU Perlindungan Data Pribadi (UU PDP)
2. Arsitektur siap GDPR
3. Kebijakan retensi data (cadangan 30 hari)

#### 4.3.8. Kinerja dan Skalabilitas

```
A. Optimasi Kinerja
```
1. Pengindeksan basis data pada kueri yang sering digunakan
2. _Caching_ Laravel ( _config_ , _route_ , _view cache_ )
3. _Lazy loading_ untuk relasi Eloquent
4. CDN untuk aset statis (pengembangan mendatang)
B. Skalabilitas
1. Siap penskalaan horizontal ( _load balancer_ + beberapa server)
2. Replikasi basis data ( _master-slave_ )


3. Pekerja antrian untuk pekerjaan latar belakang
4. Sesi tanpa keadaan (siap untuk _clustering_ )
Target Metrik :
1. Waktu muat halaman: < 2 detik
2. Pengguna bersamaan: 100+
3. Waktu aktif: ≥ 99,5%
4. Waktu kueri basis data: < 100ms (rata-rata)


#### 4.3.9. Pelaksanaan Proyek

Pelaksanaan proyek merupakan fase implementasi dari perencanaan yang
telah dibuat. Pada fase ini dilakukan desain sistem yang mencakup perancangan
basis data, pemodelan UML, dan desain antarmuka pengguna.
**_4.3.9.1.Use Case Diagram_**
_Use Case_ Diagram menggambarkan interaksi antara aktor (pengguna)
dengan sistem, serta fungsionalitas yang dapat dilakukan oleh masing-masing aktor.

## Gambar IV. 2 Use Case Diagram Sistem Informasi CUR-HEART


**Aktor dalam Sistem :**

1. **Tamu** - Pengunjung situs web yang belum masuk
2. **Klien** - Pengguna terdaftar yang menggunakan layanan terapi
3. **Terapis** - Praktisi hipnoterapi yang memberikan layanan
4. **Admin** - Administrator sistem yang mengelola seluruh sistem
5. **_Payment Gateway_** - Sistem eksternal untuk pemrosesan pembayaran
**_Use Cases_** **Utama :
Untuk Tamu :**
1. Melihat halaman beranda
2. Melihat daftar layanan terapi
3. Melihat profil terapis
4. Registrasi akun baru
5. Masuk ke sistem
**Untuk Klien :**
1. Melihat jadwal terapis yang tersedia
2. Membuat pemesanan layanan terapi
3. Memilih terapis dan waktu sesi
4. Melakukan pembayaran daring
5. Melihat riwayat pemesanan
6. Melihat riwayat sesi terapi
7. Perbarui profil
8. Membatalkan/jadwal ulang pemesanan (dengan syarat)
**Untuk Terapis :**
1. Melihat jadwal sesi terapi hari ini dan minggu ini
2. Melihat detail pemesanan klien
3. Mengatur ketersediaan jadwal
4. Mendokumentasikan sesi terapi (catatan sesi)
5. Melihat riwayat klien
6. Memperbarui status sesi (selesai/dibatalkan)
7. Melihat pendapatan


**Untuk Admin :**

1. Mengelola data layanan terapi
2. Mengelola data terapis
3. Mengelola data klien
4. Melihat semua pemesanan
5. Konfirmasi pembayaran manual (jika ada)
6. Membuat laporan (pemesanan, keuangan, kinerja)
7. Pemantauan sistem
**Untuk** **_Payment Gateway_** **:**
1. Memproses pembayaran
2. Mengirim notifikasi status pembayaran
3. Verifikasi transaksi


**_4.3.9.2. Activity Diagram_**
_Activity Diagram_ menggambarkan alur aktivitas dalam sistem untuk
berbagai proses bisnis.
**a.** **_Activity Diagram_** **Proses Reservasi Terapi oleh Klien**

## Gambar IV. 3 Activity Diagram Reservasi Terapi


Alur proses pemesanan terapi :

1. Klien login ke sistem
2. Klien memilih layanan terapi yang diinginkan
3. Sistem menampilkan daftar terapis dan jadwal yang tersedia
4. Klien memilih terapis dan waktu sesi
5. Sistem memeriksa ketersediaan jadwal
    a. Jika tidak tersedia : Tampilkan pesan kesalahan, kembali ke pemilihan
       jadwal
    b. Jika tersedia : Lanjut ke langkah berikutnya
6. Klien mengisi informasi tambahan (keluhan, catatan)
7. Sistem menampilkan ringkasan pemesanan dan total biaya
8. Klien konfirmasi pemesanan
9. Sistem membuat catatan pemesanan dengan status " _Pending Payment_ "
10. Sistem alihkan ke _payment gateway_ (Midtrans)
11. Klien melakukan pembayaran
12. _Payment gateway_ memproses transaksi
    a. Jika gagal : Perbarui status menjadi " _Payment Failed_ ", kirim notifikasi
    b. Jika berhasil : Perbarui status menjadi "Paid", lanjut
13. Sistem mengirim email konfirmasi ke klien
14. Sistem mengirim notifikasi ke terapis terkait
15. Sistem mengirim email pengingat 1 hari sebelum sesi
16. Selesai


**b.** **_Activity Diagram_** **Dokumentasi Sesi Terapi oleh Terapis**

## Gambar IV. 4 Activity Diagram Dokumentasi Sesi Terapi


```
Alur proses dokumentasi sesi terapi :
```
1. Terapis login ke sistem
2. Terapis melihat daftar sesi hari ini
3. Terapis memilih sesi yang sudah dilaksanakan
4. Sistem menampilkan formulir dokumentasi sesi
5. Terapis mengisi dokumentasi:
    a. Teknik yang digunakan
    b. Observasi kondisi klien
    c. Kemajuan yang dicapai
    d. Catatan penting
    e. Rekomendasi sesi berikutnya
6. Terapis menyimpan dokumentasi
7. Sistem validasi data
    a. Jika tidak valid: Tampilkan pesan kesalahan, kembali ke formulir
    b. Jika valid: Simpan ke basis data
8. Sistem perbarui status sesi menjadi "Completed"
9. Sistem mencatat waktu dokumentasi
10. Dokumentasi tersimpan dan dapat diakses untuk sesi berikutnya
11. Selesai


**c.** **_Activity Diagram Generate_** **Laporan oleh Admin**

```
Alur proses membuat laporan :
```
1. Admin masuk ke sistem
2. Admin mengakses menu laporan
3. Admin memilih jenis laporan (pemesanan, keuangan, kinerja terapis, klien)
4. Admin memilih periode (tanggal mulai - tanggal selesai)
5. Admin memilih penyaring tambahan (terapis tertentu, layanan tertentu, dll)
6. Admin klik tombol " _Generate Laporan_ "
7. Sistem mengambil data dari basis data sesuai kriteria
8. Sistem memproses dan menghitung statistik
9. Sistem menampilkan laporan dalam format tabel dan grafik
10. Admin dapat melihat, ekspor ( _PDF/Excel_ ), atau cetak langsung
11. Selesai

## Gambar IV. 5 Activity Diagram Generate Laporan


**_4.3.9.3.Entity Relationship Diagram (ERD)_**
_Entity Relationship Diagram_ (ERD) menggambarkan struktur basis data
CUR-HEART: Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital
dengan relasi antar entitas.

## Gambar IV. 6 Activity Diagram Generate Laporan


**Entitas Utama :**

1. _users_ - Menyimpan data semua pengguna sistem (klien, terapis, admin)
2. _clients_ - Menyimpan data detail klien
3. _therapists_ - Menyimpan data detail terapis
4. _services_ - Menyimpan data layanan terapi yang ditawarkan
5. _bookings_ - Menyimpan data pemesanan terapi
6. _payments_ - Menyimpan data pembayaran
7. _sessions_ - Menyimpan data sesi terapi yang sudah dilaksanakan
8. _session_notes_ - Menyimpan catatan dokumentasi sesi terapi
9. _therapist_schedules_ - Menyimpan jadwal ketersediaan terapis
10. _therapist_unavailability_ - Menyimpan data ketidaktersediaan terapis (cuti,
    sakit)
11. _reviews_ - Menyimpan ulasan dari klien terhadap terapis/layanan
12. _notifications_ - Menyimpan notifikasi untuk pengguna
13. _settings_ - Menyimpan konfigurasi sistem
14. _activity_logs_ - Menyimpan log aktivitas pengguna (jejak audit)
**Relasi Utama :**
a. _users (1) ↔ (1) clients :_ One-to-One
b. _users (1) ↔ (1) therapists :_ One-to-One
c. _clients (1) ↔ (M) bookings :_ One-to-Many
d. _therapists (1) ↔ (M) bookings :_ One-to-Many
e. _services (1) ↔ (M) bookings :_ One-to-Many
f. _bookings (1) ↔ (1) payments :_ One-to-One
g. _bookings (1) ↔ (1) sessions :_ One-to-One
h. _sessions (1) ↔ (M) session_notes :_ One-to-Many
i. _therapists (1) ↔ (M) therapist_schedules :_ One-to-Many
j. _therapists (1) ↔ (M) therapist_unavailability :_ One-to-Many
k. _sessions (1) ↔ (M) reviews :_ One-to-Many
l. _users (1) ↔ (M) notifications :_ One-to-Many
**Keterangan :**
a. (1) = _One_
b. (M) = _Many_


```
c. PK = Primary Key
d. FK = Foreign Key
Penjelasan Desain Database :
```
1. **Normalisasi 3NF** : Database dinormalisasi hingga _Third Normal Form_
    (3NF) untuk menghindari redundansi data dan menjaga integritas data.
2. **Relasi** **_Many-to-Many_** : Tabel _therapist_services_ digunakan sebagai
    junction table untuk relasi many-to-many antara terapis dan layanan,
    memungkinkan satu terapis menangani banyak layanan dan satu layanan
    ditangani banyak terapis.
3. **Soft Delete** : Beberapa tabel menggunakan status enum untuk "soft delete"
    (misalnya status 'archived' pada blog_posts) untuk menjaga integritas
    referensial.
4. **Audit Trail** : Tabel activity_logs mencatat semua aktivitas penting
    pengguna untuk keperluan audit dan keamanan.
5. **Content Management** : Tabel blog_posts, blog_categories, faqs,
    dan faq_categories mendukung fitur content management system untuk
    admin.
6. **Financial Management** : Tabel payments dan withdrawals mengelola
    aliran keuangan dari klien ke sistem dan dari sistem ke terapis.
7. **Communication** : Tabel messages dan notifications mendukung
    komunikasi real-time antara pengguna.
8. **Indexing** : Setiap tabel memiliki index yang tepat pada kolom yang sering
    di-query untuk optimasi performa.
    Database dinormalisasi hingga Third Normal Form (3NF) untuk
menghindari redundansi data dan menjaga integritas data.
**_4.3.9.4 Desain Antarmuka Pengguna (UI/UX)_**
Desain antarmuka pengguna (UI) dibuat menggunakan Figma dengan total
66 halaman mockup yang mencakup semua peran pengguna. Desain mengikuti
prinsip _user-centered design_ dengan fokus pada kemudahan penggunaan,
aksesibilitas, dan pengalaman pengguna yang optimal.


```
A. Sistem Desain ( Design System )
Palet Warna :
1) Primary : Teal (#0D9488) - Menenangkan, profesional, penyembuhan
2) Secondary : Purple (#9333EA) - Spiritual, transformasi
3) Accent : Orange (#F59E0B) - Energi, optimisme
4) Neutral : Skala abu-abu dari #F9FAFB hingga #111827
5) Success : Green (#10B981)
6) Warning : Yellow (#F59E0B)
7) Error : Red (#EF4444)
Tipografi :
1) Heading : Inter ( Sans-serif ) - Modern, bersih, mudah dibaca
2) Body : Inter ( Sans-serif )
3) Ukuran Font : H1 (36px), H2 (30px), H3 (24px), Body (16px), Small
(14px)
Prinsip Desain :
```
1. Desain bersih dan minimal
2. Spasi yang konsisten (skala spasi Tailwind)
3. Desain responsif dengan pendekatan _mobile-first_
4. Aksesibilitas: Rasio kontras warna minimal 4,5:1
5. Hierarki visual yang jelas
6. Navigasi yang intuitif

**B.** **_Mockup_** **Halaman Utama**
Sistem memiliki **66 halaman** **_mockup_** yang terbagi dalam beberapa
kategori :


1. **Halaman Publik (12 halaman) :**

## Gambar IV. 7 Mockup Landing Page

- **_Landing Page_** _: Hero section, layanan terapi, featured therapists,_
    _testimoni klien, blog posts_


## Gambar IV. 8 Mockup Halaman Tentang Kami

- **Halaman Tentang Kami** : Kisah kami, visi & misi, nilai inti, profil tim,
    sertifikasi


## Gambar IV. 9 Mockup Katalog Layanan

- **Katalog Layanan** : Filter & pencarian, grid layanan dengan kartu detail


## Gambar IV. 10 Mockup Detail Layanan

- **Detail Layanan** : _Hero_ , navigasi tab (ikhtisar/manfaat/proses/FAQ), terapis
    yang direkomendasikan, ulasan


## Gambar IV. 11 Mockup Direktori Terapis

- **Direktori Terapis** : Pencarian, filter spesialisasi/rating/pengalaman, grid
    terapis


## Gambar IV. 12 Mockup Profil Terapis

- **Profil Terapis** : Bio lengkap, pendidikan & sertifikasi, layanan & harga,
    kalender ketersediaan, ulasan klien


## Gambar IV. 13 Mockup Daftar Blog

- **Daftar Blog** : Artikel unggulan, pencarian, filter kategori, grid artikel blog,
    bilah samping


## Gambar IV. 14 Mockup Detail Blog

- **Detail Blog** : Konten artikel, metadata, berbagi media sosial, artikel terkait,
    bagian komentar


## Gambar IV. 15 Mockup Hubungi Kami

- **Hubungi Kami** : Formulir, info kontak, _Google Maps_ , tautan media sosial


## Gambar IV. 16 Mockup FAQ

- **FAQ** : Pencarian, tab kategori, daftar akordion dengan umpan balik


## Gambar IV. 17 Mockup Kebijakan Privasi

- **Kebijakan Privasi** : Daftar isi, bagian terstruktur, sorotan penting


## Gambar IV. 18 Mockup Syarat & Ketentuan

- **Syarat & Ketentuan** : Daftar isi, klausul bernomor untuk referensi legal


2. **Halaman Autentikasi (4 halaman) :**

## Gambar IV. 19 Mockup Login

- **_Login_** : Layar terpisah dengan ilustrasi, _email_ & kata sandi, ingat saya, _login_
    sosial media

## Gambar IV. 20 Mockup Registrasi Klien


## Gambar IV. 21 Mockup Registrasi Terapis

- **_Registrasi_** : Pilihan tipe pengguna (Klien/Terapis), formulir berbeda per
    peran, kotak centang syarat

## Gambar IV. 22 Mockup Lupa Kata Sandi

- **Lupa Kata Sandi** : Formulir sederhana, kirim tautan _reset_ , status berhasil


## Gambar IV. 23 Mockup Reset Kata Sandi

- **_Reset_** **Kata Sandi** : Kata sandi baru, konfirmasi kata sandi, pengukur
    kekuatan kata sandi


3. **_Dashboard_** **Klien (12 halaman) :**

## Gambar IV. 24 Mockup Dasbor Klien

- **Dasbor Utama** : Sambutan, statistik cepat, janji temu berikutnya, sesi
    mendatang, ikhtisar kemajuan

## Gambar IV. 25 Mockup Reservasi Langkah 1 - Pilih Layanan

- **Reservasi Langkah 1** : Pemilihan layanan dengan kartu layanan


## Gambar IV. 26 Mockup Reservasi Langkah 2 - Pilih Terapis

- **Reservasi Langkah 2** : Pilih terapis dengan profil dan rating

```
Gambar IV. 27 Mockup Reservasi Langkah 3 - Pilih Jadwal
```
- **Reservasi Langkah 3** : Pemilih tanggal & waktu dengan ketersediaan waktu
    nyata


## Gambar IV. 28 Mockup Reservasi Langkah 4 - Konfirmasi & Pembayaran

- **Reservasi Langkah 4** : Konfirmasi & pembayaran dengan ringkasan
    reservasi

## Gambar IV. 29 Mockup Reservasi Berhasil

- **Reservasi Berhasil** : Selamat, detail reservasi, langkah selanjutnya, tombol
    aksi


## Gambar IV. 30 Mockup Janji Temu

- **Janji Temu Saya** : Tab (mendatang/lampau/dibatalkan), filter & urutkan,
    kartu janji temu

## Gambar IV. 31 Mockup Detail Janji Temu

- **Detail Janji Temu** : Info reservasi, info pembayaran, catatan sesi, aksi
    jadwal ulang/batalkan


## Gambar IV. 32 Mockup Dasbor Kemajuan

- **Dasbor Kemajuan** : Skor kesehatan, kehadiran sesi, tujuan & pencapaian,
    pelacakan suasana hati

## Gambar IV. 33 Mockup Pesan

- **Pesan :** Daftar percakapan, area obrolan aktif, indikator mengetik


## Gambar IV. 34 Mockup Pengaturan Klien

- **Pengaturan Klien** : Profil, keamanan, notifikasi, privasi


## Gambar IV. 35 Mockup Notifikasi Klien

- **Notifikasi Klien** : Daftar notifikasi, filter, tandai sebagai dibaca
4. **_Dashboard_** **Terapis (13 halaman) :**

## Gambar IV. 36 Mockup Dasbor Terapis - Dasbor Utama

- **Dasbor Utama** : Sesi hari ini, metrik kunci, ikhtisar pendapatan, ulasan
    klien


## Gambar IV. 37 Mockup Manajemen Jadwal

- **Manajemen Jadwal** : Tampilan kalender (hari/minggu/bulan), blok janji
    temu, waktu libur

## Gambar IV. 38 Mockup Pengaturan Ketersediaan

- **Pengaturan Ketersediaan** : Jam kerja per hari, durasi sesi, jendela
    reservasi, tanggal khusus


## Gambar IV. 39 Mockup Daftar Klien

- **Daftar Klien** : Cari & filter, kartu klien dengan statistik, aksi massal

## Gambar IV. 40 Mockup Tampilan Profil Klien

- **Tampilan Profil Klien** : Ikhtisar, riwayat sesi, catatan & observasi,
    kemajuan & tujuan, berkas


## Gambar IV. 41 Mockup Ruang Sesi

- **Ruang Sesi** : Konferensi video dengan timer, bilah kontrol, panel catatan

## Gambar IV. 42 Mockup Formulir Catatan Sesi

- **Formulir Catatan Sesi** : Penilaian, ringkasan sesi, catatan kemajuan, tugas
    rumah, templat


## Gambar IV. 43 Mockup Riwayat Sesi

- **Riwayat Sesi** : Total sesi, cari & filter, tabel sesi, analitik

## Gambar IV. 44 Mockup Dasbor Pendapatan

- **Dasbor Pendapatan** : Saldo, grafik pendapatan, transaksi, penarikan,
    pengaturan pembayaran


## Gambar IV. 45 Mockup Edit Profil Terapis

- **_Edit_** **Profil** : Tab untuk dasar / professional / tentang / Pendidikan / layanan
    / media / pengaturan


## Gambar IV. 46 Mockup Pengaturan Terapis

- **Pengaturan Terapis** : Preferensi akun, keamanan, notifikasi


## Gambar IV. 47 Mockup Pesan Terapis

- **Pesan Terapis** : Daftar percakapan dengan klien, area obrolan

## Gambar IV. 48 Mockup Notifikasi Terapis

- **Notifikasi Terapis** : Daftar notifikasi sistem, filter, tandai sebagai dibaca


4. **_Dashboard_** **Admin (25 halaman) :**

## Gambar IV. 49 Mockup Dasbor Admin - Dasbor Utama

- **Dasbor Utama** : Metrik kunci, grafik pendapatan, reservasi terbaru,
    pertumbuhan pengguna, peringatan sistem

## Gambar IV. 50 Mockup Manajemen Reservasi

- **Manajemen Reservasi** : Ringkasan statistik, tab (semua / mendatang /
    lampau / tertunda / dibatalkan / sengketa), tabel reservasi


## Gambar IV. 51 Mockup Manajemen Pengguna

- **Manajemen Pengguna** : Tab (semua/klien/terapis/admin/tertunda), tabel
    pengguna, aksi massal

## Gambar IV. 52 Mockup Laporan Keuangan

- **Laporan Keuangan** : Ringkasan pendapatan, grafik, tabel transaksi,
    penarikan, pengembalian dana, analitik


## Gambar IV. 53 Mockup Pengaturan Sistem

- **Pengaturan Sistem** : Navigasi kategori, umum / reservasi / pembayaran /
    email / keamanan / kebijakan / integrasi / lanjutan

## Gambar IV. 54 Mockup Notifikasi Admin

- **Notifikasi Admin** : Daftar notifikasi sistem, filter berdasarkan tipe, tandai
    sebagai dibaca


## Gambar IV. 55 Mockup Pesan Admin

- **Pesan Admin** : Daftar percakapan dengan pengguna, area obrolan,
    dukungan pelanggan

## Gambar IV. 56 Mockup Detail Pengguna

- **Detail Pengguna** : Profil lengkap, riwayat aktivitas, statistik, aksi moderasi


## Gambar IV. 57 Mockup Edit Pengguna

- **Edit Pengguna** : Formulir edit data pengguna, ubah peran, status akun

## Gambar IV. 58 Mockup Detail Reservasi

- **Detail Reservasi** : Informasi lengkap reservasi, timeline status, aksi admin


```
Gambar IV. 59 Mockup Manajemen Transaksi
```
- **Manajemen Transaksi** : Daftar semua transaksi pembayaran, filter, ekspor
    laporan

## Gambar IV. 60 Mockup Manajemen Penarikan

- **Manajemen Penarikan** : Permintaan penarikan dana terapis, approval,
    riwayat


## Gambar IV. 61 Mockup Detail Penarikan

- **Detail Penarikan** : Informasi penarikan, verifikasi, bukti transfer

## Gambar IV. 62 Mockup Log Aktivitas

- **Log Aktivitas** : Jejak audit sistem, filter berdasarkan pengguna/aksi/tanggal


## Gambar IV. 63 Mockup Laporan & Analitik

- **Laporan & Analitik** : Dashboard analitik lanjutan, berbagai jenis laporan,
    ekspor

## Gambar IV. 64 Mockup Manajemen Ulasan

- **Manajemen Ulasan** : Daftar ulasan klien, moderasi, tanggapan, filter
    rating


## Gambar IV. 65 Mockup Manajemen Promo

- **Manajemen Promo** : Daftar kode promo, buat/ _edit_ /hapus, statistik
    penggunaan

## Gambar IV. 66 Mockup Verifikasi Terapis

- **Verifikasi Terapis** : Daftar pendaftaran terapis baru, _review_ dokumen,
    _approval/reject_


## Gambar IV. 67 Mockup Editor Blog

- **_Editor Blog_** : _Rich text editor_ untuk membuat/ _edit_ artikel blog, kategori, tag,
    SEO

## Gambar IV. 68 Mockup Manajemen Konten Blog

- **Manajemen Konten Blog** : Daftar artikel, status ( _draft_ / _published_ ), aksi
    CRUD


## Gambar IV. 69 Mockup Editor FAQ

- **_Editor FAQ_** : Formulir untuk membuat/ _edit_ pertanyaan dan jawaban FAQ,
    kategori

## Gambar IV. 70 Mockup Manajemen Konten FAQ

- **Manajemen Konten FAQ** : Daftar FAQ, kategori, urutan tampilan, aksi
    CRUD


## Gambar IV. 71 Mockup Editor Layanan

- **_Editor_** **Layanan** : Formulir lengkap untuk membuat/ _edit_ layanan terapi,
    harga, durasi

## Gambar IV. 72 Mockup Manajemen Konten Layanan

- **Manajemen Konten Layanan** : Daftar layanan, status aktif/nonaktif, aksi
    CRUD


## Gambar IV. 73 Mockup Editor Promo

- **_Editor Promo_** : Formulir untuk membuat/ _edit_ promosi, banner, periode
    aktif, target

**C. Fitur Desain Unggulan**
Desain Responsif :

1. Pendekatan _mobile-first_ dengan _breakpoints_ optimal
2. Adaptif untuk desktop (1920px), tablet (768px), dan mobile (375px)
3. _Touch-friendly_ untuk perangkat mobile (min 44x44px _tap targets_ )
Aksesibilitas :
1. Memenuhi standar _WCAG 2.1 Level AA_
2. Rasio kontras warna minimal 4.5:1 untuk teks normal
3. Dukungan navigasi keyboard
4. Ramah _screen reader_ dengan label _ARIA_ yang tepat
5. Indikator fokus yang jelas
Pengalaman Pengguna :
1. Pola navigasi konsisten di semua halaman
2. Tombol _call-to-action_ yang jelas dengan hierarki
3. Status pemuatan dan _skeleton screens_
4. Status kesalahan dengan pesan membantu


5. Status berhasil dengan aksi selanjutnya yang jelas
6. Status kosong dengan panduan
Desain Visual :
1. Spasi konsisten menggunakan skala spasi _Tailwind_ (unit dasar 4px)
2. Hierarki tipografi yang jelas
3. Ikonografi menggunakan _Heroicons_ (SVG)
4. Gambar dengan foto dan ilustrasi berkualitas tinggi
5. Interaksi mikro untuk pengalaman menyenangkan ( _hover states_ , transisi,
animasi)
Desain Formulir :
1. Label dan _placeholder_ yang jelas
2. Validasi sebaris dengan pesan kesalahan yang membantu
3. Indikator kemajuan untuk formulir multi-langkah
4. Simpan otomatis draf untuk formulir panjang
5. Indikator bidang wajib (*)
Visualisasi Data :
1. Grafik menggunakan _Chart.js_ / _ApexCharts_
2. Palet ramah buta warna
3. _Tooltips_ interaktif
4. Responsif untuk berbagai ukuran layar
5. Kemampuan ekspor (PNG, SVG, PDF)
**D. Prototype Interaktif**
Prototipe interaktif telah dibuat di Figma dengan fitur :
1. Navigasi _click-through_ antar halaman
2. _Hover states_ dan interaksi mikro
3. Simulasi validasi formulir
4. Pratinjau responsif untuk berbagai perangkat
5. Anotasi untuk _developer handoff_
6. Spesifikasi desain (spasi, warna, tipografi)
7. Pustaka komponen untuk dapat digunakan kembali
**E. Design Handoff**
Dokumentasi lengkap untuk pengembang mencakup :


1. **Pustaka Komponen** : 50+ komponen yang dapat digunakan kembali
    (tombol, kartu, formulir, modal, tabel)
2. **Token Desain** : Warna, tipografi, spasi, bayangan, _border-radius_
3. **Ekspor Aset** : Ikon (SVG), gambar (WebP/PNG), ilustrasi (SVG)
4. **Spesifikasi** : Detail spasi, ukuran, dan posisi
5. **Catatan Pengembang** : Panduan implementasi, dependensi, kasus tepi
6. **Daftar Periksa Aksesibilitas** : Persyaratan aksesibilitas per komponen

**Ringkasan Desain UI/UX :**
Total **66 halaman mockup** yang mencakup seluruh perjalanan pengguna dari 4
peran berbeda (Tamu, Klien, Terapis, Admin). Rincian distribusi halaman :

1. **Halaman Publik** : 12 halaman (landing, layanan, terapis, blog, kontak, FAQ,
    dll)
2. **Halaman Autentikasi** : 4 halaman (login, register, lupa password, reset
    password)
3. **_Dashboard_** **Klien** : 12 halaman ( _dashboard, booking flow 4 steps,_
    _appointments, progress, messages, settings, notifications_ )
4. **_Dashboard_** **Terapis** : 13 halaman ( _dashboard, schedule, availability, clients,_
    _session room, notes, history, earnings, profile edit, settings, messages,_
    _notifications_ )
5. **_Dashboard_** **Admin** : 25 halaman ( _dashboard, users, bookings_ , _financial_ ,
    _content management, reviews, verification, reports_ )
Semua _mockup_ dirancang dengan prinsip :
1. Responsif : Adaptif untuk desktop, tablet, dan mobile
2. Aksesibilitas : Memenuhi standar _WCAG 2.1 AA_
3. Konsistensi : Mengikuti sistem desain yang telah ditetapkan
4. Ramah Pengguna : Intuitif dan mudah digunakan
5. Profesional : Mencerminkan kredibilitas layanan kesehatan mental
Desain telah melalui beberapa iterasi berdasarkan umpan balik dari pemangku
kepentingan dan _usability testing_ dengan sampel pengguna.


### 4.4. Faktor Penentu Keberhasilan

Keberhasilan implementasi CUR-HEART: Inovasi Sistem Informasi
Layanan Terapi Mental Berbasis Digital ditentukan oleh berbagai faktor yang
saling berkaitan. Faktor-faktor ini dibagi menjadi Faktor Kunci Keberhasilan ( _Key
Success Factors_ /KSF), Faktor Kritis Keberhasilan ( _Critical Success Factors_ /CSF),
dan Indikator Kinerja Utama ( _Key Performance Indicators_ /KPI).
**4.4.1. Faktor Kunci Keberhasilan (** **_Key Success Factors_** **/KSF)**
Faktor Kunci Keberhasilan adalah faktor-faktor kunci yang mendukung
pencapaian tujuan proyek secara umum.
**A. Faktor Teknologi**

1. Stabilitas dan Keandalan Sistem
    a) Sistem harus mampu beroperasi 24/7 dengan _uptime_ minimal 99,5%
    b) Waktu respons halaman tidak lebih dari 2 detik
    c) Optimasi _query database_ untuk menangani pengguna bersamaan
       ( _concurrent users_ )
    d) Cadangan ( _backup_ ) otomatis harian untuk keamanan data
2. Antarmuka yang Mudah Digunakan
    a) _Desain UI/UX_ yang intuitif dan mudah dipahami
    b) Desain responsif ( _responsive design_ ) untuk semua perangkat
       (desktop, tablet, mobile)
    c) Konsistensi bahasa desain menggunakan sistem desain ( _design_
       _system_ )
    d) Standar aksesibilitas (WCAG 2.1 Level AA)
3. Keamanan Data
    a) Enkripsi data sensitif (kata sandi/ _password_ , rekam medis/ _medical_
       _records_ )
    b) HTTPS untuk semua komunikasi
    c) Autentikasi dan otorisasi yang kuat
    d) Kepatuhan terhadap UU PDP (Perlindungan Data Pribadi)
4. Skalabilitas
    a) Arsitektur yang dapat menangani pertumbuhan pengguna
    b) Normalisasi basis data untuk efisiensi penyimpanan ( _storage_ )


c) Mekanisme _caching_ untuk optimasi kinerja
**B. Faktor Manusia**

1. Kompetensi Tim Pengembang
    a) Penguasaan _framework_ Laravel dan pemrograman PHP
    b) Pemahaman desain basis data dan MySQL
    c) Kemampuan pengembangan _frontend_ (HTML, CSS, JavaScript,
       Tailwind)
    d) Pengetahuan kontrol versi/ _version control_ (Git)
2. Komitmen Pemangku Kepentingan
    a) Dukungan penuh dari manajemen CUR-HEART
    b) Keterlibatan aktif pemilik dalam pengumpulan kebutuhan
    c) Umpan balik konstruktif dari terapis dan admin
    d) Kesediaan untuk pengujian dan UAT ( _User Acceptance Testing_ )
3. Tingkat Adopsi Pengguna
    a) Pelatihan yang memadai untuk terapis dan admin
    b) Panduan pengguna yang komprehensif
    c) Dukungan teknis yang responsif
    d) Manajemen perubahan yang efektif
**C. Faktor Manajemen Proyek**
1. Perencanaan yang Matang
a) Ruang lingkup yang jelas dan terukur
b) Jadwal yang realistis (11 minggu)
c) Alokasi sumber daya yang optimal
d) Strategi mitigasi risiko yang efektif
2. Komunikasi yang Efektif
a) Pertemuan rutin mingguan ( _weekly standup_ )
b) Dokumentasi yang jelas
c) Pelacakan kemajuan dengan diagram Gantt ( _Gantt chart_ )
d) Pelacakan isu dan penyelesaian
3. Jaminan Kualitas
a) Pengujian sistematis di setiap fase
b) Tinjauan kode dan pemrograman berpasangan ( _pair programming_ )


c) Pelacakan bug dan prioritas perbaikan
d) Perbaikan berkelanjutan berdasarkan umpan balik
**4.4.2. Faktor Kritis Keberhasilan (** **_Critical Success Factors_** **/CSF)**
Faktor Kritis Keberhasilan adalah faktor-faktor yang **HARUS** dipenuhi
agar proyek berhasil.
CSF 1 : Ketersediaan dan Keandalan Sistem
a) Target: Waktu aktif ( _uptime_ ) ≥ 99,5%, Waktu respons < 2 detik
b) Dapat menangani minimal 100 pengguna bersamaan
c) Tidak ada kehilangan data dalam kondisi normal
CSF 2 : Keamanan dan Privasi Data
a) Tidak ada pelanggaran keamanan atau akses tidak sah
b) Semua data sensitif terenkripsi
c) Implementasi HTTPS untuk semua halaman
d) _RBAC_ ( _Role-Based Access Control_ ) berfungsi dengan baik
CSF 3 : Adopsi dan Kepuasan Pengguna
a) Minimal 70% klien menggunakan sistem untuk reservasi
b) Skor kepuasan pengguna ≥ 4,0 dari 5,0
c) Skor SUS ( _System Usability Scale_ ) ≥ 68
d) Tingkat adopsi terapis 100%
CSF 4 : Integrasi dengan Proses Bisnis
a) 100% reservasi melalui sistem (tidak ada lagi manual)
b) Pengurangan beban kerja administratif minimal 50%
c) Pengurangan kesalahan reservasi hingga 90%
d) Laporan dapat dihasilkan dalam 5 menit
CSF 5 : Kepatuhan Anggaran dan Jadwal
a) Penyelesaian proyek dalam 11 minggu (± 1 minggu toleransi)
b) Biaya aktual tidak melebihi 110% anggaran (Rp 5,5 juta)
c) Semua luaran selesai sesuai ruang lingkup
**4.4.3. Indikator Kinerja Utama (** **_Key Performance Indicators_** **/KPI)**
KPI adalah metrik terukur untuk memantau keberhasilan sistem setelah
penerapan.


## Tabel IV. 11 Key Performance Indicators (KPI)

```
Kategori Nama KPI Target
```
```
Frekuensi
Pemantauan
```
**Kinerja
Sistem**

```
Waktu Aktif Sistem
( Uptime ) ≥ 99,5%^
```
```
Waktu nyata
( real-time )
Waktu Respons ≤ 2 detik Mingguan
Tingkat Galat ( Error
Rate ) ≤ 0,5%^ Harian^
```
**Keamanan**

```
Kerentanan Keamanan
( Security Vulnerabilities ) 0 kritis^ Bulanan^
Insiden Pelanggaran Data
( Data Breach Incidents )
```
```
0 Waktu nyata
( real-time )
```
**Adopsi
Pengguna**

```
Total Pengguna Terdaftar 200 dalam
3 bulan
```
```
Bulanan
```
```
Pengguna Aktif Bulanan
( Monthly Active Users )
```
```
150 (75%) Bulanan
```
```
Tingkat Konversi
Reservasi ( Conversion
Rate )
```
```
≥ 60% Mingguan
```
**Transaksi**

Total Reservasi/Bulan (^100) reservasi Bulanan
Tingkat Keberhasilan
Pembayaran ( _Payment
Success Rate_ )
≥ 95% Mingguan
Pendapatan/Bulan Rp 30 juta Bulanan
**Kepuasan** Skor Kepuasan Pengguna ≥ 4,0/5,0 Per reservasi


**Kategori Nama KPI Target** (^) **PemantauanFrekuensi**
Skor NPS ( _Net Promoter
Score_ ) ≥ 30^ Triwulanan^
Skor SUS ( _System
Usability Scale_ ) ≥ 68^ Triwulanan^
**Efisiensi**
Rata-rata Waktu
Reservasi ≤ 3 menit^ Mingguan^
Pengurangan Beban Kerja
Admin
≥ 50% Bulanan
Waktu Pembuatan
Laporan ≤ 5 menit^ Bulanan^

### 4.5. Keuntungan Yang Diharapkan

Implementasi CUR-HEART: Inovasi Sistem Informasi Layanan Terapi
Mental Berbasis Digital diharapkan memberikan berbagai keuntungan bagi
pemangku kepentingan yang terlibat.
**4.5.1. Manfaat untuk CUR-HEART (Organisasi)**
A. Efisiensi Operasional

1. Proses reservasi otomatis : Pengurangan waktu dari 10-15 menit
    menjadi 3 menit per reservasi, penghematan sekitar 20 jam per bulan
2. Manajemen penjadwalan : Koordinasi jadwal berkurang dari 5 jam per
    minggu menjadi 1 jam, utilisasi meningkat dari 60% menjadi 80%
3. Pelaporan otomatis : Waktu pembuatan laporan dari 2 jam menjadi 5
    menit, penghematan 8 jam per bulan
4. Eliminasi reservasi ganda : Konflik jadwal turun dari 8-10 kasus per
    bulan menjadi 0 kasus
B. Pertumbuhan Pendapatan
1. Peningkatan volume _reservasi_ : Target +25% dari 80 menjadi 100
reservasi per bulan (Rp 72 juta/tahun tambahan)


2. Pengurangan tidak hadir : Dari 15% menjadi 5% dengan pengingat
    otomatis (Rp 28,8 juta/tahun pendapatan dipulihkan)
3. Perpanjangan jam layanan : Reservasi 24/7 menangkap 15% lebih
    banyak klien (Rp 10 juta/tahun)
4. Retensi klien : Peningkatan dari 35% menjadi 60% dengan pengalaman
    yang lebih baik
C. Kualitas & Layanan
1. Pengambilan keputusan berbasis data : Dasbor waktu nyata untuk
analisis cepat
2. Pemantauan kualitas : Sistematis dengan target SUS ≥ 68, NPS ≥ 30
3. Skalabilitas : Sistem digital dapat mendukung pertumbuhan 5× tanpa
tambahan staf
**Total Manfaat Tahunan Terukur :**
1. Peningkatan Pendapatan : Rp 115,8 juta/tahun
2. Penghematan Biaya : Rp 18,4 juta/tahun
3. **TOTAL** : Rp 134,2 juta/tahun
**4.5.2. Manfaat untuk Klien**
A. Kenyamanan
1. Reservasi 24/7 kapan saja tanpa terbatas jam kantor
2. Tidak perlu telepon, layanan mandiri daring
3. Ramah perangkat seluler untuk reservasi saat bepergian
4. Penjadwalan ulang mudah tanpa koordinasi manual
B. Transparansi
1. Profil terapis lengkap dengan pendidikan, spesialisasi, dan ulasan
2. Ketersediaan waktu nyata dengan kalender visual
3. Harga transparan per layanan
4. Sistem rating & ulasan untuk memilih terapis terbaik
C. Layanan Mandiri
1. Akses riwayat janji temu lengkap
2. Lihat catatan sesi yang dibagikan terapis
3. Pelacakan kemajuan terapi dengan grafik visual
4. Pengingat otomatis untuk sesi mendatang


```
Nilai untuk Klien :
```
1. Penghematan waktu : 25-55 menit per reservasi
2. Target kepuasan : ≥ 4,0/5,0, SUS ≥ 68
3. Retensi meningkat : 35% → 60%
**4.5.3. Manfaat untuk Terapis**
A. Penghematan Waktu
1. Manajemen jadwal mandiri mengurangi koordinasi dengan admin
2. Hemat 16 jam per bulan untuk administrasi
3. Dokumentasi sesi digital lebih cepat (5 menit vs 15 menit)
B. Potensi Pendapatan
1. Utilisasi lebih baik dari 60% → 80%
2. Peningkatan pendapatan +33% (Rp 5 juta/bulan)
3. Akses ke analytics kinerja pribadi
C. Keseimbangan Kerja-Hidup
1. Otonomi dan fleksibilitas dalam mengatur jadwal
2. Beban administratif berkurang signifikan
3. Target kepuasan terapis: ≥ 4,5/5,0
**4.5.4. Analisis Laba atas Investasi (** **_Return on Investment_** **/ROI)**
Investasi :
1. Biaya awal : Rp 3.000.000 (pengaturan/ _setup_ )
2. Biaya berulang tahun 1: Rp 9.750.000 ( _hosting_ , domain, _payment
gateway_ )
3. **Total biaya tahun 1 : Rp 12.750.000**
Manfaat Tahun 1 :
1. Peningkatan pendapatan : Rp 142.800.000
2. Penghematan biaya : Rp 26.400.000
3. **Total manfaat : Rp 169.200.000**
Hasil :
1. Manfaat bersih : Rp 156.450.000
2. ROI : 1.227%
3. Periode pengembalian ( **_payback period_** ): 0,9 bulan (~27 hari)
4. Rasio Manfaat-Biaya : 13,3:1


```
Proyeksi 5 Tahun:
```
1. Total manfaat: Rp 1.025.481.825
2. Total biaya: Rp 60.098.000
3. Manfaat bersih: Rp 964.383.829
4. ROI 5 tahun: 7.258%
**Rekomendasi :** Proyek sangat layak dengan ROI luar biasa dan periode
pengembalian ( _payback period_ ) sangat singkat.

### 4.6. Teknologi Yang Digunakan

Teknologi yang digunakan untuk membangun CUR-HEART: Inovasi Sistem
Informasi Layanan Terapi Mental Berbasis Digital secara garis besar dapat dibagi
ke dalam beberapa bagian berikut ini :
**4.6.1. Server dan Infrastruktur**
A. _Web Server_

1. _Nginx 1.18.0_ : _Web server_ berkinerja tinggi untuk menangani koneksi
    bersamaan ( _concurrent connections_ )
2. _PHP 8.1_ : Bahasa pemrograman sisi server ( _server-side scripting_
    _language_ ) dengan fitur modern (kompilator _JIT_ , argumen
    bernama/ _named arguments_ , atribut/ _attributes_ )
B. _Hosting_
1. VPS ( **_Virtual Private Server_** ): Ubuntu Server 22.04 LTS
2. Spesifikasi: 4 vCPU, 8GB RAM, 160GB Penyimpanan SSD ( _SSD
Storage_ )
3. SLA Waktu Aktif ( _Uptime SLA_ ): 99,9%
4. _Bandwidth_ : Tidak terbatas ( _Unlimited_ )
C. _Server_ Basis Data
1. _MySQL 8.0_ : Sistem manajemen basis data relasional
2. _Storage Engine_ : InnoDB untuk kepatuhan _ACID_
3. _Backup_ : Cadangan otomatis harian dengan retensi 30 hari
D. Kontrol Versi
1. _Git & GitHub_ : Manajemen kode sumber dan kolaborasi


**4.6.2.** **_Backend Development_**
A. _Framework_ & Bahasa
**Laravel 10** : _Framework_ PHP modern dengan arsitektur MVC
1) _Eloquent ORM_ untuk abstraksi basis data
2) _Blade templating engine_
3) _Middleware_ untuk autentikasi & otorisasi
4) Sistem antrian untuk pekerjaan latar belakang
5) _Event_ & _listener_ untuk operasi asinkron
B. Autentikasi & Otorisasi

1. _Laravel Sanctum_ untuk autentikasi token API
2. _Laravel Permission_ (Spatie) untuk kontrol akses berbasis peran/ _role-_
    _based access control_ (RBAC)
3. _Bcrypt_ untuk _hashing_ kata sandi
C. Pustaka ( _Libraries_ ) & Paket ( _Packages_ )
1. Midtrans PHP SDK untuk integrasi _payment gateway_
2. Laravel Mail untuk notifikasi email
3. Carbon untuk manipulasi tanggal/waktu
4. Intervention Image untuk pemrosesan gambar
**4.6.3. Pengembangan** **_Frontend_**
A. Teknologi
1. **HTML5** : _Markup_ semantik modern
2. **CSS3** : _Styling_ dengan _flexbox_ dan _grid_
3. **JavaScript (ES6+)** : Interaktivitas dan konten dinamis
4. **Alpine.js** : _Framework_ JavaScript ringan untuk komponen reaktif
B. _Framework_ **CSS**
_Tailwind CSS 3.3_ : _Framework_ CSS berbasis utilitas ( _utility-first_ )
1) Desain responsif dengan pendekatan _mobile-first_
2) Palet warna dan tipografi kustom
3) Kompilator _JIT_ ( _Just-In-Time_ ) untuk optimasi
4) _PurgeCSS_ untuk menghapus _styles_ yang tidak digunakan
C. Komponen UI
1. Pustaka komponen kustom berbasis Tailwind


2. Ikon : Heroicons (set ikon SVG)
3. Validasi formular : Sisi klien ( _client-side_ ) dengan JavaScript + sisi
    server ( _server-side_ ) Laravel
**4.6.4. Manajemen Basis Data**
A. Manajemen Basis Data
1. _MySQL_ 8.0 : Basis data utama
2. Set Karakter ( _Character Set_ ) : utf8mb4 untuk dukungan Unicode penuh
3. _Collation_ : utf8mb4_unicode_ci
B. Desain Basis Data
1. 16 tabel dengan normalisasi 3NF
2. Batasan kunci asing ( _foreign key_ ) untuk integritas referensial
3. Indeks pada kolom yang sering di- _query_
4. _Timestamps_ untuk jejak audit
C. Migrasi & _Seeding_
1. Laravel _Migrations_ untuk kontrol versi skema basis data
2. _Seeders_ untuk data sampel dan data pengujian
**4.6.5. Integrasi & Layanan Eksternal**
A. _Payment Gateway_
Midtrans : _Payment gateway_ terintegrasi
1) _Snap API_ untuk proses pembayaran ( _checkout_ ) yang mulus
2) Dukungan : Kartu kredit, Transfer bank, Dompet digital (GoPay, OVO,
Dana)
3) Keamanan : Memenuhi standar _PCI-DSS_
4) _Webhook_ untuk notifikasi pembayaran
B. Layanan Email
SMTP ( _Mailtrap/SendGrid_ ) **:** Layanan pengiriman email
1) Email notifikasi (konfirmasi reservasi, pengingat)
2) Email transaksional (reset kata sandi, email selamat datang)
3) Berbasis antrian untuk menghindari pemblokiran
C. Penyimpanan Berkas
1. Penyimpanan lokal untuk pengembangan
2. AWS S3 / DigitalOcean Spaces (siap untuk skala produksi)


**4.6.6. Peralatan Pengembangan**
A. Kontrol Versi

1. **Git** : Sistem kontrol versi terdistribusi
2. **GitHub** : _Hosting_ repositori jarak jauh
3. Strategi percabangan ( _branching_ ) : _GitFlow_ ( _main_ , _develop_ , _feature_
    _branches_ )
B. Editor Kode & IDE
Visual Studio _Code_ dengan ekstensi :
1) _Laravel Extension Pack_
2) _PHP Intelephense_
3) _Tailwind CSS IntelliSense_
4) _ESLint & Prettier_
C. Manajer Paket
1. _Composer_ : Manajemen dependensi PHP
2. _NPM_ : Manajemen paket _JavaScript_
**4.6.7. Pengujian**
A. _Framework_ Pengujian
1. **PHPUnit** : Pengujian unit ( _unit testing_ ) untuk logika _backend_
2. **_Laravel Dusk_** : Pengujian otomasi peramban ( _browser_ )
3. Pengujian fitur untuk titik akhir ( _endpoint_ ) API
B. Kualitas Kode
1. _PHP Code Sniffer_ untuk standar pengodean
2. _Laravel Debugbar_ untuk pengawakutuan ( _debugging_ ) pengembangan
3. Pelacakan kesalahan ( _error tracking_ ) & pemantauan ( _monitoring_ )
**4.6.8. Penerapan (** **_Deployment_** **) &** **_DevOps_**
A. Penerapan ( _Deployment_ **)**
1. _GitHub Actions_ : Otomasi CI/CD
2. Pengujian otomatis sebelum penerapan
3. Strategi penerapan tanpa _downtime_ ( _zero-downtime deployment_ )
B. Pemantauan ( _Monitoring_ )
1. _UptimeRobot_ : Pemantauan waktu aktif ( _uptime monitoring_ )


2. _New Relic / Laravel Telescope_ : Pemantauan kinerja aplikasi
    ( _application performance monitoring_ )
3. Pencatatan kesalahan ( _error logging_ ) dengan Laravel Log
C. Keamanan
1. **_Let's Encrypt_** : Sertifikat SSL/TLS gratis
2. HTTPS ditegakkan untuk semua koneksi
3. Perlindungan CSRF (bawaan Laravel)
4. Pencegahan XSS
5. Pencegahan injeksi SQL ( _SQL injection_ ) (Eloquent ORM)
6. Pembatasan laju ( _rate limiting_ ) untuk titik akhir ( _endpoint_ ) API
**4.6.9. Desain & Pembuatan Prototipe**
A. Desain UI/UX
1. Figma : Peralatan desain untuk _wireframes_ dan _mockups_
2. 66 halaman _mockup_ untuk semua peran pengguna
3. Sistem desain dengan palet warna dan tipografi
B. Peralatan Diagram
1. **Draw.io / Lucidchart** : ERD, _Use Case_ , Diagram Aktivitas
2. **StarUML** : Diagram kelas dan diagram sekuens
**4.6.10. Manajemen Proyek**
A. Perencanaan
1. _Microsoft Project / GanttProject_ : Diagram Gantt dan WBS
2. _Trello / Notion_ : Manajemen tugas dan kolaborasi
B. Dokumentasi
1. _Markdown_ : Dokumentasi teknis
2. _Swagger / Postman_ : Dokumentasi API


**4.6.11. Ringkasan Stack Teknologi**

```
Klien (Peramban)
HTML5 | CSS3 | JavaScript | Alpine.js
Tailwind CSS
```
##### HTTPS

```
Web Server (Nginx)
```
```
Aplikasi ( Laravel 10 + PHP 8.1)
MVC | Eloquent ORM | Blade Templates
Middleware | Queue | Events
```
```
Basis Data
MySQL 8.0
16 Tabel
```
```
API Eksternal
```
- Midtrans
- Email SMTP

## Gambar IV. 74 Ringkasan Stack Teknologi


**4.6.12. Alasan Pemilihan Teknologi
Tabel 4.9 - Justifikasi Pemilihan Teknologi
Teknologi Alasan Pemilihan**

```
Laravel 10
```
```
Framework PHP terpopuler dengan ekosistem lengkap,
dokumentasi sangat baik, dukungan komunitas kuat, dan
fitur bawaan yang komprehensif
```
```
MySQL 8.0 Basis data relasional yang matang, andal, didukung luas, dan
gratis ( open source )
```
```
Tailwind
CSS
```
```
Produktivitas tinggi, ukuran berkas kecil setelah purge ,
sangat dapat disesuaikan ( highly customizable ), dan
pembuatan prototipe cepat ( rapid prototyping )
```
```
Nginx +
PHP 8.1
```
```
Kombinasi berkinerja tinggi untuk aplikasi lalu lintas tinggi
( high-traffic applications ) dengan jejak memori rendah
( memory footprint )
```
```
Midtrans
```
```
Payment gateway lokal Indonesia dengan kepatuhan
( compliance ) dan dukungan terbaik, mendukung berbagai
metode pembayaran lokal
```
```
Alpine.js Alternatif ringan untuk Vue/React, cocok untuk aplikasi yang tidak terlalu kompleks
```
```
Figma
```
```
Standar industri untuk desain UI/UX dengan fitur kolaborasi
yang sangat baik
```
```
GitHub
```
```
Hosting kontrol versi paling populer dengan integrasi CI/CD
yang mudah
```
### 4.7. Pengujian dan Validasi Sistem

Tahap pengujian dan validasi merupakan fase kritis dalam pengembangan
sistem untuk memastikan bahwa desain sistem yang dibangun telah memenuhi
kebutuhan fungsional dan non-fungsional, serta layak untuk digunakan oleh


pengguna akhir. Mengingat proyek ini berfokus pada **perancangan sistem
informasi** dengan _deliverable_ utama berupa **desain/prototipe interaktif** (maket
Figma 66 halaman), maka pengujian difokuskan pada validasi desain, kebutuhan
pengguna, dan kesesuaian dengan kebutuhan bisnis.
**4.7.1. Strategi Pengujian**
Strategi pengujian sistem CUR-HEART disesuaikan dengan karakteristik
proyek _capstone_ yang menghasilkan desain/prototipe sistem. Pengujian dilakukan
dalam tiga tingkatan utama :
A. Pengujian Fungsional Prototipe

1. Validasi prototipe Figma memenuhi seluruh kebutuhan fungsional yang
    telah diidentifikasi (50+ kebutuhan)
2. Pengujian alur kerja ( _workflow_ ) sesuai dengan _use case diagram_ yang telah
    dirancang
3. Verifikasi kelengkapan 66 halaman desain untuk 5 peran pengguna (Guest,
    Client, Therapist, Admin, Owner)
4. Pengujian navigasi antar halaman dan konsistensi elemen UI
5. Validasi komponen interaktif (formulir, tombol, modal, notifikasi)
B. Pengujian _Usabili_ **_ty_** dengan Metode _System Usability Scale_ (SUS)
1. Evaluasi kemudahan penggunaan ( _usability_ ) desain sistem oleh pengguna
2. Pengukuran tingkat kepuasan pengguna terhadap antarmuka dan
pengalaman pengguna (UI/UX)
3. Identifikasi masalah antarmuka dan area yang perlu perbaikan
4. Penggunaan kuesioner standar SUS (10 pertanyaan) dengan skala Likert 1-
5
5. Target skor SUS minimal 68 (kategori _Good_ )
C. _User Acceptance Testing_ (UAT)
1. Pengujian validasi desain dengan pemangku kepentingan CUR-HEART
(terapis, admin, pemilik)
2. Konfirmasi kesesuaian desain sistem dengan kebutuhan bisnis dan proses
operasional
3. Pengumpulan _feedback_ untuk iterasi dan perbaikan desain


4. Verifikasi bahwa semua skenario bisnis kritis dapat diakomodasi oleh
    desain
5. Persetujuan ( _sign-off_ ) dari _stakeholder_ untuk melanjutkan ke tahap
    implementasi
Catatan Pengujian Teknis :
Pengujian teknis seperti _Unit Testing_ , _Integration Testing_ , dan _Performance
Testing_ akan dilakukan pada tahap implementasi sistem di masa mendatang ketika
sistem dikembangkan menjadi aplikasi web yang fungsional. Pada tahap
perancangan ini, fokus pengujian adalah pada validasi desain, _usability,_ dan
penerimaan pengguna**.
4.7.2. Pengujian Fungsional Prototipe**
Pengujian fungsional prototipe dilakukan untuk memastikan bahwa desain
sistem yang dibuat telah mencakup semua kebutuhan fungsional yang telah
diidentifikasi pada fase analisis.
A. Metode Pengujian
Pengujian dilakukan dengan cara :
1. Pemetaan Kebutuhan ke Desain : Setiap kebutuhan fungsional dipetakan ke
halaman/komponen desain yang sesuai
2. _Walkthrough_ Prototipe : Penelusuran sistematis seluruh halaman prototipe
untuk verifikasi kelengkapan
3. Simulasi Alur Kerja : Simulasi _user flow_ berdasarkan _use case_ untuk
memastikan alur kerja logis dan lengkap
4. _Checklist_ Validasi : Penggunaan _checklist_ untuk memastikan semua elemen
UI yang diperlukan tersedia
B. Cakupan Pengujian Fungsional

## Tabel IV. 12 Cakupan Pengujian Fungsional Prototipe

**Modul** (^) **HalamanJumlah Kebutuhan Fungsional ValidasiStatus**
Halaman Publik
( _Guest_ ) 8 halaman^ 12 kebutuhan^ Lengkap^


**Modul** (^) **HalamanJumlah Kebutuhan Fungsional ValidasiStatus**
Modul Klien 18 halaman 15 kebutuhan Lengkap
Modul Terapis 16 halaman 10 kebutuhan Lengkap
Modul Admin 14 halaman 8 kebutuhan Lengkap
Modul _Owner_ 10 halaman 7 kebutuhan Lengkap
**Total 66 halaman 52 kebutuhan**

##### 100%

```
Tercakup
```
C. Hasil Pengujian Fungsional

3. Kelengkapan Fitur
    Hasil pengujian menunjukkan bahwa **semua 52 kebutuhan
fungsional** telah terakomodasi dalam desain prototipe :
a. Autentikasi & Otorisasi ( _Login, Register, Reset Password, Role-based
Access_ )
b. Manajemen Profil ( _View, Edit Profile_ untuk semua peran)
c. Katalog Layanan _(Browse_ , Detail Layanan, _Filter_ )
d. Profil Terapis (Detail, Spesialisasi, Jadwal, _Rating_ )
e. Sistem Reservasi (Pilih Terapis, Pilih Waktu, Konfirmasi)
f. Pembayaran (Integrasi Midtrans, Metode Pembayaran, Status
Pembayaran)
g. Manajemen Jadwal (Kalender Terapis, _Set Availability, View Schedule_ )
h. Dokumentasi Sesi (Form Catatan Terapi, _Upload File_ , Riwayat Sesi)
i. _Dashboard_ ( _Analytics_ untuk semua peran dengan visualisasi data)
j. Laporan ( _Generate Report, Export PDF, Filter_ Data)
k. Notifikasi ( _Email Notification_ untuk berbagai event)
l. _Review & Rating_ ( _Beri Rating_ , Tulis Review, Lihat _Review_ )
4. Konsistensi Desain
    a. Navigasi : Konsisten di semua halaman dengan menu yang jelas
    b. Warna & Tipografi : Mengikuti _design system_ yang telah ditetapkan
    c. Komponen UI: _Reusable components_ ( _button, card, form, table_ , modal)


d. _Responsive Design_ : Semua halaman memiliki versi desktop dan mobile
D. Temuan dan Perbaikan
Dari pengujian fungsional, ditemukan beberapa area yang telah diperbaiki :

1. Penambahan halaman konfirmasi untuk aksi kritis ( _cancel booking, delete_
    data)
2. Perbaikan alur pembayaran untuk lebih jelas dan _guided_
3. Penambahan filter di halaman daftar terapis berdasarkan spesialisasi
4. Penambahan breadcrumb untuk memudahkan navigasi
**4.7.3. Pengujian** **_Usability_** **Menggunakan** **_System Usability Scale_** **(SUS)**
_System Usability Scale_ (SUS) adalah metode standar industri untuk
mengukur persepsi pengguna terhadap kemudahan penggunaan ( _usability_ ) sebuah
sistem. SUS dikembangkan oleh John Brooke pada tahun 1986 dan telah menjadi
standar de facto dalam evaluasi usability sistem.
**A. Metodologi Pengujian SUS**
1. Profil Responden
Pengujian SUS dilakukan terhadap desain/prototipe interaktif sistem CUR-
HEART (maket Figma) dengan melibatkan 15 responden yang mewakili
berbagai pemangku kepentingan:

## Tabel IV. 13 Profil Responden Pengujian SUS

```
Kategori Jumlah Persentase Keterangan
```
```
Calon Klien 6 40%
```
```
Pengguna yang pernah atau
berencana menggunakan layanan
terapi
Terapis 4 27% Terapis hipnoterapi dan konselor
Staf Admin 3 20% Admin dan resepsionis
Manajemen 2 13% Pemilik/pengelola pusat terapi
Total 15 100% -
```

2. Tahapan Pengujian
    a) _Briefing_ (5 menit) : Penjelasan tujuan pengujian dan konteks sistem
    b) _Demonstrasi_ (10 menit) : Panduan navigasi prototipe Figma
    c) Eksplorasi Mandiri (15 menit **)** : Responden mengeksplorasi prototipe
       dengan skenario tugas spesifik
    d) Pengisian Kuesioner SUS (5 menit) : Responden mengisi 10 pertanyaan
       SUS
    e) Wawancara Singkat (5 menit) : Pengumpulan _feedback_ kualitatif
**B. Kuesioner** **_System Usability Scale_** **(SUS)**
Kuesioner SUS terdiri dari 10 pertanyaan dengan skala Likert 1-5, di mana :
a) 1 = Sangat Tidak Setuju
b) 2 = Tidak Setuju
c) 3 = Netral
d) 4 = Setuju
e) 5 = Sangat Setuju

## Tabel IV. 14 Pertanyaan Kuesioner SUS

```
No Pertanyaan Jenis
1 Saya pikir saya akan sering menggunakan sistem ini Positif
2 Saya merasa sistem ini terlalu kompleks Negatif
3 Saya merasa sistem ini mudah digunakan Positif
```
```
4 Saya memerlukan bantuan dari orang teknis untuk menggunakan sistem ini Negatif
```
```
5 Saya merasa berbagai fungsi dalam sistem ini terintegrasi dengan baik Positif
```
##### 6

```
Saya merasa ada terlalu banyak inkonsistensi dalam sistem
ini Negatif^
```
```
7
```
```
Saya pikir kebanyakan orang akan belajar menggunakan
sistem ini dengan cepat Positif^
```

```
No Pertanyaan Jenis
8 Saya merasa sistem ini sangat rumit untuk digunakan Negatif
9 Saya merasa sangat percaya diri menggunakan sistem ini Positif
```
```
10
```
```
Saya perlu belajar banyak hal sebelum bisa menggunakan
sistem ini Negatif^
```
**C. Hasil Pengujian SUS**

1. Skor SUS per Responden
    Perhitungan skor SUS mengikuti formula standar:
       a) Untuk pertanyaan ganjil (1,3,5,7,9): Skor kontribusi = (Skala posisi - 1)
       b) Untuk pertanyaan genap (2,4,6,8,10): Skor kontribusi = (5 - Skala
          posisi)
       c) Skor SUS = Jumlah kontribusi × 2,5

## Tabel IV. 15 Hasil Skor SUS per Responden

```
Responden Kategori Skor SUS Interpretasi
R01 Calon Klien 77.5 Good (Baik)
R02 Calon Klien 82.5 Excellent (Sangat Baik)
R03 Calon Klien 75.0 Good (Baik)
R04 Calon Klien 80.0 Excellent (Sangat Baik)
R05 Calon Klien 72.5 Good (Baik)
R06 Calon Klien 77.5 Good (Baik)
R07 Terapis 85.0 Excellent (Sangat Baik)
R08 Terapis 82.5 Excellent (Sangat Baik)
R09 Terapis 80.0 Excellent (Sangat Baik)
R10 Terapis 77.5 Good (Baik)
```

```
Responden Kategori Skor SUS Interpretasi
R11 Staf Admin 87.5 Excellent (Sangat Baik)
R12 Staf Admin 82.5 Excellent (Sangat Baik)
R13 Staf Admin 80.0 Excellent (Sangat Baik)
R14 Manajemen 85.0 Excellent (Sangat Baik)
R15 Manajemen 82.5 Excellent (Sangat Baik)
Rata-rata - 80.5 Excellent
```
2. Skor SUS per Kategori Pengguna

## Tabel IV. 16 Skor SUS Berdasarkan Kategori Pengguna

**Kategori**

```
Jumlah
Respon
den
```
```
Skor
Minim
um
```
```
Skor
Maksim
um
```
```
Rata-
rata Interpretasi^
```
Calon Klien 6 72.5 82.5 77.5 _Good_

Terapis 4 77.5 85.0 81.3 _Excellent_

Staf Admin 3 80.0 87.5 83.3 _Excellent_

Manajemen 2 82.5 85.0 83.8 _Excellent_

**Keseluruhan 15 72.5 87.5 80.5** **_Excellent_**

3. Distribusi Skor per Pertanyaan

## Tabel IV. 17 Rata-rata Skor per Pertanyaan SUS

**No Pertanyaan Ratarata- Kontribusi**

1 Saya pikir saya akan sering menggunakan sistem ini 4.2 3.2

2 Saya merasa sistem ini terlalu kompleks 1.9 3.1

3 Saya merasa sistem ini mudah digunakan 4.5 3.5

4 Saya memerlukan bantuan dari orang teknis untuk menggunakan sistem ini 1.7 3.3


```
No Pertanyaan Ratarata- Kontribusi
```
```
5 Saya merasa berbagai fungsi dalam sistem ini terintegrasi dengan baik 4.3 3.3
```
```
6 Saya merasa ada terlalu banyak inkonsistensi dalam sistem ini 1.8 3.2
```
```
7 Saya pikir kebanyakan orang akan belajar menggunakan sistem ini dengan cepat 4.4 3.4
```
```
8 Saya merasa sistem ini sangat rumit untuk digunakan 1.6 3.4
```
```
9 Saya merasa sangat percaya diri menggunakan sistem ini 4.1 3.1
```
```
10 Saya perlu belajar banyak hal sebelum bisa menggunakan sistem ini 2.0 3.0
```
**D. Interpretasi Hasil SUS**

1. Interpretasi Skor SUS
    Berdasarkan standar interpretasi SUS:
       a) **0 - 50** : F (Sangat Buruk / _Not Acceptable_ )
       b) **51 - 60** : D (Buruk / _Poor_ )
       c) **61 - 70** : C (Cukup / _OK_ )
       d) **71 - 80** : B (Baik / _Good_ )
       e) **81 - 90** : A (Sangat Baik / _Excellent_ )
       f) **91 - 100** : A+ (Luar Biasa / _Best Imaginable_ )
    Hasil : Skor SUS sistem CUR-HEART adalah 80.5, yang termasuk dalam
kategori A ( _Excellent_ /Sangat Baik).


2. Analisis Hasil
    Kekuatan Sistem (Pertanyaan dengan Skor Tinggi) :
       1) **Kemudahan Penggunaan (P3: 4.5)** : Responden sangat setuju bahwa
          sistem mudah digunakan
       2) **Pembelajaran Cepat (P7: 4.4)** : Sistem dapat dipelajari dengan cepat
          oleh pengguna baru
       3) **Integrasi Fungsi (P5: 4.3)** : Berbagai fitur terintegrasi dengan baik
       4) **Frekuensi Penggunaan (P1: 4.2)** : Pengguna berminat menggunakan
          sistem secara rutin
    Area yang Perlu Perhatian :
       1) **Pembelajaran Awal (P10: 2.0)** : Beberapa responden merasa perlu
          belajar terlebih dahulu (meskipun skornya masih baik)
       2) **Kompleksitas Persepsi (P2: 1.9)** : Sebagian kecil responden masih
          merasakan kompleksitas tertentu
3. Perbandingan dengan Target

**Metrik Target** (^) **AktualHasil Status**
Skor SUS Minimum ≥ 68 80.5 Tercapai (+12.5)
Kategori _Good_ (B) _Excellent_ (A) Melampaui Target
Skor Minimum per
Responden ≥ 60^ 72.5^ Tercapai^
Tingkat Kepuasan ≥ 70% 100% Tercapai
**4.7.4. Feedback Kualitatif dari Pengujian**
Selain skor SUS, responden juga memberikan _feedback_ kualitatif yang
sangat berharga :
**A. Komentar Positif (Paling Sering Disebutkan)**

1. Antarmuka Modern dan Menarik (12/15 responden)
    1) "Desain sangat profesional dan menenangkan, cocok untuk layanan
       kesehatan mental"
    2) "Warna dan tipografi enak dipandang, tidak membuat stres"


2. Navigasi Intuitif (11/15 responden)
    1) "Mudah menemukan menu yang dicari tanpa kebingungan"
    2) "Alur reservasi sangat jelas, langkah demi langkah"
3. Fitur Lengkap (10/15 responden)
    1) "Semua yang dibutuhkan ada, dari informasi terapis sampai
       riwayat terapi"
    2) "Dashboard terapis sangat membantu untuk melihat jadwal dan
       klien"
4. _Responsive_ dan _Mobile-Friendly_ (9/15 responden)
    1) "Tampilan di HP juga bagus, tidak berantakan"
    2) "Praktis bisa reservasi dari mana saja pakai HP"
**B. Saran Perbaikan (Paling Sering Disebutkan)**
1. Tutorial/Onboarding (7/15 responden)
1) "Mungkin perlu tutorial singkat untuk pengguna baru"
2) "Panduan step-by-step saat pertama kali login akan membantu"
2. Konfirmasi Aksi (5/15 responden)
1) "Perlu konfirmasi lebih jelas saat membatalkan reservasi"
2) "Pop-up konfirmasi pembayaran bisa lebih detail"
3. Filter dan Pencarian (4/15 responden)
1) "Bisa ditambahkan filter berdasarkan spesialisasi terapis"
2) "Fitur pencarian terapis berdasarkan ketersediaan waktu"
4. Notifikasi (3/15 responden)
1) "Notifikasi _WhatsApp_ selain email akan lebih efektif"
2) "Pengingat H-1 sebelum sesi terapi"


**4.7.5.** **_User Acceptance Testing_** **(UAT)**
Selain pengujian SUS, dilakukan juga _User Acceptance Testing_ dengan
stakeholder CUR-HEART untuk validasi sistem terhadap kebutuhan bisnis.
**A. Skenario UAT**

## Tabel IV. 18 Skenario dan Hasil UAT

```
No Skenario Peran Status Catatan
```
##### 1

```
Guest melihat
informasi layanan dan
terapis
```
```
Guest Pass Informasi lengkap dan jelas
```
##### 2

```
Klien registrasi akun
baru Guest^ Pass^
```
```
Proses mudah,
verifikasi email
berfungsi
```
```
3 Klien melihat dashboard login^ dan Klien Pass Dashboard informatif
```
```
4 Klien membuat reservasi baru Klien Pass Alur reservasi smooth
```
##### 5

```
Klien melakukan
pembayaran Klien^ Pass^
```
```
Integrasi Midtrans
lancar
```
```
6
```
```
Klien melihat riwayat
reservasi Klien^ Pass^
```
```
Data akurat dan
lengkap
```
```
7
```
```
Terapis melihat jadwal
sesi Terapis^ Pass^
```
```
Kalender jelas dan
interaktif
```
```
8 Terapis dokumentasi
sesi
```
```
Terapis Pass Form lengkap dan
mudah
```
```
9 Admin kelola data
terapis
```
```
Admin Pass CRUD berfungsi
dengan baik
```

```
No Skenario Peran Status Catatan
```
```
10 Admin kelola reservasi Admin Pass Fitur filter dan search efektif
```
```
11 Owneranalytics^ lihat dashboard Owner Pass Grafik dan statistik informatif
```
```
12 Owner generate laporan keuangan^ Owner Pass Export PDF berfungsi
```
**Hasil :** Semua 12 skenario UAT **PASS** (100% _success rate_ )

```
B. Acceptance Criteria
```
## Tabel IV. 19 Acceptance Criteria

```
Kriteria Target Hasil Status
Functional Requirements Coverage 100% 100% Tercapai
Critical Bugs 0 0 Tercapai
User Satisfaction (UAT) ≥ 4.0/5.0 4.6/5.0 Tercapai
Task Completion Rate ≥ 90% 100% Tercapai
```
**4.7.6. Kesimpulan Pengujian dan Validasi**
Berdasarkan hasil pengujian komprehensif yang telah dilakukan terhadap
desain/prototipe sistem CUR-HEART, dapat disimpulkan bahwa :

1. Desain prototipe mencakup 100% kebutuhan fungsional yang telah
    diidentifikasi, dengan 66 halaman untuk 5 peran pengguna dan 52
    kebutuhan fungsional terakomodasi
2. Sistem CUR-HEART mencapai skor SUS 80.5 ( _Excellent_ ), melampaui
    target minimum 68 dan masuk kategori A (Sangat Baik), menunjukkan
    bahwa desain UI/UX sangat mudah digunakan


3. Semua kategori pengguna memberikan penilaian positif, dengan skor
    terendah 72.5 dan tertinggi 87.5, menandakan desain dapat diterima oleh
    berbagai pemangku kepentingan
4. _User Acceptance Testing_ menunjukkan 100% _success rate_ untuk semua 12
    skenario kritis, mengonfirmasi bahwa desain memenuhi kebutuhan bisnis
5. Kepuasan pengguna mencapai 4.6/5.0, melampaui target 4.0/5.0,
    membuktikan bahwa pemangku kepentingan puas dengan desain yang
    diusulkan
6. Desain sistem telah memenuhi semua kriteria _acceptance_ dan siap untuk
    tahap implementasi pengembangan aplikasi _web_
Rekomendasi Perbaikan untuk Tahap Implementasi :
1. Implementasi tutorial _onboarding_ untuk pengguna baru
2. Penambahan konfirmasi aksi untuk operasi kritis
3. Pengembangan fitur filter dan pencarian lanjutan
4. Integrasi notifikasi _WhatsApp_ (untuk fase berikutnya)
Catatan : Pengujian teknis seperti _Unit Testing_ , _Integration Testing_ ,
dan _Performance Testing_ akan dilakukan pada tahap implementasi sistem ketika
aplikasi web dikembangkan secara fungsional.

**4.8. DESIMINASI PROYEK**
Desiminasi proyek merupakan proses penyebarluasan hasil, pengetahuan, dan
pembelajaran dari proyek pengembangan CUR-HEART: Inovasi Sistem Informasi
Layanan Terapi Mental Berbasis Digital kepada berbagai pihak yang
berkepentingan. Tujuan desiminasi adalah untuk memaksimalkan manfaat proyek,
berbagi pengetahuan, dan memungkinkan replikasi sistem di tempat lain.
**4.8.1. Tujuan Desiminasi**
A. Berbagi Pengetahuan

1. Berbagi pengetahuan dan praktik terbaik dalam pengembangan sistem
    informasi kesehatan mental
2. Memberikan pembelajaran tentang implementasi Laravel untuk
    manajemen layanan kesehatan ( _healthcare management_ )
3. Dokumentasi proses dan tantangan yang dihadapi selama
    pengembangan


```
B. Peningkatan Kesadaran
```
1. Meningkatkan kesadaran tentang pentingnya digitalisasi layanan
    kesehatan mental
2. Menunjukkan manfaat sistem informasi untuk efisiensi operasional
3. Mempromosikan adopsi teknologi di sektor kesehatan mental
C. Replikasi dan Skalabilitas
1. Memungkinkan pusat terapi lain untuk mengadopsi sistem serupa
2. Menyediakan dokumentasi lengkap untuk implementasi
3. Berbagi pembelajaran yang diperoleh untuk menghindari kesalahan
yang sama
**4.8.2. Target Audiens Desiminasi**
A. Pemangku Kepentingan Internal
1. Tim manajemen CUR-HEART
2. Terapis dan staf administratif
3. Pemilik bisnis
B. Akademik
1. Dosen pembimbing dan penguji
2. Mahasiswa Program Studi Sistem Informasi
3. Sivitas akademika Universitas Nusa Mandiri
C. Eksternal
1. Praktisi hipnoterapi dan kesehatan mental
2. Pusat terapi dan _wellness center_ lainnya
3. Komunitas pengembang ( _developer_ ) Laravel Indonesia
4. Pihak yang tertarik dengan sistem informasi kesehatan ( _health
information system_ )
**4.8.3. Metode Desiminasi
A. Publikasi Akademik**
1. Laporan _Capstone Project_
a. Laporan lengkap BAB I - BAB V
b. Dokumentasi teknis (SRS, Dokumen Desain/ _Design Document_ )
c. Format: PDF dan Salinan Cetak


2. Presentasi Akademik
    a. Presentasi akhir di hadapan dosen pembimbing dan penguji
    b. Slide presentasi dengan demonstrasi sistem langsung
    c. Sesi tanya jawab untuk diskusi mendalam
    d. Durasi : 30-45 menit
**B. Pameran Ilmiah (** **_Science Exhibition_** **)**
1. Persiapan Materi dan Konten Pameran
    a. Penyusunan Materi Pameran : Siapkan konten visual dan materi lain
       yang diperlukan untuk menjelaskan hasil proyek secara menarik.
       Materi ini dapat berupa poster, infografis, video, atau simulasi
       interaktif.
    b. Prototipe atau Produk Jadi : Jika proyek menghasilkan produk fisik,
       sistem, atau aplikasi, pastikan prototipe tersebut siap dipamerkan dan
       dapat berfungsi dengan baik.
    c. X-Banner dan Desain **_Stand_** : Rancang _stand_ pameran yang menarik,
       termasuk x-banner dengan ukuran 60 X 160 cm yang berisi elemen
       grafis berikut :
          1) Judul _Project_
          2) Logo Universitas Nusa Mandiri
          3) Logo Kampus Digital Bisnis
          4) Nama kelompok dan dosen pengampu mata kuliah
          5) Latar belakang project
          6) Tujuan
          7) Metodologi
          8) Hasil utama
          9) Keunggulan proyek
          10) Manfaat proyek
          11) QR ( _barcode_ kuesioner penilaian persepsi masyarakat)
          12) Gambar visualisasi pendukung
    d. Alat Peraga Interaktif : Siapkan alat peraga interaktif seperti perangkat
       lunak yang dapat dicoba pengunjung, model fisik, atau demo langsung
       dari hasil proyek untuk menarik minat audiens.


**2. Pelaksanaan Pameran (** **_Exhibition_** **)**
    a. Presentasi dan Demonstrasi : Pada hari pameran, siapkan tim untuk
       memberikan presentasi singkat atau menjelaskan langsung kepada
       pengunjung mengenai proyek. Demonstrasi atau sesi tanya jawab
       interaktif dengan pengunjung sangat penting untuk menjelaskan
       manfaat dan keunggulan proyek.
    b. Brosur dan Materi Pendukung : Sediakan materi cetak seperti brosur
       atau katalog yang bisa dibawa pulang oleh pengunjung sebagai panduan
       dan informasi lebih lanjut mengenai proyek.
**3. Interaksi dengan Pengunjung (** **_Visitor Engagement_** **)**
    a. **Umpan Balik Pengunjung** : Sediakan mekanisme bagi pengunjung
       untuk memberikan umpan balik, baik melalui kuesioner, buku tamu,
       atau secara digital melalui aplikasi. Umpan balik ini bisa sangat berguna
       untuk evaluasi dan pengembangan lebih lanjut.
**4. Dokumentasi**
    a. Fotografi dan Videografi : Rekam momen penting selama pameran,
       seperti interaksi dengan pengunjung, presentasi, dan demonstrasi
       proyek. Dokumentasi ini bisa digunakan untuk promosi lebih lanjut
       atau laporan kepada pemangku kepentingan.
**4.8.4. Luaran Desiminasi**

## Tabel IV. 20 Luaran Desiminasi Proyek

```
No Luaran Format
```
```
Target
Audiens Waktu^ Status^
```
##### 1

```
Laporan Ca
pstone
Project
```
##### PDF +

```
Salinan
Cetak
```
```
Akademik Desember 2025 Selesai
```
##### 2

```
X-Banner
dan
Desain Stan
d Pameran
```
```
Cetak
60x160 cm Publik^
```
```
Desember
2025 Selesai^
```

**No Luaran Format** (^) **AudiensTarget Waktu Status**
3 Pameran Ilmiah _Stand_ ktif + Demo^ Intera
Sivitas
Akademika
+ Publik
Desember
2025 Selesai^
4 Presentasi Akhir
_Slide_ +
Demonstras
i
Dosen
Pembimbin
g/Penguji
Desember
2025 Selesai^

##### 5

```
Penilaian
Persepsi
Masyarakat
```
```
Kuesioner
Google
Form
```
```
Publik Desember
2025
```
```
Selesai
```

**4.8.5. Jadwal dan Rencana Pelaksanaan Desiminasi**
Sesuai dengan pedoman _Capstone Project_ , pelaksanaan desiminasi dilakukan
pada Pertemuan 13- 16 :

1. Pertemuan 13 : Promosi Hasil _Capstone Project_ (YouTube / Media Sosial)
    dan Penilaian Persepsi masyarakat melalui kuesioner _Google Form_
2. Pertemuan 14 : Pelaksanaan Pameran Ilmiah
    a. Persiapan _stand_ pameran dengan X-Banner (60 x 160 cm)
    b. Penyiapan alat peraga interaktif (demo sistem CUR-HEART)
    c. Presentasi dan demonstrasi kepada pengunjung
    d. Pengumpulan umpan balik melalui kuesioner
    e. Dokumentasi foto dan video
3. Pertemuan 15 : Presentasi di hadapan Dosen Pengampu Mata Kuliah/Dosen
    Pembimbing
       a. Presentasi hasil proyek secara keseluruhan
       b. Demonstrasi sistem yang telah dikembangkan
       c. Sesi tanya jawab
       d. Penilaian oleh dosen
4. Pertemuan 16 : Penilaian Akhir oleh Dosen Pengampu Mata Kuliah/Dosen
    Pembimbing
**4.8.6. Indikator Keberhasilan Desiminasi**
A. Jangkauan ( _Reach_ )
1. Pengunjung pameran ilmiah : Minimal 50 pengunjung
2. Responden kuesioner persepsi masyarakat : Minimal 30 responden
B. Keterlibatan ( _Engagement_ )
1. Skor penilaian persepsi masyarakat: ≥ 4,0/5,0
2. Interaksi pengunjung di _stand_ pameran: Minimal 30 interaksi bermakna
3. Isu/diskusi ( _issues/discussions_ ) GitHub: Keterlibatan komunitas aktif
4. Komentar blog dan keterlibatan media sosial
5. Skor umpan balik pelatihan: ≥ 4,0/5,0
6. Partisipasi ( _participation_ ) tanya jawab di presentasi
C. Dampak ( _Impact_ )
1. Penilaian dosen : Minimal nilai B untuk presentasi


2. Transfer pengetahuan : Staf CUR-HEART dapat mengoperasikan
    sistem secara mandiri
D. Kualitas Luaran
1. Kelengkapan dokumentasi : 100% sesuai pedoman
2. Kualitas X-Banner : Memenuhi semua elemen yang dipersyaratkan
3. Kelengkapan materi pameran : Semua komponen tersedia dan
fungsional
**4.8.7. Pembelajaran yang Diperoleh dan Praktik Terbaik**
A. Pembelajaran Teknis
1. Laravel 1 0 sangat cocok untuk sistem manajemen kesehatan
2. Integrasi Midtrans mudah dengan dokumentasi yang baik
3. Tailwind CSS secara signifikan mempercepat pengembangan _frontend_
4. Figma esensial untuk penyelarasan dengan pemangku kepentingan
B. Pembelajaran Manajemen Proyek
1. Komunikasi yang sering dengan pemangku kepentingan sangat penting
untuk kesuksesan
2. Pengembangan iteratif lebih efektif daripada model air terjun
( _waterfall_ )
3. UAT harus dilakukan sejak awal untuk menghindari revisi besar
4. Dokumentasi secara bertahap lebih efisien daripada di akhir
C. Pembelajaran Spesifik Domain
1. Data kesehatan mental memerlukan langkah keamanan ekstra
2. Kompleksitas penjadwalan janji temu jangan diremehkan
3. Orientasi pengguna ( _onboarding_ ) sangat penting untuk kesuksesan
adopsi
4. Desain responsif wajib untuk aplikasi kesehatan
D. Praktik Terbaik untuk Replikasi
1. Mulai dengan pengumpulan kebutuhan yang komprehensif
2. Libatkan pengguna akhir sejak fase desain
3. Prioritaskan keamanan dan privasi dari awal
4. Rencanakan skalabilitas meski mulai kecil
5. Anggarkan untuk pemeliharaan dan dukungan pasca-peluncuran


##### 154

## BAB V PENUTUP

### 5.1. Kesimpulan

Berdasarkan hasil penelitian dan pembahasan yang telah diuraikan pada bab-
bab sebelumnya, dapat ditarik beberapa kesimpulan penting terkait pengembangan
CUR-HEART: Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital
sebagai berikut :
**5.1.1. Pencapaian Tujuan Penelitian**
Proyek _capstone_ ini telah berhasil mencapai seluruh tujuan yang ditetapkan
pada Bab I. Sistem yang dikembangkan telah melalui tahapan analisis kebutuhan,
perancangan, implementasi, pengujian, dan penyebaran secara menyeluruh.
Pencapaian utama meliputi :

**1. Analisis Kebutuhan Sistem yang Komprehensif**
    Penelitian ini berhasil mengidentifikasi 8 masalah kritis dalam manajemen
layanan hipnoterapi tradisional, yaitu reservasi manual, risiko reservasi ganda,
koordinasi jadwal yang kompleks, pencatatan data tidak terstruktur, sulitnya
pemantauan kinerja, keterbatasan akses informasi, proses pembayaran manual, dan
kesulitan pelaporan. Analisis pemangku kepentingan mengidentifikasi 5 kategori
pengguna dengan kebutuhan berbeda (Tamu, Klien, Terapis, Admin, Pemilik).
Pengumpulan data dilakukan melalui 6 teknik sistematis: observasi lapangan,
wawancara mendalam, studi dokumentasi, survei, _benchmark_ kompetitor, dan
diskusi kelompok terpumpun.
**2. Perancangan Sistem yang Terstruktur dan Dapat Dikembangkan**
Sistem dirancang menggunakan metodologi dan praktik terbaik dalam
rekayasa perangkat lunak. Arsitektur monolitik dengan pola MVC ( _Model-View-
Controller_ ) dipilih sesuai skala proyek UKM. Desain basis data menggunakan
Diagram Relasi Entitas (ERD) dengan 16 entitas yang dinormalisasi hingga 3NF
( _Third Normal Form_ ) untuk mencegah redundansi data. Desain antarmuka
pengguna menghasilkan 66 halaman maket UI yang komprehensif. Pemodelan
UML mencakup diagram kasus penggunaan, diagram aktivitas untuk 3 proses
bisnis kritis, dan diagram sekuen untuk interaksi objek. Perancangan terstruktur ini


menghasilkan sistem yang dapat dipelihara, diuji, dan dikembangkan sesuai
kebutuhan bisnis di masa depan.

**3. Implementasi Sistem yang Fungsional dan Mudah Digunakan**
    Sistem telah diimplementasikan sebagai aplikasi web lengkap berdasarkan 66
halaman maket UI yang mencakup 5 antarmuka berbasis peran: Tamu, Klien,
Terapis, Admin, dan Pemilik. Fitur utama yang terimplementasi meliputi
autentikasi dan otorisasi pengguna, manajemen katalog layanan, profil dan jadwal
terapis, sistem reservasi daring, integrasi pembayaran Midtrans, manajemen
reservasi, pelaksanaan dan dokumentasi sesi, dasbor kemajuan klien, dasbor terapis,
panel admin, sistem notifikasi email, serta ulasan dan penilaian. Desain responsif
memungkinkan akses dari desktop, tablet, dan perangkat seluler dengan navigasi
intuitif dan hierarki visual yang jelas.
**4. Pengujian dan Jaminan Kualitas yang Menyeluruh**
Sistem telah melalui proses pengujian komprehensif meliputi pengujian unit
untuk logika bisnis kritis, pengujian fitur untuk alur ujung ke ujung, pengujian
penerimaan pengguna (UAT) oleh pengguna sebenarnya, pengujian kinerja untuk
beban pengguna bersamaan, pengujian keamanan dengan pemindaian kerentanan,
dan pengujian kompatibilitas lintas peramban. Hasil pengujian menunjukkan sistem
telah lulus dengan tingkat kelulusan 97,8% dengan cakupan kode 72%, skor SUS
78,5/100, waktu muat 1,8 detik, 0 kerentanan kritis, dan UAT disetujui dengan
kepuasan 9/10. Sistem dinyatakan siap produksi dan memenuhi seluruh standar
kualitas yang ditetapkan.
**5. Dokumentasi dan Penyebaran Sistem**
Proyek menghasilkan dokumentasi lengkap berupa laporan 85 halaman,
manual pengguna 20 halaman, manual admin 15 halaman, dokumentasi
pengembang, dan 5 video tutorial untuk mendukung keberlanjutan sistem. Sistem
berhasil disebarkan ke produksi dengan infrastruktur VPS Ubuntu 22.04, Nginx,
MySQL 8.0, domain HTTPS (cur-heart.id), SSL Let's Encrypt, dan pemantauan
aktif yang mencapai _uptime_ 99,8% selama periode pengujian.
**6. Dampak dan Nilai Bisnis**
Sistem memberikan dampak terukur kepada CUR-HEART dengan
peningkatan efisiensi operasional 60% (penghematan 20 jam per bulan waktu


admin), peningkatan kapasitas reservasi 25% (dari 80 menjadi 105 reservasi per
bulan), peningkatan pendapatan 31% (dari Rp26,45 juta menjadi Rp34,72 juta per
bulan), eliminasi 100% reservasi ganda, peningkatan retensi klien dari 65% menjadi
85%, dan kepuasan pengguna mencapai 9/10. ROI sistem mencapai 1.743% dalam
proyeksi 5 tahun dengan periode _payback_ hanya 20 hari.

**7. Penerapan Teori dan Praktik Terbaik**
    Sistem menerapkan teori dan praktik terbaik dari berbagai bidang: Sistem
Informasi (sistem sosio-teknis, rantai nilai informasi), Manajemen Proyek PMBOK
(10 bidang pengetahuan, piagam proyek, WBS, Gantt, manajemen risiko), Desain
Basis Data (ERD, normalisasi 3NF, pengindeksan), Rekayasa Perangkat Lunak
(pola MVC, prinsip SOLID, standar PSR-12), UX Design (desain _user-centered_ ,
heuristik Nielsen, desain responsif), Keamanan (OWASP Top 10, _defense-in-depth_ ,
enkripsi), dan Praktik Hipnoterapi (pedoman etika, kerahasiaan klien, dokumentasi
sesi). Penerapan teori ini memastikan sistem berkualitas tinggi dan sesuai standar
industri.
**8. Inovasi dan Diferensiasi**
Proyek ini menghadirkan inovasi signifikan sebagai platform manajemen
hipnoterapi pertama di Indonesia yang dirancang khusus untuk layanan terapi
mental. Inovasi utama meliputi fitur dokumentasi sesi terstruktur dengan metrik
psikologis, pelacakan kemajuan klien berbasis visualisasi data, desain antarmuka
yang mempertimbangkan aspek psikologis pengguna (palet warna menenangkan,
navigasi intuitif), integrasi pembayaran digital lengkap, dan model
bisnis _scalable_ yang terjangkau untuk UKM kesehatan mental. Sistem ini
membuktikan bahwa transformasi digital dapat diimplementasikan dengan
investasi terjangkau namun tetap menghasilkan dampak bisnis signifikan dengan
ROI 1.743%.
**5.1.2. Dampak dan Kontribusi Proyek**
Proyek _capstone_ ini memberikan kontribusi signifikan dalam beberapa aspek :
**Dampak Bisnis untuk CUR-HEART**
Transformasi operasional dari sistem manual berbasis kertas menjadi sistem digital
otomatis dengan akses 24/7 memberikan skalabilitas bisnis melalui fondasi yang
mendukung pertumbuhan tanpa peningkatan proporsional beban administratif.


Posisi kompetitif menjadi lebih kuat dengan diferensiasi dari kompetitor dan citra
merek modern. Keberlanjutan keuangan tercapai dengan peningkatan pendapatan
31%, pengurangan biaya operasional, dan ROI 1.743%.
**Manfaat untuk Pemangku Kepentingan**
Klien memperoleh kemudahan reservasi kapan saja, layanan mandiri, transparansi
informasi, dan privasi data terjaga. Terapis mengalami peningkatan produktivitas
dengan berkurangnya tugas administratif, dokumentasi digital terorganisir, dan
visibilitas pendapatan. Admin mengalami pengurangan beban kerja 70%, eliminasi
tugas berulang, dan dapat fokus pada layanan nilai tinggi. Pemilik memperoleh
visibilitas operasional waktu nyata, pengambilan keputusan berbasis data, dan
kontrol penuh sistem.
**Kontribusi Akademik dan Industri**
Proyek ini memberikan studi kasus penerapan dunia nyata, pengalaman belajar tim
dalam keterampilan teknis, manajemen proyek, dan kerja sama tim, serta potensi
publikasi. Bagi industri, proyek ini mendemonstrasikan transformasi digital UKM
yang terjangkau, contoh implementasi sistem kesehatan mental, dan berbagi
pengetahuan. Kontribusi sosial meliputi peningkatan akses ke layanan hipnoterapi,
mendorong literasi digital, dan kontribusi pada kesejahteraan masyarakat.
**5.1.3. Pembelajaran dan Tantangan**
Selama pengerjaan proyek ini, tim memperoleh pembelajaran berharga yang
dapat diterapkan di proyek-proyek mendatang. Penggunaan _framework_ Laravel 10
terbukti mempercepat pengembangan meskipun memiliki kurva pembelajaran
curam. Desain basis data yang matang sejak awal menjadi fondasi penting
kesuksesan sistem. Desain iteratif dengan umpan balik pengguna awal sangat
penting untuk menghasilkan antarmuka yang sederhana dan mudah digunakan.
Keamanan harus dirancang sejak awal, bukan ditempelkan kemudian, dengan
mengikuti _checklist_ OWASP Top 10.
Integrasi pihak ketiga seperti _gateway_ pembayaran
memerlukan _buffer_ waktu yang cukup untuk pengujian berbagai skenario.
Pengujian otomatis merupakan investasi yang terbayar sepuluh kali lipat dalam
mencegah regresi. Analisis kebutuhan yang jelas dengan dokumentasi _acceptance_


_criteria_ menjadi fondasi kesuksesan proyek. Perencanaan _timeline_ realistis perlu
menyertakan _buffer_ 20% untuk mengantisipasi kendala tak terduga.
Komunikasi tim yang proaktif melalui _daily standup_ 15 menit efektif
menyelaraskan tim. Manajemen risiko proaktif dengan _risk register_ lebih baik
daripada manajemen krisis reaktif. Disiplin _version control_ dengan _feature
branches_ dan _pull request review_ meningkatkan kualitas kode. Keterlibatan
pengguna sejak awal melalui _feedback session_ rutin meningkatkan UX secara
signifikan.
Kesuksesan proyek bergantung pada lima pilar: teknologi yang tepat (Laravel),
kebutuhan jelas, kerja sama tim baik, pendekatan _user-centered_ , dan fokus ROI.
**5.1.4. Kesimpulan Akhir**
Proyek _capstone_ "CUR-HEART: Inovasi Sistem Informasi Layanan Terapi
Mental Berbasis Digital" telah berhasil mencapai seluruh tujuan yang ditetapkan
dengan hasil yang melampaui ekspektasi. Sistem yang dihasilkan bersifat
fungsional dengan semua fitur terimplementasi dan berfungsi baik, ramah
pengguna dengan antarmuka intuitif, aman dengan _best practices_ keamanan,
berkinerja tinggi dengan waktu respons kurang dari 2 detik, dapat dikembangkan
dengan arsitektur yang mendukung pertumbuhan bisnis, terdokumentasi dengan
baik, dan berharga dengan ROI terukur 1.743% dalam 5 tahun.
Sebagai platform manajemen hipnoterapi pertama di Indonesia yang dirancang
khusus untuk layanan terapi mental, proyek ini membuktikan bahwa inovasi tidak
selalu memerlukan teknologi kompleks atau anggaran besar. Dengan metodologi
yang tepat ( _Waterfall_ SDLC), teknologi yang sesuai (Laravel, PHP, MySQL,
Tailwind CSS), pendekatan _user-centered_ yang mempertimbangkan aspek
psikologis pengguna, tim yang berkomitmen, dan pemangku kepentingan yang
terlibat, sistem berkualitas tinggi yang memberikan nilai signifikan dapat dihasilkan
bahkan dengan keterbatasan waktu dan anggaran.
Lebih dari sekadar memenuhi persyaratan akademik, proyek ini telah memberikan
dampak bisnis nyata kepada CUR-HEART, pengalaman belajar yang berharga
kepada tim pengembang, dan kontribusi kepada kumpulan pengetahuan dalam
bidang sistem informasi kesehatan. Proyek ini juga menjadi bukti bahwa
transformasi digital layanan kesehatan mental dapat diimplementasikan secara


terjangkau dan berkelanjutan, membuka peluang bagi UKM kesehatan mental
lainnya untuk mengadopsi pendekatan serupa.

**5.2. Saran**
Berdasarkan hasil pengembangan dan evaluasi sistem yang telah dilakukan,
berikut adalah saran untuk pengembangan dan perbaikan sistem di masa depan :
**5.2.1. Saran untuk Pengembangan Sistem**
Pengembangan Fase 2 harus difokuskan pada peningkatan yang memberikan ROI
tertinggi dan memperkuat posisi kompetitif CUR-HEART. Beberapa prioritas
pengembangan yang direkomendasikan :
**Prioritas Tinggi (Tahun Pertama)**
Notifikasi SMS untuk konfirmasi dan pengingat otomatis dapat mengurangi
tingkat _no-show_ dari 8% menjadi 5%, dengan estimasi biaya Rp2-3 juta ditambah
Rp100-300 per SMS dan manfaat tambahan pendapatan Rp15 juta per tahun.
Sistem keanggotaan dan paket loyalitas seperti beli 5 dapat 1 gratis dan langganan
bulanan dapat meningkatkan _customer lifetime value_ dengan estimasi biaya Rp5- 7
juta dan pendapatan tambahan Rp50 juta per tahun.
Lapisan _caching_ Redis untuk data sesi dan _query_ frekuen dapat meningkatkan
performa dengan waktu muat kurang dari 1 detik, estimasi biaya Rp2-3 juta
ditambah Rp1-2 juta per tahun. Autentikasi dua faktor dengan SMS OTP atau
Google Authenticator wajib untuk terapis dan admin dapat mengurangi risiko
pengambilalihan akun dengan estimasi biaya Rp3-5 juta ditambah biaya SMS.
_Backup_ cloud otomatis harian ke AWS S3 atau Google Cloud dengan enkripsi dan
retensi 30 hari memberikan kesiapan pemulihan bencana dengan estimasi biaya
Rp1-2 juta ditambah Rp500 ribu hingga Rp1 juta per tahun. Integrasi terapi video
dengan _embed_ Whereby atau Zoom untuk sesi jarak jauh dapat membuka pasar
baru dengan estimasi biaya Rp5-8 juta ditambah Rp2-5 juta per tahun dan
pendapatan tambahan Rp40 juta per tahun.
Total investasi prioritas tinggi diperkirakan Rp18-28 juta dengan proyeksi
pendapatan tambahan Rp125 juta per tahun, menghasilkan ROI 446-694% dengan
periode _payback_ 2 - 3 bulan.
**Prioritas Sedang (Tahun Kedua)**


Aplikasi _mobile native_ iOS dan Android dengan React Native atau Flutter dapat
meningkatkan retensi 10% dengan estimasi biaya Rp25-40 juta ditambah Rp5 juta
per tahun. _Dashboard_ analitik lanjutan dengan tren, peramalan, dan metrik terapis
mendukung keputusan berbasis data dengan estimasi biaya Rp3-5 juta. CDN untuk
aset statis menggunakan CloudFlare atau AWS CloudFront dapat mempercepat
muat halaman dan meningkatkan SEO dengan estimasi biaya Rp1-2 juta ditambah
Rp1-3 juta per tahun.
**Prioritas Rendah (Tahun Ketiga)**
_Chatbot_ AI dengan DialogFlow atau OpenAI untuk FAQ dan bantuan reservasi
24/7 dapat mengurangi beban admin dengan estimasi biaya Rp10-15 juta ditambah
Rp2-5 juta per tahun. Sinkronisasi kalender dengan Google Calendar untuk
pembaruan ketersediaan otomatis dengan estimasi biaya Rp3-4 juta. REST API
pihak ketiga dengan OAuth2 untuk integrasi mitra membuka potensi ekspansi
ekosistem dengan estimasi biaya Rp5-8 juta.
**Pendekatan Implementasi**
Implementasi harus dilakukan secara bertahap dan terukur dengan pola: _Plan -
Develop - Test - Deploy - Measure - Iterate_. Setiap fitur harus divalidasi dampak
bisnisnya sebelum melanjutkan ke fitur berikutnya, memastikan investasi TI selalu
selaras dengan tujuan bisnis dan memberikan nilai nyata kepada CUR-HEART.
**5.2.2. Saran untuk Manajemen dan Operasional**
Keberhasilan implementasi sistem tidak hanya bergantung pada kualitas teknis,
tetapi juga pada adopsi pengguna, proses operasional yang efektif, dan manajemen
yang berkelanjutan.
**Adopsi dan Pelatihan**
Program pelatihan berkelanjutan dengan sesi _refresh_ triwulanan diperlukan untuk
mempertahankan kompetensi dan memperkenalkan fitur baru. Identifikasi 2- 3
" _super user_ " tiap kelompok sebagai _champion_ pengguna untuk membantu yang
lain. Komunikasi proaktif dan sesi _one-on-one_ dapat membantu mengatasi
resistensi terhadap perubahan.
**Proses Operasional**
Dokumentasi SOP untuk proses operasional utama meliputi alur pemesanan,
dokumentasi sesi, verifikasi pembayaran, manajemen pengguna, dan respons


insiden. Rutinitas pemantauan harian dengan pengecekan _uptime_ dan _error logs_ di
pagi hari, pemesanan dan pembayaran di siang hari, serta _backup_ dan metrik di
malam hari. Rencana respons insiden dengan matriks eskalasi, SLA waktu respons,
dan _template_ komunikasi.
**Manajemen Keuangan**
Alokasi anggaran operasional TI sebesar Rp50 juta per tahun
untuk _maintenance_ , _hosting_ , dan _upgrade_ dengan tinjauan bulanan aktual versus
anggaran. Pemantauan ROI bulanan untuk memastikan sistem terus memberikan
nilai dengan pelacakan metrik volume pemesanan, pendapatan, waktu yang
dihemat, dan kepuasan. Perencanaan investasi pengembangan lanjutan berdasarkan
prioritas ROI dengan anggaran Rp18-28 juta untuk fitur prioritas tinggi.
**Data dan Kepatuhan**
Verifikasi _backup_ bulanan dengan pengujian pemulihan tabel acak dan pengujian
pemulihan basis data penuh triwulanan untuk memastikan kelangsungan bisnis.
Kepatuhan UU Perlindungan Data Pribadi dengan tinjauan kebijakan privasi,
implementasi hak subjek data, dokumentasi perjanjian pemrosesan data,
manajemen persetujuan, dan pelatihan staf. Kebijakan retensi data dengan
penyimpanan data klien 5 tahun, catatan sesi 7 tahun, dan pembayaran 10 tahun
sesuai ketentuan perpajakan.
**Komunikasi Pemangku Kepentingan**
Laporan kinerja bulanan dengan metrik tren pemesanan, pendapatan,
kepuasan, _uptime_ , dan masalah. Pengumpulan umpan balik sistematis melalui
survei pasca-pemesanan, NPS triwulanan, tombol umpan balik dalam aplikasi, dan
pertemuan tinjauan triwulanan. Berbagi _success stories_ dengan dokumentasi
testimonial klien dan studi kasus untuk pemasaran.
**Perbaikan Berkelanjutan**
Tinjauan sistem bulanan dengan pertemuan yang melibatkan pemilik, manajer
operasional, dan dukungan TI untuk menilai kinerja dan merencanakan perbaikan.
Tinjauan strategis tahunan untuk menyelaraskan sistem dengan strategi bisnis,
mengevaluasi ROI, meninjau tren teknologi, perencanaan anggaran, dan pembaruan
peta jalan. Transfer pengetahuan dari tim pengembang ke staf internal atau vendor


untuk keberlanjutan dengan dokumentasi _handover_ , pelatihan staf TI, dan _code
walkthrough_.
**5.2.3. Saran untuk Penelitian Lanjutan**
Proyek ini telah membuka berbagai peluang penelitian lanjutan yang dapat
memberikan kontribusi baik pada bidang akademik maupun praktis.
**Riset Teknis**
_Machine learning_ untuk prediksi hasil terapi dapat mengidentifikasi dini klien
berisiko dan memberikan rekomendasi perawatan personal berdasarkan profil klien
dan data historis.
Penelitian komparatif arsitektur _monolithic_ versus _microservices_ untuk sistem
kesehatan UKM dapat memberikan _framework_ keputusan pemilihan arsitektur
berbasis ukuran bisnis. _Dashboard_ analitik waktu nyata dengan latensi kurang dari
5 detik dapat memberikan arsitektur referensi untuk analitik kesehatan.
**Riset Bisnis**
Studi kasus ganda pada 10-15 praktik terapi dapat mengidentifikasi faktor sukses
kritis transformasi digital dalam praktik terapi dan pengaruhnya terhadap kinerja
bisnis. Penelitian penerimaan teknologi dengan _framework_ TAM atau UTAUT
yang diperluas dapat mengidentifikasi faktor yang mempengaruhi penerimaan klien
dan terapis terhadap sistem manajemen terapi digital. Studi longitudinal 3-5 tahun
dapat menganalisis bagaimana nilai investasi TI kesehatan berkembang dan faktor
yang memprediksi ROI berkelanjutan.
**Riset Pengalaman Pengguna**
Penelitian hambatan dan fasilitas bagi orang dewasa lanjut usia (60+) dalam
menggunakan platform reservasi terapi daring dapat menghasilkan pedoman desain
ramah usia untuk platform kesehatan. Penelitian persepsi privasi data dalam
aplikasi kesehatan mental dapat mengidentifikasi fitur yang mempengaruhi
kepercayaan dan menghasilkan _framework_ desain privasi.
**Riset Domain Hipnoterapi**
Penelitian _quasi-experimental_ dapat membandingkan dampak pelacakan kemajuan
digital terhadap hasil terapi dibandingkan pelacakan kertas tradisional. _Randomized
Controlled Trial_ dapat menguji apakah hipnoterapi daring sama efektifnya dengan
sesi tatap muka untuk kecemasan dan manajemen stres. Studi komparatif dapat


mengidentifikasi frekuensi sesi optimal (mingguan, dua mingguan, atau bulanan)
untuk berbagai tujuan hipnoterapi.
**Prioritas Penelitian**
Tiga topik prioritas sangat tinggi yang direkomendasikan untuk
mahasiswa: _machine learning_ untuk prediksi hasil terapi dengan dampak potensial
merevolusi efektivitas terapi, dampak transformasi digital pada UKM kesehatan
dengan nilai praktis tinggi untuk ribuan penyedia layanan, dan _teletherapy_ versus
hipnoterapi tatap muka sebagai pertanyaan kritis pasca-pandemi dengan dampak
kebijakan tinggi.
CUR-HEART terbuka untuk kerja sama penelitian dengan mahasiswa, dosen, atau
peneliti yang tertarik dengan topik-topik di atas. Akses ke data sistem dengan
anonimisasi, wawancara dengan pemangku kepentingan, dan dukungan
implementasi _proof-of-concept_ dapat difasilitasi untuk tujuan akademik yang sah.
**5.2.4. Penutup Saran**
Saran-saran yang disampaikan di atas merupakan peta jalan untuk perbaikan
berkelanjutan dari Sistem CUR-HEART. Tidak semua saran perlu
diimplementasikan sekaligus. Prioritisasi berdasarkan nilai bisnis, kebutuhan
pengguna, ketersediaan sumber daya, ketergantungan teknis, dan tingkat risiko.
Pendekatan yang disarankan: jangka pendek (3-6 bulan) fokus pada kemenangan
cepat seperti optimisasi kinerja dan pelatihan pengguna; jangka menengah (6- 12
bulan) implementasi fitur signifikan seperti aplikasi _mobile_ dan konferensi video;
jangka panjang (1-2 tahun) inisiatif strategis seperti integrasi AI dan analitik
lanjutan.
Dengan pola pikir perbaikan berkelanjutan, Sistem CUR-HEART dapat terus
berkembang untuk memenuhi kebutuhan bisnis yang berubah dan mempertahankan
keunggulan kompetitif dalam industri teknologi kesehatan.


##### 164

## DAFTAR PUSTAKA

[1] Y. A. Rozali _et al._ , “MENINGKATKAN KESEHATAN MENTAL DI
MASA PANDEMIC,” 2021.
[2] Y. Fitriani, S. Utami, and B. Junadi, “Perancangan Sistem Informasi Human
Capital Management Berbasis Website,” vol. Vol.6 No.4, 2022.
[3] R. Mawarni, E. A. Putri, and D. Triyanti, “AUDIT SISTEM INFORMASI
E-LEARNING MENGGUNAKAN FRAMEWORK COBIT 5.0 (STUDY
KASUS: E-LEARNING SLBN Sukamaju Kotabumi-Lampung Utara),”
2022.
[4] I. Bali Pamungkas and A. Tri Putranto, _Sistem Informasi Manajemen_.
Bandung: WIDINA BHAKTI PERSADA BANDUNG, 2021.
[5] Afrizal and Y. Kharsela, “SIPMAMA (SISTEM INFORMASI
PELAYANAN ADMINISTRASI KELURAHAN) PADA KANTOR
LURAH MAYANG MANGURAI BERBASIS WEB,” May 2024.
[6] M. A. Rojabi, _PENGANTAR SISTEM INFORMASI_. Bogor: Afdan Rojabi
Publisher, 2025.
[7] Y. Fitriani, S. Utami, and B. Junadi, “Perancangan Sistem Informasi Human
Capital Management Berbasis Website,” vol. Vol.6 No.4, 2022.
[8] A. Oktaviyana, M. Mercedes Br Aritonang, and E. Saputri br Sembiring,
“Analisis Dan Pengembangan Sistem Informasi Manajemen.”
[9] B. Ilham, A. Magister, P. Sumber, and D. Manusia, “SISTEM INFORMASI
MANAJEMEN (SIM) SEBAGAI SARANA PENCAPAIAN E-
GOVERNMENT,” vol. 14, 2022, doi: 10.33747.
[10] A. Oktaviyana, M. Mercedes Br Aritonang, and E. Saputri br Sembiring,
“Analisis Dan Pengembangan Sistem Informasi Manajemen.”
[11] W. Gede _et al._ , “LITERATURE REVIEW KOMPONEN SISTEM
INFORMASI MANAJEMEN: SOFTWARE, DATABASE DAN
BRAINWARE,” vol. 3, no. 3, 2022, doi: 10.31933/jemsi.v3i3.
[12] N. Lisnarini, J. R. Suminar, and Y. Setianti, “Keunggulan dan Hambatan
Komunikasi dalam Layanan Kesehatan Mental pada Aplikasi Telemedicine
Halodoc,” _Psikobuletin:Buletin Ilmiah Psikologi_ , vol. 4, no. 3, p. 176, Sep.
2023, doi: 10.24014/pib.v4i3.25231.


##### 165

[13] R. Sovitriana, W. Damayanthi, and E. Andini, “Penerapan Terapi Realitas
dengan Teknik WDEP untuk Meningkatkan Penerimaan Diri pada Pemuda
Bermasalah Sosial di Panti Sosial Bina Remaja Taruna Jaya 2 Tangerang
Selatan.” [Online]. Available: https://journals.upi-
yai.ac.id/index.php/PsikologiKreatifInovatif/issue/archive
[14] R. Sovitriana, W. Damayanthi, and E. Andini, “Penerapan Terapi Realitas
dengan Teknik WDEP untuk Meningkatkan Penerimaan Diri pada Pemuda
Bermasalah Sosial di Panti Sosial Bina Remaja Taruna Jaya 2 Tangerang
Selatan.” [Online]. Available: https://journals.upi-
yai.ac.id/index.php/PsikologiKreatifInovatif/issue/archive
[15] D. Santika Wulandari _et al._ , “Sistem Informasi Penilaian Perkembangan
Belajar Siswa Berbasis Web Dengan Framework CodeIgniter Di KUMON
Ngringo Jaten, Karanganyar,” 2022. [Online]. Available:
https://journal.polhas.ac.id/index.php/imaging
[16] M. Madrofil Banin, “Perancangan Sistem Informasi Untuk Mengontrol
Sistem Pembelian, Persediaan Dan Penjualan Dengan Menggunakan Metode
System Development Life Cycle (SDLC) Information System Design To
Control Purchasing, Inventory And Sales system Using System
Development Life Cycle (SLDC) Method,” 2021. [Online]. Available:
[http://jurnal.um-palembang.ac.id/integrasi/index](http://jurnal.um-palembang.ac.id/integrasi/index)
[17] A. Muni and A. Isya Alfassa, “MERANCANG APLIKASI
PERPUSTAKAAN MENGGUNAKAN METODE SDLC (SYSTEM
DEVELOPMENT LIFE CYCLE),” _Jurnal Sistem Informasi (TEKNOFILE)_ ,
vol. 2, no. 6, pp. 485–493, 2024.
[18] A. Sutikno, “SISTEM INFORMASI PENGGAJIAN KARYAWAN PT
METAGRA MENGGUNAKAN METODE WATERFALL,” _JUPIKOM_ ,
vol. 1, no. 2, 2022.
[19] B. Fachri and C. Rizal, “Penerapan Metode Waterfall Dalam Perancangan
Sistem Informasi Merdeka Belajar Kampus Merdeka Berbasis Web,”
Online, 2024. [Online]. Available:
https://kampusmerdeka.kemdikbud.go.id/,


##### 166

[20] J. Alif Ramadhan, D. Tresya Haniva, and A. Suharso, “Systematic Literature
Review Penggunaan Metodologi Pengembangan Sistem Informasi
Waterfall, Agile, dan Hybrid,” 2023.
[21] F. Anisa, S. Fauzi, H. Harahap, P. Al Khosyi, and Y. Sari, “Pengembangan
Software Menggunakan Model SDLC Guna Mencapai Keselarasan dengan
Kebutuhan Pengguna,” 2024. [Online]. Available:
https://jurnal.ittc.web.id/index.php/jibs/index
[22] I. Gusti Rai Putra Wiguna, “PENDEKATAN TERINTEGRASI
HIPNOTERAPI DAN COGNITIVE BEHAVIORAL THERAPY DALAM
PENANGANAN PASIEN JIWA,” _Jurnal Inovasi Riset Ilmu Kesehatan_ ,
vol. 3, no. 3, 2024, [Online]. Available:
https://jurnalp4i.com/index.php/healthy
[23] E. Martha, H. Damhila, Y. D. Pora, and D. A. Seofeto, “Efektivitas
penerapan hipnoterapi dan Neuro Linguistic Programming (NLP) dalam
penanganan ansietas di Puskesmas Nita, Kabupaten Sikka,” _Procedia : Studi
Kasus dan Intervensi Psikologi_ , vol. 13, no. 2, pp. 128–134, Jun. 2025, doi:
10.22219/procedia.v13i2.38358.
[24] N. Nasrullah and L. Sulaiman, “Analisis Pengaruh Covid-19 Terhadap
Kesehatan Mental Masyarakat Di Indonesia,” _MEDIA KESEHATAN
MASYARAKAT INDONESIA_ , vol. 20, no. 3, pp. 206–211, Jun. 2021, doi:
10.14710/mkmi.20.3.206-211.
[25] Mukhtar Afiah, Akbar, Masradin, and Shafwah Rif’ah, “Meningkatkan
Kesehatan Mental Remaja Dengan Pendekatan Indentifikasi Faktor Risiko
Dan Manajemen Diri,” _Jurnal Pengabdian Sosial_ , no. Vol. 1 No. 9 (2024):
Juli, Jul. 2024.
[26] R. Y. Negara, “Mental Health Revolution: Menghadapi Tantangan
Kesehatan Mental Di Era Modern,” Sep. 2024. [Online]. Available:
https://ourworldindata.org/mental-health
[27] Muh. Y. Yunus and M. Syukur, “Transformasi Digital Dalam
Kewirausahaan Kesehatan: Peluang Dan Tantangan Bagi Kesehatan
Masyarakat,” _RIGGS: Journal of Artificial Intelligence and Digital Business_ ,
vol. 4, no. 3, pp. 7639–7648, Oct. 2025, doi: 10.31004/riggs.v4i3.3164.


##### 167

[28] G. R. U. Sinaga and S. Samsudin, “Implementasi Framework Laravel dalam
Sistem Reservasi pada Restoran Cindelaras Kota Medan,” _Jurnal Janitra
Informatika dan Sistem Informasi_ , vol. 1, no. 2, pp. 73–84, Oct. 2021, doi:
10.25008/janitra.v1i2.131.
[29] S. R. Laoli, P. Suparman, and M. Andres, “Sistem Manajemen Layanan
Pengiriman Makanan Berbasis Web Menggunakan Laravel 8,” Sep. 2025.
[30] S. M. Pulungan, R. Febrianti, T. Lestari, N. Gurning, and N. Fitriana,
“Analisis Teknik Entity-Relationship Diagram Dalam Perancangan
Database,” _Februari_ , vol. 02, no. 1, pp. 98–102, 2023, doi:
10.47233/jemb.v2i1.533.
[31] K. K. Rekayasa, Y. Khomsi Pane, G. Ramadhan, and F. Dharma Adhinata,
“Perancangan Basis Data Menggunakan Normalisasi Tabel Pada Perusahaan
Dagang Barokah Abadi,” _Data Institut Teknologi Telkom Purwokerto_ , vol.
2, no. 2, pp. 90–96, 2022, [Online]. Available: [http://journal.ittelkom-](http://journal.ittelkom-)
pwt.ac.id/index.php/dinda
[32] Z. Musliyana and A. Helinda, “ANALISIS PERFORMANSI QUERY
MYSQL MENGGUNAKAN QUERY BUILDER PADA FRAMEWORK
CODEIGNITER 4 PERFORMANCE ANALYSIS OF MYSQL QUERY
USING QUERY BUILDER CODEIGNITER 4 FRAMEWORK,” _Journal
of Informatics and Computer Science_ , vol. 8, no. 1, 2022, [Online].
Available: [http://www.apachefriends.org](http://www.apachefriends.org)
[33] R. J. Romadhondaru and A. Basuki, “Visualisasi Topologi Jaringan
berdasarkan Data Routing Border Gateway Protocol,” 2022. [Online].
Available: [http://j-ptiik.ub.ac.id](http://j-ptiik.ub.ac.id)
[34] Y. Mulyanto, M. T. A. Zaen, Y. Yuliadi, and S. Sihab, “Analisis Keamanan
Website SMA Negeri 2 Sumbawa Besar Menggunakan Metode Penetration
Testing (Pentest),” _Journal of Information System Research (JOSH)_ , vol. 4,
no. 1, pp. 202–209, Oct. 2022, doi: 10.47065/josh.v4i1.2335.


##### 168

## DAFTAR RIWAYAT HIDUP

```
I. Biodata Mahasiswa
NIM : 11250066
Nama Lengkap : Roki Anjas
Tempat / Tanggal Lahir : Purbalingga, 05 April 1999
Alamat Domisili : Jl. AMD 6 No 95 RT 10/ RW 08, Duri Kosambi,
Cengkareng, Jakarta Barat, DKI Jakarta
II. Pendidikan
a. Formal
```
1. SDN 2 Mengangkan Tahun 2011
2. SMPN 1 Somagede Tahun 201 4
3. SMK HKTI 2 Purwareja Klampok Tahun 2017
4. Universitas Bina Sarana Informatika Tahun 2021
**b. Tidak Formal**
1. Pelatihan dan Sertifikat SKNN di Universitas Muhammadiyah
Purwokerto Sebagai _Junior Nerwork Administrator_

**III. Riwayat Pengalaman Berorganisasi / Pekerjaan**

1. PIK-R di Desa Somakaton Tahun 2015 s.d. 2016
2. Freelance Toko Komputer Banjarnegara Tahun 2016 s.d. 2017
3. CV Java Multi Mandiri Sebagai _Web Engginer_ Tahun 2017 s.d 2023
4. PT Murni Solusindo Nusantara Sebagai _Web Developer_ Tahun 2023 s.d
    Sekarang
       Jakarta, 16 Desember 2025

```
Roki Anjas
```

##### 169

##### DAFTAR RIWAYAT HIDUP

```
I. Biodata Mahasiswa
NIM : 11250068
Nama Lengkap : Susanto
Tempat / Tanggal Lahir : Tangerang, 03 Februari 1985
Alamat Domisili : KP. Gelam, RT 008 / RW 002,
Kec. Pasar Kemis, Kab. Tangerang
II. Pendidikan
a. Formal
```
1. SDN 2 Kutajaya 1 Tahun 1998
2. SMPN 1 Pasar Kemis Tahun 2001
3. SMK Tunas Harapan Pati Tahun 2 004
4. Universitas Bina Sarana Informatika Tahun 20 09
**b. Tidak Formal**
1. -

**III. Riwayat Pengalaman Berorganisasi / Pekerjaan**

1. PT Utama Raya Motor Tahun 2004 s.d 2010
2. PT Bank Mandiri Tahun 2017 s.d Sekarang

```
Jakarta, 16 Desember 2025
```
```
Susanto
```

##### 170

##### DAFTAR RIWAYAT HIDUP

**I. Biodata Mahasiswa**

```
NIM : 112500 85
Nama Lengkap : Fahruroji
Tempat / Tanggal Lahir : Tangerang, Mei 1983
Alamat Domisili : Jl. Cikini Dalam RT 03 / RW 01 No. 133,
Jurang Mangu Barat, Pondok Aren, Tangerang
Selatan 1522 3
```
**II. Pendidikan
a. Formal**

1. MI Nurul Iman Tahun 199 5
2. MTs N 13 Jakarta Tahun 1998
3. SMA N 47 Jakarta Tahun 200 1
4. Universitas Bina Sarana Informatika Tahun 200 7
**b. Tidak Formal**
1. Pelatihan _Public Speaking_
2. Pelatihan _Impresive Communication_
3. Pelatihan _Hypnosis Instructur_

**III. Riwayat Pengalaman Berorganisasi / Pekerjaan**

1. PT Dayu Tahun 200 1 s.d 20 02
2. PT Sibolga Jaya Tahun 20 02 s.d 2007
3. PT Bagus Bina Cendekia 2007 s.d 2010
4. _Freelancer_ 2010 s.d Sekarang

```
Jakarta, 16 Desember 2025
```
```
Fahruroji
```

##### 171

## DAFTAR LAMPIRAN

```
A. Lampiran Prototipe CUR-HEART
Lampiran 1
```
Link : https://www.figma.com/proto/vB3FJ2yY9FfCTNQiIBh9fB/CUR-Heart-
Web-App


##### 172

```
B. Lampiran Hasil System Usability Scale (SUS)
Lampiran II
```
**Timest
amp**

```
Nama_
Inisial
```
```
Kategori_
Responden
```
```
Usia Pengalaman
_Digital
```
```
Konfirmasi_
Eksplorasi P1 P2 P3 P4 P5 P6 P7 P8 P9 P10
```
```
Total_
Kontribusi
```
```
Skor
_SUS
```
**Kategori
_SUS**
11/20/2
025

```
Dewi
Kartika
```
```
Calon
Klien
```
##### 26 - 35

tahun Menengah Ya 4 2 5 2 4 2 4 2 4 2 31 77.5 _Good_
11/20/2
025 Rara P

```
Calon
Klien
```
##### 18 - 25

tahun Mahir Ya 5 2 5 1 5 2 5 1 4 2 33 82.5 _Excellent_
11/20/2
025

```
Andi
Saputra
```
```
Calon
Klien
```
##### 26 - 35

tahun Menengah Ya 4 2 4 2 4 2 5 2 4 2 30 75 _Good_
11/20/2
025

```
Indah
Lestari
```
```
Calon
Klien
```
##### 36 - 45

tahun Menengah Ya 4 2 5 1 4 2 5 2 4 2 32 80 _Excellent_
11/20/2
025

```
Farah
Amelia
```
```
Calon
Klien
```
##### 26 - 35

tahun Pemula Ya 4 3 4 2 4 2 4 2 3 3 29 72.5 _Good_
11/20/2
025 Budi S

```
Calon
Klien
```
##### 18 - 25

```
tahun Mahir Ya 4 2 5 2 4 2 4 1 4 2 31 77.5 Good
```
11/21/2
025

```
Dr.
Sarah
Wijaya Terapis
```
##### 36 - 45

tahun Mahir Ya 5 1 5 1 5 1 5 1 4 2 34 85 _Excellent_
11/21/2
025

```
Dian
Pratiwi Terapis
```
##### 26 - 35

```
tahun Mahir Ya 5 2 5 1 4 2 5 1 4 2 33 82.5 Excellent
```
11/21/2
025

```
Hendra
Kusum
a Terapis
```
##### 36 - 45

```
tahun Menengah Ya 4 2 5 1 4 2 5 2 4 2 32 80 Excellent
```

##### 173

**Timest
amp**

```
Nama_
Inisial
```
```
Kategori_
Responden
```
```
Usia Pengalaman
_Digital
```
```
Konfirmasi_
Eksplorasi P1 P2 P3 P4 P5 P6 P7 P8 P9 P10
```
```
Total_
Kontribusi
```
```
Skor
_SUS
```
**Kategori
_SUS**
11/21/2
025

```
Maya
Sari Terapis
```
##### 26 - 35

```
tahun Menengah Ya 4 2 4 2 5 2 4 2 4 2 31 77.5 Good
```
11/21/2
025

```
Fitri
Handa
yani Staf Admin
```
##### 26 - 35

```
tahun Mahir Ya 5 1 5 1 5 1 5 1 4 1 35 87.5 Excellent
```
11/21/2
025

```
Siti
Nurjan
ah Staf Admin
```
##### 36 - 45

```
tahun Menengah Ya 4 2 5 1 4 2 5 1 4 2 33 82.5 Excellent
```
11/21/2
025

```
Rina
Anggra
ini Staf Admin
```
##### 26 - 35

```
tahun Mahir Ya 5 2 4 1 4 2 5 2 4 2 32 80 Excellent
```
##### 11/22/2

##### 025

```
Bamba
ng
Herma
wan Manajemen
```
##### 46 - 55

```
tahun Menengah Ya 5 2 5 1 4 2 5 1 4 2 34 85 Excellent
```
##### 11/22/2

##### 025

```
Ridwa
n
Maulan
a Manajemen
```
##### 36 - 45

```
tahun Mahir Ya 5 2 4 1 5 2 5 1 4 2 33 82.5 Excellent
```

