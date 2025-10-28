# LAMPIRAN

---

## DAFTAR LAMPIRAN

- **Lampiran A:** Sample Dataset
  - A.1. Master Produk (Sample 10 produk)
  - A.2. Master Pelanggan (Sample 10 pelanggan)
  - A.3. Transaksi Penjualan (Sample 20 transaksi)
  - A.4. Riwayat Stok (Sample 10 records)
  - A.5. Biaya Operasional (Sample 10 records)
  - A.6. Marketing Campaign (Sample 5 campaigns)

- **Lampiran B:** Screenshot Dashboard
  - B.1. Executive Summary Page
  - B.2. Sales Analysis Page
  - B.3. Product Performance Page
  - B.4. Customer Analysis Page
  - B.5. Operational Metrics Page
  - B.6. Financial Analysis Page
  - B.7. Marketing Performance Page

- **Lampiran C:** Dokumentasi Teknis
  - C.1. Data Dictionary
  - C.2. Calculated Fields & Formulas
  - C.3. Dashboard Configuration

- **Lampiran D:** Surat Keterangan Riset
  - D.1. Surat Keterangan dari SATRIAMART

---

## LAMPIRAN A: SAMPLE DATASET

### A.1. Master Produk (Sample 10 dari 50 produk)

| ID | Nama Produk | Kategori | Ukuran | Harga Jual | Harga Modal | Stok | Status |
|----|-------------|----------|---------|------------|-------------|------|--------|
| P001 | Nomor Rumah Akrilik Modern 1-2 Digit | Nomor Rumah | 15x20cm | Rp 85.000 | Rp 45.000 | 25 | Aktif |
| P002 | Nomor Rumah Akrilik Minimalis 3-4 Digit | Nomor Rumah | 20x30cm | Rp 125.000 | Rp 68.000 | 18 | Aktif |
| P003 | Signage Akrilik + LED "OPEN/CLOSED" | Signage | 30x40cm | Rp 350.000 | Rp 195.000 | 12 | Aktif |
| P004 | Papan Nama Toko Akrilik + Cutting | Papan Nama | 40x60cm | Rp 450.000 | Rp 245.000 | 8 | Aktif |
| P005 | Plakat Akrilik Trophy | Aksesoris | 15x20cm | Rp 175.000 | Rp 95.000 | 15 | Aktif |
| P006 | Display Menu Akrilik + Stand | Aksesoris | 20x30cm | Rp 95.000 | Rp 52.000 | 22 | Aktif |
| P007 | Partisi Meja Akrilik Transparant | Aksesoris | 60x40cm | Rp 185.000 | Rp 98.000 | 10 | Aktif |
| P008 | Rak Display Akrilik 3 Tingkat | Aksesoris | 30x30x40cm | Rp 275.000 | Rp 145.000 | 6 | Aktif |
| P009 | Photo Frame Akrilik Magnetic | Aksesoris | 15x20cm | Rp 65.000 | Rp 35.000 | 30 | Aktif |
| P010 | Name Plate Desk Akrilik Custom | Papan Nama | 10x20cm | Rp 55.000 | Rp 28.000 | 40 | Aktif |

**Keterangan:**
- Total produk dalam database: 50 items
- Kategori: Nomor Rumah (30%), Signage (20%), Papan Nama (20%), Aksesoris (30%)
- Rentang harga: Rp 35.000 - Rp 750.000
- Material: Akrilik 3mm, 5mm, 8mm
- Finishing: Glossy, Matte, Mirror

---

### A.2. Master Pelanggan (Sample 10 dari 180 pelanggan)

