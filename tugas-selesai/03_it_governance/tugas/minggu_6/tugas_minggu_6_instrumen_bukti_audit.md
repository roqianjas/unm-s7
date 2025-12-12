# TUGAS MINGGU 6 – PERANCANGAN INSTRUMEN & BUKTI AUDIT

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Semester 7 Transfer**  
**Mata Kuliah: IT Governance**  
**Dosen Pengampu: Daniati Uki Eka Saputri, M.Kom**

---

## A. Identitas & Metadata

| Kelas | : | 11.7C.12 |  |
| :---- | :---- | :---- | :---- |
| Kelompok | : | 2 |  |
| Judul Proyek | : | Assessment dan Implementasi Framework Tata Kelola Teknologi Informasi pada SATRIAMART: Pendekatan COBIT 2019 |  |
| Organisasi/Objek | : | SATRIAMART (Perusahaan Retail Dekorasi dan Aksesoris Akrilik) |  |
| Anggota (Nama - NIM) | : | 1. Roki Anjas - 11250066<br>2. Fahruroji - 11250085<br>3. Susanto - 11250068 |  |
| Tanggal Submit | : | 9 November 2025 |  |

---

## B. Konteks & Lingkup Governance

### Tujuan Bisnis & Isu Utama

SATRIAMART adalah perusahaan retail yang bergerak di bidang dekorasi dan aksesoris akrilik dengan produk unggulan meliputi nomor rumah akrilik, signage akrilik, papan nama akrilik, dan aksesoris dekorasi custom. Isu utama yang dihadapi adalah tingkat kematangan tata kelola TI yang masih berada pada level 1.2 dari skala 5 (ad-hoc/initial), yang menimbulkan permasalahan kritis:

1. Ketidakselarasan antara strategi TI dengan strategi bisnis mengakibatkan investasi TI tidak optimal
2. Manajemen risiko TI yang belum terstruktur meningkatkan potensi kerugian akibat downtime, kehilangan data, atau pelanggaran keamanan
3. Penggunaan sumber daya TI yang tidak efisien menyebabkan pemborosan anggaran dan duplikasi fungsi sistem
4. Tidak adanya mekanisme monitoring dan evaluasi kinerja TI yang memadai

### Domain/Proses COBIT & Alasan Pemilihan

Berdasarkan analisis kebutuhan dan hasil systematic literature review, proyek ini memilih empat domain COBIT 2019:

**1. EDM03 (Ensure Risk Optimisation)**
- **Alasan:** Memastikan risiko TI dikelola secara optimal dan selaras dengan toleransi risiko organisasi
- **Relevansi:** SATRIAMART memerlukan framework manajemen risiko yang terstruktur untuk mengurangi potensi kerugian akibat insiden TI

**2. APO12 (Manage Risk)**
- **Alasan:** Mengelola risiko operasional TI secara kontinyu dengan identifikasi, penilaian, dan mitigasi yang sistematis
- **Relevansi:** Penelitian Agustriani (2024) membuktikan domain ini krusial untuk perusahaan manufaktur/retail di Indonesia

**3. DSS01 (Manage Operations)**
- **Alasan:** Memastikan operasi TI berjalan terkoordinasi dan terdokumentasi dengan baik
- **Relevansi:** Peningkatan dari proses reaktif (ad-hoc) menjadi proaktif dan terkelola (managed)

**4. MEA01 (Monitor, Evaluate and Assess Performance and Conformance)**
- **Alasan:** Menyediakan mekanisme monitoring dan evaluasi kinerja TI yang transparan
- **Relevansi:** Mendukung pengambilan keputusan strategis berbasis data dan KPI yang terukur

### Struktur Governance & Kebijakan Terkait

**Struktur Governance SATRIAMART:**
- **Level Strategis:** Direktur (pemilik strategi bisnis dan persetujuan investasi TI)
- **Level Taktis:** Manager TI (pengelolaan operasional TI dan implementasi kebijakan)
- **Level Operasional:** Staff TI (eksekusi tugas harian dan dukungan teknis)

**Kebijakan Terkait yang Perlu Dikembangkan:**
1. Kebijakan Manajemen Risiko TI
2. Kebijakan Keamanan Informasi dan Kontrol Akses
3. Kebijakan Backup dan Disaster Recovery
4. Kebijakan Perubahan Sistem (Change Management)
5. Kebijakan Monitoring dan Pelaporan Kinerja TI

