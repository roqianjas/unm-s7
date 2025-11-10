# BAB IV  
# HASIL PENELITIAN DAN PEMBAHASAN

## 4.1 Inisiasi Proyek

### 4.1.1 Latar Belakang Proyek

Proyek pengembangan Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART diinisiasi berdasarkan kebutuhan mendesak untuk mengoptimalkan operasional pusat layanan hipnoterapi dan kesehatan mental yang semakin berkembang. CUR-HEART (*Hypnotherapy & Mind Wellness Center*), sebagai salah satu pelopor dalam layanan hipnoterapi profesional di Indonesia, mengalami pertumbuhan signifikan dalam jumlah klien dan terapis sejak berdiri pada tahun 2023.

Dengan visi menjadi pusat terapi kejiwaan berbasis hipnoterapi modern dan spiritual yang terpercaya di Indonesia, CUR-HEART menyediakan enam layanan utama:

1. **Terapi Pelepasan Stres & Kecemasan** (*Stress & Anxiety Release Therapy*) - Mengatasi stres berlebih dan kecemasan yang mengganggu aktivitas sehari-hari
2. **Hipnoterapi Penyembuhan Trauma** (*Trauma Healing Hypnotherapy*) - Menghapus dampak emosional dari pengalaman traumatis masa lalu
3. **Terapi Kepercayaan Diri & Motivasi** (*Self-Confidence & Motivation Therapy*) - Meningkatkan kepercayaan diri dan semangat hidup
4. **Terapi Tidur & Relaksasi** (*Sleep & Relaxation Therapy*) - Mengatasi insomnia dan gangguan tidur dengan teknik relaksasi mendalam
5. **Terapi Pemrograman Ulang Kebiasaan** (*Habit Reprogramming Therapy*) - Mengubah kebiasaan negatif seperti merokok atau menunda pekerjaan
6. **Manajemen Fobia & Ketakutan** (*Phobia & Fear Management*) - Menangani rasa takut berlebihan terhadap situasi tertentu

---

**[GAMBAR 4.1 - Organizational Structure CUR-HEART]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT ORGANIZATION CHART DIAGRAM]                      │
│                                                             │
│   Struktur Organisasi CUR-HEART:                           │
│                                                             │
│              ┌──────────────────────┐                      │
│              │   PEMILIK/PENDIRI    │                      │
│              │   (Dr. Sarah W.)     │                      │
│              └──────────┬───────────┘                      │
│                         │                                   │
│         ┌───────────────┼───────────────┐                 │
│         │               │               │                 │
│   ┌─────┴──────┐  ┌────┴─────┐  ┌─────┴──────┐          │
│   │KEPALA       │  │MANAJER   │  │ KEUANGAN & │          │
│   │TERAPIS      │  │OPERASIONAL│  │ ADMIN      │          │
│   │(Michael A.) │  │          │  │            │          │
│   └─────┬──────┘  └────┬─────┘  └─────┬──────┘          │
│         │               │               │                 │
│    ┌────┴────┐     ┌────┴────┐    ┌────┴────┐           │
│    │TERAPIS  │     │LAYANAN  │    │STAF     │           │
│    │(5 orang)│     │PELANGGAN│    │KEUANGAN │           │
│    │         │     │(2 orang)│    │(1 orang)│           │
│    └─────────┘     └─────────┘    └─────────┘           │
│                                                             │
│   Total Tim: 10 orang                                      │
│   - 1 Pemilik/Pendiri                                      │
│   - 1 Kepala Terapis                                       │
│   - 5 Terapis                                              │
│   - 1 Manajer Operasional                                  │
│   - 2 Layanan Pelanggan/Admin                              │
│   - 1 Staf Keuangan                                        │
│                                                             │
│   Format: Bagan Organisasi PNG/JPG                         │
│   Ukuran rekomendasi: 1200x800px                           │
│   Gaya: Diagram hierarki profesional dengan foto/ikon      │
│                                                             │
│   File: assets/images/organizational-structure-curheart.png│
│   Tool: Microsoft Visio, Draw.io, PowerPoint, atau Canva  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.1: Struktur organisasi CUR-HEART menunjukkan hierarki dari Pemilik hingga staf operasional dengan total 10 anggota tim_

---

Namun, pertumbuhan ini tidak diiringi dengan sistem operasional yang memadai. Proses pemesanan yang masih manual melalui WhatsApp dan telepon, manajemen jadwal terapis menggunakan spreadsheet, serta dokumentasi sesi terapi dalam format kertas dan file Word terpisah menimbulkan berbagai ketidakefisienan yang menghambat kualitas layanan dan potensi pertumbuhan bisnis.

### 4.1.2 Permasalahan yang Dihadapi

Berdasarkan observasi lapangan dan wawancara mendalam dengan pemangku kepentingan CUR-HEART pada September 2024, teridentifikasi delapan permasalahan kritis:

**1. Tingkat Konversi Pemesanan yang Rendah (60%)**

Dari 100 pertanyaan yang masuk, hanya 60 yang berubah menjadi pemesanan aktual. Data historis menunjukkan bahwa 40% calon klien membatalkan niat mereka karena:
- Proses pemesanan yang memakan waktu (rata-rata 15-20 menit komunikasi bolak-balik)
- Harus menghubungi admin di jam kerja saja
- Tidak bisa langsung melihat ketersediaan terapis secara waktu nyata
- Informasi tidak lengkap tentang layanan dan terapis

**2. Konflik Jadwal dan Pemesanan Ganda (8-10 kasus per bulan)**

Manajemen jadwal manual menggunakan Google Calendar terpisah untuk setiap terapis menyebabkan:
- 8-10 kasus pemesanan ganda per bulan yang harus dijadwalkan ulang darurat
- Kesulitan saat terapis berhalangan mendadak (sakit, urgent matter)
- Tidak ada visibilitas terhadap total kapasitas dan okupansi
- Ketimpangan beban kerja antar terapis (beberapa *overbooked*, yang lain kurang dimanfaatkan)

**3. Waktu Dokumentasi Terapi yang Lama (15 menit per sesi)**

Terapis menghabiskan rata-rata 15 menit setelah setiap sesi untuk:
- Menulis catatan sesi secara manual di buku atau Word
- Menyimpan dan mencari file dengan konvensi penamaan yang tidak konsisten
- Kesulitan mengakses riwayat terapi klien sebelum sesi berikutnya
- Risiko kehilangan data tinggi (file rusak, dokumen hilang)

**4. Tidak Ada Data untuk Pengambilan Keputusan**

Manajemen kesulitan mendapatkan wawasan bisnis karena:
- Data tersebar di berbagai platform (WhatsApp, Excel, file fisik)
- Pembuatan laporan bulanan memakan waktu 2-3 hari kerja
- Tidak ada visibilitas terhadap KPI penting (tingkat konversi, pendapatan per layanan, utilisasi terapis)
- Keputusan bisnis masih berbasis intuisi, bukan data

**5. Pengalaman Klien yang Kurang Optimal**

Klien mengalami frustrasi karena:
- Harus selalu menghubungi admin untuk segala informasi
- Tidak ada platform untuk melacak kemajuan terapi mereka
- Tidak bisa menjadwalkan ulang atau membatalkan pemesanan secara mandiri
- Proses pembayaran manual dengan konfirmasi yang lama

**6. Beban Administratif yang Tinggi**

Admin menghabiskan 70% waktu kerja untuk:
- Menjawab pertanyaan yang sama berulang kali
- Mengelola pemesanan dan penjadwalan ulang manual
- Verifikasi pembayaran manual
- Mengompilasi data untuk pelaporan

**7. Risiko Keamanan dan Privasi**

Data klien yang sangat sensitif (riwayat trauma, masalah psikologis):
- Disimpan dalam format tidak aman (Word tidak terenkripsi, kertas fisik)
- Tidak ada kontrol akses yang tepat
- Tidak ada jejak audit
- Berpotensi melanggar UU Perlindungan Data Pribadi

**8. Hambatan Skalabilitas**

Sistem manual tidak dapat mengakomodasi pertumbuhan:
- Penambahan terapis baru memperumit koordinasi
- Tidak bisa efisien menangani volume pemesanan yang meningkat
- Sulit untuk ekspansi ke lokasi cabang baru
- Infrastruktur teknologi tidak mendukung skala

**Tabel 4.1 Analisis Masalah dengan Data Kuantitatif**

| No | Masalah | Data Kuantitatif | Dampak | Prioritas |
|----|---------|------------------|--------|-----------|
| 1 | Tingkat Konversi Pemesanan Rendah | 60% dari pertanyaan menjadi pemesanan (40% hilang) | Kehilangan potensi pendapatan Rp 20 juta/bulan | Kritis |
| 2 | Konflik Jadwal & Pemesanan Ganda | 8-10 kasus per bulan | Ketidakpuasan pelanggan, reputasi negatif | Tinggi |
| 3 | Waktu Dokumentasi Terapi Lama | 15 menit per sesi x 120 sesi/bulan = 30 jam/bulan | Inefisiensi operasional, terapis tidak produktif | Tinggi |
| 4 | Tidak Ada Data untuk Keputusan | Laporan bulanan butuh 2-3 hari kerja | Kehilangan peluang, keputusan tidak optimal | Tinggi |
| 5 | Pengalaman Klien Kurang Optimal | Tingkat retensi hanya 45% | *Churn* tinggi, kehilangan pelanggan berulang | Kritis |
| 6 | Beban Administratif Tinggi | Admin menghabiskan 70% waktu untuk tugas manual | Biaya tinggi, tidak dapat diskalakan | Tinggi |
| 7 | Risiko Keamanan & Privasi | Data sensitif tersimpan tidak terenkripsi | Risiko legal, pelanggaran UU PDP | Kritis |
| 8 | Hambatan Skalabilitas | Sistem manual tidak mendukung pertumbuhan >20 terapis | Tidak bisa ekspansi, kehilangan pangsa pasar | Sedang |

**Sumber:** Observasi lapangan dan wawancara dengan Manajemen CUR-HEART, September 2024

---

**[GAMBAR 4.2 - Current Business Process (As-Is)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN DIAGRAM ALUR PROSES BISNIS AS-IS]              │
│                                                             │
│   PROSES PEMESANAN & TERAPI YANG ADA (MANUAL):             │
│                                                             │
│   KLIEN                  ADMIN              TERAPIS         │
│     │                       │                    │          │
│     │ 1. Pertanyaan via     │                    │          │
│     │    WhatsApp/Telepon   │                    │          │
│     ├──────────────────────>│                    │          │
│     │                       │ 2. Cek jadwal      │          │
│     │                       │    manual          │          │
│     │                       ├───────────────────>│          │
│     │                       │<───────────────────┤          │
│     │                       │ 3. Konfirmasi slot │          │
│     │<──────────────────────┤                    │          │
│     │ 4. Transfer pembayaran│                    │          │
│     ├──────────────────────>│                    │          │
│     │                       │ 5. Verifikasi manual│         │
│     │                       │    (jam/hari)      │          │
│     │<──────────────────────┤                    │          │
│     │ 6. Hadiri sesi        │                    │          │
│     ├───────────────────────┼───────────────────>│          │
│     │                       │                    │ 7. Laksanakan│
│     │                       │                    │   terapi  │
│     │                       │                    │ 8. Tulis  │
│     │                       │                    │   catatan │
│     │                       │                    │   manual  │
│     │                       │                    │   (15 mnt)│
│     │                       │<───────────────────┤          │
│     │                       │ 9. Perbarui Excel  │          │
│     │                       │    (akhir hari)    │          │
│     ▼                       ▼                    ▼          │
│                                                             │
│   Titik Masalah:                                            │
│   ❌ 15-20 menit/pemesanan                                  │
│   ❌ 8-10 pemesanan ganda/bulan                             │
│   ❌ Verifikasi pembayaran manual (jam/hari)                │
│   ❌ 15 menit dokumentasi/sesi                              │
│   ❌ Tidak ada data waktu nyata                             │
│   ❌ 40% kehilangan konversi                                │
│                                                             │
│   Total Waktu Proses: ~45 menit per pemesanan              │
│   Tingkat Error: 8-10% (konflik penjadwalan)               │
│                                                             │
│   Format: Diagram Alur Proses PNG/JPG                      │
│   Ukuran rekomendasi: 1400x1000px                          │
│   Gaya: Diagram swimlane dengan titik masalah ditandai     │
│                                                             │
│   File: assets/images/as-is-business-process.png           │
│   Tool: Draw.io, Lucidchart, Microsoft Visio               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.2: Proses bisnis saat ini (As-Is) menunjukkan alur pemesanan manual dengan total waktu ~45 menit per pemesanan dan tingkat error 8-10%_

---

### 4.1.3 Tujuan Proyek

Proyek ini memiliki tujuan utama dan tujuan khusus sebagai berikut:

**Tujuan Utama:**

Mengembangkan sistem informasi manajemen pemesanan dan terapi berbasis web yang terintegrasi, efisien, ramah pengguna, dan aman untuk meningkatkan efisiensi operasional CUR-HEART minimal 40%, meningkatkan tingkat konversi pemesanan dari 60% menjadi 85%, dan memberikan fondasi untuk skalabilitas bisnis jangka panjang.

**Tujuan Khusus:**

1. Mengotomatisasi proses pemesanan dengan alur multi-langkah yang intuitif, memungkinkan klien memesan 24/7
2. Mengintegrasikan manajemen jadwal terapis untuk eliminasi konflik penjadwalan
3. Menyediakan sistem dokumentasi terapi terstruktur yang menghemat waktu hingga 60%
4. Memfasilitasi pelacakan kemajuan klien dengan visualisasi data yang bermakna
5. Menyediakan dasbor intelijen bisnis untuk pengambilan keputusan berbasis data
6. Mengimplementasikan sistem pembayaran digital terintegrasi
7. Menjamin keamanan data klien sesuai kepatuhan UU PDP
8. Meningkatkan pengalaman pengguna untuk semua pemangku kepentingan (admin, terapis, klien)

### 4.1.4 Analisis Pemangku Kepentingan

Analisis pemangku kepentingan mengidentifikasi pihak-pihak yang terlibat dan berkepentingan dalam proyek:

**Tabel 4.2 Matriks Analisis Pemangku Kepentingan**

| Pemangku Kepentingan | Peran | Kategori | Tingkat Kepentingan | Kekuatan/Pengaruh | Kebutuhan Utama | Strategi Keterlibatan | Frekuensi Komunikasi |
|-------------|------|----------|----------------|-----------------|-----------------|---------------------|---------------------|
| Pemilik CUR-HEART | Pengambil Keputusan, Sponsor | Primer | Sangat Tinggi | Sangat Tinggi | ROI, pertumbuhan, keunggulan kompetitif | Kelola Erat - Update mingguan, persetujuan tonggak | Mingguan |
| Terapis (5 orang) | Pengguna Utama | Primer | Sangat Tinggi | Tinggi | Kemudahan penggunaan, penghematan waktu, manajemen klien lebih baik | Kelola Erat - Lokakarya kebutuhan, UAT | Dua minggu sekali |
| Staf Admin (2 orang) | Operator Sistem | Primer | Tinggi | Tinggi | Pengurangan beban kerja, efisiensi | Kelola Erat - Pemetaan proses, pelatihan | Mingguan |
| Klien Aktif | Pengguna Akhir | Primer | Tinggi | Sedang | Kenyamanan, privasi, UX yang baik | Tetap Informasi - Riset pengguna, survei umpan balik | Bulanan |
| Dosen Pembimbing | Pembimbing Akademik | Sekunder | Tinggi | Tinggi | Kualitas, hasil pembelajaran, dokumentasi | Jaga Kepuasan - Konsultasi mingguan, tinjauan | Mingguan |
| Tim Pengembang (3 orang) | Tim Proyek | Internal | Sangat Tinggi | Sangat Tinggi | Penyampaian sukses, pembelajaran, portofolio | Kelola Erat - Standup harian, kolaborasi | Harian |
| Universitas Nusa Mandiri | Institusi Akademik | Sekunder | Sedang | Sedang | Prestasi mahasiswa, kolaborasi industri | Tetap Informasi - Laporan kemajuan, presentasi | Bulanan |

**Sumber:** Analisis Pemangku Kepentingan CUR-HEART, September 2024

**Matriks Kekuatan-Kepentingan Pemangku Kepentingan:**

```
Kekuatan Tinggi
    │
    │   [Pemilik]      [Dosen Pembimbing]
    │   [Terapis]      [Tim Pengembang]
    │
    │   [Admin]
    │
    │   [Klien]        [Universitas]
    │
    └─────────────────────────────────────► Kepentingan Tinggi
Kekuatan Rendah                                    
```

**Rencana Keterlibatan Pemangku Kepentingan:**

- **Kelola Erat:** Pemilik, Terapis, Tim Pengembang (Kekuatan Tinggi, Kepentingan Tinggi)
- **Jaga Kepuasan:** Dosen Pembimbing (Kekuatan Tinggi, Kepentingan Sedang)
- **Tetap Informasi:** Staf Admin, Klien (Kekuatan Sedang, Kepentingan Tinggi)
- **Pantau:** Universitas (Kekuatan Rendah, Kepentingan Sedang)

---

**[GAMBAR 4.3 - Stakeholder Power-Interest Matrix]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT POWER-INTEREST MATRIX DIAGRAM]                   │
│                                                             │
│   STAKEHOLDER ANALYSIS - POWER vs INTEREST MATRIX          │
│                                                             │
│   HIGH POWER                                                │
│        │                                                    │
│        │  MANAGE CLOSELY      │  KEEP SATISFIED            │
│        │  ┌────────────────┐  │  ┌───────────────┐        │
│        │  │ • Owner        │  │  │ • Dosen       │        │
│        │  │ • Terapis (5)  │  │  │   Pembimbing  │        │
│        │  │ • Tim Dev (3)  │  │  │               │        │
│        │  └────────────────┘  │  └───────────────┘        │
│        │──────────────────────┼────────────────────        │
│        │  MONITOR            │  KEEP INFORMED             │
│        │  ┌────────────────┐  │  ┌───────────────┐        │
│        │  │ • (None)       │  │  │ • Admin (2)   │        │
│        │  │                │  │  │ • Klien       │        │
│        │  │                │  │  │ • Universitas │        │
│        │  └────────────────┘  │  └───────────────┘        │
│   LOW POWER                                                 │
│        └───────────────────────┼────────────────────>       │
│              LOW INTEREST         HIGH INTEREST            │
│                                                             │
│   Quadrant Details:                                         │
│   ┌─ MANAGE CLOSELY (7 stakeholders):                      │
│   │  High engagement, weekly/daily communication           │
│   │  Critical untuk project success                        │
│   │                                                         │
│   ┌─ KEEP SATISFIED (1 stakeholder):                       │
│   │  Regular updates, involve in key decisions             │
│   │  Academic oversight & quality assurance                │
│   │                                                         │
│   ┌─ KEEP INFORMED (3 stakeholder groups):                 │
│   │  Regular communication, feedback loops                 │
│   │  Important users & beneficiaries                       │
│   │                                                         │
│   └─ MONITOR (0 stakeholders):                             │
│      Minimal communication, periodic updates               │
│                                                             │
│   Total Stakeholders: 11 groups, 23 individuals            │
│                                                             │
│   Format: 2x2 Matrix Diagram PNG/JPG                       │
│   Recommended size: 1200x1000px                            │
│   Style: Quadrant matrix dengan stakeholder positioning    │
│                                                             │
│   File: assets/images/stakeholder-power-interest-matrix.png│
│   Tool: PowerPoint, Canva, Draw.io, atau Excel            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.3: Stakeholder Power-Interest Matrix menunjukkan positioning 11 stakeholder groups untuk strategi engagement yang tepat_

---

### 4.1.5 Piagam Proyek (*Project Charter*)

**Piagam Proyek - Sistem Informasi CUR-HEART**

**Tabel 4.3 Piagam Proyek - Ringkasan Eksekutif**

