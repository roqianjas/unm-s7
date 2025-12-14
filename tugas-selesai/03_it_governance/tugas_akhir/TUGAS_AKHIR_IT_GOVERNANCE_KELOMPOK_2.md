Vol. XX, No. X Desember 2025 | DOI: 10.33480/pilar.vXX.xxxx

# ASESMEN DAN IMPLEMENTASI TATA KELOLA TI PADA SATRIAMART MENGGUNAKAN COBIT 2019

**Roki Anjas¹*; Fahruroji²; Susanto³**

Program Studi Sistem Informasi¹·²·³  
Universitas Nusa Mandiri, Jakarta, Indonesia¹·²·³  
https://www.nusamandiri.ac.id¹·²·³  
11250066@nusamandiri.ac.id¹*; 11250085@nusamandiri.ac.id²; 11250068@nusamandiri.ac.id³  
(*) Corresponding Author

![Lisensi Creative Commons](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)

Karya ini didistribusikan di bawah Lisensi Creative Commons Attribution-NonCommercial 4.0 International.

---

## Abstract

*The rapid development of information technology demands organizations to implement structured IT governance to optimize business value and manage risks effectively. SATRIAMART, a retail company specializing in acrylic decorations and accessories, faces challenges in managing information technology with a maturity level of only 1.2 on a scale of 5 (ad-hoc/initial). This research aims to assess the current maturity level of IT governance and design a comprehensive implementation roadmap using the COBIT 2019 framework. The research methodology combines maturity assessment, gap analysis, and risk-based control testing on four domains: EDM03, APO12, DSS01, and MEA01. Data was collected through documentation analysis, interviews, and observations conducted from May to October 2025. The results show that the current maturity level is 1.2 with critical gaps in risk management, resource optimization, and IT-business alignment. The proposed framework and 18-24 month implementation roadmap aims to increase the maturity level to 3.0 (managed), reduce IT incidents by 60%, improve IT-business alignment by 75%, and optimize IT resource utilization by 40%. This research contributes to the literature on COBIT 2019 implementation in medium-scale retail companies in Indonesia and provides a practical model that can be adapted by similar organizations.*

**Keywords:** cobit 2019, gap analysis, it governance, maturity assessment, risk management.

---

## Abstrak

Perkembangan teknologi informasi yang pesat menuntut organisasi untuk menerapkan tata kelola TI yang terstruktur guna mengoptimalkan nilai bisnis dan mengelola risiko secara efektif. SATRIAMART, perusahaan ritel yang bergerak di bidang dekorasi dan aksesoris akrilik, menghadapi tantangan dalam mengelola teknologi informasi dengan tingkat kematangan hanya 1,2 dari skala 5 (tidak formal/*ad-hoc*). Penelitian ini bertujuan untuk melakukan asesmen tingkat kematangan tata kelola TI saat ini dan merancang peta jalan implementasi yang komprehensif menggunakan kerangka kerja COBIT 2019. Metodologi penelitian mengombinasikan asesmen kematangan, analisis kesenjangan, dan pengujian kontrol berbasis risiko pada empat domain: EDM03, APO12, DSS01, dan MEA01. Data dikumpulkan melalui analisis dokumentasi, wawancara, dan observasi yang dilakukan pada periode Mei–Oktober 2025. Hasil penelitian menunjukkan bahwa tingkat kematangan saat ini berada pada level 1,2 dengan kesenjangan kritis dalam manajemen risiko, optimalisasi sumber daya, dan keselarasan TI-bisnis. Kerangka kerja yang dirancang dan peta jalan implementasi selama 18–24 bulan bertujuan untuk meningkatkan tingkat kematangan menjadi 3,0 (terkelola/*managed*), mengurangi insiden TI sebesar 60%, meningkatkan keselarasan TI-bisnis sebesar 75%, dan mengoptimalkan utilisasi sumber daya TI sebesar 40%. Penelitian ini berkontribusi pada literatur implementasi COBIT 2019 di perusahaan ritel skala menengah di Indonesia dan memberikan model praktis yang dapat diadaptasi oleh organisasi sejenis.

**Kata Kunci:** analisis kesenjangan, asesmen kematangan, cobit 2019, manajemen risiko, tata kelola ti.

---

## PENDAHULUAN

Di era transformasi digital, teknologi informasi (TI) telah menjadi tulang punggung operasional dan strategi bisnis perusahaan. Namun, pemanfaatan TI yang tidak dikelola dengan baik dapat menimbulkan risiko signifikan seperti ketidakselarasan strategi TI dengan tujuan bisnis, inefisiensi penggunaan sumber daya, dan kerentanan terhadap ancaman keamanan informasi. Menurut IT Governance Institute (2021), tata kelola TI yang efektif dapat meningkatkan nilai bisnis hingga 20% melalui pengelolaan risiko yang lebih baik dan pemanfaatan sumber daya TI yang optimal. Penelitian Afifah, Adam, dan Marfuah (2023) pada perusahaan manufaktur di Indonesia menunjukkan bahwa implementasi framework COBIT 2019 mampu meningkatkan efektivitas pemetaan tata kelola TI dan menyelaraskan strategi TI dengan objektif bisnis organisasi.

Kerangka kerja tata kelola TI seperti COBIT 2019 telah terbukti memberikan panduan komprehensif dalam mengelola dan mengatur TI secara terstruktur. ISACA (2019) menegaskan bahwa COBIT 2019 menyediakan faktor desain (*design factor*) yang dapat disesuaikan dengan karakteristik organisasi, termasuk industri manufaktur dan ritel. Hasil tinjauan literatur sistematis (*systematic literature review*) menunjukkan bahwa 100% penelitian tata kelola TI pada perusahaan manufaktur Indonesia menggunakan kerangka kerja COBIT, dengan 62% mengadopsi versi terbaru COBIT 2019 karena kemampuannya dalam memberikan pendekatan spesifik domain (*domain-specific*) yang lebih fleksibel dan adaptif terhadap kebutuhan bisnis (Aziz, Kusrini, & Nasiri, 2023; Thehawijaya & Fajar, 2024).

SATRIAMART merupakan perusahaan yang bergerak di bidang dekorasi dan aksesoris akrilik dengan produk unggulan meliputi nomor rumah akrilik, *signage* akrilik, papan nama akrilik, dan aksesoris dekorasi *custom*. Sebagai perusahaan ritel yang sedang berkembang, SATRIAMART menghadapi tantangan dalam mengelola teknologi informasi secara efektif untuk mendukung pertumbuhan bisnisnya. Berdasarkan asesmen awal, tingkat kematangan (*maturity level*) tata kelola TI SATRIAMART masih berada pada level 1,2 dari skala 5 (tidak formal/*ad-hoc*/*initial*), di mana proses-proses TI belum terdokumentasi dengan baik dan masih bersifat reaktif.

Kondisi ini menimbulkan beberapa permasalahan kritis: pertama, tidak adanya keselarasan antara strategi TI dengan strategi bisnis mengakibatkan investasi TI tidak memberikan nilai optimal bagi pencapaian tujuan organisasi. Kedua, manajemen risiko TI yang belum terstruktur meningkatkan potensi kerugian akibat downtime sistem, kehilangan data, atau security breach yang dapat berdampak pada reputasi dan kepercayaan pelanggan. Ketiga, penggunaan sumber daya TI yang tidak efisien menyebabkan pemborosan anggaran dan duplikasi fungsi sistem. Keempat, tidak adanya mekanisme monitoring dan evaluasi kinerja TI menyulitkan manajemen dalam mengambil keputusan strategis terkait investasi teknologi.

