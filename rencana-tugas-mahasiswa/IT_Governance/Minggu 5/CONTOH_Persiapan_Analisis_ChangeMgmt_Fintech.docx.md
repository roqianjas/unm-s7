**CONTOH — Persiapan Bahan & Metode Analisis (Mudah Diikuti)**  
**Domain: Change Management (Fintech)**

Catatan: Ini contoh pengisian yang ringkas dan mudah dipahami. Silakan adaptasi sesuai konteks proyek kalian.

## **A. Identitas Tim**

• Nama Tim: Orion

• Anggota & Peran: A (Lead), B (Analis Data), C (PIC Wawancara)

• Kontak: orion-team@example.edu

## **B. Ringkasan Konteks & Tujuan**

• Konteks: Perusahaan fintech menengah menggunakan ServiceNow untuk change management. Tingkat kegagalan change (failed change) Q2–Q3 2025 \= 4%.

• Tujuan (SMART): Menurunkan failed change produksi menjadi \<2% per kuartal pada Q1 2026\.

## **C. Ruang Lingkup & Framework**

• Ruang lingkup: proses Change Management (High-Risk Change).

• Framework: COBIT 2019 (DSS06/BAI06) \+ ITIL 4 (Change Enablement).

• Batasan: data 6 bulan terakhir; wawancara 2 narasumber (Change Manager & CAB Chair).

## **D. Matriks Tujuan ↔ Data ↔ Metode (Traceability)**

| Tujuan | Data/Bahan | Alasan Relevansi | Metode | Output Diharapkan |
| :---- | :---- | :---- | :---- | :---- |
| Turunkan failed change \<2% | Change log 6 bulan; Minutes CAB; SOP Change | Menggambarkan kepatuhan approval & klasifikasi risiko | Uji kontrol (desain & operasional) | Tingkat kepatuhan; gap approval/quorum |
| Perjelas peran | Daftar peran; flow proses | Identifikasi bottleneck persetujuan | RACI & walkthrough | RACI yang disepakati; pain point |

## **E. Daftar Bahan/Data**

| No | Nama Bahan | Sumber | Periode | Pemilik | Sensitivitas | Status Akses |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Change Log (High-Risk) | ServiceNow | Apr–Sep 2025 | IT Ops | Internal | Siap |
| 2 | Minutes Rapat CAB | SharePoint | Apr–Sep 2025 | Change Mgr | Internal | Diminta |
| 3 | SOP Change & Kriteria Risiko | Confluence | Versi 2025.06 | QA/PMO | Internal | Siap |

## **F. Metode/Pendekatan Analisis**

• Metode utama: Uji Desain & Operasional kontrol persetujuan CAB pada high-risk change.

• Alasan: hipotesis awal menyebut weak gatekeeping; perlu bukti kepatuhan & waktu persetujuan.

• Ruang lingkup: high-risk change; metrik: % tiket dengan persetujuan valid & quorum sebelum deploy.

• Langkah: definisikan populasi → sampling → telusuri bukti → catat hasil → simpulkan (tanpa analisis penuh di tahap ini).

## **G. Rencana Uji Kontrol (ITGC/ITAC)**

| Kontrol | Tujuan Kontrol | Populasi | Metode Sampling | Langkah Uji | Bukti | Hasil yang Diharapkan |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Persetujuan CAB untuk High-Risk Change | Memastikan semua high-risk change disetujui pihak berwenang | 320 tiket (Apr–Sep 2025\) | Acak 25 sampel, dokumentasikan seed | Cek field risk; verifikasi tanda persetujuan & timestamp \< deploy | Export CSV, screenshot approval, minutes | ≥ 95% kepatuhan; temuan didokumentasikan |
| Quorum CAB (3 orang termasuk owner bisnis) | Menjamin governance dan akuntabilitas keputusan change | Sama dengan di atas | Acak 25 sampel (sama) | Cocokkan daftar hadir/quorum di minutes vs tiket | Minutes rapat; log persetujuan elektronik | ≥ 90% memenuhi quorum |

## **H. Risk Assessment (opsional)**

| Aset/Proses | Ancaman | Kerentanan | Dampak | Kemungkinan | Skor | Perlakuan |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Proses High-Risk Change | Bypass approval | SOP longgar; tidak ada gate otomatis | Tinggi | Sedang | Tinggi | Otomasi gate \+ reminder |
| Dokumentasi CAB | Quorum tidak tercapai | Ketidakhadiran rutin | Sedang | Sedang | Sedang | Penjadwalan ulang; deputi |

## **I. Maturity/Capability Scoring (opsional)**

| Proses | Atribut | Level Saat Ini | Bukti | Target | Gap | Catatan |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| DSS06 Change | PA2 | 2 | SOP; log; minutes | 3 | 1 | Butuh KPI & review periodik |

## **J. RACI & Timeline**

RACI:

| Aktivitas | R | A | C | I |
| :---- | :---- | :---- | :---- | :---- |
| Sampling tiket | Analis | Lead | IT Ops | CAB |
| Wawancara | PIC Wawancara | Lead | Change Mgr | — |
| Uji dokumen | Analis | Lead | QA | — |

Timeline (mingguan):

| Minggu | Aktivitas Kunci | Ketergantungan |
| :---- | :---- | :---- |
| 1 | Kumpulkan dokumen & akses data | Izin akses |
| 2 | Sampling & verifikasi bukti | Export log |
| 3 | Walkthrough & finalisasi rencana uji | Jadwal wawancara |

## **K. Validasi & Etika Data**

• Triangulasi: cocokkan SOP ↔ tiket ↔ minutes.

• Privasi: anonimisasi nama user & masking ID sensitif.

• Izin: sertakan bukti persetujuan penggunaan data internal.

## **L. Risiko Proyek & Mitigasi**

| Risiko | Dampak | Probabilitas | Mitigasi |
| :---- | :---- | :---- | :---- |
| Data minutes tidak lengkap | Sedang | Sedang | Konfirmasi ke CAB; gunakan daftar hadir |
| Waktu akses log terlambat | Sedang | Tinggi | Ajukan akses lebih awal; fallback sampel kecil |

