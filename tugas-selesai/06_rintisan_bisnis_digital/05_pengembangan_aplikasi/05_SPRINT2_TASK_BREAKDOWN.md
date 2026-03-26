# Sprint 2 Task Breakdown

## CUR-HEART V1 - E2 (Booking & Scheduling)

Durasi sprint (disarankan): 2 minggu  
Fokus: mengimplementasikan booking wizard 4 langkah, validasi ketersediaan terapis, deteksi konflik jadwal, serta kebijakan reschedule/cancel.

---

## 1. Target Sprint 2

1. Client dapat melakukan booking end-to-end sampai status `pending_payment`.
2. Slot jadwal terapis ditampilkan real-time berdasarkan availability/unavailability.
3. Sistem mencegah booking bentrok dengan rule conflict detection.
4. Client dapat reschedule/cancel sesuai kebijakan waktu.
5. Data booking siap dipakai integrasi payment di Sprint 3.

---

## 2. Sprint Backlog (Story Level)

| Story ID | Story | Prioritas | Estimasi |
|---|---|---|---|
| S2-ST-01 | Implementasi katalog layanan terintegrasi booking | P1 | 3 SP |
| S2-ST-02 | Implementasi step pilih terapis + slot tersedia | P1 | 8 SP |
| S2-ST-03 | Implementasi conflict detection saat create booking | P1 | 8 SP |
| S2-ST-04 | Implementasi konfirmasi booking + ringkasan harga (tanpa payment processing) | P1 | 5 SP |
| S2-ST-05 | Implementasi reschedule booking sesuai policy | P1 | 5 SP |
| S2-ST-06 | Implementasi cancel booking sesuai policy | P1 | 5 SP |
| S2-ST-07 | Test coverage booking & scheduling | P1 | 5 SP |

---

## 3. Task Breakdown Teknis

## 3.1 Backend / API

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S2-BE-001 | Implement endpoint list services untuk booking (`GET /api/v1/services`) | Data layanan siap dipilih | Sprint 1 selesai |
| S2-BE-002 | Implement endpoint list therapist by service (`GET /api/v1/therapists?service_id=`) | Filter terapis per layanan | S2-BE-001 |
| S2-BE-003 | Implement availability resolver (availability - unavailability - booked slots) | Slot real-time tersedia | S2-BE-002 |
| S2-BE-004 | Implement create booking (`POST /api/v1/bookings`) status awal `pending_payment` | Booking tercatat | S2-BE-003 |
| S2-BE-005 | Implement conflict detection guard di create booking (atomic check) | Prevent double booking | S2-BE-004 |
| S2-BE-006 | Implement booking detail (`GET /api/v1/bookings/{id}`) | Ringkasan booking tersedia | S2-BE-004 |
| S2-BE-007 | Implement reschedule endpoint (`PATCH /api/v1/bookings/{id}/reschedule`) | Jadwal booking dapat dipindah | S2-BE-006 |
| S2-BE-008 | Implement cancel endpoint (`PATCH /api/v1/bookings/{id}/cancel`) + reason | Pembatalan sesuai policy | S2-BE-006 |
| S2-BE-009 | Implement policy window cancel/reschedule dari `system_settings` | Policy fleksibel konfigurasi | S2-BE-007 |
| S2-BE-010 | Tambahkan activity log untuk create/reschedule/cancel | Audit operasional booking | S2-BE-004 |

## 3.2 Frontend (Inertia + React TSX)

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S2-FE-001 | Buat halaman wizard Step 1: pilih layanan | Step 1 aktif | S2-BE-001 |
| S2-FE-002 | Buat halaman wizard Step 2: pilih terapis | Step 2 aktif | S2-BE-002 |
| S2-FE-003 | Buat halaman wizard Step 3: pilih tanggal/jam | Step 3 aktif | S2-BE-003 |
| S2-FE-004 | Buat halaman wizard Step 4: konfirmasi booking + total harga | Step 4 aktif | S2-BE-004 |
| S2-FE-005 | State management multi-step (persist draft booking) | Perpindahan step stabil | S2-FE-001 |
| S2-FE-006 | Implement UI indikator slot (available/booked/blocked) | UX jadwal jelas | S2-FE-003 |
| S2-FE-007 | Implement halaman detail booking client | Booking detail tampil | S2-BE-006 |
| S2-FE-008 | Implement UI reschedule/cancel + validation message | Aksi booking lengkap | S2-BE-007 |

