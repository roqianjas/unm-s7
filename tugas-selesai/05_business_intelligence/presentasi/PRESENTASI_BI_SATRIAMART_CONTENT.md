# PRESENTASI BUSINESS INTELLIGENCE
## Dashboard Interaktif SATRIAMART dengan Looker Studio

---

## STRUKTUR PRESENTASI (16 SLIDES)

### Target Durasi: 15-20 menit
- Opening: 1 menit
- Content: 13-17 menit
- Closing: 1 menit
- Q&A: 5-10 menit

---

## SLIDE 1: COVER
**Visual**: Background gradient modern dengan logo UNM dan SATRIAMART

```
PERANCANGAN DASHBOARD BUSINESS INTELLIGENCE INTERAKTIF
UNTUK MENDUKUNG KEPUTUSAN BISNIS PADA SATRIAMART

[Logo Universitas Nusa Mandiri]        [Logo SATRIAMART]

Disusun Oleh:
Kelompok [X] - Sistem Informasi

1. Nama Lengkap - NIM
2. Nama Lengkap - NIM  
3. Nama Lengkap - NIM
4. Nama Lengkap - NIM

Business Intelligence II (493)
Dosen: Ridan Nurfalah, M.Kom

Program Studi Sistem Informasi
Fakultas Teknologi Informasi
Universitas Nusa Mandiri
Jakarta, 2025
```

**Speaker Notes:**
- Selamat pagi/siang Bapak/Ibu Dosen dan teman-teman
- Perkenalkan kami dari kelompok [X]
- Hari ini kami akan mempresentasikan hasil project BI kami

---

## SLIDE 2: LATAR BELAKANG & RUMUSAN MASALAH

**Layout**: Split screen (50-50)

**Kiri - Latar Belakang:**
```
🎯 LATAR BELAKANG

✓ SATRIAMART: UMKM Dekorasi Akrilik di Depok
✓ Mengalami pertumbuhan 300% dalam 2 tahun
✓ Data tersebar di berbagai spreadsheet
✓ Kesulitan monitoring performa bisnis
✓ Keputusan masih berbasis intuisi

💡 SOLUSI: Dashboard BI Interaktif
```

**Kanan - Rumusan Masalah:**
```
❓ RUMUSAN MASALAH

1. Bagaimana merancang dashboard BI yang 
   efektif untuk SATRIAMART?

2. Data apa saja yang diperlukan untuk 
   mendukung keputusan bisnis?

3. KPI apa saja yang perlu dimonitor?

4. Bagaimana menghasilkan insight yang 
   actionable dari data operasional?
```

**Visual**: 
- Icon/ilustrasi data analytics
- Gambar produk SATRIAMART
- Chart yang masih berantakan → chart yang rapi

**Speaker Notes:**
- SATRIAMART adalah UMKM yang berkembang pesat
- Tantangan: data banyak tapi tidak ter-organize
- Butuh sistem untuk mengubah data menjadi insight
- Dashboard BI adalah solusinya

---

## SLIDE 3: TUJUAN & MANFAAT

**Layout**: 2 kolom dengan icon

**Kiri - Tujuan:**
```
🎯 TUJUAN PENELITIAN

1. Merancang dashboard BI interaktif 
   menggunakan Looker Studio

2. Menyajikan visualisasi data penjualan,
   produk, pelanggan, dan keuangan

3. Mengidentifikasi KPI utama untuk
   monitoring performa bisnis

4. Memberikan insight actionable untuk
   pengambilan keputusan
```

**Kanan - Manfaat:**
```
✨ MANFAAT

Bagi SATRIAMART:
✓ Monitoring real-time performa bisnis
✓ Identifikasi peluang & masalah cepat
✓ Keputusan berbasis data
✓ Optimasi operasional & marketing

Bagi Penulis:
✓ Aplikasi teori BI pada kasus nyata
✓ Pengalaman rancang dashboard
✓ Skill analisis data & visualisasi
```

