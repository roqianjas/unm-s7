# BAB IV (Lanjutan)  
# HASIL PENELITIAN DAN PEMBAHASAN - PART 2

## 4.3. DESKRIPSI PRODUK / SERVIS

Berikut ini adalah deskripsi umum (*high-level*) mengenai produk atau layanan yang dihasilkan dari proyek ini:

### 4.3.1 Tujuan Proyek

Tujuan proyek ini adalah membangun sistem informasi berbasis web yang dapat memberikan informasi yang berkaitan dengan manajemen pemesanan dan terapi hipnoterapi CUR-HEART, mencakup:

- Informasi lengkap tentang layanan terapi yang ditawarkan
- Profil terapis dengan spesialisasi dan jadwal ketersediaan
- Sistem pemesanan online yang mudah dan cepat
- Manajemen sesi terapi dan dokumentasi klien
- Pembayaran online yang aman dan terintegrasi
- Dashboard analytics untuk pengambilan keputusan

### 4.3.2 Pengguna Sistem

Sistem ini memiliki 3 tipe pengguna utama dengan hak akses berbeda. Sistem yang dibangun harus mampu:

**A. Untuk Klien:**
- Menampilkan informasi jumlah layanan, terapis, dan testimoni
- Menampilkan informasi layanan terbaru dan terapis unggulan
- Memberikan kemampuan pemesanan layanan secara online 24/7
- Menampilkan riwayat pemesanan dan sesi terapi
- Menyediakan sistem pembayaran yang aman dan mudah
- Menampilkan progress terapi dan catatan sesi (yang dibagikan)

**B. Untuk Terapis:**
- Manajemen jadwal dan ketersediaan secara mandiri
- Melihat daftar klien dan detail pemesanan hari ini
- Mendokumentasikan sesi terapi dengan form terstruktur
- Mengakses riwayat lengkap klien untuk kontinuitas perawatan
- Melihat dashboard earnings dan statistik kinerja
- Update profil dan pengaturan notifikasi

**C. Untuk Admin:**
- Monitoring pemesanan real-time dengan status tracking
- Manajemen users (klien, terapis, admin)
- Manajemen layanan (CRUD operations)
- Laporan keuangan dan analytics:
  - Total pemesanan dan revenue
  - Breakdown per layanan dan terapis
  - Trend pemesanan bulanan
- Approval dan verifikasi terapis baru
- System settings dan configuration

### 4.3.3 Fitur Utama Sistem

**A. Modul Public Website**
- Landing page dengan informasi bisnis
- Katalog layanan terapi lengkap dengan deskripsi
- Direktori terapis dengan profil dan rating
- Blog/artikel tentang kesehatan mental
- FAQ dan halaman bantuan
- Contact form

**B. Modul Autentikasi**
- Multi-role authentication (Client, Therapist, Admin)
- Register dengan validasi email
- Login dengan remember me
- Forgot password & reset password
- Social login (Google, Facebook) - opsional

**C. Modul Booking/Pemesanan**
- 4-step booking wizard:
  1. Pilih layanan terapi
  2. Pilih terapis (atau auto-assign)
  3. Pilih tanggal & waktu
  4. Konfirmasi & pembayaran
- Real-time availability checking
- Session type: Online/Offline
- Promo code support
- Booking confirmation email

**D. Modul Payment**
- Integrasi Midtrans payment gateway
- Multiple payment methods:
  - Credit/Debit card
  - Bank transfer
  - E-wallet (GoPay, OVO, Dana)
- Automatic payment verification
- Invoice generation (PDF)
- Payment history dan status tracking

**E. Modul Client Dashboard**
- Overview: Upcoming sessions, completed sessions, total hours
- My Appointments: List, detail, reschedule, cancel
- Progress Tracking: Visual charts dan metrics
- Messages: Chat dengan terapis
- Profile & settings

**F. Modul Therapist Dashboard**
- Today's schedule dengan countdown
- Client list dan details
- Session documentation form dengan rich text editor
- Session history dan notes archive
- Availability settings (working hours, time off)
- Earnings dashboard
- Profile management

