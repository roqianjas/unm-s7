# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 3)

## 4.3.4 UML Diagrams (Unified Modeling Language)

UML (Unified Modeling Language) adalah bahasa pemodelan standar yang digunakan untuk memvisualisasikan, menspesifikasikan, membangun, dan mendokumentasikan sistem perangkat lunak. Dalam proyek CUR-HEART, kami menggunakan tiga jenis diagram UML utama untuk menggambarkan struktur dan perilaku sistem.

### A. Use Case Diagram

Use Case Diagram menggambarkan interaksi antara aktor (pengguna sistem) dengan sistem, serta fungsi-fungsi yang dapat dilakukan oleh masing-masing aktor.

---

**[GAMBAR 4.10 - Use Case Diagram (4 Actors, 30+ Use Cases)]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT COMPREHENSIVE USE CASE DIAGRAM]                  │
│                                                             │
│   CUR-HEART SYSTEM USE CASE DIAGRAM                        │
│   UML Standard Notation                                    │
│                                                             │
│   ACTORS (4 Primary + 1 External):                         │
│                                                             │
│   🚶 Guest (Visitor)                                        │
│   • View landing page / services                           │
│   • View therapist profiles                                │
│   • Register account                                       │
│   • Login to system                                        │
│                                                             │
│   👤 Client (Customer)                                      │
│   • ALL Guest capabilities +                               │
│   • Make booking (includes: select service, therapist,     │
│     schedule, payment)                                     │
│   • View appointments                                      │
│   • Reschedule/Cancel booking                              │
│   • View progress tracker                                  │
│   • Send messages (chat therapist)                         │
│   • Submit reviews                                         │
│   • Manage profile                                         │
│                                                             │
│   👨‍⚕️ Therapist (Staff)                                    │
│   • View therapist dashboard                               │
│   • Manage work schedule (availability)                    │
│   • Block/Unblock dates                                    │
│   • View appointments                                      │
│   • Complete session (write therapy notes)                 │
│   • Update client progress                                 │
│   • Respond to messages                                    │
│   • View reviews/ratings                                   │
│   • Manage profile & credentials                           │
│                                                             │
│   👔 Admin (Administrator)                                  │
│   • View admin dashboard                                   │
│   • Manage users (CRUD all roles)                          │
│   • Manage therapists (approve/suspend)                    │
│   • Manage services (CRUD)                                 │
│   • Manage bookings (view, modify, cancel)                 │
│   • View financial reports                                 │
│   • Manage system settings                                 │
│   • View activity logs                                     │
│   • Send notifications                                     │
│                                                             │
│   💳 Payment Gateway (External System)                      │
│   • Process payment                                        │
│   • Send payment confirmation                              │
│   • Handle refunds                                         │
│                                                             │
│   KEY RELATIONSHIPS:                                        │
│   • <<include>>: Mandatory sub-use case                    │
│     (e.g., Make Booking includes Select Service)           │
│   • <<extend>>: Optional use case                          │
│     (e.g., Cancel Booking extends View Appointments)       │
│   • Generalization: Inheritance                            │
│     (e.g., Client inherits Guest capabilities)             │
│                                                             │
│   TOTAL USE CASES: 35+                                     │
│   • Guest: 6 use cases                                     │
│   • Client: 14 use cases (includes Guest)                  │
│   • Therapist: 12 use cases                                │
│   • Admin: 15 use cases                                    │
│   • Payment Gateway: 3 interactions                        │
│                                                             │
│   CRITICAL FLOWS:                                           │
│   1. Booking Flow (Client → System → Payment Gateway)      │
│   2. Session Completion (Therapist → Therapy Notes)        │
│   3. User Management (Admin → CRUD operations)             │
│                                                             │
│   Format: UML Use Case Diagram PNG                         │
│   Recommended size: 2000x1400px (large, readable)          │
│   Style: Standard UML notation dengan stick figures        │
│   Colors: Actors (outside), System boundary (box),         │
│           Use cases (ovals inside system)                   │
│                                                             │
│   File: assets/images/use-case-diagram-complete.png        │
│   Tool: Visual Paradigm, draw.io, StarUML, atau Lucidchart │
│                                                             │
│   PRIORITY: P1 - CRITICAL                                   │
│   Must show: All actors, system boundary, use cases,       │
│              <<include>>/<<extend>> relationships clearly   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.10: Use Case Diagram lengkap sistem CUR-HEART dengan 4 actors, 35+ use cases, showing Guest/Client/Therapist/Admin interactions_

---

#### Aktor dalam Sistem CUR-HEART

**1. Guest (Pengunjung)**
- Belum terautentikasi
- Dapat melihat informasi publik

**2. Client (Klien)**
- User terautentikasi dengan role client
- Dapat melakukan booking dan mengakses layanan

**3. Therapist (Terapis)**
- User terautentikasi dengan role therapist
- Mengelola jadwal dan melakukan sesi terapi

**4. Admin (Administrator)**
- User terautentikasi dengan role admin
- Mengelola seluruh sistem

**5. Payment Gateway**
- Sistem eksternal untuk pemrosesan pembayaran

**Use Case Diagram Lengkap:**

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    SISTEM INFORMASI CUR-HEART                              │
│                         USE CASE DIAGRAM                                   │
└────────────────────────────────────────────────────────────────────────────┘

