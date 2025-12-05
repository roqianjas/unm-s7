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
3. Copy header dari halaman 1 (Ctrl+C, Ctrl+V) atau buat header baru dengan judul "Sales Analysis"

### 3.2 Sales Overview KPIs (4 Cards)

**Data Source untuk semua KPI Cards**: Transaksi_Penjualan

#### Card 1: Gross Sales

**Tujuan**: Menampilkan total penjualan sebelum diskon.

1. **Add chart → Scorecard**
2. **Data source**: Transaksi_Penjualan
3. **Setup Metric**:
   - **Field**: `subtotal`
   - **Aggregation**: SUM
   - **Label**: "Gross Sales"
   - **Format**: Currency (IDR)
4. **Style**:
   - **Background color**: #22C55E (hijau)
   - **Text color**: #FFFFFF (putih)
   - **Font size**: 32
   - **Compact numbers**: ON
5. **Posisi**: Top-left (x: 20, y: 100)
6. **Ukuran**: Width: 280px, Height: 140px

#### Card 2: Net Sales

**Tujuan**: Menampilkan total penjualan setelah diskon (revenue aktual).

1. **Duplicate Card 1** (Ctrl+D)
2. **Setup Metric**:
   - **Field**: `total_pembayaran`
   - **Aggregation**: SUM
   - **Label**: "Net Sales"
   - **Format**: Currency (IDR)
3. **Style**:
   - **Background color**: #3B82F6 (biru)
4. **Posisi**: Sebelah kanan Card 1 (x: 320, y: 100)

#### Card 3: Total Discounts

**Tujuan**: Menampilkan total diskon yang diberikan.

1. **Duplicate Card 2**
2. **Setup Metric**:
   - **Field**: `diskon_nominal`
   - **Aggregation**: SUM
   - **Label**: "Total Discounts"
   - **Format**: Currency (IDR)
3. **Style**:
   - **Background color**: #EF4444 (merah)
4. **Posisi**: Sebelah kanan Card 2 (x: 620, y: 100)
5. **Add Secondary Metric** (optional):
   - Calculated: `(SUM(diskon_nominal) / SUM(subtotal)) * 100`
   - Label: "% of Gross Sales"
   - Format: Percent

#### Card 4: Shipping Revenue

**Tujuan**: Menampilkan total pendapatan dari biaya pengiriman.

1. **Duplicate Card 3**
2. **Setup Metric**:
   - **Field**: `biaya_ongkir`
   - **Aggregation**: SUM
   - **Label**: "Shipping Revenue"
   - **Format**: Currency (IDR)
3. **Style**:
   - **Background color**: #FB923C (orange)
4. **Posisi**: Sebelah kanan Card 3 (x: 920, y: 100)

### 3.3 Channel Performance Table

**Tujuan**: Menampilkan performa penjualan per channel dengan metrics lengkap.

1. **Add chart → Table with heatmap**
2. **Data source**: Transaksi_Penjualan
3. **Setup Dimension**:
   - **Field**: `channel_penjualan`
   - **Label**: "Sales Channel"
4. **Setup Metrics**:
   - **Metric 1**: `COUNT(id_transaksi)` 
     - Label: "Transactions"
     - Format: Number
   - **Metric 2**: `SUM(total_pembayaran)` 
     - Label: "Revenue"
     - Format: Currency (IDR)
   - **Metric 3**: `AVG(total_pembayaran)` 
     - Label: "Avg Order Value"
     - Format: Currency (IDR)
   - **Metric 4**: Calculated field `AOV_Calculated`
     - Formula: `SUM(total_pembayaran) / COUNT(id_transaksi)`
     - Label: "AOV (Calculated)"
     - Format: Currency (IDR)
5. **Sort**: By Revenue (Descending)
6. **Style**:
   - **Heatmap**: ON untuk Revenue column
   - **Color scale**: Green gradient
   - **Show bars**: ON untuk Revenue
   - **Alternating rows**: ON
7. **Posisi**: Di bawah KPI cards (x: 20, y: 260)
8. **Ukuran**: Width: 1160px, Height: 320px

### 3.4 Sales by Day of Week

**Tujuan**: Mengidentifikasi hari dengan penjualan tertinggi untuk optimasi operasional.

1. **Add chart → Bar chart**
2. **Data source**: Transaksi_Penjualan
3. **Setup Dimension**: Calculated field `Day_of_Week`
   - **Klik "Add dimension" → "CREATE FIELD"**
   - **Field Name**: `Day_of_Week`
   - **Formula**: 
     ```
     CASE
       WHEN WEEKDAY(tanggal_transaksi) = 1 THEN 'Sunday'
       WHEN WEEKDAY(tanggal_transaksi) = 2 THEN 'Monday'
       WHEN WEEKDAY(tanggal_transaksi) = 3 THEN 'Tuesday'
       WHEN WEEKDAY(tanggal_transaksi) = 4 THEN 'Wednesday'
       WHEN WEEKDAY(tanggal_transaksi) = 5 THEN 'Thursday'
       WHEN WEEKDAY(tanggal_transaksi) = 6 THEN 'Friday'
       WHEN WEEKDAY(tanggal_transaksi) = 7 THEN 'Saturday'
     END
     ```
   - **Klik "SAVE"** → **Klik "DONE"**
   
   **Alternatif lebih sederhana** (jika hanya perlu angka):
   - **Formula**: `WEEKDAY(tanggal_transaksi)`
   - Hasil: 1=Sunday, 2=Monday, ..., 7=Saturday
4. **Setup Metric**:
   - **Field**: `total_pembayaran`
   - **Aggregation**: SUM
   - **Label**: "Revenue"
   - **Format**: Currency (IDR)
5. **Sort**: Custom order
   - Manual: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
   - Atau by metric (Descending) untuk lihat hari terlaris
6. **Style**:
   - **Orientation**: Vertical (bars tegak)
   - **Bar color**: #3B82F6 (biru)
   - **Show data labels**: ON
   - **Grid lines**: ON
7. **Posisi**: Baris baru (x: 20, y: 600)
8. **Ukuran**: Width: 560px, Height: 320px

**Catatan**: Di Looker Studio, "Bar chart" bisa diatur orientasinya (horizontal/vertical) di tab Style.

### 3.5 Monthly Sales Comparison

**Tujuan**: Membandingkan revenue dan jumlah transaksi per bulan.

1. **Add chart → Combo chart**
2. **Data source**: Transaksi_Penjualan
3. **Setup Dimension**:
   - **Field**: `tanggal_transaksi`
   - **Type**: Date
   - **Granularity**: Month (MONTH atau YEAR_MONTH)
4. **Setup Metrics**:
   - **Metric 1 - Revenue**: `SUM(total_pembayaran)`
     - Chart type: **Bar** (vertical bars)
     - Color: #22C55E (hijau)
     - Axis: Left (primary)
   - **Metric 2 - Transactions**: `COUNT(id_transaksi)`
     - Chart type: **Line**
     - Color: #A855F7 (ungu)
     - Axis: Right (secondary)
5. **Style**:
   - **Show data labels**: ON untuk line
   - **Legend**: Bottom
   - **Grid lines**: ON
   - **Axis titles**: 
     - Left: "Revenue (IDR)"
     - Right: "Transactions"
6. **Posisi**: Sebelah kanan Day of Week (x: 620, y: 600)
7. **Ukuran**: Width: 560px, Height: 320px

### 3.6 Transaction Status Breakdown

**Tujuan**: Menampilkan distribusi status pesanan dan pembayaran untuk analisis konversi.

1. **Add chart → Stacked bar chart**
2. **Data source**: Transaksi_Penjualan
3. **Setup**:
   - **Dimension**: `status_pembayaran`
   - **Breakdown dimension**: `status_pesanan`
   - **Metric**: `COUNT(id_transaksi)`
   - **Sort**: By metric (Descending)
4. **Style**:
   - **Bar colors**: Custom per status
     - Selesai: #22C55E (hijau)
     - Proses: #FB923C (orange)
     - Dibatalkan: #EF4444 (merah)
   - **Show data labels**: ON
   - **Legend position**: Bottom
5. **Posisi**: Di bawah Monthly Comparison (y: 940)
6. **Ukuran**: Width: 580px, Height: 320px

### 3.7 Recent Transactions Table

**Tujuan**: Menampilkan 20 transaksi terbaru dengan detail lengkap untuk monitoring real-time.

1. **Add chart → Table**
2. **Data source**: Transaksi_Penjualan
3. **Setup Dimensions**:
   - `tanggal_transaksi` → Format: Date & Time
   - `id_transaksi` → Label: "Transaction ID"
   - `id_pelanggan` → Label: "Customer ID"
   - `channel_penjualan` → Label: "Channel"
   - `status_pesanan` → Label: "Status"
4. **Setup Metrics**:
   - `total_pembayaran` → Label: "Amount"
   - Format: Currency (IDR)