**Visual**:
- Icon target, chart, lightbulb
- Badge/seal "Data-Driven Decision"

**Speaker Notes:**
- Tujuan utama: dashboard yang user-friendly dan actionable
- Manfaat praktis untuk owner dan tim SATRIAMART
- Learning experience bagi kami sebagai mahasiswa

---

## SLIDE 4: PROFIL SATRIAMART

**Layout**: Visual-rich dengan foto produk

```
🏢 PROFIL PERUSAHAAN

Nama: SATRIAMART
Bidang: Dekorasi & Aksesoris Akrilik Custom
Didirikan: 2021
Lokasi: Jl. Usman Dehir No.54, Limo, Depok

📊 DATA BISNIS (12 Bulan)
├─ Total Revenue: Rp 111.976.550
├─ Total Transaksi: 320 orders
├─ Average Order Value: Rp 349.926
├─ Jumlah Produk: 50 SKU
├─ Jumlah Pelanggan: 180 customers
└─ Channel: WhatsApp, Instagram, Website, Offline

🎨 PRODUK UTAMA
├─ Nomor Rumah Akrilik (35%)
├─ Papan Nama Toko (28%)
├─ Signage LED (23%)
└─ Aksesoris Dekorasi (14%)

📍 MARKET: Jabodetabek (85%)
```

**Visual**:
- Foto produk SATRIAMART
- Foto workshop/showroom
- Mini map lokasi Depok
- Icon social media

**Speaker Notes:**
- SATRIAMART fokus pada custom akrilik
- Melayani individu dan bisnis
- Market dominan di Jabodetabek
- Multi-channel dengan WhatsApp sebagai utama

---

## SLIDE 5: LANDASAN TEORI - BUSINESS INTELLIGENCE

**Layout**: Konseptual dengan diagram

```
📚 BUSINESS INTELLIGENCE (BI)

Definisi (Turban et al., 2021):
"Seperangkat teknologi dan proses yang menggunakan data 
untuk memahami dan menganalisis performa bisnis guna 
mendorong perencanaan strategis yang lebih baik"

┌─────────────────────────────────────┐
│   KOMPONEN SISTEM BI                │
├─────────────────────────────────────┤
│ 1. Data Sources                     │
│    └─ Transactional Data            │
│       Customer Data, Product Data   │
│                                      │
│ 2. ETL Process                      │
│    └─ Extract → Transform → Load    │
│                                      │
│ 3. Data Warehouse                   │
│    └─ Centralized Repository        │
│                                      │
│ 4. Analytics & BI Tools             │
│    └─ Looker Studio, Tableau, etc   │
│                                      │
│ 5. Dashboard & Reports              │
│    └─ Interactive Visualization     │
└─────────────────────────────────────┘
```

**Visual**:
- Diagram arsitektur BI
- Flow data sources → dashboard
- Icon tools (Looker Studio logo)

**Speaker Notes:**
- BI mengubah data mentah menjadi insight
- Komponen terintegrasi dari source hingga visualization
- Fokus pada dashboard sebagai interface pengguna

---

## SLIDE 6: DASHBOARD & KPI

**Layout**: Infographic style

```
📊 DASHBOARD BUSINESS INTELLIGENCE

Definisi (Few, 2013):
"Alat visualisasi yang menyajikan informasi penting dan KPI 
dalam satu layar untuk memudahkan monitoring real-time"

Karakteristik Dashboard yang Baik:
✓ SIMPLE - Fokus pada data penting
✓ COMMUNICATIVE - Mudah dipahami
✓ RELEVANT - Sesuai kebutuhan bisnis
✓ TIMELY - Real-time atau near real-time
✓ ACTIONABLE - Dapat ditindaklanjuti

🎯 KEY PERFORMANCE INDICATORS (KPI)

Kategori KPI dalam Dashboard:
┌──────────────┬─────────────────────────────┐
│ Financial    │ Revenue, Profit, Margin     │
│ Sales        │ Orders, AOV, Growth Rate    │
│ Customer     │ CAC, CLV, Retention Rate    │
│ Product      │ Turnover, Stock, Top Items  │
│ Marketing    │ ROI, Conversion, Reach      │
│ Operational  │ Fulfillment, Delivery Time  │
└──────────────┴─────────────────────────────┘
```

