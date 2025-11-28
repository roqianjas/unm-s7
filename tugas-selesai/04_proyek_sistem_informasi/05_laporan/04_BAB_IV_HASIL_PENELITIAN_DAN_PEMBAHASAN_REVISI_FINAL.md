# BAB IV  
# HASIL PENELITIAN DAN PEMBAHASAN

## 4.1. INISIASI PROYEK

Proyek pengembangan CUR-HEART: Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital diinisiasi berdasarkan kebutuhan untuk mengoptimalkan operasional pusat layanan hipnoterapi dan kesehatan mental. CUR-HEART (*Hypnotherapy & Mind Wellness Center*) mengalami pertumbuhan signifikan dalam jumlah klien dan terapis, namun sistem manual yang digunakan menghambat efisiensi dan kualitas layanan.

### 4.1.1 Latar Belakang Masalah

Berdasarkan observasi dan wawancara yang dilakukan pada September 2024, teridentifikasi beberapa permasalahan utama:

1. **Proses reservasi manual** melalui WhatsApp dan telepon yang memakan waktu lama dan mengurangi tingkat konversi (hanya 60% dari pertanyaan menjadi reservasi aktual)

2. **Konflik jadwal dan reservasi ganda** terjadi 8-10 kasus per bulan karena manajemen jadwal menggunakan spreadsheet terpisah

3. **Dokumentasi terapi tidak terstruktur** dimana terapis menghabiskan 15 menit per sesi untuk pencatatan manual dengan risiko data hilang

4. **Tidak ada data untuk pengambilan keputusan** karena informasi tersebar di berbagai platform dan pembuatan laporan memakan waktu 2-3 hari

5. **Beban administratif tinggi** dengan admin menghabiskan 70% waktu untuk tugas repetitif seperti menjawab pertanyaan yang sama dan verifikasi pembayaran manual

6. **Risiko keamanan dan privasi data** klien yang sensitif disimpan dalam format tidak aman tanpa kontrol akses yang tepat

### 4.1.2 Identifikasi Masalah

Berdasarkan latar belakang di atas, penulis mengidentifikasikan beberapa masalah sebagai berikut:

a. Pelayanan reservasi terapi masih dilaksanakan secara konvensional sehingga kurang efektif dan efisien

b. Belum adanya sistem informasi reservasi berbasis web untuk reservasi dan manajemen terapi

c. Banyak terjadi kehilangan data klien karena belum adanya sistem informasi yang dapat mendata siapa saja klien yang sedang melakukan reservasi dan mengikuti sesi terapi

### 4.1.3 Ruang Lingkup

Ruang lingkup proyek ini mencakup pengembangan sistem informasi berbasis web dengan fitur-fitur utama:

- **Modul Reservasi Online**: Klien dapat melihat jadwal terapis, memilih layanan, dan melakukan reservasi secara mandiri 24/7
- **Manajemen Jadwal Terapis**: Sistem penjadwalan otomatis dengan deteksi konflik dan notifikasi
- **Dokumentasi Sesi Terapi**: Platform digital untuk terapis mencatat dan mengakses riwayat terapi klien
- **Pembayaran Terintegrasi**: Integrasi dengan *payment gateway* Midtrans untuk pembayaran online
- **Dashboard Admin**: Panel kontrol untuk pemantauan reservasi, terapis, dan laporan keuangan
- **Notifikasi Otomatis**: Pengingat email untuk klien dan terapis tentang jadwal sesi

### 4.1.4 Tujuan dan Manfaat Penelitian

**Tujuan penelitian dalam capstone project ini adalah:**

a. Agar pelayanan reservasi terapi dapat berjalan dengan efektif dan efisien

b. Sistem informasi reservasi diharapkan dapat memudahkan klien dalam melakukan reservasi dan melihat riwayat terapi

c. Dengan adanya sistem informasi dapat memudahkan baik klien, petugas admin, maupun terapis dalam pengelolaan data reservasi dan sesi terapi, sehingga semuanya dapat terkontrol dengan baik

d. Sebagai salah satu syarat kelulusan pada Program Studi Strata Satu (S1) untuk Program Studi Sistem Informasi di Fakultas Teknologi Informasi Universitas Nusa Mandiri

**Manfaat penelitian:**

Penelitian ini diharapkan memberikan manfaat bagi berbagai pihak:

- **Bagi CUR-HEART**: Meningkatkan efisiensi operasional, mengurangi kesalahan jadwal, dan mempercepat pertumbuhan bisnis
- **Bagi Klien**: Kemudahan dalam reservasi layanan terapi kapan saja tanpa harus menghubungi admin
- **Bagi Terapis**: Mengurangi beban administratif dan memudahkan akses riwayat klien
- **Bagi Admin**: Otomasi tugas repetitif sehingga dapat fokus pada layanan pelanggan yang lebih berkualitas
- **Bagi Akademik**: Sebagai referensi pengembangan sistem informasi sejenis untuk layanan kesehatan mental

---

## 4.2. PERENCANAAN PROYEK

Perencanaan proyek dilakukan untuk memastikan proyek berjalan sesuai target waktu, biaya, dan kualitas yang ditetapkan. Perencanaan mencakup berbagai area pengetahuan manajemen proyek yang telah diidentifikasi mencakup ruang lingkup (*scope*), waktu (*time*), biaya (*cost*), kualitas (*quality*), sumber daya (*resource*), risiko (*risk*), komunikasi (*communication*), pengadaan (*procurement*), integrasi (*integration*), serta manajemen pemangku kepentingan (*stakeholder*).

### 4.2.1 Perencanaan Ruang Lingkup (*Scope*)

Ruang lingkup proyek didefinisikan menggunakan *Work Breakdown Structure* (WBS) yang membagi pekerjaan menjadi komponen-komponen yang dapat dikelola. WBS proyek ini mencakup 6 fase utama dengan total lebih dari 40 *work packages* yang terdistribusi ke dalam aktivitas-aktivitas terstruktur.

**Tabel 4.1 Work Breakdown Structure (WBS)**

| Level 1 | Level 2 | Level 3 | Deskripsi |
|---------|---------|---------|-----------|
| 1. Project Management | 1.1 Inisiasi | 1.1.1 Identifikasi Masalah | Observasi dan wawancara pemangku kepentingan |
| | | 1.1.2 Studi Kelayakan | Analisis kelayakan teknis, operasional, ekonomi |
| | 1.2 Perencanaan | 1.2.1 Penyusunan WBS | Rincian struktur pekerjaan |
| | | 1.2.2 Estimasi Biaya | Perhitungan biaya pengembangan |
| | 1.3 Monitoring | 1.3.1 Progress Tracking | Pemantauan kemajuan mingguan |
| 2. Analysis | 2.1 Requirements | 2.1.1 Functional Requirements | Identifikasi 40+ kebutuhan fungsional |
| | | 2.1.2 Non-functional Requirements | Keamanan, kinerja, kegunaan |
| | 2.2 System Analysis | 2.2.1 As-Is Process | Dokumentasi proses bisnis saat ini |
| | | 2.2.2 To-Be Process | Rancangan proses bisnis baru |
| 3. Design | 3.1 Database Design | 3.1.1 ERD | Diagram relasi entitas 16 tabel |
| | | 3.1.2 Normalisasi | Normalisasi hingga 3NF |
| | 3.2 UI/UX Design | 3.2.1 Wireframe | Sketsa antarmuka pengguna |
| | | 3.2.2 Mockup | Desain visual 66 halaman di Figma |
| | 3.3 UML Diagrams | 3.3.1 Use Case Diagram | Diagram kasus penggunaan |
| | | 3.3.2 Activity Diagram | Diagram aktivitas proses bisnis |
| 4. Implementation | 4.1 Backend | 4.1.1 Laravel Setup | Instalasi dan konfigurasi *framework* |
| | | 4.1.2 Database Migration | Migrasi skema basis data |
| | | 4.1.3 API Development | Pengembangan *controller* dan *model* |
| | 4.2 Frontend | 4.2.1 Blade Templates | Pembuatan templat *view* |
| | | 4.2.2 Tailwind Styling | *Styling* dengan Tailwind CSS |
| | 4.3 Integration | 4.3.1 Payment Gateway | Integrasi Midtrans |
| | | 4.3.2 Email Service | Konfigurasi notifikasi email |
| 5. Testing | 5.1 Unit Testing | 5.1.1 PHPUnit Tests | 30 *test cases* |
| | 5.2 Integration Testing | 5.2.1 API Testing | Pengujian integrasi antar modul |
| | 5.3 UAT | 5.3.1 User Testing | Pengujian oleh pengguna akhir |
| 6. Deployment | 6.1 Server Setup | 6.1.1 VPS Configuration | Pengaturan Ubuntu, Nginx, PHP, MySQL |
| | | 6.1.2 SSL Certificate | Instalasi Let's Encrypt |
| | 6.2 Go Live | 6.2.1 Database Migration | Migrasi data ke produksi |
| | | 6.2.2 System Launch | Peluncuran sistem |

