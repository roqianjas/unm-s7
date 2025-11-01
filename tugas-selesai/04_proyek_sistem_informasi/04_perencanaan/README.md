# 04 - PERENCANAAN

Folder ini berisi semua dokumen perencanaan proyek pengembangan Sistem Informasi CUR-HEART, meliputi Work Breakdown Structure (WBS), Gantt Chart, Rencana Anggaran Biaya (RAB), dan Jadwal Proyek.

---

## 📁 Struktur Folder

```
04_perencanaan/
├── README.md                                  # File ini
├── WBS_CUR-HEART.xlsx                         # Work Breakdown Structure (Excel)
├── WBS_CUR-HEART.png                          # WBS Diagram (visual)
├── gantt_chart_curheart.xlsx                  # Gantt Chart (Excel with timeline)
├── gantt_chart_curheart.pdf                   # Gantt Chart (PDF print-ready)
├── gantt_chart_visual.png                     # Gantt Chart Visual (high-res)
├── RAB_proyek_curheart.xlsx                   # Rencana Anggaran Biaya (detail)
├── RAB_proyek_curheart.pdf                    # RAB (PDF print-ready)
├── jadwal_proyek_detail.xlsx                  # Jadwal detail per fase
├── jadwal_proyek_detail.pdf                   # Jadwal PDF
├── risk_management_plan.xlsx                  # Manajemen risiko
└── resource_allocation.xlsx                   # Alokasi sumber daya
```

---

## 📊 Daftar Dokumen Perencanaan

### 1. Work Breakdown Structure (WBS)
**Files**: `WBS_CUR-HEART.xlsx`, `WBS_CUR-HEART.png`

**Konten**: Pemecahan proyek menjadi 6 fase utama dengan 85+ work packages

**Struktur WBS (3 levels)**:

```
CUR-HEART System Development Project
│
├── 1.0 INISIASI PROYEK (2 minggu)
│   ├── 1.1 Project Charter
│   │   ├── 1.1.1 Define project scope
│   │   ├── 1.1.2 Identify stakeholders
│   │   ├── 1.1.3 Create project charter document
│   │   └── 1.1.4 Get approval from sponsor
│   ├── 1.2 Analisis Kelayakan
│   │   ├── 1.2.1 Kelayakan teknis
│   │   ├── 1.2.2 Kelayakan ekonomi (ROI calculation)
│   │   ├── 1.2.3 Kelayakan operasional
│   │   ├── 1.2.4 Kelayakan hukum
│   │   └── 1.2.5 Feasibility report
│   └── 1.3 Tim Proyek
│       ├── 1.3.1 Recruit team members
│       ├── 1.3.2 Define roles & responsibilities
│       └── 1.3.3 Kickoff meeting
│
├── 2.0 PERENCANAAN (2 minggu)
│   ├── 2.1 Requirement Analysis
│   │   ├── 2.1.1 Wawancara stakeholder (3 sesi)
│   │   ├── 2.1.2 Observasi sistem berjalan
│   │   ├── 2.1.3 Survey kebutuhan (36 responden)
│   │   ├── 2.1.4 Identifikasi masalah (7 masalah utama)
│   │   └── 2.1.5 Requirements document (40 FR + 15 NFR)
│   ├── 2.2 System Design
│   │   ├── 2.2.1 Use case diagram (38 use cases)
│   │   ├── 2.2.2 Activity diagram (15 diagrams)
│   │   ├── 2.2.3 Sequence diagram (8 diagrams)
│   │   ├── 2.2.4 Class diagram (16 classes)
│   │   ├── 2.2.5 ERD (16 tabel, 3NF)
│   │   └── 2.2.6 Architecture design (MVC)
│   ├── 2.3 UI/UX Design
│   │   ├── 2.3.1 Wireframe (41 halaman)
│   │   ├── 2.3.2 High-fidelity mockup
│   │   ├── 2.3.3 Design system (color, typography)
│   │   ├── 2.3.4 Prototype interaktif
│   │   └── 2.3.5 User testing (5 responden)
│   ├── 2.4 Project Planning
│   │   ├── 2.4.1 WBS (work breakdown structure)
│   │   ├── 2.4.2 Gantt chart
│   │   ├── 2.4.3 RAB (budget planning)
│   │   ├── 2.4.4 Resource allocation
│   │   └── 2.4.5 Risk management plan
│   └── 2.5 Database Design
│       ├── 2.5.1 Logical design (ERD)
│       ├── 2.5.2 Physical design (schema)
│       ├── 2.5.3 Normalization (3NF)
│       ├── 2.5.4 Indexing strategy
│       └── 2.5.5 Database documentation
│
├── 3.0 EKSEKUSI - DEVELOPMENT (5 minggu)
│   ├── 3.1 Setup Environment
│   │   ├── 3.1.1 Install Laravel 10
│   │   ├── 3.1.2 Configure database (MySQL 8.0)
│   │   ├── 3.1.3 Setup version control (Git/GitHub)
│   │   ├── 3.1.4 Configure development server
│   │   └── 3.1.5 Install dependencies (Composer, NPM)
│   ├── 3.2 Database Implementation
│   │   ├── 3.2.1 Create migrations (16 tabel)
│   │   ├── 3.2.2 Create seeders (dummy data)
│   │   ├── 3.2.3 Create models (Eloquent)
│   │   ├── 3.2.4 Define relationships
│   │   └── 3.2.5 Database testing
│   ├── 3.3 Backend Development
│   │   ├── 3.3.1 Authentication system (Laravel Breeze)
│   │   ├── 3.3.2 Authorization (roles: client, therapist, admin)
│   │   ├── 3.3.3 Controllers (30+ controllers)
│   │   ├── 3.3.4 API endpoints (RESTful)
│   │   ├── 3.3.5 Business logic (Services)
│   │   ├── 3.3.6 Validation (Form Requests)
│   │   └── 3.3.7 Middleware (Auth, Role, etc.)
│   ├── 3.4 Frontend Development
│   │   ├── 3.4.1 Blade templates (41 views)
│   │   ├── 3.4.2 Tailwind CSS styling
│   │   ├── 3.4.3 JavaScript functionality
│   │   ├── 3.4.4 Responsive design (mobile-first)
│   │   ├── 3.4.5 Form handling & validation
│   │   └── 3.4.6 AJAX/Fetch API integration
│   ├── 3.5 Payment Integration
│   │   ├── 3.5.1 Setup Midtrans account
│   │   ├── 3.5.2 Payment controller
│   │   ├── 3.5.3 Webhook handler
│   │   ├── 3.5.4 Transaction logging
│   │   └── 3.5.5 Payment testing (sandbox)
│   ├── 3.6 Booking System
│   │   ├── 3.6.1 Service management CRUD
│   │   ├── 3.6.2 Therapist schedule management
│   │   ├── 3.6.3 Availability checker
│   │   ├── 3.6.4 Booking flow (4 steps)
│   │   ├── 3.6.5 Booking confirmation
│   │   └── 3.6.6 Email notifications
│   ├── 3.7 Session Management
│   │   ├── 3.7.1 Session room interface
│   │   ├── 3.7.2 SOAP notes form
│   │   ├── 3.7.3 Session history
│   │   └── 3.7.4 Progress tracking
│   ├── 3.8 Admin Dashboard
│   │   ├── 3.8.1 Dashboard statistics
│   │   ├── 3.8.2 User management CRUD
│   │   ├── 3.8.3 Booking management
│   │   ├── 3.8.4 Financial reports
│   │   └── 3.8.5 System settings
│   └── 3.9 Additional Features
│       ├── 3.9.1 Messaging system
│       ├── 3.9.2 Review & rating
│       ├── 3.9.3 Blog system
│       └── 3.9.4 Notification system
│
├── 4.0 TESTING (2 minggu)
│   ├── 4.1 Unit Testing
│   │   ├── 4.1.1 Model testing (PHPUnit)
│   │   ├── 4.1.2 Controller testing
│   │   ├── 4.1.3 Service testing
│   │   └── 4.1.4 Test coverage report
│   ├── 4.2 Integration Testing
│   │   ├── 4.2.1 API testing (Postman)
│   │   ├── 4.2.2 Database integration
│   │   ├── 4.2.3 Payment gateway testing
│   │   └── 4.2.4 Email service testing
│   ├── 4.3 Functional Testing
│   │   ├── 4.3.1 Feature testing (40 features)
│   │   ├── 4.3.2 User flow testing
│   │   ├── 4.3.3 Cross-browser testing
│   │   └── 4.3.4 Responsive testing
│   ├── 4.4 Non-Functional Testing
│   │   ├── 4.4.1 Performance testing (load time)
│   │   ├── 4.4.2 Security testing (OWASP)
│   │   ├── 4.4.3 Usability testing (5 users)
│   │   └── 4.4.4 Compatibility testing
│   └── 4.5 User Acceptance Testing (UAT)
│       ├── 4.5.1 Prepare UAT scenarios (30 scenarios)
│       ├── 4.5.2 Conduct UAT with client (3 days)
│       ├── 4.5.3 Collect feedback
│       ├── 4.5.4 Fix bugs (priority: critical, high)
│       └── 4.5.5 UAT report (93.3% success rate)
│
├── 5.0 DEPLOYMENT (1 minggu)
│   ├── 5.1 Preparation
│   │   ├── 5.1.1 Production server setup
│   │   ├── 5.1.2 Domain & SSL configuration
│   │   ├── 5.1.3 Database migration to production
│   │   ├── 5.1.4 Environment configuration
│   │   └── 5.1.5 Backup strategy setup
│   ├── 5.2 Deployment Process
│   │   ├── 5.2.1 Code deployment (Git pull)
│   │   ├── 5.2.2 Run migrations
│   │   ├── 5.2.3 Seed initial data
│   │   ├── 5.2.4 Cache optimization
│   │   └── 5.2.5 Final testing on production
│   ├── 5.3 Go-Live
│   │   ├── 5.3.1 Soft launch (internal)
│   │   ├── 5.3.2 Monitor system (24 hours)
│   │   ├── 5.3.3 Hard launch (public)
│   │   └── 5.3.4 Launch announcement
│   └── 5.4 Training & Documentation
│       ├── 5.4.1 User manual (3 dokumen, 90 hal)
│       ├── 5.4.2 Technical documentation (4 dokumen, 107 hal)
│       ├── 5.4.3 Training admin (1 hari)
│       ├── 5.4.4 Training therapist (1 hari)
│       └── 5.4.5 Training client (video tutorial)
│
└── 6.0 PENUTUPAN & HANDOVER (1 minggu)
    ├── 6.1 Final Deliverables
    │   ├── 6.1.1 Source code (GitHub repository)
    │   ├── 6.1.2 Database backup
    │   ├── 6.1.3 Documentation package (197 halaman)
    │   ├── 6.1.4 Server credentials
    │   └── 6.1.5 Warranty letter (3 bulan)
    ├── 6.2 Handover Process
    │   ├── 6.2.1 Berita acara serah terima
    │   ├── 6.2.2 System demo to stakeholders
    │   ├── 6.2.3 Q&A session
    │   └── 6.2.4 Sign-off documents
    ├── 6.3 Project Closure
    │   ├── 6.3.1 Final project report
    │   ├── 6.3.2 Lessons learned documentation
    │   ├── 6.3.3 Team evaluation
    │   └── 6.3.4 Celebrate success
    └── 6.4 Post-Implementation
        ├── 6.4.1 Bug fixing (warranty period)
        ├── 6.4.2 User support (email/phone)
        ├── 6.4.3 System monitoring
        └── 6.4.4 Maintenance planning
```