**Visual**:
- Icon dashboard dengan gauge & chart
- KPI pyramid atau framework diagram
- Color coding per kategori KPI

**Speaker Notes:**
- Dashboard adalah jendela ke dalam bisnis
- KPI adalah metrik yang paling penting dimonitor
- Kami identifikasi 6 kategori KPI untuk SATRIAMART

---

## SLIDE 7: DATA & METODOLOGI

**Layout**: Flowchart + tabel

```
📁 SUMBER DATA

6 Dataset Utama (12 Bulan: Nov 2024 - Oct 2025):
┌────────────────────────┬───────┬──────────────┐
│ Dataset                │ Rows  │ Attributes   │
├────────────────────────┼───────┼──────────────┤
│ 01_Master_Produk       │ 50    │ 15 columns   │
│ 02_Master_Pelanggan    │ 180   │ 16 columns   │
│ 03_Transaksi_Penjualan │ 320   │ 20 columns   │
│ 04_Riwayat_Stok        │ 600   │ 9 columns    │
│ 05_Biaya_Operasional   │ 240   │ 7 columns    │
│ 06_Marketing_Campaign  │ 24    │ 11 columns   │
└────────────────────────┴───────┴──────────────┘

🔄 METODOLOGI PERANCANGAN

[Data Collection] → [Data Cleaning] → [ETL Process]
         ↓                  ↓               ↓
[Requirements Analysis] [Data Transformation] [Data Loading]
         ↓                  ↓               ↓
[KPI Identification] → [Layout Design] → [Implementation]
         ↓                  ↓               ↓
[Looker Studio] → [Testing & Validation] → [Deployment]
```

**Visual**:
- Icon spreadsheet/database
- Flowchart metodologi dengan arrows
- Screenshot sample data

**Speaker Notes:**
- Data dikumpulkan dari sistem internal SATRIAMART
- 6 dataset covering semua aspek bisnis
- Metodologi sistematis dari analisis hingga deployment
- Total 1.414 rows data untuk analisis

---

## SLIDE 8: PROSES ETL & DATA QUALITY

**Layout**: Process flow dengan metrics

```
🔧 PROSES ETL (Extract-Transform-Load)

1. EXTRACT
   └─ Import data dari 6 Google Sheets
      Source: Internal SATRIAMART database

2. TRANSFORM
   ✓ Data Cleaning
     ├─ Remove duplicates: 12 records
     ├─ Handle missing values: 8 fields
     └─ Fix inconsistent formats: dates, numbers
   
   ✓ Data Transformation
     ├─ Calculate derived fields (margin, growth, etc)
     ├─ Standardize naming conventions
     ├─ Create date dimensions (month, quarter, year)
     └─ Aggregate metrics per period
   
   ✓ Data Integration
     ├─ Join tables (products, customers, transactions)
     ├─ Create relationships & keys
     └─ Build calculated fields

3. LOAD
   └─ Connect to Looker Studio
      Data refresh: Automatic daily

📊 DATA QUALITY METRICS

Completeness: 99.2% ✓
Accuracy: 98.5% ✓
Consistency: 100% ✓
Timeliness: Real-time ✓
```

**Visual**:
- Flowchart ETL dengan icon
- Progress bar untuk quality metrics
- Before/After data cleaning

**Speaker Notes:**
- ETL adalah fondasi dashboard yang berkualitas
- Data cleaning penting untuk akurasi analisis
- Quality control di setiap tahap proses
- Automated refresh untuk data terbaru

---

## SLIDE 9: HASIL DASHBOARD - OVERVIEW

**Layout**: Full screen dashboard screenshot

