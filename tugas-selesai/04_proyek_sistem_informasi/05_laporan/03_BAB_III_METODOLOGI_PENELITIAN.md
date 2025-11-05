# BAB III  
# METODOLOGI PENELITIAN

## 3.1 Tahapan Penelitian

Penelitian dan pengembangan sistem informasi manajemen pemesanan dan terapi CUR-HEART menggunakan pendekatan ***System Development Life Cycle* (SDLC)** dengan model ***Waterfall***. Model ini dipilih karena karakteristik proyek yang memiliki kebutuhan jelas, waktu yang tetap (semester akademik), dan memerlukan dokumentasi yang komprehensif untuk keperluan akademik. Tahapan penelitian terdiri dari enam fase utama yang dilaksanakan secara berurutan dengan keluaran yang terdefinisi jelas di setiap fase.

---

**[GAMBAR 3.1 - Flowchart Metodologi Penelitian]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN FLOWCHART METODOLOGI PENELITIAN]               │
│                                                             │
│   Alur (atas ke bawah):                                    │
│                                                             │
│   MULAI (16 Sep 2024)                                      │
│     ↓                                                       │
│   ┌────────────────────────────────────────────────┐       │
│   │ 1. IDENTIFIKASI MASALAH (Minggu 1)             │       │
│   │    - Observasi CUR-HEART (7 hari)              │       │
│   │    - Wawancara pemangku kepentingan (11 orang) │       │
│   │    - Analisis proses bisnis yang ada           │       │
│   │    Keluaran: Pernyataan Masalah, Ruang Lingkup │       │
│   └────────────────────────────────────────────────┘       │
│     ↓                                                       │
│   ┌────────────────────────────────────────────────┐       │
│   │ 2. STUDI LITERATUR (Minggu 1-2)                │       │
│   │    - SDLC, Laravel, MySQL, UI/UX               │       │
│   │    - Sistem informasi kesehatan                │       │
│   │    - Penelitian terkait (6 jurnal)             │       │
│   │    Keluaran: BAB II Tinjauan Pustaka           │       │
│   └────────────────────────────────────────────────┘       │
│     ↓                                                       │
│   ┌────────────────────────────────────────────────┐       │
│   │ 3. ANALISIS KEBUTUHAN (Minggu 2)               │       │
│   │    - Kebutuhan fungsional (40+ kebutuhan)      │       │
│   │    - Kebutuhan non-fungsional (15+ kebutuhan)  │       │
│   │    - Studi kelayakan (Teknis, Ekonomi, Ops)    │       │
│   │    Keluaran: Dokumen SRS (30 hal)              │       │
│   └────────────────────────────────────────────────┘       │
│     ↓                                                       │
│   ┌────────────────────────────────────────────────┐       │
│   │ 4. DESAIN SISTEM (Minggu 3-4)                  │       │
│   │    - ERD (16 entitas)                          │       │
│   │    - UML (*Use Case*, *Activity*, *Sequence*)  │       │
│   │    - *Mockups* UI/UX Figma (41 halaman)        │       │
│   │    Keluaran: Dokumen Desain (115 hal)          │       │
│   └────────────────────────────────────────────────┘       │
│     ↓                                                       │
│   ┌────────────────────────────────────────────────┐       │
│   │ 5. IMPLEMENTASI (Minggu 5-8)                   │       │
│   │    - Pengembangan Laravel (60+ halaman)        │       │
│   │    - Basis data (16 tabel, migrasi)            │       │
│   │    - Integrasi *payment gateway*               │       │
│   │    Keluaran: Aplikasi Berjalan                 │       │
│   └────────────────────────────────────────────────┘       │
│     ↓                                                       │
│   ┌────────────────────────────────────────────────┐       │
│   │ 6. PENGUJIAN (Minggu 9-10)                     │       │
│   │    - Pengujian unit (30 kasus)                 │       │
│   │    - Pengujian fungsional (150 kasus)          │       │
│   │    - Pengujian kegunaan (18 pengguna, SUS)     │       │
│   │    - Persetujuan UAT                           │       │
│   │    Keluaran: Laporan Pengujian, Perbaikan Bug  │       │
│   └────────────────────────────────────────────────┘       │
│     ↓                                                       │
│   ┌────────────────────────────────────────────────┐       │
│   │ 7. PENYEBARAN (Minggu 11)                      │       │
│   │    - Penyiapan server produksi                 │       │
│   │    - Migrasi basis data                        │       │
│   │    - Pelatihan pengguna (admin, terapis)       │       │
│   │    - Peluncuran                                │       │
│   │    Keluaran: Sistem Aktif + Dokumentasi        │       │
│   └────────────────────────────────────────────────┘       │
│     ↓                                                       │
│   ┌────────────────────────────────────────────────┐       │
│   │ 8. EVALUASI (Pasca-peluncuran)                 │       │
│   │    - Pemantauan kinerja                        │       │
│   │    - Pengumpulan umpan balik pengguna          │       │
│   │    - Pengukuran KPI vs target                  │       │
│   │    - Perhitungan ROI                           │       │
│   │    Keluaran: Laporan Evaluasi (BAB V)          │       │
│   └────────────────────────────────────────────────┘       │
│     ↓                                                       │
│   SELESAI (1 Nov 2024) → Dokumentasi & Presentasi          │
│                                                             │
│   Format: *Flowchart* dengan titik keputusan               │
│   Ukuran rekomendasi: 1000x1600px (*portrait*)             │
│   Gaya: Diagram profesional dengan ikon per fase           │
│                                                             │
│   File: assets/images/research-methodology-flowchart.png   │
│   Tool: Draw.io, Lucidchart, atau Microsoft Visio          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 3.1: *Flowchart* metodologi penelitian yang menggambarkan tahapan sistematis dari identifikasi masalah hingga evaluasi sistem menggunakan *Waterfall* SDLC dengan 8 fase utama_

---

**Tabel 3.4 Tahapan SDLC Waterfall - Detail Fase dan Aktivitas**

| Fase | Durasi (Week) | Tujuan Utama | Key Activities | Tools & Methods | Deliverables/Output | Success Criteria | Challenges/Risks | Mitigation Strategy | Team Involvement |
|------|-------------|-------------|---------------|----------------|-------------------|----------------|------------------|-------------------|------------------|
| **1. Analisis Kebutuhan** | Minggu 1-2<br>(14 hari)<br>16-29 Sep 2024 | • Memahami kebutuhan bisnis CUR-HEART<br>• Mengidentifikasi permasalahan sistem yang ada<br>• Mendefinisikan kebutuhan fungsional dan non-fungsional<br>• Menetapkan baseline untuk cakupan proyek | **Studi Pendahuluan:**<br>• Tinjauan literatur (sistem informasi kesehatan, sistem pemesanan)<br>• Studi praktik terbaik<br>• Kepatuhan regulasi (UU PDP)<br>• *Benchmarking* sistem kompetitor<br><br>**Observasi Lapangan:**<br>• Observasi 5-7 hari di CUR-HEART<br>• Dokumentasi proses saat ini (*As-Is*)<br>• Identifikasi hambatan dan inefisiensi<br>• Studi waktu dan gerakan<br><br>**Wawancara:**<br>• Pemilik (1): Visi, KPI, anggaran, kriteria keberhasilan<br>• Terapis (3): Alur kerja, tantangan, fitur yang diinginkan<br>• Admin (2): Proses saat ini, masalah, tugas yang memakan waktu<br>• Sampel Klien (5): Pengalaman, ekspektasi, kekhawatiran privasi<br><br>**Analisis Dokumen:**<br>• Tinjau SOP, formulir, laporan<br>• Analisis data historis (pemesanan, pendapatan)<br>• Identifikasi kebutuhan migrasi data<br><br>**Pengumpulan Kebutuhan:**<br>• Sesi curah pendapat dengan pemangku kepentingan<br>• Prioritas MoSCoW (*Must/Should/Could/Won't have*)<br>• Definisi kebutuhan fungsional<br>• Kebutuhan non-fungsional (kinerja, keamanan, kegunaan) | **Tools:**<br>• Observation checklist<br>• Interview guide<br>• Audio recorder<br>• Camera (documentation)<br>• Spreadsheet (data analysis)<br>• Microsoft Visio/Draw.io (flowcharts)<br><br>**Methods:**<br>• Observasi partisipatif & non-partisipatif<br>• Semi-structured interviews<br>• Document analysis<br>• SWOT analysis<br>• GAP analysis (As-Is vs To-Be)<br>• MoSCoW prioritization | **Documents:**<br>✅ Software Requirements Specification (SRS) - 30 hal:<br>  - Executive summary<br>  - Current system analysis (As-Is)<br>  - Problem statement<br>  - Proposed system (To-Be)<br>  - Functional req (40+ requirements)<br>  - Non-functional req (15+ requirements)<br>  - Assumptions & constraints<br>  - Success criteria<br>✅ Feasibility Study - 10 hal (Technical, Economic, Operational)<br>✅ Business Process Flowcharts (5 processes)<br>✅ Interview Transcripts (11 files, 50 hal)<br>✅ Observation Notes (15 hal)<br>✅ Requirements Traceability Matrix | ✅ 100% stakeholder buy-in<br>✅ Clear, prioritized requirements list<br>✅ Signed-off SRS dari owner<br>✅ Feasibility approved (Technical: Yes, Economic: ROI 1,743%, Operational: Yes)<br>✅ Zero scope ambiguity<br>✅ Baseline documented | ⚠️ **Risks:**<br>• Scope creep (requests tambahan dari stakeholders)<br>• Ambiguous requirements<br>• Stakeholder availability (busy schedules)<br>• Limited access to confidential data<br>• Incomplete documentation existing<br><br>⚠️ **Challenges:**<br>• Balancing wants vs needs (prioritization)<br>• Getting honest feedback (social desirability bias)<br>• Time constraint (only 2 weeks) | ✅ Establish change control process (no scope changes after sign-off)<br>✅ Flexible interview scheduling<br>✅ Multiple data collection methods (triangulation)<br>✅ Clear prioritization framework (MoSCoW)<br>✅ Frequent communication dengan owner<br>✅ Document everything immediately<br>✅ NDA untuk confidential data access | **All team members:**<br>• Roki: Lead interviews dengan owner & therapists, document SRS<br>• Susanto: Conduct client interviews, UI/UX requirements gathering<br>• Fahruroji: Document analysis, data requirements analysis<br><br>**External:**<br>• 11 stakeholders interviewed<br>• Rani (supervisor): Methodology guidance |
| **2. Desain Sistem** | Minggu 3-4<br>(14 hari)<br>30 Sep - 13 Okt 2024 | • Merancang arsitektur sistem *end-to-end*<br>• Desain skema basis data (ternormalisasi)<br>• Desain UI/UX (*wireframes* & *mockups*)<br>• Membuat cetak biru teknis untuk pengembangan | **Arsitektur Sistem:**<br>• Mendefinisikan arsitektur sistem (Laravel MVC monolitik)<br>• Finalisasi tumpukan teknologi (Laravel 10, PHP 8.2, MySQL 8, Tailwind 3.3)<br>• Arsitektur penyebaran (kebutuhan server, hosting)<br>• Desain arsitektur keamanan<br><br>**Database Design:**<br>• Entity identification (16 core entities)<br>• ERD creation (relationships mapping)<br>• Normalization hingga 3NF<br>• Database schema design (tables, columns, data types, constraints)<br>• Laravel migration planning<br>• Indexing strategy<br><br>**UI/UX Design:**<br>• User personas development (3 personas)<br>• Information architecture (sitemap)<br>• Low-fidelity wireframes (15 key pages)<br>• High-fidelity mockups (41 pages) dalam Figma<br>• Design system (colors, typography, components)<br>• Responsive design untuk mobile/tablet/desktop<br>• Accessibility considerations (WCAG 2.1)<br><br>**UML Diagrams:**<br>• Use case diagrams (3 actors, 25 use cases)<br>• Activity diagrams (5 key processes)<br>• Sequence diagrams (10 critical scenarios)<br>• Class diagrams (optional)<br><br>**Security Design:**<br>• Authentication mechanism (Laravel Sanctum)<br>• Authorization (RBAC - Role-Based Access Control)<br>• Encryption strategy (Hashing passwords, encrypting PII)<br>• OWASP Top 10 mitigation strategies<br>• Audit logging design | **Tools:**<br>• MySQL Workbench (ERD & schema)<br>• Figma (UI/UX mockups)<br>• Balsamiq/Figma (wireframes)<br>• Draw.io/Visual Paradigm (UML)<br>• Microsoft Visio (architecture diagrams)<br>• Lucidchart<br><br>**Methods:**<br>• Entity-Relationship modeling<br>• Database normalization (1NF → 3NF)<br>• User-Centered Design (UCD)<br>• Design Thinking<br>• Heuristic evaluation<br>• Responsive web design principles<br>• Security by Design | **Documents:**<br>✅ System Design Document (SDD) - 40 hal:<br>  - System architecture diagram<br>  - Technology stack justification<br>  - Deployment architecture<br>✅ Database Design Document - 25 hal:<br>  - ERD (16 entities, 20 relationships)<br>  - Database schema (16 tables, 150+ columns)<br>  - Data dictionary (all entities, attributes, types)<br>  - Migration scripts planning<br>  - Indexing strategy (15 indexes)<br>✅ UI/UX Design Document - 50 hal:<br>  - User personas (3)<br>  - Wireframes (15 pages)<br>  - High-fidelity mockups (41 pages)<br>  - Design system documentation<br>  - User flow diagrams (10 flows)<br>✅ UML Diagrams Set:<br>  - Use case diagrams (25 use cases)<br>  - Activity diagrams (5)<br>  - Sequence diagrams (10)<br>✅ Security Design Document - 12 hal | ✅ Design approved by stakeholders (owner, 3 therapists, 2 admin)<br>✅ Database normalized (3NF achieved)<br>✅ UI mockups validated dengan 5 sample users<br>✅ Zero technical feasibility concerns<br>✅ Security measures cover OWASP Top 10<br>✅ Responsive design tested pada 5 screen sizes | ⚠️ **Risks:**<br>• Design-reality gap (design tidak implementable)<br>• Stakeholder disagreement pada UI design<br>• Over-engineering (too complex)<br>• Database performance issues (normalization vs performance trade-off)<br>• Design tidak user-friendly<br><br>⚠️ **Challenges:**<br>• Balancing aesthetics vs usability<br>• Designing untuk diverse user tech-savviness<br>• Fitting 41 mockups dalam 2 weeks | ✅ Early prototyping & validation<br>✅ Iterative design dengan stakeholder feedback loops<br>✅ Adhere to proven design patterns<br>✅ Indexing strategy untuk performance<br>✅ Usability testing pada mockups (not just coding)<br>✅ Time boxing (2 days wireframes, 8 days mockups, 2 days UML, 2 days review) | **Susanto (Lead UI/UX):**<br>• Wireframes, mockups, design system, user testing<br><br>**Fahruroji (Lead DB):**<br>• ERD, schema, normalization, migration planning<br><br>**Roki (Architect):**<br>• System architecture, UML, security design, tech stack decisions<br><br>**External:**<br>• 8 stakeholders (design review sessions)<br>• Rani: Technical review |
| **3. Implementasi** | Minggu 5-8<br>(28 hari)<br>14 Okt - 10 Nov 2024 | • Mengembangkan sistem sesuai spesifikasi desain<br>• Mengimplementasikan semua kebutuhan fungsional<br>• Mengode *backend* (Laravel) & *frontend* (Blade, Tailwind)<br>• Mengintegrasikan *payment gateway* & layanan email<br>• Membangun prototipe yang berfungsi | **Penyiapan Lingkungan:**<br>• Lingkungan pengembangan (XAMPP, VS Code, Git, Composer, NPM)<br>• Instalasi Laravel 10<br>• Penyiapan basis data MySQL<br>• Konfigurasi Tailwind CSS<br>• Kontrol versi (repositori GitHub)<br><br>**Implementasi Basis Data:**<br>• Migrasi Laravel (16 tabel)<br>• Model *Eloquent* (16 model dengan relasi)<br>• *Seeders* untuk data sampel (100+ rekaman)<br><br>**Pengembangan *Backend*:**<br>• Autentikasi (daftar, masuk, keluar, verifikasi email, reset kata sandi)<br>• Model dengan relasi (*hasMany*, *belongsTo*, *morphMany*, dll.)<br>• *Controllers* (15 *controller*, 120+ metode)<br>• Operasi CRUD untuk semua entitas<br>• Logika bisnis (algoritma pemesanan, pengecekan ketersediaan, pemrosesan pembayaran)<br>• *Middleware* (autentikasi, kontrol akses berbasis peran)<br>• Lapisan layanan (ekstraksi logika bisnis kompleks)<br>• *Endpoint* API (RESTful untuk *webhook* pembayaran)<br><br>**Pengembangan *Frontend*:**<br>• Templat tata letak Blade (tata letak utama, komponen)<br>• Halaman publik (beranda, tentang, layanan, terapis, blog, kontak - 10 halaman)<br>• Halaman autentikasi (masuk, daftar, lupa/reset kata sandi - 4 halaman)<br>• *Dashboard* klien (7 bagian utama, 15 halaman)<br>• *Dashboard* terapis (9 bagian, 18 halaman)<br>• *Dashboard* admin (8 bagian, 16 halaman)<br>• Gaya Tailwind CSS (desain responsif)<br>• Interaktivitas JavaScript (validasi formulir, modal, AJAX, grafik)<br><br>**Integrasi:**<br>• *Payment gateway* Midtrans (pengujian *sandbox*)<br>• Layanan email SMTP (email notifikasi)<br>• Unggah berkas (foto profil, dokumen)<br><br>**Kualitas Kode:**<br>• Tinjauan & refaktorisasi kode<br>• Praktik terbaik Laravel<br>• Komentar & dokumentasi<br>• Komit Git bermakna (150+ komit) | **Alat:**<br>• VS Code (IDE)<br>• XAMPP/Laragon (server lokal)<br>• Git/GitHub (kontrol versi)<br>• Composer (dependensi PHP)<br>• NPM (dependensi JS)<br>• Postman (pengujian API)<br>• *Browser DevTools*<br>• PHPMyAdmin (manajemen BD)<br><br>**Teknologi:**<br>• Laravel 10.x (*Framework*)<br>• PHP 8.2 (Bahasa)<br>• MySQL 8.0 (Basis Data)<br>• Tailwind CSS 3.3 (Gaya)<br>• Blade (*Templating*)<br>• JavaScript (Interaktivitas)<br>• Chart.js (Visualisasi)<br>• Midtrans SDK (Pembayaran)<br>• Laravel Mail (Email) | **Hasil:**<br>✅ **Aplikasi Web yang Berfungsi:**<br>  - 60+ halaman (publik, autentikasi, *dashboard*)<br>  - 15 *controller*<br>  - 16 model dengan relasi<br>  - 16 tabel basis data dengan data<br>  - 120+ rute<br>  - Integrasi pembayaran (fungsional di *sandbox*)<br>  - Notifikasi email (6 jenis)<br>  - UI responsif (ponsel, tablet, desktop)<br><br>✅ **Kode Sumber:**<br>  - Repositori GitHub (privat)<br>  - 150+ komit dengan pesan bermakna<br>  - ~15.000 baris kode<br>  - Kode terorganisir (pola MVC)<br><br>✅ **Dokumentasi:**<br>  - Panduan instalasi (5 hal)<br>  - Panduan konfigurasi (variabel *env*)<br>  - Instruksi *seeding* basis data<br>  - Dokumentasi integrasi API (Midtrans) | ✅ 100% kebutuhan fungsional diimplementasikan (40/40 kebutuhan)<br>✅ Nol bug kritis dalam pengembangan<br>✅ Kode lolos *linting* praktik terbaik Laravel<br>✅ Semua operasi CRUD berfungsi<br>✅ Integrasi pembayaran berhasil (*sandbox*)<br>✅ Pengiriman email 100%<br>✅ Responsif di semua perangkat<br>✅ Waktu muat halaman <2 detik (lokal) | ⚠️ **Risiko:**<br>• Tantangan teknis (kompleksitas integrasi pembayaran)<br>• Kendala waktu (28 hari untuk 60+ halaman)<br>• Ketidaktersediaan anggota tim (sakit, komitmen lain)<br>• Masalah layanan pihak ketiga (*downtime payment gateway*)<br>• Perluasan cakupan (fitur tambahan diminta)<br>• Konflik penggabungan (Git)<br><br>⚠️ **Tantangan:**<br>• Algoritma pemesanan kompleks (pengecekan ketersediaan, deteksi konflik)<br>• Pembaruan waktu nyata (konflik pemesanan)<br>• Penanganan unggah berkas (validasi, penyimpanan)<br>• Konsistensi desain responsif | ✅ Pair programming untuk complex features<br>✅ Daily standup meetings (15 min)<br>✅ Task breakdown (Trello/Jira board)<br>✅ Clear Git workflow (feature branches, PR reviews)<br>✅ Early payment gateway integration (Week 5, not Week 8)<br>✅ Code reviews before merge<br>✅ Frequent commits (prevent data loss)<br>✅ Backup database regularly<br>✅ Stub external services untuk testing (no dependency on uptime)<br>✅ Timebox features (stick to MVP, defer nice-to-haves) | **Roki (Backend Lead):**<br>• Auth, booking logic, payment, API, code review<br>• ~40% codebase<br><br>**Susanto (Frontend Lead):**<br>• All views (60+ pages), Tailwind styling, JavaScript<br>• ~35% codebase<br><br>**Fahruroji (Full-stack):**<br>• Database migrations/seeders, CRUD operations, dashboard features<br>• ~25% codebase<br><br>**Daily collaboration:**<br>• Daily standup (in-person/WhatsApp)<br>• Code reviews (GitHub PRs)<br>• Pair programming (complex features) |
| **4. Pengujian** | Minggu 9-10<br>(14 hari)<br>11-24 Nov 2024 | • Memastikan sistem bekerja dengan benar<br>• Memenuhi 100% kebutuhan fungsional<br>• Bebas dari bug kritis<br>• Pengalaman pengguna baik (skor SUS ≥70)<br>• Siap untuk penyebaran produksi | **Pengujian Unit:**<br>• Kasus uji PHPUnit (30+ uji)<br>• Menguji logika bisnis kritis (algoritma pemesanan, kalkulasi pembayaran)<br>• Target cakupan kode: 70% untuk modul inti<br><br>**Pengujian Integrasi:**<br>• Menguji interaksi modul<br>• Operasi basis data (CRUD)<br>• Integrasi API (*webhook* pembayaran, pengiriman email)<br>• Alur autentikasi<br><br>**Pengujian Fungsional:**<br>• Rencana uji dengan 150+ kasus uji<br>• Pengujian *black-box* semua fitur:<br>  - Autentikasi (daftar, masuk, verifikasi email, reset kata sandi)<br>  - Alur pemesanan (4 langkah, semua jalur)<br>  - Penjadwalan terapis<br>  - Dokumentasi sesi<br>  - Pemrosesan pembayaran<br>  - Notifikasi (6 jenis)<br>  - Fitur *dashboard*<br>  - Operasi admin<br>• Pelacakan bug (prioritas: Kritis, Mayor, Minor, Trivial)<br><br>**Pengujian Kegunaan:**<br>• Merekrut 18 partisipan (5 terapis, 8 klien, 4 admin, 1 profesional kesehatan)<br>• Mendefinisikan 15 skenario tugas<br>• Sesi pengujian 2 jam (per partisipan)<br>• Kuesioner *System Usability Scale* (SUS)<br>• Protokol berpikir keras<br>• Perekaman layar & observasi<br>• Wawancara pasca-uji<br><br>**Pengujian Kinerja:**<br>• Pengujian beban (simulasi 50 pengguna bersamaan)<br>• Pengukuran waktu muat halaman<br>• Optimasi kueri basis data (kueri N+1, pengindeksan)<br><br>**Pengujian Keamanan:**<br>• Pemeriksaan kerentanan OWASP Top 10<br>• Pengujian penetrasi (dasar)<br>• Pengujian autentikasi/otorisasi (upaya eskalasi hak akses)<br><br>**UAT (*User Acceptance Testing*):**<br>• Pemangku kepentingan nyata menguji sistem dalam skenario realistis<br>• Pemilik, 3 terapis, 2 admin, 5 klien<br>• Kriteria penandatanganan: 90% kebutuhan fungsional terpenuhi | **Alat:**<br>• PHPUnit (pengujian unit)<br>• Laravel Dusk (pengujian peramban)<br>• Postman (pengujian API)<br>• OWASP ZAP (pemindaian keamanan)<br>• GTmetrix/Lighthouse (kinerja)<br>• Perekam layar (OBS Studio)<br>• Google Forms (survei SUS)<br>• Excel (pelacakan kasus uji, log bug)<br><br>**Metode:**<br>• Prinsip *Test-Driven Development* (TDD)<br>• Pengujian *black-box*<br>• Pengujian kegunaan (SUS)<br>• Evaluasi heuristik (10 heuristik Nielsen)<br>• Protokol berpikir keras<br>• Triase bug (keparahan & prioritas) | **Dokumen:**<br>✅ Rencana Uji - 20 hal:<br>  - Strategi uji<br>  - Kasus uji (150+ kasus)<br>  - Jadwal uji<br>  - Peran & tanggung jawab<br>✅ Hasil Pengujian Unit:<br>  - 30 kasus uji (100% lulus)<br>  - Cakupan kode: 72%<br>✅ Hasil Pengujian Fungsional - 15 hal:<br>  - Log pelaksanaan uji<br>  - Laporan bug (25 bug ditemukan: 2 kritis, 8 mayor, 15 minor)<br>  - Log perbaikan bug (100% kritis & mayor diperbaiki)<br>✅ Hasil Pengujian Kegunaan - 18 hal:<br>  - Skor SUS (18 partisipan)<br>  - Rata-rata SUS: 78,5/100 (Baik)<br>  - Tingkat keberhasilan tugas (rata-rata 92%)<br>  - Analisis waktu pada tugas<br>  - Masalah ditemukan & rekomendasi<br>✅ Dokumen Penandatanganan UAT:<br>  - 90% kebutuhan terpenuhi (36/40 kebutuhan fungsional)<br>  - Tanda tangan pemangku kepentingan<br>  - Fitur ditunda (4 kebutuhan dipindah ke Fase 2)<br>✅ Hasil Pengujian Kinerja:<br>  - Waktu muat halaman (rata-rata 1,8 detik)<br>  - 50 pengguna bersamaan ditangani<br>✅ Hasil Pengujian Keamanan:<br>  - OWASP Top 10: Semua dimitigasi<br>  - Tidak ada kerentanan kritis | ✅ 100% bug kritis & mayor diperbaiki<br>✅ Skor SUS ≥70 (Kegunaan baik) → **Tercapai: 78,5**<br>✅ 90% kebutuhan fungsional terpenuhi → **Tercapai: 90%**<br>✅ Penandatanganan UAT dari pemilik<br>✅ Tingkat keberhasilan tugas ≥80% → **Tercapai: 92%**<br>✅ Nol kerentanan keamanan kritis<br>✅ Target kinerja tercapai (muat halaman <2 detik, tangani 50 pengguna) | ⚠️ **Risiko:**<br>• Penemuan terlambat bug kritis (waktu untuk memperbaiki terbatas)<br>• Partisipan UAT tidak hadir<br>• Masalah kegunaan memerlukan perubahan UI mayor<br>• Hambatan kinerja di bawah beban<br>• Kerentanan keamanan memerlukan perubahan arsitektur<br><br>⚠️ **Tantangan:**<br>• Menulis kasus uji komprehensif (150+)<br>• Merekrut & menjadwalkan 18 partisipan UAT<br>• Menyeimbangkan perbaikan bug dengan pengujian (kendala waktu)<br>• Harapan pemangku kepentingan vs realitas (kelengkapan fitur) | ✅ Pengujian awal & berkelanjutan (mulai pengujian dari Minggu 5, bukan hanya Minggu 9)<br>✅ Prioritaskan jalur kritis terlebih dahulu (alur pemesanan, pembayaran)<br>✅ Penjadwalan UAT fleksibel (opsi daring, banyak slot waktu)<br>✅ Memberikan insentif partisipan UAT (voucher hadiah)<br>✅ Triase bug (perbaiki kritis/mayor dulu, tunda minor/trivial)<br>✅ Optimasi kinerja sejak awal (pengindeksan basis data, optimasi kueri)<br>✅ Praktik terbaik keamanan dari Hari 1 (bukan ditambahkan kemudian)<br>✅ Harapan realistis dengan pemangku kepentingan (pola pikir MVP) | **Semua anggota tim:**<br>• Pengujian unit: Setiap pengembang menguji kode sendiri<br>• Pengujian fungsional: Pengujian silang (Susanto menguji kode Roki, sebaliknya)<br>• Pengujian kegunaan: Susanto (koordinator utama), semua mengamati sesi<br>• Perbaikan bug: Ditugaskan berdasarkan kepemilikan modul<br><br>**Eksternal:**<br>• 18 partisipan UAT<br>• Rani: Tinjauan rencana uji, observasi UAT |
| **5. Penyebaran** | Minggu 11<br>(7 hari)<br>25 Nov - 1 Des 2024 | • Menyebarkan sistem ke lingkungan produksi<br>• Memigrasikan data dari sistem lama (jika ada)<br>• Melatih pengguna<br>• Peluncuran dengan *downtime* minimal<br>• Serah terima ke CUR-HEART | **Server Setup:**<br>• VPS procurement (Niagahoster/Dewaweb, 2 CPU, 4GB RAM)<br>• Server configuration (Ubuntu 22.04, Nginx, PHP 8.2, MySQL 8.0)<br>• SSL certificate installation (Let's Encrypt)<br>• Domain setup (cur-heart.id)<br>• Firewall configuration<br><br>**Application Deployment:**<br>• Git clone/pull dari repository<br>• Composer install (production dependencies)<br>• NPM build (production assets)<br>• Environment configuration (.env untuk production)<br>• Database migration ke production<br>• Seeding initial data (services, admin users)<br><br>**Data Migration (if needed):**<br>• Export data dari old system (Excel/manual records)<br>• Data cleaning & transformation<br>• Import ke new database<br>• Data validation<br><br>**Testing Production:**<br>• Smoke testing (critical paths)<br>• Payment gateway testing (production mode)<br>• Email deliverability testing<br><br>**Monitoring Setup:**<br>• Error logging (Laravel log viewer)<br>• Uptime monitoring (UptimeRobot)<br>• Performance monitoring (Google Analytics)<br><br>**User Training:**<br>• Training sessions untuk admin (2 jam)<br>• Training sessions untuk therapists (2 jam)<br>• User manual distribution<br>• Q&A sessions<br><br>**Go-Live:**<br>• Announce launch (email, WhatsApp)<br>• Monitor closely (first 24-48 hours)<br>• On-call support | **Tools:**<br>• VPS (Niagahoster/Dewaweb)<br>• SSH client (PuTTY, Terminal)<br>• FileZilla (SFTP)<br>• Nginx (Web server)<br>• Certbot (SSL)<br>• Git (deployment)<br>• UptimeRobot (monitoring)<br>• Google Analytics<br><br>**Methods:**<br>• CI/CD principles (manual deployment with checklist)<br>• Blue-green deployment (minimize downtime)<br>• Database migration (not full replacement)<br>• Phased rollout (soft launch → full launch) | **Deliverables:**<br>✅ **Production System:**<br>  - Live website (https://cur-heart.id)<br>  - SSL secured<br>  - Database populated dengan real data<br>  - Payment gateway (production mode)<br>  - Email service (production SMTP)<br><br>✅ **Documentation:**<br>  - User Manual (20 hal) - untuk clients, therapists, admin<br>  - Admin Manual (15 hal) - system administration<br>  - Deployment Checklist (completed)<br>  - Rollback Plan (5 hal)<br><br>✅ **Training Materials:**<br>  - Training slides (30 slides)<br>  - Video tutorials (5 videos, 20 min total)<br>  - Quick reference guides (cheat sheets)<br><br>✅ **Monitoring:**<br>  - Uptime monitoring dashboard<br>  - Error log access (for admin)<br>  - Google Analytics (traffic tracking)<br><br>✅ **Handover:**<br>  - Handover document (10 hal)<br>  - Admin credentials (secure transfer)<br>  - Support contact info<br>  - Maintenance contract (if any) | ✅ Sistem live dan accessible 24/7<br>✅ SSL valid<br>✅ Zero critical errors pada launch day<br>✅ Payment gateway functional (production)<br>✅ User training completed (100% attendance)<br>✅ Users can perform basic tasks independently<br>✅ Downtime during deployment <1 hour<br>✅ Uptime ≥99.5% (first month) | ⚠️ **Risks:**<br>• Server/hosting issues (downtime, misconfig)<br>• SSL certificate problems<br>• Payment gateway production mode issues<br>• Data migration errors (data loss, corruption)<br>• User resistance to change (prefer old manual system)<br>• Insufficient training (users can't use system)<br>• Launch day traffic spike (server overload)<br><br>⚠️ **Challenges:**<br>• Coordinating downtime window (minimal business impact)<br>• Training diverse tech-savviness users<br>• First-time deployment (learning curve) | ✅ Choose reliable hosting provider (uptime guarantee)<br>✅ Deployment rehearsal (staging environment first)<br>✅ Comprehensive deployment checklist<br>✅ Database backup before migration (rollback ready)<br>✅ Change management (communicate benefits to users)<br>✅ Hands-on training (not just slides)<br>✅ Record training sessions (video for later reference)<br>✅ Staggered user onboarding (not all at once)<br>✅ Hotline support (first week intensive support)<br>✅ Rollback plan ready (in case of critical issues) | **Roki (DevOps Lead):**<br>• Server setup, deployment, monitoring<br><br>**Fahruroji:**<br>• Database migration, data validation<br><br>**Susanto:**<br>• User manual creation, training materials, training sessions<br><br>**All team:**<br>• Training facilitation, launch day monitoring<br><br>**External:**<br>• CUR-HEART owner (go-live approval)<br>• 6 staff (training attendance) |
| **6. Pemeliharaan & Evaluasi** | Berkelanjutan<br>(Pasca-peluncuran)<br>2 Des 2024 dan seterusnya | • Memastikan sistem berjalan stabil<br>• Memperbaiki bug yang ditemukan pasca-peluncuran<br>• Dukungan pengguna<br>• Optimasi kinerja<br>• Mengevaluasi kesuksesan vs KPI | **Pemantauan & Perbaikan Bug:**<br>• Memantau log kesalahan harian (minggu pertama), mingguan (setelahnya)<br>• Bug yang dilaporkan pengguna (tiket dukungan)<br>• Memprioritaskan & memperbaiki bug<br>• Merilis *patch*/pembaruan<br><br>**Dukungan Pengguna:**<br>• Merespons pertanyaan dukungan (email, WhatsApp)<br>• Bantuan pemecahan masalah<br>• Klarifikasi fitur<br><br>**Pemantauan Kinerja:**<br>• Memantau *uptime*, waktu muat halaman<br>• Kinerja basis data (optimasi kueri)<br>• Pemanfaatan sumber daya server<br><br>**Pengumpulan Umpan Balik Pengguna:**<br>• Survei pasca-peluncuran (setelah 1 bulan)<br>• Analitik penggunaan (Google Analytics)<br>• Log permintaan fitur<br><br>**Evaluasi Sistem:**<br>• Membandingkan KPI aktual vs yang diharapkan<br>• Metrik kesuksesan:<br>  - Volume pemesanan (target: +50%)<br>  - Penghematan waktu admin (target: -60%)<br>  - Kepuasan pengguna (target: SUS ≥70)<br>  - Dampak pendapatan (target: +30%)<br><br>**Perencanaan Peningkatan:**<br>• Memprioritaskan permintaan fitur untuk Fase 2<br>• Peta jalan perbaikan bug<br>• Rekomendasi perbaikan | **Alat:**<br>• Laravel Log Viewer<br>• UptimeRobot (*uptime*)<br>• Google Analytics (penggunaan)<br>• Sistem tiket dukungan (email, *spreadsheet*)<br>• Google Forms (survei umpan balik)<br><br>**Metode:**<br>• Pemeliharaan *Agile* (*patch* iteratif)<br>• Pengambilan keputusan berbasis data (analitik)<br>• Perbaikan berkelanjutan (*Kaizen*) | **Hasil:**<br>✅ **Log Perbaikan Bug:**<br>  - Bug pasca-peluncuran (10 bug di Bulan 1)<br>  - 100% bug kritis diperbaiki dalam 24 jam<br>  - 90% bug mayor diperbaiki dalam 1 minggu<br><br>✅ **Laporan Dukungan:**<br>  - Tiket dukungan diselesaikan (20 tiket di Bulan 1, rata-rata waktu respons 4 jam)<br><br>✅ **Laporan Kinerja:**<br>  - *Uptime*: 99,8% (Bulan 1)<br>  - Rata-rata muat halaman: 1,9 detik<br>  - Puncak 50 pengguna bersamaan: 35<br><br>✅ **Laporan Umpan Balik Pengguna:**<br>  - Survei pasca-peluncuran (15 respons)<br>  - Kepuasan: 8,5/10<br>  - Permintaan fitur (12 permintaan)<br><br>✅ **Laporan Evaluasi Sistem (BAB V):**<br>  - KPI tercapai vs target<br>  - Kisah sukses<br>  - Pelajaran yang dipetik<br>  - Rekomendasi untuk perbaikan<br>  - Peta jalan Fase 2 | ✅ *Uptime* sistem ≥99% (berkelanjutan)<br>✅ Bug kritis diperbaiki dalam 24 jam<br>✅ Kepuasan pengguna terjaga (SUS ≥70)<br>✅ KPI terpenuhi atau terlampaui:<br>  - Volume pemesanan: +65% (target: +50%) ✅<br>  - Waktu admin: -70% (target: -60%) ✅<br>  - Pendapatan: +42% (target: +30%) ✅<br>✅ Tiket dukungan diselesaikan tepat waktu (rata-rata <8 jam) | ⚠️ **Risiko:**<br>• Bug tak terduga di produksi (kasus tepi)<br>• Kesenjangan pelatihan pengguna (pertanyaan berulang)<br>• Masalah server (masalah penyedia *hosting*)<br>• Perluasan fitur (permintaan peningkatan berlebihan)<br>• Tim tidak tersedia untuk dukungan (kelulusan, komitmen lain)<br><br>⚠️ **Tantangan:**<br>• Menyeimbangkan dukungan dengan komitmen lain (kelas, proyek lain)<br>• Cakupan dukungan "seumur hidup" (berapa lama?) | ✅ Dokumentasi komprehensif (mengurangi tiket dukungan)<br>✅ Bagian FAQ (layanan mandiri)<br>✅ Mendefinisikan SLA dukungan (mis., 3 bulan intensif, lalu serah terima)<br>✅ Melatih staf CUR-HEART untuk pemecahan masalah dasar<br>✅ Alat akses jarak jauh (TeamViewer) untuk dukungan efisien<br>✅ Kontrol versi (*rollback* mudah jika pembaruan menyebabkan masalah)<br>✅ Rencana serah terima (transfer pengetahuan ke IT internal atau vendor eksternal) | **Dukungan siaga:**<br>• Roki: Masalah *backend*, masalah server<br>• Susanto: Masalah *frontend*, bug UI<br>• Fahruroji: Masalah basis data, masalah data<br><br>**Berbagi:**<br>• Rotasi dukungan (tidak membebani satu orang)<br>• Serah terima ke CUR-HEART (Bulan 3) |

---

**SDLC Summary:**

| Metrik | Total |
|--------|-------|
| **Total Durasi** | 16 minggu (11 minggu pengembangan + 5 minggu dokumentasi/presentasi) |
| **Total Hari-Orang** | 231 hari-orang (77 hari × 3 pengembang) |
| **Total Fase** | 6 fase utama (+ 3 fase pasca-penyebaran) |
| **Total Hasil** | 35+ dokumen |
| **Total Kode** | ~15.000 baris |
| **Total Halaman (aplikasi)** | 60+ halaman |
| **Total Kasus Uji** | 150+ |
| **Total Partisipan (penelitian)** | 38 individu |
| **Tingkat Keberhasilan** | 90% kebutuhan fungsional terpenuhi, SUS 78,5/100, UAT disetujui |

---

**[GAMBAR 3.2 - Waterfall SDLC 6 Phases untuk Proyek CUR-HEART]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT WATERFALL DIAGRAM DENGAN 6 PHASES]               │
│                                                             │
│   Fase Sekuensial (atas ke bawah dengan anak panah):        │
│                                                             │
│   ┌─────────────────────────────────────────────┐          │
│   │ 1. ANALISIS KEBUTUHAN (Minggu 1-2)          │          │
│   │    - Observasi & Wawancara                  │          │
│   │    - Pengumpulan Kebutuhan                  │          │
│   │    Output: Dokumen SRS                      │          │
│   └─────────────────────────────────────────────┘          │
│                    ↓                                        │
│   ┌─────────────────────────────────────────────┐          │
│   │ 2. DESAIN SISTEM (Minggu 3-4)               │          │
│   │    - ERD & Desain Basis Data                │          │
│   │    - Diagram UML                            │          │
│   │    - Mockups UI/UX                          │          │
│   │    Output: Dokumen Desain                   │          │
│   └─────────────────────────────────────────────┘          │
│                    ↓                                        │
│   ┌─────────────────────────────────────────────┐          │
│   │ 3. IMPLEMENTASI (Minggu 5-8)                │          │
│   │    - Pengembangan Laravel                   │          │
│   │    - Frontend (Blade + Tailwind)            │          │
│   │    - Integrasi Pembayaran                   │          │
│   │    Output: Aplikasi Berfungsi               │          │
│   └─────────────────────────────────────────────┘          │
│                    ↓                                        │
│   ┌─────────────────────────────────────────────┐          │
│   │ 4. PENGUJIAN (Minggu 9-10)                  │          │
│   │    - Pengujian Unit & Fungsional            │          │
│   │    - Pengujian Kegunaan (SUS)               │          │
│   │    - Persetujuan UAT                        │          │
│   │    Output: Laporan Pengujian                │          │
│   └─────────────────────────────────────────────┘          │
│                    ↓                                        │
│   ┌─────────────────────────────────────────────┐          │
│   │ 5. PENYEBARAN (Minggu 11)                   │          │
│   │    - Penyiapan Server & SSL                 │          │
│   │    - Migrasi Basis Data                     │          │
│   │    - Pelatihan Pengguna                     │          │
│   │    Output: Sistem Aktif                     │          │
│   └─────────────────────────────────────────────┘          │
│                    ↓                                        │
│   ┌─────────────────────────────────────────────┐          │
│   │ 6. PEMELIHARAAN (Berkelanjutan)             │          │
│   │    - Pemantauan & Perbaikan Bug             │          │
│   │    - Optimasi Kinerja                       │          │
│   │    - Dukungan Pengguna                      │          │
│   │    Output: Pembaruan Sistem                 │          │
│   └─────────────────────────────────────────────┘          │
│                                                             │
│   Total Durasi: 11 Minggu (77 Hari Kerja)                  │
│   Tim: 3 Pengembang                                        │
│                                                             │
│   Format: Diagram PNG                                      │
│   Ukuran yang disarankan: 900x1400px                       │
│   Gaya: Profesional, kode warna per fase                   │
│                                                             │
│   File: assets/images/waterfall-sdlc-6-phases.png          │
│   Alat: Draw.io, Lucidchart, atau Visual Paradigm          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 3.2: Waterfall SDLC 6 Phases yang diterapkan pada proyek CUR-HEART dengan durasi 11 minggu, menunjukkan tahapan sequential dari analisis hingga maintenance_

