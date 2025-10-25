# BRIEF: Design System & Mockup CUR-HEART

## TUJUAN
Membuat design system lengkap dan mockup high-fidelity untuk website CUR-HEART Hypnotherapy & Mind Wellness Center menggunakan HTML + TailwindCSS dengan bahasa Indonesia.

---

## STRUKTUR OUTPUT

### 1. Design System (folder: `design-system/`)
File yang harus dibuat:
- `index.html` - Dokumentasi lengkap design system

### 2. Mockup Pages (folder: `mockups/`)
Setiap halaman = 1 file HTML terpisah dengan konsistensi design.

---

## DESIGN SYSTEM REQUIREMENTS

### Color Palette
**Warna Brand (dari Logo CUR-HEART):**
- **Primary (Navy Blue)**: #1E0E62 - Warna biru navy dari logo, untuk header, CTA utama
- **Primary Light**: #2D1B69 - Variasi lebih terang untuk hover states
- **Primary Dark**: #150A4A - Variasi lebih gelap untuk emphasis
- **Secondary (Coral Red)**: #FF6B7A - Warna merah coral dari logo, untuk aksen dan highlights
- **Secondary Light**: #FF8A96 - Untuk backgrounds dan subtle elements
- **Secondary Dark**: #E64555 - Untuk hover states pada buttons

**Warna Pendukung:**
- **Accent**: #FFB6B9 (Pink hangat) - Untuk informasi positif, badges
- **Warm**: #FFEAA7 (Kuning lembut) - Untuk warnings, highlights
- **Gray Scale**: 
  - 50: #F9FAFB
  - 100: #F3F4F6
  - 200: #E5E7EB
  - 300: #D1D5DB
  - 400: #9CA3AF
  - 500: #6B7280
  - 600: #4B5563
  - 700: #374151
  - 800: #1F2937
  - 900: #111827

**Status Colors:**
- **Success**: #00D26A - Untuk success messages, completed states
- **Warning**: #FFA94D - Untuk warnings, pending states
- **Error**: #FF6B7A - Gunakan secondary color untuk error consistency
- **Info**: #667BC6 - Biru soft untuk informational messages

### Typography
- **Heading Font**: Poppins (Bold 700, Semibold 600)
- **Body Font**: Inter (Regular 400, Medium 500)
- **Font Sizes**: 
  - Display: 48px
  - H1: 36px
  - H2: 30px
  - H3: 24px
  - H4: 20px
  - H5: 18px
  - Body: 16px
  - Small: 14px
  - Caption: 12px

### Spacing System
- Base unit: 4px
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128

### Component Library
Harus mencakup:
1. **Buttons**: Primary, Secondary, Outline, Text, Icon, Loading state
2. **Form Elements**: Input, Textarea, Select, Checkbox, Radio, Toggle, Date picker
3. **Cards**: Info card, Service card, Therapist card, Testimonial card
4. **Navigation**: Navbar, Sidebar, Breadcrumb, Tabs, Pagination
5. **Alerts**: Success, Warning, Error, Info
6. **Modals**: Confirmation, Form, Info
7. **Tables**: Basic, Sortable, Pagination
8. **Badges**: Status, Count, Label
9. **Progress**: Bar, Circle, Steps
10. **Icons**: Menggunakan Font Awesome 6

### Layout Guidelines
- **Container**: max-width 1280px
- **Grid**: 12 kolom responsive
- **Breakpoints**: sm(640px), md(768px), lg(1024px), xl(1280px)

---

## MOCKUP PAGES - LIST LENGKAP

### A. PUBLIC WEBSITE (12 halaman)

#### 1. Homepage (`01_homepage.html`)
- Hero section dengan CTA booking
- Grid 6 layanan terapi
- Statistik & achievements
- Testimonial carousel
- CTA section
- Footer lengkap

#### 2. Tentang Kami (`02_about.html`)
- Hero section
- Visi & Misi
- Tim founder (3 orang dengan foto, role, deskripsi)
- Timeline perjalanan bisnis
- Nilai-nilai perusahaan
- Sertifikasi & kredibilitas

#### 3. Layanan (`03_services.html`)
- Grid 6 layanan utama dengan detail:
  - Stress & Anxiety Release
  - Trauma Healing
  - Self-Confidence & Motivation
  - Sleep & Relaxation
  - Habit Reprogramming
  - Phobia & Fear Management
- Setiap card: ikon, judul, deskripsi, durasi, harga, success rate, button

#### 4. Detail Layanan (`04_service_detail.html`)
- Header layanan
- Deskripsi lengkap metode
- Benefit list
- Proses terapi (timeline)
- Paket harga & perbandingan
- FAQ spesifik layanan
- CTA booking
- Testimoni relevan

