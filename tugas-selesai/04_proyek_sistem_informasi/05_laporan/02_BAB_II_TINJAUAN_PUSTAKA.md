# BAB II  
# TINJAUAN PUSTAKA

## 2.1 Landasan Teori

### 2.1.1 Sistem Informasi

#### 2.1.1.1 Pengertian Sistem Informasi

Sistem informasi merupakan kombinasi terorganisir dari manusia, perangkat keras (*hardware*), perangkat lunak (*software*), jaringan komunikasi, dan sumber daya data yang mengumpulkan, mengubah, dan menyebarkan informasi dalam sebuah organisasi (O'Brien & Marakas, 2017). Menurut Laudon & Laudon (2020), sistem informasi adalah seperangkat komponen yang saling berhubungan yang berfungsi mengumpulkan, memproses, menyimpan, dan mendistribusikan informasi untuk mendukung pengambilan keputusan, koordinasi, kontrol, analisis, dan visualisasi dalam sebuah organisasi.

Whitten & Bentley (2019) mendefinisikan sistem informasi sebagai pengaturan orang, data, proses, dan teknologi informasi yang berinteraksi untuk mengumpulkan, memproses, menyimpan, dan menyediakan informasi yang dibutuhkan sebagai keluaran untuk mendukung sebuah organisasi. Definisi ini menekankan bahwa sistem informasi bukan hanya tentang teknologi, tetapi juga tentang bagaimana teknologi tersebut digunakan oleh manusia untuk mencapai tujuan organisasi.

Stair & Reynolds (2018) menjelaskan bahwa sistem informasi terdiri dari lima komponen utama yang saling berinteraksi:

1. **Perangkat Keras (*Hardware*):** Komputer, server, perangkat penyimpanan, dan peralatan lainnya yang digunakan untuk memasukkan, memproses, dan mengeluarkan data.

2. **Perangkat Lunak (*Software*):** Program dan aplikasi yang memberikan instruksi kepada perangkat keras untuk melakukan pemrosesan data, termasuk sistem operasi, sistem manajemen basis data, dan aplikasi bisnis.

3. **Data:** Fakta mentah yang dikumpulkan, disimpan, dan diproses oleh sistem, yang kemudian diubah menjadi informasi yang bermakna dan berguna untuk pengambilan keputusan.

4. **Manusia (*People*):** Pengguna yang berinteraksi dengan sistem, termasuk pengguna akhir, profesional teknologi informasi, dan manajemen yang menggunakan keluaran sistem untuk pengambilan keputusan.

5. **Prosedur (*Procedures*):** Kebijakan, aturan, dan metode yang mengatur bagaimana sistem digunakan, termasuk prosedur masukan data, proses, keluaran, dan pencadangan.

---

**[GAMBAR 2.1 - Komponen Sistem Informasi]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT DIAGRAM KOMPONEN SISTEM INFORMASI]               │
│                                                             │
│   Center: SISTEM INFORMASI (center circle)                 │
│                                                             │
│   5 Komponen (surrounding circles with icons):             │
│                                                             │
│      🖥️  HARDWARE                                          │
│      (Komputer, Server, Storage)                           │
│                                                             │
│   💿 SOFTWARE          SISTEM         📊 DATA              │
│   (OS, Apps, DB)    INFORMASI      (Facts, Info)          │
│                                                             │
│      👥 PEOPLE                                              │
│      (Users, IT Staff)                                     │
│                                                             │
│      📋 PROCEDURES                                          │
│      (Policies, Rules)                                     │
│                                                             │
│   Arrows showing interaction between all components        │
│                                                             │
│   Format: Circular diagram atau pentagon diagram           │
│   Style: Clean, professional, dengan icon per komponen     │
│   Recommended size: 1000x800px                             │
│                                                             │
│   File: assets/images/komponen-sistem-informasi.png        │
│   Reference: Stair & Reynolds (2018)                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.1: Lima komponen utama sistem informasi yang saling berinteraksi (Stair & Reynolds, 2018)_

---

#### 2.1.1.2 Jenis-jenis Sistem Informasi

Menurut Laudon & Laudon (2020), sistem informasi dalam organisasi dapat dikategorikan berdasarkan tingkat organisasi dan fungsi yang dilayaninya:

1. **Sistem Pemrosesan Transaksi (*Transaction Processing System*/TPS):**
   Sistem yang menangani transaksi rutin harian organisasi seperti penjualan, pembelian, pembayaran, dan persediaan. TPS adalah fondasi dari sistem informasi lainnya karena menyediakan data yang akan digunakan oleh sistem-sistem di tingkat yang lebih tinggi.

2. **Sistem Informasi Manajemen (*Management Information System*/MIS):**
   Sistem yang menyediakan informasi dalam bentuk laporan dan tampilan untuk mendukung pengambilan keputusan manajerial di tingkat menengah organisasi.

3. **Sistem Pendukung Keputusan (*Decision Support System*/DSS):**
   Sistem yang membantu manajemen dalam membuat keputusan semi-terstruktur atau tidak terstruktur melalui analisis data dan pemodelan.

4. **Sistem Pendukung Eksekutif (*Executive Support System*/ESS):**
   Sistem yang dirancang untuk membantu eksekutif senior melakukan perencanaan strategis dan pengambilan keputusan melalui dasbor dan laporan ringkasan.

Dalam konteks proyek ini, sistem informasi CUR-HEART termasuk kategori **Sistem Pemrosesan Transaksi (TPS)** karena menangani transaksi pemesanan, pembayaran, dan dokumentasi sesi terapi, serta **Sistem Informasi Manajemen (MIS)** karena menyediakan pelaporan dan analitik untuk mendukung pengambilan keputusan manajerial.

#### 2.1.1.3 Manfaat Sistem Informasi

Menurut Turban et al. (2018), implementasi sistem informasi memberikan berbagai manfaat strategis bagi organisasi:

1. **Keunggulan Operasional (*Operational Excellence*):** Meningkatkan efisiensi operasional melalui otomasi proses bisnis.
2. **Produk dan Layanan Baru (*New Products and Services*):** Memungkinkan penciptaan produk dan layanan baru berbasis digital.
3. **Kedekatan Pelanggan dan Pemasok (*Customer and Supplier Intimacy*):** Meningkatkan hubungan dengan pelanggan dan pemasok melalui komunikasi yang lebih baik.
4. **Peningkatan Pengambilan Keputusan (*Improved Decision Making*):** Menyediakan informasi waktu nyata dan akurat untuk pengambilan keputusan.
5. **Keunggulan Kompetitif (*Competitive Advantage*):** Menciptakan keunggulan kompetitif melalui inovasi dan diferensiasi.
6. **Kelangsungan Hidup (*Survival*):** Dalam era digital, sistem informasi menjadi kebutuhan untuk kelangsungan hidup organisasi.

### 2.1.2 Manajemen Proyek Sistem Informasi

#### 2.1.2.1 Pengertian Manajemen Proyek

*Project Management Institute* (PMI, 2021) mendefinisikan manajemen proyek sebagai aplikasi pengetahuan, keterampilan, perangkat, dan teknik terhadap aktivitas proyek untuk memenuhi kebutuhan proyek. Manajemen proyek dilakukan melalui penerapan dan integrasi yang tepat dari 49 proses manajemen proyek yang dikelompokkan secara logis, yang terdiri dari 5 kelompok proses dan 10 area pengetahuan.

Menurut Schwalbe (2019), manajemen proyek adalah proses merencanakan, mengorganisir, dan mengelola tugas dan sumber daya untuk mencapai tujuan yang konkret dengan batasan tertentu (cakupan, waktu, biaya, kualitas). Dalam konteks proyek sistem informasi, manajemen proyek melibatkan koordinasi antara tim teknis, pemangku kepentingan, dan sumber daya untuk menyerahkan sistem yang memenuhi persyaratan dalam batasan waktu dan anggaran yang ditentukan.

#### 2.1.2.2 Kendala Tiga Sisi (*Triple Constraint*) dalam Manajemen Proyek

Konsep fundamental dalam manajemen proyek adalah Kendala Tiga Sisi (*Triple Constraint*) atau Segitiga Besi (*Iron Triangle*), yang terdiri dari tiga elemen utama yang saling berkaitan (Kerzner, 2017):

1. **Cakupan (*Scope*):**
   Mendefinisikan apa saja yang termasuk dan tidak termasuk dalam proyek, termasuk fitur, fungsi, dan luaran yang harus dihasilkan.

2. **Waktu (*Time*):**
   Jadwal atau garis waktu proyek dari inisiasi hingga penutupan, termasuk tonggak pencapaian dan tenggat untuk setiap luaran.

3. **Biaya (*Cost*):**
   Anggaran proyek yang mencakup semua biaya yang diperlukan untuk menyelesaikan proyek, termasuk tenaga kerja, bahan, peralatan, dan biaya overhead.

Ketiga elemen ini saling mempengaruhi. Perubahan pada salah satu elemen akan berdampak pada elemen lainnya. Misalnya, jika cakupan bertambah, maka waktu dan biaya biasanya juga akan meningkat. Oleh karena itu, manajer proyek harus mampu melakukan timbal balik dan penyeimbangan antara ketiga elemen ini.

Dalam perkembangan modern, Kendala Tiga Sisi diperluas menjadi **Segitiga Manajemen Proyek** (*Project Management Triangle*) dengan menambahkan elemen keempat yaitu **Kualitas (*Quality*)**, yang mengindikasikan bahwa manajemen proyek harus juga memastikan bahwa luaran memenuhi standar kualitas yang diharapkan (PMI, 2021).

#### 2.1.2.3 Area Pengetahuan (*Knowledge Areas*) dalam Manajemen Proyek

*PMBOK Guide* Edisi ke-7 (PMI, 2021) mengidentifikasi 10 area pengetahuan dalam manajemen proyek:

1. **Manajemen Integrasi Proyek (*Project Integration Management*):** Koordinasi semua aspek proyek.
2. **Manajemen Cakupan Proyek (*Project Scope Management*):** Mendefinisikan dan mengontrol apa yang termasuk dalam proyek.
3. **Manajemen Jadwal Proyek (*Project Schedule Management*):** Mengelola penyelesaian proyek tepat waktu.
4. **Manajemen Biaya Proyek (*Project Cost Management*):** Perencanaan dan kontrol anggaran proyek.
5. **Manajemen Kualitas Proyek (*Project Quality Management*):** Memastikan luaran memenuhi standar kualitas.
6. **Manajemen Sumber Daya Proyek (*Project Resource Management*):** Mengelola tim proyek dan sumber daya.
7. **Manajemen Komunikasi Proyek (*Project Communications Management*):** Mengelola komunikasi pemangku kepentingan.
8. **Manajemen Risiko Proyek (*Project Risk Management*):** Mengidentifikasi dan mitigasi risiko.
9. **Manajemen Pengadaan Proyek (*Project Procurement Management*):** Mengelola vendor dan pemasok.
10. **Manajemen Pemangku Kepentingan Proyek (*Project Stakeholder Management*):** Mengelola ekspektasi dan keterlibatan pemangku kepentingan.

---

**[GAMBAR 2.2 - Knowledge Areas PMBOK 6th Edition]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT DIAGRAM 10 KNOWLEDGE AREAS PMBOK]                │
│                                                             │
│   Center: PROJECT MANAGEMENT (core)                        │
│                                                             │
│   10 Knowledge Areas (surrounding the center):             │
│                                                             │
│   1️⃣  Integration Management                               │
│   2️⃣  Scope Management                                     │
│   3️⃣  Schedule Management                                  │
│   4️⃣  Cost Management                                      │
│   5️⃣  Quality Management                                   │
│   6️⃣  Resource Management                                  │
│   7️⃣  Communications Management                            │
│   8️⃣  Risk Management                                      │
│   9️⃣  Procurement Management                               │
│   🔟 Manajemen Pemangku Kepentingan                        │
│                                                             │
│   Format: Circular/radial diagram atau hexagon layout      │
│   Style: Color-coded per knowledge area                    │
│   Recommended size: 1200x900px                             │
│                                                             │
│   File: assets/images/pmbok-knowledge-areas.png            │
│   Reference: PMI PMBOK Guide 6th Edition (2017)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.2: Sepuluh knowledge areas dalam Project Management Body of Knowledge (PMBOK) 6th Edition yang menjadi panduan manajemen proyek sistem informasi_

---

### 2.1.3 Siklus Hidup Pengembangan Sistem (*System Development Life Cycle*/SDLC)

#### 2.1.3.1 Pengertian SDLC

Siklus Hidup Pengembangan Sistem (*System Development Life Cycle*/SDLC) adalah proses yang digunakan oleh organisasi untuk merencanakan, mengembangkan, menguji, dan menerapkan sistem informasi (Dennis et al., 2020). SDLC menyediakan kerangka kerja yang sistematis dan terstruktur untuk pengembangan sistem, memastikan bahwa sistem yang dihasilkan berkualitas tinggi, memenuhi kebutuhan pengguna, dan selesai dalam batasan waktu dan anggaran yang ditentukan.

Menurut Kendall & Kendall (2019), SDLC adalah pendekatan bertahap (*phased approach*) untuk analisis dan desain sistem dengan menggunakan seperangkat prosedur, teknik, perangkat, dan dokumentasi yang spesifik untuk setiap tahapan. Tujuan utama SDLC adalah menghasilkan sistem berkualitas tinggi yang memenuhi atau melampaui ekspektasi pelanggan, diselesaikan dalam kerangka waktu dan estimasi biaya, bekerja secara efektif dan efisien, serta mudah dan efektif biaya untuk pemeliharaan dan peningkatan.

#### 2.1.3.2 Model Air Terjun (*Waterfall*)

Model Air Terjun (*Waterfall*), yang pertama kali diperkenalkan oleh Winston Royce pada tahun 1970, adalah model SDLC yang paling klasik dan masih banyak digunakan hingga saat ini (Sommerville, 2016). Model ini dinamakan "air terjun" karena kemajuan dari satu fase ke fase berikutnya mengalir ke bawah seperti air terjun (*cascade*).

**Karakteristik Model Air Terjun:**

1. **Proses Sekuensial (*Sequential Process*):** Setiap fase harus diselesaikan sepenuhnya sebelum fase berikutnya dimulai.
2. **Didorong Dokumentasi (*Documentation-Driven*):** Setiap fase menghasilkan dokumentasi yang lengkap sebagai masukan untuk fase berikutnya.
3. **Perencanaan Prediktif (*Predictive Planning*):** Semua persyaratan didefinisikan di awal proyek dan diharapkan tidak berubah.
4. **Tinjauan Formal (*Formal Reviews*):** Setiap fase diakhiri dengan tinjauan formal atau persetujuan sebelum melanjutkan ke fase berikutnya.

**Tahapan Model Air Terjun:**

1. **Analisis Kebutuhan (*Requirements Analysis*):**
   - Mengumpulkan dan mendokumentasikan kebutuhan sistem secara lengkap
   - Melakukan studi kelayakan (kelayakan teknis, ekonomi, operasional)
   - Menghasilkan dokumen Spesifikasi Kebutuhan Perangkat Lunak (*Software Requirements Specification*/SRS)
   - Persetujuan pemangku kepentingan pada persyaratan

