# Sprint 4 Task Breakdown

## CUR-HEART V1 - E4 (Therapist Session Workflow) + E5 (Admin Operation)

Durasi sprint (disarankan): 2 minggu  
Fokus: implementasi alur kerja terapis (session notes + earnings/withdrawal) dan operasi admin (KPI dashboard, CRUD inti, reporting dasar, processing payout).

---

## 1. Target Sprint 4

1. Terapis dapat mengelola sesi, dokumentasi terapi, dan histori klien.
2. Terapis dapat mengajukan withdrawal berbasis payable (tanpa wallet).
3. Admin memiliki visibilitas KPI operasional dan transaksi utama.
4. Admin dapat mengelola data inti: users, services, bookings.
5. Admin dapat memproses request withdrawal dengan jejak audit lengkap.

---

## 2. Sprint Backlog (Story Level)

| Story ID | Story | Prioritas | Estimasi |
|---|---|---|---|
| S4-ST-01 | Implement dashboard terapis (jadwal, klien, ringkasan sesi) | P1 | 5 SP |
| S4-ST-02 | Implement session documentation dengan auto-save | P1 | 8 SP |
| S4-ST-03 | Implement therapist earnings + request withdrawal | P1 | 8 SP |
| S4-ST-04 | Implement admin dashboard KPI operasional | P1 | 5 SP |
| S4-ST-05 | Implement CRUD inti admin (users/services/bookings) | P1 | 8 SP |
| S4-ST-06 | Implement proses withdrawal admin (approve/reject/process) | P1 | 8 SP |
| S4-ST-07 | Implement reporting/export dasar untuk admin | P2 | 5 SP |
| S4-ST-08 | Test coverage workflow therapist-admin | P1 | 5 SP |

---

## 3. Task Breakdown Teknis

## 3.1 Backend / API

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S4-BE-001 | Implement endpoint therapist dashboard summary (`GET /api/v1/therapist/dashboard`) | Ringkasan data therapist tersedia | Sprint 3 selesai |
| S4-BE-002 | Implement endpoint daftar sesi therapist (`GET /api/v1/sessions?role=therapist`) | Jadwal sesi dapat difilter | S4-BE-001 |
| S4-BE-003 | Implement endpoint create/update session notes (`POST/PUT /api/v1/sessions/{id}/notes`) | Dokumentasi sesi tersimpan | S4-BE-002 |
| S4-BE-004 | Implement auto-save notes endpoint (`PATCH /api/v1/sessions/{id}/notes/draft`) | Draft notes aman | S4-BE-003 |
| S4-BE-005 | Implement endpoint therapist earnings summary (`GET /api/v1/therapist/earnings`) | Dasar payable therapist tersedia | S4-BE-001 |
| S4-BE-006 | Implement create withdrawal request (`POST /api/v1/withdrawals`) dengan validasi payable | Request payout therapist aktif | S4-BE-005 |
| S4-BE-007 | Implement admin KPI dashboard endpoint (`GET /api/v1/admin/dashboard`) | KPI admin tersedia | Sprint 3 selesai |
| S4-BE-008 | Implement admin CRUD users/services/bookings | Operasi data inti berjalan | S4-BE-007 |
| S4-BE-009 | Implement withdrawal decision endpoints (`approve/reject/process`) | Lifecycle payout admin aktif | S4-BE-006 |
| S4-BE-010 | Implement reporting endpoint dasar + export trigger | Reporting admin tersedia | S4-BE-007 |
| S4-BE-011 | Tambahkan audit log untuk notes dan withdrawal status change | Jejak audit lengkap | S4-BE-003 |

## 3.2 Frontend (Inertia + React TSX)

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S4-FE-001 | Implement halaman dashboard therapist | KPI dan agenda therapist tampil | S4-BE-001 |
| S4-FE-002 | Implement halaman session room + notes form therapist | Dokumentasi sesi usable | S4-BE-003 |
| S4-FE-003 | Implement indikator auto-save dan draft state | UX notes aman | S4-BE-004 |
| S4-FE-004 | Implement halaman earnings therapist | Transparansi payable therapist | S4-BE-005 |
| S4-FE-005 | Implement form withdrawal request therapist | Request payout dari therapist | S4-BE-006 |
| S4-FE-006 | Implement halaman admin dashboard KPI | Monitoring operasional admin | S4-BE-007 |
| S4-FE-007 | Implement admin pages CRUD users/services/bookings | Operasi data admin lengkap | S4-BE-008 |
| S4-FE-008 | Implement admin withdrawals page + detail + action buttons | Proses payout admin berjalan | S4-BE-009 |
| S4-FE-009 | Implement halaman reporting/export dasar | Report basic admin | S4-BE-010 |

