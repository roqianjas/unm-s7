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

**Tabel 4.32 Kategorisasi Faktor Kunci Keberhasilan (KSF)**

| Kategori | FKK | Sub-Faktor | Tingkat Kepentingan | Pengukuran |
|----------|-----|-------------|---------------------|------------|
| **Teknologi** | Stabilitas Sistem | • Waktu aktif ≥ 99,5%<br>• Waktu respons < 2 detik<br>• Optimasi basis data<br>• Pencadangan harian | Kritis | Pemantauan waktu aktif, Metrik kinerja |
| | Antarmuka Mudah Digunakan | • Antarmuka intuitif<br>• Desain responsif<br>• Sistem desain konsisten<br>• WCAG 2.1 AA | Tinggi | Skor SUS ≥ 68, Pengujian pengguna |
| | Keamanan Data | • Enkripsi (bcrypt, AES-256)<br>• HTTPS<br>• RBAC<br>• Kepatuhan UU PDP | Kritis | Audit keamanan, Tanpa pelanggaran |
| | Skalabilitas | • Menangani pertumbuhan<br>• Normalisasi basis data<br>• *Caching*<br>• Penyeimbang beban | Sedang | Uji beban, Pengguna bersamaan |
| **Manusia** | Kompetensi Tim | • Keahlian Laravel/PHP<br>• Desain basis data<br>• Keterampilan antarmuka<br>• Kemahiran Git | Tinggi | Kualitas kode, Kecepatan pengiriman |
| | Komitmen Pemangku Kepentingan | • Dukungan manajemen<br>• Keterlibatan aktif<br>• Umpan balik konstruktif<br>• Partisipasi UAT | Tinggi | Skor keterlibatan pemangku kepentingan |
| | Adopsi Pengguna | • Pelatihan memadai<br>• Panduan komprehensif<br>• Dukungan responsif<br>• Manajemen perubahan | Kritis | Tingkat adopsi ≥ 70% |
| **Manajemen Proyek** | Perencanaan Matang | • Ruang lingkup jelas<br>• Jadwal realistis (11 minggu)<br>• Sumber daya optimal<br>• Mitigasi risiko | Tinggi | Pengiriman tepat waktu, Kepatuhan anggaran |
| | Komunikasi Efektif | • Pertemuan mingguan<br>• Dokumentasi jelas<br>• Pelacakan kemajuan<br>• Penyelesaian masalah | Tinggi | Frekuensi komunikasi, Waktu respons |
| | Jaminan Kualitas | • Pengujian sistematis<br>• Tinjauan kode<br>• Pelacakan bug<br>• Perbaikan berkelanjutan | Kritis | Cakupan pengujian ≥ 70%, Kepadatan bug |
| **Bisnis** | Proposisi Nilai | • Nilai bisnis jelas<br>• ROI terukur<br>• Keunggulan kompetitif<br>• Keselarasan tujuan | Kritis | ROI ≥ 200%, Peningkatan efisiensi ≥ 40% |
| | Kesiapan Pasar | • Familiaritas digital<br>• Infrastruktur tersedia<br>• Dukungan regulasi<br>• Permintaan pasar | Sedang | Riset pasar, Survei pengguna |
| | Keberlanjutan Finansial | • Anggaran memadai<br>• Model pendapatan layak<br>• Efisiensi biaya<br>• Dana kontinjensi | Tinggi | Varians anggaran < 10%, Analisis titik impas |

**Prioritas FKK:**
- Kritis: 5 faktor (Stabilitas, Keamanan, Adopsi, Jaminan Kualitas, Nilai)
- Tinggi: 6 faktor (Antarmuka, Kompetensi, Komitmen, Perencanaan, Komunikasi, Finansial)
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

**Tabel 4.33 Faktor Kritis Keberhasilan (CSF) dengan Indikator**

| ID CSF | Faktor Kritis Keberhasilan | Indikator Keberhasilan | Nilai Target | Metode Pengukuran | Frekuensi Pemantauan | Risiko Jika Tidak Terpenuhi | Strategi Mitigasi |
|--------|---------------------------|------------------------|--------------|-------------------|----------------------|----------------------------|-------------------|
| CSF-01 | Ketersediaan & Keandalan Sistem | Waktu aktif sistem | ≥ 99,5% | Pemantauan UptimeRobot | Real-time (24/7) | Frustrasi pengguna, Kerugian pendapatan | • Hosting andal (SLA 99,9%)<br>• Pencadangan harian<br>• Peringatan pemantauan |
| | | Waktu respons | < 2 detik per halaman | GTmetrix, Lighthouse | Mingguan | Pengalaman pengguna buruk, *Bounce* tinggi | • Optimasi kueri<br>• *Caching* (Redis)<br>• Penggunaan CDN |
| | | Pengguna bersamaan | ≥ 100 pengguna | Uji beban (Apache JMeter) | Pra-peluncuran, Bulanan | Sistem *crash* | • Pengindeksan tepat<br>• *Connection pooling*<br>• Penskalaan horizontal |
| | | Integritas data | Tanpa kehilangan data | Audit basis data, Verifikasi cadangan | Harian | Kegagalan kritis | • Cadangan otomatis<br>• Manajemen transaksi<br>• Aturan validasi |
| CSF-02 | Keamanan & Privasi Data | Insiden pelanggaran data | Tanpa pelanggaran | Audit keamanan, Log insiden | Berkelanjutan | Tanggung jawab hukum (denda Rp 5M) | • Enkripsi (bcrypt, AES-256)<br>• HTTPS<br>• Audit keamanan |
| | | Cakupan enkripsi | 100% data sensitif | Tinjauan kode | Pra-penyebaran | Kehilangan kepercayaan, Gugatan | • Fitur keamanan Laravel<br>• Validasi input<br>• Kepatuhan OWASP |
| | | Implementasi RBAC | 100% fungsional | Pengujian akses | Mingguan | Akses tidak sah | • *Middleware* peran<br>• Gerbang izin<br>• Jejak audit |
| | | Kerentanan keamanan | Tanpa kritis/tinggi | Pemindaian OWASP ZAP | Dua mingguan | Risiko pelanggaran data | • Pembaruan rutin<br>• Uji penetrasi<br>• Perbaikan keamanan |
| CSF-03 | Adopsi & Kepuasan Pengguna | Tingkat adopsi klien | ≥ 70% | Analitik pemesanan | Bulanan | Kegagalan proyek | • Program pelatihan<br>• Panduan pengguna<br>• Sistem dukungan |
| | | Skor SUS | ≥ 68 (di atas rata-rata) | Kuesioner SUS (10 pengguna) | Pasca-UAT, Triwulanan | Kepuasan rendah | • Uji kegunaan<br>• Perbaikan iteratif<br>• Umpan balik pengguna |
| | | Kepuasan pengguna | ≥ 4,0/5,0 | Survei pasca-pemesanan | Per pemesanan | Ulasan negatif | • Dukungan responsif<br>• Perbaikan bug<br>• Permintaan fitur |
| | | Adopsi terapis | 100% (wajib) | Log penggunaan | Mingguan | Gangguan alur kerja | • Pelatihan wajib<br>• Penegakan admin<br>• Insentif |
| | | Tingkat pengguna kembali | ≥ 60% dalam 3 bulan | Analitik pengguna | Bulanan | Penggunaan sekali saja | • Pengingat email<br>• Program loyalitas<br>• Perbaikan pengalaman |
| CSF-04 | Integrasi dengan Proses Bisnis | Pemesanan via sistem | 100% (tanpa manual) | Pelacakan sumber pemesanan | Harian | Beban sistem ganda | • Kebijakan wajib<br>• Nonaktifkan proses manual<br>• Pelatihan |
| | | Pengurangan beban kerja admin | ≥ 50% | Studi pelacakan waktu | Perbandingan Sebelum/Sesudah | Tanpa peningkatan efisiensi | • Otomasi proses<br>• Optimasi alur kerja<br>• Distribusi peran |
| | | Pengurangan kesalahan pemesanan | ≥ 90% | Perbandingan log kesalahan | Bulanan | Inefisiensi berlanjut | • Aturan validasi<br>• Pemeriksaan konflik<br>• Antarmuka jelas |
| | | Waktu pembuatan laporan | ≤ 5 menit | Pengukuran waktu | Mingguan | Pengambilan keputusan lambat | • Indeks basis data<br>• Laporan ter-*cache*<br>• Optimasi kueri |
| CSF-05 | Kepatuhan Anggaran & Jadwal | Penyelesaian proyek | 11 minggu ± 1 minggu | Pelacakan jadwal proyek | Mingguan | Manfaat tertunda | • Waktu penyangga (10%)<br>• Manajemen risiko<br>• Pemantauan mingguan |
| | | Varians anggaran | ≤ 10% lebih | Pelacakan biaya | Bulanan | Pembatalan proyek | • Dana kontinjensi (20%)<br>• Kontrol biaya<br>• Alternatif gratis |
| | | Penyelesaian ruang lingkup | 95%+ kebutuhan | Daftar periksa kebutuhan | Per sprint | Sistem tidak dapat digunakan | • Prioritas MoSCoW<br>• Pembekuan ruang lingkup<br>• Kontrol perubahan |
| | | Insiden perluasan ruang lingkup | ≤ 3 perubahan besar | Log permintaan perubahan | Berkelanjutan | Penundaan jadwal | • Proses perubahan formal<br>• Analisis dampak<br>• Tunda ke Fase 2 |

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

