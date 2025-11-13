# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 4)

## 4.4 Faktor Penentu Keberhasilan

Keberhasilan implementasi Sistem Informasi CUR-HEART ditentukan oleh berbagai faktor yang saling berkaitan. Faktor-faktor ini dibagi menjadi Faktor Kunci Keberhasilan (*Key Success Factors*/KSF), Faktor Kritis Keberhasilan (*Critical Success Factors*/CSF), dan Indikator Kinerja Utama (*Key Performance Indicators*/KPI).

### 4.4.1 Faktor Kunci Keberhasilan (*Key Success Factors*/KSF)

Faktor Kunci Keberhasilan adalah faktor-faktor kunci yang mendukung pencapaian tujuan proyek secara umum.

#### A. Faktor Teknologi

**1. Stabilitas dan Keandalan Sistem**
- Sistem harus mampu beroperasi 24/7 dengan waktu aktif (*uptime*) minimal 99,5%
- Waktu respons halaman tidak lebih dari 2 detik
- Optimasi kueri basis data untuk menangani pengguna bersamaan
- Pencadangan otomatis harian untuk keamanan data

**2. Antarmuka yang Mudah Digunakan**
- Desain antarmuka/pengalaman pengguna yang intuitif dan mudah dipahami
- Desain responsif untuk semua perangkat (desktop, tablet, ponsel)
- Bahasa desain yang konsisten menggunakan sistem desain
- Standar aksesibilitas (WCAG 2.1 Level AA)

**3. Keamanan Data**
- Enkripsi data sensitif (kata sandi, riwayat medis)
- HTTPS untuk semua komunikasi
- Autentikasi dan otorisasi yang kuat
- Kepatuhan terhadap UU PDP (Perlindungan Data Pribadi)
- Audit keamanan dan uji penetrasi berkala

**4. Skalabilitas**
- Arsitektur yang dapat menangani pertumbuhan pengguna
- Normalisasi basis data untuk efisiensi penyimpanan
- Mekanisme *cache* untuk optimasi kinerja
- Kemampuan penyeimbang beban (*load balancing*) untuk lalu lintas tinggi

#### B. Faktor Manusia

**1. Kompetensi Tim Pengembang**
- Penguasaan kerangka kerja Laravel dan pemrograman PHP
- Pemahaman desain basis data dan MySQL
- Kemampuan pengembangan antarmuka (HTML, CSS, JavaScript, Tailwind)
- Pengetahuan tentang kontrol versi (Git)
- Keterampilan lunak: komunikasi, pemecahan masalah, kerja tim

**2. Komitmen Pemangku Kepentingan**
- Dukungan penuh dari manajemen CUR-HEART
- Keterlibatan aktif pemilik dalam pengumpulan kebutuhan
- Umpan balik konstruktif dari terapis dan admin
- Kesediaan untuk pengujian dan UAT (*User Acceptance Testing*/Pengujian Penerimaan Pengguna)

**3. Tingkat Adopsi oleh Pengguna**
- Pelatihan yang memadai untuk terapis dan admin
- Panduan pengguna yang komprehensif
- Dukungan teknis yang responsif
- Manajemen perubahan yang efektif

#### C. Faktor Manajemen Proyek

**1. Perencanaan yang Matang**
- Ruang lingkup yang jelas dan terukur
- Jadwal waktu yang realistis (11 minggu)
- Alokasi sumber daya yang optimal
- Strategi mitigasi risiko yang efektif

**2. Komunikasi yang Efektif**
- Pertemuan rutin (pertemuan mingguan)
- Dokumentasi yang jelas (dokumentasi teknis dan pengguna)
- Pelacakan kemajuan dengan diagram Gantt
- Pelacakan dan penyelesaian masalah

**3. Jaminan Kualitas**
- Pengujian sistematis di setiap fase (unit, integrasi, sistem, UAT)
- Tinjauan kode dan pemrograman sejawat
- Pelacakan bug dan prioritas perbaikan
- Perbaikan berkelanjutan berdasarkan umpan balik

#### D. Faktor Bisnis

**1. Proposisi Nilai yang Jelas**
- Sistem memberikan nilai nyata untuk bisnis CUR-HEART
- ROI (*Return on Investment*/Laba atas Investasi) yang terukur
- Keunggulan kompetitif terhadap pesaing
- Keselarasan dengan tujuan dan strategi bisnis

**2. Kesiapan Pasar**
- Pengguna target (klien) sudah familiar dengan pemesanan digital
- Infrastruktur pendukung tersedia (internet, perangkat)
- Regulasi yang mendukung telemedisin/terapi daring
- Permintaan pasar untuk layanan kesehatan mental digital

**3. Keberlanjutan Finansial**
- Anggaran yang memadai untuk pengembangan dan pemeliharaan
- Model pendapatan yang layak (biaya per pemesanan, berlangganan)
- Efisiensi biaya dibanding proses manual
- Dana kontinjensi untuk pengeluaran tidak terduga

