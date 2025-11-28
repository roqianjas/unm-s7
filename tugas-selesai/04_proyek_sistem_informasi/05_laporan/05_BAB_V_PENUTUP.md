# BAB V
# PENUTUP

## 5.1 Kesimpulan

Berdasarkan hasil penelitian dan pembahasan yang telah diuraikan pada bab-bab sebelumnya, dapat ditarik beberapa kesimpulan penting terkait pengembangan CUR-HEART: Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital sebagai berikut:

### 5.1.1 Pencapaian Tujuan Penelitian

Proyek *capstone* ini telah berhasil mencapai seluruh tujuan yang ditetapkan pada Bab I. Sistem yang dikembangkan telah melalui tahapan analisis kebutuhan, perancangan, implementasi, pengujian, dan penyebaran secara menyeluruh. Pencapaian utama meliputi:

**1. Analisis Kebutuhan Sistem yang Komprehensif**

Penelitian ini berhasil mengidentifikasi 8 masalah kritis dalam manajemen layanan hipnoterapi tradisional, yaitu reservasi manual, risiko reservasi ganda, koordinasi jadwal yang kompleks, pencatatan data tidak terstruktur, sulitnya pemantauan kinerja, keterbatasan akses informasi, proses pembayaran manual, dan kesulitan pelaporan. Analisis pemangku kepentingan mengidentifikasi 5 kategori pengguna dengan kebutuhan berbeda (Tamu, Klien, Terapis, Admin, Pemilik). Pengumpulan data dilakukan melalui 6 teknik sistematis: observasi lapangan, wawancara mendalam, studi dokumentasi, survei, *benchmark* kompetitor, dan diskusi kelompok terpumpun.

**2. Perancangan Sistem yang Terstruktur dan Dapat Dikembangkan**

Sistem dirancang menggunakan metodologi dan praktik terbaik dalam rekayasa perangkat lunak. Arsitektur monolitik dengan pola MVC (*Model-View-Controller*) dipilih sesuai skala proyek UKM. Desain basis data menggunakan Diagram Relasi Entitas (ERD) dengan 16 entitas yang dinormalisasi hingga 3NF (*Third Normal Form*) untuk mencegah redundansi data. Desain antarmuka pengguna menghasilkan 66 halaman maket UI yang komprehensif. Pemodelan UML mencakup diagram kasus penggunaan, diagram aktivitas untuk 3 proses bisnis kritis, dan diagram sekuen untuk interaksi objek. Perancangan terstruktur ini menghasilkan sistem yang dapat dipelihara, diuji, dan dikembangkan sesuai kebutuhan bisnis di masa depan.

**3. Implementasi Sistem yang Fungsional dan Mudah Digunakan**

Sistem telah diimplementasikan sebagai aplikasi web lengkap berdasarkan 66 halaman maket UI yang mencakup 5 antarmuka berbasis peran: Tamu, Klien, Terapis, Admin, dan Pemilik. Fitur utama yang terimplementasi meliputi autentikasi dan otorisasi pengguna, manajemen katalog layanan, profil dan jadwal terapis, sistem reservasi daring, integrasi pembayaran Midtrans, manajemen reservasi, pelaksanaan dan dokumentasi sesi, dasbor kemajuan klien, dasbor terapis, panel admin, sistem notifikasi email, serta ulasan dan penilaian. Desain responsif memungkinkan akses dari desktop, tablet, dan perangkat seluler dengan navigasi intuitif dan hierarki visual yang jelas.

**4. Pengujian dan Jaminan Kualitas yang Menyeluruh**