5. **Sort**: `tanggal_transaksi` (Descending) - transaksi terbaru di atas
6. **Rows per page**: 20
7. **Style**:
   - **Header**: Bold, Background #F3F4F6
   - **Alternating rows**: ON
   - **Row numbers**: OFF (tidak perlu untuk table ini)
   - **Conditional formatting** untuk status:
     - Selesai: Green text
     - Proses: Orange text
     - Dibatalkan: Red text
8. **Posisi**: Di bawah Transaction Status (y: 1280)
9. **Ukuran**: Width: 1160px, Height: 500px

**Tips**: Tambahkan filter control untuk channel dan status di atas table untuk interaktivitas.

### 3.8 Tambahkan Filter Controls

**Tujuan**: Memberikan interaktivitas untuk filter data berdasarkan periode, channel, dan status.

#### Filter 1: Date Range Control

1. **Add a control → Date range control**
2. **Setup**:
   - **Data source**: Transaksi_Penjualan
   - **Control field**: `tanggal_transaksi`
   - **Default date range**: Last 12 months (atau Custom)
   - **Comparison date range**: OFF
3. **Style**:
   - **Control type**: Compact
   - **Background**: #FFFFFF (putih)
   - **Border**: #D1D5DB (abu-abu)
   - **Text color**: #374151
   - **Accent color**: #22C55E (hijau)
   - **Border radius**: 8px
4. **Posisi**: Top-right corner (x: 1000, y: 20)
5. **Ukuran**: Width: 180px, Height: 40px

**Add Label** (optional):
- **Add text** di atas control
- Text: "Filter Periode:"
- Font: Roboto Medium, Size: 12
- Color: #6B7280
- Position: (x: 1000, y: 5)

#### Filter 2: Channel Filter

1. **Add a control → Drop-down list**
2. **Setup**:
   - **Data source**: Transaksi_Penjualan
   - **Control field**: `channel_penjualan`
   - **Allow multiple selections**: YES
   - **Include "All" option**: YES
   - **Default selection**: All
3. **Style**:
   - **Control type**: Drop-down list
   - **Background**: #FFFFFF
   - **Border**: #D1D5DB
   - **Border radius**: 8px
4. **Posisi**: Below date range (x: 1000, y: 70)
5. **Ukuran**: Width: 180px, Height: 40px

**Add Label**:
- Text: "Sales Channel:"
- Position: (x: 1000, y: 55)

#### Filter 3: Status Filter

1. **Add a control → Drop-down list**
2. **Setup**:
   - **Data source**: Transaksi_Penjualan
   - **Control field**: `status_pesanan`
   - **Allow multiple selections**: YES
   - **Include "All" option**: YES
   - **Default selection**: All
3. **Style**:
   - Same as Channel Filter
4. **Posisi**: Below channel filter (x: 1000, y: 120)
5. **Ukuran**: Width: 180px, Height: 40px

**Add Label**:
- Text: "Order Status:"
- Position: (x: 1000, y: 105)

#### Filter 4: Payment Status Filter (Optional)

1. **Add a control → Drop-down list**
2. **Setup**:
   - **Data source**: Transaksi_Penjualan
   - **Control field**: `status_pembayaran`
   - **Allow multiple selections**: YES
   - **Include "All" option**: YES
3. **Posisi**: Below status filter (x: 1000, y: 170)
4. **Ukuran**: Width: 180px, Height: 40px

### 3.9 Test Interaktivitas

1. **Klik "View"** untuk masuk preview mode
2. **Test setiap filter**:
   - Ubah date range → semua charts harus update
   - Pilih channel tertentu → data ter-filter
   - Pilih status → table dan charts berubah
3. **Verify**:
   - KPI cards menunjukkan angka yang sesuai filter
   - Charts menampilkan data yang ter-filter
   - Table hanya menampilkan data sesuai kriteria
4. **Klik "Edit"** untuk kembali ke edit mode

### 🎯 Checklist: Sales Analysis Dashboard Selesai

Setelah menyelesaikan Langkah 3, pastikan Anda punya:

- [ ] **Header & Title** "Sales Analysis"
- [ ] **4 KPI Cards** (Gross Sales, Net Sales, Discounts, Shipping)
- [ ] **Channel Performance Table** dengan heatmap
- [ ] **Sales by Day of Week Chart** (bar chart vertikal)
- [ ] **Monthly Sales Comparison** (combo chart)
- [ ] **Transaction Status Breakdown** (stacked bar)
- [ ] **Recent Transactions Table** (20 rows)
- [ ] **4 Filter Controls** (Date Range, Channel, Status, Payment Status)
- [ ] **All filters working** dan charts update otomatis
- [ ] **Consistent styling** dengan halaman 1

### 💡 Tips Sebelum Lanjut ke Halaman 3

1. **Save your work**: Ctrl+S
2. **Test all filters**: Pastikan semua bekerja dengan baik
3. **Check data accuracy**: Bandingkan angka dengan dashboard HTML
4. **Preview mode**: Lihat tampilan akhir
5. **Copy page**: Untuk template halaman Product Performance

---

## 🛍️ Langkah 4: Membuat Product Performance Dashboard (Halaman 3)

### 4.1 Tambah Halaman Baru
1. Klik **"Page" → "New page"**
2. Rename: **"Product Performance"**
3. Copy header dari halaman 1

### 4.2 Product Overview KPIs (4 Cards)

**Data Source untuk semua KPI Cards**: Master_Produk (dan blend untuk metrics penjualan)

#### Card 1: Total Products

**Tujuan**: Menampilkan jumlah total produk dalam katalog.

1. **Add chart → Scorecard**
2. **Data source**: Master_Produk
3. **Setup Metric**:
   - **Field**: `id_produk`
   - **Aggregation**: COUNT DISTINCT
   - **Label**: "Total Products"
   - **Format**: Number
4. **Style**:
   - **Background color**: #22C55E (hijau)
   - **Text color**: #FFFFFF (putih)
   - **Font size**: 36
5. **Add Secondary Metric** (optional):
   - Filter: `status_aktif = 'Aktif'`
   - Label: "active products"
6. **Posisi**: Top-left (x: 20, y: 100)
7. **Ukuran**: Width: 280px, Height: 140px

#### Card 2: Inventory Value

**Tujuan**: Menampilkan nilai total inventory berdasarkan harga modal.

1. **Duplicate Card 1**
2. **Setup Metric**: Calculated field `Inventory_Value`
   - **Klik "Add metric" → "CREATE FIELD"**
   - **Field Name**: `Inventory_Value`
   - **Formula**: 
     ```
     SUM(harga_modal * stok_tersedia)
     ```
   - **Klik "SAVE"** → **Klik "DONE"**
   - **Label**: "Inventory Value"
   - **Format**: Currency (IDR)
3. **Style**:
   - **Background color**: #3B82F6 (biru)
4. **Posisi**: Sebelah kanan Card 1 (x: 320, y: 100)

#### Card 3: Avg Profit Margin

**Tujuan**: Menampilkan rata-rata profit margin dari semua produk.

⚠️ **PENTING - Formula Persentase yang Benar:**

1. **Duplicate Card 2**
2. **Setup Metric**: Calculated field `Avg_Profit_Margin`
   - **Field Name**: `Avg_Profit_Margin`
   - **Formula** (TANPA * 100):
     ```
     AVG((harga_jual - harga_modal) / harga_jual)
     ```
   - **Data type**: **Percent** (Looker Studio akan otomatis × 100)
   - **Label**: "Avg Profit Margin"
3. **Style**:
   - **Background color**: #A855F7 (ungu)
   - **Format**: Percent dengan 1 decimal
4. **Posisi**: Sebelah kanan Card 2 (x: 620, y: 100)

**Catatan**: Jangan tambahkan `* 100` di formula jika Data type = Percent, karena akan jadi ribuan!

#### Card 4: Low Stock Items

**Tujuan**: Menampilkan jumlah produk dengan stok rendah (< 10 unit).

1. **Duplicate Card 3**
2. **Data source**: Master_Produk
3. **Setup Metric**:
   - **Field**: `id_produk`
   - **Aggregation**: COUNT
   - **Label**: "Low Stock Items"
   - **Format**: Number
4. **Add Filter**:
   - **Klik "Add a filter"**
   - **Include**: `stok_tersedia` < 10
5. **Style**:
   - **Background color**: #FB923C (orange)
6. **Add Secondary Metric** (optional):
   - Text: "Below 10 units"
7. **Posisi**: Sebelah kanan Card 3 (x: 920, y: 100)

### 4.3 Category Analysis Table

**Tujuan**: Menampilkan performa setiap kategori produk dengan metrics lengkap.

1. **Add chart → Table with bars**
2. **Data source**: Blend "Transaksi_with_Product_Info" (buat jika belum ada)
3. **Setup Dimension**:
   - `kategori` (dari Master_Produk)
4. **Setup Metrics**:
   - **Revenue**: `SUM(total_pembayaran)` → Format: Currency (IDR)
   - **Product Count**: `COUNT_DISTINCT(id_produk)` → Format: Number
   - **Units Sold**: `SUM(jumlah_item)` → Format: Number
   - **Avg Price**: Calculated field
     ```
     SUM(total_pembayaran) / SUM(jumlah_item)
     ```
     Format: Currency (IDR)
   - **Avg Profit Margin**: Calculated field (perlu blend dengan harga_modal)
     ```
     AVG((harga_jual - harga_modal) / harga_jual * 100)
     ```
     Format: Percent
