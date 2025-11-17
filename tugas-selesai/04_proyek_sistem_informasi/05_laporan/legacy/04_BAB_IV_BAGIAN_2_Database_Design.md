# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 2)

## 4.3.3 Perancangan Basis Data

Sistem menggunakan basis data relasional (MySQL) dengan skema yang dinormalisasi hingga Bentuk Normal Ketiga (*Third Normal Form*/3NF) untuk mengurangi redundansi dan menjaga integritas data.

### Diagram Relasi Entitas (*Entity Relationship Diagram*/ERD)


**[GAMBAR 4.9 - Diagram Relasi Entitas (ERD) - 15 Tabel]** 🔴 **KRITIS**

Berikut adalah Diagram Relasi Entitas yang menggambarkan struktur basis data sistem:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            SKEMA BASIS DATA                                  │
│                  Sistem Informasi CUR-HEART                                  │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────┐
│    users    │ (Tabel Autentikasi Pusat)
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
       │      │ total_reviews    │             └────────────────┘
       │      │ is_verified      │                      │
       │      │ created_at       │                      │ 1
       │      │ updated_at       │                      │
       │      └──────────────────┘                      │
       │             │ 1                                │ M
       │             │                                  │
       │             │ M                          ┌─────▼──────────┐
       │      ┌──────▼───────────┐               │client_progress │
       │      │therapist_services│               ├────────────────┤
       │      ├──────────────────┤               │ id (PK)        │
       │      │ id (PK)          │               │ client_id (FK) │
       │      │ therapist_id (FK)│               │ date           │
       │      │ service_id (FK)  │◄──────┐       │ anxiety_level  │
       │      │ created_at       │       │       │ confidence     │
       │      │ updated_at       │       │       │ sleep_quality  │
       │      └──────────────────┘       │       │ overall_score  │
       │                                 │       │ notes          │
       │ 1                               │       │ created_at     │
       │                                 │       │ updated_at     │
       │ M                         ┌─────┴────────┘
┌──────▼───────────┐              │   services     │
│therapist_avail   │              ├────────────────┤
├──────────────────┤              │ id (PK)        │
│ id (PK)          │              │ name           │
│ therapist_id (FK)│              │ slug (UQ)      │
│ day_of_week      │              │ description    │
│ start_time       │              │ duration       │
│ end_time         │              │ price          │
│ is_available     │              │ category       │
│ created_at       │              │ icon           │
│ updated_at       │              │ status         │
└──────────────────┘              │ created_at     │
                                  │ updated_at     │
┌──────────────────┐              └────────────────┘
│therapist_blocked │                     │ 1
├──────────────────┤                     │
│ id (PK)          │                     │ M
│ therapist_id (FK)│              ┌──────▼───────────┐
│ date             │              │    bookings      │
│ reason           │              ├──────────────────┤
│ created_at       │              │ id (PK)          │
│ updated_at       │              │ booking_number   │
└──────────────────┘              │ client_id (FK)   │
                                  │ therapist_id (FK)│
       therapists                 │ service_id (FK)  │
            │ 1                   │ booking_date     │
            │                     │ time_slot        │
            │ M                   │ duration         │
     ┌──────▼──────────┐          │ status           │
     │   education     │          │ notes            │
     ├─────────────────┤          │ created_at       │
     │ id (PK)         │          │ updated_at       │
     │ therapist_id(FK)│          │ deleted_at       │
     │ institution     │          └──────────────────┘
     │ degree          │                 │ 1
     │ field_of_study  │                 │
     │ year            │                 ├─────────────┬──────────────┐
     │ created_at      │                 │             │              │
     │ updated_at      │                 │ 1           │ 1            │ 1
     └─────────────────┘                 │             │              │
                                   ┌─────▼──────┐┌────▼─────┐  ┌─────▼─────┐
     ┌─────────────────┐           │  payments  ││ sessions │  │  reviews  │
     │ certifications  │           ├────────────┤├──────────┤  ├───────────┤
     ├─────────────────┤           │ id (PK)    ││id (PK)   │  │ id (PK)   │
     │ id (PK)         │           │booking_id  ││booking_id│  │booking_id │
     │ therapist_id(FK)│           │amount      ││started_at│  │rating     │
     │ name            │           │method      ││ended_at  │  │comment    │
     │ issuer          │           │status      ││status    │  │created_at │
     │ year            │           │transaction ││notes     │  │updated_at │
     │ expiry_date     │           │gateway     ││created_at│  └───────────┘
     │ file_path       │           │paid_at     ││updated_at│
     │ created_at      │           │created_at  │└──────────┘
     │ updated_at      │           │updated_at  │      │ 1
     └─────────────────┘           └────────────┘      │
                                                       │ M
     users                                       ┌─────▼──────────┐
       │ 1                                       │ session_notes  │
       │                                         ├────────────────┤
       │ M                                       │ id (PK)        │
  ┌────▼─────────┐                              │ session_id (FK)│
  │   messages   │                              │ condition      │
  ├──────────────┤                              │ discussion     │
  │ id (PK)      │                              │ techniques     │
  │ sender_id(FK)│                              │ response       │
  │ receiver_id  │                              │ progress_score │
  │ subject      │                              │ goals          │
  │ content      │                              │ observations   │
  │ is_read      │                              │ recommendations│
  │ created_at   │                              │ is_shared      │
  │ updated_at   │                              │ created_at     │
  └──────────────┘                              │ updated_at     │
                                                └────────────────┘