---

**Tabel 4.32 Ringkasan Faktor Kunci Keberhasilan (KSF)**

| Kategori | Faktor | Tingkat Kepentingan | Indikator Pengukuran |
|----------|--------|---------------------|----------------------|
| **Teknologi** | Stabilitas dan Keandalan Sistem | Kritis | Waktu aktif ≥ 99,5%, Waktu respons < 2 detik |
| | Antarmuka Mudah Digunakan | Tinggi | Skor SUS ≥ 68, Desain responsif |
| | Keamanan Data | Kritis | Audit keamanan, Kepatuhan UU PDP |
| | Skalabilitas | Sedang | Uji beban, Pengguna bersamaan |
| **Manusia** | Kompetensi Tim Pengembang | Tinggi | Kualitas kode, Pengiriman tepat waktu |
| | Komitmen Pemangku Kepentingan | Tinggi | Skor keterlibatan, Partisipasi UAT |
| | Adopsi Pengguna | Kritis | Tingkat adopsi ≥ 70% |
| **Manajemen Proyek** | Perencanaan yang Matang | Tinggi | Kepatuhan jadwal dan anggaran |
| | Komunikasi Efektif | Tinggi | Frekuensi pertemuan, Dokumentasi |
| | Jaminan Kualitas | Kritis | Cakupan pengujian ≥ 70% |
| **Bisnis** | Proposisi Nilai | Kritis | ROI ≥ 200%, Efisiensi ≥ 40% |
| | Kesiapan Pasar | Sedang | Riset pasar, Infrastruktur |
| | Keberlanjutan Finansial | Tinggi | Varians anggaran < 10% |

**Prioritas KSF:**
- Kritis: 5 faktor (Stabilitas Sistem, Keamanan Data, Adopsi Pengguna, Jaminan Kualitas, Proposisi Nilai)
- Tinggi: 6 faktor (Antarmuka, Kompetensi Tim, Komitmen, Perencanaan, Komunikasi, Finansial)
- Sedang: 2 faktor (Skalabilitas, Kesiapan Pasar)

---

### 4.4.2 Faktor Kritis Keberhasilan (*Critical Success Factors*/CSF)

Faktor Kritis Keberhasilan adalah faktor-faktor kritis yang **harus** dipenuhi agar proyek berhasil. Jika salah satu CSF tidak terpenuhi, proyek akan gagal.

#### CSF 1: Ketersediaan dan Keandalan Sistem

**Definisi:**
Sistem harus dapat diakses kapan saja oleh pengguna dengan tingkat ketersediaan minimal 99,5% (waktu aktif) dan mampu menangani beban pengguna secara bersamaan tanpa waktu henti.

**Indikator Keberhasilan:**
- Waktu aktif ≥ 99,5% (maksimal 3,6 jam waktu henti per bulan)
- Waktu respons maksimum: 2 detik untuk halaman standar
- Dapat menangani minimal 100 pengguna bersamaan
- Tanpa kehilangan data dalam kondisi normal

**Strategi Pencapaian:**
- Hosting pada server yang andal (VPS dengan SLA 99,9%)
- Implementasi pengindeksan basis data untuk optimasi kueri
- *Caching* menggunakan Laravel Cache
- Pemantauan rutin menggunakan alat pemantauan waktu aktif
- Pencadangan otomatis harian dengan retensi 30 hari

**Risiko Jika Tidak Terpenuhi:**
- Pengguna frustrasi karena sistem sering mati
- Kehilangan kredibilitas dan kepercayaan
- Potensi kerugian pendapatan
- Ulasan negatif dan gunjingan buruk

---

#### CSF 2: Keamanan dan Privasi Data

**Definisi:**
Sistem harus menjamin keamanan dan kerahasiaan data pengguna, terutama data sensitif seperti riwayat medis, catatan sesi, dan informasi pembayaran. Kepatuhan terhadap UU PDP dan standar keamanan internasional.

**Indikator Keberhasilan:**
- Tanpa pelanggaran data atau akses tidak sah
- Semua data sensitif terenkripsi (kata sandi dengan bcrypt, data medis dengan AES-256)
- Implementasi HTTPS untuk semua halaman
- Kontrol akses berbasis peran (RBAC) berfungsi dengan baik
- Audit keamanan rutin menunjukkan tanpa kerentanan kritis

**Strategi Pencapaian:**
- Menggunakan fitur keamanan bawaan Laravel:
  - Perlindungan CSRF
  - Pencegahan XSS
  - Pencegahan injeksi SQL (Eloquent ORM)
  - Hashing kata sandi dengan bcrypt
- Validasi dan sanitasi input
- Implementasi Laravel Sanctum untuk autentikasi API
- Pembaruan dan perbaikan keamanan rutin
- Enkripsi data saat istirahat dan dalam transit
- Audit keamanan sebelum penyebaran produksi

