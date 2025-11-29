# BAB IV
# ANALISA DAN PERANCANGAN APLIKASI START-UP

## 4.1. Analisa Kebutuhan

Analisa kebutuhan dilakukan untuk mengidentifikasi kebutuhan fungsional dan non-fungsional sistem informasi CUR-HEART berdasarkan hasil riset pengguna dan analisis proses bisnis.

### 4.1.1. Analisis Kebutuhan Aplikasi

Berdasarkan hasil wawancara, observasi, dan survei yang telah dilakukan, teridentifikasi kebutuhan aplikasi sebagai berikut:

**A. Kebutuhan Fungsional**

Kebutuhan fungsional adalah fungsi-fungsi yang harus ada dalam sistem untuk mendukung proses bisnis.

**Untuk Tamu (Guest)**:
1. Sistem harus dapat menampilkan halaman beranda dengan informasi bisnis
2. Sistem harus dapat menampilkan katalog layanan terapi lengkap dengan deskripsi dan harga
3. Sistem harus dapat menampilkan direktori terapis dengan profil, spesialisasi, dan rating
4. Sistem harus dapat menampilkan artikel blog tentang kesehatan mental
5. Sistem harus dapat menampilkan FAQ (Frequently Asked Questions)
6. Sistem harus menyediakan formulir kontak untuk inquiry
7. Sistem harus menyediakan fitur registrasi akun baru (klien atau terapis)
8. Sistem harus menyediakan fitur login untuk pengguna terdaftar

**Untuk Klien**:
1. Sistem harus dapat menampilkan dashboard klien dengan ringkasan informasi
2. Sistem harus memungkinkan klien melakukan reservasi layanan terapi online
3. Sistem harus menampilkan jadwal ketersediaan terapis secara real-time
4. Sistem harus memungkinkan klien memilih terapis berdasarkan spesialisasi dan rating
5. Sistem harus memungkinkan klien memilih tanggal dan waktu sesi terapi
6. Sistem harus terintegrasi dengan payment gateway untuk pembayaran online
7. Sistem harus mengirim email konfirmasi setelah reservasi berhasil
8. Sistem harus mengirim email reminder H-1 dan H-0 sebelum sesi
9. Sistem harus menampilkan riwayat reservasi dan sesi terapi klien
10. Sistem harus menampilkan progress tracking dengan grafik visual
11. Sistem harus memungkinkan klien menjadwal ulang atau membatalkan reservasi (dengan syarat)
12. Sistem harus memungkinkan klien memberikan rating dan review setelah sesi
13. Sistem harus memungkinkan klien mengakses catatan sesi yang dibagikan terapis
14. Sistem harus memungkinkan klien memperbarui profil dan pengaturan akun
15. Sistem harus menampilkan notifikasi untuk klien

**Untuk Terapis**:
1. Sistem harus dapat menampilkan dashboard terapis dengan ringkasan informasi
2. Sistem harus menampilkan jadwal sesi terapi hari ini dan minggu ini
3. Sistem harus menampilkan daftar klien dengan detail reservasi
4. Sistem harus memungkinkan terapis mengatur ketersediaan jadwal
5. Sistem harus memungkinkan terapis memblokir waktu untuk cuti atau keperluan pribadi
6. Sistem harus memungkinkan terapis mendokumentasikan sesi terapi dengan formulir terstruktur
7. Sistem harus menyediakan template untuk dokumentasi sesi
8. Sistem harus memungkinkan terapis mengakses riwayat lengkap klien
9. Sistem harus menampilkan timeline progress klien
10. Sistem harus memungkinkan terapis memperbarui status sesi (completed, cancelled, no-show)
11. Sistem harus menampilkan dashboard pendapatan terapis
12. Sistem harus memungkinkan terapis melakukan withdrawal pendapatan
13. Sistem harus memungkinkan terapis memperbarui profil dan pengaturan
14. Sistem harus menampilkan notifikasi untuk terapis
15. Sistem harus memungkinkan terapis melihat rating dan review dari klien

