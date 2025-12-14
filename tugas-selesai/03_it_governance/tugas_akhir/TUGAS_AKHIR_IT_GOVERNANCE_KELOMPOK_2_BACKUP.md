# ASSESSMENT DAN IMPLEMENTASI FRAMEWORK TATA KELOLA TEKNOLOGI INFORMASI PADA SATRIAMART: PENDEKATAN COBIT 2019

**Roki Anjas¹*; Fahruroji²; Susanto³**

Program Studi Sistem Informasi¹  
Universitas Nusa Mandiri, Jakarta, Indonesia¹  
https://www.nusamandiri.ac.id¹  
rokianjas@nusamandiri.ac.id¹*  
(*) Corresponding Author

![Lisensi Creative Commons](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)

Karya ini didistribusikan di bawah Lisensi Creative Commons Attribution-NonCommercial 4.0 International.

---

## Abstract

*The rapid development of information technology demands organizations to implement structured IT governance to optimize business value and manage risks effectively. SATRIAMART, a retail company specializing in acrylic decorations and accessories, faces challenges in managing information technology with a maturity level of only 1.2 on a scale of 5 (ad-hoc/initial). This research aims to assess the current maturity level of IT governance and design a comprehensive implementation roadmap using the COBIT 2019 framework. The research methodology combines maturity assessment, gap analysis, and risk-based control testing on four domains: EDM03, APO12, DSS01, and MEA01. Data was collected through documentation analysis, interviews, and observations conducted from May to October 2025. The results show that the current maturity level is 1.2 with critical gaps in risk management, resource optimization, and IT-business alignment. The proposed framework and 18-24 month implementation roadmap aims to increase the maturity level to 3.0 (managed), reduce IT incidents by 60%, improve IT-business alignment by 75%, and optimize IT resource utilization by 40%. This research contributes to the literature on COBIT 2019 implementation in medium-scale retail companies in Indonesia and provides a practical model that can be adapted by similar organizations.*

**Keywords:** cobit 2019, gap analysis, it governance, maturity assessment, risk management.

---

## Abstrak

Perkembangan teknologi informasi yang pesat menuntut organisasi untuk menerapkan tata kelola TI yang terstruktur guna mengoptimalkan nilai bisnis dan mengelola risiko secara efektif. SATRIAMART, perusahaan retail yang bergerak di bidang dekorasi dan aksesoris akrilik, menghadapi tantangan dalam mengelola teknologi informasi dengan tingkat kematangan hanya 1,2 dari skala 5 (ad-hoc/initial). Penelitian ini bertujuan untuk melakukan assessment tingkat kematangan tata kelola TI saat ini dan merancang roadmap implementasi yang komprehensif menggunakan framework COBIT 2019. Metodologi penelitian mengombinasikan maturity assessment, gap analysis, dan risk-based control testing pada empat domain: EDM03, APO12, DSS01, dan MEA01. Data dikumpulkan melalui analisis dokumentasi, wawancara, dan observasi yang dilakukan pada periode Mei–Oktober 2025. Hasil penelitian menunjukkan bahwa tingkat kematangan saat ini berada pada level 1,2 dengan kesenjangan kritis dalam manajemen risiko, optimalisasi sumber daya, dan keselarasan TI-bisnis. Framework yang dirancang dan roadmap implementasi selama 18–24 bulan bertujuan untuk meningkatkan tingkat kematangan menjadi 3,0 (managed), mengurangi insiden TI sebesar 60%, meningkatkan keselarasan TI-bisnis sebesar 75%, dan mengoptimalkan utilisasi sumber daya TI sebesar 40%. Penelitian ini berkontribusi pada literatur implementasi COBIT 2019 di perusahaan retail skala menengah di Indonesia dan memberikan model praktis yang dapat diadaptasi oleh organisasi sejenis.

**Kata Kunci:** analisis kesenjangan, cobit 2019, manajemen risiko, penilaian kematangan, tata kelola ti.

---

## PENDAHULUAN

Di era transformasi digital, teknologi informasi (TI) telah menjadi tulang punggung operasional dan strategi bisnis perusahaan. Namun, pemanfaatan TI yang tidak dikelola dengan baik dapat menimbulkan risiko signifikan seperti ketidakselarasan strategi TI dengan tujuan bisnis, inefisiensi penggunaan sumber daya, dan kerentanan terhadap ancaman keamanan informasi. Menurut IT Governance Institute (2021), tata kelola TI yang efektif dapat meningkatkan nilai bisnis hingga 20% melalui pengelolaan risiko yang lebih baik dan pemanfaatan sumber daya TI yang optimal. Penelitian Afifah, Adam, dan Marfuah (2023) pada perusahaan manufaktur di Indonesia menunjukkan bahwa implementasi framework COBIT 2019 mampu meningkatkan efektivitas pemetaan tata kelola TI dan menyelaraskan strategi TI dengan objektif bisnis organisasi.

Framework IT Governance seperti COBIT 2019 telah terbukti memberikan panduan komprehensif dalam mengelola dan mengatur TI secara terstruktur. ISACA (2019) menegaskan bahwa COBIT 2019 menyediakan design factor yang dapat disesuaikan dengan karakteristik organisasi, termasuk industri manufaktur dan retail. Hasil systematic literature review menunjukkan bahwa 100% penelitian IT governance pada perusahaan manufaktur Indonesia menggunakan framework COBIT, dengan 62% mengadopsi versi terbaru COBIT 2019 karena kemampuannya dalam memberikan pendekatan domain-specific yang lebih fleksibel dan adaptif terhadap kebutuhan bisnis (Aziz, Kusrini, & Nasiri, 2023; Thehawijaya & Fajar, 2024).

SATRIAMART merupakan perusahaan yang bergerak di bidang dekorasi dan aksesoris akrilik dengan produk unggulan meliputi nomor rumah akrilik, signage akrilik, papan nama akrilik, dan aksesoris dekorasi custom. Sebagai perusahaan retail yang sedang berkembang, SATRIAMART menghadapi tantangan dalam mengelola teknologi informasi secara efektif untuk mendukung pertumbuhan bisnisnya. Berdasarkan assessment awal, tingkat kematangan (maturity level) tata kelola TI SATRIAMART masih berada pada level 1,2 dari skala 5 (ad-hoc/initial), dimana proses-proses TI belum terdokumentasi dengan baik dan masih bersifat reaktif.

Kondisi ini menimbulkan beberapa permasalahan kritis: pertama, tidak adanya keselarasan antara strategi TI dengan strategi bisnis mengakibatkan investasi TI tidak memberikan nilai optimal bagi pencapaian tujuan organisasi. Kedua, manajemen risiko TI yang belum terstruktur meningkatkan potensi kerugian akibat downtime sistem, kehilangan data, atau security breach yang dapat berdampak pada reputasi dan kepercayaan pelanggan. Ketiga, penggunaan sumber daya TI yang tidak efisien menyebabkan pemborosan anggaran dan duplikasi fungsi sistem. Keempat, tidak adanya mekanisme monitoring dan evaluasi kinerja TI menyulitkan manajemen dalam mengambil keputusan strategis terkait investasi teknologi.

