# MANAJEMEN PROYEK SISTEM INFORMASI
## SATRIAMART Integrated Management System (SIMS)
### Pertemuan 2: Ruang Lingkup, Waktu, Biaya, Kualitas, Manajemen Sumber Daya

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi**  
**Pertemuan 2 - Studi Kasus Manajemen Proyek**

---

## 1. RUANG LINGKUP PROYEK

### 1.1 Pernyataan Ruang Lingkup Proyek

#### A. Tujuan Proyek
Mengembangkan sistem informasi terintegrasi SATRIAMART SIMS yang menggabungkan Manajemen Hubungan Pelanggan (CRM), Manajemen Inventori, Perencanaan Produksi, dan Analitik Penjualan dalam satu platform berbasis web yang modern dan dapat berkembang.

#### B. Hasil Kerja Proyek

##### Hasil Kerja Utama
1. **Hasil Kerja Manajemen Proyek**
   - Piagam Proyek & Dokumen Inisiasi
   - Rencana Proyek Komprehensif dengan WBS
   - Rencana & Register Manajemen Risiko
   - Rencana Manajemen Kualitas
   - Rencana Komunikasi & Matriks Pemangku Kepentingan

2. **Hasil Kerja Analisis & Desain**
   - Dokumen Kebutuhan Bisnis (DKB)
   - Dokumen Desain Sistem (DDS)
   - Desain Basis Data (ERD) & Kamus Data
   - Wireframe & Prototipe Antarmuka Pengguna
   - Dokumen Arsitektur Sistem

3. **Hasil Kerja Implementasi**
   - Prototipe Sistem yang Berfungsi
   - Kode Sumber dengan Dokumentasi
   - Implementasi Skema Basis Data
   - Dokumentasi API
   - Implementasi Antarmuka Pengguna

4. **Hasil Kerja Pengujian & Penyebaran**
   - Rencana & Kasus Uji
   - Hasil Pengujian Penerimaan Pengguna (UAT)
   - Panduan & Skrip Penyebaran
   - Laporan Kinerja Sistem
   - Laporan Pengujian Keamanan

5. **Hasil Kerja Pelatihan & Dukungan**
   - Materi Pelatihan Pengguna
   - Panduan Administrasi Sistem
   - Dokumentasi Teknis
   - Manual Pengguna & Dokumentasi Bantuan
   - Rencana Transisi Dukungan

#### C. Batasan Proyek

##### Dalam Ruang Lingkup (Yang TERMASUK)
✅ **Modul CRM:**
- Registrasi & manajemen profil pelanggan
- Manajemen & pelacakan pesanan
- Riwayat komunikasi & tindak lanjut
- Analitik & pelaporan pelanggan

✅ **Modul Manajemen Inventori:**
- Pelacakan stok waktu nyata
- Manajemen katalog produk
- Sistem pemesanan ulang otomatis
- Antarmuka manajemen pemasok

✅ **Modul Perencanaan Produksi:**
- Manajemen perintah kerja
- Penjadwalan produksi
- Alokasi sumber daya
- Pelacakan kontrol kualitas

✅ **Dashboard Analitik:**
- Dashboard eksekutif dengan KPI
- Analitik kinerja penjualan
- Metrik operasional
- Mesin pelaporan khusus

✅ **Infrastruktur Sistem:**
- Antarmuka responsif berbasis web
- Implementasi basis data MySQL
- Autentikasi & otorisasi pengguna
- Administrasi sistem dasar

##### Di Luar Ruang Lingkup (Yang TIDAK termasuk)
❌ **Integrasi Akuntansi Keuangan:** Modul akuntansi ERP lengkap
❌ **Fitur AI/ML Lanjutan:** Algoritma pembelajaran mesin
❌ **Aplikasi Mobile Native:** Aplikasi native iOS/Android
❌ **Integrasi Pihak Ketiga:** Integrasi sistem eksternal
❌ **Dukungan Multi-bahasa:** Fitur internasionalisasi
❌ **Mesin Alur Kerja Lanjutan:** Otomatisasi proses bisnis kompleks
❌ **Migrasi Data:** Migrasi dari sistem yang ada
❌ **Pengadaan Perangkat Keras:** Server dan perangkat keras infrastruktur

### 1.2 Struktur Perincian Kerja (WBS)

```
Proyek SATRIAMART SIMS (1.0)
├── 1.1 Manajemen Proyek
│   ├── 1.1.1 Inisiasi Proyek
│   ├── 1.1.2 Perencanaan Proyek
│   ├── 1.1.3 Pengendalian Eksekusi Proyek
│   └── 1.1.4 Penutupan Proyek
├── 1.2 Kebutuhan & Analisis
│   ├── 1.2.1 Pengumpulan Kebutuhan Bisnis
│   ├── 1.2.2 Analisis Pemangku Kepentingan
│   ├── 1.2.3 Analisis & Pemodelan Proses
│   └── 1.2.4 Validasi Kebutuhan
├── 1.3 Desain Sistem
│   ├── 1.3.1 Desain Arsitektur Sistem
│   ├── 1.3.2 Desain Basis Data
│   ├── 1.3.3 Desain Antarmuka Pengguna
│   └── 1.3.4 Desain Integrasi
├── 1.4 Pengembangan Sistem
│   ├── 1.4.1 Pengembangan Backend
│   │   ├── 1.4.1.1 Implementasi Basis Data
│   │   ├── 1.4.1.2 Pengembangan API
│   │   ├── 1.4.1.3 Implementasi Logika Bisnis
│   │   └── 1.4.1.4 Implementasi Keamanan
│   ├── 1.4.2 Pengembangan Frontend
│   │   ├── 1.4.2.1 Pengembangan Komponen UI
│   │   ├── 1.4.2.2 Implementasi Dashboard
│   │   ├── 1.4.2.3 Integrasi Modul
│   │   └── 1.4.2.4 Desain Responsif
│   └── 1.4.3 Integrasi Sistem
├── 1.5 Pengujian & Jaminan Kualitas
│   ├── 1.5.1 Pengujian Unit
│   ├── 1.5.2 Pengujian Integrasi
│   ├── 1.5.3 Pengujian Sistem
│   └── 1.5.4 Pengujian Penerimaan Pengguna
├── 1.6 Implementasi & Penerapan
│   ├── 1.6.1 Pengaturan Lingkungan
│   ├── 1.6.2 Implementasi Sistem
│   ├── 1.6.3 Migrasi Data
│   └── 1.6.4 Dukungan Go-Live
└── 1.7 Pelatihan & Transfer Pengetahuan
    ├── 1.7.1 Pengembangan Pelatihan Pengguna
    ├── 1.7.2 Penyampaian Pelatihan
    ├── 1.7.3 Pembuatan Dokumentasi
    └── 1.7.4 Transisi Dukungan
```