**G. Modul Admin Dashboard**
- Statistics cards: Users, bookings, revenue, health
- Charts: Revenue trend, user growth, top services
- User management (CRUD, approve therapist)
- Booking management (view, edit, cancel, refund)
- Service management (CRUD)
- Financial reports (export Excel/PDF)
- System settings

**H. Modul Notifications**
- Email notifications:
  - Booking confirmation
  - Payment success
  - Session reminder (H-1, H-0)
  - Cancellation notification
- In-app notifications
- SMS reminder (future enhancement)

**I. Modul Reporting**
- Booking reports: Daily, weekly, monthly
- Revenue reports: Per service, per therapist
- User activity reports
- Export formats: PDF, Excel, CSV

### 4.3.4 Arsitektur Sistem

Sistem dibangun dengan arsitektur **MVC (Model-View-Controller)** menggunakan Laravel framework:

```
┌──────────────────────────────────────────────┐
│              PRESENTATION LAYER              │
│  (Views - Blade Templates + Tailwind CSS)    │
│  - Public pages                              │
│  - Client dashboard                          │
│  - Therapist dashboard                       │
│  - Admin dashboard                           │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│            APPLICATION LAYER                 │
│         (Controllers + Middleware)           │
│  - AuthController                            │
│  - BookingController                         │
│  - PaymentController                         │
│  - DashboardController                       │
│  - AdminController                           │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│              BUSINESS LOGIC LAYER            │
│         (Models + Services + Events)         │
│  - User, Therapist, Client models            │
│  - Service, Booking, Payment models          │
│  - Session, Review models                    │
│  - Business rules & validation               │
└──────────────┬───────────────────────────────┘
               │
┌──────────────▼───────────────────────────────┐
│              DATA ACCESS LAYER               │
│       (Eloquent ORM + MySQL Database)        │
│  - 16 normalized tables (3NF)                │
│  - Migrations & seeders                      │
│  - Relationships & constraints               │
└──────────────────────────────────────────────┘
```

### 4.3.5 Database Design

Sistem menggunakan 16 tabel utama:

1. **users** - Data user universal
2. **clients** - Data spesifik klien
3. **therapists** - Data spesifik terapis
4. **services** - Katalog layanan terapi
5. **therapist_services** - Relasi terapis-layanan
6. **therapist_availability** - Jadwal ketersediaan terapis
7. **bookings** - Data pemesanan
8. **sessions** - Data sesi terapi
9. **session_notes** - Catatan sesi dari terapis
10. **payments** - Transaksi pembayaran
11. **reviews** - Ulasan dan rating
12. **notifications** - Notifikasi sistem
13. **messages** - Chat antara klien-terapis
14. **promo_codes** - Kode promo diskon
15. **audit_logs** - Log aktivitas untuk audit
16. **system_settings** - Konfigurasi sistem

Normalisasi: **Third Normal Form (3NF)** untuk menghindari redundansi dan anomali data.

### 4.3.6 User Roles dan Permissions

**A. Guest (Pengunjung)**
- View: Landing page, services, therapists, blog
- Action: Register, login, contact

**B. Client (Klien)**
- View: All guest permissions + dashboard, bookings, progress, messages
- Action: Book service, make payment, reschedule/cancel, leave review, chat

**C. Therapist (Terapis)**
- View: Dashboard, schedule, clients, sessions, earnings
- Action: Set availability, document sessions, view client history, chat, update profile

**D. Admin (Administrator)**
- View: All data (users, bookings, payments, reports)
- Action: Full CRUD on all resources, approve therapists, generate reports, system settings

### 4.3.7 Keamanan Sistem

**A. Authentication & Authorization**
- Password hashing dengan bcrypt
- Session management dengan Laravel
- CSRF protection untuk semua forms
- Role-based access control (RBAC)

**B. Data Security**
- HTTPS untuk semua komunikasi
- SQL injection prevention (Eloquent ORM)
- XSS prevention (Blade escaping)
- Encryption untuk data sensitif (medical records)

**C. Payment Security**
- PCI-DSS compliant (via Midtrans)
- No credit card data stored locally
- 3D Secure support

