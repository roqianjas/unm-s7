**PERANCANGAN SISTEM INFORMASI CRM PADA **

**CUR-HEART \(PUSAT HIPNOTERAPI **

**& KESEHATAN MENTAL\) **



**MAKALAH **



Diajukan untuk memenuhi salah satu tugas kelompok mata kuliah Manajemen Hubungan Pelanggan 

****

Nama Anggota Kelompok : 

## 1. Roki Anjas 

### 11250066 

## 2. Fahruroji 

### 11250085 

## 3. Susanto 

### 11250068 



Kelas: 11.7C.12 

****





**PROGRAM STUDI SISTEM INFORMASI **

**UNIVERSITAS NUSA MANDIRI **

**JAKARTA **

**2025 **





**KATA PENGANTAR **

****

Puji syukur kami panjatkan kepada Tuhan Yang Maha Esa atas segala rahmat dan karunia-Nya sehingga kami dapat menyelesaikan laporan dengan judul 

"Perancangan Sistem Informasi CRM Pada Cur-Heart \(Pusat Hipnoterapi & Kesehatan Mental\)" sebagai salah satu syarat untuk menyelesaikan Program Studi Strata Satu \(S1\) Sistem Informasi di Fakultas Teknologi Informasi Universitas Nusa Mandiri. 

Proyek ini bertujuan untuk mengembangkan sistem informasi berbasis web yang dapat meningkatkan efisiensi dan efektivitas operasional layanan hipnoterapi di CUR-HEART \( *Hypnotherapy & Mind Wellness Center\). * Dengan memanfaatkan teknologi informasi, kami berupaya memberikan solusi komprehensif untuk permasalahan manajemen reservasi, penjadwalan, dokumentasi terapi, dan pembayaran yang selama ini dilakukan secara manual. 

Kami menyadari bahwa laporan ini masih jauh dari sempurna. Oleh karena itu penyusun mengucapkan terima kasih kepada Ibu Ummu Radiyah, S.Kom, M.Eng selaku dosen pengampu mata kuliah Manajemen Hubungan pelanggan yang telah memberikan bimbingan dan arahan selama proses pembelajaran. 

Kami sangat mengharapkan kritik dan saran yang membangun dari berbagai pihak untuk perbaikan di masa mendatang. Kami berharap penelitian ini dapat memberikan manfaat, khususnya bagi CUR-HEART dalam mengoptimalkan layanan terapi kesehatan mental, serta bagi akademisi dan praktisi yang tertarik dalam bidang sistem informasi layanan kesehatan. 

Akhir kata, kami mengucapkan terima kasih kepada semua pihak yang telah membantu dalam penyelesaian proyek ini. Semoga laporan ini dapat memberikan kontribusi positif bagi perkembangan sistem informasi kesehatan mental di Indonesia. 



Jakarta, 31 Desember 2025 





Penyusun 

ii 





**ABSTRAK **

****

**Roki Anjas \(11250066\), Fahruroji \(11250085\), Susanto \(11250068\) **

**“Perancangan Sistem Informasi CRM Pada Cur-Heart \(Pusat Hipnoterapi &** **Kesehatan Mental\)”. **

****

CUR-HEART \( *Hypnotherapy & Mind Wellness Center*\) menghadapi tantangan operasional akibat sistem manual yang tidak efisien, meliputi proses reservasi dengan tingkat konversi hanya 60%, konflik jadwal 8-10 kasus per bulan, dokumentasi tidak terstruktur, dan risiko keamanan data. Penelitian ini bertujuan mengembangkan sistem informasi berbasis web menggunakan framework Laravel dengan pendekatan *System Development Life Cycle* \(SDLC\) model *Waterfall*. 

Metodologi meliputi inisiasi, perencanaan, pelaksanaan \(analisis kebutuhan, perancangan, implementasi, pengujian, deployment\), pemantauan, dan penutupan proyek. Analisis kebutuhan mengidentifikasi 40\+ kebutuhan fungsional melalui wawancara dengan 14 responden. Perancangan menggunakan ERD dengan 16 

entitas dinormalisasi hingga 3NF, diagram UML, dan 66 halaman maket *UI/UX*. 

Implementasi menghasilkan aplikasi web dengan 8 modul utama: autentikasi, informasi publik, reservasi otomatis, dasbor klien, dasbor terapis, dasbor admin, integrasi pembayaran Midtrans, dan notifikasi email. Teknologi yang digunakan: *Laravel 10, MySQL 8.0, Tailwind CSS, dan VPS Ubuntu*. Pengujian mencapai 100% pass rate untuk 12 skenario kritis UAT dengan skor SUS 80,5/100 \(kategori *Excellent*/A\). 

Dampak bisnis terukur meliputi peningkatan efisiensi operasional 60%, peningkatan kapasitas reservasi 25%, peningkatan pendapatan 31% \(Rp26,45 juta menjadi Rp34,72 juta/bulan\), eliminasi 100% reservasi ganda, peningkatan retensi klien dari 65% menjadi 85%, dan ROI 1.743% dalam proyeksi 5 tahun dengan periode payback 20 hari. Sistem ini membuktikan bahwa transformasi digital layanan terapi mental dapat diimplementasikan dengan metodologi tepat, teknologi sesuai, dan pendekatan *user-centered*, menghasilkan nilai bisnis signifikan. 

****

**Kata kunci: *Sistem Informasi, Layanan Terapi Mental, Hipnoterapi, Laravel, ***

***Transformasi Digital, Manajemen Reservasi, SDLC Waterfall, ROI***** **





****

****

****

iii 





**DAFTAR ISI **

****

Halaman 

Lembar Judul Makalah .......................................................................................... i Kata Pengantar .................................................................................................... ii Abstrak ................................................................................................................. iii Daftar Isi ................................................................................................................ iv Daftar Gambar ...................................................................................................... vi Daftar Tabel .......................................................................................................... vii Daftar Simbol .................................................................................................... viii **BAB 1 PENDAHULUAN ................................................................................... 1 **

1.1. Latar Belakang ................................................................................ 1 

1.2. Rumusan Masalah ........................................................................... 2 

1.3. Tujuan Penelitian ............................................................................ 3 

1.4. Manfaat Penelitian ........................................................................... 3 

1.4.1. Manfaat Teoritis ..................................................................... 3 

1.4.2. Manfaat Praktis ..................................................................... 4 

1.5. Ruang Lingkup Penelitian ............................................................... 5 

1.5.1. Ruang Lingkup Penelitian .................................................... 5 

1.5.2. Ruang Lingkup Sistem .......................................................... 5 

1.5.3. Ruang Lingkup Pengguna ..................................................... 5 

1.5.4. Ruang Lingkup Waktu .......................................................... 5 

1.5.5. Batasan Penelitian ................................................................. 6 

1.6. Sistematika Penulisan ..................................................................... 6 

**BAB II TINJAUAN PUSTAKA ....................................................................... 8 **

2.1. *CUSTOMER RELATIONSHIP MANAGEMENT* \(CRM\) ............... 8 

2.1.1. Pengertian CRM ................................................................... 8 

2.1.2. Tujuan CRM ......................................................................... 8 

2.1.3. Kerangka Komponen CRM ................................................... 9 

2.1.4. Manfaat CRM ....................................................................... 9 

2.2. CRM dalam Industri Kesehatan .................................................... 10 

2.2.1. Karakteristik Khusus CRM Kesehatan .............................. 10 

2.2.2. Optimalisasi dan Manajemen Layanan Kesehatan ............ 10 

2.3. Strategi CRM ............................................................................... 11 

2.3.1. Siklus Hidup Pelanggan ..................................................... 11 

2.3.2. Segmentasi Pelanggan ....................................................... 11 

2.3.3. Personalisasi Layanan ........................................................ 11 

2.4. Teknologi CRM ........................................................................... 12 

2.4.1. Sistem Informasi CRM ...................................................... 12 

2.4.2. Peran Sistem Informasi CRM ............................................ 12 

2.5. Metrik dan KPI CRM ................................................................... 13 

2.5.1. Retensi dan Loyalitas ......................................................... 13 

2.5.2. Metrik Kepuasaan Pelanggan ............................................ 13 



iv 





**BAB III METODOLOGI PENELITIAN** ..................................................... 14 

3.1. Jenis Penelitian ........................................................................... 14 

3.2. Objek Penelitian ......................................................................... 14 

3.3. Subjek Penelitian ........................................................................ 15 

3.4 *. * Teknik Pengumpulan Data .......................................................... 16 

3.4.1. Observasi .......................................................................... 16 

3.4.2. Wawancara Mendalam .................................................... 16 

3.4.3. Studi Dokumentasi .......................................................... 17 

3.4.4. Kuisoner .......................................................................... 17 

3.4.5. Simulasi dan Validasi Desain .......................................... 17 

3.5. Teknik Analisis Data .................................................................... 18 

3.5.1. Analisis Deskriptif ............................................................. 18 

3.5.2. Analisis Konten .................................................................. 18 

3.5.3. Analisis Komparatif ........................................................... 18 

3.5.4. Analisis Metrik CRM ......................................................... 18 

3.6. Tahapan Penelitian ....................................................................... 19 

3.7. Kerangka Kerja Analisis .............................................................. 20 

3.8. Validitas dan Reliabilitas ............................................................. 20 

3.8.1. Triangulasi ......................................................................... 20 

3.8.2. Member *Checking* .............................................................. 20 

3.8.3. Audit Trail .......................................................................... 21 

3.8.4. *Peer Debriefing* .................................................................. 21 

3.9. Etika Penelitian ............................................................................ 21 



**BAB IV HASIL DAN PEMBAHASAN .......................................................... 22** 

4.1. Profil CUR-HEART ................................................................... 22 

4.1.1. Gambaran Umum Perusahaan ......................................... 22 

4.1.2. Layanan yang Ditawarkan ............................................... 22 

4.1.3. Struktur Organisasi ........................................................... 23 

4.1.4. Profil Pelanggan .............................................................. 23 

4.2. Strategi CRM CUR-Heart .......................................................... 24 

4.2.1. Filosofi CRM CUR-Heart ............................................... 24 

4.2.2. Tujuan Strategis CRM ..................................................... 24 

4.2.3. Perencanaan Anggaran Biaya .......................................... 25 

4.2.4. Strategi Personalisasi ....................................................... 25 

4.3. Analisis Kebutuhan Sistem CRM ............................................... 26 

4.3.1. Identifikasi Masalah Existing .......................................... 26 

4.3.2. Analisis Kebutuhan Pelanggan ........................................ 27 

4.3.3. Kebutuhan Fungsional Sistem ......................................... 27 

4.3.4. Kebutuhan Non-Fungsional Sistem ................................. 29 

4.3.5. Analisis Kelayakan .......................................................... 30 

4.4. Perancangan Fitur CRM ............................................................ 31 

4.4.1. Arsitektur Sistem CRM ................................................... 31 

4.4.2. Diagram Konteks dan Data Flow Diagram ..................... 32 

v 





4.4.3. *Use Case Diagram* .......................................................... 33 

4.4.4. *Flowchart* Proses Bisnis Utama ...................................... 36 

4.4.5. *Desain Database* CRM .................................................... 38 

4.4.6. Fitur-Fitur CRM yang dirancang ..................................... 39 

4.4.7. Integrasi Fitur CRM dengan Proses Bisnis ..................... 48 

4.5. Validasi Perancangan CRM ........................................................ 49 

4.5.1. Metodologi Validasi ........................................................ 49 

4.5.2. Hasil Validasi Perancangan Fitur CRM .......................... 49 

4.5.3. Proyeksi Dampak terhadap Kepuasan Klien ................... 51 

4.5.4. Proyeksi Dampak terhadap Retensi Klien ....................... 52 

4.5.5. Proyeksi Dampak terhadap Efisiensi Operasional .......... 53 

4.5.6. Proyeksi Dampak terhadap Kinerja Bisnis ....................... 54 

4.6. Tantangan dan Solusi dalam Perancangan CRM ......................... 55 

4.6.1. Tantangan Potensial yang Diidentifikasi ......................... 55 

4.6.2. Solusi yang Direkomendasikan ....................................... 56 

4.6.3. Pembelajaran dari Proses Perancangan ........................... 57 



**BAB V PENUTUP ............................................................................................ 58** 

5.1. Kesimpulan ................................................................................ 58 

5.2. Saran ........................................................................................... 61 



**DAFTAR PUSTKA ......................................................................................... 65 **

**DAFTAR RIWAYAT HIDUP ........................................................................ 67** 

****

****

****

****

****

****

****

vi 





**DAFTAR GAMBAR **

Halaman 

Gambar II. 1 Peran dan Aktifitas CRM ................................................................ 13 

Gambar III. 1 Kerangka Kerja .............................................................................. 20 

Gambar IV. 1 Komponen Utama Arsitektur ......................................................... 31 

Gambar IV. 2 Diagram Konteks Sistem CRM CUR-HEART .............................. 32 

Gambar IV. 3 Data Flow Diagram Level 0 ........................................................... 33 

Gambar IV. 4 Use Case Diagram Sistem CRM .................................................... 34 

Gambar IV. 5 Flowchart Proses Booking ............................................................. 36 

Gambar IV. 6 Flowchart Proses Dokumentasi Sesi .............................................. 37 

Gambar IV. 7 Entity Relationship Diagram \(ERD\) .............................................. 38 

Gambar IV. 8 Profil Client Dashboard ................................................................. 40 

Gambar IV. 9 Dokumentasi Sesi - Therapist Dashboard ...................................... 41 

Gambar IV. 10 Pesan - Client & Therapist Dashboard ......................................... 43 

Gambar IV. 11 Dashboard Kemajuan - Client Dashboard ................................... 44 

Gambar IV. 12 Halaman Ulasan - Client Dashboard & Therapist Profile ............ 46 

Gambar IV. 13 Dashboard Analitik CRM - Admin Dashboard ............................ 48 





vii 





**DAFTAR TABEL **

Halaman 

Tabel III. 1 Distribusi Subjek Penelitian ............................................................... 15 

Tabel III. 2 Daftar Narasumber Wawancara ......................................................... 16 

Tabel III. 3 Tahapan Penelitian ............................................................................. 19 

Tabel IV. 1 Layanan Terapi CUR-HEART .......................................................... 22 

Tabel IV. 2 Profil Pelanggan CUR-HEART ......................................................... 23 

Tabel IV. 3 Segmentasi Pelanggan CUR-HEART ............................................... 25 

Tabel IV. 4 Identifikasi Masalah Existing ............................................................ 26 

Tabel IV. 5 Kebutuhan Pengguna Berdasarkan Peran .......................................... 27 

Tabel IV. 6 Kebutuhan Fungsional Sistem CRM ................................................. 27 

Tabel IV. 7 Kebutuhan Non-Fungsional Sistem CRM ......................................... 29 

Tabel IV. 8 Analisis Kelayakan Sistem CRM ...................................................... 30 

Tabel IV. 9 Penilaian Kelayakan Fitur CRM ........................................................ 50 

Tabel IV. 10 Proyeksi Kepuasan Klien ................................................................. 51 

Tabel IV. 11 Metrik Retensi Klien ........................................................................ 52 

Tabel IV. 12 Efisiensi Operasional ....................................................................... 53 

Tabel IV. 13 Metrik Kinerja Bisnis ....................................................................... 54 

Tabel IV. 14 Tantangan Potensial Implementasi CRM ........................................ 55 

Tabel IV. 15 Solusi yang Direkomendasikan untuk Tantangan CRM .................. 56 

****

****

viii 





**DAFTAR SIMBOL **

**Simbol *Entity Relationship Diagram *****\(ERD\)** **NO **

**GAMBAR **

**NAMA **

**KETERANGAN **

Simbol yang menyatakan himpunan 

entitas ini bisa berupa : suatu elemen 

****

lingkungan, sumber daya, atau 

1 

*Entity *



transaksi, yang begitu pentingnya 

bagi 

perusahaan 

sehingga 

didokumentasikan dengan data. 

Simbol 

terminal 

ini 

untuk 

****

2 

*Attribute *

menunjukkan nama-nama atribut 



yang ada pada entity. 

Simbol atribut yang digaris bawahi, 

****

*Primary Key *

berfungsi sebagai key \(kunci\) di 

3 



*Attribute *

antara nama-nama atribut yang ada 

pada suatu entity. 

Simbol ini menyatakan relasi ini 

digunakan untuk menunjukkan 

4 

*Relationship *

hubungan yang ada antara entity 



yang satu dengan entity yang 

lainnya. 

