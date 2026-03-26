# PRD CUR-HEART V1

## Product Requirements Document

**Produk**: CUR-HEART - Platform Terapi Kesehatan Mental  
**Versi Dokumen**: 1.0  
**Tanggal**: 16 Maret 2026  
**Audiens Utama**: Tim Produk dan Tim Development  
**Sumber Acuan Utama**: `02_laporan/*` dan `01_desain/database/schema.sql`  

---

## 1. Ringkasan Eksekutif

Dokumen ini mendefinisikan requirement produk CUR-HEART V1 sebagai aplikasi web production-ready dengan arsitektur:

- Backend: Laravel 12 (monolith)
- Frontend: Inertia.js + React + TSX
- Database: MySQL (model 22 tabel sesuai `schema.sql`)

V1 berfokus pada penguatan alur inti layanan hipnoterapi: discovery layanan, autentikasi multi-peran, booking 4 langkah, pembayaran terintegrasi, dokumentasi sesi, dashboard operasional, dan notifikasi.  
V1 tidak membangun mobile app native, namun wajib API-ready melalui kontrak `/api/v1` agar fase mobile dapat dikembangkan tanpa refactor besar.

---

## 2. Latar Belakang dan Problem Statement

Masalah utama yang diselesaikan:

1. Reservasi manual tidak efisien (konversi rendah, proses lambat).
2. Konflik jadwal terapis sering terjadi.
3. Dokumentasi sesi terapi tidak terstruktur dan menyita waktu.
4. Monitoring operasional dan finansial belum real-time.
5. Pengalaman pengguna antar peran belum terstandardisasi.

Konteks domain:

- Layanan kesehatan mental bersifat sensitif (privasi tinggi).
- Data terapi perlu kesinambungan antar sesi.
- Sistem pembayaran harus aman, terkontrol, dan mudah diaudit.

---

## 3. Tujuan Produk, KPI, dan Success Criteria

## 3.1 Tujuan Produk V1

1. Menyediakan platform web end-to-end untuk operasional terapi.
2. Meningkatkan efisiensi proses booking, jadwal, dan dokumentasi.
3. Meningkatkan pengalaman pengguna klien, terapis, dan admin.
4. Menyediakan pondasi API untuk ekspansi mobile di fase berikutnya.

## 3.2 KPI Produk V1

| KPI | Baseline | Target V1 | Sumber Baseline |
|---|---:|---:|---|
| Booking conversion rate | 60% | >= 85% | 02_BAB_I_PENDAHULUAN.md |
| Konflik jadwal bulanan | 8-10 kasus/bulan | 0 kasus/bulan | 02_BAB_I_PENDAHULUAN.md |
| Waktu dokumentasi sesi | 15 menit/sesi | <= 5 menit/sesi | 02_BAB_I_PENDAHULUAN.md |
| Beban tugas admin repetitif | 70% waktu kerja | <= 35% waktu kerja | 04_BAB_III_PEMBAHASAN_PROSES_BISNIS_STARTUP.md |
| Task completion usability | 92% | >= 90% (maintain) | 05_BAB_IV_ANALISA_DAN_PERANCANGAN_APLIKASI.md |
| SUS Score | 78/100 | >= 70 (minimal) | 05_BAB_IV_ANALISA_DAN_PERANCANGAN_APLIKASI.md |
| Pass rate black-box test | 100% (50/50) | 100% pada critical flow | 05_BAB_IV_ANALISA_DAN_PERANCANGAN_APLIKASI.md |

## 3.3 Success Criteria V1 (Go-Live Gate)

1. Seluruh critical journey (guest/client/therapist/admin) lulus UAT.
2. Checkout hanya menampilkan metode yang diizinkan (VA/Bank, Card).
3. Tidak ada opsi wallet balance, e-wallet, dan QRIS di UI maupun backend config.
4. Callback payment sukses/gagal/expired konsisten terhadap status booking-payment.
5. Kontrak `/api/v1` terdokumentasi untuk modul inti.