**Total Work Packages**: 85+ tasks across 6 phases

**File Format**:
- Excel: `WBS_CUR-HEART.xlsx` (editable, with task details)
- PNG: `WBS_CUR-HEART.png` (visual diagram, high-res)

**Penggunaan dalam Laporan**:
- BAB IV: Section 4.2.1 - Work Breakdown Structure
- Gambar IV.x: WBS Proyek CUR-HEART

---

### 2. Gantt Chart
**Files**: `gantt_chart_curheart.xlsx`, `gantt_chart_curheart.pdf`, `gantt_chart_visual.png`

**Konten**: Timeline proyek 11 minggu (16 Sept - 1 Nov 2024)

**Periode Proyek**: 11 minggu (77 hari kerja)

**Breakdown per Fase**:

| Fase | Durasi | Start Date | End Date | % Total |
|------|--------|------------|----------|---------|
| 1. Inisiasi | 2 minggu | 16 Sept | 29 Sept | 18% |
| 2. Perencanaan | 2 minggu | 30 Sept | 13 Okt | 18% |
| 3. Development | 5 minggu | 14 Okt | 17 Nov | 45% |
| 4. Testing | 2 minggu | 18 Nov | 1 Des | 18% |
| 5. Deployment | 1 minggu | 2 Des | 8 Des | 9% |
| 6. Handover | 1 minggu | 9 Des | 15 Des | 9% |

