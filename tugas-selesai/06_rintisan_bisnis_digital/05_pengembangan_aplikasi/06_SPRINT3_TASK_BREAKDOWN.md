# Sprint 3 Task Breakdown

## CUR-HEART V1 - E3 (Payment & Finance Control)

Durasi sprint (disarankan): 2 minggu  
Fokus: integrasi payment gateway Midtrans dengan kontrol finansial ketat, sinkronisasi status booking-payment, callback idempotent, dan audit trail transaksi.

---

## 1. Target Sprint 3

1. Client dapat lanjut dari booking `pending_payment` ke proses checkout.
2. Metode pembayaran hanya `VA/Bank Transfer` dan `Card`.
3. Sistem menerima webhook Midtrans dan update status secara konsisten.
4. Callback idempotent mencegah duplikasi update transaksi.
5. Audit trail payment tersedia untuk monitoring dan rekonsiliasi.

---

## 2. Sprint Backlog (Story Level)

| Story ID | Story | Prioritas | Estimasi |
|---|---|---|---|
| S3-ST-01 | Integrasi checkout Midtrans dari booking | P1 | 8 SP |
| S3-ST-02 | Validasi channel payment whitelist (VA/Bank + Card only) | P1 | 5 SP |
| S3-ST-03 | Implement webhook Midtrans dengan signature verification | P1 | 8 SP |
| S3-ST-04 | Implement idempotency guard untuk callback | P1 | 5 SP |
| S3-ST-05 | Sinkronisasi status booking-payment lifecycle | P1 | 5 SP |
| S3-ST-06 | Implement payment history/status page untuk client | P2 | 3 SP |
| S3-ST-07 | Test coverage payment flow + observability | P1 | 5 SP |

---

## 3. Task Breakdown Teknis

## 3.1 Backend / API

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S3-BE-001 | Setup konfigurasi Midtrans (`server_key`, `client_key`, env mode) | Gateway config siap | Sprint 2 selesai |
| S3-BE-002 | Implement service checkout `POST /api/v1/payments/checkout` berbasis booking | Token/redirect checkout tersedia | S3-BE-001 |
| S3-BE-003 | Implement channel whitelist validator (hanya VA/Bank + Card) | Channel non-allowed ditolak | S3-BE-002 |
| S3-BE-004 | Implement webhook endpoint `POST /api/v1/payments/webhook/midtrans` | Callback diterima aman | S3-BE-001 |
| S3-BE-005 | Implement signature verification webhook Midtrans | Callback validasi aman | S3-BE-004 |
| S3-BE-006 | Implement idempotency key strategy by `order_id/transaction_id` | Update duplikat dicegah | S3-BE-004 |
| S3-BE-007 | Implement status mapper payment (`pending/success/failed/expired/refunded`) | Status konsisten di DB | S3-BE-004 |
| S3-BE-008 | Implement booking status transition service saat payment berubah | Booking-payment sinkron | S3-BE-007 |
| S3-BE-009 | Implement endpoint payment detail/history (`GET /api/v1/payments/{id}`) | Status payment dapat dipantau | S3-BE-007 |
| S3-BE-010 | Log seluruh event payment ke `activity_logs` | Audit trail transaksi aktif | S3-BE-004 |
| S3-BE-011 | Buat command rekonsiliasi sederhana (manual trigger) untuk mismatch status | Recovery operasional tersedia | S3-BE-008 |

## 3.2 Frontend (Inertia + React TSX)

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S3-FE-001 | Tambah tombol `Proceed to Payment` pada booking `pending_payment` | Trigger checkout tersedia | S3-BE-002 |
| S3-FE-002 | Implement checkout UI dengan daftar metode yang diizinkan saja | UI compliant policy | S3-BE-003 |
| S3-FE-003 | Implement halaman status payment (pending/success/failed/expired) | Feedback user jelas | S3-BE-007 |
| S3-FE-004 | Implement retry flow untuk status failed/expired | Recovery user flow | S3-BE-002 |
| S3-FE-005 | Tampilkan history payment di dashboard client | Transparansi pembayaran | S3-BE-009 |

