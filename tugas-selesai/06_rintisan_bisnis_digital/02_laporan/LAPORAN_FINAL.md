## CUR-HEART: PLATFORM TERAPI KESEHATAN MENTAL

## BERBASIS TEKNOLOGI DIGITAL

## MAKALAH

Diajukan untuk memenuhi salah satu tugas kelompok mata kuliah Rintisan Bisnis
Digital

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
dengan judul "CUR-HEART: Platform Terapi Kesehatan Mental Berbasis
Teknologi Digital" sebagai salah satu syarat untuk menyelesaikan Program Studi
Strata Satu (S1) Sistem Informasi di Fakultas Teknologi Informasi Universitas
Nusa Mandiri.
Proyek ini bertujuan untuk mengembangkan sistem informasi berbasis web
yang dapat meningkatkan efisiensi dan efektivitas operasional layanan hipnoterapi
di CUR-HEART ( _Hypnotherapy & Mind Wellness Center)._ Dengan memanfaatkan
teknologi informasi, kami berupaya memberikan solusi komprehensif untuk
permasalahan manajemen reservasi, penjadwalan, dokumentasi terapi, dan
pembayaran yang selama ini dilakukan secara manual.
Kami menyadari bahwa laporan ini masih jauh dari sempurna. Oleh karena
itu penyusun mengucapkan terima kasih kepada : Ibu Wulan Dari, M.Kom, selaku
dosen pengampu mata kuliah Rintisan Bisnis Digital yang telah memberikan
bimbingan dan arahan selama proses pembelajaran.
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
Jakarta, 18 Desember 2025
```
```
Penyusun
```

```
iii
```
## ABSTRAK

**Roki Anjas ( 11250066 ), Fahruroji ( 11250085 ), Susanto ( 11250068 ) “CUR-
HEART: Platform Terapi Kesehatan Mental Berbasis Teknologi Digital”.**

Kesehatan mental merupakan isu penting dalam kehidupan modern, dengan sekitar
20% penduduk Indonesia mengalami gangguan mental tanpa penanganan
memadai. CUR-HEART dikembangkan sebagai solusi digital melalui sistem
informasi berbasis web yang menyediakan layanan hipnoterapi dan kesehatan
mental secara terintegrasi. Platform ini menggabungkan fitur reservasi online,
manajemen terapi, pembayaran digital, serta dokumentasi sesi terapi untuk
meningkatkan aksesibilitas dan efisiensi layanan. Sistem dibangun menggunakan
framework Laravel dengan arsitektur MVC, database MySQL ternormalisasi, serta
antarmuka modern berbasis Tailwind CSS. Pengembangan dilakukan
menggunakan metode Design Thinking yang berfokus pada kebutuhan pengguna.
Fitur utama meliputi reservasi 24/7, integrasi payment gateway, dashboard multi-
peran, dokumentasi terapi digital, dan notifikasi otomatis. Model bisnis dirancang
menggunakan Business Model Canvas dengan target pasar individu usia produktif,
perusahaan, dan institusi pendidikan. Hasil pengujian menunjukkan tingkat
kepuasan pengguna sebesar 4,2 dari 5, waktu muat halaman 1,8 detik, dan tingkat
penyelesaian reservasi 92%. Proyeksi finansial menunjukkan titik impas tercapai
pada bulan ke-8. CUR-HEART membuktikan bahwa digitalisasi layanan kesehatan
mental mampu meningkatkan kualitas, efisiensi, dan jangkauan layanan terapi
profesional.

**Kata Kunci: Rintisan Bisnis Digital, Sistem Informasi Kesehatan Mental,
Hipnoterapi,** **_Business Model Canvas_** **, Laravel, UI/UX Design**


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
Daftar Tabel .......................................................................................................... x
Daftar Simbol ....................................................................................................... xi

**BAB 1 PENDAHULUAN ................................................................................... 1**
1.1. Latar Belakang Masalah ................................................................. 1
1.2. Perumusan Masalah ........................................................................ 2
1.3. Maksud dan Tujuan ......................................................................... 2
1.4. Metode Penelitian ............................................................................ 3
1.4.1. Teknik Pengumpulan Data ..................................................... 3
1.4.2. Metode Pengembangan Aplikasi .......................................... 3
1.5. Ruang Lingkup ................................................................................ 4
1.5.1. Ruang Lingkup ..................................................................... 4
1.5.2. Ruang Lingkup Sistem .......................................................... 4
1.5.3. Ruang Lingkup Teknis .......................................................... 4
1.5.4. Batasan Proyek ..................................................................... 5

**BAB II TINJAUAN PUSTAKA ......................................................................... 6**
2.1. Landasan Teori ................................................................................ 6
2.1.1. Konsep Dasar Aplikasi ......................................................... 6
2.1.2. Metode Problem Solving ...................................................... 7
2.1.3. Business Model Canvas ........................................................ 8
2.1.4. Pitch Deck ............................................................................. 9
2.2. Penelitian Terkait ............................................................................. 9
2.3. Teori Pendukung .......................................................................... 12
2.3.1. Pengujian Aplikasi ............................................................. 12
2.3.2. Peralatan Pendukung .......................................................... 14

**BAB III PEMBAHASAN PROSES BISNIS START-UP** ............................. 16
3.1. Tinjauan START-UP (BISNIS DIGITAL) .................................. 16
3.1.1. Profil Bisnis CUR-HEART ............................................... 16
3.1.2. Visi dan Misi ...................................................................... 17
3.1.3. Sturktur Organisasi ............................................................ 17
3.2. Tahapan Membangun Start-UP .................................................... 18
3.3. Business Model Canvas (BMC) .................................................... 22
3.4_._ Pitch Deck ..................................................................................... 26


## v


```
vi
```
## DAFTAR GAMBAR



- BAB IV ANALISA DAN PERANCANGAN APLIKASI START-UP
   - 4.1. Analisa Kebutuhan
      - 4.1.1. Analisis Kebutuhan Aplikasi
      - 4.1.2. Rancangan Diagram Use Case
      - 4.1.3. Rancangan Diagram Aktivitas
      - 4.1.4. Rancangan User Interface
      - 4.1.5. Rancangan Database
   - 4.2. Implementasi
      - 4.2.1. Proses Implementasi
      - 4.2.2. Hasil Implementasi
   - 4.3. Spesifikasi Aplikasi
      - 4.3.1. Hardware
      - 4.3.2. Software
   - 4.4. Pengujian Aplikasi
      - 4.4.1. Black Box Testing
      - 4.4.2. Usability Testing
- BAB V PENUTUP
   - 5.1. Kesimpulan
   - 5 .2. Saran
- DAFTAR PUSTAKA
- DAFTAR RIWAYAT HIDUP
- Gambar II. 1 Tailwind CSS Halaman
- Gambar II. 2 Tahapan Metode Design Thinking
- Gambar II. 3 Business Model Canvas (BMC)
- Gambar III. 1 Struktur Organisasi CUR-HEART
- Gambar III. 2 Business Model Canvas CUR-HEART
- Gambar III. 3 Pich Deck Pembukaan
- Gambar III. 4 Pitch Deck Permasalahan
- Gambar III. 5 Pitch Deck Nilai Lebih CUR-HEART
- Gambar III. 6 Pitch Deck Besaran Pasar
- Gambar III. 7 Pitch Deck Model Bisnis
- Gambar III. 8 Picth Deck Rencana Pemasaran
- Gambar III. 9 Pich Deck Analisis Kompetisi
- Gambar III. 10 Pitch Deck Tim Manajemen
- Gambar III. 11 Pitch Deck Proyeksi Keuangan
- Gambar III. 12 Pich Deck Pencapaian & Rencana
- Gambar III. 13 Pitch Deck Penutup
- Gambar IV. 1 Use Case Diagram Sistem Informasi CUR-HEART
- Gambar IV. 2 Activity Diagram Proses Reservasi Terapi oleh Klien
- Gambar IV. 3 Activity Diagram Dokumentasi Sesi Terapi oleh Terapis
- Gambar IV. 4 Activity Diagram Generate Laporan oleh Admin
- Gambar IV. 5 Mockup Landing Page CUR-HEART
- Gambar IV. 6 Mockup Halaman Tentang Kami
- Gambar IV. 7 Mockup Katalog Layanan
- Gambar IV. 8 Mockup Detail Layanan
- Gambar IV. 9 Mockup Direktori Terapis
- Gambar IV. 10 Mockup Direktori Terapis
- Gambar IV. 11 Mockup Daftar Blog
- Gambar IV. 12 Mockup Detail Blog
- Gambar IV. 13 Mockup Hubungi Kami
- Gambar IV. 14 Mockup FAQ
- Gambar IV. 15 Mockup Kebijakan Privasi vii
- Gambar IV. 16 Mockup Syarat & Ketentuan
- Gambar IV. 17 Mockup Login
- Gambar IV. 18 Mockup Registrasi Klien
- Gambar IV. 19 Mockup Registrasi Terapis
- Gambar IV. 20 Mockup Lupa Kata Sandi
- Gambar IV. 21 Mockup Reset Kata Sandi
- Gambar IV. 22 Mockup Client Dashboard
- Gambar IV. 23 Mockup Booking Step 1 - Select Service
- Gambar IV. 24 Mockup Booking Step 2 - Select Therapist
- Gambar IV. 25 Mockup Booking Step 3 - Select Schedule
- Gambar IV. 26 Mockup Booking Step 4 - Konfirmasi & Pembayaran
- Gambar IV. 27 Mockup Booking Success
- Gambar IV. 28 Mockup Janji Temu Saya
- Gambar IV. 29 Mockup Detail Janji Temu
- Gambar IV. 30 Mockup Progress Tracking
- Gambar IV. 31 Mockup Pesan (Chat)
- Gambar IV. 32 Mockup Pengaturan Klien
- Gambar IV. 33 Mockup Notifikasi Klien
- Gambar IV. 34 Mockup Therapist Dashboard
- Gambar IV. 35 Mockup Manajemen Jadwal
- Gambar IV. 36 Mockup Pengaturan Ketersediaan
- Gambar IV. 37 Mockup Daftar Klien
- Gambar IV. 38 Mockup Profil Klien (View)
- Gambar IV. 39 Mockup Ruang Sesi
- Gambar IV. 40 Mockup Formulir Catatan Sesi
- Gambar IV. 41 Mockup Riwayat Sesi
- Gambar IV. 42 Mockup Dashboard Pendapatan
- Gambar IV. 43 Mockup Edit Profil Terapis
- Gambar IV. 44 Mockup Pengaturan Terapis
- Gambar IV. 45 Mockup Pesan Terapis
- Gambar IV. 46 Mockup Notifikasi Terapis
- Gambar IV. 47 Mockup Admin Dashboard viii
- Gambar IV. 48 Mockup Manajemen Reservasi
- Gambar IV. 49 Mockup Manajemen Pengguna
- Gambar IV. 50 Mockup Laporan Keuangan
- Gambar IV. 51 Mockup Pengaturan Sistem
- Gambar IV. 52 Mockup Notifikasi Admin
- Gambar IV. 53 Mockup Pesan Admin
- Gambar IV. 54 Mockup Detail Pengguna
- Gambar IV. 55 Mockup Edit Pengguna
- Gambar IV. 56 Mockup Detail Reservasi
- Gambar IV. 57 Mockup Manajemen Transaksi
- Gambar IV. 58 Mockup Manajemen Penarikan
- Gambar IV. 59 Mockup Detail Penarikan
- Gambar IV. 60 Mockup Log Aktivitas
- Gambar IV. 61 Mockup Laporan & Analitik
- Gambar IV. 62 Mockup Manajemen Konten Blog
- Gambar IV. 63 Mockup Manajemen Konten FAQ
- Gambar IV. 64 Mockup Manajemen Konten Layanan
- Gambar IV. 65 Mockup Manajemen Ulasan
- Gambar IV. 66 Mockup Manajemen Promo
- Gambar IV. 67 Mockup Verifikasi Terapis
- Gambar IV. 68 Mockup Editor Blog
- Gambar IV. 69 Mockup Editor FAQ
- Gambar IV. 70 Mockup Editor Layanan
- Gambar IV. 71 Mockup Editor Promo
- Gambar IV. 72 Entity Relationship Diagram (ERD) CUR-HEART
- Gambar IV. 73 Logical Record Structure (LRS) CUR-HEART
- Gambar IV. 74 Tampilan Halaman Utama
- Gambar IV. 75 Booking Step 1 - Select Service
- Gambar IV. 76 Tampilan Booking Step 3 - Select Schedule
- Gambar IV. 77 Tampilan Payment
- Gambar IV. 78 Tampilan Client Dashboard


```
ix
```
**Gambar IV. 79 Tampilan Therapist Dashboard** .............................................. 98
**Gambar IV. 80 Tampilan Session Documentation Form** ................................ 99
**Gambar IV. 81 Tampilan Admin Dashboard** ................................................. 100


```
x
```
## DAFTAR TABEL

Halaman
**Tabel IV. 1** Hasil Pengujian Black Box Testing ................................................ 105
**Tabel IV. 2** Hasil Quantitative Usability Testing ............................................... 119
**Tabel IV. 3** System Usability Scale (SUS) Results ........................................... 119


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
## 2^ Attribute

```
Simbol terminal ini untuk
menunjukkan nama-nama atribut
yang ada pada entity.
```
## 3^ Primary Key

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

Kesehatan mental menjadi perhatian utama dalam kehidupan modern.
Berdasarkan data Kementerian Kesehatan RI (2023), sekitar 20% penduduk
Indonesia mengalami gangguan kesehatan mental, namun sebagian besar belum
mendapatkan penanganan memadai akibat keterbatasan akses, stigma sosial, dan
kurangnya pemahaman masyarakat.
Aksesbilitas layanan kesehatan mental masih menjadi kesulitan besar di
berbagai negara termasuk Indonesia. Berbagai keterbatasan sumber daya manusia,
stigma sosoial dan hambatan letak geografis menjadi faktor utama akses layanan
kesehatan mental yang tersedia. Indonesia rasio psikiater dan psikolog masih
rendah sekirat 0,01 per 100.000 penduduk jauh berada di standar WHO yang
memiliki rekomendasi rasio 1:100.000 [1].
Berdasarkan observasi pada CUR-HEART (September 2025), layanan
hipnoterapi masih menghadapi tantangan operasional: proses reservasi manual
melalui _WhatsApp_ dengan tingkat konversi hanya 60%, konflik jadwal terjadi 8- 10
kasus per bulan, dokumentasi tidak terstruktur memakan waktu 15 menit per sesi,
tidak ada data untuk pengambilan keputusan, beban administratif tinggi dengan
admin menghabiskan 70% waktu untuk tugas repetitif, dan risiko keamanan data
klien yang sensitif.
Perkembangan teknologi informasi menghadirkan informasi digitalisasi dalam
layanan kesehatan mental. Digital mental _healt interventions_ dinilai efektif dapat
mengatasi keterbatasan akses apalagi di negara berkembang yang jumlah tenaga
profesionalnya terbatas [2]. Melihat kebutuhan tersebut, proyek rintisan bisnis
digital ini membangun sistem informasi berbasis web untuk CUR-HEART yang
mengintegrasikan layanan hipnoterapi dengan teknologi digital untuk
meningkatkan aksesibilitas, efisiensi, dan kualitas layanan.


**1.2. Perumusan Masalah**
Berdasarkan latar belakang masalah yang telah diuraikan, dapat dirumuskan
permasalahan sebagai berikut:

1. Bagaimana merancang model bisnis digital yang efektif untuk layanan
    hipnoterapi menggunakan _Business Model Canvas_ (BMC)?
2. Bagaimana mengembangkan sistem informasi berbasis web yang dapat
    mengotomasi proses reservasi, manajemen jadwal, dan dokumentasi terapi
    untuk meningkatkan efisiensi operasional CUR-HEART?
3. Bagaimana merancang antarmuka pengguna yang intuitif dan mudah digunakan
    untuk klien, terapis, dan admin?
4. Bagaimana mengintegrasikan sistem pembayaran digital yang aman untuk
    meningkatkan konversi reservasi?
5. Bagaimana membangun sistem dokumentasi terapi digital yang terstruktur
    untuk mendukung kontinuitas perawatan dan pengambilan keputusan berbasis
    data?
**1.3. Maksud dan Tujuan
1.3.1. Maksud**
    Maksud dari proyek ini adalah membangun model bisnis digital
berkelanjutan untuk layanan hipnoterapi yang mengintegrasikan sistem informasi
berbasis web, menerapkan prinsip _design thinking_ , serta memberikan pengalaman
praktis dalam membangun rintisan bisnis digital dari tahap ide hingga
implementasi.
**1.3.2. Tujuan**
    Tujuan dari proyek ini adalah:
    1. Menghasilkan _Business Model Canvas_ (BMC) komprehensif untuk CUR-
       HEART
    2. Menghasilkan sistem informasi berbasis _web_ yang dapat meningkatkan
       konversi reservasi dari 60% menjadi 85%, mengurangi konflik jadwal
       hingga 0%, menghemat waktu dokumentasi dari 15 menit menjadi 5 menit
       per sesi, dan mengurangi beban administratif hingga 50%
    3. Menghasilkan desain antarmuka pengguna dengan 66 halaman _mockup_ dan
       prototipe interaktif


4. Menghasilkan dokumentasi teknis lengkap berupa _ERD, Use Case_
    _Diagram_ , dan _Activity Diagram_
5. Memenuhi persyaratan kelulusan mata kuliah Rintisan Bisnis Digital
**1.4. Metode Penelitian
1.4.1. Teknik Pengumpulan Data**
Teknik pengumpulan data yang digunakan dalam proyek ini adalah :
a. _Observasi_
    Observasi dilakukan di CUR-HEART selama September 2025 untuk
mengamati proses reservasi, manajemen jadwal, dokumentasi terapi,
pembayaran, dan interaksi pemangku kepentingan. Hasil observasi
menunjukkan proses manual memakan waktu lama, rentan kesalahan, dan
menghambat skalabilitas bisnis.
b. Wawancara
Wawancara mendalam dilakukan dengan pemilik (1 orang), terapis (
orang), admin (2 orang), dan klien (8 orang) untuk memahami kebutuhan,
tantangan, dan harapan terhadap sistem digital. Hasil wawancara menunjukkan
semua pemangku kepentingan mendukung digitalisasi layanan.
c. Studi Pustaka
Studi pustaka dilakukan untuk mendapatkan landasan teori dan praktik
terbaik dari jurnal ilmiah, buku, dokumentasi teknis, dan studi kasus rintisan
bisnis digital di bidang teknologi kesehatan.
**1.4.2. Metode Pengembangan Aplikasi**
Pengembangan aplikasi menggunakan pendekatan _Design Thinking_ yang
terdiri dari 5 tahapan iteratif :
1. _Empathize_ : Riset mendalam melalui observasi, wawancara, survei (
responden), dan pembuatan persona pengguna
2. _Define_ : Identifikasi masalah utama, perumusan pernyataan masalah, dan
penetapan metrik keberhasilan
3. _Ideate_ : Curah pendapat solusi, analisis kompetitor, prioritas fitur
menggunakan metode MoSCoW, dan penyusunan BMC
4. _Prototype_ : Pembuatan wireframe, desain mockup (66 halaman), prototipe
interaktif, ERD (16 tabel), dan diagram UML


5. _Test_ : Pengujian kegunaan (5 responden), pengumpulan umpan balik, dan
    iterasi desain
    Metode _Design Thinking_ dipilih karena berpusat pada pengguna, bersifat
iteratif, dan sesuai untuk pengembangan produk digital.
**1.5. Ruang Lingkup**
Ruang lingkup proyek ini mencakup:
**1.5.1. Ruang Lingkup Bisnis**
1. Model Bisnis : Penyusunan Business Model Canvas (BMC) lengkap,
analisis pasar dan kompetitor, strategi pemasaran digital, proyeksi keuangan
3 tahun, dan pitch deck untuk investor.
2. Target Pasar : Individu usia 20-45 tahun dengan kesadaran kesehatan mental
tinggi, perusahaan untuk program kesejahteraan karyawan, lembaga
pendidikan untuk konseling mahasiswa, dengan wilayah operasional Jakarta
dan sekitarnya pada tahap awal.
3. Layanan yang Ditawarkan : Terapi pelepasan stres dan kecemasan,
hipnoterapi penyembuhan trauma, terapi kepercayaan diri dan motivasi,
terapi tidur dan relaksasi, terapi pemrograman ulang kebiasaan, dan
manajemen fobia dan ketakutan.
**1.5.2. Ruang Lingkup Sistem**
1. Fitur Utama : Sistem reservasi daring 24/7 dengan wizard 4 langkah,
manajemen jadwal terapis dengan deteksi konflik otomatis, integrasi
gerbang pembayaran Midtrans, dasbor multi-peran (klien, terapis, admin),
dokumentasi sesi terapi digital, sistem notifikasi surel otomatis, serta
pelaporan dan analitik
2. Pengguna Sistem: Tamu (pengunjung situs web), klien (pengguna layanan
terapi), terapis (pemberi layanan), dan administrator (pengelola sistem)
3. Platform: Aplikasi web dengan desain responsif, dioptimalkan untuk
desktop dan tablet, serta ramah perangkat seluler
**1.5.3. Ruang Lingkup Teknis**
1. Teknologi yang Digunakan: _Backend_ menggunakan _Laravel_ , _frontend_
menggunakan _Blade Templates_ dan _Tailwind_ CSS, basis data _MySQL_ 8.0,


```
gerbang pembayaran Midtrans , layanan surel SMTP/SendGrid, kontrol
versi Git dan GitHub , serta alat desain Figma
```
2. _Deliverables_ : _Business Model Canvas_ (BMC), _pitch deck_ presentasi, _Entity_
    _Relationship Diagram_ (ERD), _Use Case Diagram_ , _Activity_ Diagram (
    proses utama), _mockup_ antarmuka pengguna (66 halaman), prototipe
    interaktif, dokumentasi teknis lengkap, dan laporan proyek
**1.5.4. Batasan Proyek**
1. Tidak Termasuk dalam Lingkup : Aplikasi seluler native (iOS/Android),
fitur konferensi video untuk terapi daring (akan menggunakan integrasi
pihak ketiga di fase 2), multi-bahasa (hanya Bahasa Indonesia di fase 1),
integrasi dengan rekam medis elektronik rumah sakit, sertifikasi ISO atau
akreditasi formal, dan implementasi kecerdasan buatan untuk rekomendasi
terapi
2. Asumsi : Pengguna memiliki akses internet dan perangkat digital, terapis
memiliki sertifikasi hipnoterapi yang valid, bisnis CUR-HEART memiliki
izin operasional yang sah, anggaran pengembangan tersedia sesuai estimasi,
dan pemangku kepentingan dapat memberikan umpan balik tepat waktu
3. Risiko : Perubahan regulasi terkait data kesehatan, resistensi pengguna
terhadap adopsi teknologi, keterbatasan anggaran untuk fitur lanjutan, dan
ketergantungan pada layanan pihak ketiga


##### 6

##### BAB II

##### TINJAUAN PUSTAKA

**2.1. Tinjauan Pustaka
2.1.1. Konsep Dasar Aplikasi**
A. Sistem Informasi
Sistem Informasi adalah seluruh bagian teknologi dan prosedur yang
disatukan sepenuhnya untuk mengelola data agar perusahaan atau organisasi
selalu dapat menyajikan informasi yang akurat dari data yang telah diproses dan
disimpan [3].
B. Aplikasi Berbasis _Web_
Fungsi aplikasi berbasis _website_ secara umum antara lain [4] :

1. Komunikasi dilakukan dengan mudah melalui _platform online_.
2. Informasi _website_ menjadi media informasi terbaru dan menarik untuk
    diibaca oleh seluruh pengguna.
3. Transaksi _Online_ dapat juga menggunakan _website_ untuk sarana bisnis
    barang, jasa dll. Fungsi transaksi ini menghubungkan perusahaan,
    konsumen dan komunitas.
CUR-HEART dikembangkan menggunakan _Laravel_ untuk _backend_ , _Blade_ dan
_Tailwind CSS_ untuk _frontend_ , _MySQL_ untuk basis data, dan Nginx sebagai server
_web_.
_C. Framework Laravel
Framework_ adalah menyediakan kerangka kerja untuk membuat sebuah
sistem yang tidak harus merancang sistem dari awal. _Laravel_ adalah kerangka
kerja PHP sumber terbuka ( _open-source_ ) yang dirancang mengikuti arsitektur
_Model-View-Controller_ (MVC) yang digunakan untuk membangun aplikasi
_website_ [5].
Fitur utama Laravel meliputi [6]:
a. Arsitektur _MVC_ ( _Model-View-Controller_ )
b. _Eloquent ORM_
c. Mesin _Template Blade_
d. Fitur Keamanan Bawaan


e. Migrasi & Pembenihan Basis Data
f. Artisan CLI
Laravel dipilih karena ekosistem yang matang, dokumentasi lengkap, dan
komunitas yang besar.
_D. Database Management System (DBMS)
Database Management System_ merupakan sekumpulan program aplikasi
yang digunakan untuk membuat dan mengelola basis data. DBMS merupakan
software yang dapat menentukan data tersebut untuk dikoordinasi, disimpan,
diubah dan dapat diambil kembali [7].
_E. Tailwind CSS
Tailwind CSS_ merupakan kerangka kerja yang dikembangkan untuk
percepatan proses dalam _prototyping_ halaman web untuk sesuai kebutuhan
( _custome_ ) [8].
_Tailwind CSS_ dipilih karena fleksibilitas tinggi, ukuran berkas kecil, dan
integrasi sempurna dengan Laravel.

Sumber : Andarsyah & Raffi Kusuamah (2023)

```
Gambar II. 1 Tailwind CSS
```
**2.1.2. Metode Problem Solving**
_A. Design Thinking
Design Thinking_ adalah pendekatan yang menghubungkan kolaborasi
dengan pengguna untuk menemukan solusi dalam suatu masalah. Tujuan
utamanya adalah terciptanya layanan yang inovatif, sesuai dengan kebutuhan
pengguna dan dapat mengatasi masalah yang ada[9].

Sumber : Ansori, et.all (2023)

## Gambar II. 2 Tahapan Metode Design Thinking


_B. Lean Startup Methodology
Starup_ yaitu organisasi non-IPO atau perusahaan swasta yang tidak tercatat
di bursa efek yang mempunyai jumlah karyawan kurang dari 500 orang. _Lean
Startup_ adalah memfokuskan pada pengembangan produk kecil dan secara aktif
mengumpulkan masukan dalam perbaikan[10].
**2.1.3.** **_Business Model Canvas_** **(BMC)**
_Business Model Canvas_ adalah kerangka kerja yang digunakan untuk
memahami segmen pelanggan dan kapasitas nilai dari sebuah bisnis. BMC terdiri
dari 9 elemen yang saling terkait yaitu[11] :

1. _Customer Segments_ (Kebutuhan Pelanggan) : Kelompok orang atau organisasi
    yang ingin dijangkau dan dilayani
2. _Value Propositions_ (Nilai Yang Diberikan Kepada Pelanggan) : Kumpulan
    produk dan layanan yang menciptakan nilai untuk segmen pelanggan
3. _Channels_ (Jaungkauan Target) : Cara perusahaan berkomunikasi dan
    menjangkau segmen pelanggan
4. _Customer Relationships_ (Interaksi dengan Pelanggan) : Jenis hubungan yang
    dibangun dengan segmen pelanggan
5. _Revenue Streams_ (Penerimaan dari penjualan) : Uang yang dihasilkan dari
    setiap segmen pelanggan
6. _Key Resources_ (Sumber Daya Utama) : Aset penting yang diperlukan untuk
    membuat model bisnis berfungsi
7. _Key Activities_ (Aktivitas Utama) : Hal-hal penting yang harus dilakukan
    perusahaan
8. _Key Partnerships_ (Kemitraan Utama) : Jaringan pemasok dan mitra yang
    membuat model bisnis berfungsi
9. _Cost Structure_ (Pengeluaran Operasional) : Semua biaya yang dikeluarkan
    untuk mengoperasikan model bisnis


Sumber : Zamroni, et.all (202 2 )

## Gambar II. 3 Business Model Canvas (BMC)

BMC dipilih untuk CUR-HEART karena memberikan gambaran holistik
model bisnis dalam satu halaman, memudahkan komunikasi dengan pemangku
kepentingan, dan merupakan kerangka kerja yang terbukti efektif.
**2.1.4.** **_Pitch Deck_**
_Pitch deck_ adalah presentasi singkat yang dirancang untuk menjelaskan
gambaran umum tentang rencana bisnis kepada calon investor, mitra, atau
pemangku kepentingan[12].
Pitch deck CUR-HEART dirancang untuk menarik investor pendanaan awal,
meyakinkan mitra strategis, dan presentasi di kompetisi startup.

**2.2. Penelitian Terkait**
Berikut adalah penelitian terkait yang menjadi referensi dalam
pengembangan sistem informasi CUR-HEART :
**2.2.1. Penelitian 1: Sistem Informasi Manajemen Klinik Kesehatan Mental**
Judul: "Perancangan Sistem Informasi Rekam Medis Pasien Pada Klinik Dr.
I Wayan Jiwa Berbasis Website" oleh Maulidya, A., Haerudin, H. (2022) yang
dipublikasikan di Jurnal Sains Teknologi dan Masyarakat, Vol. 2 , No. 2.
Penelitian ini mengembangkan sistem informasi untuk mengelola
operasional klinik kesehatan yang mencakup melayani pasien, mengumpulkan data
obat, dan rekam medis pasien menggunakan PHP dan MySQL dengan pemodelan
UML. Hasil penelitian menunjukkan dapat mengatasi masalah dalam media


penyimpanan, pengolahan data pasien, rekam medis, dan data obat yang sudah
terkomputerisasi sehingga dapat dilakukan dengan efektif.
Persamaan dengan CUR-HEART adalah sama-sama sistem informasi untuk
layanan kesehatan mental berbasis web dengan fokus pada efisiensi operasional dan
dokumentasi. Perbedaan dengan CUR-HEART adalah CUR-HEART fokus pada
hipnoterapi dengan kerangka kerja modern Laravel, memiliki fitur reservasi daring
dan pembayaran, menggunakan metode _Design Thinking_ , serta memiliki model
bisnis digital yang komprehensif menggunakan BMC.
**2.2.2. Penelitian 2: Platform Digital untuk Layanan Terapi Online
Judul** : "Aplikasi “Terapi” Usaha Berbasis Teknologi Digital untuk
Meningkatkan Pelayanan Kesehatan Kota Palu" oleh Hardani, M, et all. (202 4 )
yang dipublikasikan di Media Publikasi Promosi Kesehatan Indonesia,Vol. 7 , No. 1.
Penelitian ini mengembangkan platform pasar digital yang menghubungkan
dengan pengguna untuk memudahkan dalam penggunaan fitur-fitur yang tersedia
seperti Obat, Apotek, Apoteker, Rumah Sakit, Gawat Darurat dan Order.
Persamaan dengan CUR-HEART adalah sama-sama platform digital untuk
layanan terapi dengan fitur pemesanan dan pembayaran daring serta fokus pada
aksesibilitas dan efisiensi. Perbedaan dengan CUR-HEART adalah CUR-HEART
fokus pada hipnoterapi untuk satu pusat layanan (B2C) bukan penyediaan layanan
seluruh aspek tentang kesehatan, menggunakan Laravel, memiliki fitur
dokumentasi sesi yang lebih detail, dan terintegrasi dengan model bisnis luring dan
daring.
**2.2.3. Penelitian 3: Implementasi Business Model Canvas pada Startup
Healthtech
Judul** : "Usulan Implementasi Strategi Bagi Rumah Sakit XYZ Menggunakan
Analisis Model Kanvas ( _Business Model Canvas_ )" oleh Putra, E, et all. (202 4 ) yang
dipublikasikan di Jurnal Cendekia Ilmiah, Vol. 4, No. 1.
Penelitian ini menganalisis penerapan _Business Model Canvas_ pada Rumah
Sakit XYZ dan untuk dapat merumuskan model bisnis dapat dimanfaatkan tools
_Business Model Canvas_ (BMC). Hasil penelitian menunjukkan BMC efektif untuk
visualisasi model bisnis kesehatan, memudahkan identifikasi manajamen rumah


sakit meningkatkan fasilitas kesehatan 1, membantu perubahan arah dan membantu
memperbaiki aspek-aspek operasional dan kebijakan kemitraan.
Persamaan dengan CUR-HEART adalah sama-sama menggunakan BMC untuk
perencanaan bisnis di sektor teknologi kesehatan dengan integrasi layanan daring
dan luring.
**2.2.4. Penelitian 4:** **_User Experience Design_** **untuk Aplikasi Kesehatan Mental
Judul** : "Perancangan _User Experience_ Aplikasi Konsultasi Mental Online
di Masa Pandemi berbasis Mobile menggunakan Metode _Design Thinking_ " oleh
Muhammad, F, et.all. (202 2 ) yang dipublikasikan di Jurnal Pengembangan
Teknologi Informasi dan Ilmu Komputer, Vol. 6 , No. 7.
Penelitian ini menggunakan metode _Design Thinking_ untuk melakukan
perancangan _user experience_ dengan aplikasi mobile dalam membantu masyarakat
khususnya mahasiswa dengan rentang usia 18-25 tahun. Dalam validasi dilakukan
pengujian usabilitu 10 responden dan mendapatkan nilai aspek efektivitas _success_
rate 90,5 %. Setelah itu dilakukan pengujian pengalaman pengguna kepada 20
responden menggunakan perangkat kuesioner _user experience questionnaire_
(UEQ) dengan hasil spek attractiveness sebesar 2.16, aspek perspicuity sebesar
2.06, aspek efficiency sebesar 2.28, aspek dependability sebesar 2.15, aspek
stimulation sebesar 2.08, dan aspek novelty sebesar 1.43.
Persamaan dengan CUR-HEART adalah sama-sama menggunakan _Design
Thinking_ dengan fokus pada pengalaman pengguna untuk aplikasi kesehatan mental
serta menekankan privasi dan keamanan data. Perbedaan dengan CUR-HEART
adalah CUR-HEART mencakup seluruh aspek bisnis bukan hanya pengalaman
pengguna, memiliki 3 tipe pengguna (klien, terapis, admin), dan mengintegrasikan
desain pengalaman pengguna dengan sistem informasi lengkap.
Berdasarkan analisis penelitian terkait, dapat disimpulkan bahwa digitalisasi
layanan kesehatan mental terbukti meningkatkan efisiensi dan aksesibilitas,
_Business Model Canvas_ efektif untuk perencanaan bisnis teknologi kesehatan,
_Design Thinking_ cocok untuk pengembangan produk yang berpusat pada pengguna,
integrasi teknologi web modern meningkatkan pengalaman pengguna, dan fokus
pada privasi dan keamanan data sangat penting untuk aplikasi kesehatan mental.


CUR-HEART mengambil praktik terbaik dari penelitian-penelitian tersebut
dan mengintegrasikannya dalam satu solusi komprehensif yang mencakup model
bisnis, sistem informasi, dan desain pengalaman pengguna.

**2.3. Teori Pendukung
2.3.1. Pengujian Aplikasi**
_A. Black Box Testing
Black Box Testing_ disebut sebagai pegujian perilaku pada struktur interior,
logika perangkat lunak yang diuji tidak dapat diketahui oleh penguji. Penguji
didasarkan kepada spesifikasi kebutuhan dan tidak perlu dilakukannya analisis
kode. Pengujian black box testing pengujian ini dilakukan dari sudut pandang
pengguna akhir[13].
Teknik Pengujian _Black Box Testing_ meliputi a. Teknik _Equivalence
Partitioning_ (membagi menjadi beberapa partisi dari data), b. _Boundary Value
Analysis_ (menguji nilai minimum maupun maksimum dari error yang
ditemukan), c. Teknik _Fuzzing_ (merupakan teknik untuk mencari gangguang
dari _software_ dengan menggunakan injeksi data yang terbilang cacat), d. Teknik
_Cause Effect Graph_ (Teknik testing menggunakan graphic sebagai acuan), e.
Teknik _Orthogaonal Array Testing_ (Teknik yang digunakan jika input domain
yang relative terbilang kecil ukurannya, namum cukup berat untuk digunakan
dalam skala besar), f. Teknik _All Pair Testing_ (Semua pasangan dari test cas
didesain sedemikian rupa agar dapat dieksekusi dalam kemungkinan kombinasi
distrik dari seluruh pasangan berdasarkan input parameternya), g. Teknik _State
Transition_ (Teknik ini berguna untuk melakukan pengetesan terhadap kondisi
dari mesin dan navigasi dalam bentuk grafik) [14].
Keuntungan _Black Box Testing_ adalah tidak memerlukan pengetahuan
pemrograman, dapat dilakukan oleh penguji independen, fokus pada perspektif
pengguna, dan efisien untuk sistem yang besar. Penerapan pada CUR-HEART
meliputi pengujian fungsionalitas reservasi, proses pembayaran dengan
integrasi Midtrans, autentikasi dan otorisasi, operasi CRUD, validasi formulir
dan penanganan kesalahan, serta notifikasi surel.


_B. White Box Testing
White Box Testing_ adalah metode pengujian yang memeriksa dan
melakukan analisis kode program untuk menemukan kesalahan atau kekurang
dalam suatu aplikasi atau perangkat lunak[15].
Teknik White Box Testing meliputi Statement Coverage (setiap pernyataan
dieksekusi minimal sekali), Branch Coverage (setiap cabang dieksekusi), Path
Coverage (setiap jalur yang mungkin dieksekusi), dan Condition Coverage
(setiap kondisi boolean diuji). Penerapan pada CUR-HEART meliputi
pengujian unit untuk setiap fungsi atau metode dengan cakupan kode minimal
70%, pengujian logika bisnis seperti perhitungan harga dan validasi jadwal,
pengujian kueri basis data menggunakan Eloquent ORM, serta pengujian
middleware untuk autentikasi dan otorisasi.
_C. Usability Testing_
Secara umum konsep dalam _Usability_ adalah atribut dari kualitaas dapat
digunakan dalam evaluasi bagaimana kemudahan sebuah antarmuka digunakan.
Usability Testing adalah suatu metode yang digunakan untuk melihat seberapa
nyaman pengguna dapat berhubungan dengan sistem informasi[16].
Komponen _Usability Testing_ yang digunakan dalam mengukur tingkat
_usability_ sebagai berikut[17] :
a. _Learnability_ yaitu kemudahan pengguna menyelesaikan tugas/task pertama
kali.
b. _Efficiency_ yaitu mengukur keberhasilan pengguna dalam menyelesaikan
task berdasarkan waktu yang dihabiskan dalam menyelesaikan tugas atau
task.
c. _Errors_ yaitu mengukur berapa banyak kesalahan yang terjadi saat pengguna
menyelesaikan tugas atau task, dan mengukur seberapa mudah pengguna
Kembali menggunakan _website_ dengan baik.
d. _Satisfaction_ yaitu mengukur tingkat kepuasan pengguna saat menggunak
webisite.
Metode _Usability Testing_ meliputi _Think Aloud Protocol_ (pengguna
berbicara saat menggunakan sistem), Task Analysis (mengukur waktu dan
tingkat keberhasilan tugas), _Questionnaire_ seperti _System Usability Scale_ (SUS.


Penerapan pada CUR-HEART meliputi pengujian kegunaan dengan 15
responden (5 klien, 5 terapis, 5 admin), menggunakan _kuesioner System
Usability Scale_ (SUS), dengan target tingkat penyelesaian tugas minimal 90%
dan skor SUS minimal 70/100.
**2.3.2. Peralatan Pendukung**
A. Figma
Figma adalah alat desain yang digunakan pada windows untuk membuat
_prototype_ aplikasi serta berbagai desain lainnya. Figma banyak digunakan oleh
kalangan yang bekerja pada bidang UI/UX, _web design_ dan pekerjaan yang
sejenis[18].
Penerapan pada CUR-HEART meliputi pembuatan 66 halaman mockup
untuk semua peran pengguna, pembuatan sistem desain (warna, tipografi,
komponen), pembuatan prototipe interaktif untuk pengujian pengguna,
kolaborasi dengan pemangku kepentingan untuk umpan balik, dan ekspor aset
untuk pengembangan.
_B. PlantUML_
PlantUML meruapakan alat bantu untuk merancang aplikasi untuk
visualisasi dengan diagram[19].
Penerapan pada CUR-HEART meliputi _Use Case Diagram_ untuk
menggambarkan interaksi pengguna dengan sistem, _Activity Diagram_ untuk
proses bisnis seperti reservasi, dokumentasi sesi, dan pembuatan laporan, serta
_Sequence_ Diagram untuk alur komunikasi antar komponen.
_C. dbdiagram.io_
dbdiagram.io adalah merupakan alat yang dapat digunakan dalam membuar
diagram ER dan membuat desai database secara cepat. Alat ini dapat
menggunakan Bahasa yang mudah dan bersifat terbuka [20]. Penerapan pada
CUR-HEART meliputi pembuatan ERD dengan 16 tabel, pendefinisian relasi
(satu-ke-satu, satu-ke-banyak, banyak-ke-banyak), ekspor ke SQL untuk
migrasi basis data, dan dokumentasi struktur basis data.
_D. Git & GitHub_
Git adalah sistem kontrol versi terdistribusi untuk melacak perubahan dalam
kode sumber, sedangkan GitHub sebagai platform untuk melakukan


pembelajaran kolaboratif[21]. Keunggulan Git dan GitHub meliputi kontrol
versi untuk semua berkas (kode, dokumentasi, desain), strategi percabangan
untuk pengembangan paralel, pull request untuk tinjauan kode, pelacakan isu
untuk bug dan permintaan fitur, serta GitHub Actions untuk CI/CD.
Penerapan pada CUR-HEART meliputi repositori untuk kode sumber
Laravel dan dokumentasi, strategi percabangan (main, develop, feature
branches), konvensi pesan commit untuk kejelasan, dan GitHub Projects untuk
manajemen proyek.
_E. Postman_
Postman adalah alat yang tersedia oleh Google Chrome dengan fungsi
utama dengan GUI API caller dan saat ini menyediakan fitur lain seperti
_Sharing Collection API for Documentation_ , _Testing API_ , _Realtime
Collaboration Team_ dl[22]. Penerapan pada CUR-HEART meliputi pengujian
titik akhir API (autentikasi, pemesanan, pembayaran), pembuatan koleksi untuk
semua rute API, pengujian otomatis untuk pengujian regresi, dan dokumentasi
untuk pengembang frontend.
_F. Laravel Debugbar
Laravel Debugbar_ adalah pengujian yang berfokus pada performa yang
dilakukan pemantauan waktu respon, _query database_ dan memori [23].
Penerapan pada CUR-HEART meliputi debugging masalah kinerja, optimasi
kueri basis data, pemantauan penggunaan memori, dan profiling aplikasi.
Dengan teori pendukung dan peralatan yang tepat, pengembangan sistem
informasi CUR-HEART dapat dilakukan secara efisien, terstruktur, dan
menghasilkan produk berkualitas tinggi yang memenuhi kebutuhan pengguna
dan standar industri.


##### 16

##### BAB III

##### PEMBAHASAN PROSES BISNIS START-UP

##### 3.1 TINJAUAN START-UP (BISNIS DIGITAL)

**3.1.1. Profil Bisnis CUR-HEART**
CUR-HEART adalah pusat layanan terapi kejiwaan yang mengintegrasikan
pendekatan hipnoterapi modern, konseling psikologis, dan pelatihan
pengembangan diri dengan tagline "Hypnotherapy & _Mind Wellness Center_ ".
Bisnis ini bergerak di bidang layanan kesehatan mental khususnya hipnoterapi,
berbentuk perseorangan pada tahap awal dengan rencana menjadi PT di tahun ke-
2, didirikan tahun 2025, berlokasi di Jakarta Selatan.
CUR-HEART hadir sebagai solusi untuk meningkatnya kebutuhan
masyarakat akan layanan kesehatan mental yang profesional, aman, dan mudah
diakses. Berdasarkan data Kementerian Kesehatan RI, sekitar 20% penduduk
Indonesia mengalami gangguan kesehatan mental namun sebagian besar belum
mendapatkan penanganan memadai. CUR-HEART menawarkan layanan
hipnoterapi yang terbukti efektif dalam mengatasi berbagai kondisi seperti stres,
insomnia, trauma, kecemasan, serta meningkatkan motivasi dan kepercayaan diri.

**Latar Belakang Pendirian** :
Proyek bisnis ini diinisiasi oleh tim mahasiswa Sistem Informasi Universitas Nusa
Mandiri yang melihat peluang besar dalam sektor teknologi kesehatan, khususnya
layanan kesehatan mental. Dengan meningkatnya kesadaran masyarakat tentang
pentingnya kesehatan mental pasca-pandemi COVID-19, permintaan terhadap
layanan terapi alternatif seperti hipnoterapi terus meningkat. Tim melakukan riset
pasar dan menemukan bahwa meskipun permintaan tinggi, layanan hipnoterapi di
Indonesia masih terbatas dan belum terdigitalisasi dengan baik. Melihat
kesenjangan tersebut, tim memutuskan untuk membangun CUR-HEART sebagai
rintisan bisnis digital yang mengintegrasikan layanan hipnoterapi profesional
dengan sistem informasi modern untuk memberikan pengalaman terbaik bagi klien,
terapis, dan manajemen.


**3.1.2. Visi dan Misi**
a. Visi **:**
Visi CUR-HEART adalah menjadi pusat terapi kejiwaan berbasis
hipnoterapi modern dan spiritual yang terpercaya, profesional, dan
berpengaruh dalam membantu masyarakat Indonesia mencapai kesehatan
mental, keseimbangan emosional, serta kualitas hidup yang lebih baik.
b. Misi **:**
Misi CUR-HEART meliputi: memberikan layanan terapi kejiwaan
yang aman, etis, dan ilmiah melalui metode hipnoterapi modern yang
terbukti efektif; meningkatkan kesadaran masyarakat tentang pentingnya
kesehatan mental melalui edukasi, seminar, dan program pengembangan
diri yang mudah diakses; menciptakan ruang terapi yang nyaman, rahasia,
dan humanis; mengintegrasikan pendekatan sains dan spiritualitas dalam
setiap program; memberdayakan individu agar mampu mengelola pikiran
bawah sadar secara mandiri; dan mengembangkan model bisnis
berkelanjutan dengan memperluas layanan ke bidang pelatihan hipnoterapi,
konsultasi korporat, dan platform terapi digital.
**3.1.3. Struktur Organisasi**
Berikut Gambar Struktur Organisasi CUR-HEART :

## Gambar III. 1 Struktur Organisasi CUR-HEART


Struktur organisasi CUR-HEART dirancang untuk mendukung operasional
yang efisien dan skalabilitas bisnis. Pada tahap awal, struktur organisasi masih
ramping dengan fokus pada tim inti yang terdiri dari CEO (Fahruroji), CTO (Roki
Anjas), CMO (Susanto), Terapis Utama (3 orang), Admin & _Customer Service_ (2
orang), dan _Finance & Accounting_ ( _outsource_ ).
A. Uraian tugas dan tanggung jawab meliputi :

1. _Chief Executive Officer_ (CEO) bertanggung jawab atas strategi bisnis,
    pengambilan keputusan strategis, hubungan investor dan pemangku
    kepentingan, pemantauan kinerja, dan representasi perusahaan
2. _Chief Technology Officer_ (CTO) bertanggung jawab atas arsitektur sistem,
    pengembangan platform, infrastruktur TI, keamanan data, dan peta jalan
    teknologi
3. _Chief Marketing Officer_ (CMO) bertanggung jawab atas strategi
    pemasaran, manajemen merek, riset pasar, media sosial, kampanye
    promosi, dan hubungan pelanggan
4. Terapis Utama melakukan sesi terapi, penilaian klien, dokumentasi sesi,
    pemantauan kemajuan, dan menjaga kerahasiaan data klien
5. Admin & _Customer Service_ mengelola reservasi, dukungan pelanggan,
    koordinasi dengan terapis, pelaporan, dan penanganan keluhan, serta
    _Finance & Accounting_ ( _outsource_ ) menangani pembukuan, laporan
    keuangan, kepatuhan pajak, penggajian, dan analisis keuangan.
**3.2. Tahapan Membangun Start-up**
Pembangunan start-up CUR-HEART menggunakan metode _Design Thinking_
yang terdiri dari 5 tahapan iteratif. Metode ini dipilih karena berpusat pada
pengguna, fleksibel, dan terbukti efektif untuk mengembangkan produk digital
yang inovatif.
3.2.1. Tahap 1: _Empathize_ (Berempati)
Tahap empathize adalah tahap untuk memahami pengguna secara
mendalam melalui observasi, wawancara, dan pendalaman untuk mendapatkan
wawasan tentang kebutuhan, motivasi, masalah utama, dan aspirasi pengguna.
Aktivitas yang dilakukan meliputi **:**


Observasi langsung dilakukan di CUR-HEART selama 2 minggu (September 2025)
untuk mengamati proses operasional dan mengidentifikasi hambatan. Hasil
observasi menunjukkan admin menghabiskan 70% waktu untuk tugas repetitif,
konflik jadwal terjadi 8-10 kali per bulan, dokumentasi terapi memakan waktu 15
menit per sesi, tingkat konversi reservasi hanya 60%, dan data tersebar di berbagai
platform.
Wawancara mendalam dilakukan dengan pemilik bisnis (1 orang), terapis
(3 orang), admin (2 orang), dan klien (8 orang). Wawasan yang diperoleh
menunjukkan pemilik ingin meningkatkan efisiensi operasional dan skalabilitas
bisnis, terapis kesulitan mengakses riwayat klien dan ingin fokus pada terapi bukan
administrasi, admin kewalahan dengan tugas repetitif dan koordinasi jadwal, serta
klien ingin reservasi cepat 24/7 dengan pembayaran daring dan khawatir dengan
privasi data.
Tim membuat peta perjalanan ( _roadmap_ ) pelanggan yang menunjukkan 10
tahap dari kesadaran hingga retensi, dengan titik masalah utama pada proses
pemesanan yang lama, pembayaran manual yang rumit, konfirmasi yang tidak pasti,
dan tidak adanya pengingat otomatis serta pelacakan kemajuan.
3.2.2. Tahap 2: Define (Mendefinisikan)
Tahap define adalah tahap untuk mensintesis temuan dari tahap empathize
dan mendefinisikan masalah inti yang harus diselesaikan dengan keluaran utama
berupa pernyataan masalah yang jelas dan dapat ditindaklanjuti.
Aktivitas yang dilakukan meliputi **:**
Tim melakukan pemetaan afinitas untuk mengelompokkan temuan
berdasarkan tema dengan prioritas tinggi meliputi proses pemesanan yang tidak
efisien (reservasi manual, tidak ada ketersediaan waktu nyata, tingkat konversi
rendah 60%), manajemen jadwal yang buruk (konflik jadwal 8-10 kali/bulan,
koordinasi terapis sulit, tidak ada sistem pengingat), dan beban administratif tinggi
(admin menghabiskan 70% waktu untuk tugas repetitif).
Berdasarkan pemetaan tersebut, tim merumuskan pernyataan masalah untuk
setiap pengguna: klien membutuhkan cara cepat dan fleksibel untuk reservasi 24/7
tanpa menunggu admin; terapis membutuhkan sistem dokumentasi terstruktur
untuk fokus pada terapi bukan administrasi; admin membutuhkan otomasi untuk


tugas repetitif; dan manajemen membutuhkan data terintegrasi dan dasbor analitik
untuk pemantauan waktu nyata.
3.2.3. Tahap 3: _Ideate_ (Mengideasi)
Tahap ideate adalah tahap untuk menghasilkan berbagai ide solusi melalui
curah pendapat dengan fokus pada kuantitas di tahap awal, kemudian melakukan
konvergensi untuk memilih ide terbaik.
Aktivitas yang dilakukan meliputi **:**
Tim melakukan sesi curah pendapat dengan pemangku kepentingan
(pemilik, terapis, admin) selama 3 sesi menghasilkan 50+ ide solusi seperti platform
web untuk reservasi daring, aplikasi seluler, chatbot AI, integrasi gerbang
pembayaran, dasbor analitik, sistem pengingat otomatis, konferensi video,
gamifikasi, dan forum komunitas.
Analisis kompetitor dilakukan untuk mengidentifikasi praktik terbaik dan
kesenjangan. Kompetitor utama meliputi Halodoc (telemedicine dengan brand
awareness tinggi namun tidak fokus pada hipnoterapi), Alodokter (platform
kesehatan dengan konten kuat namun tidak ada layanan hipnoterapi), dan praktisi
hipnoterapi individual (personal touch namun tidak ada sistem digital). Analisis
menunjukkan tidak ada platform khusus untuk hipnoterapi di Indonesia dan
kompetitor belum mengintegrasikan pemesanan, pembayaran, dan dokumentasi,
sehingga terdapat peluang untuk menjadi pelopor di pasar khusus. Tim
memprioritaskan fitur menggunakan metode MoSCoW dengan kategori Must Have
(MVP Fase 1) meliputi sistem reservasi daring dengan wizard 4 langkah,
manajemen jadwal terapis dengan deteksi konflik, integrasi gerbang pembayaran
Midtrans, dasbor untuk klien/terapis/admin, dokumentasi sesi terapi digital, sistem
notifikasi surel otomatis, dan autentikasi multi-peran; Should Have (Fase 2)
meliputi aplikasi seluler, konferensi video, chatbot, analitik lanjutan, dan program
loyalitas; Could Have (Fase 3) meliputi rekomendasi AI, gamifikasi, dan forum
komunitas; serta Won't Have meliputi diagnosis medis otomatis, manajemen resep,
dan integrasi asuransi.
Tim merancang proposisi nilai unik untuk setiap pengguna: untuk klien
(kemudahan reservasi 24/7, transparansi jadwal dan harga, keamanan data
terenkripsi, kualitas terapis bersertifikat, harga kompetitif); untuk terapis (efisiensi


dokumentasi dengan template, akses riwayat klien lengkap, sistem pembayaran
transparan, fleksibilitas jadwal, dukungan administratif); dan untuk manajemen
(visibilitas dasbor waktu nyata, laporan dan analitik untuk pengambilan keputusan,
skalabilitas sistem, otomasi tugas repetitif, kepatuhan regulasi bawaan).
3.2.4. Tahap 4 : _Prototype_ (Membuat Prototipe)
Tahap _prototype_ adalah tahap untuk membuat representasi nyata dari ide
untuk dieksplorasi dan diuji yang dapat berupa sketsa, wireframe, mockup, atau
prototipe yang berfungsi.
Aktivitas yang dilakukan meliputi **:**
Tim membuat wireframe untuk struktur halaman menggunakan Figma
dengan cakupan 66 halaman meliputi halaman publik (12 halaman), autentikasi (4
halaman), dasbor klien (12 halaman), dasbor terapis (13 halaman), dan dasbor
admin (25 halaman). Wireframe berfokus pada tata letak, hierarki, dan alur
pengguna dengan iterasi berdasarkan umpan balik internal.
Tim membuat mockup fidelitas tinggi menggunakan Figma dengan sistem
desain yang mencakup palet warna (Teal sebagai warna utama, Purple sebagai
warna sekunder, Orange sebagai warna aksen), tipografi Inter (sans-serif modern),
dan komponen (tombol, formulir, kartu, modal, tabel, grafik). Desain responsif
untuk desktop, tablet, dan seluler dengan pertimbangan aksesibilitas.
Tim membuat prototipe interaktif di Figma yang dapat diklik untuk alur
pengguna utama seperti alur pemesanan (4 langkah: Layanan → Terapis → Jadwal
→ Pembayaran), alur dokumentasi terapis, dan navigasi dasbor admin. Prototipe
dapat digunakan untuk pengujian pengguna dan dibagikan kepada pemangku
kepentingan.
Tim merancang struktur basis data menggunakan dbdiagram.io dengan 16
tabel ternormalisasi hingga 3NF meliputi _users, clients, therapists, services,
therapist_services, bookings, payments, sessions, session_notes, reviews,
notifications, messages, promo_codes, withdrawals, activity_logs_ , dan
_system_settings_ dengan relasi satu-ke-satu, satu-ke-banyak, dan banyak-ke-banyak.
Tim membuat diagram UML menggunakan PlantUML meliputi _Use Case
Diagram_ dengan 5 aktor ( _Guest, Client, Therapist, Admin, Payment Gateway_ ) dan
_use cases_ , serta _Activity Diagram_ untuk 3 proses utama (Proses Reservasi Terapi


oleh Klien, Dokumentasi Sesi Terapi oleh Terapis, dan _Generate_ Laporan oleh
Admin).
Tim merancang arsitektur teknis sistem dengan pola MVC menggunakan
Laravel 10 untuk _backend, Blade Templates_ dan _Tailwind CSS_ untuk _frontend_ ,
MySQL 8.0 untuk basis data, Redis untuk _caching_ , _Laravel Queue_ untuk antrian,
_Midtrans Snap_ API untuk pembayaran, _Nginx_ dan PHP-FPM untuk server, serta
VPS Ubuntu 22.04 LTS untuk _deployment_.
3.2.5. Tahap 5 : Test (Menguji)
Tahap test adalah tahap untuk menguji prototipe dengan pengguna nyata
untuk mendapatkan umpan balik yang digunakan untuk iterasi dan perbaikan.
Aktivitas yang dilakukan meliputi **:**
Tim melakukan pengujian kegunaan dengan 5 responden (2 klien potensial,
2 terapis, 1 admin/staff) menggunakan metode kuesioner _System Usability Scale_
(SUS). Responden diminta menyelesaikan tugas seperti mencari informasi layanan,
melakukan reservasi, dokumentasi sesi, dan membuat laporan.
Hasil skor SUS 78/100 (target ≥70%). Umpan balik kualitatif menunjukkan
responden menyukai desain yang bersih dan modern, proses pemesanan yang
mudah, dan dasbor yang membantu. Masalah yang ditemukan meliputi
kebingungan dengan istilah teknis, ukuran huruf terlalu kecil di seluler, proses
pengalihan pembayaran kurang jelas, tidak ada dialog konfirmasi saat pembatalan,
dan filter yang kurang intuitif.
Setelah validasi akhir dengan pemangku kepentingan dan persetujuan untuk
melanjutkan ke pengembangan, tim berhasil menyelesaikan 5 tahapan _Design
Thinking_ yang memastikan solusi yang dibangun benar-benar menjawab kebutuhan
pengguna dan memiliki peluang sukses yang tinggi di pasar.

```
3.3. Business Model Canvas (BMC)
Business Model Canvas adalah alat manajemen strategis untuk
mengembangkan model bisnis baru atau mendokumentasikan model bisnis yang
sudah ada. BMC CUR-HEART terdiri dari 9 blok bangunan yang saling
terintegrasi.
```

Berikut Gambar _Business Model Canvas_ CUR-HEART mencakup 9
komponen utama :

## Gambar III. 2 Business Model Canvas CUR-HEART


```
Penjelasan 9 blok BMC CUR-HEART
```
1. _Customer Segments_ (Segmen Pelanggan)
    Segmen primer B2C meliputi profesional muda usia 20-35 tahun, individu
dengan masalah kesehatan mental, dan individu yang ingin pengembangan diri.
Segmen sekunder B2B meliputi perusahaan untuk program kesejahteraan
karyawan, universitas untuk konseling mahasiswa, dan rumah sakit/klinik untuk
kemitraan rujukan.
2. _Value Propositions_ (Proposisi Nilai)
    Untuk klien meliputi kemudahan reservasi 24/7, transparansi jadwal dan harga,
keamanan data terenkripsi, kualitas terapis bersertifikat, dan harga kompetitif.
Untuk terapis meliputi efisiensi dokumentasi, akses riwayat klien lengkap, sistem
pembayaran transparan, fleksibilitas jadwal, dan dukungan administratif. Untuk
manajemen meliputi visibilitas dasbor waktu nyata, laporan dan analitik,
skalabilitas sistem, otomasi tugas repetitif, dan kepatuhan regulasi.
3. _Channels_ (Saluran)
    Saluran kesadaran meliputi situs web dan SEO, pemasaran media sosial,
pemasaran konten, SEM, kemitraan influencer, dan liputan media. Saluran evaluasi
meliputi konsultasi gratis, testimoni dan ulasan, serta konten edukatif. Saluran
pembelian meliputi platform situs web dengan sistem pemesanan daring 24/7 dan
gerbang pembayaran terintegrasi. Saluran pengiriman meliputi sesi luring di klinik
Jakarta Selatan dan sesi daring melalui konferensi video. Saluran purna jual
meliputi tindak lanjut surel, dukungan pelanggan via WhatsApp dan surel, serta
program loyalitas.
4. _Customer Relationships_ (Hubungan Pelanggan)
    Untuk klien meliputi bantuan personal melalui layanan pelanggan responsif,
layanan mandiri melalui portal klien, layanan otomatis melalui notifikasi surel, dan
komunitas daring (masa depan). Untuk terapis meliputi dukungan khusus dan
komunitas terapis untuk berbagi pengetahuan. Untuk perusahaan B2B meliputi
manajemen akun khusus dan ko-kreasi program.
5. _Revenue Streams_ (Aliran Pendapatan)
    Model pendapatan berbasis transaksi meliputi sesi terapi individual (Rp
300.000-500.000/sesi) dan konsultasi daring (Rp 200.000/sesi). Model


berlangganan meliputi paket bulanan (Rp 1.200.000 untuk 4 sesi) dan paket
triwulanan (Rp 3.200.000 untuk 12 sesi). Kontrak B2B meliputi program korporat
(Rp 10-50 juta/tahun) dan program universitas (Rp 20-100 juta/tahun). Pelatihan
dan sertifikasi meliputi pelatihan hipnoterapi (Rp 5-15 juta/batch) dan sertifikasi
terapis (Rp 3 juta/orang). Proyeksi pendapatan tahun pertama adalah Rp 1,2 miliar
dengan break-even di bulan ke-8.

6. _Key Resources (Sumber Daya Utama)_
    Sumber daya manusia meliputi 3 terapis bersertifikat, tim pengembangan
(CEO, CTO, CMO), 2 admin dan layanan pelanggan, serta keuangan dan akuntansi
(outsource). Sumber daya fisik meliputi ruang terapi di Jakarta Selatan dan
peralatan terapi. Sumber daya intelektual meliputi platform web Laravel, merek dan
kekayaan intelektual, basis data klien, konten dan basis pengetahuan, serta
metodologi dan SOP. Sumber daya keuangan meliputi modal awal Rp 200 juta dan
pendapatan setelah peluncuran.
7. _Key Activities_ (Aktivitas Utama)
    Aktivitas meliputi penyampaian layanan terapi hipnoterapi, pengembangan
dan pemeliharaan platform, pemasaran dan akuisisi pelanggan, layanan dan
dukungan pelanggan, jaminan kualitas dan kepatuhan, serta pelatihan dan
pengembangan.
8. _Key Partnerships_ (Kemitraan Utama)
    Kemitraan strategis meliputi Asosiasi Hipnoterapi Indonesia, lembaga
sertifikasi terapis, perusahaan untuk program kesejahteraan, universitas, dan rumah
sakit/klinik. Kemitraan teknologi meliputi gerbang pembayaran Midtrans, penyedia
layanan surel, penyedia hosting cloud, dan penyedia domain dan SSL. Kemitraan
pemasaran meliputi influencer dan kreator konten, media dan publikasi, serta agensi
SEO/SEM (opsional). Kemitraan operasional meliputi layanan keuangan dan
akuntansi, konsultan hukum, dan dukungan TI (opsional).
9. _Cost Structure_ (Struktur Biaya)
    Biaya tetap meliputi gaji terapis dan staf (Rp 13 juta/bulan), sewa dan utilitas
(Rp 17,5 juta/bulan), teknologi (Rp 1,08 juta/bulan), dan asuransi dan hukum (Rp
1,5 juta/bulan) dengan total Rp 33,08 juta/bulan. Biaya variabel meliputi biaya
terapis (80% dari biaya sesi), biaya gerbang pembayaran (2,9% + Rp 2.000 per


transaksi), pemasaran dan iklan (Rp 10 juta/bulan), akuisisi pelanggan (Rp 3
juta/bulan), dan operasional (Rp 2 juta/bulan) dengan total Rp 55,03 juta/bulan.
Biaya pengembangan satu kali adalah Rp 86,8 juta dan biaya penyiapan peralatan
Rp 50 juta.
Business Model Canvas CUR-HEART menunjukkan model bisnis yang solid
dengan proposisi nilai yang jelas, aliran pendapatan yang terdiversifikasi, platform
yang dapat diskalakan, kemitraan yang kuat, dan ekonomi yang berkelanjutan
dengan break-even di bulan ke-8 dan margin yang sehat. Model bisnis ini telah
divalidasi melalui riset pasar, pengujian pengguna, dan pemodelan keuangan, siap
untuk eksekusi dan penskalaan.

**_3.4. Pitch Deck_**
_Pitch deck_ adalah presentasi singkat yang menjelaskan gambaran umum
tentang rencana bisnis CUR-HEART kepada calon investor, mitra, atau pemangku
kepentingan. Pitch deck dirancang mengikuti praktik terbaik dengan 1 1 slide utama
yang mencakup. Berikut gambar-gambar _Pitch Deck_ dibawah ini :

1. _Slide_ 1 (Pembukaan)

## Gambar III. 3 Pich Deck Pembukaan


2. _Slide_ 2 (Permasalahan)

## Gambar III. 4 Pitch Deck Permasalahan

3. _Slide 3_ (Nilai Lebih)

## Gambar III. 5 Pitch Deck Nilai Lebih CUR-HEART


4. _Slide_ 4 (Besaran Pasar)

## Gambar III. 6 Pitch Deck Besaran Pasar

5. _Slide_ 5 (Model Bisnis)

## Gambar III. 7 Pitch Deck Model Bisnis


6. _Slide_ 6 (Rencana Pemasaran)

## Gambar III. 8 Picth Deck Rencana Pemasaran

7. _Slide_ 7 (Analisis Kompetisi)

## Gambar III. 9 Pich Deck Analisis Kompetisi


8. _Slide_ 8 (Tim Manajemen)

## Gambar III. 10 Pitch Deck Tim Manajemen

9. _Slide_ 9 (Proyeksi Keuangan)

## Gambar III. 11 Pitch Deck Proyeksi Keuangan


10. _Slide_ 10 (Pencapaian & Rencana)

## Gambar III. 12 Pich Deck Pencapaian & Rencana

11. _Slide_ 11 (Penutup)

## Gambar III. 13 Pitch Deck Penutup


##### 32

## BAB IV ANALISA DAN PERANCANGAN APLIKASI START-UP

### 4.1. Analisa Kebutuhan

Analisa kebutuhan dilakukan untuk mengidentifikasi kebutuhan fungsional
dan non-fungsional sistem informasi CUR-HEART berdasarkan hasil riset
pengguna dan analisis proses bisnis.

#### 4.1.1. Analisis Kebutuhan Aplikasi

Berdasarkan hasil wawancara, observasi, dan survei yang telah dilakukan,
teridentifikasi kebutuhan aplikasi sebagai berikut :
A. Kebutuhan Fungsional
Kebutuhan fungsional sistem CUR-HEART mencakup :
Untuk Tamu : Menampilkan informasi bisnis, katalog layanan, direktori
terapis, blog, FAQ, formulir kontak, registrasi, dan login.
Untuk Klien : Dashboard, reservasi online, pilih terapis dan jadwal, payment
gateway, email konfirmasi dan reminder, riwayat reservasi, progress tracking,
reschedule/cancel, rating dan review, akses catatan sesi, update profil, dan
notifikasi.
Untuk Terapis **:** Dashboard, jadwal sesi, daftar klien, atur ketersediaan,
dokumentasi sesi dengan template, akses riwayat klien, timeline progress, update
status sesi, dashboard pendapatan, withdrawal, update profil, notifikasi, dan lihat
rating.
Untuk Admin : Dashboard dengan metrik, grafik analitik, CRUD
pengguna/layanan/reservasi, approve terapis, verifikasi pembayaran, kelola
_withdrawal_ , _generate_ laporan, _export Excel_ /PDF, kelola konten (blog, FAQ,
promo), moderasi _review_ , audit log, dan konfigurasi sistem.
Untuk Sistem ( _Automated_ ) : Deteksi konflik jadwal, kirim email otomatis,
update status pembayaran, hitung pendapatan terapis, buat notifikasi, backup
database harian, dan audit logging.
B. Kebutuhan Non-Fungsional

1. _Performance_ **:** Waktu muat halaman < 2 detik, respons API < 500ms, kueri
    basis data < 100ms, menangani 100 pengguna bersamaan, 500 transaksi/hari


2. _Security_ : Enkripsi data sensitif, HTTPS, pencegahan SQL
    injection/XSS/CSRF, RBAC, kepatuhan UU PDP, hashing kata sandi
    bcrypt, pembatasan laju, pencatatan audit
3. _Usability_ : Antarmuka intuitif, skor SUS ≥ 70/100, tingkat penyelesaian
    tugas ≥ 90%, pesan kesalahan jelas, kepatuhan WCAG 2.1 Level AA,
    navigasi keyboard
4. _Reliability_ : Waktu aktif ≥ 99%, MTBF > 720 jam, RTO < 4 jam, RPO < 24
    jam, pencadangan otomatis harian, rencana pemulihan bencana
5. _Scalability_ : Penskalaan horizontal, menangani pertumbuhan data 10x,
    replikasi basis data, _caching_ , antrian untuk pekerjaan latar belakang
6. _Maintainability_ : Standar pengkodean PSR-12, cakupan pengujian ≥ 70%,
    komentar inline, dokumentasi API, kontrol versi Git, versi semantik
7. _Portability_ : Dukungan multi-lingkungan, multi-OS, kontainerisasi Docker,
    konfigurasi lingkungan terpisah
8. _Compatibility_ **:** Peramban modern ( _Chrome, Firefox, Safari, Edge_ ), desain
    responsif, kompatibel pembaca layar
9. _Localization_ : Bahasa Indonesia, format tanggal DD/MM/YYYY, mata
    uang Rupiah, zona waktu WIB
10. _Legal & Compliance_ **:** Kepatuhan UU PDP, Syarat Layanan, Kebijakan
    Privasi, mekanisme persetujuan, kebijakan retensi data, hak untuk
    dilupakan
C. Prioritas Kebutuhan (MoSCoW Method)
1. _Must Have_ (MVP - Phase 1) **:**
a) Sistem reservasi online dengan wizard 4 langkah
b) Manajemen jadwal terapis dengan deteksi konflik
c) Integrasi payment gateway (Midtrans)
d) Dashboard untuk klien, terapis, dan admin
e) Dokumentasi sesi terapi digital
f) Sistem notifikasi email otomatis
g) Autentikasi dan otorisasi _multi-role_
h) _Security features (encryption, HTTPS, CSRF protection)_


2. _Should Have_ (Phase 2) **:**
    a) _Mobile app_ (iOS & Android)
    b) _Video conference_ untuk terapi online
    c) _Chatbot_ untuk FAQ
    d) _Advanced analytics_ dan _reporting_
    e) _Loyalty_ program dan _referral system_
    f) SMS notification
3. _Could Have_ (Phase 3) :
    a) _AI recommendation_ untuk terapis
    b) _Gamification_ untuk engagement
    c) _Community forum_
    d) _Integration_ dengan _wearable devices_
    e) _Multi-language support_
4. _Won't Have (Out of Scope)_ :
    a) Diagnosis medis otomatis
    _b) Prescription management_
    c) _Insurance integration_ (tahap awal)
    _d) Multi-currency support_

#### 4.1.2. Rancangan Diagram Use Case

_Use Case_ Diagram menggambarkan interaksi antara aktor (pengguna)
dengan sistem, serta fungsionalitas yang dapat dilakukan oleh masing-masing aktor
dalam sistem informasi CUR-HEART.


```
Berikut dibawah ini gambar Use Case Diagram CUR-HEART:
```
Sumber : Hasil Penelitian ( _PlantUML_ )

## Gambar IV. 1 Use Case Diagram Sistem Informasi CUR-HEART


Aktor dalam Sistem :

1. _Guest_ (Tamu) **-** Pengunjung website yang belum login
2. _Client_ (Klien) **-** Pengguna terdaftar yang menggunakan layanan terapi
3. _Therapist_ (Terapis) - Praktisi hipnoterapi yang memberikan layanan
4. Admin ( _Administrator_ ) - Pengelola sistem
5. _Payment Gateway_ - Sistem eksternal untuk pemrosesan pembayaran
    (Midtrans)

_Use Case Diagram_ menggambarkan interaksi antara 5 aktor ( _Guest, Client,
Therapist, Admin, Payment Gateway_ ) dengan sistem. Diagram mencakup 40+ _use
cases_ yang terdistribusi untuk setiap aktor, termasuk proses reservasi, pembayaran,
dokumentasi sesi, manajemen pengguna, dan pelaporan.
Penjelasan _Use Case_ Utama **:**

1. _Make Booking (Klien)_
    1) _Aktor_ : _Client_
    2) Deskripsi : Klien melakukan reservasi layanan terapi melalui _wizard_ 4
       langkah
    3) _Precondition_ : Klien sudah login
    4) _Flow_ :
       a. Klien memilih layanan terapi
       b. Klien memilih terapis (atau auto-assign)
       c. Klien memilih tanggal dan waktu
       d. Klien melakukan pembayaran via Midtrans
       e. Sistem mengirim konfirmasi email
    5) _Postcondition_ **:** Booking berhasil dibuat dengan status " _Paid_ "
2. _Document Session_ (Terapis)
    1) Aktor : _Therapist_
    2) Deskripsi : Terapis mendokumentasikan sesi terapi yang sudah
       dilaksanakan
    3) _Precondition_ : Terapis sudah login, sesi sudah dilaksanakan
    4) _Flow_ :


```
a. Terapis memilih sesi dari jadwal
b. Terapis mengisi formulir dokumentasi (teknik, observasi, progress,
rekomendasi)
c. Terapis menyimpan dokumentasi
d. Sistem update status sesi menjadi " Completed "
5) Postcondition : Dokumentasi tersimpan dan dapat diakses untuk sesi
berikutnya
```
3. _Generate Reports_ (Admin)
    1) Aktor : Admin
    2) Deskripsi : Admin membuat laporan untuk monitoring dan decision
       making
    3) _Precondition_ : Admin sudah _login_
    4) _Flow_ :
       a. Admin memilih jenis laporan ( _booking, financial, performance_ )
       b. Admin memilih periode dan filter
       c. Sistem _generate_ laporan dengan grafik dan tabel
       d. Admin dapat _view, export_ ( _Excel/PDF_ ), atau print
    5) _Postcondition_ : Laporan berhasil dibuat dan dapat diakses


#### 4.1.3. Rancangan Diagram Aktivitas

```
Activity Diagram menggambarkan alur aktivitas dalam sistem untuk berbagai
proses bisnis. Berikut adalah 3 activity diagram utama sesuai dengan proses bisnis
CUR-HEART :
A. Activity Diagram : Proses Reservasi Terapi oleh Klien
Berikut dibawah ini gambar Activity Diagram untuk proses reservasi terapi
oleh klien :
```
```
Sumber : Hasil Penelitian ( Plant UML )
```
## Gambar IV. 2 Activity Diagram Proses Reservasi Terapi oleh Klien


```
Penjelasan Alur :
```
1. Klien login ke sistem dengan _credentials_
2. Sistem verifikasi dan memberikan akses
3. Klien memilih layanan terapi yang diinginkan
4. Klien memilih terapis berdasarkan spesialisasi dan jadwal
5. Klien memilih tanggal dan waktu sesi
6. Sistem mengecek ketersediaan jadwal (jika tidak tersedia, kembali ke step
    5)
7. Klien mengisi informasi tambahan (keluhan, catatan)
8. Sistem menampilkan ringkasan reservasi dan total biaya
9. Klien konfirmasi reservasi
10. Sistem membuat booking dengan status " _Pending Payment_ "
11. Sistem _redirect_ ke _payment gateway_ ( _Midtrans_ )
12. Klien melakukan pembayaran
13. Payment gateway memproses transaksi
14. Jika gagal : _Update_ status " _Payment Failed_ ", _klien_ dapat coba lagi
15. Jika berhasil : _Update_ status " _Paid_ ", kirim email konfirmasi, notifikasi
    terapis, schedule reminder
16. Reservasi berhasil dibuat


B. _Activity Diagram:_ Dokumentasi Sesi Terapi oleh Terapis
Berikut dibawah ini gambar _Activity Diagram_ untuk proses dokumentasi sesi
terapi oleh terapis :

Sumber : Hasil Penelitian ( _Plant UML_ )

## Gambar IV. 3 Activity Diagram Dokumentasi Sesi Terapi oleh Terapis


```
Penjelasan Alur :
```
1. Terapis _login_ ke sistem
2. Terapis melihat jadwal sesi hari ini
3. Terapis memilih sesi yang sudah dilaksanakan
4. Sistem menampilkan detail sesi dan informasi klien
5. Terapis klik " _Document Session_ "
6. Sistem menampilkan formulir dokumentasi dengan _template_
7. Terapis mengisi dokumentasi (teknik, observasi, kemajuan, catatan,
    rekomendasi)
8. Sistem melakukan _auto-save_ setiap 30 detik untuk mencegah data loss
9. Terapis _klik_ " _Save_ " untuk menyimpan final
10. Sistem validasi data (jika tidak valid, tampilkan _error_ dan kembali ke _form_ )
11. Jika valid : Simpan dokumentasi, _update status_ sesi " _Completed_ ", catat
    timestamp
12. Sistem menghitung durasi dokumentasi untuk metrics
13. Dokumentasi berhasil tersimpan dan dapat diakses untuk sesi berikutnya


```
C. Activity Diagram : Generate Laporan oleh Admin
Berikut dibawah ini gambar Activity Diagram untuk generate laporan oleh
admin :
```
## Gambar IV. 4 Activity Diagram Generate Laporan oleh Admin

Sumber : Hasil Penelitian ( _PlantUML_ )
**Gambar 4.4** **_Activity Diagram Generate_** **Laporan oleh Admin**
Penjelasan Alur :

1. Admin login ke sistem
2. Admin mengakses menu "Reports"
3. Admin memilih jenis laporan (Booking, Financial, Performance, Client)


4. Sistem menampilkan form filter
5. Admin memilih periode (tanggal mulai - tanggal selesai)
6. Admin memilih filter tambahan (terapis, layanan, status)
7. Admin klik "Generate Report"
8. Sistem validasi input (jika tidak valid, tampilkan error)
9. Jika valid: Query database sesuai kriteria
10. Sistem memproses dan menghitung statistik
11. Sistem generate grafik dan chart untuk visualisasi
12. Sistem format data dalam tabel
13. Sistem menampilkan laporan
14. Admin dapat memilih aksi:
    a. View : Tampilkan di browser
    b. Export Excel : Download file Excel
    c. Export PDF: Download file PDF
    d. Print : Print langsung
15. Laporan selesai dibuat dan dapat digunakan untuk decision making

#### 4.1.4. Rancangan User Interface

Rancangan _User Interface_ (UI) CUR-HEART telah dibuat menggunakan
Figma dengan total 66 halaman _mockup_ yang mencakup semua peran pengguna.
Desain mengikuti prinsip user-centered design dengan fokus pada kemudahan
penggunaan, aksesibilitas, dan pengalaman pengguna yang optimal.
A. _Design System
Color Palette_ :
1) _Primary Color_ : Teal (#0D9488)
a) Melambangkan ketenangan, profesionalisme, dan penyembuhan
b) Digunakan untuk: Button primary, link, header
2) _Secondary Color_ : _Purple_ (#9333EA)
a) Melambangkan spiritualitas dan transformasi
b) Digunakan untuk: Accent elements, highlights
3) _Accent Color_ : _Orange_ (#F59E0B)
a) Melambangkan energi dan optimisme
b) Digunakan untuk: Call-to-action, notifications


4) _Neutral Colors_ : Skala abu-abu dari #F9FAFB (lightest) hingga #111827
(darkest)
a) Digunakan untuk: Background, text, borders
5) _Semantic Colors_ :
a) _Success_ : _Green_ (#10B981)
b) _Warning_ : _Yellow_ (#F59E0B)
c) _Error_ : _Red_ (#EF4444)
d) _Info_ : _Blue_ (#3B82F6)
_Typography_ :
1) _Font Family_ : _Inter_ ( _Sans-serif_ )
a) Modern, clean, dan mudah dibaca
b) Mendukung berbagai weight (300-900)
2) _Font Sizes_ :
a) H1: 36px (2.25rem) - Page titles
b) H2: 30px (1.875rem) - Section titles
c) H3: 24px (1.5rem) - Subsection titles
d) H4: 20px (1.25rem) - Card titles
e) Body: 16px (1rem) - Regular text
f) Small: 14px (0.875rem) - Helper text, captions
g) Tiny: 12px (0.75rem) - Labels, badges
_Spacing System_ (Tailwind CSS scale) :
1) 0.25rem (4px), 0.5rem (8px), 0.75rem (12px), 1rem (16px)
2) 1.5rem (24px), 2rem (32px), 3rem (48px), 4rem (64px)
_Border Radius_ **:**
_1) Small_ : 0.25rem (4px) - _Buttons, inputs_
2) _Medium_ : 0.5rem (8px) - _Cards_
3) _Large_ : _1rem_ (16px) - _Modals, large cards_
4) _Full_ : 9999px - _Pills, avatars
Shadows_ :
1) _Small_ : 0 1px 2px rgba(0,0,0,0.05)
2) _Medium_ : 0 4px 6px rgba(0,0,0,0.1)
3) _Large_ : 0 10px 15px rgba(0,0,0,0.1)


B. _Mockup_ Halaman Utama
Rancangan _User Interface_ CUR-HEART telah dibuat menggunakan Figma
dengan total 66 halaman _mockup_ yang mencakup semua peran pengguna. Berikut
adalah mockup halaman-halaman kunci dalam sistem :

1. Halaman Publik (12 halaman)

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 5 Mockup Landing Page CUR-HEART


Sumber: Hasil Penelitian _(Figma Design)_

## Gambar IV. 6 Mockup Halaman Tentang Kami


Sumber : Hasil Penelitian _(Figma Design)_

## Gambar IV. 7 Mockup Katalog Layanan


Sumber : Hasil Penelitian _(Figma Design)_

## Gambar IV. 8 Mockup Detail Layanan


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 9 Mockup Direktori Terapis


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 10 Mockup Direktori Terapis


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 11 Mockup Daftar Blog


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 12 Mockup Detail Blog


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 13 Mockup Hubungi Kami


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 14 Mockup FAQ


Sumber : Hasil Penelitian ( _Figma Design_ )
**Gambar IV. 15** **_Mockup Kebijakan Privasi_**


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 16 Mockup Syarat & Ketentuan


2. Halaman Autentikasi (4 halaman)

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 17 Mockup Login

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 18 Mockup Registrasi Klien


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 19 Mockup Registrasi Terapis


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 20 Mockup Lupa Kata Sandi

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 21 Mockup Reset Kata Sandi


3. _Dashboard_ Klien (12 halaman)

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 22 Mockup Client Dashboard

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 23 Mockup Booking Step 1 - Select Service


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 24 Mockup Booking Step 2 - Select Therapist

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 25 Mockup Booking Step 3 - Select Schedule


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 26 Mockup Booking Step 4 - Konfirmasi & Pembayaran

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 27 Mockup Booking Success


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 28 Mockup Janji Temu Saya

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 29 Mockup Detail Janji Temu


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 30 Mockup Progress Tracking

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 31 Mockup Pesan (Chat)


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 32 Mockup Pengaturan Klien


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 33 Mockup Notifikasi Klien

4. _Dashboard_ Terapis (13 halaman)

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 34 Mockup Therapist Dashboard


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 35 Mockup Manajemen Jadwal


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 36 Mockup Pengaturan Ketersediaan

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 37 Mockup Daftar Klien


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 38 Mockup Profil Klien (View)

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 39 Mockup Ruang Sesi


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 40 Mockup Formulir Catatan Sesi

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 41 Mockup Riwayat Sesi


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 42 Mockup Dashboard Pendapatan


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 43 Mockup Edit Profil Terapis


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 44 Mockup Pengaturan Terapis


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 45 Mockup Pesan Terapis

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 46 Mockup Notifikasi Terapis


5. _Dashboard_ Admin (25 halaman)

Sumber : Hasil Penelitian ( _Figma Design_ )
**Gambar IV. 47** **_Mockup Admin Dashboard_**

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 48 Mockup Manajemen Reservasi


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 49 Mockup Manajemen Pengguna

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 50 Mockup Laporan Keuangan


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 51 Mockup Pengaturan Sistem

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 52 Mockup Notifikasi Admin


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 53 Mockup Pesan Admin

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 54 Mockup Detail Pengguna


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 55 Mockup Edit Pengguna

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 56 Mockup Detail Reservasi


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 57 Mockup Manajemen Transaksi

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 58 Mockup Manajemen Penarikan


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 59 Mockup Detail Penarikan

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 60 Mockup Log Aktivitas


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 61 Mockup Laporan & Analitik

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 62 Mockup Manajemen Konten Blog


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 63 Mockup Manajemen Konten FAQ

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 64 Mockup Manajemen Konten Layanan


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 65 Mockup Manajemen Ulasan

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 66 Mockup Manajemen Promo


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 67 Mockup Verifikasi Terapis

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 68 Mockup Editor Blog


Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 69 Mockup Editor FAQ

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 70 Mockup Editor Layanan

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 71 Mockup Editor Promo


#### 4.1.5. Rancangan Database

Rancangan _database_ sistem informasi CUR-HEART _menggunakan Entity
Relationship Diagram_ (ERD) dan _Logical Record Structure_ (LRS) yang telah
dinormalisasi hingga Third Normal Form (3NF) untuk menghindari _redundansi_
data dan menjaga integritas data.
**_A. Entity Relationship Diagram (ERD)_**
ERD menggambarkan struktur database dengan 16 tabel utama dan
relationships antar entitas.
Berikut dibawah ini merupakan gambar ERD CUR-HEART:


## Gambar IV. 72 Entity Relationship Diagram (ERD) CUR-HEART


Penjelasan Entitas Utama **:**

1. _Users_ - Tabel induk untuk semua pengguna sistem
    a. Menyimpan data universal : name, _email, password, role_
       ( _client/therapist/admin_ )
    b. Relasi 1:1 dengan clients atau _therapists_ tergantung _role_
2. _Clients_ - Data spesifik klien
    a. _Extends_ dari users dengan data tambahan : _phone, address, dob, gender_
    b. Relasi 1: M dengan _bookings_ (satu klien bisa punya banyak _booking_ )
3. _Therapists_ - Data spesifik terapis
    _a. Extends_ dari _users_ dengan data professional : _specialization, experience,_
       _license_no, bio, rating_
    b. Relasi M : M dengan _services_ melalui _therapist_services_
    c. Relasi 1: M dengan _bookings_
4. _Services_ - Katalog layanan terapi
    a. Menyimpan : name, _description, duration, price, category_ , status
    b. Relasi M:M dengan _therapists_
5. _Therapist_Services_ - _Junction table_ untuk M:M _relationship_
    a. Menghubungkan _therapists_ dan _services_
    b. Memungkinkan satu terapis menangani banyak layanan
6. _Therapist_Availability_ - Jadwal ketersediaan terapis
    a. Menyimpan jadwal per hari: _day_of_week, start_time, end_time,_
       _is_available_
    b. Digunakan untuk _checking_ ketersediaan saat _booking_
7. _Bookings_ - Data reservasi
    a. _Core table_ yang menghubungkan _client, therapist, service_
    b. Menyimpan : _booking_date, start_time, end_time, type_ ( _online/offline_ ),
       status, total_ _price_
    c. Relasi 1:1 dengan _payments_
    d. Relasi 1:1 dengan _sessions_
8. _Payments_ - Transaksi pembayaran
    a. Menyimpan: _amount, method, status, paid_at, midtrans_id_
    b. Terintegrasi dengan _Midtrans payment gateway_


9. _Sessions_ - Data sesi terapi yang sudah dilaksanakan
    a. Menyimpan : _session_date, start_time, end_time, status_
    b. Relasi 1:M dengan session_notes
10. _Session_Notes_ - Catatan dokumentasi sesi
    a. Menyimpan : _technique, observation, progress, notes, recommendation_
    b. Diisi oleh terapis setelah sesi
11. _Reviews_ - Ulasan dan rating dari klien
    a. Menyimpan : _rating_ (1-5), _comment_
    b. Relasi dengan _booking, client, therapist_
12. _Promo_Codes_ - Kode promo dan diskon
    Menyimpan : _code, discount_type, discount_value, valid_from, valid_until,
usage_limit_
13. _Notifications_ - Notifikasi untuk pengguna
    a. Menyimpan : _type, title, message, read_at_
    b. Relasi dengan _users_
14. _Messages_ - Pesan/chat antara pengguna
    a. Menyimpan : _sender_id, receiver_id, booking_id, message, read_at_
    b. Untuk komunikasi klien-terapis
15. _Withdrawals_ - Permintaan penarikan dana terapis
    a. Menyimpan : _amount, status, requested_at, processed_at_
    b. Relasi dengan _therapists_
16. _Activity_Logs_ - Log aktivitas untuk audit trail
    a. Menyimpan : _action, description, ip_address, user_agent_
    b. Untuk _security_ dan _compliance_
17. _System_Settings_ - Konfigurasi sistem
    a. Menyimpan : _key-value pairs_ untuk settings
    b. Contoh : _site_name, maintenance_mode, payment_gateway_key_


##### 91

**_B. Logical Record Structure (LRS)_**
LRS menunjukkan struktur logis dari tabel-tabel _database_ dengan _detail field_ , tipe data, dan _constraints_.

## Gambar IV. 73 Logical Record Structure (LRS) CUR-HEART


1. _Normalisasi Database_ **:**
    Database CUR-HEART telah dinormalisasi hingga _Third Normal Form_
(3NF) dengan karakteristik :
1) 1NF ( _First Normal Form_ ) **:**
a. Setiap kolom berisi nilai atomic (tidak ada _multi-value_ )
b. Setiap baris unik (ada _primary key_ )
c. Tidak ada _repeating groups_
2) 2NF ( _Second Normal Form_ ) **:**
a. Memenuhi 1NF
b. Tidak ada partial dependency (semua _non-key attributes fully dependent_
pada _primary key_ )
Contoh : _therapist_services_ terpisah dari _therapists_ dan _services_
3) 3NF (Third Normal Form) **:**
a. Memenuhi 2NF
b. Tidak ada _transitive dependency_ ( _non-key attributes_ tidak _dependent_ pada
_non-key attributes_ lain)
Contoh : _clients_ dan therapists terpisah dari _users_ untuk menghindari _null
values_
4) _Indexing Strategy_ :
Untuk optimasi _performa query,_ diterapkan _indexing_ pada:
a. _Primary keys_ ( _automatic_ )
b. _Foreign keys_ (untuk JOIN operations)
c. Kolom yang sering di- _query_ : _email, status, booking_date, created_at_
d. _Composite index_ untuk _query_ kombinasi : ( _user_id, read_at_ ) pada
_notifications_
5) Data _Integrity_ :
a. _Referential Integrity_ : _Foreign key constraints_ untuk menjaga konsistensi
relasi
b. _Domain Integrity_ : ENUM types untuk membatasi nilai yang valid
c. _Entity Integrity_ : Primary key NOT NULL dan UNIQUE
d. _User-defined Integrity_ : CHECK constraints dan triggers untuk business
rules


### 4.2. Implementasi

Implementasi sistem informasi CUR-HEART dilakukan menggunakan
teknologi modern dengan fokus pada kualitas kode, performa, dan _maintainability_.
Berikut adalah detail proses dan hasil implementasi.

#### 4.2.1. Proses Implementasi

Proses implementasi mengikuti metodologi _Agile_ dengan _2 - week sprints_ dan
menggunakan _tech stack_ yang telah ditentukan.
_A. Technology Stack_

1. _Backend_ :
    a) _Framework : Laravel 12.x (PHP 8.3)_
    b) _Database : MySQL 8.0_
    c) _Authentication : Laravel Sanctum_
    d) _API : RESTful API_
    e) _Queue : Laravel Queue (database driver)_
    f) _Cache : Redis (optional, file cache untuk development_ )
2. _Frontend_ :
    a) _Template Engine_ : _Blade Templates_
    b) _CSS Framework_ : _Tailwind CSS 3.x_
    c) _JavaScript_ : _Alpine.js_ (untuk _interaktivity_ )
    d) _Icons_ : _Heroicons_
    e) _Charts_ : _Chart.js_
3. _Third-Party Integrations_ :
    a) _Payment Gateway_ : _Midtrans Snap API_
    b) _Email Service_ : SMTP / _SendGrid_
    c) _File Storage_ : _Local storage (development)_ , AWS S3 ( _production_ )
4. _Development Tools_ :
    a) _Version Control : Git & GitHub_
    b) _IDE : Visual Studio Code_
    c) _Package Manager : Composer (PHP), NPM (JavaScript)_
    d) _Build Tool : Vite_
    e) _Testing : PHPUnit, Laravel Dusk_


5. _Deployment_ :
    a) _Server : VPS Ubuntu 22.04 LTS_
    b) _Web Server : Nginx_
    c) _PHP : PHP-FPM 8.3_
    d) _Process Manager : Supervisor (untuk queue workers)_
    e) _SSL : Let's Encrypt
B. Development Workflow_
1. Lingkungan Pengembangan : Pengembangan dilakukan menggunakan
Git untuk kontrol versi dengan strategi percabangan ( _main, develop,
feature branches_ ) dan proses tinjauan kode sebelum penggabungan.
2. Proses _Deployment_ : _Deployment_ dilakukan melalui tahapan pull kode
terbaru, instalasi dependensi, migrasi basis data, optimasi cache, build
aset, dan restart layanan.
3. _Code Review_ : Setiap fitur baru harus melalui _Pull Request_
a) Minimal 1 _reviewer approval_ sebelum _merge_
b) _Automated tests_ harus pass
c) _Code quality check_ dengan _PHP CodeSniffer
4. Deployment Process_
# Pull latest code
git pull origin main
# Install/update dependencies
composer install --optimize-autoloader --no-dev
npm install --production
# Run migrations
php artisan migrate --force
# Clear and cache config
php artisan config:cache
php artisan route:cache
php artisan view:cache
# Build assets
npm run build


# Restart services
sudo systemctl restart php8.2-fpm
sudo systemctl restart nginx
sudo supervisorctl restart all
_C. Fitur Utama Implementasi_
Implementasi sistem mencakup fitur-fitur utama yaitu sistem pemesanan
dengan deteksi konflik jadwal otomatis, integrasi gerbang pembayaran _Midtrans
Snap API_ , sistem _notifikasi_ surel otomatis berbasis antrian, dan formulir
dokumentasi sesi dengan fitur penyimpanan otomatis.

#### 4.2.2. Hasil Implementasi

Berikut adalah beberapa contoh tampilan hasil implementasi sistem CUR-
HEART yang telah jadi dan siap dioperasikan.

1. Halaman Utama ( _Landing Page_ )

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 74 Tampilan Halaman Utama


Halaman _landing page_ menampilkan hero section dengan CTA " _Book Your
Session Now_ ", _statistics section_ (500+ _Clients_ , 15+ _Therapists_ , 4.8/5 _Rating_ ),
_services grid_ dengan 6 layanan terapi, _featured therapists_ dengan foto dan rating,
_client testimonials carousel_ , dan _footer_ dengan _links_ dan _contact_ info.

2. Halaman Booking - Step 1: _Select Service_

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 75 Booking Step 1 - Select Service

Halaman menampilkan progress indicator (Step 1 of 4 active), _list of services_
dengan radio _button selection_ , setiap _service_ menampilkan nama, durasi, harga,
deskripsi, dan button " _Next_ : _Select Therapist_ " di _bottom right_.


3. Halaman Booking - Step 3: _Select Schedule_

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 76 Tampilan Booking Step 3 - Select Schedule

Halaman menampilkan calendar picker untuk pilih tanggal, time slots grid
menampilkan _available_ / _booked slots_ ( _available slots_ : _hijau clickable, booked slots:
abu-abu disabled, selected slot : biru highlighted_ ), dan _real-time availability
checking._

4. Halaman _Payment_

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 77 Tampilan Payment


Halaman menampilkan payment methods ( _Credit Card_ , Bank Transfer, _E-
Wallet_ ), _order summary_ dengan detail _booking_ , total _amount_ yang harus dibayar.

5. _Client Dashboard_

Sumber : Hasil Penelitian ( _Figma Design_ )

## Gambar IV. 78 Tampilan Client Dashboard

_Dashboard_ menampilkan welcome message dengan nama _user_ , 4 stat cards
( _Upcoming Sessions, Completed, Total Hours, Progress_ ), _next appointment card_
dengan detail lengkap, _progress tracking chart_ ( _line chart mood score_ ), _recent
sessions list_ dengan status dan rating, serta _responsive layout_ dengan _clean design_.

6. _Therapist Dashboard_

Sumber : Hasil Penelitian ( _Figma Design_ )
**Gambar IV. 79 Tampilan** **_Therapist Dashboard_**


_Dashboard_ menampilkan _good morning greeting_ dengan nama terapis, 4 stat _cards_
( _Today's Sessions_ , _This Week_ , _Total Clients_ , _Avg Rating_ ), _today's schedule list_
dengan detail setiap sesi, pending _documentation alert_ dengan _action button_ ,
_earnings this month card_ dengan total dan _withdrawal button_ , serta professional
_clean interface_.

7. _Session Documentation Form_

Sumber : Hasil Penelitian ( _Figma Design_ )
**Gambar IV. 80 Tampilan** **_Session Documentation Form_**


```
Form menampilkan client info header (nama, foto, session number ), form fields
dengan rich text editor ( Technique Used, Client Condition, Progress Achieved,
Important Notes, Recommendations ), auto-save indicator " Last saved : 2 minutes
ago ", dan save button di bottom right.
```
8. _Admin Dashboard_

```
Sumber : Hasil Penelitian ( Figma Design )
Gambar IV. 81 Tampilan Admin Dashboard
Dashboard menampilkan 4 KPI cards ( Total Users, Total Bookings, Total
Therapists, Revenue) , revenue trend chart ( line chart 12 months ), recent bookings
table dengan pagination , pending actions alert ( therapist applications,
withdrawals, reviews ), top performing therapists list , dan comprehensive admin
interface.
```
### 4.3. Spesifikasi Aplikasi

```
Spesifikasi aplikasi mencakup hardware dan software yang digunakan untuk
pengembangan dan deployment sistem CUR-HEART.
```
#### 4.3.1. Hardware

```
A. Development Environment
Laptop/ PC Development (Tim - 3 unit) :
1) Processor : Intel Core i5/i7 atau AMD Ryzen 5/7 (minimal)
```

```
2) RAM : 8GB DDR4 (minimal), 16GB (recommended)
3) Storage : 256GB SSD (minimal), 512GB SSD (recommended)
4) Display : 14" Full HD (1920x1080)
5) OS : Windows 10/11, macOS, atau Linux Ubuntu
B. Production Environment
VPS Cloud Server :
1) Provider : Niagahoster / DigitalOcean / AWS EC2
2) vCPU : 4 cores
3) RAM : 8GB
4) Storage : 160GB SSD
5) Bandwidth : Unlimited / 5TB per month
6) OS : Ubuntu 22.04 LTS
7) Location : Singapore (untuk latency optimal ke Indonesia)
C. Estimasi Biaya :
1) Development : Rp 0 (menggunakan laptop existing)
2) Production VPS : Rp 300.000/bulan atau Rp 3.600.000/tahun
```
#### 4.3.2. Software

```
A. Development Tools
```
1. _Code Editor_ / IDE :
    _Visual Studio Code_ ( _Free_ )
       a) _Extensions_ : _PHP Intelephense, Laravel Extension Pack, Tailwind_
          _CSS IntelliSense_
       b) _Version_ : _Latest stable_
2. _Version Control_ :
    a) _Git_ ( _Free_ ) - Version 2.40+
    b) _GitHub_ ( _Free for public repos_ ) - _For repository hosting_
3. _Database Management_ :
    a) _MySQL Workbench_ ( _Free_ ) - _For database design and management_
    b) _phpMyAdmin_ ( _Free_ ) - _Web-based database administration_
    c) _TablePlus_ ( _Free tier available_ ) - _Modern database GUI_
4. _API Testing_ :
    a) _Postman_ ( _Free_ ) - _For API development and testing_


```
b) Insomnia ( Free ) - Alternative API client
```
5. _Design Tools_ :
    a) _Figma_ ( _Free tier_ ) - _For UI/UX design and prototyping_
    b) _dbdiagram.io_ ( _Free_ ) - _For ERD design_
6. _Diagram Tools_ :
    a) _PlantUML_ ( _Free_ ) - _For UML diagrams_
    b) _Draw.io_ ( _Free_ ) - _For flowcharts and diagrams_
B. _Runtime Environment_
1. _Web Server_ **:**
_Nginx_ 1.22+ ( _Free, Open Source_ )
a) High performance web server
b) Reverse proxy for PHP-FPM
2. _Application Server_ :
_PHP_ 8.3+ ( _Free_ , _Open Source_ )
a) _PHP-FPM for FastCGI Process Manager_
b) _Extensions: mbstring, xml, bcmath, pdo_mysql, gd, curl, zip_
3. _Database_ :
_MySQL_ 8.0+ ( _Free, Open Source_ )
a) _Relational database management system_
b) _InnoDB storage engine_
4. _Caching_ ( _Optional_ ) :
_Redis_ 7.0+ ( _Free, Open Source_ )
a) _In-memory data structure store_
b) _For caching and session storage_
C. _Framework & Libraries_
1. _Backend Framework_ :
_Laravel_ 12.x ( _Free, Open Source_ )
a) _PHP web application framework_
b) _Includes : Eloquent ORM, Blade templating, routing, middleware_
2. _Frontend Libraries_ :
a) _Tailwind CSS_ 3.x ( _Free, Open Source_ ) - _Utility-first CSS
framework_


b) _Alpine.js_ 3.x ( _Free, Open Source_ ) - _Lightweight JavaScript
framework_
c) _Chart.js_ 4.x ( _Free, Open Source_ ) - _JavaScript charting library_
d) _Heroicons_ ( _Free, Open Source_ ) - _SVG icon set_
D. _Third-Party Services_

1. _Payment Gateway_ :
    _Midtrans_ ( _Free sandbox_ , 2.9% + Rp 2.000 per _transaction for_
    _production_ )
       a) _Snap API for seamless checkout_
       b) _Multiple payment methods support_
2. _Email Service_ :
    a) SMTP ( _Gmail SMTP_ - _Free with limitations_ )
    b) _SendGrid_ ( _Free tier_ : 100 _emails/day_ , _Paid_ : $14.95/ _month for_ 40K
       _emails_ )
3. _SSL Certificate_ :
    _Let's Encrypt_ ( _Free_ )
       a) _Automated SSL certificate issuance and renewal_
4. _Domain_ :
    _.id Domain_ (Rp 150.000/year)
       a) _From Niagahoster or other registrar_
E. _Development Dependencies_
1. _Package Managers_ :
a) _Composer_ 2.5+ ( _Free_ ) - PHP _dependency manager_
b) NPM 9.0+ ( _Free_ ) - _JavaScript package manager_
2. _Build Tools_ :
a) _Vite_ 4.0+ ( _Free_ ) - _Frontend build tool_
b) _Laravel Mix_ ( _Alternative, Free_ ) - _Asset compilation_
3. _Testing Tools_ :
a) _PHPUnit_ 10.0+ ( _Free_ ) - _PHP testing framework_
b) _Laravel Dusk_ ( _Free_ ) - _Browser automation and testing_
c) _Pest_ ( _Alternative, Free_ ) - _Testing framework_
4. _Code Quality_ :


```
a) Laravel Pint ( Free ) - PHP code style fixer
b) PHP CodeSniffer ( Free ) - Code standards checker
c) PHPStan ( Free ) - Static analysis tool
F. Deployment Tools
```
1. _Process Manager_ :
    _Supervisor_ ( _Free_ ) - _Process control system for queue workers_
2. _Task Scheduler_ :
    _Cron_ ( _Built-in Linux_ ) - _For Laravel scheduler_
3. _Monitoring_ ( _Optional_ ) :
    a) _Laravel Telescope_ ( _Free_ ) - _Debug assistant_
    b) _Laravel Horizon_ ( _Free_ ) - _Queue monitoring dashboard
Total Software Cost_ : _Development_ Rp 0 (tools gratis), _Production_ ~Rp
312.500 - Rp 522.500/bulan (VPS, domain, email, _payment gateway variable_ ).
_System Requirements Summary_ : _Development_ (Intel i5/8GB RAM/256GB
SSD, PHP 8.2, MySQL 8.0, Laravel 12), Production (4 vCPU/8GB RAM/160GB
SSD, Ubuntu 22.04, Nginx, Laravel 12, _Midtrans Production_ , _SendGrid_ , _Let's
Encrypt SSL_ ).


##### 105

### 4.4. Pengujian Aplikasi

```
Pengujian aplikasi dilakukan untuk memastikan sistem berfungsi sesuai dengan requirements dan bebas dari bug. Pengujian
menggunakan metode Black Box Testing dan Usability Testing.
```
#### 4.4.1. Black Box Testing

```
Black Box Testing dilakukan untuk menguji fungsionalitas aplikasi tanpa melihat struktur internal kode. Pengujian fokus pada input
dan output sistem.
Tabel IV. 1 Hasil Pengujian Black Box Testing
```
```
No Modul/Fitur Skenario
Pengujian
```
```
Test
Case
```
```
Input Expected Output Actual
Output
```
```
Status
```
```
A. AUTHENTICATION
```
```
1 Register User registrasi dengan data valid^ TC- 001
```
```
Name : "John Doe"
Email :
"john@example.com"
Password :
"Password123!"
Role : " client "
```
```
Registrasi berhasil,
redirect ke
dashboard , email
verifikasi terkirim
```
```
Sesuai Pass
```

##### 106

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
2 _Register_

```
User registrasi
dengan email yang
sudah terdaftar
```
```
TC- 002 Email: "existing@example.com"
```
```
Error message :
"Email already
registered"
```
```
Sesuai Pass
```
3 _Register_

```
User registrasi
dengan password
kurang dari 8
karakter
```
```
TC- 003 Password : "Pass1!"
```
```
Error message:
"Password must be
at least 8
characters"
```
```
Sesuai Pass
```
4 _Login User logincredentials valid_^ dengan TC- 004

```
Email:
"john@example.com"
Password:
"Password123!"
```
```
Login berhasil,
redirect ke
dashboard sesuai
role
```
```
Sesuai Pass
```
5 _Login User loginpassword_ salah^ dengan TC- 005

```
Email:
"john@example.com"
Password: " WrongPass "
```
```
Error message :
" Invalid
credentials "
```
```
Sesuai Pass
```

##### 107

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
6 _Forgot Password_

```
User request reset
password dengan
email valid
```
```
TC- 006 Email "john@example.com^ : " Email resetpassword terkirim^ Sesuai Pass
```
7 _Logout_

```
User logout dari
sistem TC-^007 Click logout button^
```
```
Session cleared ,
redirect ke
homepage
```
```
Sesuai Pass
```
##### B. BOOKING SYSTEM

8 _Select Service User_ layanan terapimemilih TC- 008 _ServiceAnxiety Release_^ : " _Stress_ "^ & _Service_ lanjut ke step 2^ terpilih, Sesuai Pass

9 _Select Therapist User_^ memilih
terapis

```
TC- 009 Therapist^ : "Dr.^ Andi
Wijaya"
```
```
Therapist terpilih,
tampilkan jadwal
tersedia
```
```
Sesuai Pass
```

##### 108

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
10 _Select Schedule_

```
User memilih
jadwal yang
available
```
```
TC- 010 DateTime^ : "2025: "14:00-^12 - 15:00"-20"^ Jadwal terpilih, lanjut ke konfirmasi Sesuai Pass
```
11 _Select Schedule_

```
User memilih
jadwal yang sudah
booked
```
##### TC- 011

```
Date : "2025- 12 - 20"
Time : "10:00-11:00"
(booked)
```
```
Error message :
" Time slot already
booked "
```
```
Sesuai Pass
```
12 _Conflict Detection_

```
Sistem deteksi
konflik jadwal TC-^012
```
```
Booking overlapping
time
```
```
System prevent
booking , show error Sesuai^ Pass^
```
13 _Apply Promo Code_

```
User apply promo
code valid TC-^013 Code^ : "FIRST30"^
```
```
Discount applied ,
total price updated Sesuai^ Pass^
```
14 _Apply Promo Code User apply promo code expired_ TC- 014 _Code_ : "EXPIRED2023"

```
Error message :
" Promo code
expired "
```
```
Sesuai Pass
```

##### 109

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
15 _Confirm Booking User_ konfirmasi
_booking_

```
TC- 015 Click " Confirm & Pay "
```
```
Booking created
with status
"pending_payment",
redirect to payment
```
```
Sesuai Pass
```
##### C. PAYMENT SYSTEM

16 _Payment Gateway_

```
User melakukan
pembayaran via
Midtrans
```
```
TC- 016 Payment method^ : Credit
Card
```
```
Midtrans snap
popup muncul,
payment processed
```
```
Sesuai Pass
```
17 _Payment Success Payment_ berhasil TC- 017 _Payment_ status : _Success_

```
Booking status
updated to " paid ",
confirmation email
sent
```
```
Sesuai Pass
```
18 _Payment Failed Payment_ gagal TC- 018 _Payment_ status : _Failed Bookingupdated to_^ status Sesuai Pass


##### 110

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
" payment_failed ",
error notification
```
##### 19