Permasalahan yang dihadapi SATRIAMART sejalan dengan temuan penelitian Agustriani (2024) pada perusahaan manufaktur di Indonesia, yang mengidentifikasi bahwa manajemen risiko TI merupakan area kritis yang memerlukan perhatian khusus melalui implementasi domain EDM03 (*Ensure Risk Optimisation*) dan APO12 (*Manage Risk*) COBIT 2019. Studi Ramadhan dan Ramadhan (2025) pada UMKM juga menunjukkan bahwa transformasi digital tanpa kerangka kerja tata kelola TI yang memadai dapat menghambat efektivitas sistem dan meningkatkan risiko operasional. Riyadli dan Arliyana (2022) menekankan pentingnya perencanaan dan implementasi TI yang terstruktur pada usaha skala menengah untuk menghindari pemborosan investasi teknologi. Penelitian Elina (2021) membuktikan bahwa evaluasi implementasi tata kelola TI menggunakan kerangka kerja COBIT dapat meningkatkan efisiensi organisasi secara signifikan.

Meskipun penelitian tentang implementasi COBIT 2019 pada perusahaan manufaktur telah cukup banyak dilakukan, namun terdapat kesenjangan dalam penerapannya pada perusahaan ritel skala menengah yang fokus pada produk *custom* dan dekorasi. Mayoritas penelitian yang ada (50%) terbatas pada studi kasus tunggal (*single case study*) dengan fokus domain tertentu (Afifah dkk., 2023; Aziz dkk., 2023), sementara implementasi komprehensif yang mencakup asesmen kematangan, manajemen risiko, dan peta jalan implementasi masih terbatas, khususnya untuk sektor ritel dekorasi dan aksesoris.

Thehawijaya dan Fajar (2024) menyoroti bahwa pendekatan spesifik domain (*domain-specific*) sangat penting dalam implementasi COBIT 2019 pada perusahaan manufaktur, di mana domain APO (*Align, Plan, and Organize*) menjadi prioritas utama untuk perencanaan strategis TI. Namun, penelitian tersebut belum mengeksplorasi secara mendalam bagaimana kerangka kerja tersebut dapat diadaptasi untuk perusahaan ritel dengan karakteristik operasional yang berbeda dari manufaktur otomotif. Di sisi lain, Hapsari (2018) mengimplementasikan COBIT 5 pada PT Krakatau Tirta Industri namun menggunakan versi kerangka kerja yang sudah tidak terbaru dan kurang relevan dengan faktor desain (*design factor*) COBIT 2019 yang lebih adaptif.

Berdasarkan latar belakang tersebut, penelitian ini bertujuan untuk: (1) menganalisis tingkat kematangan tata kelola TI pada SATRIAMART menggunakan kerangka kerja COBIT 2019 dengan pendekatan analisis faktor desain (*design factor analysis*); (2) mengidentifikasi kesenjangan antara kondisi saat ini dengan target tingkat kematangan (*maturity level*) serta faktor kritis keberhasilan implementasi kerangka kerja tata kelola TI; dan (3) merancang kerangka kerja tata kelola TI dengan fokus domain EDM, APO, EDM03, dan APO12 serta menyusun peta jalan implementasi untuk meningkatkan tingkat kematangan dari tidak formal/*ad-hoc* (1,2) ke terkelola/*managed* (3,0). Penelitian ini diharapkan dapat memperkaya literatur implementasi COBIT 2019 pada perusahaan ritel skala menengah di Indonesia dan memberikan model asesmen kematangan tata kelola TI yang dapat direplikasi oleh peneliti lain serta diadaptasi oleh perusahaan ritel sejenis.

---

## BAHAN DAN METODE

Penelitian ini menggunakan pendekatan kualitatif dengan metode studi kasus untuk menganalisis tata kelola teknologi informasi pada SATRIAMART. Metode penelitian dirancang untuk menjawab tiga rumusan masalah utama: (1) tingkat kematangan tata kelola TI saat ini; (2) kesenjangan dan faktor kritis yang memengaruhi capaian tingkat kematangan (*maturity level*); dan (3) rekomendasi perbaikan dan peta jalan implementasi kerangka kerja COBIT 2019.

### Desain Penelitian

Penelitian ini mengombinasikan tiga metode analisis utama: Asesmen Kematangan (*Maturity Assessment*) COBIT 2019, Analisis Kesenjangan (*Gap Analysis*), dan Pengujian Kontrol Berbasis Risiko (*Risk-Based Control Testing*). Asesmen kematangan diperlukan untuk mengukur tingkat kematangan tata kelola TI saat ini (*baseline* level 1,2) dan memetakan target pencapaian (level 3,0). Analisis kesenjangan digunakan untuk mengidentifikasi kesenjangan antara kondisi eksisting dengan praktik terbaik (*best practice*) COBIT 2019. Pengujian kontrol berbasis risiko dipilih karena SATRIAMART menghadapi risiko signifikan terkait insiden TI, kehilangan data, dan *downtime* yang berdampak pada operasional bisnis. Kerangka kerja COBIT 2019 dipilih karena terbukti efektif untuk perusahaan ritel skala menengah di Indonesia dan dapat disesuaikan dengan karakteristik SATRIAMART.

### Sumber Data

Penelitian ini menggunakan data primer dan sekunder yang dikumpulkan selama periode Mei–Oktober 2025. Data primer diperoleh melalui wawancara mendalam dengan Direktur SATRIAMART, Manajer TI, dan Staf TI, serta observasi langsung terhadap proses operasional TI. Data sekunder bersumber dari dokumen kebijakan TI (jika tersedia), Prosedur Operasional Standar (*Standard Operating Procedure*/SOP) operasional TI, catatan (*log*) insiden dan *downtime* sistem, daftar risiko (*risk register*), data *backup* dan *recovery log*, dokumentasi kontrol akses pengguna, laporan anggaran dan investasi TI, inventaris aset TI, dokumen strategi bisnis periode 2025–2027, serta struktur organisasi dan deskripsi pekerjaan (*job description*).

Tabel 1 menunjukkan daftar lengkap sumber data yang digunakan dalam penelitian ini beserta periode pengumpulan, pemilik data, tingkat sensitivitas, dan status akses.

**Tabel 1. Daftar Sumber Data Penelitian**

| No | Nama Bahan | Sumber | Periode | Pemilik | Sensitivitas | Status Akses |
|----|------------|--------|---------|---------|--------------|--------------|
| 1 | Dokumen Kebijakan TI | Manajemen SATRIAMART | Versi 2025 | Direktur | Internal | Diperoleh |
| 2 | SOP Operasional TI | Tim TI | Versi 2025 | Manager TI | Internal | Diperoleh |
| 3 | Catatan Insiden & *Downtime* | Sistem *Ticketing* | Mei–Okt 2025 | Staf TI | Internal | Diperoleh |
| 4 | Daftar Risiko (*Risk Register*) | Manajemen | Q2-Q3 2025 | Manajer TI | Rahasia | Diperoleh |
| 5 | Data *Backup* & *Recovery* | Server | Mei–Okt 2025 | Staf TI | Internal | Diperoleh |
| 6 | Kontrol Akses Pengguna | Sistem | Oktober 2025 | Staf TI | Rahasia | Diperoleh |
| 7 | Anggaran & Investasi TI | Keuangan | Tahun 2025 | Keuangan | Rahasia | Diperoleh |
| 8 | Inventaris Aset TI | Basis Data | Oktober 2025 | Staf TI | Internal | Diperoleh |
| 9 | Strategi Bisnis | Manajemen | 2025-2027 | Direktur | Internal | Diperoleh |
| 10 | Struktur Organisasi | SDM | 2025 | Manajemen | Internal | Diperoleh |

Sumber: (Hasil Penelitian, 2025)

### Teknik Pengumpulan Data

Pengumpulan data dilakukan melalui tiga teknik utama. Pertama, analisis dokumentasi terhadap seluruh dokumen yang tercantum dalam Tabel 1 untuk memahami kondisi eksisting tata kelola TI SATRIAMART. Kedua, wawancara terstruktur dan semiterstruktur dengan pemangku kepentingan (*stakeholder*) kunci menggunakan instrumen asesmen COBIT 2019 yang telah disesuaikan dengan konteks SATRIAMART. Ketiga, observasi langsung terhadap proses operasional TI, mekanisme penanganan insiden, prosedur *backup* dan *recovery*, serta implementasi kontrol keamanan informasi.

