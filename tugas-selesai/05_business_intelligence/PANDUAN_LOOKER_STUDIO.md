# 📊 Panduan Step-by-Step: Membuat Dashboard Looker Studio

## 🎯 Tujuan
Membuat dashboard Business Intelligence interaktif di **Google Looker Studio** (formerly Data Studio) berdasarkan rancangan dashboard HTML yang sudah ada.

---

## 📋 Persiapan Awal

### 💡 Apa itu BLEND di Looker Studio?

**BLEND** adalah fitur untuk menggabungkan data dari 2 atau lebih data source, mirip seperti JOIN di SQL atau VLOOKUP di Excel.

**Kapan perlu BLEND?**
- ✅ Ketika butuh data dari 2 tabel berbeda dalam 1 chart
- ✅ Contoh: Transaksi (punya revenue) + Produk (punya kategori)
- ✅ Untuk mendapatkan "Revenue per Kategori Produk"

**Konsep JOIN:**
```
Transaksi_Penjualan          Master_Produk
┌─────────────┬────────┐     ┌─────────────┬──────────┐
│ id_transaksi│id_produk│     │ id_produk   │ kategori │
├─────────────┼────────┤     ├─────────────┼──────────┤
│ TRX001      │ P001   │ ──→ │ P001        │ Nomor    │
│ TRX002      │ P016   │ ──→ │ P016        │ Signage  │
│ TRX003      │ P010   │ ──→ │ P010        │ Nomor    │
└─────────────┴────────┘     └─────────────┴──────────┘

HASIL BLEND:
┌─────────────┬────────┬──────────┬────────────┐
│ id_transaksi│id_produk│ kategori │ revenue    │
├─────────────┼────────┼──────────┼────────────┤
│ TRX001      │ P001   │ Nomor    │ 199,000    │
│ TRX002      │ P016   │ Signage  │ 200,000    │
│ TRX003      │ P010   │ Nomor    │ 201,250    │
└─────────────┴────────┴──────────┴────────────┘
```

---

### 1. Persiapan Data

#### A. Upload Data ke Google Sheets
1. **Buka Google Drive** (drive.google.com)
2. **Buat folder baru**: `SATRIAMART_BI_Data`
3. **Upload semua file CSV** ke folder tersebut:
   - `01_master_produk.csv`
   - `02_master_pelanggan.csv`
   - `03_transaksi_penjualan.csv`
   - `04_riwayat_stok.csv`
   - `05_biaya_operasional.csv`
   - `06_marketing_campaign.csv`

4. **Konversi CSV ke Google Sheets**:
   - Klik kanan pada setiap file CSV
   - Pilih **"Open with" → "Google Sheets"**
   - File akan otomatis terkonversi
   - Rename setiap sheet dengan nama yang jelas:
     - `Master_Produk`
     - `Master_Pelanggan`
     - `Transaksi_Penjualan`
     - `Riwayat_Stok`
     - `Biaya_Operasional`
     - `Marketing_Campaign`

#### B. Verifikasi Data
Pastikan setiap Google Sheet memiliki:
- ✅ Header row di baris pertama
- ✅ Tidak ada baris kosong di tengah data
- ✅ Format tanggal konsisten (YYYY-MM-DD HH:MM:SS)
- ✅ Format angka tanpa simbol mata uang (hanya angka)

---

## � PANDUAN  KHUSUS: Memahami BLEND di Looker Studio

### Mengapa Perlu BLEND?

Dalam dashboard SATRIAMART, kita punya data terpisah:
- **Transaksi_Penjualan**: Punya `total_pembayaran`, `tanggal`, `id_produk`
- **Master_Produk**: Punya `kategori`, `nama_produk`, `harga_jual`

Untuk membuat chart "Revenue per Kategori", kita butuh:
- Revenue → dari Transaksi
- Kategori → dari Produk

Solusinya: **BLEND kedua tabel dengan join key `id_produk`**

### Cara Kerja BLEND (Analogi Sederhana)

Bayangkan Anda punya 2 buku:
1. **Buku Transaksi**: Daftar penjualan dengan kode produk
2. **Buku Katalog**: Daftar produk dengan kategorinya

Untuk tahu "Berapa total penjualan kategori Signage?", Anda harus:
1. Lihat transaksi → ambil kode produk
2. Cari kode produk di katalog → dapat kategorinya
3. Jumlahkan semua transaksi dengan kategori yang sama

**BLEND melakukan ini secara otomatis!**

### 3 Jenis JOIN di Looker Studio

#### 1. Left Outer Join (Paling Umum)
```
Transaksi (LEFT)    +    Produk (RIGHT)
┌────────┬────────┐     ┌────────┬──────────┐
│ TRX001 │ P001   │ ──→ │ P001   │ Nomor    │ ✅ Match
│ TRX002 │ P999   │ ──→ │ P002   │ Signage  │ ❌ P999 tidak ada
│ TRX003 │ P002   │ ──→ │ P003   │ Papan    │ ✅ Match
└────────┴────────┘     └────────┴──────────┘

HASIL: Semua transaksi tetap muncul, meski produknya tidak ada di katalog
```
**Gunakan ini untuk**: Analisis transaksi (jangan sampai ada transaksi yang hilang)

#### 2. Inner Join
```
HASIL: Hanya transaksi yang produknya ada di katalog
```
**Gunakan ini untuk**: Analisis produk yang masih aktif

#### 3. Full Outer Join
```
HASIL: Semua data dari kedua tabel (jarang dipakai)
```

### Contoh Praktis: 3 Blend yang Akan Kita Buat

#### Blend 1: Transaksi + Produk (Untuk Category Performance)
```
LEFT: Transaksi_Penjualan
RIGHT: Master_Produk
JOIN KEY: id_produk = id_produk
JOIN TYPE: Left Outer

FIELDS YANG DIAMBIL:
✅ total_pembayaran (dari Transaksi)
✅ kategori (dari Produk)
✅ nama_produk (dari Produk)

DIGUNAKAN UNTUK:
- Revenue per kategori
- Top products
- Category analysis
```

#### Blend 2: Transaksi + Pelanggan (Untuk Customer Analytics)
```
LEFT: Transaksi_Penjualan
RIGHT: Master_Pelanggan
JOIN KEY: id_pelanggan = id_pelanggan
JOIN TYPE: Left Outer

FIELDS YANG DIAMBIL:
✅ total_pembayaran (dari Transaksi)
✅ nama_lengkap (dari Pelanggan)
✅ kota (dari Pelanggan)
✅ jenis_pelanggan (dari Pelanggan)

DIGUNAKAN UNTUK:
- Revenue per customer
- Geographic analysis
- Customer segmentation
```

#### Blend 3: Transaksi + Produk + Pelanggan (Untuk Analisis Lengkap)
```
STEP 1: Blend Transaksi + Produk
STEP 2: Blend hasil step 1 + Pelanggan

DIGUNAKAN UNTUK:
- Analisis kompleks
- Cross-analysis
- Custom reports
```

### Tips Sukses BLEND

✅ **DO:**
- Pastikan join key memiliki format yang sama (text vs text)
- Gunakan Left Outer Join untuk analisis transaksi
- Beri nama blend yang jelas (contoh: "Transaksi_with_Product")
- Test dengan filter kecil dulu (1 bulan data)

❌ **DON'T:**
- Jangan blend lebih dari 3 tabel sekaligus (lambat)
- Jangan ambil semua fields (pilih yang perlu saja)
- Jangan lupa set aggregation (SUM, COUNT, AVG)

### Alternatif Jika BLEND Terlalu Kompleks

Jika Anda kesulitan dengan BLEND di Looker Studio, ada cara lebih mudah:

#### Opsi 1: Join di Google Sheets (Recommended untuk pemula)

1. **Buat sheet baru** di Google Sheets: "Transaksi_Enriched"
2. **Copy data transaksi** ke sheet baru
3. **Tambah kolom** untuk data produk:
   ```
   =VLOOKUP(B2, Master_Produk!A:D, 3, FALSE)
   ```
   - B2 = id_produk di transaksi
   - Master_Produk!A:D = range data produk
   - 3 = kolom kategori (kolom ke-3)
   - FALSE = exact match

4. **Drag formula** ke bawah untuk semua baris
5. **Connect sheet ini** ke Looker Studio
6. **Selesai!** Tidak perlu blend lagi

#### Opsi 2: Gunakan Query di Google Sheets

1. Buat sheet baru: "Query_Results"
2. Gunakan formula QUERY untuk join:
   ```
   =QUERY({Transaksi_Penjualan!A:Z, 
           ARRAYFORMULA(VLOOKUP(Transaksi_Penjualan!C:C, 
                                Master_Produk!A:D, 
                                {2,3,4}, 
                                0))}, 
          "SELECT * WHERE Col1 IS NOT NULL")
   ```

#### Opsi 3: Pre-process di Excel/Python

