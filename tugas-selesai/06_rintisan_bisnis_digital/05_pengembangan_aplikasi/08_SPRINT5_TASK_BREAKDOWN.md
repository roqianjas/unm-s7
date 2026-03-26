# Sprint 5 Task Breakdown

## CUR-HEART V1 - E6 (Notification & Monitoring) + Hardening

Durasi sprint (disarankan): 2 minggu  
Fokus: penyelesaian notifikasi email/in-app, monitoring metrik inti, hardening performa dan keamanan, serta release readiness V1.

---

## 1. Target Sprint 5

1. Event penting sistem mengirim notifikasi otomatis (email dan in-app).
2. Reminder sesi H-1 dan H-0 berjalan stabil lewat queue.
3. Monitoring metrik inti V1 aktif (booking, payment, error, response time).
4. Security dan performance hardening mencapai baseline PRD.
5. Paket release readiness V1 siap untuk go-live.

---

## 2. Sprint Backlog (Story Level)

| Story ID | Story | Prioritas | Estimasi |
|---|---|---|---|
| S5-ST-01 | Implement event-driven notification pipeline | P1 | 8 SP |
| S5-ST-02 | Implement reminder sesi H-1 dan H-0 | P1 | 5 SP |
| S5-ST-03 | Implement in-app notification center | P1 | 5 SP |
| S5-ST-04 | Implement monitoring dashboard metrik inti V1 | P1 | 8 SP |
| S5-ST-05 | Security hardening (authz, rate limiting, audit coverage) | P1 | 8 SP |
| S5-ST-06 | Performance hardening endpoint kritis | P1 | 5 SP |
| S5-ST-07 | UAT end-to-end dan bug fixing final | P1 | 8 SP |
| S5-ST-08 | Release readiness checklist + rollout plan | P1 | 5 SP |

---

## 3. Task Breakdown Teknis

## 3.1 Backend / API

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S5-BE-001 | Implement domain events untuk booking/payment/session/withdrawal | Event bus siap notifikasi | Sprint 4 selesai |
| S5-BE-002 | Implement notification jobs (queue) untuk email + in-app | Dispatch notifikasi otomatis | S5-BE-001 |
| S5-BE-003 | Implement scheduler reminder H-1 dan H-0 | Reminder tepat waktu | S5-BE-002 |
| S5-BE-004 | Implement endpoint list/read notifications (`GET /api/v1/notifications`, `PATCH /api/v1/notifications/{id}/read`) | Notification center siap | S5-BE-002 |
| S5-BE-005 | Implement metrics aggregation service (booking conversion, payment success rate, api error rate) | Data monitoring tersedia | S5-BE-001 |
| S5-BE-006 | Tambahkan rate limiting endpoint sensitif (auth/payment/webhook) | Proteksi abuse aktif | Sprint 3 selesai |
| S5-BE-007 | Hardening authorization audit coverage untuk action admin/therapist | Kontrol akses tervalidasi | Sprint 4 selesai |
| S5-BE-008 | Optimasi query endpoint kritis (dashboard, booking list, payments list) | Response time membaik | S5-BE-005 |
| S5-BE-009 | Tambah health endpoint internal dan readiness check | Readiness monitoring tersedia | S5-BE-005 |

## 3.2 Frontend (Inertia + React TSX)

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S5-FE-001 | Implement notification bell + unread badge | In-app notification UX aktif | S5-BE-004 |
| S5-FE-002 | Implement halaman daftar notifikasi per role | Notifikasi terpusat | S5-BE-004 |
| S5-FE-003 | Implement CTA reminder ke halaman detail sesi/booking | Reminder actionable | S5-BE-003 |
| S5-FE-004 | Implement admin monitoring view ringkas (kpi cards + trend) | Monitoring operasional tersedia | S5-BE-005 |
| S5-FE-005 | Perbaikan UX error state dan loading state endpoint kritis | Stabilitas UX meningkat | S5-BE-008 |

