# 📊 PANDUAN LENGKAP IMPLEMENTASI DASHBOARD BUSINESS INTELLIGENCE SATRIAMART

## Daftar Isi
- [Pendahuluan](#pendahuluan)
- [Requirements](#requirements)
- [Tahap 1: Persiapan Data](#tahap-1-persiapan-data)
- [Tahap 2: Upload ke Google Sheets](#tahap-2-upload-ke-google-sheets)
- [Tahap 3: Setup Looker Studio](#tahap-3-setup-looker-studio)
- [Tahap 4: Membuat Dashboard](#tahap-4-membuat-dashboard)
- [Tahap 5: Testing & Deployment](#tahap-5-testing--deployment)
- [Troubleshooting](#troubleshooting)

---

## Pendahuluan

Panduan ini memberikan langkah-langkah detail untuk mengimplementasikan dashboard Business Intelligence interaktif untuk SATRIAMART menggunakan Looker Studio dan Google Sheets.

**Estimasi Waktu Total**: 8-12 jam
- Persiapan Data: 2-3 jam
- Setup & Upload: 1-2 jam
- Pembuatan Dashboard: 4-6 jam
- Testing & Refinement: 1-2 jam

---

## Requirements

### 1. Akun yang Diperlukan
- ✅ Google Account (Gmail)
- ✅ Google Sheets access
- ✅ Looker Studio access (lookerstudio.google.com)

### 2. Software/Tools
- ✅ Web Browser (Chrome recommended)
- ✅ Spreadsheet software (Excel, Google Sheets, atau LibreOffice)
- ✅ Text editor untuk edit CSV
- ✅ (Optional) Python 3.x untuk data generation

### 3. Skills Prerequisites
- ✅ Basic spreadsheet skills
- ✅ Basic understanding of data visualization
- ✅ Familiar dengan Google products
- ❌ Tidak perlu coding skills (for basic implementation)

### 4. Data Files yang Dibutuhkan
- ✅ `01_master_produk.csv` (50 products)
- ✅ `02_master_pelanggan.csv` (180 customers)
- ✅ `03_transaksi_penjualan.csv` (320 transactions)
- ✅ (Optional) `04_riwayat_stok.csv`
- ✅ (Optional) `05_biaya_operasional.csv`
- ✅ (Optional) `06_marketing_campaign.csv`

---

## Tahap 1: Persiapan Data

### Step 1.1: Generate atau Prepare Data

**Opsi A: Gunakan Data yang Sudah Ada**
```bash
cd /var/www/unm-s7/tugas-selesai/05_business_intelligence/data
ls -l *.csv
```

**Opsi B: Generate Data Baru (jika diperlukan)**
```bash
python3 generate_all_data.py
```

### Step 1.2: Validasi Data Quality

Buka setiap CSV file dan check:

1. **Header Row**: Pastikan row pertama adalah column names
2. **Data Types**: 
   - Tanggal format: YYYY-MM-DD
   - Angka: tanpa formatting (no currency symbol, no thousand separator)
   - Text: proper case, no special characters yang aneh
3. **Missing Values**: Replace empty cells dengan:
   - Numeric: 0
   - Text: "Unknown" atau "-"
4. **Encoding**: Save as UTF-8 encoding

### Step 1.3: Data Cleaning Checklist

Gunakan spreadsheet software untuk check:

**Master Produk:**
- ✅ Semua id_produk unique (P001-P050)
- ✅ Harga jual > harga modal
- ✅ Stok >= 0
- ✅ Kategori konsisten

**Master Pelanggan:**
- ✅ Semua id_pelanggan unique (C001-C180)
- ✅ Email format valid
- ✅ Nomor telepon format konsisten
- ✅ Kota ada di list yang valid

**Transaksi Penjualan:**
- ✅ id_transaksi unique (TRX0001-TRX0320)
- ✅ id_pelanggan exists di master_pelanggan
- ✅ id_produk exists di master_produk
- ✅ total_pembayaran = subtotal - diskon + biaya_custom + ongkir
- ✅ Tanggal dalam range Nov 2024 - Okt 2025

---

## Tahap 2: Upload ke Google Sheets

### Step 2.1: Create New Google Spreadsheet

1. Buka https://sheets.google.com
2. Click **Blank** untuk create new spreadsheet
3. Rename spreadsheet: "SATRIAMART BI Data"

### Step 2.2: Import CSV Files

**Untuk setiap CSV file:**

1. Click **File** → **Import**
2. Tab **Upload** → **Browse** atau drag file
3. Import settings:
   - **Import location**: "Insert new sheet(s)"
   - **Separator type**: "Comma"
   - **Convert text to numbers, dates**: ✅ Yes
4. Click **Import data**
5. Rename sheet sesuai nama file (tanpa extension):
   - `01_master_produk` → rename ke `master_produk`
   - `02_master_pelanggan` → rename ke `master_pelanggan`
   - `03_transaksi_penjualan` → rename ke `transaksi_penjualan`

### Step 2.3: Format Data di Google Sheets

**Master Produk Sheet:**
1. Select column `harga_jual` dan `harga_modal`
2. Format → Number → Currency (Rp)
3. Select column `tanggal_dibuat` dan `tanggal_update`
4. Format → Number → Date

**Master Pelanggan Sheet:**
1. Select column `total_nilai_pembelian`
2. Format → Number → Currency (Rp)
3. Select column `tanggal_registrasi`
4. Format → Number → Date

**Transaksi Penjualan Sheet:**
1. Select columns dengan nilai currency: `harga_satuan`, `subtotal`, `diskon_nominal`, `biaya_custom`, `biaya_ongkir`, `total_pembayaran`
2. Format → Number → Currency (Rp)
3. Select column `tanggal_transaksi` dan `tanggal_selesai`
4. Format → Number → Date time (for transaksi) / Date (for selesai)

### Step 2.4: Create Calculated Fields (Optional)

Buat sheet baru bernama `calculated_metrics`:

**Revenue Summary:**
```
=QUERY(transaksi_penjualan!A:T, 
  "SELECT YEAR(B), MONTH(B), SUM(L) 
   WHERE B IS NOT NULL 
   GROUP BY YEAR(B), MONTH(B) 
   ORDER BY YEAR(B), MONTH(B)")
```

**Product Performance:**
```
=QUERY(transaksi_penjualan!A:T, 
  "SELECT D, COUNT(D), SUM(E), SUM(L) 
   WHERE D IS NOT NULL 
   GROUP BY D 
   ORDER BY SUM(L) DESC")
```

### Step 2.5: Share Settings

1. Click **Share** button (top right)
2. Change **General Access** ke "Anyone with the link" → **Viewer**
3. Copy spreadsheet URL untuk digunakan di Looker Studio

---

## Tahap 3: Setup Looker Studio

### Step 3.1: Access Looker Studio

1. Buka https://lookerstudio.google.com
2. Sign in dengan Google Account yang sama
3. Accept Terms of Service jika first time

### Step 3.2: Create Data Source

**Untuk Master Produk:**

1. Click **Create** → **Data Source**
2. Pilih **Google Sheets** connector
3. Select spreadsheet: "SATRIAMART BI Data"
4. Select worksheet: `master_produk`
5. Click **Connect**
6. Di Field Configuration:
   - Rename data source: "Master Produk"
   - Verify field types:
     * `id_produk`: Text
     * `harga_jual`: Currency (Rp)
     * `harga_modal`: Currency (Rp)
     * `stok_tersedia`: Number
     * `tanggal_dibuat`: Date
   - Create calculated field `profit`:
     ```
     harga_jual - harga_modal
     ```
   - Create calculated field `profit_margin_pct`:
     ```
     (harga_jual - harga_modal) / harga_jual * 100
     ```
7. Click **Create Report** (atau **Save** jika sudah ada report)

**Ulangi untuk Data Sources lain:**
- Master Pelanggan
- Transaksi Penjualan
- Riwayat Stok (optional)
- Biaya Operasional (optional)
- Marketing Campaign (optional)

### Step 3.3: Create Blended Data Source

Untuk join multiple tables:

1. **Blend: Transaksi + Produk**
   - Create → Data Source → Blend data
   - Add data source: Transaksi Penjualan
   - Join another table: Master Produk
   - Join configuration:
     * Left table: `id_produk`
     * Right table: `id_produk`
     * Join operator: Left outer join
   - Select fields to include dari both tables
   - Save as "Transaksi with Product Details"

2. **Blend: Transaksi + Pelanggan**
   - Similar process
   - Join on `id_pelanggan`
   - Save as "Transaksi with Customer Details"

---

## Tahap 4: Membuat Dashboard

### Step 4.1: Create New Report

1. Click **Create** → **Report**
2. Pilih data source: "Transaksi Penjualan" (atau blended source)
3. Click **Add to Report**
4. Canvas akan terbuka

### Step 4.2: Setup Report Properties

1. **File** → **Rename**: "SATRIAMART BI Dashboard"
2. **File** → **Page Settings**:
   - Canvas size: 1600 x 1200 (Desktop) atau Custom
   - Grid settings: Enable grid untuk alignment
3. **Theme and Layout**:
   - Click **Theme** (top toolbar)
   - Choose simple theme atau customize colors

### Step 4.3: Create Page 1 - Executive Summary

**A. Add Header:**

1. **Insert** → **Text**
2. Type: "SATRIAMART Business Intelligence Dashboard"
3. Font: Roboto Bold, Size: 24pt, Color: #2E7D32
4. Position: Top center

**B. Add Logo (Optional):**

1. **Insert** → **Image**
2. Upload logo SATRIAMART atau logo UNM
3. Position: Top left

**C. Add Date Range Control:**

1. **Add a control** → **Date range control**
2. Position: Top right
3. Properties:
   - Auto date range: Last 365 days
   - Allow comparison: Yes

**D. Add KPI Scorecards:**

1. **Add a chart** → **Scorecard**
2. Data source: Transaksi Penjualan
3. Metric: SUM(total_pembayaran)
4. Properties:
   - Label: "Total Revenue"
   - Number format: Currency (Rp)
   - Comparison: Previous period
   - Compact numbers: No
5. Style:
   - Font size: 32pt for metric
   - Background color: White
   - Border: 1px solid #E0E0E0
   - Border radius: 8px
6. Position: Below header, first card

**Repeat for other KPIs:**
- Total Transaksi: COUNT(id_transaksi)
- Total Pelanggan: COUNT_DISTINCT(id_pelanggan)
- Average Order Value: AVG(total_pembayaran)
- Profit Margin: Calculated field
- Growth Rate: Calculated field with comparison

**E. Add Revenue Trend Chart:**

1. **Add a chart** → **Time series chart**
2. Data source: Transaksi Penjualan
3. Dimension: tanggal_transaksi (Month)
4. Metric: SUM(total_pembayaran)
5. Properties:
   - Chart type: Line chart
   - Show data labels: No
   - Line style: Smooth
   - Missing data: Linear interpolation
6. Style:
   - Line color: #2E7D32
   - Line thickness: 2px
   - Point style: Filled circle
   - Background: White
7. Position: Center, large chart

**F. Add Revenue by Channel Chart:**

1. **Add a chart** → **Bar chart**
2. Data source: Transaksi Penjualan
3. Dimension: channel_penjualan
4. Metric: SUM(total_pembayaran)
5. Sort: Metric descending
6. Properties:
   - Orientation: Horizontal
   - Show data labels: Yes
   - Bar chart styling: Rounded corners
7. Style:
   - Bar color: By dimension (multi-color)
   - Color palette: Custom (Green, Gold, Blue, Gray)

**G. Add Revenue by Category Chart:**

1. **Add a chart** → **Pie chart**
2. Data source: Blend "Transaksi with Product Details"
3. Dimension: kategori (from master_produk)
4. Metric: SUM(total_pembayaran)
5. Properties:
   - Donut hole: 50%
   - Show data labels: Percent of total
   - Legend position: Right
6. Style:
   - Slice colors: Custom colors

### Step 4.4: Add Interactivity

**A. Add Filters:**

1. **Add a control** → **Drop-down list**
2. Control field: channel_penjualan
3. Properties:
   - Label: "Filter by Channel"
   - Allow multiple selections: Yes
   - Include "All" option: Yes
4. Position: Top section

**B. Setup Cross-filtering:**

1. Select a chart (e.g., Bar chart)
2. Right click → **Cross-filtering**
3. Enable: "Apply filter"
4. This allows clicking bar to filter other charts

**C. Add Drill-down:**

1. Select chart
2. Properties → **Interactions**
3. Enable drill-down: Kategori → Sub-kategori → Produk

### Step 4.5: Create Additional Pages

**Create Page 2 - Sales Analysis:**

1. Click **Page** → **New page**
2. Name: "Sales Analysis"
3. Copy header dan controls dari Page 1 (Ctrl+C, Ctrl+V)
4. Add specific charts:
   - Top 10 Products by Revenue (Bar chart)
   - Top 10 Products by Quantity (Bar chart)
   - Sales by Day of Week (Bar chart)
   - Sales by Hour (Line chart)
   - Transactions detail table

**Create Pages 3-7:**

Ulangi proses untuk:
- Page 3: Product Performance
- Page 4: Customer Analysis
- Page 5: Operational Metrics
- Page 6: Financial Analysis
- Page 7: Marketing Performance

### Step 4.6: Add Navigation

**Option A: Page Navigation Control:**

1. **Add a control** → **Page navigation**
2. Style:
   - Position: Top (horizontal tabs)
   - Style: Tabs dengan icon
   - Color: Match theme

**Option B: Custom Navigation Buttons:**

1. Create text atau image untuk each page
2. Add hyperlink: Click text → **Insert link** → **Page in this report**
3. Style as buttons dengan background color

---

## Tahap 5: Testing & Deployment

### Step 5.1: Functional Testing

**Test Checklist:**

✅ **Data Accuracy:**
- [ ] KPI values match source data
- [ ] Calculated fields correct
- [ ] Aggregations working properly
- [ ] Date ranges filtering correctly

✅ **Interactivity:**
- [ ] Date picker updates all charts
- [ ] Filter controls work
- [ ] Cross-filtering between charts works
- [ ] Drill-down functional
- [ ] Page navigation smooth

✅ **Visualizations:**
- [ ] All charts rendering properly
- [ ] No error messages
- [ ] Tooltips showing correct info
- [ ] Data labels readable
- [ ] Colors consistent

✅ **Performance:**
- [ ] Page loads in < 5 seconds
- [ ] Charts render smoothly
- [ ] No lag when filtering
- [ ] Responsive on mobile

### Step 5.2: User Acceptance Testing

1. Share draft dashboard dengan stakeholder
2. Collect feedback tentang:
   - Ease of use
   - Information completeness
   - Visual design
   - Missing features
3. Iterate berdasarkan feedback

### Step 5.3: Browser Testing

Test di multiple browsers:
- ✅ Chrome (primary)
- ✅ Firefox
- ✅ Safari
- ✅ Edge

### Step 5.4: Device Testing

Test di different devices:
- ✅ Desktop (1920x1080)
- ✅ Laptop (1366x768)
- ✅ Tablet (iPad)
- ✅ Mobile (iPhone, Android)

### Step 5.5: Deployment

**Step A: Finalize Dashboard**
1. Review semua pages
2. Fix any issues found during testing
3. Add final touches (descriptions, annotations)

**Step B: Setup Sharing**
1. Click **Share** button
2. **Manage access**:
   - Add specific people (with edit/view rights)
   - OR Get shareable link dengan view access
3. **Schedule email delivery** (optional):
   - Setup weekly/monthly email reports
   - Select recipients

**Step C: Create Documentation**
1. Create user guide document
2. Record video tutorial (optional)
3. Prepare training materials

**Step D: Launch**
1. Announce dashboard availability
2. Send shareable link
3. Conduct training session
4. Provide support

### Step 5.6: Monitoring & Maintenance

**Weekly:**
- Check data freshness
- Monitor dashboard usage (viewers count)
- Review any error reports

**Monthly:**
- Collect user feedback
- Assess usage patterns
- Identify improvement opportunities

**Quarterly:**
- Major updates based on feedback
- Add new features or pages
- Review and update KPIs

---

## Troubleshooting

### Issue 1: Data not updating

**Symptoms:** Dashboard shows old data

**Solutions:**
1. Check Google Sheets - is data updated there?
2. In Looker Studio: Data Source → **Refresh fields**
3. Check data source connection status
4. Re-authenticate if needed

### Issue 2: Charts showing "No data"

**Symptoms:** Chart is blank with "No data" message

**Solutions:**
1. Check filters - are they too restrictive?
2. Verify date range includes data
3. Check data source configuration
4. Verify field types are correct
5. Check for null values in dimension fields

### Issue 3: Calculations incorrect

**Symptoms:** KPI values don't match expectations

**Solutions:**
1. Review calculated field formulas
2. Check aggregation types (SUM vs AVG vs COUNT)
3. Verify joins in blended data sources
4. Check for duplicate data
5. Test with small dataset first

### Issue 4: Slow performance

**Symptoms:** Dashboard takes long to load

**Solutions:**
1. Reduce data volume - use date range filters
2. Optimize calculated fields - avoid nested calculations
3. Use extract data instead of live connection
4. Simplify complex charts
5. Reduce number of charts per page

### Issue 5: Mobile view broken

**Symptoms:** Dashboard doesn't display well on mobile

**Solutions:**
1. Create mobile-specific layout
2. Use responsive canvas size
3. Simplify visualizations for mobile
4. Test on actual mobile devices
5. Consider separate mobile dashboard

### Issue 6: Sharing issues

**Symptoms:** Users can't access dashboard

**Solutions:**
1. Check sharing settings - is link access enabled?
2. Verify users have Google account
3. Check data source permissions
4. Re-send invitation link
5. Check organization restrictions

### Issue 7: Currency formatting

**Symptoms:** Currency shows wrong symbol or format

**Solutions:**
1. In data source, set field type to Currency
2. Set currency to IDR (Indonesian Rupiah)
3. Custom format: `Rp #,##0`
4. Check locale settings in report

### Issue 8: Date parsing errors

**Symptoms:** Dates showing as text or errors

**Solutions:**
1. Ensure date format is YYYY-MM-DD in source
2. Set field type to Date in data source
3. Use DATE() function for text to date conversion
4. Check for invalid dates (e.g., Feb 30)

---

## Best Practices

### Design Principles

1. **Simplicity**: Less is more - don't overcrowd dashboard
2. **Consistency**: Use consistent colors, fonts, layouts
3. **Hierarchy**: Important metrics prominent, details secondary
4. **Context**: Always provide context (comparisons, benchmarks)
5. **Actionability**: Every visualization should drive action

### Data Quality

1. **Validate Source Data**: Ensure data quality before loading
2. **Document Calculations**: Add descriptions to calculated fields
3. **Version Control**: Keep track of dashboard versions
4. **Test with Edge Cases**: Test with empty data, extreme values
5. **Regular Audits**: Periodically validate metrics accuracy

### Performance Optimization

1. **Limit Data Volume**: Use appropriate date ranges
2. **Optimize Queries**: Avoid unnecessary joins
3. **Cache When Possible**: Use data extract for large datasets
4. **Lazy Loading**: Load charts on-demand when possible
5. **Monitor Performance**: Track loading times

### User Experience

1. **Intuitive Navigation**: Clear page labels and navigation
2. **Helpful Tooltips**: Add descriptions to controls and charts
3. **Mobile Friendly**: Test and optimize for mobile
4. **Accessibility**: Use colorblind-friendly palettes
5. **Training**: Provide user guides and training

---

## Resources

### Official Documentation
- [Looker Studio Help Center](https://support.google.com/looker-studio)
- [Google Sheets Function List](https://support.google.com/docs/table/25273)

### Video Tutorials
- [Looker Studio Getting Started](https://www.youtube.com/playlist?list=PLI5YfMzCfRtZ8O1D3hcwmn3BT7yNZQbzo)
- [Data Visualization Best Practices](https://www.youtube.com/watch?v=hEWY6kkBdpo)

### Community
- [Looker Studio Community](https://www.googlecommunityhub.com/looker-studio)
- [r/LookerStudio Reddit](https://www.reddit.com/r/LookerStudio/)

### Templates
- [Looker Studio Template Gallery](https://lookerstudio.google.com/gallery)

---

## Appendix: Formula Reference

### Common Calculated Fields

**Revenue Growth Rate:**
```
(SUM(total_pembayaran_current) - SUM(total_pembayaran_previous)) 
/ SUM(total_pembayaran_previous) * 100
```

**Profit Margin:**
```
(SUM(harga_jual) - SUM(harga_modal)) / SUM(harga_jual) * 100
```

**Customer Lifetime Value:**
```
SUM(total_pembayaran) / COUNT_DISTINCT(id_pelanggan)
```

**Repeat Purchase Rate:**
```
COUNT_DISTINCT(CASE WHEN total_transaksi > 1 THEN id_pelanggan END) 
/ COUNT_DISTINCT(id_pelanggan) * 100
```

**Average Order Value:**
```
SUM(total_pembayaran) / COUNT(id_transaksi)
```

---

**End of Implementation Guide**

Good luck with your implementation! 🚀

For support: contact dosen pengampu atau refer ke dokumentasi official Looker Studio.