**Risiko Jika Tidak Terpenuhi:**
- Tanggung jawab hukum (pelanggaran UU PDP, denda hingga Rp 5 miliar)
- Kehilangan kepercayaan klien dan reputasi
- Potensi gugatan hukum dari pengguna yang terdampak
- Risiko penutupan bisnis

---

#### CSF 3: Adopsi dan Kepuasan Pengguna

**Definisi:**
Sistem harus diadopsi dan digunakan secara aktif oleh pengguna target (klien, terapis, admin) dengan tingkat kepuasan yang tinggi.

**Indikator Keberhasilan:**
- Minimal 70% klien menggunakan sistem untuk pemesanan (vs. manual/telepon)
- Skor kepuasan pengguna ≥ 4,0 dari 5,0 (melalui survei)
- Skor Skala Kegunaan Sistem (SUS) ≥ 68 (di atas rata-rata)
- Tingkat adopsi terapis 100% (penggunaan wajib)
- Tingkat pengguna kembali ≥ 60% dalam 3 bulan pertama

**Strategi Pencapaian:**
- Desain antarmuka/pengalaman pengguna yang mudah digunakan dan intuitif
- Orientasi dan pelatihan komprehensif:
  - Tutorial video untuk klien
  - Pelatihan tatap muka untuk terapis dan admin
  - Panduan pengguna dalam Bahasa Indonesia
- Dukungan pelanggan yang responsif:
  - Halaman Tanya Jawab yang komprehensif
  - Dukungan obrolan langsung atau WhatsApp
  - Dukungan email dengan SLA respons 24 jam
- Perbaikan berkelanjutan berdasarkan umpan balik pengguna:
  - Survei setelah setiap pemesanan
  - Formulir umpan balik yang dapat diakses
  - Pembaruan dan perbaikan bug rutin

**Risiko Jika Tidak Terpenuhi:**
- Sistem tidak digunakan (kegagalan proyek)
- Investasi terbuang (anggaran Rp 5 juta)
- Penolakan perubahan dari staf
- Kelanjutan proses manual yang tidak efisien

---

#### CSF 4: Integrasi dengan Proses Bisnis

**Definisi:**
Sistem harus terintegrasi dengan mulus ke dalam proses bisnis yang sudah ada di CUR-HEART, tidak mengganggu operasional, dan meningkatkan efisiensi.

**Indikator Keberhasilan:**
- 100% pemesanan melalui sistem (tidak ada lagi pemesanan manual melalui lembar kerja)
- Pengurangan beban kerja administratif minimal 50%
- Pengurangan kesalahan pemesanan (pemesanan ganda, miskomunikasi) hingga 90%
- Laporan keuangan dapat dihasilkan dalam 5 menit (vs. 2 jam manual)

**Strategi Pencapaian:**
- Pengumpulan kebutuhan yang mendalam dengan pemangku kepentingan
- Rekayasa Ulang Proses Bisnis (*Business Process Reengineering*/BPR) jika diperlukan
- Strategi manajemen perubahan:
  - Komunikasi awal tentang perubahan
  - Keterlibatan pemangku kepentingan dalam fase desain
  - Peluncuran bertahap (uji coba → penyebaran penuh)
- Prosedur Operasi Standar (SOP) baru yang terdokumentasi
- Tinjauan dan penyesuaian rutin berdasarkan umpan balik

**Risiko Jika Tidak Terpenuhi:**
- Gangguan alur kerja
- Beban sistem ganda (manual + digital)
- Frustrasi dan penolakan staf
- Inefisiensi proses bisnis berlanjut

---

#### CSF 5: Kepatuhan Anggaran dan Jadwal Waktu

**Definisi:**
Proyek harus diselesaikan dalam waktu 11 minggu dengan anggaran Rp 5.000.000 tanpa pembengkakan besar.

**Indikator Keberhasilan:**
- Penyelesaian proyek dalam 11 minggu (± 1 minggu toleransi)
- Biaya aktual tidak melebihi anggaran 110% (Rp 5,5 juta)
- Semua hasil kerja diselesaikan sesuai ruang lingkup
- Tanpa perluasan ruang lingkup besar

**Strategi Pencapaian:**
- Perencanaan proyek detail dengan WBS dan diagram Gantt
- Pelacakan kemajuan mingguan dan pelaporan status
- Manajemen ruang lingkup yang ketat (proses permintaan perubahan formal)
- Optimasi sumber daya:
  - Manfaatkan alat dan pustaka sumber terbuka
  - Pengembangan internal vs. penyerahan keluar
  - Hosting awan dengan harga yang dapat diprediksi
- Penyangga risiko dalam jadwal waktu (10%) dan anggaran (10%)

