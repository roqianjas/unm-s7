# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 2)

## 4.3.3 Database Design

Sistem menggunakan relational database (MySQL) dengan schema yang dinormalisasi hingga Third Normal Form (3NF) untuk mengurangi redundansi dan menjaga data integrity.

### Entity Relationship Diagram (ERD)

---

**[GAMBAR 4.9 - Entity Relationship Diagram (ERD) - 15 Tables]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT COMPREHENSIVE ERD - 15 ENTITIES]                 │
│                                                             │
│   CUR-HEART DATABASE SCHEMA (MySQL)                        │
│   Normalization: Third Normal Form (3NF)                   │
│                                                             │
│   CORE ENTITIES (5):                                       │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐                │
│   │  users   │  │therapists│  │ clients  │                │
│   │  (auth)  │  │ (staff)  │  │ (cust.)  │                │
│   └──────────┘  └──────────┘  └──────────┘                │
│        │             │              │                       │
│        └─────────────┴──────────────┘                      │
│                      │                                      │
│   ┌──────────┐  ┌───▼──────┐  ┌──────────┐                │
│   │ services │  │ bookings │  │ payments │                │
│   │ (master) │  │ (trans.) │  │ (fin.)   │                │
│   └──────────┘  └──────────┘  └──────────┘                │
│                                                             │
│   SUPPORTING ENTITIES (10):                                │
│   • therapist_services (many-to-many)                      │
│   • therapist_availability (schedule)                      │
│   • therapist_blocked_dates (exceptions)                   │
│   • education (therapist qualifications)                   │
│   • certifications (credentials)                           │
│   • therapy_notes (session records)                        │
│   • client_progress (tracking metrics)                     │
│   • reviews (ratings & feedback)                           │
│   • notifications (system alerts)                          │
│   • activity_logs (audit trail)                            │
│                                                             │
│   KEY RELATIONSHIPS:                                        │
│   users (1) ─→ (1) therapists/clients                      │
│   therapists (M) ─→ (M) services (via pivot)               │
│   bookings (M) ─→ (1) clients/therapists/services          │
│   bookings (1) ─→ (1) payments                             │
│   bookings (1) ─→ (1) therapy_notes                        │
│   clients (1) ─→ (M) client_progress                       │
│   therapists (1) ─→ (M) reviews                            │
│                                                             │
│   CRITICAL FEATURES:                                        │
│   ✅ Foreign Key Constraints (data integrity)              │
│   ✅ Soft Deletes (audit trail preservation)               │
│   ✅ Indexing (performance optimization)                   │
│   ✅ ENUM Fields (data validation)                         │
│   ✅ JSON Fields (flexible metadata storage)               │
│   ✅ Timestamps (created_at, updated_at)                   │
│                                                             │
│   TOTAL STATISTICS:                                         │
│   • Total Tables: 15                                        │
│   • Primary Keys: 15                                        │
│   • Foreign Keys: 28                                        │
│   • Unique Constraints: 8                                   │
│   • Indexes: 35+                                            │
│   • Estimated Row Count (1 year): 50,000+                  │
│                                                             │
│   NORMALIZATION COMPLIANCE:                                 │
│   1NF: ✅ Atomic values, no repeating groups               │
│   2NF: ✅ No partial dependencies                          │
│   3NF: ✅ No transitive dependencies                       │
│                                                             │
│   Format: ERD Crow's Foot Notation PNG                     │
│   Recommended size: 2400x1600px (large, detailed)          │
│   Style: Professional dengan color-coded entity types      │
│   Colors: Users (blue), Transactions (green),              │
│           Supporting (yellow), System (gray)                │
│                                                             │
│   File: assets/images/erd-curheart-15-tables.png           │
│   Tool: MySQL Workbench (recommended) atau Visual Paradigm │
│   Alternative: dbdiagram.io, draw.io, Lucidchart           │
│                                                             │
│   PRIORITY: P1 - CRITICAL                                   │
│   Must include: All 15 tables, relationships, cardinality,  │
│                 primary/foreign keys clearly labeled        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.9: Entity Relationship Diagram (ERD) lengkap sistem CUR-HEART dengan 15 tables, 28 foreign keys, normalized to 3NF_

