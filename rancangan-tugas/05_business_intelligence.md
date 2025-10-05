# RANCANGAN TUGAS MATA KULIAH
## BUSINESS INTELLIGENCE

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Semester 7**

---

### INFORMASI DASAR TUGAS

**Mata Kuliah:** Business Intelligence II  
**Kode:** 493  
**SKS:** 4  
**Dosen Pengampu:** Ridan Nurfalah, M.Kom  
**Objek Studi:** SATRIAMART - Dekorasi & Aksesoris Akrilik  
**Durasi Pengerjaan:** 9 minggu (Final Project)

---

### TUJUAN PEMBELAJARAN

**Capaian Pembelajaran Mata Kuliah (CPMK):**
CPMK043: Mampu menerapkan pendekatan sistem berorientasi atas pencapaian hasil kerja kelompok dan melakukan supervisi dan evaluasi terhadap penyelesaian pekerjaan yang ditugaskan kepada pekerja yang berada di bawah tanggung jawabnya. (CPL04)

**Tujuan Khusus:**
1. Merancang dan mengimplementasikan solusi Business Intelligence untuk SATRIAMART
2. Mengembangkan dashboard interaktif untuk mendukung decision making
3. Melakukan analisis data untuk mengidentifikasi business insights
4. Mendemonstrasikan kemampuan leadership dalam project management

---

### DESKRIPSI TUGAS

Mahasiswa akan merancang dan mengimplementasikan sistem Business Intelligence komprehensif untuk SATRIAMART, mencakup data warehouse design, ETL processes, analytics dashboard, dan predictive modeling untuk mendukung strategic business decisions.

---

### METODOLOGI PENGERJAAN

**BI Development Lifecycle:**
1. **Business Requirements Analysis**
2. **Data Source Identification & Assessment**
3. **Data Warehouse Design & Implementation**
4. **ETL Development & Data Integration**
5. **OLAP Cube Development**
6. **Dashboard & Reporting Development**
7. **Advanced Analytics & Data Mining**
8. **Testing & Validation**
9. **Deployment & User Training**

**Technical Approach:**
- **Data Warehouse:** Dimensional modeling approach
- **ETL Process:** Extract, Transform, Load dengan data quality checks
- **Analytics Platform:** Tableau, Power BI, atau open-source alternatives
- **Advanced Analytics:** Python/R untuk predictive modeling

---

### SCOPE PROYEK BUSINESS INTELLIGENCE

**Business Areas untuk Analysis:**

#### 1. **Sales Performance Analytics**
- Revenue trends analysis (monthly, quarterly, yearly)
- Product performance comparison
- Customer segment profitability analysis
- Sales forecasting dan demand planning

#### 2. **Customer Analytics**
- Customer segmentation based pada purchase behavior
- Customer lifetime value analysis
- Customer acquisition dan retention metrics
- Cross-selling dan up-selling opportunities

#### 3. **Operations Analytics**
- Production efficiency metrics
- Inventory turnover analysis
- Supply chain performance
- Quality control analytics

#### 4. **Financial Analytics**
- Profitability analysis by product/customer
- Cost structure analysis
- Cash flow forecasting
- ROI analysis untuk marketing campaigns

---

### DELIVERABLES

#### 1. **Business Intelligence Strategy Document** (20%)
**Format:** Executive-level strategic document

**Konten:**
- **Business Case untuk BI Implementation**
  - Current state analysis
  - Business objectives alignment
  - Expected ROI dan benefits
  
- **BI Architecture Design**
  - Data architecture blueprint
  - Technology stack selection
  - Integration strategy
  
- **Implementation Roadmap**
  - Phase-wise implementation plan
  - Resource requirements
  - Success metrics definition

#### 2. **Data Warehouse Implementation** (25%)
**Format:** Technical documentation + working database

**Konten:**
- **Data Model Documentation**
  - Conceptual data model
  - Logical data model (star/snowflake schema)
  - Physical data model dengan indexing strategy
  
- **ETL Documentation**
  - Data source mapping
  - Transformation business rules
  - Data quality validation rules
  - ETL process documentation
  
- **Working Data Warehouse**
  - Populated data warehouse dengan sample data
  - OLAP cubes untuk different business areas
  - Data quality reports