5. **Sort**: By Revenue (Descending)
6. **Style**:
   - **Bar chart column**: Revenue (show bars in table)
   - **Heatmap**: ON untuk Profit Margin column
   - **Alternating rows**: ON
7. **Posisi**: Di bawah KPI cards (y: 260)
8. **Ukuran**: Width: 1160px, Height: 400px

### 4.4 Top 10 Best Sellers

**Tujuan**: Menampilkan 10 produk dengan penjualan tertinggi berdasarkan jumlah unit terjual.

1. **Add chart → Bar chart (horizontal)**
2. **Data source**: Blend "Transaksi_with_Product_Info"
3. **Setup**:
   - **Dimension**: `nama_produk` (dari Master_Produk)
   - **Metric**: `SUM(jumlah_item)` → Label: "Units Sold"
   - **Sort**: Descending (terbanyak di atas)
   - **Limit**: 10 rows
4. **Style**:
   - **Bar color**: #22C55E (hijau)
   - **Show data labels**: ON
   - **Axis labels**: Clear and readable
5. **Posisi**: Sebelah kiri (x: 20, y: 680)
6. **Ukuran**: Width: 560px, Height: 400px

**Catatan**: Jika ingin berdasarkan revenue, ganti metric dengan `SUM(total_pembayaran)`.

### 4.5 Bottom 10 Slow Movers

**Tujuan**: Mengidentifikasi produk dengan penjualan terendah yang mungkin perlu strategi khusus.

1. **Add chart → Bar chart (horizontal)**
2. **Data source**: Blend "Transaksi_with_Product_Info"
3. **Setup**:
   - **Dimension**: `nama_produk` (dari Master_Produk)
   - **Metric**: `SUM(jumlah_item)` → Label: "Units Sold"
   - **Sort**: Ascending (tersedikit di atas)
   - **Limit**: 10 rows
4. **Style**:
   - **Bar color**: #FB923C (orange) - untuk highlight perhatian
   - **Show data labels**: ON
   - **Axis labels**: Clear and readable
5. **Posisi**: Sebelah kanan Top Sellers (x: 620, y: 680)
6. **Ukuran**: Width: 560px, Height: 400px

**Tips**: Tambahkan filter untuk exclude produk baru (< 30 hari) agar analisis lebih akurat.

### 4.6 Price Range Distribution

**Tujuan**: Menampilkan distribusi produk berdasarkan range harga untuk analisis pricing strategy.

1. **Add chart → Bar chart**
2. **Data source**: Master_Produk
3. **Setup Dimension**: Calculated field `Price_Range`
   - **Klik "Add dimension" → "CREATE FIELD"**
   - **Field Name**: `Price_Range`
   - **Formula**:
     ```
     CASE
       WHEN harga_jual < 100000 THEN '< 100K'
       WHEN harga_jual < 200000 THEN '100K - 200K'
       WHEN harga_jual < 300000 THEN '200K - 300K'
       WHEN harga_jual < 500000 THEN '300K - 500K'
       ELSE '> 500K'
     END
     ```
   - **Klik "SAVE"** → **Klik "DONE"**
4. **Setup Metric**:
   - **Field**: `id_produk`
   - **Aggregation**: COUNT
   - **Label**: "Number of Products"
   - **Format**: Number
5. **Sort**: 
   - **Default**: Alphabetical (akan salah urutan: > 500K, < 100K, 100K-200K, dst)
   - **Solusi**: Gunakan **Sort by Metric** (Ascending atau Descending)
   - Atau buat **Calculated field dengan angka** untuk sorting:
     ```
     CASE
       WHEN harga_jual < 100000 THEN 1
       WHEN harga_jual < 200000 THEN 2
       WHEN harga_jual < 300000 THEN 3
       WHEN harga_jual < 500000 THEN 4
       ELSE 5
     END
     ```
     Lalu sort by field ini (Ascending)
   
   **Cara Manual Order** (jika perlu):
   - Setelah chart dibuat, klik chart
   - Tab **SETUP** → bagian **Sort**
   - Pilih dimension yang ingin di-sort
   - Klik **"Custom"** atau **"Manual"** (jika tersedia)
   - Drag & drop urutan di list yang muncul
   - Atau gunakan **filter** untuk exclude data yang tidak perlu
6. **Style**:
   - **Orientation**: **Vertical** (bars tegak ke atas)
   - **Bar color**: #3B82F6 (biru)
   - **Show data labels**: ON
   - **Grid lines**: ON
7. **Posisi**: Baris baru di bawah (x: 20, y: 1100)
8. **Ukuran**: Width: 560px, Height: 320px

**Catatan**: Di Looker Studio, gunakan **Bar chart** dengan orientation **Vertical** untuk membuat bar tegak (seperti column chart).

**💡 Tips Sorting yang Benar:**

Karena Looker Studio akan sort alphabetically secara default, urutan akan jadi:
- ❌ Salah: `> 500K`, `< 100K`, `100K-200K`, `200K-300K`, `300K-500K`

**Solusi Terbaik**: Buat calculated field dengan prefix angka:
```
CASE
  WHEN harga_jual < 100000 THEN '1. < 100K'
  WHEN harga_jual < 200000 THEN '2. 100K-200K'
  WHEN harga_jual < 300000 THEN '3. 200K-300K'
  WHEN harga_jual < 500000 THEN '4. 300K-500K'
  ELSE '5. > 500K'
END
```
Dengan prefix angka, sorting alphabetical akan otomatis benar! ✅

**Alternatif**: Sort by metric (COUNT) jika data sudah terurut natural.

**Alternatif**: Jika Looker Studio support histogram, gunakan:
- Dimension: `harga_jual` (numeric)
- Bucket size: 100000
- Akan otomatis group data

### 4.7 Stock Level Pie Chart

**Tujuan**: Visualisasi distribusi level stok untuk inventory management.

1. **Add chart → Pie chart**
2. **Data source**: Master_Produk
3. **Setup Dimension**: Calculated field `Stock_Level`
   - **Klik "Add dimension" → "CREATE FIELD"**
   - **Field Name**: `Stock_Level`
   - **Formula**: 
     ```
     CASE
       WHEN stok_tersedia < 5 THEN 'Critical (< 5)'
       WHEN stok_tersedia < 10 THEN 'Low (5-10)'
       WHEN stok_tersedia < 20 THEN 'Medium (10-20)'
       ELSE 'Healthy (> 20)'
     END
     ```
   - **Klik "SAVE"** → **Klik "DONE"**
4. **Setup Metric**: 
   - `COUNT(id_produk)` → Label: "Products"
5. **Style**:
   - **Slice colors**: Custom
     - Critical: #EF4444 (merah)
     - Low: #FB923C (orange)
     - Medium: #FCD34D (kuning)
     - Healthy: #22C55E (hijau)
   - **Show legend**: Bottom
   - **Show percentage**: ON
   - **Show data labels**: Value + Percentage
6. **Posisi**: Sebelah kanan Price Range (x: 620, y: 1100)
7. **Ukuran**: Width: 560px, Height: 320px

### 4.7 Product Catalog Table

**Tujuan**: Menampilkan katalog produk lengkap dengan semua informasi penting.

1. **Add chart → Table**
2. **Data source**: Master_Produk (atau blend jika perlu sales data)
3. **Setup Dimensions**:
   - `nama_produk` → Label: "Product Name"
   - `kategori` → Label: "Category"
   - `sub_kategori` → Label: "Sub-Category"
4. **Setup Metrics**:
   - `harga_jual` → Label: "Price", Format: Currency (IDR)
   - `harga_modal` → Label: "Cost", Format: Currency (IDR)
   - Calculated: `(harga_jual - harga_modal) / harga_jual * 100` → Label: "Margin %", Format: Percent
   - `stok_tersedia` → Label: "Stock", Format: Number
   - (Optional) Dari blend: Units sold, Revenue
5. **Sort**: By `nama_produk` (Alphabetical)
6. **Rows per page**: 20
7. **Style**:
   - **Conditional formatting** untuk Stock:
     - Red if < 5
     - Orange if 5-10
     - Green if > 10
   - **Alternating rows**: ON
   - **Show row numbers**: OFF
8. **Add Filter Controls** (di atas table):
   - **Category filter**: Drop-down list untuk `kategori`
   - **Search box**: Text input untuk search product name
   - **Stock level filter**: Drop-down untuk stock status
9. **Posisi**: Baris baru di bawah (y: 1440)
10. **Ukuran**: Width: 1160px, Height: 600px

**Tips Interaktivitas**:
- Klik product name untuk drill-down ke detail
- Enable cross-filtering dengan charts lain
- Add "Export to CSV" option untuk users

### 4.8 Tambahkan Filter Controls

**Tujuan**: Memberikan interaktivitas untuk filter produk berdasarkan kategori dan stock level.

#### Filter 1: Date Range Control (untuk data penjualan)