Sistem telah melalui proses pengujian komprehensif meliputi pengujian unit untuk logika bisnis kritis, pengujian fitur untuk alur ujung ke ujung, pengujian penerimaan pengguna (UAT) oleh pengguna sebenarnya, pengujian kinerja untuk beban pengguna bersamaan, pengujian keamanan dengan pemindaian kerentanan, dan pengujian kompatibilitas lintas peramban. Hasil pengujian menunjukkan sistem telah lulus dengan tingkat kelulusan 97,8% dengan cakupan kode 72%, skor SUS 78,5/100, waktu muat 1,8 detik, 0 kerentanan kritis, dan UAT disetujui dengan kepuasan 9/10. Sistem dinyatakan siap produksi dan memenuhi seluruh standar kualitas yang ditetapkan.

**5. Dokumentasi dan Penyebaran Sistem**

Proyek menghasilkan dokumentasi lengkap berupa laporan 85 halaman, manual pengguna 20 halaman, manual admin 15 halaman, dokumentasi pengembang, dan 5 video tutorial untuk mendukung keberlanjutan sistem. Sistem berhasil disebarkan ke produksi dengan infrastruktur VPS Ubuntu 22.04, Nginx, MySQL 8.0, domain HTTPS (cur-heart.id), SSL Let's Encrypt, dan pemantauan aktif yang mencapai *uptime* 99,8% selama periode pengujian.

**6. Dampak dan Nilai Bisnis**

Sistem memberikan dampak terukur kepada CUR-HEART dengan peningkatan efisiensi operasional 60% (penghematan 20 jam per bulan waktu admin), peningkatan kapasitas reservasi 25% (dari 80 menjadi 105 reservasi per bulan), peningkatan pendapatan 31% (dari Rp26,45 juta menjadi Rp34,72 juta per bulan), eliminasi 100% reservasi ganda, peningkatan retensi klien dari 65% menjadi 85%, dan kepuasan pengguna mencapai 9/10. ROI sistem mencapai 1.743% dalam proyeksi 5 tahun dengan periode *payback* hanya 20 hari.

**7. Penerapan Teori dan Praktik Terbaik**

Sistem menerapkan teori dan praktik terbaik dari berbagai bidang: Sistem Informasi (sistem sosio-teknis, rantai nilai informasi), Manajemen Proyek PMBOK (10 bidang pengetahuan, piagam proyek, WBS, Gantt, manajemen risiko), Desain Basis Data (ERD, normalisasi 3NF, pengindeksan), Rekayasa Perangkat Lunak (pola MVC, prinsip SOLID, standar PSR-12), UX Design (desain *user-centered*, heuristik Nielsen, desain responsif), Keamanan (OWASP Top 10, *defense-in-depth*, enkripsi), dan Praktik Hipnoterapi (pedoman etika, kerahasiaan klien, dokumentasi sesi). Penerapan teori ini memastikan sistem berkualitas tinggi dan sesuai standar industri.

### 5.1.2 Dampak dan Kontribusi Proyek

Proyek *capstone* ini memberikan kontribusi signifikan dalam beberapa aspek:

**Dampak Bisnis untuk CUR-HEART**

Transformasi operasional dari sistem manual berbasis kertas menjadi sistem digital otomatis dengan akses 24/7 memberikan skalabilitas bisnis melalui fondasi yang mendukung pertumbuhan tanpa peningkatan proporsional beban administratif. Posisi kompetitif menjadi lebih kuat dengan diferensiasi dari kompetitor dan citra merek modern. Keberlanjutan keuangan tercapai dengan peningkatan pendapatan 31%, pengurangan biaya operasional, dan ROI 1.743%.

**Manfaat untuk Pemangku Kepentingan**

Klien memperoleh kemudahan reservasi kapan saja, layanan mandiri, transparansi informasi, dan privasi data terjaga. Terapis mengalami peningkatan produktivitas dengan berkurangnya tugas administratif, dokumentasi digital terorganisir, dan visibilitas pendapatan. Admin mengalami pengurangan beban kerja 70%, eliminasi tugas berulang, dan dapat fokus pada layanan nilai tinggi. Pemilik memperoleh visibilitas operasional waktu nyata, pengambilan keputusan berbasis data, dan kontrol penuh sistem.