---

## 4. Persona dan Peran Pengguna

| Peran | Tujuan Utama | Kebutuhan Kritis |
|---|---|---|
| Guest | Mengenal layanan dan trust building | Konten layanan, profil terapis, FAQ, blog, CTA booking |
| Client | Booking dan menjalani terapi dengan nyaman | Jadwal real-time, pembayaran aman, histori & progress, notifikasi |
| Therapist | Menjalankan sesi efektif | Manajemen jadwal, data klien, dokumentasi sesi cepat, tracking pendapatan |
| Admin | Operasional dan kontrol bisnis | Monitoring KPI, manajemen pengguna/booking, verifikasi, reporting, audit trail |

---

## 5. Scope Produk V1

## 5.1 In-Scope V1

1. Public pages: homepage, about, services, service detail, therapists, therapist profile, blog, blog detail, FAQ, contact, privacy policy, terms.
2. Auth multi-role: register, login, forgot/reset password, role-based access.
3. Booking wizard 4 langkah: pilih layanan, pilih terapis, pilih jadwal, konfirmasi + pembayaran.
4. Scheduling dan conflict detection untuk slot terapis.
5. Session management dan dokumentasi sesi terapi.
6. Dashboard per role: client, therapist, admin.
7. Admin modules: booking management, user management, therapist verification, services/content management, financial/reporting.
8. Notifikasi: in-app + email event-based.
9. API `/api/v1` untuk modul inti (auth, services, therapists, bookings, payments, sessions, notifications).
10. Konsultasi online didukung melalui `session_type=online` dengan `session_link` ke platform pihak ketiga.

## 5.2 Out-of-Scope V1

1. Aplikasi mobile native (iOS/Android).
2. Pembangunan engine live konsultasi internal real-time (WebRTC server sendiri).
3. Fitur wallet internal, top-up saldo, dompet pengguna.
4. Metode pembayaran e-wallet dan QRIS.
5. AI recommendation, gamification, forum komunitas.
6. Insurance integration dan diagnosis medis otomatis.

---

## 6. Kebutuhan Fungsional V1

## 6.1 Domain Public Experience

| ID | Requirement | Prioritas |
|---|---|---|
| FR-PUB-001 | Pengunjung dapat melihat halaman publik tanpa login | Must |
| FR-PUB-002 | Pengunjung dapat melihat katalog layanan dan detail harga/durasi | Must |
| FR-PUB-003 | Pengunjung dapat melihat profil terapis dan rating | Must |
| FR-PUB-004 | Pengunjung dapat membaca blog dan FAQ | Must |
| FR-PUB-005 | Pengunjung dapat submit form kontak | Should |

## 6.2 Domain Authentication & Authorization

| ID | Requirement | Prioritas |
|---|---|---|
| FR-AUTH-001 | Sistem menyediakan register untuk client dan therapist | Must |
| FR-AUTH-002 | Sistem menyediakan login/logout dan sesi aman | Must |
| FR-AUTH-003 | Sistem menyediakan forgot/reset password | Must |
| FR-AUTH-004 | Role-based access control untuk guest/client/therapist/admin | Must |

## 6.3 Domain Booking & Scheduling

| ID | Requirement | Prioritas |
|---|---|---|
| FR-BKG-001 | Client dapat membuat booking melalui wizard 4 langkah | Must |
| FR-BKG-002 | Sistem menampilkan slot jadwal terapis yang tersedia real-time | Must |
| FR-BKG-003 | Sistem mencegah booking saat slot konflik | Must |
| FR-BKG-004 | Client dapat menggunakan kode promo yang valid | Should |
| FR-BKG-005 | Client dapat melihat, reschedule, dan cancel booking sesuai policy | Must |

## 6.4 Domain Payment

