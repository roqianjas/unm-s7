# 02 - ANALISIS

Folder ini berisi semua dokumen analisis yang dilakukan dalam tahap awal penelitian, mencakup analisis kebutuhan, stakeholder, SWOT, dan analisis sistem yang berjalan.

---

## 📁 Struktur Folder

```
02_analisis/
├── README.md                           # File ini
├── analisis_kebutuhan.md              # Analisis kebutuhan fungsional & non-fungsional
├── stakeholder_analysis.md            # Analisis stakeholder & perannya
├── swot_analysis.md                   # Analisis SWOT CUR-HEART
├── analisis_sistem_berjalan.md        # Dokumentasi sistem lama (manual)
├── analisis_masalah.md                # Identifikasi masalah bisnis
├── requirement_specification.md       # Spesifikasi kebutuhan sistem
└── user_stories.md                    # User stories untuk setiap role
```

---

## 📄 Daftar Dokumen Analisis

### 1. Analisis Kebutuhan
**File**: `analisis_kebutuhan.md`

**Konten**:

#### A. Kebutuhan Fungsional (40 fitur)
**Modul Public** (8 fitur):
1. Menampilkan landing page dengan informasi perusahaan
2. Menampilkan daftar layanan hypnotherapy
3. Menampilkan detail setiap layanan
4. Menampilkan daftar terapis dengan profil
5. Menampilkan artikel blog kesehatan mental
6. Form kontak untuk inquiry
7. FAQ untuk pertanyaan umum
8. Halaman About Us, Privacy Policy, Terms

**Modul Authentication** (6 fitur):
9. Registrasi user baru (client & therapist)
10. Login multi-role (client, therapist, admin)
11. Logout dengan session clear
12. Forgot password via email
13. Reset password dengan token
14. Email verification setelah registrasi

**Modul Client Dashboard** (10 fitur):
15. Dashboard overview (upcoming appointments, progress)
16. Browse dan search layanan terapi
17. View profil terapis dengan rating & review
18. 4-step booking process (layanan → terapis → jadwal → bayar)
19. Payment integration (Midtrans gateway)
20. Booking confirmation & email notification
21. Lihat daftar appointment (upcoming & past)
22. Reschedule atau cancel appointment
23. Progress tracking dengan chart
24. Messages/chat dengan terapis

**Modul Therapist Dashboard** (10 fitur):
25. Dashboard overview (today schedule, earnings, clients)
26. Schedule management (calendar view)
27. Set availability (working hours, days off)
28. Lihat daftar klien dengan filter
29. View client profile (medical history, session history)
30. Session room (video call placeholder)
31. Input session notes (SOAP format)
32. View session history dengan timeline
33. Earnings report dengan chart
34. Edit profil dan sertifikasi

**Modul Admin Dashboard** (6 fitur):
35. Dashboard overview (metrics, KPI, charts)
36. User management (CRUD: clients, therapists, admins)
37. Booking management (semua booking dengan status)
38. Payment verification & management
39. Financial reports (revenue, expenses, profit)
40. System settings (SMTP, payment gateway, general)

---

#### B. Kebutuhan Non-Fungsional (15 kriteria)

**Performance**:
1. Response time < 3 detik untuk halaman normal
2. Response time < 1 detik untuk AJAX request
3. Dapat menangani minimal 100 concurrent users
4. Page load speed > 90 (Google PageSpeed)

**Security**:
5. HTTPS/SSL encryption
6. Password hashing (bcrypt)
7. CSRF protection
8. SQL injection prevention
9. XSS prevention
10. Role-based access control (RBAC)

**Usability**:
11. User-friendly interface (intuitif)
12. Responsive design (desktop, tablet, mobile)
13. Accessible (WCAG 2.1 level A minimal)

**Reliability**:
14. System uptime > 99%
15. Data backup otomatis (daily)

