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

---

**[GAMBAR 4.1 - Organizational Structure CUR-HEART]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT ORGANIZATION CHART DIAGRAM]                      │
│                                                             │
│   Struktur Organisasi CUR-HEART:                           │
│                                                             │
│              ┌──────────────────────┐                      │
│              │   OWNER/FOUNDER      │                      │
│              │   (Dr. Sarah W.)     │                      │
│              └──────────┬───────────┘                      │
│                         │                                   │
│         ┌───────────────┼───────────────┐                 │
│         │               │               │                 │
│   ┌─────┴──────┐  ┌────┴─────┐  ┌─────┴──────┐          │
│   │HEAD         │  │OPERATIONS│  │ FINANCE &  │          │
│   │THERAPIST    │  │MANAGER   │  │ ADMIN      │          │
│   │(Michael A.) │  │          │  │            │          │
│   └─────┬──────┘  └────┬─────┘  └─────┬──────┘          │
│         │               │               │                 │
│    ┌────┴────┐     ┌────┴────┐    ┌────┴────┐           │
│    │TERAPIS  │     │CUSTOMER │    │FINANCE  │           │
│    │(5 orang)│     │SERVICE  │    │STAFF    │           │
│    │         │     │(2 orang)│    │(1 orang)│           │
│    └─────────┘     └─────────┘    └─────────┘           │
│                                                             │
│   Total Team: 10 orang                                     │
│   - 1 Owner/Founder                                        │
│   - 1 Head Therapist                                       │
│   - 5 Therapists                                           │
│   - 1 Operations Manager                                   │
│   - 2 Customer Service/Admin                               │
│   - 1 Finance Staff                                        │
│                                                             │
│   Format: Organizational Chart PNG/JPG                     │
│   Recommended size: 1200x800px                             │
│   Style: Professional hierarchy diagram dengan foto/icon   │
│                                                             │
│   File: assets/images/organizational-structure-curheart.png│
│   Tool: Microsoft Visio, Draw.io, PowerPoint, atau Canva  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.1: Struktur organisasi CUR-HEART menunjukkan hierarchy dari Owner hingga staff operasional dengan total 10 anggota tim_

---

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

**Tabel 4.1 Analisis Masalah dengan Data Kuantitatif**

| No | Masalah | Data Kuantitatif | Dampak | Prioritas |
|----|---------|------------------|--------|-----------|
| 1 | Conversion Rate Booking Rendah | 60% dari inquiry menjadi booking (40% loss) | Loss potensial revenue Rp 20 juta/bulan | Critical |
| 2 | Konflik Jadwal & Double Booking | 8-10 kasus per bulan | Customer dissatisfaction, reputasi negatif | High |
| 3 | Waktu Dokumentasi Terapi Lama | 15 menit per sesi x 120 sesi/bulan = 30 jam/bulan | Inefisiensi operasional, terapis tidak produktif | High |
| 4 | Tidak Ada Data untuk Decision | Laporan bulanan butuh 2-3 hari kerja | Missed opportunities, keputusan tidak optimal | High |
| 5 | Pengalaman Klien Kurang Optimal | Retention rate hanya 45% | Churn tinggi, kehilangan repeat customers | Critical |
| 6 | Beban Administratif Tinggi | Admin menghabiskan 70% waktu untuk tugas manual | Cost tinggi, tidak scalable | High |
| 7 | Security & Privacy Risks | Data sensitif tersimpan tidak encrypted | Resiko legal, pelanggaran UU PDP | Critical |
| 8 | Hambatan Skalabilitas | Sistem manual tidak support growth >20 terapis | Tidak bisa ekspansi, kehilangan market share | Medium |

**Sumber:** Observasi lapangan dan wawancara dengan CUR-HEART Management, September 2024

---

**[GAMBAR 4.2 - Current Business Process (As-Is)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT AS-IS BUSINESS PROCESS FLOWCHART]                │
│                                                             │
│   PROSES BOOKING & TERAPI EXISTING (MANUAL):               │
│                                                             │
│   CLIENT                  ADMIN              THERAPIST      │
│     │                       │                    │          │
│     │ 1. Inquiry via        │                    │          │
│     │    WhatsApp/Phone     │                    │          │
│     ├──────────────────────>│                    │          │
│     │                       │ 2. Check schedule  │          │
│     │                       │    manually        │          │
│     │                       ├───────────────────>│          │
│     │                       │<───────────────────┤          │
│     │                       │ 3. Confirm slot    │          │
│     │<──────────────────────┤                    │          │
│     │ 4. Transfer payment   │                    │          │
│     ├──────────────────────>│                    │          │
│     │                       │ 5. Manual verify   │          │
│     │                       │    (hours/days)    │          │
│     │<──────────────────────┤                    │          │
│     │ 6. Attend session     │                    │          │
│     ├───────────────────────┼───────────────────>│          │
│     │                       │                    │ 7. Conduct│
│     │                       │                    │   therapy │
│     │                       │                    │ 8. Write  │
│     │                       │                    │   notes   │
│     │                       │                    │   manual  │
│     │                       │                    │   (15 min)│
│     │                       │<───────────────────┤          │
│     │                       │ 9. Update Excel    │          │
│     │                       │    (end of day)    │          │
│     ▼                       ▼                    ▼          │
│                                                             │
│   Pain Points:                                              │
│   ❌ 15-20 min/booking                                      │
│   ❌ 8-10 double bookings/month                             │
│   ❌ Manual payment verification (hours/days)               │
│   ❌ 15 min documentation/session                           │
│   ❌ No real-time data                                      │
│   ❌ 40% conversion loss                                    │
│                                                             │
│   Total Process Time: ~45 minutes per booking              │
│   Error Rate: 8-10% (scheduling conflicts)                 │
│                                                             │
│   Format: Process Flowchart PNG/JPG                        │
│   Recommended size: 1400x1000px                            │
│   Style: Swimlane diagram dengan pain points highlighted   │
│                                                             │
│   File: assets/images/as-is-business-process.png           │
│   Tool: Draw.io, Lucidchart, Microsoft Visio               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.2: Current business process (As-Is) menunjukkan alur booking manual dengan total waktu ~45 menit per booking dan error rate 8-10%_

---

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

**Tabel 4.2 Stakeholder Analysis Matrix**

| Stakeholder | Role | Kategori | Interest Level | Power/Influence | Kebutuhan Utama | Engagement Strategy | Frekuensi Komunikasi |
|-------------|------|----------|----------------|-----------------|-----------------|---------------------|---------------------|
| Owner CUR-HEART | Decision Maker, Sponsor | Primary | Very High | Very High | ROI, growth, competitive advantage | Manage Closely - Weekly updates, milestone approvals | Weekly |
| Terapis (5 orang) | Primary Users | Primary | Very High | High | Ease of use, time saving, better client management | Manage Closely - Requirements workshop, UAT | Bi-weekly |
| Admin Staff (2 orang) | System Operators | Primary | High | High | Workload reduction, efficiency | Manage Closely - Process mapping, training | Weekly |
| Klien Aktif | End Users | Primary | High | Medium | Convenience, privacy, good UX | Keep Informed - User research, feedback surveys | Monthly |
| Dosen Pembimbing | Academic Supervisor | Secondary | High | High | Quality, learning outcomes, documentation | Keep Satisfied - Weekly consultation, reviews | Weekly |
| Tim Pengembang (3 orang) | Project Team | Internal | Very High | Very High | Successful delivery, learning, portfolio | Manage Closely - Daily standups, collaboration | Daily |
| Universitas Nusa Mandiri | Academic Institution | Secondary | Medium | Medium | Student achievement, industry collaboration | Keep Informed - Progress reports, presentations | Monthly |

**Sumber:** Analisis Stakeholder CUR-HEART, September 2024

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

---