**Tabel 4.34 Indikator Kinerja Utama (KPI) - Metrik Teknis**

| Kategori KPI | Nama KPI | Definisi | Nilai Target | Nilai Dasar (Saat Ini) | Metode Pengukuran | Alat Pengukuran | Frekuensi | Penanggung Jawab | Tindakan Jika Di Bawah Target |
|--------------|----------|----------|--------------|------------------------|-------------------|-----------------|-----------|------------------|-------------------------------|
| **Kinerja Sistem** | Waktu Aktif Sistem | Persentase waktu sistem beroperasi | ≥ 99,5% | T/A (Sistem baru) | (Total waktu aktif / Total waktu) × 100% | UptimeRobot, Pingdom | Waktu nyata, laporan bulanan | Tim DevOps | • Periksa log server<br>• Tingkatkan sumber daya<br>• Implementasi redundansi |
| | Waktu Respons Rata-rata | Waktu muat halaman rata-rata | ≤ 2 detik | T/A | Pengukuran waktu muat halaman | Google PageSpeed Insights, GTmetrix | Mingguan | Tim Backend | • Optimasi kueri<br>• Aktifkan *caching*<br>• Implementasi CDN |
| | Waktu Kueri Basis Data | Waktu eksekusi kueri basis data rata-rata | ≤ 100ms | T/A | Pelacakan waktu eksekusi kueri | Laravel Debugbar, MySQL slow query log | Mingguan | Admin Basis Data | • Tambah indeks<br>• Optimasi kueri<br>• *Tuning* basis data |
| | Tingkat Kesalahan | Persentase permintaan yang menghasilkan kesalahan | ≤ 0,5% | T/A | (Permintaan error / Total permintaan) × 100% | Log Laravel, Sentry | Harian | Tim *Full-stack* | • Debug kesalahan<br>• Perbaiki bug<br>• Tingkatkan penanganan error |
| | Kapasitas Pengguna Bersamaan | Pengguna simultan maksimum yang didukung | ≥ 100 pengguna | T/A | Simulasi uji beban | Apache JMeter, LoadRunner | Pra-peluncuran, Triwulanan | Tim DevOps | • Optimasi *connection pool*<br>• Tingkatkan infrastruktur<br>• Penyeimbangan beban |
| | Waktu Respons API | Waktu respons *endpoint* API rata-rata | ≤ 500ms | T/A | Pemantauan kinerja API | Postman, New Relic | Mingguan | Tim Backend | • Optimasi *endpoint*<br>• Kurangi ukuran *payload*<br>• Implementasi paginasi |
| **Keamanan Sistem** | Kerentanan Keamanan | Jumlah masalah keamanan teridentifikasi | 0 kritis, ≤ 2 tinggi | T/A | Pemindaian keamanan otomatis | OWASP ZAP, Nessus | Bulanan | Tim Keamanan | • Perbaiki kerentanan<br>• Perbarui dependensi<br>• Audit keamanan |
| | Insiden Pelanggaran Data | Jumlah kejadian akses data tidak sah | 0 insiden | T/A | Audit keamanan & log insiden | Jejak audit, IDS | Waktu nyata | Tim Keamanan | • Respons insiden<br>• Analisis forensik<br>• Perkuat keamanan |
| | Upaya Login Gagal | Persentase upaya login yang gagal | ≤ 5% | T/A | (Login gagal / Total upaya login) × 100% | Log autentikasi Laravel | Harian | Tim Keamanan | • Periksa *brute force*<br>• Implementasi CAPTCHA<br>• Pembatasan laju |
| | Validitas Sertifikat SSL | Status kedaluwarsa sertifikat SSL | Selalu valid (>30 hari) | T/A | Pemeriksaan kedaluwarsa sertifikat | SSL Labs, Let's Encrypt | Otomatis (peringatan) | Tim DevOps | • Perbarui sertifikat<br>• Penyiapan perpanjangan otomatis<br>• Cadangan sertifikat |
| | Kepatuhan Kekuatan Kata Sandi | Persentase pengguna dengan kata sandi kuat | ≥ 95% | T/A | Validasi kebijakan kata sandi | Validator kustom Laravel | Bulanan | Tim Backend | • Terapkan kebijakan<br>• Reset kata sandi<br>• Edukasi pengguna |
| **Kualitas Sistem** | Cakupan Uji Kode | Persentase kode yang tercakup pengujian | ≥ 70% | 65% | (Baris diuji / Total baris) × 100% | PHPUnit, Jest | Per *commit* | Tim Pengembangan | • Tulis lebih banyak tes<br>• Tingkatkan cakupan<br>• Pendekatan TDD |
| | Skor Kualitas Kode | Status gerbang kualitas SonarQube | Rating A | Rating B | Analisis kode statis | SonarQube, PHPStan | Per *commit* | Tim Pengembangan | • Refaktor kode<br>• Perbaiki *code smell*<br>• Ikuti standar |
| | Cakupan Dokumentasi | Persentase kode dengan dokumentasi | ≥ 80% | 50% | Analisis komentar dokumentasi | PHPDocumentor | Bulanan | Tim Pengembangan | • Tambah *docblock*<br>• Perbarui README<br>• Dokumentasi API |

**Ringkasan KPI Teknis:**
- Total KPI Teknis: 14
- Area Fokus: Kinerja (6), Keamanan (5), Kualitas (3)
- KPI Kritis: Waktu Aktif, Waktu Respons, Kerentanan Keamanan, Pelanggaran Data
- Alat Pengukuran: 12 alat (campuran gratis dan komersial)

---

**Tabel 4.35 Indikator Kinerja Utama (KPI) - Metrik Bisnis & Pengguna**

| Kategori KPI | Nama KPI | Definisi | Nilai Target | Nilai Dasar (Saat Ini) | Metode Pengukuran | Sumber Data | Frekuensi | Penanggung Jawab | Tindakan Jika Di Bawah Target |
|--------------|----------|----------|--------------|------------------------|-------------------|-------------|-----------|------------------|-------------------------------|
| **Adopsi Pengguna** | Total Pengguna Terdaftar | Jumlah kumulatif pengguna terdaftar | 200 dalam 3 bulan | 0 | COUNT(users) | Tabel users | Bulanan | Tim Pemasaran | • Kampanye pemasaran<br>• Program rujukan<br>• Iklan media sosial |
| | Pengguna Aktif (MAU) | Pengguna yang login 30 hari terakhir | 150 pengguna (75%) | T/A | COUNT(DISTINCT user_id) WHERE login >= NOW() - 30 hari | activity_logs | Bulanan | Tim Produk | • Email keterlibatan ulang<br>• Notifikasi push<br>• Sorotan fitur |
| | Tingkat Konversi Pemesanan | Persentase pemesanan dimulai yang diselesaikan | ≥ 60% | 40% (manual) | (Pemesanan selesai / Upaya pemesanan) × 100% | Tabel bookings | Mingguan | Tim Produk | • Sederhanakan alur<br>• Kurangi langkah<br>• Tingkatkan pengalaman |
| | Tingkat Utilisasi Terapis | Persentase slot terapis yang dipesan | ≥ 80% | 60% (manual) | (Slot dipesan / Slot tersedia) × 100% | bookings, availability | Mingguan | Tim Operasi | • Pemasaran ke klien<br>• Harga dinamis<br>• Optimasi jadwal |
| | Tingkat Retensi Pengguna (3 bulan) | Persentase pengguna kembali setelah 3 bulan | ≥ 60% | 35% (estimasi) | (Pengguna aktif bulan 4 / Pengguna baru bulan 1) × 100% | users, bookings | Triwulanan | Tim Produk | • Program loyalitas<br>• Pengingat email<br>• Personalisasi |
| | Pengguna Baru vs Kembali | Rasio pengguna baru terhadap pengguna kembali | 40:60 | 70:30 | Segmentasi pengguna berdasarkan first_booking_date | bookings | Bulanan | Tim Pemasaran | • Tingkatkan retensi<br>• Insentif rujukan<br>• Layanan berkualitas |
| **Transaksi** | Total Pemesanan per Bulan | Jumlah pemesanan diselesaikan per bulan | 100 pemesanan | 80 (manual) | COUNT(bookings) WHERE status = 'completed' | bookings | Bulanan | Tim Operasi | • Kampanye promosi<br>• Tambah terapis<br>• Perpanjang jam |
| | Tingkat Keberhasilan Pembayaran | Persentase pembayaran berhasil | ≥ 95% | 90% (manual) | (Pembayaran berhasil / Upaya pembayaran) × 100% | payments | Mingguan | Tim Keuangan | • Berbagai metode pembayaran<br>• Dukungan pembayaran<br>• Instruksi jelas |
| | Tingkat Pembatalan Pemesanan | Persentase pemesanan dibatalkan | ≤ 10% | 15% (manual) | (Pemesanan dibatalkan / Total pemesanan) × 100% | bookings | Bulanan | Tim Operasi | • Sistem pengingat<br>• Kebijakan pembatalan<br>• Kemudahan penjadwalan ulang |
| | Nilai Pemesanan Rata-rata | Pendapatan rata-rata per pemesanan | Rp 300.000 | Rp 250.000 | SUM(booking_amount) / COUNT(bookings) | payments | Bulanan | Tim Keuangan | • *Upsell* layanan<br>• Paket penawaran<br>• Sesi premium |
| | Pendapatan per Bulan | Total pendapatan bulanan dari pemesanan | Rp 30.000.000 | Rp 20.000.000 | SUM(amount) WHERE status = 'paid' | payments | Bulanan | Tim Keuangan | • Tingkatkan pemesanan<br>• Optimasi harga<br>• Layanan baru |
| | Pendapatan Rata-rata per Pengguna | Nilai seumur hidup per pengguna | Rp 900.000 | Rp 750.000 | SUM(payments) / COUNT(DISTINCT users) | payments | Triwulanan | Tim Keuangan | • Tingkatkan frekuensi<br>• Penjualan paket<br>• Keanggotaan |
| **Kepuasan Pelanggan** | Skor Kepuasan Pengguna | Rating kepuasan pasca-pemesanan rata-rata | ≥ 4,0/5,0 | 3,8/5,0 | AVG(satisfaction_rating) | feedback | Per pemesanan | Layanan Pelanggan | • Kumpulkan umpan balik<br>• Tingkatkan layanan<br>• Selesaikan masalah |
| | Skor Promotor Bersih (NPS) | Kemungkinan merekomendasikan (skala 0-10) | ≥ 30 | 15 (manual) | % Promotor (9-10) - % Pencela (0-6) | surveys | Triwulanan | Tim Pemasaran | • Tangani pencela<br>• Tingkatkan pengalaman<br>• Tonjolkan kekuatan |
| | Skala Kegunaan Sistem (SUS) | Skor kegunaan standar | ≥ 68 (di atas rata-rata) | T/A | Kuesioner SUS (10 pertanyaan) | Survei UAT | Pasca-UAT, Triwulanan | Tim Produk | • Uji kegunaan<br>• Perbaikan antarmuka<br>• Uji pengguna |
| | Rating Sesi Rata-rata | Rating sesi terapis rata-rata | ≥ 4,5/5,0 | 4,3/5,0 | AVG(session_rating) | session_notes | Per sesi | Tim Operasi | • Pelatihan terapis<br>• Kontrol kualitas<br>• Lingkaran umpan balik |
| | Tingkat Respons Umpan Balik | Persentase umpan balik pengguna yang ditangani | ≥ 90% | 60% | (Umpan balik direspons / Total umpan balik) × 100% | feedback | Mingguan | Layanan Pelanggan | • Tim khusus<br>• SLA untuk respons<br>• Respons otomatis |

