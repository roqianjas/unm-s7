# 06 - PRESENTASI

Folder ini berisi semua material presentasi final Capstone Project CUR-HEART, termasuk slide PowerPoint, video demo sistem, dan script presentasi.

---

## 📁 Struktur Folder

```
06_presentasi/
├── README.md                                  # File ini
├── slide_presentasi_curheart.pptx            # Slide PowerPoint final (15-20 slides)
├── slide_presentasi_curheart.pdf             # PDF version (untuk backup)
├── video_demo_sistem.mp4                     # Video demo sistem (5-7 menit)
├── video_demo_short.mp4                      # Short version (2-3 menit)
├── script_presentasi.docx                    # Script lengkap presentasi
├── speaker_notes.pdf                         # Catatan pembicara
├── backup/                                    # Folder backup & alternatif
│   ├── slide_v1.pptx
│   ├── slide_v2.pptx
│   └── slide_final_backup.pptx
└── assets/                                    # Assets untuk presentasi
    ├── logo_curheart.png
    ├── logo_unm.png
    ├── team_photo.jpg
    └── qr_code_demo.png
```

---

## 📊 Struktur Slide Presentasi (15-20 Slides)

### Slide Breakdown:

```
SLIDE 1: COVER
├── Judul: "Sistem Informasi Manajemen Booking dan Layanan
│           Terapi Hypnotherapy Berbasis Web (CUR-HEART)"
├── Logo: UNM + CUR-HEART
├── Tim: Roki Anjas, Susanto, Fahruroji
└── Mata Kuliah: Capstone Project (6 MK Terintegrasi)

SLIDE 2: AGENDA
├── 1. Latar Belakang
├── 2. Rumusan Masalah
├── 3. Tujuan Penelitian
├── 4. Metodologi
├── 5. Hasil & Pembahasan
├── 6. Demo Sistem
├── 7. Kesimpulan & Saran
└── 8. Q&A

SLIDE 3: LATAR BELAKANG
├── Problem Statement (3 poin):
│   • Booking manual via WhatsApp (15-20 menit/booking)
│   • Tidak ada tracking progress klien
│   • Laporan keuangan manual (4-5 jam/minggu)
├── Solution: Sistem informasi berbasis web
└── Impact: Efisiensi 85%, ROI 210%

SLIDE 4: PROFIL CUR-HEART
├── Tentang CUR-HEART:
│   • Klinik hypnotherapy di Makassar
│   • 3 terapis profesional (bersertifikat)
│   • 150+ klien aktif
├── Layanan:
│   • Stress Management (Rp 350K/sesi)
│   • Confidence Building (Rp 400K)
│   • Weight Management (Rp 450K)
│   • Quit Smoking (Rp 500K)
│   • Past Life Regression (Rp 600K)
└── Jam Operasional: Senin-Sabtu, 09:00-18:00

SLIDE 5: RUMUSAN MASALAH
├── 7 Masalah Utama:
│   1. Proses booking tidak efisien (manual, 15-20 min)
│   2. Tidak ada reminder otomatis → banyak no-show
│   3. Payment tracking manual → error prone
│   4. Tidak ada history sesi terapi klien
│   5. Laporan keuangan lambat (4-5 jam/minggu)
│   6. Kesulitan manage jadwal 3 terapis
│   7. Tidak ada sistem rating & review
└── Urgency: High (90% proses masih manual)

SLIDE 6: TUJUAN PENELITIAN
├── Tujuan Utama: Mengembangkan sistem informasi terintegrasi
├── Tujuan Spesifik (5):
│   1. Otomasi booking (reduce time 85%)
│   2. Payment integration (Midtrans)
│   3. Session management (SOAP notes)
│   4. Progress tracking (visualisasi grafik)
│   5. Financial reporting (real-time)
└── Target: Sistem live dalam 11 minggu

SLIDE 7: METODOLOGI PENELITIAN
├── Framework: SDLC Waterfall (6 fase)
├── Timeline: 11 minggu (16 Sept - 1 Nov 2024)
├── Teknik Pengumpulan Data:
│   • Wawancara (3 stakeholder)
│   • Observasi (3 sesi, 12 jam)
│   • Survey (36 responden)
│   • Dokumentasi (foto, video, dokumen)
├── Tools: Laravel 10, MySQL 8, Tailwind CSS
└── Team: 3 orang (PM, UI/UX, Full-stack)

SLIDE 8: ARSITEKTUR SISTEM
├── Visual: Diagram arsitektur MVC
├── Komponen:
│   • Frontend: Blade + Tailwind CSS + JavaScript
│   • Backend: Laravel 10 (PHP 8.2)
│   • Database: MySQL 8.0 (16 tabel, 3NF)
│   • Payment: Midtrans Gateway
│   • Email: SMTP/Gmail
└── Hosting: VPS (cPanel, SSL)

SLIDE 9: DATABASE DESIGN
├── Visual: Entity Relationship Diagram (ERD)
├── Statistik:
│   • 16 tabel (normalized 3NF)
│   • 22 foreign key constraints
│   • 25 indexes (query optimization)
│   • 150+ test data records
└── Key Tables: users, clients, therapists, bookings, payments

SLIDE 10: FITUR UTAMA SISTEM
├── 4 User Roles:
│   • Guest: 8 fitur (browse, contact, FAQ)
│   • Client: 15 fitur (booking, payment, progress tracking)
│   • Therapist: 10 fitur (schedule, session notes, earnings)
│   • Admin: 7 fitur (user management, reports, settings)
├── Total: 40 fitur fungsional
└── Highlight: Booking 4-step wizard, Midtrans payment, SOAP notes

SLIDE 11: USER INTERFACE DESIGN
├── Visual: Grid 6 screenshot mockup (terbaik)
│   • Landing page (modern, clean)
│   • Booking wizard (step-by-step)
│   • Client dashboard (progress chart)
│   • Therapist session room (SOAP form)
│   • Admin dashboard (statistics)
│   • Payment gateway (Midtrans)
├── Design System:
│   • Color: Navy Blue (#1E0E62), Pink (#FF6B7A)
│   • Font: Poppins (heading), Inter (body)
└── Total: 41 halaman (responsive)

SLIDE 12: HASIL TESTING
├── Unit Testing:
│   • Coverage: 80% (target: 75%)
│   • 120 test cases, 100% passed
├── Feature Testing:
│   • 40 features tested
│   • Success rate: 100%
├── User Acceptance Testing (UAT):
│   • 30 scenarios
│   • 3 days testing with client
│   • Success rate: 93.3% (28/30 passed)
│   • User satisfaction: 4.5/5.0
└── Performance: Load time < 2 detik (target: < 3s)

SLIDE 13: DEPLOYMENT & GO-LIVE
├── Deployment Timeline:
│   • Server setup: 2 hari
│   • Database migration: 1 hari
│   • Testing production: 1 hari
│   • Training: 2 hari (admin + therapist)
│   • Go-live: 1 Nov 2024 ✅
├── Training Delivered:
│   • User Manual (3 dokumen, 90 halaman)
│   • Technical Documentation (4 dokumen, 107 halaman)
│   • Video Tutorial (5 video, total 45 menit)
└── Support: 3-month warranty + email/phone support

SLIDE 14: DAMPAK & MANFAAT
├── Efisiensi Operasional:
│   • Booking time: 15-20 min → 2-3 min (85% faster)
│   • Payment processing: 5-10 min → 1 min (90% faster)
│   • Report generation: 4-5 jam → 5 menit (98% faster)
├── Financial Impact:
│   • Development cost: Rp 135 juta
│   • Annual benefit: Rp 283 juta
│   • ROI: 210% (payback period: 5.7 bulan)
├── User Satisfaction:
│   • Client: 4.3/5.0 (improved from 3.2)
│   • Therapist: 4.5/5.0
│   • Admin: 4.7/5.0
└── Business Growth: Projected 40% increase in bookings

SLIDE 15: KESIMPULAN
├── 5 Kesimpulan Utama:
│   1. ✅ Sistem berhasil dikembangkan (41 pages, 40 features)
│   2. ✅ SDLC Waterfall efektif (11 minggu, on-schedule)
│   3. ✅ Teknologi Laravel + MySQL + Tailwind solid
│   4. ✅ Testing comprehensive (93.3% UAT success)
│   5. ✅ ROI sangat menguntungkan (210%, payback 5.7 bulan)
└── Status: ✅ Production-ready, GO-LIVE 1 Nov 2024

SLIDE 16: SARAN
├── Saran Pengembangan (6):
│   1. Integrasi video call (Zoom/Jitsi) untuk online therapy
│   2. Mobile app (Flutter/React Native)
│   3. AI chatbot untuk FAQ automation
│   4. Multi-language support (EN, ID)
│   5. Export PDF untuk laporan & invoice
│   6. Integration dengan Google Calendar
└── Timeline: Phase 2 (Q1 2025)

SLIDE 17: DEMO SISTEM (VIDEO)
├── Embedded video demo (2-3 menit) atau
├── Live demo link (QR code)
└── Highlight:
    • Client booking flow (30 detik)
    • Payment integration (20 detik)
    • Therapist session management (30 detik)
    • Admin dashboard & reports (30 detik)
    • Mobile responsive (20 detik)

SLIDE 18: KONTRIBUSI PENELITIAN
├── Kontribusi Akademik:
│   • Framework integrasi 6 mata kuliah Capstone
│   • Metodologi SDLC untuk hypnotherapy system
│   • Case study CRM + Booking system
├── Kontribusi Praktis:
│   • Real system deployed (production-ready)
│   • ROI analysis untuk SME digitalization
│   • Template sistem booking untuk service-based business
└── Publikasi: Target jurnal nasional (Sinta 2-4)

SLIDE 19: Q&A
├── Visual: Foto tim + kontak
├── Contact Information:
│   • Email: curheart@example.com
│   • Website: https://curheart.com
│   • GitHub: github.com/curheart-project
├── Team:
│   • Roki Anjas (PM): roki.anjas@unm.ac.id
│   • Susanto (UI/UX): susanto@unm.ac.id
│   • Fahruroji (Dev): fahruroji@unm.ac.id
└── QR Code: Link ke demo sistem

SLIDE 20: THANK YOU
├── "Terima Kasih"
├── Logo UNM + CUR-HEART
└── Foto Tim (professional photo)
```