## 3.3 Database

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S2-DB-001 | Finalisasi migration tabel booking domain (`services`, `therapist_services`, `therapist_availability`, `therapist_unavailability`, `bookings`, `promo_codes`) | Skema booking siap | Sprint 1 selesai |
| S2-DB-002 | Tambah index query kritis (`therapist_id`, `booking_date`, `booking_time`, `status`) | Query slot efisien | S2-DB-001 |
| S2-DB-003 | Seeder data layanan/terapis/availability untuk QA | Dataset pengujian siap | S2-DB-001 |
| S2-DB-004 | Validasi relasi FK dan constraint status booking | Integritas data booking | S2-DB-001 |

## 3.4 QA / Testing

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S2-QA-001 | Feature test create booking happy path | Create booking tervalidasi | S2-BE-004 |
| S2-QA-002 | Feature test conflict detection | Double booking tertolak | S2-BE-005 |
| S2-QA-003 | Feature test reschedule policy window | Reschedule policy valid | S2-BE-007 |
| S2-QA-004 | Feature test cancel policy window | Cancel policy valid | S2-BE-008 |
| S2-QA-005 | API test ketersediaan slot terapis | Slot resolver valid | S2-BE-003 |
| S2-QA-006 | UI E2E smoke wizard 4 langkah | Flow booking UI stabil | S2-FE-004 |

---

## 4. Acceptance Criteria Sprint 2

```gherkin
Scenario: Client berhasil membuat booking sampai pending_payment
  Given client sudah login
  When client menyelesaikan wizard booking 4 langkah dengan slot valid
  Then sistem membuat booking baru
  And status booking adalah pending_payment
```

```gherkin
Scenario: Sistem menolak slot bentrok
  Given slot terapis sudah digunakan untuk waktu yang sama
  When client mencoba booking slot tersebut
  Then sistem menolak request
  And menampilkan pesan konflik jadwal
```

```gherkin
Scenario: Client reschedule dalam batas kebijakan
  Given client memiliki booking aktif
  And waktu sesi masih dalam window reschedule yang diizinkan
  When client memilih slot baru yang valid
  Then sistem memperbarui jadwal booking
```

```gherkin
Scenario: Client cancel di luar kebijakan ditolak
  Given client memiliki booking dengan waktu sesi sudah melewati batas cancel
  When client mengajukan cancel
  Then sistem menolak cancel
  And menampilkan alasan policy
```

```gherkin
Scenario: Slot availability menghitung jadwal tidak tersedia
  Given therapist memiliki unavailability pada tanggal tertentu
  When client membuka daftar slot tanggal tersebut
  Then slot yang bentrok tidak ditampilkan sebagai available
```

---

## 5. Deliverables Sprint 2

1. Modul booking wizard 4 langkah aktif.
2. Endpoint booking dan scheduling minimal V1 tersedia.
3. Conflict detection berjalan di backend.
4. Reschedule/cancel policy berjalan dari konfigurasi sistem.
5. Test report booking flow untuk handoff payment sprint berikutnya.

---

## 6. Non-Goal Sprint 2

1. Integrasi payment gateway Midtrans.
2. Payment callback/webhook.
3. Dashboard keuangan admin.
4. Notifikasi email payment.

---

## 7. Definition of Done Sprint 2

1. Semua story P1 selesai dan lulus QA.
2. Tidak ada bug blocker pada flow booking wizard.
3. Endpoint booking utama terdokumentasi.
4. Audit log create/reschedule/cancel tercatat.
5. Siap handoff ke Sprint 3 (Payment & Finance Control).

---

## 8. Handoff ke Sprint 3

Prerequisite untuk mulai Sprint 3:

1. Status booking `pending_payment` sudah stabil sebagai state awal.
2. Booking detail punya data cukup untuk pembuatan invoice/order payment.
3. Policy cancel/reschedule sudah final untuk sinkronisasi refund rule.
4. Struktur tabel payment dapat dihubungkan langsung ke booking.
