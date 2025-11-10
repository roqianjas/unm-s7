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

---

**[GAMBAR 4.15 - Sistem Desain: Palet Warna]** 🔴 **KRITIS**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN DESAIN PALET WARNA]                            │
│                                                             │
│   SISTEM WARNA CUR-HEART                                   │
│   Palet Profesional & Menenangkan                          │
│                                                             │
│   WARNA PRIMER:                                             │
│   ┌──────────┐  ┌──────────┐                               │
│   │Biru Tua  │  │   Merah  │                               │
│   │  (Navy)  │  │   Muda   │                               │
│   │ #1E0E62  │  │ #FF6B7A  │                               │
│   │ █████████│  │ █████████│                               │
│   │ Keperca- │  │ Empati & │                               │
│   │ yaan &   │  │ Kehangat │                               │
│   │ Stabili. │  │   -an    │                               │
│   └──────────┘  └──────────┘                               │
│                                                             │
│   WARNA SEKUNDER:                                           │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐                │
│   │Ungu Muda │  │Merah Muda│  │  Putih   │                │
│   │ #EEEAF9  │  │ #FFE5E8  │  │ #FFFFFF  │                │
│   │ █████████│  │ █████████│  │ █████████│                │
│   └──────────┘  └──────────┘  └──────────┘                │
│                                                             │
│   SKALA ABU-ABU:                                            │
│   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐            │
│   │#333  │ │#666  │ │#999  │ │#CCC  │ │#F5F5 │            │
│   │██████│ │██████│ │██████│ │██████│ │██████│            │
│   │Gelap │ │Sedang│ │Terang│ │Batas │ │Latar │            │
│   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘            │
│                                                             │
│   WARNA SEMANTIK:                                           │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│   │  Sukses  │  │ Peringat │  │  Bahaya  │  │   Info   │  │
│   │ #10B981  │  │ #F59E0B  │  │ #EF4444  │  │ #3B82F6  │  │
│   │ █████████│  │ █████████│  │ █████████│  │ █████████│  │
│   │  Hijau   │  │ Oranye   │  │   Merah  │  │   Biru   │  │
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
│                                                             │
│   CONTOH PENGGUNAAN WARNA:                                  │
│   • Header/Nav: Biru Tua (#1E0E62)                          │
│   • Tombol CTA: Merah Muda (#FF6B7A)                        │
│   • Latar Belakang: Ungu Muda (#EEEAF9), Putih              │
│   • Teks Isi: Abu-abu Gelap (#333333)                       │
│   • Sukses: Hijau (#10B981) - Disetujui, Selesai            │
│   • Peringatan: Oranye (#F59E0B) - Tertunda, Tinjauan       │
│   • Bahaya: Merah (#EF4444) - Kesalahan, Batal, Hapus       │
│                                                             │
│   AKSESIBILITAS:                                            │
│   ✅ Patuh WCAG 2.1 AA                                      │
│   ✅ Rasio Kontras: 4.5:1 minimum untuk teks                │
│   ✅ Kombinasi ramah buta warna                             │
│                                                             │
│   Format: PNG Palet Warna dengan kode heks                 │
│   Ukuran Disarankan: 1600x1200px                           │
│   Gaya: Papan sampel profesional dengan contoh             │
│                                                             │
│   File: assets/images/design-system-color-palette.png      │
│   Alat: Figma, Adobe XD, atau Canva                        │
│                                                             │
│   PRIORITAS: P2 - TINGGI                                    │
│   Harus menampilkan: Semua warna dengan kode heks, contoh  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.15: Palet Warna Sistem Desain CUR-HEART dengan warna primer (Biru Tua, Merah Muda), warna sekunder, skala abu-abu, dan warna semantik yang patuh WCAG AA_

---

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

---

**[GAMBAR 4.16 - Sistem Desain: Sistem Tipografi]** 🔴 **KRITIS**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN SISTEM TIPOGRAFI]                              │
│                                                             │
│   SISTEM TIPOGRAFI CUR-HEART                               │
│   Skala Tipe Modern & Mudah Dibaca                         │
│                                                             │
│   KELUARGA HURUF:                                           │
│                                                             │
│   PRIMER (Judul):                                           │
│   Poppins - Sans-serif                                     │
│   Aa Bb Cc Dd Ee Ff Gg Hh                                  │
│   Bobot: 400 (Reguler), 500 (Medium),                      │
│          600 (SemiBold), 700 (Tebal)                       │
│   Penggunaan: H1-H6, Navigasi, Tombol                      │
│                                                             │
│   SEKUNDER (Isi):                                           │
│   Inter - Sans-serif                                       │
│   Aa Bb Cc Dd Ee Ff Gg Hh                                  │
│   Bobot: 400 (Reguler), 500 (Medium), 600 (SemiBold)       │
│   Penggunaan: Paragraf, Label, Tabel, Formulir             │
│                                                             │
│   SKALA TIPE (Skala Modular 1.25):                         │
│                                                             │
│   H1 - Tampilan Besar                                      │
│   36px / 2.25rem - Tinggi Baris 43px                       │
│   Poppins Tebal (700)                                      │
│   Penggunaan: Judul halaman, judul hero                    │
│                                                             │
│   H2 - Tampilan Sedang                                     │
│   30px / 1.875rem - Tinggi Baris 36px                      │
│   Poppins SemiBold (600)                                   │
│   Penggunaan: Judul bagian                                 │
│                                                             │
│   H3 - Judul Besar                                         │
│   24px / 1.5rem - Tinggi Baris 29px                        │
│   Poppins SemiBold (600)                                   │
│   Penggunaan: Judul subbagian, header kartu                │
│                                                             │
│   H4 - Judul Sedang                                        │
│   20px / 1.25rem - Tinggi Baris 24px                       │
│   Poppins Medium (500)                                     │
│   Penggunaan: Judul komponen                               │
│                                                             │
│   H5 - Judul Kecil                                         │
│   18px / 1.125rem - Tinggi Baris 22px                      │
│   Poppins Medium (500)                                     │
│   Penggunaan: Judul kecil, penekanan                       │
│                                                             │
│   Isi Besar                                                │
│   16px / 1rem - Tinggi Baris 24px (1.5x)                   │
│   Inter Reguler (400)                                      │
│   Penggunaan: Teks isi penting, paragraf intro             │
│                                                             │
│   Isi Reguler                                              │
│   14px / 0.875rem - Tinggi Baris 21px (1.5x)               │
│   Inter Reguler (400)                                      │
│   Penggunaan: Teks isi standar, input formulir             │
│                                                             │
│   Isi Kecil / Keterangan                                   │
│   12px / 0.75rem - Tinggi Baris 18px (1.5x)                │
│   Inter Reguler (400)                                      │
│   Penggunaan: Keterangan, teks pembantu, catatan kaki      │
│                                                             │
│   SPASI & RITME:                                            │
│   • Judul: Tinggi baris 1.2x (ketat)                       │
│   • Isi: Tinggi baris 1.5x (nyaman)                        │
│   • Spasi paragraf: margin bawah 1em                       │
│   • Spasi huruf: -0.02em untuk judul besar                 │
│                                                             │
│   CONTOH:                                                   │
│   [Tampilkan contoh teks dalam setiap ukuran dengan render]│
│                                                             │
│   AKSESIBILITAS:                                            │
│   ✅ Ukuran huruf minimum 12px                              │
│   ✅ Tinggi baris ≥ 1.5 untuk teks isi                      │
│   ✅ Rasio kontras tinggi dipertahankan                     │
│                                                             │
│   Format: PNG Spesimen Tipografi                           │
│   Ukuran Disarankan: 1600x2000px (vertikal)                │
│   Gaya: Papan spesimen tipe dengan contoh                  │
│                                                             │
│   File: assets/images/design-system-typography.png         │
│   Alat: Figma, Adobe XD, atau perangkat lunak desain       │
│                                                             │
│   PRIORITAS: P2 - TINGGI                                    │
│   Harus menampilkan: Contoh huruf, ukuran, bobot, tinggi   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.16: Sistem Tipografi CUR-HEART dengan Poppins (judul) dan Inter (isi), menampilkan skala tipe lengkap dari H1 (36px) hingga Keterangan (12px) dengan tinggi baris dan bobot_

---

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

---

**[GAMBAR 4.17 - Sistem Desain: Pustaka Komponen]** 🔴 **KRITIS**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN PUSTAKA KOMPONEN]                              │
│                                                             │
│   PUSTAKA KOMPONEN CUR-HEART                               │
│   Komponen UI yang Dapat Digunakan Kembali                │
│                                                             │
│   TOMBOL (8 Varian):                                        │
│   ┌────────────────┐  ┌────────────────┐                   │
│   │  Tombol Primer │  │ Tombol Sekund. │                   │
│   │ [Latar Merah M]│  │ [Putih + Biru] │                   │
│   └────────────────┘  └────────────────┘                   │
│   ┌────────────────┐  ┌────────────────┐                   │
│   │ Tombol Outline │  │  Tombol Ghost  │                   │
│   │ [Hanya Batas]  │  │ [Hanya Teks]   │                   │
│   └────────────────┘  └────────────────┘                   │
│   Status: Default, Hover, Aktif, Nonaktif, Loading         │
│                                                             │
│   INPUT FORMULIR (6 Tipe):                                  │
│   • Input Teks (satu baris)                                 │
│   • Textarea (multi baris)                                  │
│   • Dropdown Pilihan                                        │
│   • Kotak Centang                                           │
│   • Tombol Radio                                            │
│   • Pemilih Tanggal/Waktu                                   │
│   Status: Default, Fokus, Error, Sukses, Nonaktif          │
│                                                             │
│   KARTU (4 Varian):                                         │
│   ┌─────────────────────────┐                               │
│   │ Kartu Layanan           │                               │
│   │ [Gambar + Judul + Harga]│                               │
│   └─────────────────────────┘                               │
│   ┌─────────────────────────┐                               │
│   │ Kartu Profil Terapis    │                               │
│   │ [Foto + Bio + Rating]   │                               │
│   └─────────────────────────┘                               │
│   ┌─────────────────────────┐                               │
│   │ Kartu Ringkasan Pesan   │                               │
│   │ [Detail + Status]       │                               │
│   └─────────────────────────┘                               │
│                                                             │
│   NAVIGASI:                                                 │
│   • Bilah Navigasi Atas (desktop)                           │
│   • Menu Hamburger Mobile                                   │
│   • Sidebar (dasbor admin/terapis)                          │
│   • Breadcrumb                                              │
│   • Halaman Berganda                                        │
│                                                             │
│   PERINGATAN & NOTIFIKASI:                                  │
│   • Peringatan Sukses (hijau)                               │
│   • Peringatan Warning (oranye)                             │
│   • Peringatan Error (merah)                                │
│   • Peringatan Info (biru)                                  │
│   • Notifikasi Toast (hilang otomatis)                      │
│                                                             │
│   MODAL & OVERLAY:                                          │
│   • Modal Konfirmasi                                        │
│   • Modal Formulir                                          │
│   • Lightbox Gambar                                         │
│   • Overlay Loading                                         │
│                                                             │
│   TABEL:                                                    │
│   • Tabel Data (dapat diurutkan, disaring)                  │
│   • Tabel Responsif (ramah mobile)                          │
│   • Tabel dengan tindakan                                   │
│                                                             │
│   LENCANA & LABEL:                                          │
│   • Lencana Status (Tertunda, Dikonfirmasi, Selesai, dll.) │
│   • Label Peran (Klien, Terapis, Admin)                     │
│   • Lencana Jumlah (notifikasi, pesan)                      │
│                                                             │
│   KOMPONEN LAIN:                                            │
│   • Avatar (foto pengguna)                                  │
│   • Bintang Rating (1-5 bintang)                            │
│   • Progress Bar                                            │
│   • Tab                                                     │
│   • Akordeon                                                │
│   • Tooltip                                                 │
│   • Skeleton Loader (status loading)                        │
│                                                             │
│   TOTAL KOMPONEN: 30+                                       │
│   Semua komponen:                                           │
│   ✅ Responsif (mobile-first)                               │
│   ✅ Aksesibel (WCAG AA)                                    │
│   ✅ Dapat Digunakan Kembali (prinsip DRY)                  │
│   ✅ Terdokumentasi (panduan penggunaan)                    │
│                                                             │
│   Format: PNG Pustaka Komponen (tata letak grid)           │
│   Ukuran Disarankan: 2400x3000px (besar, detail)           │
│   Gaya: Showcase komponen dengan states & variasi          │
│                                                             │
│   File: assets/images/design-system-components.png         │
│   Alat: Figma, Adobe XD (lebih disukai untuk interaktif)   │
│                                                             │
│   PRIORITAS: P2 - TINGGI                                    │
│   Harus menampilkan: Semua komponen utama dengan variasi   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.17: Pustaka Komponen CUR-HEART dengan 30+ komponen yang dapat digunakan kembali (tombol, formulir, kartu, navigasi, peringatan, modal, tabel, lencana) dengan states dan variasi_

---

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

---

**[GAMBAR 4.18 - Sistem Tata Letak & Grid]** 🔴 **KRITIS**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN SISTEM TATA LETAK & GRID]                      │
│                                                             │
│   SISTEM TATA LETAK CUR-HEART                              │
│   Grid Responsif & Spasi                                   │
│                                                             │
│   SISTEM GRID (12-Kolom):                                   │
│   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐        │
│   │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │        │
│   └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘        │
│                                                             │
│   BREAKPOINT:                                               │
│   • Mobile (xs): < 640px (lebar penuh)                      │
│   • Tablet (sm): ≥ 640px (2 kolom)                          │
│   • Desktop (md): ≥ 768px (3-4 kolom)                       │
│   • Besar (lg): ≥ 1024px (4 kolom)                          │
│   • XL (xl): ≥ 1280px (kontainer lebar maks 1280px)         │
│                                                             │
│   POLA TATA LETAK:                                          │
│                                                             │
│   1. Kolom Tunggal (Mobile):                                │
│   ┌─────────────────────────┐                               │
│   │       Header            │                               │
│   ├─────────────────────────┤                               │
│   │                         │                               │
│   │       Konten            │                               │
│   │    (Lebar Penuh)        │                               │
│   │                         │                               │
│   ├─────────────────────────┤                               │
│   │       Footer            │                               │
│   └─────────────────────────┘                               │
│                                                             │
│   2. Two Column (Tablet):                                   │
│   ┌─────────────────────────┐                               │
│   │       Header            │                               │
│   ├───────────┬─────────────┤                               │
│   │  Sidebar  │   Main      │                               │
│   │  (4 cols) │  (8 cols)   │                               │
│   │           │             │                               │
│   ├───────────┴─────────────┤                               │
│   │       Footer            │                               │
│   └─────────────────────────┘                               │
│                                                             │
│   3. Three Column (Desktop):                                │
│   ┌─────────────────────────────────────┐                   │
│   │          Header (Full)              │                   │
│   ├─────┬───────────────────────┬───────┤                   │
│   │ L.  │       Main            │ Right │                   │
│   │ Bar │     (8 cols)          │ Aside │                   │
│   │(2)  │                       │ (2)   │                   │
│   ├─────┴───────────────────────┴───────┤                   │
│   │          Footer (Full)              │                   │
│   └─────────────────────────────────────┘                   │
│                                                             │
│   SPACING SCALE (8px base):                                 │
│   • 0: 0px                                                  │
│   • 1: 4px  (0.25rem) - Tight spacing                       │
│   • 2: 8px  (0.5rem) - Base unit                            │
│   • 3: 12px (0.75rem)                                       │
│   • 4: 16px (1rem) - Standard spacing                       │
│   • 6: 24px (1.5rem) - Section spacing                      │
│   • 8: 32px (2rem) - Large spacing                          │
│   • 12: 48px (3rem) - Extra large spacing                   │
│   • 16: 64px (4rem) - Hero spacing                          │
│                                                             │
│   CONTAINER WIDTHS:                                         │
│   • Mobile: 100% (with 16px padding)                        │
│   • Tablet: 640px max                                       │
│   • Desktop: 1024px max                                     │
│   • Large: 1280px max (standard)                            │
│                                                             │
│   COMMON LAYOUTS:                                           │
│   • Landing Page: Hero + Features Grid (3 cols)             │
│   • Services Page: Card Grid (3 cols desktop, 1 mobile)     │
│   • Dashboard: Sidebar + Main Content                       │
│   • Form Pages: Centered form (max 600px width)             │
│   • Detail Pages: 2/3 main + 1/3 sidebar                    │
│                                                             │
│   Format: Layout System Diagram PNG                         │
│   Recommended size: 2000x1600px                            │
│   Style: Wireframe-style dengan grid overlay               │
│                                                             │
│   File: assets/images/design-system-layout-grid.png        │
│   Tool: Figma, Adobe XD, atau wireframing tool             │
│                                                             │
│   PRIORITY: P2 - HIGH                                       │
│   Must show: Grid system, breakpoints, layout patterns     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.18: Layout & Grid System CUR-HEART dengan 12-column grid, 5 breakpoints responsive, spacing scale (8px base), dan common layout patterns_

---

**[GAMBAR 4.19 - Iconography System]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT ICONOGRAPHY SYSTEM]                              │
│                                                             │
│   CUR-HEART ICON LIBRARY                                   │
│   Consistent Visual Language                               │
│                                                             │
│   ICON STYLE:                                               │
│   • Style: Outline (stroke-based)                           │
│   • Stroke Width: 2px                                       │
│   • Corner Radius: 2px (rounded)                            │
│   • Grid: 24x24px base                                      │
│   • Format: SVG (scalable, crisp)                           │
│                                                             │
│   ICON SIZES:                                               │
│   • XS: 16x16px - Inline text icons                         │
│   • SM: 20x20px - Button icons                              │
│   • MD: 24x24px - Standard (default)                        │
│   • LG: 32x32px - Feature icons                             │
│   • XL: 48x48px - Hero/empty state icons                    │
│                                                             │
│   ICON CATEGORIES (100+ icons):                             │
│                                                             │
│   NAVIGATION (12 icons):                                    │
│   🏠 Home  📋 Dashboard  👤 Profile  ⚙️ Settings            │
│   📅 Calendar  💬 Messages  🔔 Notifications  📊 Reports    │
│   ❓ Help  🚪 Logout  ◀️ Back  ☰ Menu                       │
│                                                             │
│   BOOKING & SERVICES (15 icons):                            │
│   📝 Book  ✅ Confirm  ❌ Cancel  🔄 Reschedule              │
│   🧘 Therapy  💆 Session  🕐 Time  📍 Location              │
│   💰 Payment  💳 Card  🏦 Bank  📄 Receipt                  │
│   ⏱️ Duration  🎯 Service  📞 Contact                       │
│                                                             │
│   USER & PROFILE (10 icons):                                │
│   👤 User  👥 Users  ⭐ Rating  💬 Review                   │
│   📧 Email  📱 Phone  🎂 Birthday  🏥 Medical               │
│   🔐 Security  ✏️ Edit                                      │
│                                                             │
│   STATUS & ACTIONS (15 icons):                              │
│   ✅ Success  ⚠️ Warning  ❌ Error  ℹ️ Info                 │
│   ⏳ Pending  ⏸️ Paused  ▶️ Active  ⏹️ Stopped              │
│   ➕ Add  ➖ Remove  🗑️ Delete  💾 Save                     │
│   📤 Upload  📥 Download  🔍 Search                         │
│                                                             │
│   MEDIA & CONTENT (8 icons):                                │
│   📸 Camera  🎥 Video  🖼️ Image  📂 Folder                  │
│   📄 Document  📊 Chart  📈 Graph  🎨 Design                │
│                                                             │
│   THERAPY SPECIFIC (10 icons):                              │
│   🧠 Mental Health  💭 Thought  😌 Calm  🎯 Focus           │
│   💪 Strength  ❤️ Heart  🌟 Star  ✨ Magic                 │
│   🌈 Progress  🎭 Emotion                                   │
│                                                             │
│   SOCIAL (5 icons):                                         │
│   👍 Like  💬 Comment  📢 Share  🔔 Bell                    │
│   ⚡ Trending                                               │
│                                                             │
│   ICON USAGE GUIDELINES:                                    │
│   • Always pair with text labels (accessibility)            │
│   • Use consistent size within same context                 │
│   • Maintain 2px stroke width for consistency               │
│   • Color: Inherit from parent or use semantic colors       │
│   • Align center with text baseline                         │
│                                                             │
│   ICON LIBRARY:                                             │
│   Primary: Heroicons v2 (Tailwind UI official)             │
│   Secondary: Font Awesome (for additional needs)            │
│   Custom: Therapy-specific icons (10 custom)                │
│                                                             │
│   Format: Icon Library PNG (grid showcase)                 │
│   Recommended size: 2400x2000px                            │
│   Style: Icon grid dengan labels dan sizes                 │
│                                                             │
│   File: assets/images/design-system-iconography.png        │
│   Tool: Figma, Adobe Illustrator, atau icon editor         │
│                                                             │
│   PRIORITY: P2 - HIGH                                       │
│   Must show: All icon categories, sizes, usage examples    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.19: Sistem Ikonografi CUR-HEART dengan 100+ ikon *outline*, 5 ukuran (16-48px), diorganisir berdasarkan kategori (Navigasi, *Booking*, Pengguna, Status, Media, Khusus Terapi, Sosial)_

---

### 4.3.5.4 *Mockup* Halaman Publik (*Public Pages*)

Halaman publik (*public pages*) adalah halaman-halaman yang dapat diakses oleh semua pengunjung tanpa perlu *login* terlebih dahulu. Halaman-halaman ini berfungsi sebagai situs web yang menghadap ke publik (*front-facing website*) yang memberikan informasi tentang CUR-HEART, layanan yang ditawarkan, dan mendorong pengunjung untuk melakukan *booking* atau registrasi.

---

**[GAMBAR 4.20 - *Mockup* Halaman Utama (*Landing Page*/Homepage)]** 📱
_Halaman publik - Bagian *hero*, ringkasan layanan, terapis, testimoni_

**[GAMBAR 4.21 - *Mockup* Halaman Tentang Kami (*About Us Page*)]** 📱
_Halaman publik - Cerita perusahaan, nilai, tim, sertifikasi_

**[GAMBAR 4.22 - *Mockup* Halaman Katalog Layanan (*Services Catalog Page*)]** 📱
_Halaman publik - *Grid* 6 layanan dengan harga dan deskripsi_

**[GAMBAR 4.23 - *Mockup* Halaman Detail Layanan (*Service Detail Page*)]** 📱
_Halaman publik - Informasi layanan detail, manfaat, CTA *booking*_

**[GAMBAR 4.24 - *Mockup* Halaman Direktori Terapis (*Therapists Directory Page*)]** 📱
_Halaman publik - *Grid* profil terapis dengan *filter*/*search*_

**[GAMBAR 4.25 - *Mockup* Halaman Profil Terapis (*Therapist Profile Page*)]** 📱
_Halaman publik - Bio, kredensial, spesialisasi, ulasan, *booking*_

**[GAMBAR 4.26 - *Mockup* Halaman Daftar Blog (*Blog List Page*)]** 📱
_Halaman publik - Daftar artikel blog dengan pencarian dan *filter*_

**[GAMBAR 4.27 - *Mockup* Halaman Detail Blog (*Blog Detail Page*)]** 📱
_Halaman publik - Artikel blog lengkap dengan pos terkait_

**[GAMBAR 4.28 - *Mockup* Halaman Hubungi Kami (*Contact Us Page*)]** 📱
_Halaman publik - Formulir kontak, peta lokasi, tautan media sosial_

**[GAMBAR 4.29 - *Mockup* Halaman FAQ (*FAQ Page*)]** 📱
_Halaman publik - Pertanyaan yang Sering Diajukan dengan *accordion*_

**[GAMBAR 4.30 - *Mockup* Halaman Kebijakan Privasi (*Privacy Policy Page*)]** 📱
_Halaman publik - Kebijakan privasi dan informasi perlindungan data_

**[GAMBAR 4.31 - *Mockup* Halaman Syarat dan Ketentuan (*Terms & Conditions Page*)]** 📱
_Halaman publik - Syarat layanan dan kondisi penggunaan_

---

#### A. Halaman Utama (*Landing Page* / Homepage)

**Deskripsi:**
Halaman utama (*landing page*) adalah halaman pertama yang dilihat pengunjung ketika mengakses situs web CUR-HEART. Halaman ini dirancang untuk memberikan kesan pertama yang kuat, profesional, dan menenangkan sesuai dengan sifat bisnis hipnoterapi dan kesehatan mental.

**Elemen Utama:**
1. **Bagian *Hero* (*Hero Section*)**:
   - Latar belakang gradien biru tua ke ungu yang menenangkan
   - Judul utama (*headline*): "Transform Your Life Through Professional Hypnotherapy"
   - Subjudul menjelaskan proposisi nilai (*value proposition*) CUR-HEART
   - Tombol CTA primer "Book Your Session" (merah muda, menonjol)
   - Tombol CTA sekunder "Learn More About Us"
   - Ilustrasi/*hero image* terapis yang profesional dan ramah

2. **Bagian Ringkasan Layanan (*Services Overview Section*)**:
   - Tata letak *grid* 3 kolom (*desktop*) untuk menyorot 3 layanan utama
   - Setiap kartu layanan dengan ikon, judul, deskripsi singkat
   - Tautan "View All Services" di bawah

3. **Bagian Mengapa Memilih Kami (*Why Choose Us Section*)**:
   - 4 poin penjualan unik (*unique selling points*) dengan ikon dan deskripsi:
     * Terapis Profesional Bersertifikat (*Certified Professional Therapists*)
     * Metode Hipnoterapi Terbukti (*Proven Hypnotherapy Methods*)
     * Sesi Nyaman & Privat (*Comfortable & Private Sessions*)
     * Opsi *Online* & *Offline* yang Fleksibel (*Flexible Online & Offline Options*)
   - Latar belakang dengan ungu muda untuk diferensiasi

4. **Bagian Terapis Unggulan (*Featured Therapists Section*)**:
   - *Carousel*/*slider* dengan 4 kartu terapis
   - Foto, nama, spesialisasi, tahun pengalaman
   - Bintang rating
   - Tombol "View Profile"
   - CTA "See All Therapists"

5. **Bagian Cara Kerja (*How It Works Section*)**:
   - Proses 4 langkah dengan penomoran visual:
     1. Jelajah & Pilih Layanan (*Browse & Choose Service*)
     2. Pilih Terapis Anda (*Select Your Therapist*)
     3. *Booking* Sesi Anda (*Book Your Session*)
     4. Mulai Transformasi Anda (*Start Your Transformation*)
   - Visual *timeline* dengan garis penghubung
   - Ikon untuk setiap langkah

6. **Bagian Testimoni (*Testimonials Section*)**:
   - 3 kartu testimoni pelanggan dengan:
     * Foto/*avatar* klien
     * Nama & usia klien
     * Bintang rating (5/5)
     * Teks testimoni (2-3 kalimat)
   - Navigasi *carousel* untuk testimoni lebih banyak

7. **Pos Blog Terbaru (*Latest Blog Posts*)**:
   - 3 pos blog terbaru dalam format kartu
   - Gambar mini (*thumbnail*), judul, kutipan, tanggal
   - Tautan "Read More"
   - Tombol "View All Articles"

8. **Bagian *Footer* CTA (*Call-to-Action Footer Section*)**:
   - *Banner* besar dengan latar belakang gradien merah muda
   - "Ready to Start Your Journey?"
   - Tombol "Book Your First Session Today"
   - "Or contact us for consultation" sebagai alternatif

**Interaksi & Perilaku:**
- Animasi *scroll* yang halus saat navigasi antar bagian
- Efek *hover* pada kartu dan tombol
- *Lazy loading* untuk gambar
- Responsif: Susun bagian secara vertikal pada *mobile*
- Bilah navigasi tetap (*sticky*/*fixed*) saat *scroll*

***User Flow***:
Pengunjung → Halaman utama → Tertarik → Klik "Book Your Session" → Diarahkan ke halaman Layanan (atau *login* jika sudah punya akun)

---

#### B. Halaman Tentang Kami (*About Us Page*)

**Deskripsi:**
Halaman Tentang Kami (*About Us page*) menjelaskan tentang CUR-HEART sebagai organisasi, visi misi, nilai-nilai yang dipegang, dan tim di balik layanan ini. Halaman ini membangun kepercayaan dan kredibilitas.

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Judul "About CUR-HEART"
   - *Breadcrumb*: Home > About Us
   - *Hero image*: Tim terapis atau kantor CUR-HEART

2. **Bagian Cerita Kami (*Our Story Section*)**:
   - Paragraf 3-4 tentang sejarah pendirian CUR-HEART
   - Motivasi pendiri (*founder*) dalam bidang hipnoterapi
   - Pencapaian penting (*milestone achievements*) (tahun berdiri, jumlah klien, tingkat kesuksesan)

3. **Visi & Misi (*Vision & Mission*)**:
   - Dua kolom berdampingan (*side-by-side*)
   - Visi di kiri dengan ikon
   - Misi di kanan dengan ikon
   - Latar belakang kartu dengan bayangan halus

4. **Nilai-Nilai Kami (*Our Values*)**:
   - 5 nilai inti (*core values*) dalam tata letak *grid*:
     * Profesionalisme (*Professionalism*)
     * Kerahasiaan (*Confidentiality*)
     * Empati (*Empathy*)
     * Keunggulan (*Excellence*)
     * Inovasi (*Innovation*)
   - Setiap nilai dengan ikon dan deskripsi

5. **Bagian Tim Kami (*Our Team Section*)**:
   - *Grid* 3-4 kolom kartu anggota tim
   - Foto profesional, nama, posisi, bio singkat
   - Tautan media sosial (LinkedIn, Instagram)
   - Dipisahkan per departemen: Manajemen, Terapis, Staf Pendukung

6. **Sertifikasi & Kemitraan (*Certifications & Partnerships*)**:
   - Logo-logo sertifikasi profesional
   - Organisasi mitra (jika ada)
   - Penghargaan & pengakuan (*awards & recognitions*)

7. **Bagian CTA**:
   - Tombol "Meet Our Therapists"
   - Tombol "Contact Us for More Info"

**Interaksi & Perilaku:**
- Animasi *fade-in* untuk bagian saat *scroll*
- Efek *hover* pada kartu anggota tim (tampilkan tautan sosial)
- *Grid* responsif yang menyesuaikan berdasarkan ukuran layar

***User Flow***:
Pengunjung ingin tahu lebih tentang CUR-HEART → Halaman Tentang Kami → Baca informasi → Membangun kepercayaan → Klik "Meet Our Therapists" atau "Book Session"

---

#### C. Halaman Layanan (*Services Page* / Katalog Layanan)

**Deskripsi:**
Halaman Layanan (*Services page*) menampilkan katalog lengkap semua layanan hipnoterapi yang ditawarkan oleh CUR-HEART. Halaman ini membantu calon klien memahami berbagai opsi layanan dan memilih yang sesuai dengan kebutuhan mereka.

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Judul "Our Services"
   - Subjudul "Professional Hypnotherapy for Your Wellness"
   - *Breadcrumb*: Home > Services

2. **Bagian *Filter* & Pencarian (*Filter & Search Section*)**:
   - Bilah pencarian (*search bar*) untuk cari layanan berdasarkan kata kunci
   - *Dropdown filter*:
     * Berdasarkan Kategori (Manajemen Stres, Adiksi, Fobia, dll.)
     * Berdasarkan Durasi (30 menit, 60 menit, 90 menit)
     * Berdasarkan Rentang Harga (*slider*)
   - Opsi pengurutan (*sort*) (Populer, Harga Rendah-Tinggi, Harga Tinggi-Rendah, Nama A-Z)

3. ***Services Grid* (Grid Layanan)**:
   - Tata letak berbasis kartu, 3 kolom *desktop*, 2 *tablet*, 1 *mobile*
   - Setiap kartu layanan berisi:
     * Gambar mini/*icon* layanan dengan latar belakang berwarna
     * Nama layanan (tebal)
     * Lencana kategori (*category badge*)
     * Deskripsi singkat (2-3 baris)
     * Durasi (mis., "60 menit")
     * Harga (mis., "Rp 300.000")
     * Rating (bintang + jumlah ulasan)
     * Tombol "View Details"

4. **Kategori Layanan (*Service Categories*)**:
   - Total 8-10 layanan ditampilkan:
     1. Manajemen Stres & Kecemasan (*Stress & Anxiety Management*)
     2. Manajemen Berat Badan (*Weight Management*)
     3. Berhenti Merokok (*Smoking Cessation*)
     4. Perawatan Fobia (*Phobia Treatment*)
     5. Gangguan Tidur (*Sleep Disorders*)
     6. Membangun Kepercayaan Diri (*Confidence Building*)
     7. Manajemen Nyeri (*Pain Management*)
     8. Penyembuhan Trauma (*Trauma Healing*)
     9. Peningkatan Kinerja (*Performance Enhancement*)
     10. Konseling Hubungan (*Relationship Counseling*)

5. **Paginasi (*Pagination*)**:
   - Navigasi untuk beberapa halaman jika layanan > 12
   - Tombol "Load More" sebagai alternatif

6. ***CTA Banner***:
   - "Not sure which service is right for you?"
   - Tombol "Take our Free Assessment"
   - Tautan "Or chat with our consultant"

**Interaksi & Perilaku:**
- Pemfilteran pencarian instan (*instant search filtering*) saat mengetik
- Animasi halus saat *filter* diterapkan
- Efek *hover* pada kartu layanan (*scale up*, peningkatan bayangan)
- *Skeleton loading* saat data di-*fetch*

***User Flow***:
Pengunjung → Halaman Layanan → Jelajah/*filter* layanan → Klik "View Details" pada layanan yang menarik → Halaman Detail Layanan

---

#### D. Halaman Detail Layanan (*Service Detail Page*)

**Deskripsi:**
Halaman Detail Layanan (*Service Detail page*) memberikan informasi lengkap dan mendalam tentang satu layanan hipnoterapi spesifik. Halaman ini bertujuan untuk mengedukasi calon klien dan mendorong mereka untuk melakukan *booking*.

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Nama layanan (H1)
   - *Breadcrumb*: Home > Services > [Nama Layanan]
   - *Hero image*/ilustrasi relevan dengan layanan

2. **Bagian Ringkasan (*Overview Section*)**:
   - Ikon/*image* besar untuk layanan
   - Harga, durasi, kategori
   - Rating & jumlah ulasan
   - Tombol primer "Book This Session" (merah muda, menonjol)
   - Fakta singkat (*quick facts*):
     * Format sesi (*session format*) (*Online*/*Offline*/Keduanya)
     * Bahasa yang tersedia
     * Jumlah sesi tipikal (mis., "3-5 sesi direkomendasikan")

3. **Bagian Tab Deskripsi (*Description Tab Section*)**:
   - Navigasi *tabs*: Overview | What to Expect | Benefits | FAQ
   - ***Overview Tab***:
     * Penjelasan detail tentang layanan (3-4 paragraf)
     * Siapa yang cocok untuk layanan ini
     * Kondisi yang dapat diatasi
   - ***What to Expect Tab***:
     * Proses sesi langkah demi langkah (*step-by-step*)
     * Persiapan yang perlu dilakukan
     * Apa yang terjadi selama dan setelah sesi
   - ***Benefits Tab***:
     * Daftar *bullet* manfaat yang akan didapat
     * *Timeline* hasil yang diharapkan
     * Statistik kisah sukses (*success stories statistics*)
   - ***FAQ Tab***:
     * 5-7 pertanyaan yang sering diajukan dengan jawaban
     * Format *accordion* yang dapat dilipat

4. **Terapis yang Direkomendasikan (*Recommended Therapists*)**:
   - "Our Therapists Specialized in This Service"
   - 3-4 kartu terapis dengan:
     * Foto, nama, tahun pengalaman
     * Persentase kecocokan spesialisasi
     * Pratinjau slot waktu tersedia
     * Tombol "View Profile" dan "Book Now"

5. **Layanan Terkait (*Related Services*)**:
   - "You Might Also Like"
   - 3 layanan terkait dalam format kartu
   - Kategori serupa atau layanan pelengkap

6. **Ulasan Pelanggan (*Customer Reviews*)**:
   - Rating keseluruhan (4.8/5.0) dengan visualisasi bintang
   - Diagram batang rincian rating (*rating breakdown bar chart*) (5★: 75%, 4★: 20%, dll)
   - Kartu ulasan dari klien:
     * Nama klien (atau anonim) + foto
     * Bintang rating
     * Teks ulasan
     * Tanggal
     * Lencana terverifikasi (*verified badge*)
   - Tombol "Write a Review" (untuk pengguna yang sudah *login*)

7. ***Sticky CTA Sidebar*** (*desktop*) atau *Bottom Bar* (*mobile*):
   - Harga
   - Tombol "Book Now"
   - Ikon "Add to Wishlist"
   - Ikon "Share"

**Interaksi & Perilaku:**
- *Sticky booking* CTA saat *scroll*
- Pergantian *tabs* dengan transisi halus
- Animasi *accordion* untuk FAQ
- *Lazy load reviews* (*infinite scroll* atau paginasi)
- *Modal popup* saat klik "Book Now" untuk pilih terapis

***User Flow***:
Pengguna sudah di Halaman Detail Layanan → Baca informasi lengkap → Yakin → Klik "Book Now" → Pilih terapis (*modal*/*redirect*) → Alur *booking*

---

#### E. Halaman Direktori Terapis (*Therapists Directory Page*)

**Deskripsi:**
Halaman Direktori Terapis (*Therapists Directory page*) menampilkan daftar semua terapis yang tersedia di CUR-HEART. Calon klien dapat menjelajah, mem-*filter*, dan memilih terapis yang sesuai dengan preferensi mereka.

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Judul "Our Professional Therapists"
   - Subjudul "Meet our certified and experienced hypnotherapists"
   - *Breadcrumb*: Home > Therapists
   - *Hero image*: Foto grup terapis atau ilustrasi abstrak

2. **Bagian Pencarian & *Filter* (*Search & Filter Section*)**:
   - Bilah pencarian "Search by name or specialization"
   - Opsi *filter*:
     * Berdasarkan Spesialisasi (*dropdown multi-select*)
     * Berdasarkan Pengalaman (0-2 tahun, 3-5, 5-10, 10+ tahun)
     * Berdasarkan Rating (4+ bintang, 4.5+, hanya 5)
     * Berdasarkan Ketersediaan (Tersedia Hari Ini, Minggu Ini)
     * Berdasarkan Bahasa (Indonesia, Inggris, dll.)
     * Berdasarkan Jenis Kelamin (Laki-laki, Perempuan, Semua)
   - Tombol "Apply Filters"
   - *Filter* aktif ditampilkan sebagai pil yang dapat dihapus

3. **Opsi Pengurutan (*Sort Options*)**:
   - *Dropdown*: Rating Tertinggi, Paling Berpengalaman, Paling Banyak Di-*booking*, Nama A-Z

4. ***Therapists Grid* (Grid Terapis)**:
   - Tata letak kartu, 3 kolom *desktop*
   - Setiap kartu terapis:
     * Foto profesional (bulat atau persegi dengan sudut membulat)
     * Nama (H4)
     * Gelar/Posisi (mis., "Hipnoterapis Senior")
     * Spesialisasi (2-3 lencana)
     * Tahun pengalaman
     * Bintang rating + jumlah ulasan
     * Bahasa yang dikuasai
     * Indikator ketersediaan (Tersedia Sekarang/titik hijau)
     * Rentang harga (mis., "Rp 250K - 400K")
     * Tombol "View Profile"
     * Tombol "Book Session" (primer)
   - Efek *hover*: Bayangan kartu naik, tombol muncul

5. **Jumlah Total (*Total Count*)**:
   - "Showing 12 of 25 therapists" dengan paginasi

6. ***Featured Therapists Banner***:
   - Bagian khusus untuk menyorot 2-3 terapis dengan rating tertinggi
   - Kartu lebih besar dengan lebih banyak info
   - Lencana "Therapist of the Month"

7. **Bagian CTA**:
   - "Can't decide? Let us help you"
   - Tombol "Get Therapist Recommendation"
   - Tautan "Or browse by specialty"

**Interaksi & Perilaku:**
- Pemfilteran pencarian waktu nyata (*real-time*)
- Hasil *filter* diperbarui dengan *skeleton loading*
- *Infinite scroll* atau paginasi
- *Bookmark*/*favorite* terapis (jika sudah *login*)
- *Quick view modal* saat *hover* (opsional)

***User Flow***:
Pengguna → Direktori Terapis → Terapkan *filter* → Jelajah kartu → Tertarik pada satu → Klik "View Profile" → Halaman Profil Terapis

---

#### F. Halaman Profil Terapis (*Therapist Profile Page*)

**Deskripsi:**
Halaman Profil Terapis (*Therapist Profile page*) menampilkan informasi detail tentang seorang terapis, termasuk latar belakang, keahlian, ulasan, dan ketersediaan. Ini adalah halaman pengambilan keputusan (*decision-making*) sebelum *booking*.

**Elemen Utama:**
1. **Bagian *Hero* (*Hero Section*)**:
   - Foto profesional besar (kiri)
   - Nama (H1)
   - Kredensial & gelar
   - Lencana spesialisasi
   - Bintang rating + total ulasan
   - Tahun pengalaman
   - Bahasa yang dikuasai
   - Tombol primer "Book Session" (menonjol)
   - Tombol sekunder "Send Message"
   - Tombol ikon "Add to Favorite"

2. **Statistik Cepat (*Quick Stats*)**:
   - Total sesi selesai
   - Persentase tingkat kesuksesan
   - Waktu respons (mis., "Biasanya merespons dalam 2 jam")
   - Ketersediaan (Tersedia Minggu Ini)

3. **Bagian Tentang Saya (*About Me Section*)**:
   - Paragraf bio (3-4 paragraf) tentang:
     * Latar belakang pendidikan
     * Pengalaman profesional
     * Pendekatan terhadap terapi
     * Filosofi pribadi

4. **Spesialisasi & Keahlian (*Specializations & Expertise*)**:
   - Daftar layanan/kondisi yang menjadi spesialisasi
   - *Progress bar* menunjukkan tingkat kemahiran
   - Sertifikasi dengan lencana/ikon

5. **Pendidikan & Sertifikasi (*Education & Certifications*)**:
   - Format *timeline*:
     * Gelar, universitas, tahun
     * Sertifikasi, badan penerbit, tahun
     * Pendidikan berkelanjutan

6. **Pendekatan Konsultasi (*Consultation Approach*)**:
   - Penjelasan metodologi terapi
   - Apa yang membuat pendekatan mereka unik
   - Gaya terapi (*gentle*, *direct*, *holistic*, dll.)

7. **Layanan yang Ditawarkan & Harga (*Services Offered & Pricing*)**:
   - Tabel dengan kolom: Nama Layanan, Durasi, Harga
   - 5-8 layanan yang ditawarkan
   - Tombol "Book" per layanan

8. **Kalender Ketersediaan (*Availability Calendar*)**:
   - Tampilan kalender mingguan (7 hari ke depan)
   - Slot waktu ditampilkan dengan status:
     * Tersedia (hijau)
     * Di-*booking* (abu-abu)
     * Istirahat (garis)
   - "View More Dates" untuk memperluas
   - *Quick book*: Klik slot waktu → *Modal booking*

9. **Ulasan & Testimoni Klien (*Client Reviews & Testimonials*)**:
   - Rating keseluruhan dengan visual bintang
   - Jumlah total ulasan
   - Distribusi rating (5★: 80%, 4★: 15%, dll.)
   - Kartu ulasan:
     * Inisial/*avatar* klien
     * Bintang rating
     * Layanan yang diambil
     * Teks ulasan
     * Tanggal
     * Jumlah suara "Helpful"
   - Paginasi untuk ulasan lebih banyak
   - *Filter* ulasan berdasarkan rating atau layanan

10. **Pengenalan Video (*Video Introduction*)** (opsional):
    - Video *embedded* di mana terapis memperkenalkan diri
    - Overlay tombol putar

11. **FAQ**:
    - Pertanyaan yang sering diajukan khusus untuk terapis ini
    - *Accordion* yang dapat dilipat

12. **Terapis Terkait (*Related Therapists*)**:
    - "Other Therapists You Might Like"
    - 3 kartu terapis serupa (spesialisasi sama)

13. ***Sticky Booking Sidebar*** (*desktop*):
    - Kartu profil mini
    - Harga mulai dari
    - Slot tersedia berikutnya
    - Tombol "Book Now"
    - Tombol "Message"

**Interaksi & Perilaku:**
- *Sticky booking sidebar* saat *scroll*
- Kalender interaktif, klik slot langsung *book*
- Ulasan *loadmore*/*infinite scroll*
- Putar video dengan *lightbox*
- *Smooth scroll* ke bagian via navigasi

***User Flow***:
Pengguna di Profil Terapis → Terkesan dengan kredensial → Cek ketersediaan → Klik slot waktu tersedia → *Modal booking* terbuka → Lanjutkan alur *booking*

---

#### G. Halaman Daftar Blog (*Blog List Page*)

**Deskripsi:**
Halaman Daftar Blog (*Blog List page*) menampilkan artikel-artikel edukatif tentang hipnoterapi, kesehatan mental, tips kesejahteraan, dan cerita sukses. Ini adalah pemasaran konten (*content marketing*) untuk SEO dan kepemimpinan pemikiran (*thought leadership*).

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Judul "CUR-HEART Blog"
   - Subjudul "Insights, Tips, and Stories About Mental Wellness"
   - *Breadcrumb*: Home > Blog

2. **Pos Unggulan (*Featured Post*)**:
   - Kartu besar untuk artikel terbaru/unggulan
   - Gambar mini (*thumbnail*) besar
   - Lencana kategori
   - Judul (H2)
   - Kutipan (2-3 kalimat)
   - Penulis, tanggal, waktu baca
   - Tombol "Read More"

3. **Pencarian & *Filter***:
   - Bilah pencarian "Search articles..."
   - *Filter* kategori: Semua, Hipnoterapi, Kesehatan Mental, Kisah Sukses, Tips & Trik, Riset, Berita
   - Awan *tag* (*tag cloud*) (tag populer)

4. ***Grid* Pos Blog (*Blog Posts Grid*)**:
   - Tata letak 2-3 kolom
   - Setiap kartu blog:
     * Gambar mini (*thumbnail*) (rasio aspek 16:9)
     * Lencana kategori
     * Judul (H3)
     * Kutipan (2 baris, dipotong)
     * *Avatar* + nama penulis
     * Tanggal publikasi
     * Waktu baca (mis., "5 min read")
     * Tautan "Read More"

5. ***Sidebar*** (*desktop* saja):
   - Widget pencarian
   - Daftar kategori dengan jumlah pos
   - Pos populer/terbaru (5 item):
     * Gambar mini kecil
     * Judul
     * Tanggal
   - Formulir langganan *newsletter*:
     * Input email
     * Tombol "Subscribe"
   - Tombol ikuti media sosial
   - Awan *tag*

6. **Paginasi (*Pagination*)**:
   - "Previous" | Nomor halaman | "Next"
   - Atau tombol "Load More"

7. **Bagian CTA *Newsletter***:
   - "Get Wellness Tips in Your Inbox"
   - Formulir langganan email
   - Tombol "Subscribe Now"

**Interaksi & Perilaku:**
- Pencarian dengan *debounce* untuk pemfilteran instan
- *Filter* kategori dengan transisi halus
- *Skeleton loading* untuk artikel
- *Infinite scroll* atau paginasi tradisional
- Efek *hover* pada kartu blog (zoom gambar)

***User Flow***:
Pengguna → Halaman Blog → Jelajah artikel atau pencarian → Klik artikel yang menarik → Halaman Detail Blog

---

#### H. Halaman Detail Blog (*Blog Detail Page*)

**Deskripsi:**
Halaman Detail Blog (*Blog Detail page*) menampilkan artikel lengkap dengan format yang mudah dibaca dan menarik. Halaman ini juga mendorong keterlibatan melalui komentar, berbagi, dan artikel terkait.

**Elemen Utama:**
1. **Header Artikel (*Article Header*)**:
   - Lencana kategori
   - Judul artikel (H1, besar)
   - Info meta:
     * Foto + nama penulis (tautan ke profil penulis)
     * Tanggal publikasi
     * Tanggal pembaruan terakhir (jika ada)
     * Waktu baca (mis., "8 min read")
   - Tombol berbagi sosial (Facebook, Twitter, LinkedIn, WhatsApp)
   - Gambar unggulan (*featured image*) (lebar penuh, kualitas tinggi)

2. **Konten Artikel (*Article Content*)**:
   - Teks terformat dengan baik dengan:
     * Judul (*Headings*) (H2, H3, H4)
     * Paragraf dengan spasi yang tepat
     * Tebal, miring, daftar
     * *Blockquotes* untuk sorotan
     * Gambar dengan keterangan
     * Video *embed* (jika ada)
     * *Code blocks* (jika artikel teknis)
   - Daftar isi (*Table of contents*) (untuk artikel panjang):
     * *Sidebar sticky* dengan tautan ke bagian
     * *Scroll spy* menyorot bagian saat ini

3. **Kotak Bio Penulis (*Author Bio Box*)**:
   - Foto penulis
   - Nama + gelar
   - Bio singkat (2-3 kalimat)
   - Tautan "View all posts by [Author]"
   - Tautan media sosial

4. ***Tags* (Tag)**:
   - *Tag* yang dapat diklik untuk kategorisasi artikel
   - Tautan ke halaman arsip *tag*

5. **Bagian Keterlibatan (*Engagement Section*)**:
   - Tombol suka/hati dengan jumlah
   - Tombol *bookmark*
   - Jumlah berbagi (*share count*)

6. **Bagian Komentar (*Comments Section*)**:
   - Judul "Leave a Comment"
   - Formulir komentar (untuk pengguna yang sudah *login*):
     * *Textarea* untuk komentar
     * Tombol "Post Comment"
   - Daftar komentar yang ada:
     * *Avatar* + nama komentator
     * Teks komentar
     * Tanggal
     * Tombol balas
     * Balasan bersarang (1 level)
   - Paginasi untuk komentar
   - Pemberitahuan moderasi

7. **Artikel Terkait (*Related Articles*)**:
   - "You May Also Like"
   - 3 artikel terkait dalam format kartu
   - Berdasarkan kategori atau *tag*
   - Tautan "View All Articles"

8. **CTA *Newsletter***:
   - "Want More Content Like This?"
   - Formulir langganan email
   - Tombol "Subscribe to Our Newsletter"

9. ***Sticky Social Share Bar*** (samping):
   - Posisi tetap di kiri artikel (*desktop*)
   - Jumlah berbagi
   - Ikon untuk: Facebook, Twitter, LinkedIn, Salin Tautan

**Interaksi & Perilaku:**
- Daftar isi *sticky* dengan *scroll* halus
- *Lazy load* gambar dalam artikel
- Penyorotan sintaks kode (*code syntax highlighting*) (jika ada *code blocks*)
- Berbagi sosial dengan *popup* atau *native share API*
- Pengiriman komentar dengan AJAX
- Bilah kemajuan membaca (*reading progress bar*) di atas

***User Flow***:
Pengguna membaca artikel → Terlibat → Suka/komentar → Klik artikel terkait atau CTA "Book Session" (jika ada)

---

### 4.3.5.5 *Mockup* Halaman Pendukung (*Support Pages*)

Halaman pendukung (*support pages*) adalah halaman-halaman pendukung yang memberikan informasi penting terkait kontak, FAQ, kebijakan privasi, dan syarat & ketentuan. Halaman ini penting untuk transparansi, kepatuhan, dan layanan pelanggan (*customer service*).

#### A. Halaman Hubungi Kami (*Contact Us Page*)

**Deskripsi:**
Halaman Hubungi Kami (*Contact Us page*) menyediakan berbagai cara untuk menghubungi CUR-HEART, termasuk formulir kontak, alamat kantor, nomor telepon, email, dan media sosial. Halaman ini penting untuk dukungan pelanggan (*customer support*) dan pertanyaan (*inquiry*).

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Judul "Contact Us"
   - Subjudul "We'd Love to Hear from You"
   - *Breadcrumb*: Home > Contact

2. **Bagian Formulir Kontak (*Contact Form Section*)**:
   - Kolom formulir:
     * Nama Lengkap (wajib)
     * Alamat Email (wajib)
     * Nomor Telepon (opsional)
     * Subjek (*dropdown*: Pertanyaan Umum, Bantuan *Booking*, Dukungan Teknis, Kemitraan, Lainnya)
     * Pesan (*textarea*, wajib)
     * Tombol "Send Message" (primer)
   - Validasi formulir dengan pesan kesalahan (*error messages*)
   - Notifikasi sukses setelah *submit*

3. **Kartu Informasi Kontak (*Contact Information Cards*)**:
   - 3 kartu berdampingan:
     * **Lokasi**: Ikon penanda peta, alamat lengkap, tautan "Get Directions" ke Google Maps
     * **Telepon**: Ikon telepon, nomor telepon, tautan "Call Us Now" (tel:)
     * **Email**: Ikon amplop, alamat email, tautan "Send Email" (mailto:)

4. **Jam Operasional (*Business Hours*)**:
   - Format tabel atau daftar:
     * Senin - Jumat: 08:00 - 20:00
     * Sabtu: 09:00 - 18:00
     * Minggu: 10:00 - 16:00
   - Catatan tentang kontak darurat

5. ***Google Maps Embed***:
   - Peta interaktif yang menunjukkan lokasi kantor CUR-HEART
   - Penanda, kontrol zoom
   - Tinggi penuh (400-500px)

6. **Tautan Media Sosial (*Social Media Links*)**:
   - "Follow Us On Social Media"
   - Tombol ikon besar untuk:
     * Instagram
     * Facebook
     * LinkedIn
     * Twitter/X
     * YouTube
     * TikTok

7. **Pintasan FAQ (*FAQ Shortcut*)**:
   - "Looking for Quick Answers?"
   - Tombol "Visit Our FAQ Page"
   - Pratinjau 3 pertanyaan paling umum

8. **Metode Kontak Alternatif (*Alternative Contact Methods*)**:
   - Tombol chat WhatsApp (mengambang/*floating*)
   - Widget chat langsung (*live chat*) (kanan bawah)
   - Opsi "Schedule a Call Back"

**Interaksi & Perilaku:**
- Validasi formulir waktu nyata (*real-time*)
- Notifikasi *toast* sukses/kesalahan
- Peta interaktif (zoom, geser)
- Klik untuk menelepon/email pada *mobile*
- Tombol WhatsApp mengambang

***User Flow***:
Pengguna punya pertanyaan → Halaman Kontak → Isi formulir atau pilih metode kontak → *Submit* → Terima konfirmasi

---

#### B. Halaman FAQ (*FAQ Page*)

**Deskripsi:**
Halaman FAQ (*FAQ page*) menjawab pertanyaan-pertanyaan yang sering ditanyakan oleh calon klien dan klien yang sudah ada. Halaman ini mengurangi beban layanan pelanggan (*customer service*) dan membantu pengguna menemukan jawaban dengan cepat.

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Judul "Frequently Asked Questions"
   - Subjudul "Find answers to common questions"
   - *Breadcrumb*: Home > FAQ

2. **Bilah Pencarian (*Search Bar*)**:
   - "Search for answers..." dengan ikon pencarian
   - Pemfilteran pencarian waktu nyata (*real-time*)
   - Saran "Popular searches"

3. **Tab Kategori (*Category Tabs*)**:
   - Tab horizontal untuk kategorisasi:
     * Umum (*General*) (*default*)
     * *Booking* & Janji Temu (*Booking & Appointments*)
     * Pembayaran & Harga (*Payments & Pricing*)
     * Sesi & Terapi (*Sessions & Therapy*)
     * Akun & Privasi (*Account & Privacy*)
     * Dukungan Teknis (*Technical Support*)
   - Tab aktif disorot

4. **Daftar FAQ *Accordion***:
   - Per kategori, 8-12 pertanyaan
   - Format *accordion*:
     * Pertanyaan sebagai header (H4)
     * Jawaban tersembunyi, perluas saat klik
     * Animasi halus (*slide down*/*up*)
     * Ikon panah/*chevron* (status atas/bawah)
   - Jawaban diformat dengan:
     * Paragraf
     * Daftar *bullet*
     * Tebal untuk penekanan
     * Tautan ke halaman relevan

5. **Contoh FAQ (*Sample FAQs*)**:
   - **Umum (*General*)**:
     * "Apa itu hipnoterapi dan bagaimana cara kerjanya?"
     * "Apakah hipnoterapi aman?"
     * "Berapa banyak sesi yang saya perlukan?"
   - ***Booking***:
     * "Bagaimana cara memesan sesi?"
     * "Bisakah saya membatalkan atau menjadwal ulang?"
     * "Bagaimana jika saya terlambat untuk janji temu?"
   - **Pembayaran (*Payments*)**:
     * "Metode pembayaran apa yang Anda terima?"
     * "Apakah Anda menawarkan pengembalian dana?"
     * "Apakah ada biaya konsultasi?"
   - **Sesi (*Sessions*)**:
     * "Apa yang harus saya siapkan sebelum sesi?"
     * "Bisakah saya melakukan sesi secara *online*?"
     * "Apakah saya akan sadar selama hipnoterapi?"

6. **Tindakan Cepat (*Quick Actions*)**:
   - *Sidebar* (*desktop*) atau bagian bawah (*mobile*):
     * "Still have questions?"
     * Tombol "Contact Support"
     * Tombol "Schedule a Consultation"
     * Tautan "Browse Services"

7. **Bagian Umpan Balik (*Feedback Section*)**:
   - "Was this helpful?" jempol atas/bawah
   - Per item FAQ
   - Pesan terima kasih setelah umpan balik

8. **Sumber Daya Terkait (*Related Resources*)**:
   - Tautan ke:
     * Panduan Memulai (*Getting Started Guide*)
     * Cara Mempersiapkan Sesi Pertama Anda
     * Memahami Hipnoterapi (artikel blog)

**Interaksi & Perilaku:**
- *Accordion* satu per satu atau beberapa terbuka
- Pencarian menyorot teks yang cocok
- *Smooth scroll* ke bagian jika dari tautan eksternal
- Pemungutan suara "Was this helpful" dengan AJAX
- *Deep linking* untuk FAQ spesifik

***User Flow***:
Pengguna punya pertanyaan → Halaman FAQ → Cari atau jelajah kategori → Temukan jawaban → Terpecahkan atau klik "Contact Support"

---

#### C. Halaman Kebijakan Privasi (*Privacy Policy Page*)

**Deskripsi:**
Halaman Kebijakan Privasi (*Privacy Policy page*) menjelaskan bagaimana CUR-HEART mengumpulkan, menggunakan, menyimpan, dan melindungi data pribadi pengguna. Halaman ini penting untuk kepatuhan (*compliance*) terhadap regulasi (GDPR, undang-undang perlindungan data Indonesia) dan membangun kepercayaan.

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Judul "Privacy Policy"
   - Tanggal pembaruan terakhir: "Last Updated: October 28, 2024"
   - *Breadcrumb*: Home > Privacy Policy

2. **Daftar Isi (*Table of Contents*)**:
   - *Sidebar sticky* (*desktop*) dengan tautan ke bagian:
     1. Pengantar (*Introduction*)
     2. Informasi yang Kami Kumpulkan (*Information We Collect*)
     3. Bagaimana Kami Menggunakan Informasi Anda (*How We Use Your Information*)
     4. Berbagi dan Pengungkapan Informasi (*Information Sharing and Disclosure*)
     5. Keamanan Data (*Data Security*)
     6. Hak dan Pilihan Anda (*Your Rights and Choices*)
     7. *Cookie* dan Teknologi Pelacakan (*Cookies and Tracking Technologies*)
     8. Layanan Pihak Ketiga (*Third-Party Services*)
     9. Privasi Anak-anak (*Children's Privacy*)
     10. Perubahan terhadap Kebijakan Ini (*Changes to This Policy*)
     11. Hubungi Kami (*Contact Us*)
   - *Scroll spy* untuk menyorot bagian saat ini

3. **Bagian Konten (*Content Sections*)**:
   - **1. Pengantar (*Introduction*)**:
     * Pernyataan sambutan
     * Cakupan kebijakan
     * Persetujuan

   - **2. Informasi yang Kami Kumpulkan (*Information We Collect*)**:
     * Informasi Pribadi (nama, email, telepon, alamat)
     * Informasi Kesehatan (catatan terapi, riwayat medis) - ditekankan sebagai sensitif
     * Informasi Akun (nama pengguna, kata sandi)
     * Informasi Pembayaran (kartu kredit, alamat penagihan)
     * Data Penggunaan (alamat IP, browser, info perangkat)
     * Data *cookie* dan pelacakan

   - **3. Bagaimana Kami Menggunakan Informasi Anda (*How We Use Your Information*)**:
     * Daftar tujuan:
       - Menyediakan layanan terapi
       - Memproses *booking* dan pembayaran
       - Berkomunikasi dengan klien
       - Meningkatkan layanan kami
       - Pemasaran (dengan persetujuan)
       - Kepatuhan hukum

   - **4. Berbagi Informasi (*Information Sharing*)**:
     * Dengan siapa kami berbagi:
       - Terapis (hanya informasi relevan)
       - Pemroses pembayaran (*payment processors*)
       - Penyedia layanan (hosting, analitik)
       - Otoritas hukum (jika diperlukan)
     * Kami TIDAK menjual data pribadi

   - **5. Keamanan Data (*Data Security*)**:
     * Enkripsi (SSL/TLS)
     * Server aman
     * Kontrol akses
     * Audit keamanan berkala
     * Prosedur notifikasi pelanggaran data

   - **6. Hak Anda (*Your Rights*)**:
     * Akses data Anda
     * Koreksi ketidakakuratan
     * Hapus data Anda (hak untuk dilupakan)
     * Ekspor data Anda
     * Tarik persetujuan
     * Tolak pemasaran (*opt-out marketing*)
     * Cara menggunakan hak

   - **7. *Cookie***:
     * Jenis *cookie* yang digunakan
     * Tujuan masing-masing
     * Cara mengelola *cookie*

   - **8. Layanan Pihak Ketiga (*Third-Party Services*)**:
     * Google Analytics
     * *Payment gateway* (Midtrans)
     * Konferensi video (untuk sesi *online*)
     * Plugin media sosial

   - **9. Privasi Anak-anak (*Children's Privacy*)**:
     * Persyaratan usia minimum (13 atau 18)
     * Persetujuan orang tua diperlukan

   - **10. Perubahan Kebijakan (*Policy Changes*)**:
     * Bagaimana pengguna akan diberitahu
     * Tanggal efektif perubahan

   - **11. Kontak (*Contact*)**:
     * Kontak petugas perlindungan data
     * Email untuk masalah privasi

4. **Kotak Sorotan (*Highlight Boxes*)**:
   - Catatan penting dalam kotak berwarna
   - Contoh: "Informasi kesehatan Anda sangat rahasia dan dilindungi berdasarkan [undang-undang terkait]"

5. **Bagian CTA**:
   - "Have Questions About Your Privacy?"
   - Tombol "Contact Our Privacy Team"

**Interaksi & Perilaku:**
- Konten bentuk panjang yang dapat di-*scroll*
- TOC *sticky* untuk navigasi mudah
- *Smooth scroll* dengan *offset* untuk header
- CSS ramah cetak (*print-friendly*)
- Opsi unduh sebagai PDF

***User Flow***:
Pengguna khawatir tentang privasi → Kebijakan Privasi → Baca bagian relevan → Terjamin atau hubungi tim privasi

---

#### D. Halaman Syarat & Ketentuan (*Terms & Conditions Page*)

**Deskripsi:**
Halaman Syarat & Ketentuan (*Terms & Conditions page*) menetapkan aturan hukum, kewajiban, dan hak antara CUR-HEART dan pengguna. Halaman ini melindungi kedua belah pihak dan menetapkan harapan untuk penggunaan layanan.

**Elemen Utama:**
1. ***Page Header* (Header Halaman)**:
   - Judul "Terms and Conditions"
   - Tanggal pembaruan terakhir
   - *Breadcrumb*: Home > Terms & Conditions

2. **Daftar Isi (*Table of Contents*)**:
   - *Sidebar sticky* dengan tautan:
     1. Penerimaan Ketentuan (*Acceptance of Terms*)
     2. Deskripsi Layanan (*Description of Services*)
     3. Akun Pengguna dan Registrasi (*User Account and Registration*)
     4. *Booking* dan Janji Temu (*Booking and Appointments*)
     5. Pembayaran, Biaya, dan Pengembalian Dana (*Payments, Fees, and Refunds*)
     6. Kebijakan Pembatalan dan Penjadwalan Ulang (*Cancellation and Rescheduling Policy*)
     7. Perilaku dan Tanggung Jawab Pengguna (*User Conduct and Responsibilities*)
     8. Hubungan Terapis-Klien (*Therapist-Client Relationship*)
     9. Kerahasiaan dan Privasi (*Confidentiality and Privacy*)
     10. Hak Kekayaan Intelektual (*Intellectual Property Rights*)
     11. Penafian dan Batasan Tanggung Jawab (*Disclaimers and Limitations of Liability*)
     12. Ganti Rugi (*Indemnification*)
     13. Penghentian (*Termination*)
     14. Penyelesaian Sengketa (*Dispute Resolution*)
     15. Hukum yang Mengatur (*Governing Law*)
     16. Perubahan terhadap Ketentuan (*Changes to Terms*)
     17. Informasi Kontak (*Contact Information*)

3. **Bagian Konten (*Content Sections*)**:
   - **1. Penerimaan (*Acceptance*)**:
     * Dengan menggunakan layanan, Anda setuju dengan ketentuan
     * Harus berusia 18+ atau memiliki persetujuan orang tua
     * Penggunaan berkelanjutan = persetujuan berkelanjutan

   - **2. Deskripsi Layanan (*Services Description*)**:
     * Apa yang disediakan CUR-HEART
     * Sesi hipnoterapi *online* dan *offline*
     * Platform *booking*
     * Bukan layanan medis darurat

   - **3. Registrasi Akun (*Account Registration*)**:
     * Persyaratan untuk *booking*
     * Kewajiban informasi akurat
     * Tanggung jawab keamanan akun
     * Satu akun per orang

   - **4. *Booking***:
     * Cara melakukan *booking*
     * Proses konfirmasi
     * Format sesi (*online*/*offline*)
     * Persyaratan usia minimum

   - **5. Pembayaran (*Payments*)**:
     * Metode pembayaran yang diterima
     * Waktu pembayaran (sebelum sesi)
     * Mata uang (IDR)
     * Kebijakan tanpa pengembalian dana (dengan pengecualian)
     * Ketentuan kode promosi (*promotional code terms*)

   - **6. Kebijakan Pembatalan (*Cancellation Policy*)**:
     * Pembatalan klien:
       - 24+ jam sebelumnya: Pengembalian dana penuh/*reschedule*
       - 12-24 jam: Biaya 50%
       - <12 jam: Tanpa pengembalian dana
     * Pembatalan terapis: Pengembalian dana penuh atau *reschedule*
     * Kebijakan tidak hadir (*no-show*)

   - **7. Perilaku Pengguna (*User Conduct*)**:
     * Aktivitas yang dilarang:
       - Informasi palsu
       - Pelecehan (*harassment*)
       - Spam
       - Penggunaan ilegal
     * Konsekuensi pelanggaran

   - **8. Hubungan Terapis-Klien (*Therapist-Client Relationship*)**:
     * Batasan profesional
     * Bukan pengganti perawatan medis
     * Penanganan situasi darurat
     * Status kontraktor independen terapis

   - **9. Kerahasiaan (*Confidentiality*)**:
     * Kerahasiaan sesi
     * Pengecualian (bahaya pada diri/orang lain, persyaratan hukum)
     * Rujukan ke Kebijakan Privasi

   - **10. Hak Kekayaan Intelektual (*Intellectual Property*)**:
     * CUR-HEART memiliki konten situs web
     * Lisensi pengguna untuk menggunakan
     * Pembatasan penyalinan/reproduksi
     * Penggunaan merek dagang (*trademark*)

   - **11. Penafian (*Disclaimers*)**:
     * Layanan disediakan "apa adanya" (*as is*)
     * Tidak ada jaminan hasil
     * Bukan saran medis
     * Penafian tautan pihak ketiga

   - **12. Batasan Tanggung Jawab (*Limitation of Liability*)**:
     * Batas tanggung jawab maksimum
     * Tidak ada tanggung jawab untuk kerusakan tidak langsung
     * Keadaan kahar (*force majeure*)

   - **13. Ganti Rugi (*Indemnification*)**:
     * Pengguna setuju untuk mengganti rugi CUR-HEART
     * Dari klaim yang timbul dari penggunaan pengguna

   - **14. Penghentian (*Termination*)**:
     * CUR-HEART dapat menghentikan akun
     * Pengguna dapat menutup akun kapan saja
     * Efek penghentian

   - **15. Penyelesaian Sengketa (*Dispute Resolution*)**:
     * Negosiasi dengan itikad baik terlebih dahulu
     * Mediasi/arbitrasi
     * Yurisdiksi

   - **16. Hukum yang Mengatur (*Governing Law*)**:
     * Hukum Indonesia berlaku
     * Yurisdiksi di pengadilan tertentu

   - **17. Perubahan terhadap Ketentuan (*Changes to Terms*)**:
     * Hak untuk memodifikasi
     * Metode notifikasi
     * Tanggal efektif

   - **18. Kontak (*Contact*)**:
     * Untuk pertanyaan tentang ketentuan
     * Email departemen hukum

4. **Pesan Penting (*Important Callouts*)**:
   - Kotak yang disorot untuk ketentuan kunci
   - Contoh: "PENTING: Sesi harus dibayar penuh sebelum konfirmasi"

5. **Bagian Pengakuan (*Acknowledgment Section*)**:
   - *Checkbox*: "I have read and agree to the Terms and Conditions"
   - Wajib saat registrasi atau *booking* pertama

**Interaksi & Perilaku:**
- Mirip dengan Kebijakan Privasi
- Navigasi TOC *sticky*
- *Scrolling* halus
- Opsi cetak/unduh
- Sorot istilah pencarian (jika dari pencarian)

***User Flow***:
Pengguna mendaftar/*booking* → Diminta menerima ketentuan → Klik tautan → Halaman Ketentuan → Baca atau *scroll* ke bawah → *Checkbox* terima → Lanjutkan dengan registrasi/*booking*

---

### 4.3.5.6 *Mockup* Halaman Autentikasi (*Authentication Pages*)

Halaman autentikasi (*authentication pages*) adalah halaman-halaman yang menangani proses *login*, registrasi, dan pemulihan kata sandi (*password recovery*). Desain halaman autentikasi harus menyeimbangkan antara keamanan, kegunaan, dan pengalaman pengguna yang lancar.

---

**[GAMBAR 4.32 - *Mockup* Halaman *Login* (*Login Page*)]** 🔐
_Halaman autentikasi - Formulir email/kata sandi, ingat saya, tautan lupa kata sandi_

**[GAMBAR 4.33 - *Mockup* Halaman Registrasi (*Register Page*) (Klien & Terapis)]** 🔐
_Halaman autentikasi - Formulir registrasi multi-langkah, penerimaan ketentuan_

**[GAMBAR 4.34 - *Mockup* Halaman Lupa Kata Sandi (*Forgot Password Page*)]** 🔐
_Halaman autentikasi - Input email untuk tautan reset kata sandi_

**[GAMBAR 4.35 - *Mockup* Halaman Reset Kata Sandi (*Reset Password Page*)]** 🔐
_Halaman autentikasi - Formulir kata sandi baru dengan konfirmasi_

---

#### A. Halaman *Login* (*Login Page*)

**Deskripsi:**
Halaman *Login* (*Login page*) memungkinkan pengguna yang sudah ada untuk masuk ke akun mereka dan mengakses *dashboard* serta fitur-fitur yang memerlukan autentikasi. Halaman ini harus sederhana, jelas, dan aman.

**Elemen Utama:**
1. **Tata Letak (*Layout*)**:
   - Tata letak layar terpisah (*split screen layout*) (*desktop*):
     * Kiri (40%): Ilustrasi/gambar tentang kesejahteraan mental, visual menenangkan
     * Kanan (60%): Formulir *login*
   - Kolom tunggal (*mobile*): Hanya formulir, dengan logo di atas

2. ***Branding***:
   - Logo CUR-HEART di tengah-atas atau kiri-atas
   - Slogan (*tagline*) (opsional): "Welcome Back to Your Wellness Journey"

3. **Formulir *Login* (*Login Form*)**:
   - Judul formulir: "Log In to Your Account"
   - Kolom input:
     * **Email/*Username***: 
       - *Placeholder* "Enter your email address"
       - Awalan ikon email
       - Validasi: Wajib, format email valid
     * **Kata Sandi (*Password*)**:
       - *Placeholder* "Enter your password"
       - Awalan ikon gembok
       - Alih tampil/sembunyikan kata sandi (ikon mata)
       - Validasi: Wajib, min 6 karakter
   - *Checkbox* "Remember Me"
   - Tautan "Forgot Password?" (sejajar kanan)
   - **Tombol "Log In"** (primer, lebar penuh, merah muda)
   - Status *loading* pada tombol saat *submit*

4. **Metode *Login* Alternatif (*Alternative Login Methods*)**:
   - Pembatas: "Or continue with"
   - Tombol *login* sosial:
     * Tombol *login* Google
     * Tombol *login* Facebook
   - Tampilan *Single Sign-On* dengan warna merek

5. **Ajakan Registrasi (*Registration Prompt*)**:
   - Teks: "Don't have an account?"
   - Tautan "Sign Up" (berwarna, tebal)

6. **Indikator Keamanan & Kepercayaan (*Security & Trust Indicators*)**:
   - Ikon gembok SSL dengan teks "Secure Login"
   - Tautan kebijakan privasi di *footer*

7. **Penanganan Kesalahan (*Error Handling*)**:
   - Pesan kesalahan muncul di atas formulir atau per kolom:
     * "Invalid email or password"
     * "Please enter a valid email address"
     * "This field is required"
   - Batas merah pada kolom yang salah
   - Ikon kesalahan

8. **Keadaan Sukses (*Success State*)**:
   - *Spinner* *loading* saat mengautentikasi
   - Pesan "Logging you in..."
   - Arahkan ke *dashboard* setelah sukses

**Interaksi & Perilaku:**
- Validasi waktu nyata saat *blur* (kehilangan fokus)
- Validasi *submit* saat klik tombol
- Tombol Enter *submit* formulir
- Navigasi Tab antar kolom
- Animasi alih tampil/sembunyikan kata sandi
- *Popup login* sosial atau alur OAuth
- Peringatan *timeout* sesi (jika dari sesi kedaluwarsa)

***User Flow***:
Pengguna → Halaman *Login* → Masukkan kredensial → Klik "Log In" → Autentikasi → Arahkan ke *Dashboard* (berbasis peran: klien/terapis/admin)

**Fitur Keamanan (*Security Features*):**
- Kata sandi tidak disimpan dalam teks biasa (*plaintext*) (*backend*)
- Perlindungan *token* CSRF
- Pembatasan laju (*rate limiting*) untuk mencegah *brute force*
- *Captcha* setelah beberapa upaya gagal
- Transmisi kata sandi aman (HTTPS)

---

#### B. Halaman Registrasi (*Register Page*)

**Deskripsi:**
Halaman Registrasi (*Register page*) memungkinkan pengguna baru untuk membuat akun CUR-HEART. Halaman ini harus jelas dalam membedakan tipe pengguna (Klien vs Terapis) dan mengumpulkan informasi yang diperlukan tanpa membebani pengguna.

**Elemen Utama:**
1. **Tata Letak (*Layout*)**:
   - Layar terpisah serupa dengan halaman *Login*
   - Kiri: Ilustrasi sambutan "Start Your Wellness Journey"
   - Kanan: Formulir registrasi

2. ***Branding* & Header**:
   - Logo CUR-HEART
   - Judul: "Create Your Account"
   - Subjudul: "Join thousands who've found their peace"

3. **Pemilihan Tipe Pengguna (*User Type Selection*)** (Langkah 0):
   - "I want to register as..."
   - Dua kartu opsi besar:
     * **Kartu Klien (*Client Card*)**:
       - Ikon: *Avatar* pengguna
       - Judul: "I'm seeking therapy"
       - Deskripsi: "Book sessions with certified therapists"
       - Tombol radio atau pemilihan kartu
     * **Kartu Terapis (*Therapist Card*)**:
       - Ikon: *Avatar* profesional
       - Judul: "I'm a therapist"
       - Deskripsi: "Join our network of professionals"
       - Tombol radio atau pemilihan kartu
   - Kartu terpilih disorot (batas merah muda, latar belakang)
   - Tombol "Continue" (*disabled* hingga dipilih)

4. **Formulir Registrasi (*Registration Form*)** (Setelah pemilihan tipe):
   
   **Untuk Klien (*For Clients*)**:
   - **Informasi Pribadi (*Personal Information*)**:
     * Nama Lengkap (wajib)
     * Alamat Email (wajib, unik)
     * Nomor Telepon (wajib, dengan *dropdown* kode negara)
     * Tanggal Lahir (*date picker*)
     * Jenis Kelamin (*dropdown*: Laki-laki, Perempuan, Lainnya, Tidak ingin menyebutkan)
   
   - **Keamanan Akun (*Account Security*)**:
     * Kata Sandi (wajib, min 8 karakter)
       - Indikator kekuatan kata sandi (lemah/sedang/kuat)
       - Daftar persyaratan:
         * Minimal 8 karakter
         * Satu huruf kapital
         * Satu angka
         * Satu karakter khusus
     * Konfirmasi Kata Sandi (wajib, harus cocok)
   
   - **Preferensi (*Preferences*)** (opsional):
     * Bahasa Pilihan (*dropdown*)
     * Dari mana Anda tahu tentang kami? (*dropdown*)
   
   **Untuk Terapis (*For Therapists*)** (Kolom tambahan):
   - Nomor Lisensi (wajib)
   - Spesialisasi (*multi-select*)
   - Tahun Pengalaman (input angka)
   - Unggah Lisensi/Sertifikat (unggah file)
   - Bio Profesional (*textarea*, maks 200 kata)
   - Catatan: "Aplikasi Anda akan ditinjau oleh tim kami"

5. **Syarat & Ketentuan (*Terms & Conditions*)**:
   - *Checkbox*: "I agree to the Terms & Conditions and Privacy Policy"
   - Tautan dapat diklik, buka di tab baru atau *modal*
   - Wajib untuk mengaktifkan tombol *submit*

6. **Tombol *Submit***:
   - "Create Account" (primer, lebar penuh)
   - *Disabled* hingga semua kolom wajib valid dan S&K diterima
   - Status *loading* dengan *spinner*

7. **Ajakan *Login* (*Login Prompt*)**:
   - "Already have an account?"
   - Tautan "Log In"

8. **Indikator Kepercayaan (*Trust Indicators*)**:
   - "Your information is secure and confidential"
   - Lencana SSL
   - "No spam, unsubscribe anytime"

**Validasi & Penanganan Kesalahan (*Validation & Error Handling*):**
- Validasi waktu nyata untuk setiap kolom
- Pemeriksaan keunikan email (*backend*)
- Indikator kekuatan kata sandi visual (merah/kuning/hijau)
- Pesan kesalahan sebaris dengan instruksi jelas
- Ikon sukses untuk kolom valid (tanda centang hijau)

**Alur Sukses (*Success Flow*):**
- **Untuk Klien (*For Clients*)**:
  * Akun dibuat langsung
  * Pesan sukses "Welcome!"
  * Email verifikasi dikirim
  * Arahkan ke orientasi/*dashboard*
  * Email sambutan dikirim

- **Untuk Terapis (*For Therapists*)**:
  * Aplikasi dikirimkan
  * Pesan "Thank you! We'll review your application"
  * Email notifikasi dikirim
  * "You'll hear from us within 2-3 business days"
  * Arahkan ke halaman status tertunda

**Interaksi & Perilaku:**
- Pengungkapan progresif (*progressive disclosure*) (tampilkan formulir setelah pemilihan tipe)
- Transisi halus antar langkah
- Indikator kekuatan kata sandi diperbarui waktu nyata
- Validasi kolom saat *blur* atau saat *submit*
- Unggah file dengan dukungan seret & lepas (*drag & drop*)
- Formulir dioptimalkan untuk *mobile* (input lebih besar, ramah *picker*)

***User Flow***:
Pengguna → Halaman Registrasi → Pilih tipe pengguna (Klien/Terapis) → Isi formulir → Terima S&K → *Submit* → Email verifikasi dikirim → Pesan sukses → Arahkan

---

#### C. Halaman Lupa Kata Sandi (*Forgot Password Page*)

**Deskripsi:**
Halaman Lupa Kata Sandi (*Forgot Password page*) membantu pengguna yang lupa kata sandi mereka untuk melakukan reset kata sandi melalui verifikasi email. Prosesnya harus aman namun ramah pengguna.

**Elemen Utama:**
1. **Tata Letak (*Layout*)**:
   - Tata letak formulir terpusat (sederhana, fokus)
   - Gangguan minimal
   - Lebar maks: 400px

2. **Header**:
   - Logo CUR-HEART (dapat diklik, kembali ke beranda)
   - Ikon: Gembok dengan tanda tanya atau ikon kunci
   - Judul: "Forgot Your Password?"
   - Subjudul: "No worries, we'll send you reset instructions"

3. **Formulir Input Email (*Email Input Form*)**:
   - Label: "Email Address"
   - Kolom input:
     * *Placeholder*: "Enter your registered email"
     * Awalan ikon email
     * Validasi: Wajib, format email valid
   - Teks pembantu: "Enter the email address associated with your account"

4. **Tombol *Submit***:
   - "Send Reset Link" (primer, lebar penuh)
   - Status *loading*: "Sending..."

5. **Kembali ke *Login* (*Back to Login*)**:
   - Tautan "← Back to Login"
   - Kembali ke halaman *Login*

6. **Keadaan Sukses (*Success State*)**:
   - Ikon sukses (tanda centang dalam lingkaran)
   - Pesan: "Reset Link Sent!"
   - Instruksi: "We've sent a password reset link to [email]. Please check your inbox and follow the instructions."
   - Catatan: "Didn't receive the email? Check your spam folder or click to resend"
   - Tombol "Resend Link" (*disabled* selama 60 detik, *countdown*)
   - Tombol "Back to Login"

7. **Keadaan Kesalahan (*Error State*)**:
   - Pesan kesalahan: "Email address not found"
   - Saran: "Please check your email or Sign Up if you don't have an account"
   - "Try Again" atau hapus kolom

8. **Fitur Keamanan (*Security Features*)**:
   - Batasan laju (*rate limiting*) (maks 3 permintaan per email per jam)
   - Pesan sukses generik (tidak mengungkapkan apakah email ada - keamanan)
   - Kedaluwarsa token (tautan reset berlaku selama 1 jam)

**Interaksi & Perilaku:**
- Halaman sederhana, tujuan tunggal
- *Auto-focus* pada input email
- *Submit* dengan tombol *Enter*
- Pesan kesalahan yang jelas
- *Timer countdown* untuk tombol *resend*
- Umpan balik visual validasi email

***User Flow***:
Pengguna lupa kata sandi → Klik "Forgot Password" dari *Login* → Masukkan email → *Submit* → Periksa email → Klik tautan reset → Arahkan ke halaman *Reset Password*

---

#### D. Halaman Reset Kata Sandi (*Reset Password Page*)

**Deskripsi:**
Halaman Reset Kata Sandi (*Reset Password page*) adalah halaman yang dibuka dari tautan di email reset kata sandi. Pengguna dapat memasukkan kata sandi baru dan mengkonfirmasinya. Halaman ini harus aman dan memberikan umpan balik yang jelas.

**Elemen Utama:**
1. **Tata Letak (*Layout*)**:
   - Formulir terpusat, sederhana
   - Lebar maks: 400px

2. **Header**:
   - Logo CUR-HEART
   - Ikon: Gembok dengan tanda centang atau ikon kunci
   - Judul: "Reset Your Password"
   - Subjudul: "Enter your new password below"

3. **Validasi Token (*Token Validation*)**:
   - Validasi otomatis saat halaman dimuat
   - Jika valid: Tampilkan formulir
   - Jika kedaluwarsa/tidak valid:
     * Pesan kesalahan: "This reset link has expired or is invalid"
     * Tombol "Request New Link"
     * Arahkan ke halaman Lupa Kata Sandi

4. **Formulir Reset Kata Sandi (*Reset Password Form*)**:
   - **Kolom Kata Sandi Baru (*New Password Field*)**:
     * Label: "New Password"
     * Input dengan tombol *show/hide*
     * Indikator kekuatan kata sandi
     * Daftar persyaratan (*live update*):
       - ✓ Minimal 8 karakter
       - ✓ Satu huruf kapital
       - ✓ Satu huruf kecil
       - ✓ Satu angka
       - ✓ Satu karakter khusus
   
   - **Kolom Konfirmasi Kata Sandi (*Confirm Password Field*)**:
     * Label: "Confirm New Password"
     * Input dengan tombol *show/hide*
     * Validasi kecocokan waktu nyata
     * Kesalahan: "Passwords do not match"

5. **Tombol *Submit***:
   - "Reset Password" (primer, lebar penuh)
   - *Disabled* hingga semua persyaratan terpenuhi
   - Status *loading*

6. **Indikator Keamanan (*Security Indicators*)**:
   - "For your security, this link will expire in [*countdown*: 58:32]"
   - "Your password will be encrypted and stored securely"

7. **Keadaan Sukses (*Success State*)**:
   - Ikon sukses (tanda centang besar)
   - Pesan: "Password Reset Successfully!"
   - "Your password has been updated. You can now log in with your new password."
   - Tombol "Go to Login" (primer)
   - *Auto-redirect* setelah 5 detik dengan *countdown*

8. **Penanganan Kesalahan (*Error Handling*)**:
   - Kesalahan server (masalah jaringan)
   - Token kedaluwarsa selama pengiriman
   - Kata sandi tidak memenuhi persyaratan
   - Pesan kesalahan yang jelas dengan tindakan yang disarankan

**Interaksi & Perilaku:**
- *Password strength meter* waktu nyata
- Daftar persyaratan dengan tanda centang
- Indikator kecocokan konfirmasi kata sandi
- *Timer countdown* token
- Peringatan kedaluwarsa (mis., "Only 5 minutes left!")
- *Auto-redirect* setelah sukses
- Token sekali pakai (*one-time use token*) (tidak valid setelah reset berhasil)

***User Flow***:
Pengguna → Klik tautan reset dari email → Token divalidasi → Masukkan kata sandi baru → Konfirmasi kata sandi → *Submit* → Sukses → Arahkan ke *Login* → *Login* dengan kata sandi baru

**Fitur Keamanan (*Security Features*)**:
- Reset berbasis token (aman, terbatas waktu)
- Penegakan kompleksitas kata sandi (*password complexity enforcement*)
- Token sekali pakai (*one-time use tokens*)
- Transmisi HTTPS
- Perlindungan CSRF
- Batasan laju (*rate limiting*)
- Kata sandi lama tidak dapat digunakan kembali (opsional)

---

### 4.3.5.7 *Mockup* ***Dashboard*** Klien (*Client Dashboard Pages*)

***Dashboard*** Klien adalah area setelah *login* khusus untuk klien yang telah terdaftar. ***Dashboard*** ini memungkinkan klien untuk melakukan *booking* sesi, mengelola janji temu (*manage appointments*), melacak kemajuan (*track progress*), dan berkomunikasi dengan terapis.

---

**[GAMBAR 4.36 - *Mockup* ***Dashboard*** Klien (*Client Dashboard*) (Utama)]** 👤
_*Dashboard* klien - Kartu ringkasan, janji temu mendatang, tindakan cepat_

**[GAMBAR 4.37 - *Mockup* *Booking* Langkah 1 - Pilih Layanan (*Select Service*)]** 👤
_Klien - Pilih layanan dengan deskripsi dan harga_

**[GAMBAR 4.38 - *Mockup* *Booking* Langkah 2 - Pilih Terapis (*Choose Therapist*)]** 👤
_Klien - Pilih terapis dengan profil dan ketersediaan_

**[GAMBAR 4.39 - *Mockup* *Booking* Langkah 3 - Pilih Tanggal & Waktu (*Select Date & Time*)]** 👤
_Klien - *Picker* kalender dan slot waktu tersedia_

**[GAMBAR 4.40 - *Mockup* *Booking* Langkah 4 - Konfirmasi & Pembayaran (*Confirm & Payment*)]** 👤
_Klien - Ringkasan *booking*, pemilihan metode pembayaran_

**[GAMBAR 4.41 - *Mockup* Halaman Sukses *Booking* (*Booking Success Page*)]** 👤
_Klien - Pesan konfirmasi, detail *booking*, langkah berikutnya_

**[GAMBAR 4.42 - *Mockup* Daftar Janji Temu Saya (*My Appointments List*)]** 👤
_Klien - Tabel/kartu semua *booking* dengan status dan tindakan_

**[GAMBAR 4.43 - *Mockup* Halaman Detail Janji Temu (*Appointment Detail Page*)]** 👤
_Klien - Detail *booking* lengkap, opsi *reschedule/cancel*_

**[GAMBAR 4.44 - *Mockup* ***Dashboard*** Pelacakan Kemajuan Klien (*Client Progress Tracking Dashboard*)]** 👤
_Klien - Grafik yang menampilkan metrik kecemasan, kepercayaan diri, kualitas tidur_

**[GAMBAR 4.45 - *Mockup* Pesan Klien (*Client Messages*) (*Chat* dengan Terapis)]** 👤
_Klien - Antarmuka *chat* dengan terapis_

---

#### A. ***Dashboard*** Klien (Utama) (*Client Dashboard Main*)

**Deskripsi:**
***Dashboard*** Klien Utama (*Client Dashboard Main*) adalah *landing page* setelah klien *login*. Halaman ini memberikan gambaran umum (*overview*) dari status janji temu (*appointments*), kemajuan (*progress*), dan tindakan cepat (*quick actions*) untuk melakukan *booking* sesi.

**Elemen Utama:**
1. ***Top Navigation Bar***:
   - Logo CUR-HEART (kiri)
   - Item menu navigasi:
     * *Dashboard* (aktif)
     * *Book Session*
     * *My Appointments*
     * *My Progress*
     * *Messages*
   - Sisi kanan:
     * Ikon bel notifikasi (dengan lencana jumlah)
     * *Avatar* pengguna dengan *dropdown*:
       - *My Profile*
       - *Settings*
       - *Help & Support*
       - *Log Out*

2. **Navigasi *Sidebar*** (***Sidebar Navigation***) (*Desktop*):
   - *Sidebar* kiri tetap, lebar 260px
   - Item menu dengan ikon:
     * *Dashboard* (ikon beranda) - aktif
     * *Book Session* (ikon kalender-plus)
     * *My Appointments* (ikon kalender)
     * *My Progress* (ikon grafik)
     * *Messages* (ikon pesan)
     * *Profile* (ikon pengguna)
     * *Settings* (ikon roda gigi)
   - Tombol tutup (*collapse button*) (*hamburger*)

3. **Bagian Sambutan (*Welcome Section*)**:
   - Salam: "Welcome back, [Nama Klien]!"
   - Subjudul: "How are you feeling today?"
   - Tanggal & waktu saat ini

4. **Kartu Statistik Cepat (*Quick Stats Cards*)** (4 kartu dalam baris):
   - **Sesi Mendatang (*Upcoming Sessions*)**:
     * Angka besar: "2"
     * Ikon: Kalender
     * Tautan: "View All"
   
   - **Sesi Selesai (*Completed Sessions*)**:
     * Angka: "8"
     * Ikon: Tanda centang
     * Teks kemajuan: "+2 this month"
   
   - **Jam yang Dihabiskan (*Hours Spent*)**:
     * Angka: "12.5"
     * Ikon: Jam
     * Satuan: "hours"
   
   - **Skor Kemajuan (*Progress Score*)**:
     * Angka: "78%"
     * Ikon: Tren naik
     * Perubahan: "+5% from last month"

5. **Kartu Janji Temu Berikutnya (*Next Appointment Card*)** (Unggulan):
   - Kartu besar dengan sorotan
   - "Your Next Session"
   - Foto terapis + nama
   - Nama layanan: "Stress & Anxiety Management"
   - Tanggal & waktu: "Today, 3:00 PM" (dengan *countdown* jika hari ini)
   - Durasi: "60 minutes"
   - Tipe sesi: "Online" (lencana)
   - Tombol tindakan:
     * "Join Session" (primer, jika dalam 15 menit)
     * "View Details" (sekunder)
     * Tautan "Reschedule"

6. **Bagian Tindakan Cepat (*Quick Actions Section*)**:
   - Judul: "Quick Actions"
   - 3 kartu tindakan:
     * ***Book* Sesi Baru (*Book New Session*)**:
       - Ikon: Kalender plus
       - Deskripsi: "Schedule your next appointment"
       - Tombol: "Book Now"
     
     * **Pesan Terapis (*Message Therapist*)**:
       - Ikon: Pesan
       - Deskripsi: "Chat with your therapist"
       - Tombol: "Open Chat"
     
     * **Lihat Kemajuan (*View Progress*)**:
       - Ikon: Grafik
       - Deskripsi: "Track your wellness journey"
       - Tombol: "See Progress"

7. **Daftar Janji Temu Mendatang (*Upcoming Appointments List*)**:
   - Judul: "Upcoming Appointments"
   - Daftar 3-4 janji temu berikutnya
   - Setiap item:
     * Lencana tanggal (vertikal: Bulan + Hari)
     * Waktu
     * *Avatar* terapis + nama
     * Nama layanan
     * Lencana status (*Confirmed*, *Pending Payment*)
     * Tindakan cepat: *View* | *Reschedule* | *Cancel*
   - Tautan "View All Appointments" di bawah

8. ***Widget* Ringkasan Kemajuan (*Progress Overview Widget*)**:
   - Judul: "Your Progress This Month"
   - Grafik garis sederhana atau *progress bar*:
     * Tren skor suasana hati
     * Kehadiran sesi
     * Penyelesaian tujuan
   - Tautan "View Detailed Report"

9. **Pesan Terbaru (*Recent Messages*)**:
   - Judul: "Recent Messages"
   - 2-3 *thread* pesan terbaru
   - Setiap:
     * *Avatar* terapis
     * Nama
     * Pratinjau pesan terakhir (dipotong)
     * *Timestamp*
     * Lencana belum dibaca (jika ada)
   - Tautan "View All Messages"

10. **Bagian Sumber Daya Bermanfaat (*Helpful Resources Section*)**:
    - "Resources for You"
    - 2-3 kartu:
      * Artikel blog
      * Tutorial video
      * Panduan swadaya
    - Tautan "Browse All Resources"

**Interaksi & Perilaku:**
- Pembaruan waktu nyata (*real-time updates*) (*WebSocket* untuk notifikasi)
- *Timer countdown* untuk sesi berikutnya
- Efek *hover* pada kartu
- *Skeleton loading* untuk data *async*
- Responsif: Tutup *sidebar* pada *mobile*, *bottom nav bar*
- Tombol *refresh* untuk pembaruan data manual

***User Flow***:
Klien *login* → ***Dashboard*** → Gambaran umum semua data → Tindakan cepat atau navigasi ke bagian tertentu

---

#### B. *Booking* Langkah 1 - Pilih Layanan (*Booking Step 1 - Select Service*)

**Deskripsi:**
Langkah pertama dalam alur *booking* di mana klien memilih layanan hipnoterapi yang ingin mereka *booking*. Halaman ini harus memudahkan penelusuran (*browsing*) dan perbandingan (*comparison*) antar layanan.

**Elemen Utama:**
1. **Indikator Kemajuan (*Progress Indicator*)**:
   - *Stepper* di atas menampilkan 4 langkah:
     * Langkah 1: *Select Service* (aktif, disorot)
     * Langkah 2: *Choose Therapist* (tidak aktif)
     * Langkah 3: *Select Date & Time* (tidak aktif)
     * Langkah 4: *Confirm & Pay* (tidak aktif)
   - Garis penghubung visual antar langkah

2. **Header Halaman (*Page Header*)**:
   - Judul: "Book Your Session"
   - ***Breadcrumb***: *Dashboard* > *Book Session* > *Select Service*

3. **Bagian Pencarian & Filter (*Search & Filter Section*)**:
   - *Search bar*: "Search services..."
   - *Dropdown* filter:
     * Kategori (*All*, *Stress*, *Addiction*, *Phobia*, dll.)
     * Durasi (*Any*, 30 menit, 60 menit, 90 menit)
     * Rentang Harga (*slider*: Rp 0 - Rp 500K)
   - Tautan "Clear Filters"

4. **Grid Layanan (*Services Grid*)**:
   - Tata letak 2-3 kolom
   - Setiap kartu layanan:
     * Ikon/ilustrasi layanan
     * Nama layanan (H3)
     * Lencana kategori
     * Deskripsi singkat (2-3 baris)
     * Lencana durasi (mis., "60 menit")
     * Harga (menonjol): "Rp 300.000"
     * Bintang *rating* + jumlah ulasan
     * Tautan "View Details" (buka *modal* atau *accordion*)
     * **Tombol "Select"** (primer)
   
   - Keadaan terpilih (*selected state*):
     * Kartu disorot dengan batas merah muda
     * Ikon tanda centang
     * Lencana "Selected"
     * Tombol berubah menjadi "Change"

5. ***Modal/Accordion* Detail Layanan (*Service Details Modal/Accordion*)**:
   - Info diperluas saat "View Details":
     * Deskripsi lengkap
     * Apa yang termasuk (*What's included*)
     * Manfaat (*Benefits*)
     * Jumlah sesi yang direkomendasikan
     * Spesialisasi terapis yang dibutuhkan
     * FAQ untuk layanan ini

6. **Sorotan Layanan Populer (*Popular Services Highlight*)**:
   - Lencana "Most Popular" pada layanan teratas
   - Bagian "Recommended for You" berdasarkan profil

7. **Bagian Bantuan (*Help Section*)**:
   - *Sidebar* atau tombol melayang (*floating button*):
     * "Not sure which service?"
     * Tombol "Take Assessment"
     * Tombol "Chat with Consultant"

8. **Navigasi (*Navigation*)**:
   - Tautan "Back to Dashboard"
   - **Tombol "Continue"** (kanan bawah, *sticky*):
     * *Disabled* hingga layanan dipilih
     * Menampilkan nama layanan terpilih saat diaktifkan
     * Klik → Pergi ke Langkah 2

**Interaksi & Perilaku:**
- Pemilihan tunggal (*single selection*) (perilaku tombol radio)
- Filter hasil waktu nyata (*real-time*)
- Pencarian dengan *debounce*
- Pemilihan kartu dengan umpan balik visual
- Animasi halus *modal/accordion*
- *Mobile*: Tumpuk kartu vertikal, tombol *continue* *sticky*

***User Flow***:
Klien → *Book Session* → Langkah 1 → Telusuri layanan → Pilih satu → Klik "Continue" → Langkah 2

---

#### C. *Booking* Langkah 2 - Pilih Terapis (*Booking Step 2 - Choose Therapist*)

**Deskripsi:**
Langkah kedua di mana klien memilih terapis yang akan melakukan sesi. Halaman ini memfilter terapis berdasarkan spesialisasi dari layanan yang dipilih di Langkah 1.

**Elemen Utama:**
1. ***Progress Stepper***:
   - Langkah 1: ✓ *Select Service* (selesai, tanda centang hijau)
   - Langkah 2: *Choose Therapist* (aktif)
   - Langkah 3: *Select Date & Time* (tidak aktif)
   - Langkah 4: *Confirm & Pay* (tidak aktif)

2. **Tampilan Layanan Terpilih (*Selected Service Display*)**:
   - *Sticky top bar* atau kartu:
     * Nama layanan
     * Harga, durasi
     * Tautan "Change Service" (kembali ke Langkah 1)

3. **Bagian Filter & Urutkan (*Filter & Sort Section*)**:
   - **Filter**:
     * Preferensi jenis kelamin (*Any*, Laki-laki, Perempuan)
     * Pengalaman (0-3 tahun, 3-5, 5-10, 10+)
     * *Rating* (4+ bintang, 4.5+, 5 saja)
     * Ketersediaan (*Available Today*, *This Week*, Tanggal Spesifik)
     * Bahasa (Indonesia, Inggris, dll.)
     * Rentang Harga (tampilkan biaya konsultasi terapis)
   
   - **Urutkan (*Sort*)**:
     * *Dropdown*: Direkomendasikan, *Rating* Tertinggi, Paling Berpengalaman, Tersedia Paling Cepat, Harga Rendah-Tinggi

4. **Daftar Terapis (*Therapists List*)**:
   - Tata letak kartu, daftar vertikal atau *grid*
   - Setiap kartu terapis:
     * Foto profil (besar, profesional)
     * Nama (H3)
     * Gelar/Kredensial (mis., "Clinical Hypnotherapist, CHT")
     * *Tag* spesialisasi (2-3 utama)
     * Tahun pengalaman
     * Bintang *rating* + jumlah ulasan
     * Bahasa yang dikuasai
     * Jumlah sesi yang selesai
     * **Indikator ketersediaan (*Availability indicator*)**:
       - "Available Today" (lencana hijau)
       - "Next available: Tomorrow" (oranye)
       - "Book in Advance" (abu-abu)
     * **Harga**: "From Rp 250K per session"
     * **Tautan "View Profile"** (buka *modal* atau halaman baru)
     * **Tombol "Select Therapist"** (primer)

5. ***Modal* Profil Terapis (*Therapist Profile Modal*)**:
   - *Modal* tampilan cepat saat "View Profile":
     * Foto lengkap
     * Bio terperinci
     * Pendidikan & sertifikasi
     * Pendekatan terapi
     * Testimoni klien (2-3)
     * Tombol "Select This Therapist"

6. **Keadaan Terpilih (*Selected State*)**:
   - Kartu terapis terpilih disorot
   - Batas merah muda, tanda centang
   - Kartu lain sedikit redup
   - Info terapis terpilih di *sticky bar*

7. **Opsi Tanpa Preferensi (*No Preference Option*)**:
   - *Checkbox*: "I don't have a preference, assign me any available therapist"
   - Pilih otomatis berdasarkan ketersediaan

8. **Fitur Perbandingan (*Comparison Feature*)** (opsional):
   - Tombol "Compare Therapists"
   - Pilih beberapa (2-3) terapis
   - Tabel perbandingan berdampingan (*side-by-side*)

**Navigasi (*Navigation*)**:
- Tombol "← Back" (kembali ke Langkah 1)
- **Tombol "Continue"** (*sticky* bawah):
  * *Disabled* hingga terapis dipilih
  * Menampilkan nama terapis terpilih
  * Klik → Pergi ke Langkah 3

**Interaksi & Perilaku:**
- Filter/*sort* dengan transisi halus
- Mode pemilihan tunggal (*single selection*)
- *Modal* profil dengan *slideshow* untuk foto
- Kartu responsif
- *Loading state* untuk data *async*

***User Flow***:
Langkah 2 → Telusuri terapis → Filter/*sort* → Lihat profil → Pilih terapis → *Continue* → Langkah 3

---

#### D. Booking Step 3 - Select Date & Time

**Deskripsi:**
Step ketiga di mana client memilih tanggal dan waktu untuk session mereka berdasarkan availability therapist yang dipilih.

**Elemen Utama:**
---

#### D. *Booking* Langkah 3 - Pilih Tanggal & Waktu (*Booking Step 3 - Select Date & Time*)

**Deskripsi:**
Langkah ketiga di mana klien memilih tanggal dan waktu untuk sesi mereka berdasarkan ketersediaan terapis yang dipilih.

**Elemen Utama:**
1. ***Progress Stepper***:
   - Langkah 1: ✓ Selesai
   - Langkah 2: ✓ Selesai
   - Langkah 3: *Select Date & Time* (aktif)
   - Langkah 4: *Confirm & Pay* (tidak aktif)

2. **Kartu Ringkasan *Booking* (*Booking Summary Card*)**:
   - *Sidebar sticky* (*desktop*) atau kartu atas (*mobile*):
     * Nama layanan + ikon
     * Foto terapis + nama
     * Harga per sesi
     * Durasi
     * Tautan "Edit" untuk mengubah layanan/terapis

3. **Pemilihan Tipe Sesi (*Session Type Selection*)**:
   - Tombol radio:
     * **Sesi *Online*** (*Video Call*)
       - Ikon: Kamera
       - Deskripsi: "Connect from anywhere"
     * **Sesi *Offline*** (Tatap Muka)
       - Ikon: Penanda lokasi
       - Deskripsi: "Visit our clinic"
       - Tampilkan alamat klinik
   - Opsi terpilih disorot

4. **Komponen Kalender (*Calendar Component*)**:
   - Tampilan bulan (*month view*)
   - Navigasi: < Bulan Sebelumnya | Bulan Saat Ini | Bulan Berikutnya >
   - Visualisasi tanggal:
     * Hari ini: Garis tepi disorot
     * Tanggal tersedia: Dapat diklik, keadaan normal
     * Tanggal penuh: *Disabled*, abu-abu
     * Tanggal terpilih: Latar belakang merah muda, teks putih
     * Tanggal lampau: *Disabled*
   - Klik tanggal → Muat slot waktu tersedia

5. **Bagian Slot Waktu (*Time Slots Section*)**:
   - Muncul setelah tanggal dipilih
   - Judul: "Available time slots for [Tanggal Terpilih]"
   - Tata letak *grid* atau daftar slot waktu:
     * Setiap slot: "09:00 AM - 10:00 AM"
     * Indikator status:
       - Tersedia (latar belakang putih, batas)
       - Terpilih (latar belakang merah muda)
       - Dipesan (abu-abu, *disabled*)
   - Durasi slot berdasarkan layanan (mis., slot 60 menit)

6. **Info Zona Waktu (*Time Zone Info*)**:
   - Tampilan: "Times shown in: Jakarta (WIB) GMT+7"
   - *Dropdown* untuk mengubah zona waktu (untuk sesi *online*)

7. **Tersedia Paling Awal (*Earliest Available*)**:
   - Tombol tindakan cepat: "Book Earliest Available"
   - Pilih otomatis slot tersedia pertama

8. **Catatan Sesi (*Session Notes*)** (opsional):
   - *Textarea*: "Any specific concerns or topics you'd like to address?"
   - Batas karakter: 500 karakter
   - Teks pembantu: "This helps your therapist prepare for your session"

9. **Pesan Validasi (*Validation Messages*)**:
   - Jika tidak ada slot tersedia: "No available slots for this date. Please choose another date."
   - *Loading state*: "Loading available slots..."

**Navigasi (*Navigation*)**:
- Tombol "← Back" (kembali ke Langkah 2)
- **Tombol "Continue"** (*sticky* bawah):
  * *Disabled* hingga tanggal & waktu dipilih
  * Menampilkan tanggal & waktu terpilih
  * Klik → Pergi ke Langkah 4

**Interaksi & Perilaku:**
- Klik tanggal kalender → Muat slot (panggilan API)
- Pemilihan slot waktu (*single select*)
- Pemeriksaan ketersediaan waktu nyata
- *Skeleton loading* untuk slot
- *Mobile*: Navigasi kalender *swipe*
- *Auto-refresh* ketersediaan setiap 60 detik

***User Flow***:
Langkah 3 → Pilih tipe sesi → Pilih tanggal dari kalender → Pilih slot waktu → Tambah catatan (opsional) → *Continue* → Langkah 4
---

#### E. *Booking* Langkah 4 - Konfirmasi & Pembayaran (*Booking Step 4 - Confirm & Payment*)

**Deskripsi:**
Langkah terakhir dalam alur *booking* di mana klien meninjau detail *booking*, memilih metode pembayaran, dan mengkonfirmasi pembayaran.

**Elemen Utama:**
1. ***Progress Stepper***:
   - Langkah 1: ✓ Selesai
   - Langkah 2: ✓ Selesai
   - Langkah 3: ✓ Selesai
   - Langkah 4: *Confirm & Pay* (aktif)

2. **Kartu Ringkasan *Booking* (*Booking Summary Card*)** (Menonjol):
   - Judul: "Review Your Booking"
   - Bagian:
     * **Detail Layanan (*Service Details*)**:
       - Nama layanan
       - Kategori
       - Durasi
       - Tautan "Edit"
     
     * **Detail Terapis (*Therapist Details*)**:
       - Foto + nama
       - Spesialisasi
       - Tautan "Edit"
     
     * **Detail Sesi (*Session Details*)**:
       - Tanggal: "Monday, November 4, 2024"
       - Waktu: "3:00 PM - 4:00 PM (WIB)"
       - Tipe sesi: *Online*/*Offline*
       - Lokasi (jika *offline*): Alamat
       - Tautan "Edit"
     
     * **Catatan (*Notes*)**:
       - Tampilkan catatan klien
       - Tautan "Edit"

3. **Kartu Rincian Harga (*Pricing Breakdown Card*)**:
   - Daftar terperinci:
     * Biaya layanan: Rp 300.000
     * Biaya platform: Rp 5.000
     * Diskon (jika ada): - Rp 30.000 (kode promo)
     * **Total**: Rp 275.000 (besar, tebal)

4. **Bagian Kode Promo (*Promo Code Section*)**:
   - Kolom input: "Enter promo code"
   - Tombol "Apply"
   - Sukses: "Promo code applied! You saved Rp 30.000"
   - Kesalahan: "Invalid or expired promo code"

5. **Pemilihan Metode Pembayaran (*Payment Method Selection*)**:
   - Judul: "Choose Payment Method"
   - Opsi radio dengan kartu:
     * ***Bank Transfer***:
       - Ikon: BCA, Mandiri, BNI, BRI
       - Deskripsi: "Pay via bank transfer"
     
     * ***E-Wallet***:
       - Ikon: GoPay, OVO, Dana, ShopeePay
       - Deskripsi: "Instant payment"
     
     * **Kartu Kredit/Debit (*Credit/Debit Card*)**:
       - Ikon: Visa, Mastercard
       - Deskripsi: "Secure card payment"
     
     * ***Virtual Account***:
       - Deskripsi: "Generate VA number"

6. **Persetujuan Syarat (*Terms Agreement*)**:
   - *Checkbox* (wajib):
     * "I agree to the Booking Terms & Conditions"
     * "I agree to the Cancellation Policy"
       - Tautan: Lihat kebijakan (*modal*)
     * "I consent to sharing my health information with the therapist"

7. **Tombol Tindakan (*Action Buttons*)**:
   - **Tombol "Confirm & Pay"** (primer, besar):
     * *Disabled* hingga metode pembayaran dipilih & syarat disetujui
     * Menampilkan jumlah total: "Pay Rp 275.000"
   - Tombol "Save as Draft" (sekunder):
     * Simpan *booking* untuk diselesaikan nanti
   - Tautan "Cancel Booking"

8. **Indikator Keamanan (*Security Indicators*)**:
   - Ikon: Gembok SSL, Lencana pembayaran aman
   - Teks: "Your payment is secure and encrypted"
   - Logo pemroses pembayaran (*Midtrans*, dll.)

9. **Ringkasan Kebijakan Pembatalan (*Cancellation Policy Summary*)**:
   - Bagian yang dapat ditutup atau kotak info:
     * "Cancel 24+ hours before: Full refund"
     * "Cancel 12-24 hours: 50% charge"
     * "Cancel <12 hours: No refund"

**Alur Pembayaran Setelah Konfirmasi (*Payment Flow After Confirm*)**:
- Klik "Confirm & Pay" → Arahkan ke *payment gateway* (*Midtrans*)
- Opsi pembayaran disajikan
- Pengguna menyelesaikan pembayaran
- Arahkan kembali ke CUR-HEART dengan status

**Keadaan Sukses (*Success State*) (Halaman Berikutnya)**:
- Arahkan ke halaman *Booking Success*
- Tampilkan konfirmasi *booking*
- Kirim email konfirmasi

**Interaksi & Perilaku:**
- Validasi kode promo waktu nyata
- Pemilihan metode pembayaran memperbarui UI
- Validasi *checkbox* syarat
- *Overlay loading* saat memproses pembayaran
- Penanganan kesalahan untuk pembayaran gagal
- Peringatan *timeout* sesi

***User Flow***:
Langkah 4 → Tinjau semua detail → Masukkan promo (opsional) → Pilih pembayaran → Setuju syarat → *Confirm & Pay* → *Payment gateway* → Pembayaran berhasil → Halaman *Booking Success*

---

#### F. Booking Success Page

---

#### F. Halaman Sukses *Booking* (*Booking Success Page*)

**Deskripsi:**
Halaman *Booking Success* ditampilkan setelah pembayaran berhasil. Halaman ini memberikan konfirmasi *booking* dan informasi tentang langkah berikutnya (*next steps*).

**Elemen Utama:**
1. **Animasi Sukses (*Success Animation*)**:
   - Ikon tanda centang besar dengan animasi (*scale in*, *check draw*)
   - Animasi konfeti (*confetti*) (perayaan singkat)

2. **Pesan Sukses (*Success Message*)**:
   - Judul: "Booking Confirmed! 🎉"
   - Subjudul: "Your session has been successfully booked"

3. **Kartu Detail *Booking* (*Booking Details Card*)**:
   - Judul "*Booking Confirmation*"
   - **ID *Booking***: #BK-2024-00123 (tombol salin)
   - Nama layanan
   - Terapis: Nama + foto
   - Tanggal & Waktu (besar, menonjol)
   - Durasi
   - Tipe Sesi (*Online*/*Offline*)
   - Lokasi (jika *offline*)
   - Total Dibayar: Rp 275.000
   - Metode Pembayaran

4. **Bagian Langkah Berikutnya (*Next Steps Section*)**:
   - Judul: "What's Next?"
   - Daftar bernomor:
     1. "You'll receive a confirmation email shortly"
     2. "For online sessions, join link will be sent 15 minutes before"
     3. "Prepare any questions or concerns for your therapist"
     4. "Arrive/join 5 minutes early"

5. **Tombol Tindakan (*Action Buttons*)**:
   - "View Appointment Details" (primer)
   - "Add to Calendar" (dengan *dropdown*: Google, Outlook, iCal)
   - "Download Invoice" (PDF)
   - "Share Booking" (opsional)

6. **Tips Persiapan (*Preparation Tips*)**:
   - "Tips for Your First Session"
   - 3-4 poin *bullet*:
     * Find a quiet, comfortable space
     * Have a glass of water nearby
     * Wear comfortable clothing
     * Arrive with an open mind

7. **Hubungi Dukungan (*Contact Support*)**:
   - "Need to change your booking?"
   - Tombol "Contact Support"
   - Tautan "View Cancellation Policy"

8. **Tindakan Terkait (*Related Actions*)**:
   - Tombol "Book Another Session"
   - "Invite a Friend" (program rujukan)

9. **Pemberitahuan Email Konfirmasi (*Confirmation Email Notice*)**:
   - Kotak info: "📧 Confirmation email sent to [email]"
   - "Didn't receive? Check spam or resend"

**Interaksi & Perilaku:**
- Animasi konfeti saat dimuat (*once*)
- Salin ID *booking* ke *clipboard*
- Tambahkan ke kalender menghasilkan file *.ics*
- Unduh faktur (pembuatan PDF)
- *Auto-redirect* ke *appointments* setelah 30 detik (opsional, dengan *countdown*)

***User Flow***:
Halaman *Booking Success* → Lihat detail / Unduh faktur / Tambahkan ke kalender → Kembali ke ***Dashboard*** atau Lihat *Appointments*

---

#### G. Daftar Janji Temu Saya (*My Appointments List*)

**Deskripsi:**
Halaman *My Appointments* menampilkan daftar lengkap semua janji temu (*appointments*) klien, baik mendatang (*upcoming*), lampau (*past*), maupun dibatalkan (*cancelled*). Halaman ini memungkinkan klien untuk mengelola janji temu mereka.

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "My Appointments"
   - ***Breadcrumb***: *Dashboard* > *My Appointments*

2. **Navigasi *Tab* (*Tabs Navigation*)**:
   - *Tab* horizontal:
     * ***Upcoming*** (default, lencana dengan jumlah)
     * ***Past***
     * ***Cancelled***
   - *Tab* aktif disorot

3. **Bagian Filter & Urutkan (*Filter & Sort Section*)**:
   - *Search bar*: "Search by service or therapist..."
   - *Dropdown* filter:
     * Rentang Tanggal (*This Week*, *This Month*, *Last 3 Months*, *Custom Range*)
     * Tipe Layanan (*All*, *Stress Management*, *Weight Loss*, dll.)
     * Tipe Sesi (*All*, *Online*, *Offline*)
     * Status (*All*, *Confirmed*, *Pending Payment*, *Completed*, *Cancelled*)
   - Urutkan: Tanggal (Terbaru/Terlama), Nama Layanan A-Z

4. **Daftar Janji Temu (*Appointments List*)** (*Tab Upcoming*):
   - Tata letak daftar berbasis kartu
   - Setiap kartu janji temu:
     * **Bagian Kiri (*Left Section*)**:
       - Lencana tanggal (vertikal: Singkatan bulan + Nomor hari)
       - Waktu (mulai - selesai)
     
     * **Bagian Tengah (*Middle Section*)**:
       - Nama layanan (H4)
       - Terapis: Foto + Nama
       - Lencana tipe sesi (*Online*/*Offline*)
       - Durasi: 60 menit
       - Lokasi (jika *offline*): Alamat
       - Lencana status (*Confirmed*/*Pending*/dll.)
     
     * **Bagian Kanan (*Right Section*)** (Tindakan):
       - *Timer countdown* (jika dalam 24 jam): "Starts in 2h 30m"
       - **Tombol "Join Session"** (primer, jika *online* & dalam 15 menit)
       - **Tombol "View Details"**
       - Menu *dropdown* (3 titik):
         * *Reschedule*
         * *Cancel Appointment*
         * *Add to Calendar*
         * *Download Invoice*
         * *Contact Therapist*

5. **Keadaan Kosong (*Empty States*)**:
   - **Tidak Ada Janji Temu Mendatang (*No Upcoming Appointments*)**:
     * Ilustrasi: Kalender dengan tanda centang
     * Pesan: "You don't have any upcoming appointments"
     * Tombol "Book Your First Session"
   
   - **Tidak Ada Janji Temu Lampau (*No Past Appointments*)**:
     * Pesan: "Your appointment history will appear here"
   
   - **Tidak Ada Janji Temu Dibatalkan (*No Cancelled Appointments*)**:
     * Pesan: "No cancelled appointments"

6. **Janji Temu Lampau (*Past Appointments*)** (*Tab Past*):
   - Tata letak kartu serupa
   - Elemen tambahan:
     * Lencana penyelesaian
     * Tombol "Leave a Review" (jika belum diulas)
     * Tindakan cepat "Book Again with [Terapis]"
     * Pratinjau catatan sesi (jika tersedia)

7. **Janji Temu Dibatalkan (*Cancelled Appointments*)** (*Tab Cancelled*):
   - Menampilkan janji temu yang dibatalkan
   - Info pembatalan:
     * Dibatalkan oleh: Klien/Terapis/Sistem
     * Tanggal pembatalan
     * Alasan (jika diberikan)
     * Status pengembalian dana (*Full*/*Partial*/*None*)
   - Tombol "Book New Session"

8. **Paginasi (*Pagination*)**:
   - Paginasi bawah: *Previous* | 1 2 3 ... 10 | *Next*
   - Item per halaman: 10 (dapat dikonfigurasi)

9. **Tindakan Massal (*Bulk Actions*)** (opsional):
   - Pilih beberapa janji temu
   - Ekspor massal ke kalender
   - Unduh faktur massal

**Interaksi & Perilaku:**
- Pembaruan waktu nyata (*real-time updates*) untuk perubahan status
- *Timer countdown* diperbarui setiap menit
- Hasil filter/pencarian dengan transisi halus
- *Skeleton loading* untuk janji temu
- Tarik untuk segarkan (*pull to refresh*) (*mobile*)
- *Infinite scroll* atau paginasi

***User Flow***:
Klien → *My Appointments* → Telusuri daftar → Lihat detail atau ambil tindakan (*join*/*reschedule*/*cancel*)

---

#### H. Halaman Detail Janji Temu (*Appointment Detail Page*)

**Deskripsi:**
Halaman *Appointment Detail* menampilkan informasi lengkap tentang satu janji temu spesifik, termasuk semua detail, status, dan tindakan yang tersedia (*available actions*).

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Tombol kembali: "← Back to Appointments"
   - ID *Booking*: #BK-2024-00123
   - Lencana status (besar): *Confirmed*/*Completed*/*Cancelled*

2. **Kartu Ringkasan Janji Temu (*Appointment Summary Card*)**:
   - **Bagian Tanggal & Waktu (*Date & Time Section*)**:
     * Tampilan tanggal besar: "Monday, November 4, 2024"
     * Waktu: "3:00 PM - 4:00 PM (WIB)"
     * *Countdown* (jika mendatang): "In 2 days, 5 hours"
     * Tombol *Add to Calendar*
   
   - **Detail Layanan (*Service Details*)**:
     * Nama layanan (H3)
     * Lencana kategori
     * Durasi: 60 menit
     * Harga: Rp 300.000
     * Tipe sesi: Lencana *Online*/*Offline*
   
   - **Informasi Terapis (*Therapist Information*)**:
     * Foto profesional (besar)
     * Nama (H4)
     * Kredensial
     * Spesialisasi
     * Tautan "View Profile"
     * Tombol "Send Message"

3. **Lokasi/Tautan Sesi (*Session Location/Link*)**:
   - **Jika *Online***:
     * Bagian tautan pertemuan (muncul 15 menit sebelumnya)
     * Tombol "Join Video Session" (primer, besar)
     * ID & *Password* Pertemuan
     * Instruksi: "Please join 5 minutes early"
     * *Checklist* persyaratan teknis
   
   - **Jika *Offline***:
     * Alamat lengkap
     * Tombol "Get Directions" (*Google Maps*)
     * Nomor telepon kontak
     * Informasi parkir

4. **Bagian Catatan Anda (*Your Notes Section*)**:
   - Tampilkan catatan yang diajukan klien saat *booking*
   - Dapat diedit (hingga 24 jam sebelum sesi)
   - Tombol "Edit Notes"
   - Jumlah karakter

5. **Informasi Pembayaran (*Payment Information*)**:
   - Lencana status pembayaran: *Paid*/*Pending*
   - **Rincian (*Breakdown*)**:
     * Biaya layanan
     * Biaya platform
     * Diskon (jika ada)
     * Total dibayar
   - Metode pembayaran yang digunakan
   - ID Transaksi
   - Tanggal & waktu pembayaran
   - Tombol "Download Invoice" (PDF)
   - Tautan "Request Receipt"

6. ***Timeline* Riwayat *Booking* (*Booking History Timeline*)**:
   - *Timeline* vertikal menampilkan:
     * *Booking* dibuat (tanggal & waktu)
     * Pembayaran selesai
     * Dikonfirmasi oleh terapis
     * Pengingat dikirim
     * Sesi selesai (jika lampau)
     * Ulasan dikirimkan (jika ada)

7. **Bagian Tindakan (*Actions Section*)**:
   - **Untuk Janji Temu Mendatang (*For Upcoming Appointments*)**:
     * Tombol "Reschedule Appointment"
       - *Modal*: Pilih tanggal/waktu baru
       - Tampilkan kebijakan *reschedule*
     * Tombol "Cancel Appointment"
       - *Modal*: Konfirmasi pembatalan
       - Tampilkan kebijakan pengembalian dana
       - Pemilihan alasan (*dropdown*)
       - *Textarea* catatan
     * Tombol "Contact Therapist"
   
   - **Untuk Janji Temu Lampau (*For Past Appointments*)**:
     * Tombol "Leave a Review" (jika belum diulas)
     * "View Session Notes" (jika terapis berbagi)
     * Tombol "Book Again"
     * "Download Report" (jika tersedia)

8. **Catatan Sesi (*Session Notes*)** (Setelah Sesi):
   - Terlihat setelah sesi selesai
   - Catatan terapis (jika dibagikan dengan klien)
   - *Homework*/rekomendasi
   - Saran sesi berikutnya

9. **Bagian Ulasan (*Review Section*)** (Jika Diulas):
   - Ulasan klien ditampilkan:
     * Bintang *rating*
     * Teks ulasan
     * Tanggal dikirimkan
   - Opsi "Edit Review"

10. **Kotak Kebijakan Pembatalan (*Cancellation Policy Box*)**:
    - Kotak info dengan ringkasan kebijakan
    - *Countdown* untuk batas waktu pembatalan gratis
    - Tautan "View Full Policy"

11. **Bagian Dukungan (*Support Section*)**:
    - Tombol "Need Help?"
    - Tautan FAQ spesifik untuk janji temu
    - Hubungi dukungan

**Interaksi & Perilaku:**
- Pembaruan status waktu nyata
- *Timer countdown*
- Tombol *join* muncul 15 menit sebelum sesi
- Konfirmasi *modal* untuk tindakan
- Validasi formulir untuk *reschedule*/*cancel*
- *Auto-refresh* sebelum waktu sesi

***User Flow***:
*Appointments List* → Klik janji temu → Halaman detail → Lihat info / Ambil tindakan (*join*/*reschedule*/*cancel*/*review*)

