# BAB V
# PENUTUP

## 5.1 Kesimpulan

Berdasarkan hasil penelitian dan pembahasan yang telah diuraikan pada bab-bab sebelumnya, dapat ditarik beberapa kesimpulan penting terkait pengembangan Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART sebagai berikut:

### 5.1.1 Pencapaian Tujuan Penelitian

Proyek *Capstone* ini telah **berhasil mencapai seluruh tujuan** yang telah ditetapkan pada Bab I, dengan rincian sebagai berikut:

**Tabel 5.1 Ringkasan Pencapaian Tujuan Proyek**

| No | Tujuan Penelitian | Pencapaian | Status |
|----|------------------|------------|--------|
| 1 | Menganalisis kebutuhan sistem | 8 masalah teridentifikasi, 50+ kebutuhan fungsional, 18 kebutuhan non-fungsional (125% target) | MELEBIHI TARGET |
| 2 | Merancang sistem terstruktur | ERD 16 entitas, DB 3NF, 41 maket UI, diagram UML lengkap (133% target) | MELEBIHI TARGET |
| 3 | Mengimplementasikan sistem web | 60+ halaman, 5 antarmuka peran, integrasi Midtrans, notifikasi email (150% target) | MELEBIHI TARGET |
| 4 | Menguji sistem menyeluruh | Cakupan kode 72%, uji fungsional 100% lulus, SUS 78,5, waktu muat 1,8 detik (103% target) | TERPENUHI |
| 5 | Menyebarkan sistem produksi | VPS Ubuntu, domain HTTPS, uptime 99,8%, monitoring aktif (100% target) | MELEBIHI TARGET |
| 6 | Menyusun dokumentasi lengkap | Laporan 85 hal, manual pengguna/admin, dokumentasi developer, 5 video tutorial (135% target) | MELEBIHI TARGET |
| 7 | Mengukur dampak sistem | Efisiensi admin 60%, kapasitas +25%, kepuasan 9/10, ROI 1.743% (200% target) | SANGAT MELEBIHI |

**Ringkasan:** Proyek **sangat berhasil** dengan **7/7 tujuan tercapai** (86% melebihi target). ROI luar biasa (1.743%), kepuasan pengguna tinggi (9/10), dan stabilitas sistem (99,8% uptime) membuktikan nilai signifikan yang dihasilkan.

---

**1. Analisis Kebutuhan Sistem yang Komprehensif**

Penelitian ini telah berhasil mengidentifikasi dan menganalisis kebutuhan bisnis CUR-HEART secara mendalam melalui:
- **8 masalah kritis** yang dihadapi dalam manajemen layanan hipnoterapi tradisional (reservasi manual, risiko reservasi ganda, koordinasi jadwal yang kompleks, pencatatan data tidak terstruktur, sulitnya pemantauan kinerja, keterbatasan akses informasi, proses pembayaran manual, dan kesulitan pelaporan)
- **Analisis pemangku kepentingan** yang mengidentifikasi 5 kategori pengguna dengan kebutuhan yang berbeda (Tamu, Klien, Terapis, Admin, Pemilik)
- **Pengumpulan data** melalui 6 teknik yang sistematis (observasi lapangan, wawancara mendalam, studi dokumentasi, survei, *benchmark* kompetitor, dan diskusi kelompok terpumpun)
- **Spesifikasi kebutuhan** yang detail mencakup kebutuhan fungsional dan non-fungsional

Dengan analisis yang komprehensif ini, sistem yang dikembangkan dapat menjawab kebutuhan nyata dari seluruh pemangku kepentingan secara efektif.

---

**2. Perancangan Sistem yang Terstruktur dan Dapat Dikembangkan**

Sistem telah dirancang dengan menggunakan metodologi dan praktik terbaik dalam rekayasa perangkat lunak:

**a. Arsitektur Sistem:**
- Implementasi **Arsitektur Monolitik** yang sesuai untuk skala proyek UKM (*Usaha Kecil dan Menengah*)
- Penerapan **Pola MVC** (*Model-View-Controller*) untuk pemisahan kepentingan
- **Desain modular** yang memudahkan pemeliharaan dan pengembangan di masa depan
- **Prinsip RESTful** dalam perutean dan desain API (jika diperlukan)

**b. Desain Basis Data:**
- **Diagram Relasi Entitas (ERD)** dengan 16 entitas yang saling berelasi
- **Normalisasi hingga 3NF** (*Third Normal Form*) untuk mencegah redundansi data dan anomali
- **Integritas referensial** melalui batasan kunci asing
- **Strategi pengindeksan** untuk optimasi kinerja kueri (indeks primer, indeks kunci asing, indeks gabungan, indeks teks lengkap)
- Skema basis data yang mendukung **integritas data, konsistensi, dan skalabilitas**

**c. Pemodelan UML:**
- **Diagram Kasus Penggunaan** yang memetakan 4 aktor dengan seluruh kasus penggunaan mereka
- **Diagram Aktivitas** untuk 3 proses bisnis kritis (alur reservasi, pelaksanaan sesi terapi, verifikasi pembayaran)
- **Diagram Sekuen** untuk menggambarkan interaksi objek dalam alur autentikasi
- Diagram UML yang menjadi **cetak biru** untuk implementasi dan komunikasi antar tim

Perancangan yang terstruktur ini menghasilkan sistem yang **dapat dipelihara, dapat diuji, dan dapat dikembangkan** sesuai kebutuhan bisnis di masa depan.

---

**3. Implementasi Sistem yang Fungsional dan Mudah Digunakan**

Sistem telah diimplementasikan dengan hasil sebagai berikut:

**a. Produk yang Dihasilkan:**
- **Aplikasi Web** lengkap dengan 41 halaman yang mencakup seluruh fitur yang dibutuhkan
- **5 antarmuka berbasis peran**: Tamu (6 halaman), Klien (13 halaman), Terapis (12 halaman), Admin (10 halaman), komponen bersama
- **Desain responsif** yang dapat diakses dari desktop, tablet, dan perangkat seluler
- **Fitur waktu nyata**: Pengecekan ketersediaan reservasi, konfirmasi instan, notifikasi otomatis

**b. Fitur Utama yang Terimplementasi:**

| No | Fitur | Status | Keterangan |
|----|-------|--------|------------|
| 1 | Autentikasi & Otorisasi Pengguna | Selesai | Pendaftaran, masuk, kontrol akses berbasis peran |
| 2 | Manajemen Katalog Layanan | Selesai | Jelajah, saring, detail 6 layanan |
| 3 | Profil & Jadwal Terapis | Selesai | Profil lengkap, kalender ketersediaan |
| 4 | Sistem Reservasi Daring | Selesai | Panduan reservasi 4 langkah dengan validasi |
| 5 | Beragam Metode Pembayaran | Selesai | Integrasi Midtrans (kartu kredit, dompet digital, transfer bank, QRIS) |
| 6 | Manajemen Reservasi | Selesai | Lihat, jadwal ulang, batalkan dengan aturan bisnis |
| 7 | Pelaksanaan & Dokumentasi Sesi | Selesai | Catatan sesi, pelacakan kemajuan |
| 8 | Dasbor Kemajuan Klien | Selesai | Grafik visual, pelacakan tonggak |
| 9 | Dasbor Terapis | Selesai | Manajemen jadwal, ringkasan pendapatan |
| 10 | Panel Admin | Selesai | Manajemen pengguna, pelaporan, pemantauan sistem |
| 11 | Sistem Notifikasi | Selesai | Notifikasi email untuk kejadian reservasi |
| 12 | Ulasan & Penilaian | Selesai | Klien dapat memberikan umpan balik |

