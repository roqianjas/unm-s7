# Panduan Desain Slide Presentasi CUR-HEART

## Spesifikasi Desain

### Rasio & Dimensi
- **Rasio**: 16:9 (standar PowerPoint)
- **Resolusi Optimal**: 1920x1080px
- **Viewport**: 100vw x 100vh dengan max-width/height

### Palet Warna (Sistem CurHeart)
```css
--cur-primary: #1E0E62        /* Ungu Tua - Brand Primary */
--cur-primary-light: #2D1B69  /* Ungu Sedang */
--cur-primary-dark: #150A4A   /* Ungu Gelap */
--cur-secondary: #FF6B7A      /* Merah Muda - Accent */
--cur-secondary-light: #FF8A96
--cur-secondary-dark: #E64555
--cur-accent: #FFB6B9         /* Pink Lembut */
--cur-warm: #FFEAA7           /* Kuning Hangat */
--cur-success: #00D26A        /* Hijau */
--cur-warning: #FFA94D        /* Oranye */
--cur-info: #667BC6           /* Biru */
```

### Tipografi
- **Font Utama**: Poppins (Judul, Heading)
- **Font Sekunder**: Inter (Body Text)
- **Ukuran**:
  - Judul Slide: 48px (bold/700)
  - Sub-judul: 28-36px (semibold/600)
  - Body Text: 16-18px (regular/400)
  - Caption: 14px (regular/400)

### Struktur Slide

#### 1. Header (Fixed)
- Logo CurHeart (kiri) + Judul Slide
- Nomor Slide (kanan)
- Divider gradient (cur-primary → cur-secondary)

#### 2. Content Area
- Padding: 40px 60px
- Spacing konsisten
- Card-based layout dengan shadow

#### 3. Navigation (Fixed Bottom)
- Tombol Sebelumnya (kiri bawah)
- Tombol Selanjutnya (kanan bawah)
- Style: rounded-full dengan gradient

### Prinsip Desain
1. **Minimalis**: Fokus pada konten, hindari elemen berlebihan
2. **Konsisten**: Gunakan komponen yang sama di semua slide
3. **Profesional**: Warna brand, tipografi jelas, spacing rapi
4. **Modern**: Gradient, shadow, rounded corners
5. **Accessible**: Kontras warna yang baik, ukuran font readable

### Komponen Reusable
- Card dengan border-left accent
- Badge dengan background gradient
- Icon box dengan background color/10
- Stats box dengan angka besar + deskripsi
- Grid layout 2-3 kolom

## Daftar Slide

1. **Sampul** - Cover dengan gradient background
2. **Latar Belakang** - Konteks masalah kesehatan mental
3. **Rumusan Masalah** - 5 pertanyaan penelitian
4. **Tujuan** - Tujuan utama + 6 tujuan spesifik
5. **Metodologi** - Design Thinking Process
6. **Business Model Canvas** - BMC lengkap
6A. **Market Opportunity** - Analisis pasar
6B. **Competitive Analysis** - Analisis kompetitor
6C. **Team** - Tim pengembang
6D. **Go-to-Market Strategy** - Strategi pemasaran
6E. **Financial Projections** - Proyeksi keuangan
6F. **Milestones & Roadmap** - Pencapaian & rencana
7. **Analisis & Perancangan** - Sistem informasi
8. **Desain UI/UX** - Mockup & prototipe
9. **Hasil & Pengujian** - Testing & validasi
10. **Kesimpulan & Saran** - Penutup

## Catatan Bahasa
- Gunakan Bahasa Indonesia yang baik dan benar (KBBI, EYD)
- Istilah teknis: gunakan bahasa Inggris jika tidak ada padanan yang tepat
- Konsisten dalam penggunaan istilah