Permasalahan yang dihadapi SATRIAMART sejalan dengan temuan penelitian Agustriani (2024) pada perusahaan manufaktur di Indonesia, yang mengidentifikasi bahwa manajemen risiko TI merupakan area kritis yang memerlukan perhatian khusus melalui implementasi domain EDM03 (Ensure Risk Optimisation) dan APO12 (Manage Risk) COBIT 2019. Studi Ramadhan dan Ramadhan (2025) pada UMKM juga menunjukkan bahwa transformasi digital tanpa framework tata kelola TI yang memadai dapat menghambat efektivitas sistem dan meningkatkan risiko operasional. Riyadli dan Arliyana (2022) menekankan pentingnya perencanaan dan implementasi TI yang terstruktur pada usaha skala menengah untuk menghindari pemborosan investasi teknologi. Penelitian Elina (2021) membuktikan bahwa evaluasi implementasi tata kelola TI menggunakan framework COBIT dapat meningkatkan efisiensi organisasi secara signifikan.

Meskipun penelitian tentang implementasi COBIT 2019 pada perusahaan manufaktur telah cukup banyak dilakukan, namun terdapat kesenjangan dalam penerapannya pada perusahaan retail skala menengah yang fokus pada produk custom dan dekorasi. Mayoritas penelitian existing (50%) terbatas pada single case study dengan fokus domain tertentu (Afifah et al., 2023; Aziz et al., 2023), sementara implementasi komprehensif yang mencakup assessment maturity, risk management, dan roadmap implementasi masih terbatas, khususnya untuk sektor retail dekorasi dan aksesoris.

Thehawijaya dan Fajar (2024) menyoroti bahwa pendekatan domain-specific sangat penting dalam implementasi COBIT 2019 pada perusahaan manufaktur, dimana domain APO (Align, Plan, and Organize) menjadi prioritas utama untuk perencanaan strategis TI. Namun, penelitian tersebut belum mengeksplorasi secara mendalam bagaimana framework tersebut dapat diadaptasi untuk perusahaan retail dengan karakteristik operasional yang berbeda dari manufaktur otomotif. Di sisi lain, Hapsari (2018) mengimplementasikan COBIT 5 pada PT Krakatau Tirta Industri namun menggunakan versi framework yang sudah tidak terbaru dan kurang relevan dengan design factor COBIT 2019 yang lebih adaptif.

Berdasarkan latar belakang tersebut, penelitian ini bertujuan untuk: (1) menganalisis tingkat kematangan tata kelola TI pada SATRIAMART menggunakan framework COBIT 2019 dengan pendekatan design factor analysis; (2) mengidentifikasi kesenjangan antara kondisi saat ini dengan target maturity level serta faktor kritis keberhasilan implementasi framework tata kelola TI; dan (3) merancang framework tata kelola TI dengan fokus domain EDM, APO, EDM03, dan APO12 serta menyusun roadmap implementasi untuk meningkatkan maturity level dari ad-hoc (1,2) ke managed (3,0). Penelitian ini diharapkan dapat memperkaya literatur implementasi COBIT 2019 pada perusahaan retail skala menengah di Indonesia dan memberikan model assessment maturity IT governance yang dapat direplikasi oleh peneliti lain serta diadaptasi oleh perusahaan retail sejenis.

---

## BAHAN DAN METODE

Penelitian ini menggunakan pendekatan kualitatif dengan metode studi kasus untuk menganalisis tata kelola teknologi informasi pada SATRIAMART. Metode penelitian dirancang untuk menjawab tiga rumusan masalah utama: (1) tingkat kematangan tata kelola TI saat ini; (2) kesenjangan dan faktor kritis yang memengaruhi capaian maturity level; dan (3) rekomendasi perbaikan dan roadmap implementasi framework COBIT 2019.

### Desain Penelitian

Penelitian ini mengombinasikan tiga metode analisis utama: Maturity Assessment COBIT 2019, Gap Analysis, dan Risk-Based Control Testing. Maturity Assessment diperlukan untuk mengukur tingkat kematangan tata kelola TI saat ini (baseline level 1,2) dan memetakan target pencapaian (level 3,0). Gap Analysis digunakan untuk mengidentifikasi kesenjangan antara kondisi eksisting dengan best practice COBIT 2019. Risk-Based Control Testing dipilih karena SATRIAMART menghadapi risiko signifikan terkait insiden TI, kehilangan data, dan downtime yang berdampak pada operasional bisnis. Framework COBIT 2019 dipilih karena terbukti efektif untuk perusahaan retail skala menengah di Indonesia dan dapat disesuaikan dengan karakteristik SATRIAMART.

### Sumber Data

Penelitian ini menggunakan data primer dan sekunder yang dikumpulkan selama periode Mei–Oktober 2025. Data primer diperoleh melalui wawancara mendalam dengan Direktur SATRIAMART, Manager TI, dan Staff TI, serta observasi langsung terhadap proses operasional TI. Data sekunder bersumber dari dokumen kebijakan TI (jika tersedia), Standard Operating Procedure (SOP) operasional TI, log insiden dan downtime sistem, risk register, data backup dan recovery log, dokumentasi kontrol akses pengguna, laporan anggaran dan investasi TI, inventaris aset TI, dokumen strategi bisnis periode 2025–2027, serta struktur organisasi dan job description.

Tabel 1 menunjukkan daftar lengkap sumber data yang digunakan dalam penelitian ini beserta periode pengumpulan, pemilik data, tingkat sensitivitas, dan status akses.

**Tabel 1. Daftar Sumber Data Penelitian**

| No | Nama Bahan | Sumber | Periode | Pemilik | Sensitivitas | Status Akses |
|----|------------|--------|---------|---------|--------------|--------------|
| 1 | Dokumen Kebijakan TI | Manajemen SATRIAMART | Versi 2025 | Direktur | Internal | Diperoleh |
| 2 | SOP Operasional TI | Tim TI | Versi 2025 | Manager TI | Internal | Diperoleh |
| 3 | Log Insiden & Downtime | Sistem Ticketing | Mei–Okt 2025 | Staff TI | Internal | Diperoleh |
| 4 | Risk Register | Manajemen | Q2-Q3 2025 | Manager TI | Confidential | Diperoleh |
| 5 | Data Backup & Recovery | Server | Mei–Okt 2025 | Staff TI | Internal | Diperoleh |
| 6 | Kontrol Akses Pengguna | Sistem | Oktober 2025 | Staff TI | Confidential | Diperoleh |
| 7 | Anggaran & Investasi TI | Keuangan | Tahun 2025 | Finance | Confidential | Diperoleh |
| 8 | Inventaris Aset TI | Database | Oktober 2025 | Staff TI | Internal | Diperoleh |
| 9 | Strategi Bisnis | Manajemen | 2025-2027 | Direktur | Internal | Diperoleh |
| 10 | Struktur Organisasi | SDM | 2025 | Manajemen | Internal | Diperoleh |

Sumber: (Hasil Penelitian, 2025)

### Teknik Pengumpulan Data

Pengumpulan data dilakukan melalui tiga teknik utama. Pertama, analisis dokumentasi terhadap seluruh dokumen yang tercantum dalam Tabel 1 untuk memahami kondisi eksisting tata kelola TI SATRIAMART. Kedua, wawancara terstruktur dan semi-terstruktur dengan stakeholder kunci menggunakan instrumen assessment COBIT 2019 yang telah disesuaikan dengan konteks SATRIAMART. Ketiga, observasi langsung terhadap proses operasional TI, mekanisme penanganan insiden, prosedur backup dan recovery, serta implementasi kontrol keamanan informasi.

