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

**[GAMBAR 4.1 - Struktur Organisasi CUR-HEART]**

_Diagram hierarki organisasi menunjukkan Pemilik/Pendiri (Dr. Sarah W.) di puncak, dengan tiga divisi utama: Kepala Terapis (Michael A.) yang membawahi 5 Terapis, Manajer Operasional yang membawahi 2 Layanan Pelanggan, dan divisi Keuangan & Admin dengan 1 Staf Keuangan. Total: 10 anggota tim._

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

**[GAMBAR 4.2 - Proses Bisnis Saat Ini (As-Is)]**

_Diagram swimlane menunjukkan proses pemesanan manual: Klien menghubungi Admin via WhatsApp/telepon → Admin cek jadwal manual dengan Terapis → Konfirmasi slot → Klien transfer pembayaran → Verifikasi manual (jam/hari) → Sesi terapi → Terapis tulis catatan manual (15 menit) → Admin update Excel. Titik masalah: 15-20 menit/pemesanan, 8-10 pemesanan ganda/bulan, verifikasi lambat, 40% kehilangan konversi. Total waktu: ~45 menit per pemesanan, tingkat error: 8-10%._

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

| No | Pemangku Kepentingan | Peran Utama | Kategori | Tingkat Kepentingan & Pengaruh | Strategi Keterlibatan |
|----|---------------------|-------------|----------|-------------------------------|----------------------|
| 1 | Pemilik CUR-HEART | Pengambil Keputusan, Sponsor | Primer | Sangat Tinggi (Power & Interest) | Kelola Erat - Update mingguan, persetujuan tonggak |
| 2 | Terapis (5 orang) | Pengguna Utama | Primer | Sangat Tinggi (Interest), Tinggi (Power) | Kelola Erat - Lokakarya kebutuhan, UAT |
| 3 | Staf Admin (2 orang) | Operator Sistem | Primer | Tinggi (Power & Interest) | Kelola Erat - Pemetaan proses, pelatihan |
| 4 | Klien Aktif | Pengguna Akhir | Primer | Tinggi (Interest), Sedang (Power) | Tetap Informasi - Riset pengguna, survei umpan balik |
| 5 | Dosen Pembimbing | Pembimbing Akademik | Sekunder | Tinggi (Power & Interest) | Jaga Kepuasan - Konsultasi mingguan, tinjauan |
| 6 | Tim Pengembang (3 orang) | Tim Proyek | Internal | Sangat Tinggi (Power & Interest) | Kelola Erat - Standup harian, kolaborasi |
| 7 | Universitas Nusa Mandiri | Institusi Akademik | Sekunder | Sedang (Power & Interest) | Tetap Informasi - Laporan kemajuan, presentasi |

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

_Matriks 2x2 (Power vs Interest) menunjukkan positioning 11 stakeholder groups: **Manage Closely** (7 stakeholders) - Owner, Terapis (5), Tim Dev (3) dengan high power & interest, memerlukan komunikasi harian/mingguan; **Keep Satisfied** (1) - Dosen Pembimbing dengan high power tapi medium interest; **Keep Informed** (3) - Admin (2), Klien, Universitas dengan high interest tapi lower power; **Monitor** (0) - tidak ada stakeholder di quadrant ini. Total: 11 groups, 23 individuals._

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

_Diagram pohon hierarki 3-level menunjukkan 7 fase proyek: 1.1 Manajemen Proyek (77 hari - 4 sub-task), 1.2 Analisis Kebutuhan (11 hari - 4 sub-task), 1.3 Perancangan Sistem (14 hari - 4 sub-task), 1.4 Pengembangan (28 hari - 5 sub-task), 1.5 Pengujian (14 hari - 5 sub-task), 1.6 Peluncuran (7 hari - 4 sub-task), 1.7 Dokumentasi (21 hari paralel - 4 sub-task). Total: 7 fase level-2, 36 paket kerja level-3, durasi 77 hari kerja (11 minggu), tim 3 pengembang._

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