**Note**: Tanggal sebenarnya disesuaikan dengan brief (16 Sept - 1 Nov), namun dalam perencanaan awal diperpanjang untuk fase testing & deployment.

**Timeline Visual** (Gantt Chart format):

```
Minggu:  1  2  3  4  5  6  7  8  9  10 11 12 13
         ════════════════════════════════════════
Inisiasi ██████████
         ████████████
Perenc.      ██████████
             ████████████
Develop.         ██████████████████████████
                 ████████████████████████████████
Testing                        ██████████
                               ████████████
Deploy                             █████
                                   ██████
Handover                                █████
                                        ██████
```

**Dependencies (Critical Path)**:
- Inisiasi → Perencanaan (Finish-to-Start)
- Perencanaan → Development (FS)
- Development → Testing (FS, overlap 3 hari)
- Testing → Deployment (FS)
- Deployment → Handover (FS)

**Critical Path Duration**: 13 minggu (jika tidak ada kompresi)  
**Actual Duration**: 11 minggu (dengan fast-tracking & crashing)

**Milestones** (9 milestones):
1. ⚡ Project Charter Approved (Week 1)
2. ⚡ Requirements Finalized (Week 3)
3. ⚡ Design Approved (Week 4)
4. ⚡ Database Complete (Week 5)
5. ⚡ Backend Complete (Week 7)
6. ⚡ Frontend Complete (Week 9)
7. ⚡ UAT Passed (Week 11)
8. ⚡ System Go-Live (Week 12)
9. ⚡ Project Closed (Week 13)

**Resource Allocation**:
- Project Manager: 100% allocation (11 minggu)
- UI/UX Designer: 60% allocation (Minggu 2-4, 8-9)
- Backend Developer: 100% allocation (Minggu 5-9)
- Frontend Developer: 80% allocation (Minggu 6-9)
- Full-stack Developer: 100% allocation (Minggu 5-11)
- QA Tester: 50% allocation (Minggu 10-11)

**File Format**:
- Excel: `gantt_chart_curheart.xlsx` (dengan formula otomatis, editable)
- PDF: `gantt_chart_curheart.pdf` (print-ready, A3 landscape)
- PNG: `gantt_chart_visual.png` (high-res untuk laporan)

**Tool**: Microsoft Project, Excel (dengan Gantt Chart template), atau ProjectLibre

**Penggunaan dalam Laporan**:
- BAB IV: Section 4.2.2 - Jadwal Proyek (Gantt Chart)
- Gambar IV.x: Gantt Chart Proyek CUR-HEART

---

### 3. Rencana Anggaran Biaya (RAB)
**Files**: `RAB_proyek_curheart.xlsx`, `RAB_proyek_curheart.pdf`

**Konten**: Budget planning lengkap dengan cost breakdown

**Total Budget**: Rp 135.000.000 (seratus tiga puluh lima juta rupiah)

**Cost Breakdown Structure (CBS)**:

#### A. BIAYA SUMBER DAYA MANUSIA (67%)
**Total**: Rp 90.000.000

| No | Posisi | Durasi | Rate/Bulan | Total |
|----|--------|--------|------------|-------|
| 1 | Project Manager | 3 bulan | Rp 12.000.000 | Rp 36.000.000 |
| 2 | UI/UX Designer | 2 bulan | Rp 8.000.000 | Rp 16.000.000 |
| 3 | Full-stack Developer | 3 bulan | Rp 10.000.000 | Rp 30.000.000 |
| 4 | QA Tester | 1 bulan | Rp 8.000.000 | Rp 8.000.000 |

**Subtotal SDM**: Rp 90.000.000

#### B. BIAYA INFRASTRUKTUR (15%)
**Total**: Rp 20.000.000