### Instrumen Penelitian

Instrumen assessment dikembangkan berdasarkan framework COBIT 2019 dengan fokus pada empat domain prioritas: EDM03 (Ensure Risk Optimisation), APO12 (Manage Risk), DSS01 (Manage Operations), dan MEA01 (Monitor, Evaluate and Assess Performance and Conformance). Setiap domain dievaluasi menggunakan capability level COBIT 2019 dengan skala 0–5: Level 0 (Incomplete), Level 1 (Performed), Level 2 (Managed), Level 3 (Established), Level 4 (Predictable), dan Level 5 (Optimizing).

Tabel 2 menunjukkan matriks keterkaitan antara tujuan penelitian, data yang diperlukan, metode analisis, dan output yang diharapkan untuk memastikan traceability yang jelas.

**Tabel 2. Matriks Tujuan, Data, Metode, dan Output Penelitian**

| Tujuan | Data/Bahan | Alasan Relevansi | Metode | Output Diharapkan |
|--------|------------|------------------|---------|-------------------|
| Meningkatkan maturity level dari 1,2 ke 3,0 | Dokumentasi SOP TI, Risk Register, Log Insiden 6 bulan | Menggambarkan kondisi tata kelola saat ini dan mengidentifikasi kesenjangan | Maturity Assessment COBIT 2019 & Gap Analysis | Skor maturity per domain, daftar gap, prioritas perbaikan |
| Menurunkan insiden TI sebesar 60% | Log insiden TI, Laporan downtime, Dokumentasi penanganan masalah | Mengidentifikasi pola insiden dan akar masalah | Risk Assessment (ISO 27005) & Root Cause Analysis | Daftar risiko prioritas, rekomendasi mitigasi |
| Meningkatkan keselarasan TI-Bisnis 75% | Dokumen strategi bisnis, Rencana investasi TI, KPI bisnis dan TI | Mengevaluasi alignment strategi TI dengan tujuan bisnis | Pemetaan COBIT 2019 (EDM & APO) & Benchmark Control | Matriks alignment, gap keselarasan, rekomendasi perbaikan |
| Optimalisasi sumber daya TI 40% | Data anggaran TI, Utilisasi sistem, Inventaris aset TI | Menganalisis efisiensi penggunaan sumber daya | RACI Matrix & Process Walkthrough | Peta proses optimal, clarity peran, efisiensi biaya |

Sumber: (Hasil Penelitian, 2025)

### Teknik Analisis Data

Analisis data dilakukan melalui lima tahapan. Tahap pertama adalah maturity assessment untuk menilai capability level setiap domain berdasarkan Process Assessment Model (PAM) COBIT 2019. Tahap kedua adalah gap analysis untuk mengidentifikasi kesenjangan antara current state (1,2) dan desired state (3,0). Tahap ketiga adalah risk assessment menggunakan metode ISO 27005 untuk mengidentifikasi, menganalisis, dan mengevaluasi risiko TI. Tahap keempat adalah root cause analysis untuk mengidentifikasi akar masalah dari insiden TI yang terjadi. Tahap kelima adalah penyusunan roadmap implementasi menggunakan pendekatan fase-fase (quick wins, short-term, medium-term, long-term) dengan mempertimbangkan prioritas, resource availability, dan business impact.

### Validitas dan Reliabilitas

Validitas penelitian dijamin melalui triangulasi data (dokumentasi, wawancara, observasi), triangulasi sumber (Direktur, Manager TI, Staff TI), dan peer review dengan dosen pembimbing. Reliabilitas dipastikan melalui penggunaan instrumen standar COBIT 2019, dokumentasi lengkap proses assessment, dan konsistensi metode scoring maturity level.

---

## HASIL DAN PEMBAHASAN

### Hasil Assessment Tingkat Kematangan Tata Kelola TI

Berdasarkan assessment yang dilakukan menggunakan framework COBIT 2019 pada periode Mei–Oktober 2025, tingkat kematangan (maturity level) tata kelola TI SATRIAMART berada pada level 1,2 dari skala 5, yang termasuk dalam kategori ad-hoc/initial. Pada level ini, proses-proses TI masih bersifat reaktif, tidak terdokumentasi dengan baik, sangat bergantung pada pengetahuan individu, dan belum memiliki standar yang konsisten.

Tabel 3 menunjukkan hasil assessment maturity level untuk setiap domain COBIT 2019 yang menjadi fokus penelitian.

**Tabel 3. Hasil Assessment Maturity Level per Domain COBIT 2019**

| Domain | Nama Proses | Current Maturity Level | Target Maturity Level | Gap |
|--------|-------------|------------------------|----------------------|-----|
| EDM03 | Ensure Risk Optimisation | 1,0 | 3,0 | 2,0 |
| APO12 | Manage Risk | 1,2 | 3,0 | 1,8 |
| DSS01 | Manage Operations | 1,5 | 3,0 | 1,5 |
| MEA01 | Monitor, Evaluate and Assess Performance | 1,0 | 3,0 | 2,0 |
| **Rata-rata** | | **1,2** | **3,0** | **1,8** |

Sumber: (Hasil Penelitian, 2025)

Hasil assessment menunjukkan bahwa domain EDM03 (Ensure Risk Optimisation) dan MEA01 (Monitor, Evaluate and Assess Performance) memiliki maturity level terendah (1,0), yang mengindikasikan bahwa framework manajemen risiko belum disetujui dan dioperasionalkan secara formal, serta tidak ada mekanisme monitoring dan evaluasi kinerja TI yang terstruktur. Domain APO12 (Manage Risk) berada pada level 1,2, dimana risiko TI dikelola secara ad-hoc tanpa risk register yang terdokumentasi. Domain DSS01 (Manage Operations) memiliki maturity level tertinggi (1,5) karena beberapa prosedur operasional dasar sudah mulai diterapkan meskipun belum terstandardisasi.

### Identifikasi Kesenjangan dan Faktor Kritis

Analisis gap mengidentifikasi beberapa kesenjangan kritis antara kondisi saat ini dengan target maturity level 3,0 (managed). Tabel 4 menunjukkan kesenjangan utama yang ditemukan pada setiap domain.

**Tabel 4. Identifikasi Kesenjangan (Gap) per Domain**

| Domain | Kesenjangan Utama | Dampak Bisnis | Prioritas |
|--------|-------------------|---------------|-----------|
| EDM03 | Tidak ada framework manajemen risiko formal; Toleransi risiko belum didefinisikan; Risiko TI tidak memiliki owner yang jelas | Potensi kerugian tidak terukur; Keputusan investasi TI tidak berbasis risiko | Sangat Tinggi |
| APO12 | Risk register tidak ada; Tidak ada proses identifikasi risiko berkala; Mitigasi risiko bersifat reaktif | Insiden berulang; Downtime tidak terprediksi; Biaya perbaikan tinggi | Sangat Tinggi |
| DSS01 | SOP operasional belum lengkap; Eskalasi masalah tidak terstruktur; Backup dilakukan manual tidak terjadwal | Inkonsistensi layanan; Recovery time lama; Potensi kehilangan data | Tinggi |
| MEA01 | Tidak ada KPI untuk TI; Pelaporan kinerja tidak rutin; Tidak ada mekanisme continuous improvement | Kinerja TI tidak terukur; Keputusan tidak data-driven; Perbaikan tidak sistematis | Tinggi |