| No | Fase Utama | Tugas Utama | Periode | Status | Tonggak (*Milestone*) |
|----|------------|-------------|---------|--------|---------------------|
| 1 | **Inisiasi** (3 hari) | Kick-off proyek, piagam, identifikasi pemangku kepentingan | 16-Sep - 18-Sep | Selesai | M1: Proyek Disetujui |
| 2 | **Kebutuhan** (11 hari) | Wawancara, analisis proses bisnis, dokumentasi kebutuhan, validasi | 19-Sep - 29-Sep | Selesai | M2: Kebutuhan Selesai |
| 3 | **Desain** (14 hari) | Desain arsitektur, basis data, UI/UX, keamanan | 30-Sep - 13-Oct | Selesai | M3: Desain Selesai |
| 4 | **Pengembangan** (28 hari) | Setup lingkungan, implementasi basis data, autentikasi, backend, frontend, integrasi, code review | 14-Oct - 10-Nov | Sedang Berjalan | M4: Pengembangan Selesai |
| 5 | **Pengujian** (14 hari) | Unit testing, integrasi, fungsional, kegunaan (SUS), UAT | 11-Nov - 24-Nov | Akan Datang | M5: Pengujian Selesai |
| 6 | **Peluncuran** (7 hari) | Setup produksi, go-live, pelatihan pengguna | 25-Nov - 1-Dec | Akan Datang | M6: Sistem Aktif |
| 7 | **Dokumentasi** (21 hari) | Dokumentasi teknis, user manual, laporan capstone, persiapan presentasi | 11-Nov - 1-Dec | Sedang Berjalan | M7: Proyek Selesai |

**Total Durasi:** 77 hari kerja (11 minggu)  
**Jalur Kritis (*Critical Path*):** Inisiasi → Kebutuhan → Desain → Pengembangan → Integrasi → Pengujian → UAT → Peluncuran  
**Kemajuan Saat Ini:** 45% selesai (Fase 1-3 selesai, Fase 4 sedang berjalan)

---

**[GAMBAR 4.5 - Diagram Gantt Jadwal Proyek (77 Hari Kerja)]**

_Diagram Gantt 11 minggu timeline (16 Sep - 1 Des 2024) menunjukkan 7 fase dengan milestone: 1) Inisiasi (3 hari) → M1 Proyek Disetujui, 2) Kebutuhan (11 hari) → M2 SRS Selesai, 3) Desain (14 hari) → M3 Desain Selesai, 4) Pengembangan (28 hari) → M4 Kode Selesai, 5) Pengujian (14 hari) → M5 UAT Lulus, 6) Peluncuran (7 hari) → M6 Go-Live, 7) Dokumentasi (21 hari paralel) → M7 Selesai. Jalur kritis disorot dari Inisiasi hingga Peluncuran._

---

### 4.2.3 Manajemen Biaya Proyek

**Tabel 4.6 Rincian Anggaran (Total Rp 5.000.000)**

| No | Kategori & Item | Deskripsi | Total (Rp) | % Anggaran | Prioritas |
|----|----------------|-----------|------------|-------------|-----------|
| 1 | **Infrastruktur** | Total Infrastruktur | **1.500.000** | 30% | Kritis |
| | - Domain (.com, 1 tahun) | 1 unit @ Rp 150.000 | 150.000 | 3% | Harus Ada |
| | - Hosting VPS (3 bulan) | 3 bulan @ Rp 300.000/bulan | 900.000 | 18% | Harus Ada |
| | - Sertifikat SSL | Let's Encrypt (gratis) | 0 | 0% | Harus Ada |
| | - Penyimpanan Cadangan | Google Drive 1 unit | 150.000 | 3% | Sebaiknya Ada |
| | - Layanan CDN | Cloudflare Pro 1 unit | 300.000 | 6% | Bisa Ada |
| 2 | **Alat Pengembangan** | Total Alat Pengembangan | **800.000** | 16% | Tinggi |
| | - Editor Kode | VS Code (gratis) | 0 | 0% | Gratis |
| | - Alat Desain | Figma Pro 1 bulan | 200.000 | 4% | Harus Ada |
| | - Database Tools | MySQL Workbench (gratis) | 0 | 0% | Gratis |
| | - Version Control | GitHub (gratis) | 0 | 0% | Gratis |
| | - Project Management | Asana 1 unit | 100.000 | 2% | Sebaiknya Ada |
| | - Testing Tools | Berbagai alat pengujian | 500.000 | 10% | Harus Ada |
| 3 | **Layanan Pihak Ketiga** | Total Layanan Eksternal | **1.200.000** | 24% | Tinggi |
| | - Payment Gateway | Midtrans (setup gratis) | 0 | 0% | Gratis |
| | - Kredit Uji Pembayaran | Testing payment system | 500.000 | 10% | Harus Ada |
| | - Layanan Email | SendGrid 1 unit | 200.000 | 4% | Harus Ada |
| | - Layanan SMS | Twilio 1 unit | 300.000 | 6% | Bisa Ada |
| | - Monitoring | Sentry 1 unit | 200.000 | 4% | Sebaiknya Ada |
| 4 | **Dokumentasi** | Total Dokumentasi & Print | **500.000** | 10% | Sedang |
| | - Pencetakan Laporan | Full color 1 set | 300.000 | 6% | Harus Ada |
| | - Pencetakan X-Banner | 60x160 cm 1 unit | 200.000 | 4% | Harus Ada |
| 5 | **Cadangan Kontinjensi** | Buffer biaya tak terduga | **1.000.000** | 20% | Kritis |
|  | **TOTAL ANGGARAN** | **Keseluruhan Proyek** | **5.000.000** | **100%** | - |

