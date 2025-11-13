# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN
## Bagian 3B: Desain Antarmuka Pengguna (UI/UX *Design*)

---

### 4.3.5 Desain Antarmuka Pengguna (*User Interface Design*)

Desain antarmuka pengguna (*User Interface*/UI) dan pengalaman pengguna (*User Experience*/UX) merupakan aspek krusial dalam pengembangan sistem informasi CUR-HEART. Antarmuka yang baik tidak hanya menarik secara visual, tetapi juga harus intuitif, mudah digunakan, dan memberikan pengalaman yang menyenangkan bagi pengguna. Dalam pengembangan sistem CUR-HEART, proses desain UI/UX dilakukan dengan pendekatan *user-centered design* yang mempertimbangkan kebutuhan dan karakteristik dari tiga tipe pengguna utama: klien, terapis, dan administrator.

Proses desain UI/UX CUR-HEART dimulai dengan penelitian pengguna (*user research*) untuk memahami kebutuhan, preferensi, dan titik kesulitan (*pain points*) dari setiap tipe pengguna. Hasil penelitian ini kemudian diterjemahkan ke dalam *wireframe*, *mockup*, dan *prototype* yang dapat diuji dan divalidasi sebelum masuk ke tahap implementasi. Pendekatan iteratif ini memastikan bahwa desain akhir benar-benar memenuhi kebutuhan pengguna dan memberikan pengalaman yang optimal.

#### 4.3.5.1 Sistem Desain (*Design System*) CUR-HEART

Sistem desain (*design system*) adalah kumpulan komponen, panduan desain, dan standar yang digunakan secara konsisten di seluruh aplikasi untuk menciptakan pengalaman pengguna yang kohesif dan profesional. Sistem desain CUR-HEART dikembangkan dengan tujuan untuk:

1. **Konsistensi Visual**: Memastikan tampilan yang seragam di seluruh halaman dan fitur
2. **Efisiensi Pengembangan**: Mempercepat proses *development* dengan komponen yang dapat digunakan kembali (*reusable*)
3. **Identitas Merek (*Brand Identity*)**: Memperkuat identitas merek CUR-HEART sebagai layanan kesehatan mental profesional
4. **Skalabilitas (*Scalability*)**: Memudahkan penambahan fitur baru dengan panduan desain yang jelas
5. **Aksesibilitas (*Accessibility*)**: Memastikan aplikasi dapat diakses oleh pengguna dengan berbagai kemampuan

Sistem desain CUR-HEART terdiri dari beberapa elemen utama yang akan dijelaskan pada sub-bagian berikutnya.

#### 4.3.5.2 Palet Warna & Tipografi (*Color Palette & Typography*)

**[GAMBAR 4.15 - Sistem Desain: Palet Warna]** 🔴 **KRITIS**

**A. Palet Warna (*Color Palette*)**

Pemilihan warna dalam CUR-HEART dirancang untuk mencerminkan nilai-nilai profesionalisme, kepercayaan, dan kesehatan mental. Berikut adalah palet warna yang digunakan:

**Warna Primer (*Primary Colors*)**:
- **Biru Tua/*Navy Blue* (#1E0E62)**: Warna dominan yang melambangkan profesionalisme, kepercayaan, dan stabilitas. Digunakan untuk *header*, navigasi, dan elemen penting.
- **Merah Muda/*Pink* (#FF6B7A)**: Warna aksen yang melambangkan empati, kehangatan, dan perawatan. Digunakan untuk tombol ajakan bertindak (*call-to-action*) dan sorotan (*highlights*).

**Warna Pendukung (*Secondary Colors*)**:
- **Ungu Muda/*Light Purple* (#EEEAF9)**: Latar belakang untuk bagian dan kartu, memberikan nuansa tenang
- **Merah Muda Lembut/*Soft Pink* (#FFE5E8)**: Sorotan untuk area tertentu, melengkapi merah muda primer
- **Putih (#FFFFFF)**: Latar belakang utama, menciptakan ruang bernafas (*breathing room*)
- **Skala Abu-Abu**: 
  - Abu-abu Gelap (#333333) untuk teks isi
  - Abu-abu Sedang (#666666) untuk teks sekunder
  - Abu-abu Terang (#F5F5F5) untuk batas dan pembagi

**Warna Fungsional (*Semantic Colors*)**:
- **Hijau Sukses (*Success Green*) (#10B981)**: Notifikasi sukses, status disetujui
- **Oranye Peringatan (*Warning Orange*) (#F59E0B)**: Peringatan, tindakan tertunda
- **Merah Bahaya (*Danger Red*) (#EF4444)**: Pesan kesalahan, tindakan hapus
- **Biru Informasi (*Info Blue*) (#3B82F6)**: Pesan informasional

Palet warna ini dipilih berdasarkan prinsip-prinsip psikologi warna dalam konteks kesehatan mental, di mana warna-warna yang menenangkan dan profesional sangat penting untuk menciptakan rasa aman dan percaya bagi klien.

**[GAMBAR 4.16 - Sistem Desain: Sistem Tipografi]** 🔴 **KRITIS**

**B. Tipografi (*Typography*)**

Tipografi yang dipilih untuk CUR-HEART mengutamakan keterbacaan (*readability*) dan kejelasan (*legibility*):

**Keluarga Huruf (*Font Families*)**:
1. **Poppins** (*Sans-serif*) - Untuk Judul
   - Huruf modern dan ramah yang mudah dibaca
   - Digunakan untuk: H1, H2, H3, H4, H5, H6, dan menu navigasi
   - Bobot huruf: Reguler (400), Medium (500), SemiBold (600), Tebal (700)

2. **Inter** (*Sans-serif*) - Untuk Teks Isi
   - Huruf yang sangat mudah dibaca bahkan dalam ukuran kecil
   - Digunakan untuk: paragraf, deskripsi, label formulir, konten tabel
   - Bobot huruf: Reguler (400), Medium (500), SemiBold (600)

**Skala Tipe (*Type Scale*)**:
- **H1 (Judul 1)**: 36px / 2.25rem - Judul halaman
- **H2 (Judul 2)**: 30px / 1.875rem - Judul bagian
- **H3 (Judul 3)**: 24px / 1.5rem - Judul subbagian
- **H4 (Judul 4)**: 20px / 1.25rem - Judul kartu
- **H5 (Judul 5)**: 18px / 1.125rem - Judul kecil
- **Isi Besar**: 16px / 1rem - Teks isi penting
- **Isi Reguler**: 14px / 0.875rem - Teks isi standar
- **Isi Kecil**: 12px / 0.75rem - Keterangan, teks pembantu

**Tinggi Baris & Spasi (*Line Height & Spacing*)**:
- Judul: 1,2x ukuran huruf (ketat untuk penekanan)
- Teks isi: 1,5x ukuran huruf (nyaman untuk dibaca)
- Spasi paragraf: margin bawah 1em

Pemilihan kombinasi Poppins dan Inter memberikan keseimbangan antara karakter yang ramah (untuk judul) dan profesional (untuk teks isi), sesuai dengan positioning CUR-HEART sebagai layanan hipnoterapi yang modern dan terpercaya.

#### 4.3.5.3 Pustaka Komponen (*Component Library*)

**[GAMBAR 4.17 - Sistem Desain: Pustaka Komponen]** 🔴 **KRITIS**

Pustaka komponen (*component library*) adalah kumpulan komponen UI yang dapat digunakan kembali (*reusable*) di berbagai halaman aplikasi. Berikut adalah komponen-komponen utama dalam sistem desain CUR-HEART:

**A. Tombol (*Buttons*)**

1. **Tombol Primer (*Primary Button*)**: 
   - Latar belakang: Merah Muda (#FF6B7A)
   - Teks: Putih
   - Penggunaan: Ajakan bertindak utama (*call-to-action*) (Pesan Sekarang, Kirim, Konfirmasi)
   - Status: *Default*, *Hover* (merah muda lebih gelap), Aktif, Nonaktif

2. **Tombol Sekunder (*Secondary Button*)**:
   - Latar belakang: Putih
   - Batas: Biru Tua (#1E0E62)
   - Teks: Biru Tua
   - Penggunaan: Aksi sekunder (Batal, Kembali)

3. **Tombol *Outline* (*Outline Button*)**:
   - Latar belakang: Transparan
   - Batas: Warna teks saat ini
   - Penggunaan: Aksi tersier

4. **Tombol Ikon (*Icon Button*)**:
   - Latar belakang: Transparan atau solid
   - Hanya berisi ikon
   - Penggunaan: Navigasi, tindakan cepat

**B. Elemen Formulir (*Form Elements*)**

1. **Input Teks (*Text Input*)**:
   - Batas: Abu-abu muda dengan status fokus (biru tua)
   - Tinggi: 40px (sedang), 36px (kecil)
   - Radius batas: 8px
   - *Padding*: 12px horizontal
   - Status: *Default*, Fokus, Error, Nonaktif

2. ***Textarea***:
   - Gaya serupa dengan input teks
   - Tinggi minimum: 100px
   - Ukuran ulang: vertikal saja

3. ***Dropdown* Pilihan (*Select Dropdown*)**:
   - Gaya kustom dengan ikon panah
   - Menu *dropdown* dengan bayangan
   - Tinggi maksimum dengan *scroll* untuk banyak opsi

4. **Kotak Centang & Radio (*Checkbox & Radio*)**:
   - Gaya kustom dengan animasi tanda centang
   - Ukuran: 20x20px
   - Warna: Biru tua saat dicentang

5. **Pemilih Tanggal (*Date Picker*)**:
   - Antarmuka kalender dengan navigasi
   - Sorot tanggal saat ini dan tanggal dipilih
   - Nonaktifkan tanggal lampau untuk pemesanan

6. **Pemilih Waktu (*Time Picker*)**:
   - Tata letak grid untuk slot waktu
   - Tampilkan status tersedia/tidak tersedia
   - Umpan balik visual untuk pemilihan

**C. Kartu (*Cards*)**

1. **Kartu Layanan (*Service Card*)**:
   - Latar belakang putih dengan bayangan
   - Gambar mini (*thumbnail*) (rasio aspek 16:9)
   - Judul, deskripsi, harga
   - Tombol CTA
   - Efek *hover*: bayangan meningkat

2. **Kartu Terapis (*Therapist Card*)**:
   - Avatar/foto (bulat)
   - Nama, spesialisasi
   - Bintang rating
   - Tahun pengalaman
   - Tombol Lihat Profil

3. **Kartu Janji Temu (*Appointment Card*)**:
   - Lencana status (mendatang, selesai, dibatalkan)
   - Info tanggal & waktu
   - Nama layanan
   - Info terapis
   - Tombol tindakan

4. **Kartu Statistik Dasbor (*Dashboard Stats Card*)**:
   - Ikon + label + nilai
   - Kode warna per kategori
   - Indikator tren opsional

**D. Komponen Navigasi (*Navigation Components*)**

1. **Bilah Navigasi Atas (*Top Navigation Bar*)**:
   - Logo di kiri
   - Item menu di tengah (desktop)
   - *Dropdown* profil pengguna di kanan
   - Perilaku lengket (*sticky*) saat *scroll*
   - Tinggi: 70px

2. **Navigasi *Sidebar*** (untuk dasbor):
   - Posisi tetap di kiri
   - Lebar: 260px (diperluas), 70px (diciutkan)
   - Item menu dengan ikon + label
   - Indikator status aktif (aksen merah muda)
   - Dapat diciutkan untuk mobile

3. ***Breadcrumb***:
   - Tampilkan hierarki halaman saat ini
   - Pemisah: "/" atau "›"
   - Item terakhir tidak dapat diklik

4. ***Tab***:
   - Tata letak horizontal
   - *Tab* aktif dengan batas bawah (merah muda)
   - Animasi transisi halus

**E. Komponen Umpan Balik (*Feedback Components*)**

1. **Peringatan/Notifikasi (*Alerts/Notifications*)**:
   - Sukses: Latar belakang hijau dengan ikon
   - Error: Latar belakang merah dengan ikon
   - Peringatan: Latar belakang oranye dengan ikon
   - Info: Latar belakang biru dengan ikon
   - Dapat ditutup dengan tombol tutup

2. **Pesan *Toast* (*Toast Messages*)**:
   - Muncul dari sudut kanan atas
   - Hilang otomatis setelah 3-5 detik
   - Tumpuk beberapa *toast*
   - Animasi *slide-in*

3. **Indikator *Loading* (*Loading Indicators*)**:
   - *Spinner*: Melingkar dengan warna biru tua
   - Layar kerangka (*skeleton screen*): Untuk data yang sedang dimuat
   - Bilah kemajuan (*progress bar*): Untuk proses multi-langkah

4. **Dialog Modal (*Modal Dialogs*)**:
   - *Overlay* dengan latar belakang kabur (*backdrop blur*)
   - Kotak konten terpusat
   - Tombol tutup (X)
   - Bagian *header*, *body*, *footer*
   - Varian ukuran: kecil, sedang, besar, layar penuh

**F. Komponen Tampilan Data (*Data Display Components*)**

1. **Tabel (*Tables*)**:
   - *Zebra striping* untuk baris (latar belakang bergantian)
   - *Header* dengan indikator urutan
   - Efek *hover* pada baris
   - Tombol tindakan per baris
   - Kontrol halaman berganda
   - Responsif: *Scroll* horizontal pada mobile

2. **Daftar (*Lists*)**:
   - Item dengan avatar/ikon
   - Teks primer & sekunder
   - Tindakan atau info meta sisi kanan
   - Pembagi antar item

3. **Lencana (*Badges*)**:
   - Indikator status (baru, tertunda, disetujui, dll.)
   - Bentuk pil kecil, bulat
   - Kode warna
   - Ukuran: kecil, sedang, besar

4. **Pelacakan Kemajuan (*Progress Tracking*)**:
   - Indikator langkah untuk alur pemesanan
   - Bilah kemajuan dengan persentase
   - Penanda tonggak (*milestone*)

**G. Komponen Media (*Media Components*)**

1. **Avatar**:
   - Gambar melingkar
   - Ukuran: xs (24px), sm (32px), md (40px), lg (64px), xl (96px)
   - Cadangan (*fallback*) dengan inisial
   - Indikator status (titik *online*/*offline*)