Sumber: (Hasil Penelitian, 2025)

Dari analisis gap tersebut, penelitian ini mengidentifikasi lima faktor kritis yang memengaruhi keberhasilan implementasi framework tata kelola TI: (1) komitmen manajemen puncak; (2) ketersediaan sumber daya (SDM dan anggaran); (3) budaya organisasi yang adaptif terhadap perubahan; (4) kemampuan tim TI dalam mengadopsi framework; dan (5) dukungan teknologi yang memadai.

### Analisis Risiko TI

Berdasarkan data log insiden dan downtime periode Mei–Oktober 2025, penelitian ini mengidentifikasi 47 insiden TI dengan total downtime 156 jam. Tabel 5 menunjukkan kategori insiden dan frekuensi kejadian.

**Tabel 5. Kategori dan Frekuensi Insiden TI**

| Kategori Insiden | Frekuensi | Persentase | Total Downtime (Jam) | MTTR (Jam) |
|------------------|-----------|------------|----------------------|------------|
| Hardware Failure | 12 | 25,5% | 48 | 4,0 |
| Software Error | 18 | 38,3% | 54 | 3,0 |
| Network Issue | 8 | 17,0% | 32 | 4,0 |
| Security Incident | 3 | 6,4% | 12 | 4,0 |
| Human Error | 6 | 12,8% | 10 | 1,7 |
| **Total** | **47** | **100%** | **156** | **3,3** |

Sumber: (Hasil Penelitian, 2025)

Analisis root cause terhadap insiden-insiden tersebut mengidentifikasi bahwa 68% insiden disebabkan oleh tidak adanya prosedur preventive maintenance, 21% disebabkan oleh kurangnya pelatihan SDM TI, dan 11% disebabkan oleh keterbatasan infrastruktur. Mean Time to Repair (MTTR) rata-rata adalah 3,3 jam, yang masih di atas target 2 jam untuk perusahaan retail.

Risk assessment menggunakan metode ISO 27005 menghasilkan risk register dengan 23 risiko TI yang teridentifikasi. Tabel 6 menunjukkan lima risiko dengan prioritas tertinggi berdasarkan skor dampak × probabilitas.

**Tabel 6. Top 5 Risiko TI Berdasarkan Prioritas**

| No | Risiko | Dampak (1-5) | Probabilitas (1-5) | Skor Risiko | Kategori | Mitigasi yang Diusulkan |
|----|--------|--------------|-------------------|-------------|----------|------------------------|
| 1 | Kehilangan data akibat kegagalan backup | 5 | 4 | 20 | Critical | Implementasi automated backup & disaster recovery plan |
| 2 | Downtime sistem order akibat server overload | 4 | 5 | 20 | Critical | Upgrade kapasitas server & implementasi load balancing |
| 3 | Pelanggaran data pelanggan akibat weak access control | 5 | 3 | 15 | High | Implementasi IAM (Identity Access Management) |
| 4 | Ketergantungan pada key person (single point of failure) | 4 | 4 | 16 | High | Knowledge transfer & dokumentasi SOP lengkap |
| 5 | Investasi TI tidak selaras dengan prioritas bisnis | 3 | 5 | 15 | High | Implementasi IT governance framework (COBIT) |

Sumber: (Hasil Penelitian, 2025)

### Analisis Keselarasan TI-Bisnis

Pemetaan keselarasan strategi TI dengan tujuan bisnis menggunakan Goals Cascade COBIT 2019 menunjukkan tingkat alignment yang masih rendah (42%). Tabel 7 menunjukkan hasil pemetaan antara business goals, enterprise goals, dan IT-related goals SATRIAMART.

**Tabel 7. Goals Cascade: Pemetaan TI-Bisnis SATRIAMART**

| Business Goals | Enterprise Goals | IT-Related Goals | Process/Domain | Tingkat Alignment Saat Ini |
|----------------|------------------|------------------|----------------|---------------------------|
| Meningkatkan efisiensi operasional | Optimalisasi sumber daya | Pengelolaan aset TI optimal | APO12, DSS01 | 35% |
| Menjamin kelangsungan bisnis | Minimalisasi risiko | Manajemen risiko TI proaktif | EDM03, APO12 | 25% |
| Meningkatkan kualitas layanan | Peningkatan keandalan | Ketersediaan infrastruktur TI | DSS01 | 55% |
| Mendukung pertumbuhan bisnis | Alignment strategi TI-bisnis | Keselarasan investasi TI | EDM03, MEA01 | 40% |
| Meningkatkan akuntabilitas | Transparansi kinerja | Monitoring kinerja TI | MEA01 | 30% |
| **Rata-rata** | | | | **37%** |

Sumber: (Hasil Penelitian, 2025)

Rendahnya tingkat alignment mengindikasikan bahwa investasi dan inisiatif TI belum sepenuhnya mendukung pencapaian tujuan bisnis strategis SATRIAMART. Hal ini sejalan dengan temuan Thehawijaya dan Fajar (2024) yang menyatakan bahwa perusahaan dengan maturity level rendah cenderung memiliki IT-business alignment di bawah 50%.

### Analisis Optimalisasi Sumber Daya TI

Analisis utilisasi sumber daya TI menunjukkan beberapa inefisiensi. Utilisasi server rata-rata hanya 45%, namun terdapat spike hingga 95% pada jam-jam tertentu yang menyebabkan downtime. Anggaran TI tahun 2025 sebesar Rp 450 juta, dengan alokasi 65% untuk operational expense (OPEX) dan 35% untuk capital expense (CAPEX). Analisis menunjukkan bahwa 40% dari OPEX digunakan untuk perbaikan reaktif yang sebenarnya dapat dicegah melalui preventive maintenance.

Tabel 8 menunjukkan analisis efisiensi penggunaan anggaran TI SATRIAMART.

**Tabel 8. Analisis Efisiensi Anggaran TI**

| Kategori Pengeluaran | Budget (Rp Juta) | Aktual (Rp Juta) | Persentase | Kategori Efisiensi |
|---------------------|------------------|------------------|------------|-------------------|
| Hardware & Infrastructure | 100 | 115 | 25,6% | Overbudget |
| Software & License | 50 | 48 | 10,7% | Efisien |
| Maintenance & Support | 120 | 145 | 32,2% | Overbudget (Reaktif) |
| Personnel & Training | 80 | 65 | 14,4% | Underutilized |
| Projects & Development | 100 | 77 | 17,1% | Underutilized |
| **Total** | **450** | **450** | **100%** | |

Sumber: (Hasil Penelitian, 2025)

Analisis menunjukkan bahwa kategori Maintenance & Support mengalami overbudget 20,8% karena sifat perbaikan yang reaktif. Sebaliknya, kategori Personnel & Training underutilized 18,8%, mengindikasikan kurangnya investasi pada pengembangan kapabilitas SDM TI.

### Perancangan Framework Tata Kelola TI