---

**[GAMBAR 4.6 - Rincian Alokasi Anggaran (Rp 5.000.000)]**

_Diagram pie chart dan bar chart combo menunjukkan alokasi: Infrastruktur 30% (Rp 1.5M - hosting, domain), Layanan Pihak Ketiga 24% (Rp 1.2M - payment gateway, email, SMS), Kontinjensi 20% (Rp 1M buffer), Alat Pengembangan 16% (Rp 800K - Figma, testing tools), Dokumentasi 10% (Rp 500K - print laporan, banner). Alat gratis: VS Code, MySQL, GitHub (Rp 0)._

---

**Indeks Kinerja Biaya (*Cost Performance Index* - CPI):**

| No | Periode | Nilai Terencana (PV) | Biaya Aktual (AC) | Varian Biaya (CV) | CPI & Status |
|----|---------|---------------------|-------------------|-------------------|--------------|
| 1 | Bulan 1 (Sep) | Rp 1.500.000 | Rp 1.450.000 | +Rp 95.000 | 1.07 - Di bawah anggaran |
| 2 | Bulan 2 (Okt) | Rp 2.000.000 | Rp 1.980.000 | +Rp 40.000 | 1.02 - Sesuai rencana |
| 3 | Bulan 3 (Nov) | Rp 1.500.000 | (sedang berjalan) | TBD | TBD - Sedang berjalan |
|  | **Total s.d. Kini** | **Rp 3.500.000** | **Rp 3.430.000** | **+Rp 135.000** | **1.04 - Di bawah anggaran** |

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

| No | Nama Sumber Daya | Peran Utama & Sekunder | Keahlian Utama | Alokasi & Fase | Jam Mingguan |
|----|-----------------|----------------------|---------------|---------------|-------------|
|  | **Tim Internal (Inti)** | | | | |
| 1 | Roki Anjas | Manajer Proyek, Backend Developer | Kepemimpinan, Laravel, PHP, MySQL, API | 100% - Semua fase | 40 jam |
| 2 | Susanto | Frontend Developer, UI/UX Designer | Tailwind CSS, Blade, Figma, Riset UX | 100% - Desain-Peluncuran | 40 jam |
| 3 | Fahruroji | Full-Stack Developer, DBA | Laravel, MySQL, Pengujian, Dokumentasi | 100% - Desain-Peluncuran | 40 jam |
|  | **Pemangku Kepentingan Eksternal** | | | | |
| 4 | Rani Irma Handayani, M.Kom | Pembimbing Akademik, Penasihat Teknis | Analisis sistem, manajemen proyek | Paruh waktu - Semua fase | 2 jam |
| 5 | Pemilik CUR-HEART | Sponsor Proyek, Pengambil Keputusan | Strategi bisnis, persetujuan anggaran | Sesuai kebutuhan - Inisiasi, UAT | 1 jam |
| 6 | Terapis (5 orang) | Subject Matter Expert, End User | Hipnoterapi, pengetahuan alur kerja | Sesuai kebutuhan - Kebutuhan, UAT | 2 jam/orang |
| 7 | Staf Admin (2 orang) | Operator Sistem, Tester | Proses admin, entri data | Sesuai kebutuhan - Kebutuhan, UAT | 3 jam/orang |
| 8 | Klien Sampel (10 orang) | End User, Tester | Perspektif pengguna, umpan balik | Sesuai kebutuhan - Pengujian | 1 jam/orang |
|  | **Sumber Daya Spesialis** | | | | |
| 9 | Mentor Teknis | Code Reviewer | Pengembang Laravel senior | Ad-hoc - Pengembangan | 1 jam/minggu |
| 10 | Konsultan Keamanan | Security Auditor | Keamanan web, OWASP | Ad-hoc - Pengujian | 2 jam total |

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