| ID | Requirement | Prioritas |
|---|---|---|
| FR-PAY-001 | Checkout hanya menampilkan VA/Bank Transfer dan Card | Must |
| FR-PAY-002 | Sistem membuat invoice/order per booking (tanpa wallet) | Must |
| FR-PAY-003 | Sistem menerima callback gateway untuk update status payment | Must |
| FR-PAY-004 | Status booking sinkron dengan status payment | Must |
| FR-PAY-005 | Sistem mencatat audit trail transaksi lengkap | Must |

## 6.5 Domain Session & Clinical Documentation

| ID | Requirement | Prioritas |
|---|---|---|
| FR-SES-001 | Therapist melihat jadwal sesi harian/mingguan | Must |
| FR-SES-002 | Therapist membuat dokumentasi sesi terstruktur | Must |
| FR-SES-003 | Auto-save dokumentasi untuk mencegah kehilangan data | Must |
| FR-SES-004 | Client melihat catatan sesi yang diizinkan | Should |

## 6.6 Domain Dashboard & Operations

| ID | Requirement | Prioritas |
|---|---|---|
| FR-DASH-001 | Client dashboard menampilkan upcoming sessions, histori, progress | Must |
| FR-DASH-002 | Therapist dashboard menampilkan jadwal, klien, pendapatan | Must |
| FR-DASH-003 | Admin dashboard menampilkan KPI, booking, payment, laporan | Must |
| FR-DASH-004 | Admin dapat export laporan (Excel/PDF) | Should |

## 6.7 Domain Notification & Messaging

| ID | Requirement | Prioritas |
|---|---|---|
| FR-NTF-001 | Sistem mengirim email konfirmasi booking dan payment | Must |
| FR-NTF-002 | Sistem mengirim reminder sesi H-1 dan H-0 | Must |
| FR-NTF-003 | Sistem menampilkan notifikasi in-app per role | Must |
| FR-NTF-004 | User dapat mark notification as read | Must |

## 6.8 Domain Withdrawal & Payout Terapis (Tanpa Wallet)

| ID | Requirement | Prioritas |
|---|---|---|
| FR-WDR-001 | Sistem menghitung hak pendapatan terapis dari sesi yang `completed` dan payment `success` | Must |
| FR-WDR-002 | Terapis dapat mengajukan pencairan ke rekening bank terdaftar | Must |
| FR-WDR-003 | Admin dapat approve/reject permintaan pencairan dengan alasan | Must |
| FR-WDR-004 | Admin dapat menandai payout sebagai processed setelah transfer bank berhasil | Must |
| FR-WDR-005 | Sistem mencatat audit trail lengkap untuk setiap perubahan status pencairan | Must |

---

## 7. User Journey Inti (Dengan Precondition/Postcondition/Error State)

| Journey | Precondition | Alur Utama | Postcondition | Error State |
|---|---|---|---|---|
| Guest menjelajah layanan | Tidak login | Buka layanan -> lihat detail -> klik daftar/login | Guest terdorong ke funnel registrasi | Halaman tidak ditemukan, konten gagal load |
| Client booking 4-step | Client login, profil valid | Pilih layanan -> terapis -> slot -> konfirmasi -> bayar | Booking tercatat + status payment terbarui | Slot bentrok, payment gagal/expired |
| Client sesi online | Client login, booking `paid/confirmed`, `session_type=online` | Buka detail sesi -> akses `session_link` | Client masuk ke ruang konsultasi pihak ketiga | Link tidak valid/expired |
| Therapist dokumentasi sesi | Therapist login, sesi tersedia | Buka sesi -> isi dokumentasi -> simpan | Catatan tersimpan, status sesi updated | Validasi form gagal, save timeout |
| Therapist request payout | Therapist login, memiliki payable eligible | Buka earnings -> ajukan pencairan -> tunggu verifikasi admin | Withdrawal tercatat dengan status `pending` | Data bank tidak valid, amount tidak memenuhi syarat |
| Admin monitoring operasional | Admin login | Buka dashboard -> filter data -> generate report | Data KPI dan report tersedia | Query timeout, data tidak konsisten |
| Admin proses payout | Admin login, ada request `pending/approved` | Review request -> approve/reject -> proses transfer -> update status | Pencairan selesai atau ditolak dengan alasan | Bukti transfer tidak valid, update status gagal |