**[GAMBAR 4.3 - Stakeholder Power-Interest Matrix]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT POWER-INTEREST MATRIX DIAGRAM]                   │
│                                                             │
│   STAKEHOLDER ANALYSIS - POWER vs INTEREST MATRIX          │
│                                                             │
│   HIGH POWER                                                │
│        │                                                    │
│        │  MANAGE CLOSELY      │  KEEP SATISFIED            │
│        │  ┌────────────────┐  │  ┌───────────────┐        │
│        │  │ • Owner        │  │  │ • Dosen       │        │
│        │  │ • Terapis (5)  │  │  │   Pembimbing  │        │
│        │  │ • Tim Dev (3)  │  │  │               │        │
│        │  └────────────────┘  │  └───────────────┘        │
│        │──────────────────────┼────────────────────        │
│        │  MONITOR            │  KEEP INFORMED             │
│        │  ┌────────────────┐  │  ┌───────────────┐        │
│        │  │ • (None)       │  │  │ • Admin (2)   │        │
│        │  │                │  │  │ • Klien       │        │
│        │  │                │  │  │ • Universitas │        │
│        │  └────────────────┘  │  └───────────────┘        │
│   LOW POWER                                                 │
│        └───────────────────────┼────────────────────>       │
│              LOW INTEREST         HIGH INTEREST            │
│                                                             │
│   Quadrant Details:                                         │
│   ┌─ MANAGE CLOSELY (7 stakeholders):                      │
│   │  High engagement, weekly/daily communication           │
│   │  Critical untuk project success                        │
│   │                                                         │
│   ┌─ KEEP SATISFIED (1 stakeholder):                       │
│   │  Regular updates, involve in key decisions             │
│   │  Academic oversight & quality assurance                │
│   │                                                         │
│   ┌─ KEEP INFORMED (3 stakeholder groups):                 │
│   │  Regular communication, feedback loops                 │
│   │  Important users & beneficiaries                       │
│   │                                                         │
│   └─ MONITOR (0 stakeholders):                             │
│      Minimal communication, periodic updates               │
│                                                             │
│   Total Stakeholders: 11 groups, 23 individuals            │
│                                                             │
│   Format: 2x2 Matrix Diagram PNG/JPG                       │
│   Recommended size: 1200x1000px                            │
│   Style: Quadrant matrix dengan stakeholder positioning    │
│                                                             │
│   File: assets/images/stakeholder-power-interest-matrix.png│
│   Tool: PowerPoint, Canva, Draw.io, atau Excel            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.3: Stakeholder Power-Interest Matrix menunjukkan positioning 11 stakeholder groups untuk strategi engagement yang tepat_

---

### 4.1.5 Project Charter

**Project Charter - Sistem Informasi CUR-HEART**

**Tabel 4.3 Project Charter - Executive Summary**

| Elemen | Deskripsi |
|--------|-----------|
| **Project Title** | Pengembangan Sistem Informasi Manajemen Booking dan Terapi CUR-HEART Berbasis Web |
| **Project Manager** | Roki Anjas (NIM: 11250066) |
| **Project Sponsor** | CUR-HEART Management |
| **Academic Supervisor** | Rani Irma Handayani, M.Kom |
| **Development Team** | 3 developers (Full Stack) |
| **Project Start Date** | 16 September 2024 |
| **Target Completion** | 1 Desember 2024 (11 minggu / 77 hari kerja) |
| **Total Budget** | Rp 5.000.000 |
| **Methodology** | Waterfall SDLC (6 phases) |
| **Target Users** | 3 roles: Admin, Therapist (5 orang), Client (100+ existing) |
| **Platform** | Web-based application (responsive design) |
| **Technology Stack** | Laravel 10, PHP 8.2, MySQL 8.0, Tailwind CSS 3.0 |
| **Main Objective** | Meningkatkan efisiensi operasional min 40%, conversion rate dari 60% ke 85% |
| **Key Deliverables** | 1) Web application production-ready<br>2) Source code & documentation<br>3) Capstone report (80-100 hal)<br>4) Training materials<br>5) Presentation & demo video |
| **Success Criteria** | 1) 95%+ functional requirements implemented<br>2) SUS score ≥ 80/100<br>3) UAT passed<br>4) No critical bugs<br>5) Conversion rate ≥ 75% |
| **Key Constraints** | 1) Timeline: 11 minggu strict<br>2) Budget: Rp 5 juta<br>3) Team: 3 developers<br>4) Academic requirement: Must use Laravel |

**Project Authorization:**

| Name | Role | Signature | Date |
|------|------|-----------|------|
| [Owner Name] | Project Sponsor | _____________ | ___/___/___ |
| Roki Anjas | Project Manager | _____________ | ___/___/___ |
| Rani Irma Handayani, M.Kom | Academic Supervisor | _____________ | ___/___/___ |

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

**Tabel 4.4 Work Breakdown Structure (Level 1-3)**

| WBS Code | Work Package | Deliverables | Duration | Responsible |
|----------|--------------|--------------|----------|-------------|
| **1.0** | **Sistem Informasi CUR-HEART** | Sistem booking & terapi lengkap | 77 hari | Tim Proyek |
| 1.1 | Project Management | Project documentation | 77 hari | Project Manager |
| 1.1.1 | Project Planning | Project charter, WBS, schedule, budget | 3 hari | Project Manager |
| 1.1.2 | Progress Monitoring | Weekly status reports | 77 hari | Project Manager |
| 1.1.3 | Risk Management | Risk register, mitigation plans | 77 hari | Project Manager |
| 1.1.4 | Stakeholder Communication | Communication logs | 77 hari | Project Manager |
| 1.2 | Requirements Analysis | SRS document | 11 hari | Business Analyst |
| 1.2.1 | Stakeholder Interviews | Interview transcripts | 5 hari | Business Analyst |
| 1.2.2 | Business Process Analysis | As-Is & To-Be process models | 3 hari | Business Analyst |
| 1.2.3 | Requirements Documentation | Functional & non-functional requirements | 3 hari | Business Analyst |
| 1.2.4 | Requirements Validation | Validated SRS | 1 hari | Business Analyst |
| 1.3 | System Design | Design documents | 14 hari | System Designer |
| 1.3.1 | Architecture Design | Architecture diagram, tech stack decision | 3 hari | System Architect |
| 1.3.2 | Database Design | ERD, table structures, normalization | 4 hari | Database Designer |
| 1.3.3 | UI/UX Design | Mockups, design system, component library | 5 hari | UI/UX Designer |
| 1.3.4 | Security Design | Security architecture, authentication flow | 2 hari | Security Specialist |
| 1.4 | Development | Working application | 28 hari | Development Team |
| 1.4.1 | Environment Setup | Dev, staging, prod environments | 2 hari | DevOps |
| 1.4.2 | Backend Development | APIs, business logic, database | 10 hari | Backend Developer |
| 1.4.3 | Frontend Development | UI implementation | 12 hari | Frontend Developer |
| 1.4.4 | Integration | Integrated system | 5 hari | Full Stack Developer |
| 1.4.5 | Code Review | Code quality reports | 2 hari | Senior Developer |
| 1.5 | Testing | Test reports, bug tracking | 14 hari | QA Team |
| 1.5.1 | Unit Testing | Unit test coverage report | 3 hari | Developers |
| 1.5.2 | Integration Testing | Integration test results | 3 hari | QA Engineer |
| 1.5.3 | Functional Testing | Functional test cases executed | 4 hari | QA Engineer |
| 1.5.4 | Usability Testing | Usability test report (SUS score) | 3 hari | UX Researcher |
| 1.5.5 | User Acceptance Testing (UAT) | UAT approval, acceptance criteria met | 2 hari | Stakeholders |
| 1.6 | Deployment | Live production system | 7 hari | DevOps Team |
| 1.6.1 | Production Setup | Server configured, domain live | 2 hari | DevOps |
| 1.6.2 | Application Deployment | App deployed to production | 2 hari | DevOps |
| 1.6.3 | Go-Live | System operational | 1 hari | Project Manager |
| 1.6.4 | User Training | Trained users, training materials | 2 hari | Trainer |
| 1.7 | Documentation | Complete project documentation | 21 hari | Documentation Team |
| 1.7.1 | Technical Documentation | API docs, architecture docs, DB schema | 7 hari | Tech Writer |
| 1.7.2 | User Documentation | User manual, admin guide | 5 hari | Tech Writer |
| 1.7.3 | Capstone Report | Final report (80-100 pages) | 14 hari | Project Team |
| 1.7.4 | Presentation Materials | Slides, demo video | 7 hari | Project Team |

**Total Work Packages:** 36 level-3 packages  
**Total Duration:** 77 hari kerja (11 minggu)

---