**Ringkasan KPI Bisnis:**
- Total KPI Bisnis: 17
- Area Fokus: Adopsi (6), Transaksi (6), Kepuasan (5)
- Target Pendapatan: Rp 30 juta/bulan (peningkatan 50% dari nilai dasar)
- Target Pengguna: 200 pengguna dalam 3 bulan, utilisasi terapis 80%

---

**Tabel 4.36 Indikator Kinerja Utama (KPI) - Metrik Operasional**

| Kategori KPI | Nama KPI | Definisi | Nilai Target | Nilai Dasar (Saat Ini) | Metode Pengukuran | Sumber Data | Frekuensi | Penanggung Jawab | Tindakan Jika Di Bawah Target |
|--------------|----------|----------|--------------|------------------------|-------------------|-------------|-----------|------------------|-------------------------------|
| **Efisiensi Proses** | Waktu Pemesanan Rata-rata | Waktu dari mulai hingga selesai pemesanan | ≤ 3 menit | 12 menit (manual) | AVG(completion_time - start_time) | booking_logs | Mingguan | Tim Produk | • Sederhanakan alur<br>• Kurangi bidang<br>• Isi otomatis data |
| | Waktu Pemrosesan Pemesanan Admin | Waktu untuk memproses/menyetujui pemesanan | ≤ 5 menit | 15 menit (manual) | AVG(approval_time - submission_time) | bookings | Bulanan | Tim Operasi | • Otomasi persetujuan<br>• Alur kerja jelas<br>• Pelatihan admin |
| | Waktu Verifikasi Pembayaran | Waktu untuk memverifikasi dan konfirmasi pembayaran | ≤ 30 menit | 2-4 jam (manual) | AVG(verified_at - payment_at) | payments | Mingguan | Tim Keuangan | • Verifikasi otomatis<br>• *Payment gateway*<br>• Peringatan waktu nyata |
| | Waktu Pembuatan Laporan | Waktu untuk menghasilkan laporan bisnis | ≤ 5 menit | 2 jam (manual) | Pengukuran waktu | Sistem pelaporan | Bulanan | Tim TI | • Optimasi kueri<br>• Laporan ter-*cache*<br>• Pengindeksan lebih baik |
| | Penyelesaian Konflik Jadwal | Waktu untuk menyelesaikan konflik penjadwalan | ≤ 10 menit | 30-60 menit | AVG(resolution_time) | conflict_logs | Mingguan | Tim Operasi | • Deteksi otomatis<br>• Aturan jelas<br>• Antarmuka penyelesaian cepat |
| **Dukungan & Pemeliharaan** | Waktu Respons Dukungan Rata-rata | Waktu hingga respons pertama pada tiket dukungan | ≤ 2 jam | T/A | AVG(first_response_at - created_at) | support_tickets | Mingguan | Layanan Pelanggan | • Tambah staf<br>• Respons otomatis<br>• Basis pengetahuan |
| | Waktu Penyelesaian Tiket Dukungan | Waktu rata-rata untuk menutup tiket dukungan | ≤ 24 jam | T/A | AVG(resolved_at - created_at) | support_tickets | Mingguan | Layanan Pelanggan | • Pelatihan lebih baik<br>• Proses eskalasi<br>• FAQ/dokumentasi |
| | Tingkat Penyelesaian Kontak Pertama | Persentase diselesaikan dalam kontak pertama | ≥ 70% | T/A | (Diselesaikan dalam 1 kontak / Total tiket) × 100% | support_tickets | Bulanan | Layanan Pelanggan | • Tingkatkan pelatihan<br>• Alat lebih baik<br>• Basis pengetahuan |
| | Waktu Penyelesaian Bug Sistem | Waktu rata-rata untuk memperbaiki bug yang dilaporkan | ≤ 48 jam (kritis) | T/A | AVG(resolved_at - reported_at) berdasarkan prioritas | issue_tracker | Mingguan | Tim Pengembangan | • Prioritaskan bug<br>• Lebih banyak pengembang<br>• Pengujian lebih baik |
| **Utilisasi Sumber Daya** | Kapasitas Rata-rata Terapis | Sesi rata-rata per terapis per minggu | ≥ 20 sesi | 15 sesi | AVG(COUNT(sessions) per terapis) | bookings | Mingguan | Tim Operasi | • Pemasaran<br>• Optimasi ketersediaan<br>• Rekrut lebih banyak |
| | Pengurangan Beban Kerja Admin | Persentase pengurangan jam admin | ≥ 50% | 0% (nilai dasar) | (Jam lama - Jam baru) / Jam lama × 100% | Pelacakan waktu | Bulanan | Manajemen | • Lebih banyak otomasi<br>• Perbaikan proses<br>• Pelatihan |
| | Pertumbuhan Penyimpanan Basis Data | Tingkat pertumbuhan penyimpanan bulanan | ≤ 5% per bulan | T/A | (Ukuran saat ini - Ukuran bulan lalu) / Bulan lalu × 100% | Metrik basis data | Bulanan | Admin Basis Data | • Arsip data<br>• Bersihkan data lama<br>• Optimasi penyimpanan |
| | Tingkat Keberhasilan Pencadangan | Persentase pencadangan yang berhasil | 100% | T/A | (Pencadangan berhasil / Total upaya pencadangan) × 100% | Log pencadangan | Harian | Tim DevOps | • Perbaiki skrip pencadangan<br>• Periksa penyimpanan<br>• Sistem peringatan |
| **Inteligensi Bisnis** | Akurasi Laporan | Akurasi laporan otomatis vs manual | ≥ 99% | T/A | Audit manual sampel laporan | Audit laporan | Bulanan | Analis Data | • Perbaiki perhitungan<br>• Validasi logika<br>• Pemeriksaan kualitas data |
| | Waktu Muat Dasbor | Waktu untuk memuat dasbor utama | ≤ 3 detik | T/A | Pengukuran waktu muat halaman | Pemantau kinerja | Mingguan | Tim *Frontend* | • Optimasi kueri<br>• *Lazy loading*<br>• *Caching* |
| | Kesegaran Data | Usia maksimum data dalam laporan | ≤ 1 jam | T/A | Periksa stempel last_updated | Sistem pelaporan | Waktu nyata | Tim Data | • Kurangi interval refresh<br>• Pembaruan waktu nyata<br>• Berbasis peristiwa |

**Ringkasan KPI Operasional:**
- Total KPI Operasional: 16
- Area Fokus: Efisiensi Proses (5), Dukungan (4), Utilisasi Sumber Daya (4), Inteligensi Bisnis (3)
- Target Utama: Pengurangan waktu 75% (pemesanan), pengurangan beban kerja admin 50%
- Peningkatan Efisiensi: 12 menit → 3 menit (pemesanan), 2 jam → 5 menit (laporan)

---

**Strategi Dasbor & Pemantauan KPI:**

| Jenis Dasbor | Laju Penyegaran | Pengguna | Metrik Utama yang Ditampilkan |
|--------------|-----------------|----------|-------------------------------|
| Dasbor Eksekutif | Harian | Manajemen, Pemilik | Pendapatan, pemesanan, pertumbuhan pengguna, NPS, ROI |
| Dasbor Operasi | Waktu nyata | Admin, Tim Operasi | Pemesanan aktif, jadwal terapis, pembayaran tertunda, tiket dukungan |
| Dasbor Teknis | Waktu nyata | Tim TI, DevOps | Waktu aktif, waktu respons, tingkat kesalahan, beban server |
| Dasbor Pemasaran | Mingguan | Tim Pemasaran | Akuisisi pengguna, tingkat konversi, MAU, tingkat rujukan |
| Dasbor Keuangan | Harian | Tim Keuangan | Pendapatan, tingkat keberhasilan pembayaran, nilai pemesanan rata-rata, pembayaran tertunggak |