---

## 8. Non-Functional Requirements (NFR)

| Kategori | Requirement V1 |
|---|---|
| Performance | Page load < 2 detik, API response < 500 ms (P95 untuk critical endpoints) |
| Reliability | Uptime >= 99%, retry policy untuk event payment callback |
| Security | HTTPS wajib, CSRF/XSS/SQLi protection, RBAC, hashing password bcrypt/argon2 |
| Compliance | Kepatuhan UU PDP, consent policy, data retention policy |
| Usability | SUS >= 70, task completion >= 90%, error rate < 5% |
| Auditability | Semua perubahan status booking/payment dan aksi admin tercatat di audit log |
| Scalability | API versioning dan modular service boundaries untuk kesiapan mobile |
| Maintainability | Type-safe frontend (TSX), coding standard, automated test minimal untuk critical flow |

---

## 9. Arsitektur Teknis V1

## 9.1 Stack Wajib

1. Backend: Laravel 12 (PHP 8.3+), monolith modular.
2. Frontend: Inertia.js + React + TypeScript (TSX).
3. Database: MySQL 8.
4. Queue/Job: Laravel Queue.
5. Payment: Midtrans (channel terbatas sesuai policy).

## 9.2 Prinsip Arsitektur

1. Single codebase web app dengan route web + API.
2. UI web menggunakan Inertia pages.
3. Endpoint mobile-ready disediakan pada namespace `/api/v1`.
4. Kontrak API stabil per versi; perubahan breaking harus via versi baru.

## 9.3 Data Model (Baseline Schema)

Baseline data model mengacu pada `schema.sql` dengan 22 tabel, dikelompokkan:

1. Identity & Role: `users`, `clients`, `therapists`
2. Services & Availability: `services`, `therapist_services`, `therapist_availability`, `therapist_unavailability`
3. Transaction Core: `bookings`, `payments`, `promo_codes`
4. Session Clinical: `sessions`, `session_notes`, `reviews`
5. Content: `blog_categories`, `blog_posts`, `faq_categories`, `faqs`
6. Communication & Ops: `messages`, `notifications`, `withdrawals`, `activity_logs`, `system_settings`

---

## 10. Strategi Mobile (Web-First, API-Ready)

## 10.1 Keputusan V1

1. Tidak membangun mobile native di V1.
2. Menyiapkan API kontrak `/api/v1` untuk modul inti.
3. Memastikan skema auth, error format, dan payload stabil agar reusable untuk mobile.

## 10.2 Deliverable Mobile-Readiness V1

1. Dokumen endpoint API V1.
2. Standar request/response.
3. Versioning policy.
4. Status transition contract untuk booking/payment/session.

---

## 11. Kebijakan Pembayaran dan Kontrol Finance

## 11.1 Metode Pembayaran

Diizinkan:

1. Virtual Account / Bank Transfer.
2. Card (credit/debit via gateway).

Dilarang:

1. E-wallet.
2. QRIS.
3. Wallet balance.
4. Top-up saldo internal.

## 11.2 Implementasi Policy

1. UI checkout hanya render channel VA/Bank + Card.
2. Backend validasi hard-rule channel whitelist.
3. Konfigurasi Midtrans menonaktifkan wallet dan QRIS.
4. Tidak ada tabel/fitur saldo user dalam domain payment.

## 11.3 Kontrol Finance dan Keamanan Transaksi

1. Semua transaksi berbasis invoice/order per booking.
2. Callback webhook wajib idempotent (dedupe by `transaction_id`/`order_id`).
3. Audit trail wajib untuk event: created, pending, success, failed, expired, refunded.
4. Rekonsiliasi status booking-payment dilakukan otomatis + manual fallback admin.
5. Semua event payment dicatat timestamp dan actor/source event.