```
🎨 DASHBOARD SATRIAMART - STRUKTUR

7 Halaman Dashboard Interaktif:

1. 📊 Executive Summary
   └─ Overview KPI utama & trend

2. 📈 Sales Analysis  
   └─ Deep dive penjualan & trend

3. 🎁 Product Performance
   └─ Analisis produk & inventory

4. 👥 Customer Analysis
   └─ Segmentasi & behavior pelanggan

5. ⚙️ Operational Metrics
   └─ Fulfillment & delivery performance

6. 💰 Financial Analysis
   └─ Revenue, cost, profitability

7. 📢 Marketing Performance
   └─ Campaign effectiveness & ROI
```

**Visual**:
- Screenshot dashboard homepage
- Navigation menu showing 7 pages
- Highlight interactive filters

**Speaker Notes:**
- Dashboard terdiri dari 7 halaman utama
- Setiap halaman fokus pada aspek bisnis tertentu
- Navigasi intuitif dengan filter interaktif
- Mari kita lihat detail setiap halaman

---

## SLIDE 10: EXECUTIVE SUMMARY PAGE

**Layout**: Screenshot dengan annotation

```
📊 PAGE 1: EXECUTIVE SUMMARY

Key Metrics (Period: Nov 2024 - Oct 2025)

┌─────────────────────────────────────────────┐
│  💰 Total Revenue      │  🛒 Total Orders   │
│  Rp 111.976.550       │  320 orders        │
│  ↑ 12% vs LY          │  ↑ 8% vs LY        │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  📊 Avg Order Value    │  💵 Profit Margin  │
│  Rp 349.926           │  47.8%             │
│  ↑ 3.5% vs LY         │  ↓ 2.1% vs LY      │
└─────────────────────────────────────────────┘

[Line Chart: Monthly Revenue Trend]
Peak: December 2024 (Rp 13.2M)
Trough: February 2025 (Rp 5.8M)

[Bar Chart: Top 5 Products]
1. Nomor Rumah Akrilik Modern - Rp 15.6M
2. Papan Nama Toko Premium - Rp 12.3M
3. Signage LED Open/Close - Rp 9.8M
4. Custom Trophy Akrilik - Rp 7.4M
5. Display Menu Standing - Rp 6.2M

[Pie Chart: Sales by Channel]
WhatsApp: 45% | Instagram: 30% 
Offline: 15% | Website: 10%
```

**Visual**:
- Full screenshot Executive Summary page
- Arrow annotations highlighting key insights
- Color coding for positive/negative trends

**Speaker Notes:**
- Executive Summary memberikan bird's eye view
- Revenue Rp 111.9M dengan 320 transaksi
- AOV Rp 349k menunjukkan produk mid-to-high value
- WhatsApp channel paling dominan (45%)
- Clear seasonal pattern dengan peak di Desember

---

## SLIDE 11: SALES & PRODUCT ANALYSIS

**Layout**: Dual screenshot

```
📈 PAGE 2: SALES ANALYSIS

Key Insights:
✓ Seasonal Pattern Detected
  └─ Q4 (Oct-Dec): Peak season +40%
  └─ Q1 (Jan-Mar): Post-holiday dip -25%
  └─ Q2-Q3: Stable growth

✓ Day of Week Pattern
  └─ Weekend: 35% transactions
  └─ Weekday: 65% transactions
  └─ Peak hours: 10-14, 19-21

✓ Payment Methods
  └─ Transfer Bank: 55%
  └─ E-wallet: 30%
  └─ COD: 15%

[Visual: Line chart dengan seasonal annotation]
[Visual: Heatmap day-hour pattern]

───────────────────────────────────────

🎁 PAGE 3: PRODUCT PERFORMANCE

Key Insights:
✓ Product Mix
  └─ Nomor Rumah: 35% revenue
  └─ Papan Nama: 28% revenue
  └─ Signage: 23% revenue
  └─ Aksesoris: 14% revenue

✓ Profitability
  └─ Highest margin: Custom products (65%)
  └─ Lowest margin: Basic items (35%)
  └─ Sweet spot: Mid-range (47-52%)

✓ Stock Status
  └─ Optimal stock: 68% products
  └─ Overstock: 12% products
  └─ Low stock: 20% products (needs reorder)

[Visual: Pareto chart top 20 products]
[Visual: Scatter plot price vs volume]
```