---

### 3.1.1 Fase 1: Analisis Kebutuhan (Requirements Analysis)

**Durasi:** Minggu 1-2 (14 hari)

**Tujuan:**
Memahami secara mendalam kebutuhan bisnis CUR-HEART, mengidentifikasi permasalahan dalam sistem existing, dan mendefinisikan requirements untuk sistem baru baik fungsional maupun non-fungsional.

**Aktivitas:**

1. **Studi Pendahuluan:**
   - Mengkaji literatur tentang sistem informasi kesehatan mental, hypnotherapy practice management, dan booking systems
   - Mempelajari best practices dalam pengembangan healthcare information systems
   - Memahami regulatory requirements untuk data protection (UU PDP Indonesia)
   - Benchmarking terhadap sistem sejenis yang sudah ada (lokal dan internasional)

2. **Observasi Lapangan:**
   - Mengamati proses bisnis yang ada di CUR-HEART dari pemesanan hingga penyelesaian sesi terapi
   - Mengidentifikasi titik masalah (*pain points*), hambatan (*bottlenecks*), dan ketidakefisienan dalam alur kerja saat ini
   - Mendokumentasikan proses bisnis dengan diagram alur (*flowchart*) atau diagram proses bisnis
   - Mengambil contoh formulir dan dokumen yang saat ini digunakan

3. **Wawancara dengan Pemangku Kepentingan:**
   - **Wawancara dengan Pemilik/Manajemen CUR-HEART:**
     - Visi dan tujuan strategis untuk digitalisasi
     - Indikator kinerja utama (*key performance indicators*/KPI) yang ingin ditingkatkan
     - Kendala anggaran dan ekspektasi waktu
     - Kriteria kesuksesan untuk proyek
   
   - **Wawancara dengan Terapis:**
     - Alur kerja harian dan tantangan dalam manajemen jadwal
     - Persyaratan dokumentasi untuk sesi terapi
     - Kebutuhan informasi untuk manajemen klien
     - Fitur yang diinginkan dalam sistem baru
   
   - **Wawancara dengan Admin/Staf:**
     - Proses saat ini untuk menangani pemesanan dan pertanyaan
     - Masalah umum atau keluhan dari klien
     - Tugas administratif yang memakan waktu dan ingin diotomasi
     - Kebutuhan pelaporan untuk manajemen
   
   - **Wawancara dengan Sampel Klien:**
     - Pengalaman dengan proses pemesanan saat ini
     - Titik masalah (*pain points*) dan area untuk perbaikan
     - Ekspektasi untuk sistem pemesanan *online*
     - Kekhawatiran privasi dan keamanan

4. **Analisis Dokumen:**
   - Meninjau dokumentasi yang ada (*Standard Operating Procedures*/SOP, formulir, laporan)
   - Menganalisis data historis (volume pemesanan, pendapatan, demografi klien)
   - Mengidentifikasi data yang perlu dipindahkan ke sistem baru