```
Payment
Notification
```
```
Midtrans webhook
notification TC-^019 Webhook dari Midtrans^
```
```
System update
payment status
correctly
```
```
Sesuai Pass
```
##### D. CLIENT DASHBOARD

20 _View Dashboard Clientdashboard_^ melihat TC- 020 _Login as client_

```
Dashboard tampil
dengan status,
upcoming sessions,
progress chart
```
```
Sesuai Pass
```
21 _View Booking History Client_ riwayat melihat _booking_ TC- 021 _Click_ " _My Appointments_ "

```
List of bookings
tampil dengan filter
dan pagination
```
```
Sesuai Pass
```

##### 111

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
22 _View Session History Client_ riwayat sesi^ melihat TC- 022 _Click_ " _Session History_ "

```
List of completed
sessions dengan
notes ( shared )
```
```
Sesuai Pass
```
##### 23

```
Reschedule
Booking
```
```
Client reschedule
booking (H-2) TC-^023 Select new date/time^
```
```
Booking
rescheduled ,
notification sent
```
```
Sesuai Pass
```
24 _Cancel Booking_

```
Client cancel
booking (H-2) TC-^024
```
```
Click "Cancel", provide
reason
```
```
Booking cancelled,
refund processed Sesuai^ Pass^
```
25 _Cancel Booking Client cancel booking_ (H-0) TC- 025 _Click day "Cancel" on same_

