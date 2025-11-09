# TEMPLATE BRIEFING — MINGGU KE-6 Perancangan Instrumen & Bukti Audit (IT Governance & Audit)

Tujuan minggu ini: menurunkan rumusan masalah & tujuan (minggu 4–5) menjadi instrumen audit dan rencana bukti yang siap dieksekusi. Output mencakup: Control & Evidence Register, instrumen (checklist, kuesioner, wawancara), rencana sampling & validasi, RACI & timeline, serta skema scoring/maturity.

# **1\) Lingkup (Scope)**

**• Domain COBIT yang dipilih (maks. 4):** 

EDM03, APO12, DSS01/DSS06, MEA01 (contoh).

**• Proses/bisnis yang diaudit:** 

Satu proses inti \+ satu pendukung (mis. order→pembayaran→pengiriman).

**• Sumber bukti:** 

SOP, log sistem, tangkapan layar, laporan KPI, kontrak, form, dsb.

# **2\) Deliverables (Dikumpulkan)**

1\. Control & Evidence Register (maks 3 hlm)

2\. Instrumen: Checklist kontrol (ITGC/ITAC), Kuesioner (Likert 1–5), Panduan Wawancara (6–8 Q per peran), Template bukti.

3\. Rencana Sampling & Validasi (1 hlm)

4\. RACI & Timeline 3 minggu (1 hlm)

5\. Skema Scoring/Maturity (1 hlm)

# **3\) Rubrik Penilaian (100)**

| Komponen | Bobot |
| :---- | :---- |
| Control & Evidence Register | 30 |
| Kualitas Instrumen (checklist, kuesioner, wawancara) | 25 |
| Rencana Sampling & Validasi | 15 |
| RACI & Timeline | 10 |
| Skema Scoring/Maturity | 10 |
| Keterpaduan & Kerapian | 10 |

# **4\) Control & Evidence Register (Template)**

| Domain/Proses | Control Objective | Risiko | KPI/Metrik | Bukti diminta | Sumber Data | Frekuensi | Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| APO12.01 | Risk Management Framework disetujui & dioperasionalkan | Perubahan tanpa analisis risiko | % risiko punya owner | Risk register \+ penetapan owner \+ matriks dampak×kemungkinan | Manrisk/TI | Bulanan | Head TI |
| DSS06 | Manage Business Process Controls | Aktivitas manual tanpa jejak | % aktivitas terekam | SOP, log sistem, contoh audit trail | App Owner | Mingguan | Admin App |
| MEA01 | Monitor, Evaluate & Assess Performance | KPI tidak konsisten | % KPI on-target | Dashboard KPI, notulen rapat kinerja | PMO/QA | Bulanan | PMO |

Catatan: batasi 6–10 kontrol paling relevan.

# **5\) Checklist Kontrol (ITGC/ITAC)**

Struktur kolom: ID | Pernyataan kontrol (Ya/Tidak/N/A) | Bukti diminta | Lokasi bukti/tautan | Catatan auditor

Contoh butir ITGC – Akses: "Setiap akun produksi punya unique ID dan role terdokumentasi (Ya/Tidak). Bukti: export user & role (CSV)."

Contoh butir ITAC – Aplikasi: "Sistem memvalidasi duplikasi nomor transaksi sebelum posting (Ya/Tidak). Bukti: screenshot setting \+ uji coba 2 transaksi duplikat."

# **6\) Kuesioner (Likert 1–5)**

Contoh item:

\- Organisasi memiliki daftar risiko TI yang diperbarui berkala.

\- Akses ke data sensitif ditinjau minimal per kuartal.

\- Backup dan uji restore dilakukan sesuai jadwal.

\- Proses insiden memiliki SLA dan root-cause analysis.

# **7\) Panduan Wawancara**

Peran: Manajer Unit / Pemilik Proses

• Apa tiga risiko TI terbesar di proses Anda tahun ini?

• Bagaimana persetujuan perubahan akses dilakukan dan dicatat?

• Seberapa sering KPI/insiden ditinjau dan ditindaklanjuti?

Peran: Admin Aplikasi / Admin TI

• Bagaimana Anda mengekspor daftar user & role?

• Contoh bukti terakhir yang diberikan ke auditor?

# **8\) Rencana Sampling & Validasi**

Populasi, teknik sampling (total/stratified/purposive), ukuran sampel, langkah validasi (triangulasi: dokumen–wawancara–data).

Contoh: Ambil 10 tiket insiden prioritas tinggi Q1–Q2 (DSS02), cocokkan SLA di tiket vs laporan KPI bulanan (MEA01), verifikasi RCA & approval.

# **9\) RACI & Timeline (3 minggu)**

| Aktivitas | R | A | C | I |
| :---- | :---- | :---- | :---- | :---- |
| Ekspor daftar user & role | Admin App | Head TI | Auditor Tim | Owner Proses |
| Wawancara App Owner | Auditor Tim | Ketua Tim | HR/PMO | Manajemen |

Timeline: M1 – finalisasi instrumen & akses data; M2 – kumpulkan bukti dokumen \+ kuesioner (≥70% respon); M3 – wawancara \+ uji bukti \+ scoring awal.

# **10\) Skema Scoring/Maturity**

Gunakan COBIT PAM 0–5 atau PA1–PA5. Tentukan bobot per domain (mis. EDM 20%, APO 25%, DSS 35%, MEA 20%).

Aturan konversi contoh: bukti lengkap=1; parsial=0,5; tidak ada=0. Rata-rata → level kapabilitas.

Contoh DSS06: bukti wajib 3 item, terpenuhi 2 → skor 0,67 → Level 2 (Managed) dengan catatan: monitoring belum rutin.

# **11\) Contoh Paket “Siap Pakai”**

Judul: Audit Pengendalian Akses Aplikasi POS (DSS05, DSS06)

Kontrol Kunci: DSS05.01 – Identity Management; DSS06.02 – Application Controls.

Instrumen: Checklist 12 butir; Kuesioner 10 butir; Wawancara 7 pertanyaan.

Bukti: export user-role (CSV), log approval akses (PDF), screenshot setting validasi, laporan review akses Q1–Q2.

Sampling: 20 akun aktif acak \+ 10 perubahan akses 6 bulan terakhir.

Scoring: 80% terpenuhi → Level 3 (Established); gap: tidak ada bukti review akses periode Q2.

# **12\) Checklist Kualitas (Sebelum Submit)**

□ Kontrol selaras risiko & domain COBIT

□ Setiap kontrol punya bukti spesifik & obtainable

□ Instrumen tidak leading, pertanyaan jelas

□ Sampling realistis & ada triangulasi

□ RACI & timeline feasible

□ Skema scoring transparan \+ contoh kalkulasi

Catatan: Template ini netral untuk IT Governance dan Audit. Untuk kelas Audit, tekankan bukti & pengujian kontrol (ITGC/ITAC). Untuk kelas IT Governance, tekankan penyelarasan, kebijakan, dan target maturity.  