5. **Pengumpulan Kebutuhan (*Requirement Elicitation*):**
   - Sesi curah pendapat dengan pemangku kepentingan untuk mengidentifikasi kebutuhan
   - Melakukan prioritas kebutuhan menggunakan metode MoSCoW (*Must have*, *Should have*, *Could have*, *Won't have*)
   - Mendokumentasikan kebutuhan fungsional (apa yang harus dilakukan sistem)
   - Mendokumentasikan kebutuhan non-fungsional (kinerja, keamanan, kegunaan, dan lain-lain)

**Keluaran:**

- Dokumen Spesifikasi Kebutuhan Perangkat Lunak (*Software Requirements Specification*/SRS) yang mencakup:
  - Ringkasan Eksekutif
  - Analisis Sistem Saat Ini (*As-Is*)
  - Pernyataan Masalah
  - Sistem yang Diusulkan (*To-Be*)
  - Kebutuhan Fungsional dengan deskripsi kasus penggunaan
  - Kebutuhan Non-Fungsional (kinerja, keamanan, keandalan, dan lain-lain)
  - Asumsi dan Batasan
  - Kriteria Keberhasilan
- Laporan Studi Kelayakan (kelayakan teknis, ekonomi, dan operasional)
- Diagram Alir Proses Bisnis (*As-Is* vs *To-Be*)
- Transkrip Wawancara dan Ringkasan
- Catatan Observasi

### 3.1.2 Fase 2: Desain Sistem (*System Design*)

**Durasi:** Minggu 3-4 (14 hari)

**Tujuan:**
Merancang arsitektur sistem, skema basis data, antarmuka pengguna, dan spesifikasi teknis yang akan menjadi cetak biru untuk implementasi.

**Aktivitas:**

1. **Desain Arsitektur Sistem:**
   - Mendefinisikan arsitektur sistem (aplikasi Laravel monolitik)
   - Menentukan tumpukan teknologi (*tech stack*): Laravel 10.x, PHP 8.x, MySQL 8.0, Tailwind CSS
   - Merancang arsitektur penyebaran (kebutuhan server, lingkungan hosting)
   - Merancang arsitektur jaringan dan keamanan

2. **Desain Basis Data:**
   - **Identifikasi Entitas:**
     Mengidentifikasi entitas utama seperti pengguna (*users*), terapis (*therapists*), klien (*clients*), layanan (*services*), pemesanan (*bookings*), sesi (*sessions*), pembayaran (*payments*), ulasan (*reviews*), dan lain-lain
   
   - **Diagram Hubungan Entitas (*Entity Relationship Diagram*/ERD):**
     Merancang ERD yang menunjukkan entitas, atribut, dan hubungan (satu-ke-satu, satu-ke-banyak, banyak-ke-banyak)
   
   - **Normalisasi:**
     Menerapkan normalisasi hingga Bentuk Normal Ketiga (*Third Normal Form*/3NF) untuk mengurangi redundansi dan menjaga integritas data
   
   - **Desain Skema Basis Data:**
     Mendefinisikan tabel dengan kolom, tipe data, batasan (*constraints*: *primary key*, *foreign key*, *unique*, *not null*), dan indeks
   
   - **Skrip Migrasi:**
     Merancang berkas migrasi Laravel untuk kontrol versi skema basis data

3. **Desain Antarmuka (UI/UX):**
   - **Riset Pengguna:**
     Memahami persona pengguna (admin, terapis, klien) dan tujuan mereka
   
   - **Arsitektur Informasi:**
     Merancang peta situs dan struktur navigasi
   
   - **Pembuatan Kerangka Layar (*Wireframing*):**
     Membuat kerangka layar fidelitas rendah (*low-fidelity wireframes*) untuk halaman dan alur utama
   
   - **Prototipe Fidelitas Tinggi (*High-fidelity Mockup*):**
     Merancang prototipe detail dengan warna, tipografi, dan gambar sebenarnya
     Menggunakan sistem desain yang sudah ada (41 halaman prototipe)
   
   - **Desain Responsif:**
     Memastikan desain bekerja pada tampilan ponsel, tablet, dan desktop
   
   - **Pertimbangan Aksesibilitas:**
     Kontras warna, ukuran huruf, navigasi keyboard, kompatibilitas pembaca layar

4. **Desain Proses (Diagram UML):**
   - **Diagram Kasus Penggunaan (*Use Case Diagram*):**
     Menunjukkan aktor (admin, terapis, klien) dan interaksi mereka dengan sistem (kasus penggunaan)
   
   - **Diagram Aktivitas (*Activity Diagram*):**
     Menggambarkan alur kerja atau proses bisnis seperti alur pemesanan, alur pembayaran, alur dokumentasi sesi
   
   - **Diagram Urutan (*Sequence Diagram*):**
     Menunjukkan interaksi antar objek/komponen dalam skenario tertentu (misalnya, urutan pembuatan pemesanan)
   
   - **Diagram Kelas (*Class Diagram*) (Opsional):**
     Menunjukkan kelas dalam sistem dengan atribut, metode, dan hubungan

5. **Desain Keamanan:**
   - Merancang mekanisme autentikasi (Laravel Sanctum/autentikasi bawaan)
   - Merancang otorisasi (kontrol akses berbasis peran/*role-based access control*)
   - Strategi enkripsi data untuk informasi sensitif
   - Langkah-langkah keamanan untuk kerentanan umum (CSRF, XSS, *SQL Injection*)
   - Manajemen sesi dan kebijakan waktu habis
   - Merancang pencatatan audit

6. **Desain API (jika diperlukan):**
   - Merancang titik akhir RESTful untuk integrasi masa depan
   - Format permintaan/respons (JSON)
   - Autentikasi untuk API (*tokens*)

**Keluaran:**

- Dokumen Desain Sistem (*System Design Document*/SDD) yang mencakup:
  - Diagram Arsitektur Sistem
  - Deskripsi Tumpukan Teknologi
  - Arsitektur Penyebaran
- Dokumen Desain Basis Data:
  - Diagram Hubungan Entitas (ERD)
  - Skema Basis Data dengan definisi tabel rinci
  - Kamus Data
  - Contoh Skrip Migrasi
- Dokumen Desain UI/UX:
  - Kerangka Layar (*wireframes*) fidelitas rendah
  - Prototipe Fidelitas Tinggi (41 halaman)
  - Dokumentasi Sistem Desain (warna, tipografi, komponen)
  - Diagram Alur Pengguna
- Diagram UML:
  - Diagram Kasus Penggunaan
  - Diagram Aktivitas
  - Diagram Urutan
  - Diagram Kelas (jika berlaku)
- Dokumen Desain Keamanan
- Dokumen Spesifikasi API (jika berlaku)

### 3.1.3 Fase 3: Implementasi (*Implementation/Development*)

**Durasi:** Minggu 5-8 (28 hari)

**Tujuan:**
Mengembangkan sistem informasi sesuai dengan spesifikasi desain yang telah dibuat pada fase sebelumnya.

**Aktivitas:**

1. **Penyiapan Lingkungan (*Environment Setup*):**
   - Menyiapkan lingkungan pengembangan (XAMPP/Laragon, VS Code, Git)
   - Memasang Laravel 10.x dan dependensi (paket Composer)
   - Mengonfigurasi basis data (MySQL)
   - Memasang dependensi antarmuka (*frontend*): Node.js, NPM, Tailwind CSS
   - Menyiapkan kontrol versi (repositori Git)

2. **Implementasi Basis Data:**
   - Membuat basis data dan tabel menggunakan migrasi Laravel
   - Menyiapkan hubungan dalam model Eloquent
   - Membuat *seeders* untuk data contoh
   - Menguji koneksi basis data dan kueri

3. **Pengembangan *Backend*:**
   - **Sistem Autentikasi:**
     - Mengimplementasikan registrasi pengguna (multi-peran: admin, terapis, klien)
     - Fungsionalitas *login*/*logout* dengan manajemen sesi
     - Verifikasi email
     - Fungsionalitas *reset password*
     - Manajemen profil
   
   - **Pengembangan *Models*:**
     - Membuat *models* Eloquent untuk setiap entitas
     - Mendefinisikan relasi (*hasOne*, *hasMany*, *belongsTo*, *belongsToMany*)
     - Mengimplementasikan *accessors* dan *mutators* jika diperlukan
     - Menambahkan aturan validasi
   
   - **Pengembangan *Controllers*:**
     - Membuat *controllers* untuk setiap modul (BookingController, UserController, PaymentController, dll.)
     - Mengimplementasikan operasi CRUD (*Create*, *Read*, *Update*, *Delete*)
     - Menangani pengiriman formulir dan validasi
     - Menyiapkan data untuk *views*
   
   - **Implementasi Logika Bisnis:**
     - Logika alur pemesanan (pemilihan layanan, pemilihan terapis, penjadwalan, konfirmasi)
     - Algoritma pemeriksaan ketersediaan
     - Integrasi pemrosesan pembayaran
     - Pemicu notifikasi (email, SMS)
     - Logika pelaporan dan analitik
   
   - **Implementasi *Middleware*:**
     - *Middleware* kontrol akses berbasis peran
     - *Middleware* autentikasi untuk rute yang dilindungi
     - *Middleware* khusus untuk kebutuhan spesifik
   
   - **Lapisan Layanan (*Service Layer*, Opsional):**
     - Mengekstrak logika bisnis kompleks ke dalam kelas layanan untuk *reusability* dan *testability*

4. **Pengembangan *Frontend*:**
   - **Template Tata Letak:**
     - Membuat tata letak utama (*master layout*) dengan Blade
     - Komponen *header*, *sidebar*, *footer*
     - Menu navigasi responsif
   
   - **Halaman Publik:**
     - *Landing page* dengan bagian hero, tinjauan layanan, testimoni
     - Halaman Tentang Kami
     - Halaman katalog layanan
     - Halaman direktori terapis
     - Halaman blog/artikel
     - Halaman kontak dan FAQ
   
   - **Halaman Autentikasi:**
     - Halaman *login* dengan validasi formulir
     - Halaman registrasi (terpisah untuk klien dan terapis)
     - Halaman lupa *password*
     - Halaman *reset password*
   
   - ***Dashboard* Klien:**
     - Tinjauan *dashboard* dengan kartu ringkasan
     - Alur pemesanan (4 langkah: layanan, terapis, jadwal, konfirmasi)
     - Janji temu saya (tampilan daftar dan kalender)
     - Riwayat pemesanan
     - Pelacakan kemajuan dengan grafik
     - Kotak masuk pesan
     - Riwayat pembayaran
   
   - ***Dashboard* Terapis:**
     - Tinjauan *dashboard* dengan statistik
     - Manajemen jadwal (tampilan kalender)
     - Pengaturan ketersediaan
     - Daftar klien dengan detail
     - Antarmuka ruang sesi
     - Editor catatan sesi dengan template
     - Riwayat sesi
     - *Dashboard* pendapatan dengan grafik
     - Pengaturan profil
   
   - ***Dashboard* Admin:**
     - Tinjauan *dashboard* dengan KPI
     - Manajemen pengguna (operasi CRUD)
     - Persetujuan dan manajemen terapis
     - Manajemen layanan
     - Manajemen pemesanan
     - Verifikasi pembayaran
     - Laporan keuangan dengan visualisasi
     - Pengaturan sistem
   
   - **Penataan Gaya dengan Tailwind CSS:**
     - Menerapkan kelas utilitas untuk penataan gaya
     - Memastikan desain responsif di berbagai perangkat
     - Menyesuaikan konfigurasi Tailwind untuk warna dan gaya merek
     - Membuat komponen yang dapat digunakan kembali
   
   - **Elemen Interaktif dengan JavaScript:**
     - Validasi formulir
     - Interaksi kalender dinamis
     - Dialog modal
     - Permintaan AJAX untuk operasi asinkron
     - Grafik dan visualisasi (Chart.js atau ApexCharts)

5. **Integration:**
   - **Integrasi Gerbang Pembayaran (*Payment Gateway*):**
     - Mengintegrasikan dengan Midtrans atau Xendit untuk pembayaran daring
     - Mengonfigurasi *webhooks* untuk notifikasi pembayaran
     - Menguji alur pembayaran (lingkungan *sandbox*)
   
   - **Integrasi Layanan Email:**
     - Mengonfigurasi SMTP untuk pengiriman email
     - Membuat templat email (notifikasi, verifikasi, tanda terima)
     - Menguji pengiriman email
   
   - **Integrasi Layanan SMS (Opsional):**
     - Mengintegrasikan dengan *gateway* SMS untuk notifikasi SMS
     - Membuat templat SMS
   
   - **Integrasi Konferensi Video (Opsional):**
     - Menanamkan Zoom, Google Meet, atau Whereby untuk ruang sesi

6. **Jaminan Kualitas Kode:**
   - Tinjauan dan refaktorisasi kode
   - Mengikuti praktik terbaik Laravel dan standar pengkodean
   - Menambahkan komentar pada kode untuk pemeliharaan yang lebih baik
   - Komit kontrol versi dengan pesan yang bermakna

**Keluaran:**

- Aplikasi Web yang Berfungsi:
  - Kode *backend* (Model, *Controller*, *Middleware*, Layanan)
  - Kode *frontend* (tampilan Blade, CSS, JavaScript)
  - Basis data dengan data contoh
- Repositori Kode Sumber (GitHub) dengan riwayat komit yang baik
- Berkas Konfigurasi dan dokumentasi Variabel Lingkungan
- Dokumentasi Integrasi API (Gerbang Pembayaran, Email, SMS)

### 3.1.4 Fase 4: Pengujian (*Testing*)

**Durasi:** Minggu 9-10 (14 hari)

**Tujuan:**
Memastikan bahwa sistem bekerja dengan benar, memenuhi kebutuhan, bebas dari kesalahan kritis, dan memberikan pengalaman pengguna yang baik.

**Aktivitas:**

1. **Pengujian Unit (*Unit Testing*):**
   - Menguji fungsi atau metode individual
   - Menggunakan PHPUnit (kerangka pengujian bawaan Laravel)
   - Menulis kasus uji untuk logika bisnis yang kritis
   - Memastikan cakupan kode pada fungsi inti
   - Pengujian otomatis untuk pencegahan regresi

2. **Pengujian Integrasi (*Integration Testing*):**
   - Menguji interaksi antar modul atau komponen
   - Menguji operasi basis data (CRUD)
   - Menguji integrasi API (gerbang pembayaran, layanan email)
   - Menguji alur autentikasi dan otorisasi

3. **Pengujian Fungsional (*Functional Testing/Black-Box Testing*):**
   - **Pembuatan Rencana Uji:**
     - Mendefinisikan skenario uji berdasarkan kebutuhan fungsional
     - Membuat kasus uji dengan hasil yang diharapkan
   
   - **Pelaksanaan Pengujian:**
     - Menguji semua fitur sesuai kasus uji:
       - Autentikasi (pendaftaran, masuk, keluar, pengaturan ulang kata sandi)
       - Alur pemesanan (semua 4 langkah)
       - Manajemen janji temu (buat, lihat, jadwal ulang, batalkan)
       - Penjadwalan terapis
       - Dokumentasi sesi
       - Pemrosesan pembayaran
       - Notifikasi (verifikasi email, konfirmasi pemesanan, pengingat)
       - Fitur dasbor (statistik, grafik)
       - Operasi admin (manajemen pengguna, manajemen layanan, pelaporan)
   
   - **Pelacakan Kesalahan (*Bug Tracking*):**
     - Mendokumentasikan kesalahan yang ditemukan dengan rinci (langkah untuk mereproduksi, perilaku yang diharapkan vs aktual, tingkat keparahan)
     - Memprioritaskan kesalahan (kritis, mayor, minor, trivial)
     - Melacak kemajuan perbaikan kesalahan

4. **Pengujian Kegunaan (*Usability Testing*):**
   - **Perekrutan Peserta:**
     - Merekrut pengguna sampel (calon klien, terapis, admin)
     - Total 10-15 peserta yang mewakili berbagai peran pengguna
   
   - **Skenario Pengujian:**
     - Mendefinisikan tugas untuk peserta (misalnya, "Pesan sesi terapi", "Periksa janji temu Anda")
   
   - **Pelaksanaan Pengujian:**
     - Mengamati peserta saat menggunakan sistem
     - Mencatat waktu untuk menyelesaikan tugas, tingkat keberhasilan, kesalahan yang dibuat
     - Mencatat area yang membingungkan atau sulit
   
   - **Pengumpulan Umpan Balik:**
     - Kuesioner pasca-uji (*System Usability Scale*/SUS)
     - Wawancara untuk mengumpulkan umpan balik kualitatif
     - Saran untuk perbaikan
   
   - **Analisis:**
     - Menganalisis metrik kegunaan
     - Mengidentifikasi masalah UI/UX
     - Memprioritaskan perbaikan

5. **Pengujian Kinerja (*Performance Testing*):**
   - **Pengujian Beban (*Load Testing*):**
     - Mensimulasikan banyak pengguna bersamaan
     - Menguji kinerja sistem di bawah beban yang diharapkan
   
   - **Pengujian Stres (*Stress Testing*):**
     - Menguji batas sistem dengan beban ekstrem
     - Mengidentifikasi titik kegagalan
   
   - **Pengujian Waktu Respons:**
     - Mengukur waktu muat halaman
     - Memastikan kinerja yang dapat diterima (< 3 detik untuk sebagian besar halaman)
   
   - **Optimasi Kueri Basis Data:**
     - Mengidentifikasi kueri lambat dengan Laravel Debugbar
     - Mengoptimalkan kueri dengan pengindeksan yang tepat dan optimasi kueri

6. **Pengujian Keamanan (*Security Testing*):**
   - **Pemindaian Kerentanan:**
     - Menguji kerentanan umum (*SQL Injection*, XSS, CSRF)
     - Menggunakan alat otomatis (OWASP ZAP, Burp Suite Community Edition)
   
   - **Pengujian Penetrasi Dasar (*Penetration Testing*):**
     - Mencoba akses tidak sah
     - Menguji bypass autentikasi
     - Menguji pelanggaran otorisasi (kontrol akses)
   
   - **Tinjauan Kode untuk Keamanan:**
     - Meninjau kode untuk praktik terbaik keamanan
     - Memastikan enkripsi data sensitif
     - Memvalidasi sanitasi masukan

7. **Pengujian Penerimaan Pengguna (*User Acceptance Testing*/UAT):**
   - **Perencanaan UAT:**
     - Menyiapkan rencana UAT dan kasus uji
     - Menjadwalkan sesi UAT dengan pemangku kepentingan CUR-HEART
   
   - **Pelaksanaan UAT:**
     - Mempresentasikan sistem kepada pemangku kepentingan
     - Pemangku kepentingan menguji sistem dengan skenario nyata
     - Mengumpulkan umpan balik dan persetujuan
   
   - **Persetujuan:**
     - Memperoleh persetujuan formal dari pemangku kepentingan
     - Mendokumentasikan permintaan perubahan menit terakhir

8. **Perbaikan Kesalahan dan Pengujian Ulang:**
   - Memprioritaskan dan memperbaiki kesalahan kritis dan mayor
   - Menguji ulang kesalahan yang diperbaiki untuk memastikan penyelesaian
   - Pengujian regresi untuk memastikan perbaikan tidak merusak fitur lain
   - Siklus pengujian berulang hingga kualitas yang dapat diterima tercapai

**Keluaran:**

- Dokumen Rencana Pengujian
- Kasus Uji dengan langkah rinci dan hasil yang diharapkan
- Laporan Hasil Pengujian dengan status lulus/gagal
- Laporan Kesalahan dengan deskripsi, tangkapan layar, tingkat keparahan
- Laporan Pengujian Kegunaan dengan skor SUS dan ringkasan umpan balik
- Laporan Pengujian Kinerja dengan waktu respons dan kapasitas beban
- Laporan Audit Keamanan
- Laporan UAT dengan persetujuan pemangku kepentingan
- Aplikasi yang Telah Diperbaiki dan Diuji siap untuk penyebaran

### 3.1.5 Fase 5: Penyebaran (*Deployment*) ke Lingkungan Produksi

**Durasi:** Minggu 11 (7 hari)

**Tujuan:**
Menyebarkan sistem ke lingkungan produksi sehingga dapat diakses dan digunakan oleh pengguna akhir secara nyata.

**Aktivitas:**

1. **Persiapan Pra-Penyebaran:**
   - Tinjauan dan pembersihan kode akhir
   - Memperbarui dokumentasi (README, panduan penyebaran, manual pengguna)
   - Menyiapkan catatan rilis
   - Membuat rencana cadangan dan prosedur pemulihan
   - Menguji proses penyebaran di lingkungan *staging* (jika ada)