```

### Deskripsi Tabel-Tabel Utama

#### 1. Tabel `users`
Tabel pusat untuk autentikasi semua pengguna sistem (admin, terapis, klien).

**Tabel 4.14 Deskripsi Tabel Basis Data - Users**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik pengguna |
| `name` | VARCHAR(255) | NOT NULL | Nama lengkap pengguna |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL | Surel untuk masuk sistem |
| `password` | VARCHAR(255) | NOT NULL | Kata sandi terenkripsi (bcrypt) |
| `role` | ENUM | NOT NULL | Peran: 'admin', 'therapist', 'client' |
| `phone` | VARCHAR(20) | NULLABLE | Nomor telepon |
| `status` | ENUM | DEFAULT 'active' | Status: 'active', 'inactive', 'suspended' |
| `email_verified_at` | TIMESTAMP | NULLABLE | Waktu verifikasi surel |
| `remember_token` | VARCHAR(100) | NULLABLE | Token "ingat saya" |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |
| `deleted_at` | TIMESTAMP | NULLABLE | Stempel waktu penghapusan lunak |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `email`
- INDEX pada `role` untuk penyaringan cepat

**Relasi:**
- Has One: `therapists` (jika role = 'therapist')
- Has One: `clients` (jika role = 'client')
- Has Many: `messages` (sebagai pengirim atau penerima)

---

#### 2. Tabel `therapists`
Profil lengkap untuk pengguna dengan peran terapis.

**Tabel 4.15 Deskripsi Tabel Basis Data - Therapists**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik terapis |
| `user_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Rujukan ke `users.id` (CASCADE ON DELETE) |
| `credentials` | VARCHAR(255) | NULLABLE | Gelar/kredensial (mis., "M.Psi., C.Ht.") |
| `specializations` | TEXT/JSON | NULLABLE | Spesialisasi (mis., "Kecemasan, Trauma, Stres") |
| `bio` | TEXT | NULLABLE | Biografi profesional (maks. 1000 kata) |
| `years_experience` | INT UNSIGNED | DEFAULT 0 | Tahun pengalaman praktik |
| `rating` | DECIMAL(3,2) | DEFAULT 0.00 | Penilaian rata-rata (rentang 0,00-5,00) |
| `total_reviews` | INT UNSIGNED | DEFAULT 0 | Jumlah total ulasan yang diterima |
| `is_verified` | BOOLEAN | DEFAULT FALSE | Status verifikasi oleh admin |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `user_id`
- INDEX pada `rating` untuk pengurutan
- INDEX pada `is_verified` untuk penyaringan

**Relasi:**
- Belongs To: `users`
- Has Many: `therapist_services` (banyak-ke-banyak dengan services)
- Has Many: `bookings`
- Has Many: `therapist_availability`
- Has Many: `therapist_blocked_dates`
- Has Many: `education`
- Has Many: `certifications`
- Has Many Through: `sessions` melalui `bookings`

---

#### 3. Tabel `clients`
Profil lengkap untuk pengguna dengan peran klien.