┌──────────┐                                                      ┌──────────┐
│          │                                                      │          │
│  Guest   │                                                      │  Client  │
│          │                                                      │          │
└────┬─────┘                                                      └────┬─────┘
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Melihat Landing Page                                   │   │
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Melihat Daftar Layanan                                │◄──┤
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Melihat Detail Layanan                                │◄──┤
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Melihat Profil Terapis                                │◄──┤
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Membaca Artikel Blog                                   │◄──┤
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Registrasi Akun                                        │   │
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Login ke Sistem                                        │◄──┤
     │  └─────────────────────┬──────────────────────────────────┘   │
     │                        │                                       │
     │                        │ <<include>>                           │
     │                        ▼                                       │
     │              ┌──────────────────────┐                          │
     │              │ Verifikasi Email     │                          │
     │              └──────────────────────┘                          │
     │                                                                 │
     │                                                                 │
     │                                                     ┌───────────┴──────┐
     │                                                     │                  │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Melakukan Booking     │     │
     │                                          └──────────┬────────────┘     │
     │                                                     │                  │
     │                                          <<include>>│                  │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Memilih Layanan       │     │
     │                                          └───────────────────────┘     │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Memilih Terapis       │     │
     │                                          └───────────────────────┘     │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Memilih Jadwal        │     │
     │                                          └───────────────────────┘     │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Melakukan Pembayaran  │◄────┼────┐
     │                                          └───────────────────────┘     │    │
     │                                                     │                  │    │
     │                                          ┌──────────▼────────────┐     │    │
     │                                          │ Melihat Konfirmasi    │     │    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Melihat Appointment   │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Reschedule Booking    │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Cancel Booking        │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Melihat Progress      │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Mengirim Pesan        │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Memberikan Review     │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                                                        │    │
┌────┴─────┐                                                                 │    │
│          │                                                                 │    │
│Therapist │                                                                 │    │
│          │                                                                 │    │
└────┬─────┘                                                                 │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Dashboard Terapis                              │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Mengelola Jadwal Kerja                                 │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Mengatur Ketersediaan                                  │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Block/Unblock Tanggal                                  │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Daftar Klien                                   │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Profil Klien                                   │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melakukan Sesi Terapi                                  │          │    │
     │  └─────────────────────┬──────────────────────────────────┘          │    │
     │                        │                                             │    │
     │                        │ <<include>>                                 │    │
     │                        ▼                                             │    │
     │              ┌──────────────────────┐                                │    │
     │              │ Menulis Catatan Sesi │                                │    │
     │              └──────────────────────┘                                │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Riwayat Sesi                                   │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Laporan Pendapatan                             │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Mengelola Profil                                       │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Membalas Pesan                                         │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │                                                                       │    │
┌────┴─────┐                                                                │    │
│          │                                                                │    │
│  Admin   │                                                                │    │
│          │                                                                │    │
└────┬─────┘                                                                │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Melihat Dashboard Admin                                │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Mengelola Users                                        │         │    │
     │  └─────────────────────┬──────────────────────────────────┘         │    │
     │                        │                                            │    │
     │                        │ <<extend>>                                 │    │
     │              ┌─────────▼──────────┐                                 │    │
     │              │ Approve Terapis    │                                 │    │
     │              └────────────────────┘                                 │    │
     │              ┌─────────▼──────────┐                                 │    │
     │              │ Suspend User       │                                 │    │
     │              └────────────────────┘                                 │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Mengelola Layanan                                      │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Mengelola Booking                                      │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Verifikasi Pembayaran Manual                           │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Melihat Laporan Keuangan                               │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Generate Reports                                       │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Konfigurasi Sistem                                     │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │                                                                      │    │
     │                                                                      │    │
     │                                                        ┌─────────────┴────┐
     │                                                        │                  │
     │                                                        │ Payment Gateway  │
     │                                                        │                  │
     │                                                        └──────────────────┘