## 11.4 Mekanisme Pencairan Dana Terapis (Tanpa Wallet)

Prinsip:

1. Sistem tidak menyimpan saldo wallet user.
2. Hak terapis dicatat sebagai payable operasional berbasis transaksi sesi selesai.

Alur payout:

1. Booking memiliki payment `success` dan sesi berstatus `completed`.
2. Sistem menghitung nilai payout terapis:
   `net_payout = final_price - platform_fee - penyesuaian (jika ada)`.
3. Nilai payout menjadi eligible setelah melewati settlement hold/refund window sesuai kebijakan bisnis.
4. Terapis membuat request pencairan ke rekening bank yang tersimpan pada profil.
5. Admin meninjau request:
   - `pending -> approved`, atau
   - `pending -> rejected` (wajib alasan).
6. Setelah transfer bank dilakukan, admin set status:
   - `approved -> processed` (wajib bukti transfer/reference).
7. Semua perubahan status tercatat di audit log.

Catatan implementasi:

1. Tidak ada fitur top-up/withdraw saldo pelanggan.
2. Tabel operasional yang digunakan: `therapists`, `bookings`, `payments`, `withdrawals`, `activity_logs`.

---

## 12. Kontrak API V1 (`/api/v1`)

## 12.1 Aturan Umum

1. Prefix versi: `/api/v1`.
2. Format respons sukses:

```json
{
  "success": true,
  "message": "OK",
  "data": {},
  "meta": {}
}
```

3. Format respons gagal:

```json
{
  "success": false,
  "message": "Validation error",
  "errors": {
    "field_name": ["error detail"]
  }
}
```

4. Auth API: Bearer token (Sanctum/Personal Access Token).
5. Semua endpoint protected wajib role-based authorization.

## 12.2 Modul Endpoint Inti

| Modul | Endpoint Minimal V1 |
|---|---|
| Auth | `POST /auth/login`, `POST /auth/logout`, `GET /auth/me` |
| Services | `GET /services`, `GET /services/{id}` |
| Therapists | `GET /therapists`, `GET /therapists/{id}`, `GET /therapists/{id}/availability` |
| Bookings | `POST /bookings`, `GET /bookings`, `GET /bookings/{id}`, `PATCH /bookings/{id}/reschedule`, `PATCH /bookings/{id}/cancel` |
| Payments | `POST /payments/checkout`, `POST /payments/webhook/midtrans`, `GET /payments/{id}` |
| Sessions | `GET /sessions`, `GET /sessions/{id}`, `POST /sessions/{id}/notes` |
| Notifications | `GET /notifications`, `PATCH /notifications/{id}/read` |
| Withdrawals | `GET /withdrawals`, `POST /withdrawals`, `PATCH /withdrawals/{id}/approve`, `PATCH /withdrawals/{id}/reject`, `PATCH /withdrawals/{id}/process` |

## 12.3 Status Transition Contract

Booking:

1. `pending_payment` -> `paid` -> `confirmed` -> `completed`
2. `pending_payment` -> `cancelled`
3. `paid/confirmed` -> `cancelled` (sesuai policy)

Payment:

1. `pending` -> `success`
2. `pending` -> `failed`
3. `pending` -> `expired`
4. `success` -> `refunded` (jika kebijakan refund aktif)

Session:

1. `scheduled` -> `in_progress` -> `completed`
2. `scheduled` -> `cancelled`

Withdrawal:

1. `pending` -> `approved`
2. `pending` -> `rejected`
3. `approved` -> `processed`

---

## 13. Data Reconciliation

## 13.1 Aturan Prioritas

Saat data antar artefak bertabrakan, gunakan urutan:

1. `02_laporan/*`
2. `schema.sql`
3. `TBD (butuh validasi stakeholder)`

## 13.2 Conflict Matrix dan Baseline Terpilih