2. **Desain Sistem (*System Design*):**
   - Desain tingkat tinggi (arsitektur sistem, desain basis data, desain antarmuka)
   - Desain tingkat rendah (algoritma terperinci, struktur data, spesifikasi modul)
   - Menghasilkan Dokumen Desain Sistem (*System Design Document*/SDD)
   - Tinjauan desain dan persetujuan

3. **Implementasi (*Implementation*):**
   - Pengodean atau pemrograman berdasarkan dokumen desain
   - Pengujian unit untuk setiap modul atau komponen
   - Tinjauan kode dan jaminan kualitas
   - Kontrol versi dan manajemen konfigurasi

4. **Pengujian (*Testing*):**
   - Pengujian integrasi untuk menguji interaksi antar modul
   - Pengujian sistem untuk menguji keseluruhan sistem
   - Pengujian Penerimaan Pengguna (*User Acceptance Testing*/UAT) dengan keterlibatan pengguna
   - Perbaikan *bug* dan pengujian ulang

5. **Penerapan (*Deployment*):**
   - Instalasi sistem di lingkungan produksi
   - Migrasi data dari sistem lama (jika ada)
   - Pelatihan pengguna dan transfer pengetahuan
   - Peluncuran dan serah terima ke tim operasi

6. **Pemeliharaan (*Maintenance*):**
   - Perbaikan *bug* dan resolusi masalah
   - Penyetelan kinerja dan optimisasi
   - Peningkatan dan pengembangan fitur baru
   - Pembaruan dan tambalan rutin

---

**[GAMBAR 2.3 - Waterfall SDLC Model]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT WATERFALL DIAGRAM]                               │
│                                                             │
│   6 Fase Berurutan (dari atas ke bawah):                   │
│   ┌────────────────────────────┐                           │
│   │ 1. REQUIREMENTS ANALYSIS   │                           │
│   └────────────────────────────┘                           │
│              ↓                                              │
│   ┌────────────────────────────┐                           │
│   │ 2. SYSTEM DESIGN           │                           │
│   └────────────────────────────┘                           │
│              ↓                                              │
│   ┌────────────────────────────┐                           │
│   │ 3. IMPLEMENTATION          │                           │
│   └────────────────────────────┘                           │
│              ↓                                              │
│   ┌────────────────────────────┐                           │
│   │ 4. TESTING                 │                           │
│   └────────────────────────────┘                           │
│              ↓                                              │
│   ┌────────────────────────────┐                           │
│   │ 5. DEPLOYMENT              │                           │
│   └────────────────────────────┘                           │
│              ↓                                              │
│   ┌────────────────────────────┐                           │
│   │ 6. MAINTENANCE             │                           │
│   └────────────────────────────┘                           │
│                                                             │
│   Format: Flowchart dengan arrow ke bawah                  │
│   Style: Clean, professional dengan box per fase           │
│   Recommended size: 800x1200px (portrait)                  │
│                                                             │
│   File: assets/images/waterfall-sdlc-model.png             │
│   Reference: Royce (1970), Sommerville (2016)              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.3: Model Waterfall SDLC dengan 6 fase berurutan yang digunakan dalam pengembangan sistem CUR-HEART_

---

**Kelebihan Model Air Terjun:**

- Mudah dipahami dan diimplementasikan karena strukturnya yang sederhana dan linear
- Dokumentasi yang lengkap di setiap tahapan memudahkan pemeliharaan
- Kemajuan dapat diukur dengan jelas melalui tonggak pencapaian setiap fase
- Cocok untuk proyek dengan persyaratan yang jelas dan stabil
- Perencanaan sumber daya lebih mudah karena sifat sekuensial

**Kekurangan Model Air Terjun:**

- Tidak fleksibel terhadap perubahan persyaratan di tengah proyek
- Perangkat lunak yang berfungsi baru tersedia di akhir siklus hidup proyek
- Risiko tinggi jika terjadi kesalahan di tahap awal yang baru terdeteksi di tahap akhir
- Tidak cocok untuk proyek besar dan kompleks dengan persyaratan yang tidak jelas
- Keterlibatan pelanggan hanya di awal (persyaratan) dan akhir (UAT)

Dalam proyek sistem informasi CUR-HEART ini, model Air Terjun dipilih karena:

1. Persyaratan sudah cukup jelas dan stabil berdasarkan analisis proses bisnis yang ada
2. Cakupan proyek terdefinisi dengan baik dan tidak diharapkan ada perubahan signifikan
3. Proyek memiliki garis waktu yang tetap (semester akademik)
4. Dokumentasi lengkap diperlukan untuk keperluan akademik (Proyek Akhir/*Capstone Project*)
5. Tim pengembang relatif kecil dan terstruktur

#### 2.1.3.3 Model SDLC Lainnya (Comparison)

Selain Waterfall, terdapat beberapa model SDLC lain yang populer. Berikut adalah perbandingan berbagai model SDLC:

---

**Tabel 2.1 Perbandingan Model SDLC**

| Model | Karakteristik Utama | Tahapan/Siklus | Kelebihan | Kekurangan | Cocok Untuk | CUR-HEART Fit Score |
|-------|-------------------|---------------|-----------|------------|------------|-------------------|
| **Air Terjun** (*Waterfall*) | • Sekuensial, linear<br>• Berbasis dokumentasi<br>• Perencanaan prediktif<br>• Tinjauan fase formal | 1. Persyaratan<br>2. Desain<br>3. Implementasi<br>4. Pengujian<br>5. Penerapan<br>6. Pemeliharaan | • Mudah dipahami & dikelola<br>• Dokumentasi lengkap<br>• Kemajuan terukur<br>• Tonggak jelas<br>• Cocok untuk tim kecil | • Tidak fleksibel terhadap perubahan<br>• Perangkat lunak berfungsi di akhir<br>• Risiko tinggi jika kesalahan di awal<br>• Keterlibatan pelanggan terbatas | • Persyaratan jelas & stabil<br>• Proyek terstruktur<br>• Garis waktu tetap<br>• Dokumentasi penting | ✅ **95%** (DIPILIH)<br>Alasan: Persyaratan stabil, garis waktu tetap (11 minggu), dokumentasi akademik |
| ***Agile* (Scrum)** | • Iteratif & inkremental<br>• Fleksibel & adaptif<br>• Kolaborasi berkelanjutan<br>• *Sprint* (2-4 minggu) | Iterasi berulang:<br>1. Perencanaan *Sprint*<br>2. *Daily Standups*<br>3. Pengembangan<br>4. Tinjauan *Sprint*<br>5. Retrospektif | • Fleksibel terhadap perubahan<br>• Luaran sering<br>• Keterlibatan pelanggan tinggi<br>• Mitigasi risiko<br>• Kolaborasi tim | • Garis waktu kurang dapat diprediksi<br>• Dokumentasi minimal<br>• Memerlukan tim berpengalaman<br>• Risiko perluasan cakupan<br>• Komitmen harian diperlukan | • Persyaratan berkembang<br>• Pelanggan tersedia harian<br>• Tim berpengalaman<br>• Proyek jangka panjang | ⚠️ **60%**<br>Perhatian: Garis waktu ketat, tim baru, dokumentasi akademik diperlukan |
| **Spiral** | • Berbasis risiko<br>• Purwarupa iteratif<br>• Putaran berganda<br>• Analisis risiko setiap putaran | Putaran berulang:<br>1. Perencanaan<br>2. Analisis Risiko<br>3. Rekayasa<br>4. Evaluasi | • Manajemen risiko sangat baik<br>• Fleksibilitas tinggi<br>• Purwarupa awal<br>• Cocok untuk proyek kompleks | • Kompleks untuk dikelola<br>• Mahal (analisis risiko)<br>• Memerlukan ahli risiko<br>• Memakan waktu | • Proyek berisiko tinggi<br>• Sistem besar & kompleks<br>• Persyaratan tidak pasti<br>• Aplikasi kritis | ❌ **40%**<br>Perhatian: Berlebihan untuk skala proyek, tidak ada ahli risiko, biaya tinggi |
| **Model-V** (*V-Model*) | • Ekstensi Air Terjun<br>• Penekanan pengujian<br>• Verifikasi & Validasi<br>• Setiap fase pengembangan = fase uji | Sekuensial dengan pengujian paralel:<br>1. Persyaratan → Uji Penerimaan<br>2. Desain → Uji Sistem<br>3. Desain Modul → Uji Integrasi<br>4. Pengodean → Uji Unit | • Jaminan kualitas tinggi<br>• Perencanaan uji awal<br>• Luaran jelas<br>• Baik untuk kritis-keselamatan | • Kaku seperti Air Terjun<br>• Tidak fleksibel<br>• Memerlukan persyaratan lengkap<br>• Pengujian mahal | • Sistem kritis-keselamatan<br>• Aplikasi medis/penerbangan<br>• Keandalan tinggi diperlukan<br>• Persyaratan jelas | ⚠️ **50%**<br>Perhatian: Berlebihan untuk pengujian, bukan kritis-keselamatan, terlalu kaku |
| **RAD** (*Rapid Application Development*) | • Purwarupa cepat<br>• Berfokus pengguna<br>• *Timeboxed* (60-90 hari)<br>• Komponen dapat digunakan ulang | 1. Perencanaan Persyaratan<br>2. Desain Pengguna (lokakarya JAD)<br>3. Konstruksi (purwarupa)<br>4. *Cutover* (pengujian & penerapan) | • Pengembangan cepat<br>• Keterlibatan pengguna tinggi<br>• Pengodean manual berkurang<br>• Umpan balik awal | • Memerlukan pengembang terampil<br>• Tidak dapat diskalakan untuk tim besar<br>• Masalah kinerja mungkin<br>• Bergantung pada tim kuat | • Proyek kritis-waktu<br>• Proyek kecil-menengah<br>• Sistem modular<br>• Tim berpengalaman | ⚠️ **70%**<br>Potensi: Pengiriman cepat, tapi dokumentasi kurang, tim belum berpengalaman RAD |
| **DevOps** | • Integrasi Dev + Ops<br>• *Pipeline* CI/CD<br>• Otomasi berat<br>• Pemantauan berkelanjutan | Siklus berkelanjutan:<br>1. Rencana<br>2. Kode<br>3. *Build*<br>4. Uji (otomatis)<br>5. Rilis<br>6. Terapkan<br>7. Operasikan<br>8. Pantau | • Pengiriman cepat<br>• Otomasi & efisiensi<br>• Umpan balik berkelanjutan<br>• Keandalan tinggi<br>• Skalabilitas | • Memerlukan budaya DevOps<br>• Pengaturan awal kompleks<br>• Kurva belajar perangkat<br>• Perlu keahlian otomasi | • Aplikasi *cloud-native*<br>• *Microservices*<br>• Rilis sering<br>• Organisasi besar | ❌ **35%**<br>Perhatian: Overhead pengaturan, aplikasi monolitik, penerapan tunggal, tim belum siap DevOps |
| **Iteratif** (*Iterative*) | • Siklus berulang<br>• Peningkatan bertahap<br>• Bangun-tingkatkan-bangun<br>• Versi berfungsi awal | Iterasi berulang:<br>1. Analisis<br>2. Desain<br>3. Implementasi<br>4. Pengujian<br>→ Ulangi dengan peningkatan | • Sistem berfungsi awal<br>• Pelajaran diterapkan<br>• Pengurangan risiko<br>• Fleksibilitas | • Memerlukan perencanaan baik<br>• Overhead manajemen<br>• Perubahan cakupan bisa mahal | • Proyek menengah<br>• Beberapa ketidakpastian<br>• Penyempurnaan progresif | ⚠️ **65%**<br>Potensi: Baik untuk pembelajaran, tapi kendala garis waktu, overhead manajemen |
| **Purwarupa** (*Prototyping*) | • Bangun-uji-sempurnakan<br>• Maket awal<br>• Didorong umpan balik pengguna<br>• Buang atau evolusioner | 1. Identifikasi Persyaratan<br>2. Kembangkan Purwarupa<br>3. Evaluasi Pengguna<br>4. Sempurnakan Purwarupa<br>5. Implementasi Sistem Final | • Umpan balik pengguna awal<br>• Klarifikasi persyaratan<br>• Risiko penolakan berkurang<br>• UX lebih baik | • Risiko analisis tidak lengkap<br>• Iterasi tanpa akhir mungkin<br>• Kinerja tidak dioptimalkan<br>• Mungkin melewatkan persyaratan | • Proyek berat UI/UX<br>• Kebutuhan pengguna tidak jelas<br>• Solusi inovatif | ⚠️ **55%**<br>Digunakan untuk: Purwarupa UI/UX (Figma), tapi bukan pendekatan SDLC penuh |

**Detailed Comparison Matrix:**

| Kriteria | Weight | Waterfall Score | Agile Score | Spiral Score | RAD Score | DevOps Score | Winner |
|------------------|--------|----------------|------------|-------------|-----------|-------------|--------|
| **Kejelasan Persyaratan** | 20% | 5/5 (Very clear) | 3/5 (Flexible) | 4/5 (Risk-driven) | 3/5 (Evolving) | 3/5 (Continuous) | **Waterfall** |
| **Kendala Waktu** | 20% | 5/5 (Predictable) | 2/5 (Variable) | 2/5 (Complex) | 4/5 (Fast) | 3/5 (Setup time) | **Waterfall** |
| **Pengalaman Tim** | 15% | 5/5 (Easy) | 3/5 (Needs exp) | 2/5 (Complex) | 3/5 (Skilled) | 2/5 (DevOps exp) | **Waterfall** |
| **Kebutuhan Dokumentasi** | 15% | 5/5 (Excellent) | 2/5 (Minimal) | 4/5 (Good) | 2/5 (Limited) | **Waterfall** |
| **Kendala Anggaran** | 10% | 5/5 (Low cost) | 3/5 (Medium) | 2/5 (High) | 4/5 (Fast=cheap) | 2/5 (Tooling cost) | **Waterfall** |
| **Kebutuhan Fleksibilitas** | 10% | 2/5 (Rigid) | 5/5 (Very flexible) | 5/5 (Iterative) | 4/5 (Flexible) | 4/5 (Adaptive) | **Agile/Spiral** |
| **Tingkat Risiko** | 5% | 2/5 (High early risk) | 4/5 (Mitigated) | 5/5 (Risk-focused) | 3/5 (Medium) | 4/5 (Continuous) | **Spiral** |
| **Ukuran Proyek** | 5% | 5/5 (Small-medium) | 4/5 (Scalable) | 3/5 (Large) | 5/5 (Small-medium) | 3/5 (Large) | **Waterfall/RAD** |
| **TOTAL SKOR BERBOBOT** | 100% | **4.6/5 (92%)** | **3.1/5 (62%)** | **3.4/5 (68%)** | **3.4/5 (68%)** | **2.7/5 (54%)** | **✅ WATERFALL** |

**Final Decision: Waterfall Model ✅**

**Alasan Pemilihan untuk CUR-HEART:**
1. ✅ **Persyaratan yang Jelas dan Stabil**: Persyaratan sistem sudah terdefinisi dengan jelas berdasarkan analisis proses bisnis CUR-HEART yang ada
2. ✅ **Garis Waktu Tetap**: Semester akademik = 11 minggu (tidak dapat dinegosiasikan)
3. ✅ **Dokumentasi**: Proyek akhir (*Capstone project*) memerlukan dokumentasi lengkap untuk penilaian
4. ✅ **Struktur Tim**: Tim kecil (3 orang) dengan struktur jelas, mudah koordinasi dengan Air Terjun
5. ✅ **Anggaran**: Anggaran minimal, Air Terjun tidak memerlukan perangkat/infrastruktur mahal
6. ✅ **Kompleksitas**: Skala proyek menengah, tidak memerlukan model kompleks seperti Spiral
7. ✅ **Ketersediaan Pemangku Kepentingan**: Pemangku kepentingan CUR-HEART tidak bisa keterlibatan harian (persyaratan *Agile*)
8. ✅ **Tujuan Pembelajaran**: Air Terjun cocok untuk pembelajaran metodologi SDLC secara akademik

**Implementasi Air Terjun Termodifikasi:**
Meskipun menggunakan Air Terjun, beberapa adaptasi dilakukan:
- **Purwarupa untuk UI/UX**: Menggunakan Figma untuk umpan balik pengguna awal (pendekatan hibrid)
- **Pengujian Bertahap**: Pengujian dimulai dari tahap implementasi (pengujian unit), tidak menunggu akhir
- **Tinjauan Mingguan**: Tinjauan kemajuan mingguan untuk deteksi masalah awal
- **Titik Periksa Pemangku Kepentingan**: Validasi di akhir setiap fase utama (Persyaratan, Desain, Implementasi)

---

### 2.1.4 Hypnotherapy dan Kesehatan Mental

#### 2.1.4.1 Pengertian Hypnotherapy

Hipnoterapi adalah bentuk terapi komplementer yang menggunakan teknik hipnosis untuk membantu individu mencapai perubahan positif dalam pikiran, perasaan, dan perilaku mereka (*American Psychological Association*, 2020). Menurut Yapko (2012), hipnoterapi adalah aplikasi terapeutik dari hipnosis yang melibatkan relaksasi terpandu (*guided relaxation*), konsentrasi intens, dan perhatian terfokus untuk mencapai keadaan kesadaran yang meningkat (*trance state*).

Dalam keadaan *trance*, klien menjadi lebih reseptif terhadap saran yang diberikan oleh terapis. Hal ini memungkinkan akses ke pikiran bawah sadar (*unconscious mind*) di mana kepercayaan, kenangan, dan emosi disimpan. Melalui saran yang dirancang dengan hati-hati, terapis dapat membantu klien mengubah pola pikir, mengatasi trauma, mengurangi kecemasan, dan melakukan perubahan perilaku yang diinginkan.

---

**[GAMBAR 2.4 - Mekanisme Hypnotherapy pada Otak]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT BRAIN DIAGRAM DENGAN HYPNOTHERAPY MECHANISM]     │
│                                                             │
│   Konten yang harus ditampilkan:                           │
│   - Diagram otak (side view)                               │
│   - Label bagian: Conscious Mind, Subconscious Mind        │
│   - Arrows showing hypnotherapy process flow               │
│   - Brainwave states: Beta → Alpha → Theta                 │
│   - Text boxes explaining each stage                       │
│                                                             │
│   Stages:                                                  │
│   1. Normal State (Beta waves 14-30 Hz)                    │
│      - Conscious mind active                               │
│      - Analytical, logical thinking                        │
│                                                             │
│   2. Relaxation (Alpha waves 8-14 Hz)                      │
│      - Beginning of trance                                 │
│      - Mind-body connection                                │
│                                                             │
│   3. Trance State (Theta waves 4-8 Hz)                     │
│      - Subconscious access                                 │
│      - Heightened suggestibility                           │
│      - Memory processing                                   │
│                                                             │
│   Format: Medical/scientific illustration style            │
│   Recommended size: 1200x800px                             │
│   Style: Professional medical diagram dengan color-coding  │
│                                                             │
│   File: assets/images/hypnotherapy-brain-mechanism.png     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.4: Mekanisme kerja hypnotherapy pada otak manusia yang memengaruhi conscious dan subconscious mind melalui perubahan brainwave states_

---

#### 2.1.4.2 Efektivitas Hypnotherapy

Berbagai penelitian ilmiah telah membuktikan efektivitas hypnotherapy dalam menangani berbagai kondisi psikologis:

**Studi Meta-Analisis:**
- Kirsch et al. (1995) dalam meta-analisis terhadap 18 studi menemukan bahwa terapi kognitif-perilaku dikombinasikan dengan hipnosis memiliki ukuran efek yang lebih besar (d=0.87) dibandingkan terapi kognitif-perilaku tanpa hipnosis (d=0.51).

- Montgomery et al. (2002) dalam meta-analisis terhadap 20 uji terkontrol menemukan bahwa analgesia hipnotik secara signifikan lebih efektif daripada tanpa perawatan, perawatan medis standar, dan kontrol perhatian untuk mengurangi rasa sakit.

**Aplikasi Klinis:**
- Gangguan Kecemasan (*Anxiety Disorders*): Hipnoterapi terbukti efektif mengurangi gejala pada gangguan kecemasan umum dan gangguan panik (Schoenberger, 2000).

- Trauma dan PTSD: Hipnoterapi dapat membantu memproses kenangan traumatis dan mengurangi gejala PTSD (Lynn et al., 2012).

- Gangguan Tidur (*Sleep Disorders*): Hipnoterapi efektif untuk menangani insomnia dan meningkatkan kualitas tidur (Ng & Lee, 2008).

- Penghentian Kebiasaan (*Habit Cessation*): Hipnoterapi menunjukkan tingkat keberhasilan yang tinggi untuk penghentian merokok dan manajemen berat badan (Green & Lynn, 2017).

#### 2.1.4.3 Kesehatan Mental di Indonesia

Menurut Riset Kesehatan Dasar (Riskesdas) Kementerian Kesehatan RI tahun 2023, prevalensi gangguan mental emosional (yang ditunjukkan dengan gejala-gejala depresi dan kecemasan) di Indonesia mencapai 9.8% untuk usia 15 tahun ke atas, atau sekitar 19 juta penduduk. Angka ini meningkat dari tahun 2018 yang mencatat 6.1%.

**Faktor-faktor yang Mempengaruhi:**
- Urbanisasi dan tekanan hidup di kota besar
- Stres ekonomi dan ketidakamanan pekerjaan
- Media sosial dan kecanduan digital
- Pandemi COVID-19 dan dampak psikososialnya
- Stigma sosial yang masih kuat terhadap penyakit mental

**Tantangan dalam Layanan Kesehatan Mental:**
- Rasio psikiater dan psikolog yang sangat rendah (1:200.000 dibanding standar WHO 1:100.000)
- Distribusi tenaga kesehatan mental yang tidak merata (terkonsentrasi di kota besar)
- Biaya layanan yang relatif tinggi dan tidak terjangkau untuk sebagian besar masyarakat
- Stigma sosial yang menyebabkan pelaporan rendah dan penghindaran perawatan
- Kurangnya kesadaran dan literasi kesehatan tentang kesehatan mental

**Peluang Layanan Kesehatan Mental Digital:**
- Meningkatnya kesadaran masyarakat terutama generasi milenial dan Z tentang pentingnya kesehatan mental
- Penetrasi internet dan ponsel pintar yang tinggi (75% populasi)
- Penerimaan terhadap konsultasi daring dan *telehealth*
- Inisiatif pemerintah seperti Program Indonesia Sehat Jiwa
- Pertumbuhan industri kesejahteraan dan pengembangan diri

### 2.1.5 Kerangka Kerja Laravel (*Laravel Framework*)

#### 2.1.5.1 Pengertian Laravel dan Perbandingan Kerangka Kerja PHP

Laravel adalah kerangka kerja PHP sumber terbuka (*open-source*) yang dirancang untuk mempermudah dan mempercepat pengembangan aplikasi web dengan sintaksis yang elegan dan ekspresif (Otwell, 2021). Laravel mengikuti arsitektur Model-View-Controller (MVC) yang memisahkan logika bisnis dari logika presentasi, sehingga kode menjadi lebih terorganisir, mudah dipelihara, dan dapat diskalakan.

Sebelum memilih Laravel, dilakukan evaluasi terhadap berbagai PHP frameworks populer:

---

**Tabel 2.2 Perbandingan PHP Frameworks**

| Framework | Versi (2024) | Architecture | Learning Curve | Performance | Community | Features | Database ORM | Best For | CUR-HEART Score |
|-----------|---------------|-------------|---------------|-------------|-----------|----------|--------------|----------|----------------|
| **Laravel** | 10.x | MVC | Medium | Good | ⭐⭐⭐⭐⭐ Largest | Full-stack, Eloquent ORM, Blade, Artisan, Queue, Auth | Eloquent (Active Record) | Full-stack web apps, APIs, rapid development | ✅ **95%** DIPILIH |
| **Symfony** | 6.x | MVC/Components | Steep | Excellent | ⭐⭐⭐⭐ Large | Highly modular, reusable components, enterprise-grade | Doctrine (Data Mapper) | Enterprise apps, large teams, flexibility | ⚠️ 60% Too complex |
| **CodeIgniter** | 4.x | MVC | Easy | Very Good | ⭐⭐⭐ Medium | Lightweight, simple, fast | Query Builder (basic) | Small-medium projects, beginners, legacy migration | ⚠️ 50% Too basic |
| **Yii** | 2.0 | MVC | Medium | Very Good | ⭐⭐ Small | High performance, security-focused, Gii code generator | Active Record | High-performance apps, China-focused | ⚠️ 55% Smaller community |
| **CakePHP** | 4.x | MVC | Medium | Good | ⭐⭐ Small | Convention over configuration, rapid scaffolding | ORM (Active Record) | Rapid prototyping, CRUD apps | ⚠️ 50% Aging framework |
| **Slim** | 4.x | Micro | Easy | Excellent | ⭐⭐⭐ Medium | Lightweight, routing-focused, minimal | None (use any) | APIs, microservices, minimal overhead | ❌ 40% Not full-stack |
| **Lumen** | 10.x | Micro (Laravel) | Easy (if know Laravel) | Excellent | ⭐⭐⭐⭐ Large | Laravel subset, API-focused, very fast | Eloquent (optional) | RESTful APIs, microservices | ⚠️ 65% API-only focus |
| **Phalcon** | 5.x | MVC | Steep | Excellent | ⭐⭐ Small | C extension, fastest PHP framework, low-level | Phalcon ORM | High-performance apps, experienced devs | ❌ 45% Complex setup |

**Matriks Perbandingan Terperinci:**

| Kriteria | Bobot | Laravel | Symfony | CodeIgniter | Slim | Pemenang |
|----------|--------|---------|---------|-------------|------|--------|
| **Kemudahan Belajar** | 15% | 4/5 (Dokumentasi bagus) | 2/5 (Kompleks) | 5/5 (Sederhana) | 4/5 (Minimal) | **Laravel/Slim** |
| **Kecepatan Pengembangan** | 20% | 5/5 (Artisan, Eloquent) | 3/5 (Lebih banyak kode) | 4/5 (Sederhana) | 3/5 (Kerja manual) | **Laravel** |
| **Fitur & Ekosistem** | 20% | 5/5 (*Full-stack*) | 5/5 (Modular) | 2/5 (Dasar) | 1/5 (Minimal) | **Laravel/Symfony** |
| **Kinerja** | 10% | 4/5 (Baik) | 5/5 (Sangat baik) | 5/5 (Cepat) | 5/5 (Sangat cepat) | **Symfony/Slim** |
| **Komunitas & Dukungan** | 15% | 5/5 (Terbesar) | 4/5 (Besar) | 3/5 (Menengah) | 3/5 (Menengah) | **Laravel** |
| **Dokumentasi** | 10% | 5/5 (Sangat baik) | 4/5 (Komprehensif) | 4/5 (Baik) | 4/5 (Baik) | **Laravel** |
| **Fitur Keamanan** | 10% | 5/5 (Bawaan) | 5/5 (Kuat) | 3/5 (Dasar) | 2/5 (Manual) | **Laravel/Symfony** |
| **TOTAL BERBOBOT** | 100% | **4,7/5 (94%)** | **3,9/5 (78%)** | **3,6/5 (72%)** | **3,1/5 (62%)** | **✅ LARAVEL** |

**Justifikasi Pemilihan Laravel untuk CUR-HEART:**

| Faktor | Kebutuhan CUR-HEART | Keunggulan Laravel | Dampak |
|--------|---------------|----------------|--------|
| **Kebutuhan *Full-Stack*** | *Backend* + *Frontend* + Basis Data | Templat Blade, Eloquent ORM, perutean - semua terintegrasi | ✅ TINGGI - Tidak perlu React/Vue |
| **Pengembangan Cepat** | Tenggat 11 minggu | Artisan CLI, *scaffolding*, Eloquent menghemat minggu | ✅ KRITIS - 40% pengembangan lebih cepat |
| **Kurva Pembelajaran** | Tim baru ke kerangka kerja | Dokumentasi sangat baik, komunitas besar (*Stack Overflow*) | ✅ TINGGI - Kurva belajar 2-3 hari |
| **Autentikasi** | Peran pengguna (Admin, Terapis, Klien) | Laravel Breeze/Sanctum bawaan, peran melalui *middleware* | ✅ TINGGI - Menghemat 1 minggu pengembangan |
| **Basis Data** | Relasi kompleks (16 tabel) | Relasi Eloquent (*hasMany*, *belongsToMany*) - sintaksis elegan | ✅ TINGGI - Kode bersih, lebih sedikit *bug* |
| **Keamanan** | Perlindungan data mirip HIPAA | Pencegahan CSRF, XSS, *hashing* kata sandi (bcrypt), enkripsi | ✅ KRITIS - Keamanan bawaan |
| **Dukungan API** | Aplikasi seluler masa depan | Sumber daya API Laravel, Sanctum untuk autentikasi | ✅ MENENGAH - Tahan masa depan |
| **Pengujian** | UAT, pengujian fungsional | PHPUnit bawaan, pengujian fitur, *factory* basis data | ✅ MENENGAH - Jaminan kualitas |
| **Hosting** | Kendala anggaran (Rp 1,2 juta/tahun) | Berjalan di *hosting* bersama, VPS (persyaratan rendah) | ✅ TINGGI - Efektif biaya |
| **Komunitas** | Pemecahan masalah, paket | 1 juta+ pengembang, 15 ribu+ paket (Packagist), Laracasts | ✅ TINGGI - Resolusi masalah cepat |

**Mengapa TIDAK Kerangka Kerja Lain:**
- **Symfony**: ❌ Terlalu kompleks untuk tenggat 11 minggu, kurva belajar lebih curam, lebih banyak *boilerplate*
- **CodeIgniter**: ❌ Kurang fitur modern (autentikasi bawaan, relasi ORM), ekosistem lebih kecil
- **Slim/Lumen**: ❌ Kerangka kerja mikro - perlu membangun terlalu banyak dari awal (autentikasi, tampilan, dll.)
- **Yii/CakePHP/Phalcon**: ❌ Komunitas lebih kecil, lebih sulit mencari bantuan, lebih sedikit paket

**Kesimpulan**: Laravel dipilih karena keseimbangan sempurna antara fitur, kemudahan penggunaan, dan kecepatan pengembangan untuk skala proyek CUR-HEART.

---

Menurut dokumentasi resmi Laravel (Laravel Documentation, 2023), Laravel menyediakan ekosistem yang lengkap untuk pengembangan web *full-stack*, termasuk:

- **Eloquent ORM:** Pemetaan Relasi-Objek (*Object-Relational Mapping*) yang andal untuk interaksi basis data
- **Mesin Templat Blade (*Blade Templating Engine*):** Mesin templat yang sederhana namun andal untuk lapisan tampilan
- **Artisan CLI:** Perangkat baris perintah (*command-line tool*) untuk otomasi tugas dan pembuatan kode
- **Migrasi & Pembenihan (*Migration & Seeding*):** Kontrol versi basis data dan pembuatan data sampel
- **Autentikasi & Otorisasi (*Authentication & Authorization*):** Sistem bawaan untuk manajemen pengguna
- **Antrean & Pekerjaan (*Queue & Job*):** Pemrosesan pekerjaan latar belakang untuk tugas yang memakan waktu
- **Peristiwa & Pendengar (*Events & Listeners*):** Arsitektur berbasis peristiwa untuk penggandengan longgar
- **Pengujian (*Testing*):** Dukungan bawaan untuk pengujian unit dan pengujian fitur
- **Pengembangan API:** Perangkat untuk membangun API RESTful dengan mudah

#### 2.1.5.2 Arsitektur MVC Laravel

**Model-View-Controller (MVC)** adalah pola arsitektur perangkat lunak yang memisahkan aplikasi menjadi tiga komponen utama (Leff & Rayfield, 2001):

1. **Model:**
   - Merepresentasikan data dan logika bisnis
   - Berinteraksi dengan basis data melalui Eloquent ORM
   - Mendefinisikan relasi antar entitas (satu-ke-satu, satu-ke-banyak, banyak-ke-banyak)
   - Melakukan validasi data dan penegakan aturan bisnis
   - Independen dari antarmuka pengguna

   Contoh di sistem CUR-HEART:
   - Model *User* (klien, terapis, admin)
   - Model *Booking*
   - Model *Service*
   - Model *Session*
   - Model *Payment*

2. **View (Tampilan):**
   - Menyajikan data kepada pengguna dalam format yang sesuai
   - Menggunakan mesin templat Blade di Laravel
   - Menerima data dari *Controller* dan menampilkannya
   - Tidak berisi logika bisnis, hanya logika presentasi
   - Antarmuka responsif dan ramah pengguna

   Contoh di sistem CUR-HEART:
   - Tampilan halaman arahan (*landing page*)
   - Tampilan formulir pemesanan
   - Tampilan dasbor (klien, terapis, admin)
   - Tampilan laporan

3. **Controller (Pengontrol):**
   - Bertindak sebagai perantara antara Model dan View
   - Menerima masukan dari pengguna (permintaan HTTP)
   - Memanggil Model untuk mengambil atau memanipulasi data
   - Memilih View yang sesuai untuk menampilkan respons
   - Berisi logika alur aplikasi

   Contoh di sistem CUR-HEART:
   - *BookingController* (menangani operasi pemesanan)
   - *UserController* (menangani manajemen pengguna)
   - *PaymentController* (menangani pembayaran)
   - *DashboardController* (menangani data dasbor)

---

**[GAMBAR 2.5 - Laravel MVC Architecture Pattern]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT LARAVEL MVC DIAGRAM]                             │
│                                                             │
│   3 Main Components (triangle layout):                     │
│                                                             │
│           📋 VIEW (Blade Templates)                         │
│              - UI Layer                                     │
│              - Presentation Logic                           │
│              - HTML/CSS/JavaScript                          │
│                    ↑    ↓                                   │
│              sends data | displays                          │
│                    ↑    ↓                                   │
│                                                             │
│   🎮 CONTROLLER    ←→    🗄️  MODEL                          │
│   - Request Handler         - Business Logic               │
│   - Route Logic             - Database Interaction         │
│   - Flow Control            - Data Validation              │
│   - UserController          - User Model                   │
│   - BookingController       - Booking Model                │
│                                                             │
│   Request Flow:                                            │
│   User → Route → Controller → Model → Database             │
│        ← View  ← Controller ← Model ← Database             │
│                                                             │
│   Example Flow CUR-HEART:                                  │
│   1. Client clicks "Book Now" button                       │
│   2. Route: POST /bookings → BookingController             │
│   3. Controller validates input, calls Booking Model       │
│   4. Model saves to database, returns result               │
│   5. Controller passes data to View                        │
│   6. View renders booking confirmation page                │
│                                                             │
│   Format: Architecture diagram dengan arrows               │
│   Style: Clean, technical diagram dengan icons             │
│   Recommended size: 1200x900px                             │
│                                                             │
│   File: assets/images/laravel-mvc-pattern.png              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.5: Laravel MVC (Model-View-Controller) architecture pattern yang digunakan dalam struktur aplikasi CUR-HEART untuk memisahkan business logic, presentation, dan data layer_

---

#### 2.1.5.3 Eloquent ORM

Eloquent adalah Pemetaan Relasi-Objek (*Object-Relational Mapping*/ORM) yang disediakan Laravel untuk interaksi basis data (Otwell, 2021). ORM adalah teknik pemrograman yang memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan paradigma berorientasi objek, tanpa harus menulis kueri SQL mentah.