### Instrumen Penelitian

Instrumen asesmen dikembangkan berdasarkan kerangka kerja COBIT 2019 dengan fokus pada empat domain prioritas: EDM03 (*Ensure Risk Optimisation*), APO12 (*Manage Risk*), DSS01 (*Manage Operations*), dan MEA01 (*Monitor, Evaluate and Assess Performance and Conformance*). Setiap domain dievaluasi menggunakan tingkat kapabilitas (*capability level*) COBIT 2019 dengan skala 0–5: Level 0 (*Incomplete*/tidak lengkap), Level 1 (*Performed*/dilakukan), Level 2 (*Managed*/terkelola), Level 3 (*Established*/mapan), Level 4 (*Predictable*/dapat diprediksi), dan Level 5 (*Optimizing*/optimal).

Tabel 2 menunjukkan matriks keterkaitan antara tujuan penelitian, data yang diperlukan, metode analisis, dan output yang diharapkan untuk memastikan traceability yang jelas.

**Tabel 2. Matriks Tujuan, Data, Metode, dan Output Penelitian**

| Tujuan | Data/Bahan | Alasan Relevansi | Metode | Output Diharapkan |
|--------|------------|------------------|---------|-------------------|
| Meningkatkan tingkat kematangan dari 1,2 ke 3,0 | Dokumentasi SOP TI, Daftar Risiko (*Risk Register*), Catatan Insiden 6 bulan | Menggambarkan kondisi tata kelola saat ini dan mengidentifikasi kesenjangan | Asesmen Kematangan (*Maturity Assessment*) COBIT 2019 & Analisis Kesenjangan (*Gap Analysis*) | Skor kematangan per domain, daftar kesenjangan, prioritas perbaikan |
| Menurunkan insiden TI sebesar 60% | Catatan insiden TI, Laporan waktu henti (*downtime*), Dokumentasi penanganan masalah | Mengidentifikasi pola insiden dan akar masalah | Asesmen Risiko (*Risk Assessment*) ISO 27005 & Analisis Akar Masalah (*Root Cause Analysis*) | Daftar risiko prioritas, rekomendasi mitigasi |
| Meningkatkan keselarasan TI-Bisnis 75% | Dokumen strategi bisnis, Rencana investasi TI, KPI bisnis dan TI | Mengevaluasi keselarasan (*alignment*) strategi TI dengan tujuan bisnis | Pemetaan COBIT 2019 (EDM & APO) & Kontrol Pembanding (*Benchmark Control*) | Matriks keselarasan, kesenjangan keselarasan, rekomendasi perbaikan |
| Optimalisasi sumber daya TI 40% | Data anggaran TI, Utilisasi sistem, Inventaris aset TI | Menganalisis efisiensi penggunaan sumber daya | Matriks RACI & Penelusuran Proses (*Process Walkthrough*) | Peta proses optimal, kejelasan peran, efisiensi biaya |

Sumber: (Hasil Penelitian, 2025)

### Teknik Analisis Data

Analisis data dilakukan melalui lima tahapan. Tahap pertama adalah asesmen kematangan (*maturity assessment*) untuk menilai tingkat kapabilitas (*capability level*) setiap domain berdasarkan Model Asesmen Proses (*Process Assessment Model*/PAM) COBIT 2019. Tahap kedua adalah analisis kesenjangan (*gap analysis*) untuk mengidentifikasi kesenjangan antara kondisi saat ini (*current state*) 1,2 dan kondisi yang diinginkan (*desired state*) 3,0. Tahap ketiga adalah asesmen risiko (*risk assessment*) menggunakan metode ISO 27005 untuk mengidentifikasi, menganalisis, dan mengevaluasi risiko TI. Tahap keempat adalah analisis akar masalah (*root cause analysis*) untuk mengidentifikasi akar masalah dari insiden TI yang terjadi. Tahap kelima adalah penyusunan peta jalan implementasi menggunakan pendekatan bertahap (*quick wins*, *short-term*, *medium-term*, *long-term*) dengan mempertimbangkan prioritas, ketersediaan sumber daya, dan dampak bisnis.

### Validitas dan Reliabilitas

Validitas penelitian dijamin melalui triangulasi data (dokumentasi, wawancara, observasi), triangulasi sumber (Direktur, Manager TI, Staff TI), dan peer review dengan dosen pembimbing. Reliabilitas dipastikan melalui penggunaan instrumen standar COBIT 2019, dokumentasi lengkap proses assessment, dan konsistensi metode scoring maturity level.

---

## HASIL DAN PEMBAHASAN

### Hasil Asesmen Tingkat Kematangan Tata Kelola TI

Berdasarkan asesmen yang dilakukan menggunakan kerangka kerja COBIT 2019 pada periode Mei–Oktober 2025, tingkat kematangan (*maturity level*) tata kelola TI SATRIAMART berada pada level 1,2 dari skala 5, yang termasuk dalam kategori tidak formal/*ad-hoc*/*initial*. Pada level ini, proses-proses TI masih bersifat reaktif, tidak terdokumentasi dengan baik, sangat bergantung pada pengetahuan individu, dan belum memiliki standar yang konsisten.

Tabel 3 menunjukkan hasil asesmen tingkat kematangan untuk setiap domain COBIT 2019 yang menjadi fokus penelitian.

**Tabel 3. Hasil Asesmen Tingkat Kematangan per Domain COBIT 2019**

| Domain | Nama Proses | Tingkat Kematangan Saat Ini | Tingkat Kematangan Target | Kesenjangan |
|--------|-------------|------------------------|----------------------|-----|
| EDM03 | Ensure Risk Optimisation | 1,0 | 3,0 | 2,0 |
| APO12 | Manage Risk | 1,2 | 3,0 | 1,8 |
| DSS01 | Manage Operations | 1,5 | 3,0 | 1,5 |
| MEA01 | Monitor, Evaluate and Assess Performance | 1,0 | 3,0 | 2,0 |
| **Rata-rata** | | **1,2** | **3,0** | **1,8** |

Sumber: (Hasil Penelitian, 2025)

