# PANDUAN LENGKAP MEMBUAT DASHBOARD LOOKER STUDIO
## SATRIAMART Business Intelligence Dashboard

---

## 📋 DAFTAR ISI
1. [Persiapan Data](#persiapan-data)
2. [Setup Looker Studio](#setup-looker-studio)
3. [Dashboard 1: Executive Summary](#dashboard-1-executive-summary)
4. [Dashboard 2: Sales Analysis](#dashboard-2-sales-analysis)
5. [Dashboard 3: Product Performance](#dashboard-3-product-performance)
6. [Dashboard 4: Customer Analytics](#dashboard-4-customer-analytics)
7. [Dashboard 5: Financial Analysis](#dashboard-5-financial-analysis)
8. [Dashboard 6: Operations & Inventory](#dashboard-6-operations--inventory)
9. [Dashboard 7: Marketing Performance](#dashboard-7-marketing-performance)
10. [Tips & Best Practices](#tips--best-practices)

---

## 📊 PERSIAPAN DATA

### Step 1: Upload CSV ke Google Sheets

**Buat 6 Google Sheets terpisah dengan nama:**

1. **SATRIAMART - Master Produk**
   - Upload: `01_master_produk.csv`
   - 50 baris data produk
   
2. **SATRIAMART - Master Pelanggan**
   - Upload: `02_master_pelanggan.csv`
   - 180 baris data pelanggan
   
3. **SATRIAMART - Transaksi Penjualan**
   - Upload: `03_transaksi_penjualan.csv`
   - 320 baris transaksi
   
4. **SATRIAMART - Riwayat Stok**
   - Upload: `04_riwayat_stok.csv`
   - Data pergerakan stok
   
5. **SATRIAMART - Biaya Operasional**
   - Upload: `05_biaya_operasional.csv`
   - 349 baris biaya operasional
   
6. **SATRIAMART - Marketing Campaign**
   - Upload: `06_marketing_campaign.csv`
   - 24 campaign marketing

### Step 2: Format Data di Google Sheets

**Untuk setiap sheet, pastikan:**
- ✅ Baris pertama adalah header
- ✅ Format tanggal: DD/MM/YYYY
- ✅ Format angka: Gunakan number format tanpa simbol
- ✅ Tidak ada baris kosong
- ✅ Tidak ada karakter spesial yang aneh

**Khusus untuk kolom tanggal, ubah format:**
```
Format > Number > Date
```

**Khusus untuk kolom uang/angka:**
```
Format > Number > Number (tanpa desimal)
```

---

## 🚀 SETUP LOOKER STUDIO

### Step 1: Buka Looker Studio
1. Buka https://lookerstudio.google.com
2. Login dengan akun Google Anda
3. Klik **"Create"** > **"Report"**

### Step 2: Koneksi Data Source
1. Pilih **"Google Sheets"**
2. Pilih spreadsheet yang sudah di-upload
3. Pilih worksheet (tab) yang sesuai
4. Klik **"Add"**

### Step 3: Ulangi untuk Semua Data Source
Tambahkan 6 data source:
- Master Produk
- Master Pelanggan
- Transaksi Penjualan
- Riwayat Stok
- Biaya Operasional
- Marketing Campaign

### Step 4: Setup Blend Data (Menggabungkan Data)

**Blend 1: Transaksi + Produk**
- Left table: Transaksi Penjualan
- Join key: `id_produk`
- Right table: Master Produk
- Join key: `id_produk`
- Join type: LEFT OUTER JOIN

**Blend 2: Transaksi + Pelanggan**
- Left table: Transaksi Penjualan
- Join key: `id_pelanggan`
- Right table: Master Pelanggan
- Join key: `id_pelanggan`
- Join type: LEFT OUTER JOIN

**Blend 3: Riwayat Stok + Produk**
- Left table: Riwayat Stok
- Join key: `id_produk`
- Right table: Master Produk
- Join key: `id_produk`
- Join type: LEFT OUTER JOIN

---

## 📈 DASHBOARD 1: EXECUTIVE SUMMARY

### Layout Dashboard
```
┌─────────────────────────────────────────────────────┐
│  🏢 SATRIAMART - Executive Dashboard                │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Total    │ Total    │ Avg      │ Total    │ Period  │
│ Revenue  │ Trans    │ Order    │ Customer │ Filter  │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│ Revenue Trend (Line Chart)  │ Sales by Channel     │
│                              │ (Donut Chart)        │
├──────────────────────────────┴──────────────────────┤
│ Category Performance │ Payment Method │ Order Status│
│ (Bar Chart)          │ (Pie Chart)    │ (Pie)       │
├──────────────────────────────────────────────────────┤
│ Top 10 Products by Revenue (Table)                  │
└─────────────────────────────────────────────────────┘
```

### Komponen Dashboard 1

#### 1. Header & Title
- **Component**: Text box
- **Content**: "SATRIAMART Business Intelligence Dashboard"
- **Style**: 
  - Font: Roboto Bold
  - Size: 24pt
  - Color: #166534 (hijau)
  - Background: Linear gradient hijau

#### 2. Period Filter (Date Range Control)
- **Component**: Date range control
- **Data source**: Transaksi Penjualan
- **Date field**: `tanggal_transaksi`
- **Default range**: Last 365 days
- **Position**: Top right

#### 3. KPI Card: Total Revenue
- **Component**: Scorecard
- **Data source**: Transaksi Penjualan
- **Metric**: `SUM(total_pembayaran)`
- **Format**: Currency (IDR)
- **Compact numbers**: Yes
- **Style**:
  - Background: #22C55E (hijau)
  - Text color: White
  - Font size: 36pt

**Calculated Field untuk Total Revenue:**
```
Field Name: Total Revenue
Formula: SUM(total_pembayaran)
Type: Number
```

#### 4. KPI Card: Total Transactions
- **Component**: Scorecard
- **Data source**: Transaksi Penjualan
- **Metric**: `COUNT(id_transaksi)`
- **Format**: Number
- **Style**:
  - Background: #3B82F6 (biru)
  - Text color: White

#### 5. KPI Card: Average Order Value
- **Component**: Scorecard
- **Data source**: Transaksi Penjualan
- **Metric**: Calculated field
- **Format**: Currency (IDR)
- **Style**:
  - Background: #A855F7 (ungu)
  - Text color: White

**Calculated Field untuk AOV:**
```
Field Name: Average Order Value
Formula: SUM(total_pembayaran) / COUNT(id_transaksi)
Type: Currency (IDR)
```

#### 6. KPI Card: Total Customers
- **Component**: Scorecard
- **Data source**: Transaksi Penjualan
- **Metric**: `COUNT_DISTINCT(id_pelanggan)`
- **Format**: Number
- **Style**:
  - Background: #F97316 (orange)
  - Text color: White

#### 7. Revenue Trend (Line Chart)
- **Component**: Time series chart
- **Data source**: Transaksi Penjualan
- **Dimension**: `tanggal_transaksi` (Month)
- **Metric**: `SUM(total_pembayaran)`
- **Configuration**:
  - Chart type: Line chart with smooth curve
  - Show data labels: No
  - Show legend: Yes
  - Line color: #22C55E
  - Grid lines: Yes

**Steps:**
1. Add chart > Time series
2. Date dimension: `tanggal_transaksi`
3. Metric: `total_pembayaran`
4. Aggregation: SUM
5. Style tab > Line > Smooth curve

#### 8. Sales by Channel (Donut Chart)
- **Component**: Pie chart (Donut style)
- **Data source**: Transaksi Penjualan
- **Dimension**: `channel_penjualan`
- **Metric**: `SUM(total_pembayaran)`
- **Configuration**:
  - Donut: Yes
  - Donut hole: 50%
  - Show slice labels: Yes
  - Show percentages: Yes
  - Colors: Custom palette

**Custom Colors:**
- Offline Store: #22C55E
- Instagram: #EC4899
- TikTok: #000000
- WhatsApp: #10B981
- Website: #3B82F6

#### 9. Category Performance (Bar Chart)
- **Component**: Bar chart (Horizontal)
- **Data source**: Blend (Transaksi + Produk)
- **Dimension**: `kategori` (from Master Produk)
- **Metric**: `SUM(total_pembayaran)`
- **Configuration**:
  - Sort: Descending by metric
  - Show data labels: Yes
  - Bar color: #3B82F6

**Steps:**
1. Add chart > Bar chart
2. Dimension: `kategori`
3. Metric: `total_pembayaran`
4. Sort: Metric descending
5. Style > Bars > Color: Blue

#### 10. Payment Method Distribution (Pie Chart)
- **Component**: Pie chart
- **Data source**: Transaksi Penjualan
- **Dimension**: `metode_pembayaran`
- **Metric**: `COUNT(id_transaksi)`
- **Configuration**:
  - Show legend: Bottom
  - Show percentages: Yes

#### 11. Order Status (Pie Chart)
- **Component**: Pie chart
- **Data source**: Transaksi Penjualan
- **Dimension**: `status_pesanan`
- **Metric**: `COUNT(id_transaksi)`
- **Configuration**:
  - Show legend: Bottom
  - Show percentages: Yes

**Custom Colors:**
- Selesai: #22C55E (hijau)
- Diterima: #10B981 (hijau muda)
- Dikirim: #3B82F6 (biru)
- Proses: #F59E0B (orange)
- Dibatalkan: #EF4444 (merah)

#### 12. Top 10 Products Table
- **Component**: Table with heatmap
- **Data source**: Blend (Transaksi + Produk)
- **Dimensions**: 
  1. `nama_produk`
  2. `kategori`
- **Metrics**:
  1. `SUM(total_pembayaran)` - as "Revenue"
  2. `SUM(jumlah_item)` - as "Units Sold"
  3. `COUNT(id_transaksi)` - as "Transactions"
- **Configuration**:
  - Rows per page: 10
  - Sort: Revenue descending
  - Show heatmap on Revenue column

**Steps:**
1. Add chart > Table
2. Add dimensions: nama_produk, kategori
3. Add metrics: total_pembayaran (SUM), jumlah_item (SUM)
4. Sort by Revenue descending
5. Style > Table body > Enable heatmap for Revenue

---

## 💰 DASHBOARD 2: SALES ANALYSIS

### Layout Dashboard
```
┌─────────────────────────────────────────────────────┐
│  💰 Sales Analysis Dashboard                        │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Gross    │ Net      │ Total    │ Shipping │ Filters │
│ Sales    │ Sales    │ Discount │ Revenue  │         │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│ Channel Performance (Bar Chart + Metrics Table)     │
├──────────────────────────────┬──────────────────────┤
│ Sales by Day of Week         │ Monthly Trend        │
│ (Column Chart)               │ (Combo Chart)        │
├──────────────────────────────┼──────────────────────┤
│ Order Status Distribution    │ Payment Status       │
│ (Donut Chart)                │ (Pie Chart)          │
├──────────────────────────────────────────────────────┤
│ Transaction Details Table (with filters)            │
└─────────────────────────────────────────────────────┘
```

### Komponen Dashboard 2

#### 1. Filter Controls (Top)
**Filter 1: Period**
- Component: Date range control
- Field: `tanggal_transaksi`

**Filter 2: Channel**
- Component: Drop-down list
- Field: `channel_penjualan`
- Include "All" option: Yes

**Filter 3: Status**
- Component: Drop-down list
- Field: `status_pesanan`
- Include "All" option: Yes

#### 2. KPI: Gross Sales
**Calculated Field:**
```
Field Name: Gross Sales
Formula: SUM(subtotal)
Type: Currency (IDR)
```

- **Component**: Scorecard
- **Metric**: Gross Sales
- **Style**: Green background

#### 3. KPI: Net Sales
- **Component**: Scorecard
- **Metric**: `SUM(total_pembayaran)`
- **Style**: Blue background

#### 4. KPI: Total Discounts
- **Component**: Scorecard
- **Metric**: `SUM(diskon_nominal)`
- **Style**: Purple background
- **Add comparison**: Show % of Gross Sales

**Calculated Field untuk Discount Rate:**
```
Field Name: Discount Rate
Formula: SUM(diskon_nominal) / SUM(subtotal)
Type: Percent
```

#### 5. KPI: Shipping Revenue
- **Component**: Scorecard
- **Metric**: `SUM(biaya_ongkir)`
- **Style**: Orange background

#### 6. Channel Performance Comparison
**Part A: Revenue Bar Chart**
- **Component**: Bar chart
- **Dimension**: `channel_penjualan`
- **Metric**: `SUM(total_pembayaran)`
- **Sort**: Descending

**Part B: Channel Metrics Table**
- **Component**: Table
- **Dimensions**: `channel_penjualan`
- **Metrics**:
  1. `SUM(total_pembayaran)` - Revenue
  2. `COUNT(id_transaksi)` - Transactions
  3. `AVG(total_pembayaran)` - Avg Order Value
  4. `SUM(jumlah_item)` - Items Sold

**Calculated Field untuk Average per Channel:**
```
Field Name: Channel AOV
Formula: SUM(total_pembayaran) / COUNT(id_transaksi)
Type: Currency (IDR)
```

#### 7. Sales by Day of Week
- **Component**: Column chart
- **Dimension**: Custom calculated field
- **Metric**: `SUM(total_pembayaran)`

**Calculated Field untuk Day of Week:**
```
Field Name: Day of Week
Formula: 
CASE 
  WHEN WEEKDAY(tanggal_transaksi) = 1 THEN "Sunday"
  WHEN WEEKDAY(tanggal_transaksi) = 2 THEN "Monday"
  WHEN WEEKDAY(tanggal_transaksi) = 3 THEN "Tuesday"
  WHEN WEEKDAY(tanggal_transaksi) = 4 THEN "Wednesday"
  WHEN WEEKDAY(tanggal_transaksi) = 5 THEN "Thursday"
  WHEN WEEKDAY(tanggal_transaksi) = 6 THEN "Friday"
  WHEN WEEKDAY(tanggal_transaksi) = 7 THEN "Saturday"
END
Type: Text
```

**Order the days:**
1. Add dimension: Day of Week
2. Style > Sort > Manual
3. Arrange: Mon, Tue, Wed, Thu, Fri, Sat, Sun

#### 8. Monthly Sales Trend (Combo Chart)
- **Component**: Combo chart (Line + Bar)
- **Dimension**: `tanggal_transaksi` (Month)
- **Metrics**:
  - Bar: `SUM(total_pembayaran)` - Monthly Revenue
  - Line: `COUNT(id_transaksi)` - Transaction Count
- **Configuration**:
  - Left Y-axis: Revenue (IDR)
  - Right Y-axis: Transaction count
  - Bar color: Blue
  - Line color: Orange

#### 9. Transaction Status & Conversion

**Scorecard Group: Conversion Metrics**

**Completion Rate:**
```
Field Name: Completion Rate
Formula: 
COUNT(CASE WHEN status_pesanan IN ("Selesai", "Diterima") THEN id_transaksi END) 
/ COUNT(id_transaksi)
Type: Percent
```

**Cancellation Rate:**
```
Field Name: Cancellation Rate
Formula: 
COUNT(CASE WHEN status_pesanan = "Dibatalkan" THEN id_transaksi END) 
/ COUNT(id_transaksi)
Type: Percent
```

**In Progress Rate:**
```
Field Name: In Progress Rate
Formula: 
COUNT(CASE WHEN status_pesanan IN ("Proses", "Dikirim") THEN id_transaksi END) 
/ COUNT(id_transaksi)
Type: Percent
```

#### 10. Order Status Donut Chart
- **Component**: Pie chart (Donut)
- **Dimension**: `status_pesanan`
- **Metric**: `COUNT(id_transaksi)`
- **Custom colors**: As defined earlier

#### 11. Payment Status Pie Chart
- **Component**: Pie chart
- **Dimension**: `status_pembayaran`
- **Metric**: `COUNT(id_transaksi)`

#### 12. Transaction Details Table
- **Component**: Table with pagination
- **Dimensions**:
  1. `id_transaksi`
  2. `tanggal_transaksi`
  3. `channel_penjualan`
  4. `status_pesanan`
- **Metrics**:
  1. `subtotal`
  2. `diskon_nominal`
  3. `total_pembayaran`
- **Configuration**:
  - Rows per page: 20
  - Enable pagination
  - Sort: Date descending
  - Compact numbers: No

---

## 📦 DASHBOARD 3: PRODUCT PERFORMANCE

### Layout Dashboard
```
┌─────────────────────────────────────────────────────┐
│  📦 Product Performance Dashboard                   │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Total    │ Active   │ Inventory│ Avg      │ Low     │
│ Products │ Products │ Value    │ Margin   │ Stock   │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│ Category Revenue (Bar) │ Category Metrics (Table)  │
├────────────────────────┴───────────────────────────┤
│ Top 10 Products        │ Bottom 10 Products        │
│ (Bar Chart)            │ (Bar Chart)               │
├────────────────────────┼───────────────────────────┤
│ Price Range Dist.      │ Profit Margin by Category │
│ (Histogram)            │ (Bar Chart)               │
├──────────────────────────────────────────────────────┤
│ Stock Level Analysis (3 Scorecards + Pie Chart)     │
├──────────────────────────────────────────────────────┤
│ Product Catalog Table (with search & filters)       │
└─────────────────────────────────────────────────────┘
```

### Komponen Dashboard 3

#### 1. Filter Controls
**Filter 1: Period**
- Component: Date range control
- Field: `tanggal_transaksi` (from blended data)

**Filter 2: Category**
- Component: Drop-down list
- Field: `kategori` (from Master Produk)
- Multi-select: Yes

**Filter 3: Search Product**
- Component: Text filter
- Field: `nama_produk`
- Match type: Contains

#### 2. KPI: Total Products
**Calculated Field:**
```
Field Name: Total Products
Formula: COUNT_DISTINCT(id_produk)
Type: Number
```

- **Component**: Scorecard
- **Data source**: Blend (Transaksi + Produk)
- **Metric**: Total Products
- **Note**: Only counts products with sales in period

#### 3. KPI: Active Products
**Calculated Field:**
```
Field Name: Active Products Count
Formula: COUNT(CASE WHEN status_aktif = "Aktif" THEN id_produk END)
Type: Number
```

- **Component**: Scorecard
- **Metric**: Active Products Count
- **Comparison metric**: Total Products
- **Show percentage**: Yes

#### 4. KPI: Inventory Value
**Calculated Field:**
```
Field Name: Inventory Value
Formula: SUM(stok_tersedia * harga_jual)
Type: Currency (IDR)
```

- **Component**: Scorecard
- **Data source**: Master Produk
- **Metric**: Inventory Value
- **Style**: Purple background

#### 5. KPI: Average Margin
**Calculated Field:**
```
Field Name: Profit Margin Percent
Formula: 
SUM((harga_jual - harga_modal) * stok_tersedia) / SUM(harga_jual * stok_tersedia)
Type: Percent
```

- **Component**: Scorecard
- **Metric**: Profit Margin Percent
- **Format**: Percentage with 1 decimal

#### 6. KPI: Low Stock Count
**Calculated Field:**
```
Field Name: Low Stock Products
Formula: COUNT(CASE WHEN stok_tersedia < 10 THEN id_produk END)
Type: Number
```

- **Component**: Scorecard with alert
- **Metric**: Low Stock Products
- **Style**: Orange/Red if > 0
- **Conditional formatting**: Red if > 10

#### 7. Category Revenue (Bar Chart)
- **Component**: Bar chart (horizontal)
- **Data source**: Blend (Transaksi + Produk)
- **Dimension**: `kategori`
- **Metric**: `SUM(total_pembayaran)`
- **Configuration**:
  - Sort: Descending by revenue
  - Show data labels: Yes
  - Bar color gradient: Blue to Green

#### 8. Category Metrics Table
- **Component**: Table with heatmap
- **Data source**: Blend (Transaksi + Produk)
- **Dimension**: `kategori`
- **Metrics**:
  1. `SUM(total_pembayaran)` - Revenue
  2. `COUNT_DISTINCT(id_produk)` - Products
  3. `SUM(jumlah_item)` - Units Sold
  4. Average Price (calculated)
  5. Average Margin (calculated)

**Calculated Field: Category Average Price**
```
Field Name: Avg Product Price
Formula: AVG(harga_jual)
Type: Currency (IDR)
```

**Calculated Field: Category Average Margin**
```
Field Name: Avg Margin
Formula: AVG((harga_jual - harga_modal) / harga_jual)
Type: Percent
```

#### 9. Top 10 Products (Best Sellers)
- **Component**: Bar chart
- **Data source**: Blend (Transaksi + Produk)
- **Dimension**: `nama_produk`
- **Metric**: `SUM(total_pembayaran)`
- **Configuration**:
  - Max rows: 10
  - Sort: Descending
  - Bar color: Green gradient
  - Show data labels: Yes

#### 10. Bottom 10 Products (Slow Movers)
- **Component**: Bar chart
- **Data source**: Blend (Transaksi + Produk)
- **Dimension**: `nama_produk`
- **Metric**: `SUM(total_pembayaran)`
- **Configuration**:
  - Max rows: 10
  - Sort: Ascending
  - Bar color: Red gradient
  - Show data labels: Yes
  - Filter: Exclude products with 0 sales

#### 11. Price Range Distribution
- **Component**: Column chart (Histogram)
- **Data source**: Master Produk
- **Dimension**: Price Range (calculated)
- **Metric**: `COUNT(id_produk)`

**Calculated Field: Price Range**
```
Field Name: Price Range
Formula: 
CASE 
  WHEN harga_jual < 100000 THEN "< Rp 100K"
  WHEN harga_jual < 200000 THEN "Rp 100K - 200K"
  WHEN harga_jual < 300000 THEN "Rp 200K - 300K"
  WHEN harga_jual < 500000 THEN "Rp 300K - 500K"
  ELSE "> Rp 500K"
END
Type: Text
```

**Manual Sort Order:**
1. < Rp 100K
2. Rp 100K - 200K
3. Rp 200K - 300K
4. Rp 300K - 500K
5. > Rp 500K

#### 12. Profit Margin by Category
- **Component**: Bar chart
- **Data source**: Master Produk
- **Dimension**: `kategori`
- **Metric**: Average Margin (calculated)
- **Configuration**:
  - Sort: Descending
  - Bar color: Based on value (conditional)
  - Green if > 30%, Orange if 20-30%, Red if < 20%

**Calculated Field:**
```
Field Name: Margin Percentage
Formula: AVG((harga_jual - harga_modal) / harga_jual) * 100
Type: Number
```

#### 13. Stock Level Analysis

**Scorecard 1: Critical Stock (< 5)**
```
Field Name: Critical Stock
Formula: COUNT(CASE WHEN stok_tersedia < 5 THEN id_produk END)
Type: Number
Style: Red background, White text
```

**Scorecard 2: Low Stock (5-10)**
```
Field Name: Low Stock
Formula: COUNT(CASE WHEN stok_tersedia >= 5 AND stok_tersedia < 10 THEN id_produk END)
Type: Number
Style: Orange background, White text
```

**Scorecard 3: Healthy Stock (>= 10)**
```
Field Name: Healthy Stock
Formula: COUNT(CASE WHEN stok_tersedia >= 10 THEN id_produk END)
Type: Number
Style: Green background, White text
```

**Pie Chart: Stock Distribution**
- **Component**: Pie chart
- **Data source**: Master Produk
- **Dimension**: Stock Level Category (calculated)
- **Metric**: `COUNT(id_produk)`

**Calculated Field: Stock Level**
```
Field Name: Stock Level Category
Formula: 
CASE 
  WHEN stok_tersedia < 5 THEN "Critical (< 5)"
  WHEN stok_tersedia < 10 THEN "Low (5-10)"
  ELSE "Healthy (>= 10)"
END
Type: Text
```

#### 14. Product Catalog Table
- **Component**: Table with search and filters
- **Data source**: Master Produk
- **Dimensions**:
  1. `nama_produk`
  2. `kategori`
  3. `sub_kategori`
  4. `ukuran`
  5. `warna_base`
- **Metrics**:
  1. `harga_jual` - Price
  2. `harga_modal` - Cost
  3. Margin % (calculated)
  4. `stok_tersedia` - Stock
  5. `status_aktif` - Status
- **Configuration**:
  - Enable search
  - Rows per page: 20
  - Sort: Stock ascending (prioritize low stock)
  - Conditional formatting on stock column

**Conditional Formatting Rules:**
- Stock < 5: Red background
- Stock 5-10: Orange background
- Stock >= 10: Green background

---

## 👥 DASHBOARD 4: CUSTOMER ANALYTICS

### Layout Dashboard
```
┌─────────────────────────────────────────────────────┐
│  👥 Customer Analytics Dashboard                    │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Total    │ Avg      │ Repeat   │ Avg      │ Filters │
│ Customer │ Value    │ Rate     │ Rating   │         │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│ Customer Segmentation  │ Segment Details (Table)   │
│ (Donut Chart)          │                           │
├────────────────────────┴───────────────────────────┤
│ Geographic Distribution│ City Revenue (Bar Chart)  │
│ (Geo Map/Bar Chart)    │                           │
├────────────────────────┼───────────────────────────┤
│ Purchase Frequency     │ Gender Distribution       │
│ (Histogram)            │ (Pie Chart)               │
├────────────────────────┼───────────────────────────┤
│ Age Distribution       │ Top 20 Customers          │
│ (Column Chart)         │ (Table with metrics)      │
├──────────────────────────────────────────────────────┤
│ Customer Database (Detailed Table with RFM)         │
└─────────────────────────────────────────────────────┘
```

### Komponen Dashboard 4

#### 1. Filter Controls
**Filter 1: Period**
- Component: Date range control
- Field: `tanggal_transaksi`

**Filter 2: City**
- Component: Drop-down list
- Field: `kota` (from Master Pelanggan)
- Multi-select: Yes

**Filter 3: Customer Search**
- Component: Text filter
- Field: `nama_pelanggan`
- Match type: Contains

#### 2. KPI: Total Customers (Active in Period)
**Calculated Field:**
```
Field Name: Active Customers
Formula: COUNT_DISTINCT(id_pelanggan)
Type: Number
Note: Based on customers who made transactions in selected period
```

- **Component**: Scorecard
- **Data source**: Blend (Transaksi + Pelanggan)
- **Metric**: Active Customers

#### 3. KPI: Average Customer Value
**Calculated Field:**
```
Field Name: Customer Lifetime Value
Formula: SUM(total_pembayaran) / COUNT_DISTINCT(id_pelanggan)
Type: Currency (IDR)
```

- **Component**: Scorecard
- **Metric**: Customer Lifetime Value
- **Style**: Blue background

#### 4. KPI: Repeat Customer Rate

**Step 1: Create Blend for Repeat Customers**
- Blend: Group by `id_pelanggan`
- Metric: `COUNT(id_transaksi)` as transaction_count

**Calculated Field:**
```
Field Name: Repeat Customer Rate
Formula: 
COUNT(CASE WHEN transaction_count >= 2 THEN id_pelanggan END) 
/ COUNT_DISTINCT(id_pelanggan)
Type: Percent
```

- **Component**: Scorecard
- **Metric**: Repeat Customer Rate
- **Style**: Purple background

#### 5. KPI: Average Rating
**Calculated Field:**
```
Field Name: Average Customer Rating
Formula: AVG(rating_kepuasan)
Type: Number (1 decimal)
```

- **Component**: Scorecard
- **Metric**: Average Customer Rating
- **Suffix**: "⭐ / 5.0"
- **Style**: Orange background

#### 6. Customer Segmentation (RFM - Donut Chart)

**First, create RFM Segment calculated field:**
```
Field Name: Customer Segment
Formula: 
CASE 
  WHEN transaction_count >= 4 THEN "VIP"
  WHEN transaction_count >= 2 AND total_revenue >= 500000 THEN "Loyal"
  WHEN transaction_count >= 2 THEN "Regular"
  WHEN total_revenue >= 300000 THEN "High Value"
  ELSE "New"
END
Type: Text
```

**Note:** You'll need to create a blended data source that groups by customer:
- Data source: Transaksi Penjualan
- Group by: `id_pelanggan`
- Metrics: 
  - `COUNT(id_transaksi)` as transaction_count
  - `SUM(total_pembayaran)` as total_revenue

- **Component**: Donut chart
- **Dimension**: Customer Segment
- **Metric**: `COUNT_DISTINCT(id_pelanggan)`
- **Custom colors**:
  - VIP: #9333EA (purple)
  - Loyal: #22C55E (green)
  - Regular: #3B82F6 (blue)
  - High Value: #F59E0B (orange)
  - New: #6B7280 (gray)

#### 7. Segment Details Table
- **Component**: Table
- **Data source**: Customer segments blend
- **Dimension**: Customer Segment
- **Metrics**:
  1. `COUNT_DISTINCT(id_pelanggan)` - Customers
  2. `SUM(total_pembayaran)` - Total Revenue
  3. `AVG(total_pembayaran)` - Avg Revenue per Customer
  4. `AVG(transaction_count)` - Avg Transactions
- **Configuration**:
  - Sort: By customer count descending
  - Show totals: Yes
  - Heatmap on Revenue column

#### 8. Geographic Distribution - City Revenue
- **Component**: Bar chart (horizontal)
- **Data source**: Blend (Transaksi + Pelanggan)
- **Dimension**: `kota`
- **Metric**: `SUM(total_pembayaran)`
- **Configuration**:
  - Sort: Descending
  - Top 10 cities
  - Show data labels: Yes

**Alternative: Geo Map (if available)**
- Component: Geo chart
- Location: `kota`
- Metric: `SUM(total_pembayaran)`
- Color range: Light to dark green

#### 9. City Details Table
- **Component**: Table
- **Data source**: Blend (Transaksi + Pelanggan)
- **Dimension**: `kota`
- **Metrics**:
  1. `COUNT_DISTINCT(id_pelanggan)` - Customers
  2. `SUM(total_pembayaran)` - Revenue
  3. `COUNT(id_transaksi)` - Transactions
  4. Customer LTV (calculated)

#### 10. Purchase Frequency Distribution
- **Component**: Column chart (Histogram)
- **Data source**: Customer transaction counts blend
- **Dimension**: Transaction Bucket (calculated)
- **Metric**: `COUNT(id_pelanggan)`

**Calculated Field: Transaction Bucket**
```
Field Name: Transaction Frequency
Formula: 
CASE 
  WHEN transaction_count = 1 THEN "1 Transaction"
  WHEN transaction_count = 2 THEN "2 Transactions"
  WHEN transaction_count = 3 THEN "3 Transactions"
  WHEN transaction_count >= 4 AND transaction_count <= 5 THEN "4-5 Transactions"
  ELSE "6+ Transactions"
END
Type: Text
```

#### 11. Gender Distribution
- **Component**: Pie chart
- **Data source**: Master Pelanggan
- **Dimension**: `jenis_kelamin`
- **Metric**: `COUNT(id_pelanggan)`
- **Colors**:
  - Laki-laki: #3B82F6 (blue)
  - Perempuan: #EC4899 (pink)

#### 12. Age Distribution
- **Component**: Column chart
- **Data source**: Master Pelanggan
- **Dimension**: Age Group (calculated)
- **Metric**: `COUNT(id_pelanggan)`

**Calculated Field: Age Group**
```
Field Name: Age Group
Formula: 
CASE 
  WHEN usia < 25 THEN "18-24"
  WHEN usia < 35 THEN "25-34"
  WHEN usia < 45 THEN "35-44"
  WHEN usia < 55 THEN "45-54"
  ELSE "55+"
END
Type: Text
```

**Manual Sort:**
1. 18-24
2. 25-34
3. 35-44
4. 45-54
5. 55+

#### 13. Top 20 Customers Table
- **Component**: Table with ranking
- **Data source**: Customer aggregated blend
- **Dimensions**:
  1. Rank (row number)
  2. `nama_pelanggan`
  3. `kota`
  4. Customer Segment
- **Metrics**:
  1. `SUM(total_pembayaran)` - Total Spent
  2. `COUNT(id_transaksi)` - Transactions
  3. `AVG(total_pembayaran)` - Avg Order
  4. Last Purchase Date (MAX)
- **Configuration**:
  - Max rows: 20
  - Sort: Total Spent descending
  - Heatmap on Total Spent

**Add Row Number:**
1. Style > Table header
2. Enable row numbers
3. Start from: 1

#### 14. Customer Database Table
- **Component**: Table with filters
- **Data source**: Blend (Transaksi + Pelanggan)
- **Dimensions**:
  1. `nama_pelanggan`
  2. `email`
  3. `kota`
  4. `jenis_kelamin`
  5. Age Group
  6. Customer Segment
- **Metrics**:
  1. `COUNT(id_transaksi)` - Orders
  2. `SUM(total_pembayaran)` - Revenue
  3. `AVG(rating_kepuasan)` - Avg Rating
  4. Last Purchase (calculated)
- **Configuration**:
  - Rows per page: 25
  - Enable search
  - Enable column sorting

**Calculated Field: Last Purchase**
```
Field Name: Last Purchase Date
Formula: MAX(tanggal_transaksi)
Type: Date
Format: DD/MM/YYYY
```

**Calculated Field: Days Since Last Purchase**
```
Field Name: Days Since Purchase
Formula: DATE_DIFF(TODAY(), MAX(tanggal_transaksi))
Type: Number
```

---

## 💵 DASHBOARD 5: FINANCIAL ANALYSIS

### Layout Dashboard
```
┌─────────────────────────────────────────────────────┐
│  💵 Financial Analysis Dashboard                    │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Total    │ Total    │ Gross    │ Net      │ Filters │
│ Revenue  │ Costs    │ Profit   │ Profit   │         │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│ Revenue vs Profit Trend (Line/Combo Chart)         │
├──────────────────────────────┬──────────────────────┤
│ Profit Margin Trend          │ Cost Breakdown       │
│ (Line Chart)                 │ (Donut Chart)        │
├──────────────────────────────┴──────────────────────┤
│ Cost Category (Bar)│ Monthly Cost Trend (Line)     │
├────────────────────┴───────────────────────────────┤
│ Revenue Sources (3 Scorecards + Bar Chart)         │
├──────────────────────────────────────────────────────┤
│ Payment Method Distribution (Pie + Table)           │
├──────────────────────────────────────────────────────┤
│ Expense Details Table (with filters)                │
└─────────────────────────────────────────────────────┘
```

### Komponen Dashboard 5

#### 1. Filter Controls
**Filter 1: Period**
- Component: Date range control
- Field: `tanggal_transaksi`

**Filter 2: Cost Category**
- Component: Drop-down list
- Field: `kategori_biaya` (from Biaya Operasional)
- Multi-select: Yes

**Filter 3: Month**
- Component: Drop-down list
- Field: Month from `tanggal` (extracted)

#### 2. KPI: Total Revenue
- **Component**: Scorecard
- **Data source**: Transaksi Penjualan
- **Metric**: `SUM(total_pembayaran)`
- **Comparison**: Previous period (if date range control allows)
- **Style**: Green background

**Add Period Comparison:**
```
Field Name: Revenue Growth
Formula: 
(SUM(total_pembayaran) - SUM(total_pembayaran) [Previous Period]) 
/ SUM(total_pembayaran) [Previous Period]
Type: Percent
Note: Use comparison date range feature in Looker Studio
```

#### 3. KPI: Total Costs
**Calculated Field - COGS:**
```
Field Name: COGS (Cost of Goods Sold)
Formula: SUM(harga_modal * jumlah_item)
Type: Currency (IDR)
Data source: Blend (Transaksi + Produk)
```

**Calculated Field - Operational Costs (Exclude Bahan Baku):**
```
Field Name: Operational Costs
Formula: 
SUM(CASE WHEN kategori_biaya != "Bahan Baku" THEN jumlah END)
Type: Currency (IDR)
Data source: Biaya Operasional
```

**Calculated Field - Total Costs:**
```
Field Name: Total Costs
Formula: COGS + Operational Costs
Type: Currency (IDR)
Note: May need to create a blended data source
```

- **Component**: Scorecard
- **Metric**: Total Costs
- **Style**: Blue background

#### 4. KPI: Gross Profit
**Calculated Field:**
```
Field Name: Gross Profit
Formula: SUM(total_pembayaran) - SUM(harga_modal * jumlah_item)
Type: Currency (IDR)
```

- **Component**: Scorecard
- **Metric**: Gross Profit
- **Add metric**: Gross Margin %
- **Style**: Purple background

**Calculated Field: Gross Margin:**
```
Field Name: Gross Margin Percent
Formula: 
(SUM(total_pembayaran) - SUM(harga_modal * jumlah_item)) 
/ SUM(total_pembayaran)
Type: Percent
```

#### 5. KPI: Net Profit
**Calculated Field:**
```
Field Name: Net Profit
Formula: Total Revenue - (COGS + Operational Costs)
Type: Currency (IDR)
Note: This requires careful blending of data sources
```

- **Component**: Scorecard
- **Metric**: Net Profit
- **Add metric**: Net Margin %
- **Style**: Orange background
- **Conditional color**: Green if positive, Red if negative

**Calculated Field: Net Margin:**
```
Field Name: Net Margin Percent
Formula: Net Profit / Total Revenue
Type: Percent
```

#### 6. Revenue vs Profit Trend (Combo Chart)
- **Component**: Combo chart (Line + Column)
- **Dimension**: `tanggal_transaksi` (Month)
- **Metrics**:
  - Column: `SUM(total_pembayaran)` - Revenue
  - Line: Gross Profit (calculated)
  - Line: Net Profit (calculated)
- **Configuration**:
  - Left Y-axis: Currency (IDR)
  - Column color: Blue
  - Gross Profit line: Green
  - Net Profit line: Orange
  - Show data labels: Key points only

#### 7. Profit Margin Trend
- **Component**: Line chart with dual lines
- **Dimension**: `tanggal_transaksi` (Month)
- **Metrics**:
  - Gross Margin % (calculated)
  - Net Margin % (calculated)
- **Configuration**:
  - Y-axis: Percentage (0-100%)
  - Gross Margin: Green line
  - Net Margin: Blue line
  - Show reference line at 20% (target margin)

#### 8. Cost Breakdown (Donut Chart)
- **Component**: Donut chart
- **Data sources**: Blended (COGS + Operational)
- **Dimension**: Cost Type
- **Metric**: Amount

**You'll need to create a manual data source or union:**
- COGS as one category
- Each operational cost category

**Alternative approach:**
- Chart 1: COGS vs Operational Costs (2 slices)
- Chart 2: Operational Cost Breakdown (detailed)

#### 9. Cost by Category (Bar Chart)
- **Component**: Bar chart
- **Data source**: Biaya Operasional (filtered: exclude Bahan Baku)
- **Dimension**: `kategori_biaya`
- **Metric**: `SUM(jumlah)`
- **Configuration**:
  - Sort: Descending
  - Show data labels: Yes

#### 10. Monthly Cost Trend
- **Component**: Line chart (multi-line)
- **Dimension**: Month from `tanggal`
- **Metrics**: 
  - COGS (calculated from transactions)
  - Total Operational Costs
- **Configuration**:
  - Smooth curves: Yes
  - Show area under curve: Optional

#### 11. Revenue Sources (Breakdown)

**Scorecard 1: Product Sales**
```
Field Name: Product Sales Revenue
Formula: SUM(subtotal - diskon_nominal)
Type: Currency (IDR)
```

**Scorecard 2: Shipping Revenue**
```
Field Name: Shipping Revenue
Formula: SUM(biaya_ongkir)
Type: Currency (IDR)
```

**Scorecard 3: Customization Revenue**
```
Field Name: Custom Revenue
Formula: SUM(biaya_custom)
Type: Currency (IDR)
```

**Bar Chart: Revenue Composition**
- Component: Stacked bar chart (100%)
- Dimension: Month
- Metrics: Product Sales, Shipping, Custom
- Show as percentage: Yes

#### 12. Payment Method Distribution

**Pie Chart:**
- Component: Pie chart
- Dimension: `metode_pembayaran`
- Metric: `SUM(total_pembayaran)`

**Table:**
- Dimensions: `metode_pembayaran`
- Metrics:
  1. `COUNT(id_transaksi)` - Transactions
  2. `SUM(total_pembayaran)` - Revenue
  3. `AVG(total_pembayaran)` - Avg Transaction
  4. Percentage of total

#### 13. Expense Details Table
- **Component**: Table with filters
- **Data source**: Biaya Operasional
- **Dimensions**:
  1. `tanggal` - Date
  2. `kategori_biaya` - Category
  3. `deskripsi` - Description
- **Metrics**:
  1. `jumlah` - Amount
- **Configuration**:
  - Rows per page: 25
  - Sort: Date descending
  - Enable filtering by category
  - Show totals at bottom

**Add summary row:**
- Enable table footer
- Show: Total expenses

---

## 📦 DASHBOARD 6: OPERATIONS & INVENTORY

### Layout Dashboard
```
┌─────────────────────────────────────────────────────┐
│  📦 Operations & Inventory Management               │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Total    │ Total    │ Stock    │ Stock    │ Filters │
│ Stock In │ Stock Out│ Turnover │ Adjustmt │         │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│ Stock Movement Trend (Line Chart - In vs Out)      │
├──────────────────────────────┬──────────────────────┤
│ Movement by Type             │ Movement by Category │
│ (Donut Chart)                │ (Bar Chart)          │
├──────────────────────────────┴──────────────────────┤
│ Top 10 Most Active Products (Bar Chart)            │
├──────────────────────────────────────────────────────┤
│ Transaction Type Analysis (Cards + Table)           │
├──────────────────────────────────────────────────────┤
│ Recent Stock Movements (Table with filters)        │
└─────────────────────────────────────────────────────┘
```

### Komponen Dashboard 6

#### 1. Filter Controls
**Filter 1: Period**
- Component: Date range control
- Field: `tanggal` (from Riwayat Stok)

**Filter 2: Transaction Type**
- Component: Drop-down list
- Field: `jenis_transaksi`
- Options: Penjualan, Pembelian, Penyesuaian, Retur

**Filter 3: Product Search**
- Component: Text filter
- Field: `nama_produk` (from blended data)

#### 2. KPI: Total Stock In
**Calculated Field:**
```
Field Name: Total Stock In
Formula: SUM(stok_masuk)
Type: Number
Data source: Riwayat Stok
```

- **Component**: Scorecard
- **Metric**: Total Stock In
- **Style**: Green background
- **Icon**: ⬆️ or arrow up

#### 3. KPI: Total Stock Out
**Calculated Field:**
```
Field Name: Total Stock Out
Formula: SUM(stok_keluar)
Type: Number
Data source: Riwayat Stok
```

- **Component**: Scorecard
- **Metric**: Total Stock Out
- **Style**: Blue background
- **Icon**: ⬇️ or arrow down

#### 4. KPI: Stock Turnover Rate
**Calculated Field:**
```
Field Name: Turnover Rate
Formula: SUM(stok_keluar) / SUM(stok_masuk)
Type: Number (2 decimals)
Suffix: "x"
```

- **Component**: Scorecard
- **Metric**: Turnover Rate
- **Style**: Purple background
- **Interpretation**: Higher = faster inventory movement

#### 5. KPI: Stock Adjustments
**Calculated Field:**
```
Field Name: Adjustment Count
Formula: COUNT(CASE WHEN jenis_transaksi = "Penyesuaian" THEN id_stok END)
Type: Number
```

- **Component**: Scorecard
- **Metric**: Adjustment Count
- **Style**: Orange background

#### 6. Stock Movement Trend (Line Chart)
- **Component**: Time series chart (dual line)
- **Data source**: Riwayat Stok
- **Dimension**: `tanggal` (by month or day)
- **Metrics**:
  - Line 1: `SUM(stok_masuk)` - Stock In (Green)
  - Line 2: `SUM(stok_keluar)` - Stock Out (Red)
- **Configuration**:
  - Smooth curves: Yes
  - Show legend: Bottom
  - Y-axis: Units
  - Show gridlines: Yes

#### 7. Movement by Type (Donut Chart)
**Calculated Field for Total Movement:**
```
Field Name: Total Movement
Formula: SUM(stok_masuk) + SUM(stok_keluar)
Type: Number
```

- **Component**: Donut chart
- **Data source**: Riwayat Stok
- **Dimension**: Movement Type (calculated)
- **Metric**: Units moved

**Create Movement Type dimension:**
```
Field Name: Movement Type
Formula: 
CASE 
  WHEN stok_masuk > 0 THEN "Stock In"
  WHEN stok_keluar > 0 THEN "Stock Out"
  ELSE "No Movement"
END
Type: Text
```

**Custom Colors:**
- Stock In: #22C55E (green)
- Stock Out: #EF4444 (red)

#### 8. Movement by Category
- **Component**: Bar chart (horizontal)
- **Data source**: Blend (Riwayat Stok + Produk)
- **Dimension**: `kategori` (from Master Produk)
- **Metric**: Total movement (calculated)

**Calculated Field:**
```
Field Name: Category Total Movement
Formula: SUM(stok_masuk + stok_keluar)
Type: Number
```

- **Configuration**:
  - Sort: Descending
  - Show data labels: Yes
  - Bar color: Blue gradient

#### 9. Top 10 Most Active Products
- **Component**: Bar chart
- **Data source**: Blend (Riwayat Stok + Produk)
- **Dimension**: `nama_produk`
- **Metric**: Total movement (calculated)
- **Configuration**:
  - Max rows: 10
  - Sort: Descending
  - Bar color: Purple gradient

**Steps:**
1. Add blend: Riwayat Stok + Master Produk (on id_produk)
2. Dimension: nama_produk
3. Metric: SUM(stok_masuk + stok_keluar)
4. Sort: Metric descending
5. Max rows: 10

#### 10. Transaction Type Analysis

**Scorecard Group (3 cards):**

**Card 1: Total Penjualan Transactions**
```
Field Name: Sales Transactions
Formula: COUNT(CASE WHEN jenis_transaksi = "Penjualan" THEN id_stok END)
Type: Number
Style: Blue background
```

**Card 2: Total Pembelian Transactions**
```
Field Name: Purchase Transactions
Formula: COUNT(CASE WHEN jenis_transaksi = "Pembelian" THEN id_stok END)
Type: Number
Style: Green background
```

**Card 3: Total Penyesuaian**
```
Field Name: Adjustment Transactions
Formula: COUNT(CASE WHEN jenis_transaksi = "Penyesuaian" THEN id_stok END)
Type: Number
Style: Orange background
```

**Transaction Type Details Table:**
- **Component**: Table
- **Data source**: Riwayat Stok
- **Dimension**: `jenis_transaksi`
- **Metrics**:
  1. `COUNT(id_stok)` - Transactions
  2. `SUM(stok_masuk)` - Stock In
  3. `SUM(stok_keluar)` - Stock Out
  4. Net Change (calculated)
- **Configuration**:
  - Show totals row
  - Heatmap on Stock In/Out columns

**Calculated Field: Net Change**
```
Field Name: Net Stock Change
Formula: SUM(stok_masuk) - SUM(stok_keluar)
Type: Number
```

#### 11. Recent Stock Movements Table
- **Component**: Table with detailed information
- **Data source**: Blend (Riwayat Stok + Produk)
- **Dimensions**:
  1. `tanggal` - Date
  2. `nama_produk` - Product
  3. `jenis_transaksi` - Type
- **Metrics**:
  1. Stock In (with conditional display)
  2. Stock Out (with conditional display)
  3. `stok_awal` - Before
  4. `stok_akhir` - After
- **Configuration**:
  - Rows per page: 50
  - Sort: Date descending
  - Enable search
  - Conditional formatting on movement columns

**Conditional Formatting:**
- Stock In > 0: Green text
- Stock Out > 0: Red text

**Table Columns Setup:**
1. Date: Format as DD/MM/YYYY
2. Product: Link to product details (optional)
3. Type: Badge style with colors:
   - Penjualan: Blue badge
   - Pembelian: Green badge
   - Penyesuaian: Orange badge
   - Retur: Red badge
4. Movement: Show +X or -X with colors
5. Stock Before/After: Number format

---

## 📢 DASHBOARD 7: MARKETING PERFORMANCE

### Layout Dashboard
```
┌─────────────────────────────────────────────────────┐
│  📢 Marketing Performance Dashboard                 │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Total    │ Total    │ Avg ROI  │ Total    │ Filters │
│ Campaign │ Spend    │          │ Reach    │         │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│ Campaign ROI Comparison (Bar Chart - Top 10)       │
├──────────────────────────────┬──────────────────────┤
│ Spend by Platform            │ Conversion Rate      │
│ (Donut Chart)                │ by Platform (Bar)    │
├──────────────────────────────┼──────────────────────┤
│ Campaign Status Distribution │ ROI Trend Over Time  │
│ (Pie Chart)                  │ (Line Chart)         │
├──────────────────────────────────────────────────────┤
│ Top 5 Campaigns by ROI (Detailed Cards)            │
├──────────────────────────────────────────────────────┤
│ All Marketing Campaigns (Table with metrics)       │
└─────────────────────────────────────────────────────┘
```

### Komponen Dashboard 7

#### 1. Filter Controls
**Filter 1: Period**
- Component: Date range control
- Field: `tanggal_mulai` (campaign start date)

**Filter 2: Platform**
- Component: Drop-down list
- Field: `platform`
- Multi-select: Yes
- Options: Google Ads, Instagram Ads, TikTok Ads, Facebook Ads

**Filter 3: Status**
- Component: Drop-down list
- Field: Campaign Status (calculated)
- Options: Active, Completed

#### 2. KPI: Total Campaigns
- **Component**: Scorecard
- **Data source**: Marketing Campaign
- **Metric**: `COUNT(id_campaign)`
- **Add metric**: Active campaigns count
- **Style**: Green background

**Calculated Field: Active Campaigns**
```
Field Name: Active Campaigns
Formula: COUNT(CASE WHEN tanggal_selesai >= TODAY() THEN id_campaign END)
Type: Number
```

#### 3. KPI: Total Marketing Spend
- **Component**: Scorecard
- **Data source**: Marketing Campaign
- **Metric**: `SUM(budget)`
- **Format**: Currency (IDR)
- **Style**: Blue background
- **Comparison**: Previous period spend

#### 4. KPI: Average ROI
**Calculated Field:**
```
Field Name: Average ROI
Formula: AVG(roi)
Type: Number (1 decimal)
Suffix: ""
Note: ROI is already in the data, not percentage
```

- **Component**: Scorecard
- **Metric**: Average ROI
- **Format**: Number with 1 decimal
- **Style**: Purple background
- **Conditional color**: 
  - Green if > 0
  - Red if < 0

#### 5. KPI: Total Reach/Impressions
- **Component**: Scorecard
- **Data source**: Marketing Campaign
- **Metric**: `SUM(reach)`
- **Format**: Compact numbers (K, M)
- **Style**: Orange background

#### 6. Campaign ROI Comparison (Bar Chart)
- **Component**: Bar chart (horizontal)
- **Data source**: Marketing Campaign
- **Dimension**: `nama_campaign`
- **Metric**: `roi`
- **Configuration**:
  - Max rows: 10
  - Sort: ROI descending
  - Bar color: Conditional
    - Green if ROI > 0
    - Red if ROI < 0
  - Show data labels: Yes
  - IndexAxis: Y (horizontal bars)

**Alternative: Show as ROI with campaign details**
```
Display format: 
"Campaign Name: ROI Value"
Example: "Promo Tahun Baru: 19,914,214.25"
```

#### 7. Spend by Platform (Donut Chart)
- **Component**: Donut chart
- **Data source**: Marketing Campaign
- **Dimension**: `platform`
- **Metric**: `SUM(budget)`
- **Configuration**:
  - Donut hole: 50%
  - Show percentages: Yes
  - Show legend: Bottom

**Custom Colors:**
- Google Ads: #4285F4 (Google blue)
- Instagram Ads: #E4405F (Instagram pink)
- TikTok Ads: #000000 (Black)
- Facebook Ads: #1877F2 (Facebook blue)

#### 8. Conversion Rate by Platform
- **Component**: Bar chart
- **Data source**: Marketing Campaign
- **Dimension**: `platform`
- **Metric**: Conversion Rate (calculated)

**Calculated Field: Conversion Rate**
```
Field Name: Conversion Rate
Formula: (SUM(conversion) / SUM(engagement)) * 100
Type: Percent
```

- **Configuration**:
  - Sort: Descending
  - Y-axis: Percentage (0-100%)
  - Bar color: Blue
  - Show data labels: Yes with % symbol

#### 9. Campaign Status Distribution
**First, create Status calculated field:**
```
Field Name: Campaign Status
Formula: 
CASE 
  WHEN tanggal_selesai >= TODAY() THEN "Active"
  ELSE "Completed"
END
Type: Text
```

- **Component**: Pie chart
- **Dimension**: Campaign Status
- **Metric**: `COUNT(id_campaign)`
- **Colors**:
  - Active: #22C55E (green)
  - Completed: #3B82F6 (blue)

#### 10. ROI Trend Over Time
- **Component**: Line chart (area chart optional)
- **Data source**: Marketing Campaign
- **Dimension**: `tanggal_mulai` (by month)
- **Metrics**:
  - Average ROI per month
  - Total budget per month (secondary axis)
- **Configuration**:
  - Smooth curve: Yes
  - Show reference line at ROI = 0
  - Line color: Green if above 0, Red if below

**Calculated Fields for Monthly Aggregation:**
```
Field Name: Monthly Avg ROI
Formula: AVG(roi)
Group by: MONTH(tanggal_mulai)
Type: Number
```

#### 11. Platform Performance Metrics Table
- **Component**: Table
- **Data source**: Marketing Campaign
- **Dimension**: `platform`
- **Metrics**:
  1. `COUNT(id_campaign)` - Campaigns
  2. `SUM(budget)` - Total Spend
  3. `SUM(reach)` - Total Reach
  4. `SUM(engagement)` - Engagement
  5. `SUM(conversion)` - Conversions
  6. `AVG(roi)` - Avg ROI
  7. CPM (calculated)
  8. CPC (calculated)

**Calculated Field: CPM (Cost Per Mille)**
```
Field Name: CPM
Formula: (SUM(budget) / SUM(reach)) * 1000
Type: Currency (IDR)
```

**Calculated Field: CPC (Cost Per Click)**
```
Field Name: CPC
Formula: SUM(budget) / SUM(engagement)
Type: Currency (IDR)
```

- **Configuration**:
  - Sort: By total spend descending
  - Heatmap: On ROI column
  - Show totals: Yes

#### 12. Top 5 Campaigns by ROI (Scorecard Cards)

**Create 5 separate scorecards or use a table with detailed view:**

**Option A: Scorecard Grid**
- Create 5 scorecards arranged in a grid
- Each shows: Campaign name, ROI value, Budget, Conversions
- Sort by ROI descending
- Use filter: Top 5

**Option B: Detailed Cards Table**
- **Component**: Table with rich formatting
- **Data source**: Marketing Campaign
- **Dimensions**:
  1. Rank (row number)
  2. `nama_campaign`
  3. `platform`
- **Metrics**:
  1. `budget` - Budget
  2. `reach` - Reach
  3. `conversion` - Conversions
  4. `roi` - ROI
  5. Conversion Rate (calculated)
- **Configuration**:
  - Max rows: 5
  - Sort: ROI descending
  - Add ranking badge/number
  - Use heatmap on ROI

**Add visual elements:**
- Row 1: 🥇 Gold background
- Row 2: 🥈 Silver background
- Row 3: 🥉 Bronze background
- Rows 4-5: Standard styling

#### 13. All Marketing Campaigns Table
- **Component**: Table with pagination
- **Data source**: Marketing Campaign
- **Dimensions**:
  1. `nama_campaign` - Campaign
  2. `platform` - Platform
  3. Campaign Period (calculated)
  4. Campaign Status
- **Metrics**:
  1. `budget` - Budget
  2. `reach` - Reach
  3. `engagement` - Engagement
  4. `conversion` - Conversions
  5. `roi` - ROI
- **Configuration**:
  - Rows per page: 25
  - Enable sorting on all columns
  - Enable search
  - Conditional formatting on ROI

**Calculated Field: Campaign Period**
```
Field Name: Campaign Period
Formula: 
CONCAT(
  TEXT(tanggal_mulai, "DD/MM/YYYY"), 
  " - ", 
  TEXT(tanggal_selesai, "DD/MM/YYYY")
)
Type: Text
```

**Calculated Field: Campaign Duration**
```
Field Name: Duration (Days)
Formula: DATE_DIFF(tanggal_selesai, tanggal_mulai)
Type: Number
```

**Conditional Formatting:**
- ROI > 100,000: Dark green background
- ROI > 0: Light green background
- ROI < 0: Red background
- ROI = 0: Gray background

**Add Interactive Features:**
1. Click on campaign → Opens detailed view
2. Filter by platform chips
3. Search by campaign name
4. Export to CSV option

---

## 🎨 TIPS & BEST PRACTICES

### 1. Design & Layout Best Practices

#### A. Color Palette Consistency
**Primary Colors:**
- Success/Positive: #22C55E (Green)
- Primary/Info: #3B82F6 (Blue)
- Warning: #F59E0B (Orange)
- Danger/Negative: #EF4444 (Red)
- Neutral: #6B7280 (Gray)
- Premium: #9333EA (Purple)

**Use cases:**
- Revenue/Profit/Positive metrics: Green
- Costs/Expenses: Blue
- Alerts/Low stock: Orange
- Errors/Negative: Red
- Customer data: Purple

#### B. Typography Guidelines
- **Headers**: Roboto Bold, 18-24pt
- **KPI Values**: Roboto Bold, 32-48pt
- **Labels**: Roboto Regular, 12-14pt
- **Table text**: Roboto Regular, 11-12pt

#### C. Layout Structure
```
Recommended layout flow:
1. Header (title + logo)
2. Filter controls (top right)
3. KPI cards (4-5 in a row)
4. Main charts (2 columns max)
5. Detailed tables (full width)
6. Footer (date range, refresh info)
```

**Spacing:**
- Between sections: 16-24px
- Between charts: 12-16px
- Card padding: 16px
- Chart margins: 12px

### 2. Data Source Optimization

#### A. Refresh Schedule
**In Looker Studio:**
1. Go to Resource > Manage added data sources
2. Set refresh schedule:
   - Daily: 00:00 AM (midnight)
   - Weekly: Sunday 00:00 AM
   - Or: On-demand only

**For Google Sheets:**
- Data updates automatically when sheet is edited
- Max 100 queries per 100 seconds per user
- Consider caching for large datasets

#### B. Blended Data Best Practices
- Always use LEFT OUTER JOIN for transactions + master data
- Primary table: Transactions (left)
- Secondary table: Master data (right)
- Join on indexed columns (id_produk, id_pelanggan)

**Blend naming convention:**
```
[Primary Table] + [Secondary Table]
Example: "Transaksi + Produk"
```

#### C. Calculated Fields Organization
**Create folder structure:**
- 📁 Revenue Metrics
  - Total Revenue
  - Gross Sales
  - Net Sales
- 📁 Cost Metrics
  - COGS
  - Operational Costs
  - Total Costs
- 📁 Profit Metrics
  - Gross Profit
  - Net Profit
  - Margins
- 📁 Customer Metrics
  - Customer LTV
  - Repeat Rate
  - Segments
- 📁 Date Calculations
  - Day of Week
  - Month Name
  - Quarter
  - Year

### 3. Performance Optimization

#### A. Chart Optimization
- **Limit rows displayed**: Max 20-50 rows per chart
- **Use aggregation**: Don't show raw data unless necessary
- **Simplify visualizations**: Avoid 3D charts, fancy animations
- **Cache data**: Enable data caching in data source settings

#### B. Table Performance
- **Pagination**: 20-25 rows per page
- **Conditional formatting**: Use sparingly (max 3 rules per table)
- **Blending**: Minimize number of blends (max 2 tables per blend)

#### C. Dashboard Loading
- **Lazy loading**: Enable in dashboard settings
- **Limit charts per page**: Max 10-12 charts per dashboard
- **Use summary pages**: Link to detailed pages instead of one massive dashboard

### 4. Filter Controls Best Practices

#### A. Filter Hierarchy
**Recommended order (top to bottom):**
1. **Period/Date Range** - Most frequently used
2. **Category/Dimension** - Second level filter
3. **Status/Type** - Third level filter
4. **Search** - Last resort filter

#### B. Default Values
- Date range: Last 365 days or Last 12 months
- Category: "All" selected
- Status: "All" selected
- Enable "Include All" option

#### C. Filter Display
- Use **dropdown** for 3-10 options
- Use **checkbox list** for multi-select with < 8 options
- Use **search box** for large lists (> 50 items)
- Use **slider** for numeric ranges

### 5. Calculated Fields Reference

#### Essential Date Functions
```javascript
// Day of Week
WEEKDAY(tanggal_field)

// Month Name
TEXT(tanggal_field, "MMMM")

// Quarter
CONCAT("Q", QUARTER(tanggal_field))

// Year-Month
TEXT(tanggal_field, "YYYY-MM")

// Days Difference
DATE_DIFF(date1, date2)

// Today
TODAY()
```

#### Essential Aggregation Functions
```javascript
// Sum with condition
SUM(CASE WHEN condition THEN field END)

// Count Distinct
COUNT_DISTINCT(field)

// Average
AVG(field)

// Percentage
(SUM(field) / SUM(total)) * 100

// Growth Rate
((current - previous) / previous) * 100
```

#### Text Functions
```javascript
// Concatenate
CONCAT(field1, " - ", field2)

// Text formatting
TEXT(field, "format")

// Upper/Lower case
UPPER(field)
LOWER(field)

// Substring
SUBSTR(field, start, length)
```

### 6. Sharing & Collaboration

#### A. Sharing Options
**View Access:**
- Share link: Anyone with link can view
- Embed: Embed in website/presentation
- PDF Export: Schedule email delivery

**Edit Access:**
- Collaborators can edit dashboard
- Limit to specific Google accounts

#### B. Embed Settings
```html
<!-- Responsive embed -->
<iframe 
  width="100%" 
  height="600" 
  src="https://lookerstudio.google.com/embed/reporting/..."
  frameborder="0" 
  style="border:0" 
  allowfullscreen>
</iframe>
```

#### C. PDF Delivery Schedule
1. Share > Schedule delivery
2. Recipients: Enter emails
3. Schedule: Daily/Weekly/Monthly
4. Time: Set delivery time
5. Attachment: PDF format

### 7. Mobile Optimization

#### A. Mobile Layout
- **Single column layout** for mobile
- **Stacked KPI cards** (1 per row)
- **Simplified charts** (fewer data points)
- **Hide complex tables** on mobile
- **Larger touch targets** (min 44x44px)

#### B. Responsive Design
- Set canvas width: 1200px (desktop)
- Enable responsive mode
- Test on different devices
- Use relative sizing (%) instead of fixed (px)

### 8. Common Issues & Solutions

#### Issue 1: Blend Returns No Data
**Solution:**
- Check join keys match exactly
- Verify data types (text vs number)
- Use LEFT OUTER JOIN, not INNER
- Check for null values in join keys

#### Issue 2: Slow Loading Dashboard
**Solution:**
- Reduce number of charts (split to multiple pages)
- Enable data caching
- Optimize calculated fields
- Use date range filters
- Aggregate data before blending

#### Issue 3: Incorrect Calculations
**Solution:**
- Check aggregation type (SUM vs AVG)
- Verify filter scope
- Test calculated fields separately
- Use parentheses in complex formulas

#### Issue 4: Date Filter Not Working
**Solution:**
- Ensure field type is "Date"
- Format: DD/MM/YYYY or YYYY-MM-DD
- Check for invalid dates
- Use TEXT() to convert if needed

### 9. Documentation Checklist

#### For Each Dashboard, Document:
- ✅ Purpose and target audience
- ✅ Data sources used
- ✅ Blend definitions
- ✅ Calculated fields formulas
- ✅ Filter dependencies
- ✅ Update schedule
- ✅ Known limitations
- ✅ Change log

#### Naming Conventions:
- **Dashboards**: "[Company] - [Topic] Dashboard"
- **Data sources**: "[Source] - [Date]"
- **Calculated fields**: "[Metric Name]" (descriptive)
- **Blends**: "[Table1] + [Table2]"

### 10. Maintenance Schedule

#### Daily:
- ✅ Check data refresh status
- ✅ Monitor error logs
- ✅ Review alert notifications

#### Weekly:
- ✅ Validate key metrics accuracy
- ✅ Update calculated fields if needed
- ✅ Check user feedback

#### Monthly:
- ✅ Review performance metrics
- ✅ Optimize slow-loading pages
- ✅ Archive old data
- ✅ Update documentation

#### Quarterly:
- ✅ Stakeholder review
- ✅ Add new features/charts
- ✅ Remove unused dashboards
- ✅ Security audit

---

## 📚 REFERENSI & RESOURCES

### Official Documentation
- [Looker Studio Help Center](https://support.google.com/looker-studio)
- [Calculated Fields Reference](https://support.google.com/looker-studio/table/6379764)
- [Data Blending Guide](https://support.google.com/looker-studio/answer/9061420)

### Video Tutorials
- Looker Studio Official YouTube Channel
- Google Analytics Academy

### Community
- [Looker Studio Community Forum](https://support.google.com/looker-studio/community)
- Reddit: r/LookerStudio
- Stack Overflow: [looker-studio] tag

### Best Practices Articles
- Google Cloud Blog - Looker Studio tips
- Supermetrics Blog - Dashboard design
- Analytics Mania - Looker Studio tutorials

---

## ✅ CHECKLIST IMPLEMENTASI

### Phase 1: Persiapan (Week 1)
- [ ] Upload semua CSV ke Google Sheets (6 files)
- [ ] Format data (dates, numbers, text)
- [ ] Verifikasi tidak ada data kosong
- [ ] Buat backup dari semua sheets

### Phase 2: Setup Looker Studio (Week 2)
- [ ] Buat report baru di Looker Studio
- [ ] Connect ke 6 Google Sheets
- [ ] Setup 3 blended data sources
- [ ] Test koneksi data
- [ ] Buat semua calculated fields dasar

### Phase 3: Dashboard 1-3 (Week 3-4)
- [ ] Dashboard 1: Executive Summary
- [ ] Dashboard 2: Sales Analysis
- [ ] Dashboard 3: Product Performance
- [ ] Test filters dan interactivity
- [ ] Review dengan stakeholder

### Phase 4: Dashboard 4-5 (Week 5-6)
- [ ] Dashboard 4: Customer Analytics
- [ ] Dashboard 5: Financial Analysis
- [ ] Optimize performance
- [ ] Add drill-down features

### Phase 5: Dashboard 6-7 (Week 7-8)
- [ ] Dashboard 6: Operations & Inventory
- [ ] Dashboard 7: Marketing Performance
- [ ] Final testing
- [ ] Mobile optimization

### Phase 6: Finalisasi (Week 9)
- [ ] Complete documentation
- [ ] User training
- [ ] Setup scheduled emails
- [ ] Launch & monitor

---

## 🎓 TIPS UNTUK PRESENTASI

### Struktur Presentasi
1. **Opening (5 min)**
   - Problem statement
   - Business objectives
   - Data sources overview

2. **Dashboard Demo (10 min)**
   - Executive Summary (2 min)
   - Sales & Products (3 min)
   - Customers & Financial (3 min)
   - Operations & Marketing (2 min)

3. **Key Insights (3 min)**
   - Top 3 findings from data
   - Business recommendations
   - ROI/Impact projection

4. **Q&A (2 min)**

### Demo Tips
- ✅ Start with Executive Dashboard (big picture)
- ✅ Show filter interactivity
- ✅ Highlight 2-3 key insights per dashboard
- ✅ Explain business value, not just features
- ✅ Have backup screenshots (in case of connection issues)

### Talking Points
**Executive Dashboard:**
- "Total revenue Rp XXX with X% growth"
- "Top selling category is X with Y% market share"
- "Peak sales on [day/month]"

**Customer Analytics:**
- "X% are repeat customers (loyalty indicator)"
- "VIP segment generates Y% of revenue"
- "Geographic concentration in [cities]"

**Financial Analysis:**
- "Gross margin X%, Net margin Y%"
- "Top expense category: [category]"
- "Profitability trend: [increasing/stable/decreasing]"

**Marketing Performance:**
- "Best ROI platform: X with Y return"
- "Campaign Z generated Rp XX with ROI of YY"
- "Conversion rate: X%"

---

## 🏆 KRITERIA PENILAIAN (Sesuai Brief)

### A. Ketepatan Waktu (20%)
- ✅ Submit sesuai deadline
- ✅ Lengkap semua deliverables

### B. Laporan Tertulis (30%)
- ✅ Sistematika sesuai outline
- ✅ Bahasa Indonesia yang baik dan benar
- ✅ Konsistensi istilah dan format
- ✅ Referensi dengan Mendeley (APA/IEEE)
- ✅ Lampiran lengkap (dataset, screenshots)

### C. Slide Presentasi (20%)
- ✅ Jelas dan konsisten
- ✅ Font mudah dibaca
- ✅ Gambar relevan dan berkualitas
- ✅ Flow logis

### D. Presentasi & Demo (30%)
- ✅ Bahasa komunikatif
- ✅ Penguasaan materi
- ✅ Dashboard interaktif dan berfungsi
- ✅ Pengendalian waktu (15 menit)
- ✅ Pengendalian media presentasi

---

## 📝 PENUTUP

Dashboard Looker Studio untuk SATRIAMART ini dirancang untuk memberikan insights menyeluruh tentang:
- 💰 Financial performance
- 📊 Sales effectiveness
- 📦 Product performance
- 👥 Customer behavior
- 📢 Marketing ROI
- 🏭 Operational efficiency

**Key Success Factors:**
1. Data quality dan akurasi
2. User-friendly design
3. Actionable insights
4. Regular updates
5. Stakeholder alignment

**Next Steps After Implementation:**
1. Schedule regular reviews (weekly/monthly)
2. Gather user feedback
3. Iterate and improve
4. Expand to real-time data sources
5. Integrate with other tools (ERP, CRM)

---

**Good luck dengan implementasi dashboard Looker Studio Anda! 🚀**

Jika ada pertanyaan atau butuh klarifikasi, jangan ragu untuk bertanya.

---

*Document Version: 1.0*  
*Last Updated: November 2025*  
*Created for: SATRIAMART Business Intelligence Project*  
*Course: Business Intelligence II - Universitas Negeri Makassar*
