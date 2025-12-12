# TUGAS MINGGU 5 – PERSIAPAN BAHAN & METODE ANALISIS

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Semester 7 Transfer**  
**Mata Kuliah: IT Governance & Audit**  
**Dosen Pengampu: Daniati Uki Eka Saputri, M.Kom**

---

## A. Identitas Tim

• **Nama Tim:** Kelompok X

• **Anggota & Peran:**
  - Roki Anjas (11250066) – Ketua Tim & Analis Data
  - Fahruroji (11250085) – PIC Wawancara & Dokumentasi
  - Susanto (11250068) – Analis Risiko & Penyusun Laporan

• **Kontak:** kelompokx@students.nusamandiri.ac.id

---

## B. Ringkasan Konteks & Tujuan

### Konteks
SATRIAMART adalah perusahaan retail yang bergerak di bidang dekorasi dan aksesoris akrilik dengan produk unggulan meliputi nomor rumah akrilik, signage akrilik, papan nama akrilik, dan aksesoris dekorasi custom. Perusahaan saat ini menghadapi tantangan dalam pengelolaan teknologi informasi yang efektif untuk mendukung pertumbuhan bisnis. Berdasarkan penilaian awal, tingkat kematangan (*maturity level*) tata kelola TI SATRIAMART berada pada level 1.2 dari skala 5 (*ad-hoc*/*initial*), dimana proses TI belum terdokumentasi dengan baik dan masih bersifat reaktif.

### Tujuan Terukur (SMART)
Meningkatkan tingkat kematangan tata kelola TI SATRIAMART dari level *ad-hoc* (1.2) menjadi level *managed* (3.0) dalam periode 18-24 bulan melalui implementasi framework COBIT 2019, dengan fokus pada penurunan insiden TI sebesar 60%, peningkatan keselarasan strategi TI-bisnis sebesar 75%, dan optimalisasi penggunaan sumber daya TI sebesar 40%.

---

## C. Ruang Lingkup & Framework

• **Domain Proses:**
  - EDM03 (Ensure Risk Optimisation) – Manajemen Risiko TI
  - APO12 (Manage Risk) – Pengelolaan Risiko Operasional

• **Framework Acuan:**
  - COBIT 2019 sebagai framework utama
  - ISO/IEC 27001 (untuk kontrol keamanan informasi)
  - ITIL 4 (untuk manajemen layanan TI)

• **Asumsi & Batasan:**
  - Data historis tersedia untuk periode 6 bulan terakhir (Mei–Oktober 2025)
  - Akses wawancara dengan minimal 3 narasumber kunci (Direktur, Manager TI, Staff Operasional)
  - Fokus pada proses kritis: manajemen risiko, manajemen perubahan, dan kontrol akses
  - Data yang digunakan merupakan data nyata dari SATRIAMART yang telah dianonimisasi
  - Waktu pelaksanaan assessment: 4 minggu (November–Desember 2025)

---

## D. Matriks Tujuan ↔ Data ↔ Metode (Traceability)

| Tujuan | Data/Bahan | Alasan Relevansi | Metode | Output Diharapkan |
|--------|------------|------------------|---------|-------------------|
| Meningkatkan maturity level dari 1.2 ke 3.0 | Dokumentasi SOP TI, Risk Register, Log Insiden 6 bulan | Menggambarkan kondisi tata kelola saat ini dan mengidentifikasi kesenjangan | Maturity Assessment COBIT 2019 & Gap Analysis | Skor maturity per domain, daftar gap, prioritas perbaikan |
| Menurunkan insiden TI sebesar 60% | Log insiden TI, Laporan downtime, Dokumentasi penanganan masalah | Mengidentifikasi pola insiden dan akar masalah | Risk Assessment (ISO 27005) & Root Cause Analysis | Daftar risiko prioritas, rekomendasi mitigasi |
| Meningkatkan keselarasan TI-Bisnis 75% | Dokumen strategi bisnis, Rencana investasi TI, KPI bisnis dan TI | Mengevaluasi alignment strategi TI dengan tujuan bisnis | Pemetaan COBIT 2019 (EDM & APO) & Benchmark Control | Matriks alignment, gap keselarasan, rekomendasi perbaikan |
| Optimalisasi sumber daya TI 40% | Data anggaran TI, Utilisasi sistem, Inventaris aset TI | Menganalisis efisiensi penggunaan sumber daya | RACI Matrix & Process Walkthrough | Peta proses optimal, clarity peran, efisiensi biaya |

---

## E. Daftar Bahan/Data

| No | Nama Bahan | Sumber | Periode | Pemilik | Sensitivitas | Status Akses |
|----|------------|--------|---------|---------|--------------|--------------|
| 1 | Dokumen Kebijakan TI (jika ada) | Manajemen SATRIAMART | Versi terbaru 2025 | Direktur | Internal | Diminta |
| 2 | SOP Operasional TI | Tim TI | Versi 2025 | Manager TI | Internal | Diminta |
| 3 | Log Insiden & Downtime | Sistem Ticketing/Manual | Mei–Oktober 2025 | Staff TI | Internal | Siap |
| 4 | Risk Register (jika tersedia) | Manajemen | Q2-Q3 2025 | Manager TI | Internal-Confidential | Diminta |
| 5 | Data Backup & Recovery Log | Server/Cloud Storage | Mei–Oktober 2025 | Staff TI | Internal | Siap |
| 6 | Dokumentasi Kontrol Akses Pengguna | Sistem/Manual | Oktober 2025 | Staff TI | Internal-Confidential | Diminta |
| 7 | Laporan Anggaran & Investasi TI | Keuangan | Tahun 2025 | Direktur/Finance | Internal-Confidential | Diminta |
| 8 | Inventaris Aset TI | Database Aset | Oktober 2025 | Staff TI | Internal | Siap |
| 9 | Dokumen Strategi Bisnis | Manajemen | 2025-2027 | Direktur | Internal | Diminta |
| 10 | Struktur Organisasi & Job Description | SDM | 2025 | Manajemen | Internal | Diminta |

---

## F. Metode/Pendekatan Analisis

### Metode Utama
**Kombinasi Maturity Assessment COBIT 2019 dan Risk-Based Control Testing**

### Alasan Pemilihan
1. **Maturity Assessment** diperlukan untuk mengukur tingkat kematangan tata kelola TI saat ini (baseline level 1.2) dan memetakan target pencapaian (level 3.0)
2. **Risk Assessment** dipilih karena SATRIAMART menghadapi risiko signifikan terkait insiden TI, kehilangan data, dan downtime yang berdampak pada operasional bisnis
3. **Gap Analysis** dibutuhkan untuk mengidentifikasi kesenjangan antara kondisi eksisting dengan best practice COBIT 2019
4. Framework COBIT 2019 dipilih karena terbukti efektif untuk perusahaan retail skala menengah di Indonesia dan dapat disesuaikan dengan karakteristik SATRIAMART

### Ruang Lingkup & Batasan
- Fokus pada domain EDM03 (Ensure Risk Optimisation) dan APO12 (Manage Risk)
- Mencakup proses-proses kritis: manajemen risiko TI, change management, access control, backup & recovery
- Periode analisis: data 6 bulan terakhir (Mei–Oktober 2025)
- Batasan: tidak mencakup audit teknis infrastruktur mendalam atau penetration testing

### Langkah Analisis Tingkat Tinggi
1. **Persiapan:** Pengumpulan dokumen dan data, persiapan instrumen assessment
2. **Penilaian Maturity:** Evaluasi capability level untuk setiap proses pada domain EDM03 dan APO12 menggunakan rating scale COBIT 2019 (0-5)
3. **Risk Assessment:** Identifikasi aset kritis, ancaman, kerentanan, dan penilaian risiko menggunakan matriks dampak-probabilitas
4. **Gap Analysis:** Membandingkan kondisi saat ini dengan target maturity level dan best practice
5. **Validasi:** Triangulasi data melalui wawancara, review dokumen, dan observasi proses
6. **Rekomendasi:** Menyusun prioritas perbaikan dan roadmap implementasi

---

## G. Rencana Uji Kontrol (ITGC/ITAC)

| Kontrol | Tujuan Kontrol | Populasi | Metode Sampling | Langkah Uji | Bukti | Hasil yang Diharapkan |
|---------|----------------|----------|-----------------|-------------|-------|----------------------|
| Manajemen Perubahan Sistem | Memastikan setiap perubahan sistem disetujui dan didokumentasi | Seluruh perubahan sistem Mei–Oktober 2025 (estimasi 30-50 perubahan) | Purposive sampling: 15 sampel mencakup perubahan kritis dan non-kritis | 1) Identifikasi daftar perubahan<br>2) Verifikasi approval<br>3) Cek dokumentasi<br>4) Validasi testing | Email approval, Change log, Dokumentasi testing | ≥80% perubahan memiliki approval formal dan dokumentasi lengkap |
| Kontrol Akses Pengguna | Memastikan hanya pengguna berwenang yang memiliki akses ke sistem kritis | Seluruh akun pengguna aktif (estimasi 15-25 user) | Census (100% population) | 1) Review daftar user<br>2) Verifikasi otorisasi<br>3) Cek segregation of duties<br>4) Validasi review berkala | User access list, Approval form, Access review log | ≥90% akun memiliki otorisasi valid dan SoD terpenuhi |
| Backup & Recovery | Memastikan data kritis di-backup secara berkala dan dapat di-restore | Semua aktivitas backup Mei–Oktober 2025 (estimasi 180 backup) | Stratified random: 20 sampel (10 harian, 10 mingguan) | 1) Review backup log<br>2) Verifikasi jadwal backup<br>3) Uji restore sampling<br>4) Cek offsite storage | Backup log, Restore test result, Storage record | ≥95% backup berhasil dan minimal 80% dapat di-restore dengan baik |
| Penanganan Insiden TI | Memastikan insiden TI ditangani sesuai SOP dan didokumentasi | Seluruh insiden TI Mei–Oktober 2025 (estimasi 40-60 insiden) | Random sampling: 20 sampel | 1) Review log insiden<br>2) Verifikasi response time<br>3) Cek root cause analysis<br>4) Validasi lesson learned | Incident ticket, Resolution log, RCA document | ≥70% insiden ditangani sesuai SLA dan memiliki dokumentasi lengkap |

---

## H. Risk Assessment

| Aset/Proses | Ancaman | Kerentanan | Dampak | Kemungkinan | Skor Risiko | Perlakuan |
|-------------|---------|------------|--------|-------------|-------------|-----------|
| Sistem E-commerce SATRIAMART | Serangan siber (hacking, DDoS) | Tidak ada firewall memadai, password lemah | Tinggi (kehilangan data pelanggan, reputasi) | Sedang | **Tinggi** | Implementasi firewall, kebijakan password kuat, MFA |
| Database Pelanggan & Transaksi | Kehilangan/kerusakan data | Backup tidak teratur, tidak ada disaster recovery plan | Sangat Tinggi (hilang data bisnis kritis) | Tinggi | **Kritis** | Otomasi backup harian, implementasi DRP, offsite storage |
| Proses Perubahan Sistem | Perubahan tidak terkontrol | Tidak ada prosedur change management formal | Sedang-Tinggi (downtime, error sistem) | Tinggi | **Tinggi** | Buat SOP change management, approval workflow, testing mandatory |
| Akses Sistem Internal | Akses tidak sah/abuse of privilege | Tidak ada review akses berkala, SoD lemah | Sedang (data breach internal, fraud) | Sedang | **Sedang** | Implementasi access review berkala, strengthening SoD, monitoring log |
| Infrastruktur Server | Downtime hardware/software | Single point of failure, maintenance kurang | Tinggi (gangguan operasional) | Sedang-Tinggi | **Tinggi** | Redundancy sistem kritis, preventive maintenance, monitoring 24/7 |

---

## I. Maturity/Capability Scoring

| Proses | Atribut | Level Saat Ini | Bukti | Target | Gap | Catatan |
|--------|---------|----------------|-------|--------|-----|---------|
| EDM03.01 (Evaluate Risk Management) | PA1-PA2 | 1 (Performed - incomplete) | Risk management dilakukan ad-hoc, tidak ada framework formal | 3 (Established) | 2 | Butuh risk register formal, risk assessment berkala |
| EDM03.02 (Direct Risk Management) | PA1-PA2 | 1 (Performed - incomplete) | Keputusan risiko tidak terdokumentasi formal | 3 (Established) | 2 | Perlu risk committee, approval workflow risk treatment |
| APO12.01 (Collect Data) | PA1-PA3 | 1 (Performed - incomplete) | Data risiko dikumpulkan tidak terstruktur | 3 (Established) | 2 | Implementasi risk data repository, standardisasi format |
| APO12.02 (Analyse Risk) | PA1-PA3 | 1 (Performed - incomplete) | Analisis risiko subjektif, tidak ada metode baku | 3 (Established) | 2 | Adopsi risk assessment methodology (ISO 27005), tools analisis |
| APO12.03 (Maintain Risk Profile) | PA1-PA3 | 0-1 (Not achieved/incomplete) | Tidak ada risk profile terdokumentasi | 3 (Established) | 2-3 | Buat risk profile organisasi, update berkala |
| APO12.04 (Articulate Risk) | PA1-PA2 | 1 (Performed - incomplete) | Komunikasi risiko tidak terstruktur | 3 (Established) | 2 | Risk reporting dashboard, stakeholder communication plan |
| APO12.05 (Define Risk Management Action Portfolio) | PA1-PA3 | 1 (Performed - incomplete) | Risk treatment tidak terprioritisasi | 3 (Established) | 2 | Risk treatment roadmap, resource allocation, monitoring |

**Rata-rata Maturity Level Saat Ini:** 1.0 (Initial/Ad-hoc)  
**Target Maturity Level:** 3.0 (Established/Managed)  
**Gap Maturity:** 2.0 level

---

## J. RACI & Timeline

### RACI Matrix

| Aktivitas | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|-----------|----------------|-----------------|---------------|--------------|
| Pengumpulan dokumen & data | Susanto | Roki Anjas | Manager TI, Staff TI | Direktur |
| Wawancara narasumber | Fahruroji | Roki Anjas | Direktur, Manager TI | Tim |
| Maturity assessment | Roki Anjas | Roki Anjas | Fahruroji, Susanto | Manager TI |
| Risk assessment | Susanto | Roki Anjas | Manager TI | Direktur |
| Gap analysis & uji kontrol | Roki Anjas, Susanto | Roki Anjas | Staff TI | Manager TI |
| Penyusunan rekomendasi | Tim (All) | Roki Anjas | Manager TI, Direktur | — |
| Review & validasi | Fahruroji | Roki Anjas | Dosen Pembimbing | — |
| Finalisasi laporan | Susanto | Roki Anjas | Tim | Dosen, Manajemen |

### Timeline Mingguan

| Minggu | Periode | Aktivitas Kunci | Ketergantungan | PIC Utama |
|--------|---------|-----------------|----------------|-----------|
| 1 | 4-10 Nov 2025 | - Persiapan instrumen assessment<br>- Pengajuan akses data & izin wawancara<br>- Pengumpulan dokumen awal (SOP, struktur organisasi) | Approval akses dari Direktur SATRIAMART | Roki Anjas, Susanto |
| 2 | 11-17 Nov 2025 | - Pengumpulan data lengkap (log insiden, backup, anggaran)<br>- Wawancara Direktur & Manager TI<br>- Review dokumentasi kebijakan TI | Ketersediaan narasumber | Fahruroji, Susanto |
| 3 | 18-24 Nov 2025 | - Maturity assessment domain EDM03 & APO12<br>- Risk assessment & identifikasi kontrol<br>- Sampling data untuk uji kontrol | Data lengkap dari minggu 2 | Roki Anjas, Susanto |
| 4 | 25 Nov-1 Des 2025 | - Uji kontrol (change management, access control, backup)<br>- Gap analysis & validasi temuan<br>- Penyusunan draft rekomendasi & roadmap | Hasil assessment minggu 3 | Tim (All) |
| 5 | 2-8 Des 2025 | - Validasi & triangulasi data<br>- Finalisasi laporan persiapan analisis<br>- Presentasi ke manajemen SATRIAMART (opsional) | Draft laporan selesai | Roki Anjas, Fahruroji |

---

## K. Validasi & Etika Data

### Triangulasi Sumber
Untuk memastikan validitas dan reliabilitas data, tim akan melakukan triangulasi melalui tiga pendekatan:
1. **Triangulasi Dokumen:** Membandingkan SOP ↔ Log Aktual ↔ Risk Register untuk memastikan konsistensi
2. **Triangulasi Metode:** Kombinasi wawancara mendalam, review dokumentasi, dan observasi langsung proses operasional
3. **Triangulasi Narasumber:** Validasi informasi dari tiga level: Direktur (strategic), Manager TI (tactical), Staff TI (operational)

### Anonimisasi & Privasi
- Semua data sensitif (informasi pelanggan, data keuangan detail, kredensial akses) akan dianonimisasi dengan masking/pseudonym
- Data pribadi karyawan akan menggunakan kode (mis. User A, User B) tanpa menyebut nama asli
- Informasi strategis bisnis yang bersifat rahasia akan disamarkan atau digeneralisasi dalam laporan final
- Dokumentasi akan mematuhi prinsip data minimization (hanya data relevan yang dikumpulkan)

### Izin & Batas Penggunaan Data
- Surat permohonan izin formal akan diajukan ke Direktur SATRIAMART sebelum pengumpulan data
- Data hanya digunakan untuk keperluan akademis (tugas mata kuliah IT Governance & Audit)
- Tidak ada publikasi atau distribusi data ke pihak ketiga tanpa izin tertulis dari SATRIAMART
- Setelah proyek selesai, data sensitif akan dihapus/dikembalikan sesuai kesepakatan
- Laporan final yang diserahkan ke dosen sudah dalam bentuk ter-anonimisasi

### Informed Consent
- Setiap narasumber wawancara akan diberikan penjelasan tentang tujuan penelitian dan penggunaan data
- Narasumber memiliki hak untuk menolak menjawab pertanyaan tertentu atau menarik persetujuan
- Rekaman wawancara (jika ada) hanya dilakukan dengan izin eksplisit narasumber

---

## L. Risiko Proyek & Mitigasi

| Risiko | Dampak | Probabilitas | Mitigasi | PIC |
|--------|--------|--------------|----------|-----|
| Data/dokumentasi TI tidak lengkap atau tidak tersedia | Tinggi (analisis tidak komprehensif, kesimpulan bias) | Sedang-Tinggi | - Identifikasi gap data sejak awal<br>- Cari sumber alternatif (wawancara, observasi)<br>- Dokumentasikan keterbatasan dalam laporan | Susanto, Roki Anjas |
| Narasumber kunci tidak tersedia untuk wawancara (sibuk/berhalangan) | Sedang (data kualitatif terbatas) | Sedang | - Jadwal wawancara sejak minggu 1<br>- Siapkan daftar narasumber alternatif/deputy<br>- Opsi wawancara fleksibel (online/offline) | Fahruroji |
| Timeline proyek mundur karena approval akses data terlambat | Sedang-Tinggi (delay deliverable) | Sedang | - Submit request akses H-7 sebelum minggu 1<br>- Follow up berkala ke manajemen<br>- Siapkan contingency plan: mulai dengan data publik/existing | Roki Anjas |
| Temuan assessment sensitif dan tidak nyaman bagi manajemen | Sedang (resistensi, akses data dibatasi) | Sedang | - Komunikasi awal tentang tujuan improvement, bukan blame<br>- Jaga confidentiality temuan<br>- Fokus pada solusi konstruktif, bukan kritik | Roki Anjas, Tim |
| Keterbatasan expertise tim dalam metode assessment COBIT 2019 | Sedang (kualitas analisis kurang optimal) | Rendah-Sedang | - Studi mendalam framework COBIT 2019 sebelum assessment<br>- Konsultasi dengan dosen pembimbing<br>- Benchmarking dengan contoh kasus serupa | Tim (All) |
| Bias subjektivitas dalam penilaian maturity level | Sedang (skor tidak akurat) | Sedang | - Gunakan rating guide objective dari COBIT 2019<br>- Triangulasi data dari berbagai sumber<br>- Peer review antar anggota tim | Roki Anjas, Susanto |
| Data backup/log insiden dalam format tidak terstruktur sulit dianalisis | Sedang (effort analisis tinggi) | Tinggi | - Lakukan data cleaning & transformation<br>- Gunakan tools sederhana (Excel, script) untuk parsing<br>- Sampling fokus pada data berkualitas | Susanto |

---

## M. Lampiran (Opsional)

### Lampiran A: Daftar Pertanyaan Wawancara (Draft)

**Untuk Direktur:**
1. Bagaimana visi dan strategi bisnis SATRIAMART 3-5 tahun ke depan?
2. Apa harapan terhadap peran TI dalam mendukung pencapaian tujuan bisnis?
3. Bagaimana kebijakan manajemen terkait investasi dan risiko TI?
4. Apakah pernah terjadi insiden TI yang berdampak signifikan pada bisnis?

**Untuk Manager TI:**
1. Bagaimana struktur dan tata kelola TI saat ini di SATRIAMART?
2. Apa saja proses TI utama yang sudah berjalan? Apakah sudah terdokumentasi formal?
3. Bagaimana proses identifikasi dan pengelolaan risiko TI dilakukan?
4. Apa tantangan utama dalam mengelola TI di SATRIAMART?
5. Apakah ada KPI atau metrik untuk mengukur kinerja TI?

**Untuk Staff TI/Operasional:**
1. Bagaimana prosedur penanganan insiden TI sehari-hari?
2. Apakah ada SOP untuk perubahan sistem, backup data, atau kontrol akses?
3. Seberapa sering terjadi downtime atau masalah TI? Apa penyebab utamanya?
4. Bagaimana koordinasi dengan unit bisnis lain terkait kebutuhan TI?

### Lampiran B: Contoh Risk Register (Template)

| Risk ID | Kategori | Deskripsi Risiko | Aset Terkait | Ancaman | Kerentanan | Dampak (1-5) | Probabilitas (1-5) | Skor Risiko | Risk Owner | Risk Treatment | Status |
|---------|----------|------------------|--------------|---------|------------|--------------|-------------------|-------------|------------|----------------|--------|
| R001 | Security | Data breach pelanggan | Database Customer | Hacking, Insider Threat | Weak access control | 5 | 3 | 15 (High) | Manager TI | Implement MFA, access review | Open |
| R002 | Operational | Kehilangan data kritis | Server & Storage | Hardware failure, Human error | No backup automation | 5 | 4 | 20 (Critical) | Manager TI | Daily auto-backup, DRP | Open |

---

## Format & Pengumpulan

• **Nama File:** 11.7C.12_KelompokX_PersiapanAnalisis_v1

• **Format:** PDF dan Markdown (MD), panjang 3–6 halaman inti (lampiran tidak dihitung)

• **Anggota Tim:**
  - Roki Anjas (11250066) – Ketua Tim & Analis Data
  - Fahruroji (11250085) – PIC Wawancara & Dokumentasi
  - Susanto (11250068) – Analis Risiko & Penyusun Laporan

• **Tanggal Pengumpulan:** [Sesuai jadwal dosen]

• **Lampiran:** Contoh log insiden (dianonimisasi), draft pertanyaan wawancara, template risk register

---

## Referensi

Afifah, U. F., Adam, S., & Marfuah. (2023). Pemetaan tata kelola teknologi informasi melalui desain faktor framework COBIT 2019 pada perusahaan manufaktur X. *STMSI*, 14(2), 630-641.

Agustriani, N. H. P. (2024). Analisis manajemen risiko teknologi informasi pada PT XYZ (perusahaan manufacturing) menggunakan framework COBIT 2019 dengan domain EDM03 dan APO12. *Journal of Information Technology and Software*, 1(2), 45-58.

ISACA. (2019). *COBIT 2019 Framework: Governance and management objectives*. ISACA.

ISO/IEC. (2018). *ISO/IEC 27005:2018 Information security risk management*. International Organization for Standardization.

IT Governance Institute. (2021). *Board briefing on IT governance* (3rd ed.). IT Governance Institute.

---

**Catatan Akhir:**  
Dokumen ini merupakan rencana persiapan analisis untuk proyek akhir IT Governance. Pelaksanaan akan disesuaikan dengan kondisi lapangan dan ketersediaan data dari SATRIAMART. Tim berkomitmen untuk menjaga confidentiality dan integritas data sesuai etika penelitian akademis.