Hasil asesmen menunjukkan bahwa domain EDM03 (*Ensure Risk Optimisation*) dan MEA01 (*Monitor, Evaluate and Assess Performance*) memiliki tingkat kematangan terendah (1,0), yang mengindikasikan bahwa kerangka kerja manajemen risiko belum disetujui dan dioperasionalkan secara formal, serta tidak ada mekanisme pemantauan dan evaluasi kinerja TI yang terstruktur. Domain APO12 (*Manage Risk*) berada pada level 1,2, di mana risiko TI dikelola secara tidak formal/*ad-hoc* tanpa daftar risiko (*risk register*) yang terdokumentasi. Domain DSS01 (*Manage Operations*) memiliki tingkat kematangan tertinggi (1,5) karena beberapa prosedur operasional dasar sudah mulai diterapkan meskipun belum terstandardisasi.

### Identifikasi Kesenjangan dan Faktor Kritis

Analisis kesenjangan (*gap analysis*) mengidentifikasi beberapa kesenjangan kritis antara kondisi saat ini dengan target tingkat kematangan (*maturity level*) 3,0 (terkelola/*managed*). Tabel 4 menunjukkan kesenjangan utama yang ditemukan pada setiap domain.

**Tabel 4. Identifikasi Kesenjangan (Gap) per Domain**

| Domain | Kesenjangan Utama | Dampak Bisnis | Prioritas |
|--------|-------------------|---------------|-----------|
| EDM03 | Tidak ada kerangka kerja manajemen risiko formal; Toleransi risiko belum didefinisikan; Risiko TI tidak memiliki pemilik (*owner*) yang jelas | Potensi kerugian tidak terukur; Keputusan investasi TI tidak berbasis risiko | Sangat Tinggi |
| APO12 | Daftar risiko (*risk register*) tidak ada; Tidak ada proses identifikasi risiko berkala; Mitigasi risiko bersifat reaktif | Insiden berulang; Waktu henti (*downtime*) tidak terprediksi; Biaya perbaikan tinggi | Sangat Tinggi |
| DSS01 | SOP operasional belum lengkap; Eskalasi masalah tidak terstruktur; Pencadangan (*backup*) dilakukan manual tidak terjadwal | Inkonsistensi layanan; Waktu pemulihan (*recovery time*) lama; Potensi kehilangan data | Tinggi |
| MEA01 | Tidak ada KPI untuk TI; Pelaporan kinerja tidak rutin; Tidak ada mekanisme perbaikan berkelanjutan (*continuous improvement*) | Kinerja TI tidak terukur; Keputusan tidak berbasis data (*data-driven*); Perbaikan tidak sistematis | Tinggi |

Sumber: (Hasil Penelitian, 2025)

Dari analisis kesenjangan tersebut, penelitian ini mengidentifikasi lima faktor kritis yang memengaruhi keberhasilan implementasi kerangka kerja tata kelola TI: (1) komitmen manajemen puncak; (2) ketersediaan sumber daya (SDM dan anggaran); (3) budaya organisasi yang adaptif terhadap perubahan; (4) kemampuan tim TI dalam mengadopsi kerangka kerja; dan (5) dukungan teknologi yang memadai.

### Analisis Risiko TI

Berdasarkan data catatan (*log*) insiden dan *downtime* periode Mei–Oktober 2025, penelitian ini mengidentifikasi 47 insiden TI dengan total *downtime* 156 jam. Tabel 5 menunjukkan kategori insiden dan frekuensi kejadian.

**Tabel 5. Kategori dan Frekuensi Insiden TI**

| Kategori Insiden | Frekuensi | Persentase | Total *Downtime* (Jam) | MTTR (Jam) |
|------------------|-----------|------------|----------------------|------------|
| Kegagalan Perangkat Keras | 12 | 25,5% | 48 | 4,0 |
| Kesalahan Perangkat Lunak | 18 | 38,3% | 54 | 3,0 |
| Masalah Jaringan | 8 | 17,0% | 32 | 4,0 |
| Insiden Keamanan | 3 | 6,4% | 12 | 4,0 |
| Kesalahan Manusia | 6 | 12,8% | 10 | 1,7 |
| **Total** | **47** | **100%** | **156** | **3,3** |

Sumber: (Hasil Penelitian, 2025)

Analisis akar masalah (*root cause*) terhadap insiden-insiden tersebut mengidentifikasi bahwa 68% insiden disebabkan oleh tidak adanya prosedur pemeliharaan preventif (*preventive maintenance*), 21% disebabkan oleh kurangnya pelatihan SDM TI, dan 11% disebabkan oleh keterbatasan infrastruktur. Waktu Rata-rata untuk Perbaikan (*Mean Time to Repair*/MTTR) rata-rata adalah 3,3 jam, yang masih di atas target 2 jam untuk perusahaan ritel.

Asesmen risiko (*risk assessment*) menggunakan metode ISO 27005 menghasilkan daftar risiko (*risk register*) dengan 23 risiko TI yang teridentifikasi. Tabel 6 menunjukkan lima risiko dengan prioritas tertinggi berdasarkan skor dampak × probabilitas.

**Tabel 6. Lima Risiko TI Teratas Berdasarkan Prioritas**

| No | Risiko | Dampak (1-5) | Probabilitas (1-5) | Skor Risiko | Kategori | Mitigasi yang Diusulkan |
|----|--------|--------------|-------------------|-------------|----------|------------------------|
| 1 | Kehilangan data akibat kegagalan *backup* | 5 | 4 | 20 | Kritis | Implementasi *automated backup* & rencana pemulihan bencana |
| 2 | *Downtime* sistem pemesanan akibat beban berlebih server | 4 | 5 | 20 | Kritis | Peningkatan kapasitas server & implementasi penyeimbang beban |
| 3 | Pelanggaran data pelanggan akibat kontrol akses lemah | 5 | 3 | 15 | Tinggi | Implementasi manajemen identitas dan akses (IAM) |
| 4 | Ketergantungan pada orang kunci (*single point of failure*) | 4 | 4 | 16 | Tinggi | Transfer pengetahuan & dokumentasi SOP lengkap |
| 5 | Investasi TI tidak selaras dengan prioritas bisnis | 3 | 5 | 15 | Tinggi | Implementasi kerangka kerja tata kelola TI (COBIT) |

Sumber: (Hasil Penelitian, 2025)

### Analisis Keselarasan TI-Bisnis

Pemetaan keselarasan strategi TI dengan tujuan bisnis menggunakan Kaskade Tujuan (*Goals Cascade*) COBIT 2019 menunjukkan tingkat keselarasan (*alignment*) yang masih rendah (42%). Tabel 7 menunjukkan hasil pemetaan antara tujuan bisnis (*business goals*), tujuan perusahaan (*enterprise goals*), dan tujuan terkait TI (*IT-related goals*) SATRIAMART.

**Tabel 7. Kaskade Tujuan: Pemetaan TI-Bisnis SATRIAMART**

| Tujuan Bisnis | Tujuan Perusahaan | Tujuan Terkait TI | Proses/Domain | Tingkat Keselarasan Saat Ini |
|----------------|------------------|------------------|----------------|---------------------------|
| Meningkatkan efisiensi operasional | Optimalisasi sumber daya | Pengelolaan aset TI optimal | APO12, DSS01 | 35% |
| Menjamin kelangsungan bisnis | Minimalisasi risiko | Manajemen risiko TI proaktif | EDM03, APO12 | 25% |
| Meningkatkan kualitas layanan | Peningkatan keandalan | Ketersediaan infrastruktur TI | DSS01 | 55% |
| Mendukung pertumbuhan bisnis | Keselarasan (*alignment*) strategi TI-bisnis | Keselarasan investasi TI | EDM03, MEA01 | 40% |
| Meningkatkan akuntabilitas | Transparansi kinerja | Pemantauan (*monitoring*) kinerja TI | MEA01 | 30% |
| **Rata-rata** | | | | **37%** |

Sumber: (Hasil Penelitian, 2025)

Rendahnya tingkat keselarasan mengindikasikan bahwa investasi dan inisiatif TI belum sepenuhnya mendukung pencapaian tujuan bisnis strategis SATRIAMART. Hal ini sejalan dengan temuan Thehawijaya dan Fajar (2024) yang menyatakan bahwa perusahaan dengan tingkat kematangan rendah cenderung memiliki keselarasan TI-bisnis (*IT-business alignment*) di bawah 50%.

### Analisis Optimalisasi Sumber Daya TI

Analisis utilisasi sumber daya TI menunjukkan beberapa inefisiensi. Utilisasi server rata-rata hanya 45%, namun terdapat lonjakan (*spike*) hingga 95% pada jam-jam tertentu yang menyebabkan waktu henti (*downtime*). Anggaran TI tahun 2025 sebesar Rp 450 juta, dengan alokasi 65% untuk biaya operasional (*operational expense*/OPEX) dan 35% untuk biaya modal (*capital expense*/CAPEX). Analisis menunjukkan bahwa 40% dari OPEX digunakan untuk perbaikan reaktif yang sebenarnya dapat dicegah melalui pemeliharaan preventif (*preventive maintenance*).

Tabel 8 menunjukkan analisis efisiensi penggunaan anggaran TI SATRIAMART.

**Tabel 8. Analisis Efisiensi Anggaran TI**