**Untuk Admin**:
1. Sistem harus dapat menampilkan dashboard admin dengan metrik kunci
2. Sistem harus menampilkan grafik pendapatan, pertumbuhan pengguna, dan layanan terpopuler
3. Sistem harus memungkinkan admin mengelola data pengguna (CRUD)
4. Sistem harus memungkinkan admin menyetujui atau menolak pendaftaran terapis baru
5. Sistem harus memungkinkan admin mengelola data layanan terapi (CRUD)
6. Sistem harus memungkinkan admin mengelola data reservasi
7. Sistem harus memungkinkan admin memverifikasi pembayaran manual (jika ada)
8. Sistem harus memungkinkan admin mengelola permintaan withdrawal terapis
9. Sistem harus memungkinkan admin membuat laporan (reservasi, keuangan, kinerja)
10. Sistem harus memungkinkan admin mengekspor laporan ke Excel/PDF
11. Sistem harus memungkinkan admin mengelola konten blog (CRUD)
12. Sistem harus memungkinkan admin mengelola konten FAQ (CRUD)
13. Sistem harus memungkinkan admin mengelola kode promo (CRUD)
14. Sistem harus memungkinkan admin melihat dan moderasi ulasan klien
15. Sistem harus memungkinkan admin melihat log aktivitas pengguna (audit trail)
16. Sistem harus memungkinkan admin mengatur konfigurasi sistem
17. Sistem harus menampilkan notifikasi untuk admin

**Untuk Sistem (Automated)**:
1. Sistem harus secara otomatis mendeteksi konflik jadwal saat reservasi
2. Sistem harus secara otomatis mengirim email konfirmasi setelah reservasi
3. Sistem harus secara otomatis mengirim email reminder H-1 dan H-0
4. Sistem harus secara otomatis memperbarui status pembayaran setelah verifikasi dari payment gateway
5. Sistem harus secara otomatis menghitung pendapatan terapis (80% dari fee sesi)
6. Sistem harus secara otomatis membuat notifikasi untuk pengguna terkait
7. Sistem harus secara otomatis melakukan backup database harian
8. Sistem harus secara otomatis mencatat semua aktivitas penting ke audit log

**B. Kebutuhan Non-Fungsional**

Kebutuhan non-fungsional adalah karakteristik sistem yang tidak terkait langsung dengan fungsi, tetapi penting untuk kualitas sistem.

**1. Performance (Kinerja)**:
- Waktu muat halaman rata-rata < 2 detik
- Waktu respons API < 500ms untuk 95% permintaan
- Waktu kueri database < 100ms (rata-rata)
- Sistem harus dapat menangani minimal 100 pengguna bersamaan
- Sistem harus dapat menangani minimal 500 transaksi per hari

**2. Security (Keamanan)**:
- Sistem harus mengenkripsi semua data sensitif (password, data kesehatan)
- Sistem harus menggunakan HTTPS untuk semua komunikasi
- Sistem harus mencegah SQL injection menggunakan prepared statements/ORM
- Sistem harus mencegah XSS (Cross-Site Scripting) dengan input sanitization
- Sistem harus mencegah CSRF (Cross-Site Request Forgery) dengan token
- Sistem harus mengimplementasikan role-based access control (RBAC)
- Sistem harus comply dengan UU Perlindungan Data Pribadi (UU PDP)
- Sistem harus melakukan hashing password dengan bcrypt (cost factor 12)
- Sistem harus mengimplementasikan rate limiting untuk mencegah brute force attack
- Sistem harus melakukan audit logging untuk semua aktivitas penting

**3. Usability (Kegunaan)**:
- Sistem harus memiliki antarmuka yang intuitif dan mudah dipahami
- Sistem harus memiliki System Usability Scale (SUS) score minimal 70/100
- Sistem harus memiliki tingkat penyelesaian tugas (task completion rate) ≥ 90%
- Sistem harus menyediakan pesan error yang jelas dan actionable
- Sistem harus menyediakan help text dan tooltip untuk fitur yang kompleks
- Sistem harus accessible (WCAG 2.1 Level AA compliance)
- Sistem harus memiliki rasio kontras warna minimal 4.5:1
- Sistem harus dapat digunakan dengan keyboard navigation