---

#### I. ***Dashboard*** Pelacakan Kemajuan Klien (*Client Progress Tracking Dashboard*)

**Deskripsi:**
Halaman *Progress Tracking* membantu klien melihat perkembangan mereka dalam perjalanan terapi (*therapy journey*). Halaman ini menampilkan metrik, grafik, dan wawasan (*insights*) tentang kemajuan kesejahteraan (*wellness progress*) mereka.

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "My Progress"
   - Subjudul: "Track your wellness journey"
   - ***Breadcrumb***: *Dashboard* > *My Progress*
   - Pemilih rentang tanggal: *Last 30 Days*, 3 Bulan, 6 Bulan, 1 Tahun, *All Time*

2. **Kartu Ringkasan Kemajuan (*Progress Overview Cards*)**:
   - 4 kartu metrik dalam baris:
     * **Total Sesi (*Total Sessions*)**: Angka + tren
     * **Tingkat Penyelesaian (*Completion Rate*)**: Persentase + *progress bar*
     * **Pencapaian Tujuan (*Goal Achievement*)**: X dari Y tujuan selesai
     * **Skor Kesejahteraan (*Wellness Score*)**: 78/100 + indikator tren

3. **Grafik Skor Kesejahteraan (*Wellness Score Chart*)**:
   - Kartu besar: "Your Wellness Score Over Time"
   - Grafik garis menampilkan perkembangan skor kesejahteraan
   - Sumbu-X: *Timeline* (minggu/bulan)
   - Sumbu-Y: Skor (0-100)
   - Titik data: Dapat diklik untuk detail
   - Garis tren (*overlay*)
   - Garis tujuan (skor target)
   - Kode warna: Meningkat (hijau), Menurun (merah), Stabil (biru)