2. **Penyiapan Lingkungan Produksi:**
   - **Penyediaan Server:**
     - Menyiapkan server web (Apache atau Nginx)
     - Memasang PHP 8.x dengan ekstensi yang diperlukan
     - Memasang MySQL 8.0
     - Mengonfigurasi *firewall* dan pengaturan keamanan
   
   - **Domain dan SSL:**
     - Mengonfigurasi nama domain (curheart.com atau subdomain)
     - Memasang sertifikat SSL untuk HTTPS (Let's Encrypt)
   
   - **Penyebaran Aplikasi:**
     - Mengunggah kode sumber ke server (via FTP, Git, atau SSH)
     - Memasang dependensi Composer (`composer install --optimize-autoloader --no-dev`)
     - Memasang dependensi NPM dan membangun aset (`npm install && npm run build`)
     - Menyiapkan variabel lingkungan (berkas `.env` dengan pengaturan produksi)
     - Menjalankan migrasi basis data (`php artisan migrate --force`)
     - Mengisi data awal jika diperlukan (`php artisan db:seed`)
     - Mengatur izin berkas yang tepat
     - Mengonfigurasi *cron jobs* untuk Laravel Scheduler
     - Mengonfigurasi *queue workers* untuk pekerjaan latar belakang

3. **Konfigurasi:**
   - **Konfigurasi Aplikasi:**
     - Mengatur APP_ENV=production
     - Mengatur APP_DEBUG=false untuk keamanan
     - Mengonfigurasi *cache drivers* (file, Redis, atau Memcached)
     - Mengonfigurasi *session* dan *queue drivers*
   
   - **Konfigurasi Basis Data:**
     - Membuat basis data produksi
     - Mengonfigurasi kredensial basis data di `.env`
     - Mengoptimalkan pengaturan basis data untuk produksi
   
   - **Konfigurasi Layanan Pihak Ketiga:**
     - Mengonfigurasi gerbang pembayaran dengan *API keys* produksi
     - Mengonfigurasi layanan email dengan pengaturan SMTP produksi
     - Mengonfigurasi layanan SMS (jika ada)
     - Menyiapkan *webhooks* untuk notifikasi pembayaran

4. **Pengujian di Lingkungan Produksi:**
   - Pengujian asap (*smoke testing*) semua fitur kritis
   - Menguji integrasi (pembayaran, email, SMS)
   - Menguji dari berbagai perangkat dan peramban
   - Memastikan SSL berfungsi dengan baik
   - Menguji kinerja dan waktu respons

5. **Penyiapan Pemantauan:**
   - Menyiapkan pencatatan kesalahan (berkas log Laravel)
   - Mengonfigurasi pelaporan pengecualian (misalnya, Sentry, Bugsnag)
   - Menyiapkan pemantauan waktu aktif (misalnya, UptimeRobot)
   - Mengonfigurasi pemantauan server (CPU, RAM, penggunaan disk)
   - Menyiapkan cadangan otomatis (cadangan basis data harian)

6. **Peluncuran (*Go-Live*):**
   - Pemeriksaan akhir sebelum peluncuran
   - Mengumumkan peluncuran kepada pemangku kepentingan
   - Memantau dengan cermat untuk masalah apa pun
   - Bersiap untuk perbaikan cepat jika ada masalah kritis

7. **Aktivitas Pasca-Penyebaran:**
   - **Pelatihan Pengguna:**
     - Melakukan sesi pelatihan untuk admin dan terapis
     - Menyediakan manual pengguna dan tutorial video
     - Membuat tanya jawab dan panduan pemecahan masalah
   
   - **Migrasi Data (jika ada):**
     - Memindahkan data dari sistem lama (jika berlaku)
     - Memverifikasi integritas data pasca-migrasi
   
   - **Pengumuman kepada Klien:**
     - Menginformasikan klien yang ada tentang sistem baru
     - Menyediakan instruksi untuk pendaftaran dan pemesanan
     - Menawarkan dukungan untuk orientasi

**Keluaran:**

- Aplikasi Web yang Dapat Diakses melalui domain dengan HTTPS
- Dokumentasi Penyebaran (penyiapan server, konfigurasi, langkah-langkah penyebaran)
- Rencana dan Prosedur Pemulihan
- Manual Pengguna (Manual Admin, Manual Terapis, Manual Klien)
- Materi Pelatihan (presentasi, tutorial video)
- Sistem Pemantauan dan Pencatatan yang dikonfigurasi
- Sistem Cadangan yang dikonfigurasi dan diuji

### 3.1.6 Fase 6: Pemeliharaan dan Evaluasi (*Maintenance* dan Evaluasi) (Berkelanjutan)

**Durasi:** Pasca-penyebaran (Berkelanjutan)

**Tujuan:**
Memastikan sistem tetap berjalan dengan baik, mengatasi masalah yang muncul, dan melakukan perbaikan berdasarkan umpan balik pengguna.

**Aktivitas:**

1. **Pemantauan dan Pencatatan:**
   - Pemantauan harian waktu aktif sistem dan kinerja
   - Meninjau catatan kesalahan untuk mengidentifikasi masalah
   - Memantau sumber daya server (CPU, RAM, disk, *bandwidth*)
   - Melacak metrik aplikasi (pengguna, pemesanan, pendapatan)

2. **Perbaikan Kesalahan (*Bug Fixing*):**
   - Merespons laporan kesalahan dari pengguna
   - Memprioritaskan kesalahan berdasarkan keparahan dan dampak
   - Mengembangkan perbaikan dan menyebarkan tambalan
   - Berkomunikasi dengan pengguna tentang penyelesaian kesalahan

3. **Dukungan Pengguna:**
   - Menyediakan dukungan teknis kepada pengguna
   - Menjawab pertanyaan melalui email, telepon, atau obrolan langsung
   - Membuat artikel basis pengetahuan untuk masalah umum
   - Mengumpulkan umpan balik dan permintaan fitur

4. **Optimasi Kinerja:**
   - Mengidentifikasi kemacetan kinerja
   - Mengoptimalkan kueri basis data yang lambat
   - Menerapkan strategi *caching* (*query caching*, *view caching*, *route caching*)
   - Optimasi gambar
   - Optimasi kode

5. **Pembaruan Keamanan:**
   - Menerapkan tambalan keamanan untuk Laravel dan dependensi
   - Memantau kerentanan keamanan
   - Memperbarui sertifikat SSL sebelum kedaluwarsa
   - Audit keamanan berkala

6. **Cadangan dan Pemulihan Bencana:**
   - Memastikan cadangan otomatis berjalan dengan baik
   - Menguji pemulihan cadangan secara berkala
   - Memelihara rencana pemulihan bencana

7. **Peningkatan Fitur:**
   - Mengevaluasi permintaan fitur dari pengguna
   - Memprioritaskan peningkatan berdasarkan nilai dan upaya
   - Mengembangkan dan menyebarkan fitur baru secara bertahap
   - Mengkomunikasikan pembaruan kepada pengguna

8. **Evaluasi dan Pelaporan:**
   - **Pengumpulan Metrik:**
     - Mengumpulkan metrik penggunaan (pengguna aktif harian, volume pemesanan, tingkat konversi)
     - Mengukur kinerja sistem (waktu aktif, waktu respons)
     - Melacak metrik bisnis (pendapatan, kepuasan pelanggan)
   
   - **Analisis:**
     - Menganalisis tren dan pola
     - Mengidentifikasi area untuk perbaikan
     - Menghitung *Return on Investment* (ROI) dari sistem
   
   - **Pelaporan:**
     - Membuat laporan bulanan untuk manajemen
     - Mempresentasikan temuan dan rekomendasi
     - Merayakan keberhasilan dan mengatasi tantangan

9. **Perbaikan Berkelanjutan (*Continuous Improvement*):**
   - Meninjau sistem dan proses secara teratur
   - Menerapkan pelajaran yang dipetik
   - Tetap mengikuti pembaruan Laravel dan praktik terbaik
   - Merencanakan peningkatan dan skalabilitas masa depan

**Keluaran:**

- Laporan Pemeliharaan Bulanan
- Catatan Perbaikan Kesalahan dengan penyelesaian
- Laporan Metrik Kinerja
- Hasil Survei Kepuasan Pengguna
- Peta Jalan Peningkatan Fitur
- Dokumentasi yang Diperbarui
- Dasbor Kesehatan Sistem

---

## 3.2 Tempat dan Waktu Penelitian

### 3.2.1 Tempat Penelitian

Penelitian dan pengembangan sistem informasi ini dilaksanakan di beberapa lokasi:

1. **CUR-HEART (*Hypnotherapy & Mind Wellness Center*)**
   - Alamat: [Alamat CUR-HEART - dapat disesuaikan dengan lokasi aktual]
   - Kegiatan: Observasi proses bisnis, wawancara dengan pemangku kepentingan, pengujian penerimaan pengguna
   - Periode: Minggu 1-2 (Analisis Kebutuhan) dan Minggu 10 (UAT)

2. **Universitas Nusa Mandiri - Kampus Margonda**
   - Alamat: Jl. Margonda Raya No. 100, Depok, Jawa Barat
   - Kegiatan: Pengembangan, konsultasi dengan dosen pembimbing, koordinasi tim
   - Periode: Minggu 1-11 (sepanjang proyek)

3. **Jarak Jauh/Daring (*Remote/Online*) - Bekerja dari Rumah**
   - Kegiatan: Pengembangan, dokumentasi, pengujian, koordinasi tim melalui alat daring
   - Periode: Mayoritas waktu pengembangan (Minggu 3-9)

### 3.2.2 Waktu Penelitian

Penelitian dilaksanakan dalam satu semester akademik dengan total durasi 11 minggu, dari pertengahan September 2024 hingga awal Desember 2024.

---

**Tabel 3.1 Jadwal Penelitian dan Pengembangan Sistem**

| No | Fase | Minggu | Tanggal Mulai | Tanggal Selesai | Durasi (Hari) | Aktivitas Utama | Deliverables | PIC | Status (Nov 2024) |
|----|------|--------|---------------|-----------------|---------------|----------------|-------------|-----|------------------|
| **1** | **Analisis Kebutuhan** | 1-2 | 16 Sep 2024 | 29 Sep 2024 | 14 | • Observasi proses bisnis<br>• Wawancara pemangku kepentingan<br>• Studi literatur<br>• Analisis dokumen<br>• Pengumpulan kebutuhan | • Dokumen SRS<br>• Studi Kelayakan<br>• Diagram Alir Proses Bisnis<br>• Transkrip Wawancara | Semua Tim | ✅ **SELESAI** |
| **2** | **Desain Sistem** | 3-4 | 30 Sep 2024 | 13 Okt 2024 | 14 | • Desain basis data (ERD, skema)<br>• Desain UI/UX (*wireframe*, *mockup*)<br>• Desain arsitektur sistem<br>• Diagram UML (*Use Case*, *Activity*, *Sequence*)<br>• Pembuatan prototipe (Figma) | • Dokumen Desain Sistem<br>• ERD & Skema Basis Data<br>• *Mockups* UI/UX (Figma)<br>• Diagram UML<br>• Prototipe Interaktif | Susanto (UI/UX)<br>Fahruroji (BD)<br>Roki (Arsitek) | ✅ **SELESAI** |
| **3** | **Implementasi** | 5-8 | 14 Okt 2024 | 10 Nov 2024 | 28 | **Minggu 5-6**: Pengembangan *backend*<br>• Penyiapan & konfigurasi Laravel<br>• Migrasi & pengisian basis data<br>• Autentikasi & otorisasi<br>• Modul inti (Pengguna, Layanan)<br><br>**Minggu 7**: Fitur inti<br>• Implementasi sistem pemesanan<br>• Integrasi pembayaran (Midtrans)<br>• Dasbor terapis<br><br>**Minggu 8**: Fitur lanjutan<br>• Catatan sesi & pelacakan kemajuan<br>• Dasbor admin & laporan<br>• Dasbor klien | • Aplikasi Laravel yang Berfungsi<br>• Basis data dengan data contoh<br>• Sistem autentikasi<br>• Modul pemesanan<br>• Integrasi pembayaran<br>• Dasbor terapis<br>• Dasbor admin<br>• Dasbor klien<br>• Repositori Git | Roki (*Backend*)<br>Susanto (*Frontend*)<br>Fahruroji (*Full-stack*) | ✅ **SELESAI** |
| **4** | **Pengujian** | 9-10 | 11 Nov 2024 | 24 Nov 2024 | 14 | **Minggu 9**: Pengujian pengembang<br>• Pengujian unit (PHPUnit)<br>• Pengujian integrasi<br>• Pengujian fungsional<br>• Perbaikan kesalahan<br><br>**Minggu 10**: Pengujian pengguna<br>• Pengujian kegunaan (SUS)<br>• Pengujian Penerimaan Pengguna (UAT)<br>• Pengujian kinerja<br>• Pengujian keamanan | • Dokumen Kasus Uji<br>• Hasil Pengujian Unit<br>• Hasil Pengujian UAT<br>• Laporan & Perbaikan Kesalahan<br>• Hasil Skor SUS<br>• Hasil Pengujian Kinerja | Semua Tim + 10 peserta UAT | ✅ **SELESAI** |
| **5** | **Penyebaran** | 11 | 25 Nov 2024 | 1 Des 2024 | 7 | • Penyiapan server (konfigurasi VPS)<br>• Migrasi basis data ke produksi<br>• Penyebaran aplikasi<br>• Konfigurasi SSL<br>• Penyiapan domain<br>• Penyiapan pemantauan<br>• Pelatihan pengguna<br>• Peluncuran | • Sistem Produksi (langsung)<br>• Manual Pengguna<br>• Manual Admin<br>• Materi Pelatihan<br>• Daftar Periksa Penyebaran<br>• Dasbor Pemantauan | Roki (DevOps)<br>Fahruroji (migrasi BD) | ✅ **SELESAI** |
| **6** | **Pemeliharaan & Evaluasi** | Berkelanjutan | 2 Des 2024 | Berkelanjutan | - | • Pemantauan & perbaikan kesalahan<br>• Dukungan pengguna<br>• Optimasi kinerja<br>• Peningkatan fitur (jika diperlukan)<br>• Evaluasi sistem | • Catatan Perbaikan Kesalahan<br>• Laporan Umpan Balik Pengguna<br>• Laporan Kinerja Sistem<br>• Rekomendasi Perbaikan | Semua Tim (*on-call*) | ⏳ **BERLANGSUNG** |
| **7** | **Dokumentasi Laporan** | 12-14 | 2 Des 2024 | 22 Des 2024 | 21 | • Penyusunan laporan akhir<br>• Dokumentasi teknis<br>• Dokumentasi pengguna<br>• Tinjauan & revisi laporan | • Laporan Akhir *Capstone* (80-100 hal)<br>• Dokumentasi Teknis<br>• Panduan Pengguna<br>• Dokumentasi API | Semua Tim | ⏳ **SEDANG BERLANGSUNG** |
| **8** | **Persiapan Presentasi** | 15 | 23 Des 2024 | 29 Des 2024 | 7 | • Persiapan slide presentasi<br>• Latihan presentasi<br>• Persiapan demo<br>• Persiapan tanya jawab | • Slide Presentasi<br>• Skrip Demo<br>• Dokumen Tanya Jawab | Semua Tim | 🔜 **AKAN DATANG** |
| **9** | **Presentasi Final** | 16 | 30 Des 2024 | 30 Des 2024 | 1 | • Presentasi proyek akhir<br>• Demo sistem langsung<br>• Sesi tanya jawab<br>• Sidang | • Presentasi Akhir<br>• Demo Langsung<br>• Nilai Akhir | Semua Tim | 🔜 **AKAN DATANG** |

**Ringkasan Waktu:**
- **Durasi Total Penelitian & Pengembangan**: 11 minggu (16 Sep - 1 Des 2024)
- **Durasi Total Proyek (termasuk dokumentasi & presentasi)**: 16 minggu (16 Sep - 30 Des 2024)
- **Pengembangan Inti**: 4 minggu (14 Okt - 10 Nov 2024)
- **Pengujian & Penyebaran**: 3 minggu (11 Nov - 1 Des 2024)

**Tonggak Kritis:**

| Tonggak | Tanggal Target | Status | Catatan |
|---------|---------------|--------|---------|
| Persetujuan Kebutuhan | 29 Sep 2024 | ✅ Selesai | SRS ditandatangani oleh pemilik CUR-HEART |
| Tinjauan Desain | 13 Okt 2024 | ✅ Selesai | *Mockups* & ERD disetujui |
| Penyelesaian MVP *Backend* | 27 Okt 2024 | ✅ Selesai | Alur pemesanan inti berfungsi |
| Penyelesaian Fitur | 10 Nov 2024 | ✅ Selesai | Semua modul diimplementasikan |
| Persetujuan UAT | 24 Nov 2024 | ✅ Selesai | 90% kebutuhan fungsional terpenuhi |
| Peluncuran | 1 Des 2024 | ✅ Selesai | Sistem disebarkan ke produksi |
| Draf Laporan Selesai | 22 Des 2024 | ⏳ Sedang Berlangsung | 80% selesai per 2 Nov 2024 |
| Presentasi Akhir | 30 Des 2024 | 🔜 Akan Datang | Persiapan sidang sedang berlangsung |

**Gantt Chart:**

```
Fase                      | Minggu
                          | 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
------------------------------------------------------------------------------
1. Analisis Kebutuhan     |████████
2. Desain Sistem          |        ████████
3. Implementasi           |                ████████████████████████████
4. Pengujian              |                                            ████████████████
5. Penyebaran             |                                                            ████████
6. Pemeliharaan & Evaluasi|                                                                    ━━━━━━━━→
7. Dokumentasi Laporan    |                                                                ████████████████████████
8. Persiapan Presentasi   |                                                                                    ████████
9. Presentasi Final       |                                                                                            ██
```

**Alokasi Sumber Daya:**

| Fase | Roki Anjas (Pemimpin/*Backend*) | Susanto (*Frontend*/UI) | Fahruroji (*Full-stack*/DB) | Total Hari-Orang |
|------|---------------------------|---------------------|-------------------------|------------------|
| Analisis Kebutuhan | 14 hari | 14 hari | 14 hari | 42 hari-orang |
| Desain Sistem | 14 hari | 14 hari | 14 hari | 42 hari-orang |
| Implementasi | 28 hari | 28 hari | 28 hari | 84 hari-orang |
| Pengujian | 14 hari | 14 hari | 14 hari | 42 hari-orang |
| Penyebaran | 7 hari | 7 hari | 7 hari | 21 hari-orang |
| **TOTAL** | **77 hari** | **77 hari** | **77 hari** | **231 hari-orang** |

**Risiko & Mitigasi:**

| Risiko | Probabilitas | Dampak | Strategi Mitigasi | Status |
|--------|-------------|--------|-------------------|--------|
| Keterlambatan waktu (hari libur nasional) | Sedang | Tinggi | Waktu cadangan dimasukkan ke jadwal (10%) | ✅ Dimitigasi |
| Tantangan teknis (integrasi pembayaran) | Sedang | Sedang | Pembuatan prototipe awal, studi dokumentasi | ✅ Dimitigasi |
| Ketersediaan pemangku kepentingan untuk UAT | Tinggi | Sedang | Jadwal pengujian fleksibel, opsi pengujian daring | ✅ Dimitigasi |
| Perluasan cakupan (*scope creep*) | Sedang | Tinggi | Prioritas MoSCoW, proses kontrol perubahan | ✅ Terkontrol |
| Sakit anggota tim | Rendah | Tinggi | Berbagi pengetahuan, dokumentasi, keterampilan tumpang tindih | ✅ Tidak ada masalah |

---

**[GAMBAR 3.3 - Gantt Chart Timeline Penelitian (11 Minggu)]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT GANTT CHART DIAGRAM]                             │
│                                                             │
│   Timeline: 16 Sep 2024 - 1 Des 2024 (11 weeks)            │
│                                                             │
│   Fase Proyek                  Minggu                       │
│                          | 1  2  3  4  5  6  7  8  9  10 11│
│   ──────────────────────────────────────────────────────────│
│   1. Analisis Kebutuhan  |████████                          │
│      (Minggu 1-2)        |                                  │
│                          |                                  │
│   2. Desain Sistem       |        ████████                  │
│      (Minggu 3-4)        |                                  │
│                          |                                  │
│   3. Implementasi        |                ████████████████  │
│      (Minggu 5-8)        |                                  │
│                          |                                  │
│   4. Pengujian           |                                ████████│
│      (Minggu 9-10)       |                                  │
│                          |                                  │
│   5. Penyebaran          |                                      ████│
│      (Minggu 11)         |                                  │
│                          |                                  │
│   6. Pemeliharaan        |                                          →│
│      (Berkelanjutan)     |                                  │
│   ──────────────────────────────────────────────────────────│
│                                                             │
│   Pencapaian Penting (*Milestones*):                       │
│   ⭐ Minggu 2: Persetujuan SRS                              │
│   ⭐ Minggu 4: Tinjauan Desain                              │
│   ⭐ Minggu 8: Fitur Lengkap                                │
│   ⭐ Minggu 10: Persetujuan UAT                             │
│   ⭐ Minggu 11: Peluncuran (*Go-Live*)                      │
│                                                             │
│   Tim: 3 Pengembang (Roki, Susanto, Fahruroji)             │
│   Total: 231 hari-orang (77 hari × 3 orang)                │
│                                                             │
│   Format: Gantt Chart PNG/JPG                              │
│   Ukuran yang disarankan: 1400x800px                       │
│   Gaya: Profesional dengan kode warna per fase             │
│                                                             │
│   File: assets/images/gantt-chart-timeline-11-weeks.png    │
│   Alat: Microsoft Project, GanttProject, atau Excel        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 3.3: Gantt Chart *timeline* penelitian selama 11 minggu (16 Sep - 1 Des 2024) menunjukkan 6 fase SDLC dengan total 231 hari-orang dan 5 pencapaian penting (*milestone*) kunci_

---

## 3.3 Subjek Penelitian

Subjek penelitian dalam pengembangan sistem informasi CUR-HEART terdiri dari beberapa kategori pemangku kepentingan yang terlibat langsung dalam sistem:

---

**Tabel 3.2 Analisis Pemangku Kepentingan & Matriks Keterlibatan**

| No | Kelompok Pemangku Kepentingan | Jumlah | Identitas/Deskripsi | Peran dalam Proyek | Tanggung Jawab | Fase Keterlibatan | Frekuensi Komunikasi | Metode Komunikasi | Tingkat Pengaruh | Kontribusi yang Diharapkan | Status |
|----|------------------|--------|---------------------|-------------------|-----------------|------------------|---------------------|------------------|----------------|-----------------------------------|--------|
| **A** | **INTERNAL CUR-HEART** | | | | | | | | | | |
| 1 | Pemilik/Manajemen | 1 | Pemilik CUR-HEART *Hypnotherapy*<br>• Laki-laki, 45 tahun<br>• Hipnoterapis Klinis<br>• 10+ tahun pengalaman | Pengambil Keputusan<br>Sponsor Proyek<br>Pemberi Persetujuan Akhir | • Mendefinisikan tujuan bisnis & KPI<br>• Persetujuan kebutuhan<br>• Persetujuan anggaran<br>• Penandatanganan akhir<br>• Arahan strategis | • Analisis (Minggu 1-2)<br>• Tinjauan Desain (Minggu 4)<br>• UAT (Minggu 10)<br>• Peluncuran (Minggu 11) | **Mingguan** (Minggu 1-2)<br>**Dua mingguan** (Minggu 3-10)<br>**Harian** (Minggu 11) | • Pertemuan tatap muka<br>• WhatsApp<br>• Email formal<br>• Telepon | **SANGAT TINGGI**<br>(10/10)<br>Memiliki kekuasaan veto atas semua keputusan | • Definisi kebutuhan bisnis<br>• Persetujuan kebutuhan<br>• Penandatanganan UAT<br>• Persetujuan peluncuran | ✅ **AKTIF** |
| 2 | Terapis Senior | 3 | **Terapis 1**: Perempuan, 38 tahun, 5 tahun pengalaman<br>**Terapis 2**: Laki-laki, 35 tahun, 4 tahun pengalaman<br>**Terapis 3**: Perempuan, 32 tahun, 3 tahun pengalaman<br>• Hipnoterapis Bersertifikat<br>• Pengguna utama sistem | Pengguna Akhir Utama<br>Kontributor Kebutuhan<br>Partisipan UAT | • Mendefinisikan kebutuhan alur kerja<br>• Kebutuhan *dashboard* terapis<br>• Kebutuhan manajemen sesi<br>• Pengujian kegunaan<br>• Pelaksanaan UAT<br>• Partisipasi pelatihan pengguna | • Analisis (Minggu 1-2): Wawancara<br>• Desain (Minggu 3-4): Tinjauan UI/UX<br>• Pengujian (Minggu 9-10): UAT<br>• Penyebaran (Minggu 11): Pelatihan | **Mingguan** (Minggu 1-2)<br>**Bulanan** (Minggu 3-8)<br>**Mingguan** (Minggu 9-11) | • Wawancara tatap muka<br>• Grup WhatsApp<br>• Sesi pengujian daring<br>• Lokakarya pelatihan | **TINGGI**<br>(8/10)<br>Masukan sangat penting untuk fitur terapis | • Dokumentasi alur kerja<br>• Kebutuhan fitur<br>• Umpan balik kegunaan<br>• Hasil pengujian UAT<br>• Umpan balik pelatihan | ✅ **AKTIF** |
| 3 | Admin/Staf | 2 | **Admin 1**: Perempuan, 28 tahun, Manajer Kantor<br>**Admin 2**: Perempuan, 25 tahun, Layanan Pelanggan<br>• Menangani pemesanan & penjadwalan<br>• Komunikasi klien | Pengguna Akhir Utama<br>Kontributor Kebutuhan<br>Partisipan UAT | • Mendefinisikan kebutuhan proses admin<br>• Alur kerja pemesanan & penjadwalan<br>• Kebutuhan manajemen klien<br>• Kebutuhan pelaporan<br>• Pengujian kegunaan<br>• Pelaksanaan UAT | • Analisis (Minggu 1-2): Wawancara & observasi<br>• Desain (Minggu 3-4): Tinjauan UI/UX<br>• Pengujian (Minggu 9-10): UAT<br>• Penyebaran (Minggu 11): Pelatihan | **Mingguan** (Minggu 1-2)<br>**Dua mingguan** (Minggu 3-8)<br>**Mingguan** (Minggu 9-11) | • Wawancara tatap muka<br>• WhatsApp<br>• Pengujian daring<br>• Lokakarya pelatihan | **TINGGI**<br>(8/10)<br>Operator sistem harian | • Dokumentasi proses saat ini<br>• Kebutuhan fitur admin<br>• Umpan balik kegunaan<br>• Hasil pengujian UAT<br>• Umpan balik pelatihan | ✅ **AKTIF** |
| **B** | **PENGGUNA EKSTERNAL (KLIEN)** | | | | | | | | | | |
| 4 | Klien Sampel | 8 | **Demografi Beragam:**<br>• 5 Perempuan, 3 Laki-laki<br>• Rentang usia: 25-45 tahun<br>• Profesi: Profesional, pengusaha, mahasiswa<br>• Kemampuan teknologi: Rendah (2), Sedang (4), Tinggi (2)<br>• Pengalaman: Klien yang ada (5), Klien potensial baru (3) | Perwakilan Pengguna Akhir<br>Penguji Kegunaan<br>Pemberi Umpan Balik | • Memberikan perspektif klien<br>• Mendefinisikan kebutuhan yang menghadap klien<br>• Pengujian kegunaan<br>• Pengujian Penerimaan Pengguna<br>• Umpan balik pada alur pemesanan, UI, fitur | • Analisis (Minggu 1-2): Wawancara (sampel 3 orang)<br>• Desain (Minggu 4): Tinjauan *mockup* (sampel 2 orang)<br>• Pengujian (Minggu 9-10): UAT (semua 8 partisipan) | **Sekali** (Minggu 1-2)<br>**Sekali** (Minggu 4)<br>**2-3x** (Minggu 9-10) | • Wawancara telepon<br>• Survei daring<br>• Pengujian kegunaan langsung<br>• Sesi UAT daring | **SEDANG**<br>(6/10)<br>Penting untuk validasi pengalaman klien | • Kebutuhan & harapan klien<br>• Preferensi pemesanan<br>• Umpan balik kegunaan<br>• Hasil UAT<br>• Skor SUS | ✅ **AKTIF** |
| **C** | **TIM PENGEMBANG** | | | | | | | | | | |
| 5 | Pemimpin Proyek & Pengembang *Backend* | 1 | **Roki Anjas (NIM: 11250066)**<br>• Mahasiswa S1 Sistem Informasi<br>• Semester 7<br>• Keterampilan: Laravel, PHP, MySQL, Git, RESTful API | Manajer Proyek<br>Pengembang *Backend* Utama<br>Arsitek Sistem<br>Koordinator Utama | • Perencanaan & manajemen proyek<br>• Desain arsitektur *backend*<br>• Pengembangan aplikasi Laravel<br>• Autentikasi & otorisasi<br>• Pengembangan API<br>• Tinjauan kode<br>• Koordinasi tim<br>• Pimpinan dokumentasi | **Semua fase** (Minggu 1-16)<br>• Memimpin semua kegiatan proyek<br>• Fokus pengodean: Minggu 5-8<br>• Integrasi: Minggu 7-8<br>• Penyebaran: Minggu 11 | **Harian** (tim internal)<br>**Mingguan** (pembimbing)<br>**Sesuai kebutuhan** (pemangku kepentingan) | • *Standup* harian (langsung/WhatsApp)<br>• GitHub (kolaborasi kode)<br>• Grup WhatsApp<br>• Pertemuan pembimbing mingguan | **SANGAT TINGGI**<br>(10/10)<br>Kesuksesan proyek bergantung pada kepemimpinan | • Rencana & jadwal proyek<br>• SRS & SDD<br>• Kode basis *backend*<br>• Dokumentasi API<br>• Dokumentasi pengujian<br>• Laporan akhir (penulis utama) | ✅ **AKTIF** |
| 6 | Pengembang *Frontend* & Perancang UI/UX | 1 | **Susanto (NIM: 11250068)**<br>• Mahasiswa S1 Sistem Informasi<br>• Semester 7<br>• Keterampilan: HTML, CSS, JavaScript, Tailwind CSS, Figma, Blade | Perancang UI/UX<br>Pengembang *Frontend*<br>Penguji Kegunaan | • Riset & desain UI/UX<br>• Pembuatan *wireframes* & *mockups*<br>• Implementasi *frontend* (Blade, Tailwind)<br>• Desain responsif<br>• Koordinasi pengujian kegunaan<br>• Pengembangan antarmuka yang menghadap klien | • Desain (Minggu 3-4): Fokus desain UI/UX<br>• Implementasi (Minggu 5-8): Pengembangan *frontend*<br>• Pengujian (Minggu 9-10): Pengujian kegunaan<br>• Semua fase: Konsistensi desain | **Harian** (tim internal)<br>**Mingguan** (tinjauan UI/UX dengan pengguna) | • *Standup* harian<br>• Figma (kolaborasi desain)<br>• GitHub<br>• WhatsApp | **TINGGI**<br>(9/10)<br>UI/UX kritis untuk penerimaan pengguna | • Laporan riset UI/UX<br>• *Wireframes* & *mockups* (Figma)<br>• Kode basis *frontend* (*views*)<br>• Rencana pengujian kegunaan<br>• Hasil evaluasi SUS | ✅ **AKTIF** |
| 7 | Pengembang *Full-Stack* & Administrator Basis Data | 1 | **Fahruroji (NIM: 11250085)**<br>• Mahasiswa S1 Sistem Informasi<br>• Semester 7<br>• Keterampilan: Laravel, PHP, MySQL, Desain Basis Data, Git | Arsitek Basis Data<br>Pengembang *Full-Stack*<br>Dukungan *DevOps* | • Desain basis data (ERD, skema)<br>• Implementasi & optimasi basis data<br>• Migrasi & pengisian data<br>• Dukungan *backend* & *frontend*<br>• Dukungan integrasi<br>• Penyiapan server & dukungan penyebaran | • Desain (Minggu 3-4): Desain basis data<br>• Implementasi (Minggu 5-8): Implementasi BD & pengembangan *full-stack*<br>• Pengujian (Minggu 9-10): Pengujian kinerja<br>• Penyebaran (Minggu 11): Migrasi BD | **Harian** (tim internal)<br>**Sesuai kebutuhan** (optimasi kinerja) | • *Standup* harian<br>• GitHub<br>• WhatsApp<br>• Dokumentasi basis data | **TINGGI**<br>(9/10)<br>Basis data kritis untuk integritas sistem | • ERD & Skema Basis Data<br>• Migrasi basis data<br>• Dokumentasi basis data<br>• Hasil pengujian kinerja<br>• Skrip penyebaran | ✅ **AKTIF** |
| **D** | **PEMBIMBINGAN AKADEMIK** | | | | | | | | | | |
| 8 | Dosen Pembimbing | 1 | **Rani Irma Handayani, M.Kom**<br>• Dosen Sistem Informasi UNM<br>• Keahlian: Rekayasa Perangkat Lunak, Sistem Informasi, Manajemen Proyek | Pembimbing Akademik<br>Penasihat Teknis<br>Jaminan Kualitas<br>Penilai Akhir | • Pemantauan kemajuan mingguan<br>• Bimbingan teknis<br>• Validasi metodologi<br>• Tinjauan dokumentasi<br>• Konsultasi pemecahan masalah<br>• Evaluasi & penilaian akhir | **Semua fase** (Minggu 1-16)<br>• Konsultasi mingguan<br>• Tinjauan kritis: Minggu 4, 8, 10, 15<br>• Evaluasi akhir: Minggu 16 | **Mingguan** (konsultasi wajib)<br>**Sesuai kebutuhan** (isu mendesak) | • Konsultasi tatap muka (mingguan)<br>• WhatsApp (mendesak)<br>• Email (laporan formal) | **SANGAT TINGGI**<br>(10/10)<br>Penjaga gerbang akademik | • Umpan balik konsultasi<br>• Evaluasi kemajuan<br>• Persetujuan dokumen<br>• Rekomendasi teknis<br>• Nilai akhir | ✅ **AKTIF** |
| **E** | **PARTISIPAN PENGUJIAN KEGUNAAN** | | | | | | | | | | |
| 9 | Penguji UAT Tambahan | 5 | **Penguji tambahan:**<br>• 2 Terapis (dari klinik lain - tidak bias)<br>• 2 Profesional Admin/CS (dari industri lain)<br>• 1 Profesional kesehatan<br>• Direkrut untuk pengujian tidak bias | Penguji Independen<br>Penilai Kegunaan | • Evaluasi kegunaan objektif<br>• Penyelesaian kuesioner SUS<br>• Pengujian penyelesaian tugas<br>• Umpan balik & saran | • Pengujian (Minggu 9-10):<br>  - Sesi pengujian kegunaan 2 jam<br>  - Survei pasca-uji<br>  - Wawancara lanjutan (opsional) | **Sekali** (Minggu 9-10)<br>2-3 sesi | • Pengujian kegunaan langsung<br>• Survei daring<br>• Perekaman layar (dengan izin) | **SEDANG**<br>(5/10)<br>Memberikan evaluasi objektif | • Data penyelesaian tugas<br>• Skor SUS<br>• Umpan balik kualitatif<br>• Identifikasi titik kendala | ✅ **SELESAI** |

