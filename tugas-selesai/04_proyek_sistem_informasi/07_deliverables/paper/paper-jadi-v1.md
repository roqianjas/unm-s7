## **SISTEM INFORMASI MANAJEMEN **

### **RESERVASI TERAPI CUR-HEART **

**\(PUSAT HIPNOTERAPI & KESEHATAN MENTAL\) **

**BERBASIS WEB DENGAN KERANGKA KERJA LARAVEL **



## **MAKALAH **

Diajukan untuk memenuhi salah satu tugas kelompok mata kuliah Proyek Sistem Informasi 



Nama Anggota Kelompok : 

1. Roki Anjas 

11250066 

2. Fahruroji 

11250085 

3. Susanto 

11250068 



Kelas: 11.7C.12 



**PROGRAM STUDI INFORMATIKA **

**UNIVERSITAS NUSA MANDIRI **

**JAKARTA **

## **2025 **





**BAB I **

## **PENDAHULUAN **

**1.1. ** **Latar Belakang Masalah **



Di era ekonomi modern saat ini tanpa disadari menuntut masyarakat untuk terus bekerja dengan harapan bisa memenuhi semua kebutuhan pokok dan kebutuhan sosial yang tinggi berujuan mencapai kepentingan personal branding atau sering dikenal dengan *Flexing*. Fenomena ini dipicu oleh tekanan pekerjaan, ketidakstabilan ekonomi dan gangguan digital \(Sosial Media\). Pengaruh ekonomi modern saat ini memberikan dampak yang cukup signifikan meningkat oleh kesehatan mental dan menjadi isu kesehatan global yang mendesak di abad ke-21. 

Kesehatan mental merupakan terwujudnya keselarasan yang sungguh-sungguh antara fungsi kejiwaan yang menciptakan penyesuaian diri antara manusia oleh dirinya sendiri dan lingkunganya \[1\] 

Indonesia memiliki rasio psikiater dan psikolog yang sangat rendah \(1:200.000\), jauh di bawah standar WHO \(1:100.000\). Layanan kesehatan mental konvensional seringkali memiliki waktu tunggu lama, biaya tinggi, lokasi tidak mudah diakses, serta proses administrasi rumit. Di tengah keterbatasan ini, hipnoterapi \( *hypnotherapy*\) sebagai metode terapi alternatif mulai mendapat perhatian sebagai solusi efektif dan efisien. 

CUR-HEART \( *Hypnotherapy & Mind Wellness Center*\) hadir sebagai pusat layanan terapi kesehatan mental yang mengintegrasikan pendekatan hipnoterapi modern dengan nilai spiritualitas dan humanisme. Namun, CUR-HEART 

menghadapi tantangan manajerial: \(1\) proses pemesanan manual via telepon/ *WhatsApp* menyebabkan kesalahpahaman dan pemesanan ganda; \(2\) manajemen jadwal terapis menggunakan *spreadsheet* tidak efisien dan rawan kesalahan; \(3\) dokumentasi catatan terapi menggunakan kertas/ *Word* terpisah menyulitkan pencarian riwayat; \(4\) tidak ada sistem pelacakan kemajuan klien yang terstruktur; \(5\) klien tidak memiliki *platform* layanan mandiri \( *self-service*\); \(6\) kesulitan dalam analisis data operasional dan pengambilan keputusan strategis; \(7\) sistem pembayaran manual rawan kesalahan dan kehilangan transaksi; \(8\) risiko keamanan dan privasi data tinggi. 





Pengembangan sistem informasi manajemen pemesanan dan terapi berbasis web menggunakan *Laravel Framework* menjadi solusi untuk mengotomatisasi proses bisnis, meningkatkan akurasi data, memfasilitasi komunikasi, serta menyediakan dasbor pemantauan untuk pengambilan keputusan berbasis data. 

Sistem ini dirancang dengan 41 halaman antarmuka mencakup halaman publik, autentikasi, dan dasbor untuk klien, terapis, dan admin, menggunakan pendekatan SDLC *Waterfall* dengan desain responsif *mobile-first*. 



## **1.2. Identifikasi Masalah **

Berdasarkan analisis kondisi eksisting melalui observasi, wawancara dengan pemangku kepentingan, dan studi dokumentasi proses bisnis, teridentifikasi permasalahan utama : 

1. Proses Pemesanan Tidak Efisien** **: Komunikasi manual via *WhatsApp* menyebabkan tingkat konversi hanya 60%, tidak ada transparansi informasi terapis dan layanan, klien tidak dapat membandingkan sebelum memutuskan. 

2. Ketiadaan Sistem Manajemen Jadwal Terpadu : Penjadwalan manual menyebabkan konflik jadwal, tidak ada sistem pemblokiran tanggal untuk cuti, ketimpangan beban kerja antar terapis. 

3. Dokumentasi Tidak Terstruktur** **: Catatan terapi terpisah-pisah, sulit diakses, tidak ada templat standar, risiko kehilangan data tinggi, tidak ada sistem pencadangan. 

4. Tidak Ada Pelacakan Kemajuan Klien : Klien tidak dapat melihat perkembangan terapi, tidak ada data terukur untuk evaluasi keberhasilan, sulit identifikasi klien yang perlu perhatian khusus. 

5. Keterbatasan Akses Informasi Klien : Tidak ada platform *self-service*, klien bergantung penuh pada admin, tidak dapat melakukan penjadwalan ulang mandiri. 

6. Kesulitan Pengambilan Keputusan : Tidak ada laporan otomatis, analisis manual memakan waktu, tidak ada *business intelligence* untuk optimasi operasional. 



7. Sistem Pembayaran Tidak Terpadu** **: Verifikasi manual, rekonsiliasi sulit, tidak ada variasi metode pembayaran digital, pelacakan status pembayaran sulit. 

8. Risiko Keamanan Data Tinggi** **: Tidak ada enkripsi, akses tidak terkontrol, tidak ada jejak audit, tidak patuh regulasi perlindungan data pribadi \(UU 

No. 27 Tahun 2022\). 

Dampak kumulatif : penurunan efisiensi operasional, potensi kehilangan pendapatan, risiko reputasi, terhambatnya skalabilitas bisnis, hilangnya peluang optimasi. 



**1.3. Ruang Lingkup **

## **1.3.1. Ruang Lingkup Sistem **

### Sistem informasi CUR-HEART mencakup : 

Modul Utama :** **

1. Manajemen Pengguna : Registrasi, autentikasi multi-peran \(Admin, Terapis, Klien\), profil pengguna, kontrol akses berbasis peran \(RBAC\). 

2. Manajemen Layanan : CRUD layanan terapi, kategori layanan, harga dan durasi, deskripsi detail, gambar layanan. 

3. Manajemen Pemesanan : Alur pemesanan 4 langkah \(pilih layanan → pilih terapis → pilih jadwal → pembayaran\), kalender ketersediaan real-time, konfirmasi otomatis, notifikasi email/SMS. 

4. Manajemen Jadwal Terapis : Pengaturan ketersediaan \(hari, jam operasional, jadwal berulang\), pemblokiran tanggal cuti, visualisasi kalender, pencegahan konflik jadwal. 

5. Manajemen Sesi Terapi **:** Dokumentasi catatan terapi terstruktur, templat berdasarkan jenis layanan, riwayat sesi per klien, pelacakan kemajuan dengan metrik \(skala kecemasan, frekuensi sesi\). 

6. Sistem Pembayaran : Integrasi payment gateway \(Midtrans\), multiple *payment methods* \( *Virtual Account*, *E-wallet, QRIS*, Kartu Kredit\), verifikasi otomatis, *invoice* digital. 



7. Dasbor Analitik **:** Dasbor Admin \(metrik bisnis komprehensif\), Dasbor Terapis \(jadwal, klien, pendapatan\), Dasbor Klien \(riwayat pemesanan, progress tracking\). 

8. Manajemen Konten : Halaman informatif \(About, Services, Blog\), FAQ, Privacy Policy, Terms & Conditions. 

## **1.3.2. Ruang Lingkup Teknologi **

a. *Backend* :** **

• *Framework : Laravel* 10.x \(PHP 8.2\) 

• *Database : MySQL* 8.0 

• *Authentication : Laravel Sanctum *

• *Payment Gateway* : Midtrans API 

b. *Frontend ***:** 

• *Blade Templating Engine *

• *Tailwind* CSS 3.x 

• *Alpine.js* \(interaktivitas ringan\) 

• *Responsive Design* \(Mobile-first\) 

c. *Infrastructure*** :** 

• *Web Server* : *Nginx*/ *Apache* 

• *Hosting* : VPS \( *Niagahoster*/AWS\) 

• *Version Control* : *Git/GitHub* 

• *Deployment* : Manual/CI-CD 

## **1.3.3. Ruang Lingkup Pengguna **

a. Tiga Peran Pengguna :** **

1. Admin : Manajemen seluruh sistem, *users, bookings, services*, laporan keuangan, pengaturan sistem. 

2. Terapis : Manajemen jadwal pribadi, lihat klien assigned, buat catatan sesi, lihat pendapatan, kelola profil. 

3. Klien** **: Reservasi layanan, lihat riwayat pemesanan, tracking *progress*, komunikasi dengan terapis, kelola profil. 

## **1.3.4. Batasan Sistem **

1. Tidak mencakup video *conferencing* untuk sesi online \(menggunakan *tools* eksternal seperti *Zoom*/ *Google Meet*\). 



2. Tidak ada aplikasi *mobile native* \( *responsive web only*\). 

3. Tidak ada integrasi dengan *Electronic Health Record* \(EHR\) *eksternal*. 

4. Tidak ada sistem *inventory* untuk produk fisik atau *merchandise*. 

5. Tidak ada *multi-language support* \(Bahasa Indonesia\). 

6. Tidak ada sistem *loyalty*/membership dengan poin *reward*. 

7. Tidak mencakup AI/ML untuk rekomendasi terapis atau prediksi. 

8. Tidak ada forum/komunitas untuk klien. 



**1.4. Tujuan dan Manfaat Penelitian **

## **1.4.1. Tujuan Penelitian **

**Tujuan Umum :** Mengembangkan sistem informasi manajemen pemesanan dan terapi berbasis web untuk meningkatkan efisiensi operasional dan kualitas layanan CUR-HEART. 

**Tujuan Khusus :** 

1. Menganalisis proses bisnis eksisting dan kebutuhan sistem CUR-HEART. 

2. Merancang arsitektur sistem, *database, * dan antarmuka pengguna yang *user-friendly*. 

3. Mengimplementasikan sistem menggunakan *Laravel Framework* dengan fitur komprehensif. 

4. Melakukan pengujian fungsional, *usability*, dan *performance* untuk memastikan kualitas. 

5. Menghasilkan 

dokumentasi 

lengkap 

untuk 

pemeliharaan 

dan 

pengembangan. 

## **1.4.2. Manfaat Penelitian **

**a. Bagi CUR-HEART :** 

• Efisiensi operasional meningkat 40% 

• Pengurangan kesalahan administrasi 60% 

• Peningkatan konversi pemesanan dari 60% ke 85% 

• Data terpusat untuk *business intelligence* 

• Skalabilitas untuk pertumbuhan bisnis 

**b. Bagi Terapis :** 

• Manajemen jadwal otomatis 



• Akses mudah ke riwayat klien 

• *Tracking* kinerja dan pendapatan 

• Dokumentasi terstruktur 

• Fokus pada layanan terapi, bukan administrasi 

**c. Bagi Klien :** 

• Kemudahan *booking* 24/7 

• Transparansi informasi layanan dan terapis 

• *Self-service* portal 

• *Tracking progress* terapi 

• Pengalaman pengguna lebih baik 

**d. Bagi Akademik :** 

• Model referensi pengembangan sistem informasi kesehatan mental 

• Kontribusi literatur tentang implementasi Laravel di sektor *healthcare *

• Studi kasus SDLC *Waterfall* dalam proyek nyata 

• Dokumentasi *best practices* untuk mahasiswa **e. Bagi Masyarakat :** 

• Peningkatan akses layanan kesehatan mental 

• Mengurangi stigma melalui kemudahan akses digital 

• Model sistem yang dapat diadopsi pusat terapi lain 

• Kontribusi pada digitalisasi layanan kesehatan Indonesia 

****



**BAB II **

## **TINJAUAN PUSTAKA **

****

## **2.1. Landasan Teori **

A. Pengertian Sistem Informasi 

Sistem merupakan kumpulan kelompok atau perangkat yang mempunyai hubungan antara satu unsur dengan lainnya berfungsi dalam mencapai suatu tujuan tertentu bersama.\[2\] 

Sistem adalah kumpulan prosedur kerja yang terjalin erat yang bekerja bersama sebagai satu jaringan demi menyelesaikan suatu kegiatan atau mencapai sasaran akhir tertentu.\[3\] 

Informasi adalah sekumpulan fakta yang terhimpun diolah menjadi data yang memiliki nilai yang dapat digunakan oleh siapapun yang membutuhkan data tersebut dalam mengambil keputusan maupun untuk ilmu pengetahuan.\[3\] 

Informasi adalah aset non-fisik yang krusial yang digunakan manajemen untuk menjalankan dan mengarahkan perusahaan.\[4\] 

Sistem Informasi adalah seluruh bagian teknologi dan prosedur yang disatukan sepenuhnya untuk mengelola data agar perusahaan atau organisasi selalu dapat menyajikan informasi yang akurat dari data yang telah diproses dan disimpan. \[5\] 

Sistem Informasi adalah susunan komponen yang saling terkait yang berfungsi untuk menghimpun, memproses, menyimpan, dan menyebarluaskan data dan informasi.\[6\] 

Fungsi Sistem Informasi : 

1. Sistem memastikan adanya standar kualitas yang tinggi dan kompetensi yang memadai dalam mengelola sistem informasi itu sendiri, dilakukan melalui pemikiran yang kritis dan terstruktur. 

2. Kemampuan sistem dalam menyediakan mutu \(kualitas\) serta pengalaman yang diperlukan untuk menjalankan pengelolaan sistem informasi dengan cara yang logis dan penuh analisis. 

3. Menyediakan kemampuan untuk menganalisis situasi guna mengurangi potensi kerugian yang berasal dari aspek ekonomi. 



4. Menyediakan kemudahan akses yang baik bagi semua penggunanya. 

5. Dapat membantu organisasi atau perusahaan mencapai sasarannya dengan lebih cepat, berkat adanya data pendukung yang terjamin kebenarannya.\[7\] 



B. Jenis-jenis Sistem Informasi 

Terdiri atas : 

**1. **Sistem Pemrosesan Transaksi \(TPS\) 

• TPS merupakan sistem informasi berbasis komputer yang dirancang untuk mengolah data dalam volume besar terkait transaksi bisnis harian, contohnya mencatat inventaris atau daftar gaji. 

• Fungsi utamanya berada di level operasional, memungkinkan organisasi berinteraksi dengan pihak di luar lingkungan kerjanya. 

• Data yang dihasilkan oleh TPS tersedia untuk digunakan atau dilihat oleh para manajer. 

**2. **Sistem Otomatisasi Perkantoran \(OAS\) & Sistem Kerja Pengetahuan \(KWS\) 

Kedua sistem ini beroperasi pada level pengetahuan \( *knowledge*\). 

• OAS berfungsi mendukung pekerja data, di mana tugasnya lebih banyak 

menganalisis 

dan 

memanipulasi 

informasi 

untuk 

mentransformasikannya, bukan menciptakan pengetahuan baru. 

• Aspek OAS mencakup penggunaan alat seperti pemrosesan kata \( *word* *processing*\), *spreadsheet*, penjadwalan elektronik, dan alat komunikasi \( *email*, *voice mail*\). 

• KWS bertugas mendukung para profesional \(seperti insinyur atau ilmuwan\) dengan membantu mereka menciptakan pengetahuan baru dan memungkinkannya dikontribusikan kepada organisasi atau masyarakat. 

**3. **Sistem Informasi Manajemen \(SIM\) 

• SIM tidak berfungsi sebagai pengganti TPS, melainkan mendukung jangkauan tugas organisasi yang lebih luas daripada TPS. 

• SIM berfokus pada analisis dan dukungan pengambilan keputusan. 



• Sistem ini menghasilkan informasi yang digunakan untuk dasar membuat keputusan, dan juga dapat membantu menyatukan beberapa fungsi informasi bisnis yang sudah terkomputerisasi \(seperti basis data\).\[8\] 

Dalam konteks proyek ini, sistem informasi CUR-HEART termasuk kategori Sistem Pemrosesan Transaksi \(TPS\) karena menangani transaksi pemesanan, pembayaran, dan dokumentasi sesi terapi, serta Sistem Informasi Manajemen \(MIS\) karena menyediakan pelaporan dan analitik untuk mendukung pengambilan keputusan manajerial. 



C. Manfaat Sistem Informasi 

Manfaat sistem informasi antara lain sebagai berikut ini : 1. Menyediakan kemudahan akses data yang disajikan secara akurat dan tepat waktu bagi pengguna, sehingga pengguna dapat mengaksesnya tanpa memerlukan pihak perantara. 

2. Memastikan ketersediaan mutu serta keahlian yang memadai dalam mengoperasikan sistem informasi dengan pendekatan yang kritis. 

3. Mendukung pengembangan proses perencanaan yang lebih efektif. 

4. Menentukan keahlian dan keterampilan apa saja yang dibutuhkan untuk mendukung operasional sistem informasi. 

5. Memungkinkan organisasi menetapkan investasi yang akan difokuskan pada pengembangan dan pemanfaatan sistem informasi. 

6. Mampu memprediksi dan menganalisis dampak atau konsekuensi finansial \(ekonomi\) yang mungkin timbul dari penerapan sistem informasi dan teknologi baru. 

7. Meningkatkan daya guna atau efisiensi dalam fase aplikasi, pengembangan, dan pemeliharaan sistem. 

8. Mampu mengolah transaksi, mengurangi biaya operasional, dan menghasilkan pendapatan sebagai produk atau layanan utama perusahaan.\[9\] 

****

****



**2.1.1. Sistem Informasi Manajemen** A. Pengertian Sistem Informasi Manajemen 

Manajemen yaitu menggabungkan sistematis dan kreatifitas dalam merealisasikan tugas-tugas yang telah ditetapkan, dengan mengandalkan pelaksanaan oleh pihak lain.\[10\] 

Manajemen adalah suatu proses rangkaian yang terdiri dari perencanaan, pengorganisasian, kepemimpinan dan pengendalian dalam pengunaan semua sumber daya yang dimiliki dalam mencapai tujuan yang telah ditentukan sesuai dengan target.\[10\] 

Sistem Informasi Manajemen yaitu susunan terstruktur dari berbagai komponen yang saling terkait, bekerja sama untuk menghasilkan data yang kemudian dimanfaatkan oleh pihak manajemen perusahaan.\[10\] 

Sistem Informasi Manajemen adalah suatu sistem yang yang digunakan untuk menyediakan informasi yang efektif dalam mendukung pengambilan keputusan kegiatan manajemen.\[11\] 

B. Komponen Sistem Informasi Manajemen Secara Fisik Komponen sistem informasi manajemen secara fisik yaitu seluruh perangkat dan peralatan fisik digunakan untuk mengoperasikan sistem informasi manajemen. Komponen terdiri atas : 

1. Perangkat Keras \( *Hardweare*\) : perangkat yang digunakan secara fisik seperti komputer dan alat yang dibutuhkan. 

2. Perangkat Lunak \( *Software*\) : serangkaian instruksi yang dapat memproses data ke perangkat keras. 

3. Basis Data * \(Database\) *: kumpulan-kumpulan hubungan tabel dan komponen lain, yang melakukan penyimpanan data-data. 

4. Prosedur pengoperasian : susunan aturan petunjuk untuk menggunakan sistem informasi berbasis komputer. 

5. Personalian pengoperasian \( *Brainware*\) : ahli komputer, manajer, pengguna, penganalisis, penyusun program, manajer basis data, dan jabatan yang berkaitan dengan memanfaatkan sistem informasi komputer. 

6. Komunikasi data dan jaringan komputer.\[12\] 





Sumber : Gede et al.,2022 

Gambar II. 1Komponen Sistem Informasi Manajemen 



C. Fungsi DBMS \( *Database Management System*\) Mengidentifikasikan terdiri dari beberapa fungsi DBMS yang digunakan dalam mengatur data dalam sistem antara lain : 

1. Manajemen penjagaan integritas data 

2. Diimplementasikan menjadi kamus data 

3. Menampilkan *interface* dalam komunikasi 4. Peralihan dan sajian data-data 

5. Keamanan data-data 

6. Bisa mengakses lebih dari satu pengguna \( *multi access*\) 7. Penyimpanan data-data \( *Data Storage Management*\) 8. Tersedia prosedur *Recovery* dan *Backup* 9. Menyediakan akses bahasa dan pemrograman dan manajemen.\[12\] 

* *

**2.1.2. Reservasi * *****Terapi **

A. Pengertian Reservasi Terapi 

Reservasi yaitu suatu permintaan pelanggan untuk mendapatkan fasilitas yang diinginkan sesuai dengan ketersediaan dengan tujuan pelanggan melakukan transaksi dengan aman.\[13\] 

Terapi realitas adalah sistem yang memfokuskan pada tingkah laku saat ini 



dan melakukan penerimaan serta tanggung jawab pribadi. Terapis mempunyai fungsi sebagai mediator yang mengonfrontasikan klien menggunakan cara yang bisa membantu klien bisa menghadapi masalah dan memenuhi kebutuhan tanpa merugikan dirinya sendiri dan orang lain.\[14\] 

