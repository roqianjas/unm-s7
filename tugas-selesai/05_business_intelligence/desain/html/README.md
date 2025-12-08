# 📊 SATRIAMART Business Intelligence Dashboard

Dashboard interaktif berbasis HTML untuk visualisasi data Business Intelligence SATRIAMART menggunakan Tailwind CSS dan Chart.js.

## 🎯 Fitur Dashboard

Dashboard ini terdiri dari 5 halaman utama yang menampilkan analisis komprehensif:

### 1. **Executive Dashboard** (`index.html`)
- **KPI Cards**: Total Revenue, Total Transactions, Average Order Value, Total Customers
- **Revenue Trend**: Grafik tren pendapatan 12 bulan
- **Sales by Channel**: Distribusi penjualan per channel (WhatsApp, Instagram, Offline, Marketplace)
- **Category Performance**: Performa per kategori produk
- **Payment Methods**: Metode pembayaran yang digunakan
- **Order Status**: Status pesanan (Selesai, Proses, Dibatalkan, dll)
- **Top 10 Products**: Tabel produk terlaris berdasarkan revenue

### 2. **Sales Analysis** (`sales.html`)
- **Sales Overview**: Gross Sales, Net Sales, Total Discounts, Shipping Revenue
- **Channel Performance**: Analisis performa per channel dengan metrics detail
- **Time-based Analysis**: 
  - Sales by Day of Week
  - Monthly Sales Comparison
- **Transaction Status**: Order status dan payment status dengan conversion metrics
- **Recent Transactions**: Tabel transaksi terbaru dengan filter

### 3. **Product Performance** (`products.html`)
- **Product Overview**: Total Products, Inventory Value, Avg Profit Margin, Low Stock Items
- **Category Analysis**: Revenue by category dengan metrics detail
- **Top & Bottom Performers**: Best sellers dan slow-moving products
- **Price Analysis**: Distribusi price range dan profit margin per kategori
- **Stock Levels**: Critical stock, Low stock, dan Healthy stock
- **Product Catalog**: Tabel lengkap semua produk dengan filter

### 4. **Customer Analytics** (`customers.html`)
- **Customer Overview**: Total Customers, Avg Customer Value, Repeat Rate, Avg Rating
- **RFM Segmentation**: VIP, Loyal, Regular, High Value, New customers
- **Geographic Distribution**: Top locations by revenue
- **Customer Behavior**: Purchase frequency, Gender distribution, Age groups
- **Top 20 Customers**: Customer terbaik berdasarkan revenue/transactions/items
- **Customer Database**: Tabel lengkap semua customer dengan filter

### 5. **Financial Dashboard** (`financial.html`)
- **Financial Overview**: Total Revenue, Total Costs, Gross Profit, Net Profit
- **Revenue vs Profit Trend**: Perbandingan revenue, costs, dan profit bulanan
- **Profit Margin Analysis**: Tren profit margin per bulan
- **Operational Costs**: Breakdown biaya operasional per kategori
- **Revenue Composition**: Product sales, Shipping revenue, Custom services
- **Expense Details**: Tabel detail pengeluaran operasional

## 📁 Struktur File

```
dashboard/
├── index.html          # Executive Dashboard (Halaman Utama)
├── sales.html          # Sales Analysis
├── products.html       # Product Performance
├── customers.html      # Customer Analytics
├── financial.html      # Financial Dashboard
└── README.md           # Dokumentasi ini

data/
├── 01_master_produk.csv
├── 02_master_pelanggan.csv
├── 03_transaksi_penjualan.csv
├── 04_riwayat_stok.csv
├── 05_biaya_operasional.csv
└── 06_marketing_campaign.csv
```

## 🚀 Cara Menggunakan

### Metode 1: Langsung di Browser (Local)

1. **Download atau Clone Repository**
   ```bash
   cd c:\laragon\www\unm-s7\tugas-selesai\05_business_intelligence
   ```