Jika Anda familiar dengan Excel atau Python:
- Join data di Excel (Power Query)
- Atau gunakan Python pandas: `pd.merge()`
- Export hasil join ke CSV
- Upload ke Google Sheets
- Connect ke Looker Studio

---

## 🚀 Langkah 1: Membuat Project Looker Studio

### 1.1 Akses Looker Studio
1. Buka browser dan akses: **https://lookerstudio.google.com**
2. Login dengan akun Google yang sama dengan Google Sheets
3. Klik tombol **"Create"** → **"Report"**

### 1.2 Connect Data Source
1. Pada popup "Add data to report":
   - Pilih **"Google Sheets"**
   - Pilih spreadsheet **"Master_Produk"**
   - Klik **"Add"**
   - Klik **"Add to Report"**

2. **Tambahkan data source lainnya**:
   - Klik **"Resource" → "Manage added data sources"**
   - Klik **"Add a data source"**
   - Ulangi untuk semua sheets:
     - Master_Pelanggan
     - Transaksi_Penjualan
     - Riwayat_Stok
     - Biaya_Operasional
     - Marketing_Campaign

---

## 📊 Langkah 2: Membuat Executive Dashboard (Halaman 1)

### 2.1 Setup Halaman
1. **Rename halaman**: Klik "Page 1" → Rename menjadi **"Executive Dashboard"**
2. **Set ukuran canvas**: 
   - Klik **"File" → "Page settings"**
   - Width: **1200px**, Height: **Auto**
3. **Tambahkan background color**: 
   - Pilih canvas → Properties → Background: **#F9FAFB** (abu-abu terang)

### 2.2 Tambahkan Header
1. **Klik "Add a text"** (ikon T)
2. Ketik: **"SATRIAMART Business Intelligence Dashboard"**
3. Format:
   - Font: **Roboto Bold**
   - Size: **32**
   - Color: **#1F2937** (hitam gelap)
4. **Tambahkan subtitle**:
   - Text: "Executive Dashboard - Overview of Business Performance"
   - Font: Roboto Regular, Size: 16, Color: #6B7280

### 2.3 Buat KPI Cards (4 Cards)

#### Card 1: Total Revenue
1. **Klik "Add a chart" → Scorecard**
2. **Data source**: Transaksi_Penjualan
3. **Metric**: 
   - Klik "Add metric"
   - Pilih field: `total_pembayaran`
   - Aggregation: **SUM**
   - Rename: "Total Revenue"
4. **Style**:
   - Background color: **#22C55E** (hijau)
   - Text color: **#FFFFFF** (putih)
   - Font size: **36**
   - Compact numbers: **ON**
   - Number format: **Currency (IDR)**
5. **Posisi**: Top-left corner (x: 20, y: 100)
6. **Ukuran**: Width: 280px, Height: 140px

#### Card 2: Total Transactions
1. **Duplicate Card 1** (Ctrl+D atau Cmd+D)
2. **Metric**: 
   - Ganti dengan: `id_transaksi`
   - Aggregation: **COUNT DISTINCT**
   - Rename: "Total Transactions"
3. **Style**:
   - Background color: **#3B82F6** (biru)
   - Number format: **Number**
4. **Posisi**: Sebelah kanan Card 1 (x: 320, y: 100)

#### Card 3: Average Order Value
1. **Duplicate Card 2**
2. **Metric**: 
   - Buat calculated field baru:
   - Name: `Avg_Order_Value`
   - Formula: `SUM(total_pembayaran) / COUNT_DISTINCT(id_transaksi)`
3. **Style**:
   - Background color: **#A855F7** (ungu)
   - Number format: **Currency (IDR)**
4. **Posisi**: Sebelah kanan Card 2 (x: 620, y: 100)

#### Card 4: Total Customers
1. **Duplicate Card 3**
2. **Data source**: Ganti ke **Master_Pelanggan**
3. **Metric**: 
   - Field: `id_pelanggan`
   - Aggregation: **COUNT DISTINCT**
   - Rename: "Total Customers"
4. **Style**:
   - Background color: **#FB923C** (orange)
   - Number format: **Number**
5. **Posisi**: Sebelah kanan Card 3 (x: 920, y: 100)

### 2.4 Buat Revenue Trend Chart

1. **Klik "Add a chart" → Time series chart**
2. **Data source**: Transaksi_Penjualan
3. **Date range dimension**: `tanggal_transaksi`
4. **Metric**: `total_pembayaran` (SUM)
5. **Style**:
   - Line color: **#22C55E** (hijau)
   - Line thickness: **3**
   - Show data points: **ON**
   - Fill area: **ON** (opacity 20%)
6. **Posisi**: Di bawah KPI cards (x: 20, y: 260)
7. **Ukuran**: Width: 580px, Height: 320px

### 2.5 Buat Sales by Channel Chart

1. **Klik "Add a chart" → Donut chart**
2. **Data source**: Transaksi_Penjualan
3. **Dimension**: `channel_penjualan`
4. **Metric**: `total_pembayaran` (SUM)
5. **Style**:
   - Colors: Custom palette
     - WhatsApp: **#22C55E**
     - Instagram: **#3B82F6**
     - Offline: **#A855F7**
     - Marketplace: **#FB923C**
   - Show legend: **Bottom**
   - Show data labels: **Percentage**
6. **Posisi**: Sebelah kanan Revenue Trend (x: 620, y: 260)
7. **Ukuran**: Width: 580px, Height: 320px

### 2.6 Buat Category Performance Chart

**Catatan**: Chart ini memerlukan data dari 2 tabel (Transaksi + Produk), jadi kita perlu membuat **BLEND** terlebih dahulu.

#### Step A: Buat Blend Data Source

1. **Klik menu "Resource"** di toolbar atas
2. **Pilih "Manage added data sources"**
3. **Klik tombol "+ ADD A DATA SOURCE"** (pojok kanan bawah)
4. **Pilih "BLEND DATA"** (ikon dengan 2 tabel yang overlap)

5. **Configure Blend - Table 1 (Left)**:
   - Klik "Add data source"
   - Pilih: **Transaksi_Penjualan**
   - Join key: Pilih field **`id_produk`**
   - Metrics yang diambil:
     - ✅ `total_pembayaran` (SUM)
     - ✅ `id_transaksi` (COUNT)
     - ✅ `jumlah_item` (SUM)

6. **Configure Blend - Table 2 (Right)**:
   - Klik "Add another data source"
   - Pilih: **Master_Produk**
   - Join key: Pilih field **`id_produk`** (harus sama dengan Table 1)
   - Dimensions yang diambil:
     - ✅ `kategori`
     - ✅ `nama_produk`
     - ✅ `sub_kategori`

7. **Set Join Configuration**:
   - Join operator: **Left Outer Join** (default)
   - Ini artinya: Ambil semua transaksi, dan tambahkan info produk jika ada
   
8. **Rename Blend**:
   - Klik nama blend (biasanya "Blend 1")
   - Rename menjadi: **"Transaksi_with_Product_Info"**

9. **Klik "SAVE"** (pojok kanan atas)

10. **Klik "CLOSE"** untuk kembali ke report

#### Step B: Buat Pie Chart dengan Blend

1. **Klik "Add a chart" → Pie chart**

2. **Set Data Source**:
   - Klik dropdown "Data source" di panel kanan
   - Pilih: **"Transaksi_with_Product_Info"** (blend yang baru dibuat)

3. **Configure Chart**:
   - **Dimension**: 
     - Klik "Add dimension"
     - Pilih: **`kategori`** (ini dari Master_Produk)
     - Anda akan lihat ada prefix nama tabel di depannya
   
   - **Metric**: 
     - Klik "Add metric"
     - Pilih: **`total_pembayaran`** (dari Transaksi_Penjualan)
     - Pastikan aggregation: **SUM**

4. **Style Settings**:
   - **Pie chart type**: Pie (bukan donut)
   - **Slice colors**: 
     - Klik "Color by" → "Dimension value"
     - Klik ikon palette untuk custom colors:
       - Nomor Rumah: **#22C55E** (hijau)
       - Signage: **#3B82F6** (biru)
       - Papan Nama: **#A855F7** (ungu)
       - Aksesoris Dekorasi: **#FB923C** (orange)
   - **Legend**: 
     - Position: **Bottom**
     - Show legend: **ON**
   - **Data labels**: 
     - Show: **Percentage**
     - Font size: **12**

5. **Posisi & Ukuran**:
   - Drag chart ke posisi: Baris baru di bawah (x: 20, y: 600)
   - Resize: Width: **380px**, Height: **320px**

6. **Add Title** (optional):
   - Double-click chart title
   - Edit: "Category Performance"
   - Font: Roboto Bold, Size: 16

#### Troubleshooting Blend:

**Jika data tidak muncul:**
- ✅ Pastikan `id_produk` ada di kedua tabel
- ✅ Pastikan format `id_produk` sama (text vs text, bukan text vs number)
- ✅ Check apakah ada data yang ter-join (preview blend)