**Penggunaan dalam Laporan**:
- BAB I: Identifikasi Masalah
- BAB IV: Requirement Specification

---

### 2. Stakeholder Analysis
**File**: `stakeholder_analysis.md`

**Konten**:

| No | Stakeholder | Role | Interest | Influence | Priority |
|----|------------|------|----------|-----------|----------|
| 1 | Dr. Sarah Wellness | Owner | High - Pertumbuhan bisnis, ROI | High - Decision maker | High |
| 2 | Michael Ananda, CHt | Head Therapist | High - Efisiensi kerja, tools | Medium - Technical advisor | High |
| 3 | Rina Kusuma | Admin/CS | High - Kemudahan operasional | Medium - Daily user | High |
| 4 | 8 Terapis | Therapist | High - Kemudahan manage klien | Low - End user | Medium |
| 5 | 120+ Klien Aktif | Client | High - Kemudahan booking | Low - End user | High |
| 6 | Tim Proyek UNM | Developer | High - Pembelajaran, portfolio | High - System builder | High |
| 7 | Dosen Pembimbing | Academic Advisor | Medium - Kualitas proyek | Medium - Evaluator | Medium |

**Analisis Power-Interest Grid**:
- **High Power, High Interest**: Owner, Admin → Manage Closely
- **High Power, Low Interest**: - (none)
- **Low Power, High Interest**: Therapist, Client → Keep Informed
- **Low Power, Low Interest**: - (none)

**Penggunaan dalam Laporan**:
- BAB IV: Inisiasi Proyek (Stakeholder Analysis)

---

### 3. SWOT Analysis
**File**: `swot_analysis.md`

**Konten**:

#### Strengths (Kekuatan)
1. Terapis bersertifikat dan berpengalaman (8 terapis)
2. Lokasi strategis di Jakarta Selatan
3. Layanan komprehensif (6 jenis terapi)
4. Reputasi baik di komunitas
5. Basis klien loyal (120+ klien aktif)

#### Weaknesses (Kelemahan)
1. **Sistem booking manual** (via WhatsApp/telepon)
2. **Tidak ada database klien terpusat**
3. **Laporan keuangan manual** (Excel)
4. **Sering terjadi double booking**
5. **Follow-up klien tidak sistematis**
6. **Tidak ada sistem pembayaran digital**
7. **Dokumentasi sesi tidak terorganisir**

#### Opportunities (Peluang)
1. Meningkatnya awareness kesehatan mental di Indonesia
2. Tren terapi alternatif yang berkembang
3. Teknologi digital untuk healthcare
4. Market hypnotherapy yang masih terbatas kompetitor
5. Potensi ekspansi layanan (online therapy)

#### Threats (Ancaman)
1. Kompetitor dengan sistem digital lebih baik
2. Regulasi kesehatan yang ketat
3. Stigma negatif tentang hypnotherapy
4. Biaya terapi dianggap mahal oleh sebagian target market

**Penggunaan dalam Laporan**:
- BAB I: Latar Belakang (gap analysis)
- BAB IV: Inisiasi Proyek (justifikasi proyek)

---

### 4. Analisis Sistem Berjalan
**File**: `analisis_sistem_berjalan.md`

**Konten**:

#### Proses Bisnis Saat Ini (Manual):

**1. Proses Booking**:
```
Client → WhatsApp/Call Admin → Admin cek jadwal terapis manual →
Admin konfirmasi ke client → Client datang & bayar cash/transfer manual →
Admin input ke Excel → Admin buat reminder manual
```
**Waktu**: 15-20 menit per booking  
**Masalah**: 
- Double booking sering terjadi
- Admin overwhelmed (1 orang handle 120+ klien)
- Tidak ada reminder otomatis

