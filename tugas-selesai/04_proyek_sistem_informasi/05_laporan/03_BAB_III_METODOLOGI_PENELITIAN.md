# BAB III  
# METODOLOGI PENELITIAN

## 3.1 Tahapan Penelitian

Penelitian dan pengembangan sistem informasi manajemen reservasi dan terapi CUR-HEART menggunakan pendekatan ***System Development Life Cycle* (SDLC)** dengan model ***Waterfall***. Model ini dipilih karena karakteristik proyek yang memiliki kebutuhan jelas, waktu yang tetap (semester akademik), dan memerlukan dokumentasi yang komprehensif untuk keperluan akademik. Tahapan penelitian terdiri dari lima fase utama yang dilaksanakan secara berurutan dengan keluaran yang terdefinisi jelas di setiap fase.

---

**[GAMBAR 3.1 - Tahapan Penelitian]**

```
┌─────────────────┐
│   Inisiasi      │
│    Proyek       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Perencanaan    │
│    Proyek       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Pelaksanaan    │
│    Proyek       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Pemantauan &   │
│  Pengendalian   │
│    Proyek       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Penutupan     │
│    Proyek       │
└─────────────────┘
```

---

Uraian tahapan penelitian sebagai berikut:

**1. Inisiasi Proyek**

Tahapan ini dimulai dengan mengidentifikasi permasalahan yang dihadapi CUR-HEART dalam manajemen reservasi dan terapi, menentukan tujuan proyek, mengidentifikasi pemangku kepentingan, serta menyusun project charter sebagai dokumen otorisasi formal untuk memulai proyek.

**2. Perencanaan Proyek** 

Tahapan perencanaan mencakup penyusunan ruang lingkup proyek (*scope*), penjadwalan waktu pengerjaan (*timeline*), estimasi anggaran biaya, perencanaan kualitas, identifikasi sumber daya yang dibutuhkan, analisis risiko, perencanaan komunikasi, dan strategi pengadaan (*procurement*).

**3. Pelaksanaan Proyek**

Tahapan pelaksanaan merupakan fase inti pengembangan sistem yang terdiri dari:
- Analisis kebutuhan sistem melalui observasi, wawancara, dan studi dokumentasi
- Perancangan sistem meliputi desain basis data, desain antarmuka pengguna, dan diagram UML
- Implementasi sistem menggunakan framework Laravel dengan bahasa pemrograman PHP
- Pengujian sistem secara menyeluruh untuk memastikan kualitas dan kesesuaian dengan kebutuhan
- Deployment sistem ke lingkungan produksi

**4. Pemantauan dan Pengendalian Proyek**

Tahapan ini dilakukan paralel dengan pelaksanaan proyek untuk memastikan proyek berjalan sesuai rencana. Aktivitas meliputi pemantauan progres pengerjaan, pengendalian perubahan ruang lingkup, pengendalian kualitas deliverables, dan pengelolaan risiko yang muncul selama pengerjaan.

**5. Penutupan Proyek**

Tahapan akhir mencakup serah terima sistem (*handover*) kepada klien, penyusunan dokumentasi lengkap (manual pengguna, dokumentasi teknis), evaluasi pencapaian tujuan proyek, lessons learned, dan pelepasan sumber daya tim proyek

---

## 3.2 Tempat dan Waktu Penelitian

### 3.2.1 Tempat Penelitian

Penelitian dan pengembangan sistem informasi ini dilaksanakan di beberapa lokasi sebagai berikut:

**1. CUR-HEART (*Hypnotherapy & Mind Wellness Center*)**
   - Alamat: Jl. Raya Cilodong No. 88, Depok, Jawa Barat
   - Kegiatan: Observasi proses bisnis, wawancara dengan pemangku kepentingan, dan pengujian penerimaan pengguna (*User Acceptance Testing*)

**2. Universitas Nusa Mandiri - Kampus Margonda**
   - Alamat: Jl. Margonda Raya No. 100, Pondok Cina, Depok, Jawa Barat
   - Kegiatan: Pengembangan sistem, konsultasi dengan dosen pembimbing, dan koordinasi tim proyek