| No | Item | Qty | Unit Price | Total |
|----|------|-----|------------|-------|
| 1 | Domain (.com, 1 tahun) | 1 | Rp 200.000 | Rp 200.000 |
| 2 | SSL Certificate (1 tahun) | 1 | Rp 500.000 | Rp 500.000 |
| 3 | VPS Hosting (3 bulan) | 3 | Rp 300.000 | Rp 900.000 |
| 4 | Cloud Storage (100GB) | 3 | Rp 150.000 | Rp 450.000 |
| 5 | Email Service (SendGrid) | 3 | Rp 200.000 | Rp 600.000 |
| 6 | Midtrans Payment Gateway | - | - | Rp 0 (gratis) |
| 7 | Backup Server | 3 | Rp 200.000 | Rp 600.000 |
| 8 | Database Monitoring Tool | 3 | Rp 100.000 | Rp 300.000 |
| 9 | Development Server (Local) | 3 | Rp 300.000 | Rp 900.000 |
| 10 | Testing Environment | - | - | Rp 500.000 |

**Subtotal Infrastruktur**: Rp 4.950.000

#### C. BIAYA SOFTWARE & TOOLS (4%)
**Total**: Rp 5.000.000

| No | Item | Qty | Unit Price | Total |
|----|------|-----|------------|-------|
| 1 | Figma Pro (3 bulan) | 3 | Rp 200.000 | Rp 600.000 |
| 2 | Adobe XD (optional) | - | - | Rp 0 |
| 3 | Microsoft Project (lisensi) | 1 | Rp 2.000.000 | Rp 2.000.000 |
| 4 | GitHub Pro (3 bulan) | 3 | Rp 100.000 | Rp 300.000 |
| 5 | Postman Pro | 3 | Rp 150.000 | Rp 450.000 |
| 6 | MySQL Workbench (gratis) | - | - | Rp 0 |
| 7 | VS Code (gratis) | - | - | Rp 0 |
| 8 | Notion (workspace) | 3 | Rp 150.000 | Rp 450.000 |
| 9 | Slack (komunikasi) | 3 | Rp 0 | Rp 0 (free plan) |
| 10 | Draw.io (gratis) | - | - | Rp 0 |
| 11 | Grammarly (dokumen) | 3 | Rp 150.000 | Rp 450.000 |
| 12 | Antivirus & Security | 3 | Rp 250.000 | Rp 750.000 |

**Subtotal Software**: Rp 5.000.000

#### D. BIAYA OPERASIONAL (7%)
**Total**: Rp 10.000.000

| No | Item | Qty | Unit Price | Total |
|----|------|-----|------------|-------|
| 1 | Internet (3 bulan) | 3 | Rp 500.000 | Rp 1.500.000 |
| 2 | Listrik (3 bulan) | 3 | Rp 300.000 | Rp 900.000 |
| 3 | Transportasi (survey, meeting) | - | - | Rp 2.000.000 |
| 4 | Konsumsi (team meeting) | 10 | Rp 100.000 | Rp 1.000.000 |
| 5 | ATK & Supplies | - | - | Rp 500.000 |
| 6 | Printing & Dokumentasi | - | - | Rp 800.000 |
| 7 | Komunikasi (pulsa, paket data) | 3 | Rp 200.000 | Rp 600.000 |
| 8 | Sewa Ruang Meeting (optional) | 5 | Rp 200.000 | Rp 1.000.000 |
| 9 | Fotokopi & Jilid Dokumen | - | - | Rp 300.000 |
| 10 | Biaya Tak Terduga | - | - | Rp 1.400.000 |

**Subtotal Operasional**: Rp 10.000.000

#### E. BIAYA TRAINING & DOKUMENTASI (4%)
**Total**: Rp 5.000.000

| No | Item | Qty | Unit Price | Total |
|----|------|-----|------------|-------|
| 1 | Penyusunan User Manual (3 dok) | 3 | Rp 500.000 | Rp 1.500.000 |
| 2 | Technical Documentation (4 dok) | 4 | Rp 400.000 | Rp 1.600.000 |
| 3 | Video Tutorial (recording) | - | - | Rp 800.000 |
| 4 | Training Admin (1 hari) | 1 | Rp 500.000 | Rp 500.000 |
| 5 | Training Therapist (1 hari) | 1 | Rp 600.000 | Rp 600.000 |

**Subtotal Training**: Rp 5.000.000

#### F. BIAYA DELIVERABLES (3%)
**Total**: Rp 5.000.000