2. **Galeri Gambar (*Image Gallery*)**:
   - Tata letak grid
   - *Lightbox* untuk tampilan penuh
   - *Lazy loading*
   - Rasio aspek dipertahankan

3. **Pemutar Video (*Video Player*)** (untuk ruang sesi):
   - Kontrol kustom
   - Opsi layar penuh
   - Bisukan/buka bisukan
   - Ganti kamera

Semua komponen ini dikembangkan dengan mempertimbangkan:
- **Responsivitas (*Responsiveness*)**: Bekerja optimal di desktop, tablet, dan mobile
- **Aksesibilitas (*Accessibility*)**: Navigasi *keyboard*, label ARIA, rasio kontras
- **Konsistensi (*Consistency*)**: Gaya visual yang seragam
- **Interaktivitas (*Interactivity*)**: Umpan balik yang jelas untuk setiap tindakan pengguna
- **Kinerja (*Performance*)**: Dioptimalkan untuk kecepatan pemuatan

Pustaka komponen ini memungkinkan pengembangan yang lebih cepat dan konsisten, sekaligus memudahkan pemeliharaan dan skalabilitas sistem di masa depan.

**[GAMBAR 4.18 - Sistem Tata Letak & Grid]** 🔴 **KRITIS**

**[GAMBAR 4.19 - Iconography System]** 🔴 **CRITICAL**

### 4.3.5.4 *Mockup* Halaman Publik (*Public Pages*)

Halaman publik adalah halaman yang dapat diakses tanpa autentikasi, berfungsi sebagai *front-facing website* untuk memberikan informasi tentang CUR-HEART dan mendorong konversi pengunjung menjadi klien.

---

#### A. Halaman Utama (*Landing Page* / Homepage)

**[GAMBAR 4.20 - *Mockup* Halaman Utama (*Landing Page*/Homepage)]** 📱
_Halaman publik - Bagian *hero*, ringkasan layanan, terapis, testimoni_

**Deskripsi:**
Halaman pertama yang dilihat pengunjung, dirancang untuk memberikan kesan profesional dan menenangkan sesuai sifat bisnis hipnoterapi.

**Komponen Utama:**
Halaman terdiri dari *hero section* dengan gradien biru-ungu dan CTA utama, ringkasan layanan dalam grid 3 kolom, bagian *Why Choose Us* dengan USP, featured therapists carousel, visualisasi *How It Works*, testimoni klien, blog posts terbaru, dan footer CTA untuk booking.