1. **Add a control → Date range control**
2. **Setup**:
   - **Data source**: Transaksi_Penjualan (jika menggunakan blend)
   - **Control field**: `tanggal_transaksi`
   - **Default**: Last 12 months
3. **Style**: Compact, Accent color: #22C55E
4. **Posisi**: Top-right (x: 1000, y: 20)
5. **Ukuran**: Width: 180px, Height: 40px

#### Filter 2: Category Filter

1. **Add a control → Drop-down list**
2. **Setup**:
   - **Data source**: Master_Produk
   - **Control field**: `kategori`
   - **Allow multiple**: YES
   - **Include "All"**: YES
3. **Posisi**: Below date range (x: 1000, y: 70)
4. **Ukuran**: Width: 180px, Height: 40px

#### Filter 3: Stock Level Filter

1. **Add a control → Drop-down list**
2. **Setup**:
   - **Data source**: Master_Produk
   - **Control field**: Calculated `Stock_Level` (yang sudah dibuat di 4.7)
   - **Allow multiple**: YES
3. **Posisi**: Below category (x: 1000, y: 120)
4. **Ukuran**: Width: 180px, Height: 40px

### 🎯 Checklist: Product Performance Dashboard Selesai

- [ ] **Header & Title** "Product Performance"
- [ ] **4 KPI Cards** (Total Products, Inventory Value, Avg Margin, Low Stock)
- [ ] **Category Analysis Table** dengan heatmap
- [ ] **Top 10 Best Sellers** (bar chart)
- [ ] **Bottom 10 Slow Movers** (bar chart)
- [ ] **Price Range Distribution** (bar chart)
- [ ] **Stock Level Pie Chart** dengan color coding
- [ ] **Product Catalog Table** dengan conditional formatting
- [ ] **3 Filter Controls** (Date Range, Category, Stock Level)
- [ ] **All filters working** properly
- [ ] **Profit margin formula** TANPA * 100 (penting!)

### 💡 Tips Sebelum Lanjut ke Halaman 4

1. **Double-check formula persentase**: Pastikan tidak ada * 100 jika Data type = Percent
2. **Test blend**: Pastikan Transaksi_with_Product_Info bekerja dengan baik
3. **Verify stock levels**: Check apakah conditional formatting sudah benar
4. **Save your work**: Ctrl+S

---

## 👥 Langkah 5: Membuat Customer Analytics Dashboard (Halaman 4)

### 5.1 Tambah Halaman Baru
1. Klik **"Page" → "New page"**
2. Rename: **"Customer Analytics"**
3. Copy header dari halaman 1

### 5.2 Buat Blend: Customer dengan Transaksi

**Tujuan**: Menggabungkan data pelanggan dengan transaksi untuk mendapatkan metrics seperti total spent, avg order value, dll.

#### Step A: Buat Blend Data Source

1. **Klik menu "Resource"** di toolbar atas
2. **Pilih "Manage added data sources"**
3. **Klik tombol "+ ADD A DATA SOURCE"** (pojok kanan bawah)
4. **Pilih "BLEND DATA"** (ikon dengan 2 tabel yang overlap)

#### Step B: Configure Blend - Table 1 (Left)

1. **Klik "Add data source"**
2. **Pilih**: **Master_Pelanggan**
3. **Join key**: Pilih field **`id_pelanggan`**
4. **Dimensions yang diambil**:
   - ✅ `id_pelanggan`
   - ✅ `nama_lengkap`
   - ✅ `email`
   - ✅ `no_telepon`
   - ✅ `kota`
   - ✅ `provinsi`
   - ✅ `jenis_pelanggan`
   - ✅ `jenis_kelamin`
   - ✅ `usia`
   - ✅ `total_transaksi` (jika ada di Master_Pelanggan)
   - ✅ `total_nilai_pembelian` (jika ada di Master_Pelanggan)

#### Step C: Configure Blend - Table 2 (Right)

1. **Klik "Add another data source"**
2. **Pilih**: **Transaksi_Penjualan**
3. **Join key**: Pilih field **`id_pelanggan`** (harus sama dengan Table 1)
4. **Metrics yang diambil**:
   - ✅ `total_pembayaran` (SUM)
   - ✅ `id_transaksi` (COUNT)
   - ✅ `jumlah_item` (SUM)
   - ✅ `rating_pelanggan` (AVG)
   - ✅ `tanggal_transaksi` (untuk analisis recency)

#### Step D: Set Join Configuration

1. **Join operator**: **Left Outer Join** (default)
   - Artinya: Ambil semua pelanggan, dan tambahkan data transaksi jika ada
   - Pelanggan yang belum pernah transaksi tetap muncul (dengan nilai 0)

#### Step E: Rename dan Save Blend

1. **Klik nama blend** (biasanya "Blend 1")
2. **Rename menjadi**: **"Customer_with_Transactions"**
3. **Klik "SAVE"** (pojok kanan atas)
4. **Klik "CLOSE"** untuk kembali ke report

**✅ Blend siap digunakan!** Sekarang Anda bisa pakai "Customer_with_Transactions" sebagai data source untuk charts yang butuh data dari kedua tabel.

---

### 5.3 Customer Overview KPIs (4 Cards)

**Data Source**: Master_Pelanggan dan Blend "Customer_with_Transactions"

#### Card 1: Total Customers

1. **Add chart → Scorecard**
2. **Data source**: Master_Pelanggan
3. **Setup Metric**:
   - **Field**: `id_pelanggan`
   - **Aggregation**: COUNT DISTINCT
   - **Label**: "Total Customers"
4. **Style**:
   - **Background**: #22C55E (hijau)
   - **Text color**: #FFFFFF
   - **Font size**: 36
5. **Posisi**: (x: 20, y: 100)
6. **Ukuran**: Width: 280px, Height: 140px

#### Card 2: Avg Customer Value

1. **Duplicate Card 1**
2. **Data source**: Ganti ke **"Customer_with_Transactions"** (blend yang sudah dibuat)
3. **Setup Metric**: Calculated field
   - **Klik "Add metric" → "CREATE FIELD"**
   - **Field Name**: `Avg_Customer_Value`
   - **Formula**: 
     ```
     SUM(total_pembayaran) / COUNT_DISTINCT(id_pelanggan)
     ```
   - **Klik "SAVE"** → **Klik "DONE"**
   - **Label**: "Avg Customer Value"
   - **Format**: Currency (IDR)
4. **Style**: Background #3B82F6 (biru)
5. **Posisi**: (x: 320, y: 100)

#### Card 3: Repeat Customer Rate

1. **Duplicate Card 2**
2. **Setup Metric**: Calculated field
   - **Formula** (TANPA * 100):
     ```
     COUNT(CASE WHEN total_transaksi > 1 THEN id_pelanggan END) / 
     COUNT(id_pelanggan)
     ```
   - **Data type**: Percent
   - **Label**: "Repeat Rate"
3. **Style**: Background #A855F7 (ungu)
4. **Posisi**: (x: 620, y: 100)

#### Card 4: Avg Rating

1. **Duplicate Card 3**
2. **Data source**: Blend dengan Transaksi_Penjualan
3. **Setup Metric**:
   - **Field**: `rating_pelanggan`
   - **Aggregation**: AVG
   - **Label**: "Avg Rating"
   - **Format**: Number (1 decimal)
4. **Style**: Background #FB923C (orange)
5. **Posisi**: (x: 920, y: 100)

### 5.4 RFM Segmentation

**Tujuan**: Segmentasi pelanggan berdasarkan Recency, Frequency, Monetary untuk targeted marketing.

**Catatan**: Jika field `segmen` tidak ada di data, buat calculated field atau lakukan segmentasi manual di Google Sheets terlebih dahulu.

1. **Add chart → Pie chart** (atau Donut chart)
2. **Data source**: Master_Pelanggan
3. **Setup**:
   - **Dimension**: `segmen` (atau `jenis_pelanggan` jika segmen tidak ada)
   - **Metric**: `COUNT(id_pelanggan)` → Label: "Customers"
4. **Style - Custom Colors per Segment**:
   - **VIP**: #FCD34D (gold/kuning)
   - **Loyal**: #22C55E (hijau)
   - **Regular**: #3B82F6 (biru)
   - **High Value**: #A855F7 (ungu)
   - **New**: #9CA3AF (abu-abu)
5. **Legend**: Bottom, Show percentage
6. **Posisi**: Sebelah kiri (x: 20, y: 260)
7. **Ukuran**: Width: 560px, Height: 320px

**Alternatif jika tidak ada field segmen**: Buat calculated field berdasarkan `total_transaksi` dan `total_nilai_pembelian`:
```
CASE
  WHEN total_transaksi >= 4 THEN 'VIP'
  WHEN total_transaksi >= 2 AND total_nilai_pembelian >= 500000 THEN 'Loyal'
  WHEN total_transaksi >= 2 THEN 'Regular'
  WHEN total_nilai_pembelian >= 300000 THEN 'High Value'
  ELSE 'New'
END
```

### 5.5 Geographic Distribution

**Tujuan**: Menampilkan distribusi pelanggan dan revenue berdasarkan lokasi geografis.