**Total Slides**: 20 slides (estimasi 20-25 menit presentasi)

---

## 🎬 Video Demo Sistem

### Video 1: Full Demo (5-7 menit)
**File**: `video_demo_sistem.mp4`

**Storyboard**:

```
00:00-00:30 | INTRO
├── Logo CUR-HEART + title
├── Voice-over: "Sistem Informasi CUR-HEART..."
└── Background music (soft, professional)

00:30-01:30 | LANDING PAGE & PUBLIC FEATURES
├── Show landing page (hero section, services, testimonials)
├── Browse services (grid view)
├── View therapist list (with ratings)
├── Blog section (articles)
└── Contact form

01:30-03:00 | CLIENT FLOW (BOOKING)
├── Register account (quick signup)
├── Login to system
├── Browse services (select "Stress Management")
├── Choose therapist (view profile, schedule)
├── Select date & time (calendar picker)
├── Booking confirmation (summary)
├── Payment (Midtrans integration demo)
├── Payment success → Email notification
└── View appointment in dashboard

03:00-04:30 | THERAPIST FLOW
├── Login as therapist
├── View dashboard (statistics, today schedule)
├── View upcoming appointments
├── Start session (click "Start Session" button)
├── Input session notes (SOAP format)
│   • Subjective: "Klien merasa stress berat..."
│   • Objective: "Tekanan darah normal, ekspresi cemas"
│   • Assessment: "Diagnosis: Stress akut work-related"
│   • Plan: "Terapi relaksasi + CBT, 4 sesi lagi"
├── Save session notes
└── View session history

04:30-05:30 | ADMIN FLOW
├── Login as admin
├── View admin dashboard
│   • Statistics: Total users, bookings, revenue
│   • Charts: Revenue trend, booking by service
├── Manage users (CRUD demo - add new client)
├── Manage bookings (view all, filter by status)
├── Financial report (monthly revenue, therapist earnings)
└── System settings

05:30-06:30 | MOBILE RESPONSIVE & FEATURES
├── Show responsive design (mobile view)
├── Touch interactions (swipe, tap)
├── Additional features:
│   • Messaging system
│   • Rating & review
│   • Progress tracking (chart)
│   • Notification system
└── Performance (fast loading, smooth transitions)

06:30-07:00 | CLOSING
├── Recap key features
├── Call-to-action: "Visit curheart.com"
├── Team credits
└── Fade out with logo
```