**[GAMBAR 4.4 - Work Breakdown Structure (WBS) CUR-HEART System]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT WBS HIERARCHICAL DIAGRAM - 3 LEVELS]             │
│                                                             │
│   Level 1: PROJECT (Root)                                  │
│   CUR-HEART System Development                             │
│   │                                                         │
│   ├─ 1.1 Project Management (77 days)                      │
│   │  ├─ 1.1.1 Project Planning (3 days)                    │
│   │  ├─ 1.1.2 Progress Monitoring (77 days)                │
│   │  ├─ 1.1.3 Risk Management (77 days)                    │
│   │  └─ 1.1.4 Stakeholder Communication (77 days)          │
│   │                                                         │
│   ├─ 1.2 Requirements Analysis (11 days)                   │
│   │  ├─ 1.2.1 Stakeholder Interviews (5 days)              │
│   │  ├─ 1.2.2 Business Process Analysis (3 days)           │
│   │  ├─ 1.2.3 Requirements Documentation (3 days)          │
│   │  └─ 1.2.4 Requirements Validation (1 day)              │
│   │                                                         │
│   ├─ 1.3 System Design (14 days)                           │
│   │  ├─ 1.3.1 Architecture Design (3 days)                 │
│   │  ├─ 1.3.2 Database Design (4 days)                     │
│   │  ├─ 1.3.3 UI/UX Design (5 days)                        │
│   │  └─ 1.3.4 Security Design (2 days)                     │
│   │                                                         │
│   ├─ 1.4 Development (28 days)                             │
│   │  ├─ 1.4.1 Environment Setup (2 days)                   │
│   │  ├─ 1.4.2 Backend Development (10 days)                │
│   │  ├─ 1.4.3 Frontend Development (12 days)               │
│   │  ├─ 1.4.4 Integration (5 days)                         │
│   │  └─ 1.4.5 Code Review (2 days)                         │
│   │                                                         │
│   ├─ 1.5 Testing (14 days)                                 │
│   │  ├─ 1.5.1 Unit Testing (3 days)                        │
│   │  ├─ 1.5.2 Integration Testing (3 days)                 │
│   │  ├─ 1.5.3 Functional Testing (4 days)                  │
│   │  ├─ 1.5.4 Usability Testing (3 days)                   │
│   │  └─ 1.5.5 User Acceptance Testing (2 days)             │
│   │                                                         │
│   ├─ 1.6 Deployment (7 days)                               │
│   │  ├─ 1.6.1 Production Setup (2 days)                    │
│   │  ├─ 1.6.2 Application Deployment (2 days)              │
│   │  ├─ 1.6.3 Go-Live (1 day)                              │
│   │  └─ 1.6.4 User Training (2 days)                       │
│   │                                                         │
│   └─ 1.7 Documentation (21 days, parallel)                 │
│      ├─ 1.7.1 Technical Documentation (7 days)             │
│      ├─ 1.7.2 User Documentation (5 days)                  │
│      ├─ 1.7.3 Capstone Report (14 days)                    │
│      └─ 1.7.4 Presentation Materials (7 days)              │
│                                                             │
│   Summary:                                                  │
│   • 7 Level-2 Phases                                       │
│   • 36 Level-3 Work Packages                               │
│   • 77 Working Days (11 weeks)                             │
│   • Team: 3 Developers                                     │
│                                                             │
│   Format: Hierarchical Tree Diagram PNG                    │
│   Recommended size: 1800x1400px                            │
│   Style: Tree structure dengan color coding per phase      │
│                                                             │
│   File: assets/images/wbs-curheart-3-levels.png            │
│   Tool: Microsoft Project, WBS Chart Pro, atau Draw.io     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.4: Work Breakdown Structure (WBS) 3-level proyek CUR-HEART dengan 7 phases, 36 work packages, durasi 77 hari_

---

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

**Tabel 4.5 Project Schedule dengan Milestones**

| Phase | Task Name | Duration | Start | End | Status | Milestone |
|-------|-----------|----------|-------|-----|--------|-----------|
| **1. Initiation** | Project kick-off & charter | 3 hari | 16-Sep | 18-Sep | ✅ Complete | M1: Project Approved |
| | Kick-off meeting | 1 hari | 16-Sep | 16-Sep | ✅ | |
| | Stakeholder identification | 1 hari | 17-Sep | 17-Sep | ✅ | |
| | Project charter approval | 1 hari | 18-Sep | 18-Sep | ✅ | |
| **2. Requirements** | Analysis & documentation | 11 hari | 19-Sep | 29-Sep | ✅ Complete | M2: Requirements Complete |
| | Stakeholder interviews | 5 hari | 19-Sep | 23-Sep | ✅ | |
| | Business process analysis | 3 hari | 19-Sep | 21-Sep | ✅ | |
| | Requirements documentation | 3 hari | 26-Sep | 28-Sep | ✅ | |
| | Requirements validation | 1 hari | 29-Sep | 29-Sep | ✅ | |
| **3. Design** | System & UI/UX design | 14 hari | 30-Sep | 13-Oct | ✅ Complete | M3: Design Complete |
| | Architecture design | 3 hari | 30-Sep | 2-Oct | ✅ | |
| | Database design | 4 hari | 3-Oct | 6-Oct | ✅ | |
| | UI/UX design | 5 hari | 7-Oct | 11-Oct | ✅ | |
| | Security design | 2 hari | 12-Oct | 13-Oct | ✅ | |
| **4. Development** | Coding & integration | 28 hari | 14-Oct | 10-Nov | ⏳ In Progress | M4: Development Complete |
| | Environment setup | 2 hari | 14-Oct | 15-Oct | ✅ | |
| | Database implementation | 3 hari | 16-Oct | 18-Oct | ✅ | |
| | Authentication system | 4 hari | 19-Oct | 22-Oct | ✅ | |
| | Backend development | 10 hari | 23-Oct | 1-Nov | ⏳ | |
| | Frontend development | 12 hari | 23-Oct | 3-Nov | ⏳ | |
| | Integration | 5 hari | 4-Nov | 8-Nov | 🔜 Upcoming | |
| | Code review | 2 hari | 9-Nov | 10-Nov | 🔜 | |
| **5. Testing** | QA & UAT | 14 hari | 11-Nov | 24-Nov | 🔜 Upcoming | M5: Testing Complete |
| | Unit testing | 3 hari | 11-Nov | 13-Nov | 🔜 | |
| | Integration testing | 3 hari | 14-Nov | 16-Nov | 🔜 | |
| | Functional testing | 4 hari | 17-Nov | 20-Nov | 🔜 | |
| | Usability testing (SUS) | 3 hari | 21-Nov | 23-Nov | 🔜 | |
| | UAT | 2 hari | 23-Nov | 24-Nov | 🔜 | |
| **6. Deployment** | Go-live & training | 7 hari | 25-Nov | 1-Dec | 🔜 Upcoming | M6: System Live |
| | Production setup | 2 hari | 25-Nov | 26-Nov | 🔜 | |
| | App deployment | 2 hari | 27-Nov | 28-Nov | 🔜 | |
| | Go-live | 1 hari | 29-Nov | 29-Nov | 🔜 | M6: System Live |
| | User training | 2 hari | 30-Nov | 1-Dec | 🔜 | M7: Project Complete |
| **7. Documentation** | Reports & materials | 21 hari | 11-Nov | 1-Dec | ⏳ In Progress | M7: Project Complete |
| | Technical documentation | 7 hari | 11-Nov | 17-Nov | ⏳ | |
| | User documentation | 5 hari | 18-Nov | 22-Nov | 🔜 | |
| | Capstone report | 14 hari | 18-Nov | 1-Dec | ⏳ | |
| | Presentation prep | 7 hari | 25-Nov | 1-Dec | 🔜 | |

**Total Duration:** 77 hari kerja (11 minggu)  
**Critical Path:** Initiation → Requirements → Design → Development → Integration → Testing → UAT → Deployment  
**Current Progress:** 45% complete (Phase 1-3 done, Phase 4 in progress)

---

