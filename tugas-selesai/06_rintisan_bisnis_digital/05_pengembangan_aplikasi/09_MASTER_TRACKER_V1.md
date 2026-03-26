# Master Tracker V1

## CUR-HEART - Progress Matrix dan Control Board

Dokumen ini dipakai sebagai tracker harian/mingguan lintas sprint.

## Referensi

1. `05_pengembangan_aplikasi/00_PRD_CURHEART_V1.md`
2. `05_pengembangan_aplikasi/03_BACKLOG_MVP_V1.md`
3. `05_pengembangan_aplikasi/04_SPRINT1_TASK_BREAKDOWN.md`
4. `05_pengembangan_aplikasi/05_SPRINT2_TASK_BREAKDOWN.md`
5. `05_pengembangan_aplikasi/06_SPRINT3_TASK_BREAKDOWN.md`
6. `05_pengembangan_aplikasi/07_SPRINT4_TASK_BREAKDOWN.md`
7. `05_pengembangan_aplikasi/08_SPRINT5_TASK_BREAKDOWN.md`
8. `05_pengembangan_aplikasi/00_BACKLOG_PHASE2A_LIVE_CONSULTATION_JITSI.md`

---

## 1. Status Legend

| Code | Status |
|---|---|
| NS | Not Started |
| IP | In Progress |
| BLK | Blocked |
| RVW | In Review/QA |
| DONE | Completed |

---

## 2. Sprint Overview Board

| Sprint | Epic Scope | Goal Ringkas | Owner PO | Owner Tech Lead | Rencana Waktu | Status | Progress % | Blocker Utama | Next Checkpoint |
|---|---|---|---|---|---|---|---:|---|---|
| Sprint 1 | E0 + E1 | Foundation + Public/Auth | TBD | TBD | TBD | NS | 0 | - | Kickoff setup stack |
| Sprint 2 | E2 | Booking + Scheduling | TBD | TBD | TBD | NS | 0 | - | Wizard booking siap QA |
| Sprint 3 | E3 | Payment + Finance Control | TBD | TBD | TBD | NS | 0 | - | Webhook idempotent pass |
| Sprint 4 | E4 + E5 | Therapist Workflow + Admin Operation | TBD | TBD | TBD | NS | 0 | - | Withdrawal lifecycle pass |
| Sprint 5 | E6 + Hardening | Notification + Monitoring + Release Readiness | TBD | TBD | TBD | NS | 0 | - | UAT final + go-live gate |
| Phase 2A | Live Consultation | Jitsi integration (non-priority) | TBD | TBD | TBD | NS | 0 | - | Pilot enablement |

---

## 3. Workstream Tracker

### 3.1 Product

| Item | Sprint | PIC | Status | Notes |
|---|---|---|---|---|
| Finalisasi acceptance criteria per sprint | 1-5 | TBD | NS | Sinkron dengan PRD |
| Sign-off policy payment no wallet | 3 | TBD | NS | VA/Bank + Card only |
| UAT scenario lintas role | 5 | TBD | NS | Guest/client/therapist/admin |

### 3.2 Backend

| Item | Sprint | PIC | Status | Notes |
|---|---|---|---|---|
| Role middleware + auth API baseline | 1 | TBD | NS | `/api/v1/auth/me` |
| Booking conflict detection | 2 | TBD | NS | Atomic validation |
| Midtrans checkout + webhook idempotent | 3 | TBD | NS | Signature verification wajib |
| Session notes + withdrawal endpoints | 4 | TBD | NS | Payable-based |
| Notification pipeline + hardening | 5 | TBD | NS | Queue + scheduler |

### 3.3 Frontend

| Item | Sprint | PIC | Status | Notes |
|---|---|---|---|---|
| Public pages + auth screens | 1 | TBD | NS | Inertia React TSX |
| Booking wizard 4 langkah | 2 | TBD | NS | Persist draft state |
| Payment status + retry flow | 3 | TBD | NS | Jangan tampilkan e-wallet/QRIS |
| Therapist/admin operation screens | 4 | TBD | NS | Notes + withdrawals + KPI |
| Notification center + monitoring UI | 5 | TBD | NS | Unread badge + list |

### 3.4 QA/Testing

| Item | Sprint | PIC | Status | Notes |
|---|---|---|---|---|
| Auth/public smoke test | 1 | TBD | NS | Critical access control |
| Booking E2E + policy tests | 2 | TBD | NS | Conflict + reschedule/cancel |
| Payment callback/security tests | 3 | TBD | NS | Signature + duplicate callback |
| Therapist-admin flow tests | 4 | TBD | NS | Withdrawal lifecycle |
| UAT final + regression | 5 | TBD | NS | Go-live confidence |

---

## 4. Risk Register

| Risk ID | Risiko | Dampak | Probabilitas | Mitigasi | Owner | Status |
|---|---|---|---|---|---|---|
| R-01 | Scope creep lintas sprint | High | Medium | Kunci scope per sprint, change request terpisah | TBD | NS |
| R-02 | Delay integrasi payment | High | Medium | Sandbox test lebih awal + fallback plan | TBD | NS |
| R-03 | Bug di role authorization | High | Medium | Feature test akses lintas role | TBD | NS |
| R-04 | Query lambat saat data tumbuh | Medium | Medium | Index review + profiling endpoint kritis | TBD | NS |
| R-05 | Ketergantungan provider eksternal live consultation | Medium | Low | Tetap non-priority, pilot bertahap | TBD | NS |

---

## 5. Decision Log

| Date | Decision | Rationale | Impact | Owner |
|---|---|---|---|---|
| 2026-03-16 | Stack V1: Laravel 12 + Inertia + React TSX | Konsisten dengan arah arsitektur PRD | Menentukan foundation sprint 1 | Team |
| 2026-03-16 | Payment policy: VA/Bank + Card only | Mengurangi risiko dan pertanyaan finance | Mempengaruhi UI/checkout/webhook logic | Team |
| 2026-03-16 | No wallet model | Sederhana dan audit-friendly | Payout pakai withdrawal flow | Team |
| 2026-03-16 | Live consultation phase 2A via external service | Faster delivery, low cost | Non-priority, tidak ganggu V1 | Team |

---

## 6. Weekly Standup Template

Gunakan format ini untuk update mingguan:

```text
Periode: [YYYY-MM-DD s/d YYYY-MM-DD]
Sprint aktif: [Sprint X]

Done minggu ini:
- ...

In progress:
- ...

Blocker:
- ...

Plan minggu depan:
- ...

Need decision:
- ...
```

---

## 7. Go-Live Gate Checklist (Ringkas)

| Gate | Kriteria | Status | Catatan |
|---|---|---|---|
| G-01 | Must-have PRD selesai | NS | |
| G-02 | Critical journey pass UAT | NS | |
| G-03 | Payment policy compliance pass | NS | |
| G-04 | Monitoring + alert minimum aktif | NS | |
| G-05 | Runbook deployment + rollback siap | NS | |


