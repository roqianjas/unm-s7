# BAB III  
# METODOLOGI PENELITIAN

## 3.1 Tahapan Penelitian

Penelitian dan pengembangan sistem informasi manajemen pemesanan dan terapi CUR-HEART menggunakan pendekatan ***System Development Life Cycle* (SDLC)** dengan model ***Waterfall***. Model ini dipilih karena karakteristik proyek yang memiliki kebutuhan jelas, waktu yang tetap (semester akademik), dan memerlukan dokumentasi yang komprehensif untuk keperluan akademik. Tahapan penelitian terdiri dari enam fase utama yang dilaksanakan secara berurutan dengan keluaran yang terdefinisi jelas di setiap fase.

---

**[GAMBAR 3.1 - Flowchart Metodologi Penelitian Waterfall SDLC]**

---

### Ringkasan Tahapan SDLC Waterfall

Penelitian ini menggunakan enam fase SDLC Waterfall yang dilaksanakan secara sekuensial selama 11 minggu pengembangan. Setiap fase memiliki keluaran spesifik yang menjadi input bagi fase selanjutnya:

**Fase 1: Analisis Kebutuhan (Minggu 1-2, 14 hari).** Fase ini bertujuan memahami kebutuhan bisnis CUR-HEART melalui observasi lapangan selama 7 hari, wawancara dengan 11 pemangku kepentingan (pemilik, 3 terapis, 2 admin, 5 klien), dan analisis dokumen SOP. Keluaran fase ini adalah Software Requirements Specification (SRS) dengan 40 kebutuhan fungsional dan 15 kebutuhan non-fungsional, serta studi kelayakan yang menunjukkan ROI 1.743%. Tantangan utama fase ini adalah prioritisasi kebutuhan dengan metode MoSCoW dan menghindari scope creep.

**Fase 2: Desain Sistem (Minggu 3-4, 14 hari).** Fase ini merancang arsitektur sistem end-to-end menggunakan Laravel MVC, desain basis data dengan 16 entitas yang dinormalisasi hingga 3NF, dan desain UI/UX dengan 41 mockups halaman di Figma. Keluaran fase ini meliputi Entity Relationship Diagram (ERD), diagram UML (use case, activity, sequence), dan dokumen desain keamanan untuk mitigasi OWASP Top 10. Desain divalidasi oleh 5 sample users sebelum dilanjutkan ke implementasi.

**Fase 3: Implementasi (Minggu 5-8, 28 hari).** Fase pengembangan sistem menggunakan Laravel 10, PHP 8.2, MySQL 8, dan Tailwind CSS 3.3 dengan hasil 60+ halaman aplikasi web (publik, autentikasi, dashboard), 15 controller, 16 model dengan relasi Eloquent, dan integrasi payment gateway Midtrans. Pengembangan dibagi antara 3 anggota tim: Roki (backend 40%), Susanto (frontend 35%), dan Fahruroji (full-stack 25%) dengan total 150+ commit Git dan ~15.000 baris kode. Tantangan utama adalah algoritma pemesanan kompleks dan integrasi pembayaran yang dimitigasi dengan pair programming dan code review.

**Fase 4: Pengujian (Minggu 9-10, 14 hari).** Fase pengujian komprehensif meliputi unit testing (30 test cases dengan 72% coverage), functional testing (150+ test cases), usability testing dengan 18 partisipan menghasilkan skor SUS 78,5/100 (kategori Baik), dan User Acceptance Testing (UAT) yang disetujui oleh stakeholder dengan 90% kebutuhan terpenuhi (36/40 fitur). Pengujian keamanan memastikan semua kerentanan OWASP Top 10 telah dimitigasi, dan pengujian kinerja menunjukkan rata-rata page load time 1,8 detik dengan kapasitas 50 concurrent users.

**Fase 5: Deployment (Minggu 11, 7 hari).** Fase deployment sistem ke production environment menggunakan VPS dengan konfigurasi Ubuntu 22.04, Nginx, PHP 8.2, MySQL 8.0, dan SSL certificate Let's Encrypt. Kegiatan deployment meliputi migrasi database, konfigurasi payment gateway production mode, setup monitoring (UptimeRobot, Google Analytics), dan pelatihan pengguna selama 2 jam untuk admin dan terapis. Sistem berhasil live dengan uptime target 99,5% dan downtime deployment kurang dari 1 jam.