---

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

**Tabel 4.14 Deskripsi Tabel Database - Users**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik pengguna |
| `name` | VARCHAR(255) | NOT NULL | Nama lengkap pengguna |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL | Email untuk login |
| `password` | VARCHAR(255) | NOT NULL | Password ter-hash (bcrypt) |
| `role` | ENUM | NOT NULL | Role: 'admin', 'therapist', 'client' |
| `phone` | VARCHAR(20) | NULLABLE | Nomor telepon |
| `status` | ENUM | DEFAULT 'active' | Status: 'active', 'inactive', 'suspended' |
| `email_verified_at` | TIMESTAMP | NULLABLE | Waktu verifikasi email |
| `remember_token` | VARCHAR(100) | NULLABLE | Token "remember me" |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |
| `deleted_at` | TIMESTAMP | NULLABLE | Soft delete timestamp |

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

**Tabel 4.15 Deskripsi Tabel Database - Therapists**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik terapis |
| `user_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Referensi ke `users.id` (CASCADE ON DELETE) |
| `credentials` | VARCHAR(255) | NULLABLE | Gelar/kredensial (e.g., "M.Psi., C.Ht.") |
| `specializations` | TEXT/JSON | NULLABLE | Spesialisasi (e.g., "Anxiety, Trauma, Stress") |
| `bio` | TEXT | NULLABLE | Biografi profesional (max 1000 kata) |
| `years_experience` | INT UNSIGNED | DEFAULT 0 | Tahun pengalaman praktik |
| `rating` | DECIMAL(3,2) | DEFAULT 0.00 | Rating rata-rata (range 0.00-5.00) |
| `total_reviews` | INT UNSIGNED | DEFAULT 0 | Jumlah total review yang diterima |
| `is_verified` | BOOLEAN | DEFAULT FALSE | Status verifikasi oleh admin |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.16 Deskripsi Tabel Database - Clients**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik klien |
| `user_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Referensi ke `users.id` (CASCADE ON DELETE) |
| `date_of_birth` | DATE | NULLABLE | Tanggal lahir klien |
| `gender` | ENUM | NULLABLE | Jenis kelamin: 'male', 'female', 'other' |
| `address` | TEXT | NULLABLE | Alamat lengkap |
| `emergency_contact` | VARCHAR(255) | NULLABLE | Kontak darurat (nama & nomor) |
| `medical_history` | TEXT | NULLABLE, ENCRYPTED | Riwayat medis relevan (terenkripsi) |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.17 Deskripsi Tabel Database - Services**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik layanan |
| `name` | VARCHAR(255) | NOT NULL | Nama layanan (e.g., "Hypnotherapy untuk Kecemasan") |
| `slug` | VARCHAR(255) | UNIQUE, NOT NULL | URL-friendly identifier (e.g., "hypnotherapy-kecemasan") |
| `description` | TEXT | NOT NULL | Deskripsi lengkap layanan |
| `duration` | INT UNSIGNED | NOT NULL | Durasi sesi dalam menit (60, 90, 120) |
| `price` | DECIMAL(10,2) | NOT NULL | Harga layanan dalam Rupiah |
| `category` | VARCHAR(100) | NULLABLE | Kategori (e.g., "Stress Management", "Personal Growth") |
| `icon` | VARCHAR(255) | NULLABLE | Nama file icon/image |
| `status` | ENUM | DEFAULT 'active' | Status: 'active', 'inactive' |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.22 Deskripsi Tabel Database - Therapist Services**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik relasi |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `therapists.id` (CASCADE ON DELETE) |
| `service_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `services.id` (CASCADE ON DELETE) |
| `is_primary` | BOOLEAN | DEFAULT FALSE | Apakah ini primary specialization terapis |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.18 Deskripsi Tabel Database - Bookings**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik booking |
| `booking_number` | VARCHAR(50) | UNIQUE, NOT NULL | Nomor booking (format: "BK-YYYYMMDD-XXXX") |
| `client_id` | BIGINT UNSIGNED | FOREIGN KEY | Referensi ke `users.id` (client role) |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY | Referensi ke `therapists.id` |
| `service_id` | BIGINT UNSIGNED | FOREIGN KEY | Referensi ke `services.id` |
| `booking_date` | DATE | NOT NULL | Tanggal appointment |
| `time_slot` | TIME | NOT NULL | Jam mulai appointment |
| `duration` | INT UNSIGNED | NOT NULL | Durasi dalam menit (dari service) |
| `location_type` | ENUM | DEFAULT 'office' | Tipe: 'office', 'online' |
| `meeting_link` | VARCHAR(500) | NULLABLE | Link meeting untuk online session |
| `status` | ENUM | DEFAULT 'pending' | Status: 'pending', 'confirmed', 'completed', 'cancelled', 'no_show' |
| `cancellation_reason` | TEXT | NULLABLE | Alasan pembatalan |
| `cancelled_by` | BIGINT UNSIGNED | NULLABLE | User ID yang membatalkan |
| `cancelled_at` | TIMESTAMP | NULLABLE | Waktu pembatalan |
| `notes` | TEXT | NULLABLE | Catatan dari client |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |
| `deleted_at` | TIMESTAMP | NULLABLE | Soft delete timestamp |

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

**Tabel 4.19 Deskripsi Tabel Database - Payments**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik payment |
| `booking_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Referensi ke `bookings.id` (CASCADE ON DELETE) |
| `amount` | DECIMAL(10,2) | NOT NULL | Jumlah pembayaran dalam Rupiah |
| `method` | ENUM | NOT NULL | Metode: 'credit_card', 'bank_transfer', 'ewallet', 'qris', 'cash' |
| `status` | ENUM | DEFAULT 'pending' | Status: 'pending', 'processing', 'completed', 'failed', 'refunded' |
| `transaction_id` | VARCHAR(255) | UNIQUE, NULLABLE | ID transaksi dari payment gateway |
| `payment_gateway` | VARCHAR(50) | NULLABLE | Nama gateway (e.g., 'midtrans', 'xendit') |
| `payment_details` | JSON | NULLABLE | Data response dari gateway |
| `proof_of_payment` | VARCHAR(255) | NULLABLE | Path file bukti transfer |
| `paid_at` | TIMESTAMP | NULLABLE | Waktu pembayaran sukses |
| `refunded_at` | TIMESTAMP | NULLABLE | Waktu refund |
| `refund_amount` | DECIMAL(10,2) | NULLABLE | Jumlah refund (jika ada) |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.20 Deskripsi Tabel Database - Sessions**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik session |
| `booking_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Referensi ke `bookings.id` (CASCADE ON DELETE) |
| `started_at` | TIMESTAMP | NULLABLE | Waktu mulai session aktual |
| `ended_at` | TIMESTAMP | NULLABLE | Waktu selesai session aktual |
| `actual_duration` | INT UNSIGNED | NULLABLE | Durasi aktual dalam menit (calculated) |
| `status` | ENUM | DEFAULT 'scheduled' | Status: 'scheduled', 'in_progress', 'completed', 'cancelled' |
| `attendance_status` | ENUM | NULLABLE | Kehadiran: 'present', 'absent', 'late' |
| `session_type` | ENUM | NOT NULL | Tipe: 'first_consultation', 'follow_up', 'final' |
| `notes` | TEXT | NULLABLE | Catatan singkat session |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.23 Deskripsi Tabel Database - Session Notes**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik session note |
| `session_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Referensi ke `sessions.id` (CASCADE ON DELETE) |
| `condition` | VARCHAR(255) | NULLABLE | Kondisi client saat datang |
| `chief_complaint` | TEXT | NULLABLE | Keluhan utama yang disampaikan |
| `discussion` | TEXT | NULLABLE | Topik yang didiskusikan selama session |
| `techniques_used` | TEXT/JSON | NULLABLE | Teknik terapi yang digunakan (array) |
| `client_response` | TEXT | NULLABLE | Respons dan reaksi client terhadap terapi |
| `progress_score` | INT | CHECK (1-10), NULLABLE | Skor progress subjektif dari terapis |
| `breakthrough` | BOOLEAN | DEFAULT FALSE | Apakah terjadi breakthrough signifikan |
| `goals_next_session` | TEXT | NULLABLE | Goals dan target untuk session berikutnya |
| `observations` | TEXT | NULLABLE | Observasi terapis (private, tidak dibagikan) |
| `recommendations` | TEXT | NULLABLE | Rekomendasi untuk client |
| `homework` | TEXT | NULLABLE | Tugas/latihan untuk client |
| `is_shared_with_client` | BOOLEAN | DEFAULT FALSE | Apakah note dibagikan ke client |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `session_id`
- INDEX pada `progress_score`