| Elemen | Deskripsi |
|--------|-----------|
| **Judul Proyek** | Pengembangan Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART Berbasis Web |
| **Manajer Proyek** | Roki Anjas (NIM: 11250066) |
| **Sponsor Proyek** | Manajemen CUR-HEART |
| **Pembimbing Akademik** | Rani Irma Handayani, M.Kom |
| **Tim Pengembang** | 3 pengembang (*Full Stack*) |
| **Tanggal Mulai Proyek** | 16 September 2024 |
| **Target Penyelesaian** | 1 Desember 2024 (11 minggu / 77 hari kerja) |
| **Total Anggaran** | Rp 5.000.000 |
| **Metodologi** | *Waterfall* SDLC (6 fase) |
| **Pengguna Target** | 3 peran: Admin, Terapis (5 orang), Klien (100+ existing) |
| **Platform** | Aplikasi berbasis web (*responsive design*) |
| **Teknologi** | Laravel 10, PHP 8.2, MySQL 8.0, Tailwind CSS 3.0 |
| **Tujuan Utama** | Meningkatkan efisiensi operasional min 40%, tingkat konversi dari 60% ke 85% |
| **Hasil Kunci** | 1) Aplikasi web siap produksi<br>2) Kode sumber & dokumentasi<br>3) Laporan *capstone* (80-100 hal)<br>4) Materi pelatihan<br>5) Presentasi & video demo |
| **Kriteria Keberhasilan** | 1) 95%+ kebutuhan fungsional terimplementasi<br>2) Skor SUS ≥ 80/100<br>3) UAT lulus<br>4) Tidak ada *bug* kritis<br>5) Tingkat konversi ≥ 75% |
| **Batasan Kunci** | 1) Waktu: 11 minggu ketat<br>2) Anggaran: Rp 5 juta<br>3) Tim: 3 pengembang<br>4) Kebutuhan akademik: Harus gunakan Laravel |

**Otorisasi Proyek:**

| Name | Role | Signature | Date |
|------|------|-----------|------|
**Otorisasi Proyek:**

| Nama | Peran | Tanda Tangan | Tanggal |
|------|------|-----------|------|
| [Nama Pemilik] | Sponsor Proyek | _____________ | ___/___/___ |
| Roki Anjas | Manajer Proyek | _____________ | ___/___/___ |
| Rani Irma Handayani, M.Kom | Pembimbing Akademik | _____________ | ___/___/___ |

**Tujuan Proyek:**
1. Mengembangkan sistem manajemen pemesanan dan terapi berbasis web yang fungsional penuh
2. Mencapai minimal 95% kepatuhan kebutuhan fungsional
3. Mencapai minimal skor 80/100 *System Usability Scale* (SUS)
4. Menyelesaikan dalam jangka waktu 11 minggu
5. Tetap dalam anggaran yang dialokasikan
6. Menyediakan dokumentasi komprehensif

**Ruang Lingkup Proyek:**

**Termasuk dalam Ruang Lingkup:**
- Aplikasi web dengan 41 halaman (publik, autentikasi, dasbor)
- Autentikasi multi-peran (admin, terapis, klien)
- Sistem pemesanan *online* dengan alur 4 langkah
- Manajemen jadwal terapis
- Sistem dokumentasi sesi
- Pelacakan kemajuan klien
- Integrasi pembayaran (verifikasi manual dan *payment gateway* digital)
- Analitik dan pelaporan dasbor
- Notifikasi email
- Desain responsif (*mobile-friendly*)

**Tidak Termasuk dalam Ruang Lingkup:**
- Aplikasi *mobile native* (iOS/Android)
- Fitur berbasis AI (*chatbot*, rekomendasi)
- Integrasi konferensi video *native* (akan gunakan *iframe third-party*)
- Dukungan multi-bahasa (hanya Bahasa Indonesia)
- Resep elektronik atau integrasi rekam medis
- Arsitektur *multi-tenant*

**Hasil Utama (*Key Deliverables*):**
1. Aplikasi web fungsional (siap produksi)
2. Repositori kode sumber (GitHub)
3. Dokumentasi lengkap (teknis, manual pengguna)
4. Laporan proyek *capstone* (80-100 halaman)
5. Slide presentasi dan video demo
6. Materi pelatihan untuk pengguna

**Kriteria Keberhasilan:**
1. Semua kebutuhan fungsional wajib terimplementasi
2. Sistem lulus UAT dengan persetujuan pemangku kepentingan
3. Skor SUS ≥ 80/100
4. Tidak ada *bug* kritis atau tingkat tinggi di produksi
5. *Uptime* sistem ≥ 99% di bulan pertama
6. Peningkatan tingkat konversi dari 60% ke minimal 75%
7. Dokumentasi lengkap dan disetujui

**Risiko Kunci:**

| Risiko | Probabilitas | Dampak | Strategi Mitigasi |
|------|-------------|--------|---------------------|
| Perluasan ruang lingkup (*scope creep*) | Sedang | Tinggi | Proses kontrol perubahan ketat, prioritaskan kebutuhan wajib |
| Tantangan teknis | Sedang | Sedang | Tinjauan teknis reguler, konsultasi mentor |
| Pemangku kepentingan tidak tersedia | Rendah | Sedang | Penjadwalan fleksibel, komunikasi asinkron |
| Keterlambatan jadwal | Sedang | Tinggi | Pemantauan mingguan, alokasi waktu *buffer* |
| Masalah integrasi | Rendah | Tinggi | Pengujian integrasi awal, rencana cadangan |
| Pelanggaran keamanan data | Rendah | Sangat Tinggi | Praktik keamanan terbaik, audit reguler |

**Asumsi:**
- CUR-HEART akan menyediakan informasi bisnis dan dokumen yang dibutuhkan
- Pemangku kepentingan akan tersedia untuk wawancara dan pengujian
- Koneksi internet dan alat pengembangan akan tersedia
- API *payment gateway* akan dapat diakses untuk pengujian
- Data klien yang ada (jika perlu migrasi) tersedia

**Batasan:**
- Waktu: Harus selesai dalam 11 minggu (jadwal semester)
- Anggaran: Terbatas Rp 5.000.000
- Sumber Daya: Tim pengembang 3 orang
- Teknologi: Harus menggunakan *framework* Laravel (kebutuhan akademik)
- Kepatuhan: Harus mematuhi regulasi perlindungan data

**Persetujuan:**

| Nama | Peran | Tanda Tangan | Tanggal |
|------|------|-----------|------|
| [Nama Pemilik] | Sponsor Proyek | _____________ | ___/___/___ |
| Roki Anjas | Manajer Proyek | _____________ | ___/___/___ |
| Rani Irma Handayani, M.Kom | Pembimbing Akademik | _____________ | ___/___/___ |

---

## 4.2 Perencanaan Proyek

### 4.2.1 Manajemen Ruang Lingkup Proyek

Ruang lingkup proyek didefinisikan menggunakan **Struktur Rincian Kerja** (*Work Breakdown Structure* - WBS) yang memecah hasil utama menjadi paket kerja yang dapat dikelola.

**Tabel 4.4 Struktur Rincian Kerja (*Work Breakdown Structure*) Level 1-3**

| Kode WBS | Paket Kerja | Hasil | Durasi | Penanggung Jawab |
|----------|--------------|--------------|----------|-------------|
| **1.0** | **Sistem Informasi CUR-HEART** | Sistem pemesanan & terapi lengkap | 77 hari | Tim Proyek |
| 1.1 | Manajemen Proyek | Dokumentasi proyek | 77 hari | Manajer Proyek |
| 1.1.1 | Perencanaan Proyek | Piagam proyek, WBS, jadwal, anggaran | 3 hari | Manajer Proyek |
| 1.1.2 | Pemantauan Kemajuan | Laporan status mingguan | 77 hari | Manajer Proyek |
| 1.1.3 | Manajemen Risiko | Daftar risiko, rencana mitigasi | 77 hari | Manajer Proyek |
| 1.1.4 | Komunikasi Pemangku Kepentingan | Log komunikasi | 77 hari | Manajer Proyek |
| 1.2 | Analisis Kebutuhan | Dokumen SRS | 11 hari | Analis Bisnis |
| 1.2.1 | Wawancara Pemangku Kepentingan | Transkrip wawancara | 5 hari | Analis Bisnis |
| 1.2.2 | Analisis Proses Bisnis | Model proses As-Is & To-Be | 3 hari | Analis Bisnis |
| 1.2.3 | Dokumentasi Kebutuhan | Kebutuhan fungsional & non-fungsional | 3 hari | Analis Bisnis |
| 1.2.4 | Validasi Kebutuhan | SRS tervalidasi | 1 hari | Analis Bisnis |
| 1.3 | Perancangan Sistem | Dokumen desain | 14 hari | Perancang Sistem |
| 1.3.1 | Desain Arsitektur | Diagram arsitektur, keputusan *tech stack* | 3 hari | Arsitek Sistem |
| 1.3.2 | Desain Basis Data | ERD, struktur tabel, normalisasi | 4 hari | Perancang Basis Data |
| 1.3.3 | Desain UI/UX | *Mockup*, sistem desain, pustaka komponen | 5 hari | Perancang UI/UX |
| 1.3.4 | Desain Keamanan | Arsitektur keamanan, alur autentikasi | 2 hari | Spesialis Keamanan |
| 1.4 | Pengembangan | Aplikasi yang berfungsi | 28 hari | Tim Pengembang |
| 1.4.1 | Pengaturan Lingkungan | Lingkungan dev, *staging*, produksi | 2 hari | DevOps |
| 1.4.2 | Pengembangan *Backend* | API, logika bisnis, basis data | 10 hari | Pengembang *Backend* |
| 1.4.3 | Pengembangan *Frontend* | Implementasi UI | 12 hari | Pengembang *Frontend* |
| 1.4.4 | Integrasi | Sistem terintegrasi | 5 hari | Pengembang *Full Stack* |
| 1.4.5 | Tinjauan Kode (*Code Review*) | Laporan kualitas kode | 2 hari | Pengembang Senior |
| 1.5 | Pengujian | Laporan uji, pelacakan *bug* | 14 hari | Tim QA |
| 1.5.1 | Pengujian Unit (*Unit Testing*) | Laporan cakupan pengujian unit | 3 hari | Pengembang |
| 1.5.2 | Pengujian Integrasi | Hasil pengujian integrasi | 3 hari | Teknisi QA |
| 1.5.3 | Pengujian Fungsional | Kasus uji fungsional dijalankan | 4 hari | Teknisi QA |
| 1.5.4 | Pengujian Kegunaan (*Usability*) | Laporan uji kegunaan (skor SUS) | 3 hari | Peneliti UX |
| 1.5.5 | Pengujian Penerimaan Pengguna (UAT) | Persetujuan UAT, kriteria diterima | 2 hari | Pemangku Kepentingan |
| 1.6 | Peluncuran (*Deployment*) | Sistem produksi aktif | 7 hari | Tim DevOps |
| 1.6.1 | Pengaturan Produksi | Server terkonfigurasi, domain aktif | 2 hari | DevOps |
| 1.6.2 | Peluncuran Aplikasi | Aplikasi diluncurkan ke produksi | 2 hari | DevOps |
| 1.6.3 | *Go-Live* | Sistem operasional | 1 hari | Manajer Proyek |
| 1.6.4 | Pelatihan Pengguna | Pengguna terlatih, materi pelatihan | 2 hari | Pelatih |
| 1.7 | Dokumentasi | Dokumentasi proyek lengkap | 21 hari | Tim Dokumentasi |
| 1.7.1 | Dokumentasi Teknis | Dokumentasi API, arsitektur, skema DB | 7 hari | Penulis Teknis |
| 1.7.2 | Dokumentasi Pengguna | Manual pengguna, panduan admin | 5 hari | Penulis Teknis |
| 1.7.3 | Laporan *Capstone* | Laporan akhir (80-100 halaman) | 14 hari | Tim Proyek |
| 1.7.4 | Materi Presentasi | Slide, video demo | 7 hari | Tim Proyek |

**Total Paket Kerja:** 36 paket level-3  
**Total Durasi:** 77 hari kerja (11 minggu)

---

**[GAMBAR 4.4 - Struktur Rincian Kerja (WBS) Sistem CUR-HEART]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT WBS HIERARCHICAL DIAGRAM - 3 LEVELS]             │
│                                                             │
│   Level 1: PROYEK (Root)                                   │
│   Pengembangan Sistem CUR-HEART                            │
│   │                                                         │
│   ├─ 1.1 Manajemen Proyek (77 hari)                        │
│   │  ├─ 1.1.1 Perencanaan Proyek (3 hari)                  │
│   │  ├─ 1.1.2 Pemantauan Kemajuan (77 hari)                │
│   │  ├─ 1.1.3 Manajemen Risiko (77 hari)                   │
│   │  └─ 1.1.4 Komunikasi Pemangku Kepentingan (77 hari)    │
│   │                                                         │
│   ├─ 1.2 Analisis Kebutuhan (11 hari)                      │
│   │  ├─ 1.2.1 Wawancara Pemangku Kepentingan (5 hari)      │
│   │  ├─ 1.2.2 Analisis Proses Bisnis (3 hari)              │
│   │  ├─ 1.2.3 Dokumentasi Kebutuhan (3 hari)               │
│   │  └─ 1.2.4 Validasi Kebutuhan (1 hari)                  │
│   │                                                         │
│   ├─ 1.3 Perancangan Sistem (14 hari)                      │
│   │  ├─ 1.3.1 Desain Arsitektur (3 hari)                   │
│   │  ├─ 1.3.2 Desain Basis Data (4 hari)                   │
│   │  ├─ 1.3.3 Desain UI/UX (5 hari)                        │
│   │  └─ 1.3.4 Desain Keamanan (2 hari)                     │
│   │                                                         │
│   ├─ 1.4 Pengembangan (28 hari)                            │
│   │  ├─ 1.4.1 Pengaturan Lingkungan (2 hari)               │
│   │  ├─ 1.4.2 Pengembangan Backend (10 hari)               │
│   │  ├─ 1.4.3 Pengembangan Frontend (12 hari)              │
│   │  ├─ 1.4.4 Integrasi (5 hari)                           │
│   │  └─ 1.4.5 Tinjauan Kode (2 hari)                       │
│   │                                                         │
│   ├─ 1.5 Pengujian (14 hari)                               │
│   │  ├─ 1.5.1 Pengujian Unit (3 hari)                      │
│   │  ├─ 1.5.2 Pengujian Integrasi (3 hari)                 │
│   │  ├─ 1.5.3 Pengujian Fungsional (4 hari)                │
│   │  ├─ 1.5.4 Pengujian Kegunaan (3 hari)                  │
│   │  └─ 1.5.5 Pengujian Penerimaan Pengguna (2 hari)       │
│   │                                                         │
│   ├─ 1.6 Peluncuran (7 hari)                               │
│   │  ├─ 1.6.1 Pengaturan Produksi (2 hari)                 │
│   │  ├─ 1.6.2 Peluncuran Aplikasi (2 hari)                 │
│   │  ├─ 1.6.3 Go-Live (1 hari)                             │
│   │  └─ 1.6.4 Pelatihan Pengguna (2 hari)                  │
│   │                                                         │
│   └─ 1.7 Dokumentasi (21 hari, paralel)                    │
│      ├─ 1.7.1 Dokumentasi Teknis (7 hari)                  │
│      ├─ 1.7.2 Dokumentasi Pengguna (5 hari)                │
│      ├─ 1.7.3 Laporan Capstone (14 hari)                   │
│      └─ 1.7.4 Materi Presentasi (7 hari)                   │
│                                                             │
│   Ringkasan:                                                │
│   • 7 Fase Level-2                                         │
│   • 36 Paket Kerja Level-3                                 │
│   • 77 Hari Kerja (11 minggu)                              │
│   • Tim: 3 Pengembang                                      │
│                                                             │
│   Format: Diagram Pohon Hierarkis PNG                      │
│   Ukuran rekomendasi: 1800x1400px                          │
│   Gaya: Struktur pohon dengan kode warna per fase          │
│                                                             │
│   File: assets/images/wbs-curheart-3-levels.png            │
│   Tool: Microsoft Project, WBS Chart Pro, atau Draw.io     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.4: Struktur Rincian Kerja (WBS) 3-level proyek CUR-HEART dengan 7 fase, 36 paket kerja, durasi 77 hari_

---

**Garis Dasar Ruang Lingkup (*Scope Baseline*):**

Pernyataan ruang lingkup yang disetujui pada tanggal 29 September 2024 mencakup:

1. **Ruang Lingkup Produk:**
   - Aplikasi web dengan 41 halaman antarmuka
   - Sistem multi-peran (Admin, Terapis, Klien)
   - Sistem pemesanan *online* dengan ketersediaan *real-time*
   - Dasbor komprehensif untuk setiap peran
   - Integrasi pembayaran dengan beberapa metode
   - Sistem notifikasi email
   - Desain responsif untuk *mobile* dan *desktop*

2. **Ruang Lingkup Proyek:**
   - Analisis, desain, pengembangan, pengujian, dan peluncuran
   - Durasi: 11 minggu
   - Tim: 3 pengembang
   - Metodologi: *Waterfall* SDLC

3. **Kriteria Penerimaan:**
   - Semua kebutuhan fungsional dari MoSCoW "Harus Ada" terimplementasi
   - Sistem lolos UAT dengan persetujuan pemangku kepentingan
   - Tidak ada *bug* kritis di produksi
   - Dokumentasi lengkap dan disetujui
   - Pelatihan pengguna selesai

### 4.2.2 Manajemen Jadwal Proyek

**Tabel 4.5 Jadwal Proyek dengan Tonggak Pencapaian (*Milestones*)**

| Fase | Nama Tugas | Durasi | Mulai | Selesai | Status | Tonggak |
|-------|-----------|----------|-------|-----|--------|-----------|
| **1. Inisiasi** | *Kick-off* proyek & piagam | 3 hari | 16-Sep | 18-Sep | ✅ Selesai | M1: Proyek Disetujui |
| | Rapat *kick-off* | 1 hari | 16-Sep | 16-Sep | ✅ | |
| | Identifikasi pemangku kepentingan | 1 hari | 17-Sep | 17-Sep | ✅ | |
| | Persetujuan piagam proyek | 1 hari | 18-Sep | 18-Sep | ✅ | |
| **2. Kebutuhan** | Analisis & dokumentasi | 11 hari | 19-Sep | 29-Sep | ✅ Selesai | M2: Kebutuhan Selesai |
| | Wawancara pemangku kepentingan | 5 hari | 19-Sep | 23-Sep | ✅ | |
| | Analisis proses bisnis | 3 hari | 19-Sep | 21-Sep | ✅ | |
| | Dokumentasi kebutuhan | 3 hari | 26-Sep | 28-Sep | ✅ | |
| | Validasi kebutuhan | 1 hari | 29-Sep | 29-Sep | ✅ | |
| **3. Desain** | Desain sistem & UI/UX | 14 hari | 30-Sep | 13-Oct | ✅ Selesai | M3: Desain Selesai |
| | Desain arsitektur | 3 hari | 30-Sep | 2-Oct | ✅ | |
| | Desain basis data | 4 hari | 3-Oct | 6-Oct | ✅ | |
| | Desain UI/UX | 5 hari | 7-Oct | 11-Oct | ✅ | |
| | Desain keamanan | 2 hari | 12-Oct | 13-Oct | ✅ | |
| **4. Pengembangan** | Pengkodean & integrasi | 28 hari | 14-Oct | 10-Nov | ⏳ Sedang Berjalan | M4: Pengembangan Selesai |
| | Pengaturan lingkungan | 2 hari | 14-Oct | 15-Oct | ✅ | |
| | Implementasi basis data | 3 hari | 16-Oct | 18-Oct | ✅ | |
| | Sistem autentikasi | 4 hari | 19-Oct | 22-Oct | ✅ | |
| | Pengembangan *backend* | 10 hari | 23-Oct | 1-Nov | ⏳ | |
| | Pengembangan *frontend* | 12 hari | 23-Oct | 3-Nov | ⏳ | |
| | Integrasi | 5 hari | 4-Nov | 8-Nov | 🔜 Akan Datang | |
| | Tinjauan kode | 2 hari | 9-Nov | 10-Nov | 🔜 | |
| **5. Pengujian** | QA & UAT | 14 hari | 11-Nov | 24-Nov | 🔜 Akan Datang | M5: Pengujian Selesai |
| | Pengujian unit | 3 hari | 11-Nov | 13-Nov | 🔜 | |
| | Pengujian integrasi | 3 hari | 14-Nov | 16-Nov | 🔜 | |
| | Pengujian fungsional | 4 hari | 17-Nov | 20-Nov | 🔜 | |
| | Pengujian kegunaan (SUS) | 3 hari | 21-Nov | 23-Nov | 🔜 | |
| | UAT | 2 hari | 23-Nov | 24-Nov | 🔜 | |
| **6. Peluncuran** | *Go-live* & pelatihan | 7 hari | 25-Nov | 1-Dec | 🔜 Akan Datang | M6: Sistem Aktif |
| | Pengaturan produksi | 2 hari | 25-Nov | 26-Nov | 🔜 | |
| | Peluncuran aplikasi | 2 hari | 27-Nov | 28-Nov | 🔜 | |
| | *Go-live* | 1 hari | 29-Nov | 29-Nov | 🔜 | M6: Sistem Aktif |
| | Pelatihan pengguna | 2 hari | 30-Nov | 1-Dec | 🔜 | M7: Proyek Selesai |
| **7. Dokumentasi** | Laporan & materi | 21 hari | 11-Nov | 1-Dec | ⏳ Sedang Berjalan | M7: Proyek Selesai |
| | Dokumentasi teknis | 7 hari | 11-Nov | 17-Nov | ⏳ | |
| | Dokumentasi pengguna | 5 hari | 18-Nov | 22-Nov | 🔜 | |
| | Laporan *capstone* | 14 hari | 18-Nov | 1-Dec | ⏳ | |
| | Persiapan presentasi | 7 hari | 25-Nov | 1-Dec | 🔜 | |

