# BAB IV  
# HASIL PENELITIAN DAN PEMBAHASAN

## 4.1 Inisiasi Proyek

### 4.1.1 Latar Belakang Proyek

Proyek pengembangan Sistem Informasi Manajemen Booking dan Terapi CUR-HEART diinisiasi berdasarkan kebutuhan mendesak untuk mengoptimalkan operasional pusat layanan hypnotherapy dan kesehatan mental yang semakin berkembang. CUR-HEART (Hypnotherapy & Mind Wellness Center), sebagai salah satu pioneer dalam layanan hypnotherapy profesional di Indonesia, mengalami pertumbuhan signifikan dalam jumlah klien dan terapis sejak berdiri pada tahun 2023.

Dengan visi menjadi pusat terapi kejiwaan berbasis hypnotherapy modern dan spiritual yang terpercaya di Indonesia, CUR-HEART menyediakan enam layanan utama:

1. **Stress & Anxiety Release Therapy** - Mengatasi stres berlebih dan kecemasan yang mengganggu aktivitas sehari-hari
2. **Trauma Healing Hypnotherapy** - Menghapus dampak emosional dari pengalaman traumatis masa lalu
3. **Self-Confidence & Motivation Therapy** - Meningkatkan kepercayaan diri dan semangat hidup
4. **Sleep & Relaxation Therapy** - Mengatasi insomnia dan gangguan tidur dengan teknik relaksasi mendalam
5. **Habit Reprogramming Therapy** - Mengubah kebiasaan negatif seperti merokok atau menunda pekerjaan
6. **Phobia & Fear Management** - Menangani rasa takut berlebihan terhadap situasi tertentu

Namun, pertumbuhan ini tidak diiringi dengan sistem operasional yang memadai. Proses booking yang masih manual melalui WhatsApp dan telepon, manajemen jadwal terapis menggunakan spreadsheet, serta dokumentasi sesi terapi dalam format kertas dan file Word terpisah menimbulkan berbagai inefficiency yang menghambat kualitas layanan dan potensi pertumbuhan bisnis.

### 4.1.2 Permasalahan yang Dihadapi

Berdasarkan observasi lapangan dan wawancara mendalam dengan stakeholders CUR-HEART pada September 2024, teridentifikasi delapan permasalahan kritis:

**1. Conversion Rate Booking yang Rendah (60%)**

Dari 100 inquiry yang masuk, hanya 60 yang berubah menjadi actual booking. Data historis menunjukkan bahwa 40% potensial klien membatalkan niat mereka karena:
- Proses booking yang memakan waktu (rata-rata 15-20 menit komunikasi bolak-balik)
- Harus menghubungi admin di jam kerja saja
- Tidak bisa langsung melihat availability terapis secara real-time
- Informasi tidak lengkap tentang layanan dan terapis

**2. Konflik Jadwal dan Double Booking (8-10 kasus per bulan)**

Manajemen jadwal manual menggunakan Google Calendar terpisah untuk setiap terapis menyebabkan:
- 8-10 kasus double booking per bulan yang harus direscheduled emergency
- Kesulitan saat terapis berhalangan mendadak (sakit, urgent matter)
- Tidak ada visibility terhadap total kapasitas dan okupansi
- Ketimpangan workload antar terapis (beberapa overbooked, yang lain underutilized)

**3. Waktu Dokumentasi Terapi yang Lama (15 menit per sesi)**

Terapis menghabiskan rata-rata 15 menit setelah setiap sesi untuk:
- Menulis catatan sesi secara manual di buku atau Word
- Menyimpan dan mencari file dengan naming convention yang tidak konsisten
- Kesulitan mengakses riwayat terapi klien sebelum sesi berikutnya
- Risiko kehilangan data tinggi (file corrupt, lost document)

**4. Tidak Ada Data untuk Decision Making**

Manajemen kesulitan mendapatkan insight bisnis karena:
- Data tersebar di berbagai platform (WhatsApp, Excel, file fisik)
- Pembuatan laporan bulanan memakan waktu 2-3 hari kerja
- Tidak ada visibility terhadap KPI penting (conversion rate, revenue per service, therapist utilization)
- Keputusan bisnis masih berbasis intuisi, bukan data

**5. Pengalaman Klien yang Kurang Optimal**

Klien mengalami frustration karena:
- Harus selalu menghubungi admin untuk segala informasi
- Tidak ada platform untuk tracking progress terapi mereka
- Tidak bisa reschedule atau cancel booking secara mandiri
- Proses pembayaran manual dengan konfirmasi yang lama

**6. Beban Administratif yang Tinggi**

Admin menghabiskan 70% waktu kerja untuk:
- Menjawab pertanyaan yang sama berulang kali
- Mengelola booking dan reschedule manual
- Verifikasi pembayaran manual
- Mengompilasi data untuk reporting

**7. Security dan Privacy Risks**

Data klien yang sangat sensitif (riwayat trauma, masalah psikologis):
- Disimpan dalam format tidak secure (Word tidak ter-encrypt, kertas fisik)
- Tidak ada access control yang proper
- Tidak ada audit trail
- Berpotensi melanggar UU Perlindungan Data Pribadi

**8. Hambatan Skalabilitas**

Sistem manual tidak dapat mengakomodasi growth:
- Penambahan terapis baru memperumit koordinasi
- Tidak bisa efisien handle volume booking yang meningkat
- Sulit untuk ekspansi ke lokasi cabang baru
- Technology infrastructure tidak mendukung scale

### 4.1.3 Tujuan Proyek

Proyek ini memiliki tujuan utama dan tujuan khusus sebagai berikut:

**Tujuan Utama:**

Mengembangkan sistem informasi manajemen booking dan terapi berbasis web yang terintegrasi, efisien, user-friendly, dan secure untuk meningkatkan efisiensi operasional CUR-HEART minimal 40%, meningkatkan conversion rate booking dari 60% menjadi 85%, dan memberikan foundation untuk skalabilitas bisnis jangka panjang.

**Tujuan Khusus:**

1. Mengotomatisasi proses booking dengan multi-step flow yang intuitif, memungkinkan klien booking 24/7
2. Mengintegrasikan manajemen jadwal terapis untuk eliminasi konflik scheduling
3. Menyediakan sistem dokumentasi terapi terstruktur yang menghemat waktu hingga 60%
4. Memfasilitasi tracking progress klien dengan visualisasi data yang meaningful
5. Menyediakan dashboard business intelligence untuk data-driven decision making
6. Mengimplementasikan sistem pembayaran digital terintegrasi
7. Menjamin keamanan data klien sesuai compliance UU PDP
8. Meningkatkan user experience untuk semua stakeholders (admin, terapis, klien)

### 4.1.4 Stakeholder Analysis

Analisis stakeholder mengidentifikasi pihak-pihak yang terlibat dan berkepentingan dalam proyek:

**1. Primary Stakeholders:**

| Stakeholder | Role | Interest | Influence | Engagement Strategy |
|-------------|------|----------|-----------|---------------------|
| Owner CUR-HEART | Decision Maker | ROI, Business Growth, Competitive Advantage | Very High | Weekly progress updates, milestone approvals, UAT involvement |
| Terapis (5 orang) | Primary Users | Ease of use, Time saving, Better client management | High | Requirements workshop, usability testing, training sessions |
| Admin Staff (2 orang) | System Operators | Workload reduction, Efficiency | High | Process mapping sessions, UAT, comprehensive training |
| Klien (Existing & Potential) | End Users | Convenience, Privacy, Good UX | Medium | User research, usability testing, feedback surveys |

**2. Secondary Stakeholders:**

| Stakeholder | Role | Interest | Influence | Engagement Strategy |
|-------------|------|----------|-----------|---------------------|
| Dosen Pembimbing | Academic Supervisor | Quality, Learning outcomes, Documentation | High | Weekly consultation, progress reviews, technical guidance |
| Tim Pengembang | Project Team | Successful delivery, Learning, Portfolio | Very High | Daily standups, collaborative development, peer reviews |
| Universitas Nusa Mandiri | Academic Institution | Student achievement, Industry collaboration | Medium | Progress reports, final presentation, documentation submission |

**Stakeholder Power-Interest Matrix:**

```
High Power
    │
    │   [Owner]        [Dosen Pembimbing]
    │   [Terapis]      [Tim Pengembang]
    │
    │   [Admin]
    │
    │   [Klien]        [Universitas]
    │
    └─────────────────────────────────────► High Interest
Low Power                                    
```

**Stakeholder Engagement Plan:**

- **Manage Closely:** Owner, Terapis, Tim Pengembang (High Power, High Interest)
- **Keep Satisfied:** Dosen Pembimbing (High Power, Medium Interest)
- **Keep Informed:** Admin Staff, Klien (Medium Power, High Interest)
- **Monitor:** Universitas (Low Power, Medium Interest)

### 4.1.5 Project Charter

**Project Charter - Sistem Informasi CUR-HEART**

**Project Title:** Pengembangan Sistem Informasi Manajemen Booking dan Terapi CUR-HEART Berbasis Web

**Project Manager:** Roki Anjas (NIM: 11250066)

**Project Sponsor:** CUR-HEART Management

**Project Start Date:** 16 September 2024

**Target Completion Date:** 1 Desember 2024

**Budget:** Rp 5.000.000 (estimasi untuk hosting, domain, payment gateway setup, development tools)

**Project Objectives:**
1. Develop fully functional web-based booking and therapy management system
2. Achieve minimum 95% functional requirements compliance
3. Achieve minimum 80/100 System Usability Scale (SUS) score
4. Complete within 11-week timeframe
5. Stay within allocated budget
6. Provide comprehensive documentation

**Project Scope:**

**In Scope:**
- Web application with 41 pages (public, authentication, dashboards)
- Multi-role authentication (admin, therapist, client)
- Online booking system with 4-step flow
- Therapist schedule management
- Session documentation system
- Client progress tracking
- Payment integration (manual verification dan digital payment gateway)
- Dashboard analytics and reporting
- Email notifications
- Responsive design (mobile-friendly)

**Out of Scope:**
- Native mobile applications (iOS/Android)
- AI-powered features (chatbot, recommendations)
- Video conference native integration (akan gunakan third-party iframe)
- Multi-language support (English only dalam Indonesia)
- Electronic prescription atau medical records integration
- Multi-tenant architecture

**Key Deliverables:**
1. Functional web application (production-ready)
2. Source code repository (GitHub)
3. Complete documentation (technical, user manual)
4. Capstone project report (80-100 pages)
5. Presentation slides and demo video
6. Training materials for users