4. **Grafik Kehadiran Sesi (*Session Attendance Chart*)**:
   - Grafik batang atau *heatmap* kalender
   - Menampilkan frekuensi sesi
   - Intensitas warna berdasarkan sesi per minggu
   - *Tooltip* dengan detail sesi

5. **Bagian Tujuan & Pencapaian (*Goals & Milestones Section*)**:
   - Judul: "Your Goals"
   - Daftar tujuan yang ditetapkan dengan terapis:
     * Deskripsi tujuan
     * *Progress bar* (0-100%)
     * Tanggal target
     * Status saat ini (*In Progress*/*Achieved*/*Overdue*)
     * Catatan
   - Tombol "Add New Goal"
   - Tujuan selesai ditutup atau *tab* terpisah

6. **Pelacakan Suasana Hati (*Mood Tracking*)**:
   - "How Have You Been Feeling?"
   - Grafik garis/area:
     * Sumbu-X: Tanggal
     * Sumbu-Y: Skor suasana hati (1-10)
     * Metrik ganda: Kecemasan, Stres, Kebahagiaan, Energi
     * *Toggle* untuk tampilkan/sembunyikan metrik
   - Perbandingan rata-rata mingguan

7. **Statistik Ringkasan Sesi (*Session Summary Statistics*)**:
   - Tabel atau daftar:
     * Total sesi yang dihadiri
     * Layanan paling sering
     * Terapis favorit
     * Rata-rata *rating* sesi
     * Total jam yang dihabiskan
     * *Streak* terpanjang
     * *Streak* saat ini