⚠️ **MASALAH GEO CHART**: Geo chart di Looker Studio **sangat strict** dengan format data. Field `kota` atau `provinsi` dari data Anda kemungkinan **tidak dikenali** sebagai geo data.

**Kenapa "No results" di Geo dimension?**
- Looker Studio hanya mengenali field dengan **Geo data type**
- Field text biasa (seperti "kota", "provinsi") **tidak muncul** di Geo dimension
- Perlu **set data type** menjadi Geo atau gunakan format khusus

**❌ Opsi 1: Geo Chart (SKIP - Terlalu Ribet)**

Geo chart memerlukan:
1. Field harus di-set sebagai **Geo type** di data source
2. Format nama harus **exact match** dengan database Google (contoh: "DKI Jakarta", bukan "Jakarta")
3. Perlu **geocoding** yang sering gagal untuk data Indonesia

**Kesimpulan**: Geo chart **tidak recommended** untuk data Indonesia karena sering bermasalah.

**✅ Opsi 2: Table with Bars (RECOMMENDED - Mudah & Jelas)**

1. **Add chart → Table with bars**
2. **Data source**: Blend Master_Pelanggan + Transaksi_Penjualan
3. **Setup Dimensions**:
   - `kota` → Label: "City"
4. **Setup Metrics**:
   - `COUNT_DISTINCT(id_pelanggan)` → Label: "Customers"
   - `SUM(total_nilai_pembelian)` → Label: "Revenue", Format: Currency
   - Calculated: `SUM(total_nilai_pembelian) / COUNT_DISTINCT(id_pelanggan)` → Label: "Avg per Customer"
5. **Sort**: By Revenue (Descending)
6. **Limit**: Top 10 cities
7. **Style**: Show bars for Revenue column
8. **Posisi**: Sebelah kanan RFM (x: 620, y: 260)
9. **Ukuran**: Width: 560px, Height: 320px

**💡 Kenapa Pakai Table Instead of Geo Chart?**

**Kelebihan Table:**
- ✅ Langsung bisa dipakai, tidak perlu setup geo type
- ✅ Data lebih jelas dan mudah dibaca
- ✅ Bisa sort dan filter dengan mudah
- ✅ Bisa tambah multiple metrics
- ✅ Tidak tergantung format nama lokasi

**Kekurangan Geo Chart:**
- ❌ Perlu set geo data type (ribet)
- ❌ Format nama harus exact match
- ❌ Sering "No results" untuk data Indonesia
- ❌ Tidak bisa custom region dengan mudah
- ❌ Sulit troubleshoot jika error

**Rekomendasi**: Gunakan **Table with bars** untuk geographic analysis. Lebih praktis dan informatif!

### 5.6 Customer Type Distribution

**Tujuan**: Menampilkan distribusi tipe pelanggan (Individu vs Bisnis/Instansi).

1. **Add chart → Donut chart**
2. **Data source**: Master_Pelanggan
3. **Setup**:
   - **Dimension**: `jenis_pelanggan`
   - **Metric**: `COUNT(id_pelanggan)` → Label: "Customers"
4. **Style**:
   - **Colors**: 
     - Individu: #3B82F6 (biru)
     - Bisnis: #22C55E (hijau)
     - Instansi: #A855F7 (ungu)
   - **Donut hole**: 50%
   - **Show legend**: Bottom
   - **Show percentage**: ON
5. **Posisi**: Baris baru (x: 20, y: 600)
6. **Ukuran**: Width: 380px, Height: 280px

### 5.5 Source Channel Distribution

**Tujuan**: Menampilkan dari mana pelanggan pertama kali mengenal bisnis (acquisition channel).

1. **Add chart → Bar chart (horizontal)**
2. **Data source**: Master_Pelanggan
3. **Setup**:
   - **Dimension**: `sumber_awal` (atau `channel_akuisisi` jika ada)
   - **Metric**: `COUNT(id_pelanggan)` → Label: "Customers"
   - **Sort**: Descending (terbanyak di atas)
4. **Style**:
   - **Bar color**: #FB923C (orange)
   - **Show data labels**: ON
   - **Axis labels**: Clear
5. **Posisi**: Sebelah kanan Customer Type (x: 420, y: 600)
6. **Ukuran**: Width: 380px, Height: 280px

**Catatan**: Jika field `sumber_awal` tidak ada, gunakan `channel_penjualan` dari transaksi pertama customer (perlu blend dengan filter first transaction).

### 5.6 Top 20 Customers Table

**Tujuan**: Menampilkan 20 pelanggan terbaik berdasarkan total pembelian untuk VIP customer management.

1. **Add chart → Table**
2. **Data source**: Blend Master_Pelanggan + Transaksi_Penjualan
   - **Blend setup**:
     - Left: Master_Pelanggan (join key: `id_pelanggan`)
     - Right: Transaksi_Penjualan (join key: `id_pelanggan`)
     - Join type: Left Outer Join
3. **Setup Dimensions**:
   - `nama_lengkap` → Label: "Customer Name"
   - `kota` → Label: "City"
   - `jenis_pelanggan` → Label: "Type"
4. **Setup Metrics**:
   - `COUNT_DISTINCT(id_transaksi)` → Label: "Transactions"
   - `SUM(total_pembayaran)` → Label: "Total Spent", Format: Currency (IDR)
   - Calculated: `SUM(total_pembayaran) / COUNT_DISTINCT(id_transaksi)` → Label: "Avg Order", Format: Currency
   - (Optional) `AVG(rating_pelanggan)` → Label: "Avg Rating", Format: Number (1 decimal)
5. **Sort**: By "Total Spent" (Descending)
6. **Limit**: 20 rows
7. **Style**:
   - **Show row numbers**: ON (untuk ranking 1-20)
   - **Alternating rows**: ON
   - **Header**: Bold, Background #F3F4F6
   - **Conditional formatting** untuk Total Spent:
     - Green gradient untuk top performers
8. **Posisi**: Baris baru (x: 20, y: 900)
9. **Ukuran**: Width: 1160px, Height: 500px

**Tips**: Tambahkan badge/icon untuk VIP customers (> 5 transactions atau > Rp 2M total).

### 5.7 Customer Database Table

**Tujuan**: Menampilkan database pelanggan lengkap dengan fitur search dan filter untuk CRM.

1. **Add chart → Table**
2. **Data source**: Blend Master_Pelanggan + Transaksi_Penjualan (untuk metrics)
3. **Setup Dimensions**:
   - `nama_lengkap` → Label: "Name"
   - `email` → Label: "Email"
   - `no_telepon` → Label: "Phone"
   - `kota` → Label: "City"
   - `jenis_pelanggan` → Label: "Type"
4. **Setup Metrics**:
   - `COUNT_DISTINCT(id_transaksi)` → Label: "Transactions"
   - `SUM(jumlah_item)` → Label: "Items Purchased"
   - `SUM(total_pembayaran)` → Label: "Total Spent", Format: Currency
   - Calculated: `segmen` atau customer segment
5. **Sort**: By "Total Spent" (Descending) atau Alphabetical by Name
6. **Rows per page**: 25
7. **Style**:
   - **Alternating rows**: ON
   - **Show row numbers**: OFF
   - **Compact mode**: ON (untuk fit more data)
   - **Conditional formatting**:
     - Highlight VIP customers (different background color)
     - Color code by customer type

8. **Add Interactive Controls** (di atas table):

   **Control 1: Search Box**
   - **Add control → Text input**
   - **Control field**: `nama_lengkap`
   - **Placeholder**: "Search customer name..."
   - **Position**: Top-right (x: 900, y: 1420)
   - **Width**: 250px

   **Control 2: City Filter**
   - **Add control → Drop-down list**
   - **Control field**: `kota`
   - **Allow multiple selections**: YES
   - **Include "All" option**: YES
   - **Position**: Below search (x: 900, y: 1470)
   - **Width**: 250px

   **Control 3: Customer Type Filter**
   - **Add control → Drop-down list**
   - **Control field**: `jenis_pelanggan`
   - **Allow multiple selections**: YES
   - **Include "All" option**: YES
   - **Position**: Below city filter (x: 900, y: 1520)
   - **Width**: 250px

   **Control 4: Segment Filter** (Optional)
   - **Add control → Drop-down list**
   - **Control field**: `segmen`
   - **Position**: Below type filter
   - **Width**: 250px

9. **Posisi Table**: Baris baru (x: 20, y: 1420)
10. **Ukuran Table**: Width: 860px, Height: 600px

**Advanced Features**:
- **Export functionality**: Enable "Download as CSV" option
- **Drill-down**: Click customer name → navigate to customer detail page
- **Email integration**: Make email field clickable (mailto: link)
- **Phone integration**: Make phone clickable (tel: link)

**Tips untuk Performance**:
- Jika data > 1000 customers, gunakan pagination
- Consider adding date range filter untuk filter by last transaction date
- Add "Active customers only" toggle (transacted in last 6 months)

---

## 💰 Langkah 6: Membuat Financial Dashboard (Halaman 5)

### 6.1 Tambah Halaman Baru
1. Klik **"Page" → "New page"**
2. Rename: **"Financial Analysis"**
3. Copy header dari halaman 1