#### 5. Terapis (`05_therapists.html`)
- Filter: spesialisasi, bahasa, rating, ketersediaan
- Grid kartu terapis dengan:
  - Foto
  - Nama & gelar
  - Spesialisasi
  - Rating & jumlah klien
  - Bahasa
  - Pengalaman tahun
  - Button lihat profil

#### 6. Profil Terapis (`06_therapist_profile.html`)
- Hero section dengan foto besar
- Info detail: pendidikan, sertifikasi, pengalaman
- Spesialisasi & metode
- Rating & review dari klien
- Jadwal ketersediaan minggu ini
- Statistik (total sesi, klien puas, dll)
- Button booking

#### 7. Blog/Artikel (`07_blog.html`)
- Filter: kategori, tanggal
- Search bar
- Grid artikel dengan thumbnail
- Sidebar: artikel populer, kategori

#### 8. Detail Artikel (`08_blog_detail.html`)
- Header dengan gambar featured
- Konten artikel dengan formatting
- Author info
- Share buttons
- Artikel terkait

#### 9. Kontak (`09_contact.html`)
- Form kontak (nama, email, telepon, subjek, pesan)
- Info kontak: alamat, telp, email, jam operasional
- Google Maps embed
- Social media links
- FAQ umum

#### 10. FAQ (`10_faq.html`)
- Kategori FAQ: Layanan, Pembayaran, Teknis, Umum
- Accordion questions
- Search FAQ
- Contact support CTA

#### 11. Kebijakan Privasi (`11_privacy_policy.html`)
- Structured content dengan TOC
- Section: pengumpulan data, penggunaan, keamanan, hak pengguna

#### 12. Syarat & Ketentuan (`12_terms_conditions.html`)
- Structured content dengan TOC
- Section: layanan, pembayaran, pembatalan, tanggung jawab

---

### B. AUTH PAGES (4 halaman)

#### 13. Login (`13_login.html`)
- Form: email/username, password
- Remember me checkbox
- Forgot password link
- Login button
- Divider "atau"
- Social login (Google, Facebook)
- Link ke register
- Ilustrasi/gambar samping

#### 14. Register (`14_register.html`)
- Tab: Daftar sebagai Klien / Terapis
- Form klien: nama lengkap, email, telepon, password, confirm password, agreement checkbox
- Form terapis: + field nomor izin praktik, spesialisasi, pengalaman
- Register button
- Link ke login
- Social register

#### 15. Lupa Password (`15_forgot_password.html`)
- Input email
- Instruksi pengiriman link reset
- Button kirim
- Link kembali ke login

#### 16. Reset Password (`16_reset_password.html`)
- Input password baru
- Input konfirmasi password
- Password strength indicator
- Button reset
- Success message

---

### C. CLIENT DASHBOARD (10 halaman)

#### 17. Dashboard Overview (`17_client_dashboard.html`)
- Sidebar menu lengkap
- Stats cards: sesi mendatang, sesi selesai, progress, poin
- Grafik progress mingguan
- Upcoming appointments (3 terdekat)
- Quick action buttons
- Rekomendasi layanan

#### 18. Booking Sesi - Step 1 (`18_booking_step1.html`)
- Progress indicator (4 steps)
- Grid pilihan 6 layanan
- Radio selection dengan highlight
- Button lanjut

#### 19. Booking Sesi - Step 2 (`19_booking_step2.html`)
- Progress indicator
- Filter terapis: spesialisasi, bahasa, rating
- Grid kartu terapis dengan info singkat
- Radio selection
- Button kembali & lanjut

#### 20. Booking Sesi - Step 3 (`20_booking_step3.html`)
- Progress indicator
- Kalender tanggal
- Slot waktu tersedia per hari
- Durasi sesi info
- Button kembali & lanjut

#### 21. Booking Sesi - Step 4 (`21_booking_step4.html`)
- Progress indicator
- Ringkasan booking (layanan, terapis, jadwal)
- Total harga
- Pilihan metode pembayaran: Transfer Bank, E-wallet, Kartu Kredit
- Form detail pembayaran
- Terms agreement checkbox
- Button konfirmasi & bayar

#### 22. Booking Success (`22_booking_success.html`)
- Success icon & message
- Ringkasan booking lengkap
- Nomor booking
- Instruksi pembayaran (jika transfer)
- Button: Download invoice, Lihat detail booking, Kembali ke dashboard
- Countdown payment deadline (untuk transfer)

#### 23. Daftar Janji Temu (`23_client_appointments.html`)
- Tab: Mendatang, Selesai, Dibatalkan
- Filter: tanggal, layanan, terapis
- Search bar
- List appointment dengan card:
  - Tanggal & waktu
  - Layanan & terapis
  - Status (label badge)
  - Action buttons: Detail, Reschedule, Cancel, Join (video)