**Total Pemangku Kepentingan**: 26 individu di 9 kelompok pemangku kepentingan

**Ringkasan Pemangku Kepentingan Berdasarkan Kategori:**

| Kategori | Jumlah | Tingkat Keterlibatan | Kebutuhan Komunikasi |
|----------|-------|---------------------|---------------------|
| **Internal CUR-HEART** | 6 (1 pemilik + 3 terapis + 2 admin) | Sangat Tinggi - Pengguna harian | Pembaruan mingguan hingga harian |
| **Klien Eksternal** | 8 | Sedang - Pengujian berkala | Sesekali, fokus pengujian |
| **Tim Pengembang** | 3 | Sangat Tinggi - Tim inti | Kolaborasi harian |
| **Pembimbingan Akademik** | 1 | Sangat Tinggi - Pengawasan | Wajib mingguan |
| **Penguji UAT** | 5 | Sedang - Pengujian sekali | Keterlibatan sekali |
| **TOTAL** | **23** | | |

---

**[GAMBAR 3.4 - Stakeholder Map CUR-HEART]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT STAKEHOLDER MAP DIAGRAM]                         │
│                                                             │
│   Format: Lingkaran konsentris atau Matriks Kekuatan-Minat│
│                                                             │
│   PEMANGKU KEPENTINGAN INTI (Lingkaran Dalam):             │
│   ┌─────────────────────────────────────────┐             │
│   │  TIM PENGEMBANG (3 orang)               │             │
│   │  • Roki Anjas (Pemimpin/*Backend*)      │             │
│   │  • Susanto (*Frontend*/UI/UX)           │             │
│   │  • Fahruroji (*Full-stack*/DB)          │             │
│   │                                         │             │
│   │  DOSEN PEMBIMBING (1 orang)             │             │
│   │  • Rani Irma Handayani, M.Kom           │             │
│   └─────────────────────────────────────────┘             │
│                                                             │
│   PEMANGKU KEPENTINGAN PRIMER (Lingkaran Tengah):          │
│   ┌─────────────────────────────────────────┐             │
│   │  INTERNAL CUR-HEART (6 orang)           │             │
│   │  • Pemilik/Manajemen (1)                │             │
│   │  • Terapis Senior (3)                   │             │
│   │  • Admin/Staf (2)                       │             │
│   │                                         │             │
│   │  Tingkat Pengaruh: SANGAT TINGGI (8-10/10)│           │
│   │  Keterlibatan: Harian/Mingguan          │             │
│   └─────────────────────────────────────────┘             │
│                                                             │
│   PEMANGKU KEPENTINGAN SEKUNDER (Lingkaran Luar):          │
│   ┌─────────────────────────────────────────┐             │
│   │  PENGGUNA EKSTERNAL (13 orang)          │             │
│   │  • Sampel Klien (8)                     │             │
│   │  • Penguji UAT Tambahan (5)             │             │
│   │                                         │             │
│   │  Tingkat Pengaruh: SEDANG (5-6/10)      │             │
│   │  Keterlibatan: Berkala/Hanya Pengujian  │             │
│   └─────────────────────────────────────────┘             │
│                                                             │
│   ALTERNATIF MATRIKS KEKUATAN-MINAT:                       │
│                                                             │
│   KEKUATAN TINGGI, MINAT TINGGI (Kelola Erat):             │
│   • Pemilik/Manajemen                                      │
│   • Dosen Pembimbing                                       │
│   • Tim Pengembang                                         │
│                                                             │
│   KEKUATAN TINGGI, MINAT RENDAH (Jaga Kepuasan):           │
│   • (Tidak ada dalam proyek ini)                           │
│                                                             │
│   KEKUATAN RENDAH, MINAT TINGGI (Beri Informasi):          │
│   • Terapis Senior (3)                                     │
│   • Admin/Staf (2)                                         │
│                                                             │
│   KEKUATAN RENDAH, MINAT RENDAH (Pantau):                  │
│   • Sampel Klien (8)                                       │
│   • Penguji UAT (5)                                        │
│                                                             │
│   Total Pemangku Kepentingan: 23 individu                  │
│   Frekuensi Komunikasi: Harian hingga Sekali              │
│                                                             │
│   Format: Diagram PNG/JPG                                  │
│   Ukuran yang disarankan: 1200x1000px                      │
│   Gaya: Profesional dengan kode warna                      │
│                                                             │
│   File: assets/images/stakeholder-map-curheart.png         │
│   Alat: Draw.io, PowerPoint, atau Canva                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 3.4: Peta Pemangku Kepentingan (*Stakeholder Map*) CUR-HEART menunjukkan 23 pemangku kepentingan dalam 3 kategori (Inti, Primer, Sekunder) dengan tingkat pengaruh dan keterlibatan yang berbeda_

---

### 3.3.4 Kriteria Partisipan Pengujian Kegunaan

Untuk fase pengujian kegunaan (*usability testing*), partisipan direkrut dengan kriteria spesifik untuk memastikan perspektif beragam dan umpan balik komprehensif:

**Partisipan Terapis (5 orang total: 3 internal + 2 eksternal):**
- ✅ Berpengalaman dalam praktik terapi minimal 1 tahun
- ✅ Akrab dengan penggunaan komputer/*smartphone* (minimal tingkat menengah)
- ✅ Bersedia memberikan umpan balik jujur tanpa bias
- ✅ **Penguji eksternal**: Dari klinik terapi lain (untuk objektivitas)
- ✅ Tersedia untuk sesi pengujian kegunaan 2 jam

**Partisipan Klien (8 orang):**
- ✅ Pernah atau berencana menggunakan layanan terapi kesehatan mental
- ✅ Beragam dalam usia (25-45 tahun), jenis kelamin (5P, 3L), dan kemampuan teknologi (Rendah: 2, Sedang: 4, Tinggi: 2)
- ✅ Bersedia mengikuti sesi pengujian kegunaan (1-2 jam)
- ✅ Campuran antara klien yang ada (5) dan calon klien baru (3)
- ✅ Bersedia memberikan umpan balik jujur tentang pengalaman pemesanan

**Partisipan Admin (4 orang total: 2 internal + 2 eksternal):**
- ✅ Berpengalaman dalam tugas administratif atau layanan pelanggan (minimal 1 tahun)
- ✅ Akrab dengan sistem pemesanan atau manajemen janji temu
- ✅ Bersedia memberikan umpan balik untuk perbaikan
- ✅ **Penguji eksternal**: Admin/CS dari industri lain (*healthcare*, perhotelan) untuk perspektif tidak bias
- ✅ Tersedia untuk sesi pengujian 2 jam

**Profesional Kesehatan (1 orang):**
- ✅ Latar belakang di layanan kesehatan atau kesehatan mental
- ✅ Memahami privasi dan pertimbangan etika dalam sistem kesehatan
- ✅ Dapat memberikan perspektif profesional pada penanganan data dan manajemen pasien
- ✅ Bersedia untuk pengujian terfokus pada fitur kepatuhan dan privasi

**Total Partisipan Pengujian Kegunaan**: 18 orang (5 terapis + 8 klien + 4 admin + 1 profesional kesehatan)

## 3.4 Teknik Pengumpulan Data

Pengumpulan data dalam penelitian ini menggunakan metode ganda untuk memastikan pemahaman komprehensif dan validasi dari berbagai perspektif.

---

**[GAMBAR 3.5 - Teknik Pengumpulan Data Multi-Method]**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT DATA COLLECTION METHODS DIAGRAM]                 │
│                                                             │
│   Format: Piramida atau Matriks dengan 5 teknik            │
│                                                             │
│   ┌───────────────────────────────────────────┐            │
│   │  1. OBSERVASI (Minggu 1)                  │            │
│   │  📹 Partisipatif & Non-partisipatif       │            │
│   │  • Operasi CUR-HEART (5-7 hari)           │            │
│   │  • Dokumentasi alur kerja                 │            │
│   │  • Studi waktu & gerakan                  │            │
│   │  Output: Flowchart As-Is, Titik Masalah   │            │
│   │  Partisipan: 6 staf internal              │            │
│   └───────────────────────────────────────────┘            │
│                    ↓                                        │
│   ┌───────────────────────────────────────────┐            │
│   │  2. WAWANCARA (Minggu 1-2)                │            │
│   │  🎤 Semi-terstruktur                      │            │
│   │  • Pemilik (1) - 90 menit                 │            │
│   │  • Terapis (3) - 45 menit masing-masing   │            │
│   │  • Admin (2) - 45 menit masing-masing     │            │
│   │  • Sampel Klien (5) - 30 menit masing-masing│          │
│   │  Output: Transkrip Wawancara (50 hal)     │            │
│   │  Partisipan: 11 pemangku kepentingan      │            │
│   └───────────────────────────────────────────┘            │
│                    ↓                                        │
│   ┌───────────────────────────────────────────┐            │
│   │  3. STUDI PUSTAKA (Minggu 1-15)           │            │
│   │  📚 Tinjauan Literatur                    │            │
│   │  • Jurnal ilmiah (15)                     │            │
│   │  • Buku teks (5)                          │            │
│   │  • Dokumen *online* (10)                  │            │
│   │  • Tesis/*capstone* (5)                   │            │
│   │  • Artikel/blog (10)                      │            │
│   │  Output: BAB II Tinjauan Pustaka          │            │
│   │  Total Referensi: 45 sumber               │            │
│   └───────────────────────────────────────────┘            │
│                    ↓                                        │
│   ┌───────────────────────────────────────────┐            │
│   │  4. ANALISIS DOKUMEN (Minggu 1-2)         │            │
│   │  📄 Dokumen Internal & Eksternal          │            │
│   │  • SOP, formulir, laporan (20 dokumen)    │            │
│   │  • Data historis (3 bulan)                │            │
│   │  • Analisis kompetitor (5 situs)          │            │
│   │  • Dokumen regulasi (UU PDP)              │            │
│   │  Output: Aturan Bisnis (50+ aturan)       │            │
│   │  Total Dokumen: 30+                       │            │
│   └───────────────────────────────────────────┘            │
│                    ↓                                        │
│   ┌───────────────────────────────────────────┐            │
│   │  5. SURVEI/KUESIONER (Minggu 2 & 10)      │            │
│   │  📊 Survei *Online* (Google Forms)        │            │
│   │  • Pra-survei: 20 calon klien             │            │
│   │  • Pasca-UAT: 18 partisipan               │            │
│   │  • Kuesioner SUS (10 item)                │            │
│   │  Output: Skor SUS (78,5/100), Laporan     │            │
│   │  Total Respons: 38                        │            │
│   └───────────────────────────────────────────┘            │
│                                                             │
│   TRIANGULASI DATA:                                         │
│   ✅ Data Primer: Observasi, Wawancara, Survei (Kual+Kuan) │
│   ✅ Data Sekunder: Literatur, Dokumen (Riset Meja)        │
│   ✅ Multi-perspektif: 38 partisipan (pemangku kepentingan)│
│   ✅ Multi-metode: 5 teknik untuk validasi                 │
│                                                             │
│   Total Jam-Orang: ~120 jam                                │
│   Total Output: 25+ hasil                                  │
│                                                             │
│   Format: Infografis/Diagram PNG                           │
│   Ukuran yang disarankan: 1000x1400px                      │
│   Gaya: Infografis modern dengan ikon                      │
│                                                             │
│   File: assets/images/data-collection-multimethod.png      │
│   Alat: Canva, PowerPoint, atau Adobe Illustrator          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 3.5: Teknik pengumpulan data multi-metode menggunakan 5 pendekatan (Observasi, Wawancara, Studi Pustaka, Analisis Dokumen, Survei) dengan 38 partisipan dan 45 referensi untuk triangulasi data_

---

**Tabel 3.3 Teknik Pengumpulan Data**

| No | Teknik | Tujuan | Partisipan/Sumber | Tools/Instrumen | Durasi/Periode | Jenis Data | Prosedur Pelaksanaan | Output/Deliverables | Analisis Method | Kelebihan | Keterbatasan |
|----|--------|--------|------------------|----------------|---------------|-----------|-------------------|-------------------|----------------|----------|-------------|
| **1** | **Observasi Partisipatif & Non-Partisipatif** | • Memahami proses bisnis yang ada secara nyata<br>• Mengidentifikasi alur kerja aktual<br>• Menemukan titik kendala operasional<br>• Dokumentasi visual proses saat ini | • Pemilik (1)<br>• Terapis (3)<br>• Admin (2)<br>• Klien yang datang (5-8 observasi) | • Daftar periksa observasi<br>• Kamera/*smartphone* untuk foto<br>• Perekam suara (opsional)<br>• Buku catatan untuk catatan lapangan<br>• *Stopwatch* untuk pelacakan waktu | **5-7 hari**<br>Minggu 1 (16-22 Sep 2024)<br>• Hari 1-2: Proses pemesanan<br>• Hari 3-4: Alur kerja terapis<br>• Hari 5-6: Tugas admin<br>• Hari 7: Skenario pengecualian | **Kualitatif:**<br>• Alur kerja proses<br>• Pola perilaku<br>• Titik kendala<br>• Pengukuran waktu<br><br>**Kuantitatif:**<br>• Durasi tugas<br>• Frekuensi kesalahan<br>• Penggunaan alat | **Persiapan:**<br>1. Meminta izin formal dari pemilik<br>2. Menyiapkan daftar periksa observasi<br>3. Menginformasikan partisipan tentang tujuan<br><br>**Pelaksanaan:**<br>1. Mengamati proses pemesanan dari awal hingga akhir<br>2. Mengamati alur kerja terapis (persiapan - sesi - dokumentasi)<br>3. Mengamati tugas admin harian<br>4. Membuat catatan rinci dengan *timestamp*<br>5. Mengambil foto/*screenshot* (dengan izin)<br>6. Merekam waktu untuk setiap langkah<br><br>**Dokumentasi:**<br>1. Mengompilasi catatan observasi<br>2. Membuat *flowchart* *As-Is*<br>3. Mendaftar titik kendala & peluang | • Catatan Observasi (15-20 hal)<br>• *Flowchart* Proses *As-Is* (5 proses)<br>• Dokumentasi Foto (20-30 foto)<br>• Hasil Studi Waktu<br>• Daftar Titik Kendala (15-20 item)<br>• Matriks Peluang Perbaikan | **Analisis Tematik:**<br>• Pengodean observasi berdasarkan tema<br>• Identifikasi pola<br>• Pemetaan proses<br>• Analisis waktu & gerak<br>• Analisis kesenjangan (*As-Is* vs *To-Be*) | ✅ Memahami perilaku aktual (bukan hanya klaim)<br>✅ Menangkap bukti visual<br>✅ Mengidentifikasi pengetahuan tacit<br>✅ Melihat konteks & lingkungan<br>✅ Menemukan inefisiensi secara langsung | ❌ Memakan waktu<br>❌ Efek pengamat (perilaku bisa berubah karena diobservasi)<br>❌ Sampel terbatas (hanya hari yang diobservasi)<br>❌ Memerlukan izin akses |
| **2** | **Wawancara Semi-Terstruktur** | • Mendapatkan wawasan mendalam dari pemangku kepentingan<br>• Memahami kebutuhan, harapan, & titik kendala<br>• Validasi temuan dari observasi<br>• Mengumpulkan kebutuhan | • Pemilik (1 orang)<br>• Terapis (3 orang)<br>• Admin (2 orang)<br>• Klien Sampel (5 orang)<br><br>**Total: 11 wawancara** | • Panduan wawancara dengan pertanyaan yang disiapkan<br>• Perekam audio (dengan persetujuan)<br>• Laptop untuk pencatatan<br>• Formulir persetujuan<br>• Templat ringkasan wawancara | **10-12 hari**<br>Minggu 1-2 (16-29 Sep 2024)<br>• 30-60 menit per wawancara<br>• Pemilik: 90 menit (diskusi strategis mendalam)<br>• Terapis: 45 menit per orang<br>• Admin: 45 menit per orang<br>• Klien: 30 menit per orang | **Kualitatif:**<br>• Opini & preferensi<br>• Cerita pengguna<br>• Permintaan fitur<br>• Titik kendala & frustrasi<br>• Harapan<br>• Kriteria keberhasilan | **Persiapan:**<br>1. Mengembangkan panduan wawancara (5-10 pertanyaan per kelompok pemangku kepentingan)<br>2. Menjadwalkan wawancara<br>3. Menyiapkan alat perekam<br>4. Menyiapkan formulir persetujuan<br><br>**Pelaksanaan:**<br>1. Perkenalan & menjelaskan tujuan (5 menit)<br>2. Mendapat persetujuan lisan/tertulis untuk perekaman<br>3. Mengajukan pertanyaan yang disiapkan (20-40 menit)<br>4. Pertanyaan lanjutan pendalaman (10-15 menit)<br>5. Menutup & mengucapkan terima kasih ke partisipan (5 menit)<br><br>**Pasca-Wawancara:**<br>1. Menyalin rekaman (hari yang sama/hari berikutnya)<br>2. Menyorot kutipan kunci<br>3. Mengorganisir berdasarkan tema | • Transkrip Wawancara (11 berkas, 50-80 hal total)<br>• Ringkasan Wawancara per Kelompok Pemangku Kepentingan (5 hal)<br>• Laporan Temuan Kunci (10 hal)<br>• Daftar Kebutuhan (diekstrak dari wawancara)<br>• Koleksi Kutipan Penting | **Analisis Tematik:**<br>• Transkripsi<br>• Pengodean (*open coding* → *axial coding* → *selective coding*)<br>• Identifikasi tema<br>• Analisis pola lintas pemangku kepentingan<br>• Ekstraksi kebutuhan | ✅ Wawasan mendalam & pemahaman bernuansa<br>✅ Pertanyaan lanjutan untuk klarifikasi<br>✅ Membangun hubungan dengan pemangku kepentingan<br>✅ Menangkap emosi & motivasi<br>✅ Fleksibel - dapat menyesuaikan pertanyaan | ❌ Memakan waktu intensif (transkripsi)<br>❌ Ukuran sampel kecil<br>❌ Potensi bias pewawancara<br>❌ Sulit dikuantifikasi<br>❌ Tantangan penjadwalan |
| **3** | **Studi Pustaka (*Literature Review*)** | • Membangun landasan teoretis<br>• Memahami praktik terbaik di industri<br>• Tolok ukur dengan sistem serupa<br>• Membenarkan pilihan teknologi<br>• Mendukung dengan penelitian berbasis bukti | **Sumber:**<br>• 15 jurnal ilmiah (internasional & nasional)<br>• 5 buku teks<br>• 10 dokumentasi daring (Laravel, MySQL, Tailwind)<br>• 5 tesis/*capstone* serupa<br>• 10 posting blog/artikel<br><br>**Total: 45 referensi** | • Basis data akademik:<br>  - Google Scholar<br>  - IEEE Xplore<br>  - ResearchGate<br>  - ScienceDirect<br>• Sumber perpustakaan<br>• Mendeley (manajer referensi)<br>• Situs web dokumentasi resmi | **Berkelanjutan**<br>Minggu 1-15 (16 Sep - 29 Des 2024)<br>• Intensif: Minggu 1-3<br>• Pembaruan berkelanjutan sepanjang proyek<br>• Referensi akhir: Minggu 15 | **Kualitatif:**<br>• Teori & konsep<br>• Praktik terbaik<br>• Studi kasus<br>• Kerangka kerja & metodologi<br><br>**Kuantitatif:**<br>• Statistik tolok ukur<br>• Hasil survei dari makalah<br>• Metrik kinerja | **Pencarian:**<br>1. Mendefinisikan kata kunci (mis., "sistem informasi kesehatan mental", "sistem pemesanan daring", "keamanan Laravel")<br>2. Mencari pada basis data<br>3. Menyaring judul & abstrak<br>4. Menyaring berdasarkan relevansi, kebaruan (<5 tahun), kualitas<br><br>**Membaca:**<br>1. Membaca teks lengkap dari makalah terpilih<br>2. Menyorot poin kunci<br>3. Membuat catatan dalam Mendeley<br>4. Mengekstrak teori/temuan relevan<br><br>**Sintesis:**<br>1. Mengorganisir berdasarkan tema (struktur BAB II)<br>2. Membandingkan & membedakan perspektif<br>3. Mengidentifikasi kesenjangan<br>4. Mengintegrasikan ke tinjauan pustaka | • Bibliografi Beranotasi (45 entri)<br>• Tinjauan Pustaka (BAB II - 25-30 hal)<br>• Kerangka Teoretis<br>• Tabel Perbandingan (SDLC, kerangka kerja, basis data)<br>• Daftar Referensi (gaya IEEE)<br>• Analisis *state of the art* | **Analisis Konten:**<br>• Tinjauan sistematis<br>• Sintesis tematik<br>• Analisis komparatif<br>• Penilaian kritis<br>• Identifikasi kesenjangan<br>• Pengembangan kerangka kerja | ✅ Akses ke basis pengetahuan ekstensif<br>✅ Hemat biaya<br>✅ Dapat meninjau sesuai kecepatan sendiri<br>✅ Mengidentifikasi praktik terbaik yang terbukti<br>✅ Mendukung klaim dengan sitasi<br>✅ Cakupan komprehensif | ❌ Kelebihan informasi<br>❌ Mungkin tidak spesifik untuk konteks CUR-HEART<br>❌ Memakan waktu untuk membaca & mensintesis<br>❌ Beberapa jurnal berbayar<br>❌ Kualitas bervariasi |
| **4** | **Analisis Dokumen** | • Memahami aturan bisnis yang ada<br>• Mengekstrak kebutuhan data<br>• Memahami kebutuhan kepatuhan<br>• Intelijen kompetitif<br>• Pengumpulan data dasar | **Dokumen Internal:**<br>• SOP (5 dokumen)<br>• Formulir (10 jenis)<br>• Laporan keuangan (3 bulan)<br>• Data klien (sampel anonim 50)<br><br>**Eksternal:**<br>• Situs web kompetitor (5)<br>• Dokumen regulasi (UU PDP, Kode Etik)<br><br>**Total: 30+ dokumen** | • Surat permintaan dokumen<br>• *Spreadsheet* untuk ekstraksi data<br>• Daftar periksa analisis<br>• Templat analisis kompetitor<br>• Daftar periksa kepatuhan<br>• Pemindai untuk dokumen fisik | **7-10 hari**<br>Minggu 1-2 (16-29 Sep 2024)<br>• Minggu 1: Dokumen internal<br>• Minggu 2: Dokumen eksternal & kompetitor<br>• Berkelanjutan: Referensi ke dokumen selama pengembangan | **Kualitatif:**<br>• Aturan bisnis<br>• Deskripsi proses<br>• Persyaratan kepatuhan<br>• Fitur kompetitor<br><br>**Kuantitatif:**<br>• Data pemesanan historis<br>• Tren pendapatan<br>• Demografi klien<br>• Volume layanan | **Pengumpulan:**<br>1. Meminta formal dari pemilik untuk akses dokumen<br>2. Mengumpulkan dokumen fisik (pindai)<br>3. Mengumpulkan dokumen digital (salin)<br>4. Mengorganisir dalam folder terstruktur<br><br>**Analisis:**<br>1. Meninjau setiap dokumen secara menyeluruh<br>2. Mengekstrak info relevan:<br>   - Aturan bisnis<br>   - Elemen data<br>   - Langkah proses<br>   - Persyaratan kepatuhan<br>3. Membuat ringkasan<br>4. Memetakan ke kebutuhan sistem<br><br>**Analisis Kompetitor:**<br>1. Mengunjungi 5 situs web kompetitor<br>2. Mencoba proses pemesanan mereka (jika mungkin)<br>3. Mendokumentasikan fitur, UI, alur<br>4. Membandingkan kekuatan/kelemahan | • Ringkasan Analisis Dokumen (15 hal)<br>• Daftar Aturan Bisnis (50+ aturan)<br>• Kamus Data (awal - 40 entitas)<br>• Daftar Periksa Persyaratan Kepatuhan<br>• Matriks Analisis Kompetitif (5 kompetitor, 15 kriteria)<br>• Laporan Analisis Data Historis | **Analisis Konten:**<br>• Tinjauan dokumen<br>• Ekstraksi data<br>• Penambangan aturan bisnis<br>• Pemetaan kepatuhan<br>• Tolok ukur kompetitor<br>• Analisis tren (data historis) | ✅ Akses ke data bisnis aktual<br>✅ Memahami proses formal<br>✅ Persyaratan kepatuhan jelas<br>✅ Tren historis terlihat<br>✅ Tidak mengganggu (riset meja) | ❌ Dokumen mungkin usang<br>❌ Mungkin tidak mencerminkan praktik aktual (vs terdokumentasi)<br>❌ Dokumentasi tidak lengkap<br>❌ Kekhawatiran kerahasiaan<br>❌ Data kompetitor terbatas pada info publik |
| **5** | **Kuesioner/Survei (Daring)** | • Mengumpulkan data kuantitatif dari sampel lebih besar<br>• Memvalidasi temuan wawancara<br>• Mengukur kepuasan & kegunaan (SUS)<br>• Analisis statistik<br>• Evaluasi pasca-implementasi | **Pra-Implementasi:**<br>• 20 klien potensial (survei daring)<br><br>**Pasca-Implementasi (UAT):**<br>• 18 partisipan UAT:<br>  - 5 Terapis<br>  - 8 Klien<br>  - 4 Admin<br>  - 1 Profesional kesehatan<br><br>**Total: 38 respons** | • Google Forms<br>• Kuesioner SUS (10 item)<br>• Pertanyaan khusus (20-25 item)<br>• Skala Likert (1-5)<br>• Pilihan ganda<br>• Skala penilaian<br>• Pertanyaan terbuka (opsional) | **2 survei:**<br><br>**Survei 1 (Pra):**<br>Minggu 2 (23-29 Sep 2024)<br>• Desain: 2 hari<br>• Distribusi: 5 hari<br>• Pengumpulan respons: 7 hari<br><br>**Survei 2 (Pasca-UAT):**<br>Minggu 10 (18-24 Nov 2024)<br>• SUS + pertanyaan khusus<br>• Segera pasca-pengujian<br>• Waktu respons: 15-20 menit | **Kuantitatif:**<br>• Respons skala Likert (1-5)<br>• Skor SUS (0-100)<br>• Penilaian & peringkat<br>• Frekuensi & persentase<br><br>**Kualitatif:**<br>• Umpan balik terbuka<br>• Saran<br>• Komentar | **Desain:**<br>1. Mendefinisikan tujuan untuk survei<br>2. Mengembangkan pertanyaan selaras dengan tujuan<br>3. Uji coba dengan 3 orang<br>4. Merevisi berdasarkan umpan balik<br>5. Menyelesaikan kuesioner<br><br>**Distribusi:**<br>1. Membuat Google Form<br>2. Mengirim tautan via WhatsApp/email<br>3. Mengirim pengingat (jika respons rendah)<br><br>**Pengumpulan:**<br>1. Memantau respons harian<br>2. Menutup survei setelah tenggat<br>3. Mengunduh data (CSV/Excel)<br><br>**Analisis:**<br>1. Membersihkan data (menghapus yang tidak lengkap)<br>2. Menghitung skor SUS<br>3. Statistik deskriptif<br>4. Memvisualisasikan data (grafik) | **Survei 1 (Pra):**<br>• Hasil Survei Kebutuhan Klien (5 hal)<br>• Grafik & bagan<br>• 20 respons dari klien potensial<br><br>**Survei 2 (Pasca-UAT):**<br>• Hasil Skor SUS (18 partisipan)<br>• Laporan Evaluasi Kegunaan (10 hal)<br>• Tingkat Keberhasilan Tugas<br>• Penilaian Kepuasan<br>• Ringkasan Umpan Balik<br>• Prioritas rekomendasi | **Analisis Kuantitatif:**<br>• Statistik deskriptif (mean, median, SD)<br>• Kalkulasi skor SUS<br>• Distribusi frekuensi<br>• Tabulasi silang<br>• Visualisasi data (grafik, bagan)<br><br>**Kualitatif:**<br>• Pengodean tematik untuk respons terbuka | ✅ Ukuran sampel besar (dapat diskalakan)<br>✅ Hasil terukur<br>✅ Mudah dikelola (daring)<br>✅ Hemat biaya<br>✅ Terstandarisasi (SUS untuk perbandingan)<br>✅ Pengumpulan data cepat | ❌ Kedalaman terbatas (vs wawancara)<br>❌ Bias respons mungkin<br>❌ Tidak ada kesempatan klarifikasi<br>❌ Memerlukan akses internet<br>❌ Mungkin tingkat respons rendah<br>❌ Kata-kata pertanyaan mempengaruhi hasil |

**Ringkasan Pengumpulan Data:**

| Metrik | Total |
|--------|-------|
| **Total Partisipan Terlibat** | 38 individu unik (11 wawancara + 18 UAT + 20 survei pra) |
| **Total Jam-Orang (Pengumpulan Data)** | ~120 jam (observasi: 40j, wawancara: 15j, analisis dok: 30j, pustaka: 20j, survei: 15j) |
| **Total Dokumen Terkumpul** | 30+ dokumen internal & eksternal |
| **Total Referensi (Pustaka)** | 45 sumber (15 jurnal + 5 buku + 10 dok + 5 tesis + 10 artikel) |
| **Total Keluaran/Hasil** | 25+ dokumen (transkrip, laporan, ringkasan, dokumen analisis) |
| **Data Primer** | Observasi, wawancara, survei (38 partisipan) |
| **Data Sekunder** | Pustaka, dokumen, data historis |

---

### 3.4.1 Observasi

**Jenis Observasi:**
Observasi partisipatif dan non-partisipatif terhadap proses bisnis existing di CUR-HEART.

**Prosedur:**

1. **Persiapan:**
   - Menyiapkan observation checklist berdasarkan areas of interest
   - Meminta izin formal dari CUR-HEART untuk melakukan observasi
   - Menjelaskan tujuan observasi kepada staff yang akan diobservasi

2. **Pelaksanaan:**
   - Mengamati proses booking dari client inquiry hingga confirmation (1-2 hari)
   - Mengamati workflow terapis dari preparing session hingga documentation (1-2 hari)
   - Mengamati tugas administratif yang dilakukan staf (1-2 hari)
   - Membuat catatan rinci atau merekam (dengan izin)
   - Mengambil foto dari formulir, dokumen, atau ruang kerja (dengan izin)

3. **Dokumentasi:**
   - Mendokumentasikan observasi dalam catatan observasi
   - Membuat diagram alur proses berdasarkan alur kerja yang diamati
   - Mengidentifikasi titik masalah, ketidakefisienan, atau peluang perbaikan

**Aspek yang Diobservasi:**

- Langkah-langkah dalam proses pemesanan
- Alat dan media yang digunakan (WhatsApp, Excel, kalender manual)
- Waktu yang dibutuhkan untuk setiap langkah
- Pola komunikasi antara klien, admin, dan terapis
- Metode dokumentasi untuk catatan sesi
- Proses penyimpanan dan pengambilan data
- Penanganan kesalahan atau skenario pengecualian

**Output:**
- Catatan Observasi dengan *timestamps* dan detail
- Diagram Alur Proses (*As-Is*)
- Foto atau *screenshot* dari alat/formulir saat ini
- Daftar titik masalah dan peluang perbaikan

### 3.4.2 Wawancara (Interview)

**Jenis Wawancara:**
Wawancara semi-terstruktur yang mengombinasikan pertanyaan yang telah disiapkan dengan fleksibilitas untuk pertanyaan lanjutan berdasarkan respons.

**Prosedur:**

1. **Persiapan:**
   - Mengembangkan panduan wawancara dengan pertanyaan kunci untuk setiap kelompok pemangku kepentingan
   - Menjadwalkan wawancara dengan partisipan
   - Menyiapkan alat perekam (perekam audio atau aplikasi pencatat) dengan persetujuan partisipan

2. **Pelaksanaan:**
   - Melakukan wawancara satu-per-satu (30-60 menit per partisipan)
   - Memulai dengan perkenalan dan menjelaskan tujuan
   - Mengajukan pertanyaan yang telah disiapkan dan membiarkan partisipan menjelaskan lebih lanjut
   - Menindaklanjuti dengan pertanyaan penggalian untuk klarifikasi atau wawasan lebih dalam
   - Merekam wawancara atau membuat catatan rinci

3. **Dokumentasi:**
   - Mentranskripsikan rekaman wawancara
   - Mengorganisir respons berdasarkan tema atau topik
   - Mengidentifikasi pola umum, wawasan unik, atau pandangan yang bertentangan

**Interview Questions (Sample):**

**Untuk Owner/Manajemen:**
1. Apa visi Anda untuk digitalisasi CUR-HEART?
2. Apa KPI yang ingin Anda tingkatkan dengan sistem baru?
3. Apa tantangan terbesar yang dihadapi dalam operasional saat ini?
4. Apa ekspektasi Anda untuk sistem baru dalam hal ROI dan waktu?
5. Apa kekhawatiran atau kendala yang perlu kami pertimbangkan?

**Untuk Terapis:**
1. Bagaimana Anda saat ini mengelola jadwal Anda?
2. Apa titik masalah dalam proses pemesanan dan penjadwalan?
3. Bagaimana Anda mendokumentasikan catatan sesi? Apa tantangannya?
4. Informasi apa yang Anda butuhkan untuk mengelola klien secara efektif?
5. Fitur apa yang Anda harapkan dalam sistem baru?

**Untuk Admin/Staf:**
1. Bagaimana proses menangani pemesanan dari pertanyaan klien hingga konfirmasi?
2. Apa masalah umum atau keluhan dari klien?
3. Berapa lama waktu yang dibutuhkan untuk setiap tugas administratif?
4. Tugas apa yang paling memakan waktu dan berpotensi untuk diotomasi?
5. Informasi atau laporan apa yang sering diminta oleh manajemen?

**Untuk Sampel Klien:**
1. Bagaimana pengalaman Anda dalam memesan layanan terapi saat ini?
2. Apa yang Anda suka dan tidak suka dari proses saat ini?
3. Apa ekspektasi Anda untuk sistem pemesanan *online*?
4. Seberapa penting privasi dan keamanan data Anda?
5. Fitur apa yang akan membuat Anda lebih nyaman menggunakan layanan?

**Output:**
- Transkrip Wawancara
- Ringkasan Temuan Kunci untuk setiap kelompok pemangku kepentingan
- Kebutuhan yang Teridentifikasi dari masukan pemangku kepentingan
- Kutipan atau wawasan untuk mendukung temuan dalam laporan

### 3.4.3 Studi Pustaka (*Literature Review*)

**Sumber Pustaka:**

1. **Buku:**
   - Buku teks tentang Sistem Informasi, Manajemen Proyek, Desain Basis Data, Pengembangan *Web*
   - Buku pemrograman Laravel dan PHP
   - Buku desain UI/UX

2. **Jurnal Ilmiah:**
   - Jurnal internasional dan nasional tentang sistem informasi kesehatan
   - Jurnal tentang sistem pemesanan *online* dan penjadwalan janji temu
   - Jurnal tentang teknologi kesehatan mental dan terapi digital
   - Minimal 10-15 artikel jurnal (diterbitkan dalam 5 tahun terakhir)

3. **Dokumentasi Teknis:**
   - Dokumentasi Resmi Laravel
   - Dokumentasi MySQL
   - Dokumentasi Tailwind CSS
   - Praktik terbaik keamanan *web* (panduan OWASP)

4. **Tesis dan Laporan Penelitian:**
   - Tesis atau proyek *capstone* serupa dari universitas lain
   - Laporan industri tentang tren kesehatan digital

5. **Sumber *Online*:**
   - Postingan blog dan tutorial dari sumber terpercaya
   - Studi kasus dari implementasi yang berhasil
   - Data *benchmark* dari survei industri

**Prosedur:**

1. **Pencarian dan Pemilihan:**
   - Menggunakan basis data akademik (Google Scholar, IEEE Xplore, ResearchGate)
   - Mencari dengan kata kunci relevan
   - Menyaring artikel berdasarkan relevansi, kebaruan, dan kualitas
   - Memilih kumpulan referensi akhir

2. **Membaca dan Anotasi:**
   - Membaca materi terpilih dengan cermat
   - Menyorot poin kunci, teori, temuan
   - Membuat catatan atau ringkasan
   - Mengidentifikasi kesenjangan atau area untuk investigasi lebih lanjut

3. **Sintesis:**
   - Mengorganisir informasi berdasarkan tema atau topik
   - Membandingkan dan membedakan berbagai perspektif
   - Mengintegrasikan temuan ke dalam kerangka teoretis
   - Mengutip dengan benar sesuai dengan gaya sitasi (IEEE atau APA)

**Keluaran:**
- Bibliografi Beranotasi
- Bagian tinjauan pustaka dalam laporan (BAB II)
- Kerangka teoretis untuk penelitian
- Daftar referensi (Daftar Pustaka)

### 3.4.4 Analisis Dokumen

**Dokumen yang Dianalisis:**

1. **Dokumen Internal CUR-HEART:**
   - Prosedur Operasional Standar (*Standard Operating Procedures*/SOP)
   - Formulir pemesanan dan formulir penerimaan klien
   - Templat dokumentasi sesi
   - Laporan keuangan dan faktur
   - Perjanjian klien atau formulir persetujuan
   - Materi pemasaran (brosur, situs web)