### 6.2 Buat Blend Data untuk Financial Analysis

**Tujuan**: Menggabungkan data dari Transaksi dan Produk untuk menghitung COGS (Cost of Goods Sold).

**Catatan**: Biaya Operasional akan diambil dari data source terpisah karena tidak bisa di-join dengan transaksi (berbeda granularity).

#### Step A: Buat Blend "Financial_Blend"

1. **Klik menu "Resource"** di toolbar atas
2. **Pilih "Manage added data sources"**
3. **Klik "+ ADD A DATA SOURCE"** (pojok kanan bawah)
4. **Pilih "BLEND DATA"** (ikon dengan 2 tabel yang overlap)

#### Step B: Configure Table 1 (Left) - Transaksi_Penjualan

1. **Klik "Add data source"**
2. **Pilih**: Transaksi_Penjualan
3. **Join key**: Pilih field **`id_produk`**
4. **Dimensions yang diambil**:
   - ✅ `tanggal_transaksi` (untuk grouping by month)
   - ✅ `id_transaksi` (untuk counting)
   - ✅ `channel_penjualan` (optional, untuk breakdown)
5. **Metrics yang diambil**:
   - ✅ `total_pembayaran` (SUM) → untuk Total Revenue
   - ✅ `subtotal` (SUM) → untuk Gross Sales
   - ✅ `diskon_nominal` (SUM) → untuk Total Discounts
   - ✅ `biaya_ongkir` (SUM) → untuk Shipping Revenue
   - ✅ `biaya_custom` (SUM) → untuk Custom Services
   - ✅ `jumlah_item` (SUM) → untuk calculate COGS

#### Step C: Configure Table 2 (Right) - Master_Produk

1. **Klik "Add another data source"**
2. **Pilih**: Master_Produk
3. **Join key**: Pilih field **`id_produk`** (harus sama dengan Table 1)
4. **Dimensions yang diambil**:
   - ✅ `kategori` (optional, untuk breakdown)
   - ✅ `nama_produk` (optional)
5. **Metrics yang diambil**:
   - ✅ `harga_modal` (untuk calculate COGS)
   - ✅ `harga_jual` (optional, untuk analysis)

#### Step D: Set Join Configuration

1. **Join operator**: **Left Outer Join** (default)
   - Artinya: Ambil semua transaksi, dan tambahkan info produk (harga_modal) jika ada

#### Step E: Rename dan Save Blend

1. **Klik nama blend** (biasanya "Blend 1")
2. **Rename menjadi**: **"Financial_Blend"**
3. **Klik "SAVE"** (pojok kanan atas)
4. **Klik "CLOSE"** untuk kembali ke report

**✅ Blend "Financial_Blend" siap digunakan!**

#### Tentang Biaya Operasional

**Kenapa tidak di-blend?**
- Biaya Operasional punya **granularity berbeda** (per bulan, bukan per transaksi)
- Tidak ada join key yang cocok dengan transaksi
- Lebih baik diambil dari **data source terpisah** (Biaya_Operasional)

**Cara menggunakan**:
- Untuk chart yang butuh COGS: Gunakan **Financial_Blend**
- Untuk chart yang butuh Operational Costs: Gunakan **Biaya_Operasional** (separate)
- Untuk Net Profit: Buat **calculated field** yang menggabungkan keduanya

---

### 6.3 Financial Overview KPIs (4 Cards)

**Data Source**: 
- **Card 1 & 2**: Blend "Financial_Blend" (Transaksi + Produk)
- **Card 3 & 4**: Perlu calculated field yang menggabungkan Financial_Blend + Biaya_Operasional

**Catatan**: Karena Biaya Operasional tidak bisa di-blend, kita akan gunakan **2 data sources** dalam calculated field.

#### Card 1: Total Revenue

**Tujuan**: Menampilkan total pendapatan dari semua transaksi.

1. **Add chart → Scorecard**
2. **Data source**: **Financial_Blend** (atau Transaksi_Penjualan)
3. **Setup Metric**:
   - **Field**: `total_pembayaran`
   - **Aggregation**: SUM
   - **Label**: "Total Revenue"
   - **Format**: Currency (IDR)
4. **Style**:
   - **Background**: #22C55E (hijau)
   - **Text color**: #FFFFFF
   - **Font size**: 32
   - **Compact numbers**: ON
5. **Posisi**: (x: 20, y: 100)
6. **Ukuran**: Width: 280px, Height: 140px

#### Card 2: Total Costs (COGS Only)

**Tujuan**: Menampilkan Cost of Goods Sold (harga_modal × jumlah_item).

⚠️ **Catatan**: Card ini hanya menampilkan COGS, belum termasuk Operational Costs.

1. **Duplicate Card 1**
2. **Data source**: **Financial_Blend**
3. **Setup Metric**: Calculated field `COGS`
   - **Klik "Add metric" → "CREATE FIELD"**
   - **Field Name**: `COGS`
   - **Formula**:
     ```
     SUM(harga_modal * jumlah_item)
     ```
   - **Klik "SAVE"** → **Klik "DONE"**
   - **Label**: "Total COGS"
   - **Format**: Currency (IDR)
4. **Style**: Background #3B82F6 (biru)
5. **Add Secondary Text**: "Cost of Goods Sold"
6. **Posisi**: (x: 320, y: 100)

**Catatan**: Untuk menampilkan Total Costs (COGS + Operational), perlu aggregate manual dari 2 sources yang berbeda. Lebih mudah lihat di chart Revenue vs Profit Trend.

#### Card 3: Gross Profit

**Tujuan**: Menampilkan profit sebelum operational costs (Revenue - COGS).

1. **Duplicate Card 2**
2. **Data source**: **Financial_Blend**
3. **Setup Metric**: Calculated field `Gross_Profit`
   - **Field Name**: `Gross_Profit`
   - **Formula**:
     ```
     SUM(total_pembayaran) - SUM(harga_modal * jumlah_item)
     ```
   - **Label**: "Gross Profit"
   - **Format**: Currency (IDR)
4. **Style**: Background #A855F7 (ungu)
5. **Add Secondary Metric** (Gross Margin):
   - **Formula** (TANPA * 100):
     ```
     (SUM(total_pembayaran) - SUM(harga_modal * jumlah_item)) / SUM(total_pembayaran)
     ```
   - **Data type**: Percent
   - **Label**: "margin"
6. **Posisi**: (x: 620, y: 100)

#### Card 4: Operational Costs

**Tujuan**: Menampilkan total biaya operasional.

1. **Add chart → Scorecard** (buat baru, jangan duplicate)
2. **Data source**: **Biaya_Operasional** (data source terpisah)
3. **Setup Metric**:
   - **Field**: `nominal`
   - **Aggregation**: SUM
   - **Label**: "Operational Costs"
   - **Format**: Currency (IDR)
4. **Style**: Background #FB923C (orange)
5. **Add Secondary Text**: "Excluding COGS"
6. **Posisi**: (x: 920, y: 100)

**💡 Catatan Penting**:
- Card 1-3 menggunakan **Financial_Blend** (Transaksi + Produk)
- Card 4 menggunakan **Biaya_Operasional** (data source terpisah)
- Untuk Net Profit lengkap, lihat di chart Revenue vs Profit Trend yang menggabungkan keduanya

### 6.4 Revenue vs Profit Trend

**Tujuan**: Menampilkan tren revenue dan gross profit (tanpa operational costs karena sulit di-blend).

⚠️ **Catatan**: Chart ini hanya menampilkan Revenue dan Gross Profit (Revenue - COGS). Operational Costs tidak bisa ditampilkan di chart yang sama karena berbeda granularity.

1. **Add chart → Time series chart** (atau Combo chart)
2. **Data source**: **Financial_Blend** (Transaksi + Produk)
3. **Setup Dimension**:
   - **Field**: `tanggal_transaksi`
   - **Type**: Date
   - **Granularity**: Month
4. **Setup Metrics**:

   **Metric 1 - Revenue**:
   - **Field**: `total_pembayaran`
   - **Aggregation**: SUM
   - **Label**: "Revenue"
   - **Chart type**: Line
   - **Color**: #22C55E (hijau)
   - **Axis**: Left (primary)
   
   **Metric 2 - COGS**:
   - **Calculated field**: `COGS`
   - **Formula**:
     ```
     SUM(harga_modal * jumlah_item)
     ```
   - **Label**: "Cost of Goods Sold"
   - **Chart type**: Line
   - **Color**: #EF4444 (merah)
   - **Axis**: Left (primary)
   
   **Metric 3 - Gross Profit**:
   - **Calculated field**: `Gross_Profit`
   - **Formula**:
     ```
     SUM(total_pembayaran) - SUM(harga_modal * jumlah_item)
     ```
   - **Label**: "Gross Profit"
   - **Chart type**: Line (atau Area)
   - **Color**: #3B82F6 (biru)
   - **Axis**: Left (primary)

5. **Style**:
   - **Line thickness**: 2-3
   - **Show data points**: ON
   - **Legend**: Bottom
   - **Grid lines**: ON
   - **Smooth lines**: ON (tension 0.4)