| ID | Peristiwa Risiko & Kategori | Prob × Dampak | Prioritas | Strategi Mitigasi Utama | Status & Pemilik |
|----|---------------------------|---------------|-----------|------------------------|-----------------|
| R01 | Perluasan ruang lingkup (Ruang Lingkup) | 50% × 8 = 4.0 | Kritis | Kontrol perubahan ketat, prioritas MoSCoW, dokumentasi baseline. Kontinjensi: Tunda fitur ke Fase 2 | Aktif - PM |
| R02 | Kompleksitas teknis tinggi (Teknis) | 40% × 6 = 2.4 | Tinggi | Prototyping awal, tinjauan reguler, solusi spike. Kontinjensi: Bantuan mentor, perpanjang jadwal | Aktif - Tech Lead |
| R03 | Ketidaktersediaan tim (Sumber Daya) | 20% × 8 = 1.6 | Tinggi | Pelatihan silang, pair programming, dokumentasi. Kontinjensi: Distribusi ulang pekerjaan | Dipantau - PM |
| R04 | Stakeholder tidak tersedia (Stakeholder) | 30% × 5 = 1.5 | Sedang | Penjadwalan fleksibel, komunikasi asinkron. Kontinjensi: Demo rekaman, persetujuan email | Dipantau - PM |
| R05 | Masalah integrasi payment (Integrasi) | 40% × 6 = 2.4 | Tinggi | Testing integrasi awal, sandbox, backup provider. Kontinjensi: Verifikasi manual sementara | Aktif - Backend Dev |
| R06 | Masalah kinerja produksi (Kinerja) | 30% × 7 = 2.1 | Tinggi | Load testing, optimasi query, caching Redis, CDN. Kontinjensi: Upgrade hosting, optimize critical queries | Dipantau - DevOps |
| R07 | Pelanggaran keamanan (Keamanan) | 10% × 10 = 1.0 | Kritis | OWASP best practices, audit, penetration testing. Kontinjensi: Patch segera, incident response | Dipantau - Security Lead |
| R08 | Keterlambatan jadwal (Jadwal) | 40% × 7 = 2.8 | Kritis | Monitoring mingguan, buffer 20%, standup harian. Kontinjensi: Kurangi scope, perpanjangan jadwal | Aktif - PM |
| R09 | Pembengkakan anggaran (Biaya) | 20% × 5 = 1.0 | Sedang | Tracking bulanan, approval process, alternatif gratis. Kontinjensi: Gunakan dana kontinjensi Rp 1M | Dipantau - PM |
| R10 | Adopsi pengguna rendah (Bisnis) | 30% × 8 = 2.4 | Tinggi | User-centered design, training, change management. Kontinjensi: Training tambahan, insentif adopsi | Aktif - PM |
| R11 | Downtime layanan 3rd party (Eksternal) | 25% × 6 = 1.5 | Sedang | Provider andal (SLA 99.9%), retry logic. Kontinjensi: Backup provider, manual fallback | Dipantau - DevOps |
| R12 | Perubahan kebutuhan (Kebutuhan) | 35% × 6 = 2.1 | Tinggi | Validasi stakeholder, change control board. Kontinjensi: Nilai dampak, prioritaskan ulang backlog | Aktif - PM |

**Perhitungan Skor Risiko:** Probabilitas (%) × Dampak (1-10)  
**Tingkat Prioritas:** Kritis (>3.5), Tinggi (2.0-3.5), Sedang (1.0-2.0), Rendah (<1.0)


**[GAMBAR 4.7 - Matriks Risiko (Probabilitas vs Dampak dengan 12 Risiko)]**


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

| No | Stakeholder | Informasi Utama | Metode & Frekuensi | Format | Penanggung Jawab |
|----|-------------|----------------|-------------------|--------|-----------------|
| 1 | Pemilik CUR-HEART | Status proyek, anggaran, keputusan kunci, ROI | Email (PDF), Rapat - Mingguan (Senin 9 pagi) | Template laporan status | Manajer Proyek |
| 2 | Dosen Pembimbing | Kemajuan, tantangan teknis, hasil akademik | Tatap muka, Google Meet - Mingguan (Jumat 2 siang) | Dokumen kemajuan, demo kode | Manajer Proyek |
| 3 | Terapis (5 orang) | Demo fitur, jadwal testing, training, perubahan workflow | WhatsApp, Email - Dua mingguan (Selasa sore) | Screenshot, video demo | Manajer Proyek |
| 4 | Staf Admin (2 orang) | Fitur sistem, testing, training, perubahan proses | WhatsApp, Email - Dua mingguan (Selasa sore) | Screenshot, draft user guide | Manajer Proyek |
| 5 | Klien Sampel (10) | Undangan testing, feedback, studi kegunaan | Email, Telepon - Ad-hoc (Minggu 10) | Email undangan, form persetujuan | Perancang UX |
| 6 | Tim Pengembang (3) | Task assignment, progress harian, blockers, code review | Discord/Slack, Standup video - Harian (10 pagi) | Format standup (done/todo/blockers) | Manajer Proyek |
| 7 | Mentor Teknis | Code review, tantangan teknis, keputusan arsitektur | GitHub PR, Email, Zoom - Ad-hoc (mingguan) | Code snippet, diagram arsitektur | Tech Lead |
| 8 | Universitas | Kemajuan bulanan, hasil akhir | Email, Pengiriman fisik - Bulanan & Akhir | Format laporan akademik | Manajer Proyek |