| Kategori Pengeluaran | Anggaran (Rp Juta) | Aktual (Rp Juta) | Persentase | Kategori Efisiensi |
|---------------------|------------------|------------------|------------|-------------------|
| Perangkat Keras & Infrastruktur (*Hardware & Infrastructure*) | 100 | 115 | 25,6% | Melebihi Anggaran (*Overbudget*) |
| Perangkat Lunak & Lisensi (*Software & License*) | 50 | 48 | 10,7% | Efisien |
| Pemeliharaan & Dukungan (*Maintenance & Support*) | 120 | 145 | 32,2% | Melebihi Anggaran (Reaktif) |
| Personel & Pelatihan (*Personnel & Training*) | 80 | 65 | 14,4% | Kurang Dimanfaatkan (*Underutilized*) |
| Proyek & Pengembangan (*Projects & Development*) | 100 | 77 | 17,1% | Kurang Dimanfaatkan |
| **Total** | **450** | **450** | **100%** | |

Sumber: (Hasil Penelitian, 2025)

Analisis menunjukkan bahwa kategori Pemeliharaan & Dukungan mengalami kelebihan anggaran (*overbudget*) 20,8% karena sifat perbaikan yang reaktif. Sebaliknya, kategori Personel & Pelatihan kurang dimanfaatkan (*underutilized*) 18,8%, mengindikasikan kurangnya investasi pada pengembangan kapabilitas SDM TI.

### Perancangan Kerangka Kerja Tata Kelola TI

Berdasarkan hasil asesmen (*assessment*) dan analisis kesenjangan (*gap analysis*), penelitian ini merancang kerangka kerja tata kelola TI SATRIAMART yang komprehensif dengan fokus pada empat domain COBIT 2019: EDM03, APO12, DSS01, dan MEA01. Kerangka kerja ini dirancang untuk meningkatkan tingkat kematangan (*maturity level*) dari 1,2 (tidak formal/*ad-hoc*) menjadi 3,0 (terkelola/*managed*) dalam periode 18–24 bulan.

Kerangka kerja yang dirancang mencakup lima komponen utama yang terintegrasi: (1) Struktur Tata Kelola (*Governance Structure*) – penetapan peran dan tanggung jawab yang jelas menggunakan matriks RACI; (2) Kebijakan dan Prosedur (*Policy & Procedure*) – pengembangan kebijakan manajemen risiko, keamanan informasi, pencadangan dan pemulihan (*backup & recovery*), manajemen perubahan (*change management*), dan pemantauan kinerja; (3) Kerangka Kerja Manajemen Risiko (*Risk Management Framework*) – implementasi daftar risiko (*risk register*), asesmen risiko berkala, dan mekanisme mitigasi proaktif; (4) Manajemen Kinerja (*Performance Management*) – penetapan KPI TI yang selaras dengan tujuan bisnis dan dasbor pemantauan waktu nyata (*real-time*); dan (5) Perbaikan Berkelanjutan (*Continuous Improvement*) – mekanisme tinjauan berkala, pembelajaran dari pengalaman (*lessons learned*), dan optimalisasi.

Struktur tata kelola yang dirancang mengadopsi model tiga tingkat (*three-tier*): strategis (*strategic*), taktis (*tactical*), dan operasional (*operational*) dengan penetapan peran dan tanggung jawab menggunakan matriks RACI. Gambar 1 menunjukkan kerangka kerja tata kelola dan pembagian peran untuk setiap pemangku kepentingan dalam implementasi kerangka kerja tata kelola TI.

![Framework Tata Kelola TI SATRIAMART](plantuml/images/gambar_1_framework.png)
Sumber: (Hasil Penelitian, 2025)
**Gambar 1. Framework Tata Kelola TI SATRIAMART Berbasis COBIT 2019**

Gambar 2 menunjukkan struktur organisasi tata kelola dengan tiga tingkat: strategis (Direktur), taktis (Manajer TI dan Manajer Keuangan), dan operasional (Staf TI). Setiap tingkat memiliki tanggung jawab yang spesifik dalam mendukung implementasi kerangka kerja tata kelola TI.

![Struktur Governance SATRIAMART](plantuml/images/gambar_2a_struktur_governance.png)
Sumber: (Hasil Penelitian, 2025)
**Gambar 2. Struktur Tata Kelola SATRIAMART**

Untuk memastikan kejelasan dalam peran dan tanggung jawab, penelitian ini mengembangkan matriks RACI yang mencakup 12 proses kunci dalam tata kelola TI. Tabel 9 menunjukkan matriks RACI yang mendefinisikan peran *Responsible* (Pelaksana), *Accountable* (Penanggung Jawab), *Consulted* (Konsultasi), dan *Informed* (Informasi) untuk setiap proses. Matriks RACI ini menjadi panduan operasional dalam implementasi kerangka kerja untuk menghindari konflik peran dan memastikan akuntabilitas yang jelas.

**Tabel 9. Matriks RACI - Proses Kunci SATRIAMART**

| Proses | Direktur | Manajer TI | Staf TI | Keuangan |
|--------|----------|------------|---------|----------|
| Penetapan Kebijakan TI | **A** | R | C | I |
| Asesmen & Mitigasi Risiko (*Risk Assessment & Mitigation*) | **A** | R | C | I |
| Persetujuan Anggaran TI (*Budget Approval*) | **A** | R | I | C |
| Implementasi Kerangka Kerja COBIT | I | **A/R** | R | I |
| Pemantauan & Pelaporan KPI (*Monitoring & Reporting*) | I | **A** | R | C |
| Pencadangan & Pemulihan Bencana (*Backup & Disaster Recovery*) | I | **A** | R | I |
| Keamanan & Kontrol Akses (*Security & Access Control*) | C | **A** | R | I |
| Manajemen Insiden (*Incident Management*) | I | **A** | R | I |
| Manajemen Perubahan (*Change Management*) | **A** | R | R | C |
| Audit Internal Tata Kelola TI | **A** | C | I | C |
| Pelatihan & Pengembangan Keterampilan (*Training & Skill Development*) | **A** | R | C | C |
| Manajemen Vendor & Kontrak (*Vendor & Contract Management*) | **A** | R | C | C |

**Keterangan:** R = Responsible (Pelaksana), A = Accountable (Penanggung Jawab), C = Consulted (Konsultasi), I = Informed (Informasi)

Sumber: (Hasil Penelitian, 2025)

Selain matriks RACI, penelitian ini juga merancang jalur eskalasi (*escalation path*) untuk penanganan insiden TI yang terstruktur. Gambar 3 menunjukkan mekanisme eskalasi tiga tingkat dengan waktu respons (*response time*) yang jelas: Tingkat 1 (Staf TI, <2 jam), Tingkat 2 (Manajer TI, <4 jam), dan Tingkat 3 (Direktur, <24 jam). Jalur eskalasi ini memastikan bahwa setiap insiden ditangani pada tingkat yang tepat sesuai dengan kompleksitas dan dampak bisnisnya.

![Escalation Path](plantuml/images/gambar_2b_escalation_path.png)
Sumber: (Hasil Penelitian, 2025)
**Gambar 3. Jalur Eskalasi Insiden TI SATRIAMART**

Tabel 10 menunjukkan sasaran kontrol (*control objectives*) dan indikator kinerja kunci (*key performance indicators*/KPI) untuk setiap domain.

**Tabel 10. Sasaran Kontrol dan KPI per Domain**

| Domain | Sasaran Kontrol | KPI/Metrik | Target (12 Bulan) | Target (24 Bulan) |
|--------|-------------------|------------|-------------------|-------------------|
| EDM03 | Kerangka kerja manajemen risiko disetujui dan dioperasionalkan | % risiko yang memiliki pemilik (*owner*) dan rencana mitigasi | 60% | 90% |
| EDM03 | Toleransi risiko TI diselaraskan dengan toleransi organisasi | Jumlah risiko yang melampaui toleransi | < 5 | < 2 |
| APO12 | Daftar risiko (*risk register*) dipelihara dan diperbarui | Frekuensi pembaruan daftar risiko | Bulanan | Bulanan |
| APO12 | Proses mitigasi risiko diimplementasikan | % risiko kritis yang dimitigasi | 70% | 95% |
| DSS01 | SOP operasional TI terdokumentasi lengkap | % proses yang memiliki SOP | 75% | 100% |
| DSS01 | Pencadangan dan pemulihan (*backup & recovery*) terautomasi | Frekuensi pencadangan berhasil | 95% | 99% |
| MEA01 | KPI TI ditetapkan dan dipantau | Jumlah KPI yang dilacak | 10 | 20 |
| MEA01 | Dasbor pemantauan (*dashboard monitoring*) tersedia | Frekuensi pembaruan dasbor | Mingguan | Waktu Nyata (*Real-time*) |