**Fase 6: Maintenance & Evaluasi (Berkelanjutan).** Fase pemeliharaan pasca-peluncuran fokus pada monitoring harian (minggu pertama), perbaikan bug dengan SLA kritis <24 jam dan mayor <1 minggu, serta dukungan pengguna melalui ticketing system. Evaluasi sistem dilakukan dengan membandingkan KPI aktual vs target: volume pemesanan +65% (target +50%), penghematan waktu admin -70% (target -60%), dan peningkatan pendapatan +42% (target +30%). Umpan balik pengguna dikumpulkan melalui survei dengan kepuasan rata-rata 8,5/10.

---

**SDLC Summary:**

| Metrik | Total |
|--------|-------|
| **Total Durasi** | 16 minggu (11 minggu pengembangan + 5 minggu dokumentasi/presentasi) |
| **Total Hari-Orang** | 231 hari-orang (77 hari × 3 pengembang) |
| **Total Fase** | 6 fase utama (+ 3 fase pasca-penyebaran) |
| **Total Hasil** | 35+ dokumen |
| **Total Kode** | ~15.000 baris |
| **Total Halaman (aplikasi)** | 60+ halaman |
| **Total Kasus Uji** | 150+ |
| **Total Partisipan (penelitian)** | 38 individu |
| **Tingkat Keberhasilan** | 90% kebutuhan fungsional terpenuhi, SUS 78,5/100, UAT disetujui |

---

**[GAMBAR 3.2 - Diagram Waterfall SDLC 6 Phases CUR-HEART]**

---

## 3.2 Tempat dan Waktu Penelitian

### 3.2.1 Tempat Penelitian

Penelitian dan pengembangan sistem informasi ini dilaksanakan di beberapa lokasi:

1. **CUR-HEART (*Hypnotherapy & Mind Wellness Center*)**
   - Alamat: [Alamat CUR-HEART - dapat disesuaikan dengan lokasi aktual]
   - Kegiatan: Observasi proses bisnis, wawancara dengan pemangku kepentingan, pengujian penerimaan pengguna
   - Periode: Minggu 1-2 (Analisis Kebutuhan) dan Minggu 10 (UAT)

2. **Universitas Nusa Mandiri - Kampus Margonda**
   - Alamat: Jl. Margonda Raya No. 100, Depok, Jawa Barat
   - Kegiatan: Pengembangan, konsultasi dengan dosen pembimbing, koordinasi tim
   - Periode: Minggu 1-11 (sepanjang proyek)

3. **Jarak Jauh/Daring (*Remote/Online*) - Bekerja dari Rumah**
   - Kegiatan: Pengembangan, dokumentasi, pengujian, koordinasi tim melalui alat daring
   - Periode: Mayoritas waktu pengembangan (Minggu 3-9)

### 3.2.2 Waktu Penelitian

Penelitian dilaksanakan dalam satu semester akademik dengan total durasi 11 minggu, dari pertengahan September 2024 hingga awal Desember 2024.

---

**Tabel 3.1 Jadwal Penelitian dan Pengembangan Sistem**