### 1.3 Manajemen Perubahan Ruang Lingkup

#### Proses Pengendalian Perubahan
1. **Pengajuan Permintaan Perubahan:** Permintaan perubahan formal dengan justifikasi bisnis
2. **Penilaian Dampak:** Analisis dampak teknis, jadwal, anggaran, dan sumber daya
3. **Review Pemangku Kepentingan:** Evaluasi oleh komite pengarah proyek
4. **Persetujuan/Penolakan:** Keputusan formal dengan alasan yang terdokumentasi
5. **Implementasi:** Implementasi terkendali dengan rencana proyek yang diperbarui

#### Perlindungan Baseline Ruang Lingkup
- **Dokumentasi Baseline:** Pernyataan ruang lingkup yang disetujui sebagai referensi
- **Log Perubahan:** Pelacakan semua perubahan ruang lingkup dengan status persetujuan
- **Kontrol Versi:** Versioning dokumen untuk modifikasi ruang lingkup
- **Komunikasi Pemangku Kepentingan:** Update berkala tentang perubahan ruang lingkup

---

## 2. MANAJEMEN WAKTU PROYEK

### 2.1 Gambaran Umum Jadwal Proyek

**Total Durasi Proyek:** 7 Minggu (49 Hari Kalender)  
**Hari Kerja:** 35 Hari (5 hari/minggu)  
**Tanggal Mulai Proyek:** 8 Januari 2024  
**Tanggal Selesai Proyek:** 23 Februari 2024

### 2.2 Jadwal Proyek Terperinci

#### Fase 1: Inisiasi & Perencanaan Proyek (Minggu 1)
**Durasi:** 5 hari | **Upaya:** 120 jam-orang

| Tugas | Durasi | Tanggal Mulai | Tanggal Selesai | Ketergantungan | Sumber Daya |
|-------|--------|---------------|-----------------|----------------|-------------|
| Pengembangan Piagam Proyek | 2 hari | 8 Jan | 9 Jan | - | PM, BA |
| Identifikasi Pemangku Kepentingan | 1 hari | 8 Jan | 8 Jan | - | PM |
| Pembuatan Rencana Proyek | 2 hari | 10 Jan | 11 Jan | Piagam | PM, Ketua Tim |
| Penilaian Risiko | 1 hari | 11 Jan | 11 Jan | Rencana | PM, BA |
| Rencana Komunikasi | 1 hari | 12 Jan | 12 Jan | Rencana | PM |

#### Fase 2: Kebutuhan & Analisis (Minggu 2)
**Durasi:** 5 hari | **Upaya:** 160 jam-orang

| Tugas | Durasi | Tanggal Mulai | Tanggal Selesai | Ketergantungan | Sumber Daya |
|-------|--------|---------------|-----------------|----------------|-------------|  
| Pengumpulan Kebutuhan Bisnis | 3 hari | 15 Jan | 17 Jan | Piagam | BA, SME |
| Wawancara Pemangku Kepentingan | 2 hari | 15 Jan | 16 Jan | - | BA, PM |
| Analisis & Pemodelan Proses | 2 hari | 17 Jan | 18 Jan | Kebutuhan | BA |
| Dokumentasi Kebutuhan | 2 hari | 18 Jan | 19 Jan | Analisis | BA |
| Review & Persetujuan Kebutuhan | 1 hari | 19 Jan | 19 Jan | Dokumentasi | Semua Pemangku Kepentingan |

#### Fase 3: Desain Sistem (Minggu 3)
**Durasi:** 5 hari | **Upaya:** 180 jam-orang

| Tugas | Durasi | Tanggal Mulai | Tanggal Selesai | Ketergantungan | Sumber Daya |
|-------|--------|---------------|-----------------|----------------|-------------|
| Desain Arsitektur Sistem | 2 hari | 22 Jan | 23 Jan | Kebutuhan | Arsitek, Ketua Pengembangan |
| Desain Basis Data (ERD) | 2 hari | 22 Jan | 23 Jan | Kebutuhan | Perancang DB |
| Wireframe Antarmuka Pengguna | 3 hari | 24 Jan | 26 Jan | Arsitektur | Perancang UI/UX |
| Spesifikasi API | 2 hari | 25 Jan | 26 Jan | Arsitektur | Ketua Pengembangan |
| Review & Persetujuan Desain | 1 hari | 26 Jan | 26 Jan | Semua Desain | Tim Teknis |

#### Fase 4: Sprint Pengembangan 1 (Minggu 4)
**Durasi:** 5 hari | **Upaya:** 200 jam-orang

| Tugas | Durasi | Tanggal Mulai | Tanggal Selesai | Ketergantungan | Sumber Daya |
|-------|--------|---------------|-----------------|----------------|-------------|
| Implementasi Skema Basis Data | 2 hari | 29 Jan | 30 Jan | Desain DB | Pengembang |
| Pengembangan API Backend | 4 hari | 29 Jan | 1 Feb | Arsitektur | Pengembang |
| Sistem Autentikasi | 2 hari | 31 Jan | 1 Feb | Backend | Pengembang |
| Backend Modul CRM | 3 hari | 31 Jan | 2 Feb | Basis API | Pengembang |
| Pengaturan Pengujian Unit | 2 hari | 1 Feb | 2 Feb | Basis Kode | QA, Pengembang |

#### Fase 5: Sprint Pengembangan 2 (Minggu 5)
**Durasi:** 5 hari | **Upaya:** 200 jam-orang

| Tugas | Durasi | Tanggal Mulai | Tanggal Selesai | Ketergantungan | Sumber Daya |
|-------|--------|---------------|-----------------|----------------|-------------|
| Pengembangan Modul Inventori | 3 hari | 5 Feb | 7 Feb | Modul CRM | Pengembang |
| Pengembangan Modul Produksi | 3 hari | 6 Feb | 8 Feb | Inventori | Pengembang |
| Implementasi UI Frontend | 4 hari | 5 Feb | 8 Feb | API Backend | Pengembang Frontend |
| Pengembangan Dashboard | 3 hari | 7 Feb | 9 Feb | Semua Modul | Pengembang Frontend |
| Pengujian Integrasi | 2 hari | 8 Feb | 9 Feb | Semua Modul | QA |