8. **Pencapaian & Lencana (*Achievements & Badges*)**:
   - Elemen gamifikasi:
     * Lencana "First Session"
     * Lencana "5 Sessions Milestone"
     * Lencana "30-Day Streak"
     * Lencana "Goal Achiever"
   - *Progress bar* untuk lencana berikutnya

9. **Ringkasan Catatan Terapis (*Therapist Notes Summary*)**:
   - Bagian yang dapat ditutup
   - Catatan teragregasi dari terapis
   - Rekomendasi
   - Pelacakan penyelesaian *homework*

10. **Laporan Kemajuan (*Progress Reports*)**:
    - "Monthly Progress Report"
    - Unduh sebagai PDF
    - Opsi email laporan
    - Bagikan dengan terapis

11. **Metrik Perbandingan (*Comparison Metrics*)**:
    - "You vs Your Goals"
    - "This Month vs Last Month"
    - Persentase peningkatan

12. **Wawasan & Rekomendasi (*Insights & Recommendations*)**:
    - Wawasan yang dihasilkan AI (opsional):
      * "You're doing great! Your mood has improved 25% this month"
      * "Consider booking more stress management sessions"
      * "Your goal completion rate is above average!"

13. **Tindakan Cepat (*Quick Actions*)**:
    - Tombol "Book Next Session"
    - Tombol "Set New Goal"
    - Tombol "Update Mood" (*daily check-in*)