| ID | Nama Lengkap | Kota | Jenis Pelanggan | Total Transaksi | Total Nilai | Status |
|----|--------------|------|-----------------|-----------------|-------------|--------|
| C001 | Ahmad Dewi | Bogor | Individu | 2 | Rp 1.207.216 | Aktif |
| C002 | Siti Rahman | Jakarta Selatan | Bisnis | 5 | Rp 3.450.000 | Aktif |
| C003 | Budi Santoso | Depok | Individu | 1 | Rp 285.000 | Aktif |
| C004 | Rina Wulandari | Tangerang | Reseller | 8 | Rp 5.680.000 | Aktif |
| C005 | Agus Pratama | Jakarta Barat | Bisnis | 3 | Rp 1.950.000 | Aktif |
| C006 | Dewi Lestari | Bekasi | Individu | 1 | Rp 175.000 | Aktif |
| C007 | Rudi Hartono | Depok | Individu | 2 | Rp 540.000 | Aktif |
| C008 | Maya Kusuma | Jakarta Selatan | Bisnis | 4 | Rp 2.780.000 | Aktif |
| C009 | Andi Wijaya | Bandung | Reseller | 6 | Rp 4.250.000 | Aktif |
| C010 | Linda Permata | Depok | Individu | 1 | Rp 95.000 | Aktif |

**Keterangan:**
- Total pelanggan: 180 customers
- Distribusi jenis: Individu (60%), Bisnis (30%), Reseller (10%)
- Geographic: 85% Jabodetabek, 15% luar Jabodetabek
- Repeat customer rate: 15%
- Customer Lifetime Value rata-rata: Rp 622.092

---

### A.3. Transaksi Penjualan (Sample 20 dari 320 transaksi)

| ID Transaksi | Tanggal | Pelanggan | Produk | Qty | Subtotal | Total Bayar | Channel | Status |
|--------------|---------|-----------|--------|-----|----------|-------------|---------|--------|
| TRX0001 | 2024-11-23 | C138 | P015 | 1 | Rp 205.000 | Rp 199.000 | WhatsApp | Selesai |
| TRX0002 | 2024-11-15 | C045 | P032 | 2 | Rp 310.000 | Rp 345.000 | Instagram | Selesai |
| TRX0003 | 2024-11-28 | C092 | P008 | 1 | Rp 275.000 | Rp 290.000 | Website | Selesai |
| TRX0004 | 2024-12-05 | C167 | P001 | 3 | Rp 255.000 | Rp 280.000 | WhatsApp | Selesai |
| TRX0005 | 2024-12-12 | C023 | P045 | 1 | Rp 680.000 | Rp 715.000 | Instagram | Selesai |
| TRX0006 | 2024-12-20 | C134 | P012 | 2 | Rp 450.000 | Rp 465.000 | Offline | Selesai |
| TRX0007 | 2025-01-08 | C078 | P027 | 1 | Rp 350.000 | Rp 365.000 | WhatsApp | Selesai |
| TRX0008 | 2025-01-15 | C156 | P039 | 4 | Rp 540.000 | Rp 590.000 | Instagram | Selesai |
| TRX0009 | 2025-01-22 | C089 | P006 | 2 | Rp 190.000 | Rp 205.000 | Website | Selesai |
| TRX0010 | 2025-02-03 | C145 | P021 | 1 | Rp 295.000 | Rp 320.000 | WhatsApp | Selesai |
| TRX0011 | 2025-02-14 | C067 | P033 | 3 | Rp 615.000 | Rp 645.000 | Instagram | Selesai |
| TRX0012 | 2025-02-28 | C112 | P049 | 1 | Rp 125.000 | Rp 140.000 | WhatsApp | Selesai |
| TRX0013 | 2025-03-10 | C034 | P018 | 2 | Rp 370.000 | Rp 400.000 | Offline | Selesai |
| TRX0014 | 2025-03-18 | C178 | P005 | 1 | Rp 175.000 | Rp 190.000 | Instagram | Selesai |
| TRX0015 | 2025-03-25 | C098 | P042 | 3 | Rp 585.000 | Rp 610.000 | WhatsApp | Selesai |
| TRX0016 | 2025-04-05 | C123 | P030 | 1 | Rp 225.000 | Rp 250.000 | Website | Selesai |
| TRX0017 | 2025-04-12 | C056 | P014 | 2 | Rp 410.000 | Rp 435.000 | WhatsApp | Selesai |
| TRX0018 | 2025-04-20 | C167 | P025 | 1 | Rp 165.000 | Rp 180.000 | Instagram | Selesai |
| TRX0019 | 2025-05-02 | C089 | P037 | 4 | Rp 720.000 | Rp 770.000 | WhatsApp | Selesai |
| TRX0020 | 2025-05-15 | C145 | P009 | 2 | Rp 130.000 | Rp 145.000 | Instagram | Selesai |

