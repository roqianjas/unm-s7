# BAB IV  
# HASIL PENELITIAN DAN PEMBAHASAN

## 4.1. INISIASI PROYEK

Proyek pengembangan Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART diinisiasi berdasarkan kebutuhan untuk mengoptimalkan operasional pusat layanan hipnoterapi dan kesehatan mental. CUR-HEART (*Hypnotherapy & Mind Wellness Center*) mengalami pertumbuhan signifikan dalam jumlah klien dan terapis, namun sistem manual yang digunakan menghambat efisiensi dan kualitas layanan.

### 4.1.1 Latar Belakang Masalah

Berdasarkan observasi dan wawancara yang dilakukan pada September 2024, teridentifikasi beberapa permasalahan utama:

1. **Proses pemesanan manual** melalui WhatsApp dan telepon yang memakan waktu lama dan mengurangi tingkat konversi (hanya 60% dari pertanyaan menjadi pemesanan aktual)

2. **Konflik jadwal dan pemesanan ganda** terjadi 8-10 kasus per bulan karena manajemen jadwal menggunakan spreadsheet terpisah

3. **Dokumentasi terapi tidak terstruktur** dimana terapis menghabiskan 15 menit per sesi untuk pencatatan manual dengan risiko data hilang

4. **Tidak ada data untuk pengambilan keputusan** karena informasi tersebar di berbagai platform dan pembuatan laporan memakan waktu 2-3 hari

5. **Beban administratif tinggi** dengan admin menghabiskan 70% waktu untuk tugas repetitif seperti menjawab pertanyaan yang sama dan verifikasi pembayaran manual

6. **Risiko keamanan dan privasi data** klien yang sensitif disimpan dalam format tidak aman tanpa kontrol akses yang tepat

### 4.1.2 Identifikasi Masalah

Berdasarkan latar belakang di atas, penulis mengidentifikasikan beberapa masalah sebagai berikut:

a. Pelayanan pemesanan terapi masih dilaksanakan secara konvensional sehingga kurang efektif dan efisien

b. Belum adanya sistem informasi pemesanan berbasis web untuk pemesanan dan manajemen terapi

c. Banyak terjadi kehilangan data klien karena belum adanya sistem informasi yang dapat mendata siapa saja klien yang sedang melakukan pemesanan dan mengikuti sesi terapi

### 4.1.3 Ruang Lingkup

Ruang lingkup proyek ini mencakup pengembangan sistem informasi berbasis web dengan fitur-fitur utama:

- **Modul Pemesanan Online**: Klien dapat melihat jadwal terapis, memilih layanan, dan melakukan pemesanan secara mandiri 24/7
- **Manajemen Jadwal Terapis**: Sistem penjadwalan otomatis dengan deteksi konflik dan notifikasi
- **Dokumentasi Sesi Terapi**: Platform digital untuk terapis mencatat dan mengakses riwayat terapi klien
- **Pembayaran Terintegrasi**: Integrasi dengan payment gateway Midtrans untuk pembayaran online
- **Dashboard Admin**: Panel kontrol untuk monitoring pemesanan, terapis, dan laporan keuangan
- **Notifikasi Otomatis**: Email reminder untuk klien dan terapis tentang jadwal sesi

### 4.1.4 Tujuan dan Manfaat Penelitian

**Tujuan penelitian dalam capstone project ini adalah:**

a. Agar pelayanan pemesanan terapi dapat berjalan dengan efektif dan efisien

b. Sistem informasi pemesanan diharapkan dapat memudahkan klien dalam melakukan pemesanan dan melihat riwayat terapi

c. Dengan adanya sistem informasi dapat memudahkan baik klien, petugas admin, maupun terapis dalam pengelolaan data pemesanan dan sesi terapi, sehingga semuanya dapat terkontrol dengan baik

d. Sebagai salah satu syarat kelulusan pada Program Studi Strata Satu (S1) untuk Program Studi Sistem Informasi di Fakultas Teknologi Informasi Universitas Nusa Mandiri

**Manfaat penelitian:**

Penelitian ini diharapkan memberikan manfaat bagi berbagai pihak:

- **Bagi CUR-HEART**: Meningkatkan efisiensi operasional, mengurangi kesalahan jadwal, dan mempercepat pertumbuhan bisnis
- **Bagi Klien**: Kemudahan dalam pemesanan layanan terapi kapan saja tanpa harus menghubungi admin
- **Bagi Terapis**: Mengurangi beban administratif dan memudahkan akses riwayat klien
- **Bagi Admin**: Otomasi tugas repetitif sehingga dapat fokus pada layanan pelanggan yang lebih berkualitas
- **Bagi Akademik**: Sebagai referensi pengembangan sistem informasi sejenis untuk layanan kesehatan mental

---

## 4.2. PERENCANAAN PROYEK

Perencanaan proyek dilakukan untuk memastikan proyek berjalan sesuai target waktu, biaya, dan kualitas yang ditetapkan. Perencanaan mencakup berbagai area pengetahuan manajemen proyek yang telah diidentifikasi mencakup ruang lingkup (*scope*), waktu (*time*), biaya (*cost*), kualitas (*quality*), sumber daya (*resource*), risiko (*risk*), komunikasi (*communication*), pengadaan (*procurement*), integrasi (*integration*), serta manajemen pemangku kepentingan (*stakeholder*).

### 4.2.1 Perencanaan Ruang Lingkup (*Scope*)

Ruang lingkup proyek didefinisikan menggunakan Work Breakdown Structure (WBS) yang membagi pekerjaan menjadi komponen-komponen yang dapat dikelola. WBS proyek ini mencakup 6 fase utama dengan total lebih dari 40 work packages yang terdistribusi ke dalam aktivitas-aktivitas terstruktur.

**Tabel 4.1 Work Breakdown Structure (WBS)**

| Level 1 | Level 2 | Level 3 | Deskripsi |
|---------|---------|---------|-----------|
| 1. Project Management | 1.1 Inisiasi | 1.1.1 Identifikasi Masalah | Observasi dan wawancara pemangku kepentingan |
| | | 1.1.2 Studi Kelayakan | Analisis kelayakan teknis, operasional, ekonomi |
| | 1.2 Perencanaan | 1.2.1 Penyusunan WBS | Breakdown struktur pekerjaan |
| | | 1.2.2 Estimasi Biaya | Perhitungan biaya pengembangan |
| | 1.3 Monitoring | 1.3.1 Progress Tracking | Pemantauan kemajuan mingguan |
| 2. Analysis | 2.1 Requirements | 2.1.1 Functional Requirements | Identifikasi 40+ kebutuhan fungsional |
| | | 2.1.2 Non-functional Requirements | Keamanan, performa, usability |
| | 2.2 System Analysis | 2.2.1 As-Is Process | Dokumentasi proses bisnis saat ini |
| | | 2.2.2 To-Be Process | Rancangan proses bisnis baru |
| 3. Design | 3.1 Database Design | 3.1.1 ERD | Diagram relasi entitas 16 tabel |
| | | 3.1.2 Normalisasi | Normalisasi hingga 3NF |
| | 3.2 UI/UX Design | 3.2.1 Wireframe | Sketsa antarmuka pengguna |
| | | 3.2.2 Mockup | Desain visual 41 halaman di Figma |
| | 3.3 UML Diagrams | 3.3.1 Use Case Diagram | Diagram kasus penggunaan |
| | | 3.3.2 Activity Diagram | Diagram aktivitas proses bisnis |
| 4. Implementation | 4.1 Backend | 4.1.1 Laravel Setup | Instalasi dan konfigurasi framework |
| | | 4.1.2 Database Migration | Migrasi skema database |
| | | 4.1.3 API Development | Pengembangan controller dan model |
| | 4.2 Frontend | 4.2.1 Blade Templates | Pembuatan template view |
| | | 4.2.2 Tailwind Styling | Styling dengan Tailwind CSS |
| | 4.3 Integration | 4.3.1 Payment Gateway | Integrasi Midtrans |
| | | 4.3.2 Email Service | Konfigurasi notifikasi email |
| 5. Testing | 5.1 Unit Testing | 5.1.1 PHPUnit Tests | 30 test cases |
| | 5.2 Integration Testing | 5.2.1 API Testing | Pengujian integrasi antar modul |
| | 5.3 UAT | 5.3.1 User Testing | Pengujian oleh pengguna akhir |
| 6. Deployment | 6.1 Server Setup | 6.1.1 VPS Configuration | Setup Ubuntu, Nginx, PHP, MySQL |
| | | 6.1.2 SSL Certificate | Instalasi Let's Encrypt |
| | 6.2 Go Live | 6.2.1 Database Migration | Migrasi data ke production |
| | | 6.2.2 System Launch | Peluncuran sistem |