**Technical Specs**:
- Resolution: 1920x1080 (Full HD)
- Frame rate: 30 fps
- Bitrate: 5-8 Mbps
- Format: MP4 (H.264 codec)
- Audio: AAC, 44.1kHz, stereo
- File size: ~50-100 MB

**Tools**:
- Screen recording: OBS Studio (free)
- Video editing: DaVinci Resolve / Adobe Premiere Pro
- Voice-over: Audacity (audio recording)
- Background music: Bensound.com (royalty-free)

---

### Video 2: Short Demo (2-3 menit)
**File**: `video_demo_short.mp4`

**Storyboard (Condensed)**:

```
00:00-00:15 | INTRO (quick)
00:15-01:00 | CLIENT BOOKING (fast-forward)
01:00-01:30 | THERAPIST SESSION (highlight SOAP notes)
01:30-02:00 | ADMIN DASHBOARD (statistics)
02:00-02:30 | KEY FEATURES (montage: payment, messaging, reports)
02:30-03:00 | CLOSING (CTA + credits)
```

**Technical Specs**: Same as full demo  
**File size**: ~30-50 MB

**Usage**:
- Slide 17 (embedded dalam presentasi)
- Social media (Instagram, YouTube)
- Quick pitch (elevator pitch)

---

## 📝 Script Presentasi

### Script Lengkap (20-25 menit)
**File**: `script_presentasi.docx`

**Format**:

```markdown
# SCRIPT PRESENTASI CAPSTONE PROJECT CUR-HEART

## PEMBAGIAN PERAN
- **Roki Anjas (PM)**: Slide 1-7, 15-16 (Intro, Latar Belakang, Metodologi, Kesimpulan)
- **Susanto (UI/UX)**: Slide 11 (UI/UX Design) + Demo
- **Fahruroji (Dev)**: Slide 8-10, 12-14 (Arsitektur, Database, Testing, Deployment)

---

## SLIDE 1: COVER (Roki Anjas - 30 detik)

**Script**:
"Selamat pagi/siang Bapak/Ibu dosen dan teman-teman semua. Kami dari kelompok CUR-HEART 
akan mempresentasikan hasil Capstone Project kami yang berjudul 'Sistem Informasi 
Manajemen Booking dan Layanan Terapi Hypnotherapy Berbasis Web untuk Studi Kasus CUR-HEART'.

Tim kami terdiri dari:
- Roki Anjas (11250066) sebagai Project Manager
- Susanto (11250068) sebagai UI/UX Designer
- Fahruroji (11250085) sebagai Full-stack Developer

Proyek ini merupakan integrasi dari 6 mata kuliah capstone: Manajemen Hubungan Pelanggan, 
Proses Bisnis TI, IT Governance, Proyek Sistem Informasi, Business Intelligence, dan 
Rintisan Bisnis Digital."

---

## SLIDE 2: AGENDA (Roki - 20 detik)

**Script**:
"Presentasi hari ini akan kami bagi menjadi 8 bagian: Dimulai dari latar belakang masalah, 
rumusan masalah, tujuan penelitian, metodologi yang kami gunakan, hasil dan pembahasan, 
demo sistem secara langsung, kesimpulan dan saran, serta diakhiri dengan sesi tanya jawab."

---

## SLIDE 3: LATAR BELAKANG (Roki - 2 menit)

**Script**:
"CUR-HEART adalah sebuah klinik hypnotherapy yang berlokasi di Makassar dengan 3 terapis 
profesional dan melayani lebih dari 150 klien aktif. Namun, berdasarkan hasil observasi dan 
wawancara kami, CUR-HEART menghadapi beberapa masalah operasional yang signifikan.

[Pause, tunjuk ke poin 1]
Pertama, proses booking masih manual melalui WhatsApp yang memakan waktu 15-20 menit per 
booking. Bayangkan jika ada 10 booking per hari, itu berarti 3 jam hanya untuk koordinasi jadwal.

[Tunjuk poin 2]
Kedua, tidak ada sistem tracking progress klien. Terapis kesulitan mengingat riwayat sesi 
sebelumnya, terutama untuk klien yang sudah lama.

[Tunjuk poin 3]
Ketiga, laporan keuangan dibuat manual setiap minggu dan membutuhkan 4-5 jam. Ini sangat 
tidak efisien dan rawan error.

Dari masalah-masalah ini, kami melihat urgensi untuk mengembangkan sistem informasi yang 
terintegrasi. Berdasarkan analisis ROI awal, sistem ini diproyeksikan menghasilkan return 
sebesar 210% dengan payback period hanya 5.7 bulan."

---

## SLIDE 4: PROFIL CUR-HEART (Roki - 1 menit)

**Script**:
"Mari saya perkenalkan profil CUR-HEART lebih detail. CUR-HEART menawarkan 5 layanan utama 
hypnotherapy dengan range harga Rp 350 ribu hingga Rp 600 ribu per sesi. Layanan paling 
populer adalah Stress Management dan Confidence Building.

Klinik beroperasi 6 hari seminggu dari Senin hingga Sabtu, jam 9 pagi sampai 6 sore. Ketiga 
terapis memiliki sertifikasi profesional dan pengalaman 5-10 tahun di bidang hypnotherapy.

Target market utama adalah profesional usia 25-45 tahun yang mengalami stress kerja, 
kecemasan, atau masalah kepercayaan diri."

---

## SLIDE 5: RUMUSAN MASALAH (Roki - 2 menit)

**Script**:
"Dari hasil analisis mendalam yang kami lakukan melalui wawancara dengan owner dan 2 terapis, 
observasi selama 3 sesi (total 12 jam), serta survey kepada 36 klien, kami mengidentifikasi 
7 masalah utama.

[Baca poin per poin dengan penekanan]
Satu, proses booking tidak efisien karena masih manual via WhatsApp.
Dua, tingkat no-show tinggi karena tidak ada sistem reminder otomatis.
Tiga, payment tracking manual sehingga sering terjadi kesalahan pencatatan.
Empat, tidak ada dokumentasi history sesi terapi yang terstruktur.
Lima, pembuatan laporan keuangan sangat lambat.
Enam, kesulitan mengelola jadwal 3 terapis secara bersamaan.
Tujuh, tidak ada mekanisme feedback dari klien melalui sistem rating dan review.

Dari 7 masalah ini, kami prioritaskan 3 masalah kritis yang menjadi fokus utama development: 
booking automation, payment integration, dan reporting system."

---

## SLIDE 6: TUJUAN PENELITIAN (Roki - 1.5 menit)

**Script**:
"Berdasarkan masalah-masalah tersebut, kami menetapkan tujuan penelitian sebagai berikut:

Tujuan utama kami adalah mengembangkan sistem informasi terintegrasi yang dapat mengotomasi 
proses bisnis CUR-HEART.

Secara spesifik, ada 5 tujuan yang ingin kami capai:
Pertama, mengurangi waktu booking hingga 85% dari 15-20 menit menjadi hanya 2-3 menit.
Kedua, integrasi payment gateway Midtrans untuk transaksi cashless yang aman.
Ketiga, digitalisasi session management dengan format SOAP notes standar medis.
Keempat, visualisasi progress klien dalam bentuk chart dan grafik.
Kelima, automasi laporan keuangan real-time yang dapat diakses kapan saja.

Target kami adalah menyelesaikan development dan deployment sistem dalam waktu 11 minggu, 
dan Alhamdulillah kami berhasil go-live tepat waktu pada 1 November 2024."

---

## SLIDE 7: METODOLOGI PENELITIAN (Roki - 2 menit)

**Script**:
"Untuk mencapai tujuan tersebut, kami menggunakan metodologi SDLC Waterfall dengan 6 fase: 
Inisiasi, Perencanaan, Development, Testing, Deployment, dan Handover.

Timeline proyek adalah 11 minggu dari 16 September hingga 1 November 2024.

Teknik pengumpulan data yang kami gunakan meliputi:
- Wawancara mendalam dengan 3 stakeholder kunci: owner, kepala terapis, dan admin
- Observasi langsung selama 3 sesi dengan total 12 jam untuk memahami proses bisnis aktual
- Survey online kepada 36 klien aktif CUR-HEART untuk mengetahui kebutuhan user
- Dokumentasi lengkap berupa foto, video, dan dokumen bisnis

Dari segi teknologi, kami memilih stack Laravel 10 sebagai backend framework karena mature 
dan powerful, MySQL 8 untuk database dengan normalisasi 3NF, dan Tailwind CSS untuk frontend 
yang modern dan responsive.

Tim kami terdiri dari 3 orang dengan pembagian peran yang jelas sesuai keahlian masing-masing."

[Transisi]
"Selanjutnya akan dijelaskan oleh Fahruroji mengenai arsitektur dan database sistem."

---

## SLIDE 8: ARSITEKTUR SISTEM (Fahruroji - 2 menit)

**Script**:
"Terima kasih Roki. Baik, saya akan jelaskan arsitektur sistem yang kami kembangkan.

[Tunjuk diagram]
Sistem kami menggunakan pola arsitektur MVC atau Model-View-Controller yang merupakan 
best practice dalam pengembangan aplikasi web.

Layer pertama adalah Presentation Layer, di mana user berinteraksi dengan sistem. Kami 
gunakan Blade template engine dari Laravel, dikombinasikan dengan Tailwind CSS untuk 
styling dan JavaScript vanilla untuk interaktivitas.

Layer kedua adalah Application Layer yang menangani business logic melalui Laravel Controllers, 
Middleware untuk authentication dan authorization, serta Form Requests untuk validasi input.

Layer ketiga adalah Business Logic Layer di mana semua aturan bisnis diterapkan. Di sini 
kami implementasikan Eloquent Models dan Repository pattern untuk abstraksi data access.

Layer keempat adalah Data Access Layer yang berkomunikasi langsung dengan MySQL database 
melalui Eloquent ORM dan Query Builder.

Dan terakhir, kami integrasikan dengan External Services yaitu Midtrans untuk payment gateway, 
Email Service untuk notifikasi, dan Cloud Storage untuk file management.

Arsitektur ini memastikan separation of concerns yang baik, sehingga sistem mudah di-maintain 
dan di-scale di masa depan."

---

## SLIDE 9: DATABASE DESIGN (Fahruroji - 2 menit)

**Script**:
"Untuk database design, kami merancang Entity Relationship Diagram yang terdiri dari 16 tabel 
dengan total 22 foreign key constraints dan 25 indexes untuk optimasi query.

[Tunjuk tabel-tabel penting]
Tabel-tabel utama meliputi:
- Users sebagai parent table untuk semua user role
- Clients dan Therapists sebagai child table dengan relasi one-to-one ke Users
- Services untuk menyimpan layanan hypnotherapy
- Bookings sebagai core table yang menghubungkan client, therapist, dan service
- Payments untuk tracking transaksi dengan Midtrans
- Sessions dan Session_notes untuk dokumentasi sesi terapi dengan format SOAP
- Dan tabel-tabel pendukung lainnya seperti schedules, reviews, messages, dan notifications

Database kami sudah normalized hingga Third Normal Form atau 3NF untuk menghindari redundansi 
data dan anomali. Kami juga implementasikan proper indexing di 25 kolom yang sering di-query 
untuk meningkatkan performance.

Untuk testing, kami sudah populate database dengan 150+ test records yang mewakili berbagai 
skenario real-world."

---

## SLIDE 10: FITUR UTAMA SISTEM (Fahruroji - 2 menit)

**Script**:
"Sistem kami memiliki 4 user roles dengan total 40 fitur fungsional.

Role pertama adalah Guest atau pengunjung website, yang dapat mengakses 8 fitur public seperti 
browse services, view therapist profiles, read blog articles, dan contact form.

Role kedua adalah Client dengan 15 fitur dedicated, di mana highlight-nya adalah booking wizard 
4-step yang sangat user-friendly, payment integration dengan Midtrans, progress tracking dengan 
visualisasi chart, messaging dengan terapis, dan rating & review system.

Role ketiga adalah Therapist dengan 10 fitur untuk operasional harian seperti manage schedule 
dan availability, view client list, input session notes dalam format SOAP standar medis, view 
session history, dan monitor earnings.

Role terakhir adalah Admin dengan 7 fitur untuk manajemen sistem seperti CRUD users, manage 
bookings, verify payments, generate financial reports real-time, dan configure system settings.

Semua fitur ini sudah melalui requirement gathering yang comprehensive dengan 40 functional 
requirements dan 15 non-functional requirements yang terdokumentasi lengkap."

[Transisi]
"Selanjutnya Susanto akan menjelaskan desain UI/UX sistem."

---

## SLIDE 11: USER INTERFACE DESIGN (Susanto - 3 menit)

**Script**:
"Terima kasih Fahruroji. Baik, saya akan jelaskan proses design dan hasil UI/UX sistem.

[Tunjuk grid mockup]
Di sini terlihat 6 screenshot representatif dari total 41 halaman yang kami design.

Pertama, landing page dengan design modern dan clean, menggunakan hero section yang eye-catching 
dengan call-to-action yang jelas.

Kedua, booking wizard dengan 4 langkah yang intuitif: pilih layanan, pilih terapis, pilih 
jadwal, dan konfirmasi pembayaran. Setiap step memiliki progress indicator yang clear.

Ketiga, client dashboard dengan visualisasi progress dalam bentuk chart. User dapat melihat 
riwayat sesi, upcoming appointments, dan statistik personal mereka.

Keempat, therapist session room dengan form SOAP notes yang terstruktur sesuai standar medis. 
Form ini memudahkan terapis untuk mendokumentasikan setiap sesi dengan lengkap.

Kelima, admin dashboard dengan statistik bisnis real-time: total users, bookings, revenue, 
dan berbagai chart untuk analisis trend.

Keenam, integration dengan Midtrans payment gateway yang seamless dan secure.

Untuk design system, kami gunakan color palette yang konsisten dengan Navy Blue sebagai primary 
color yang mencerminkan profesionalisme, dan Pink sebagai secondary color yang warm dan 
approachable sesuai dengan nature bisnis hypnotherapy yang caring.

Typography kami pilih Poppins untuk heading karena modern dan bold, serta Inter untuk body 
text karena excellent readability di berbagai ukuran screen.

Semua 41 halaman kami design fully responsive, dari desktop 1920px hingga mobile 375px, dengan 
touch-friendly button size minimal 44px sesuai standard usability.

Kami juga lakukan user testing dengan 5 responden dan mendapat feedback sangat positif dengan 
rata-rata satisfaction score 4.3 dari 5.0."

---

## SLIDE 12: HASIL TESTING (Fahruroji - 2.5 menit)

**Script**:
"Setelah development selesai, kami melakukan testing yang comprehensive di 3 level.

Level pertama adalah Unit Testing menggunakan PHPUnit. Kami berhasil mencapai code coverage 
80%, melebihi target kami yang 75%. Dari 120 test cases, semuanya passed 100%.

Level kedua adalah Feature Testing di mana kami test 40 fitur secara end-to-end. Semua fitur 
berfungsi sesuai requirement dengan success rate 100%.

Level ketiga dan paling penting adalah User Acceptance Testing atau UAT. Kami menyiapkan 30 
scenarios yang mewakili real-world usage, dan melakukan testing selama 3 hari bersama client 
yaitu owner dan 2 terapis CUR-HEART.

Hasil UAT sangat memuaskan: dari 30 scenarios, 28 passed (93.3% success rate). 2 scenarios 
yang failed adalah minor issues yang sudah kami fix dalam 1 hari. User satisfaction score 
mencapai 4.5 dari 5.0, jauh melebihi target kami yang 4.0.

Kami juga lakukan non-functional testing:
- Performance testing: Average load time 1.8 detik, well below target 3 detik
- Security testing: Implementasi OWASP best practices, passed vulnerability scan
- Usability testing: 5 user dapat menyelesaikan task tanpa guidance
- Compatibility testing: Tested di Chrome, Firefox, Safari, Edge - semua compatible

Semua hasil testing terdokumentasi lengkap dalam test reports yang tersedia di repository."

---

## SLIDE 13: DEPLOYMENT & GO-LIVE (Fahruroji - 2 menit)

**Script**:
"Setelah semua testing passed, kami proceed ke deployment phase.

Timeline deployment kami adalah 5 hari:
- Hari 1-2: Server setup dan konfigurasi (domain, SSL, database)
- Hari 3: Database migration ke production environment
- Hari 4: Testing di production (smoke testing, sanity testing)
- Hari 5: Training dan soft launch

Kami delivered comprehensive training materials:
- 3 dokumen user manual dengan total 90 halaman, covering client guide, therapist guide, 
  dan admin guide
- 4 dokumen technical documentation dengan total 107 halaman untuk system maintenance
- 5 video tutorial dengan total durasi 45 menit untuk various user tasks

Training dilakukan 2 hari: 1 hari untuk admin dan 1 hari untuk terapis. Response dari 
participants sangat positif.

Go-live dilakukan pada 1 November 2024, tepat sesuai timeline yang kami planning di awal. 
Dalam 24 jam pertama setelah launch, tidak ada critical issue yang muncul. Minor bugs yang 
ditemukan sudah kami address dalam warranty period.

Kami juga provide 3-month warranty dan ongoing support via email dan phone untuk memastikan 
system berjalan smooth."

---

## SLIDE 14: DAMPAK & MANFAAT (Fahruroji - 2 menit)

**Script**:
"Sekarang mari kita lihat dampak dan manfaat nyata dari sistem ini.

Dari segi efisiensi operasional, improvement-nya sangat signifikan:
[Tunjuk angka dengan emphasis]
- Booking time turun drastis 85%: dari 15-20 menit menjadi hanya 2-3 menit
- Payment processing 90% lebih cepat: dari 5-10 menit menjadi 1 menit
- Report generation 98% lebih cepat: dari 4-5 jam per minggu menjadi hanya 5 menit

Dari segi financial impact, berdasarkan cost-benefit analysis:
- Total development cost adalah Rp 135 juta
- Projected annual benefit adalah Rp 283 juta dari efficiency gain dan revenue increase
- Return on Investment mencapai 210%
- Payback period hanya 5.7 bulan

Ini adalah ROI yang excellent untuk investasi teknologi di SME.

Dari segi user satisfaction, semua stakeholder sangat puas:
- Client satisfaction meningkat dari 3.2 menjadi 4.3 dari 5.0
- Therapist satisfaction 4.5 dari 5.0 - mereka sangat appreciate SOAP notes feature
- Admin satisfaction 4.7 dari 5.0 - automated reporting sangat membantu mereka

Dan yang paling penting, CUR-HEART memproyeksikan 40% increase dalam booking volume di 6 
bulan pertama karena kemudahan akses dan improved customer experience."

[Transisi]
"Sekarang kembali ke Roki untuk kesimpulan dan saran."

---

## SLIDE 15: KESIMPULAN (Roki - 2 menit)

**Script**:
"Terima kasih Fahruroji. Baik, kami akan closing dengan kesimpulan dari penelitian ini.

Dari seluruh proses development yang kami lalui, kami dapat menarik 5 kesimpulan utama:

Kesimpulan pertama: Sistem informasi CUR-HEART berhasil dikembangkan dengan sangat baik, 
terdiri dari 41 halaman dengan 40 fitur fungsional yang semuanya berjalan sesuai requirement. 
Check.

Kesimpulan kedua: Metodologi SDLC Waterfall terbukti efektif untuk proyek ini. Kami berhasil 
complete dalam 11 minggu sesuai planning, dengan Schedule Performance Index 1.05 yang berarti 
5% ahead of schedule. Check.

Kesimpulan ketiga: Technology stack yang kami pilih - Laravel, MySQL, dan Tailwind CSS - 
terbukti solid, stable, dan cocok untuk requirement proyek. Development process smooth tanpa 
major technical blocker. Check.

Kesimpulan keempat: Testing yang kami lakukan sangat comprehensive dengan UAT success rate 
93.3% dan user satisfaction 4.5 dari 5.0. Ini membuktikan sistem meeting user expectation. Check.

Kesimpulan kelima dan terakhir: Dari segi business value, ROI 210% dengan payback period 5.7 
bulan adalah achievement yang luar biasa. Sistem ini tidak hanya memecahkan masalah teknis, 
tapi juga deliver real business value. Check.

Status akhir: Sistem production-ready dan already GO-LIVE sejak 1 November 2024."

---

## SLIDE 16: SARAN (Roki - 1.5 menit)

**Script**:
"Meskipun sistem sudah berjalan dengan baik, kami melihat beberapa area untuk improvement 
di masa depan.

Saran pertama: Integrasi video call menggunakan Zoom atau Jitsi untuk memfasilitasi online 
therapy sessions. Ini akan membuka market lebih luas tidak terbatas geografis.

Saran kedua: Development mobile app menggunakan Flutter atau React Native untuk better mobile 
experience, terutama untuk notification dan quick booking.

Saran ketiga: Implementasi AI chatbot untuk automate FAQ dan customer support. Ini akan 
mengurangi beban admin untuk pertanyaan-pertanyaan repetitif.

Saran keempat: Multi-language support, minimal Bahasa Indonesia dan English, untuk target 
market expat di Makassar.

Saran kelima: Feature export PDF untuk laporan dan invoice, memudahkan client dan admin 
untuk archiving dan printing.

Saran keenam: Integration dengan Google Calendar untuk sync jadwal terapis dengan calendar 
mereka yang existing.

Semua saran ini sudah kami dokumentasikan dalam roadmap Phase 2 yang direncanakan untuk Q1 2025."

---

## SLIDE 17: DEMO SISTEM (Susanto - 3-5 menit)

**Script**:
"Sekarang kami akan tunjukkan demo sistem secara langsung.

[Play video atau live demo]

Seperti yang terlihat di video, kami akan walkthrough main user flows:

Pertama, client flow dari landing page, register, login, browse services, select therapist, 
book appointment, payment via Midtrans, dan menerima confirmation email. Seluruh proses 
ini hanya memakan waktu 2-3 menit.

Kedua, therapist flow dari login, view dashboard dengan today's schedule, start session, 
input SOAP notes yang terstruktur, save, dan system automatically notify client.

Ketiga, admin flow dari dashboard overview dengan real-time statistics, manage users dengan 
CRUD operations, verify payments, dan generate financial report dengan one-click.

[Jika live demo]
Sekarang saya akan tunjukkan langsung... [lakukan demo interaktif]

[Jika video]
Untuk detail lebih lengkap, video full demo 7 menit tersedia di repository kami dan bisa 
diakses via QR code di slide terakhir.

Sistem juga fully responsive. [Tunjuk mobile version] Ini tampilan mobile yang equally 
functional dengan desktop."

---

## SLIDE 18: KONTRIBUSI PENELITIAN (Roki - 1.5 menit)

**Script**:
"Penelitian kami ini memberikan kontribusi baik secara akademik maupun praktis.

Kontribusi akademik meliputi:
Pertama, framework integrasi 6 mata kuliah capstone menjadi satu proyek cohesive. Ini bisa 
menjadi reference untuk mahasiswa batch selanjutnya.

Kedua, dokumentasi metodologi SDLC khusus untuk hypnotherapy system atau lebih umum untuk 
service-based booking system.

Ketiga, comprehensive case study tentang implementasi CRM dan Booking system di SME healthcare.

Dari segi kontribusi praktis:
Pertama, real system yang deployed dan production-ready, bukan hanya prototype atau proof 
of concept.

Kedua, detailed ROI analysis untuk digitalization di SME yang bisa jadi reference untuk 
business serupa.

Ketiga, template sistem booking yang bisa di-adapt untuk service-based business lainnya 
seperti salon, barbershop, konsultasi, dll.

Kami juga targeting untuk publikasi hasil penelitian ini di jurnal nasional terakreditasi 
Sinta 2 hingga 4 sebagai scientific contribution."

---

## SLIDE 19: Q&A (All - 5-10 menit)

**Script (Roki)**:
"Baik, kami sudah sampai di akhir presentasi. Sebelum sesi tanya jawab, ini contact information 
kami jika Bapak/Ibu ingin follow up:

[Tunjuk contact info]
Email CUR-HEART, website, GitHub repository, dan email masing-masing anggota tim.

[Tunjuk QR code]
Untuk akses demo sistem secara langsung, Bapak/Ibu bisa scan QR code ini.

Sekarang kami open floor untuk pertanyaan. Silakan."

[Tips menjawab pertanyaan]
- Listen carefully ke pertanyaan
- Clarify jika pertanyaan tidak jelas
- Answer confidently dengan refer ke evidence (test result, metrics, dll)
- Jika tidak tahu, jujur dan tawarkan untuk follow up
- Keep answer concise (1-2 menit max per pertanyaan)

**Common Questions & Suggested Answers**:

**Q1: "Kenapa pilih Laravel dibanding framework lain seperti Django atau Node.js?"**
**A1 (Fahruroji)**: "Pilihan Laravel based on beberapa pertimbangan: Pertama, team expertise - 
kami lebih familiar dengan PHP ecosystem. Kedua, Laravel punya built-in features yang lengkap 
untuk authentication, ORM, routing yang mempercepat development. Ketiga, large community dan 
dokumentasi excellent memudahkan troubleshooting. Keempat, mature dan production-proven untuk 
aplikasi enterprise. Dibanding Django, PHP hosting lebih accessible dan affordable di Indonesia. 
Dibanding Node.js, Laravel lebih opinionated sehingga faster untuk development terstruktur."

**Q2: "Bagaimana handle security terutama untuk payment dan data medis?"**
**A2 (Fahruroji)**: "Security adalah prioritas utama. Pertama, semua connection menggunakan 
SSL/TLS encryption. Kedua, payment dilakukan via Midtrans yang PCI-DSS compliant, kami tidak 
store sensitive card data. Ketiga, session notes dan medical data di-encrypt at rest di database. 
Keempat, implement OWASP Top 10 best practices: input validation, SQL injection prevention via 
prepared statements, XSS protection, CSRF tokens. Kelima, role-based access control strict - 
therapist hanya bisa access client mereka sendiri. Keenam, all actions logged untuk audit trail. 
Kami sudah lakukan vulnerability scan dan passed."

**Q3: "Berapa lama maintenance-nya dan apakah sustainable?"**
**A3 (Roki)**: "Untuk post-launch maintenance, kami provide 3-month warranty untuk bug fixing. 
Untuk sustainability, sistem ini sangat maintainable karena: Pertama, kode terorganisir baik 
mengikuti Laravel best practices. Kedua, dokumentasi technical lengkap 107 halaman. Ketiga, 
test coverage 80% memastikan regression tidak terjadi saat update. Keempat, Laravel adalah LTS 
version dengan support hingga 2026. Untuk long-term, kami sudah train internal team CUR-HEART 
untuk basic maintenance, dan kami ready untuk support contract jika diperlukan. Estimated 
maintenance cost hanya sekitar 5-10% dari development cost per tahun."

**Q4: "Apakah sudah consider scalability jika user growth significant?"**
**A4 (Fahruroji)**: "Yes, scalability adalah consideration dari awal. Arsitektur kami support 
horizontal scaling - bisa add more servers behind load balancer. Database sudah properly indexed 
untuk performance. Kami gunakan caching layer (Redis) untuk reduce database load. File storage 
bisa migrate ke cloud storage seperti S3 jika needed. Current infrastructure bisa handle sampai 
1000 concurrent users. Dari business projection CUR-HEART, growth akan bertahap jadi infrastructure 
bisa di-scale incrementally. Kami juga implement monitoring tools untuk track performance metrics 
dan alert jika ada bottleneck."

**Q5: "Apa lessons learned dari proyek ini?"**
**A5 (Roki)**: "Lessons learned yang valuable: Pertama, requirement gathering tidak boleh di-rush. 
Kami spend 2 minggu full untuk ini dan it paid off karena minimal change request during development. 
Kedua, automated testing adalah must - saved us banyak waktu during bug fixing. Ketiga, communication 
dengan client harus frequent - kami weekly demo progress untuk avoid surprise. Keempat, documentation 
harus dibuat concurrent dengan development, jangan di akhir. Kelima, UI/UX testing dengan real user 
early on mencegah major redesign. Keenam, risk management planning sangat help - kami anticipate 
potential issues dan punya mitigation ready."

---

## SLIDE 20: THANK YOU (All - 15 detik)

**Script (Roki)**:
"Baik, sekian presentasi dari kami. Terima kasih banyak atas perhatian Bapak/Ibu dosen dan 
teman-teman. Kami sangat berterima kasih atas bimbingan selama proses capstone ini.

[Bow/gesture of respect]

Semoga hasil kerja kami bisa bermanfaat dan menjadi referensi untuk project-project selanjutnya.

Terima kasih."

[All team members stand and bow together]

---

**END OF SCRIPT**
```