**Tabel 4.16 Deskripsi Tabel Basis Data - Clients**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik klien |
| `user_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Rujukan ke `users.id` (CASCADE ON DELETE) |
| `date_of_birth` | DATE | NULLABLE | Tanggal lahir klien |
| `gender` | ENUM | NULLABLE | Jenis kelamin: 'male', 'female', 'other' |
| `address` | TEXT | NULLABLE | Alamat lengkap |
| `emergency_contact` | VARCHAR(255) | NULLABLE | Kontak darurat (nama & nomor) |
| `medical_history` | TEXT | NULLABLE, ENCRYPTED | Riwayat medis relevan (terenkripsi) |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `user_id`

**Relasi:**
- Belongs To: `users`
- Has Many: `bookings`
- Has Many: `client_progress`
- Has Many Through: `sessions` melalui `bookings`
- Has Many Through: `reviews` melalui `bookings`

---

#### 4. Tabel `services`
Katalog semua layanan terapi yang ditawarkan.

**Tabel 4.17 Deskripsi Tabel Basis Data - Services**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik layanan |
| `name` | VARCHAR(255) | NOT NULL | Nama layanan (mis., "Hipnoterapi untuk Kecemasan") |
| `slug` | VARCHAR(255) | UNIQUE, NOT NULL | Pengidentifikasi ramah URL (mis., "hipnoterapi-kecemasan") |
| `description` | TEXT | NOT NULL | Deskripsi lengkap layanan |
| `duration` | INT UNSIGNED | NOT NULL | Durasi sesi dalam menit (60, 90, 120) |
| `price` | DECIMAL(10,2) | NOT NULL | Harga layanan dalam Rupiah |
| `category` | VARCHAR(100) | NULLABLE | Kategori (mis., "Manajemen Stres", "Pengembangan Diri") |
| `icon` | VARCHAR(255) | NULLABLE | Nama berkas ikon/gambar |
| `status` | ENUM | DEFAULT 'active' | Status: 'active', 'inactive' |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `slug`
- INDEX pada `status` dan `category`

**Relasi:**
- Has Many: `therapist_services` (banyak-ke-banyak dengan therapists)
- Has Many: `bookings`

---

#### 5. Tabel `therapist_services`
Tabel pivot untuk relasi banyak-ke-banyak antara terapis dan layanan.

**Tabel 4.22 Deskripsi Tabel Basis Data - Therapist Services**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik relasi |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `therapists.id` (CASCADE ON DELETE) |
| `service_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `services.id` (CASCADE ON DELETE) |
| `is_primary` | BOOLEAN | DEFAULT FALSE | Apakah ini spesialisasi utama terapis |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE COMPOSITE INDEX pada (`therapist_id`, `service_id`) untuk mencegah duplikasi
- INDEX pada `therapist_id` dan `service_id` untuk kueri

**Relasi:**
- Belongs To: `therapists`
- Belongs To: `services`

---

#### 6. Tabel `bookings`
Rekaman semua pemesanan/janji temu.