---

---

## 4.5 Keuntungan yang Diharapkan

Implementasi Sistem Informasi CUR-HEART diharapkan memberikan berbagai keuntungan bagi pemangku kepentingan yang terlibat.

### 4.5.1 Manfaat untuk CUR-HEART (Bisnis)

---

**Tabel 4.37 Analisis Manfaat - CUR-HEART (Organisasi)**

| Kategori Manfaat | Manfaat Spesifik | Sebelum Sistem (Nilai Dasar) | Setelah Sistem (Target) | Dampak Terukur | Kerangka Waktu | Metode Pengukuran | Nilai Strategis |
|------------------|-----------------|------------------------------|-------------------------|----------------|----------------|-------------------|-----------------|
| **Efisiensi Operasional** | Proses pemesanan otomatis | Pemesanan manual (10-15 menit/pemesanan) | Pemesanan otomatis (3 menit/pemesanan) | • Penghematan waktu: 12 menit × 100 pemesanan = 20 jam/bulan<br>• Penghematan biaya: Rp 500.000/bulan<br>• **Tahunan: Rp 6.000.000** | Segera | Pelacakan waktu, analisis biaya | TINGGI - Mengurangi beban admin, fokus pada tugas strategis |
| | Manajemen penjadwalan | 5 jam/minggu koordinasi | 1 jam/minggu koordinasi | • Penghematan waktu: 16 jam/bulan<br>• Utilisasi sumber daya lebih baik: 60% → 80%<br>• Penghematan biaya: Rp 400.000/bulan | Bulan 1 | Log waktu, tingkat utilisasi | TINGGI - Meningkatkan produktivitas terapis, mengurangi konflik |
| | Pelaporan otomatis | 2 jam/laporan manual | 5 menit otomatis | • Penghematan waktu: 8 jam/bulan<br>• Penghematan biaya: Rp 200.000/bulan<br>• **Tahunan: Rp 2.400.000** | Bulan 2 | Waktu pembuatan laporan | SEDANG - Memungkinkan keputusan berbasis data, wawasan lebih cepat |
| | Eliminasi pemesanan ganda | 2-3 insiden/bulan | 0 insiden | • Konflik dicegah: 100%<br>• Peningkatan kepuasan klien<br>• Tanpa biaya kompensasi | Segera | Log insiden | TINGGI - Melindungi reputasi, meningkatkan keandalan |
| | Pemrosesan pembayaran | Verifikasi manual (2-4 jam) | Otomatis (30 menit) | • Penghematan waktu: 10 jam/bulan<br>• Arus kas lebih cepat<br>• Pengurangan kesalahan: 90% | Bulan 1 | Waktu pemrosesan, tingkat kesalahan | SEDANG - Meningkatkan arus kas, mengurangi beban keuangan |
| **Pertumbuhan Pendapatan** | Peningkatan volume pemesanan | 80 pemesanan/bulan | 100 pemesanan/bulan (peningkatan 25%) | • Pendapatan tambahan: 20 × Rp 300.000<br>• **Rp 6 juta/bulan = Rp 72 juta/tahun** | Bulan 3-6 | Jumlah pemesanan, pelacakan pendapatan | KRITIS - Dampak pendapatan langsung, pertumbuhan bisnis |
| | Pengurangan tidak hadir | Tingkat tidak hadir 15% (12/bulan) | Tingkat tidak hadir 5% (4/bulan) | • Pencegahan tidak hadir: 8 pemesanan<br>• **Pendapatan yang dipulihkan: Rp 2,4 juta/bulan = Rp 28,8 juta/tahun** | Bulan 2 | Pelacakan tingkat tidak hadir | TINGGI - Memaksimalkan pendapatan dari kapasitas |
| | Peluang *upselling* | Visibilitas terbatas | Rekomendasi otomatis | • 20% memesan sesi tambahan<br>• 10% upgrade ke paket<br>• **Tambahan: Rp 5 juta/tahun** | Bulan 6 | Pelacakan konversi | SEDANG - Meningkatkan nilai seumur hidup pelanggan |
| | Perpanjangan jam layanan | 08:00-17:00 (9 jam) | Pemesanan 24/7 tersedia | • Tangkap pemesanan di luar jam: 15%<br>• **Tambahan: Rp 10 juta/tahun** | Segera | Analisis waktu pemesanan | TINGGI - Menangkap peluang yang hilang sebelumnya |
| **Kualitas & Layanan** | Pengambilan keputusan berbasis data | Analisis manual, tertunda | Dasbor waktu nyata | • Keputusan lebih cepat (hari → jam)<br>• Wawasan lebih baik<br>• Identifikasi tren | Bulan 2 | Waktu penyelesaian keputusan | TINGGI - Keunggulan kompetitif, perencanaan strategis |
| | Pemantauan kualitas layanan | Umpan balik terbatas (informal) | Umpan balik & rating sistematis | • Tangkapan umpan balik 100%<br>• Skor SUS: 68+<br>• NPS: 30+ | Bulan 3 | Tingkat respons survei, skor | TINGGI - Perbaikan berkelanjutan, jaminan kualitas |
| | Retensi klien | Tingkat kembali 35% (estimasi) | Tingkat kembali 60% (target) | • Peningkatan loyalitas<br>• Nilai seumur hidup lebih tinggi<br>• Pemasaran dari mulut ke mulut | Bulan 6 | Perhitungan tingkat retensi | KRITIS - Pertumbuhan bisnis berkelanjutan |
| | Reputasi merek | Hanya dari mulut ke mulut | Kehadiran digital + ulasan | • Citra profesional<br>• Ulasan online positif<br>• Bukti sosial | Bulan 3 | Ulasan online, rating | TINGGI - Posisi pasar, membangun kepercayaan |
| **Skalabilitas** | Ekspansi bisnis | Terbatas oleh kapasitas manual | Sistem digital skalabel | • Dukung pertumbuhan 5× tanpa penambahan staf proporsional<br>• Kesiapan multi-lokasi | Tahun 1-2 | Analisis kapasitas pertumbuhan | KRITIS - Strategi bisnis jangka panjang |
| | Kemampuan analitik data | Laporan Excel dasar | BI & analitik lanjutan | • Wawasan prediktif<br>• Pengenalan pola<br>• Pelacakan ROI | Bulan 3 | Penggunaan analitik, kualitas wawasan | SEDANG - Dukungan keputusan strategis |
| **Mitigasi Risiko** | Pencadangan & pemulihan data | Manual, tidak konsisten | Pencadangan harian otomatis | • Risiko kehilangan data nol<br>• Kelangsungan bisnis<br>• Pemulihan bencana siap | Segera | Tingkat keberhasilan pencadangan (100%) | TINGGI - Melindungi aset bisnis |
| | Kepatuhan & audit | Pencatatan manual | Jejak audit digital | • Pelaporan kepatuhan mudah<br>• Ketertelusuran penuh<br>• Perlindungan hukum | Segera | Kelengkapan jejak audit | SEDANG - Kepatuhan hukum & regulasi |
| **Penghematan Biaya** | Pengurangan beban kerja admin | 100% pemrosesan manual | Pengurangan beban kerja 50% | • Bebaskan 50% waktu admin<br>• Realokasi ke aktivitas pertumbuhan<br>• **Penghindaran biaya: Rp 10 juta/tahun** | Bulan 2 | Pelacakan beban kerja | TINGGI - Optimasi biaya operasional |
| | Biaya terkait kesalahan | Kesalahan manusia (typo, pemesanan ganda) | Validasi sistem | • Pengurangan kesalahan: 95%<br>• Biaya kompensasi: Rp 0<br>• Waktu layanan pelanggan: pengurangan 70% | Bulan 1 | Pelacakan insiden kesalahan | SEDANG - Melindungi margin, meningkatkan layanan |

**Total Manfaat Tahunan Terukur untuk CUR-HEART:**
- Peningkatan Pendapatan Langsung: Rp 115,8 juta/tahun (Rp 72 juta + Rp 28,8 juta + Rp 5 juta + Rp 10 juta)
- Penghematan Biaya: Rp 18,4 juta/tahun (Rp 6 juta + Rp 2,4 juta + Rp 10 juta)
- **TOTAL MANFAAT TAHUNAN: Rp 134,2 juta/tahun**
- **ROI atas Investasi (Rp 5 juta)**: 2.584% selama 1 tahun

**Manfaat Strategis Tidak Terukur:**
- Peningkatan reputasi merek dan posisi pasar
- Skalabilitas untuk pertumbuhan masa depan (ekspansi multi-lokasi)
- Kemampuan pengambilan keputusan berbasis data
- Keunggulan kompetitif dalam transformasi digital
- Peningkatan kepuasan klien dan terapis yang mengarah pada retensi

---

### 4.5.2 Manfaat untuk Klien

---

**Tabel 4.38 Analisis Manfaat - Klien (Pengguna Akhir)**