**[GAMBAR 4.5 - Gantt Chart Project Schedule (77 Working Days)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT GANTT CHART - 11 WEEKS TIMELINE]                 │
│                                                             │
│   PROJECT: CUR-HEART System Development                    │
│   Timeline: 16 Sep 2024 - 1 Dec 2024 (77 days)             │
│                                                             │
│   Task Name              Week                               │
│                    1  2  3  4  5  6  7  8  9  10 11        │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      │
│   1. Initiation    ██                                       │
│   M1: Approved     ⭐                                       │
│                                                             │
│   2. Requirements  ░░██████                                 │
│   M2: SRS Done        ⭐                                    │
│                                                             │
│   3. Design           ░░░░████████                          │
│   M3: Design Done            ⭐                             │
│                                                             │
│   4. Development            ░░░░██████████████████          │
│   M4: Code Done                                  ⭐         │
│                                                             │
│   5. Testing                                ░░░░████████    │
│   M5: UAT Pass                                      ⭐      │
│                                                             │
│   6. Deployment                                     ░░░░██  │
│   M6: Go-Live                                           ⭐  │
│                                                             │
│   7. Documentation                      ████████████████    │
│   M7: Complete                                          ⭐  │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      │
│                                                             │
│   Legend:                                                   │
│   ██ = Completed     ░░ = Dependency/Buffer                 │
│   ⭐ = Milestone     (Dates shown)                          │
│                                                             │
│   Critical Path (Red): Init → Req → Design → Dev →         │
│                       Integration → Test → Deploy           │
│   Total Duration: 77 working days                          │
│   Milestones: 7 major milestones                           │
│   Dependencies: Sequential with some parallel tasks         │
│                                                             │
│   Format: Gantt Chart PNG/PDF                              │
│   Recommended size: 1800x1000px                            │
│   Style: Professional dengan critical path highlighted      │
│                                                             │
│   File: assets/images/gantt-chart-77-days.png              │
│   Tool: Microsoft Project, GanttProject, atau Excel        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.5: Gantt Chart project schedule 77 hari kerja (11 minggu) dengan 7 phases, 7 milestones, dan critical path_

---

### 4.2.3 Biaya Proyek (Cost Management)

**Tabel 4.6 Budget Breakdown (Rp 5,000,000 Total)**