## 3.3 Database

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S3-DB-001 | Validasi migration tabel `payments` sesuai schema baseline | Tabel payment siap produksi | Sprint 2 selesai |
| S3-DB-002 | Pastikan constraint unik `booking_id` dan `transaction_id` berjalan | Anti-duplikasi transaksi | S3-DB-001 |
| S3-DB-003 | Tambah index untuk query monitoring (`status`, `paid_at`) | Query operasional cepat | S3-DB-001 |
| S3-DB-004 | Sinkronkan relasi `payments` -> `bookings` dan audit logs | Integritas data terjaga | S3-DB-001 |

## 3.4 QA / Testing

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S3-QA-001 | Feature test checkout success path | Checkout valid | S3-BE-002 |
| S3-QA-002 | Feature test channel blacklist (e-wallet/QRIS) ditolak | Policy payment tervalidasi | S3-BE-003 |
| S3-QA-003 | Feature test webhook signature invalid ditolak | Security webhook tervalidasi | S3-BE-005 |
| S3-QA-004 | Feature test callback duplicate (idempotent) | Tidak ada update ganda | S3-BE-006 |
| S3-QA-005 | Feature test status transition booking-payment | Konsistensi state tervalidasi | S3-BE-008 |
| S3-QA-006 | UI E2E test booking -> payment -> status result | End-to-end payment stabil | S3-FE-003 |

---

## 4. Acceptance Criteria Sprint 3

```gherkin
Scenario: Client checkout dari booking pending_payment
  Given client memiliki booking berstatus pending_payment
  When client menekan tombol proceed to payment
  Then sistem membuat transaksi payment
  And client menerima context checkout yang valid
```

```gherkin
Scenario: Metode terlarang tidak tersedia
  Given client berada di halaman checkout
  When sistem menampilkan opsi pembayaran
  Then hanya VA/Bank Transfer dan Card yang ditampilkan
  And e-wallet serta QRIS tidak ditampilkan
```

```gherkin
Scenario: Webhook sukses mengubah status payment
  Given payment berstatus pending
  When webhook valid mengirim status success
  Then status payment berubah menjadi success
  And booking diperbarui sesuai aturan transisi
```

```gherkin
Scenario: Callback duplikat tidak menyebabkan update ganda
  Given webhook dengan order_id yang sama dikirim ulang
  When sistem menerima callback kedua
  Then sistem tidak membuat perubahan status kedua
  And audit log menandai event sebagai duplicate callback
```

```gherkin
Scenario: Webhook signature invalid ditolak
  Given request callback tanpa signature valid
  When endpoint webhook dipanggil
  Then sistem menolak request
  And tidak ada perubahan status transaksi
```

---

## 5. Deliverables Sprint 3

1. Integrasi Midtrans checkout aktif pada flow booking.
2. Webhook callback dengan signature verification dan idempotency guard.
3. Sinkronisasi status booking-payment tervalidasi.
4. UI payment status + retry flow untuk user.
5. Test report payment flow dan daftar observability event.

---

## 6. Non-Goal Sprint 3

1. Payout/withdrawal processing terapis (Sprint 4).
2. Laporan keuangan admin lengkap.
3. Notifikasi reminder H-1/H-0 berbasis queue penuh.
4. Integrasi live consultation.

---

## 7. Definition of Done Sprint 3

1. Semua story P1 selesai dan lulus QA.
2. Payment policy PRD dipatuhi sepenuhnya (tanpa wallet/e-wallet/QRIS).
3. Callback Midtrans aman (signature validasi + idempotent).
4. Tidak ada bug blocker pada flow booking-to-payment.
5. Endpoint payment terdokumentasi dan siap handoff sprint 4.

---

## 8. Handoff ke Sprint 4

Prerequisite untuk mulai Sprint 4:

1. Status payment dan booking sudah stabil di production-like environment.
2. Audit trail payment siap dipakai admin operation.
3. Rule dasar refund/penyesuaian status sudah terdokumentasi.
4. Dasar data pendapatan terapis siap dipakai modul withdrawal.