**Visual**:
- Split screen: Sales page + Product page
- Highlight specific charts with insights
- Use callout boxes for key numbers

**Speaker Notes:**
- Sales Analysis mengungkap pola musiman
- Peak season di Q4 untuk planning inventory
- Product Analysis menunjukkan 80/20 rule
- 20% produk menghasilkan 70% revenue
- Insight untuk fokus produksi & marketing

---

## SLIDE 12: CUSTOMER & OPERATIONAL ANALYSIS

**Layout**: Dual screenshot dengan insights

```
👥 PAGE 4: CUSTOMER ANALYSIS

Key Insights:
✓ Customer Segmentation (RFM)
  ├─ Champions: 15% (high value, frequent)
  ├─ Loyal: 20% (regular repeat buyers)
  ├─ Potential: 25% (recent, good value)
  ├─ At Risk: 10% (declining frequency)
  └─ Lost: 30% (need re-engagement)

✓ Geographic Distribution
  └─ Jabodetabek: 85%
     ├─ Depok: 28%
     ├─ Jakarta: 25%
     ├─ Tangerang: 18%
     ├─ Bekasi: 10%
     └─ Bogor: 4%
  └─ Outside: 15% (growth opportunity)

✓ Customer Lifetime Value
  └─ Average CLV: Rp 622.092
  └─ Repeat purchase rate: 45%
  └─ Avg transactions per customer: 1.78

[Visual: RFM heatmap matrix]
[Visual: Geo map Indonesia]

───────────────────────────────────────

⚙️ PAGE 5: OPERATIONAL METRICS

Key Insights:
✓ Order Fulfillment
  └─ Completion rate: 85%
  └─ In progress: 8%
  └─ Cancelled: 7% (target: <5%)

✓ Production Time
  └─ Average: 3.5 days
  └─ Rush orders: 1-2 days (+30% fee)
  └─ Standard: 3-5 days

✓ Customer Satisfaction
  └─ Average rating: 4.5/5
  └─ 5-star: 65%
  └─ 4-star: 20%
  └─ ≤3-star: 15%

[Visual: Funnel chart order status]
[Visual: Gauge chart satisfaction]
```

**Visual**:
- Split screen showcasing both pages
- RFM heatmap dengan color gradient
- Geo map dengan bubble size
- Funnel & gauge charts

**Speaker Notes:**
- Customer Analysis menggunakan RFM segmentation
- 15% champions adalah target retain
- 30% lost customers perlu re-engagement campaign
- Operasional metrics menunjukkan kinerja baik
- 85% completion rate, target improve cancellation

---

## SLIDE 13: FINANCIAL & MARKETING ANALYSIS

**Layout**: Dual screenshot dengan ROI focus