**Keterangan:**
- Total transaksi: 320 orders
- Periode: November 2024 - Oktober 2025 (12 bulan)
- Total revenue: Rp 111.976.550
- Average Order Value: Rp 349.926
- Completion rate: 85%
- Channel distribution: WhatsApp (45%), Instagram (30%), Website (15%), Offline (10%)

---

### A.4. Riwayat Stok (Sample 10 dari 600 records)

| ID | Tanggal | Produk | Stok Awal | Masuk | Keluar | Stok Akhir | Transaksi |
|----|---------|--------|-----------|-------|--------|------------|-----------|
| STK0001 | 2025-01-01 | P001 | 35 | 0 | 1 | 34 | Penjualan |
| STK0002 | 2025-01-01 | P002 | 28 | 0 | 0 | 28 | - |
| STK0003 | 2025-01-05 | P001 | 34 | 10 | 0 | 44 | Pembelian |
| STK0004 | 2025-01-08 | P003 | 15 | 0 | 1 | 14 | Penjualan |
| STK0005 | 2025-01-12 | P004 | 10 | 0 | 1 | 9 | Penjualan |
| STK0006 | 2025-01-15 | P005 | 20 | 5 | 0 | 25 | Pembelian |
| STK0007 | 2025-01-18 | P001 | 44 | 0 | 2 | 42 | Penjualan |
| STK0008 | 2025-01-22 | P006 | 25 | 0 | 1 | 24 | Penjualan |
| STK0009 | 2025-01-25 | P007 | 12 | 0 | 1 | 11 | Penjualan |
| STK0010 | 2025-01-28 | P008 | 8 | 3 | 0 | 11 | Pembelian |

**Keterangan:**
- Total records: 600 (50 produk × 12 bulan)
- Tracking: Stok masuk, keluar, adjustment
- Stock turnover rate rata-rata: 3.2x per tahun

---

### A.5. Biaya Operasional (Sample 10 dari 348 records)

| ID | Tanggal | Kategori | Sub-Kategori | Nominal | Keterangan |
|----|---------|----------|--------------|---------|------------|
| BYA0001 | 2025-01-23 | Bahan Baku | LED Strip | Rp 206.912 | Pembelian LED strip |
| BYA0002 | 2025-01-15 | Bahan Baku | Akrilik Sheet | Rp 1.850.000 | Pembelian akrilik 5mm |
| BYA0003 | 2025-01-08 | Marketing | Instagram Ads | Rp 500.000 | Campaign Januari |
| BYA0004 | 2025-01-20 | Operasional | Listrik | Rp 450.000 | Tagihan listrik workshop |
| BYA0005 | 2025-01-25 | Transportasi | Bensin | Rp 300.000 | Delivery orders |
| BYA0006 | 2025-02-05 | Bahan Baku | Cutting Tools | Rp 780.000 | Pisau cutting laser |
| BYA0007 | 2025-02-12 | Marketing | Google Ads | Rp 850.000 | Campaign Februari |
| BYA0008 | 2025-02-18 | Operasional | Sewa Tempat | Rp 2.500.000 | Sewa workshop bulanan |
| BYA0009 | 2025-02-25 | Utilitas | Internet | Rp 350.000 | Tagihan internet |
| BYA0010 | 2025-03-02 | Bahan Baku | Lem Akrilik | Rp 185.000 | Pembelian lem |