**Kontribusi Akademik dan Industri**

Proyek ini memberikan studi kasus penerapan dunia nyata, pengalaman belajar tim dalam keterampilan teknis, manajemen proyek, dan kerja sama tim, serta potensi publikasi. Bagi industri, proyek ini mendemonstrasikan transformasi digital UKM yang terjangkau, contoh implementasi sistem kesehatan mental, dan berbagi pengetahuan. Kontribusi sosial meliputi peningkatan akses ke layanan hipnoterapi, mendorong literasi digital, dan kontribusi pada kesejahteraan masyarakat.

### 5.1.3 Pembelajaran dan Tantangan

Selama pengerjaan proyek ini, tim memperoleh pembelajaran berharga yang dapat diterapkan di proyek-proyek mendatang. Penggunaan *framework* Laravel 10 terbukti mempercepat pengembangan meskipun memiliki kurva pembelajaran curam. Desain basis data yang matang sejak awal menjadi fondasi penting kesuksesan sistem. Desain iteratif dengan umpan balik pengguna awal sangat penting untuk menghasilkan antarmuka yang sederhana dan mudah digunakan. Keamanan harus dirancang sejak awal, bukan ditempelkan kemudian, dengan mengikuti *checklist* OWASP Top 10.

Integrasi pihak ketiga seperti *gateway* pembayaran memerlukan *buffer* waktu yang cukup untuk pengujian berbagai skenario. Pengujian otomatis merupakan investasi yang terbayar sepuluh kali lipat dalam mencegah regresi. Analisis kebutuhan yang jelas dengan dokumentasi *acceptance criteria* menjadi fondasi kesuksesan proyek. Perencanaan *timeline* realistis perlu menyertakan *buffer* 20% untuk mengantisipasi kendala tak terduga.

Komunikasi tim yang proaktif melalui *daily standup* 15 menit efektif menyelaraskan tim. Manajemen risiko proaktif dengan *risk register* lebih baik daripada manajemen krisis reaktif. Disiplin *version control* dengan *feature branches* dan *pull request review* meningkatkan kualitas kode. Keterlibatan pengguna sejak awal melalui *feedback session* rutin meningkatkan UX secara signifikan.

Kesuksesan proyek bergantung pada lima pilar: teknologi yang tepat (Laravel), kebutuhan jelas, kerja sama tim baik, pendekatan *user-centered*, dan fokus ROI.

### 5.1.4 Kesimpulan Akhir

Proyek *capstone* "CUR-HEART: Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital" telah berhasil mencapai seluruh tujuan yang ditetapkan dengan hasil yang melampaui ekspektasi. Sistem yang dihasilkan bersifat fungsional dengan semua fitur terimplementasi dan berfungsi baik, ramah pengguna dengan antarmuka intuitif, aman dengan *best practices* keamanan, berkinerja tinggi dengan waktu respons kurang dari 2 detik, dapat dikembangkan dengan arsitektur yang mendukung pertumbuhan bisnis, terdokumentasi dengan baik, dan berharga dengan ROI terukur 1.743% dalam 5 tahun.

Proyek ini membuktikan bahwa dengan metodologi yang tepat (*Waterfall* SDLC), teknologi yang sesuai (Laravel, PHP, MySQL, Tailwind CSS), tim yang berkomitmen, dan pemangku kepentingan yang terlibat, bahkan proyek dengan garis waktu dan anggaran terbatas dapat menghasilkan sistem berkualitas tinggi yang memberikan nilai signifikan kepada bisnis.

Lebih dari sekadar memenuhi persyaratan akademik, proyek ini telah memberikan dampak bisnis nyata kepada CUR-HEART, pengalaman belajar yang berharga kepada tim pengembang, dan kontribusi kepada kumpulan pengetahuan dalam bidang sistem informasi kesehatan.

---

## 5.2 Saran

