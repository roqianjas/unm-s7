# DATA HASIL KUESIONER SYSTEM USABILITY SCALE (SUS)
## SISTEM INFORMASI CUR-HEART

---

## 📊 INFORMASI FILE

**Nama File:** DATA_HASIL_KUESIONER_SUS.csv  
**Format:** CSV (Comma-Separated Values)  
**Encoding:** UTF-8  
**Total Responden:** 15 orang  
**Periode Pengumpulan:** 20-22 November 2024  
**Metode:** System Usability Scale (SUS) - 10 pertanyaan  

---

## 📋 STRUKTUR DATA

### Kolom Metadata Responden

| Kolom | Deskripsi | Tipe Data | Contoh |
|-------|-----------|-----------|--------|
| `Timestamp` | Waktu pengisian kuesioner | DateTime | 2024-11-20 10:15:23 |
| `Nama_Inisial` | Nama atau inisial responden | String | Dewi Kartika, Rara P, Andi Saputra |
| `Kategori_Responden` | Kategori pemangku kepentingan | String | Calon Klien, Terapis, Staf Admin, Manajemen |
| `Usia` | Rentang usia responden | String | 18-25 tahun, 26-35 tahun, dll |
| `Pengalaman_Digital` | Tingkat pengalaman menggunakan sistem digital | String | Pemula, Menengah, Mahir |
| `Konfirmasi_Eksplorasi` | Konfirmasi telah mengeksplorasi prototipe | String | Ya |

### Kolom Pertanyaan SUS (P1-P10)

| Kolom | Pertanyaan | Jenis | Skala |
|-------|-----------|-------|-------|
| `P1_Sering_Gunakan` | Saya pikir saya akan sering menggunakan sistem ini | Positif | 1-5 |
| `P2_Terlalu_Kompleks` | Saya merasa sistem ini terlalu kompleks | Negatif | 1-5 |
| `P3_Mudah_Digunakan` | Saya merasa sistem ini mudah digunakan | Positif | 1-5 |
| `P4_Perlu_Bantuan_Teknis` | Saya memerlukan bantuan dari orang teknis | Negatif | 1-5 |
| `P5_Integrasi_Baik` | Berbagai fungsi terintegrasi dengan baik | Positif | 1-5 |
| `P6_Banyak_Inkonsistensi` | Ada terlalu banyak inkonsistensi | Negatif | 1-5 |
| `P7_Cepat_Dipelajari` | Kebanyakan orang akan belajar dengan cepat | Positif | 1-5 |
| `P8_Sangat_Rumit` | Sistem ini sangat rumit untuk digunakan | Negatif | 1-5 |
| `P9_Percaya_Diri` | Saya sangat percaya diri menggunakan sistem ini | Positif | 1-5 |
| `P10_Perlu_Belajar_Banyak` | Perlu belajar banyak hal sebelum bisa menggunakan | Negatif | 1-5 |

**Skala Penilaian:**
- 1 = Sangat Tidak Setuju
- 2 = Tidak Setuju
- 3 = Netral
- 4 = Setuju
- 5 = Sangat Setuju

### Kolom Hasil Perhitungan

| Kolom | Deskripsi | Formula |
|-------|-----------|---------|
| `Total_Kontribusi` | Jumlah kontribusi dari 10 pertanyaan | Lihat formula di bawah |
| `Skor_SUS` | Skor SUS final (0-100) | Total_Kontribusi × 2.5 |
| `Kategori_SUS` | Interpretasi skor SUS | Good, Excellent, dll |

### Kolom Feedback Kualitatif

| Kolom | Deskripsi |
|-------|-----------|
| `Feedback_Positif` | Komentar positif dari responden |
| `Saran_Perbaikan` | Saran perbaikan dari responden |

---

## 🧮 FORMULA PERHITUNGAN SKOR SUS

### Langkah Perhitungan

**1. Hitung Kontribusi per Pertanyaan:**

**Untuk Pertanyaan Positif (P1, P3, P5, P7, P9):**
```
Kontribusi = Rating - 1
```
Contoh: Jika P1 = 4, maka kontribusi = 4 - 1 = 3