**Risiko Jika Tidak Terpenuhi:**
- Pembatalan proyek jika pembengkakan anggaran signifikan
- Penundaan peluncuran → kehilangan peluang bisnis
- Ketidakpuasan pemangku kepentingan
- Fitur tidak lengkap → sistem tidak dapat digunakan

---

**Tabel 4.33 Ringkasan Faktor Kritis Keberhasilan (CSF)**

| ID CSF | Faktor Kritis | Indikator Keberhasilan | Nilai Target | Risiko Jika Tidak Terpenuhi |
|--------|---------------|------------------------|--------------|----------------------------|
| CSF-01 | Ketersediaan & Keandalan Sistem | Waktu aktif sistem, Waktu respons | ≥ 99,5%, < 2 detik | Frustrasi pengguna, kerugian pendapatan, sistem *crash* |
| CSF-02 | Keamanan & Privasi Data | Tanpa pelanggaran, enkripsi 100% | 0 insiden, RBAC fungsional | Tanggung jawab hukum (denda Rp 5M), kehilangan kepercayaan |
| CSF-03 | Adopsi & Kepuasan Pengguna | Tingkat adopsi, Skor SUS, Rating | ≥ 70%, ≥ 68, ≥ 4,0/5,0 | Kegagalan proyek, ulasan negatif |
| CSF-04 | Integrasi Proses Bisnis | Pemesanan via sistem, pengurangan beban | 100%, ≥ 50% | Beban sistem ganda, inefisiensi berlanjut |
| CSF-05 | Kepatuhan Anggaran & Jadwal | Penyelesaian proyek, varians anggaran | 11 minggu ± 1, ≤ 10% | Manfaat tertunda, pembatalan proyek |

**Status Pencapaian CSF (per November 2024):**
- CSF-01: ⏳ 70% (Sistem stabil, kinerja baik, perlu pengujian produksi)
- CSF-02: ✅ 90% (Keamanan diimplementasi, menunggu audit akhir)
- CSF-03: 🔜 30% (Menunggu UAT dan penyebaran untuk pengujian pengguna)
- CSF-04: ⏳ 50% (Integrasi dirancang, perlu implementasi)
- CSF-05: ✅ 85% (Sesuai jalur - Minggu ke-7 dari 11, anggaran 65% terpakai)

---

### 4.4.3 Indikator Kinerja Utama (*Key Performance Indicators*/KPI)

KPI adalah metrik terukur yang digunakan untuk memantau dan mengevaluasi keberhasilan sistem setelah penyebaran.

---

**[GAMBAR 4.65 - Visualisasi Metrik Dasbor KPI]** 📊
_Dasbor waktu nyata menampilkan kinerja sistem, adopsi pengguna, pendapatan, dan metrik kepuasan_

---

**Tabel 4.34 Ringkasan Indikator Kinerja Utama (KPI)**

| Kategori | Nama KPI | Nilai Target | Frekuensi Pemantauan | Penanggung Jawab |
|----------|----------|--------------|----------------------|------------------|
| **Kinerja Sistem** | Waktu Aktif Sistem | ≥ 99,5% | Waktu nyata | Tim DevOps |
| | Waktu Respons Rata-rata | ≤ 2 detik | Mingguan | Tim Backend |
| | Tingkat Kesalahan | ≤ 0,5% | Harian | Tim *Full-stack* |
| | Kapasitas Pengguna Bersamaan | ≥ 100 pengguna | Pra-peluncuran, Triwulanan | Tim DevOps |
| **Keamanan** | Kerentanan Keamanan | 0 kritis, ≤ 2 tinggi | Bulanan | Tim Keamanan |
| | Insiden Pelanggaran Data | 0 insiden | Waktu nyata | Tim Keamanan |
| **Kualitas** | Cakupan Uji Kode | ≥ 70% | Per *commit* | Tim Pengembangan |
| | Cakupan Dokumentasi | ≥ 80% | Bulanan | Tim Pengembangan |
| **Adopsi Pengguna** | Total Pengguna Terdaftar | 200 dalam 3 bulan | Bulanan | Tim Pemasaran |
| | Pengguna Aktif (MAU) | 150 pengguna (75%) | Bulanan | Tim Produk |
| | Tingkat Konversi Pemesanan | ≥ 60% | Mingguan | Tim Produk |
| | Tingkat Retensi (3 bulan) | ≥ 60% | Triwulanan | Tim Produk |
| **Transaksi** | Total Pemesanan per Bulan | 100 pemesanan | Bulanan | Tim Operasi |
| | Tingkat Keberhasilan Pembayaran | ≥ 95% | Mingguan | Tim Keuangan |
| | Pendapatan per Bulan | Rp 30.000.000 | Bulanan | Tim Keuangan |
| **Kepuasan** | Skor Kepuasan Pengguna | ≥ 4,0/5,0 | Per pemesanan | Layanan Pelanggan |
| | Skor Promotor Bersih (NPS) | ≥ 30 | Triwulanan | Tim Pemasaran |
| | Skala Kegunaan Sistem (SUS) | ≥ 68 | Pasca-UAT, Triwulanan | Tim Produk |
| **Efisiensi** | Waktu Pemesanan Rata-rata | ≤ 3 menit | Mingguan | Tim Produk |
| | Pengurangan Beban Kerja Admin | ≥ 50% | Bulanan | Manajemen |
| | Waktu Pembuatan Laporan | ≤ 5 menit | Bulanan | Tim TI |