Berdasarkan hasil pengembangan dan evaluasi sistem yang telah dilakukan, berikut adalah saran untuk pengembangan dan perbaikan sistem di masa depan:

### 5.2.1 Saran untuk Pengembangan Sistem

Pengembangan Fase 2 harus difokuskan pada peningkatan yang memberikan ROI tertinggi dan memperkuat posisi kompetitif CUR-HEART. Beberapa prioritas pengembangan yang direkomendasikan:

**Prioritas Tinggi (Tahun Pertama)**

Notifikasi SMS untuk konfirmasi dan pengingat otomatis dapat mengurangi tingkat *no-show* dari 8% menjadi 5%, dengan estimasi biaya Rp2-3 juta ditambah Rp100-300 per SMS dan manfaat tambahan pendapatan Rp15 juta per tahun. Sistem keanggotaan dan paket loyalitas seperti beli 5 dapat 1 gratis dan langganan bulanan dapat meningkatkan *customer lifetime value* dengan estimasi biaya Rp5-7 juta dan pendapatan tambahan Rp50 juta per tahun.

Lapisan *caching* Redis untuk data sesi dan *query* frekuen dapat meningkatkan performa dengan waktu muat kurang dari 1 detik, estimasi biaya Rp2-3 juta ditambah Rp1-2 juta per tahun. Autentikasi dua faktor dengan SMS OTP atau Google Authenticator wajib untuk terapis dan admin dapat mengurangi risiko pengambilalihan akun dengan estimasi biaya Rp3-5 juta ditambah biaya SMS.

*Backup* cloud otomatis harian ke AWS S3 atau Google Cloud dengan enkripsi dan retensi 30 hari memberikan kesiapan pemulihan bencana dengan estimasi biaya Rp1-2 juta ditambah Rp500 ribu hingga Rp1 juta per tahun. Integrasi terapi video dengan *embed* Whereby atau Zoom untuk sesi jarak jauh dapat membuka pasar baru dengan estimasi biaya Rp5-8 juta ditambah Rp2-5 juta per tahun dan pendapatan tambahan Rp40 juta per tahun.

Total investasi prioritas tinggi diperkirakan Rp18-28 juta dengan proyeksi pendapatan tambahan Rp125 juta per tahun, menghasilkan ROI 446-694% dengan periode *payback* 2-3 bulan.

**Prioritas Sedang (Tahun Kedua)**

Aplikasi *mobile native* iOS dan Android dengan React Native atau Flutter dapat meningkatkan retensi 10% dengan estimasi biaya Rp25-40 juta ditambah Rp5 juta per tahun. *Dashboard* analitik lanjutan dengan tren, peramalan, dan metrik terapis mendukung keputusan berbasis data dengan estimasi biaya Rp3-5 juta. CDN untuk aset statis menggunakan CloudFlare atau AWS CloudFront dapat mempercepat muat halaman dan meningkatkan SEO dengan estimasi biaya Rp1-2 juta ditambah Rp1-3 juta per tahun.

**Prioritas Rendah (Tahun Ketiga)**

*Chatbot* AI dengan DialogFlow atau OpenAI untuk FAQ dan bantuan reservasi 24/7 dapat mengurangi beban admin dengan estimasi biaya Rp10-15 juta ditambah Rp2-5 juta per tahun. Sinkronisasi kalender dengan Google Calendar untuk pembaruan ketersediaan otomatis dengan estimasi biaya Rp3-4 juta. REST API pihak ketiga dengan OAuth2 untuk integrasi mitra membuka potensi ekspansi ekosistem dengan estimasi biaya Rp5-8 juta.

**Pendekatan Implementasi**

Implementasi harus dilakukan secara bertahap dan terukur dengan pola: *Plan - Develop - Test - Deploy - Measure - Iterate*. Setiap fitur harus divalidasi dampak bisnisnya sebelum melanjutkan ke fitur berikutnya, memastikan investasi TI selalu selaras dengan tujuan bisnis dan memberikan nilai nyata kepada CUR-HEART.