---

## C. Goals Cascade & Traceability

| Business Goals | Enterprise Goals | IT-Related Goals | Process/Domain | KPI/KGI |
| :---- | :---- | :---- | :---- | :---- |
| Meningkatkan efisiensi operasional bisnis | Optimalisasi penggunaan sumber daya organisasi | Pengelolaan aset dan sumber daya TI yang optimal | APO12, DSS01 | • Utilisasi aset TI ≥ 75%<br>• Pengurangan biaya operasional TI 40% |
| Menjamin kelangsungan bisnis | Minimalisasi risiko operasional | Manajemen risiko TI yang proaktif dan terstruktur | EDM03, APO12 | • Penurunan insiden TI 60%<br>• Risk coverage ratio ≥ 80% |
| Meningkatkan kualitas layanan pelanggan | Peningkatan keandalan sistem | Ketersediaan dan keandalan infrastruktur TI | DSS01 | • System uptime ≥ 99%<br>• MTTR ≤ 4 jam |
| Mendukung pertumbuhan bisnis | Alignment strategi TI dengan bisnis | Keselarasan investasi TI dengan prioritas bisnis | EDM03, MEA01 | • IT-Business alignment ≥ 75%<br>• ROI investasi TI ≥ 20% |
| Meningkatkan akuntabilitas | Transparansi kinerja organisasi | Monitoring dan pelaporan kinerja TI yang akurat | MEA01 | • KPI achievement rate ≥ 80%<br>• Frekuensi pelaporan bulanan |

---

## D. Control & Evidence Register (Governance View)

| Domain/Proses | Control Objective/Kebijakan | Risiko/Isu | KPI/Metrik | Bukti/Pedoman | Owner |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **EDM03.01** | Framework manajemen risiko disetujui dan dioperasionalkan | Perubahan sistem tanpa analisis risiko | % risiko yang memiliki owner dan rencana mitigasi | • Risk Register<br>• Dokumen penetapan owner risiko<br>• Matriks dampak × probabilitas | Direktur |
| **EDM03.02** | Toleransi risiko TI diselaraskan dengan toleransi risiko organisasi | Risiko TI melebihi toleransi bisnis | Jumlah risiko yang melampaui toleransi | • Dokumen risk appetite<br>• Laporan risiko yang eskalasi<br>• Notulen rapat risk review | Direktur |
| **APO12.01** | Analisis risiko dilakukan secara berkala | Risiko baru tidak teridentifikasi | Frekuensi risk assessment (minimal kuartalan) | • Jadwal dan hasil risk assessment<br>• Daftar risiko baru teridentifikasi<br>• Dokumentasi metodologi assessment | Manager TI |
| **APO12.02** | Rencana mitigasi risiko tersedia untuk risiko prioritas tinggi | Risiko tinggi tanpa mitigasi | % risiko tinggi dengan rencana mitigasi | • Risk Treatment Plan<br>• Timeline implementasi mitigasi<br>• Dokumen PIC dan anggaran | Manager TI |
| **APO12.03** | Monitoring risiko dilakukan dan dilaporkan | Risiko tidak terkontrol | Frekuensi monitoring dan pelaporan risiko | • Dashboard monitoring risiko<br>• Laporan bulanan risiko<br>• Trend analysis risiko | Manager TI |
| **DSS01.01** | Prosedur operasional TI terdokumentasi dan diikuti | Proses manual tanpa standar | % proses dengan SOP terdokumentasi | • Dokumen SOP operasional TI<br>• Checklist kepatuhan SOP<br>• Log audit kepatuhan | Manager TI |
| **DSS01.02** | Log aktivitas sistem terekam dan dapat diaudit | Aktivitas tanpa jejak audit | % transaksi dengan audit trail lengkap | • Log sistem aplikasi<br>• Sample audit trail transaksi<br>• Dokumentasi retention policy | Staff TI |
| **DSS01.03** | Backup dilakukan sesuai jadwal dan dapat di-restore | Kehilangan data kritis | Success rate backup dan restore test | • Jadwal backup<br>• Log hasil backup<br>• Laporan restore test bulanan | Staff TI |
| **DSS01.04** | Kontrol akses pengguna diterapkan dan direview | Akses tidak sesuai dengan peran | % user dengan akses sesuai job role | • Daftar user dan role<br>• Matriks RACI akses<br>• Laporan review akses kuartalan | Staff TI |
| **MEA01.01** | KPI TI didefinisikan dan selaras dengan KPI bisnis | KPI TI tidak relevan dengan bisnis | % KPI TI yang align dengan bisnis | • Dokumen definisi KPI<br>• Matriks keterkaitan KPI TI-bisnis<br>• Dashboard KPI | Manager TI |
| **MEA01.02** | Kinerja TI dimonitor dan dilaporkan secara berkala | Kinerja TI tidak terukur | Frekuensi pelaporan kinerja (bulanan) | • Dashboard kinerja TI<br>• Laporan bulanan ke manajemen<br>• Notulen rapat review kinerja | Manager TI |
| **MEA01.03** | Penilaian kematangan proses TI dilakukan | Tidak ada peningkatan maturity | Peningkatan maturity level per tahun | • Hasil maturity assessment<br>• Gap analysis report<br>• Roadmap peningkatan maturity | Manager TI |

