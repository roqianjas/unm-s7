# 📊 TUGAS AKHIR BUSINESS INTELLIGENCE - SATRIAMART

## Informasi Umum

**Mata Kuliah:** Business Intelligence  
**Topik:** Implementasi Dashboard BI Interaktif untuk UMKM SATRIAMART  
**Tool:** Looker Studio (Google Data Studio)  
**Periode Analisis:** November 2024 - Oktober 2025 (12 bulan)  
**Industri:** Retail - Produk Akrilik Dekorasi Custom

---

## 📁 Struktur Folder

```
05_business_intelligence/
├── README.md                          # File ini - Overview project
├── BRIEF_TUGAS_BUSINESS_INTELLIGENCE.md  # Spesifikasi lengkap assignment
├── PANDUAN_IMPLEMENTASI.md            # Step-by-step implementation guide
│
├── data/                              # Dataset & scripts
│   ├── README.md                      # Dokumentasi data
│   ├── generate_all_data.py          # Python script untuk generate data
│   ├── 01_master_produk.csv          # 50 produk akrilik
│   ├── 02_master_pelanggan.csv       # 180 customer records
│   ├── 03_transaksi_penjualan.csv    # 320 transaksi
│   ├── 04_riwayat_stok.csv           # (Optional) Stock movement history
│   ├── 05_biaya_operasional.csv      # (Optional) Operational costs
│   └── 06_marketing_campaign.csv     # (Optional) Marketing campaigns
│
├── laporan/                           # Laporan akademik
│   ├── LAPORAN_BI_SATRIAMART_BAB_I.md    # Pendahuluan
│   ├── LAPORAN_BI_SATRIAMART_BAB_II.md   # Landasan Teori
│   ├── LAPORAN_BI_SATRIAMART_BAB_III.md  # Pembahasan & Analisis
│   ├── LAPORAN_BI_SATRIAMART_BAB_IV.md   # Kesimpulan & Saran
│   ├── DAFTAR_PUSTAKA.md              # Bibliography (APA format)
│   ├── COVER.md                       # (TODO) Cover page
│   ├── KATA_PENGANTAR.md              # (TODO) Preface
│   ├── ABSTRAK.md                     # (TODO) Abstract
│   └── LAMPIRAN.md                    # (TODO) Appendices
│
├── presentasi/                        # (TODO) Presentation materials
│   ├── PRESENTASI_BI_SATRIAMART.pptx # PowerPoint slides
│   └── SCRIPT_PRESENTASI.md          # Presentation script
│
├── dashboard/                         # (TODO) Dashboard files
│   ├── LINK_DASHBOARD.txt            # Looker Studio dashboard URL
│   ├── screenshot_page1.png          # Executive Summary
│   ├── screenshot_page2.png          # Sales Analysis
│   ├── screenshot_page3.png          # Product Performance
│   ├── screenshot_page4.png          # Customer Analysis
│   ├── screenshot_page5.png          # Operational Metrics
│   ├── screenshot_page6.png          # Financial Analysis
│   └── screenshot_page7.png          # Marketing Performance
│
└── deliverables/                      # (TODO) Final submission files
    ├── LAPORAN_BI_SATRIAMART.docx    # Final report (MS Word)
    ├── LAPORAN_BI_SATRIAMART.pdf     # PDF version
    └── PRESENTASI_BI_SATRIAMART.pptx # Final presentation
```

---

## 🎯 Ringkasan Project

### Objektif
Merancang dan mengimplementasikan dashboard Business Intelligence interaktif untuk membantu SATRIAMART dalam:
1. Monitoring performa penjualan real-time
2. Analisis perilaku pelanggan
3. Optimasi inventory dan produk
4. Evaluasi efektivitas channel penjualan
5. Pengambilan keputusan berbasis data

### Metodologi
- **Data Collection**: Simulation data generation (Python)
- **Data Storage**: Google Sheets (Cloud)
- **Data Visualization**: Looker Studio
- **Analysis Framework**: Descriptive & Diagnostic Analytics
- **Reporting**: Academic paper format (Bahasa Indonesia formal)