**Gantt Chart:**

*Gantt Chart* menampilkan jadwal proyek dalam bentuk diagram batang yang menunjukkan tanggal mulai, durasi, dan tanggal selesai dari setiap aktivitas.

**[GAMBAR 4.1 - Gantt Chart Proyek CUR-HEART]**

```
Activity                  | Week
                          | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
──────────────────────────┼────────────────────────────────────────────────
1. Requirements Analysis  |████████                                         
   - Observation          |████                                             
   - Interview            |    ████                                         
   - Documentation        |████████                                         
                          |                                                 
2. System Design          |        ████████                                 
   - Database Design      |        ████                                     
   - UI/UX Design         |            ████                                 
   - UML Diagrams         |        ████████                                 
                          |                                                 
3. Implementation         |                ████████████████████████████     
   - Backend Development  |                ████████████████                 
   - Frontend Development |                    ████████████████             
   - Integration          |                            ████████             
                          |                                                 
4. Testing                |                                    ████████████ 
   - Unit Testing         |                                    ████         
   - Integration Testing  |                                        ████     
   - Functional Testing   |                                        ████     
   - UAT                  |                                            ████ 
                          |                                                 
5. Deployment             |                                                ████
   - Server Setup         |                                                ██  
   - Migration            |                                                  ██
   - Go Live              |                                                  ██
                          |                                                 
6. Documentation          |                                                ████████████████
   - Report Writing       |                                                ████████████████
   - Presentation Prep    |                                                            ████
```

### 4.2.2 Perencanaan Waktu Pengerjaan (*Time*)

Proyek dikerjakan selama 16 minggu (4 bulan) dengan pembagian waktu sebagai berikut:

**Tabel 4.2 Jadwal Pengerjaan Proyek**

| No | Fase | Durasi | Periode | Luaran |
|----|------|--------|---------|--------|
| 1 | Analisis Kebutuhan | 2 minggu | 16-29 Sep 2024 | Dokumen SRS, Studi Kelayakan |
| 2 | Desain Sistem | 2 minggu | 30 Sep - 13 Okt 2024 | ERD, Diagram UML, Mockup UI/UX |
| 3 | Implementasi | 4 minggu | 14 Okt - 10 Nov 2024 | Aplikasi web 60+ halaman |
| 4 | Pengujian | 2 minggu | 11-24 Nov 2024 | Laporan pengujian, persetujuan UAT |
| 5 | Deployment | 1 minggu | 25 Nov - 1 Des 2024 | Sistem produksi aktif |
| 6 | Dokumentasi | 5 minggu | Paralel dengan semua fase | Laporan akhir, manual, presentasi |

### 4.2.3 Perencanaan Anggaran Biaya (*Cost*)

Estimasi biaya proyek menggunakan metode bottom-up berdasarkan WBS:

**Tabel 4.3 Estimasi Biaya Proyek**

| No | Kategori | Item | Biaya (Rp) |
|----|----------|------|------------|
| 1 | Project Management | Project Manager (11 minggu × Rp 100.000/minggu) | 1.100.000 |
| | | Contingency (10%) | 110.000 |
| 2 | Hardware | Laptop Development (sudah ada) | 0 |
| | | VPS Hosting (1 tahun) | 1.200.000 |
| 3 | Software | Laravel Framework (gratis) | 0 |
| | | MySQL Database (gratis) | 0 |
| | | Domain & SSL (1 tahun) | 150.000 |
| 4 | Development | Backend Developer (4 minggu × Rp 200.000/minggu) | 800.000 |
| | | Frontend Developer (4 minggu × Rp 200.000/minggu) | 800.000 |
| | | Full-stack Developer (4 minggu × Rp 200.000/minggu) | 800.000 |
| 5 | Testing | Testing Tools (gratis - PHPUnit) | 0 |
| | | UAT Sessions | 200.000 |
| 6 | Training | User Training Materials | 100.000 |
| 7 | Lain-lain | Dokumentasi, Transport, Komunikasi | 300.000 |
| **TOTAL** | | | **5.560.000** |

**Estimasi Biaya Berulang Tahunan (Biaya Operasional):**

| No | Item | Biaya/Tahun (Rp) |
|----|------|------------------|
| 1 | VPS Hosting | 1.200.000 |
| 2 | Domain & SSL renewal | 150.000 |
| 3 | Payment Gateway Fee (2,9% + Rp 2.000 per transaksi) | ~7.200.000 (estimasi 100 transaksi/bulan) |
| 4 | Pemeliharaan & Dukungan | 1.200.000 |
| **TOTAL** | | **9.750.000** |

### 4.2.4 Perencanaan Kualitas (*Quality*)

Standar kualitas yang ditetapkan untuk proyek ini:

**A. Standar Kualitas Fungsional:**
- **Fungsionalitas**: Minimal 90% kebutuhan fungsional harus terpenuhi dan berfungsi dengan baik
- **Akurasi**: 100% akurasi dalam perhitungan pembayaran, penjadwalan, dan pelaporan
- **Kelengkapan**: Semua modul utama (reservasi, pembayaran, dasbor) harus tersedia
- **Interoperabilitas**: Integrasi Midtrans dan layanan email berfungsi tanpa galat

**B. Standar Kualitas Non-Fungsional:**
- **Performa**: 
  - Waktu muat halaman < 2 detik (rata-rata)
  - Waktu respons API < 500ms untuk 95% permintaan
  - Waktu kueri basis data < 100ms (rata-rata)
- **Keamanan**: 
  - Mitigasi kerentanan OWASP Top 10
  - *Hashing* kata sandi dengan *bcrypt*
  - HTTPS untuk semua komunikasi
  - Pencegahan *SQL injection* (Eloquent ORM)
- **Usabilitas**: 
  - Skor *System Usability Scale* (SUS) minimal 70/100
  - Tingkat kepuasan pengguna minimal 4/5
  - Tingkat penyelesaian tugas ≥ 90%
- **Keandalan**: 
  - Waktu aktif minimal 99% (maksimal waktu mati 7,2 jam/bulan)
  - Waktu Rata-rata Antar Kegagalan (*Mean Time Between Failures*/MTBF) > 720 jam
  - Tujuan Waktu Pemulihan (*Recovery Time Objective*/RTO) < 4 jam
- **Kemudahan Pemeliharaan**: 
  - Cakupan pengujian kode minimal 70%
  - Skor kualitas kode (CodeClimate) ≥ B
  - Dokumentasi lengkap (*inline comments*, README, dokumentasi API)

### 4.2.5 Perencanaan Sumber Daya (*Resource*)

**A. Sumber Daya Manusia:**

**Tabel 4.4 Alokasi Sumber Daya Manusia**

| No | Nama | Peran | Tanggung Jawab | Alokasi Waktu |
|----|------|-------|----------------|---------------|
| 1 | Roki Anjas (11250066) | Project Manager & Backend Developer | Koordinasi tim, pengembangan backend, dokumentasi | 40 jam/minggu |
| 2 | Susanto (11250068) | Frontend Developer & UI/UX Designer | Desain antarmuka, pengembangan frontend | 35 jam/minggu |
| 3 | Fahruroji (11250085) | Full-stack Developer & Database Architect | Desain database, pengembangan full-stack, deployment | 35 jam/minggu |

**B. Sumber Daya Teknologi:**
- **Perangkat Keras Pengembangan:**
  - Laptop/PC untuk pengembangan (3 unit - milik tim)
  - VPS Ubuntu 22.04 LTS untuk server produksi
  - Spesifikasi VPS: 4 vCPU, 8GB RAM, 160GB SSD

- **Perangkat Lunak Pengembangan:**
  - IDE: Visual Studio Code (gratis)
  - Kontrol Versi: Git & GitHub (gratis)
  - Desain: Figma (*free tier*)
  - *Framework*: Laravel 10 (*open source*)
  - Basis Data: MySQL 8.0 (*open source*)
  - *Framework* CSS: Tailwind CSS (*open source*)

**C. Sumber Daya Infrastruktur:**
- Domain & Sertifikat SSL
- Layanan email (SMTP)
- Akun *payment gateway* (Midtrans)

### 4.2.6 Manajemen Risiko (*Risk*)

Identifikasi, analisis, dan strategi mitigasi risiko proyek:

**Tabel 4.5 Identifikasi dan Mitigasi Risiko**