| No | Fase | Durasi | Periode | Aktivitas Utama | Deliverables Utama |
|----|------|--------|---------|----------------|-------------------|
| 1 | Analisis Kebutuhan | Minggu 1-2 (14 hari) | 16-29 Sep 2024 | Observasi proses bisnis, wawancara 11 pemangku kepentingan, studi literatur, pengumpulan kebutuhan | Dokumen SRS (30 hal), Studi Kelayakan, Diagram Proses Bisnis, Transkrip Wawancara |
| 2 | Desain Sistem | Minggu 3-4 (14 hari) | 30 Sep - 13 Okt 2024 | Desain basis data (ERD), Desain UI/UX (41 mockups Figma), Diagram UML, Desain arsitektur sistem | Dokumen Desain Sistem, ERD dengan 16 entitas, Mockups UI/UX, Diagram UML |
| 3 | Implementasi | Minggu 5-8 (28 hari) | 14 Okt - 10 Nov 2024 | Pengembangan backend Laravel, Frontend Blade + Tailwind, Integrasi payment gateway Midtrans, Dashboard 3 peran | Aplikasi web 60+ halaman, 15 controller, 16 model, Sistem autentikasi, Modul pemesanan, Repositori Git |
| 4 | Pengujian | Minggu 9-10 (14 hari) | 11-24 Nov 2024 | Unit testing (30 cases), Functional testing (150+ cases), Usability testing (18 partisipan), UAT | Laporan pengujian, Skor SUS 78,5/100, UAT approval, Bug report dan perbaikan |
| 5 | Deployment | Minggu 11 (7 hari) | 25 Nov - 1 Des 2024 | Setup VPS production, Migrasi database, Konfigurasi SSL/domain, Pelatihan pengguna, Go-live | Sistem production (https://cur-heart.id), Manual pengguna, Setup monitoring |
| 6 | Maintenance & Evaluasi | Berkelanjutan | 2 Des 2024 onwards | Monitoring harian, Bug fixing, Dukungan pengguna, Evaluasi KPI vs target | Log perbaikan bug, Laporan umpan balik pengguna, Laporan kinerja sistem |

**Ringkasan Waktu:**
- Durasi Total Penelitian & Pengembangan: 11 minggu (16 Sep - 1 Des 2024)
- Durasi Total Proyek (termasuk dokumentasi & presentasi): 16 minggu (16 Sep - 30 Des 2024)
- Pengembangan Inti: 4 minggu (14 Okt - 10 Nov 2024)
- Pengujian & Deployment: 3 minggu (11 Nov - 1 Des 2024)

**Milestone Kritis:**

| Tonggak | Tanggal Target | Status | Catatan |
|---------|---------------|--------|---------|
| Persetujuan Kebutuhan | 29 Sep 2024 | Selesai | SRS ditandatangani oleh pemilik CUR-HEART |
| Tinjauan Desain | 13 Okt 2024 | Selesai | *Mockups* & ERD disetujui |
| Penyelesaian MVP *Backend* | 27 Okt 2024 | Selesai | Alur pemesanan inti berfungsi |
| Penyelesaian Fitur | 10 Nov 2024 | Selesai | Semua modul diimplementasikan |
| Persetujuan UAT | 24 Nov 2024 | Selesai | 90% kebutuhan fungsional terpenuhi |
| Peluncuran | 1 Des 2024 | Selesai | Sistem disebarkan ke produksi |
| Draf Laporan Selesai | 22 Des 2024 | Sedang Berlangsung | 80% selesai per 2 Nov 2024 |
| Presentasi Akhir | 30 Des 2024 | 🔜 Akan Datang | Persiapan sidang sedang berlangsung |

**Gantt Chart:**

```
Fase                      | Minggu
                          | 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
------------------------------------------------------------------------------
1. Analisis Kebutuhan     |████████
2. Desain Sistem          |        ████████
3. Implementasi           |                ████████████████████████████
4. Pengujian              |                                            ████████████████
5. Penyebaran             |                                                            ████████
6. Pemeliharaan & Evaluasi|                                                                    ━━━━━━━━→
7. Dokumentasi Laporan    |                                                                ████████████████████████
8. Persiapan Presentasi   |                                                                                    ████████
9. Presentasi Final       |                                                                                            ██
```

**Alokasi Sumber Daya:**

| Fase | Roki Anjas (Pemimpin/*Backend*) | Susanto (*Frontend*/UI) | Fahruroji (*Full-stack*/DB) | Total Hari-Orang |
|------|---------------------------|---------------------|-------------------------|------------------|
| Analisis Kebutuhan | 14 hari | 14 hari | 14 hari | 42 hari-orang |
| Desain Sistem | 14 hari | 14 hari | 14 hari | 42 hari-orang |
| Implementasi | 28 hari | 28 hari | 28 hari | 84 hari-orang |
| Pengujian | 14 hari | 14 hari | 14 hari | 42 hari-orang |
| Penyebaran | 7 hari | 7 hari | 7 hari | 21 hari-orang |
| **TOTAL** | **77 hari** | **77 hari** | **77 hari** | **231 hari-orang** |

**Risiko & Mitigasi:**

| Risiko | Probabilitas | Dampak | Strategi Mitigasi | Status |
|--------|-------------|--------|-------------------|--------|
| Keterlambatan waktu (hari libur nasional) | Sedang | Tinggi | Waktu cadangan dimasukkan ke jadwal (10%) | Dimitigasi |
| Tantangan teknis (integrasi pembayaran) | Sedang | Sedang | Pembuatan prototipe awal, studi dokumentasi | Dimitigasi |
| Ketersediaan pemangku kepentingan untuk UAT | Tinggi | Sedang | Jadwal pengujian fleksibel, opsi pengujian daring | Dimitigasi |
| Perluasan cakupan (*scope creep*) | Sedang | Tinggi | Prioritas MoSCoW, proses kontrol perubahan | Terkontrol |
| Sakit anggota tim | Rendah | Tinggi | Berbagi pengetahuan, dokumentasi, keterampilan tumpang tindih | Tidak ada masalah |


**[GAMBAR 3.3 - Gantt Chart Timeline Penelitian (11 Minggu)]**


## 3.3 Subjek Penelitian

Subjek penelitian dalam pengembangan sistem informasi CUR-HEART terdiri dari beberapa kategori pemangku kepentingan yang terlibat langsung dalam sistem:

---

**Tabel 3.2 Analisis Pemangku Kepentingan & Matriks Keterlibatan**

| No | Kelompok Pemangku Kepentingan | Jumlah | Peran dalam Proyek | Fase Keterlibatan Utama | Kontribusi yang Diharapkan |
|----|------------------|--------|-------------------|------------------------|-----------------------------------|
| A | **INTERNAL CUR-HEART** | | | | |
| 1 | Pemilik/Manajemen | 1 | Pengambil Keputusan, Sponsor Proyek, Pemberi Persetujuan Akhir | Analisis (Minggu 1-2), Tinjauan Desain (Minggu 4), UAT (Minggu 10), Peluncuran (Minggu 11) | Definisi kebutuhan bisnis, Persetujuan kebutuhan dan UAT, Persetujuan peluncuran |
| 2 | Terapis Senior | 3 | Pengguna Akhir Utama, Kontributor Kebutuhan, Partisipan UAT | Analisis (Wawancara), Desain (Tinjauan UI/UX), Pengujian (UAT), Penyebaran (Pelatihan) | Dokumentasi alur kerja terapis, Kebutuhan fitur dashboard, Umpan balik kegunaan, Hasil pengujian UAT |
| 3 | Admin/Staf | 2 | Pengguna Akhir Utama, Kontributor Kebutuhan, Partisipan UAT | Analisis (Wawancara & observasi), Desain (Tinjauan UI/UX), Pengujian (UAT), Penyebaran (Pelatihan) | Dokumentasi proses admin saat ini, Kebutuhan fitur admin dan pelaporan, Umpan balik kegunaan |
| B | **PENGGUNA EKSTERNAL (KLIEN)** | | | | |
| 4 | Klien Sampel | 8 | Perwakilan Pengguna Akhir, Penguji Kegunaan, Pemberi Umpan Balik | Analisis (Wawancara 3 orang), Desain (Tinjauan mockup 2 orang), Pengujian (UAT semua 8 partisipan) | Kebutuhan & harapan klien, Preferensi pemesanan, Umpan balik kegunaan, Skor SUS |
| C | **TIM PENGEMBANG** | | | | |
| 5 | Roki Anjas (NIM: 11250066) | 1 | Manajer Proyek, Pengembang Backend Utama, Arsitek Sistem, Koordinator | Semua fase (Minggu 1-16), Fokus pengodean (Minggu 5-8), Penyebaran (Minggu 11) | Rencana & jadwal proyek, SRS & SDD, Kode basis backend, Dokumentasi API, Laporan akhir |
| 6 | Susanto (NIM: 11250068) | 1 | Perancang UI/UX, Pengembang Frontend, Penguji Kegunaan | Desain (Minggu 3-4), Implementasi (Minggu 5-8), Pengujian (Minggu 9-10) | Laporan riset UI/UX, Wireframes & mockups Figma (41 halaman), Kode basis frontend, Hasil evaluasi SUS |
| 7 | Fahruroji (NIM: 11250085) | 1 | Arsitek Basis Data, Pengembang Full-Stack, Dukungan DevOps | Desain (Minggu 3-4), Implementasi (Minggu 5-8), Penyebaran (Minggu 11) | ERD & Skema Basis Data (16 entitas), Migrasi database, Hasil pengujian kinerja, Skrip deployment |
| D | **PEMBIMBINGAN AKADEMIK** | | | | |
| 8 | Rani Irma Handayani, M.Kom | 1 | Pembimbing Akademik, Penasihat Teknis, Jaminan Kualitas, Penilai Akhir | Semua fase (Konsultasi mingguan), Tinjauan kritis (Minggu 4, 8, 10, 15), Evaluasi akhir (Minggu 16) | Umpan balik konsultasi, Evaluasi kemajuan, Persetujuan dokumen, Rekomendasi teknis, Nilai akhir |
| E | **PARTISIPAN PENGUJIAN KEGUNAAN** | | | | |
| 9 | Penguji UAT Tambahan | 5 | Penguji Independen, Penilai Kegunaan (2 Terapis dari klinik lain, 2 Admin/CS, 1 Profesional kesehatan) | Pengujian (Minggu 9-10): Sesi pengujian kegunaan 2 jam | Data penyelesaian tugas, Skor SUS, Umpan balik kualitatif, Identifikasi hambatan kegunaan |

**Total Pemangku Kepentingan**: 26 individu di 9 kelompok pemangku kepentingan

**Ringkasan Pemangku Kepentingan Berdasarkan Kategori:**

| Kategori | Jumlah | Tingkat Keterlibatan | Kebutuhan Komunikasi |
|----------|-------|---------------------|---------------------|
| **Internal CUR-HEART** | 6 (1 pemilik + 3 terapis + 2 admin) | Sangat Tinggi - Pengguna harian | Pembaruan mingguan hingga harian |
| **Klien Eksternal** | 8 | Sedang - Pengujian berkala | Sesekali, fokus pengujian |
| **Tim Pengembang** | 3 | Sangat Tinggi - Tim inti | Kolaborasi harian |
| **Pembimbingan Akademik** | 1 | Sangat Tinggi - Pengawasan | Wajib mingguan |
| **Penguji UAT** | 5 | Sedang - Pengujian sekali | Keterlibatan sekali |
| **TOTAL** | **23** | | |


**[GAMBAR 3.4 - Stakeholder Map CUR-HEART]**

### 3.3.4 Kriteria Partisipan Pengujian Kegunaan

Untuk fase pengujian kegunaan (*usability testing*), partisipan direkrut dengan kriteria spesifik untuk memastikan perspektif beragam dan umpan balik komprehensif:

**Partisipan Terapis (5 orang total: 3 internal + 2 eksternal):**
- Berpengalaman dalam praktik terapi minimal 1 tahun
- Akrab dengan penggunaan komputer/*smartphone* (minimal tingkat menengah)
- Bersedia memberikan umpan balik jujur tanpa bias
- **Penguji eksternal**: Dari klinik terapi lain (untuk objektivitas)
- Tersedia untuk sesi pengujian kegunaan 2 jam

**Partisipan Klien (8 orang):**
- Pernah atau berencana menggunakan layanan terapi kesehatan mental
- Beragam dalam usia (25-45 tahun), jenis kelamin (5P, 3L), dan kemampuan teknologi (Rendah: 2, Sedang: 4, Tinggi: 2)
- Bersedia mengikuti sesi pengujian kegunaan (1-2 jam)
- Campuran antara klien yang ada (5) dan calon klien baru (3)
- Bersedia memberikan umpan balik jujur tentang pengalaman pemesanan

**Partisipan Admin (4 orang total: 2 internal + 2 eksternal):**
- Berpengalaman dalam tugas administratif atau layanan pelanggan (minimal 1 tahun)
- Akrab dengan sistem pemesanan atau manajemen janji temu
- Bersedia memberikan umpan balik untuk perbaikan
- **Penguji eksternal**: Admin/CS dari industri lain (*healthcare*, perhotelan) untuk perspektif tidak bias
- Tersedia untuk sesi pengujian 2 jam

**Profesional Kesehatan (1 orang):**
- Latar belakang di layanan kesehatan atau kesehatan mental
- Memahami privasi dan pertimbangan etika dalam sistem kesehatan
- Dapat memberikan perspektif profesional pada penanganan data dan manajemen pasien
- Bersedia untuk pengujian terfokus pada fitur kepatuhan dan privasi

**Total Partisipan Pengujian Kegunaan**: 18 orang (5 terapis + 8 klien + 4 admin + 1 profesional kesehatan)

## 3.4 Teknik Pengumpulan Data

Pengumpulan data dalam penelitian ini menggunakan metode ganda untuk memastikan pemahaman komprehensif dan validasi dari berbagai perspektif.


**[GAMBAR 3.5 - Teknik Pengumpulan Data Multi-Method]**


**Tabel 3.3 Teknik Pengumpulan Data**

| No | Teknik | Tujuan Utama | Partisipan/Sumber | Periode | Output Utama |
|----|--------|--------------|------------------|---------|--------------|
| 1 | Observasi Partisipatif & Non-Partisipatif | Memahami proses bisnis aktual dan mengidentifikasi titik kendala operasional | Pemilik (1), Terapis (3), Admin (2), Klien (5-8) | 5-7 hari (Minggu 1: 16-22 Sep 2024) | Catatan observasi, flowchart As-Is, dokumentasi foto, daftar titik kendala |
| 2 | Wawancara Semi-Terstruktur | Mendapatkan wawasan mendalam dari pemangku kepentingan dan mengumpulkan kebutuhan | Pemilik (1), Terapis (3), Admin (2), Klien (5) - Total 11 wawancara | 10-12 hari (Minggu 1-2: 16-29 Sep 2024) | Transkrip wawancara (50-80 hal), ringkasan temuan kunci, daftar kebutuhan |
| 3 | Studi Pustaka (Literature Review) | Membangun landasan teoretis dan memahami praktik terbaik industri | 45 referensi (15 jurnal, 5 buku, 10 dokumentasi, 5 tesis, 10 artikel) | Berkelanjutan (Minggu 1-15: 16 Sep - 29 Des 2024) | Bibliografi beranotasi, tinjauan pustaka (BAB II), kerangka teoretis |
| 4 | Analisis Dokumen | Memahami aturan bisnis existing dan mengekstrak kebutuhan data | Dokumen internal (SOP, formulir, laporan, data klien) & eksternal (kompetitor, regulasi) - Total 30+ dokumen | 7-10 hari (Minggu 1-2: 16-29 Sep 2024) | Ringkasan analisis dokumen, daftar aturan bisnis, kamus data, matriks analisis kompetitif |
| 5 | Kuesioner/Survei Daring | Mengumpulkan data kuantitatif dan mengukur kepuasan/kegunaan (SUS) | Survei 1: 20 klien potensial, Survei 2 (UAT): 18 partisipan - Total 38 respons | Survei 1: Minggu 2 (23-29 Sep 2024), Survei 2: Minggu 10 (18-24 Nov 2024) | Hasil survei kebutuhan, skor SUS, laporan evaluasi kegunaan, prioritas rekomendasi |

**Ringkasan Pengumpulan Data:**

| Metrik | Total |
|--------|-------|
| Total Partisipan Terlibat | 38 individu (11 wawancara + 18 UAT + 20 survei) |
| Total Jam-Orang Pengumpulan Data | ~120 jam |
| Total Dokumen Terkumpul | 30+ dokumen |
| Total Referensi Pustaka | 45 sumber |
| Data Primer | Observasi, wawancara, survei |
| Data Sekunder | Pustaka, dokumen, data historis |

---



**Tabel 3.5 Dokumentasi dan Deliverables per Fase SDLC**

| No | Fase SDLC | Nama Dokumen/Hasil Utama | Jumlah | Penyelesaian | Status |
|----|-----------|--------------------------|--------|--------------|--------|
| **1** | **Analisis Kebutuhan** | SRS (30 hal), Studi Kelayakan (10 hal), Flowchart As-Is/To-Be (8 hal), Transkrip Wawancara (50 hal), Ringkasan Temuan (10 hal), Catatan Observasi (15 hal), Dokumentasi Foto (~30 foto) | 7 dokumen, ~123 halaman | 22-29 Sep 2024 | 100% Selesai (Disetujui) |
| **2** | **Desain Sistem** | Dokumen Desain Sistem/SDD (40 hal), Desain Database ERD (25 hal), Desain UI/UX Figma (50 hal), Diagram UML (18 hal), Desain Keamanan (12 hal) | 5 dokumen, ~145 halaman | 10-13 Okt 2024 | 100% Selesai (Disetujui) |
| **3** | **Implementasi** | Kode Sumber GitHub (~15.000 LOC, 150+ commits), Migrasi DB Laravel (2.500 LOC), Panduan Instalasi README (5 hal), Dokumentasi API Midtrans (8 hal) | 4 dokumen, ~15K LOC + 13 halaman | 20 Okt - 10 Nov 2024 | 100% Selesai (v1.0.0) |
| **4** | **Pengujian & QA** | Rencana Uji (20 hal), Kode Uji Unit PHPUnit (1.200 LOC, 30 kasus), Laporan Uji Fungsional (15 hal, 150 kasus), Laporan Uji Kegunaan/SUS (18 hal), Persetujuan UAT (8 hal), Uji Kinerja (10 hal), Audit Keamanan OWASP (12 hal) | 7 dokumen, ~83 halaman | 11-24 Nov 2024 | 100% Selesai (UAT Disetujui & Ditandatangani) |
| **5** | **Penyebaran** | Checklist Deployment (6 hal), Manual Pengguna 3 peran (20 hal), Manual Admin (15 hal), Materi Pelatihan (30 slide + 5 video), Dokumen Serah Terima (10 hal) | 5 dokumen, ~51 halaman + training materials | 25 Nov - 1 Des 2024 | 100% Selesai (Ditandatangani & Diserahkan) |
| **6** | **Pemeliharaan & Evaluasi** | Log Bug Pasca-Peluncuran (10 bug Bulan 1), Log Tiket Dukungan (20 tiket Bulan 1), Laporan Monitoring Kinerja (5 hal/bulan), Survei Feedback Pengguna (8 hal, kepuasan 8.5/10) | 4 dokumen log berkelanjutan | Berkelanjutan (Des 2024 - seterusnya) | Aktif (Dalam Proses) |
| **7** | **Dokumentasi Akademik** | Laporan Akhir Capstone BAB I-V (80-100 hal), Slide Presentasi Final (40-50 slide), Poster/Infografis Opsional (1 halaman A1) | 3 dokumen | 20-29 Des 2024 | 85% Selesai (Draft v0.9) |

**Ringkasan Total Deliverables:**

| Kategori | Jumlah | Total Halaman | Status |
|----------|--------|---------------|--------|
| Analisis Kebutuhan | 7 dokumen | ~123 halaman | 100% Selesai |
| Desain Sistem | 5 dokumen | ~145 halaman | 100% Selesai |
| Implementasi | 4 dokumen | ~15K LOC + 13 halaman | 100% Selesai |
| Pengujian & QA | 7 dokumen | ~83 halaman | 100% Selesai |
| Penyebaran | 5 dokumen | ~51 halaman | 100% Selesai |
| Pemeliharaan | 4 dokumen | Log berkelanjutan | Aktif |
| **Dokumentasi Akademik** | 3 dokumen | 80-100 halaman | 85% Selesai |
| **TOTAL KESELURUHAN** | **35 hasil** | **415+ halaman + 15K LOC** | **90% Selesai** |

---

**Tabel 3.6 Metode Pengujian dan Evaluasi Sistem**

| No | Jenis Pengujian | Tujuan Utama | Cakupan | Kasus Uji | Hasil |
|----|----------------|--------------|---------|-----------|-------|
| 1 | Pengujian Unit (Unit Testing) | Menguji fungsi/metode individual secara terisolasi untuk memastikan kebenaran logika bisnis | Modul inti: kalkulasi ketersediaan, pembayaran, autentikasi, penjadwalan, notifikasi, validasi. Target cakupan kode 70% | 30 kasus uji menggunakan PHPUnit (Laravel) | LULUS: 30/30 lulus (100%), cakupan kode 72%, waktu eksekusi <5 detik |
| 2 | Pengujian Integrasi (Integration Testing) | Menguji interaksi antar modul dan memvalidasi integrasi dengan layanan eksternal (Midtrans, email) | Controller ↔ Model ↔ DB, integrasi payment gateway, notifikasi email, alur pemesanan end-to-end | 25 kasus uji (pengujian HTTP Laravel, Postman) | LULUS: 24/25 lulus (96%), 1 masalah minor (email delay) diperbaiki |
| 3 | Pengujian Fungsional (Functional Testing - Black-Box) | Memverifikasi sistem memenuhi semua kebutuhan fungsional (40 kebutuhan) dari perspektif pengguna | Semua fitur untuk Klien, Terapis, Admin, dan halaman publik menggunakan teknik equivalence partitioning, boundary value analysis, use case testing | 150+ kasus uji manual (berbagai browser dan perangkat) | LULUS (setelah perbaikan): 150/150 lulus (100%). Bug ditemukan: 25 total (2 kritis, 8 mayor, 15 minor) - semua diperbaiki |
| 4 | Pengujian Kegunaan (Usability Testing) | Mengevaluasi UI/UX, mengukur kemudahan penggunaan dengan System Usability Scale (SUS), mengidentifikasi masalah antarmuka | 15 skenario tugas utama untuk Klien, Terapis, dan Admin menggunakan protokol think-aloud dan analisis tugas | 18 partisipan × 15 tugas = 270 percobaan tugas, plus kuesioner SUS (10 item) | SANGAT BAIK: Skor SUS rata-rata 78,5/100 (Grade B), tingkat keberhasilan tugas 92%, waktu pada tugas sesuai target, tingkat kesalahan 6,8% |
| 5 | Pengujian Kinerja (Performance Testing) | Mengukur responsivitas, kecepatan, dan skalabilitas sistem (target: waktu muat <2 detik, tangani 50 pengguna simultan) | Load testing, stress testing, spike testing. Metrik: waktu muat halaman, TTFB, waktu kueri DB, pengguna bersamaan | Simulasi 50-100 pengguna virtual, profil kueri DB, pengukuran waktu muat 60+ halaman menggunakan GTmetrix, Lighthouse, JMeter | LULUS: Waktu muat rata-rata 1,8 detik, TTFB 450ms, tangani 50 pengguna (0% error), skor Lighthouse 88/100, rata-rata waktu kueri DB 85ms |
| 6 | Pengujian Keamanan (Security Testing) | Mengidentifikasi kerentanan, memastikan perlindungan data, mitigasi risiko OWASP Top 10, validasi kepatuhan UU PDP | OWASP Top 10 (2021), SQL injection, XSS, CSRF, session hijacking, brute force, file upload vulnerabilities | 73 skenario serangan menggunakan OWASP ZAP, Burp Suite, SQL Map, Laravel Security Checker | AMAN: 0 kerentanan kritis/tinggi, 2 sedang (diperbaiki), 5 rendah (prioritas rendah). Semua OWASP Top 10 dimitigasi |
| 7 | Pengujian Penerimaan Pengguna (User Acceptance Testing - UAT) | Validasi sistem memenuhi kebutuhan bisnis, mendapatkan persetujuan formal untuk peluncuran dari pemangku kepentingan | Skenario bisnis real-world untuk Admin, Terapis, Klien. Kriteria penerimaan: 90% kebutuhan fungsional terpenuhi (36/40 minimum) | 40 kebutuhan fungsional dipetakan ke kasus uji, diuji oleh 11 pemangku kepentingan nyata (Pemilik, Terapis, Admin, Klien) | DISETUJUI: 36/40 kebutuhan terpenuhi (90%), 4 kebutuhan ditunda ke Fase 2, kepuasan 9/10, 0 masalah kritis, persetujuan formal ditandatangani 24 Nov 2024 |

**Ringkasan Pengujian:**

| Fase Pengujian | Kasus Uji | Tingkat Kelulusan | Masalah Kritis | Status | Durasi |
|---------------|-----------|-------------------|----------------|--------|--------|
| Unit | 30 | 100% | 0 | Lulus | 2 minggu |
| Integrasi | 25 | 96% | 0 | Lulus | 3 hari |
| Fungsional | 150 | 100% (setelah perbaikan) | 2 (diperbaiki) | Lulus | 7 hari |
| Kegunaan | 270 percobaan | 92% keberhasilan | 0 | Lulus (SUS: 78,5) | 6 hari |
| Kinerja | ~20 skenario | 100% | 0 | Lulus | 5 hari |
| Keamanan | 73 skenario | 100% diblokir | 0 | Lulus | 5 hari |
| UAT | 36 kebutuhan | 90% | 0 (2 mayor diperbaiki) | Disetujui | 3 hari |
| **TOTAL** | **594+ Kasus Uji** | **~95%** | **2 Kritis (Diperbaiki)** | **SIAP PRODUKSI** | **14 hari** |

---