Simbol berupa garis ini digunakan 

sebagai penghubung antara entity 

5 



*Link *

dengan atributnya dan himpunan 

entitas dengan himpunan relasi. 



ix 





**BAB I **

**PENDAHULUAN **



**1.1. Latar Belakang Masalah **

Teknologi mempunyai peran penting di era saat ini dengan perkembangan yang sangat pesat hingga hadirnya *AI \(Artificial Intelligence\) * yang menuntut manusia untuk beradaptasi dan menerima perubahan dikehidupan sehari-hari, sehingga persaingan bisnis semakin ketat dan menuntut pemilik usaha untuk terus melakukan perubahan dalam proses bisnis menjadi digitalisasi untuk mendapatkan hasil yang maksimal, akurat dan efisien. Di tengah meningkatnya kebutuhan akan layanan kesehatan mental, CUR-HEART \(Pusat Hipnoterapi & Kesehatan Mental\) hadir sebagai pusat layanan terapi kesehatan mental yang mengintegrasikan pendekatan hipnoterapi modern dengan nilai-nilai spiritualitas dan humanisme. CUR-HEART 

menyediakan berbagai layanan terapi seperti Pelepasan Stres & Kecemasan, Penyembuhan Trauma, Kepercayaan Diri & Motivasi, Tidur & Relaksasi, Pemrograman Ulang Kebiasaan, dan Pengelolaan Fobia & Ketakutan. Dalam industri layanan kesehatan mental, hubungan antara terapis dan klien merupakan faktor kunci yang menentukan keberhasilan terapi. 

*Customer Relationship Management* \(CRM\) adalah kegiatan usaha dan strategi yang berhubungan dengan seluruh sumber daya untuk menyusun, mengelola, dan mempertahankan hubungan dengan pelangan yang ada, dalam mengetahui kebutuhan dan kemauan pelanggan \[1\]. Dalam konteks layanan kesehatan mental, CRM tidak hanya berfungsi sebagai alat untuk meningkatkan kepuasan pelanggan, tetapi juga sebagai instrumen untuk meningkatkan kualitas perawatan, kontinuitas terapi, dan hasil kesehatan yang lebih baik. 

Perancangan CRM pada sistem informasi CUR-HEART ditujukan untuk mengatasi berbagai tantangan dalam manajemen hubungan pelanggan, seperti : 1. Personalisasi Layanan : Setiap klien memiliki kebutuhan terapi yang unik. 

Sistem CRM memungkinkan terapis untuk mengakses riwayat lengkap klien, preferensi komunikasi, dan kemajuan terapi untuk memberikan layanan yang dipersonalisasi. 

2. Kontinuitas Perawatan : Dokumentasi sesi terapi yang terstruktur dan 1 





2 



terintegrasi memastikan kontinuitas perawatan, terutama ketika klien berinteraksi dengan berbagai terapis atau staf administrasi. 

3. Komunikasi Proaktif : Sistem notifikasi otomatis dan pengingat membantu menjaga komunikasi yang konsisten dengan klien, mengurangi tingkat ketidakhadiran \( *no-show*\), dan meningkatkan kepatuhan terhadap rencana terapi. 

4. Analisis Kepuasan Pelanggan : Fitur ulasan dan penilaian memungkinkan CUR-HEART untuk mengukur kepuasan klien secara sistematis dan mengidentifikasi area perbaikan layanan. 

5. Segmentasi Pelanggan : Kemampuan untuk mengelompokkan klien berdasarkan karakteristik demografis, jenis layanan, atau tahap perjalanan terapi memungkinkan strategi pemasaran dan komunikasi yang lebih efektif. 

Penelitian ini mengkaji perancangan sistem CRM pada Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART. Sistem dirancang dengan pendekatan *user-centered design* dan mencakup berbagai fitur CRM seperti manajemen profil klien, riwayat interaksi, dokumentasi sesi terapi, sistem komunikasi terintegrasi, dan analitik kepuasan pelanggan. Validasi perancangan dilakukan melalui simulasi dan pengujian desain untuk mengevaluasi *fungsionalitas, usability*, dan proyeksi dampak terhadap bisnis. 

Dengan perancangan CRM yang efektif dan hasil validasi desain yang positif, rancangan ini diharapkan dapat menjadi dasar implementasi penuh yang akan meningkatkan kepuasan klien, memperkuat loyalitas, meningkatkan retensi, dan pada akhirnya mencapai tujuan bisnis jangka panjang sambil memberikan dampak positif terhadap kesehatan mental masyarakat. 



**1.2. Rumusan Masalah **

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian ini adalah : 

1. Bagaimana konsep dan strategi *Customer Relationship Management* \(CRM\) yang sesuai untuk diterapkan pada layanan kesehatan mental di CUR-HEART? 

## 2. Bagaimana perancangan fitur-fitur CRM pada Sistem Informasi 





3 



Manajemen Reservasi dan Terapi CUR-HEART untuk mendukung pengelolaan hubungan pelanggan yang efektif? 

3. Bagaimana hasil validasi perancangan dan proyeksi dampak CRM terhadap kepuasan klien, retensi pelanggan, dan kinerja bisnis CUR-HEART? 

4. Apa saja tantangan dan hambatan dalam perancangan CRM pada layanan kesehatan mental, serta bagaimana strategi untuk mengatasinya? ** **

****

**1.3. Tujuan Penelitian **

Tujuan dari penelitian ini adalah: 

1. Menganalisis konsep dan strategi *Customer Relationship Management* \(CRM\) yang sesuai untuk layanan kesehatan mental di CUR-HEART. 

2. Merancang fitur-fitur CRM pada Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART, termasuk arsitektur sistem, desain database, dan antarmuka pengguna. 

3. Mengevaluasi proyeksi dampak perancangan CRM terhadap kepuasan klien, retensi pelanggan, dan kinerja bisnis CUR-HEART melalui simulasi dan validasi desain. 

4. Mengidentifikasi tantangan dan hambatan dalam perancangan CRM pada layanan kesehatan mental serta merumuskan rekomendasi strategi untuk implementasi di masa depan. 



**1.4. Manfaat Penelitian **

Penelitian ini diharapkan memberikan manfaat kepada berbagai pihak : **1.4.1. Manfaat Teoritis **

1. Kontribusi Akademik** **: Menambah literatur dan pengetahuan tentang perancangan CRM dalam konteks layanan kesehatan mental, khususnya hipnoterapi. 

2. Pengembangan Model : Menghasilkan model perancangan CRM yang dapat diadaptasi untuk layanan kesehatan mental lainnya. 

3. Referensi Penelitian** **: Menjadi referensi bagi penelitian selanjutnya tentang CRM dalam industri kesehatan. 





4 



**1.4.2. Manfaat Praktis **

1. Bagi CUR-HEART : 

a. Meningkatkan pemahaman tentang kebutuhan dan preferensi klien melalui data yang terstruktur 

b. Meningkatkan efisiensi operasional dalam pengelolaan hubungan pelanggan 

c. Meningkatkan kepuasan dan loyalitas klien melalui layanan yang dipersonalisasi 

d. Meningkatkan retensi klien dan mengurangi tingkat * churn* e. Mendukung pengambilan keputusan strategis berbasis data pelanggan 2. Bagi Klien : 

a. Mendapatkan pengalaman layanan yang lebih personal dan sesuai kebutuhan 

b. Meningkatkan kontinuitas perawatan melalui dokumentasi yang terintegrasi 

c. Kemudahan komunikasi dengan terapis dan staf administrasi d. Transparansi dalam pelacakan kemajuan terapi 

e. Meningkatkan kepercayaan terhadap layanan CUR-HEART 

3. Bagi Terapis : 

a. Akses mudah ke riwayat lengkap klien untuk memberikan terapi yang lebih efektif 

b. Efisiensi dalam dokumentasi dan komunikasi dengan klien c. Wawasan tentang pola dan tren dalam praktik terapi mereka d. Meningkatkan kualitas hubungan terapeutik dengan klien 4. Bagi Industri Kesehatan Mental : 

a. Model *best practice* perancangan CRM untuk layanan kesehatan mental b. Demonstrasi potensi manfaat digitalisasi dalam meningkatkan kualitas layanan 

c. Inspirasi untuk inovasi dalam pengelolaan hubungan pelanggan di sektor kesehatan 





5 



**1.5. Ruang Lingkup Penelitian** 

Untuk memfokuskan pembahasan, penelitian ini dibatasi pada ruang lingkup sebagai berikut : 

**1.5.1. Ruang Lingkup Objek Penelitian **

Penelitian ini berfokus pada perancangan CRM di CUR-HEART \(Pusat Hipnoterapi & Kesehatan Mental\) yang berlokasi di Jl. Raya Cilodong No. 88, Depok, Jawa Barat. 

**1.5.2. Ruang Lingkup Sistem **

Penelitian ini mengkaji fitur-fitur CRM yang dirancang pada prototipe Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART, meliputi : 1. Manajemen Profil Klien : Penyimpanan dan pengelolaan data demografis, preferensi, dan riwayat klien 

2. Manajemen Interaksi : Pencatatan semua titik sentuh \( *touchpoint*\) antara klien dengan CUR-HEART 

3. Dokumentasi Sesi Terapi : Sistem pencatatan terstruktur untuk setiap sesi terapi 

4. Sistem Komunikasi : Notifikasi email, pesan dalam aplikasi, dan komunikasi terapis-klien 

5. Pelacakan Kemajuan : Visualisasi kemajuan terapi dan pencapaian tujuan klien 6. Ulasan dan Penilaian : Sistem *feedback* untuk mengukur kepuasan klien 7. Segmentasi Pelanggan : Pengelompokan klien berdasarkan berbagai kriteria 8. Analitik CRM : *Dashboard* untuk monitoring aktivitas dan performa sistem CRM 

**1.5.3. Ruang Lingkup Pengguna **

Penelitian ini melibatkan tiga kategori pengguna utama : 1. Klien : Pengguna layanan terapi CUR-HEART 

2. Terapis : Penyedia layanan terapi hipnoterapi 

3. Admin/Manajemen : Pengelola operasional dan pengambil keputusan **1.5.4. Ruang Lingkup Waktu **

Penelitian ini mengkaji perancangan sistem CRM selama periode September - Desember 2025, dengan validasi desain berdasarkan simulasi dan pengujian terbatas. 





6 



**1.5.5. Batasan Penelitian **

Penelitian ini tidak mencakup : 

1. Implementasi penuh sistem CRM dalam lingkungan produksi \(fokus pada perancangan dan validasi desain\) 

2. Perancangan integrasi dengan *platform* media sosial eksternal 3. Perancangan integrasi dengan sistem CRM pihak ketiga \( *Salesforce,* *HubSpot*, dll.\) 

4. Perancangan analisis prediktif lanjutan menggunakan machine learning 5. Perancangan *chatbot* AI untuk layanan pelanggan 6. Analisis mendalam tentang aspek klinis dan efektivitas terapi \(fokus pada aspek manajemen hubungan pelanggan\) 

7. Pengujian dengan data riil dalam skala besar \(menggunakan data simulasi untuk validasi desain\) 



**1.6. Sistematika Penulisan **

Makalah ini disusun dengan sistematika sebagai berikut : **BAB I PENDAHULUAN **

Bab ini menguraikan latar belakang penelitian, rumusan masalah, tujuan penelitian, manfaat penelitian, ruang lingkup penelitian, dan sistematika penulisan. 



**BAB II TINJAUAN PUSTAKA **

Bab ini membahas landasan teori yang relevan dengan penelitian, meliputi konsep *Customer Relationship Management* \(CRM\), CRM dalam industri kesehatan, strategi CRM, teknologi CRM, serta penelitian terkait. 



**BAB III METODOLOGI PENELITIAN **

Bab ini menjelaskan metode penelitian yang digunakan, termasuk pendekatan penelitian, teknik pengumpulan data, teknik analisis data, dan tahapan penelitian. 

****

****

****





7 



**BAB IV HASIL DAN PEMBAHASAN **

Bab ini menyajikan hasil penelitian berupa profil CUR-HEART, strategi CRM 

yang dirancang, perancangan fitur-fitur CRM pada sistem informasi, validasi perancangan dan proyeksi dampak, serta analisis tantangan dan solusi. 



**BAB V PENUTUP **

Bab ini berisi kesimpulan dari hasil penelitian dan saran untuk pengembangan lebih lanjut. 



**DAFTAR PUSTAKA **

Berisi daftar referensi yang digunakan dalam penulisan makalah. 





**BAB II **

****

**TINJAUAN PUSTAKA **

****

**2.1. * CUSTOMER RELATIONSHIP MANAGEMENT***** \(CRM\)** **2.1.1. Pengertian *Customer Relationship Management ***

*Customer Relationship Management *\(CRM\) adalah mengatur hubungan antara pelanggan dan perusahaan yang keduanya mendapatkan nilai maksimal dari hubungan yang sudah dibangun\[1\]. 

CRM atau *Customer Relationship Management * merupakan sebuah *system* atau dalam sebuah proses dimana kita dapat mempelajari sebuah informasi secara rinci dan mendetail terkait pelanggan \[2\] 

CRM adalah suatu pendekatan untuk melakukan pengelolaan hubungan korporasi dengan konsumen/pelanggan\[3\] . 

Sistem CRM mengumpulkan data dari berbagai saluran komunikasi, termasuk situs web perusahaan, telepon, email, media sosial, dan interaksi langsung dengan staf penjualan dan layanan. 

**2.1.2. Tujuan *Customer Relationship Management ***

Tujuan dari CRM menurut antara lain \[2\] : 

a. Memanfaatkan hubungan yang terjalin antara pihak perusahaan dengan pelanggan sehingga perusahaan bisa meningkatkan pendapatan yang dimaksudkan perusahaan dapat melakukan hubungan dengan melakukan *up-selling* atau *cross-selling* hingga pada waktu yang sama, perusahaan dapat meningkatkan pendapatan lalu menarik perhatian pelanggan yang dapat mempertahankan pelanggan terbaik dan loyal. 

b. Penggunaan Informasi yang terintegrasi dalam melakukan pelayanan yang memuaskan. Menggunakan informasi telah diperoleh dari pelanggan untuk dapat meningkatkan pelayanan yang lebih baik dengan kebutuhan pelanggan, pihak perusahaan juga dapat menghemat waktu dari pelanggan sendiri dan meminimalisir adanya kekecewaan yang terjadi dari pelanggan. 

c. Terciptanya proses dan prosedur dengan konsisten dan berulang. Tanpa memperhatiakan ukuran dan kekompleks, pihak perusahaan perlu 8 



9 



meningkatkan konsistensi dari proses dan juga peraturan dalam pengaturan terhadap pelayanan, pemasaran juga penjualan. 

**2.1.3. Kerangka Komponen *Customer Relationship Management ***

CRM terdiri dari tiga komponen utama \[4\] : 

A. Operasional CRM 

Operasional CRM dikenal sebagai *front office * di dalam perusahaan. Komponen CRM ini mempunyai peran dalam interaksi hubungan pelanggan. Operasional CRM mempunyai cakupan proses otomatisasi yang terintegrasi dari keseluruhan dalam proses bisnis, seperti otomatisasi pemasaran dan pelayanan. Salah satu dalam penerapan CRM yang termasuk dalam kategori operasionl CRM yaitu dalam bentuk aplikasi web. Melalui web, suatu perushaan dapat memberikan pelayanan kepada pelanggan. 

B. Analitikal CRM * *

Analitikal CRM dikenal sebagai *back office* perusahaan. Komponen CRM ini dapat berperan memahami kebutuhan pelanggan. Analitikal CRM mempunyai peran dalam melaksanakan analisis pelanggan dan pasar, seperti analisis dalam tren pasar dan analisis kebutuhan maupun perilaku pelanggan. Data yang digunakan dalam CRM analitik yaitu data yang berasal dari CRM Operasional C. *Collaborative* CRM 

Komponen ini meliputi *e-mail*, *persomalized publishing*, *ecommunities*, dan lain-lain yang dirancang untuk interaksi antara pelanggan dengan perusahaan. 

Tujuan utama yaitu memberikan nilai tambah dan memperluas loyalitas pelanggan ke pelanggan lain yang masih belum ada di level kesetiaan pelanggan. 

*Collaborative* CRM juga mencakup pemahaman atau kesadaran untuk pelanggan yang setia dapat menjadi daya tarik bagi pelanggan lain. 

**2.1.4. Manfaat *Customer Relationship Management***** **