**D. Compliance**
- UU Perlindungan Data Pribadi (UU PDP)
- GDPR-ready architecture
- Data retention policy (30 hari backup)

### 4.3.8 Performance & Scalability

**A. Performance Optimization**
- Database indexing pada frequent queries
- Laravel caching (config, route, view cache)
- Lazy loading untuk relasi Eloquent
- CDN untuk static assets (future)

**B. Scalability**
- Horizontal scaling ready (load balancer + multiple servers)
- Database replication (master-slave)
- Queue workers untuk background jobs
- Stateless sessions (ready untuk clustering)

**Target Metrics:**
- Page load time: < 2 seconds
- Concurrent users: 100+
- Uptime: ≥ 99,5%
- Database query time: < 100ms (average)

---

### 4.3.9 Pelaksanaan Proyek (Desain Sistem)

Pelaksanaan proyek merupakan fase implementasi dari perencanaan yang telah dibuat. Pada fase ini dilakukan desain sistem yang mencakup perancangan basis data, pemodelan UML, dan desain antarmuka pengguna.

#### 4.3.9.1 Use Case Diagram

Use Case Diagram menggambarkan interaksi antara aktor (pengguna) dengan sistem, serta fungsionalitas yang dapat dilakukan oleh masing-masing aktor.

**[GAMBAR 4.3 - Use Case Diagram Sistem Informasi CUR-HEART]**

**Aktor dalam Sistem:**

1. **Tamu (Guest)** - Pengunjung website yang belum login
2. **Klien** - Pengguna terdaftar yang menggunakan layanan terapi
3. **Terapis** - Praktisi hipnoterapi yang memberikan layanan
4. **Admin** - Administrator sistem yang mengelola seluruh sistem
5. **Payment Gateway** - Sistem eksternal untuk pemrosesan pembayaran

**Use Cases Utama:**

**Untuk Tamu:**
- Melihat halaman beranda
- Melihat daftar layanan terapi
- Melihat profil terapis
- Registrasi akun baru
- Login ke sistem

**Untuk Klien:**
- Melihat jadwal terapis yang tersedia
- Membuat pemesanan layanan terapi
- Memilih terapis dan waktu sesi
- Melakukan pembayaran online
- Melihat riwayat pemesanan
- Melihat riwayat sesi terapi
- Update profil
- Membatalkan/reschedule pemesanan (dengan syarat)

**Untuk Terapis:**
- Melihat jadwal sesi terapi hari ini dan minggu ini
- Melihat detail pemesanan klien
- Mengatur ketersediaan jadwal
- Mendokumentasikan sesi terapi (catatan sesi)
- Melihat riwayat klien
- Mengupdate status sesi (selesai/dibatalkan)
- Melihat earnings (pendapatan)

**Untuk Admin:**
- Mengelola data layanan terapi
- Mengelola data terapis
- Mengelola data klien
- Melihat semua pemesanan
- Konfirmasi pembayaran manual (jika ada)
- Generate laporan (pemesanan, keuangan, kinerja)
- Monitoring sistem

**Untuk Payment Gateway:**
- Memproses pembayaran
- Mengirim notifikasi status pembayaran
- Verifikasi transaksi

#### 4.3.9.2 Activity Diagram

Activity Diagram menggambarkan alur aktivitas dalam sistem untuk berbagai proses bisnis.

**a. Activity Diagram Proses Pemesanan Terapi oleh Klien**

**[GAMBAR 4.4 - Activity Diagram Pemesanan Terapi]**

Alur proses pemesanan terapi:
1. Klien login ke sistem
2. Klien memilih layanan terapi yang diinginkan
3. Sistem menampilkan daftar terapis dan jadwal yang tersedia
4. Klien memilih terapis dan waktu sesi
5. Sistem memeriksa ketersediaan jadwal
   - Jika tidak tersedia: Tampilkan pesan error, kembali ke pemilihan jadwal
   - Jika tersedia: Lanjut ke langkah berikutnya