**Word Count**: ~6,500 words  
**Presentation Duration**: 20-25 minutes (without Q&A), 30-35 minutes (with Q&A)

---

## 🎤 Tips Presentasi

### Persiapan (3 hari sebelum):
- [ ] Rehearsal 3x (individual + team)
- [ ] Time each section (pastikan tidak over/under time)
- [ ] Prepare backup laptop & USB
- [ ] Test video & audio di venue (jika memungkinkan)
- [ ] Print handout (optional, 1 page summary)
- [ ] Prepare demo account (username/password ready)
- [ ] Backup internet (hotspot ready jika WiFi fail)

### Hari H:
- [ ] Datang 30 menit lebih awal
- [ ] Setup & test peralatan
- [ ] Dress code: Professional (kemeja/blazer)
- [ ] Bawa air minum
- [ ] Deep breath before start

### During Presentation:
✅ **Do's**:
- Speak clearly & confidently
- Make eye contact with audience
- Use hand gestures (natural, not excessive)
- Refer to slides but don't read verbatim
- Engage audience dengan pertanyaan rhetoric
- Smile & show enthusiasm
- Handle transitions smoothly antar presenter
- Keep time (use timer/watch)

❌ **Don'ts**:
- Jangan baca slide word-by-word
- Jangan terlalu cepat bicara
- Jangan monotone (vary your tone)
- Jangan berdiri membelakangi audience
- Jangan panik jika ada technical issue (stay calm)
- Jangan defensive saat menjawab pertanyaan
- Jangan gunakan filler words berlebihan ("eee", "anu", "hmm")