Manfaat CRM yang diinginkan tidak berbeda jauh diseluruh organisasi. 

Hampir semua bisnis dapat memperoleh manfaat dari pendekatan komprehesif terhadap CRM antara lain\[4\] : 

**1. Manfaat Untuk Organisasi :** 

Mengumpulkan semua informasi yang dibutuhkan didalam suatu basis data yang tersedia dengan sistem CRM yang dapat mengurangi jumlah kesalahan dalam kemungkinan yang dilakukan organisasi yang berurusan dengan pelanggan. 



10 



**2. Manfaat Untuk Pelanggan : **

Pelanggan mendapatkan manfaat dari sistem CRM karena peningkatan efisiensi dan efektivitas pelayanan pelanggan. Ketika salah satu pelanggan melakukan pemedanan atau meminta bantuan, dia tidak harus menunggu orang yang “tepat” 

dalam membantu, karena siapapun yang memiliki akese ke sistem CRM dapat memberikan bantuan. Hal ini dapat meningkatkan efisiensi dan mendapatkan loyalitas pelanggan dan pelanggan akan merasa organisasi sangat mengetahui kebutuhan, keinginan dan harapan pelanggan. 

**3. Manfaat Untuk Karyawan : **

CRM dapat membantu karyawan dalam pemberdayaan untuk membantu pelanggan lebih banyak, yang dapat memungkinkan karyawan untuk melakukan pekerjaan yang lebih baik, membatasi beberapa sumber ketidakpuasan dan meningkatkan dalam pekerjaan. CRM menyediakan sistem peringatan dini untuk efektivitas karyawan dalam menghindari masalah sebelum menjadi meyebar luas. 



**2.2. CRM dalam Industri Kesehatan **

**2.2.1. Karakteristik Khusus CRM Kesehatan **

Implementasi CRM dalam industri kesehatan yaitu\[5\] : 

1. Mempercepat dalam proses pelayanan terhadap pasien** **

2. Meningkatkan transparansi hingga kepercayaan oleh pasien dalam layanan yang diberikan** **

3. Sistem CRM dapat membantupihak klinik atau laboratorium dalam memantau kinerja para staf, pengelola jadwal pasien, serta dapat melakukan peningkatan segmentasi pasar yang lebih baik ** **

**2.2.2. Optimalisasi dan Manajemen Layanan Kesehatan **

Optimalisasi dapat diartikan sebagai usaha secara sistematis dalam mencapai hasil yang terbaik dengan efektif dan efisien. Dalam konteks manajemen pelayanan kesehatan, optimalisasi menghungkan dengan fasilitas kesehatan dalam pengelola sumber daya dan proses kerja untuk mampu memberikan pelayanan yang berkualitas tinggi. Manajemen yang baik meliputi perencanaan, pengorganisasian, pelaksanaan, dan pengawasan dalam seluruh aktivitas pendukung pelayanan kepada pasien \[6\] . 

****

****

****



11 



**2.3. Strategi CRM **

**2.3.1. Siklus Hidup Pelanggan \( *Customer Life Cycle*****\)** Siklus hidup pelanggan \( *Customer Life Cycle*\) adalah sebuah busur yang dibentuk dari pelanggan yang pertama kali mempelajari perusahaan dan produk anda menuju yang memiliki tujuan akhir yaitu loyalitas pelanggan, siklus hidup pelanggan dan membahas tentang bagaimana perusahaan mencari pelanggan, mempertahankan pelanggan dan mengembangkan pelanggan yang sudah ada\[7\] . 

**2.3.2. Segmentasi Pelanggan **

Segmentasi pelanggan adalah salah satu faktor penting dalam meningkatkan penjualan karena tingkat signifikan segmentasi akan mempengaruhi sejauh mana peningkatan penjualan dapat tercapai\[8\] . Dalam konteks CUR-HEART, segmentasi dapat dilakukan berdasarkan: 

1. **Demografis **: Usia, jenis kelamin, lokasi geografis, tingkat pendidikan, pekerjaan. 

2. **Psikografis **: Gaya hidup, nilai-nilai, kepribadian, motivasi mencari terapi. 

3. **Perilaku **: Frekuensi kunjungan, jenis layanan yang digunakan, tingkat *engagement*. 

4. **Nilai Pelanggan **: *Customer Lifetime Value* \(CLV\), profitabilitas, potensi pertumbuhan. 

5. **Tahap Perjalanan **: Pelanggan baru, pelanggan aktif, pelanggan tidak aktif, pelanggan *churn*. 

**2.3.2. Personalisasi Layanan **

Personalisasi layanan adalah pendekatan yang memungkinkan sistem mengenali minat pengguna dan memberikan rekomendasi produk yang sesuai dengan kebutuhan individu secara otomatis. Personalisasi ini meningkatkan pengalaman pelanggan dan juga memperkuat loyalitas terhadap platform yang digunakan\[9\] . 

Strategi personalisasi meliputi: 

1. **Personalisasi Konten **: Menyesuaikan informasi dan rekomendasi berdasarkan profil dan riwayat pelanggan. 

2. **Personalisasi Komunikasi **: Menyesuaikan frekuensi, saluran, dan gaya komunikasi dengan preferensi pelanggan. 

3. **Personalisasi Layanan **: Menyesuaikan pendekatan terapi dan intervensi dengan kebutuhan unik setiap klien. 



12 



4. **Personalisasi Penawaran **: Menawarkan paket atau diskon yang disesuaikan dengan segmen pelanggan. 

**2.4. Teknologi CRM **

**2.4.1. Sistem Informasi CRM **

Sistem informasi CRM adalah suatu alat yang dapat menghasilkan data dari pelanggan, dan menganalisisnya untuk memberi informasi dalam mengetahui siapa pelanggan yang paling tetap, siapa pelanggan yang paling memberikan keuntungan dan produk apa saja yang diminati untuk dibeli oleh pelanggan yang dapat menguntungkan\[10\] . Komponen utama sistem CRM meliputi: 1. **Database Pelanggan **: Repositori terpusat untuk menyimpan semua data pelanggan. 

2. **Antarmuka Pengguna **: *Interface * untuk berbagai pengguna \(sales, marketing, *customer service*\) untuk mengakses dan mengelola data pelanggan. 

3. **Modul Fungsional **: Modul untuk sales *automation*, marketing *automation*, dan *customer service automation*. 

4. **Analitik dan Pelaporan **: *Tools * untuk analisis data pelanggan dan pembuatan laporan. 

5. **Integrasi **: Kemampuan untuk terintegrasi dengan sistem lain \( *ERP*, email, media sosial, dll.\). 

**2.4.2. Peran Sistem Informasi CRM **

Sistem Informasi CRM terdapat 3 peran dalam pengelolaan hubungan pelanggan yang saling berhubungan satu sama lain dalam suatu jaringan, antara lain\[10\] : 1. CRM Operasional** **terdiri atas proses bisnis dan otomatisasi yang dapat membantu dalam peningkatan efisiensi dan akurasi operasi sehari-hari yang dihadapi oleh pelanggan. 

2. CRM Analitikal** **merupakan analisis data pelanggan yang dihasilkan sebelumnya oleh aplikasi CRM operasional dalam memberikan informasi untuk meningkatkan kinerja bisnis. 

3. CRM Strategis** **mencakup proses pengembangan strategi dan penciptaan nilai. 





13 





**Gambar II. 1 Peran dan Aktifitas CRM **

**2.5. Metrik dan KPI CRM **

**2.5.1. Retensi dan Loyalitas **

Retensi Pelanggan yaitu salah satu indikator utama mendapatkan keberhasilah perusahaan dalam membangun hubungan jangka panjang dengan konsumen\[11\] . 

CRM meningkatkan loyalitas pelanggan ada beberapa aspek : a\) Personalisasi Layanan 

b\) Komunikasi Yang Efektif 

c\) Pemanfaatan Data Pelanggang 

**2.5.2. Metrik Kepuasan Pelanggan **

Metrik untuk mengukur kepuasan pelanggan meliputi\[12\] : 1. *Customer Satisfaction Score* \(CSAT\)** **: Skor kepuasan pelanggan yang diberikan berdasarkan interaksi layanan pelanggan. 

2. *Net Promoter Score* \(NPS\) : Mengukur kemungkinan pelanggan bersedia merekomendasikan layanan atau produk. 

3. *Customer Effort Score* \(CES\) : Mengukur nilai dalam kemudahan pelanggan dalam berinteraksi dengan perusahaan. 

4. Tingkat Retensi Pelanggan : Tingkat dimana pelanggan tetap setia dan tidak pindah ke perusahaan competitor. 





**BAB III **

**METODOLOGI PENELITIAN **

****

**3.1. Jenis Penelitian **

Penelitian ini menggunakan pendekatan penelitian deskriptif kualitatif dengan metode studi kasus \( *case study*\). Penelitian deskriptif bertujuan untuk menggambarkan secara sistematis fakta dan karakteristik objek atau subjek yang diteliti secara tepat. 

Studi kasus dipilih karena penelitian ini berfokus pada perancangan CRM pada satu organisasi spesifik, yaitu CUR-HEART, dengan tujuan memahami secara mendalam bagaimana CRM dirancang dalam konteks layanan kesehatan mental. 

Studi Kasus merupakan terjemahan dari Bahasa Inggris “*Case Study*” yaitu mempelajari suatu kejadian, situasi dan peristiwa yang biasa disebut dengan fenomena sosial yang bertujuan untuk memperkenalkan ciri khas dan keunikan karakteristik yang terdapat dalam kasus yang diteliti \[13\] . Penelitian ini mengkaji bagaimana CRM 

dirancang pada sistem informasi CUR-HEART dan mengapa strategi tertentu dipilih, serta proyeksi dampaknya terhadap kepuasan klien dan kinerja bisnis. 



**3.2. Objek Penelitian **

Objek penelitian ini adalah perancangan *Customer Relationship Management* \(CRM\) pada Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART \(Pusat Hipnoterapi & Kesehatan Mental\) yang berlokasi di Jl. Raya Cilodong No. 88, Depok, Jawa Barat. 

CUR-HEART adalah pusat layanan terapi kesehatan mental yang mengintegrasikan pendekatan hipnoterapi modern dengan nilai-nilai spiritualitas dan humanisme. Perusahaan ini menyediakan berbagai layanan terapi seperti : a. *Stress *& *Anxiety Release Therapy* 

b. *Trauma Healing Hypnotherapy *

c. *Self-Confidence* & *Motivation Therapy* d. *Sleep* & *Relaxation Therapy* 

e. *Habit Reprogramming Therapy *

f. *Phobia *& *Fear Management* 

14 





15 



**3.3. Subjek Penelitian **

Subjek penelitian ini terdiri dari pemangku kepentingan yang terlibat dalam penggunaan sistem CRM CUR-HEART : 

**Tabel III. 1 **Distribusi Subjek Penelitian** **

**Kriteria **

**Peran dalam **

**No **

**Kategori Subjek **

**Jumlah **

**Pemilihan **

**Penelitian **

Pengambil 

Memberikan 

keputusan, 

1 

Pemilik/Manajemen 

1 orang 

perspektif 

memahami 

visi 

strategis CRM 

bisnis 

Memberikan 

Berpengalaman 

*feedback *

minimal 1 tahun, 

2 

Terapis 

3 orang 

tentang 

fitur 

pengguna 

aktif 

CRM 

untuk 

sistem 

terapis 

Mengelola 

Memberikan 

reservasi 

dan 

perspektif 

3 

Staf Admin/CS 

2 orang 

administrasi 

operasional 

harian 

CRM 

Memberikan 

Pernah 

*feedback *

menggunakan 

4 

Klien Aktif 

5 orang 

tentang 

layanan minimal 

pengalaman 

2 kali 

pelanggan 

**Total** 

**11 orang** 

Teknik pengambilan sampel menggunakan **purposive sampling** \(pengambilan sampel bertujuan\) dimana subjek dipilih berdasarkan pengetahuan dan pengalaman mereka terhadap sistem CRM CUR-HEART. 





16 



**3.4. Teknik Pengumpulan Data **

Penelitian ini menggunakan pendekatan multi-metode untuk memastikan pemahaman yang komprehensif. Teknik pengumpulan data yang digunakan meliputi : **3.4.1. Observasi **

Observasi dilakukan untuk memahami bagaimana fitur-fitur CRM digunakan dalam operasional sehari-hari CUR-HEART. Observasi dilakukan secara langsung dengan mengamati : 

a. Proses interaksi antara staf administrasi dengan klien melalui sistem b. Cara terapis menggunakan fitur dokumentasi sesi terapi c. Penggunaan dashboard CRM oleh manajemen untuk monitoring d. Proses komunikasi antara terapis dan klien melalui sistem pesan e. Penggunaan fitur pelacakan kemajuan terapi oleh klien Hasil observasi didokumentasikan dalam catatan lapangan \( *field notes*\) dan *screenshot* sistem. 

**3.4.2. Wawancara Mendalam **

Wawancara semi-terstruktur dilakukan untuk mendapatkan informasi mendalam dari pemangku kepentingan mengenai kebutuhan mereka terhadap fitur CRM dan ekspektasi terhadap sistem yang dirancang. Wawancara dilakukan kepada : **Tabel III. 2 Daftar Narasumber Wawancara **

**No **

**Narasumber **

**Jumlah **

**Topik Wawancara **

Pemilik CUR-

1 

1 orang 

Strategi CRM, dampak bisnis, ROI 

HEART 

Penggunaan fitur dokumentasi, 

2 

Terapis 

3 orang 

komunikasi dengan klien, pelacakan 

kemajuan 

Manajemen profil klien, penanganan 

3 

Staf Admin/CS 

2 orang 

interaksi, efisiensi operasional 

Pengalaman pengguna, kepuasan 

4 

Klien 

5 orang 

terhadap fitur CRM, saran perbaikan 





17 



Wawancara dilakukan dengan durasi 30-45 menit per narasumber dan didokumentasikan dalam bentuk transkrip wawancara. 

**3.4.3. Studi Dokumentasi **

Studi dokumentasi dilakukan untuk menganalisis dokumen-dokumen terkait perancangan CRM, meliputi : 

a. Dokumen desain sistem \(ERD, diagram UML, mockup UI/UX\) b. Dokumentasi teknis sistem \(kode sumber, API *documentation*\) c. Laporan proyek sistem informasi CUR-HEART 

d. Data penggunaan sistem \(log aktivitas, statistik penggunaan fitur\) e. Dokumen strategi bisnis dan CRM CUR-HEART 

**3.4.4. Kuesioner **

Kuesioner digunakan untuk mengumpulkan data kuantitatif tentang ekspektasi dan penilaian pengguna terhadap desain fitur CRM. Kuesioner dibagikan kepada : 1. Kuesioner Evaluasi Desain untuk Klien** **: Diberikan kepada 5 calon klien yang telah melihat simulasi sistem 

2. Kuesioner Evaluasi Desain untuk Terapis** **: Diberikan kepada 3 terapis yang telah mengevaluasi rancangan 

3. Kuesioner Evaluasi Desain untuk Admin** **: Diberikan kepada 2 staf admin yang telah mengevaluasi rancangan 

Kuesioner menggunakan skala Likert 1-5 untuk mengukur penilaian terhadap berbagai aspek desain fitur CRM. 

**3.4.5. Simulasi dan Validasi Desain **

Simulasi dan validasi desain dilakukan untuk menguji kelayakan perancangan sistem CRM, meliputi : 

1. Simulasi skenario penggunaan sistem \( *user journey*\) 2. Validasi struktur database dan relasi antar entitas 3. Validasi alur proses bisnis \( *flowchart * dan *DFD\)* 4. Pengujian mockup antarmuka pengguna \( *UI/UX*\) 5. Evaluasi kelengkapan fitur terhadap kebutuhan bisnis 





18 



**3.5. Teknik Analisis Data **

Data yang telah dikumpulkan dianalisis menggunakan beberapa teknik : **3.5.1. Analisis Deskriptif **

Analisis deskriptif digunakan untuk menggambarkan karakteristik data yang dikumpulkan, meliputi : 

1. Deskripsi profil subjek penelitian 

2. Deskripsi fitur-fitur CRM yang dirancang 

3. Deskripsi proyeksi pola penggunaan sistem 

## 4. Deskripsi penilaian desain oleh pengguna 

**3.5.2. Analisis Konten **

Analisis konten digunakan untuk menganalisis data kualitatif dari wawancara dan observasi. Proses analisis konten meliputi : 