**Ringkasan KPI:**
- Total KPI: 21 indikator utama
- Area Fokus: Kinerja (4), Keamanan (2), Kualitas (2), Adopsi (4), Transaksi (3), Kepuasan (3), Efisiensi (3)
- KPI Kritis: Waktu Aktif, Keamanan, Adopsi Pengguna, Pendapatan, Kepuasan
- Alat Pengukuran: UptimeRobot, GTmetrix, OWASP ZAP, Google Analytics, PHPUnit

---

## 4.5 Keuntungan yang Diharapkan

Implementasi Sistem Informasi CUR-HEART diharapkan memberikan berbagai keuntungan bagi pemangku kepentingan yang terlibat.

### 4.5.1 Manfaat untuk CUR-HEART (Bisnis)

---

**Tabel 4.37 Analisis Manfaat - CUR-HEART (Organisasi)**

| Kategori Manfaat | Manfaat Spesifik | Nilai Dasar | Target Setelah Sistem | Dampak Terukur | Prioritas |
|------------------|-----------------|-------------|----------------------|----------------|-----------|
| **Efisiensi Operasional** | Proses pemesanan otomatis | 10-15 menit/pemesanan | 3 menit/pemesanan | Penghematan: 20 jam/bulan = **Rp 6 juta/tahun** | TINGGI |
| | Manajemen penjadwalan | 5 jam/minggu koordinasi | 1 jam/minggu | Utilisasi: 60% → 80%, Hemat Rp 400rb/bulan | TINGGI |
| | Pelaporan otomatis | 2 jam/laporan | 5 menit otomatis | Penghematan: 8 jam/bulan = **Rp 2,4 juta/tahun** | SEDANG |
| | Eliminasi pemesanan ganda | 2-3 insiden/bulan | 0 insiden | Konflik dicegah 100%, Kepuasan meningkat | TINGGI |
| **Pertumbuhan Pendapatan** | Peningkatan volume pemesanan | 80 pemesanan/bulan | 100 pemesanan (+25%) | **Rp 72 juta/tahun** pendapatan tambahan | KRITIS |
| | Pengurangan tidak hadir | 15% (12/bulan) | 5% (4/bulan) | **Rp 28,8 juta/tahun** pendapatan dipulihkan | TINGGI |
| | Peluang *upselling* | Visibilitas terbatas | Rekomendasi otomatis | 20% pesan tambahan = **Rp 5 juta/tahun** | SEDANG |
| | Perpanjangan jam layanan | 08:00-17:00 (9 jam) | Pemesanan 24/7 | Tangkap 15% lebih = **Rp 10 juta/tahun** | TINGGI |
| **Kualitas & Layanan** | Pengambilan keputusan data | Analisis manual tertunda | Dasbor waktu nyata | Keputusan: hari → jam, Wawasan lebih baik | TINGGI |
| | Pemantauan kualitas | Umpan balik informal | Sistematis (SUS 68+, NPS 30+) | Perbaikan berkelanjutan, Jaminan kualitas | TINGGI |
| | Retensi klien | 35% kembali | 60% target | Loyalitas meningkat, Nilai seumur hidup tinggi | KRITIS |
| **Skalabilitas** | Ekspansi bisnis | Terbatas manual | Sistem digital skalabel | Dukung pertumbuhan 5× tanpa tambahan staf | KRITIS |
| **Penghematan Biaya** | Pengurangan beban admin | 100% manual | 50% otomatis | Bebaskan 50% waktu = **Rp 10 juta/tahun** | TINGGI |
| | Biaya kesalahan | Kesalahan manusia | Validasi sistem (95% reduksi) | Kompensasi Rp 0, Layanan pelanggan -70% | SEDANG |

**Total Manfaat Tahunan Terukur:**
- **Peningkatan Pendapatan**: Rp 115,8 juta/tahun
- **Penghematan Biaya**: Rp 18,4 juta/tahun
- **TOTAL MANFAAT**: **Rp 134,2 juta/tahun**
- **ROI atas Investasi Rp 5 juta**: **2.584% per tahun**

---

### 4.5.2 Manfaat untuk Klien

---

**Tabel 4.38 Analisis Manfaat - Klien (Pengguna Akhir)**

