# JAWABAN KUIS BUSINESS INTELLIGENCE

**Mata Kuliah:** Business Intelligence  
**Dosen:** [NAMA DOSEN]  
**Nama:** [NAMA MAHASISWA]  
**NIM:** [NIM MAHASISWA]  
**Kelas:** [KELAS]

---

## JAWABAN SOAL ESSAY

### 1. Mengapa visualisasi data penting dalam proses BI, dan bagaimana hal itu membantu manajer dalam mengambil keputusan?

Visualisasi data itu penting banget dalam BI karena manusia lebih cepat nangkap informasi lewat gambar atau grafik daripada cuma liat angka-angka di tabel. Bayangin aja kalau manajer disodori laporan excel dengan ribuan baris data, pasti pusing dan butuh waktu lama buat memahaminya.

Dengan visualisasi, data yang rumit bisa disajikan dalam bentuk yang lebih gampang dimengerti, misalnya pakai chart, diagram, atau dashboard. Jadi manajer bisa langsung lihat pola, tren, atau anomali yang terjadi tanpa harus baca satu-satu datanya.

Contohnya, kalau ada penurunan penjualan di wilayah tertentu, dengan visualisasi bisa langsung keliatan pakai peta atau grafik batang. Ini membantu manajer untuk cepat ambil keputusan, misalnya perlu nambah promosi di daerah itu atau evaluasi strategi pemasaran. Intinya, visualisasi bikin proses analisis jadi lebih efisien dan keputusan bisa diambil lebih cepat dan tepat.

### 2. Bandingkan antara Data Warehouse dan Data Mart, serta jelaskan peran keduanya dalam sistem Business Intelligence.

Data Warehouse itu seperti gudang besar yang menyimpan semua data dari berbagai sumber di perusahaan. Sifatnya menyeluruh dan mencakup seluruh organisasi. Data yang ada di sini udah diolah dan diintegrasikan dari berbagai sistem, jadi bisa dipake untuk analisis yang lebih luas.

Sedangkan Data Mart itu lebih spesifik, kayak gudang kecil yang fokus ke departemen atau fungsi bisnis tertentu aja. Misalnya ada Data Mart khusus buat divisi penjualan, atau khusus buat divisi marketing. Ukurannya lebih kecil dan lebih fokus, jadi prosesnya lebih cepat.

Peran keduanya dalam BI cukup penting. Data Warehouse jadi sumber utama yang menyediakan data untuk kebutuhan analisis perusahaan secara keseluruhan. Sementara Data Mart memudahkan departemen tertentu buat akses data yang relevan dengan pekerjaan mereka tanpa harus ngelus-ngelus data yang gak perlu.

Hubungannya, Data Mart biasanya diambil dari Data Warehouse, jadi kayak subset-nya. Dengan begini, setiap divisi bisa kerja lebih efisien karena punya akses ke data yang mereka butuhkan aja, tapi tetap terintegrasi dengan sistem data perusahaan secara keseluruhan.

### 3. Jelaskan peran Business Analytics dan Business Performance Management (BPM) dalam meningkatkan kinerja perusahaan.

Business Analytics itu intinya adalah proses menganalisis data untuk mendapatkan insight atau wawasan yang berguna buat bisnis. Dengan analytics, perusahaan bisa mengerti pola perilaku pelanggan, prediksi tren pasar, atau bahkan identifikasi masalah sebelum jadi besar. Jadi perannya adalah memberikan dasar atau landasan untuk pengambilan keputusan yang lebih baik berdasarkan data, bukan cuma feeling atau asumsi.

Sementara Business Performance Management (BPM) lebih ke arah monitoring dan mengelola kinerja perusahaan supaya sesuai dengan target yang udah ditetapkan. BPM biasanya pakai tools kayak KPI (Key Performance Indicator) atau balanced scorecard untuk ngukur seberapa baik perusahaan mencapai tujuannya.

Kalau digabung, Business Analytics menyediakan informasi dan insight, sedangkan BPM menggunakan informasi itu untuk memastikan perusahaan jalan di jalur yang benar. Misalnya, dari analytics ketahuan bahwa produk A kurang laku di musim tertentu, nah BPM bakal bikin strategi atau action plan supaya di musim depan bisa lebih baik, misalnya dengan promosi khusus atau bundling produk.