**Keterangan:**
- Total records: 348 (12 bulan × ~29 entries/bulan)
- Kategori: Bahan Baku (45%), Marketing (18%), Operasional (22%), Transportasi (10%), Utilitas (5%)
- Total biaya bulanan rata-rata: Rp 5.200.000

---

### A.6. Marketing Campaign (Sample 5 dari 24 campaigns)

| ID | Nama Campaign | Platform | Periode | Budget | Reach | Conversion | Revenue | ROI |
|----|---------------|----------|---------|--------|-------|------------|---------|-----|
| CMP001 | Promo Tahun Baru | Google Ads | 01-13 Jan 2025 | Rp 1.850.135 | 118M | 852K | Rp 368B | 19914% |
| CMP002 | Valentine Special | Instagram | 01-14 Feb 2025 | Rp 1.500.000 | 85M | 520K | Rp 185M | 12333% |
| CMP003 | Ramadan Promo | Facebook | 01-15 Mar 2025 | Rp 2.200.000 | 145M | 680K | Rp 425M | 19318% |
| CMP004 | Lebaran Sale | Instagram | 20-30 Apr 2025 | Rp 1.800.000 | 95M | 450K | Rp 220M | 12222% |
| CMP005 | Mid Year Sale | Google Ads | 15-30 Jun 2025 | Rp 2.500.000 | 165M | 850K | Rp 520M | 20800% |

**Keterangan:**
- Total campaigns: 24 (2 per bulan)
- Platform: Google Ads (40%), Instagram (35%), Facebook (25%)
- Average ROI: 250-400%
- Total marketing budget: Rp 45.000.000 (12 bulan)

---

## LAMPIRAN B: SCREENSHOT DASHBOARD

### B.1. Executive Summary Page

**[INSERT SCREENSHOT HERE]**

**Deskripsi:**
Halaman Executive Summary menampilkan overview performa bisnis dengan 6 KPI scorecard utama, tren revenue 12 bulan, breakdown revenue by channel, dan revenue by category.

**Komponen:**
- Header: Logo SATRIAMART + Judul Dashboard
- Date Range Control: Filter periode data
- 6 KPI Cards: Total Revenue, Growth Rate, Total Transaksi, Total Pelanggan, AOV, Profit Margin
- Line Chart: Revenue Trend (12 months)
- Bar Chart: Revenue by Channel (4 channels)
- Donut Chart: Revenue by Category (4 categories)

**Insight Utama:**
- Total revenue Rp 111.976.550
- Growth rate 12,4%
- WhatsApp channel dominan (45%)
- Kategori Nomor Rumah terlaris (45%)

---

### B.2. Sales Analysis Page

**[INSERT SCREENSHOT HERE]**

**Deskripsi:**
Halaman Sales Analysis untuk deep dive analisis pola penjualan berdasarkan waktu, produk, dan karakteristik transaksi.

**Komponen:**
- Time Series: Daily/Weekly/Monthly Sales Trend
- Bar Chart: Top 10 Products by Revenue
- Bar Chart: Top 10 Products by Quantity
- Heatmap: Sales by Day of Week & Hour
- Table: Recent Transaction Details

**Insight Utama:**
- Peak hours: 10:00-14:00 dan 19:00-21:00
- Weekend sales: 35% dari total
- Top product: Nomor Rumah Akrilik Modern

---

### B.3. Product Performance Page

**[INSERT SCREENSHOT HERE]**

**Deskripsi:**
Analisis performa produk per kategori, profit margin, dan inventory turnover.

**Komponen:**
- Scorecard: Total Active Products
- Bar Chart: Revenue per Category
- Scatter Plot: Price vs Sales Volume
- Table: Product Performance Ranking
- Gauge Chart: Inventory Turnover Rate