**Prinsip Komunikasi:**
1. Informasi yang tepat kepada orang yang tepat pada waktu yang tepat
2. Pesan yang jelas, ringkas, dan dapat ditindaklanjuti
3. Komunikasi dua arah (umpan balik didorong)
4. Dokumentasi keputusan penting
5. Jalur eskalasi untuk masalah mendesak


**[GAMBAR 4.8 - Matriks Komunikasi Pemangku Kepentingan]**


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
| FR-AUTH-01 | Registrasi pengguna dengan verifikasi email | Harus Ada | Semua | Pengguna dapat registrasi, terima email, verifikasi akun |  Terimplementasi |
| FR-AUTH-02 | Login dengan email dan kata sandi | Harus Ada | Semua | Pengguna dapat login dengan kredensial valid |  Terimplementasi |
| FR-AUTH-03 | Lupa kata sandi dan *reset* via email | Harus Ada | Semua | Pengguna dapat *reset* kata sandi via tautan email |  Terimplementasi |
| FR-AUTH-04 | Kontrol akses berbasis peran (Admin, Terapis, Klien) | Harus Ada | Semua | Setiap peran hanya akses fitur yang sesuai |  Terimplementasi |
| FR-AUTH-05 | Fungsi *logout* | Harus Ada | Semua | Pengguna dapat *logout* dengan aman |  Terimplementasi |
| **FR-BOOKING** | **Manajemen Pemesanan** | | | | |
| FR-BOOK-01 | Telusuri dan filter layanan | Harus Ada | Klien | Klien dapat lihat semua layanan dengan filter |  Terimplementasi |
| FR-BOOK-02 | Lihat profil terapis dan ketersediaan | Harus Ada | Klien | Klien dapat lihat profil dan jadwal terapis |  Terimplementasi |
| FR-BOOK-03 | Alur pemesanan 4 langkah (Layanan → Terapis → Tanggal/Waktu → Konfirmasi) | Harus Ada | Klien | Klien dapat selesaikan pemesanan dalam 4 langkah |  Sedang Berjalan |
| FR-BOOK-04 | Pengecekan ketersediaan *real-time* | Harus Ada | Klien | Sistem cegah pemesanan ganda |  Sedang Berjalan |
| FR-BOOK-05 | Email konfirmasi pemesanan | Harus Ada | Klien | Klien terima email setelah pemesanan | 🔜 Direncanakan |
| FR-BOOK-06 | Jadwal ulang pemesanan (min 24 jam sebelum) | Sebaiknya Ada | Klien | Klien dapat jadwal ulang dengan batasan | 🔜 Direncanakan |
| FR-BOOK-07 | Batalkan pemesanan dengan alasan | Sebaiknya Ada | Klien | Klien dapat batalkan pemesanan | 🔜 Direncanakan |
| **FR-SCHEDULE** | **Manajemen Jadwal** | | | | |
| FR-SCHED-01 | Atur ketersediaan mingguan (berulang) | Harus Ada | Terapis | Terapis atur jam kerja per hari |  Terimplementasi |
| FR-SCHED-02 | Blokir tanggal tertentu (cuti, libur) | Harus Ada | Terapis | Terapis blokir tanggal tertentu |  Terimplementasi |
| FR-SCHED-03 | Lihat kalender janji temu | Harus Ada | Terapis | Terapis lihat jadwal dalam tampilan kalender |  Terimplementasi |
| FR-SCHED-04 | Terima/tolak permintaan pemesanan | Sebaiknya Ada | Terapis | Terapis bisa setujui atau tolak pemesanan | 🔜 Direncanakan |
| **FR-SESSION** | **Manajemen Sesi** | | | | |
| FR-SESS-01 | Mulai sesi (tandai sebagai dimulai) | Harus Ada | Terapis | Terapis mulai sesi tepat waktu |  Sedang Berjalan |
| FR-SESS-02 | Akhiri sesi dan input catatan sesi | Harus Ada | Terapis | Terapis dokumentasi sesi secara terstruktur |  Sedang Berjalan |
| FR-SESS-03 | Unggah lampiran sesi (file, gambar) | Bisa Ada | Terapis | Terapis unggah dokumen pendukung | 🔜 Direncanakan |
| FR-SESS-04 | Lihat riwayat sesi dengan catatan | Harus Ada | Terapis | Terapis akses riwayat sesi klien |  Sedang Berjalan |
| FR-SESS-05 | Klien lihat catatan sesi sendiri (ringkasan saja) | Sebaiknya Ada | Klien | Klien lihat ringkasan kemajuan | 🔜 Direncanakan |
| **FR-PAYMENT** | **Manajemen Pembayaran** | | | | |
| FR-PAY-01 | Beberapa metode pembayaran (transfer, kartu kredit, *ewallet*) | Harus Ada | Klien | Klien pilih metode pembayaran |  Sedang Berjalan |
| FR-PAY-02 | Integrasi *payment gateway* (Midtrans) | Harus Ada | Klien | Klien bayar via *payment gateway* |  Sedang Berjalan |
| FR-PAY-03 | Unggah bukti pembayaran (transfer manual) | Harus Ada | Klien | Klien unggah bukti transfer |  Sedang Berjalan |
| FR-PAY-04 | Admin verifikasi pembayaran manual | Harus Ada | Admin | Admin setujui/tolak pembayaran |  Sedang Berjalan |
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
| FR-ADM-01 | Kelola pengguna (CRUD) | Harus Ada | Admin | Admin kelola semua pengguna |  Sedang Berjalan |
| FR-ADM-02 | Kelola layanan (CRUD) | Harus Ada | Admin | Admin kelola layanan |  Sedang Berjalan |
| FR-ADM-03 | Lihat semua pemesanan dan status | Harus Ada | Admin | Admin pantau semua pemesanan |  Sedang Berjalan |
| FR-ADM-04 | Buat laporan keuangan | Sebaiknya Ada | Admin | Admin ekspor laporan keuangan | 🔜 Direncanakan |
| FR-ADM-05 | Konfigurasi dan pengaturan sistem | Harus Ada | Admin | Admin ubah pengaturan sistem |  Sedang Berjalan |
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
| ***Framework Backend*** | Laravel 10 | Express.js (Node.js) | Django (Python) |  Laravel 10 | MVC *built-in*, Eloquent ORM, ekosistem besar, kebutuhan akademik, keahlian tim |
| **Bahasa Pemrograman** | PHP 8.2 | JavaScript (Node) | Python 3.11 |  PHP 8.2 | Fitur modern (*enum*, *readonly*), *strong typing*, kompatibilitas Laravel |
| **Basis Data** | MySQL 8.0 | PostgreSQL 15 | MongoDB 6.0 |  MySQL 8.0 | Kepatuhan ACID, data relasional cocok, gratis, dukungan *hosting* luas |
| ***Framework* CSS** | Tailwind CSS 3.3 | Bootstrap 5 | CSS Kustom |  Tailwind 3.3 | *Utility-first*, sangat dapat disesuaikan, ukuran *bundle* lebih kecil, modern |
| **JavaScript** | Alpine.js 3.x | Vue.js 3 | React 18 |  Alpine.js | Ringan (15KB), deklaratif, *overhead* minimal, kompatibel Laravel Livewire |
| **Mesin Templat** | Blade (Laravel) | Twig | PHP Biasa |  Blade | *Built-in* Laravel, sintaks bersih, pewarisan templat, direktif |
| **Autentikasi** | Laravel Sanctum | Laravel Passport | JWT (tymon/jwt-auth) |  Sanctum | Ringan, ramah SPA, berbasis token, dibuat untuk Laravel |
| ***Payment Gateway*** | Midtrans | Xendit | Stripe |  Midtrans | Fokus Indonesia, beberapa metode pembayaran, dokumentasi baik, biaya terjangkau |
| **Layanan Email** | SendGrid | Mailgun | AWS SES |  SendGrid | Andal, 100 email/hari gratis, *deliverability* baik, integrasi mudah |
| ***Hosting*** | Niagahoster VPS | DigitalOcean Droplet | AWS EC2 |  Niagahoster VPS | Berbasis Indonesia, terjangkau (Rp 300k/bln), terkelola, dukungan lokal |
| **Kontrol Versi** | GitHub | GitLab | Bitbucket |  GitHub | Repo privat gratis, CI/CD (Actions), komunitas besar, familiar |
| **Manajemen Tugas** | Asana | Trello | Jira |  Asana | Dependensi tugas, tampilan *timeline*, tier gratis cukup, kolaboratif |
| **Alat Desain** | Figma | Adobe XD | Sketch |  Figma | Kolaboratif, berbasis *browser*, tier gratis, pustaka komponen, *prototyping* |
| **Pengujian API** | Postman | Insomnia | Thunder Client |  Postman | Koleksi, variabel lingkungan, sinkronisasi tim, komprehensif |
| **Alat Basis Data** | MySQL Workbench | phpMyAdmin | DBeaver |  MySQL Workbench | Perancang ERD visual, alat optimasi *query*, dukungan migrasi |
| **Pelacakan Error** | Sentry | Rollbar | Bugsnag |  Sentry | Pemberitahuan *real-time*, *stack trace*, tier gratis 5k *event*/bln, integrasi Laravel |
| **Pemantauan** | UptimeRobot | Pingdom | StatusCake |  UptimeRobot | Gratis 50 monitor, interval 5 menit, pemberitahuan email/SMS, halaman status publik |