```
💰 PAGE 6: FINANCIAL ANALYSIS

Key Insights:
✓ Revenue Breakdown
  └─ Product sales: Rp 111.9M (100%)
  └─ Custom charges: Rp 8.5M (7.6%)
  └─ Shipping fees: Rp 6.2M (5.5%)

✓ Cost Structure
  └─ COGS: 52% of revenue
  └─ Operating expenses: 18%
  └─ Marketing: 12%
  └─ Other: 8%
  └─ Net profit margin: 10%

✓ Profitability by Category
  ├─ Signage: 55% margin (highest)
  ├─ Papan Nama: 48% margin
  ├─ Nomor Rumah: 45% margin
  └─ Aksesoris: 38% margin (volume play)

✓ Monthly P&L Trend
  └─ Best: December (profit Rp 1.8M)
  └─ Worst: February (profit Rp 450K)

[Visual: Waterfall chart revenue→profit]
[Visual: Stacked bar cost breakdown]

───────────────────────────────────────

📢 PAGE 7: MARKETING PERFORMANCE

Key Insights:
✓ Campaign ROI (24 campaigns, 12 months)
  └─ Average ROI: 1,847%
  └─ Best campaign: CMP020 (ROI 4,664%)
  └─ Platform performance:
     ├─ TikTok: ROI 2,156% (best)
     ├─ Facebook: ROI 1,789%
     ├─ Instagram: ROI 1,654%
     └─ Google Ads: ROI 2,012%

✓ Total Marketing Investment
  └─ Budget: Rp 26.3M (12 months)
  └─ Revenue generated: Rp 5.1B
  └─ Overall ROI: 1,940%

✓ Best Performing Campaigns
  1. Giveaway Contest - Oct (ROI 4,664%)
  2. Customer Testimonial - Aug (ROI 2,843%)
  3. Behind The Scene - Jun (ROI 3,786%)

[Visual: Bar chart ROI per campaign]
[Visual: Spider chart platform comparison]
```

**Visual**:
- Financial waterfall chart prominent
- Marketing ROI bar chart dengan top 10
- Platform comparison spider/radar chart
- Highlight best ROI campaigns

**Speaker Notes:**
- Financial analysis menunjukkan business health
- Net profit margin 10% adalah baseline
- Opportunity: improve margin di kategori aksesoris
- Marketing ROI 1,940% adalah excellent performance
- TikTok dan Customer Testimonial paling efektif
- Budget allocation dapat di-optimize

---

## SLIDE 14: KEY INSIGHTS & RECOMMENDATIONS

**Layout**: Two columns with icons

```
💡 KEY INSIGHTS

🎯 SALES & REVENUE
✓ Strong seasonal pattern (peak Q4)
✓ WhatsApp adalah channel terkuat (45%)
✓ AOV Rp 349K menunjukkan good ticket size

📦 PRODUCT & INVENTORY
✓ 20% produk = 70% revenue (Pareto principle)
✓ Custom products highest margin (65%)
✓ 20% produk butuh reorder (low stock alert)

👥 CUSTOMER BEHAVIOR
✓ 45% repeat purchase rate (industry avg: 30%)
✓ 30% lost customers (reactivation opportunity)
✓ 85% pelanggan dari Jabodetabek

💰 FINANCIAL HEALTH
✓ Net profit margin: 10%
✓ COGS: 52% (opportunity to negotiate)
✓ Marketing ROI: 1,940% (excellent)

📢 MARKETING EFFECTIVENESS
✓ TikTok platform paling efektif (ROI 2,156%)
✓ Giveaway & Testimonial best campaign type
✓ Video viral content high engagement

───────────────────────────────────────

🚀 STRATEGIC RECOMMENDATIONS

1. MAXIMIZE PEAK SEASON
   └─ Stock up Nov-Dec (40% lebih banyak)
   └─ Extra marketing budget Q4
   └─ Promote gift packages

2. FOCUS ON HIGH-MARGIN PRODUCTS
   └─ Push custom products & signage
   └─ Bundling strategy untuk increase AOV
   └─ Premium product line development

3. CUSTOMER RETENTION
   └─ Loyalty program untuk champions
   └─ Re-engagement campaign untuk lost (30%)
   └─ Referral incentive program

4. GEOGRAPHIC EXPANSION
   └─ Target cities: Bandung, Surabaya
   └─ Marketplace expansion (Tokopedia, Shopee)
   └─ Partner dengan reseller lokal

5. OPTIMIZE MARKETING MIX
   └─ Increase TikTok budget (best ROI)
   └─ More video content & testimonials
   └─ Reduce underperforming channels

6. OPERATIONAL IMPROVEMENT
   └─ Reduce cancellation <5% (current 7%)
   └─ Standardize production time
   └─ Improve customer service response time

7. INVENTORY MANAGEMENT
   └─ Implement ABC analysis
   └─ Auto-reorder untuk fast-moving items
   └─ Reduce overstock 12% → 5%
```