**Success Criteria:**
1. All must-have functional requirements implemented
2. System passes UAT with stakeholder approval
3. SUS score ≥ 80/100
4. No critical or high-severity bugs in production
5. System uptime ≥ 99% in first month
6. Conversion rate increase from 60% to minimum 75%
7. Documentation complete and approved

**Key Risks:**

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| Scope creep | Medium | High | Strict change control process, prioritize must-haves |
| Technical challenges | Medium | Medium | Regular technical reviews, mentor consultation |
| Stakeholder unavailability | Low | Medium | Flexible scheduling, asynchronous communication |
| Timeline delay | Medium | High | Weekly monitoring, buffer time allocation |
| Integration issues | Low | High | Early testing of integrations, backup plans |
| Data security breach | Low | Very High | Security best practices, regular audits |

**Assumptions:**
- CUR-HEART will provide required business information and documents
- Stakeholders will be available for interviews and testing
- Internet connection and development tools will be available
- Payment gateway APIs will be accessible for testing
- Existing client data (if any migration needed) is available

**Constraints:**
- Timeline: Must complete within 11 weeks (semester schedule)
- Budget: Limited to Rp 5.000.000
- Resources: 3-person development team
- Technology: Must use Laravel framework (academic requirement)
- Compliance: Must adhere to data protection regulations

**Approval:**

| Name | Role | Signature | Date |
|------|------|-----------|------|
| [Owner Name] | Project Sponsor | _____________ | ___/___/___ |
| Roki Anjas | Project Manager | _____________ | ___/___/___ |
| Rani Irma Handayani, M.Kom | Academic Supervisor | _____________ | ___/___/___ |

---

## 4.2 Perencanaan Proyek

### 4.2.1 Ruang Lingkup Proyek (Scope Management)

Ruang lingkup proyek didefinisikan menggunakan **Work Breakdown Structure (WBS)** yang memecah deliverables menjadi work packages yang dapat dimanage.

**WBS Level 1 - Major Deliverables:**

```
1.0 Sistem Informasi CUR-HEART
│
├── 1.1 Project Management
│   ├── 1.1.1 Project Planning
│   ├── 1.1.2 Progress Monitoring
│   ├── 1.1.3 Risk Management
│   └── 1.1.4 Stakeholder Communication
│
├── 1.2 Requirements Analysis
│   ├── 1.2.1 Stakeholder Interviews
│   ├── 1.2.2 Business Process Analysis
│   ├── 1.2.3 Requirements Documentation
│   └── 1.2.4 Requirements Validation
│
├── 1.3 System Design
│   ├── 1.3.1 Architecture Design
│   ├── 1.3.2 Database Design
│   ├── 1.3.3 UI/UX Design
│   └── 1.3.4 Security Design
│
├── 1.4 Development
│   ├── 1.4.1 Environment Setup
│   ├── 1.4.2 Backend Development
│   ├── 1.4.3 Frontend Development
│   ├── 1.4.4 Integration
│   └── 1.4.5 Code Review
│
├── 1.5 Testing
│   ├── 1.5.1 Unit Testing
│   ├── 1.5.2 Integration Testing
│   ├── 1.5.3 Functional Testing
│   ├── 1.5.4 Usability Testing
│   └── 1.5.5 UAT
│
├── 1.6 Deployment
│   ├── 1.6.1 Production Setup
│   ├── 1.6.2 Data Migration
│   ├── 1.6.3 Go-Live
│   └── 1.6.4 Post-Deployment Support
│
└── 1.7 Documentation
    ├── 1.7.1 Technical Documentation
    ├── 1.7.2 User Documentation
    ├── 1.7.3 Capstone Report
    └── 1.7.4 Presentation Materials
```

**Scope Baseline:**

Scope Statement yang approved pada tanggal 29 September 2024 mencakup:

1. **Product Scope:**
   - Web application dengan 41 halaman interface
   - Multi-role system (Admin, Therapist, Client)
   - Online booking system dengan real-time availability
   - Comprehensive dashboard untuk setiap role
   - Payment integration dengan multiple methods
   - Email notification system
   - Responsive design untuk mobile dan desktop

2. **Project Scope:**
   - Analysis, design, development, testing, dan deployment
   - Duration: 11 minggu
   - Team: 3 developers
   - Methodology: Waterfall SDLC

3. **Acceptance Criteria:**
   - Semua functional requirements dari MoSCoW "Must Have" terimplementasi
   - System lolos UAT dengan approval stakeholders
   - No critical bugs di production
   - Documentation lengkap dan approved
   - User training completed

### 4.2.2 Jadwal Proyek (Schedule Management)

**Project Schedule - Gantt Chart:**

| ID | Task Name | Duration | Start | End | Predecessors |
|----|-----------|----------|-------|-----|--------------|
| 1 | **Project Initiation** | 3 days | 16-Sep | 18-Sep | - |
| 1.1 | Kick-off meeting | 1 day | 16-Sep | 16-Sep | - |
| 1.2 | Stakeholder identification | 1 day | 17-Sep | 17-Sep | 1.1 |
| 1.3 | Project charter approval | 1 day | 18-Sep | 18-Sep | 1.2 |
| 2 | **Requirements Analysis** | 11 days | 19-Sep | 29-Sep | 1 |
| 2.1 | Stakeholder interviews | 5 days | 19-Sep | 23-Sep | 1.3 |
| 2.2 | Business process observation | 3 days | 19-Sep | 21-Sep | 1.3 |
| 2.3 | Document analysis | 2 days | 24-Sep | 25-Sep | 2.1,2.2 |
| 2.4 | Requirements documentation | 3 days | 26-Sep | 28-Sep | 2.3 |
| 2.5 | Requirements validation | 1 day | 29-Sep | 29-Sep | 2.4 |
| 3 | **System Design** | 14 days | 30-Sep | 13-Oct | 2 |
| 3.1 | Architecture design | 3 days | 30-Sep | 2-Oct | 2.5 |
| 3.2 | Database design | 4 days | 3-Oct | 6-Oct | 3.1 |
| 3.3 | UI/UX design | 5 days | 7-Oct | 11-Oct | 3.1 |
| 3.4 | Security design | 2 days | 12-Oct | 13-Oct | 3.2,3.3 |
| 3.5 | Design review | 1 day | 13-Oct | 13-Oct | 3.4 |
| 4 | **Development** | 28 days | 14-Oct | 10-Nov | 3 |
| 4.1 | Environment setup | 2 days | 14-Oct | 15-Oct | 3.5 |
| 4.2 | Database implementation | 3 days | 16-Oct | 18-Oct | 4.1 |
| 4.3 | Authentication system | 4 days | 19-Oct | 22-Oct | 4.2 |
| 4.4 | Backend development | 10 days | 23-Oct | 1-Nov | 4.3 |
| 4.5 | Frontend development | 12 days | 23-Oct | 3-Nov | 4.3 |
| 4.6 | Integration | 5 days | 4-Nov | 8-Nov | 4.4,4.5 |
| 4.7 | Code review | 2 days | 9-Nov | 10-Nov | 4.6 |
| 5 | **Testing** | 14 days | 11-Nov | 24-Nov | 4 |
| 5.1 | Unit testing | 3 days | 11-Nov | 13-Nov | 4.7 |
| 5.2 | Integration testing | 3 days | 14-Nov | 16-Nov | 5.1 |
| 5.3 | Functional testing | 4 days | 17-Nov | 20-Nov | 5.2 |
| 5.4 | Usability testing | 3 days | 21-Nov | 23-Nov | 5.3 |
| 5.5 | UAT | 2 days | 23-Nov | 24-Nov | 5.4 |
| 6 | **Deployment** | 7 days | 25-Nov | 1-Dec | 5 |
| 6.1 | Production environment setup | 2 days | 25-Nov | 26-Nov | 5.5 |
| 6.2 | Application deployment | 2 days | 27-Nov | 28-Nov | 6.1 |
| 6.3 | Go-live | 1 day | 29-Nov | 29-Nov | 6.2 |
| 6.4 | User training | 2 days | 30-Nov | 1-Dec | 6.3 |
| 7 | **Documentation** | 21 days | 11-Nov | 1-Dec | - |
| 7.1 | Technical documentation | 7 days | 11-Nov | 17-Nov | 5.1 |
| 7.2 | User documentation | 5 days | 18-Nov | 22-Nov | 7.1 |
| 7.3 | Capstone report writing | 14 days | 18-Nov | 1-Dec | 7.1 |
| 7.4 | Presentation preparation | 7 days | 25-Nov | 1-Dec | 7.3 |

**Critical Path:**

Initiation → Requirements → Design → Development (Backend & Frontend) → Integration → Testing → UAT → Deployment → Go-Live

Total Duration: **77 days (11 minggu)**

**Milestones:**

| Milestone | Date | Deliverable |
|-----------|------|-------------|
| M1: Project Approved | 18-Sep-2024 | Project Charter signed |
| M2: Requirements Complete | 29-Sep-2024 | SRS Document approved |
| M3: Design Complete | 13-Oct-2024 | Design Documents approved |
| M4: Development Complete | 10-Nov-2024 | Working application |
| M5: Testing Complete | 24-Nov-2024 | UAT passed, bugs fixed |
| M6: System Live | 29-Nov-2024 | Production deployment |
| M7: Project Complete | 1-Dec-2024 | All deliverables submitted |

### 4.2.3 Biaya Proyek (Cost Management)

**Budget Breakdown:**