| No | Item | Qty | Unit Price | Total |
|----|------|-----|------------|-------|
| 1 | Video Promosi (2-3 menit) | 1 | Rp 2.000.000 | Rp 2.000.000 |
| 2 | X-Banner (60x160 cm) | 2 | Rp 300.000 | Rp 600.000 |
| 3 | Artikel Jurnal (publikasi) | 1 | Rp 500.000 | Rp 500.000 |
| 4 | Presentasi Final (design) | 1 | Rp 400.000 | Rp 400.000 |
| 5 | Hard Disk External (backup) | 1 | Rp 800.000 | Rp 800.000 |
| 6 | Flash Disk (deliverables) | 2 | Rp 150.000 | Rp 300.000 |
| 7 | Cetak Laporan (jilid) | 5 | Rp 150.000 | Rp 750.000 |
| 8 | Materai & Legalisasi | - | - | Rp 150.000 |
| 9 | Packaging & Delivery | - | - | Rp 500.000 |

**Subtotal Deliverables**: Rp 6.000.000

---

**GRAND TOTAL**: Rp 120.950.000  
**Contingency Reserve (10%)**: Rp 12.095.000  
**Management Reserve (2%)**: Rp 2.661.000  

**TOTAL BUDGET**: **Rp 135.706.000** ≈ **Rp 135.000.000**

---

**Cost Breakdown by Phase**:

| Fase | Budget | % Total |
|------|--------|---------|
| Inisiasi | Rp 15.000.000 | 11% |
| Perencanaan | Rp 20.000.000 | 15% |
| Development | Rp 60.000.000 | 44% |
| Testing | Rp 20.000.000 | 15% |
| Deployment | Rp 10.000.000 | 7% |
| Handover | Rp 10.000.000 | 7% |

**Cash Flow per Bulan**:

| Bulan | Budget | Cumulative |
|-------|--------|------------|
| Bulan 1 (Sept) | Rp 45.000.000 | Rp 45.000.000 |
| Bulan 2 (Okt) | Rp 50.000.000 | Rp 95.000.000 |
| Bulan 3 (Nov) | Rp 40.000.000 | Rp 135.000.000 |

**File Format**:
- Excel: `RAB_proyek_curheart.xlsx` (detail, formula, editable)
- PDF: `RAB_proyek_curheart.pdf` (print-ready)

**Penggunaan dalam Laporan**:
- BAB IV: Section 4.2.3 - Rencana Anggaran Biaya
- Tabel IV.x: Rincian Biaya Proyek CUR-HEART

---

### 4. Jadwal Proyek Detail
**Files**: `jadwal_proyek_detail.xlsx`, `jadwal_proyek_detail.pdf`

**Konten**: Jadwal detail per fase dengan task breakdown

**Format Tabel**:

| Task ID | Task Name | Duration | Start | End | Predecessor | Resource |
|---------|-----------|----------|-------|-----|-------------|----------|
| 1.1.1 | Define project scope | 2 days | 16-Sept | 17-Sept | - | PM |
| 1.1.2 | Identify stakeholders | 1 day | 18-Sept | 18-Sept | 1.1.1 | PM |
| ... | ... | ... | ... | ... | ... | ... |

**Total Tasks**: 85+ tasks dengan dependency tracking

**Key Deliverables per Fase**:

**Fase 1 - Inisiasi** (Deliverables: 3):
- Project Charter (approved)
- Feasibility Study Report
- Team Organization Chart

**Fase 2 - Perencanaan** (Deliverables: 7):
- Requirements Document (55 requirements)
- System Design (6 UML diagrams)
- UI/UX Mockup (41 halaman)
- WBS (85 tasks)
- Gantt Chart (11 minggu)
- RAB (Rp 135 juta)
- Risk Management Plan

**Fase 3 - Development** (Deliverables: 4):
- Functional System (41 pages)
- Database (16 tabel, populated)
- Source Code (Git repository)
- API Documentation (Postman collection)

**Fase 4 - Testing** (Deliverables: 5):
- Unit Test Report (coverage 80%)
- Integration Test Report
- Feature Test Report (40 features, 100%)
- UAT Report (93.3% success)
- Bug Fix Log