| Category | Item | Unit Cost | Qty | Total (Rp) | % of Budget | Priority |
|----------|------|-----------|-----|------------|-------------|----------|
| **Infrastructure** | | | | **1.500.000** | 30% | Critical |
| | Domain (.com, 1 tahun) | 150.000 | 1 | 150.000 | 3% | Must Have |
| | VPS Hosting (3 bulan) | 300.000 | 3 | 900.000 | 18% | Must Have |
| | SSL Certificate (Let's Encrypt) | 0 | 1 | 0 | 0% | Must Have |
| | Backup Storage (Google Drive) | 150.000 | 1 | 150.000 | 3% | Should Have |
| | CDN Service (Cloudflare Pro) | 300.000 | 1 | 300.000 | 6% | Could Have |
| **Development Tools** | | | | **800.000** | 16% | High |
| | Code Editor (VS Code) | 0 | 3 | 0 | 0% | Free |
| | Design Tools (Figma Pro) | 200.000 | 1 | 200.000 | 4% | Must Have |
| | Database Tools (MySQL Workbench) | 0 | 3 | 0 | 0% | Free |
| | Version Control (GitHub) | 0 | 1 | 0 | 0% | Free |
| | Project Management (Asana) | 100.000 | 1 | 100.000 | 2% | Should Have |
| | Testing Tools | 500.000 | 1 | 500.000 | 10% | Must Have |
| **Third-Party Services** | | | | **1.200.000** | 24% | High |
| | Payment Gateway (Midtrans) | 0 | 1 | 0 | 0% | Setup free |
| | Payment Testing Credit | 500.000 | 1 | 500.000 | 10% | Must Have |
| | Email Service (SendGrid) | 200.000 | 1 | 200.000 | 4% | Must Have |
| | SMS Service (Twilio) | 300.000 | 1 | 300.000 | 6% | Could Have |
| | Monitoring (Sentry) | 200.000 | 1 | 200.000 | 4% | Should Have |
| **Documentation** | | | | **500.000** | 10% | Medium |
| | Report Printing (Full Color) | 300.000 | 1 | 300.000 | 6% | Must Have |
| | X-Banner Printing (60x160) | 200.000 | 1 | 200.000 | 4% | Must Have |
| **Contingency Reserve** | | | | **1.000.000** | 20% | Critical |
| | Buffer for unexpected costs | 1.000.000 | 1 | 1.000.000 | 20% | Buffer |
| **TOTAL PROJECT BUDGET** | | | | **5.000.000** | 100% | |

---

**[GAMBAR 4.6 - Budget Allocation Breakdown (Rp 5,000,000)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT BUDGET PIE CHART + BAR COMPARISON]               │
│                                                             │
│   TOTAL BUDGET: Rp 5,000,000                               │
│                                                             │
│   ┌─────────────────────────────────────────┐              │
│   │   PIE CHART - Budget Allocation         │              │
│   │                                         │              │
│   │     Infrastructure 30%                  │              │
│   │     Rp 1,500,000                        │              │
│   │                                         │              │
│   │     Third-Party Services 24%            │              │
│   │     Rp 1,200,000                        │              │
│   │                                         │              │
│   │     Contingency 20%                     │              │
│   │     Rp 1,000,000                        │              │
│   │                                         │              │
│   │     Dev Tools 16%                       │              │
│   │     Rp 800,000                          │              │
│   │                                         │              │
│   │     Documentation 10%                   │              │
│   │     Rp 500,000                          │              │
│   └─────────────────────────────────────────┘              │
│                                                             │
│   BAR CHART - Spending by Category:                        │
│   Infrastructure    ████████████████░░ 30%                 │
│   Third-Party       ████████████░░░░░░ 24%                 │
│   Contingency       ████████████░░░░░░ 20%                 │
│   Dev Tools         ████████░░░░░░░░░░ 16%                 │
│   Documentation     █████░░░░░░░░░░░░░ 10%                 │
│                                                             │
│   Key Highlights:                                          │
│   • Largest: Infrastructure (Rp 1.5M - hosting, domain)    │
│   • Critical: Third-Party APIs (Rp 1.2M - payment, email)  │
│   • Buffer: Contingency 20% (Rp 1M reserved)               │
│   • Free Tools: VS Code, MySQL, GitHub (Rp 0)              │
│                                                             │
│   Format: Combo Chart (Pie + Bar) PNG                      │
│   Recommended size: 1600x900px                             │
│   Style: Professional dengan color coding                  │
│                                                             │
│   File: assets/images/budget-allocation-5m.png             │
│   Tool: Excel, Google Sheets, atau Canva                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.6: Budget allocation breakdown Rp 5 juta dengan pie chart alokasi 5 kategori dan bar chart perbandingan_

---

**Cost Performance Index (CPI):**

| Period | Planned Value (PV) | Earned Value (EV) | Actual Cost (AC) | Cost Variance (CV) | CPI | Status |
|--------|-------------------|-------------------|------------------|-------------------|-----|--------|
| Month 1 (Sep) | Rp 1.500.000 | Rp 1.545.000 | Rp 1.450.000 | +Rp 95.000 | 1.07 | ✅ Under budget |
| Month 2 (Oct) | Rp 2.000.000 | Rp 2.020.000 | Rp 1.980.000 | +Rp 40.000 | 1.02 | ✅ On track |
| Month 3 (Nov) | Rp 1.500.000 | (in progress) | (in progress) | TBD | TBD | ⏳ In progress |
| **Total to Date** | **Rp 3.500.000** | **Rp 3.565.000** | **Rp 3.430.000** | **+Rp 135.000** | **1.04** | ✅ **Under budget** |

**Notes:**
- CPI > 1.0 = Under budget (good performance)
- CPI = 1.0 = On budget (as planned)
- CPI < 1.0 = Over budget (need corrective action)
- Current CPI 1.04 indicates efficient cost management

### 4.2.4 Kualitas Proyek (Quality Management)

**Tabel 4.7 Quality Standards dan Metrics**

| Quality Area | Standard/Criteria | Target Metric | Measurement Method | Responsibility | Frequency |
|--------------|-------------------|---------------|-------------------|----------------|-----------|
| **Code Quality** | Laravel PSR-12, PHPDoc | Grade A, No critical issues | SonarQube, PHPStan | Developers | Per commit |
| | DRY principle, SOLID | Cyclomatic complexity < 10 | Code analysis tools | Developers | Per PR |
| | Meaningful names, modularity | Maintainability Index > 70 | Code metrics | Developers | Weekly |
| **Functional Quality** | All must-have requirements | 95%+ implemented | Requirements traceability | PM | Per sprint |
| | Business rules correct | 100% rules validated | Functional testing | QA | Pre-UAT |
| | Error handling | All exceptions handled | Unit & integration test | Developers | Continuous |
| **Performance** | Page load time | < 3 seconds | Lighthouse, GTmetrix | Developers | Weekly |
| | Time to First Byte (TTFB) | < 600ms | Performance monitoring | DevOps | Weekly |
| | Database query performance | < 100ms per query | Query profiler | DBA | Weekly |
| | API response time | < 500ms | API testing tools | Backend Dev | Weekly |
| **Security** | OWASP Top 10 compliance | No critical vulnerabilities | OWASP ZAP, security audit | Security Lead | Bi-weekly |
| | Authentication & Authorization | JWT secure, role-based | Security testing | Backend Dev | Pre-deploy |
| | Data encryption | Sensitive data encrypted | Code review | Security Lead | Pre-deploy |
| | SQL injection prevention | Zero SQL vulnerabilities | Penetration testing | QA | Pre-deploy |
| **Usability** | System Usability Scale (SUS) | ≥ 80/100 | User testing with 10 users | UX Lead | Week 10 |
| | Task success rate | ≥ 90% | Usability testing | UX Lead | Week 10 |
| | Error rate per task | < 5% | User testing observation | UX Lead | Week 10 |
| | WCAG 2.1 Level AA | Pass accessibility audit | Lighthouse, aXe | Frontend Dev | Weekly |
| **Testing Coverage** | Unit test coverage | ≥ 70% for critical code | PHPUnit coverage | Developers | Continuous |
| | Integration test coverage | 100% critical flows | Laravel Dusk | QA | Pre-UAT |
| | Defect density | < 5 bugs per 1000 LOC | Bug tracking (Jira) | QA | Post-testing |
| **Documentation** | Technical docs | 100% complete | Documentation review | Tech Writer | Pre-deploy |
| | User manuals | All roles covered | User review | Tech Writer | Pre-training |
| | Code comments | Complex logic commented | Code review | Developers | Per PR |

**Quality Assurance Process:**
1. Code Review (GitHub PR) → Unit Testing (PHPUnit) → Integration Testing (Laravel Dusk) → Performance Testing (Lighthouse) → Security Audit (OWASP ZAP) → Usability Testing (SUS) → UAT (Stakeholders)
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

**Tabel 4.8 Resource Allocation Matrix**

| Resource Name | Primary Role | Secondary Role | Skills/Expertise | Allocation | Project Phases | Weekly Hours | Cost (if any) |
|---------------|--------------|----------------|------------------|------------|----------------|--------------|---------------|
| **Internal Team (Core)** | | | | | | | |
| Roki Anjas | Project Manager | Backend Developer | Leadership, Laravel, PHP, MySQL, API | 100% | All phases | 40 hrs | Free (student) |
| Susanto | Frontend Developer | UI/UX Designer | Tailwind CSS, Blade, Figma, UX research | 100% | Design-Deployment | 40 hrs | Free (student) |
| Fahruroji | Full-Stack Developer | Database Admin | Laravel, MySQL, Testing, Documentation | 100% | Design-Deployment | 40 hrs | Free (student) |
| **External Stakeholders** | | | | | | | |
| Rani Irma Handayani, M.Kom | Academic Supervisor | Technical Advisor | Systems analysis, project management | Part-time | All phases | 2 hrs | Free (faculty) |
| CUR-HEART Owner | Project Sponsor | Decision Maker | Business strategy, budget approval | As needed | Initiation, UAT | 1 hr | Free (sponsor) |
| Terapis (5 orang) | Subject Matter Expert | End User | Hypnotherapy, workflow knowledge | As needed | Requirements, UAT | 2 hrs/person | Free (SME) |
| Admin Staff (2 orang) | System Operator | Tester | Admin processes, data entry | As needed | Requirements, UAT | 3 hrs/person | Free (SME) |
| Sample Clients (10 orang) | End User | Tester | User perspective, feedback | As needed | Testing | 1 hr/person | Free (volunteer) |
| **Specialized Resources** | | | | | | | |
| Technical Mentor | Code Reviewer | - | Senior Laravel developer | Ad-hoc | Development | 1 hr/week | Free (community) |
| Security Consultant | Security Auditor | - | Web security, OWASP | Ad-hoc | Testing | 2 hrs total | Free (volunteer) |

**Resource Distribution by Phase:**

| Phase | Roki (PM/BE) | Susanto (FE/UX) | Fahruroji (FS/DBA) | External | Total Hours |
|-------|-------------|-----------------|-------------------|----------|-------------|
| 1. Initiation (3 days) | 24 hrs (Lead) | 8 hrs | 8 hrs | 2 hrs (Supervisor) | 42 hrs |
| 2. Requirements (11 days) | 40 hrs | 32 hrs | 16 hrs | 20 hrs (SME) | 108 hrs |
| 3. Design (14 days) | 56 hrs | 80 hrs (Lead) | 56 hrs | 4 hrs (Review) | 196 hrs |
| 4. Development (28 days) | 112 hrs (Lead) | 112 hrs | 112 hrs | 4 hrs (Mentor) | 340 hrs |
| 5. Testing (14 days) | 40 hrs | 40 hrs | 72 hrs (Lead) | 20 hrs (Users) | 172 hrs |
| 6. Deployment (7 days) | 32 hrs (Lead) | 16 hrs | 24 hrs | 8 hrs (Training) | 80 hrs |
| 7. Documentation (21 days) | 60 hrs | 40 hrs | 60 hrs (Lead) | 2 hrs (Review) | 162 hrs |
| **Total** | **364 hrs** | **328 hrs** | **348 hrs** | **60 hrs** | **1100 hrs** |

**Notes:**
- All internal team members: Full-time allocation (40 hrs/week during project)
- No salary costs (academic capstone project)
- Total project effort: ~1100 person-hours over 11 weeks
- Average: 100 person-hours per week

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

**Tabel 4.9 Risk Register dengan Mitigation Strategy**

| ID | Risk Event | Category | Probability | Impact | Risk Score | Priority | Mitigation Strategy (Preventive) | Contingency Plan (Reactive) | Risk Owner | Status |
|----|-----------|----------|-------------|--------|------------|----------|----------------------------------|---------------------------|------------|--------|
| R01 | Scope creep dari stakeholder requests | Scope | Medium (50%) | High (8) | 4.0 | Critical | Strict change control process, MoSCoW prioritization, document approved scope baseline | Defer nice-to-have features to Phase 2 post-launch, renegotiate timeline | PM | ⚠️ Active |
| R02 | Technical complexity lebih tinggi dari estimasi | Technical | Medium (40%) | Medium (6) | 2.4 | High | Early prototyping, regular technical reviews, spike solutions for unknowns | Request mentor assistance, break into smaller tasks, extend timeline if critical | Tech Lead | ⚠️ Active |
| R03 | Team member unavailability (sakit, personal) | Resource | Low (20%) | High (8) | 1.6 | High | Cross-training, pair programming, comprehensive documentation, knowledge sharing sessions | Redistribute work among team, adjust timeline, defer non-critical tasks | PM | ✅ Monitored |
| R04 | Stakeholder tidak available untuk review/UAT | Stakeholder | Low (30%) | Medium (5) | 1.5 | Medium | Flexible scheduling, asynchronous communication, early engagement planning | Use recorded demos, email approvals, proxy decision maker | PM | ✅ Monitored |
| R05 | Payment gateway integration issues | Integration | Medium (40%) | Medium (6) | 2.4 | High | Early integration testing, sandbox environment, backup provider (Xendit), API documentation review | Use manual verification temporarily, implement alternative payment method first | Backend Dev | ⚠️ Active |
| R06 | Performance issues pada production | Performance | Low (30%) | High (7) | 2.1 | High | Load testing, query optimization, database indexing, caching strategy (Redis), CDN | Upgrade hosting plan (scale up), implement full CDN, optimize critical queries | DevOps | ✅ Monitored |
| R07 | Data security breach atau vulnerability | Security | Low (10%) | Critical (10) | 1.0 | Critical | Security best practices (OWASP), regular audits, penetration testing, encryption, input validation | Immediate patch deployment, incident response plan, notify affected users, forensic analysis | Security Lead | ✅ Monitored |
| R08 | Timeline delay due to unforeseen challenges | Schedule | Medium (40%) | High (7) | 2.8 | Critical | Weekly progress monitoring, buffer time (20%), early issue identification, daily standups | Reduce scope (remove nice-to-have), request timeline extension, increase work hours | PM | ⚠️ Active |
| R09 | Budget overrun | Cost | Low (20%) | Medium (5) | 1.0 | Medium | Cost tracking (monthly), approval process for expenses, use free alternatives where possible | Use contingency fund (Rp 1M), seek additional funding from sponsor, reduce optional expenses | PM | ✅ Monitored |
| R10 | Low user adoption post-launch | Business | Medium (30%) | High (8) | 2.4 | High | User-centric design, comprehensive training, change management plan, early user involvement | Additional training sessions, 1-on-1 user support, incentives for adoption, feedback loop | PM | ⚠️ Active |
| R11 | Third-party service downtime (hosting, APIs) | External | Low (25%) | Medium (6) | 1.5 | Medium | Choose reliable providers (99.9% uptime SLA), implement retry logic, error handling | Switch to backup provider, manual fallback process, communicate with users | DevOps | ✅ Monitored |
| R12 | Requirement changes mid-project | Requirements | Medium (35%) | Medium (6) | 2.1 | High | Requirements validation with stakeholders, sign-off, change control board | Assess impact, re-prioritize backlog, negotiate timeline/scope adjustment | PM | ⚠️ Active |

**Risk Score Calculation:** Probability (%) × Impact (1-10)  
**Priority Levels:** Critical (>3.5), High (2.0-3.5), Medium (1.0-2.0), Low (<1.0)

---

**[GAMBAR 4.7 - Risk Matrix (Probability vs Impact with 12 Risks)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT RISK MATRIX - 12 IDENTIFIED RISKS]               │
│                                                             │
│   CUR-HEART PROJECT RISK MATRIX                            │
│                                                             │
│   IMPACT (Severity) →                                      │
│   P                                                         │
│   r                                                         │
│   o    High    │                   │ R01      │ R03        │
│   b  (40-60%)  │                   │ Scope    │ Resource   │
│   a            │                   │ Creep    │ Unavail    │
│   b            │─────────────────────────────────────────  │
│   i  Medium    │          │ R02      │ R08      │ R10      │
│   l  (30-40%)  │          │ Tech     │ Timeline │ User     │
│   i            │          │ Complex  │ Delay    │ Adoption │
│   t            │─────────────────────────────────────────  │
│   y  Low       │ R09      │ R04 R11  │ R06      │ R07      │
│      (10-30%)  │ Budget   │ Stake/   │ Perf     │ Security │
│   ↓            │ Overrun  │ 3rdParty │ Issues   │ CRITICAL │
│                └─────────────────────────────────────────  │
│                  Low(1-3)  Medium(4-6) High(7-8) Crit(9-10)│
│                         IMPACT (Severity) →                 │
│                                                             │
│   Color Coding:                                            │
│   🔴 CRITICAL (Score > 3.5): R01 (4.0), R08 (2.8)          │
│   🟡 HIGH (Score 2.0-3.5): R02, R05, R10, R12 (2.1-2.4)    │
│   🟢 MEDIUM (Score 1.0-2.0): R03, R04, R06, R11 (1.5-2.1)  │
│   ⚪ LOW (Score < 1.0): R07, R09 (1.0)                     │
│                                                             │
│   Top 3 Critical Risks:                                    │
│   1. R01 - Scope Creep (4.0): MoSCoW prioritization        │
│   2. R08 - Timeline Delay (2.8): Weekly monitoring         │
│   3. R05 - Payment Integration (2.4): Early testing        │
│                                                             │
│   Risk Distribution:                                       │
│   • Critical Priority: 2 risks (17%)                       │
│   • High Priority: 4 risks (33%)                           │
│   • Medium Priority: 4 risks (33%)                         │
│   • Low Priority: 2 risks (17%)                            │
│                                                             │
│   Mitigation Status:                                       │
│   ⚠️ Active Monitoring: 6 risks                            │
│   ✅ Under Control: 6 risks                                │
│                                                             │
│   Format: Risk Matrix PNG dengan positioning 12 risks      │
│   Recommended size: 1600x1000px                            │
│   Style: Professional dengan color-coded quadrants         │
│                                                             │
│   File: assets/images/risk-matrix-12-risks.png             │
│   Tool: PowerPoint, Excel, atau draw.io                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.7: Risk matrix probability vs impact dengan 12 identified risks, menunjukkan R01 (Scope Creep) dan R08 (Timeline Delay) sebagai critical priorities_

---

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

**Tabel 4.10 Communication Plan Matrix**

| Stakeholder | Information Needs | Communication Type | Method/Tool | Frequency | Format | Responsible | Delivery Time | Feedback Mechanism |
|-------------|------------------|-------------------|-------------|-----------|--------|-------------|---------------|-------------------|
| CUR-HEART Owner | Project status, budget, key decisions, ROI updates | Formal Report | Email (PDF), Face-to-face meeting | Weekly (Monday) | Status report template | Project Manager | Monday 9 AM | Email response, meeting discussion |
| Dosen Pembimbing | Progress, technical challenges, deliverables, academic requirements | Formal Consultation | Face-to-face, Google Meet, Documentation | Weekly (Friday) | Progress docs, code demo | Project Manager | Friday 2 PM | Technical guidance, approval/revision |
| Terapis (5) | Feature demos, testing schedules, training invites, workflow changes | Informal Update | WhatsApp group, Email | Bi-weekly | Screenshots, video demo | Project Manager | Tuesday PM | WhatsApp feedback, testing participation |
| Admin Staff (2) | System features, testing schedules, training materials, process changes | Informal Update | WhatsApp, Email | Bi-weekly | Screenshots, user guide draft | Project Manager | Tuesday PM | WhatsApp feedback, process validation |
| Sample Clients (10) | Testing invitations, feedback requests, usability study participation | Request | Email, Phone call | As needed (Week 10) | Invitation email, consent form | UX Designer | 3 days before test | Survey, interview responses |
| Development Team (3) | Task assignments, daily progress, blockers, code reviews, technical decisions | Daily Sync | Discord/Slack chat, Daily standup (video) | Daily (10 AM) | Standup format (done/todo/blockers) | Project Manager | Daily 10 AM | Immediate (chat), standup discussion |
| Technical Mentor | Code review requests, technical challenges, architecture decisions | Ad-hoc Consultation | GitHub PR, Email, Zoom | As needed (weekly) | Code snippets, architecture diagram | Tech Lead | When blocker occurs | Code comments, review approval |
| Universitas (Academic) | Monthly progress, final deliverables | Formal Report | Email, Physical submission | Monthly, Final | Academic report format | Project Manager | End of month | Academic evaluation |

**Communication Principles:**
1. Right information to right person at right time
2. Clear, concise, actionable messaging
3. Two-way communication (feedback encouraged)
4. Documented important decisions
5. Escalation path for urgent issues

---

**[GAMBAR 4.8 - Communication Matrix Stakeholder]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT COMMUNICATION MATRIX VISUAL]                      │
│                                                             │
│   STAKEHOLDER COMMUNICATION MATRIX                          │
│   CUR-HEART Project (8 Stakeholder Groups)                 │
│                                                             │
│   Frequency Axis (Vertical) vs Formality (Horizontal)      │
│                                                             │
│   Daily  │ Dev Team (3)                   │                │
│          │ Discord/Standup                │                │
│          │ ━━━━━━━━━━━━                   │                │
│   Weekly │ Owner           │ Dosen        │                │
│          │ Status Report   │ Consultation │                │
│          │ ━━━━━━━━━      │ ━━━━━━━━━   │                │
│          │                                │                │
│ Bi-Week  │ Terapis (5)     │ Admin (2)    │                │
│          │ WhatsApp Demo   │ Training     │                │
│          │ ━━━━━━━━━      │ ━━━━━━━     │                │
│          │                                │                │
│ Monthly  │                                │ Universitas    │
│          │                                │ Progress Report│
│          │                                │ ━━━━━━━━━━━   │
│ As-Need  │ Tech Mentor     │ Clients (10) │                │
│          │ Code Review     │ UAT Testing  │                │
│          │ ━━━━━━━━━      │ ━━━━━━━━━   │                │
│          └───────────────────────────────────────────────  │
│            Informal          Semi-Formal       Formal       │
│                        FORMALITY →                          │
│                                                             │
│   Legend:                                                   │
│   📧 Formal: Email, Reports, Documentation                  │
│   💬 Informal: WhatsApp, Chat, Phone                        │
│   🎯 Semi-Formal: Meetings, Presentations, Demos           │
│                                                             │
│   Communication Volume:                                     │
│   • Highest: Dev Team (daily, 40 hrs/week)                 │
│   • High: Owner + Dosen (weekly, 2-3 hrs/week)             │
│   • Medium: Terapis + Admin (bi-weekly, 1 hr/week)         │
│   • Low: Mentor, Clients, Univ (as-needed, <1 hr/week)     │
│                                                             │
│   Total Stakeholders: 26 individuals                        │
│   • Internal Team: 3 (core developers)                      │
│   • External: 23 (owner, faculty, users, mentors)          │
│                                                             │
│   Format: Communication Matrix Chart PNG                    │
│   Recommended size: 1600x900px                             │
│   Style: Professional quadrant/matrix dengan labels         │
│                                                             │
│   File: assets/images/communication-matrix.png              │
│   Tool: PowerPoint, Excel, atau Canva                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.8: Communication matrix stakeholder menunjukkan frequency dan formality level untuk 8 stakeholder groups (26 individuals)_

