# ANALISIS DAN DESAIN SISTEM - PART 1
## SATRIAMART Integrated Management System (SIMS)
### Pertemuan 4: Analisa Kebutuhan Sistem, Use Case, Activity Diagram, ERD, User Interface

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi II**  
**Pertemuan 4 - Studi Kasus Analisis dan Desain Sistem**

---

## DAFTAR ISI

1. [Analisa Kebutuhan Sistem](#1-analisa-kebutuhan-sistem)
   - 1.1 Identifikasi Kebutuhan Fungsional
   - 1.2 Identifikasi Kebutuhan Non-Fungsional
   - 1.3 Spesifikasi Kebutuhan Pengguna
2. [Use Case Diagram](#2-use-case-diagram)
   - 2.1 Identifikasi Aktor
   - 2.2 Use Case Modul CRM
   - 2.3 Use Case Modul Inventory
   - 2.4 Use Case Modul Production
3. [Activity Diagram](#3-activity-diagram)
4. [Entity Relationship Diagram (ERD)](#4-entity-relationship-diagram)
5. [User Interface Design](#5-user-interface-design)

---

## 1. ANALISA KEBUTUHAN SISTEM

### 1.1 Identifikasi Kebutuhan Fungsional

Berdasarkan kondisi bisnis SATRIAMART yang bergerak di bidang dekorasi dan aksesoris akrilik, sistem informasi terintegrasi SIMS harus memiliki kemampuan fungsional sebagai berikut:

#### A. Kebutuhan Fungsional Modul CRM (Customer Relationship Management)

**FR-CRM-001: Manajemen Data Pelanggan**
- **Deskripsi:** Sistem harus mampu menyimpan dan mengelola informasi lengkap pelanggan
- **Kebutuhan Detail:**
  - Registrasi pelanggan baru dengan form lengkap (nama, kontak, alamat, kategori)
  - Edit dan update informasi pelanggan yang sudah terdaftar
  - Pencarian pelanggan berdasarkan nama, email, nomor telepon
  - Kategorisasi pelanggan (individu, perusahaan, reseller)
  - Tracking status pelanggan (aktif, tidak aktif, potensial)
  - History transaksi pelanggan secara lengkap
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Meningkatkan efektivitas manajemen hubungan pelanggan

**FR-CRM-002: Manajemen Pesanan Pelanggan**
- **Deskripsi:** Sistem harus dapat mengelola pesanan dari pelanggan
- **Kebutuhan Detail:**
  - Input pesanan baru dengan detail produk yang dipesan
  - Tracking status pesanan (pending, processed, production, shipped, completed)
  - Update status pesanan secara real-time
  - Kalkulasi otomatis total harga berdasarkan produk dan jumlah
  - Generate nomor pesanan unik secara otomatis
  - Notifikasi perubahan status pesanan ke pelanggan
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Meningkatkan kecepatan proses order dan kepuasan pelanggan

**FR-CRM-003: Manajemen Komunikasi Pelanggan**
- **Deskripsi:** Sistem harus mencatat semua komunikasi dengan pelanggan
- **Kebutuhan Detail:**
  - Logging komunikasi (email, telepon, WhatsApp, tatap muka)
  - Tracking follow-up pelanggan dengan reminder otomatis
  - Template response untuk komunikasi standar
  - History lengkap komunikasi per pelanggan
  - Notifikasi untuk follow-up yang pending
- **Prioritas:** Sedang (Important)
- **Business Value:** Meningkatkan kualitas layanan pelanggan

**FR-CRM-004: Analisis Perilaku Pelanggan**
- **Deskripsi:** Sistem harus dapat menganalisis perilaku dan preferensi pelanggan
- **Kebutuhan Detail:**
  - Identifikasi pelanggan paling aktif (top customers)
  - Analisis produk yang paling sering dipesan per pelanggan
  - Segmentasi pelanggan berdasarkan value dan frekuensi
  - Prediksi repeat order berdasarkan pola historis
  - Customer lifetime value calculation
- **Prioritas:** Sedang (Important)
- **Business Value:** Mendukung strategi marketing yang lebih efektif

**FR-CRM-005: Manajemen Komplain dan Feedback**
- **Deskripsi:** Sistem harus mengelola komplain dan feedback pelanggan
- **Kebutuhan Detail:**
  - Input komplain dengan kategori dan prioritas
  - Assignment komplain ke staff yang tepat
  - Tracking resolusi komplain dengan SLA monitoring
  - Rating kepuasan pelanggan setelah resolusi
  - Dashboard komplain untuk monitoring manajemen
- **Prioritas:** Sedang (Important)
- **Business Value:** Meningkatkan kepuasan dan retensi pelanggan

#### B. Kebutuhan Fungsional Modul Inventory Management

**FR-INV-001: Manajemen Master Data Produk**
- **Deskripsi:** Sistem harus dapat mengelola master data produk akrilik
- **Kebutuhan Detail:**
  - Input produk baru dengan spesifikasi lengkap (kode, nama, kategori, ukuran, warna)
  - Upload foto produk dengan multiple images
  - Manajemen variasi produk (size, color variants)
  - Set harga jual dan harga modal per produk
  - Kategorisasi produk (nomor rumah, signage, papan nama, aksesoris custom)
  - Status produk (aktif, tidak aktif, pre-order)
  - Informasi dimensi dan berat untuk keperluan shipping
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Standarisasi katalog produk untuk operasional

**FR-INV-002: Tracking Stok Real-Time**
- **Deskripsi:** Sistem harus melacak level stok secara real-time
- **Kebutuhan Detail:**
  - Update stok otomatis saat ada transaksi (in/out)
  - Dashboard stok per produk dan per kategori
  - Alert otomatis untuk stok menipis (low stock alert)
  - Multi-location inventory tracking jika ada cabang
  - History pergerakan stok (stock movement history)
  - Stock opname dan adjustment
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Akurasi inventory 95% untuk menghindari stockout

**FR-INV-003: Manajemen Material dan Bahan Baku**
- **Deskripsi:** Sistem harus mengelola bahan baku akrilik dan material pendukung
- **Kebutuhan Detail:**
  - Master data material (acrylic sheets, adhesive, cutting tools, packaging)
  - Tracking stok material dengan unit of measure (UoM)
  - Minimum stock level dengan automatic reorder point
  - Konversi material ke finished goods (bill of materials)
  - Material usage tracking untuk cost calculation
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Optimasi penggunaan material dan cost control

**FR-INV-004: Manajemen Supplier**
- **Deskripsi:** Sistem harus mengelola data supplier dan purchase order
- **Kebutuhan Detail:**
  - Master data supplier dengan rating dan performance
  - Purchase order (PO) creation dengan approval workflow
  - Goods receipt dan quality check
  - Tracking lead time supplier
  - Supplier performance monitoring (on-time delivery, quality)
  - Payment terms management per supplier
- **Prioritas:** Sedang (Important)
- **Business Value:** Efisiensi procurement process

**FR-INV-005: Sistem Reorder Otomatis**
- **Deskripsi:** Sistem harus memiliki mekanisme reorder otomatis
- **Kebutuhan Detail:**
  - Set reorder point dan reorder quantity per produk
  - Auto-generate purchase requisition saat stok mencapai reorder point
  - Rekomendasi quantity berdasarkan demand forecast
  - Consideration untuk lead time supplier
  - Approval workflow untuk PR (Purchase Requisition)
- **Prioritas:** Sedang (Important)
- **Business Value:** Mengurangi stockout dan excess inventory

**FR-INV-006: Stock Opname dan Adjustment**
- **Deskripsi:** Sistem harus mendukung proses stock opname periodik
- **Kebutuhan Detail:**
  - Create stock opname schedule
  - Mobile-friendly interface untuk counting
  - Compare physical count vs system count
  - Generate variance report
  - Stock adjustment dengan approval dan reasoning
  - Audit trail untuk setiap adjustment
- **Prioritas:** Sedang (Important)
- **Business Value:** Menjaga akurasi data inventory

#### C. Kebutuhan Fungsional Modul Production Planning

**FR-PROD-001: Manajemen Work Order**
- **Deskripsi:** Sistem harus dapat membuat dan mengelola work order produksi
- **Kebutuhan Detail:**
  - Generate work order dari customer order
  - Work order detail (produk, quantity, spesifikasi khusus, deadline)
  - Assignment work order ke production team
  - Status tracking (scheduled, in progress, quality check, completed)
  - Batch production untuk order yang sama
  - Priority level untuk urgent orders
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Meningkatkan efisiensi produksi 35%

**FR-PROD-002: Production Scheduling**
- **Deskripsi:** Sistem harus memiliki kemampuan penjadwalan produksi
- **Kebutuhan Detail:**
  - Calendar view untuk production schedule
  - Resource availability checking (mesin cutting, staff)
  - Automatic scheduling berdasarkan due date dan kapasitas
  - Drag-and-drop untuk reschedule
  - Conflict detection untuk overlapping schedule
  - Gantt chart untuk visualisasi timeline
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Optimasi kapasitas produksi dan on-time delivery

**FR-PROD-003: Resource Management**
- **Deskripsi:** Sistem harus mengelola resource produksi (mesin, tools, staff)
- **Kebutuhan Detail:**
  - Master data mesin dan equipment
  - Maintenance schedule untuk preventive maintenance
  - Staff skill matrix dan availability
  - Resource allocation untuk setiap work order
  - Utilization tracking per resource
  - Downtime recording dan analysis
- **Prioritas:** Sedang (Important)
- **Business Value:** Maksimalkan utilisasi resource produksi

**FR-PROD-004: Quality Control Management**
- **Deskripsi:** Sistem harus mendukung proses quality control
- **Kebutuhan Detail:**
  - QC checklist template per produk
  - QC inspection recording (pass/fail/rework)
  - Defect categorization dan root cause analysis
  - QC approval untuk release ke finished goods
  - Quality metrics dashboard (defect rate, rework rate)
  - Photo upload untuk defect documentation
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Meningkatkan kualitas produk dan mengurangi rework

**FR-PROD-005: Production Monitoring**
- **Deskripsi:** Sistem harus menyediakan monitoring produksi real-time
- **Kebutuhan Detail:**
  - Production dashboard dengan KPI real-time
  - Work order progress tracking
  - Production output vs target
  - OEE (Overall Equipment Effectiveness) calculation
  - Bottleneck identification
  - Alert untuk production delay
- **Prioritas:** Sedang (Important)
- **Business Value:** Visibilitas penuh terhadap production performance

**FR-PROD-006: Bill of Materials (BOM)**
- **Deskripsi:** Sistem harus mengelola BOM untuk setiap produk
- **Kebutuhan Detail:**
  - BOM definition dengan material dan quantity required
  - Multi-level BOM untuk produk kompleks
  - BOM versioning untuk product changes
  - Material requirement calculation berdasarkan production plan
  - Cost roll-up dari material cost ke product cost
  - What-if analysis untuk BOM changes
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Akurasi material planning dan cost calculation

#### D. Kebutuhan Fungsional Modul Sales Analytics & Reporting

**FR-ANAL-001: Dashboard Eksekutif**
- **Deskripsi:** Sistem harus menyediakan executive dashboard dengan KPI utama
- **Kebutuhan Detail:**
  - Total penjualan (daily, monthly, yearly)
  - Jumlah customer baru vs repeat customer
  - Top selling products
  - Inventory turnover ratio
  - Production output dan efficiency
  - Outstanding orders dan backlog
  - Interactive charts dan graphs
  - Drill-down capability ke detail data
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Decision making berbasis data real-time

**FR-ANAL-002: Sales Performance Analysis**
- **Deskripsi:** Sistem harus menganalisis performa penjualan
- **Kebutuhan Detail:**
  - Sales trend analysis (daily, weekly, monthly)
  - Year-over-year comparison
  - Sales by product category
  - Sales by customer segment
  - Seasonal pattern identification
  - Sales forecasting berdasarkan historical data
  - Sales conversion funnel analysis
- **Prioritas:** Sedang (Important)
- **Business Value:** Insight untuk strategi penjualan

**FR-ANAL-003: Inventory Analytics**
- **Deskripsi:** Sistem harus menyediakan analitik inventory
- **Kebutuhan Detail:**
  - Slow-moving dan fast-moving item analysis
  - Stock aging report
  - ABC analysis untuk inventory classification
  - Inventory turnover by category
  - Stockout frequency analysis
  - Carrying cost calculation
  - Optimal order quantity recommendation
- **Prioritas:** Sedang (Important)
- **Business Value:** Optimasi inventory investment

**FR-ANAL-004: Production Performance Analytics**
- **Deskripsi:** Sistem harus menganalisis performa produksi
- **Kebutuhan Detail:**
  - Production output trend
  - On-time delivery rate
  - Capacity utilization
  - Quality metrics (defect rate, rework rate)
  - Production efficiency by product type
  - Downtime analysis
  - Cost per unit analysis
- **Prioritas:** Sedang (Important)
- **Business Value:** Continuous improvement production process

**FR-ANAL-005: Customer Analytics**
- **Deskripsi:** Sistem harus menganalisis data pelanggan
- **Kebutuhan Detail:**
  - Customer lifetime value (CLV)
  - Customer retention rate
  - Customer churn analysis
  - RFM analysis (Recency, Frequency, Monetary)
  - Customer satisfaction score trending
  - Customer acquisition cost
  - Repeat purchase rate
- **Prioritas:** Sedang (Important)
- **Business Value:** Customer relationship strategy

**FR-ANAL-006: Custom Report Generator**
- **Deskripsi:** Sistem harus memiliki report generator yang fleksibel
- **Kebutuhan Detail:**
  - Drag-and-drop report builder
  - Multiple data source integration
  - Custom filter dan grouping
  - Export ke multiple format (Excel, PDF, CSV)
  - Scheduled report dengan email delivery
  - Report template library
  - Ad-hoc query capability
- **Prioritas:** Rendah (Nice to Have)
- **Business Value:** Fleksibilitas dalam reporting

#### E. Kebutuhan Fungsional Modul System Administration

**FR-ADMIN-001: User Management**
- **Deskripsi:** Sistem harus mengelola user dan access control
- **Kebutuhan Detail:**
  - Create, edit, delete user accounts
  - Role-based access control (RBAC)
  - Password policy enforcement
  - Multi-factor authentication (MFA)
  - User activity logging
  - Password reset workflow
  - Session management dan timeout
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Security dan audit trail

**FR-ADMIN-002: Configuration Management**
- **Deskripsi:** Sistem harus memiliki setting dan konfigurasi global
- **Kebutuhan Detail:**
  - Company profile dan branding
  - Tax rate configuration
  - Currency dan localization settings
  - Email template customization
  - Notification preferences
  - Workflow approval configuration
  - Integration settings (API keys, webhooks)
- **Prioritas:** Sedang (Important)
- **Business Value:** Fleksibilitas sistem sesuai kebutuhan bisnis

**FR-ADMIN-003: Audit Trail**
- **Deskripsi:** Sistem harus mencatat semua aktivitas penting
- **Kebutuhan Detail:**
  - Logging untuk semua create, update, delete operations
  - User activity history
  - Login/logout tracking
  - Data change tracking (before/after values)
  - Export audit log untuk compliance
  - Retention policy untuk audit data
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Compliance dan security

**FR-ADMIN-004: Backup dan Recovery**
- **Deskripsi:** Sistem harus memiliki mekanisme backup
- **Kebutuhan Detail:**
  - Scheduled automatic backup (daily, weekly)
  - On-demand manual backup
  - Backup verification
  - Point-in-time recovery
  - Backup retention policy
  - Disaster recovery procedure documentation
- **Prioritas:** Tinggi (Critical)
- **Business Value:** Business continuity

---

### 1.2 Identifikasi Kebutuhan Non-Fungsional

#### A. Performance Requirements

**NFR-PERF-001: Response Time**
- **Deskripsi:** Waktu respons sistem harus optimal
- **Spesifikasi:**
  - Page load time: < 3 detik untuk 90% requests
  - API response time: < 1 detik untuk operasi CRUD standar
  - Search query: < 2 detik untuk hasil maksimal 1000 records
  - Report generation: < 5 detik untuk report standar
  - Dashboard refresh: < 2 detik
- **Measurement:** Apache JMeter load testing
- **Prioritas:** Tinggi

**NFR-PERF-002: Throughput**
- **Deskripsi:** Sistem harus menangani concurrent users
- **Spesifikasi:**
  - Minimum 100 concurrent users
  - Peak load handling: 150 concurrent users
  - Transaction per second (TPS): 50 TPS
  - Database connection pooling: 50 connections
- **Measurement:** Load testing dengan realistic user scenarios
- **Prioritas:** Tinggi

**NFR-PERF-003: Scalability**
- **Deskripsi:** Sistem harus scalable untuk pertumbuhan bisnis
- **Spesifikasi:**
  - Horizontal scaling capability untuk application server
  - Database sharding readiness untuk data growth
  - Cache layer (Redis) untuk performance optimization
  - CDN integration untuk static assets
  - Support untuk 200% business growth tanpa re-architecture
- **Measurement:** Architecture review dan capacity planning
- **Prioritas:** Sedang

#### B. Security Requirements

**NFR-SEC-001: Authentication**
- **Deskripsi:** Mekanisme autentikasi yang kuat
- **Spesifikasi:**
  - Username dan password dengan minimum complexity
  - Multi-factor authentication (MFA) untuk admin
  - Password encryption dengan bcrypt (minimum 10 rounds)
  - Session timeout: 30 menit inactivity
  - Maximum login attempts: 5 (dengan lockout mechanism)
  - Password history: tidak boleh sama dengan 3 password terakhir
- **Compliance:** OWASP Authentication Guidelines
- **Prioritas:** Tinggi

**NFR-SEC-002: Authorization**
- **Deskripsi:** Kontrol akses berbasis role
- **Spesifikasi:**
  - Role-based access control (RBAC) implementation
  - Principle of least privilege
  - Granular permission per module dan function
  - Row-level security untuk data sensitivity
  - API authorization dengan JWT tokens
- **Compliance:** OWASP Authorization Guidelines
- **Prioritas:** Tinggi

**NFR-SEC-003: Data Encryption**
- **Deskripsi:** Enkripsi data sensitif
- **Spesifikasi:**
  - Data at rest: AES-256 encryption untuk sensitive data
  - Data in transit: TLS 1.3 untuk semua communications
  - Database encryption untuk personal information
  - Secure key management dengan rotation policy
- **Compliance:** GDPR data protection standards
- **Prioritas:** Tinggi

**NFR-SEC-004: Security Audit**
- **Deskripsi:** Audit dan monitoring security
- **Spesifikasi:**
  - Comprehensive audit trail
  - Security event logging
  - Failed login attempt monitoring
  - Unauthorized access attempt detection
  - Regular security assessment (quarterly)
  - Vulnerability scanning (monthly)
- **Compliance:** ISO 27001 guidelines
- **Prioritas:** Tinggi

**NFR-SEC-005: Data Privacy**
- **Deskripsi:** Perlindungan data pribadi pelanggan
- **Spesifikasi:**
  - Personal data minimization
  - Consent management untuk data collection
  - Right to erasure (data deletion capability)
  - Data masking untuk non-production environments
  - Privacy policy dan terms of service
- **Compliance:** UU PDP (Undang-Undang Perlindungan Data Pribadi)
- **Prioritas:** Tinggi

#### C. Usability Requirements

**NFR-USA-001: User Interface**
- **Deskripsi:** Interface yang intuitif dan mudah digunakan
- **Spesifikasi:**
  - Consistent UI/UX across all modules
  - Maximum 3 clicks untuk common tasks
  - Clear navigation dengan breadcrumb
  - Tooltips dan inline help
  - Responsive design untuk desktop dan tablet
  - Loading indicators untuk long operations
- **Measurement:** User acceptance testing dengan min. 80% satisfaction
- **Prioritas:** Tinggi

**NFR-USA-002: Accessibility**
- **Deskripsi:** Aksesibilitas untuk semua user
- **Spesifikasi:**
  - WCAG 2.1 Level AA compliance
  - Keyboard navigation support
  - Screen reader compatibility
  - Color contrast ratio minimum 4.5:1
  - Text resizing capability
  - Alt text untuk images
- **Compliance:** Web Content Accessibility Guidelines (WCAG)
- **Prioritas:** Sedang

**NFR-USA-003: Learning Curve**
- **Deskripsi:** Sistem mudah dipelajari
- **Spesifikasi:**
  - Maximum 2 hari training untuk basic user
  - Maximum 5 hari training untuk power user
  - Interactive tutorial untuk first-time users
  - Context-sensitive help system
  - Video tutorial library
  - User manual dalam Bahasa Indonesia
- **Measurement:** Training completion rate dan feedback
- **Prioritas:** Sedang

#### D. Reliability Requirements

**NFR-REL-001: Availability**
- **Deskripsi:** Sistem harus tersedia setiap saat
- **Spesifikasi:**
  - Uptime: 99.5% (maksimal 3.6 jam downtime per bulan)
  - Planned maintenance window: maksimal 4 jam per bulan
  - Notification 48 jam sebelum planned maintenance
  - Redundant server untuk high availability
  - Automatic failover mechanism
- **Measurement:** Uptime monitoring dengan Pingdom/UptimeRobot
- **Prioritas:** Tinggi

**NFR-REL-002: Error Handling**
- **Deskripsi:** Penanganan error yang graceful
- **Spesifikasi:**
  - User-friendly error messages (bukan technical error)
  - Error logging untuk debugging
  - Automatic retry untuk transient errors
  - Graceful degradation untuk partial system failure
  - Error notification ke admin untuk critical errors
- **Measurement:** Error rate monitoring
- **Prioritas:** Tinggi

**NFR-REL-003: Data Integrity**
- **Deskripsi:** Integritas data harus terjaga
- **Spesifikasi:**
  - ACID compliance untuk database transactions
  - Data validation pada application dan database level
  - Referential integrity dengan foreign key constraints
  - Checksum verification untuk data transfer
  - Regular data integrity checks
- **Measurement:** Data quality audits
- **Prioritas:** Tinggi

**NFR-REL-004: Backup dan Recovery**
- **Deskripsi:** Kemampuan recovery dari disaster
- **Spesifikasi:**
  - RTO (Recovery Time Objective): 4 jam
  - RPO (Recovery Point Objective): 24 jam
  - Daily automated backup
  - Offsite backup storage
  - Monthly backup restore testing
  - Documented disaster recovery procedures
- **Measurement:** Backup success rate dan restore testing
- **Prioritas:** Tinggi

#### E. Maintainability Requirements

**NFR-MAIN-001: Code Quality**
- **Deskripsi:** Kualitas kode yang tinggi
- **Spesifikasi:**
  - Code coverage minimum 80% untuk unit tests
  - Static code analysis dengan SonarQube
  - Code review untuk semua changes
  - Coding standards dan style guide
  - Technical debt monitoring
  - Code documentation dengan inline comments
- **Measurement:** Automated code quality metrics
- **Prioritas:** Sedang

**NFR-MAIN-002: Modularity**
- **Deskripsi:** Arsitektur modular untuk maintainability
- **Spesifikasi:**
  - Loose coupling antar modules
  - High cohesion dalam module
  - Clear separation of concerns
  - Reusable components dan libraries
  - API-first design untuk integration
- **Measurement:** Architecture review
- **Prioritas:** Sedang

**NFR-MAIN-003: Documentation**
- **Deskripsi:** Dokumentasi lengkap
- **Spesifikasi:**
  - Technical documentation (architecture, API, database schema)
  - User documentation (user manual, training materials)
  - Operations documentation (deployment, configuration)
  - Change log dan release notes
  - Up-to-date documentation dengan code changes
- **Measurement:** Documentation completeness review
- **Prioritas:** Sedang

#### F. Compatibility Requirements

**NFR-COMP-001: Browser Compatibility**
- **Deskripsi:** Dukungan untuk berbagai browser
- **Spesifikasi:**
  - Google Chrome (latest 2 versions)
  - Mozilla Firefox (latest 2 versions)
  - Microsoft Edge (latest 2 versions)
  - Safari (latest 2 versions untuk macOS)
  - Responsive design untuk tablet (minimum iPad)
- **Measurement:** Cross-browser testing
- **Prioritas:** Tinggi

**NFR-COMP-002: Database Compatibility**
- **Deskripsi:** Kompatibilitas database
- **Spesifikasi:**
  - MySQL 8.0+ (primary)
  - MariaDB 10.5+ (alternative)
  - Database migration scripts untuk version upgrades
- **Measurement:** Database compatibility testing
- **Prioritas:** Sedang

**NFR-COMP-003: Integration Compatibility**
- **Deskripsi:** Kemampuan integrasi dengan sistem lain
- **Spesifikasi:**
  - RESTful API dengan OpenAPI specification
  - JSON sebagai data interchange format
  - Webhook support untuk event notification
  - OAuth 2.0 untuk third-party integration
  - API versioning untuk backward compatibility
- **Measurement:** API integration testing
- **Prioritas:** Sedang

---

### 1.3 Spesifikasi Kebutuhan Pengguna

#### A. Identifikasi Stakeholder dan Pengguna

**Stakeholder Internal SATRIAMART:**

1. **Pemilik/Owner (Executive Level)**
   - **Peran:** Pengambil keputusan strategis bisnis
   - **Kebutuhan:**
     - Executive dashboard dengan business KPIs
     - Sales performance overview
     - Financial summary dan profitability
     - Strategic analytics untuk business planning
   - **Frekuensi Penggunaan:** Daily untuk dashboard, weekly untuk detailed reports
   - **Technical Proficiency:** Basic (minimal technical knowledge)

2. **Manajer Operasional (Management Level)**
   - **Peran:** Mengelola operasional harian SATRIAMART
   - **Kebutuhan:**
     - Operational dashboard (inventory, production, orders)
     - Performance monitoring tools
     - Resource allocation dan scheduling
     - Problem identification dan resolution
   - **Frekuensi Penggunaan:** Daily, multiple times
   - **Technical Proficiency:** Intermediate

3. **Staff Sales/Customer Service**
   - **Peran:** Menangani customer interaction dan order processing
   - **Kebutuhan:**
     - Customer data management (CRUD operations)
     - Order entry dan tracking
     - Communication logging dengan customers
     - Quick access ke product catalog
     - Customer complaint handling
   - **Frekuensi Penggunaan:** Daily, extensive usage
   - **Technical Proficiency:** Basic to Intermediate
   - **Jumlah User:** 3-5 orang

4. **Staff Inventory/Warehouse**
   - **Peran:** Mengelola inventory dan material
   - **Kebutuhan:**
     - Real-time stock monitoring
     - Stock in/out recording
     - Stock opname functionality
     - Material request dan purchase order
     - Supplier management
   - **Frekuensi Penggunaan:** Daily, extensive usage
   - **Technical Proficiency:** Basic
   - **Jumlah User:** 2-3 orang

5. **Production Team/Supervisor**
   - **Peran:** Menjalankan dan supervisi produksi
   - **Kebutuhan:**
     - Work order list dan details
     - Production schedule visibility
     - Material consumption recording
     - Quality control check-in
     - Production progress update
   - **Frekuensi Penggunaan:** Daily, throughout working hours
   - **Technical Proficiency:** Basic
   - **Jumlah User:** 5-8 orang

6. **Admin/IT Support**
   - **Peran:** System administration dan user support
   - **Kebutuhan:**
     - User management
     - System configuration
     - Backup dan maintenance
     - Audit trail access
     - Technical troubleshooting
   - **Frekuensi Penggunaan:** Daily untuk monitoring, as-needed untuk configuration
   - **Technical Proficiency:** Advanced
   - **Jumlah User:** 1-2 orang

**Stakeholder Eksternal:**

7. **Customer SATRIAMART**
   - **Peran:** Pembeli produk dekorasi akrilik
   - **Kebutuhan:**
     - Self-service order tracking (optional, future enhancement)
     - Order confirmation notification
     - Delivery status notification
   - **Frekuensi Penggunaan:** Occasional (per order)
   - **Technical Proficiency:** Basic
   - **Jumlah User:** Tidak terbatas

8. **Supplier**
   - **Peran:** Pemasok material akrilik dan supplies
   - **Kebutuhan:**
     - Purchase order notification (email/WhatsApp)
     - Delivery schedule information
   - **Frekuensi Penggunaan:** Per transaction
   - **Technical Proficiency:** Basic
   - **Jumlah User:** 5-10 suppliers

#### B. User Stories per Role

**User Stories - Owner/Executive:**

```
US-EXEC-001: Melihat Dashboard Eksekutif
As an Owner,
I want to see an executive dashboard dengan key business metrics,
So that saya dapat monitor kesehatan bisnis secara cepat.

Acceptance Criteria:
- Dashboard menampilkan total sales (daily, monthly, yearly)
- Menampilkan jumlah order dan status (completed, in-progress, pending)
- Menampilkan top 5 produk terlaris
- Menampilkan inventory value
- Menampilkan customer growth chart
- Data di-refresh otomatis setiap 5 menit
- Export dashboard to PDF untuk presentation

US-EXEC-002: Analisis Sales Performance
As an Owner,
I want to analyze sales trends dan patterns,
So that saya dapat membuat keputusan strategis untuk growth.

Acceptance Criteria:
- Dapat filter sales data berdasarkan periode (daily, weekly, monthly, yearly)
- Dapat compare sales antar periode (month-over-month, year-over-year)
- Dapat lihat sales breakdown by product category
- Dapat lihat sales breakdown by customer segment
- Dapat export report ke Excel untuk further analysis

US-EXEC-003: Monitor Profitability
As an Owner,
I want to see profitability per product dan per customer,
So that saya dapat fokus pada produk dan customer yang paling profitable.

Acceptance Criteria:
- Dashboard menampilkan profit margin per product category
- Menampilkan top profitable customers
- Menampilkan cost breakdown (material, labor, overhead)
- Trend profitability over time
```

**User Stories - Sales/Customer Service Staff:**

```
US-SALES-001: Registrasi Customer Baru
As a Sales Staff,
I want to register new customer dengan informasi lengkap,
So that data customer tersimpan di sistem untuk future reference.

Acceptance Criteria:
- Form input dengan field: nama, email, phone, alamat, tipe customer
- Validasi untuk email format dan phone number
- Auto-generate customer code unik
- Simpan data ke database dengan sukses
- Notifikasi sukses setelah save
- Redirect ke customer detail page setelah registrasi

US-SALES-002: Membuat Order Baru
As a Sales Staff,
I want to create order untuk customer,
So that order dapat diproses oleh production team.

Acceptance Criteria:
- Search customer existing atau create new customer inline
- Select produk dari catalog dengan search dan filter
- Input quantity dan custom specification (jika ada)
- Sistem calculate total price otomatis
- Input estimated delivery date
- Generate order number otomatis
- Print order confirmation untuk customer

US-SALES-003: Tracking Status Order
As a Sales Staff,
I want to check status order customer,
So that saya dapat inform customer tentang progress ordernya.

Acceptance Criteria:
- Search order by order number, customer name, atau phone
- View order details dan timeline
- Lihat current status (pending, in-production, quality-check, ready, shipped)
- View estimated completion date
- View production progress percentage
- Send status update notification ke customer via WhatsApp/Email
```

**User Stories - Inventory Staff:**

```
US-INV-001: Input Stock Masuk
As an Inventory Staff,
I want to record material yang masuk dari supplier,
So that stok material ter-update di sistem.

Acceptance Criteria:
- Reference ke PO number (jika ada)
- Select material dari master data
- Input quantity received dan UoM
- Input supplier information
- Upload delivery note photo
- Sistem update stok otomatis setelah save
- Generate goods receipt note

US-INV-002: Monitor Level Stok
As an Inventory Staff,
I want to monitor stock level untuk semua material dan produk,
So that saya dapat anticipate stockout.

Acceptance Criteria:
- Dashboard menampilkan list material/produk dengan current stock
- Highlight item dengan stock < reorder point (warna merah)
- Filter by category, status (low stock, sufficient, overstock)
- Search by nama material/produk
- View stock movement history
- Export stock report to Excel

US-INV-003: Stock Opname
As an Inventory Staff,
I want to conduct periodic stock count,
So that data stock di sistem sesuai dengan physical stock.

Acceptance Criteria:
- Create stock opname session dengan cut-off date
- Print stock count sheet (list material/produk yang akan dicount)
- Input physical count result
- Sistem compare physical vs system count
- Generate variance report
- Approval workflow untuk stock adjustment
- Update sistem stock setelah approved
```

**User Stories - Production Team:**

```
US-PROD-001: Melihat Work Order
As a Production Staff,
I want to see list work order yang assigned ke saya,
So that saya tahu apa yang harus dikerjakan.

Acceptance Criteria:
- Dashboard menampilkan work order list dengan priority
- Filter by status (scheduled, in-progress, completed)
- Sort by due date
- View work order detail (product, quantity, spec, material needed)
- View customer special request (jika ada)
- Indicator untuk urgent order

US-PROD-002: Update Progress Produksi
As a Production Staff,
I want to update progress work order,
So that supervisor dan sales team bisa monitor progress.

Acceptance Criteria:
- Select work order dari list
- Update status (start production, in-progress, quality-check, completed)
- Input percentage completion (0-100%)
- Record material consumption (actual usage)
- Upload work-in-progress photo
- Add notes untuk issues atau delays
- Notification ke supervisor untuk completed work order

US-PROD-003: Quality Control Check
As a Production Supervisor,
I want to perform QC untuk finished product,
So that hanya produk berkualitas yang dikirim ke customer.

Acceptance Criteria:
- QC checklist sesuai product type
- Check pass/fail untuk setiap criteria
- Upload photo untuk defect (jika ada)
- Decision: Pass (move to finished goods) atau Fail (rework required)
- Record defect type dan root cause
- Notify production staff untuk rework jika fail
```

---

## Ringkasan Kebutuhan Sistem

### Total Kebutuhan Fungsional: 26 Requirements
- **CRM Module:** 5 FR
- **Inventory Module:** 6 FR
- **Production Module:** 6 FR
- **Analytics Module:** 6 FR
- **Administration Module:** 4 FR

### Total Kebutuhan Non-Fungsional: 20 Requirements
- **Performance:** 3 NFR
- **Security:** 5 NFR
- **Usability:** 3 NFR
- **Reliability:** 4 NFR
- **Maintainability:** 3 NFR
- **Compatibility:** 3 NFR

### Total User Stories: 12 User Stories
- **Executive:** 3 US
- **Sales Staff:** 3 US
- **Inventory Staff:** 3 US
- **Production Staff:** 3 US

---

*Dokumen ini merupakan Part 1 dari Analisis dan Desain Sistem SATRIAMART SIMS. Untuk Part 2 (Use Case Diagram dan Activity Diagram), Part 3 (ERD), dan Part 4 (User Interface Design), silakan lihat dokumen terpisah.*