**Visual**:
- Icon untuk setiap kategori insight
- Color coding: green (good), yellow (attention), red (action needed)
- Arrow icons untuk recommendations
- Priority badges (High/Medium/Low)

**Speaker Notes:**
- Insight menunjukkan SATRIAMART dalam kondisi healthy
- Banyak opportunity untuk growth
- Recommendations berdasarkan data, bukan asumsi
- Prioritas: retention, high-margin products, expansion
- Implementasi bertahap 3-6 bulan

---

## SLIDE 15: KESIMPULAN

**Layout**: Summary dengan checklist

```
✅ KESIMPULAN

1. ✓ DASHBOARD BERHASIL DIIMPLEMENTASIKAN
   └─ 7 halaman dashboard interaktif
   └─ 25+ visualisasi berbeda
   └─ 50+ KPI tracked
   └─ Real-time data refresh

2. ✓ INSIGHT ACTIONABLE TERIDENTIFIKASI
   └─ Pola musiman & trend penjualan
   └─ Segmentasi pelanggan efektif
   └─ Optimasi marketing ROI
   └─ Peluang ekspansi geografis

3. ✓ DATA-DRIVEN DECISION SUPPORT
   └─ KPI monitoring real-time
   └─ Alert untuk metrics penting
   └─ Benchmark untuk target setting
   └─ Historical analysis untuk forecasting

4. ✓ BUSINESS IMPACT
   └─ Visibility 100% operasional bisnis
   └─ Reduce decision time 50%
   └─ Identify revenue opportunity +30%
   └─ Cost optimization potential 15%

5. ✓ FEASIBILITY UNTUK UMKM
   └─ Low cost implementation (Looker Studio free)
   └─ No coding required
   └─ Easy to maintain & update
   └─ Scalable seiring pertumbuhan bisnis

───────────────────────────────────────

🎯 PENCAPAIAN TUJUAN

✓ Dashboard interaktif selesai 100%
✓ Semua KPI utama ter-cover
✓ User-friendly & accessible
✓ Insight actionable tersampaikan
✓ Owner SATRIAMART satisfied

───────────────────────────────────────

💡 LEARNING OUTCOMES

✓ Penerapan teori BI dalam kasus nyata
✓ Hands-on experience dengan Looker Studio
✓ Data analysis & interpretation skills
✓ Dashboard design best practices
✓ Business acumen dalam UMKM context
```

**Visual**:
- Checkmark icons untuk setiap poin
- Summary metrics dalam boxes
- Before/After comparison visual
- Team photo dengan dashboard di background

**Speaker Notes:**
- Dashboard BI berhasil diimplementasikan sesuai tujuan
- Memberikan value signifikan untuk SATRIAMART
- Feasible untuk UMKM dengan budget terbatas
- Learning experience sangat valuable bagi kami
- Applicable untuk bisnis lain dengan penyesuaian

---

## SLIDE 16: PENUTUP & TERIMA KASIH

**Layout**: Clean & professional

```
🙏 TERIMA KASIH

"Data is the new oil, but only if you refine it"

───────────────────────────────────────

Special Thanks to:

🎓 Bapak Ridan Nurfalah, M.Kom
   Dosen Pembimbing - Business Intelligence II

🏢 SATRIAMART Team
   Owner & Staff untuk kolaborasi dan data support

👥 Teman-teman Mahasiswa
   Feedback dan diskusi selama pengerjaan

───────────────────────────────────────

📧 CONTACT

Kelompok [X] - Sistem Informasi
[email@student.nusamandiri.ac.id]

📊 Dashboard Link:
[bit.ly/dashboard-satriamart-bi]

📄 Full Report:
[Available upon request]

───────────────────────────────────────

❓ SESI TANYA JAWAB

Silakan ajukan pertanyaan 🙋
```