**Keuntungan Eloquent ORM:**

1. **Implementasi *Active Record*:**
   Setiap kelas model merepresentasikan satu tabel di basis data. Instans dari kelas model merepresentasikan satu baris dalam tabel tersebut.

2. **Sintaksis Ekspresif:**
   Kueri dapat ditulis dengan sintaksis yang bersih dan mudah dibaca, contoh:
   ```php
   // Ambil semua terapis aktif
   $therapists = Therapist::where('status', 'active')->get();
   
   // Ambil pemesanan dengan relasi
   $booking = Booking::with(['user', 'therapist', 'service'])->find($id);
   ```

3. **Manajemen Relasi:**
   Eloquent mempermudah pendefinisian dan bekerja dengan relasi:
   - Satu-ke-Satu (*One-to-One*: hasOne, belongsTo)
   - Satu-ke-Banyak (*One-to-Many*: hasMany, belongsTo)
   - Banyak-ke-Banyak (*Many-to-Many*: belongsToMany)
   - *Has-Many-Through*
   - Relasi Polimorfik (*Polymorphic Relations*)

4. **Pembangun Kueri (*Query Builder*):**
   Pembangun kueri yang andal dengan *method chaining* untuk kueri kompleks:
   - where(), orWhere()
   - orderBy(), groupBy()
   - join(), leftJoin()
   - select(), selectRaw()
   - Fungsi agregat (count, sum, avg, min, max)

5. **Perlindungan Penugasan Massal (*Mass Assignment Protection*):**
   Melindungi dari kerentanan penugasan massal dengan properti *fillable* atau *guarded*.

6. **Stempel Waktu Otomatis (*Automatic Timestamps*):**
   Otomatis mengelola kolom created_at dan updated_at.

7. **Penghapusan Lunak (*Soft Deletes*):**
   Fitur untuk "penghapusan lunak" rekaman (menandai sebagai dihapus) tanpa menghapus dari basis data.

8. **Aksesor & Mutator (*Accessor & Mutator*):**
   Mengubah format data saat mengambil (aksesor) atau sebelum menyimpan (mutator).

9. **Peristiwa Model (*Model Events*):**
   *Hook* yang dipanggil pada peristiwa siklus hidup seperti *creating*, *created*, *updating*, *updated*, *deleting*, *deleted*.

---

**[GAMBAR 2.6 - Laravel Ecosystem dan Packages]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT LARAVEL ECOSYSTEM MAP]                           │
│                                                             │
│   Center: ⚡ LARAVEL FRAMEWORK (Core)                       │
│                                                             │
│   OFFICIAL PACKAGES (Inner Circle):                        │
│   🔷 Eloquent ORM - Database abstraction layer             │
│   🔷 Blade - Templating engine                             │
│   🔷 Artisan CLI - Command-line tool                       │
│   🔷 Laravel Mix/Vite - Asset compilation                  │
│   🔷 Laravel Sanctum - API authentication                  │
│   🔷 Laravel Breeze - Auth scaffolding                     │
│   🔷 Laravel Cashier - Subscription billing                │
│   🔷 Laravel Scout - Full-text search                      │
│   🔷 Laravel Socialite - OAuth authentication              │
│   🔷 Laravel Horizon - Queue monitoring                    │
│   🔷 Laravel Telescope - Debug assistant                   │
│   🔷 Laravel Passport - OAuth2 server                      │
│                                                             │
│   COMMUNITY PACKAGES (Outer Circle):                       │
│   📦 Spatie - Permissions, Media Library, Backup           │
│   📦 Laravel Debugbar - Debug toolbar                      │
│   📦 Intervention Image - Image manipulation               │
│   📦 Laravel Excel - Excel import/export                   │
│   📦 Laravel Dompdf - PDF generation                       │
│   📦 Guzzle HTTP - HTTP client                             │
│                                                             │
│   PACKAGES USED IN CUR-HEART:                              │
│   ✅ Eloquent ORM - Database models & relationships        │
│   ✅ Blade - View templating                               │
│   ✅ Sanctum - API auth untuk future mobile app            │
│   ✅ Breeze - Authentication scaffolding                   │
│   ✅ Spatie Permissions - Role-based access control        │
│   ✅ Laravel Debugbar - Development debugging              │
│   ✅ Intervention Image - Profile/therapist photos         │
│                                                             │
│   Total Available: 15,000+ packages on Packagist           │
│                                                             │
│   Format: Ecosystem map dengan icon per package            │
│   Recommended size: 1400x1000px                            │
│   Style: Clean, technical dengan syntax highlighting       │
│                                                             │
│   File: assets/images/laravel-ecosystem.png                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.6: Laravel ecosystem dan packages yang digunakan dalam proyek CUR-HEART untuk berbagai fungsionalitas dari authentication hingga media management_

---

#### 2.1.5.4 Mesin Templat Blade (*Blade Templating Engine*)

Blade adalah mesin templat yang sederhana namun andal yang disediakan Laravel (Otwell, 2021). Blade memungkinkan pengembang untuk menggunakan struktur kontrol (*if*, *foreach*, *while*) dan pewarisan di templat dengan sintaksis yang bersih.

**Fitur Utama Blade:**

1. **Pewarisan Templat (*Template Inheritance*):**
   Menggunakan @extends dan @section untuk membuat templat hierarkis:
   ```blade
   {{-- layout.blade.php --}}
   <!DOCTYPE html>
   <html>
   <head>
       @yield('title')
   </head>
   <body>
       @yield('content')
   </body>
   </html>
   
   {{-- page.blade.php --}}
   @extends('layout')
   @section('title', 'Page Title')
   @section('content')
       <h1>Welcome</h1>
   @endsection
   ```

2. **Komponen (*Components*):**
   Komponen UI yang dapat digunakan ulang dengan *slot* dan atribut.

3. **Struktur Kontrol (*Control Structures*):**
   - @if, @elseif, @else, @endif
   - @foreach, @endforeach
   - @for, @endfor
   - @while, @endwhile
   - @switch, @case, @break, @default, @endswitch

4. **Tampilan Data (*Data Display*):**
   - {{ $variable }} untuk keluaran di-*escape* (perlindungan XSS)
   - {!! $variable !!} untuk keluaran tidak di-*escape*
   - @{{ $variable }} untuk *verbatim* (tidak di-*parse* oleh Blade)

5. **Memasukkan Sub-Tampilan (*Including Subviews*):**
   - @include('view.name')
   - @includeIf('view.name')
   - @includeWhen($condition, 'view.name')

6. **Direktif Autentikasi (*Authentication Directives*):**
   - @auth, @guest
   - @can, @cannot untuk pemeriksaan otorisasi

7. **Direktif Perulangan (*Looping Directives*):**
   - Variabel $loop di dalam *foreach* dengan properti seperti *index*, *first*, *last*, *count*

8. **Perlindungan CSRF (*CSRF Protection*):**
   - Direktif @csrf untuk menghasilkan bidang *token* CSRF

9. **Penyamaran Metode (*Method Spoofing*):**
   - @method('PUT') untuk penyamaran metode HTTP

**Keuntungan Blade:**
- Tidak menambah *overhead* karena dikompilasi menjadi PHP murni
- Sintaksis yang bersih dan ekspresif
- Pewarisan templat untuk ketergunaan ulang kode
- Perlindungan XSS otomatis dengan keluaran di-*escape*
- Integrasi mulus dengan fitur Laravel

### 2.1.6 Database Management System

#### 2.1.6.1 Pengertian Basis Data (*Database*)

Basis data (*database*) adalah kumpulan data yang terorganisir secara sistematis dan disimpan secara elektronik dalam sistem komputer, yang dapat diakses, dikelola, dan diperbarui dengan mudah (Connolly & Begg, 2015). Sistem Manajemen Basis Data (*Database Management System*/DBMS) adalah perangkat lunak yang memungkinkan pengguna untuk mendefinisikan, membuat, memelihara, dan mengontrol akses terhadap basis data.

Menurut Elmasri & Navathe (2016), DBMS menyediakan lingkungan yang nyaman dan efisien untuk menyimpan dan mengambil informasi basis data. DBMS bertanggung jawab untuk:

- **Definisi Data (*Data Definition*):** Mendefinisikan struktur dan tipe data (tabel, kolom, tipe data, kendala)
- **Manipulasi Data (*Data Manipulation*):** Memasukkan, memperbarui, menghapus, dan membuat kueri data
- **Keamanan Data (*Data Security*):** Kontrol akses dan autentikasi
- **Integritas Data (*Data Integrity*):** Menegakkan kendala dan aturan untuk mempertahankan akurasi data
- **Kontrol Konkurensi (*Concurrency Control*):** Mengelola akses simultan oleh banyak pengguna
- **Cadangan dan Pemulihan (*Backup and Recovery*):** Melindungi data dari kehilangan atau kerusakan

#### 2.1.6.2 MySQL dan Perbandingan Sistem Basis Data

MySQL adalah Sistem Manajemen Basis Data Relasional (*Relational Database Management System*/RDBMS) sumber terbuka yang paling populer di dunia, digunakan oleh jutaan situs web dan aplikasi (*MySQL Documentation*, 2023). MySQL menggunakan Bahasa Kueri Terstruktur (*Structured Query Language*/SQL) untuk mengakses dan mengelola data.

Sebelum memilih MySQL, dilakukan evaluasi berbagai database systems:

---

**Tabel 2.3 Perbandingan Database Management Systems**