**Jika kategori tidak muncul:**
- ✅ Pastikan field `kategori` sudah di-check saat setup blend
- ✅ Refresh data source: Resource → Refresh data

**Alternatif tanpa Blend** (jika blend terlalu kompleks):
- Buat calculated field di Google Sheets
- Gunakan VLOOKUP untuk join data di Sheets
- Import hasil join sebagai data source baru

### 2.7 Buat Payment Methods Chart

1. **Klik "Add a chart" → Bar chart**
2. **Data source**: Transaksi_Penjualan
3. **Dimension**: `metode_pembayaran`
4. **Metric**: `id_transaksi` (COUNT)
5. **Style**:
   - Bar color: **#22C55E**
   - Show data labels: **ON**
   - Sort: **Descending**
6. **Posisi**: Sebelah kanan Category chart (x: 420, y: 600)
7. **Ukuran**: Width: 380px, Height: 320px

### 2.8 Buat Order Status Chart

1. **Klik "Add a chart" → Donut chart**
2. **Data source**: Transaksi_Penjualan
3. **Dimension**: `status_pesanan`
4. **Metric**: `id_transaksi` (COUNT)
5. **Style**:
   - Colors: 
     - Selesai: **#22C55E** (hijau)
     - Proses: **#FB923C** (orange)
     - Dibatalkan: **#EF4444** (merah)
     - Dikirim: **#3B82F6** (biru)
   - Show legend: **Bottom**
6. **Posisi**: Sebelah kanan Payment chart (x: 820, y: 600)
7. **Ukuran**: Width: 380px, Height: 320px

### 2.9 Buat Top 10 Products Table

**Tujuan**: Menampilkan 10 produk terlaris berdasarkan revenue dengan informasi lengkap.

#### Step 1: Pastikan Blend Sudah Ada

Jika belum membuat blend di step 2.6, buat dulu:
- Nama blend: **"Transaksi_with_Product_Info"**
- Left: Transaksi_Penjualan (join key: id_produk)
- Right: Master_Produk (join key: id_produk)

#### Step 2: Tambahkan Table Chart

1. **Klik "Add a chart"** di toolbar
2. **Pilih "Table"** (ikon tabel dengan grid)
3. **Klik di canvas** untuk menempatkan table

#### Step 3: Set Data Source

1. **Di panel kanan**, klik dropdown **"Data source"**
2. **Pilih**: **"Transaksi_with_Product_Info"** (blend yang sudah dibuat)
3. Jika blend belum ada, akan muncul error → buat blend dulu

#### Step 4: Configure Dimensions (Kolom Kategorikal)

1. **Di panel kanan**, bagian **"Dimension"**:
   
   **Dimension 1: Nama Produk**
   - Klik **"Add dimension"**
   - Scroll cari: **`nama_produk`** (dari Master_Produk)
   - Klik untuk menambahkan
   
   **Dimension 2: Kategori**
   - Klik **"Add dimension"** lagi
   - Pilih: **`kategori`** (dari Master_Produk)

2. **Urutan kolom** (drag untuk mengatur):
   - Kolom 1: `nama_produk`
   - Kolom 2: `kategori`

#### Step 5: Configure Metrics (Kolom Angka)

1. **Di panel kanan**, bagian **"Metric"**:

   **Metric 1: Revenue**
   - Klik **"Add metric"**
   - Pilih: **`total_pembayaran`**
   - Pastikan aggregation: **SUM** (default)
   - **Rename metric**:
     - Klik ikon pensil di sebelah nama metric
     - Ganti nama menjadi: **"Revenue"**
   
   **Metric 2: Units Sold**
   - Klik **"Add metric"** lagi
   - Pilih: **`jumlah_item`**
   - Aggregation: **SUM**
   - Rename: **"Units Sold"**
   
   **Metric 3: Average Price (Calculated Field)**
   - Klik **"Add metric"**
   - Klik **"CREATE FIELD"** (di bagian bawah dropdown)
   - **Field Name**: `Avg_Price`
   - **Formula**: 
     ```
     SUM(total_pembayaran) / SUM(jumlah_item)
     ```
   - **Penjelasan formula**:
     - Total revenue dibagi total unit terjual
     - Menghasilkan harga rata-rata per unit
   - Klik **"SAVE"**
   - Klik **"DONE"**
   - Rename metric menjadi: **"Avg Price"**

#### Step 6: Set Sorting & Limit

1. **Sort (Pengurutan)**:
   - Di panel kanan, bagian **"Sort"**
   - Klik dropdown, pilih: **"Revenue"**
   - Order: **Descending** (dari besar ke kecil)
   - Ini akan menampilkan produk dengan revenue tertinggi di atas

2. **Limit Rows**:
   - Scroll ke bawah di panel kanan
   - Cari: **"Rows per page"**
   - Set value: **10**
   - Ini membatasi hanya 10 produk teratas

#### Step 7: Styling Table

1. **Klik tab "STYLE"** di panel kanan

2. **Table Header**:
   - **Header background color**: 
     - Klik color picker
     - Input: **#F3F4F6** (abu-abu terang)
   - **Header text**:
     - Font: **Roboto**
     - Weight: **Bold**
     - Size: **12**
     - Color: **#1F2937** (hitam gelap)

3. **Table Body**:
   - **Alternating row colors**: Toggle **ON**
     - Row color 1: **#FFFFFF** (putih)
     - Row color 2: **#F9FAFB** (abu-abu sangat terang)
   - **Text**:
     - Font: **Roboto**
     - Weight: **Regular**
     - Size: **11**
     - Color: **#374151** (abu-abu gelap)

4. **Row Numbers**:
   - **Show row numbers**: Toggle **ON**
   - Ini akan menampilkan ranking 1-10 di kolom pertama

5. **Borders**:
   - **Table border**: Toggle **ON**
   - **Cell borders**: Toggle **ON**
   - Border color: **#E5E7EB** (abu-abu)

6. **Number Formatting**:
   - Klik metric **"Revenue"**
   - Format: **Currency**
   - Currency: **IDR (Indonesian Rupiah)**
   - Decimal places: **0**
   - Compact numbers: **OFF** (tampilkan full)
   
   - Klik metric **"Units Sold"**
   - Format: **Number**
   - Decimal places: **0**
   
   - Klik metric **"Avg Price"**
   - Format: **Currency**
   - Currency: **IDR**
   - Decimal places: **0**

#### Step 8: Posisi & Ukuran

1. **Drag table** ke posisi di bawah semua charts
   - Position X: **20px** (dari kiri)
   - Position Y: **940px** (dari atas)

2. **Resize table**:
   - Width: **1160px** (hampir full width)
   - Height: **400px** (cukup untuk 10 rows + header)

3. **Tips positioning**:
   - Gunakan grid lines (View → Show grid)
   - Align dengan charts di atasnya
   - Pastikan ada spacing 20px dari chart terakhir

#### Step 9: Add Table Title (Optional)

1. **Klik "Add text"** (ikon T)
2. **Ketik**: "Top 10 Products by Revenue"
3. **Format**:
   - Font: **Roboto Bold**
   - Size: **18**
   - Color: **#1F2937**
4. **Posisi**: Di atas table (y: 910)

#### Troubleshooting Table:

**Jika data tidak muncul:**
- ✅ Check blend connection
- ✅ Pastikan ada data di date range yang dipilih
- ✅ Refresh data: Resource → Refresh data

**Jika calculated field error:**
- ✅ Pastikan formula tidak ada typo
- ✅ Gunakan SUM() untuk aggregation
- ✅ Test dengan formula sederhana dulu

**Jika sorting tidak bekerja:**
- ✅ Pastikan sort by metric (bukan dimension)
- ✅ Check aggregation type (harus SUM)

---

### 2.10 Tambahkan Date Range Control

**Tujuan**: Memberikan filter tanggal interaktif untuk semua charts di halaman.

#### Step 1: Tambahkan Control

1. **Klik "Add a control"** di toolbar
2. **Pilih "Date range control"** (ikon kalender)
3. **Klik di canvas** untuk menempatkan control (top-right corner)

#### Step 2: Configure Control

1. **Di panel kanan**, tab **"SETUP"**:

   **Control Field**:
   - **Data source**: Pilih **"Transaksi_Penjualan"**
   - **Date range dimension**: Pilih **`tanggal_transaksi`**
   - Ini akan filter semua charts yang menggunakan field ini

   **Default Date Range**:
   - Klik dropdown **"Auto date range"**
   - Pilih: **"Last 12 months"**
   - Atau pilih **"Custom"** untuk set manual:
     - Start: 2024-11-01
     - End: 2025-10-31

   **Comparison Date Range** (Optional):
   - Toggle **OFF** (tidak perlu untuk sekarang)
   - Bisa diaktifkan nanti untuk compare periods

#### Step 3: Style Control