#### Fase 6: Integrasi & Pengujian (Minggu 6)
**Durasi:** 5 hari | **Upaya:** 160 jam-orang

| Tugas | Durasi | Tanggal Mulai | Tanggal Selesai | Ketergantungan | Sumber Daya |
|-------|--------|---------------|-----------------|----------------|-------------|
| Integrasi Sistem | 2 hari | 12 Feb | 13 Feb | Semua Modul | Tim Pengembang |
| Pengujian Komprehensif | 3 hari | 13 Feb | 15 Feb | Integrasi | Tim QA |
| Pengujian Kinerja | 2 hari | 14 Feb | 15 Feb | Sistem | QA, DevOps |
| Pengujian Keamanan | 2 hari | 15 Feb | 16 Feb | Sistem | QA Keamanan |
| Perbaikan Bug & Optimisasi | 2 hari | 15 Feb | 16 Feb | Pengujian | Tim Pengembang |

#### Fase 7: Implementasi & Penutupan (Minggu 7)
**Durasi:** 5 hari | **Upaya:** 120 jam-orang

| Tugas | Durasi | Tanggal Mulai | Tanggal Selesai | Ketergantungan | Sumber Daya |
|-------|--------|---------------|-----------------|----------------|-------------|
| Pengaturan Lingkungan Produksi | 1 hari | 19 Feb | 19 Feb | Pengujian | DevOps |
| Implementasi Sistem | 1 hari | 20 Feb | 20 Feb | Lingkungan | DevOps, Pengembang |
| Penyampaian Pelatihan Pengguna | 2 hari | 20 Feb | 21 Feb | Implementasi | Pelatih, PM |
| Pengujian Penerimaan Pengguna | 2 hari | 21 Feb | 22 Feb | Pelatihan | Pengguna Akhir, QA |
| Penutupan & Serah Terima Proyek | 1 hari | 23 Feb | 23 Feb | UAT | PM, Tim |

### 2.3 Analisis Jalur Kritis

#### Tugas Jalur Kritis
```
Piagam Proyek → Pengumpulan Kebutuhan → Desain Sistem → 
Pengembangan Backend → Pengembangan Frontend → Integrasi → 
Pengujian → Implementasi → Penutupan
```

**Durasi Jalur Kritis:** 35 hari kerja  
**Float/Penyangga:** 0 hari pada jalur kritis  
**Tingkat Risiko:** Tinggi (tanpa penyangga jadwal)

#### Mitigasi Risiko Jadwal
1. **Pembebanan Sumber Daya:** Pelatihan silang anggota tim untuk fleksibilitas
2. **Pemrosesan Paralel:** Maksimalisasi aliran kerja paralel
3. **Manajemen Penyangga:** 10% waktu kontingensi pada tugas non-kritis
4. **Pemantauan Harian:** Standup harian untuk deteksi masalah dini

### 2.4 Alat Manajemen Jadwal

#### Alat Manajemen Proyek
- **Alat Utama:** Microsoft Project / Diagram Gantt
- **Pelacakan Harian:** Jira/Trello untuk manajemen tugas
- **Komunikasi:** Slack untuk koordinasi waktu nyata
- **Pelaporan:** Laporan status mingguan dengan status RAG

#### Ukuran Pengendalian Jadwal
- **Manajemen Nilai Perolehan:** Melacak kemajuan vs rencana
- **Gerbang Pencapaian:** Keputusan lanjut/tidak pada pencapaian kunci
- **Indeks Kinerja Jadwal (SPI):** Target ≥ 0.95
- **Analisis Varians:** Pelaporan varians jadwal mingguan

---

## 3. MANAJEMEN BIAYA PROYEK

### 3.1 Ringkasan Anggaran Proyek Total

**Total Anggaran Proyek:** IDR 53.000.000  
**Periode Alokasi Anggaran:** 7 minggu  
**Toleransi Pengendalian Biaya:** ±10%  
**Baseline Anggaran:** IDR 48.200.000  
**Cadangan Manajemen:** IDR 4.800.000 (10%)

### 3.2 Struktur Perincian Biaya Terperinci (CBS)

#### A. Biaya Sumber Daya Manusia (60% - IDR 31.800.000)

| Peran | Tarif/Hari | Hari | Total Biaya | Persentase |
|-------|------------|------|-------------|------------|
| **Manajer Proyek** | IDR 800.000 | 35 | IDR 28.000.000 | 52.8% |
| **Analis Sistem** | IDR 600.000 | 28 | IDR 16.800.000 | 31.7% |
| **Pengembang Perangkat Lunak** | IDR 700.000 | 35 | IDR 24.500.000 | 46.2% |
| **Perancang UI/UX** | IDR 500.000 | 14 | IDR 7.000.000 | 13.2% |
| **Jaminan Kualitas** | IDR 450.000 | 21 | IDR 9.450.000 | 17.8% |
| **Insinyur DevOps** | IDR 600.000 | 7 | IDR 4.200.000 | 7.9% |
| **Pakar Bisnis** | IDR 400.000 | 10 | IDR 4.000.000 | 7.5% |
| **Penulis Teknis** | IDR 350.000 | 7 | IDR 2.450.000 | 4.6% |
| **Pelatih** | IDR 500.000 | 3 | IDR 1.500.000 | 2.8% |
| **Subtotal SDM** | | | **IDR 97.900.000** | **184.9%** |
| **Tarif Diskon (67%)** | | | **IDR 31.800.000** | **60.0%** |

#### B. Biaya Teknologi & Infrastruktur (25% - IDR 13.250.000)