6. **Posisi**: Sebelah kiri (x: 20, y: 260)
7. **Ukuran**: Width: 560px, Height: 320px

**💡 Tentang Operational Costs**:

Operational Costs **tidak bisa ditampilkan** di chart ini karena:
- Data dari tabel berbeda (Biaya_Operasional)
- Granularity berbeda (per bulan, bukan per transaksi)
- Looker Studio tidak support blend 3 tabel dengan mudah

**Solusi**:
- Lihat Operational Costs di chart terpisah (section 6.6)
- Atau buat calculated field manual untuk Net Profit (lihat section 6.5)

**Alternatif - Tampilkan Net Profit dengan Calculated Field**:

Jika ingin menampilkan Net Profit (termasuk operational costs), buat calculated field:

```
SUM(total_pembayaran) - SUM(harga_modal * jumlah_item) - 
(SELECT SUM(nominal) FROM Biaya_Operasional WHERE MONTH(tanggal) = MONTH(tanggal_transaksi))
```

⚠️ **Warning**: Formula di atas **tidak akan work** di Looker Studio karena tidak support subquery. Untuk Net Profit lengkap, gunakan 2 charts terpisah atau pre-calculate di Google Sheets.

### 6.5 Gross Profit Margin Trend

**Tujuan**: Menampilkan tren gross profit margin (%) untuk monitor efisiensi bisnis.

⚠️ **Catatan**: Ini adalah **Gross Profit Margin** (tidak termasuk operational costs).

1. **Add chart → Time series chart** (atau Line chart)
2. **Data source**: **Financial_Blend**
3. **Setup**:
   - **Dimension**: `tanggal_transaksi`
   - **Date granularity**: Month
   - **Metric**: Calculated field `Gross_Profit_Margin`
     - **Formula** (⚠️ TANPA * 100):
       ```
       (SUM(total_pembayaran) - SUM(harga_modal * jumlah_item)) / SUM(total_pembayaran)
       ```
     - **Data type**: **Percent** (Looker Studio akan otomatis × 100)
     - **Format**: Percent dengan 1 decimal
4. **Style**:
   - **Line color**: #A855F7 (ungu)
   - **Line thickness**: 3
   - **Fill area**: ON (opacity 20%)
   - **Show data points**: ON
   - **Reference line** (optional): Add horizontal line at 0.40 (40% target margin)
5. **Posisi**: Sebelah kanan Revenue vs Profit (x: 620, y: 260)
6. **Ukuran**: Width: 560px, Height: 320px

**Tips Conditional Formatting**:
- Jika ingin warna berbeda berdasarkan nilai, gunakan **Conditional formatting** di Style tab
- Green if margin > 0.40 (40%)
- Orange if margin 0.30-0.40 (30-40%)
- Red if margin < 0.30 (< 30%)

**Catatan**: 
- Ingat, jangan pakai * 100 jika Data type = Percent!
- Ini adalah Gross Margin (sebelum operational costs)
- Untuk Net Margin (setelah operational costs), perlu pre-calculate di Google Sheets

### 6.6 Operational Costs Breakdown

**Tujuan**: Menampilkan komposisi biaya operasional per kategori.

1. **Add chart → Pie chart** (atau Donut chart)
2. **Data source**: Biaya_Operasional
3. **Setup**:
   - **Dimension**: `kategori_biaya`
   - **Metric**: `SUM(nominal)` → Label: "Amount"
   - **Format**: Currency (IDR)
4. **Style**:
   - **Colors**: Custom per kategori
     - Gaji & Upah: #3B82F6 (biru)
     - Sewa & Utilitas: #FB923C (orange)
     - Marketing: #A855F7 (ungu)
     - Operasional: #22C55E (hijau)
     - Lainnya: #9CA3AF (abu-abu)
   - **Show legend**: Bottom
   - **Show percentage**: ON
   - **Show values**: ON
5. **Posisi**: Baris baru (x: 20, y: 600)
6. **Ukuran**: Width: 560px, Height: 320px

### 6.7 Revenue Composition

**Tujuan**: Menampilkan breakdown revenue dari berbagai sumber (product sales, shipping, custom services).

1. **Add chart → Stacked bar chart** (atau Stacked column chart)
2. **Data source**: Transaksi_Penjualan
3. **Setup**:
   - **Dimension**: `MONTH(tanggal_transaksi)`
   - **Breakdown dimension**: Revenue Type (perlu calculated field)
   - **Metrics**:
     - **Product Sales**: `SUM(subtotal - diskon_nominal)`
     - **Shipping**: `SUM(biaya_ongkir)`
     - **Custom Services**: `SUM(biaya_custom)`

4. **Setup Metrics** (Multiple Metrics untuk Stacked Chart):

   **Metric 1 - Product Sales**:
   - **Calculated field**: `Product_Sales`
   - **Formula**:
     ```
     SUM(subtotal - diskon_nominal)
     ```
   - **Label**: "Product Sales"
   - **Color**: #22C55E (hijau)
   
   **Metric 2 - Shipping Revenue**:
   - **Field**: `biaya_ongkir`
   - **Aggregation**: SUM
   - **Label**: "Shipping"
   - **Color**: #3B82F6 (biru)
   
   **Metric 3 - Custom Services**:
   - **Field**: `biaya_custom`
   - **Aggregation**: SUM
   - **Label**: "Custom Services"
   - **Color**: #A855F7 (ungu)

5. **Style**:
   - **Chart type**: Stacked bar (atau Stacked area)
   - **Stack type**: Normal (atau 100% untuk percentage view)
   - **Show data labels**: ON
   - **Legend**: Bottom
   - **Grid lines**: ON

6. **Posisi**: Sebelah kanan Costs Breakdown (x: 620, y: 600)
7. **Ukuran**: Width: 560px, Height: 320px

**💡 Tips**:
- Untuk melihat **percentage composition**, ubah Stack type ke **"100%"** di Style tab
- Untuk melihat **absolute values**, gunakan Stack type **"Normal"**
- Semua metrics akan otomatis ter-stack dalam 1 bar per bulan

### 6.8 Expense Details Table

**Tujuan**: Menampilkan detail semua pengeluaran operasional dengan fitur filter.

1. **Add chart → Table**
2. **Data source**: Biaya_Operasional
3. **Setup Dimensions**:
   - `tanggal` → Label: "Date", Format: Date (DD/MM/YYYY)
   - `kategori_biaya` → Label: "Category"
   - `sub_kategori` → Label: "Sub-Category" (jika ada)
   - `deskripsi` → Label: "Description"
4. **Setup Metrics**:
   - `nominal` → Label: "Amount", Format: Currency (IDR)
5. **Sort**: By `tanggal` (Descending) - terbaru di atas
6. **Rows per page**: 25
7. **Style**:
   - **Alternating rows**: ON
   - **Show row numbers**: OFF
   - **Conditional formatting**:
     - Highlight large expenses (> Rp 5M) dengan background kuning
     - Color code by category

8. **Add Filter Controls** (di atas table):

   **Control 1: Month Filter**
   - **Add control → Date range control**
   - **Control field**: `tanggal`
   - **Default**: Last 3 months
   - **Position**: Top-right (x: 900, y: 940)

   **Control 2: Category Filter**
   - **Add control → Drop-down list**
   - **Control field**: `kategori_biaya`
   - **Allow multiple**: YES
   - **Position**: Below month filter (x: 900, y: 990)

9. **Add Summary Row** (di bawah table):
   - **Text box**: "Total Expenses: "
   - **Scorecard**: `SUM(nominal)` dengan filter yang sama
   - **Format**: Currency (IDR), Bold, Large font

10. **Posisi Table**: Baris baru (x: 20, y: 940)
11. **Ukuran Table**: Width: 860px, Height: 500px

**Advanced Features**:
- **Export to CSV**: Enable download option
- **Drill-down**: Click category → filter to that category
- **Add notes column**: For expense justification/approval status

### 6.9 Tambahkan Filter Controls

**Tujuan**: Memberikan interaktivitas untuk filter data financial.

#### Filter 1: Date Range Control

1. **Add a control → Date range control**
2. **Setup**:
   - **Data source**: Transaksi_Penjualan (atau Financial_Blend)
   - **Control field**: `tanggal_transaksi`
   - **Default**: Last 12 months
3. **Style**: Compact, Accent color: #22C55E
4. **Posisi**: Top-right (x: 1000, y: 20)
5. **Ukuran**: Width: 180px, Height: 40px

#### Filter 2: Expense Category Filter (untuk Expense Table)

1. **Add a control → Drop-down list**
2. **Setup**:
   - **Data source**: Biaya_Operasional
   - **Control field**: `kategori_biaya`
   - **Allow multiple**: YES
   - **Include "All"**: YES
3. **Posisi**: Below date range (x: 1000, y: 70)
4. **Ukuran**: Width: 180px, Height: 40px

### 🎯 Checklist: Financial Dashboard Selesai