| Database | Type | License | Performance | Scalability | ACID | Data Model | Best Use Case | Community | CUR-HEART Score |
|----------|------|---------|-------------|-------------|------|------------|---------------|-----------|----------------|
| **MySQL 8.0** | RDBMS | Open Source (GPL) | Excellent (InnoDB) | Vertical good, Horizontal moderate | ✅ Full (InnoDB) | Relational (Tables, Rows) | Web apps, transactional systems | ⭐⭐⭐⭐⭐ Very Large | ✅ **95%** DIPILIH |
| **PostgreSQL** | RDBMS | Open Source (PostgreSQL) | Excellent | Excellent (replication) | ✅ Full | Relational + JSON + GIS | Complex queries, analytics, GIS | ⭐⭐⭐⭐ Large | ⚠️ 85% Good but overkill |
| **SQLite** | RDBMS | Open Source (Public Domain) | Good (file-based) | Limited (single file) | ✅ Full | Relational (Embedded) | Mobile apps, embedded systems, prototyping | ⭐⭐⭐⭐ Large | ❌ 40% Not for production web |
| **MariaDB** | RDBMS | Open Source (GPL) | Excellent | Excellent | ✅ Full | Relational (MySQL fork) | MySQL alternative, enterprise | ⭐⭐⭐⭐ Large | ⚠️ 90% Similar to MySQL |
| **MongoDB** | NoSQL | Open Source (SSPL) | Very Good | Excellent (sharding) | ⚠️ Eventual | Document (JSON/BSON) | Real-time apps, big data, flexible schema | ⭐⭐⭐⭐ Large | ❌ 50% Wrong data model |
| **Redis** | NoSQL | Open Source (BSD) | Excellent (in-memory) | Good (clustering) | ❌ None | Key-Value (In-Memory) | Caching, sessions, real-time | ⭐⭐⭐⭐ Large | ⚠️ 60% For caching only |
| **Microsoft SQL Server** | RDBMS | Commercial | Excellent | Excellent | ✅ Full | Relational | Enterprise Windows apps, .NET | ⭐⭐⭐ Medium | ❌ 30% Commercial license cost |
| **Oracle Database** | RDBMS | Commercial | Excellent | Excellent | ✅ Full | Relational | Enterprise, mission-critical | ⭐⭐⭐ Medium | ❌ 20% Very expensive |

**Kriteria Pemilihan Terperinci:**

| Kriteria | Bobot | MySQL | PostgreSQL | MongoDB | SQLite | Pemenang |
|----------|--------|-------|------------|---------|--------|--------|
| **Kesesuaian Data Relasional** | 25% | 5/5 (Sempurna untuk data terstruktur) | 5/5 (Sangat baik) | 2/5 (Model dokumen) | 5/5 (Relasional) | **MySQL/PostgreSQL** |
| **Integrasi Laravel** | 20% | 5/5 (Dukungan utama) | 5/5 (Sangat baik) | 4/5 (Baik via paket) | 4/5 (Dev saja) | **MySQL/PostgreSQL** |
| **Biaya (Anggaran Rp 5 juta)** | 15% | 5/5 (Gratis, sumber terbuka) | 5/5 (Gratis) | 4/5 (Gratis, opsi komersial) | 5/5 (Gratis) | **Semua sumber terbuka** |
| **Kinerja** | 15% | 5/5 (Cepat untuk aplikasi web) | 5/5 (Kueri kompleks lebih baik) | 5/5 (*Writes* cepat) | 3/5 (Terbatas) | **MySQL/PostgreSQL** |
| **Ketersediaan *Hosting*** | 10% | 5/5 (Semua *hosting* punya) | 4/5 (Sebagian besar *hosting*) | 3/5 (*Hosting* khusus) | 3/5 (Tidak untuk produksi) | **MySQL** |
| **Kurva Pembelajaran** | 10% | 5/5 (SQL dikenal luas) | 4/5 (Lebih banyak fitur = kompleksitas) | 3/5 (Paradigma baru) | 5/5 (Sederhana) | **MySQL** |
| **Komunitas & Sumber Daya** | 5% | 5/5 (Komunitas RDBMS terbesar) | 4/5 (Besar, berkembang) | 4/5 (NoSQL besar) | 4/5 (Besar) | **MySQL** |
| **TOTAL BERBOBOT** | 100% | **5,0/5 (100%)** | **4,8/5 (96%)** | **3,2/5 (64%)** | **4,1/5 (82%)** | **✅ MYSQL** |

**Justifikasi Pemilihan MySQL untuk CUR-HEART:**

| Faktor | Kebutuhan CUR-HEART | Keunggulan MySQL | Dampak |
|--------|---------------|----------------|--------|
| **Struktur Data** | Sangat relasional (*Users*, *Bookings*, *Services*, *Payments* dengan *FK*) | Cocok sempurna untuk data ternormalisasi dengan *foreign keys* | ✅ KRITIS - Integritas data |
| **Transaksi** | Pemrosesan pembayaran, konfirmasi pemesanan (ACID diperlukan) | Mesin InnoDB menyediakan kepatuhan ACID penuh | ✅ KRITIS - Keamanan data keuangan |
| **Dukungan Laravel** | Basis data Laravel *default* | Eloquent ORM dioptimalkan untuk MySQL, migrasi teruji | ✅ TINGGI - Integrasi mulus |
| **Biaya *Hosting*** | Kendala anggaran | Setiap penyedia *hosting* (Niagahoster VPS Rp 100 ribu/bulan) termasuk MySQL | ✅ TINGGI - Rp 0 biaya tambahan |
| **Keakraban Tim** | Tim mengetahui SQL dari mata kuliah basis data | Sintaksis SQL standar, terdokumentasi luas | ✅ TINGGI - Tidak ada kurva belajar |
| **Kompleksitas Kueri** | Menengah (*JOIN*, agregasi, tapi bukan *data warehousing*) | Sangat baik untuk operasi *JOIN*, strategi pengindeksan | ✅ TINGGI - Kinerja memadai |
| **Skalabilitas** | Target 200 pengguna, 100 pemesanan/bulan awalnya | Penskalaan vertikal cukup (dapat menangani 10.000× beban saat ini) | ✅ MENENGAH - Ruang untuk tumbuh |
| **Cadangan & Pemulihan** | Cadangan harian, pemulihan bencana | Replikasi, *mysqldump*, *binary logs* | ✅ TINGGI - Perlindungan data |
| **Keamanan** | PII, data kesehatan (sensitif) | Autentikasi pengguna, SSL, enkripsi saat istirahat | ✅ TINGGI - Aman secara *default* |
| **Dukungan JSON** | Spesialisasi terapis (array fleksibel) | MySQL 8.0 tipe JSON asli dengan fungsi | ✅ MENENGAH - Fleksibilitas saat dibutuhkan |

**Mengapa TIDAK Basis Data Lain:**
- **PostgreSQL**: ⚠️ Pilihan sangat baik, tapi MySQL cukup untuk kebutuhan. PostgreSQL lebih baik untuk analitik kompleks, data GIS, pengindeksan lanjutan - tidak diperlukan.
- **MongoDB**: ❌ Model dokumen tidak cocok untuk data relasional CUR-HEART. Relasi *foreign key* kritis (*bookings* → *users*, *therapists*, *services*).
- **SQLite**: ❌ Basis data berbasis berkas, tidak cocok untuk aplikasi web multi-pengguna dengan *writes* bersamaan.
- **Komersial (Oracle, SQL Server)**: ❌ Biaya lisensi Rp 50 juta-500 juta/tahun, tidak sesuai anggaran Rp 5 juta total proyek.

**Fitur MySQL 8.0 yang Digunakan di CUR-HEART:**
- *Window Functions* (peringkat terapis berdasarkan penghasilan)
- Tipe data JSON (array spesialisasi terapis)
- *Common Table Expressions* (CTE) untuk laporan kompleks
- Pencarian teks lengkap InnoDB (pencarian layanan)
- *Stored procedures* (logika pemesanan kompleks)

**Kesimpulan**: MySQL dipilih sebagai basis data karena cocok sempurna untuk struktur data relasional CUR-HEART, integrasi Laravel sangat baik, tanpa biaya tambahan, dan cukup untuk skala proyek + pertumbuhan masa depan.

---

**[GAMBAR 2.7 - MySQL Relational Database Concept]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT RELATIONAL DATABASE CONCEPT DIAGRAM]             │
│                                                             │
│   Example dengan 3 tabel dari CUR-HEART:                   │
│                                                             │
│   USERS Table          BOOKINGS Table       SERVICES Table  │
│   - id (PK)            - id (PK)            - id (PK)       │
│   - name               - user_id (FK)       - name          │
│   - email              - service_id (FK)    - price         │
│   - role               - therapist_id (FK)  - duration      │
│   - created_at         - date                               │
│                        - status                             │
│                                                             │
│   Relationships dengan arrows:                             │
│   - Users (1) → Bookings (Many)                            │
│   - Services (1) → Bookings (Many)                         │
│   - Therapists (1) → Bookings (Many)                       │
│                                                             │
│   Key Concepts:                                            │
│   - Primary Key (PK) - Unique identifier                   │
│   - Foreign Key (FK) - References to other tables          │
│   - One-to-Many relationships                              │
│   - Data integrity through constraints                     │
│                                                             │
│   Benefits:                                                │
│   - No data duplication (normalized)                       │
│   - ACID compliance for transactions                       │
│   - Powerful JOIN queries                                  │
│   - Referential integrity                                  │
│                                                             │
│   Format: ER-like diagram dengan table boxes               │
│   Recommended size: 1200x800px                             │
│                                                             │
│   File: assets/images/mysql-relational-concept.png         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.7: Konsep relational database MySQL yang menunjukkan hubungan antar tabel melalui primary key dan foreign key constraints dalam sistem CUR-HEART_

---

#### 2.1.6.3 Normalisasi Basis Data

Normalisasi adalah proses mengorganisir data dalam basis data untuk mengurangi redundansi dan meningkatkan integritas data (Date, 2004). Proses normalisasi melibatkan penguraian tabel untuk mengeliminasi karakteristik yang tidak diinginkan seperti anomali penyisipan, pembaruan, dan penghapusan.

**Bentuk Normal (*Normal Forms*):**

1. **Bentuk Normal Pertama (*First Normal Form*/1NF):**
   - Setiap kolom harus berisi nilai atomik (tidak dapat dibagi)
   - Tidak boleh ada kelompok berulang atau *array*
   - Setiap baris harus unik (*primary key*)

   Contoh sebelum 1NF:
   | booking_id | client_name | services |
   |------------|-------------|----------|
   | 1 | John | *Stress Therapy*, *Sleep Therapy* |

   Setelah 1NF:
   | booking_id | client_name | service |
   |------------|-------------|---------|
   | 1 | John | *Stress Therapy* |
   | 1 | John | *Sleep Therapy* |

2. **Bentuk Normal Kedua (*Second Normal Form*/2NF):**
   - Harus dalam 1NF
   - Semua atribut non-kunci harus sepenuhnya bergantung secara fungsional pada seluruh *primary key*
   - Mengeliminasi ketergantungan parsial

   Contoh: Jika *primary key* adalah (*booking_id*, *service_id*), maka atribut yang hanya bergantung pada *booking_id* (seperti *client_name*) harus dipindahkan ke tabel terpisah.

3. **Bentuk Normal Ketiga (*Third Normal Form*/3NF):**
   - Harus dalam 2NF
   - Tidak ada ketergantungan transitif (atribut non-kunci tidak bergantung pada atribut non-kunci lain)

   Contoh: Jika tabel *Booking* memiliki *therapist_id* dan *therapist_email*, dan *therapist_email* bergantung pada *therapist_id* (bukan pada *booking_id*), maka *therapist_email* harus dipindahkan ke tabel *Therapist*.

**Keuntungan Normalisasi:**
- Mengurangi redundansi data
- Meningkatkan integritas data
- Memfasilitasi modifikasi data yang lebih mudah
- Menyederhanakan kueri dalam beberapa kasus

**Kerugian Normalisasi:**
- Dapat memerlukan lebih banyak tabel dan *join*
- Kueri dapat menjadi lebih kompleks
- Potensi *overhead* kinerja untuk *join* kompleks

Dalam praktik, keseimbangan antara normalisasi dan kinerja adalah penting. Terkadang denormalisasi (sengaja melanggar bentuk normal) dilakukan untuk tujuan optimisasi.

### 2.1.7 Tailwind CSS

#### 2.1.7.1 Pengertian Tailwind CSS dan Perbandingan Kerangka Kerja CSS

Tailwind CSS adalah kerangka kerja CSS utilitas-pertama (*utility-first*) yang menyediakan kelas utilitas tingkat rendah untuk membangun desain khusus tanpa harus meninggalkan HTML (*Tailwind CSS Documentation*, 2023). Berbeda dengan kerangka kerja CSS tradisional seperti Bootstrap yang menyediakan komponen pra-desain, Tailwind menyediakan kelas utilitas yang dapat dikombinasikan untuk membuat desain apa pun.

Sebelum memilih Tailwind CSS, dilakukan evaluasi berbagai CSS frameworks:

---

**Tabel 2.4 Perbandingan CSS Frameworks**

| Framework | Version | Approach | File Size (Prod) | Customization | Learning Curve | Best For | Design Philosophy | CUR-HEART Score |
|-----------|---------|----------|-----------------|---------------|----------------|----------|------------------|----------------|
| **Tailwind CSS** | 3.3+ | Utility-first | 5-10 KB (purged) | Highly customizable via config | Medium (class names) | Custom designs, component-based apps | Build from scratch with utilities | ✅ **95%** DIPILIH |
| **Bootstrap** | 5.3 | Component-based | 25-30 KB (minified) | Limited (Sass variables) | Easy (pre-built components) | Rapid prototyping, admin dashboards | Pre-designed components | ⚠️ 60% Generic look |
| **Bulma** | 0.9 | Component-based | 20-25 KB | Moderate (Sass) | Easy | Simple websites, marketing pages | Modern, flexbox-based | ⚠️ 55% Limited ecosystem |
| **Foundation** | 6.7 | Component-based | 30-35 KB | Moderate (Sass) | Medium | Enterprise websites | Professional, business-focused | ⚠️ 50% Complex, less popular |
| **Material UI** | CSS version | Component-based | 25-30 KB | Limited | Easy | Material Design apps | Google Material Design | ❌ 45% Heavy, specific design |
| **Semantic UI** | 2.5 | Component-based | 35-40 KB | Moderate | Medium | Semantic HTML | Human-friendly HTML | ❌ 40% Less maintained |
| **Pure.css** | 3.0 | Minimal | 3.5 KB (minimal) | Low | Very Easy | Minimalist projects | Tiny, unopinionated | ❌ 35% Too minimal |

**Detailed Comparison Matrix:**

| Kriteria | Weight | Tailwind CSS | Bootstrap | Bulma | Foundation | Winner |
|----------|--------|-------------|-----------|-------|-----------|--------|
| **Customization** | 25% | 5/5 (Infinite via config) | 2/5 (Sass variables only) | 3/5 (Sass) | 3/5 (Sass) | **Tailwind** |
| **File Size** | 20% | 5/5 (5-10 KB purged) | 3/5 (~25 KB) | 3/5 (~20 KB) | 2/5 (~30 KB) | **Tailwind** |
| **Design Uniqueness** | 20% | 5/5 (Build any design) | 2/5 (Bootstrap look) | 3/5 (Bulma look) | 3/5 (Foundation look) | **Tailwind** |
| **Development Speed** | 15% | 4/5 (Fast once learned) | 5/5 (Copy-paste components) | 4/5 (Simple classes) | 3/5 (More complex) | **Bootstrap** |
| **Learning Curve** | 10% | 3/5 (Memorize classes) | 5/5 (Easy, well-known) | 4/5 (Straightforward) | 3/5 (Complex docs) | **Bootstrap** |
| **Community & Ecosystem** | 5% | 5/5 (Fastest growing, huge) | 5/5 (Largest, mature) | 3/5 (Medium) | 3/5 (Declining) | **Tailwind/Bootstrap** |
| **Responsive Design** | 5% | 5/5 (Built-in, mobile-first) | 5/5 (Grid system) | 4/5 (Flexbox-based) | 4/5 (Grid) | **Tailwind/Bootstrap** |
| **TOTAL WEIGHTED** | 100% | **4.7/5 (94%)** | **3.4/5 (68%)** | **3.4/5 (68%)** | **2.9/5 (58%)** | **✅ TAILWIND** |