**3. Secara Daring (*Remote/Online*)**
   - Kegiatan: Pengembangan sistem, dokumentasi, pengujian, dan koordinasi tim melalui platform kolaborasi daring

### 3.2.2 Waktu Penelitian

Penelitian ini dilaksanakan selama satu semester akademik dengan rentang waktu sebagai berikut:

**Tabel 3.1 Jadwal Penelitian**

| No | Kegiatan | Waktu Pelaksanaan |
|----|----------|-------------------|
| 1 | Inisiasi dan Analisis Kebutuhan | Minggu 1-2 (16-29 September 2024) |
| 2 | Perancangan Sistem | Minggu 3-4 (30 September - 13 Oktober 2024) |
| 3 | Implementasi Sistem | Minggu 5-8 (14 Oktober - 10 November 2024) |
| 4 | Pengujian Sistem | Minggu 9-10 (11-24 November 2024) |
| 5 | Deployment dan Evaluasi | Minggu 11 (25 November - 1 Desember 2024) |
| 6 | Penyusunan Laporan | Minggu 12-15 (2-29 Desember 2024) |

Total durasi penelitian adalah **15 minggu** (16 September - 29 Desember 2024)
---

## 3.3 Subjek Penelitian

Subjek penelitian dalam pengembangan sistem informasi CUR-HEART terdiri dari pemangku kepentingan yang terlibat langsung dalam penggunaan sistem. Penelitian ini menggunakan metode sampling purposive (non-probabilitas) dimana partisipan dipilih berdasarkan kriteria tertentu yang relevan dengan tujuan penelitian.

### 3.3.1 Populasi

Populasi dalam penelitian ini adalah seluruh pengguna potensial sistem informasi CUR-HEART yang terdiri dari:
- Pemilik dan manajemen CUR-HEART
- Terapis yang bekerja di CUR-HEART
- Staf administrasi dan customer service
- Klien yang menggunakan layanan terapi CUR-HEART
- Calon klien potensial yang membutuhkan layanan terapi kesehatan mental

### 3.3.2 Sampel dan Teknik Pengambilan Sampel

Penelitian ini menggunakan teknik **purposive sampling** (pengambilan sampel bertujuan) dimana sampel dipilih secara sengaja berdasarkan karakteristik dan kriteria tertentu yang sesuai dengan kebutuhan penelitian.

**Tabel 3.2 Distribusi Sampel Penelitian**

| No | Kategori Sampel | Jumlah | Kriteria Pemilihan | Peran dalam Penelitian |
|----|----------------|--------|-------------------|----------------------|
| 1 | Pemilik/Manajemen | 1 orang | Pengambil keputusan, memahami visi bisnis | Memberikan kebutuhan bisnis, validasi sistem |
| 2 | Terapis | 3 orang | Berpengalaman minimal 1 tahun, pengguna aktif sistem | Memberikan kebutuhan fungsional, pengujian sistem |
| 3 | Staf Admin/CS | 2 orang | Mengelola reservasi dan administrasi harian | Memberikan proses bisnis existing, pengujian |
| 4 | Klien Aktif | 5 orang | Pernah menggunakan layanan minimal 2 kali | Memberikan feedback kebutuhan klien, UAT |
| 5 | Calon Klien | 3 orang | Berminat menggunakan layanan terapi | Pengujian usability dari perspektif user baru |
| **Total** | **14 orang** | | |

Teknik pengambilan sampel menggunakan **purposive sampling** dengan pertimbangan:
- Sampel dipilih berdasarkan pengetahuan dan pengalaman mereka terhadap proses bisnis CUR-HEART
- Mewakili berbagai peran pengguna dalam sistem (admin, terapis, klien)
- Dapat memberikan informasi yang mendalam dan relevan untuk pengembangan sistem
- Bersedia berpartisipasi dalam wawancara, observasi, dan pengujian sistem
---

## 3.4 Teknik Pengumpulan Data

