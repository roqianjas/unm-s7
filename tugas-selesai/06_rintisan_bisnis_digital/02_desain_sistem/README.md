# 03 - DESAIN

Folder ini berisi semua dokumen desain sistem, meliputi diagram UML, ERD, mockup UI/UX, dan design system yang digunakan dalam pengembangan Sistem Informasi CUR-HEART.

---

## 📁 Struktur Folder

```
03_desain/
├── README.md                           # File ini
├── use_case_diagram.png               # Use Case Diagram (38 use cases)
├── activity_diagram.png               # Activity Diagram (15 aktivitas)
├── sequence_diagram.png               # Sequence Diagram (8 skenario)
├── class_diagram.png                  # Class Diagram (16 classes)
├── erd.png                            # Entity Relationship Diagram (16 tabel)
├── database_schema.pdf                # Dokumentasi skema database lengkap
├── architecture_diagram.png           # Arsitektur sistem (MVC)
├── mockups/                           # Screenshot 41 mockup halaman
│   ├── 01_landing.png
│   ├── 02_about.png
│   ├── ... (41 files)
│   └── 41_admin_settings.png
└── design_system/                     # Design system & components
    ├── color_palette.png
    ├── typography.png
    ├── components_library.png
    └── design_tokens.json
```

---

## 🎨 Daftar Dokumen Desain

### 1. Use Case Diagram
**File**: `use_case_diagram.png`

**Konten**:

**Actors**:
1. **Guest** (Pengunjung website)
2. **Client** (Klien yang booking terapi)
3. **Therapist** (Terapis hypnotherapy)
4. **Admin** (Administrator sistem)

**Total Use Cases**: 38 use cases

**Guest Use Cases** (8):
- UC-001: View Landing Page
- UC-002: View Services List
- UC-003: View Service Detail
- UC-004: View Therapists List
- UC-005: View Therapist Profile
- UC-006: View Blog Articles
- UC-007: Contact via Form
- UC-008: View FAQ

**Client Use Cases** (10 + Authentication):
- UC-009: Register Account
- UC-010: Login to System
- UC-011: Logout
- UC-012: Reset Password
- UC-013: Browse Services
- UC-014: Select Therapist
- UC-015: Book Therapy Session (4 steps)
- UC-016: Make Payment
- UC-017: View My Appointments
- UC-018: Reschedule Appointment
- UC-019: Cancel Appointment
- UC-020: Track Progress
- UC-021: Message Therapist
- UC-022: View Session History
- UC-023: Give Rating & Review

**Therapist Use Cases** (10):
- UC-024: View Dashboard
- UC-025: Manage Schedule
- UC-026: Set Availability
- UC-027: View Client List
- UC-028: View Client Profile
- UC-029: Conduct Session (video placeholder)
- UC-030: Input Session Notes
- UC-031: View Session History
- UC-032: View Earnings Report
- UC-033: Update Profile

**Admin Use Cases** (6):
- UC-034: View Admin Dashboard
- UC-035: Manage Users (CRUD)
- UC-036: Manage Bookings
- UC-037: Verify Payments
- UC-038: Generate Financial Reports
- UC-039: Configure System Settings

**Relationships**:
- Include: Payment Gateway (Midtrans)
- Include: Email Notification
- Extend: Cancel Booking, Reschedule

**Tool**: Draw.io, StarUML, atau Lucidchart  
**Format**: PNG (high resolution, 300 dpi)

**Penggunaan dalam Laporan**:
- BAB IV: Deskripsi Produk (Use Case Diagram)
- Gambar IV.x: Use Case Diagram Sistem Informasi CUR-HEART

---

### 2. Activity Diagram
**File**: `activity_diagram.png`

**Konten**: 15 Activity Diagrams untuk proses bisnis utama

**Key Activity Diagrams**:

**AD-001: Proses Booking (Client)**
```
Start → Browse Services → Select Service → 
View Available Therapists → Select Therapist → 
Choose Date & Time → Confirm Booking → 
Make Payment → [Payment Success?] → 
Yes: Booking Confirmed → Email Notification → End
No: Back to Payment → End
```

**AD-002: Proses Terapi (Therapist)**
```
Start → View Today Schedule → 
[Client Arrived?] → Yes: Start Session → 
Conduct Therapy (60-90 min) → 
Input Session Notes (SOAP) → 
Save to Database → End
```