**Gantt Chart:**

Gantt Chart menampilkan jadwal proyek dalam bentuk diagram batang yang menunjukkan start date, duration, dan end date dari setiap aktivitas.

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

| No | Fase | Durasi | Periode | Deliverables |
|----|------|--------|---------|--------------|
| 1 | Analisis Kebutuhan | 2 minggu | 16-29 Sep 2024 | Dokumen SRS, Studi Kelayakan |
| 2 | Desain Sistem | 2 minggu | 30 Sep - 13 Okt 2024 | ERD, Diagram UML, Mockup UI/UX |
| 3 | Implementasi | 4 minggu | 14 Okt - 10 Nov 2024 | Aplikasi web 60+ halaman |
| 4 | Pengujian | 2 minggu | 11-24 Nov 2024 | Laporan pengujian, UAT approval |
| 5 | Deployment | 1 minggu | 25 Nov - 1 Des 2024 | Sistem production live |
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

**Estimasi Biaya Berulang Tahunan (Operational Cost):**

| No | Item | Biaya/Tahun (Rp) |
|----|------|------------------|
| 1 | VPS Hosting | 1.200.000 |
| 2 | Domain & SSL renewal | 150.000 |
| 3 | Payment Gateway Fee (2,9% + Rp 2.000 per transaksi) | ~7.200.000 (estimasi 100 transaksi/bulan) |
| 4 | Maintenance & Support | 1.200.000 |
| **TOTAL** | | **9.750.000** |

### 4.2.4 Perencanaan Kualitas (*Quality*)

Standar kualitas yang ditetapkan untuk proyek ini:

**A. Standar Kualitas Fungsional:**
- **Fungsionalitas**: Minimal 90% kebutuhan fungsional harus terpenuhi dan berfungsi dengan baik
- **Akurasi**: 100% akurasi dalam perhitungan pembayaran, penjadwalan, dan pelaporan
- **Kelengkapan**: Semua modul utama (pemesanan, pembayaran, dashboard) harus tersedia
- **Interoperabilitas**: Integrasi Midtrans dan email service berfungsi tanpa error

**B. Standar Kualitas Non-Fungsional:**
- **Performa**: 
  - Waktu load halaman < 2 detik (average)
  - Response time API < 500ms untuk 95% request
  - Database query time < 100ms (average)
- **Keamanan**: 
  - Mitigasi OWASP Top 10 vulnerabilities
  - Password hashing dengan bcrypt
  - HTTPS untuk semua komunikasi
  - SQL injection prevention (Eloquent ORM)
- **Usability**: 
  - Skor System Usability Scale (SUS) minimal 70/100
  - User satisfaction rating minimal 4/5
  - Task completion rate ≥ 90%
- **Reliability**: 
  - Uptime minimal 99% (maksimal downtime 7,2 jam/bulan)
  - Mean Time Between Failures (MTBF) > 720 jam
  - Recovery Time Objective (RTO) < 4 jam
- **Maintainability**: 
  - Code coverage testing minimal 70%
  - Code quality score (CodeClimate) ≥ B
  - Dokumentasi lengkap (inline comments, README, API docs)

### 4.2.5 Perencanaan Sumber Daya (*Resource*)

**A. Sumber Daya Manusia:**

**Tabel 4.4 Alokasi Sumber Daya Manusia**

| No | Nama | Peran | Tanggung Jawab | Alokasi Waktu |
|----|------|-------|----------------|---------------|
| 1 | Roki Anjas (11250066) | Project Manager & Backend Developer | Koordinasi tim, pengembangan backend, dokumentasi | 40 jam/minggu |
| 2 | Susanto (11250068) | Frontend Developer & UI/UX Designer | Desain antarmuka, pengembangan frontend | 35 jam/minggu |
| 3 | Fahruroji (11250085) | Full-stack Developer & Database Architect | Desain database, pengembangan full-stack, deployment | 35 jam/minggu |

