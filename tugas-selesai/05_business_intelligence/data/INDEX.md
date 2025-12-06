# 📚 Index - Data SATRIAMART BI Project

## 🗂️ Struktur Lengkap

```
data/
├── raw/                              # Data mentah (dengan masalah)
│   ├── 01_master_produk_raw.csv      # 20 baris, 8 masalah (40%)
│   ├── 02_master_pelanggan_raw.csv   # 20 baris, 7 masalah (35%)
│   ├── 03_transaksi_penjualan_raw.csv # 20 baris, 3 masalah (15%)
│   ├── 04_riwayat_stok_raw.csv       # 40 baris, 4 masalah (10%)
│   ├── 05_biaya_operasional_raw.csv  # 30 baris, 6 masalah (20%)
│   └── 06_marketing_campaign_raw.csv # 28 baris, 10 masalah (36%)
│
├── clean/                            # Data bersih (siap analisis)
│   ├── 01_master_produk.csv          # 50 produk
│   ├── 02_master_pelanggan.csv       # 180 pelanggan
│   ├── 03_transaksi_penjualan.csv    # 320 transaksi
│   ├── 04_riwayat_stok.csv           # Riwayat stok lengkap
│   ├── 05_biaya_operasional.csv      # Biaya operasional
│   └── 06_marketing_campaign.csv     # 24 campaigns
│
├── README.md                         # Dokumentasi data original
├── README_DATA_QUALITY.md            # Dokumentasi lengkap data quality
├── MASALAH_DATA_SUMMARY.md           # Quick reference masalah data
├── PANDUAN_SCREENSHOT.md             # Panduan membuat screenshot
├── INDEX.md                          # File ini
└── generate_all_data.py              # Script generator data
```

---

## 📖 Panduan Penggunaan

### 1. Untuk Memahami Data Quality Issues
**Baca:** `MASALAH_DATA_SUMMARY.md`
- Quick reference semua masalah
- Tabel ringkasan per file
- Highlight untuk screenshot

### 2. Untuk Detail Lengkap Data Quality
**Baca:** `README_DATA_QUALITY.md`
- Penjelasan detail setiap masalah
- Solusi pembersihan
- Proses ETL
- Statistik lengkap

### 3. Untuk Membuat Screenshot
**Baca:** `PANDUAN_SCREENSHOT.md`
- Step-by-step cara screenshot
- Layout recommendations
- Tools yang digunakan
- Tips profesional

### 4. Untuk Informasi Data Original
**Baca:** `README.md`
- Deskripsi dataset
- Struktur data
- Metadata

---

## 🎯 Quick Start

### Untuk Laporan BI:

#### Step 1: Pahami Masalah Data
```bash
1. Buka: MASALAH_DATA_SUMMARY.md
2. Lihat tabel ringkasan masalah
3. Catat masalah utama untuk dijelaskan
```

#### Step 2: Buat Screenshot Data Raw
```bash
1. Upload file dari folder raw/ ke Google Sheets
2. Highlight masalah sesuai panduan
3. Screenshot dengan resolusi tinggi
4. Save di folder screenshots/01_data_quality/before/
```

#### Step 3: Buat Screenshot Data Clean
```bash
1. Upload file dari folder clean/ ke Google Sheets
2. Tunjukkan data sudah bersih
3. Screenshot dengan resolusi tinggi
4. Save di folder screenshots/01_data_quality/after/
```

#### Step 4: Buat Screenshot Dashboard
```bash
1. Buka dashboard Looker Studio
2. Screenshot setiap halaman (7 halaman)
3. Screenshot fitur interaktif
4. Save di folder screenshots/02_dashboard/
```

#### Step 5: Susun di Laporan
```bash
1. Insert screenshot di BAB III (Pembahasan)
2. Tambahkan caption dan penjelasan
3. Buat perbandingan before/after
4. Highlight insight dari dashboard
```

---

## 📊 Statistik Data

### Data Raw (Mentah)
| Metrik | Nilai |
|--------|-------|
| Total Files | 6 files |
| Total Baris | 158 baris |
| Total Masalah | 38 masalah |
| Persentase Masalah | 24% |
| Data Completeness | 87% |