### Q&A Tips:
- Listen carefully to question (repeat if necessary)
- Pause 2-3 detik sebelum jawab (think first)
- Answer with confidence (refer to data/evidence)
- If tidak tahu: "Terima kasih pertanyaannya, kami belum explore area itu secara mendalam, tapi kami bisa follow up setelah presentasi"
- Keep answer concise (1-2 menit max)
- Thank the questioner

---

## 🛠️ Tools untuk Membuat Presentasi

### Slide Design:
- **Microsoft PowerPoint** (recommended) - Industry standard
- **Google Slides** (online, collaborative)
- **Canva** (template-based, easy)
- **Prezi** (non-linear, creative)
- **Apple Keynote** (Mac users, beautiful animations)

### Video Demo Creation:
- **OBS Studio** (free, screen recording)
- **Camtasia** (paid, professional)
- **Loom** (free, quick recording)
- **ScreenFlow** (Mac, advanced editing)

### Video Editing:
- **DaVinci Resolve** (free, professional)
- **Adobe Premiere Pro** (paid, industry standard)
- **Final Cut Pro** (Mac, professional)
- **iMovie** (Mac, basic editing)
- **Shotcut** (free, cross-platform)

### Voice Over:
- **Audacity** (free, audio recording & editing)
- **Adobe Audition** (paid, professional)
- **GarageBand** (Mac, music & podcast)