**B. Sumber Daya Teknologi:**
- **Hardware Development:**
  - Laptop/PC untuk development (3 unit - milik tim)
  - VPS Ubuntu 22.04 LTS untuk production server
  - Spesifikasi VPS: 4 vCPU, 8GB RAM, 160GB SSD

- **Software Development:**
  - IDE: Visual Studio Code (gratis)
  - Version Control: Git & GitHub (gratis)
  - Design: Figma (free tier)
  - Framework: Laravel 10 (open source)
  - Database: MySQL 8.0 (open source)
  - CSS Framework: Tailwind CSS (open source)

**C. Sumber Daya Infrastruktur:**
- Domain & SSL Certificate
- Email service (SMTP)
- Payment gateway account (Midtrans)

### 4.2.6 Manajemen Risiko (*Risk*)

Identifikasi, analisis, dan strategi mitigasi risiko proyek:

**Tabel 4.5 Identifikasi dan Mitigasi Risiko**

| No | Risiko | Probabilitas | Dampak | Skor Risiko | Mitigasi | Owner |
|----|--------|-------------|--------|-------------|----------|-------|
| 1 | Keterlambatan jadwal | Sedang | Tinggi | 12 | Buffer time 10%, prioritas fitur dengan MoSCoW, daily standup | PM |
| 2 | Scope creep (perubahan kebutuhan) | Sedang | Tinggi | 12 | Dokumentasi kebutuhan yang jelas, change control process, approval formal | PM |
| 3 | Bug kritis saat deployment | Rendah | Tinggi | 6 | Testing menyeluruh, staging environment, rollback plan | Dev Team |
| 4 | Anggota tim sakit/tidak tersedia | Rendah | Sedang | 4 | Knowledge sharing, dokumentasi kode, pair programming | PM |
| 5 | Integrasi payment gateway gagal | Sedang | Sedang | 6 | Prototyping awal, dokumentasi API lengkap, sandbox testing | Backend Dev |
| 6 | Kehilangan data | Rendah | Tinggi | 6 | Automated daily backup, retention 30 hari, disaster recovery plan | DB Architect |
| 7 | Security breach | Rendah | Sangat Tinggi | 8 | Security audit, penetration testing, follow OWASP guidelines | Dev Team |
| 8 | Performance issues | Sedang | Sedang | 6 | Load testing, database indexing, caching strategy | Full-stack Dev |

**Catatan Skor Risiko:**
- Probabilitas: Rendah (1), Sedang (2), Tinggi (3)
- Dampak: Rendah (2), Sedang (4), Tinggi (6), Sangat Tinggi (8)
- Skor Risiko = Probabilitas × Dampak

### 4.2.7 Perencanaan Komunikasi (*Communication*)

Strategi komunikasi untuk memastikan informasi mengalir dengan efektif:

**A. Komunikasi Internal Tim:**
- **Daily Standup**: Chat group WhatsApp setiap pagi (15 menit)
  - What did I do yesterday?
  - What will I do today?
  - Any blockers?

- **Weekly Team Meeting**: Setiap Senin pukul 19.00 WIB via Google Meet (1-2 jam)
  - Review progress vs plan
  - Demo fitur yang selesai
  - Planning untuk minggu depan
  - Risk review

- **Code Review**: Pull request di GitHub dengan review wajib dari minimal 1 anggota tim

**B. Komunikasi dengan Stakeholder:**
- **Progress Report ke Dosen Pembimbing**: Setiap 2 minggu (email + meeting)
- **Client Meeting (CUR-HEART)**: Bi-weekly untuk review dan feedback
- **UAT Sessions**: 3 kali selama fase testing

**C. Dokumentasi:**
- **Google Drive**: Repository untuk semua dokumen proyek
- **GitHub Wiki**: Dokumentasi teknis dan API
- **Notion**: Knowledge base dan meeting notes