### Key Metrics (KPI)
1. **Revenue Metrics**
   - Total Revenue: Rp 111.976.550
   - Monthly Average: Rp 9.331.379
   - Growth Rate: 12,4% (trend)

2. **Transaction Metrics**
   - Total Transaksi: 320 orders
   - Average Order Value (AOV): Rp 349.926
   - Completion Rate: 85%

3. **Customer Metrics**
   - Total Customers: 180 active
   - Repeat Purchase Rate: 15%
   - Customer Satisfaction: 4.2/5.0

4. **Product Metrics**
   - Total SKU: 50 products
   - Best Category: Nomor Rumah (45% revenue)
   - Average Margin: 25%

5. **Channel Performance**
   - WhatsApp: 45% (Rp 50,4M)
   - Instagram: 30% (Rp 33,6M)
   - Website: 15% (Rp 16,8M)
   - Offline: 10% (Rp 11,2M)

---

## 🚀 Quick Start Guide

### Untuk Reviewer/Dosen

**Option 1: Review Dokumentasi**
1. Baca `BRIEF_TUGAS_BUSINESS_INTELLIGENCE.md` untuk full assignment spec
2. Review laporan di folder `laporan/` (BAB I-IV)
3. Check data quality di folder `data/`

**Option 2: View Dashboard** (setelah implementasi)
1. Open link di `dashboard/LINK_DASHBOARD.txt`
2. Explore 7 halaman dashboard interaktif
3. Review screenshots jika dashboard belum live

**Option 3: Reproducibility Test**
```bash
cd data/
python3 generate_all_data.py
# Verify output: 3 CSV files generated
```

### Untuk Implementor

**Step 1: Setup Environment**
```bash
# Pastikan Python 3.x installed
python3 --version

# Install dependencies (if any)
pip install pandas numpy

# Navigate to project folder
cd /var/www/unm-s7/tugas-selesai/05_business_intelligence/
```

**Step 2: Generate/Verify Data**
```bash
cd data/
python3 generate_all_data.py
ls -lh *.csv
```

**Step 3: Follow Implementation Guide**
- Baca `PANDUAN_IMPLEMENTASI.md` secara menyeluruh
- Follow step-by-step dari Tahap 1 sampai Tahap 5
- Estimated time: 8-12 hours total

**Step 4: Create Dashboard**
- Upload data ke Google Sheets
- Connect ke Looker Studio
- Build 7 pages dashboard
- Test dan deploy

**Step 5: Finalize Report**
- Compile chapters BAB I-IV ke MS Word
- Add front matter (cover, kata pengantar, abstrak, daftar isi)
- Insert dashboard screenshots
- Add appendices
- Convert to PDF

---

## 📊 Dashboard Pages Overview

### Page 1: Executive Summary
**Audience:** Management, Stakeholders  
**Purpose:** High-level overview of business performance  
**Contents:**
- KPI Scorecards (6 metrics)
- Revenue trend (12 months)
- Revenue by channel (bar chart)
- Revenue by category (pie chart)

### Page 2: Sales Analysis
**Audience:** Sales Team, Management  
**Purpose:** Deep dive into sales patterns  
**Contents:**
- Top 10 products by revenue
- Top 10 products by quantity
- Sales by day of week
- Sales by hour
- Transaction details table

### Page 3: Product Performance
**Audience:** Inventory Manager, Product Team  
**Purpose:** Product-level insights for inventory optimization  
**Contents:**
- Product profitability analysis
- Category comparison
- Stock turnover rate
- Slow-moving products alert

### Page 4: Customer Analysis
**Audience:** Marketing Team, CRM  
**Purpose:** Customer behavior and segmentation insights  
**Contents:**
- Customer segmentation (RFM)
- Top customers by value
- Customer lifetime value
- Geographic distribution
- Customer type breakdown

### Page 5: Operational Metrics
**Audience:** Operations Team  
**Purpose:** Operational efficiency monitoring  
**Contents:**
- Order completion rate
- Average processing time
- Custom order percentage
- Delivery performance