**AD-003: Proses Payment (System)**
```
Start → Client Submit Payment → 
Send to Midtrans Gateway → 
[Payment Status] → 
Success: Update Booking Status → Send Confirmation Email
Failed: Send Failed Notification
Pending: Wait for Callback
→ End
```

*(... 12 activity diagrams lainnya)*

**Tool**: Draw.io atau Microsoft Visio  
**Format**: PNG (high resolution)

**Penggunaan dalam Laporan**:
- BAB IV: Deskripsi Produk (Activity Diagram)
- Gambar IV.x: Activity Diagram Proses Booking

---

### 3. Sequence Diagram
**File**: `sequence_diagram.png`

**Konten**: 8 Sequence Diagrams untuk interaksi sistem

**Key Sequence Diagrams**:

**SD-001: Login Sequence**
```
Client → Login Page → Controller → Authentication Middleware →
User Model → Database → Return User Data →
Create Session → Redirect to Dashboard
```

**SD-002: Booking Sequence**
```
Client → Booking Page → BookingController →
Check Therapist Availability → ServiceModel → TherapistModel →
Database → Return Available Slots → Display to Client →
Client Confirm → Create Booking Record → PaymentGateway →
Payment Confirmation → Email Service → Send Notification
```

**SD-003: Payment Callback Sequence**
```
Midtrans → Webhook Endpoint → PaymentController →
Verify Signature → Update Booking Status → 
BookingModel → Database → Email Service → 
Send Receipt to Client
```

*(... 5 sequence diagrams lainnya)*

**Actors**: Client, System (Controller), Model, Database, External Services

**Tool**: Draw.io, Lucidchart, atau PlantUML  
**Format**: PNG (high resolution)

**Penggunaan dalam Laporan**:
- BAB IV: Deskripsi Produk (Sequence Diagram)
- Gambar IV.x: Sequence Diagram Proses Login

---

### 4. Class Diagram
**File**: `class_diagram.png`

**Konten**: Class Diagram dengan 16 classes (Laravel Models)

**Core Classes (Laravel Eloquent Models)**:

1. **User** (Parent class)
   - Attributes: id, name, email, password, role, phone, avatar
   - Methods: hasRole(), isClient(), isTherapist(), isAdmin()
   - Relationships: hasOne(Client), hasOne(Therapist)

2. **Client** (extends User)
   - Attributes: user_id, date_of_birth, gender, medical_history
   - Methods: bookings(), sessions(), reviews()
   - Relationships: hasMany(Booking), hasMany(Review)

3. **Therapist** (extends User)
   - Attributes: user_id, specialization, certification, bio, rating
   - Methods: schedules(), bookings(), earnings()
   - Relationships: hasMany(Schedule), hasMany(Booking)

4. **Service**
   - Attributes: id, name, description, duration, price
   - Methods: bookings()
   - Relationships: hasMany(Booking)

5. **Booking**
   - Attributes: id, client_id, therapist_id, service_id, date, time, status, total
   - Methods: client(), therapist(), service(), payment()
   - Relationships: belongsTo(Client, Therapist, Service), hasOne(Payment)

6. **Payment**
   - Attributes: id, booking_id, amount, method, status, transaction_id
   - Methods: booking()
   - Relationships: belongsTo(Booking)

7. **Session**
   - Attributes: id, booking_id, start_time, end_time, notes, status
   - Methods: booking(), sessionNotes()
   - Relationships: belongsTo(Booking), hasOne(SessionNote)

8. **SessionNote**
   - Attributes: id, session_id, therapist_id, subjective, objective, assessment, plan
   - Methods: session(), therapist()
   - Relationships: belongsTo(Session, Therapist)

*(... 8 classes lainnya: Schedule, Availability, Message, Review, Notification, BlogPost, SystemSetting, etc.)*

**Tool**: StarUML, Draw.io, atau PlantUML  
**Format**: PNG (high resolution)

**Penggunaan dalam Laporan**:
- BAB IV: Deskripsi Produk (Class Diagram)
- Gambar IV.x: Class Diagram Sistem Informasi CUR-HEART

---

### 5. Entity Relationship Diagram (ERD)
**File**: `erd.png`

**Konten**: ERD dengan 16 tabel, relasi lengkap

**Tabel-tabel Database**:

1. **users** (PK: id)
   - Columns: id, name, email, password, role, phone, avatar, email_verified_at, timestamps
   - Relationships: 1:1 clients, 1:1 therapists

2. **clients** (PK: id, FK: user_id)
   - Columns: id, user_id, date_of_birth, gender, medical_history, timestamps
   - Relationships: 1:N bookings, 1:N reviews