| Kategori Manfaat | Manfaat Spesifik | Titik Kesulitan yang Ditangani | Solusi yang Diberikan | Dampak bagi Pengguna | Proposisi Nilai | Metrik Kepuasan | Prioritas |
|------------------|-----------------|--------------------------------|----------------------|----------------------|------------------|-----------------|----------|
| **Kenyamanan & Aksesibilitas** | Ketersediaan pemesanan 24/7 | Terbatas pada jam kantor (08:00-17:00) | Pesan kapan saja, di mana saja via web | • Tidak perlu menunggu jam kantor<br>• Pesan saat waktu nyaman<br>• Konfirmasi instan | Fleksibilitas waktu, akses langsung | Tingkat penyelesaian pemesanan: 90% | KRITIS |
| | Tidak perlu telepon | Harus menelepon dan menunggu | Layanan mandiri pemesanan online | • Tidak menunggu telepon<br>• Hindari kekhawatiran telepon<br>• Dapat multitasking | Kenyamanan, otonomi | Preferensi pengguna: 85% lebih suka online | TINGGI |
| | Antarmuka ramah ponsel | Alternatif hanya desktop | Desain responsif, mengutamakan ponsel | • Pesan saat bepergian<br>• Cek janji temu di mana saja<br>• Akses cepat | Kenyamanan ponsel | Penggunaan ponsel: 70% dari pemesanan | TINGGI |
| | Penjadwalan ulang mudah | Koordinasi manual diperlukan | Jadwal ulang satu klik (sesuai kebijakan) | • Tidak bergantung pada admin<br>• Pembaruan langsung<br>• Tanpa penalti jika lebih awal | Fleksibilitas, kontrol | Kepuasan penjadwalan ulang: 4,5/5 | TINGGI |
| | Konfirmasi instan | Menunggu konfirmasi admin (2-4 jam) | Konfirmasi pemesanan waktu nyata | • Ketenangan pikiran<br>• Tanpa kekhawatiran menunggu<br>• Dapat merencanakan segera | Kepastian, kepercayaan | Kepuasan kecepatan konfirmasi: 4,8/5 | TINGGI |
| **Transparansi & Informasi** | Profil terapis | Informasi terbatas pra-pemesanan | Profil detail (pendidikan, spesialisasi, ulasan) | • Pilihan berdasar informasi<br>• Sesuai preferensi<br>• Bangun kepercayaan | Keyakinan, kepercayaan | Tingkat tampilan profil: 95% sebelum pesan | KRITIS |
| | Ketersediaan waktu nyata | Harus telepon untuk cek ketersediaan | Kalender visual dengan slot terbuka | • Lihat semua opsi sekaligus<br>• Bandingkan waktu<br>• Rencanakan fleksibel | Transparansi, efisiensi | Interaksi kalender: 90% pengguna | TINGGI |
| | Harga jelas | Harga ambigu, harus telepon | Harga transparan per layanan | • Tanpa kejutan<br>• Perencanaan anggaran<br>• Bandingkan opsi | Kejelasan finansial | Rating kejelasan harga: 4,6/5 | TINGGI |
| | Rating & ulasan terapis | Tanpa umpan balik sejawat tersedia | Sistem rating (1-5 bintang) + ulasan tertulis | • Bukti sosial<br>• Jaminan kualitas<br>• Bangun kepercayaan | Kepercayaan, validasi | Pengaruh ulasan: 80% baca sebelum pesan | TINGGI |
| | Deskripsi layanan | Info layanan samar | Detail layanan komprehensif | • Pahami apa yang diharapkan<br>• Pilih layanan tepat<br>• Hindari miskomunikasi | Kejelasan, manajemen ekspektasi | Rating kejelasan layanan: 4,4/5 | SEDANG |
| **Manajemen Layanan Mandiri** | Riwayat janji temu | Pencatatan manual | Rekaman digital semua pemesanan | • Tidak perlu mengingat<br>• Rujukan mudah<br>• Lacak frekuensi | Organisasi, kenyamanan | Penggunaan riwayat: 60% pengguna | SEDANG |
| | Akses catatan sesi | Tidak ada akses ke catatan | Lihat catatan sesi yang dibagikan | • Pahami kemajuan<br>• Ingat wawasan<br>• Kontinuitas | Transparansi, keterlibatan | Kepuasan akses catatan: 4,3/5 | SEDANG |
| | Riwayat pembayaran | Kwitansi manual | Rekaman pembayaran digital | • Keperluan pajak<br>• Pelacakan pengeluaran<br>• Penarikan mudah | Manajemen finansial | Penggunaan riwayat pembayaran: 70% pengguna | SEDANG |
| | Manajemen profil | Pengisian form berulang | Profil persisten dengan isi otomatis | • Hemat waktu<br>• Konsistensi<br>• Pembaruan mudah | Efisiensi | Tingkat pembaruan profil: 40% pengguna | RENDAH |
| **Kualitas Perawatan Lebih Baik** | Pelacakan kemajuan | Tidak ada visibilitas kemajuan | Grafik & metrik kemajuan visual | • Motivasi<br>• Lihat peningkatan<br>• Pencapaian tujuan | Keterlibatan, motivasi | Tingkat tampilan kemajuan: 50% pengguna | TINGGI |
| | Penetapan & pelacakan tujuan | Pelacakan tujuan informal | Manajemen tujuan terstruktur | • Objektif jelas<br>• Pelacakan milestone<br>• Perayaan pencapaian | Akuntabilitas, motivasi | Penggunaan tujuan: 40% pengguna | SEDANG |
| | Konsistensi terapi | Lupa memesan tindak lanjut | Sistem pengingat + pemesanan ulang mudah | • Hasil lebih baik<br>• Perawatan konsisten<br>• Pembentukan kebiasaan | Peningkatan kesehatan | Tingkat retensi: 60% → 75% | TINGGI |
| | Rekomendasi personal | Saran generik | Rekomendasi layanan berbasis AI | • Layanan relevan<br>• Hasil lebih baik<br>• Temukan opsi | Personalisasi | Penerimaan rekomendasi: 35% | SEDANG |
| **Komunikasi** | Perpesanan dalam aplikasi | Campuran telepon/WhatsApp | Perpesanan terpusat dengan terapis | • Semua komunikasi di satu tempat<br>• Komunikasi async<br>• Riwayat pesan | Kenyamanan, organisasi | Penggunaan perpesanan: 30% pengguna | SEDANG |
| | Pengingat otomatis | Pengingat manual atau tidak ada | Pengingat email + SMS (H-1, H-0) | • Tidak ada janji terlewat<br>• Persiapan tepat waktu<br>• Pengurangan tidak hadir | Keandalan | Efektivitas pengingat: 90% hadir setelah pengingat | TINGGI |
| | Akses dukungan | Telepon selama jam kantor | Tiket dukungan dalam aplikasi + FAQ | • Bantuan cepat<br>• FAQ layanan mandiri<br>• Lacak masalah | Dukungan, pemberdayaan | Kepuasan dukungan: 4,0/5 | SEDANG |
| **Privasi & Keamanan** | Privasi data | Penanganan data tidak pasti | Patuh GDPR, data terenkripsi | • Kepercayaan pada kerahasiaan<br>• Perlindungan hukum<br>• Ketenangan pikiran | Kepercayaan, keamanan | Rating kepercayaan privasi: 4,5/5 | KRITIS |
| | Pembayaran aman | Manual tunai/transfer | *Payment gateway* aman (SSL) | • Keamanan pembayaran<br>• Tidak ada risiko pencurian data<br>• Pengalaman profesional | Keamanan finansial | Rating kepercayaan pembayaran: 4,6/5 | TINGGI |
| **Penghematan Biaya** | Waktu hemat | Proses pemesanan 30-60 menit | Proses pemesanan 3-5 menit | • Hemat 25-55 menit per pemesanan<br>• Pengurangan biaya peluang | Nilai waktu | Kepuasan penghematan waktu: 4,7/5 | TINGGI |
| | Hemat biaya perjalanan | Kunjungan fisik untuk memesan | Pemesanan online | • Tanpa biaya transportasi<br>• Tanpa biaya parkir | Penghematan finansial | Apresiasi penghematan biaya: 4,2/5 | SEDANG |
| **Pengalaman Keseluruhan** | Kepuasan pengguna | Frustrasi dengan proses manual | Pengalaman digital mulus | • Interaksi menyenangkan<br>• Pengalaman modern<br>• Kepercayaan pada merek | Kebahagiaan keseluruhan | Target SUS: 68+ (di atas rata-rata) | KRITIS |
| | Kemungkinan kembali | Tingkat kembali 35% | Pengalaman ditingkatkan → retensi | • Loyalitas lebih tinggi<br>• Pemesanan berulang<br>• Nilai seumur hidup | Retensi | Target retensi: 60% | TINGGI |
| | Kemungkinan merekomendasikan | Pemasaran mulut ke mulut terbatas | Pengalaman positif → rujukan | • Peningkatan skor NPS<br>• Pertumbuhan organik<br>• Bukti sosial | Advokasi | Target NPS: 30+ | TINGGI |

**Ringkasan Manfaat Klien:**
- **Kenyamanan**: Layanan mandiri 24/7, ramah ponsel, konfirmasi instan, penjadwalan ulang mudah
- **Transparansi**: Profil terapis lengkap, ketersediaan waktu nyata, harga jelas, rating & ulasan
- **Kualitas**: Pelacakan kemajuan, manajemen tujuan, rekomendasi personal, perawatan konsisten
- **Komunikasi**: Perpesanan dalam aplikasi, pengingat otomatis, akses dukungan cepat
- **Kepercayaan**: Privasi data, pembayaran aman, pengalaman profesional
- **Penghematan**: Hemat waktu (25-55 menit/pemesanan), pengurangan biaya perjalanan