| Item | Konflik Data | Baseline Terpilih | Alasan |
|---|---|---|---|
| Jumlah tabel DB | 16 tabel (narasi laporan) vs 22 tabel (`schema.sql`) | 22 tabel | `schema.sql` adalah sumber teknis implementable |
| Revenue Year 1 | Rp 180 juta vs Rp 1,2 miliar vs Rp 2,4 miliar | Rp 1,2 miliar (baseline kerja) | Muncul konsisten di bagian model bisnis laporan/presentasi; perlu validasi stakeholder untuk final finansial |
| Investment ask | Rp 500 juta vs Rp 1,5 miliar vs Rp 800 juta initial capital | Rp 500 juta (ask) + catatan initial capital TBD | Ask investor dan kebutuhan modal operasional punya konteks berbeda |
| Break-even | Bulan ke-8 vs 18 bulan | Bulan ke-8 (operasional) | Lebih sering muncul pada target sistem bisnis V1 |

Catatan:

- Item finansial tetap harus dikonfirmasi pada sesi alignment stakeholder bisnis sebelum final sign-off PRD.
- Item teknis mengikuti struktur `schema.sql` sebagai acuan build.

---

## 14. Test Plan V1

## 14.1 Strategi Pengujian

1. Unit test: validasi logic inti (pricing, conflict detection, status transition).
2. Feature/API test: endpoint auth, booking, payment, session, notifications.
3. Integration test: Midtrans checkout + webhook callback lifecycle.
4. E2E/UAT: user journey lintas role.
5. Security test: authz/authn, invalid token, CSRF, input validation.
6. Non-functional test: performa endpoint kritis, error monitoring.

## 14.2 Coverage Wajib

1. Semua journey inti memiliki precondition, postcondition, dan error state.
2. Semua fitur Must-have memiliki acceptance criteria Gherkin.
3. Payment constraint test memastikan channel terlarang tidak tersedia di UI/backend.
4. Callback status test memastikan konsistensi booking-payment-session.

---

## 15. Acceptance Criteria (Gherkin Style)

## 15.1 Public dan Auth

```gherkin
Scenario: Guest melihat detail layanan
  Given pengguna belum login
  When pengguna membuka halaman detail layanan
  Then sistem menampilkan deskripsi, durasi, dan harga layanan
```

```gherkin
Scenario: Client login berhasil
  Given client memiliki akun aktif
  When client memasukkan email dan password valid
  Then sistem mengarahkan client ke dashboard client
```

## 15.2 Booking dan Jadwal

```gherkin
Scenario: Client membuat booking 4 langkah
  Given client sudah login
  When client menyelesaikan langkah layanan, terapis, jadwal, dan konfirmasi
  Then sistem membuat booking dengan status pending_payment
```

```gherkin
Scenario: Sistem menolak slot bentrok
  Given slot terapis sudah terisi
  When client memilih slot yang sama
  Then sistem menolak booking dan menampilkan pesan konflik jadwal
```

```gherkin
Scenario: Client reschedule sesuai kebijakan
  Given client memiliki booking aktif
  When client melakukan reschedule dalam jendela waktu yang diizinkan
  Then sistem memperbarui jadwal booking dan mengirim notifikasi
```

## 15.3 Payment Policy

```gherkin
Scenario: Checkout hanya tampilkan metode yang diizinkan
  Given client berada di halaman checkout
  When sistem memuat payment methods
  Then hanya VA/Bank Transfer dan Card yang tampil
  And e-wallet, QRIS, wallet balance, dan top-up tidak tampil
```

```gherkin
Scenario: Payment success sinkron ke booking
  Given booking berstatus pending_payment
  When webhook gateway mengirim status success valid
  Then payment menjadi success
  And booking berubah menjadi paid atau confirmed sesuai aturan sistem
```

```gherkin
Scenario: Payment failed/expired ditangani konsisten
  Given booking berstatus pending_payment
  When webhook gateway mengirim status failed atau expired
  Then payment diperbarui sesuai status
  And booking tidak boleh menjadi confirmed
```