1. **Klik tab "STYLE"** di panel kanan:

   **Control Type**:
   - Pilih: **"Compact"** (lebih kecil, hemat space)
   - Alternatif: "Advanced" (lebih banyak opsi)

   **Colors**:
   - **Background**: **#FFFFFF** (putih)
   - **Border**: **#D1D5DB** (abu-abu)
   - **Text**: **#374151** (abu-abu gelap)
   - **Accent color**: **#22C55E** (hijau, sesuai brand)

   **Font**:
   - Font family: **Roboto**
   - Font size: **12**

   **Border**:
   - Border radius: **8px** (rounded corners)
   - Border width: **1px**

#### Step 4: Posisi & Ukuran

1. **Drag control** ke pojok kanan atas:
   - Position X: **1000px** (dari kiri)
   - Position Y: **20px** (dari atas)
   - Sejajar dengan header dashboard

2. **Resize control**:
   - Width: **180px** (compact)
   - Height: **40px** (single line)

3. **Alignment**:
   - Pastikan sejajar dengan header text
   - Beri spacing 20px dari edge kanan canvas

#### Step 5: Test Control

1. **Klik "View"** untuk preview mode
2. **Klik date range control**
3. **Pilih date range berbeda**:
   - Last 30 days
   - Last 3 months
   - Custom range
4. **Observe**: Semua charts harus update otomatis
5. **Klik "Edit"** untuk kembali ke edit mode

#### Step 6: Add Label (Optional)

1. **Klik "Add text"** di atas control
2. **Ketik**: "Filter Periode:"
3. **Format**:
   - Font: **Roboto Medium**
   - Size: **12**
   - Color: **#6B7280** (abu-abu)
4. **Posisi**: Di atas control (y: 5)

#### Advanced: Multiple Controls

Jika ingin tambah filter lain:

**Filter Channel**:
1. **Add control → Drop-down list**
2. **Control field**: `channel_penjualan`
3. **Position**: Di bawah date range (y: 70)

**Filter Category**:
1. **Add control → Drop-down list**
2. **Control field**: `kategori` (dari blend)
3. **Position**: Di bawah channel filter (y: 120)

**Filter Status**:
1. **Add control → Drop-down list**
2. **Control field**: `status_pesanan`
3. **Position**: Di bawah category filter (y: 170)

#### Tips Control:

✅ **Best Practices**:
- Letakkan controls di area yang konsisten (top-right atau left sidebar)
- Gunakan "Compact" style untuk hemat space
- Set default range yang masuk akal (12 months)
- Test filter dengan berbagai date ranges

❌ **Avoid**:
- Terlalu banyak controls (max 3-4 per page)
- Controls yang overlap dengan charts
- Default range terlalu kecil (< 1 month)

#### Troubleshooting Control:

**Jika filter tidak bekerja:**
- ✅ Pastikan control field sama dengan dimension di charts
- ✅ Check data source connection
- ✅ Pastikan charts menggunakan field yang sama

**Jika date range tidak muncul:**
- ✅ Pastikan field type adalah DATE atau DATETIME
- ✅ Check format tanggal di Google Sheets
- ✅ Refresh data source

**Jika control terlalu besar:**
- ✅ Gunakan "Compact" style
- ✅ Reduce font size
- ✅ Adjust width manually

---

### 📸 Visual Guide: Layout Executive Dashboard

Berikut gambaran layout lengkap halaman Executive Dashboard:

```
┌─────────────────────────────────────────────────────────────────────┐
│  📊 SATRIAMART BI Dashboard              [Filter: Last 12 months ▼] │ ← Header + Date Control
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │ Total    │  │ Total    │  │ Avg Order│  │ Total    │           │ ← KPI Cards
│  │ Revenue  │  │ Trans.   │  │ Value    │  │ Customers│           │
│  │ Rp 150M  │  │   320    │  │ Rp 468K  │  │   180    │           │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │
│                                                                       │
│  ┌─────────────────────────┐  ┌─────────────────────────┐          │
│  │ Revenue Trend           │  │ Sales by Channel        │          │ ← Charts Row 1
│  │ [Line Chart]            │  │ [Donut Chart]           │          │
│  │                         │  │                         │          │
│  └─────────────────────────┘  └─────────────────────────┘          │
│                                                                       │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                   │
│  │ Category   │  │ Payment    │  │ Order      │                   │ ← Charts Row 2
│  │ Performance│  │ Methods    │  │ Status     │                   │
│  │ [Pie Chart]│  │ [Bar Chart]│  │ [Donut]    │                   │
│  └────────────┘  └────────────┘  └────────────┘                   │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ Top 10 Products by Revenue                                  │   │ ← Table
│  ├────┬──────────────────┬──────────┬──────────┬──────────────┤   │
│  │ #  │ Product Name     │ Category │ Revenue  │ Units │ Avg  │   │
│  ├────┼──────────────────┼──────────┼──────────┼───────┼──────┤   │
│  │ 1  │ Signage LED...   │ Signage  │ Rp 8.5M  │  45   │ 189K │   │
│  │ 2  │ Papan Nama...    │ Papan    │ Rp 7.2M  │  38   │ 189K │   │
│  │ 3  │ Nomor Rumah...   │ Nomor    │ Rp 6.8M  │  52   │ 131K │   │
│  │... │ ...              │ ...      │ ...      │ ...   │ ...  │   │
│  └────┴──────────────────┴──────────┴──────────┴───────┴──────┘   │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

### 🎯 Checklist: Executive Dashboard Selesai

Setelah menyelesaikan Langkah 2, pastikan Anda punya:

- [ ] **Header & Title** dengan branding SATRIAMART
- [ ] **Date Range Control** di top-right (working)
- [ ] **4 KPI Cards** dengan warna berbeda:
  - [ ] Total Revenue (hijau)
  - [ ] Total Transactions (biru)
  - [ ] Avg Order Value (ungu)
  - [ ] Total Customers (orange)
- [ ] **Revenue Trend Chart** (line chart, 12 months)
- [ ] **Sales by Channel Chart** (donut chart)
- [ ] **Category Performance Chart** (pie chart, using blend)
- [ ] **Payment Methods Chart** (bar chart)
- [ ] **Order Status Chart** (donut chart)
- [ ] **Top 10 Products Table** (with ranking, sorted by revenue)
- [ ] **All charts update** when date range changes
- [ ] **Consistent styling** (colors, fonts, spacing)

### 💡 Tips Sebelum Lanjut ke Halaman Berikutnya

1. **Save your work**: Ctrl+S atau File → Save
2. **Test semua filters**: Pastikan date range control bekerja
3. **Preview mode**: Klik "View" untuk lihat hasil akhir
4. **Check mobile view**: View → Mobile layout
5. **Duplicate page**: Untuk template halaman berikutnya
   - Right-click page → Duplicate
   - Rename → "Sales Analysis"
   - Hapus charts yang tidak perlu
   - Ganti dengan charts baru

---

## 📈 Langkah 3: Membuat Sales Analysis Dashboard (Halaman 2)

### 3.1 Tambah Halaman Baru
1. Klik **"Page" → "New page"**
2. Rename: **"Sales Analysis"**
3. Copy header dari halaman 1 (Ctrl+C, Ctrl+V)

### 3.2 Sales Overview KPIs (4 Cards)

#### Card 1: Gross Sales
- **Metric**: `SUM(subtotal)`
- **Background**: #22C55E

#### Card 2: Net Sales
- **Metric**: `SUM(total_pembayaran)`
- **Background**: #3B82F6

#### Card 3: Total Discounts
- **Metric**: `SUM(diskon_nominal)`
- **Background**: #EF4444

#### Card 4: Shipping Revenue
- **Metric**: `SUM(biaya_ongkir)`
- **Background**: #FB923C

### 3.3 Channel Performance Table

1. **Add chart → Table with heatmap**
2. **Dimension**: `channel_penjualan`
3. **Metrics**:
   - `COUNT(id_transaksi)` → "Transactions"
   - `SUM(total_pembayaran)` → "Revenue"
   - `AVG(total_pembayaran)` → "Avg Order Value"
   - Calculated: `SUM(total_pembayaran) / COUNT(id_transaksi)` → "AOV"
4. **Style**: Heatmap on Revenue column

### 3.4 Sales by Day of Week

1. **Add chart → Column chart**
2. **Dimension**: Calculated field
   - Name: `Day_of_Week`
   - Formula: `DAYNAME(tanggal_transaksi)`
3. **Metric**: `SUM(total_pembayaran)`
4. **Sort**: Custom (Mon, Tue, Wed, Thu, Fri, Sat, Sun)

### 3.5 Monthly Sales Comparison

1. **Add chart → Combo chart**
2. **Dimension**: `MONTH(tanggal_transaksi)`
3. **Metrics**:
   - `SUM(total_pembayaran)` → Bar chart
   - `COUNT(id_transaksi)` → Line chart (right axis)

### 3.6 Transaction Status Breakdown

1. **Add chart → Stacked bar chart**
2. **Dimension**: `status_pembayaran`
3. **Breakdown dimension**: `status_pesanan`
4. **Metric**: `COUNT(id_transaksi)`

### 3.7 Recent Transactions Table

1. **Add chart → Table**
2. **Dimensions**:
   - `tanggal_transaksi`
   - `id_transaksi`
   - `id_pelanggan`
   - `channel_penjualan`
   - `status_pesanan`
3. **Metric**: `total_pembayaran`
4. **Sort**: Date (Descending)
5. **Rows**: 20

---

## 🛍️ Langkah 4: Membuat Product Performance Dashboard (Halaman 3)

### 4.1 Product Overview KPIs

#### Card 1: Total Products
- **Data source**: Master_Produk
- **Metric**: `COUNT_DISTINCT(id_produk)`

#### Card 2: Inventory Value
- **Calculated field**: `SUM(harga_modal * stok_tersedia)`

#### Card 3: Avg Profit Margin
- **Calculated field**: `AVG((harga_jual - harga_modal) / harga_jual * 100)`
- **Format**: Percentage

#### Card 4: Low Stock Items
- **Metric**: `COUNT(id_produk)` WHERE `stok_tersedia < 10`

### 4.2 Category Analysis Table

1. **Table with bars**
2. **Dimension**: `kategori`
3. **Metrics**:
   - Revenue (from blended data)
   - Product count
   - Avg price
   - Avg profit margin

### 4.3 Top 10 Best Sellers

1. **Bar chart (horizontal)**
2. **Blend**: Transaksi + Produk
3. **Dimension**: `nama_produk`
4. **Metric**: `SUM(jumlah_item)`
5. **Sort**: Descending
6. **Limit**: 10

### 4.4 Bottom 10 Slow Movers

1. **Bar chart (horizontal)**
2. **Same as above but sort Ascending**

### 4.5 Price Range Distribution

1. **Histogram**
2. **Dimension**: `harga_jual`
3. **Bucket size**: 100000
4. **Metric**: `COUNT(id_produk)`

### 4.6 Stock Level Pie Chart

1. **Pie chart**
2. **Dimension**: Calculated field
   - Name: `Stock_Level`
   - Formula: 
     ```
     CASE
       WHEN stok_tersedia < 5 THEN 'Critical'
       WHEN stok_tersedia < 10 THEN 'Low'
       WHEN stok_tersedia < 20 THEN 'Medium'
       ELSE 'Healthy'
     END
     ```
3. **Metric**: `COUNT(id_produk)`

### 4.7 Product Catalog Table

1. **Table with search**
2. **All product fields**
3. **Add filter control** for kategori

---

## 👥 Langkah 5: Membuat Customer Analytics Dashboard (Halaman 4)

### 5.1 Customer Overview KPIs

#### Card 1: Total Customers
- **Metric**: `COUNT_DISTINCT(id_pelanggan)`

#### Card 2: Avg Customer Value
- **Calculated**: `SUM(total_nilai_pembelian) / COUNT_DISTINCT(id_pelanggan)`

#### Card 3: Repeat Rate
- **Calculated**: `COUNT(id_pelanggan WHERE total_transaksi > 1) / COUNT(id_pelanggan) * 100`

#### Card 4: Avg Rating
- **Blend with Transaksi**
- **Metric**: `AVG(rating_pelanggan)`

### 5.2 RFM Segmentation

1. **Pie chart**
2. **Dimension**: `segmen`
3. **Metric**: `COUNT(id_pelanggan)`
4. **Colors**: Custom per segment

### 5.3 Geographic Distribution

1. **Geo chart (Indonesia map)**
2. **Dimension**: `provinsi`
3. **Metric**: `SUM(total_nilai_pembelian)`
4. **Or use Table** if geo chart not working:
   - Dimension: `kota`
   - Metrics: Customer count, Total revenue

### 5.4 Customer Type Distribution

1. **Donut chart**
2. **Dimension**: `jenis_pelanggan`
3. **Metric**: `COUNT(id_pelanggan)`

### 5.5 Source Channel Distribution

1. **Bar chart**
2. **Dimension**: `sumber_awal`
3. **Metric**: `COUNT(id_pelanggan)`
4. **Sort**: Descending

### 5.6 Top 20 Customers Table

1. **Table**
2. **Dimensions**: `nama_lengkap`, `kota`, `jenis_pelanggan`
3. **Metrics**: 
   - `total_transaksi`
   - `total_nilai_pembelian`
4. **Sort**: Total value (Descending)
5. **Limit**: 20

### 5.7 Customer Database Table

1. **Full table with all customer fields**
2. **Add search control**
3. **Add filter controls**:
   - Kota
   - Jenis pelanggan
   - Status

---

## 💰 Langkah 6: Membuat Financial Dashboard (Halaman 5)

### 6.1 Financial Overview KPIs

#### Card 1: Total Revenue
- **Metric**: `SUM(total_pembayaran)`

#### Card 2: Total Costs
- **Blend Transaksi + Produk**
- **Calculated**: `SUM(harga_modal * jumlah_item) + SUM(biaya_operasional.nominal)`

#### Card 3: Gross Profit
- **Calculated**: Revenue - COGS

#### Card 4: Net Profit
- **Calculated**: Gross Profit - Operating Costs

### 6.2 Revenue vs Profit Trend

1. **Combo chart**
2. **Dimension**: `MONTH(tanggal_transaksi)`
3. **Metrics**:
   - Revenue (Bar)
   - Costs (Bar)
   - Profit (Line, right axis)

### 6.3 Profit Margin Trend

1. **Line chart**
2. **Dimension**: `MONTH(tanggal_transaksi)`
3. **Metric**: Calculated
   - Formula: `(Revenue - Costs) / Revenue * 100`
4. **Format**: Percentage

### 6.4 Operational Costs Breakdown

1. **Pie chart**
2. **Data source**: Biaya_Operasional
3. **Dimension**: `kategori_biaya`
4. **Metric**: `SUM(nominal)`

### 6.5 Revenue Composition

1. **Stacked bar chart**
2. **Dimension**: `MONTH(tanggal_transaksi)`
3. **Breakdown**: Revenue type
   - Product sales: `SUM(subtotal)`
   - Shipping: `SUM(biaya_ongkir)`
   - Custom services: `SUM(biaya_custom)`

### 6.6 Expense Details Table

1. **Table**
2. **Data source**: Biaya_Operasional
3. **Dimensions**: 
   - `tanggal`
   - `kategori_biaya`
   - `deskripsi`
4. **Metric**: `nominal`
5. **Add filter**: Month, Category

---

## 📦 Langkah 7: Membuat Operations & Inventory Dashboard (Halaman 6)

### 7.1 Tambah Halaman Baru
1. Klik **"Page" → "New page"**
2. Rename: **"Operations & Inventory"**
3. Copy header dari halaman 1

### 7.2 Operations Overview KPIs (4 Cards)

#### Card 1: Total Stock In
- **Data source**: Riwayat_Stok
- **Metric**: `SUM(jumlah)` WHERE `jenis_perubahan = 'Masuk'`
- **Calculated field**:
  ```
  SUM(CASE WHEN jenis_perubahan = 'Masuk' THEN jumlah ELSE 0 END)
  ```
- **Background**: #22C55E (hijau)
- **Label**: "Units received"

#### Card 2: Total Stock Out
- **Calculated field**:
  ```
  SUM(CASE WHEN jenis_perubahan = 'Keluar' THEN jumlah ELSE 0 END)
  ```
- **Background**: #3B82F6 (biru)
- **Label**: "Units sold/used"

#### Card 3: Stock Turnover Rate
- **Calculated field**:
  ```
  SUM(CASE WHEN jenis_perubahan = 'Keluar' THEN jumlah ELSE 0 END) / 
  AVG(stok_setelah)
  ```
- **Format**: Number (2 decimals)
- **Background**: #A855F7 (ungu)
- **Label**: "Times per period"

#### Card 4: Stock Adjustments
- **Calculated field**:
  ```
  SUM(CASE WHEN jenis_perubahan = 'Penyesuaian' THEN jumlah ELSE 0 END)
  ```
- **Background**: #FB923C (orange)
- **Label**: "Corrections made"

### 7.3 Stock Movement Trend Chart

1. **Add chart → Time series chart**
2. **Data source**: Riwayat_Stok
3. **Date dimension**: `tanggal_perubahan`
4. **Metrics** (multiple lines):
   - Stock In: `SUM(jumlah)` WHERE `jenis_perubahan = 'Masuk'`
   - Stock Out: `SUM(jumlah)` WHERE `jenis_perubahan = 'Keluar'`
5. **Style**:
   - Stock In line: Green (#22C55E)
   - Stock Out line: Red (#EF4444)
   - Show data points: ON
   - Fill area: ON (opacity 20%)

### 7.4 Movement by Type Chart

1. **Add chart → Donut chart**
2. **Data source**: Riwayat_Stok
3. **Dimension**: `jenis_perubahan`
4. **Metric**: `SUM(jumlah)`
5. **Style**:
   - Colors:
     - Masuk: #22C55E (hijau)
     - Keluar: #EF4444 (merah)
     - Penyesuaian: #FB923C (orange)
     - Retur: #3B82F6 (biru)

### 7.5 Stock Level by Category

1. **Add chart → Bar chart (horizontal)**
2. **Data source**: Blend Riwayat_Stok + Master_Produk
3. **Dimension**: `kategori` (from Master_Produk)
4. **Metric**: `AVG(stok_setelah)`
5. **Sort**: Descending

### 7.6 Low Stock Alert Table

1. **Add chart → Table**
2. **Data source**: Master_Produk
3. **Filter**: `stok_tersedia < 10`
4. **Dimensions**:
   - `nama_produk`
   - `kategori`
   - `stok_tersedia`
5. **Metrics**:
   - Calculated: `harga_modal * stok_tersedia` → "Stock Value"
6. **Style**:
   - Conditional formatting: Red background if stock < 5
   - Sort by: `stok_tersedia` (Ascending)

### 7.7 Stock Movement History Table

1. **Add chart → Table**
2. **Data source**: Blend Riwayat_Stok + Master_Produk
3. **Dimensions**:
   - `tanggal_perubahan`
   - `nama_produk`
   - `jenis_perubahan`
   - `keterangan`
4. **Metrics**:
   - `jumlah`
   - `stok_sebelum`
   - `stok_setelah`
5. **Sort**: Date (Descending)
6. **Rows**: 50

### 7.8 Warehouse Efficiency Metrics

1. **Add chart → Scorecard group**
2. **Metrics**:
   - **Average Days to Sell**: 
     ```
     AVG(stok_tersedia / (SUM(jumlah_keluar) / 30))
     ```
   - **Stock Accuracy Rate**:
     ```
     (COUNT(id_stok) - COUNT(CASE WHEN jenis_perubahan = 'Penyesuaian' THEN 1 END)) / 
     COUNT(id_stok) * 100
     ```
   - **Fulfillment Rate**:
     ```
     COUNT(CASE WHEN status = 'Selesai' THEN 1 END) / 
     COUNT(id_transaksi) * 100
     ```

---

## 📢 Langkah 8: Membuat Marketing Performance Dashboard (Halaman 7)

### 8.1 Tambah Halaman Baru
1. Klik **"Page" → "New page"**
2. Rename: **"Marketing Performance"**
3. Copy header dari halaman 1

### 8.2 Marketing Overview KPIs (4 Cards)

#### Card 1: Total Campaigns
- **Data source**: Marketing_Campaign
- **Metric**: `COUNT_DISTINCT(id_campaign)`
- **Background**: #22C55E (hijau)
- **Secondary metric**: 
  ```
  COUNT_DISTINCT(CASE WHEN status_campaign = 'Aktif' THEN id_campaign END)
  ```
  Label: "active campaigns"

#### Card 2: Total Marketing Spend
- **Metric**: `SUM(budget_campaign)`
- **Format**: Currency (IDR)
- **Background**: #3B82F6 (biru)

#### Card 3: Average ROI
- **Calculated field**:
  ```
  (SUM(revenue_generated) - SUM(budget_campaign)) / SUM(budget_campaign) * 100
  ```
- **Format**: Percentage
- **Background**: #A855F7 (ungu)
- **Conditional formatting**: 
  - Green if > 100%
  - Orange if 50-100%
  - Red if < 50%

#### Card 4: Total Impressions
- **Metric**: `SUM(impressions)`
- **Format**: Number (compact)
- **Background**: #FB923C (orange)

### 8.3 Campaign ROI Comparison Chart

1. **Add chart → Bar chart (horizontal)**
2. **Data source**: Marketing_Campaign
3. **Dimension**: `nama_campaign`
4. **Metric**: Calculated ROI
   ```
   (revenue_generated - budget_campaign) / budget_campaign * 100
   ```
5. **Sort**: Descending (best ROI first)
6. **Limit**: Top 10 campaigns
7. **Style**:
   - Bar color: Gradient based on value
   - Show data labels: ON
   - Format: Percentage

### 8.4 Spend by Channel Chart

1. **Add chart → Pie chart**
2. **Data source**: Marketing_Campaign
3. **Dimension**: `channel_marketing`
4. **Metric**: `SUM(budget_campaign)`
5. **Style**:
   - Colors: Custom per channel
     - Instagram: #E4405F
     - Facebook: #1877F2
     - Google Ads: #4285F4
     - TikTok: #000000
     - WhatsApp: #25D366
   - Show legend: Bottom
   - Show percentage: ON

### 8.5 Campaign Performance Over Time

1. **Add chart → Time series chart**
2. **Data source**: Marketing_Campaign
3. **Date dimension**: `tanggal_mulai`
4. **Metrics** (multiple lines):
   - Budget: `SUM(budget_campaign)`
   - Revenue: `SUM(revenue_generated)`
   - Profit: `SUM(revenue_generated - budget_campaign)`
5. **Style**:
   - Budget line: Orange
   - Revenue line: Green
   - Profit line: Blue
   - Show data points: ON

### 8.6 Channel Performance Table

1. **Add chart → Table with heatmap**
2. **Data source**: Marketing_Campaign
3. **Dimension**: `channel_marketing`
4. **Metrics**:
   - `COUNT(id_campaign)` → "Campaigns"
   - `SUM(budget_campaign)` → "Spend"
   - `SUM(impressions)` → "Impressions"
   - `SUM(clicks)` → "Clicks"
   - Calculated: `clicks / impressions * 100` → "CTR %"
   - `SUM(conversions)` → "Conversions"
   - Calculated: `conversions / clicks * 100` → "CVR %"
   - `SUM(revenue_generated)` → "Revenue"
   - Calculated ROI → "ROI %"
5. **Style**:
   - Heatmap on ROI column
   - Sort by: ROI (Descending)

### 8.7 Top Performing Campaigns Table

1. **Add chart → Table**
2. **Data source**: Marketing_Campaign
3. **Dimensions**:
   - `nama_campaign`
   - `channel_marketing`
   - `tanggal_mulai`
   - `tanggal_selesai`
   - `status_campaign`
4. **Metrics**:
   - `budget_campaign`
   - `revenue_generated`
   - Calculated ROI
   - `impressions`
   - `clicks`
   - `conversions`
5. **Sort**: ROI (Descending)
6. **Limit**: 20 campaigns

### 8.8 Customer Acquisition Cost (CAC)

1. **Add chart → Scorecard**
2. **Calculated field**:
   ```
   SUM(budget_campaign) / SUM(conversions)
   ```
3. **Format**: Currency (IDR)
4. **Label**: "Cost per Acquisition"

### 8.9 Marketing Funnel Chart

1. **Add chart → Funnel chart** (if available) or **Stacked bar**
2. **Data source**: Marketing_Campaign
3. **Stages**:
   - Impressions: `SUM(impressions)`
   - Clicks: `SUM(clicks)`
   - Conversions: `SUM(conversions)`
4. **Style**:
   - Show conversion rates between stages
   - Color gradient: Top (light) to bottom (dark)

### 8.10 Campaign Status Distribution

1. **Add chart → Donut chart**
2. **Dimension**: `status_campaign`
3. **Metric**: `COUNT(id_campaign)`
4. **Style**:
   - Colors:
     - Aktif: #22C55E (hijau)
     - Selesai: #3B82F6 (biru)
     - Dijadwalkan: #FB923C (orange)
     - Dibatalkan: #EF4444 (merah)

### 8.11 Add Filter Controls

1. **Date range control**: `tanggal_mulai`
2. **Channel filter**: Drop-down for `channel_marketing`
3. **Status filter**: Drop-down for `status_campaign`

---

## 🎨 Langkah 9: Styling & Branding

### 9.1 Theme Setup
1. **Klik "Theme and layout"**
2. **Choose theme**: Minimal atau Custom
3. **Primary color**: #22C55E (hijau SATRIAMART)
4. **Secondary color**: #3B82F6 (biru)
5. **Font**: Roboto

### 9.2 Consistent Styling
- **All KPI cards**: Same height (140px)
- **All charts**: Consistent padding (20px)
- **Color palette**: Stick to 4-5 colors
- **Font sizes**: 
  - Headers: 24-32px
  - Subheaders: 16-18px
  - Body: 12-14px

### 9.3 Add Logo
1. **Upload logo** (if available)
2. **Position**: Top-left corner
3. **Size**: 40x40px

---

## 🔧 Langkah 10: Interactivity & Filters

### 10.1 Add Global Filters
1. **Date range control** (all pages)
2. **Channel filter** (Sales, Executive)
3. **Category filter** (Products)
4. **City filter** (Customers)

### 10.2 Enable Cross-Filtering
1. **Select any chart**
2. **Properties → Interactions**
3. **Enable "Apply filter"**
4. **Test**: Click on chart element → other charts update

### 10.3 Add Navigation Menu
1. **Add text boxes** for each page name
2. **Add hyperlinks**:
   - Right-click text → "Add link"
   - Link type: "Page in this report"
   - Select target page
3. **Style**: Highlight current page

---

## 📱 Langkah 11: Mobile Optimization

### 11.1 Enable Mobile View
1. **Klik "View" → "Mobile layout"**
2. **Adjust layout** for mobile:
   - Stack KPI cards vertically
   - Reduce chart sizes
   - Hide less important elements

### 11.2 Test Responsiveness
1. **Preview** in different screen sizes
2. **Adjust** as needed

---

## 🚀 Langkah 12: Publish & Share

### 12.1 Final Review
- ✅ Check all data connections
- ✅ Verify calculations
- ✅ Test all filters
- ✅ Check spelling
- ✅ Test on different browsers

### 12.2 Publish Dashboard
1. **Klik "Share"**
2. **Set permissions**:
   - **View**: Anyone with link
   - **Edit**: Specific people
3. **Copy link**

### 12.3 Schedule Email Reports (Optional)
1. **Klik "Schedule email delivery"**
2. **Set frequency**: Daily/Weekly/Monthly
3. **Add recipients**
4. **Choose format**: PDF or Link

### 12.4 Embed in Website (Optional)
1. **Klik "File" → "Embed report"**
2. **Copy embed code**
3. **Paste** in your website HTML

---

## 📊 Calculated Fields Reference

### Revenue Metrics
```
// Gross Sales
SUM(subtotal)

