# BAB I  
# PENDAHULUAN

## 1.1 Latar Belakang Masalah

**[GAMBAR 1.1 - Logo CUR-HEART]**

Kesehatan mental telah menjadi salah satu isu kesehatan global yang paling mendesak di abad ke-21. Menurut data Organisasi Kesehatan Dunia (*World Health Organization*/WHO) tahun 2023, lebih dari 450 juta orang di seluruh dunia mengalami gangguan kesehatan mental, dengan proyeksi peningkatan yang signifikan setiap tahunnya. Di Indonesia, berdasarkan data Riset Kesehatan Dasar (Riskesdas) Kementerian Kesehatan Republik Indonesia tahun 2023, prevalensi gangguan kesehatan mental mencapai 20% dari total populasi, yang berarti sekitar 1 dari 5 orang Indonesia mengalami masalah kesehatan mental mulai dari tingkat ringan hingga berat.

**[GAMBAR 1.2 - Statistik Kesehatan Mental Indonesia]**

Fenomena ini dipicu oleh berbagai faktor kompleks yang saling berkaitan seperti tekanan pekerjaan yang semakin tinggi, ketidakstabilan ekonomi pascapandemi COVID-19, gangguan digital, serta perubahan nilai-nilai sosial yang cepat. Kondisi ini diperparah dengan masih tingginya stigma sosial terhadap gangguan kesehatan mental di masyarakat Indonesia, yang menyebabkan banyak penderita enggan mencari bantuan profesional.

Meskipun kesadaran akan pentingnya kesehatan mental mulai meningkat, akses terhadap layanan kesehatan mental yang berkualitas masih sangat terbatas. Indonesia memiliki rasio tenaga kesehatan mental yang sangat rendah, yaitu hanya sekitar 1:200.000 penduduk, jauh di bawah standar WHO yang merekomendasikan 1:100.000. Layanan kesehatan mental konvensional juga seringkali memiliki waktu tunggu yang lama, biaya tinggi, lokasi yang tidak mudah diakses, serta proses administrasi yang rumit.

Di tengah keterbatasan tersebut, metode terapi alternatif berbasis hipnoterapi mulai mendapat perhatian sebagai solusi yang efektif dan efisien. Hipnoterapi (*hypnotherapy*) adalah metode terapi yang menggunakan teknik hipnosis untuk mengakses alam bawah sadar, membantu mengatasi berbagai masalah psikologis seperti trauma, stres, kecemasan, fobia, hingga kebiasaan buruk. Penelitian ilmiah telah membuktikan efektivitas hipnoterapi dengan tingkat keberhasilan 75-85% dalam mengatasi gangguan kecemasan, dengan durasi terapi yang relatif lebih singkat (6-8 sesi) dibandingkan terapi konvensional (12-20 sesi).

CUR-HEART (*Hypnotherapy & Mind Wellness Center*) hadir sebagai pusat layanan terapi kesehatan mental yang mengintegrasikan pendekatan hipnoterapi modern dengan nilai-nilai spiritualitas dan humanisme. CUR-HEART menyediakan berbagai layanan terapi seperti Pelepasan Stres & Kecemasan, Penyembuhan Trauma, Kepercayaan Diri & Motivasi, Tidur & Relaksasi, Pemrograman Ulang Kebiasaan, dan Pengelolaan Fobia & Ketakutan.

Namun, dalam menjalankan operasionalnya, CUR-HEART menghadapi berbagai tantangan manajerial yang menghambat efisiensi dan kualitas layanan. Proses reservasi yang masih manual melalui telepon atau WhatsApp sering menyebabkan kesalahpahaman, reservasi ganda (*double booking*), dan kesulitan pelacakan status. Manajemen jadwal terapis menggunakan lembar kerja atau kalender manual tidak efisien dan rawan kesalahan. Dokumentasi catatan sesi terapi yang masih menggunakan kertas atau berkas terpisah menyulitkan pencarian riwayat dan pemantauan kemajuan klien.