**Target Kepuasan Pengguna:**
- Kepuasan Keseluruhan: ≥ 4,0/5,0
- Skala Kegunaan Sistem (SUS): ≥ 68 (di atas rata-rata)
- Skor Promotor Bersih (NPS): ≥ 30
- Tingkat Retensi: 60% kembali dalam 3 bulan

---

### 4.5.3 Manfaat untuk Terapis

---

**Tabel 4.39 Analisis Manfaat - Terapis (Penyedia Layanan)**

| Kategori Manfaat | Manfaat Spesifik | Titik Kesulitan Saat Ini | Solusi Sistem | Dampak bagi Terapis | Penghematan Waktu/Biaya | Nilai Profesional | Prioritas |
|------------------|-----------------|--------------------------|---------------|---------------------|------------------------|-------------------|----------|
| **Manajemen Jadwal** | Pengaturan ketersediaan layanan mandiri | Koordinasi via grup WhatsApp | Atur jadwal mingguan berulang dalam sistem | • Otonomi penuh<br>• Pembaruan instan<br>• Tidak bergantung admin | Waktu: 2 jam/minggu → 30 menit/minggu<br>**Hemat: 1,5 jam/minggu = 6 jam/bulan** | Kontrol, fleksibilitas | KRITIS |
| | Manajemen cuti mudah | Beritahu admin, pemblokiran manual | Fitur blokir tanggal satu klik | • Kelola cuti sendiri<br>• Tanpa penundaan persetujuan<br>• Kalender visual | Waktu: 30 menit per permintaan cuti → 2 menit | Otonomi, kenyamanan | TINGGI |
| | Pencegahan konflik | Pemeriksaan konflik manual | Deteksi konflik otomatis | • Tanpa pemesanan ganda<br>• Tanpa pembatalan canggung<br>• Keandalan profesional | Penyelesaian konflik: 1 jam/insiden → 0 | Ketenangan pikiran, profesionalisme | KRITIS |
| | Integrasi kalender | Kalender pribadi/kerja terpisah | Ekspor .ics untuk sinkronisasi Google/Outlook | • Tampilan kalender terpadu<br>• Manajemen waktu lebih baik<br>• Tanpa janji terlewat | Manajemen kalender: 30 menit/minggu → 0 | Efisiensi, organisasi | SEDANG |
| | Perubahan mendadak | Telepon admin, harap terjangkau | Perbarui ketersediaan waktu nyata | • Fleksibilitas darurat<br>• Kontrol atas jadwal<br>• Komunikasi klien | Pemrosesan perubahan: 15 menit → 2 menit | Fleksibilitas, pengurangan stres | TINGGI |
| **Manajemen Klien** | Profil klien komprehensif | Info tersebar (WhatsApp, kertas) | Profil digital terpusat | • Riwayat klien lengkap di ujung jari<br>• Konteks lebih baik<br>• Sesi yang terinformasi | Pencarian profil: 10 menit → 30 detik | Kualitas perawatan lebih baik | TINGGI |
| | Akses riwayat sesi | Catatan manual, sulit ditemukan | Arsip digital yang dapat dicari | • Rujukan mudah<br>• Lacak kemajuan<br>• Kontinuitas perawatan | Pengambilan riwayat: 15 menit → 1 menit | Profesionalisme, kualitas perawatan | TINGGI |
| | Alat pelacakan kemajuan | Pelacakan manual, subjektif | Grafik visual, metrik, milestone | • Ukuran objektif<br>• Motivasi klien<br>• Bukti efektivitas | Analisis kemajuan: 30 menit/klien → 5 menit | Efektivitas klinis | TINGGI |
| | Komunikasi klien | Campuran telepon, WhatsApp, email | Perpesanan dalam aplikasi (terpusat) | • Semua pesan di satu tempat<br>• Riwayat pesan<br>• Saluran profesional | Waktu komunikasi: 2 jam/minggu → 1 jam/minggu | Organisasi, profesionalisme | SEDANG |
| **Dokumentasi & Admin** | Catatan sesi terstruktur | Catatan bebas, tidak konsisten | Formulir catatan sesi template | • Dokumentasi konsisten<br>• Tidak ada yang terlupa<br>• Rekaman profesional | Waktu pencatatan: Sama tapi kualitas lebih baik | Kualitas, kepatuhan | TINGGI |
| | Fungsi penyimpanan otomatis | Simpan manual, risiko kehilangan data | Penyimpanan otomatis setiap 30 detik | • Tanpa kehilangan data<br>• Ketenangan pikiran<br>• Fokus pada konten | Pemulihan dari kehilangan data: 0 insiden | Keandalan | SEDANG |
| | Catatan yang dapat dicari | Dokumen kertas/Word (sulit dicari) | Pencarian teks lengkap | • Pengambilan informasi cepat<br>• Pencarian pola<br>• Rujukan wawasan masa lalu | Waktu pencarian: 20 menit → 30 detik | Efisiensi | SEDANG |
| | Arsip digital | Penyimpanan fisik, degradasi | Penyimpanan permanen berbasis cloud | • Tidak pernah kehilangan rekaman<br>• Akses di mana saja<br>• Tanpa ruang fisik diperlukan | Biaya penyimpanan: Rp 0 (vs. pengarsipan) | Keamanan, aksesibilitas | SEDANG |
| | Koordinasi admin | 3 jam/minggu bolak-balik | Sistem layanan mandiri | • Tanpa menunggu admin<br>• Tindakan langsung<br>• Lebih sedikit gangguan | Koordinasi: 3 jam/minggu → 30 menit/minggu<br>**Hemat: 2,5 jam/minggu = 10 jam/bulan** | Otonomi, efisiensi | TINGGI |
| **Manajemen Keuangan** | Dasbor pendapatan waktu nyata | Tunggu laporan bulanan | Pelacakan pendapatan langsung | • Tahu pendapatan kapan saja<br>• Rencanakan keuangan<br>• Motivasi | Visibilitas finansial: langsung vs. bulanan | Transparansi finansial | TINGGI |
| | Rincian sesi | Perhitungan manual | Pendapatan rinci per sesi | • Verifikasi pembayaran<br>• Pahami sumber pendapatan<br>• Pelaporan pajak | Waktu perhitungan: 2 jam/bulan → 0 | Akurasi, kepercayaan | SEDANG |
| | Pelaporan pajak | Kompilasi laporan manual | Pembuatan laporan satu klik | • Kepatuhan pajak mudah<br>• Dokumentasi profesional<br>• Siap audit | Waktu persiapan pajak: 4 jam/tahun → 30 menit/tahun | Kepatuhan, kenyamanan | SEDANG |
| | Transparansi pembayaran | Status pembayaran tidak jelas | Pelacakan pembayaran waktu nyata | • Tahu kapan dibayar<br>• Lacak pembayaran tertunda<br>• Perencanaan arus kas | Pertanyaan pembayaran: 30 menit/bulan → 0 | Kepercayaan, kejelasan | TINGGI |
| **Analitik Kinerja** | Statistik sesi | Tidak ada visibilitas kinerja | Dasbor analitik (volume, tingkat, dll.) | • Kesadaran diri<br>• Penetapan tujuan<br>• Peningkatan kinerja | Analisis: Tidak tersedia → Waktu nyata | Pertumbuhan profesional | SEDANG |
| | Skor kepuasan klien | Tidak ada umpan balik formal | Sistem rating & ulasan | • Tahu kekuatan<br>• Identifikasi kelemahan<br>• Tingkatkan layanan | Pengumpulan umpan balik: Ad-hoc → Sistematis | Peningkatan kualitas | TINGGI |
| | Pelacakan tingkat utilisasi | Penggunaan kapasitas tidak diketahui | Metrik persentase utilisasi | • Optimasi ketersediaan<br>• Seimbangkan beban kerja<br>• Maksimalkan pendapatan | Perencanaan kapasitas: Tidak tersedia → Berbasis data | Optimasi bisnis | SEDANG |
| | Pembandingan | Tidak ada perbandingan dengan sejawat | Perbandingan sejawat anonim | • Standar industri<br>• Posisi kompetitif<br>• Motivasi | Pembandingan: Tidak tersedia → Diaktifkan | Kesadaran pasar | RENDAH |
| **Pengembangan Profesional** | Pelacakan hasil klien | Penilaian subjektif | Ukuran hasil berbasis data | • Praktik berbasis bukti<br>• Efektivitas pengobatan<br>• Perbaikan berkelanjutan | Analisis hasil: Kualitatif → Kuantitatif | Keunggulan klinis | TINGGI |
| | Wawasan peningkatan layanan | Tebakan tentang apa yang berhasil | Pengenalan pola, analitik | • Identifikasi pendekatan sukses<br>• Replikasi praktik terbaik<br>• Personalisasi pengobatan | Pembuatan wawasan: Tidak tersedia → Otomatis | Optimasi pengobatan | SEDANG |
| | Pembuatan portofolio | Dokumentasi terbatas | Portofolio digital (sertifikasi, ulasan, statistik) | • Kredibilitas profesional<br>• Kemajuan karir<br>• Materi pemasaran | Pembuatan portofolio: 10 jam → Otomatis | Pertumbuhan karir | SEDANG |
| **Keseimbangan Kerja-Hidup** | Penjadwalan fleksibel | Jadwal manual kaku | Ketersediaan yang dikelola sendiri | • Kontrol jam kerja<br>• Seimbangkan kehidupan pribadi<br>• Cegah kelelahan | Keseimbangan kerja-hidup: Meningkat signifikan | Kesejahteraan, kepuasan | KRITIS |
| | Pengurangan beban admin | 5-6 jam/minggu tugas admin | 1-2 jam/minggu tugas admin | • Lebih banyak waktu untuk terapi<br>• Atau waktu pribadi<br>• Fokus lebih baik | **Total waktu dibebaskan: 4 jam/minggu = 16 jam/bulan** | Kualitas hidup | KRITIS |
| | Manajemen jadwal jarak jauh | Tatap muka atau telepon admin | Kelola via aplikasi ponsel di mana saja | • Fleksibilitas<br>• Manajemen liburan<br>• Perubahan darurat | Aksesibilitas: 24/7 vs. jam kantor | Kenyamanan | TINGGI |
| **Potensi Pendapatan** | Peningkatan pemesanan | Utilisasi 60%, penjadwalan manual | Utilisasi 80%, penjadwalan dioptimalkan | • Lebih banyak sesi<br>• Pendapatan lebih tinggi<br>• Penggunaan kapasitas lebih baik | Pendapatan: +33% (12 → 16 sesi/minggu)<br>**Contoh: Rp 15 juta → Rp 20 juta/bulan** | Pertumbuhan finansial | KRITIS |
| | Pengurangan tidak hadir | Tingkat tidak hadir 15% | Tingkat tidak hadir 5% (sistem pengingat) | • Pendapatan lebih andal<br>• Lebih sedikit waktu terbuang<br>• Perencanaan lebih baik | Pengurangan tidak hadir: 10% → Hemat 1,5 sesi/minggu | Stabilitas pendapatan | TINGGI |
| | Peluang *upselling* | Visibilitas terbatas | Rekomendasi sistem ke klien | • Penjualan paket<br>• Sesi tambahan<br>• Nilai lebih tinggi | Keberhasilan *upsell*: Potensi pendapatan +15% | Diversifikasi pendapatan | SEDANG |