**Insight Utama:**
- 50 active products
- Average margin 25%
- Inventory turnover 3.2x/year

---

### B.4. Customer Analysis Page

**[INSERT SCREENSHOT HERE]**

**Deskripsi:**
Segmentasi pelanggan, analisis RFM, dan distribusi geografis.

**Komponen:**
- KPI Cards: Total Customers, New Customers, CLV
- Pie Chart: Customer Segmentation (Individu/Bisnis/Reseller)
- Bar Chart: Top 10 Customers by Revenue
- Geo Map: Customer Distribution by City
- Table: RFM Analysis

**Insight Utama:**
- 180 active customers
- Repeat rate 15%
- 85% customers dari Jabodetabek

---

### B.5. Operational Metrics Page

**[INSERT SCREENSHOT HERE]**

**Deskripsi:**
Monitoring efisiensi operasional dan fulfillment.

**Komponen:**
- KPI Cards: Avg Fulfillment Time, On-Time Delivery Rate
- Bar Chart: Order Status Distribution
- Line Chart: Fulfillment Time Trend
- Pie Chart: Payment Method Distribution

**Insight Utama:**
- Completion rate 85%
- Average fulfillment 3-5 hari
- Transfer bank method dominan (55%)

---

### B.6. Financial Analysis Page

**[INSERT SCREENSHOT HERE]**

**Deskripsi:**
Analisis profitabilitas, struktur biaya, dan P&L statement.

**Komponen:**
- KPI Cards: Gross Revenue, Net Profit, Profit Margin
- Waterfall Chart: Revenue Breakdown
- Stacked Bar: Revenue vs Cost vs Profit
- Pie Chart: Cost Breakdown by Category
- Table: Monthly P&L Statement

**Insight Utama:**
- Profit margin 25%
- Bahan baku 45% dari total cost
- Net profit trend positif

---

### B.7. Marketing Performance Page

**[INSERT SCREENSHOT HERE]**

**Deskripsi:**
Evaluasi efektivitas kampanye marketing dan ROI per channel.

**Komponen:**
- KPI Cards: Total Budget, Marketing ROI, Conversion Rate
- Bar Chart: Performance by Platform
- Line Chart: Campaign Timeline
- Funnel Chart: Marketing Funnel
- Table: Campaign Details & ROI

**Insight Utama:**
- Average ROI 300%
- Instagram campaign paling efektif
- Conversion rate 2.5%

---

## LAMPIRAN C: DOKUMENTASI TEKNIS

### C.1. Data Dictionary

**Tabel: master_produk**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| id_produk | VARCHAR(10) | Primary key, unique product ID | P001 |
| nama_produk | VARCHAR(255) | Product name | Nomor Rumah Akrilik Modern |
| kategori | VARCHAR(50) | Product category | Nomor Rumah |
| sub_kategori | VARCHAR(50) | Product sub-category | Custom Standard |
| ukuran | VARCHAR(50) | Product dimensions | 15x20cm |
| warna_base | VARCHAR(50) | Base color | Hitam/Gold |
| harga_jual | DECIMAL(10,2) | Selling price (IDR) | 85000 |
| harga_modal | DECIMAL(10,2) | Cost price (IDR) | 45000 |
| stok_tersedia | INT | Available stock quantity | 25 |
| material | VARCHAR(50) | Material type | Akrilik 5mm |
| finishing | VARCHAR(50) | Finishing type | Glossy |
| berat_gram | INT | Weight in grams | 180 |
| deskripsi | TEXT | Product description | Nomor rumah modern... |
| status_aktif | VARCHAR(20) | Active status | Aktif |
| tanggal_dibuat | DATE | Created date | 2024-01-15 |
| tanggal_update | DATE | Last updated date | 2025-10-20 |