Sumber: (Hasil Penelitian, 2025)

### Peta Jalan Implementasi

Peta jalan (*roadmap*) implementasi dirancang dalam empat fase selama 18–24 bulan: Perbaikan Cepat (*Quick Wins*, Bulan 1–3), Jangka Pendek (*Short-term*, Bulan 4–9), Jangka Menengah (*Medium-term*, Bulan 10–18), dan Jangka Panjang (*Long-term*, Bulan 19–24). Setiap fase memiliki fokus, hasil (*deliverables*), dan kebutuhan sumber daya (*resource requirements*) yang spesifik. Tabel 11 menunjukkan peta jalan implementasi dengan garis waktu (*timeline*) dan hasil utama setiap fase.

**Tabel 11. Peta Jalan Implementasi Kerangka Kerja Tata Kelola TI SATRIAMART (18-24 Bulan)**

| Fase | Aktivitas | Durasi | Garis Waktu | Target Kematangan |
|------|-----------|--------|----------|-----------------|
| **FASE 1: PERBAIKAN CEPAT** | | **Bulan 1-3** | **Jan-Mar 2026** | **1.2 → 1.7** |
| | Daftar Risiko (*Risk Register*) - 20 risiko | 30 hari | Jan 2026 | |
| | Pencadangan Otomatis (*Automated Backup*) | 45 hari | Jan-Feb 2026 | |
| | Matriks RACI & Peran | 30 hari | Jan 2026 | |
| | SOP 5 Proses Kritikal | 60 hari | Jan-Mar 2026 | |
| | Dasbor Pemantauan (*Dashboard Monitoring*) | 45 hari | Jan-Feb 2026 | |
| **FASE 2: JANGKA PENDEK** | | **Bulan 4-9** | **Apr-Sep 2026** | **1.7 → 2.2** |
| | Kebijakan Manajemen Risiko | 60 hari | Apr-Mei 2026 | |
| | Asesmen Risiko Triwulanan (*Risk Assessment Quarterly*) | 90 hari | Apr-Jun 2026 | |
| | Peningkatan Server & Penyeimbang Beban (*Load Balancing*) | 75 hari | Apr-Jun 2026 | |
| | Pelatihan COBIT 2019 | 45 hari | Mei-Jun 2026 | |
| | Prosedur Manajemen Perubahan (*Change Management*) | 60 hari | Jul-Agu 2026 | |
| **FASE 3: JANGKA MENENGAH** | | **Bulan 10-18** | **Okt 2026-Jun 2027** | **2.2 → 2.6** |
| | Implementasi Manajemen Identitas & Akses (IAM) | 90 hari | Okt-Des 2026 | |
| | Rencana Pemulihan Bencana (*Disaster Recovery Plan*) | 120 hari | Okt 2026-Jan 2027 | |
| | Integrasi KPI TI dengan BSC | 90 hari | Feb-Apr 2027 | |
| | Perangkat Manajemen Layanan TI (*ITSM Tools*) | 105 hari | Feb-Mei 2027 | |
| | Audit Internal #1 | 30 hari | Jun 2027 | |
| **FASE 4: JANGKA PANJANG** | | **Bulan 19-24** | **Jul-Des 2027** | **2.6 → 3.0** |
| | Optimalisasi Proses (*Process Optimization*) | 60 hari | Jul-Agu 2027 | |
| | Analitik Prediktif (*Predictive Analytics*) | 90 hari | Jul-Sep 2027 | |
| | Sertifikasi ISO 27001 | 90 hari | Sep-Nov 2027 | |
| | Transfer Pengetahuan (*Knowledge Transfer*) | 60 hari | Okt-Nov 2027 | |
| | Asesmen Kematangan Final (*Final Maturity Assessment*) | 30 hari | Des 2027 | |

Sumber: (Hasil Penelitian, 2025)

**Fase 1: Perbaikan Cepat/*Quick Wins* (Bulan 1–3)**
Fokus: Perbaikan cepat dengan dampak tinggi dan upaya rendah. Hasil (*deliverables*) mencakup: (1) Dokumentasi daftar risiko (*risk register*) awal dengan 20 risiko prioritas; (2) Implementasi *backup* otomatis (*automated backup*) untuk sistem kritikal; (3) Penetapan matriks RACI untuk peran dan tanggung jawab (*roles & responsibilities*) TI; (4) Penyusunan SOP untuk 5 proses operasional kritikal; dan (5) Pengaturan dasbor pemantauan (*dashboard monitoring*) sederhana.

**Fase 2: Jangka Pendek/*Short-term* (Bulan 4–9)**
Fokus: Implementasi kerangka kerja dasar dan peningkatan kapabilitas. Hasil (*deliverables*) mencakup: (1) Pengesahan kebijakan manajemen risiko TI oleh Direktur; (2) Implementasi asesmen risiko berkala (triwulanan/*quarterly*); (3) Peningkatan (*upgrade*) infrastruktur server dan implementasi penyeimbang beban (*load balancing*); (4) Pelatihan tim TI tentang COBIT 2019 dan manajemen risiko (*risk management*); dan (5) Implementasi prosedur manajemen perubahan (*change management procedure*).

**Fase 3: Jangka Menengah/*Medium-term* (Bulan 10–18)**
Fokus: Optimalisasi proses dan peningkatan tingkat kematangan (*maturity level*). Hasil (*deliverables*) mencakup: (1) Implementasi Manajemen Identitas dan Akses (*Identity Access Management*/IAM); (2) Rencana Pemulihan Bencana (*Disaster Recovery Plan*/DRP) dan pengujian berkala; (3) Integrasi KPI TI dengan kartu skor berimbang (*balanced scorecard*) organisasi; (4) Implementasi perangkat Manajemen Layanan TI (*ITSM tools*) untuk *ticketing* dan basis pengetahuan (*knowledge base*); dan (5) Audit internal tata kelola TI pertama.