## 3.3 Database

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S4-DB-001 | Finalisasi tabel session domain (`sessions`, `session_notes`, relasi bookings) | Data sesi siap produksi | Sprint 3 selesai |
| S4-DB-002 | Validasi tabel withdrawal dan relasi therapist/users | Payout flow konsisten | Sprint 3 selesai |
| S4-DB-003 | Tambah index query notes/withdrawals (`session_id`, `therapist_id`, `status`) | Performa query stabil | S4-DB-001 |
| S4-DB-004 | Seeder data sesi dan withdrawal dummy untuk QA | Data test coverage tersedia | S4-DB-001 |

## 3.4 QA / Testing

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S4-QA-001 | Feature test create/update session notes | Notes workflow tervalidasi | S4-BE-003 |
| S4-QA-002 | Feature test auto-save notes | Draft notes tervalidasi | S4-BE-004 |
| S4-QA-003 | Feature test withdrawal request validation | Payout request aman | S4-BE-006 |
| S4-QA-004 | Feature test admin approve/reject/process withdrawal | Lifecycle payout tervalidasi | S4-BE-009 |
| S4-QA-005 | Feature test role access (therapist/admin) di module operation | Security access tervalidasi | S4-BE-008 |
| S4-QA-006 | UI E2E test therapist session documentation flow | UX therapist stabil | S4-FE-002 |
| S4-QA-007 | UI E2E test admin withdrawal processing flow | UX admin stabil | S4-FE-008 |

---

## 4. Acceptance Criteria Sprint 4

```gherkin
Scenario: Therapist menyimpan catatan sesi
  Given therapist memiliki sesi yang valid
  When therapist mengisi catatan sesi dan menyimpan
  Then catatan sesi tersimpan
  And status sesi diperbarui sesuai alur
```

```gherkin
Scenario: Auto-save catatan sesi aktif
  Given therapist sedang mengisi formulir catatan
  When interval auto-save tercapai
  Then draft catatan tersimpan tanpa submit final
```

```gherkin
Scenario: Therapist mengajukan withdrawal
  Given therapist memiliki payable eligible
  And data rekening bank valid
  When therapist submit permintaan payout
  Then sistem membuat withdrawal berstatus pending
```

```gherkin
Scenario: Admin memproses withdrawal
  Given ada withdrawal berstatus approved
  When admin melakukan process dengan reference transfer
  Then status menjadi processed
  And aktivitas tercatat di audit log
```

```gherkin
Scenario: Admin mengelola booking dari dashboard
  Given admin login dengan role valid
  When admin memperbarui data booking
  Then perubahan tersimpan
  And perubahan tercatat pada audit log
```

---

## 5. Deliverables Sprint 4

1. Therapist dashboard + session documentation + auto-save aktif.
2. Therapist earnings + withdrawal request berjalan tanpa wallet.
3. Admin dashboard KPI dan CRUD inti berfungsi.
4. Admin withdrawal processing lifecycle aktif.
5. Reporting/export dasar tersedia.

---

## 6. Non-Goal Sprint 4

1. Notifikasi reminder lengkap H-1/H-0 berbasis queue advanced.
2. Monitoring dashboard teknis full observability.
3. Live consultation integration (phase 2A).
4. Mobile app implementation.

---

## 7. Definition of Done Sprint 4

1. Semua story P1 selesai dan lulus QA.
2. Workflow therapist-admin tidak memiliki bug blocker.
3. Withdrawal flow sesuai PRD (payable-based, no wallet).
4. Audit log untuk operasi penting aktif.
5. Siap handoff ke Sprint 5 (Notification + Monitoring + Hardening).

---

## 8. Handoff ke Sprint 5

Prerequisite untuk mulai Sprint 5:

1. Event utama booking/payment/withdrawal sudah tercatat stabil.
2. Endpoint notifikasi dapat dihook ke event domain.
3. KPI dashboard memiliki sumber data konsisten.
4. Security baseline role access sudah stabil.