```

**Penjelasan Relasi:**

- **<<include>>**: Use case yang wajib dieksekusi (misal: Booking harus include Memilih Layanan)
- **<<extend>>**: Use case opsional yang memperluas fungsionalitas (misal: Mengelola Users bisa diperluas dengan Approve Terapis)

---

**Tabel 4.31 Use Case List dengan Actors**

| UC ID | Use Case Name | Actor(s) | Priority | Complexity | Description |
|-------|---------------|----------|----------|------------|-------------|
| **Authentication & Authorization** | | | | | |
| UC-01 | Register | Guest | Must Have | Low | User registrasi akun baru (client atau therapist) |
| UC-02 | Login | All Users | Must Have | Low | User login ke sistem dengan email dan password |
| UC-03 | Logout | All Users | Must Have | Low | User logout dari sistem |
| UC-04 | Forgot Password | Guest | Must Have | Medium | User request reset password via email |
| UC-05 | Reset Password | Guest | Must Have | Medium | User set password baru dengan token |
| UC-06 | Verify Email | Guest | Should Have | Low | User verify email setelah registrasi |
| **Client Use Cases** | | | | | |
| UC-07 | Browse Services | Client, Guest | Must Have | Low | User browse katalog layanan terapi |
| UC-08 | View Service Detail | Client, Guest | Must Have | Low | User lihat detail lengkap service |
| UC-09 | Browse Therapists | Client, Guest | Must Have | Low | User browse directory terapis |
| UC-10 | View Therapist Profile | Client, Guest | Must Have | Medium | User lihat profil lengkap terapis |
| UC-11 | Check Therapist Availability | Client | Must Have | High | User cek jadwal available terapis |
| UC-12 | Create Booking | Client | Must Have | High | User booking session terapi (4-step flow) |
| UC-13 | View Booking History | Client | Must Have | Medium | User lihat riwayat booking |
| UC-14 | Reschedule Booking | Client | Should Have | Medium | User ubah jadwal booking (min 24h before) |
| UC-15 | Cancel Booking | Client | Should Have | Medium | User batalkan booking dengan reason |
| UC-16 | Make Payment | Client | Must Have | High | User bayar booking (transfer/gateway) |
| UC-17 | Upload Payment Proof | Client | Must Have | Medium | User upload bukti transfer |
| UC-18 | View Session Notes Summary | Client | Should Have | Medium | User lihat summary catatan terapi |
| UC-19 | Track Progress | Client | Should Have | Medium | User lihat visualisasi progress terapi |
| UC-20 | Self-Assess Progress | Client | Could Have | Low | User input self-assessment metrics |
| UC-21 | Submit Review | Client | Should Have | Medium | User submit rating dan review setelah session |
| UC-22 | Send Message | Client | Could Have | Medium | User kirim pesan ke terapis/admin |
| UC-23 | Update Profile | Client | Must Have | Low | User update profile information |
| **Therapist Use Cases** | | | | | |
| UC-24 | View Appointments | Therapist | Must Have | Medium | Terapis lihat jadwal appointments |
| UC-25 | Set Weekly Availability | Therapist | Must Have | Medium | Terapis set jam kerja per hari |
| UC-26 | Block Specific Dates | Therapist | Must Have | Medium | Terapis block tanggal (cuti, libur) |
| UC-27 | Accept/Reject Booking | Therapist | Should Have | Medium | Terapis approve atau decline booking |
| UC-28 | Start Session | Therapist | Must Have | Low | Terapis mark session as started |
| UC-29 | End Session | Therapist | Must Have | Medium | Terapis mark session as completed |
| UC-30 | Document Session Notes | Therapist | Must Have | High | Terapis input detailed session notes |
| UC-31 | View Client History | Therapist | Must Have | Medium | Terapis lihat riwayat session client |
| UC-32 | Assess Client Progress | Therapist | Should Have | Medium | Terapis input progress assessment |
| UC-33 | Upload Session Attachments | Therapist | Could Have | Low | Terapis upload supporting documents |
| UC-34 | Respond to Reviews | Therapist | Could Have | Low | Terapis reply to client reviews |
| UC-35 | View Earnings Report | Therapist | Should Have | Medium | Terapis lihat laporan pendapatan |
| UC-36 | Update Professional Profile | Therapist | Must Have | Medium | Terapis update bio, credentials, certifications |
| UC-37 | Manage Services Offered | Therapist | Should Have | Low | Terapis pilih services yang dikuasai |
| **Admin Use Cases** | | | | | |
| UC-38 | View Dashboard Overview | Admin | Must Have | Medium | Admin lihat summary metrics sistem |
| UC-39 | Manage Users (CRUD) | Admin | Must Have | High | Admin create/read/update/delete users |
| UC-40 | Approve Therapist | Admin | Must Have | Medium | Admin verify dan approve new therapist |
| UC-41 | Manage Services (CRUD) | Admin | Must Have | Medium | Admin kelola services catalog |
| UC-42 | View All Bookings | Admin | Must Have | Medium | Admin monitor semua bookings |
| UC-43 | Verify Manual Payments | Admin | Must Have | High | Admin approve/reject payment proofs |
| UC-44 | Generate Financial Reports | Admin | Should Have | High | Admin export laporan keuangan |
| UC-45 | Generate Analytics Reports | Admin | Should Have | High | Admin export laporan analytics |
| UC-46 | Moderate Reviews | Admin | Should Have | Medium | Admin approve/hide inappropriate reviews |
| UC-47 | Send Bulk Notifications | Admin | Could Have | Medium | Admin kirim announcement ke users |
| UC-48 | Manage System Settings | Admin | Must Have | Medium | Admin ubah konfigurasi sistem |
| UC-49 | View Audit Logs | Admin | Should Have | Low | Admin lihat activity logs |
| UC-50 | Backup Database | Admin | Must Have | Low | Admin trigger manual backup |

**Use Case Summary:**
- **Total Use Cases:** 50
- **Must Have:** 32 (64%)
- **Should Have:** 14 (28%)
- **Could Have:** 4 (8%)
- **Actors:** 4 (Guest, Client, Therapist, Admin)
- **Average Complexity:** Medium

---

### B. Activity Diagram

Activity Diagram menggambarkan alur kerja (workflow) dari proses bisnis dalam sistem. Berikut adalah activity diagram untuk proses-proses utama:

---

**[GAMBAR 4.11 - Activity Diagram: Booking Process Flow]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT ACTIVITY DIAGRAM - BOOKING FLOW]                 │
│                                                             │
│   CUR-HEART ACTIVITY DIAGRAM                               │
│   Process: Client Booking Workflow (End-to-End)            │
│                                                             │
│   SWIMLANES (3 Actors):                                    │
│   ┌──────────────────────────────────────────────┐         │
│   │ CLIENT                                       │         │
│   ├──────────────────────────────────────────────┤         │
│   │ • Start (Login)                              │         │
│   │ • Browse services                            │         │
│   │ • Select service                             │         │
│   │ • Select therapist                           │         │
│   │ • Choose date & time                         │         │
│   │ • Enter booking details                      │         │
│   │ • Make payment                               │         │
│   │ • Receive confirmation                       │         │
│   │ • End                                        │         │
│   └──────────────────────────────────────────────┘         │
│                                                             │
│   ┌──────────────────────────────────────────────┐         │
│   │ SYSTEM                                       │         │
│   ├──────────────────────────────────────────────┤         │
│   │ • Validate login                             │         │
│   │ • Fetch services list                        │         │
│   │ • Validate service selection                 │         │
│   │ • Filter therapists by service               │         │
│   │ • Get therapist availability                 │         │
│   │ • Check slot availability (Decision)         │         │
│   │ • Create booking record                      │         │
│   │ • Process payment (Payment Gateway)          │         │
│   │ • Update booking status                      │         │
│   │ • Send notification                          │         │
│   │ • Generate confirmation                      │         │
│   └──────────────────────────────────────────────┘         │
│                                                             │
│   ┌──────────────────────────────────────────────┐         │
│   │ PAYMENT GATEWAY                              │         │
│   ├──────────────────────────────────────────────┤         │
│   │ • Receive payment request                    │         │
│   │ • Validate payment method                    │         │
│   │ • Process transaction                        │         │
│   │ • Return payment result (Success/Failed)     │         │
│   └──────────────────────────────────────────────┘         │
│                                                             │
│   KEY ELEMENTS:                                             │
│   • ● (Start node) - Begin booking process                 │
│   • ◉ (End node) - Booking confirmed / cancelled           │
│   • ◇ (Decision) - Slot available? Payment success?        │
│   • ▭ (Activity) - Each action/step                        │
│   • → (Flow) - Sequential flow                             │
│   • ━ (Fork/Join) - Parallel activities                    │
│                                                             │
│   DECISION POINTS (Critical):                               │
│   1. "Is slot still available?"                            │
│      YES → Proceed to booking                              │
│      NO → Show error, re-select time                       │
│                                                             │
│   2. "Payment successful?"                                 │
│      YES → Confirm booking, send notification              │
│      NO → Cancel booking, show error                       │
│                                                             │
│   ALTERNATE FLOWS:                                          │
│   • Slot unavailable → Loop back to date selection         │
│   • Payment failed → Retry or cancel                       │
│   • Validation error → Show error message                  │
│                                                             │
│   TOTAL ACTIVITIES: 20+ nodes                              │
│   DECISION NODES: 3                                        │
│   SWIMLANES: 3 (Client, System, Payment Gateway)           │
│                                                             │
│   Format: UML Activity Diagram (Swimlane) PNG              │
│   Recommended size: 1800x2400px (vertical, detailed)       │
│   Style: UML standard dengan swimlanes, clear labels       │
│                                                             │
│   File: assets/images/activity-diagram-booking-flow.png    │
│   Tool: Visual Paradigm, draw.io, Lucidchart               │
│                                                             │
│   PRIORITY: P1 - CRITICAL                                   │
│   Must show: Swimlanes, decision points, happy & sad paths │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.11: Activity Diagram untuk proses booking lengkap dengan 3 swimlanes (Client, System, Payment Gateway), showing decision points dan alternate flows_

---

#### 1. Activity Diagram: Proses Booking Layanan

```
┌──────────────────────────────────────────────────────────────────────────┐
│              ACTIVITY DIAGRAM - PROSES BOOKING LAYANAN                   │
└──────────────────────────────────────────────────────────────────────────┘

    Client                  Sistem                     Therapist
      │                       │                            │
      │                       │                            │
     ●─┐                      │                            │
      START                   │                            │
      │                       │                            │
      ├──────────────────────►│                            │
      │   Pilih Layanan       │                            │
      │                       │                            │
      │◄──────────────────────┤                            │
      │  Tampilkan List       │                            │
      │    Layanan            │                            │
      │                       │                            │
      ├──────────────────────►│                            │
      │  Submit Layanan       │                            │
      │                       │                            │
      │                    ┌──▼───┐                        │
      │                    │Validasi│                       │
      │                    └──┬───┘                        │
      │                       │                            │
      │                    ╱     ╲                         │
      │                   ╱ Valid? ╲                       │
      │                   ╲       ╱                        │
      │                    ╲     ╱                         │
      │                     ╲   ╱                          │
      │                No   ╱ ╲  Yes                       │
      │◄────────────────────┘  └────┐                     │
      │  Error Message              │                     │
      │                             ▼                     │
      │                    ┌─────────────────┐            │
      │                    │ Filter Terapis  │            │
      │                    │ by Layanan      │            │
      │                    └────────┬────────┘            │
      │◄────────────────────────────┤                     │
      │  Tampilkan List Terapis     │                     │
      │                             │                     │
      ├─────────────────────────────►                     │
      │  Pilih Terapis              │                     │
      │                             │                     │
      │                    ┌────────▼────────┐            │
      │                    │ Get Availability│            │
      │                    │   Terapis       │            │
      │                    └────────┬────────┘            │
      │◄────────────────────────────┤                     │
      │  Tampilkan Calendar         │                     │
      │                             │                     │
      ├─────────────────────────────►                     │
      │  Pilih Tanggal & Waktu      │                     │
      │                             │                     │
      │                    ┌────────▼────────┐            │
      │                    │ Check Conflict  │            │
      │                    └────────┬────────┘            │
      │                             │                     │
      │                          ╱     ╲                  │
      │                         ╱Conflict?╲               │
      │                         ╲       ╱                 │
      │                          ╲     ╱                  │
      │                Yes        ╲   ╱   No              │
      │◄──────────────────────────┘  └───┐               │
      │  Slot Unavailable                │               │
      │                                  ▼               │
      │                         ┌─────────────────┐      │
      │                         │ Create Booking  │      │
      │                         │   (Pending)     │      │
      │                         └────────┬────────┘      │
      │◄─────────────────────────────────┤               │
      │  Tampilkan Ringkasan Booking     │               │
      │                                  │               │
      ├──────────────────────────────────►               │
      │  Konfirmasi & Bayar              │               │
      │                                  │               │
      │                         ┌────────▼────────┐      │
      │                         │ Process Payment │      │
      │                         └────────┬────────┘      │
      │                                  │               │
      │                               ╱     ╲            │
      │                              ╱Success?╲          │
      │                              ╲       ╱           │
      │                               ╲     ╱            │
      │                   No           ╲   ╱  Yes        │
      │                        ┌────────┘  └─────┐       │
      │                        │                 │       │
      │               ┌────────▼─────┐  ┌────────▼──────┐│
      │               │Cancel Booking│  │Update Booking ││
      │               │              │  │  (Confirmed)  ││
      │               └──────┬───────┘  └────────┬──────┘│
      │◄──────────────────────┤                  │       │
      │  Payment Failed       │                  │       │
      │                       │         ┌────────▼──────┐│
      │                       │         │Send Email     ││
      │                       │         │Notification   ││
      │                       │         └────────┬──────┘│
      │                       │                  │       │
      │                       │                  ├───────┼───────────►
      │                       │                  │  Email to Therapist
      │                       │                  │       │
      │◄──────────────────────┴──────────────────┤       │
      │  Booking Confirmation                    │       │
      │                                          │       │
     ─┴─                                         │       │
     END                                         │       │
                                                 │       │
                                            ┌────▼───┐   │
                                            │Notifikasi  │
                                            │Booking Baru│
                                            └────────┘   │
                                                 │       │
                                                ●─┴─     │
                                               END       │