### Page 6: Financial Analysis
**Audience:** Finance Team, Management  
**Purpose:** Financial health and profitability  
**Contents:**
- Profit margin trends
- Cost breakdown
- Revenue vs costs
- Cash flow indicators

### Page 7: Marketing Performance
**Audience:** Marketing Team  
**Purpose:** Marketing effectiveness evaluation  
**Contents:**
- Campaign ROI
- Channel effectiveness
- Customer acquisition cost
- Conversion rates

---

## 🔬 Metodologi Penelitian

### 1. Tahap Persiapan
- **Studi Literatur**: Review teori BI, dashboard design, KPI definition
- **Requirement Analysis**: Interview stakeholder, identify KPIs
- **Tool Selection**: Looker Studio (free, cloud-based, user-friendly)

### 2. Tahap Pengumpulan Data
- **Data Generation**: Python script untuk simulate realistic business data
- **Data Validation**: Check data quality, consistency, completeness
- **Data Documentation**: Maintain data dictionary

### 3. Tahap Perancangan
- **Dashboard Design**: Wireframe 7 pages, define visualizations
- **Data Modeling**: Design star schema, define relationships
- **Calculated Metrics**: Define formulas for KPIs

### 4. Tahap Implementasi
- **Data Upload**: Google Sheets setup
- **Dashboard Development**: Looker Studio implementation
- **Interactivity**: Filters, drill-downs, cross-filtering

### 5. Tahap Pengujian
- **Functional Testing**: Verify calculations, filters, navigation
- **User Testing**: Collect feedback from stakeholders
- **Performance Testing**: Load time, responsiveness

### 6. Tahap Deployment
- **Sharing Setup**: Configure access permissions
- **Training**: User guides, video tutorials
- **Documentation**: Comprehensive documentation

---

## 📝 Komponen Laporan

### BAB I: Pendahuluan (7 halaman)
- Latar belakang masalah UMKM dan pentingnya BI
- Rumusan masalah (5 poin)
- Tujuan penelitian (5 poin)
- Manfaat penelitian (praktis & akademis)
- Ruang lingkup dan batasan

### BAB II: Landasan Teori (15+ halaman)
- Konsep Business Intelligence
- Dashboard dan Key Performance Indicator (KPI)
- Proses ETL (Extract, Transform, Load)
- Google Looker Studio
- Sumber data untuk BI
- Metodologi perancangan dashboard

### BAB III: Pembahasan (20+ halaman)
- Profil bisnis SATRIAMART
- Analisis kebutuhan dashboard
- Perancangan visualisasi
- Implementasi dashboard (7 halaman detail)
- Interpretasi hasil & insights

### BAB IV: Penutup (10+ halaman)
- Kesimpulan (10 poin)
- Saran untuk SATRIAMART (6 poin)
- Saran pengembangan dashboard (5 poin)

### Daftar Pustaka
- 7+ referensi primer (buku, dokumentasi official)
- 5+ jurnal ilmiah (2020-2025)
- Format APA 7th edition
- Managed dengan Mendeley

---

## 🛠️ Technical Stack

### Data Generation & Processing
- **Python 3.x**: Data generation script
  - Libraries: `random`, `datetime`, `csv`
- **CSV Format**: Standard comma-separated values
- **Encoding**: UTF-8

### Data Storage
- **Google Sheets**: Cloud spreadsheet
  - 6 worksheets (data tables)
  - Calculated fields dengan QUERY formulas
  - Shared access untuk collaboration

### Visualization & BI
- **Looker Studio**: Free BI platform
  - Data sources: Google Sheets connector
  - Charts: Scorecards, line, bar, pie, table, geo maps
  - Features: Filters, date range, drill-down, cross-filtering

### Documentation
- **Markdown**: Technical documentation format
- **Microsoft Word**: Final report (target .docx)
- **Microsoft PowerPoint**: Presentation slides
- **Mendeley**: Reference management

---

## 📚 References & Resources