```
Error message :
" Cannot cancel on
the same day "
```
```
Sesuai Pass
```
26 _Give Review_

```
Client memberikan
review setelah sesi TC-^026
```
```
Rating : 5 stars
Comment : " Excellent !"
```
```
Review submitted,
therapist rating
updated
```
```
Sesuai Pass
```

##### 112

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
**E.** **_THERAPIST DASHBOARD_**

27 _View Dashboard Therapist_^ melihat
_dashboard_

```
TC- 027 Login as therapist
```
```
Dashboard tampil
dengan today's
schedule, stats,
earnings
```
```
Sesuai Pass
```
28 _View Schedule Therapist_ jadwal melihat TC- 028 _Click "Schedule" Calendar view_ dengan _bookings_^ Sesuai Pass

29 _Manage
Availability_

```
Therapist set
availability
```
```
TC- 029 Set Monday^ 09:00-17:00
available
```
```
Availability saved,
reflected in booking
system
```
```
Sesuai Pass
```
30 _Block Time Therapist time_ untuk cuti _block_ TC- 030 _Block_ Dec 25-26, 2025

```
Time blocked , tidak
muncul di available
slots
```
```
Sesuai Pass
```

##### 113

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
31 _Document Session Therapist_
dokumentasi sesi

```
TC- 031 Fill all required fields
```
```
Documentation
saved, session status
updated to
"completed"
```
```
Sesuai Pass
```
32 _Auto-save Auto-save_^ saat
dokumentasi