**Teknis & Interaksi:**
Menggunakan animasi scroll halus, hover effect, lazy loading, dan responsive layout dengan sticky navigation. Semua elemen mengikuti design system (warna primer biru tua #1E0E62, aksen merah muda #FF6B7A).

***User Flow***:
Pengunjung → Landing page → Klik "Book Your Session" → Redirect ke halaman Services (atau login jika sudah registered)

---

#### B. Halaman Tentang Kami (*About Us Page*)

**[GAMBAR 4.21 - *Mockup* Halaman Tentang Kami (*About Us Page*)]** 📱
_Halaman publik - Cerita perusahaan, nilai, tim, sertifikasi_

**Deskripsi:**
Halaman yang menjelaskan CUR-HEART sebagai organisasi, membangun kepercayaan dan kredibilitas melalui cerita, visi misi, dan profil tim.

**Komponen Utama:**
Halaman menyajikan page header dengan breadcrumb, bagian *Our Story* tentang sejarah pendirian dan milestone, visi & misi dalam layout 2 kolom, core values dengan ikon, profil tim dalam grid dengan foto dan bio, logo sertifikasi dan partnerships, serta CTA untuk bertemu dengan terapis.

**Teknis & Interaksi:**
Fade-in animation saat scroll, hover effect pada kartu tim untuk menampilkan social links, responsive grid yang menyesuaikan layout berdasarkan viewport.

***User Flow***:
Pengunjung → About Us → Baca informasi → Build trust → Klik "Meet Our Therapists" atau "Book Session"

---

#### C. Halaman Layanan (*Services Page* / Katalog Layanan)

**[GAMBAR 4.22 - *Mockup* Halaman Katalog Layanan (*Services Catalog Page*)]** 📱
_Halaman publik - Grid 6 layanan dengan harga dan deskripsi_

**Deskripsi:**
Katalog lengkap layanan hipnoterapi yang membantu calon klien memahami opsi layanan dan memilih sesuai kebutuhan.

**Komponen Utama:**
Halaman menampilkan page header dengan breadcrumb, filter & search section untuk kategori dan harga, services grid responsif dengan informasi lengkap per layanan, pagination atau load more, serta CTA untuk assessment gratis.

**Teknis & Interaksi:**
Instant search filtering, smooth animation saat apply filter, hover scale-up effect pada cards, skeleton loading state, responsive card grid.

***User Flow***:
Pengunjung → Services page → Browse/filter → Klik "View Details" → Service Detail page

---

#### D. Halaman Detail Layanan (*Service Detail Page*)

**[GAMBAR 4.23 - *Mockup* Halaman Detail Layanan (*Service Detail Page*)]**
_Halaman publik - Informasi layanan detail, manfaat, CTA *booking*_

Halaman Detail Layanan memberikan informasi lengkap tentang satu layanan hipnoterapi spesifik untuk mengedukasi calon klien dan mendorong *booking*.

**Komponen Utama:**
Halaman menyajikan page header dengan hero image, bagian ringkasan dengan harga dan quick facts, navigasi tabs untuk konten detail, terapis yang direkomendasikan, layanan terkait, ulasan pelanggan dengan rating, serta sticky CTA sidebar atau bottom bar untuk booking.

**Teknis & Interaksi:**
Sticky CTA saat scroll, transisi halus pergantian tabs, animasi accordion FAQ, lazy load ulasan, modal popup saat klik "Book Now" untuk pilih terapis. Responsive dengan bottom bar pada mobile.

***User Flow***:
Pengguna di Halaman Detail → Baca informasi → Klik "Book Now" → Pilih terapis → Alur *booking*

---

#### E. Halaman Direktori Terapis (*Therapists Directory Page*)

**[GAMBAR 4.24 - *Mockup* Halaman Direktori Terapis (*Therapists Directory Page*)]**
_Halaman publik - *Grid* profil terapis dengan *filter*/*search*_

Halaman Direktori Terapis menampilkan daftar semua terapis di CUR-HEART, memungkinkan calon klien menjelajah, mem-*filter*, dan memilih terapis sesuai preferensi.

**Komponen Utama:**
Halaman terdiri dari page header, pencarian & filter komprehensif dengan opsi spesialisasi dan ketersediaan, opsi pengurutan, therapists grid responsif dengan kartu lengkap, featured therapists banner, serta CTA untuk rekomendasi terapis.

**Teknis & Interaksi:**
Pemfilteran pencarian real-time, hasil filter diperbarui dengan skeleton loading, infinite scroll atau paginasi, bookmark/favorite terapis (jika sudah login), quick view modal saat hover (opsional). Responsive dengan grid yang menyesuaikan kolom.

***User Flow***:
Pengguna → Direktori Terapis → Terapkan *filter* → Jelajah kartu → Tertarik pada satu → Klik "View Profile" → Halaman Profil Terapis

---

#### F. Halaman Profil Terapis (*Therapist Profile Page*)

**[GAMBAR 4.25 - *Mockup* Halaman Profil Terapis (*Therapist Profile Page*)]**
_Halaman publik - Bio, kredensial, spesialisasi, ulasan, *booking*_

Halaman Profil Terapis menampilkan informasi detail tentang seorang terapis, termasuk latar belakang, keahlian, ulasan, dan ketersediaan sebagai halaman pengambilan keputusan sebelum booking.

**Komponen Utama:**
Halaman menyajikan hero section dengan foto dan quick stats, bio lengkap, spesialisasi & keahlian dengan progress bar, pendidikan & sertifikasi, pendekatan konsultasi, tabel layanan & harga, kalender ketersediaan interaktif, ulasan & testimoni dengan rating, video introduction, FAQ, terapis terkait, serta sticky booking sidebar.

**Teknis & Interaksi:**
Sticky booking sidebar saat scroll, kalender interaktif dengan klik slot langsung book, ulasan loadmore/infinite scroll, putar video dengan lightbox, smooth scroll ke bagian via navigasi. Responsive dengan sidebar di bawah pada mobile.

***User Flow***:
Pengguna di Profil Terapis → Terkesan dengan kredensial → Cek ketersediaan → Klik slot waktu tersedia → *Modal booking* terbuka → Lanjutkan alur *booking*

---

#### G. Halaman Daftar Blog (*Blog List Page*)

**[GAMBAR 4.26 - *Mockup* Halaman Daftar Blog (*Blog List Page*)]**
_Halaman publik - Daftar artikel blog dengan pencarian dan *filter*_

Halaman Daftar Blog menampilkan artikel edukatif tentang hipnoterapi, kesehatan mental, dan cerita sukses untuk *content marketing*, SEO, dan *thought leadership*.

**Komponen Utama:**
Halaman terdiri dari page header, pos unggulan untuk artikel terbaru, pencarian & filter kategori dengan tag cloud, grid pos blog responsif, sidebar dengan pencarian dan pos populer, pagination atau load more, serta CTA newsletter.

**Teknis & Interaksi:**
Pencarian dengan debounce untuk filter instan, skeleton loading, efek hover zoom gambar, infinite scroll atau paginasi tradisional. Responsive dengan sidebar di bawah pada mobile.

***User Flow***:
Pengguna → Jelajah/cari artikel → Klik artikel → Halaman Detail Blog

---

#### H. Halaman Detail Blog (*Blog Detail Page*)

**[GAMBAR 4.27 - *Mockup* Halaman Detail Blog (*Blog Detail Page*)]**
_Halaman publik - Artikel blog lengkap dengan pos terkait_

Halaman Detail Blog menampilkan artikel lengkap dengan format mudah dibaca dan mendorong keterlibatan melalui komentar, berbagi, dan artikel terkait.

**Komponen Utama:**
Halaman menyajikan header artikel dengan meta info dan gambar unggulan, konten artikel terformat dengan daftar isi sticky, kotak bio penulis, tags yang dapat diklik, bagian keterlibatan untuk interaksi, bagian komentar dengan formulir, artikel terkait, CTA newsletter, serta sticky social share bar.

**Teknis & Interaksi:**
Daftar isi sticky dengan smooth scroll, lazy load gambar, code syntax highlighting, berbagi sosial dengan popup/native share API, pengiriman komentar AJAX, reading progress bar di atas. Responsive dengan share bar di bawah pada mobile.

***User Flow***:
Pengguna baca artikel → Terlibat (suka/komentar) → Klik artikel terkait atau CTA "Book Session"

---

### 4.3.5.5 *Mockup* Halaman Pendukung (*Support Pages*)

Halaman pendukung (*support pages*) adalah halaman-halaman pendukung yang memberikan informasi penting terkait kontak, FAQ, kebijakan privasi, dan syarat & ketentuan. Halaman ini penting untuk transparansi, kepatuhan, dan layanan pelanggan (*customer service*).

#### A. Halaman Hubungi Kami (*Contact Us Page*)

**[GAMBAR 4.28 - *Mockup* Halaman Hubungi Kami (*Contact Us Page*)]**
_Halaman publik - Formulir kontak, peta lokasi, tautan media sosial_

Halaman Hubungi Kami menyediakan berbagai cara untuk menghubungi CUR-HEART, termasuk formulir kontak, alamat kantor, nomor telepon, email, dan media sosial untuk dukungan pelanggan dan pertanyaan.

**Komponen Utama:**
Halaman terdiri dari page header, formulir kontak dengan validasi, kartu informasi kontak untuk lokasi/telepon/email, jam operasional, Google Maps embed interaktif, tautan media sosial, pintasan FAQ, serta metode kontak alternatif seperti WhatsApp dan live chat.

**Teknis & Interaksi:**
Validasi formulir real-time, notifikasi toast sukses/kesalahan, peta interaktif (zoom, geser), klik untuk telepon/email pada mobile, tombol WhatsApp floating. Responsive dengan grid yang menyesuaikan.

***User Flow***:
Pengguna punya pertanyaan → Halaman Kontak → Isi formulir atau pilih metode kontak → *Submit* → Terima konfirmasi

---

#### B. Halaman FAQ (*FAQ Page*)

**[GAMBAR 4.29 - *Mockup* Halaman FAQ (*FAQ Page*)]**
_Halaman publik - Pertanyaan yang Sering Diajukan dengan *accordion*_

Halaman FAQ menjawab pertanyaan yang sering ditanyakan oleh calon klien dan klien, mengurangi beban customer service dan membantu pengguna menemukan jawaban dengan cepat.

**Komponen Utama:**
Halaman menyajikan page header, bilah pencarian dengan pemfilteran real-time, tab kategori horizontal untuk berbagai topik, daftar FAQ accordion per kategori, tindakan cepat untuk kontak support, bagian umpan balik untuk setiap item, serta sumber daya terkait.

**Teknis & Interaksi:**
Accordion satu atau beberapa terbuka, pencarian menyorot teks cocok, smooth scroll ke bagian jika dari link eksternal, pemungutan suara AJAX, deep linking untuk FAQ spesifik. Responsive dengan tabs scroll horizontal pada mobile.

***User Flow***:
Pengguna punya pertanyaan → Halaman FAQ → Cari atau jelajah kategori → Temukan jawaban → Terpecahkan atau klik "Contact Support"

---

#### C. Halaman Kebijakan Privasi (*Privacy Policy Page*)

**[GAMBAR 4.30 - *Mockup* Halaman Kebijakan Privasi (*Privacy Policy Page*)]**
_Halaman publik - Kebijakan privasi dan informasi perlindungan data_

Halaman Kebijakan Privasi menjelaskan bagaimana CUR-HEART mengumpulkan, menggunakan, menyimpan, dan melindungi data pribadi pengguna, penting untuk compliance (GDPR, regulasi Indonesia) dan membangun kepercayaan.

**Komponen Utama:**
Halaman terdiri dari page header dengan tanggal update, daftar isi sidebar sticky dengan scroll spy untuk navigasi mudah, bagian konten terstruktur yang mencakup informasi pengumpulan data, penggunaan, berbagi, keamanan, hak pengguna, cookies, layanan pihak ketiga, privasi anak, perubahan kebijakan, kotak sorotan untuk catatan penting, serta CTA untuk pertanyaan privasi.

**Teknis & Interaksi:**
Konten long-form scrollable, TOC sticky untuk navigasi mudah, smooth scroll dengan offset untuk header, CSS print-friendly, opsi unduh sebagai PDF. Responsive dengan TOC di atas pada mobile.

***User Flow***:
Pengguna khawatir tentang privasi → Kebijakan Privasi → Baca bagian relevan → Terjamin atau hubungi tim privasi

---

#### D. Halaman Syarat & Ketentuan (*Terms & Conditions Page*)

**[GAMBAR 4.31 - *Mockup* Halaman Syarat dan Ketentuan (*Terms & Conditions Page*)]**
_Halaman publik - Syarat layanan dan kondisi penggunaan_

Halaman Syarat & Ketentuan menetapkan aturan hukum, kewajiban, dan hak antara CUR-HEART dan pengguna, melindungi kedua belah pihak dan menetapkan harapan penggunaan layanan.

**Komponen Utama:**
Halaman menyajikan page header dengan tanggal update, daftar isi sidebar sticky untuk navigasi, bagian konten terstruktur yang mencakup penerimaan ketentuan, deskripsi layanan, registrasi akun, booking, pembayaran, kebijakan pembatalan, perilaku pengguna, hubungan terapis-klien, kerahasiaan, hak kekayaan intelektual, penafian, batasan tanggung jawab, ganti rugi, penghentian, penyelesaian sengketa, hukum yang berlaku, perubahan ketentuan, pesan penting highlighted, serta bagian pengakuan dengan checkbox.

**Teknis & Interaksi:**
Mirip dengan Privacy Policy, navigasi TOC sticky, scrolling halus, opsi cetak/unduh, sorot istilah pencarian (jika dari search). Responsive dengan TOC collapsible pada mobile.

***User Flow***:
Pengguna mendaftar/*booking* → Diminta menerima ketentuan → Klik tautan → Halaman Ketentuan → Baca atau *scroll* ke bawah → *Checkbox* terima → Lanjutkan dengan registrasi/*booking*

---

### 4.3.5.6 *Mockup* Halaman Autentikasi (*Authentication Pages*)

Halaman autentikasi (*authentication pages*) adalah halaman-halaman yang menangani proses *login*, registrasi, dan pemulihan kata sandi (*password recovery*). Desain halaman autentikasi harus menyeimbangkan antara keamanan, kegunaan, dan pengalaman pengguna yang lancar.

---

#### A. Halaman *Login* (*Login Page*)

**[GAMBAR 4.32 - *Mockup* Halaman *Login* (*Login Page*)]**
_Halaman autentikasi - Formulir email/kata sandi, ingat saya, tautan lupa kata sandi_

Halaman Login memungkinkan pengguna yang sudah ada untuk masuk ke akun mereka dan mengakses dashboard serta fitur yang memerlukan autentikasi dengan desain sederhana, jelas, dan aman.

**Komponen Utama:**
Halaman menggunakan tata letak split screen dengan ilustrasi wellness dan branding, formulir login dengan email dan password field, checkbox "Remember Me", tautan "Forgot Password", tombol "Log In", metode login alternatif dengan SSO Google/Facebook, ajakan registrasi, indikator keamanan SSL, error handling per field, serta success state dengan spinner.

**Teknis & Interaksi:**
Validasi real-time saat blur, submit validation, tombol Enter submit form, navigasi Tab antar field, animasi show/hide password, popup/OAuth flow untuk social login, session timeout warning. Security: no plaintext password, CSRF protection, rate limiting, CAPTCHA after failed attempts, HTTPS transmission. Responsive dengan form optimization untuk mobile.

***User Flow***:
Pengguna → Halaman *Login* → Masukkan kredensial → Klik "Log In" → Autentikasi → Arahkan ke *Dashboard* (berbasis peran: klien/terapis/admin)

---

#### B. Halaman Registrasi (*Register Page*)

**[GAMBAR 4.33 - *Mockup* Halaman Registrasi (*Register Page*) (Klien & Terapis)]**
_Halaman autentikasi - Formulir registrasi multi-langkah, penerimaan ketentuan_

Halaman Registrasi memungkinkan pengguna baru membuat akun CUR-HEART dengan membedakan tipe pengguna (Klien vs Terapis) dan mengumpulkan informasi yang diperlukan tanpa membebani pengguna.

**Komponen Utama:**
Halaman menggunakan tata letak split screen dengan ilustrasi dan branding, pemilihan tipe pengguna antara Client dan Therapist, formulir registrasi yang berbeda per tipe dengan field yang disesuaikan untuk klien atau terapis termasuk upload dokumen untuk terapis, checkbox terms & conditions wajib, tombol submit dengan loading state, login prompt, serta trust indicators untuk keamanan.

**Teknis & Interaksi:**
Validasi real-time per field, email uniqueness check, password strength visual indicator (red/yellow/green), inline error messages dengan instruksi jelas, success icon untuk valid fields. Alur Sukses - Klien: akun langsung dibuat, welcome message, verification email sent, redirect ke onboarding/dashboard - Terapis: aplikasi submitted, "We'll review in 2-3 days", notification email, redirect ke pending status page. Progressive disclosure (tampilkan form setelah tipe dipilih), smooth transitions, file upload dengan drag & drop support. Responsive dengan input lebih besar untuk mobile.

***User Flow***:
Pengguna → Halaman Registrasi → Pilih tipe pengguna (Klien/Terapis) → Isi formulir → Terima S&K → *Submit* → Email verifikasi dikirim → Pesan sukses → Arahkan

---

#### C. Halaman Lupa Kata Sandi (*Forgot Password Page*)

**[GAMBAR 4.34 - *Mockup* Halaman Lupa Kata Sandi (*Forgot Password Page*)]**
_Halaman autentikasi - Input email untuk tautan reset kata sandi_

Halaman Lupa Kata Sandi membantu pengguna yang lupa kata sandi mereka untuk melakukan reset melalui verifikasi email dengan proses aman namun ramah pengguna.

**Komponen Utama:**
Halaman menggunakan tata letak formulir terpusat sederhana dengan header berisi logo dan judul, formulir input email dengan validasi, tombol submit, back to login link, success state dengan instruksi dan opsi resend link, error state dengan saran, serta security features untuk rate limiting dan token expiry.

**Teknis & Interaksi:**
Halaman sederhana dengan single purpose, auto-focus pada email input, submit dengan Enter key, error messages yang jelas, timer countdown untuk resend, visual feedback validasi email. Responsive dengan form optimization.

***User Flow***:
Pengguna lupa kata sandi → Klik "Forgot Password" dari *Login* → Masukkan email → *Submit* → Periksa email → Klik tautan reset → Arahkan ke halaman *Reset Password*

---

#### D. Halaman Reset Kata Sandi (*Reset Password Page*)

**[GAMBAR 4.35 - *Mockup* Halaman Reset Kata Sandi (*Reset Password Page*)]**
_Halaman autentikasi - Formulir kata sandi baru dengan konfirmasi_

Halaman Reset Kata Sandi dibuka dari tautan di email reset, memungkinkan pengguna memasukkan kata sandi baru dan mengkonfirmasinya dengan aman dan feedback yang jelas.

**Komponen Utama:**
Halaman menggunakan tata letak formulir terpusat dengan header berisi logo dan judul, validasi token otomatis saat load, formulir reset password dengan field new password dan confirm password yang dilengkapi strength indicator dan checklist persyaratan, tombol submit, security indicators dengan countdown expiry, success state dengan auto-redirect, serta error handling untuk berbagai kondisi.

**Teknis & Interaksi:**
Password strength meter real-time, requirements checklist dengan checkmarks, confirm password match indicator, token timer countdown, expiry warning ("Only 5 minutes left!"), auto-redirect setelah sukses, one-time use token (invalid setelah reset berhasil). Security: token-based reset (secure, time-limited), password complexity enforcement, one-time tokens, HTTPS transmission, CSRF protection, rate limiting, password history check (optional). Responsive dengan form optimization.

***User Flow***:
Pengguna → Klik tautan reset dari email → Token divalidasi → Masukkan kata sandi baru → Konfirmasi kata sandi → *Submit* → Sukses → Arahkan ke *Login* → *Login* dengan kata sandi baru

---

### 4.3.5.7 *Mockup* ***Dashboard*** Klien (*Client Dashboard Pages*)

***Dashboard*** Klien adalah area setelah *login* khusus untuk klien yang telah terdaftar. ***Dashboard*** ini memungkinkan klien untuk melakukan *booking* sesi, mengelola janji temu (*manage appointments*), melacak kemajuan (*track progress*), dan berkomunikasi dengan terapis.

---

#### A. ***Dashboard*** Klien (Utama) (*Client Dashboard Main*)

**[GAMBAR 4.36 - *Mockup* ***Dashboard*** Klien (*Client Dashboard*) (Utama)]**
_*Dashboard* klien - Kartu ringkasan, janji temu mendatang, tindakan cepat_

Dashboard Klien Utama adalah landing page setelah klien login, memberikan overview status appointments, progress, dan quick actions untuk booking sesi.

**Komponen Utama:**
Dashboard menyajikan top navigation bar dengan menu dan notifikasi, sidebar navigation untuk desktop, welcome section dengan greeting personal, quick stats cards untuk metrik utama, next appointment card unggulan dengan countdown, quick actions section untuk fungsi cepat, upcoming appointments list, progress overview widget dengan grafik, recent messages threads, serta helpful resources section.

**Teknis & Interaksi:**
Real-time updates (WebSocket untuk notifikasi), timer countdown untuk sesi berikutnya, hover effects pada kartu, skeleton loading untuk async data. Responsive: collapse sidebar pada mobile dengan bottom nav bar, tombol refresh untuk manual update.

***User Flow***:
Klien *login* → ***Dashboard*** → Gambaran umum semua data → Tindakan cepat atau navigasi ke bagian tertentu

---

#### B. *Booking* Langkah 1 - Pilih Layanan (*Booking Step 1 - Select Service*)

**[GAMBAR 4.37 - *Mockup* *Booking* Langkah 1 - Pilih Layanan (*Select Service*)]**
_Klien - Pilih layanan dengan deskripsi dan harga_

Langkah pertama dalam alur booking di mana klien memilih layanan hipnoterapi yang ingin dibooking, dengan kemudahan browsing dan comparison antar layanan.

**Komponen Utama:**
Halaman menyajikan progress indicator stepper untuk tracking proses, page header dengan breadcrumb, pencarian & filter untuk memudahkan pencarian layanan, services grid dengan kartu detail per layanan, modal/accordion untuk detail lengkap layanan, popular services highlight dengan badge, help section untuk konsultasi, serta navigasi dengan tombol continue yang disabled hingga layanan dipilih.

**Teknis & Interaksi:**
Single selection (radio behavior), real-time filter results, search dengan debounce, visual feedback pemilihan kartu, smooth modal/accordion animations. Responsive: vertical card stack, sticky continue button pada mobile.

***User Flow***:
Klien → *Book Session* → Langkah 1 → Telusuri layanan → Pilih satu → Klik "Continue" → Langkah 2

---

#### C. *Booking* Langkah 2 - Pilih Terapis (*Booking Step 2 - Choose Therapist*)

**[GAMBAR 4.38 - *Mockup* *Booking* Langkah 2 - Pilih Terapis (*Choose Therapist*)]**
_Klien - Pilih terapis dengan profil dan ketersediaan_

Langkah kedua di mana klien memilih terapis yang akan melakukan sesi, halaman ini memfilter terapis berdasarkan spesialisasi dari layanan yang dipilih di Langkah 1.

**Komponen Utama:**
Halaman menyajikan progress stepper dengan langkah sebelumnya completed, selected service display sticky untuk referensi, filter & sort section komprehensif untuk preferensi terapis, therapists list dengan kartu detail per terapis termasuk availability indicator, modal profil terapis untuk quick view, selected state visual feedback, no preference option untuk auto-assign, serta comparison feature opsional untuk membandingkan terapis.

**Teknis & Interaksi:**
Filter/sort dengan smooth transitions, single selection mode, modal profil dengan slideshow foto, responsive cards, async loading state. Navigasi: tombol "← Back" ke Langkah 1, tombol "Continue" sticky bawah disabled hingga terapis dipilih, menampilkan nama terapis terpilih.

***User Flow***:
Langkah 2 → Telusuri terapis → Filter/*sort* → Lihat profil → Pilih terapis → *Continue* → Langkah 3

---

#### D. *Booking* Langkah 3 - Pilih Tanggal & Waktu (*Booking Step 3 - Select Date & Time*)

**[GAMBAR 4.39 - *Mockup* *Booking* Langkah 3 - Pilih Tanggal & Waktu (*Select Date & Time*)]**
_Klien - *Picker* kalender dan slot waktu tersedia_

Langkah ketiga di mana klien memilih tanggal dan waktu untuk sesi mereka berdasarkan ketersediaan terapis yang dipilih.

**Komponen Utama:**
Halaman menyajikan progress stepper, booking summary card sticky dengan detail layanan dan terapis, session type selection antara online dan offline, calendar component untuk memilih tanggal dengan visualisasi ketersediaan, time slots section yang muncul setelah tanggal dipilih, time zone info untuk sesi online, earliest available quick action, session notes optional untuk persiapan terapis, serta validation messages.

**Teknis & Interaksi:**
Klik tanggal kalender → load slots (API call), single select time slots, real-time availability checking, skeleton loading untuk slots, mobile: swipe calendar navigation, auto-refresh availability setiap 60 detik. Navigasi: tombol "← Back" ke Langkah 2, tombol "Continue" sticky bawah disabled hingga tanggal & waktu dipilih, menampilkan tanggal & waktu terpilih.

***User Flow***:
Langkah 3 → Pilih tipe sesi → Pilih tanggal dari kalender → Pilih slot waktu → Tambah catatan (opsional) → *Continue* → Langkah 4

---

#### E. *Booking* Langkah 4 - Konfirmasi & Pembayaran (*Booking Step 4 - Confirm & Payment*)

**[GAMBAR 4.40 - *Mockup* *Booking* Langkah 4 - Konfirmasi & Pembayaran (*Confirm & Payment*)]** 👤
_Klien - Ringkasan *booking*, pemilihan metode pembayaran_

Langkah terakhir dalam alur *booking* di mana klien meninjau detail *booking*, memilih metode pembayaran, dan mengkonfirmasi pembayaran.

**Komponen Utama:**
Halaman menyajikan progress stepper dengan semua langkah sebelumnya completed, booking summary card dengan review lengkap untuk service/therapist/session/notes, pricing breakdown dengan detail biaya, promo code section untuk diskon, payment method selection dengan berbagai opsi, terms agreement checkboxes wajib, action buttons untuk konfirmasi pembayaran, security indicators untuk kepercayaan, serta cancellation policy summary.

**Teknis & Interaksi:**
Validasi kode promo real-time, pemilihan payment update UI, validasi checkbox terms, overlay loading saat proses payment, error handling payment gagal, session timeout warning. Payment Flow: Klik "Confirm & Pay" → redirect payment gateway Midtrans → opsi payment → user complete → redirect kembali dengan status → Success State redirect ke Booking Success page, tampilkan konfirmasi, kirim email.

***User Flow***:
Langkah 4 → Tinjau semua detail → Masukkan promo (opsional) → Pilih pembayaran → Setuju syarat → *Confirm & Pay* → *Payment gateway* → Pembayaran berhasil → Halaman *Booking Success*

---

#### F. Halaman Sukses *Booking* (*Booking Success Page*)

**[GAMBAR 4.41 - *Mockup* Halaman Sukses *Booking* (*Booking Success Page*)]**
_Klien - Pesan konfirmasi, detail *booking*, langkah berikutnya_

Halaman ditampilkan setelah pembayaran berhasil, memberikan konfirmasi booking dan informasi langkah berikutnya.

**Komponen Utama:**
Halaman menyajikan success animation dengan checkmark dan konfeti, success message dengan konfirmasi, booking details card lengkap dengan ID booking, next steps section berisi panduan, action buttons untuk berbagai keperluan, preparation tips untuk sesi pertama, contact support untuk perubahan, related actions untuk booking tambahan, serta confirmation email notice.

**Teknis & Interaksi:**
Animasi konfeti saat dimuat (once), salin ID booking ke clipboard, tambahkan ke kalender menghasilkan file .ics, unduh faktur (PDF generation), auto-redirect ke appointments setelah 30 detik (opsional dengan countdown).

***User Flow***:
Halaman *Booking Success* → Lihat detail / Unduh faktur / Tambahkan ke kalender → Kembali ke ***Dashboard*** atau Lihat *Appointments*

---

#### G. Daftar Janji Temu Saya (*My Appointments List*)

**[GAMBAR 4.42 - *Mockup* Daftar Janji Temu Saya (*My Appointments List*)]**
_Klien - Tabel/kartu semua *booking* dengan status dan tindakan_

Halaman menampilkan daftar lengkap semua janji temu klien (upcoming, past, cancelled) dan memungkinkan pengelolaan.

**Komponen Utama:**
Halaman menyajikan page header, tabs navigation untuk kategori appointments, filter & sort section komprehensif, appointments list upcoming dengan card detail lengkap dan countdown timer, empty states untuk setiap tab, past appointments tab dengan opsi review, cancelled appointments tab dengan info pengembalian, pagination untuk navigasi, serta bulk actions opsional.

**Teknis & Interaksi:**
Real-time updates untuk perubahan status, timer countdown diperbarui setiap menit, hasil filter/pencarian dengan transisi halus, skeleton loading untuk janji, pull to refresh mobile, infinite scroll atau paginasi.

***User Flow***:
Klien → *My Appointments* → Telusuri daftar → Lihat detail atau ambil tindakan (*join*/*reschedule*/*cancel*)

---

#### H. Halaman Detail Janji Temu (*Appointment Detail Page*)

**[GAMBAR 4.43 - *Mockup* Halaman Detail Janji Temu (*Appointment Detail Page*)]**
_Klien - Detail *booking* lengkap, opsi *reschedule/cancel*_

Halaman menampilkan informasi lengkap tentang satu janji temu spesifik, termasuk semua detail, status, dan tindakan yang tersedia.

**Komponen Utama:**
Halaman menyajikan page header dengan ID booking dan status badge, appointment summary card dengan detail date/time/service/therapist, session location/link berbeda untuk online dan offline, your notes section yang dapat diedit, payment information dengan breakdown dan invoice, booking history timeline vertikal, actions section berbeda untuk upcoming dan past appointments, session notes setelah sesi, review section jika sudah diulas, cancellation policy box dengan countdown, serta support section.

**Teknis & Interaksi:**
Pembaruan status real-time, timer countdown, tombol join muncul 15 menit sebelum sesi, konfirmasi modal untuk tindakan, validasi formulir untuk reschedule/cancel, auto-refresh sebelum waktu sesi.

***User Flow***:
*Appointments List* → Klik janji temu → Halaman detail → Lihat info / Ambil tindakan (*join*/*reschedule*/*cancel*/*review*)