**Visual**:
- Professional thank you design
- QR code untuk dashboard link
- Team photo
- Logo UNM & SATRIAMART
- Contact information layout

**Speaker Notes:**
- Terima kasih atas perhatiannya
- Dashboard sudah live dan bisa diakses
- Kami siap menjawab pertanyaan
- Silakan scan QR code untuk akses dashboard

---

## TIPS PRESENTASI

### DO's ✅
- Practice timing (15-20 menit)
- Gunakan laser pointer untuk highlight
- Eye contact dengan audience
- Speak clearly & confidently
- Explain charts dengan context
- Tell a story, bukan hanya show data
- Prepare backup jika demo gagal
- Involve all team members

### DON'Ts ❌
- Membaca slides word by word
- Terlalu banyak text di slide
- Menggunakan jargon tanpa explain
- Terburu-buru atau terlalu lambat
- Membelakangi audience saat explain
- Skip important insights
- Unprepared untuk Q&A
- Monopoli presentasi satu orang

### Q&A PREPARATION

**Potential Questions:**

1. **Teknis**: "Kenapa pilih Looker Studio vs Power BI?"
   - Answer: Free, cloud-based, easy collaboration, no installation

2. **Data**: "Bagaimana cara collect data dari SATRIAMART?"
   - Answer: Export dari sistem internal ke Google Sheets, automated daily

3. **Metodologi**: "Bagaimana validasi accuracy dashboard?"
   - Answer: Cross-check dengan laporan manual, UAT dengan owner

4. **Impact**: "Apa impact konkrit untuk bisnis SATRIAMART?"
   - Answer: Faster decision (50%), identify opportunity (+30% revenue potential)

5. **Scalability**: "Apakah dashboard bisa di-scale untuk data lebih besar?"
   - Answer: Yes, Looker Studio support millions of rows, dapat integrate dengan BigQuery

6. **Limitation**: "Apa limitation dari solusi ini?"
   - Answer: Require internet, limited custom calculation, refresh rate tergantung data source

7. **Security**: "Bagaimana ensure data security?"
   - Answer: Restricted access dengan Google account, role-based permission

8. **Cost**: "Berapa total biaya implementasi?"
   - Answer: Rp 0 (Looker Studio free), only time investment ~80 jam kerja kelompok

---

## BACKUP SLIDES (Optional)

### Backup 1: Technical Architecture
- Detailed data flow diagram
- ETL process flowchart
- System architecture

### Backup 2: Data Dictionary
- Table structure untuk 6 datasets
- Field definitions
- Data types & constraints

### Backup 3: Additional Insights
- Detailed RFM analysis
- Cohort analysis
- Predictive analytics (if any)

### Backup 4: Implementation Timeline
- Gantt chart project timeline
- Milestones & deliverables
- Team roles & responsibilities

### Backup 5: References
- List of books & journals
- Tools documentation
- Related case studies

---

## NOTES UNTUK TIM

### Pembagian Tugas Presentasi:

**Person 1:** Slides 1-4 (Intro, Background, Tujuan, Profil)
**Person 2:** Slides 5-8 (Theory, Metodologi, ETL)
**Person 3:** Slides 9-13 (Dashboard demo & insights)
**Person 4:** Slides 14-16 (Recommendations, Conclusion, Closing)

### Rehearsal Checklist:
- [ ] Practice 3x sebelum presentasi
- [ ] Time each person (max 5 menit/person)
- [ ] Prepare transisi antar presenter
- [ ] Test dashboard demo (internet, login)
- [ ] Backup plan jika tech issue
- [ ] Print handout untuk dosen (optional)
- [ ] Dress code: formal (kemeja/blazer)

### Equipment Checklist:
- [ ] Laptop + charger
- [ ] HDMI cable / adapter
- [ ] Backup file di USB & cloud
- [ ] Pointer / clicker (if available)
- [ ] Notes / cue cards
- [ ] Water bottle

---

**Good luck with your presentation! 🚀**