### Background Music (Royalty-Free):
- Bensound.com
- YouTube Audio Library
- Incompetech.com
- Artlist.io (paid, premium)

---

## ✅ Checklist Pre-Presentation

### 1 Week Before:
- [ ] Slide content complete
- [ ] Video demo recorded & edited
- [ ] Script written & reviewed
- [ ] First rehearsal (individual)

### 3 Days Before:
- [ ] Slide design polished
- [ ] Video demo final version
- [ ] Script memorized (key points)
- [ ] Team rehearsal 1

### 1 Day Before:
- [ ] All files ready (PPTX, PDF, MP4 backup)
- [ ] Demo account tested
- [ ] Team rehearsal 2 (full run)
- [ ] Print backup materials (optional)

### Day of Presentation:
- [ ] Laptop fully charged
- [ ] Backup USB with all files
- [ ] Demo account credentials written down
- [ ] Hotspot internet ready
- [ ] Arrive 30 min early
- [ ] Setup & test equipment
- [ ] Final check with team
- [ ] **READY TO PRESENT!** 🎉

---

**Last Updated**: 1 November 2024  
**Status**: Ready for final presentation  
**Estimated Duration**: 20-25 minutes (presentation) + 10 minutes (Q&A)  
**Prepared by**: Tim Proyek CUR-HEART