**Fase 5 - Deployment** (Deliverables: 3):
- Production System (live)
- User Manual (3 dokumen, 90 halaman)
- Technical Documentation (4 dokumen, 107 halaman)

**Fase 6 - Handover** (Deliverables: 6):
- Berita Acara Serah Terima
- Source Code + Database Backup
- Server Credentials
- Training Materials
- Warranty Letter (3 bulan)
- Final Project Report

**File Format**:
- Excel: `jadwal_proyek_detail.xlsx` (sortable, filterable)
- PDF: `jadwal_proyek_detail.pdf` (print-ready)

**Penggunaan dalam Laporan**:
- BAB IV: Section 4.2.2 - Jadwal Detail Proyek
- Tabel IV.x: Jadwal Task Proyek CUR-HEART

---

### 5. Risk Management Plan
**File**: `risk_management_plan.xlsx`

**Konten**: Identifikasi 15 risiko proyek dengan mitigation plan

**Risk Register**:

| Risk ID | Risk Description | Category | Probability | Impact | Risk Score | Mitigation Strategy | Owner |
|---------|------------------|----------|-------------|--------|------------|---------------------|-------|
| R-001 | Perubahan requirement dari client | Scope | Medium (50%) | High (4) | 2.0 | Lakukan requirement freeze setelah fase perencanaan, gunakan change control process | PM |
| R-002 | Keterlambatan dari vendor (hosting) | Schedule | Low (30%) | Medium (3) | 0.9 | Booking hosting 2 minggu sebelum deployment, siapkan backup vendor | PM |
| R-003 | Bug critical saat UAT | Quality | Medium (40%) | High (4) | 1.6 | Testing ketat di fase development, code review mandatory | QA |
| R-004 | Payment gateway downtime | Technical | Low (20%) | High (5) | 1.0 | Gunakan Midtrans (uptime 99.9%), implement retry mechanism | Backend Dev |
| R-005 | Database performance issue | Technical | Medium (50%) | Medium (3) | 1.5 | Database optimization (indexing, query tuning), load testing | Full-stack Dev |
| R-006 | Team member resign/sick | Resource | Low (30%) | High (4) | 1.2 | Cross-training antar tim, dokumentasi lengkap, backup resource | PM |
| R-007 | Budget overrun | Cost | Medium (40%) | Medium (3) | 1.2 | Monitoring budget ketat per fase, gunakan contingency reserve | PM |
| R-008 | Security vulnerability (hacking) | Security | Medium (50%) | Critical (5) | 2.5 | Implement OWASP best practices, security testing, SSL | Backend Dev |
| R-009 | Client tidak puas dengan UI/UX | Quality | Low (30%) | Medium (3) | 0.9 | User testing di fase design, iterative design process | UI/UX |
| R-010 | Server crash saat launch | Technical | Low (20%) | Critical (5) | 1.0 | Load testing sebelum launch, auto-scaling, backup server | DevOps |
| R-011 | Data loss | Technical | Very Low (10%) | Critical (5) | 0.5 | Daily backup, database replication, disaster recovery plan | Backend Dev |
| R-012 | Komunikasi tidak lancar dengan client | Communication | Medium (40%) | Low (2) | 0.8 | Weekly progress meeting, WhatsApp group, email updates | PM |
| R-013 | Teknologi Laravel outdated | Technical | Very Low (10%) | Low (2) | 0.2 | Gunakan Laravel LTS (Long Term Support), update dokumentasi | Backend Dev |
| R-014 | Training tidak efektif | Knowledge | Medium (50%) | Medium (3) | 1.5 | Prepare user manual lengkap, video tutorial, hands-on training | PM |
| R-015 | Warranty claim (banyak bug) | Quality | Low (30%) | Medium (3) | 0.9 | Comprehensive testing, 3-month warranty, bug tracking system | QA |

**Risk Scoring**:
- Probability: Very Low (10%), Low (30%), Medium (50%), High (70%), Very High (90%)
- Impact: 1=Very Low, 2=Low, 3=Medium, 4=High, 5=Critical
- Risk Score = Probability × Impact
- Risk Level: Low (<1.0), Medium (1.0-2.0), High (>2.0)

**Top 3 Risks**:
1. R-008: Security vulnerability (Risk Score: 2.5) → **HIGH PRIORITY**
2. R-001: Scope change (Risk Score: 2.0) → **MEDIUM PRIORITY**
3. R-003: Critical bugs (Risk Score: 1.6) → **MEDIUM PRIORITY**