---

#### I. ***Dashboard*** Pelacakan Kemajuan Klien (*Client Progress Tracking Dashboard*)

**[GAMBAR 4.44 - *Mockup* ***Dashboard*** Pelacakan Kemajuan Klien (*Client Progress Tracking Dashboard*)]**
_Klien - Grafik yang menampilkan metrik kecemasan, kepercayaan diri, kualitas tidur_

Halaman membantu klien melihat perkembangan mereka dalam perjalanan terapi, menampilkan metrik, grafik, dan wawasan tentang kemajuan kesejahteraan.

**Komponen Utama:**
Halaman menyajikan page header dengan pemilih rentang tanggal, progress overview cards untuk metrik utama, wellness score chart dengan grafik garis perkembangan, session attendance chart untuk frekuensi sesi, goals & milestones section dengan progress tracking, mood tracking chart multi-dimensi, session summary statistics, achievements & badges untuk gamifikasi, therapist notes summary, progress reports yang dapat diunduh, comparison metrics antar periode, insights & recommendations berbasis data, serta quick actions.

**Teknis & Interaksi:**
Grafik interaktif (hover untuk tooltip, klik untuk drill-down), pemilih rentang tanggal memperbarui semua grafik, animasi halus untuk rendering grafik, ekspor data sebagai CSV/PDF, grafik responsif adaptasi ke mobile, pembaruan real-time saat data baru tersedia.