**Kriteria Pemilihan Utama:**
1. **Biaya:** Gratis atau terjangkau untuk anggaran Rp 5 juta
2. **Kurva Belajar:** Tim familiar atau mudah dipelajari
3. **Dukungan Komunitas:** Komunitas besar, dokumentasi baik
4. **Integrasi:** Integrasi mulus dengan *stack* lain
5. **Skalabilitas:** Dapat menangani pertumbuhan
6. **Kebutuhan Akademik:** Harus menggunakan Laravel (batasan akademik)

---

### 4.3.2 Fitur-Fitur Utama Sistem

Sistem CUR-HEART terdiri dari **41 halaman interface** yang dikelompokkan berdasarkan peran pengguna dan fungsi bisnis. Berikut adalah ringkasan komprehensif dari seluruh halaman yang dirancang:

**Tabel 4.11 Ringkasan Fitur dan Halaman Sistem CUR-HEART**

| No | Kategori | Nama Halaman | Fungsi Utama | Target Pengguna | Fitur Kunci |
|----|----------|--------------|--------------|-----------------|-------------|
| 1 | Public | Landing Page | Halaman utama untuk konversi pengunjung | Visitor/Calon Klien | Hero section, service overview, testimonials, CTA booking |
| 2 | Public | About Us | Membangun kredibilitas dan kepercayaan | Visitor/Calon Klien | Company story, pendiri, sertifikasi, nilai perusahaan |
| 3 | Public | Services Catalog | Katalog layanan dengan filtering | Visitor/Calon Klien | Grid 6 layanan, filter kategori, sorting harga/durasi |
| 4 | Public | Service Detail | Detail lengkap per layanan | Visitor/Calon Klien | Deskripsi, manfaat, harga, terapis tersedia, CTA booking |
| 5 | Public | Therapists Directory | Direktori terapis dengan filter | Visitor/Calon Klien | Grid terapis, filter spesialisasi, rating, search |
| 6 | Public | Therapist Profile | Profil detail terapis | Visitor/Calon Klien | Bio, spesialisasi, layanan, availability, reviews, CTA |
| 7 | Public | Blog | Repositori artikel edukatif | Visitor/Semua User | Grid artikel, kategori, search, pagination |
| 8 | Public | Blog Detail | Halaman artikel lengkap | Visitor/Semua User | Content, author, sharing, komentar, related articles |
| 9 | Public | Contact | Formulir kontak dan info lokasi | Visitor/Semua User | Form kontak, alamat, telepon, email, maps embed |
| 10 | Public | FAQ | Pertanyaan umum dengan accordion | Visitor/Semua User | Kategori FAQ, accordion layout, search |
| 11 | Public Legal | Privacy Policy | Dokumen kebijakan privasi | Visitor/Semua User | TOC, pengumpulan data, hak pengguna, cookies |
| 12 | Public Legal | Terms & Conditions | Syarat dan ketentuan layanan | Visitor/Semua User | Kewajiban, kebijakan pembatalan, tanggung jawab |
| 13 | Auth | Login | Autentikasi pengguna | Semua User | Form email/password, remember me, forgot password, social login |
| 14 | Auth | Register | Pendaftaran akun baru | Calon User | Form registrasi, pilih role (Klien/Terapis), email verification |
| 15 | Auth | Forgot Password | Request reset password | Semua User | Input email, kirim reset link |
| 16 | Auth | Reset Password | Set password baru | Semua User | Token validation, form password baru, konfirmasi |
| 17 | Client | Client Dashboard | Overview status klien | Klien | Summary cards, upcoming appointments, quick actions, activity |
| 18 | Client | Booking Step 1 | Pilih layanan (booking flow) | Klien | Service selection grid, stepper 1/4, next button |
| 19 | Client | Booking Step 2 | Pilih terapis (booking flow) | Klien | Therapist cards filtered by service, stepper 2/4 |
| 20 | Client | Booking Step 3 | Pilih tanggal & waktu | Klien | Calendar widget, time slots, stepper 3/4 |
| 21 | Client | Booking Step 4 | Konfirmasi & pembayaran | Klien | Summary review, payment method, confirm booking |
| 22 | Client | Appointments | Manajemen janji temu | Klien | Tabs (upcoming/completed/cancelled), search, filter, actions |
| 23 | Client | Appointment Detail | Detail janji temu individu | Klien | Info lengkap, payment summary, actions (join/reschedule/cancel) |
| 24 | Client | Profile | Kelola profil pribadi | Klien | Form profile, foto, settings, change password, preferences |
| 25 | Client | Progress & History | Tracking kemajuan terapi | Klien | Summary stats, session timeline, notes, goals, achievements |
| 26 | Client | Messages | Komunikasi dengan terapis/admin | Klien | Inbox layout, conversation threads, attachments, notifications |
| 27 | Therapist | Therapist Dashboard | Overview untuk terapis | Terapis | Today's schedule, stats cards, quick actions, notifications |
| 28 | Therapist | Schedule Management | Manajemen kalender | Terapis | Calendar view (day/week/month), availability settings, sync |
| 29 | Therapist | Clients List | Daftar semua klien | Terapis | Table/grid klien, search, filter, total sessions |
| 30 | Therapist | Client Profile View | Profil klien (viewed by therapist) | Terapis | Client info, session history, notes, goals, actions |
| 31 | Therapist | Session Notes | Buat/edit catatan sesi | Terapis | Form notes (goal, topic, techniques, observation, plan) |
| 32 | Therapist | My Profile | Kelola profil profesional | Terapis | Bio, credentials, specializations, education, services, rates |
| 33 | Therapist | Reviews & Ratings | Lihat semua review dari klien | Terapis | Summary rating, review list, reply, filter/sort |
| 34 | Therapist | Earnings | Track pendapatan dan keuangan | Terapis | Earning summary, charts, transaction details, withdrawal |
| 35 | Therapist | Messages | Komunikasi dengan klien/admin | Terapis | Inbox layout, conversation threads |
| 36 | Therapist | Analytics | Dashboard analitik (optional) | Terapis | Metrics, charts (sessions/services/attendance), insights |
| 37 | Admin | Admin Dashboard | Overview sistem | Admin | Key stats, growth charts, recent activity, quick actions |
| 38 | Admin | Users Management | Kelola semua user | Admin | Tabs (all/clients/therapists/admin), table, search, filter, CRUD |
| 39 | Admin | Appointments Management | Kelola semua janji temu | Admin | Tabs by status, table, search, filter, CRUD, export |
| 40 | Admin | Services & Content | Kelola layanan dan konten | Admin | Tabs (services/blog/FAQ/testimonials), CRUD operations |
| 41 | Admin | System Settings | Konfigurasi platform | Admin | Tabs (general/payment/email/notifications/legal/advanced) |