---

## E. Baseline vs Target Maturity

| Domain/Proses | Baseline Level | Target Level | Evidence Kunci | Gap | Prioritas |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **EDM03** - Ensure Risk Optimisation | 1.0 (Initial) | 3.0 (Established) | • Tidak ada risk register formal<br>• Manajemen risiko reaktif<br>• Tidak ada framework manajemen risiko | • Framework manajemen risiko<br>• Risk register terstruktur<br>• Proses review risiko berkala | **Tinggi** |
| **APO12** - Manage Risk | 1.5 (Initial-Managed) | 3.0 (Established) | • Risk assessment tidak terstruktur<br>• Mitigasi dilakukan ad-hoc<br>• Monitoring risiko manual | • Metodologi risk assessment<br>• Risk treatment plan formal<br>• Dashboard monitoring risiko | **Tinggi** |
| **DSS01** - Manage Operations | 1.0 (Initial) | 3.0 (Established) | • SOP tidak lengkap/terdokumentasi<br>• Audit trail tidak konsisten<br>• Backup tidak terjadwal rutin | • SOP operasional lengkap<br>• Log sistem terintegrasi<br>• Schedule backup otomatis | **Sedang** |
| **MEA01** - Monitor & Evaluate | 1.5 (Initial-Managed) | 3.0 (Established) | • KPI TI belum terukur jelas<br>• Pelaporan tidak konsisten<br>• Tidak ada assessment maturity | • KPI dashboard terintegrasi<br>• Laporan berkala terstruktur<br>• Maturity assessment tahunan | **Sedang** |

**Rata-rata Baseline Maturity:** 1.25 (Initial)  
**Target Maturity:** 3.0 (Established)  
**Gap Maturity:** 1.75 level  
**Timeline Target:** 18-24 bulan

---

## F. Analisis Gap & Akar Masalah

| Isu/Gap | Akar Masalah | Dampak | Kontrol/Kebijakan yang Dibutuhkan |
| :---- | :---- | :---- | :---- |
| Framework manajemen risiko tidak ada | • Keterbatasan pengetahuan manajemen risiko<br>• Tidak ada kebijakan formal<br>• Prioritas rendah pada risk management | • Risiko tidak terkelola<br>• Kerugian akibat insiden tidak terprediksi<br>• Keputusan bisnis tidak berbasis risiko | • Kebijakan Manajemen Risiko TI<br>• Pelatihan risk management<br>• Implementasi risk register<br>• Penetapan risk owner |
| SOP operasional tidak lengkap | • Dokumentasi tidak diprioritaskan<br>• Ketergantungan pada knowledge individual<br>• Tidak ada standardisasi proses | • Inkonsistensi layanan<br>• Kesulitan onboarding staff baru<br>• Risiko error tinggi | • Template SOP standar<br>• Program dokumentasi proses<br>• Review dan update SOP berkala |
| Audit trail tidak konsisten | • Sistem tidak terintegrasi<br>• Logging tidak diaktifkan<br>• Tidak ada retention policy | • Kesulitan investigasi insiden<br>• Risiko compliance<br>• Tidak dapat melacak perubahan | • Konfigurasi logging sistem<br>• Implementasi SIEM sederhana<br>• Kebijakan retention log |
| KPI TI tidak terukur | • Definisi KPI tidak jelas<br>• Tidak ada baseline data<br>• Tools monitoring terbatas | • Kinerja TI tidak terukur<br>• Sulit justify investasi TI<br>• Tidak ada continuous improvement | • Framework KPI (BSC/OKR)<br>• Dashboard monitoring<br>• Regular review meeting |
| Backup tidak terjadwal rutin | • Proses manual tanpa automasi<br>• Tidak ada policy backup<br>• Resource terbatas | • Risiko kehilangan data tinggi<br>• RTO/RPO tidak terdefinisi<br>• Business continuity terancam | • Kebijakan Backup & Recovery<br>• Automasi backup<br>• Regular restore testing |
| Kontrol akses tidak direview | • Tidak ada prosedur review akses<br>• Perubahan organisasi tidak update sistem<br>• Awareness keamanan rendah | • Akses berlebih (privilege creep)<br>• Risiko insider threat<br>• Pelanggaran segregation of duty | • Kebijakan Access Control<br>• Review akses kuartalan<br>• User access matrix |