**Ringkasan Manfaat Terapis:**
- **Penghematan Waktu**: 16 jam/bulan dibebaskan (jadwal: 6 jam, koordinasi: 10 jam)
- **Potensi Pendapatan**: +33% melalui utilisasi lebih baik (60% → 80%) = peningkatan ~Rp 5 juta/bulan
- **Kualitas Profesional**: Dokumentasi lebih baik, wawasan berbasis data, pelacakan hasil
- **Keseimbangan Kerja-Hidup**: Otonomi, fleksibilitas, beban admin berkurang
- **Kejelasan Finansial**: Pendapatan waktu nyata, pembayaran transparan, pelaporan pajak mudah

**Total Nilai per Terapis:**
- Nilai waktu (16 jam @ Rp 250.000/jam): Rp 4.000.000/bulan dihemat
- Peningkatan pendapatan (utilisasi lebih baik): Rp 5.000.000/bulan
- **Total nilai bulanan: Rp 9.000.000/terapis**
- **Nilai tahunan: Rp 108.000.000/terapis**

**Target Kepuasan Terapis:**
- Kepuasan Keseluruhan: ≥ 4,5/5,0
- Kemudahan Penggunaan Sistem: ≥ 4,3/5,0
- Rekomendasi ke Terapis Lain: ≥ 80%
- Peningkatan Utilisasi: 60% → 80% (peningkatan 33%)

---

#### C. Keseimbangan Kerja-Hidup

**1. Penjadwalan Fleksibel**
- Kontrol atas ketersediaan
- Manajemen waktu libur yang mudah
- Mencegah kelebihan kerja (pengaturan sesi maksimal per hari)

**2. Beban Administratif Berkurang**
- Waktu koordinasi lebih sedikit
- Pengingat otomatis mengurangi ketidakhadiran
- Dokumentasi digital lebih cepat dari manual

---

### 4.5.4 Analisis *Return on Investment* (ROI)

---

**[GAMBAR 4.66 - Grafik Proyeksi ROI (5 Tahun)]** 📈
_Grafik proyeksi ROI 5 tahun menunjukkan pemulihan investasi, manfaat bersih, dan pengembalian kumulatif_

---

**Tabel 4.40 Perhitungan ROI - Analisis Tahun Pertama**