Tidak adanya sistem informasi terpadu menyebabkan CUR-HEART kesulitan menganalisis data operasional seperti tingkat hunian terapis, layanan yang diminati, aliran pendapatan, hingga kepuasan klien. Hal ini menghambat pengambilan keputusan strategis berbasis data. Klien juga tidak memiliki platform yang memudahkan mereka melihat informasi layanan, profil terapis, ketersediaan jadwal, riwayat reservasi, serta pelacakan kemajuan terapi secara mandiri.

Pengembangan sistem informasi layanan terapi mental berbasis digital menjadi solusi yang sangat diperlukan. Sistem informasi dapat mengotomatisasi proses bisnis, meningkatkan akurasi data, memfasilitasi komunikasi, serta menyediakan dasbor pemantauan untuk pengambilan keputusan. Studi literatur menunjukkan implementasi sistem informasi di sektor layanan kesehatan dapat meningkatkan efisiensi operasional hingga 40%, mengurangi kesalahan administrasi hingga 60%, dan meningkatkan kepuasan pelanggan hingga 35%.

Proyek ini mengembangkan sistem informasi berbasis web menggunakan Laravel sebagai kerangka kerja utama dan Tailwind CSS untuk desain antarmuka, dengan pendekatan Siklus Hidup Pengembangan Sistem (*System Development Life Cycle*/SDLC) model air terjun (*waterfall*). Sistem yang dihasilkan diharapkan dapat memberikan solusi komprehensif untuk manajemen operasional CUR-HEART, meningkatkan pengalaman pengguna, serta mendukung pengambilan keputusan berbasis data untuk pengembangan bisnis berkelanjutan.

## 1.2 Identifikasi Masalah

Berdasarkan analisis kondisi eksisting pada CUR-HEART melalui observasi, wawancara dengan pemangku kepentingan, dan studi dokumentasi proses bisnis, teridentifikasi beberapa permasalahan utama yang menghambat efektivitas dan efisiensi operasional, yaitu:

1. **Proses Reservasi yang Tidak Efisien**

   Proses reservasi layanan terapi yang masih dilakukan secara manual melalui komunikasi telepon, WhatsApp, atau surel mengakibatkan berbagai masalah operasional. Admin harus melakukan pemeriksaan manual terhadap kalender terapis, yang memakan waktu rata-rata 5-10 menit per reservasi. Seringkali terjadi kesalahpahaman komunikasi antara klien, admin, dan terapis mengenai jadwal atau informasi penting lainnya. Tingkat konversi dari pertanyaan menjadi reservasi aktual hanya mencapai 60%, yang berarti 40% calon klien membatalkan niat mereka karena proses yang rumit.

2. **Ketiadaan Sistem Manajemen Jadwal Terapis Terpadu**

   Manajemen jadwal terapis menggunakan lembar kerja Excel atau Kalender Google manual tidak efisien dan rawan konflik jadwal. Setiap terapis mengelola kalendernya sendiri dengan format berbeda-beda, menyulitkan admin untuk sinkronisasi dan pemeriksaan ketersediaan secara waktu nyata. Ketika ada perubahan jadwal mendadak, proses pemberitahuan dan penjadwalan ulang dilakukan manual satu per satu. Seringkali terjadi reservasi ganda (*double booking*) atau kesalahan penjadwalan, serta ketimpangan beban kerja antar terapis.

3. **Dokumentasi Catatan Terapi yang Tidak Terstruktur**

   Dokumentasi catatan sesi terapi menggunakan metode konvensional (kertas fisik atau berkas Word terpisah) menimbulkan berbagai masalah. Terapis membutuhkan waktu tambahan 10-15 menit untuk menulis catatan manual. Catatan yang tersimpan dalam format fisik sangat sulit dicari kembali. Tidak adanya templat standar menyebabkan inkonsistensi dokumentasi antar terapis. Risiko kehilangan data tinggi dan tidak ada sistem pencadangan yang menjamin keamanan data sensitif.