---

## G. Roadmap & Inisiatif (12 bulan)

| No | Inisiatif | Quick Win / Long-term | Deliverable | Estimasi Effort | PIC | Timeline (Q1–Q4) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Penyusunan Risk Register & Framework Manajemen Risiko | Quick Win | • Dokumen Risk Management Policy<br>• Risk Register (minimal 20 risiko)<br>• Matriks dampak-probabilitas | 3 minggu | Manager TI | **Q1** (Minggu 1-3) |
| 2 | Dokumentasi SOP Operasional TI | Quick Win | • SOP Backup & Recovery<br>• SOP Change Management<br>• SOP Incident Management<br>• SOP Access Control | 4 minggu | Manager TI & Staff TI | **Q1** (Minggu 4-7) |
| 3 | Implementasi Logging & Audit Trail | Long-term | • Konfigurasi logging sistem<br>• Retention policy<br>• Sample audit trail report | 6 minggu | Staff TI | **Q1-Q2** (Minggu 8-13) |
| 4 | Definisi dan Setup KPI Dashboard | Long-term | • Dokumen KPI TI<br>• Dashboard monitoring (Excel/BI tool)<br>• Baseline data KPI | 4 minggu | Manager TI | **Q2** (Minggu 14-17) |
| 5 | Automasi Backup & Restore Testing | Quick Win | • Script automasi backup<br>• Schedule backup harian/mingguan<br>• Laporan restore test bulanan | 3 minggu | Staff TI | **Q2** (Minggu 18-20) |
| 6 | Review & Update Kontrol Akses Pengguna | Quick Win | • User access matrix terkini<br>• Laporan review akses<br>• Dokumentasi revoke akses | 2 minggu | Staff TI | **Q2** (Minggu 21-22) |
| 7 | Pelatihan Risk Management untuk Tim TI | Quick Win | • Materi training risk management<br>• Sertifikat peserta<br>• Evaluation report | 1 minggu | Manager TI | **Q3** (Minggu 23) |
| 8 | Implementasi Dashboard Monitoring Risiko | Long-term | • Dashboard monitoring risiko<br>• Prosedur escalation<br>• Laporan bulanan risiko | 5 minggu | Manager TI | **Q3** (Minggu 24-28) |
| 9 | Penetapan Risk Owner & Treatment Plan | Long-term | • Dokumen penetapan risk owner<br>• Risk Treatment Plan<br>• Budget alokasi mitigasi | 4 minggu | Direktur & Manager TI | **Q3** (Minggu 29-32) |
| 10 | Review & Update Kebijakan TI | Long-term | • Policy Keamanan Informasi<br>• Policy Change Management<br>• Policy Disaster Recovery | 6 minggu | Manager TI | **Q3-Q4** (Minggu 33-38) |
| 11 | Maturity Assessment Tahap 2 | Long-term | • Laporan maturity assessment<br>• Gap analysis progress<br>• Adjustment roadmap | 2 minggu | Manager TI | **Q4** (Minggu 39-40) |
| 12 | Evaluasi & Continuous Improvement | Long-term | • Laporan evaluasi implementasi<br>• Lesson learned<br>• Rencana tahun berikutnya | 4 minggu | Manager TI & Direktur | **Q4** (Minggu 41-44) |