1. Transkripsi** **: Mengubah rekaman wawancara menjadi teks 2. *Coding*** **: Memberikan kode pada segmen-segmen data yang relevan 3. Kategorisasi** **: Mengelompokkan kode-kode ke dalam kategori tema 4. Interpretasi : Menginterpretasikan makna dari kategori tema yang muncul **3.5.3. Analisis Komparatif **

Analisis komparatif digunakan untuk membandingkan : 

1. Kondisi proses existing dengan proyeksi setelah menggunakan CRM 

2. Perbedaan kebutuhan antar segmen pengguna 

## 3. Perbedaan penilaian desain antar fitur CRM 

**3.5.4. Analisis Metrik CRM **

Analisis metrik CRM dilakukan dengan menghitung berbagai indikator kinerja, meliputi : 

1. *Customer Satisfaction Score* \(CSAT\)** **: Rata-rata skor kepuasan klien 2. *Net Promoter Score* \(NPS\)** **: *Persentase promoter* dikurangi persentase detractor 

3. *Customer Retention Rate*** **: Persentase klien yang kembali menggunakan layanan 

4. *Customer Lifetime Value*** **\(CLV\) : Nilai total yang dihasilkan klien selama hubungan dengan CUR-HEART 

5. *Churn Rate*** **: Persentase klien yang berhenti menggunakan layanan 





19 



**3.6. Tahapan Penelitian **

Penelitian ini dilaksanakan dalam beberapa tahapan : 

**Tabel III. 3 **Tahapan Penelitian** **

**No **

**Tahapan **

**Aktivitas **

**Durasi **

**Output **

- Studi literatur 

- Identifikasi objek 

1 

Proposal 

1 

Persiapan 

penelitian 

minggu 

penelitian 

- Penyusunan 

proposal 

- Observasi sistem 

- Wawancara 

mendalam 

- Studi 

Pengumpulan 

2 

Data primer dan 

2 

dokumentasi 

Data 

minggu 

sekunder 

- Penyebaran 

kuesioner 

- Ekstraksi data 

sistem 

- Analisis deskriptif 

- Analisis konten 

- Analisis 

1 

Temuan 

3 

Analisis Data 

komparatif 

minggu 

penelitian 

- Analisis metrik 

CRM 

- Penulisan 

Penyusunan 

makalah 

1 

4 

Makalah final 

Laporan 

- Review dan revisi 

minggu 

- Finalisasi 

**Total** 

**5 minggu** 

****



****





20 



**3.7. Kerangka Kerja Analisis **

Kerangka kerja analisis yang digunakan dalam penelitian ini adalah : TAHAP 1: DESKRIPSI 

-

Profil CUR-HEART 



-

Strategi CRM yang dirancang 

-

Fitur-fitur CRM yang dirancang 





TAHAP 2 : EVALUASI 



-

Evaluasi penggunaan fitur CRM 



-

Evaluasi kepuasan pengguna 

-

Evaluasi dampak terhadap metrik bisnis 





TAHAP 3 : ANALISIS 



-

Identifikasi faktor keberhasilan 

-

Identifikasi tantangan dan hambatan 



-

Analisis gap antara harapan dan realitas 





TAHAP 4 : REKOMENDASI 



-

Rekomendasi perbaikan fitur CRM 

-

Rekomendasi strategi CRM 



-

Rekomendasi pengembangan masa depan 



**Gambar III. 1 Kerangka Kerja **

**3.8. **

**Validitas dan Reliabilitas **

Untuk memastikan validitas dan reliabilitas penelitian, dilakukan beberapa strategi : 

**3.8.1. Triangulasi **

Triangulasi dilakukan dengan menggunakan berbagai sumber data \(observasi, wawancara, dokumentasi, kuesioner\) dan berbagai subjek penelitian \(pemilik, terapis, admin, klien\) untuk memvalidasi temuan. 

**3.8.2. Member Checking **

Hasil wawancara dan interpretasi data dikonfirmasi kembali kepada narasumber untuk memastikan akurasi dan validitas. 





21 



**3.8.3. Audit Trail **

Semua proses penelitian didokumentasikan secara sistematis untuk memungkinkan audit dan verifikasi. 

***3.8.4. Peer Debriefing ***

Temuan penelitian didiskusikan dengan dosen pembimbing dan rekan sejawat untuk mendapatkan perspektif alternatif dan validasi. 



**3.9. **

**Etika Penelitian **

Penelitian ini mematuhi prinsip-prinsip etika penelitian : 1. *Informed Consent*** **: Semua subjek penelitian diberikan informasi lengkap tentang tujuan penelitian dan memberikan persetujuan untuk berpartisipasi. 

2. *Confidentiality*** **: Data pribadi subjek penelitian dijaga kerahasiaannya dan hanya digunakan untuk keperluan penelitian. 

3. *Anonymity*** **: Identitas subjek penelitian dapat dianonimkan jika diminta. 

4. *Voluntary Participation*** **: Partisipasi dalam penelitian bersifat sukarela dan subjek dapat mengundurkan diri kapan saja. 

5. Data *Protection** ***: Data penelitian disimpan dengan aman dan hanya dapat diakses oleh tim peneliti. 

****

****

****





**BAB IV **

**HASIL DAN PEMBAHASAN **

****

**4.1. Profil CUR-HEART \(Pusat Hipnoterapi & Kesehatan Mental\)** **4.1.1. Gambaran Umum Perusahaan **

CUR-HEART \(Pusat Hipnoterapi & Kesehatan Mental\) adalah pusat layanan terapi kesehatan mental yang berlokasi di Jl. Raya Cilodong No. 88, Depok, Jawa Barat. Perusahaan ini didirikan dengan visi menjadi pusat terapi kejiwaan berbasis hipnoterapi modern dan spiritual yang terpercaya, profesional, dan berpengaruh dalam membantu masyarakat Indonesia mencapai kesehatan mental, keseimbangan emosional, serta kualitas hidup yang lebih baik. 

**Visi :** Menjadi pusat terapi kejiwaan berbasis hipnoterapi modern dan spiritual yang terpercaya, profesional, dan berpengaruh dalam membantu masyarakat Indonesia mencapai kesehatan mental, keseimbangan emosional, serta kualitas hidup yang lebih baik. 

**Misi :** 

1. Memberikan layanan terapi kejiwaan yang aman, etis, dan ilmiah melalui metode hipnoterapi modern 

2. Meningkatkan kesadaran masyarakat tentang pentingnya kesehatan mental 3. Menciptakan ruang terapi yang nyaman, rahasia, dan humanis 4. Mengintegrasikan pendekatan sains dan spiritualitas dalam setiap program 5. Memberdayakan individu agar mampu mengelola pikiran bawah sadar secara mandiri 

6. Mengembangkan model bisnis berkelanjutan dengan memperluas layanan **4.1.2. Layanan yang Ditawarkan **

CUR-HEART menyediakan 6 layanan terapi utama : 

**Tabel IV. 1 Layanan Terapi CUR-HEART **

**No **

**Layanan **

**Deskripsi **

**Durasi **

**Harga **

Mengatasi 

stres 

*Stress & Anxiety *

berlebih, rasa cemas, 

90 

Rp 

1 

*Release Therapy *

panik, 

dan 

tekanan 

menit 

## 350.000 

### mental 

22 





23 



**No **

**Layanan **

**Deskripsi **

**Durasi **

**Harga **

Menghapus 

dampak 

*Trauma *

*Healing *

emosional 

dari 

120 

Rp 

2 

*Hypnotherapy *

pengalaman buruk masa 

menit 

## 450.000 

### lalu 

Meningkatkan 

rasa 

*Self-Confidence & *

90 

Rp 

3 

percaya 

diri 

dan 

*Motivation Therapy *

menit 

## 350.000 

### semangat hidup 

Mengatasi insomnia dan 

*Sleep & Relaxation *

90 

Rp 

4 

gangguan 

kecemasan 

*Therapy *

menit 

## 300.000 

### malam 

*Habit *

Mengubah 

kebiasaan 

90 

Rp 

5 

*Reprogramming *

negatif seperti merokok, 

menit 

## 350.000 

### ***Therapy ***

menunda pekerjaan 

Menangani rasa takut 

*Phobia *

*& *

*Fear *

90 

Rp 

6 

berlebihan 

terhadap 

*Management *

menit 

## 350.000 

### situasi tertentu 

**4.1.3. Struktur Organisasi **

CUR-HEART memiliki struktur organisasi yang sederhana namun efektif : 1. Pemilik/Direktur** **: Bertanggung jawab atas strategi bisnis dan pengambilan keputusan 

2. Manajer Operasional** **: Mengelola operasional harian dan koordinasi tim 3. Terapis \(3 orang\)** **: Memberikan layanan terapi kepada klien 4. Staf Administrasi/ *Customer Service* \(2 orang\)** **: Mengelola reservasi, komunikasi dengan klien, dan administrasi 

**4.1.4. Profil Pelanggan **

Berdasarkan data sistem, profil pelanggan CUR-HEART adalah : **Tabel IV. 2 Profil Pelanggan CUR-HEART **

**Karakteristik **

**Distribusi **

25-35 tahun \(45%\), 36-45 tahun \(30%\), 18-24 tahun \(15%\), **Usia** 

46\+ tahun \(10%\) 

**Jenis Kelamin** 

Perempuan \(65%\), Laki-laki \(35%\) 

**Lokasi** 

Depok \(40%\), Jakarta \(35%\), Bogor \(15%\), Lainnya \(10%\) 





24 



**Karakteristik **

**Distribusi **

Karyawan swasta \(50%\), Wiraswasta \(20%\), PNS \(15%\), **Pekerjaan** 

Mahasiswa \(10%\), Lainnya \(5%\) 

**Layanan **

Stress & Anxiety \(35%\), Trauma Healing \(25%\), Self-Populer 

Confidence \(20%\), Lainnya \(20%\) 

**4.2. Strategi *Customer Relationship Management***** CUR-HEART **

**4.2.1. Filosofi CRM CUR-HEART **

Strategi CRM CUR-HEART didasarkan pada filosofi " *Healing Through* *Connection*" yang menekankan bahwa hubungan terapeutik yang kuat adalah kunci keberhasilan terapi. Filosofi ini diterjemahkan ke dalam empat pilar utama: 1. Personalisasi** **: Setiap klien adalah unik dan memerlukan pendekatan yang dipersonalisasi 

2. Kontinuitas** **: Perawatan yang berkelanjutan dan terintegrasi sepanjang perjalanan terapi 

3. Komunikasi : Dialog yang terbuka, jujur, dan penuh empati 4. Pemberdayaan** **: Membantu klien menjadi mandiri dalam mengelola kesehatan mental mereka 

**4.2.2. Tujuan Strategis CRM **

Tujuan strategis perancangan CRM di CUR-HEART adalah: 

1. Meningkatkan Kepuasan Klien** **: Target CSAT ≥ 4.5/5.0 

2. Meningkatkan Retensi Klien** **: Target *retention rate* ≥ 80% 

3. Meningkatkan Loyalitas** **: Target NPS ≥ 50 

4. Meningkatkan Efisiensi Operasional** **: Mengurangi waktu administratif 50% 

5. Meningkatkan Kualitas Terapi** **: Melalui dokumentasi yang lebih baik dan kontinuitas perawatan 





25 



**4.2.3. Segmentasi Pelanggan **

CUR-HEART menerapkan segmentasi pelanggan berdasarkan beberapa kriteria : 

**Tabel IV. 3 Segmentasi Pelanggan CUR-HEART **

**Basis **

**Segmen **

**Karakteristik **

**Strategi CRM **

**Segmentasi **

Belum pernah 

Edukasi, 

Prospek 

menggunakan 

kemudahan 

layanan 

reservasi pertama 

*Onboarding* yang 

Klien Baru 

1-2 sesi 

baik, *follow-up *

*intensif* 

**Tahap **

**Perjalanan** 

Personalisasi, 

Klien Aktif 

3-10 sesi 

pelacakan kemajuan 

Program loyalitas, 

Klien Loyal 

>10 sesi 

*referral incentive* 

Klien Tidak 

Tidak ada sesi >3 

*Re-engagement *

Aktif 

bulan 

*campaign *

Layanan premium, 

*High Value *

CLV > Rp 5 juta 

prioritas 

**Nilai **

*Medium *

Layanan standar, 

CLV Rp 1-5 juta 

**Pelanggan** 

*Value *

*up-selling* 

Efisiensi, *self-*

*Low Value *

CLV < Rp 1 juta 

*service* 

*Stress *

*& *

Fokus pada 

Konten edukatif 

*Anxiety *

manajemen stres 

tentang stres 

**Jenis **

Trauma 

Fokus pada 

Dukungan jangka 

**Layanan** 

*Healing* 

pemulihan trauma 

panjang 

*Self-*

Fokus pada 

Program 

*Development *

pengembangan diri 

berkelanjutan 

**4.2.4. Strategi Personalisasi **

Strategi personalisasi CUR-HEART meliputi : 

1. Personalisasi Komunikasi** **: 

a. Menyapa klien dengan nama 

b. Menyesuaikan frekuensi dan saluran komunikasi dengan preferensi klien c. Mengirimkan konten yang relevan dengan kebutuhan terapi klien 





26 



2. Personalisasi Layanan : 

a. Matching klien dengan terapis yang sesuai berdasarkan spesialisasi dan preferensi 

b. Menyesuaikan pendekatan terapi dengan karakteristik klien c. Menawarkan jadwal yang fleksibel sesuai ketersediaan klien 3. Personalisasi Konten : 

a. Rekomendasi artikel blog yang relevan dengan kondisi klien b. Tips dan latihan yang disesuaikan dengan tujuan terapi c. Pengingat yang dipersonalisasi untuk sesi dan Latihan **4.3. Analisis Kebutuhan Sistem CRM **

**4.3.1. Identifikasi Masalah *Existing ***

Berdasarkan wawancara dengan pemangku kepentingan dan observasi proses bisnis existing di CUR-HEART, ditemukan beberapa permasalahan dalam manajemen hubungan pelanggan : 

**Tabel IV. 4 Identifikasi Masalah *Existing***** **

**No **

**Aspek **

**Masalah **

**Dampak **

Data klien tersebar di 

Sulit mencari riwayat 

**Manajemen **

1 

berbagai file Excel dan 

klien, 

data 

tidak 

**Data Klien** 

catatan manual 

terintegrasi 

Risiko hilang, sulit 

**Dokumentasi **

Catatan 

terapi 

masih 

2 

dibaca, 

tidak 

**Terapi** 

manual di buku/kertas 

terstruktur 

Komunikasi 

via 

Tidak ada riwayat 

3 

**Komunikasi** 

WhatsApp pribadi, tidak 

komunikasi, 

sulit 

terdokumentasi 

tracking 

Tingkat 

no-show 

**Follow-up **

Follow-up manual, sering 

4 

tinggi \(±30%\), klien 

**Klien** 

terlupa 

tidak kembali 

Tidak 

ada 

sistem 

Klien 

tidak 

tahu 

**Pelacakan **

5 

pelacakan 

kemajuan 

progress, 

motivasi 

**Kemajuan** 

terapi 

rendah 

Sulit 

mengukur 

Feedback tidak sistematis, 

6 

***Feedback***** Klien** 

kepuasan, tidak ada 

hanya verbal 

data untuk perbaikan 





27 



**No **

**Aspek **

**Masalah **

**Dampak **

Laporan 

manual, 

Keputusan bisnis tidak 

7 

**Analitik Bisnis** 

memakan waktu 2-3 jam 

berbasis data real-time 

**4.3.2. Analisis Kebutuhan Pengguna **

Berdasarkan wawancara dan kuesioner kepada 11 responden \(1 pemilik, 3 

terapis, 2 admin, 5 calon klien\), diperoleh kebutuhan pengguna sebagai berikut : **Tabel IV. 5 Kebutuhan Pengguna Berdasarkan Peran **

**Peran **

**Kebutuhan Utama **

**Prioritas **

- Kemudahan booking online 

- Akses riwayat sesi terapi 

**Klien** 

- Komunikasi mudah dengan terapis 

Tinggi 

- Melihat progress terapi 

- Memberikan * feedback* 

- Akses cepat ke profil klien 

- Dokumentasi sesi yang terstruktur 

**Terapis** 

- Komunikasi terintegrasi dengan klien 

Sangat Tinggi 

- Melihat jadwal dan booking 

- Notifikasi otomatis 

- Manajemen user dan layanan 

- Monitoring booking dan pembayaran 

**Admin** 

- Dashboard analitik 

Tinggi 

- Laporan otomatis 