| Category | Item | Cost (Rp) | Notes |
|----------|------|-----------|-------|
| **Infrastructure** | | **1.500.000** | |
| | Domain (.com, 1 tahun) | 150.000 | curheart.com |
| | VPS Hosting (3 bulan) | 900.000 | 2 CPU, 4GB RAM, 80GB SSD |
| | SSL Certificate | 0 | Let's Encrypt (free) |
| | Backup Storage | 150.000 | Google Drive Business |
| | CDN Service (optional) | 300.000 | Cloudflare Pro |
| **Development Tools** | | **800.000** | |
| | Code Editor (VS Code) | 0 | Free |
| | Design Tools (Figma Pro) | 200.000 | 1 month subscription |
| | Database Tools | 0 | Free (phpMyAdmin, MySQL Workbench) |
| | Version Control (GitHub) | 0 | Free tier |
| | Project Management Tool | 100.000 | Trello/Asana premium |
| | Communication Tools | 0 | Discord/Slack free |
| | Testing Tools | 500.000 | Browser testing, performance tools |
| **Third-Party Services** | | **1.200.000** | |
| | Payment Gateway Setup | 0 | No setup fee (Midtrans) |
| | Payment Gateway Transaction | 500.000 | Testing credit |
| | Email Service (SMTP) | 200.000 | SendGrid/Mailgun |
| | SMS Service (optional) | 300.000 | Twilio credits untuk testing |
| | Analytics Tools | 0 | Google Analytics (free) |
| | Monitoring Service | 200.000 | UptimeRobot, Sentry |
| **Documentation** | | **500.000** | |
| | Report Printing | 300.000 | Full color, hard cover |
| | X-Banner Printing | 200.000 | 60x160 cm |
| **Contingency (20%)** | | **1.000.000** | |
| | Reserve for unexpected costs | 1.000.000 | Buffer |
| **TOTAL** | | **5.000.000** | |

**Cost Performance Tracking:**

| Period | Planned Cost | Actual Cost | Variance | CPI |
|--------|--------------|-------------|----------|-----|
| Month 1 (Sep) | 1.500.000 | 1.450.000 | +50.000 | 1.03 |
| Month 2 (Oct) | 2.000.000 | 1.980.000 | +20.000 | 1.01 |
| Month 3 (Nov) | 1.500.000 | (ongoing) | - | - |

CPI (Cost Performance Index) = EV / AC
- CPI > 1.0 = Under budget (good)
- CPI = 1.0 = On budget
- CPI < 1.0 = Over budget (concern)

### 4.2.4 Kualitas Proyek (Quality Management)

**Quality Standards:**

1. **Code Quality Standards:**
   - Follow Laravel best practices dan coding standards (PSR-12)
   - Code documentation dengan PHPDoc
   - No critical atau high-severity bugs
   - Code review by peers before merge
   - Minimum 70% code coverage untuk critical functions

2. **Performance Standards:**
   - Page load time < 3 seconds (on average connection)
   - Time to First Byte (TTFB) < 600ms
   - Database query optimization (no N+1 problems)
   - Image optimization (max 500KB per image)
   - Lighthouse score ≥ 80 untuk Performance

3. **Security Standards:**
   - OWASP Top 10 vulnerabilities mitigated
   - Data encryption untuk sensitive information
   - Secure authentication dan authorization
   - Regular security audits
   - Compliance dengan UU Perlindungan Data Pribadi

4. **Usability Standards:**
   - System Usability Scale (SUS) score ≥ 80/100
   - Task success rate ≥ 90%
   - Error rate < 5% per task
   - Accessibility WCAG 2.1 Level AA (minimum)

5. **Documentation Standards:**
   - Complete technical documentation (architecture, database, APIs)
   - Comprehensive user manuals untuk setiap role
   - Code comments untuk complex logic
   - README files dengan setup instructions
   - Change log maintained

**Quality Assurance Activities:**

| Activity | Frequency | Responsibility | Tool/Method |
|----------|-----------|----------------|-------------|
| Code Review | Per pull request | Peer developer | GitHub PR review |
| Unit Testing | Continuous | Developer | PHPUnit |
| Integration Testing | Per integration | QA/Developer | Laravel Dusk, Postman |
| Performance Testing | Weekly | Developer | Lighthouse, GTmetrix |
| Security Audit | Bi-weekly | Security lead | OWASP ZAP, manual review |
| Usability Testing | Once (Week 10) | UX lead | User sessions |
| UAT | Once (Week 10) | Stakeholders | Acceptance criteria |

**Quality Metrics:**

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Defect Density | < 5 bugs per 1000 LOC | Bug tracking tool |
| Test Coverage | ≥ 70% for critical code | Code coverage tool |
| Performance Score | ≥ 80/100 (Lighthouse) | Lighthouse audit |
| Security Score | A rating | Security scanner |
| Usability Score | ≥ 80/100 (SUS) | User testing |
| Code Quality | Grade A | Code analysis tool |

### 4.2.5 Manajemen Sumber Daya (Resource Management)

**Tim Proyek:**

| Name | Role | Responsibilities | Allocation |
|------|------|------------------|------------|
| **Roki Anjas** | Project Manager & Backend Developer | Project planning, coordination, backend development (Models, Controllers), database design, API integration | 100% (Full-time) |
| **Susanto** | Frontend Developer & UI/UX Designer | UI/UX design, frontend development (Blade views, Tailwind CSS), responsive design, user testing | 100% (Full-time) |
| **Fahruroji** | Full-Stack Developer & Database Administrator | Full-stack development support, database implementation, testing, documentation | 100% (Full-time) |

**External Resources:**

| Resource | Role | Involvement |
|----------|------|-------------|
| Rani Irma Handayani, M.Kom | Dosen Pembimbing | Weekly consultation (2 hours/week), technical guidance, final evaluation |
| CUR-HEART Owner | Project Sponsor | Requirement approval, UAT, budget approval |
| CUR-HEART Terapis (5 orang) | Subject Matter Experts | Requirements input, usability testing, training |
| CUR-HEART Admin (2 orang) | System Operators | Process documentation, usability testing, training |
| Sample Clients (10 orang) | End Users | User research, usability testing, feedback |

**Resource Calendar:**

```
      September         October          November
Week: 1  2  3  4    5  6  7  8    9  10 11
────────────────────────────────────────────
Roki: ████████████████████████████████████
Susanto: ████████████████████████████████████
Fahruroji: ████████████████████████████████████
Dosen: █ █ █ █    █ █ █ █    █ █  █
Owner:  █       █        █        █    █
Terapis:     █              █         █
```

**Resource Leveling:**

Untuk menghindari resource overallocation, beberapa tasks dilakukan parallel:
- Backend dan Frontend development (Week 5-8)
- Testing dan Documentation (Week 9-11)
- Code dapat di-distribute berdasarkan module untuk parallel work

### 4.2.6 Manajemen Risiko (Risk Management)

**Risk Register:**

| ID | Risk | Probability | Impact | Risk Score | Mitigation Strategy | Contingency Plan |
|----|------|-------------|--------|------------|---------------------|------------------|
| R01 | Scope creep dari stakeholder requests | Medium (50%) | High (8) | 4.0 | Strict change control process, prioritize must-haves only | Defer nice-to-have features to post-launch |
| R02 | Technical complexity lebih tinggi dari estimasi | Medium (40%) | Medium (6) | 2.4 | Regular technical reviews, early prototyping | Request mentor assistance, extend timeline jika critical |
| R03 | Team member unavailability (sakit, personal issues) | Low (20%) | High (8) | 1.6 | Cross-training, knowledge sharing, documentation | Redistribute work, adjust timeline |
| R04 | Stakeholder tidak available untuk reviews/UAT | Low (30%) | Medium (5) | 1.5 | Flexible scheduling, asynchronous communication | Use recorded demos, email approvals |
| R05 | Payment gateway integration issues | Medium (40%) | Medium (6) | 2.4 | Early testing, backup payment providers | Use manual verification temporarily |
| R06 | Performance issues pada production | Low (30%) | High (7) | 2.1 | Load testing, optimization, caching | Upgrade hosting plan, implement CDN |
| R07 | Data security breach atau vulnerability | Low (10%) | Very High (10) | 1.0 | Security best practices, regular audits, penetration testing | Immediate patch, incident response plan, notify affected users |
| R08 | Timeline delay due to unforeseen challenges | Medium (40%) | High (7) | 2.8 | Weekly progress monitoring, buffer time, early issue identification | Reduce scope, request timeline extension |
| R09 | Budget overrun | Low (20%) | Medium (5) | 1.0 | Cost tracking, approval for expenses, use free alternatives | Use contingency fund, seek additional funding |
| R10 | Low user adoption post-launch | Medium (30%) | High (8) | 2.4 | User-centric design, training, change management | Additional training sessions, user support, incentives |

**Risk Score Calculation:** Probability (%) × Impact (1-10)

**Risk Response Strategies:**

1. **Avoid:** Eliminate risk (e.g., choose proven technology instead of experimental)
2. **Mitigate:** Reduce probability or impact (e.g., thorough testing to reduce bugs)
3. **Transfer:** Shift risk to third party (e.g., use managed hosting untuk infrastructure risks)
4. **Accept:** Accept risk jika low impact (e.g., minor UI inconsistencies)

**Risk Monitoring:**

Risks di-review setiap weekly meeting:
- Update risk probability dan impact
- Check effectiveness of mitigation strategies
- Identify new risks
- Document lessons learned

### 4.2.7 Manajemen Komunikasi (Communications Management)

**Stakeholder Communication Matrix:**

| Stakeholder | Information Needs | Method | Frequency | Responsible |
|-------------|------------------|--------|-----------|-------------|
| CUR-HEART Owner | Project status, budget, key decisions | Email report, meeting | Weekly | Project Manager |
| Dosen Pembimbing | Progress, technical challenges, deliverables | Consultation meeting, documentation | Weekly | Project Manager |
| Terapis | Feature updates, testing schedules, training | WhatsApp group, email | Bi-weekly | Project Manager |
| Admin Staff | Feature updates, testing schedules, training | WhatsApp group, email | Bi-weekly | Project Manager |
| Sample Clients | Testing invitations, feedback requests | Email, phone | As needed | UX Designer |
| Development Team | Task assignments, blockers, updates | Daily standup, Slack | Daily | Project Manager |

**Communication Tools:**

1. **Internal Team:**
   - Discord/Slack: Daily communication, quick questions
   - GitHub: Code reviews, issue tracking
   - Trello/Asana: Task management
   - Google Drive: Document sharing

2. **With Stakeholders:**
   - Email: Formal communication, reports
   - WhatsApp: Quick updates, coordination
   - Zoom/Google Meet: Remote meetings
   - Face-to-face: Important discussions, demos

**Meeting Schedule:**

| Meeting | Participants | Frequency | Duration | Purpose |
|---------|-------------|-----------|----------|---------|
| Daily Standup | Development Team | Daily | 15 min | Progress update, blockers |
| Weekly Status | PM, Dosen Pembimbing | Weekly | 60 min | Progress review, guidance |
| Stakeholder Review | PM, Owner, SMEs | Bi-weekly | 90 min | Demo, feedback, decisions |
| Sprint Planning | Development Team | Every 2 weeks | 120 min | Plan upcoming work |
| Retrospective | Development Team | Every 2 weeks | 60 min | Lessons learned, improvements |