***User Flow***:
Klien → *My Progress* → Lihat grafik & metrik → Identifikasi tren → Ambil tindakan (*book* sesi, perbarui tujuan)

---

#### J. Pesan Klien (*Client Messages*) (*Chat* dengan Terapis)

**[GAMBAR 4.45 - *Mockup* Pesan Klien (*Client Messages*) (*Chat* dengan Terapis)]**
_Klien - Antarmuka *chat* dengan terapis_

Halaman memungkinkan klien berkomunikasi dengan terapis melalui antarmuka chat untuk pertanyaan lanjutan, koordinasi janji temu, dan dukungan berkelanjutan.

**Komponen Utama:**
Halaman menyajikan page layout split-view untuk desktop, conversations list sidebar dengan search dan list chat, active conversation area dengan header terapis, message thread kronologis dengan berbagai tipe pesan, input area dengan teks multiline dan attachment options, empty conversation state, quick responses untuk balasan cepat, automated messages dari sistem, conversation info sidebar opsional, notification settings per chat, privacy & guidelines banner, serta offline/error states.

**Teknis & Interaksi:**
Perpesanan real-time WebSocket/Pusher, indikator mengetik, tanda terima dibaca read receipts, status pengiriman pesan, auto-scroll ke bawah pada pesan baru, lightbox pratinjau gambar, progress bar unggah file, antarmuka perekaman pesan suara, cari dalam percakapan, opsi salin/hapus pesan (long press/right click), pemilih emoji dengan kategori, reaksi pesan opsional.

***User Flow***:
Klien → *Messages* → Pilih percakapan terapis → Baca pesan → Ketik balasan → Kirim → Pengiriman waktu nyata

---

### 4.3.5.8 *Mockup* ***Dashboard*** Terapis (*Therapist Dashboard Pages*)

***Dashboard*** Terapis adalah area khusus untuk terapis yang telah terdaftar dan disetujui (*approved*). ***Dashboard*** ini memungkinkan terapis untuk mengelola jadwal (*schedule*), janji temu (*appointments*), klien (*clients*), sesi (*sessions*), dan penghasilan (*earnings*).

---

#### A. ***Dashboard*** Terapis (Utama) (*Therapist Dashboard Main*)

**[GAMBAR 4.46 - *Mockup* ***Dashboard*** Terapis (*Therapist Dashboard*) (Utama)]**
_*Dashboard* terapis - Jadwal hari ini, statistik, tindakan cepat_

Dashboard Terapis Utama adalah landing page setelah terapis login, memberikan overview lengkap dari jadwal hari ini, janji temu mendatang, penghasilan, dan metrik kunci.

**Komponen Utama:**
Halaman menyajikan top navigation & sidebar dengan menu terapis, welcome section dengan greeting dan tanggal, key metrics cards untuk today's sessions/total clients/earnings/rating, today's schedule card dengan timeline appointments, upcoming clients card dengan list klien berikutnya, recent activities feed, earnings overview widget dengan grafik, client reviews section, quick actions untuk fungsi umum, serta notifications center.

**Teknis & Interaksi:**
Pembaruan real-time untuk booking baru, auto-refresh jadwal setiap 5 menit, timer countdown untuk sesi berikutnya, notifikasi popup/toast, tata letak responsif.

***User Flow***:
Terapis *login* → ***Dashboard*** → Gambaran umum metrik → Periksa jadwal hari ini → Ambil tindakan

---

#### B. Manajemen Jadwal Terapis (*Therapist Schedule Management*)

**[GAMBAR 4.47 - *Mockup* Manajemen Jadwal Terapis (*Therapist Schedule Management*)]**
_Terapis - Tampilan kalender semua *booking*, filter berdasarkan status_

Halaman Schedule Management memungkinkan terapis melihat kalender janji temu dengan berbagai tampilan (day, week, month) dan mengelola booking.

**Komponen Utama:**
Halaman menyajikan page header dengan tombol "Set Availability", calendar view selector untuk day/week/month, week view default dengan grid timeline dan appointment blocks berwarna, day view terperinci dengan informasi lengkap, month view dengan kalender grid, filter & legend untuk status dan tipe sesi, sidebar desktop dengan mini kalender dan statistik, appointment actions modal untuk detail dan tindakan, serta time off blocks visualization.

**Teknis & Interaksi:**
Transisi halus antar tampilan, drag & drop reschedule dengan konfirmasi, pembaruan real-time dari booking baru, sinkronisasi dengan Google Calendar opsional, ekspor kalender (.ics), opsi cetak jadwal.

***User Flow***:
Terapis → *My Schedule* → Pilih tampilan → Telusuri janji temu → Klik untuk detail → Ambil tindakan

---

#### C. Pengaturan Ketersediaan Terapis (*Therapist Availability Settings*)

**[GAMBAR 4.48 - *Mockup* Pengaturan Ketersediaan Terapis (*Therapist Availability Settings*)]**
_Terapis - Atur jadwal mingguan, blokir tanggal/waktu_

Halaman Availability Settings memungkinkan terapis mengatur jam kerja reguler, tanggal spesifik tidak tersedia, dan waktu istirahat yang mempengaruhi ketersediaan booking untuk klien.

**Komponen Utama:**
Halaman menyajikan page header, working hours section dengan pengaturan per hari dan break configuration, session duration settings untuk default durasi dan buffer time, booking window preferences, specific dates unavailable untuk time off/holidays, override availability untuk tanggal khusus, availability preview dengan mini kalender visual, notification preferences untuk booking alerts, serta save changes options.

**Teknis & Interaksi:**
Time picker dengan validasi (selesai > mulai), deteksi konflik (waktu tumpang tindih), pembaruan pratinjau real-time, modal konfirmasi untuk perubahan besar, auto-save draft opsional.