```gherkin
Scenario: Callback idempotent
  Given webhook dengan transaction_id yang sama dikirim ulang
  When sistem memproses callback kedua
  Then sistem tidak menduplikasi transaksi
  And status akhir tetap konsisten
```

## 15.4 Therapist dan Session Documentation

```gherkin
Scenario: Therapist menyimpan dokumentasi sesi
  Given therapist login dan sesi tersedia
  When therapist mengisi field wajib dokumentasi dan klik simpan
  Then catatan sesi tersimpan
  And status sesi diperbarui sesuai alur
```

```gherkin
Scenario: Auto-save dokumentasi aktif
  Given therapist sedang mengetik catatan sesi
  When interval auto-save tercapai
  Then draft dokumentasi tersimpan otomatis
```

## 15.5 Dashboard, Reporting, Notification

```gherkin
Scenario: Admin generate laporan
  Given admin login
  When admin memilih jenis laporan dan periode
  Then sistem menampilkan laporan dengan data terfilter
```

```gherkin
Scenario: Notifikasi reminder sesi
  Given client memiliki sesi besok
  When jadwal reminder H-1 berjalan
  Then sistem mengirim notifikasi email dan in-app
```

```gherkin
Scenario: Mark notification as read
  Given user memiliki notifikasi belum dibaca
  When user menandai notifikasi sebagai dibaca
  Then badge unread berkurang
```

## 15.6 API Mobile-Readiness

```gherkin
Scenario: Endpoint API versi v1 tersedia
  Given client aplikasi mengakses /api/v1/services
  When request valid dikirim
  Then sistem mengembalikan respons sukses dengan format standar
```

```gherkin
Scenario: Error format API konsisten
  Given request API tidak valid
  When endpoint memproses request
  Then sistem mengembalikan success false dan object errors terstruktur
```

## 15.7 Withdrawal & Payout Terapis

```gherkin
Scenario: Terapis mengajukan pencairan dana
  Given terapis memiliki payable yang eligible
  And rekening bank terapis sudah terdaftar
  When terapis submit permintaan pencairan
  Then sistem membuat data withdrawal dengan status pending
```

```gherkin
Scenario: Admin menyetujui pencairan dana
  Given ada withdrawal berstatus pending
  When admin melakukan approve
  Then status berubah menjadi approved
```

```gherkin
Scenario: Admin memproses transfer payout
  Given ada withdrawal berstatus approved
  When admin mengisi referensi transfer dan bukti transfer
  Then status berubah menjadi processed
  And aktivitas tercatat pada audit log
```

```gherkin
Scenario: Admin menolak pencairan dana
  Given ada withdrawal berstatus pending
  When admin melakukan reject dengan alasan
  Then status berubah menjadi rejected
  And alasan penolakan tersimpan
```

---

## 16. Monitoring dan Operational Metrics

Minimal metrik monitoring production:

1. Booking conversion rate.
2. Payment success rate.
3. Payment failed/expired rate.
4. API error rate untuk endpoint kritis.
5. Average response time endpoint kritis.
6. Queue failure count untuk notifikasi/payment event.
7. Withdrawal processing time (pending hingga processed).

Alert minimum:

1. Payment webhook failure spike.
2. Error rate endpoint checkout > threshold.
3. Uptime turun di bawah SLA.

---

## 17. Asumsi, Dependensi, dan Risiko

## 17.1 Asumsi Default

1. V1 fokus web release; mobile app masuk roadmap fase berikutnya.
2. Payment gateway menggunakan Midtrans dengan wallet/QRIS nonaktif.
3. User memiliki akses internet dan perangkat modern browser.

## 17.2 Dependensi

1. Ketersediaan akun dan kredensial gateway Midtrans.
2. Infrastruktur email SMTP/gateway.
3. Konfirmasi kebijakan legal dan PDP dari stakeholder.

## 17.3 Risiko Utama