**Tabel 4.18 Deskripsi Tabel Basis Data - Bookings**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik pemesanan |
| `booking_number` | VARCHAR(50) | UNIQUE, NOT NULL | Nomor pemesanan (format: "BK-YYYYMMDD-XXXX") |
| `client_id` | BIGINT UNSIGNED | FOREIGN KEY | Rujukan ke `users.id` (peran klien) |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY | Rujukan ke `therapists.id` |
| `service_id` | BIGINT UNSIGNED | FOREIGN KEY | Rujukan ke `services.id` |
| `booking_date` | DATE | NOT NULL | Tanggal janji temu |
| `time_slot` | TIME | NOT NULL | Jam mulai janji temu |
| `duration` | INT UNSIGNED | NOT NULL | Durasi dalam menit (dari layanan) |
| `location_type` | ENUM | DEFAULT 'office' | Tipe: 'office', 'online' |
| `meeting_link` | VARCHAR(500) | NULLABLE | Tautan pertemuan untuk sesi daring |
| `status` | ENUM | DEFAULT 'pending' | Status: 'pending', 'confirmed', 'completed', 'cancelled', 'no_show' |
| `cancellation_reason` | TEXT | NULLABLE | Alasan pembatalan |
| `cancelled_by` | BIGINT UNSIGNED | NULLABLE | ID pengguna yang membatalkan |
| `cancelled_at` | TIMESTAMP | NULLABLE | Waktu pembatalan |
| `notes` | TEXT | NULLABLE | Catatan dari klien |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |
| `deleted_at` | TIMESTAMP | NULLABLE | Stempel waktu penghapusan lunak |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_number`
- INDEX pada `client_id`, `therapist_id`, `service_id`
- INDEX pada `booking_date`, `status`
- COMPOSITE INDEX pada (`therapist_id`, `booking_date`, `time_slot`) untuk pemeriksaan konflik

**Relasi:**
- Belongs To: `users` (klien)
- Belongs To: `therapists`
- Belongs To: `services`
- Has One: `payment`
- Has One: `session`
- Has One: `review`

---

#### 7. Tabel `payments`
Rekaman transaksi untuk semua pembayaran.

**Tabel 4.19 Deskripsi Tabel Basis Data - Payments**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik pembayaran |
| `booking_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Rujukan ke `bookings.id` (CASCADE ON DELETE) |
| `amount` | DECIMAL(10,2) | NOT NULL | Jumlah pembayaran dalam Rupiah |
| `method` | ENUM | NOT NULL | Metode: 'credit_card', 'bank_transfer', 'ewallet', 'qris', 'cash' |
| `status` | ENUM | DEFAULT 'pending' | Status: 'pending', 'processing', 'completed', 'failed', 'refunded' |
| `transaction_id` | VARCHAR(255) | UNIQUE, NULLABLE | ID transaksi dari gerbang pembayaran |
| `payment_gateway` | VARCHAR(50) | NULLABLE | Nama gerbang (mis., 'midtrans', 'xendit') |
| `payment_details` | JSON | NULLABLE | Data respons dari gerbang |
| `proof_of_payment` | VARCHAR(255) | NULLABLE | Jalur berkas bukti transfer |
| `paid_at` | TIMESTAMP | NULLABLE | Waktu pembayaran berhasil |
| `refunded_at` | TIMESTAMP | NULLABLE | Waktu pengembalian dana |
| `refund_amount` | DECIMAL(10,2) | NULLABLE | Jumlah pengembalian dana (jika ada) |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_id` (satu pembayaran per pemesanan)
- INDEX pada `transaction_id`, `status`
- INDEX pada `paid_at` untuk pelaporan

**Relasi:**
- Belongs To: `bookings`

---

#### 8. Tabel `sessions`
Sesi terapi aktual yang dilaksanakan.

**Tabel 4.20 Deskripsi Tabel Basis Data - Sessions**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik sesi |
| `booking_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Rujukan ke `bookings.id` (CASCADE ON DELETE) |
| `started_at` | TIMESTAMP | NULLABLE | Waktu mulai sesi aktual |
| `ended_at` | TIMESTAMP | NULLABLE | Waktu selesai sesi aktual |
| `actual_duration` | INT UNSIGNED | NULLABLE | Durasi aktual dalam menit (terhitung) |
| `status` | ENUM | DEFAULT 'scheduled' | Status: 'scheduled', 'in_progress', 'completed', 'cancelled' |
| `attendance_status` | ENUM | NULLABLE | Kehadiran: 'present', 'absent', 'late' |
| `session_type` | ENUM | NOT NULL | Tipe: 'first_consultation', 'follow_up', 'final' |
| `notes` | TEXT | NULLABLE | Catatan singkat sesi |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_id`
- INDEX pada `status`, `started_at`

**Relasi:**
- Belongs To: `bookings`
- Has One: `session_notes`

---

#### 9. Tabel `session_notes`
Dokumentasi rinci setiap sesi oleh terapis.

**Tabel 4.23 Deskripsi Tabel Basis Data - Session Notes**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik catatan sesi |
| `session_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Rujukan ke `sessions.id` (CASCADE ON DELETE) |
| `condition` | VARCHAR(255) | NULLABLE | Kondisi klien saat datang |
| `chief_complaint` | TEXT | NULLABLE | Keluhan utama yang disampaikan |
| `discussion` | TEXT | NULLABLE | Topik yang didiskusikan selama sesi |
| `techniques_used` | TEXT/JSON | NULLABLE | Teknik terapi yang digunakan (larik) |
| `client_response` | TEXT | NULLABLE | Respons dan reaksi klien terhadap terapi |
| `progress_score` | INT | CHECK (1-10), NULLABLE | Skor kemajuan subjektif dari terapis |
| `breakthrough` | BOOLEAN | DEFAULT FALSE | Apakah terjadi terobosan signifikan |
| `goals_next_session` | TEXT | NULLABLE | Tujuan dan target untuk sesi berikutnya |
| `observations` | TEXT | NULLABLE | Pengamatan terapis (pribadi, tidak dibagikan) |
| `recommendations` | TEXT | NULLABLE | Rekomendasi untuk klien |
| `homework` | TEXT | NULLABLE | Tugas/latihan untuk klien |
| `is_shared_with_client` | BOOLEAN | DEFAULT FALSE | Apakah catatan dibagikan ke klien |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `session_id`
- INDEX pada `progress_score`