**Catatan Prioritas:**
- **Quick Wins (6 inisiatif):** Fokus pada deliverable cepat dengan dampak signifikan (Q1-Q2)
- **Long-term (6 inisiatif):** Memerlukan effort lebih besar, implementasi bertahap (Q1-Q4)

---

## H. KPI & Monitoring

| KPI | Definisi & Rumus | Target | Sumber Data | Frekuensi | PIC |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Risk Coverage Ratio** | (Jumlah risiko dengan rencana mitigasi / Total risiko teridentifikasi) × 100% | ≥ 80% | Risk Register | Bulanan | Manager TI |
| **Incident Reduction Rate** | ((Insiden bulan lalu - Insiden bulan ini) / Insiden bulan lalu) × 100% | 60% dalam 12 bulan (5%/bulan) | Log Insiden TI | Bulanan | Manager TI |
| **SOP Compliance Rate** | (Jumlah proses dengan SOP / Total proses TI) × 100% | 100% | Daftar SOP & Proses | Kuartalan | Manager TI |
| **System Uptime** | (Total waktu tersedia / Total waktu operasional) × 100% | ≥ 99% | Monitoring Tool/Log | Bulanan | Staff TI |
| **Backup Success Rate** | (Backup berhasil / Total scheduled backup) × 100% | 100% | Log Backup | Mingguan | Staff TI |
| **Restore Test Success** | Jumlah restore test berhasil per bulan | ≥ 1 kali/bulan | Laporan Restore Test | Bulanan | Staff TI |
| **IT-Business Alignment Score** | Skor hasil survey alignment (skala 1-5) | ≥ 3.75 (75%) | Survey & Wawancara | Semesteran | Manager TI |
| **KPI Achievement Rate** | (Jumlah KPI tercapai / Total KPI) × 100% | ≥ 80% | Dashboard KPI | Bulanan | Manager TI |
| **Access Review Compliance** | Jumlah review akses tepat waktu per kuartal | 1 kali/kuartal | Laporan Review Akses | Kuartalan | Staff TI |
| **Maturity Level Progress** | Peningkatan maturity level (skala 0-5) | +0.35 level per semester (target 3.0 dalam 24 bulan) | Maturity Assessment | Semesteran | Manager TI |
| **IT Cost Optimization** | ((Biaya TI tahun lalu - Biaya TI tahun ini) / Biaya TI tahun lalu) × 100% | 40% dalam 18 bulan | Laporan Keuangan | Kuartalan | Direktur |
| **Risk Monitoring Frequency** | Jumlah monitoring risiko dilakukan per bulan | ≥ 1 kali/bulan | Dashboard Risiko | Bulanan | Manager TI |

---

## I. RACI

| Aktivitas Governance | R | A | C | I |
| :---- | :---- | :---- | :---- | :---- |
| Penyusunan Risk Register | Manager TI | Direktur | Staff TI | - |
| Persetujuan Risk Management Policy | Direktur | Direktur | Manager TI | - |
| Identifikasi & Penilaian Risiko | Staff TI | Manager TI | Direktur | - |
| Penyusunan Risk Treatment Plan | Manager TI | Direktur | Staff TI | - |
| Monitoring & Pelaporan Risiko | Staff TI | Manager TI | Direktur | - |
| Dokumentasi SOP Operasional | Staff TI | Manager TI | - | Direktur |
| Review & Update SOP | Manager TI | Manager TI | Staff TI | Direktur |
| Konfigurasi Logging Sistem | Staff TI | Manager TI | - | - |
| Setup & Maintenance Dashboard KPI | Staff TI | Manager TI | - | Direktur |
| Definisi KPI TI | Manager TI | Direktur | Staff TI | - |
| Pelaksanaan Backup Harian | Staff TI | Staff TI | Manager TI | - |
| Restore Testing Bulanan | Staff TI | Manager TI | - | Direktur |
| Review Akses Pengguna Kuartalan | Staff TI | Manager TI | - | - |
| Pemberian/Pencabutan Akses | Staff TI | Manager TI | - | - |
| Maturity Assessment | Manager TI | Direktur | Staff TI | - |
| Pelatihan Risk Management | Manager TI | Direktur | - | Staff TI |
| Approval Investasi TI | Direktur | Direktur | Manager TI | - |
| Escalation Risiko Tinggi | Manager TI | Direktur | - | Staff TI |