// Net Sales
SUM(total_pembayaran)

// Total Discounts
SUM(diskon_nominal)

// Average Order Value
SUM(total_pembayaran) / COUNT_DISTINCT(id_transaksi)
```

### Profit Metrics
```
// Gross Profit
SUM(total_pembayaran) - SUM(harga_modal * jumlah_item)

// Profit Margin
(SUM(harga_jual) - SUM(harga_modal)) / SUM(harga_jual) * 100

// Net Profit
Gross_Profit - SUM(biaya_operasional.nominal)
```

### Customer Metrics
```
// Customer Lifetime Value
SUM(total_nilai_pembelian) / COUNT_DISTINCT(id_pelanggan)

// Repeat Customer Rate
COUNT(id_pelanggan WHERE total_transaksi > 1) / COUNT(id_pelanggan) * 100

// Average Rating
AVG(rating_pelanggan)
```

### Product Metrics
```
// Inventory Value
SUM(harga_modal * stok_tersedia)

// Stock Level Category
CASE
  WHEN stok_tersedia < 5 THEN 'Critical'
  WHEN stok_tersedia < 10 THEN 'Low'
  WHEN stok_tersedia < 20 THEN 'Medium'
  ELSE 'Healthy'
END

// Profit per Product
(harga_jual - harga_modal) * jumlah_terjual
```

### Time-based Metrics
```
// Day of Week
DAYNAME(tanggal_transaksi)