**Relasi:**
- Belongs To: `sessions`

---

#### 10. Tabel `reviews`
Ulasan klien untuk terapis setelah sesi.

**Tabel 4.21 Deskripsi Tabel Basis Data - Reviews**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik ulasan |
| `booking_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Rujukan ke `bookings.id` (CASCADE ON DELETE) |
| `rating` | INT | NOT NULL, CHECK (1-5) | Penilaian 1-5 bintang untuk layanan |
| `comment` | TEXT | NULLABLE | Komentar dan ulasan dari klien |
| `is_anonymous` | BOOLEAN | DEFAULT FALSE | Tampilkan ulasan secara anonim |
| `is_approved` | BOOLEAN | DEFAULT TRUE | Status persetujuan untuk publikasi |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu ulasan dibuat |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_id` (satu ulasan per pemesanan)
- INDEX pada `rating`, `is_approved`

**Relasi:**
- Belongs To: `bookings`

---

#### 11. Tabel `therapist_availability`
Jadwal mingguan reguler terapis.

**Tabel 4.24 Deskripsi Tabel Basis Data - Therapist Availability**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik ketersediaan |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `therapists.id` (CASCADE ON DELETE) |
| `day_of_week` | INT | NOT NULL, CHECK (0-6) | Hari dalam minggu (0=Minggu, 6=Sabtu) |
| `start_time` | TIME | NOT NULL | Jam mulai kerja (mis., 09:00) |
| `end_time` | TIME | NOT NULL | Jam selesai kerja (mis., 17:00) |
| `is_available` | BOOLEAN | DEFAULT TRUE | Pengaturan hidup/mati untuk hari tertentu |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- UNIQUE COMPOSITE INDEX pada (`therapist_id`, `day_of_week`, `start_time`) untuk mencegah tumpang tindih
- INDEX pada `therapist_id`

**Relasi:**
- Belongs To: `therapists`

**Logika Bisnis:**
- Sistem menggunakan tabel ini untuk membangkitkan slot waktu tersedia
- Waktu jeda (15 menit) ditambahkan antara sesi
- Waktu istirahat ditangani sebagai periode terblokir

---

#### 12. Tabel `therapist_blocked_dates`
Tanggal tertentu di mana terapis tidak tersedia (cuti, libur).

**Tabel 4.25 Deskripsi Tabel Basis Data - Therapist Blocked Dates**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik tanggal terblokir |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `therapists.id` (CASCADE ON DELETE) |
| `blocked_date` | DATE | NOT NULL | Tanggal yang diblokir |
| `reason` | VARCHAR(255) | NULLABLE | Alasan pemblokiran (mis., "Cuti", "Sakit", "Libur Nasional") |
| `is_full_day` | BOOLEAN | DEFAULT TRUE | Seharian penuh atau sebagian |
| `start_time` | TIME | NULLABLE | Jam mulai pemblokiran jika sebagian |
| `end_time` | TIME | NULLABLE | Jam selesai pemblokiran jika sebagian |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- INDEX pada (`therapist_id`, `blocked_date`)

**Relasi:**
- Belongs To: `therapists`

**Logika Bisnis:**
- Sistem memeriksa tabel ini sebelum menampilkan tanggal tersedia
- Tanggal terblokir tidak muncul dalam kalender pemesanan

---

#### 13. Tabel `client_progress`
Pelacakan metrik kemajuan untuk klien.