**Interaksi & Perilaku:**
- Grafik interaktif (*hover* untuk *tooltip*, klik untuk *drill-down*)
- Pemilih rentang tanggal memperbarui semua grafik
- Animasi halus untuk rendering grafik
- Ekspor data sebagai CSV/PDF
- Grafik responsif (beradaptasi ke *mobile*)
- Pembaruan waktu nyata saat data baru tersedia

***User Flow***:
Klien → *My Progress* → Lihat grafik & metrik → Identifikasi tren → Ambil tindakan (*book* sesi, perbarui tujuan)

---

#### J. Pesan Klien (*Client Messages*) (*Chat* dengan Terapis)

**Deskripsi:**
Halaman *Messages* memungkinkan klien untuk berkomunikasi dengan terapis mereka melalui antarmuka *chat*. Ini penting untuk pertanyaan lanjutan (*follow-up questions*), koordinasi janji temu, dan dukungan berkelanjutan (*ongoing support*).

**Elemen Utama:**
1. **Tata Letak Halaman (*Page Layout*)**:
   - Tampilan terpisah (*split view*) (*desktop*):
     * *Sidebar* kiri (30%): Daftar percakapan
     * Area utama kanan (70%): Percakapan aktif
   - Tampilan tunggal (*mobile*): Beralih Daftar ↔ Percakapan

2. ***Sidebar* Daftar Percakapan (*Conversations List Sidebar*)**:
   - Header:
     * Judul: "Messages"
     * *Search bar*: "Search conversations..."
     * Tombol pesan baru (*compose*)
   
   - Item percakapan:
     * *Avatar* terapis
     * Nama terapis
     * Pratinjau pesan terakhir (dipotong)
     * *Timestamp* (relatif: "2h ago", "Yesterday")
     * Lencana jumlah belum dibaca (jika ada)
     * Indikator status *online* (titik hijau)
     * Opsi sematkan (*pin*) (untuk *chat* penting)
   
   - Diurutkan berdasarkan: Terbaru di atas
   - Keadaan kosong: "No messages yet. Book a session to start chatting!"

3. **Area Percakapan Aktif (*Active Conversation Area*)**:
   - **Header**:
     * *Avatar* terapis + nama
     * Status *online* ("Active now" / "Last seen 2h ago")
     * Tindakan:
       - Ikon panggilan video (jika selama waktu sesi)
       - Ikon panggilan telepon
       - Ikon info (lihat profil terapis)
       - Menu lainnya (*mute*, laporkan, blokir)
   
   - ***Thread* Pesan (*Message Thread*)**:
     * Pesan ditampilkan secara kronologis
     * Pemisah tanggal ("Today", "Yesterday", "Oct 25, 2024")
     * **Pesan masuk (*Incoming messages*)** (terapis):
       - *Avatar* di kiri
       - Gelembung pesan (latar belakang abu-abu)
       - *Timestamp* di bawah
       - Status dibaca (jika diaktifkan)
     
     * **Pesan keluar (*Outgoing messages*)** (klien):
       - Sejajar kanan
       - Gelembung pesan (latar belakang merah muda)
       - *Timestamp*
       - Indikator status:
         * Terkirim (tanda centang tunggal)
         * Tersampaikan (tanda centang ganda)
         * Dibaca (tanda centang ganda biru)
     
     * **Tipe pesan yang didukung (*Message types supported*)**:
       - Pesan teks
       - Emoji
       - Gambar (dengan pratinjau)
       - File (PDF, dokumen) dengan tautan unduh
       - Pesan suara (tombol *play*)
       - Balasan cepat (*quick replies*) (tombol)
     
     * Tombol *scroll* ke bawah (muncul saat di-*scroll* ke atas)
   
   - **Area Input (*Input Area*)**:
     * Kolom input teks (*multiline*)
     * *Placeholder*: "Type a message..."
     * Tindakan kiri:
       - Ikon pemilih emoji
       - Ikon lampiran (unggah file/gambar)
       - Ikon rekam suara (tahan untuk merekam)
     * Tindakan kanan:
       - Tombol kirim (ikon, *disabled* saat kosong)
     * Penghitung karakter (opsional)
     * Indikator mengetik: "Therapist is typing..."

4. **Keadaan Percakapan Kosong (*Empty Conversation State*)**:
   - Saat tidak ada percakapan dipilih:
     * Ilustrasi
     * "Select a conversation to start messaging"
     * Atau: Tombol "Start a New Conversation"

5. **Respons Cepat (*Quick Responses*)** (Opsional):
   - Respons yang disarankan:
     * "Thank you"
     * "Yes, I'll be there"
     * "Can we reschedule?"
     * "I have a question"

6. **Pesan Otomatis (*Automated Messages*)**:
   - Pesan sistem dalam percakapan:
     * "Booking confirmed for Nov 4 at 3:00 PM"
     * "Session completed. Leave a review?"
     * Pengingat janji temu
   - Gaya berbeda (abu-abu, miring)

7. ***Sidebar* Info Percakapan (*Conversation Info Sidebar*)** (Opsional):
   - Dapat diakses melalui ikon info
   - Menampilkan:
     * Profil lengkap terapis
     * Janji temu mendatang
     * Galeri file/media yang dibagikan
     * Cari dalam percakapan
     * Pengaturan notifikasi
     * Opsi laporkan/blokir

8. **Pengaturan Notifikasi (*Notification Settings*)**:
   - Opsi *mute* per percakapan
   - Tautan preferensi notifikasi global

9. **Privasi & Panduan (*Privacy & Guidelines*)**:
   - Banner atau info:
     * "All messages are confidential and encrypted"
     * Tautan "Community guidelines"
     * "Response time: Usually within 2 hours"

10. **Keadaan *Offline*/Kesalahan (*Offline/Error States*)**:
    - Banner "No internet connection"
    - Indikator gagal kirim (tanda seru merah)
    - Tombol coba lagi (*retry*)

**Interaksi & Perilaku:**
- Perpesanan waktu nyata (*WebSocket*/*Pusher*)
- Indikator mengetik
- Tanda terima dibaca (*read receipts*)
- Status pengiriman pesan
- *Auto-scroll* ke bawah pada pesan baru
- *Lightbox* pratinjau gambar
- *Progress bar* unggah file
- Antarmuka perekaman pesan suara
- Cari dalam percakapan
- Opsi salin/hapus pesan (*long press*/*right click*)
- Pemilih emoji dengan kategori
- Reaksi pesan (opsional)

***User Flow***:
Klien → *Messages* → Pilih percakapan terapis → Baca pesan → Ketik balasan → Kirim → Pengiriman waktu nyata

---

### 4.3.5.8 *Mockup* ***Dashboard*** Terapis (*Therapist Dashboard Pages*)

***Dashboard*** Terapis adalah area khusus untuk terapis yang telah terdaftar dan disetujui (*approved*). ***Dashboard*** ini memungkinkan terapis untuk mengelola jadwal (*schedule*), janji temu (*appointments*), klien (*clients*), sesi (*sessions*), dan penghasilan (*earnings*).

---

**[GAMBAR 4.46 - *Mockup* ***Dashboard*** Terapis (*Therapist Dashboard*) (Utama)]** 👨‍⚕️
_*Dashboard* terapis - Jadwal hari ini, statistik, tindakan cepat_

**[GAMBAR 4.47 - *Mockup* Manajemen Jadwal Terapis (*Therapist Schedule Management*)]** 👨‍⚕️
_Terapis - Tampilan kalender semua *booking*, filter berdasarkan status_

**[GAMBAR 4.48 - *Mockup* Pengaturan Ketersediaan Terapis (*Therapist Availability Settings*)]** 👨‍⚕️
_Terapis - Atur jadwal mingguan, blokir tanggal/waktu_

**[GAMBAR 4.49 - *Mockup* Daftar Klien Terapis (*Therapist Clients List*)]** 👨‍⚕️
_Terapis - Tabel semua klien dengan pencarian/filter_

**[GAMBAR 4.50 - *Mockup* Tampilan Profil Klien (*Client Profile View*) (Perspektif Terapis)]** 👨‍⚕️
_Terapis - Profil klien, riwayat, data kemajuan_

**[GAMBAR 4.51 - *Mockup* Ruang Sesi (*Session Room*) (Konferensi Video)]** 👨‍⚕️
_Terapis - Antarmuka panggilan video untuk sesi *online*_

**[GAMBAR 4.52 - *Mockup* Formulir Entri Catatan Sesi (*Session Notes Entry Form*)]** 👨‍⚕️
_Terapis - Formulir untuk menulis catatan terapi setelah sesi_

**[GAMBAR 4.53 - *Mockup* Riwayat Sesi Terapis (*Therapist Session History*)]** 👨‍⚕️
_Terapis - Daftar semua sesi yang selesai dengan catatan_

**[GAMBAR 4.54 - *Mockup* ***Dashboard*** Penghasilan Terapis (*Therapist Earnings Dashboard*)]** 👨‍⚕️
_Terapis - Grafik pendapatan, riwayat transaksi_

**[GAMBAR 4.55 - *Mockup* Halaman Edit Profil Terapis (*Therapist Profile Edit Page*)]** 👨‍⚕️
_Terapis - Edit bio, kredensial, foto, spesialisasi_

---

#### A. ***Dashboard*** Terapis (Utama) (*Therapist Dashboard Main*)

**Deskripsi:**
***Dashboard*** Terapis Utama (*Therapist Dashboard Main*) adalah *landing page* setelah terapis *login*. Memberikan gambaran umum (*overview*) lengkap dari jadwal hari ini, janji temu mendatang, penghasilan, dan metrik kunci (*key metrics*).

**Elemen Utama:**
1. ***Top Navigation* & *Sidebar***:
   - Struktur serupa dengan *dashboard* klien
   - Item navigasi:
     * *Dashboard* (aktif)
     * *My Schedule*
     * *Clients*
     * *Sessions*
     * *Earnings*
     * *Profile*
     * *Settings*

2. **Bagian Sambutan (*Welcome Section*)**:
   - "Good Morning, Dr. [Nama Terapis]"
   - Tanggal & waktu saat ini
   - Statistik cepat: "You have 5 sessions today"