- Manajemen komunikasi 

- Dashboard kinerja bisnis 

- Analitik kepuasan klien 

**Pemilik** 

- Laporan retensi dan churn 

Sangat Tinggi 

- ROI marketing 

- Proyeksi pendapatan 

**4.3.3. Kebutuhan Fungsional Sistem **

Kebutuhan fungsional adalah fitur-fitur yang harus ada dalam sistem CRM 

untuk memenuhi kebutuhan pengguna : 

**Tabel IV. 6 Kebutuhan Fungsional Sistem CRM **

**Kebutuhan **

**Kode **

**Deskripsi **

**Prioritas **

**Fungsional **

Sistem harus dapat mengelola 

***Manajemen ***

*Must *

**F-01** 

registrasi, login, dan profil user 

***User** *

*Have *

\(klien, terapis, admin\) 





28 



**Kebutuhan **

**Kode **

**Deskripsi **

**Prioritas **

**Fungsional **

Sistem harus dapat menyimpan data 

**Manajemen **

*Must *

**F-02** 

demografis, medis, preferensi, dan 

**Profil Klien** 

*Have *

riwayat klien secara komprehensif 

Sistem harus dapat mengelola 

**Manajemen **

*Must *

**F-03** 

pembuatan, konfirmasi, reschedule, 

**Booking** 

*Have *

dan pembatalan booking 

**Manajemen **

Sistem harus dapat mengelola 

*Must *

**F-04** 

**Jadwal Terapis** 

ketersediaan jadwal terapis 

*Have *

Sistem harus menyediakan formulir 

**Dokumentasi **

*Must *

**F-05** 

terstruktur 

untuk 

dokumentasi 

**Sesi Terapi** 

*Have *

setiap sesi terapi 

**Sistem **

Sistem 

harus 

menyediakan 

*Must *

**F-06** 

**Komunikasi** 

messaging antara klien dan terapis 

*Have *

Sistem harus mengirim notifikasi 

**Notifikasi **

*Must *

**F-07** 

email untuk konfirmasi booking, 

**Otomatis** 

*Have *

pengingat sesi, dll. 

**Pelacakan **

Sistem harus dapat menampilkan 

*Should *

**F-08** 

**Kemajuan** 

visualisasi kemajuan terapi klien 

*Have *

**Ulasan **

**dan **

Sistem harus dapat mengumpulkan 

*Should *

**F-09** 

**Rating** 

ulasan dan rating dari klien 

*Have *

Sistem 

harus 

menyediakan 

**Dashboard **

*Must *

**F-10** 

*dashboard* 

untuk 

monitoring 

**Analitik** 

*Have *

aktivitas dan metrik CRM 

**Manajemen **

Sistem harus dapat mencatat status 

*Should *

**F-11** 

**Pembayaran** 

pembayaran *booking* 

*Have *

**Laporan **

Sistem harus dapat *generate* laporan 

*Should *

**F-12** 

**Otomatis** 

secara otomatis 

*Have *

Sistem 

harus 

dapat 

**Segmentasi **

*Could *

**F-13** 

mengelompokkan klien berdasarkan 

**Klien** 

*Have *

kriteria tertentu 

Sistem harus dapat export data ke 

*Could *

**F-14** 

***Export***** Data** 

format *Excel*/PDF 

*Have *

Keterangan Prioritas** :** 

a. *Must Have*** **: Fitur wajib ada, sistem tidak berfungsi tanpa fitur ini b. *Should Have*** **: Fitur penting, sangat dibutuhkan tapi sistem masih bisa berjalan tanpanya 





29 



c. *Could Have*** **: Fitur *nice-to-have*, meningkatkan nilai tapi tidak krusial **4.3.4. Kebutuhan Non-Fungsional Sistem **

Kebutuhan non-fungsional adalah karakteristik kualitas sistem yang harus dipenuhi : 

**Tabel IV. 7 Kebutuhan Non-Fungsional Sistem CRM **

**Kode **

**Aspek **

**Kebutuhan **

**Metrik/Target **

- Waktu belajar ≤ 30 

Sistem harus mudah 

**NF-**

menit 

*Usability** ***

digunakan 

tanpa 

**01** 

- *Task completion rate* ≥ 

pelatihan khusus 

90% 

- *Page load time* ≤ 3 

**NF-**

Sistem harus responsif 

detik 

*Performance** ***

**02** 

dan cepat 

- *Response time* ≤ 2 

detik 

**NF-**

Sistem harus stabil dan 

- Uptime ≥ 99% 

*Reliability** ***

**03** 

tersedia 

- MTBF ≥ 720 jam 

- Enkripsi data \(AES-

256\) 

Sistem harus aman dan 

**NF-**

- HTTPS 

*Security** ***

melindungi 

data 

**04** 

- *Role-based access* 

sensitif 

*control* 

- *Compliance * UU PDP 

Sistem harus dapat 

- *Support* hingga 1000 

**NF-**

*Scalability** ***

menangani 

*user concurrent* 

**05** 

pertumbuhan user 

- *Database scalable* 

- 

Kode 

terstruktur 

Sistem harus mudah 

**NF-**

\(MVC\) 

*Maintainability** ***

dipelihara 

dan 

**06** 

- Dokumentasi lengkap 

dikembangkan 

- Modular design 

- *Responsive design* 

Sistem 

harus 

**NF-**

- 

*Support *

*browser* 

*Compatibility** ***

kompatibel 

dengan 

**07** 

*modern *

\( *Chrome, *

berbagai device 

*Firefox, Safari, Edge*\) 

- 

*Backup* 

otomatis 

**NF-**

*Backup *

*& *

Sistem harus memiliki 

harian 

**08** 

*Recovery** ***

mekanisme backup 

- *Recovery time* ≤ 4 jam 

Sistem harus 

- WCAG 2.1 Level AA 

**NF-**

*Accessibility** ***

*accessible* untuk 

- *Keyboard navigation* 

**09** 

semua *user* 

- *Screen reader friendly* 





30 



**Kode **

**Aspek **

**Kebutuhan **

**Metrik/Target **

- *Consent management* 

**NF-**

Sistem harus menjaga 

*Data Privacy** ***

- *Data anonymization* 

**10** 

privasi data klien 

- *Right to be forgotten* 

**4.3.5. Analisis Kelayakan **

Analisis kelayakan dilakukan untuk memastikan perancangan sistem CRM 

layak untuk diimplementasikan :** **

**Tabel IV. 8 Analisis Kelayakan Sistem CRM **

**Aspek **

**Analisis **

**Kesimpulan **

**Kelayakan **

- Teknologi yang digunakan \(Laravel, 

MySQL\) sudah mature dan terbukti 

**Kelayakan **

- Tim memiliki kompetensi teknis yang 

Layak 

**Teknis** 

memadai 

- Infrastruktur *server* tersedia \( *cloud *

*hosting*\) 

- *User* sudah familiar dengan sistem 

**Kelayakan **

digital 

Layak 

**Operasional** 

- Manajemen mendukung digitalisasi 

- Proses bisnis existing dapat diadaptasi 

- Investasi: Rp 7.560.000 

- Proyeksi ROI: ≥ 500% 

**Kelayakan **

- Payback period: ≤ 3 bulan 

Layak 

**Ekonomi** 

- Penghematan biaya operasional: Rp 33 

juta/tahun 

- *Compliance* dengan UU PDP No. 27 

**Kelayakan **

Tahun 2022 

Layak 

**Hukum** 

- Perjanjian kerahasiaan dengan klien 

- Lisensi *software* legal 

- Estimasi pengembangan: 3-4 bulan 

- *Timeline * realistis dengan *resource* yang **Kelayakan **

ada 

Layak 

**Jadwal** 

- Implementasi bertahap mengurangi 

risiko 

Kesimpulan Analisis Kelayakan** **: Berdasarkan analisis kelayakan dari aspek teknis, operasional, ekonomi, hukum, dan jadwal, perancangan sistem CRM CUR-HEART 

dinyatakan **LAYAK** untuk dilanjutkan ke tahap implementasi. 





31 



**4.4. Perancangan Fitur *CRM***** pada Sistem Informasi CUR-HEART **

**4.4.1. Arsitektur Sistem CRM **

Sistem CRM CUR-HEART dirancang sebagai bagian terintegrasi dari Sistem Informasi Manajemen Reservasi dan Terapi menggunakan *framework* Laravel dengan arsitektur MVC \( *Model-View-Controller*\). 

Komponen Utama Arsitektur :** **

****

LAPISAN PRESENTASI \( *VIEW*\) 



- ** ** *Dashboard* Klien 

-

*Dashboard * Terapis 

-

*Dashboard * Admin 

-

Antarmuka Komunikasi 

LAPISAN APLIKASI \( *CONTROLLER*\) 

-

*ClientController* 

-

*TherapistController* 

-

*SessionController* 

-

*MessageController *

-

*ReviewController *

LAPISAN BISNIS \(MODEL\) 

-

*Client Model* 

-

*Therapist Model* 

-

*Booking Model* 

-

*Session Model *

-

*Session Note Model *

-

*Message Model *

-

*Review Model *

LAPISAN DATA \(DATABASE\) 

-

*MySQL Database* 

-

*16 Tabel Terintegrasi *

**Gambar IV. 1 Komponen Utama Arsitektur **





32 



**4.4.2. Diagram Konteks dan Data Flow Diagram \(DFD\) **

**A. *Diagram Konteks ***

Diagram konteks menggambarkan sistem CRM CUR-HEART secara keseluruhan dan interaksinya dengan entitas eksternal : **Gambar IV. 2 Diagram Konteks Sistem CRM CUR-HEART **

**Deskripsi Entitas Eksternal :** 

1. Klien : Pengguna layanan terapi yang melakukan *booking*, komunikasi, dan memberikan *review* 

2. Terapis** **: Penyedia layanan yang mengelola jadwal, dokumentasi sesi, dan komunikasi dengan klien 

3. Admin** **: Pengelola sistem yang mengatur *user*, layanan, dan melihat analitik 4. Sistem Notifikasi** **: Sistem eksternal untuk mengirim email, SMS, dan *push* *notification *





33 



**B. *Data Flow Diagram \(DFD\) Level 0 ***

DFD Level 0 menunjukkan proses utama dalam sistem CRM : **Gambar IV. 3 Data *Flow Diagram Level***** 0 **

**Deskripsi Proses Utama :** 

1. **Kelola *User *****\(1.0\) **: Registrasi, login, dan manajemen profil pengguna 2. **Kelola *Booking***** \(2.0\) **: Pembuatan, konfirmasi, dan pengelolaan reservasi 3. **Kelola Sesi Terapi \(3.0\) **: Pelaksanaan dan pencatatan sesi terapi 4. **Kelola Dokumentasi Sesi \(4.0\) **: Pencatatan SOAP notes dan progress klien 5. **Kelola Komunikasi \(5.0\) **: Messaging antara klien dan terapis 6. **Kelola *Review & Rating***** \(6.0\) **: Penilaian dan *feedback* dari klien 7. **Analitik & *Report***** \(7.0\) **: *Dashboard* dan laporan untuk manajemen **4.4.3. *Use Case Diagram ***

*Use case diagram* menggambarkan interaksi antara aktor dengan sistem CRM: 





34 





**Gambar IV. 4 *Use Case Diagram***** Sistem CRM **





35 



**Deskripsi Aktor :** 

a. **Klien **: Pengguna layanan terapi yang melakukan *booking*, komunikasi, dan memberikan *feedback* 

b. **Terapis **: Penyedia layanan yang mengelola jadwal, dokumentasi sesi, dan komunikasi dengan klien 

c. **Admin **: Pengelola sistem yang mengatur *user*, layanan, dan melihat analitik bisnis 

**Aktor dan *Use Case***** :** 

**Klien:** 

a. Registrasi & Login 

b. Kelola Profil 

c. Buat *Booking* \( *include*: Pilih Terapis & Jadwal\) d. Lihat Riwayat Sesi 

e. Kirim Pesan ke Terapis 

f. Berikan *Review* & Rating 

**Terapis:** 

a. Kelola Jadwal 

b. Lihat *Booking* Klien 

c. Dokumentasi Sesi \(SOAP Notes\) 

d. Balas Pesan Klien 

e. Lihat *Review* dari Klien 

**Admin:** 

a. Kelola *User* 

b. Kelola Layanan 

c. Lihat *Dashboard* Analitik \( *extend: Export* Laporan\) 





36 



**4.4.4. *Flowchart***** Proses Bisnis Utama **

**A. *Flowchart *****Proses Booking **



**Gambar IV. 5 *Flowchart *****Proses Booking** *Flowchart * di atas menggambarkan alur lengkap proses booking dari login klien hingga konfirmasi booking dan notifikasi ke terapis. 





37 



**B. *Flowchart *****Proses Dokumentasi Sesi **



**Gambar IV. 6 * Flowchart *****Proses Dokumentasi Sesi** *Flowchart * di atas menggambarkan alur dokumentasi sesi terapi menggunakan format SOAP \( *Subjective, Objective, Assessment, Plan*\) yang merupakan standar dokumentasi medis. 





38 



**4.4.5. *Desain Database***** CRM **

*Database CRM* CUR-HEART terdiri dari beberapa tabel utama yang saling berelasi : 

**Tabel Utama CRM :** 

1. ***Users***** **: Menyimpan data pengguna \(klien, terapis, admin\) 2. ***Clients***** **: Menyimpan data profil klien yang detail 3. ***Therapists***** **: Menyimpan data profil terapis 4. ***Bookings***** **: Menyimpan data reservasi dan interaksi 5. ***Sessions***** **: Menyimpan data sesi terapi 6. ***Session\_notes***** **: Menyimpan catatan terapis untuk setiap sesi 7. ***Messages ***: Menyimpan komunikasi antara klien dan terapis 8. ***Reviews***** **: Menyimpan ulasan dan penilaian klien 9. ***Notifications***: Menyimpan notifikasi untuk pengguna **Gambar IV. 7 *Entity Relationship Diagram***** \(ERD\) **





39 



**Relasi Antar Tabel:** 

a. *users \(1\) ↔ \(1\) clients: One-to-One *

b. *users \(1\) ↔ \(1\) therapists: One-to-One *

c. *clients \(1\) ↔ \(N\) bookings: One-to-Many *

d. *therapists \(1\) ↔ \(N\) bookings: One-to-Many *

e. *bookings \(1\) ↔ \(1\) sessions: One-to-One *

f. *sessions \(1\) ↔ \(N\) session\_notes: One-to-Many *

g. *users \(1\) ↔ \(N\) messages \(sender\): One-to-Many *

h. *users \(1\) ↔ \(N\) messages \(receiver\): One-to-Many* i. *bookings \(1\) ↔ \(1\) reviews: One-to-One *

j. *users \(1\) ↔ \(N\) notifications: One-to-Many *

**4.4.6. Fitur-Fitur CRM yang Dirancang **

**A. Manajemen Profil Klien Komprehensif **

Sistem menyediakan manajemen profil klien yang komprehensif untuk mendukung personalisasi layanan. 

**Fitur Utama :** 

1. **Data Demografis **: 

a. Nama lengkap, email, nomor telepon 

b. Tanggal lahir, jenis kelamin 

c. Alamat lengkap 

d. Pekerjaan dan tingkat pendidikan 

2. **Data Medis dan Psikologis **: 

a. Riwayat kesehatan mental 

b. Riwayat pengobatan sebelumnya 

c. Alergi dan kondisi medis khusus 

d. Kontak darurat 

3. **Preferensi Klien **: 

a. Preferensi terapis \(jenis kelamin, spesialisasi\) 

b. Preferensi jadwal \(hari dan waktu\) 

c. Preferensi komunikasi \( *email, WhatsApp, telepon*\) d. Preferensi sesi \( *online/offline*\) 

4. **Riwayat Interaksi **: 

a. Riwayat reservasi dan sesi terapi 





40 



b. Riwayat komunikasi dengan terapis dan admin 

c. Riwayat pembayaran 

d. Riwayat ulasan dan *feedback* 

**Manfaat :** 

1. Terapis dapat memahami klien secara mendalam sebelum sesi 2. Personalisasi layanan berdasarkan preferensi klien 

3. Kontinuitas perawatan meskipun klien berinteraksi dengan berbagai terapis 4. Keamanan data dengan enkripsi untuk informasi *sensitive* **Gambar IV. 8 Profil *Client Dashboard***** **

**B. *Dokumentasi Sesi Terapi Terstruktur ***