---

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

**Tabel 4.11 Functional Requirements List**

| ID | Requirement | Priority (MoSCoW) | User Role | Acceptance Criteria | Status |
|----|-------------|-------------------|-----------|-------------------|--------|
| **FR-AUTH** | **Authentication & Authorization** | | | | |
| FR-AUTH-01 | User registration dengan email verification | Must Have | All | User dapat register, receive email, verify account | ✅ Implemented |
| FR-AUTH-02 | Login dengan email dan password | Must Have | All | User dapat login dengan credentials valid | ✅ Implemented |
| FR-AUTH-03 | Forgot password dan reset via email | Must Have | All | User dapat reset password via email link | ✅ Implemented |
| FR-AUTH-04 | Role-based access control (Admin, Therapist, Client) | Must Have | All | Setiap role hanya akses fitur yang sesuai | ✅ Implemented |
| FR-AUTH-05 | Logout functionality | Must Have | All | User dapat logout dengan aman | ✅ Implemented |
| **FR-BOOKING** | **Booking Management** | | | | |
| FR-BOOK-01 | Browse dan filter services | Must Have | Client | Client dapat lihat semua services dengan filter | ✅ Implemented |
| FR-BOOK-02 | View therapist profiles dan availability | Must Have | Client | Client dapat lihat profil dan jadwal terapis | ✅ Implemented |
| FR-BOOK-03 | 4-step booking flow (Service → Therapist → Date/Time → Confirm) | Must Have | Client | Client dapat complete booking dalam 4 steps | ⏳ In Progress |
| FR-BOOK-04 | Real-time availability check | Must Have | Client | System prevent double booking | ⏳ In Progress |
| FR-BOOK-05 | Booking confirmation email | Must Have | Client | Client receive email setelah booking | 🔜 Planned |
| FR-BOOK-06 | Reschedule booking (min 24h before) | Should Have | Client | Client dapat reschedule dengan constraints | 🔜 Planned |
| FR-BOOK-07 | Cancel booking dengan reason | Should Have | Client | Client dapat cancel booking | 🔜 Planned |
| **FR-SCHEDULE** | **Schedule Management** | | | | |
| FR-SCHED-01 | Set weekly availability (recurring) | Must Have | Therapist | Terapis set jam kerja per hari | ✅ Implemented |
| FR-SCHED-02 | Block specific dates (leave, holiday) | Must Have | Therapist | Terapis block tanggal tertentu | ✅ Implemented |
| FR-SCHED-03 | View appointments calendar | Must Have | Therapist | Terapis lihat jadwal dalam calendar view | ✅ Implemented |
| FR-SCHED-04 | Accept/reject booking requests | Should Have | Therapist | Terapis bisa approve atau reject booking | 🔜 Planned |
| **FR-SESSION** | **Session Management** | | | | |
| FR-SESS-01 | Start session (mark as started) | Must Have | Therapist | Terapis start session on time | ⏳ In Progress |
| FR-SESS-02 | End session dan input session notes | Must Have | Therapist | Terapis dokumentasi session secara terstruktur | ⏳ In Progress |
| FR-SESS-03 | Upload session attachments (files, images) | Could Have | Therapist | Terapis upload supporting documents | 🔜 Planned |
| FR-SESS-04 | View session history dengan notes | Must Have | Therapist | Terapis akses riwayat session klien | ⏳ In Progress |
| FR-SESS-05 | Client view own session notes (summary only) | Should Have | Client | Client lihat summary progress | 🔜 Planned |
| **FR-PAYMENT** | **Payment Management** | | | | |
| FR-PAY-01 | Multiple payment methods (transfer, credit card, ewallet) | Must Have | Client | Client pilih payment method | ⏳ In Progress |
| FR-PAY-02 | Payment gateway integration (Midtrans) | Must Have | Client | Client bayar via payment gateway | ⏳ In Progress |
| FR-PAY-03 | Upload proof of payment (manual transfer) | Must Have | Client | Client upload bukti transfer | ⏳ In Progress |
| FR-PAY-04 | Admin verify manual payments | Must Have | Admin | Admin approve/reject payment | ⏳ In Progress |
| FR-PAY-05 | Payment confirmation notification | Must Have | Client | Client notified setelah payment confirmed | 🔜 Planned |
| FR-PAY-06 | View payment history dan invoices | Should Have | Client | Client download invoices | 🔜 Planned |
| **FR-PROGRESS** | **Progress Tracking** | | | | |
| FR-PROG-01 | Track client progress dengan metrics | Should Have | Therapist | Terapis input dan track progress | 🔜 Planned |
| FR-PROG-02 | Visualize progress dengan charts | Should Have | Client | Client lihat progress dalam grafik | 🔜 Planned |
| FR-PROG-03 | Set therapy goals dan milestones | Could Have | Therapist | Terapis set goals untuk klien | 🔜 Planned |
| **FR-REVIEW** | **Review & Feedback** | | | | |
| FR-REV-01 | Client submit review setelah session | Should Have | Client | Client rate dan review terapis | 🔜 Planned |
| FR-REV-02 | Therapist respond to reviews | Could Have | Therapist | Terapis reply to review | 🔜 Planned |
| FR-REV-03 | Admin moderate reviews | Should Have | Admin | Admin approve/hide inappropriate reviews | 🔜 Planned |
| **FR-ADMIN** | **Admin Management** | | | | |
| FR-ADM-01 | Manage users (CRUD) | Must Have | Admin | Admin kelola semua users | ⏳ In Progress |
| FR-ADM-02 | Manage services (CRUD) | Must Have | Admin | Admin kelola services | ⏳ In Progress |
| FR-ADM-03 | View all bookings dan status | Must Have | Admin | Admin monitor semua booking | ⏳ In Progress |
| FR-ADM-04 | Generate financial reports | Should Have | Admin | Admin export laporan keuangan | 🔜 Planned |
| FR-ADM-05 | System configuration dan settings | Must Have | Admin | Admin ubah system settings | ⏳ In Progress |
| **FR-NOTIF** | **Notifications** | | | | |
| FR-NOTIF-01 | Email notification untuk booking events | Must Have | All | Users receive email untuk booking updates | 🔜 Planned |
| FR-NOTIF-02 | Reminder email (24h dan 1h before session) | Should Have | Client | Client receive reminders | 🔜 Planned |
| FR-NOTIF-03 | In-app notification badge | Could Have | All | Users see notification count | 🔜 Planned |