2. **Buka Dashboard**
   - Double-click file `dashboard/index.html`
   - Atau klik kanan → Open with → Chrome/Firefox/Edge
   
   **⚠️ PENTING**: Beberapa browser (terutama Chrome) memblokir loading file CSV dari `file://` karena CORS policy. Jika data tidak muncul, gunakan Metode 2 atau 3.

### Metode 2: Menggunakan Local Server (Recommended)

**Dengan Python:**
```bash
# Di folder dashboard
cd dashboard
python -m http.server 8000
```
Kemudian buka: `http://localhost:8000`

**Dengan PHP:**
```bash
# Di folder dashboard
cd dashboard
php -S localhost:8000
```
Kemudian buka: `http://localhost:8000`

**Dengan Node.js (http-server):**
```bash
# Install http-server globally (sekali saja)
npm install -g http-server

# Di folder dashboard
cd dashboard
http-server -p 8000
```
Kemudian buka: `http://localhost:8000`

### Metode 3: Menggunakan Laragon (Jika sudah terinstall)

1. Pastikan Laragon sudah running
2. Buka browser dan akses:
   ```
   http://localhost/unm-s7/tugas-selesai/05_business_intelligence/dashboard/
   ```

### Metode 4: Menggunakan VS Code Live Server

1. Install extension "Live Server" di VS Code
2. Buka folder `dashboard` di VS Code
3. Klik kanan pada `index.html` → "Open with Live Server"
4. Dashboard akan otomatis terbuka di browser

## 🎨 Fitur Interaktif

### Filter & Search
- **Sales Page**: Filter by channel, status, dan periode
- **Products Page**: Filter by category, search products
- **Customers Page**: Filter by city, search customers
- **Financial Page**: Filter expenses by category dan month

### Charts
Semua chart menggunakan **Chart.js** dengan fitur:
- ✅ Hover tooltips dengan format currency
- ✅ Responsive (menyesuaikan ukuran layar)
- ✅ Interactive legends
- ✅ Real-time data dari CSV

### Navigation
- **Top Navigation Bar**: Mudah berpindah antar halaman
- **Active Page Indicator**: Highlight halaman yang sedang aktif
- **Responsive Design**: Berfungsi di desktop, tablet, dan mobile

## 📊 Sumber Data

Dashboard ini menggunakan data REAL dari file CSV:

1. **01_master_produk.csv** (50 produk)
   - id_produk, nama_produk, kategori, harga_jual, harga_modal, stok_tersedia, dll

2. **02_master_pelanggan.csv** (180 customers)
   - id_pelanggan, nama_lengkap, email, nomor_telepon, kota, jenis_kelamin, usia, dll

3. **03_transaksi_penjualan.csv** (320 transaksi)
   - id_transaksi, tanggal_transaksi, id_pelanggan, id_produk, total_pembayaran, dll

4. **05_biaya_operasional.csv** (biaya operasional)
   - id_biaya, tanggal, kategori_biaya, nominal, metode_pembayaran, dll

## 🛠️ Teknologi yang Digunakan

### Frontend Framework
- **HTML5**: Struktur halaman
- **Tailwind CSS** (CDN): Styling dan responsive design
- **JavaScript (Vanilla)**: Logic dan interaktivity

### Libraries
- **Chart.js 4.x** (CDN): Visualisasi charts
- **PapaParse 5.3** (CDN): CSV parser

### No Backend Required!
Dashboard ini 100% **client-side**, tidak memerlukan:
- ❌ Database server
- ❌ Backend framework
- ❌ API endpoints
- ✅ Hanya butuh web browser dan file CSV

## 📱 Responsive Design

Dashboard dioptimalkan untuk berbagai ukuran layar:
- **Desktop** (1200px+): Full layout dengan semua fitur
- **Tablet** (768px - 1199px): Adjusted grid layout
- **Mobile** (<768px): Stacked layout, scrollable tables