**D. Tools Komunikasi:**
- WhatsApp: Quick communication
- Google Meet: Virtual meetings
- Email: Formal communication
- GitHub: Code collaboration
- Figma: Design collaboration

### 4.2.8 Perencanaan Pengadaan (*Procurement*)

Pengadaan barang dan jasa yang diperlukan:

**Tabel 4.6 Daftar Pengadaan**

| No | Item | Vendor | Biaya | Timeline | PIC |
|----|------|--------|-------|----------|-----|
| 1 | VPS Hosting | Niagahoster | Rp 1.200.000/tahun | Minggu 8 | Fahruroji |
| 2 | Domain .id | Niagahoster | Rp 150.000/tahun | Minggu 8 | Fahruroji |
| 3 | SSL Certificate | Let's Encrypt | Gratis | Minggu 8 | Fahruroji |
| 4 | Payment Gateway | Midtrans | Gratis (dev), 2,9% + Rp 2.000 (prod) | Minggu 6 | Roki |
| 5 | Email Service | Gmail SMTP / SendGrid | Gratis (limited) | Minggu 7 | Roki |

**Proses Pengadaan:**
1. Identifikasi kebutuhan
2. Vendor selection & comparison
3. Approval dari sponsor
4. Purchase order
5. Delivery & verification
6. Payment
7. Documentation

### 4.2.9 Perencanaan Integrasi (*Integration*)

Integrasi sistem dengan layanan eksternal:

**A. Payment Gateway Integration (Midtrans):**
- **Metode**: Snap API untuk seamless checkout
- **Payment Methods**: Credit/debit card, Bank transfer, E-wallet (GoPay, OVO, Dana)
- **Security**: PCI-DSS compliant, 3D Secure support
- **Webhook**: Untuk real-time payment notification
- **Timeline**: Minggu 6-7 (implementation + testing)

**B. Email Service Integration:**
- **Provider**: Gmail SMTP / SendGrid
- **Use Cases**:
  - Welcome email saat registrasi
  - Email verifikasi
  - Booking confirmation
  - Payment notification
  - Session reminder (H-1, H-0)
  - Password reset
- **Timeline**: Minggu 7-8

**C. Future Integrations (Phase 2):**
- SMS notification via Twilio
- Cloud storage (Google Drive / AWS S3)
- Video conferencing (Zoom API)
- Analytics (Google Analytics)

### 4.2.10 Manajemen Pemangku Kepentingan (*Stakeholder*)

Identifikasi dan strategi keterlibatan pemangku kepentingan:

**Tabel 4.7 Daftar Pemangku Kepentingan**

| No | Stakeholder | Peran | Kepentingan | Power | Interest | Strategi |
|----|------------|-------|-------------|-------|----------|----------|
| 1 | Pemilik CUR-HEART | Sponsor & Decision Maker | Sangat Tinggi | Tinggi | Tinggi | Manage Closely: Presentasi progress bulanan, approval kebutuhan |
| 2 | Terapis (3 orang) | End User | Tinggi | Sedang | Tinggi | Keep Informed: Workshop kebutuhan, UAT, training |
| 3 | Admin (2 orang) | End User | Tinggi | Sedang | Tinggi | Keep Informed: Workshop kebutuhan, UAT, training |
| 4 | Klien (8 orang sample) | End User | Sedang | Rendah | Sedang | Monitor: Survey kebutuhan, usability testing |
| 5 | Dosen Pembimbing | Academic Advisor | Sangat Tinggi | Tinggi | Tinggi | Manage Closely: Konsultasi mingguan, review dokumen |
| 6 | Tim Pengembang | Development Team | Sangat Tinggi | Tinggi | Tinggi | Manage Closely: Daily standup, weekly meeting |

**Strategi Keterlibatan:**
- **Manage Closely**: High power, high interest - keterlibatan intensif dan update regular
- **Keep Informed**: Low power, high interest - informasi regular, input didengarkan
- **Keep Satisfied**: High power, low interest - update penting, minta approval
- **Monitor**: Low power, low interest - komunikasi minimal, monitoring

### 4.2.11 Batasan Proyek

Batasan-batasan proyek yang telah disepakati:

**A. Batasan Waktu:**
- Fokus proyek pada pembangunan sistem informasi dalam kurun waktu 16 minggu (4 bulan)
- Tidak membahas quality control & quality assurance secara khusus (hanya pengujian standar)
- Evaluasi jangka panjang (> 6 bulan) tidak termasuk dalam scope

**B. Batasan Fitur:**
- Tidak membahas mengenai risiko proyek secara mendalam, fokus hanya pada risiko permintaan perubahan
- Modul analytics dan reporting dibatasi pada laporan standar (advanced analytics/BI ditunda ke fase 2)
- Integrasi dengan sistem eksternal lain (selain Midtrans dan email) tidak termasuk dalam fase 1

**C. Batasan Biaya:**
- Biaya yang dimaksud adalah biaya untuk tim proyek (tidak termasuk manajer proyek senior eksternal)
- Budget terbatas pada development dan 1 tahun operasional awal
- Biaya training intensif untuk semua staf tidak termasuk (hanya training dasar 2 jam)

**D. Batasan Teknis:**
- Sistem dioptimalkan untuk desktop dan tablet, support mobile dalam bentuk responsive design (bukan native mobile app)
- Kapasitas sistem didesain untuk menangani hingga 50 concurrent users
- Bahasa sistem: Bahasa Indonesia (multi-language tidak termasuk fase 1)
- Sistem tidak termasuk fitur video call untuk sesi terapi online

**E. Batasan Data:**
- Migrasi data historis dibatasi pada data 6 bulan terakhir
- Data backup retention: 30 hari (untuk backup jangka panjang memerlukan biaya tambahan)

**F. Batasan Hukum:**
- Sistem mengikuti prinsip dasar UU Perlindungan Data Pribadi, namun sertifikasi kepatuhan formal tidak termasuk
- Disclaimer medis: Sistem untuk manajemen administrasi, bukan untuk diagnosis medis

### 4.2.12 Asumsi Proyek

Asumsi-asumsi yang mendasari perencanaan proyek:

**A. Asumsi Pengadaan:**
- Procurement atau pengadaan sudah tidak ada masalah, sumber daya non-personil tersedia sesuai spesifikasi
- VPS hosting dapat disewa sesuai spesifikasi yang dibutuhkan
- Domain dapat dibeli dan dikonfigurasi dengan lancar

**B. Asumsi Sumber Daya Manusia:**
- Human resource sudah tersedia sesuai dengan spesifikasi proyek
- Anggota tim adalah SDM profesional (mahasiswa dengan kompetensi memadai)
- Tidak ada anggota tim yang mengundurkan diri atau sakit berkepanjangan selama proyek
- Terapis dan admin CUR-HEART bersedia meluangkan waktu untuk workshop, UAT, dan training

**C. Asumsi Teknis:**
- Manajer proyek adalah personil dari dalam tim (ketua tim mahasiswa)
- Infrastruktur teknologi (internet, listrik) stabil di lokasi development dan CUR-HEART
- API Midtrans berfungsi stabil dengan dokumentasi lengkap
- SMTP email service dapat dikonfigurasi tanpa hambatan

**D. Asumsi Organisasi:**
- Struktur organisasi CUR-HEART sudah diterapkan dengan baik
- Pemilik & manajer proyek sudah ditunjuk beserta anggota tim
- Approval dan decision making dari stakeholder dapat dilakukan tepat waktu
- Tidak ada perubahan manajemen atau struktur organisasi selama proyek

**E. Asumsi Proses Bisnis:**
- Proses bisnis CUR-HEART yang ada saat ini sudah terdokumentasi dengan baik
- Stakeholder dapat mengartikulasikan kebutuhan mereka dengan jelas
- Tidak ada perubahan signifikan pada proses bisnis selama pengembangan

**F. Asumsi Pengguna:**
- Klien CUR-HEART memiliki akses internet dan perangkat (smartphone/laptop/tablet)
- Pengguna memiliki kemampuan dasar menggunakan teknologi digital
- Klien bersedia mengadopsi sistem online untuk pemesanan

**G. Asumsi Regulasi:**
- Tidak ada perubahan regulasi terkait data pribadi atau layanan kesehatan mental selama proyek
- Bisnis CUR-HEART memiliki izin operasional yang legal

---