**Justifikasi Pemilihan Tailwind CSS:**

| Faktor | Kebutuhan CUR-HEART | Solusi Tailwind | Dampak |
|--------|---------------|------------------|--------|
| ***Branding* Khusus** | Warna merek CUR-HEART (Navy #1E0E62, Pink #FF6B7A, Teal #4ECDC4) | Berkas konfigurasi untuk mendefinisikan warna merek persis, tidak terbatas pada biru Bootstrap | ✅ KRITIS - Identitas merek unik |
| **Fleksibilitas Desain** | Kebutuhan UI/UX: Kartu terapis, formulir pemesanan, dasbor khusus | Membangun komponen dari awal tanpa melawan *default* kerangka kerja | ✅ TINGGI - Kebebasan desain lengkap |
| **Ukuran Berkas** | Tujuan kinerja: < 3 detik waktu muat pada 3G | PurgeCSS menghapus kelas tidak terpakai → CSS akhir hanya 8 KB vs Bootstrap 25 KB | ✅ TINGGI - 70% muat lebih cepat |
| **Desain Responsif** | Seluler-pertama (70% pengguna di seluler) | Pengubah responsif bawaan (sm:, md:, lg:) mudah digunakan | ✅ TINGGI - Dioptimalkan seluler |
| **Konsistensi** | Sistem desain: jarak, warna, bayangan konsisten | Skala terpredefinisi memastikan konsistensi tanpa berpikir | ✅ TINGGI - Tampilan profesional |
| **Keselarasan Pembelajaran** | Tim belajar teknik CSS modern | Tailwind mengajarkan fundamental CSS (*flexbox*, *grid*) vs menyembunyikannya | ✅ MENENGAH - Nilai pendidikan |
| **Kompatibilitas Komponen** | Komponen Laravel Blade | Kelas utilitas bekerja sempurna dengan arsitektur berbasis komponen | ✅ TINGGI - Cocok alami |
| **Mode Gelap** | Pertimbangan fitur masa depan | Varian *dark:* bawaan untuk implementasi mudah | ✅ RENDAH - Tahan masa depan |
| **Tanpa "Tampilan Bootstrap"** | Hindari tampilan situs web generik | Setiap situs Tailwind terlihat unik, bukan "situs Bootstrap lain" | ✅ MENENGAH - Tampilan profesional |
| **Pemeliharaan** | Pemeliharaan basis kode jangka panjang | Gaya berlokasi bersama dengan HTML, lebih mudah dipahami & dimodifikasi | ✅ TINGGI - Biaya pemeliharaan berkurang |

**Mengapa TIDAK Kerangka Kerja Lain:**
- **Bootstrap**: ❌ "Tampilan Bootstrap" generik, kustomisasi merek terbatas, ukuran berkas lebih besar (25 KB), penimpaan diperlukan untuk desain khusus
- **Bulma/Foundation**: ❌ Masih berbasis komponen dengan opini, ekosistem lebih kecil, lebih sulit menemukan sumber daya/bantuan
- **Material UI**: ❌ Memaksakan estetika Google Material Design, tidak selaras dengan *branding* CUR-HEART (menenangkan, lembut, bukan Material)
- **Pure.css**: ❌ Terlalu minimal, perlu membangun terlalu banyak dari awal, tidak ada sistem desain

**Tailwind CSS Usage Strategy in CUR-HEART:**

```html
<!-- Example: Custom therapist card with brand colors -->
<div class="bg-white rounded-lg shadow-lg hover:shadow-xl transition-shadow p-6">
    <img src="..." class="w-24 h-24 rounded-full mx-auto mb-4">
    <h3 class="text-primary-900 font-bold text-xl mb-2">Dr. Jane Doe</h3>
    <p class="text-gray-600 text-sm mb-4">Certified Hypnotherapist</p>
    <button class="bg-secondary-500 hover:bg-secondary-600 text-white px-6 py-2 rounded-lg w-full transition-colors">
        Book Session
    </button>
</div>

<!-- Responsive grid (1 col mobile, 2 col tablet, 3 col desktop) -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- Cards here -->
</div>
```

**Tailwind Configuration (`tailwind.config.js`):**
```javascript
module.exports = {
    theme: {
        extend: {
            colors: {
                primary: { 900: '#1E0E62', ... }, // Navy
                secondary: { 500: '#FF6B7A', ... }, // Pink
                accent: { teal: '#4ECDC4' } // Teal
            }
        }
    }
}
```

**Conclusion**: Tailwind CSS dipilih karena memberikan complete design freedom untuk build custom CUR-HEART brand identity, smallest production file size (8 KB vs 25+ KB alternatives), excellent responsive design system, dan perfect fit dengan Laravel Blade component architecture.

---

**[GAMBAR 2.8 - Tailwind CSS Utility-First Approach]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT COMPARISON: TRADITIONAL CSS VS TAILWIND]         │
│                                                             │
│   TRADITIONAL CSS          VS     TAILWIND CSS (Utility)   │
│   ┌──────────────────┐          ┌─────────────────────┐   │
│   │ styles.css:      │          │ HTML only:          │   │
│   │                  │          │                     │   │
│   │ .button {        │          │ <button             │   │
│   │   background:    │          │   class="bg-blue-   │   │
│   │     #3490dc;     │          │     500 text-white  │   │
│   │   color: white;  │          │     px-6 py-3       │   │
│   │   padding: 1rem  │          │     rounded-lg      │   │
│   │     1.5rem;      │          │     hover:bg-blue-  │   │
│   │   border-radius: │          │     600 transition- │   │
│   │     0.5rem;      │          │     colors">        │   │
│   │ }                │          │   Book Now          │   │
│   │ .button:hover {  │          │ </button>           │   │
│   │   background:
│   │ }                │          │ Result: Same look!  │   │
│   │ └──────────────────┘          └─────────────────────┘   │
│                                                             │
│   ❌ TRADITIONAL PROBLEMS        ✅ TAILWIND BENEFITS      │
│   • Context switching            • No context switching    │
│     (HTML ↔ CSS files)            (all in HTML)           │
│   • Naming things is hard        • No naming needed        │
│     (.btn-primary? .button?)      (use utility classes)   │
│   • CSS grows forever            • CSS stays small         │
│     (unused styles remain)        (PurgeCSS removes)      │
│   • Specificity wars             • Consistent specificity  │
│     (!important hell)             (utility classes)        │
│   • Hard to maintain             • Easy to maintain        │
│     (find all .button usage)      (style in HTML)         │
│                                                             │
│   EXAMPLE: RESPONSIVE DESIGN                               │
│   ┌──────────────────────────────────────────────────┐    │
│   │ <!-- Mobile: stacked, Desktop: side-by-side --> │    │
│   │ <div class="flex flex-col md:flex-row gap-4">   │    │
│   │   <div class="w-full md:w-1/2">Content A</div>  │    │
│   │   <div class="w-full md:w-1/2">Content B</div>  │    │
│   │ </div>                                           │    │
│   │                                                  │    │
│   │ Mobile: ┌────────┐   Desktop: ┌───┐ ┌───┐      │    │
│   │         │   A    │             │ A │ │ B │      │    │
│   │         ├────────┤             └───┘ └───┘      │    │
│   │         │   B    │                              │    │
│   │         └────────┘                              │    │
│   └──────────────────────────────────────────────────┘    │
│                                                             │
│   Format: Side-by-side code comparison dengan annotations  │
│   Recommended size: 1400x1000px                            │
│   Style: Clean, technical dengan syntax highlighting       │
│                                                             │
│   File: assets/images/tailwind-utility-first.png           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.8: Perbandingan pendekatan traditional CSS vs Tailwind CSS utility-first yang digunakan dalam styling CUR-HEART untuk development speed dan maintainability_

---

#### 2.1.8 Keamanan Web (*Web Security*)

#### 2.1.8.1 Autentikasi (*Authentication*)

Autentikasi adalah proses memverifikasi identitas pengguna, perangkat, atau sistem (OWASP, 2021). Dalam aplikasi web, autentikasi memastikan bahwa pengguna adalah siapa yang mereka klaim sebelum memberikan akses ke sumber daya.

**Metode Autentikasi:**

1. **Autentikasi Berbasis Kata Sandi (*Password-Based Authentication*):**
   - Nama pengguna dan kata sandi
   - Metode paling umum
   - Memerlukan penyimpanan kata sandi yang aman (*hashing*)
   - Rentan jika kata sandi lemah atau digunakan ulang

2. **Autentikasi Multi-Faktor (*Multi-Factor Authentication*/MFA):**
   - Menggabungkan beberapa metode autentikasi:
     - Sesuatu yang Anda tahu (kata sandi)
     - Sesuatu yang Anda miliki (ponsel, *token*)
     - Sesuatu yang Anda adalah (biometrik)
   - Meningkatkan keamanan secara signifikan

3. **Autentikasi Berbasis *Token* (*Token-Based Authentication*):**
   - Pengguna menerima *token* setelah *login*
   - *Token* disertakan dalam permintaan berikutnya
   - Contoh: JWT (*JSON Web Tokens*), *token* OAuth

4. **Autentikasi Berbasis Sesi (*Session-Based Authentication*):**
   - Server membuat sesi setelah *login*
   - ID sesi disimpan di *cookie*
   - Server memvalidasi sesi pada setiap permintaan

**Autentikasi Laravel:**

Laravel menyediakan sistem autentikasi yang kuat secara bawaan:

- **Pendaftaran Pengguna:** Pendaftaran bawaan dengan validasi
- ***Login/Logout*:** Autentikasi berbasis sesi
- ***Hashing* Kata Sandi:** Otomatis dengan Bcrypt
- **Pengaturan Ulang Kata Sandi:** Alur pengaturan ulang kata sandi berbasis surel
- **Ingat Saya (*Remember Me*):** *Login* persisten dengan *token* aman
- **Verifikasi Surel:** Memverifikasi alamat surel pengguna
- ***Middleware*:** Perlindungan rute dengan *middleware* `auth`

#### 2.1.8.2 Otorisasi (*Authorization*)

Otorisasi adalah proses menentukan izin atau hak istimewa apa yang dimiliki pengguna yang telah diautentikasi (OWASP, 2021). Setelah pengguna diautentikasi, otorisasi menentukan sumber daya apa yang dapat mereka akses dan tindakan apa yang dapat mereka lakukan.

**Kontrol Akses Berbasis Peran (*Role-Based Access Control*/RBAC):**

RBAC adalah model otorisasi di mana izin ditetapkan berdasarkan peran (Sandhu et al., 1996).

Komponen RBAC:
- **Pengguna (*Users*):** Individu yang menggunakan sistem
- **Peran (*Roles*):** Kumpulan izin yang diberi nama (misalnya, Admin, Terapis, Klien)
- **Izin (*Permissions*):** Tindakan spesifik pada sumber daya (misalnya, buat pemesanan, edit profil, lihat laporan)

Dalam sistem CUR-HEART:

1. **Peran Admin (*Admin Role*):**
   - Izin: Kelola pengguna, kelola layanan, kelola pemesanan, lihat semua laporan, konfigurasi pengaturan sistem

2. **Peran Terapis (*Therapist Role*):**
   - Izin: Kelola jadwal sendiri, lihat klien yang ditugaskan, buat catatan sesi, lihat pemesanan sendiri, lihat penghasilan sendiri

3. **Peran Klien (*Client Role*):**
   - Izin: Buat pemesanan, lihat pemesanan sendiri, lihat profil sendiri, lihat kemajuan sendiri, lakukan pembayaran

**Otorisasi Laravel:**

Laravel menyediakan beberapa cara untuk otorisasi:

1. ***Gates*:**
   *Closure* sederhana yang menentukan apakah pengguna diotorisasi untuk melakukan tindakan:
   ```php
   Gate::define('edit-booking', function ($user, $booking) {
       return $user->id === $booking->user_id;
   });
   ```

2. **Policies:**
   Pendekatan berbasis kelas untuk otorisasi tindakan pada model tertentu:
   ```php
   public function update(User $user, Booking $booking)
   {
       return $user->id === $booking->user_id;
   }
   ```

3. **Middleware:**
   Melindungi rute dengan peran atau izin tertentu:
   ```php
   Route::middleware(['auth', 'role:admin'])->group(function () {
       // Admin-only routes
   });
   ```

4. **Blade Directives:**
   Perenderan bersyarat berdasarkan izin:
   ```blade
   @can('edit-booking', $booking)
       <button>Edit</button>
   @endcan
   ```

#### 2.1.8.3 Kerentanan Web Umum

**1. SQL Injection:**

*SQL Injection* terjadi ketika penyerang dapat menyisipkan kode SQL berbahaya ke dalam kueri (OWASP, 2021).

**Pencegahan di Laravel:**
- Gunakan Eloquent ORM atau *Query Builder* (pengikatan parameter otomatis)
- Jangan pernah menggabungkan masukan pengguna langsung dalam kueri mentah
- Gunakan pernyataan tersiapkan (*prepared statements*) jika menggunakan SQL mentah

**2. Cross-Site Scripting (XSS):**

XSS memungkinkan penyerang menyisipkan skrip berbahaya ke dalam halaman yang dilihat pengguna lain.

**Pencegahan di Laravel:**
- Mesin templat Blade secara otomatis meng-*escape* keluaran dengan `{{ }}`
- Gunakan `{!! !!}` hanya untuk konten terpercaya
- Validasi dan sanitasi masukan pengguna

**3. Cross-Site Request Forgery (CSRF):**

CSRF menipu pengguna untuk melakukan tindakan yang tidak diinginkan pada aplikasi tempat mereka terautentikasi.

**Pencegahan di Laravel:**
- Laravel secara otomatis menghasilkan *token* CSRF untuk setiap sesi pengguna aktif
- Semua permintaan POST, PUT, PATCH, DELETE harus menyertakan *token* CSRF
- Direktif Blade `@csrf` untuk menyertakan *token* dalam formulir

**4. Session Hijacking:**

Penyerang mencuri atau memprediksi ID sesi yang valid untuk mendapatkan akses tidak sah.

**Pencegahan:**
- Gunakan HTTPS untuk mengenkripsi transmisi data
- Atur *flag* aman dan *httpOnly* untuk *cookie* sesi
- Regenerasi ID sesi setelah *login* (Laravel melakukan ini secara otomatis)
- Terapkan batas waktu sesi (*session timeout*)

**5. Insecure Direct Object References (IDOR):**

Penyerang dapat mengakses sumber daya dengan memodifikasi nilai parameter (misalnya, mengubah *user_id* dalam URL).

**Pencegahan:**
- Terapkan pemeriksaan otorisasi yang tepat
- Gunakan *Policies* Laravel untuk memastikan pengguna hanya dapat mengakses sumber daya mereka sendiri
- Jangan ekspos ID internal secara langsung; gunakan UUID atau *slug*