**Total Durasi:** 77 hari kerja (11 minggu)  
**Jalur Kritis (*Critical Path*):** Inisiasi → Kebutuhan → Desain → Pengembangan → Integrasi → Pengujian → UAT → Peluncuran  
**Kemajuan Saat Ini:** 45% selesai (Fase 1-3 selesai, Fase 4 sedang berjalan)

---

**[GAMBAR 4.5 - Diagram Gantt Jadwal Proyek (77 Hari Kerja)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT GANTT CHART - 11 WEEKS TIMELINE]                 │
│                                                             │
│   PROYEK: Pengembangan Sistem CUR-HEART                    │
│   Garis Waktu: 16 Sep 2024 - 1 Des 2024 (77 hari)          │
│                                                             │
│   Nama Tugas           Minggu                               │
│                    1  2  3  4  5  6  7  8  9  10 11        │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      │
│   1. Inisiasi      ██                                       │
│   M1: Disetujui    ⭐                                       │
│                                                             │
│   2. Kebutuhan     ░░██████                                 │
│   M2: SRS Selesai     ⭐                                    │
│                                                             │
│   3. Desain           ░░░░████████                          │
│   M3: Desain Selesai         ⭐                             │
│                                                             │
│   4. Pengembangan           ░░░░██████████████████          │
│   M4: Kode Selesai                               ⭐         │
│                                                             │
│   5. Pengujian                              ░░░░████████    │
│   M5: UAT Lulus                                     ⭐      │
│                                                             │
│   6. Peluncuran                                     ░░░░██  │
│   M6: Go-Live                                           ⭐  │
│                                                             │
│   7. Dokumentasi                        ████████████████    │
│   M7: Selesai                                           ⭐  │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      │
│                                                             │
│   Legenda:                                                  │
│   ██ = Selesai       ░░ = Dependensi/Buffer                 │
│   ⭐ = Tonggak       (Tanggal ditampilkan)                  │
│                                                             │
│   Jalur Kritis (Merah): Inisiasi → Kebutuhan → Desain →    │
│                         Pengembangan → Integrasi →          │
│                         Pengujian → Peluncuran              │
│   Total Durasi: 77 hari kerja                              │
│   Tonggak: 7 tonggak utama                                 │
│   Dependensi: Berurutan dengan beberapa tugas paralel       │
│                                                             │
│   Format: Gantt Chart PNG/PDF                              │
│   Ukuran rekomendasi: 1800x1000px                          │
│   Gaya: Profesional dengan jalur kritis disorot            │
│                                                             │
│   File: assets/images/gantt-chart-77-days.png              │
│   Tool: Microsoft Project, GanttProject, atau Excel        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.5: Diagram Gantt jadwal proyek 77 hari kerja (11 minggu) dengan 7 fase, 7 tonggak, dan jalur kritis_

---

### 4.2.3 Manajemen Biaya Proyek

**Tabel 4.6 Rincian Anggaran (Total Rp 5.000.000)**

| Kategori | Item | Biaya Unit | Qty | Total (Rp) | % Anggaran | Prioritas |
|----------|------|-----------|-----|------------|-------------|----------|
| **Infrastruktur** | | | | **1.500.000** | 30% | Kritis |
| | Domain (.com, 1 tahun) | 150.000 | 1 | 150.000 | 3% | Harus Ada |
| | *Hosting* VPS (3 bulan) | 300.000 | 3 | 900.000 | 18% | Harus Ada |
| | Sertifikat SSL (Let's Encrypt) | 0 | 1 | 0 | 0% | Harus Ada |
| | Penyimpanan Cadangan (Google Drive) | 150.000 | 1 | 150.000 | 3% | Sebaiknya Ada |
| | Layanan CDN (Cloudflare Pro) | 300.000 | 1 | 300.000 | 6% | Bisa Ada |
| **Alat Pengembangan** | | | | **800.000** | 16% | Tinggi |
| | Editor Kode (VS Code) | 0 | 3 | 0 | 0% | Gratis |
| | Alat Desain (Figma Pro) | 200.000 | 1 | 200.000 | 4% | Harus Ada |
| | Alat Basis Data (MySQL Workbench) | 0 | 3 | 0 | 0% | Gratis |
| | Kontrol Versi (GitHub) | 0 | 1 | 0 | 0% | Gratis |
| | Manajemen Proyek (Asana) | 100.000 | 1 | 100.000 | 2% | Sebaiknya Ada |
| | Alat Pengujian | 500.000 | 1 | 500.000 | 10% | Harus Ada |
| **Layanan Pihak Ketiga** | | | | **1.200.000** | 24% | Tinggi |
| | *Payment Gateway* (Midtrans) | 0 | 1 | 0 | 0% | Setup gratis |
| | Kredit Uji Pembayaran | 500.000 | 1 | 500.000 | 10% | Harus Ada |
| | Layanan Email (SendGrid) | 200.000 | 1 | 200.000 | 4% | Harus Ada |
| | Layanan SMS (Twilio) | 300.000 | 1 | 300.000 | 6% | Bisa Ada |
| | Pemantauan (Sentry) | 200.000 | 1 | 200.000 | 4% | Sebaiknya Ada |
| **Dokumentasi** | | | | **500.000** | 10% | Sedang |
| | Pencetakan Laporan (*Full Color*) | 300.000 | 1 | 300.000 | 6% | Harus Ada |
| | Pencetakan X-Banner (60x160) | 200.000 | 1 | 200.000 | 4% | Harus Ada |
| **Cadangan Kontinjensi** | | | | **1.000.000** | 20% | Kritis |
| | *Buffer* untuk biaya tak terduga | 1.000.000 | 1 | 1.000.000 | 20% | *Buffer* |
| **TOTAL ANGGARAN PROYEK** | | | | **5.000.000** | 100% | |

---

**[GAMBAR 4.6 - Rincian Alokasi Anggaran (Rp 5.000.000)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT BUDGET PIE CHART + BAR COMPARISON]               │
│                                                             │
│   TOTAL ANGGARAN: Rp 5.000.000                             │
│                                                             │
│   ┌─────────────────────────────────────────┐              │
│   │   DIAGRAM PIE - Alokasi Anggaran        │              │
│   │                                         │              │
│   │     Infrastruktur 30%                   │              │
│   │     Rp 1.500.000                        │              │
│   │                                         │              │
│   │     Layanan Pihak Ketiga 24%            │              │
│   │     Rp 1.200.000                        │              │
│   │                                         │              │
│   │     Kontinjensi 20%                     │              │
│   │     Rp 1.000.000                        │              │
│   │                                         │              │
│   │     Alat Pengembangan 16%               │              │
│   │     Rp 800.000                          │              │
│   │                                         │              │
│   │     Dokumentasi 10%                     │              │
│   │     Rp 500.000                          │              │
│   └─────────────────────────────────────────┘              │
│                                                             │
│   DIAGRAM BATANG - Pengeluaran per Kategori:               │
│   Infrastruktur     ████████████████░░ 30%                 │
│   Pihak Ketiga      ████████████░░░░░░ 24%                 │
│   Kontinjensi       ████████████░░░░░░ 20%                 │
│   Alat Dev          ████████░░░░░░░░░░ 16%                 │
│   Dokumentasi       █████░░░░░░░░░░░░░ 10%                 │
│                                                             │
│   Sorotan Kunci:                                           │
│   • Terbesar: Infrastruktur (Rp 1.5M - hosting, domain)   │
│   • Kritis: API Pihak Ketiga (Rp 1.2M - pembayaran, email)│
│   • Buffer: Kontinjensi 20% (Rp 1M dicadangkan)            │
│   • Alat Gratis: VS Code, MySQL, GitHub (Rp 0)             │
│                                                             │
│   Format: Diagram Kombo (Pie + Bar) PNG                    │
│   Ukuran rekomendasi: 1600x900px                           │
│   Gaya: Profesional dengan kode warna                      │
│                                                             │
│   File: assets/images/budget-allocation-5m.png             │
│   Tool: Excel, Google Sheets, atau Canva                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.6: Rincian alokasi anggaran Rp 5 juta dengan diagram *pie* untuk 5 kategori dan diagram batang perbandingan_

---

**Indeks Kinerja Biaya (*Cost Performance Index* - CPI):**

| Periode | Nilai Terencana (PV) | Nilai Hasil (EV) | Biaya Aktual (AC) | Varian Biaya (CV) | CPI | Status |
|--------|-------------------|-------------------|------------------|-------------------|-----|--------|
| Bulan 1 (Sep) | Rp 1.500.000 | Rp 1.545.000 | Rp 1.450.000 | +Rp 95.000 | 1.07 | ✅ Di bawah anggaran |
| Bulan 2 (Okt) | Rp 2.000.000 | Rp 2.020.000 | Rp 1.980.000 | +Rp 40.000 | 1.02 | ✅ Sesuai rencana |
| Bulan 3 (Nov) | Rp 1.500.000 | (sedang berjalan) | (sedang berjalan) | TBD | TBD | ⏳ Sedang berjalan |
| **Total s.d. Kini** | **Rp 3.500.000** | **Rp 3.565.000** | **Rp 3.430.000** | **+Rp 135.000** | **1.04** | ✅ **Di bawah anggaran** |

**Catatan:**
- CPI > 1.0 = Di bawah anggaran (kinerja baik)
- CPI = 1.0 = Sesuai anggaran (sesuai rencana)
- CPI < 1.0 = Melebihi anggaran (perlu tindakan korektif)
- CPI saat ini 1.04 menunjukkan manajemen biaya yang efisien

### 4.2.4 Manajemen Kualitas Proyek

**Tabel 4.7 Standar dan Metrik Kualitas**

| Area Kualitas | Standar/Kriteria | Metrik Target | Metode Pengukuran | Penanggung Jawab | Frekuensi |
|--------------|-------------------|---------------|-------------------|----------------|-----------|
| **Kualitas Kode** | Laravel PSR-12, PHPDoc | Grade A, Tidak ada isu kritis | SonarQube, PHPStan | Pengembang | Per *commit* |
| | Prinsip DRY, SOLID | Kompleksitas siklomatis < 10 | Alat analisis kode | Pengembang | Per PR |
| | Nama bermakna, modularitas | Indeks Kemudahan Pemeliharaan > 70 | Metrik kode | Pengembang | Mingguan |
| **Kualitas Fungsional** | Semua kebutuhan wajib | 95%+ terimplementasi | Pelacakan kebutuhan | PM | Per *sprint* |
| | Aturan bisnis benar | 100% aturan tervalidasi | Pengujian fungsional | QA | Pra-UAT |
| | Penanganan error | Semua eksepsi ditangani | Uji unit & integrasi | Pengembang | Berkelanjutan |
| **Kinerja** | Waktu muat halaman | < 3 detik | Lighthouse, GTmetrix | Pengembang | Mingguan |
| | *Time to First Byte* (TTFB) | < 600ms | Pemantauan kinerja | DevOps | Mingguan |
| | Kinerja *query* basis data | < 100ms per *query* | *Profiler query* | DBA | Mingguan |
| | Waktu respons API | < 500ms | Alat uji API | Pengembang *Backend* | Mingguan |
| **Keamanan** | Kepatuhan OWASP Top 10 | Tidak ada kerentanan kritis | OWASP ZAP, audit keamanan | Pemimpin Keamanan | Dua mingguan |
| | Autentikasi & Otorisasi | JWT aman, berbasis peran | Pengujian keamanan | Pengembang *Backend* | Pra-*deploy* |
| | Enkripsi data | Data sensitif terenkripsi | Tinjauan kode | Pemimpin Keamanan | Pra-*deploy* |
| | Pencegahan injeksi SQL | Nol kerentanan SQL | Uji penetrasi | QA | Pra-*deploy* |
| **Kegunaan** | *System Usability Scale* (SUS) | ≥ 80/100 | Uji pengguna dengan 10 orang | Pemimpin UX | Minggu 10 |
| | Tingkat keberhasilan tugas | ≥ 90% | Pengujian kegunaan | Pemimpin UX | Minggu 10 |
| | Tingkat error per tugas | < 5% | Observasi uji pengguna | Pemimpin UX | Minggu 10 |
| | WCAG 2.1 Level AA | Lulus audit aksesibilitas | Lighthouse, aXe | Pengembang *Frontend* | Mingguan |
| **Cakupan Pengujian** | Cakupan uji unit | ≥ 70% untuk kode kritis | Cakupan PHPUnit | Pengembang | Berkelanjutan |
| | Cakupan uji integrasi | 100% alur kritis | Laravel Dusk | QA | Pra-UAT |
| | Densitas defek | < 5 *bug* per 1000 LOC | Pelacakan *bug* (Jira) | QA | Pasca-pengujian |
| **Dokumentasi** | Dokumentasi teknis | 100% lengkap | Tinjauan dokumentasi | Penulis Teknis | Pra-*deploy* |
| | Manual pengguna | Semua peran tercakup | Tinjauan pengguna | Penulis Teknis | Pra-pelatihan |
| | Komentar kode | Logika kompleks berkomentar | Tinjauan kode | Pengembang | Per PR |

**Proses Jaminan Kualitas:**
1. Tinjauan Kode (GitHub PR) → Pengujian Unit (PHPUnit) → Pengujian Integrasi (Laravel Dusk) → Pengujian Kinerja (Lighthouse) → Audit Keamanan (OWASP ZAP) → Pengujian Kegunaan (SUS) → UAT (Pemangku Kepentingan)
   - Tidak ada *bug* kritis atau tingkat tinggi
   - Tinjauan kode oleh rekan sebelum *merge*
   - Minimum 70% cakupan kode untuk fungsi kritis

2. **Standar Kinerja:**
   - Waktu muat halaman < 3 detik (pada koneksi rata-rata)
   - *Time to First Byte* (TTFB) < 600ms
   - Optimasi *query* basis data (tidak ada masalah N+1)
   - Optimasi gambar (maks 500KB per gambar)
   - Skor Lighthouse ≥ 80 untuk Kinerja

3. **Standar Keamanan:**
   - Kerentanan OWASP Top 10 dimitigasi
   - Enkripsi data untuk informasi sensitif
   - Autentikasi dan otorisasi yang aman
   - Audit keamanan reguler
   - Kepatuhan terhadap UU Perlindungan Data Pribadi

4. **Standar Kegunaan:**
   - Skor *System Usability Scale* (SUS) ≥ 80/100
   - Tingkat keberhasilan tugas ≥ 90%
   - Tingkat error < 5% per tugas
   - Aksesibilitas WCAG 2.1 Level AA (minimum)

5. **Standar Dokumentasi:**
   - Dokumentasi teknis lengkap (arsitektur, basis data, API)
   - Manual pengguna komprehensif untuk setiap peran
   - Komentar kode untuk logika kompleks
   - File README dengan instruksi *setup*
   - *Change log* dipelihara

**Aktivitas Jaminan Kualitas:**

| Aktivitas | Frekuensi | Penanggung Jawab | Alat/Metode |
|----------|-----------|----------------|-------------|
| Tinjauan Kode | Per *pull request* | Pengembang rekan | Tinjauan PR GitHub |
| Pengujian Unit | Berkelanjutan | Pengembang | PHPUnit |
| Pengujian Integrasi | Per integrasi | QA/Pengembang | Laravel Dusk, Postman |
| Pengujian Kinerja | Mingguan | Pengembang | Lighthouse, GTmetrix |
| Audit Keamanan | Dua mingguan | Pemimpin keamanan | OWASP ZAP, tinjauan manual |
| Pengujian Kegunaan | Sekali (Minggu 10) | Pemimpin UX | Sesi pengguna |
| UAT | Sekali (Minggu 10) | Pemangku Kepentingan | Kriteria penerimaan |

**Metrik Kualitas:**

| Metrik | Target | Metode Pengukuran |
|--------|--------|-------------------|
| Densitas Defek | < 5 *bug* per 1000 LOC | Alat pelacakan *bug* |
| Cakupan Uji | ≥ 70% untuk kode kritis | Alat cakupan kode |
| Skor Kinerja | ≥ 80/100 (Lighthouse) | Audit Lighthouse |
| Skor Keamanan | Rating A | *Scanner* keamanan |
| Skor Kegunaan | ≥ 80/100 (SUS) | Pengujian pengguna |
| Kualitas Kode | Grade A | Alat analisis kode |

### 4.2.5 Manajemen Sumber Daya

**Tabel 4.8 Matriks Alokasi Sumber Daya**

| Nama Sumber Daya | Peran Utama | Peran Sekunder | Keahlian/Ketrampilan | Alokasi | Fase Proyek | Jam Mingguan | Biaya (jika ada) |
|---------------|--------------|----------------|------------------|------------|----------------|--------------|---------------|
| **Tim Internal (Inti)** | | | | | | | |
| Roki Anjas | Manajer Proyek | Pengembang *Backend* | Kepemimpinan, Laravel, PHP, MySQL, API | 100% | Semua fase | 40 jam | Gratis (mahasiswa) |
| Susanto | Pengembang *Frontend* | Perancang UI/UX | Tailwind CSS, Blade, Figma, Riset UX | 100% | Desain-Peluncuran | 40 jam | Gratis (mahasiswa) |
| Fahruroji | Pengembang *Full-Stack* | Admin Basis Data | Laravel, MySQL, Pengujian, Dokumentasi | 100% | Desain-Peluncuran | 40 jam | Gratis (mahasiswa) |
| **Pemangku Kepentingan Eksternal** | | | | | | | |
| Rani Irma Handayani, M.Kom | Pembimbing Akademik | Penasihat Teknis | Analisis sistem, manajemen proyek | Paruh waktu | Semua fase | 2 jam | Gratis (dosen) |
| Pemilik CUR-HEART | Sponsor Proyek | Pengambil Keputusan | Strategi bisnis, persetujuan anggaran | Sesuai kebutuhan | Inisiasi, UAT | 1 jam | Gratis (sponsor) |
| Terapis (5 orang) | Ahli Materi Subjek | Pengguna Akhir | Hipnoterapi, pengetahuan alur kerja | Sesuai kebutuhan | Kebutuhan, UAT | 2 jam/orang | Gratis (SME) |
| Staf Admin (2 orang) | Operator Sistem | Penguji | Proses admin, entri data | Sesuai kebutuhan | Kebutuhan, UAT | 3 jam/orang | Gratis (SME) |
| Klien Sampel (10 orang) | Pengguna Akhir | Penguji | Perspektif pengguna, umpan balik | Sesuai kebutuhan | Pengujian | 1 jam/orang | Gratis (sukarelawan) |
| **Sumber Daya Spesialis** | | | | | | | |
| Mentor Teknis | Peninjau Kode | - | Pengembang Laravel senior | Ad-hoc | Pengembangan | 1 jam/minggu | Gratis (komunitas) |
| Konsultan Keamanan | Auditor Keamanan | - | Keamanan web, OWASP | Ad-hoc | Pengujian | 2 jam total | Gratis (sukarelawan) |

**Distribusi Sumber Daya per Fase:**

| Fase | Roki (PM/BE) | Susanto (FE/UX) | Fahruroji (FS/DBA) | Eksternal | Total Jam |
|-------|-------------|-----------------|-------------------|----------|-------------|
| 1. Inisiasi (3 hari) | 24 jam (Pimpinan) | 8 jam | 8 jam | 2 jam (Pembimbing) | 42 jam |
| 2. Kebutuhan (11 hari) | 40 jam | 32 jam | 16 jam | 20 jam (SME) | 108 jam |
| 3. Desain (14 hari) | 56 jam | 80 jam (Pimpinan) | 56 jam | 4 jam (Tinjauan) | 196 jam |
| 4. Pengembangan (28 hari) | 112 jam (Pimpinan) | 112 jam | 112 jam | 4 jam (Mentor) | 340 jam |
| 5. Pengujian (14 hari) | 40 jam | 40 jam | 72 jam (Pimpinan) | 20 jam (Pengguna) | 172 jam |
| 6. Peluncuran (7 hari) | 32 jam (Pimpinan) | 16 jam | 24 jam | 8 jam (Pelatihan) | 80 jam |
| 7. Dokumentasi (21 hari) | 60 jam | 40 jam | 60 jam (Pimpinan) | 2 jam (Tinjauan) | 162 jam |
| **Total** | **364 jam** | **328 jam** | **348 jam** | **60 jam** | **1100 jam** |

**Catatan:**
- Semua anggota tim internal: Alokasi penuh waktu (40 jam/minggu selama proyek)
- Tidak ada biaya gaji (proyek *capstone* akademik)
- Total upaya proyek: ~1100 jam-orang selama 11 minggu
- Rata-rata: 100 jam-orang per minggu

**Kalender Sumber Daya:**

```
      September         Oktober          November
Minggu: 1  2  3  4    5  6  7  8    9  10 11
────────────────────────────────────────────
Roki: ████████████████████████████████████
Susanto: ████████████████████████████████████
Fahruroji: ████████████████████████████████████
Dosen: █ █ █ █    █ █ █ █    █ █  █
Owner:  █       █        █        █    █
Terapis:     █              █         █
```

**Perataan Sumber Daya (*Resource Leveling*):**

Untuk menghindari alokasi sumber daya yang berlebihan, beberapa tugas dilakukan paralel:
- Pengembangan *backend* dan *frontend* (Minggu 5-8)
- Pengujian dan Dokumentasi (Minggu 9-11)
- Kode dapat didistribusikan berdasarkan modul untuk kerja paralel

### 4.2.6 Manajemen Risiko

**Tabel 4.9 Daftar Risiko dengan Strategi Mitigasi**

| ID | Peristiwa Risiko | Kategori | Probabilitas | Dampak | Skor Risiko | Prioritas | Strategi Mitigasi (Preventif) | Rencana Kontinjensi (Reaktif) | Pemilik Risiko | Status |
|----|-----------|----------|-------------|--------|------------|----------|----------------------------------|---------------------------|------------|--------|
| R01 | Perluasan ruang lingkup dari permintaan pemangku kepentingan | Ruang Lingkup | Sedang (50%) | Tinggi (8) | 4.0 | Kritis | Proses kontrol perubahan ketat, prioritas MoSCoW, dokumentasi garis dasar ruang lingkup yang disetujui | Tunda fitur *nice-to-have* ke Fase 2 pasca-peluncuran, negosiasi ulang jadwal | PM | ⚠️ Aktif |
| R02 | Kompleksitas teknis lebih tinggi dari estimasi | Teknis | Sedang (40%) | Sedang (6) | 2.4 | Tinggi | *Prototyping* awal, tinjauan teknis reguler, solusi *spike* untuk hal yang tidak diketahui | Minta bantuan mentor, pecah menjadi tugas kecil, perpanjang jadwal jika kritis | Pemimpin Teknis | ⚠️ Aktif |
| R03 | Ketidaktersediaan anggota tim (sakit, pribadi) | Sumber Daya | Rendah (20%) | Tinggi (8) | 1.6 | Tinggi | Pelatihan silang, *pair programming*, dokumentasi komprehensif, sesi berbagi pengetahuan | Distribusi ulang pekerjaan antar tim, sesuaikan jadwal, tunda tugas non-kritis | PM | ✅ Dipantau |
| R04 | Pemangku kepentingan tidak tersedia untuk tinjauan/UAT | Pemangku Kepentingan | Rendah (30%) | Sedang (5) | 1.5 | Sedang | Penjadwalan fleksibel, komunikasi asinkron, perencanaan keterlibatan awal | Gunakan demo yang direkam, persetujuan email, pengambil keputusan proksi | PM | ✅ Dipantau |
| R05 | Masalah integrasi *payment gateway* | Integrasi | Sedang (40%) | Sedang (6) | 2.4 | Tinggi | Pengujian integrasi awal, lingkungan *sandbox*, penyedia cadangan (Xendit), tinjauan dokumentasi API | Gunakan verifikasi manual sementara, implementasi metode pembayaran alternatif terlebih dahulu | Pengembang *Backend* | ⚠️ Aktif |
| R06 | Masalah kinerja pada produksi | Kinerja | Rendah (30%) | Tinggi (7) | 2.1 | Tinggi | Uji beban, optimasi *query*, indeks basis data, strategi *caching* (Redis), CDN | Tingkatkan paket *hosting* (*scale up*), implementasi CDN penuh, optimalkan *query* kritis | DevOps | ✅ Dipantau |
| R07 | Pelanggaran keamanan data atau kerentanan | Keamanan | Rendah (10%) | Kritis (10) | 1.0 | Kritis | Praktik keamanan terbaik (OWASP), audit reguler, uji penetrasi, enkripsi, validasi input | Peluncuran *patch* segera, rencana respons insiden, beri tahu pengguna yang terkena dampak, analisis forensik | Pemimpin Keamanan | ✅ Dipantau |
| R08 | Keterlambatan jadwal karena tantangan tak terduga | Jadwal | Sedang (40%) | Tinggi (7) | 2.8 | Kritis | Pemantauan kemajuan mingguan, waktu *buffer* (20%), identifikasi masalah awal, *standup* harian | Kurangi ruang lingkup (hapus *nice-to-have*), minta perpanjangan jadwal, tingkatkan jam kerja | PM | ⚠️ Aktif |
| R09 | Pembengkakan anggaran | Biaya | Rendah (20%) | Sedang (5) | 1.0 | Sedang | Pelacakan biaya (bulanan), proses persetujuan pengeluaran, gunakan alternatif gratis bila memungkinkan | Gunakan dana kontinjensi (Rp 1M), cari pendanaan tambahan dari sponsor, kurangi biaya opsional | PM | ✅ Dipantau |
| R10 | Adopsi pengguna rendah pasca-peluncuran | Bisnis | Sedang (30%) | Tinggi (8) | 2.4 | Tinggi | Desain berpusat pengguna, pelatihan komprehensif, rencana manajemen perubahan, keterlibatan pengguna awal | Sesi pelatihan tambahan, dukungan pengguna 1-on-1, insentif untuk adopsi, *loop* umpan balik | PM | ⚠️ Aktif |
| R11 | *Downtime* layanan pihak ketiga (*hosting*, API) | Eksternal | Rendah (25%) | Sedang (6) | 1.5 | Sedang | Pilih penyedia andal (SLA *uptime* 99.9%), implementasi logika *retry*, penanganan error | Beralih ke penyedia cadangan, proses *fallback* manual, komunikasi dengan pengguna | DevOps | ✅ Dipantau |
| R12 | Perubahan kebutuhan di tengah proyek | Kebutuhan | Sedang (35%) | Sedang (6) | 2.1 | Tinggi | Validasi kebutuhan dengan pemangku kepentingan, persetujuan, dewan kontrol perubahan | Nilai dampak, prioritaskan ulang *backlog*, negosiasi penyesuaian jadwal/ruang lingkup | PM | ⚠️ Aktif |

**Perhitungan Skor Risiko:** Probabilitas (%) × Dampak (1-10)  
**Tingkat Prioritas:** Kritis (>3.5), Tinggi (2.0-3.5), Sedang (1.0-2.0), Rendah (<1.0)

---

**[GAMBAR 4.7 - Matriks Risiko (Probabilitas vs Dampak dengan 12 Risiko)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT RISK MATRIX - 12 IDENTIFIED RISKS]               │
│                                                             │
│   MATRIKS RISIKO PROYEK CUR-HEART                          │
│                                                             │
│   DAMPAK (Keparahan) →                                     │
│   P                                                         │
│   r                                                         │
│   o    Tinggi  │                   │ R01      │ R03        │
│   b  (40-60%)  │                   │ Perluasan│ Sumber     │
│   a            │                   │ Lingkup  │ Daya       │
│   b            │─────────────────────────────────────────  │
│   i  Sedang    │          │ R02      │ R08      │ R10      │
│   l  (30-40%)  │          │ Kompleks │ Jadwal   │ Adopsi   │
│   i            │          │ Teknis   │ Terlambat│ Pengguna │
│   t            │─────────────────────────────────────────  │
│   a  Rendah    │ R09      │ R04 R11  │ R06      │ R07      │
│   s  (10-30%)  │ Anggaran │ Stakehld/│ Kinerja  │ Keamanan │
│   ↓            │ Bengkak  │ Pihak-3  │ Masalah  │ KRITIS   │
│                └─────────────────────────────────────────  │
│                  Rendah  Sedang(4-6) Tinggi(7-8) Kritis(9-10)│
│                      (1-3)       DAMPAK (Keparahan) →       │
│                                                             │
│   Kode Warna:                                              │
│   🔴 KRITIS (Skor > 3.5): R01 (4.0), R08 (2.8)             │
│   🟡 TINGGI (Skor 2.0-3.5): R02, R05, R10, R12 (2.1-2.4)   │
│   🟢 SEDANG (Skor 1.0-2.0): R03, R04, R06, R11 (1.5-2.1)   │
│   ⚪ RENDAH (Skor < 1.0): R07, R09 (1.0)                    │
│                                                             │
│   3 Risiko Kritis Teratas:                                 │
│   1. R01 - Perluasan Lingkup (4.0): Prioritas MoSCoW       │
│   2. R08 - Keterlambatan Jadwal (2.8): Pantau mingguan     │
│   3. R05 - Integrasi Pembayaran (2.4): Uji awal            │
│                                                             │
│   Distribusi Risiko:                                       │
│   • Prioritas Kritis: 2 risiko (17%)                       │
│   • Prioritas Tinggi: 4 risiko (33%)                       │
│   • Prioritas Sedang: 4 risiko (33%)                       │
│   • Prioritas Rendah: 2 risiko (17%)                       │
│                                                             │
│   Status Mitigasi:                                         │
│   ⚠️ Pemantauan Aktif: 6 risiko                            │
│   ✅ Terkendali: 6 risiko                                  │
│                                                             │
│   Format: Matriks Risiko PNG dengan posisi 12 risiko       │
│   Ukuran rekomendasi: 1600x1000px                          │
│   Gaya: Profesional dengan kuadran kode warna              │
│                                                             │
│   File: assets/images/risk-matrix-12-risks.png             │
│   Tool: PowerPoint, Excel, atau draw.io                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.7: Matriks risiko probabilitas vs dampak dengan 12 risiko teridentifikasi, menunjukkan R01 (Perluasan Lingkup) dan R08 (Keterlambatan Jadwal) sebagai prioritas kritis_

---

**Strategi Respons Risiko:**

1. **Hindari (*Avoid*):** Eliminasi risiko (mis., pilih teknologi terbukti daripada eksperimental)
2. **Mitigasi (*Mitigate*):** Kurangi probabilitas atau dampak (mis., pengujian menyeluruh untuk kurangi *bug*)
3. **Transfer (*Transfer*):** Alihkan risiko ke pihak ketiga (mis., gunakan *managed hosting* untuk risiko infrastruktur)
4. **Terima (*Accept*):** Terima risiko jika dampak rendah (mis., inkonsistensi UI minor)

**Pemantauan Risiko:**

Risiko ditinjau setiap rapat mingguan:
- Perbarui probabilitas dan dampak risiko
- Periksa efektivitas strategi mitigasi
- Identifikasi risiko baru
- Dokumentasikan pelajaran yang dipetik

### 4.2.7 Manajemen Komunikasi

**Tabel 4.10 Matriks Rencana Komunikasi**

| Pemangku Kepentingan | Kebutuhan Informasi | Jenis Komunikasi | Metode/Alat | Frekuensi | Format | Penanggung Jawab | Waktu Pengiriman | Mekanisme Umpan Balik |
|-------------|------------------|-------------------|-------------|-----------|--------|-------------|---------------|-------------------|
| Pemilik CUR-HEART | Status proyek, anggaran, keputusan kunci, pembaruan ROI | Laporan Formal | Email (PDF), Rapat tatap muka | Mingguan (Senin) | Templat laporan status | Manajer Proyek | Senin 9 pagi | Respons email, diskusi rapat |
| Dosen Pembimbing | Kemajuan, tantangan teknis, hasil, kebutuhan akademik | Konsultasi Formal | Tatap muka, Google Meet, Dokumentasi | Mingguan (Jumat) | Dokumen kemajuan, demo kode | Manajer Proyek | Jumat 2 siang | Panduan teknis, persetujuan/revisi |
| Terapis (5) | Demo fitur, jadwal pengujian, undangan pelatihan, perubahan alur kerja | Pembaruan Informal | Grup WhatsApp, Email | Dua mingguan | *Screenshot*, video demo | Manajer Proyek | Selasa sore | Umpan balik WhatsApp, partisipasi uji |
| Staf Admin (2) | Fitur sistem, jadwal pengujian, materi pelatihan, perubahan proses | Pembaruan Informal | WhatsApp, Email | Dua mingguan | *Screenshot*, draf panduan pengguna | Manajer Proyek | Selasa sore | Umpan balik WhatsApp, validasi proses |
| Klien Sampel (10) | Undangan pengujian, permintaan umpan balik, partisipasi studi kegunaan | Permintaan | Email, Panggilan telepon | Sesuai kebutuhan (Minggu 10) | Email undangan, formulir persetujuan | Perancang UX | 3 hari sebelum uji | Survei, respons wawancara |
| Tim Pengembang (3) | Penugasan tugas, kemajuan harian, hambatan, tinjauan kode, keputusan teknis | Sinkronisasi Harian | Obrolan Discord/Slack, *Standup* harian (video) | Harian (10 pagi) | Format *standup* (*done/todo/blockers*) | Manajer Proyek | Harian 10 pagi | Segera (obrolan), diskusi *standup* |
| Mentor Teknis | Permintaan tinjauan kode, tantangan teknis, keputusan arsitektur | Konsultasi Ad-hoc | GitHub PR, Email, Zoom | Sesuai kebutuhan (mingguan) | *Snippet* kode, diagram arsitektur | Pemimpin Teknis | Saat hambatan terjadi | Komentar kode, persetujuan tinjauan |
| Universitas (Akademik) | Kemajuan bulanan, hasil akhir | Laporan Formal | Email, Pengiriman fisik | Bulanan, Akhir | Format laporan akademik | Manajer Proyek | Akhir bulan | Evaluasi akademik |

**Prinsip Komunikasi:**
1. Informasi yang tepat kepada orang yang tepat pada waktu yang tepat
2. Pesan yang jelas, ringkas, dan dapat ditindaklanjuti
3. Komunikasi dua arah (umpan balik didorong)
4. Dokumentasi keputusan penting
5. Jalur eskalasi untuk masalah mendesak

---

**[GAMBAR 4.8 - Matriks Komunikasi Pemangku Kepentingan]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT COMMUNICATION MATRIX VISUAL]                      │
│                                                             │
│   MATRIKS KOMUNIKASI PEMANGKU KEPENTINGAN                   │
│   Proyek CUR-HEART (8 Kelompok Pemangku Kepentingan)       │
│                                                             │
│   Sumbu Frekuensi (Vertikal) vs Formalitas (Horizontal)    │
│                                                             │
│   Harian │ Tim Dev (3)                    │                │
│          │ Discord/Standup                │                │
│          │ ━━━━━━━━━━━━                   │                │
│ Mingguan │ Pemilik         │ Dosen        │                │
│          │ Laporan Status  │ Konsultasi   │                │
│          │ ━━━━━━━━━      │ ━━━━━━━━━   │                │
│          │                                │                │
│ Dua      │ Terapis (5)     │ Admin (2)    │                │
│ Minggu   │ WhatsApp Demo   │ Pelatihan    │                │
│          │ ━━━━━━━━━      │ ━━━━━━━     │                │
│          │                                │                │
│ Bulanan  │                                │ Universitas    │
│          │                                │ Laporan Kemajuan│
│          │                                │ ━━━━━━━━━━━   │
│ Sesuai   │ Mentor Teknis   │ Klien (10)   │                │
│ Kebutuhan│ Tinjauan Kode   │ Uji UAT      │                │
│          │ ━━━━━━━━━      │ ━━━━━━━━━   │                │
│          └───────────────────────────────────────────────  │
│            Informal          Semi-Formal       Formal       │
│                        FORMALITAS →                         │
│                                                             │
│   Legenda:                                                  │
│   📧 Formal: Email, Laporan, Dokumentasi                    │
│   💬 Informal: WhatsApp, Obrolan, Telepon                   │
│   🎯 Semi-Formal: Rapat, Presentasi, Demo                  │
│                                                             │
│   Volume Komunikasi:                                        │
│   • Tertinggi: Tim Dev (harian, 40 jam/minggu)             │
│   • Tinggi: Pemilik + Dosen (mingguan, 2-3 jam/minggu)     │
│   • Sedang: Terapis + Admin (dua mingguan, 1 jam/minggu)   │
│   • Rendah: Mentor, Klien, Univ (kebutuhan, <1 jam/minggu) │
│                                                             │
│   Total Pemangku Kepentingan: 26 individu                   │
│   • Tim Internal: 3 (pengembang inti)                       │
│   • Eksternal: 23 (pemilik, dosen, pengguna, mentor)       │
│                                                             │
│   Format: Diagram Matriks Komunikasi PNG                    │
│   Ukuran rekomendasi: 1600x900px                           │
│   Gaya: Matriks/kuadran profesional dengan label           │
│                                                             │
│   File: assets/images/communication-matrix.png              │
│   Tool: PowerPoint, Excel, atau Canva                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.8: Matriks komunikasi pemangku kepentingan menunjukkan frekuensi dan tingkat formalitas untuk 8 kelompok pemangku kepentingan (26 individu)_