***User Flow***:
Terapis → *Availability Settings* → Atur jam kerja → Tambah waktu istirahat → Simpan → Sistem memperbarui ketersediaan *booking* untuk klien

---

#### D. Daftar Klien Terapis (*Therapist Clients List*)

**[GAMBAR 4.49 - *Mockup* Daftar Klien Terapis (*Therapist Clients List*)]**
_Terapis - Tabel semua klien dengan pencarian/filter_

Halaman Clients List menampilkan semua klien yang pernah atau sedang ditangani oleh terapis untuk melihat profil, riwayat sesi, dan mengelola hubungan.

**Komponen Utama:**
Halaman menyajikan page header dengan total clients dan export button, search & filter section komprehensif, clients grid/list dengan card atau tabel layout, quick filters tabs untuk segmentasi klien, client detail modal untuk quick view, bulk actions opsional untuk operasi massal, serta pagination controls.

**Teknis & Interaksi:**
Pencarian dengan debounce, kombinasi filter, urutkan dengan animasi, tampilan cepat modal, tabel/kartu responsif.

***User Flow***:
Terapis → *My Clients* → Cari/filter → Pilih klien → Lihat profil → Ambil tindakan (pesan, lihat riwayat, dll.)

---

#### E. Tampilan Profil Klien (*Client Profile View*) (Perspektif Terapis)

**[GAMBAR 4.50 - *Mockup* Tampilan Profil Klien (*Client Profile View*) (Perspektif Terapis)]**
_Terapis - Profil klien, riwayat, data kemajuan_

Halaman profil klien terperinci yang hanya dapat diakses oleh terapis, berisi informasi komprehensif tentang klien, riwayat sesi, catatan, dan pelacakan kemajuan.

**Komponen Utama:**
Halaman menyajikan profile header dengan avatar dan action buttons, tabs navigation untuk berbagai section, tab overview dengan personal information dan statistics, session history tab dengan daftar semua sesi, notes & observations tab dengan session notes kronologis dan add note form, progress & goals tab dengan tracking metrics, files & documents tab, risk assessment section jika berlaku, serta communication log.

**Teknis & Interaksi:**
Peralihan tab dengan transisi halus, bagian yang dapat ditutup, rich text editor untuk catatan, unggah file dengan pratinjau, cetak profil klien, ekspor data kepatuhan GDPR.

***User Flow***:
Terapis → *My Clients* → Pilih klien → Tampilan profil → Telusuri *tab* → Tambah catatan / Lihat riwayat / Perbarui tujuan

---

#### F. Ruang Sesi (*Session Room*) (Konferensi Video)

**[GAMBAR 4.51 - *Mockup* Ruang Sesi (*Session Room*) (Konferensi Video)]**
_Terapis - Antarmuka panggilan video untuk sesi *online*_

Session Room adalah halaman khusus untuk melakukan sesi terapi online melalui panggilan video, dirancang untuk pengalaman profesional, aman, dan kondusif untuk terapi.

**Komponen Utama:**
Halaman menyajikan video layout dengan multiple view options, control bar dengan audio/video/screen share controls, session timer dengan color indication, session information bar, sidebar chat untuk komunikasi teks, notes panel untuk catatan terapis, virtual background options, network quality indicator, waiting room sebelum sesi dimulai, end session modal dengan feedback, technical issue handling, serta security indicators.

**Teknis & Interaksi:**
Streaming video WebRTC, bitrate adaptif berdasarkan bandwidth, pembatalan gema (echo cancellation)/penekanan kebisingan (noise suppression), auto-focus pada pembicara aktif, keyboard shortcuts (M untuk mute, V untuk video dll), responsif mobile (mode landscape lebih disukai), mode picture-in-picture saat tab diganti.

***User Flow***:
Terapis → Bergabung sesi 5 menit lebih awal → Tes koneksi → Klien bergabung → Mulai sesi → Lakukan terapi → Buat catatan → Akhiri panggilan → Tambah catatan final

---

#### G. Formulir Entri Catatan Sesi (*Session Notes Entry Form*)

**[GAMBAR 4.52 - *Mockup* Formulir Entri Catatan Sesi (*Session Notes Entry Form*)]**
_Terapis - Formulir untuk menulis catatan terapi setelah sesi_

Formulir Session Notes memungkinkan terapis mendokumentasikan observasi, kemajuan, dan rekomendasi setelah (atau selama) sesi terapi untuk kelangsungan perawatan dan dokumentasi hukum.

**Komponen Utama:**
Formulir menyajikan page header dengan identitas klien dan sesi, session information section yang auto-filled, assessment section dengan current state ratings dan observations, session summary mencakup topics/techniques/response, progress notes dengan rich text editor, goals review untuk tracking tujuan klien, homework/action items yang dapat dibagikan, recommendations untuk sesi berikutnya, risk assessment jika berlaku, attachments upload section, visibility settings untuk kontrol akses, save options dengan auto-save, serta templates untuk efisiensi.

**Teknis & Interaksi:**
Auto-save setiap 60 detik, rich text editor dengan pemformatan, sistem template untuk efisiensi, responsif mobile (ramah tablet), opsi suara-ke-teks (pengenalan ucapan), validasi kolom wajib disorot, minimum karakter dipaksa (standar profesional), peringatan "Incomplete note" jika info kritis hilang, pemberitahuan kepatuhan HIPAA/perlindungan data.

***User Flow***:
Setelah sesi → Tambah catatan sesi → Isi semua bagian → Tinjau → Simpan → Catatan disimpan dalam rekam klien

---

#### H. Riwayat Sesi Terapis (*Therapist Session History*)

**[GAMBAR 4.53 - *Mockup* Riwayat Sesi Terapis (*Therapist Session History*)]**
_Terapis - Daftar semua sesi yang selesai dengan catatan_

Halaman Session History menampilkan daftar komprehensif dari semua sesi yang telah dilakukan oleh terapis dengan kemampuan filter dan analitik.

**Komponen Utama:**
Halaman menyajikan page header dengan jumlah total sesi, summary statistics cards untuk metrik utama, search & filter section komprehensif, sort options dropdown, sessions table/list dengan kolom detail lengkap, session detail modal untuk quick view, bulk actions untuk operasi massal, analytics section dengan berbagai grafik, serta export & pagination controls.

**Teknis & Interaksi:**
Filter pencarian real-time, kolom dapat diurutkan, baris yang dapat diperluas untuk tampilan cepat, tampilan detail modal, lazy loading untuk performa, ekspor menghasilkan async.

***User Flow***:
Terapis → *Session History* → Filter/cari sesi → Lihat detail → Ekspor atau analisis data

---

#### I. ***Dashboard*** Penghasilan Terapis (*Therapist Earnings Dashboard*)

**[GAMBAR 4.54 - *Mockup* ***Dashboard*** Penghasilan Terapis (*Therapist Earnings Dashboard*)]**
_Terapis - Grafik pendapatan, riwayat transaksi_

***Dashboard*** Penghasilan memberikan ikhtisar komprehensif tentang pendapatan terapis, riwayat pembayaran, dan manajemen penarikan.

**Komponen Utama:**
Halaman menyajikan page header dengan total lifetime earnings, earnings summary cards untuk balance dan monthly stats, earnings chart dengan grafik timeline interaktif, recent transactions table dengan detail earning per sesi, breakdown section dengan distribusi per layanan, withdrawal history dengan daftar penarikan, request withdrawal section untuk penarikan dana, payment settings untuk metode pembayaran, tax information untuk pelaporan pajak, earnings goals untuk target tracking, serta commission structure info.

**Teknis & Interaksi:**
Pembaruan saldo waktu nyata, interaksi grafik *hover* dan *zoom*, validasi formulir penarikan, notifikasi sukses/error, *email* konfirmasi untuk penarikan, tabel responsif mobile.

***User Flow***:
Terapis → *Earnings* → Lihat saldo → Minta penarikan → Pilih metode → Konfirmasi → Tunggu pemrosesan → Terima pembayaran

---

#### J. Therapist Profile Edit Page

**[GAMBAR 4.55 - *Mockup* Halaman Edit Profil Terapis (*Therapist Profile Edit Page*)]**
_Terapis - Edit bio, kredensial, foto, spesialisasi_

Profile Edit page memungkinkan therapist untuk update informasi professional mereka yang ditampilkan kepada clients.

**Komponen Utama:**
Halaman menyajikan page header dengan preview public profile button, basic information tab dengan photo upload dan personal details, professional information dengan license dan credentials, about me section dengan bio dan therapy approach, education & certifications dengan add/remove entries, services & pricing untuk rate configuration, media & portfolio dengan video intro dan photo gallery, social media & website links, visibility settings untuk profile status, verification status badges, preview mode untuk review changes, serta save section dengan validation.

**Teknis & Interaksi:**
*Draft auto-save* setiap 2 menit, alat pemangkasan gambar *image cropping tool*, *rich text editor* dengan pemformatan, pengurutan ulang *drag & drop*, pembaruan langsung pratinjau *preview live updates*, formulir responsif mobile. Validasi: bidang wajib ditandai *, validasi ukuran/format gambar, batas karakter diberlakukan, verifikasi lisensi diperlukan, pedoman foto profesional.

***User Flow***:
Terapis → Pengaturan Profil → Edit bagian → Unggah media → Pratinjau perubahan → Simpan → Profil diperbarui di direktori publik

---

### 4.3.5.9 *Mockup Admin Dashboard* (Halaman ***Dashboard*** Admin)

***Admin Dashboard*** adalah area khusus untuk administrator sistem yang memiliki akses penuh untuk mengelola pengguna (*manage users*), *booking*, keuangan (*finances*), dan pengaturan sistem (*system settings*). *Interface* dirancang untuk efisiensi dan manajemen data komprehensif.

---

#### A. ***Dashboard*** Admin (Utama) (*Admin Dashboard Main*)

**[GAMBAR 4.56 - *Mockup Admin Dashboard* (Utama)]**
_***Dashboard*** admin - Statistik sistem, grafik, aktivitas terbaru_

***Admin Dashboard*** Utama adalah pusat komando untuk administrator sistem, menyediakan ikhtisar tingkat tinggi dari operasi platform, metrik kunci, dan akses cepat ke fungsi manajemen.

**Komponen Utama:**
Halaman menyajikan top navigation dengan global search dan notifications, sidebar navigation untuk menu admin, key metrics cards untuk total users/active sessions/revenue/platform health, revenue chart dengan grafik timeline, recent bookings table, user growth chart, system alerts panel, top performing therapists leaderboard, top services statistics, quick actions section, activity feed dengan real-time updates, serta platform statistics ringkasan.

**Teknis & Interaksi:**
Pembaruan data waktu nyata *WebSocket*, grafik interaktif klik untuk detail, *dashboard widget* yang dapat disesuaikan, kemampuan ekspor untuk semua data, desain responsif untuk tablet.

***User Flow***:
Login admin → Dashboard → Ikhtisar tingkat tinggi → Identifikasi masalah/tren → Navigasi ke area manajemen spesifik