### Official Documentation
- [Looker Studio Help Center](https://support.google.com/looker-studio)
- [Google Sheets Documentation](https://support.google.com/docs)
- [Python CSV Module](https://docs.python.org/3/library/csv.html)

### Academic References
Key references used in this project:
- Turban, E., et al. (2021). *Business Intelligence and Analytics: Systems for Decision Support*
- Howson, C., et al. (2021). *Successful Business Intelligence*
- Antonius, R. (2023). *Looker Studio: Panduan Praktis untuk Pemula*
- Davenport, T. H., & Harris, J. (2020). *Competing on Analytics*

### Related Work
- Previous CRM project: `/tugas-selesai/01_tugas_manajemen_hubungan_pelanggan/`
- Company profile: `/company_profile_satriamart.md`
- Business analysis: `/analisis-kelayakan/analisis_kelayakan_satriamart.md`

---

## ✅ Checklist Progress

### ✅ Phase 1: Preparation (DONE)
- [x] Brief document created
- [x] Directory structure setup
- [x] Requirements analysis documented

### ⏳ Phase 2: Data Preparation (IN PROGRESS - 50%)
- [x] Master produk (50 records)
- [x] Master pelanggan (180 records)
- [x] Transaksi penjualan (320 records)
- [ ] Riwayat stok (optional)
- [ ] Biaya operasional (optional)
- [ ] Marketing campaign (optional)

### ⏳ Phase 3: Dashboard Implementation (PENDING)
- [ ] Google Sheets upload
- [ ] Data source configuration
- [ ] Page 1: Executive Summary
- [ ] Page 2: Sales Analysis
- [ ] Page 3: Product Performance
- [ ] Page 4: Customer Analysis
- [ ] Page 5: Operational Metrics
- [ ] Page 6: Financial Analysis
- [ ] Page 7: Marketing Performance
- [ ] Testing & refinement

### ⏳ Phase 4: Report Writing (IN PROGRESS - 80%)
- [x] BAB I: Pendahuluan
- [x] BAB II: Landasan Teori
- [x] BAB III: Pembahasan (content complete, needs screenshots)
- [x] BAB IV: Penutup
- [x] Daftar Pustaka
- [ ] Cover page
- [ ] Kata Pengantar
- [ ] Abstrak (complete version)
- [ ] Daftar Isi
- [ ] Daftar Gambar
- [ ] Daftar Tabel
- [ ] Lampiran
- [ ] MS Word formatting & assembly

### ❌ Phase 5: Presentation (PENDING)
- [ ] PowerPoint slides (16 slides)
- [ ] Presentation script
- [ ] Dashboard demo preparation

### ❌ Phase 6: Final Submission (PENDING)
- [ ] Final report (DOCX + PDF)
- [ ] Presentation (PPTX)
- [ ] Dashboard link
- [ ] Supporting files
- [ ] Submission package

---

## 🎓 Grading Criteria

Total: **100 points**

### 1. Dashboard Implementation (40 points)
- Data quality & completeness: 10 pts
- Visualization design: 10 pts
- Interactivity & usability: 10 pts
- Technical implementation: 10 pts

### 2. Written Report (30 points)
- Content depth & accuracy: 10 pts
- Analysis quality: 10 pts
- Writing quality (KBBI standard): 5 pts
- Formatting & references: 5 pts

### 3. Presentation (20 points)
- Clarity & structure: 10 pts
- Delivery & communication: 10 pts

### 4. Innovation & Insights (10 points)
- Unique insights: 5 pts
- Actionable recommendations: 5 pts

---

## 💡 Key Insights from Analysis

### Business Insights
1. **Seasonal Patterns**: Peak sales in Q4 (Oct-Dec) - gift season
2. **Channel Performance**: WhatsApp dominates (45%) - optimize this channel
3. **Customer Behavior**: Low repeat rate (15%) - need retention strategy
4. **Product Mix**: Nomor Rumah contributes 45% revenue - focus category
5. **Geographic**: 85% customers from Jabodetabek - expansion opportunity

### Operational Insights
1. **Inventory**: Need better stock management for custom orders
2. **Processing**: 15% incomplete orders - investigate root cause
3. **Delivery**: On-time delivery critical for satisfaction
4. **Pricing**: Healthy margin (25%) but room for optimization
5. **Marketing**: Low marketing spend ROI - need better targeting

### Strategic Recommendations
1. **Customer Retention**: Implement loyalty program, follow-up system
2. **Channel Optimization**: Invest in WhatsApp Business API automation
3. **Product Development**: Expand "Nomor Rumah" product line
4. **Geographic Expansion**: Target cities outside Jabodetabek
5. **Data-Driven Culture**: Regular dashboard review meetings

---

## 📞 Support & Contact

### For Technical Issues
- Refer to `PANDUAN_IMPLEMENTASI.md`
- Check Troubleshooting section
- Looker Studio community forums

### For Academic Questions
- Contact: Dosen Pengampu Mata Kuliah Business Intelligence
- Office Hours: [sesuai jadwal dosen]

### For Data Issues
- Check `data/README.md` for documentation
- Review Python script: `generate_all_data.py`
- Validate data dengan provided formulas

---

## 📄 License & Usage

### Academic Use
This project is created for educational purposes as part of Business Intelligence course at Universitas Negeri Makassar (UNM).

### Data Privacy
All data used in this project is **simulated/synthetic**. No real customer data was used.

### Reuse & Attribution
- Feel free to reuse methodology and structure for similar projects
- Please provide attribution if using significant portions
- Modify as needed for different business contexts

---

## 🏆 Acknowledgments

### Tools & Platforms
- **Google Looker Studio**: Free BI platform
- **Google Sheets**: Cloud data storage
- **Python**: Data generation
- **Mendeley**: Reference management

### Learning Resources
- Looker Studio official documentation
- YouTube tutorials on data visualization
- Academic papers on BI implementation

### Inspiration
- Previous course projects (CRM, IT Governance, etc.)
- UMKM SATRIAMART business case
- Real-world BI implementations

---

## 📅 Version History

### Version 1.0 (Current)
- Initial project setup
- Data generation complete (3/6 tables)
- Report chapters complete (BAB I-IV)
- Implementation guide created
- Documentation structured

### Planned Updates
- Version 1.1: Complete all 6 data tables
- Version 1.2: Dashboard implementation
- Version 1.3: Final report assembly
- Version 1.4: Presentation materials
- Version 2.0: Final submission package

---

**Last Updated:** January 2025  
**Status:** 🔄 In Progress (60% complete)  
**Next Milestone:** Dashboard Implementation (Fase 3)

---

## 🔗 Quick Links

- **Main Brief**: [BRIEF_TUGAS_BUSINESS_INTELLIGENCE.md](./BRIEF_TUGAS_BUSINESS_INTELLIGENCE.md)
- **Implementation Guide**: [PANDUAN_IMPLEMENTASI.md](./PANDUAN_IMPLEMENTASI.md)
- **Data Documentation**: [data/README.md](./data/README.md)
- **Report BAB I**: [laporan/LAPORAN_BI_SATRIAMART_BAB_I.md](./laporan/LAPORAN_BI_SATRIAMART_BAB_I.md)
- **Report BAB II**: [laporan/LAPORAN_BI_SATRIAMART_BAB_II.md](./laporan/LAPORAN_BI_SATRIAMART_BAB_II.md)
- **Report BAB III**: [laporan/LAPORAN_BI_SATRIAMART_BAB_III.md](./laporan/LAPORAN_BI_SATRIAMART_BAB_III.md)
- **Report BAB IV**: [laporan/LAPORAN_BI_SATRIAMART_BAB_IV.md](./laporan/LAPORAN_BI_SATRIAMART_BAB_IV.md)
- **Bibliography**: [laporan/DAFTAR_PUSTAKA.md](./laporan/DAFTAR_PUSTAKA.md)

---

**End of README**

Semoga proyek Business Intelligence ini bermanfaat! 🎓📊