**Reporting:**

1. **Weekly Status Report** (Email to Owner dan Dosen)
   - Accomplishments this week
   - Planned activities next week
   - Issues dan blockers
   - Budget status
   - Risks dan mitigation

2. **Monthly Progress Report** (Formal document)
   - Executive summary
   - Detailed progress by work package
   - Milestone achievements
   - Budget vs. actual
   - Updated schedule
   - Risk register
   - Photos/screenshots

### 4.2.8 Manajemen Pengadaan (Procurement Management - jika ada)

Untuk proyek ini, procurement minimal karena menggunakan mostly open-source tools dan free services. Namun, beberapa items yang di-procure:

| Item | Vendor | Contract Type | Amount | Status |
|------|--------|---------------|--------|--------|
| VPS Hosting | Niagahoster/IDCloudHost | Fixed Price | Rp 900.000 | Ordered |
| Domain Registration | Namecheap/Niagahoster | Fixed Price | Rp 150.000 | Ordered |
| Payment Gateway (Midtrans) | Midtrans | Pay-per-transaction | Variable | Integrated |
| Email Service | SendGrid | Pay-as-you-go | Rp 200.000 | Active |
| Backup Storage | Google Drive Business | Subscription | Rp 150.000 | Active |

Semua procurement follow standard process:
1. Requirements identification
2. Vendor research dan comparison
3. Budget approval
4. Order/signup
5. Configuration dan testing
6. Invoice processing

---

## 4.3 Deskripsi Produk / Servis

### 4.3.1 Gambaran Umum Sistem

Sistem Informasi Manajemen Booking dan Terapi CUR-HEART adalah aplikasi web full-stack berbasis Laravel yang dirancang khusus untuk mendukung operasional pusat layanan hypnotherapy dan kesehatan mental. Sistem ini mengintegrasikan seluruh proses bisnis mulai dari booking layanan, manajemen jadwal terapis, conduct sesi terapi, dokumentasi, hingga pelaporan dalam satu platform yang unified, secure, dan user-friendly.

**Karakteristik Utama Sistem:**

1. **Multi-Role Architecture:** Mendukung tiga role pengguna utama (Admin, Therapist, Client) dengan hak akses dan interface yang disesuaikan
2. **Real-Time Availability:** Menampilkan ketersediaan jadwal terapis secara real-time untuk booking
3. **Comprehensive Workflow:** Cover seluruh client journey dari awareness hingga post-therapy follow-up
4. **Data-Driven:** Menyediakan analytics dan reporting untuk business intelligence
5. **Secure dan Compliant:** Mengikuti security best practices dan compliance regulations
6. **Responsive Design:** Accessible dari desktop, tablet, dan smartphone dengan experience yang optimal
7. **Scalable Architecture:** Dapat accommodate pertumbuhan users dan data tanpa major refactoring

**Arsitektur Sistem:**

Sistem menggunakan **Monolithic Architecture** dengan **Model-View-Controller (MVC) Pattern**:

```
┌─────────────────────────────────────────────────────┐
│                  CLIENT LAYER                        │
│  (Web Browser - Desktop, Tablet, Mobile)            │
└────────────┬────────────────────────────────────────┘
             │ HTTPS Requests
             ├─────────────────────────────────────────┐
             │                                         │
┌────────────▼───────────────────────────────────┐   │
│            PRESENTATION LAYER                   │   │
│  ┌──────────────────────────────────────────┐  │   │
│  │    Blade Templates (Views)               │  │   │
│  │  - Public Pages                           │  │   │
│  │  - Authentication Pages                   │  │   │
│  │  - Dashboard (Admin, Therapist, Client)  │  │   │
│  │  - Components (Forms, Tables, Charts)    │  │   │
│  └──────────────────────────────────────────┘  │   │
│  ┌──────────────────────────────────────────┐  │   │
│  │    Tailwind CSS + JavaScript             │  │   │
│  └──────────────────────────────────────────┘  │   │
└────────────┬───────────────────────────────────┘   │
             │                                         │
┌────────────▼───────────────────────────────────┐   │
│           APPLICATION LAYER                     │   │
│  ┌──────────────────────────────────────────┐  │   │
│  │          Routes (web.php)                 │  │   │
│  └──────────────────────────────────────────┘  │   │
│  ┌──────────────────────────────────────────┐  │   │
│  │    Middleware                             │  │   │
│  │  - Authentication                         │  │   │
│  │  - Authorization (Role-based)            │  │   │
│  │  - CSRF Protection                        │  │   │
│  └──────────────────────────────────────────┘  │   │
│  ┌──────────────────────────────────────────┐  │   │
│  │        Controllers                        │  │   │
│  │  - AuthController                         │  │   │
│  │  - BookingController                      │  │   │
│  │  - TherapistController                    │  │   │
│  │  - SessionController                      │  │   │
│  │  - PaymentController                      │  │   │
│  │  - DashboardController                    │  │   │
│  │  - ReportController                       │  │   │
│  └──────────────────────────────────────────┘  │   │
└────────────┬───────────────────────────────────┘   │
             │                                         │
┌────────────▼───────────────────────────────────┐   │
│          BUSINESS LOGIC LAYER                   │   │
│  ┌──────────────────────────────────────────┐  │   │
│  │         Models (Eloquent ORM)            │  │   │
│  │  - User, Therapist, Client               │  │   │
│  │  - Service, Booking                       │  │   │
│  │  - Session, SessionNote                   │  │   │
│  │  - Payment, Transaction                   │  │   │
│  │  - Review, Progress                       │  │   │
│  └──────────────────────────────────────────┘  │   │
│  ┌──────────────────────────────────────────┐  │   │
│  │         Business Rules                    │  │   │
│  │  - Validation Rules                       │  │   │
│  │  - Business Logic                         │  │   │
│  │  - Relationships                          │  │   │
│  └──────────────────────────────────────────┘  │   │
└────────────┬───────────────────────────────────┘   │
             │                                         │
┌────────────▼───────────────────────────────────┐   │
│             DATA LAYER                          │   │
│  ┌──────────────────────────────────────────┐  │   │
│  │         MySQL Database                    │  │   │
│  │  - Tables (normalized to 3NF)            │  │   │
│  │  - Indexes for performance                │  │   │
│  │  - Foreign Keys for integrity             │  │   │
│  └──────────────────────────────────────────┘  │   │
└─────────────────────────────────────────────────┘   │
                                                       │
┌──────────────────────────────────────────────────┐ │
│          EXTERNAL SERVICES                        │ │
│  - Payment Gateway (Midtrans)                    │◄┘
│  - Email Service (SMTP)                          │
│  - SMS Service (optional)                        │
│  - Video Conference (Zoom/GMeet via iframe)     │
└──────────────────────────────────────────────────┘
```

### 4.3.2 Fitur-Fitur Utama Sistem

Sistem terdiri dari **41 halaman interface** yang dikelompokkan berdasarkan fungsi:

#### A. Public Pages (8 halaman)

**1. Landing Page (01_landing.html)**

Halaman utama yang menjadi first touchpoint untuk visitors. Dirancang untuk conversion optimization dengan elemen:

- **Hero Section:** 
  - Headline yang powerful: "Transformasi Diri Dimulai Dari Sini"
  - Subheadline yang menjelaskan value proposition
  - Primary CTA button: "Booking Sekarang"
  - Hero image/illustration yang calming dan relatable
  
- **Services Overview:**
  - Grid layout menampilkan 6 layanan utama dengan icon dan deskripsi singkat
  - Hover effect untuk interactivity
  - Link ke detail masing-masing layanan
  
- **Why Choose Us Section:**
  - USPs (Unique Selling Points): Terapis bersertifikat, metode scientific, lingkungan rahasia
  - Statistics: "500+ Klien Terbantu", "95% Success Rate", "4.8★ Average Rating"
  
- **How It Works:**
  - 4-step process illustration: Pilih Layanan → Pilih Terapis → Jadwalkan → Terapi
  - Visual icons untuk each step
  
- **Testimonials:**
  - Carousel menampilkan 5-6 testimonials dari klien dengan foto, nama, dan quote
  - Star ratings visible
  
- **Latest Articles (Blog Preview):**
  - 3 artikel terbaru dengan thumbnail, title, excerpt, dan "Read More" link
  
- **CTA Section:**
  - Encouraging message dengan button ke registration/booking
  
- **Footer:**
  - Quick links (About, Services, Therapists, Blog, Contact, FAQ)
  - Social media icons
  - Copyright information
  - Privacy Policy dan Terms & Conditions links

**2. About Page (02_about.html)**

Halaman "Tentang Kami" yang membangun trust dan credibility:

- **Company Story:** Narrative tentang founding CUR-HEART, visi, misi
- **Our Approach:** Penjelasan tentang pendekatan hypnotherapy yang digunakan
- **Certifications:** Display sertifikat dan akreditasi
- **Team Section:** Photos dan bios dari founders/key management
- **Values:** Core values perusahaan (Professional, Empathetic, Scientific, Confidential)
- **Achievements:** Milestones dan recognition yang diterima

**3. Services Page (03_services.html)**

Katalog lengkap semua layanan dengan filtering:

- **Services Grid:** Card layout untuk 6 layanan, setiap card berisi:
  - Icon/illustration representatif
  - Service name
  - Short description (2-3 kalimat)
  - Duration dan price range
  - "Learn More" button → link ke service detail page
  
- **Filter/Sort Options:**
  - Filter by category (Stress Management, Personal Growth, Habit Change)
  - Sort by popularity, price, duration
  
- **FAQ Section:** Common questions tentang layanan

**4. Service Detail Page (04_services_detail.html)**

Halaman detail untuk setiap layanan individual:

- **Service Header:** Name, icon, breadcrumb navigation
- **Detailed Description:** Comprehensive explanation tentang layanan
- **What to Expect:** Outline tentang what happens during session
- **Benefits:** Bullet list benefits yang bisa didapatkan
- **Ideal For:** Target audience/kondisi yang suitable
- **Duration & Pricing:** Clear information
- **Success Stories:** Testimonials specific untuk layanan ini
- **Available Therapists:** List terapis yang menyediakan layanan ini dengan photos, names, specializations
- **CTA Button:** "Book This Service" → redirect ke booking flow

**5. Therapists Directory (05_therapists.html)**

Directory semua terapis dengan filtering dan search:

- **Therapists Grid:** Card layout, setiap card menampilkan:
  - Professional photo
  - Name dan credentials (M.Psi., C.Ht.)
  - Specializations (tags: Anxiety, Trauma, Motivation)
  - Years of experience
  - Rating (e.g., 4.9★ from 120 reviews)
  - "View Profile" button
  
- **Filter Options:**
  - By specialization
  - By rating
  - By availability
  - By years of experience
  
- **Search Bar:** Search by name
- **Sort Options:** Name A-Z, Rating, Experience

**6. Therapist Profile Page (06_therapist_profile.html)**

Profile detail page untuk individual terapis:

- **Profile Header:**
  - Large professional photo
  - Name, credentials, title
  - Rating dan total reviews
  - Years of experience
  - Specializations (badges/tags)
  - "Book with This Therapist" button
  
- **About Section:** Bio paragraph tentang background, philosophy, approach
- **Education:** List pendidikan formal dengan institutions dan years
- **Certifications:** Professional certifications dengan issuing bodies
- **Services Offered:** Layanan-layanan yang dikuasai
- **Availability Calendar:** Mini calendar showing available dates (next 2 weeks preview)
- **Reviews Section:**
  - Overall rating breakdown (5★: 80%, 4★: 15%, etc.)
  - Individual reviews dengan client name (anonymized if preferred), date, rating, comment
  - Pagination untuk multiple reviews
  
- **Related Therapists:** "You may also like" section dengan 3 terapis similar

**7. Blog List Page (07_blog_list.html)**

Archive page untuk semua artikel blog/educational content:

- **Featured Article:** Hero section dengan latest atau featured article
- **Articles Grid:** Card layout untuk articles, setiap card berisi:
  - Thumbnail image
  - Category tag (e.g., Mental Health, Self-Care, Success Stories)
  - Title
  - Excerpt (first 150 characters)
  - Author name dan publish date
  - "Read More" link
  
- **Sidebar:**
  - Search bar
  - Categories list
  - Popular articles
  - Tags cloud
  
- **Pagination:** Navigate through multiple pages of articles

**8. Blog Detail Page (08_blog_detail.html)**

Individual article page:

- **Article Header:**
  - Title (H1)
  - Author info dengan photo
  - Publish date dan reading time estimate
  - Category dan tags
  - Share buttons (social media)
  
- **Article Content:**
  - Rich text content dengan images, headings, lists, quotes
  - Proper typography dan spacing untuk readability
  - Table of contents untuk long articles (sticky sidebar)
  
- **Engagement:**
  - Like/helpful button
  - Comment section (optional)
  
- **Related Articles:** 3-4 related articles at bottom
- **CTA:** "Ready to start your journey? Book a session now"

#### B. Support Pages (4 halaman)

**9. Contact Page (09_contact.html)**

- **Contact Form:** Name, email, phone, subject, message fields
- **Contact Information:** Address, phone numbers, email, business hours
- **Google Maps Embed:** Interactive map showing location
- **Social Media Links**
- **FAQ Link:** Redirect to FAQ page for common questions

**10. FAQ Page (10_faq.html)**

- **Search Bar:** Search through FAQs
- **Categories:** General, Booking, Services, Payment, Privacy
- **Accordion Layout:** Click to expand answers
- **Contact Prompt:** "Didn't find your answer? Contact us"

**11. Privacy Policy Page (11_privacy_policy.html)**

- **Legal Document:** Comprehensive privacy policy
- **Sections:** Data collection, usage, protection, rights, cookies
- **Last Updated Date**
- **Compliance Statement:** UU No. 27 Tahun 2022 tentang PDP

**12. Terms & Conditions Page (12_terms_conditions.html)**

- **Legal Document:** Terms of service
- **Sections:** User obligations, service usage, cancellation policy, liability, disputes
- **Acceptance Checkbox:** Required during registration

#### C. Authentication Pages (4 halaman)

**13. Login Page (13_login.html)**

- **Login Form:**
  - Email field
  - Password field dengan show/hide toggle
  - "Remember Me" checkbox
  - "Forgot Password?" link
  - "Login" button (primary CTA)
  
- **Social Login (optional):** Google, Facebook login buttons
- **Registration Link:** "Don't have an account? Sign Up"
- **Branding:** Logo, tagline
- **Illustration/Image:** Calming visual di side (split-screen layout)

**14. Register Page (14_register.html)**

- **Registration Form:**
  - Full Name
  - Email Address
  - Phone Number
  - Password (dengan strength indicator)
  - Confirm Password
  - Terms & Conditions acceptance checkbox
  
- **User Type Selection:**
  - Radio buttons atau tabs: "Client" atau "Therapist"
  - Different forms untuk each type (therapists need additional info: credentials, specializations)
  
- **"Create Account" Button**
- **Login Link:** "Already have an account? Login"
- **Email Verification Notice:** "We'll send verification email"

**15. Forgot Password Page (15_forgot_password.html)**

- **Instruction Text:** "Enter your email to receive reset link"
- **Email Input Field**
- **"Send Reset Link" Button**
- **Back to Login Link**
- **Success Message:** "Reset link sent! Check your email"

**16. Reset Password Page (16_reset_password.html)**

- **Token Validation:** System checks if reset token valid dan not expired
- **New Password Form:**
  - New Password field dengan strength indicator
  - Confirm New Password field
  
- **"Reset Password" Button**
- **Success Redirect:** After successful reset, redirect ke login dengan success message

#### D. Client Dashboard (10 halaman)

**17. Client Dashboard Main (17_client_dashboard.html)**

Overview dashboard untuk klien setelah login:

- **Welcome Header:** "Welcome back, [Client Name]!"
- **Summary Cards:**
  - Upcoming Appointments (count dengan next appointment details)
  - Completed Sessions (total count)
  - Progress Score (percentage atau score)
  - Pending Payments (if any)
  
- **Upcoming Appointments Widget:**
  - List 2-3 upcoming appointments dengan:
    - Date dan time
    - Service name
    - Therapist name dan photo
    - "View Details" atau "Join Session" button (if online)
  - "View All" link → redirects to appointments page
  
- **Quick Actions:**
  - Large buttons: "Book New Session", "View My Progress", "Contact Therapist"
  
- **Recent Activities Timeline:**
  - Last session completed
  - Payment confirmed
  - Appointment rescheduled
  - etc.
  
- **Announcements/News:**
  - System announcements
  - Tips of the day
  - Upcoming events atau workshops
  
- **Motivational Quote:** Random mental health quote atau affirmation

**18. Booking Step 1 - Select Service (18_booking_step1.html)**

Tahap 1 dari 4-step booking flow:

- **Progress Indicator:** Visual stepper showing "Step 1 of 4"
- **Page Title:** "Choose Your Service"
- **Services Grid:** Similar to services catalog, tapi dengan selection mechanism:
  - Radio buttons atau clickable cards
  - Highlight selected service
  
- **Service Preview:** When service selected, show:
  - Full description
  - Duration
  - Price
  
- **Navigation:**
  - "Next" button (enabled only when service selected) → go to Step 2
  - "Cancel" button → back to dashboard

**19. Booking Step 2 - Select Therapist (19_booking_step2.html)**

- **Progress Indicator:** "Step 2 of 4"
- **Page Title:** "Choose Your Therapist"
- **Filter:** Show only therapists yang provide selected service
- **Therapists Grid:** Similar to directory, dengan selection:
  - Radio buttons atau clickable cards
  - Show availability indicator (e.g., "Available this week")
  
- **Therapist Preview:** When selected, show:
  - Profile summary
  - Specializations
  - Rating
  - "View Full Profile" link (opens modal atau new tab)
  
- **Navigation:**
  - "Back" button → return to Step 1
  - "Next" button → go to Step 3

**20. Booking Step 3 - Select Date & Time (20_booking_step3.html)**

- **Progress Indicator:** "Step 3 of 4"
- **Page Title:** "Choose Date & Time"
- **Calendar Widget:** Interactive calendar showing:
  - Available dates (clickable)
  - Unavailable dates (grayed out)
  - Current month dengan prev/next navigation
  
- **Time Slots:** When date selected, show available time slots:
  - Grid of buttons: "09:00 AM", "10:30 AM", "01:00 PM", etc.
  - Disabled/grayed out untuk slots already booked
  - Highlight selected slot
  
- **Duration Display:** "Session duration: 60 minutes"
- **Selected Summary:** Box showing:
  - Service: [Name]
  - Therapist: [Name]
  - Date: [Selected Date]
  - Time: [Selected Time]
  
- **Navigation:**
  - "Back" button → Step 2
  - "Next" button → Step 4

**21. Booking Step 4 - Confirmation & Payment (21_booking_step4.html)**

- **Progress Indicator:** "Step 4 of 4"
- **Page Title:** "Confirm & Pay"
- **Booking Summary:** Complete recap:
  - Service name, description, duration
  - Therapist name, photo
  - Date and time
  - Location (if physical) atau "Online Session"
  - Subtotal
  - Tax (if applicable)
  - Total amount
  
- **Client Information:** Pre-filled dengan logged-in user data:
  - Name
  - Email
  - Phone
  - Special notes/requests (textarea - optional)
  
- **Payment Method Selection:**
  - Radio buttons:
    - Credit/Debit Card (via payment gateway)
    - Bank Transfer (manual)
    - E-Wallet (GoPay, OVO, Dana)
    - QRIS
  
- **Terms Agreement:** Checkbox untuk agree dengan cancellation policy
- **Navigation:**
  - "Back" button → Step 3
  - "Confirm & Pay" button (primary CTA) → process payment

**22. Booking Success Page (22_booking_success.html)**

Confirmation page after successful booking:

- **Success Icon:** Large checkmark atau success animation
- **Success Message:** "Booking Confirmed!"
- **Booking Details:**
  - Booking reference number
  - Service, Therapist, Date, Time
  - Payment status
  
- **Next Steps:**
  - "You'll receive confirmation email at [email]"
  - "Reminder will be sent 1 day before session"
  - If online: "Link to join will be sent via email"
  
- **Actions:**
  - "View My Appointments" button → go to appointments page
  - "Book Another Session" button → restart booking flow
  - "Download Confirmation" button → generate PDF

**23. Client Appointments List (23_client_appointments.html)**

List view semua appointments klien:

- **View Toggles:** Tabs atau buttons to switch:
  - List View (default)
  - Calendar View
  
- **Filter Options:**
  - Status: All, Upcoming, Completed, Cancelled
  - Date range picker
  