1. Perubahan regulasi data pribadi.
2. Ketidakkonsistenan data finansial antar dokumen bisnis.
3. Integrasi callback payment yang tidak idempotent jika implementasi tidak disiplin.

Mitigasi:

1. Terapkan data reconciliation dan sign-off stakeholder.
2. Wajibkan contract test untuk payment callback.
3. Wajibkan audit log dan observability untuk transaksi.

---

## 18. Definisi Selesai (Definition of Done V1)

V1 dinyatakan selesai jika:

1. Seluruh requirement Must-have pada PRD terimplementasi.
2. Seluruh acceptance criteria Gherkin critical flow lulus.
3. Checkout policy sesuai constraint finance (tanpa wallet/QRIS/e-wallet).
4. Endpoint `/api/v1` inti tersedia dan terdokumentasi.
5. NFR minimum terpenuhi pada UAT dan smoke test production.

---

## 19. Backlog Non-Prioritas: Live Consultation via External Service (Phase 2)

Status prioritas:

1. Live consultation ditetapkan sebagai `P3 (non-priority)` terhadap V1.
2. Eksekusi dimulai setelah V1 stabil pasca go-live.

Tujuan fase 2:

1. Menyediakan konsultasi video 1:1 langsung di dalam aplikasi dengan integrasi provider eksternal.
2. Menjaga standar privasi dan keamanan untuk domain kesehatan mental.

Keputusan teknis fase 2:

1. Tidak membangun engine live sendiri pada fase ini.
2. Menggunakan layanan/package eksternal yang tersedia, dengan prioritas opsi gratis.
3. Pilihan default implementasi: **Jitsi** (embed via IFrame API atau React SDK).
4. Arsitektur backend tetap provider-agnostic untuk memudahkan ganti vendor jika diperlukan.

Persiapan yang tetap dilakukan di V1 (tanpa membangun engine live):

1. Mempertahankan struktur sesi online (`session_type=online`, `session_link`) sebagai fallback.
2. Menjaga desain API versioned agar modul sesi dapat diperluas tanpa breaking changes.
3. Menyiapkan boundary service konsultasi (provider-agnostic) di arsitektur backend.
4. Menyusun requirement consent dan kebijakan privasi sesi live untuk fase 2.

Rencana implementasi bertahap:

1. **Phase 2A (Recommended)**: Integrasi Jitsi gratis sebagai baseline live consultation.
2. **Phase 2B (Opsional)**: Evaluasi provider lain (misalnya Daily/Agora free-tier atau paket berbayar) jika dibutuhkan SLA/fitur tambahan.
3. **Phase 2C (Exceptional Case)**: Evaluasi engine internal/WebRTC native hanya jika kebutuhan compliance/scale tidak bisa dipenuhi provider eksternal.

Exit criteria fase 2 (high-level):

1. Join success rate sesi live memenuhi target SLA produk.
2. Audio/video stability memenuhi target kualitas minimum.
3. Event sesi tercatat (join/leave/duration/error) untuk audit operasional.
4. Security review untuk akses meeting token dan session authorization lulus.

Catatan:

1. Sampai fase 2 aktif, fitur konsultasi online V1 tetap menggunakan link pihak ketiga.
2. Fitur ini disiapkan, tetapi tidak mengubah prioritas delivery V1.
3. Jika pemakaian provider gratis mencapai limit usage, kebijakan fallback adalah upgrade plan provider atau pindah provider, bukan langsung membangun engine internal.

---

## 20. Lampiran

Dokumen referensi:

1. `02_laporan/02_BAB_I_PENDAHULUAN.md`
2. `02_laporan/04_BAB_III_PEMBAHASAN_PROSES_BISNIS_STARTUP.md`
3. `02_laporan/05_BAB_IV_ANALISA_DAN_PERANCANGAN_APLIKASI.md`
4. `01_desain/database/schema.sql`
5. `05_pengembangan_aplikasi/00_BACKLOG_PHASE2A_LIVE_CONSULTATION_JITSI.md`