**4. Reliability (Keandalan)**:
- Sistem harus memiliki uptime minimal 99% (maksimal downtime 7,2 jam/bulan)
- Sistem harus memiliki Mean Time Between Failures (MTBF) > 720 jam
- Sistem harus memiliki Recovery Time Objective (RTO) < 4 jam
- Sistem harus memiliki Recovery Point Objective (RPO) < 24 jam
- Sistem harus melakukan automated backup harian dengan retensi 30 hari
- Sistem harus memiliki disaster recovery plan

**5. Scalability (Skalabilitas)**:
- Sistem harus dapat di-scale secara horizontal (menambah server)
- Sistem harus dapat menangani pertumbuhan data hingga 10x tanpa degradasi performa
- Database harus dapat di-scale dengan replication (master-slave)
- Sistem harus menggunakan caching untuk mengurangi load database
- Sistem harus menggunakan queue untuk background jobs

**6. Maintainability (Kemudahan Pemeliharaan)**:
- Kode harus mengikuti coding standards (PSR-12 untuk PHP)
- Kode harus memiliki test coverage minimal 70%
- Kode harus memiliki inline comments untuk logika yang kompleks
- Sistem harus memiliki dokumentasi API yang lengkap
- Sistem harus memiliki dokumentasi deployment dan configuration
- Sistem harus menggunakan version control (Git)
- Sistem harus menggunakan semantic versioning

**7. Portability (Portabilitas)**:
- Sistem harus dapat berjalan di berbagai environment (development, staging, production)
- Sistem harus dapat berjalan di berbagai OS (Linux, Windows, macOS)
- Sistem harus menggunakan containerization (Docker) untuk consistency
- Sistem harus memiliki environment configuration yang terpisah

**8. Compatibility (Kompatibilitas)**:
- Sistem harus kompatibel dengan browser modern (Chrome, Firefox, Safari, Edge)
- Sistem harus kompatibel dengan browser versi 2 tahun terakhir
- Sistem harus responsive dan dapat diakses dari desktop, tablet, dan mobile
- Sistem harus kompatibel dengan screen reader untuk accessibility

**9. Localization (Lokalisasi)**:
- Sistem harus menggunakan Bahasa Indonesia sebagai bahasa utama
- Sistem harus menggunakan format tanggal Indonesia (DD/MM/YYYY)
- Sistem harus menggunakan format mata uang Rupiah (Rp)
- Sistem harus menggunakan timezone WIB (UTC+7)

**10. Legal & Compliance**:
- Sistem harus comply dengan UU Perlindungan Data Pribadi (UU PDP)
- Sistem harus memiliki Terms of Service dan Privacy Policy
- Sistem harus memiliki consent mechanism untuk data collection
- Sistem harus memiliki data retention policy
- Sistem harus memiliki data deletion mechanism (right to be forgotten)

**C. Prioritas Kebutuhan (MoSCoW Method)**

**Must Have (MVP - Phase 1)**:
- Sistem reservasi online dengan wizard 4 langkah
- Manajemen jadwal terapis dengan deteksi konflik
- Integrasi payment gateway (Midtrans)
- Dashboard untuk klien, terapis, dan admin
- Dokumentasi sesi terapi digital
- Sistem notifikasi email otomatis
- Autentikasi dan otorisasi multi-role
- Security features (encryption, HTTPS, CSRF protection)

**Should Have (Phase 2)**:
- Mobile app (iOS & Android)
- Video conference untuk terapi online
- Chatbot untuk FAQ
- Advanced analytics dan reporting
- Loyalty program dan referral system
- SMS notification

**Could Have (Phase 3)**:
- AI recommendation untuk terapis
- Gamification untuk engagement
- Community forum
- Integration dengan wearable devices
- Multi-language support

**Won't Have (Out of Scope)**:
- Diagnosis medis otomatis
- Prescription management
- Insurance integration (tahap awal)
- Multi-currency support


### 4.1.2. Rancangan Diagram Use Case

Use Case Diagram menggambarkan interaksi antara aktor (pengguna) dengan sistem, serta fungsionalitas yang dapat dilakukan oleh masing-masing aktor dalam sistem informasi CUR-HEART.