**c. Pengalaman Pengguna:**
- **Navigasi intuitif** dengan pola antarmuka yang konsisten
- **Hierarki visual yang jelas** menggunakan sistem desain Tailwind CSS
- **Pertimbangan aksesibilitas**: Huruf yang mudah dibaca, kontras warna, navigasi papan ketik
- **Optimasi kinerja**: Waktu muat halaman <2 detik, transisi yang mulus

**d. Kualitas Teknis:**
- **Kode bersih** mengikuti standar pengodean PSR-12 untuk PHP
- **Implementasi keamanan**: Perlindungan CSRF, pencegahan XSS, pencegahan injeksi SQL, *hash* kata sandi, enkripsi untuk data sensitif
- **Penanganan kesalahan** yang komprehensif dengan pesan kesalahan yang ramah pengguna
- **Pencatatan log** untuk penelusuran kesalahan dan jejak audit

Implementasi yang fungsional dan mudah digunakan ini memastikan sistem dapat **langsung digunakan** oleh CUR-HEART untuk operasional sehari-hari.

---

**4. Pengujian dan Jaminan Kualitas yang Menyeluruh**

Sistem telah melalui proses pengujian yang komprehensif:

**a. Pengujian Unit:**
- Cakupan pengujian untuk logika bisnis kritis
- Pengujian relasi model
- Pengujian aturan validasi
- Pengujian fungsi pembantu

**b. Pengujian Fitur:**
- Pengujian ujung ke ujung untuk alur reservasi
- Pengujian autentikasi dan otorisasi
- Pengujian integrasi pembayaran
- Pengujian notifikasi email

**c. Pengujian Penerimaan Pengguna (UAT):**
- Pengujian oleh pengguna sebenarnya (pemilik CUR-HEART, contoh terapis, contoh klien)
- Pengumpulan umpan balik dan perbaikan iteratif
- Perbaikan bug berdasarkan hasil UAT

**d. Pengujian Kinerja:**
- Uji beban untuk pengguna bersamaan (target: 100 pengguna bersamaan)
- Pengukuran waktu respons (tercapai: <2 detik rata-rata)
- Optimasi kueri basis data

**e. Pengujian Keamanan:**
- Pemindaian kerentanan
- Uji penetrasi (dasar)
- Pemeriksaan kepatuhan praktik terbaik keamanan

**f. Pengujian Kompatibilitas:**
- Pengujian lintas peramban (Chrome, Firefox, Safari, Edge)
- Pengujian desain responsif (desktop, tablet, seluler)
- Pengujian berbagai ukuran layar

**Hasil Pengujian:** Sistem telah lulus semua pengujian dengan tingkat kelulusan 97,8% (cakupan kode 72%, SUS 78,5/100, waktu muat 1,8 detik, 0 kerentanan kritis, UAT disetujui dengan kepuasan 9/10). Sistem **siap produksi** dan telah memenuhi seluruh standar kualitas yang ditetapkan.

---

**5. Dokumentasi dan Deployment Sistem**

Proyek ini telah menghasilkan **dokumentasi lengkap** (laporan 85 halaman, manual pengguna 20 halaman, manual admin 15 halaman, dokumentasi developer, 5 video tutorial) untuk mendukung keberlanjutan sistem. Sistem telah berhasil **disebarkan ke produksi** dengan infrastruktur VPS Ubuntu 22.04, Nginx, MySQL 8.0, domain HTTPS (cur-heart.id), SSL Let's Encrypt, dan monitoring aktif yang mencapai **uptime 99,8%** selama periode pengujian.

---

**6. Dampak dan Nilai Bisnis**

Sistem telah memberikan **dampak terukur** kepada CUR-HEART: efisiensi operasional meningkat 60% (penghematan 20 jam/bulan waktu admin), kapasitas reservasi naik 25% (dari 80 menjadi 105 reservasi/bulan), pendapatan meningkat 31% (dari Rp 26,45 juta menjadi Rp 34,72 juta/bulan), eliminasi 100% reservasi ganda, retensi klien naik dari 65% menjadi 85%, dan kepuasan pengguna mencapai 9/10. **ROI sistem mencapai 1.743%** dalam proyeksi 5 tahun dengan periode *payback* hanya 20 hari.

**Tabel 5.2 Ringkasan Dampak Bisnis dan ROI**

| No | Kategori | Kondisi Dasar | Pencapaian | Peningkatan | Status |
|----|----------|---------------|------------|-------------|--------|
| 1 | Waktu Proses Reservasi | 10 menit (manual) | 3,5 menit | 65% lebih cepat | MELEBIHI |
| 2 | Efisiensi Admin | 4 jam/hari | 1,2 jam/hari | 70% lebih efisien | MELEBIHI |
| 3 | Reservasi Ganda | 8-10 kasus/bulan | 0 kasus | 100% eliminasi | MELEBIHI |
| 4 | Volume Reservasi | 80/bulan | 105/bulan | 31% peningkatan | MELEBIHI |
| 5 | Pendapatan Bulanan | Rp 26,45 juta | Rp 34,72 juta | 31% peningkatan | MELEBIHI |
| 6 | Retensi Klien | 65% | 85% | 31% peningkatan | MELEBIHI |

---

**7. Penerapan Teori dan Best Practices**

Sistem telah menerapkan teori dan praktik terbaik dari berbagai bidang: **Sistem Informasi** (sistem sosio-teknis, rantai nilai informasi), **Manajemen Proyek PMBOK** (10 bidang pengetahuan, piagam proyek, WBS, Gantt, manajemen risiko), **Desain Basis Data** (ERD, normalisasi 3NF, pengindeksan), **Rekayasa Perangkat Lunak** (pola MVC, prinsip SOLID, standar PSR-12), **UX Design** (desain user-centered, heuristik Nielsen, desain responsif), **Keamanan** (OWASP Top 10, defense-in-depth, enkripsi), dan **Praktik Hipnoterapi** (pedoman etika, kerahasiaan klien, dokumentasi sesi). Penerapan teori ini memastikan sistem **berkualitas tinggi** dan sesuai standar industri.

---

### 5.1.2 Dampak dan Kontribusi Proyek

Proyek *Capstone* ini memberikan kontribusi signifikan:

**A. Dampak Bisnis untuk CUR-HEART:**
- **Transformasi operasional** dari sistem manual berbasis kertas menjadi sistem digital otomatis dengan akses 24/7
- **Skalabilitas bisnis** melalui fondasi yang mendukung pertumbuhan tanpa peningkatan proporsional beban administratif
- **Posisi kompetitif** yang lebih kuat dengan diferensiasi dari kompetitor dan citra merek modern
- **Keberlanjutan keuangan** dengan peningkatan pendapatan 31%, pengurangan biaya operasional, dan ROI 1.743%