2. **Data Historis:**
   - Data pemesanan (volume, tren, waktu puncak)
   - Demografi klien
   - Data pendapatan
   - Tingkat pemanfaatan terapis
   - Jenis layanan umum

3. **Analisis Kompetitor:**
   - Situs web dari layanan kesehatan mental kompetitor
   - Proses dan fitur pemesanan mereka
   - Model penetapan harga
   - Proposisi penjualan unik

4. **Dokumen Regulasi:**
   - UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi
   - Kode Etik Psikologi Indonesia
   - Pedoman perlindungan data kesehatan

**Prosedur:**

1. **Pengumpulan:**
   - Meminta dokumen relevan dari CUR-HEART
   - Mengunduh atau menyalin dokumen dengan izin yang tepat
   - Mengorganisir dokumen dalam sistem folder terstruktur

2. **Tinjauan dan Analisis:**
   - Membaca dokumen secara menyeluruh
   - Mengekstrak informasi relevan (aturan bisnis, elemen data, proses)
   - Mengidentifikasi persyaratan kepatuhan atau batasan
   - Mencatat praktik terbaik atau area untuk perbaikan

3. **Dokumentasi:**
   - Meringkas temuan dari setiap dokumen
   - Membuat model data berdasarkan formulir yang ada
   - Membuat daftar aturan bisnis untuk implementasi
   - Mendokumentasikan persyaratan kepatuhan untuk pertimbangan desain

**Keluaran:**
- Ringkasan Analisis Dokumen
- Daftar Aturan Bisnis
- Kamus Data (awal)
- Daftar Periksa Persyaratan Kepatuhan
- Matriks Analisis Kompetitif

### 3.4.5 Kuesioner/Survei (*Questionnaire/Survey*)

**Tujuan:**
Mengumpulkan data kuantitatif dari sampel yang lebih besar untuk melengkapi data kualitatif dari wawancara.

**Prosedur:**

1. **Desain Kuesioner:**
   - Mengembangkan pertanyaan yang selaras dengan tujuan penelitian
   - Campuran pertanyaan pilihan ganda, skala Likert, dan pertanyaan terbuka
   - Memastikan kejelasan dan menghindari pertanyaan mengarahkan
   - Melakukan uji coba kuesioner dengan kelompok kecil untuk validasi

2. **Distribusi:**
   - Mendistribusikan secara daring (Google Forms atau SurveyMonkey)
   - Mendistribusikan kepada klien CUR-HEART yang ada (melalui email atau WhatsApp)
   - Mendistribusikan kepada calon pengguna (media sosial, forum)
   - Menetapkan batas waktu respons (1-2 minggu)

3. **Pengumpulan Data:**
   - Memantau tingkat respons
   - Mengirim pengingat untuk meningkatkan partisipasi
   - Memastikan anonimitas untuk respons jujur

4. **Analisis Data:**
   - Mengekspor respons ke Excel atau SPSS
   - Melakukan statistik deskriptif (mean, median, frekuensi)
   - Membuat grafik dan bagan untuk visualisasi
   - Menganalisis korelasi atau pola

**Sample Questions:**

**Demografis:**
- Usia, jenis kelamin, pekerjaan, lokasi

**Pengalaman Saat Ini:**
- Apakah Anda pernah menggunakan layanan terapi kesehatan mental? (Ya/Tidak)
- Bagaimana Anda biasanya melakukan pemesanan? (Telepon/WhatsApp/Email/Datang langsung)
- Seberapa puas Anda dengan proses pemesanan saat ini? (Skala 1-5)

**Kebutuhan dan Preferensi:**
- Fitur apa yang penting untuk Anda dalam sistem pemesanan daring? (Pilihan ganda dengan peringkat)
- Seberapa penting privasi dan keamanan data Anda? (Skala 1-5)
- Metode pembayaran apa yang Anda pilih? (Pilihan ganda)

**Adopsi Teknologi:**
- Seberapa nyaman Anda menggunakan teknologi? (Skala 1-5)
- Apakah Anda lebih memilih mengakses dari ponsel atau desktop? (Pilihan ganda)

**Keluaran:**
- Laporan Hasil Survei dengan statistik dan visualisasi
- *User Personas* berdasarkan demografis dan pola perilaku
- Daftar fitur yang diprioritaskan berdasarkan preferensi pengguna

### 3.4.6 Pengujian Kegunaan (*Usability Testing*)

**Tujuan:**
Mengevaluasi antarmuka pengguna dan pengalaman pengguna dengan mengamati pengguna nyata saat mereka berinteraksi dengan sistem.

**Prosedur:**

1. **Perencanaan:**
   - Mendefinisikan tujuan pengujian kegunaan
   - Membuat skenario uji dan tugas untuk partisipan
   - Menyiapkan lingkungan pengujian (laptop dengan sistem terinstal)
   - Merekrut partisipan (10-15 orang mewakili peran pengguna berbeda)

2. **Pelaksanaan Uji:**
   - **Pengenalan (5 menit):**
     - Menjelaskan tujuan uji
     - Menekankan bahwa yang diuji adalah sistem, bukan partisipan
     - Mendapatkan persetujuan untuk observasi dan perekaman
   
   - **Kuesioner Pra-Uji (5 menit):**
     - Mengumpulkan informasi demografis dan latar belakang
     - Menilai kemampuan teknologi saat ini
   
   - **Pelaksanaan Tugas (30-45 menit):**
     - Memberikan tugas spesifik kepada partisipan untuk diselesaikan:
       - **Untuk Klien:** "Pesan sesi terapi stres dengan terapis pilihan Anda untuk minggu depan"
       - **Untuk Terapis:** "Atur ketersediaan Anda untuk bulan depan dan blokir tanggal untuk liburan Anda"
       - **Untuk Admin:** "Temukan semua pemesanan yang menunggu dan setujui mereka"
     - Mendorong partisipan untuk berpikir keras (mengungkapkan pikiran)
     - Mengamati dan mencatat:
       - Waktu untuk menyelesaikan tugas
       - Jumlah kesalahan atau klik yang salah
       - Area kebingungan atau keragu-raguan
       - Ekspresi wajah atau bahasa tubuh (frustrasi, kepuasan)
     - Merekam layar (dengan alat seperti OBS Studio) untuk analisis nanti
   
   - **Kuesioner Pasca-Uji (10 menit):**
     - *System Usability Scale* (SUS) - survei standar 10 pertanyaan
     - Penilaian kepuasan untuk fitur spesifik
     - Pertanyaan terbuka tentang hal yang disukai, tidak disukai, saran
   
   - **Wawancara Penutup (10 menit):**
     - Mendiskusikan observasi dengan partisipan
     - Meminta klarifikasi pada perilaku yang diamati
     - Mengumpulkan umpan balik atau saran tambahan

3. **Analisis Data:**
   - **Analisis Kuantitatif:**
     - Menghitung tingkat keberhasilan tugas (%)
     - Menghitung rata-rata waktu untuk menyelesaikan tugas
     - Menghitung tingkat kesalahan
     - Menghitung skor SUS (rata-rata di seluruh partisipan)
   
   - **Analisis Kualitatif:**
     - Meninjau catatan observasi dan rekaman
     - Mengidentifikasi masalah kegunaan umum
     - Mengkategorikan masalah berdasarkan tingkat keparahan (kritis, mayor, minor)
     - Mengidentifikasi pola dalam perilaku pengguna
   
   - **Sintesis:**
     - Memprioritaskan masalah kegunaan untuk diperbaiki
     - Membuat rekomendasi untuk perbaikan
     - Mendokumentasikan wawasan untuk iterasi desain

**Metrik yang Dikumpulkan:**

- **Tingkat Keberhasilan Tugas:** Persentase partisipan yang berhasil menyelesaikan tugas
- **Waktu pada Tugas:** Rata-rata waktu yang dibutuhkan untuk menyelesaikan setiap tugas
- **Tingkat Kesalahan:** Jumlah kesalahan yang dibuat per tugas
- **Skor Kepuasan:** Skor SUS (skala 0-100)
- ***Net Promoter Score* (NPS):** Kemungkinan untuk merekomendasikan sistem kepada orang lain (skala 0-10)

**Keluaran:**
- Laporan Pengujian Kegunaan dengan:
  - Ringkasan Eksekutif
  - Metodologi
  - Demografis Partisipan
  - Skenario Tugas dan Hasil
  - Metrik Kuantitatif (tingkat keberhasilan, waktu, skor SUS)
  - Temuan Kualitatif (observasi, kutipan)
  - Daftar Masalah Kegunaan dengan peringkat keparahan
  - Rekomendasi untuk Perbaikan
  - *Screenshot* atau video yang menggambarkan masalah

**Alat yang Digunakan:**
- OBS Studio untuk perekaman layar
- *Stopwatch* atau *timer* untuk mengukur waktu pada tugas
- Google Forms untuk kuesioner
- *Spreadsheet* untuk kompilasi data dan analisis
- Perangkat lunak pengeditan video untuk membuat sorotan

---

**Tabel 3.5 Dokumentasi dan Deliverables per Fase SDLC**