3. **Kartu Metrik Kunci (*Key Metrics Cards*)** (4 kartu):
   - **Sesi Hari Ini (*Today's Sessions*)**:
     * Angka: "5"
     * Ikon: Kalender
     * Tautan "View Schedule"
   
   - **Total Klien (*Total Clients*)**:
     * Angka: "127"
     * Ikon: Pengguna
     * Tren "+5 this month"
   
   - **Penghasilan Bulan Ini (*This Month Earnings*)**:
     * Jumlah: "Rp 18.500.000"
     * Ikon: Uang
     * Tren "+12% from last month"
   
   - **Rata-rata *Rating* (*Average Rating*)**:
     * Bintang: 4.9/5.0
     * Ikon: Bintang
     * "Based on 87 reviews"

4. **Kartu Jadwal Hari Ini (*Today's Schedule Card*)**:
   - "Today's Appointments"
   - Tampilan *timeline* sesi hari ini:
     * Setiap janji temu:
       - Waktu: "09:00 AM - 10:00 AM"
       - Nama klien + *avatar*
       - Nama layanan
       - Lencana tipe sesi (*Online*/*Offline*)
       - Status: *Upcoming*/*In Progress*/*Completed*
       - Tindakan cepat:
         * "Join Session" (jika *online* & waktu)
         * "View Details"
         * "Start Session"
         * "Cancel" (dengan alasan)
   - Slot kosong ditampilkan sebagai istirahat
   - Tautan "View Full Schedule"

5. **Kartu Klien Mendatang (*Upcoming Clients Card*)**:
   - "Next Clients"
   - Daftar 3-4 klien berikutnya:
     * *Avatar* + nama
     * Layanan yang di-*booking*
     * Waktu
     * Lencana klien baru (jika pertama kali)
     * Tautan "View Profile"
   - Tautan "See All Clients"

6. **Aktivitas Terbaru (*Recent Activities*)**:
   - *Feed* aktivitas:
     * "New booking from [Nama Klien]"
     * "[Klien] left a 5-star review"
     * "Payment received: Rp 300.000"
     * "New message from [Klien]"
   - *Timestamp*
   - Tautan "View All"

7. ***Widget* Ringkasan Penghasilan (*Earnings Overview Widget*)**:
   - "This Month Earnings"
   - Grafik batang menampilkan penghasilan harian/mingguan
   - Tautan "View Detailed Report"

8. **Ulasan Klien (*Client Reviews*)**:
   - "Recent Reviews"
   - 2-3 ulasan terbaru:
     * Nama klien (atau anonim)
     * Bintang *rating*
     * Kutipan ulasan
     * Tanggal
   - Tautan "View All Reviews"

9. **Bagian Tindakan Cepat (*Quick Actions Section*)**:
   - Tombol:
     * "Set Availability"
     * "View Messages"
     * "Add Session Notes"
     * "Request Withdrawal"

10. **Pusat Notifikasi (*Notifications Center*)**:
    - Ikon bel dengan lencana jumlah
    - Daftar *dropdown*:
      * *Booking* baru
      * Pembatalan
      * Pesan
      * Ulasan
      * Notifikasi pembayaran
    - Opsi tandai sebagai dibaca

**Interaksi & Perilaku:**
- Pembaruan waktu nyata (*real-time updates*) untuk *booking* baru
- *Auto-refresh* jadwal setiap 5 menit
- *Timer countdown* untuk sesi berikutnya
- Notifikasi *popup*/*toast*
- Tata letak responsif

***User Flow***:
Terapis *login* → ***Dashboard*** → Gambaran umum metrik → Periksa jadwal hari ini → Ambil tindakan

---

#### B. Manajemen Jadwal Terapis (*Therapist Schedule Management*)

**Deskripsi:**
Halaman *Schedule Management* memungkinkan terapis melihat kalender janji temu mereka dengan berbagai tampilan (*views*) (*day*, *week*, *month*) dan mengelola *booking*.

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "My Schedule"
   - Rentang tanggal ditampilkan
   - Tombol "Set Availability" (menonjol)

2. **Pemilih Tampilan Kalender (*Calendar View Selector*)**:
   - Tombol *toggle*:
     * Tampilan hari (*Day view*)
     * Tampilan minggu (*Week view*) (default)
     * Tampilan bulan (*Month view*)
   - Navigasi tanggal: < Hari Ini | *Date picker* | >

3. **Tampilan Minggu (*Week View*)** (Default):
   - Tata letak *grid*:
     * Sumbu-Y: Slot waktu (8:00 AM - 8:00 PM)
     * Sumbu-X: Hari dalam minggu (Sen - Min)
   
   - Janji temu ditampilkan sebagai blok:
     * Kode warna berdasarkan status:
       - *Confirmed*: Hijau
       - *Pending*: Oranye
       - *Completed*: Abu-abu
       - *Cancelled*: Merah coret
     * Setiap blok menampilkan:
       - Waktu
       - Nama klien
       - Nama layanan
       - Ikon tipe sesi
     * *Hover*: Tampilkan lebih banyak detail
     * Klik: Buka *modal* detail janji temu
   
   - Slot kosong dapat diklik (blokir waktu istirahat)
   - *Drag & drop* untuk *reschedule* (opsional)

4. **Tampilan Hari (*Day View*)**:
   - *Timeline* terperinci hari tunggal
   - Blok lebih besar dengan lebih banyak info:
     * Foto klien
     * Nama layanan lengkap
     * Pratinjau catatan sesi
     * Tombol tindakan terlihat

5. **Tampilan Bulan (*Month View*)**:
   - *Grid* kalender
   - Titik atau angka menunjukkan sesi per hari
   - Klik hari → Tampilkan daftar janji temu
   - Intensitas warna berdasarkan kepadatan *booking*

6. **Filter & Legenda (*Filter & Legend*)**:
   - Filter janji temu:
     * Berdasarkan status (*All*, *Confirmed*, *Pending*, dll.)
     * Berdasarkan tipe sesi (*Online*, *Offline*)
     * Berdasarkan layanan
   - Legenda warna menjelaskan warna status

7. ***Sidebar*** (*Desktop*):
   - Mini kalender untuk navigasi cepat
   - Statistik ringkasan hari ini
   - Filter cepat
   - Tombol "Add Time Off"

8. **Tindakan Janji Temu (*Appointment Actions*)**:
   - Klik blok janji temu → *Modal*:
     * Lihat detail klien
     * Informasi sesi
     * Tombol "Start Session"
     * Tombol "Add Notes"
     * "Cancel Appointment"
     * "Reschedule"
     * "Contact Client"

9. **Blok Waktu Istirahat (*Time Off Blocks*)**:
   - Blokir waktu istirahat ditampilkan sebagai tidak tersedia
   - Warna berbeda (abu-abu bergaris)
   - Label: "Break" / "Time Off" / "Lunch"
   - Dapat diedit/dihapus

**Interaksi & Perilaku:**
- Transisi halus antar tampilan
- *Drag & drop reschedule* dengan konfirmasi
- Pembaruan waktu nyata dari *booking* baru
- Sinkronisasi dengan *Google Calendar* (opsional)
- Ekspor kalender (*.ics*)
- Opsi cetak jadwal

***User Flow***:
Terapis → *My Schedule* → Pilih tampilan → Telusuri janji temu → Klik untuk detail → Ambil tindakan

---

#### C. Pengaturan Ketersediaan Terapis (*Therapist Availability Settings*)

**Deskripsi:**
Halaman *Availability Settings* memungkinkan terapis mengatur jam kerja reguler mereka, tanggal spesifik yang tidak tersedia, dan waktu istirahat (*time off*). Ini mempengaruhi ketersediaan *booking* untuk klien.

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "Availability Settings"
   - Subjudul: "Manage your working hours and time off"

2. **Bagian Jam Kerja (*Working Hours Section*)**:
   - "Regular Working Hours"
   - Pengaturan per hari:
     * Daftar hari dalam minggu:
       - Senin: *Toggle* Aktif/Nonaktif
         * Jika Aktif: *Time picker* (Mulai - Selesai)
         * Contoh: 09:00 AM - 05:00 PM
         * Tombol "Add Break" (untuk makan siang, dll.)
         * Beberapa slot waktu per hari
       - Selasa: ...
       - ... (semua 7 hari)
   
   - Tindakan cepat "Apply to All Days"
   - Opsi "Copy from Monday"
   
   - Konfigurasi istirahat (*breaks*):
     * Nama istirahat: "Lunch Break"
     * Waktu Mulai - Selesai: 12:00 PM - 1:00 PM
     * Tombol hapus istirahat

3. **Pengaturan Durasi Sesi (*Session Duration Settings*)**:
   - "Default Session Duration"
   - *Dropdown*: 30 menit, 45 menit, 60 menit, 90 menit, 120 menit
   - Waktu penyangga (*buffer time*) antar sesi: 5/10/15/30 menit

4. **Jendela *Booking* (*Booking Window*)**:
   - "How far in advance can clients book?"
   - Pemberitahuan minimum: 2 jam, 4 jam, 1 hari, 2 hari
   - Maksimum di muka: 1 minggu, 2 minggu, 1 bulan, 3 bulan

5. **Tanggal Spesifik Tidak Tersedia (*Specific Dates Unavailable*)**:
   - "Time Off / Holidays"
   - *Calendar picker* untuk memilih tanggal
   - Daftar waktu istirahat mendatang:
     * Rentang tanggal: 15-17 Nov 2024
     * Alasan: "Conference Attendance"
     * Status: Aktif
     * Tombol Edit/Hapus
   - Tombol "Add Time Off"

6. **Ketersediaan Pengganti (*Override Availability*)**:
   - "Custom Availability for Specific Dates"
   - Kasus penggunaan: Bekerja pada hari Minggu secara khusus
   - *Date picker* + pengaturan waktu
   - Prioritas atas jam reguler

7. **Pratinjau Ketersediaan (*Availability Preview*)**:
   - "Preview Your Availability"
   - Mini kalender menampilkan:
     * Hari tersedia (hijau)
     * Sebagian tersedia (kuning)
     * Tidak tersedia (merah)
     * Waktu istirahat (abu-abu)
   - Klik hari → Tampilkan slot waktu

8. **Preferensi Notifikasi (*Notification Preferences*)**:
   - "Notify me for bookings:"
   - *Checkbox*:
     * *Booking* baru (instan)
     * *Booking* X jam sebelumnya
     * Ringkasan jadwal harian
     * Ringkasan jadwal mingguan

9. **Simpan Perubahan (*Save Changes*)**:
   - Tombol "Save Availability" (primer)
   - Tombol "Reset to Default"
   - Konfirmasi: "Changes saved successfully"

**Interaksi & Perilaku:**
- *Time picker* dengan validasi (selesai > mulai)
- Deteksi konflik (waktu tumpang tindih)
- Pembaruan pratinjau waktu nyata
- *Modal* konfirmasi untuk perubahan besar
- *Auto-save draft* (opsional)

***User Flow***:
Terapis → *Availability Settings* → Atur jam kerja → Tambah waktu istirahat → Simpan → Sistem memperbarui ketersediaan *booking* untuk klien

---

#### D. Daftar Klien Terapis (*Therapist Clients List*)

**Deskripsi:**
Halaman *Clients List* menampilkan semua klien yang pernah atau sedang ditangani oleh terapis. Terapis dapat melihat profil, riwayat sesi, dan mengelola hubungan.

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "My Clients"
   - Jumlah klien: "127 Total Clients"
   - Tombol "Export Client List" (CSV)

2. **Pencarian & Filter (*Search & Filter*)**:
   - *Search bar*: "Search by name or ID..."
   - Filter:
     * Status: *All*, *Active*, *Inactive*, *New*
     * Tipe Layanan: *All*, *Stress*, *Weight Loss*, dll.
     * Sesi Terakhir: 7 hari terakhir, 30 hari, 3 bulan, 6 bulan
     * Urutkan: Nama A-Z, Aktivitas Terbaru, Total Sesi

3. ***Grid*/Daftar Klien (*Clients Grid/List*)**:
   - Tata letak kartu atau tabel
   - Setiap entri klien:
     * ***Avatar* + Nama**:
       - Foto profil
       - Nama lengkap
       - ID Klien
     
     * **Lencana Status (*Status Badge*)**:
       - *Active* (hijau)
       - *New Client* (biru)
       - *Inactive* (abu-abu)
     
     * **Statistik (*Statistics*)**:
       - Total sesi: 8 sesi
       - Sesi terakhir: 3 hari yang lalu
       - Sesi berikutnya: Besok 2:00 PM
       - Total dihabiskan: Rp 2.400.000
     
     * **Layanan Utama (*Primary Service*)**:
       - Layanan paling sering di-*booking*
       - Lencana
     
     * **Tindakan (*Actions*)**:
       - Tombol "View Profile" (primer)
       - Tombol "Send Message"
       - "*Book Session*" (atas nama)
       - *Dropdown*: *View History*, *Add Notes*, Arsipkan

4. ***Tab* Filter Cepat (*Quick Filters Tabs*)**:
   - *All Clients*
   - *Active* (memiliki sesi mendatang)
   - *New This Month*
   - *Needs Follow-up* (ditandai)

5. ***Modal* Detail Klien (*Client Detail Modal*)** (Tampilan Cepat):
   - Terbuka saat "View Profile" diklik
   - Tampilan ringkasan:
     * Info profil lengkap
     * Detail kontak (email, telepon)
     * Riwayat sesi (5 terakhir)
     * Gambaran umum kemajuan
     * Ringkasan catatan
     * Tautan "View Full Profile"

6. **Tindakan Massal (*Bulk Actions*)** (Opsional):
   - Pilih beberapa klien
   - Kirim pesan massal
   - Ekspor yang dipilih
   - Tambahkan ke grup

7. **Paginasi (*Pagination*)**:
   - Kontrol paginasi standar
   - Item per halaman: 20

**Interaksi & Perilaku:**
- Pencarian dengan *debounce*
- Kombinasi filter
- Urutkan dengan animasi
- Tampilan cepat *modal*
- Tabel/kartu responsif

***User Flow***:
Terapis → *My Clients* → Cari/filter → Pilih klien → Lihat profil → Ambil tindakan (pesan, lihat riwayat, dll.)

---

#### E. Tampilan Profil Klien (*Client Profile View*) (Perspektif Terapis)

**Deskripsi:**
Halaman profil klien terperinci yang hanya dapat diakses oleh terapis. Berisi informasi komprehensif tentang klien, riwayat sesi, catatan, dan pelacakan kemajuan.

**Elemen Utama:**
1. **Header Profil (*Profile Header*)**:
   - *Avatar* besar
   - Nama klien (H2)
   - ID Klien
   - Lencana status (*Active*/*Inactive*)
   - Tanggal menjadi anggota
   - Tombol tindakan:
     * "Send Message"
     * "Schedule Session"
     * "Add Note"
     * Menu lainnya (*Flag*, Arsipkan, Laporkan)

2. **Navigasi *Tab* (*Tabs Navigation*)**:
   - *Overview*
   - *Session History*
   - *Notes & Observations*
   - *Progress & Goals*
   - *Files & Documents*

3. ***Tab Overview***:
   - **Informasi Pribadi (*Personal Information*)**:
     * Nama lengkap
     * Email (dapat diklik)
     * Telepon (dapat diklik, panggil)
     * Tanggal lahir / Usia
     * Jenis kelamin
     * Alamat (untuk sesi *offline*)
     * Kontak darurat
   
   - **Statistik Cepat (*Quick Stats*)**:
     * Total sesi: 12
     * Total dihabiskan: Rp 3.600.000
     * Rata-rata *rating* yang diberikan: 5.0
     * Sesi terakhir: 28 Okt 2024
     * Sesi berikutnya: 5 Nov 2024
   
   - **Keluhan Utama (*Primary Concerns*)**:
     * Daftar masalah utama yang ditangani klien:
       - Stres & Kecemasan
       - Gangguan Tidur
     * Ditambahkan oleh klien selama *intake*
   
   - **Riwayat Layanan (*Services History*)**:
     * Grafik atau daftar layanan yang digunakan
     * Frekuensi per tipe layanan

4. ***Tab* Riwayat Sesi (*Session History Tab*)**:
   - Daftar semua sesi lampau:
     * Tanggal & waktu
     * Nama layanan
     * Durasi
     * Status (*Completed*/*Cancelled*)
     * Status pembayaran
     * *Rating* sesi (jika klien memberi nilai)
     * Tautan "View Notes"
   - Ekspor sebagai PDF
   - Total: 12 sesi selesai

5. ***Tab* Catatan & Observasi (*Notes & Observations Tab*)**:
   - **Catatan Sesi (*Session Notes*)** (Kronologis):
     * Setiap entri catatan:
       - Tanggal sesi
       - Tipe layanan
       - Catatan terapis (pribadi, tidak dibagikan dengan klien)
       - Observasi
       - *Feedback* klien
       - *Homework* yang diberikan
       - Langkah berikutnya
       - Tombol Edit/Hapus
   
   - **Tombol "Add New Note"**:
     * Buka formulir:
       - Tanggal (*auto-filled*)
       - Terkait sesi? (Ya/Tidak)
       - Tipe catatan (Observasi, Kemajuan, Kekhawatiran)
       - Konten catatan (*rich text editor*)
       - Bagikan dengan klien? (*checkbox*)
       - Simpan/Batal

6. ***Tab* Kemajuan & Tujuan (*Progress & Goals Tab*)**:
   - **Daftar Tujuan (*Goals List*)**:
     * Deskripsi tujuan
     * Tanggal ditetapkan
     * Target penyelesaian
     * *Progress bar*
     * Status (*In Progress*/*Achieved*)
     * Catatan tentang kemajuan
   
   - **Metrik Kemajuan (*Progress Metrics*)**:
     * Grafik menampilkan peningkatan
     * Tren skor kesejahteraan
     * Tingkat kehadiran
   
   - Tombol "Set New Goal"

7. ***Tab* File & Dokumen (*Files & Documents Tab*)**:
   - Dokumen yang diunggah:
     * Formulir *intake*
     * Formulir persetujuan
     * Riwayat medis
     * Laporan kemajuan
     * Rekaman sesi (jika ada)
   - Tombol "Upload New File"
   - Opsi unduh/lihat

8. **Bagian Penilaian Risiko (*Risk Assessment Section*)** (jika berlaku):
   - Indikator tingkat risiko
   - Tanggal penilaian terakhir
   - Catatan tentang faktor risiko
   - Tindakan *follow-up*

9. **Log Komunikasi (*Communication Log*)**:
   - Riwayat semua pesan yang dipertukarkan
   - Log komunikasi email
   - Catatan panggilan telepon

**Interaksi & Perilaku:**
- Peralihan *tab* dengan transisi halus
- Bagian yang dapat ditutup
- *Rich text editor* untuk catatan
- Unggah file dengan pratinjau
- Cetak profil klien
- Ekspor data (kepatuhan GDPR)

***User Flow***:
Terapis → *My Clients* → Pilih klien → Tampilan profil → Telusuri *tab* → Tambah catatan / Lihat riwayat / Perbarui tujuan

---

#### F. Ruang Sesi (*Session Room*) (Konferensi Video)

**Deskripsi:**
*Session Room* adalah halaman khusus untuk melakukan sesi terapi *online* melalui panggilan video. Antarmuka dirancang untuk memberikan pengalaman yang profesional, aman, dan kondusif untuk sesi terapi.

**Elemen Utama:**
1. **Tata Letak Video (*Video Layout*)**:
   - **Tampilan Utama (*Main View*)**:
     * Video klien (besar, area dominan 70%)
     * Video terapis (lebih kecil, *picture-in-picture* di sudut)
     * Tombol ganti tampilan (*switch view*)
   
   - **Opsi Tata Letak (*Layout Options*)**:
     * Tampilan galeri (*Gallery view*) (*side-by-side*, ukuran sama)
     * Tampilan pembicara (*Speaker view*) (pembicara aktif dominan)
     * Mode presentasi (*screen share* utama)

2. ***Control Bar*** (Bawah):
   - Selalu terlihat atau *auto-hide* dengan *hover*
   - Ikon dengan label:
     * **Mikrofon (*Microphone*)**: *Mute*/*Unmute* (merah saat *mute*)
     * **Kamera (*Camera*)**: Mulai/Hentikan video
     * ***Screen Share***: Opsi berbagi layar
     * ***Chat***: Buka *sidebar* *chat* teks (lencana untuk pesan baru)
     * **Peserta (*Participants*)**: Tampilkan daftar peserta (biasanya hanya 2)
     * **Pengaturan (*Settings*)**: Pengaturan audio/video
     * **Rekam (*Record*)**: Rekam sesi (jika diaktifkan & disetujui)
     * **Akhiri Panggilan (*End Call*)**: Tombol merah, *modal* konfirmasi

3. ***Timer* Sesi (*Session Timer*)**:
   - Ditampilkan secara menonjol (atas-tengah atau sudut)
   - Menampilkan waktu yang berlalu: "00:45:30"
   - Waktu tersisa: "15 min left"
   - Perubahan warna: Hijau → Kuning (10 menit) → Merah (5 menit)

4. ***Bar* Informasi Sesi (*Session Information Bar*)** (Atas):
   - Nama klien
   - Tipe layanan
   - Durasi sesi yang di-*booking*
   - Indikator kualitas koneksi (hijau/kuning/merah)

5. ***Sidebar Chat*** (Dapat Ditutup):
   - *Chat* teks selama sesi
   - Kirim pesan, tautan, sumber daya
   - Kemampuan berbagi file
   - Transkrip *chat* disimpan

6. **Panel Catatan (*Notes Panel*)** (Dapat Ditutup, Sisi Kanan):
   - Catatan cepat selama sesi
   - Area teks untuk terapis mengetik observasi
   - *Auto-save* setiap 30 detik
   - Hanya dapat diakses oleh terapis
   - Tombol "Save & Add to Client Record"

7. **Latar Belakang Virtual (*Virtual Background*)** (Opsional):
   - *Blur* latar belakang
   - Pilih dari latar belakang *preset*
   - Unggah latar belakang kustom

8. **Indikator Kualitas Jaringan (*Network Quality Indicator*)**:
   - Ikon menampilkan kekuatan koneksi
   - Tampilan penggunaan *bandwidth*
   - Peringatan "Poor connection" dengan tips pemecahan masalah

9. **Ruang Tunggu (*Waiting Room*)** (Sebelum Sesi):
   - "Waiting for [Nama Klien] to join..."
   - Tes koneksi:
     * Pratinjau kamera
     * Tes mikrofon
     * Tes *speaker*
   - Tombol "Start Session" (setelah klien bergabung)

10. ***Modal* Akhiri Sesi (*End Session Modal*)**:
    - Konfirmasi: "Are you sure you want to end the session?"
    - Opsi:
      * Tambah catatan sesi sekarang
      * Tambah catatan nanti
      * Akhiri tanpa catatan
    - *Feedback*: "How was the video quality?" (1-5 bintang)
    - Tombol "End Session"

11. **Penanganan Masalah Teknis (*Technical Issue Handling*)**:
    - *Overlay* menghubungkan kembali jika koneksi terputus
    - Opsi "Switch to audio only" jika video *lag*
    - Tombol kontak darurat
    - Tautan "Report Technical Issue"

12. **Indikator Keamanan (*Security Indicators*)**:
    - Lencana enkripsi *end-to-end*
    - "This session is private and secure"
    - Indikator perekaman (jika merekam): Titik merah "Recording"

**Interaksi & Perilaku:**
- Streaming video WebRTC
- *Bitrate* adaptif berdasarkan *bandwidth*
- Pembatalan gema (*echo cancellation*), penekanan kebisingan (*noise suppression*)
- *Auto-focus* pada pembicara aktif
- *Keyboard shortcuts* (M untuk *mute*, V untuk video, dll.)
- Responsif *mobile* (mode *landscape* lebih disukai)
- Mode *picture-in-picture* saat *tab* diganti

***User Flow***:
Terapis → Bergabung sesi 5 menit lebih awal → Tes koneksi → Klien bergabung → Mulai sesi → Lakukan terapi → Buat catatan → Akhiri panggilan → Tambah catatan final

---

#### G. Session Notes Entry Form

**Deskripsi:**
Session Notes form memungkinkan therapist untuk mendokumentasikan observations, progress, dan recommendations setelah (atau selama) therapy session. Notes ini penting untuk continuity of care dan legal documentation.

---

#### G. Formulir Entri Catatan Sesi (*Session Notes Entry Form*)

**Deskripsi:**
Formulir *Session Notes* memungkinkan terapis untuk mendokumentasikan observasi, kemajuan, dan rekomendasi setelah (atau selama) sesi terapi. Catatan ini penting untuk kelangsungan perawatan (*continuity of care*) dan dokumentasi hukum.

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "Session Notes"
   - Nama klien + foto
   - Tanggal & waktu sesi
   - Tipe layanan
   - Durasi sesi

2. **Bagian Informasi Sesi (*Session Information Section*)** (*Auto-filled*):
   - ID Sesi
   - Tanggal & waktu (*pre-filled*)
   - Durasi (aktual, dapat diedit jika berbeda dari yang di-*booking*)
   - Nomor sesi (mis., "Session 8 of 10")
   - Tipe sesi (*Online*/*Offline*)
   - Status kehadiran:
     * Hadir
     * Terlambat (tentukan menit)
     * Tidak hadir (*No-show*)
     * Dibatalkan

3. **Bagian Penilaian (*Assessment Section*)**:
   - **Keadaan Saat Ini (*Current State*)**:
     * *Textarea*: "Client's presenting concern/state at start of session"
     * *Rating* suasana hati (skala 1-10 *slider*)
     * Tingkat kecemasan (1-10)
     * Kesejahteraan keseluruhan (1-10)
   
   - **Observasi (*Observations*)**:
     * *Textarea*: "Behavioral observations, body language, tone"
     * *Rich text editor* dengan opsi pemformatan

4. **Ringkasan Sesi (*Session Summary*)**:
   - **Topik yang Dibahas (*Topics Discussed*)**:
     * *Multi-select* atau *tag*: Stres, Hubungan, Pekerjaan, Tidur, dll.
     * Topik tambahan *free-text*
   
   - **Teknik yang Digunakan (*Techniques Used*)**:
     * *Checkbox*: Induksi Hipnotik, Regresi, Terapi Sugesti, CBT, dll.
     * *Rating* efektivitas per teknik (1-5)
   
   - **Respons Klien (*Client Response*)**:
     * *Textarea*: "How client responded to interventions"
     * Kualitas respons: *Excellent*, *Good*, *Fair*, *Poor*

5. **Catatan Kemajuan (*Progress Notes*)**:
   - *Textarea*: "Detailed notes on session content and progress"
   - Minimum 200 karakter (standar profesional)
   - *Rich text editor*:
     * Tebal, miring, garis bawah
     * *Bullet point*, daftar bernomor
     * Judul
   - Penyisipan *template*: Frasa/bagian umum

6. **Tinjauan Tujuan (*Goals Review*)**:
   - Daftar tujuan aktif klien
   - Untuk setiap tujuan:
     * Deskripsi tujuan
     * *Dropdown* pembaruan kemajuan: *No Change*, *Some Progress*, *Significant Progress*, *Goal Met*
     * Catatan tentang kemajuan tujuan (*textarea*)

7. **Item *Homework*/Tindakan (*Homework/Action Items*)**:
   - "Assigned Tasks for Client"
   - Tambah beberapa tugas:
     * Deskripsi tugas
     * Tanggal jatuh tempo
     * Instruksi
   - *Checkbox* "Share with client"

8. **Rekomendasi (*Recommendations*)**:
   - **Sesi Berikutnya (*Next Session*)**:
     * Waktu yang direkomendasikan: 1 minggu, 2 minggu, 1 bulan
     * Area fokus untuk sesi berikutnya
   
   - **Layanan Tambahan (*Additional Services*)**:
     * Sarankan layanan lain
     * Rujukan (jika diperlukan)

9. **Penilaian Risiko (*Risk Assessment*)** (Jika berlaku):
   - Tingkat risiko: Tidak Ada, Rendah, Sedang, Tinggi
   - Jika Sedang/Tinggi:
     * Kekhawatiran spesifik
     * Rencana keamanan
     * Tindakan *follow-up*
     * Notifikasi supervisor diperlukan

10. **Lampiran (*Attachments*)**:
    - Unggah file:
      * Lembar kerja yang digunakan
      * Gambar/diagram klien
      * Rekaman audio (jika disetujui)
    - Batas ukuran file ditampilkan

11. **Pengaturan Visibilitas (*Visibility Settings*)**:
    - Tombol radio:
      * Pribadi (Hanya terapis)
      * Dibagikan dengan Klien (Klien dapat melihat di portal mereka)
      * Dibagikan dengan Supervisor (Jika berlaku)

12. **Opsi Simpan (*Save Options*)**:
    - Tombol "Save as Draft" (abu-abu)
    - Tombol "Save & Mark Complete" (primer)
    - "Save & Email to Client" (jika dibagikan)
    - Indikator *auto-save*: "Last saved 2 minutes ago"

13. ***Template*** (Opsional):
    - *Dropdown* "Load Template"
    - Bagian *pre-filled* untuk tipe sesi umum
    - *Template* kustom dapat disimpan

**Validasi & Kepatuhan (*Validation & Compliance*)**:
- Kolom wajib disorot
- Minimum karakter dipaksa (standar profesional)
- Peringatan "Incomplete note" jika info kritis hilang
- Pemberitahuan kepatuhan HIPAA/perlindungan data

**Interaksi & Perilaku:**
- *Auto-save* setiap 60 detik
- *Rich text editor* dengan pemformatan
- Sistem *template* untuk efisiensi
- Responsif *mobile* (ramah tablet)
- Opsi suara-ke-teks (pengenalan ucapan)

***User Flow***:
Setelah sesi → Tambah catatan sesi → Isi semua bagian → Tinjau → Simpan → Catatan disimpan dalam rekam klien

---

#### H. Riwayat Sesi Terapis (*Therapist Session History*)

**Deskripsi:**
Halaman *Session History* menampilkan daftar komprehensif dari semua sesi yang telah dilakukan oleh terapis, dengan kemampuan filter dan analitik.

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "Session History"
   - Jumlah total sesi selesai
   - Pemilih rentang tanggal

2. **Kartu Statistik Ringkasan (*Summary Statistics Cards*)**:
   - **Total Sesi (*Total Sessions*)**: 487
   - **Bulan Ini (*This Month*)**: 42 (+8 dari bulan lalu)
   - **Tingkat Penyelesaian (*Completion Rate*)**: 96%
   - **Durasi Rata-rata (*Average Duration*)**: 58 menit

3. **Bagian Filter (*Filter Section*)**:
   - Pencarian: "Search by client name or session ID..."
   - Filter:
     * Rentang tanggal (*calendar picker*)
     * Status: *All*, *Completed*, *Cancelled*, *No-show*
     * Tipe sesi: *All*, *Online*, *Offline*
     * Layanan: *Dropdown* semua layanan
     * Klien: Pilih klien spesifik
   - Tombol "Apply Filters"
   - Tautan "Clear All"

4. **Opsi Urutkan (*Sort Options*)**:
   - *Dropdown*: Terbaru Pertama, Terlama Pertama, Nama Klien A-Z, Durasi

5. **Tabel/Daftar Sesi (*Sessions Table/List*)**:
   - Kolom:
     * **Tanggal & Waktu**: Dapat diurutkan
     * **Klien**: Nama + *avatar*, dapat diklik ke profil
     * **Layanan**: Nama layanan + lencana
     * **Durasi**: Waktu aktual yang dihabiskan
     * **Tipe**: Ikon *Online*/*Offline*
     * **Status**: Lencana (*Completed*/*Cancelled*/*No-show*)
     * ***Rating***: *Rating* klien (jika diberikan)
     * **Catatan**: Indikator ikon (hijau jika catatan ditambahkan)
     * **Tindakan**: Menu *dropdown*
   
   - Tindakan baris:
     * *View Details*
     * *View/Edit Notes*
     * *View Recording* (jika tersedia)
     * *Generate Report*
     * *Copy Session Details*

6. ***Modal* Detail Sesi (*Session Detail Modal*)**:
   - Terbuka saat baris diklik
   - Menampilkan:
     * Semua informasi sesi
     * Catatan sesi (jika ditambahkan)
     * *Feedback*/*rating* klien
     * Detail pembayaran
     * Tautan rekaman (jika berlaku)
   - Tombol "Edit Notes"
   - Tombol "Download Report"

7. **Tindakan Massal (*Bulk Actions*)**:
   - Pilih beberapa sesi (*checkbox*)
   - Ekspor massal (CSV/PDF)
   - Buat laporan ringkasan

8. **Bagian Analitik (*Analytics Section*)** (Dapat Ditutup):
   - "Session Analytics"
   - Grafik:
     * Sesi per bulan (grafik batang)
     * Rasio *Online* vs *Offline* (grafik lingkaran)
     * Distribusi layanan (grafik donat)
     * Tren tingkat penyelesaian (grafik garis)
   - Tautan "View Detailed Analytics"

9. **Opsi Ekspor (*Export Options*)**:
   - Tombol "Export Session History"
   - Opsi format: CSV, Excel, PDF
   - Pemilihan rentang tanggal untuk ekspor
   - Sertakan catatan? (*checkbox*)

10. **Paginasi (*Pagination*)**:
    - Kontrol paginasi standar
    - Item per halaman: 10, 25, 50, 100
    - Indikator total halaman

**Interaksi & Perilaku:**
- Filter pencarian waktu nyata
- Kolom dapat diurutkan
- Baris yang dapat diperluas untuk tampilan cepat
- Tampilan detail *modal*
- *Lazy loading* untuk performa
- Ekspor menghasilkan *async* (unduh saat siap)

***User Flow***:
Terapis → *Session History* → Filter/cari sesi → Lihat detail → Ekspor atau analisis data

---

#### I. ***Dashboard*** Penghasilan Terapis (*Therapist Earnings Dashboard*)

**Deskripsi:**
***Dashboard*** Penghasilan memberikan ikhtisar komprehensif tentang pendapatan terapis (*therapist*), riwayat pembayaran (*payment history*), dan manajemen penarikan (*withdrawal management*).

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "My Earnings"
   - Total penghasilan sepanjang waktu (*lifetime earnings*) (besar, menonjol)

2. **Kartu Ringkasan Penghasilan (*Earnings Summary Cards*)**:
   - **Saldo Tersedia (*Available Balance*)**:
     * Jumlah: Rp 4.250.000
     * Siap untuk ditarik (*ready for withdrawal*)
     * Tombol "Request Withdrawal" (primer)
   
   - **Saldo Tertunda (*Pending Balance*)**:
     * Jumlah: Rp 1.800.000
     * Dari sesi terbaru (belum diproses)
     * Tautan "View Details"
   
   - **Penghasilan Bulan Ini (*This Month Earnings*)**:
     * Jumlah: Rp 6.500.000
     * +12% dari bulan lalu
     * *Progress bar* ke target bulanan
   
   - **Total Ditarik (*Total Withdrawn*)**:
     * Jumlah: Rp 45.000.000
     * Total sepanjang waktu (*lifetime total*)

3. **Grafik Penghasilan (*Earnings Chart*)**:
   - "Earnings Over Time"
   - Grafik garis menampilkan penghasilan bulanan
   - *Toggle*: 6 Bulan Terakhir, Tahun Lalu, Semua Waktu
   - Interaktif: *Hover* untuk jumlah pasti
   - Garis target (*goal line overlay*) (jika diatur)

4. **Tabel Transaksi Terbaru (*Recent Transactions Table*)**:
   - "Recent Earnings"
   - Kolom:
     * Tanggal
     * Nama Klien
     * Layanan
     * Durasi Sesi
     * Jumlah Diperoleh (*Amount Earned*)
     * Biaya Platform (*Platform Fee*)
     * Jumlah Bersih (*Net Amount*)
     * Status (*Cleared*/*Pending*)
   - Filter berdasarkan rentang tanggal
   - Opsi ekspor

5. **Bagian Rincian (*Breakdown Section*)**:
   - **Berdasarkan Tipe Layanan (*By Service Type*)**:
     * Grafik lingkaran menampilkan distribusi penghasilan
     * Tabel: Layanan | Sesi | Total Diperoleh
   
   - **Berdasarkan Tipe Sesi (*By Session Type*)**:
     * Perbandingan penghasilan *Online* vs *Offline*
     * Grafik batang

6. **Riwayat Penarikan (*Withdrawal History*)**:
   - "Past Withdrawals"
   - Daftar permintaan penarikan:
     * Tanggal permintaan
     * Jumlah
     * Metode (*Bank Transfer*/*E-Wallet*)
     * Status: *Processing*/*Completed*/*Failed*
     * ID Transaksi
     * Tautan "View Receipt"
   - Paginasi

7. **Bagian Permintaan Penarikan (*Request Withdrawal Section*)**:
   - Tombol "Withdraw Funds" membuka *modal*:
     * Saldo tersedia ditampilkan
     * *Input* jumlah (validasi min/maks)
     * Metode penarikan:
       - Transfer bank (*default*)
         * *Dropdown* nama bank
         * Nomor rekening
         * Nama pemegang rekening
       - Opsi *E-Wallet*
         * GoPay, OVO, Dana
         * Nomor telepon/akun
     * Waktu pemrosesan: "2-3 hari kerja"
     * Biaya: "Tidak ada biaya untuk transfer bank"
     * Tombol "Confirm Withdrawal"
   - Layar konfirmasi setelah permintaan

8. **Pengaturan Pembayaran (*Payment Settings*)**:
   - "Payment Methods"
   - Rekening bank/*e-wallet* yang tersimpan
   - Tombol "Add New Payment Method"
   - Atur metode *default*

9. **Informasi Pajak (*Tax Information*)** (Jika berlaku):
   - "Tax Summary"
   - Penghasilan tahun berjalan (*year-to-date earnings*)
   - Estimasi pajak (jika berlaku)
   - "Download Tax Report" (untuk pelaporan)

10. **Target Penghasilan (*Earnings Goals*)**:
    - "Set Monthly Goal"
    - *Input* jumlah target
    - Visualisasi kemajuan
    - "You're 85% to your goal!"

11. **Struktur Komisi (*Commission Structure*)**:
    - Bagian info: "How Earnings Work"
    - Biaya platform: 15% per sesi
    - Jadwal pembayaran: Pembersihan mingguan (*weekly clearance*)
    - Tautan kebijakan penarikan (*withdrawal policies link*)

**Interaksi & Perilaku:**
- Pembaruan saldo waktu nyata (*real-time balance updates*)
- Interaksi grafik (*hover*, *zoom*)
- Validasi formulir penarikan
- Notifikasi sukses/error
- *Email* konfirmasi untuk penarikan
- Tabel responsif mobile

***User Flow***:
Terapis → *Earnings* → Lihat saldo → Minta penarikan → Pilih metode → Konfirmasi → Tunggu pemrosesan → Terima pembayaran

---

#### J. Therapist Profile Edit Page

**Deskripsi:**
Profile Edit page memungkinkan therapist untuk update informasi professional mereka yang ditampilkan kepada clients. Ini penting untuk maintaining accurate dan attractive therapist profiles.

**Elemen Utama:**
1. **Page Header**:
   - Title: "Edit My Profile"
   - "Preview Public Profile" button (see as clients see)
   - Last updated date

2. **Profile Sections** (Tabs atau Accordion):

   **A. Basic Information**:
   - Profile Photo:
     * Current photo display (large)
     * "Change Photo" button (upload)
     * Guidelines: "Professional headshot, max 5MB, JPG/PNG"
     * Crop tool after upload
   
   - Full Name (required)
   - Title/Credentials: "Dr.", "CHT", "M.Psi", etc.
   - Gender dropdown
   - Date of Birth (for age calculation)
   - Contact Information:
     * Email (verified badge)
     * Phone number (verified)
     * Alternative contact

   **B. Professional Information**:
   - License Number (required, verified)
   - License Expiry Date
   - Issuing Authority
   - Professional Title: Dropdown (Clinical Hypnotherapist, Licensed Therapist, etc.)
   - Years of Experience: Number input
   - Languages Spoken: Multi-select (Indonesian, English, Mandarin, etc.)
   - Specializations:
     * Multi-select checkboxes:
       - Stress & Anxiety Management
       - Weight Management
       - Smoking Cessation
       - Phobia Treatment
       - Sleep Disorders
       - Trauma Healing
       - Pain Management
       - Confidence Building
     * Primary specialization (radio, must select one)

   **C. About Me**:
   - Professional Bio:
     * Rich text editor
     * Character limit: 500 words
     * Guidelines: "Describe your approach, experience, and what makes you unique"
     * Word count display
   
   - Therapy Approach:
     * Dropdown: Cognitive Behavioral, Psychodynamic, Holistic, Solution-Focused, etc.
   
   - Why I Became a Therapist:
     * Textarea (optional)
     * 200 kata

   **D. Pendidikan & Sertifikasi (*Education & Certifications*)**:
   - Tombol "Add Education":
     * Gelar: *Dropdown* (*Bachelor's*, *Master's*, *Doctorate*)
     * Bidang Studi (*Field of Study*)
     * Universitas/Institusi
     * Tahun Lulus (*Graduation Year*)
     * Tombol hapus entri
   
   - Tombol "Add Certification":
     * Nama Sertifikasi
     * Organisasi Penerbit
     * Tanggal Terbit (*Issue Date*)
     * Tanggal Kadaluarsa (jika berlaku)
     * ID Sertifikat
     * Unggah Sertifikat (PDF/Gambar)
     * Tombol hapus entri
   
   - Urutkan ulang entri (*drag & drop*)

   **E. Layanan & Harga (*Services & Pricing*)**:
   - Daftar layanan yang ditawarkan:
     * Setiap layanan:
       - Nama layanan (dari katalog)
       - Tawarkan layanan ini? (*checkbox*)
       - Harga Anda: *Input* (Rp)
       - Harga yang direkomendasikan: Rp 250K - 350K (info)
       - Durasi *default*: 30/60/90 menit
   
   - Biaya Konsultasi:
     * Harga sesi pertama (dapat berbeda)
     * Harga sesi lanjutan (*follow-up*)

   **F. Media & Portofolio (*Media & Portfolio*)**:
   - Video Pengenalan (*Video Introduction*):
     * Unggah video (maks 2 menit, 50MB)
     * Tautan YouTube/Vimeo (alternatif)
     * Pedoman: "Perkenalkan diri Anda dan pendekatan Anda"
   
   - Galeri Foto (*Photo Gallery*):
     * Unggah hingga 5 foto
     * Foto kantor/ruang kerja
     * Seret untuk mengurutkan ulang
     * Atur foto utama
   
   - Testimoni (*Testimonials*) (opsional):
     * Tambahkan testimoni secara manual
     * Nama klien (atau anonim)
     * Teks testimoni
     * *Rating*

   **G. Media Sosial & Situs Web (*Social Media & Website*)**:
   - URL LinkedIn
   - Akun (*handle*) Instagram
   - Halaman Facebook
   - Situs web profesional
   - Tautan publikasi/artikel

3. **Pengaturan Visibilitas (*Visibility Settings*)**:
   - Status Profil:
     * Aktif (Menerima klien baru)
     * Ketersediaan terbatas (*limited availability*)
     * Tidak menerima klien baru
   
   - Tampilkan di Direktori:
     * Publik (terlihat untuk semua)
     * Privat (hanya tautan langsung)

4. **Status Verifikasi (*Verification Status*)**:
   - Lencana yang ditampilkan:
     * ✓ *Email* Terverifikasi
     * ✓ Telepon Terverifikasi
     * ✓ Lisensi Terverifikasi
     * ✓ Identitas Terverifikasi
   - "Request Re-verification" jika diperlukan

5. **Mode Pratinjau (*Preview Mode*)**:
   - Tombol "Preview Changes"
   - Menampilkan bagaimana profil muncul kepada klien
   - Perbandingan berdampingan (lama vs baru)

6. **Bagian Simpan (*Save Section*)**:
   - Tombol "Save Changes" (primer, *sticky bottom*)
   - Tombol "Discard Changes"
   - "Save as Draft" (untuk edit yang belum selesai)
   - *Error* validasi disorot
   - Notifikasi sukses: "Profile updated successfully!"

**Validasi & Persyaratan:**
- Bidang wajib ditandai dengan *
- Validasi ukuran/format gambar
- Batas karakter diberlakukan
- Verifikasi lisensi diperlukan
- Pedoman foto profesional

**Interaksi & Perilaku:**
- *Draft auto-save* setiap 2 menit
- Alat pemangkasan gambar (*image cropping tool*)
- *Rich text editor* dengan pemformatan
- Pengurutan ulang *drag & drop*
- Pembaruan langsung pratinjau (*preview live updates*)
- Formulir responsif mobile

***User Flow***:
Terapis → Pengaturan Profil → Edit bagian → Unggah media → Pratinjau perubahan → Simpan → Profil diperbarui di direktori publik

---

### 4.3.5.9 *Mockup Admin Dashboard* (Halaman ***Dashboard*** Admin)

***Admin Dashboard*** adalah area khusus untuk administrator sistem yang memiliki akses penuh untuk mengelola pengguna (*manage users*), *booking*, keuangan (*finances*), dan pengaturan sistem (*system settings*). *Interface* dirancang untuk efisiensi dan manajemen data komprehensif.

---

**[GAMBAR 4.56 - *Mockup Admin Dashboard* (Utama)]** 👔
_***Dashboard*** admin - Statistik sistem, grafik, aktivitas terbaru_

**[GAMBAR 4.57 - *Mockup* Manajemen Pengguna Admin]** 👔
_Admin - Tabel semua pengguna (klien, terapis) dengan tindakan CRUD_

**[GAMBAR 4.58 - *Mockup* Manajemen *Booking* Admin]** 👔
_Admin - Lihat/edit semua *booking*, ubah status_

**[GAMBAR 4.59 - *Mockup* Laporan Keuangan Admin]** 👔
_Admin - Grafik pendapatan, laporan transaksi, ekspor data_

**[GAMBAR 4.60 - *Mockup* Pengaturan Sistem Admin]** 👔
_Admin - Konfigurasi parameter sistem, mode pemeliharaan_

---

#### A. ***Dashboard*** Admin (Utama) (*Admin Dashboard Main*)

**Deskripsi:**
***Admin Dashboard*** Utama adalah pusat komando (*command center*) untuk administrator sistem, menyediakan ikhtisar tingkat tinggi dari operasi platform, metrik kunci (*key metrics*), dan akses cepat ke fungsi manajemen.

**Elemen Utama:**
1. **Navigasi Atas (*Top Navigation*)**:
   - Logo CUR-HEART Admin
   - *Search bar* global (pengguna, *booking*, transaksi)
   - Lonceng notifikasi (*notification bell*) (peringatan sistem)
   - *Dropdown* profil admin

2. **Navigasi *Sidebar***:
   - *Dashboard* (aktif)
   - Manajemen Pengguna (*Users Management*)
   - Manajemen *Bookings* (*Bookings Management*)
   - Laporan Keuangan (*Financial Reports*)
   - Pengaturan Sistem (*System Settings*)
   - Tiket Dukungan (*Support Tickets*)
   - Analitik (*Analytics*)
   - Log & Audit

3. **Kartu Metrik Kunci (*Key Metrics Cards*)** (Baris Atas):
   - **Total Pengguna (*Total Users*)**:
     * Angka: 1.523
     * Rincian: Klien (1.250) | Terapis (58) | Admin (15)
     * Tren: +45 minggu ini
   
   - **Sesi Aktif Hari Ini (*Active Sessions Today*)**:
     * Angka: 37
     * *Online*: 28 | *Offline*: 9
     * Penghitung waktu nyata (*real-time counter*)
   
   - **Total Pendapatan (Bulan) (*Total Revenue Month*)**:
     * Jumlah: Rp 127.500.000
     * +18% dari bulan lalu
     * Ikon grafik tautan ke detail
   
   - **Kesehatan Platform (*Platform Health*)**:
     * Status: Semua Sistem Operasional (hijau)
     * *Uptime*: 99.8%
     * Tautan ke halaman status

4. **Grafik Pendapatan (*Revenue Chart*)**:
   - "Revenue Overview"
   - Grafik garis/area menampilkan pendapatan harian
   - *Toggle*: 7 hari terakhir, 30 hari, 3 bulan, Tahun
   - Bandingkan dengan periode sebelumnya (*overlay*)
   - Total dan rata-rata ditampilkan

5. **Tabel *Booking* Terbaru (*Recent Bookings Table*)**:
   - "Latest Bookings"
   - Kolom:
     * ID *Booking* (dapat diklik)
     * Nama klien
     * Nama terapis
     * Layanan
     * Tanggal & Waktu
     * Jumlah
     * Lencana status
     * Tindakan (*View*, *Cancel*, *Refund*)
   - Tautan "View All Bookings"

6. **Grafik Pertumbuhan Pengguna (*User Growth Chart*)**:
   - "User Registrations"
   - Grafik batang: Pengguna baru per hari/minggu
   - Dibagi berdasarkan tipe: Klien vs Terapis
   - *Toggle* periode waktu

7. **Panel Peringatan Sistem (*System Alerts Panel*)**:
   - "Important Alerts"
   - Daftar peringatan:
     * "5 aplikasi terapis tertunda (*pending*)"
     * "2 sengketa pembayaran perlu ditinjau"
     * "Pemeliharaan server dijadwalkan: 10 Nov"
     * "3 tiket dukungan belum terselesaikan"
   - Lencana prioritas (*High*, *Medium*, *Low*)
   - Tombol tindakan cepat

8. **Terapis Berkinerja Terbaik (*Top Performing Therapists*)**:
   - "Top Therapists This Month"
   - Papan peringkat (*leaderboard*) (5 teratas):
     * Peringkat
     * Nama terapis + foto
     * Sesi selesai
     * Pendapatan yang dihasilkan
     * *Rating* rata-rata
   - Tautan "View Full Report"

9. **Layanan Teratas (*Top Services*)**:
   - "Most Booked Services"
   - Grafik batang horizontal
   - Nama layanan | Jumlah *booking* | Persentase
   - Total pendapatan per layanan

10. **Bagian Tindakan Cepat (*Quick Actions Section*)**:
    - Tombol tindakan besar:
      * "Add New User"
      * "Review Therapist Applications"
      * "Generate Report"
      * "View Support Tickets"
      * "System Settings"

11. ***Feed* Aktivitas (*Activity Feed*)**:
    - "Recent Activity"
    - Linimasa (*timeline*) tindakan terbaru:
      * Registrasi pengguna baru
      * *Booking* dibuat/dibatalkan
      * Pembayaran diproses
      * Aplikasi terapis
      * Ulasan dikirim
    - Pembaruan waktu nyata (*real-time updates*)
    - Tautan "View All Activity"

12. **Statistik Platform (*Platform Statistics*)**:
    - Metrik tambahan:
      * Total *booking* (sepanjang waktu): 8.523
      * Durasi sesi rata-rata: 57 menit
      * Tingkat pembatalan (*cancellation rate*): 4,2%
      * Kepuasan klien (*client satisfaction*): 4,8/5,0
      * Biaya platform terkumpul: Rp 18,5M (bulan)

**Interaksi & Perilaku:**
- Pembaruan data waktu nyata (*real-time data updates*) (*WebSocket*)
- Grafik interaktif (klik untuk detail)
- *Widget dashboard* yang dapat disesuaikan
- Kemampuan ekspor untuk semua data
- Desain responsif untuk tablet

***User Flow***:
Login admin → *Dashboard* → Ikhtisar tingkat tinggi → Identifikasi masalah/tren → Navigasi ke area manajemen spesifik

---

#### B. Manajemen Pengguna Admin (*Admin Users Management*)

**Deskripsi:**
Halaman Manajemen Pengguna memungkinkan admin untuk melihat (*view*), mencari (*search*), memfilter (*filter*), mengedit (*edit*), dan mengelola semua pengguna dalam platform (klien, terapis, admin).

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "Users Management"
   - Jumlah total pengguna dengan rincian
   - Tombol "Add New User" (pembuatan manual)
   - Tombol "Export Users" (CSV)

2. **Navigasi Tab (*Tabs Navigation*)**:
   - Semua Pengguna (*All Users*)
   - Klien (lencana jumlah)
   - Terapis (lencana jumlah)
   - Admin
   - Persetujuan Tertunda (*Pending Approvals*) (aplikasi terapis)
   - Disuspend/Dibanned (*Suspended/Banned*)

3. **Bagian Pencarian & Filter (*Search & Filter Section*)**:
   - Pencarian global: "Search by name, email, ID..."
   - Filter lanjutan (*advanced filters*):
     * Tipe pengguna: Semua, Klien, Terapis, Admin
     * Status: Aktif, Tidak Aktif, Tertunda, Disuspend, Dibanned
     * Rentang tanggal registrasi
     * Tanggal login terakhir
     * Status verifikasi: *Email*, Telepon, Lisensi (untuk terapis)
     * Lokasi (kota/wilayah)
   - Opsi urutkan: Terbaru, Nama A-Z, Paling Aktif

4. **Tabel Pengguna (*Users Table*)**:
   - Kolom:
     * **ID**: ID Pengguna (dapat diklik)
     * **Pengguna (*User*)**: *Avatar* + Nama + *Email*
     * **Tipe (*Type*)**: Lencana (Klien/Terapis/Admin)
     * **Status**: Lencana (Aktif/Tidak Aktif/Disuspend)
     * **Terdaftar (*Registered*)**: Tanggal
     * **Login Terakhir (*Last Login*)**: Waktu relatif
     * **Total Sesi (*Total Sessions*)**: Jumlah (jika berlaku)
     * **Dihabiskan/Diperoleh (*Spent/Earned*)**: Jumlah
     * **Verifikasi (*Verification*)**: Ikon (✓ *email*, ✓ telepon, ✓ lisensi)
     * **Tindakan (*Actions*)**: Menu *dropdown*
   
   - *Hover* baris: Sorot
   - Baris dapat diklik: Lihat detail

5. **Tindakan Massal (*Bulk Actions*)**:
   - Pilih beberapa pengguna (*checkbox*)
   - Operasi massal (*bulk operations*):
     * Ekspor yang dipilih
     * Kirim *email* massal
     * Ubah status (aktifkan/suspend)
     * Hapus pengguna (dengan konfirmasi)

6. **Menu Tindakan Pengguna (*User Actions Menu*)** (Per Baris):
   - *View Profile*
   - *Edit User*
   - *Impersonate* (login sebagai pengguna untuk *troubleshooting*)
   - *Send Email*
   - *View Activity Log*
   - Suspend/Aktifkan Akun
   - *Reset Password*
   - *Delete User*

7. ***Modal* Detail Pengguna (*User Detail Modal*)** (*Quick View*):
   - Terbuka saat baris diklik
   - Tab:
     * ***Overview***:
       - Informasi profil lengkap
       - Detail registrasi
       - Status verifikasi
       - Statistik akun
     
     * **Aktivitas (*Activity*)**:
       - Riwayat login
       - Linimasa tindakan (*actions timeline*)
       - Riwayat sesi (jika berlaku)
     
     * **Transaksi (*Transactions*)**:
       - Riwayat pembayaran
       - Penghasilan (jika terapis)
       - *Refund*
     
     * **Catatan (*Notes*)**:
       - Catatan admin tentang pengguna
       - Tanda/*warning*
       - Riwayat komunikasi
   
   - Tombol tindakan:
     * *Edit Profile*
     * Suspend/Aktifkan
     * *Send Message*
     * *View Full Profile*

8. **Aplikasi Terapis Tertunda (*Pending Therapist Applications*)** (Tab):
   - Daftar aplikasi terapis yang menunggu persetujuan
   - Setiap aplikasi:
     * Info pelamar
     * Dokumen yang dikirimkan
     * Tanggal aplikasi
     * Status tinjauan: *Pending*, *Under Review*, *Approved*, *Rejected*
   - Tindakan:
     * *View Application Details*
     * *Approve* (buka konfirmasi)
     * *Reject* (memerlukan alasan)
     * *Request More Info*

9. ***Modal* Tambah/Edit Pengguna (*Add/Edit User Modal*)**:
   - Bidang formulir:
     * Pemilihan tipe pengguna
     * Informasi pribadi
     * Detail kontak
     * Status akun
     * *Permission* (untuk admin)
   - Validasi
   - Tombol "Create User" / "Save Changes"

10. **Bagian Statistik (*Statistics Section*)**:
    - Grafik pertumbuhan pengguna
    - Tren pengguna aktif
    - Tingkat retensi (*retention rate*)
    - Tingkat *churn* (*churn rate*)

11. **Opsi Ekspor (*Export Options*)**:
    - Ekspor semua atau pengguna terfilter
    - Format: CSV, Excel
    - Bidang yang disertakan: *Checkbox*
    - Tombol "Generate Export"

**Interaksi & Perilaku:**
- Pencarian waktu nyata dengan *debounce*
- Kolom dapat diurutkan
- Kombinasi filter
- Tindakan cepat *modal*
- Dialog konfirmasi untuk tindakan destruktif
- Pencatatan aktivitas (*activity logging*) untuk tindakan admin
- Paginasi dengan item per halaman yang dapat dikonfigurasi

***User Flow***:
Admin → Manajemen Pengguna → Filter pengguna → Lihat detail → Ambil tindakan (*edit*, *suspend*, *approve*, dll.)

---

#### C. Manajemen *Booking* Admin (*Admin Bookings Management*)

**Deskripsi:**
Halaman Manajemen *Bookings* memberikan admin kontrol komprehensif atas semua janji temu (*appointments*) dalam platform, termasuk pemantauan (*monitoring*), modifikasi (*modifying*), dan penyelesaian masalah terkait *booking* (*resolving booking-related issues*).

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "Bookings Management"
   - Jumlah total *booking*
   - Pemilih rentang tanggal (lihat periode spesifik)

2. **Kartu Statistik Ringkasan (*Summary Statistics Cards*)**:
   - **Total *Bookings* (Periode)**: 1.247
   - **Mendatang (*Upcoming*)**: 342
   - **Selesai (*Completed*)**: 853
   - **Dibatalkan (*Cancelled*)**: 52 (4,2%)
   - ***No-Shows***: 15 (1,2%)
   - **Pendapatan Dihasilkan (*Revenue Generated*)**: Rp 374.100.000

3. **Navigasi Tab (*Tabs Navigation*)**:
   - Semua *Bookings* (*All Bookings*)
   - Mendatang (*Upcoming*)
   - Sesi Hari Ini (*Today's Sessions*)
   - Selesai (*Completed*)
   - Dibatalkan (*Cancelled*)
   - Sengketa/Masalah (*Disputed/Issues*)

4. **Pencarian & Filter (*Search & Filter*)**:
   - Pencarian: "Booking ID, client, or therapist name..."
   - Filter:
     * Rentang tanggal (*from - to*)
     * Status: Semua, Dikonfirmasi, Pembayaran Tertunda, Selesai, Dibatalkan, *No-show*
     * Tipe layanan: *Dropdown* semua layanan
     * Tipe sesi: Semua, *Online*, *Offline*
     * Terapis: Pilih terapis spesifik
     * Klien: Pilih klien spesifik
     * Status pembayaran: Semua, Dibayar, Tertunda, Di-*refund*
     * Rentang jumlah: Min - Maks
   - Tombol "Apply Filters"

5. **Tabel *Bookings***:
   - Kolom:
     * **ID *Booking***: #BK-2024-XXXXX (dapat diklik)
     * **Tanggal & Waktu (*Date & Time*)**: Tanggal/waktu terjadwal
     * **Klien (*Client*)**: Nama + *avatar* (tautan ke profil)
     * **Terapis (*Therapist*)**: Nama + *avatar* (tautan ke profil)
     * **Layanan (*Service*)**: Nama layanan
     * **Durasi (*Duration*)**: Menit
     * **Tipe (*Type*)**: Lencana *Online*/*Offline*
     * **Jumlah (*Amount*)**: Harga dalam Rp
     * **Pembayaran (*Payment*)**: Lencana status (Dibayar/Tertunda/Di-*refund*)
     * **Status**: Lencana status *booking*
     * **Tindakan (*Actions*)**: Menu *dropdown*
   
   - Kode warna (*color coding*):
     * Mendatang: Biru
     * Selesai: Hijau
     * Dibatalkan: Merah
     * Masalah: Oranye

6. **Menu Tindakan *Booking* (*Booking Actions Menu*)**:
   - *View Details*
   - *Edit Booking*
   - *Reschedule* (atas nama)
   - *Cancel Booking*
   - *Process Refund*
   - *Contact Client*
   - *Contact Therapist*
   - *View Session Notes*
   - Tandai sebagai Selesai/*No-show*
   - Tandai untuk Tinjauan (*Flag for Review*)

7. ***Modal* Detail *Booking* (*Booking Detail Modal*)**:
   - Tampilan komprehensif:
     * Informasi *booking* lengkap
     * Detail klien
     * Detail terapis
     * Detail layanan
     * Detail pembayaran
     * Riwayat transaksi
     * Log komunikasi
     * Catatan sesi (jika selesai)
     * *Timestamp* (dibuat, dikonfirmasi, selesai, dll.)
   
   - Tombol tindakan:
     * *Edit*
     * *Cancel* dengan opsi *refund*
     * *Reschedule*
     * *Generate Invoice*
     * *Send Reminder*
     * *Mark Completed*

8. **Operasi Massal (*Bulk Operations*)**:
   - Pilih beberapa *booking*
   - Tindakan massal (*bulk actions*):
     * Ekspor yang dipilih
     * Kirim pengingat (*reminders*)
     * Batalkan beberapa (dengan konfirmasi)
     * Ubah status
     * Buat laporan

9. ***Bookings* yang Disengketakan (*Disputed Bookings*)** (Tab):
   - *Bookings* yang ditandai untuk masalah:
     * Sengketa pembayaran
     * Keluhan klien
     * Laporan terapis
     * Permintaan *refund*
   - Setiap sengketa:
     * Detail *booking*
     * Tipe masalah
     * Deskripsi
     * Pelapor (*reporter*)
     * Status: Terbuka (*Open*), *Under Review*, Terselesaikan (*Resolved*)
   - Tindakan:
     * *Review Dispute*
     * *Resolve* (dengan catatan penyelesaian)
     * *Process Refund*
     * *Contact Parties*

10. **Tampilan Kalender (*Calendar View*)** (Opsional):
    - *Toggle* ke visualisasi kalender
    - Menampilkan semua *booking* di kalender
    - Dikodekan warna berdasarkan status
    - Klik tanggal → Lihat daftar *booking*
    - Klik *booking* → Tampilan detail

11. **Bagian Analitik (*Analytics Section*)**:
    - "Booking Trends"
    - Grafik:
      * *Bookings* per hari (grafik garis)
      * Distribusi layanan (grafik lingkaran)
      * Tingkat penyelesaian (*completion rate*) seiring waktu
      * Alasan pembatalan (grafik batang)
    - Ekspor analitik

12. **Ekspor & Laporan (*Export & Reports*)**:
    - "Generate Booking Report"
    - Pilih rentang tanggal
    - Pilih bidang yang disertakan
    - Format: CSV, Excel, PDF
    - Jadwalkan laporan otomatis (harian/mingguan/bulanan)

**Interaksi & Perilaku:**
- Pembaruan waktu nyata (*real-time updates*) untuk *booking* baru
- Pencarian lanjutan (*advanced search*) dengan *autocomplete*
- Editing sebaris (*inline editing*) untuk perubahan cepat
- *Modal* konfirmasi untuk tindakan kritis
- Pelacakan perubahan status (*status change tracking*)
- Perhitungan *refund* otomatis
- Notifikasi *email* pada tindakan

***User Flow***:
Admin → Manajemen *Bookings* → Filter *bookings* → Lihat detail → Ambil tindakan (*reschedule*, *cancel*, *refund*) → Catat penyelesaian

---

#### D. Laporan Keuangan Admin (*Admin Financial Reports*)

**Deskripsi:**
Halaman Laporan Keuangan memberikan admin wawasan terperinci (*detailed insights*) tentang pendapatan (*revenue*), pembayaran (*payments*), penarikan (*withdrawals*), dan kesehatan keuangan (*financial health*) dari platform.

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "Financial Reports"
   - Pemilih rentang tanggal (periode kustom)
   - Tombol "Export Financial Report"

2. **Kartu Ringkasan Pendapatan (*Revenue Summary Cards*)**:
   - **Total Pendapatan (Periode) (*Total Revenue Period*)**:
     * Jumlah: Rp 127.500.000
     * Tren vs periode sebelumnya
   
   - **Biaya Platform Terkumpul (*Platform Fees Collected*)**:
     * Jumlah: Rp 19.125.000 (15% dari pendapatan)
     * Tren
   
   - **Penghasilan Terapis (*Therapist Earnings*)**:
     * Jumlah: Rp 108.375.000 (85% dari pendapatan)
     * Tertunda (*Pending*): Rp 12,5M
     * Ditarik (*Withdrawn*): Rp 95,8M
   
   - **Pembayaran Tertunggak (*Outstanding Payments*)**:
     * Jumlah: Rp 3.250.000
     * *Bookings* tertunda

3. **Grafik Pendapatan (*Revenue Chart*)**:
   - "Revenue Over Time"
   - Grafik garis:
     * Total pendapatan
     * Biaya platform
     * Pembayaran terapis (*payouts*)
   - *Toggle*: Harian (*Daily*), Mingguan (*Weekly*), Bulanan (*Monthly*), Tahunan (*Yearly*)
   - Bandingkan periode: *Overlay* periode sebelumnya
   - *Tooltip* interaktif

4. **Rincian Pendapatan (*Revenue Breakdown*)**:
   - **Berdasarkan Tipe Layanan (*By Service Type*)**:
     * Tabel: Layanan | Sesi | Pendapatan | Persentase
     * Visualisasi grafik lingkaran (*pie chart*)
   
   - **Berdasarkan Tipe Sesi (*By Session Type*)**:
     * Pendapatan *Online* vs *Offline*
     * Perbandingan grafik batang
   
   - **Berdasarkan Metode Pembayaran (*By Payment Method*)**:
     * Kartu Kredit, Transfer Bank, *E-Wallet*, dll.
     * Persentase distribusi

5. **Tabel Transaksi (*Transactions Table*)**:
   - "All Transactions"
   - Kolom:
     * ID Transaksi
     * Tanggal & Waktu
     * Tipe: Pembayaran Diterima, *Refund*, Penarikan, dll.
     * ID *Booking* (tautan)
     * Klien/Terapis
     * Jumlah
     * Metode Pembayaran
     * Status: Berhasil (*Successful*), Tertunda (*Pending*), Gagal (*Failed*), Di-*refund*
     * Biaya Platform
     * Jumlah Bersih (*Net Amount*)
   - Filter berdasarkan tipe transaksi, status, tanggal
   - Ekspor transaksi

6. **Manajemen Penarikan (*Withdrawals Management*)**:
   - "Therapist Withdrawal Requests"
   - Tabel:
     * ID Permintaan (*Request ID*)
     * Nama terapis
     * Jumlah diminta
     * Tanggal permintaan
     * Metode penarikan
     * Status: *Pending*, *Processing*, *Completed*, *Failed*
     * Tindakan: *Approve*, *Reject*, *Mark Completed*
   
   - Tindakan *Approve*/*Reject*:
     * Pemeriksaan verifikasi
     * Proses pembayaran
     * Perbarui status
     * Kirim notifikasi

7. **Manajemen *Refund* (*Refunds Management*)**:
   - "Refund Requests & History"
   - Tabel:
     * ID *Refund*
     * *Booking* asli
     * Nama klien
     * Jumlah *refund*
     * Alasan
     * Tanggal permintaan
     * Status: *Pending*, *Approved*, *Processed*, *Rejected*
     * Tindakan: *Review*, *Approve*, *Process*, *Reject*
   
   - Pemrosesan *refund*:
     * Verifikasi kelayakan
     * Hitung jumlah (penuh/sebagian per kebijakan)
     * Proses ke metode pembayaran asli
     * Perbarui status *booking*
     * Beritahu klien

8. **Analitik Keuangan (*Financial Analytics*)**:
   - "Key Financial Metrics"
   - Metrik:
     * Nilai transaksi rata-rata (*average transaction value*)
     * Pendapatan per sesi (*revenue per session*)
     * Persentase biaya platform
     * Tingkat *refund* (*refund rate*)
     * Tingkat keberhasilan pembayaran (*payment success rate*)
     * Rata-rata penghasilan terapis
   - Grafik dan visualisasi

9. **Laporan Pajak (*Tax Reports*)** (Jika berlaku):
   - "Tax Summary"
   - Dokumen pajak yang dapat diunduh
   - Laporan kuartalan
   - Laporan tahunan
   - Ekspor untuk perangkat lunak akuntansi

10. **Sengketa & *Chargeback* (*Disputes & Chargebacks*)**:
    - "Payment Disputes"
    - Daftar transaksi yang disengketakan
    - Notifikasi *chargeback*
    - Pelacakan penyelesaian
    - Tindakan: Tanggapi (*Respond*), Berikan Bukti (*Provide Evidence*), Terima (*Accept*), Lawan (*Contest*)

11. **Status *Payment Gateway***:
    - Pemeriksaan kesehatan integrasi (*integration health checks*)
    - Tingkat keberhasilan transaksi per *gateway*
    - Peringatan *downtime*
    - Perbandingan biaya penyedia (*provider fees comparison*)

12. **Laporan Terjadwal (*Scheduled Reports*)**:
    - "Automated Reports"
    - Siapkan laporan keuangan berulang
    - Penerima (daftar *email*)
    - Frekuensi: Harian, Mingguan, Bulanan
    - Tipe laporan: Pendapatan, Transaksi, Pajak
    - Tombol "Add New Scheduled Report"

**Interaksi & Perilaku:**
- Pembaruan transaksi waktu nyata (*real-time transaction updates*)
- Grafik interaktif (*drill-down*)
- Ekspor Excel/PDF dengan pemformatan
- Penanganan data aman (*secure data handling*)
- Akses berbasis peran (*role-based access*) (hanya admin senior)
- Pencatatan audit (*audit logging*) untuk semua tindakan keuangan

***User Flow***:
Admin → Laporan Keuangan → Pilih periode → Analisis data → Proses penarikan/*refund* → Buat laporan → Ekspor untuk akuntansi

---

#### E. Pengaturan Sistem Admin (*Admin System Settings*)

**Deskripsi:**
Halaman Pengaturan Sistem memungkinkan admin untuk mengonfigurasi pengaturan platform global (*configure global platform settings*), mengelola preferensi sistem (*manage system preferences*), dan mengontrol berbagai parameter operasional (*control various operational parameters*).

**Elemen Utama:**
1. **Header Halaman (*Page Header*)**:
   - Judul: "System Settings"
   - Modifikasi terakhir: Tanggal + Nama admin
   - Tombol "Save All Changes" (*sticky*)

2. **Kategori Pengaturan (*Settings Categories*)** (Navigasi *Sidebar*):
   - Pengaturan Umum (*General Settings*)
   - Pengaturan *Booking* (*Booking Settings*)
   - Pengaturan Pembayaran (*Payment Settings*)
   - *Email* & Notifikasi (*Email & Notifications*)
   - Keamanan & Privasi (*Security & Privacy*)
   - Kebijakan Platform (*Platform Policies*)
   - Integrasi (*Integrations*)
   - Lanjutan (*Advanced*)

3. **Pengaturan Umum (*General Settings*)**:
   - **Informasi Platform (*Platform Information*)**:
     * Nama platform: "CUR-HEART"
     * *Tagline*
     * Deskripsi
     * Unggah logo (versi terang & gelap)
     * Unggah *favicon*
   
   - **Informasi Kontak (*Contact Information*)**:
     * *Email* dukungan
     * Nomor telepon
     * Alamat
     * Jam operasional
   
   - ***Timezone* & Lokal (*Timezone & Locale*)**:
     * *Timezone default*: Asia/Jakarta
     * Format tanggal: DD/MM/YYYY, MM/DD/YYYY
     * Format waktu: 12 jam, 24 jam
     * Mata uang: IDR
     * Bahasa: Indonesia, Inggris

4. **Pengaturan *Booking* (*Booking Settings*)**:
   - **Aturan *Booking* (*Booking Rules*)**:
     * Waktu minimum *booking* di muka: *Dropdown* jam
     * Waktu maksimum *booking* di muka: *Dropdown* minggu
     * Izinkan *booking* hari yang sama: *Toggle*
     * Durasi sesi *default*: Menit
     * Waktu *buffer* antar sesi: Menit
   
   - **Kebijakan Pembatalan (*Cancellation Policy*)**:
     * Periode pembatalan gratis: 24 jam
     * Periode *refund* sebagian: 12-24 jam (50%)
     * Periode tanpa *refund*: <12 jam
     * Kebijakan *no-show*
   
   - **Batasan *Booking* (*Booking Limits*)**:
     * Maks *booking* per klien per hari: Angka
     * Maks *booking* per terapis per hari: Angka
     * Aktifkan *waitlist*: *Toggle*

5. **Pengaturan Pembayaran (*Payment Settings*)**:
   - ***Payment Gateway***:
     * Konfigurasi Midtrans:
       - *Server key* (tersembunyi)
       - *Client key*
       - *Merchant ID*
       - Aktifkan mode *sandbox*: *Toggle*
     * Status: Terhubung (*Connected*) (hijau) / Terputus (*Disconnected*)
     * Tombol "Test Connection"
   
   - **Metode Pembayaran (*Payment Methods*)**:
     * Aktifkan/nonaktifkan metode:
       - Kartu Kredit/Debit (*toggle*)
       - Transfer Bank (*toggle*)
       - *E-Wallet* (GoPay, OVO, Dana, ShopeePay)
       - Akun Virtual (*Virtual Account*) (*toggle*)
   
   - **Harga & Biaya (*Pricing & Fees*)**:
     * Persentase biaya platform: 15% (*input*)
     * Jumlah *booking* minimum: Rp 100.000
     * Pengaturan mata uang
   
   - **Pengaturan *Refund* (*Refund Settings*)**:
     * *Auto-approve refund* di bawah: Jumlah Rp
     * Waktu pemrosesan *refund*: Hari
     * Aktifkan *refund* sebagian: *Toggle*

6. ***Email* & Notifikasi (*Email & Notifications*)**:
   - **Konfigurasi *Email* (*Email Configuration*)**:
     * Pengaturan SMTP:
       - *Host*
       - *Port*
       - *Username*
       - *Password*
       - Enkripsi (TLS/SSL)
     * Alamat *email* pengirim (*from email address*)
     * Nama pengirim (*from name*): "CUR-HEART"
     * Tombol "Send Test Email"
   
   - ***Template Email* (*Email Templates*)**:
     * Daftar *template*:
       - *Email* selamat datang (*welcome email*)
       - Konfirmasi *booking*
       - Pengingat *booking*
       - Sesi selesai
       - Tanda terima pembayaran (*payment receipt*)
       - *Reset password*
       - dll.
     * Setiap *template*: Tombol *Preview*, *Edit*
   
   - **Preferensi Notifikasi (*Notification Preferences*)**:
     * Notifikasi *email* aktifkan/nonaktifkan
     * Notifikasi SMS (jika terintegrasi)
     * Notifikasi *push*
     * Notifikasi dalam aplikasi (*in-app*)

7. **Keamanan & Privasi (*Security & Privacy*)**:
   - **Autentikasi (*Authentication*)**:
     * Persyaratan *password*:
       - Panjang minimum: 8 karakter
       - Memerlukan huruf besar: *Toggle*
       - Memerlukan angka: *Toggle*
       - Memerlukan karakter khusus: *Toggle*
     * *Timeout* sesi: Menit
     * Autentikasi dua faktor (2FA):
       - Aktifkan untuk admin: *Toggle*
       - Aktifkan untuk terapis: *Toggle*
       - Aktifkan untuk klien: *Toggle*
   
   - **Perlindungan Data (*Data Protection*)**:
     * Enkripsi data: Diaktifkan (*read-only*)
     * *Backup* otomatis: Harian
     * Retensi *backup*: Hari
     * Kepatuhan GDPR: Diaktifkan
     * Kebijakan retensi data: Tahun
   
   - **Pengaturan Privasi (*Privacy Settings*)**:
     * Tampilkan nama lengkap terapis: *Toggle*
     * Tampilkan ulasan klien secara publik: *Toggle*
     * Izinkan pengindeksan profil (SEO): *Toggle*

8. **Kebijakan Platform (*Platform Policies*)**:
   - **Syarat & Ketentuan (*Terms & Conditions*)**:
     * *Rich text editor*
     * Tanggal pembaruan terakhir
     * Tombol "Save Changes"
   
   - **Kebijakan Privasi (*Privacy Policy*)**:
     * *Rich text editor*
     * Tanggal pembaruan terakhir
   
   - **Kebijakan Pembatalan (*Cancellation Policy*)**:
     * *Rich text editor*
   
   - **Pedoman Komunitas (*Community Guidelines*)**:
     * *Rich text editor*

9. **Integrasi (*Integrations*)**:
   - **Google Analytics**:
     * *Input Tracking ID*
     * Aktifkan: *Toggle*
     * Status: Terhubung (*Connected*)
   
   - **Google Calendar**:
     * Koneksi OAuth
     * Tombol "Connect"
   
   - **Konferensi Video (*Video Conferencing*)**:
     * Penyedia: Jitsi, Zoom, kustom
     * Kredensial API
   
   - ***SMS Gateway*** (Opsional):
     * Pemilihan penyedia
     * *API key*
     * Aktifkan: *Toggle*
   
   - **Media Sosial (*Social Media*)**:
     * *Login* Facebook (OAuth)
     * *Login* Google (OAuth)
     * *Toggle* aktifkan/nonaktifkan

10. **Pengaturan Lanjutan (*Advanced Settings*)**:
    - **Mode Pemeliharaan (*Maintenance Mode*)**:
      * Aktifkan mode pemeliharaan: *Toggle*
      * Pesan pemeliharaan: *Textarea*
      * IP yang diizinkan (*Allowed IPs*): Dipisahkan koma
    
    - **Performa Sistem (*System Performance*)**:
      * Pengaturan *cache*
      * Penanganan sesi (*session handling*)
      * Konfigurasi CDN
    
    - **Pengaturan API (*API Settings*)**:
      * Pembatasan tingkat API (*API rate limiting*)
      * Manajemen *API key*
      * Konfigurasi *webhook*
    
    - **Log & Debugging**:
      * Aktifkan *error logging*: *Toggle*
      * Tingkat log: *Debug*, *Info*, *Warning*, *Error*
      * Retensi log: Hari
      * Tombol "View Logs"
      * Tombol "Clear Logs"

11. **Simpan & Terapkan (*Save & Apply*)**:
    - Tombol "Save All Changes" (*sticky footer*)
    - Tombol "Reset to Defaults"
    - Konfirmasi: "Settings saved successfully"
    - Peringatan untuk perubahan kritis: "This will affect all users"

**Validasi & Keamanan (*Validation & Safety*):**
- Pengaturan kritis memerlukan konfirmasi
- *Backup* sebelum perubahan besar
- Validasi pengaturan sebelum simpan
- Kemampuan *rollback*
- Pencatatan audit (*audit logging*) untuk semua perubahan

**Interaksi & Perilaku:**
- *Draft auto-save*
- Validasi pada *blur*
- Pratinjau perubahan sebelum terapkan
- Tombol tes untuk integrasi
- *Modal* konfirmasi untuk pengaturan kritis
- Indikator status waktu nyata
- Formulir responsif

***User Flow***:
Admin → Pengaturan Sistem → Navigasi ke kategori → Modifikasi pengaturan → Tes (jika berlaku) → Simpan → Konfirmasi → Pengaturan diterapkan ke seluruh platform

---

### 4.3.5.10 Pendekatan Desain Responsif (*Responsive Design Approach*)

Dalam pengembangan UI/UX CUR-HEART, pendekatan desain responsif (*responsive design*) diterapkan untuk memastikan aplikasi dapat diakses dan digunakan secara optimal di berbagai perangkat (*desktop*, *tablet*, *mobile*). Berikut adalah strategi dan implementasi desain responsif:

---

**[GAMBAR 4.61 - Ilustrasi *Breakpoint* Desain Responsif (*Responsive Design Breakpoints Illustration*)]** 📱💻
_Visualisasi *breakpoint*: *mobile* (320-767px), *tablet* (768-1023px), *desktop* (1024px+)_

**[GAMBAR 4.62 - Perbandingan Tata Letak *Mobile* vs *Desktop* (*Mobile vs Desktop Layout Comparison*)]** 📱💻
_Perbandingan berdampingan halaman utama, *dashboard*, dan alur *booking* pada *mobile* vs *desktop*_

**[GAMBAR 4.63 - Panduan Ukuran Target Sentuh (Minimum 44px) (*Touch Target Size Guidelines*)]** 👆
_Ukuran tombol dan elemen interaktif untuk kegunaan *mobile* (sesuai WCAG 2.1)_

**[GAMBAR 4.64 - Fitur Aksesibilitas - Kepatuhan WCAG (*Accessibility Features - WCAG Compliance*)]** ♿
_Rasio kontras warna, navigasi keyboard, dukungan pembaca layar, teks alt_

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
   - *Mobile*: Kolom tunggal, label di atas input, target sentuh lebih besar (minimal 44px)

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

8. **Widget *Dashboard***:
   - *Desktop*: *Grid* multi-kolom, seret & lepas (*drag & drop*)
   - *Mobile*: Kolom tunggal, urutan prioritas, bagian yang dapat dilipat

9. **Grafik & Diagram (*Charts & Graphs*)**:
   - Berbasis SVG (dapat diskalakan)
   - Tampilan sederhana pada *mobile*
   - Interaksi ramah sentuh (cubit, zoom)

**Optimasi Sentuh & Gestur (*Touch & Gesture Optimization*):**
- Target sentuh minimal: 44x44px (standar Apple HIG)
- Spasi memadai antar elemen interaktif
- Gestur geser: Navigasi *carousel*, geser-untuk-hapus
- Tarik-untuk-muat-ulang (*pull-to-refresh*) pada *mobile*
- Menu konteks tekan-lama (*long-press*)

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
- **Teks yang Dapat Diubah Ukurannya (*Resizable Text*)**: Mendukung zoom browser hingga 200%

**3. Kinerja & Kecepatan (*Performance & Speed*):**
- **Waktu Muat Halaman (*Page Load Time*)**: Target <3 detik untuk *first contentful paint*
- ***Lazy Loading***: Gambar, komponen dimuat sesuai permintaan
- **Strategi *Caching***: Aset statis di-*cache*, konten dinamis segar
- **Aset yang Dioptimalkan (*Optimized Assets*)**: Gambar terkompresi, CSS/JS diminifikasi
- **Kinerja yang Dirasakan (*Perceived Performance*)**: Layar *skeleton*, pemuatan progresif

**4. Pencegahan & Pemulihan Kesalahan (*Error Prevention & Recovery*):**
- **Validasi Sebaris (*Inline Validation*)**: Umpan balik waktu nyata pada input formulir
- **Dialog Konfirmasi (*Confirmation Dialogs*)**: Untuk tindakan destruktif (hapus, batalkan *booking*)
- **Kemampuan Membatalkan (*Undo Capabilities*)**: Jika memungkinkan (penyimpanan draft)
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
- **Umpan Balik Formulir (*Form Feedback*)**: Tanda centang untuk input valid, animasi goyang untuk kesalahan
- ***Notification Toast***: Geser masuk dengan halus, tutup otomatis

**9. Strategi Konten (*Content Strategy*):**
- **Konten yang Dapat Dipindai (*Scannable Content*)**: Judul, poin *bullet*, paragraf pendek
- **Pengungkapan Progresif (*Progressive Disclosure*)**: Tampilkan info penting dulu, detail sesuai permintaan
- **Bahasa Sederhana (*Plain Language*)**: Hindari jargon medis, jelaskan istilah bila perlu
***Placeholder* yang Membantu (*Helpful Placeholders*)**: Teks contoh dalam kolom input
- **Bantuan Kontekstual (*Contextual Help*)**: Ikon info dengan *tooltip*

**10. Pertimbangan Mengutamakan *Mobile* (*Mobile-First Considerations*):**
- **Ramah Jempol (*Thumb-Friendly*)**: Tindakan penting dalam jangkauan mudah
- **Input Minimal (*Minimal Input*)**: Gunakan *picker*, *dropdown* daripada mengetik jika memungkinkan
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

**Dokumentasi visual lengkap dari 41 *mockup* halaman tersedia di:**
`/var/www/unm-s7/tugas-selesai/06_rintisan_bisnis_digital/mockups/`

*Mockup-mockup* tersebut dapat diakses dan ditinjau untuk implementasi pengembangan, pengujian pengguna (*user testing*), dan presentasi pemangku kepentingan (*stakeholder presentations*).

---

*Catatan: Tangkapan layar (*screenshot*) visual dan detail implementasi teknis dari setiap *mockup* dapat dilihat pada file HTML yang tersimpan di direktori *mockups*. Setiap file HTML merupakan prototipe fungsional (*functional prototype*) yang dapat dibuka di browser untuk melihat interaksi dan responsivitas secara langsung.*