**Tabel: transaksi_penjualan**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| id_transaksi | VARCHAR(10) | Primary key, unique transaction ID | TRX0001 |
| tanggal_transaksi | DATETIME | Transaction timestamp | 2024-11-23 13:05:58 |
| id_pelanggan | VARCHAR(10) | Foreign key to master_pelanggan | C138 |
| id_produk | VARCHAR(10) | Foreign key to master_produk | P015 |
| jumlah_item | INT | Quantity ordered | 1 |
| harga_satuan | DECIMAL(10,2) | Unit price | 205000 |
| subtotal | DECIMAL(10,2) | Subtotal amount | 205000 |
| diskon_persen | INT | Discount percentage | 20 |
| diskon_nominal | DECIMAL(10,2) | Discount amount | 41000 |
| biaya_custom | DECIMAL(10,2) | Customization fee | 0 |
| biaya_ongkir | DECIMAL(10,2) | Shipping fee | 35000 |
| total_pembayaran | DECIMAL(10,2) | Total payment | 199000 |
| metode_pembayaran | VARCHAR(50) | Payment method | Transfer Bank |
| status_pembayaran | VARCHAR(20) | Payment status | Lunas |
| status_pesanan | VARCHAR(20) | Order status | Selesai |
| channel_penjualan | VARCHAR(50) | Sales channel | WhatsApp |
| catatan_pesanan | TEXT | Order notes | (optional) |
| waktu_pengerjaan_hari | INT | Processing time (days) | 2 |
| rating_pelanggan | INT | Customer rating (1-5) | 5 |
| tanggal_selesai | DATE | Completion date | 2024-11-25 |

*(Data dictionary lengkap untuk semua tabel tersedia di dokumentasi terpisah)*

---

### C.2. Calculated Fields & Formulas

**Revenue Metrics:**

1. **Total Revenue:**
   ```
   SUM(total_pembayaran)
   ```

2. **Revenue Growth Rate (%):**
   ```
   (SUM(total_pembayaran_current_period) - SUM(total_pembayaran_previous_period)) 
   / SUM(total_pembayaran_previous_period) * 100
   ```

3. **Average Order Value (AOV):**
   ```
   SUM(total_pembayaran) / COUNT(id_transaksi)
   ```

**Product Metrics:**

4. **Profit per Product:**
   ```
   harga_jual - harga_modal
   ```

5. **Profit Margin (%):**
   ```
   (harga_jual - harga_modal) / harga_jual * 100
   ```

6. **Inventory Turnover Rate:**
   ```
   SUM(stok_keluar) / AVG(stok_tersedia)
   ```

**Customer Metrics:**

7. **Customer Lifetime Value (CLV):**
   ```
   SUM(total_pembayaran) / COUNT_DISTINCT(id_pelanggan)
   ```

8. **Repeat Purchase Rate (%):**
   ```
   COUNT_DISTINCT(CASE WHEN total_transaksi > 1 THEN id_pelanggan END) 
   / COUNT_DISTINCT(id_pelanggan) * 100
   ```

9. **Customer Acquisition Cost (CAC):**
   ```
   SUM(biaya_marketing) / COUNT(new_customers)
   ```

**Operational Metrics:**

10. **Order Fulfillment Time (days):**
    ```
    AVG(waktu_pengerjaan_hari)
    ```

11. **Order Completion Rate (%):**
    ```
    COUNT(CASE WHEN status_pesanan = 'Selesai' THEN 1 END) 
    / COUNT(id_transaksi) * 100
    ```

**Financial Metrics:**

12. **Gross Profit:**
    ```
    SUM(total_pembayaran) - SUM(harga_modal * jumlah_item)
    ```

13. **Net Profit:**
    ```
    SUM(total_pembayaran) - SUM(harga_modal * jumlah_item) - SUM(biaya_operasional)
    ```

14. **ROI Marketing (%):**
    ```
    (revenue_generated - budget) / budget * 100
    ```

---

### C.3. Dashboard Configuration