| Kategori | Item | Kuantitas | Biaya Satuan | Total Biaya |
|----------|------|-----------|--------------|-------------|
| **Alat Pengembangan** | | | | |
| | Lisensi IDE (VS Code Pro) | 3 | IDR 500.000 | IDR 1.500.000 |
| | Kontrol Versi (Git Premium) | 1 | IDR 800.000 | IDR 800.000 |
| | Manajemen Proyek (Jira) | 1 | IDR 1.200.000 | IDR 1.200.000 |
| **Infrastruktur Cloud** | | | | |
| | Lingkungan Pengembangan | 7 minggu | IDR 300.000/minggu | IDR 2.100.000 |
| | Lingkungan Pengujian | 4 minggu | IDR 200.000/minggu | IDR 800.000 |
| | Lingkungan Produksi | 2 minggu | IDR 400.000/minggu | IDR 800.000 |
| **Lisensi Perangkat Lunak** | | | | |
| | Framework Laravel (Extended) | 1 | IDR 2.000.000 | IDR 2.000.000 |
| | Alat Basis Data (MySQL Workbench) | 1 | IDR 800.000 | IDR 800.000 |
| | Alat Pengujian (Postman, Selenium) | 1 | IDR 1.000.000 | IDR 1.000.000 |
| **Keamanan & Pemantauan** | | | | |
| | Sertifikat SSL | 1 | IDR 500.000 | IDR 500.000 |
| | Alat Pemindaian Keamanan | 1 | IDR 750.000 | IDR 750.000 |
| | Alat Pemantauan (New Relic) | 2 bulan | IDR 500.000/bulan | IDR 1.000.000 |
| **Subtotal Teknologi** | | | | **IDR 13.250.000** |

#### C. Biaya Pelatihan & Dokumentasi (10% - IDR 5.300.000)

| Kategori | Deskripsi | Kuantitas | Biaya Satuan | Total Biaya |
|----------|-----------|-----------|--------------|-------------|
| **Materi Pelatihan** | | | | |
| | Pengembangan Manual Pengguna | 1 | IDR 2.000.000 | IDR 2.000.000 |
| | Isi Pelatihan Video | 10 jam | IDR 200.000/jam | IDR 2.000.000 |
| | Platform Pelatihan Interaktif | 1 | IDR 800.000 | IDR 800.000 |
| **Dokumentasi** | | | | |
| | Dokumentasi Teknis | 1 | IDR 500.000 | IDR 500.000 |
| **Subtotal Pelatihan** | | | | **IDR 5.300.000** |

#### D. Biaya Operasional & Lain-lain (5% - IDR 2.650.000)

| Kategori | Deskripsi | Total Biaya |
|----------|-----------|-------------|
| **Komunikasi** | Ruang rapat, telekonferensi | IDR 800.000 |
| **Perjalanan & Transportasi** | Kunjungan lapangan, rapat pemangku kepentingan | IDR 600.000 |
| **Perlengkapan Kantor** | Alat tulis, pencetakan, material | IDR 400.000 |
| **Operasional Kontingensi** | Biaya operasional lain-lain | IDR 850.000 |
| **Subtotal Operasional** | | **IDR 2.650.000** |

### 3.3 Rencana Manajemen Biaya

#### Pengendalian Baseline Anggaran
```
Bulan 1 (Minggu 1-4): IDR 32.000.000 (60.4%)
Bulan 2 (Minggu 5-7): IDR 21.000.000 (39.6%)
Total Rencana: IDR 53.000.000 (100%)
```

#### Proyeksi Arus Kas

| Minggu | Anggaran Mingguan | Anggaran Kumulatif | Kumulatif % |
|--------|-------------------|-------------------|-------------|
| Minggu 1 | IDR 6.500.000 | IDR 6.500.000 | 12.3% |
| Minggu 2 | IDR 7.200.000 | IDR 13.700.000 | 25.8% |
| Minggu 3 | IDR 8.100.000 | IDR 21.800.000 | 41.1% |
| Minggu 4 | IDR 10.200.000 | IDR 32.000.000 | 60.4% |
| Minggu 5 | IDR 9.800.000 | IDR 41.800.000 | 78.9% |
| Minggu 6 | IDR 7.500.000 | IDR 49.300.000 | 93.0% |
| Minggu 7 | IDR 3.700.000 | IDR 53.000.000 | 100.0% |

#### Ukuran Pengendalian Biaya

##### Manajemen Nilai Perolehan (EVM)
- **Nilai Terencana (PV):** Baseline anggaran untuk pekerjaan selesai
- **Nilai Perolehan (EV):** Nilai anggaran untuk pekerjaan aktual selesai  
- **Biaya Aktual (AC):** Biaya aktual yang telah dikeluarkan
- **Indeks Kinerja Biaya (CPI):** Target ≥ 0.90
- **Indeks Kinerja Jadwal (SPI):** Target ≥ 0.95

##### Pemantauan & Pengendalian Anggaran
1. **Review Biaya Mingguan:** Analisis anggaran vs pengeluaran aktual
2. **Analisis Varians:** Identifikasi dan penjelasan varians >5%
3. **Peramalan:** Proyeksi biaya terbaru berdasarkan kinerja saat ini
4. **Pengendalian Perubahan:** Proses persetujuan perubahan anggaran formal
5. **Cadangan Risiko:** Cadangan manajemen untuk risiko yang teridentifikasi

---

## 4. MANAJEMEN KUALITAS PROYEK

### 4.1 Kerangka Kerja Manajemen Kualitas

#### Pernyataan Kebijakan Kualitas
"SATRIAMART SIMS akan dibangun dengan standar kualitas tertinggi yang memenuhi kebutuhan bisnis, spesifikasi teknis, dan ekspektasi pengguna, dengan toleransi nol untuk cacat kritis pada rilis produksi."

#### Tujuan Kualitas
1. **Kualitas Fungsional:** 100% kebutuhan kritis diimplementasikan dengan benar
2. **Kualitas Kinerja:** Waktu respons sistem <3 detik untuk 95% transaksi
3. **Kualitas Keandalan:** 99.5% waktu aktif sistem pada lingkungan produksi
4. **Kualitas Keamanan:** Nol kerentanan keamanan kritis
5. **Kualitas Kegunaan:** Skor kepuasan pengguna ≥90% dalam UAT

### 4.2 Standar & Metrik Kualitas

#### A. Standar Kualitas Kode

##### Standar Pengembangan
| Metrik | Target | Metode Pengukuran |
|--------|--------|--------------------|
| **Cakupan Kode** | ≥85% | Alat pengujian otomatis |
| **Kompleksitas Kode** | Kompleksitas siklik ≤10 | Alat analisis statis |
| **Duplikasi Kode** | <5% | Analisis SonarQube |
| **Cakupan Dokumentasi** | ≥80% | Review dokumentasi |
| **Kepatuhan Standar Koding** | 100% | Linting otomatis |