---

**Alat Komunikasi:**

1. **Tim Internal:**
   - Discord/Slack: Komunikasi harian, pertanyaan cepat
   - GitHub: Tinjauan kode, pelacakan masalah
   - Trello/Asana: Manajemen tugas
   - Google Drive: Berbagi dokumen

2. **Dengan Pemangku Kepentingan:**
   - Email: Komunikasi formal, laporan
   - WhatsApp: Pembaruan cepat, koordinasi
   - Zoom/Google Meet: Rapat jarak jauh
   - Tatap muka: Diskusi penting, demo

**Jadwal Rapat:**

| Rapat | Peserta | Frekuensi | Durasi | Tujuan |
|---------|-------------|-----------|----------|---------|
| *Standup* Harian | Tim Pengembang | Harian | 15 menit | Pembaruan kemajuan, hambatan |
| Status Mingguan | PM, Dosen Pembimbing | Mingguan | 60 menit | Tinjauan kemajuan, panduan |
| Tinjauan Pemangku Kepentingan | PM, Pemilik, SME | Dua mingguan | 90 menit | Demo, umpan balik, keputusan |
| Perencanaan *Sprint* | Tim Pengembang | Setiap 2 minggu | 120 menit | Rencanakan pekerjaan mendatang |
| Retrospektif | Tim Pengembang | Setiap 2 minggu | 60 menit | Pelajaran dipetik, perbaikan |

**Pelaporan:**

1. **Laporan Status Mingguan** (Email ke Pemilik dan Dosen)
   - Pencapaian minggu ini
   - Aktivitas yang direncanakan minggu depan
   - Masalah dan hambatan
   - Status anggaran
   - Risiko dan mitigasi