```

**Keterangan:**
- **●** : Start/End point
- **╱ ╲** : Decision/branching point
- **┌──┐** : Activity/process
- **→** : Flow direction

**Proses:**
1. Client memilih layanan dari katalog
2. Sistem memfilter terapis yang menyediakan layanan tersebut
3. Client memilih terapis
4. Sistem menampilkan availability calendar
5. Client memilih tanggal dan waktu
6. Sistem check conflict dengan booking lain
7. Jika available, create booking dengan status "pending"
8. Client melakukan pembayaran
9. Jika pembayaran sukses:
   - Update booking status menjadi "confirmed"
   - Send email notification ke client dan therapist
10. Jika pembayaran gagal:
    - Cancel booking
    - Show error message

---

#### 2. Activity Diagram: Proses Conduct Therapy Session

```
┌──────────────────────────────────────────────────────────────────────────┐
│           ACTIVITY DIAGRAM - CONDUCT THERAPY SESSION                     │
└──────────────────────────────────────────────────────────────────────────┘

    Therapist              Sistem                    Client
      │                      │                          │
      │                      │                          │
     ●─┐                     │                          │
    START                    │                          │
      │                      │                          │
      │              ┌───────▼───────┐                  │
      │              │ Reminder Email│                  │
      │              │   H-1         │                  │
      │              └───────┬───────┘                  │
      │                      │                          │
      │◄─────────────────────┼──────────────────────────┤
      │     Receive Reminder │    Receive Reminder      │
      │                      │                          │
      │              ┌───────▼───────┐                  │
      │              │Session Day     │                  │
      │              │Check Time      │                  │
      │              └───────┬───────┘                  │
      │                      │                          │
      │                   ╱     ╲                       │
      │                  ╱ Time to ╲                    │
      │                  ╲  start? ╱                    │
      │                   ╲       ╱                     │
      │         No         ╲     ╱  Yes                 │
      │          ┌──────────┘   └─────────┐             │
      │          │                        │             │
      │          │ Wait                   ▼             │
      │          └───────────►   ┌────────────────┐     │
      │                         │Enable "Join     │     │
      │                         │Session" Button  │     │
      │                         └────────┬────────┘     │
      │                                  │             │
      │◄─────────────────────────────────┼─────────────┤
      │    Join Session Link             │  Join Session Link
      │                                  │             │
      ├──────────────────────────────────►            │
      │    Click "Join Session"          │             │
      │                                  │             │
      │                         ┌────────▼────────┐    │
      │                         │Create Session   │    │
      │                         │Record           │    │
      │                         └────────┬────────┘    │
      │                                  │             │
      │                         ┌────────▼────────┐    │
      │                         │Open Session Room│    │
      │                         │(Video Call)     │    │
      │                         └────────┬────────┘    │
      │◄─────────────────────────────────┼─────────────┤
      │    Session Room Interface        │  Session Room Interface
      │                                  │             │
      ├──────────────────────────────────┼─────────────►
      │    Start Video Call              │  Join Video Call
      │                                  │             │
      ├──────────────────────────────────┼─────────────►
      │◄─────────────────────────────────┼─────────────┤
      │    Video & Audio Stream          │  Video & Audio Stream
      │                                  │             │
      ├──────────────────────────────────►            │
      │    Conduct Therapy               │             │
      │    (Discussion, Hypnosis, etc)   │             │
      │                                  │             │
      │    ┌─────────────────┐           │             │
      │    │ Take Notes      │           │             │
      │    │ (Real-time)     │           │             │
      │    └────────┬────────┘           │             │
      │             │                    │             │
      │    ┌────────▼────────┐           │             │
      │───►│ Autosave Notes  │           │             │
      │    │ Every 2 minutes │           │             │
      │    └─────────────────┘           │             │
      │                                  │             │
      │                               ╱     ╲          │
      │                              ╱Session ╲        │
      │                              ╲Complete?╱       │
      │                               ╲       ╱        │
      │             No                 ╲     ╱  Yes    │
      │          ┌─────────────────────┘   └──────┐   │
      │          │ Continue                       │   │
      │          └───────────►                    │   │
      │                                           ▼   │
      ├───────────────────────────────────────────►   │
      │    End Video Call                         │   │
      │                                           │   │
      │                              ┌────────────▼───┤
      │                              │Record End Time │
      │                              │Update Duration │
      │                              └────────────┬───┘
      │                                           │   │
      │◄──────────────────────────────────────────┤   │
      │    Redirect to Session Notes Page         │   │
      │                                           │   │
      ├───────────────────────────────────────────►   │
      │    Complete Session Notes                 │   │
      │    (Condition, Techniques,                │   │
      │     Progress, Recommendations)            │   │
      │                                           │   │
      │                              ┌────────────▼───┤
      │                              │ Save Notes     │
      │                              │ Mark Session   │
      │                              │ Completed      │
      │                              └────────────┬───┘
      │                                           │   │
      │                              ┌────────────▼───┤
      │                              │ Update Client  │
      │                              │ Progress Score │
      │                              └────────────┬───┘
      │                                           │   │
      │                              ┌────────────▼───┤
      │                              │Send Follow-up  │
      │                              │Email & Request │
      │                              │Review          │
      │                              └────────────┬───┘
      │                                           │   │
      │◄──────────────────────────────────────────┼───┤
      │    Success Notification                   │ Email Notification
      │                                           │   │
     ─┴─                                          │  ●─┴─
     END                                          │  END
                                                  │