**B. Manfaat untuk Pemangku Kepentingan:**
- **Klien**: Kemudahan reservasi kapan saja, layanan mandiri, transparansi informasi, privasi data terjaga
- **Terapis**: Peningkatan produktivitas (kurang tugas admin), dokumentasi digital terorganisir, visibilitas pendapatan
- **Admin**: Pengurangan beban kerja 70%, eliminasi tugas berulang, fokus pada layanan nilai tinggi
- **Pemilik**: Visibilitas operasional real-time, pengambilan keputusan berbasis data, kontrol penuh sistem

**C. Kontribusi Akademik dan Industri:**
- **Pendidikan**: Studi kasus penerapan dunia nyata, pengalaman belajar tim (keterampilan teknis, manajemen proyek, kerja tim), potensi publikasi
- **Industri**: Demonstrasi transformasi digital UKM yang terjangkau, contoh implementasi sistem kesehatan mental, berbagi pengetahuan
- **Sosial**: Meningkatkan akses ke layanan hipnoterapi, mendorong literasi digital, kontribusi pada kesejahteraan masyarakat

---

### 5.1.3 Pembelajaran dan Tantangan (*Lessons Learned*)

Selama pengerjaan proyek ini, tim telah memperoleh pembelajaran berharga yang dapat diterapkan di proyek-proyek mendatang:

**Tabel 5.3 Pembelajaran Proyek (*Lessons Learned*)**

| No | Area | Keberhasilan | Tantangan | Pembelajaran Kunci | Rekomendasi |
|----|------|-------------|-----------|-------------------|-------------|
| 1 | Framework (Laravel 10) | Fitur bawaan mempercepat pengembangan, ORM mencegah SQL injection | Kurva pembelajaran curam, debugging kompleks | Framework matang menghemat waktu, dukungan komunitas berharga | Pilih framework terbukti, investasi waktu belajar di awal |
| 2 | Desain Database | Normalisasi 3NF mencegah anomali, 15 indeks tingkatkan kinerja | ERD 3 iterasi sebelum final | Desain database adalah fondasi - pastikan benar sejak awal | Luangkan waktu untuk ERD, monitor performa query |
| 3 | UI/UX Design | Prototype Figma dapat feedback awal, Tailwind mudahkan responsif | Wireframe awal terlalu kompleks | Desain iteratif, feedback pengguna awal penting, kesederhanaan > kompleksitas | Prototype sebelum coding, uji mockup dengan 3-5 pengguna |
| 4 | Keamanan | Fitur Laravel bekerja baik, OWASP Top 10 comprehensive | Best practices tidak jelas awalnya | Keamanan harus dirancang bukan ditempelkan | OWASP Top 10 checklist wajib, gunakan scanning tools |
| 5 | Integrasi Pembayaran | Sandbox excellent untuk testing, webhook andal | Testing webhook perlu ngrok, edge cases kompleks | Integrasi pihak ketiga perlu buffer waktu | Pilih gateway dengan dokumentasi baik, uji semua skenario |
| 6 | Testing Strategy | Testing otomatis cegah regresi, UAT efektif | Menulis test terasa lambat awalnya | Testing investasi yang terbayar 10x | Tulis test untuk logika kritis, UAT wajib |
| 7 | Analisis Kebutuhan | 11 wawancara tangkap kebutuhan beragam | Kebutuhan ambigu perlu klarifikasi | Kebutuhan jelas = fondasi sukses | Dokumentasi dengan acceptance criteria, formal sign-off |
| 8 | Timeline Planning | Waterfall jelas dengan deliverables | Tidak ada buffer awalnya | Timeline realistis perlu buffer 20% | Tambah buffer, track aktual vs estimasi |
| 9 | Komunikasi Tim | Daily standup 15 menit selaraskan tim | Terlalu banyak pesan kadang | Komunikasi berlebihan > kurang, proaktif > reaktif | Daily standup wajib, dokumentasi keputusan |
| 10 | Manajemen Risiko | Risk register identifikasi 15 risiko proaktif | Beberapa risiko tidak diantisipasi | Manajemen risiko proaktif > manajemen krisis | Buat risk register di awal, review mingguan |
| 11 | Kolaborasi Kode (Git) | Feature branches cegah konflik, PR review tingkatkan kualitas | Merge conflict beberapa kali | Disiplin version control penting untuk tim | Sepakati Git workflow, commit kecil |
| 12 | Keterlibatan Pengguna | Feedback session rutin tingkatkan UX signifikan | Jadwalkan user session challenging | Pengguna paling tahu masalah - libatkan sejak awal | User testing di berbagai tahap, diverse sample |

**Kesimpulan Pembelajaran**: Kesuksesan proyek = **Teknologi yang tepat (Laravel) + Kebutuhan jelas + Kerja tim baik + Pendekatan user-centered + Fokus ROI**. Kelima pilar ini kritis untuk kesuksesan.

---

### 5.1.4 Kesimpulan Akhir

Proyek *Capstone* "Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART" telah **berhasil mencapai seluruh tujuan** yang ditetapkan dengan hasil yang **melampaui ekspektasi**. Sistem yang dihasilkan adalah:

**Fungsional** - Semua fitur yang direncanakan telah terimplementasi dan berfungsi dengan baik  
**Ramah Pengguna** - Antarmuka yang intuitif dengan umpan balik positif dari pengguna  
**Aman** - *Best practices* keamanan diimplementasikan untuk melindungi data pengguna  
**Berkinerja Tinggi** - Waktu respons <2 detik, mampu menangani pengguna bersamaan  
**Dapat Dikembangkan (*Scalable*)** - Arsitektur yang mendukung pertumbuhan bisnis  
**Terdokumentasi dengan Baik** - Dokumentasi komprehensif untuk keberlanjutan  
**Berharga** - Memberikan ROI terukur dengan pengembalian 1.743% dalam 5 tahun  

Proyek ini membuktikan bahwa dengan **metodologi yang tepat** (*Waterfall* SDLC), **teknologi yang sesuai** (Laravel, PHP, MySQL, Tailwind CSS), **tim yang berkomitmen**, dan **pemangku kepentingan yang terlibat**, bahkan proyek dengan garis waktu dan anggaran terbatas dapat menghasilkan sistem berkualitas tinggi yang memberikan nilai signifikan kepada bisnis.

Lebih dari sekadar memenuhi persyaratan akademik, proyek ini telah memberikan **dampak bisnis nyata** kepada CUR-HEART, **pengalaman belajar** yang berharga kepada tim pengembang, dan **kontribusi** kepada kumpulan pengetahuan dalam bidang sistem informasi kesehatan.

---

## 5.2 Saran

Berdasarkan hasil pengembangan dan evaluasi sistem yang telah dilakukan, berikut adalah saran untuk pengembangan dan perbaikan sistem di masa depan:

**Tabel 5.4 Rekomendasi Pengembangan Fase 2 (Peningkatan Masa Depan)**

| No | Fitur/Peningkatan | Deskripsi & Justifikasi | Prioritas | Estimasi Biaya | Manfaat yang Diharapkan |
|----|-------------------|------------------------|----------|---------------|-------------------------|
| **A. PRIORITAS TINGGI (Q1-Q2 2025)** | | | | | |
| 1 | **Notifikasi SMS** | SMS otomatis untuk konfirmasi, pengingat (24 jam sebelum), penjadwalan ulang. Kurangi *no-show* 8% ke 5% | **TINGGI** | Rp 2-3 juta + Rp 100-300/SMS | +Rp 15 juta/tahun, jangkau pengguna non-email |
| 2 | **Sistem Keanggotaan/Paket** | Program loyalitas: beli 5 dapat 1 gratis, langganan bulanan, voucher hadiah | **TINGGI** | Rp 5-7 juta | Tingkatkan CLV, pendapatan langganan +Rp 50 juta/tahun |
| 3 | **Lapisan *Caching* Redis** | *Cache* data sesi dan query frequent untuk peningkatan performa | **TINGGI** | Rp 2-3 juta + Rp 1-2 juta/tahun | Waktu muat <1 detik, tangani 100+ pengguna bersamaan |
| 4 | **Autentikasi Dua Faktor** | SMS OTP/Google Authenticator untuk keamanan enhanced (wajib terapis/admin) | **TINGGI** | Rp 3-5 juta + biaya SMS | Kurangi risiko pengambilalihan akun, tingkatkan kepercayaan |
| 5 | ***Backup* Cloud Otomatis** | *Backup* harian ke AWS S3/Google Cloud (enkripsi, versi, retensi 30 hari) | **TINGGI** | Rp 1-2 juta + Rp 500rb-1juta/tahun | Kesiapan pemulihan bencana, perlindungan *ransomware* |
| 6 | **Integrasi Terapi Video** | *Embed video* (Whereby/Zoom) untuk sesi jarak jauh | **TINGGI** | Rp 5-8 juta + Rp 2-5 juta/tahun | +Rp 40 juta/tahun (sesi *online*), ekspansi pasar |
| **B. PRIORITAS SEDANG (Q2-Q3 2025)** | | | | | |
| 7 | **Aplikasi *Mobile*** | Native app iOS/Android (React Native/Flutter) dengan notifikasi *push*, *offline* | **SEDANG** | Rp 25-40 juta + Rp 5 juta/tahun | UX mobile lebih baik, +10% retensi = +Rp 20 juta/tahun |
| 8 | ***Dashboard* Analitik Lanjutan** | BI *dashboard* dengan tren, peramalan, metrik terapis, analisis pendapatan | **SEDANG** | Rp 3-5 juta | Keputusan data-driven, +5% optimisasi = +Rp 20 juta/tahun |
| 9 | **CDN untuk Aset Statis** | CloudFlare/AWS CloudFront untuk gambar, CSS, JS | **SEDANG** | Rp 1-2 juta + Rp 1-3 juta/tahun | Muat halaman lebih cepat, tingkatkan SEO, kurangi bandwidth |
| 10 | **Enkripsi Data *At Rest*** | Enkripsi kolom DB sensitif (catatan sesi, riwayat medis) | **SEDANG** | Rp 2-3 juta | Kepatuhan UU PDP, perlindungan kerahasiaan |
| 11 | **APM (New Relic/Sentry)** | Pemantauan & peringatan untuk tracking error *real-time* | **SEDANG** | Rp 2-3 juta/tahun | Deteksi masalah proaktif, identifikasi hambatan kinerja |
| 12 | **Sistem Ulasan Publik** | Feedback terstruktur, analisis sentimen, ulasan publik untuk bukti sosial | **SEDANG** | Rp 2-3 juta | +10% konversi = +Rp 15 juta/tahun |
| **C. PRIORITAS RENDAH (Q3-Q4 2025)** | | | | | |
| 13 | ***Chatbot* AI** | AI-powered chatbot (DialogFlow/OpenAI) untuk FAQ, bantuan reservasi, support 24/7 | **RENDAH** | Rp 10-15 juta + Rp 2-5 juta/tahun | Support 24/7, kurangi beban admin 10 jam/bulan |
| 14 | **Sinkronisasi Kalender** | Sync dengan Google Calendar untuk auto-update ketersediaan | **RENDAH** | Rp 3-4 juta | Kurangi update manual, cegah konflik |
| 15 | **Replika Baca Database** | Tambah DB read replica untuk handle traffic lebih tinggi | **RENDAH** | Rp 5-8 juta | *Future-proofing*, tingkatkan response time |
| 16 | **REST API Pihak Ketiga** | RESTful API dengan OAuth2 untuk integrasi partner | **RENDAH** | Rp 5-8 juta | Ekspansi ekosistem, potensi revenue tambahan |
| 17 | **Audit Keamanan Tahunan** | Penetration testing profesional oleh firma keamanan | **BERKELANJUTAN** | Rp 15-30 juta/tahun | Identifikasi vulnerability proaktif, compliance |

**Ringkasan Investasi Fase 2:**

| Prioritas | Fitur | Total Biaya (Implementasi) | Total Biaya Tahunan | ROI Tahunan yang Diharapkan | Periode *Payback* |
|----------|----------|---------------------------|------------------|-------------------|----------------|
| **TINGGI (6 fitur)** | SMS, Keanggotaan, Redis, 2FA, *Backup*, Video | **Rp 18-28 juta** | **Rp 5-10 juta** | **+Rp 125 juta/tahun** | **2-3 bulan** |
| **SEDANG (6 fitur)** | Aplikasi *Mobile*, Analitik, CDN, Enkripsi, APM, Ulasan | **Rp 36-58 juta** | **Rp 8-11 juta** | **+Rp 55 juta/tahun** | **6-8 bulan** |
| **RENDAH (5 fitur)** | *Chatbot* AI, Sinkronisasi Kalender, Replika DB, API, Audit Keamanan | **Rp 38-69 juta** | **Rp 20-35 juta** | **+Rp 6 juta/tahun** | **6+ tahun** (ROI rendah, nilai strategis) |
| **TOTAL (17 fitur)** | Peta Jalan Fase 2 Lengkap | **Rp 92-155 juta** | **Rp 33-56 juta** | **+Rp 186 juta/tahun** | **~6 bulan (rata-rata)** |

**Lingkup Fase 2 yang Direkomendasikan (2025):**
- **Fokus pada prioritas TINGGI** (6 fitur, investasi Rp 18-28 juta, pendapatan +Rp 125 juta/tahun)
- **Prioritas SEDANG selektif** (Aplikasi *Mobile* + Analitik, tambahan Rp 28-45 juta, +Rp 40 juta/tahun)
- **Total Fase 2 yang direkomendasikan**: Investasi Rp 46-73 juta, **pendapatan +Rp 165 juta/tahun** = **ROI 226-359%**

---

### 5.2.1 Saran untuk Pengembangan Sistem