#### 24. Detail Janji Temu (`24_appointment_detail.html`)
- Header dengan status
- Info lengkap: layanan, terapis, jadwal, lokasi/online
- Catatan klien (editable sebelum sesi)
- Riwayat komunikasi
- Action buttons sesuai status
- Button join video call (jika online & waktunya tiba)

#### 25. Progress Tracking (`25_client_progress.html`)
- Timeline sesi yang sudah dilakukan
- Grafik progress per metrik (anxiety level, sleep quality, confidence level)
- Milestone achievements dengan badge
- Catatan dari terapis per sesi
- Mood journal calendar
- Export report button

#### 26. Pesan/Chat (`26_client_messages.html`)
- Sidebar: list konversasi dengan terapis
- Main area: chat window
- Input message dengan attachment
- Online status indicator
- Notifikasi unread

---

### D. THERAPIST DASHBOARD (10 halaman)

#### 27. Dashboard Terapis (`27_therapist_dashboard.html`)
- Sidebar menu terapis
- Stats cards: sesi hari ini, klien aktif, rating, pendapatan bulan ini
- Jadwal hari ini (list appointment)
- Klien baru minggu ini
- Notifikasi & reminder
- Quick stats grafik: sesi per minggu, pendapatan per bulan

#### 28. Jadwal Saya (`28_therapist_schedule.html`)
- Kalender bulanan dengan indikator sesi
- Filter: tipe layanan, status
- List sesi per hari dengan detail
- Color coding per layanan
- Button: Atur ketersediaan, Block time

#### 29. Atur Ketersediaan (`29_therapist_availability.html`)
- Kalender untuk set available dates
- Slot waktu per hari (multi select)
- Recurring schedule pattern
- Block dates (cuti, libur)
- Working hours default
- Save button

#### 30. Klien Saya (`30_therapist_clients.html`)
- Filter: status, layanan, join date
- Search klien
- Grid/list klien dengan:
  - Nama & foto
  - Layanan diambil
  - Total sesi
  - Last session date
  - Progress indicator
  - Button: Lihat profil, Kirim pesan

#### 31. Profil Klien (`31_client_profile_view.html`)
- Header info klien (nama, umur, kontak)
- Layanan yang diikuti
- Riwayat sesi lengkap
- Progress tracking grafik
- Catatan penting
- Medical history (jika ada)
- Button: Edit notes, Schedule session, Send message

#### 32. Ruang Sesi (`32_session_room.html`)
- Video call interface (fullscreen option)
- Timer sesi
- Sidebar: client info, session notes (real-time typing)
- Tools: Whiteboard, Screen share, Recording
- Button: Mute, Camera, End session
- Emergency contact button

#### 33. Catatan Sesi (`33_session_notes.html`)
- Header: pilih klien & sesi
- Form catatan:
  - Tanggal & durasi aktual
  - Topik pembahasan
  - Observasi klien
  - Teknik yang digunakan
  - Homework untuk klien
  - Rencana sesi berikutnya
  - Assessment rating (anxiety, engagement, homework completion)
  - Risk assessment checklist
- Template notes (predefined)
- Save & send to client

#### 34. Riwayat Sesi Klien (`34_therapist_session_history.html`)
- Filter klien
- Timeline semua sesi klien
- Expandable cards per sesi
- Progress visualization
- Export button

#### 35. Pendapatan (`35_therapist_earnings.html`)
- Summary cards: bulan ini, minggu ini, rata-rata per klien, total
- Grafik pendapatan 6 bulan terakhir
- List transaksi: tanggal, klien, layanan, jumlah, status
- Filter: periode, status pembayaran
- Export ke Excel/PDF
- Payment analytics: breakdown per layanan

#### 36. Profil Terapis Edit (`36_therapist_profile_edit.html`)
- Form edit profil:
  - Upload foto
  - Bio & deskripsi
  - Pendidikan (dynamic add)
  - Sertifikasi (dynamic add)
  - Spesialisasi (multi select)
  - Bahasa (multi select)
  - Tarif per layanan
  - Social media links
- Preview profil publik
- Save button

---

### E. ADMIN DASHBOARD (Optional - 5 halaman)

#### 37. Admin Dashboard (`37_admin_dashboard.html`)
- Stats overview: total users, total sessions, revenue, active therapists
- Grafik: registrasi bulanan, revenue trend, popular services
- Recent activities
- Quick actions

#### 38. User Management (`38_admin_users.html`)
- Tab: Klien, Terapis, Admin
- Table users dengan: nama, email, join date, status, actions
- Filter & search
- Actions: View, Edit, Deactivate, Delete