---

#### B. Manajemen Pengguna Admin (*Admin Users Management*)

**[GAMBAR 4.57 - *Mockup* Manajemen Pengguna Admin]**
_Admin - Tabel semua pengguna (klien, terapis) dengan tindakan CRUD_

Halaman Manajemen Pengguna memungkinkan admin untuk melihat, mencari, memfilter, mengedit, dan mengelola semua pengguna dalam platform (klien, terapis, admin).

**Komponen Utama:**
Halaman menyajikan page header dengan total users dan add/export buttons, tabs navigation untuk filter tipe pengguna, search & filter section komprehensif, users table dengan kolom detail lengkap, bulk actions untuk operasi massal, user actions menu per row, user detail modal untuk quick view dengan tabs, pending therapist applications tab, add/edit user modal, statistics section dengan growth charts, serta export options.

**Teknis & Interaksi:**
Pencarian waktu nyata dengan *debounce*, kolom dapat diurutkan, kombinasi filter, tindakan cepat *modal*, dialog konfirmasi untuk tindakan destruktif, pencatatan aktivitas *activity logging* untuk tindakan admin, paginasi dengan item per halaman yang dapat dikonfigurasi.

***User Flow***:
Admin → Manajemen Pengguna → Filter pengguna → Lihat detail → Ambil tindakan (edit, suspend, approve, dll.)

---

#### C. Manajemen *Booking* Admin (*Admin Bookings Management*)

**[GAMBAR 4.58 - *Mockup* Manajemen *Booking* Admin]**
_Admin - Lihat/edit semua *booking*, ubah status_

Halaman Manajemen *Bookings* memberikan admin kontrol komprehensif atas semua janji temu dalam platform, termasuk pemantauan, modifikasi, dan penyelesaian masalah terkait *booking*.

**Komponen Utama:**
Halaman menyajikan page header dengan total bookings dan date range selector, summary statistics cards untuk berbagai metrik booking, tabs navigation untuk status categories, search & filter section komprehensif, bookings table dengan kolom detail dan color coding, booking actions menu per row, booking detail modal untuk full view, bulk operations untuk multiple bookings, disputed bookings tab untuk issue resolution, calendar view opsional, analytics section dengan booking trends charts, serta export & reports options.

**Teknis & Interaksi:**
Pembaruan waktu nyata *real-time updates* untuk booking baru, pencarian lanjutan *advanced search* dengan *autocomplete*, editing sebaris *inline editing* untuk perubahan cepat, *modal* konfirmasi untuk tindakan kritis, pelacakan perubahan status *status change tracking*, perhitungan refund otomatis, notifikasi email pada tindakan.

***User Flow***:
Admin → Manajemen Bookings → Filter bookings → Lihat detail → Ambil tindakan (reschedule, cancel, refund) → Catat penyelesaian

---

#### D. Laporan Keuangan Admin (*Admin Financial Reports*)

**[GAMBAR 4.59 - *Mockup* Laporan Keuangan Admin]**
_Admin - Grafik pendapatan, laporan transaksi, ekspor data_

Halaman Laporan Keuangan memberikan admin wawasan terperinci tentang pendapatan, pembayaran, penarikan, dan kesehatan keuangan dari platform.

**Komponen Utama:**
Halaman menyajikan page header dengan date range selector dan export button, revenue summary cards untuk total/fees/earnings/outstanding, revenue chart dengan grafik timeline, revenue breakdown by service/session type/payment method, transactions table dengan semua transaksi, withdrawals management untuk therapist payouts, refunds management untuk processing refunds, financial analytics dengan key metrics, tax reports jika berlaku, disputes & chargebacks tracking, payment gateway status monitoring, serta scheduled reports automation.

**Teknis & Interaksi:**
Pembaruan transaksi waktu nyata *real-time transaction updates*, grafik interaktif *drill-down*, ekspor Excel/PDF dengan pemformatan, penanganan data aman *secure data handling*, akses berbasis peran *role-based access* hanya admin senior, pencatatan audit *audit logging* untuk semua tindakan keuangan.

***User Flow***:
Admin → Laporan Keuangan → Pilih periode → Analisis data → Proses penarikan/refund → Buat laporan → Ekspor untuk akuntansi

---

#### E. Pengaturan Sistem Admin (*Admin System Settings*)

**[GAMBAR 4.60 - *Mockup* Pengaturan Sistem Admin]**
_Admin - Konfigurasi parameter sistem, mode pemeliharaan_

Halaman Pengaturan Sistem memungkinkan admin untuk mengonfigurasi pengaturan platform global, mengelola preferensi sistem, dan mengontrol berbagai parameter operasional.

**Komponen Utama:**
Halaman menyajikan page header dengan last modified info dan save button, settings categories sidebar navigation, general settings dengan platform information dan timezone/locale, booking settings dengan rules/cancellation policy/limits, payment settings dengan payment gateway configuration dan pricing/fees, email & notifications dengan SMTP config dan templates editor, security & privacy dengan authentication requirements dan data protection, platform policies dengan rich text editors untuk T&C/Privacy/Guidelines, integrations dengan Google Analytics/Calendar/video conferencing/SMS/social media, advanced settings dengan maintenance mode/performance/API/logging, serta save & apply section dengan validation dan confirmation.

**Teknis & Interaksi:**
*Draft auto-save*, validasi pada *blur*, pratinjau perubahan sebelum terapkan, tombol tes untuk integrasi, *modal* konfirmasi untuk pengaturan kritis, indikator status waktu nyata, formulir responsif. Validasi: Pengaturan kritis memerlukan konfirmasi, backup sebelum perubahan besar, validasi pengaturan sebelum simpan, kemampuan rollback, pencatatan audit *audit logging* untuk semua perubahan.

***User Flow***:
Admin → Pengaturan Sistem → Navigasi ke kategori → Modifikasi pengaturan → Tes jika berlaku → Simpan → Konfirmasi → Pengaturan diterapkan ke seluruh platform

---

### 4.3.5.10 Pendekatan Desain Responsif (*Responsive Design Approach*)

**[GAMBAR 4.61 - Ilustrasi *Breakpoint* Desain Responsif (*Responsive Design Breakpoints Illustration*)]** 📱💻
_Visualisasi *breakpoint*: *mobile* (320-767px), *tablet* (768-1023px), *desktop* (1024px+)_

**[GAMBAR 4.62 - Perbandingan Tata Letak *Mobile* vs *Desktop* (*Mobile vs Desktop Layout Comparison*)]** 📱💻
_Perbandingan berdampingan halaman utama, *dashboard*, dan alur *booking* pada *mobile* vs *desktop*_

**[GAMBAR 4.63 - Panduan Ukuran Target Sentuh (Minimum 44px) (*Touch Target Size Guidelines*)]** 👆
_Ukuran tombol dan elemen interaktif untuk kegunaan *mobile* (sesuai WCAG 2.1)_

**[GAMBAR 4.64 - Fitur Aksesibilitas - Kepatuhan WCAG (*Accessibility Features - WCAG Compliance*)]** ♿
_Rasio kontras warna, navigasi keyboard, dukungan pembaca layar, teks alt_


Dalam pengembangan UI/UX CUR-HEART, pendekatan desain responsif (*responsive design*) diterapkan untuk memastikan aplikasi dapat diakses dan digunakan secara optimal di berbagai perangkat (*desktop*, *tablet*, *mobile*). Berikut adalah strategi dan implementasi desain responsif:

---

**Strategi *Breakpoint* (*Breakpoint Strategy*):**
- ***Mobile Portrait* (Potret Mobile)**: 320px - 575px (iPhone SE, ponsel kecil)
- ***Mobile Landscape* (Lanskap Mobile)**: 576px - 767px
- ***Tablet Portrait* (Potret Tablet)**: 768px - 991px (iPad)
- ***Tablet Landscape* / *Small Desktop* (Lanskap Tablet / Desktop Kecil)**: 992px - 1199px
- ***Desktop***: 1200px - 1439px
- ***Large Desktop* (Desktop Besar)**: 1440px+ (Full HD, 4K)

**Pola Responsif yang Diimplementasikan (*Responsive Patterns Implemented*):**

1. **Adaptasi Navigasi (*Navigation Adaptations*)**:
   - *Desktop*: Navigasi atas horizontal + *sidebar* untuk *dashboard*
   - *Tablet*: *Sidebar* yang dapat dilipat, menu hamburger
   - *Mobile*: Bilah navigasi bawah (*sticky*), laci samping hamburger

2. **Tata Letak *Grid* (*Grid Layouts*)**:
   - *Desktop*: 3-4 kolom untuk kartu/konten
   - *Tablet*: 2-3 kolom
   - *Mobile*: Kolom tunggal, susun vertikal

3. **Skala Tipografi (*Typography Scaling*)**:
   - *Desktop*: H1 (36px), *Body* (16px)
   - *Tablet*: H1 (30px), *Body* (15px)
   - *Mobile*: H1 (24px), *Body* (14px)
   - Tinggi baris menyesuaikan: 1.2x hingga 1.6x untuk keterbacaan

4. **Formulir & Input (*Forms & Inputs*)**:
   - *Desktop*: Formulir multi-kolom, label sebaris
   - *Mobile*: Kolom tunggal, label di atas *input*, target sentuh lebih besar (minimal 44px)

5. **Tabel (*Tables*)**:
   - *Desktop*: Tabel penuh dengan semua kolom
   - *Tablet*: Dapat di-*scroll* horizontal, kolom prioritas terlihat
   - *Mobile*: Tata letak berbasis kartu, susun data vertikal, geser untuk lihat lebih banyak

6. ***Modal* & Dialog**:
   - *Desktop*: *Modal* terpusat dengan *overlay* (lebar maks 600-800px)
   - *Mobile*: *Modal* layar penuh, geser naik dari bawah

7. **Gambar & Media (*Images & Media*)**:
   - Gambar responsif dengan *srcset*
   - *Lazy loading*
   - Rasio aspek dipertahankan
   - Galeri ramah sentuh dengan geser (*swipe*)

8. ***Widget Dashboard***:
   - *Desktop*: *Grid* multi-kolom, seret & lepas (*drag & drop*)
   - *Mobile*: Kolom tunggal, urutan prioritas, bagian yang dapat dilipat

9. **Grafik & Diagram (*Charts & Graphs*)**:
   - Berbasis SVG (dapat diskalakan)
   - Tampilan sederhana pada *mobile*
   - Interaksi ramah sentuh (cubit, *zoom*)

**Optimasi Sentuh & Gestur (*Touch & Gesture Optimization*):**
- Target sentuh minimal: 44x44px (standar Apple HIG)
- Spasi memadai antar elemen interaktif
- Gestur geser: Navigasi *carousel*, geser-untuk-hapus (*swipe-to-delete*)
- Tarik-untuk-muat-ulang (*pull-to-refresh*) pada *mobile*
- Menu konteks tekan-lama (*long-press context menu*)