3. **therapists** (PK: id, FK: user_id)
   - Columns: id, user_id, specialization, certification, bio, years_experience, rating, timestamps
   - Relationships: 1:N schedules, 1:N bookings, 1:N session_notes

4. **services** (PK: id)
   - Columns: id, name, description, duration, price, image, is_active, timestamps
   - Relationships: 1:N bookings

5. **bookings** (PK: id, FK: client_id, therapist_id, service_id)
   - Columns: id, client_id, therapist_id, service_id, booking_date, booking_time, status, total_price, notes, timestamps
   - Relationships: N:1 clients, N:1 therapists, N:1 services, 1:1 payments, 1:1 sessions

6. **payments** (PK: id, FK: booking_id)
   - Columns: id, booking_id, amount, payment_method, payment_status, transaction_id, paid_at, timestamps
   - Relationships: 1:1 bookings

7. **sessions** (PK: id, FK: booking_id)
   - Columns: id, booking_id, start_time, end_time, session_status, timestamps
   - Relationships: 1:1 bookings, 1:1 session_notes

8. **session_notes** (PK: id, FK: session_id, therapist_id)
   - Columns: id, session_id, therapist_id, subjective, objective, assessment, plan (SOAP format), timestamps
   - Relationships: 1:1 sessions, N:1 therapists

9. **schedules** (PK: id, FK: therapist_id)
   - Columns: id, therapist_id, day_of_week, start_time, end_time, timestamps
   - Relationships: N:1 therapists

10. **availability** (PK: id, FK: therapist_id)
    - Columns: id, therapist_id, date, is_available, reason, timestamps
    - Relationships: N:1 therapists

11. **messages** (PK: id, FK: sender_id, receiver_id)
    - Columns: id, sender_id, receiver_id, message, is_read, timestamps
    - Relationships: N:1 users (as sender), N:1 users (as receiver)

12. **reviews** (PK: id, FK: client_id, therapist_id, booking_id)
    - Columns: id, client_id, therapist_id, booking_id, rating, comment, timestamps
    - Relationships: N:1 clients, N:1 therapists, 1:1 bookings

13. **notifications** (PK: id, FK: user_id)
    - Columns: id, user_id, type, title, message, is_read, timestamps
    - Relationships: N:1 users

14. **blog_posts** (PK: id, FK: author_id)
    - Columns: id, author_id, title, slug, content, image, published_at, timestamps
    - Relationships: N:1 users (as author)

15. **system_settings** (PK: id)
    - Columns: id, key, value, type, timestamps

16. **password_resets** (Composite Key: email, token)
    - Columns: email, token, created_at

**Normalization**: 3NF (Third Normal Form)  
**Indexes**: 25 indexes untuk optimasi query  
**Foreign Keys**: 22 foreign key constraints

**Tool**: MySQL Workbench, dbdiagram.io, atau Lucidchart  
**Format**: PNG (high resolution) + PDF (dokumentasi lengkap)

**Penggunaan dalam Laporan**:
- BAB IV: Database Design (ERD)
- Gambar IV.x: Entity Relationship Diagram

---

### 6. Database Schema Documentation
**File**: `database_schema.pdf`

**Konten**: Dokumentasi lengkap skema database (30-40 halaman)

**Isi Dokumentasi**:
1. Overview Database
2. List Semua Tabel (16 tabel)
3. Detail Setiap Tabel:
   - Table name
   - Description
   - Columns (name, type, length, nullable, default, description)
   - Primary Key
   - Foreign Keys
   - Indexes
   - Relationships
   - Sample Data (5-10 records)
4. ERD Diagram
5. Normalization Explanation (1NF, 2NF, 3NF)
6. Query Optimization Strategy
7. Backup & Recovery Strategy

**Tool**: Microsoft Word atau LaTeX  
**Export**: PDF (print-ready)

**Penggunaan dalam Laporan**:
- BAB IV: Database Design (detail tabel)
- Lampiran (jika terlalu panjang)

---

### 7. System Architecture Diagram
**File**: `architecture_diagram.png`

**Konten**: Arsitektur Sistem (MVC Pattern)

**Layers**:

```
┌─────────────────────────────────────────┐
│         PRESENTATION LAYER              │
│  (Blade Templates + Tailwind CSS +      │
│   JavaScript + HTML5)                   │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│         APPLICATION LAYER               │
│  (Laravel Controllers + Middleware +    │
│   Form Requests + Services)             │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│          BUSINESS LOGIC LAYER           │
│  (Eloquent Models + Repositories +      │
│   Business Rules)                       │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│          DATA ACCESS LAYER              │
│  (MySQL Database + Eloquent ORM +       │
│   Query Builder)                        │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│         EXTERNAL SERVICES               │
│  - Midtrans Payment Gateway             │
│  - Email Service (SMTP/Gmail)           │
│  - Cloud Storage (optional)             │
└─────────────────────────────────────────┘
```

**Technology Stack**:
- Framework: Laravel 10
- Language: PHP 8.2
- Database: MySQL 8.0
- Frontend: Blade, Tailwind CSS, JavaScript Vanilla
- Server: Apache/Nginx
- Version Control: Git/GitHub

**Penggunaan dalam Laporan**:
- BAB IV: Arsitektur Sistem
- Gambar IV.x: Arsitektur Sistem CUR-HEART

---

### 8. UI/UX Mockups (41 Halaman)
**Folder**: `mockups/`

**Konten**: Screenshot 41 halaman mockup (PNG, 1920x1080px)

**Daftar 41 Mockup**:

**Public Pages (8)**:
1. 01_landing.png - Homepage/Landing page
2. 02_about.png - Tentang kami
3. 03_services.png - Daftar layanan
4. 04_services_detail.png - Detail layanan
5. 05_therapists.png - Daftar terapis
6. 06_therapist_profile.png - Profil terapis detail
7. 07_blog_list.png - Daftar artikel blog
8. 08_blog_detail.png - Detail artikel blog

**Support Pages (4)**:
9. 09_contact.png - Hubungi kami
10. 10_faq.png - FAQ
11. 11_privacy_policy.png - Kebijakan privasi
12. 12_terms_conditions.png - Syarat & ketentuan

**Authentication (4)**:
13. 13_login.png - Login
14. 14_register.png - Registrasi
15. 15_forgot_password.png - Lupa password
16. 16_reset_password.png - Reset password

**Client Dashboard (10)**:
17. 17_client_dashboard.png - Dashboard klien
18. 18_booking_step1.png - Booking: Pilih layanan
19. 19_booking_step2.png - Booking: Pilih terapis
20. 20_booking_step3.png - Booking: Jadwal & waktu
21. 21_booking_step4.png - Booking: Konfirmasi & pembayaran
22. 22_booking_success.png - Booking berhasil
23. 23_client_appointments.png - Daftar janji temu
24. 24_appointment_detail.png - Detail janji temu
25. 25_client_progress.png - Progress tracking
26. 26_client_messages.png - Pesan/chat

**Therapist Dashboard (10)**:
27. 27_therapist_dashboard.png - Dashboard terapis
28. 28_therapist_schedule.png - Jadwal kerja
29. 29_therapist_availability.png - Pengaturan ketersediaan
30. 30_therapist_clients.png - Daftar klien
31. 31_client_profile_view.png - Profil klien
32. 32_session_room.png - Ruang sesi
33. 33_session_notes.png - Catatan sesi
34. 34_therapist_session_history.png - Riwayat sesi
35. 35_therapist_earnings.png - Pendapatan
36. 36_therapist_profile_edit.png - Edit profil

**Admin Dashboard (5)**:
37. 37_admin_dashboard.png - Dashboard admin
38. 38_admin_users.png - Manajemen pengguna
39. 39_admin_bookings.png - Manajemen booking
40. 40_admin_financial.png - Laporan keuangan
41. 41_admin_settings.png - Pengaturan sistem

**Sumber Mockup HTML**:  
`/var/www/unm-s7/tugas-selesai/06_rintisan_bisnis_digital/mockups/`

**Cara Membuat Screenshot**:
1. Buka setiap file HTML di browser (Chrome/Firefox)
2. Set resolusi viewport: 1920x1080
3. Screenshot dengan ekstensi Full Page Screen Capture
4. Save sebagai PNG (high quality)
5. Rename sesuai naming convention

**Penggunaan dalam Laporan**:
- BAB IV: User Interface Design
- Gambar IV.x sampai IV.41: Screenshot UI Sistem

---

### 9. Design System
**Folder**: `design_system/`

**Konten**: Design system lengkap

**Files**:

**A. Color Palette** (`color_palette.png`)
```
Primary: #1E0E62 (Navy Blue)
Secondary: #FF6B7A (Pink)
Accent: #6C5CE7 (Purple)
Success: #00B894 (Green)
Warning: #FDCB6E (Yellow)
Error: #D63031 (Red)
Gray Scale: #F5F6FA, #DFE6E9, #B2BEC3, #636E72, #2D3436
```

