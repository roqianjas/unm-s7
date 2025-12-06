# 📸 Panduan Screenshot untuk Laporan BI

## 🎯 Tujuan
Panduan ini membantu Anda membuat screenshot yang profesional dan informatif untuk laporan Business Intelligence SATRIAMART.

---

## 📋 Daftar Screenshot yang Dibutuhkan

### A. Data Quality (Before & After)
1. ✅ Master Produk - Raw vs Clean
2. ✅ Master Pelanggan - Raw vs Clean
3. ✅ Transaksi Penjualan - Raw vs Clean
4. ✅ Riwayat Stok - Raw vs Clean
5. ✅ Biaya Operasional - Raw vs Clean
6. ✅ Marketing Campaign - Raw vs Clean

### B. Dashboard Looker Studio
7. ✅ Executive Dashboard (Halaman 1)
8. ✅ Sales Analysis (Halaman 2)
9. ✅ Product Performance (Halaman 3)
10. ✅ Customer Analytics (Halaman 4)
11. ✅ Financial Dashboard (Halaman 5)
12. ✅ Operations & Inventory (Halaman 6)
13. ✅ Marketing Performance (Halaman 7)

### C. Fitur Interaktif
14. ✅ Filter controls (date range, category)
15. ✅ Drill-down example
16. ✅ Cross-filtering example

---

## 🖼️ Cara Membuat Screenshot Data Quality

### Step 1: Buka Data Raw di Google Sheets

1. Upload file dari `data/raw/` ke Google Sheets
2. Buka file (contoh: `01_master_produk_raw.csv`)

### Step 2: Highlight Masalah Data

**Gunakan Conditional Formatting atau Manual Highlight:**

#### Untuk Missing Values (Sel Kosong):
```
1. Select sel yang kosong
2. Format → Fill color → Red (#FF0000)
3. Tambahkan comment: "Missing value"
```

#### Untuk Format Tidak Konsisten:
```
1. Select sel dengan format salah (contoh: 15/01/2024)
2. Format → Fill color → Yellow (#FFFF00)
3. Tambahkan comment: "Format tidak konsisten"
```

#### Untuk Duplikasi:
```
1. Select baris duplikat
2. Format → Fill color → Orange (#FFA500)
3. Tambahkan comment: "Data duplikat"
```

#### Untuk Kapitalisasi Salah:
```
1. Select sel dengan kapitalisasi salah
2. Format → Fill color → Light Blue (#ADD8E6)
3. Tambahkan comment: "Inkonsistensi kapitalisasi"
```

### Step 3: Ambil Screenshot

**Pengaturan Screenshot:**
- Zoom: 100% atau 125% (agar teks jelas)
- Tampilkan: 10-15 baris data
- Include: Header kolom
- Format: PNG atau JPG (resolusi tinggi)

**Tools Screenshot:**
- Windows: Win + Shift + S
- Mac: Cmd + Shift + 4
- Chrome Extension: Awesome Screenshot

### Step 4: Annotate (Opsional)

Gunakan tools seperti:
- Snagit
- Greenshot
- Paint / Paint 3D
- PowerPoint

Tambahkan:
- Arrow/callout ke masalah
- Text box dengan penjelasan singkat
- Numbering untuk multiple issues

---

## 📊 Contoh Layout Screenshot Data Quality

### Layout 1: Side by Side
```
┌─────────────────────────┬─────────────────────────┐
│   BEFORE (Raw Data)     │   AFTER (Clean Data)    │
│                         │                         │
│  [Screenshot dengan     │  [Screenshot tanpa      │
│   highlight masalah]    │   masalah, semua OK]    │
│                         │                         │
│  ❌ Missing values      │  ✅ All filled          │
│  ❌ Format inconsistent │  ✅ Standardized        │
│  ❌ Duplicates          │  ✅ Removed             │
└─────────────────────────┴─────────────────────────┘
```

### Layout 2: Vertical (Before → After)
```
┌─────────────────────────────────────┐
│   BEFORE: Master Produk (Raw)       │
│   [Screenshot dengan masalah]       │
│                                     │
│   Masalah:                          │
│   • 3 missing values                │
│   • 2 format tidak konsisten        │
│   • 1 duplikasi                     │
└─────────────────────────────────────┘
              ↓ CLEANING PROCESS
┌─────────────────────────────────────┐
│   AFTER: Master Produk (Clean)      │
│   [Screenshot bersih]               │
│                                     │
│   Hasil:                            │
│   ✅ 100% data complete             │
│   ✅ Format standardized            │
│   ✅ No duplicates                  │
└─────────────────────────────────────┘
```

---

## 🎨 Cara Membuat Screenshot Dashboard

### Step 1: Buka Dashboard di Looker Studio

1. Buka dashboard yang sudah dibuat
2. Mode: View mode (bukan Edit mode)
3. Pastikan data sudah ter-load semua

### Step 2: Pengaturan Tampilan

**Untuk Full Page Screenshot:**
- Zoom: 100%
- Hide browser toolbar (F11 untuk fullscreen)
- Pastikan semua chart ter-render

**Untuk Specific Chart:**
- Zoom in ke chart yang ingin di-highlight
- Crop area yang tidak perlu