**6. Kelemahan Kata Sandi:**

Kata sandi yang lemah atau disimpan dengan tidak tepat dapat dikompromikan dengan mudah.

**Pencegahan di Laravel:**
- Gunakan *hashing* kata sandi bawaan Laravel (Bcrypt/Argon2)
- Terapkan kebijakan kata sandi yang kuat (panjang minimum, persyaratan kompleksitas)
- Jangan pernah menyimpan kata sandi dalam teks biasa
- Terapkan konfirmasi kata sandi untuk tindakan sensitif

---

**[GAMBAR 2.9 - Web Security Layers (OWASP Top 10)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT OWASP TOP 10 SECURITY THREATS INFOGRAPHIC]       │
│                                                             │
│   OWASP Top 10 Web Application Security Risks (2021):      │
│                                                             │
│   1️⃣  BROKEN ACCESS CONTROL                                │
│       • Bypass authorization checks                         │
│       • Access unauthorized data/functions                  │
│       Laravel Protection: Middleware, Policies, Gates       │
│                                                             │
│   2️⃣  CRYPTOGRAPHIC FAILURES                               │
│       • Sensitive data exposure                             │
│       • Weak encryption algorithms                          │
│       Laravel Protection: Bcrypt hashing, Encryption facade │
│                                                             │
│   3️⃣  INJECTION (SQL, XSS, Command)                        │
│       • Malicious code in queries/commands                  │
│       • Data theft or destruction                           │
│       Laravel Protection: Eloquent ORM, Parameter binding   │
│                                                             │
│   4️⃣  INSECURE DESIGN                                      │
│       • Missing security controls by design                 │
│       • Architecture flaws                                  │
│       CUR-HEART: Security requirements from start           │
│                                                             │
│   5️⃣  SECURITY MISCONFIGURATION                            │
│       • Default credentials, unnecessary features           │
│       • Verbose error messages                              │
│       Laravel Protection: .env config, Debug mode control   │
│                                                             │
│   6️⃣  VULNERABLE & OUTDATED COMPONENTS                     │
│       • Using libraries with known vulnerabilities          │
│       Laravel Protection: Composer audit, Regular updates   │
│                                                             │
│   7️⃣  IDENTIFICATION & AUTHENTICATION FAILURES             │
│       • Weak password policies                              │
│       • Session management flaws                            │
│       Laravel Protection: Breeze, Sanctum, Session handling │
│                                                             │
│   8️⃣  SOFTWARE & DATA INTEGRITY FAILURES                   │
│       • Unsigned/unverified updates                         │
│       • CI/CD pipeline vulnerabilities                      │
│       Protection: Code reviews, Version control             │
│                                                             │
│   9️⃣  SECURITY LOGGING & MONITORING FAILURES               │
│       • Insufficient logging                                │
│       • No breach detection                                 │
│       Laravel Protection: Log facade, Monitoring tools      │
│                                                             │
│   🔟 SERVER-SIDE REQUEST FORGERY (SSRF)                    │
│       • Fetch remote resources without validation           │
│       Laravel Protection: Input validation, URL whitelist   │
│                                                             │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│                                                             │
│   SECURITY LAYERS IMPLEMENTED IN CUR-HEART:                │
│                                                             │
│   🛡️  Layer 1: NETWORK (HTTPS, Firewall)                   │
│   🛡️  Layer 2: APPLICATION (Laravel Security Features)     │
│   🛡️  Layer 3: DATABASE (Encrypted data, Backups)          │
│   🛡️  Layer 4: AUTHENTICATION (Multi-factor capable)       │
│   🛡️  Layer 5: AUTHORIZATION (RBAC with Policies)          │
│   🛡️  Layer 6: MONITORING (Logs, Alerts, Audits)           │
│                                                             │
│   Format: Infographic dengan icon per threat + mitigation  │
│   Recommended size: 1200x1600px (vertical layout)          │
│   Style: Professional security diagram dengan color-coding │
│         Red (threats) → Green (protections)                │
│                                                             │
│   File: assets/images/owasp-top-10-security.png            │
│   Reference: OWASP Foundation (2021)                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.9: OWASP Top 10 web application security risks yang menjadi acuan implementasi keamanan sistem CUR-HEART dengan mitigation strategies menggunakan Laravel built-in security features_

---

### 2.1.9 Antarmuka Pengguna dan Pengalaman Pengguna (*User Interface* dan *User Experience*/UI/UX)

#### 2.1.9.1 Pengertian UI/UX

**Antarmuka Pengguna (*User Interface*/UI)** adalah segala sesuatu yang pengguna berinteraksi dengannya ketika menggunakan produk digital (Norman, 2013). UI mencakup layar, halaman, tombol, ikon, dan semua elemen visual lainnya yang memungkinkan pengguna untuk berinteraksi dengan produk.

**Pengalaman Pengguna (*User Experience*/UX)** adalah pengalaman keseluruhan pengguna saat berinteraksi dengan produk, termasuk kemudahan penggunaan, efisiensi, kepuasan, dan respons emosional (Hassenzahl & Tractinsky, 2006). UX lebih luas dari UI dan mencakup seluruh perjalanan pengguna dari kesadaran hingga dukungan pasca-pembelian.

Menurut Nielsen Norman Group (2021), UX yang baik adalah tentang memahami kebutuhan, nilai, kemampuan, dan keterbatasan pengguna. UX yang baik juga berarti memahami tujuan bisnis dan menyeimbangkannya dengan kebutuhan pengguna.

#### 2.1.9.2 Prinsip-prinsip Desain UI/UX

**1. Desain Berpusat pada Pengguna (*User-Centered Design*):**
Keputusan desain berdasarkan riset pengguna dan umpan balik, bukan asumsi (Norman, 2013).

**2. Konsistensi (*Consistency*):**
Elemen antarmuka harus konsisten dalam penampilan dan perilaku di seluruh aplikasi (Shneiderman et al., 2016).

**3. Umpan Balik (*Feedback*):**
Sistem harus memberikan umpan balik yang jelas untuk setiap tindakan pengguna (klik tombol, pengiriman formulir, dll.).

**4. Kesederhanaan (*Simplicity*):**
Pertahankan antarmuka sederhana dan langsung. Hapus elemen yang tidak perlu yang tidak berkontribusi pada tujuan pengguna.

**5. Hierarki (*Hierarchy*):**
Organisir konten dengan hierarki visual yang jelas untuk memandu perhatian pengguna ke elemen yang paling penting.

**6. Aksesibilitas (*Accessibility*):**
Desain untuk semua pengguna, termasuk mereka dengan disabilitas (pedoman WCAG).

**7. Pencegahan & Pemulihan Kesalahan (*Error Prevention & Recovery*):**
Cegah kesalahan jika memungkinkan; ketika kesalahan terjadi, berikan pesan yang jelas dan opsi pemulihan yang mudah.

**8. Desain Responsif (*Responsive Design*):**
Antarmuka harus bekerja dengan baik di berbagai perangkat dan ukuran layar (seluler, tablet, desktop).

---

**[GAMBAR 2.10 - UI/UX Design Process]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT UI/UX DESIGN PROCESS FLOWCHART]                  │
│                                                             │
│   5 Phases (horizontal flow):                              │
│                                                             │
│   1. RESEARCH        2. DEFINE        3. IDEATE           │
│   - User research    - Personas       - Wireframes        │
│   - Competitor       - User stories   - Sketches          │
│   - Interviews       - Requirements   - Brainstorming     │
│         ↓                  ↓                ↓              │
│                                                             │
│   4. PROTOTYPE       5. TEST & ITERATE                     │
│   - Mockups          - Usability testing                   │
│   - Hi-fi designs    - Feedback collection                 │
│   - Interactions     - Refinement                          │
│         ↓                  ↓                                │
│                    ← Loop back if needed                   │
│                                                             │
│   Format: Process flowchart dengan icon per phase          │
│   Recommended size: 1400x800px                             │
│                                                             │
│   File: assets/images/uiux-design-process.png              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.10: Proses desain UI/UX yang digunakan dalam perancangan antarmuka sistem CUR-HEART dari research hingga testing_

---

#### 2.1.9.3 Desain Web Responsif (*Responsive Web Design*)

Desain Web Responsif (*Responsive Web Design*/RWD) adalah pendekatan untuk desain web yang membuat halaman ditampilkan dengan baik pada berbagai perangkat dan ukuran layar (Marcotte, 2011).

**Teknik RWD:**

1. **Kisi Fluida (*Fluid Grids*):**
   Tata letak menggunakan unit relatif (%, em, rem) alih-alih unit tetap (px).

2. **Gambar Fleksibel (*Flexible Images*):**
   Gambar diskalakan berdasarkan elemen penampung dengan `max-width: 100%`.

3. **Kueri Media (*Media Queries*):**
   Aturan CSS yang diterapkan berdasarkan karakteristik perangkat (lebar layar, orientasi):
   ```css
   @media (min-width: 768px) {
       /* Gaya untuk tablet dan desktop */
   }
   ```

4. **Pendekatan Seluler-Pertama (*Mobile-First Approach*):**
   Desain untuk layar terkecil terlebih dahulu, kemudian tingkatkan untuk layar yang lebih besar.

**Desain Responsif Tailwind CSS:**

Tailwind mempermudah desain responsif dengan awalan *breakpoint*:
```html
<div class="text-sm md:text-base lg:text-lg">
    <!-- Ukuran font berubah berdasarkan ukuran layar -->
</div>
```

Dalam sistem CUR-HEART, desain responsif sangat penting karena banyak pengguna akan mengakses dari perangkat seluler, terutama untuk pemesanan dan memeriksa janji temu saat bepergian.

## 2.2 Penelitian Terkait

Beberapa penelitian terkait yang relevan dengan pengembangan sistem informasi manajemen booking dan terapi telah dilakukan sebelumnya. Penelitian-penelitian ini menjadi referensi dan landasan untuk identifikasi gap serta differentiation dari proyek CUR-HEART.

### 2.2.1 Penelitian tentang Sistem Informasi Kesehatan

**Penelitian 1:**

**Judul:** "Rancang Bangun Sistem Informasi Manajemen Rumah Sakit Berbasis Web dengan Metode Air Terjun"

**Penulis:** Pratama, A. W., & Kusumawati, R. D. (2022)

**Jurnal:** Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK), Vol. 9, No. 3

**Abstrak:**
Penelitian ini mengembangkan sistem informasi manajemen rumah sakit berbasis web yang mencakup pendaftaran pasien, rekam medis elektronik, penjadwalan dokter, dan penagihan. Metode pengembangan menggunakan air terjun (*waterfall*) dengan tahapan analisis, desain, implementasi, dan pengujian. Hasil penelitian menunjukkan bahwa sistem dapat meningkatkan efisiensi administrasi hingga 45% dan mengurangi waktu tunggu pasien hingga 30%.

**Relevansi:**
Penelitian ini relevan karena menggunakan metodologi air terjun yang sama dan mengembangkan sistem pemesanan/penjadwalan di sektor kesehatan. Namun, fokus pada rumah sakit umum, bukan spesifik layanan terapi kesehatan mental.

**Gap yang Diidentifikasi:**
- Tidak ada fitur khusus untuk dokumentasi sesi terapi dan pelacakan kemajuan
- Tidak ada sistem untuk mengelola ketersediaan terapis dengan penjadwalan fleksibel
- UI/UX tidak dioptimasi untuk pengguna dengan kondisi mental yang rapuh

**Penelitian 2:**

**Judul:** "Development of Online Mental Health Consultation Platform Using Laravel Framework"

**Penulis:** Chen, X., Li, Y., & Wang, Z. (2021)

**Jurnal:** International Journal of Environmental Research and Public Health, Vol. 18, Issue 15

**Abstrak:**
Penelitian ini mengembangkan platform konsultasi kesehatan mental daring yang menghubungkan pasien dengan psikolog melalui panggilan video dan obrolan. Platform dibangun menggunakan kerangka kerja Laravel dengan fitur penjadwalan janji temu, konferensi video aman, dan catatan pasien dasar. Pengujian pengguna menunjukkan tingkat kepuasan 85% dan pengurangan 70% dalam janji temu yang tidak dihadiri berkat sistem pengingat.

**Relevansi:**
Penelitian ini sangat relevan karena domain yang sama (kesehatan mental) dan teknologi yang sama (Laravel). Menjadi tolok ukur untuk fitur penjadwalan janji temu dan fitur komunikasi.

**Gap yang Diidentifikasi:**
- Tidak ada fokus hipnoterapi sebagai metode perawatan yang memiliki persyaratan unik
- Belum ada sistem komprehensif untuk pemantauan kinerja terapis dan pelacakan pendapatan
- Sistem pembayaran masih manual, belum terintegrasi dengan *payment gateway*

### 2.2.2 Penelitian tentang Sistem Booking dan Penjadwalan

**Penelitian 3:**

**Judul:** "Sistem Informasi Pemesanan Salon Kecantikan Berbasis Web dengan Fitur Penjadwalan Waktu Nyata"

**Penulis:** Wijaya, S., & Lestari, P. (2023)

**Jurnal:** Jurnal Sistem Informasi Bisnis, Vol. 13, No. 1

**Abstrak:**
Penelitian ini mengembangkan sistem pemesanan daring untuk salon kecantikan yang memungkinkan pelanggan untuk memilih layanan, penata gaya, dan slot waktu secara waktu nyata. Sistem menggunakan PHP dengan basis data MySQL dan menerapkan algoritma untuk optimasi penjadwalan penata gaya berdasarkan ketersediaan dan riwayat pemesanan. Hasil implementasi menunjukkan peningkatan 60% dalam tingkat konversi pemesanan dan pengurangan 40% dalam konflik penjadwalan.

**Relevansi:**
Penelitian ini relevan untuk aspek alur pemesanan dan algoritma penjadwalan. Pemesanan berbasis layanan dengan pemilihan penyedia layanan (penata gaya/terapis) memiliki kemiripan dengan sistem CUR-HEART.

**Gap yang Diidentifikasi:**
- Tidak ada pertimbangan untuk sifat sensitif dari layanan kesehatan mental
- Dokumentasi dan pencatatan untuk sesi tidak dibahas
- Pelacakan kemajuan klien tidak ada karena sifat layanan salon yang transaksional

**Penelitian 4:**

**Judul:** "Aplikasi Manajemen Pemesanan dan Penjadwalan Klinik Kesehatan Menggunakan Kerangka Kerja Laravel"

**Penulis:** Hartono, B., Santoso, D., & Wijayanti, E. (2022)

**Jurnal:** Jurnal Informatika dan Komputer, Vol. 27, No. 2

**Abstrak:**
Penelitian mengembangkan aplikasi manajemen pemesanan untuk klinik kesehatan dengan fitur pemesanan daring, manajemen antrian, rekam medis, dan pelaporan. Kerangka kerja Laravel digunakan dengan basis data MySQL dan Tailwind CSS untuk antarmuka. Pengujian sistem menunjukkan kepatuhan 90% terhadap persyaratan fungsional dan skor kepuasan pengguna 82%.

**Relevansi:**
Penelitian ini sangat relevan dengan tumpukan teknologi yang identik (Laravel, MySQL, Tailwind). Dapat menjadi referensi untuk detail implementasi dan praktik terbaik.