```

**Proses:**
1. Sistem send reminder email H-1 ke client dan therapist
2. Pada hari H, sistem check waktu session
3. 15 menit sebelum session, enable "Join Session" button
4. Client dan therapist join session room
5. Therapist start video call
6. Conduct therapy session dengan video call
7. Therapist take notes real-time (autosave setiap 2 menit)
8. Setelah session selesai, end video call
9. Sistem record end time dan calculate duration
10. Therapist finalize session notes
11. Sistem update client progress score
12. Send follow-up email dan request review

---

#### 3. Activity Diagram: Proses Verifikasi Pembayaran Manual (Admin)

```
┌──────────────────────────────────────────────────────────────────────────┐
│        ACTIVITY DIAGRAM - VERIFIKASI PEMBAYARAN MANUAL (ADMIN)          │
└──────────────────────────────────────────────────────────────────────────┘

    Client                  Sistem                     Admin
      │                       │                          │
      │                       │                          │
     ●─┐                      │                          │
    START                     │                          │
      │                       │                          │
      ├──────────────────────►│                          │
      │  Pilih Metode         │                          │
      │  Bank Transfer        │                          │
      │                       │                          │
      │◄──────────────────────┤                          │
      │  Show Bank Account    │                          │
      │  Info & Instructions  │                          │
      │                       │                          │
      ├──────────────────────►│                          │
      │  Confirm Order        │                          │
      │                       │                          │
      │              ┌────────▼────────┐                 │
      │              │Create Booking   │                 │
      │              │Status: Pending  │                 │
      │              │Payment          │                 │
      │              └────────┬────────┘                 │
      │◄──────────────────────┤                          │
      │  Booking Number &     │                          │
      │  Payment Instructions │                          │
      │                       │                          │
      ├──────────────────────►│                          │
      │  Transfer to Bank     │                          │
      │                       │                          │
      ├──────────────────────►│                          │
      │  Upload Proof of      │                          │
      │  Payment (Screenshot) │                          │
      │                       │                          │
      │              ┌────────▼────────┐                 │
      │              │Save Proof File  │                 │
      │              │Update Payment   │                 │
      │              │Status:Processing│                 │
      │              └────────┬────────┘                 │
      │                       │                          │
      │              ┌────────▼────────┐                 │
      │              │Notify Admin     │                 │
      │              │(Email + System) │                 │
      │              └────────┬────────┘                 │
      │                       │                          │
      │                       ├──────────────────────────►
      │                       │   New Payment to Verify  │
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Access Admin Panel│
      │                       │              │Financial Reports │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │View Pending      │
      │                       │              │Payments List     │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Click Payment     │
      │                       │              │to Verify         │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │View Details:     │
      │                       │              │- Booking Info    │
      │                       │              │- Amount          │
      │                       │              │- Proof of Payment│
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Download & Check  │
      │                       │              │Proof Image       │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Check Bank Account│
      │                       │              │(via Mobile Bank) │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │                       ╱     ╲
      │                       │                      ╱Payment ╲
      │                       │                      ╲ Valid? ╱
      │                       │                       ╲       ╱
      │                       │           No           ╲     ╱  Yes
      │                       │              ┌──────────┘   └────────┐
      │                       │              │                       │
      │                       │    ┌─────────▼─────┐     ┌──────────▼────┐
      │                       │    │Reject Payment │     │Approve Payment │
      │                       │    │Enter Reason   │     │Enter Ref. No. │
      │                       │    └─────────┬─────┘     └──────────┬────┘
      │                       │              │                       │
      │                       │    ┌─────────▼─────┐     ┌──────────▼────┐
      │                       │◄───┤Update Payment │     │Update Payment  │
      │                       │    │Status: Failed │     │Status:Completed│
      │                       │    └─────────┬─────┘     └──────────┬────┘
      │                       │              │                       │
      │                       │    ┌─────────▼─────┐     ┌──────────▼────┐
      │                       │◄───┤Send Email:    │     │Send Email:     │
      │                       │    │Payment Rejected│    │Payment Confirmed│
      │                       │    └─────────┬─────┘     └──────────┬────┘
      │                       │              │                       │
      │◄──────────────────────┼──────────────┴───────────────────────┘
      │  Email Notification   │
      │                       │
      │                    ╱     ╲
      │                   ╱Approved?╲
      │                   ╲       ╱
      │        No          ╲     ╱  Yes
      │          ┌──────────┘   └──────┐
      │          │                     │
      │    ┌─────▼─────┐      ┌────────▼────┐
      │    │Re-upload  │      │Booking      │
      │    │Proof or   │      │Confirmed    │
      │    │Request    │      └────────┬────┘
      │    │Refund     │               │
      │    └─────┬─────┘      ┌────────▼────┐
      │          │            │Send Calendar│
      │          │            │Invite (.ics)│
      │          │            └────────┬────┘
      │          │                     │
      │          │◄────────────────────┤
      │          │   Calendar File     │
      │          │                     │
     ─┴──────────┴─                   ─┴─
     END         END                  END