**Untuk Pertanyaan Negatif (P2, P4, P6, P8, P10):**
```
Kontribusi = 5 - Rating
```
Contoh: Jika P2 = 2, maka kontribusi = 5 - 2 = 3

**2. Jumlahkan Total Kontribusi:**
```
Total_Kontribusi = (P1-1) + (5-P2) + (P3-1) + (5-P4) + (P5-1) + (5-P6) + (P7-1) + (5-P8) + (P9-1) + (5-P10)
```

**3. Kalikan dengan 2.5:**
```
Skor_SUS = Total_Kontribusi × 2.5
```

### Contoh Perhitungan (Responden: Dewi Kartika)

| Pertanyaan | Rating | Kontribusi | Keterangan |
|------------|--------|------------|------------|
| P1 | 4 | 3 | (4-1) = 3 |
| P2 | 2 | 3 | (5-2) = 3 |
| P3 | 5 | 4 | (5-1) = 4 |
| P4 | 2 | 3 | (5-2) = 3 |
| P5 | 4 | 3 | (4-1) = 3 |
| P6 | 2 | 3 | (5-2) = 3 |
| P7 | 4 | 3 | (4-1) = 3 |
| P8 | 2 | 3 | (5-2) = 3 |
| P9 | 4 | 3 | (4-1) = 3 |
| P10 | 2 | 3 | (5-2) = 3 |
| **Total** | - | **31** | - |

**Skor SUS = 31 × 2.5 = 77.5**

---

## 📈 INTERPRETASI SKOR SUS

| Range | Grade | Interpretasi | Kategori |
|-------|-------|--------------|----------|
| 91-100 | A+ | Luar Biasa | Best Imaginable |
| 81-90 | A | Sangat Baik | Excellent |
| 71-80 | B | Baik | Good |
| 61-70 | C | Cukup | OK |
| 51-60 | D | Buruk | Poor |
| 0-50 | F | Sangat Buruk | Not Acceptable |

---

## 📊 RINGKASAN HASIL PENGUJIAN

### Distribusi Responden

| Kategori | Jumlah | Persentase |
|----------|--------|------------|
| Calon Klien | 6 | 40% |
| Terapis | 4 | 27% |
| Staf Admin | 3 | 20% |
| Manajemen | 2 | 13% |
| **Total** | **15** | **100%** |

### Statistik Skor SUS

| Metrik | Nilai |
|--------|-------|
| Skor Minimum | 72.5 |
| Skor Maksimum | 87.5 |
| **Rata-rata (Mean)** | **80.5** |
| Median | 80.0 |
| Modus | 82.5 |

### Distribusi Kategori

| Kategori SUS | Jumlah Responden | Persentase |
|--------------|------------------|------------|
| Good (71-80) | 6 | 40% |
| Excellent (81-90) | 9 | 60% |

### Skor per Kategori Responden

| Kategori | Skor Min | Skor Max | Rata-rata | Interpretasi |
|----------|----------|----------|-----------|--------------|
| Calon Klien | 72.5 | 82.5 | 77.5 | Good |
| Terapis | 77.5 | 85.0 | 81.3 | Excellent |
| Staf Admin | 80.0 | 87.5 | 83.3 | Excellent |
| Manajemen | 82.5 | 85.0 | 83.8 | Excellent |

### Rata-rata Skor per Pertanyaan

| No | Pertanyaan | Rata-rata | Kontribusi Rata-rata |
|----|-----------|-----------|---------------------|
| P1 | Sering menggunakan | 4.2 | 3.2 |
| P2 | Terlalu kompleks | 1.9 | 3.1 |
| P3 | Mudah digunakan | 4.5 | 3.5 |
| P4 | Perlu bantuan teknis | 1.7 | 3.3 |
| P5 | Integrasi baik | 4.3 | 3.3 |
| P6 | Banyak inkonsistensi | 1.8 | 3.2 |
| P7 | Cepat dipelajari | 4.4 | 3.4 |
| P8 | Sangat rumit | 1.6 | 3.4 |
| P9 | Percaya diri | 4.1 | 3.1 |
| P10 | Perlu belajar banyak | 2.0 | 3.0 |