**Data Sources:**
- Google Sheets: "SATRIAMART BI Data"
- Worksheets: 6 sheets (master_produk, master_pelanggan, transaksi_penjualan, riwayat_stok, biaya_operasional, marketing_campaign)
- Connection: Google Sheets Connector
- Refresh: Manual (atau scheduled via Apps Script)

**Blended Data Sources:**
1. **Transaksi_with_Product_Details:**
   - Left: transaksi_penjualan
   - Right: master_produk
   - Join key: id_produk
   - Type: Left outer join

2. **Transaksi_with_Customer_Details:**
   - Left: transaksi_penjualan
   - Right: master_pelanggan
   - Join key: id_pelanggan
   - Type: Left outer join

**Filters & Controls:**
- Date Range Control: Default last 365 days
- Channel Filter: Multi-select dropdown
- Category Filter: Multi-select dropdown
- Status Filter: Single select dropdown

**Interactivity:**
- Cross-filtering: Enabled
- Drill-down: Category → Product
- Hover tooltips: Custom messages

**Sharing:**
- Access level: View only
- Link sharing: Enabled
- Embed: Allowed

**Performance:**
- Data cache: 12 hours
- Query optimization: Aggregation at source
- Lazy loading: Enabled for tables

---

## LAMPIRAN D: SURAT KETERANGAN RISET

### D.1. Surat Keterangan dari SATRIAMART

**[INSERT SURAT KETERANGAN DI SINI]**

---

**Template Surat Keterangan:**

```
SURAT KETERANGAN
Nomor: [Nomor Surat]/SATRIAMART/[Bulan]/2025

Yang bertanda tangan di bawah ini:

Nama    : [Nama Pemilik/Manager SATRIAMART]
Jabatan : Pemilik/Manager SATRIAMART
Alamat  : Jl. Usman Dehir No.54, Limo, Depok

Dengan ini menerangkan bahwa:

Nama    : [Nama Mahasiswa]
NIM     : [Nomor Induk Mahasiswa]
Prodi   : Pendidikan Teknik Informatika dan Komputer
Instansi: Universitas Negeri Makassar

Telah melakukan riset dan pengembangan Dashboard Business Intelligence 
untuk SATRIAMART pada periode [Bulan] 2025 dalam rangka penyusunan 
Tugas Akhir Mata Kuliah Business Intelligence.

Kegiatan yang dilakukan meliputi:
1. Analisis kebutuhan dashboard dan identifikasi KPI
2. Pengumpulan dan analisis data bisnis
3. Perancangan dan implementasi dashboard interaktif
4. Validasi dan evaluasi dashboard dengan stakeholder

Demikian surat keterangan ini dibuat untuk dapat dipergunakan sebagaimana 
mestinya.


Depok, [Tanggal] Januari 2025

Pemilik SATRIAMART,



[Nama & Tanda Tangan]
[Stempel SATRIAMART]
```

---

## Catatan Penggunaan Lampiran:

1. **Sample Data:**
   - Untuk publikasi, gunakan sample data (bukan full dataset)
   - Pastikan tidak ada informasi sensitif customer

2. **Screenshot Dashboard:**
   - Gunakan high-resolution screenshots (minimum 1920x1080)
   - Blur atau anonymize data sensitif jika perlu
   - Tambahkan caption dan nomor gambar

3. **Dokumentasi Teknis:**
   - Update jika ada perubahan struktur data atau formula
   - Maintain version control

4. **Surat Keterangan:**
   - Minta tanda tangan dan stempel resmi dari SATRIAMART
   - Scan dengan resolusi tinggi (300 dpi)
   - Format: PDF

---

**Status:** Template lampiran siap. Perlu melengkapi:
- [ ] Screenshot dashboard (7 pages)
- [ ] Surat keterangan dari SATRIAMART (dengan tanda tangan & stempel)
- [ ] Nomor gambar dan caption yang sesuai

---

**End of Lampiran**