6. Klien mengisi informasi tambahan (keluhan, catatan)
7. Sistem menampilkan ringkasan pemesanan dan total biaya
8. Klien konfirmasi pemesanan
9. Sistem membuat record pemesanan dengan status "Pending Payment"
10. Sistem redirect ke payment gateway (Midtrans)
11. Klien melakukan pembayaran
12. Payment gateway memproses transaksi
    - Jika gagal: Update status menjadi "Payment Failed", kirim notifikasi
    - Jika berhasil: Update status menjadi "Paid", lanjut
13. Sistem mengirim email konfirmasi ke klien
14. Sistem mengirim notifikasi ke terapis terkait
15. Sistem mengirim reminder email 1 hari sebelum sesi
16. Selesai

**b. Activity Diagram Dokumentasi Sesi Terapi oleh Terapis**

**[GAMBAR 4.5 - Activity Diagram Dokumentasi Sesi Terapi]**

Alur proses dokumentasi sesi terapi:
1. Terapis login ke sistem
2. Terapis melihat daftar sesi hari ini
3. Terapis memilih sesi yang sudah dilaksanakan
4. Sistem menampilkan form dokumentasi sesi
5. Terapis mengisi dokumentasi:
   - Teknik yang digunakan
   - Observasi kondisi klien
   - Kemajuan yang dicapai
   - Catatan penting
   - Rekomendasi sesi berikutnya
6. Terapis menyimpan dokumentasi
7. Sistem validasi data
   - Jika tidak valid: Tampilkan pesan error, kembali ke form
   - Jika valid: Simpan ke database
8. Sistem update status sesi menjadi "Completed"
9. Sistem mencatat waktu dokumentasi
10. Dokumentasi tersimpan dan dapat diakses untuk sesi berikutnya
11. Selesai

**c. Activity Diagram Generate Laporan oleh Admin**

**[GAMBAR 4.6 - Activity Diagram Generate Laporan]**

Alur proses generate laporan:
1. Admin login ke sistem
2. Admin mengakses menu laporan
3. Admin memilih jenis laporan (pemesanan, keuangan, kinerja terapis, klien)
4. Admin memilih periode (tanggal mulai - tanggal selesai)
5. Admin memilih filter tambahan (terapis tertentu, layanan tertentu, dll)
6. Admin klik tombol "Generate Laporan"
7. Sistem mengambil data dari database sesuai kriteria
8. Sistem memproses dan menghitung statistik
9. Sistem menampilkan laporan dalam format tabel dan chart
10. Admin dapat melihat, export (PDF/Excel), atau print langsung
11. Selesai

#### 4.3.9.3 Entity Relationship Diagram (ERD)

Entity Relationship Diagram (ERD) menggambarkan struktur basis data sistem informasi CUR-HEART dengan relasi antar entitas.

**[GAMBAR 4.7 - Entity Relationship Diagram (ERD)]**

**Entitas Utama:**

1. **users** - Menyimpan data semua pengguna sistem (klien, terapis, admin)
2. **clients** - Menyimpan data detail klien
3. **therapists** - Menyimpan data detail terapis
4. **services** - Menyimpan data layanan terapi yang ditawarkan
5. **bookings** - Menyimpan data pemesanan terapi
6. **payments** - Menyimpan data pembayaran
7. **sessions** - Menyimpan data sesi terapi yang sudah dilaksanakan
8. **session_notes** - Menyimpan catatan dokumentasi sesi terapi
9. **therapist_schedules** - Menyimpan jadwal ketersediaan terapis
10. **therapist_unavailability** - Menyimpan data ketidaktersediaan terapis (cuti, sakit)
11. **reviews** - Menyimpan review dari klien terhadap terapis/layanan
12. **notifications** - Menyimpan notifikasi untuk pengguna
13. **settings** - Menyimpan konfigurasi sistem
14. **activity_logs** - Menyimpan log aktivitas pengguna (audit trail)

**Relasi Utama:**