Pengumpulan data dalam penelitian ini menggunakan pendekatan multi-metode untuk memastikan pemahaman yang komprehensif terhadap kebutuhan sistem dan validasi dari berbagai perspektif. Teknik pengumpulan data yang digunakan meliputi observasi, wawancara, studi pustaka, dan kuesioner.

### 3.4.1 Observasi

Observasi dilakukan untuk memahami proses bisnis aktual yang berjalan di CUR-HEART dan mengidentifikasi permasalahan yang terjadi dalam operasional sehari-hari. Observasi dilakukan secara langsung di lokasi CUR-HEART dengan mengamati:

- Proses reservasi layanan terapi melalui WhatsApp dan telepon
- Proses penjadwalan terapis dan manajemen waktu
- Interaksi antara staf administrasi dengan klien
- Proses pencatatan data klien dan dokumentasi sesi terapi
- Proses pembayaran dan pembuatan laporan

Hasil observasi didokumentasikan dalam catatan lapangan (*field notes*) dan digunakan sebagai dasar untuk menyusun diagram proses bisnis (*as-is process*) yang menggambarkan kondisi sebelum implementasi sistem.

### 3.4.2 Wawancara

Wawancara semi-terstruktur dilakukan untuk mendapatkan informasi mendalam dari pemangku kepentingan mengenai kebutuhan, harapan, dan kendala yang dihadapi dalam sistem yang sedang berjalan. Wawancara dilakukan kepada:

**Tabel 3.3 Daftar Narasumber Wawancara**

| No | Narasumber | Jumlah | Tujuan Wawancara |
|----|-----------|--------|------------------|
| 1 | Pemilik CUR-HEART | 1 orang | Memahami visi bisnis, target, dan ekspektasi terhadap sistem |
| 2 | Terapis | 3 orang | Mengidentifikasi kebutuhan untuk manajemen jadwal dan dokumentasi sesi terapi |
| 3 | Staf Admin/CS | 2 orang | Memahami proses reservasi, pembayaran, dan administrasi |
| 4 | Klien | 5 orang | Menggali pengalaman reservasi dan ekspektasi terhadap sistem online |

Wawancara dilakukan dengan durasi 30-60 menit per narasumber dan didokumentasikan dalam bentuk transkrip wawancara. Hasil wawancara dianalisis untuk mengidentifikasi kebutuhan fungsional dan non-fungsional sistem.

### 3.4.3 Studi Pustaka

Studi pustaka dilakukan untuk membangun landasan teoritis dan memahami best practice dalam pengembangan sistem informasi sejenis. Sumber pustaka yang digunakan meliputi:

- Jurnal ilmiah tentang sistem informasi manajemen pelayanan kesehatan
- Buku referensi tentang rekayasa perangkat lunak dan manajemen proyek
- Dokumentasi teknis framework Laravel dan teknologi terkait
- Penelitian terdahulu tentang sistem reservasi dan manajemen terapi
- Standar dan regulasi terkait keamanan data kesehatan

Studi pustaka menghasilkan tinjauan literatur yang disajikan dalam BAB II dan menjadi dasar dalam perancangan dan pengembangan sistem.

### 3.4.4 Kuesioner

Kuesioner digunakan untuk mengumpulkan data kuantitatif dari sampel yang lebih luas dan mengukur tingkat kepuasan serta kegunaan sistem. Kuesioner dibagikan dalam dua tahap:

**1. Kuesioner Analisis Kebutuhan**
   - Diberikan kepada calon pengguna sistem (20 responden)
   - Bertujuan mengidentifikasi fitur yang dibutuhkan dan prioritasnya
   - Mengukur kesiapan pengguna terhadap sistem digital

**2. Kuesioner Evaluasi Sistem (System Usability Scale/SUS)**
   - Diberikan kepada partisipan pengujian setelah menggunakan sistem (14 responden)
   - Mengukur tingkat kegunaan sistem dengan metode SUS
   - Mengidentifikasi area perbaikan untuk pengembangan selanjutnya

Hasil kuesioner dianalisis secara deskriptif dan statistik untuk mendukung pengambilan keputusan dalam pengembangan sistem.

---