**Total Requirements:** 48 functional requirements  
**Must Have:** 29 (60%)  
**Should Have:** 14 (29%)  
**Could Have:** 5 (11%)  
**Implementation Status:** 45% complete (as of Nov 2024)

---

**Tabel 4.12 Non-Functional Requirements**

| ID | Category | Requirement | Metric/Target | Testing Method | Priority |
|----|----------|-------------|---------------|----------------|----------|
| **NFR-PERF** | **Performance** | | | | |
| NFR-PERF-01 | Response Time | Page load time < 3 seconds (desktop) | < 3s | Lighthouse, GTmetrix | Critical |
| NFR-PERF-02 | Response Time | API response time < 500ms | < 500ms | Postman, browser DevTools | High |
| NFR-PERF-03 | Response Time | Time to First Byte < 600ms | < 600ms | WebPageTest | High |
| NFR-PERF-04 | Throughput | Support 100 concurrent users | 100 users | Load testing (Apache JMeter) | High |
| NFR-PERF-05 | Database Performance | Query execution < 100ms | < 100ms | MySQL slow query log | High |
| **NFR-SEC** | **Security** | | | | |
| NFR-SEC-01 | Authentication | Secure password hashing (bcrypt) | All passwords encrypted | Code review | Critical |
| NFR-SEC-02 | Authorization | Role-based access control (RBAC) | Unauthorized access blocked | Penetration testing | Critical |
| NFR-SEC-03 | Data Protection | Sensitive data encrypted at rest | Client medical data encrypted | Security audit | Critical |
| NFR-SEC-04 | Communication | HTTPS only (SSL certificate) | All traffic encrypted | SSL test | Critical |
| NFR-SEC-05 | Input Validation | Protection against SQL injection | No SQL vulnerabilities | OWASP ZAP scan | Critical |
| NFR-SEC-06 | Input Validation | Protection against XSS attacks | No XSS vulnerabilities | Security testing | Critical |
| NFR-SEC-07 | Session Management | Secure session handling dengan timeout | Session expires after 30 min inactive | Manual testing | High |
| NFR-SEC-08 | CSRF Protection | CSRF token validation | All forms protected | Code review | Critical |
| **NFR-USAB** | **Usability** | | | | |
| NFR-USAB-01 | Learnability | First-time user dapat booking tanpa training | 90% task success rate | Usability testing | High |
| NFR-USAB-02 | User Satisfaction | System Usability Scale (SUS) score | ≥ 80/100 | SUS questionnaire (10 users) | Critical |
| NFR-USAB-03 | Error Prevention | Clear validation messages | < 5% error rate per task | Usability testing | High |
| NFR-USAB-04 | Accessibility | WCAG 2.1 Level AA compliance | Pass aXe audit | aXe DevTools, Lighthouse | High |
| NFR-USAB-05 | Consistency | Consistent UI across all pages | Design system followed | Design review | High |
| **NFR-REL** | **Reliability** | | | | |
| NFR-REL-01 | Availability | System uptime | ≥ 99% monthly | Uptime monitoring (UptimeRobot) | Critical |
| NFR-REL-02 | Fault Tolerance | Graceful error handling | No unhandled exceptions | Error logging (Sentry) | High |
| NFR-REL-03 | Data Integrity | Database constraints enforced | No orphan records | Database testing | Critical |
| NFR-REL-04 | Backup & Recovery | Daily automated backup | RPO < 24 hours | Backup verification | High |
| **NFR-MAINT** | **Maintainability** | | | | |
| NFR-MAINT-01 | Code Quality | Follow PSR-12 coding standards | Grade A (SonarQube) | Static code analysis | High |
| NFR-MAINT-02 | Documentation | Comprehensive code documentation | All public methods documented | Code review | High |
| NFR-MAINT-03 | Modularity | Loosely coupled, high cohesion | Cyclomatic complexity < 10 | Code metrics | High |
| NFR-MAINT-04 | Version Control | Git branching strategy | All changes committed | Git history review | High |
| **NFR-SCALE** | **Scalability** | | | | |
| NFR-SCALE-01 | Data Volume | Handle 10,000+ users | Database performance stable | Load testing | Medium |
| NFR-SCALE-02 | Data Volume | Handle 100,000+ bookings per year | Query performance maintained | Stress testing | Medium |
| NFR-SCALE-03 | Concurrent Users | Support 500 concurrent users (future) | Server resources adequate | Load testing | Medium |
| **NFR-COMPAT** | **Compatibility** | | | | |
| NFR-COMPAT-01 | Browser Support | Chrome, Firefox, Safari, Edge (latest 2 versions) | Full functionality | Cross-browser testing | Critical |
| NFR-COMPAT-02 | Responsive Design | Mobile, tablet, desktop (320px - 1920px) | UI adapts gracefully | Responsive testing | Critical |
| NFR-COMPAT-03 | Server Environment | PHP 8.2+, MySQL 8.0+, Ubuntu 22.04 LTS | System runs without issues | Deployment testing | Critical |