| Kategori Biaya/Manfaat | Item | Kuantitas/Tarif | Biaya Unit | Frekuensi | Jumlah Tahunan (Rp) | Metode Perhitungan | Catatan |
|-----------------------|-----------|---------------|-----------|-----------|-------------------|-------------------|-------|
| **INVESTASI AWAL (Tahun 0)** |
| Pengembangan | Sumber Daya Manusia | 3 orang × 11 minggu | Rp 0 | Sekali | 0 | Biaya peluang = 0 | Proyek *capstone* akademik |
| Infrastruktur | Nama domain (.id) | 1 domain | Rp 150.000 | Tahunan | 150.000 | 1 × Rp 150.000 | Registrasi TLD .id |
| | *Hosting* (VPS 2GB RAM, 50GB SSD) | 1 server | Rp 100.000 | Bulanan × 12 | 1.200.000 | Rp 100.000 × 12 | Niagahoster atau setara |
| | Sertifikat SSL | 1 sertifikat | Rp 0 | Tahunan | 0 | Gratis | Let's Encrypt |
| | Perangkat pengembangan | Berbagai | Rp 0 | Sekali | 0 | Gratis/*open source* | VS Code, Git, MySQL Workbench |
| Layanan Pihak Ketiga | Pengaturan *payment gateway* | 1 akun | Rp 0 | Sekali | 0 | Pengaturan gratis | Midtrans (biaya transaksi 2%) |
| | Layanan email (SMTP) | 500 email/hari | Rp 50.000 | Bulanan × 12 | 600.000 | Rp 50.000 × 12 | Mailtrap/SendGrid |
| | Penyimpanan *backup* (25GB) | 25GB cloud | Rp 50.000 | Bulanan × 12 | 600.000 | Rp 50.000 × 12 | Google Drive Business |
| Lain-lain | Perangkat pengujian | Tersedia | Rp 0 | Sekali | 0 | Gunakan perangkat tim | Desktop, laptop, mobile |
| | Materi pelatihan | Manual, video | Rp 200.000 | Sekali | 200.000 | Upaya dokumentasi | Panduan pengguna, video pelatihan |
| | Cadangan (10%) | Penyangga keamanan | 10% | Sekali | 200.000 | 10% dari (1,35M + 1,25M) | Mitigasi risiko |
| | **SUBTOTAL - INVESTASI AWAL** | | | | **3.000.000** | | **Biaya sekali bayar** |
| **BIAYA BERULANG TAHUNAN (Tahun 1)** |
| Infrastruktur | Perpanjangan domain | 1 domain | Rp 150.000 | Tahunan | 150.000 | 1 × Rp 150.000 | Perpanjangan tahunan |
| | *Hosting* | 1 server | Rp 100.000 | Bulanan × 12 | 1.200.000 | Rp 100.000 × 12 | Langganan bulanan |
| Layanan | Layanan email | 500 email/hari | Rp 50.000 | Bulanan × 12 | 600.000 | Rp 50.000 × 12 | Email transaksional |
| | Penyimpanan *backup* | 25GB | Rp 50.000 | Bulanan × 12 | 600.000 | Rp 50.000 × 12 | Cadangan harian |
| | Biaya *payment gateway* | 100 pemesanan @ Rp 300K | 2% | Bulanan × 12 | 7.200.000 | (100 × Rp 300K × 2%) × 12 | Berbasis transaksi |
| Pemeliharaan | Perbaikan bug & pembaruan | Ad-hoc | Rp 0 | Berkelanjutan | 0 | Kemampuan internal | Tim menangani pemeliharaan |
| | **SUBTOTAL - BIAYA BERULANG** | | | | **9.750.000** | | **Berulang tahunan** |
| | **TOTAL BIAYA TAHUN 1** | | | | **12.750.000** | | **Awal + Berulang** |
| **MANFAAT PENDAPATAN (Tahun 1)** |
| Pertumbuhan Pendapatan | Pemesanan tambahan | 20 lebih/bulan | Rp 300.000 | Bulanan × 12 | 72.000.000 | (100 - 80) × Rp 300K × 12 | Peningkatan volume 25% |
| | Pengurangan tidak hadir | 8 dicegah/bulan | Rp 300.000 | Bulanan × 12 | 28.800.000 | 8 × Rp 300K × 12 | Tingkat tidak hadir 15% → 5% |
| | *Upselling* (paket) | 5 upgrade/bulan | Rp 100.000 | Bulanan × 12 | 6.000.000 | 5 × Rp 100K × 12 | Tingkat upgrade 10% |
| | Pemesanan jam diperpanjang | 10 di luar jam/bulan | Rp 300.000 | Bulanan × 12 | 36.000.000 | 10 × Rp 300K × 12 | Tangkapan ketersediaan 24/7 |
| | **SUBTOTAL - PENINGKATAN PENDAPATAN** | | | | **142.800.000** | | **Dampak pendapatan langsung** |
| **PENGHEMATAN BIAYA (Tahun 1)** |
| Efisiensi Operasional | Penghematan waktu admin | 20 jam/bulan | Rp 25.000/jam | Bulanan × 12 | 6.000.000 | 20 × Rp 25K × 12 | Otomatisasi pemesanan |
| | Pengurangan waktu koordinasi | 16 jam/bulan | Rp 25.000/jam | Bulanan × 12 | 4.800.000 | 16 × Rp 25K × 12 | Penjadwalan terapis |
| | Penghematan waktu pelaporan | 8 jam/bulan | Rp 25.000/jam | Bulanan × 12 | 2.400.000 | 8 × Rp 25K × 12 | Laporan otomatis |
| | Resolusi kesalahan/konflik | 4 insiden/bulan | Rp 200.000 | Bulanan × 12 | 9.600.000 | 4 × Rp 200K × 12 | Pemesanan ganda dicegah |
| | Kertas & percetakan | Pengurangan 50% | Rp 100.000 | Bulanan × 12 | 600.000 | Rp 50K × 12 | Dokumentasi digital |
| | Waktu verifikasi pembayaran | 10 jam/bulan | Rp 25.000/jam | Bulanan × 12 | 3.000.000 | 10 × Rp 25K × 12 | Verifikasi otomatis |
| | **SUBTOTAL - PENGHEMATAN BIAYA** | | | | **26.400.000** | | **Efisiensi operasional** |
| | **TOTAL MANFAAT TAHUNAN** | | | | **169.200.000** | | **Pendapatan + Penghematan** |
| **MANFAAT BERSIH & ROI (Tahun 1)** |
| Manfaat Bersih | Total Manfaat - Total Biaya | | | | **156.450.000** | Rp 169,2M - Rp 12,75M | **Manfaat bersih tahunan** |
| ROI | (Manfaat Bersih / Total Investasi) × 100% | | | | **1.227%** | (Rp 156,45M / Rp 12,75M) × 100% | **ROI Luar Biasa** |
| Periode *Payback* | Total Investasi / Manfaat Bulanan | | | | **0,9 bulan** | Rp 12,75M / (Rp 169,2M / 12) | **~27 hari untuk impas** |

**Metrik Keuangan Kunci:**
- **Total Investasi Tahun 1**: Rp 12.750.000 (termasuk biaya awal + berulang)
- **Total Manfaat Tahun 1**: Rp 169.200.000 (peningkatan pendapatan + penghematan biaya)
- **Manfaat Bersih Tahun 1**: Rp 156.450.000
- **ROI**: 1.227% (pengembalian luar biasa)
- **Periode *Payback***: 27 hari (kurang dari 1 bulan)
- **Rasio Manfaat-Biaya**: 13,3:1 (untuk setiap Rp 1 diinvestasikan, menghasilkan Rp 13,3)

**Pendorong ROI:**
1. **Dampak Pendapatan Tinggi**: Rp 142,8M dari peningkatan pemesanan, pengurangan ketidakhadiran, *upselling*
2. **Penghematan Biaya Signifikan**: Rp 26,4M dari peningkatan efisiensi operasional
3. **Biaya Pengembangan Rendah**: Rp 0 (proyek akademik, tim internal)
4. **Biaya Berulang Moderat**: Rp 9,75M/tahun (infrastruktur + layanan)
5. ***Payback* Cepat**: Kurang dari 1 bulan untuk mengembalikan investasi

---

---

**[GAMBAR 4.67 - Grafik Analisis Biaya-Manfaat]** 📊
_Analisis komparatif total biaya vs total manfaat selama 5 tahun dengan visualisasi titik impas_

---

**Tabel 4.41 Proyeksi Analisis Biaya-Manfaat 5 Tahun**

| Tahun | Investasi Awal | Biaya Berulang Tahunan | Biaya *Payment Gateway* (2%) | Total Biaya Tahunan | Manfaat Pendapatan | Penghematan Biaya | Total Manfaat | Manfaat Bersih Tahunan | Manfaat Bersih Kumulatif | ROI Kumulatif | Catatan |
|------|-------------------|----------------------|---------------------------|------------------|------------------|--------------|----------------|-------------------|----------------------|---------------|-------|
| **0** | Rp 3.000.000 | Rp 0 | Rp 0 | **Rp 3.000.000** | Rp 0 | Rp 0 | **Rp 0** | **(Rp 3.000.000)** | **(Rp 3.000.000)** | **-100%** | Fase setup (Bulan 1-3) |
| **1** | Rp 0 | Rp 2.550.000 | Rp 7.200.000 | **Rp 9.750.000** | Rp 142.800.000 | Rp 26.400.000 | **Rp 169.200.000** | **Rp 159.450.000** | **Rp 156.450.000** | **1.218%** | Operasi penuh (kapasitas 100%) |
| **2** | Rp 0 | Rp 2.627.000 | Rp 7.992.000 | **Rp 10.619.000** | Rp 158.760.000 | Rp 27.720.000 | **Rp 186.480.000** | **Rp 175.861.000** | **Rp 332.311.000** | **2.506%** | Pertumbuhan +10%, Biaya +3% |
| **3** | Rp 0 | Rp 2.706.000 | Rp 8.871.600 | **Rp 11.577.600** | Rp 174.636.000 | Rp 29.106.000 | **Rp 203.742.000** | **Rp 192.164.400** | **Rp 524.475.400** | **3.947%** | Pertumbuhan berkelanjutan +10% |
| **4** | Rp 0 | Rp 2.787.000 | Rp 9.758.760 | **Rp 12.545.760** | Rp 192.099.600 | Rp 30.561.300 | **Rp 222.660.900** | **Rp 210.115.140** | **Rp 734.590.540** | **5.528%** | Ekspansi pasar +10% |
| **5** | Rp 0 | Rp 2.871.000 | Rp 10.734.636 | **Rp 13.605.636** | Rp 211.309.560 | Rp 32.089.365 | **Rp 243.398.925** | **Rp 229.793.289** | **Rp 964.383.829** | **7.258%** | Skala & optimisasi +10% |

**Ringkasan Kumulatif 5 Tahun:**
- **Total Investasi (5 tahun)**: Rp 60.098.000 (Rp 3M awal + Rp 57,098M berulang)
- **Total Manfaat (5 tahun)**: Rp 1.025.481.825 (pendapatan + penghematan)
- **Total Manfaat Bersih (5 tahun)**: Rp 964.383.829
- **Rata-rata Manfaat Bersih Tahunan**: Rp 192.876.766
- **ROI 5 Tahun**: 7.258%
- **Rasio Manfaat-Biaya Kumulatif**: 17,1:1

**Asumsi Proyeksi:**
1. **Pertumbuhan Pendapatan**: Peningkatan tahunan 10% (estimasi konservatif berdasarkan kurva adopsi pengguna)
2. **Inflasi Biaya**: Peningkatan tahunan 3% untuk *hosting*/infrastruktur
3. **Biaya *Payment Gateway***: 2% dari volume transaksi (berkembang dengan pendapatan)
4. **Volume Pemesanan**: 100/bulan Tahun 1 → 264/bulan Tahun 5 (pertumbuhan progresif)
5. **Tanpa Upgrade Sistem Besar**: Mengasumsikan *tech stack* saat ini tetap layak
6. **Kondisi Pasar**: Permintaan layanan kesehatan mental stabil

**Analisis Sensitivitas:**

| Skenario | Perubahan Pendapatan | Perubahan Biaya | ROI Tahun 1 | Manfaat Bersih Kumulatif 5 Tahun | Kelayakan |
|----------|---------------|-------------|-----------|----------------------|-------------|
| **Kasus Terbaik** (+20% pendapatan, -10% biaya) | +20% | -10% | 1.823% | Rp 1.276.909.180 | Luar biasa |
| **Kasus Dasar** (sesuai proyeksi) | 0% | 0% | 1.227% | Rp 964.383.829 | Sangat baik |
| **Konservatif** (-10% pendapatan, +10% biaya) | -10% | +10% | 988% | Rp 672.419.562 | Sangat baik |
| **Kasus Terburuk** (-20% pendapatan, +20% biaya) | -20% | +20% | 749% | Rp 380.455.295 | Tetap menguntungkan |

**Analisis Impas:**
- **Pemesanan Minimum yang Diperlukan** (Tahun 1): 14 pemesanan/bulan (vs. target 100/bulan)
- **Ambang Pendapatan**: Rp 4,2M/bulan (vs. proyeksi Rp 14,1M/bulan)
- **Margin Keamanan**: 86% penyangga (sistem menguntungkan bahkan pada 14% dari target)

**Wawasan Kunci:**
1. **ROI Luar Biasa**: Bahkan dalam skenario terburuk (ROI 749%), investasi sangat menguntungkan
2. ***Payback* Cepat**: Investasi awal dikembalikan dalam kurang dari 1 bulan
3. **Ekonomi Terukur**: Seiring pendapatan tumbuh, peningkatan biaya minimal (ekonomi skala)
4. **Risiko Rendah**: Impas hanya memerlukan 14% dari pemesanan target
5. **Nilai Jangka Panjang**: Manfaat bersih kumulatif 5 tahun sebesar Rp 964M dari investasi Rp 60M

**Rekomendasi**: **LANJUTKAN DENGAN IMPLEMENTASI**
- Analisis keuangan sangat mendukung pengembangan sistem
- Berbagai skenario mengkonfirmasi profitabilitas
- Risiko minimal dengan *payback* cepat dan margin keamanan tinggi
- Nilai strategis jangka panjang melampaui pengembalian keuangan

---

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

**[File ini mencakup 4.4 Faktor Penentu Keberhasilan dan 4.5 Keuntungan yang Diharapkan. Akan dilanjutkan dengan file terpisah untuk 4.6 dan 4.7]**