**2. Proses Sesi Terapi**:
```
Terapis cek jadwal di grup WhatsApp → Client datang →
Terapis lakukan terapi → Terapis tulis notes di buku →
Terapis report ke admin via WhatsApp
```
**Waktu**: 60-90 menit per sesi (+ 10 menit dokumentasi)  
**Masalah**:
- Notes manual sulit dicari
- Tidak ada tracking progress klien
- Data tersebar

**3. Proses Pembayaran**:
```
Client bayar cash/transfer manual → Admin terima →
Admin input ke Excel → Admin buat invoice manual di Word →
Admin print & kasih ke client
```
**Waktu**: 5-10 menit per transaksi  
**Masalah**:
- Rekonsiliasi lama (2 jam/hari)
- Tidak ada payment gateway
- Tidak ada receipt otomatis

**4. Laporan Keuangan**:
```
Admin kumpulkan data dari Excel → Admin hitung manual →
Admin buat report di Excel → Admin print untuk owner
```
**Waktu**: 4-5 jam untuk laporan mingguan  
**Masalah**:
- Tidak real-time
- Rawan human error
- Tidak ada dashboard

**Penggunaan dalam Laporan**:
- BAB I: Latar Belakang (kondisi existing)
- BAB IV: Analisis Sistem Berjalan

---

### 5. Analisis Masalah
**File**: `analisis_masalah.md`

**Konten**:

#### 7 Masalah Utama yang Diidentifikasi:

1. **Proses Booking Manual & Tidak Efisien**
   - Impact: Waktu lama, double booking, client frustasi
   - Root Cause: Tidak ada sistem booking online
   - Solution: Sistem booking online 24/7

2. **Tidak Ada Database Klien Terpusat**
   - Impact: Data tersebar, sulit tracking, tidak aman
   - Root Cause: Masih pakai Excel terpisah-pisah
   - Solution: Database MySQL dengan backup otomatis

3. **Dokumentasi Sesi Tidak Terorganisir**
   - Impact: Sulit mencari riwayat, tidak ada tracking progress
   - Root Cause: Catatan manual di buku fisik
   - Solution: Session notes digital dengan search & filter

4. **Tidak Ada Sistem Pembayaran Digital**
   - Impact: Rekonsiliasi lama, tidak convenient untuk klien
   - Root Cause: Masih cash/transfer manual
   - Solution: Payment gateway terintegrasi (Midtrans)

5. **Laporan Keuangan Manual & Lambat**
   - Impact: Decision making lambat, tidak real-time insight
   - Root Cause: Laporan dibuat manual setiap minggu
   - Solution: Dashboard real-time dengan auto-report

6. **Komunikasi Tidak Efektif**
   - Impact: Follow-up terlewat, reminder manual
   - Root Cause: Grup WhatsApp yang kacau
   - Solution: Built-in messaging & notification system

7. **Tidak Ada Self-Service untuk Client**
   - Impact: Client harus selalu via admin, admin overwhelmed
   - Root Cause: Tidak ada portal client
   - Solution: Client dashboard untuk manage sendiri

**Penggunaan dalam Laporan**:
- BAB I: Identifikasi Masalah (lengkap)
- BAB IV: Problem Statement

---

### 6. Requirement Specification
**File**: `requirement_specification.md`

**Konten**:

#### Spesifikasi Kebutuhan Lengkap

**FR-001: User Registration**
- Actor: Client, Therapist
- Description: User dapat registrasi dengan email, password, nama lengkap, nomor HP
- Input: Form registrasi
- Process: Validasi, hash password, simpan ke database, kirim email verifikasi
- Output: Akun baru, email verifikasi
- Priority: High
- Status: Implemented

*(... 40 functional requirements lengkap)*

**NFR-001: Response Time**
- Description: System harus merespon dalam < 3 detik
- Metric: Average response time
- Target: < 3 seconds
- Priority: High
- Status: Achieved (avg 245ms)

*(... 15 non-functional requirements lengkap)*

**Penggunaan dalam Laporan**:
- BAB IV: Requirement Specification (tabel lengkap)