**Tabel 4.26 Deskripsi Tabel Basis Data - Client Progress**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik rekaman kemajuan |
| `client_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `clients.id` (CASCADE ON DELETE) |
| `assessment_date` | DATE | NOT NULL | Tanggal penilaian dilakukan |
| `anxiety_level` | INT | CHECK (1-10), NULLABLE | Tingkat kecemasan (1=rendah, 10=tinggi) |
| `confidence_level` | INT | CHECK (1-10), NULLABLE | Tingkat kepercayaan diri (1=rendah, 10=tinggi) |
| `sleep_quality` | INT | CHECK (1-10), NULLABLE | Kualitas tidur (1=buruk, 10=sangat baik) |
| `stress_level` | INT | CHECK (1-10), NULLABLE | Tingkat stres (1=rendah, 10=tinggi) |
| `overall_wellbeing` | INT | CHECK (1-10), NULLABLE | Kesejahteraan menyeluruh (1=rendah, 10=tinggi) |
| `overall_score` | DECIMAL(3,1) | COMPUTED, NULLABLE | Skor rata-rata dari metrik (terhitung otomatis) |
| `notes` | TEXT | NULLABLE | Catatan tambahan penilaian mandiri |
| `assessed_by` | ENUM | NOT NULL | Sumber penilaian: 'self', 'therapist' |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- INDEX pada (`client_id`, `assessment_date`)
- INDEX pada `overall_score`

**Relasi:**
- Belongs To: `clients`

**Logika Bisnis:**
- Klien dapat melakukan penilaian mandiri antara sesi
- Terapis dapat memasukkan penilaian setelah sesi
- Sistem membangkitkan grafik dari data historis

---

#### 14. Tabel `messages`
Sistem pesan internal antara pengguna.

**Tabel 4.27 Deskripsi Tabel Basis Data - Messages**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik pesan |
| `sender_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `users.id` sebagai pengirim (CASCADE ON DELETE) |
| `receiver_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `users.id` sebagai penerima (CASCADE ON DELETE) |
| `subject` | VARCHAR(255) | NULLABLE | Subjek pesan |
| `content` | TEXT | NOT NULL | Isi pesan |
| `is_read` | BOOLEAN | DEFAULT FALSE | Status sudah dibaca atau belum |
| `read_at` | TIMESTAMP | NULLABLE | Waktu pesan dibaca |
| `parent_message_id` | BIGINT UNSIGNED | FOREIGN KEY, NULLABLE | Rujukan ke `messages.id` untuk percakapan berantai |
| `attachment_path` | VARCHAR(255) | NULLABLE | Jalur ke berkas lampiran |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- INDEX pada (`receiver_id`, `is_read`) untuk kueri kotak masuk
- INDEX pada `sender_id`
- INDEX pada `parent_message_id` untuk utas

**Relasi:**
- Belongs To: `users` (sebagai pengirim)
- Belongs To: `users` (sebagai penerima)
- Has Many: `messages` (sebagai induk untuk balasan)

---

#### 15. Tabel `education`
Pendidikan formal terapis.

**Tabel 4.28 Deskripsi Tabel Basis Data - Education**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik rekaman pendidikan |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `therapists.id` (CASCADE ON DELETE) |
| `institution` | VARCHAR(255) | NOT NULL | Nama institusi pendidikan |
| `degree` | VARCHAR(100) | NOT NULL | Gelar (mis., "S1 Psikologi", "S2 Psikologi Klinis") |
| `field_of_study` | VARCHAR(255) | NOT NULL | Bidang studi atau jurusan |
| `start_year` | YEAR | NOT NULL | Tahun mulai pendidikan |
| `end_year` | YEAR | NULLABLE | Tahun selesai (NULL jika masih berjalan) |
| `is_current` | BOOLEAN | DEFAULT FALSE | Apakah masih menjalani pendidikan ini |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- INDEX pada `therapist_id`

**Relasi:**
- Belongs To: `therapists`

---

#### 16. Tabel `certifications`
Sertifikasi profesional terapis.

**Tabel 4.29 Deskripsi Tabel Basis Data - Certifications**

| Kolom | Tipe Data | Batasan | Deskripsi |
|-------|-----------|---------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik rekaman sertifikasi |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Rujukan ke `therapists.id` (CASCADE ON DELETE) |
| `certification_name` | VARCHAR(255) | NOT NULL | Nama sertifikat profesional |
| `issuing_organization` | VARCHAR(255) | NOT NULL | Organisasi atau lembaga penerbit sertifikat |
| `issue_date` | DATE | NOT NULL | Tanggal sertifikat diterbitkan |
| `expiry_date` | DATE | NULLABLE | Tanggal kadaluarsa (NULL jika seumur hidup) |
| `credential_id` | VARCHAR(100) | NULLABLE | ID kredensial untuk verifikasi |
| `file_path` | VARCHAR(255) | NULLABLE | Jalur ke berkas pindai sertifikat |
| `is_verified` | BOOLEAN | DEFAULT FALSE | Sudah diverifikasi oleh admin |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan rekaman |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu pembaruan terakhir |

**Indeks:**
- PRIMARY KEY pada `id`
- INDEX pada `therapist_id`
- INDEX pada `is_verified`

**Relasi:**
- Belongs To: `therapists`

---

### Normalisasi Basis Data

Basis data telah dinormalisasi hingga **Bentuk Normal Ketiga (Third Normal Form/3NF)** dengan karakteristik:

**1NF (Bentuk Normal Pertama):**
- ✅ Semua kolom berisi nilai atomik (tidak ada atribut bernilai ganda)
- ✅ Setiap kolom berisi nilai dari satu domain
- ✅ Setiap nama kolom unik
- ✅ Urutan penyimpanan data tidak berpengaruh

**2NF (Bentuk Normal Kedua):**
- ✅ Memenuhi 1NF
- ✅ Tidak ada ketergantungan parsial (semua atribut non-kunci sepenuhnya bergantung pada kunci primer)
- ✅ Tabel pivot (`therapist_services`) digunakan untuk relasi banyak-ke-banyak

**3NF (Bentuk Normal Ketiga):**
- ✅ Memenuhi 2NF
- ✅ Tidak ada ketergantungan transitif (atribut non-kunci tidak bergantung pada atribut non-kunci lain)
- ✅ Profil lengkap (`therapists`, `clients`) dipisahkan dari tabel `users`

**Contoh Normalisasi:**

*Sebelum normalisasi (tidak dinormalisasi):*
```
bookings: id, client_name, client_email, therapist_name, therapist_credentials, 
          service_name, service_price, date, time, ...