| No | Fase | Nama Dokumen/Hasil | Tujuan Dokumen | Format | Jumlah Halaman | Penulis/PIC | Peninjau/Penyetuju | Target Penyelesaian | Penyelesaian Aktual | Status | Versi | Audiens/Pengguna |
|----|------|-------------------------|---------------|---------|---------------|-----------|------------------|---------------------|-------------------|--------|---------|---------------|
| **FASE 1: ANALISIS KEBUTUHAN** | | | | | | | | | | | | |
| 1.1 | Analisis | Spesifikasi Kebutuhan Perangkat Lunak (SRS) | Dokumen komprehensif yang berisi kebutuhan fungsional & non-fungsional, kasus penggunaan, kendala, kriteria kesuksesan | Microsoft Word (.docx) → PDF | 30 hal | Roki Anjas (Pemimpin) | • Rani Irma Handayani (Pembimbing)<br>• Pemilik CUR-HEART (Pemangku Kepentingan) | 29 Sep 2024 | 29 Sep 2024 | ✅ **DISETUJUI** | v2.1 (Final) | • Tim Pengembang<br>• Pemangku Kepentingan<br>• Evaluator Akademik |
| 1.2 | Analisis | Laporan Studi Kelayakan | Analisis kelayakan proyek dari aspek teknis, ekonomi, dan operasional dengan rekomendasi | Microsoft Word (.docx) → PDF | 10 hal | Fahruroji | Rani Irma Handayani | 27 Sep 2024 | 27 Sep 2024 | ✅ **DISETUJUI** | v1.0 | • Pemilik CUR-HEART<br>• Evaluator Akademik |
| 1.3 | Analisis | Diagram Alur Proses Bisnis (*As-Is* & *To-Be*) | Visualisasi proses bisnis yang ada vs yang diusulkan untuk identifikasi perbaikan | Visio/Draw.io → PDF | 8 hal (5 proses × *As-Is* & *To-Be*) | Roki Anjas | • Pemilik CUR-HEART<br>• Rani Irma Handayani | 26 Sep 2024 | 26 Sep 2024 | ✅ **SELESAI** | v1.0 | • Pemangku Kepentingan<br>• Tim Pengembang<br>• Laporan BAB I & III |
| 1.4 | Analisis | Transkrip Wawancara | Transkrip *verbatim* dari 11 wawancara untuk referensi dan jejak audit | Microsoft Word (.docx) | 50 hal (11 file, 3-6 hal masing-masing) | Semua Tim (transkripsi) | Tidak diperlukan (data mentah) | 25 Sep 2024 | 25 Sep 2024 | ✅ **SELESAI** | v1.0 | • Arsip Penelitian<br>• Lampiran Laporan |
| 1.5 | Analisis | Ringkasan Wawancara & Temuan Kunci | Ringkasan eksekutif dari temuan dengan tema, pola, dan kebutuhan yang diekstrak | Microsoft Word (.docx) → PDF | 10 hal | Roki Anjas (sintesis) | Rani Irma Handayani | 28 Sep 2024 | 28 Sep 2024 | ✅ **SELESAI** | v1.0 | • Tim Pengembang<br>• Laporan BAB III & IV |
| 1.6 | Analisis | Catatan Observasi | Catatan lapangan rinci dari 5-7 hari observasi dengan *timestamps*, titik masalah, peluang | Microsoft Word (.docx) | 15 hal | Semua Tim (pengamat bergantian) | Tidak diperlukan (data mentah) | 22 Sep 2024 | 22 Sep 2024 | ✅ **SELESAI** | v1.0 | • Arsip Penelitian<br>• Laporan BAB III |
| 1.7 | Analisis | Dokumentasi Foto | Bukti visual dari proses saat ini, formulir, ruang kerja, alat | JPEG/PNG (diorganisir dalam folder) | ~30 foto | Susanto (fotografi) | Tidak diperlukan | 22 Sep 2024 | 22 Sep 2024 | ✅ **SELESAI** | N/A | • Laporan (inklusi selektif)<br>• Slide presentasi |
| **FASE 2: DESAIN SISTEM** | | | | | | | | | | | | |
| 2.1 | Desain | Dokumen Desain Sistem (SDD) | Arsitektur sistem, *tech stack*, arsitektur penyebaran, desain keamanan | Microsoft Word (.docx) → PDF | 40 hal | Roki Anjas (Arsitek) | Rani Irma Handayani | 13 Okt 2024 | 13 Okt 2024 | ✅ **DISETUJUI** | v1.0 | • Tim Pengembang<br>• Laporan BAB IV<br>• Evaluator Akademik |
| 2.2 | Desain | Dokumen Desain Basis Data (ERD & Skema) | ERD (16 entitas), skema basis data, kamus data, dokumentasi normalisasi, strategi indeks | MySQL Workbench → PDF<br>+ Microsoft Word (dokumentasi) | 25 hal | Fahruroji (Arsitek DB) | • Roki Anjas (tinjauan)<br>• Rani Irma Handayani | 10 Okt 2024 | 10 Okt 2024 | ✅ **DISETUJUI** | v2.0 (setelah revisi tinjauan) | • Tim Pengembang (referensi implementasi)<br>• Laporan BAB IV |
| 2.3 | Desain | Dokumen Desain UI/UX | Persona pengguna (3), *wireframes* (15), *mockups* fidelitas tinggi (41), sistem desain, alur pengguna (10) | Figma (interaktif) + Ekspor PDF | 50 hal (diekspor) | Susanto (Desainer UI/UX) | • 5 pengguna sampel (sesi umpan balik)<br>• Roki Anjas<br>• Rani Irma Handayani | 12 Okt 2024 | 12 Okt 2024 | ✅ **DISETUJUI** | v3.0 (setelah iterasi umpan balik pengguna) | • Tim Pengembang (referensi *frontend*)<br>• Pemangku Kepentingan<br>• Laporan BAB IV |
| 2.4 | Desain | Set Diagram UML | Diagram kasus penggunaan (25 kasus), diagram aktivitas (5), diagram sekuens (10), diagram kelas (opsional) | Visual Paradigm/Draw.io → PDF | 18 hal | Roki Anjas | Rani Irma Handayani | 11 Okt 2024 | 11 Okt 2024 | ✅ **SELESAI** | v1.0 | • Tim Pengembang<br>• Laporan BAB IV<br>• Evaluator Akademik |
| 2.5 | Desain | Dokumen Desain Keamanan | Strategi autentikasi/otorisasi, enkripsi, mitigasi OWASP Top 10, *logging* audit | Microsoft Word (.docx) → PDF | 12 hal | Roki Anjas | Rani Irma Handayani | 13 Okt 2024 | 13 Okt 2024 | ✅ **SELESAI** | v1.0 | • Tim Pengembang<br>• Referensi Pengujian Keamanan |
| **FASE 3: IMPLEMENTASI** | | | | | | | | | | | | |
| 3.1 | Implementasi | Kode Sumber (Repositori GitHub) | Kode aplikasi Laravel lengkap (*models*, *controllers*, *views*, migrasi, *seeders*, konfigurasi, tes) | PHP, Blade, JavaScript, CSS (repo Git) | ~15.000 baris kode<br>150+ *commits* | Semua Tim (kolaboratif) | • Tinjauan rekan (*via* GitHub PR)<br>• Rani (pemeriksaan spot) | 10 Nov 2024 | 10 Nov 2024 | ✅ **SELESAI** | v1.0.0 (*release tag*) | • Tim Pengembang<br>• Pemelihara masa depan<br>• Evaluator kode |
| 3.2 | Implementasi | Migrasi & *Seeders* Basis Data | File migrasi Laravel (16 tabel) dan file *seeder* untuk data sampel/awal | PHP (migrasi Laravel) | 2.500 baris kode | Fahruroji (Pemimpin DB)<br>+ Roki (tabel auth) | Tinjauan kode (tim) | 5 Nov 2024 | 5 Nov 2024 | ✅ **SELESAI** | N/A (bagian dari *codebase*) | • Pengembangan & Pengujian<br>• Penyebaran |
| 3.3 | Implementasi | Panduan Instalasi & Penyiapan | Panduan langkah-demi-langkah untuk penyiapan pengembangan lokal (persyaratan, instalasi, konfigurasi) | Markdown (README.md) | 5 hal (*rendered*) | Roki Anjas | Tidak diperlukan (dokumen hidup) | 20 Okt 2024 | 20 Okt 2024 | ✅ **SELESAI** | v1.2 (diperbarui sesuai kebutuhan) | • Pengembang baru<br>• Tim penyebaran<br>• Evaluator akademik |
| 3.4 | Implementasi | Dokumentasi Integrasi API | Integrasi *payment gateway* Midtrans (kunci API, *endpoints*, *webhooks*, pengujian), konfigurasi SMTP email | Markdown + Microsoft Word → PDF | 8 hal | Roki Anjas | Tidak diperlukan (dokumen teknis) | 8 Nov 2024 | 8 Nov 2024 | ✅ **SELESAI** | v1.0 | • Tim Pengembang<br>• Penyebaran<br>• Pemecahan masalah |
| **FASE 4: PENGUJIAN** | | | | | | | | | | | | |
| 4.1 | Pengujian | Rencana Uji | Strategi pengujian, kasus uji (150+), peran & tanggung jawab, jadwal pengujian, penyiapan lingkungan uji | Microsoft Word (.docx) → PDF | 20 hal | Roki Anjas (Pemimpin QA) | Rani Irma Handayani | 11 Nov 2024 | 11 Nov 2024 | ✅ **DISETUJUI** | v1.0 | • Tim Pengujian<br>• Pemangku Kepentingan<br>• Evaluator Akademik |
| 4.2 | Pengujian | Kode Uji Unit (PHPUnit) | Uji unit otomatis untuk logika bisnis kritis | PHP (kelas uji PHPUnit) | ~1.200 baris kode uji<br>30 kasus uji | Semua Tim (masing-masing menguji kode sendiri) | Tinjauan kode (tim) | 15 Nov 2024 | 15 Nov 2024 | ✅ **SELESAI** | N/A (bagian dari *codebase*) | • CI/CD (masa depan)<br>• Pencegahan regresi |
| 4.3 | Pengujian | Laporan Hasil Uji Fungsional | Log eksekusi uji (150+ kasus uji), status lulus/gagal, laporan bug (25 bug: 2 kritis, 8 mayor, 15 minor), log perbaikan bug | Microsoft Excel (.xlsx) + Word → PDF | 15 hal | Susanto (Koordinator Uji) | Roki Anjas | 20 Nov 2024 | 20 Nov 2024 | ✅ **SELESAI** | v1.0 | • Tim Pengembang (perbaikan bug)<br>• Laporan BAB IV<br>• Referensi UAT |
| 4.4 | Pengujian | Laporan Hasil Uji Kegunaan | Skor SUS (18 partisipan, rata-rata 78,5/100), tingkat keberhasilan tugas (92%), waktu per tugas, umpan balik kualitatif, rekomendasi | Microsoft Word (.docx) → PDF | 18 hal | Susanto (Pemimpin Kegunaan) | Rani Irma Handayani | 22 Nov 2024 | 22 Nov 2024 | ✅ **SELESAI** | v1.0 | • Perbaikan UI/UX<br>• Laporan BAB IV & V<br>• Evaluator Akademik |
| 4.5 | Pengujian | Dokumen Persetujuan UAT | Hasil uji UAT (90% kebutuhan terpenuhi: 36/40), umpan balik pemangku kepentingan, tanda tangan persetujuan resmi, daftar fitur yang ditunda | Microsoft Word (.docx) → PDF | 8 hal | Roki Anjas | • Pemilik CUR-HEART (persetujuan)<br>• Rani Irma Handayani | 24 Nov 2024 | 24 Nov 2024 | ✅ **DISETUJUI & DITANDATANGANI** | v1.0 (mengikat secara hukum) | • Otorisasi peluncuran<br>• Laporan BAB IV<br>• Bukti penerimaan akademik |
| 4.6 | Pengujian | Hasil Uji Kinerja | Waktu muat halaman (rata-rata 1,8 detik), kapasitas pengguna bersamaan (50 pengguna), analisis kueri basis data, rekomendasi optimasi | Microsoft Excel + Word → PDF | 10 hal | Fahruroji (Fokus kinerja) | Roki Anjas | 21 Nov 2024 | 21 Nov 2024 | ✅ **SELESAI** | v1.0 | • Penyebaran (ukuran server)<br>• Prioritas optimasi<br>• Laporan BAB IV |
| 4.7 | Pengujian | Laporan Audit Keamanan | Daftar periksa OWASP Top 10 (semua dimitigasi), hasil uji penetrasi (tidak ada kerentanan kritis), rekomendasi keamanan | Microsoft Word (.docx) → PDF | 12 hal | Roki Anjas (Keamanan) | Rani Irma Handayani | 23 Nov 2024 | 23 Nov 2024 | ✅ **SELESAI** | v1.0 | • Penyebaran produksi (penilaian risiko)<br>• Laporan BAB IV<br>• Dokumentasi kepatuhan |
| **FASE 5: PENYEBARAN** | | | | | | | | | | | | |
| 5.1 | Penyebaran | Daftar Periksa Penyebaran | Tugas pra-penyebaran, langkah penyebaran, verifikasi pasca-penyebaran, prosedur *rollback* | Microsoft Excel (.xlsx) + Word → PDF | 6 hal | Roki Anjas (DevOps) | Fahruroji (tinjauan migrasi DB) | 25 Nov 2024 | 25 Nov 2024 | ✅ **SELESAI** | v1.0 | • Eksekusi Penyebaran<br>• Penyebaran masa depan (pembaruan) |
| 5.2 | Penyebaran | Manual Pengguna (Klien, Terapis, Admin) | Panduan komprehensif untuk pengguna akhir: memulai, panduan fitur, FAQ, pemecahan masalah | Microsoft Word (.docx) → PDF<br>(3 manual terpisah) | 20 hal (total) | Susanto (Penulisan Teknis) | • 3 pengguna sampel (tinjauan kejelasan)<br>• Rani Irma Handayani | 30 Nov 2024 | 30 Nov 2024 | ✅ **SELESAI** | v1.0 | • Pengguna Akhir (pelatihan & penggunaan harian)<br>• Referensi Dukungan |
| 5.3 | Penyebaran | Manual Admin (Administrasi Sistem) | Panduan teknis untuk admin: manajemen pengguna, pengaturan sistem, *backup*, pemecahan masalah | Microsoft Word (.docx) → PDF | 15 hal | Roki Anjas | Fahruroji (tinjauan) | 30 Nov 2024 | 30 Nov 2024 | ✅ **SELESAI** | v1.0 | • Admin CUR-HEART<br>• Staf Dukungan IT |
| 5.4 | Penyebaran | Materi Pelatihan (Slide + Video) | Slide presentasi pelatihan (30 slide) + tutorial video (5 video, 20 menit total) + panduan referensi cepat | PowerPoint → PDF<br>+ Video MP4<br>+ *cheat sheets* PDF | 30 slide + 20 menit video | Susanto (Pemimpin Pelatihan) | Tidak diperlukan (materi pelatihan) | 28 Nov 2024 | 28 Nov 2024 | ✅ **SELESAI** | v1.0 | • Sesi Pelatihan<br>• Pembelajaran mandiri<br>• *Onboarding* masa depan |
| 5.5 | Penyebaran | Dokumen Serah Terima | Tinjauan sistem, kredensial (aman), kontak dukungan, rekomendasi pemeliharaan, peta jalan Fase 2 | Microsoft Word (.docx) → PDF | 10 hal | Roki Anjas | Pemilik CUR-HEART (pengakuan) | 1 Des 2024 | 1 Des 2024 | ✅ **DITANDATANGANI & DISERAHKAN** | v1.0 | • Kepemilikan CUR-HEART<br>• Bukti serah terima hukum |
| **FASE 6: PEMELIHARAAN & EVALUASI** | | | | | | | | | | | | |
| 6.1 | Pemeliharaan | Log Perbaikan Bug (Pasca-Peluncuran) | Pelacakan bug pasca-peluncuran, prioritas, status perbaikan, catatan rilis untuk *patch* | Microsoft Excel (.xlsx) (dokumen hidup) | Berkelanjutan (10 bug di Bulan 1) | Roki Anjas (Triase Bug) | Tidak diperlukan (log operasional) | Berkelanjutan | Berkelanjutan | ⏳ **AKTIF** | v1.x (inkremental) | • Tim Pengembang<br>• Admin CUR-HEART (pembaruan status) |
| 6.2 | Pemeliharaan | Log Tiket Dukungan | Pertanyaan dukungan pengguna, masalah, resolusi, waktu respons | Google Sheets (dibagikan) | Berkelanjutan (20 tiket Bulan 1) | Susanto (Koordinator Dukungan) | Tidak diperlukan (log operasional) | Berkelanjutan | Berkelanjutan | ⏳ **AKTIF** | v1.x | • Tim Dukungan<br>• Pemantauan SLA |
| 6.3 | Pemeliharaan | Laporan Pemantauan Kinerja | Laporan *uptime* mingguan/bulanan, waktu muat halaman, analitik lalu lintas, insiden | Google Analytics + UptimeRobot → PDF (bulanan) | 5 hal (per bulan) | Fahruroji (Pemantauan) | Roki Anjas (tinjauan) | Bulanan | 31 Des 2024 (Bulan 1) | ⏳ **DALAM PROSES** | v1.0 (Bulan 1) | • Pemilik CUR-HEART (KPI bisnis)<br>• Laporan BAB V (evaluasi) |
| 6.4 | Pemeliharaan | Survei Umpan Balik Pengguna (Pasca-Peluncuran) | Survei 1 bulan pasca-peluncuran: kepuasan, masalah, permintaan fitur (15 respons, 8,5/10 kepuasan) | Google Forms → PDF | 8 hal | Susanto (Desain Survei) | Tidak diperlukan | 31 Des 2024 | 31 Des 2024 | ⏳ **DIRENCANAKAN** | v1.0 | • Prioritas Perbaikan<br>• Laporan BAB V |
| **DOKUMENTASI AKADEMIK (PASCA-PENGEMBANGAN)** | | | | | | | | | | | | |
| 7.1 | Laporan | Laporan Akhir Proyek *Capstone* | Laporan akademik komprehensif: BAB I-V, tinjauan pustaka, metodologi, hasil, analisis, kesimpulan, rekomendasi | Microsoft Word (.docx) → PDF | 80-100 hal | Semua Tim (kolaboratif)<br>Roki (Penulis Utama) | Rani Irma Handayani (Pembimbing Akademik) | 22 Des 2024 | 20 Des 2024 | ⏳ **DALAM PROSES** (85% selesai) | v0.9 (*draft*) | • Pengajuan Akademik<br>• Persyaratan Kelulusan<br>• Arsip Universitas |
| 7.2 | Laporan | Slide Presentasi Final | Presentasi pertahanan: tinjauan proyek, masalah, solusi, metodologi, hasil, demo, persiapan *Q&A* | PowerPoint (.pptx) → PDF | 40-50 slide | Semua Tim (kolaboratif) | Rani Irma Handayani (tinjauan) | 29 Des 2024 | Belum dimulai | 🔜 **AKAN DATANG** | v0.1 | • Pertahanan Final<br>• Evaluator Akademik<br>• Audiens Publik |
| 7.3 | Laporan | Poster/Infografis (Opsional) | Ringkasan visual proyek untuk pameran akademik atau kompetisi | Adobe Illustrator/Canva → PDF | 1 halaman (ukuran A1) | Susanto (Desain) | Tidak diperlukan | 5 Jan 2025 | Belum dimulai | 🔜 **OPSIONAL** | v1.0 | • Pameran Akademik<br>• Portofolio |

**Ringkasan Total Hasil:**

| Kategori | Jumlah | Total Halaman (estimasi) | Status |
|----------|-------|------------------------|--------|
| **Analisis Kebutuhan** | 7 dokumen | 123 halaman | ✅ 100% Selesai |
| **Desain Sistem** | 5 dokumen | 145 halaman | ✅ 100% Selesai |
| **Implementasi Kode & Dokumentasi** | 4 dokumen | ~15.000 LOC + 13 halaman | ✅ 100% Selesai |
| **Pengujian & QA** | 7 dokumen | 83 halaman | ✅ 100% Selesai |
| **Penyebaran & Serah Terima** | 5 dokumen | 51 halaman | ✅ 100% Selesai |
| **Pemeliharaan (Berkelanjutan)** | 4 dokumen | Log berkelanjutan | ⏳ Aktif |
| **Dokumentasi Akademik** | 3 dokumen | 80-100 halaman | ⏳ 85% Selesai |
| **TOTAL KESELURUHAN** | **35 hasil** | **415+ halaman + 15K LOC** | **90% Selesai** |

---

**Tabel 3.6 Metode Pengujian dan Evaluasi Sistem**