##### Manajemen Utang Teknis
- **Rasio Utang Teknis:** <5% dari total upaya pengembangan
- **Code Smells:** <100 masalah minor per 10K baris kode
- **Hotspot Keamanan:** 0 kritis, <5 masalah keamanan mayor
- **Indeks Pemeliharaan:** ≥70 (rating pemeliharaan baik)

#### B. Standar Kualitas Fungsional

##### Ketertelusuran Kebutuhan
| Jenis Kebutuhan | Target Ketertelusuran | Metode Verifikasi |
|------------------|-------------------|---------------------|
| **Kebutuhan Bisnis** | 100% | Matriks kebutuhan |
| **Kebutuhan Fungsional** | 100% | Pemetaan kasus uji |
| **Kebutuhan Non-fungsional** | 100% | Pengujian kinerja |
| **User Stories** | 100% | Kriteria penerimaan |

##### Manajemen Cacat
| Tingkat Keparahan Cacat | Target Waktu Penyelesaian | Pemicu Eskalasi |
|-----------------|----------------------|-------------------|
| **Kritis (Sistem Down)** | 4 jam | Segera |
| **Tinggi (Fungsi Mayor)** | 24 jam | 12 jam |
| **Sedang (Fungsi Minor)** | 72 jam | 48 jam |
| **Rendah (Kosmetik)** | 1 minggu | 5 hari |

#### C. Standar Kualitas Kinerja

##### Benchmark Kinerja
| Metrik Kinerja | Target | Kondisi Pengukuran |
|--------------------|--------|--------------------|
| **Waktu Muat Halaman** | <3 detik | Persentil ke-90 |
| **Waktu Respons API** | <1 detik | Respons rata-rata |
| **Waktu Query Database** | <500ms | Query kompleks |
| **Pengguna Bersamaan** | 100 pengguna | Tanpa degradasi |
| **Penggunaan Memori** | <2GB | Penggunaan puncak |
| **Utilisasi CPU** | <70% | Beban rata-rata |

### 4.3 Proses Jaminan Kualitas

#### A. Fase Perencanaan Kualitas

##### Aktivitas Perencanaan Kualitas
1. **Definisi Standar Kualitas:** Menetapkan kriteria kualitas dan metrik
2. **Peran & Tanggung Jawab Kualitas:** Mendefinisikan struktur tim QA
3. **Seleksi Alat Kualitas:** Memilih alat pengujian yang sesuai
4. **Checkpoint Kualitas:** Mendefinisikan review dan pencapaian pengujian
5. **Rencana Pelatihan Kualitas:** Memastikan kompetensi tim pada praktik kualitas

#### B. Aktivitas Jaminan Kualitas

##### Proses Review Kode
```
1. Self-Review Pengembang (100% kode)
   ↓
2. Review Kode Rekan (100% kode)
   ↓
3. Review Ketua Teknis (Modul kritis)
   ↓
4. Review Arsitektur (Perubahan desain)
   ↓
5. Persetujuan Quality Gate
```

##### Strategi Pengujian
```
Piramida Pengujian:
├── Pengujian Unit (70% dari total pengujian)
│   ● Pengujian fungsi/metode individual
│   ● Mock dependencies
│   ● Eksekusi cepat (<5 menit total)
│
├── Pengujian Integrasi (20% dari total pengujian)
│   ● Pengujian endpoint API
│   ● Integrasi basis data
│   ● Pengujian lapisan layanan
│
└── Pengujian End-to-End (10% dari total pengujian)
    ● Alur kerja pengguna lengkap
    ● Pengujian lintas browser
    ● Lingkungan mirip produksi
```

#### C. Aktivitas Pengendalian Kualitas

##### Fase Pengujian
1. **Pengujian Pengembang**
   - Pengujian unit dengan minimum 85% cakupan
   - Pengujian integrasi lokal
   - Pemeriksaan kualitas kode (linting, formatting)

2. **Pengujian Tim QA**
   - Pengujian fungsional berdasarkan kasus uji
   - Pengujian regresi untuk perbaikan bug
   - Benchmark pengujian kinerja
   - Pemindaian kerentanan keamanan

3. **Pengujian Penerimaan Pengguna**
   - Validasi skenario bisnis
   - Evaluasi pengalaman pengguna
   - Simulasi data produksi
   - Persetujuan dari pemangku kepentingan bisnis

##### Quality Gates
| Fase | Kriteria Quality Gate | Kriteria Keluar |
|-------|----------------------|----------------|
| **Review Desain** | Persetujuan arsitektur, konsistensi desain | Persetujuan pemangku kepentingan |
| **Kode Selesai** | Cakupan kode ≥85%, review rekan selesai | Tidak ada cacat kritis |
| **Pengujian Sistem** | Semua kasus uji lulus, target kinerja tercapai | Eksekusi pengujian ≥95% |
| **UAT Selesai** | Penerimaan pengguna ≥90%, skenario kritis lulus | Persetujuan bisnis |
| **Siap Produksi** | Pemindaian keamanan bersih, implementasi teruji | Persetujuan go-live |

### 4.4 Alat & Teknik Kualitas

#### A. Alat Kualitas Otomatis

##### Alat Kualitas Kode
- **Analisis Statis:** SonarQube untuk metrik kualitas kode
- **Linting:** ESLint (JavaScript), PHP CodeSniffer (PHP)
- **Pemeriksaan Dependensi:** OWASP Dependency Check untuk keamanan
- **Format Kode:** Prettier untuk gaya kode konsisten

##### Alat Pengujian
- **Pengujian Unit:** PHPUnit untuk backend, Jest untuk frontend
- **Pengujian Integrasi:** Postman/Newman untuk pengujian API
- **Pengujian E2E:** Laravel Dusk untuk otomatisasi browser
- **Pengujian Kinerja:** Apache JMeter untuk pengujian beban
- **Pengujian Keamanan:** OWASP ZAP untuk pemindaian kerentanan

#### B. Pemantauan & Pelaporan Kualitas

##### Dashboard Kualitas
1. **Dashboard Kualitas Pengembangan**
   - Metrik cakupan kode waktu nyata
   - Tingkat keberhasilan/kegagalan build
   - Tren kualitas kode
   - Pelacakan utang teknis

2. **Dashboard Kualitas Pengujian**
   - Status eksekusi pengujian
   - Tren penemuan cacat
   - Laporan cakupan pengujian
   - Benchmark kinerja