**Aktor dalam Sistem**:

1. **Guest (Tamu)** - Pengunjung website yang belum login
2. **Client (Klien)** - Pengguna terdaftar yang menggunakan layanan terapi
3. **Therapist (Terapis)** - Praktisi hipnoterapi yang memberikan layanan
4. **Admin (Administrator)** - Pengelola sistem
5. **Payment Gateway** - Sistem eksternal untuk pemrosesan pembayaran (Midtrans)

**Use Case Diagram Sistem CUR-HEART**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SISTEM INFORMASI CUR-HEART                               │
│                                                                             │
│  ┌──────────┐                                                               │
│  │  Guest   │                                                               │
│  └────┬─────┘                                                               │
│       │                                                                     │
│       ├──────────> View Homepage                                           │
│       ├──────────> View Services                                           │
│       ├──────────> View Therapists                                         │
│       ├──────────> View Blog                                               │
│       ├──────────> View FAQ                                                │
│       ├──────────> Contact Us                                              │
│       ├──────────> Register                                                │
│       └──────────> Login                                                   │
│                                                                             │
│  ┌──────────┐                                                               │
│  │  Client  │                                                               │
│  └────┬─────┘                                                               │
│       │                                                                     │
│       ├──────────> View Dashboard                                          │
│       ├──────────> Make Booking ──────> Select Service                     │
│       │                          └────> Select Therapist                   │
│       │                          └────> Select Schedule                    │
│       │                          └────> Make Payment ──> [Payment Gateway] │
│       ├──────────> View Booking History                                    │
│       ├──────────> View Session History                                    │
│       ├──────────> View Progress Tracking                                  │
│       ├──────────> Reschedule Booking                                      │
│       ├──────────> Cancel Booking                                          │
│       ├──────────> Give Review & Rating                                    │
│       ├──────────> View Session Notes (shared)                             │
│       ├──────────> Update Profile                                          │
│       ├──────────> View Notifications                                      │
│       └──────────> Logout                                                  │
│                                                                             │
│  ┌──────────┐                                                               │
│  │ Therapist│                                                               │
│  └────┬─────┘                                                               │
│       │                                                                     │
│       ├──────────> View Dashboard                                          │
│       ├──────────> View Today's Schedule                                   │
│       ├──────────> View Client List                                        │
│       ├──────────> View Client Details                                     │
│       ├──────────> View Client History                                     │
│       ├──────────> Manage Availability                                     │
│       ├──────────> Block Time (Leave/Holiday)                              │
│       ├──────────> Document Session ──────> Use Template                   │
│       │                              └────> Save Notes                     │
│       │                              └────> Update Session Status          │
│       ├──────────> View Session History                                    │
│       ├──────────> View Earnings Dashboard                                 │
│       ├──────────> Request Withdrawal                                      │
│       ├──────────> View Reviews & Ratings                                  │
│       ├──────────> Update Profile                                          │
│       ├──────────> View Notifications                                      │
│       └──────────> Logout                                                  │
│                                                                             │
│  ┌──────────┐                                                               │
│  │  Admin   │                                                               │
│  └────┬─────┘                                                               │
│       │                                                                     │
│       ├──────────> View Dashboard                                          │
│       ├──────────> Manage Users ──────────> CRUD Clients                   │
│       │                          └────────> CRUD Therapists                │
│       │                          └────────> CRUD Admins                    │
│       │                          └────────> Approve Therapist              │
│       ├──────────> Manage Services ────────> CRUD Services                 │
│       ├──────────> Manage Bookings ────────> View All Bookings             │
│       │                            └──────> Edit Booking                   │
│       │                            └──────> Cancel Booking                 │
│       │                            └──────> Verify Payment (manual)        │
│       ├──────────> Manage Withdrawals ─────> View Requests                 │
│       │                              └────> Approve/Reject                 │
│       │                              └────> Process Payment                │
│       ├──────────> Manage Content ─────────> CRUD Blog Posts               │
│       │                            └──────> CRUD FAQ                       │
│       │                            └──────> CRUD Promo Codes               │
│       ├──────────> Manage Reviews ─────────> View All Reviews              │
│       │                            └──────> Moderate Reviews               │
│       ├──────────> Generate Reports ───────> Booking Report                │
│       │                             └─────> Financial Report               │
│       │                             └─────> Performance Report             │
│       │                             └─────> Export to Excel/PDF            │
│       ├──────────> View Activity Logs                                      │
│       ├──────────> System Settings                                         │
│       ├──────────> View Notifications                                      │
│       └──────────> Logout                                                  │
│                                                                             │
│  ┌──────────────┐                                                           │
│  │Payment Gateway│                                                          │
│  └────┬─────────┘                                                           │
│       │                                                                     │
│       ├──────────> Process Payment                                         │
│       ├──────────> Send Payment Notification                               │
│       └──────────> Verify Transaction                                      │
│                                                                             │
│  [System Automated]                                                         │
│       │                                                                     │
│       ├──────────> Detect Schedule Conflict                                │
│       ├──────────> Send Email Confirmation                                 │
│       ├──────────> Send Email Reminder (H-1, H-0)                          │
│       ├──────────> Update Payment Status                                   │
│       ├──────────> Calculate Therapist Earnings                            │
│       ├──────────> Create Notifications                                    │
│       ├──────────> Backup Database (Daily)                                 │
│       └──────────> Log Activities (Audit Trail)                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Gambar 4.1 Use Case Diagram Sistem Informasi CUR-HEART**