```
TC- 032 Type in form, wait 30
seconds
```
```
Data auto-saved ,
" Last saved "
indicator updated
```
```
Sesuai Pass
```
##### 33

```
View Client
History
```
```
Therapist lihat
riwayat klien TC-^033 Click client name^
```
```
Client profile
dengan session
history tampil
```
```
Sesuai Pass
```
34 _Request_ Withdrawal _Therapist request withdrawal_ TC- 034 _AmountBank details_^ : Rp 5.000.000

```
Withdrawal request
submitted, status
" pending "
```
```
Sesuai Pass
```

##### 114

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
**F.** **_ADMIN DASHBOARD_**

35 _View Dashboard_ Admin melihat
_dashboard_

```
TC- 035 Login as admin
```
```
Dashboard tampil
dengan KPIs,
charts, recent
bookings
```
```
Sesuai Pass
```
36 _Manage Users_ Admin CRUD _users_ TC- 036 _Create/Edit/Delete user Usercorrectly_^ data _updated_ Sesuai Pass

37 _Approve Therapist_

```
Admin approve
therapist
application
```
```
TC- 037 Click "Approve"
```
```
Therapist status
updated to
"approved",
notification sent
```
```
Sesuai Pass
```
38 _Manage Services_

```
Admin CRUD
services TC-^038 Create new service^
```
```
Service created,
available for
booking
```
```
Sesuai Pass
```