Teknik yang digunakan dalam terapi realitas yaitu Teknik WDEP antara lain 

: 

**1. **W = *Wants* \(Keinginan\) dalam hal ini klien memberikan eksplorasi dalam segi kehidupan termasuk hal diinginkan. 

**2. **D = *Doing and Direction* \(Tindakan dan Arah\) hal ini mencakup empat komponen eksplorasi antara lain : tindakan, pikiran, perasaan dan fisiologi. 

**3. **E = *Evaluation *\(Evaluasi\) memberikan evaluasi pada klien. 

**4. **P = *Plannning* \(Rencana\) memberikan bantuan pada klien untuk tindakan rencana.\[15\] 

****

**2.1.3. Siklus Hidup Pengembangan Sistem \( *System Development Life ***

***Cycle/SDLC*****\) **

A. Pengertian SDLC 

*System Development Life Cycle* atau SDLC merupakan metode prose pembangunan sistem informasi.\[16\] Metode ini terdapat tahapan-tahapan yaitu : perencanaan, analisis, perancangan, implementasi, pengujian dan pemiliharaan. 

Metode SDLC biasanya digunakan di dalam sitem informasi seperti *Waterfall* dan *Prototype*. 

*System Development Life Cycle* \(SDLC\) adalah salah satu metode pengembangan sistem informasi yang terkenal pertama kali sistem informasi dikembangkan.\[17\] 

Tahapan yang terdapat pada SDLC yaitu : 

1. *Investigate *

2. *Analyze *

3. *Design *

4. *Implement *

5. *Maintainance\[18\] *





Sumber : Irpan et al.,2024 

Gambar II. 2 * * Pola Perputaran dari *Sistem Development Life Cycle* B. Metode Air Terjun \( *Waterfall*\) 

Waterfall adalah model pengembangan aplikasi yang masuk ke dalam *classic life cycle *\(siklus hidup klasik\), dimana metode ini menekankan pada fase berurutan dan sistematis. Pengembangan model ini dapat digambarkan seperti air terjun, karena setiap tahapnya dikerjakan secara berurutan mulai dari atas sampai ke bawah.\[19\] 

Metode *Waterfall* adalah metode pengembangan sistem yang tertata dan terstrukur yang setiap tahapan dilakukan secara bertahap dan tidak bisa dilanjutkan sampai setiap tahapan sebelumnya selesai.\[20\] 



Sumber : Fachri B et al.,2024 

Gambar II. 3 Metode *Waterfall* 



- Tahapan Metode Air Terjun \( *Waterfall\) *: 1. Perencanaan Konsep \( *Requirements Analysis*\) : Tahapan ini dilakukan analisis untuk melakukan pemahaman kebutuhan dan permintaan yang tepat dari pelanggan dan pengumpulan data dapat dilakukan dengan wawancara langsung kepada yang mempunyai kepentingan. Setelah itu mendapatkan hasil analisis kebutuhan sistem yang berkaitan dengan persyaratan perangkat lunak dan sesuai spesifikasi kebutuhan dalam sistem baik dokumentasi sesuai kualifikasi kebutuhan pengembangan perangkat lunak. 

2. Pemodelan Sistem \( *System Design*\) : 

Tahapan ini merupakan analisis kebutuhan sistem yang sebelumnya sudah dibuat namun dituangkan menjadi sebuah desai sistem yang selanjutnya dilakukan proses pengkodean. 

3. Implementasi \( *Implementation*\) : 

Tahapan ini melakukan proses coding atau pengkodean untuk menerjemahkan desain sistem menjadi aplikasi. 

4. Pengujian \( *Testing*\) : 

Sistem yang sudah selesai dibuat selanjutnya akan diuji untuk melihat keberhasilan sistem, menentukan kinerja dan optimasi apakah sudah sesuai dengan kebutuhan. 

5. Pemeliharaan \( *Maintenance*\) : 

Tahap ini dilakukan untuk melakukan pemeliharaan sistem apabila menemukan *error* atau *bug*.\[21\] 

- Kelebihan Model Air Terjun \( *Waterfall*\) : 1. Persyaratan harus sudah ditentukan semua di awal, sebelum melakukan pembuatan program. 

2. Sistem ini bagus karena mempunyai cara kerja yang teratur sehingga kualitas perangkat lunak akan terjaga. 

3. Urutan kerja yang jelas dan masuk akal sehingga dapat membantu menghindari kesalahan yang besar sejak perancangan awal dibuat. 

4. Jumlah total proyek bisa diperkirakan dengan akurasi tepat, apabila tidak ada masalah. 



5. Proses ini menentukan dengan pasti kapan pekerjaan dimulai dan kapan pekerjaan selesai\[22\] 

- Kekurangan Model Air Terjun \( *Waterfall*\): 1. Tidak bisa melakukan perubahan ditengah kondisi jalannya proyek 2. Jika terjadi perubahan yang diperlukan maka proyek harus diinisiasi dari tahap awal. Dalam hal ini dapat menimbulkan tambahan biaya anggaran bagi organisasi 

3. Kualitas dapat dinilai eksklusif oleh pengguna secara langsung pada tahap akhir 

4. Produk yang dihasilkan tidak cepat selesai harus menunggu sampai tahapan selesai 

5. Mempunyai resiko yang besar apabila project tertunda peluncuran karena bisa mempengaruhi kebutuhan klien yang bisa berubah\[22\] 



Dalam proyek sistem informasi CUR-HEART ini, model Air Terjun dipilih karena : 

a. Persyaratan sudah cukup jelas dan stabil berdasarkan analisis proses bisnis yang ada 

b. Cakupan proyek terdefinisi dengan baik dan tidak diharapkan ada perubahan signifikan 

c. Proyek memiliki garis waktu yang tetap \(semester akademik\) d. Dokumentasi lengkap diperlukan untuk keperluan akademik \(Proyek Akhir/ *Capstone Project*\) 

e. Tim pengembang relatif kecil dan terstruktur 



C. Model SDLC Lainnya \( *Comparison*\) 

Selain Waterfall, terdapat beberapa model SDLC lain yang populer seperti *Agile*, Spiral, V-Model, RAD, dan, DevOps. Namun, model *Waterfall* dipilih untuk proyek CUR-HEART** **dengan pertimbangan berikut: 1. Persyaratan Jelas dan Stabil** **: Kebutuhan sistem sudah teridentifikasi dengan baik melalui analisis bisnis CUR-HEART 



2. Garis Waktu Tetap : Proyek dibatasi waktu semester akademik \(11 minggu\) sehingga memerlukan perencanaan yang terukur 

3. Dokumentasi Lengkap : Kebutuhan akademik memerlukan dokumentasi komprehensif di setiap fase 

4. Tim Kecil dan Terstruktur : Pengembangan dilakukan oleh tim kecil dengan struktur jelas, cocok dengan model sekuensial 

5. Skala Proyek Sesuai : Sistem dengan kompleksitas menengah yang tidak memerlukan iterasi *sprint* berulang 



## **2.1.4. Hipnoterapi dan Kesehatan Mental **

A. Pengertian Hipnoterapi 

Hipnoterapi \( *hypnotherapy*\) adalah bentuk psikoterapi komplementer yang menggunakan teknik hipnosis untuk membantu individu relaksasi yang mendalam untuk mencapai perubahan positif dalam pikiran, perasaan, dan perilaku. Dalam keadaan ini, klien menjadi lebih terbuka terhadap saran yang diberikan oleh terapis. Hal ini memungkinkan akses ke pikiran bawah sadar di mana kepercayaan, kenangan, dan emosi disimpan. Hipnoterapi fokus pada modifikasi dan pemahaman perilaku emosi yang berasal dari pikiran bawah sadar yang biasanya menjadi akar dari berbagai gangguan psikologis pola pikir, trauma, kecemasan, fobia dan kebiasan yang negatif.\[23\] 



B. Efektivitas Hipnoterapi 

Berbagai penelitian ilmiah telah membuktikan efektivitas hipnoterapi dalam menangani berbagai kondisi psikologis : 

• Kirsch et al. \(1995\) dalam meta-analisis terhadap 18 studi menemukan bahwa terapi kognitif-perilaku dikombinasikan dengan hipnosis memiliki ukuran efek yang lebih besar \(d=0.87\) dibandingkan terapi kognitif-perilaku tanpa hipnosis \(d=0.51\). 

• Montgomery et al. \(2002\) dalam meta-analisis terhadap 20 uji terkontrol menemukan bahwa analgesia hipnotik secara signifikan lebih efektif daripada tanpa perawatan, perawatan medis standar, dan kontrol perhatian untuk mengurangi rasa sakit. 



**4. **Aplikasi Klinis : 

• Gangguan Kecemasan \( *Anxiety Disorders*\) : Hipnoterapi terbukti efektif mengurangi gejala pada gangguan kecemasan umum dan gangguan panik \(Schoenberger, 2000\). 

• Trauma dan PTSD : Hipnoterapi dapat membantu memproses kenangan traumatis dan mengurangi gejala PTSD \(Lynn et al., 2012\). 

• Gangguan Tidur \( *Sleep Disorders*\) : Hipnoterapi efektif untuk menangani insomnia dan meningkatkan kualitas tidur \(Ng & Lee, 2008\). 

• Penghentian Kebiasaan \( *Habit Cessation*\) : Hipnoterapi menunjukkan tingkat keberhasilan yang tinggi untuk penghentian merokok dan manajemen berat badan \(Green & Lynn, 2017\). 



C. Kesehatan Mental di Indonesia 

Menurut Riset Kesehatan Dasar \(Riskesdas\) Kementerian Kesehatan RI tahun 2023, prevalensi gangguan mental emosional \(yang ditunjukkan dengan gejala-gejala depresi dan kecemasan\) di Indonesia mencapai 9.8% untuk usia 15 tahun ke atas, atau sekitar 19 juta penduduk. Angka ini meningkat dari tahun 2018 yang mencatat 6.1%. 

- Faktor-faktor yang Mempengaruhi : 

• Urbanisasi dan tekanan hidup di kota besar 

• Stres ekonomi dan ketidakamanan pekerjaan 

• Media sosial dan kecanduan digital 

• Pandemi COVID-19 dan dampak psikososialnya 

• Stigma sosial yang masih kuat terhadap penyakit mental 

- Tantangan dalam Layanan Kesehatan Mental : 

• Rasio psikiater dan psikolog yang sangat rendah \(1:200.000 dibanding standar WHO 1:100.000\) 

• Distribusi tenaga kesehatan mental yang tidak merata \(terkonsentrasi di kota besar\) 

• Biaya layanan yang relatif tinggi dan tidak terjangkau untuk sebagian besar masyarakat 

• Stigma sosial yang menyebabkan pelaporan rendah dan penghindaran 



perawatan 

• Kurangnya kesadaran dan literasi kesehatan tentang kesehatan mental 

- Peluang Layanan Kesehatan Mental Digital : 

• Meningkatnya kesadaran masyarakat terutama generasi milenial dan Z 

tentang pentingnya kesehatan mental 

• Penetrasi internet dan ponsel pintar yang tinggi \(75% populasi\) 

• Penerimaan terhadap konsultasi daring dan *telehealth* 

• Inisiatif pemerintah seperti Program Indonesia Sehat Jiwa 

• Pertumbuhan industri kesejahteraan dan pengembangan diri **2.1.5. Kerangka Kerja Laravel \( *Laravel Framework*****\)** A. Pengertian Laravel dan Perbandingan Kerangka Kerja PHP 

Laravel adalah kerangka kerja PHP sumber terbuka \( *open-source*\) yang dirancang untuk mempermudah dan mempercepat pengembangan aplikasi *web* dengan sintaksis yang elegan dan ekspresif \(Otwell, 2021\). Laravel mengikuti arsitektur *Model-View-Controller* \(MVC\) yang memisahkan logika bisnis dari logika presentasi, sehingga kode menjadi lebih terorganisir, mudah dipelihara, dan dapat diskalakan. 

Mengapa TIDAK Kerangka Kerja Lain : 

• *Symfony* : Terlalu kompleks untuk tenggat 11 minggu, kurva belajar lebih curam, lebih banyak boilerplate 

• *CodeIgniter *: Kurang fitur modern \(autentikasi bawaan, relasi ORM\), ekosistem lebih kecil 

• *Slim/Lumen* : Kerangka kerja mikro - perlu membangun terlalu banyak dari awal \(autentikasi, tampilan, dll.\) 

• *Yii/CakePHP/Phalcon* : Komunitas lebih kecil, lebih sulit mencari bantuan, lebih sedikit paket 

Kesimpulan : Laravel dipilih karena keseimbangan sempurna antara fitur, kemudahan penggunaan, dan kecepatan pengembangan untuk skala proyek CURHEART. 





Menurut dokumentasi resmi Laravel \(Laravel Documentation, 2023\), Laravel menyediakan ekosistem yang lengkap untuk pengembangan web full-stack, termasuk : 

• *Eloquent* ORM : Pemetaan Relasi-Objek \( *Object-Relational Mapping*\) yang andal untuk interaksi basis data 

• Mesin Templat *Blade* \( *Blade Templating Engine*\) : Mesin templat yang sederhana namun andal untuk lapisan tampilan 

• Artisan CLI : Perangkat baris perintah \( *command-line tool*\) untuk otomasi tugas dan pembuatan kode 

• Migrasi & Pembenihan \( *Migration* & *Seeding*\) : Kontrol versi basis data dan pembuatan data sampel 

• Autentikasi & Otorisasi \( *Authentication* & *Authorization*\) : Sistem bawaan untuk manajemen pengguna 

• Antrean & Pekerjaan \( *Queue* & *Job*\) : Pemrosesan pekerjaan latar belakang untuk tugas yang memakan waktu 

• Peristiwa & Pendengar \( *Events* & *Listeners*\) : Arsitektur berbasis peristiwa untuk penggandengan longgar 

• Pengujian \( *Testing*\) : Dukungan bawaan untuk pengujian unit dan pengujian fitur 

• Pengembangan API : Perangkat untuk membangun API RESTful dengan mudah 



B. Arsitektur MVC Laravel 

*Model-View-Controller* \(MVC\) adalah pola arsitektur perangkat lunak yang memisahkan aplikasi menjadi tiga komponen utama \(Leff & Rayfield, 2001\): 1. Model : 

• Merepresentasikan data dan logika bisnis 

• Berinteraksi dengan basis data melalui *Eloquent * ORM 

• Mendefinisikan relasi antar entitas \(satu-ke-satu, satu-ke-banyak, banyak-ke-banyak\) 

• Melakukan validasi data dan penegakan aturan bisnis 

• Independen dari antarmuka pengguna 



- Contoh di sistem CUR-HEART: 

• Model *User* \(klien, terapis, admin\) 

• Model *Booking* 

• Model *Service *

• Model *Session *

• Model *Payment *

2. *View* \(Tampilan\) : 

• Menyajikan data kepada pengguna dalam format yang sesuai 

• Menggunakan mesin templat Blade di Laravel 

• Menerima data dari *Controller* dan menampilkannya 

• Tidak berisi logika bisnis, hanya logika presentasi 

• Antarmuka responsif dan ramah pengguna 

- Contoh di sistem CUR-HEART : 

• Tampilan halaman arahan \( *landing page*\) 

• Tampilan formulir pemesanan 

• Tampilan dasbor \(klien, terapis, admin\) 

• Tampilan laporan 

3. *Controller* \(Pengontrol\) : 

• Bertindak sebagai perantara antara Model dan View 

• Menerima masukan dari pengguna \(permintaan HTTP\) 

• Memanggil Model untuk mengambil atau memanipulasi data 

• Memilih View yang sesuai untuk menampilkan respons 

• Berisi logika alur aplikasi 

- Contoh di sistem CUR-HEART: 

• *Booking Controller* \(menangani operasi pemesanan\) 

• *User Controller* \(menangani manajemen pengguna\) 

• *Payment Controller* \(menangani pembayaran\) 

• *Dashboard Controller* \(menangani data dasbor\) C. *Eloquent* ORM 

*Eloquent *

adalah 

Pemetaan 

Relasi-Objek 

\( *Object-Relational *

*Mapping*/ORM\) yang disediakan Laravel untuk interaksi basis data \(Otwell, 



2021\). ORM adalah teknik pemrograman yang memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan paradigma berorientasi objek, tanpa harus menulis kueri SQL mentah. 

- Keuntungan Eloquent ORM: 

1. *Implementasi Active Record* : Setiap kelas model merepresentasikan satu tabel di basis data. Instans dari kelas model merepresentasikan satu baris dalam tabel tersebut. 

2. *Sintaksis Ekspresif* : Kueri dapat ditulis dengan sintaksis yang bersih dan mudah dibaca. 

3. Manajemen Relasi : *Eloquent* mempermudah pendefinisian dan bekerja dengan relasi: 

• Satu-ke-Satu \( *One-to-One: hasOne, belongsTo*\) 

• Satu-ke-Banyak \( *One-to-Many: hasMany, belongsTo*\) 

• Banyak-ke-Banyak \( *Many-to-Many: belongsToMany*\) 

• *Has-Many-Through *

• Relasi Polimorfik \( *Polymorphic Relations*\) 4. Pembangun Kueri \( *Query Builder*\): Pembangun kueri yang andal dengan method chaining untuk kueri kompleks : 

• where\(\), orWhere\(\) 

• orderBy\(\), groupBy\(\) 

• join\(\), leftJoin\(\) 

• select\(\), selectRaw\(\) 



**2.2. **

## **Tailwind CSS **

A. Pengertian Tailwind CSS dan Perbandingan Kerangka Kerja CSS 

Tailwind CSS adalah kerangka kerja CSS utilitas-pertama \(utility-first\) yang menyediakan kelas utilitas tingkat rendah untuk membangun desain khusus tanpa harus meninggalkan HTML \(Tailwind CSS Documentation, 2023\). Berbeda dengan kerangka kerja CSS tradisional seperti Bootstrap yang menyediakan komponen pra-desain, Tailwind menyediakan kelas utilitas yang dapat dikombinasikan untuk membuat desain apa pun. 

Tailwind CSS adalah framework CSS utility-first yang dipilih karena : 



• ***Customization***** tinggi **: *Config file* untuk brand *colors CUR-HEART* 

• ***File size***** kecil **: PurgeCSS menghasilkan 8KB \(vs Bootstrap 25KB\) 

• ***Mobile-first responsive***** **: *Built-in breakpoints* \(sm, md, lg, xl, 2xl\) 

• **Konsistensi desain **: *Predefined scale* untuk *spacing, colors, shadows* 

• **Maintainability **: *Style co-located* dengan HTML 

Kombinasi Laravel \+ Tailwind CSS mendukung pengembangan efisien dengan *hot-reload* dan *build optimization*. 



**2.1.5. Keamanan Web \( *Web Security*****\)** A. Autentikasi \( *Authentication*\) 

Autentikasi adalah proses memverifikasi identitas pengguna, perangkat, atau sistem \(OWASP, 2021\). Dalam aplikasi web, autentikasi memastikan bahwa pengguna adalah siapa yang mereka klaim sebelum memberikan akses ke sumber daya. 

- Metode Autentikasi : 

1. Autentikasi Berbasis Kata Sandi \(Password-Based Authentication\) : 

• Nama pengguna dan kata sandi 

• Metode paling umum 

• Memerlukan penyimpanan kata sandi yang aman \(hashing\) 

• Rentan jika kata sandi lemah atau digunakan ulang 2. Autentikasi Multi-Faktor \(Multi-Factor Authentication/MFA\) : Menggabungkan beberapa metode autentikasi: 

• Sesuatu yang Anda tahu \(kata sandi\) 

• Sesuatu yang Anda miliki \(ponsel, token\) 

• Sesuatu yang Anda adalah \(biometrik\) 

• Meningkatkan keamanan secara signifikan 

3. Autentikasi Berbasis *Token* \( *Token-Based Authentication*\) : 

• Pengguna menerima token setelah login 

• Token disertakan dalam permintaan berikutnya 

4. Autentikasi Berbasis Sesi \( *Session-Based Authentication*\): 

• Server membuat sesi setelah login 

• ID sesi disimpan di cookie 



• Server memvalidasi sesi pada setiap permintaan 5. Autentikasi Laravel : 

- Laravel menyediakan sistem autentikasi yang kuat secara bawaan: 

• Pendaftaran Pengguna: Pendaftaran bawaan dengan validasi 

• Login/Logout: Autentikasi berbasis sesi 

• Hashing Kata Sandi: Otomatis dengan Bcrypt 

• Pengaturan Ulang Kata Sandi: Alur pengaturan ulang kata sandi berbasis surel 

• Ingat Saya \(Remember Me\): Login persisten dengan token aman 

• Verifikasi Surel: Memverifikasi alamat surel pengguna 

• Middleware: Perlindungan rute dengan middleware auth B. Otorisasi \( *Authorization*\) 

Otorisasi adalah proses menentukan izin atau hak istimewa apa yang dimiliki pengguna yang telah diautentikasi \(OWASP, 2021\). Setelah pengguna diautentikasi, otorisasi menentukan sumber daya apa yang dapat mereka akses dan tindakan apa yang dapat mereka lakukan. 



## **2.2. Penelitian Terkait **

Beberapa penelitian terkait yang relevan dengan pengembangan sistem informasi manajemen booking dan terapi telah dilakukan sebelumnya. Penelitian-penelitian ini menjadi referensi dan landasan untuk identifikasi gap serta differentiation dari proyek CUR-HEART. 

