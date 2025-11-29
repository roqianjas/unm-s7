# BAB IV (Lanjutan)
# ANALISA DAN PERANCANGAN APLIKASI START-UP

### 4.1.4. Rancangan User Interface

Rancangan User Interface (UI) CUR-HEART telah dibuat menggunakan Figma dengan total 66 halaman mockup yang mencakup semua peran pengguna. Desain mengikuti prinsip user-centered design dengan fokus pada kemudahan penggunaan, aksesibilitas, dan pengalaman pengguna yang optimal.

#### A. Design System

**Color Palette**:
- **Primary Color**: Teal (#0D9488)
  - Melambangkan ketenangan, profesionalisme, dan penyembuhan
  - Digunakan untuk: Button primary, link, header
  
- **Secondary Color**: Purple (#9333EA)
  - Melambangkan spiritualitas dan transformasi
  - Digunakan untuk: Accent elements, highlights
  
- **Accent Color**: Orange (#F59E0B)
  - Melambangkan energi dan optimisme
  - Digunakan untuk: Call-to-action, notifications
  
- **Neutral Colors**: Skala abu-abu dari #F9FAFB (lightest) hingga #111827 (darkest)
  - Digunakan untuk: Background, text, borders
  
- **Semantic Colors**:
  - Success: Green (#10B981)
  - Warning: Yellow (#F59E0B)
  - Error: Red (#EF4444)
  - Info: Blue (#3B82F6)

**Typography**:
- **Font Family**: Inter (Sans-serif)
  - Modern, clean, dan mudah dibaca
  - Mendukung berbagai weight (300-900)
  
- **Font Sizes**:
  - H1: 36px (2.25rem) - Page titles
  - H2: 30px (1.875rem) - Section titles
  - H3: 24px (1.5rem) - Subsection titles
  - H4: 20px (1.25rem) - Card titles
  - Body: 16px (1rem) - Regular text
  - Small: 14px (0.875rem) - Helper text, captions
  - Tiny: 12px (0.75rem) - Labels, badges

**Spacing System** (Tailwind CSS scale):
- 0.25rem (4px), 0.5rem (8px), 0.75rem (12px), 1rem (16px)
- 1.5rem (24px), 2rem (32px), 3rem (48px), 4rem (64px)

**Border Radius**:
- Small: 0.25rem (4px) - Buttons, inputs
- Medium: 0.5rem (8px) - Cards
- Large: 1rem (16px) - Modals, large cards
- Full: 9999px - Pills, avatars

**Shadows**:
- Small: 0 1px 2px rgba(0,0,0,0.05)
- Medium: 0 4px 6px rgba(0,0,0,0.1)
- Large: 0 10px 15px rgba(0,0,0,0.1)

#### B. Mockup Halaman Utama

Berikut adalah daftar mockup untuk halaman-halaman kunci dalam sistem CUR-HEART. Semua mockup lengkap (66 halaman) tersedia di folder `01_desain/mockup/`.

**1. Halaman Publik (12 halaman)**

**Gambar 4.5 Mockup Landing Page (Homepage)**  
File: `01_desain/mockup/01_homepage.jpg`  
Sumber: Hasil Penelitian (Figma Design)

Halaman landing page menampilkan hero section dengan CTA "Book Your Session Now", statistics section (500+ Clients, 15+ Therapists, 4.8/5 Rating), services grid dengan 6 layanan terapi, featured therapists dengan foto dan rating, client testimonials carousel, dan footer dengan links dan contact info.

**Gambar 4.6 Mockup Halaman Tentang Kami**  
File: `01_desain/mockup/02_about.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.7 Mockup Katalog Layanan**  
File: `01_desain/mockup/03_services.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.8 Mockup Detail Layanan**  
File: `01_desain/mockup/04_service_detail.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.9 Mockup Direktori Terapis**  
File: `01_desain/mockup/05_therapists.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.10 Mockup Profil Terapis**  
File: `01_desain/mockup/06_therapist_profile.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.11 Mockup Daftar Blog**  
File: `01_desain/mockup/07_blog.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.12 Mockup Detail Blog**  
File: `01_desain/mockup/08_blog_detail.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.13 Mockup Hubungi Kami**  
File: `01_desain/mockup/09_contact.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.14 Mockup FAQ**  
File: `01_desain/mockup/10_faq.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.15 Mockup Kebijakan Privasi**  
File: `01_desain/mockup/11_privacy_policy.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.16 Mockup Syarat & Ketentuan**  
File: `01_desain/mockup/12_terms_conditions.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**2. Halaman Autentikasi (4 halaman)**

**Gambar 4.17 Mockup Login**  
File: `01_desain/mockup/13_login.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.18 Mockup Registrasi Klien**  
File: `01_desain/mockup/14_register_klien.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.19 Mockup Registrasi Terapis**  
File: `01_desain/mockup/14_register_terapis.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.20 Mockup Lupa Kata Sandi**  
File: `01_desain/mockup/15_forgot_password.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.21 Mockup Reset Kata Sandi**  
File: `01_desain/mockup/16_reset_password.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**3. Dashboard Klien (12 halaman)**

**Gambar 4.22 Mockup Dashboard Klien**  
File: `01_desain/mockup/17_client_dashboard.jpg`  
Sumber: Hasil Penelitian (Figma Design)

Dashboard klien menampilkan welcome message, 4 stat cards (Upcoming Sessions, Completed, Total Hours, Progress), next appointment card dengan detail lengkap, progress tracking chart (line chart mood score), recent sessions list dengan status dan rating, serta responsive layout dengan clean design.

**Gambar 4.23 Mockup Booking Step 1 - Select Service**  
File: `01_desain/mockup/18_booking_step1.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.24 Mockup Booking Step 2 - Select Therapist**  
File: `01_desain/mockup/19_booking_step2.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.25 Mockup Booking Step 3 - Select Schedule**  
File: `01_desain/mockup/20_booking_step3.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.26 Mockup Booking Step 4 - Konfirmasi & Pembayaran**  
File: `01_desain/mockup/21_booking_step4.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.27 Mockup Booking Success**  
File: `01_desain/mockup/22_booking_success.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.28 Mockup Janji Temu Saya**  
File: `01_desain/mockup/23_client_appointments.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.29 Mockup Detail Janji Temu**  
File: `01_desain/mockup/24_appointment_detail.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.30 Mockup Progress Tracking**  
File: `01_desain/mockup/25_client_progress.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.31 Mockup Pesan (Chat)**  
File: `01_desain/mockup/26_client_messages.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.32 Mockup Pengaturan Klien**  
File: `01_desain/mockup/27_client_settings.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.33 Mockup Notifikasi Klien**  
File: `01_desain/mockup/28_client_notifications.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**4. Dashboard Terapis (13 halaman)**

**Gambar 4.34 Mockup Dashboard Terapis**  
File: `01_desain/mockup/29_therapist_dashboard.jpg`  
Sumber: Hasil Penelitian (Figma Design)

Dashboard terapis menampilkan good morning greeting, 4 stat cards (Today's Sessions, This Week, Total Clients, Avg Rating), today's schedule list dengan detail setiap sesi, pending documentation alert dengan action button, earnings this month card dengan total dan withdrawal button, serta professional clean interface.

**Gambar 4.35 Mockup Manajemen Jadwal**  
File: `01_desain/mockup/30_therapist_schedule.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.36 Mockup Pengaturan Ketersediaan**  
File: `01_desain/mockup/31_therapist_availability.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.37 Mockup Daftar Klien**  
File: `01_desain/mockup/32_therapist_clients.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.38 Mockup Profil Klien (View)**  
File: `01_desain/mockup/33_client_profile_view.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.39 Mockup Ruang Sesi**  
File: `01_desain/mockup/34_session_room.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.40 Mockup Formulir Catatan Sesi**  
File: `01_desain/mockup/35_session_notes.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.41 Mockup Riwayat Sesi**  
File: `01_desain/mockup/36_therapist_session_history.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.42 Mockup Dashboard Pendapatan**  
File: `01_desain/mockup/37_therapist_earnings.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.43 Mockup Edit Profil Terapis**  
File: `01_desain/mockup/38_therapist_profile_edit.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.44 Mockup Pengaturan Terapis**  
File: `01_desain/mockup/39_therapist_settings.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.45 Mockup Pesan Terapis**  
File: `01_desain/mockup/40_therapist_messages.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.46 Mockup Notifikasi Terapis**  
File: `01_desain/mockup/41_therapist_notification.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**5. Dashboard Admin (25 halaman)**

**Gambar 4.47 Mockup Dashboard Admin**  
File: `01_desain/mockup/42_admin_dashboard.jpg`  
Sumber: Hasil Penelitian (Figma Design)

Dashboard admin menampilkan 4 KPI cards (Total Users, Total Bookings, Total Therapists, Revenue), revenue trend chart (line chart 12 months), recent bookings table dengan pagination, pending actions alert (therapist applications, withdrawals, reviews), top performing therapists list, serta comprehensive admin interface.

**Gambar 4.48 Mockup Manajemen Reservasi**  
File: `01_desain/mockup/43_admin_bookings.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.49 Mockup Manajemen Pengguna**  
File: `01_desain/mockup/44_admin_users.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.50 Mockup Laporan Keuangan**  
File: `01_desain/mockup/45_admin_financial.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.51 Mockup Pengaturan Sistem**  
File: `01_desain/mockup/46_admin_settings.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.52 Mockup Notifikasi Admin**  
File: `01_desain/mockup/47_admin_notifications.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.53 Mockup Pesan Admin**  
File: `01_desain/mockup/48_admin_messages.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.54 Mockup Detail Pengguna**  
File: `01_desain/mockup/49_admin_user_detail.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.55 Mockup Edit Pengguna**  
File: `01_desain/mockup/50_admin_user_edit.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.56 Mockup Detail Reservasi**  
File: `01_desain/mockup/51_admin_booking_detail.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.57 Mockup Manajemen Transaksi**  
File: `01_desain/mockup/52_admin_transactions.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.58 Mockup Manajemen Penarikan**  
File: `01_desain/mockup/53_admin_withdrawals.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.59 Mockup Detail Penarikan**  
File: `01_desain/mockup/54_admin_withdrawal_detail.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.60 Mockup Log Aktivitas**  
File: `01_desain/mockup/55_admin_activity_log.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.61 Mockup Laporan & Analitik**  
File: `01_desain/mockup/56_admin_reports.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.62 Mockup Manajemen Konten Blog**  
File: `01_desain/mockup/57_admin_content_blog.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.63 Mockup Manajemen Konten FAQ**  
File: `01_desain/mockup/58_admin_content_faq.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.64 Mockup Manajemen Konten Layanan**  
File: `01_desain/mockup/59_admin_content_services.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.65 Mockup Manajemen Ulasan**  
File: `01_desain/mockup/60_admin_reviews.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.66 Mockup Manajemen Promo**  
File: `01_desain/mockup/61_admin_promo.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.67 Mockup Verifikasi Terapis**  
File: `01_desain/mockup/62_admin_therapist_verification.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.68 Mockup Editor Blog**  
File: `01_desain/mockup/63_admin_blog_editor.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.69 Mockup Editor FAQ**  
File: `01_desain/mockup/64_admin_faq_editor.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.70 Mockup Editor Layanan**  
File: `01_desain/mockup/65_admin_service_editor.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.71 Mockup Editor Promo**  
File: `01_desain/mockup/66_admin_promo_editor.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Catatan**: Semua file mockup dalam format JPG tersedia di folder `tugas-selesai/06_rintisan_bisnis_digital/01_desain/mockup/`. Total 66 halaman mockup mencakup seluruh user journey untuk semua peran pengguna (Guest, Client, Therapist, Admin)

**Gambar 4.5 Mockup Landing Page CUR-HEART**  
File: `01_desain/mockup/01_homepage.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.6 Mockup Booking Step 1 - Select Service**  
File: `01_desain/mockup/18_booking_step1.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.7 Mockup Client Dashboard**  
File: `01_desain/mockup/17_client_dashboard.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.8 Mockup Therapist Dashboard**  
File: `01_desain/mockup/29_therapist_dashboard.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Gambar 4.9 Mockup Admin Dashboard**  
File: `01_desain/mockup/42_admin_dashboard.jpg`  
Sumber: Hasil Penelitian (Figma Design)

**Catatan**: Semua mockup lengkap (66 halaman) tersedia di folder `tugas-selesai/06_rintisan_bisnis_digital/01_desain/mockup/` dalam format JPG. Mockup mencakup:
- 12 halaman public pages
- 4 halaman authentication
- 12 halaman client dashboard
- 13 halaman therapist dashboard
- 25 halaman admin dashboard

**Prinsip Desain yang Diterapkan**:
1. **Consistency**: Penggunaan design system yang konsisten di seluruh halaman
2. **Clarity**: Informasi disajikan dengan jelas dan mudah dipahami
3. **Efficiency**: Minimize clicks untuk menyelesaikan tugas
4. **Feedback**: Provide clear feedback untuk setiap aksi pengguna
5. **Accessibility**: Comply dengan WCAG 2.1 Level AA
6. **Responsive**: Desain yang adapt dengan berbagai ukuran layar


### 4.1.5. Rancangan Database

Rancangan database sistem informasi CUR-HEART menggunakan Entity Relationship Diagram (ERD) dan Logical Record Structure (LRS) yang telah dinormalisasi hingga Third Normal Form (3NF) untuk menghindari redundansi data dan menjaga integritas data.

#### A. Entity Relationship Diagram (ERD)

ERD menggambarkan struktur database dengan 16 tabel utama dan relationships antar entitas.

**Gambar 4.10 Entity Relationship Diagram (ERD) CUR-HEART**  
File: `01_desain/database/erd_diagram.png`  
Sumber: Hasil Penelitian (dbdiagram.io)

**Penjelasan Entitas Utama**:

**1. users** - Tabel induk untuk semua pengguna sistem
- Menyimpan data universal: name, email, password, role (client/therapist/admin)
- Relasi 1:1 dengan clients atau therapists tergantung role

**2. clients** - Data spesifik klien
- Extends dari users dengan data tambahan: phone, address, dob, gender
- Relasi 1:M dengan bookings (satu klien bisa punya banyak booking)

**3. therapists** - Data spesifik terapis
- Extends dari users dengan data profesional: specialization, experience, license_no, bio, rating
- Relasi M:M dengan services melalui therapist_services
- Relasi 1:M dengan bookings

**4. services** - Katalog layanan terapi
- Menyimpan: name, description, duration, price, category, status
- Relasi M:M dengan therapists

**5. therapist_services** - Junction table untuk M:M relationship
- Menghubungkan therapists dan services
- Memungkinkan satu terapis menangani banyak layanan

**6. therapist_availability** - Jadwal ketersediaan terapis
- Menyimpan jadwal per hari: day_of_week, start_time, end_time, is_available
- Digunakan untuk checking ketersediaan saat booking

**7. bookings** - Data reservasi
- Core table yang menghubungkan client, therapist, service
- Menyimpan: booking_date, start_time, end_time, type (online/offline), status, total_price
- Relasi 1:1 dengan payments
- Relasi 1:1 dengan sessions

**8. payments** - Transaksi pembayaran
- Menyimpan: amount, method, status, paid_at, midtrans_id
- Terintegrasi dengan Midtrans payment gateway

**9. sessions** - Data sesi terapi yang sudah dilaksanakan
- Menyimpan: session_date, start_time, end_time, status
- Relasi 1:M dengan session_notes

**10. session_notes** - Catatan dokumentasi sesi
- Menyimpan: technique, observation, progress, notes, recommendation
- Diisi oleh terapis setelah sesi

**11. reviews** - Ulasan dan rating dari klien
- Menyimpan: rating (1-5), comment
- Relasi dengan booking, client, therapist

**12. promo_codes** - Kode promo dan diskon
- Menyimpan: code, discount_type, discount_value, valid_from, valid_until, usage_limit

**13. notifications** - Notifikasi untuk pengguna
- Menyimpan: type, title, message, read_at
- Relasi dengan users

**14. messages** - Pesan/chat antara pengguna
- Menyimpan: sender_id, receiver_id, booking_id, message, read_at
- Untuk komunikasi klien-terapis

**15. withdrawals** - Permintaan penarikan dana terapis
- Menyimpan: amount, status, requested_at, processed_at
- Relasi dengan therapists

**16. activity_logs** - Log aktivitas untuk audit trail
- Menyimpan: action, description, ip_address, user_agent
- Untuk security dan compliance

**17. system_settings** - Konfigurasi sistem
- Menyimpan: key-value pairs untuk settings
- Contoh: site_name, maintenance_mode, payment_gateway_key

#### B. Logical Record Structure (LRS)

LRS menunjukkan struktur logis dari tabel-tabel database dengan detail field, tipe data, dan constraints.

**Gambar 4.11 Logical Record Structure (LRS) CUR-HEART**  
File: `01_desain/database/lrs_structure.png`  
Sumber: Hasil Penelitian

**Normalisasi Database**:

Database CUR-HEART telah dinormalisasi hingga **Third Normal Form (3NF)** dengan karakteristik:

**1NF (First Normal Form)**:
- Setiap kolom berisi nilai atomic (tidak ada multi-value)
- Setiap baris unik (ada primary key)
- Tidak ada repeating groups

**2NF (Second Normal Form)**:
- Memenuhi 1NF
- Tidak ada partial dependency (semua non-key attributes fully dependent pada primary key)
- Contoh: therapist_services terpisah dari therapists dan services

**3NF (Third Normal Form)**:
- Memenuhi 2NF
- Tidak ada transitive dependency (non-key attributes tidak dependent pada non-key attributes lain)
- Contoh: clients dan therapists terpisah dari users untuk menghindari null values

**Indexing Strategy**:

Untuk optimasi performa query, diterapkan indexing pada:
- Primary keys (automatic)
- Foreign keys (untuk JOIN operations)
- Kolom yang sering di-query: email, status, booking_date, created_at
- Composite index untuk query kombinasi: (user_id, read_at) pada notifications

**Data Integrity**:

- **Referential Integrity**: Foreign key constraints untuk menjaga konsistensi relasi
- **Domain Integrity**: ENUM types untuk membatasi nilai yang valid
- **Entity Integrity**: Primary key NOT NULL dan UNIQUE
- **User-defined Integrity**: CHECK constraints dan triggers untuk business rules

File schema SQL lengkap tersedia di: `tugas-selesai/06_rintisan_bisnis_digital/01_desain/database/schema.sql`