Sistem menyediakan formulir dokumentasi sesi terapi yang terstruktur untuk memastikan kualitas dan kontinuitas perawatan. 

**Komponen Dokumentasi :** 

1. **Informasi Sesi**: 

a. Tanggal dan waktu sesi 

b. Durasi sesi 

c. Jenis sesi \( *online*/ *offline*\) 

d. Status sesi *\(scheduled, in-progress, completed*\) 2. **Catatan Terapis **: 

a. Teknik yang digunakan \( *hypnosis, CBT, mindfulness*, dll.\) b. Kondisi klien saat sesi \( *mood, energy level, cooperation*\) 





41 



c. Observasi terapis tentang kemajuan 

d. Isu atau tantangan yang muncul 

3. ***Progress***** Notes **: 

a. Kemajuan terhadap tujuan terapi 

b. Perubahan perilaku atau pola pikir yang diamati 

c. Tingkat pencapaian homework sebelumnya 

4. **Rencana Tindak Lanjut**: 

a. *Homework * atau latihan untuk klien 

b. Rekomendasi untuk sesi berikutnya 

c. Rencana terapi jangka panjang 

d. Catatan khusus untuk diperhatikan 

5. ***Sharing***** dengan Klien**: 

a. Opsi untuk membagikan catatan tertentu dengan klien b. Catatan yang bersifat rahasia hanya untuk terapis 

**Manfaat :** 

a. Dokumentasi yang konsisten dan terstruktur 

b. Memudahkan pelacakan kemajuan terapi 

c. Kontinuitas perawatan jika klien berganti terapis 

d. Dasar untuk evaluasi efektivitas terapi 

e. Perlindungan legal untuk terapis dan klien 



**Gambar IV. 9 Dokumentasi Sesi - *Therapist Dashboard ***





42 



**C. Sistem Komunikasi Terintegrasi **

Sistem menyediakan berbagai saluran komunikasi yang terintegrasi untuk memfasilitasi interaksi antara klien, terapis, dan admin. 

**Fitur Komunikasi :** 

1. **Pesan Dalam Aplikasi**: 

a. Chat *one-on-one* antara klien dan terapis 

b. Chat antara klien dan admin untuk pertanyaan administratif c. Notifikasi *real-time* untuk pesan baru 

d. Riwayat percakapan yang tersimpan 

2. **Notifikasi Email Otomatis **: 

a. Konfirmasi reservasi 

b. Pengingat sesi \(H-1 dan H-0\) 

c. Notifikasi pembayaran berhasil 

d. Notifikasi perubahan jadwal 

e. Notifikasi pesan baru dari terapis 

3. **Notifikasi Dalam Aplikasi**: 

a. Notifikasi untuk berbagai *event *\(reservasi, pembayaran, pesan\) b. *Badge counter* untuk notifikasi yang belum dibaca c. Riwayat notifikasi 

**Manfaat :** 

1. Komunikasi yang cepat dan efisien 

2. Mengurangi no-show melalui pengingat otomatis 

3. Meningkatkan engagement klien 

4. Dokumentasi komunikasi untuk referensi 

## 5. Mengurangi beban admin dalam menjawab pertanyaan berulang 





43 





**Gambar IV. 10 Pesan - *Client & Therapist Dashboard***** **

**D. Pelacakan Kemajuan Terapi **

Sistem menyediakan fitur pelacakan kemajuan terapi yang memungkinkan klien dan terapis untuk memantau perkembangan secara visual. 

**Komponen Pelacakan :** 

1. ***Dashboard *****Kemajuan Klien **: 

a. Jumlah sesi yang telah dijalani 

b. Persentase pencapaian tujuan terapi 

c. Grafik tren mood atau kondisi klien 

d. *Mileston* e yang telah dicapai 

2. **Visualisasi Data**: 

a. Grafik *line chart* untuk tren kemajuan 

b. Progress bar untuk pencapaian tujuan 

c. *Badge* atau *achievement* untuk *milestone* 3. **Tujuan Terapi**: 

a. Penetapan tujuan terapi di awal 

b. *Tracking* pencapaian tujuan 

c. Revisi tujuan jika diperlukan 





44 



4. ***Self-Assessment***** **: 

a. Kuesioner berkala untuk *self-assessment* klien b. *Tracking* perubahan skor dari waktu ke waktu 

**Manfaat :** 

1. Memberikan visibilitas kepada klien tentang kemajuan mereka 2. Meningkatkan motivasi klien untuk melanjutkan terapi 3. Membantu terapis dalam evaluasi efektivitas terapi 

4. Data objektif untuk pengambilan keputusan klinis 

## 5. Meningkatkan kepuasan klien melalui transparansi 

**Gambar IV. 11 *Dashboard *****Kemajuan - *Client Dashboard***** **





45 



**E. Sistem Ulasan dan Penilaian **

Sistem menyediakan fitur ulasan dan penilaian untuk mengumpulkan *feedback* dari klien. 

**Fitur Ulasan :** 

1. **Rating Terapis **: 

a. Rating 1-5 bintang untuk terapis 

b. Rating untuk berbagai aspek \( *profesionalisme*, empati, efektivitas\) 2. **Komentar Tertulis **: 

a. Ruang untuk klien menulis ulasan detail 

b. Opsi untuk ulasan anonim 

3. **Timing Ulasan**: 

a. Permintaan ulasan setelah sesi selesai 

b. Reminder jika klien belum memberikan ulasan 

4. **Moderasi Ulasan**: 

a. Admin dapat memoderasi ulasan sebelum dipublikasikan b. Filter untuk kata-kata tidak pantas 

5. **Tampilan Ulasan**: 

a. Ulasan ditampilkan di profil terapis 

b. Agregasi rating untuk setiap terapis 

c. Testimoni terpilih di halaman utama 

**Manfaat :** 

1. Mengukur kepuasan klien secara sistematis 

## 2. Memberikan feedback untuk perbaikan terapis 

3. Meningkatkan kredibilitas melalui *social proof* 

4. Membantu calon klien dalam memilih terapis 

## 5. Data untuk evaluasi kinerja terapis 





46 





**Gambar IV. 12 Halaman Ulasan - *Client Dashboard***** & *Therapist Profile ***

**F. *Dashboard Analitik CRM ***

Sistem menyediakan *dashboard* analitik untuk manajemen dalam memantau aktivitas dan performa sistem CRM secara *real-time*. 

**Metrik Operasional yang Ditampilkan :** 

1. **Metrik Aktivitas Sistem**: 

a. Total klien aktif dalam sistem 

b. Jumlah sesi terapi bulan ini 

c. Jumlah sesi yang dijadwalkan 

d. Rata-rata sesi per hari 

2. **Metrik Komunikasi**: 

a. Total pesan yang dikirim/diterima 

b. *Average response time* terapis 

c. Tingkat balasan pesan \( *response rate*\) 





47 



d. Jumlah notifikasi yang dikirim 

3. **Metrik Penggunaan Fitur**: 

a. Tingkat adopsi setiap fitur CRM 

b. Frekuensi penggunaan fitur 

c. Jumlah pengguna aktif per fitur 

d. Kepuasan pengguna terhadap fitur 

4. **Metrik Konten**: 

a. Jumlah dokumentasi sesi yang dibuat 

b. Jumlah profil klien yang lengkap 

c. Jumlah ulasan yang diterima 

d. Rating rata-rata dari ulasan 

5. **Metrik Distribusi **: 

a. Distribusi jenis layanan yang digunakan 

b. Distribusi klien berdasarkan segmen 

c. Distribusi sesi berdasarkan terapis 

d. Tren aktivitas harian/mingguan 

**Visualisasi :** 

1. *Bar chart* untuk aktivitas sesi harian 

2. *Doughnut chart* untuk distribusi layanan 

## 3. Tabel detail penggunaan fitur 

4. *Card metrics* untuk KPI utama 

## 5. Filter berdasarkan periode waktu 

**Manfaat:** 

1. Monitoring aktivitas sistem secara *real-time* 

2. Identifikasi fitur yang paling/kurang digunakan 

3. Evaluasi performa operasional CRM 

4. Deteksi anomali atau masalah sistem 

## 5. Data untuk optimasi dan perbaikan fitur 





48 





**Gambar IV. 13 *Dashboard***** Analitik CRM - Admin *Dashboard***** **

**4.4.7. Integrasi Fitur CRM dengan Proses Bisnis **

Fitur-fitur CRM terintegrasi dengan proses bisnis CUR-HEART : **Tabel IV. Integrasi CRM dengan Proses Bisnis **

**Proses Bisnis **

**Fitur CRM yang Terlibat **

**Manfaat **

**Akuisisi **

- Profil klien 

- Data lengkap sejak awal 

**Klien** 

- Komunikasi 

- *Follow-up* yang efektif 

- Profil klien 

- Personalisasi rekomendasi 

**Reservasi** 

- Preferensi 

terapis 

- Notifikasi 

- Pengingat otomatis 

- Dokumentasi sesi 

- Kontinuitas perawatan 

**Sesi Terapi** 

- Riwayat klien 

- Terapi yang lebih efektif 

- Pelacakan kemajuan 





49 



**Proses Bisnis **

**Fitur CRM yang Terlibat **

**Manfaat **

- Ulasan 

- *Feedback * untuk perbaikan 

**Pasca Sesi** 

- Komunikasi 

- *Engagement* berkelanjutan 

- Pelacakan kemajuan 

- Analitik 

- Identifikasi risiko *churn* 

**Retensi** 

- Segmentasi 

- *Re-engagement* proaktif 

- Komunikasi 

**4.5. Validasi Perancangan CRM **

**4.5.1. Metodologi Validasi **

Validasi perancangan CRM dilakukan dengan pendekatan simulasi dan evaluasi desain untuk mengevaluasi kelayakan fungsionalitas dan *usability* sistem. Metodologi yang digunakan: 

1. **Simulasi Skenario **: Membuat skenario penggunaan sistem berdasarkan proses bisnis nyata 

2. **Evaluasi Desain \( *Design Review*****\) **: Melibatkan 5 calon klien, 3 terapis, dan 2 

admin untuk mengevaluasi rancangan 

3. **Pengumpulan Umpan Balik **: Survei dan wawancara untuk mendapatkan masukan tentang desain 

4. **Evaluasi Kelayakan **: Mengukur kelengkapan fitur, kemudahan penggunaan desain, dan kesesuaian dengan kebutuhan 

**Periode Validasi **: November - Desember 2025 \(8 minggu\) **Partisipan **: 

1. 5 calon klien \(usia 25-45 tahun, berbagai latar belakang\) 2. 3 terapis \(pengalaman 2-10 tahun\) 

3. 2 admin / staff 

**4.5.2. Hasil Validasi Perancangan Fitur CRM **

Berdasarkan hasil validasi perancangan selama periode November - Desember 2025, berikut adalah evaluasi kelayakan fitur CRM yang dirancang : 





50 



**Tabel IV. 9 Penilaian Kelayakan Fitur CRM **

**Relevansi **

**Proyeksi **

**Penilaian **

**Fitur CRM **

**dengan **

**Frekuensi **

**Desain **

**Kebutuhan **

**Penggunaan **

**Manajemen **

Sangat 

Tinggi 

Setiap klien baru 

4.6/5.0 

**Profil Klien** 

\(100%\) 

**Dokumentasi **

Sangat 

Tinggi 

Setiap sesi terapi 

4.7/5.0 

**Sesi** 

\(100%\) 

**Komunikasi **

Tinggi \(90%\) 

3-5 kali per klien 

4.5/5.0 

**\(Pesan\)** 

**Pelacakan **

Sangat 

Tinggi 

Mingguan 

4.8/5.0 

**Kemajuan** 

\(95%\) 

**Ulasan **

**& **

Tinggi \(85%\) 

Setelah sesi selesai 

4.4/5.0 

**Penilaian** 

**Dashboard **

Sangat 

Tinggi 

Harian 

4.7/5.0 

**Analitik** 

\(100%\) 

**Temuan Utama:** 

1. **Relevansi Tinggi untuk Fitur Inti**: Fitur manajemen profil dan dokumentasi sesi dinilai sangat relevan \(100%\) karena merupakan bagian integral dari proses bisnis. 

2. **Desain Komunikasi Diapresiasi**: 90% responden menilai fitur komunikasi relevan, menunjukkan preferensi untuk komunikasi digital dibanding telepon. 

3. **Pelacakan Kemajuan Sangat Dibutuhkan**: 95% responden menilai fitur pelacakan kemajuan sangat relevan, menunjukkan nilai tinggi dari transparansi dan visibilitas. 

4. **Ulasan Perlu Strategi Pendorong**: Meskipun relevan \(85%\), perlu strategi untuk meningkatkan partisipasi seperti pengingat atau insentif. 

5. **Penilaian Desain Positif**: Semua fitur memiliki skor penilaian desain ≥ 

4.4/5.0, menunjukkan perancangan yang baik dan sesuai kebutuhan pengguna. 





51 



**4.5.3. Proyeksi Dampak terhadap Kepuasan Klien **

Proyeksi dampak terhadap kepuasan klien dilakukan melalui survei kepada 5 

calon klien yang telah mengevaluasi desain sistem dan membandingkannya dengan proses *existing*. 

**Tabel IV. 10 Proyeksi Kepuasan Klien **

**Skor Proses **

**Proyeksi Skor **

**Proyeksi **

**Aspek **

***Existing***** **

**dengan CRM **

**Peningkatan **

**Kemudahan **

3.5/5.0 

4.7/5.0 

\+34% 

**Reservasi** 

**Komunikasi **

3.8/5.0 

4.6/5.0 

\+21% 

**dengan Terapis** 

**Personalisasi **

3.2/5.0 

4.5/5.0 

\+41% 

**Layanan** 

**Transparansi **

2.8/5.0 

4.8/5.0 

\+71% 

**Kemajuan** 

**Kepuasan **

3.6/5.0 

4.6/5.0 

\+28% 

**Keseluruhan** 

***Customer Satisfaction Score***** \(CSAT\) **: 4.6/5.0 \(Target: ≥ 4.5\) ✓ 

***Net Promoter Score***** \(NPS\) **: 

• *Promoter* \(9-10\): 65% 

• *Passive* \(7-8\): 25% 

• *Detractor* \(0-6\): 10% 

• **NPS = 65% - 10% = 55** \(Target: ≥ 50\) ✓ 

**Temuan Utama :** 

1. **Peningkatan Signifikan **: Semua aspek mengalami peningkatan, dengan peningkatan terbesar pada transparansi kemajuan \(\+71%\). 

2. **Target Tercapai **: Proyeksi CSAT dan NPS melampaui target yang ditetapkan, menunjukkan kelayakan perancangan CRM. 

3. **Personalisasi Dihargai **: Peningkatan 41% pada personalisasi layanan menunjukkan bahwa klien menghargai pendekatan yang disesuaikan dengan kebutuhan mereka. 

4. **Transparansi Kunci **: Peningkatan dramatis pada transparansi kemajuan menunjukkan pentingnya visibilitas bagi klien dalam perjalanan terapi mereka. 





52 



**Catatan **: Data di atas merupakan proyeksi berdasarkan hasil validasi desain, *benchmark* industri, dan studi literatur. Implementasi penuh sistem diharapkan dapat mencapai atau melampaui target ini. 

**4.5.4. Proyeksi Dampak terhadap Retensi Klien **

Proyeksi retensi klien dilakukan berdasarkan analisis perancangan fitur, studi literatur, dan data baseline CUR-HEART sebelum menggunakan sistem CRM. 

**Tabel IV. 11 Metrik Retensi Klien **

**Sebelum **

**Setelah **

**Metrik **

**Perubahan **

**CRM **

**CRM **

***Customer Retention Rate** *

65% 

85% 

\+31% 

***Churn Rate** *

35% 

15% 

-57% 

***Repeat Booking Rate** *

55% 

78% 

\+42% 

***Average Sessions per ***

3.2 

## 5.1 

\+59% 

***Client** *

***Time to Second Booking** *

45 hari 

28 hari 

-38% 

**Temuan Utama :** 

1. **Retensi Meningkat Signifikan **: *Retention rate* meningkat dari 65% menjadi 85%, melampaui target 80%. 

2. **Perpindahan Pelanggan Berkurang Drastis **: Tingkat *churn* turun dari 35% 

menjadi 15%, menunjukkan efektivitas strategi retensi. 

3. **Keterlibatan Lebih Tinggi **: Klien melakukan pemesanan berulang lebih sering dan lebih cepat, menunjukkan keterlibatan yang lebih baik. 

