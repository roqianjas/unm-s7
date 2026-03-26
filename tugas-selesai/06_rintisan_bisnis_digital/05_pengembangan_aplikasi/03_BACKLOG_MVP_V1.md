# Backlog MVP V1 (Siap Sprint)

Backlog ini turunan langsung dari PRD V1 agar tim bisa langsung eksekusi.

## Epic E0 - Platform Foundation

1. Setup Laravel 12 + Breeze React TS.
2. Setup Inertia layout dan route grouping.
3. Setup role-permission dasar.
4. Setup database model inti dan migration.

## Epic E1 - Public dan Auth

1. Implement public pages (home/services/therapists/blog/faq/contact).
2. Register/login/forgot-reset password.
3. Proteksi route by role.

## Epic E2 - Booking dan Scheduling

1. Wizard 4 langkah booking.
2. Validasi ketersediaan slot.
3. Conflict detection dan error handling.
4. Reschedule/cancel sesuai policy.

## Epic E3 - Payment dan Finance Control

1. Integrasi Midtrans (channel whitelist VA/Bank + Card).
2. Callback idempotent untuk status payment.
3. Sinkronisasi status booking-payment.
4. Audit trail transaksi.

## Epic E4 - Therapist Session Workflow

1. Dashboard therapist.
2. Session notes + auto-save.
3. Riwayat sesi dan data klien.

## Epic E5 - Admin Operation

1. Dashboard KPI.
2. CRUD users/services/bookings.
3. Reporting dan export.
4. Withdrawal request processing.

## Epic E6 - Notification dan Monitoring

1. Email konfirmasi dan reminder H-1/H-0.
2. In-app notification.
3. Monitoring: payment success rate, booking conversion, API error rate.

## Sprint sequencing (disarankan)

1. Sprint 1: E0 + E1
2. Sprint 2: E2
3. Sprint 3: E3
4. Sprint 4: E4 + E5
5. Sprint 5: E6 + hardening

## Definition of Ready (DoR)

1. Story punya acceptance criteria.
2. Dependency teknis jelas.
3. Estimasi dan owner jelas.

## Definition of Done (DoD)

1. Lolos code review.
2. Lolos test skenario kritis.
3. Tidak melanggar payment policy PRD.
4. Dokumentasi endpoint/update perilaku diperbarui.