- users (1) ↔ (1) clients: One-to-One
- users (1) ↔ (1) therapists: One-to-One  
- clients (1) ↔ (M) bookings: One-to-Many
- therapists (1) ↔ (M) bookings: One-to-Many
- services (1) ↔ (M) bookings: One-to-Many
- bookings (1) ↔ (1) payments: One-to-One
- bookings (1) ↔ (1) sessions: One-to-One
- sessions (1) ↔ (M) session_notes: One-to-Many
- therapists (1) ↔ (M) therapist_schedules: One-to-Many
- therapists (1) ↔ (M) therapist_unavailability: One-to-Many
- sessions (1) ↔ (M) reviews: One-to-Many
- users (1) ↔ (M) notifications: One-to-Many

**Keterangan:**
- (1) = One
- (M) = Many
- PK = Primary Key
- FK = Foreign Key

Database dinormalisasi hingga Third Normal Form (3NF) untuk menghindari redundansi data dan menjaga integritas data.

#### 4.3.9.4 Desain Antarmuka Pengguna (UI/UX)

Desain antarmuka pengguna (UI) dibuat menggunakan Figma dengan total 41 halaman mockup yang mencakup semua role pengguna. Desain mengikuti prinsip *user-centered design* dengan fokus pada kemudahan penggunaan, aksesibilitas, dan pengalaman pengguna yang optimal.

##### A. Sistem Desain (Design System)

