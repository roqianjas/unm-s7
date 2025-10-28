**Briefing Tugas — Tahap Persiapan Bahan & Metode Analisis**  
**Mata Kuliah: IT Governance & Audit**

Dokumen ini adalah briefing resmi untuk tahap berikutnya setelah penyusunan bagian Tujuan Proyek. Fokus tahap ini ada dua: (1) menyiapkan bahan/data yang akan dianalisis, dan (2) menentukan metode/pendekatan analisis yang akan digunakan. Harap dibaca sampai tuntas; seluruh bagian di bawah berisi langkah kerja, checklist, panduan pemilihan metode, rubrik penilaian, serta ketentuan pengumpulan. Catatan: pada tahap ini kalian belum perlu melakukan analisis penuh.

## **1\) Tujuan Tugas**

* Mampu mengidentifikasi bukti/artefak yang relevan dengan tujuan proyek.  
* Mampu memilih dan menjelaskan metode analisis yang tepat, berbasis framework yang diakui.  
* Menyusun rencana kerja analisis yang realistis dan dapat direplikasi (reproducible).

## **2\) Output yang Dikumpulkan (Deliverables)**

1. Ringkasan konteks & tujuan (≤ ½ halaman).  
2. Daftar bahan/data yang akan digunakan beserta sumber dan alasan relevansi.  
3. Metode/pendekatan analisis yang dipilih, termasuk alasan pemilihan, ruang lingkup, dan langkah singkat.  
4. Rencana kerja (timeline tingkat-minggu, peran tim, dependensi).  
5. Matriks pemetaan tujuan ↔ data ↔ metode (traceability).  
6. Rencana validasi & etika data (akses, privasi, izin).  
7. Risiko & mitigasi (minimal 3 butir).

**Catatan:** Belum perlu melakukan analisis penuh. Tahap ini fokus pada persiapan yang siap dieksekusi.

## **3\) Batasan & Aturan**

* Ruang lingkup: pilih 1–2 domain proses saja (mis. Change Management & Access Management) agar fokus.  
* Framework payung: COBIT 2019 (boleh kombinasikan ISO/IEC 27001, ITIL 4, atau NIST SP 800-53 jika relevan).  
* Data: fiktif atau nyata diperbolehkan. Jika menggunakan data nyata, wajib anonimisasi identitas sensitif.  
* Sitasi: gunakan gaya sitasi yang konsisten (mis. APA/IEEE).  
* Panjang dokumen: 3–6 halaman (tidak termasuk lampiran).  
* Kolaborasi: tim 2–4 orang; cantumkan pembagian peran di halaman awal.

## **4\) Langkah Kerja (Step-by-Step)**

8. Perjelas tujuan (review singkat dari dokumen sebelumnya): rumuskan ulang indikator keberhasilan dan batasan.  
9. Pemetaan proses & kontrol: tentukan domain (mis. domain COBIT terkait) dan kontrol utama yang relevan.  
10. Inventarisasi bahan/data: kumpulkan kandidat bukti (lihat Checklist) lalu seleksi yang paling relevan.  
11. Pilih metode analisis: gunakan Panduan Pemilihan Metode pada bagian 6 untuk menyesuaikan dengan tujuan dan data.  
12. Rancang rencana kerja: buat timeline mingguan, RACI, dan daftar dependensi (izin akses, jadwal wawancara, dsb.).  
13. Rencana validasi & etika: jelaskan verifikasi bukti (triangulasi) & langkah menjaga kerahasiaan data.  
14. Risiko & mitigasi: minimal 3 risiko beserta mitigasinya (contoh: data tidak lengkap, bias responden, jadwal molor).

## **5\) Checklist Bahan/Data (Pilih yang Relevan)**

* Kebijakan & Prosedur:

* Kebijakan TI/ISMS, SOP Change/Access/Backup, Work Instruction/Standard Operating Procedure.  
* Charter Komite TI, Risk Appetite Statement.

* Artefak Proses:

* Ticketing (incident/change/service request), change log, risalah rapat CAB (minutes).  
* Access request & approval record, user access review, joiner–mover–leaver.  
* Backup log & hasil uji restore.  
* Artefak SDLC: BRD, test plan, UAT sign-off, deployment checklist.

* Kontrol & Bukti Teknis:

* Konfigurasi kontrol (mis. MFA policy, password policy), contoh alert SIEM.  
* Segregation of Duties (SoD) matrix, snapshot firewall rules.  
* Sampling log aplikasi/DB, audit trail.

* Manajemen Risiko & Kinerja:

* Risk register, KRI/KPI, hasil internal audit sebelumnya.  
* Maturity/self-assessment (jika tersedia).

* Wawancara/Observasi (opsional):

* Daftar pertanyaan singkat untuk PIC proses.  
* Hasil walkthrough (dengan redaksi/anonimisasi seperlunya).

* Metadata Data:

* Sumber, periode, pemilik data, sensitivitas, batas penggunaan.

## **6\) Pilihan Metode & Kapan Dipakai**

* **Pemetaan COBIT 2019 → Kontrol/Kesenjangan**

* Gunakan saat ingin melihat keselarasan proses & kontrol terhadap tujuan TI. Output: matriks praktik-proses, temuan gap, rekomendasi awal.

* **Uji Kontrol ITGC/ITAC (Design & Operating Effectiveness)**

* Gunakan saat menilai desain dan efektivitas operasional kontrol umum TI (akses, change, operasi) atau kontrol aplikasi. Output: tabel uji (populasi, sampel, langkah uji, hasil, kesimpulan).

* **Risk Assessment (ISO 27005/ISO 31000\)**

* Gunakan saat fokus pada risiko dan membutuhkan prioritas berbasis dampak & kemungkinan. Output: daftar aset–ancaman–kerentanan, skoring, rencana perlakuan risiko.

* **Maturity/Capability Scoring (COBIT/Process Attribute)**

* Gunakan saat ingin baseline level kematangan & target. Output: skor per atribut (PA1–PA5), gap & roadmap singkat.

* **RACI & Process Walkthrough**

* Gunakan saat stakeholder banyak dan butuh kejelasan peran & bottleneck. Output: matriks RACI, peta pain point proses.

* **Benchmark Control (ISO/IEC 27001 Annex A / NIST)**

* Gunakan saat perlu pembanding kontrol standar. Output: mapping kontrol yang ada vs yang disyaratkan, gap list.

* Decision Helper (ringkas):

* Tujuan \= kepatuhan standar → Benchmark Control \+ Uji Desain.  
* Tujuan \= mengurangi insiden → Uji Operasional \+ Walkthrough proses.  
* Tujuan \= prioritas perbaikan → Risk Assessment \+ Maturity.  
* Tujuan \= kejelasan peran → RACI \+ SIPOC/process map.

## **7\) Rubrik Penilaian (Total 100\)**

* Relevansi & kelengkapan bahan (25) — data selaras tujuan, ada metadata & akses.  
* Kecocokan metode (25) — metode tepat, ada justifikasi, jelas scope & batasan.  
* Rencana kerja & reproducibility (20) — timeline, RACI, langkah uji jelas dan dapat diulang.  
* Traceability tujuan–data–metode (15) — matriks rapi, tidak ada loncatan logika.  
* Etika & validasi data (10) — privasi, izin, rencana verifikasi.  
* Kerapian & sitasi (5).  
* Bonus (maks 5\) — kreativitas visual & ketajaman risiko–mitigasi.

## **8\) Kesalahan Umum & Tips**

Hindari:

* Mengumpulkan data yang tidak menjawab tujuan.  
* Memilih metode yang terlalu kompleks untuk kualitas/kuantitas data yang tersedia.  
* Tidak menuliskan rencana validasi (hanya mengandalkan satu sumber).  
* Memperluas scope berlebihan.

Tips:

* Mulai dari pertanyaan audit yang spesifik (mis. “Kontrol X dirancang dan berjalan efektif?”).  
* Dokumentasikan asumsi dan keterbatasan sejak awal.  
* Gunakan penamaan file yang konsisten (mis. TeamA\_PersiapanAnalisis\_v1).

## **9\) Format Pengumpulan**

* Nama file: Kelas\_TeamX\_PersiapanAnalisis\_v1  
* Format: PDF/Doc, 3–6 halaman (lampiran tidak dihitung).  
* Daftar anggota & peran dicantumkan di halaman awal.  
* Lampiran opsional: contoh bukti (di-anonimkan) dan daftar pertanyaan wawancara (jika ada).