| Kategori Manfaat | Manfaat Spesifik | Masalah yang Diselesaikan | Dampak untuk Pengguna | Metrik Kepuasan | Prioritas |
|------------------|-----------------|---------------------------|----------------------|-----------------|----------|
| **Kenyamanan** | Pemesanan 24/7 | Terbatas jam kantor 08:00-17:00 | Pesan kapan saja, konfirmasi instan | Penyelesaian: 90% | KRITIS |
| | Tidak perlu telepon | Harus menelepon & menunggu | Layanan mandiri online | 85% lebih suka online | TINGGI |
| | Ramah ponsel | Hanya desktop | Pesan saat bepergian, akses mudah | 70% via ponsel | TINGGI |
| | Penjadwalan ulang mudah | Koordinasi manual | Ubah jadwal satu klik, tanpa penalti | Rating: 4,5/5 | TINGGI |
| **Transparansi** | Profil terapis lengkap | Info terbatas | Detail pendidikan, spesialisasi, ulasan | 95% lihat profil dulu | KRITIS |
| | Ketersediaan real-time | Telepon untuk cek | Kalender visual slot terbuka | 90% gunakan kalender | TINGGI |
| | Harga jelas | Harga ambigu | Harga transparan per layanan | Rating: 4,6/5 | TINGGI |
| | Rating & ulasan | Tanpa umpan balik | Sistem rating 1-5 bintang + ulasan | 80% baca ulasan | TINGGI |
| **Layanan Mandiri** | Riwayat janji temu | Pencatatan manual | Rekaman digital semua pemesanan | 60% gunakan | SEDANG |
| | Akses catatan sesi | Tidak ada akses | Lihat catatan yang dibagikan terapis | Rating: 4,3/5 | SEDANG |
| | Riwayat pembayaran | Kwitansi manual | Rekaman pembayaran digital | 70% gunakan | SEDANG |
| **Kualitas Perawatan** | Pelacakan kemajuan | Tanpa visibilitas | Grafik & metrik visual | 50% lihat kemajuan | TINGGI |
| | Konsistensi terapi | Lupa tindak lanjut | Pengingat otomatis + pesan ulang mudah | Retensi: 60% → 75% | TINGGI |
| **Komunikasi** | Pengingat otomatis | Manual atau tidak ada | Email + SMS (H-1, H-0) | 90% hadir setelah reminder | TINGGI |
| | Dukungan dalam aplikasi | Telepon jam kantor | Tiket dukungan + FAQ | Rating: 4,0/5 | SEDANG |
| **Privasi & Keamanan** | Privasi data | Penanganan tidak pasti | Patuh UU PDP, enkripsi | Rating: 4,5/5 | KRITIS |
| | Pembayaran aman | Manual tunai/transfer | *Payment gateway* aman (SSL) | Rating: 4,6/5 | TINGGI |
| **Penghematan** | Waktu hemat | Proses 30-60 menit | Proses 3-5 menit | Hemat 25-55 menit | TINGGI |
| **Pengalaman** | Kepuasan keseluruhan | Frustrasi manual | Pengalaman digital mulus | Target SUS: 68+ | KRITIS |
| | Kemungkinan kembali | Tingkat 35% | Pengalaman lebih baik | Target: 60% | TINGGI |

**Ringkasan Nilai untuk Klien:**
- **Penghematan Waktu**: 25-55 menit per pemesanan
- **Kepuasan**: Target ≥ 4,0/5,0, SUS ≥ 68
- **Retensi**: Peningkatan dari 35% → 60%
- **Kenyamanan**: Akses 24/7, ramah ponsel, layanan mandiri

---

**Tabel 4.35 Ringkasan Manfaat bagi Pemangku Kepentingan**

| Pemangku Kepentingan | Kategori Manfaat | Manfaat Utama | Dampak Terukur |
|----------------------|------------------|---------------|----------------|
| **CUR-HEART (Organisasi)** | Efisiensi Operasional | Proses pemesanan otomatis, pelaporan otomatis | Penghematan: Rp 13.200.000/tahun (20 + 16 + 8 jam/bulan) |
| | Pertumbuhan Pendapatan | Peningkatan volume pemesanan, pengurangan tidak hadir | Tambahan: Rp 116.800.000/tahun (+25% volume, -10% tidak hadir) |
| | Kualitas & Layanan | Pengambilan keputusan berbasis data, retensi klien | Retensi: 35% → 60%, NPS: 15 → 30 |
| **Klien (Pengguna)** | Kenyamanan | Pemesanan mandiri 24/7, ramah ponsel | Hemat waktu: 25-55 menit/pemesanan |
| | Transparansi | Profil terapis lengkap, harga jelas, rating & ulasan | Kepuasan: ≥ 4,0/5,0, SUS: ≥ 68 |
| | Kualitas | Pelacakan kemajuan, rekomendasi personal | Kepuasan: ≥ 4,0/5,0, retensi: 60% |
| **Terapis (Penyedia)** | Penghematan Waktu | Manajemen jadwal mandiri, koordinasi admin berkurang | Hemat: 16 jam/bulan (jadwal + koordinasi) |
| | Potensi Pendapatan | Utilisasi lebih baik (60% → 80%) | Pendapatan: +Rp 5.000.000/bulan (+33%) |
| | Keseimbangan Kerja-Hidup | Otonomi, fleksibilitas, beban admin berkurang | Kepuasan: ≥ 4,5/5,0, rekomendasi: ≥ 80% |