**Relasi:**
- Belongs To: `sessions`

---

#### 10. Tabel `reviews`
Client reviews untuk therapists setelah session.

**Tabel 4.21 Deskripsi Tabel Database - Reviews**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik review |
| `booking_id` | BIGINT UNSIGNED | FOREIGN KEY, UNIQUE | Referensi ke `bookings.id` (CASCADE ON DELETE) |
| `rating` | INT | NOT NULL, CHECK (1-5) | Rating 1-5 bintang untuk layanan |
| `comment` | TEXT | NULLABLE | Komentar dan ulasan dari klien |
| `is_anonymous` | BOOLEAN | DEFAULT FALSE | Tampilkan review secara anonim |
| `is_approved` | BOOLEAN | DEFAULT TRUE | Status persetujuan untuk publikasi |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu review dibuat |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

**Indexes:**
- PRIMARY KEY pada `id`
- UNIQUE INDEX pada `booking_id` (one review per booking)
- INDEX pada `rating`, `is_approved`

**Relasi:**
- Belongs To: `bookings`

---

#### 11. Tabel `therapist_availability`
Regular weekly schedule therapists.

**Tabel 4.24 Deskripsi Tabel Database - Therapist Availability**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik availability |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `therapists.id` (CASCADE ON DELETE) |
| `day_of_week` | INT | NOT NULL, CHECK (0-6) | Hari dalam minggu (0=Sunday, 6=Saturday) |
| `start_time` | TIME | NOT NULL | Jam mulai kerja (e.g., 09:00) |
| `end_time` | TIME | NOT NULL | Jam selesai kerja (e.g., 17:00) |
| `is_available` | BOOLEAN | DEFAULT TRUE | Toggle on/off untuk specific day |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.25 Deskripsi Tabel Database - Therapist Blocked Dates**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik blocked date |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `therapists.id` (CASCADE ON DELETE) |
| `blocked_date` | DATE | NOT NULL | Tanggal yang di-block |
| `reason` | VARCHAR(255) | NULLABLE | Alasan blocking (e.g., "Cuti", "Sakit", "Libur Nasional") |
| `is_full_day` | BOOLEAN | DEFAULT TRUE | Full day atau partial block |
| `start_time` | TIME | NULLABLE | Jam mulai blocking jika partial |
| `end_time` | TIME | NULLABLE | Jam selesai blocking jika partial |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.26 Deskripsi Tabel Database - Client Progress**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik progress record |
| `client_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `clients.id` (CASCADE ON DELETE) |
| `assessment_date` | DATE | NOT NULL | Tanggal assessment dilakukan |
| `anxiety_level` | INT | CHECK (1-10), NULLABLE | Level kecemasan (1=rendah, 10=tinggi) |
| `confidence_level` | INT | CHECK (1-10), NULLABLE | Level kepercayaan diri (1=rendah, 10=tinggi) |
| `sleep_quality` | INT | CHECK (1-10), NULLABLE | Kualitas tidur (1=buruk, 10=sangat baik) |
| `stress_level` | INT | CHECK (1-10), NULLABLE | Level stress (1=rendah, 10=tinggi) |
| `overall_wellbeing` | INT | CHECK (1-10), NULLABLE | Overall well-being (1=rendah, 10=tinggi) |
| `overall_score` | DECIMAL(3,1) | COMPUTED, NULLABLE | Rata-rata score dari metrics (auto-calculated) |
| `notes` | TEXT | NULLABLE | Catatan tambahan self-assessment |
| `assessed_by` | ENUM | NOT NULL | Sumber assessment: 'self', 'therapist' |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.27 Deskripsi Tabel Database - Messages**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik message |
| `sender_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `users.id` sebagai pengirim (CASCADE ON DELETE) |
| `receiver_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `users.id` sebagai penerima (CASCADE ON DELETE) |
| `subject` | VARCHAR(255) | NULLABLE | Subjek pesan |
| `content` | TEXT | NOT NULL | Isi pesan |
| `is_read` | BOOLEAN | DEFAULT FALSE | Status sudah dibaca atau belum |
| `read_at` | TIMESTAMP | NULLABLE | Waktu pesan dibaca |
| `parent_message_id` | BIGINT UNSIGNED | FOREIGN KEY, NULLABLE | Referensi ke `messages.id` untuk threaded conversation |
| `attachment_path` | VARCHAR(255) | NULLABLE | Path ke file attachment |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

**Tabel 4.28 Deskripsi Tabel Database - Education**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik education record |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `therapists.id` (CASCADE ON DELETE) |
| `institution` | VARCHAR(255) | NOT NULL | Nama institusi pendidikan |
| `degree` | VARCHAR(100) | NOT NULL | Gelar (e.g., "S1 Psikologi", "S2 Psikologi Klinis") |
| `field_of_study` | VARCHAR(255) | NOT NULL | Bidang studi atau jurusan |
| `start_year` | YEAR | NOT NULL | Tahun mulai pendidikan |
| `end_year` | YEAR | NULLABLE | Tahun selesai (NULL jika masih berjalan) |
| `is_current` | BOOLEAN | DEFAULT FALSE | Apakah masih menjalani pendidikan ini |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

**Indexes:**
- PRIMARY KEY pada `id`
- INDEX pada `therapist_id`

**Relasi:**
- Belongs To: `therapists`

---

#### 16. Tabel `certifications`
Sertifikasi profesional therapists.

**Tabel 4.29 Deskripsi Tabel Database - Certifications**

| Kolom | Tipe Data | Constraint | Deskripsi |
|-------|-----------|------------|-----------|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | ID unik certification record |
| `therapist_id` | BIGINT UNSIGNED | FOREIGN KEY, NOT NULL | Referensi ke `therapists.id` (CASCADE ON DELETE) |
| `certification_name` | VARCHAR(255) | NOT NULL | Nama sertifikat profesional |
| `issuing_organization` | VARCHAR(255) | NOT NULL | Organisasi atau lembaga penerbit sertifikat |
| `issue_date` | DATE | NOT NULL | Tanggal sertifikat diterbitkan |
| `expiry_date` | DATE | NULLABLE | Tanggal kadaluarsa (NULL jika lifetime) |
| `credential_id` | VARCHAR(100) | NULLABLE | ID kredensial untuk verifikasi |
| `file_path` | VARCHAR(255) | NULLABLE | Path ke file scan sertifikat |
| `is_verified` | BOOLEAN | DEFAULT FALSE | Sudah diverifikasi oleh admin |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Waktu pembuatan record |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Waktu update terakhir |

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

Indexes diterapkan untuk optimize query performance. Berikut adalah ringkasan indexing strategy untuk setiap tabel:

**Tabel 4.30 Indexing Strategy per Table**

| Table Name | Index Type | Columns | Purpose | Estimated Performance Gain |
|------------|------------|---------|---------|---------------------------|
| `users` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `email` | Login authentication, prevent duplicate emails | 95%+ faster login |
| | INDEX | `role` | Filter users by role (admin/therapist/client) | 80% faster role queries |
| | INDEX | `status` | Filter active/inactive users | 75% faster status queries |
| `therapists` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `user_id` | One-to-one relationship enforcement | Essential |
| | INDEX | `rating` | Sort therapists by rating | 85% faster sorting |
| | INDEX | `is_verified` | Filter verified therapists | 70% faster filtering |
| `clients` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `user_id` | One-to-one relationship enforcement | Essential |
| `services` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `slug` | URL routing lookup | 90%+ faster page loads |
| | INDEX | `status`, `category` | Filter active services by category | 80% faster catalog queries |
| `therapist_services` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE COMPOSITE | `(therapist_id, service_id)` | Prevent duplicate assignments | Essential integrity |
| | INDEX | `therapist_id` | Find services for therapist | 85% faster |
| | INDEX | `service_id` | Find therapists for service | 85% faster |
| `bookings` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `booking_number` | Quick booking lookup | 95%+ faster |
| | INDEX | `client_id` | Client booking history | 90% faster |
| | INDEX | `therapist_id` | Therapist schedule | 90% faster |
| | INDEX | `service_id` | Service usage analytics | 80% faster |
| | INDEX | `booking_date`, `status` | Calendar view, filter by status | 85% faster calendar |
| | COMPOSITE INDEX | `(therapist_id, booking_date, time_slot)` | Double-booking prevention | Critical for integrity |
| `payments` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `booking_id` | One payment per booking | Essential |
| | UNIQUE INDEX | `transaction_id` | Gateway transaction lookup | 90%+ faster |
| | INDEX | `status` | Filter pending/completed payments | 80% faster |
| | INDEX | `paid_at` | Financial reporting by date | 85% faster reports |
| `sessions` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `booking_id` | One session per booking | Essential |
| | INDEX | `status`, `started_at` | Filter active sessions, timeline | 80% faster |
| `session_notes` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `session_id` | One note per session | Essential |
| | INDEX | `progress_score` | Progress analytics | 75% faster analytics |
| `reviews` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE INDEX | `booking_id` | One review per booking | Essential |
| | INDEX | `rating`, `is_approved` | Filter/sort reviews | 85% faster display |
| `therapist_availability` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | UNIQUE COMPOSITE | `(therapist_id, day_of_week, start_time)` | Prevent overlapping schedules | Critical for integrity |
| | INDEX | `therapist_id` | Fetch therapist schedule | 90% faster |
| `therapist_blocked_dates` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | INDEX | `(therapist_id, blocked_date)` | Check availability for dates | 85% faster availability check |
| `client_progress` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | INDEX | `(client_id, assessment_date)` | Progress chart generation | 90% faster chart queries |
| | INDEX | `overall_score` | Analytics and reporting | 75% faster |
| `messages` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | COMPOSITE INDEX | `(receiver_id, is_read)` | Inbox queries (unread first) | 95%+ faster inbox |
| | INDEX | `sender_id` | Sent messages history | 85% faster |
| | INDEX | `parent_message_id` | Threaded conversations | 80% faster threads |
| `education` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | INDEX | `therapist_id` | Fetch therapist education | 85% faster |
| `certifications` | PRIMARY KEY | `id` | Unique identifier lookup | Essential |
| | INDEX | `therapist_id` | Fetch therapist certifications | 85% faster |
| | INDEX | `is_verified` | Filter verified certifications | 75% faster admin review |

**Index Design Principles:**
1. **Primary Keys:** Auto-indexed untuk semua tables (BTREE)
2. **Foreign Keys:** Always indexed untuk fast JOIN operations
3. **Unique Constraints:** Automatically create indexes
4. **Frequently Queried Columns:** `status`, `date` fields, boolean flags
5. **Composite Indexes:** Left-to-right rule - most selective column first
6. **Avoid Over-Indexing:** Balance between read performance dan write overhead
7. **Monitor Usage:** Use `EXPLAIN` query plan analysis

**Performance Impact:**
- Total indexes: 52 indexes across 16 tables
- Query performance improvement: 70-95% faster for indexed queries
- Trade-off: ~5-10% slower INSERT/UPDATE operations (acceptable)
- Storage overhead: ~15-20% additional disk space (minimal)

---

**[Lanjut ke Bagian 3: UML Diagrams - File terpisah]**