**Penjelasan Use Case Utama**:

**1. Make Booking (Klien)**
- **Aktor**: Client
- **Deskripsi**: Klien melakukan reservasi layanan terapi melalui wizard 4 langkah
- **Precondition**: Klien sudah login
- **Flow**:
  1. Klien memilih layanan terapi
  2. Klien memilih terapis (atau auto-assign)
  3. Klien memilih tanggal dan waktu
  4. Klien melakukan pembayaran via Midtrans
  5. Sistem mengirim konfirmasi email
- **Postcondition**: Booking berhasil dibuat dengan status "Paid"

**2. Document Session (Terapis)**
- **Aktor**: Therapist
- **Deskripsi**: Terapis mendokumentasikan sesi terapi yang sudah dilaksanakan
- **Precondition**: Terapis sudah login, sesi sudah dilaksanakan
- **Flow**:
  1. Terapis memilih sesi dari jadwal
  2. Terapis mengisi formulir dokumentasi (teknik, observasi, progress, rekomendasi)
  3. Terapis menyimpan dokumentasi
  4. Sistem update status sesi menjadi "Completed"
- **Postcondition**: Dokumentasi tersimpan dan dapat diakses untuk sesi berikutnya

**3. Generate Reports (Admin)**
- **Aktor**: Admin
- **Deskripsi**: Admin membuat laporan untuk monitoring dan decision making
- **Precondition**: Admin sudah login
- **Flow**:
  1. Admin memilih jenis laporan (booking, financial, performance)
  2. Admin memilih periode dan filter
  3. Sistem generate laporan dengan grafik dan tabel
  4. Admin dapat view, export (Excel/PDF), atau print
- **Postcondition**: Laporan berhasil dibuat dan dapat diakses

### 4.1.3. Rancangan Diagram Aktivitas

Activity Diagram menggambarkan alur aktivitas dalam sistem untuk berbagai proses bisnis. Berikut adalah 3 activity diagram utama sesuai dengan proses bisnis CUR-HEART:

#### A. Activity Diagram: Proses Reservasi Terapi oleh Klien