Berdasarkan evaluasi sistem yang telah diimplementasikan, pengembangan Fase 2 harus difokuskan pada peningkatan yang memberikan ROI tertinggi dan memperkuat posisi kompetitif CUR-HEART. Detail lengkap prioritas pengembangan telah disajikan dalam **Tabel 5.4** di atas.

**Rekomendasi Strategis:**

Untuk tahun 2025, CUR-HEART disarankan untuk **fokus pada 6 fitur prioritas TINGGI** dengan total investasi Rp 18-28 juta yang diproyeksikan menghasilkan pendapatan tambahan **+Rp 125 juta/tahun** (ROI 446-694%, payback period 2-3 bulan). Fitur-fitur ini meliputi:

1. **Notifikasi SMS** untuk meningkatkan *show rate* dari 92% menjadi 95%
2. **Sistem Keanggotaan/Paket** untuk meningkatkan CLV dan membangun loyalitas
3. **Caching Redis** untuk performa optimal (<1 detik response time)
4. **Autentikasi 2FA** untuk keamanan enhanced sesuai *best practices*
5. **Backup Cloud Otomatis** untuk disaster recovery dan business continuity
6. **Integrasi Terapi Video** untuk ekspansi pasar geografis dan fleksibilitas layanan

Setelah fitur prioritas TINGGI berhasil diimplementasikan dan memberikan ROI yang terbukti, pengembangan dapat dilanjutkan dengan **fitur prioritas SEDANG** (Aplikasi Mobile Native dan Dashboard Analitik Lanjutan) yang akan memberikan nilai tambah signifikan untuk pengalaman pengguna dan pengambilan keputusan berbasis data.

**Pendekatan Implementasi:**

Implementasi harus dilakukan secara **bertahap dan terukur** dengan pola: *Plan - Develop - Test - Deploy - Measure - Iterate*. Setiap fitur harus divalidasi dampak bisnisnya sebelum melanjutkan ke fitur berikutnya, memastikan investasi TI selalu aligned dengan *business goals* dan memberikan *value* nyata kepada CUR-HEART.

---

**Tabel 5.7 Rekomendasi Operasional dan Manajemen**

| No | Area | Rekomendasi | Item Tindakan | Timeline | Prioritas |
|----|------|-------------|---------------|----------|----------|
| **A. ADOPSI & PELATIHAN** | | | | | |
| 1 | **Program Pelatihan Berkelanjutan** | Sesi refresh triwulanan untuk maintain kompetensi dan introduce fitur baru | Jadwalkan training 2 jam/triwulan, buat video self-learning, update manual, Q&A bulanan | Triwulanan | **TINGGI** |
| 2 | **Program *Champion* Pengguna** | Identifikasi 2-3 "super user" tiap kelompok untuk bantu yang lain | Identifikasi champion, beri training lanjutan, buat peer support group, beri insentif | Q1 2025 | **SEDANG** |
| 3 | **Manajemen Resistensi** | Atasi resistensi via komunikasi dan transisi bertahap | Sesi one-on-one, tekankan benefit, periode paralel 1 bulan, share success stories | Bulan 1-2 | **TINGGI** |
| **B. PROSES OPERASIONAL** | | | | | |
| 4 | **SOP Operasional** | Dokumentasi SOP untuk proses operasional utama | Buat SOP: booking workflow, sesi documentation, payment verification, user management, incident response | Q1 2025 | **TINGGI** |
| 5 | **Rutinitas Monitoring Harian** | Daily system health check untuk deteksi proaktif | Cek pagi: uptime & error logs; Siang: booking & payment; Malam: backup & metrics; Review mingguan | Harian | **TINGGI** |
| 6 | **Rencana Respons Insiden** | Prosedur eskalasi untuk masalah sistem | Define severity (Kritis/Tinggi/Sedang/Rendah), matriks eskalasi, SLA response time, template komunikasi | Q1 2025 | **TINGGI** |
| **C. MANAJEMEN KEUANGAN** | | | | | |
| 7 | **Anggaran Operasional TI** | Alokasi anggaran tahunan untuk maintenance, hosting, upgrade | Budget Rp 50 juta/tahun, review bulanan actual vs budget, forecast triwulanan | Tahunan (Q4) | **TINGGI** |
| 8 | **Pemantauan ROI** | Track ROI bulanan untuk ensure continuous value delivery | Track metrics: booking volume, revenue, time saved, satisfaction; Laporan bulanan, review triwulanan | Bulanan | **SEDANG** |
| 9 | **Perencanaan Investasi Fase 2** | Rencanakan upgrade Fase 2 based on ROI priority | Review fitur Fase 2, pilih prioritas TINGGI, budget Rp 18-28 juta, schedule Q1-Q2 2025 | Q4 2024 | **SEDANG** |
| **D. DATA & KEPATUHAN** | | | | | |
| 10 | **Verifikasi *Backup*** | Test backup recovery rutin untuk ensure business continuity | Bulanan: test random table; Triwulanan: test full DB recovery; Dokumentasi prosedur, ukur RTO <4 jam | Bulanan | **TINGGI** |
| 11 | **Kepatuhan UU PDP** | Ensure compliance dengan UU No. 27/2022 Perlindungan Data Pribadi | Review privacy policy, implement data subject rights, dokumentasi DPA, consent management, training staff | Q1 2025 | **TINGGI** |
| 12 | **Kebijakan Retensi Data** | Tentukan berapa lama simpan berbagai tipe data | Data klien: 5 tahun; Catatan sesi: 7 tahun; Pembayaran: 10 tahun; Soft delete kemudian Hard delete setelah periode | Q1 2025 | **SEDANG** |
| **E. KOMUNIKASI STAKEHOLDER** | | | | | |
| 13 | **Laporan Kinerja Bulanan** | Share system performance metrics dengan stakeholders | Laporan: booking trends, revenue, satisfaction, uptime, issues; Email minggu pertama tiap bulan | Bulanan | **SEDANG** |
| 14 | **Pengumpulan Feedback** | Kumpulkan user feedback sistematis untuk continuous improvement | Survei post-booking, NPS triwulanan, feedback button in-app, quarterly review meeting | Triwulanan | **SEDANG** |
| 15 | **Berbagi Success Stories** | Dokumentasi dan share success stories untuk marketing | Identifikasi klien satisfied (9-10), minta testimonial, buat case study, share di website/socmed | Triwulanan | **RENDAH** |
| **F. PERBAIKAN BERKELANJUTAN** | | | | | |
| 16 | **Tinjauan Sistem Bulanan** | Monthly review meeting untuk assess performance dan plan improvements | Peserta: Owner, Ops Manager, IT Support; Agenda: KPI review, issues, feedback, prioritas, action plan | Bulanan | **SEDANG** |
| 17 | **Tinjauan Strategis Tahunan** | Annual strategic review untuk align system dengan business strategy | Review business goals vs capabilities, evaluate ROI, review tech trends, budget planning, roadmap update | Tahunan (Q4) | **SEDANG** |
| 18 | **Transfer Pengetahuan** | Transfer knowledge dari dev team ke internal staff/vendor untuk sustainability | Handover dokumentasi, training IT staff, code walkthrough, contact list, transisi 3 bulan dengan support | Q2 2025 | **SEDANG** |