Berdasarkan hasil assessment dan gap analysis, penelitian ini merancang framework tata kelola TI SATRIAMART yang komprehensif dengan fokus pada empat domain COBIT 2019: EDM03, APO12, DSS01, dan MEA01. Framework ini dirancang untuk meningkatkan maturity level dari 1,2 (ad-hoc) menjadi 3,0 (managed) dalam periode 18–24 bulan.

Framework yang dirancang mencakup lima komponen utama yang terintegrasi: (1) Governance Structure – penetapan roles & responsibilities yang jelas menggunakan RACI matrix; (2) Policy & Procedure – pengembangan kebijakan manajemen risiko, keamanan informasi, backup & recovery, change management, dan performance monitoring; (3) Risk Management Framework – implementasi risk register, risk assessment berkala, dan mekanisme mitigasi proaktif; (4) Performance Management – penetapan KPI TI yang selaras dengan business goals dan dashboard monitoring real-time; dan (5) Continuous Improvement – mekanisme review berkala, lessons learned, dan optimization.

Struktur governance yang dirancang mengadopsi model three-tier (strategic, tactical, operational) dengan penetapan roles & responsibilities menggunakan RACI matrix. Gambar 3 menunjukkan struktur governance dan pembagian peran untuk setiap stakeholder dalam implementasi framework tata kelola TI.

```
┌─────────────────────────────────────────────────────────────────────────┐
│           STRUKTUR GOVERNANCE & RACI MATRIX SATRIAMART                  │
└─────────────────────────────────────────────────────────────────────────┘

                        ┌──────────────────┐
                        │    DIREKTUR      │
                        │  (STRATEGIC)     │
                        │                  │
                        │ • Approve Policy │
                        │ • Resource Alloc │
                        │ • Risk Appetite  │
                        └────────┬─────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
          ┌─────────▼─────────┐     ┌────────▼────────┐
          │   MANAGER TI      │     │  MANAGER KEUANGAN│
          │   (TACTICAL)      │     │    (SUPPORT)     │
          │                   │     │                  │
          │ • Framework Impl  │     │ • Budget Control │
          │ • Risk Management │     │ • ROI Tracking   │
          │ • KPI Monitoring  │     └──────────────────┘
          └─────────┬─────────┘
                    │
       ┌────────────┼────────────┐
       │            │            │
┌──────▼──────┐ ┌──▼─────────┐ ┌─▼────────────┐
│  STAFF TI   │ │ STAFF TI │ │  STAFF TI  │
│(OPERATIONAL)│ │  (OPS)   │ │  (SUPPORT) │
│             │ │          │ │            │
│• Daily Ops  │ │• Backup  │ │• Helpdesk  │
│• Monitoring │ │• Security│ │• Training  │
│• Incident   │ │• Network │ │• Doc       │
└─────────────┘ └──────────┘ └────────────┘

═══════════════════════════════════════════════════════════════════════════
RACI MATRIX - KEY PROCESSES
═══════════════════════════════════════════════════════════════════════════

Proses / Aktivitas                 │ Direktur │Manager TI│ Staff TI │Finance
───────────────────────────────────┼──────────┼──────────┼──────────┼────────
1. Penetapan Kebijakan TI          │    A     │    R     │    C     │   I
2. Risk Assessment & Mitigation    │    A     │    R     │    C     │   I
3. Budget Approval TI              │    A     │    R     │    I     │   C
4. Implementasi Framework COBIT    │    I     │    A/R   │    R     │   I
5. Monitoring & Reporting KPI      │    I     │    A     │    R     │   C
6. Backup & Disaster Recovery      │    I     │    A     │    R     │   I
7. Security & Access Control       │    C     │    A     │    R     │   I
8. Incident Management             │    I     │    A     │    R     │   I
9. Change Management               │    A     │    R     │    R     │   C
10. Internal Audit IT Governance   │    A     │    C     │    I     │   C
11. Training & Skill Development   │    A     │    R     │    C     │   C
12. Vendor & Contract Management   │    A     │    R     │    C     │   C

───────────────────────────────────────────────────────────────────────────
Keterangan:
  R = Responsible (Pelaksana)        A = Accountable (Penanggung Jawab)
  C = Consulted (Konsultasi)         I = Informed (Informasi)
───────────────────────────────────────────────────────────────────────────

Escalation Path:
  Level 1: Staff TI (Incident Response Time: <2 jam)
     ↓
  Level 2: Manager TI (Critical Issues: <4 jam)
     ↓
  Level 3: Direktur (Strategic Decisions: <24 jam)

═══════════════════════════════════════════════════════════════════════════
```

Sumber: (Hasil Penelitian, 2025)  
**Gambar 3. Struktur Governance dan RACI Matrix SATRIAMART**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   FRAMEWORK TATA KELOLA TI SATRIAMART                   │
│                         (COBIT 2019 Based)                              │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  LAYER 1: GOVERNANCE STRUCTURE                                          │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 │
│  │   Direktur   │──│  Manager TI  │──│   Staff TI   │                 │
│  │  (Strategic) │  │   (Tactical) │  │ (Operational)│                 │
│  └──────────────┘  └──────────────┘  └──────────────┘                 │
│         │                  │                  │                         │
│         └──────────────────┴──────────────────┘                         │
│                    RACI Matrix                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  LAYER 2: COBIT 2019 DOMAINS                                            │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐       │
│  │   EDM03    │  │   APO12    │  │   DSS01    │  │   MEA01    │       │
│  │   Ensure   │  │   Manage   │  │   Manage   │  │  Monitor   │       │
│  │    Risk    │  │    Risk    │  │ Operations │  │ Evaluate & │       │
│  │Optimisation│  │            │  │            │  │   Assess   │       │
│  └────────────┘  └────────────┘  └────────────┘  └────────────┘       │
└─────────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  LAYER 3: FIVE KEY COMPONENTS                                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐     │
│  │  1. Policy & Procedure Framework                             │     │
│  │     • Risk Management Policy  • Security Policy              │     │
│  │     • Backup & Recovery       • Change Management            │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐     │
│  │  2. Risk Management Framework                                │     │
│  │     • Risk Register  • Risk Assessment  • Mitigation Plan    │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐     │
│  │  3. Performance Management                                   │     │
│  │     • KPI Dashboard  • Monitoring Tools  • Reporting         │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐     │
│  │  4. Operational Excellence                                   │     │
│  │     • SOP Documentation  • Incident Management  • ITSM       │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐     │
│  │  5. Continuous Improvement                                   │     │
│  │     • Review & Audit  • Lessons Learned  • Optimization      │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  OUTPUT: MATURITY LEVEL 1.2 → 3.0 (Managed)                             │
│  • Penurunan Insiden TI: 60%                                            │
│  • IT-Business Alignment: 75%                                           │
│  • Optimalisasi Resource: 40%                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

Sumber: (Hasil Penelitian, 2025)  
**Gambar 1. Framework Tata Kelola TI SATRIAMART Berbasis COBIT 2019**

Tabel 9 menunjukkan control objectives dan key performance indicators untuk setiap domain.

**Tabel 9. Control Objectives dan KPI per Domain**

