# Database Schema - CUR-HEART

## 📊 Overview

Database CUR-HEART dirancang untuk mendukung sistem informasi manajemen pemesanan dan terapi hipnoterapi dengan 22 tabel yang ternormalisasi hingga 3NF (Third Normal Form).

## 📁 Files

### 1. `erd_dbdiagram.txt`
File DBML (Database Markup Language) untuk visualisasi ERD di [dbdiagram.io](https://dbdiagram.io)

**Cara Menggunakan:**
1. Buka https://dbdiagram.io/d
2. Klik "Import" atau buat diagram baru
3. Copy-paste isi file `erd_dbdiagram.txt`
4. Diagram ERD akan ter-generate otomatis

### 2. `schema.sql`
File SQL lengkap untuk membuat database di MySQL 8.0+

**Cara Menggunakan:**
```bash
# Login ke MySQL
mysql -u root -p

# Buat database
CREATE DATABASE curheart_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Gunakan database
USE curheart_db;

# Import schema
SOURCE schema.sql;

# Atau via command line
mysql -u root -p curheart_db < schema.sql
```

## 🗂️ Database Structure

### Total: 22 Tables

#### **Core Tables (User Management)**
1. `users` - Data pengguna universal (admin, terapis, klien)
2. `clients` - Data detail klien
3. `therapists` - Data detail terapis

#### **Service Management**
4. `services` - Katalog layanan terapi
5. `therapist_services` - Relasi terapis-layanan (many-to-many)
6. `therapist_availability` - Jadwal ketersediaan terapis
7. `therapist_unavailability` - Waktu tidak tersedia (cuti, sakit)

#### **Booking & Payment**
8. `promo_codes` - Kode promo dan diskon
9. `bookings` - Data pemesanan terapi
10. `payments` - Transaksi pembayaran
11. `sessions` - Sesi terapi yang dilaksanakan
12. `session_notes` - Catatan dokumentasi terapis
13. `reviews` - Ulasan dan rating klien

#### **Content Management**
14. `blog_categories` - Kategori artikel blog
15. `blog_posts` - Artikel blog edukasi
16. `faq_categories` - Kategori FAQ
17. `faqs` - Pertanyaan dan jawaban FAQ

#### **Communication**
18. `messages` - Chat antara klien dan terapis
19. `notifications` - Notifikasi sistem

#### **Financial Management**
20. `withdrawals` - Penarikan dana terapis

#### **System**
21. `activity_logs` - Log aktivitas untuk audit
22. `system_settings` - Konfigurasi sistem

## 🔑 Key Features

### 1. **Normalisasi 3NF**
- Eliminasi redundansi data
- Integritas referensial dengan foreign keys
- Konsistensi data melalui constraints

### 2. **Indexing Strategy**
- Primary keys pada semua tabel
- Foreign key indexes untuk JOIN optimization
- Composite indexes untuk query kompleks
- Full-text indexes untuk pencarian

### 3. **Data Types**
- `BIGINT UNSIGNED` untuk IDs (support hingga 18 quintillion records)
- `DECIMAL(10,2)` untuk nilai uang (presisi finansial)
- `ENUM` untuk status dengan nilai terbatas
- `JSON` untuk data semi-structured
- `TIMESTAMP` untuk audit trail

### 4. **Relationships**
- **One-to-One**: users ↔ clients, users ↔ therapists, bookings ↔ payments
- **One-to-Many**: therapists ↔ bookings, clients ↔ bookings
- **Many-to-Many**: therapists ↔ services (via therapist_services)

### 5. **Security**
- Password hashing (bcrypt) di aplikasi layer
- Soft delete untuk data sensitif
- Activity logs untuk audit trail
- Foreign key constraints untuk data integrity

## 📈 Database Statistics

| Metric | Value |
|--------|-------|
| Total Tables | 22 |
| Total Indexes | 60+ |
| Relationships | 35+ |
| Normalization | 3NF |
| Charset | utf8mb4 |
| Collation | utf8mb4_unicode_ci |
| Engine | InnoDB |

## 🔄 Sample Data

Schema sudah include sample data:
- 1 Admin user (email: admin@curheart.id, password: password)
- 8 System settings default

## 📝 Notes

### Naming Conventions
- **Tables**: plural, snake_case (e.g., `blog_posts`)
- **Columns**: singular, snake_case (e.g., `user_id`)
- **Foreign Keys**: `{table}_id` (e.g., `therapist_id`)
- **Timestamps**: `created_at`, `updated_at`

### Best Practices
- Selalu gunakan transactions untuk operasi multi-table
- Backup database secara regular
- Monitor slow queries dan optimize indexes
- Gunakan prepared statements untuk prevent SQL injection

## 🚀 Performance Tips

1. **Query Optimization**
   - Gunakan EXPLAIN untuk analyze queries
   - Avoid SELECT * (pilih kolom yang diperlukan)
   - Gunakan LIMIT untuk pagination

2. **Index Usage**
   - Index sudah optimal untuk query umum
   - Monitor index usage dengan `SHOW INDEX`
   - Pertimbangkan composite index untuk query kompleks

3. **Connection Pooling**
   - Gunakan connection pooling di aplikasi
   - Set max_connections sesuai kebutuhan
   - Monitor active connections

## 📞 Support

Untuk pertanyaan atau issue terkait database:
- Email: dev@curheart.id
- Documentation: `/05_laporan/04_BAB_IV_HASIL_PENELITIAN_DAN_PEMBAHASAN_REVISI_FINAL.md`