### Data Clean (Bersih)
| Metrik | Nilai |
|--------|-------|
| Total Files | 6 files |
| Total Baris | 600+ baris |
| Total Masalah | 0 masalah |
| Persentase Masalah | 0% |
| Data Completeness | 100% |

---

## 🔍 Jenis Masalah Data

### Breakdown Masalah di Data Raw:
1. **Missing Values** (20 masalah, 53%)
   - Kolom kosong yang seharusnya terisi
   - Impact: Analisis tidak lengkap
   
2. **Format Tidak Konsisten** (15 masalah, 39%)
   - Tanggal: DD/MM/YYYY vs YYYY-MM-DD
   - Impact: Error saat parsing
   
3. **Inkonsistensi Kapitalisasi** (12 masalah, 32%)
   - "aktif" vs "Aktif"
   - "NAMA" vs "Nama"
   - Impact: Grouping salah
   
4. **Data Tidak Realistis** (4 masalah, 11%)
   - Nilai terlalu besar/kecil
   - Impact: Insight menyesatkan
   
5. **Duplikasi** (1 masalah, 3%)
   - Baris yang sama muncul 2x
   - Impact: Perhitungan ganda

---

## 🛠️ Tools yang Digunakan

### Untuk Data Cleaning:
- ✅ Microsoft Excel / Google Sheets
- ✅ Python (Pandas) - optional
- ✅ Google Sheets Functions

### Untuk Screenshot:
- ✅ Snipping Tool (Windows)
- ✅ Awesome Screenshot (Chrome)
- ✅ Snagit (Professional)

### Untuk Dashboard:
- ✅ Google Looker Studio
- ✅ Google Sheets (data source)

### Untuk Dokumentasi:
- ✅ Markdown
- ✅ Microsoft Word
- ✅ Google Docs

---

## 📝 Checklist Kelengkapan

### Data Files:
- [x] Raw data (6 files) ✅
- [x] Clean data (6 files) ✅
- [x] Dokumentasi data quality ✅
- [x] Panduan screenshot ✅

### Screenshots:
- [ ] Data raw (6 screenshots)
- [ ] Data clean (6 screenshots)
- [ ] Dashboard pages (7 screenshots)
- [ ] Interactive features (3 screenshots)

### Laporan:
- [ ] BAB I: Pendahuluan
- [ ] BAB II: Landasan Teori
- [ ] BAB III: Pembahasan (dengan screenshots)
- [ ] BAB IV: Kesimpulan
- [ ] Lampiran

---

## 🎓 Tips untuk Presentasi

### Highlight Points:
1. **Data Quality Matters**
   - "24% data memiliki masalah"
   - "Setelah cleaning: 100% valid"
   
2. **ETL Process**
   - Extract → Transform → Load
   - Automated dengan script
   
3. **Impact**
   - Data kotor = Keputusan salah
   - Data bersih = Insight akurat
   
4. **Dashboard Value**
   - Real-time monitoring
   - Interactive exploration
   - Data-driven decisions

---

## 📞 Support

Jika ada pertanyaan tentang:
- **Data structure**: Lihat README.md
- **Data quality**: Lihat README_DATA_QUALITY.md
- **Screenshot**: Lihat PANDUAN_SCREENSHOT.md
- **Quick reference**: Lihat MASALAH_DATA_SUMMARY.md

---

## 🔗 Related Files

- [README.md](./README.md) - Dokumentasi data original
- [README_DATA_QUALITY.md](./README_DATA_QUALITY.md) - Detail data quality
- [MASALAH_DATA_SUMMARY.md](./MASALAH_DATA_SUMMARY.md) - Quick reference
- [PANDUAN_SCREENSHOT.md](./PANDUAN_SCREENSHOT.md) - Screenshot guide

---

**Dibuat oleh:** Tim BI SATRIAMART  
**Tanggal:** Desember 2024  
**Versi:** 1.0  
**Status:** ✅ Complete