4. **Tidak Ada Sistem Pelacakan Kemajuan Klien**

   Ketiadaan sistem pelacakan kemajuan klien yang sistematis menyulitkan terapis dalam mengevaluasi efektivitas terapi. Terapis hanya mengandalkan ingatan dan catatan manual yang tidak terstruktur. Klien tidak memiliki visibilitas terhadap kemajuan mereka sendiri. Tidak adanya data kemajuan yang terukur menyulitkan dalam membuktikan keberhasilan terapi dan mengidentifikasi klien yang memerlukan perhatian khusus.

5. **Keterbatasan Akses Informasi bagi Klien**

   Klien kesulitan mengakses informasi lengkap tentang layanan, terapis, jadwal ketersediaan, dan harga secara mandiri. Mereka harus selalu menghubungi admin untuk mendapatkan informasi, terutama di luar jam operasional. Klien tidak dapat melihat riwayat reservasi, status pembayaran, atau catatan terapis dengan mudah. Tidak adanya platform layanan mandiri (*self-service*) mengurangi rasa otonomi dan kepuasan klien.

6. **Kesulitan dalam Pengambilan Keputusan Manajerial**

   Manajemen kesulitan mengakses data operasional dan bisnis untuk pengambilan keputusan strategis. Tidak ada dasbor atau sistem pelaporan yang menyediakan indikator kinerja utama (*Key Performance Indicators*/KPI). Data tersebar di berbagai platform, sulit dikompilasi dan dianalisis. Pembuatan laporan memakan waktu berhari-hari dan rawan kesalahan. Ketiadaan kecerdasan bisnis menghambat optimasi operasional dan pertumbuhan bisnis.

7. **Tidak Ada Sistem Pembayaran Terpadu**

   Proses pembayaran manual melalui transfer bank dengan konfirmasi manual sangat tidak efisien. Klien harus melakukan transfer, mengirimkan bukti, dan menunggu konfirmasi yang kadang memakan waktu berjam-jam bahkan berhari-hari. Tidak ada pembuatan tanda terima atau faktur otomatis. Pelacakan status pembayaran sulit dilakukan dan seringkali terjadi pembayaran yang hilang atau ganda. Tidak adanya berbagai pilihan pembayaran digital mengurangi kemudahan bagi klien.

8. **Risiko Keamanan dan Privasi Data yang Tinggi**

   Data klien yang sangat sensitif disimpan dalam format yang tidak aman seperti berkas tidak terenkripsi atau bahkan di obrolan WhatsApp. Tidak ada mekanisme pengendalian akses yang tepat dan jejak audit yang mencatat akses data. Kepatuhan terhadap UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi tidak dapat dipastikan, menimbulkan risiko hukum.

**[GAMBAR 1.3 - Perbandingan Reservasi Manual vs Digital]**

Permasalahan-permasalahan tersebut secara kumulatif menyebabkan penurunan efisiensi operasional, potensi kehilangan pendapatan, risiko reputasi, terhambatnya skalabilitas bisnis, dan hilangnya peluang optimisasi. Oleh karena itu, pengembangan sistem informasi layanan terapi mental berbasis digital yang terpadu, aman, dan mudah digunakan menjadi kebutuhan mendesak.

## 1.3 Ruang Lingkup

Untuk memfokuskan pembahasan dan memastikan keberhasilan proyek, penelitian ini menetapkan batasan-batasan cakupan sebagai berikut:

**[GAMBAR 1.4 - Diagram Ruang Lingkup Sistem]**

### 1.3.1 Ruang Lingkup Fungsional

Sistem informasi yang dikembangkan mencakup fungsi-fungsi utama sebagai berikut:

1. **Modul Autentikasi dan Manajemen Pengguna**
   - Pendaftaran dan verifikasi akun untuk klien dan terapis
   - Sistem masuk dengan pengendalian akses berbasis peran (admin, terapis, klien)
   - Manajemen kata sandi (lupa kata sandi, atur ulang, ubah kata sandi)
   - Manajemen profil pengguna

2. **Modul Informasi Publik**
   - Halaman arahan, tentang kami, layanan, direktori terapis
   - Blog/artikel edukatif tentang kesehatan mental
   - Halaman kontak dan FAQ

3. **Modul Reservasi dan Penjadwalan**
   - Alur reservasi bertahap (pilih layanan → pilih terapis → pilih jadwal → konfirmasi)
   - Kalender interaktif dengan visualisasi ketersediaan terapis
   - Manajemen reservasi (lihat, jadwal ulang, batal)
   - Notifikasi pengingat otomatis

4. **Modul Dasbor Klien**
   - Ikhtisar dasbor dengan ringkasan janji temu dan kemajuan
   - Manajemen janji temu dan riwayat reservasi
   - Pelacakan kemajuan terapi dengan visualisasi grafik
   - Komunikasi dengan terapis melalui pesan
   - Riwayat pembayaran dan unduh faktur

5. **Modul Dasbor Terapis**
   - Ikhtisar dasbor dengan statistik kinerja
   - Manajemen jadwal dan ketersediaan (termasuk pemblokiran tanggal)
   - Manajemen klien dan sesi terapi
   - Dokumentasi catatan sesi terapi terstruktur
   - Pelacakan kemajuan klien dan komunikasi
   - Melihat penghasilan dan riwayat sesi

6. **Modul Dasbor Admin**
   - Ikhtisar dasbor dengan metrik operasional dan keuangan
   - Manajemen pengguna, terapis, layanan, dan reservasi
   - Manajemen konten (blog, FAQ, layanan, promo)
   - Verifikasi dan persetujuan terapis baru
   - Manajemen ulasan dan penilaian klien
   - Pelaporan dan analitik (operasional, keuangan, kinerja)
   - Pengaturan sistem

7. **Modul Pembayaran**
   - Integrasi dengan gerbang pembayaran (Midtrans, Xendit, atau sejenisnya)
   - Berbagai metode pembayaran (transfer bank, kartu kredit, dompet elektronik, QRIS)
   - Pembuatan faktur dan tanda terima otomatis
   - Pelacakan status pembayaran

8. **Modul Notifikasi dan Komunikasi**
   - Notifikasi surel (pendaftaran, konfirmasi reservasi, pengingat, pembayaran)
   - Notifikasi dalam aplikasi
   - Sistem pesan antar pengguna

### 1.3.2 Ruang Lingkup Teknis

1. **Platform:**
   - Aplikasi web berbasis Laravel Framework (PHP)
   - Basis data MySQL
   - Desain responsif menggunakan Tailwind CSS
   - Hosting pada VPS dengan domain dan SSL

2. **Arsitektur:**
   - Arsitektur monolitik dengan pola MVC
   - Sistem informasi manajemen terintegrasi dalam satu aplikasi

3. **Keamanan:**
   - Autentikasi dan otorisasi berbasis peran
   - Enkripsi data sensitif
   - Kepatuhan terhadap UU PDP Indonesia
   - Pencadangan data otomatis

### 1.3.3 Ruang Lingkup Pengguna

Sistem ini diperuntukkan bagi tiga kategori pengguna utama:

1. **Admin/Pemilik CUR-HEART** - Mengelola seluruh aspek sistem, pemantauan, dan pelaporan
2. **Terapis** - Mengelola jadwal, sesi terapi, dokumentasi, dan komunikasi dengan klien
3. **Klien** - Melakukan reservasi, mengelola janji temu, pelacakan kemajuan, dan komunikasi

### 1.3.4 Batasan Sistem

Beberapa fitur berikut **tidak** termasuk dalam ruang lingkup proyek ini:

1. Tidak ada pengembangan fitur konferensi video bawaan (menggunakan integrasi pihak ketiga)
2. Tidak ada aplikasi seluler bawaan (menggunakan desain web responsif)
3. Tidak ada fitur kecerdasan buatan atau pembelajaran mesin
4. Tidak ada resep telemedis atau resep obat
5. Tidak ada dukungan multibahasa (hanya Bahasa Indonesia)
6. Tidak ada analitik prediktif atau penambangan data kompleks

### 1.3.5 Ruang Lingkup Metodologi

1. **Metodologi Pengembangan:**
   - Siklus Hidup Pengembangan Sistem (*System Development Life Cycle*/SDLC) dengan model Air Terjun (*Waterfall*)
   - Tahapan: Analisis → Desain → Implementasi → Pengujian → Penerapan

2. **Teknik Pengumpulan Data:**
   - Observasi terhadap proses bisnis yang ada
   - Wawancara dengan pemangku kepentingan (*owner*, terapis, sampel klien)
   - Studi literatur dan praktik terbaik
   - Analisis dokumen internal CUR-HEART

3. **Teknik Analisis Sistem:**
   - Analisis kebutuhan fungsional dan non-fungsional
   - Analisis Kasus Pakai (*Use Case Analysis*) dengan Diagram Kasus Pakai UML
   - Pemodelan proses dengan Diagram Aktivitas (*Activity Diagram*)
   - Pemodelan data dengan Diagram Relasi Entitas (*Entity Relationship Diagram*/ERD)

4. **Teknik Desain:**
   - Desain basis data dengan normalisasi hingga Bentuk Normal Ketiga (3NF)
   - Desain antarmuka pengguna dengan kerangka kawat (*wireframe*) dan maket fidelitas tinggi (*high-fidelity mockup*)
   - Desain arsitektur sistem
   - Desain keamanan

5. **Teknik Pengujian:**
   - Pengujian unit (*unit testing*) untuk fungsi individual
   - Pengujian fungsional dengan pendekatan kotak hitam (*black-box*)
   - Pengujian kebergunaan (*usability testing*) dengan sampel pengguna
   - Pengujian Penerimaan Pengguna (*User Acceptance Testing*/UAT) dengan pemangku kepentingan

### 1.3.6 Ruang Lingkup Luaran (*Deliverables*)

Luaran yang dihasilkan dari proyek ini adalah:

1. **Dokumentasi:**
   - Laporan Proyek Akhir (*Capstone Project*) lengkap (80-100 halaman)
   - Dokumentasi sistem (dokumentasi teknis)
   - Panduan pengguna untuk setiap peran pengguna
   - Dokumentasi skema basis data

2. **Sistem:**
   - Prototipe fungsional aplikasi web (66 halaman mockup)
   - Kode sumber lengkap di repositori GitHub
   - Basis data dengan data sampel
   - Panduan penerapan (*deployment*)

3. **Presentasi:**
   - Salindia presentasi PowerPoint (15-20 salindia)
   - Video demonstrasi sistem (5-10 menit)
   - *X-Banner* infografis proyek

4. **Tambahan:**
   - Video promosi CUR-HEART (2-3 menit) untuk berbagai media sosial
   - Surat keterangan riset dari CUR-HEART
   - Dokumen keabsahan data dan produk

Dengan batasan ruang lingkup yang jelas ini, proyek dapat difokuskan pada pengembangan fitur-fitur inti yang paling krusial untuk operasional CUR-HEART, sambil tetap memastikan kualitas dan kelengkapan implementasi.

## 1.4 Tujuan dan Manfaat Penelitian

### 1.4.1 Tujuan Penelitian

Penelitian ini bertujuan untuk:

1. **Menganalisis kebutuhan sistem informasi** manajemen reservasi dan terapi hipnoterapi CUR-HEART melalui studi mendalam terhadap proses bisnis, wawancara pemangku kepentingan, dan identifikasi masalah operasional.

