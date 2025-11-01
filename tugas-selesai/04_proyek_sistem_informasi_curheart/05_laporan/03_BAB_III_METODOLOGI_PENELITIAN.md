# BAB III  
# METODOLOGI PENELITIAN

## 3.1 Tahapan Penelitian

Penelitian dan pengembangan sistem informasi manajemen booking dan terapi CUR-HEART menggunakan pendekatan **System Development Life Cycle (SDLC)** dengan model **Waterfall**. Model ini dipilih karena nature proyek yang memiliki requirements jelas, timeline tetap (semester akademik), dan memerlukan dokumentasi komprehensif untuk keperluan akademik. Tahapan penelitian terdiri dari enam fase utama yang dilaksanakan secara sekuensial dengan output yang terdefinisi jelas di setiap fase.

### 3.1.1 Fase 1: Analisis Kebutuhan (Requirements Analysis)

**Durasi:** Minggu 1-2 (14 hari)

**Tujuan:**
Memahami secara mendalam kebutuhan bisnis CUR-HEART, mengidentifikasi permasalahan dalam sistem existing, dan mendefinisikan requirements untuk sistem baru baik fungsional maupun non-fungsional.

**Aktivitas:**

1. **Studi Pendahuluan:**
   - Mengkaji literatur tentang sistem informasi kesehatan mental, hypnotherapy practice management, dan booking systems
   - Mempelajari best practices dalam pengembangan healthcare information systems
   - Memahami regulatory requirements untuk data protection (UU PDP Indonesia)
   - Benchmarking terhadap sistem sejenis yang sudah ada (lokal dan internasional)

2. **Observasi Lapangan:**
   - Mengamati proses bisnis existing di CUR-HEART dari booking hingga completion sesi terapi
   - Mengidentifikasi pain points, bottlenecks, dan inefficiencies dalam workflow current
   - Mendokumentasikan business processes dengan flowchart atau business process diagram
   - Mengambil sample forms dan documents yang currently digunakan

3. **Wawancara dengan Stakeholders:**
   - **Interview dengan Owner/Manajemen CUR-HEART:**
     - Vision dan strategic goals untuk digitalisasi
     - Key performance indicators yang ingin improved
     - Budget constraints dan timeline expectations
     - Success criteria untuk proyek
   
   - **Interview dengan Terapis:**
     - Daily workflow dan challenges dalam manajemen jadwal
     - Documentation requirements untuk sesi terapi
     - Information needs untuk client management
     - Desired features dalam sistem baru
   
   - **Interview dengan Admin/Staff:**
     - Current process untuk handling bookings dan inquiries
     - Common issues atau complaints dari klien
     - Time-consuming administrative tasks yang ingin diotomasi
     - Reporting needs untuk management
   
   - **Interview dengan Sample Klien:**
     - Experience dengan current booking process
     - Pain points dan areas for improvement
     - Expectations untuk online booking system
     - Privacy dan security concerns

4. **Analisis Dokumen:**
   - Review existing documentation (SOPs, forms, reports)
   - Analisis data historis (booking volumes, revenue, client demographics)
   - Identifikasi data yang perlu dimigrate ke sistem baru