**Posisi Penelitian:** CUR-HEART adalah ***solusi komprehensif, domain-specific, ***

***user-centered*** untuk manajemen hipnoterapi, mengintegrasikan *best practices* dari penelitian *existing * dengan fitur inovatif yang mengatasi kebutuhan klinis dan bisnis spesifik. 





****

****

****





**BAB III **

## **METODOLOGI PENELITIAN **



## **3.1. Tahapan Penelitan **

Penelitian dan pengembangan sistem informasi manajemen pemesanan dan terapi CUR-HEART menggunakan pendekatan ***System Development Life ***

***Cycle***** \(SDLC\)** dengan model ***Waterfall***. Model ini dipilih karena karakteristik proyek yang memiliki kebutuhan jelas, waktu yang tetap \(semester akademik\), dan memerlukan dokumentasi yang komprehensif untuk keperluan akademik. Tahapan penelitian terdiri dari lima fase utama yang dilaksanakan secara berurutan dengan keluaran yang terdefinisi jelas di setiap fase. 



Inisiasi 

****

Proyek 





Perencanaan 



Proyek 





Pelaksanaan 



Proyek 





Pemantauan & 



Pengendalian Proyek 





****

Penutupan 



Proyek 

****





Gambar III. 1 Tahapan Penelitian 





Uraian tahapan penelitian sebagai berikut : **1. Inisiasi Proyek** 

Tahapan ini dimulai dengan mengidentifikasi permasalahan yang dihadapi CUR-HEART dalam manajemen pemesanan dan terapi, menentukan tujuan proyek, mengidentifikasi pemangku kepentingan, serta menyusun *project charter* sebagai dokumen otorisasi formal untuk memulai proyek. 

## **2. Perencanaan Proyek**

Tahapan perencanaan mencakup penyusunan ruang lingkup proyek \( *scope*\), penjadwalan waktu pengerjaan \( *timeline*\), estimasi anggaran biaya, perencanaan kualitas, identifikasi sumber daya yang dibutuhkan, analisis risiko, perencanaan komunikasi, dan strategi pengadaan \( *procurement*\). 

## **3. Pelaksanaan Proyek**

Tahapan pelaksanaan merupakan fase inti pengembangan sistem yang terdiri dari : 

• Analisis kebutuhan sistem melalui observasi, wawancara, dan studi dokumentasi 

• Perancangan sistem meliputi desain basis data, desain antarmuka pengguna, dan diagram UML 

• Implementasi sistem menggunakan *framework Laravel* dengan bahasa pemrograman PHP 

• Pengujian sistem secara menyeluruh untuk memastikan kualitas dan kesesuaian dengan kebutuhan 

• *Deployment * sistem ke lingkungan produksi **4. Pemantauan dan Pengendalian Proyek** 

Tahapan ini dilakukan paralel dengan pelaksanaan proyek untuk memastikan proyek berjalan sesuai rencana. Aktivitas meliputi pemantauan progres pengerjaan, pengendalian perubahan ruang lingkup, pengendalian kualitas *deliverables*, dan pengelolaan risiko yang muncul selama pengerjaan. 

## **5. Penutupan Proyek**

Tahapan akhir mencakup serah terima sistem \( *handover*\) kepada klien, penyusunan dokumentasi lengkap \(manual pengguna, dokumentasi teknis\), 



evaluasi pencapaian tujuan proyek, *lessons learned*, dan pelepasan sumber daya tim proyek. 



**3.2. Tempat dan Waktu Penelitian **

## **3.2.1. Tempat Penelitian **

Penelitian dan pengembangan sistem informasi ini dilaksanakan di beberapa lokasi sebagai berikut : 

**1. CUR-HEART \( *Hypnotherapy & Mind Wellness Center*****\) **

• Alamat : Jl. Raya Cilodong No. 88, Depok, Jawa Barat 

• Kegiatan : Observasi proses bisnis, wawancara dengan pemangku kepentingan, dan pengujian penerimaan pengguna \( *User Acceptance* *Testing*\) 

**2. Universitas Nusa Mandiri - Kampus Margonda **

• Alamat : Jl. Margonda Raya No. 100, Pondok Cina, Depok, Jawa Barat 

• Kegiatan : Pengembangan sistem, konsultasi dengan dosen pembimbing, dan koordinasi tim proyek 

**3. Secara Daring \( *Remote/Online*****\)** 

• Kegiatan: Pengembangan sistem, dokumentasi, pengujian, dan koordinasi tim melalui platform kolaborasi daring 

## **3.2.2. Waktu Penelitian **

Penelitian ini dilaksanakan selama satu semester akademik dengan rentang waktu sebagai berikut : 

**Tabel III.1 **

**Jadwal Penelitan **

**No **

**Kegiatan **

## **Waktu Pelaksanaan **

### Inisiasi dan Analisis 

1 

Minggu 1-2 \(16-29 September 2025\) 

Kebutuhan 

Minggu 3-4 \(30 September - 13 

2 

Perancangan Sistem 

Oktober 2025\) 



**No **

**Kegiatan **

## **Waktu Pelaksanaan **

Minggu 5-8 \(14 Oktober - 10 

3 

Implementasi Sistem 

November 2025\) 

4 

Pengujian Sistem 

Minggu 9-10 \(11-24 November 2025\) 

Minggu 11 \(25 November - 1 

5 

Deployment dan Evaluasi 

Desember 2025\) 

6 

Penyusunan Laporan 

Minggu 12-15 \(2-29 Desember 2025\) 

**Total durasi penelitian adalah 15 minggu \(16 September - 29 Desember 2025\)** **3.3. Subjek Penelitian **

Subjek penelitian dalam pengembangan sistem informasi CUR-HEART terdiri dari pemangku kepentingan yang terlibat langsung dalam penggunaan sistem. 

Penelitian ini menggunakan metode *sampling purposive \(non-probabilitas\)* dimana partisipan dipilih berdasarkan kriteria tertentu yang relevan dengan tujuan penelitian. 

## **3.3.1. Populasi **

Populasi dalam penelitian ini adalah seluruh pengguna potensial sistem informasi CUR-HEART yang terdiri dari : 

• 

Pemilik dan manajemen CUR-HEART 

• 

Terapis yang bekerja di CUR-HEART 

• 

Staf administrasi dan *customer service* 

• 

Klien yang menggunakan layanan terapi CUR-HEART 

• 

Calon klien potensial yang membutuhkan layanan terapi kesehatan mental **3.3.2. Sampel dan Teknik Pengambilan Sampel **

Penelitian ini menggunakan teknik ***purposive***** sampling** \(pengambilan sampel bertujuan\) dimana sampel dipilih secara sengaja berdasarkan karakteristik dan kriteria tertentu yang sesuai dengan kebutuhan penelitian. 



**Tabel III.2 **

**Distribusi Sampel Penelitian** 

**Kriteria **

**Peran dalam **

**No **

**Kategori Sampel **

**Jumlah **

**Pemilihan **

## **Penelitian **

### Memberikan 

Pengambil 

kebutuhan 

Pemilik/ 

keputusan, 

1 

1 orang 

bisnis, 

Manajemen 

memahami visi 

validasi 

bisnis 

sistem 

Memberikan 

Berpengalaman 

kebutuhan 

minimal 1 

2 

Terapis 

3 orang 

fungsional, 

tahun, pengguna pengujian 

aktif sistem 

sistem 

Mengelola 

Memberikan 

pemesanan dan 

proses bisnis 

3 

Staf Admin/CS 

2 orang 

administrasi 

existing, 

harian 

pengujian 

Pernah 

Memberikan 

menggunakan 

feedback 

4 

Klien Aktif 

5 orang 

layanan 

kebutuhan 

minimal 2 kali 

klien, UAT 

Pengujian 

Berminat 

usability dari 

5 

Calon Klien 

3 orang 

menggunakan 

perspektif 

layanan terapi 

user baru 

**Total** 

## **14 orang**

Teknik 

pengambilan 

sampel 

menggunakan ***purposive ***

***sampling*** dengan 

pertimbangan : 

• Sampel dipilih berdasarkan pengetahuan dan pengalaman mereka terhadap proses bisnis CUR-HEART 

• Mewakili berbagai peran pengguna dalam sistem \(admin, terapis, klien\) 

• Dapat memberikan informasi yang mendalam dan relevan untuk pengembangan sistem 

• Bersedia berpartisipasi dalam wawancara, observasi, dan pengujian sistem **3.4. Teknik Pengumpulan Data **

Pengumpulan data dalam penelitian ini menggunakan pendekatan multi-metode untuk memastikan pemahaman yang komprehensif terhadap kebutuhan sistem dan validasi dari berbagai perspektif. Teknik pengumpulan data yang digunakan meliputi observasi, wawancara, studi pustaka, dan kuesioner. 

## **3.4.1. Observasi **

Observasi dilakukan untuk memahami proses bisnis aktual yang berjalan di CUR-HEART dan mengidentifikasi permasalahan yang terjadi dalam operasional sehari-hari. Observasi dilakukan secara langsung di lokasi CUR-HEART dengan mengamati: 

• Proses pemesanan layanan terapi melalui *WhatsApp* dan telepon 

• Proses penjadwalan terapis dan manajemen waktu 

• Interaksi antara staf administrasi dengan klien 

• Proses pencatatan data klien dan dokumentasi sesi terapi 

• Proses pembayaran dan pembuatan laporan 

Hasil observasi didokumentasikan dalam catatan lapangan \( *field notes*\) dan digunakan sebagai dasar untuk menyusun diagram proses bisnis \( *as-is process*\) yang menggambarkan kondisi sebelum implementasi sistem. 

## **3.4.2. Wawancara **

Wawancara semi-terstruktur dilakukan untuk mendapatkan informasi mendalam dari pemangku kepentingan mengenai kebutuhan, harapan, dan kendala yang dihadapi dalam sistem yang sedang berjalan. Wawancara dilakukan kepada : 

****

****



**Tabel III.3 **

**Daftar Narasumber Wawancara** 

**No **

**Narasumber **

**Jumlah **

## **Tujuan Wawancara **

### Pemilik CUR-

Memahami visi bisnis, target, dan 

1 

1 orang 

HEART 

ekspektasi terhadap sistem 

Mengidentifikasi kebutuhan untuk 

2 

Terapis 

3 orang 

manajemen jadwal dan dokumentasi 

sesi terapi 

Memahami proses pemesanan, 

3 

Staf Admin/CS 

2 orang 

pembayaran, dan administrasi 

Menggali pengalaman pemesanan dan 

4 

Klien 

5 orang 

ekspektasi terhadap sistem online 



Wawancara dilakukan dengan durasi 30-60 menit per narasumber dan didokumentasikan dalam bentuk transkrip wawancara. Hasil wawancara dianalisis untuk mengidentifikasi kebutuhan fungsional dan non-fungsional sistem. 

## **3.4.3. Studi Pustaka **

Studi pustaka dilakukan untuk membangun landasan teoritis dan memahami *best practice* dalam pengembangan sistem informasi sejenis. Sumber pustaka yang digunakan meliputi : 

• Jurnal ilmiah tentang sistem informasi manajemen pelayanan kesehatan 

• Buku referensi tentang rekayasa perangkat lunak dan manajemen proyek 

• Dokumentasi teknis *framework Laravel* dan teknologi terkait 

• Penelitian terdahulu tentang sistem pemesanan dan manajemen terapi 

• Standar dan regulasi terkait keamanan data kesehatan Studi pustaka menghasilkan tinjauan literatur yang disajikan dalam BAB II dan menjadi dasar dalam perancangan dan pengembangan sistem. 





**3.4.4. Kuesioner **

Kuesioner digunakan untuk mengumpulkan data kuantitatif dari sampel yang lebih luas dan mengukur tingkat kepuasan serta kegunaan sistem. Kuesioner dibagikan dalam dua tahap: 

## **1. Kuesioner Analisis Kebutuhan**

• Diberikan kepada calon pengguna sistem \(20 responden\) 

• Bertujuan mengidentifikasi fitur yang dibutuhkan dan prioritasnya 

• Mengukur kesiapan pengguna terhadap sistem digital **2. Kuesioner Evaluasi Sistem \( *System Usability Scale*****/SUS\)** 

• Diberikan kepada partisipan pengujian setelah menggunakan sistem \(14 

responden\) 

• Mengukur tingkat kegunaan sistem dengan metode SUS 

• Mengidentifikasi area perbaikan untuk pengembangan selanjutnya Hasil kuesioner dianalisis secara deskriptif dan statistik untuk mendukung pengambilan keputusan dalam pengembangan sistem. 





**BAB IV **

## **HASIL PENELITIAN DAN PEMBAHASAN **



## **4.1. INISIASI PROYEK **

Proyek pengembangan Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART diinisiasi berdasarkan kebutuhan untuk mengoptimalkan operasional pusat layanan hipnoterapi dan kesehatan mental. CUR-HEART \( *Hypnotherapy &* *Mind Wellness Center*\) mengalami pertumbuhan signifikan dalam jumlah klien dan terapis, namun sistem manual yang digunakan menghambat efisiensi dan kualitas layanan. 

## **4.1.1. Latar Belakang Masalah **

Berdasarkan observasi dan wawancara yang dilakukan pada September 2025, teridentifikasi beberapa permasalahan utama : 1. **Proses pemesanan manual** melalui WhatsApp dan telepon yang memakan waktu lama dan mengurangi tingkat konversi \(hanya 60% dari pertanyaan menjadi pemesanan aktual\) 

2. **Konflik jadwal dan pemesanan ganda** terjadi 8-10 kasus per bulan karena manajemen jadwal menggunakan spreadsheet terpisah 

3. **Dokumentasi terapi tidak terstruktur** dimana terapis menghabiskan 15 

menit per sesi untuk pencatatan manual dengan risiko data hilang 4. **Tidak ada data untuk pengambilan keputusan** karena informasi tersebar di berbagai platform dan pembuatan laporan memakan waktu 2-3 hari 5. **Beban administratif tinggi** dengan admin menghabiskan 70% waktu untuk tugas repetitif seperti menjawab pertanyaan yang sama dan verifikasi pembayaran manual 

6. **Risiko keamanan dan privasi data** klien yang sensitif disimpan dalam format tidak aman tanpa kontrol akses yang tepat 

## **4.1.2. Identifikasi Masalah **

Berdasarkan latar belakang di atas, penulis mengidentifikasikan beberapa masalah sebagai berikut : 

a. Pelayanan pemesanan terapi masih dilaksanakan secara konvensional sehingga kurang efektif dan efisien 



b. Belum adanya sistem informasi pemesanan berbasis web untuk pemesanan dan manajemen terapi 

c. Banyak terjadi kehilangan data klien karena belum adanya sistem informasi yang dapat mendata siapa saja klien yang sedang melakukan pemesanan dan mengikuti sesi terapi 

## **4.1.3. Ruang Lingkup **

Ruang lingkup proyek ini mencakup pengembangan sistem informasi berbasis web dengan fitur-fitur utama : 

• **Modul Pemesanan Online **: Klien dapat melihat jadwal terapis, memilih layanan, dan melakukan pemesanan secara mandiri 24/7 

• **Manajemen Jadwal Terapis **: Sistem penjadwalan otomatis dengan deteksi konflik dan notifikasi 

• **Dokumentasi Sesi Terapi **: Platform digital untuk terapis mencatat dan mengakses riwayat terapi klien 

• **Pembayaran Terintegrasi **: Integrasi dengan *payment gateway* Midtrans untuk pembayaran online 

• **Dashboard Admin **: Panel kontrol untuk pemantauan pemesanan, terapis, dan laporan keuangan 

• **Notifikasi Otomatis **: Pengingat email untuk klien dan terapis tentang jadwal sesi 

## **4.1.4. Tujuan dan Manfaat Penelitian **

**Tujuan penelitian dalam *capstone project***** ini adalah:** a. Agar pelayanan pemesanan terapi dapat berjalan dengan efektif dan efisien 

b. Sistem informasi pemesanan diharapkan dapat memudahkan klien dalam melakukan pemesanan dan melihat riwayat terapi c. Dengan adanya sistem informasi dapat memudahkan baik klien, petugas admin, maupun terapis dalam pengelolaan data pemesanan dan sesi terapi, sehingga semuanya dapat terkontrol dengan baik d. Sebagai salah satu syarat kelulusan pada Program Studi Strata Satu \(S1\) untuk Program Studi Sistem Informasi di Fakultas Teknologi Informasi Universitas Nusa Mandiri 



**Manfaat penelitian :** 

Penelitian ini diharapkan memberikan manfaat bagi berbagai pihak : 

• **Bagi CUR-HEART **: Meningkatkan efisiensi operasional, mengurangi kesalahan jadwal, dan mempercepat pertumbuhan bisnis 

• **Bagi Klien **: Kemudahan dalam pemesanan layanan terapi kapan saja tanpa harus menghubungi admin 

• **Bagi Terapis **: Mengurangi beban administratif dan memudahkan akses riwayat klien 

• **Bagi Admin **: Otomasi tugas repetitif sehingga dapat fokus pada layanan pelanggan yang lebih berkualitas 

• **Bagi Akademik **: Sebagai referensi pengembangan sistem informasi sejenis untuk layanan kesehatan mental 



## **4.2. PERENCANAAN PROYEK **

Perencanaan proyek dilakukan untuk memastikan proyek berjalan sesuai target waktu, biaya, dan kualitas yang ditetapkan. Perencanaan mencakup berbagai area pengetahuan manajemen proyek yang telah diidentifikasi mencakup ruang lingkup \( *scope*\), waktu \( *time*\), biaya \( *cost*\), kualitas \( *quality*\), sumber daya \( *resource*\), risiko \( *risk*\), komunikasi \( *communication*\), pengadaan \( *procurement*\), integrasi \( *integration*\), serta manajemen pemangku kepentingan \( *stakeholder*\). 

**4.2.1. Perencanaan Ruang Lingkup \( *Scope*****\)** Ruang lingkup proyek didefinisikan menggunakan *Work Breakdown* *Structure* \(WBS\) yang membagi pekerjaan menjadi komponen-komponen yang dapat dikelola. WBS proyek ini mencakup 6 fase utama dengan total lebih dari 40 *work packages* yang terdistribusi ke dalam aktivitas-aktivitas terstruktur. 

****

****

****

****

****

****



**Tabel IV.1 **

***Work Breakdown Structure***** \(WBS\)** 

**Level 1 **

**Level 2 **

**Level 3 **

## **Deskripsi **

1.1.1 

Observasi dan 

Identifikasi 

wawancara pemangku 

Masalah 

kepentingan 

1.1 Inisiasi 

Analisis kelayakan 

1.1.2 Studi 

teknis, operasional, 

Kelayakan 

ekonomi 

1.2.1 

1. *Project *

Rincian struktur 

Penyusunan 

*Management* 

pekerjaan 

1.2 

WBS 

Perencanaan 

1.2.2 

Perhitungan biaya 

Estimasi 

pengembangan 

Biaya 

1.3.1 

1.3 

Pemantauan kemajuan 

Progress 

Monitoring 

mingguan 

Tracking 

2.1.1 

*Functional *

Identifikasi 40\+ 

*Requiremen*

kebutuhan fungsional 

2.1 

*ts* 

*Requirements* 

2.1.2 *Non-*

2. Analysis 

*functional *

Keamanan, kinerja, 

*Requiremen*

kegunaan 

*ts* 

2.2 *System *

2.2.1 *As-Is *

Dokumentasi proses 

*Analysis* 

*Process* 

bisnis saat ini 



**Level 1 **

**Level 2 **

**Level 3 **

## **Deskripsi **

2.2.2 *To-Be *

Rancangan proses bisnis 

*Process* 

baru 

Diagram relasi entitas 16 

3.1.1 *ERD* 

3.1 *Database *

tabel 

*Design* 

3.1.2 

Normalisasi hingga 3NF 

Normalisasi 

3.2.1 

Sketsa antarmuka 

3.2 *UI/UX *

*Wireframe* 

pengguna 

*Design* 

3. *Design* 

3.2.2 

Desain visual 41 

*Mockup* 

halaman di Figma 

3.3.1 *Use *

Diagram kasus 

*Case *

penggunaan 

3.3 *UML *

*Diagram* 

*Diagrams* 

3.3.2 

Diagram aktivitas proses 

*Activity *

bisnis 

*Diagram* 

4.1.1 

Instalasi dan 

*Laravel *

konfigurasi *framework* 

*Setup* 

4. 

4.1.2 

*Implementati*

4.1 *Backend* 

*Database *

Migrasi skema basis data 

*on* 

*Migration* 

4.1.3 *API *

Pengembangan *controlle*

*Developme*

*r* dan *model* 

*nt* 



**Level 1 **

**Level 2 **

**Level 3 **

## **Deskripsi **

4.2.1 *Blade *

Pembuatan templat *view* 

*Templates* 

4.2 *Frontend* 

4.2.2 

*Styling* dengan Tailwind 

*Tailwind *

CSS 

*Styling* 

4.3.1 

*Payment *

*Integrasi Midtrans *

4.3 *Integration* 

*Gateway* 

4.3.2 *Email *

Konfigurasi notifikasi 

*Service* 

email 

5.1 *Unit *

5.1.1 PHP 

30 *test cases* 

*Testing* 

Unit *Tests* 

5.2 *Integration *

5.2.1 *API *

Pengujian integrasi antar 

5. *Testing* 

*Testing* 

*Testing* 

modul 

5.3.1 *User *