| No | Jenis Pengujian | Tujuan | Cakupan | Teknik/Metode | Alat/*Framework* | Jumlah Kasus Uji | Kriteria Kelulusan | Partisipan/Penguji | Durasi Eksekusi | Ringkasan Hasil | Status |
|----|----------------|--------|---------------|---------------|----------------|-----------------|-------------|-------------------|----------------|----------------|--------|
| **1** | **Pengujian Unit** (*Unit Testing*) | • Menguji fungsi/metode individual secara terisolasi<br>• Memastikan kebenaran logika bisnis<br>• Memungkinkan pengujian regresi<br>• Jaminan kualitas kode | **Modul yang Diuji:**<br>• Kalkulasi ketersediaan pemesanan<br>• Kalkulasi jumlah pembayaran<br>• Logika autentikasi pengguna<br>• Logika penjadwalan sesi<br>• Kondisi pemicu notifikasi<br>• Fungsi validasi data<br><br>**Target Cakupan:** 70% cakupan kode pada modul inti | **Prinsip *Test-Driven Development* (TDD):**<br>• Pola *Arrange-Act-Assert* (AAA)<br>• *Mock* dependensi eksternal (*payment gateway*, email)<br>• Pengujian terisolasi (tanpa panggilan DB → SQLite *in-memory*)<br>• Eksekusi pengujian otomatis<br><br>**Jenis Asersi:**<br>• assertEquals()<br>• assertTrue()<br>• assertDatabaseHas()<br>• assertRedirect()<br>• assertStatus() | **PHPUnit** (bawaan Laravel)<br>• Utilitas Pengujian Laravel (*factories*, *seeders*)<br>• Mockery (*mocking*)<br>• Faker (generasi data uji) | **30 Kasus Uji:**<br>• Autentikasi: 5 uji<br>• Logika pemesanan: 8 uji<br>• Kalkulasi pembayaran: 4 uji<br>• Pengecekan ketersediaan: 6 uji<br>• Pemicu notifikasi: 3 uji<br>• Validasi: 4 uji | ✅ **Tingkat Kelulusan 100%**<br>• Semua 30 uji lulus<br>• Cakupan kode: 72% (melampaui target 70%)<br>• Waktu eksekusi: <5 detik | **Pengembang (Uji Mandiri):**<br>• Roki Anjas: 12 uji (logika *backend*)<br>• Fahruroji: 10 uji (operasi DB)<br>• Susanto: 8 uji (*controller frontend*) | **Berkelanjutan (Selama Pengembangan)**<br>Minggu 5-8<br>• Tulis uji → Tulis kode → Jalankan uji<br>• Jalankan otomatis saat komit Git (*pre-commit hook*) | ✅ **LULUS**<br>• 30/30 uji lulus<br>• Cakupan kode 72%<br>• Nol uji gagal<br>• Pencegahan regresi diaktifkan | ✅ **SELESAI**<br>(15 Nov 2024) |
| **2** | **Pengujian Integrasi** (*Integration Testing*) | • Menguji interaksi antar modul/komponen<br>• Memvalidasi aliran data lintas sistem<br>• Memastikan integrasi eksternal berfungsi<br>• Menguji *endpoint* API | **Titik Integrasi:**<br>• *Controller* ↔ *Model* ↔ Basis Data<br>• *Controller* Pembayaran ↔ API Midtrans<br>• Sistem Notifikasi ↔ Layanan Email<br>• Modul Pemesanan ↔ Modul Ketersediaan ↔ Modul Jadwal<br>• Autentikasi ↔ Otorisasi ↔ Manajemen Sesi<br>• Unggah Berkas ↔ Penyimpanan ↔ Pengambilan | **Jenis Pengujian Integrasi:**<br>• *Big Bang* (semua modul bersama)<br>• *Top-Down* (dari *controller* ke bawah)<br>• *Bottom-Up* (dari basis data ke atas)<br><br>**Skenario Uji:**<br>• Alur pemesanan *end-to-end* (pilih layanan → pembayaran → konfirmasi)<br>• Pendaftaran pengguna → verifikasi email → login<br>• *Webhook* pembayaran → pembaruan status → notifikasi email | **Pengujian HTTP Laravel:**<br>• `$this->post()`, `$this->get()`<br>• `$this->actingAs()` (uji terotentikasi)<br>• Asersi Basis Data<br><br>**Pengujian API:**<br>• Postman (manual)<br>• Pengujian HTTP PHPUnit (otomatis) | **25 Kasus Uji Integrasi:**<br>• Alur autentikasi: 4 uji<br>• Pemesanan *end-to-end*: 6 uji<br>• Integrasi pembayaran: 5 uji<br>• Notifikasi email: 4 uji<br>• Unggah berkas: 3 uji<br>• *Endpoint* API: 3 uji | ✅ **Tingkat Kelulusan 95%**<br>• 24/25 lulus<br>• 1 masalah minor (keterlambatan pengiriman email di lingkungan uji → diperbaiki dengan queue:work)<br>• Semua jalur kritis berfungsi | **Pengembang (Uji Silang):**<br>• Susanto menguji *backend* Roki<br>• Roki menguji operasi DB Fahruroji<br>• Fahruroji menguji *frontend* Susanto | **Minggu 8-9**<br>5-15 Nov 2024<br>• Setelah modul utama selesai<br>• Sebelum UAT<br>• 3 hari pengujian intensif | ✅ **LULUS**<br>• 24/25 uji lulus (96%)<br>• 1 masalah non-kritis diperbaiki<br>• Semua integrasi fungsional | ✅ **SELESAI**<br>(15 Nov 2024) |
| **3** | **Pengujian Fungsional** (*Functional Testing - Black-Box*) | • Memverifikasi sistem memenuhi semua kebutuhan fungsional (40 kebutuhan)<br>• Menguji fitur yang dihadapi pengguna<br>• Mengidentifikasi bug dari perspektif pengguna<br>• Tidak memerlukan pengetahuan kode | **Semua Fitur untuk 3 Peran Pengguna:**<br>• **Klien:** Pendaftaran, login, pemesanan (4 langkah), pembayaran, tampilan janji temu, penjadwalan ulang/batal, ulasan, profil<br>• **Terapis:** Manajemen jadwal, pengaturan ketersediaan, manajemen klien, catatan sesi, *dashboard* pendapatan<br>• **Admin:** CRUD pengguna, persetujuan terapis, manajemen layanan, pengawasan pemesanan, laporan, pengaturan sistem<br>• **Publik:** Halaman arahan, katalog layanan, direktori terapis, formulir kontak | **Teknik *Black-Box*:**<br>• *Equivalence Partitioning* (input valid/tidak valid)<br>• *Boundary Value Analysis* (nilai min/maks)<br>• *Decision Table Testing* (aturan bisnis kompleks)<br>• *Use Case Testing* (ikuti skenario kasus penggunaan)<br>• *Error Guessing* (skenario kesalahan umum)<br><br>**Struktur Kasus Uji:**<br>• ID Uji, Fitur, Langkah, Hasil Diharapkan, Hasil Aktual, Lulus/Gagal, Catatan | **Pengujian Manual:**<br>• Peramban (Chrome, Firefox, Safari)<br>• Berbagai perangkat (ponsel, tablet, desktop)<br>• *Spreadsheet* Kasus Uji (Excel)<br>• *Spreadsheet* Pelacakan Bug<br>• Alat tangkapan layar (untuk laporan bug) | **150+ Kasus Uji:**<br>• Autentikasi: 15 kasus<br>• Fitur klien: 40 kasus<br>• Fitur terapis: 35 kasus<br>• Fitur admin: 35 kasus<br>• Halaman publik: 15 kasus<br>• Kasus tepi & penanganan kesalahan: 10 kasus | ✅ **Tingkat Kelulusan 95% (Putaran Awal)**<br>• 143/150 lulus<br>• 7 gagal (bug ditemukan)<br><br>✅ **Tingkat Kelulusan 100% (Setelah Perbaikan Bug)**<br>• Semua 150 lulus setelah perbaikan | **Tim Pengujian:**<br>• Susanto (Koordinator Uji & Penguji Utama)<br>• Roki (30% eksekusi uji)<br>• Fahruroji (30% eksekusi uji)<br>• 2 penguji eksternal (tidak bias) | **Minggu 9**<br>11-17 Nov 2024<br>• 7 hari pengujian intensif<br>• 2 hari perbaikan bug<br>• 1 hari pengujian ulang | ✅ **LULUS (Setelah Perbaikan)**<br>• **Bug Ditemukan:** 25 total<br>  - Kritis: 2 (kasus tepi kegagalan pembayaran, upaya bypass autentikasi) ✅ Diperbaiki<br>  - Mayor: 8 (konflik pemesanan, masalah validasi) ✅ Diperbaiki<br>  - Minor: 15 (glitch UI, masalah UX minor) ✅ Diperbaiki<br>• 100% bug kritis & mayor terselesaikan | ✅ **SELESAI**<br>(20 Nov 2024) |
| **4** | **Pengujian Kegunaan** (*Usability Testing*) | • Mengevaluasi antarmuka pengguna dan pengalaman pengguna<br>• Mengukur kemudahan penggunaan (skor SUS)<br>• Mengidentifikasi masalah UI/UX<br>• Memvalidasi keputusan desain<br>• Meningkatkan kepuasan pengguna | **Tugas Pengguna Utama (15 Skenario):**<br>**Klien:**<br>• Daftar akun<br>• Pesan sesi terapi (alur 4 langkah)<br>• Lakukan pembayaran<br>• Lihat detail janji temu<br>• Jadwal ulang/batalkan pemesanan<br><br>**Terapis:**<br>• Atur ketersediaan mingguan<br>• Lihat sesi mendatang<br>• Tulis catatan sesi<br>• Lihat pendapatan<br><br>**Admin:**<br>• Setujui terapis baru<br>• Lihat laporan keuangan<br>• Kelola layanan | **Metode Kegunaan:**<br>• **Protokol *Think-Aloud*** (partisipan mengungkapkan pikiran saat menggunakan sistem)<br>• **Analisis Tugas** (amati keberhasilan penyelesaian tugas, waktu, kesalahan)<br>• ***System Usability Scale* (SUS)** (survei standar 10 pertanyaan, skor 0-100)<br>• **Evaluasi Heuristik** (10 heuristik kegunaan Nielsen)<br>• **Wawancara Pasca-Uji** (umpan balik kualitatif) | **Alat:**<br>• OBS Studio (perekaman layar)<br>• *Stopwatch* (waktu pada tugas)<br>• Google Forms (kuesioner SUS)<br>• Formulir Observasi (catatan)<br>• Excel (analisis data)<br>• Zoom (pengujian jarak jauh) | **18 Partisipan × 15 Tugas = 270 Percobaan Tugas**<br><br>**Metrik per Tugas:**<br>• Tingkat keberhasilan (biner: selesai/gagal)<br>• Waktu untuk menyelesaikan (detik)<br>• Jumlah kesalahan/klik salah<br>• Peringkat kepuasan (1-5)<br><br>**Plus Kuesioner SUS (10 item per partisipan)** | ✅ **Skor SUS ≥70** (Kegunaan Baik)<br>✅ **Tingkat Keberhasilan Tugas ≥80%**<br>✅ **Waktu pada Tugas dalam rentang wajar** (mis., alur pemesanan <3 menit)<br>✅ **Tingkat Kesalahan <10%** | **18 Partisipan (Sampel Beragam):**<br>• 5 Terapis (3 internal, 2 eksternal)<br>• 8 Klien (beragam usia, kemampuan teknologi)<br>• 4 Admin (2 internal, 2 eksternal)<br>• 1 Profesional Kesehatan<br><br>**Demografi:**<br>• Usia: 25-45<br>• Jenis Kelamin: 11 Perempuan, 7 Laki-laki<br>• Kemampuan teknologi: Rendah (3), Sedang (9), Tinggi (6) | **Minggu 10**<br>18-24 Nov 2024<br>• Sesi 2 jam per partisipan<br>• 3-4 partisipan per hari<br>• 6 hari total<br>• 1 hari analisis data | ✅ **HASIL SANGAT BAIK:**<br>• **Rata-rata Skor SUS: 78,5/100** (Nilai: B, kegunaan "Baik") ✅ Melampaui target 70<br>• **Tingkat Keberhasilan Tugas: 92%** ✅ Melampaui target 80%<br>• **Rata-rata Waktu pada Tugas:** Dalam rentang diharapkan (Pemesanan: rata-rata 2,5 menit, target <3 menit)<br>• **Tingkat Kesalahan: 6,8%** ✅ Di bawah target 10%<br><br>**Temuan Kualitatif:**<br>• Positif: UI bersih, alur pemesanan intuitif, navigasi jelas<br>• Masalah: 5 inkonsistensi UI minor, 2 label membingungkan (diperbaiki pasca-UAT) | ✅ **SELESAI**<br>(22 Nov 2024) |
| **5** | **Pengujian Kinerja** (*Performance Testing*) | • Mengukur responsivitas & kecepatan sistem<br>• Menguji skalabilitas (pengguna bersamaan)<br>• Mengidentifikasi hambatan kinerja<br>• Mengoptimalkan kueri basis data<br>• Memastikan pengalaman pengguna dapat diterima di bawah beban | **Metrik Kinerja:**<br>• **Waktu Muat Halaman** (target: <2 detik)<br>• **Waktu ke Byte Pertama** (*Time to First Byte*/TTFB) (target: <500ms)<br>• **Waktu Kueri Basis Data** (target: <100ms per kueri)<br>• **Pengguna Bersamaan** (target: menangani 50 pengguna simultan)<br>• **Waktu Respons API** (target: <1 detik)<br>• **Pemanfaatan Sumber Daya** (CPU, Memori, I/O Disk) | **Jenis Pengujian Kinerja:**<br>• **Pengujian Beban** (*Load Testing*) (simulasi beban normal yang diharapkan)<br>• **Pengujian Stres** (*Stress Testing*) (dorong melampaui batas untuk menemukan titik putus)<br>• **Pengujian Lonjakan** (*Spike Testing*) (peningkatan lalu lintas mendadak)<br>• **Pengujian Ketahanan** (*Endurance Testing*) (beban berkelanjutan dari waktu ke waktu)<br><br>**Teknik Optimasi:**<br>• Pengindeksan basis data (15 indeks ditambahkan)<br>• Optimasi kueri (eliminasi kueri N+1 dengan *eager loading*)<br>• *Caching* (Redis untuk sesi, hasil kueri)<br>• Optimasi aset (minifikasi CSS/JS, kompresi gambar) | **Alat:**<br>• **GTmetrix** (kecepatan halaman)<br>• **Google Lighthouse** (audit kinerja)<br>• **Laravel Debugbar** (profil kueri)<br>• **Apache JMeter** (pengujian beban)<br>• **New Relic/Blackfire** (APM - *Application Performance Monitoring*)<br>• MySQL EXPLAIN (analisis kueri) | **Skenario Uji:**<br>• 50 pengguna virtual memesan bersamaan (uji beban)<br>• Lonjakan 100 pengguna (uji stres)<br>• Pengukuran waktu muat halaman (semua 60+ halaman)<br>• Profil kueri basis data (20 kueri lambat teratas)<br>• Waktu respons *endpoint* API (10 *endpoint*) | ✅ **Waktu Muat Halaman <2 detik** (rata-rata di semua halaman)<br>✅ **Tangani 50 Pengguna Bersamaan** tanpa kesalahan/*crash*<br>✅ **Kueri Basis Data <100ms** (setelah optimasi)<br>✅ **Nol Masalah Kueri N+1**<br>✅ **Skor Lighthouse ≥85/100** (Kinerja) | **Insinyur Kinerja:**<br>• Fahruroji (Pemimpin optimasi basis data)<br>• Roki (Penyetelan kinerja *backend*)<br>• Susanto (Optimasi *frontend* - kompresi aset) | **Minggu 9-10**<br>16-21 Nov 2024<br>• 3 hari profil & identifikasi hambatan<br>• 2 hari optimasi<br>• 1 hari pengujian ulang | ✅ **LULUS:**<br>• **Rata-rata Waktu Muat Halaman: 1,8 detik** ✅ (target <2 detik)<br>• **TTFB: 450ms** ✅ (target <500ms)<br>• **50 Pengguna Bersamaan:** Ditangani dengan sukses ✅ (tingkat kesalahan 0%)<br>• **80 Pengguna:** Ditangani (uji stres, tingkat kesalahan 2% dapat diterima)<br>• **Skor Lighthouse: 88/100** ✅ (kategori Kinerja)<br>• **Basis Data:** 15 indeks ditambahkan, kueri N+1 dieliminasi, rata-rata waktu kueri 85ms ✅<br><br>**Hambatan Diidentifikasi & Diperbaiki:**<br>• Kueri pemesanan (10 *join*) → Dioptimalkan dengan *eager loading* & pengindeksan (2,5 detik → 0,15 detik)<br>• Grafik *dashboard* (agregasi kompleks) → Ditambahkan *caching* (3 detik → 0,3 detik) | ✅ **SELESAI**<br>(21 Nov 2024) |
| **6** | **Pengujian Keamanan** (*Security Testing*) | • Mengidentifikasi kerentanan keamanan<br>• Memastikan perlindungan data (PII, info pembayaran)<br>• Mencegah akses tidak sah<br>• Mitigasi risiko OWASP *Top* 10<br>• Validasi kepatuhan (UU PDP Indonesia) | **Cakupan Pengujian Keamanan:**<br>• **OWASP *Top* 10 (2021):**<br>  1. Kontrol Akses Rusak (*Broken Access Control*) ✅<br>  2. Kegagalan Kriptografi (*Cryptographic Failures*) ✅<br>  3. Injeksi (SQL, XSS, dll.) ✅<br>  4. Desain Tidak Aman (*Insecure Design*) ✅<br>  5. Konfigurasi Keamanan Salah (*Security Misconfiguration*) ✅<br>  6. Komponen Rentan (*Vulnerable Components*) ✅<br>  7. Kegagalan Autentikasi & Sesi ✅<br>  8. Integritas Perangkat Lunak & Data ✅<br>  9. Kegagalan *Logging* & Pemantauan ✅<br>  10. SSRF ✅<br>• **Tambahan:**<br>  - Proteksi CSRF ✅<br>  - XSS (*Reflected*, *Stored*, berbasis DOM) ✅<br>  - Pembajakan sesi (*Session hijacking*) ✅<br>  - Serangan *brute force* ✅<br>  - Kerentanan unggah berkas ✅ | **Jenis Pengujian Keamanan:**<br>• **Pemindaian Kerentanan** (*Vulnerability Scanning*) (alat otomatis mendeteksi kerentanan yang diketahui)<br>• **Pengujian Penetrasi** (*Penetration Testing*) (upaya manual untuk mengeksploitasi kerentanan)<br>• **Tinjauan Kode** (*Code Review*) (analisis statis untuk kelemahan keamanan)<br>• **Pengujian Autentikasi** (kekuatan kata sandi, manajemen sesi, MFA)<br>• **Pengujian Otorisasi** (eskalasi hak akses, kontrol akses horizontal/vertikal)<br>• **Pengujian Validasi Input** (injeksi SQL, XSS, injeksi perintah)<br>• **Pengujian Manajemen Sesi** (fiksasi sesi, pembajakan, *timeout*) | **Alat:**<br>• **OWASP ZAP** (*Zed Attack Proxy* - pemindai kerentanan)<br>• **Burp Suite Community** (pengujian keamanan web)<br>• **SQL Map** (pengujian injeksi SQL)<br>• **Laravel Security Checker** (periksa dependensi untuk kerentanan yang diketahui)<br>• **Pengujian Manual** (Postman untuk pengujian autentikasi, *browser DevTools*) | **Kasus Uji (Skenario Keamanan):**<br>• Upaya injeksi SQL (20 *payload*)<br>• Upaya XSS (15 *payload*: *reflected*, *stored*)<br>• Upaya *bypass* CSRF (10 skenario)<br>• Upaya *bypass* autentikasi (8 skenario)<br>• Upaya *bypass* otorisasi (10 skenario: eskalasi hak akses, akses horizontal)<br>• Upaya pembajakan sesi (5 skenario)<br>• Serangan unggah berkas (5 skenario: berkas berbahaya, *path traversal*)<br>• Login *brute force* (uji pembatasan laju) | ✅ **NOL Kerentanan Kritis**<br>✅ **OWASP *Top* 10 Semua Dimitigasi**<br>✅ **Semua Kasus Uji Keamanan Diblokir** (sistem berhasil mencegah serangan)<br>✅ ***Header* Keamanan Ada** (X-Frame-Options, X-XSS-Protection, CSP)<br>✅ **Data Sensitif Terenkripsi** (kata sandi di-*hash* dengan bcrypt, PII terenkripsi saat istirahat) | **Penguji Keamanan:**<br>• Roki Anjas (Pemimpin Keamanan)<br>• 1 Konsultan Keamanan Eksternal (audit independen - opsional, jika anggaran memungkinkan) | **Minggu 10**<br>19-23 Nov 2024<br>• 3 hari pemindaian otomatis (OWASP ZAP, Burp Suite)<br>• 2 hari pengujian penetrasi manual<br>• 1 hari laporan & rekomendasi | ✅ **LULUS (AMAN):**<br>• **Kerentanan Kritis: 0** ✅<br>• **Kerentanan Tinggi: 0** ✅<br>• **Sedang: 2** (keduanya dimitigasi sebelum peluncuran):<br>  - *Header* keamanan hilang (X-Content-Type-Options) ✅ Diperbaiki<br>  - Kebijakan kekuatan kata sandi tidak diterapkan ✅ Diperbaiki (ditambahkan validasi: min 8 karakter, 1 huruf besar, 1 angka)<br>• **Rendah: 5** (kosmetik, prioritas rendah):<br>  - Pesan kesalahan *verbose* (dapat diterima untuk sekarang)<br>  - *Clickjacking* pada halaman publik (risiko rendah, dimitigasi dengan X-Frame-Options)<br><br>**Status Mitigasi OWASP *Top* 10:**<br>• Semua 10 risiko ditangani ✅<br>• Proteksi bawaan Laravel dimanfaatkan (token CSRF, *hashing* kata sandi, pencegahan injeksi SQL via Eloquent ORM)<br>• Proteksi tambahan ditambahkan (pembatasan laju, sanitasi input, *encoding output*) | ✅ **SELESAI**<br>(23 Nov 2024) |
| **7** | **Pengujian Penerimaan Pengguna** (*User Acceptance Testing*/UAT) | • Memvalidasi sistem memenuhi kebutuhan bisnis<br>• Mendapatkan persetujuan pemangku kepentingan untuk peluncuran<br>• Memastikan pengguna nyata dapat menggunakan sistem secara efektif<br>• Validasi final sebelum penyebaran | **Cakupan UAT:**<br>• **Skenario Bisnis (Kasus Penggunaan Dunia Nyata):**<br>  - Admin: Orientasi terapis baru, hasilkan laporan pendapatan bulanan<br>  - Terapis: Kelola jadwal seminggu penuh, lakukan sesi & dokumentasi catatan<br>  - Klien: Pesan sesi, lakukan pembayaran, terima konfirmasi, hadiri sesi<br>• **Kriteria Penerimaan:** 90% kebutuhan fungsional terpenuhi (36/40 kebutuhan minimum) | **Proses UAT:**<br>1. **Perencanaan UAT:** Siapkan rencana UAT, skenario, kriteria persetujuan<br>2. **Pelatihan UAT:** *Brief* pemangku kepentingan tentang sistem (pelatihan 30 menit)<br>3. **Eksekusi UAT:** Pemangku kepentingan menguji sistem secara mandiri (dengan observasi)<br>4. **Pengumpulan Umpan Balik:** Kumpulkan umpan balik via kuesioner & wawancara<br>5. **Penyelesaian Masalah:** Perbaiki masalah kritis yang ditemukan selama UAT<br>6. **Persetujuan:** Dapatkan tanda tangan persetujuan formal | **Lingkungan UAT:**<br>• Server *staging* (seperti produksi)<br>• Data seperti nyata (data sampel teranonimisasi)<br>• *Payment gateway* produksi (mode *sandbox*)<br><br>**Dokumentasi:**<br>• Rencana Uji UAT<br>• Kasus Uji UAT (dipetakan ke kebutuhan bisnis)<br>• Formulir Persetujuan UAT<br>• Formulir Umpan Balik | **Kasus Uji UAT:**<br>• 40 kebutuhan fungsional dipetakan ke kasus uji<br>• Setiap pemangku kepentingan menguji fitur relevan:<br>  - Pemilik: 10 fitur strategis/pelaporan<br>  - Terapis: 15 fitur *dashboard* terapis<br>  - Admin: 12 fitur admin<br>  - Klien: 12 fitur klien<br>• Total skenario unik: 35 (beberapa tumpang tindih) | ✅ **90% Kebutuhan Fungsional Terpenuhi** (36/40 minimum)<br>✅ **Kepuasan Pemangku Kepentingan ≥8/10**<br>✅ **Nol Masalah Kritis Ditemukan**<br>✅ **Persetujuan Formal Diperoleh** (tanda tangan) | **Partisipan UAT (Pemangku Kepentingan Nyata):**<br>• Pemilik CUR-HEART (1)<br>• Terapis (3)<br>• Admin/Staf (2)<br>• Sampel Klien (5)<br><br>**Total: 11 Partisipan UAT** (subset dari 18 partisipan pengujian kegunaan) | **Minggu 10**<br>22-24 Nov 2024<br>• Hari 1 (22 Nov): Pelatihan & penyiapan (2 jam)<br>• Hari 2 (23 Nov): Pengujian mandiri oleh pemangku kepentingan (4 jam)<br>• Hari 3 (24 Nov): Tinjauan umpan balik, diskusi masalah, persetujuan (3 jam) | ✅ **DISETUJUI & DITANDATANGANI:**<br>• **Kebutuhan Terpenuhi: 90%** (36/40) ✅ Tepat di ambang batas<br>• **Ditunda ke Fase 2 (4 kebutuhan):**<br>  1. Notifikasi SMS (email cukup untuk sekarang)<br>  2. Integrasi sesi video (*link* Zoom sebagai solusi sementara)<br>  3. *Dashboard* analitik lanjutan (laporan dasar cukup)<br>  4. Aplikasi mobile (web responsif cukup)<br>• **Kepuasan Pemangku Kepentingan: 9/10** ✅ Melampaui target 8/10<br>• **Masalah Kritis: 0** ✅<br>• **Masalah Mayor: 2** (keduanya diperbaiki dalam 24 jam sebelum peluncuran):<br>  - Terapis tidak bisa melihat semua detail pemesanan (masalah izin) ✅ Diperbaiki<br>  - Email konfirmasi pembayaran tidak terkirim (*queue worker* tidak berjalan) ✅ Diperbaiki<br>• **Persetujuan Formal Diterima:** 24 Nov 2024, ditandatangani oleh Pemilik CUR-HEART ✅ | ✅ **SELESAI & DISETUJUI**<br>(24 Nov 2024) |

**Ringkasan Pengujian:**

| Fase Pengujian | Kasus Uji | Tingkat Kelulusan | Masalah Kritis Ditemukan | Status | Durasi |
|--------------|-----------|-----------|---------------------|--------|----------|
| Pengujian Unit | 30 | 100% | 0 | ✅ Lulus | 2 minggu (berkelanjutan) |
| Pengujian Integrasi | 25 | 96% (24/25) | 0 | ✅ Lulus | 3 hari |
| Pengujian Fungsional | 150 | 100% (setelah perbaikan) | 2 (diperbaiki) | ✅ Lulus | 7 hari |
| Pengujian Kegunaan | 270 percobaan tugas (18 pengguna × 15 tugas) | 92% tingkat keberhasilan | 0 | ✅ Lulus (SUS: 78,5) | 6 hari |
| Pengujian Kinerja | ~20 skenario | 100% | 0 | ✅ Lulus | 5 hari |
| Pengujian Keamanan | 73 skenario serangan | 100% diblokir | 0 | ✅ Lulus (sesuai OWASP) | 5 hari |
| UAT | 36 kebutuhan | 90% terpenuhi | 0 (2 mayor diperbaiki) | ✅ Disetujui | 3 hari |
| **TOTAL** | **594+ Kasus Uji/Skenario** | **~95% Keseluruhan** | **2 Kritis (Diperbaiki)** | ✅ **SIAP PRODUKSI** | **14 hari (Minggu 9-10)** |

---

Dengan menggunakan berbagai teknik pengumpulan data dan metode pengujian komprehensif ini, penelitian akan menghasilkan pemahaman menyeluruh tentang kebutuhan, kendala, dan ekspektasi dari pemangku kepentingan, serta bukti empiris tentang kegunaan, kinerja, keamanan, dan efektivitas dari sistem yang dikembangkan. Kombinasi dari metode kualitatif (observasi, wawancara) dan metode kuantitatif (survei, metrik kegunaan, *benchmark* kinerja) akan memberikan triangulasi, meningkatkan validitas dan reliabilitas dari temuan.

---