// Month Name
MONTHNAME(tanggal_transaksi)

// Quarter
QUARTER(tanggal_transaksi)

// Year-Month
CONCAT(YEAR(tanggal_transaksi), '-', MONTH(tanggal_transaksi))
```

---

## ❓ FAQ: Pertanyaan Umum

### Tentang Table

**Q: Bagaimana cara menambah kolom ranking/nomor urut di table?**
A: Di tab STYLE → Table → Show row numbers: Toggle ON

**Q: Calculated field di table tidak bisa dibuat, kenapa?**
A: Pastikan Anda klik "CREATE FIELD" bukan "Add metric". Calculated field harus dibuat dulu sebelum bisa digunakan.

**Q: Bagaimana cara membuat kolom dengan warna berbeda (heatmap)?**
A: 
1. Pilih table
2. Tab STYLE → Table colors
3. Enable "Conditional formatting"
4. Set rules berdasarkan nilai metric

**Q: Table saya terlalu panjang, bagaimana cara membatasi?**
A: 
- Set "Rows per page" di tab SETUP
- Atau tambahkan filter untuk limit data
- Atau gunakan "Show pagination" untuk multiple pages

**Q: Bagaimana cara export table ke Excel?**
A: 
1. View mode → Klik table
2. Klik ikon "..." (more options)
3. Pilih "Export" → "Download as CSV"

### Tentang Date Range Control

**Q: Date range control tidak memfilter charts, kenapa?**
A: Pastikan:
- Control field menggunakan field yang sama dengan charts
- Charts menggunakan dimension tanggal yang sama
- Data source connected dengan benar

**Q: Bagaimana cara set default date range custom?**
A: 
1. Pilih control
2. Tab SETUP → Auto date range
3. Pilih "Custom"
4. Set Start date dan End date manual

**Q: Bisa tidak membuat multiple date range controls?**
A: Bisa, tapi tidak recommended. Gunakan 1 date range control untuk semua charts di 1 page.

**Q: Bagaimana cara membuat comparison date range?**
A: 
1. Pilih control
2. Tab SETUP → Comparison date range: Toggle ON
3. Pilih comparison type (Previous period, Previous year, etc.)

### Tentang Blend

**Q: Blend saya error "No matching data", kenapa?**
A: 
- Check apakah join key memiliki nilai yang sama di kedua tabel
- Pastikan format data sama (text vs text, bukan text vs number)
- Coba gunakan Inner Join untuk test

**Q: Blend terlalu lambat, bagaimana cara mempercepat?**
A: 
- Limit fields yang diambil (jangan ambil semua)
- Filter data di source (jangan blend semua data)
- Gunakan extract data untuk cache
- Pertimbangkan pre-join di Google Sheets

**Q: Bisa blend lebih dari 2 tabel?**
A: Bisa, tapi:
- Blend hasil blend pertama dengan tabel ketiga
- Atau gunakan pre-join di Google Sheets (lebih cepat)

**Q: Perbedaan Left Join vs Inner Join?**
A: 
- **Left Join**: Ambil semua data dari tabel kiri, meski tidak match
- **Inner Join**: Hanya ambil data yang match di kedua tabel
- Untuk analisis transaksi, gunakan Left Join

### Tentang Calculated Fields

**Q: Formula calculated field saya error, kenapa?**
A: Common errors:
- Typo nama field (case-sensitive)
- Lupa aggregation (SUM, AVG, COUNT)
- Pembagian dengan 0 (gunakan IFNULL)
- Syntax error (missing parentheses)

**Q: Bagaimana cara membuat percentage calculation?**
A: 
```
(SUM(metric1) / SUM(metric2)) * 100
```
Jangan lupa set format ke "Percent"

**Q: Bisa tidak menggunakan IF condition di calculated field?**
A: Bisa, gunakan CASE:
```
CASE
  WHEN condition1 THEN value1
  WHEN condition2 THEN value2
  ELSE default_value