**Keterangan:**
- **R (Responsible):** Pihak yang melaksanakan aktivitas
- **A (Accountable):** Pihak yang bertanggung jawab dan memiliki otoritas keputusan final
- **C (Consulted):** Pihak yang dikonsultasikan sebelum keputusan/tindakan diambil
- **I (Informed):** Pihak yang diberi informasi setelah keputusan/tindakan diambil

---

## J. Risiko Implementasi & Mitigasi

| Risiko | Prob | Impact | Level | Mitigasi | Owner |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Resistensi perubahan dari tim TI terhadap proses baru | Tinggi | Sedang | **TINGGI** | • Komunikasi manfaat perubahan secara jelas<br>• Libatkan tim dalam penyusunan SOP<br>• Pelatihan dan sosialisasi bertahap<br>• Quick wins untuk membangun kepercayaan | Manager TI |
| Keterbatasan anggaran untuk tools monitoring & automasi | Sedang | Tinggi | **TINGGI** | • Prioritaskan solusi open-source/low-cost<br>• Fase implementasi bertahap<br>• Gunakan Excel/Google Sheets untuk dashboard awal<br>• Justifikasi ROI yang kuat ke manajemen | Direktur |
| Kurangnya kompetensi risk management di tim internal | Tinggi | Tinggi | **TINGGI** | • Pelatihan risk management (internal/eksternal)<br>• Engage konsultan untuk fase awal<br>• Mentoring dan coaching berkelanjutan<br>• Dokumentasi knowledge base | Manager TI |
| Data historis tidak lengkap untuk baseline KPI | Sedang | Sedang | **SEDANG** | • Mulai pengumpulan data dari sekarang<br>• Gunakan estimasi reasonable untuk baseline<br>• Review dan adjust baseline setelah 3-6 bulan<br>• Fokus pada trend improvement | Manager TI |
| Sistem legacy tidak mendukung logging/audit trail | Sedang | Tinggi | **TINGGI** | • Evaluasi upgrade sistem prioritas<br>• Implementasi workaround manual log<br>• Budget untuk modernisasi sistem dalam roadmap<br>• Fokus pada sistem kritis terlebih dahulu | Staff TI |
| Turnover staff TI tinggi | Rendah | Tinggi | **SEDANG** | • Dokumentasi knowledge yang komprehensif<br>• Cross-training antar staff<br>• Improve employee engagement & retention<br>• Rekrutmen talent dengan fit culture | Direktur |
| Scope creep dalam implementasi | Sedang | Sedang | **SEDANG** | • Definisi scope yang jelas di awal<br>• Change control process yang ketat<br>• Regular review progress vs roadmap<br>• Fokus pada prioritas tinggi terlebih dahulu | Manager TI |
| Gangguan operasional selama implementasi | Sedang | Tinggi | **TINGGI** | • Implementasi di luar jam operasional<br>• Pilot testing sebelum full deployment<br>• Rollback plan untuk setiap perubahan<br>• Komunikasi downtime ke stakeholders | Staff TI |
| Ketidakselarasan ekspektasi manajemen vs realitas implementasi | Sedang | Sedang | **SEDANG** | • Komunikasi progress transparan dan berkala<br>• Set realistic expectations di awal<br>• Laporan milestone achievement<br>• Manage ekspektasi dengan evidence | Manager TI |

**Risk Matrix Summary:**
- **Risiko Tinggi (5):** Memerlukan perhatian dan mitigasi segera
- **Risiko Sedang (4):** Monitor ketat dan mitigasi preventif
- **Risiko Rendah (0):** -

---

## K. Lampiran Instrumen

### K.1 Checklist Kebijakan

#### ✅ Checklist Kelengkapan Dokumen Kebijakan TI

| No | Item Kebijakan | Status | Target Completion | PIC |
|----|----------------|--------|-------------------|-----|
| 1 | Kebijakan Manajemen Risiko TI | Belum Ada | Q1 Minggu 3 | Manager TI |
| 2 | Kebijakan Keamanan Informasi & Access Control | Belum Ada | Q3 Minggu 33-34 | Manager TI |
| 3 | Kebijakan Backup & Disaster Recovery | Belum Ada | Q3 Minggu 35-36 | Manager TI |
| 4 | Kebijakan Change Management | Belum Ada | Q3 Minggu 37-38 | Manager TI |
| 5 | Kebijakan Monitoring & Pelaporan Kinerja TI | Belum Ada | Q2 Minggu 17 | Manager TI |