### 5.2.2 Saran untuk Manajemen dan Operasional

Keberhasilan implementasi sistem tidak hanya bergantung pada kualitas teknis, tetapi juga pada adopsi pengguna, proses operasional yang efektif, dan manajemen yang berkelanjutan.

**Adopsi dan Pelatihan**

Program pelatihan berkelanjutan dengan sesi *refresh* triwulanan diperlukan untuk mempertahankan kompetensi dan memperkenalkan fitur baru. Identifikasi 2-3 "*super user*" tiap kelompok sebagai *champion* pengguna untuk membantu yang lain. Komunikasi proaktif dan sesi *one-on-one* dapat membantu mengatasi resistensi terhadap perubahan.

**Proses Operasional**

Dokumentasi SOP untuk proses operasional utama meliputi alur pemesanan, dokumentasi sesi, verifikasi pembayaran, manajemen pengguna, dan respons insiden. Rutinitas pemantauan harian dengan pengecekan *uptime* dan *error logs* di pagi hari, pemesanan dan pembayaran di siang hari, serta *backup* dan metrik di malam hari. Rencana respons insiden dengan matriks eskalasi, SLA waktu respons, dan *template* komunikasi.

**Manajemen Keuangan**

Alokasi anggaran operasional TI sebesar Rp50 juta per tahun untuk *maintenance*, *hosting*, dan *upgrade* dengan tinjauan bulanan aktual versus anggaran. Pemantauan ROI bulanan untuk memastikan sistem terus memberikan nilai dengan pelacakan metrik volume pemesanan, pendapatan, waktu yang dihemat, dan kepuasan. Perencanaan investasi pengembangan lanjutan berdasarkan prioritas ROI dengan anggaran Rp18-28 juta untuk fitur prioritas tinggi.

**Data dan Kepatuhan**

Verifikasi *backup* bulanan dengan pengujian pemulihan tabel acak dan pengujian pemulihan basis data penuh triwulanan untuk memastikan kelangsungan bisnis. Kepatuhan UU Perlindungan Data Pribadi dengan tinjauan kebijakan privasi, implementasi hak subjek data, dokumentasi perjanjian pemrosesan data, manajemen persetujuan, dan pelatihan staf. Kebijakan retensi data dengan penyimpanan data klien 5 tahun, catatan sesi 7 tahun, dan pembayaran 10 tahun sesuai ketentuan perpajakan.

**Komunikasi Pemangku Kepentingan**

Laporan kinerja bulanan dengan metrik tren pemesanan, pendapatan, kepuasan, *uptime*, dan masalah. Pengumpulan umpan balik sistematis melalui survei pasca-pemesanan, NPS triwulanan, tombol umpan balik dalam aplikasi, dan pertemuan tinjauan triwulanan. Berbagi *success stories* dengan dokumentasi testimonial klien dan studi kasus untuk pemasaran.

**Perbaikan Berkelanjutan**

Tinjauan sistem bulanan dengan pertemuan yang melibatkan pemilik, manajer operasional, dan dukungan TI untuk menilai kinerja dan merencanakan perbaikan. Tinjauan strategis tahunan untuk menyelaraskan sistem dengan strategi bisnis, mengevaluasi ROI, meninjau tren teknologi, perencanaan anggaran, dan pembaruan peta jalan. Transfer pengetahuan dari tim pengembang ke staf internal atau vendor untuk keberlanjutan dengan dokumentasi *handover*, pelatihan staf TI, dan *code walkthrough*.

### 5.2.3 Saran untuk Penelitian Lanjutan

Proyek ini telah membuka berbagai peluang penelitian lanjutan yang dapat memberikan kontribusi baik pada bidang akademik maupun praktis.

**Riset Teknis**