```
┌─────────────────────────────────────────────────────────────────────────────┐
│           ACTIVITY DIAGRAM: PROSES RESERVASI TERAPI OLEH KLIEN             │
└─────────────────────────────────────────────────────────────────────────────┘

    KLIEN                    SISTEM                    PAYMENT GATEWAY
      │                        │                              │
      │ Login                  │                              │
      ├───────────────────────>│                              │
      │                        │ Verify credentials           │
      │                        ├──────────┐                   │
      │                        │          │                   │
      │                        │<─────────┘                   │
      │ Login success          │                              │
      │<───────────────────────┤                              │
      │                        │                              │
      │ Pilih layanan terapi   │                              │
      ├───────────────────────>│                              │
      │                        │ Tampilkan daftar layanan     │
      │<───────────────────────┤                              │
      │                        │                              │
      │ Pilih terapis          │                              │
      ├───────────────────────>│                              │
      │                        │ Tampilkan daftar terapis     │
      │                        │ dengan jadwal tersedia       │
      │<───────────────────────┤                              │
      │                        │                              │
      │ Pilih tanggal & waktu  │                              │
      ├───────────────────────>│                              │
      │                        │ Cek ketersediaan jadwal      │
      │                        ├──────────┐                   │
      │                        │          │                   │
      │                        │<─────────┘                   │
      │                        │                              │
      │                        │ [Jadwal tidak tersedia]      │
      │                        ├──────────┐                   │
      │ Jadwal tidak tersedia  │          │                   │
      │<───────────────────────┤          │                   │
      │ (kembali pilih jadwal) │          │                   │
      │                        │          │                   │
      │                        │ [Jadwal tersedia]            │
      │                        │<─────────┘                   │
      │                        │                              │
      │ Isi informasi tambahan │                              │
      │ (keluhan, catatan)     │                              │
      ├───────────────────────>│                              │
      │                        │ Tampilkan ringkasan          │
      │                        │ reservasi & total biaya      │
      │<───────────────────────┤                              │
      │                        │                              │
      │ Konfirmasi reservasi   │                              │
      ├───────────────────────>│                              │
      │                        │ Buat booking (status:        │
      │                        │ "Pending Payment")           │
      │                        ├──────────┐                   │
      │                        │          │                   │
      │                        │<─────────┘                   │
      │                        │ Redirect ke payment gateway  │
      │                        ├─────────────────────────────>│
      │                        │                              │
      │ Lakukan pembayaran     │                              │
      ├──────────────────────────────────────────────────────>│
      │                        │                              │ Proses transaksi
      │                        │                              ├──────────┐
      │                        │                              │          │
      │                        │                              │<─────────┘
      │                        │                              │
      │                        │                              │ [Pembayaran gagal]
      │                        │ Payment failed notification  │
      │                        │<─────────────────────────────┤
      │                        │ Update status: "Payment      │
      │                        │ Failed"                      │
      │                        ├──────────┐                   │
      │                        │          │                   │
      │                        │<─────────┘                   │
      │ Pembayaran gagal       │                              │
      │<───────────────────────┤                              │
      │ (coba lagi)            │                              │
      │                        │                              │
      │                        │                              │ [Pembayaran berhasil]
      │                        │ Payment success notification │
      │                        │<─────────────────────────────┤
      │                        │ Update status: "Paid"        │
      │                        ├──────────┐                   │
      │                        │          │                   │
      │                        │<─────────┘                   │
      │                        │ Kirim email konfirmasi       │
      │                        │ ke klien                     │
      │ Email konfirmasi       ├──────────┐                   │
      │<───────────────────────┤          │                   │
      │                        │<─────────┘                   │
      │                        │ Kirim notifikasi ke terapis  │
      │                        ├──────────┐                   │
      │                        │          │                   │
      │                        │<─────────┘                   │
      │                        │ Schedule email reminder      │
      │                        │ (H-1 dan H-0)                │
      │                        ├──────────┐                   │
      │                        │          │                   │
      │                        │<─────────┘                   │
      │ Reservasi berhasil     │                              │
      │<───────────────────────┤                              │
      │                        │                              │
      ▼                        ▼                              ▼
    [END]                   [END]                          [END]
```

**Gambar 4.2 Activity Diagram Proses Reservasi Terapi oleh Klien**