---

### K.2 Template SOP

#### Template SOP Operasional TI (Contoh: Backup & Recovery)

**STANDAR OPERASIONAL PROSEDUR (SOP)**  
**Backup & Recovery Data**

**Nomor SOP:** SOP-TI-001  
**Tanggal Berlaku:** [Tanggal]  
**Revisi:** 1.0

**1. Tujuan**
Memastikan data kritis perusahaan di-backup secara berkala dan dapat di-restore dengan sukses untuk menjaga keberlangsungan bisnis.

**2. Ruang Lingkup**
Seluruh data aplikasi, database, dan file penting yang mendukung operasional SATRIAMART.

**3. Tanggung Jawab**
- **Pelaksana:** Staff TI
- **Penanggung Jawab:** Manager TI
- **Reviewer:** Manager TI (bulanan)

**4. Prosedur**

**4.1 Backup Harian (Incremental)**
- **Waktu:** Setiap hari pukul 23:00 WIB
- **Data:** Transaksi harian, perubahan file
- **Media:** Cloud Storage (Google Drive/OneDrive)
- **Retention:** 7 hari

**4.2 Backup Mingguan (Differential)**
- **Waktu:** Setiap Minggu pukul 22:00 WIB
- **Data:** Seluruh perubahan sejak full backup terakhir
- **Media:** Cloud Storage + External HDD
- **Retention:** 4 minggu

**4.3 Backup Bulanan (Full)**
- **Waktu:** Minggu pertama setiap bulan pukul 20:00 WIB
- **Data:** Seluruh sistem dan data
- **Media:** Cloud Storage + External HDD + Offsite Storage
- **Retention:** 12 bulan

**4.4 Restore Testing**
- **Frekuensi:** Minimal 1 kali per bulan
- **Sample:** Random 5 file/transaksi
- **Dokumentasi:** Laporan hasil test (sukses/gagal + durasi restore)

**5. Checklist Pelaksanaan**
- [ ] Verifikasi jadwal backup sudah terkonfigurasi
- [ ] Periksa kapasitas storage tersedia
- [ ] Jalankan backup sesuai jadwal
- [ ] Verifikasi log backup (success/failed)
- [ ] Dokumentasikan hasil backup di log sheet
- [ ] Lakukan restore test bulanan
- [ ] Laporan ke Manager TI jika ada kegagalan

**6. Lampiran**
- Log Sheet Backup Harian/Mingguan/Bulanan
- Form Laporan Restore Test

---

### K.3 Contoh Dashboard KPI

#### Dashboard KPI Tata Kelola TI SATRIAMART (Format Sederhana)

**Periode:** [Bulan/Tahun]

| KPI | Target | Aktual | Status | Trend | Keterangan |
|-----|--------|--------|--------|-------|------------|
| Risk Coverage Ratio | ≥ 80% | 45% | Belum Tercapai | Stabil | Perlu percepat penyusunan risk treatment plan |
| Incident Reduction | -5%/bulan | -2% | Perlu Perbaikan | Menurun | Insiden menurun namun belum sesuai target |
| SOP Compliance | 100% | 30% | Belum Tercapai | Meningkat | Dokumentasi SOP sedang dalam progress |
| System Uptime | ≥ 99% | 97.5% | Perlu Perbaikan | Stabil | Downtime 2.5% akibat maintenance tidak terencana |
| Backup Success Rate | 100% | 95% | Perlu Perbaikan | Meningkat | 5% gagal karena storage penuh |
| Restore Test Success | ≥ 1/bulan | 0 | Belum Tercapai | Stabil | Belum ada schedule restore test |

**Keterangan Status:**
- **Tercapai:** Aktual ≥ Target
- **Perlu Perbaikan:** Aktual 70-99% dari Target
- **Belum Tercapai:** Aktual < 70% dari Target

**Trend:**
- Meningkat: Menunjukkan perbaikan dari periode sebelumnya
- Stabil: Tidak ada perubahan signifikan
- Menurun: Menunjukkan penurunan dari periode sebelumnya

---

### K.4 Template Risk Register

#### Risk Register SATRIAMART

**Tabel 1: Identifikasi dan Penilaian Risiko**