| No | Risiko | Probabilitas | Dampak | Skor Risiko | Mitigasi | Owner |
|----|--------|-------------|--------|-------------|----------|-------|
| 1 | Keterlambatan jadwal | Sedang | Tinggi | 12 | Waktu penyangga 10%, prioritas fitur dengan MoSCoW, *daily standup* | PM |
| 2 | *Scope creep* (perubahan kebutuhan) | Sedang | Tinggi | 12 | Dokumentasi kebutuhan yang jelas, proses kontrol perubahan, persetujuan formal | PM |
| 3 | Bug kritis saat *deployment* | Rendah | Tinggi | 6 | Pengujian menyeluruh, *staging environment*, rencana *rollback* | Tim Dev |
| 4 | Anggota tim sakit/tidak tersedia | Rendah | Sedang | 4 | Berbagi pengetahuan, dokumentasi kode, *pair programming* | PM |
| 5 | Integrasi *payment gateway* gagal | Sedang | Sedang | 6 | *Prototyping* awal, dokumentasi API lengkap, pengujian *sandbox* | *Backend* Dev |
| 6 | Kehilangan data | Rendah | Tinggi | 6 | Cadangan otomatis harian, retensi 30 hari, rencana pemulihan bencana | DB Architect |
| 7 | Pelanggaran keamanan | Rendah | Sangat Tinggi | 8 | Audit keamanan, *penetration testing*, mengikuti pedoman *OWASP* | Tim Dev |
| 8 | Masalah kinerja | Sedang | Sedang | 6 | *Load testing*, *database indexing*, strategi *caching* | *Full-stack* Dev |

**Catatan Skor Risiko:**
- Probabilitas: Rendah (1), Sedang (2), Tinggi (3)
- Dampak: Rendah (2), Sedang (4), Tinggi (6), Sangat Tinggi (8)
- Skor Risiko = Probabilitas × Dampak

### 4.2.7 Perencanaan Komunikasi (*Communication*)

Strategi komunikasi untuk memastikan informasi mengalir dengan efektif kepada seluruh pemangku kepentingan proyek.

**Tabel 4.5 Matriks Perencanaan Komunikasi**

| No | Jenis Komunikasi | Pemangku Kepentingan | Frekuensi | Media | Durasi | Tujuan |
|----|------------------|---------------------|-----------|-------|--------|--------|
| **A. KOMUNIKASI INTERNAL TIM** |
| 1 | *Daily Standup* | Tim Proyek (3 orang) | Harian (Pagi) | WhatsApp Group | 15 menit | Update progress harian, identifikasi blocker |
| 2 | *Weekly Team Meeting* | Tim Proyek (3 orang) | Mingguan (Senin 19.00) | Google Meet | 1-2 jam | Review progress, demo fitur, planning minggu depan, risk review |
| 3 | *Code Review* | Developer | Setiap *Pull Request* | GitHub | Sesuai kebutuhan | Jaminan kualitas kode, knowledge sharing |
| **B. KOMUNIKASI PEMANGKU KEPENTINGAN** |
| 4 | Laporan Kemajuan | Dosen Pembimbing | Dua mingguan | Email + Pertemuan | 30-60 menit | Update progress, konsultasi masalah, approval milestone |
| 5 | Pertemuan Klien | Pemilik CUR-HEART | Dua mingguan | Google Meet / Tatap Muka | 1-2 jam | Validasi kebutuhan, demo progress, feedback |
| 6 | Sesi UAT | Pengguna CUR-HEART | 3 kali (Fase Testing) | Tatap Muka | 2-3 jam | Pengujian sistem, pengumpulan feedback |
| **C. DOKUMENTASI & KOLABORASI** |
| 7 | Dokumentasi Proyek | Tim & Stakeholder | Berkelanjutan | Google Drive | - | Repositori dokumen (laporan, SOP, manual) |
| 8 | Dokumentasi Teknis | Developer | Berkelanjutan | GitHub Wiki | - | Dokumentasi API, arsitektur, deployment |
| 9 | *Knowledge Base* | Tim Proyek | Berkelanjutan | Notion | - | Catatan meeting, keputusan, lessons learned |
| 10 | Kolaborasi Desain | Designer & Developer | Sesuai kebutuhan | Figma | - | Review dan approval desain UI/UX |

**Alat Komunikasi yang Digunakan:**
- **WhatsApp**: Komunikasi cepat dan koordinasi harian
- **Google Meet**: Pertemuan virtual dan presentasi
- **Email**: Komunikasi formal dan laporan resmi
- **GitHub**: Kolaborasi kode dan *code review*
- **Figma**: Kolaborasi desain UI/UX
- **Google Drive**: Penyimpanan dan berbagi dokumen
- **Notion**: Manajemen pengetahuan dan catatan

### 4.2.8 Perencanaan Pengadaan (*Procurement*)

Pengadaan barang dan jasa yang diperlukan:

**Tabel 4.6 Daftar Pengadaan**

| No | Item | Vendor | Biaya | Waktu | PIC |
|----|------|--------|-------|----------|-----|
| 1 | VPS Hosting | Niagahoster | Rp 1.200.000/tahun | Minggu 8 | Fahruroji |
| 2 | Domain .id | Niagahoster | Rp 150.000/tahun | Minggu 8 | Fahruroji |
| 3 | SSL Certificate | Let's Encrypt | Gratis | Minggu 8 | Fahruroji |
| 4 | Payment Gateway | Midtrans | Gratis (dev), 2,9% + Rp 2.000 (prod) | Minggu 6 | Roki |
| 5 | Email Service | Gmail SMTP / SendGrid | Gratis (limited) | Minggu 7 | Roki |

**Proses Pengadaan:**
1. Identifikasi kebutuhan
2. Pemilihan & perbandingan vendor
3. Persetujuan dari sponsor
4. *Purchase order*
5. Pengiriman & verifikasi
6. Pembayaran
7. Dokumentasi

### 4.2.9 Perencanaan Integrasi (*Integration*)

Integrasi sistem dengan layanan eksternal:

**A. Integrasi *Payment Gateway* (Midtrans):**
- **Metode**: *Snap API* untuk *checkout* yang mulus
- **Metode Pembayaran**: Kartu kredit/debit, Transfer bank, Dompet digital (GoPay, OVO, Dana)
- **Keamanan**: Memenuhi *PCI-DSS*, dukungan *3D Secure*
- **Webhook**: Untuk notifikasi pembayaran waktu nyata
- **Waktu**: Minggu 6-7 (implementasi + pengujian)

**B. Integrasi Layanan Email:**
- **Penyedia**: Gmail SMTP / SendGrid
- **Kasus Penggunaan**:
  - Email selamat datang saat registrasi
  - Email verifikasi
  - Konfirmasi reservasi
  - Notifikasi pembayaran
  - Pengingat sesi (H-1, H-0)
  - Reset kata sandi
- **Waktu**: Minggu 7-8

**C. Integrasi Masa Depan (Fase 2):**
- Notifikasi SMS via Twilio
- Penyimpanan cloud (Google Drive / AWS S3)
- Konferensi video (Zoom API)
- Analytics (Google Analytics)

### 4.2.10 Manajemen Pemangku Kepentingan (*Stakeholder*)

Identifikasi dan strategi keterlibatan pemangku kepentingan:

**Tabel 4.7 Daftar Pemangku Kepentingan**

| No | Pemangku Kepentingan | Peran | Kepentingan | Kekuasaan | Minat | Strategi |
|----|------------|-------|-------------|-------|----------|----------|
| 1 | Pemilik CUR-HEART | Sponsor & Pengambil Keputusan | Sangat Tinggi | Tinggi | Tinggi | Kelola Erat: Presentasi kemajuan bulanan, persetujuan kebutuhan |
| 2 | Terapis (3 orang) | Pengguna Akhir | Tinggi | Sedang | Tinggi | Tetap Berinformasi: Lokakarya kebutuhan, UAT, pelatihan |
| 3 | Admin (2 orang) | Pengguna Akhir | Tinggi | Sedang | Tinggi | Tetap Berinformasi: Lokakarya kebutuhan, UAT, pelatihan |
| 4 | Klien (8 orang sample) | Pengguna Akhir | Sedang | Rendah | Sedang | Pantau: Survei kebutuhan, pengujian kegunaan |
| 5 | Dosen Pembimbing | Penasihat Akademik | Sangat Tinggi | Tinggi | Tinggi | Kelola Erat: Konsultasi mingguan, tinjauan dokumen |
| 6 | Tim Pengembang | Tim Pengembangan | Sangat Tinggi | Tinggi | Tinggi | Kelola Erat: *Daily standup*, pertemuan mingguan |

**Strategi Keterlibatan:**
- **Kelola Erat**: Kekuasaan tinggi, minat tinggi - keterlibatan intensif dan pembaruan berkala
- **Tetap Berinformasi**: Kekuasaan rendah, minat tinggi - informasi berkala, masukan didengarkan
- **Jaga Kepuasan**: Kekuasaan tinggi, minat rendah - pembaruan penting, minta persetujuan
- **Pantau**: Kekuasaan rendah, minat rendah - komunikasi minimal, pemantauan