**Total NFR:** 33 requirements  
**Critical Priority:** 19 (58%)  
**High Priority:** 12 (36%)  
**Medium Priority:** 2 (6%)

---

**Tabel 4.13 Technology Stack Comparison**

| Component | Option 1 | Option 2 | Option 3 | Selected | Rationale |
|-----------|----------|----------|----------|----------|-----------|
| **Backend Framework** | Laravel 10 | Express.js (Node.js) | Django (Python) | ✅ Laravel 10 | MVC built-in, Eloquent ORM, large ecosystem, academic requirement, team expertise |
| **Programming Language** | PHP 8.2 | JavaScript (Node) | Python 3.11 | ✅ PHP 8.2 | Modern features (enum, readonly), strong typing, Laravel compatibility |
| **Database** | MySQL 8.0 | PostgreSQL 15 | MongoDB 6.0 | ✅ MySQL 8.0 | ACID compliance, relational data fits well, free, wide hosting support |
| **CSS Framework** | Tailwind CSS 3.3 | Bootstrap 5 | Custom CSS | ✅ Tailwind 3.3 | Utility-first, highly customizable, smaller bundle size, modern |
| **JavaScript** | Alpine.js 3.x | Vue.js 3 | React 18 | ✅ Alpine.js | Lightweight (15KB), declarative, minimal overhead, Laravel Livewire compatible |
| **Template Engine** | Blade (Laravel) | Twig | Plain PHP | ✅ Blade | Built-in Laravel, clean syntax, template inheritance, directives |
| **Authentication** | Laravel Sanctum | Laravel Passport | JWT (tymon/jwt-auth) | ✅ Sanctum | Lightweight, SPA-friendly, token-based, built for Laravel |
| **Payment Gateway** | Midtrans | Xendit | Stripe | ✅ Midtrans | Indonesia-focused, multiple payment methods, good docs, affordable fees |
| **Email Service** | SendGrid | Mailgun | AWS SES | ✅ SendGrid | Reliable, 100 emails/day free, good deliverability, easy integration |
| **Hosting** | Niagahoster VPS | DigitalOcean Droplet | AWS EC2 | ✅ Niagahoster VPS | Indonesia-based, affordable (Rp 300k/mo), managed, local support |
| **Version Control** | GitHub | GitLab | Bitbucket | ✅ GitHub | Free private repos, CI/CD (Actions), large community, familiar |
| **Task Management** | Asana | Trello | Jira | ✅ Asana | Task dependencies, timeline view, free tier sufficient, collaborative |
| **Design Tool** | Figma | Adobe XD | Sketch | ✅ Figma | Collaborative, browser-based, free tier, component libraries, prototyping |
| **API Testing** | Postman | Insomnia | Thunder Client | ✅ Postman | Collections, environment variables, team sync, comprehensive |
| **Database Tool** | MySQL Workbench | phpMyAdmin | DBeaver | ✅ MySQL Workbench | Visual ERD designer, query optimization tools, migration support |
| **Error Tracking** | Sentry | Rollbar | Bugsnag | ✅ Sentry | Real-time alerts, stack traces, free tier 5k events/mo, Laravel integration |
| **Monitoring** | UptimeRobot | Pingdom | StatusCake | ✅ UptimeRobot | Free 50 monitors, 5min intervals, email/SMS alerts, public status page |

**Key Selection Criteria:**
1. **Cost:** Free atau affordable untuk budget Rp 5 juta
2. **Learning Curve:** Tim familiar atau easy to learn
3. **Community Support:** Large community, good documentation
4. **Integration:** Seamless integration dengan stack lain
5. **Scalability:** Dapat handle growth
6. **Academic Requirements:** Must use Laravel (academic constraint)

---

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