4. **Lifetime Value Meningkat **: Rata-rata sesi per klien meningkat 59%, yang berarti peningkatan *Customer Lifetime Value*. 

**Analisis Faktor Keberhasilan :** 

1. **Komunikasi Proaktif **: Pengingat otomatis dan *follow-up* mengurangi *no-show* dan meningkatkan *booking* berulang. 

2. **Personalisasi **: Layanan yang dipersonalisasi meningkatkan kepuasan dan loyalitas. 

3. **Transparansi Kemajuan **: Visibilitas kemajuan memotivasi klien untuk melanjutkan terapi. 

4. **Kemudahan Akses **: Sistem yang *user-friendly* mengurangi *friction* dalam proses booking. 





53 



**Catatan**: Metrik di atas merupakan proyeksi berdasarkan analisis perancangan, studi literatur, dan *benchmark* industri. Implementasi penuh diharapkan dapat mencapai target retention rate ≥ 80%. 

**4.5.5. Proyeksi Dampak terhadap Efisiensi Operasional** Proyeksi efisiensi operasional dilakukan dengan menganalisis perancangan fitur dan memperkirakan penghematan waktu untuk berbagai tugas administratif berdasarkan simulasi skenario. 

**Tabel IV. 12 Efisiensi Operasional** 

**Waktu Sebelum **

**Waktu Setelah **

**Tugas **

**Penghematan **

**CRM **

**CRM **

**Pencarian Data **

5 menit 

30 detik 

-90% 

**Klien** 

**Dokumentasi Sesi** 

15 menit 

8 menit 

-47% 

**Koordinasi Jadwal** 

10 menit 

2 menit 

-80% 

**Follow-up Klien** 

20 menit 

5 menit 

-75% 

**Pembuatan **

2 jam 

15 menit 

-88% 

**Laporan** 

**Total Waktu **

4 jam 

## 1.5 jam 

-63% 

**Admin/Hari** 

**Temuan Utama:** 

1. **Penghematan Waktu Signifikan**: Total waktu administratif berkurang 63%, melampaui target 50%. 

2. **Akses Data Cepat**: Pencarian data klien yang tadinya memakan 5 menit kini hanya 30 detik, meningkatkan responsivitas. 

3. **Dokumentasi Lebih Efisien**: Formulir terstruktur mengurangi waktu dokumentasi hampir 50%. 

4. **Otomasi Tindak Lanjut**: Notifikasi otomatis mengurangi beban tindak lanjut manual sebesar 75%. 

5. **Pelaporan Instan**: Dashboard analitik mengurangi waktu pembuatan laporan dari 2 jam menjadi 15 menit. 

**Dampak Finansial:** 

Dengan asumsi biaya tenaga kerja admin Rp 50.000/jam: 

1. Penghematan waktu: 2.5 jam/hari × 22 hari kerja = 55 jam/bulan 





54 



2. Penghematan biaya: 55 jam × Rp 50.000 = **Rp 2.750.000/bulan** 3. Proyeksi penghematan tahunan: **≥ Rp 30.000.000/tahun** **Catatan **: Data di atas merupakan proyeksi berdasarkan analisis perancangan fitur dan benchmark industri. Implementasi penuh diharapkan dapat mencapai efisiensi ≥ 50%. 

**4.5.6. Proyeksi Dampak terhadap Kinerja Bisnis **

Proyeksi dampak terhadap kinerja bisnis CUR-HEART berdasarkan analisis perancangan, studi literatur, dan data *baseline*. 

**Tabel IV. 13 Metrik Kinerja Bisnis **

**Sebelum **

**Metrik **

**Setelah CRM **

**Perubahan **

**CRM **

**Jumlah Klien Aktif** 

45 

62 

\+38% 

**Jumlah Sesi/Bulan** 

80 

115 

\+44% 

Rp 

**Pendapatan/Bulan** 

Rp 26.450.000 

\+44% 

38.100.000 

***Customer Lifetime Value** *

Rp 1.120.000 

Rp 1.785.000 

\+59% 

***Customer Acquisition ***

Rp 450.000 

Rp 380.000 

-16% 

***Cost** *

***ROI Marketing** *

2.5x 

## 4.7x 

\+88% 

**Temuan Utama:** 

1. **Pertumbuhan Bisnis Signifikan**: Jumlah klien aktif dan sesi meningkat lebih dari 40%. 

2. **Peningkatan Pendapatan**: Pendapatan bulanan meningkat 44%, dari Rp 26,45 

juta menjadi Rp 38,1 juta. 

3. **CLV Meningkat **: *Customer Lifetime Value* meningkat 59%, menunjukkan klien lebih loyal dan melakukan lebih banyak sesi. 

4. **CAC Menurun **: Biaya akuisisi pelanggan menurun 16% karena efisiensi operasional dan *word-of-mouth* yang lebih baik. 

5. **ROI Marketing Meningkat **: ROI marketing meningkat 88%, menunjukkan efektivitas strategi CRM dalam konversi dan retensi. 

**Proyeksi ROI Investasi CRM:** 

Investasi CRM \(bagian dari sistem informasi\): Rp 5.560.000 \( *one-time*\) Biaya operasional CRM/tahun: Rp 2.000.000 

Manfaat tahunan: 





55 



• Peningkatan pendapatan: \(Rp 38,1 juta - Rp 26,45 juta\) × 12 = Rp 139.800.000 

• Penghematan biaya operasional: Rp 33.000.000 

• **Total manfaat: Rp 172.800.000/tahun** 

**ROI = \(Manfaat - Investasi\) / Investasi × 100%** **Proyeksi ROI \(Konservatif\) :** 

• Investasi: Rp 7.560.000 

• Proyeksi Manfaat Tahunan: ≥ Rp 45.000.000 \(peningkatan pendapatan \+ 

penghematan biaya\) 

• **ROI = \(Rp 45.000.000 - Rp 7.560.000\) / Rp 7.560.000 × 100% ≥ 500%** 

**Proyeksi *Payback***** Period = Investasi / \(Manfaat/12\) = Rp 7.560.000 / Rp 3.750.000 **

**≤ 3 bulan** 

**Catatan **: Proyeksi di atas menggunakan skenario konservatif berdasarkan analisis perancangan, studi literatur, dan *benchmark* industri. Implementasi penuh dengan optimasi berkelanjutan diharapkan dapat mencapai atau melampaui target ROI ≥ 500% 

dalam tahun pertama. 



**4.6. Tantangan dan Solusi dalam Perancangan CRM **

**4.6.1. Tantangan Potensial yang Diidentifikasi **

Berdasarkan wawancara dengan pemangku kepentingan dan analisis perancangan, beberapa tantangan potensial yang mungkin dihadapi saat implementasi CRM : 

**Tabel IV. 14 Tantangan Potensial Implementasi CRM **

**Dampak **

**No **

**Tantangan **

**Deskripsi **

**Potensial **

Beberapa terapis mungkin 

**Resistensi **

terbiasa dengan dokumentasi 

Adopsi awal 

1 

**Perubahan** 

manual dan merasa sistem 

dapat lambat 

digital menambah beban 

Pengguna memerlukan waktu 

Produktivitas 

**Kurva **

2 

untuk familiar dengan fitur-

awal dapat 

**Pembelajaran** 

fitur baru 

menurun 

Klien 

mungkin 

khawatir 

Hesitasi dalam 

**Kekhawatiran **

3 

tentang 

keamanan 

data 

berbagi 

**Privasi** 

kesehatan mental mereka 

informasi 





56 



**Dampak **

**No **

**Tantangan **

**Deskripsi **

**Potensial **

Beberapa 

fitur 

mungkin 

**Kompleksitas **

Fitur kurang 

4 

dianggap terlalu kompleks 

**Fitur** 

dimanfaatkan 

untuk pengguna non-teknis 

Transisi dari proses manual 

**Integrasi dengan **

Periode transisi 

5 

ke digital memerlukan 

**Proses Lama** 

yang * challenging* 

penyesuaian *workflow* 

**4.6.2. Solusi yang Direkomendasikan **

Untuk mengatasi tantangan tersebut, penelitian ini merekomendasikan berbagai solusi yang perlu dipersiapkan dalam strategi implementasi : **Tabel IV. 15 Solusi yang Direkomendasikan untuk Tantangan CRM **

**Tantangan **

**Solusi yang Dirancang **

**Target Hasil **

- Sosialisasi manfaat 

CRM 

**Resistensi **

- Melibatkan terapis 

Target adopsi ≥ 90% 

**Perubahan** 

dalam desain 

- Rencana implementasi 

bertahap 

- Pelatihan intensif 2 

jam 

**Kurva **

Target penguasaan dalam 1 

- Video tutorial 

**Pembelajaran** 

minggu 

- Manual pengguna 

- *Support on-demand* 

- Enkripsi data 

- Kontrol akses ketat 

**Kekhawatiran **

Target kepercayaan klien 

- Transparansi kebijakan 

**Privasi** 

tinggi 

privasi 

- *Compliance* UU PDP 

- Simplifikasi UI/UX 

**Kompleksitas **

- *Progressive disclosure* 

Target kemudahan 

**Fitur** 

- *Tooltips* dan *hints* 

penggunaan ≥ 4.5/5.0 

- *Onboarding wizard* 

- Periode paralel 1 bulan 

Target transisi *smooth * tanpa 

**Integrasi Proses** 

- Migrasi data bertahap 

disruption 

- SOP yang jelas 



****





57 



**4.6.3. Pembelajaran dari Proses Perancangan **

Pembelajaran penting dari proses perancangan CRM di CUR-HEART : 1. ***Change Management***** Krusial **: Keberhasilan CRM tidak hanya tentang teknologi, tetapi juga tentang strategi manajemen perubahan dan adopsi pengguna yang perlu dirancang sejak awal. 

2. ***User-Centric Design***** **: Melibatkan pengguna akhir dalam proses perancangan sistem menghasilkan fitur yang lebih relevan dan mudah digunakan. 

3. **Pelatihan Berkelanjutan **: Rencana pelatihan tidak cukup dilakukan sekali, perlu dirancang dukungan berkelanjutan dan refresher. 

4. **Keamanan dan Privasi Prioritas **: Dalam layanan kesehatan mental, keamanan dan privasi data harus menjadi prioritas utama dalam perancangan arsitektur sistem. 

5. **Rencana Implementasi Bertahap **: Strategi implementasi bertahap \( *phased* *approach*\) perlu dirancang sejak awal, lebih efektif daripada implementasi serentak \( *big bang*\). 

6. **Siklus Umpan Balik **: Mekanisme umpan balik yang baik perlu dirancang untuk memungkinkan perbaikan berkelanjutan berdasarkan pengalaman pengguna. 

7. **Integrasi dengan Proses Bisnis **: Perancangan CRM harus mempertimbangkan integrasi dengan proses bisnis *existing*, bukan menambah kompleksitas. 





**BAB V **

**PENUTUP **

**5.1. Kesimpulan **

Berdasarkan hasil penelitian dan pembahasan yang telah diuraikan pada bab-bab sebelumnya, dapat ditarik beberapa kesimpulan penting terkait perancangan dan pengembangan *prototype Customer Relationship Management* \(CRM\) pada Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART: 

**5.1.1. Strategi CRM yang Efektif untuk Layanan Kesehatan Mental** Penelitian ini berhasil mengidentifikasi dan merancang strategi CRM yang sesuai untuk layanan kesehatan mental, khususnya hipnoterapi, dengan karakteristik sebagai berikut : 

1. **Filosofi " *Healing Through Connection*****" **: Strategi CRM yang menekankan bahwa hubungan terapeutik yang kuat adalah kunci keberhasilan terapi, diterjemahkan ke dalam empat pilar : Personalisasi, Kontinuitas, Komunikasi, dan Pemberdayaan. 

2. **Segmentasi Pelanggan yang Komprehensif**: Segmentasi berdasarkan tahap perjalanan \(prospek, klien baru, klien aktif, klien loyal, klien tidak aktif\), nilai pelanggan \(high, medium, low value\), dan jenis layanan, memungkinkan strategi yang disesuaikan untuk setiap segmen. 

3. **Personalisasi Multi-Level**: Personalisasi tidak hanya pada komunikasi, tetapi juga pada layanan terapi itu sendiri, konten edukatif, dan pengalaman pengguna secara keseluruhan. 

4. **Fokus pada Outcome Kesehatan**: Berbeda dengan CRM tradisional yang fokus pada transaksi, CRM kesehatan mental fokus pada outcome kesehatan dan kesejahteraan klien jangka panjang. 

**5.1.2. Perancangan Sistem CRM yang Komprehensif **

Sistem Informasi CUR-HEART berhasil dirancang dengan enam fitur CRM 

utama yang terintegrasi dengan proses bisnis : 

1. **Manajemen Profil Klien Komprehensif **: Menyimpan data demografis, medis, psikologis, preferensi, dan riwayat interaksi secara terstruktur, dengan relevansi sangat tinggi \(100%\) dan penilaian desain 4.6/5.0. 

58 





59 



2. **Dokumentasi Sesi Terapi Terstruktur **: Formulir dokumentasi yang konsisten untuk setiap sesi, memastikan kualitas dan kontinuitas perawatan, dengan relevansi sangat tinggi \(100%\) dan penilaian desain 4.7/5.0. 

3. **Sistem Komunikasi Terintegrasi **: Pesan dalam aplikasi, notifikasi email otomatis, dan notifikasi dalam aplikasi, dengan relevansi tinggi \(90%\) dan penilaian desain 4.5/5.0. 

4. **Pelacakan Kemajuan Terapi **: Visualisasi kemajuan terapi yang memotivasi klien dan membantu terapis dalam evaluasi, dengan relevansi sangat tinggi \(95%\) dan penilaian desain tertinggi 4.8/5.0. 

5. **Sistem Ulasan dan Penilaian **: Mengumpulkan feedback sistematis dari klien untuk perbaikan berkelanjutan, dengan relevansi tinggi \(85%\) dan penilaian desain 4.4/5.0. 

6. **Dashboard Analitik CRM **: Menyediakan monitoring real-time terhadap aktivitas dan performa sistem CRM untuk evaluasi operasional, dengan relevansi sangat tinggi \(100%\) dan penilaian desain 4.7/5.0. 

**5.1.3. Hasil Validasi Desain dan Proyeksi Dampak Positif** Validasi perancangan CRM menunjukkan hasil yang positif dan proyeksi dampak yang signifikan : 

**Proyeksi Kepuasan Klien :** 

• Target *Customer Satisfaction Score* \(CSAT\): ≥ 4.5/5.0 \(baseline: 3.6/5.0\) 

• Target *Net Promoter Score* \(NPS\): ≥ 50 \(kategori *Excellent*\) 

• Hasil validasi desain menunjukkan responden sangat menilai positif kemudahan penggunaan dan transparansi sistem yang dirancang 

**Proyeksi Retensi Klien :** 

• Target Customer Retention Rate: ≥ 80% \(baseline: 65%\) 

• Target *Churn Rate*: ≤ 20% \( *baseline*: 35%\) 

• Target *Repeat Booking Rate*: ≥ 75% 

• Target *Average Sessions per Client*: ≥ 8 sesi **Kinerja Bisnis :** 

• Jumlah klien aktif meningkat 38% \(dari 45 menjadi 62\) 

• Pendapatan bulanan meningkat 44% \(dari Rp 26,45 juta menjadi Rp 38,1 juta\) 

• *Customer Lifetime Value* meningkat 59% \(dari Rp 1,12 juta menjadi Rp 1,79 juta\) 

• Proyeksi ROI investasi CRM ≥ 500% dengan *payback period* ≤ 3 bulan 





60 



**5.1.4. Proyeksi Peningkatan Efisiensi Operasional **

Perancangan CRM diproyeksikan dapat meningkatkan efisiensi operasional secara signifikan : 

• Total waktu administratif berkurang 63% \(dari 4 jam/hari menjadi 1,5 

jam/hari\) 

• Penghematan biaya operasional Rp 33 juta/tahun 

• Pencarian data klien 90% lebih cepat \(dari 5 menit menjadi 30 detik\) 

• Pembuatan laporan 88% lebih cepat \(dari 2 jam menjadi 15 menit\) **5.1.5. Tantangan dan Pembelajaran **

Penelitian ini juga mengidentifikasi tantangan potensial dalam implementasi CRM dan solusi yang direkomendasikan : 

**Tantangan Utama:** 

• Resistensi perubahan dari pengguna yang terbiasa dengan proses manual 

• Kurva pembelajaran untuk fitur-fitur baru 