```

**Proses:**
1. Client pilih bank transfer sebagai payment method
2. Sistem show bank account details dan instructions
3. Client transfer dana ke bank account CUR-HEART
4. Client upload proof of payment (screenshot)
5. Sistem save file dan update payment status ke "processing"
6. Sistem notify admin ada payment baru untuk diverifikasi
7. Admin access financial reports panel
8. Admin view list pending payments
9. Admin click specific payment untuk verify
10. Admin check proof of payment image
11. Admin cross-check dengan mobile banking transaction history
12. Jika valid:
    - Admin approve payment
    - Enter reference number
    - Update payment status ke "completed"
    - Update booking status ke "confirmed"
    - Send confirmation email ke client
    - Send calendar invite (.ics file)
13. Jika tidak valid:
    - Admin reject payment
    - Enter rejection reason
    - Update payment status ke "failed"
    - Send rejection email ke client
    - Client bisa re-upload proof atau request refund

---

### C. Sequence Diagram

Sequence Diagram menggambarkan interaksi antar objek dalam sistem berdasarkan urutan waktu. Berikut adalah sequence diagram untuk use case kritis:

---

**[GAMBAR 4.12 - Sequence Diagram: Booking Process Interaction]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT SEQUENCE DIAGRAM - BOOKING PROCESS]              │
│                                                             │
│   CUR-HEART SEQUENCE DIAGRAM                               │
│   Scenario: Client Makes Booking (Happy Path)              │
│                                                             │
│   OBJECTS/LIFELINES (7):                                   │
│   1. Client (Actor)                                        │
│   2. Browser (UI)                                          │
│   3. BookingController (Laravel Controller)                │
│   4. BookingService (Business Logic)                       │
│   5. TherapistModel (Data Access)                          │
│   6. PaymentGateway (External API)                         │
│   7. Database (MySQL)                                      │
│                                                             │
│   MESSAGE FLOW (Sequential):                               │
│                                                             │
│   Client → Browser                                         │
│   1. "Click Book Now"                                      │
│                                                             │
│   Browser → BookingController                              │
│   2. "GET /booking/create"                                 │
│   3. ← Return booking form                                 │
│                                                             │
│   Client → Browser                                         │
│   4. "Fill form & Submit"                                  │
│                                                             │
│   Browser → BookingController                              │
│   5. "POST /booking/store" (service_id, therapist_id,      │
│       date, time)                                          │
│                                                             │
│   BookingController → BookingService                       │
│   6. "validateBooking(data)"                               │
│                                                             │
│   BookingService → TherapistModel                          │
│   7. "checkAvailability(therapist_id, date, time)"         │
│                                                             │
│   TherapistModel → Database                                │
│   8. "SELECT * FROM therapist_availability WHERE..."       │
│   9. ← Return availability data                            │
│                                                             │
│   (Decision: If available)                                 │
│                                                             │
│   BookingService → Database                                │
│   10. "INSERT INTO bookings (...)"                         │
│   11. ← Return booking_id                                  │
│                                                             │
│   BookingController → PaymentGateway                       │
│   12. "createPayment(booking_id, amount)"                  │
│   13. ← Return payment_url                                 │
│                                                             │
│   BookingController → Browser                              │
│   14. ← Redirect to payment_url                            │
│                                                             │
│   Browser → PaymentGateway                                 │
│   15. "Complete payment (Midtrans page)"                   │
│   16. ← Payment success callback                           │
│                                                             │
│   PaymentGateway → BookingController                       │
│   17. "POST /payment/callback" (transaction_status)        │
│                                                             │
│   BookingController → Database                             │
│   18. "UPDATE bookings SET status='confirmed'"             │
│   19. "INSERT INTO payments (...)"                         │
│   20. ← Success                                            │
│                                                             │
│   BookingController → Browser                              │
│   21. ← Return confirmation page                           │
│                                                             │
│   KEY FEATURES:                                             │
│   • Synchronous calls (solid arrows →)                     │
│   • Return messages (dashed arrows ←)                      │
│   • Activation boxes (vertical rectangles on lifelines)    │
│   • ALT frame (alternative flow for errors)                │
│   • OPT frame (optional payment gateway interaction)       │
│                                                             │
│   TOTAL MESSAGES: 21                                       │
│   DECISION POINTS: 1 (availability check)                  │
│   EXTERNAL SYSTEMS: 1 (Payment Gateway)                    │
│                                                             │
│   Format: UML Sequence Diagram PNG                         │
│   Recommended size: 2000x1600px (horizontal, wide)         │
│   Style: UML standard dengan lifelines, activation boxes   │
│                                                             │
│   File: assets/images/sequence-diagram-booking.png         │
│   Tool: Visual Paradigm, draw.io, PlantUML, Lucidchart    │
│                                                             │
│   PRIORITY: P1 - CRITICAL                                   │
│   Must show: All objects, message sequence numbers,        │
│              return messages, activation periods            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.12: Sequence Diagram untuk proses booking dengan 7 objects/lifelines, 21 messages, showing interaction between Client, Browser, Controllers, Services, Models, Payment Gateway, and Database_

---

#### 1. Sequence Diagram: User Authentication (Login)

```
┌──────────────────────────────────────────────────────────────────────────┐
│              SEQUENCE DIAGRAM - USER AUTHENTICATION                      │
└──────────────────────────────────────────────────────────────────────────┘