**Penjelasan Alur**:
1. Klien login ke sistem dengan credentials
2. Sistem verifikasi dan memberikan akses
3. Klien memilih layanan terapi yang diinginkan
4. Klien memilih terapis berdasarkan spesialisasi dan jadwal
5. Klien memilih tanggal dan waktu sesi
6. Sistem mengecek ketersediaan jadwal (jika tidak tersedia, kembali ke step 5)
7. Klien mengisi informasi tambahan (keluhan, catatan)
8. Sistem menampilkan ringkasan reservasi dan total biaya
9. Klien konfirmasi reservasi
10. Sistem membuat booking dengan status "Pending Payment"
11. Sistem redirect ke payment gateway (Midtrans)
12. Klien melakukan pembayaran
13. Payment gateway memproses transaksi
14. Jika gagal: Update status "Payment Failed", klien dapat coba lagi
15. Jika berhasil: Update status "Paid", kirim email konfirmasi, notifikasi terapis, schedule reminder
16. Reservasi berhasil dibuat

#### B. Activity Diagram: Dokumentasi Sesi Terapi oleh Terapis

```
┌─────────────────────────────────────────────────────────────────────────────┐
│        ACTIVITY DIAGRAM: DOKUMENTASI SESI TERAPI OLEH TERAPIS              │
└─────────────────────────────────────────────────────────────────────────────┘

    TERAPIS                  SISTEM
      │                        │
      │ Login                  │
      ├───────────────────────>│
      │                        │ Verify credentials
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │ Login success          │
      │<───────────────────────┤
      │                        │
      │ Lihat jadwal hari ini  │
      ├───────────────────────>│
      │                        │ Tampilkan daftar sesi
      │                        │ hari ini
      │<───────────────────────┤
      │                        │
      │ Pilih sesi yang sudah  │
      │ dilaksanakan           │
      ├───────────────────────>│
      │                        │ Tampilkan detail sesi
      │                        │ dan klien
      │<───────────────────────┤
      │                        │
      │ Klik "Document Session"│
      ├───────────────────────>│
      │                        │ Tampilkan formulir
      │                        │ dokumentasi dengan
      │                        │ template
      │<───────────────────────┤
      │                        │
      │ Isi dokumentasi:       │
      │ - Teknik yang digunakan│
      │ - Observasi kondisi    │
      │ - Kemajuan yang dicapai│
      │ - Catatan penting      │
      │ - Rekomendasi          │
      ├───────────────────────>│
      │                        │ Auto-save (setiap 30 detik)
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │
      │ Klik "Save"            │
      ├───────────────────────>│
      │                        │ Validasi data
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │
      │                        │ [Data tidak valid]
      │                        ├──────────┐
      │ Error message          │          │
      │<───────────────────────┤          │
      │ (kembali ke form)      │          │
      │                        │          │
      │                        │ [Data valid]
      │                        │<─────────┘
      │                        │ Simpan dokumentasi
      │                        │ ke database
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │ Update status sesi:
      │                        │ "Completed"
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │ Catat timestamp
      │                        │ dokumentasi
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │ Hitung durasi
      │                        │ dokumentasi
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │ Success message        │
      │<───────────────────────┤
      │                        │
      │ Dokumentasi tersimpan  │
      │ dan dapat diakses      │
      │ untuk sesi berikutnya  │
      │                        │
      ▼                        ▼
    [END]                   [END]
```

**Gambar 4.3 Activity Diagram Dokumentasi Sesi Terapi oleh Terapis**

**Penjelasan Alur**:
1. Terapis login ke sistem
2. Terapis melihat jadwal sesi hari ini
3. Terapis memilih sesi yang sudah dilaksanakan
4. Sistem menampilkan detail sesi dan informasi klien
5. Terapis klik "Document Session"
6. Sistem menampilkan formulir dokumentasi dengan template
7. Terapis mengisi dokumentasi (teknik, observasi, kemajuan, catatan, rekomendasi)
8. Sistem melakukan auto-save setiap 30 detik untuk mencegah data loss
9. Terapis klik "Save" untuk menyimpan final
10. Sistem validasi data (jika tidak valid, tampilkan error dan kembali ke form)
11. Jika valid: Simpan dokumentasi, update status sesi "Completed", catat timestamp
12. Sistem menghitung durasi dokumentasi untuk metrics
13. Dokumentasi berhasil tersimpan dan dapat diakses untuk sesi berikutnya