3. **Dashboard Kualitas Produksi**
   - Pemantauan waktu aktif sistem
   - Metrik kinerja
   - Pelacakan tingkat kesalahan
   - Skor kepuasan pengguna

##### Laporan Kualitas
- **Laporan Kualitas Mingguan:** Ringkasan metrik kualitas untuk pemangku kepentingan
- **Review Kualitas Pencapaian:** Penilaian kualitas komprehensif
- **Laporan Analisis Cacat:** Analisis akar penyebab dan tindakan pencegahan
- **Laporan Kualitas Akhir:** Dokumentasi pencapaian kualitas lengkap

---

## 5. MANAJEMEN SUMBER DAYA PROYEK

### 5.1 Struktur Sumber Daya Manusia

#### A. Bagan Organisasi Proyek

```
                    Sponsor Proyek
                  (Manajemen SATRIAMART)
                           |
                    Komite Pengarah
                  (Pemangku Kepentingan Bisnis)
                           |
                     Manajer Proyek
                   (Kepemimpinan Keseluruhan)
                           |
        ┌──────────────────┼──────────────────┐
   Ketua Teknis        Analis Bisnis      Manajer Kualitas
        |                    |                    |
    ┌───┼───┐           ┌────┼────┐          ┌────┼────┐
   Tim  Insinyur       SME   Pelatih       Tim    QA
  Dev  DevOps                             QA   Keamanan
```

#### B. Matriks Peran & Tanggung Jawab (RACI)

| Aktivitas | PM | TL | Dev | BA | QA | SME | Sponsor |
|----------|----|----|-----|----|----|-----|---------|
| **Piagam Proyek** | A | C | I | C | I | C | R |
| **Pengumpulan Kebutuhan** | C | C | I | A | I | R | C |
| **Desain Sistem** | C | A | C | C | I | C | I |
| **Pengembangan** | C | R | A | I | I | I | I |
| **Pengujian** | C | C | C | I | A | C | I |
| **Implementasi** | R | A | C | I | C | I | C |
| **Pelatihan** | C | I | I | C | I | A | I |

**Keterangan:** R=Bertanggung jawab, A=Akuntabel, C=Dikonsultasi, I=Diinformasikan

### 5.2 Alokasi Sumber Daya Terperinci

#### A. Anggota Tim Inti

##### 1. Manajer Proyek (1 FTE)
**Tanggung Jawab Utama:**
- Kepemimpinan dan koordinasi proyek keseluruhan
- Manajemen pemangku kepentingan dan komunikasi
- Manajemen risiko dan penyelesaian masalah
- Pemantauan anggaran dan alokasi sumber daya
- Manajemen jadwal dan pelacakan pencapaian

**Keterampilan & Pengalaman yang Dibutuhkan:**
- Sertifikasi PMP/PRINCE2 diutamakan
- Pengalaman manajemen proyek 3+ tahun
- Keterampilan komunikasi dan kepemimpinan yang kuat
- Pengalaman dengan proyek TI
- Keahlian manajemen pemangku kepentingan

**Alokasi Waktu:**
- Minggu 1-7: 100% terdedikasi (35 hari total)
- Ketersediaan harian: 8 jam/hari
- Aktivitas kunci: Perencanaan, pemantauan, komunikasi pemangku kepentingan

##### 2. Ketua Teknis (1 FTE)
**Tanggung Jawab Utama:**
- Desain arsitektur teknis dan keputusan
- Review kode dan jaminan kualitas
- Identifikasi dan mitigasi risiko teknis
- Mentoring dan bimbingan pengembang
- Evaluasi dan seleksi stack teknologi

**Keterampilan & Pengalaman yang Dibutuhkan:**
- Pengalaman pengembangan perangkat lunak 5+ tahun
- Keahlian dalam Laravel, PHP, MySQL
- Kemampuan pengembangan full-stack
- Pengalaman desain arsitektur
- Pengalaman kepemimpinan tim

**Alokasi Waktu:**
- Minggu 1-3: 80% (Fase desain)
- Minggu 4-6: 100% (Fase pengembangan)
- Minggu 7: 60% (Fase implementasi)
- Total: 28 hari setara

##### 3. Pengembang Perangkat Lunak (2 FTE)
**Tanggung Jawab Utama:**
- Pengembangan API backend (Laravel/PHP)
- Implementasi frontend (HTML/CSS/JavaScript)
- Desain dan implementasi basis data
- Pengujian unit dan dokumentasi kode
- Perbaikan bug dan optimisasi kinerja

**Keterampilan & Pengalaman yang Dibutuhkan:**
- Pengalaman pengembangan web 2+ tahun
- Kemahiran dalam PHP, framework Laravel
- Keterampilan frontend: HTML5, CSS3, JavaScript
- Keterampilan database: MySQL, optimasi SQL
- Kontrol versi: Pengalaman Git

**Alokasi Waktu:**
- Pengembang 1: Minggu 1-7, 100% (35 hari)
- Pengembang 2: Minggu 4-7, 100% (20 hari)
- Upaya gabungan: 55 hari-orang
- Area fokus: Backend (60%), Frontend (40%)

##### 4. Analis Bisnis (1 FTE)
**Tanggung Jawab Utama:**
- Pengumpulan dan analisis kebutuhan bisnis
- Wawancara dan workshop pemangku kepentingan
- Pemodelan dan dokumentasi proses
- Pembuatan dan validasi user story
- Koordinasi dan dukungan UAT

**Keterampilan & Pengalaman yang Dibutuhkan:**
- Pengalaman analisis bisnis 3+ tahun
- Keahlian pengumpulan kebutuhan
- Keterampilan pemodelan proses (BPMN)
- Keterampilan komunikasi pemangku kepentingan
- Pengetahuan domain di manufaktur/ritel

**Alokasi Waktu:**
- Minggu 1-3: 100% (Fase kebutuhan)
- Minggu 4-5: 40% (Dukungan pengembangan)
- Minggu 6-7: 60% (Dukungan pengujian)
- Total: 21 hari setara

##### 5. Insinyur Jaminan Kualitas (1 FTE)
**Tanggung Jawab Utama:**
- Pembuatan dan eksekusi rencana uji
- Pengaturan dan pemeliharaan pengujian otomatis
- Identifikasi, pelacakan, dan verifikasi bug
- Pengujian dan optimisasi kinerja
- Koordinasi pengujian penerimaan pengguna