- **Appointments List:** Table atau card layout, setiap row/card shows:
  - Date & Time
  - Service name
  - Therapist name dan photo
  - Status badge (Upcoming: blue, Completed: green, Cancelled: red)
  - Actions dropdown:
    - View Details
    - Reschedule (if upcoming)
    - Cancel (if upcoming dan within policy)
    - Join Session (if online dan time to join)
    - Download Receipt
  
- **Pagination:** Navigate through pages if many appointments
- **Empty State:** If no appointments, show encouraging message dan "Book Your First Session" button

**24. Appointment Detail Page (24_appointment_detail.html)**

Detail page untuk individual appointment:

- **Breadcrumb:** Dashboard > Appointments > [Booking ID]
- **Appointment Header:**
  - Status badge
  - Booking reference number
  - Date created
  
- **Details Section:**
  - **Service Information:**
    - Service name dan description
    - Duration
    - Price
  
  - **Therapist Information:**
    - Photo, name, credentials
    - Specializations
    - Contact button (opens messaging)
  
  - **Schedule:**
    - Date dan time
    - Location atau online link (if session time)
  
  - **Client Notes:** Any special requests submitted
  - **Therapist Notes:** (visible after session) Summary dari terapis
  
- **Payment Information:**
  - Amount
  - Payment method
  - Payment status
  - Transaction ID
  - Invoice download button
  
- **Actions:**
  - If upcoming:
    - "Reschedule" button
    - "Cancel Appointment" button (dengan confirmation modal)
    - "Add to Calendar" button (download .ics file)
  - If online dan time to join:
    - "Join Session" button (large, prominent)
  - If completed:
    - "Leave Review" button
    - "Book Again dengan Therapist yang Sama" button

**25. Client Progress Tracking (25_client_progress.html)**

Visualisasi progress terapi klien:

- **Progress Overview Cards:**
  - Total Sessions Completed
  - Current Streak (consecutive weeks/months)
  - Overall Progress Score (algorithm-based)
  - Improvement Percentage
  
- **Self-Assessment History:**
  - Line chart showing scores over time
  - Multiple series untuk different metrics (e.g., Anxiety Level, Confidence Level, Sleep Quality)
  - Interactive: hover untuk see exact values
  - Date range selector
  
- **Progress Notes dari Terapis:**
  - Timeline view showing notes setiap after session
  - Expand/collapse untuk read full notes
  
- **Goals Tracking:**
  - List personal goals yang diset dengan terapis
  - Progress bar untuk each goal
  - Completion status
  
- **Milestones:**
  - Achievement badges (e.g., "First Session", "10 Sessions", "3 Months Consistent")
  - Gamification elements untuk motivation
  
- **Download Report:** Button to download comprehensive progress report dalam PDF

**26. Client Messages/Inbox (26_client_messages.html)**

Communication hub untuk communicate dengan terapis atau admin:

- **Inbox Layout:**
  - Left sidebar: List conversations dengan:
    - Contact photo dan name
    - Last message preview
    - Timestamp
    - Unread indicator (badge dengan count)
  
  - Right pane: Selected conversation:
    - Message thread (chronological)
    - Each message shows sender, timestamp, content
    - Support attachments (view images, download documents)
    
- **Compose Message:**
  - Rich text editor
  - Attachment button
  - "Send" button
  
- **Filter/Search:**
  - Search messages by keyword
  - Filter by sender (Therapist, Admin)
  
- **Notifications:** Real-time notifications untuk new messages
- **Archive:** Option to archive old conversations

#### E. Therapist Dashboard (10 halaman)

**27. Therapist Dashboard Main (27_therapist_dashboard.html)**

Overview dashboard untuk terapis setelah login:

- **Welcome Header:** "Welcome, Dr. [Name]"
- **Today's Schedule Widget:**
  - Timeline view of today's appointments
  - Each appointment shows:
    - Time
    - Client name (clickable → view client profile)
    - Service type
    - Status (Upcoming, In Progress, Completed)
    - Quick action: "Start Session", "View Details"
  
- **Summary Statistics Cards:**
  - Today's Sessions (count)
  - Total Clients (all-time)
  - This Month's Earnings (Rp amount)
  - Average Rating (★ 4.8 dari 5)
  
- **Quick Actions:**
  - "Manage My Schedule"
  - "View All Clients"
  - "Check Messages"
  
- **Notifications Panel:**
  - New booking requests (if approval workflow enabled)
  - Rescheduling requests dari clients
  - Payment confirmations
  - System announcements
  
- **Performance Metrics:**
  - Chart showing sessions over time (line chart - last 30 days)
  - Session completion rate (%)
  - No-show rate (%)
  
- **Upcoming Appointments (Next 7 Days):**
  - List view dengan date, time, client, service
  - "View Full Schedule" link

**28. Therapist Schedule Management (28_therapist_schedule.html)**

Calendar management untuk terapis:

- **Calendar Views:**
  - Tabs to switch: Day, Week, Month
  - Large calendar grid showing all appointments
  
- **Appointment Display dalam Calendar:**
  - Colored blocks representing appointments
  - Color-coded by service type atau status
  - Show time, client name (truncated if long)
  - Click appointment → modal dengan details dan actions
  
- **Legend:** Explain color codes
- **Actions:**
  - Add manual block (for walk-in atau phone bookings) - admin only
  - View/Edit/Cancel appointments
  
- **Integration:**
  - "Export to Google Calendar" button
  - "Download as PDF" untuk print

**29. Therapist Availability Settings (29_therapist_availability.html)**

Interface untuk set working hours dan availability:

- **Regular Schedule:**
  - Weekly grid (Monday - Sunday)
  - For each day:
    - Toggle: Available / Unavailable
    - If available: Time slots (start time - end time)
    - Add multiple time slots per day (e.g., 09:00-12:00 dan 14:00-17:00)
    - "Copy to All Days" option untuk consistency
  
- **Break Time Settings:**
  - Default break duration between sessions (e.g., 15 minutes)
  - Lunch break time
  
- **Blocked Dates (Cuti/Off Days):**
  - Calendar widget untuk select dates
  - List blocked dates dengan delete option
  - Reason field (optional - for personal tracking)
  
- **Advance Booking Window:**
  - Setting: "Clients can book up to X days in advance"
  - Setting: "Require minimum X days notice for booking"
  
- **Maximum Sessions per Day:**
  - Number input untuk prevent overwork
  
- **Override Availability:**
  - Option untuk temporarily override untuk specific dates (special hours)
  
- **Save Changes Button:** Commit changes, refresh availability dalam booking system

**30. Therapist Clients List (30_therapist_clients.html)**

Manage dan view list semua klien yang pernah ditangani:

- **Clients Table:**
  - Columns:
    - Client Photo & Name
    - Last Session Date
    - Total Sessions (count)
    - Status (Active, Inactive, Completed)
    - Progress Indicator (visual gauge atau percentage)
    - Actions (View Profile, Send Message)
  
- **Search & Filter:**
  - Search by name atau email
  - Filter by status
  - Sort by name, last session, total sessions
  
- **Pagination**
- **Click Row:** Go to client profile detail page

**31. Client Profile View (Therapist Side) (31_client_profile_view.html)**

Detailed view client profile dari perspektif terapis:

- **Client Information:**
  - Photo, name, age, gender, contact info
  - Initial consultation date
  - Total sessions completed
  - Current status (Active/Inactive)
  
- **Session History dengan Client:**
  - Table listing all sessions:
    - Date, Service, Duration, Status
    - Link to view session notes
  
- **Progress Summary:**
  - Chart showing progress metrics over time
  - Goals dan achievements
  
- **Notes & Observations:**
  - Private notes hanya visible untuk terapis
  - Add new note button
  - Chronological list previous notes
  
- **Flags/Tags:**
  - Mark client dengan flags (e.g., "Requires Follow-up", "High Priority")
  
- **Actions:**
  - "Send Message" button
  - "Schedule Session" button (shortcut untuk book dengan client ini)
  - "Generate Progress Report" button (PDF export)

**32. Session Room (32_session_room.html)**

Virtual room untuk conduct session (primarily untuk online sessions):

- **Video Conference Area:**
  - Embedded iframe dari Zoom/Google Meet/Whereby
  - Full-screen toggle
  - Mute/Unmute, Camera On/Off controls
  
- **Session Information Panel:**
  - Client name
  - Service type
  - Session start time
  - Timer showing elapsed time
  - "End Session" button (prominent, red)
  
- **Quick Access:**
  - Button to view client profile dalam modal (non-intrusive)
  - Button to view previous session notes dalam modal
  
- **Note-Taking Pad:**
  - Collapsible side panel atau bottom drawer
  - Real-time note editor (autosave every minute)
  - Quick template insertion (untuk common observations)
  
- **Session Timer Alert:**
  - Alert notification 5 minutes before scheduled end time
  
- **Post-Session:**
  - Clicking "End Session" → prompt to save notes dan mark session completed
  - Redirect to session notes page untuk finalize documentation

**33. Session Notes Editor (33_session_notes.html)**

Structured editor untuk document session:

- **Session Header:**
  - Client name
  - Date dan time
  - Service type
  
- **Note Template Fields:** (customizable berdasarkan service type)
  - **Client Condition:** Dropdown atau radio (Calm, Anxious, Distressed, etc.) + textarea untuk details
  - **Issues Discussed:** Textarea
  - **Techniques Used:** Checkboxes (e.g., Progressive Relaxation, Visualization, Cognitive Restructuring) + textarea
  - **Client Response:** Textarea
  - **Progress Assessment:** Rating scale (1-10) + comments
  - **Goals for Next Session:** Textarea
  - **Therapist Observations:** Textarea (private)
  - **Recommendations:** Textarea (can be shared dengan client)
  
- **Attachments:**
  - Upload files atau images if needed
  
- **Save Options:**
  - "Save Draft" (not finalized)
  - "Save & Finalize" (mark session complete)
  
- **Sharing Options:**
  - Toggle: "Share observation dengan client" (controls visibility)
  
- **Rich Text Formatting:** Bold, italic, bullet lists, etc.
- **Auto-Save:** Draft auto-saved every 2 minutes
- **Navigate:** "Back to Session History" link

**34. Therapist Session History (34_therapist_session_history.html)**

Archive all sessions conducted:

- **Filters:**
  - Date range
  - Client (dropdown)
  - Service type (dropdown)
  - Status (Completed, No-show, Cancelled)
  
- **Sessions Table:**
  - Columns:
    - Date & Time
    - Client Name
    - Service Type
    - Duration
    - Status
    - Actions (View Notes, Edit Notes)
  