#### 3. **Interactive Business Dashboard** (30%)
**Format:** Working BI dashboard dengan user documentation

**Dashboard Components:**
- **Executive Dashboard**
  - Key performance indicators (KPIs)
  - Business health scorecard
  - Trend analysis visualizations
  
- **Sales Analytics Dashboard**
  - Sales performance tracking
  - Product performance analysis
  - Customer analytics
  
- **Operations Dashboard**
  - Production metrics
  - Inventory management
  - Quality control indicators
  
- **Financial Dashboard**
  - Profitability analysis
  - Cost analysis
  - Financial forecasting

#### 4. **Advanced Analytics & Insights Report** (25%)
**Format:** Analytical report dengan actionable insights

**Konten:**
- **Predictive Analytics**
  - Sales forecasting models
  - Customer churn prediction
  - Demand forecasting
  
- **Data Mining Results**
  - Customer segmentation analysis
  - Market basket analysis
  - Pattern discovery dalam sales data
  
- **Business Insights & Recommendations**
  - Key findings dari data analysis
  - Strategic recommendations
  - Action plans untuk business improvement

---

### KRITERIA PENILAIAN

#### A. **Technical Implementation** (40%)
1. **Data warehouse design quality** (15%)
2. **ETL process effectiveness** (10%)
3. **Dashboard functionality dan user experience** (15%)

#### B. **Business Value & Analytics** (35%)
1. **Business requirements alignment** (10%)
2. **Quality of insights dan recommendations** (15%)
3. **Predictive modeling accuracy** (10%)

#### C. **Project Leadership & Management** (15%)
1. **Team coordination dan leadership** (8%)
2. **Project timeline management** (7%)

#### D. **Presentation & Communication** (10%)
1. **Final presentation quality** (5%)
2. **Documentation completeness** (5%)

---

### TIMELINE PENGERJAAN

| Minggu | Phase | Aktivitas Utama | Key Deliverables |
|--------|-------|----------------|------------------|
| 1 | Planning | Business requirements gathering, team formation | BI strategy document |
| 2 | Analysis | Data source analysis, data profiling | Data assessment report |
| 3 | Design | Data warehouse design, dashboard wireframes | Design specifications |
| 4 | ETL Development | ETL process development, data integration | Working ETL processes |
| 5 | DW Implementation | Data warehouse implementation, testing | Populated data warehouse |
| 6 | Dashboard Development | Dashboard creation, visualization design | Interactive dashboards |
| 7 | Advanced Analytics | Predictive modeling, data mining | Analytics models |
| 8 | Testing & Validation | User testing, performance optimization | Test results, final system |
| 9 | Presentation | Final presentation preparation, documentation | Final deliverables |

---

### TECHNICAL SPECIFICATIONS

#### **Data Sources (Simulated untuk SATRIAMART):**
- **Sales Data:** Order transactions, customer information, product details
- **Inventory Data:** Stock levels, supplier information, procurement records
- **Production Data:** Work orders, resource utilization, quality metrics
- **Financial Data:** Revenue, costs, profitability metrics

#### **Technology Stack Options:**

**Option 1: Microsoft Stack**
- Data Warehouse: SQL Server
- ETL: SQL Server Integration Services (SSIS)
- Analytics: Power BI
- Advanced Analytics: Python/R integration

**Option 2: Open Source Stack**
- Data Warehouse: PostgreSQL
- ETL: Pentaho Data Integration
- Analytics: Tableau Public atau Apache Superset
- Advanced Analytics: Python dengan Jupyter Notebooks

**Option 3: Cloud-based Stack**
- Data Warehouse: Amazon Redshift atau Google BigQuery
- ETL: AWS Glue atau Google Dataflow
- Analytics: Tableau Online atau Google Data Studio
- Advanced Analytics: Python dalam cloud environment

---

### SAMPLE DATA GENERATION

Untuk keperluan project, mahasiswa akan membuat synthetic data yang realistic untuk SATRIAMART:

**Data Volume Guidelines:**
- **Customer Records:** 1,000+ customers
- **Product Catalog:** 50+ products across categories
- **Sales Transactions:** 5,000+ transactions (2 years history)
- **Inventory Records:** Monthly stock movements
- **Production Records:** Work order dan resource utilization