---

### 7. User Stories
**File**: `user_stories.md`

**Konten**:

#### User Stories untuk Setiap Role

**Client Stories** (30 stories):
1. As a **client**, I want to **view available services**, so that **I can choose therapy yang sesuai**
2. As a **client**, I want to **book a therapy session online**, so that **I don't have to call admin**
3. As a **client**, I want to **pay online securely**, so that **booking process lebih convenient**

*(... 27 more client stories)*

**Therapist Stories** (25 stories):
1. As a **therapist**, I want to **set my availability**, so that **clients can book when I'm free**
2. As a **therapist**, I want to **view my schedule**, so that **I know my appointments**
3. As a **therapist**, I want to **input session notes**, so that **I can track client progress**

*(... 22 more therapist stories)*

**Admin Stories** (20 stories):
1. As an **admin**, I want to **view all bookings**, so that **I can monitor operations**
2. As an **admin**, I want to **manage users**, so that **I can add/remove accounts**
3. As an **admin**, I want to **generate financial reports**, so that **I can analyze revenue**

*(... 17 more admin stories)*

**Total**: 85 user stories

**Penggunaan dalam Laporan**:
- BAB IV: User Requirements (dalam bentuk use case)

---

## 📊 Hasil Analisis (Summary)

### Kesimpulan Analisis:

1. ✅ **40 Kebutuhan Fungsional** telah diidentifikasi dan lengkap
2. ✅ **15 Kebutuhan Non-Fungsional** telah ditetapkan dengan target jelas
3. ✅ **7 Stakeholder Utama** dengan interest dan influence yang berbeda
4. ✅ **7 Masalah Utama** yang harus diselesaikan dengan sistem baru
5. ✅ **SWOT Analysis** menunjukkan kebutuhan urgent untuk digitalisasi
6. ✅ **Sistem Berjalan** sangat manual dan tidak efisien
7. ✅ **85 User Stories** untuk guide development

**Rekomendasi**: 
Develop sistem informasi berbasis web dengan Laravel untuk mengatasi semua masalah yang teridentifikasi.

---

## 🔗 Integrasi dengan BAB Laporan

**BAB I - Pendahuluan**:
- 1.1 Latar Belakang → Gunakan: SWOT Analysis, Analisis Sistem Berjalan
- 1.2 Identifikasi Masalah → Gunakan: Analisis Masalah (7 masalah utama)
- 1.3 Ruang Lingkup → Gunakan: Requirement Specification

**BAB IV - Hasil Penelitian**:
- 4.1 Inisiasi Proyek → Gunakan: Stakeholder Analysis, Analisis Masalah
- 4.2 Perencanaan Proyek → Gunakan: Requirement Specification
- 4.3 Deskripsi Produk → Gunakan: Analisis Kebutuhan

---

## ✅ Checklist Kelengkapan Analisis

- [x] Analisis kebutuhan fungsional (40 fitur)
- [x] Analisis kebutuhan non-fungsional (15 kriteria)
- [x] Stakeholder analysis dengan Power-Interest Grid
- [x] SWOT analysis lengkap
- [x] Analisis sistem berjalan (proses bisnis manual)
- [x] Identifikasi 7 masalah utama dengan root cause
- [x] Requirement specification (FR & NFR)
- [x] User stories untuk 3 role (85 stories)

---

**Metode Analisis yang Digunakan**:
1. Wawancara dengan stakeholder (3 sesi)
2. Observasi lapangan (3 sesi, 10 jam)
3. Studi dokumen (SOP, data operasional)
4. Survey/kuesioner (36 responden)

**Tools yang Digunakan**:
- Google Forms (survey)
- Microsoft Excel (tabulasi data)
- Draw.io (diagram)
- Notion/Google Docs (dokumentasi)

---

**Last Updated**: 1 November 2024  
**Prepared by**: Tim Proyek CUR-HEART