Pengujian oleh pengguna 

5.3 UAT 

*Testing* 

akhir 

6.1.1 VPS 

Pengaturan *Ubuntu, *

*Configurati*

6.1 *Server *

*Nginx, PHP, MySQL* 

*on* 

*Setup* 

6. 

6.1.2 *SSL *

*Instalasi Let's Encrypt *

*Deployment* 

*Certificate* 

6.2.1 

6.2 *Go Live* 

*Database *

Migrasi data ke produksi 

*Migration* 



**Level 1 **

**Level 2 **

**Level 3 **

## **Deskripsi **

6.2.2 

*System *

Peluncuran sistem 

*Launch* 

****

**Gantt Chart :** 

*Gantt Chart* menampilkan jadwal proyek dalam bentuk diagram batang yang menunjukkan tanggal mulai, durasi, dan tanggal selesai dari setiap aktivitas. 





Week 

Activity 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20 21 22 23 24 25 

1. Requirements 





Analysis 

- Observation 

- Interview 

- Documentation 

2. System Design 





- Database 

Design 

- UI/UX Design 

- UML 

Diagrams 



3. Implementation 





- Backend 

Development 



- Frontend 

Development 

- Integration 





Week 

Activity 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20 21 22 23 24 25 

4. Testing 





- Unit Testing 

- Integration 

Testing 

- Functional 

Testing 

- UAT 

5. Deployment 





- Server Setup 

- Migration 

- Go Live 

6. Documentation 





- Report Writing 

- Presentation 

Prep 

****





**4.2.2. Perencanaan Waktu Pengerjaan \( *Time*****\)** Proyek dikerjakan selama 16 minggu \(4 bulan\) dengan pembagian waktu sebagai berikut : 

**Tabel IV.2 **

**Jadwal Pengerjaan Proyek** 

**No **

**Fase **

**Durasi **

**Periode **

## **Luaran **

### Analisis 

16-29 Sep 

Dokumen SRS, 

1 

2 minggu 

Kebutuhan 

2025 

Studi Kelayakan 

ERD, Diagram 

Desain 

30 Sep - 13 

2 

2 minggu 

UML, *Mockup *

Sistem 

Okt 2025 

*UI/UX* 

14 Okt - 10 

Aplikasi web 60\+ 

3 

Implementasi 

4 minggu 

Nov 2025 

halaman 

11-24 Nov 

Laporan pengujian, 

4 

Pengujian 

2 minggu 

2025 

persetujuan UAT 

25 Nov - 1 

Sistem produksi 

5 

Deployment 

1 minggu 

Des 2025 

aktif 

Paralel 

Laporan akhir, 

6 

Dokumentasi 

5 minggu 

dengan semua 

manual, presentasi 

fase 

****



****





**4.2.3. Perencanaan Anggaran Biaya \( *Cost*****\)** Estimasi biaya proyek menggunakan metode *bottom-up* berdasarkan WBS: **Tabel IV.3 **

**Estimasi Biaya Proyek** 

**No **

**Kategori **

## **Item **

**Biaya \(Rp\) **

*Project Manager* \(11 minggu × Rp 

*Project *

1.100.000 

1 

100.000/minggu\) 

*Management *

*Contingency* \(10%\) 

110.000 

Laptop *Development* \(sudah ada\) 

0 

2 

*Hardware *

VPS *Hosting* \(1 tahun\) 

1.200.000 

*Laravel Framework* \(gratis\) 

0 

3 

*Software *

*MySQL Database *\(gratis\) 

0 

Domain & SSL \(1 tahun\) 

150.000 

*Backend Developer* \(4 minggu × 

800.000 

Rp 200.000/minggu\) 

*Frontend Developer* \(4 minggu × 

4 

*Development *

800.000 

Rp 200.000/minggu\) 

*Full-stack Developer* \(4 minggu × 

800.000 

Rp 200.000/minggu\) 

*Testing Tools* \(gratis - PHPUnit\) 

0 

5 

*Testing *

UAT *Sessions* 

200.000 

6 

Training 

*User Training Materials *

100.000 

Dokumentasi, Transport, 

7 

Lain-lain 

300.000 

Komunikasi 

**TOTAL** 

## **5.560.000**

**Estimasi Biaya Berulang Tahunan \(Biaya Operasional\) :** **No **

## **Item **

**Biaya/Tahun \(Rp\) **

1 

VPS *Hosting* 

1.200.000 

2 

Domain & SSL renewal 

150.000 

*Payment Gateway Fee* \(2,9% \+ Rp 2.000 per 

~7.200.000 \(estimasi 

3 

transaksi\) 

100 transaksi/bulan\) 

4 

Pemeliharaan & Dukungan 

1.200.000 

**TOTAL** 

## **9.750.000**

****

**4.2.4. Perencanaan Kualitas \( *Quality*****\)** Standar kualitas yang ditetapkan untuk proyek ini: A. Standar Kualitas Fungsional : 

• Fungsionalitas : Minimal 90% kebutuhan fungsional harus terpenuhi dan berfungsi dengan baik 

• Akurasi : 100% akurasi dalam perhitungan pembayaran, penjadwalan, dan pelaporan 

• Kelengkapan : Semua modul utama \(pemesanan, pembayaran, dasbor\) harus tersedia 

• Interoperabilitas** **: Integrasi Midtrans dan layanan email berfungsi tanpa galat 

B. Standar Kualitas Non-Fungsional : 

• Performa** **: 

- Waktu muat halaman < 2 detik \(rata-rata\) 

- Waktu respons API < 500ms untuk 95% permintaan 

- Waktu kueri basis data < 100ms \(rata-rata\) 

• Keamanan** **: 

- Mitigasi kerentanan OWASP Top 10 

- *Hashing* kata sandi dengan *bcrypt* 

- HTTPS untuk semua komunikasi 

- Pencegahan *SQL injection* \(Eloquent ORM\) 



• Usabilitas** **: 

- Skor *System Usability Scale* \(SUS\) minimal 70/100 

- Tingkat kepuasan pengguna minimal 4/5 

- Tingkat penyelesaian tugas ≥ 90% 

• Keandalan** **: 

- Waktu aktif minimal 99% \(maksimal waktu mati 7,2 jam/bulan\) 

- Waktu Rata-rata Antar Kegagalan \( *Mean Time Between* *Failures*/MTBF\) > 720 jam 

- Tujuan Waktu Pemulihan \( *Recovery Time Objective*/RTO\) < 4 jam 

• Kemudahan Pemeliharaan** **: 

- Cakupan pengujian kode minimal 70% 

- Skor kualitas kode \(CodeClimate\) ≥ B 

- Dokumentasi lengkap \( *inline comments*, README, dokumentasi API\) 

**4.2.5. Perencanaan Sumber Daya \( *Resource*****\)** **A. Sumber Daya Manusia : **

**Tabel IV.4 **

**Alokasi Sumber Daya Manusia** 

**Alokasi **

**No **

**Nama **

**Peran **

**Tanggung Jawab **

## **Waktu **

### ***Project ***

Koordinasi tim, 

Roki Anjas 

*Manager & *

pengembangan 

40 

1 

\(11250066\) 

*Backend *

*backend*, 

jam/minggu 

*Developer *

dokumentasi 

*Frontend *

Desain 

Susanto 

*Developer & *

antarmuka, 

35 

2 

\(11250068\) 

*UI/UX *

pengembangan 

jam/minggu 

*Designer *

*frontend* 

Fahruroji 

*Full-stack *

Desain database, 

35 

3 

\(11250085\) 

*Developer & *

pengembangan 

jam/minggu 



**Alokasi **

**No **

**Nama **

**Peran **

**Tanggung Jawab **

## **Waktu **

### ***Database ***

*full-stack*, 

*Architect *

*deployment* 

**B. Sumber Daya Teknologi : **

• Perangkat Keras Pengembangan :** **

- Laptop/PC untuk pengembangan \(3 unit - milik tim\) 

- VPS Ubuntu 22.04 LTS untuk server produksi 

- Spesifikasi VPS: 4 vCPU, 8GB RAM, 160GB SSD 

• Perangkat Lunak Pengembangan :** **

- IDE: *Visual Studio Code* \(gratis\) 

- Kontrol Versi: Git & GitHub \(gratis\) 

- Desain: Figma \( *free tier*\) 

- *Framework*: Laravel 10 \( *open source*\) 

- Basis Data: MySQL 8.0 \( *open source*\) 

- *Framework* CSS: Tailwind CSS \( *open source*\) **C. Sumber Daya Infrastruktur : **

• Domain & Sertifikat SSL 

• Layanan email \(SMTP\) 

• Akun *payment gateway* \(Midtrans\) 





**4.2.6. Manajemen Risiko \( *Risk*****\)** Identifikasi, analisis, dan strategi mitigasi risiko proyek : **Tabel IV.5 **

**Identifikasi dan Mitigasi Risiko** 

**Probabilit**

**Skor **

***Ow***

**No **

**Risiko **

**Dampak **

**Mitigasi **

**as **

**Risiko **

## **ner **

### Waktu 

penyangga 

Keterla

10%, prioritas 

1 

mbatan 

Sedang 

Tinggi 

12 

PM 

fitur dengan 

Jadwal 

MoSCoW, *daily *

*standup* 

Dokumentasi 

*Scope *

kebutuhan yang 

*creep* \(

jelas, proses 

peruba

2 

Sedang 

Tinggi 

12 

kontrol 

PM 

han 

perubahan, 

kebutu

persetujuan 

han\) 

formal 

Bug 

Pengujian 

kritis 

menyeluruh, 

Tim 

3 

saat *de*

Rendah 

Tinggi 

6 

*staging *

Dev 

*ployme*

*environment*, 

*nt* 

rencana *rollback* 

Anggot

Berbagi 

a tim 

pengetahuan, 

sakit/ti

4 

Rendah 

Sedang 

4 

dokumentasi 

PM 

dak 

kode, *pair *

tersedi

*programming* 

a 



**Probabilit**

**Skor **

***Ow***

**No **

**Risiko **

**Dampak **

**Mitigasi **

**as **

**Risiko **

## **ner **

### Integra

*Prototyping* awa

*Bac*

si *paym*

l, dokumentasi 

*kend*

5 

*ent *

Sedang 

Sedang 

6 

API lengkap, 

De

*gatewa*

pengujian *sandb*

v 

*y* gagal 

*ox* 

Cadangan 

otomatis harian, 

DB 

Kehila

retensi 30 hari, 

*Arc*

6 

ngan 

Rendah 

Tinggi 

6 

rencana 

*hite*

data 

pemulihan 

*ct* 

bencana 

Audit 

Pelang

keamanan, *pene*

garan 

Sangat 

*tration testing*, 

Tim 

7 

Rendah 

8 

keama

Tinggi 

mengikuti 

Dev 

nan 

pedoman 

*OWASP* 

*Full*

*Load *

*-*

Masalah 

*testing*, *database *

8 

Sedang 

Sedang 

6 

*stac*

kinerja 

*indexing*, 

*k* 

strategi *caching* 

Dev 

**Catatan Skor Risiko :** 

• Probabilitas : Rendah \(1\), Sedang \(2\), Tinggi \(3\) 

• Dampak : Rendah \(2\), Sedang \(4\), Tinggi \(6\), Sangat Tinggi \(8\) 

• Skor Risiko = Probabilitas × Dampak 





**4.2.7. Perencanaan Komunikasi \( *Communication*****\)** Strategi komunikasi untuk memastikan informasi mengalir dengan efektif : 

**A. Komunikasi Internal Tim: **

• *Daily Standup*** **: Chat group *WhatsApp* setiap pagi \(15 menit\) 

- *What did I do yesterday*? 

- *What will I do today*? 

- *Any blockers*? 

• 

*Weekly Team Meeting*** **: Setiap Senin pukul 19.00 WIB *via* *Google Meet* \(1-2 jam\) 

- *Review progress vs plan *

- *Demo fitur yang selesai *

- *Planning untuk minggu depan *

- *Risk review *

• Tinjauan Kode** **: *Pull request* di GitHub dengan tinjauan wajib dari minimal 1 anggota tim 

**B. Komunikasi dengan Pemangku Kepentingan : **

• Laporan Kemajuan ke Dosen Pembimbing** **: Setiap 2 minggu \(email \+ 

pertemuan\) 

• Pertemuan Klien \(CUR-HEART\)** **: Dua mingguan untuk tinjauan dan umpan balik 

• Sesi UAT** **: 3 kali selama fase pengujian 

**C. Dokumentasi : **

• *Google Drive *: Repositori untuk semua dokumen proyek 

• *GitHub Wiki *: Dokumentasi teknis dan API 

• **Notion **: Basis pengetahuan dan catatan pertemuan **D. Alat Komunikasi : **

• *WhatsApp* : Komunikasi cepat 

• *Google Meet* : Pertemuan virtual 

• *Email* : Komunikasi formal 

• *GitHub* : Kolaborasi kode 

• *Figma* : Kolaborasi desain 



**4.2.8. Perencanaan Pengadaan \( *Procurement*****\)** Pengadaan barang dan jasa yang diperlukan : 

**Tabel IV.6 **

**Daftar Pengadaan** 

**NO **

***Item ***

***Vendor ***

**Biaya **

**Waktu **

## **PIC **

### ***VPS ***

*Niagahost*

Rp 

Fahru

1 

Minggu 8 

*Hosting *

*er *

1.200.000/tahun 

roji 

*Niagahost*

Rp 

Fahru

2 

*Domain .id *

Minggu 8 

*er *

150.000/tahun 

roji 

*SSL *

*Let's *

Fahru

3 

Gratis 

Minggu 8 

*Certificate *

*Encrypt *

roji 

Gratis \(dev\), 

*Payment *

4 

*Midtrans *

2,9% \+ Rp 

Minggu 6 

Roki 

*Gateway *

2.000 \(prod\) 

*Gmail *

*Email *

5 

*SMTP / *

Gratis \( *limited\)* 

Minggu 7 

Roki 

*Service *

*SendGrid *

**Proses Pengadaan :** 

1. Identifikasi kebutuhan 

2. Pemilihan & perbandingan vendor 

3. Persetujuan dari sponsor 

4. *Purchase order* 

5. Pengiriman & verifikasi 

6. Pembayaran 

7. Dokumentasi 

**4.2.9. Perencanaan Integrasi \( *Integration*****\)** Integrasi sistem dengan layanan eksternal : 

**A. Integrasi *Payment Gateway***** \(Midtrans\) : **

• Metode** **: *Snap API* untuk *checkout* yang mulus 



• Metode Pembayaran** **: Kartu kredit/debit, Transfer bank, Dompet digital \(GoPay, OVO, Dana\) 

• Keamanan** **: Memenuhi *PCI-DSS*, dukungan *3D Secure* 

• *Webhook*** **: Untuk notifikasi pembayaran waktu nyata 

• Waktu** **: Minggu 6-7 \(implementasi \+ pengujian\) **B. Integrasi Layanan Email : **

• Penyedia** **: Gmail SMTP / *SendGrid* 

• Kasus Penggunaan** **: 

- Email selamat datang saat registrasi 

- Email verifikasi 

- Konfirmasi pemesanan 

- Notifikasi pembayaran 

- Pengingat sesi \(H-1, H-0\) 

- Reset kata sandi 

• Waktu** **: Minggu 7-8 

**C. Integrasi Masa Depan \(Fase 2\) : **

• Notifikasi SMS via *Twilio* 

• Penyimpanan *cloud *\( *Google Drive* / AWS S3\) 

• Konferensi video \( *Zoom API*\) 

• *Analytics* \( *Google Analytics*\) 

**4.2.10. Manajemen Pemangku Kepentingan \( *Stakeholder*****\)** Identifikasi dan strategi keterlibatan pemangku kepentingan: **Tabel IV.7 **

**Daftar Pemangku Kepentingan** 

**Kepe**

**Pemangku **

**Keku**

**No **

**Peran **

**nting**

**Minat **

**Strategi **

**Kepentingan **

**asaan **

## **an **

### Spons

Kelola 

Pemilik CUR-

Sangat 

1 

or & 

Tinggi 

Tinggi 

Erat: 

HEART 

Tinggi 

Penga

Presentasi 



**Kepe**

**Pemangku **

**Keku**

**No **

**Peran **

**nting**

**Minat **

**Strategi **

**Kepentingan **

**asaan **

## **an **

### mbil 

kemajuan 

Keput

bulanan, 

usan 

persetujuan 

kebutuhan 

Tetap 

Berinforma

Pengg

si: 

Terapis \(3 

2 

una 

Tinggi 

Sedang Tinggi 

Lokakarya 

orang\) 

Akhir 

kebutuhan, 

UAT, 

pelatihan 

Tetap 

Berinforma

Pengg

si: 

Admin \(2 

3 

una 

Tinggi 

Sedang Tinggi 

Lokakarya 

orang\) 

Akhir 

kebutuhan, 

UAT, 

pelatihan 

Pantau: 

Pengg

Survei 

Klien \(8 orang 

4 

una 

Sedang Rendah Sedang 

kebutuhan, 

sample\) 

Akhir 

pengujian 

kegunaan 

Dosen 

Penas

Sangat 

Kelola 

5 

Tinggi 

Tinggi 

Pembimbing 

ihat 

Tinggi 

Erat: 



**Kepe**

**Pemangku **

**Keku**

**No **

**Peran **

**nting**

**Minat **

**Strategi **

**Kepentingan **

**asaan **

## **an **

### Akad

Konsultasi 

emik 

mingguan, 

tinjauan 

dokumen 

Kelola 

Tim 

Erat: *Daily *

Tim 

Penge

Sangat 

6 

Tinggi 

Tinggi 

*standup*, 

Pengembang 

mban

Tinggi 

pertemuan 

gan 

mingguan 

Strategi Keterlibatan :** **

• Kelola Erat** **: Kekuasaan tinggi, minat tinggi - keterlibatan intensif dan pembaruan berkala 

• Tetap Berinformasi** **: Kekuasaan rendah, minat tinggi - informasi berkala, masukan didengarkan 

• Jaga Kepuasan : Kekuasaan tinggi, minat rendah - pembaruan penting, minta persetujuan 

• Pantau** **: Kekuasaan rendah, minat rendah - komunikasi minimal, pemantauan 

## **4.2.11. Batasan Proyek **

### Batasan-batasan proyek yang telah disepakati: 

**A. Batasan Waktu: **

• Fokus proyek pada pembangunan sistem informasi dalam kurun waktu 16 minggu \(4 bulan\) 

• Tidak membahas kontrol kualitas & jaminan kualitas secara khusus \(hanya pengujian standar\) 

• Evaluasi jangka panjang \(> 6 bulan\) tidak termasuk dalam ruang lingkup 



**B. Batasan Fitur : **

• Tidak membahas mengenai risiko proyek secara mendalam, fokus hanya pada risiko permintaan perubahan 

• Modul analitik dan pelaporan dibatasi pada laporan standar \(analitik lanjutan/ *BI* ditunda ke fase 2\) 

• Integrasi dengan sistem eksternal lain \(selain Midtrans dan email\) tidak termasuk dalam fase 1 

**C. Batasan Biaya : **

• Biaya yang dimaksud adalah biaya untuk tim proyek \(tidak termasuk manajer proyek senior eksternal\) 

• Anggaran terbatas pada pengembangan dan 1 tahun operasional awal 

• Biaya pelatihan intensif untuk semua staf tidak termasuk \(hanya pelatihan dasar 2 jam\) 

**D. Batasan Teknis : **

• Sistem dioptimalkan untuk desktop dan tablet, dukungan mobile dalam bentuk *responsive design* \(bukan aplikasi mobile *native*\) 

• Kapasitas sistem didesain untuk menangani hingga 50 pengguna bersamaan 

• Bahasa sistem: Bahasa Indonesia \(multi-bahasa tidak termasuk fase 1\) 

• Sistem tidak termasuk fitur panggilan video untuk sesi terapi daring **E. Batasan Data : **

• Migrasi data historis dibatasi pada data 6 bulan terakhir 

• Retensi cadangan data: 30 hari \(untuk cadangan jangka panjang memerlukan biaya tambahan\) 

**F. Batasan Hukum: **

• Sistem mengikuti prinsip dasar UU Perlindungan Data Pribadi, namun sertifikasi kepatuhan formal tidak termasuk 

• Penyangkalan medis: Sistem untuk manajemen administrasi, bukan untuk diagnosis medis 





**4.2.12. Asumsi Proyek **

Asumsi-asumsi yang mendasari perencanaan proyek : 

**A. Asumsi Pengadaan : **

• Pengadaan sudah tidak ada masalah, sumber daya non-personil tersedia sesuai spesifikasi 

• VPS hosting dapat disewa sesuai spesifikasi yang dibutuhkan 

• Domain dapat dibeli dan dikonfigurasi dengan lancar **B. Asumsi Sumber Daya Manusia : **

• Sumber daya manusia sudah tersedia sesuai dengan spesifikasi proyek 

• Anggota tim adalah SDM profesional \(mahasiswa dengan kompetensi memadai\) 

• Tidak ada anggota tim yang mengundurkan diri atau sakit berkepanjangan selama proyek 

• Terapis dan admin CUR-HEART bersedia meluangkan waktu untuk lokakarya, UAT, dan pelatihan 

**C. Asumsi Teknis : **

• Manajer proyek adalah personil dari dalam tim \(ketua tim mahasiswa\) 

• Infrastruktur teknologi \(internet, listrik\) stabil di lokasi pengembangan dan CUR-HEART 