**B. Typography** (`typography.png`)
```
Heading Font: Poppins (Semi-Bold, Bold)
Body Font: Inter (Regular, Medium)

H1: 48px/56px, Poppins Bold
H2: 40px/48px, Poppins Bold
H3: 32px/40px, Poppins Semi-Bold
H4: 24px/32px, Poppins Semi-Bold
H5: 20px/28px, Poppins Semi-Bold
H6: 16px/24px, Poppins Semi-Bold
Body: 16px/24px, Inter Regular
Small: 14px/20px, Inter Regular
Caption: 12px/16px, Inter Regular
```

**C. Components Library** (`components_library.png`)
- Buttons (Primary, Secondary, Outline, Ghost, Disabled states)
- Forms (Input text, textarea, select, checkbox, radio, file upload)
- Cards (Service card, therapist card, blog card)
- Modals & Dialogs
- Alerts & Notifications
- Tables & Data grids
- Charts & Graphs
- Navigation (Navbar, Sidebar, Breadcrumb)
- Pagination
- Badges & Tags

**D. Design Tokens** (`design_tokens.json`)
```json
{
  "colors": {...},
  "typography": {...},
  "spacing": {...},
  "breakpoints": {...},
  "shadows": {...},
  "borders": {...}
}
```

**Tool**: Figma untuk design, export PNG  
**Sumber**: `/var/www/unm-s7/tugas-selesai/06_rintisan_bisnis_digital/design-system/`

**Penggunaan dalam Laporan**:
- BAB IV: Design System
- Gambar IV.x: Color Palette & Typography

---

## 📊 Summary Desain

### Statistik Desain:

- ✅ **6 Diagram UML** (Use Case, Activity, Sequence, Class, ERD, Architecture)
- ✅ **16 Tabel Database** dengan normalisasi 3NF
- ✅ **41 Mockup UI/UX** (full responsive design)
- ✅ **Design System Lengkap** (colors, typography, components)
- ✅ **38 Use Cases** untuk 4 actors
- ✅ **15 Activity Diagrams** untuk proses bisnis
- ✅ **8 Sequence Diagrams** untuk interaksi sistem

**Total Visual Assets**: 50+ files (diagram + mockups + design system)

---

## 🔗 Integrasi dengan BAB Laporan

**BAB IV - Hasil Penelitian (Bagian Desain)**:

**4.3 Deskripsi Produk / Servis**:
- 4.3.1 Arsitektur Sistem → `architecture_diagram.png`
- 4.3.2 Use Case Diagram → `use_case_diagram.png`
- 4.3.3 Activity Diagram → `activity_diagram.png`
- 4.3.4 Sequence Diagram → `sequence_diagram.png`
- 4.3.5 Class Diagram → `class_diagram.png`
- 4.3.6 Database Design (ERD) → `erd.png` + `database_schema.pdf`
- 4.3.7 User Interface Design → `mockups/*.png` (41 gambar)
- 4.3.8 Design System → `design_system/*.png`

---

## ✅ Checklist Kelengkapan Desain

- [x] Use Case Diagram (38 use cases)
- [x] Activity Diagram (15 diagrams)
- [x] Sequence Diagram (8 diagrams)
- [x] Class Diagram (16 classes/models)
- [x] ERD (16 tabel, 3NF)
- [x] Database Schema Documentation (PDF)
- [x] Architecture Diagram (MVC)
- [x] 41 Mockup Screenshots (PNG, high res)
- [x] Design System (color, typography, components)
- [x] Design Tokens (JSON)

---

## 🛠️ Tools yang Digunakan

**Diagram**:
- Draw.io (free, web-based)
- StarUML (for UML diagrams)
- MySQL Workbench (for ERD)
- Lucidchart (alternative)

**Mockup & Design**:
- Figma (UI/UX design)
- Adobe XD (alternative)
- HTML/CSS/Tailwind (mockup prototype)

**Screenshot**:
- Full Page Screen Capture (Chrome extension)
- Firefox Developer Tools
- Lightshot / Greenshot

**Documentation**:
- Microsoft Word / Google Docs (database schema doc)
- LaTeX (alternative for academic formatting)

---

**Last Updated**: 1 November 2024  
**Prepared by**: Tim Proyek CUR-HEART (Susanto - UI/UX Designer, Fahruroji - Database Designer)
