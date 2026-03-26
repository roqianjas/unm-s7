# Backlog Implementasi Phase 2A

## Live Consultation via Jitsi (Gratis-First)

**Produk**: CUR-HEART  
**Dokumen Turunan**: PRD V1 (`07_PRD_CURHEART_V1.md`)  
**Fokus**: Menyiapkan live consultation non-priority setelah V1 stabil  
**Prioritas**: P3  

---

## 1. Ringkasan

Dokumen ini memecah roadmap Phase 2A menjadi backlog implementasi yang siap dikerjakan tim produk/dev.

Keputusan utama:

1. Tidak membangun engine video internal.
2. Mengintegrasikan layanan eksternal dengan default **Jitsi** (gratis).
3. Tetap mempertahankan arsitektur provider-agnostic agar bisa pindah provider jika dibutuhkan.

---

## 2. Scope Phase 2A

## 2.1 In-Scope

1. Integrasi meeting room online 1:1 untuk sesi terjadwal.
2. Join flow dari dashboard client/therapist.
3. Logging event join/leave/fail untuk operasional.
4. Reminder dan CTA join sesi.
5. Consent dan kebijakan privasi sebelum masuk room.

## 2.2 Out-of-Scope

1. Engine WebRTC internal.
2. Group call (lebih dari 2 partisipan inti).
3. Recording server-side bawaan platform.
4. Fitur billing usage real-time lintas provider.

---

## 3. Rencana Sprint (High-Level)

| Sprint | Fokus | Output |
|---|---|---|
| Sprint 1 | Core meeting flow | Join page, room generation, start/end session |
| Sprint 2 | Security & UX | Access guard, consent, reminder, fallback handling |
| Sprint 3 | Observability & rollout | Event metrics, dashboard monitoring, pilot release |

---

## 4. Epic Map

| Epic ID | Epic | Prioritas | Target Sprint |
|---|---|---|---|
| EP-LC-01 | Integrasi Sesi Online dengan Jitsi | P1 (dalam Phase 2A) | Sprint 1 |
| EP-LC-02 | Security, Access Control, dan Consent | P1 | Sprint 2 |
| EP-LC-03 | Reminder, UX Flow, dan Fallback | P2 | Sprint 2 |
| EP-LC-04 | Observability dan Operasional | P2 | Sprint 3 |
| EP-LC-05 | Pilot Rollout dan Stabilization | P2 | Sprint 3 |

Catatan: Prioritas P1/P2 di atas adalah prioritas internal dalam Phase 2A, sementara Phase 2A tetap P3 terhadap PRD V1.

---

## 5. User Stories dan Acceptance Criteria

## 5.1 EP-LC-01 Integrasi Sesi Online dengan Jitsi

| Story ID | User Story | Priority | Estimasi |
|---|---|---|---|
| US-LC-001 | Sebagai therapist, saya ingin sistem menyiapkan room meeting otomatis untuk sesi online agar saya tidak membuat link manual. | P1 | 5 SP |
| US-LC-002 | Sebagai client, saya ingin tombol join dari detail sesi agar masuk konsultasi lebih cepat. | P1 | 3 SP |
| US-LC-003 | Sebagai therapist, saya ingin menandai sesi dimulai/selesai agar status sesi sinkron dengan proses terapi. | P1 | 3 SP |

Acceptance Criteria:

```gherkin
Scenario: Room meeting otomatis dibuat
  Given booking online berstatus paid/confirmed
  When sesi H-1 mencapai waktu preparation window
  Then sistem menyediakan meeting context untuk sesi tersebut
```

```gherkin
Scenario: Client join dari detail sesi
  Given client memiliki sesi online aktif
  When client menekan tombol "Join Session"
  Then client diarahkan ke halaman meeting room yang valid
```

## 5.2 EP-LC-02 Security, Access Control, dan Consent

| Story ID | User Story | Priority | Estimasi |
|---|---|---|---|
| US-LC-101 | Sebagai sistem, saya ingin hanya client dan therapist yang terdaftar pada sesi yang bisa join room. | P1 | 5 SP |
| US-LC-102 | Sebagai pengguna, saya ingin melihat consent privasi sebelum join sesi online. | P1 | 2 SP |
| US-LC-103 | Sebagai admin, saya ingin ada guard join window agar akses room tidak terbuka tanpa batas. | P1 | 3 SP |

Acceptance Criteria:

```gherkin
Scenario: Unauthorized user ditolak
  Given user tidak terasosiasi dengan sesi
  When user mengakses endpoint join context
  Then sistem mengembalikan 403 forbidden
```

```gherkin
Scenario: Consent wajib sebelum join
  Given user valid untuk sesi online
  When user belum menyetujui consent
  Then tombol join tidak aktif sampai consent disetujui
```

## 5.3 EP-LC-03 Reminder, UX Flow, dan Fallback

| Story ID | User Story | Priority | Estimasi |
|---|---|---|---|
| US-LC-201 | Sebagai client, saya ingin reminder H-1/H-0 berisi CTA join sesi agar tidak terlambat. | P2 | 3 SP |
| US-LC-202 | Sebagai therapist, saya ingin pre-join checklist mic/camera agar sesi lebih lancar. | P2 | 3 SP |
| US-LC-203 | Sebagai pengguna, saya ingin fallback link eksternal jika embed gagal agar sesi tetap berjalan. | P2 | 3 SP |

Acceptance Criteria:

```gherkin
Scenario: Reminder berisi CTA join
  Given sesi online akan dimulai
  When jadwal reminder berjalan
  Then notifikasi mengandung tombol "Join Session"
```

```gherkin
Scenario: Embed gagal, fallback aktif
  Given halaman room gagal load dalam batas waktu
  When user memilih fallback
  Then sistem membuka session_link eksternal yang sama
```

## 5.4 EP-LC-04 Observability dan Operasional

| Story ID | User Story | Priority | Estimasi |
|---|---|---|---|
| US-LC-301 | Sebagai admin, saya ingin event join/leave/fail tercatat agar bisa audit dan troubleshooting. | P2 | 5 SP |
| US-LC-302 | Sebagai manajemen, saya ingin metrik join success rate untuk menilai kualitas layanan online. | P2 | 3 SP |
| US-LC-303 | Sebagai support, saya ingin status sesi online terlihat di dashboard agar bisa bantu cepat saat kendala. | P2 | 3 SP |

Acceptance Criteria:

```gherkin
Scenario: Event sesi tercatat
  Given user masuk/keluar room
  When event terjadi
  Then sistem menyimpan event dengan timestamp, session_id, actor, dan event_type
```

## 5.5 EP-LC-05 Pilot Rollout dan Stabilization

| Story ID | User Story | Priority | Estimasi |
|---|---|---|---|
| US-LC-401 | Sebagai product owner, saya ingin rollout bertahap ke sebagian therapist/client dulu agar risiko terkendali. | P2 | 2 SP |
| US-LC-402 | Sebagai admin, saya ingin kill-switch fitur live consultation agar bisa rollback cepat saat incident. | P2 | 2 SP |
| US-LC-403 | Sebagai tim QA, saya ingin checklist UAT khusus live consultation sebelum full release. | P2 | 2 SP |

Acceptance Criteria:

```gherkin
Scenario: Feature flag rollout
  Given fitur live consultation diaktifkan terbatas
  When user di luar segmen pilot mencoba akses
  Then sistem tetap menampilkan flow session_link standar
```

---

## 6. Backlog Teknis per Subsystem

## 6.1 Backend (Laravel 12)

1. Tambah service `MeetingProviderInterface` + adapter `JitsiProvider`.
2. Endpoint API:
   - `GET /api/v1/sessions/{id}/join-context`
   - `POST /api/v1/sessions/{id}/start`
   - `POST /api/v1/sessions/{id}/end`
   - `POST /api/v1/sessions/{id}/events`
3. Policy authorization join berdasarkan relasi sesi.
4. Logging event ke `activity_logs` (payload JSON terstruktur).
5. Feature flag untuk pilot rollout.

## 6.2 Frontend (Inertia + React TSX)

1. Halaman `SessionRoomPage` untuk client/therapist.
2. Komponen pre-join checks (mic/camera/network hint).
3. Komponen embed Jitsi + fallback open external link.
4. Consent modal sebelum join.
5. Status panel: connecting, in-session, disconnected, ended.

## 6.3 Notifikasi

1. Template reminder H-1/H-0 dengan join CTA.
2. Notifikasi in-app saat sesi dimulai.
3. Notifikasi fallback jika join gagal.

## 6.4 Dashboard Operasional

1. Widget metrik: join success rate, join fail rate, average online session duration.
2. Tabel incident ringan: sesi gagal join > threshold.

---

## 7. Perubahan API Contract (Phase 2A)

## 7.1 Join Context Response (Contoh)

```json
{
  "success": true,
  "message": "Join context fetched",
  "data": {
    "session_id": 123,
    "provider": "jitsi",
    "room_name": "curheart-s-123-8f3ab1",
    "display_name": "Client Name",
    "role": "client",
    "join_window": {
      "starts_at": "2026-06-01T09:45:00+07:00",
      "ends_at": "2026-06-01T11:30:00+07:00"
    },
    "fallback_url": "https://meet.jit.si/curheart-s-123-8f3ab1"
  }
}
```

## 7.2 Event Payload (Contoh)

```json
{
  "event_type": "join_success",
  "occurred_at": "2026-06-01T10:02:13+07:00",
  "client_meta": {
    "device": "desktop",
    "browser": "chrome"
  }
}
```

---

## 8. Definisi Done Phase 2A

Phase 2A dianggap selesai bila:

1. Story P1 selesai dan lulus UAT.
2. Event join/leave/fail terekam untuk >= 95% sesi online pilot.
3. Join success rate pilot mencapai threshold minimum yang disepakati produk.
4. Fallback flow berjalan saat embed gagal.
5. Tidak ada perubahan pada kebijakan payment/no-wallet di PRD V1.

---

## 9. Risiko dan Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Limit layanan gratis tercapai | Sesi online terganggu | Fallback provider plan (upgrade/pindah vendor) |
| Kualitas jaringan user buruk | Pengalaman sesi menurun | Pre-join checks + fallback link |
| Incident provider eksternal | Downtime fitur live | Feature flag rollback ke flow link standar |
| Event logging kurang lengkap | Sulit troubleshooting | Event schema wajib + QA checklist observability |

---

## 10. Catatan Implementasi

1. Fase ini tidak mengubah prioritas V1; eksekusi setelah V1 stabil.
2. Keputusan provider tetap bisa direview ulang saat sprint planning.
3. Jika compliance/scale menuntut kontrol lebih tinggi, baru evaluasi jalur internal sebagai exceptional case.

