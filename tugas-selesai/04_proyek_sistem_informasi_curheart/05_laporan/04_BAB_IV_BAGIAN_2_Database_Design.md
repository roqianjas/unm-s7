# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 2)

## 4.3.3 Database Design

Sistem menggunakan relational database (MySQL) dengan schema yang dinormalisasi hingga Third Normal Form (3NF) untuk mengurangi redundansi dan menjaga data integrity.

### Entity Relationship Diagram (ERD)

Berikut adalah Entity Relationship Diagram yang menggambarkan struktur database sistem:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            DATABASE SCHEMA                                   │
│                     CUR-HEART Information System                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────┐
│    users    │ (Central Authentication Table)
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

### Deskripsi Tabel-tabel Utama

#### 1. Tabel `users`
Tabel central untuk autentikasi semua pengguna sistem (admin, therapist, client).

**Kolom:**
- `id`: Primary key (BIGINT UNSIGNED AUTO_INCREMENT)
- `name`: Nama lengkap pengguna (VARCHAR 255)
- `email`: Email unik untuk login (VARCHAR 255, UNIQUE)
- `password`: Password ter-hash menggunakan bcrypt (VARCHAR 255)
- `role`: Role pengguna (ENUM: 'admin', 'therapist', 'client')
- `phone`: Nomor telepon (VARCHAR 20, NULLABLE)
- `status`: Status akun (ENUM: 'active', 'inactive', 'suspended')
- `email_verified_at`: Timestamp verifikasi email (TIMESTAMP, NULLABLE)
- `remember_token`: Token untuk "remember me" functionality (VARCHAR 100)
- `created_at`, `updated_at`: Timestamps Laravel
- `deleted_at`: Soft delete timestamp (NULLABLE)

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `email`
- INDEX pada `role` untuk filtering cepat

**Relasi:**
- Has One: `therapists` (jika role = 'therapist')
- Has One: `clients` (jika role = 'client')
- Has Many: `messages` (sebagai sender atau receiver)

---

#### 2. Tabel `therapists`
Extended profile untuk users dengan role therapist.