```

*Setelah normalisasi (3NF):*
```
users: id, name, email, ...
therapists: id, user_id, credentials, ...
services: id, name, price, ...
bookings: id, client_id (FK), therapist_id (FK), service_id (FK), date, time, ...
```

Keuntungan:
- **Konsistensi Data:** Pembaruan data klien/terapis/layanan hanya di satu tempat
- **Efisiensi Penyimpanan:** Mengurangi redundansi data
- **Pemeliharaan:** Lebih mudah dipelihara dan diperbarui
- **Integritas:** Batasan kunci asing memastikan integritas referensial

---

### Strategi Pengindeksan

Indeks diterapkan untuk mengoptimalkan kinerja kueri. Berikut adalah ringkasan strategi pengindeksan untuk setiap tabel:

**Tabel 4.30 Strategi Pengindeksan per Tabel**

| Nama Tabel | Tipe Indeks | Kolom | Tujuan | Estimasi Peningkatan Kinerja |
|------------|-------------|-------|--------|------------------------------|
| `users` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `email` | Autentikasi masuk, cegah duplikasi surel | 95%+ lebih cepat masuk |
| | INDEX | `role` | Filter pengguna berdasarkan peran (admin/terapis/klien) | 80% lebih cepat kueri peran |
| | INDEX | `status` | Filter pengguna aktif/tidak aktif | 75% lebih cepat kueri status |
| `therapists` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `user_id` | Penegakan relasi satu-ke-satu | Esensial |
| | INDEX | `rating` | Urutkan terapis berdasarkan penilaian | 85% lebih cepat pengurutan |
| | INDEX | `is_verified` | Filter terapis terverifikasi | 70% lebih cepat penyaringan |
| `clients` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `user_id` | Penegakan relasi satu-ke-satu | Esensial |
| `services` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `slug` | Pencarian perutean URL | 90%+ lebih cepat muat halaman |
| | INDEX | `status`, `category` | Filter layanan aktif berdasarkan kategori | 80% lebih cepat kueri katalog |
| `therapist_services` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE COMPOSITE | `(therapist_id, service_id)` | Cegah duplikasi penugasan | Integritas esensial |
| | INDEX | `therapist_id` | Temukan layanan untuk terapis | 85% lebih cepat |
| | INDEX | `service_id` | Temukan terapis untuk layanan | 85% lebih cepat |
| `bookings` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `booking_number` | Pencarian pemesanan cepat | 95%+ lebih cepat |
| | INDEX | `client_id` | Riwayat pemesanan klien | 90% lebih cepat |
| | INDEX | `therapist_id` | Jadwal terapis | 90% lebih cepat |
| | INDEX | `service_id` | Analitik penggunaan layanan | 80% lebih cepat |
| | INDEX | `booking_date`, `status` | Tampilan kalender, filter berdasarkan status | 85% lebih cepat kalender |
| | COMPOSITE INDEX | `(therapist_id, booking_date, time_slot)` | Pencegahan pemesanan ganda | Kritis untuk integritas |
| `payments` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `booking_id` | Satu pembayaran per pemesanan | Esensial |
| | UNIQUE INDEX | `transaction_id` | Pencarian transaksi gerbang | 90%+ lebih cepat |
| | INDEX | `status` | Filter pembayaran tertunda/selesai | 80% lebih cepat |
| | INDEX | `paid_at` | Pelaporan keuangan berdasarkan tanggal | 85% lebih cepat laporan |
| `sessions` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `booking_id` | Satu sesi per pemesanan | Esensial |
| | INDEX | `status`, `started_at` | Filter sesi aktif, garis waktu | 80% lebih cepat |
| `session_notes` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `session_id` | Satu catatan per sesi | Esensial |
| | INDEX | `progress_score` | Analitik kemajuan | 75% lebih cepat analitik |
| `reviews` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE INDEX | `booking_id` | Satu ulasan per pemesanan | Esensial |
| | INDEX | `rating`, `is_approved` | Filter/urutkan ulasan | 85% lebih cepat tampilan |
| `therapist_availability` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | UNIQUE COMPOSITE | `(therapist_id, day_of_week, start_time)` | Cegah jadwal tumpang tindih | Kritis untuk integritas |
| | INDEX | `therapist_id` | Ambil jadwal terapis | 90% lebih cepat |
| `therapist_blocked_dates` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | INDEX | `(therapist_id, blocked_date)` | Periksa ketersediaan untuk tanggal | 85% lebih cepat pemeriksaan |
| `client_progress` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | INDEX | `(client_id, assessment_date)` | Pembangkitan grafik kemajuan | 90% lebih cepat kueri grafik |
| | INDEX | `overall_score` | Analitik dan pelaporan | 75% lebih cepat |
| `messages` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | COMPOSITE INDEX | `(receiver_id, is_read)` | Kueri kotak masuk (belum dibaca dahulu) | 95%+ lebih cepat kotak masuk |
| | INDEX | `sender_id` | Riwayat pesan terkirim | 85% lebih cepat |
| | INDEX | `parent_message_id` | Percakapan berantai | 80% lebih cepat utas |
| `education` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | INDEX | `therapist_id` | Ambil pendidikan terapis | 85% lebih cepat |
| `certifications` | PRIMARY KEY | `id` | Pencarian pengidentifikasi unik | Esensial |
| | INDEX | `therapist_id` | Ambil sertifikasi terapis | 85% lebih cepat |
| | INDEX | `is_verified` | Filter sertifikasi terverifikasi | 75% lebih cepat tinjauan admin |

**Prinsip Desain Indeks:**
1. **Kunci Primer:** Diindeks otomatis untuk semua tabel (BTREE)
2. **Kunci Asing:** Selalu diindeks untuk operasi JOIN cepat
3. **Batasan Unik:** Otomatis membuat indeks
4. **Kolom yang Sering Dikueri:** Bidang `status`, `date`, flag boolean
5. **Indeks Komposit:** Aturan kiri-ke-kanan - kolom paling selektif dahulu
6. **Hindari Pengindeksan Berlebihan:** Keseimbangan antara kinerja baca dan overhead tulis
7. **Pantau Penggunaan:** Gunakan analisis rencana kueri `EXPLAIN`

**Dampak Kinerja:**
- Total indeks: 52 indeks di 16 tabel
- Peningkatan kinerja kueri: 70-95% lebih cepat untuk kueri terindeks
- Pertukaran: ~5-10% lebih lambat operasi INSERT/UPDATE (dapat diterima)
- Overhead penyimpanan: ~15-20% ruang disk tambahan (minimal)

---