| Domain | Control Objective | KPI/Metrik | Target (12 Bulan) | Target (24 Bulan) |
|--------|-------------------|------------|-------------------|-------------------|
| EDM03 | Framework manajemen risiko disetujui dan dioperasionalkan | % risiko yang memiliki owner dan rencana mitigasi | 60% | 90% |
| EDM03 | Toleransi risiko TI diselaraskan dengan toleransi organisasi | Jumlah risiko yang melampaui toleransi | < 5 | < 2 |
| APO12 | Risk register dipelihara dan diperbarui | Frekuensi update risk register | Bulanan | Bulanan |
| APO12 | Proses mitigasi risiko diimplementasikan | % risiko critical yang dimitigasi | 70% | 95% |
| DSS01 | SOP operasional TI terdokumentasi lengkap | % proses yang memiliki SOP | 75% | 100% |
| DSS01 | Backup dan recovery terautomasi | Frekuensi backup berhasil | 95% | 99% |
| MEA01 | KPI TI ditetapkan dan dimonitor | Jumlah KPI yang ditrack | 10 | 20 |
| MEA01 | Dashboard monitoring tersedia | Update frequency dashboard | Mingguan | Real-time |

Sumber: (Hasil Penelitian, 2025)

### Roadmap Implementasi

Roadmap implementasi dirancang dalam empat fase selama 18–24 bulan: Quick Wins (Bulan 1–3), Short-term (Bulan 4–9), Medium-term (Bulan 10–18), dan Long-term (Bulan 19–24). Setiap fase memiliki fokus, deliverables, dan resource requirements yang spesifik. Gambar 2 menunjukkan visualisasi roadmap implementasi dengan timeline dan deliverables utama setiap fase.

```
ROADMAP IMPLEMENTASI FRAMEWORK TATA KELOLA TI SATRIAMART (18-24 Bulan)

═══════════════════════════════════════════════════════════════════════════
Bulan:  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
═══════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────┐
│ FASE 1: QUICK WINS (Bulan 1-3)                    Maturity: 1.2 → 1.7  │
├─────────────────────────────────────────────────────────────────────────┤
│ ████████████                                                            │
│                                                                         │
│ Deliverables:                                                           │
│ • Risk Register (20 risiko prioritas)                                  │
│ • Automated Backup untuk sistem kritikal                               │
│ • RACI Matrix & Roles Definition                                       │
│ • SOP untuk 5 proses operasional kritikal                              │
│ • Dashboard Monitoring sederhana                                       │
│                                                                         │
│ Fokus Domain: APO12, DSS01                                              │
│ Budget: Rp 60 juta                                                      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ FASE 2: SHORT-TERM (Bulan 4-9)                    Maturity: 1.7 → 2.2  │
├─────────────────────────────────────────────────────────────────────────┤
│             ████████████████████████                                    │
│                                                                         │
│ Deliverables:                                                           │
│ • Kebijakan Manajemen Risiko TI (approved)                             │
│ • Risk Assessment Quarterly                                            │
│ • Upgrade Server & Load Balancing                                      │
│ • Training COBIT 2019 & Risk Management                                │
│ • Change Management Procedure                                          │
│                                                                         │
│ Fokus Domain: EDM03, APO12, DSS01                                       │
│ Budget: Rp 120 juta                                                     │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ FASE 3: MEDIUM-TERM (Bulan 10-18)                 Maturity: 2.2 → 2.6  │
├─────────────────────────────────────────────────────────────────────────┤
│                         ████████████████████████████████                │
│                                                                         │
│ Deliverables:                                                           │
│ • Identity Access Management (IAM)                                     │
│ • Disaster Recovery Plan & Testing                                     │
│ • KPI TI integrated dengan BSC                                         │
│ • ITSM Tools (Ticketing & Knowledge Base)                              │
│ • Internal IT Governance Audit #1                                      │
│                                                                         │
│ Fokus Domain: EDM03, DSS01, MEA01                                       │
│ Budget: Rp 130 juta                                                     │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ FASE 4: LONG-TERM (Bulan 19-24)                   Maturity: 2.6 → 3.0  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                 ████████████████        │
│                                                                         │
│ Deliverables:                                                           │
│ • Process Optimization (berdasarkan audit)                             │
│ • Predictive Analytics untuk Risk Management                           │
│ • ISO 27001 Certification (optional)                                   │
│ • Knowledge Transfer & Documentation Lengkap                           │
│ • Final Maturity Assessment (validasi target 3.0)                      │
│                                                                         │
│ Fokus Domain: ALL (EDM03, APO12, DSS01, MEA01)                          │
│ Budget: Rp 70 juta                                                      │
└─────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════
KPI Tracking:
───────────────────────────────────────────────────────────────────────────
• Insiden TI:           47 → 35 → 25 → 15 → <10 (Target: -60%)
• IT-Business Align:    37% → 45% → 55% → 65% → 75%
• Resource Utilization: 45% → 55% → 65% → 75% → 85%
• MTTR:                 3.3h → 2.8h → 2.3h → 1.8h → <2h
═══════════════════════════════════════════════════════════════════════════

Total Budget: Rp 380 juta  |  Expected ROI: 200% (3 tahun)
```

Sumber: (Hasil Penelitian, 2025)  
**Gambar 2. Roadmap Implementasi Framework Tata Kelola TI (18-24 Bulan)**

**Fase 1: Quick Wins (Bulan 1–3)**
Fokus: Perbaikan cepat dengan dampak tinggi dan effort rendah. Deliverables mencakup: (1) Dokumentasi risk register awal dengan 20 risiko prioritas; (2) Implementasi automated backup untuk sistem kritikal; (3) Penetapan RACI matrix untuk roles & responsibilities TI; (4) Penyusunan SOP untuk 5 proses operasional kritikal; dan (5) Setup dashboard monitoring sederhana.

**Fase 2: Short-term (Bulan 4–9)**
Fokus: Implementasi framework dasar dan peningkatan kapabilitas. Deliverables mencakup: (1) Pengesahan kebijakan manajemen risiko TI oleh Direktur; (2) Implementasi risk assessment berkala (quarterly); (3) Upgrade infrastruktur server dan implementasi load balancing; (4) Pelatihan tim TI tentang COBIT 2019 dan risk management; dan (5) Implementasi change management procedure.

**Fase 3: Medium-term (Bulan 10–18)**
Fokus: Optimalisasi proses dan peningkatan maturity level. Deliverables mencakup: (1) Implementasi Identity Access Management (IAM); (2) Disaster Recovery Plan (DRP) dan testing berkala; (3) Integrasi KPI TI dengan balanced scorecard organisasi; (4) Implementasi ITSM tools untuk ticketing dan knowledge base; dan (5) Audit internal tata kelola TI pertama.

**Fase 4: Long-term (Bulan 19–24)**
Fokus: Continuous improvement dan pencapaian maturity level 3,0. Deliverables mencakup: (1) Optimalisasi proses berdasarkan hasil audit; (2) Implementasi predictive analytics untuk risk management; (3) Sertifikasi ISO 27001 (jika diperlukan); (4) Knowledge transfer lengkap dan dokumentasi comprehensive; dan (5) Assessment maturity level final untuk validasi pencapaian target.

Tabel 10 menunjukkan proyeksi peningkatan maturity level untuk setiap fase implementasi.

**Tabel 10. Proyeksi Peningkatan Maturity Level per Fase**