**Penjelasan Kategori Halaman:**

**A. Public Pages (12 halaman):** Halaman yang dapat diakses tanpa login, dirancang untuk konversi pengunjung menjadi klien, membangun kredibilitas, dan memberikan informasi layanan. Termasuk landing page dengan hero section dan CTA, katalog layanan dengan filtering, direktori terapis dengan rating dan spesialisasi, blog untuk konten edukatif, serta halaman legal (Privacy Policy & Terms).

**B. Authentication (4 halaman):** Sistem autentikasi lengkap dengan login multi-role, registrasi dengan pemilihan role (Klien/Terapis), forgot password dengan email verification, dan reset password dengan token validation untuk keamanan.

**C. Client Dashboard (10 halaman):** Portal lengkap untuk klien mencakup dashboard dengan summary cards dan upcoming appointments, booking flow 4-step yang intuitif (pilih layanan → terapis → waktu → bayar), manajemen janji temu dengan tabs status, tracking progress dengan goals dan achievements, serta sistem messaging untuk komunikasi dengan terapis.

**D. Therapist Dashboard (10 halaman):** Portal profesional untuk terapis dengan dashboard yang menampilkan jadwal harian dan metrics, manajemen kalender dengan availability settings, daftar klien dengan session history, form session notes terstruktur, profil profesional dengan credentials dan specializations, halaman earnings dengan withdrawal system, dan analytics untuk insight kinerja.

**E. Admin Dashboard (5 halaman):** Panel kontrol penuh untuk admin mencakup dashboard dengan statistik sistem, manajemen user dengan CRUD lengkap untuk semua role, manajemen appointments dengan export data, manajemen services dan content (layanan, blog, FAQ, testimonials), serta system settings komprehensif untuk konfigurasi platform (payment gateway, email, notifications, legal documents).

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