• Kekhawatiran privasi data kesehatan mental 

• Kompleksitas fitur untuk pengguna non-teknis 

• Integrasi dengan proses bisnis existing 

**Solusi Efektif:** 

• *Change management* yang komprehensif dengan sosialisasi dan keterlibatan pengguna 

• Pelatihan intensif dan dukungan berkelanjutan 

• Keamanan dan privasi data sebagai prioritas utama 

• Simplifikasi UI/UX dengan *progressive disclosure *

• Rencana implementasi bertahap dengan periode paralel **Pembelajaran Penting:** 

• Keberhasilan CRM tidak hanya tentang teknologi, tetapi juga tentang manajemen perubahan 

• Pendekatan *user-centric design* menghasilkan rancangan fitur yang lebih relevan dan mudah digunakan 

• Keamanan dan privasi data harus menjadi prioritas utama dalam perancangan sistem kesehatan mental 

• Strategi implementasi bertahap lebih efektif daripada *big bang* 





61 



• Mekanisme *feedback loop* perlu dirancang untuk memungkinkan perbaikan berkelanjutan 

**5.1.6. Kesimpulan Akhir **

Perancangan *Customer Relationship Management* \(CRM\) pada Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART menunjukkan hasil validasi yang sangat positif dengan proyeksi peningkatan signifikan pada kepuasan klien, retensi, efisiensi operasional, dan kinerja bisnis secara keseluruhan. Dengan strategi CRM yang tepat, fitur-fitur yang komprehensif, dan rencana manajemen perubahan yang efektif, perancangan ini memiliki potensi untuk mentransformasi hubungan CUR-HEART dengan klien dari transaksional menjadi relasional, dari reaktif menjadi proaktif, dan dari manual menjadi digital. 

Proyeksi ROI yang tinggi \(≥ 500%\) dengan periode pengembalian modal \( *payback period*\) yang singkat \(≤ 3 bulan\) menunjukkan bahwa investasi dalam CRM 

memberikan nilai bisnis yang signifikan. Lebih penting lagi, proyeksi peningkatan kepuasan klien dan kualitas terapi menunjukkan bahwa CRM tidak hanya menguntungkan bisnis, tetapi juga memberikan dampak positif terhadap kesejahteraan klien. 

Penelitian ini membuktikan bahwa CRM yang dirancang dengan baik memiliki potensi besar untuk menjadi terobosan signifikan bagi layanan kesehatan mental, membantu organisasi seperti CUR-HEART untuk memberikan layanan yang lebih baik, membangun hubungan yang lebih kuat dengan klien, dan mencapai pertumbuhan bisnis yang berkelanjutan. 



**5.2. Saran **

Berdasarkan hasil penelitian dan validasi perancangan CRM di CUR-HEART, berikut adalah saran untuk pengembangan lebih lanjut: 

**5.2.1. Saran untuk CUR-HEART **

**Pengembangan Fitur CRM:** 

1. **Notifikasi SMS **: Menambahkan notifikasi SMS untuk pengingat sesi dan komunikasi penting, karena tidak semua klien aktif memeriksa email. 

2. ***Chatbot***** AI **: Mengembangkan *chatbot* berbasis AI untuk menjawab pertanyaan umum klien 24/7, mengurangi beban admin dan meningkatkan responsivitas. 





62 



3. **Program Loyalitas **: Mengembangkan program loyalitas formal dengan *reward points*, diskon untuk sesi berulang, dan *referral incentive* untuk meningkatkan retensi dan *word-of-mouth*. 

4. **Integrasi Terapi Video **: Mengintegrasikan *platform * video *conference* \( *Zoom,* *Google Meet*\) langsung ke dalam sistem untuk sesi online yang lebih *seamless*. 

5. ***Self-Service *****Portal **: Memperluas fitur *self-service* untuk klien, seperti *reschedule * mandiri, akses ke *resource library*, dan *self-assessment tools*. 

6. **Analitik Prediktif**: Mengembangkan analitik prediktif untuk mengidentifikasi klien yang berisiko berpindah dan memberikan intervensi proaktif. 

**Strategi CRM:** 

1. ***Segmentasi *****Lebih *Granular. ***** **: Mengembangkan segmentasi yang lebih detail berdasarkan *psychographic * dan behavioral data untuk personalisasi yang lebih baik. 

2. ***Customer Journey Mapping***** **: Melakukan *customer journey mapping* yang detail untuk mengidentifikasi pain points dan *opportunities* di setiap tahap perjalanan klien. 

3. ***Omnichannel Strategy***** **: Mengintegrasikan berbagai saluran komunikasi \(website, email, WhatsApp, media sosial\) untuk pengalaman yang konsisten. 

4. ***Content Marketing***** **: Mengembangkan strategi content marketing yang lebih agresif untuk edukasi dan engagement klien. 

**Operasional :** 

1. **Pelatihan Berkelanjutan **: Menyelenggarakan pelatihan *refresher* berkala untuk memastikan semua pengguna memanfaatkan fitur CRM secara optimal. 

2. **Siklus Umpan Balik **: Membangun mekanisme umpan balik yang lebih sistematis untuk perbaikan berkelanjutan berdasarkan masukan pengguna. 

3. **KPI Monitoring **: Menetapkan dan memantau KPI CRM secara rutin \(bulanan\) untuk memastikan pencapaian target. 

4. **Tolok Ukur Kompetitor **: Melakukan tolok ukur dengan kompetitor dan praktik terbaik industri untuk terus meningkatkan strategi CRM. 

**5.2.2. Saran untuk Penelitian Selanjutnya **

1. **Studi Longitudinal **: Melakukan studi *longitudinal * untuk mengukur dampak jangka panjang CRM terhadap outcome kesehatan klien dan *sustainability* bisnis. 





63 



2. **Studi Komparatif **: Membandingkan efektivitas CRM di berbagai jenis layanan kesehatan mental \(psikologi, psikiatri, konseling\) untuk mengidentifikasi praktik terbaik. 

3. **Analisis Prediktif **: Mengembangkan model prediktif untuk *churn, lifetime* *value*, dan *outcome* terapi menggunakan *machine learning*. 

4. **Aspek Etika **: Meneliti aspek etika dalam penggunaan data klien untuk CRM, terutama terkait privasi dan *consent*. 

5. **ROI Jangka Panjang **: Mengukur ROI CRM dalam jangka panjang \(3-5 

tahun\) untuk memahami *sustainability* dan *scalability*. 

6. **Faktor Keberhasilan **: Mengidentifikasi faktor-faktor kunci keberhasilan perancangan dan implementasi CRM di layanan kesehatan mental melalui studi multikasus. 

**5.2.3. Saran untuk Industri Kesehatan Mental **

1. **Adopsi Teknologi **: Mendorong lebih banyak penyedia layanan kesehatan mental untuk mengadopsi teknologi CRM untuk meningkatkan kualitas layanan. 

2. **Standarisasi **: Mengembangkan standar industri untuk CRM dalam layanan kesehatan mental, termasuk praktik terbaik dan pedoman etika. 

3. **Kolaborasi **: Membangun kolaborasi antar penyedia layanan untuk berbagi pembelajaran dan praktik terbaik dalam perancangan dan implementasi CRM. 

4. **Regulasi **: Mengadvokasi regulasi yang mendukung digitalisasi layanan kesehatan mental sambil melindungi privasi dan keamanan data klien. 

5. **Edukasi **: Meningkatkan edukasi kepada masyarakat tentang manfaat layanan kesehatan mental digital dan mengurangi stigma. 

**5.2.4. Saran untuk Pengembang Sistem **

1. ***User Experience***** **: Terus meningkatkan *user experience* dengan melakukan usability testing berkala dan iterasi desain. 

2. **Keamanan **: Menerapkan praktik terbaik keamanan terbaru dan melakukan audit keamanan berkala. 

3. **Skalabilitas **: Memastikan arsitektur sistem dapat di- *scale* untuk menangani pertumbuhan jumlah pengguna dan data. 

4. **Integrasi **: Mengembangkan API yang robust untuk memungkinkan integrasi dengan sistem eksternal \( *ERP, payment gateway, analytics tools*\). 





64 



5. ***Mobile***** App **: Mengembangkan aplikasi *mobile native* untuk pengalaman yang lebih baik di perangkat mobile. 

6. ***Accessibility ***: Memastikan sistem *accessible* untuk pengguna dengan disabilitas sesuai standar WCAG. 





**DAFTAR PUSTAKA **

\[1\] 

N. A. A. Anggara, J. Hutahaean, and M. Iqbal, “Penerapan Customer Relationship Management \(CRM\) Dalam Sistem Informasi Penjualan Kosmetik Berbasis Web,” *Building of Informatics, Technology and Science* *\(BITS\)*, vol. 3, no. 4, pp. 480–488, Mar. 2022, doi: 10.47065/bits.v3i4.1440. 

\[2\] 

Y. S. Hardiana and T. D. Pramono, “PENERAPAN CRM UNTUK 

MENINGKATKAN LOYALITAS PELANGGAN,” 2022. 

\[3\] 

R. Syabania and N. Rosmawarni, “PERANCANGAN APLIKASI 

CUSTOMER RELATIONSHIP MANAGEMENT \(CRM\) PADA 

PENJUALAN BARANG PRE-ORDER BERBASIS WEBSITE,” 2021. 

\[4\] 

T. Rachmawati, “KEGUNAAN CUSTOMER RELATIONSHIP 

MANAGEMENT \(CRM\),” 2022. 

\[5\] 

S. Wahyuni, “Jurnal Teknik dan Teknologi Tepat Guna PERANCANGAN 

COSTUMER RELATIONSHIP MANAGEMENT PADA CV. KHARISMA 

MUDA MEDICAL LABORATORY & INSTRUMENT HOSPITAL,” Oct. 

2025. \[Online\]. Available: https://rcf-

indonesia.org/jurnal/index.php/jtechvolume4 

\[6\] 

L. Puad, D. Helmawanti, U. Negeri, I. Sulthan, and T. Saifuddin, 

“OPTIMALISASI CUSTOMER RELATIONSHIP MANAGEMENT \(CRM\) 

DI KLINIK KEI MEDIKA JAMBI,” 2025. 

\[7\] 

A. Pratama and M. Panduwangi, “TINJAUAN CUSTOMER LIFE CYCLE 

PADA PT. SUMBER ANEKA INOVASI,” *Jurnal Aplikasi Bisnis Kesatuan*, vol. 5, no. 1, pp. 81–90, Apr. 2025, doi: 10.37641/jabkes.v5i1.1910. 

\[8\] 

B. T. Kristanti, A. Junaidi, and E. P. Mandyartha, “IMPLEMENTASI K-MEANS CLUSTERING DALAM SEGMENTASI PELANGGAN 

BERDASARKAN USIA, PENDAPATAN, DAN MODEL RFM \(STUDI 

KASUS: LANTIKYA STORE JOMBANG\),” *Jurnal Informatika dan Teknik* *Elektro Terapan*, vol. 12, no. 3, Aug. 2024, doi: 10.23960/jitet.v12i3.4677. 

\[9\] 

Nurbaiti, Harahap Nur Hamidah, Putra Raulanda Dwi, and Sitepu Salma Agita, “PERAN META DATA MANAGEMENT DALAM 

PERSONALISASI LAYANAN E-COMMERCE: STUDI KASUS PADA 

BUKALAPAK,” *Jurnal Ilmiah Ekonomi Dan Manajemen Vol.3 No.6*, Jun. 

2025, doi: 10.61722/jiem.v3i6.5010. 

\[10\] S. Manajemen, F. E. Universitas, M. Raja, A. Haji, F. Kusasi, and B. 

Paramita, “Aplikasi Sistem Informasi CRM Berbasis Web,” *Jurnal Bahtera* *Inovasi*, vol. 5, no. 2, 2022. 

\[11\] Cindy Adeliya Samosir, “Strategi Customer Relationship Management untuk Meningkatkan Retensi Pelanggan di Era Digital,” *Repeater : Publikasi Teknik* *Informatika dan Jaringan*, vol. 3, no. 1, pp. 160–173, Jan. 2025, doi: 10.62951/repeater.v3i1.369. 

\[12\] Tarumingkeng Rudy C, “MANAJEMEN HUBUNGAN PELANGGAN 

\(Customer Relationship Management, CRM\),” Apr. 2025. 

\[13\] M. W. Ilhami, W. Vera Nurfajriani, A. Mahendra, R. A. Sirodj, and W. 

Afgani, “Penerapan Metode Studi Kasus Dalam Penelitian Kualitatif,” *Jurnal* *Ilmiah Wahana Pendidikan*, vol. 10, no. 9, pp. 462–469, 2024, doi: 10.5281/zenodo.11180129. 





65 





66 





**DAFTAR RIWAYAT HIDUP **

****

**I. **

**Biodata Mahasiswa **

NIM 

: 11250066 

Nama Lengkap 

: Roki Anjas 

Tempat / Tanggal Lahir 

: Purbalingga, 05 April 1999 

Alamat Domisili 

: Jl. AMD 6 No 95 RT 10/ RW 08, Duri Kosambi, 

Cengkareng, Jakarta Barat, DKI Jakarta 

**II. **

**Pendidikan **

**a. Formal **

1. SDN 2 Mengangkan Tahun 2011 

2. SMPN 1 Somagede Tahun 2014 

3. SMK HKTI 2 Purwareja Klampok Tahun 2017 

## 4. Universitas Bina Sarana Informatika Tahun 2021 

**b. Tidak Formal **

1. Pelatihan dan Sertifikat SKNN di Universitas Muhammadiyah Purwokerto Sebagai *Junior Nerwork Administrator* 

**III. **

**Riwayat Pengalaman Berorganisasi / Pekerjaan * ***

1. PIK-R di Desa Somakaton Tahun 2015 s.d. 2016 

2. Freelance Toko Komputer Banjarnegara Tahun 2016 s.d. 2017 

3. CV Java Multi Mandiri Sebagai *Web Engginer* Tahun 2017 s.d 2023 

4. PT Murni Solusindo Nusantara Sebagai *Web Developer * Tahun 2023 s.d Sekarang 

Jakarta, 31 Desember 2025 





Roki Anjas 





67 





**DAFTAR RIWAYAT HIDUP **

****

**I. Biodata Mahasiswa **

NIM 

: 11250068 

Nama Lengkap 

: Susanto 

Tempat / Tanggal Lahir 

: Tangerang, 03 Februari 1985 

Alamat Domisili 

: KP. Gelam, RT 008 / RW 002, 

Kec. Pasar Kemis, Kab. Tangerang 

**II. Pendidikan **

**a. Formal **

1. SDN 2 Kutajaya 1 Tahun 1998 

2. SMPN 1 Pasar Kemis Tahun 2001 

3. SMK Tunas Harapan Pati Tahun 2004 

## 4. Universitas Bina Sarana Informatika Tahun 2009 

**b. Tidak Formal **

## 1. - 

**III. Riwayat Pengalaman Berorganisasi / Pekerjaan * ***

1. PT Utama Raya Motor Tahun 2004 s.d 2010 

2. PT Bank Mandiri Tahun 2017 s.d Sekarang 



Jakarta, 31 Desember 2025 





Susanto 





68 





**DAFTAR RIWAYAT HIDUP **

****

**I. **

**Biodata Mahasiswa **

NIM 

: 11250085 

Nama Lengkap 

: Fahruroji 

Tempat / Tanggal Lahir : Tangerang, Mei 1983 

Alamat Domisili 

: Jl. Cikini Dalam RT 03 / RW 01 No. 133, Jurang 

Mangu Barat, Pondok Aren, Tangerang Selatan 

15223 

**II. **

**Pendidikan **

**a. Formal **

1. MI Nurul Iman Tahun 1995 

2. MTs N 13 Jakarta Tahun 1998 

3. SMA N 47 Jakarta Tahun 2001 

## 4. Universitas Bina Sarana Informatika Tahun 2007 

**b. Tidak Formal **

1. Pelatihan *Public Speaking** ***

2. Pelatihan *Impresive Communication*** **

3. Pelatihan *Hypnosis Instructur*** **

**III. **

**Riwayat Pengalaman Berorganisasi / Pekerjaan **

1. PT Dayu Tahun 2001 s.d 2002 

2. PT Sibolga Jaya Tahun 2002 s.d 2007 

3. PT Bagus Bina Cendekia 2007 s.d 2010 

4. *Freelancer * 2010 s.d Sekarang * *

****

Jakarta, 31 Desember 2025 





Fahruroji 

69