2. **Laporan Kemajuan Bulanan** (Dokumen formal)
   - Ringkasan eksekutif
   - Kemajuan terperinci per paket kerja
   - Pencapaian tonggak (*milestone*)
   - Anggaran vs. aktual
   - Jadwal yang diperbarui
   - Daftar risiko
   - Foto/*screenshot*

### 4.2.8 Manajemen Pengadaan (jika ada)

Untuk proyek ini, pengadaan minimal karena sebagian besar menggunakan alat *open-source* dan layanan gratis. Namun, beberapa item yang diadakan:

| Item | Vendor | Jenis Kontrak | Jumlah | Status |
|------|--------|---------------|--------|--------|
| *Hosting* VPS | Niagahoster/IDCloudHost | Harga Tetap | Rp 900.000 | Dipesan |
| Registrasi Domain | Namecheap/Niagahoster | Harga Tetap | Rp 150.000 | Dipesan |
| *Payment Gateway* (Midtrans) | Midtrans | Bayar per transaksi | Variabel | Terintegrasi |
| Layanan Email | SendGrid | Bayar sesuai penggunaan | Rp 200.000 | Aktif |
| Penyimpanan Cadangan | Google Drive Business | Langganan | Rp 150.000 | Aktif |

Semua pengadaan mengikuti proses standar:
1. Identifikasi kebutuhan
2. Riset dan perbandingan vendor
3. Persetujuan anggaran
4. Pemesanan/*signup*
5. Konfigurasi dan pengujian
6. Pemrosesan faktur

---

## 4.3 Deskripsi Produk / Layanan

### 4.3.1 Gambaran Umum Sistem

Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART adalah aplikasi web *full-stack* berbasis Laravel yang dirancang khusus untuk mendukung operasional pusat layanan hipnoterapi dan kesehatan mental. Sistem ini mengintegrasikan seluruh proses bisnis mulai dari pemesanan layanan, manajemen jadwal terapis, pelaksanaan sesi terapi, dokumentasi, hingga pelaporan dalam satu platform yang terpadu, aman, dan ramah pengguna.

**Karakteristik Utama Sistem:**

1. **Arsitektur Multi-Peran:** Mendukung tiga peran pengguna utama (Admin, Terapis, Klien) dengan hak akses dan antarmuka yang disesuaikan
2. **Ketersediaan *Real-Time*:** Menampilkan ketersediaan jadwal terapis secara *real-time* untuk pemesanan
3. **Alur Kerja Komprehensif:** Mencakup seluruh perjalanan klien dari kesadaran hingga tindak lanjut pasca-terapi
4. **Berbasis Data:** Menyediakan analitik dan pelaporan untuk intelijen bisnis
5. **Aman dan Patuh:** Mengikuti praktik keamanan terbaik dan regulasi kepatuhan
6. **Desain Responsif:** Dapat diakses dari desktop, tablet, dan *smartphone* dengan pengalaman yang optimal
7. **Arsitektur Skalabel:** Dapat menampung pertumbuhan pengguna dan data tanpa *refactoring* besar

**Arsitektur Sistem:**

Sistem menggunakan **Arsitektur Monolitik** dengan **Pola Model-View-Controller (MVC)**:

```
┌─────────────────────────────────────────────────────────────┐
│                  LAPISAN KLIEN                              │
│  (Browser Web - Desktop, Tablet, Mobile)                    │
└────────────┬────────────────────────────────────────────────┘
             │ Permintaan HTTPS
             ├─────────────────────────────────────────────────┐
             │                                                 │
┌────────────▼───────────────────────────────────────────┐   │
│            LAPISAN PRESENTASI                           │   │
│  ┌──────────────────────────────────────────────────┐  │   │
│  │    Templat Blade (Views)                         │  │   │
│  │  - Halaman Publik                                 │  │   │
│  │  - Halaman Autentikasi                           │  │   │
│  │  - Dasbor (Admin, Terapis, Klien)               │  │   │
│  │  - Komponen (Formulir, Tabel, Grafik)           │  │   │
│  └──────────────────────────────────────────────────┘  │   │
│  ┌──────────────────────────────────────────────────┐  │   │
│  │    Tailwind CSS + JavaScript                     │  │   │
│  └──────────────────────────────────────────────────┘  │   │
└────────────┬───────────────────────────────────────────┘   │
             │                                                 │
┌────────────▼───────────────────────────────────────────┐   │
│           LAPISAN APLIKASI                              │   │
│  ┌──────────────────────────────────────────────────┐  │   │
│  │          Rute (web.php)                          │  │   │
│  └──────────────────────────────────────────────────┘  │   │
│  ┌──────────────────────────────────────────────────┐  │   │
│  │    Middleware                                     │  │   │
│  │  - Autentikasi                                    │  │   │
│  │  - Otorisasi (Berbasis peran)                    │  │   │
│  │  - Proteksi CSRF                                  │  │   │
│  └──────────────────────────────────────────────────┘  │   │
│  ┌──────────────────────────────────────────────────┐  │   │
│  │        Kontroler                                  │  │   │
│  │  - AuthController                                 │  │   │
│  │  - BookingController                              │  │   │
│  │  - TherapistController                            │  │   │
│  │  - SessionController                              │  │   │
│  │  - PaymentController                              │  │   │
│  │  - DashboardController                            │  │   │
│  │  - ReportController                               │  │   │
│  └──────────────────────────────────────────────────┘  │   │
└────────────┬───────────────────────────────────────────┘   │
             │                                                 │
┌────────────▼───────────────────────────────────────────┐   │
│          LAPISAN LOGIKA BISNIS                          │   │
│  ┌──────────────────────────────────────────────────┐  │   │
│  │         Model (Eloquent ORM)                     │  │   │
│  │  - User, Therapist, Client                       │  │   │
│  │  - Service, Booking                              │  │   │
│  │  - Session, SessionNote                          │  │   │
│  │  - Payment, Transaction                          │  │   │
│  │  - Review, Progress                              │  │   │
│  └──────────────────────────────────────────────────┘  │   │
│  ┌──────────────────────────────────────────────────┐  │   │
│  │         Aturan Bisnis                            │  │   │
│  │  - Aturan Validasi                               │  │   │
│  │  - Logika Bisnis                                 │  │   │
│  │  - Relasi                                        │  │   │
│  └──────────────────────────────────────────────────┘  │   │
└────────────┬───────────────────────────────────────────┘   │
             │                                                 │
┌────────────▼───────────────────────────────────────────┐   │
│             LAPISAN DATA                                │   │
│  ┌──────────────────────────────────────────────────┐  │   │
│  │         Basis Data MySQL                         │  │   │
│  │  - Tabel (dinormalisasi ke 3NF)                 │  │   │
│  │  - Indeks untuk kinerja                          │  │   │
│  │  - Kunci Asing untuk integritas                 │  │   │
│  └──────────────────────────────────────────────────┘  │   │
└─────────────────────────────────────────────────────────┘   │
                                                               │
┌──────────────────────────────────────────────────────────┐ │
│          LAYANAN EKSTERNAL                                │ │
│  - Payment Gateway (Midtrans)                            │◄┘
│  - Layanan Email (SMTP)                                  │
│  - Layanan SMS (opsional)                                │
│  - Konferensi Video (Zoom/GMeet via iframe)             │
└──────────────────────────────────────────────────────────┘
```

**Tabel 4.11 Daftar Kebutuhan Fungsional**

| ID | Kebutuhan | Prioritas (MoSCoW) | Peran Pengguna | Kriteria Penerimaan | Status |
|----|-------------|-------------------|-----------|-------------------|--------|
| **FR-AUTH** | **Autentikasi & Otorisasi** | | | | |
| FR-AUTH-01 | Registrasi pengguna dengan verifikasi email | Harus Ada | Semua | Pengguna dapat registrasi, terima email, verifikasi akun | ✅ Terimplementasi |
| FR-AUTH-02 | Login dengan email dan kata sandi | Harus Ada | Semua | Pengguna dapat login dengan kredensial valid | ✅ Terimplementasi |
| FR-AUTH-03 | Lupa kata sandi dan *reset* via email | Harus Ada | Semua | Pengguna dapat *reset* kata sandi via tautan email | ✅ Terimplementasi |
| FR-AUTH-04 | Kontrol akses berbasis peran (Admin, Terapis, Klien) | Harus Ada | Semua | Setiap peran hanya akses fitur yang sesuai | ✅ Terimplementasi |
| FR-AUTH-05 | Fungsi *logout* | Harus Ada | Semua | Pengguna dapat *logout* dengan aman | ✅ Terimplementasi |
| **FR-BOOKING** | **Manajemen Pemesanan** | | | | |
| FR-BOOK-01 | Telusuri dan filter layanan | Harus Ada | Klien | Klien dapat lihat semua layanan dengan filter | ✅ Terimplementasi |
| FR-BOOK-02 | Lihat profil terapis dan ketersediaan | Harus Ada | Klien | Klien dapat lihat profil dan jadwal terapis | ✅ Terimplementasi |
| FR-BOOK-03 | Alur pemesanan 4 langkah (Layanan → Terapis → Tanggal/Waktu → Konfirmasi) | Harus Ada | Klien | Klien dapat selesaikan pemesanan dalam 4 langkah | ⏳ Sedang Berjalan |
| FR-BOOK-04 | Pengecekan ketersediaan *real-time* | Harus Ada | Klien | Sistem cegah pemesanan ganda | ⏳ Sedang Berjalan |
| FR-BOOK-05 | Email konfirmasi pemesanan | Harus Ada | Klien | Klien terima email setelah pemesanan | 🔜 Direncanakan |
| FR-BOOK-06 | Jadwal ulang pemesanan (min 24 jam sebelum) | Sebaiknya Ada | Klien | Klien dapat jadwal ulang dengan batasan | 🔜 Direncanakan |
| FR-BOOK-07 | Batalkan pemesanan dengan alasan | Sebaiknya Ada | Klien | Klien dapat batalkan pemesanan | 🔜 Direncanakan |
| **FR-SCHEDULE** | **Manajemen Jadwal** | | | | |
| FR-SCHED-01 | Atur ketersediaan mingguan (berulang) | Harus Ada | Terapis | Terapis atur jam kerja per hari | ✅ Terimplementasi |
| FR-SCHED-02 | Blokir tanggal tertentu (cuti, libur) | Harus Ada | Terapis | Terapis blokir tanggal tertentu | ✅ Terimplementasi |
| FR-SCHED-03 | Lihat kalender janji temu | Harus Ada | Terapis | Terapis lihat jadwal dalam tampilan kalender | ✅ Terimplementasi |
| FR-SCHED-04 | Terima/tolak permintaan pemesanan | Sebaiknya Ada | Terapis | Terapis bisa setujui atau tolak pemesanan | 🔜 Direncanakan |
| **FR-SESSION** | **Manajemen Sesi** | | | | |
| FR-SESS-01 | Mulai sesi (tandai sebagai dimulai) | Harus Ada | Terapis | Terapis mulai sesi tepat waktu | ⏳ Sedang Berjalan |
| FR-SESS-02 | Akhiri sesi dan input catatan sesi | Harus Ada | Terapis | Terapis dokumentasi sesi secara terstruktur | ⏳ Sedang Berjalan |
| FR-SESS-03 | Unggah lampiran sesi (file, gambar) | Bisa Ada | Terapis | Terapis unggah dokumen pendukung | 🔜 Direncanakan |
| FR-SESS-04 | Lihat riwayat sesi dengan catatan | Harus Ada | Terapis | Terapis akses riwayat sesi klien | ⏳ Sedang Berjalan |
| FR-SESS-05 | Klien lihat catatan sesi sendiri (ringkasan saja) | Sebaiknya Ada | Klien | Klien lihat ringkasan kemajuan | 🔜 Direncanakan |
| **FR-PAYMENT** | **Manajemen Pembayaran** | | | | |
| FR-PAY-01 | Beberapa metode pembayaran (transfer, kartu kredit, *ewallet*) | Harus Ada | Klien | Klien pilih metode pembayaran | ⏳ Sedang Berjalan |
| FR-PAY-02 | Integrasi *payment gateway* (Midtrans) | Harus Ada | Klien | Klien bayar via *payment gateway* | ⏳ Sedang Berjalan |
| FR-PAY-03 | Unggah bukti pembayaran (transfer manual) | Harus Ada | Klien | Klien unggah bukti transfer | ⏳ Sedang Berjalan |
| FR-PAY-04 | Admin verifikasi pembayaran manual | Harus Ada | Admin | Admin setujui/tolak pembayaran | ⏳ Sedang Berjalan |
| FR-PAY-05 | Notifikasi konfirmasi pembayaran | Harus Ada | Klien | Klien diberi tahu setelah pembayaran dikonfirmasi | 🔜 Direncanakan |
| FR-PAY-06 | Lihat riwayat pembayaran dan faktur | Sebaiknya Ada | Klien | Klien unduh faktur | 🔜 Direncanakan |
| **FR-PROGRESS** | **Pelacakan Kemajuan** | | | | |
| FR-PROG-01 | Lacak kemajuan klien dengan metrik | Sebaiknya Ada | Terapis | Terapis input dan lacak kemajuan | 🔜 Direncanakan |
| FR-PROG-02 | Visualisasi kemajuan dengan grafik | Sebaiknya Ada | Klien | Klien lihat kemajuan dalam grafik | 🔜 Direncanakan |
| FR-PROG-03 | Atur tujuan dan tonggak terapi | Bisa Ada | Terapis | Terapis atur tujuan untuk klien | 🔜 Direncanakan |
| **FR-REVIEW** | **Ulasan & Umpan Balik** | | | | |
| FR-REV-01 | Klien kirim ulasan setelah sesi | Sebaiknya Ada | Klien | Klien beri nilai dan ulasan terapis | 🔜 Direncanakan |
| FR-REV-02 | Terapis tanggapi ulasan | Bisa Ada | Terapis | Terapis balas ulasan | 🔜 Direncanakan |
| FR-REV-03 | Admin moderasi ulasan | Sebaiknya Ada | Admin | Admin setujui/sembunyikan ulasan tidak pantas | 🔜 Direncanakan |
| **FR-ADMIN** | **Manajemen Admin** | | | | |
| FR-ADM-01 | Kelola pengguna (CRUD) | Harus Ada | Admin | Admin kelola semua pengguna | ⏳ Sedang Berjalan |
| FR-ADM-02 | Kelola layanan (CRUD) | Harus Ada | Admin | Admin kelola layanan | ⏳ Sedang Berjalan |
| FR-ADM-03 | Lihat semua pemesanan dan status | Harus Ada | Admin | Admin pantau semua pemesanan | ⏳ Sedang Berjalan |
| FR-ADM-04 | Buat laporan keuangan | Sebaiknya Ada | Admin | Admin ekspor laporan keuangan | 🔜 Direncanakan |
| FR-ADM-05 | Konfigurasi dan pengaturan sistem | Harus Ada | Admin | Admin ubah pengaturan sistem | ⏳ Sedang Berjalan |
| **FR-NOTIF** | **Notifikasi** | | | | |
| FR-NOTIF-01 | Notifikasi email untuk peristiwa pemesanan | Harus Ada | Semua | Pengguna terima email untuk pembaruan pemesanan | 🔜 Direncanakan |
| FR-NOTIF-02 | Email pengingat (24 jam dan 1 jam sebelum sesi) | Sebaiknya Ada | Klien | Klien terima pengingat | 🔜 Direncanakan |
| FR-NOTIF-03 | Lencana notifikasi dalam aplikasi | Bisa Ada | Semua | Pengguna lihat jumlah notifikasi | 🔜 Direncanakan |

**Total Kebutuhan:** 48 kebutuhan fungsional  
**Harus Ada:** 29 (60%)  
**Sebaiknya Ada:** 14 (29%)  
**Bisa Ada:** 5 (11%)  
**Status Implementasi:** 45% selesai (per Nov 2024)

---

**Tabel 4.12 Non-Functional Requirements**

| ID | Category | Requirement | Metric/Target | Testing Method | Priority |
|----|----------|-------------|---------------|----------------|----------|
| **NFR-PERF** | **Performance** | | | | |
| NFR-PERF-01 | Response Time | Page load time < 3 seconds (desktop) | < 3s | Lighthouse, GTmetrix | Critical |
| NFR-PERF-02 | Response Time | API response time < 500ms | < 500ms | Postman, browser DevTools | High |
| NFR-PERF-03 | Response Time | Time to First Byte < 600ms | < 600ms | WebPageTest | High |
| NFR-PERF-04 | Throughput | Support 100 concurrent users | 100 users | Load testing (Apache JMeter) | High |
| NFR-PERF-05 | Database Performance | Query execution < 100ms | < 100ms | MySQL slow query log | High |
| **NFR-SEC** | **Security** | | | | |
| NFR-SEC-01 | Authentication | Secure password hashing (bcrypt) | All passwords encrypted | Code review | Critical |
| NFR-SEC-02 | Authorization | Role-based access control (RBAC) | Unauthorized access blocked | Penetration testing | Critical |
| NFR-SEC-03 | Data Protection | Sensitive data encrypted at rest | Client medical data encrypted | Security audit | Critical |
| NFR-SEC-04 | Communication | HTTPS only (SSL certificate) | All traffic encrypted | SSL test | Critical |
| NFR-SEC-05 | Input Validation | Protection against SQL injection | No SQL vulnerabilities | OWASP ZAP scan | Critical |
| NFR-SEC-06 | Input Validation | Protection against XSS attacks | No XSS vulnerabilities | Security testing | Critical |
| NFR-SEC-07 | Session Management | Secure session handling dengan timeout | Session expires after 30 min inactive | Manual testing | High |
| NFR-SEC-08 | CSRF Protection | CSRF token validation | All forms protected | Code review | Critical |
| **NFR-USAB** | **Usability** | | | | |
| NFR-USAB-01 | Learnability | First-time user dapat booking tanpa training | 90% task success rate | Usability testing | High |
| NFR-USAB-02 | User Satisfaction | System Usability Scale (SUS) score | ≥ 80/100 | SUS questionnaire (10 users) | Critical |
| NFR-USAB-03 | Error Prevention | Clear validation messages | < 5% error rate per task | Usability testing | High |
| NFR-USAB-04 | Accessibility | WCAG 2.1 Level AA compliance | Pass aXe audit | aXe DevTools, Lighthouse | High |
| NFR-USAB-05 | Consistency | Consistent UI across all pages | Design system followed | Design review | High |
| **NFR-REL** | **Reliability** | | | | |
| NFR-REL-01 | Availability | System uptime | ≥ 99% monthly | Uptime monitoring (UptimeRobot) | Critical |
| NFR-REL-02 | Fault Tolerance | Graceful error handling | No unhandled exceptions | Error logging (Sentry) | High |
| NFR-REL-03 | Data Integrity | Database constraints enforced | No orphan records | Database testing | Critical |
| NFR-REL-04 | Backup & Recovery | Daily automated backup | RPO < 24 hours | Backup verification | High |
| **NFR-MAINT** | **Kemudahan Pemeliharaan** | | | | |
| NFR-MAINT-01 | Kualitas Kode | Ikuti standar *coding* PSR-12 | Grade A (SonarQube) | Analisis kode statis | Tinggi |
| NFR-MAINT-02 | Dokumentasi | Dokumentasi kode komprehensif | Semua metode publik terdokumentasi | Tinjauan kode | Tinggi |
| NFR-MAINT-03 | Modularitas | *Loosely coupled*, *high cohesion* | Kompleksitas siklomatis < 10 | Metrik kode | Tinggi |
| NFR-MAINT-04 | Kontrol Versi | Strategi *branching* Git | Semua perubahan di-*commit* | Tinjauan riwayat Git | Tinggi |
| **NFR-SCALE** | **Skalabilitas** | | | | |
| NFR-SCALE-01 | Volume Data | Menangani 10.000+ pengguna | Kinerja basis data stabil | Uji beban | Sedang |
| NFR-SCALE-02 | Volume Data | Menangani 100.000+ pemesanan per tahun | Kinerja *query* terjaga | Uji *stress* | Sedang |
| NFR-SCALE-03 | Pengguna Bersamaan | Mendukung 500 pengguna bersamaan (masa depan) | Sumber daya server memadai | Uji beban | Sedang |
| **NFR-COMPAT** | **Kompatibilitas** | | | | |
| NFR-COMPAT-01 | Dukungan *Browser* | Chrome, Firefox, Safari, Edge (2 versi terbaru) | Fungsionalitas penuh | Pengujian *cross-browser* | Kritis |
| NFR-COMPAT-02 | Desain Responsif | *Mobile*, tablet, desktop (320px - 1920px) | UI menyesuaikan dengan baik | Pengujian responsif | Kritis |
| NFR-COMPAT-03 | Lingkungan Server | PHP 8.2+, MySQL 8.0+, Ubuntu 22.04 LTS | Sistem berjalan tanpa masalah | Pengujian *deployment* | Kritis |

**Total NFR:** 33 kebutuhan  
**Prioritas Kritis:** 19 (58%)  
**Prioritas Tinggi:** 12 (36%)  
**Prioritas Sedang:** 2 (6%)

---

**Tabel 4.13 Perbandingan Tumpukan Teknologi**

| Komponen | Opsi 1 | Opsi 2 | Opsi 3 | Dipilih | Alasan |
|-----------|----------|----------|----------|----------|-----------|
| ***Framework Backend*** | Laravel 10 | Express.js (Node.js) | Django (Python) | ✅ Laravel 10 | MVC *built-in*, Eloquent ORM, ekosistem besar, kebutuhan akademik, keahlian tim |
| **Bahasa Pemrograman** | PHP 8.2 | JavaScript (Node) | Python 3.11 | ✅ PHP 8.2 | Fitur modern (*enum*, *readonly*), *strong typing*, kompatibilitas Laravel |
| **Basis Data** | MySQL 8.0 | PostgreSQL 15 | MongoDB 6.0 | ✅ MySQL 8.0 | Kepatuhan ACID, data relasional cocok, gratis, dukungan *hosting* luas |
| ***Framework* CSS** | Tailwind CSS 3.3 | Bootstrap 5 | CSS Kustom | ✅ Tailwind 3.3 | *Utility-first*, sangat dapat disesuaikan, ukuran *bundle* lebih kecil, modern |
| **JavaScript** | Alpine.js 3.x | Vue.js 3 | React 18 | ✅ Alpine.js | Ringan (15KB), deklaratif, *overhead* minimal, kompatibel Laravel Livewire |
| **Mesin Templat** | Blade (Laravel) | Twig | PHP Biasa | ✅ Blade | *Built-in* Laravel, sintaks bersih, pewarisan templat, direktif |
| **Autentikasi** | Laravel Sanctum | Laravel Passport | JWT (tymon/jwt-auth) | ✅ Sanctum | Ringan, ramah SPA, berbasis token, dibuat untuk Laravel |
| ***Payment Gateway*** | Midtrans | Xendit | Stripe | ✅ Midtrans | Fokus Indonesia, beberapa metode pembayaran, dokumentasi baik, biaya terjangkau |
| **Layanan Email** | SendGrid | Mailgun | AWS SES | ✅ SendGrid | Andal, 100 email/hari gratis, *deliverability* baik, integrasi mudah |
| ***Hosting*** | Niagahoster VPS | DigitalOcean Droplet | AWS EC2 | ✅ Niagahoster VPS | Berbasis Indonesia, terjangkau (Rp 300k/bln), terkelola, dukungan lokal |
| **Kontrol Versi** | GitHub | GitLab | Bitbucket | ✅ GitHub | Repo privat gratis, CI/CD (Actions), komunitas besar, familiar |
| **Manajemen Tugas** | Asana | Trello | Jira | ✅ Asana | Dependensi tugas, tampilan *timeline*, tier gratis cukup, kolaboratif |
| **Alat Desain** | Figma | Adobe XD | Sketch | ✅ Figma | Kolaboratif, berbasis *browser*, tier gratis, pustaka komponen, *prototyping* |
| **Pengujian API** | Postman | Insomnia | Thunder Client | ✅ Postman | Koleksi, variabel lingkungan, sinkronisasi tim, komprehensif |
| **Alat Basis Data** | MySQL Workbench | phpMyAdmin | DBeaver | ✅ MySQL Workbench | Perancang ERD visual, alat optimasi *query*, dukungan migrasi |
| **Pelacakan Error** | Sentry | Rollbar | Bugsnag | ✅ Sentry | Pemberitahuan *real-time*, *stack trace*, tier gratis 5k *event*/bln, integrasi Laravel |
| **Pemantauan** | UptimeRobot | Pingdom | StatusCake | ✅ UptimeRobot | Gratis 50 monitor, interval 5 menit, pemberitahuan email/SMS, halaman status publik |