**Gap yang Diidentifikasi:**
- Fokus pada klinik kesehatan umum, bukan layanan terapi khusus
- Alur pemesanan multi-langkah tidak diimplementasikan (pemesanan satu langkah yang lebih sederhana)
- Fitur khusus terapis seperti templat catatan sesi dan dasbor pendapatan tidak ada

### 2.2.3 Penelitian tentang Laravel dan Web Development

**Penelitian 5:**

**Judul:** "Analisis Perbandingan Performa Kerangka Kerja PHP (Laravel, CodeIgniter, Symfony) untuk Pengembangan Aplikasi Web"

**Penulis:** Nugroho, A. P., & Setiawan, F. (2021)

**Jurnal:** Jurnal Teknik Informatika, Vol. 14, No. 3

**Abstrak:**
Penelitian ini melakukan analisis komparatif terhadap tiga kerangka kerja PHP populer (Laravel, CodeIgniter, Symfony) dalam hal kinerja, kemudahan pengembangan, dan skalabilitas. *Benchmarking* dilakukan menggunakan kasus uji yang identik. Hasil menunjukkan Laravel memberikan keseimbangan terbaik antara produktivitas pengembang dan kinerja aplikasi, dengan waktu eksekusi hanya 15% lebih lambat dari CodeIgniter tetapi dengan pemeliharaan kode dan ekosistem yang jauh lebih baik.

**Relevansi:**
Penelitian ini membenarkan pemilihan Laravel sebagai kerangka kerja untuk proyek ini, memberikan alasan berbasis bukti.

**Gap yang Diidentifikasi:**
- Tidak ada analisis spesifik untuk persyaratan aplikasi kesehatan
- Pertimbangan keamanan untuk penanganan data sensitif tidak dieksplorasi secara mendalam

### 2.2.4 Penelitian tentang UI/UX untuk Healthcare

**Penelitian 6:**

**Judul:** "Desain Pengalaman Pengguna untuk Aplikasi Kesehatan Mental: Studi Kasus pada Generasi Milenial"

**Penulis:** Rahayu, D., Kusuma, W., & Pratiwi, A. (2023)

**Jurnal:** Jurnal Desain Interaksi, Vol. 8, No. 1

**Abstrak:**
Penelitian ini menginvestigasi preferensi desain pengalaman pengguna untuk aplikasi kesehatan mental di antara pengguna milenial di Indonesia. Melalui riset pengguna, pembuatan kerangka kawat, purwarupa, dan pengujian kegunaan dengan 50 partisipan, penelitian menemukan bahwa faktor kunci untuk pengalaman pengguna yang baik adalah kesederhanaan, jaminan privasi, desain visual yang menenangkan, dan navigasi yang mudah. Pengguna lebih menyukai palet warna lembut (biru, hijau) dan beban kognitif minimal dalam antarmuka.

**Relevansi:**
Penelitian ini sangat relevan untuk menginformasikan keputusan desain dalam sistem CUR-HEART, terutama untuk menargetkan pengguna milenial dan Gen Z.

**Gap yang Diidentifikasi:**
- Fokus pada aplikasi kesehatan mental umum, tidak spesifik pada sistem manajemen pemesanan dan terapi
- Detail implementasi dan kendala teknis tidak dibahas

### 2.2.5 Gap Analysis dan Posisi Penelitian

---

**Tabel 2.5 Summary of Related Research (Penelitian Terkait)**

| No | Penulis & Tahun | Judul Penelitian | Metodologi | Teknologi | Fitur Utama | Hasil/Temuan | Gap yang Teridentifikasi | Relevansi CUR-HEART |
|----|----------------|-----------------|------------|-----------|-------------|-------------|-------------------------|-------------------|
| 1 | Pratama & Kusumawati (2022) | Rancang Bangun Sistem Informasi Manajemen Rumah Sakit Berbasis Web dengan Metode Air Terjun | SDLC Air Terjun | PHP, MySQL, Bootstrap | • Pendaftaran pasien<br>• Rekam medis elektronik<br>• Penjadwalan dokter<br>• Sistem penagihan | • Efisiensi admin +45%<br>• Waktu tunggu -30%<br>• Implementasi sukses di RS kecil | ❌ Tidak ada fitur pelacakan kemajuan terapi<br>❌ Penjadwalan tidak fleksibel untuk terapis<br>❌ UI/UX tidak dioptimasi untuk kesehatan mental | ⚠️ SEDANG<br>**Dapat Diadopsi**: Metodologi air terjun, konsep alur pemesanan<br>**Berbeda**: Rumah sakit umum vs terapi khusus |
| 2 | Chen, Li, & Wang (2021) | Development of Online Mental Health Consultation Platform Using Laravel Framework | *Agile* | Laravel, MySQL, WebRTC | • Konsultasi daring<br>• Penjadwalan janji temu<br>• Konferensi video<br>• Catatan pasien | • Kepuasan pengguna 85%<br>• Pengurangan ketidakhadiran 70%<br>• Sistem pengingat efektif | ❌ Tidak fokus hipnoterapi spesifik<br>❌ Pemantauan kinerja terbatas<br>❌ Verifikasi pembayaran manual | ⭐ TINGGI<br>**Dapat Diadopsi**: Arsitektur Laravel, domain kesehatan mental, sistem pengingat<br>**Ditingkatkan**: Otomasi pembayaran, analitik terapis |
| 3 | Wijaya & Lestari (2023) | Sistem Informasi Pemesanan Salon Kecantikan Berbasis Web dengan Fitur Penjadwalan Waktu Nyata | Purwarupa | PHP natif, MySQL, Bootstrap | • Pemesanan waktu nyata<br>• Pemilihan penyedia layanan<br>• Algoritma penjadwalan<br>• Pencegahan konflik | • Konversi pemesanan +60%<br>• Konflik penjadwalan -40%<br>• Optimasi algoritma sukses | ❌ Tidak ada dokumentasi sesi<br>❌ Tidak ada pelacakan kemajuan klien<br>❌ Layanan transaksional (bukan terapi) | ⚠️ SEDANG<br>**Dapat Diadopsi**: Alur pemesanan, ketersediaan waktu nyata, algoritma konflik<br>**Berbeda**: Layanan salon vs sesi terapi |
| 4 | Hartono, Santoso, & Wijayanti (2022) | Aplikasi Manajemen Pemesanan dan Penjadwalan Klinik Kesehatan Menggunakan Kerangka Kerja Laravel | Air Terjun | Laravel 9, MySQL, Tailwind CSS | • Pemesanan daring<br>• Manajemen antrian<br>• Rekam medis<br>• Dasbor pelaporan | • Persyaratan fungsional 90%<br>• Kepuasan pengguna 82%<br>• Sistem stabil di produksi | ❌ Klinik umum, bukan terapi khusus<br>❌ Alur pemesanan 1 langkah sederhana<br>❌ Fitur terapis minimal | ⭐⭐ SANGAT TINGGI<br>**Dapat Diadopsi**: Tumpukan teknologi sama persis (Laravel+MySQL+Tailwind), sistem pemesanan, pelaporan<br>**Ditingkatkan**: Pemesanan multi-langkah, dasbor terapis |
| 5 | Nugroho & Setiawan (2021) | Analisis Perbandingan Performa Kerangka Kerja PHP (Laravel, CodeIgniter, Symfony) untuk Pengembangan Aplikasi Web | Studi Komparatif | Laravel 8, CodeIgniter 4, Symfony 5 | • *Benchmarking* kinerja<br>• Analisis pemeliharaan kode<br>• Pengujian skalabilitas | • Laravel: keseimbangan terbaik produktivitas & kinerja<br>• 15% lebih lambat dari CodeIgniter<br>• Ekosistem jauh lebih baik | ❌ Tidak ada analisis spesifik untuk aplikasi kesehatan<br>❌ Keamanan untuk data sensitif tidak mendalam | ⚠️ SEDANG<br>**Dapat Diadopsi**: Bukti pemilihan Laravel, ekspektasi kinerja<br>**Nilai**: Justifikasi kerangka kerja |
| 6 | Rahayu, Kusuma, & Pratiwi (2023) | Desain Pengalaman Pengguna untuk Aplikasi Kesehatan Mental: Studi Kasus pada Generasi Milenial | Riset Pengguna, Pengujian Kegunaan | Figma (desain saja) | • Riset pengguna (n=50)<br>• Pembuatan kerangka kawat<br>• Pengujian purwarupa<br>• Pedoman pengalaman pengguna | • Preferensi: kesederhanaan, privasi, warna menenangkan<br>• Palet lembut (biru, hijau) efektif<br>• Beban kognitif minimal penting | ❌ Aplikasi kesehatan mental umum<br>❌ Tidak spesifik untuk sistem pemesanan<br>❌ Tidak ada detail implementasi | ⭐ TINGGI<br>**Dapat Diadopsi**: Prinsip pengalaman pengguna, psikologi warna, preferensi milenial<br>**Diterapkan**: Desain menenangkan untuk CUR-HEART |

**Gap Analysis Summary:**

| Kategori Gap | Deskripsi | Bagaimana CUR-HEART Mengatasinya | Tingkat Inovasi |
|--------------|-------------|----------------------------------|-----------------|
| **1. Persyaratan Spesifik Domain** | Penelitian yang ada fokus pada kesehatan umum/kesehatan mental, tidak spesifik hipnoterapi dengan kebutuhan dokumentasi unik | • Templat sesi spesifik hipnoterapi<br>• Dokumentasi keadaan *trance*<br>• Metrik kemajuan khusus (skala kecemasan)<br>• Pelacakan teknik (relaksasi progresif, visualisasi) | 🔥 TINGGI - Sistem manajemen hipnoterapi pertama |
| **2. Manajemen Terapis Komprehensif** | Sistem yang ada fokus pada sisi pasien, fitur terapis terbatas | • Dasbor pendapatan dengan rincian<br>• Analitik kinerja (jumlah sesi, rating, utilisasi)<br>• Manajemen ketersediaan fleksibel (berulang + pengecualian)<br>• Wawasan klien dan visibilitas kemajuan | 🔥 TINGGI - Fitur berpusat terapis langka |
| **3. Alur Pemesanan Multi-Langkah** | Sistem yang ada menggunakan pemesanan sederhana 1-2 langkah | • Panduan 4 langkah (Layanan → Terapis → Jadwal → Pembayaran)<br>• Indikasi kemajuan yang jelas<br>• Pengungkapan informasi progresif<br>• Beban kognitif optimal per langkah | 🟡 SEDANG - Meningkatkan pengalaman pengguna |
| **4. Pelacakan Kemajuan & Analitik** | Pelacakan kemajuan klien komprehensif dengan visualisasi jarang | • Integrasi alat penilaian mandiri<br>• Grafik kemajuan (frekuensi sesi, tingkat kecemasan)<br>• Penetapan tujuan dan pelacakan pencapaian<br>• Garis waktu catatan terapis | 🔥 TINGGI - Tampilan perjalanan terapi holistik |
| **5. Sistem Pembayaran Terintegrasi** | Banyak sistem masih verifikasi pembayaran manual | • Integrasi *payment gateway* Midtrans<br>• Berbagai metode pembayaran (VA, *e-wallet*, QRIS)<br>• Verifikasi otomatis<br>• Riwayat pembayaran & kuitansi | 🟡 SEDANG - Standar industri sekarang |
| **6. Fokus Keamanan & Privasi** | Keamanan dasar, tidak komprehensif untuk data kesehatan mental sensitif | • Kontrol akses berbasis peran (3 peran, 15 izin)<br>• Enkripsi data (kata sandi bcrypt, bidang sensitif AES-256)<br>• Jejak audit (siapa mengakses apa kapan)<br>• Kontrol privasi terinspirasi GDPR | 🔥 TINGGI - Keamanan tingkat kesehatan |
| **7. Desain Responsif & Dapat Diakses** | Fokus *desktop*, optimasi seluler terbatas | • Desain seluler-pertama (70% pengguna seluler)<br>• Titik putus responsif Tailwind (6 titik putus)<br>• Palet warna menenangkan (Biru Laut, Pink, Teal)<br>• Pertimbangan aksesibilitas (WCAG 2.1) | 🟡 SEDANG - Praktik terbaik modern |

**Posisi Penelitian:**

Penelitian dan pengembangan sistem informasi CUR-HEART ini memposisikan diri sebagai **solusi komprehensif, spesifik domain, dan berpusat pada pengguna** untuk manajemen layanan hipnoterapi dan kesehatan mental. Sistem ini mengintegrasikan praktik terbaik dari penelitian yang ada dengan fitur inovatif yang secara khusus mengatasi kebutuhan praktik hipnoterapi, menghasilkan solusi yang tidak hanya kokoh secara teknis tetapi juga selaras secara mendalam dengan persyaratan klinis dan bisnis CUR-HEART.

Dengan mengatasi kesenjangan yang teridentifikasi dan membangun di atas pengetahuan dari penelitian yang ada, sistem CUR-HEART diharapkan dapat menjadi **model referensi** untuk pengembangan sistem informasi serupa di sektor layanan kesehatan mental di Indonesia, serta **berkontribusi** pada kumpulan pengetahuan dalam domain sistem informasi kesehatan dan interaksi manusia-komputer untuk layanan kesehatan mental.

---

**[GAMBAR 2.11 - Timeline Penelitian Terkait (2020-2024)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT RESEARCH TIMELINE GRAPHIC]                       │
│                                                             │
│   Timeline (horizontal):                                   │
│                                                             │
│   2020        2021        2022        2023        2024     │
│   ─────────────────────────────────────────────────────    │
│     │           │           │           │           │      │
│     │           │           │           │           │      │
│   [Gap]     [Chen et    [Pratama    [Hartono    ★ CUR-    │
│             al. 2021]   Wijaya      Rahayu      HEART     │
│                         2022]       2023]       2024      │
│                                                             │
│   Key Milestones:                                          │
│   2021: Online Mental Health Platform (Laravel+WebRTC)     │
│   2022: Hospital Management (Waterfall+Web)                │
│   2022: Clinic Booking (Laravel+Tailwind) ← Most similar   │
│   2023: Salon Booking (Real-time scheduling)               │
│   2023: UX Design for Mental Health (Research)             │
│   2024: ★ CUR-HEART Hypnotherapy Management System         │
│                                                             │
│   Evolution of Features:                                   │
│   2020-2021: Basic booking + consultation                  │
│   2022: + Queue management, Laravel adoption               │
│   2023: + Real-time scheduling, UX focus                   │
│   2024: + Progress tracking, therapist analytics,          │
│          specialized hypnotherapy features                 │
│                                                             │
│   Gap Analysis:                                            │
│   Previous: General healthcare/mental health apps          │
│   CUR-HEART: Specialized hypnotherapy management           │
│              + Therapist-centric features                  │
│              + Comprehensive progress tracking             │
│              + Healthcare-grade security                   │
│                                                             │
│   Format: Timeline dengan milestone markers                │
│   Recommended size: 1400x600px (landscape)                 │
│   Style: Modern timeline infographic                       │
│                                                             │
│   File: assets/images/penelitian-terkait-timeline.png      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 2.11: Timeline penelitian-penelitian terkait (2020-2024) yang menunjukkan evolusi sistem informasi kesehatan dan posisi proyek CUR-HEART dalam mengisi gap domain-specific hypnotherapy management_

---