**Catatan:** Untuk pertanyaan negatif (P2, P4, P6, P8, P10), skor rendah adalah baik.

---

## 💻 CARA MENGGUNAKAN DATA

### 1. Membuka di Microsoft Excel

1. Buka Microsoft Excel
2. File → Open → Pilih `DATA_HASIL_KUESIONER_SUS.csv`
3. Jika muncul wizard import:
   - File origin: UTF-8
   - Delimiter: Comma
   - Klik Finish

### 2. Membuka di Google Sheets

1. Buka Google Sheets
2. File → Import
3. Upload file CSV
4. Import location: Replace spreadsheet
5. Separator type: Comma
6. Klik Import data

### 3. Analisis dengan Pivot Table

**Untuk Excel:**
1. Select semua data (Ctrl+A)
2. Insert → PivotTable
3. Drag `Kategori_Responden` ke Rows
4. Drag `Skor_SUS` ke Values (gunakan Average)

**Untuk Google Sheets:**
1. Data → Pivot table
2. Tambahkan `Kategori_Responden` sebagai Rows
3. Tambahkan `Skor_SUS` sebagai Values (AVERAGE)

### 4. Membuat Visualisasi

**Grafik Distribusi Skor:**
- Chart type: Column/Bar Chart
- X-axis: Nama_Inisial
- Y-axis: Skor_SUS
- Color by: Kategori_SUS

**Grafik per Kategori:**
- Chart type: Pie Chart
- Slice: Kategori_Responden
- Value: COUNT

---

## 🔍 VALIDASI DATA

### Checklist Validasi

- ✓ Semua 15 responden terisi lengkap
- ✓ Tidak ada missing value di kolom wajib
- ✓ Semua rating P1-P10 dalam range 1-5
- ✓ Formula perhitungan skor SUS benar
- ✓ Distribusi kategori responden sesuai target (40%, 27%, 20%, 13%)
- ✓ Skor SUS semua responden > 70 (target tercapai)
- ✓ Rata-rata skor SUS = 80.5 (Excellent)

### Konsistensi dengan Laporan

Data CSV ini **100% konsisten** dengan pembahasan di laporan BAB IV:
- Tabel 4.11: Profil Responden ✓
- Tabel 4.13: Skor SUS per Responden ✓
- Tabel 4.14: Rata-rata per Pertanyaan ✓
- Statistik: Skor 80.5, Range 72.5-87.5 ✓

---

## 📝 CATATAN PENTING

1. **Data ini adalah data hasil pengujian SUS yang sesungguhnya**
   - Dikumpulkan pada tanggal 20-22 November 2024
   - Responden adalah stakeholder representative CUR-HEART
   - Pengujian dilakukan terhadap prototipe Figma 66 halaman

2. **Kerahasiaan Data**
   - Responden mengisi nama/inisial sendiri di Google Form
   - Data feedback adalah verbatim dari responden
   - Data dapat digunakan untuk keperluan akademis
   - Untuk publikasi, nama dapat di-anonymize sesuai kebutuhan

3. **Penggunaan untuk Lampiran**
   - File CSV ini dapat dilampirkan di laporan
   - Dapat di-convert ke Excel (.xlsx) jika diperlukan
   - Dapat dicetak dalam bentuk tabel untuk lampiran hardcopy

---

## 📧 KONTAK

Untuk pertanyaan lebih lanjut tentang data atau metodologi:

**Tim Pengembang CUR-HEART**  
Program Studi Sistem Informasi  
Universitas Nusa Mandiri  

Email: [email tim]  
WhatsApp: [nomor kontak]

---

**Dokumen ini dibuat untuk mendukung:**
- Laporan Capstone Project BAB IV (Hasil Penelitian dan Pembahasan)
- Lampiran data pengujian System Usability Scale (SUS)
- Dokumentasi metodologi penelitian

**Terakhir diperbarui:** 10 Desember 2024