| ID | Kategori | Deskripsi Risiko | Prob | Impact | Level | Owner |
|----|----------|------------------|------|--------|-------|-------|
| R001 | Keamanan | Kehilangan data akibat tidak ada backup teratur | 4 | 4 | 16 - Tinggi | Staff TI |
| R002 | Operasional | Downtime sistem aplikasi POS | 3 | 4 | 12 - Tinggi | Staff TI |
| R003 | Keamanan | Akses tidak authorized ke data sensitif | 3 | 4 | 12 - Tinggi | Manager TI |
| R004 | Compliance | Tidak ada dokumentasi SOP proses TI | 4 | 3 | 12 - Tinggi | Manager TI |
| R005 | Strategic | Ketidakselarasan investasi TI dengan tujuan bisnis | 3 | 3 | 9 - Sedang | Direktur |

**Tabel 2: Rencana Mitigasi Risiko**

| ID | Rencana Treatment/Mitigasi | Status |
|----|----------------------------|--------|
| R001 | Implementasi backup otomatis, Upgrade storage capacity, Restore testing bulanan | Open |
| R002 | Setup monitoring tool, Maintenance berkala, Upgrade server | Open |
| R003 | Implementasi access control matrix, Review akses kuartalan, Pelatihan awareness keamanan | Open |
| R004 | Program dokumentasi SOP, Template standar, Review dan update SOP berkala | In Progress |
| R005 | Implementasi COBIT 2019, IT-Business alignment workshop, KPI dashboard | In Progress |

**Keterangan Penilaian:**
- **Probabilitas (Prob):** 1=Sangat Rendah, 2=Rendah, 3=Sedang, 4=Tinggi, 5=Sangat Tinggi
- **Impact:** 1=Sangat Rendah, 2=Rendah, 3=Sedang, 4=Tinggi, 5=Sangat Tinggi
- **Level Risiko:** Prob × Impact (1-6=Rendah, 8-12=Sedang, 15-25=Tinggi)

---

## L. Penutup

Dokumen ini merupakan roadmap komprehensif untuk meningkatkan tata kelola TI SATRIAMART dari maturity level 1.25 (Initial) menjadi 3.0 (Established) dalam periode 12-18 bulan. Keberhasilan implementasi memerlukan komitmen penuh dari seluruh stakeholder, terutama Direktur sebagai sponsor dan Manager TI sebagai champion perubahan.

**Key Success Factors:**
1. **Komitmen Manajemen:** Dukungan penuh dari top management dalam alokasi resources dan decision making
2. **Komunikasi Efektif:** Sosialisasi berkelanjutan kepada seluruh tim tentang manfaat dan progress implementasi
3. **Quick Wins:** Fokus pada inisiatif quick wins di Q1-Q2 untuk membangun momentum dan kepercayaan
4. **Monitoring Ketat:** Dashboard KPI dan regular review meeting untuk ensure on-track execution
5. **Continuous Learning:** Pelatihan dan knowledge sharing untuk meningkatkan capability tim

**Next Steps:**
1. **Minggu 1-2:** Sosialisasi roadmap ke seluruh stakeholder dan kick-off meeting
2. **Minggu 3:** Mulai penyusunan Risk Register dan Risk Management Policy (Inisiatif #1)
3. **Minggu 4:** Parallel: Dokumentasi SOP Operasional TI (Inisiatif #2)
4. **Monthly Review:** Progress review meeting setiap akhir bulan dengan Direktur

---

**Disusun Oleh:**  
Kelompok 2 - IT Governance Project Team

**Roki Anjas** (11250066) - Ketua Tim & Analis Data  
**Fahruroji** (11250085) - Analis Kebijakan & Instrumen  
**Susanto** (11250068) - Analis Risiko & Penyusun Laporan

**Tanggal:** 9 November 2025

---

**Lembar Persetujuan**

|  | Nama | Jabatan | Tanda Tangan | Tanggal |
|--|------|---------|--------------|---------|
| **Dibuat oleh:** | Kelompok 2 | Tim Proyek | _____________ | 9 Nov 2025 |
| **Diperiksa oleh:** | Daniati Uki Eka Saputri, M.Kom | Dosen Pengampu | _____________ | __________ |
| **Disetujui oleh:** | [Nama Direktur SATRIAMART] | Direktur | _____________ | __________ |