#### 39. Booking Management (`39_admin_bookings.html`)
- Table semua booking
- Filter: status, tanggal, layanan, terapis
- Action: View detail, Cancel, Refund

#### 40. Laporan Keuangan (`40_admin_financial.html`)
- Revenue summary cards
- Grafik revenue harian/bulanan/tahunan
- Top performing services
- Top earning therapists
- Export laporan

#### 41. Settings (`41_admin_settings.html`)
- Tab: General, Services, Payment, Email, Notifications
- Form konfigurasi masing-masing
- Save changes button

---

## CONSISTENCY RULES

### Semua Mockup Harus Memiliki:
1. **Navbar konsisten** (logo, menu, CTA login/register atau user dropdown)
2. **Footer konsisten** (info kontak, quick links, social media, copyright)
3. **Color palette konsisten** sesuai design system
4. **Typography konsisten** (Poppins untuk heading, Inter untuk body)
5. **Spacing konsisten** menggunakan Tailwind spacing scale
6. **Component style konsisten** (buttons, cards, forms menggunakan komponen dari design system)
7. **Responsive design** dengan breakpoint Tailwind
8. **Loading states** & empty states di setiap list/table
9. **Error handling** visual di form
10. **Accessibility**: alt text, ARIA labels, keyboard navigation support

### Konvensi Penamaan File:
- Format: `{nomor}_{nama_halaman}.html`
- Lowercase dengan underscore
- Urut sesuai flow user

### Struktur HTML Konsisten:
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Judul Halaman - CUR-HEART</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'cur-primary': '#1E0E62',
                        'cur-primary-light': '#2D1B69',
                        'cur-primary-dark': '#150A4A',
                        'cur-secondary': '#FF6B7A',
                        'cur-secondary-light': '#FF8A96',
                        'cur-secondary-dark': '#E64555',
                        'cur-accent': '#FFB6B9',
                        'cur-warm': '#FFEAA7',
                        'cur-success': '#00D26A',
                        'cur-warning': '#FFA94D',
                        'cur-error': '#FF6B7A',
                        'cur-info': '#667BC6',
                        'cur-gray-50': '#F9FAFB',
                        'cur-gray-100': '#F3F4F6',
                        'cur-gray-200': '#E5E7EB',
                        'cur-gray-300': '#D1D5DB',
                        'cur-gray-400': '#9CA3AF',
                        'cur-gray-500': '#6B7280',
                        'cur-gray-600': '#4B5563',
                        'cur-gray-700': '#374151',
                        'cur-gray-800': '#1F2937',
                        'cur-gray-900': '#111827',
                    },
                    fontFamily: {
                        'poppins': ['Poppins', 'sans-serif'],
                        'inter': ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
</head>
<body class="font-inter bg-gray-50">
    <!-- Content here -->
</body>
</html>
```

---

## DESIGN PRINCIPLES

1. **Modern & Professional**: Clean, spacious, tidak ramai
2. **Calming & Therapeutic**: Warna lembut, rounded corners, soft shadows
3. **Trust & Credibility**: Tampilkan sertifikasi, testimonial, statistik
4. **User-Friendly**: Navigasi jelas, CTA menonjol, form sederhana
5. **Mobile-First**: Responsive di semua device
6. **Fast & Lightweight**: Hindari gambar berat, optimasi loading

---

## DELIVERABLES

### Folder Structure:
```
tugas-selesai/06_rintisan_bisnis_digital/
├── design-system/
│   └── index.html (dokumentasi lengkap design system)
└── mockups/
    ├── 01_homepage.html
    ├── 02_about.html
    ├── ... (semua 41 file mockup)
    └── 41_admin_settings.html
```

### Quality Checklist:
- [ ] Semua 41 mockup sudah dibuat
- [ ] Design system terdokumentasi lengkap
- [ ] Konsistensi visual 100%
- [ ] Responsive di semua breakpoint
- [ ] Semua component library sudah ada
- [ ] Bahasa Indonesia di semua konten
- [ ] Tidak ada placeholder/lorem ipsum di teks penting
- [ ] Semua link/button memiliki state (hover, active, disabled)
- [ ] Form validation visual
- [ ] Loading & empty states ada

---

## NOTES
- Gunakan data/konten realistis dari profil bisnis yang dilampirkan
- Mockup harus interaktif (hover effects, transitions) walaupun static HTML
- Fokus pada visual fidelity tinggi, bukan fungsionalitas backend
- Setiap halaman standalone (bisa dibuka sendiri tanpa dependencies)
- Comment di code untuk section penting
- Gunakan semantic HTML5 tags

---

**Target**: Hasil akhir adalah 1 design system file + 41 mockup file yang siap dipresentasikan/demo kepada stakeholder, dengan kualitas production-ready visual.