**Kriteria Pemilihan Utama:**
1. **Biaya:** Gratis atau terjangkau untuk anggaran Rp 5 juta
2. **Kurva Belajar:** Tim familiar atau mudah dipelajari
3. **Dukungan Komunitas:** Komunitas besar, dokumentasi baik
4. **Integrasi:** Integrasi mulus dengan *stack* lain
5. **Skalabilitas:** Dapat menangani pertumbuhan
6. **Kebutuhan Akademik:** Harus menggunakan Laravel (batasan akademik)

---

### 4.3.2 Fitur-Fitur Utama Sistem

Sistem terdiri dari **41 halaman interface** yang dikelompokkan berdasarkan fungsi:

#### A. Public Pages (8 halaman)

**1. Landing Page (01_landing.html)**

Halaman utama yang menjadi first touchpoint untuk visitors. Dirancang untuk conversion optimization dengan elemen:

- **Hero Section:** 
  - Headline yang powerful: "Transformasi Diri Dimulai Dari Sini"
  - Subheadline yang menjelaskan value proposition
  - Primary CTA button: "Booking Sekarang"
  - Hero image/illustration yang calming dan relatable
  
- **Services Overview:**
  - Grid layout menampilkan 6 layanan utama dengan icon dan deskripsi singkat
  - Hover effect untuk interactivity
  - Link ke detail masing-masing layanan
  
- **Why Choose Us Section:**
  - USPs (Unique Selling Points): Terapis bersertifikat, metode scientific, lingkungan rahasia
  - Statistics: "500+ Klien Terbantu", "95% Success Rate", "4.8★ Average Rating"
  
- **How It Works:**
  - 4-step process illustration: Pilih Layanan → Pilih Terapis → Jadwalkan → Terapi
  - Visual icons untuk each step
  
- **Testimonials:**
  - Carousel menampilkan 5-6 testimonials dari klien dengan foto, nama, dan quote
  - Star ratings visible
  
- **Latest Articles (Blog Preview):**
  - 3 artikel terbaru dengan thumbnail, title, excerpt, dan "Read More" link
  
- **CTA Section:**
  - Encouraging message dengan button ke registration/booking
  
- **Footer:**
  - Quick links (About, Services, Therapists, Blog, Contact, FAQ)
  - Social media icons
  - Informasi hak cipta (*copyright*)
  - Tautan Kebijakan Privasi dan Syarat & Ketentuan

**2. Halaman Tentang Kami (02_about.html)**

Halaman "Tentang Kami" yang membangun kepercayaan dan kredibilitas:

- **Kisah Perusahaan:** Narasi tentang pendirian CUR-HEART, visi, misi
- **Pendekatan Kami:** Penjelasan tentang pendekatan hipnoterapi yang digunakan
- **Sertifikasi:** Tampilan sertifikat dan akreditasi
- **Bagian Tim:** Foto dan biografi dari pendiri/manajemen kunci
- **Nilai:** Nilai inti perusahaan (Profesional, Empatik, Ilmiah, Rahasia)
- **Pencapaian:** Tonggak pencapaian dan pengakuan yang diterima

**3. Halaman Layanan (03_services.html)**

Katalog lengkap semua layanan dengan fitur penyaringan:

- **Kisi-Kisi Layanan:** Tata letak kartu untuk 6 layanan, setiap kartu berisi:
  - Ikon/ilustrasi representatif
  - Nama layanan
  - Deskripsi singkat (2-3 kalimat)
  - Durasi dan rentang harga
  - Tombol "Pelajari Lebih Lanjut" → tautan ke halaman detail layanan
  
- **Opsi Penyaringan/Pengurutan:**
  - Saring berdasarkan kategori (Manajemen Stres, Pertumbuhan Pribadi, Perubahan Kebiasaan)
  - Urutkan berdasarkan popularitas, harga, durasi
  
- **Bagian FAQ:** Pertanyaan umum tentang layanan

**4. Halaman Detail Layanan (04_services_detail.html)**

Halaman detail untuk setiap layanan individual:

- ***Header* Layanan:** Nama, ikon, navigasi *breadcrumb*
- **Deskripsi Detail:** Penjelasan komprehensif tentang layanan
- **Apa yang Diharapkan:** Garis besar tentang apa yang terjadi selama sesi
- **Manfaat:** Daftar poin manfaat yang bisa didapatkan
- **Ideal Untuk:** Audiens target/kondisi yang sesuai
- **Durasi & Harga:** Informasi jelas
- **Kisah Sukses:** Testimoni spesifik untuk layanan ini
- **Terapis Tersedia:** Daftar terapis yang menyediakan layanan ini dengan foto, nama, spesialisasi
- **Tombol CTA:** "Pesan Layanan Ini" → arahkan ke alur pemesanan

**5. Direktori Terapis (05_therapists.html)**

Direktori semua terapis dengan fitur penyaringan dan pencarian:

- **Kisi-Kisi Terapis:** Tata letak kartu, setiap kartu menampilkan:
  - Foto profesional
  - Nama dan kredensial (M.Psi., C.Ht.)
  - Spesialisasi (*tag*: Kecemasan, Trauma, Motivasi)
  - Tahun pengalaman
  - Peringkat (mis., 4,9★ dari 120 ulasan)
  - Tombol "Lihat Profil"
  
- **Opsi Penyaringan:**
  - Berdasarkan spesialisasi
  - Berdasarkan peringkat
  - Berdasarkan ketersediaan
  - Berdasarkan tahun pengalaman
  
- **Bilah Pencarian:** Cari berdasarkan nama
- **Opsi Pengurutan:** Nama A-Z, Peringkat, Pengalaman

**6. Halaman Profil Terapis (06_therapist_profile.html)**

Halaman detail profil untuk terapis individual:

- ***Header* Profil:**
  - Foto profesional besar
  - Nama, kredensial, gelar
  - Peringkat dan total ulasan
  - Tahun pengalaman
  - Spesialisasi (lencana/*tag*)
  - Tombol "Pesan dengan Terapis Ini"
  
- **Bagian Tentang:** Paragraf biografi tentang latar belakang, filosofi, pendekatan
- **Pendidikan:** Daftar pendidikan formal dengan institusi dan tahun
- **Sertifikasi:** Sertifikasi profesional dengan badan penerbit
- **Layanan yang Ditawarkan:** Layanan-layanan yang dikuasai
- **Kalender Ketersediaan:** Kalender mini menampilkan tanggal tersedia (pratinjau 2 minggu ke depan)
- **Bagian Ulasan:**
  - Rincian peringkat keseluruhan (5★: 80%, 4★: 15%, dll.)
  - Ulasan individual dengan nama klien (dianonimkan jika diinginkan), tanggal, peringkat, komentar
  - Halaman berganda untuk banyak ulasan
  
- **Terapis Terkait:** Bagian "Anda mungkin juga suka" dengan 3 terapis serupa

**7. Halaman Daftar Blog (07_blog_list.html)**

Halaman arsip untuk semua artikel blog/konten edukatif:

- **Artikel Unggulan:** Bagian *hero* dengan artikel terbaru atau unggulan
- **Kisi-Kisi Artikel:** Tata letak kartu untuk artikel, setiap kartu berisi:
  - Gambar mini
  - *Tag* kategori (mis., Kesehatan Mental, Perawatan Diri, Kisah Sukses)
  - Judul
  - Kutipan (150 karakter pertama)
  - Nama penulis dan tanggal publikasi
  - Tautan "Baca Selengkapnya"
  
- **Bilah Samping:**
  - Bilah pencarian
  - Daftar kategori
  - Artikel populer
  - Awan *tag*
  
- **Halaman Berganda:** Navigasi melalui beberapa halaman artikel

**8. Halaman Detail Blog (08_blog_detail.html)**

Halaman artikel individual:

- ***Header* Artikel:**
  - Judul (H1)
  - Informasi penulis dengan foto
  - Tanggal publikasi dan estimasi waktu baca
  - Kategori dan *tag*
  - Tombol bagikan (media sosial)
  
- **Konten Artikel:**
  - Konten teks kaya dengan gambar, judul, daftar, kutipan
  - Tipografi dan spasi yang tepat untuk keterbacaan
  - Daftar isi untuk artikel panjang (bilah samping lengket/*sticky*)
  
- **Keterlibatan:**
  - Tombol suka/membantu
  - Bagian komentar (opsional)
  
- **Artikel Terkait:** 3-4 artikel terkait di bagian bawah
- **CTA:** "Siap memulai perjalanan Anda? Pesan sesi sekarang"

#### B. Halaman Dukungan (4 halaman)

**9. Halaman Kontak (09_contact.html)**

- **Formulir Kontak:** Kolom nama, email, telepon, subjek, pesan
- **Informasi Kontak:** Alamat, nomor telepon, email, jam operasional
- **Peta Google *Embed*:** Peta interaktif menampilkan lokasi
- **Tautan Media Sosial**
- **Tautan FAQ:** Arahkan ke halaman FAQ untuk pertanyaan umum

**10. Halaman FAQ (10_faq.html)**

- **Bilah Pencarian:** Cari melalui FAQ
- **Kategori:** Umum, Pemesanan, Layanan, Pembayaran, Privasi
- **Tata Letak Akordeon:** Klik untuk memperluas jawaban
- **Ajakan Kontak:** "Tidak menemukan jawaban Anda? Hubungi kami"

**11. Halaman Kebijakan Privasi (11_privacy_policy.html)**

- **Dokumen Legal:** Kebijakan privasi komprehensif
- **Bagian:** Pengumpulan data, penggunaan, perlindungan, hak, *cookie*
- **Tanggal Pembaruan Terakhir**
- **Pernyataan Kepatuhan:** UU No. 27 Tahun 2022 tentang PDP

**12. Halaman Syarat & Ketentuan (12_terms_conditions.html)**

- **Dokumen Legal:** Syarat layanan
- **Bagian:** Kewajiban pengguna, penggunaan layanan, kebijakan pembatalan, tanggung jawab, sengketa
- **Kotak Centang Penerimaan:** Diperlukan saat pendaftaran

#### C. Halaman Autentikasi (4 halaman)

**13. Halaman Login (13_login.html)**

- **Formulir Login:**
  - Kolom email
  - Kolom kata sandi dengan tombol tampilkan/sembunyikan
  - Kotak centang "Ingat Saya"
  - Tautan "Lupa Kata Sandi?"
  - Tombol "Masuk" (CTA utama)
  
- **Login Sosial (opsional):** Tombol login Google, Facebook
- **Tautan Pendaftaran:** "Belum punya akun? Daftar"
- **Pencitraan Merek (*Branding*):** Logo, *tagline*
- **Ilustrasi/Gambar:** Visual menenangkan di samping (tata letak layar terpisah/*split-screen*)

**14. Halaman Pendaftaran (14_register.html)**

- **Formulir Pendaftaran:**
  - Nama Lengkap
  - Alamat Email
  - Nomor Telepon
  - Kata Sandi (dengan indikator kekuatan)
  - Konfirmasi Kata Sandi
  - Kotak centang penerimaan Syarat & Ketentuan
  
- **Pemilihan Tipe Pengguna:**
  - Tombol radio atau *tab*: "Klien" atau "Terapis"
  - Formulir berbeda untuk setiap tipe (terapis memerlukan info tambahan: kredensial, spesialisasi)
  
- **Tombol "Buat Akun"**
- **Tautan Login:** "Sudah punya akun? Masuk"
- **Pemberitahuan Verifikasi Email:** "Kami akan mengirim email verifikasi"

**15. Halaman Lupa Kata Sandi (15_forgot_password.html)**

- **Teks Instruksi:** "Masukkan email Anda untuk menerima tautan pengaturan ulang"
- **Kolom Input Email**
- **Tombol "Kirim Tautan Pengaturan Ulang"**
- **Tautan Kembali ke Login**
- **Pesan Sukses:** "Tautan pengaturan ulang terkirim! Periksa email Anda"

**16. Halaman Atur Ulang Kata Sandi (16_reset_password.html)**

- **Validasi Token:** Sistem memeriksa apakah token pengaturan ulang valid dan tidak kedaluwarsa
- **Formulir Kata Sandi Baru:**
  - Kolom Kata Sandi Baru dengan indikator kekuatan
  - Kolom Konfirmasi Kata Sandi Baru
  
- **Tombol "Atur Ulang Kata Sandi"**
- **Pengalihan Sukses:** Setelah pengaturan ulang berhasil, arahkan ke login dengan pesan sukses

#### D. Dasbor Klien (10 halaman)

**17. Dasbor Utama Klien (17_client_dashboard.html)**

Dasbor ikhtisar untuk klien setelah login:

- ***Header* Sambutan:** "Selamat datang kembali, [Nama Klien]!"
- **Kartu Ringkasan:**
  - Janji Temu Mendatang (jumlah dengan detail janji temu berikutnya)
  - Sesi Selesai (total jumlah)
  - Skor Kemajuan (persentase atau skor)
  - Pembayaran Tertunda (jika ada)
  
- ***Widget* Janji Temu Mendatang:**
  - Daftar 2-3 janji temu mendatang dengan:
    - Tanggal dan waktu
    - Nama layanan
    - Nama terapis dan foto
    - Tombol "Lihat Detail" atau "Gabung Sesi" (jika *online*)
  - Tautan "Lihat Semua" → arahkan ke halaman janji temu
  
- **Tindakan Cepat:**
  - Tombol besar: "Pesan Sesi Baru", "Lihat Kemajuan Saya", "Hubungi Terapis"
  
- **Linimasa Aktivitas Terkini:**
  - Sesi terakhir selesai
  - Pembayaran dikonfirmasi
  - Janji temu dijadwalkan ulang
  - dll.
  
- **Pengumuman/Berita:**
  - Pengumuman sistem
  - Tips hari ini
  - Acara atau lokakarya mendatang
  
- **Kutipan Motivasi:** Kutipan kesehatan mental atau afirmasi acak

**18. Pemesanan Langkah 1 - Pilih Layanan (18_booking_step1.html)**

Tahap 1 dari alur pemesanan 4 langkah:

- **Indikator Kemajuan:** *Stepper* visual menampilkan "Langkah 1 dari 4"
- **Judul Halaman:** "Pilih Layanan Anda"
- **Kisi-Kisi Layanan:** Mirip dengan katalog layanan, tetapi dengan mekanisme pemilihan:
  - Tombol radio atau kartu yang dapat diklik
  - Sorot layanan yang dipilih
  
- **Pratinjau Layanan:** Saat layanan dipilih, tampilkan:
  - Deskripsi lengkap
  - Durasi
  - Harga
  
- **Navigasi:**
  - Tombol "Berikutnya" (diaktifkan hanya saat layanan dipilih) → ke Langkah 2
  - Tombol "Batal" → kembali ke dasbor

**19. Pemesanan Langkah 2 - Pilih Terapis (19_booking_step2.html)**

- **Indikator Kemajuan:** "Langkah 2 dari 4"
- **Judul Halaman:** "Pilih Terapis Anda"
- **Penyaringan:** Tampilkan hanya terapis yang menyediakan layanan yang dipilih
- **Kisi-Kisi Terapis:** Mirip dengan direktori, dengan pemilihan:
  - Tombol radio atau kartu yang dapat diklik
  - Tampilkan indikator ketersediaan (mis., "Tersedia minggu ini")
  
- **Pratinjau Terapis:** Saat dipilih, tampilkan:
  - Ringkasan profil
  - Spesialisasi
  - Peringkat
  - Tautan "Lihat Profil Lengkap" (buka modal atau *tab* baru)
  
- **Navigasi:**
  - Tombol "Kembali" → kembali ke Langkah 1
  - Tombol "Berikutnya" → ke Langkah 3

**20. Pemesanan Langkah 3 - Pilih Tanggal & Waktu (20_booking_step3.html)**

- **Indikator Kemajuan:** "Langkah 3 dari 4"
- **Judul Halaman:** "Pilih Tanggal & Waktu"
- ***Widget* Kalender:** Kalender interaktif menampilkan:
  - Tanggal tersedia (dapat diklik)
  - Tanggal tidak tersedia (berwarna abu-abu)
  - Bulan saat ini dengan navigasi sebelumnya/berikutnya
  
- **Slot Waktu:** Saat tanggal dipilih, tampilkan slot waktu tersedia:
  - Kisi tombol: "09:00", "10:30", "13:00", dll.
  - Dinonaktifkan/berwarna abu-abu untuk slot yang sudah dipesan
  - Sorot slot yang dipilih
  
- **Tampilan Durasi:** "Durasi sesi: 60 menit"
- **Ringkasan Pilihan:** Kotak menampilkan:
  - Layanan: [Nama]
  - Terapis: [Nama]
  - Tanggal: [Tanggal Dipilih]
  - Waktu: [Waktu Dipilih]
  
- **Navigasi:**
  - Tombol "Kembali" → Langkah 2
  - Tombol "Berikutnya" → Langkah 4

**21. Pemesanan Langkah 4 - Konfirmasi & Pembayaran (21_booking_step4.html)**

- **Indikator Kemajuan:** "Langkah 4 dari 4"
- **Judul Halaman:** "Konfirmasi & Bayar"
- **Ringkasan Pemesanan:** Rekap lengkap:
  - Nama layanan, deskripsi, durasi
  - Nama terapis, foto
  - Tanggal dan waktu
  - Lokasi (jika fisik) atau "Sesi *Online*"
  - Subtotal
  - Pajak (jika berlaku)
  - Total jumlah
  
- **Informasi Klien:** Terisi otomatis dengan data pengguna yang login:
  - Nama
  - Email
  - Telepon
  - Catatan/permintaan khusus (*textarea* - opsional)
  
- **Pemilihan Metode Pembayaran:**
  - Tombol radio:
    - Kartu Kredit/Debit (via *payment gateway*)
    - Transfer Bank (manual)
    - Dompet Digital (*E-Wallet*) (GoPay, OVO, Dana)
    - QRIS
  
- **Persetujuan Syarat:** Kotak centang untuk menyetujui kebijakan pembatalan
- **Navigasi:**
  - Tombol "Kembali" → Langkah 3
  - Tombol "Konfirmasi & Bayar" (CTA utama) → proses pembayaran

**22. Halaman Sukses Pemesanan (22_booking_success.html)**

Halaman konfirmasi setelah pemesanan berhasil:

- **Ikon Sukses:** Tanda centang besar atau animasi sukses
- **Pesan Sukses:** "Pemesanan Dikonfirmasi!"
- **Detail Pemesanan:**
  - Nomor referensi pemesanan
  - Layanan, Terapis, Tanggal, Waktu
  - Status pembayaran
  
- **Langkah Berikutnya:**
  - "Anda akan menerima email konfirmasi di [email]"
  - "Pengingat akan dikirim 1 hari sebelum sesi"
  - Jika *online*: "Tautan untuk bergabung akan dikirim via email"
  
- **Tindakan:**
  - Tombol "Lihat Janji Temu Saya" → ke halaman janji temu
  - Tombol "Pesan Sesi Lain" → mulai ulang alur pemesanan
  - Tombol "Unduh Konfirmasi" → hasilkan PDF

**23. Daftar Janji Temu Klien (23_client_appointments.html)**

Tampilan daftar semua janji temu klien:

- **Pengalih Tampilan:** *Tab* atau tombol untuk beralih:
  - Tampilan Daftar (*default*)
  - Tampilan Kalender
  
- **Opsi Penyaringan:**
  - Status: Semua, Mendatang, Selesai, Dibatalkan
  - Pemilih rentang tanggal
  
- **Daftar Janji Temu:** Tabel atau tata letak kartu, setiap baris/kartu menampilkan:
  - Tanggal & Waktu
  - Nama layanan
  - Nama terapis dan foto
  - Lencana status (Mendatang: biru, Selesai: hijau, Dibatalkan: merah)
  - *Dropdown* tindakan:
    - Lihat Detail
    - Jadwalkan Ulang (jika mendatang)
    - Batalkan (jika mendatang dan dalam kebijakan)
    - Gabung Sesi (jika *online* dan waktu bergabung)
    - Unduh Tanda Terima
  
- **Halaman Berganda:** Navigasi melalui halaman jika banyak janji temu
- **Keadaan Kosong:** Jika tidak ada janji temu, tampilkan pesan mendorong dan tombol "Pesan Sesi Pertama Anda"

**24. Halaman Detail Janji Temu (24_appointment_detail.html)**

Halaman detail untuk janji temu individual:

- ***Breadcrumb*:** Dasbor > Janji Temu > [ID Pemesanan]
- ***Header* Janji Temu:**
  - Lencana status
  - Nomor referensi pemesanan
  - Tanggal dibuat
  
- **Bagian Detail:**
  - **Informasi Layanan:**
    - Nama dan deskripsi layanan
    - Durasi
    - Harga
  
  - **Informasi Terapis:**
    - Foto, nama, kredensial
    - Spesialisasi
    - Tombol kontak (buka perpesanan)
  
  - **Jadwal:**
    - Tanggal dan waktu
    - Lokasi atau tautan *online* (jika waktu sesi)
  
  - **Catatan Klien:** Permintaan khusus yang dikirimkan
  - **Catatan Terapis:** (terlihat setelah sesi) Ringkasan dari terapis
  
- **Informasi Pembayaran:**
  - Jumlah
  - Metode pembayaran
  - Status pembayaran
  - ID transaksi
  - Tombol unduh faktur
  
- **Tindakan:**
  - Jika mendatang:
    - Tombol "Jadwalkan Ulang"
    - Tombol "Batalkan Janji Temu" (dengan modal konfirmasi)
    - Tombol "Tambah ke Kalender" (unduh file .ics)
  - Jika *online* dan waktu bergabung:
    - Tombol "Gabung Sesi" (besar, menonjol)
  - Jika selesai:
    - Tombol "Berikan Ulasan"
    - Tombol "Pesan Lagi dengan Terapis yang Sama"

**25. Pelacakan Kemajuan Klien (25_client_progress.html)**

Visualisasi kemajuan terapi klien:

- **Kartu Ikhtisar Kemajuan:**
  - Total Sesi Selesai
  - *Streak* Saat Ini (minggu/bulan berturut-turut)
  - Skor Kemajuan Keseluruhan (berbasis algoritma)
  - Persentase Peningkatan
  
- **Riwayat Penilaian Mandiri:**
  - Grafik garis menampilkan skor dari waktu ke waktu
  - Beberapa seri untuk metrik berbeda (mis., Tingkat Kecemasan, Tingkat Kepercayaan Diri, Kualitas Tidur)
  - Interaktif: *hover* untuk melihat nilai tepat
  - Pemilih rentang tanggal
  
- **Catatan Kemajuan dari Terapis:**
  - Tampilan linimasa menampilkan catatan setiap setelah sesi
  - Perluas/ciutkan untuk membaca catatan lengkap
  
- **Pelacakan Tujuan:**
  - Daftar tujuan pribadi yang ditetapkan dengan terapis
  - Bilah kemajuan untuk setiap tujuan
  - Status penyelesaian
  
- **Tonggak Pencapaian:**
  - Lencana pencapaian (mis., "Sesi Pertama", "10 Sesi", "3 Bulan Konsisten")
  - Elemen gamifikasi untuk motivasi
  
- **Unduh Laporan:** Tombol untuk mengunduh laporan kemajuan komprehensif dalam PDF

**26. Pesan/Kotak Masuk Klien (26_client_messages.html)**

*Hub* komunikasi untuk berkomunikasi dengan terapis atau admin:

- **Tata Letak Kotak Masuk:**
  - Bilah samping kiri: Daftar percakapan dengan:
    - Foto dan nama kontak
    - Pratinjau pesan terakhir
    - Stempel waktu
    - Indikator belum dibaca (lencana dengan jumlah)
  
  - Panel kanan: Percakapan yang dipilih:
    - Utas pesan (kronologis)
    - Setiap pesan menampilkan pengirim, stempel waktu, konten
    - Dukungan lampiran (lihat gambar, unduh dokumen)
    
- **Tulis Pesan:**
  - Editor teks kaya
  - Tombol lampiran
  - Tombol "Kirim"
  
- **Penyaringan/Pencarian:**
  - Cari pesan berdasarkan kata kunci
  - Saring berdasarkan pengirim (Terapis, Admin)
  
- **Notifikasi:** Notifikasi waktu nyata untuk pesan baru
- **Arsip:** Opsi untuk mengarsipkan percakapan lama

#### E. Dasbor Terapis (10 halaman)

**27. Dasbor Utama Terapis (27_therapist_dashboard.html)**

Dasbor ikhtisar untuk terapis setelah login:

- ***Header* Sambutan:** "Selamat Datang, Dr. [Nama]"
- ***Widget* Jadwal Hari Ini:**
  - Tampilan linimasa janji temu hari ini
  - Setiap janji temu menampilkan:
    - Waktu
    - Nama klien (dapat diklik → lihat profil klien)
    - Tipe layanan
    - Status (Mendatang, Sedang Berjalan, Selesai)
    - Tindakan cepat: "Mulai Sesi", "Lihat Detail"
  
- **Kartu Statistik Ringkasan:**
  - Sesi Hari Ini (jumlah)
  - Total Klien (sepanjang waktu)
  - Pendapatan Bulan Ini (jumlah Rp)
  - Peringkat Rata-rata (★ 4,8 dari 5)
  
- **Tindakan Cepat:**
  - "Kelola Jadwal Saya"
  - "Lihat Semua Klien"
  - "Periksa Pesan"
  
- **Panel Notifikasi:**
  - Permintaan pemesanan baru (jika alur kerja persetujuan diaktifkan)
  - Permintaan penjadwalan ulang dari klien
  - Konfirmasi pembayaran
  - Pengumuman sistem
  
- **Metrik Kinerja:**
  - Grafik menampilkan sesi dari waktu ke waktu (grafik garis - 30 hari terakhir)
  - Tingkat penyelesaian sesi (%)
  - Tingkat ketidakhadiran (%)
  
- **Janji Temu Mendatang (7 Hari Ke Depan):**
  - Tampilan daftar dengan tanggal, waktu, klien, layanan
  - Tautan "Lihat Jadwal Lengkap"

**28. Manajemen Jadwal Terapis (28_therapist_schedule.html)**

Manajemen kalender untuk terapis:

- **Tampilan Kalender:**
  - *Tab* untuk beralih: Hari, Minggu, Bulan
  - Kisi kalender besar menampilkan semua janji temu
  
- **Tampilan Janji Temu dalam Kalender:**
  - Blok berwarna mewakili janji temu
  - Kode warna berdasarkan tipe layanan atau status
  - Tampilkan waktu, nama klien (dipotong jika panjang)
  - Klik janji temu → modal dengan detail dan tindakan
  
- **Legenda:** Menjelaskan kode warna
- **Tindakan:**
  - Tambah blok manual (untuk *walk-in* atau pemesanan telepon) - hanya admin
  - Lihat/Edit/Batalkan janji temu
  
- **Integrasi:**
  - Tombol "Ekspor ke Google Calendar"
  - "Unduh sebagai PDF" untuk cetak

**29. Pengaturan Ketersediaan Terapis (29_therapist_availability.html)**

Antarmuka untuk mengatur jam kerja dan ketersediaan:

- **Jadwal Reguler:**
  - Kisi mingguan (Senin - Minggu)
  - Untuk setiap hari:
    - Pengalih: Tersedia / Tidak Tersedia
    - Jika tersedia: Slot waktu (waktu mulai - waktu selesai)
    - Tambah beberapa slot waktu per hari (mis., 09:00-12:00 dan 14:00-17:00)
    - Opsi "Salin ke Semua Hari" untuk konsistensi
  
- **Pengaturan Waktu Istirahat:**
  - Durasi istirahat *default* antara sesi (mis., 15 menit)
  - Waktu istirahat makan siang
  
- **Tanggal Diblokir (Cuti/Hari Libur):**
  - *Widget* kalender untuk memilih tanggal
  - Daftar tanggal diblokir dengan opsi hapus
  - Kolom alasan (opsional - untuk pelacakan pribadi)
  
- **Jendela Pemesanan di Muka:**
  - Pengaturan: "Klien dapat memesan hingga X hari di muka"
  - Pengaturan: "Memerlukan minimal X hari pemberitahuan untuk pemesanan"
  
- **Maksimum Sesi per Hari:**
  - Input angka untuk mencegah kelebihan kerja
  
- **Penggantian Ketersediaan:**
  - Opsi untuk sementara mengganti untuk tanggal tertentu (jam khusus)
  
- **Tombol Simpan Perubahan:** Terapkan perubahan, segarkan ketersediaan dalam sistem pemesanan

**30. Daftar Klien Terapis (30_therapist_clients.html)**

Kelola dan lihat daftar semua klien yang pernah ditangani:

- **Tabel Klien:**
  - Kolom:
    - Foto & Nama Klien
    - Tanggal Sesi Terakhir
    - Total Sesi (jumlah)
    - Status (Aktif, Tidak Aktif, Selesai)
    - Indikator Kemajuan (pengukur visual atau persentase)
    - Tindakan (Lihat Profil, Kirim Pesan)
  
- **Pencarian & Penyaringan:**
  - Cari berdasarkan nama atau email
  - Saring berdasarkan status
  - Urutkan berdasarkan nama, sesi terakhir, total sesi
  
- **Halaman Berganda**
- **Klik Baris:** Ke halaman detail profil klien

**31. Tampilan Profil Klien (Sisi Terapis) (31_client_profile_view.html)**

Tampilan detail profil klien dari perspektif terapis:

- **Informasi Klien:**
  - Foto, nama, usia, jenis kelamin, info kontak
  - Tanggal konsultasi awal
  - Total sesi selesai
  - Status saat ini (Aktif/Tidak Aktif)
  
- **Riwayat Sesi dengan Klien:**
  - Tabel daftar semua sesi:
    - Tanggal, Layanan, Durasi, Status
    - Tautan untuk melihat catatan sesi
  
- **Ringkasan Kemajuan:**
  - Grafik menampilkan metrik kemajuan dari waktu ke waktu
  - Tujuan dan pencapaian
  
- **Catatan & Observasi:**
  - Catatan privat hanya terlihat untuk terapis
  - Tombol tambah catatan baru
  - Daftar kronologis catatan sebelumnya
  
- ***Flag*/Tag:**
  - Tandai klien dengan *flag* (mis., "Perlu Tindak Lanjut", "Prioritas Tinggi")
  
- **Tindakan:**
  - Tombol "Kirim Pesan"
  - Tombol "Jadwalkan Sesi" (pintasan untuk memesan dengan klien ini)
  - Tombol "Hasilkan Laporan Kemajuan" (ekspor PDF)

**32. Ruang Sesi (32_session_room.html)**

Ruang virtual untuk melakukan sesi (terutama untuk sesi *online*):

- **Area Konferensi Video:**
  - *Iframe embed* dari Zoom/Google Meet/Whereby
  - Pengalih layar penuh
  - Kontrol Bisukan/Buka Bisukan, Kamera Nyala/Mati
  
- **Panel Informasi Sesi:**
  - Nama klien
  - Tipe layanan
  - Waktu mulai sesi
  - Penghitung waktu menampilkan waktu berlalu
  - Tombol "Akhiri Sesi" (menonjol, merah)
  
- **Akses Cepat:**
  - Tombol untuk melihat profil klien dalam modal (tidak mengganggu)
  - Tombol untuk melihat catatan sesi sebelumnya dalam modal
  
- **Panel Pencatatan:**
  - Panel samping atau laci bawah yang dapat diciutkan
  - Editor catatan waktu nyata (simpan otomatis setiap menit)
  - Penyisipan templat cepat (untuk observasi umum)
  
- **Peringatan Penghitung Waktu Sesi:**
  - Pemberitahuan peringatan 5 menit sebelum waktu akhir terjadwal
  
- **Pasca-Sesi:**
  - Mengklik "Akhiri Sesi" → ajakan untuk menyimpan catatan dan menandai sesi selesai
  - Arahkan ke halaman catatan sesi untuk menyelesaikan dokumentasi

**33. Editor Catatan Sesi (33_session_notes.html)**

Editor terstruktur untuk mendokumentasikan sesi:

- ***Header* Sesi:**
  - Nama klien
  - Tanggal dan waktu
  - Tipe layanan
  
- **Kolom Templat Catatan:** (dapat disesuaikan berdasarkan tipe layanan)
  - **Kondisi Klien:** *Dropdown* atau radio (Tenang, Cemas, Tertekan, dll.) + *textarea* untuk detail
  - **Masalah yang Dibahas:** *Textarea*
  - **Teknik yang Digunakan:** Kotak centang (mis., Relaksasi Progresif, Visualisasi, Restrukturisasi Kognitif) + *textarea*
  - **Respons Klien:** *Textarea*
  - **Penilaian Kemajuan:** Skala peringkat (1-10) + komentar
  - **Tujuan untuk Sesi Berikutnya:** *Textarea*
  - **Observasi Terapis:** *Textarea* (privat)
  - **Rekomendasi:** *Textarea* (dapat dibagikan dengan klien)
  
- **Lampiran:**
  - Unggah file atau gambar jika diperlukan
  
- **Opsi Simpan:**
  - "Simpan Draf" (belum diselesaikan)
  - "Simpan & Selesaikan" (tandai sesi selesai)
  
- **Opsi Berbagi:**
  - Pengalih: "Bagikan observasi dengan klien" (kontrol visibilitas)
  
- **Pemformatan Teks Kaya:** Tebal, miring, daftar poin, dll.
- **Simpan Otomatis:** Draf disimpan otomatis setiap 2 menit
- **Navigasi:** Tautan "Kembali ke Riwayat Sesi"

**34. Riwayat Sesi Terapis (34_therapist_session_history.html)**

Arsip semua sesi yang dilakukan:

- **Penyaringan:**
  - Rentang tanggal
  - Klien (*dropdown*)
  - Tipe layanan (*dropdown*)
  - Status (Selesai, Tidak Hadir, Dibatalkan)
  
- **Tabel Sesi:**
  - Kolom:
    - Tanggal & Waktu
    - Nama Klien
    - Tipe Layanan
    - Durasi
    - Status
    - Tindakan (Lihat Catatan, Edit Catatan)
  
- **Pencarian:** Berdasarkan nama klien atau ID sesi
- **Ekspor:** Unduh hasil penyaringan sebagai CSV atau laporan PDF
- **Halaman Berganda**
- **Statistik Ringkasan:** Total sesi dalam tampilan penyaringan, total jam

**35. Dasbor Pendapatan Terapis (35_therapist_earnings.html)**

Pelacakan keuangan untuk terapis:

- **Kartu Ringkasan Pendapatan:**
  - Pendapatan Hari Ini
  - Pendapatan Minggu Ini
  - Pendapatan Bulan Ini
  - Total Pendapatan (sepanjang waktu)
  
- **Grafik Pendapatan:**
  - Grafik garis atau batang menampilkan pendapatan dari waktu ke waktu
  - Opsi granularitas: Harian, Mingguan, Bulanan, Tahunan
  - Pemilih rentang tanggal
  
- **Rincian per Layanan:**
  - Grafik pai atau donat
  - Menampilkan kontribusi pendapatan dari setiap tipe layanan
  - Tabel dengan nama layanan, jumlah sesi, total pendapatan
  
- **Rincian per Bulan:**
  - Tabel menampilkan pendapatan setiap bulan, sesi, rata-rata per sesi
  
- **Pembayaran Tertunda:**
  - Daftar sesi yang belum dibayar (jika berlaku)
  - Tindakan tindak lanjut
  
- **Tampilan Struktur Komisi:**
  - Jika berlaku, tampilkan tingkat komisi atau skema pembayaran
  
- **Unduh Laporan:**
  - Hasilkan laporan PDF atau Excel untuk akuntansi atau tujuan pajak
  - Pemilih rentang tanggal kustom
  
- **Riwayat Pembayaran:**
  - Tautan ke riwayat transaksi detail (jika dibayar oleh CUR-HEART)

**36. Pengaturan Profil Terapis (36_therapist_profile_edit.html)**

Edit informasi profil sendiri:

- **Foto Profil:**
  - Tampilan foto saat ini
  - Tombol unggah foto baru (dengan fungsi potong)
  
- **Informasi Pribadi:**
  - Nama Lengkap
  - Email
  - Nomor Telepon
  - Tanggal Lahir
  
- **Informasi Profesional:**
  - Gelar/Kredensial (mis., M.Psi., C.Ht.)
  - Tahun Pengalaman
  - Spesialisasi (*tag* multi-pilih)
  - Bio/Tentang (*textarea* kaya)
  
- **Pendidikan:**
  - Tambah/Edit/Hapus entri pendidikan
  - Kolom: Institusi, Gelar, Bidang Studi, Tahun
  
- **Sertifikasi:**
  - Tambah/Edit/Hapus entri sertifikasi
  - Kolom: Nama Sertifikasi, Organisasi Penerbit, Tahun, Kedaluwarsa (jika berlaku)
  - Unggah gambar sertifikat
  
- **Layanan yang Ditawarkan:**
  - Kotak centang untuk memilih layanan mana yang dapat disediakan terapis
  
- **Pengaturan Privasi:**
  - Pengalih visibilitas profil publik
  - Pengalih tampilkan email/telepon ke klien
  
- **Pengaturan Akun:**
  - Ubah kata sandi
  - Preferensi notifikasi (email, SMS)
  
- **Tombol "Simpan Perubahan"**
- **Tombol "Batal"** (buang perubahan)

#### F. Dasbor Admin (5 halaman)

**37. Dasbor Utama Admin (37_admin_dashboard.html)**

Pusat komando sentral untuk admin/pemilik:

- **Indikator Kinerja Utama (KPI):**
  - Pendapatan Hari Ini (jumlah Rp)
  - Total Pengguna (jumlah dengan rincian: X klien, Y terapis)
  - Pemesanan Aktif (jumlah pemesanan terbuka saat ini)
  - Masalah Tertunda (persetujuan, verifikasi, jumlah keluhan)
  
- ***Feed* Aktivitas Waktu Nyata:**
  - Pendaftaran baru
  - Pemesanan baru
  - Pembayaran diterima
  - Sesi selesai
  - Stempel waktu dan nama pengguna
  
- **Grafik Pendapatan:**
  - Grafik garis menampilkan pendapatan harian selama 30 hari terakhir
  - Perbandingan dengan periode sebelumnya (perubahan persentase)
  
- **Ikhtisar Pemesanan:**
  - Grafik batang menampilkan pemesanan berdasarkan status (Mendatang, Selesai, Dibatalkan)
  - Perbandingan bulanan
  
- **Popularitas Layanan:**
  - Grafik batang horizontal menampilkan jumlah pemesanan per layanan
  - Membantu mengidentifikasi layanan paling/paling tidak populer
  
- **Kinerja Terapis:**
  - Tabel daftar terapis dengan:
    - Nama
    - Total Sesi Bulan Ini
    - Pendapatan Dihasilkan
    - Peringkat Rata-rata
  - Opsi pengurutan
  
- **Kesehatan Sistem:**
  - Status server (*Online*/*Offline*)
  - Ukuran basis data
  - Stempel waktu cadangan terakhir
  - Peringatan atau pemberitahuan (mis., ruang disk rendah, pekerjaan *cron* gagal)
  
- **Tindakan Cepat:**
  - "Tambah Pengguna Baru"
  - "Buat Pemesanan Manual"
  - "Hasilkan Laporan"
  - "Pengaturan Sistem"

**38. Manajemen Pengguna Admin (38_admin_users.html)**

Operasi CRUD untuk semua pengguna:

- **Tabel Pengguna:**
  - Kolom:
    - ID
    - Foto & Nama
    - Email
    - Peran (Admin, Terapis, Klien)
    - Status (Aktif, Tidak Aktif, Ditangguhkan)
    - Tanggal Pendaftaran
    - Login Terakhir
    - Tindakan (Lihat, Edit, Hapus/Tangguhkan)
  
- **Penyaringan:**
  - Berdasarkan Peran
  - Berdasarkan Status
  - Berdasarkan Rentang Tanggal Pendaftaran
  
- **Pencarian:** Berdasarkan nama, email, atau ID
- **Pengurutan:** Berdasarkan kolom apa pun
- **Tindakan Massal:**
  - Pilih beberapa pengguna
  - Aktifkan/nonaktifkan massal
  - Email massal
  
- **Tombol Tambah Pengguna Baru:**
  - Buka modal atau navigasi ke formulir
  - Kolom: Nama, Email, Telepon, Peran, Kata Sandi (opsi *auto-generate*)
  - Kotak centang kirim email sambutan
  
- **Edit Pengguna:**
  - Modal atau halaman terpisah
  - Edit semua detail pengguna
  - Ubah peran
  - Atur ulang kata sandi
  - Tangguhkan/aktifkan akun
  
- **Hapus Pengguna:**
  - Modal konfirmasi dengan peringatan
  - Hapus lunak (tandai sebagai dihapus tetapi simpan data) vs. hapus keras
  
- **Ekspor Pengguna:**
  - Unduh daftar pengguna sebagai CSV atau Excel

**Sub-Manajemen Terapis:**

- **Persetujuan Tertunda:**
  - Daftar pendaftaran terapis baru menunggu persetujuan
  - Lihat dokumen yang dikirimkan (kredensial, sertifikat)
  - Tindakan: Setujui, Tolak (dengan alasan), Minta Info Lebih
  
- **Verifikasi Dokumen:**
  - Penampil gambar untuk sertifikat yang diunggah
  - *Checklist* validasi
  - Alur kerja persetujuan
  
- **Tetapkan Layanan:**
  - Layanan mana yang disetujui terapis untuk disediakan
  
- **Tetapkan Komisi:**
  - Tingkat komisi atau biaya tetap per sesi
  - Tingkat berbeda untuk layanan berbeda

**39. Manajemen Pemesanan Admin (39_admin_bookings.html)**

Kelola semua pemesanan di seluruh sistem:

- **Tabel Pemesanan:**
  - Kolom:
    - ID Pemesanan
    - Tanggal & Waktu
    - Nama Klien
    - Nama Terapis
    - Layanan
    - Status (Tertunda, Dikonfirmasi, Selesai, Dibatalkan)
    - Status Pembayaran (Dibayar, Tertunda, Dikembalikan)
    - Tindakan (Lihat, Edit, Batalkan, Jadwalkan Ulang)
  
- **Penyaringan:**
  - Berdasarkan Status
  - Berdasarkan Status Pembayaran
  - Berdasarkan Rentang Tanggal
  - Berdasarkan Terapis
  - Berdasarkan Layanan
  
- **Pencarian:** Berdasarkan ID pemesanan, nama klien, atau nama terapis
- **Pengalih Tampilan Kalender:** Beralih ke tampilan kalender menampilkan semua pemesanan
- **Deteksi Konflik:** Sorot pemesanan ganda atau konflik penjadwalan (*flag* merah)
- **Buat Pemesanan Manual:**
  - Tombol untuk membuat pemesanan atas nama klien (*walk-in* atau pemesanan telepon)
  - Panduan mirip dengan alur pemesanan klien
  - Opsi untuk menandai sebagai dibayar segera
  
- **Edit Pemesanan:**
  - Ubah tanggal/waktu
  - Ubah terapis
  - Perbarui status
  - Tambah catatan admin
  
- **Batalkan Pemesanan:**
  - *Dropdown* alasan
  - Pemrosesan pengembalian dana (jika berlaku)
  - Notifikasi otomatis ke klien dan terapis
  
- **Tindakan Massal:**
  - Ekspor data pemesanan
  - Batalkan massal (mis., jika terapis tidak tersedia untuk sepanjang hari)
  
- **Panel Statistik:**
  - Total pemesanan periode dipilih
  - Tingkat konversi (pertanyaan ke pemesanan dikonfirmasi)
  - Tingkat pembatalan
  - Tingkat ketidakhadiran

**40. Laporan Keuangan Admin (40_admin_financial.html)**

Pelaporan keuangan dan analitik komprehensif:

- **Dasbor Pendapatan:**
  - **Kartu Total Pendapatan:**
    - Hari Ini
    - Minggu Ini
    - Bulan Ini
    - Tahun Ini
  
  - **Grafik Tren Pendapatan:**
    - Grafik garis selama periode yang dapat disesuaikan
    - Opsi: Harian, Mingguan, Bulanan, Tahunan
    - Bandingkan dengan periode sebelumnya (*overlay* atau sumbu ganda)
  
  - **Pendapatan per Layanan:**
    - Grafik pai atau batang
    - Menampilkan layanan mana yang menghasilkan pendapatan terbanyak
    - Tabel dengan rincian detail: Nama layanan, total pemesanan, total pendapatan, harga rata-rata
  
  - **Pendapatan per Terapis:**
    - Bar chart ranking therapists
    - Tabel: Nama terapis, sesi, pendapatan, komisi dibayar, bersih untuk bisnis
  
- **Pelacakan Pembayaran:**
  - **Ikhtisar Status Pembayaran:**
    - Dibayar (hijau): jumlah & nilai
    - Tertunda (kuning): jumlah & nilai
    - Gagal (merah): jumlah & nilai
    - Dikembalikan (abu-abu): jumlah & nilai
  
  - **Pembayaran Tertunggak:**
    - Daftar tabel pemesanan dengan pembayaran tertunda
    - Hari terlambat
    - Tindakan: Kirim pengingat, tandai sebagai dibayar, batalkan pemesanan
  
  - **Antrean Verifikasi Manual:**
    - Untuk pembayaran transfer bank
    - Unggah gambar bukti pembayaran
    - Verifikasi dan setujui
  
- **Pengembalian Dana:**
  - Daftar permintaan pengembalian dana
  - Alur kerja persetujuan
  - Pemrosesan pengembalian dana
  
- **Pengeluaran (Opsional):**
  - Lacak pengeluaran operasional (sewa, utilitas, pemasaran)
  - Perhitungan laba (Pendapatan - Pengeluaran)
  
- **Laporan Pajak:**
  - Hitung kewajiban pajak
  - Hasilkan laporan siap pajak untuk akuntan
  
- **Prakiraan Keuangan:**
  - Proyeksi pendapatan berdasarkan tren
  - Analisis musiman
  
- **Opsi Ekspor:**
  - Unduh laporan dalam PDF, Excel, CSV
  - Email laporan ke pemangku kepentingan
  - Jadwalkan laporan otomatis (harian/mingguan/bulanan)

**41. Pengaturan Sistem Admin (41_admin_settings.html)**

*Hub* konfigurasi untuk pengaturan di seluruh sistem:

- **Pengaturan Umum:**
  - Nama Situs
  - Unggah Logo Situs
  - *Tagline*/Slogan
  - Informasi Kontak (alamat, telepon, email)
  - Jam Operasional
  - Zona Waktu
  
- **Pengaturan Email:**
  - Konfigurasi SMTP:
    - *Host* SMTP
    - *Port* SMTP
    - Nama Pengguna SMTP
    - Kata Sandi SMTP
    - Enkripsi (TLS/SSL)
  - Tombol Email Uji (kirim email uji untuk memverifikasi konfigurasi)
  - Manajemen Templat Email:
    - Daftar templat (sambutan, konfirmasi pemesanan, pengingat, dll.)
    - Edit konten templat (dukungan variabel: {{nama}}, {{tanggal}}, dll.)
  
- **Pengaturan SMS (Opsional):**
  - Konfigurasi *Gateway* SMS
  - Kunci API
  - ID Pengirim
  - Tombol SMS Uji
  
- **Pengaturan *Payment Gateway*:**
  - Konfigurasi Midtrans/Xendit:
    - Kunci API (*Server Key*, *Client Key*)
    - ID *Merchant*
    - Pengalih Mode Uji/Produksi
  - Tampilan URL *Webhook*
  - Metode Pembayaran Diaktifkan (kotak centang: Kartu Kredit, Dompet Digital, Transfer Bank, QRIS)
  
- **Pengaturan Pemesanan:**
  - Hari Pemesanan di Muka (seberapa jauh di muka klien dapat memesan)
  - Periode Pemberitahuan Minimum (mis., harus memesan minimal 2 hari di muka)
  - Waktu *Buffer* Sesi *Default* (menit antara sesi)
  - Kebijakan Pembatalan:
    - Izinkan pembatalan hingga X jam sebelum sesi
    - Persentase pengembalian dana berdasarkan periode pemberitahuan
  - Konfirmasi otomatis (atau memerlukan persetujuan admin)
  
- **Pengaturan Notifikasi:**
  - Aktifkan/Nonaktifkan Notifikasi Email (pengalih untuk setiap tipe):
    - Email Sambutan
    - Verifikasi Email
    - Konfirmasi Pemesanan
    - Pengingat Pemesanan (H-1)
    - Pengingat Pemesanan (H-0, 1 jam sebelumnya)
    - Notifikasi Penjadwalan Ulang
    - Notifikasi Pembatalan
    - Konfirmasi Pembayaran
    - Permintaan Ulasan
  - Aktifkan/Nonaktifkan Notifikasi SMS
  - Aktifkan/Nonaktifkan Notifikasi *Push* (untuk aplikasi seluler masa depan)
  
- **Pengaturan Keamanan:**
  - Kebijakan Kata Sandi:
    - Panjang Minimum
    - Memerlukan Huruf Besar
    - Memerlukan Angka
    - Memerlukan Karakter Khusus
  - Waktu Tunggu Sesi (menit)
  - Penegakan Autentikasi Dua Faktor (2FA)
  - Batas Percobaan Login
  - *Whitelist*/*Blacklist* IP (opsional, untuk akses admin)
  
- **Pengaturan Cadangan:**
  - Jadwal Cadangan Otomatis (harian, mingguan, bulanan)
  - Lokasi Penyimpanan Cadangan (lokal, Google Drive, Dropbox)
  - Periode Retensi Cadangan (berapa lama menyimpan cadangan)
  - Tombol Cadangan Manual (picu cadangan segera)
  - Pulihkan dari Cadangan (unggah dan pulihkan)
  
- **Mode Pemeliharaan:**
  - Pengalih Mode Pemeliharaan (tampilkan halaman "Dalam Pemeliharaan" ke pengunjung)
  - Pesan Pemeliharaan (teks yang dapat disesuaikan)
  - *Whitelist* IP (admin masih dapat mengakses selama pemeliharaan)
  
- **Analitik:**
  - ID Pelacakan Google Analytics
  - ID Piksel Facebook
  - Aktifkan/Nonaktifkan Pelacakan
  
- **Legal:**
  - Editor Kebijakan Privasi (teks kaya)
  - Editor Syarat & Ketentuan (teks kaya)
  - Editor Kebijakan *Cookie* (teks kaya)
  - Stempel Waktu Pembaruan Terakhir
  
- **Pengaturan Lanjutan (Pengembang):**
  - Mode *Debug* (aktifkan/nonaktifkan tampilan kesalahan)
  - Level *Log* (*error*, *warning*, *info*, *debug*)
  - Pengaturan *Cache* (aktifkan/nonaktifkan, tombol bersihkan *cache*)
  - Pengaturan Antrean
  
- **Tombol "Simpan Perubahan":** Terapkan semua pengaturan (dengan konfirmasi)
- **Tombol "Atur Ulang ke *Default*":** Kembalikan ke pengaturan *default* (dengan peringatan)

---

### 4.3.3 Perancangan Basis Data

Sistem menggunakan basis data relasional (MySQL) dengan skema yang dinormalisasi hingga Bentuk Normal Ketiga (3NF) untuk mengurangi redundansi dan menjaga integritas data.

**Diagram Hubungan Entitas (ERD):**

```
┌─────────────┐
│    users    │
├─────────────┤
│ id (PK)     │
│ name        │
│ email (UQ)  │
│ password    │
│ role        │──────┬──────────────────────────────────┐
│ phone       │      │                                  │
│ status      │      │                                  │
│ created_at  │      │                                  │
│ updated_at  │      │                                  │
└─────────────┘      │                                  │
       │             │                                  │
       │ 1           │                                  │
       │             │                                  │
       │             │ 1                                │ 1
       │      ┌──────▼───────────┐             ┌───────▼────────┐
       │      │   therapists     │             │    clients     │
       │      ├──────────────────┤             ├────────────────┤
       │      │ id (PK)          │             │ id (PK)        │
       │      │ user_id (FK)     │             │ user_id (FK)   │
       │      │ credentials      │             │ date_of_birth  │
       │      │ specializations  │             │ address        │
       │      │ bio              │             │ emergency_cont │
       │      │ years_experience │             │ created_at     │
       │      │ rating           │             │ updated_at     │
       │      │ created_at       │             └────────────────┘
       │      │ updated_at       │                      │
       │      └──────────────────┘                      │
       │             │ 1                                │ 1
       │             │                                  │
       │             │ M                                │ M
       │      ┌──────▼───────────┐             ┌───────▼────────┐
       │      │therapist_services│             │    bookings    │
       │      ├──────────────────┤             ├────────────────┤
       │      │ therapist_id (FK)│             │ id (PK)        │
       │      │ service_id (FK)  │◄─────┐      │ client_id (FK) │
       │      └──────────────────┘      │      │ therapist_id(F)│
       │                                │      │ service_id (FK)│
       │                          ┌─────┴──────────┤ date           │
       │                          │   services     │ time_slot      │
       │                          ├────────────────┤ status         │
       │                          │ id (PK)        │ notes          │
       │                          │ name           │ created_at     │
       │                          │ description    │ updated_at     │
       │                          │ duration       │ deleted_at     │
       │                          │ price          │ (soft deletes) │
       │                          │ category       │ └────────────────┘
       │                          │ status         │        │ 1
       │                          │ created_at     │        │
       │                          │ updated_at     │        │ M
       │                          └────────────────┘  ┌─────▼──────────┐
       │                                             │   payments     │
       │                                             ├────────────────┤
       │                                             │ id (PK)        │
       │                                             │ booking_id (FK)│
       │                                             │ amount         │
       │                                             │ method         │
       │                                             │ status         │
       │                                             │ transaction_id │
       │                                             │ paid_at        │
       │                                             │ created_at     │
       │                                             │ updated_at     │
       │                                             └────────────────┘
       │
       │ 1                                          bookings
       │                                                │ 1
       │                                                │
       │ M                                              │ 1
┌──────▼───────────┐                             ┌─────▼──────────┐
│therapist_avail   │                             │    sessions    │
├──────────────────┤                             ├────────────────┤
│ id (PK)          │                             │ id (PK)        │
│ therapist_id (FK)│                             │ booking_id (FK)│
│ day_of_week      │                             │ started_at     │
│ start_time       │                             │ ended_at       │
│ end_time         │                             │ status         │
│ is_available     │                             │ notes          │
│ created_at       │                             │ created_at     │
│ updated_at       │                             │ updated_at     │
└──────────────────┘                             └────────────────┘
                                                         │ 1
┌──────────────────┐                                    │
│therapist_blocked │                                    │ M
├──────────────────┤                             ┌──────▼─────────┐
│ id (PK)          │                             │ session_notes  │
│ therapist_id (FK)│                             ├────────────────┤
│ date             │                             │ id (PK)        │
│ reason           │                             │ session_id (FK)│
│ created_at       │                             │ condition      │
│ updated_at       │                             │ discussion     │
└──────────────────┘                             │ techniques     │
                                                 │ response       │
              bookings                           │ progress       │
                 │ 1                             │ goals          │
                 │                               │ observations   │
                 │ M                             │ recommendations│
          ┌──────▼───────────┐                  │ is_shared      │
          │     reviews      │                  │ created_at     │
          ├──────────────────┤                  │ updated_at     │
          │ id (PK)          │                  └────────────────┘
          │ booking_id (FK)  │
          │ rating           │          clients
          │ comment          │             │ 1
          │ created_at       │             │
          │ updated_at       │             │ M
          └──────────────────┘      ┌──────▼─────────┐
                                    │client_progress │
              clients               ├────────────────┤
                 │ 1                │ id (PK)        │
                 │                  │ client_id (FK) │
                 │ M                │ date           │
          ┌──────▼───────────┐     │ anxiety_level  │
          │    messages      │     │ confidence     │
          ├──────────────────┤     │ sleep_quality  │
          │ id (PK)          │     │ overall_score  │
          │ sender_id (FK)   │     │ notes          │
          │ receiver_id (FK) │     │ created_at     │
          │ content          │     │ updated_at     │
          │ is_read          │     └────────────────┘
          │ created_at       │
          │ updated_at       │
          └──────────────────┘
```

**Tabel-tabel Utama:**

1. **users** - Central table untuk semua users (admin, therapists, clients)
2. **therapists** - Extended profile untuk users dengan role therapist
3. **clients** - Extended profile untuk users dengan role client
4. **services** - Katalog layanan terapi
5. **bookings** - Records booking/appointments
6. **sessions** - Actual sessions yang conducted
7. **session_notes** - Dokumentasi detailed setiap session
8. **payments** - Transaction records
9. **reviews** - Client reviews untuk therapists
10. **therapist_services** - Many-to-many relationship antara therapists dan services
11. **therapist_availability** - Regular weekly schedule therapists
12. **therapist_blocked_dates** - Specific dates therapists unavailable
13. **client_progress** - Progress tracking metrics
14. **messages** - Communication between users

**Sample Table Definitions (MySQL):**

```sql
-- Users Table
CREATE TABLE users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'therapist', 'client') NOT NULL DEFAULT 'client',
    phone VARCHAR(20),
    status ENUM('active', 'inactive', 'suspended') NOT NULL DEFAULT 'active',
    email_verified_at TIMESTAMP NULL,
    remember_token VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,
    INDEX idx_email (email),
    INDEX idx_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Therapists Table
CREATE TABLE therapists (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    credentials VARCHAR(255),
    specializations TEXT,
    bio TEXT,
    years_experience INT UNSIGNED,
    rating DECIMAL(3,2) DEFAULT 0.00,
    total_reviews INT UNSIGNED DEFAULT 0,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_rating (rating)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Services Table
CREATE TABLE services (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    duration INT UNSIGNED NOT NULL COMMENT 'Duration in minutes',
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(100),
    status ENUM('active', 'inactive') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_slug (slug),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bookings Table
CREATE TABLE bookings (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    booking_number VARCHAR(50) UNIQUE NOT NULL,
    client_id BIGINT UNSIGNED NOT NULL,
    therapist_id BIGINT UNSIGNED NOT NULL,
    service_id BIGINT UNSIGNED NOT NULL,
    booking_date DATE NOT NULL,
    time_slot TIME NOT NULL,
    status ENUM('pending', 'confirmed', 'completed', 'cancelled', 'no_show') DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,
    FOREIGN KEY (client_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE,
    INDEX idx_booking_number (booking_number),
    INDEX idx_client_id (client_id),
    INDEX idx_therapist_id (therapist_id),
    INDEX idx_booking_date (booking_date),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Payments Table
CREATE TABLE payments (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    booking_id BIGINT UNSIGNED NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    method ENUM('credit_card', 'bank_transfer', 'ewallet', 'qris') NOT NULL,
    status ENUM('pending', 'processing', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    transaction_id VARCHAR(255),
    payment_gateway VARCHAR(50),
    paid_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE,
    INDEX idx_booking_id (booking_id),
    INDEX idx_status (status),
    INDEX idx_transaction_id (transaction_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

Ini sudah bagian yang sangat panjang dan detail untuk BAB IV. File sudah mencapai lebih dari 670 baris. Saya perlu melanjutkan dengan bagian 4.4, 4.5, 4.6, dan 4.7 di file yang sama atau terpisah.

Apakah Anda ingin saya:
1. Lanjutkan di file yang sama (akan menjadi sangat panjang)?
2. Buat file terpisah untuk bagian sisanya?
3. Atau review dulu yang sudah ada?