**Fase 4: Jangka Panjang/*Long-term* (Bulan 19–24)**
Fokus: Perbaikan berkelanjutan (*continuous improvement*) dan pencapaian tingkat kematangan 3,0. Hasil (*deliverables*) mencakup: (1) Optimalisasi proses berdasarkan hasil audit; (2) Implementasi analitik prediktif (*predictive analytics*) untuk manajemen risiko; (3) Sertifikasi ISO 27001 (jika diperlukan); (4) Transfer pengetahuan (*knowledge transfer*) lengkap dan dokumentasi komprehensif; dan (5) Asesmen tingkat kematangan final untuk validasi pencapaian target.

Tabel 12 menunjukkan proyeksi peningkatan tingkat kematangan untuk setiap fase implementasi.

**Tabel 12. Proyeksi Peningkatan Tingkat Kematangan per Fase**

| Domain | Awal (*Baseline*) | Fase 1 (M3) | Fase 2 (M9) | Fase 3 (M18) | Fase 4 (M24) | Target |
|--------|----------|-------------|-------------|--------------|--------------|--------|
| EDM03 | 1,0 | 1,5 | 2,0 | 2,5 | 3,0 | 3,0 |
| APO12 | 1,2 | 1,7 | 2,2 | 2,7 | 3,0 | 3,0 |
| DSS01 | 1,5 | 2,0 | 2,5 | 2,8 | 3,0 | 3,0 |
| MEA01 | 1,0 | 1,5 | 2,0 | 2,5 | 3,0 | 3,0 |
| **Rata-rata** | **1,2** | **1,7** | **2,2** | **2,6** | **3,0** | **3,0** |

Sumber: (Hasil Penelitian, 2025)

### Estimasi Biaya dan Pengembalian Investasi (ROI)

Estimasi biaya implementasi kerangka kerja tata kelola TI selama 24 bulan adalah Rp 380 juta, dengan rincian: Peningkatan infrastruktur (*infrastructure upgrade*) Rp 120 juta, Perangkat Lunak & Peralatan (*software & tools*) Rp 80 juta, Pelatihan & Sertifikasi (*training & certification*) Rp 60 juta, Konsultasi & Dukungan (*consulting & support*) Rp 80 juta, dan Kontinjensi (*contingency*) 10% Rp 40 juta.

Proyeksi penghematan dan manfaat finansial mencakup: (1) Pengurangan biaya *downtime* sebesar Rp 150 juta/tahun (asumsi *downtime* berkurang 60% × rata-rata biaya *downtime* Rp 250 juta/tahun); (2) Pengurangan biaya pemeliharaan reaktif sebesar Rp 100 juta/tahun; (3) Optimalisasi utilisasi aset TI menghemat Rp 50 juta/tahun; dan (4) Peningkatan produktivitas operasional setara Rp 80 juta/tahun.

Total manfaat finansial tahunan diproyeksikan Rp 380 juta, sehingga pengembalian investasi (ROI) dapat tercapai dalam 12 bulan (periode pengembalian/*payback period*). ROI 3 tahun diproyeksikan mencapai 200%, dengan Nilai Sekarang Bersih (*Net Present Value*/NPV) sebesar Rp 760 juta dan Tingkat Pengembalian Internal (*Internal Rate of Return*/IRR) sebesar 78%.

### Pembahasan

Hasil penelitian ini menunjukkan bahwa tingkat kematangan tata kelola TI SATRIAMART berada pada tingkat yang sangat rendah (1,2 dari skala 5), yang konsisten dengan fenomena yang diamati pada perusahaan ritel skala menengah di Indonesia. Temuan ini sejalan dengan penelitian Ramadhan dan Ramadhan (2025) yang mengidentifikasi bahwa UMKM di Indonesia cenderung memiliki tingkat kematangan tata kelola TI di bawah 2,0 karena keterbatasan sumber daya dan kesadaran terhadap pentingnya tata kelola TI yang terstruktur.

Domain EDM03 (*Ensure Risk Optimisation*) dan MEA01 (*Monitor, Evaluate and Assess Performance*) memiliki tingkat kematangan terendah (1,0), mengindikasikan bahwa aspek strategis tata kelola TI belum menjadi prioritas manajemen. Hal ini kontras dengan penelitian Agustriani (2024) pada perusahaan manufaktur yang lebih besar, di mana domain EDM03 dan APO12 sudah mencapai tingkat 2,5 karena tekanan regulasi (*regulatory pressure*) dan kompleksitas operasional yang lebih tinggi. Perbedaan ini menunjukkan bahwa ukuran dan kompleksitas organisasi memengaruhi prioritas implementasi tata kelola TI.

Analisis kesenjangan mengidentifikasi bahwa kesenjangan terbesar berada pada aspek manajemen risiko (kesenjangan 2,0 untuk EDM03 dan 1,8 untuk APO12), yang merupakan area kritis mengingat tingginya frekuensi insiden TI (47 insiden dalam 6 bulan). Penelitian Afifah dkk. (2023) menekankan bahwa implementasi COBIT 2019 spesifik domain (*domain-specific*) pada perusahaan manufaktur harus memprioritaskan area dengan kesenjangan terbesar untuk memaksimalkan dampak perbaikan. Oleh karena itu, peta jalan implementasi yang dirancang dalam penelitian ini menempatkan manajemen risiko sebagai prioritas utama pada fase Perbaikan Cepat (*Quick Wins*) dan Jangka Pendek (*Short-term*).

Tingkat keselarasan TI-bisnis yang rendah (37%) menjadi perhatian serius karena mengindikasikan bahwa investasi TI belum optimal dalam mendukung tujuan bisnis strategis. Thehawijaya dan Fajar (2024) menemukan bahwa perusahaan manufaktur otomotif dengan keselarasan TI-bisnis (*IT-business alignment*) di bawah 50% cenderung mengalami pemborosan investasi TI hingga 35%. Temuan ini memperkuat urgensi implementasi kerangka kerja tata kelola TI yang dapat menyelaraskan strategi TI dengan prioritas bisnis melalui Kaskade Tujuan (*Goals Cascade*) COBIT 2019.

Analisis risiko mengidentifikasi kehilangan data dan waktu henti (*downtime*) sistem sebagai risiko dengan prioritas tertinggi (skor 20), yang sejalan dengan temuan Agustriani (2024) bahwa manajemen risiko TI pada perusahaan ritel dan manufaktur di Indonesia harus fokus pada kelangsungan bisnis (*business continuity*) dan perlindungan data (*data protection*). Implementasi pencadangan otomatis (*automated backup*) dan rencana pemulihan bencana (*disaster recovery plan*) pada fase Perbaikan Cepat dirancang untuk memitigasi risiko-risiko kritis tersebut dengan cepat.

Inefisiensi penggunaan anggaran TI, khususnya melebihi anggaran (*overbudget*) 20,8% pada pemeliharaan reaktif (*reactive maintenance*), mengonfirmasi hipotesis bahwa tata kelola TI yang buruk berdampak langsung pada pemborosan finansial. Elina (2021) membuktikan bahwa implementasi kerangka kerja COBIT dapat meningkatkan efisiensi organisasi hingga 40% melalui optimalisasi proses dan pengurangan aktivitas tanpa nilai tambah (*non-value-added*). Peta jalan implementasi yang dirancang dalam penelitian ini bertujuan untuk mengalihkan fokus dari pemeliharaan reaktif ke pemeliharaan preventif (*preventive maintenance*), yang diproyeksikan menghemat Rp 100 juta per tahun.

Kerangka kerja tata kelola TI yang dirancang mengadopsi pendekatan bertahap (*phased approach*) yang terbukti efektif pada penelitian Aziz dkk. (2023) tentang implementasi domain APO COBIT 2019. Pendekatan ini memungkinkan SATRIAMART untuk mencapai perbaikan cepat (*quick wins*) pada bulan ke-3, membangun momentum perubahan, dan secara bertahap meningkatkan tingkat kematangan tanpa mengganggu operasional bisnis.

Proyeksi ROI sebesar 200% dalam 3 tahun dengan periode pengembalian (*payback period*) 12 bulan menunjukkan bahwa investasi pada tata kelola TI memberikan nilai bisnis (*business value*) yang signifikan. IT Governance Institute (2021) menyatakan bahwa organisasi dengan tingkat kematangan terkelola (*managed*, 3,0) dapat meningkatkan nilai bisnis hingga 20% melalui pengelolaan risiko yang lebih baik dan pemanfaatan sumber daya TI yang optimal. Proyeksi ini realistis mengingat potensi penghematan dari pengurangan waktu henti (Rp 150 juta/tahun) dan optimalisasi pemeliharaan (Rp 100 juta/tahun).

Penelitian ini memberikan kontribusi akademis dengan mengisi kesenjangan literatur implementasi COBIT 2019 pada perusahaan ritel skala menengah di Indonesia. Berbeda dengan penelitian Hapsari (2018) yang menggunakan COBIT 5 versi lama, penelitian ini mengadopsi COBIT 2019 dengan faktor desain (*design factor*) yang lebih adaptif terhadap karakteristik SATRIAMART. Model asesmen kematangan dan peta jalan implementasi yang dikembangkan dapat direplikasi oleh peneliti lain dan diadaptasi oleh perusahaan ritel sejenis.