**Optimasi Kinerja (*Performance Optimization*):**
- Kemampuan Aplikasi Web Progresif (*Progressive Web App* / PWA)
- *Service worker* untuk fungsionalitas *offline*
- Pemisahan kode (*code splitting*) per rute
- Optimasi gambar (format WebP)
- *Lazy loading* komponen non-kritis
- *Script* pihak ketiga minimal

**Strategi Pengujian (*Testing Strategy*):**
- Pengujian perangkat: iPhone (iOS), Samsung/Pixel (Android), iPad, MacBook, laptop Windows
- Kompatibilitas browser: Chrome, Safari, Firefox, Edge
- Pengujian pembaca layar (aksesibilitas)
- Verifikasi target sentuh
- Perubahan orientasi (potret ↔ lanskap)

---

### 4.3.5.11 Pertimbangan Pengalaman Pengguna (UX) (*User Experience Considerations*)

Selain desain visual, pengalaman pengguna secara keseluruhan adalah fokus utama dalam pengembangan CUR-HEART. Berikut adalah pertimbangan UX yang diterapkan:

**1. Prinsip Desain Berpusat pada Pengguna (*User-Centered Design Principles*):**
- **Empati (*Empathy*)**: Memahami keadaan emosional pengguna yang mencari dukungan kesehatan mental
- **Kejelasan (*Clarity*)**: Informasi disajikan secara jelas tanpa jargon medis berlebihan
- **Kesederhanaan (*Simplicity*)**: Alur *booking* yang lugas (hanya 4 langkah)
- **Konsistensi (*Consistency*)**: Pola yang sama di seluruh aplikasi
- **Umpan Balik (*Feedback*)**: Setiap tindakan mendapat respons (status *loading*, pesan sukses/kesalahan)

**2. Aksesibilitas - Kepatuhan WCAG 2.1 AA (*Accessibility - WCAG 2.1 AA Compliance*):**
- **Kontras Warna (*Color Contrast*)**: Minimum 4.5:1 untuk teks isi, 3:1 untuk teks besar
- **Navigasi *Keyboard***: Semua fungsi dapat diakses via *keyboard* (Tab, Enter, Esc)
- **Dukungan Pembaca Layar (*Screen Reader Support*)**: Label ARIA, HTML semantik
- **Indikator Fokus (*Focus Indicators*)**: Jelas dan terlihat untuk pengguna *keyboard*
- **Teks Alternatif (*Alternative Text*)**: Semua gambar memiliki teks alt
- **Keterangan & Transkrip (*Captions & Transcripts*)**: Konten video (jika ada)
- **Teks yang Dapat Diubah Ukurannya (*Resizable Text*)**: Mendukung *zoom* browser hingga 200%

**3. Kinerja & Kecepatan (*Performance & Speed*):**
- **Waktu Muat Halaman (*Page Load Time*)**: Target <3 detik untuk *first contentful paint*
- ***Lazy Loading***: Gambar, komponen dimuat sesuai permintaan
- **Strategi *Caching***: Aset statis di-*cache*, konten dinamis segar
- **Aset yang Dioptimalkan (*Optimized Assets*)**: Gambar terkompresi, CSS/JS diminifikasi
- **Kinerja yang Dirasakan (*Perceived Performance*)**: Layar *skeleton*, pemuatan progresif

**4. Pencegahan & Pemulihan Kesalahan (*Error Prevention & Recovery*):**
- **Validasi Sebaris (*Inline Validation*)**: Umpan balik waktu nyata pada *input* formulir
- **Dialog Konfirmasi (*Confirmation Dialogs*)**: Untuk tindakan destruktif (hapus, batalkan *booking*)
- **Kemampuan Membatalkan (*Undo Capabilities*)**: Jika memungkinkan (penyimpanan *draft*)
- **Pesan Kesalahan yang Jelas (*Clear Error Messages*)**: Panduan spesifik dan dapat ditindaklanjuti
- **Nilai *Default* yang Membantu (*Helpful Defaults*)**: Nilai awal yang masuk akal sudah terisi

**5. Orientasi Pengguna (*User Onboarding*):**
- **Tur Selamat Datang (*Welcome Tour*)**: Pengguna pertama kali dipandu melalui *dashboard* (opsional)
- ***Tooltip***: Bantuan kontekstual saat *hover*/klik
- **Keadaan Kosong (*Empty States*)**: Pesan membantu dengan CTA saat tidak ada data
- **Indikator Kemajuan (*Progress Indicators*)**: Menunjukkan posisi pengguna dalam proses multi-langkah

**6. Indikator Kepercayaan & Keamanan (*Trust & Security Indicators*):**
- **Lencana SSL (*SSL Badge*)**: Pesan "Koneksi aman"
- **Pemberitahuan Privasi (*Privacy Notices*)**: Komunikasi jelas tentang penggunaan data
- **Lencana Terverifikasi (*Verified Badges*)**: Verifikasi lisensi terapis ditampilkan
- **Info Enkripsi (*Encryption Info*)**: "Terenkripsi *end-to-end*" untuk sesi video
- **Citra Profesional (*Professional Imagery*)**: Visual berkualitas tinggi yang membangun kepercayaan

**7. Desain Emosional (*Emotional Design*):**
- **Warna Menenangkan (*Calming Colors*)**: Biru tua & merah muda dipilih untuk efek psikologis menenangkan
- **Nada Ramah (*Friendly Tone*)**: Penulisan naskah yang empatik dan mendukung
- **Perayaan Kesuksesan (*Success Celebrations*)**: Animasi *confetti* setelah *booking* (kegembiraan halus)
- **Pengakuan Kemajuan (*Progress Recognition*)**: Lencana, pencapaian untuk memotivasi klien
- **Sentuhan Manusia (*Human Touch*)**: Foto terapis asli (bukan foto *stock* generik)

**8. Interaksi Mikro (*Micro-interactions*):**
- **Status Tombol (*Button States*)**: Efek *hover*, status aktif, status *disabled*
- **Animasi *Loading***: *Spinner* halus, bilah kemajuan
- **Transisi (*Transitions*)**: *Fade in*, animasi geser (cepat, 200-300ms)
- **Umpan Balik Formulir (*Form Feedback*)**: Tanda centang untuk *input* valid, animasi goyang untuk kesalahan
- ***Notification Toast***: Geser masuk dengan halus, tutup otomatis

**9. Strategi Konten (*Content Strategy*):**
- **Konten yang Dapat Dipindai (*Scannable Content*)**: Judul, poin *bullet*, paragraf pendek
- **Pengungkapan Progresif (*Progressive Disclosure*)**: Tampilkan info penting dulu, detail sesuai permintaan
- **Bahasa Sederhana (*Plain Language*)**: Hindari jargon medis, jelaskan istilah bila perlu
- ***Placeholder* yang Membantu (*Helpful Placeholders*)**: Teks contoh dalam kolom *input*
- **Bantuan Kontekstual (*Contextual Help*)**: Ikon info dengan *tooltip*

**10. Pertimbangan Mengutamakan *Mobile* (*Mobile-First Considerations*):**
- **Ramah Jempol (*Thumb-Friendly*)**: Tindakan penting dalam jangkauan mudah
- ***Input* Minimal (*Minimal Input*)**: Gunakan *picker*, *dropdown* daripada mengetik jika memungkinkan
- **Kemampuan *Offline***: Fungsionalitas dasar saat koneksi hilang
- **Dukungan Orientasi (*Orientation Support*)**: Bekerja dalam mode potret dan lanskap
- **Fitur Asli (*Native Features*)**: Gunakan kemampuan perangkat (kamera, lokasi, notifikasi)

**11. Personalisasi (*Personalization*):**
- **Terapis yang Direkomendasikan (*Recommended Therapists*)**: Berdasarkan preferensi dan riwayat klien
- ***Dashboard* yang Dipersonalisasi**: Tampilkan info relevan per tipe pengguna
- **Preferensi Bahasa (*Language Preferences*)**: Mendukung Indonesia dan Inggris
- **Preferensi Notifikasi (*Notification Preferences*)**: Kontrol granular atas pemberitahuan
- **Preferensi Tersimpan (*Saved Preferences*)**: Ingat pilihan pengguna (tema, *filter*, dll.)

**12. Perbaikan Berkelanjutan (*Continuous Improvement*):**
- **Integrasi Analitik (*Analytics Integration*)**: Lacak perilaku pengguna, identifikasi titik kesulitan
- ***A/B Testing***: Uji variasi untuk mengoptimalkan konversi
- **Mekanisme Umpan Balik Pengguna (*User Feedback Mechanism*)**: Formulir umpan balik dalam aplikasi, survei
- **Pengujian Kegunaan (*Usability Testing*)**: Sesi reguler dengan pengguna nyata
- **Iterasi (*Iteration*)**: Penyempurnaan berkelanjutan berdasarkan data dan umpan balik

---

## 4.3.6 Kesimpulan Desain UI/UX

Desain antarmuka pengguna dan pengalaman pengguna (UI/UX) untuk sistem informasi CUR-HEART telah dikembangkan dengan pendekatan yang komprehensif dan berpusat pada pengguna. Dari 41 halaman *mockup* yang telah didokumentasikan, setiap halaman dirancang dengan mempertimbangkan kebutuhan spesifik dari tiga tipe pengguna utama: klien, terapis, dan administrator.

**Aspek-aspek kunci yang telah dicapai:**

1. **Sistem Desain yang Konsisten (*Consistent Design System*)**: Palet warna (*color palette*), tipografi (*typography*), dan pustaka komponen (*component library*) yang kohesif memastikan pengalaman yang seragam di seluruh aplikasi.

2. **Alur Pengguna yang Intuitif (*Intuitive User Flow*)**: Proses *booking* yang disederhanakan menjadi 4 langkah, navigasi yang jelas, dan struktur informasi yang logis memudahkan pengguna mencapai tujuan mereka.

3. **Desain Responsif (*Responsive Design*)**: *Mockup* dirancang untuk bekerja optimal di *desktop*, *tablet*, dan perangkat *mobile*, dengan adaptasi tata letak yang sesuai untuk setiap *breakpoint*.

4. **Aksesibilitas (*Accessibility*)**: Pertimbangan terhadap pedoman WCAG memastikan aplikasi dapat digunakan oleh pengguna dengan berbagai kemampuan.

5. **Kepercayaan & Keamanan (*Trust & Security*)**: Indikator visual dan pesan yang menekankan keamanan data dan profesionalisme layanan, sangat penting untuk aplikasi kesehatan mental.

6. **Berorientasi pada Kinerja (*Performance-Oriented*)**: Desain yang mempertimbangkan waktu muat (*loading times*), *lazy loading*, dan optimasi aset untuk pengalaman yang responsif.

Dengan sistem desain (*design system*) dan *mockup* yang telah dikembangkan ini, tim pengembangan (*development*) memiliki cetak biru (*blueprint*) yang jelas untuk implementasi *front-end*, memastikan konsistensi visual dan fungsional yang akan menghasilkan pengalaman pengguna (*user experience*) yang sangat baik untuk pengguna CUR-HEART.