END
```

**Q: Bagaimana cara handle NULL values?**
A: Gunakan IFNULL:
```
IFNULL(field_name, 0)
```
Atau COALESCE untuk multiple fallbacks

### Tentang Styling

**Q: Bagaimana cara membuat gradient color di KPI cards?**
A: 
1. Pilih scorecard
2. Tab STYLE → Background
3. Pilih "Gradient"
4. Set 2 colors untuk gradient

**Q: Font saya tidak konsisten, bagaimana cara fix?**
A: 
1. Klik "Theme and layout"
2. Set default font untuk semua elements
3. Atau select all charts → Apply same font

**Q: Bagaimana cara membuat rounded corners di charts?**
A: 
1. Pilih chart
2. Tab STYLE → Border
3. Set "Border radius" (8-12px recommended)

### Tentang Performance

**Q: Dashboard saya lambat loading, kenapa?**
A: Penyebab umum:
- Terlalu banyak data (> 100K rows)
- Terlalu banyak charts (> 15 per page)
- Blend kompleks (> 3 tables)
- Calculated fields berat

Solusi:
- Limit date range default
- Gunakan extract data
- Pre-aggregate di Google Sheets
- Split ke multiple pages

**Q: Bagaimana cara enable caching?**
A: 
1. Resource → Manage added data sources
2. Pilih data source
3. Data freshness → Set cache duration

---

## ⚠️ Troubleshooting

### Data Not Showing
- **Check data source connection**
- **Refresh data**: Resource → Refresh data
- **Check date range filter**

### Calculation Errors
- **Verify field names** (case-sensitive)
- **Check data types** (number vs text)
- **Use IFNULL()** for null values

### Slow Performance
- **Limit data range** (last 12 months)
- **Use aggregated data** instead of raw
- **Reduce number of charts** per page

### Blend Issues
- **Check join keys** match exactly
- **Verify join type** (left/inner/outer)
- **Test with small dataset** first

---

## ❓ FAQ - Pertanyaan yang Sering Ditanyakan

### Q1: Apakah saya harus membuat blend untuk setiap chart?
**A:** Tidak! Hanya untuk chart yang butuh data dari 2+ tabel. Contoh:
- ✅ Perlu blend: "Revenue per Kategori" (revenue dari Transaksi, kategori dari Produk)
- ❌ Tidak perlu: "Revenue per Bulan" (semua data dari Transaksi saja)

### Q2: Blend saya error "No data to display", kenapa?
**A:** Kemungkinan penyebab:
1. **Join key tidak match**: Cek apakah `id_produk` di kedua tabel formatnya sama
2. **Tidak ada data yang ter-join**: Coba ganti ke Full Outer Join untuk lihat semua data
3. **Filter terlalu ketat**: Lepas semua filter dulu, test dengan "All time"
4. **Field tidak di-include**: Pastikan field yang dibutuhkan sudah di-check saat setup blend

### Q3: Blend saya lambat, bagaimana cara mempercepat?
**A:** Tips optimasi:
1. **Batasi date range**: Gunakan filter "Last 6 months" instead of "All time"
2. **Pilih field seperlunya**: Jangan "Select all", pilih yang benar-benar dipakai
3. **Gunakan extract**: Resource → Extract data (untuk dataset besar)
4. **Pre-aggregate di Sheets**: Buat summary table di Google Sheets

### Q4: Bisa tidak blend 3 tabel sekaligus?
**A:** Bisa, tapi tidak recommended. Cara yang benar:
1. Buat Blend 1: Transaksi + Produk → Save as "Blend_Transaksi_Produk"
2. Buat Blend 2: Blend_Transaksi_Produk + Pelanggan → Save as "Blend_Full"
3. Gunakan Blend_Full untuk chart yang butuh data dari 3 tabel

### Q5: Apakah blend akan update otomatis jika data berubah?
**A:** Ya! Blend akan otomatis update ketika:
- Data source di-refresh
- Ada data baru di Google Sheets
- Anda klik "Refresh data" di Looker Studio

### Q6: Bagaimana cara menghapus blend yang salah?
**A:** 
1. Klik "Resource" → "Manage added data sources"
2. Cari blend yang ingin dihapus
3. Klik ikon titik tiga (⋮) → "Remove"
4. Confirm deletion

### Q7: Apakah saya bisa edit blend yang sudah dibuat?
**A:** Ya!
1. Klik "Resource" → "Manage added data sources"
2. Klik nama blend yang ingin diedit
3. Edit join keys, fields, atau join type
4. Klik "Save"

### Q8: Kenapa kategori produk saya muncul "null" atau kosong?
**A:** Kemungkinan:
1. **Ada transaksi dengan id_produk yang tidak ada di Master_Produk**
   - Solusi: Cek data, tambahkan produk yang hilang
2. **Field kategori tidak di-include dalam blend**
   - Solusi: Edit blend, pastikan field `kategori` ter-check
3. **Join type salah**
   - Solusi: Gunakan Left Outer Join

### Q9: Apakah saya bisa blend data dari sumber berbeda (Sheets + BigQuery)?
**A:** Ya! Looker Studio bisa blend data dari berbagai sumber:
- Google Sheets + BigQuery
- Google Analytics + Google Ads
- MySQL + PostgreSQL
- Dan lain-lain

### Q10: Bagaimana cara membuat blend untuk "Revenue per Kategori per Bulan"?
**A:** 
1. Buat blend: Transaksi + Produk (join by id_produk)
2. Di chart, gunakan:
   - Dimension 1: `MONTH(tanggal_transaksi)`
   - Dimension 2: `kategori`
   - Metric: `SUM(total_pembayaran)`
3. Chart type: Stacked column chart atau Pivot table

---

## 📚 Resources

### Looker Studio Documentation
- **Official Docs**: https://support.google.com/looker-studio
- **Community Forum**: https://www.en.advertisercommunity.com/t5/Data-Studio/ct-p/data-studio
- **Release Notes**: https://support.google.com/looker-studio/answer/11521624

### Video Tutorials (YouTube)
**Untuk Pemula:**
- "Looker Studio Tutorial for Beginners 2024" - Measureschool
- "How to Create Your First Dashboard in Looker Studio" - Google Analytics
- "Looker Studio Complete Course" - Loves Data

**Untuk BLEND:**
- "How to Blend Data in Looker Studio" - Measureschool
- "Data Blending Tutorial" - Analytics Mania
- "Advanced Blending Techniques" - Loves Data

**Bahasa Indonesia:**
- Search: "Tutorial Looker Studio Bahasa Indonesia"
- Search: "Cara Membuat Dashboard Looker Studio"

### Formula Reference
- **Calculated Fields Guide**: https://support.google.com/looker-studio/table/6379764
- **Functions List**: https://support.google.com/looker-studio/answer/7570353
- **Date Functions**: https://support.google.com/looker-studio/answer/7570353#date
- **Aggregation Functions**: https://support.google.com/looker-studio/answer/7570353#aggregation

### Design Inspiration
- **Looker Studio Gallery**: https://lookerstudio.google.com/gallery
- **Dashboard Templates**: https://lookerstudio.google.com/navigation/reporting
- **Community Dashboards**: Search "Looker Studio dashboard examples" di Google Images

### Google Sheets Functions (untuk pre-processing)
- **VLOOKUP Tutorial**: https://support.google.com/docs/answer/3093318
- **QUERY Function**: https://support.google.com/docs/answer/3093343
- **ARRAYFORMULA**: https://support.google.com/docs/answer/3093275

### Tools Pendukung
- **Color Picker**: https://htmlcolorcodes.com/
- **Chart Chooser**: https://www.data-to-viz.com/
- **Dashboard Design Guide**: https://www.tableau.com/learn/articles/dashboard-design-principles

---

## ✅ Checklist Completion

Setelah selesai, pastikan dashboard Anda memiliki:

### 1. Executive Dashboard
- [ ] 4 KPI cards (Revenue, Transactions, AOV, Customers)
- [ ] Revenue trend line chart
- [ ] Sales by channel donut chart
- [ ] Category performance pie chart
- [ ] Payment methods bar chart
- [ ] Order status donut chart
- [ ] Top 10 products table
- [ ] Date range filter

### 2. Sales Analysis
- [ ] 4 Sales KPI cards
- [ ] Channel performance table
- [ ] Day of week chart
- [ ] Monthly comparison chart
- [ ] Transaction status breakdown
- [ ] Recent transactions table

### 3. Product Performance
- [ ] 4 Product KPI cards
- [ ] Category analysis table
- [ ] Top 10 best sellers
- [ ] Bottom 10 slow movers
- [ ] Price distribution histogram
- [ ] Stock level pie chart
- [ ] Product catalog table

### 4. Customer Analytics
- [ ] 4 Customer KPI cards
- [ ] RFM segmentation chart
- [ ] Geographic distribution
- [ ] Customer type distribution
- [ ] Source channel chart
- [ ] Top 20 customers table
- [ ] Customer database table

### 5. Financial Dashboard
- [ ] 4 Financial KPI cards
- [ ] Revenue vs profit trend
- [ ] Profit margin trend
- [ ] Operational costs breakdown
- [ ] Revenue composition chart
- [ ] Expense details table

### 6. Operations & Inventory (BARU!)
- [ ] 4 Operations KPI cards
- [ ] Stock movement trend chart
- [ ] Movement by type chart
- [ ] Stock level by category
- [ ] Low stock alert table
- [ ] Stock movement history table
- [ ] Warehouse efficiency metrics

### 7. Marketing Performance (BARU!)
- [ ] 4 Marketing KPI cards
- [ ] Campaign ROI comparison chart
- [ ] Spend by channel chart
- [ ] Campaign performance over time
- [ ] Channel performance table
- [ ] Top performing campaigns table
- [ ] Customer acquisition cost (CAC)
- [ ] Marketing funnel chart
- [ ] Campaign status distribution

### General
- [ ] Consistent branding & colors across all 7 pages
- [ ] All filters working properly
- [ ] Cross-filtering enabled
- [ ] Mobile-responsive layout
- [ ] Navigation menu between pages
- [ ] Published & shared with stakeholders

---

## 🎓 Tips & Best Practices

### Design Tips
1. **Keep it simple**: Don't overcrowd pages
2. **Use white space**: Let charts breathe
3. **Consistent colors**: Stick to brand palette
4. **Clear labels**: Make everything self-explanatory
5. **Logical flow**: Top to bottom, left to right

### Data Tips
1. **Clean data first**: Fix issues in Google Sheets
2. **Use blends wisely**: Only when necessary
3. **Optimize calculations**: Pre-calculate in sheets if slow
4. **Test with sample**: Before full dataset
5. **Document formulas**: Add comments

### Performance Tips
1. **Limit date range**: Default to last 12 months
2. **Use extract data**: For large datasets
3. **Reduce chart complexity**: Fewer data points
4. **Optimize blends**: Only include needed fields
5. **Cache data**: Enable data freshness settings

---

## 📞 Support

Jika mengalami kesulitan:
1. **Check Looker Studio Help Center**
2. **Search YouTube tutorials**
3. **Ask in Google Community forums**
4. **Review this guide step-by-step**

---

**Selamat membuat dashboard! 🎉**

Dashboard Looker Studio Anda akan menjadi alat yang powerful untuk analisis bisnis SATRIAMART.