• API Midtrans berfungsi stabil dengan dokumentasi lengkap 

• Layanan email SMTP dapat dikonfigurasi tanpa hambatan **D. Asumsi Organisasi : **

• Struktur organisasi CUR-HEART sudah diterapkan dengan baik 

• Pemilik & manajer proyek sudah ditunjuk beserta anggota tim 

• Persetujuan dan pengambilan keputusan dari pemangku kepentingan dapat dilakukan tepat waktu 

• Tidak ada perubahan manajemen atau struktur organisasi selama proyek 

**E. Asumsi Proses Bisnis : **

• Proses bisnis CUR-HEART yang ada saat ini sudah terdokumentasi dengan baik 



• Pemangku kepentingan dapat mengartikulasikan kebutuhan mereka dengan jelas 

• Tidak ada perubahan signifikan pada proses bisnis selama pengembangan 

**F. Asumsi Pengguna : **

• Klien CUR-HEART memiliki akses internet dan perangkat \(smartphone/laptop/tablet\) 

• Pengguna memiliki kemampuan dasar menggunakan teknologi digital 

• Klien bersedia mengadopsi sistem online untuk pemesanan **G. Asumsi Regulasi : **

• Tidak ada perubahan regulasi terkait data pribadi atau layanan kesehatan mental selama proyek 

• Bisnis CUR-HEART memiliki izin operasional yang legal **4.3. DESKRIPSI PRODUK / SERVIS **

Berikut ini adalah deskripsi umum \( *high-level*\) mengenai produk atau layanan yang dihasilkan dari proyek ini : 

## **4.3.1. Tujuan Proyek **

Tujuan proyek ini adalah membangun sistem informasi berbasis web yang dapat memberikan informasi yang berkaitan dengan manajemen pemesanan dan terapi hipnoterapi CUR-HEART, mencakup : 

• Informasi lengkap tentang layanan terapi yang ditawarkan 

• Profil terapis dengan spesialisasi dan jadwal ketersediaan 

• Sistem pemesanan online yang mudah dan cepat 

• Manajemen sesi terapi dan dokumentasi klien 

• Pembayaran online yang aman dan terintegrasi 

• Dasbor analitik untuk pengambilan keputusan 

## **4.3.2. Pengguna Sistem **

Sistem ini memiliki 3 tipe pengguna utama dengan hak akses berbeda. 

Sistem yang dibangun harus mampu : 





**A. Untuk Klien : **

• Menampilkan informasi jumlah layanan, terapis, dan testimoni 

• Menampilkan informasi layanan terbaru dan terapis unggulan 

• Memberikan kemampuan pemesanan layanan secara online 24/7 

• Menampilkan riwayat pemesanan dan sesi terapi 

• Menyediakan sistem pembayaran yang aman dan mudah 

• Menampilkan kemajuan terapi dan catatan sesi \(yang dibagikan\) **B. Untuk Terapis : **

• Manajemen jadwal dan ketersediaan secara mandiri 

• Melihat daftar klien dan detail pemesanan hari ini 

• Mendokumentasikan sesi terapi dengan formulir terstruktur 

• Mengakses riwayat lengkap klien untuk kontinuitas perawatan 

• Melihat dasbor pendapatan dan statistik kinerja 

• Memperbarui profil dan pengaturan notifikasi 

**C. Untuk Admin : **

• Pemantauan pemesanan waktu nyata dengan pelacakan status 

• Manajemen pengguna \(klien, terapis, admin\)in\) 

• Manajemen layanan \(operasi CRUD\) 

• Laporan keuangan dan analitik : 

- Total pemesanan dan pendapatan 

- Rincian per layanan dan terapis 

- Trend pemesanan bulanan 

• Approval dan verifikasi terapis baru 

• System settings dan configuration 

## **4.3.3. Fitur Utama Sistem **

**A. Modul *Public Website***** **

• *Landing page* dengan informasi bisnis 

• Katalog layanan terapi lengkap dengan deskripsi 

• Direktori terapis dengan profil dan rating 

• Blog/artikel tentang kesehatan mental 

• FAQ dan halaman bantuan 

• Formulir kontak 



**B. Modul Autentikasi **

• Autentikasi multi-peran \(Klien, Terapis, Admin\) 

• Registrasi dengan validasi email 

• *Login* dengan fitur ingat saya 

• Lupa kata sandi & atur ulang kata sandi 

• *Social login* \( *Google, Facebook*\) - opsional **C. Modul Pemesanan **

• *Wizard* pemesanan 4 langkah: 

1. Pilih layanan terapi 

2. Pilih terapis \(atau penugasan otomatis\) 

3. Pilih tanggal & waktu 

4. Konfirmasi & pembayaran 

• Pengecekan ketersediaan waktu nyatayata 

• Tipe sesi: Daring/ *Online*/Luring/ *Offline* 

• Dukungan kode promo 

• Email konfirmasi pemesanan 

## **D. Modul Pembayaran **

• Integrasi *payment gateway* Midtrans 

• Beragam metode pembayaran : 

- Kartu kredit/debit 

- Transfer bank 

- Dompet digital \(GoPay, OVO, Dana\) Dana\) 

• Verifikasi pembayaran otomatis 

• Pembuatan faktur \(PDF\) 

• Riwayat pembayaran dan pelacakan status 

## **E. Modul Dasbor Klien **

• Ikhtisar : Sesi mendatang, sesi selesai, total jam 

• Janji Temu Saya: Daftar, detail, jadwal ulang, batalkan 

• Pelacakan Kemajuan : Grafik visual dan metrik 

• Pesan : Obrolan dengan terapis 

• Profile & settings 





**F. Modul Dasbor Terapis **

• Jadwal hari ini dengan hitungan mundur 

• Daftar klien dan detail 

• Formulir dokumentasi sesi dengan *rich text editor* 

• Riwayat sesi dan arsip catatan 

• Pengaturan ketersediaan \(jam kerja, waktu libur\) 

• Dasbor pendapatan 

• Manajemen profil 

## **G. Modul Dasbor Admin **

• Kartu statistic : Pengguna, pemesanan, pendapatan, kesehatan sistem 

• Grafik : Tren pendapatan, pertumbuhan pengguna, layanan teratasayanan teratas 

• Manajemen pengguna \(CRUD, menyetujui terapis\) 

• Manajemen pemesanan \(lihat, edit, batalkan, pengembalian dana\) 

• Manajemen layanan \(CRUD\) 

• Laporan keuangan \( *ekspor Excel*/PDF\) 

• Pengaturan sistem 

## **H. Modul Notifikasi **

• Notifikasi email : 

- Konfirmasi pemesanan 

- Pembayaran berhasil 

- Pengingat sesi \(H-1, H-0\) 

- Notifikasi pembatalan 

• Notifikasi dalam aplikasi 

• Pengingat SMS \(pengembangan mendatang\) 

## **I. Modul Pelaporan **

• Laporan pemesanan : Harian, mingguan, bulanan 

• Laporan pendapatan : Per layanan, per terapis 

• Laporan aktivitas pengguna 

• Format ekspor : PDF, Excel, CSV 





## **4.3.4. Arsitektur Sistem **

### Sistem 

dibangun 

dengan 

arsitektur 

## **MVC **

**\( *Model-View-***

***Controller*****\)** menggunakan *framework* Laravel : LAPISAN PRESANTASI 

\( *Views – Blade Templates \+ Tailwind CSS\) *

****

-

*Halaman public *



-

*Dasbor klien *



-

*Dasbor terapis *



-

*Dasbor admin *





LAPISAN APLIKASI 



\( *Controllers \+ Middleware\) *



-

*AuthController *



-

*BookingController *



-

*PaymentController *



-

*DasboardController *



-

*AdminController *





LAPISAN LOGIKA BISNIS 



*\(Models \+ Services \+ Events\) *



-

*Model User, Therapist, Client *



-

*Model Service, Booking, Payment *



-

*Model Session, Review *



-

Aturan bisnis & Validasi 





LAPISAN AKSES DATA 



\( *Eloquent ORM \+ MySQL Database*\) 



-

16 tabel ternomalisasi \(3NF\) 



-

*Migrations & senders *



-

*Relationships & constraints *





Gambar IV. 1 * Framework Laravel *





**4.3.5. Desain Basis Data **

Sistem menggunakan 16 tabel utama : 

1. **users** - Data pengguna universal 

2. **clients** - Data spesifik klien 

3. **therapists** - Data spesifik terapis 

4. **services** - Katalog layanan terapi 

5. **therapist\_services** - Relasi terapis-layanan 6. **therapist\_availability** - Jadwal ketersediaan terapis 7. **bookings** - Data pemesanan 

8. **sessions** - Data sesi terapi 

9. **session\_notes** - Catatan sesi dari terapis 10. **payments** - Transaksi pembayaran 

11. **reviews** - Ulasan dan rating 

12. **notifications** - Notifikasi sistem 

13. **messages** - Obrolan antara klien-terapis 14. **promo\_codes** - Kode promo diskon 

15. **audit\_logs** - Log aktivitas untuk audit 

16. **system\_settings** - Konfigurasi sistem 

Normalisasi : **Third Normal Form \(3NF\)** untuk menghindari redundansi dan anomali data. 

**4.3.6. Peran dan Hak Akses Pengguna **

## **A. Tamu **

• Lihat: Halaman utama, layanan, terapis, blog 

• Aksi: Registrasi, login, kontak 

## **B. Klien **

• Lihat: Semua izin tamu \+ dasbor, pemesanan, kemajuan, pesan 

• Aksi: Pesan layanan, lakukan pembayaran, jadwal ulang/batalkan, beri ulasan, obrolan 

## **C. Terapis **

• Lihat: Dasbor, jadwal, klien, sesi, pendapatan 

• Aksi: Atur ketersediaan, dokumentasi sesi, lihat riwayat klien, obrolan, perbarui profil 



**D. Administrator **

• Lihat: Semua data \(pengguna, pemesanan, pembayaran, laporan\) 

• Aksi: CRUD penuh pada semua sumber daya, menyetujui terapis, membuat laporan, pengaturan sistem 

## **4.3.7. Keamanan Sistem **

**A. Autentikasi & Otorisasi **

• *Hashing* kata sandi dengan *bcrypt* 

• Manajemen sesi dengan Laravel 

• Perlindungan CSRF untuk semua formulir 

• Kontrol akses berbasis peran \( *Role-Based Access Control*/RBAC\) **B. Keamanan Data **

• HTTPS untuk semua komunikasi 

• Pencegahan *SQL injection* \(Eloquent ORM\) 

• Pencegahan XSS \( *Blade escaping*\) 

• Enkripsi untuk data sensitif \(rekam medis\) 

## **C. Keamanan Pembayaran **

• Sesuai PCI-DSS \(melalui Midtrans\) 

• Tidak ada data kartu kredit disimpan secara lokal 

• Dukungan 3D Secure 

## **D. Kepatuhan **

• UU Perlindungan Data Pribadi \(UU PDP\) 

• Arsitektur siap GDPR 

• Kebijakan retensi data \(cadangan 30 hari\) 

**4.3.8. Kinerja dan Skalabilitas **

## **A. Optimasi Kinerja **

• Pengindeksan basis data pada kueri yang sering digunakan 

• *Caching* Laravel \( *config*, *route*, *view cache*\) 

• *Lazy loading* untuk relasi Eloquent 

• CDN untuk aset statis \(pengembangan mendatang\) 

## **B. Skalabilitas **

• Siap penskalaan horizontal \( *load balancer* \+ beberapa server\) 

• Replikasi basis data \( *master-slave*\) 



• Pekerja antrian untuk pekerjaan latar belakang 

• Sesi tanpa keadaan \(siap untuk *clustering*\) **Target Metrik :** 

• Waktu muat halaman: < 2 detik 

• Pengguna bersamaan: 100\+ 

• Waktu aktif: ≥ 99,5% 

• Waktu kueri basis data: < 100ms \(rata-rata\) 





**4.3.9. Pelaksanaan Proyek \(Desain Sistem\) **

Pelaksanaan proyek merupakan fase implementasi dari perencanaan yang telah dibuat. Pada fase ini dilakukan desain sistem yang mencakup perancangan basis data, pemodelan UML, dan desain antarmuka pengguna. 

## **4.3.9.1.Use Case Diagram **

*Use Case* Diagram menggambarkan interaksi antara aktor \(pengguna\) dengan sistem, serta fungsionalitas yang dapat dilakukan oleh masing-masing aktor. 





Gambar IV. 2 *Use Case Diagram* Sistem Informasi CUR-HEART 





**Aktor dalam Sistem :** 

1. **Tamu** - Pengunjung situs web yang belum masuk 2. **Klien** - Pengguna terdaftar yang menggunakan layanan terapi 3. **Terapis** - Praktisi hipnoterapi yang memberikan layanan 4. **Admin** - Administrator sistem yang mengelola seluruh sistem 5. ***Payment Gateway*** - Sistem eksternal untuk pemrosesan pembayaran 

***Use Cases***** Utama :** 

**Untuk Tamu :** 

• Melihat halaman beranda 

• Melihat daftar layanan terapi 

• Melihat profil terapis 

• Registrasi akun baru 

• Masuk ke sistem 

**Untuk Klien :** 

• Melihat jadwal terapis yang tersedia 

• Membuat pemesanan layanan terapi 

• Memilih terapis dan waktu sesi 

• Melakukan pembayaran daring 

• Melihat riwayat pemesanan 

• Melihat riwayat sesi terapi 

• Perbarui profil 

• Membatalkan/jadwal ulang pemesanan \(dengan syarat\) **Untuk Terapis :** 

• Melihat jadwal sesi terapi hari ini dan minggu ini 

• Melihat detail pemesanan klien 

• Mengatur ketersediaan jadwal 

• Mendokumentasikan sesi terapi \(catatan sesi\) 

• Melihat riwayat klien 

• Memperbarui status sesi \(selesai/dibatalkan\) 

• Melihat pendapatan 





**Untuk Admin :** 

• Mengelola data layanan terapi 

• Mengelola data terapis 

• Mengelola data klien 

• Melihat semua pemesanan 

• Konfirmasi pembayaran manual \(jika ada\) 

• Membuat laporan \(pemesanan, keuangan, kinerja\) 

• Pemantauan sistem 

**Untuk *Payment Gateway *****:** 

• Memproses pembayaran 

• Mengirim notifikasi status pembayaran 

• Verifikasi transaksi 





## **4.3.9.2. Activity Diagram **

*Activity Diagram* menggambarkan alur aktivitas dalam sistem untuk berbagai proses bisnis. 

**a. *Activity Diagram***** Proses Reservasi Terapi oleh Klien** Gambar IV. 3 * Activity Diagram * Reservasi Terapi 





Alur proses pemesanan terapi : 

1. Klien login ke sistem 

2. Klien memilih layanan terapi yang diinginkan 

3. Sistem menampilkan daftar terapis dan jadwal yang tersedia 4. Klien memilih terapis dan waktu sesi 

5. Sistem memeriksa ketersediaan jadwal 

- Jika tidak tersedia : Tampilkan pesan kesalahan, kembali ke pemilihan jadwal 

- Jika tersedia : Lanjut ke langkah berikutnya 

6. Klien mengisi informasi tambahan \(keluhan, catatan\) 7. Sistem menampilkan ringkasan pemesanan dan total biaya 8. Klien konfirmasi pemesanan 

9. Sistem membuat catatan pemesanan dengan status " *Pending Payment*" 

10. Sistem alihkan ke *payment gateway* \(Midtrans\) 11. Klien melakukan pembayaran 

12. *Payment gateway* memproses transaksi 

- Jika gagal : Perbarui status menjadi " *Payment Failed*", kirim notifikasi 

- Jika berhasil : Perbarui status menjadi "Paid", lanjut 13. Sistem mengirim email konfirmasi ke klien 

14. Sistem mengirim notifikasi ke terapis terkait 

15. Sistem mengirim email pengingat 1 hari sebelum sesi 16. Selesai 





**b. *Activity Diagram***** Dokumentasi Sesi Terapi oleh Terapis** Gambar IV. 4 * Activity Diagram * Dokumentasi Sesi Terapi * *





Alur proses dokumentasi sesi terapi : 1. Terapis login ke sistem 

2. Terapis melihat daftar sesi hari ini 

3. Terapis memilih sesi yang sudah dilaksanakan 

4. Sistem menampilkan formulir dokumentasi sesi 

5. Terapis mengisi dokumentasi: 

- Teknik yang digunakan 

- Observasi kondisi klien 

- Kemajuan yang dicapai 

- Catatan penting 

- Rekomendasi sesi berikutnya 

6. Terapis menyimpan dokumentasi 

7. Sistem validasi data 

- Jika tidak valid: Tampilkan pesan kesalahan, kembali ke formulir 

- Jika valid: Simpan ke basis data 

8. Sistem perbarui status sesi menjadi "Completed" 

9. Sistem mencatat waktu dokumentasi 

10. Dokumentasi tersimpan dan dapat diakses untuk sesi berikutnya 11. Selesai 





**c. *Activity Diagram Generate *****Laporan oleh Admin **

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****



****

Gambar IV. 5 * Activity Diagram Generate Laporan* Alur pros



es membuat laporan :** **

1. Admin masuk ke sistem 

2. Admin mengakses menu laporan 

3. Admin memilih jenis laporan \(pemesanan, keuangan, kinerja terapis, klien\) 4. Admin memilih periode \(tanggal mulai - tanggal selesai\) 5. Admin memilih penyaring tambahan \(terapis tertentu, layanan tertentu, dll\) 6. Admin klik tombol " *Generate Laporan*" 

7. Sistem mengambil data dari basis data sesuai kriteria 8. Sistem memproses dan menghitung statistik 

9. Sistem menampilkan laporan dalam format tabel dan grafik 10. Admin dapat melihat, ekspor \( *PDF/Excel*\), atau cetak langsung 11. Selesai 





***4.3.9.3.Entity Relationship Diagram \(ERD\) ***

*Entity Relationship Diagram* \(ERD\) menggambarkan struktur basis data sistem informasi CUR-HEART dengan relasi antar entitas. 

****

****

****



Gambar IV. 6 * Activity Diagram Generate * Laporan * *





**Entitas Utama :** 

1. *users* - Menyimpan data semua pengguna sistem \(klien, terapis, admin\) 2. *clients* - Menyimpan data detail klien 

3. *therapists* - Menyimpan data detail terapis 4. *services* - Menyimpan data layanan terapi yang ditawarkan 5. *bookings* - Menyimpan data pemesanan terapi 6. *payments* - Menyimpan data pembayaran 

7. *sessions* - Menyimpan data sesi terapi yang sudah dilaksanakan 8. *session\_notes* - Menyimpan catatan dokumentasi sesi terapi 9. *therapist\_schedules* - Menyimpan jadwal ketersediaan terapis 10. *therapist\_unavailability* - Menyimpan data ketidaktersediaan terapis \(cuti, sakit\) 

11. *reviews* - Menyimpan ulasan dari klien terhadap terapis/layanan 12. *notifications* - Menyimpan notifikasi untuk pengguna 13. *settings* - Menyimpan konfigurasi sistem 14. *activity\_logs* - Menyimpan log aktivitas pengguna \(jejak audit\) **Relasi Utama :** 

• *users \(1\) ↔ \(1\) clients : * One-to-One * *

• *users \(1\) ↔ \(1\) therapists : * One-to-One * *

• *clients \(1\) ↔ \(M\) bookings : * One-to-Many * *

• *therapists \(1\) ↔ \(M\) bookings : * One-to-Many * *

• *services \(1\) ↔ \(M\) bookings : * One-to-Many * *

• *bookings \(1\) ↔ \(1\) payments : * One-to-One * *

• *bookings \(1\) ↔ \(1\) sessions : * One-to-One * *

• *sessions \(1\) ↔ \(M\) session\_notes : * One-to-Many * *

• *therapists \(1\) ↔ \(M\) therapist\_schedules : * One-to-Many * *

• *therapists \(1\) ↔ \(M\) therapist\_unavailability : * One-to-Many * *

• *sessions \(1\) ↔ \(M\) reviews : * One-to-Many * *

• *users \(1\) ↔ \(M\) notifications : * One-to-Many * *

**Keterangan :** 

• \(1\) = *One* 

• \(M\) = *Many* 



• PK = *Primary Key *

• FK = *Foreign Key* 

**Penjelasan Desain Database :** 

1. **Normalisasi 3NF **: Database dinormalisasi hingga *Third Normal Form* \(3NF\) untuk menghindari redundansi data dan menjaga integritas data. 

2. **Relasi *Many-to-Many***** **: Tabel *therapist\_services* digunakan sebagai junction table untuk relasi many-to-many antara terapis dan layanan, memungkinkan satu terapis menangani banyak layanan dan satu layanan ditangani banyak terapis. 

3. **Soft Delete **: Beberapa tabel menggunakan status enum untuk "soft delete" 

\(misalnya status 'archived' pada blog\_posts\) untuk menjaga integritas referensial. 

4. **Audit Trail**: Tabel activity\_logs mencatat semua aktivitas penting pengguna untuk keperluan audit dan keamanan. 

5. **Content **

## **Management **

### : 

Tabel blog\_posts, blog\_categories, faqs, 

dan faq\_categories mendukung fitur content management system untuk admin. 

6. **Financial Management **: Tabel payments dan withdrawals mengelola aliran keuangan dari klien ke sistem dan dari sistem ke terapis. 

7. **Communication **

: 

Tabel messages dan notifications mendukung 

komunikasi real-time antara pengguna. 