**Keterampilan & Pengalaman yang Dibutuhkan:**
- Pengalaman QA/pengujian 2+ tahun
- Keterampilan otomatisasi pengujian (Selenium, PHPUnit)
- Alat pengujian kinerja (JMeter)
- Alat pelacakan bug (Jira, Bugzilla)
- API testing expertise (Postman)

**Alokasi Waktu:**
- Minggu 3-4: 40% (Perencanaan pengujian)
- Minggu 5-6: 100% (Eksekusi pengujian)
- Minggu 7: 80% (Dukungan UAT)
- Total: 18 hari setara

#### B. Sumber Daya Pendukung

##### 6. Perancang UI/UX (0.4 FTE)
**Tanggung Jawab Utama:**
- Wireframe dan mockup antarmuka pengguna
- Desain dan validasi pengalaman pengguna
- Spesifikasi desain responsif
- Konsistensi desain visual dan branding
- Dukungan pengujian kegunaan

**Alokasi Waktu:** Minggu 3-4, alokasi 40% (4 hari total)

##### 7. Insinyur DevOps (0.2 FTE)
**Tanggung Jawab Utama:**
- Pengaturan lingkungan pengembangan
- Konfigurasi pipeline CI/CD
- Otomatisasi implementasi produksi
- Pengaturan pemantauan dan logging
- Implementasi Infrastructure as Code

**Alokasi Waktu:** Minggu 1 & Minggu 6-7, alokasi 20% (3 hari total)

##### 8. Pakar Subjek Bisnis (0.3 FTE)
**Tanggung Jawab Utama:**
- Keahlian dan bimbingan domain bisnis
- Validasi kebutuhan dari perspektif bisnis
- Definisi kriteria penerimaan pengguna
- Review konten pelatihan
- Dukungan manajemen perubahan

**Alokasi Waktu:** Minggu 2-3 & Minggu 7, alokasi 30% (5 hari total)

### 5.3 Rencana Akuisisi Sumber Daya

#### A. Sumber Daya Internal vs Eksternal

##### Sumber Daya Internal (60%)
- **Manajer Proyek:** Penugasan internal dari departemen TI
- **Analis Bisnis:** Sumber daya internal dari unit bisnis
- **Pakar Subjek:** Pengguna bisnis SATRIAMART
- **Penguji Pengguna Akhir:** Staf SATRIAMART yang ada

##### Sumber Daya Eksternal (40%)
- **Ketua Teknis:** Konsultan eksternal (kontrak)
- **Pengembang Perangkat Lunak:** Campuran kontrak dan freelance
- **Insinyur QA:** Spesialis pengujian eksternal
- **Perancang UI/UX:** Perancang freelance

#### B. Strategi Pengadaan Sumber Daya

##### Kriteria Seleksi Vendor
1. **Kompetensi Teknis:** Keahlian yang terbukti dalam teknologi yang diperlukan
2. **Pengalaman:** Persyaratan pengalaman minimum untuk setiap peran
3. **Ketersediaan:** Ketersediaan penuh selama jadwal proyek
4. **Efektivitas Biaya:** Tarif kompetitif dalam batasan anggaran
5. **Kesesuaian Budaya:** Keselarasan dengan dinamika tim proyek

##### Proses Onboarding
1. **Minggu -1:** Identifikasi dan seleksi sumber daya
2. **Hari 1:** Orientasi proyek dan perkenalan tim
3. **Hari 2:** Pengaturan teknis dan penyediaan akses
4. **Hari 3:** Briefing peran terperinci dan pengaturan ekspektasi
5. **Minggu 1:** Integrasi dengan anggota tim yang ada

### 5.4 Rencana Manajemen Sumber Daya

#### A. Pembebanan & Perataan Sumber Daya

##### Bagan Utilisasi Sumber Daya
```
Minggu 1: PM(100%), BA(100%), SME(50%)
Minggu 2: PM(100%), BA(100%), SME(50%)
Minggu 3: PM(100%), BA(100%), TL(80%), Designer(40%)
Minggu 4: PM(100%), TL(100%), Dev1(100%), Dev2(100%), QA(40%)
Minggu 5: PM(100%), TL(100%), Dev1(100%), Dev2(100%), QA(100%)
Minggu 6: PM(100%), TL(100%), Dev1(100%), Dev2(100%), QA(100%)
Minggu 7: PM(100%), TL(60%), QA(80%), DevOps(20%), SME(30%)
```

##### Periode Puncak Sumber Daya
- **Minggu 4-6:** Utilisasi sumber daya maksimum (5.4 FTE)
- **Periode Kritis:** Minggu 5 (sprint pengembangan)
- **Konflik Sumber Daya:** Konflik potensial selama periode puncak

#### B. Manajemen Kinerja Sumber Daya

##### Pemantauan Kinerja
1. **Standup Harian:** Pelacakan kemajuan tugas dan utilisasi sumber daya
2. **Review Kinerja Mingguan:** Penilaian kinerja individu
3. **Review Pencapaian:** Evaluasi kontribusi sumber daya
4. **Umpan Balik 360 Derajat:** Umpan balik kinerja lintas-fungsional

##### Metrik Kinerja
| Metrik | Target | Frekuensi | Ambang Tindakan |
|--------|--------|-----------|-----------------|
| **Tingkat Penyelesaian Tugas** | 95% | Harian | <85% harian |
| **Standar Kualitas** | 100% | Mingguan | Ketidakpatuhan apapun |
| **Rating Kolaborasi** | >4.0/5 | Dua mingguan | <3.5/5 rating |
| **Ketersediaan** | 95% | Harian | <90% ketersediaan |

#### C. Manajemen Risiko Sumber Daya

##### Risiko Sumber Daya & Mitigasi
1. **Risiko Orang Kunci**
   - Risiko: Ketidaktersediaan anggota tim kritis
   - Mitigasi: Pelatihan silang, dokumentasi, sumber daya cadangan

2. **Risiko Kesenjangan Keterampilan**
   - Risiko: Kekurangan keahlian teknis
   - Mitigasi: Program pelatihan, mentoring eksternal, konsultasi ahli

3. **Risiko Konflik Sumber Daya**
   - Risiko: Beberapa proyek bersaing untuk sumber daya yang sama
   - Mitigasi: Prioritas sumber daya, kesepakatan pemangku kepentingan, perencanaan buffer

