# PANDUAN PERMINTAAN DATA UNTUK DASHBOARD BI LOOKER STUDIO
## Business Intelligence Dashboard - SATRIAMART

---

**Dokumen:** Permintaan Data untuk Dashboard Business Intelligence  
**Tool:** Google Looker Studio  
**Periode:** Oktober 2025  
**Tujuan:** Implementasi Dashboard BI untuk Analisis Performa Bisnis SATRIAMART

---

## DAFTAR ISI

1. [Overview Kebutuhan Data](#overview-kebutuhan-data)
2. [Data yang Dibutuhkan](#data-yang-dibutuhkan)
3. [Format dan Spesifikasi Data](#format-dan-spesifikasi-data)
4. [Template Permintaan Data](#template-permintaan-data)
5. [Checklist Permintaan](#checklist-permintaan)
6. [Tips Implementasi](#tips-implementasi)

---

## OVERVIEW KEBUTUHAN DATA

Untuk membuat Dashboard Business Intelligence yang komprehensif menggunakan Looker Studio, kami memerlukan data dari berbagai aspek bisnis SATRIAMART yang mencakup:

- **Data Pelanggan**: Untuk analisis customer segmentation dan behavior
- **Data Transaksi**: Untuk analisis sales performance dan revenue
- **Data Produk**: Untuk analisis product performance dan profitability
- **Data Produksi**: Untuk analisis operational efficiency
- **Data Inventory**: Untuk analisis stock management
- **Data Finansial**: Untuk analisis profitability dan cost

---

## DATA YANG DIBUTUHKAN

### 1. MASTER DATA PELANGGAN (Customer Master Data)

**Tabel/File:** `customer_master.csv` atau `dim_customer`

| No | Nama Kolom | Tipe Data | Contoh | Keterangan |
|----|------------|-----------|---------|------------|
| 1 | customer_id | Text/String | CUST0001 | ID unik pelanggan |
| 2 | customer_name | Text/String | PT Indah Jaya | Nama pelanggan/perusahaan |
| 3 | customer_type | Text/String | B2B | B2B atau B2C |
| 4 | industry_sector | Text/String | Retail | Sektor industri (untuk B2B) |
| 5 | region | Text/String | Jakarta | Region/wilayah |
| 6 | city | Text/String | Jakarta Selatan | Kota |
| 7 | province | Text/String | DKI Jakarta | Provinsi |
| 8 | registration_date | Date | 2024-01-15 | Tanggal registrasi |
| 9 | customer_status | Text/String | Active | Status: Active/Inactive |
| 10 | email | Text/String | contact@indahjaya.com | Email (opsional) |
| 11 | phone | Text/String | 021-12345678 | Nomor telepon (opsional) |

**Periode Data:** Semua pelanggan (aktif dan tidak aktif)  
**Estimasi Jumlah:** ~1,000 records

---

### 2. DATA TRANSAKSI PENJUALAN (Sales Transaction Data)

**Tabel/File:** `sales_transactions.csv` atau `fact_sales`

| No | Nama Kolom | Tipe Data | Contoh | Keterangan |
|----|------------|-----------|---------|------------|
| 1 | transaction_id | Text/String | TRX20250115001 | ID transaksi unik |
| 2 | order_number | Text/String | ORD-2025-0001 | Nomor order/invoice |
| 3 | transaction_date | Date | 2025-01-15 | Tanggal transaksi |
| 4 | customer_id | Text/String | CUST0001 | ID pelanggan (FK) |
| 5 | product_id | Text/String | PROD0001 | ID produk (FK) |
| 6 | product_name | Text/String | Display Stand Akrilik | Nama produk |
| 7 | category | Text/String | Display Stand | Kategori produk |
| 8 | quantity | Number | 10 | Jumlah unit terjual |
| 9 | unit_price | Number | 250000 | Harga per unit (IDR) |
| 10 | total_amount | Number | 2500000 | Total sebelum diskon |
| 11 | discount_amount | Number | 250000 | Nilai diskon (IDR) |
| 12 | net_amount | Number | 2250000 | Total setelah diskon |
| 13 | cost_of_goods | Number | 1500000 | Harga pokok penjualan |
| 14 | profit | Number | 750000 | Laba kotor |
| 15 | payment_method | Text/String | Transfer | Metode pembayaran |
| 16 | order_status | Text/String | Completed | Status: Pending/Completed/Cancelled |
| 17 | sales_channel | Text/String | Direct | Online/Offline/Direct |

**Periode Data:** 24 bulan terakhir (November 2023 - Oktober 2025)  
**Estimasi Jumlah:** ~5,000 - 10,000 transactions  
**Detail Level:** Per item dalam order (bukan per order)

---

### 3. MASTER DATA PRODUK (Product Master Data)

**Tabel/File:** `product_master.csv` atau `dim_product`

| No | Nama Kolom | Tipe Data | Contoh | Keterangan |
|----|------------|-----------|---------|------------|
| 1 | product_id | Text/String | PROD0001 | ID produk unik |
| 2 | product_name | Text/String | Display Stand Akrilik 30cm | Nama produk lengkap |
| 3 | category | Text/String | Display Stand | Kategori utama |
| 4 | sub_category | Text/String | Table Display | Sub-kategori |
| 5 | material_type | Text/String | Acrylic Clear | Jenis material |
| 6 | size_category | Text/String | Medium | Small/Medium/Large/XL |
| 7 | dimensions | Text/String | 30x20x15 cm | Dimensi (P x L x T) |
| 8 | color | Text/String | Clear | Warna |
| 9 | product_type | Text/String | Standard | Standard/Custom |
| 10 | unit_cost | Number | 150000 | Harga pokok (IDR) |
| 11 | unit_price | Number | 250000 | Harga jual (IDR) |
| 12 | weight | Number | 0.5 | Berat (kg) |
| 13 | product_status | Text/String | Active | Active/Discontinued |
| 14 | launch_date | Date | 2023-06-01 | Tanggal peluncuran |

**Periode Data:** Semua produk (aktif dan discontinued)  
**Estimasi Jumlah:** ~50-100 products

---

### 4. DATA PRODUKSI (Production Data)

**Tabel/File:** `production_records.csv` atau `fact_production`

| No | Nama Kolom | Tipe Data | Contoh | Keterangan |
|----|------------|-----------|---------|------------|
| 1 | work_order_id | Text/String | WO-2025-0001 | ID work order |
| 2 | production_date | Date | 2025-01-15 | Tanggal produksi |
| 3 | product_id | Text/String | PROD0001 | ID produk (FK) |
| 4 | product_name | Text/String | Display Stand Akrilik | Nama produk |
| 5 | quantity_produced | Number | 50 | Jumlah diproduksi |
| 6 | quantity_defect | Number | 2 | Jumlah defect |
| 7 | material_cost | Number | 5000000 | Biaya material (IDR) |
| 8 | labor_cost | Number | 2000000 | Biaya tenaga kerja |
| 9 | overhead_cost | Number | 1000000 | Biaya overhead |
| 10 | total_production_cost | Number | 8000000 | Total biaya produksi |
| 11 | labor_hours | Number | 40 | Jam kerja |
| 12 | machine_hours | Number | 20 | Jam mesin |
| 13 | quality_score | Number | 96 | Skor kualitas (%) |
| 14 | production_status | Text/String | Completed | Status produksi |

**Periode Data:** 24 bulan terakhir (November 2023 - Oktober 2025)  
**Estimasi Jumlah:** ~2,000 - 3,000 work orders  
**Keterangan:** Data ini opsional jika tidak tersedia

---

### 5. DATA INVENTORY/STOK (Inventory Data)

**Tabel/File:** `inventory_movements.csv` atau `fact_inventory`

| No | Nama Kolom | Tipe Data | Contoh | Keterangan |
|----|------------|-----------|---------|------------|
| 1 | movement_id | Text/String | INV-2025-0001 | ID movement |
| 2 | movement_date | Date | 2025-01-15 | Tanggal movement |
| 3 | product_id | Text/String | PROD0001 | ID produk (FK) |
| 4 | product_name | Text/String | Display Stand Akrilik | Nama produk |
| 5 | warehouse_location | Text/String | Warehouse A | Lokasi gudang |
| 6 | movement_type | Text/String | IN | IN/OUT/ADJUSTMENT |
| 7 | quantity | Number | 50 | Jumlah movement |
| 8 | opening_stock | Number | 100 | Stok awal |
| 9 | closing_stock | Number | 150 | Stok akhir |
| 10 | unit_cost | Number | 150000 | Nilai per unit |
| 11 | total_value | Number | 22500000 | Nilai total stok |
| 12 | reference_number | Text/String | WO-2025-0001 | Referensi (WO/Order) |

**Periode Data:** 24 bulan terakhir (November 2023 - Oktober 2025)  
**Estimasi Jumlah:** ~5,000 - 10,000 movements

---

### 6. DATA BIAYA & FINANSIAL (Financial Data)

**Tabel/File:** `financial_data.csv` atau `fact_financial`

| No | Nama Kolom | Tipe Data | Contoh | Keterangan |
|----|------------|-----------|---------|------------|
| 1 | period_date | Date | 2025-01 | Bulan periode |
| 2 | cost_category | Text/String | Marketing | Kategori biaya |
| 3 | cost_type | Text/String | Digital Ads | Tipe biaya |
| 4 | amount | Number | 5000000 | Nilai biaya (IDR) |
| 5 | department | Text/String | Marketing | Departemen |
| 6 | description | Text/String | Facebook Ads Campaign | Deskripsi |

**Kategori Biaya yang Diperlukan:**
- Marketing & Sales
- Operational Expenses
- Overhead Costs
- Administrative Costs
- Utilities
- Rent & Facilities

**Periode Data:** 24 bulan terakhir  
**Keterangan:** Data agregat per bulan sudah cukup

---

### 7. DATA DIMENSI WAKTU (Date Dimension)

**Tabel/File:** `dim_date.csv` (opsional - bisa di-generate)

| No | Nama Kolom | Tipe Data | Contoh | Keterangan |
|----|------------|-----------|---------|------------|
| 1 | date | Date | 2025-01-15 | Tanggal lengkap |
| 2 | year | Number | 2025 | Tahun |
| 3 | quarter | Number | 1 | Kuartal (1-4) |
| 4 | month | Number | 1 | Bulan (1-12) |
| 5 | month_name | Text/String | January | Nama bulan |
| 6 | week | Number | 3 | Minggu dalam tahun |
| 7 | day_of_week | Number | 3 | Hari dalam minggu (1-7) |
| 8 | day_name | Text/String | Wednesday | Nama hari |
| 9 | is_weekend | Boolean | FALSE | Weekend flag |
| 10 | is_holiday | Boolean | FALSE | Holiday flag |

**Keterangan:** Tabel ini bisa di-generate otomatis, tidak wajib dari perusahaan

---

## FORMAT DAN SPESIFIKASI DATA

### Format File yang Diterima

#### Pilihan 1: File Format (Paling Umum)
- **CSV** (Comma Separated Values) - **RECOMMENDED**
- **Excel** (.xlsx) - maksimal 100,000 rows per sheet
- **Google Sheets** - bisa langsung connect ke Looker Studio

#### Pilihan 2: Database Connection (Paling Ideal)
- **MySQL** - direct connection ke Looker Studio
- **PostgreSQL** - direct connection ke Looker Studio
- **Google BigQuery** - optimal untuk Looker Studio
- **Cloud SQL** - fully supported

### Spesifikasi Format Data

#### 1. Format Tanggal
```
Format yang Diinginkan: YYYY-MM-DD
Contoh: 2025-01-15

❌ Hindari: 15/01/2025, 01-15-2025, 15 Jan 2025
✅ Gunakan: 2025-01-15
```

#### 2. Format Angka
```
Separator Desimal: . (titik)
Contoh: 2500000.50

❌ Hindari: 2.500.000,50 (format Indonesia)
✅ Gunakan: 2500000.50 atau 2500000
```

#### 3. Format Teks
```
Encoding: UTF-8
Quote Character: " (double quote)
Line Terminator: \n (LF) atau \r\n (CRLF)

❌ Hindari: Karakter special yang tidak perlu
✅ Gunakan: Text bersih tanpa formatting
```

#### 4. Struktur File CSV
```csv
header1,header2,header3
value1,value2,value3
value1,value2,value3
```

**Requirements:**
- Baris pertama adalah header/nama kolom
- Tidak ada baris kosong di tengah data
- Tidak ada total/subtotal rows
- Consistent column count per row

### Data Quality Requirements

#### ✅ Data yang Baik:
- Tidak ada duplikasi records
- ID konsisten dan unik
- Tanggal dalam range yang valid
- Angka tidak mengandung text
- Status/kategori menggunakan nilai standar
- Relasi antar tabel konsisten (Foreign Keys valid)

#### ❌ Hindari:
- Duplikasi data
- Missing values pada kolom kunci (ID, tanggal)
- Format tanggal tidak konsisten
- Typo pada kategori/status
- NULL values berlebihan

---

## TEMPLATE PERMINTAAN DATA

### Template Email Formal

```
Kepada Yth.
[Nama Pimpinan/Manager Data/IT Manager]
[Nama Perusahaan - SATRIAMART]

Perihal: Permintaan Data untuk Dashboard Business Intelligence

Dengan hormat,

Sehubungan dengan proyek pembuatan Dashboard Business Intelligence menggunakan 
Google Looker Studio untuk SATRIAMART, kami memerlukan beberapa data historis 
untuk keperluan analisis dan visualisasi performa bisnis.

Dashboard yang akan dibuat bertujuan untuk:
1. Analisis performa penjualan dan revenue
2. Analisis perilaku dan segmentasi pelanggan
3. Analisis performa produk dan profitability
4. Monitoring inventory dan produksi
5. Analisis finansial dan cost efficiency

Berikut detail data yang kami perlukan:

┌─────────────────────────────────────────────────────────────────┐
│ 1. MASTER DATA PELANGGAN                                        │
├─────────────────────────────────────────────────────────────────┤
│    - File: customer_master.csv/xlsx                            │
│    - Periode: Semua pelanggan (aktif dan tidak aktif)         │
│    - Kolom: customer_id, customer_name, customer_type,        │
│             industry_sector, region, city, registration_date,  │
│             customer_status                                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 2. DATA TRANSAKSI PENJUALAN                                    │
├─────────────────────────────────────────────────────────────────┤
│    - File: sales_transactions.csv/xlsx                        │
│    - Periode: 24 bulan (November 2023 - Oktober 2025)        │
│    - Detail: Per item dalam order (bukan agregat)            │
│    - Kolom: transaction_id, order_number, transaction_date,  │
│             customer_id, product_id, quantity, unit_price,   │
│             total_amount, discount, net_amount, COGS, profit │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 3. MASTER DATA PRODUK                                          │
├─────────────────────────────────────────────────────────────────┤
│    - File: product_master.csv/xlsx                            │
│    - Periode: Semua produk                                    │
│    - Kolom: product_id, product_name, category, sub_category,│
│             material_type, size, color, product_type,         │
│             unit_cost, unit_price, product_status             │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 4. DATA PRODUKSI (Jika tersedia)                              │
├─────────────────────────────────────────────────────────────────┤
│    - File: production_records.csv/xlsx                        │
│    - Periode: 24 bulan (November 2023 - Oktober 2025)        │
│    - Kolom: work_order_id, production_date, product_id,      │
│             quantity_produced, production_cost, labor_hours,  │
│             quality_score                                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 5. DATA INVENTORY/STOK                                         │
├─────────────────────────────────────────────────────────────────┤
│    - File: inventory_movements.csv/xlsx                       │
│    - Periode: 24 bulan (November 2023 - Oktober 2025)        │
│    - Kolom: movement_date, product_id, movement_type,        │
│             quantity, opening_stock, closing_stock            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 6. DATA BIAYA & FINANSIAL                                      │
├─────────────────────────────────────────────────────────────────┤
│    - File: financial_data.csv/xlsx                            │
│    - Periode: 24 bulan (November 2023 - Oktober 2025)        │
│    - Detail: Per bulan (agregat)                             │
│    - Kolom: period_date, cost_category, cost_type, amount    │
└─────────────────────────────────────────────────────────────────┘

SPESIFIKASI FORMAT:
- Format file: CSV atau Excel (.xlsx) atau Google Sheets
- Format tanggal: YYYY-MM-DD (contoh: 2025-01-15)
- Format angka: Gunakan titik (.) sebagai separator desimal
- Encoding: UTF-8
- Header: Baris pertama adalah nama kolom
- Tidak ada baris kosong di tengah data

ALTERNATIF (Jika Memungkinkan):
Jika memungkinkan, kami lebih prefer akses langsung ke database 
(MySQL/PostgreSQL) karena Looker Studio dapat connect langsung dan 
data akan selalu up-to-date secara otomatis.

DATA PRIVACY & KEAMANAN:
- Data akan digunakan hanya untuk keperluan akademis
- Data akan dijaga kerahasiaannya dan tidak disebarluaskan
- Jika diperlukan, nama pelanggan dapat di-anonymize/di-mask

TIMELINE:
Kami berharap dapat menerima data paling lambat [tanggal], agar 
dapat memulai proses development dashboard.

Demikian surat permintaan data ini kami sampaikan. Atas perhatian 
dan kerjasamanya, kami ucapkan terima kasih.

Hormat kami,

[Nama Anda]
[NIM]
[Program Studi Sistem Informasi]
[Universitas Nusa Mandiri]
[Email]
[No. HP]

Lampiran:
1. Dokumen detail spesifikasi data (file ini)
2. Proposal dashboard BI (jika ada)
```

---

## CHECKLIST PERMINTAAN

### Checklist Kelengkapan Data

```
☐ MASTER DATA
  ☐ Master Data Pelanggan (customer_master.csv)
  ☐ Master Data Produk (product_master.csv)
  
☐ TRANSACTIONAL DATA
  ☐ Data Transaksi Penjualan - 24 bulan (sales_transactions.csv)
  ☐ Data Produksi - 24 bulan (production_records.csv) [opsional]
  ☐ Data Inventory Movements - 24 bulan (inventory_movements.csv)
  
☐ FINANCIAL DATA
  ☐ Data Biaya Operasional per bulan (financial_data.csv)
  ☐ Data COGS per produk (bisa dalam product_master atau sales)
  
☐ SUPPORTING DATA
  ☐ Data Dictionary / Penjelasan kolom
  ☐ Business rules & definitions
  ☐ Contact person untuk follow-up questions
```

### Checklist Format & Kualitas

```
☐ FORMAT FILE
  ☐ Format: CSV/Excel/Google Sheets
  ☐ Encoding: UTF-8
  ☐ Header row ada di baris pertama
  ☐ Tidak ada baris kosong di tengah data
  
☐ FORMAT DATA
  ☐ Tanggal: YYYY-MM-DD format
  ☐ Angka: Menggunakan titik (.) sebagai desimal
  ☐ Text: Tanpa formatting special
  ☐ Consistent column count per row
  
☐ DATA QUALITY
  ☐ Tidak ada duplikasi records
  ☐ ID unik dan konsisten
  ☐ Foreign keys valid (relasi antar tabel konsisten)
  ☐ Kategori/status menggunakan nilai standar
  ☐ Minimal missing values pada kolom kunci
```

### Checklist Alternatif

Jika data lengkap tidak tersedia:

```
☐ MINIMUM VIABLE DATA (untuk mulai)
  ☐ Data transaksi penjualan 6 bulan terakhir
  ☐ Master data pelanggan
  ☐ Master data produk
  
☐ SAMPLE DATA (untuk testing)
  ☐ Sample 1,000 transaksi untuk testing struktur data
  ☐ Sample 50 produk
  ☐ Sample 100 pelanggan
  
☐ ANONYMIZED DATA
  ☐ Nama pelanggan di-mask (CUST001, CUST002, dst)
  ☐ Nilai transaksi bisa di-scale jika sensitif
  ☐ Tetap maintain proporsi dan pattern
```

---

## TIPS IMPLEMENTASI

### 1. Komunikasi dengan Stakeholder

**Sebelum Meminta Data:**
- Pahami dulu sistem/software yang digunakan perusahaan
- Identifikasi siapa data owner (biasanya IT atau Finance)
- Jelaskan tujuan dan manfaat dashboard
- Tunjukkan contoh dashboard yang akan dibuat (mockup)

**Saat Meminta Data:**
- Gunakan bahasa yang profesional
- Berikan deadline yang reasonable
- Tawarkan fleksibilitas format jika memungkinkan
- Jelaskan soal privacy dan keamanan data

**Follow-up:**
- Confirm receipt of data
- Validate data quality secepatnya
- Report jika ada issue atau data yang kurang
- Update progress secara berkala

### 2. Validasi Data Awal

Setelah menerima data, lakukan validasi:

```
✅ BASIC CHECKS:
- File bisa dibuka tanpa error
- Jumlah rows sesuai ekspektasi
- Semua kolom yang diminta ada
- Format tanggal konsisten
- Tidak ada kolom yang semuanya kosong

✅ QUALITY CHECKS:
- Cek duplikasi: Apakah ada transaction_id duplicate?
- Cek missing: Berapa % missing values per kolom?
- Cek range: Apakah tanggal dalam range yang masuk akal?
- Cek consistency: Apakah total_amount = quantity * unit_price?
- Cek foreign keys: Apakah semua customer_id ada di master customer?

✅ BUSINESS LOGIC CHECKS:
- Apakah profit = net_amount - cost_of_goods?
- Apakah closing_stock = opening_stock + receipts - issues?
- Apakah sum(transactions) per month make sense?
```

### 3. Handling Data Issues

**Jika Data Tidak Lengkap:**
- Mulai dengan data yang ada
- Request specific missing data
- Gunakan sample data untuk testing dulu

**Jika Format Tidak Sesuai:**
- Bisa di-transform menggunakan tools:
  - Excel: Power Query
  - Google Sheets: Apps Script
  - Python: Pandas
  - SQL: Database transformation

**Jika Data Quality Rendah:**
- Dokumentasikan semua issues
- Diskusikan dengan data owner
- Buat cleaning procedure
- Set expectation tentang accuracy

### 4. Database Connection (Ideal Setup)

Jika perusahaan bisa provide database access:

**Keuntungan:**
- Data selalu up-to-date (real-time/near real-time)
- Tidak perlu manual upload
- Bisa handle data besar
- Looker Studio auto-refresh

**Requirements:**
- Database harus accessible dari internet atau
- Database harus allow Looker Studio IP addresses
- Read-only user account
- Proper firewall configuration

**Database yang Supported Looker Studio:**
- MySQL
- PostgreSQL
- Google Cloud SQL
- BigQuery
- SQL Server
- Oracle (via partner connector)

### 5. Looker Studio Best Practices

**Data Source Setup:**
- Gunakan blended data sources untuk join tables
- Set proper data types (Date, Number, Text)
- Create calculated fields untuk metrics
- Use parameters untuk dynamic filtering

**Performance Optimization:**
- Aggregate data di database level jika mungkin
- Gunakan data extract/cache untuk large datasets
- Limit date range dengan default parameters
- Use database views untuk complex calculations

**Security:**
- Set proper sharing permissions
- Use row-level security jika diperlukan
- Schedule refresh pada off-peak hours
- Backup dashboard configuration regularly

### 6. Sample Data untuk Testing

Jika sulit mendapat data real:

**Option 1: Generate Sample Data**
- Gunakan Python Faker library
- Excel random functions
- Online data generators

**Option 2: Use Public Datasets**
- Google Dataset Search
- Kaggle Datasets
- UCI Machine Learning Repository

**Option 3: Create Minimal Viable Dataset**
- 100 customers
- 500 transactions
- 20 products
- 3 months data
- Cukup untuk prove concept

---

## APPENDIX

### A. Contoh Data Sample

#### Sample: customer_master.csv
```csv
customer_id,customer_name,customer_type,industry_sector,region,city,registration_date,customer_status
CUST0001,PT Indah Jaya,B2B,Retail,Jakarta,Jakarta Selatan,2024-01-15,Active
CUST0002,Toko Maju Bersama,B2B,Retail,Bandung,Bandung,2024-02-20,Active
CUST0003,John Doe,B2C,Individual,Jakarta,Jakarta Utara,2024-03-10,Active
```

#### Sample: sales_transactions.csv
```csv
transaction_id,order_number,transaction_date,customer_id,product_id,product_name,quantity,unit_price,total_amount,discount_amount,net_amount,cost_of_goods,profit
TRX001,ORD-2025-0001,2025-01-15,CUST0001,PROD0001,Display Stand Akrilik,10,250000,2500000,250000,2250000,1500000,750000
TRX002,ORD-2025-0002,2025-01-16,CUST0002,PROD0002,Custom Panel,5,500000,2500000,0,2500000,1750000,750000
```

#### Sample: product_master.csv
```csv
product_id,product_name,category,sub_category,material_type,size_category,color,product_type,unit_cost,unit_price,product_status
PROD0001,Display Stand Akrilik 30cm,Display Stand,Table Display,Acrylic Clear,Medium,Clear,Standard,150000,250000,Active
PROD0002,Custom Panel Akrilik,Custom Panels,Wall Panel,Acrylic Clear,Large,Clear,Custom,350000,500000,Active
```

### B. Tools yang Berguna

**Data Preparation:**
- **Excel/Google Sheets**: Basic data cleaning
- **OpenRefine**: Advanced data cleaning
- **Python Pandas**: Programmatic data transformation
- **SQL**: Database-level transformation

**Data Validation:**
- **Great Expectations**: Python data validation framework
- **csvlint**: CSV validation tool
- **Data Validator**: Excel add-in

**Documentation:**
- **Data Dictionary Template**: Document semua kolom
- **ERD Tools**: Draw.io, Lucidchart untuk relationship diagram
- **Confluence/Notion**: Documentation platform

### C. Resources & References

**Looker Studio:**
- [Looker Studio Documentation](https://support.google.com/looker-studio)
- [Looker Studio Community](https://www.en.advertisercommunity.com/t5/Looker-Studio/ct-p/looker-studio)
- [Data Source Connectors](https://support.google.com/looker-studio/answer/6268208)

**Data Modeling:**
- Star Schema Design Patterns
- Kimball Dimensional Modeling
- Data Warehouse Toolkit

**Sample Dashboards:**
- [Looker Studio Template Gallery](https://lookerstudio.google.com/navigation/reporting)
- Public Dashboard Examples
- Industry-specific Templates

---

## CONTACT INFORMATION

Untuk pertanyaan lebih lanjut terkait permintaan data ini:

**Nama:** [Nama Anda]  
**NIM:** [NIM Anda]  
**Program Studi:** Sistem Informasi  
**Universitas:** Nusa Mandiri  
**Email:** [email@student.nusamandiri.ac.id]  
**HP:** [Nomor HP]  

**Dosen Pembimbing:**  
Ridan Nurfalah, M.Kom  
Email: [email dosen]

---

**Dokumen ini dibuat:** 16 Oktober 2025  
**Versi:** 1.0  
**Status:** Draft untuk Permintaan Data

---

*Semoga dokumen ini membantu proses permintaan data untuk implementasi Dashboard Business Intelligence. Good luck dengan project Anda!* 🚀