**Data Quality Requirements:**
- Realistic business relationships
- Seasonal patterns dalam sales data
- Data quality issues untuk ETL challenge
- Missing values untuk data cleaning practice

---

### SUMBER REFERENSI

1. P.Antonius, S.M.Gede, dkk. *BUSINESS INTELEGENT* (Pengantar Business Intelligence dalam Bisnis). Jambi: PT. Sonpedia Publishing Indonesia. 2023

2. RH. Valentinus. *Buku Ajar Kecerdasan Bisnis*. Surabaya: Institut Bisnis Dan Informatika Stikom.2017

3. Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling*. 3rd Edition. Wiley.

4. Turban, E., Sharda, R., & Delen, D. (2018). *Business Intelligence, Analytics, and Data Science: A Managerial Perspective*. 4th Edition. Pearson.

5. Vercellis, C. (2009). *Business Intelligence: Data Mining and Optimization for Decision Making*. Wiley.

---

### BENTUK DAN FORMAT LUARAN

#### **Format Laporan:**
1. **Systematic Report Structure** dengan academic writing standards
2. **Professional PowerPoint Presentation** untuk final demo
3. **Working BI System** yang dapat diakses dan didemonstrasikan

#### **Submission Format:**
- **Digital Portfolio:** Complete project documentation
- **Live Demo:** Working system demonstration
- **Source Code Repository:** All development artifacts
- **Video Demo:** 10-minute system walkthrough

---

### INDIKATOR KRITERIA DAN BOBOT PENILAIAN

#### **Ketepatan Waktu Pengumpulan Laporan (20%)**
Mahasiswa mengumpulkan laporan sesuai dengan waktu yang telah ditentukan

#### **Laporan Penelitian (30%)**
1. **Ketepatan sistematika penyusunan laporan** sesuai standar panduan (10%)
2. **Ketepatan dalam penyusunan laporan** yang disesuaikan dengan hasil rancang dashboard yang dibuat (10%)
3. **Laporan dalam ejaan Bahasa Indonesia** yang benar dan sesuai dengan standar (5%)
4. **Konsistensi dalam penggunaan istilah, warna, symbol, dan lambang** (5%)

#### **Penyusunan Slide Presentasi (20%)**
Jelas dan konsisten sederhana dan inovatif, menampilkan gambar dan blok sistem tulisan menggunakan font yang mudah dibaca, jika diperlukan didukung dengan gambar yang relevan.

#### **Presentasi (30%)**
Bahasa komunikatif, penguasaan materi, penguasaan audiensi, pengendalian waktu (15 menit presentasi +5 menit diskusi), kejelasan dan ketajaman paparan, penguasaan media presentasi.

---

### ASSESSMENT RUBRIC DETAIL

| Aspek | Excellent (A) | Good (B) | Satisfactory (C) | Needs Improvement (D) |
|-------|---------------|----------|------------------|----------------------|
| **Technical Mastery** | Advanced BI implementation, innovative solutions | Good technical skills, solid implementation | Basic technical competency | Limited technical understanding |
| **Business Acumen** | Deep business insights, strategic recommendations | Good business understanding | Basic business knowledge | Poor business relevance |
| **Leadership & Teamwork** | Exemplary leadership, excellent collaboration | Good leadership skills | Adequate team coordination | Poor team management |
| **Innovation & Creativity** | Highly innovative approach, creative solutions | Some innovative elements | Standard approach | Lack of innovation |

---

### FINAL PRESENTATION GUIDELINES

**Presentation Schedule:** Dikumpulkan pada pertemuan 11 sd 15

**Presentation Format:**
- **Duration:** 15 menit presentasi + 5 menit Q&A
- **Audience:** Academic panel + Industry expert dari manufacturing/retail
- **Live Demo:** Working BI system demonstration
- **Q&A Focus:** Technical implementation, business value, future enhancements

**Evaluation Panel:**
- Academic supervisor (50%)
- Industry expert (30%)
- Peer evaluation (20%)

---

*Rancangan tugas Business Intelligence ini dirancang untuk memberikan comprehensive experience dalam BI development lifecycle, mengintegrasikan technical skills dengan business acumen, dan mengembangkan leadership capabilities sesuai dengan CPMK mata kuliah.*