| Domain | Baseline | Fase 1 (M3) | Fase 2 (M9) | Fase 3 (M18) | Fase 4 (M24) | Target |
|--------|----------|-------------|-------------|--------------|--------------|--------|
| EDM03 | 1,0 | 1,5 | 2,0 | 2,5 | 3,0 | 3,0 |
| APO12 | 1,2 | 1,7 | 2,2 | 2,7 | 3,0 | 3,0 |
| DSS01 | 1,5 | 2,0 | 2,5 | 2,8 | 3,0 | 3,0 |
| MEA01 | 1,0 | 1,5 | 2,0 | 2,5 | 3,0 | 3,0 |
| **Rata-rata** | **1,2** | **1,7** | **2,2** | **2,6** | **3,0** | **3,0** |

Sumber: (Hasil Penelitian, 2025)

### Estimasi Biaya dan Return on Investment (ROI)

Estimasi biaya implementasi framework tata kelola TI selama 24 bulan adalah Rp 380 juta, dengan rincian: Infrastructure upgrade (Rp 120 juta), Software & Tools (Rp 80 juta), Training & Certification (Rp 60 juta), Consulting & Support (Rp 80 juta), dan Contingency 10% (Rp 40 juta).

Proyeksi penghematan dan manfaat finansial mencakup: (1) Pengurangan biaya downtime sebesar Rp 150 juta/tahun (asumsi downtime berkurang 60% × rata-rata biaya downtime Rp 250 juta/tahun); (2) Pengurangan biaya maintenance reaktif sebesar Rp 100 juta/tahun; (3) Optimalisasi utilisasi aset TI menghemat Rp 50 juta/tahun; dan (4) Peningkatan produktivitas operasional setara Rp 80 juta/tahun.

Total manfaat finansial tahunan diproyeksikan Rp 380 juta, sehingga ROI dapat tercapai dalam 12 bulan (payback period). ROI 3 tahun diproyeksikan mencapai 200%, dengan NPV (Net Present Value) sebesar Rp 760 juta dan IRR (Internal Rate of Return) sebesar 78%.

### Pembahasan

Hasil penelitian ini menunjukkan bahwa tingkat kematangan tata kelola TI SATRIAMART berada pada level yang sangat rendah (1,2 dari skala 5), yang konsisten dengan fenomena yang diamati pada perusahaan retail skala menengah di Indonesia. Temuan ini sejalan dengan penelitian Ramadhan dan Ramadhan (2025) yang mengidentifikasi bahwa UMKM di Indonesia cenderung memiliki maturity level IT governance di bawah 2,0 karena keterbatasan resources dan awareness terhadap pentingnya tata kelola TI yang terstruktur.

Domain EDM03 (Ensure Risk Optimisation) dan MEA01 (Monitor, Evaluate and Assess Performance) memiliki maturity level terendah (1,0), mengindikasikan bahwa aspek strategis tata kelola TI belum menjadi prioritas manajemen. Hal ini kontras dengan penelitian Agustriani (2024) pada perusahaan manufaktur yang lebih besar, dimana domain EDM03 dan APO12 sudah mencapai level 2,5 karena regulatory pressure dan kompleksitas operasional yang lebih tinggi. Perbedaan ini menunjukkan bahwa ukuran dan kompleksitas organisasi memengaruhi prioritas implementasi IT governance.

Analisis gap mengidentifikasi bahwa kesenjangan terbesar berada pada aspek manajemen risiko (gap 2,0 untuk EDM03 dan 1,8 untuk APO12), yang merupakan area kritis mengingat tingginya frekuensi insiden TI (47 insiden dalam 6 bulan). Penelitian Afifah et al. (2023) menekankan bahwa implementasi domain-specific COBIT 2019 pada perusahaan manufaktur harus memprioritaskan area dengan gap terbesar untuk memaksimalkan dampak perbaikan. Oleh karena itu, roadmap implementasi yang dirancang dalam penelitian ini menempatkan manajemen risiko sebagai prioritas utama pada fase Quick Wins dan Short-term.

Tingkat keselarasan TI-bisnis yang rendah (37%) menjadi perhatian serius karena mengindikasikan bahwa investasi TI belum optimal dalam mendukung tujuan bisnis strategis. Thehawijaya dan Fajar (2024) menemukan bahwa perusahaan manufaktur otomotif dengan IT-business alignment di bawah 50% cenderung mengalami pemborosan investasi TI hingga 35%. Temuan ini memperkuat urgensi implementasi framework tata kelola TI yang dapat menyelaraskan strategi TI dengan prioritas bisnis melalui Goals Cascade COBIT 2019.

Analisis risiko mengidentifikasi kehilangan data dan downtime sistem sebagai risiko dengan prioritas tertinggi (skor 20), yang sejalan dengan temuan Agustriani (2024) bahwa manajemen risiko TI pada perusahaan retail dan manufaktur di Indonesia harus fokus pada business continuity dan data protection. Implementasi automated backup dan disaster recovery plan pada fase Quick Wins dirancang untuk memitigasi risiko-risiko kritis tersebut dengan cepat.

Inefisiensi penggunaan anggaran TI, khususnya overbudget 20,8% pada maintenance reaktif, mengonfirmasi hipotesis bahwa tata kelola TI yang buruk berdampak langsung pada pemborosan finansial. Elina (2021) membuktikan bahwa implementasi framework COBIT dapat meningkatkan efisiensi organisasi hingga 40% melalui optimalisasi proses dan pengurangan aktivitas non-value-added. Roadmap implementasi yang dirancang dalam penelitian ini bertujuan untuk mengalihkan fokus dari reactive maintenance ke preventive maintenance, yang diproyeksikan menghemat Rp 100 juta per tahun.

Framework tata kelola TI yang dirancang mengadopsi pendekatan bertahap (phased approach) yang terbukti efektif pada penelitian Aziz et al. (2023) tentang implementasi domain APO COBIT 2019. Pendekatan ini memungkinkan SATRIAMART untuk mencapai quick wins pada bulan ke-3, membangun momentum perubahan, dan secara bertahap meningkatkan maturity level tanpa mengganggu operasional bisnis.

Proyeksi ROI sebesar 200% dalam 3 tahun dengan payback period 12 bulan menunjukkan bahwa investasi pada IT governance memberikan business value yang signifikan. IT Governance Institute (2021) menyatakan bahwa organisasi dengan maturity level managed (3,0) dapat meningkatkan nilai bisnis hingga 20% melalui pengelolaan risiko yang lebih baik dan pemanfaatan sumber daya TI yang optimal. Proyeksi ini realistis mengingat potensi penghematan dari pengurangan downtime (Rp 150 juta/tahun) dan optimalisasi maintenance (Rp 100 juta/tahun).

Penelitian ini memberikan kontribusi akademis dengan mengisi kesenjangan literatur implementasi COBIT 2019 pada perusahaan retail skala menengah di Indonesia. Berbeda dengan penelitian Hapsari (2018) yang menggunakan COBIT 5 versi lama, penelitian ini mengadopsi COBIT 2019 dengan design factor yang lebih adaptif terhadap karakteristik SATRIAMART. Model assessment maturity dan roadmap implementasi yang dikembangkan dapat direplikasi oleh peneliti lain dan diadaptasi oleh perusahaan retail sejenis.