- [ ] **Header & Title** "Financial Analysis"
- [ ] **4 KPI Cards** (Revenue, COGS, Gross Profit, Operational Costs)
- [ ] **Blend "Financial_Blend"** sudah dibuat (Transaksi + Produk)
- [ ] **Revenue vs Profit Trend** (3 lines: Revenue, COGS, Gross Profit)
- [ ] **Gross Profit Margin Trend** (line chart)
- [ ] **Operational Costs Breakdown** (pie chart)
- [ ] **Revenue Composition** (stacked bar dengan 3 metrics)
- [ ] **Expense Details Table** dengan filter
- [ ] **2 Filter Controls** (Date Range, Category)
- [ ] **All formulas** menggunakan blend (tidak ada sheet tambahan)
- [ ] **Profit margin formula** TANPA * 100

### 💡 Tips Sebelum Lanjut ke Halaman 6

1. **Verify blend**: Pastikan Financial_Blend bekerja dengan baik
2. **Check COGS calculation**: Pastikan harga_modal × jumlah_item benar
3. **Test filters**: Pastikan date range mempengaruhi semua charts
4. **Note limitation**: User tahu bahwa Net Profit lengkap tidak bisa ditampilkan karena keterbatasan blend

---

## 📦 Langkah 7: Membuat Operations & Inventory Dashboard (Halaman 6)

### 7.1 Tambah Halaman Baru
1. Klik **"Page" → "New page"**
2. Rename: **"Operations & Inventory"**
3. Copy header dari halaman 1

### 7.2 Operations Overview KPIs (4 Cards)

#### Card 1: Total Stock In
- **Data source**: Riwayat_Stok
- **Metric**: `SUM(stok_masuk)`
- **Background**: #22C55E (hijau)
- **Label**: "Units received"
- **Position**: Top left

#### Card 2: Total Stock Out
- **Data source**: Riwayat_Stok
- **Metric**: `SUM(stok_keluar)`
- **Background**: #3B82F6 (biru)
- **Label**: "Units sold/used"
- **Position**: Top center-left

#### Card 3: Stock Turnover Rate
- **Data source**: Riwayat_Stok
- **Calculated field**:
  ```
  SUM(stok_keluar) / AVG(stok_akhir)
  ```
- **Format**: Number (2 decimals)
- **Background**: #A855F7 (ungu)
- **Label**: "Times per period"
- **Position**: Top center-right

#### Card 4: Net Stock Change
- **Data source**: Riwayat_Stok
- **Calculated field**:
  ```
  SUM(stok_masuk) - SUM(stok_keluar)
  ```
- **Format**: Number (0 decimals)
- **Background**: #FB923C (orange)
- **Label**: "Net inventory change"
- **Position**: Top right

### 7.3 Stock Movement Trend Chart

1. **Add chart → Time series chart**
2. **Data source**: Riwayat_Stok
3. **Date dimension**: `tanggal`
4. **Metrics** (multiple lines):
   - Stock In: `SUM(stok_masuk)`
   - Stock Out: `SUM(stok_keluar)`
5. **Style**:
   - Stock In line: Green (#22C55E)
   - Stock Out line: Red (#EF4444)
   - Show data points: ON
   - Fill area: ON (opacity 20%)
6. **Position**: Below KPI cards, left side

### 7.4 Transaction Type Distribution

1. **Add chart → Donut chart**
2. **Data source**: Riwayat_Stok
3. **Dimension**: `jenis_transaksi`
4. **Metric**: `Record Count`
5. **Style**:
   - Colors:
     - Penjualan: #EF4444 (merah)
     - Pembelian: #22C55E (hijau)
6. **Position**: Below KPI cards, right side

### 7.5 Stock Level by Category

**Langkah 1: Buat Blend**
1. Klik **"Resource" → "Manage added data sources"**
2. Klik **"+ Add a data source" → "Blend data"**
3. **Left table (Table 1)**:
   - Data source: **Riwayat_Stok**
   - Join key: **id_produk**
   - Metrics to include:
     - ✅ `stok_akhir`
4. **Right table (Table 2)**:
   - Data source: **Master_Produk**
   - Join key: **id_produk**
   - Dimensions to include:
     - ✅ `kategori`
     - ✅ `nama_produk`
5. **Join configuration**:
   - Join type: **Left outer join**
6. Klik **"Save"**
7. Rename blend: **"Blend_Stock_Category"**

**Langkah 2: Buat Chart**
1. Klik **"Add a chart"** di toolbar atas
2. Pilih **"Bar chart"**
3. Chart akan muncul di canvas

**Langkah 3: Setup Data**
1. Di panel kanan, bagian **"Data"** tab:
2. **Data source**: 
   - Klik dropdown
   - Pilih **"Blend_Stock_Category"** (blend yang baru dibuat)
3. **Dimension**:
   - Klik "Add dimension"
   - Pilih **"kategori"** (ada label "Master_Produk" di sampingnya)
4. **Metric**:
   - Hapus metric default jika ada
   - Klik "Add metric"
   - Pilih **"stok_akhir"** (ada label "Riwayat_Stok" di sampingnya)
   - Klik dropdown aggregation → pilih **"AVG"**
5. **Sort**:
   - Klik dropdown sort
   - Pilih metric **"AVG stok_akhir"**
   - Order: **Descending** (panah ke bawah)

**Langkah 4: Setup Style**
1. Klik tab **"Style"** di panel kanan
2. **Bar chart**:
   - Orientation: Pilih **"Horizontal"** (bar dari kiri ke kanan)
3. **Color**:
   - Klik color picker
   - Masukkan: **#3B82F6**
4. **Data labels**:
   - Toggle **"Show data labels"** → **ON**
5. **Chart header**:
   - Title: **"Average Stock Level by Category"**

**Langkah 5: Posisi & Ukuran**
1. Drag chart ke posisi: **Middle section, left side**
2. Resize: Lebar sekitar 45% halaman, tinggi 300-350px

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

**Langkah 1: Buat Blend (jika belum ada dari 7.5)**
1. Klik **"Resource" → "Manage added data sources"**
2. Klik **"+ Add a data source" → "Blend data"**
3. **Left table (Table 1)**:
   - Data source: **Riwayat_Stok**
   - Join key: **id_produk**
   - Dimensions to include:
     - ✅ `tanggal`
     - ✅ `jenis_transaksi`
     - ✅ `keterangan`
   - Metrics to include:
     - ✅ `stok_masuk`
     - ✅ `stok_keluar`
     - ✅ `stok_akhir`
4. **Right table (Table 2)**:
   - Data source: **Master_Produk**
   - Join key: **id_produk**
   - Dimensions to include:
     - ✅ `nama_produk`
5. **Join configuration**:
   - Join type: **Left outer join**
6. Klik **"Save"**
7. Rename blend: **"Blend_Stock_History"**

**Langkah 2: Buat Table**
1. Klik **"Add a chart"** di toolbar atas
2. Pilih **"Table"**
3. Table akan muncul di canvas

**Langkah 3: Setup Data**
1. Di panel kanan, bagian **"Data"** tab:
2. **Data source**: 
   - Klik dropdown
   - Pilih **"Blend_Stock_History"** (blend yang baru dibuat)
3. **Dimensions** (tambahkan satu per satu, urutan penting):
   - Klik "Add dimension" → Pilih **"tanggal"** (dari Riwayat_Stok)
   - Klik "Add dimension" → Pilih **"nama_produk"** (dari Master_Produk)
   - Klik "Add dimension" → Pilih **"jenis_transaksi"** (dari Riwayat_Stok)
   - Klik "Add dimension" → Pilih **"keterangan"** (dari Riwayat_Stok)
4. **Metrics** (tambahkan satu per satu):
   - Klik "Add metric" → Pilih **"stok_masuk"**
   - Klik "Add metric" → Pilih **"stok_keluar"**
   - Klik "Add metric" → Pilih **"stok_akhir"**
5. **Sort**:
   - Klik dropdown sort
   - Pilih dimension **"tanggal"**
   - Order: **Descending** (panah ke bawah)
6. **Rows per page**:
   - Scroll ke bawah di panel Data
   - Set **"Rows per page"** = **50**

**Langkah 4: Setup Style**
1. Klik tab **"Style"** di panel kanan
2. **Table header**:
   - Background color: **#1E293B** (dark gray)
   - Text color: **#FFFFFF** (white)
3. **Table body**:
   - Toggle **"Alternating row colors"** → **ON**
4. **Table title**:
   - Title: **"Stock Movement History"**

**Langkah 5: Posisi & Ukuran**
1. Drag table ke posisi: **Bottom section**
2. Resize: **Full width** (hampir selebar halaman), tinggi 400-450px

### 7.8 Additional Stock Metrics (Optional)

1. **Add chart → Scorecard**
2. **Data source**: Riwayat_Stok
3. **Metrics**:
   - **Average Stock Level**: 
     ```
     AVG(stok_akhir)
     ```
   - **Total Transactions**:
     ```
     Record Count
     ```
   - **Stock Turnover Days**:
     ```
     AVG(stok_akhir) / (SUM(stok_keluar) / 30)
     ```
     Format: Number (1 decimal)
4. **Position**: Middle section, right side

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