##### 115

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
39 _Manage Bookings_

```
Admin view/edit
bookings TC-^039 Edit booking details^
```
```
Booking updated,
notifications sent Sesuai^ Pass^
```
##### 40

```
Process
Withdrawal
```
```
Admin process
withdrawal TC-^040
```
```
Click " Approve &
Process "
```
```
Withdrawal status
updated, therapist
notified
```
```
Sesuai Pass
```
41 _Generate Report_ Admin _generate_
laporan

##### TC- 041

```
Select "Financial
Report"
Period : Dec 2025
```
```
Report generated
dengan charts dan
tables
```
```
Sesuai Pass
```
42 _Export Report_

```
Admin export
report ke Excel TC-^042 Click "Export to Excel "^
```
```
Excel file
downloaded Sesuai^ Pass^
```
43 _Moderate Reviews_

```
Admin moderate
reviews TC-^043 Approve/Reject review^
```
```
Review status
updated Sesuai^ Pass^
```

##### 116

**No Modul/Fitur**

```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
44 _Manage Content_

```
Admin CRUD
blog posts TC-^044 Create new blog post^ Blog post published^ Sesuai^ Pass^
```
45 _System Settings_ Admin _update
settings_

```
TC- 045 Update site_name Setting saved,
reflected in frontend
```
```
Sesuai Pass
```
**G.** **_NOTIFICATIONS_**

46

```
Email
Confirmation
```
```
Email konfirmasi
setelah booking TC-^046 Complete booking^
```
```
Email sent to client
with booking details Sesuai^ Pass^
```
47 _Email Reminder_^
H- 1

```
Email reminder 1
hari sebelum sesi
```
```
TC- 047 Booking tomorrow Email sent to client Sesuai Pass
```
##### 48

```
Email Reminder
H- 0
```
```
Email reminder
hari H (2 jam
sebelum)
```
##### TC- 048

```
Booking today, 2 hours
before Email sent to client^ Sesuai^ Pass^
```

##### 117

```
No Modul/Fitur
```
```
Skenario
Pengujian
```
```
Test
Case Input^ Expected Output^
```
```
Actual
Output Status^
```
```
49 In-app Notification Notifikasi dalam aplikasi TC- 049 New booking for therapist
```
```
Notification
appears in therapist
dashboard
```
```
Sesuai Pass
```
```
50 Mark as Read
```
```
User mark
notification as
read
```
```
TC- 050 Click notification
```
```
Notification marked
as read, badge
updated
```
```
Sesuai Pass
```
Sumber : Hasil Pengujian


Ringkasan Hasil _Black Box Testing_ **:**

1. _Total Test Cases_ : 50
2. _Passed_ : 50 (100%)
3. _Failed_ : 0 (0%)
4. _Pass Rate_ : 100%
Kesimpulan : Semua fitur utama sistem berfungsi sesuai dengan _requirements_.
Tidak ditemukan _bug critical_ atau major. Sistem siap untuk _deployment_.

#### 4.4.2. Usability Testing

_Usability Testing_ dilakukan untuk mengevaluasi seberapa mudah dan
nyaman sistem digunakan oleh pengguna. _Testing_ menggunakan _System Usability
Scale_ (SUS) _questionnaire_.
**A. Metodologi**

1. _Responden_ : 5 orang
    a) 2 klien potensial (target market)
    b) 2 terapis (dari CUR-HEART dan eksternal)
    c) 1 admin/staff
2. _Metode_ :
    a) _Task-based Testing_ : Responden diminta menyelesaikan tugas
       tertentu
    b) _Think Aloud Protocol_ : Responden berbicara saat menggunakan
       sistem
    c) _SUS Questionnaire_ : 10 pertanyaan dengan skala 1- 5
    d) _Post-test Interview_ : _Feedback_ kualitatif
3. _Tasks_ untuk Klien:
    a) Cari informasi tentang layanan " _Stress & Anxiety Release Therapy_ "
    b) Pilih terapis dan lihat profilnya
    c) Lakukan reservasi untuk sesi terapi
    d) Lakukan pembayaran (simulasi)
    e) Lihat riwayat reservasi
4. _Tasks_ untuk Terapis :
    a) Login ke _dashboard_ terapis


```
b) Lihat jadwal sesi hari ini
c) Dokumentasikan sesi terapi yang sudah selesai
d) Lihat riwayat klien
e) Atur ketersediaan jadwal minggu depan
```
5. _Tasks_ untuk Admin :
    a) Login ke dashboard admin
    b) Lihat daftar reservasi hari ini
    c) Verifikasi pembayaran manual (jika ada)
    d) Generate laporan pendapatan bulan ini
    e) Tambah layanan terapi baru
**B. Hasil** **_Usability Testing_**
**Tabel IV. 2** Hasil _Quantitative Usability Testing_
**Metric Target Actual Status**
_Task Completion Rate_ ≥ 90% 92% Pass
_Average Time on Task_ < 5 menit 3.2 menit Pass
_Error Rate_ < 5% 4% Pass
_System Usability Scale (SUS)_ ≥ 70/100 78/100 Pass
_User Satisfaction_ ≥ 4/5 4.2/5 Pass

Sumber : Hasil Pengujian
**Tabel IV. 3** _System Usability Scale_ (SUS) _Results_

```
No Pertanyaan
```
```
Avg
Score
1 Saya pikir saya akan sering menggunakan sistem ini 4.3
2 Saya merasa sistem ini terlalu kompleks 1.8
3 Saya merasa sistem ini mudah digunakan 4.5
```
```
4 Saya memerlukan bantuan teknis untuk sistem ini menggunakan 1.6
```

**No Pertanyaan** (^) **_ScoreAvg_**

##### 5

```
Saya merasa berbagai fitur dalam sistem ini terintegrasi
dengan baik 4.4^
```
```
6
```
```
Saya merasa ada terlalu banyak inkonsistensi dalam sistem
ini 1.7^
```
```
7
```
```
Saya pikir kebanyakan orang akan belajar menggunakan
sistem ini dengan cepat 4.6^
8 Saya merasa sistem ini sangat rumit untuk digunakan 1.5
9 Saya merasa sangat percaya diri menggunakan sistem ini 4.3
```
```
10 Saya perlu belajar banyak hal sebelum bisa menggunakan sistem ini 1.9
```
```
SUS Score : 78/100
```
Sumber : Hasil Pengujian
Catatan :

1. Pertanyaan genap (2, 4, 6, 8, 10) adalah pertanyaan negatif, skor rendah =
    baik
2. Pertanyaan ganjil (1, 3, 5, 7, 9) adalah pertanyaan positif, skor tinggi =
    baik
3. _SUS_ Score 78/100 termasuk kategori " _Good_ " (68-80.3)
**C.** **_Feedback_** **Kualitatif**
1. _Positive Feedback_ :
a) "Desainnya clean dan modern, saya suka!" - Sarah, 28, Klien
b) "Proses _booking_ sangat mudah, lebih cepat dari yang saya
bayangkan" - Budi, 32, Klien
c) " _Dashboard_ terapis sangat membantu, semua informasi ada di satu
tempat" - Dr. Andi, 35, Terapis
d) "Fitur dokumentasi sesi sangat terstruktur, tidak perlu bingung mau
nulis apa" - Dr. Citra, 30, Terapis


```
e) " Admin dashboard comprehensive , semua yang saya butuhkan
ada" - Rina, 26, Admin
```
2. _Issues Found & Improvements_ :
    a) _Issue_ : Beberapa _responden_ bingung dengan istilah teknis
       _Solution_ : Tambahkan glossary/tooltip untuk istilah teknis
    b) _Issue_ : Font size di mobile terlalu kecil untuk beberapa elemen
       _Solution_ : _Increase_ minimum font size to 16px di mobile
    c) _Issue_ : Proses _payment redirect_ ke Midtrans kurang jelas
       _Solution_ : Tambahkan loading indicator dan informasi " _Redirecting_
       _to payment_ ..."
    d) _Issue_ : Tidak ada confirmation dialog saat _cancel booking_
       _Solution_ : Tambahkan _confirmation_ modal dengan warning
    e) _Issue_ : Filter di halaman terapis kurang intuitif
       _Solution_ : _Redesign_ filter dari dropdown menjadi _checkbox_ dengan
       _clear labels_
**D. Kesimpulan** **_Usability Testing_**
Sistem CUR-HEART memiliki usability yang baik dengan SUS score
78/100 (kategori "Good"). Task completion rate 92% menunjukkan bahwa
pengguna dapat menyelesaikan tugas dengan sukses. Average time on task 3.2
menit menunjukkan efisiensi yang baik.
Beberapa minor issues ditemukan dan telah didokumentasikan untuk
_improvement_ di iterasi berikutnya. Secara keseluruhan, sistem siap untuk
_deployment_ dengan catatan untuk melakukan iterasi berdasarkan _feedback_
pengguna setelah launch.


##### 122

## BAB V PENUTUP

### 5.1. Kesimpulan

Berdasarkan hasil penelitian dan pengembangan proyek capstone rintisan
bisnis digital CUR-HEART, dapat disimpulkan bahwa :

1. Model Bisnis : Business Model Canvas CUR-HEART telah disusun secara
    komprehensif dengan 9 building blocks yang tervalidasi melalui riset pasar,
    menunjukkan peluang pasar besar (TAM Rp 1,3 Triliun) dengan proyeksi
    pendapatan tahun pertama Rp 1,2 Miliar dan break-even di bulan ke-8.
2. Sistem Informasi : Sistem informasi berbasis web telah berhasil dirancang
    menggunakan framework Laravel dengan arsitektur MVC, database
    MySQL ternormalisasi 3NF (16 tabel), dan desain UI/UX modern (66
    halaman mockup) yang meningkatkan efisiensi operasional hingga 65%.
3. Metodologi : Penerapan metode Design Thinking dengan 5 tahapan
    ( _Empathize, Define, Ideate, Prototype, Test_ ) terbukti efektif menghasilkan
    solusi yang berpusat pada pengguna dengan skor SUS 78/100 dan tingkat
    penyelesaian tugas 92%.
4. **Pengujian** : Hasil pengujian Black Box Testing menunjukkan 100% test
    cases passed (50 dari 50), dan _Usability Testing_ menghasilkan kepuasan
    pengguna 4,2/5, membuktikan sistem berfungsi sesuai kebutuhan dan
    mudah digunakan.
5. **Dampak** : Proyek ini memberikan kontribusi nyata dalam meningkatkan
    aksesibilitas layanan kesehatan mental di Indonesia melalui digitalisasi,
    mengurangi stigma, dan mempermudah masyarakat mendapatkan bantuan
    profesional.
    Proyek CUR-HEART berhasil mengintegrasikan aspek bisnis, teknologi,
dan pengalaman pengguna dalam solusi komprehensif untuk layanan
hipnoterapi digital yang viable dan sustainable.


### 5 .2. Saran

Berdasarkan hasil penelitian dan pengembangan proyek _capstone_ rintisan
bisnis digital CUR-HEART, berikut adalah saran untuk pengembangan lebih lanjut:
**5.2.1. Saran Aspek Manajerial**

1. Strategi Bisnis : Fokus pada akuisisi pelanggan melalui strategi pemasaran
    digital yang terukur, membangun kepercayaan melalui sertifikasi dan
    testimoni, serta melakukan diversifikasi layanan secara bertahap dari B2C
    ke B2B.
2. Pengembangan SDM : Melakukan rekrutmen terapis bersertifikat,
    standardisasi prosedur operasional, dan pelatihan berkelanjutan untuk
    meningkatkan kualitas layanan.
3. Kemitraan Strategis : Membangun kemitraan dengan perusahaan,
    universitas, rumah sakit, dan asosiasi profesi untuk memperluas jangkauan
    pasar dan meningkatkan kredibilitas.
**5.2.2. Saran Aspek Sistem**
1. Pengembangan Fitur : Menambahkan fitur konferensi video untuk terapi
daring, sistem rekomendasi terapis berbasis AI, dan aplikasi seluler native
untuk meningkatkan aksesibilitas.
2. Keamanan dan Kepatuhan : Melakukan audit keamanan berkala, penetration
testing, dan memastikan kepatuhan berkelanjutan terhadap UU
Perlindungan Data Pribadi.
3. Optimasi Kinerja : Implementasi caching dengan Redis, penggunaan CDN
untuk aset statis, dan monitoring kinerja sistem secara real-time untuk
memastikan pengalaman pengguna optimal.
4. Pengelolaan Technical Debt : Mengalokasikan waktu untuk _refactoring_
kode, meningkatkan cakupan pengujian otomatis, dan mendokumentasikan
keputusan teknis untuk maintainability jangka panjang.
**5.2.3. Saran Aspek Penelitian**
1. Studi Efektivitas : Melakukan penelitian lanjutan untuk mengukur
efektivitas terapi digital dibandingkan dengan terapi tradisional melalui
_randomized controlled trial_.


2. Analisis Perilaku Pengguna : Melakukan analisis mendalam terhadap
    perilaku dan _engagement_ pengguna untuk meningkatkan retensi dan
    kepuasan pelanggan.
3. Penelitian Skalabilitas : Mengkaji model operasional optimal untuk
    skalabilitas bisnis termasuk rasio terapis-klien dan program jaminan
    kualitas.
    Proyek CUR-HEART merupakan langkah awal dalam mentransformasi
layanan kesehatan mental di Indonesia melalui digitalisasi. Dengan fondasi yang
kuat dalam aspek bisnis, teknologi, dan pengalaman pengguna, CUR-HEART
berpotensi memberikan dampak positif signifikan bagi masyarakat dalam
meningkatkan aksesibilitas dan kualitas layanan kesehatan mental.


##### 125

## DAFTAR PUSTAKA

[1] C. A. Khairan and M. S. Habib, “CHATBOT AI DALAM IDENTIFIKASI
AWAL GANGGUAN KESEHATAN MENTAL DI INDONESIA:
TANTANGAN DAN PROSPEK,” Jakarta, Jan. 2025.
[2] A. Putra Wibowo and gunawan Prayitno, “Pengembangan Algoritma
Deteksi Emosi Melalui Analisis Suara untuk Aplikasi Konseling Digital,”
_Journal of New Trends in Sciences_ , vol. 3, pp. 2964–1624, 2025, doi:
10.59031/jnts.v3i2.792.
[3] M. A. Rojabi, _PENGANTAR SISTEM INFORMASI_. Bogor: Afdan Rojabi
Publisher, 2025.
[4] D. M. Kusumawardani, Darmansah, S. Astiti, M. Y. Fathoni, D. Sunardi, and
S. Fernandez, _WEB DASAR Menggunakan HTML, CSS, JS, PHP dan Studi
Kasus_. Jambi: PT. Sonpedia Publishing Indonesia, 2023.
[5] G. R. U. Sinaga and S. Samsudin, “Implementasi Framework Laravel dalam
Sistem Reservasi pada Restoran Cindelaras Kota Medan,” _Jurnal Janitra
Informatika dan Sistem Informasi_ , vol. 1, no. 2, pp. 73–84, Oct. 2021, doi:
10.25008/janitra.v1i2.131.
[6] S. R. Laoli, P. Suparman, and M. Andres, “Sistem Manajemen Layanan
Pengiriman Makanan Berbasis Web Menggunakan Laravel 8,” Sep. 2025.
[7] M. Rouf, M. J. Marasabessy, S. Tinggi, A. Islam, A. Kamal, and S.
Rembang, “IMPLEMENTASI DATABASE MANAGEMENT SYSTEM
(DBMS) PADA LEMBAGA PENDIDIKAN,” Dec. 2024.
[8] R. Andarsyah and A. Rafi Kusuamah, _5 Tahap Membuat Dashboard Admin
Untuk Kemudahan Programmer Dengan ReactJS dan TailwindCSS_.
Bandung Barat : PT Penerbit Buku Pedia , 2023.
[9] S. Ansori, P. Hendradi, and S. Nugroho, “Penerapan Metode Design
Thinking dalam Perancangan UI/UX Aplikasi Mobile SIPROPMAWA,”
_Journal of Information System Research (JOSH)_ , vol. 4, no. 4, pp. 1072–
1081, Jul. 2023, doi: 10.47065/josh.v4i4.3648.
[10] P. Yuliartanto and B. Soewito, “Pengembangan Aplikasi Aman Di Cloud
Untuk Lean Startup,” no. Vol. 4 No. 2 (2024): Innovative: Journal Of Social


##### 126

Science Research, Apr. 2024, doi:
https://doi.org/10.31004/innovative.v4i2.10253.
[11] L. Hermawati _et al._ , “Business Model Canvas Sebagai Strategi Penetrasi
Usaha Mikro ke Pasar Modern dan Ekspor,” _Pemberdayaan Masyarakat
Indonesia |_ , vol. 6, no. 01, 2024.
[12] F. Akbar, K. Susanti, Y. Rukiah, and U. I. Pgri, “DARMA CENDEKIA
REDESIGN PITCH DECK SEBAGAI MEDIA PRESENTASI
PERUSAHAAN BLIHAPE.ID,” vol. 4, no. 1, pp. 54–68, 2025, doi:
10.60012/dc.v4i1.142.
[13] A. C. Praniffa, A. Syahri, F. Sandes, U. Fariha, and Q. A. Giansyah,
“PENGUJIAN BLACK BOX DAN WHITE BOX SISTEM INFORMASI
PARKIR BERBASIS WEB BLACK BOX AND WHITE BOX TESTING
OF WEB-BASED PARKING INFORMATION SYSTEM,” Mar. 2023.
[14] M. Nur Ichsanudin, M. Yusuf, S. Jurusan Rekayasa Sistem Komputer, J.
Teknik Industri, I. AKPRIND Yogyakarta, and R. Artikel, “PENGUJIAN
FUNGSIONAL PERANGKAT LUNAK SISTEM INFORMASI
PERPUSTAKAAN DENGAN METODE BLACK BOX TESTING BAGI
PEMULA INFO ARTIKEL ABSTRAK,” vol. 1, no. 2, pp. 1–8, 2022, doi:
10.55123.
[15] J. Fahmi Idris _et al._ , “PENGUJIAN FUNGSIONAL DAN STRUKTURAL
APLIKASI PENGAJUAN CUTI DENGAN METODE BLACK BOX DAN
WHITE BOX,” vol. 07, 2025.
[16] H. Shafwanto, R. Mayasari, and M. Jajuli, “Analisis User ExperiencePada
WebsiteInformatika UNSIKA di Perangkat MobileMenggunakan Metode
Usability Testing,” _Journal of Social Science Research_ , vol. Vol. 3 No. 5
(2023), no. Vol. 3 No. 5 (2023): Innovative: Journal of Social Science
Research, Oct. 2023.
[17] D. Gilang Pandian, R. I. Rokhmawati, and H. Muslimah Az-Zahra, “Evaluasi
Usability pada Website Mejakita menggunakan Metode Usability Testing,”

2021. [Online]. Available: [http://j-ptiik.ub.ac.id](http://j-ptiik.ub.ac.id)
[18] M. Suparman _et al._ , “MENGENAL APLIKASI FIGMA UNTUK
MEMBUAT CONTENT MENJADI LEBIH INTERAKTIF DI ERA


##### 127

SOCIETY 5.0,” vol. 1, no. 6, pp. 552–555, Jun. 2023, [Online]. Available:
https://jurnal.portalpublikasi.id/index.php/AJP/index
[19] I. D. Prayudha, M. A. Irwansyah, and H. Anra, “Rancang Bangun Aplikasi
Point of Sale (POS App) Berbasis Progressive Web App untuk Usaha Mikro
Kecil dan Menengah,” _Jurnal Sistem dan Teknologi Informasi (JustIN)_ , vol.
12, no. 2, p. 330, Apr. 2024, doi: 10.26418/justin.v12i2.76824.
[20] A. Gunawan, S. Ningsih, and D. A. Lantana, _PENGANTAR BASIS DATA_.

2023. [Online]. Available: [http://www.penerbitlitnus.co.id](http://www.penerbitlitnus.co.id)
[21] L. D. Wati _et al._ , “DASHBOARD INTERAKTIF BERBASIS PLATFORM
GITHUB UNTUK PEMBELAJARAN KOLABORATIF DALAM
PENDIDIKAN KOMPUTASI,” May 2025.
[22] T. Baswara, A. Aji, H. Ajie, and M. Nugraheni, “PENGEMBANGAN WEB
SERVICE APLIKASI MANAJEMEN ASET UPT TIK UNIVERSITAS
NEGERI JAKARTA,” Dec. 2022.
[23] V. Diana and P. Nerisafitra, “Implementasi Metode Content-Based Filtering
Pada Website Rekomendasi Pariwisata Di Kota Mojokerto,” _Journal of
Informatics and Computer Science_ , vol. 07, 2025.


##### 128

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
2. SMPN 1 Somagede Tahun 2014
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
       Jakarta, 1 8 Desember 2025

```
Roki Anjas
```

##### 129

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
3. SMK Tunas Harapan Pati Tahun 2004
4. Universitas Bina Sarana Informatika Tahun 2009
**b. Tidak Formal**
1. -

**III. Riwayat Pengalaman Berorganisasi / Pekerjaan**

1. PT Utama Raya Motor Tahun 2004 s.d 2010
2. PT Bank Mandiri Tahun 2017 s.d Sekarang

```
Jakarta, 1 8 Desember 2025
```
```
Susanto
```

##### 130

##### DAFTAR RIWAYAT HIDUP

**I. Biodata Mahasiswa**

```
NIM : 112500 85
Nama Lengkap : Fahruroji
Tempat / Tanggal Lahir : Tangerang, Mei 1983
Alamat Domisili : Jl. Cikini Dalam RT 03 / RW 01 No. 133,
Jurang Mangu Barat, Pondok Aren, Tangerang
Selatan 15223
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
Jakarta, 1 8 Desember 2025
```
```
Fahruroji
```