8. **Indexing**: Setiap tabel memiliki index yang tepat pada kolom yang sering di-query untuk optimasi performa. 

Database dinormalisasi hingga Third Normal Form \(3NF\) untuk menghindari redundansi data dan menjaga integritas data. 

***4.3.9.4 Desain Antarmuka Pengguna \(UI/UX\) ***

Desain antarmuka pengguna \(UI\) dibuat menggunakan Figma dengan total 66 halaman mockup yang mencakup semua peran pengguna. Desain mengikuti prinsip *user-centered design* dengan fokus pada kemudahan penggunaan, aksesibilitas, dan pengalaman pengguna yang optimal. 



****

**A. Sistem Desain \( *Design System*****\)** **Palet Warna :** 

• **Primary**: Teal \(\#0D9488\) - Menenangkan, profesional, penyembuhan 

• **Secondary**: Purple \(\#9333EA\) - Spiritual, transformasi 

• **Accent**: Orange \(\#F59E0B\) - Energi, optimisme 

• **Neutral**: Skala abu-abu dari \#F9FAFB hingga \#111827 

• **Success**: Green \(\#10B981\) 

• **Warning**: Yellow \(\#F59E0B\) 

• **Error**: Red \(\#EF4444\) 

**Tipografi :** 

• **Heading **: Inter \( *Sans-serif*\) - Modern, bersih, mudah dibaca 

• **Body **: Inter \( *Sans-serif*\) 

• **Ukuran Font **: H1 \(36px\), H2 \(30px\), H3 \(24px\), Body \(16px\), Small \(14px\) 

**Prinsip Desain :** 

• Desain bersih dan minimal 

• Spasi yang konsisten \(skala spasi Tailwind\) 

• Desain responsif dengan pendekatan *mobile-first* 

• Aksesibilitas: Rasio kontras warna minimal 4,5:1 

• Hierarki visual yang jelas 

• Navigasi yang intuitif 



**B. *Mockup***** Halaman Utama **

Sistem memiliki **66 halaman *mockup**** * yang terbagi dalam beberapa kategori : 





**1. Halaman Publik \(12 halaman\) : **



Gambar IV. 7 * Mockup Landing Page** ***

• ***Landing Page **: Hero section, layanan terapi, featured therapists,* *testimoni klien, blog posts *

* *





Gambar IV. 8 * Mockup * Halaman Tentang Kami *** ***

• **Halaman Tentang Kami **: Kisah kami, visi & misi, nilai inti, profil tim, sertifikasi 





Gambar IV. 9 *Mockup* Katalog Layanan 

• **Katalog Layanan**: Filter & pencarian, grid layanan dengan kartu detail 





Gambar IV. 10 * Mockup * Detail Layanan** **

• **Detail Layanan **: *Hero*, navigasi tab \(ikhtisar/manfaat/proses/FAQ\), terapis yang direkomendasikan, ulasan 





Gambar IV. 11 * Mockup Direktori * Terapis *** ***

• **Direktori Terapis**: Pencarian, filter spesialisasi/rating/pengalaman, grid terapis 





Gambar IV. 12 *Mockup* Profil Terapis 

• **Profil Terapis **: Bio lengkap, pendidikan & sertifikasi, layanan & harga, kalender ketersediaan, ulasan klien 





Gambar IV. 13 *Mockup* Daftar Blog** **

• **Daftar Blog **: Artikel unggulan, pencarian, filter kategori, grid artikel blog, bilah samping 





Gambar IV. 14 * Mockup* Detail Blog *** ***

• **Detail Blog **: Konten artikel, metadata, berbagi media sosial, artikel terkait, bagian komentar 





Gambar IV. 15 *Mockup * Hubungi Kami** **

• **Hubungi Kami **: Formulir, info kontak, *Google Maps*, tautan media sosial 





Gambar IV. 16 * Mockup FAQ** ***

• **FAQ **: Pencarian, tab kategori, daftar akordion dengan umpan balik 





Gambar IV. 17 *Mockup* Kebijakan Privasi** **

• **Kebijakan Privasi **: Daftar isi, bagian terstruktur, sorotan penting 





Gambar IV. 18 * Mockup * Syarat & Ketentuan *** ***

• **Syarat & Ketentuan **: Daftar isi, klausul bernomor untuk referensi legal 





**2. Halaman Autentikasi \(4 halaman\) :** 



Gambar IV. 19 *Mockup Login*** **

• ***Login***** **: Layar terpisah dengan ilustrasi, *email* & kata sandi, ingat saya, *login* sosial media 



Gambar IV. 20 * Mockup Registrasi Klien** ***





Gambar IV. 21 *Mockup Registrasi* Terapis** **

• ***Registrasi***** **: Pilihan tipe pengguna \(Klien/Terapis\), formulir berbeda per peran, kotak centang syarat 



Gambar IV. 22 *Mockup* Lupa Kata Sandi 

• **Lupa Kata Sandi **: Formulir sederhana, kirim tautan *reset*, status berhasil 





Gambar IV. 23 *Mockup Reset* Kata Sandi** **

****

• ***Reset***** Kata Sandi **: Kata sandi baru, konfirmasi kata sandi, pengukur kekuatan kata sandi 





**3. *Dashboard***** Klien \(12 halaman\) :** Gambar IV. 24 * Mockup Dasbor Klien** ***

• **Dasbor Utama **: Sambutan, statistik cepat, janji temu berikutnya, sesi mendatang, ikhtisar kemajuan 



Gambar IV. 25 *Mockup* Reservasi Langkah 1 - Pilih Layanan** **

• **Reservasi Langkah 1**: Pemilihan layanan dengan kartu layanan 





Gambar IV. 26 * Mockup* Reservasi Langkah 2 - Pilih Terapis** **

• **Reservasi Langkah 2 **: Pilih terapis dengan profil dan rating Gambar IV. 27 * Mockup * Reservasi Langkah 3 - Pilih Jadwal** **

• **Reservasi Langkah 3**: Pemilih tanggal & waktu dengan ketersediaan waktu nyata 

****

****

****





Gambar IV. 28 *Mockup* Reservasi Langkah 4 - Konfirmasi & Pembayaran** **

• **Reservasi Langkah 4 **: Konfirmasi & pembayaran dengan ringkasan reservasi 



Gambar IV. 29 *Mockup * Reservasi Berhasil** **

• **Reservasi Berhasil **: Selamat, detail reservasi, langkah selanjutnya, tombol aksi 





Gambar IV. 30 *Mockup* Janji Temu** **

• **Janji Temu Saya **: Tab \(mendatang/lampau/dibatalkan\), filter & urutkan, kartu janji temu 



Gambar IV. 31 *Mockup * Detail Janji Temu** **

• **Detail Janji Temu**: Info reservasi, info pembayaran, catatan sesi, aksi jadwal ulang/batalkan 

****

****

****





Gambar IV. 32 * Mockup * Dasbor Kemajuan 

• **Dasbor Kemajuan **: Skor kesehatan, kehadiran sesi, tujuan & pencapaian, pelacakan suasana hati 



Gambar IV. 33 *Mockup * Pesan 

• **Pesan :** Daftar percakapan, area obrolan aktif, indikator mengetik 





Gambar IV. 34 *Mockup* Pengaturan Klien** **

• **Pengaturan Klien**: Profil, keamanan, notifikasi, privasi 





Gambar IV. 35 *Mockup* Notifikasi Klien** **

• **Notifikasi Klien**: Daftar notifikasi, filter, tandai sebagai dibaca **4. *Dashboard***** Terapis \(13 halaman\) :** Gambar IV. 36 *Mockup* Dasbor Terapis - Dasbor Utama 

• **Dasbor Utama **: Sesi hari ini, metrik kunci, ikhtisar pendapatan, ulasan klien 





Gambar IV. 37 * Mockup* Manajemen Jadwal** **

• **Manajemen Jadwal **: Tampilan kalender \(hari/minggu/bulan\), blok janji temu, waktu libur 



Gambar IV. 38 * Mockup * Pengaturan Ketersediaan * *

• **Pengaturan Ketersediaan **: Jam kerja per hari, durasi sesi, jendela reservasi, tanggal khusus 





Gambar IV. 39 * Mockup * Daftar Klien *** ***

• **Daftar Klien **: Cari & filter, kartu klien dengan statistik, aksi massal Gambar IV. 40 * Mockup * Tampilan Profil Klien * *

• **Tampilan Profil Klien **: Ikhtisar, riwayat sesi, catatan & observasi, kemajuan & tujuan, berkas 





Gambar IV. 41 * Mockup * Ruang Sesi * *

• **Ruang Sesi **: Konferensi video dengan timer, bilah kontrol, panel catatan Gambar IV. 42 *Mockup * Formulir Catatan Sesi** **

• **Formulir Catatan Sesi**: Penilaian, ringkasan sesi, catatan kemajuan, tugas rumah, templat 





Gambar IV. 43 *Mockup * Riwayat Sesi** **

• **Riwayat Sesi**: Total sesi, cari & filter, tabel sesi, analitik Gambar IV. 44 *Mockup * Dasbor Pendapatan** **

• **Dasbor Pendapatan **: Saldo, grafik pendapatan, transaksi, penarikan, pengaturan pembayaran 





Gambar IV. 45 *Mockup* *Edit * Profil Terapis** **

• ***Edit *****Profil **: Tab untuk dasar / professional / tentang / Pendidikan / layanan 

/ media / pengaturan 

****

****

****





Gambar IV. 46 * Mockup * Pengaturan Terapis *** ***

• **Pengaturan Terapis **: Preferensi akun, keamanan, notifikasi 

****





Gambar IV. 47 *Mockup* Pesan Terapis** **

• **Pesan Terapis **: Daftar percakapan dengan klien, area obrolan Gambar IV. 48 *Mockup * Notifikasi Terapis 

• **Notifikasi Terapis **: Daftar notifikasi sistem, filter, tandai sebagai dibaca 

****

****

****





**5. *Dashboard *****Admin \(25 halaman\) :** Gambar IV. 49 *Mockup* Dasbor Admin - Dasbor Utama 

• **Dasbor Utama **: Metrik kunci, grafik pendapatan, reservasi terbaru, pertumbuhan pengguna, peringatan sistem 



Gambar IV. 50 *Mockup* Manajemen Reservasi 

• **Manajemen Reservasi **: Ringkasan statistik, tab \(semua / mendatang / 

lampau / tertunda / dibatalkan / sengketa\), tabel reservasi 





Gambar IV. 51 *Mockup* Manajemen Pengguna 

• **Manajemen Pengguna **: Tab \(semua/klien/terapis/admin/tertunda\), tabel pengguna, aksi massal 



Gambar IV. 52 * Mockup * Laporan Keuangan *** ***

• **Laporan Keuangan **: Ringkasan pendapatan, grafik, tabel transaksi, penarikan, pengembalian dana, analitik 





Gambar IV. 53 *Mockup* Pengaturan Sistem 

• **Pengaturan Sistem **: Navigasi kategori, umum / reservasi / pembayaran / 

email / keamanan / kebijakan / integrasi / lanjutan Gambar IV. 54 *Mockup * Notifikasi Admin 

• **Notifikasi Admin **: Daftar notifikasi sistem, filter berdasarkan tipe, tandai sebagai dibaca 





Gambar IV. 55 *Mockup* Pesan Admin 

• **Pesan Admin **: Daftar percakapan dengan pengguna, area obrolan, dukungan pelanggan 



Gambar IV. 56 *Mockup * Detail Pengguna 

• **Detail Pengguna **: Profil lengkap, riwayat aktivitas, statistik, aksi moderasi 

****

****

****





Gambar IV. 57 *Mockup* Edit Pengguna** **

• **Edit Pengguna **: Formulir edit data pengguna, ubah peran, status akun Gambar IV. 58 *Mockup* Detail Reservasi 

• **Detail Reservasi **: Informasi lengkap reservasi, timeline status, aksi admin 





Gambar IV. 59 *Mockup* Manajemen Transaksi** **

• **Manajemen Transaksi **: Daftar semua transaksi pembayaran, filter, ekspor laporan 



Gambar IV. 60 *Mockup * Manajemen Penarikan** **

• **Manajemen Penarikan **: Permintaan penarikan dana terapis, approval, riwayat 

****

****





Gambar IV. 61 *Mockup* Detail Penarikan** **

• **Detail Penarikan **: Informasi penarikan, verifikasi, bukti transfer Gambar IV. 62 *Mockup Log* Aktivitas 

• **Log Aktivitas **: Jejak audit sistem, filter berdasarkan pengguna/aksi/tanggal 





*Gambar IV. 63 Mockup Laporan & Analitik** ***

• **Laporan & Analitik **: Dashboard analitik lanjutan, berbagai jenis laporan, ekspor 





Gambar IV. 64 *Mockup* Manajemen Ulasan 

• **Manajemen Ulasan**: Daftar ulasan klien, moderasi, tanggapan, filter rating 

****





Gambar IV. 65 *Mockup* Manajemen Promo 

• **Manajemen Promo **: Daftar kode promo, buat/ *edit*/hapus, statistik penggunaan 



Gambar IV. 66 *Mockup* Verifikasi Terapis 

• **Verifikasi Terapis **: Daftar pendaftaran terapis baru, *review* dokumen, *approval/reject* 





Gambar IV. 67 *Mockup Editor Blog* 

• ***Editor Blog***** **: *Rich text editor* untuk membuat/ *edit * artikel blog, kategori, tag, SEO 



Gambar IV. 68 *Mockup* Manajemen Konten Blog** **

• **Manajemen Konten Blog **: Daftar artikel, status \( *draft*/ *published*\), aksi CRUD 





Gambar IV. 69 *Mockup Editor FAQ*** **

• ***Editor FAQ ***: Formulir untuk membuat/ *edit* pertanyaan dan jawaban FAQ, kategori 



Gambar IV. 70 *Mockup* Manajemen Konten FAQ** **

• **Manajemen Konten FAQ **: Daftar FAQ, kategori, urutan tampilan, aksi CRUD 

****

****

****

****





Gambar IV. 71 *Mockup Editor* Layanan** **

• ***Editor***** Layanan **: Formulir lengkap untuk membuat/ *edit * layanan terapi, harga, durasi 



Gambar IV. 72 * Mockup * Manajemen Konten Layanan** **

• **Manajemen Konten Layanan **: Daftar layanan, status aktif/nonaktif, aksi CRUD 

****

****

****

****

****





Gambar IV. 73 * Mockup Editor Promo** ***

• ***Editor Promo***** **: Formulir untuk membuat/ *edit* promosi, banner, periode aktif, target 



## **C. Fitur Desain Unggulan **

**Desain Responsif :** 

• Pendekatan *mobile-first* dengan *breakpoints* optimal 

• Adaptif untuk desktop \(1920px\), tablet \(768px\), dan mobile \(375px\) 

• *Touch-friendly* untuk perangkat mobile \(min 44x44px *tap targets*\) **Aksesibilitas :** 

• Memenuhi standar *WCAG 2.1 Level AA* 

• Rasio kontras warna minimal 4.5:1 untuk teks normal 

• Dukungan navigasi keyboard 

• Ramah *screen reader* dengan label *ARIA* yang tepat 

• Indikator fokus yang jelas 

**Pengalaman Pengguna :** 

• Pola navigasi konsisten di semua halaman 

• Tombol *call-to-action* yang jelas dengan hierarki 

• Status pemuatan dan *skeleton screens* 

• Status kesalahan dengan pesan membantu 



• Status berhasil dengan aksi selanjutnya yang jelas 

• Status kosong dengan panduan 

**Desain Visual :** 

• Spasi konsisten menggunakan skala spasi Tailwind \(unit dasar 4px\) 

• Hierarki tipografi yang jelas 

• Ikonografi menggunakan Heroicons \(SVG\) 

• Gambar dengan foto dan ilustrasi berkualitas tinggi 

• Interaksi mikro untuk pengalaman menyenangkan \( *hover states*, transisi, animasi\) 

**Desain Formulir :** 

• Label dan *placeholder* yang jelas 

• Validasi sebaris dengan pesan kesalahan yang membantu 

• Indikator kemajuan untuk formulir multi-langkah 

• Simpan otomatis draf untuk formulir panjang 

• Indikator bidang wajib \(\*\) 

**Visualisasi Data :** 

• Grafik menggunakan *Chart.js*/ *ApexCharts* 

• Palet ramah buta warna 

• *Tooltips* interaktif 

• Responsif untuk berbagai ukuran layar 

• Kemampuan ekspor \(PNG, SVG, PDF\) 

****

## **D. Prototype Interaktif **

**\[LINK - Figma Prototype : https://figma.com/proto/curheart...\]** 

Prototipe interaktif telah dibuat di Figma dengan fitur : 

• Navigasi *click-through* antar halaman 

• *Hover states* dan interaksi mikro 

• Simulasi validasi formulir 

• Pratinjau responsif untuk berbagai perangkat 

• Anotasi untuk *developer handoff* 

• Spesifikasi desain \(spasi, warna, tipografi\) 

• Pustaka komponen untuk dapat digunakan kembali 



**E. Design Handoff **

Dokumentasi lengkap untuk pengembang mencakup : 

• **Pustaka Komponen **: 50\+ komponen yang dapat digunakan kembali \(tombol, kartu, formulir, modal, tabel\) 

• **Token Desain **: Warna, tipografi, spasi, bayangan, *border-radius* 

• **Ekspor Aset **: Ikon \(SVG\), gambar \(WebP/PNG\), ilustrasi \(SVG\) 

• **Spesifikasi **: Detail spasi, ukuran, dan posisi 

• **Catatan Pengembang **: Panduan implementasi, dependensi, kasus tepi 

• **Daftar Periksa Aksesibilitas **: Persyaratan aksesibilitas per komponen **Ringkasan Desain UI/UX:** 

Total **66 halaman mockup** yang mencakup seluruh perjalanan pengguna dari 4 

peran berbeda \(Tamu, Klien, Terapis, Admin\). Rincian distribusi halaman: 

• **Halaman Publik**: 12 halaman \(landing, layanan, terapis, blog, kontak, FAQ, dll\) 

• **Halaman Autentikasi**: 4 halaman \(login, register, lupa password, reset password\) 

• ***Dashboard***** Klien **: 12 halaman \( *dashboard, booking flow 4 steps,* *appointments, progress, messages, settings, notifications*\) 

• ***Dashboard***** Terapis **: 13 halaman \( *dashboard, schedule, availability, clients,* *session room, notes, history, earnings, profile edit, settings, messages,* *notifications*\) 

• ***Dashboard***** Admin**: 25 halaman \( *dashboard, users, bookings*, *financial*, *content management, reviews, verification, reports*\) Semua mockup dirancang dengan prinsip : 

**Responsif **: Adaptif untuk desktop, tablet, dan mobile **Aksesibilitas **: Memenuhi standar *WCAG 2.1 AA* **Konsistensi **: Mengikuti sistem desain yang telah ditetapkan **Ramah Pengguna **: Intuitif dan mudah digunakan **Profesional **: Mencerminkan kredibilitas layanan kesehatan mental Desain telah melalui beberapa iterasi berdasarkan umpan balik dari pemangku kepentingan dan *usability testing* dengan sampel pengguna. 



**4.4. FAKTOR PENENTU KEBERHASILAN **

Keberhasilan implementasi Sistem Informasi CUR-HEART ditentukan oleh berbagai faktor yang saling berkaitan. Faktor-faktor ini dibagi menjadi Faktor Kunci Keberhasilan \( *Key Success Factors*/KSF\), Faktor Kritis Keberhasilan \( *Critical Success Factors*/CSF\), dan Indikator Kinerja Utama \( *Key Performance* *Indicators*/KPI\). 

**4.4.1. Faktor Kunci Keberhasilan \( *Key Success Factors*****/KSF\)** Faktor Kunci Keberhasilan adalah faktor-faktor kunci yang mendukung pencapaian tujuan proyek secara umum. 

***A. Faktor Teknologi ***

## **1. Stabilitas dan Keandalan Sistem**

• Sistem harus mampu beroperasi 24/7 dengan *uptime* minimal 99,5% 

• Waktu respons halaman tidak lebih dari 2 detik 

• Optimasi *query database* untuk menangani pengguna bersamaan \( *concurrent users*\) 

• Cadangan \( *backup*\) otomatis harian untuk keamanan data **2. Antarmuka yang Mudah Digunakan** 

• Desain UI/UX yang intuitif dan mudah dipahami 

• Desain responsif \( *responsive design*\) untuk semua perangkat \(desktop, tablet, mobile\) 

• Konsistensi bahasa desain menggunakan sistem desain \( *design system*\) 

• Standar aksesibilitas \(WCAG 2.1 Level AA\) 

## **3. Keamanan Data**

• Enkripsi data sensitif \(kata sandi/ *password*, rekam medis/ *medical records*\) 

• HTTPS untuk semua komunikasi 

• Autentikasi dan otorisasi yang kuat 

• Kepatuhan terhadap UU PDP \(Perlindungan Data Pribadi\) **4. Skalabilitas** 

• Arsitektur yang dapat menangani pertumbuhan pengguna 

• Normalisasi basis data untuk efisiensi penyimpanan \( *storage*\) 

• Mekanisme *caching* untuk optimasi kinerja 



***B. Faktor Manusia ***

## **1. Kompetensi Tim Pengembang**

• Penguasaan *framework* Laravel dan pemrograman PHP 

• Pemahaman desain basis data dan MySQL 

• Kemampuan pengembangan *frontend* \(HTML, CSS, JavaScript, Tailwind\) 

• Pengetahuan kontrol versi/ *version control* \(Git\) **2. Komitmen Pemangku Kepentingan** 

• Dukungan penuh dari manajemen CUR-HEART 

• Keterlibatan aktif pemilik dalam pengumpulan kebutuhan 

• Umpan balik konstruktif dari terapis dan admin 

• Kesediaan untuk pengujian dan UAT \( *User Acceptance Testing*\) **3. Tingkat Adopsi Pengguna** 

• Pelatihan yang memadai untuk terapis dan admin 

• Panduan pengguna yang komprehensif 

• Dukungan teknis yang responsif 

• Manajemen perubahan yang efektif 

***C. Faktor Manajemen Proyek ***

## **1. Perencanaan yang Matang**

• Ruang lingkup yang jelas dan terukur 

• Jadwal yang realistis \(11 minggu\) 

• Alokasi sumber daya yang optimal 

• Strategi mitigasi risiko yang efektif 

## **2. Komunikasi yang Efektif**

• Pertemuan rutin mingguan \( *weekly standup*\) 

• Dokumentasi yang jelas 

• Pelacakan kemajuan dengan diagram Gantt \( *Gantt chart*\) 

• Pelacakan isu dan penyelesaian 

## **3. Jaminan Kualitas**

• Pengujian sistematis di setiap fase 

• Tinjauan kode dan pemrograman berpasangan \( *pair programming*\) 

• Pelacakan bug dan prioritas perbaikan 

• Perbaikan berkelanjutan berdasarkan umpan balik 



**4.4.2. Faktor Kritis Keberhasilan \( *Critical Success Factors*****/CSF\)** Faktor Kritis Keberhasilan adalah faktor-faktor yang **HARUS** dipenuhi agar proyek berhasil. 

**CSF 1 : Ketersediaan dan Keandalan Sistem** 

• Target: Waktu aktif \( *uptime*\) ≥ 99,5%, Waktu respons < 2 detik 

• Dapat menangani minimal 100 pengguna bersamaan 

• Tidak ada kehilangan data dalam kondisi normal 

**CSF 2 : Keamanan dan Privasi Data** 

• Tidak ada pelanggaran keamanan atau akses tidak sah 

• Semua data sensitif terenkripsi 

• Implementasi HTTPS untuk semua halaman 

• *RBAC* \( *Role-Based Access Control*\) berfungsi dengan baik **CSF 3 : Adopsi dan Kepuasan Pengguna** 

• Minimal 70% klien menggunakan sistem untuk reservasi 

• Skor kepuasan pengguna ≥ 4,0 dari 5,0 

• Skor SUS \( *System Usability Scale*\) ≥ 68 

• Tingkat adopsi terapis 100% 

**CSF 4 : Integrasi dengan Proses Bisnis** 

• 100% reservasi melalui sistem \(tidak ada lagi manual\) 

• Pengurangan beban kerja administratif minimal 50% 

• Pengurangan kesalahan reservasi hingga 90% 

• Laporan dapat dihasilkan dalam 5 menit 

**CSF 5 : Kepatuhan Anggaran dan Jadwal** 

• Penyelesaian proyek dalam 11 minggu \(± 1 minggu toleransi\) 

• Biaya aktual tidak melebihi 110% anggaran \(Rp 5,5 juta\) 

• Semua luaran selesai sesuai ruang lingkup 

**4.4.3. Indikator Kinerja Utama \( *Key Performance Indicators*****/KPI\)** KPI adalah metrik terukur untuk memantau keberhasilan sistem setelah penerapan. 





**Tabel 4.8 - Key Performance Indicators \(KPI\)** **Frekuensi **

**Kategori **

**Nama KPI **

**Target **

## **Pemantauan **

### Waktu Aktif Sistem 

Waktu nyata 

≥ 99,5% 

\( *Uptime*\) 

\( *real-time*\) 

## **Kinerja **

### Waktu Respons 

≤ 2 detik 

Mingguan 

## **Sistem**

Tingkat Galat \( *Error *

≤ 0,5% 

Harian 

*Rate*\) 

Kerentanan Keamanan 

0 kritis 

Bulanan 

\( *Security Vulnerabilities*\) 

## **Keamanan**

### Insiden Pelanggaran Data 

Waktu nyata 

0 

\( *Data Breach Incidents*\) 

\( *real-time*\) 

200 dalam 

Total Pengguna Terdaftar 

Bulanan 

3 bulan 

Pengguna Aktif Bulanan 

## **Adopsi **

150 \(75%\) 

Bulanan 

\( *Monthly Active Users*\) 

## **Pengguna**

### Tingkat Konversi 

Reservasi \( *Conversion *

≥ 60% 

Mingguan 

*Rate*\) 

100 

Total Reservasi/Bulan 

Bulanan 

reservasi 

Tingkat Keberhasilan 

## **Transaksi**

Pembayaran \( *Payment *

≥ 95% 

Mingguan 

*Success Rate*\) 

Pendapatan/Bulan 

Rp 30 juta 

Bulanan 

## **Kepuasan**

### Skor Kepuasan Pengguna 

≥ 4,0/5,0 

Per reservasi 



**Frekuensi **

**Kategori **

**Nama KPI **

**Target **

## **Pemantauan **

Skor NPS \( *Net Promoter *

≥ 30 

Triwulanan 

*Score*\) 

Skor SUS \( *System *

≥ 68 

Triwulanan 

*Usability Scale*\) 

Rata-rata Waktu 

≤ 3 menit 

Mingguan 

Reservasi 

Pengurangan Beban Kerja 

## **Efisiensi**

≥ 50% 

Bulanan 

Admin 

Waktu Pembuatan 

≤ 5 menit 

Bulanan 

Laporan 



## **4.5. KEUNTUNGAN YANG DIHARAPKAN **

Implementasi Sistem Informasi CUR-HEART diharapkan memberikan berbagai keuntungan bagi pemangku kepentingan yang terlibat. 

**4.5.1. Manfaat untuk CUR-HEART \(Organisasi\) **

## **A. Efisiensi Operasional **

• **Proses reservasi otomatis **: Pengurangan waktu dari 10-15 menit menjadi 3 menit per reservasi, penghematan sekitar 20 jam per bulan 

• **Manajemen penjadwalan **: Koordinasi jadwal berkurang dari 5 jam per minggu menjadi 1 jam, utilisasi meningkat dari 60% menjadi 80% 

• **Pelaporan otomatis **: Waktu pembuatan laporan dari 2 jam menjadi 5 

menit, penghematan 8 jam per bulan 

• **Eliminasi reservasi ganda **: Konflik jadwal turun dari 8-10 kasus per bulan menjadi 0 kasus 

## **B. Pertumbuhan Pendapatan **

• **Peningkatan volume reservasi **: Target \+25% dari 80 menjadi 100 

reservasi per bulan \(Rp 72 juta/tahun tambahan\) 



• **Pengurangan tidak hadir **: Dari 15% menjadi 5% dengan pengingat otomatis \(Rp 28,8 juta/tahun pendapatan dipulihkan\) 

• **Perpanjangan jam layanan **: Reservasi 24/7 menangkap 15% lebih banyak klien \(Rp 10 juta/tahun\) 

• **Retensi klien **: Peningkatan dari 35% menjadi 60% dengan pengalaman yang lebih baik 

**C. Kualitas & Layanan **

• **Pengambilan keputusan berbasis data **: Dasbor waktu nyata untuk analisis cepat 

• **Pemantauan kualitas **: Sistematis dengan target SUS ≥ 68, NPS ≥ 30 

• **Skalabilitas **: Sistem digital dapat mendukung pertumbuhan 5× tanpa tambahan staf 

**Total Manfaat Tahunan Terukur :** 

• Peningkatan Pendapatan : Rp 115,8 juta/tahun 

• Penghematan Biaya : Rp 18,4 juta/tahun 

• **TOTAL **: Rp 134,2 juta/tahun 

**4.5.2. Manfaat untuk Klien **

## **A. Kenyamanan **

• Reservasi 24/7 kapan saja tanpa terbatas jam kantor 

• Tidak perlu telepon, layanan mandiri daring 

• Ramah perangkat seluler untuk reservasi saat bepergian 

• Penjadwalan ulang mudah tanpa koordinasi manual **B. Transparansi **

• Profil terapis lengkap dengan pendidikan, spesialisasi, dan ulasan 

• Ketersediaan waktu nyata dengan kalender visual 

• Harga transparan per layanan 

• Sistem rating & ulasan untuk memilih terapis terbaik **C. Layanan Mandiri **

• Akses riwayat janji temu lengkap 

• Lihat catatan sesi yang dibagikan terapis 

• Pelacakan kemajuan terapi dengan grafik visual 

• Pengingat otomatis untuk sesi mendatang 



**Nilai untuk Klien :** 

• Penghematan waktu : 25-55 menit per reservasi 

• Target kepuasan : ≥ 4,0/5,0, SUS ≥ 68 

• Retensi meningkat : 35% → 60% 

**4.5.3. Manfaat untuk Terapis **

## **A. Penghematan Waktu **

• Manajemen jadwal mandiri mengurangi koordinasi dengan admin 

• Hemat 16 jam per bulan untuk administrasi 

• Dokumentasi sesi digital lebih cepat \(5 menit vs 15 menit\) **B. Potensi Pendapatan **

• Utilisasi lebih baik dari 60% → 80% 

• Peningkatan pendapatan \+33% \(Rp 5 juta/bulan\) 

• Akses ke analytics kinerja pribadi 

**C. Keseimbangan Kerja-Hidup **

• Otonomi dan fleksibilitas dalam mengatur jadwal 

• Beban administratif berkurang signifikan 

• Target kepuasan terapis: ≥ 4,5/5,0 

**4.5.4. Analisis Laba atas Investasi \( *Return on Investment*****/ROI\)** **Investasi:** 

• Biaya awal: Rp 3.000.000 \(pengaturan/ *setup*\) 

• Biaya berulang tahun 1: Rp 9.750.000 \( *hosting*, domain, *payment* *gateway*\) 

• **Total biaya tahun 1: Rp 12.750.000** 

**Manfaat Tahun 1:** 

• Peningkatan pendapatan: Rp 142.800.000 

• Penghematan biaya: Rp 26.400.000 

• **Total manfaat: Rp 169.200.000** 

**Hasil:** 

• Manfaat bersih: Rp 156.450.000 

• **ROI: 1.227%** 

• **Periode pengembalian \( *payback period*****\): 0,9 bulan \(~27 hari\)** 

• Rasio Manfaat-Biaya: 13,3:1 



**Proyeksi 5 Tahun:** 

• Total manfaat: Rp 1.025.481.825 

• Total biaya: Rp 60.098.000 

• Manfaat bersih: Rp 964.383.829 

• ROI 5 tahun: 7.258% 

**Rekomendasi:** Proyek sangat layak dengan ROI luar biasa dan periode pengembalian \( *payback period*\) sangat singkat. 



## **4.6. TEKNOLOGI YANG DIGUNAKAN **

Teknologi yang digunakan untuk membangun Sistem Informasi CUR-HEART 

secara garis besar dapat dibagi ke dalam beberapa bagian berikut ini: **4.6.1 Server dan Infrastruktur **

**A. *Web Server*** 

• **Nginx 1.18.0**: *Web server* berkinerja tinggi untuk menangani koneksi bersamaan \( *concurrent connections*\) 

• **PHP 8.1**: Bahasa pemrograman sisi server \( *server-side scripting* *language*\) dengan fitur modern \(kompilator *JIT*, argumen bernama/ *named* *arguments*, atribut/ *attributes*\) 

**B. *Hosting*** 

• **VPS \( *Virtual Private Server*****\)**: Ubuntu Server 22.04 LTS 

• Spesifikasi: 4 vCPU, 8GB RAM, 160GB Penyimpanan SSD \( *SSD *

*Storage*\) 

• SLA Waktu Aktif \( *Uptime SLA*\): 99,9% 

• *Bandwidth*: Tidak terbatas \( *Unlimited*\) **C. Server Basis Data** 

• **MySQL 8.0**: Sistem manajemen basis data relasional 

• *Storage Engine*: InnoDB untuk kepatuhan *ACID* 

• *Backup*: Cadangan otomatis harian dengan retensi 30 hari **D. Kontrol Versi** 

• **Git & GitHub**: Manajemen kode sumber dan kolaborasi **4.6.2 Backend Development **

**A. *Framework***** & Bahasa** 



• **Laravel 10**: *Framework* PHP modern dengan arsitektur MVC 

o *Eloquent ORM* untuk abstraksi basis data o *Blade templating engine* 

o *Middleware* untuk autentikasi & otorisasi o Sistem antrian untuk pekerjaan latar belakang 

o *Event* & *listener* untuk operasi asinkron **B. Autentikasi & Otorisasi** 

• Laravel Sanctum untuk autentikasi token API 

• Laravel Permission \(Spatie\) untuk kontrol akses berbasis peran/ *role-based* *access control* \(RBAC\) 

• Bcrypt untuk *hashing* kata sandi 

**C. Pustaka \( *Libraries*****\) & Paket \( *Packages*****\)** 

• Midtrans PHP SDK untuk integrasi *payment gateway* 

• Laravel Mail untuk notifikasi email 

• Carbon untuk manipulasi tanggal/waktu 

• Intervention Image untuk pemrosesan gambar 

**4.6.3 Pengembangan *Frontend***** **

## **A. Teknologi**

• **HTML5**: *Markup* semantik modern 

• **CSS3**: *Styling* dengan *flexbox* dan *grid* 

• **JavaScript \(ES6\+\)**: Interaktivitas dan konten dinamis 

• **Alpine.js**: *Framework* JavaScript ringan untuk komponen reaktif **B. *Framework***** CSS** 

• **Tailwind CSS 3.3**: *Framework* CSS berbasis utilitas \( *utility-first*\) o Desain responsif dengan pendekatan *mobile-first* o Palet warna dan tipografi kustom 

o Kompilator *JIT* \( *Just-In-Time*\) untuk optimasi o *PurgeCSS* untuk menghapus *styles* yang tidak digunakan **C. Komponen UI** 

• Pustaka komponen kustom berbasis Tailwind 

• Ikon: Heroicons \(set ikon SVG\) 



• Validasi formulir: Sisi klien \( *client-side*\) dengan JavaScript \+ sisi server \( *server-side*\) Laravel 

**4.6.4 Manajemen Basis Data **

## **A. Manajemen Basis Data**

• **MySQL 8.0**: Basis data utama 

• Set Karakter \( *Character Set*\): utf8mb4 untuk dukungan Unicode penuh 

• *Collation*: utf8mb4\_unicode\_ci 

## **B. Desain Basis Data**

• 16 tabel dengan normalisasi 3NF 

• Batasan kunci asing \( *foreign key*\) untuk integritas referensial 

• Indeks pada kolom yang sering di- *query* 

• *Timestamps* untuk jejak audit 

**C. Migrasi & *Seeding*** 

• Laravel *Migrations* untuk kontrol versi skema basis data 

• *Seeders* untuk data sampel dan data pengujian **4.6.5 Integrasi & Layanan **

## **Eksternal **

**A. *Payment Gateway*** 

• **Midtrans**: *Payment gateway* terintegrasi o *Snap API* untuk proses pembayaran \( *checkout*\) yang mulus o Dukungan: Kartu kredit, Transfer bank, Dompet digital \(GoPay, OVO, Dana\) 

o Keamanan: Memenuhi standar *PCI-DSS* 

o *Webhook* untuk notifikasi pembayaran 

## **B. Layanan Email**

• **SMTP \(Mailtrap/SendGrid\)**: Layanan pengiriman email o Email notifikasi \(konfirmasi reservasi, pengingat\) o Email transaksional \(reset kata sandi, email selamat datang\) o Berbasis antrian untuk menghindari pemblokiran 

## **C. Penyimpanan Berkas**

• Penyimpanan lokal untuk pengembangan 

• AWS S3 / DigitalOcean Spaces \(siap untuk skala produksi\) 



**4.6.6 Peralatan Pengembangan **

## **A. Kontrol Versi**

• **Git**: Sistem kontrol versi terdistribusi 

• **GitHub**: *Hosting* repositori jarak jauh 

• Strategi percabangan \( *branching*\): *GitFlow* \( *main*, *develop*, *feature* *branches*\) 

**B. Editor Kode & IDE** 

• Visual Studio Code dengan ekstensi: 

o Laravel Extension Pack 

o PHP Intelephense 

o Tailwind CSS IntelliSense 

o ESLint & Prettier 

## **C. Manajer Paket**

• **Composer**: Manajemen dependensi PHP 

• **NPM**: Manajemen paket JavaScript 

## **4.6.7 Pengujian **

**A. *Framework***** Pengujian** 

• **PHPUnit**: Pengujian unit \( *unit testing*\) untuk logika *backend* 

• **Laravel Dusk**: Pengujian otomasi peramban \( *browser*\) 

• Pengujian fitur untuk titik akhir \( *endpoint*\) API **B. Kualitas Kode** 

• PHP Code Sniffer untuk standar pengodean 

• Laravel Debugbar untuk pengawakutuan \( *debugging*\) pengembangan 

• Pelacakan kesalahan \( *error tracking*\) & pemantauan \( *monitoring*\) **4.6.8 Penerapan \( *Deployment*****\) **

**& *DevOps***** **

**A. Penerapan \( *Deployment*****\)** 

• **GitHub Actions**: Otomasi CI/CD 

• Pengujian otomatis sebelum penerapan 

• Strategi penerapan tanpa *downtime* \( *zero-downtime deployment*\) **B. Pemantauan \( *Monitoring*****\)** 

• **UptimeRobot**: Pemantauan waktu aktif \( *uptime monitoring*\) 



• **New Relic / Laravel Telescope**: Pemantauan kinerja aplikasi \( *application* *performance monitoring*\) 

• Pencatatan kesalahan \( *error logging*\) dengan Laravel Log **C. Keamanan** 

• **Let's Encrypt**: Sertifikat SSL/TLS gratis 

• HTTPS ditegakkan untuk semua koneksi 

• Perlindungan CSRF \(bawaan Laravel\) 

• Pencegahan XSS 

• Pencegahan injeksi SQL \( *SQL injection*\) \(Eloquent ORM\) 

• Pembatasan laju \( *rate limiting*\) untuk titik akhir \( *endpoint*\) API **4.6.9 Desain & Pembuatan **

## **Prototipe **

**A. Desain UI/UX** 

• **Figma**: Peralatan desain untuk *wireframes* dan *mockups* 

• 66 halaman *mockup* untuk semua peran pengguna 

• Sistem desain dengan palet warna dan tipografi 

## **B. Peralatan Diagram**

• **Draw.io / Lucidchart**: ERD, *Use Case*, Diagram Aktivitas 

• **StarUML**: Diagram kelas dan diagram sekuens **4.6.10 Manajemen Proyek **

## **A. Perencanaan**

• **Microsoft Project / GanttProject**: Diagram Gantt dan WBS 

• **Trello / Notion**: Manajemen tugas dan kolaborasi **B. Dokumentasi** 

• **Markdown**: Dokumentasi teknis 

• **Swagger / Postman**: Dokumentasi API 

**4.6.11 Ringkasan Stack **

## **Teknologi **

┌─────────────────────────────────────────┐ 

│ Klien \(Peramban\) │ 

│ HTML5 | CSS3 | JavaScript | Alpine.js │ 

│ Tailwind CSS │ 



└─────────────┬───────────────────────────┘ 

│ HTTPS 

┌─────────────▼───────────────────────────┐ 

│ Web Server \(Nginx\) │ 

└─────────────┬───────────────────────────┘ 

│ 

┌─────────────▼───────────────────────────┐ 

│ Aplikasi \(Laravel 10 \+ PHP 8.1\) │ 

│ MVC | Eloquent ORM | Blade Templates │ 

│ Middleware | Queue | Events │ 

└─────┬───────────────────────────┬───────┘ 

│ │ 

▼ ▼ 

┌─────────────┐ ┌────────────────┐ 

│ Basis Data │ │ API Eksternal │ 

│ MySQL 8.0 │ │ - Midtrans │ 

│ 16 Tabel │ │ - Email SMTP │ 

└─────────────┘ └────────────────┘ 

**4.6.12 Alasan Pemilihan **

## **Teknologi **

**Tabel 4.9 - Justifikasi Pemilihan Teknologi** 

**Teknologi **

## **Alasan Pemilihan **

*Framework* PHP terpopuler dengan ekosistem lengkap, **Laravel 10** 

dokumentasi sangat baik, dukungan komunitas kuat, dan fitur bawaan yang komprehensif 

Basis data relasional yang matang, andal, didukung luas, dan **MySQL 8.0** 

gratis \( *open source*\) 

Produktivitas tinggi, ukuran berkas kecil setelah *purge*, **Tailwind **

sangat dapat disesuaikan \( *highly customizable*\), dan **CSS** 

pembuatan prototipe cepat \( *rapid prototyping*\) 



**Teknologi **

## **Alasan Pemilihan **

Kombinasi berkinerja tinggi untuk aplikasi lalu lintas tinggi **Nginx \+ **

\( *high-traffic applications*\) dengan jejak memori rendah **PHP 8.1** 

\( *memory footprint*\) 

*Payment gateway* lokal Indonesia dengan kepatuhan **Midtrans** 

\( *compliance*\) dan dukungan terbaik, mendukung berbagai metode pembayaran lokal 

Alternatif ringan untuk Vue/React, cocok untuk aplikasi **Alpine.js** 

yang tidak terlalu kompleks 

Standar industri untuk desain UI/UX dengan fitur kolaborasi **Figma** 

yang sangat baik 

*Hosting* kontrol versi paling populer dengan integrasi CI/CD 

## **GitHub**

### yang mudah 



## **4.7. DESIMINASI PROYEK **

Desiminasi proyek merupakan proses penyebarluasan hasil, pengetahuan, dan pembelajaran dari proyek pengembangan Sistem Informasi CUR-HEART kepada berbagai pihak yang berkepentingan. Tujuan desiminasi adalah untuk memaksimalkan manfaat proyek, berbagi pengetahuan, dan memungkinkan replikasi sistem di tempat lain. 

**4.7.1 Tujuan Desiminasi **

## **A. Berbagi Pengetahuan**

• Berbagi pengetahuan dan praktik terbaik dalam pengembangan sistem informasi kesehatan mental 

• Memberikan pembelajaran tentang implementasi Laravel untuk manajemen layanan kesehatan \( *healthcare management*\) 

• Dokumentasi proses dan tantangan yang dihadapi selama pengembangan **B. Peningkatan Kesadaran** 



• Meningkatkan kesadaran tentang pentingnya digitalisasi layanan kesehatan mental 

• Menunjukkan manfaat sistem informasi untuk efisiensi operasional 

• Mempromosikan adopsi teknologi di sektor kesehatan mental **C. Replikasi dan Skalabilitas** 

• Memungkinkan pusat terapi lain untuk mengadopsi sistem serupa 

• Menyediakan dokumentasi lengkap untuk implementasi 

• Berbagi pembelajaran yang diperoleh untuk menghindari kesalahan yang sama 

**4.7.2 Target Audiens Desiminasi **

## **A. Pemangku Kepentingan Internal**

• Tim manajemen CUR-HEART 

• Terapis dan staf administratif 

• Pemilik bisnis 

## **B. Akademik**

• Dosen pembimbing dan penguji 

• Mahasiswa Program Studi Sistem Informasi 

• Sivitas akademika Universitas Nusa Mandiri 

## **C. Eksternal**

• Praktisi hipnoterapi dan kesehatan mental 

• Pusat terapi dan *wellness center* lainnya 

• Komunitas pengembang \( *developer*\) Laravel Indonesia 

• Pihak yang tertarik dengan sistem informasi kesehatan \( *health information* *system*\) 

**4.7.3 Metode Desiminasi **

## **A. Publikasi Akademik**

**1. Laporan *Capstone Project*** 

• Laporan lengkap BAB I - BAB V 

• Dokumentasi teknis \(SRS, Dokumen Desain/ *Design Document*\) 

• Panduan pengguna dan panduan admin 

• Kode sumber dengan dokumentasi lengkap 

• Format: PDF dan Salinan Cetak 



**2. Presentasi Akademik** 

• Presentasi akhir di hadapan dosen pembimbing dan penguji 

• Slide presentasi dengan demonstrasi sistem langsung 

• Sesi tanya jawab untuk diskusi mendalam 

• Durasi: 30-45 menit 

**B. Dokumentasi dan Repositori** 

## **1. Repositori GitHub**

• Kode sumber lengkap dengan README.md komprehensif 

• Panduan instalasi bertahap 

• Dokumentasi API 

• Dokumentasi skema basis data 

• Panduan kontribusi 

• Lisensi: MIT \(sumber terbuka/ *open source*\) **2. Dokumentasi Teknis** 

• Diagram arsitektur sistem 

• ERD basis data dengan penjelasan 

• Dokumentasi titik akhir \( *endpoint*\) API 

• Panduan penerapan \( *deployment*\) 

• Panduan pemecahan masalah \( *troubleshooting*\) 

• Format: Markdown \+ PDF 

**C. Pameran Ilmiah \( *Science Exhibition*****\)** **1. Persiapan Materi dan Konten Pameran** 

• **Penyusunan Materi Pameran**: Siapkan konten visual dan materi lain yang diperlukan untuk menjelaskan hasil proyek secara menarik. Materi ini dapat berupa poster, infografis, video, atau simulasi interaktif. 

• **Prototipe atau Produk Jadi**: Jika proyek menghasilkan produk fisik, sistem, atau aplikasi, pastikan prototipe tersebut siap dipamerkan dan dapat berfungsi dengan baik. 

• **X-Banner dan Desain *Stand***: Rancang *stand* pameran yang menarik, termasuk x-banner dengan ukuran 60 X 160 cm yang berisi elemen grafis berikut: 

o Judul *Project* 



o Logo Universitas Nusa Mandiri 

o Logo Kampus Digital Bisnis 

o Nama kelompok dan dosen pengampu mata kuliah 

o Latar belakang project 

o Tujuan 

o Metodologi 

o Hasil utama 

o Keunggulan proyek 

o Manfaat proyek 

o QR \( *barcode* kuesioner penilaian persepsi masyarakat\) o Gambar visualisasi pendukung 

o Link *youtube video* promosi hasil proyek 

• **Alat Peraga Interaktif**: Siapkan alat peraga interaktif seperti perangkat lunak yang dapat dicoba pengunjung, model fisik, atau demo langsung dari hasil proyek untuk menarik minat audiens. 

**2. Pelaksanaan Pameran \( *Exhibition*****\)** 

• **Presentasi dan Demonstrasi**: Pada hari pameran, siapkan tim untuk memberikan presentasi singkat atau menjelaskan langsung kepada pengunjung mengenai proyek. Demonstrasi atau sesi tanya jawab interaktif dengan pengunjung sangat penting untuk menjelaskan manfaat dan keunggulan proyek. 

• **Brosur dan Materi Pendukung**: Sediakan materi cetak seperti brosur atau katalog yang bisa dibawa pulang oleh pengunjung sebagai panduan dan informasi lebih lanjut mengenai proyek. 

**3. Interaksi dengan Pengunjung \( *Visitor Engagement*****\)** 

• **Umpan Balik Pengunjung**: Sediakan mekanisme bagi pengunjung untuk memberikan umpan balik, baik melalui kuesioner, buku tamu, atau secara digital melalui aplikasi. Umpan balik ini bisa sangat berguna untuk evaluasi dan pengembangan lebih lanjut. 

## **4. Dokumentasi**

• **Fotografi dan Videografi**: Rekam momen penting selama pameran, seperti interaksi dengan pengunjung, presentasi, dan demonstrasi proyek. 



Dokumentasi ini bisa digunakan untuk promosi lebih lanjut atau laporan kepada pemangku kepentingan. 

**D. Publikasi Video Promosi/Campaign** 

## **1. Video Promosi**

• Durasi: 3-5 menit untuk diunggah di YouTube 

• Durasi pendek: 1 menit maksimal untuk media sosial 

• Resolusi minimal: 1080 Pixel 

• Konten: Visual, musik, *voice over*, teks, subtitle 

• Format: mp4 atau format video umum untuk media sosial **2. Isi Konten Video Promosi** 

• Pembukaan dengan logo Universitas Nusa Mandiri 

• Logo Kampus Digital Bisnis 

• Nama kelompok dan dosen pengampu mata kuliah 

• Latar belakang project 

• Tujuan 

• Solusi yang ditawarkan 

• Keunggulan dan inovasi 

• Manfaat 

• Dampak proyek 

• Simulasi prototipe dan penutup 

## **E. Pelatihan Internal**

### Pelatihan untuk pemangku kepentingan CUR-HEART: 

• Pelatihan pengguna untuk terapis \(2 jam\) 

• Pelatihan admin \(2 jam\) 

• Ikhtisar manajemen \(1 jam\) 

• Materi: Slide \+ praktik langsung 

• Dokumentasi video pelatihan 

**F. Media Daring** 

## **1. Artikel Blog**

• Medium.com atau Dev.to 

• Topik: 

o "Membangun Sistem Manajemen Kesehatan dengan Laravel 10" 



o "Mengintegrasikan *Payment Gateway* Midtrans di Laravel" 

o "Desain UI/UX untuk Layanan Kesehatan Mental" 

• Format: Tutorial bertahap dengan cuplikan kode \( *code snippets*\) **2. Media Sosial** 

• Posting LinkedIn tentang penyelesaian proyek 

• Utas \( *thread*\) Twitter tentang pembelajaran kunci 

• Infografis Instagram tentang hasil proyek 

## **4.7.4. Luaran Desiminasi **

**Tabel 4.10 - Luaran Desiminasi Proyek** 

**Target **

**No **

**Luaran **

**Format **

**Waktu **

**Status **

## **Audiens **

Laporan *Ca*

PDF \+ 

Desember 

1 

*pstone *

Salinan 

Akademik 

Selesai 

2025 

*Project* 

Cetak 

X-Banner 

dan 

Cetak 

Desember 

2 

Publik 

Selesai 

Desain *Stan*

60x160 cm 

2025 

*d* Pameran 

Video 

MP4 \(3-5 

Desember 

3 

Promosi/ *Ca*

menit \+ 1 

Publik 

Selesai 

2025 

*mpaign* 

menit\) 

Sivitas 

Pameran 

*Stand* Intera

Desember 

Terjad

4 

Akademika 

Ilmiah 

ktif \+ Demo 

2025 

wal 

\+ Publik 

*Slide* \+ 

Dosen 

Presentasi 

Desember 

Terjad

5 

Demonstras

Pembimbin

Akhir 

2025 

wal 

i 

g/Penguji 



**Target **

**No **

**Luaran **

**Format **

**Waktu **

**Status **

## **Audiens **

### Penilaian 

Kuesioner 

Desember 

6 

Persepsi 

*Google *

Publik 

Siap 

2025 

Masyarakat 

*Form* 

Repositori 

Desember 

7 

Kode 

GitHub 

Publik 

Siap 

2025 

Sumber 

Dokumentas

Markdown 

Pengemban

Desember 

8 

Selesai 

i Teknis 

\+ PDF 

g 

2025 

Panduan 

Pengguna 

Desember 

9 

PDF 

Selesai 

Pengguna 

Akhir 

2025 

Materi 

*Slide* \+ 

Staf CUR-

Januari 

Direnc

10 

Pelatihan 

Video 

HEART 

2026 

anakan 

Komunitas 

Medium/De

Januari 

Direnc

11 

Artikel Blog 

Pengemban

v.to 

2026 

anakan 

g 

**4.7.5 Jadwal dan Rencana **

## **Pelaksanaan Desiminasi **

**A. Pelaksanaan Desiminasi Akademik \(Pertemuan 13-16\)** Sesuai dengan pedoman *Capstone Project*, pelaksanaan desiminasi dilakukan pada **Pertemuan 13-16**: 

• **Pertemuan 13**: Promosi Hasil *Capstone Project* \(YouTube / Media Sosial\) dan Penilaian Persepsi masyarakat melalui kuesioner *Google Form* 

• **Pertemuan 14**: Pelaksanaan Pameran Ilmiah o Persiapan *stand* pameran dengan X-Banner \(60 x 160 cm\) o Penyiapan alat peraga interaktif \(demo sistem CUR-HEART\) o Penyediaan brosur dan materi pendukung 

o Presentasi dan demonstrasi kepada pengunjung 



o Pengumpulan umpan balik melalui kuesioner o Dokumentasi foto dan video 

• **Pertemuan 15**: Presentasi di hadapan Dosen Pengampu Mata Kuliah/Dosen Pembimbing 

o Presentasi hasil proyek secara keseluruhan 

o Demonstrasi sistem yang telah dikembangkan 

o Sesi tanya jawab 

o Penilaian oleh dosen 

• **Pertemuan 16**: Penilaian Akhir oleh Dosen Pengampu Mata Kuliah/Dosen Pembimbing 

## **B. Kegiatan Pendukung**

• **Januari 2025**: Pelatihan internal untuk staf CUR-HEART dan publikasi artikel blog di Medium/Dev.to 

**4.7.6 Indikator Keberhasilan **

## **Desiminasi **

**A. Jangkauan \( *Reach*****\)** 

• Pengunjung pameran ilmiah: Minimal 50 pengunjung 

• Tampilan video promosi YouTube: Target 100\+ tampilan dalam 1 bulan 

• Responden kuesioner persepsi masyarakat: Minimal 30 responden 

• Bintang repositori GitHub: Target 50\+ bintang dalam 6 bulan 

• Tampilan artikel blog: Target 500\+ tampilan 

**B. Keterlibatan \( *Engagement*****\)** 

• Skor penilaian persepsi masyarakat: ≥ 4,0/5,0 

• Interaksi pengunjung di *stand* pameran: Minimal 30 interaksi bermakna 

• Isu/diskusi \( *issues/discussions*\) GitHub: Keterlibatan komunitas aktif 

• Komentar blog dan keterlibatan media sosial 

• Skor umpan balik pelatihan: ≥ 4,0/5,0 

• Partisipasi \( *participation*\) tanya jawab di presentasi **C. Dampak \( *Impact*****\)** 

• Penilaian dosen: Minimal nilai B untuk presentasi 

• Transfer pengetahuan: Staf CUR-HEART dapat mengoperasikan sistem secara mandiri 



**D. Kualitas Luaran** 

• Kelengkapan dokumentasi: 100% sesuai pedoman 

• Kualitas X-Banner: Memenuhi semua elemen yang dipersyaratkan 

• Kualitas video promosi: Memenuhi spesifikasi teknis \(1080p, durasi sesuai\) 

• Kelengkapan materi pameran: Semua komponen tersedia dan fungsional **4.7.7 Pembelajaran yang **

**Diperoleh dan Praktik Terbaik **

## **A. Pembelajaran Teknis**

• Laravel 10 sangat cocok untuk sistem manajemen kesehatan 

• Integrasi Midtrans mudah dengan dokumentasi yang baik 

• Tailwind CSS secara signifikan mempercepat pengembangan *frontend* 

• Figma esensial untuk penyelarasan dengan pemangku kepentingan **B. Pembelajaran Manajemen Proyek** 

• Komunikasi yang sering dengan pemangku kepentingan sangat penting untuk kesuksesan 

• Pengembangan iteratif lebih efektif daripada model air terjun \( *waterfall*\) 

• UAT harus dilakukan sejak awal untuk menghindari revisi besar 

• Dokumentasi secara bertahap lebih efisien daripada di akhir **C. Pembelajaran Spesifik Domain** 

• Data kesehatan mental memerlukan langkah keamanan ekstra 

• Kompleksitas penjadwalan janji temu jangan diremehkan 

• Orientasi pengguna \( *onboarding*\) sangat penting untuk kesuksesan adopsi 

• Desain responsif wajib untuk aplikasi kesehatan **D. Praktik Terbaik untuk Replikasi** 

• Mulai dengan pengumpulan kebutuhan yang komprehensif 

• Libatkan pengguna akhir sejak fase desain 

• Prioritaskan keamanan dan privasi dari awal 

• Rencanakan skalabilitas meski mulai kecil 

• Anggarkan untuk pemeliharaan dan dukungan pasca-peluncuran 





## **DAFTAR PUSTAKA **

\[1\] 

Y. A. Rozali *et al. *, “MENINGKATKAN KESEHATAN MENTAL DI MASA PANDEMIC,” 2021. 

\[2\] 

Y. Fitriani, S. Utami, and B. Junadi, “Perancangan Sistem Informasi Human Capital Management Berbasis Website,” vol. Vol.6 No.4, 2022. 

\[3\] 

R. Mawarni, E. A. Putri, and D. Triyanti, “AUDIT SISTEM INFORMASI E-LEARNING MENGGUNAKAN FRAMEWORK COBIT 5.0 \(STUDY 

KASUS: E-LEARNING SLBN Sukamaju Kotabumi-Lampung Utara\),” 

2022. 

\[4\] 

I. Bali Pamungkas and A. Tri Putranto, *Sistem Informasi Manajemen*. 

Bandung: WIDINA BHAKTI PERSADA BANDUNG, 2021. 

\[5\] 

Afrizal and Y. Kharsela, “SIPMAMA \(SISTEM INFORMASI PELAYANAN ADMINISTRASI KELURAHAN\) PADA KANTOR 

LURAH MAYANG MANGURAI BERBASIS WEB,” May 2024. 

\[6\] 

M. A. Rojabi, *PENGANTAR SISTEM INFORMASI*. Bogor: Afdan Rojabi Publisher, 2025. 

\[7\] 

Y. Fitriani, S. Utami, and B. Junadi, “Perancangan Sistem Informasi Human Capital Management Berbasis Website,” vol. Vol.6 No.4, 2022. 

\[8\] 

S. Suci, B. Putri, Y. Dharma, N. Putra, & Rizka, and A. Purba, “Analisis Dan Pengembangan Sistem Informasi Manajemen.” 

\[9\] 

A. Oktaviyana, M. Mercedes Br Aritonang, and E. Saputri br Sembiring, 

“Analisis Dan Pengembangan Sistem Informasi Manajemen.” 

\[10\] B. Ilham, A. Magister, P. Sumber, and D. Manusia, “SISTEM INFORMASI MANAJEMEN \(SIM\) SEBAGAI SARANA PENCAPAIAN E-GOVERNMENT,” vol. 14, 2022, doi: 10.33747. 

\[11\] A. Oktaviyana, M. Mercedes Br Aritonang, and E. Saputri br Sembiring, 

“Analisis Dan Pengembangan Sistem Informasi Manajemen.” 

\[12\] W. Gede *et al. *, “LITERATURE REVIEW KOMPONEN SISTEM 

INFORMASI MANAJEMEN: SOFTWARE, DATABASE DAN 

BRAINWARE,” vol. 3, no. 3, 2022, doi: 10.31933/jemsi.v3i3. 

\[13\] R. Kivania, A. Novianti, and R. Firmansyah, “Analisis Implementasi Peranan Sistem Reservasi Pada Bisnis Di Sektor Industri,” *Sosial dan* *Humaniora*, vol. 1, no. 1, 2023. 

\[14\] R. Sovitriana, W. Damayanthi, and E. Andini, “Penerapan Terapi Realitas dengan Teknik WDEP untuk Meningkatkan Penerimaan Diri pada Pemuda Bermasalah Sosial di Panti Sosial Bina Remaja Taruna Jaya 2 Tangerang Selatan.” 

\[Online\]. 

Available: 

https://journals.upi-

yai.ac.id/index.php/PsikologiKreatifInovatif/issue/archive 

\[15\] R. Sovitriana, W. Damayanthi, and E. Andini, “Penerapan Terapi Realitas dengan Teknik WDEP untuk Meningkatkan Penerimaan Diri pada Pemuda Bermasalah Sosial di Panti Sosial Bina Remaja Taruna Jaya 2 Tangerang Selatan.” 

\[Online\]. 

Available: 

https://journals.upi-

yai.ac.id/index.php/PsikologiKreatifInovatif/issue/archive 

\[16\] D. Santika Wulandari *et al. *, “Sistem Informasi Penilaian Perkembangan Belajar Siswa Berbasis Web Dengan Framework CodeIgniter Di KUMON 



Ngringo 

Jaten, 

Karanganyar,” 

2022. 

\[Online\]. 

Available: 

https://journal.polhas.ac.id/index.php/imaging 

\[17\] M. Madrofil Banin, “Perancangan Sistem Informasi Untuk Mengontrol Sistem Pembelian, Persediaan Dan Penjualan Dengan Menggunakan Metode System Development Life Cycle \(SDLC\) Information System Design To Control Purchasing, Inventory And Sales system Using System Development Life Cycle \(SLDC\) Method,” 2021. \[Online\]. Available: http://jurnal.um-palembang.ac.id/integrasi/index 

\[18\] A. Muni and A. Isya Alfassa, “MERANCANG APLIKASI PERPUSTAKAAN MENGGUNAKAN METODE SDLC \(SYSTEM 

DEVELOPMENT LIFE CYCLE\),” *Jurnal Sistem Informasi \(TEKNOFILE\)*, vol. 2, no. 6, pp. 485–493, 2024. 

\[19\] A. Sutikno, “SISTEM INFORMASI PENGGAJIAN KARYAWAN PT 

METAGRA MENGGUNAKAN METODE WATERFALL,” *JUPIKOM*, vol. 1, no. 2, 2022. 

\[20\] B. Fachri and C. Rizal, “Penerapan Metode Waterfall Dalam Perancangan Sistem Informasi Merdeka Belajar Kampus Merdeka Berbasis Web,” 

Online, 

2024. 

\[Online\]. 

Available: 

https://kampusmerdeka.kemdikbud.go.id/, 

\[21\] J. Alif Ramadhan, D. Tresya Haniva, and A. Suharso, “Systematic Literature Review Penggunaan Metodologi Pengembangan Sistem Informasi Waterfall, Agile, dan Hybrid,” 2023. 

\[22\] F. Anisa, S. Fauzi, H. Harahap, P. Al Khosyi, and Y. Sari, “Pengembangan Software Menggunakan Model SDLC Guna Mencapai Keselarasan dengan Kebutuhan 

Pengguna,” 

2024. 

\[Online\]. 

Available: 

https://jurnal.ittc.web.id/index.php/jibs/index 

\[23\] I. Gusti Rai Putra Wiguna, “PENDEKATAN TERINTEGRASI HIPNOTERAPI DAN COGNITIVE BEHAVIORAL THERAPY DALAM 

PENANGANAN PASIEN JIWA,” *Jurnal Inovasi Riset Ilmu Kesehatan*, vol. 

3, 

no. 

3, 

2024, 

\[Online\]. 

Available: 

https://jurnalp4i.com/index.php/healthy