Jadi keduanya saling melengkapi: analytics kasih tau "apa yang terjadi" dan "kenapa bisa terjadi", sedangkan BPM pastikan perusahaan "melakukan sesuatu" untuk perbaiki atau tingkatkan kinerjanya.

### 4. Jelaskan perbedaan antara model data Star Schema dan Snowflake Schema dalam konteks Business Intelligence!

Star Schema dan Snowflake Schema itu dua model desain database yang sering dipake di data warehouse.

**Star Schema** bentuknya sederhana, ada satu tabel fakta di tengah yang nyimpen data transaksi atau metric, terus dikelilingi sama beberapa tabel dimensi yang nyimpen detail informasi. Tabel dimensi di star schema ini gak dinormalisasi, jadi semua atribut langsung ada di satu tabel aja. Bentuknya kayak bintang gitu, makanya disebut star.

Kelebihannya, query-nya cepet karena struktur sederhana dan gak banyak join. Cocok buat keperluan analisis yang butuh kecepatan. Kelemahannya, bisa ada redundansi data karena gak dinormalisasi, jadi ukuran database bisa lebih besar.

**Snowflake Schema** ini lebih kompleks. Tabel dimensinya dinormalisasi, jadi dipecah-pecah lagi jadi sub-tabel. Misalnya dimensi produk bisa dipecah jadi tabel kategori, sub-kategori, dan lain-lain. Bentuknya jadi kayak kepingan salju yang bercabang-cabang.

Kelebihannya, lebih hemat storage karena gak ada redundansi data. Tapi kelemahannya, query jadi lebih lambat karena harus join banyak tabel.

Dalam konteks BI, pilihan antara keduanya tergantung kebutuhan. Kalau prioritasnya kecepatan query dan kemudahan maintenance, pakai star schema. Kalau lebih peduli sama efisiensi storage dan kompleksitas data, snowflake bisa jadi pilihan. Tapi secara umum, star schema lebih populer karena performa yang lebih baik untuk analisis.

### 5. Jelaskan perbedaan fungsi dari Tableau Desktop, Tableau Server, dan Tableau Public dalam ekosistem Tableau.

Ketiga produk Tableau ini punya fungsi yang berbeda tapi saling melengkapi:

**Tableau Desktop** ini adalah aplikasi yang dipasang di komputer untuk membuat visualisasi dan dashboard. Ini tool utama buat analyst atau siapa pun yang mau bikin laporan visual dari data. Di sini kita bisa konek ke berbagai sumber data, bikin chart, dashboard, dan melakukan analisis. Sifatnya lebih ke personal use atau untuk development. Tableau Desktop ini berbayar dan ada dua versi: Tableau Desktop Professional dan Tableau Desktop Personal.

**Tableau Server** adalah platform untuk sharing dan kolaborasi. Setelah bikin dashboard di Tableau Desktop, kita bisa publish ke Tableau Server supaya orang lain di organisasi bisa akses lewat browser. Tableau Server ini dipasang di server perusahaan sendiri (on-premise), jadi perusahaan punya kontrol penuh atas data dan akses. Cocok buat perusahaan yang butuh keamanan tinggi dan mau manage user access dengan ketat. Ini juga berbayar dan biasanya butuh lisensi untuk setiap user yang mau akses.

**Tableau Public** adalah versi gratis dari Tableau yang bisa dipake siapa aja. Mirip kayak Tableau Desktop tapi dengan batasan: semua visualisasi yang dibuat harus di-publish ke cloud Tableau Public dan bisa dilihat sama semua orang (publik). Jadi gak ada privasi untuk data. Ini cocok buat belajar, latihan, atau kalau mau share insight ke publik kayak untuk blog atau portfolio. Karena gratis dan publik, biasanya gak dipake untuk data perusahaan yang sensitif.

Jadi intinya: Tableau Desktop buat bikin visualisasi, Tableau Server buat sharing internal dengan keamanan, dan Tableau Public buat sharing ke publik secara gratis.

---

**Catatan:** Jawaban ini dibuat berdasarkan pemahaman pribadi terhadap materi Business Intelligence yang telah dipelajari.
