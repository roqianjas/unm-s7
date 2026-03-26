# Roadmap Eksekusi V1

Dokumen ini memecah implementasi PRD V1 ke fase kerja yang bisa langsung dijalankan.

## Fase 0 - Foundation

Target:

1. Setup project Laravel 12 + Inertia + React TSX.
2. Setup auth multi-role dasar.
3. Setup database baseline dari `schema.sql` (22 tabel).

Output:

1. Repositori aplikasi berjalan lokal.
2. Konfigurasi environment dev/staging.
3. Migration dan seeding awal siap.

## Fase 1 - Core Product MVP

Target:

1. Public pages dan auth.
2. Booking 4 langkah.
3. Payment tanpa wallet (VA/Bank + Card).
4. Dashboard client/therapist/admin.

Output:

1. Critical journey end-to-end berjalan.
2. Status booking-payment sinkron.

## Fase 2 - Stabilization V1

Target:

1. Notifikasi email dan in-app.
2. Session documentation + auto-save.
3. Reporting admin dan audit trail.
4. Hardening security + observability.

Output:

1. UAT lulus untuk flow kritis.
2. Monitoring minimum aktif.

## Fase 3 - Post V1 (Non-Priority)

Target:

1. Mobile readiness dipakai untuk app mobile.
2. Live consultation via external service (Jitsi) sesuai backlog phase 2A.

Output:

1. Pilot live consultation berjalan terbatas.

## Exit criteria go-live V1

1. Must-have requirement PRD selesai.
2. Payment policy compliant: tanpa e-wallet, QRIS, wallet balance/top-up.
3. Endpoint `/api/v1` inti tersedia dan terdokumentasi.
4. Blackbox flow kritis pass.