### Step 3: Capture Screenshot

**Tools Recommended:**
- **Full Page**: Awesome Screenshot (Chrome Extension)
- **Specific Area**: Snipping Tool / Snagit
- **Video**: Loom / OBS Studio (untuk demo interaktif)

### Step 4: Annotate Dashboard Screenshot

Tambahkan:
- **Numbering** untuk setiap section
- **Callout** untuk fitur penting
- **Legend** untuk warna/simbol

---

## 📐 Contoh Layout Dashboard Screenshot

### Layout: Annotated Dashboard
```
┌─────────────────────────────────────────────────┐
│  EXECUTIVE DASHBOARD - SATRIAMART               │
│                                                 │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐              │
│  │  1  │ │  2  │ │  3  │ │  4  │ ← KPI Cards  │
│  └─────┘ └─────┘ └─────┘ └─────┘              │
│                                                 │
│  ┌──────────────────┐ ┌──────────────────┐    │
│  │        5         │ │        6         │    │
│  │  Revenue Trend   │ │  Sales by Cat    │    │
│  └──────────────────┘ └──────────────────┘    │
│                                                 │
│  ┌──────────────────────────────────────┐     │
│  │              7                        │     │
│  │      Top Products Table               │     │
│  └──────────────────────────────────────┘     │
└─────────────────────────────────────────────────┘

Legend:
1. Total Revenue KPI
2. Total Transactions KPI
3. Average Order Value KPI
4. Total Customers KPI
5. Revenue trend over time (line chart)
6. Sales by category (pie chart)
7. Top 10 products by revenue (table)
```

---

## ✅ Checklist Kualitas Screenshot

### Untuk Data Quality Screenshots:
- [ ] Resolusi minimal 1920x1080
- [ ] Teks jelas dan terbaca
- [ ] Masalah data ter-highlight dengan jelas
- [ ] Ada perbandingan before/after
- [ ] Include header kolom
- [ ] Tidak ada informasi sensitif (jika ada, blur)

### Untuk Dashboard Screenshots:
- [ ] Resolusi minimal 1920x1080
- [ ] Semua chart ter-render sempurna
- [ ] Warna konsisten dengan branding
- [ ] Data ter-load (tidak ada "loading...")
- [ ] Filter controls visible (jika relevan)
- [ ] Tidak ada error message
- [ ] Layout rapi dan profesional

---

## 🎯 Tips Pro untuk Screenshot

### 1. Konsistensi
- Gunakan zoom level yang sama untuk semua screenshot
- Gunakan color scheme yang konsisten
- Gunakan font yang sama untuk annotation

### 2. Clarity
- Hindari screenshot yang terlalu ramai
- Focus pada 1-2 poin utama per screenshot
- Gunakan white space dengan baik

### 3. Context
- Selalu include judul/caption
- Tambahkan keterangan singkat
- Numbering untuk sequence

### 4. Quality
- Save dalam format PNG (lossless)
- Resolusi tinggi (minimal 1920x1080)
- Compress jika file terlalu besar (gunakan TinyPNG)

---

## 📁 Struktur Penyimpanan Screenshot

```
screenshots/
├── 01_data_quality/
│   ├── before/
│   │   ├── master_produk_raw.png
│   │   ├── master_pelanggan_raw.png
│   │   └── ...
│   ├── after/
│   │   ├── master_produk_clean.png
│   │   ├── master_pelanggan_clean.png
│   │   └── ...
│   └── comparison/
│       ├── produk_before_after.png
│       └── ...
│
├── 02_dashboard/
│   ├── page1_executive.png
│   ├── page2_sales.png
│   ├── page3_product.png
│   ├── page4_customer.png
│   ├── page5_financial.png
│   ├── page6_operations.png
│   └── page7_marketing.png
│
└── 03_features/
    ├── filter_controls.png
    ├── drill_down_example.png
    └── cross_filtering.png
```

---

## 🎬 Bonus: Video Demo

Jika ingin membuat video demo dashboard:

### Tools:
- **Loom** (free, cloud-based)
- **OBS Studio** (free, powerful)
- **Camtasia** (paid, professional)

### Script Demo:
1. **Intro** (10 detik)
   - "Dashboard BI SATRIAMART"
   
2. **Overview** (20 detik)
   - Pan through all 7 pages
   
3. **Deep Dive** (60 detik)
   - Show 2-3 key insights
   - Demonstrate filters
   - Show drill-down
   
4. **Conclusion** (10 detik)
   - Summary of benefits

**Total Duration: 90-120 detik**

---

## 📞 Troubleshooting

### Screenshot Blur?
- Increase zoom level
- Use higher resolution display
- Save as PNG instead of JPG

### Colors Look Different?
- Check monitor calibration
- Use consistent color profile
- Test on multiple devices

### File Size Too Large?
- Compress with TinyPNG
- Reduce resolution (but keep readable)
- Convert to JPG (if PNG too large)

---

**Selamat membuat screenshot! 📸**

**Dibuat oleh:** Tim BI SATRIAMART  
**Tanggal:** Desember 2024  
**Versi:** 1.0