Keterbatasan penelitian ini mencakup: (1) ruang lingkup terbatas pada satu studi kasus sehingga generalisasi hasil memerlukan validasi lebih lanjut pada konteks organisasi yang berbeda; (2) asesmen dilakukan pada satu titik waktu (*snapshot*) sehingga belum menangkap dinamika perubahan tingkat kematangan; dan (3) proyeksi ROI didasarkan pada asumsi yang perlu divalidasi melalui implementasi aktual. Penelitian lanjutan dapat melakukan studi longitudinal (*longitudinal study*) untuk memvalidasi efektivitas peta jalan implementasi dan mengukur peningkatan tingkat kematangan secara empiris.

---

## KESIMPULAN

Berdasarkan hasil asesmen dan analisis yang telah dilakukan, penelitian ini menghasilkan beberapa kesimpulan penting. Pertama, tingkat kematangan tata kelola TI SATRIAMART berada pada level 1,2 dari skala 5 (tidak formal/*ad-hoc*/*initial*), dengan domain EDM03 (*Ensure Risk Optimisation*) dan MEA01 (*Monitor, Evaluate and Assess Performance*) memiliki tingkat kematangan terendah (1,0). Kondisi ini mengindikasikan bahwa proses-proses TI masih bersifat reaktif, tidak terdokumentasi dengan baik, dan belum memiliki standar yang konsisten.

Kedua, analisis kesenjangan (*gap*) mengidentifikasi kesenjangan rata-rata 1,8 level antara kondisi saat ini dengan target tingkat kematangan 3,0 (terkelola/*managed*). Kesenjangan terbesar berada pada aspek manajemen risiko (kesenjangan 2,0 untuk EDM03 dan 1,8 untuk APO12), pemantauan kinerja (kesenjangan 2,0 untuk MEA01), dan operasional TI (kesenjangan 1,5 untuk DSS01). Faktor kritis yang memengaruhi capaian tingkat kematangan mencakup komitmen manajemen puncak, ketersediaan sumber daya, budaya organisasi yang adaptif, kemampuan tim TI, dan dukungan teknologi yang memadai.

Ketiga, analisis risiko mengidentifikasi 23 risiko TI dengan 5 risiko prioritas tertinggi: kehilangan data akibat kegagalan *backup*, *downtime* sistem pemesanan, pelanggaran data pelanggan, ketergantungan pada orang kunci (*key person*), dan ketidakselarasan investasi TI dengan prioritas bisnis. Analisis insiden menunjukkan 47 insiden TI dalam periode 6 bulan dengan total *downtime* 156 jam dan MTTR rata-rata 3,3 jam. Tingkat keselarasan TI-bisnis yang rendah (37%) mengindikasikan bahwa investasi TI belum optimal dalam mendukung tujuan bisnis strategis.

Keempat, kerangka kerja tata kelola TI yang dirancang mencakup lima komponen utama: struktur tata kelola (*governance structure*), kebijakan dan prosedur (*policy & procedure*), kerangka kerja manajemen risiko (*risk management framework*), manajemen kinerja (*performance management*), dan perbaikan berkelanjutan (*continuous improvement*). Kerangka kerja ini difokuskan pada empat domain COBIT 2019 (EDM03, APO12, DSS01, MEA01) dengan 8 sasaran kontrol (*control objectives*) dan KPI yang terukur.

Kelima, peta jalan implementasi dirancang dalam empat fase selama 18–24 bulan: Perbaikan Cepat/*Quick Wins* (Bulan 1–3), Jangka Pendek/*Short-term* (Bulan 4–9), Jangka Menengah/*Medium-term* (Bulan 10–18), dan Jangka Panjang/*Long-term* (Bulan 19–24). Implementasi peta jalan ini diproyeksikan dapat meningkatkan tingkat kematangan dari 1,2 menjadi 3,0, mengurangi insiden TI sebesar 60%, meningkatkan keselarasan TI-bisnis sebesar 75%, dan mengoptimalkan utilisasi sumber daya TI sebesar 40%.

Keenam, estimasi biaya implementasi selama 24 bulan adalah Rp 380 juta dengan proyeksi ROI 200% dalam 3 tahun dan periode pengembalian (*payback period*) 12 bulan. Manfaat finansial tahunan diproyeksikan mencapai Rp 380 juta melalui pengurangan biaya *downtime*, optimalisasi pemeliharaan, efisiensi utilisasi aset, dan peningkatan produktivitas operasional.

Penelitian ini merekomendasikan SATRIAMART untuk segera mengimplementasikan kerangka kerja tata kelola TI yang telah dirancang dengan memprioritaskan perbaikan cepat (*quick wins*) pada aspek manajemen risiko dan *backup*/*recovery*. Komitmen manajemen puncak dan alokasi sumber daya yang memadai menjadi kunci keberhasilan transformasi tata kelola TI. Pemantauan (*monitoring*) dan evaluasi berkala perlu dilakukan untuk memastikan pencapaian target tingkat kematangan sesuai peta jalan yang telah ditetapkan.

Untuk penelitian lanjutan, disarankan untuk melakukan studi longitudinal (*longitudinal study*) guna memvalidasi efektivitas peta jalan implementasi dan mengukur peningkatan tingkat kematangan secara empiris. Penelitian komparatif pada perusahaan ritel sejenis juga dapat dilakukan untuk menguji generalisasi model asesmen dan kerangka kerja yang telah dikembangkan. Eksplorasi lebih lanjut terhadap faktor-faktor sukses implementasi tata kelola TI pada konteks UMKM dan perusahaan ritel skala menengah di Indonesia juga menjadi area penelitian yang menarik untuk dieksplorasi.

---

## REFERENSI

Afifah, U. F., Adam, S., & Marfuah, M. (2023). Pemetaan Tata Kelola Teknologi Informasi melalui Desain Faktor Framework COBIT 2019 pada Perusahaan Manufaktur X. *Jurnal Sistem Informasi dan Teknologi, 15*(2), 145-152.

Agustriani, N. H. P. (2024). Analisis Manajemen Risiko Teknologi Informasi pada PT XYZ (Perusahaan Manufacturing) menggunakan Framework COBIT 2019 dengan Domain EDM03 dan APO12. *Jurnal Teknik Informatika, 12*(1), 78-89.

Aziz, M. A., Kusrini, K., & Nasiri, A. (2023). Perancangan Tata Kelola Teknologi Informasi Menggunakan Framework COBIT 2019 Domain Align Plan and Organize. *Jurnal Informatika dan Komputer, 18*(3), 234-245.

Elina, R. (2021). Evaluasi Implementasi Tata Kelola Teknologi Informasi Berdasarkan Framework COBIT. *Jurnal Manajemen Sistem Informasi, 9*(2), 112-125.

Hapsari, S. W. (2018). Implementasi Tata Kelola Teknologi Informasi Berdasarkan Framework COBIT 5 Pada PT Krakatau Tirta Industri. *Jurnal TEKNOINFO, 12*(1), 45-52.

ISACA. (2019). *COBIT 2019 Framework: Introduction and Methodology*. Rolling Meadows, IL: ISACA.

IT Governance Institute. (2021). *Global Status Report on IT Governance 2021*. Rolling Meadows, IL: IT Governance Institute.

Ramadhan, R. P., & Ramadhan, V. P. (2025). Analisis Tata Kelola TI untuk Pembukuan Digital UMKM dengan COBIT 2019: Studi Kasus Taylor Cahaya. *Jurnal Teknologi Informasi dan Bisnis, 14*(1), 67-78.

Riyadli, H., & Arliyana, A. (2022). Analisis Perencanaan Dan Implementasi Teknologi Informasi Menggunakan Framework COBIT Pada Usaha Toko Plastik. *Jurnal Sistem Informasi Bisnis, 10*(2), 156-165.

Thehawijaya, H. B., & Fajar, A. N. (2024). Evaluasi Tata Kelola Teknologi Informasi di Perusahaan Manufaktur Otomotif: Pendekatan Menggunakan Kerangka Kerja COBIT 2019. *Jurnal Teknik Industri, 16*(1), 89-102.