- **Search:** By client name atau session ID
- **Export:** Download filtered results as CSV atau PDF report
- **Pagination**
- **Summary Stats:** Total sessions dalam filtered view, total hours

**35. Therapist Earnings Dashboard (35_therapist_earnings.html)**

Financial tracking untuk terapis:

- **Earnings Summary Cards:**
  - Today's Earnings
  - This Week's Earnings
  - This Month's Earnings
  - Total Earnings (all-time)
  
- **Earnings Chart:**
  - Line atau bar chart showing earnings over time
  - Granularity options: Daily, Weekly, Monthly, Yearly
  - Date range selector
  
- **Breakdown by Service:**
  - Pie atau donut chart
  - Shows revenue contribution dari each service type
  - Table dengan service name, sessions count, total revenue
  
- **Breakdown by Month:**
  - Table showing each month's earnings, sessions, average per session
  
- **Pending Payments:**
  - List sessions yang belum paid (if applicable)
  - Follow-up actions
  
- **Commission Structure Display:**
  - If applicable, show commission rate atau payment scheme
  
- **Download Reports:**
  - Generate PDF atau Excel report untuk accounting atau tax purposes
  - Custom date range selector
  
- **Payment History:**
  - Link to detailed transaction history (if paid by CUR-HEART)

**36. Therapist Profile Settings (36_therapist_profile_edit.html)**

Edit own profile information:

- **Profile Photo:**
  - Current photo display
  - Upload new photo button (with crop functionality)
  
- **Personal Information:**
  - Full Name
  - Email
  - Phone Number
  - Date of Birth
  
- **Professional Information:**
  - Title/Credentials (e.g., M.Psi., C.Ht.)
  - Years of Experience
  - Specializations (multi-select tags)
  - Bio/About (rich textarea)
  
- **Education:**
  - Add/Edit/Delete education entries
  - Fields: Institution, Degree, Field of Study, Year
  
- **Certifications:**
  - Add/Edit/Delete certification entries
  - Fields: Certification Name, Issuing Organization, Year, Expiry (if applicable)
  - Upload certificate images
  
- **Services Offered:**
  - Checkboxes untuk select which services terapis can provide
  
- **Privacy Settings:**
  - Public profile visibility toggle
  - Display email/phone to clients toggle
  
- **Account Settings:**
  - Change password
  - Notification preferences (email, SMS)
  
- **"Save Changes" Button**
- **"Cancel" Button** (discard changes)

#### F. Admin Dashboard (5 halaman)

**37. Admin Dashboard Main (37_admin_dashboard.html)**

Central command center untuk admin/owner:

- **Key Performance Indicators (KPIs):**
  - Today's Revenue (Rp amount)
  - Total Users (count dengan breakdown: X clients, Y therapists)
  - Active Bookings (current open bookings count)
  - Pending Issues (approvals, verifications, complaints count)
  
- **Real-Time Activity Feed:**
  - New registrations
  - New bookings
  - Payments received
  - Sessions completed
  - Timestamps dan user names
  
- **Revenue Chart:**
  - Line chart showing daily revenue over last 30 days
  - Comparison dengan previous period (percentage change)
  
- **Bookings Overview:**
  - Bar chart showing bookings by status (Upcoming, Completed, Cancelled)
  - Monthly comparison
  
- **Services Popularity:**
  - Horizontal bar chart showing number of bookings per service
  - Helps identify most/least popular services
  
- **Therapist Performance:**
  - Table listing therapists dengan:
    - Name
    - Total Sessions This Month
    - Revenue Generated
    - Average Rating
  - Sort options
  
- **System Health:**
  - Server status (Online/Offline)
  - Database size
  - Last backup timestamp
  - Warnings atau alerts (e.g., low disk space, failed cron jobs)
  
- **Quick Actions:**
  - "Add New User"
  - "Create Manual Booking"
  - "Generate Report"
  - "System Settings"

**38. Admin Users Management (38_admin_users.html)**

CRUD operations untuk all users:

- **Users Table:**
  - Columns:
    - ID
    - Photo & Name
    - Email
    - Role (Admin, Therapist, Client)
    - Status (Active, Inactive, Suspended)
    - Registration Date
    - Last Login
    - Actions (View, Edit, Delete/Suspend)
  
- **Filters:**
  - By Role
  - By Status
  - By Registration Date Range
  
- **Search:** By name, email, atau ID
- **Sort:** By any column
- **Bulk Actions:**
  - Select multiple users
  - Bulk activate/deactivate
  - Bulk email
  
- **Add New User Button:**
  - Opens modal atau navigate to form
  - Fields: Name, Email, Phone, Role, Password (auto-generate option)
  - Send welcome email checkbox
  
- **Edit User:**
  - Modal atau separate page
  - Edit all user details
  - Change role
  - Reset password
  - Suspend/activate account
  
- **Delete User:**
  - Confirmation modal with warning
  - Soft delete (mark as deleted but retain data) vs. hard delete
  
- **Export Users:**
  - Download user list as CSV atau Excel

**Therapists Sub-Management:**

- **Pending Approvals:**
  - List new therapist registrations waiting approval
  - View submitted documents (credentials, certificates)
  - Actions: Approve, Reject (with reason), Request More Info
  
- **Verify Documents:**
  - Image viewer untuk uploaded certificates
  - Validation checklist
  - Approval workflow
  
- **Assign Services:**
  - Which services terapis approved untuk provide
  
- **Set Commission:**
  - Commission rate atau fixed fee per session
  - Different rates untuk different services

**39. Admin Bookings Management (39_admin_bookings.html)**

Manage all bookings system-wide:

- **Bookings Table:**
  - Columns:
    - Booking ID
    - Date & Time
    - Client Name
    - Therapist Name
    - Service
    - Status (Pending, Confirmed, Completed, Cancelled)
    - Payment Status (Paid, Pending, Refunded)
    - Actions (View, Edit, Cancel, Resched

ule)
  
- **Filters:**
  - By Status
  - By Payment Status
  - By Date Range
  - By Therapist
  - By Service
  
- **Search:** By booking ID, client name, atau therapist name
- **Calendar View Toggle:** Switch to calendar view showing all bookings
- **Conflict Detection:** Highlight double bookings atau scheduling conflicts (red flags)
- **Create Manual Booking:**
  - Button to create booking on behalf of client (walk-in atau phone bookings)
  - Wizard similar to client booking flow
  - Option to mark as paid immediately
  
- **Edit Booking:**
  - Change date/time
  - Change therapist
  - Update status
  - Add admin notes
  
- **Cancel Booking:**
  - Reason dropdown
  - Refund processing (if applicable)
  - Automatic notification to client dan therapist
  
- **Bulk Actions:**
  - Export bookings data
  - Bulk cancel (e.g., if therapist unavailable for entire day)
  
- **Statistics Panel:**
  - Total bookings selected period
  - Conversion rate (inquiries to confirmed bookings)
  - Cancellation rate
  - No-show rate

**40. Admin Financial Reports (40_admin_financial.html)**

Comprehensive financial reporting dan analytics:

- **Revenue Dashboard:**
  - **Total Revenue Cards:**
    - Today
    - This Week
    - This Month
    - This Year
  
  - **Revenue Trend Chart:**
    - Line chart over customizable period
    - Options: Daily, Weekly, Monthly, Yearly
    - Compare dengan previous period (overlay atau dual-axis)
  
  - **Revenue by Service:**
    - Pie atau bar chart
    - Shows which services generating most revenue
    - Table dengan detailed breakdown: Service name, total bookings, total revenue, average price
  
  - **Revenue by Therapist:**
    - Bar chart ranking therapists
    - Table: Therapist name, sessions, revenue, commission paid, net untuk business
  
- **Payments Tracking:**
  - **Payment Status Overview:**
    - Paid (green): count & amount
    - Pending (yellow): count & amount
    - Failed (red): count & amount
    - Refunded (gray): count & amount
  
  - **Outstanding Payments:**
    - Table list bookings dengan pending payments
    - Days overdue
    - Actions: Send reminder, mark as paid, cancel booking
  
  - **Manual Verification Queue:**
    - For bank transfer payments
    - Upload proof of payment images
    - Verify and approve
  
- **Refunds:**
  - List refund requests
  - Approval workflow
  - Refund processing
  
- **Expenses (Optional):**
  - Track operational expenses (rent, utilities, marketing)
  - Profit calculation (Revenue - Expenses)
  
- **Tax Reports:**
  - Calculate tax liabilities
  - Generate tax-ready reports untuk accountant
  
- **Financial Forecasting:**
  - Projected revenue based on trends
  - Seasonal analysis
  
- **Export Options:**
  - Download reports dalam PDF, Excel, CSV
  - Email reports to stakeholders
  - Schedule automated reports (daily/weekly/monthly)

**41. Admin System Settings (41_admin_settings.html)**

Configuration hub untuk system-wide settings:

- **General Settings:**
  - Site Name
  - Site Logo Upload
  - Tagline/Slogan
  - Contact Information (address, phone, email)
  - Business Hours
  - Timezone
  
- **Email Settings:**
  - SMTP Configuration:
    - SMTP Host
    - SMTP Port
    - SMTP Username
    - SMTP Password
    - Encryption (TLS/SSL)
  - Test Email Button (send test email to verify configuration)
  - Email Templates Management:
    - List templates (welcome, booking confirmation, reminder, etc.)
    - Edit template content (variables support: {{name}}, {{date}}, etc.)
  
- **SMS Settings (Optional):**
  - SMS Gateway Configuration
  - API Key
  - Sender ID
  - Test SMS Button
  
- **Payment Gateway Settings:**
  - Midtrans/Xendit Configuration:
    - API Keys (Server Key, Client Key)
    - Merchant ID
    - Test/Production Mode Toggle
  - Webhook URL display
  - Payment Methods Enabled (checkboxes: Credit Card, E-Wallet, Bank Transfer, QRIS)
  
- **Booking Settings:**
  - Advance Booking Days (how far in advance clients can book)
  - Minimum Notice Period (e.g., must book at least 2 days in advance)
  - Default Session Buffer Time (minutes between sessions)
  - Cancellation Policy:
    - Allow cancellation up to X hours before session
    - Refund percentage based on notice period
  - Auto-confirmation (or require admin approval)
  