**Ringkasan Nilai:**
- **Organisasi**: Rp 130.000.000/tahun (pendapatan + penghematan)
- **Klien**: Hemat 25-55 menit/pemesanan, pengalaman lebih baik
- **Terapis**: Rp 9.000.000/bulan (waktu + pendapatan), kepuasan tinggi

---

### 4.5.4 Analisis *Return on Investment* (ROI)

---

**[GAMBAR 4.66 - Grafik Proyeksi ROI (5 Tahun)]** 📈
_Grafik proyeksi ROI 5 tahun menunjukkan pemulihan investasi, manfaat bersih, dan pengembalian kumulatif_

---

**Tabel 4.36 Ringkasan Analisis ROI Tahun Pertama**

| Kategori | Item Utama | Jumlah Tahunan (Rp) |
|----------|------------|---------------------|
| **INVESTASI AWAL** | Domain, *hosting* setup, layanan, cadangan | 3.000.000 |
| **BIAYA BERULANG (Tahun 1)** | Domain, *hosting*, email, *backup*, *payment gateway* (2%) | 9.750.000 |
| **TOTAL BIAYA TAHUN 1** | Awal + Berulang | **12.750.000** |
| **MANFAAT PENDAPATAN** | Pemesanan tambahan (+25%), pengurangan tidak hadir, *upselling*, jam diperpanjang | 142.800.000 |
| **PENGHEMATAN BIAYA** | Waktu admin, koordinasi, pelaporan, resolusi konflik, verifikasi pembayaran | 26.400.000 |
| **TOTAL MANFAAT TAHUN 1** | Pendapatan + Penghematan | **169.200.000** |
| **MANFAAT BERSIH** | Total Manfaat - Total Biaya | **156.450.000** |
| **ROI** | (Manfaat Bersih / Total Investasi) × 100% | **1.227%** |
| **PERIODE *PAYBACK*** | Total Investasi / Manfaat Bulanan | **0,9 bulan (~27 hari)** |

**Metrik Keuangan Kunci:**
- Rasio Manfaat-Biaya: 13,3:1 (setiap Rp 1 diinvestasikan menghasilkan Rp 13,3)
- Periode *payback*: Kurang dari 1 bulan
- ROI: 1.227% (pengembalian luar biasa)

---

**Tabel 4.37 Proyeksi Analisis Biaya-Manfaat 5 Tahun**

| Tahun | Total Biaya | Total Manfaat | Manfaat Bersih Tahunan | Manfaat Bersih Kumulatif | ROI Kumulatif |
|-------|-------------|---------------|------------------------|--------------------------|---------------|
| **0** | Rp 3.000.000 | Rp 0 | (Rp 3.000.000) | (Rp 3.000.000) | -100% |
| **1** | Rp 9.750.000 | Rp 169.200.000 | Rp 159.450.000 | Rp 156.450.000 | 1.218% |
| **2** | Rp 10.619.000 | Rp 186.480.000 | Rp 175.861.000 | Rp 332.311.000 | 2.506% |
| **3** | Rp 11.577.600 | Rp 203.742.000 | Rp 192.164.400 | Rp 524.475.400 | 3.947% |
| **4** | Rp 12.545.760 | Rp 222.660.900 | Rp 210.115.140 | Rp 734.590.540 | 5.528% |
| **5** | Rp 13.605.636 | Rp 243.398.925 | Rp 229.793.289 | Rp 964.383.829 | 7.258% |

**Ringkasan Kumulatif 5 Tahun:**
- Total Investasi: Rp 60.098.000
- Total Manfaat: Rp 1.025.481.825
- Total Manfaat Bersih: Rp 964.383.829
- Rata-rata Manfaat Bersih Tahunan: Rp 192.876.766
- ROI 5 Tahun: 7.258%
- Rasio Manfaat-Biaya: 17,1:1

**Asumsi Proyeksi:**
- Pertumbuhan pendapatan: +10% per tahun
- Inflasi biaya: +3% per tahun
- Utilisasi terapis: 80% (stabil)
- Tingkat retensi klien: 60% (tahun 1) → 70% (tahun 5)

---

**[GAMBAR 4.67 - Grafik Analisis Biaya-Manfaat]** 📊
_Analisis komparatif total biaya vs total manfaat selama 5 tahun dengan visualisasi titik impas_

---

**Tabel 4.41 Proyeksi Analisis Biaya-Manfaat 5 Tahun**