**Kolom:**
- `id`: Primary key
- `user_id`: Foreign key ke `users.id` (CASCADE ON DELETE)
- `credentials`: Gelar/kredensial (VARCHAR 255, e.g., "M.Psi., C.Ht.")
- `specializations`: Spesialisasi (TEXT/JSON, e.g., "Anxiety, Trauma, Stress")
- `bio`: Biografi profesional (TEXT, max 1000 kata)
- `years_experience`: Tahun pengalaman (INT UNSIGNED)
- `rating`: Rating rata-rata (DECIMAL 3,2, default 0.00, range 0-5)
- `total_reviews`: Jumlah total review (INT UNSIGNED, default 0)
- `is_verified`: Status verifikasi admin (BOOLEAN, default FALSE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `user_id`
- INDEX pada `rating` untuk sorting
- INDEX pada `is_verified` untuk filtering

**Relasi:**
- Belongs To: `users`
- Has Many: `therapist_services` (many-to-many dengan services)
- Has Many: `bookings`
- Has Many: `therapist_availability`
- Has Many: `therapist_blocked_dates`
- Has Many: `education`
- Has Many: `certifications`
- Has Many Through: `sessions` melalui `bookings`

---

#### 3. Tabel `clients`
Extended profile untuk users dengan role client.

**Kolom:**
- `id`: Primary key
- `user_id`: Foreign key ke `users.id` (CASCADE ON DELETE)
- `date_of_birth`: Tanggal lahir (DATE, NULLABLE)
- `gender`: Jenis kelamin (ENUM: 'male', 'female', 'other', NULLABLE)
- `address`: Alamat lengkap (TEXT, NULLABLE)
- `emergency_contact`: Kontak darurat (VARCHAR 255, NULLABLE)
- `medical_history`: Riwayat medis relevan (TEXT, NULLABLE, encrypted)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
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

**Kolom:**
- `id`: Primary key
- `name`: Nama layanan (VARCHAR 255, e.g., "Hypnotherapy untuk Kecemasan")
- `slug`: URL-friendly identifier (VARCHAR 255, UNIQUE, e.g., "hypnotherapy-kecemasan")
- `description`: Deskripsi lengkap layanan (TEXT)
- `duration`: Durasi sesi dalam menit (INT UNSIGNED, e.g., 60, 90, 120)
- `price`: Harga layanan (DECIMAL 10,2)
- `category`: Kategori layanan (VARCHAR 100, e.g., "Stress Management", "Personal Growth")
- `icon`: Nama icon/image file (VARCHAR 255, NULLABLE)
- `status`: Status aktif/nonaktif (ENUM: 'active', 'inactive')
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `slug`
- INDEX pada `status` dan `category`

**Relasi:**
- Has Many: `therapist_services` (many-to-many dengan therapists)
- Has Many: `bookings`

---

#### 5. Tabel `therapist_services`
Pivot table untuk relasi many-to-many antara therapists dan services.

**Kolom:**
- `id`: Primary key
- `therapist_id`: Foreign key ke `therapists.id` (CASCADE ON DELETE)
- `service_id`: Foreign key ke `services.id` (CASCADE ON DELETE)
- `is_primary`: Apakah ini primary specialization (BOOLEAN, default FALSE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE COMPOSITE INDEX pada (`therapist_id`, `service_id`) untuk prevent duplicates
- INDEX pada `therapist_id` dan `service_id` untuk queries

**Relasi:**
- Belongs To: `therapists`
- Belongs To: `services`

---

#### 6. Tabel `bookings`
Records semua booking/appointment.

**Kolom:**
- `id`: Primary key
- `booking_number`: Nomor booking unik (VARCHAR 50, UNIQUE, format: "BK-YYYYMMDD-XXXX")
- `client_id`: Foreign key ke `users.id` (client role)
- `therapist_id`: Foreign key ke `therapists.id`
- `service_id`: Foreign key ke `services.id`
- `booking_date`: Tanggal appointment (DATE)
- `time_slot`: Jam mulai appointment (TIME)
- `duration`: Durasi dalam menit (INT UNSIGNED, copied dari service)
- `location_type`: Tipe lokasi (ENUM: 'office', 'online', default 'office')
- `meeting_link`: Link meeting untuk online session (VARCHAR 500, NULLABLE)
- `status`: Status booking (ENUM: 'pending', 'confirmed', 'completed', 'cancelled', 'no_show')
- `cancellation_reason`: Alasan pembatalan (TEXT, NULLABLE)
- `cancelled_by`: User ID yang membatalkan (BIGINT UNSIGNED, NULLABLE)
- `cancelled_at`: Timestamp pembatalan (TIMESTAMP, NULLABLE)
- `notes`: Catatan dari client (TEXT, NULLABLE)
- `created_at`, `updated_at`, `deleted_at`: Timestamps (soft deletes)

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_number`
- INDEX pada `client_id`, `therapist_id`, `service_id`
- INDEX pada `booking_date`, `status`
- COMPOSITE INDEX pada (`therapist_id`, `booking_date`, `time_slot`) untuk conflict checking

**Relasi:**
- Belongs To: `users` (client)
- Belongs To: `therapists`
- Belongs To: `services`
- Has One: `payment`
- Has One: `session`
- Has One: `review`

---

#### 7. Tabel `payments`
Transaction records untuk semua pembayaran.

**Kolom:**
- `id`: Primary key
- `booking_id`: Foreign key ke `bookings.id` (CASCADE ON DELETE)
- `amount`: Jumlah pembayaran (DECIMAL 10,2)
- `method`: Metode pembayaran (ENUM: 'credit_card', 'bank_transfer', 'ewallet', 'qris', 'cash')
- `status`: Status pembayaran (ENUM: 'pending', 'processing', 'completed', 'failed', 'refunded')
- `transaction_id`: ID transaksi dari payment gateway (VARCHAR 255, UNIQUE, NULLABLE)
- `payment_gateway`: Nama gateway (VARCHAR 50, e.g., 'midtrans', 'xendit', NULLABLE)
- `payment_details`: JSON data dari gateway response (JSON, NULLABLE)
- `proof_of_payment`: Path ke file bukti transfer (VARCHAR 255, NULLABLE untuk bank transfer)
- `paid_at`: Timestamp pembayaran sukses (TIMESTAMP, NULLABLE)
- `refunded_at`: Timestamp refund (TIMESTAMP, NULLABLE)
- `refund_amount`: Jumlah refund (DECIMAL 10,2, NULLABLE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_id` (one payment per booking)
- INDEX pada `transaction_id`, `status`
- INDEX pada `paid_at` untuk reporting

**Relasi:**
- Belongs To: `bookings`

---

#### 8. Tabel `sessions`
Actual therapy sessions yang dilaksanakan.

**Kolom:**
- `id`: Primary key
- `booking_id`: Foreign key ke `bookings.id` (CASCADE ON DELETE)
- `started_at`: Timestamp mulai session (TIMESTAMP, NULLABLE)
- `ended_at`: Timestamp selesai session (TIMESTAMP, NULLABLE)
- `actual_duration`: Durasi aktual dalam menit (INT UNSIGNED, calculated)
- `status`: Status session (ENUM: 'scheduled', 'in_progress', 'completed', 'cancelled')
- `attendance_status`: Status kehadiran (ENUM: 'present', 'absent', 'late')
- `session_type`: Tipe session (ENUM: 'first_consultation', 'follow_up', 'final')
- `notes`: Catatan singkat (TEXT, NULLABLE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_id`
- INDEX pada `status`, `started_at`

**Relasi:**
- Belongs To: `bookings`
- Has One: `session_notes`

---

#### 9. Tabel `session_notes`
Detailed documentation setiap session oleh therapist.

**Kolom:**
- `id`: Primary key
- `session_id`: Foreign key ke `sessions.id` (CASCADE ON DELETE)
- `condition`: Kondisi client saat datang (VARCHAR 255)
- `chief_complaint`: Keluhan utama (TEXT)
- `discussion`: Topik yang didiskusikan (TEXT)
- `techniques_used`: Teknik yang digunakan (TEXT/JSON array)
- `client_response`: Respons client terhadap terapi (TEXT)
- `progress_score`: Skor progress subjektif (INT 1-10)
- `breakthrough`: Apakah ada breakthrough (BOOLEAN, default FALSE)
- `goals_next_session`: Goals untuk session berikutnya (TEXT)
- `observations`: Observasi therapist (TEXT, private)
- `recommendations`: Rekomendasi untuk client (TEXT, can be shared)
- `homework`: Tugas untuk client (TEXT, NULLABLE)
- `is_shared_with_client`: Apakah note dibagikan ke client (BOOLEAN, default FALSE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `session_id`
- INDEX pada `progress_score`

**Relasi:**
- Belongs To: `sessions`

---

#### 10. Tabel `reviews`
Client reviews untuk therapists setelah session.

**Kolom:**
- `id`: Primary key
- `booking_id`: Foreign key ke `bookings.id` (CASCADE ON DELETE)
- `rating`: Rating 1-5 bintang (INT, range 1-5)
- `comment`: Komentar review (TEXT, NULLABLE)
- `is_anonymous`: Apakah review anonim (BOOLEAN, default FALSE)
- `is_approved`: Apakah disetujui admin untuk publish (BOOLEAN, default TRUE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_id` (one review per booking)
- INDEX pada `rating`, `is_approved`

**Relasi:**
- Belongs To: `bookings`

---

#### 11. Tabel `therapist_availability`
Regular weekly schedule therapists.

**Kolom:**
- `id`: Primary key
- `therapist_id`: Foreign key ke `therapists.id` (CASCADE ON DELETE)
- `day_of_week`: Hari dalam minggu (INT 0-6, 0=Sunday, 6=Saturday)
- `start_time`: Jam mulai kerja (TIME)
- `end_time`: Jam selesai kerja (TIME)
- `is_available`: Toggle on/off untuk specific day (BOOLEAN, default TRUE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE COMPOSITE INDEX pada (`therapist_id`, `day_of_week`, `start_time`) untuk prevent overlaps
- INDEX pada `therapist_id`

**Relasi:**
- Belongs To: `therapists`

**Business Logic:**
- System menggunakan tabel ini untuk generate available time slots
- Buffer time (15 minutes) ditambahkan antara sessions
- Break times di-handle sebagai blocked periods

---

#### 12. Tabel `therapist_blocked_dates`
Specific dates di mana therapist tidak available (cuti, libur).

**Kolom:**
- `id`: Primary key
- `therapist_id`: Foreign key ke `therapists.id` (CASCADE ON DELETE)
- `blocked_date`: Tanggal yang di-block (DATE)
- `reason`: Alasan blocking (VARCHAR 255, NULLABLE)
- `is_full_day`: Full day atau partial (BOOLEAN, default TRUE)
- `start_time`: Jam mulai blocking jika partial (TIME, NULLABLE)
- `end_time`: Jam selesai blocking jika partial (TIME, NULLABLE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- INDEX pada (`therapist_id`, `blocked_date`)

**Relasi:**
- Belongs To: `therapists`

**Business Logic:**
- System check tabel ini sebelum show available dates
- Blocked dates tidak muncul dalam calendar booking

---

#### 13. Tabel `client_progress`
Progress tracking metrics untuk clients.

**Kolom:**
- `id`: Primary key
- `client_id`: Foreign key ke `clients.id` (CASCADE ON DELETE)
- `assessment_date`: Tanggal assessment (DATE)
- `anxiety_level`: Level kecemasan (INT 1-10)
- `confidence_level`: Level kepercayaan diri (INT 1-10)
- `sleep_quality`: Kualitas tidur (INT 1-10)
- `stress_level`: Level stress (INT 1-10)
- `overall_wellbeing`: Overall well-being (INT 1-10)
- `overall_score`: Calculated average score (DECIMAL 3,1, computed)
- `notes`: Catatan self-assessment (TEXT, NULLABLE)
- `assessed_by`: 'self' atau 'therapist' (ENUM: 'self', 'therapist')
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- INDEX pada (`client_id`, `assessment_date`)
- INDEX pada `overall_score`

**Relasi:**
- Belongs To: `clients`

**Business Logic:**
- Client bisa self-assess antara sessions
- Therapist bisa input assessment setelah session
- System generate charts dari historical data

---

#### 14. Tabel `messages`
Internal messaging system antara users.

**Kolom:**
- `id`: Primary key
- `sender_id`: Foreign key ke `users.id` (CASCADE ON DELETE)
- `receiver_id`: Foreign key ke `users.id` (CASCADE ON DELETE)
- `subject`: Subjek pesan (VARCHAR 255, NULLABLE)
- `content`: Isi pesan (TEXT)
- `is_read`: Status sudah dibaca (BOOLEAN, default FALSE)
- `read_at`: Timestamp dibaca (TIMESTAMP, NULLABLE)
- `parent_message_id`: FK untuk threaded conversation (BIGINT UNSIGNED, NULLABLE)
- `attachment_path`: Path ke file attachment (VARCHAR 255, NULLABLE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- INDEX pada (`receiver_id`, `is_read`) untuk inbox queries
- INDEX pada `sender_id`
- INDEX pada `parent_message_id` untuk threads

**Relasi:**
- Belongs To: `users` (sebagai sender)
- Belongs To: `users` (sebagai receiver)
- Has Many: `messages` (sebagai parent untuk replies)

---

#### 15. Tabel `education`
Pendidikan formal therapists.

**Kolom:**
- `id`: Primary key
- `therapist_id`: Foreign key ke `therapists.id` (CASCADE ON DELETE)
- `institution`: Nama institusi (VARCHAR 255)
- `degree`: Gelar (VARCHAR 100, e.g., "S1 Psikologi", "S2 Psikologi Klinis")
- `field_of_study`: Bidang studi (VARCHAR 255)
- `start_year`: Tahun mulai (YEAR)
- `end_year`: Tahun selesai (YEAR, NULLABLE jika masih berjalan)
- `is_current`: Masih berjalan (BOOLEAN, default FALSE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- INDEX pada `therapist_id`

**Relasi:**
- Belongs To: `therapists`

---

#### 16. Tabel `certifications`
Sertifikasi profesional therapists.

**Kolom:**
- `id`: Primary key
- `therapist_id`: Foreign key ke `therapists.id` (CASCADE ON DELETE)
- `certification_name`: Nama sertifikat (VARCHAR 255)
- `issuing_organization`: Organisasi penerbit (VARCHAR 255)
- `issue_date`: Tanggal terbit (DATE)
- `expiry_date`: Tanggal kadaluarsa (DATE, NULLABLE)
- `credential_id`: ID kredensial (VARCHAR 100, NULLABLE)
- `file_path`: Path ke file sertifikat (VARCHAR 255, NULLABLE)
- `is_verified`: Sudah diverifikasi admin (BOOLEAN, default FALSE)
- `created_at`, `updated_at`: Timestamps

**Indexes:**
- PRIMARY KEY pada `id`
- INDEX pada `therapist_id`
- INDEX pada `is_verified`

**Relasi:**
- Belongs To: `therapists`

---

### Normalisasi Database

Database telah dinormalisasi hingga **Third Normal Form (3NF)** dengan karakteristik:

**1NF (First Normal Form):**
- ✅ Semua columns berisi atomic values (tidak ada multi-valued attributes)
- ✅ Setiap column berisi values dari single domain
- ✅ Setiap column name unik
- ✅ Order di mana data disimpan tidak matter

**2NF (Second Normal Form):**
- ✅ Memenuhi 1NF
- ✅ Tidak ada partial dependencies (semua non-key attributes fully dependent pada primary key)
- ✅ Pivot tables (`therapist_services`) digunakan untuk many-to-many relationships

**3NF (Third Normal Form):**
- ✅ Memenuhi 2NF
- ✅ Tidak ada transitive dependencies (non-key attributes tidak depend pada non-key attributes lain)
- ✅ Extended profiles (`therapists`, `clients`) separated dari `users` table

**Contoh Normalisasi:**

*Sebelum normalisasi (denormalized):*
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
- **Data Consistency:** Update data client/therapist/service hanya di satu tempat
- **Storage Efficiency:** Mengurangi redundansi data
- **Maintenance:** Easier to maintain dan update
- **Integrity:** Foreign key constraints ensure referential integrity

---

### Indexing Strategy

Indexes diterapkan untuk optimize query performance:

1. **Primary Keys:** Auto-indexed untuk semua tables
2. **Foreign Keys:** Indexed untuk JOIN operations yang cepat
3. **Unique Constraints:** Indexed untuk enforce uniqueness (`email`, `booking_number`, etc.)
4. **Frequently Queried Columns:** `status`, `booking_date`, `rating`, `is_verified`
5. **Composite Indexes:** Untuk queries dengan multiple WHERE conditions:
   - `(therapist_id, booking_date, time_slot)` pada `bookings` untuk conflict detection
   - `(receiver_id, is_read)` pada `messages` untuk inbox queries
   - `(client_id, assessment_date)` pada `client_progress` untuk chart generation

---

**[Lanjut ke Bagian 3: UML Diagrams - File terpisah]**