#### C. Activity Diagram: Generate Laporan oleh Admin

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            ACTIVITY DIAGRAM: GENERATE LAPORAN OLEH ADMIN                    │
└─────────────────────────────────────────────────────────────────────────────┘

    ADMIN                    SISTEM
      │                        │
      │ Login                  │
      ├───────────────────────>│
      │                        │ Verify credentials
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │ Login success          │
      │<───────────────────────┤
      │                        │
      │ Akses menu "Reports"   │
      ├───────────────────────>│
      │                        │ Tampilkan halaman
      │                        │ laporan
      │<───────────────────────┤
      │                        │
      │ Pilih jenis laporan:   │
      │ - Booking Report       │
      │ - Financial Report     │
      │ - Performance Report   │
      │ - Client Report        │
      ├───────────────────────>│
      │                        │ Tampilkan form filter
      │<───────────────────────┤
      │                        │
      │ Pilih periode:         │
      │ - Tanggal mulai        │
      │ - Tanggal selesai      │
      ├───────────────────────>│
      │                        │
      │ Pilih filter tambahan: │
      │ - Terapis tertentu     │
      │ - Layanan tertentu     │
      │ - Status tertentu      │
      ├───────────────────────>│
      │                        │
      │ Klik "Generate Report" │
      ├───────────────────────>│
      │                        │ Validasi input
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │
      │                        │ [Input tidak valid]
      │                        ├──────────┐
      │ Error message          │          │
      │<───────────────────────┤          │
      │ (kembali ke form)      │          │
      │                        │          │
      │                        │ [Input valid]
      │                        │<─────────┘
      │                        │ Query database sesuai
      │                        │ kriteria
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │ Proses dan hitung
      │                        │ statistik
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │ Generate grafik dan
      │                        │ chart
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │                        │ Format data dalam
      │                        │ tabel
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │ Tampilkan laporan      │
      │<───────────────────────┤
      │                        │
      │ [Pilih aksi]           │
      │                        │
      │ Option 1: View         │
      │ ├─────────────────────>│
      │ │                      │ Tampilkan laporan
      │ │                      │ di browser
      │ │<─────────────────────┤
      │                        │
      │ Option 2: Export Excel │
      │ ├─────────────────────>│
      │ │                      │ Generate file Excel
      │ │                      ├──────────┐
      │ │                      │          │
      │ │                      │<─────────┘
      │ │ Download file Excel  │
      │ │<─────────────────────┤
      │                        │
      │ Option 3: Export PDF   │
      │ ├─────────────────────>│
      │ │                      │ Generate file PDF
      │ │                      ├──────────┐
      │ │                      │          │
      │ │                      │<─────────┘
      │ │ Download file PDF    │
      │ │<─────────────────────┤
      │                        │
      │ Option 4: Print        │
      │ └─────────────────────>│
      │                        │ Format untuk print
      │                        ├──────────┐
      │                        │          │
      │                        │<─────────┘
      │   Print dialog         │
      │<───────────────────────┤
      │                        │
      │ Laporan selesai        │
      │                        │
      ▼                        ▼
    [END]                   [END]
```

**Gambar 4.4 Activity Diagram Generate Laporan oleh Admin**

**Penjelasan Alur**:
1. Admin login ke sistem
2. Admin mengakses menu "Reports"
3. Admin memilih jenis laporan (Booking, Financial, Performance, Client)
4. Sistem menampilkan form filter
5. Admin memilih periode (tanggal mulai - tanggal selesai)
6. Admin memilih filter tambahan (terapis, layanan, status)
7. Admin klik "Generate Report"
8. Sistem validasi input (jika tidak valid, tampilkan error)
9. Jika valid: Query database sesuai kriteria
10. Sistem memproses dan menghitung statistik
11. Sistem generate grafik dan chart untuk visualisasi
12. Sistem format data dalam tabel
13. Sistem menampilkan laporan
14. Admin dapat memilih aksi:
    - View: Tampilkan di browser
    - Export Excel: Download file Excel
    - Export PDF: Download file PDF
    - Print: Print langsung
15. Laporan selesai dibuat dan dapat digunakan untuk decision making