*Machine learning* untuk prediksi hasil terapi dapat mengidentifikasi dini klien berisiko dan memberikan rekomendasi perawatan personal berdasarkan profil klien dan data historis. Penelitian komparatif arsitektur *monolithic* versus *microservices* untuk sistem kesehatan UKM dapat memberikan *framework* keputusan pemilihan arsitektur berbasis ukuran bisnis. *Dashboard* analitik waktu nyata dengan latensi kurang dari 5 detik dapat memberikan arsitektur referensi untuk analitik kesehatan.

**Riset Bisnis**

Studi kasus ganda pada 10-15 praktik terapi dapat mengidentifikasi faktor sukses kritis transformasi digital dalam praktik terapi dan pengaruhnya terhadap kinerja bisnis. Penelitian penerimaan teknologi dengan *framework* TAM atau UTAUT yang diperluas dapat mengidentifikasi faktor yang mempengaruhi penerimaan klien dan terapis terhadap sistem manajemen terapi digital. Studi longitudinal 3-5 tahun dapat menganalisis bagaimana nilai investasi TI kesehatan berkembang dan faktor yang memprediksi ROI berkelanjutan.

**Riset Pengalaman Pengguna**

Penelitian hambatan dan fasilitas bagi orang dewasa lanjut usia (60+) dalam menggunakan platform reservasi terapi daring dapat menghasilkan pedoman desain ramah usia untuk platform kesehatan. Penelitian persepsi privasi data dalam aplikasi kesehatan mental dapat mengidentifikasi fitur yang mempengaruhi kepercayaan dan menghasilkan *framework* desain privasi.

**Riset Domain Hipnoterapi**

Penelitian *quasi-experimental* dapat membandingkan dampak pelacakan kemajuan digital terhadap hasil terapi dibandingkan pelacakan kertas tradisional. *Randomized Controlled Trial* dapat menguji apakah hipnoterapi daring sama efektifnya dengan sesi tatap muka untuk kecemasan dan manajemen stres. Studi komparatif dapat mengidentifikasi frekuensi sesi optimal (mingguan, dua mingguan, atau bulanan) untuk berbagai tujuan hipnoterapi.

**Prioritas Penelitian**

Tiga topik prioritas sangat tinggi yang direkomendasikan untuk mahasiswa: *machine learning* untuk prediksi hasil terapi dengan dampak potensial merevolusi efektivitas terapi, dampak transformasi digital pada UKM kesehatan dengan nilai praktis tinggi untuk ribuan penyedia layanan, dan *teletherapy* versus hipnoterapi tatap muka sebagai pertanyaan kritis pasca-pandemi dengan dampak kebijakan tinggi.

CUR-HEART terbuka untuk kerja sama penelitian dengan mahasiswa, dosen, atau peneliti yang tertarik dengan topik-topik di atas. Akses ke data sistem dengan anonimisasi, wawancara dengan pemangku kepentingan, dan dukungan implementasi *proof-of-concept* dapat difasilitasi untuk tujuan akademik yang sah.

### 5.2.4 Penutup Saran

Saran-saran yang disampaikan di atas merupakan peta jalan untuk perbaikan berkelanjutan dari Sistem CUR-HEART. Tidak semua saran perlu diimplementasikan sekaligus. Prioritisasi berdasarkan nilai bisnis, kebutuhan pengguna, ketersediaan sumber daya, ketergantungan teknis, dan tingkat risiko.

Pendekatan yang disarankan: jangka pendek (3-6 bulan) fokus pada kemenangan cepat seperti optimisasi kinerja dan pelatihan pengguna; jangka menengah (6-12 bulan) implementasi fitur signifikan seperti aplikasi *mobile* dan konferensi video; jangka panjang (1-2 tahun) inisiatif strategis seperti integrasi AI dan analitik lanjutan.

Dengan pola pikir perbaikan berkelanjutan, Sistem CUR-HEART dapat terus berkembang untuk memenuhi kebutuhan bisnis yang berubah dan mempertahankan keunggulan kompetitif dalam industri teknologi kesehatan.

---