### 4.2.11 Batasan Proyek

Batasan-batasan proyek yang telah disepakati:

**A. Batasan Waktu:**
- Fokus proyek pada pembangunan sistem informasi dalam kurun waktu 16 minggu (4 bulan)
- Tidak membahas kontrol kualitas & jaminan kualitas secara khusus (hanya pengujian standar)
- Evaluasi jangka panjang (> 6 bulan) tidak termasuk dalam ruang lingkup

**B. Batasan Fitur:**
- Tidak membahas mengenai risiko proyek secara mendalam, fokus hanya pada risiko permintaan perubahan
- Modul analitik dan pelaporan dibatasi pada laporan standar (analitik lanjutan/*BI* ditunda ke fase 2)
- Integrasi dengan sistem eksternal lain (selain Midtrans dan email) tidak termasuk dalam fase 1

**C. Batasan Biaya:**
- Biaya yang dimaksud adalah biaya untuk tim proyek (tidak termasuk manajer proyek senior eksternal)
- Anggaran terbatas pada pengembangan dan 1 tahun operasional awal
- Biaya pelatihan intensif untuk semua staf tidak termasuk (hanya pelatihan dasar 2 jam)

**D. Batasan Teknis:**
- Sistem dioptimalkan untuk desktop dan tablet, dukungan mobile dalam bentuk *responsive design* (bukan aplikasi mobile *native*)
- Kapasitas sistem didesain untuk menangani hingga 50 pengguna bersamaan
- Bahasa sistem: Bahasa Indonesia (multi-bahasa tidak termasuk fase 1)
- Sistem tidak termasuk fitur panggilan video untuk sesi terapi daring

**E. Batasan Data:**
- Migrasi data historis dibatasi pada data 6 bulan terakhir
- Retensi cadangan data: 30 hari (untuk cadangan jangka panjang memerlukan biaya tambahan)

**F. Batasan Hukum:**
- Sistem mengikuti prinsip dasar UU Perlindungan Data Pribadi, namun sertifikasi kepatuhan formal tidak termasuk
- Penyangkalan medis: Sistem untuk manajemen administrasi, bukan untuk diagnosis medis

### 4.2.12 Asumsi Proyek

Asumsi-asumsi yang mendasari perencanaan proyek:

**A. Asumsi Pengadaan:**
- Pengadaan sudah tidak ada masalah, sumber daya non-personil tersedia sesuai spesifikasi
- VPS hosting dapat disewa sesuai spesifikasi yang dibutuhkan
- Domain dapat dibeli dan dikonfigurasi dengan lancar

**B. Asumsi Sumber Daya Manusia:**
- Sumber daya manusia sudah tersedia sesuai dengan spesifikasi proyek
- Anggota tim adalah SDM profesional (mahasiswa dengan kompetensi memadai)
- Tidak ada anggota tim yang mengundurkan diri atau sakit berkepanjangan selama proyek
- Terapis dan admin CUR-HEART bersedia meluangkan waktu untuk lokakarya, UAT, dan pelatihan

**C. Asumsi Teknis:**
- Manajer proyek adalah personil dari dalam tim (ketua tim mahasiswa)
- Infrastruktur teknologi (internet, listrik) stabil di lokasi pengembangan dan CUR-HEART
- API Midtrans berfungsi stabil dengan dokumentasi lengkap
- Layanan email SMTP dapat dikonfigurasi tanpa hambatan

**D. Asumsi Organisasi:**
- Struktur organisasi CUR-HEART sudah diterapkan dengan baik
- Pemilik & manajer proyek sudah ditunjuk beserta anggota tim
- Persetujuan dan pengambilan keputusan dari pemangku kepentingan dapat dilakukan tepat waktu
- Tidak ada perubahan manajemen atau struktur organisasi selama proyek

**E. Asumsi Proses Bisnis:**
- Proses bisnis CUR-HEART yang ada saat ini sudah terdokumentasi dengan baik
- Pemangku kepentingan dapat mengartikulasikan kebutuhan mereka dengan jelas
- Tidak ada perubahan signifikan pada proses bisnis selama pengembangan

**F. Asumsi Pengguna:**
- Klien CUR-HEART memiliki akses internet dan perangkat (smartphone/laptop/tablet)
- Pengguna memiliki kemampuan dasar menggunakan teknologi digital
- Klien bersedia mengadopsi sistem online untuk reservasi

**G. Asumsi Regulasi:**
- Tidak ada perubahan regulasi terkait data pribadi atau layanan kesehatan mental selama proyek
- Bisnis CUR-HEART memiliki izin operasional yang legal

---

## 4.3. DESKRIPSI PRODUK / SERVIS

Berikut ini adalah deskripsi umum (*high-level*) mengenai produk atau layanan yang dihasilkan dari proyek ini:

### 4.3.1 Tujuan Proyek

Tujuan proyek ini adalah membangun sistem informasi berbasis web yang dapat memberikan informasi yang berkaitan dengan manajemen reservasi dan terapi hipnoterapi CUR-HEART, mencakup:

- Informasi lengkap tentang layanan terapi yang ditawarkan
- Profil terapis dengan spesialisasi dan jadwal ketersediaan
- Sistem reservasi online yang mudah dan cepat
- Manajemen sesi terapi dan dokumentasi klien
- Pembayaran online yang aman dan terintegrasi
- Dasbor analitik untuk pengambilan keputusan

### 4.3.2 Pengguna Sistem

Sistem ini memiliki 3 tipe pengguna utama dengan hak akses berbeda. Sistem yang dibangun harus mampu:

**A. Untuk Klien:**
- Menampilkan informasi jumlah layanan, terapis, dan testimoni
- Menampilkan informasi layanan terbaru dan terapis unggulan
- Memberikan kemampuan reservasi layanan secara online 24/7
- Menampilkan riwayat reservasi dan sesi terapi
- Menyediakan sistem pembayaran yang aman dan mudah
- Menampilkan kemajuan terapi dan catatan sesi (yang dibagikan)

**B. Untuk Terapis:**
- Manajemen jadwal dan ketersediaan secara mandiri
- Melihat daftar klien dan detail reservasi hari ini
- Mendokumentasikan sesi terapi dengan formulir terstruktur
- Mengakses riwayat lengkap klien untuk kontinuitas perawatan
- Melihat dasbor pendapatan dan statistik kinerja
- Memperbarui profil dan pengaturan notifikasi

**C. Untuk Admin:**
- Pemantauan reservasi waktu nyata dengan pelacakan status
- Manajemen pengguna (klien, terapis, admin)in)
- Manajemen layanan (operasi CRUD)
- Laporan keuangan dan analitik:
  - Total reservasi dan pendapatan
  - Rincian per layanan dan terapis
  - Trend reservasi bulanan
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

**C. Modul Reservasi**
- Wizard reservasi 4 langkah:
  1. Pilih layanan terapi
  2. Pilih terapis (atau penugasan otomatis)
  3. Pilih tanggal & waktu
  4. Konfirmasi & pembayaran
- Pengecekan ketersediaan waktu nyatayata
- Tipe sesi: Daring/*Online*/Luring/*Offline*
- Dukungan kode promo
- Email konfirmasi reservasi

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
- Kartu statistik: Pengguna, reservasi, pendapatan, kesehatan sistem
- Grafik: Tren pendapatan, pertumbuhan pengguna, layanan teratasayanan teratas
- Manajemen pengguna (CRUD, menyetujui terapis)
- Manajemen reservasi (lihat, edit, batalkan, pengembalian dana)
- Manajemen layanan (CRUD)
- Laporan keuangan (ekspor Excel/PDF)
- Pengaturan sistem

**H. Modul Notifikasi**
- Notifikasi email:
  - Konfirmasi reservasi
  - Pembayaran berhasil
  - Pengingat sesi (H-1, H-0)
  - Notifikasi pembatalan
- Notifikasi dalam aplikasi
- Pengingat SMS (pengembangan mendatang)

**I. Modul Pelaporan**
- Laporan reservasi: Harian, mingguan, bulanan
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
7. **bookings** - Data reservasi
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
- Lihat: Semua izin tamu + dasbor, reservasi, kemajuan, pesan
- Aksi: Pesan layanan, lakukan pembayaran, jadwal ulang/batalkan, beri ulasan, obrolan

**C. Terapis**
- Lihat: Dasbor, jadwal, klien, sesi, pendapatan
- Aksi: Atur ketersediaan, dokumentasi sesi, lihat riwayat klien, obrolan, perbarui profil

**D. Administrator**
- Lihat: Semua data (pengguna, reservasi, pembayaran, laporan)
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
- Membuat reservasi layanan terapi
- Memilih terapis dan waktu sesi
- Melakukan pembayaran daring
- Melihat riwayat reservasi
- Melihat riwayat sesi terapi
- Perbarui profil
- Membatalkan/jadwal ulang reservasi (dengan syarat)

**Untuk Terapis:**
- Melihat jadwal sesi terapi hari ini dan minggu ini
- Melihat detail reservasi klien
- Mengatur ketersediaan jadwal
- Mendokumentasikan sesi terapi (catatan sesi)
- Melihat riwayat klien
- Memperbarui status sesi (selesai/dibatalkan)
- Melihat pendapatan

**Untuk Admin:**
- Mengelola data layanan terapi
- Mengelola data terapis
- Mengelola data klien
- Melihat semua reservasi
- Konfirmasi pembayaran manual (jika ada)
- Membuat laporan (reservasi, keuangan, kinerja)
- Pemantauan sistem

**Untuk *Payment Gateway*:**
- Memproses pembayaran
- Mengirim notifikasi status pembayaran
- Verifikasi transaksi

#### 4.3.9.2 Activity Diagram

Activity Diagram menggambarkan alur aktivitas dalam sistem untuk berbagai proses bisnis.

**a. Activity Diagram Proses Reservasi Terapi oleh Klien**

**[GAMBAR 4.4 - Activity Diagram Reservasi Terapi]**

Alur proses reservasi terapi:
1. Klien login ke sistem
2. Klien memilih layanan terapi yang diinginkan
3. Sistem menampilkan daftar terapis dan jadwal yang tersedia
4. Klien memilih terapis dan waktu sesi
5. Sistem memeriksa ketersediaan jadwal
   - Jika tidak tersedia: Tampilkan pesan kesalahan, kembali ke pemilihan jadwal
   - Jika tersedia: Lanjut ke langkah berikutnya
6. Klien mengisi informasi tambahan (keluhan, catatan)
7. Sistem menampilkan ringkasan reservasi dan total biaya
8. Klien konfirmasi reservasi
9. Sistem membuat catatan reservasi dengan status "Pending Payment"
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
3. Admin memilih jenis laporan (reservasi, keuangan, kinerja terapis, klien)
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
5. **therapist_services** - Relasi many-to-many antara terapis dan layanan
6. **therapist_availability** - Menyimpan jadwal ketersediaan terapis per hari
7. **therapist_unavailability** - Menyimpan data ketidaktersediaan terapis (cuti, sakit)
8. **promo_codes** - Menyimpan kode promo dan diskon
9. **bookings** - Menyimpan data reservasi terapi
10. **payments** - Menyimpan data pembayaran
11. **sessions** - Menyimpan data sesi terapi yang sudah dilaksanakan
12. **session_notes** - Menyimpan catatan dokumentasi sesi terapi
13. **reviews** - Menyimpan ulasan dari klien terhadap terapis/layanan
14. **blog_categories** - Menyimpan kategori artikel blog
15. **blog_posts** - Menyimpan artikel blog untuk edukasi kesehatan mental
16. **faq_categories** - Menyimpan kategori FAQ
17. **faqs** - Menyimpan pertanyaan dan jawaban FAQ
18. **messages** - Menyimpan pesan/chat antara klien dan terapis
19. **notifications** - Menyimpan notifikasi untuk pengguna
20. **withdrawals** - Menyimpan permintaan penarikan dana terapis
21. **activity_logs** - Menyimpan log aktivitas pengguna (jejak audit)
22. **system_settings** - Menyimpan konfigurasi sistem

**Relasi Utama:**

**Relasi Pengguna:**
- users (1) ↔ (1) clients: *One-to-One*
- users (1) ↔ (1) therapists: *One-to-One*
- users (1) ↔ (M) notifications: *One-to-Many*
- users (1) ↔ (M) messages (sender): *One-to-Many*
- users (1) ↔ (M) messages (receiver): *One-to-Many*
- users (1) ↔ (M) blog_posts (author): *One-to-Many*

**Relasi Terapis:**
- therapists (M) ↔ (M) services: *Many-to-Many* (melalui therapist_services)
- therapists (1) ↔ (M) therapist_availability: *One-to-Many*
- therapists (1) ↔ (M) therapist_unavailability: *One-to-Many*
- therapists (1) ↔ (M) bookings: *One-to-Many*
- therapists (1) ↔ (M) reviews: *One-to-Many*
- therapists (1) ↔ (M) withdrawals: *One-to-Many*

**Relasi Reservasi:**
- clients (1) ↔ (M) bookings: *One-to-Many*
- services (1) ↔ (M) bookings: *One-to-Many*
- promo_codes (1) ↔ (M) bookings: *One-to-Many*
- bookings (1) ↔ (1) payments: *One-to-One*
- bookings (1) ↔ (1) sessions: *One-to-One*
- bookings (1) ↔ (M) messages: *One-to-Many*
- bookings (1) ↔ (1) reviews: *One-to-One*

**Relasi Sesi:**
- sessions (1) ↔ (M) session_notes: *One-to-Many*

**Relasi Konten:**
- blog_categories (1) ↔ (M) blog_posts: *One-to-Many*
- faq_categories (1) ↔ (M) faqs: *One-to-Many*

**Keterangan:**
- (1) = One
- (M) = Many
- PK = Primary Key
- FK = Foreign Key

**Penjelasan Desain Database:**

1. **Normalisasi 3NF**: Database dinormalisasi hingga Third Normal Form (3NF) untuk menghindari redundansi data dan menjaga integritas data.

2. **Relasi Many-to-Many**: Tabel `therapist_services` digunakan sebagai junction table untuk relasi many-to-many antara terapis dan layanan, memungkinkan satu terapis menangani banyak layanan dan satu layanan ditangani banyak terapis.

3. **Soft Delete**: Beberapa tabel menggunakan status enum untuk "soft delete" (misalnya status 'archived' pada blog_posts) untuk menjaga integritas referensial.

4. **Audit Trail**: Tabel `activity_logs` mencatat semua aktivitas penting pengguna untuk keperluan audit dan keamanan.

5. **Content Management**: Tabel `blog_posts`, `blog_categories`, `faqs`, dan `faq_categories` mendukung fitur content management system untuk admin.

6. **Financial Management**: Tabel `payments` dan `withdrawals` mengelola aliran keuangan dari klien ke sistem dan dari sistem ke terapis.

7. **Communication**: Tabel `messages` dan `notifications` mendukung komunikasi real-time antara pengguna.

8. **Indexing**: Setiap tabel memiliki index yang tepat pada kolom yang sering di-query untuk optimasi performa.

Database dinormalisasi hingga Third Normal Form (3NF) untuk menghindari redundansi data dan menjaga integritas data.

#### 4.3.9.4 Desain Antarmuka Pengguna (UI/UX)

Desain antarmuka pengguna (UI) dibuat menggunakan Figma dengan total 66 halaman mockup yang mencakup semua peran pengguna. Desain mengikuti prinsip *user-centered design* dengan fokus pada kemudahan penggunaan, aksesibilitas, dan pengalaman pengguna yang optimal.

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

Sistem memiliki **66 halaman mockup** yang terbagi dalam beberapa kategori:

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

**3. Dashboard Klien (12 halaman):**

**[GAMBAR 4.25 - Mockup Dasbor Klien - Dasbor Utama]**
- **Dasbor Utama**: Sambutan, statistik cepat, janji temu berikutnya, sesi mendatang, ikhtisar kemajuan

**[GAMBAR 4.26 - Mockup Reservasi Langkah 1 - Pilih Layanan]**
- **Reservasi Langkah 1**: Pemilihan layanan dengan kartu layanan

**[GAMBAR 4.27 - Mockup Reservasi Langkah 2 - Pilih Terapis]**
- **Reservasi Langkah 2**: Pilih terapis dengan profil dan rating

**[GAMBAR 4.28 - Mockup Reservasi Langkah 3 - Pilih Jadwal]**
- **Reservasi Langkah 3**: Pemilih tanggal & waktu dengan ketersediaan waktu nyata

**[GAMBAR 4.29 - Mockup Reservasi Langkah 4 - Konfirmasi & Pembayaran]**
- **Reservasi Langkah 4**: Konfirmasi & pembayaran dengan ringkasan reservasi

**[GAMBAR 4.30 - Mockup Reservasi Berhasil]**
- **Reservasi Berhasil**: Selamat, detail reservasi, langkah selanjutnya, tombol aksi

**[GAMBAR 4.31 - Mockup Janji Temu Saya]**
- **Janji Temu Saya**: Tab (mendatang/lampau/dibatalkan), filter & urutkan, kartu janji temu

**[GAMBAR 4.32 - Mockup Detail Janji Temu]**
- **Detail Janji Temu**: Info reservasi, info pembayaran, catatan sesi, aksi jadwal ulang/batalkan

**[GAMBAR 4.33 - Mockup Dasbor Kemajuan]**
- **Dasbor Kemajuan**: Skor kesehatan, kehadiran sesi, tujuan & pencapaian, pelacakan suasana hati

**[GAMBAR 4.34 - Mockup Pesan (Obrolan)]**
- **Pesan (Obrolan)**: Daftar percakapan, area obrolan aktif, indikator mengetik

**[GAMBAR 4.35 - Mockup Pengaturan Klien]**
- **Pengaturan Klien**: Profil, keamanan, notifikasi, privasi

**[GAMBAR 4.36 - Mockup Notifikasi Klien]**
- **Notifikasi Klien**: Daftar notifikasi, filter, tandai sebagai dibaca

**4. Dashboard Terapis (13 halaman):**

**[GAMBAR 4.37 - Mockup Dasbor Terapis - Dasbor Utama]**
- **Dasbor Utama**: Sesi hari ini, metrik kunci, ikhtisar pendapatan, ulasan klien

**[GAMBAR 4.38 - Mockup Manajemen Jadwal]**
- **Manajemen Jadwal**: Tampilan kalender (hari/minggu/bulan), blok janji temu, waktu libur

**[GAMBAR 4.39 - Mockup Pengaturan Ketersediaan]**
- **Pengaturan Ketersediaan**: Jam kerja per hari, durasi sesi, jendela reservasi, tanggal khusus

**[GAMBAR 4.40 - Mockup Daftar Klien]**
- **Daftar Klien**: Cari & filter, kartu klien dengan statistik, aksi massal

**[GAMBAR 4.41 - Mockup Tampilan Profil Klien]**
- **Tampilan Profil Klien**: Ikhtisar, riwayat sesi, catatan & observasi, kemajuan & tujuan, berkas

**[GAMBAR 4.42 - Mockup Ruang Sesi]**
- **Ruang Sesi**: Konferensi video dengan timer, bilah kontrol, panel catatan

**[GAMBAR 4.43 - Mockup Formulir Catatan Sesi]**
- **Formulir Catatan Sesi**: Penilaian, ringkasan sesi, catatan kemajuan, tugas rumah, templat

**[GAMBAR 4.44 - Mockup Riwayat Sesi]**
- **Riwayat Sesi**: Total sesi, cari & filter, tabel sesi, analitik

**[GAMBAR 4.45 - Mockup Dasbor Pendapatan]**
- **Dasbor Pendapatan**: Saldo, grafik pendapatan, transaksi, penarikan, pengaturan pembayaran

**[GAMBAR 4.46 - Mockup Edit Profil Terapis]**
- **Edit Profil**: Tab untuk dasar/profesional/tentang/pendidikan/layanan/media/pengaturan

**[GAMBAR 4.47 - Mockup Pengaturan Terapis]**
- **Pengaturan Terapis**: Preferensi akun, keamanan, notifikasi

**[GAMBAR 4.48 - Mockup Pesan Terapis]**
- **Pesan Terapis**: Daftar percakapan dengan klien, area obrolan

**[GAMBAR 4.49 - Mockup Notifikasi Terapis]**
- **Notifikasi Terapis**: Daftar notifikasi sistem, filter, tandai sebagai dibaca

**5. Dashboard Admin (25 halaman):**

**[GAMBAR 4.50 - Mockup Dasbor Admin - Dasbor Utama]**
- **Dasbor Utama**: Metrik kunci, grafik pendapatan, reservasi terbaru, pertumbuhan pengguna, peringatan sistem

**[GAMBAR 4.46 - Mockup Manajemen Reservasi]**
- **Manajemen Reservasi**: Ringkasan statistik, tab (semua/mendatang/lampau/tertunda/dibatalkan/sengketa), tabel reservasi

**[GAMBAR 4.47 - Mockup Manajemen Pengguna]**
- **Manajemen Pengguna**: Tab (semua/klien/terapis/admin/tertunda), tabel pengguna, aksi massal

**[GAMBAR 4.48 - Mockup Laporan Keuangan]**
- **Laporan Keuangan**: Ringkasan pendapatan, grafik, tabel transaksi, penarikan, pengembalian dana, analitik

**[GAMBAR 4.49 - Mockup Pengaturan Sistem]**
- **Pengaturan Sistem**: Navigasi kategori, umum/reservasi/pembayaran/email/keamanan/kebijakan/integrasi/lanjutan

**[GAMBAR 4.50 - Mockup Notifikasi Admin]**
- **Notifikasi Admin**: Daftar notifikasi sistem, filter berdasarkan tipe, tandai sebagai dibaca

**[GAMBAR 4.51 - Mockup Pesan Admin]**
- **Pesan Admin**: Daftar percakapan dengan pengguna, area obrolan, dukungan pelanggan

**[GAMBAR 4.52 - Mockup Detail Pengguna]**
- **Detail Pengguna**: Profil lengkap, riwayat aktivitas, statistik, aksi moderasi

**[GAMBAR 4.53 - Mockup Edit Pengguna]**
- **Edit Pengguna**: Formulir edit data pengguna, ubah peran, status akun

**[GAMBAR 4.54 - Mockup Detail Reservasi]**
- **Detail Reservasi**: Informasi lengkap reservasi, timeline status, aksi admin

**[GAMBAR 4.55 - Mockup Manajemen Transaksi]**
- **Manajemen Transaksi**: Daftar semua transaksi pembayaran, filter, ekspor laporan

**[GAMBAR 4.56 - Mockup Manajemen Penarikan]**
- **Manajemen Penarikan**: Permintaan penarikan dana terapis, approval, riwayat

**[GAMBAR 4.57 - Mockup Detail Penarikan]**
- **Detail Penarikan**: Informasi penarikan, verifikasi, bukti transfer

**[GAMBAR 4.58 - Mockup Log Aktivitas]**
- **Log Aktivitas**: Jejak audit sistem, filter berdasarkan pengguna/aksi/tanggal

**[GAMBAR 4.59 - Mockup Laporan & Analitik]**
- **Laporan & Analitik**: Dashboard analitik lanjutan, berbagai jenis laporan, ekspor

**[GAMBAR 4.60 - Mockup Manajemen Ulasan]**
- **Manajemen Ulasan**: Daftar ulasan klien, moderasi, tanggapan, filter rating

**[GAMBAR 4.61 - Mockup Manajemen Promo]**
- **Manajemen Promo**: Daftar kode promo, buat/edit/hapus, statistik penggunaan

**[GAMBAR 4.62 - Mockup Verifikasi Terapis]**
- **Verifikasi Terapis**: Daftar pendaftaran terapis baru, review dokumen, approval/reject

**[GAMBAR 4.63 - Mockup Editor Blog]**
- **Editor Blog**: Rich text editor untuk membuat/edit artikel blog, kategori, tag, SEO

**[GAMBAR 4.64 - Mockup Manajemen Konten Blog]**
- **Manajemen Konten Blog**: Daftar artikel, status (draft/published), aksi CRUD

**[GAMBAR 4.65 - Mockup Editor FAQ]**
- **Editor FAQ**: Formulir untuk membuat/edit pertanyaan dan jawaban FAQ, kategori

**[GAMBAR 4.66 - Mockup Manajemen Konten FAQ]**
- **Manajemen Konten FAQ**: Daftar FAQ, kategori, urutan tampilan, aksi CRUD

**[GAMBAR 4.67 - Mockup Editor Layanan]**
- **Editor Layanan**: Formulir lengkap untuk membuat/edit layanan terapi, harga, durasi

**[GAMBAR 4.68 - Mockup Manajemen Konten Layanan]**
- **Manajemen Konten Layanan**: Daftar layanan, status aktif/nonaktif, aksi CRUD

**[GAMBAR 4.69 - Mockup Editor Promo]**
- **Editor Promo**: Formulir untuk membuat/edit promosi, banner, periode aktif, target

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

Total **66 halaman mockup** yang mencakup seluruh perjalanan pengguna dari 4 peran berbeda (Tamu, Klien, Terapis, Admin). Rincian distribusi halaman:

- **Halaman Publik**: 12 halaman (landing, layanan, terapis, blog, kontak, FAQ, dll)
- **Halaman Autentikasi**: 4 halaman (login, register, lupa password, reset password)
- **Dashboard Klien**: 12 halaman (dashboard, booking flow 4 steps, appointments, progress, messages, settings, notifications)
- **Dashboard Terapis**: 13 halaman (dashboard, schedule, availability, clients, session room, notes, history, earnings, profile edit, settings, messages, notifications)
- **Dashboard Admin**: 25 halaman (dashboard, users, bookings, financial, content management, reviews, verification, reports)

Semua mockup dirancang dengan prinsip:

**Responsif**: Adaptif untuk desktop, tablet, dan mobile  
**Aksesibilitas**: Memenuhi standar *WCAG 2.1 AA*  
**Konsistensi**: Mengikuti sistem desain yang telah ditetapkan  
**Ramah Pengguna**: Intuitif dan mudah digunakan  
**Profesional**: Mencerminkan kredibilitas layanan kesehatan mental

Desain telah melalui beberapa iterasi berdasarkan umpan balik dari pemangku kepentingan dan *usability testing* dengan sampel pengguna.

---

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
- Minimal 70% klien menggunakan sistem untuk reservasi
- Skor kepuasan pengguna ≥ 4,0 dari 5,0
- Skor SUS (*System Usability Scale*) ≥ 68
- Tingkat adopsi terapis 100%

**CSF 4: Integrasi dengan Proses Bisnis**
- 100% reservasi melalui sistem (tidak ada lagi manual)
- Pengurangan beban kerja administratif minimal 50%
- Pengurangan kesalahan reservasi hingga 90%
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
| | Tingkat Konversi Reservasi (*Conversion Rate*) | ≥ 60% | Mingguan |
| **Transaksi** | Total Reservasi/Bulan | 100 reservasi | Bulanan |
| | Tingkat Keberhasilan Pembayaran (*Payment Success Rate*) | ≥ 95% | Mingguan |
| | Pendapatan/Bulan | Rp 30 juta | Bulanan |
| **Kepuasan** | Skor Kepuasan Pengguna | ≥ 4,0/5,0 | Per reservasi |
| | Skor NPS (*Net Promoter Score*) | ≥ 30 | Triwulanan |
| | Skor SUS (*System Usability Scale*) | ≥ 68 | Triwulanan |
| **Efisiensi** | Rata-rata Waktu Reservasi | ≤ 3 menit | Mingguan |
| | Pengurangan Beban Kerja Admin | ≥ 50% | Bulanan |
| | Waktu Pembuatan Laporan | ≤ 5 menit | Bulanan |

---

## 4.5. KEUNTUNGAN YANG DIHARAPKAN

Implementasi Sistem Informasi CUR-HEART diharapkan memberikan berbagai keuntungan bagi pemangku kepentingan yang terlibat.

### 4.5.1 Manfaat untuk CUR-HEART (Organisasi)

**A. Efisiensi Operasional**

- **Proses reservasi otomatis**: Pengurangan waktu dari 10-15 menit menjadi 3 menit per reservasi, penghematan sekitar 20 jam per bulan
- **Manajemen penjadwalan**: Koordinasi jadwal berkurang dari 5 jam per minggu menjadi 1 jam, utilisasi meningkat dari 60% menjadi 80%
- **Pelaporan otomatis**: Waktu pembuatan laporan dari 2 jam menjadi 5 menit, penghematan 8 jam per bulan
- **Eliminasi reservasi ganda**: Konflik jadwal turun dari 8-10 kasus per bulan menjadi 0 kasus

**B. Pertumbuhan Pendapatan**

- **Peningkatan volume reservasi**: Target +25% dari 80 menjadi 100 reservasi per bulan (Rp 72 juta/tahun tambahan)
- **Pengurangan tidak hadir**: Dari 15% menjadi 5% dengan pengingat otomatis (Rp 28,8 juta/tahun pendapatan dipulihkan)
- **Perpanjangan jam layanan**: Reservasi 24/7 menangkap 15% lebih banyak klien (Rp 10 juta/tahun)
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

- Reservasi 24/7 kapan saja tanpa terbatas jam kantor
- Tidak perlu telepon, layanan mandiri daring
- Ramah perangkat seluler untuk reservasi saat bepergian
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
- Penghematan waktu: 25-55 menit per reservasi
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
  - Email notifikasi (konfirmasi reservasi, pengingat)
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
- 66 halaman *mockup* untuk semua peran pengguna
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


## 4.7. DESIMINASI PROYEK

Desiminasi proyek merupakan proses penyebarluasan hasil, pengetahuan, dan pembelajaran dari proyek pengembangan Sistem Informasi CUR-HEART kepada berbagai pihak yang berkepentingan. Tujuan desiminasi adalah untuk memaksimalkan manfaat proyek, berbagi pengetahuan, dan memungkinkan replikasi sistem di tempat lain.

### 4.7.1 Tujuan Desiminasi

**A. Berbagi Pengetahuan**
- Berbagi pengetahuan dan praktik terbaik dalam pengembangan sistem informasi kesehatan mental
- Memberikan pembelajaran tentang implementasi Laravel untuk manajemen layanan kesehatan (*healthcare management*)
- Dokumentasi proses dan tantangan yang dihadapi selama pengembangan

**B. Peningkatan Kesadaran**
- Meningkatkan kesadaran tentang pentingnya digitalisasi layanan kesehatan mental
- Menunjukkan manfaat sistem informasi untuk efisiensi operasional
- Mempromosikan adopsi teknologi di sektor kesehatan mental

**C. Replikasi dan Skalabilitas**
- Memungkinkan pusat terapi lain untuk mengadopsi sistem serupa
- Menyediakan dokumentasi lengkap untuk implementasi
- Berbagi pembelajaran yang diperoleh untuk menghindari kesalahan yang sama

### 4.7.2 Target Audiens Desiminasi

**A. Pemangku Kepentingan Internal**
- Tim manajemen CUR-HEART
- Terapis dan staf administratif
- Pemilik bisnis

**B. Akademik**
- Dosen pembimbing dan penguji
- Mahasiswa Program Studi Sistem Informasi
- Sivitas akademika Universitas Nusa Mandiri

**C. Eksternal**
- Praktisi hipnoterapi dan kesehatan mental
- Pusat terapi dan *wellness center* lainnya
- Komunitas pengembang (*developer*) Laravel Indonesia
- Pihak yang tertarik dengan sistem informasi kesehatan (*health information system*)

### 4.7.3 Metode Desiminasi

**A. Publikasi Akademik**

**1. Laporan *Capstone Project***
- Laporan lengkap BAB I - BAB V
- Dokumentasi teknis (SRS, Dokumen Desain/*Design Document*)
- Panduan pengguna dan panduan admin
- Kode sumber dengan dokumentasi lengkap
- Format: PDF dan Salinan Cetak

**2. Presentasi Akademik**
- Presentasi akhir di hadapan dosen pembimbing dan penguji
- Slide presentasi dengan demonstrasi sistem langsung
- Sesi tanya jawab untuk diskusi mendalam
- Durasi: 30-45 menit

**B. Dokumentasi dan Repositori**

**1. Repositori GitHub**
- Kode sumber lengkap dengan README.md komprehensif
- Panduan instalasi bertahap
- Dokumentasi API
- Dokumentasi skema basis data
- Panduan kontribusi
- Lisensi: MIT (sumber terbuka/*open source*)

**2. Dokumentasi Teknis**
- Diagram arsitektur sistem
- ERD basis data dengan penjelasan
- Dokumentasi titik akhir (*endpoint*) API
- Panduan penerapan (*deployment*)
- Panduan pemecahan masalah (*troubleshooting*)
- Format: Markdown + PDF

**C. Pameran Ilmiah (*Science Exhibition*)**

**1. Persiapan Materi dan Konten Pameran**

- **Penyusunan Materi Pameran**: Siapkan konten visual dan materi lain yang diperlukan untuk menjelaskan hasil proyek secara menarik. Materi ini dapat berupa poster, infografis, video, atau simulasi interaktif.

- **Prototipe atau Produk Jadi**: Jika proyek menghasilkan produk fisik, sistem, atau aplikasi, pastikan prototipe tersebut siap dipamerkan dan dapat berfungsi dengan baik.

- **X-Banner dan Desain *Stand***: Rancang *stand* pameran yang menarik, termasuk x-banner dengan ukuran 60 X 160 cm yang berisi elemen grafis berikut:
  - Judul *Project*
  - Logo Universitas Nusa Mandiri
  - Logo Kampus Digital Bisnis
  - Nama kelompok dan dosen pengampu mata kuliah
  - Latar belakang project
  - Tujuan
  - Metodologi
  - Hasil utama
  - Keunggulan proyek
  - Manfaat proyek
  - QR (*barcode* kuesioner penilaian persepsi masyarakat)
  - Gambar visualisasi pendukung
  - Link *youtube video* promosi hasil proyek

- **Alat Peraga Interaktif**: Siapkan alat peraga interaktif seperti perangkat lunak yang dapat dicoba pengunjung, model fisik, atau demo langsung dari hasil proyek untuk menarik minat audiens.

**2. Pelaksanaan Pameran (*Exhibition*)**

- **Presentasi dan Demonstrasi**: Pada hari pameran, siapkan tim untuk memberikan presentasi singkat atau menjelaskan langsung kepada pengunjung mengenai proyek. Demonstrasi atau sesi tanya jawab interaktif dengan pengunjung sangat penting untuk menjelaskan manfaat dan keunggulan proyek.

- **Brosur dan Materi Pendukung**: Sediakan materi cetak seperti brosur atau katalog yang bisa dibawa pulang oleh pengunjung sebagai panduan dan informasi lebih lanjut mengenai proyek.

**3. Interaksi dengan Pengunjung (*Visitor Engagement*)**

- **Umpan Balik Pengunjung**: Sediakan mekanisme bagi pengunjung untuk memberikan umpan balik, baik melalui kuesioner, buku tamu, atau secara digital melalui aplikasi. Umpan balik ini bisa sangat berguna untuk evaluasi dan pengembangan lebih lanjut.

**4. Dokumentasi**

- **Fotografi dan Videografi**: Rekam momen penting selama pameran, seperti interaksi dengan pengunjung, presentasi, dan demonstrasi proyek. Dokumentasi ini bisa digunakan untuk promosi lebih lanjut atau laporan kepada pemangku kepentingan.

**D. Publikasi Video Promosi/Campaign**

**1. Video Promosi**
- Durasi: 3-5 menit untuk diunggah di YouTube
- Durasi pendek: 1 menit maksimal untuk media sosial
- Resolusi minimal: 1080 Pixel
- Konten: Visual, musik, *voice over*, teks, subtitle
- Format: mp4 atau format video umum untuk media sosial

**2. Isi Konten Video Promosi**
- Pembukaan dengan logo Universitas Nusa Mandiri
- Logo Kampus Digital Bisnis
- Nama kelompok dan dosen pengampu mata kuliah
- Latar belakang project
- Tujuan
- Solusi yang ditawarkan
- Keunggulan dan inovasi
- Manfaat
- Dampak proyek
- Simulasi prototipe dan penutup

**E. Pelatihan Internal**

Pelatihan untuk pemangku kepentingan CUR-HEART:
- Pelatihan pengguna untuk terapis (2 jam)
- Pelatihan admin (2 jam)
- Ikhtisar manajemen (1 jam)
- Materi: Slide + praktik langsung
- Dokumentasi video pelatihan

**F. Media Daring**

**1. Artikel Blog**
- Medium.com atau Dev.to
- Topik: 
  - "Membangun Sistem Manajemen Kesehatan dengan Laravel 10"
  - "Mengintegrasikan *Payment Gateway* Midtrans di Laravel"
  - "Desain UI/UX untuk Layanan Kesehatan Mental"
- Format: Tutorial bertahap dengan cuplikan kode (*code snippets*)

**2. Media Sosial**
- Posting LinkedIn tentang penyelesaian proyek
- Utas (*thread*) Twitter tentang pembelajaran kunci
- Infografis Instagram tentang hasil proyek

### 4.7.4 Luaran Desiminasi

**Tabel 4.10 - Luaran Desiminasi Proyek**

| No | Luaran | Format | Target Audiens | Waktu | Status |
|----|-------------|--------|----------------|----------|--------|
| 1 | Laporan *Capstone Project* | PDF + Salinan Cetak | Akademik | Desember 2024 | Selesai |
| 2 | X-Banner dan Desain *Stand* Pameran | Cetak 60x160 cm | Publik | Desember 2024 | Selesai |
| 3 | Video Promosi/*Campaign* | MP4 (3-5 menit + 1 menit) | Publik | Desember 2024 | Selesai |
| 4 | Pameran Ilmiah | *Stand* Interaktif + Demo | Sivitas Akademika + Publik | Desember 2024 | Terjadwal |
| 5 | Presentasi Akhir | *Slide* + Demonstrasi | Dosen Pembimbing/Penguji | Desember 2024 | Terjadwal |
| 6 | Penilaian Persepsi Masyarakat | Kuesioner *Google Form* | Publik | Desember 2024 | Siap |
| 7 | Repositori Kode Sumber | GitHub | Publik | Desember 2024 | Siap |
| 8 | Dokumentasi Teknis | Markdown + PDF | Pengembang | Desember 2024 | Selesai |
| 9 | Panduan Pengguna | PDF | Pengguna Akhir | Desember 2024 | Selesai |
| 10 | Materi Pelatihan | *Slide* + Video | Staf CUR-HEART | Januari 2025 | Direncanakan |
| 11 | Artikel Blog | Medium/Dev.to | Komunitas Pengembang | Januari 2025 | Direncanakan |

### 4.7.5 Jadwal dan Rencana Pelaksanaan Desiminasi

**A. Pelaksanaan Desiminasi Akademik (Pertemuan 13-16)**

Sesuai dengan pedoman *Capstone Project*, pelaksanaan desiminasi dilakukan pada **Pertemuan 13-16**:

- **Pertemuan 13**: Promosi Hasil *Capstone Project* (YouTube / Media Sosial) dan Penilaian Persepsi masyarakat melalui kuesioner *Google Form*
  
- **Pertemuan 14**: Pelaksanaan Pameran Ilmiah
  - Persiapan *stand* pameran dengan X-Banner (60 x 160 cm)
  - Penyiapan alat peraga interaktif (demo sistem CUR-HEART)
  - Penyediaan brosur dan materi pendukung
  - Presentasi dan demonstrasi kepada pengunjung
  - Pengumpulan umpan balik melalui kuesioner
  - Dokumentasi foto dan video
  
- **Pertemuan 15**: Presentasi di hadapan Dosen Pengampu Mata Kuliah/Dosen Pembimbing
  - Presentasi hasil proyek secara keseluruhan
  - Demonstrasi sistem yang telah dikembangkan
  - Sesi tanya jawab
  - Penilaian oleh dosen
  
- **Pertemuan 16**: Penilaian Akhir oleh Dosen Pengampu Mata Kuliah/Dosen Pembimbing

**B. Kegiatan Pendukung**

- **Januari 2025**: Pelatihan internal untuk staf CUR-HEART dan publikasi artikel blog di Medium/Dev.to

### 4.7.6 Indikator Keberhasilan Desiminasi

**A. Jangkauan (*Reach*)**
- Pengunjung pameran ilmiah: Minimal 50 pengunjung
- Tampilan video promosi YouTube: Target 100+ tampilan dalam 1 bulan
- Responden kuesioner persepsi masyarakat: Minimal 30 responden
- Bintang repositori GitHub: Target 50+ bintang dalam 6 bulan
- Tampilan artikel blog: Target 500+ tampilan

**B. Keterlibatan (*Engagement*)**
- Skor penilaian persepsi masyarakat: ≥ 4,0/5,0
- Interaksi pengunjung di *stand* pameran: Minimal 30 interaksi bermakna
- Isu/diskusi (*issues/discussions*) GitHub: Keterlibatan komunitas aktif
- Komentar blog dan keterlibatan media sosial
- Skor umpan balik pelatihan: ≥ 4,0/5,0
- Partisipasi (*participation*) tanya jawab di presentasi

**C. Dampak (*Impact*)**
- Penilaian dosen: Minimal nilai B untuk presentasi
- Transfer pengetahuan: Staf CUR-HEART dapat mengoperasikan sistem secara mandiri

**D. Kualitas Luaran**
- Kelengkapan dokumentasi: 100% sesuai pedoman
- Kualitas X-Banner: Memenuhi semua elemen yang dipersyaratkan
- Kualitas video promosi: Memenuhi spesifikasi teknis (1080p, durasi sesuai)
- Kelengkapan materi pameran: Semua komponen tersedia dan fungsional

### 4.7.7 Pembelajaran yang Diperoleh dan Praktik Terbaik

**A. Pembelajaran Teknis**
- Laravel 10 sangat cocok untuk sistem manajemen kesehatan
- Integrasi Midtrans mudah dengan dokumentasi yang baik
- Tailwind CSS secara signifikan mempercepat pengembangan *frontend*
- Figma esensial untuk penyelarasan dengan pemangku kepentingan

**B. Pembelajaran Manajemen Proyek**
- Komunikasi yang sering dengan pemangku kepentingan sangat penting untuk kesuksesan
- Pengembangan iteratif lebih efektif daripada model air terjun (*waterfall*)
- UAT harus dilakukan sejak awal untuk menghindari revisi besar
- Dokumentasi secara bertahap lebih efisien daripada di akhir

**C. Pembelajaran Spesifik Domain**
- Data kesehatan mental memerlukan langkah keamanan ekstra
- Kompleksitas penjadwalan janji temu jangan diremehkan
- Orientasi pengguna (*onboarding*) sangat penting untuk kesuksesan adopsi
- Desain responsif wajib untuk aplikasi kesehatan

**D. Praktik Terbaik untuk Replikasi**
- Mulai dengan pengumpulan kebutuhan yang komprehensif
- Libatkan pengguna akhir sejak fase desain
- Prioritaskan keamanan dan privasi dari awal
- Rencanakan skalabilitas meski mulai kecil
- Anggarkan untuk pemeliharaan dan dukungan pasca-peluncuran

---

**[AKHIR BAB IV]**