- **Notification Settings:**
  - Enable/Disable Email Notifications (toggle untuk each type):
    - Welcome Email
    - Email Verification
    - Booking Confirmation
    - Booking Reminder (H-1)
    - Booking Reminder (H-0, 1 hour before)
    - Rescheduling Notification
    - Cancellation Notification
    - Payment Confirmation
    - Review Request
  - Enable/Disable SMS Notifications
  - Enable/Disable Push Notifications (for future mobile app)
  
- **Security Settings:**
  - Password Policy:
    - Minimum Length
    - Require Uppercase
    - Require Numbers
    - Require Special Characters
  - Session Timeout (minutes)
  - Two-Factor Authentication (2FA) Enforcement
  - Login Attempt Limit
  - IP Whitelist/Blacklist (optional, for admin access)
  
- **Backup Settings:**
  - Automatic Backup Schedule (daily, weekly, monthly)
  - Backup Storage Location (local, Google Drive, Dropbox)
  - Backup Retention Period (how long to keep backups)
  - Manual Backup Button (trigger immediate backup)
  - Restore dari Backup (upload and restore)
  
- **Maintenance Mode:**
  - Toggle Maintenance Mode (show "Under Maintenance" page to visitors)
  - Maintenance Message (customizable text)
  - Whitelist IPs (admin can still access during maintenance)
  
- **Analytics:**
  - Google Analytics Tracking ID
  - Facebook Pixel ID
  - Enable/Disable Tracking
  
- **Legal:**
  - Privacy Policy Editor (rich text)
  - Terms & Conditions Editor (rich text)
  - Cookie Policy Editor (rich text)
  - Last Updated Timestamps
  
- **Advanced Settings (Developer):**
  - Debug Mode (enable/disable error displaying)
  - Log Level (error, warning, info, debug)
  - Cache Settings (enable/disable, clear cache button)
  - Queue Settings
  
- **"Save Changes" Button:** Applies all settings (with confirmation)
- **"Reset to Default" Button:** Revert to default settings (with warning)

---

### 4.3.3 Database Design

Sistem menggunakan relational database (MySQL) dengan schema yang dinormalisasi hingga Third Normal Form (3NF) untuk mengurangi redundansi dan menjaga data integrity.

**Entity Relationship Diagram (ERD):**

```
┌─────────────┐
│    users    │
├─────────────┤
│ id (PK)     │
│ name        │
│ email (UQ)  │
│ password    │
│ role        │──────┬──────────────────────────────────┐
│ phone       │      │                                  │
│ status      │      │                                  │
│ created_at  │      │                                  │
│ updated_at  │      │                                  │
└─────────────┘      │                                  │
       │             │                                  │
       │ 1           │                                  │
       │             │                                  │
       │             │ 1                                │ 1
       │      ┌──────▼───────────┐             ┌───────▼────────┐
       │      │   therapists     │             │    clients     │
       │      ├──────────────────┤             ├────────────────┤
       │      │ id (PK)          │             │ id (PK)        │
       │      │ user_id (FK)     │             │ user_id (FK)   │
       │      │ credentials      │             │ date_of_birth  │
       │      │ specializations  │             │ address        │
       │      │ bio              │             │ emergency_cont │
       │      │ years_experience │             │ created_at     │
       │      │ rating           │             │ updated_at     │
       │      │ created_at       │             └────────────────┘
       │      │ updated_at       │                      │
       │      └──────────────────┘                      │
       │             │ 1                                │ 1
       │             │                                  │
       │             │ M                                │ M
       │      ┌──────▼───────────┐             ┌───────▼────────┐
       │      │therapist_services│             │    bookings    │
       │      ├──────────────────┤             ├────────────────┤
       │      │ therapist_id (FK)│             │ id (PK)        │
       │      │ service_id (FK)  │◄─────┐      │ client_id (FK) │
       │      └──────────────────┘      │      │ therapist_id(F)│
       │                                │      │ service_id (FK)│
       │                          ┌─────┴──────────┤ date           │
       │                          │   services     │ time_slot      │
       │                          ├────────────────┤ status         │
       │                          │ id (PK)        │ notes          │
       │                          │ name           │ created_at     │
       │                          │ description    │ updated_at     │
       │                          │ duration       │ deleted_at     │
       │                          │ price          │ (soft deletes) │
       │                          │ category       │ └────────────────┘
       │                          │ status         │        │ 1
       │                          │ created_at     │        │
       │                          │ updated_at     │        │ M
       │                          └────────────────┘  ┌─────▼──────────┐
       │                                             │   payments     │
       │                                             ├────────────────┤
       │                                             │ id (PK)        │
       │                                             │ booking_id (FK)│
       │                                             │ amount         │
       │                                             │ method         │
       │                                             │ status         │
       │                                             │ transaction_id │
       │                                             │ paid_at        │
       │                                             │ created_at     │
       │                                             │ updated_at     │
       │                                             └────────────────┘
       │
       │ 1                                          bookings
       │                                                │ 1
       │                                                │
       │ M                                              │ 1
┌──────▼───────────┐                             ┌─────▼──────────┐
│therapist_avail   │                             │    sessions    │
├──────────────────┤                             ├────────────────┤
│ id (PK)          │                             │ id (PK)        │
│ therapist_id (FK)│                             │ booking_id (FK)│
│ day_of_week      │                             │ started_at     │
│ start_time       │                             │ ended_at       │
│ end_time         │                             │ status         │
│ is_available     │                             │ notes          │
│ created_at       │                             │ created_at     │
│ updated_at       │                             │ updated_at     │
└──────────────────┘                             └────────────────┘
                                                         │ 1
┌──────────────────┐                                    │
│therapist_blocked │                                    │ M
├──────────────────┤                             ┌──────▼─────────┐
│ id (PK)          │                             │ session_notes  │
│ therapist_id (FK)│                             ├────────────────┤
│ date             │                             │ id (PK)        │
│ reason           │                             │ session_id (FK)│
│ created_at       │                             │ condition      │
│ updated_at       │                             │ discussion     │
└──────────────────┘                             │ techniques     │
                                                 │ response       │
              bookings                           │ progress       │
                 │ 1                             │ goals          │
                 │                               │ observations   │
                 │ M                             │ recommendations│
          ┌──────▼───────────┐                  │ is_shared      │
          │     reviews      │                  │ created_at     │
          ├──────────────────┤                  │ updated_at     │
          │ id (PK)          │                  └────────────────┘
          │ booking_id (FK)  │
          │ rating           │          clients
          │ comment          │             │ 1
          │ created_at       │             │
          │ updated_at       │             │ M
          └──────────────────┘      ┌──────▼─────────┐
                                    │client_progress │
              clients               ├────────────────┤
                 │ 1                │ id (PK)        │
                 │                  │ client_id (FK) │
                 │ M                │ date           │
          ┌──────▼───────────┐     │ anxiety_level  │
          │    messages      │     │ confidence     │
          ├──────────────────┤     │ sleep_quality  │
          │ id (PK)          │     │ overall_score  │
          │ sender_id (FK)   │     │ notes          │
          │ receiver_id (FK) │     │ created_at     │
          │ content          │     │ updated_at     │
          │ is_read          │     └────────────────┘
          │ created_at       │
          │ updated_at       │
          └──────────────────┘
```

**Tabel-tabel Utama:**

1. **users** - Central table untuk semua users (admin, therapists, clients)
2. **therapists** - Extended profile untuk users dengan role therapist
3. **clients** - Extended profile untuk users dengan role client
4. **services** - Katalog layanan terapi
5. **bookings** - Records booking/appointments
6. **sessions** - Actual sessions yang conducted
7. **session_notes** - Dokumentasi detailed setiap session
8. **payments** - Transaction records
9. **reviews** - Client reviews untuk therapists
10. **therapist_services** - Many-to-many relationship antara therapists dan services
11. **therapist_availability** - Regular weekly schedule therapists
12. **therapist_blocked_dates** - Specific dates therapists unavailable
13. **client_progress** - Progress tracking metrics
14. **messages** - Communication between users

**Sample Table Definitions (MySQL):**

```sql
-- Users Table
CREATE TABLE users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'therapist', 'client') NOT NULL DEFAULT 'client',
    phone VARCHAR(20),
    status ENUM('active', 'inactive', 'suspended') NOT NULL DEFAULT 'active',
    email_verified_at TIMESTAMP NULL,
    remember_token VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,
    INDEX idx_email (email),
    INDEX idx_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Therapists Table
CREATE TABLE therapists (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    credentials VARCHAR(255),
    specializations TEXT,
    bio TEXT,
    years_experience INT UNSIGNED,
    rating DECIMAL(3,2) DEFAULT 0.00,
    total_reviews INT UNSIGNED DEFAULT 0,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_rating (rating)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Services Table
CREATE TABLE services (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    duration INT UNSIGNED NOT NULL COMMENT 'Duration in minutes',
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(100),
    status ENUM('active', 'inactive') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_slug (slug),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bookings Table
CREATE TABLE bookings (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    booking_number VARCHAR(50) UNIQUE NOT NULL,
    client_id BIGINT UNSIGNED NOT NULL,
    therapist_id BIGINT UNSIGNED NOT NULL,
    service_id BIGINT UNSIGNED NOT NULL,
    booking_date DATE NOT NULL,
    time_slot TIME NOT NULL,
    status ENUM('pending', 'confirmed', 'completed', 'cancelled', 'no_show') DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,
    FOREIGN KEY (client_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE,
    INDEX idx_booking_number (booking_number),
    INDEX idx_client_id (client_id),
    INDEX idx_therapist_id (therapist_id),
    INDEX idx_booking_date (booking_date),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Payments Table
CREATE TABLE payments (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    booking_id BIGINT UNSIGNED NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    method ENUM('credit_card', 'bank_transfer', 'ewallet', 'qris') NOT NULL,
    status ENUM('pending', 'processing', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    transaction_id VARCHAR(255),
    payment_gateway VARCHAR(50),
    paid_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE,
    INDEX idx_booking_id (booking_id),
    INDEX idx_status (status),
    INDEX idx_transaction_id (transaction_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

Ini sudah bagian yang sangat panjang dan detail untuk BAB IV. File sudah mencapai lebih dari 670 baris. Saya perlu melanjutkan dengan bagian 4.4, 4.5, 4.6, dan 4.7 di file yang sama atau terpisah.

Apakah Anda ingin saya:
1. Lanjutkan di file yang sama (akan menjadi sangat panjang)?
2. Buat file terpisah untuk bagian sisanya?
3. Atau review dulu yang sudah ada?