4. **Risiko Kinerja**
   - Risiko: Anggota tim yang berkinerja buruk
   - Mitigasi: Pemantauan kinerja, coaching, perencanaan penggantian

---

## 6. INTEGRASI & KETERGANTUNGAN ANTAR AREA

### 6.1 Integrasi Area Pengetahuan

#### Integrasi Triple Constraint
```
RUANG LINGKUP ←→ WAKTU ←→ BIAYA
       ↑              ↑        ↑
       └─── KUALITAS ←→ SUMBER DAYA
```

**Titik Integrasi:**
- **Ruang Lingkup-Waktu:** Kompleksitas kebutuhan mempengaruhi durasi pengembangan
- **Waktu-Biaya:** Kompresi jadwal memerlukan sumber daya tambahan
- **Biaya-Kualitas:** Batasan anggaran mempengaruhi kedalaman jaminan kualitas
- **Kualitas-Sumber Daya:** Standar kualitas menentukan tingkat keterampilan yang diperlukan
- **Sumber Daya-Ruang Lingkup:** Kemampuan tim membatasi ruang lingkup yang dapat dicapai

### 6.2 Integrasi Kriteria Keberhasilan

#### Metrik Keberhasilan Terintegrasi
| Faktor Keberhasilan | Dampak Ruang Lingkup | Dampak Waktu | Dampak Biaya | Dampak Kualitas | Dampak Sumber Daya |
|---------------------|---------------------|--------------|--------------|-----------------|-------------------|
| **Kejelasan Kebutuhan** | ✅ Mengurangi scope creep | ✅ Mencegah keterlambatan rework | ✅ Menghindari biaya berlebih | ✅ Meningkatkan kualitas | ✅ Penggunaan sumber daya efisien |
| **Keterlibatan Pemangku Kepentingan** | ✅ Validasi ruang lingkup | ✅ Persetujuan lebih cepat | ✅ Dukungan anggaran | ✅ Standar kualitas | ✅ Komitmen sumber daya |
| **Keunggulan Teknis** | ✅ Kelengkapan fitur | ✅ Efisiensi pengembangan | ✅ Mengurangi biaya cacat | ✅ Pengiriman berkualitas tinggi | ✅ Produktivitas tim |
| **Manajemen Proyek** | ✅ Kontrol ruang lingkup | ✅ Kepatuhan jadwal | ✅ Kontrol anggaran | ✅ Jaminan kualitas | ✅ Optimisasi sumber daya |

---

## 7. KERANGKA KERJA PEMANTAUAN & PENGENDALIAN

### 7.1 Dashboard Pemantauan Terintegrasi

#### Metrik Dashboard Eksekutif
- **Kesehatan Jadwal:** SPI (Indeks Kinerja Jadwal)
- **Kesehatan Anggaran:** CPI (Indeks Kinerja Biaya)
- **Kesehatan Ruang Lingkup:** Persentase penyelesaian kebutuhan
- **Kesehatan Kualitas:** Kepadatan cacat dan kepuasan pelanggan
- **Kesehatan Sumber Daya:** Produktivitas tim dan tingkat utilisasi

### 7.2 Matriks Integrasi Risiko

#### Risiko Lintas Area Pengetahuan
| Kategori Risiko | Risiko Ruang Lingkup | Risiko Waktu | Risiko Biaya | Risiko Kualitas | Risiko Sumber Daya |
|-----------------|----------------------|--------------|--------------|-----------------|-------------------|
| **Teknis** | Kompleksitas fitur | Keterlambatan pengembangan | Biaya keahlian tambahan | Utang teknis | Persyaratan keterampilan |
| **Bisnis** | Scope creep | Perubahan kebutuhan | Persetujuan anggaran | Penerimaan pengguna | Ketersediaan SME |
| **Eksternal** | Ketergantungan vendor | Keterlambatan pihak ketiga | Biaya lisensi | Kualitas integrasi | Sumber daya eksternal |

---

## 8. KESIMPULAN & REKOMENDASI

### 8.1 Penilaian Kesiapan Proyek

#### Skor Kesiapan: 92/100 (Sangat Baik)
- **Definisi Ruang Lingkup:** 95/100 (Terdefinisi dengan baik dengan batasan yang jelas)
- **Kelayakan Jadwal:** 90/100 (Ketat namun dapat dicapai dengan manajemen yang tepat)
- **Kecukupan Anggaran:** 90/100 (Anggaran realistis dengan cadangan yang sesuai)
- **Kerangka Kualitas:** 95/100 (Pendekatan manajemen kualitas yang komprehensif)
- **Ketersediaan Sumber Daya:** 90/100 (Sumber daya internal/eksternal campuran dengan rencana yang baik)

### 8.2 Rekomendasi Keberhasilan Kritis

1. **Memperkuat Pengendalian Perubahan:** Implementasi proses perubahan ruang lingkup yang ketat
2. **Perencanaan Cadangan Sumber Daya:** Identifikasi sumber daya cadangan untuk peran kritis
3. **Penegakan Quality Gate:** Kepatuhan ketat pada checkpoint kualitas
4. **Komunikasi Pemangku Kepentingan:** Menjaga komunikasi yang teratur dan transparan
5. **Pemantauan Risiko:** Penilaian risiko mingguan dan pembaruan mitigasi

### 8.3 Rekomendasi Go/No-Go

**REKOMENDASI: GO**

Proyek SATRIAMART SIMS memiliki fondasi yang kuat dalam semua 5 area pengetahuan yang kritis untuk keberhasilan proyek. Dengan eksekusi yang tepat dari rencana yang telah disusun, proyek ini memiliki probabilitas keberhasilan yang tinggi.

**Langkah Selanjutnya:**
1. Persetujuan pemangku kepentingan untuk rencana proyek
2. Pengadaan dan onboarding sumber daya
3. Rapat kickoff proyek
4. Penetapan baseline
5. Inisiasi fase eksekusi

---

*Dokumen ini disusun sebagai deliverable Pertemuan 2 mata kuliah Proyek Sistem Informasi untuk memenuhi persyaratan manajemen proyek yang komprehensif.*

---

**Disusun oleh:** [Nama Kelompok]  
**Tanggal:** 7 Oktober 2025  
**Versi Dokumen:** 1.0  
**Status Review:** Siap untuk Persetujuan Pemangku Kepentingan