2. **Merancang sistem informasi** yang terstruktur, dapat dikembangkan (*scalable*), dan mudah digunakan (*user-friendly*) dengan menggunakan diagram ERD, UML, dan desain antarmuka berbasis praktik terbaik UI/UX.

3. **Mengimplementasikan sistem informasi** berbasis web menggunakan Laravel Framework, MySQL, dan Tailwind CSS yang mencakup modul autentikasi, reservasi, penjadwalan, dasbor berbasis peran, pembayaran, dan pelaporan.

4. **Menguji sistem secara menyeluruh** untuk memastikan fungsionalitas, kegunaan, keandalan, dan keamanan melalui pengujian unit, integrasi, sistem, dan pengujian penerimaan pengguna (UAT).

5. **Menyebarkan sistem ke lingkungan produksi** yang dapat diakses 24/7 dengan konfigurasi server, domain, SSL, dan mekanisme pencadangan data.

6. **Menyusun dokumentasi lengkap** (teknis, pengguna, dan akademik) untuk memastikan keberlanjutan dan kemudahan pemeliharaan sistem.

7. **Mengukur dampak sistem** terhadap efisiensi operasional, kepuasan pengguna, dan kinerja bisnis CUR-HEART.

### 1.4.2 Manfaat Penelitian

Penelitian ini diharapkan memberikan manfaat kepada berbagai pihak:

#### 1.4.2.1 Manfaat bagi CUR-HEART (Organisasi)

1. Peningkatan efisiensi operasional hingga 60% melalui otomatis proses manual
2. Peningkatan pendapatan dengan tingkat konversi dari 60% menjadi 85%
3. Pengambilan keputusan berbasis data melalui dasbor analitik dan pelaporan
4. Keunggulan kompetitif sebagai pusat hipnoterapi dengan sistem digital profesional
5. Skalabilitas bisnis untuk ekspansi terapis, lokasi, dan layanan
6. Kepatuhan terhadap regulasi dan mitigasi risiko keamanan data
7. Peningkatan citra merek dan kredibilitas

#### 1.4.2.2 Manfaat bagi Terapis

1. Kemudahan manajemen jadwal dan ketersediaan
2. Efisiensi dokumentasi sesi terapi (pengurangan waktu hingga 50%)
3. Manajemen klien yang lebih baik dengan akses profil lengkap dan riwayat
4. Transparansi penghasilan dengan dasbor waktu nyata
5. Wawasan kinerja untuk pengembangan profesional
6. Pengurangan beban administratif untuk fokus pada kualitas terapi

#### 1.4.2.3 Manfaat bagi Klien

1. Kemudahan akses layanan 24/7 melalui reservasi online
2. Transparansi informasi lengkap tentang layanan, terapis, dan harga
3. Kontrol dan otonomi melalui platform layanan mandiri
4. Visibilitas kemajuan terapi dengan visualisasi objektif
5. Privasi dan kerahasiaan data terjamin dengan sistem keamanan berlapis
6. Komunikasi yang lebih baik dengan terapis melalui fitur pesan
7. Pengalaman pengguna yang baik dengan antarmuka modern dan responsif

#### 1.4.2.4 Manfaat bagi Akademik

1. Kontribusi ilmu pengetahuan di bidang sistem informasi kesehatan mental
2. Referensi untuk penelitian selanjutnya
3. Studi kasus untuk pembelajaran mata kuliah terkait
4. Dokumentasi praktik terbaik pengembangan sistem informasi
5. Contoh kolaborasi industri-akademik yang efektif

#### 1.4.2.5 Manfaat bagi Masyarakat

1. Peningkatan akses ke layanan kesehatan mental yang berkualitas
2. Pengurangan stigma terhadap terapi kesehatan mental
3. Edukasi kesehatan mental melalui konten blog dan artikel
4. Model digitalisasi untuk UMKM layanan kesehatan lainnya
5. Kontribusi pada penciptaan lapangan kerja di sektor kesehatan mental