| Tahun | Total Biaya Tahunan | Total Manfaat | Manfaat Bersih Tahunan | Manfaat Bersih Kumulatif | ROI Kumulatif | Catatan |
|-------|---------------------|---------------|------------------------|--------------------------|---------------|---------|
| **0** | Rp 3.000.000 | Rp 0 | (Rp 3.000.000) | (Rp 3.000.000) | -100% | Setup awal (Bulan 1-3) |
| **1** | Rp 9.750.000 | Rp 169.200.000 | Rp 159.450.000 | Rp 156.450.000 | 1.218% | Operasi penuh (100% kapasitas) |
| **2** | Rp 10.619.000 | Rp 186.480.000 | Rp 175.861.000 | Rp 332.311.000 | 2.506% | Pertumbuhan +10%, Biaya +3% |
| **3** | Rp 11.577.600 | Rp 203.742.000 | Rp 192.164.400 | Rp 524.475.400 | 3.947% | Pertumbuhan berkelanjutan |
| **4** | Rp 12.545.760 | Rp 222.660.900 | Rp 210.115.140 | Rp 734.590.540 | 5.528% | Ekspansi pasar |
| **5** | Rp 13.605.636 | Rp 243.398.925 | Rp 229.793.289 | Rp 964.383.829 | 7.258% | Skala & optimisasi |

**Ringkasan Kumulatif 5 Tahun:**
- **Total Investasi**: Rp 60.098.000 (Rp 3M awal + Rp 57,098M berulang)
- **Total Manfaat**: Rp 1.025.481.825 (pendapatan + penghematan)
- **Manfaat Bersih**: Rp 964.383.829
- **ROI 5 Tahun**: 7.258%
- **Rasio Manfaat-Biaya**: 17,1:1

**Asumsi Proyeksi:**
- Pertumbuhan pendapatan: +10%/tahun
- Inflasi biaya: +3%/tahun
- Utilisasi terapis: 80% (stabil)
- Retensi klien: 60% (tahun 1) → 70% (tahun 5)

**Analisis Sensitivitas:**

| Skenario | Perubahan | ROI Tahun 1 | Manfaat Bersih 5 Tahun | Kelayakan |
|----------|-----------|-------------|------------------------|-----------|
| **Terbaik** (+20% pendapatan, -10% biaya) | +20%/-10% | 1.823% | Rp 1.276.909.180 | Luar biasa |
| **Dasar** (sesuai proyeksi) | 0%/0% | 1.227% | Rp 964.383.829 | Sangat baik |
| **Konservatif** (-10% pendapatan, +10% biaya) | -10%/+10% | 988% | Rp 672.419.562 | Sangat baik |
| **Terburuk** (-20% pendapatan, +20% biaya) | -20%/+20% | 749% | Rp 380.455.295 | Tetap menguntungkan |

**Analisis Impas:**
- Pemesanan minimum: 14/bulan (vs target 100/bulan)
- Ambang pendapatan: Rp 4,2M/bulan (vs proyeksi Rp 14,1M)
- Margin keamanan: 86% buffer

**Rekomendasi: LANJUTKAN DENGAN IMPLEMENTASI**
- ROI luar biasa bahkan di skenario terburuk (749%)
- Payback period < 1 bulan
- Risiko rendah dengan margin keamanan 86%
- Nilai strategis jangka panjang melampaui finansial

---

### 4.5.5 Manfaat Tidak Berwujud

Selain manfaat yang dapat dikuantifikasi, ada juga manfaat tidak berwujud (*intangible*):

#### A. Citra Merek dan Reputasi

**1. Citra Modern dan Profesional**
- Kehadiran di ruang digital
- Persepsi merek yang paham teknologi
- Membangun kepercayaan melalui transparansi

**2. Keunggulan Kompetitif**
- Keunggulan penggerak pertama (*first-mover advantage*) dalam pemesanan hipnoterapi digital di area tersebut
- Diferensiasi dari kompetitor yang masih manual
- Persepsi inovasi

#### B. Aset Data

**1. Kecerdasan Bisnis**
- Data perilaku pelanggan
- Wawasan popularitas layanan
- Peluang optimisasi harga
- Identifikasi tren pasar

**2. Perencanaan Strategis**
- Pengambilan keputusan berbasis data
- Kapabilitas analitik prediktif
- Optimisasi sumber daya

#### C. Skalabilitas dan Potensi Pertumbuhan

**1. Fondasi untuk Ekspansi**
- Siap untuk ekspansi ke berbagai lokasi
- Sistem siap waralaba
- API siap untuk integrasi masa depan (aplikasi mobile, sistem mitra)

**2. Aliran Pendapatan Baru**
- Kapabilitas konsultasi *online*
- Produk digital (sesi rekaman, materi *self-help*)
- Layanan B2B (program kesehatan korporat)

---