5. **Requirement Elicitation:**
   - Brainstorming session dengan stakeholders untuk identify requirements
   - Prioritization requirements menggunakan MoSCoW method (Must have, Should have, Could have, Won't have)
   - Dokumentasi functional requirements (what system should do)
   - Dokumentasi non-functional requirements (performance, security, usability, etc.)

**Output:**

- Software Requirements Specification (SRS) Document yang mencakup:
  - Executive Summary
  - Current System Analysis (As-Is)
  - Problem Statement
  - Proposed System (To-Be)
  - Functional Requirements dengan use case descriptions
  - Non-Functional Requirements (performance, security, reliability, etc.)
  - Assumptions dan Constraints
  - Success Criteria
- Feasibility Study Report (Technical, Economic, Operational feasibility)
- Business Process Flowcharts (As-Is vs To-Be)
- Interview Transcripts dan Summary
- Observation Notes

### 3.1.2 Fase 2: Desain Sistem (System Design)

**Durasi:** Minggu 3-4 (14 hari)

**Tujuan:**
Merancang arsitektur sistem, database schema, user interface, dan spesifikasi teknis yang akan menjadi blueprint untuk implementasi.

**Aktivitas:**

1. **Desain Arsitektur Sistem:**
   - Mendefinisikan system architecture (monolithic Laravel application)
   - Menentukan tech stack (Laravel 10.x, PHP 8.x, MySQL 8.0, Tailwind CSS)
   - Desain deployment architecture (server requirements, hosting environment)
   - Network dan security architecture design

2. **Desain Database:**
   - **Entity Identification:**
     Mengidentifikasi entities utama seperti Users, Therapists, Clients, Services, Bookings, Sessions, Payments, Reviews, etc.
   
   - **Entity Relationship Diagram (ERD):**
     Merancang ERD yang menunjukkan entities, attributes, dan relationships (one-to-one, one-to-many, many-to-many)
   
   - **Normalization:**
     Menerapkan normalisasi hingga Third Normal Form (3NF) untuk mengurangi redundansi dan menjaga integrity
   
   - **Database Schema Design:**
     Mendefinisikan tables dengan columns, data types, constraints (primary key, foreign key, unique, not null), dan indexes
   
   - **Migration Scripts:**
     Merancang Laravel migration files untuk version control database schema

3. **Desain Interface (UI/UX):**
   - **User Research:**
     Memahami user personas (admin, therapist, client) dan their goals
   
   - **Information Architecture:**
     Merancang site map dan navigation structure
   
   - **Wireframing:**
     Membuat low-fidelity wireframes untuk key pages dan flows
   
   - **High-Fidelity Mockup:**
     Merancang detailed mockups dengan actual colors, typography, images
     Menggunakan design system yang sudah ada (41 mockup pages)
   
   - **Responsive Design:**
     Ensuring designs work pada mobile, tablet, dan desktop views
   
   - **Accessibility Considerations:**
     Color contrast, font sizes, keyboard navigation, screen reader compatibility

4. **Desain Proses (UML Diagrams):**
   - **Use Case Diagram:**
     Menunjukkan actors (Admin, Therapist, Client) dan their interactions dengan system (use cases)
   
   - **Activity Diagram:**
     Menggambarkan workflow atau business processes seperti booking flow, payment flow, session documentation flow
   
   - **Sequence Diagram:**
     Menunjukkan interaction antar objects/components dalam specific scenarios (e.g., booking creation sequence)
   
   - **Class Diagram (Optional):**
     Menunjukkan classes dalam system dengan attributes, methods, dan relationships

5. **Desain Keamanan:**
   - Authentication mechanism design (Laravel Sanctum/built-in auth)
   - Authorization design (role-based access control)
   - Data encryption strategy untuk sensitive information
   - Security measures untuk common vulnerabilities (CSRF, XSS, SQL Injection)
   - Session management dan timeout policies
   - Audit logging design

6. **API Design (jika diperlukan):**
   - RESTful endpoint design untuk potential future integrations
   - Request/Response formats (JSON)
   - Authentication untuk API (tokens)

**Output:**

- System Design Document (SDD) yang mencakup:
  - System Architecture Diagram
  - Technology Stack Description
  - Deployment Architecture
- Database Design Document:
  - Entity Relationship Diagram (ERD)
  - Database Schema dengan detailed table definitions
  - Data Dictionary
  - Sample Migration Scripts
- UI/UX Design Document:
  - Wireframes (low-fidelity)
  - High-Fidelity Mockups (41 pages)
  - Design System Documentation (colors, typography, components)
  - User Flow Diagrams
- UML Diagrams:
  - Use Case Diagrams
  - Activity Diagrams
  - Sequence Diagrams
  - Class Diagrams (if applicable)
- Security Design Document
- API Specification Document (if applicable)

### 3.1.3 Fase 3: Implementasi (Implementation/Development)

**Durasi:** Minggu 5-8 (28 hari)

**Tujuan:**
Mengembangkan sistem informasi sesuai dengan design specifications yang telah dibuat pada fase sebelumnya.

**Aktivitas:**

1. **Environment Setup:**
   - Setting up development environment (XAMPP/Laragon, VS Code, Git)
   - Installing Laravel 10.x dan dependencies (Composer packages)
   - Configuring database (MySQL)
   - Installing frontend dependencies (Node.js, NPM, Tailwind CSS)
   - Setting up version control (Git repository)

2. **Database Implementation:**
   - Creating database dan tables menggunakan Laravel migrations
   - Setting up relationships dalam Eloquent models
   - Creating seeders untuk sample data
   - Testing database connections dan queries

3. **Backend Development:**
   - **Authentication System:**
     - Implementing user registration (multi-role: admin, therapist, client)
     - Login/logout functionality dengan session management
     - Email verification
     - Password reset functionality
     - Profile management
   
   - **Models Development:**
     - Creating Eloquent models untuk setiap entity
     - Defining relationships (hasOne, hasMany, belongsTo, belongsToMany)
     - Implementing accessors dan mutators jika diperlukan
     - Adding validation rules
   
   - **Controllers Development:**
     - Creating controllers untuk setiap module (BookingController, UserController, PaymentController, etc.)
     - Implementing CRUD operations (Create, Read, Update, Delete)
     - Handling form submissions dan validations
     - Preparing data untuk views
   
   - **Business Logic Implementation:**
     - Booking flow logic (service selection, therapist selection, scheduling, confirmation)
     - Availability checking algorithms
     - Payment processing integration
     - Notification triggers (email, SMS)
     - Reporting dan analytics logic
   
   - **Middleware Implementation:**
     - Role-based access control middleware
     - Authentication middleware untuk protected routes
     - Custom middleware untuk specific needs
   
   - **Service Layer (Optional):**
     - Extracting complex business logic kedalam service classes untuk reusability dan testability

4. **Frontend Development:**
   - **Layout Templates:**
     - Creating master layout dengan Blade
     - Header, sidebar, footer components
     - Responsive navigation menu
   
   - **Public Pages:**
     - Landing page dengan hero section, services overview, testimonials
     - About page
     - Services catalog page
     - Therapists directory page
     - Blog/articles pages
     - Contact dan FAQ pages
   
   - **Authentication Pages:**
     - Login page dengan form validation
     - Registration page (separate untuk client dan therapist)
     - Forgot password page
     - Reset password page
   
   - **Client Dashboard:**
     - Dashboard overview dengan summary cards
     - Booking flow (4 steps: service, therapist, schedule, confirmation)
     - My appointments (list dan calendar views)
     - Booking history
     - Progress tracking dengan charts
     - Messages inbox
     - Payment history
   
   - **Therapist Dashboard:**
     - Dashboard overview dengan statistics
     - Schedule management (calendar view)
     - Availability settings
     - Clients list dengan details
     - Session room interface
     - Session notes editor dengan templates
     - Session history
     - Earnings dashboard dengan charts
     - Profile settings
   
   - **Admin Dashboard:**
     - Dashboard overview dengan KPIs
     - Users management (CRUD operations)
     - Therapists approval dan management
     - Services management
     - Bookings management
     - Payments verification
     - Financial reports dengan visualizations
     - System settings
   
   - **Styling dengan Tailwind CSS:**
     - Applying utility classes untuk styling
     - Ensuring responsive design across devices
     - Customizing Tailwind configuration untuk brand colors dan styles
     - Creating reusable components
   
   - **Interactive Elements dengan JavaScript:**
     - Form validations
     - Dynamic calendar interactions
     - Modal dialogs
     - AJAX requests untuk asynchronous operations
     - Charts dan visualizations (Chart.js atau ApexCharts)

5. **Integration:**
   - **Payment Gateway Integration:**
     - Integrating dengan Midtrans atau Xendit untuk online payments
     - Configuring webhooks untuk payment notifications
     - Testing payment flows (sandbox environment)
   
   - **Email Service Integration:**
     - Configuring SMTP untuk email sending
     - Creating email templates (notification, verification, receipt)
     - Testing email deliverability
   
   - **SMS Service Integration (Optional):**
     - Integrating dengan SMS gateway untuk SMS notifications
     - Creating SMS templates
   
   - **Video Conference Integration (Optional):**
     - Embedding Zoom, Google Meet, atau Whereby untuk session rooms

6. **Code Quality Assurance:**
   - Code review dan refactoring
   - Following Laravel best practices dan coding standards
   - Commenting code untuk better maintainability
   - Version control commits dengan meaningful messages

**Output:**

- Functional Web Application:
  - Backend code (Models, Controllers, Middleware, Services)
  - Frontend code (Blade views, CSS, JavaScript)
  - Database dengan sample data
- Source Code Repository (GitHub) dengan proper commit history
- Configuration Files dan Environment Variables documentation
- API Integration Documentation (Payment Gateway, Email, SMS)

### 3.1.4 Fase 4: Pengujian (Testing)

**Durasi:** Minggu 9-10 (14 hari)

**Tujuan:**
Memastikan bahwa sistem bekerja dengan benar, memenuhi requirements, bebas dari critical bugs, dan memberikan user experience yang baik.

**Aktivitas:**

1. **Unit Testing:**
   - Testing individual functions atau methods
   - Menggunakan PHPUnit (built-in Laravel testing framework)
   - Writing test cases untuk critical business logic
   - Ensuring code coverage pada core functionalities
   - Automated testing untuk regression prevention

2. **Integration Testing:**
   - Testing interactions antar modules atau components
   - Testing database operations (CRUD)
   - Testing API integrations (payment gateway, email service)
   - Testing authentication dan authorization flows

3. **Functional Testing (Black-Box Testing):**
   - **Test Plan Creation:**
     - Defining test scenarios berdasarkan functional requirements
     - Creating test cases dengan expected outcomes
   
   - **Test Execution:**
     - Testing semua fitur sesuai test cases:
       - Authentication (registration, login, logout, password reset)
       - Booking flow (semua 4 steps)
       - Appointment management (create, view, reschedule, cancel)
       - Therapist scheduling
       - Session documentation
       - Payment processing
       - Notifications (email verification, booking confirmation, reminders)
       - Dashboard features (statistics, charts)
       - Admin operations (user management, service management, reporting)
   
   - **Bug Tracking:**
     - Documenting bugs yang ditemukan dengan details (steps to reproduce, expected vs actual behavior, severity)
     - Prioritizing bugs (critical, major, minor, trivial)
     - Tracking bug fixing progress

4. **Usability Testing:**
   - **Participant Recruitment:**
     - Recruiting sample users (potential clients, therapists, admin)
     - Total 10-15 participants representing different user roles
   
   - **Test Scenarios:**
     - Defining tasks untuk participants (e.g., "Book a therapy session", "Check your appointments")
   
   - **Test Execution:**
     - Observing participants saat menggunakan sistem
     - Recording time to complete tasks, success rate, errors made
     - Noting areas of confusion atau difficulty
   
   - **Feedback Collection:**
     - Post-test questionnaire (System Usability Scale - SUS)
     - Interview untuk gather qualitative feedback
     - Suggestions untuk improvements
   
   - **Analysis:**
     - Analyzing usability metrics
     - Identifying UI/UX issues
     - Prioritizing improvements

5. **Performance Testing:**
   - **Load Testing:**
     - Simulating multiple concurrent users
     - Testing system performance under expected load
   
   - **Stress Testing:**
     - Testing system limits dengan extreme load
     - Identifying breaking points
   
   - **Response Time Testing:**
     - Measuring page load times
     - Ensuring acceptable performance (< 3 seconds untuk most pages)
   
   - **Database Query Optimization:**
     - Identifying slow queries dengan Laravel Debugbar
     - Optimizing queries dengan proper indexing dan query optimization

6. **Security Testing:**
   - **Vulnerability Scanning:**
     - Testing untuk common vulnerabilities (SQL Injection, XSS, CSRF)
     - Using automated tools (OWASP ZAP, Burp Suite Community Edition)
   
   - **Penetration Testing (Basic):**
     - Attempting unauthorized access
     - Testing authentication bypass
     - Testing authorization violations (access control)
   
   - **Code Review untuk Security:**
     - Reviewing code untuk security best practices
     - Ensuring sensitive data encryption
     - Validating input sanitization

7. **User Acceptance Testing (UAT):**
   - **UAT Planning:**
     - Preparing UAT plan dan test cases
     - Scheduling UAT sessions dengan CUR-HEART stakeholders
   
   - **UAT Execution:**
     - Presenting sistem kepada stakeholders
     - Stakeholders testing system dengan real scenarios
     - Collecting feedback dan approval
   
   - **Sign-off:**
     - Obtaining formal approval dari stakeholders
     - Documenting any last-minute change requests

8. **Bug Fixing dan Retesting:**
   - Prioritizing dan fixing critical dan major bugs
   - Retesting fixed bugs untuk ensure resolution
   - Regression testing untuk ensure fixes didn't break other features
   - Iterative testing cycle hingga acceptable quality achieved

**Output:**

- Test Plan Document
- Test Cases dengan detailed steps dan expected results
- Test Results Report dengan pass/fail status
- Bug Report dengan descriptions, screenshots, severity levels
- Usability Testing Report dengan SUS scores dan feedback summary
- Performance Testing Report dengan response times dan load capacities
- Security Audit Report
- UAT Report dengan stakeholder sign-off
- Fixed dan Tested Application ready untuk deployment

### 3.1.5 Fase 5: Deployment (Implementasi di Production)

**Durasi:** Minggu 11 (7 hari)

**Tujuan:**
Men-deploy sistem ke production environment sehingga dapat diakses dan digunakan oleh end-users secara real.

**Aktivitas:**

1. **Pre-Deployment Preparation:**
   - Final code review dan cleanup
   - Updating documentation (README, deployment guide, user manual)
   - Preparing release notes
   - Creating backup plan dan rollback procedures
   - Testing deployment process di staging environment (jika ada)

2. **Production Environment Setup:**
   - **Server Provisioning:**
     - Setting up web server (Apache atau Nginx)
     - Installing PHP 8.x dengan required extensions
     - Installing MySQL 8.0
     - Configuring firewall dan security settings
   
   - **Domain dan SSL:**
     - Configuring domain name (curheart.com atau subdomain)
     - Installing SSL certificate untuk HTTPS (Let's Encrypt)
   
   - **Application Deployment:**
     - Uploading source code ke server (via FTP, Git, atau SSH)
     - Installing Composer dependencies (`composer install --optimize-autoloader --no-dev`)
     - Installing NPM dependencies dan building assets (`npm install && npm run build`)
     - Setting up environment variables (`.env` file dengan production settings)
     - Running database migrations (`php artisan migrate --force`)
     - Seeding initial data jika diperlukan (`php artisan db:seed`)
     - Setting proper file permissions
     - Configuring cron jobs untuk Laravel Scheduler
     - Configuring queue workers untuk background jobs

3. **Configuration:**
   - **Application Configuration:**
     - Setting APP_ENV=production
     - Setting APP_DEBUG=false untuk security
     - Configuring cache drivers (file, Redis, atau Memcached)
     - Configuring session dan queue drivers
   
   - **Database Configuration:**
     - Creating production database
     - Configuring database credentials di `.env`
     - Optimizing database settings untuk production
   
   - **Third-Party Services Configuration:**
     - Configuring payment gateway dengan production API keys
     - Configuring email service dengan production SMTP settings
     - Configuring SMS service (jika ada)
     - Setting up webhooks untuk payment notifications

4. **Testing di Production Environment:**
   - Smoke testing semua critical features
   - Testing integrations (payment, email, SMS)
   - Testing dari different devices dan browsers
   - Ensuring SSL working properly
   - Testing performance dan response times

5. **Monitoring Setup:**
   - Setting up error logging (Laravel log files)
   - Configuring exception reporting (e.g., Sentry, Bugsnag)
   - Setting up uptime monitoring (e.g., UptimeRobot)
   - Configuring server monitoring (CPU, RAM, disk usage)
   - Setting up backup automated backups (daily database backups)

6. **Go-Live:**
   - Final checks before launch
   - Announcing go-live kepada stakeholders
   - Monitoring closely untuk any issues
   - Being ready untuk quick fixes jika ada critical issues

7. **Post-Deployment Activities:**
   - **User Training:**
     - Conducting training sessions untuk admin dan therapists
     - Providing user manuals dan video tutorials
     - Creating FAQ dan troubleshooting guides
   
   - **Data Migration (jika ada):**
     - Migrating data dari sistem lama (jika applicable)
     - Verifying data integrity post-migration
   
   - **Announcement kepada Clients:**
     - Informing existing clients tentang sistem baru
     - Providing instructions untuk registration dan booking
     - Offering support untuk onboarding

**Output:**

- Live Web Application accessible via domain dengan HTTPS
- Deployment Documentation (server setup, configuration, deployment steps)
- Rollback Plan dan Procedures
- User Manuals (Admin Manual, Therapist Manual, Client Manual)
- Training Materials (presentations, video tutorials)
- Monitoring dan Logging System configured
- Backup System configured dan tested

### 3.1.6 Fase 6: Maintenance dan Evaluasi (Ongoing)

**Durasi:** Post-deployment (Continuous)

**Tujuan:**
Memastikan sistem tetap berjalan dengan baik, mengatasi issues yang muncul, dan melakukan improvements berdasarkan feedback users.

**Aktivitas:**

1. **Monitoring dan Logging:**
   - Daily monitoring system uptime dan performance
   - Reviewing error logs untuk identify issues
   - Monitoring server resources (CPU, RAM, disk, bandwidth)
   - Tracking application metrics (users, bookings, revenue)

2. **Bug Fixing:**
   - Responding to bug reports dari users
   - Prioritizing bugs based on severity dan impact
   - Developing fixes dan deploying patches
   - Communicating dengan users tentang bug resolutions

3. **User Support:**
   - Providing technical support kepada users
   - Answering questions via email, phone, atau live chat
   - Creating knowledge base articles untuk common issues
   - Collecting feedback dan feature requests

4. **Performance Optimization:**
   - Identifying performance bottlenecks
   - Optimizing slow database queries
   - Implementing caching strategies (query caching, view caching, route caching)
   - Image optimization
   - Code optimization

5. **Security Updates:**
   - Applying security patches untuk Laravel dan dependencies
   - Monitoring untuk security vulnerabilities
   - Updating SSL certificates before expiry
   - Regular security audits

6. **Backup dan Disaster Recovery:**
   - Ensuring automated backups running properly
   - Testing backup restoration periodically
   - Maintaining disaster recovery plan

7. **Feature Enhancements:**
   - Evaluating feature requests dari users
   - Prioritizing enhancements based on value dan effort
   - Developing dan deploying new features incrementally
   - Communicating updates kepada users

8. **Evaluation dan Reporting:**
   - **Metrics Collection:**
     - Collecting usage metrics (daily active users, booking volumes, conversion rates)
     - Measuring system performance (uptime, response times)
     - Tracking business metrics (revenue, customer satisfaction)
   
   - **Analysis:**
     - Analyzing trends dan patterns
     - Identifying areas for improvement
     - Calculating ROI dari sistem
   
   - **Reporting:**
     - Creating monthly reports untuk management
     - Presenting findings dan recommendations
     - Celebrating successes dan addressing challenges

9. **Continuous Improvement:**
   - Regularly reviewing system dan process
   - Implementing lessons learned
   - Staying updated dengan Laravel updates dan best practices
   - Planning untuk future enhancements dan scalability

**Output:**

- Monthly Maintenance Reports
- Bug Fix Logs dengan resolutions
- Performance Metrics Reports
- User Satisfaction Survey Results
- Feature Enhancement Roadmap
- Updated Documentation
- System Health Dashboard

---

## 3.2 Tempat dan Waktu Penelitian

### 3.2.1 Tempat Penelitian

Penelitian dan pengembangan sistem informasi ini dilaksanakan di beberapa lokasi:

1. **CUR-HEART (Hypnotherapy & Mind Wellness Center)**
   - Alamat: [Alamat CUR-HEART - dapat disesuaikan dengan lokasi aktual]
   - Kegiatan: Observasi proses bisnis, wawancara dengan stakeholders, user acceptance testing
   - Periode: Minggu 1-2 (Analisis Kebutuhan) dan Minggu 10 (UAT)

2. **Universitas Nusa Mandiri - Kampus Margonda**
   - Alamat: Jl. Margonda Raya No. 100, Depok, Jawa Barat
   - Kegiatan: Development, konsultasi dengan dosen pembimbing, koordinasi tim
   - Periode: Minggu 1-11 (Sepanjang proyek)

3. **Remote/Online (Work From Home)**
   - Kegiatan: Development, documentation, testing, koordinasi tim via online tools
   - Periode: Mayoritas waktu development (Minggu 3-9)

### 3.2.2 Waktu Penelitian

Penelitian dilaksanakan dalam satu semester akademik dengan total durasi 11 minggu, dari pertengahan September 2024 hingga awal Desember 2024. Breakdown jadwal sebagai berikut:

| No | Fase | Minggu | Tanggal Mulai | Tanggal Selesai | Durasi (Hari) |
|----|------|--------|---------------|-----------------|---------------|
| 1 | Analisis Kebutuhan | 1-2 | 16 Sep 2024 | 29 Sep 2024 | 14 |
| 2 | Desain Sistem | 3-4 | 30 Sep 2024 | 13 Okt 2024 | 14 |
| 3 | Implementasi | 5-8 | 14 Okt 2024 | 10 Nov 2024 | 28 |
| 4 | Pengujian | 9-10 | 11 Nov 2024 | 24 Nov 2024 | 14 |
| 5 | Deployment | 11 | 25 Nov 2024 | 1 Des 2024 | 7 |
| 6 | Maintenance & Evaluasi | Ongoing | 2 Des 2024 | Berkelanjutan | - |

**Catatan:**
- Minggu 12-15: Finalisasi dokumentasi laporan dan persiapan presentasi
- Minggu 15: Presentasi Final Project

**Gantt Chart:**

```
Fase                  | Minggu
                      | 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
-------------------------------------------------------------------
Analisis Kebutuhan    |███████
Desain Sistem         |       ███████
Implementasi          |              ██████████████████████████
Pengujian             |                                      ███████████████
Deployment            |                                                 ████████
Dokumentasi Laporan   |                                                         ████████████████
Persiapan Presentasi  |                                                                     ████████
Presentasi Final      |                                                                             ██
```

## 3.3 Subjek Penelitian

Subjek penelitian dalam pengembangan sistem informasi CUR-HEART terdiri dari beberapa kategori stakeholders yang terlibat langsung dalam sistem:

### 3.3.1 Stakeholder Internal CUR-HEART

1. **Owner/Manajemen CUR-HEART (1 orang)**
   - Role: Decision maker, approver
   - Involvement: Interview untuk understanding business goals, requirements approval, UAT, final sign-off

2. **Terapis (3-5 orang)**
   - Role: Primary users dari therapist dashboard
   - Involvement: Interview untuk understanding workflow dan pain points, requirements definition untuk therapist features, usability testing, UAT, user training

3. **Admin/Staff (1-2 orang)**
   - Role: Primary users dari admin dashboard, system operator
   - Involvement: Interview untuk understanding administrative processes, requirements definition untuk admin features, usability testing, UAT, user training

### 3.3.2 External Users (Klien)

4. **Sample Klien (5-10 orang)**
   - Role: Potensial users dari client-facing features
   - Demographics: Diverse age groups (25-45 tahun), tech-savviness levels, gender
   - Involvement: Interview untuk understanding needs dan expectations, usability testing, UAT, feedback collection

### 3.3.3 Tim Pengembang

5. **Mahasiswa Pengembang (3 orang)**
   - Roki Anjas (11250066) - Project Leader, Backend Developer
   - Susanto (11250068) - Frontend Developer, UI/UX Designer
   - Fahruroji (11250085) - Full-Stack Developer, Database Administrator

6. **Dosen Pembimbing (1 orang)**
   - Rani Irma Handayani, M.Kom
   - Role: Academic supervisor, technical advisor
   - Involvement: Weekly consultation, progress monitoring, technical guidance, final evaluation

### 3.3.4 Kriteria Partisipan Usability Testing

Untuk usability testing phase, participants direkrut dengan kriteria:

**Therapist Participants (3 orang):**
- Berpengalaman dalam praktik terapi minimal 1 tahun
- Familiar dengan penggunaan komputer/smartphone
- Bersedia memberikan honest feedback

**Client Participants (5 orang):**
- Pernah atau berencana menggunakan layanan terapi kesehatan mental
- Beragam dalam age, gender, dan tech-savviness
- Bersedia mengikuti usability testing session (1-2 jam)

**Admin Participants (2 orang):**
- Berpengalaman dalam administrative tasks atau customer service
- Familiar dengan sistem booking atau appointment management
- Bersedia memberikan feedback untuk improvements

## 3.4 Teknik Pengumpulan Data

Pengumpulan data dalam penelitian ini menggunakan multiple methods untuk ensure comprehensive understanding dan validation dari berbagai perspektif.

### 3.4.1 Observasi

**Jenis Observasi:**
Observasi partisipatif dan non-partisipatif terhadap proses bisnis existing di CUR-HEART.

**Prosedur:**

1. **Persiapan:**
   - Menyiapkan observation checklist berdasarkan areas of interest
   - Meminta izin formal dari CUR-HEART untuk melakukan observasi
   - Menjelaskan tujuan observasi kepada staff yang akan diobservasi

2. **Pelaksanaan:**
   - Mengamati proses booking dari client inquiry hingga confirmation (1-2 hari)
   - Mengamati workflow terapis dari preparing session hingga documentation (1-2 hari)
   - Mengamati administrative tasks yang dilakukan staff (1-2 hari)
   - Taking detailed notes atau recording (dengan izin)
   - Taking photos dari forms, documents, atau workspace (dengan izin)

3. **Dokumentasi:**
   - Mendokumentasikan observations dalam observation notes
   - Creating process flowcharts berdasarkan observed workflows
   - Identifying pain points, inefficiencies, atau improvement opportunities

**Aspek yang Diobservasi:**

- Langkah-langkah dalam booking process
- Tools dan media yang digunakan (WhatsApp, Excel, kalender manual)
- Time taken untuk each step
- Communication patterns antara client, admin, dan therapist
- Documentation methods untuk session notes
- Data storage dan retrieval processes
- Error handling atau exception scenarios

**Output:**
- Observation Notes dengan timestamps dan details
- Process Flowcharts (As-Is)
- Photos atau screenshots dari current tools/forms
- List of pain points dan improvement opportunities

### 3.4.2 Wawancara (Interview)

**Jenis Wawancara:**
Semi-structured interview yang mengkombinasikan prepared questions dengan flexibility untuk follow-up questions berdasarkan responses.

**Prosedur:**

1. **Persiapan:**
   - Developing interview guide dengan key questions untuk each stakeholder group
   - Scheduling interviews dengan participants
   - Preparing recording tools (audio recorder atau note-taking app) dengan participant consent

2. **Pelaksanaan:**
   - Conducting one-on-one interviews (30-60 menit per participant)
   - Starting dengan introduction dan explaining purpose
   - Asking prepared questions dan allowing participants untuk elaborate
   - Following up dengan probing questions untuk clarification atau deeper insights
   - Recording interviews atau taking detailed notes

3. **Dokumentasi:**
   - Transcribing interview recordings
   - Organizing responses by themes atau topics
   - Identifying common patterns, unique insights, atau conflicting views

**Interview Questions (Sample):**

**Untuk Owner/Manajemen:**
1. Apa visi Anda untuk digitalisasi CUR-HEART?
2. Apa KPIs yang ingin Anda improve dengan sistem baru?
3. Apa biggest challenges yang dihadapi dalam operasional saat ini?
4. Apa expectations Anda untuk sistem baru dalam hal ROI dan timeline?
5. Apa concerns atau constraints yang perlu kami consider?

**Untuk Terapis:**
1. Bagaimana Anda currently mengelola jadwal Anda?
2. Apa pain points dalam proses booking dan scheduling?
3. Bagaimana Anda mendokumentasikan session notes? Apa challenges-nya?
4. Informasi apa yang Anda butuhkan untuk effectively mengelola clients?
5. Features apa yang Anda harapkan dalam sistem baru?

**Untuk Admin/Staff:**
1. Bagaimana proses handling booking dari client inquiry hingga confirmation?
2. Apa common issues atau complaints dari clients?
3. Berapa lama waktu yang dibutuhkan untuk setiap administrative task?
4. Tasks apa yang paling time-consuming dan berpotensi untuk diotomasi?
5. Informasi atau reports apa yang sering diminta oleh management?

**Untuk Sample Clients:**
1. Bagaimana experience Anda dalam booking layanan terapi saat ini?
2. Apa yang Anda suka dan tidak suka dari current process?
3. Apa expectations Anda untuk sistem booking online?
4. Seberapa penting privacy dan security data Anda?
5. Features apa yang akan membuat Anda lebih comfortable menggunakan layanan?

**Output:**
- Interview Transcripts
- Summary of Key Findings untuk each stakeholder group
- Identified Requirements dari stakeholder inputs
- Quotes atau insights untuk supporting findings dalam laporan

### 3.4.3 Studi Pustaka (Literature Review)

**Sumber Pustaka:**

1. **Buku:**
   - Textbooks tentang Sistem Informasi, Manajemen Proyek, Database Design, Web Development
   - Laravel dan PHP programming books
   - UI/UX design books

2. **Jurnal Ilmiah:**
   - Jurnal internasional dan nasional tentang health information systems
   - Jurnal tentang online booking systems dan appointment scheduling
   - Jurnal tentang mental health technology dan digital therapeutics
   - Minimal 10-15 jurnal articles (published dalam 5 tahun terakhir)

3. **Dokumentasi Teknis:**
   - Laravel Official Documentation
   - MySQL Documentation
   - Tailwind CSS Documentation
   - Web security best practices (OWASP guidelines)

4. **Thesis dan Laporan Penelitian:**
   - Thesis atau capstone projects serupa dari universitas lain
   - Industry reports tentang digital health trends

5. **Online Resources:**
   - Blog posts dan tutorials dari credible sources
   - Case studies dari successful implementations
   - Benchmark data dari industry surveys

**Prosedur:**

1. **Search dan Selection:**
   - Using academic databases (Google Scholar, IEEE Xplore, ResearchGate)
   - Searching dengan relevant keywords
   - Screening articles berdasarkan relevance, recency, dan quality
   - Selecting final set of references

2. **Reading dan Annotation:**
   - Reading selected materials carefully
   - Highlighting key points, theories, findings
   - Taking notes atau creating summaries
   - Identifying gaps atau areas for further investigation

3. **Synthesis:**
   - Organizing information by themes atau topics
   - Comparing dan contrasting different perspectives
   - Integrating findings into theoretical framework
   - Citing properly sesuai dengan citation style (IEEE atau APA)

**Output:**
- Annotated Bibliography
- Literature Review section dalam laporan (BAB II)
- Theoretical Framework untuk research
- References list (Daftar Pustaka)

### 3.4.4 Analisis Dokumen

**Dokumen yang Dianalisis:**

1. **Internal Documents CUR-HEART:**
   - Standard Operating Procedures (SOPs)
   - Booking forms dan client intake forms
   - Session documentation templates
   - Financial reports dan invoices
   - Client agreements atau consent forms
   - Marketing materials (brochures, website)

2. **Data Historis:**
   - Booking data (volumes, trends, peak times)
   - Client demographics
   - Revenue data
   - Therapist utilization rates
   - Common service types

3. **Competitor Analysis:**
   - Websites dari competitor mental health services
   - Their booking processes dan features
   - Pricing models
   - Unique selling propositions

4. **Regulatory Documents:**
   - UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi
   - Kode Etik Psikologi Indonesia
   - Health data protection guidelines

**Prosedur:**

1. **Collection:**
   - Requesting relevant documents dari CUR-HEART
   - Downloading atau copying documents dengan proper permission
   - Organizing documents dalam structured folder system

2. **Review dan Analysis:**
   - Reading documents thoroughly
   - Extracting relevant information (business rules, data elements, processes)
   - Identifying compliance requirements atau constraints
   - Noting best practices atau areas for improvement

3. **Documentation:**
   - Summarizing findings from each document
   - Creating data models based on existing forms
   - Listing business rules untuk implementation
   - Documenting compliance requirements untuk design considerations

**Output:**
- Document Analysis Summary
- Business Rules List
- Data Dictionary (preliminary)
- Compliance Requirements Checklist
- Competitive Analysis Matrix

### 3.4.5 Questionnaire/Survey

**Tujuan:**
Collecting quantitative data dari larger sample untuk supplement qualitative data dari interviews.

**Prosedur:**

1. **Questionnaire Design:**
   - Developing questions aligned dengan research objectives
   - Mix of multiple choice, Likert scale, dan open-ended questions
   - Ensuring clarity dan avoiding leading questions
   - Piloting questionnaire dengan small group untuk validation

2. **Distribution:**
   - Distributing online (Google Forms atau SurveyMonkey)
   - Distributing kepada CUR-HEART's existing clients (via email atau WhatsApp)
   - Distributing kepada potential users (social media, forums)
   - Setting response deadline (1-2 minggu)

3. **Data Collection:**
   - Monitoring response rates
   - Sending reminders untuk increase participation
   - Ensuring anonymity untuk honest responses

4. **Data Analysis:**
   - Exporting responses to Excel atau SPSS
   - Performing descriptive statistics (mean, median, frequencies)
   - Creating charts dan graphs untuk visualization
   - Analyzing correlations atau patterns

**Sample Questions:**

**Demographic:**
- Usia, jenis kelamin, pekerjaan, lokasi

**Current Experience:**
- Apakah Anda pernah menggunakan layanan terapi kesehatan mental? (Ya/Tidak)
- Bagaimana Anda usually melakukan booking? (Telepon/WhatsApp/Email/Walk-in)
- Seberapa puas Anda dengan current booking process? (Skala 1-5)

**Needs dan Preferences:**
- Features apa yang penting untuk Anda dalam sistem booking online? (Multiple choice dengan ranking)
- Seberapa penting privacy dan security data Anda? (Skala 1-5)
- Payment method apa yang Anda prefer? (Multiple choice)

**Technology Adoption:**
- Seberapa comfortable Anda menggunakan teknologi? (Skala 1-5)
- Apakah Anda lebih prefer mengakses dari mobile atau desktop? (Multiple choice)

**Output:**
- Survey Results Report dengan statistics dan visualizations
- User Personas based pada demographic dan behavior patterns
- Prioritized feature list based pada user preferences

### 3.4.6 Usability Testing

**Tujuan:**
Evaluating user interface dan user experience dengan observing real users saat mereka berinteraksi dengan sistem.

**Prosedur:**

1. **Planning:**
   - Defining usability testing objectives
   - Creating test scenarios dan tasks untuk participants
   - Preparing testing environment (laptop dengan sistem installed)
   - Recruiting participants (10-15 orang representing different user roles)

2. **Test Execution:**
   - **Introduction (5 menit):**
     - Explaining purpose of test
     - Emphasizing that we're testing sistem, not participants
     - Obtaining consent untuk observation dan recording
   
   - **Pre-Test Questionnaire (5 menit):**
     - Collecting demographic dan background information
     - Assessing current technology proficiency
   
   - **Task Execution (30-45 menit):**
     - Giving participants specific tasks to complete:
       - **Untuk Clients:** "Book a stress therapy session dengan terapis pilihan Anda untuk next week"
       - **Untuk Therapists:** "Set your availability untuk next month dan block dates untuk your vacation"
       - **Untuk Admin:** "Find all pending bookings dan approve them"
     - Encouraging participants untuk think aloud (verbalize thoughts)
     - Observing dan taking notes:
       - Time to complete tasks
       - Number of errors atau wrong clicks
       - Areas of confusion atau hesitation
       - Facial expressions atau body language (frustration, satisfaction)
     - Recording screen (dengan tools seperti OBS Studio) untuk later analysis
   
   - **Post-Test Questionnaire (10 menit):**
     - System Usability Scale (SUS) - standardized 10-question survey
     - Satisfaction ratings untuk specific features
     - Open-ended questions tentang likes, dislikes, suggestions
   
   - **Debriefing Interview (10 menit):**
     - Discussing observations dengan participants
     - Asking for clarification pada behaviors observed
     - Collecting additional feedback atau suggestions

3. **Data Analysis:**
   - **Quantitative Analysis:**
     - Calculating task success rates (%)
     - Calculating average time to complete tasks
     - Calculating error rates
     - Calculating SUS scores (average across participants)
   
   - **Qualitative Analysis:**
     - Reviewing observation notes dan recordings
     - Identifying common usability issues
     - Categorizing issues by severity (critical, major, minor)
     - Identifying patterns dalam user behavior
   
   - **Synthesis:**
     - Prioritizing usability issues untuk fixing
     - Creating recommendations untuk improvements
     - Documenting insights untuk design iterations

**Metrics Collected:**

- **Task Success Rate:** Percentage of participants who successfully completed task
- **Time on Task:** Average time taken to complete each task
- **Error Rate:** Number of errors made per task
- **Satisfaction Score:** SUS score (0-100 scale)
- **Net Promoter Score (NPS):** Likelihood to recommend system to others (0-10 scale)

**Output:**
- Usability Testing Report dengan:
  - Executive Summary
  - Methodology
  - Participant Demographics
  - Task Scenarios dan Results
  - Quantitative Metrics (success rates, times, SUS scores)
  - Qualitative Findings (observations, quotes)
  - List of Usability Issues dengan severity rankings
  - Recommendations untuk Improvements
  - Screenshots atau videos illustrating issues

**Tools Used:**
- OBS Studio untuk screen recording
- Stopwatch atau timer untuk measuring time on task
- Google Forms untuk questionnaires
- Spreadsheet untuk data compilation dan analysis
- Video editing software untuk creating highlights reel

---

Dengan menggunakan multiple data collection techniques ini, penelitian akan menghasilkan comprehensive understanding tentang kebutuhan, constraints, dan expectations dari stakeholders, serta empirical evidence tentang usability dan effectiveness dari sistem yang dikembangkan. Kombinasi dari qualitative methods (observasi, interview) dan quantitative methods (survey, usability metrics) akan provide triangulation, increasing validity dan reliability dari findings.

---