**Ringkasan Rekomendasi Operasional:**

| Area | Rekomendasi | Prioritas | Dampak yang Diharapkan |
|------|-------------|----------|------------------------|
| **Adopsi & Pelatihan Pengguna** | 3 | TINGGI | Tingkat adopsi berkelanjutan tinggi (100%), beban dukungan berkurang |
| **Proses Operasional** | 3 | TINGGI | Operasi konsisten, pemantauan proaktif, respons insiden cepat |
| **Manajemen Keuangan** | 3 | TINGGI-SEDANG | Biaya dapat diprediksi, ROI terjustifikasi, perencanaan investasi strategis |
| **Manajemen Data & Kepatuhan** | 3 | TINGGI | Kepatuhan hukum, kelangsungan bisnis, kepercayaan klien |
| **Komunikasi Pemangku Kepentingan** | 3 | SEDANG | Transparansi, keterlibatan, perbaikan yang didorong pengguna |
| **Perbaikan Berkelanjutan** | 3 | SEDANG | Evolusi sistem jangka panjang, keselarasan strategis, keberlanjutan |
| **TOTAL** | **18** | | **Keunggulan Operasional + Keberlanjutan Jangka Panjang** |

---

### 5.2.2 Saran untuk Manajemen dan Operasional

Keberhasilan implementasi sistem tidak hanya bergantung pada kualitas teknis, tetapi juga pada adopsi pengguna, proses operasional yang efektif, dan manajemen yang berkelanjutan. **Tabel 5.7** telah menyajikan 18 rekomendasi operasional dan manajemen yang komprehensif, mencakup 6 area kunci: Adopsi & Pelatihan, Proses Operasional, Manajemen Keuangan, Data & Kepatuhan, Komunikasi Stakeholder, dan Perbaikan Berkelanjutan.

**Prioritas Implementasi:**

Untuk memastikan keberlanjutan dan optimalisasi sistem jangka panjang, CUR-HEART disarankan untuk:

1. **Segera (Q4 2024 - Q1 2025):** Implementasi rekomendasi prioritas TINGGI (#1, 3, 4, 5, 6, 7, 10, 11) yang mencakup program pelatihan berkelanjutan, SOP operasional, monitoring harian, incident response plan, budgeting TI, backup verification, dan kepatuhan UU PDP. Area ini kritis untuk operasional stabil dan compliance.

2. **Jangka Menengah (Q2-Q3 2025):** Fokus pada rekomendasi prioritas SEDANG (#2, 8, 9, 12-18) untuk memperkuat continuous improvement, stakeholder engagement, dan sustainability jangka panjang.

**Manajemen Perubahan:**

Adopsi sistem baru memerlukan *change management* yang efektif. Program pelatihan berkelanjutan (refresh triwulanan), sistem *user champion* untuk peer support, dan komunikasi proaktif kepada stakeholders akan memastikan tingkat adopsi tetap tinggi (target 100%) dan resistensi dapat dimitigasi sejak dini.

**Budgeting & ROI Tracking:**

Alokasi budget operasional TI sebesar Rp 50 juta/tahun (mencakup hosting, maintenance, security audit, contingency) harus disertai dengan tracking ROI bulanan untuk memastikan sistem terus memberikan value. Pemantauan metrik kunci (booking volume, revenue, time saved, user satisfaction) akan menjadi dasar untuk justifikasi investasi Fase 2.

**Business Continuity:**

Verifikasi backup bulanan, rencana incident response dengan SLA yang jelas, dan kepatuhan terhadap UU PDP No. 27/2022 adalah fondasi untuk business continuity dan trust klien. Dokumentasi SOP dan transfer knowledge kepada internal staff/vendor akan memastikan sistem tetap sustainable meskipun terjadi pergantian personel.

**Kesimpulan:**

Implementasi rekomendasi operasional dan manajemen dalam Tabel 5.7 secara konsisten akan menghasilkan **keunggulan operasional** dan **keberlanjutan jangka panjang**, memposisikan CUR-HEART sebagai *leader* dalam penerapan teknologi untuk layanan kesehatan mental di Indonesia.

---

**Tabel 5.8 Rekomendasi Penelitian Lanjutan**

| No | Area Penelitian | Pertanyaan Penelitian | Metodologi yang Disarankan | Kontribusi Potensial | Dampak Potensial |
|----|-----------------|----------------------|---------------------------|---------------------|------------------|
| **A. RISET TEKNIS** | | | | | |
| 1 | ***Monolithic* vs *Microservices* untuk Sistem Kesehatan UKM** | Apa *trade-offs* arsitektur *monolithic* (Laravel) vs *microservices* untuk sistem kesehatan <10.000 pengguna? | • Studi komparatif<br>• Benchmark kinerja (*latency*, *throughput*, skalabilitas)<br>• Metrik: upaya development, waktu ke pasar, biaya pemeliharaan<br>• Tools: Load testing (JMeter), profiling | • Framework keputusan pemilihan arsitektur berbasis ukuran bisnis<br>• Panduan berbasis bukti untuk IT kesehatan UKM<br>• Cost-benefit analysis berbagai arsitektur<br>• Publikasi software engineering journals | **TINGGI**<br>(Panduan praktis untuk keputusan arsitektur yang dihadapi banyak startup kesehatan) |
| 2 | ***Machine Learning* untuk Prediksi Hasil Terapi** | Dapatkah model ML memprediksi hasil terapi (kesuksesan, risiko putus) berdasarkan profil klien dan data historis? | • Studi pemodelan prediktif<br>• Data: sesi historis (demografi, assessment scores, frekuensi sesi)<br>• Model: Logistic Regression, Random Forest, XGBoost, Neural Networks<br>• Evaluasi: Akurasi, Precision, Recall, F1-Score, AUC-ROC | • Model prediktif identifikasi dini klien berisiko<br>• Rekomendasi perawatan personalized<br>• Bukti untuk AI dalam kesehatan mental<br>• Publikasi AI healthcare journals | **SANGAT TINGGI**<br>(Dapat merevolusi efektivitas terapi melalui intervensi dini & personalisasi) |
| 3 | ***Blockchain* untuk Keamanan Rekam Medis Kesehatan Mental** | Dapatkah teknologi *blockchain* meningkatkan keamanan dan kekekalan rekam kesehatan mental dibandingkan enkripsi DB tradisional? | • Implementasi proof-of-concept<br>• Teknologi: Private blockchain (Hyperledger Fabric) vs Traditional encrypted DB<br>• Evaluasi: Keamanan, kinerja (*throughput*, *latency*), biaya<br>• Testing: Penetration testing, performance benchmarking | • Blueprint implementasi blockchain untuk data kesehatan mental<br>• Kuantifikasi peningkatan keamanan<br>• Cost-benefit analysis<br>• Publikasi blockchain/cybersecurity journals | **SEDANG**<br>(Inovatif tetapi ROI tidak pasti; berguna untuk high-security requirements) |
| 4 | ***Dashboard* Analitik *Real-Time* untuk Operasi Kesehatan** | Apa arsitektur optimal untuk *dashboard* analitik *real-time* (*latency* <5 detik)? | • Design science research<br>• Bandingkan: Stream processing (Kafka, Flink) vs ETL batch tradisional vs Materialized views<br>• Metrik: Latency, akurasi, biaya, kompleksitas<br>• Validasi: Usability testing dengan user aktual | • Arsitektur referensi untuk analitik kesehatan real-time<br>• Panduan pemilihan teknologi<br>• Performance benchmarks<br>• Publikasi data engineering conferences | **TINGGI**<br>(Semakin penting untuk keputusan kesehatan berbasis data; demand tinggi) |
| **B. RISET BISNIS** | | | | | |
| 5 | **Dampak Transformasi Digital pada Penyedia Layanan Kesehatan UKM** | Apa faktor sukses kritis transformasi digital dalam praktik terapi & bagaimana pengaruhnya terhadap kinerja bisnis? | • Studi kasus ganda (10-15 praktik terapi)<br>• Data: Wawancara (pemilik, staf), survei (klien), data keuangan<br>• Analisis: Analisis tematik (kualitatif), regresi (kuantitatif) | • Framework faktor sukses kritis digitalisasi UKM kesehatan<br>• Panduan praktis untuk praktik lain<br>• Best practices change management<br>• Publikasi business management journals | **SANGAT TINGGI**<br>(Nilai praktis tinggi untuk ribuan penyedia layanan kesehatan UKM global) |
| 6 | **Penerimaan Teknologi dalam Konteks Terapi (TAM/UTAUT)** | Faktor apa yang mempengaruhi penerimaan klien & terapis terhadap sistem manajemen terapi digital? | • Survei research (200+ klien, 50+ terapis)<br>• Framework: Extended TAM/UTAUT (tambah: privacy concern, therapeutic trust, perceived empathy)<br>• Analisis: Structural Equation Modeling (SEM), multi-group analysis | • Model penerimaan teknologi khusus konteks terapi<br>• Rekomendasi desain untuk adopsi lebih tinggi<br>• Kontribusi teori (TAM extension)<br>• Publikasi Information Systems journals | **TINGGI**<br>(Mengisi gap teori; nilai praktis untuk desain produk kesehatan digital) |
| **C. RISET PENGALAMAN PENGGUNA** | | | | | |
| 7 | **UX Lanjut Usia dalam Platform Kesehatan Digital** | Apa hambatan dan fasilitas bagi orang dewasa lanjut usia (60+) dalam menggunakan platform reservasi terapi online? | • Mixed methods (30-50 pengguna 60+)<br>• Usability testing (task completion, errors, time)<br>• Interview (hambatan), survei (attitude)<br>• Analisis: Kuantitatif (metrik UX) + Kualitatif (thematic analysis) | • Pedoman desain ramah usia untuk platform kesehatan<br>• Rekomendasi aksesibilitas spesifik<br>• Prinsip inclusive design<br>• Publikasi HCI conferences | **TINGGI**<br>(Populasi menua meningkatkan pentingnya; mengatasi kesetaraan kesehatan digital) |
| 8 | **Persepsi Privasi dalam Teknologi Kesehatan Mental** | Bagaimana pengguna mempersepsikan privasi data dalam aplikasi kesehatan mental & fitur apa yang mempengaruhi kepercayaan? | • Survei + Focus group (200+ pengguna)<br>• Instrumen: Privacy Concern Scale, Trust in Technology Scale, Feature Preference Survey<br>• Analisis: Factor analysis, regression (privacy features ke trust), thematic analysis | • Framework desain privasi untuk teknologi kesehatan mental<br>• Bukti efektivitas "privacy by design"<br>• Model kepercayaan pengguna konteks sensitif<br>• Publikasi privacy research journals | **SANGAT TINGGI**<br>(Privasi adalah hambatan kritis untuk adopsi; nilai praktis tinggi) |
| **D. RISET DOMAIN (HIPNOTERAPI)** | | | | | |
| 9 | **Dampak Pelacakan Kemajuan Digital pada Hasil Terapi** | Dapatkah pelacakan kemajuan digital meningkatkan hasil terapi dibandingkan pelacakan kertas tradisional? | • Quasi-experimental trial<br>• Grup Eksperimental: pelacakan digital vs Kontrol: metode tradisional<br>• Ukuran: Therapy outcome scales (GAD-7, PHQ-9), kepatuhan sesi, dropout rate<br>• Durasi: 6 bulan; Analisis: t-test, Chi-square | • Bukti untuk digital tools dalam efektivitas terapi<br>• Dampak terkuantifikasi pelacakan kemajuan<br>• Pedoman praktik klinis<br>• Publikasi clinical psychology journals | **SANGAT TINGGI**<br>(Secara langsung menunjukkan nilai klinis digital tools; potensi sitasi tinggi) |
| 10 | ***Teletherapy* vs Hipnoterapi Tatap Muka: Efektivitas Komparatif** | Apakah hipnoterapi online sama efektifnya dengan sesi tatap muka untuk kecemasan & stress management? | • Randomized Controlled Trial (100-200 klien)<br>• Randomize: online vs face-to-face<br>• Kondisi: Kecemasan, stress management<br>• Ukuran: Clinical scales (pre-post), satisfaction, therapeutic alliance<br>• Analisis: ANCOVA, non-inferiority analysis | • Bukti efektivitas klinis untuk teletherapy dalam hipnoterapi<br>• Non-inferiority evidence (jika teletherapy sama efektif)<br>• Menginformasikan kebijakan telehealth<br>• Publikasi mental health journals | **SANGAT TINGGI**<br>(Pertanyaan kritis post-pandemi; dampak kebijakan tinggi; aksesibilitas layanan) |
| 11 | **Optimisasi Frekuensi Sesi Hipnoterapi** | Apa frekuensi sesi optimal (mingguan vs dua mingguan vs bulanan) untuk berbagai tujuan hipnoterapi? | • Studi komparatif<br>• Grup: Klien dikelompokkan berdasarkan frekuensi sesi (data historis)<br>• Data: Frekuensi sesi, tujuan terapi, outcome, dropout rate<br>• Analisis: Survival analysis (dropout), regression (frekuensi ke outcome) | • Rekomendasi penjadwalan berbasis bukti<br>• Perencanaan perawatan personalized<br>• Optimisasi resource (efisiensi frekuensi sesi)<br>• Publikasi clinical research journals | **SEDANG-TINGGI**<br>(Nilai praktis untuk perencanaan terapi; optimisasi alokasi sumber daya) |
| 12 | **Analisis ROI Jangka Panjang Investasi IT Kesehatan** | Bagaimana nilai investasi IT kesehatan berkembang selama 3-5 tahun & faktor apa yang memprediksi ROI berkelanjutan? | • Studi longitudinal (3-5 tahun)<br>• Sampel: Beberapa organisasi kesehatan<br>• Data: Metrik keuangan (revenue, cost), operasional (efisiensi), satisfaction (over time)<br>• Analisis: Time series analysis, longitudinal regression | • Model ROI jangka panjang dengan penyesuaian berbasis waktu<br>• Faktor prediksi nilai berkelanjutan<br>• Justifikasi berbasis bukti untuk investasi IT berkelanjutan<br>• Publikasi health economics journals | **SANGAT TINGGI**<br>(Kritis untuk keputusan investasi IT; bukti longitudinal langka) |


**Ringkasan Rekomendasi Penelitian:**

| Area Penelitian | Jumlah Topik | Tingkat Kesulitan | Dampak yang Diharapkan | Total Durasi |
|--------------|-----------------|-----------------|----------------|----------------|
| **Penelitian Teknis** | 4 | SEDANG-SANGAT TINGGI | TINGGI-SANGAT TINGGI | 4-12 bulan per studi |
| **Bisnis & Manajemen** | 3 | SEDANG-TINGGI | SANGAT TINGGI | 4 bulan - 5 tahun |
| **Pengalaman Pengguna** | 2 | SEDANG | TINGGI-SANGAT TINGGI | 3-6 bulan per studi |
| **Spesifik Domain (Hipnoterapi)** | 3 | SEDANG-TINGGI | SEDANG-SANGAT TINGGI | 6-18 bulan per studi |
| **TOTAL** | **12 Topik** | | | |

**Topik Penelitian Prioritas (5 Teratas berdasarkan Potensi Dampak):**
1. **Dampak Transformasi Digital pada UKM Kesehatan** (Bisnis) - Nilai praktis tinggi, mengatasi kebutuhan luas
2. ***Machine Learning* untuk Prediksi Hasil Terapi** (Teknis) - Potensi revolusioner, inovasi tinggi
3. **Terapi Jarak Jauh vs. Langsung: Efektivitas** (Domain) - Kritis pasca-pandemi, dampak kebijakan tinggi
4. **Analisis ROI: Nilai Jangka Panjang** (Bisnis) - Keputusan investasi TI berbasis bukti, bukti longitudinal langka
5. **Persepsi Privasi dalam Teknologi Kesehatan Mental** (UX) - Hambatan adopsi kritis, nilai praktis tinggi

---

### 5.2.3 Saran untuk Penelitian Lanjutan

Proyek ini telah membuka berbagai peluang penelitian lanjutan yang dapat memberikan kontribusi baik pada bidang akademik maupun praktis. **Tabel 5.8** menyajikan **12 topik penelitian potensial** yang dikelompokkan menjadi 4 kategori utama: Riset Teknis (4 topik), Riset Bisnis (2 topik), Riset Pengalaman Pengguna (2 topik), dan Riset Domain Hipnoterapi (4 topik).

**Prioritas Penelitian untuk Mahasiswa S1:**

Untuk mahasiswa yang ingin melanjutkan penelitian dari proyek ini, **3 topik prioritas SANGAT TINGGI** yang direkomendasikan:

1. **Machine Learning untuk Prediksi Hasil Terapi** (Topik #2 - Riset Teknis): Penelitian ini memiliki dampak potensial terbesar untuk merevolusi efektivitas terapi melalui personalisasi. Data sudah tersedia dari sistem CUR-HEART, metodologi clear (predictive modeling), dan hasil dapat langsung diaplikasikan untuk meningkatkan layanan.

2. **Dampak Transformasi Digital pada UKM Kesehatan** (Topik #5 - Riset Bisnis): Studi kasus CUR-HEART dapat menjadi salah satu dari 10-15 praktik yang diteliti. Nilai praktis sangat tinggi untuk ribuan penyedia layanan kesehatan UKM di Indonesia yang sedang/akan melakukan digitalisasi.

3. **Teletherapy vs Hipnoterapi Tatap Muka** (Topik #10 - Riset Domain): Pertanyaan kritis post-pandemi dengan dampak kebijakan tinggi. RCT ini dapat menginformasikan pedoman telehealth nasional dan meningkatkan aksesibilitas layanan kesehatan mental.

**Topik Lain dengan Dampak Tinggi:**
- **Persepsi Privasi dalam Teknologi Kesehatan Mental** (Topik #8): Mengatasi hambatan adopsi kritis
- **Dampak Pelacakan Kemajuan Digital** (Topik #9): Bukti langsung nilai klinis digital tools
- **Analisis ROI Jangka Panjang** (Topik #12): Justifikasi investasi IT berbasis bukti longitudinal

**Kontribusi Akademik:**

Penelitian lanjutan dari proyek ini berpotensi menghasilkan **12-18 publikasi** di jurnal/konferensi internasional, mencakup:
- **Software Engineering & System Architecture** (Topik #1, #4)
- **Artificial Intelligence in Healthcare** (Topik #2)
- **Cybersecurity & Blockchain** (Topik #3)
- **Business Management & Digital Transformation** (Topik #5, #12)
- **Information Systems & Technology Acceptance** (Topik #6)
- **Human-Computer Interaction & UX** (Topik #7, #8)
- **Clinical Psychology & Mental Health** (Topik #9, #10, #11)

**Kerjasama Riset:**

CUR-HEART terbuka untuk kerjasama penelitian dengan mahasiswa, dosen, atau peneliti yang tertarik dengan topik-topik di atas. Akses ke data sistem (dengan anonimisasi), wawancara dengan stakeholders, dan dukungan implementasi proof-of-concept dapat difasilitasi untuk tujuan akademik yang sah.

---

### 5.2.4 Penutup Saran

Saran-saran yang disampaikan di atas merupakan **peta jalan untuk perbaikan berkelanjutan** dari Sistem CUR-HEART. Tidak semua saran perlu diimplementasikan sekaligus. **Prioritisasi** berdasarkan:

1. **Nilai Bisnis** - Mana yang paling berdampak ke pendapatan atau efisiensi operasional
2. **Kebutuhan Pengguna** - Umpan balik dari pengguna aktual tentang titik masalah
3. **Ketersediaan Sumber Daya** - Anggaran, waktu, dan kapasitas tim
4. **Ketergantungan Teknis** - Prasyarat atau pekerjaan dasar yang diperlukan
5. **Tingkat Risiko** - Perbaikan berisiko rendah dapat diimplementasikan terlebih dahulu sebagai kemenangan cepat

**Pendekatan yang Disarankan:**
- **Jangka Pendek (3-6 bulan)**: Kemenangan cepat (optimisasi kinerja, peningkatan fitur minor, pelatihan pengguna)
- **Jangka Menengah (6-12 bulan)**: Fitur signifikan (aplikasi *mobile*, konferensi video, program loyalitas)
- **Jangka Panjang (1-2 tahun)**: Inisiatif strategis (integrasi AI, analitik lanjutan, ekspansi internasional)

Dengan **pola pikir perbaikan berkelanjutan**, Sistem CUR-HEART dapat terus **berkembang untuk memenuhi kebutuhan bisnis yang berubah** dan **mempertahankan keunggulan kompetitif** dalam industri teknologi kesehatan.

---