## 🎯 Penggunaan untuk Looker Studio

Dashboard HTML ini dirancang sebagai **prototype** dan **reference** untuk pembuatan dashboard di Looker Studio:

### Mapping Dashboard ke Looker Studio

1. **KPI Cards** → Looker Studio **Scorecards**
2. **Line Charts** → Looker Studio **Time Series Charts**
3. **Bar Charts** → Looker Studio **Bar Charts**
4. **Pie/Doughnut** → Looker Studio **Pie Charts**
5. **Tables** → Looker Studio **Tables**

### Data Connection
1. Upload file CSV ke **Google Sheets**
2. Connect Google Sheets to **Looker Studio**
3. Recreate visualizations berdasarkan prototype HTML ini

### Design Reference
- Color scheme: Green (#22C55E), Blue (#3B82F6), Purple (#A855F7), Orange (#FB923C)
- Layout: 4-column grid untuk KPIs, 2-column untuk charts
- Font: System fonts (Tailwind default)

## 🔧 Customization

### Mengganti Warna
Edit nilai warna di setiap file HTML:
```javascript
backgroundColor: [
    'rgb(34, 197, 94)',   // Green
    'rgb(59, 130, 246)',   // Blue
    'rgb(168, 85, 247)',   // Purple
    'rgb(251, 146, 60)',   // Orange
]
```

### Menambah/Mengubah Chart
Lihat dokumentasi Chart.js: https://www.chartjs.org/docs/latest/

### Mengubah Layout
Edit Tailwind classes:
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
```

## ⚠️ Troubleshooting

### Data Tidak Muncul / "Loading..."
**Penyebab**: Browser CORS policy
**Solusi**: Gunakan local server (Python, PHP, atau http-server)

### Chart Tidak Tampil
**Penyebab**: Chart.js tidak ter-load
**Solusi**: Pastikan koneksi internet aktif (CDN)

### CSV Path Error
**Penyebab**: Relative path tidak benar
**Solusi**: Pastikan struktur folder:
```
dashboard/
  ├── index.html
  └── (other html files)
data/
  └── (csv files)
```

### Performance Lambat
**Penyebab**: Banyak data di-render
**Solusi**: Sudah ada pagination di tabel, maksimal 20-50 rows

## 📈 Metrics & KPIs yang Ditampilkan

### Financial Metrics
- Total Revenue, Gross Profit, Net Profit
- Profit Margin, Net Margin
- COGS (Cost of Goods Sold)
- Operational Costs

### Sales Metrics
- Total Transactions
- Average Order Value (AOV)
- Conversion Rate (Completion Rate)
- Sales by Channel

### Product Metrics
- Total Products, Active Products
- Inventory Value
- Stock Levels (Critical, Low, Healthy)
- Best Sellers, Slow Movers

### Customer Metrics
- Total Customers
- Average Customer Value (LTV)
- Repeat Customer Rate
- Customer Satisfaction (Avg Rating)
- RFM Segmentation

## 📝 Catatan Penting

1. **Data Real**: Semua data berasal dari CSV yang sudah Anda buat
2. **Dynamic**: Jika CSV diupdate, refresh browser untuk melihat data baru
3. **Offline Ready**: Setelah halaman load, bisa digunakan offline (kecuali CDN)
4. **Print Friendly**: Bisa di-print atau export to PDF dari browser

## 📞 Support

Jika ada pertanyaan atau masalah:
1. Check console browser (F12) untuk error messages
2. Pastikan file CSV ada di folder `../data/`
3. Gunakan local server untuk menghindari CORS issues

## 📄 License

Dashboard ini dibuat untuk keperluan tugas Business Intelligence - Universitas Negeri Makassar.

---

**Developed by**: Mahasiswa S7 - Business Intelligence Course  
**Data Period**: November 2024 - Oktober 2025  
**Company**: SATRIAMART (Dekorasi & Aksesoris Akrilik)