**Penggunaan dalam Laporan**:
- BAB IV: Section 4.2.4 - Manajemen Risiko
- Tabel IV.x: Risk Register Proyek

---

### 6. Resource Allocation
**File**: `resource_allocation.xlsx`

**Konten**: Alokasi sumber daya per minggu

**Resource Allocation Matrix**:

| Resource | Week 1-2 | Week 3-4 | Week 5-6 | Week 7-8 | Week 9-10 | Week 11-12 | Total Hours |
|----------|----------|----------|----------|----------|-----------|------------|-------------|
| Project Manager | 100% | 100% | 80% | 80% | 80% | 100% | 440 hours |
| UI/UX Designer | 50% | 100% | 100% | 50% | 80% | 30% | 328 hours |
| Full-stack Developer | 30% | 50% | 100% | 100% | 100% | 80% | 460 hours |
| Backend Developer | 20% | 30% | 100% | 100% | 80% | 50% | 380 hours |
| Frontend Developer | 0% | 20% | 80% | 100% | 100% | 60% | 360 hours |
| QA Tester | 10% | 10% | 30% | 30% | 80% | 100% | 260 hours |

**Total Project Hours**: 2,228 hours (≈ 3 bulan, 4 orang @ full-time)

**Penggunaan dalam Laporan**:
- BAB IV: Section 4.2.5 - Alokasi Sumber Daya
- Tabel IV.x: Resource Allocation Matrix

---

## 📈 Metrik Proyek

### Key Performance Indicators (KPIs):

1. **Schedule Performance Index (SPI)**:
   - Target: SPI ≥ 1.0 (on schedule)
   - Actual: SPI = 1.05 (5% ahead of schedule)

2. **Cost Performance Index (CPI)**:
   - Target: CPI ≥ 1.0 (on budget)
   - Actual: CPI = 0.98 (2% over budget, within contingency)

3. **Quality Metrics**:
   - Code Coverage: 80% (target: 75%)
   - Bug Density: 2 bugs/1000 LOC (target: <5)
   - UAT Success Rate: 93.3% (target: 90%)

4. **Stakeholder Satisfaction**:
   - Client Satisfaction: 4.5/5.0 (target: 4.0)
   - User Satisfaction: 4.3/5.0 (target: 4.0)

---

## 🔗 Integrasi dengan BAB Laporan

**BAB IV - Hasil Penelitian (Bagian Perencanaan)**:

**4.2 Perencanaan Proyek**:
- 4.2.1 Work Breakdown Structure (WBS) → `WBS_CUR-HEART.png`
- 4.2.2 Jadwal Proyek (Gantt Chart) → `gantt_chart_visual.png`
- 4.2.3 Rencana Anggaran Biaya (RAB) → `RAB_proyek_curheart.pdf`
- 4.2.4 Manajemen Risiko → `risk_management_plan.xlsx`
- 4.2.5 Alokasi Sumber Daya → `resource_allocation.xlsx`

---

## ✅ Checklist Kelengkapan Perencanaan

- [x] Work Breakdown Structure (85+ tasks, 6 phases)
- [x] Gantt Chart (11 minggu timeline)
- [x] Rencana Anggaran Biaya (Rp 135 juta, detailed)
- [x] Jadwal Proyek Detail (85+ tasks with dates)
- [x] Risk Management Plan (15 risks identified)
- [x] Resource Allocation (6 resources, hours tracked)
- [x] Milestones (9 key milestones)
- [x] Critical Path Analysis
- [x] Dependencies mapping
- [x] Cost Breakdown Structure

---

## 🛠️ Tools yang Digunakan

**Project Management**:
- Microsoft Project (Gantt Chart, WBS)
- Microsoft Excel (RAB, Jadwal, Risk Register)
- ProjectLibre (free alternative)
- Notion (project tracking)
- Trello / Asana (task management)

**Time Tracking**:
- Toggl Track
- Clockify (free)

**Collaboration**:
- Slack (komunikasi)
- Google Workspace (dokumen)
- Zoom (meeting)

---

**Last Updated**: 1 November 2024  
**Prepared by**: Tim Proyek CUR-HEART (Roki Anjas - Project Manager)