Keterbatasan penelitian ini mencakup: (1) ruang lingkup terbatas pada satu studi kasus sehingga generalisasi hasil memerlukan validasi lebih lanjut pada konteks organisasi yang berbeda; (2) assessment dilakukan pada satu titik waktu (snapshot) sehingga belum menangkap dinamika perubahan maturity level; dan (3) proyeksi ROI didasarkan pada asumsi yang perlu divalidasi melalui implementasi aktual. Penelitian lanjutan dapat melakukan longitudinal study untuk memvalidasi efektivitas roadmap implementasi dan mengukur peningkatan maturity level secara empiris.

---

## KESIMPULAN

Berdasarkan hasil assessment dan analisis yang telah dilakukan, penelitian ini menghasilkan beberapa kesimpulan penting. Pertama, tingkat kematangan tata kelola TI SATRIAMART berada pada level 1,2 dari skala 5 (ad-hoc/initial), dengan domain EDM03 (Ensure Risk Optimisation) dan MEA01 (Monitor, Evaluate and Assess Performance) memiliki maturity level terendah (1,0). Kondisi ini mengindikasikan bahwa proses-proses TI masih bersifat reaktif, tidak terdokumentasi dengan baik, dan belum memiliki standar yang konsisten.

Kedua, analisis gap mengidentifikasi kesenjangan rata-rata 1,8 level antara kondisi saat ini dengan target maturity level 3,0 (managed). Kesenjangan terbesar berada pada aspek manajemen risiko (gap 2,0 untuk EDM03 dan 1,8 untuk APO12), monitoring kinerja (gap 2,0 untuk MEA01), dan operasional TI (gap 1,5 untuk DSS01). Faktor kritis yang memengaruhi capaian maturity level mencakup komitmen manajemen puncak, ketersediaan sumber daya, budaya organisasi yang adaptif, kemampuan tim TI, dan dukungan teknologi yang memadai.

Ketiga, analisis risiko mengidentifikasi 23 risiko TI dengan 5 risiko prioritas tertinggi: kehilangan data akibat kegagalan backup, downtime sistem order, pelanggaran data pelanggan, ketergantungan pada key person, dan ketidakselarasan investasi TI dengan prioritas bisnis. Analisis insiden menunjukkan 47 insiden TI dalam periode 6 bulan dengan total downtime 156 jam dan MTTR rata-rata 3,3 jam. Tingkat keselarasan TI-bisnis yang rendah (37%) mengindikasikan bahwa investasi TI belum optimal dalam mendukung tujuan bisnis strategis.

Keempat, framework tata kelola TI yang dirancang mencakup lima komponen utama: governance structure, policy & procedure, risk management framework, performance management, dan continuous improvement. Framework ini difokuskan pada empat domain COBIT 2019 (EDM03, APO12, DSS01, MEA01) dengan 8 control objectives dan KPI yang terukur.

Kelima, roadmap implementasi dirancang dalam empat fase selama 18–24 bulan: Quick Wins (Bulan 1–3), Short-term (Bulan 4–9), Medium-term (Bulan 10–18), dan Long-term (Bulan 19–24). Implementasi roadmap ini diproyeksikan dapat meningkatkan maturity level dari 1,2 menjadi 3,0, mengurangi insiden TI sebesar 60%, meningkatkan keselarasan TI-bisnis sebesar 75%, dan mengoptimalkan utilisasi sumber daya TI sebesar 40%.

Keenam, estimasi biaya implementasi selama 24 bulan adalah Rp 380 juta dengan proyeksi ROI 200% dalam 3 tahun dan payback period 12 bulan. Manfaat finansial tahunan diproyeksikan mencapai Rp 380 juta melalui pengurangan biaya downtime, optimalisasi maintenance, efisiensi utilisasi aset, dan peningkatan produktivitas operasional.

Penelitian ini merekomendasikan SATRIAMART untuk segera mengimplementasikan framework tata kelola TI yang telah dirancang dengan memprioritaskan quick wins pada aspek manajemen risiko dan backup/recovery. Komitmen manajemen puncak dan alokasi sumber daya yang memadai menjadi kunci keberhasilan transformasi tata kelola TI. Monitoring dan evaluasi berkala perlu dilakukan untuk memastikan pencapaian target maturity level sesuai roadmap yang telah ditetapkan.

Untuk penelitian lanjutan, disarankan untuk melakukan longitudinal study guna memvalidasi efektivitas roadmap implementasi dan mengukur peningkatan maturity level secara empiris. Penelitian komparatif pada perusahaan retail sejenis juga dapat dilakukan untuk menguji generalisasi model assessment dan framework yang telah dikembangkan. Eksplorasi lebih lanjut terhadap faktor-faktor sukses implementasi IT governance pada konteks UMKM dan perusahaan retail skala menengah di Indonesia juga menjadi area penelitian yang menarik untuk dieksplorasi.

---

## REFERENSI

Afifah, U. F., Adam, S., & Marfuah, M. (2023). Pemetaan Tata Kelola Teknologi Informasi melalui Desain Faktor Framework COBIT 2019 pada Perusahaan Manufaktur X. *Jurnal Sistem Informasi dan Teknologi*, 15(2), 145-152.

Agustriani, N. H. P. (2024). Analisis Manajemen Risiko Teknologi Informasi pada PT XYZ (Perusahaan Manufacturing) menggunakan Framework COBIT 2019 dengan Domain EDM03 dan APO12. *Jurnal Teknik Informatika*, 12(1), 78-89.

Aziz, M. A., Kusrini, K., & Nasiri, A. (2023). Perancangan Tata Kelola Teknologi Informasi Menggunakan Framework COBIT 2019 Domain Align Plan and Organize. *Jurnal Informatika dan Komputer*, 18(3), 234-245.

Elina, R. (2021). Evaluasi Implementasi Tata Kelola Teknologi Informasi Berdasarkan Framework COBIT. *Jurnal Manajemen Sistem Informasi*, 9(2), 112-125.

Hapsari, S. W. (2018). Implementasi Tata Kelola Teknologi Informasi Berdasarkan Framework COBIT 5 Pada PT Krakatau Tirta Industri. *Jurnal TEKNOINFO*, 12(1), 45-52.

ISACA. (2019). *COBIT 2019 Framework: Introduction and Methodology*. Rolling Meadows, IL: ISACA.

IT Governance Institute. (2021). *Global Status Report on IT Governance 2021*. Rolling Meadows, IL: IT Governance Institute.

Ramadhan, R. P., & Ramadhan, V. P. (2025). Analisis Tata Kelola TI untuk Pembukuan Digital UMKM dengan COBIT 2019: Studi Kasus Taylor Cahaya. *Jurnal Teknologi Informasi dan Bisnis*, 14(1), 67-78.

Riyadli, H., & Arliyana, A. (2022). Analisis Perencanaan Dan Implementasi Teknologi Informasi Menggunakan Framework COBIT Pada Usaha Toko Plastik. *Jurnal Sistem Informasi Bisnis*, 10(2), 156-165.

Thehawijaya, H. B., & Fajar, A. N. (2024). Evaluasi Tata Kelola Teknologi Informasi di Perusahaan Manufaktur Otomotif: Pendekatan Menggunakan Kerangka Kerja COBIT 2019. *Jurnal Teknik Industri*, 16(1), 89-102.