## 3.3 Database

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S5-DB-001 | Validasi struktur tabel notifications untuk volume produksi | Notifikasi siap skala awal | Sprint 4 selesai |
| S5-DB-002 | Tambah index operasional (`user_id`, `is_read`, `created_at`) pada notifications | Query notifikasi optimal | S5-DB-001 |
| S5-DB-003 | Review index activity_logs untuk query audit cepat | Audit query lebih cepat | Sprint 4 selesai |
| S5-DB-004 | Cleanup/retention policy awal untuk logs dan notifications | Data growth terkendali | S5-DB-003 |

## 3.4 QA / Testing

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S5-QA-001 | Feature test notifikasi event booking/payment | Notifikasi domain tervalidasi | S5-BE-002 |
| S5-QA-002 | Feature test reminder H-1/H-0 scheduler | Reminder terjadwal valid | S5-BE-003 |
| S5-QA-003 | Feature test mark notification as read | Status unread konsisten | S5-BE-004 |
| S5-QA-004 | Security test role access + rate limit | Hardening security tervalidasi | S5-BE-006 |
| S5-QA-005 | Performance smoke test endpoint kritis | Baseline performa tervalidasi | S5-BE-008 |
| S5-QA-006 | UAT full critical journey (guest/client/therapist/admin) | Go-live confidence | S5-ST-07 |

## 3.5 DevOps / Release

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S5-OPS-001 | Setup log aggregation minimum untuk error tracking | Observability dasar aktif | S5-BE-005 |
| S5-OPS-002 | Setup alert threshold (payment webhook failure, api error spike) | Alerting aktif | S5-OPS-001 |
| S5-OPS-003 | Finalisasi deployment runbook dan rollback plan | Go-live playbook siap | S5-ST-08 |
| S5-OPS-004 | Dry run deployment staging -> production-like | Risiko release menurun | S5-OPS-003 |

---

## 4. Acceptance Criteria Sprint 5

```gherkin
Scenario: Notifikasi booking terkirim otomatis
  Given booking baru berhasil dibuat
  When event booking_created diproses
  Then sistem mengirim notifikasi email dan in-app ke pihak terkait
```

```gherkin
Scenario: Reminder sesi H-1 berjalan
  Given client memiliki sesi besok
  When scheduler reminder H-1 dijalankan
  Then client menerima reminder dengan CTA menuju detail sesi
```

```gherkin
Scenario: Notification center menandai notifikasi dibaca
  Given user memiliki notifikasi unread
  When user menandai notifikasi sebagai read
  Then unread badge berkurang sesuai jumlah notifikasi yang dibaca
```

```gherkin
Scenario: Endpoint sensitif terkena rate limit
  Given client mengirim request berlebih ke endpoint auth
  When batas request terlampaui
  Then sistem mengembalikan response rate limited
```

```gherkin
Scenario: UAT critical journey lulus
  Given sistem siap UAT
  When tim QA menjalankan skenario lintas role
  Then semua skenario critical lulus tanpa blocker
```

---

## 5. Deliverables Sprint 5

1. Notification system event-driven aktif.
2. Reminder H-1/H-0 aktif melalui scheduler + queue.
3. Monitoring metrik inti dan alert minimum aktif.
4. Security/performance hardening baseline terpenuhi.
5. UAT report final + release checklist + runbook deployment.

---

## 6. Non-Goal Sprint 5

1. Implementasi mobile app native.
2. Implementasi live consultation phase 2A.
3. AI recommendation dan advanced analytics lanjutan.
4. Integrasi payment method baru di luar policy PRD.

---

## 7. Definition of Done Sprint 5

1. Semua story P1 selesai, test lulus, dan tanpa blocker terbuka.
2. Critical flow end-to-end lulus UAT.
3. Monitoring dan alert minimum berjalan stabil.
4. Runbook release dan rollback tervalidasi lewat dry-run.
5. Tim menyatakan V1 siap go-live.

---

## 8. Handoff ke Phase 2A (Opsional, Non-Priority)

Prerequisite untuk mulai phase 2A live consultation:

1. V1 sudah stabil pasca go-live minimal 1 siklus operasional.
2. Metrik baseline operasional tersedia untuk evaluasi kapasitas tim.
3. Incident rate payment/booking berada dalam batas aman.
4. Alokasi resource phase 2A disetujui stakeholder.