**Color Palette:**
- **Primary**: Teal (#0D9488) - Menenangkan, profesional, healing
- **Secondary**: Purple (#9333EA) - Spiritual, transformasi
- **Accent**: Orange (#F59E0B) - Energi, optimisme
- **Neutral**: Gray scale dari #F9FAFB hingga #111827
- **Success**: Green (#10B981)
- **Warning**: Yellow (#F59E0B)
- **Error**: Red (#EF4444)

**Typography:**
- **Heading**: Inter (Sans-serif) - Modern, clean, readable
- **Body**: Inter (Sans-serif)
- **Font Sizes**: H1 (36px), H2 (30px), H3 (24px), Body (16px), Small (14px)

**Design Principles:**
- Clean and minimal design
- Consistent spacing (Tailwind spacing scale)
- Mobile-first responsive design
- Accessibility: Color contrast ratio minimal 4.5:1
- Clear visual hierarchy
- Intuitive navigation

**[GAMBAR 4.8 - Sistem Desain: Color Palette & Typography]**

##### B. Mockup Halaman Utama

Sistem memiliki **41 halaman mockup** yang terbagi dalam beberapa kategori:

**1. Halaman Publik (12 halaman):**

**[GAMBAR 4.9 - Mockup Landing Page]**
- **Landing Page**: Hero section, layanan terapi, featured therapists, testimoni klien, blog posts

**[GAMBAR 4.10 - Mockup Halaman Tentang Kami]**
- **Halaman Tentang Kami**: Our story, visi & misi, core values, tim profil, sertifikasi

**[GAMBAR 4.11 - Mockup Katalog Layanan]**
- **Katalog Layanan**: Filter & search, services grid dengan card detail

**[GAMBAR 4.12 - Mockup Detail Layanan]**
- **Detail Layanan**: Hero, tab navigation (overview/benefits/process/FAQ), terapis recommended, ulasan

**[GAMBAR 4.13 - Mockup Direktori Terapis]**
- **Direktori Terapis**: Search, filter spesialisasi/rating/pengalaman, therapists grid

**[GAMBAR 4.14 - Mockup Profil Terapis]**
- **Profil Terapis**: Bio lengkap, pendidikan & sertifikasi, layanan & harga, kalender ketersediaan, ulasan klien

**[GAMBAR 4.15 - Mockup Daftar Blog]**
- **Daftar Blog**: Featured article, search, filter kategori, blog posts grid, sidebar

**[GAMBAR 4.16 - Mockup Detail Blog]**
- **Detail Blog**: Article content, metadata, social sharing, related articles, comment section

**[GAMBAR 4.17 - Mockup Contact Us]**
- **Contact Us**: Form, info kontak, Google Maps, social media links

**[GAMBAR 4.18 - Mockup FAQ]**
- **FAQ**: Search, tab kategori, accordion list dengan feedback

**[GAMBAR 4.19 - Mockup Privacy Policy]**
- **Privacy Policy**: Table of contents, sections terstruktur, highlight penting

**[GAMBAR 4.20 - Mockup Terms & Conditions]**
- **Terms & Conditions**: Table of contents, numbered clauses untuk referensi legal

**2. Halaman Autentikasi (4 halaman):**

**[GAMBAR 4.21 - Mockup Login]**
- **Login**: Split screen dengan ilustrasi, email & password, remember me, social login

**[GAMBAR 4.22 - Mockup Register]**
- **Register**: Pilihan tipe user (Client/Therapist), form berbeda per role, terms checkbox

**[GAMBAR 4.23 - Mockup Forgot Password]**
- **Forgot Password**: Simple form, send reset link, success state

**[GAMBAR 4.24 - Mockup Reset Password]**
- **Reset Password**: New password, confirm password, password strength meter

**3. Dashboard Klien (10 halaman):**

**[GAMBAR 4.25 - Mockup Dashboard Klien - Main Dashboard]**
- **Main Dashboard**: Welcome, quick stats, next appointment, upcoming sessions, progress overview

**[GAMBAR 4.26 - Mockup Booking Step 1 - Pilih Layanan]**
- **Booking Step 1**: Service selection dengan card layanan

**[GAMBAR 4.27 - Mockup Booking Step 2 - Pilih Terapis]**
- **Booking Step 2**: Choose therapist dengan profil dan rating

**[GAMBAR 4.28 - Mockup Booking Step 3 - Pilih Jadwal]**
- **Booking Step 3**: Date & time picker dengan ketersediaan real-time

**[GAMBAR 4.29 - Mockup Booking Step 4 - Konfirmasi & Pembayaran]**
- **Booking Step 4**: Confirm & payment dengan ringkasan pemesanan

**[GAMBAR 4.30 - Mockup Booking Success]**
- **Booking Success**: Congratulations, booking details, next steps, action buttons

**[GAMBAR 4.31 - Mockup My Appointments]**
- **My Appointments**: Tabs (upcoming/past/cancelled), filter & sort, appointments cards

**[GAMBAR 4.32 - Mockup Appointment Detail]**
- **Appointment Detail**: Booking info, payment info, session notes, reschedule/cancel actions

**[GAMBAR 4.33 - Mockup Progress Dashboard]**
- **Progress Dashboard**: Wellness score, session attendance, goals & milestones, mood tracking

**[GAMBAR 4.34 - Mockup Messages (Chat)]**
- **Messages (Chat)**: Conversations list, active chat area, typing indicator

**4. Dashboard Terapis (10 halaman):**

**[GAMBAR 4.35 - Mockup Dashboard Terapis - Main Dashboard]**
- **Main Dashboard**: Today's sessions, key metrics, earnings overview, client reviews

**[GAMBAR 4.36 - Mockup Schedule Management]**
- **Schedule Management**: Calendar views (day/week/month), appointment blocks, time off

**[GAMBAR 4.37 - Mockup Availability Settings]**
- **Availability Settings**: Working hours per day, session duration, booking window, special dates

**[GAMBAR 4.38 - Mockup Clients List]**
- **Clients List**: Search & filter, client cards dengan stats, bulk actions

**[GAMBAR 4.39 - Mockup Client Profile View]**
- **Client Profile View**: Overview, session history, notes & observations, progress & goals, files

**[GAMBAR 4.40 - Mockup Session Room]**
- **Session Room**: Video conference dengan timer, control bar, notes panel

**[GAMBAR 4.41 - Mockup Session Notes Form]**
- **Session Notes Form**: Assessment, session summary, progress notes, homework, templates

**[GAMBAR 4.42 - Mockup Session History]**
- **Session History**: Total sessions, search & filter, sessions table, analytics

**[GAMBAR 4.43 - Mockup Earnings Dashboard]**
- **Earnings Dashboard**: Balance, earnings chart, transactions, withdrawal, payment settings

**[GAMBAR 4.44 - Mockup Profile Edit]**
- **Profile Edit**: Tabs untuk basic/professional/about/education/services/media/settings

**5. Dashboard Admin (5 halaman):**

**[GAMBAR 4.45 - Mockup Dashboard Admin - Main Dashboard]**
- **Main Dashboard**: Key metrics, revenue chart, recent bookings, user growth, system alerts

**[GAMBAR 4.46 - Mockup Users Management]**
- **Users Management**: Tabs (all/clients/therapists/admins/pending), user table, bulk actions

**[GAMBAR 4.47 - Mockup Bookings Management]**
- **Bookings Management**: Summary stats, tabs (all/upcoming/past/pending/cancelled/disputed), booking table

**[GAMBAR 4.48 - Mockup Financial Reports]**
- **Financial Reports**: Revenue summary, charts, transactions table, withdrawals, refunds, analytics

**[GAMBAR 4.49 - Mockup System Settings]**
- **System Settings**: Categories navigation, general/booking/payment/email/security/policies/integrations/advanced

##### C. Fitur Desain Unggulan

**Responsive Design:**
- Mobile-first approach dengan breakpoints optimal
- Adaptif untuk desktop (1920px), tablet (768px), dan mobile (375px)
- Touch-friendly untuk mobile devices (min 44x44px tap targets)

**Aksesibilitas (Accessibility):**
- WCAG 2.1 Level AA compliant
- Color contrast ratio minimal 4.5:1 untuk text normal
- Keyboard navigation support
- Screen reader friendly dengan proper ARIA labels
- Focus indicators yang jelas

**User Experience (UX):**
- Consistent navigation patterns di semua halaman
- Clear call-to-action buttons dengan hierarchy
- Loading states dan skeleton screens
- Error states dengan helpful messages
- Success states dengan clear next actions
- Empty states dengan guidance

**Visual Design:**
- Consistent spacing menggunakan Tailwind spacing scale (4px base unit)
- Typography hierarchy yang jelas
- Iconography menggunakan Heroicons (SVG)
- Imagery dengan high-quality photos dan illustrations
- Micro-interactions untuk delight (hover states, transitions, animations)

**Form Design:**
- Clear labels dan placeholders
- Inline validation dengan helpful error messages
- Progress indicators untuk multi-step forms
- Auto-save drafts untuk long forms
- Required field indicators (*)

**Data Visualization:**
- Charts menggunakan Chart.js/ApexCharts
- Color-blind friendly palettes
- Interactive tooltips
- Responsive untuk berbagai screen sizes
- Export capabilities (PNG, SVG, PDF)

##### D. Prototype Interaktif

**[LINK - Figma Prototype: https://figma.com/proto/curheart...]**

Prototype interaktif telah dibuat di Figma dengan fitur:
- Click-through navigation antar halaman
- Hover states dan micro-interactions
- Form validation simulation
- Responsive preview untuk berbagai devices
- Annotation untuk developer handoff
- Design specifications (spacing, colors, typography)
- Component library untuk reusability

##### E. Design Handoff

Dokumentasi lengkap untuk developer mencakup:
- **Component Library**: 50+ reusable components (buttons, cards, forms, modals, tables)
- **Design Tokens**: Colors, typography, spacing, shadows, border-radius
- **Asset Export**: Icons (SVG), images (WebP/PNG), illustrations (SVG)
- **Specifications**: Detailed spacing, sizing, dan positioning
- **Developer Notes**: Implementation guidance, dependencies, edge cases
- **Accessibility Checklist**: Per component accessibility requirements

---

**Ringkasan Desain UI/UX:**

Total **41 halaman mockup** yang mencakup seluruh user journey dari 4 role berbeda (Guest, Client, Therapist, Admin). Semua mockup dirancang dengan prinsip:

✅ **Responsiveness**: Adaptif untuk desktop, tablet, dan mobile  
✅ **Accessibility**: Memenuhi standar WCAG 2.1 AA  
✅ **Consistency**: Mengikuti design system yang telah ditetapkan  
✅ **User-Friendly**: Intuitif dan mudah digunakan  
✅ **Professional**: Mencerminkan kredibilitas layanan kesehatan mental

Desain telah melalui beberapa iterasi berdasarkan feedback dari stakeholder dan usability testing dengan sampel pengguna.

---

_Catatan: BAB IV Part 2 ini merupakan lanjutan dari Part 1. Untuk bagian 4.4-4.7, lihat Part 3 dan Part 4._

---