Client      Browser        LoginController    AuthMiddleware    UserModel    Database
  │             │                 │                │                │            │
  │   Open      │                 │                │                │            │
  │ Login Page  │                 │                │                │            │
  ├────────────►│                 │                │                │            │
  │             │   GET /login    │                │                │            │
  │             ├────────────────►│                │                │            │
  │             │                 │                │                │            │
  │             │   Return View   │                │                │            │
  │             │◄────────────────┤                │                │            │
  │             │                 │                │                │            │
  │◄────────────┤                 │                │                │            │
  │ Show Login  │                 │                │                │            │
  │    Form     │                 │                │                │            │
  │             │                 │                │                │            │
  │   Enter     │                 │                │                │            │
  │ Credentials │                 │                │                │            │
  │ (Email +    │                 │                │                │            │
  │  Password)  │                 │                │                │            │
  │             │                 │                │                │            │
  │   Submit    │                 │                │                │            │
  │    Form     │                 │                │                │            │
  ├────────────►│                 │                │                │            │
  │             │ POST /login     │                │                │            │
  │             │ {email,password}│                │                │            │
  │             ├────────────────►│                │                │            │
  │             │                 │                │                │            │
  │             │                 │  Validate CSRF Token            │            │
  │             │                 ├────────────────►                │            │
  │             │                 │                │                │            │
  │             │                 │    Valid       │                │            │
  │             │                 │◄────────────────                │            │
  │             │                 │                │                │            │
  │             │                 │  Validate Input                 │            │
  │             │                 │  (email format,│                │            │
  │             │                 │   required)    │                │            │
  │             │                 │                │                │            │
  │             │                 │  Find User by Email             │            │
  │             │                 ├─────────────────────────────────►           │
  │             │                 │                │                │            │
  │             │                 │                │ SELECT * FROM users        │
  │             │                 │                │  WHERE email = ?           │
  │             │                 │                │                ├───────────►
  │             │                 │                │                │            │
  │             │                 │                │      User Data │            │
  │             │                 │                │◄───────────────┼────────────┤
  │             │                 │                │                │            │
  │             │                 │    User Object │                │            │
  │             │                 │◄─────────────────────────────────           │
  │             │                 │                │                │            │
  │             │                 │  Check if User Exists           │            │
  │             │                 │                │                │            │
  │             │                 │ ╔═════════════════════════════╗ │            │
  │             │                 │ ║  Alt [User Not Found]       ║ │            │
  │             │                 │ ╠═════════════════════════════╣ │            │
  │             │                 │ ║  Return Error               ║ │            │
  │             │                 │ ║  "Invalid Credentials"      ║ │            │
  │             │   Error 401     │ ╚═════════════════════════════╝ │            │
  │             │◄────────────────┤                │                │            │
  │◄────────────┤                 │                │                │            │
  │  Show Error │                 │                │                │            │
  │   Message   │                 │                │                │            │
  │             │                 │ ╔═════════════════════════════╗ │            │
  │             │                 │ ║  Alt [User Found]           ║ │            │
  │             │                 │ ╠═════════════════════════════╣ │            │
  │             │                 │ ║  Verify Password Hash       ║ │            │
  │             │                 │ ║  (bcrypt compare)           ║ │            │
  │             │                 │ ╚══════════════╦══════════════╝ │            │
  │             │                 │                ▼                │            │
  │             │                 │  ╔═══════════════════════════╗  │            │
  │             │                 │  ║ Alt [Password Mismatch]   ║  │            │
  │             │                 │  ╠═══════════════════════════╣  │            │
  │             │                 │  ║ Return Error              ║  │            │
  │             │                 │  ║ "Invalid Credentials"     ║  │            │
  │             │   Error 401     │  ╚═══════════════════════════╝  │            │
  │             │◄────────────────┤                │                │            │
  │◄────────────┤                 │                │                │            │
  │  Show Error │                 │                │                │            │
  │             │                 │  ╔═══════════════════════════╗  │            │
  │             │                 │  ║ Alt [Password Match]      ║  │            │
  │             │                 │  ╠═══════════════════════════╣  │            │
  │             │                 │  ║ Check User Status         ║  │            │
  │             │                 │  ║ (active/inactive/suspended║  │            │
  │             │                 │  ╚═══════════╦═══════════════╝  │            │
  │             │                 │              ▼                  │            │
  │             │                 │  ╔═══════════════════════════╗  │            │
  │             │                 │  ║ Alt [Status != active]    ║  │            │
  │             │                 │  ╠═══════════════════════════╣  │            │
  │             │                 │  ║ Return Error              ║  │            │
  │             │                 │  ║ "Account suspended/       ║  │            │
  │             │                 │  ║  inactive"                ║  │            │
  │             │   Error 403     │  ╚═══════════════════════════╝  │            │
  │             │◄────────────────┤                │                │            │
  │◄────────────┤                 │                │                │            │
  │             │                 │  ╔═══════════════════════════╗  │            │
  │             │                 │  ║ Alt [Status = active]     ║  │            │
  │             │                 │  ╠═══════════════════════════╣  │            │
  │             │                 │  ║ Create Session            ║  │            │
  │             │                 │  ║ (Laravel Session)         ║  │            │
  │             │                 │  ╚═══════════════════════════╝  │            │
  │             │                 │                │                │            │
  │             │                 │  Store User ID in Session       │            │
  │             │                 │                │                │            │
  │             │                 │  Generate Session Token         │            │
  │             │                 │                │                │            │
  │             │                 │  Update last_login              │            │
  │             │                 ├─────────────────────────────────►           │
  │             │                 │                │                │            │
  │             │                 │                │  UPDATE users  │            │
  │             │                 │                │  SET last_login = NOW()    │
  │             │                 │                │  WHERE id = ?  ├───────────►
  │             │                 │                │                │            │
  │             │                 │                │   Success      │            │
  │             │                 │◄─────────────────────────────────┼────────────┤
  │             │                 │                │                │            │
  │             │                 │  Log Activity  │                │            │
  │             │                 │  "User X logged in"             │            │
  │             │                 │                │                │            │
  │             │                 │  Redirect Based on Role         │            │
  │             │                 │  - Client → /client/dashboard   │            │
  │             │                 │  - Therapist → /therapist/dash  │            │
  │             │                 │  - Admin → /admin/dashboard     │            │
  │             │                 │                │                │            │
  │             │   Redirect 302  │                │                │            │
  │             │◄────────────────┤                │                │            │
  │             │                 │                │                │            │
  │◄────────────┤                 │                │                │            │
  │   Navigate  │                 │                │                │            │
  │     to      │                 │                │                │            │
  │  Dashboard  │                 │                │                │            │
  │             │                 │                │                │            │
```

**Objek yang Terlibat:**
- **Client**: End user (browser)
- **Browser**: User agent
- **LoginController**: Controller yang handle login logic
- **AuthMiddleware**: Middleware untuk authentication dan authorization
- **UserModel**: Model Eloquent untuk user data
- **Database**: MySQL database

**Proses:**
1. Client buka login page (GET request)
2. Server return login form view
3. User enter credentials (email + password)
4. Submit form (POST request)
5. System validate CSRF token
6. System validate input format
7. System query database untuk find user by email
8. System check if user exists
9. System verify password using bcrypt
10. System check user account status
11. If semua valid:
    - Create session
    - Store user ID dalam session
    - Generate session token (cookie)
    - Update last_login timestamp
    - Log activity
    - Redirect ke dashboard sesuai role
12. If ada error (credentials invalid, account suspended, dll):
    - Return error message
    - Redirect back ke login form

---

**[File ini mencakup Use Case Diagram, Activity Diagram, dan Sequence Diagram. Akan dilanjutkan dengan file berikutnya untuk bagian 4.4-4.7]**
