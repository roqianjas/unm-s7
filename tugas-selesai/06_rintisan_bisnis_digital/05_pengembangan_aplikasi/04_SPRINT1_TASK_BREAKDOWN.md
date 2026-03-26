# Sprint 1 Task Breakdown

## CUR-HEART V1 - E0 (Foundation) + E1 (Public & Auth)

Durasi sprint (disarankan): 2 minggu  
Fokus: menyiapkan fondasi aplikasi Laravel 12 + Inertia React TSX dan menyelesaikan public/auth flow dasar.

---

## 1. Target Sprint 1

1. Project Laravel 12 + Inertia + React TSX berjalan stabil di local dev.
2. Struktur role-based access (`guest/client/therapist/admin`) aktif.
3. Public pages utama tampil (minimal skeleton siap konten).
4. Auth dasar selesai: register, login, logout, forgot/reset password.
5. Baseline database siap untuk iterasi sprint 2.

---

## 2. Sprint Backlog (Story Level)

| Story ID | Story | Prioritas | Estimasi |
|---|---|---|---|
| S1-ST-01 | Bootstrap project dan konfigurasi environment pengembangan | P1 | 5 SP |
| S1-ST-02 | Implementasi layout Inertia + route grouping web/app/admin | P1 | 3 SP |
| S1-ST-03 | Implementasi role-permission dan route middleware | P1 | 5 SP |
| S1-ST-04 | Implementasi public pages dasar | P1 | 5 SP |
| S1-ST-05 | Implementasi auth (register/login/forgot-reset/logout) | P1 | 8 SP |
| S1-ST-06 | Setup baseline database, seed role, seed system settings awal | P1 | 5 SP |
| S1-ST-07 | Testing dan quality gate sprint 1 | P1 | 5 SP |

---

## 3. Task Breakdown Teknis

## 3.1 Backend / API

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S1-BE-001 | Inisialisasi project Laravel 12 + Breeze React TS | Project bootstrapped | - |
| S1-BE-002 | Setup environment `.env.example` standar tim | Template env siap pakai | S1-BE-001 |
| S1-BE-003 | Setup route group: `web`, `app`, `admin` | Route map jelas | S1-BE-001 |
| S1-BE-004 | Buat middleware role guard (`client`, `therapist`, `admin`) | Proteksi akses aktif | S1-BE-003 |
| S1-BE-005 | Setup auth flow Laravel Breeze + kustom role assignment register | Register/login sesuai role | S1-BE-001 |
| S1-BE-006 | Implement forgot/reset password flow end-to-end | Reset password aktif | S1-BE-005 |
| S1-BE-007 | Tambahkan endpoint `GET /api/v1/auth/me` (baseline mobile-ready) | Auth profile API siap | S1-BE-005 |
| S1-BE-008 | Seed data role dan user dummy internal | Akun dev siap test | S1-BE-006 |

## 3.2 Frontend (Inertia + React TSX)

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S1-FE-001 | Setup shared layout (public/app/admin) | Reusable layout components | S1-BE-003 |
| S1-FE-002 | Setup design token dasar (warna, typography, spacing) | Konsistensi UI awal | S1-FE-001 |
| S1-FE-003 | Implement public pages skeleton: home, services, therapists, blog, faq, contact | Navigasi publik berjalan | S1-FE-001 |
| S1-FE-004 | Implement halaman auth UI: login/register/forgot/reset | Auth screens siap | S1-BE-005 |
| S1-FE-005 | Guard navigation berdasarkan role (menu kondisional) | Menu role-based | S1-BE-004 |
| S1-FE-006 | Implement state/error handling form auth | UX form stabil | S1-FE-004 |

## 3.3 Database

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S1-DB-001 | Sinkronisasi migration baseline untuk tabel inti identitas (`users`, `clients`, `therapists`) | Tabel identitas siap | S1-BE-001 |
| S1-DB-002 | Migration `system_settings` baseline | Konfigurasi sistem awal | S1-BE-001 |
| S1-DB-003 | Seeder role + system settings minimum | Data awal konsisten | S1-DB-001 |
| S1-DB-004 | Validasi constraint unik email + role consistency | Integritas auth | S1-DB-001 |

## 3.4 QA / Testing

| Task ID | Task | Output | Dependency |
|---|---|---|---|
| S1-QA-001 | Feature test register/login/logout | Test auth green | S1-BE-005 |
| S1-QA-002 | Feature test forgot/reset password | Test recovery green | S1-BE-006 |
| S1-QA-003 | Feature test role middleware (allow/deny) | Proteksi route tervalidasi | S1-BE-004 |
| S1-QA-004 | UI smoke test public pages | Navigasi publik stabil | S1-FE-003 |
| S1-QA-005 | API test `/api/v1/auth/me` | Baseline mobile-ready tervalidasi | S1-BE-007 |

---

## 4. Acceptance Criteria Sprint 1

```gherkin
Scenario: User register sebagai client
  Given pengunjung berada di halaman register
  When pengunjung mengisi data valid dan submit
  Then akun client berhasil dibuat
  And pengguna diarahkan ke area app client
```

```gherkin
Scenario: Route admin tidak bisa diakses non-admin
  Given user login sebagai client
  When user mengakses route admin
  Then sistem mengembalikan forbidden atau redirect aman
```

```gherkin
Scenario: Forgot password flow berhasil
  Given user memiliki akun aktif
  When user request reset password dan submit token valid
  Then password diperbarui
  And user dapat login dengan password baru
```

```gherkin
Scenario: Public pages dapat diakses tanpa login
  Given pengunjung belum login
  When membuka halaman publik utama
  Then semua halaman public tampil tanpa error server
```

```gherkin
Scenario: Endpoint auth me mengembalikan profile user
  Given user login valid
  When user memanggil GET /api/v1/auth/me
  Then sistem mengembalikan data user sesuai role
```

---

## 5. Deliverables Sprint 1

1. Codebase foundation siap lanjut ke Sprint 2 (booking/scheduling).
2. Dokumen route map web + app + admin.
3. Dokumen akun dummy dev/test.
4. Test report sprint 1 (auth + access control + public smoke).

---

## 6. Non-Goal Sprint 1

1. Booking wizard 4 langkah.
2. Integrasi payment Midtrans.
3. Session documentation.
4. Dashboard operasional penuh.

---

## 7. Definition of Done Sprint 1

1. Semua story sprint berstatus done dan teruji.
2. Tidak ada bug blocker pada auth/public pages.
3. Lint/build/test utama lulus.
4. Dokumentasi setup lokal terbarui.
5. Tidak ada pelanggaran kebijakan payment/no-wallet PRD (meski payment belum diimplementasi).

---

## 8. Handoff ke Sprint 2

Prerequisite untuk mulai Sprint 2:

1. Role middleware dan route guard stabil.
2. Struktur database identitas siap dipakai modul booking.
3. API auth baseline sudah berjalan.
4. UI layout siap dipakai flow wizard booking.
