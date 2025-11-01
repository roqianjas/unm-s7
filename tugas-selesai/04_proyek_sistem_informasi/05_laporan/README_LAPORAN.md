# README - LAPORAN CAPSTONE PROJECT CUR-HEART
## Panduan Lengkap Finalisasi Dokumen

---

## 📋 DAFTAR FILE LAPORAN

Laporan Capstone Project CUR-HEART terdiri dari file-file berikut:

### File Utama (Markdown)
```
laporan/
├── 00_BAGIAN_AWAL.md                                    # Halaman depan, pengesahan, abstrak
├── 01_BAB_I_PENDAHULUAN.md                              # Latar belakang, masalah, tujuan
├── 02_BAB_II_TINJAUAN_PUSTAKA.md                        # Teori dan penelitian terkait
├── 03_BAB_III_METODOLOGI_PENELITIAN.md                  # Metode penelitian
├── 04_BAB_IV_HASIL_PENELITIAN_DAN_PEMBAHASAN.md         # Bagian 1: Inisiasi & Perencanaan
├── 04_BAB_IV_BAGIAN_2_Database_Design.md                # Bagian 2: ERD & Database
├── 04_BAB_IV_BAGIAN_3_UML_Diagrams.md                   # Bagian 3: Use Case, Activity, Sequence
├── 04_BAB_IV_BAGIAN_4_Faktor_Keberhasilan_dan_Keuntungan.md  # Bagian 4: KSF, CSF, KPI, ROI
├── 04_BAB_IV_BAGIAN_5_Teknologi_dan_Desiminasi.md       # Bagian 5: Tech stack & Dissemination
├── 05_BAB_V_PENUTUP.md                                  # Kesimpulan dan saran
├── 06_DAFTAR_ISI_GAMBAR_TABEL.md                        # Daftar isi, gambar, tabel
├── 07_DAFTAR_PUSTAKA.md                                 # Referensi (45 sumber)
└── README_LAPORAN.md                                    # File ini
```

### Total Konten
- **~60,000+ kata** (~100 halaman format A4)
- **45 referensi** (buku, jurnal, online, standar)
- **50+ gambar/diagram** (placeholder untuk screenshot mockup, ERD, UML, dll.)
- **50+ tabel** (data, analisis, requirements, dll.)

---

## 🎯 LANGKAH-LANGKAH FINALISASI

### TAHAP 1: Persiapan Dokumen MS Word

#### 1.1 Setup Template Word
1. Buka Microsoft Word
2. Buat dokumen baru
3. Set page setup:
   - **Size**: A4 (21 x 29.7 cm)
   - **Margins**: 
     - Top: 3 cm
     - Bottom: 3 cm
     - Left: 4 cm
     - Right: 3 cm
   - **Orientation**: Portrait

#### 1.2 Set Styles
Buat Heading Styles untuk consistency:

**Heading 1 (BAB):**
- Font: Times New Roman, 14 pt, Bold
- Alignment: Center
- Spacing: Before 24pt, After 12pt
- Format: ALL CAPS
- Numbering: Romawi (I, II, III, IV, V)

**Heading 2 (Sub-Bab Level 1):**
- Font: Times New Roman, 12 pt, Bold
- Alignment: Left
- Spacing: Before 12pt, After 6pt
- Numbering: 1.1, 1.2, 2.1, dst.

**Heading 3 (Sub-Bab Level 2):**
- Font: Times New Roman, 12 pt, Bold
- Alignment: Left
- Spacing: Before 6pt, After 6pt
- Numbering: 1.1.1, 1.1.2, dst.

**Body Text:**
- Font: Times New Roman, 12 pt, Regular
- Alignment: Justify
- Line Spacing: 1.5
- Indentation: First line 1 cm

**Caption (Gambar/Tabel):**
- Font: Times New Roman, 10 pt, Regular
- Alignment: Center (gambar) / Left (tabel)
- Spacing: Before 6pt

---

### TAHAP 2: Copy Content dari Markdown ke Word

#### 2.1 Urutan Penyusunan
Copy content dalam urutan berikut:

**BAGIAN AWAL (Penomoran Romawi Kecil: i, ii, iii, ...)**
1. Cover/Lembar Judul (i) - **TIDAK DIBERI NOMOR HALAMAN**
2. Lembar Deskripsi Tugas (ii)
3. Lembar Pengesahan (iii)
4. Kata Pengantar (iv)
5. Abstrak Bahasa Indonesia (v)
6. Abstract Bahasa Inggris (vi)
7. Daftar Isi (vii)
8. Daftar Gambar (xi)
9. Daftar Tabel (xiii)

**BAGIAN ISI (Penomoran Angka Arab: 1, 2, 3, ...)**
10. BAB I - Pendahuluan (1)
11. BAB II - Tinjauan Pustaka (17)
12. BAB III - Metodologi Penelitian (44)
13. BAB IV - Hasil Penelitian dan Pembahasan (64)
    - Gabungkan 5 file BAB IV menjadi satu bab
    - Hapus header/footer redundant
14. BAB V - Penutup (166)

**BAGIAN AKHIR (Lanjutan Angka Arab)**
15. Daftar Pustaka (204)
16. Lampiran A: Mockup Screenshots (208)
17. Lampiran B: Code Samples (250)
18. Lampiran C: Testing Results (260)
19. Lampiran D: Project Management Docs (268)
20. Lampiran E: Surat Keterangan (275)
21. Daftar Riwayat Hidup (278)

#### 2.2 Tips Copy-Paste
- Copy per section (heading + content)
- Apply style setelah paste (Heading 1, Heading 2, Body Text)
- Check formatting consistency
- Replace **bold** dengan Bold, *italic* dengan Italic
- Convert markdown tables ke Word tables
- Convert bullet points ke Word bullets

---

### TAHAP 3: Insert Gambar dan Diagram

#### 3.1 Gambar yang Harus Dibuat/Dicari

**BAB I:**
- Gambar 1.1: Logo CUR-HEART → `/tugas-selesai/06_rintisan_bisnis_digital/logo-cur-heart.jpeg`
- Gambar 1.2: Statistik Kesehatan Mental → Buat di Excel/Canva dari data di teks
- Gambar 1.3: Perbandingan Manual vs Online → Buat infografis

**BAB II:**
- Gambar 2.1-2.10: Diagram teori → Cari dari buku/jurnal atau buat sendiri di draw.io
- Gunakan sumber yang kredibel, cantumkan "Sumber: [referensi]"

**BAB III:**
- Gambar 3.1: Flowchart Metodologi → Buat di draw.io/Lucidchart
- Gambar 3.2: Waterfall SDLC → Buat diagram custom untuk CUR-HEART
- Gambar 3.3: Gantt Chart → Buat di Excel atau MS Project, screenshot
- Gambar 3.4: Stakeholder Map → Buat di PowerPoint/draw.io

**BAB IV:**
- Gambar 4.1: Org Structure → Buat di PowerPoint
- Gambar 4.4: WBS → Buat di MindMap/Excel
- Gambar 4.5: Gantt Chart Project → Excel/MS Project
- Gambar 4.9: **ERD** → **PENTING! Buat di MySQL Workbench/draw.io**
- Gambar 4.11: **Use Case Diagram** → **Buat di draw.io/StarUML**
- Gambar 4.12-4.14: **Activity Diagrams** → **Buat di draw.io**
- Gambar 4.15: **Sequence Diagram** → **Buat di draw.io/PlantUML**
- Gambar 4.19: Monolithic vs Microservices → Diagram architecture
- Gambar 4.20: Laravel MVC Flow → Buat diagram custom

**LAMPIRAN A (41 Mockup Screenshots):**
- Screenshot seluruh mockup dari `/tugas-selesai/06_rintisan_bisnis_digital/mockups/`
- Buka setiap file HTML di browser
- Screenshot dengan resolution tinggi (min 1920x1080)
- Crop dengan rapi
- Compress jika file size terlalu besar (max 500KB per image)

#### 3.2 Format Insert Gambar
```
[Gambar centered, size 80-90% page width]

Gambar 4.9 Entity Relationship Diagram (ERD) CUR-HEART System
Sumber: Hasil Penelitian, 2024
```

#### 3.3 Tools untuk Membuat Diagram
- **ERD**: MySQL Workbench, draw.io, Lucidchart
- **UML**: draw.io, StarUML, Visual Paradigm, PlantUML
- **Flowchart**: draw.io, Lucidchart, Microsoft Visio
- **Gantt Chart**: Microsoft Project, Excel, GanttProject
- **Infografics**: Canva, Adobe Illustrator, PowerPoint

---

### TAHAP 4: Insert Tabel

#### 4.1 Convert Markdown Tables
Markdown table seperti ini:
```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
```

Convert ke Word Table:
1. Copy markdown table
2. Di Word: Insert → Table → Convert Text to Table
3. Atau manual: Insert → Table → specify rows/columns
4. Apply table style: Table Design → Table Styles (pilih professional style)
5. Add caption di atas tabel

#### 4.2 Table Formatting
- Border: Semua border visible
- Header row: Bold, background color (light gray/blue)
- Alternate row colors (optional, untuk readability)
- Text alignment: Left untuk text, Right untuk numbers
- Cell padding: 5-8 pt

---

### TAHAP 5: Penomoran Halaman

#### 5.1 Setup Section Breaks
1. Bagian Awal: Romawi kecil (i, ii, iii, ...)
2. Bagian Isi: Angka arab (1, 2, 3, ...)

**Cara:**
- Setelah Daftar Tabel (sebelum BAB I): Insert → Break → Section Break (Next Page)
- Insert → Page Numbers → Format Page Numbers
  - Bagian Awal: Number format: i, ii, iii
  - Bagian Isi: Number format: 1, 2, 3, start at 1

#### 5.2 Header/Footer
- Header: Kosong (atau logo UNM kecil di kanan atas - optional)
- Footer: Nomor halaman centered
- Different First Page: Checked (cover page tidak ada nomor)

---

### TAHAP 6: Daftar Isi, Gambar, Tabel (Auto-Generate)

#### 6.1 Table of Contents (Daftar Isi)
1. Pastikan semua heading sudah menggunakan Heading Styles
2. Place cursor di halaman Daftar Isi
3. References → Table of Contents → Custom Table of Contents
4. Settings:
   - Show levels: 3
   - Show page numbers: Yes
   - Right align page numbers: Yes
   - Tab leader: Dots
5. Klik OK

**Update setiap kali ada perubahan:**
- Klik pada Table of Contents
- Klik "Update Table"
- Pilih "Update entire table"

#### 6.2 List of Figures (Daftar Gambar)
1. Pastikan semua gambar sudah ada Caption (Insert Caption)
2. References → Insert Table of Figures
3. Caption label: Figure
4. Formats: From template
5. Klik OK

#### 6.3 List of Tables (Daftar Tabel)
1. Pastikan semua tabel sudah ada Caption
2. References → Insert Table of Figures
3. Caption label: Table
4. Klik OK

---

### TAHAP 7: Citations dan References

#### 7.1 Insert Citations
1. References → Manage Sources → New
2. Type of Source: Book/Journal Article/Website
3. Fill details sesuai Daftar Pustaka
4. Klik OK

**Untuk insert citation dalam teks:**
- Place cursor
- References → Insert Citation → pilih sumber
- Citation akan muncul: [1], [2], dst.

#### 7.2 Bibliography (Daftar Pustaka)
1. Place cursor di halaman Daftar Pustaka
2. References → Bibliography → Insert Bibliography
3. Style: IEEE (or APA jika diminta)

**Atau manual:**
- Copy dari file `07_DAFTAR_PUSTAKA.md`
- Format manually sesuai IEEE style

---

### TAHAP 8: Lampiran

#### 8.1 Lampiran A: Mockup Screenshots (41 Gambar)
Untuk setiap mockup:
```
LAMPIRAN A
MOCKUP DAN SCREENSHOT SISTEM

Gambar A.1 Landing Page (Homepage)

[Screenshot mockup 01_landing.html]

Deskripsi:
Halaman landing page adalah halaman utama yang pertama kali dilihat pengunjung. 
Berisi hero section dengan call-to-action, overview layanan, featured therapists, 
testimonials, dan footer dengan informasi kontak.

Fitur Utama:
- Hero banner dengan booking button
- Service cards (6 layanan)
- Therapist profiles preview
- Client testimonials slider
- FAQ section
- Newsletter subscription

---

Gambar A.2 About Us Page

[Screenshot mockup 02_about.html]

Deskripsi:
Halaman tentang CUR-HEART yang menjelaskan visi, misi, sejarah, dan tim. 
Memberikan informasi kredibilitas kepada calon klien.

... (lanjutkan untuk 41 mockup)
```

#### 8.2 Lampiran B: Code Samples
Include critical code snippets:
- Laravel Migration (create_bookings_table.php)
- Eloquent Model (Booking.php)
- Controller (BookingController.php)
- Blade Template (booking_step1.blade.php)
- Tailwind Config (tailwind.config.js)

**Format:**
```
LAMPIRAN B
CODE SAMPLES DAN TECHNICAL DOCUMENTATION

B.1 Laravel Migration - Create Bookings Table

[Code snippet dengan syntax highlighting]

Penjelasan:
Migration ini membuat tabel bookings dengan foreign key constraints ke tabel 
users, therapists, dan services. Tabel ini menyimpan informasi booking seperti 
tanggal, waktu, status, dan nomor booking yang unique.

...
```

#### 8.3 Lampiran C: Testing Results
Include:
- Unit test results table
- Feature test checklist
- UAT feedback summary
- Performance test metrics
- Security test report

#### 8.4 Lampiran D: Project Management Documents
Include:
- Project Charter (full document)
- Risk Register (complete with all 10 risks)
- Communication Plan Matrix
- RACI Matrix
- Meeting Minutes sample

#### 8.5 Lampiran E: Surat Keterangan
Include:
- Surat Keterangan Riset dari CUR-HEART
- Surat Keabsahan Data
- Surat Serah Terima Produk (jika sudah ada)

**Format surat:** Scan dengan resolution tinggi (300 DPI), format PDF atau JPEG

---

### TAHAP 9: Quality Check

#### 9.1 Content Review Checklist
- [ ] Semua BAB lengkap (I-V)
- [ ] Tidak ada placeholder text yang belum diisi
- [ ] Semua istilah konsisten (sistem/system, pengguna/user - pilih satu)
- [ ] Semua data kuantitatif konsisten (budget, timeline, ROI, dll.)
- [ ] Semua nama proper noun konsisten (CUR-HEART, Laravel, MySQL)
- [ ] Tidak ada typo atau kesalahan ejaan

#### 9.2 Format Review Checklist
- [ ] Semua heading menggunakan Heading Styles
- [ ] Font konsisten (Times New Roman 12pt)
- [ ] Margin sesuai (4-3-3-3 cm)
- [ ] Line spacing 1.5 untuk body text
- [ ] Alignment Justify untuk body text
- [ ] Penomoran halaman benar (romawi vs arab)

#### 9.3 Visual Review Checklist
- [ ] Semua gambar terinsert dengan caption
- [ ] Semua gambar resolution tinggi (tidak blur)
- [ ] Semua tabel terformat dengan rapi
- [ ] Semua tabel ada caption di atas
- [ ] Semua gambar/tabel direferensikan dalam teks
- [ ] Daftar Gambar dan Daftar Tabel akurat

#### 9.4 Reference Review Checklist
- [ ] Setiap claim ada citation
- [ ] Semua citation ada di Daftar Pustaka
- [ ] Tidak ada referensi "mati" (listed tapi tidak dikutip)
- [ ] Format IEEE style konsisten
- [ ] Minimal 15 referensi (target: 45 ✓)

#### 9.5 Lampiran Review Checklist
- [ ] Semua 41 mockup screenshot terinsert
- [ ] Code samples lengkap dan syntax highlighted
- [ ] Testing results terdokumentasi
- [ ] Surat-surat resmi terinclude

---

### TAHAP 10: Final Polish

#### 10.1 Proofreading
1. **Baca Ulang**: Baca seluruh dokumen dari awal hingga akhir
2. **Grammar Check**: Gunakan Grammarly atau LanguageTool
3. **Spell Check**: Word spell checker (F7)
4. **Peer Review**: Minta teman/team member untuk baca dan beri feedback

#### 10.2 Plagiarism Check
- Upload ke Turnitin (jika ada akses)
- Atau gunakan tools online (gratis dengan limitasi)
- Target: Similarity index <25%, exact matches <5%

#### 10.3 Print Preview
- File → Print → Print Preview
- Check:
  - Page breaks di tempat yang tepat (tidak memotong gambar/tabel)
  - Header/footer muncul dengan benar
  - Margin konsisten di semua halaman

#### 10.4 Generate PDF
1. File → Save As → PDF
2. Options:
   - Optimize for: Standard (publishing online and printing)
   - Include: Document properties, Document structure tags
3. Save dengan naming: `Laporan_Capstone_CURHEART_Tim_[NamaTim].pdf`

---

## 📊 ESTIMASI WAKTU PENGERJAAN

| Tahap | Durasi | PIC |
|-------|--------|-----|
| Setup Template Word | 1 jam | Susanto |
| Copy Content BAB I-III | 2 jam | Fahruroji |
| Copy Content BAB IV-V | 3 jam | Roki Anjas |
| Buat Diagram (ERD, UML, Flowchart) | 8 jam | Roki Anjas |
| Screenshot 41 Mockup | 3 jam | Susanto |
| Insert Gambar & Tabel | 4 jam | Fahruroji |
| Setup Penomoran & Daftar Isi | 1 jam | Susanto |
| Lampiran A (Mockups) | 2 jam | Susanto |
| Lampiran B-E (Docs) | 2 jam | Fahruroji |
| Quality Check & Proofreading | 3 jam | All |
| Final Polish & PDF | 1 jam | Roki Anjas |
| **TOTAL** | **30 jam** | **Team** |

**Rekomendasi:** Kerjakan dalam 3-5 hari kerja (6-10 jam per hari untuk team 3 orang)

---

## 🛠️ TOOLS YANG DIBUTUHKAN

### Software
- [ ] Microsoft Word 2016 atau lebih baru
- [ ] PDF Reader (Adobe Acrobat, Foxit)
- [ ] Image Editor (Photoshop, GIMP, Paint.NET) - untuk crop/resize screenshot
- [ ] Diagram Tools:
  - [ ] draw.io (free, online/desktop)
  - [ ] MySQL Workbench (untuk ERD)
  - [ ] Lucidchart (online, free tier)
- [ ] Browser (Chrome/Firefox) - untuk screenshot mockup HTML
- [ ] Screenshot Tool:
  - Windows: Snipping Tool, Win+Shift+S
  - Mac: Cmd+Shift+4
  - Extension: FireShot (full page screenshot)

### Optional Tools
- [ ] Grammarly (grammar check)
- [ ] Mendeley/Zotero (reference management)
- [ ] Turnitin (plagiarism check)
- [ ] Canva (infographics)

---

## 📁 BACKUP STRATEGY

### Backup Files
1. **Cloud Backup**: Upload ke Google Drive/OneDrive/Dropbox
2. **Version Control**: Save multiple versions
   - `Laporan_v1_draft.docx`
   - `Laporan_v2_review.docx`
   - `Laporan_v3_final.docx`
3. **Local Backup**: Copy ke external hard drive/USB

### Backup Schedule
- After setiap tahap major (after BAB completion)
- Before major edits
- Daily backup saat intensive editing

---

## 🎯 DELIVERABLES FINAL

### 1. Dokumen Laporan
**Format**: PDF + DOCX
**Naming**: 
- `Laporan_Capstone_CURHEART_Tim_[NamaTim]_Final.pdf`
- `Laporan_Capstone_CURHEART_Tim_[NamaTim]_Final.docx`

### 2. Hard Copy
- **Print**: Color (untuk cover, gambar), Hitam-Putih (untuk teks)
- **Binding**: Hard cover (jilid hard cover)
- **Cover**: Mengikuti template UNM
- **Jumlah**: 
  - 3 eksemplar untuk dosen pembimbing
  - 1 eksemplar untuk perpustakaan
  - 1 eksemplar untuk arsip pribadi

### 3. CD/DVD (Optional)
Berisi:
- Laporan PDF
- Laporan DOCX (editable)
- Slide presentasi PPT
- Video promosi
- Source code (jika diminta)
- Mockup HTML files

**Label CD**: Cetak label profesional dengan:
- Logo UNM
- Judul proyek
- Nama tim
- Tanggal

---

## ❓ FAQ & TROUBLESHOOTING

### Q: Bagaimana jika content melebihi 100 halaman?
**A:** Tidak masalah. Laporan capstone biasanya 80-120 halaman. Yang penting adalah **kualitas konten**, bukan hanya quantity. Pastikan tidak ada filler content.

### Q: Apakah semua 41 mockup harus dimasukkan?
**A:** Ya, masukkan semua ke Lampiran A. Ini menunjukkan completeness dari deliverable. Di BAB IV cukup highlight beberapa screenshot key features saja.

### Q: Diagram UML harus menggunakan tools apa?
**A:** Bebas, yang penting **standar UML** (notasi yang benar). Recommended: draw.io (gratis), StarUML, atau Visual Paradigm.

### Q: Apakah harus membuat prototype functional?
**A:** Tidak mandatory untuk laporan. Mockup HTML yang sudah ada sudah cukup sebagai "prototype". Jika ada waktu dan skill, buat Laravel functional prototype adalah nilai plus besar.

### Q: Format citation IEEE atau APA?
**A:** Dokumen ini menggunakan **IEEE**. Jika dosen meminta APA, tinggal adjust format saja (author-year vs numbering).

### Q: Bagaimana jika ada feedback revisi dari dosen?
**A:** 
1. Catat semua feedback
2. Buat revision log
3. Implement perubahan
4. Highlight perubahan (gunakan Track Changes di Word)
5. Submit revision dengan cover letter yang list perubahan

---

## 📞 SUPPORT & CONTACTS

### Jika Ada Pertanyaan:
- **Tim Internal**: Group chat team
- **Dosen Pembimbing**: Rani Irma Handayani, M.Kom (via email atau konsultasi schedule)
- **Prodi**: Ketua Prodi Sistem Informasi UNM

### Resources:
- Pedoman Capstone: `/rencana-tugas-mahasiswa/Proyek_Sistem_Informasi/pedoman_capstone/`
- Brief: `/rencana-tugas-mahasiswa/Proyek_Sistem_Informasi/BRIEF_MAKALAH_CAPSTONE_PROJECT_CURHEART.md`
- Mockups: `/tugas-selesai/06_rintisan_bisnis_digital/mockups/`

---

## ✅ PRE-SUBMISSION CHECKLIST

**1 Minggu Sebelum Deadline:**
- [ ] Semua BAB complete dan reviewed
- [ ] Semua gambar dan diagram inserted
- [ ] Semua tabel formatted
- [ ] Daftar Isi, Gambar, Tabel updated
- [ ] Referensi lengkap dan formatted

**3 Hari Sebelum Deadline:**
- [ ] Quality check complete
- [ ] Plagiarism check done (<25%)
- [ ] Peer review feedback implemented
- [ ] Print preview checked
- [ ] PDF generated

**1 Hari Sebelum Deadline:**
- [ ] Hard copy printed and bound
- [ ] CD/DVD prepared (if required)
- [ ] Backup files uploaded to cloud
- [ ] Presentasi slide ready
- [ ] Video promosi uploaded

**Hari H Submission:**
- [ ] Submit soft copy (PDF) via email/LMS
- [ ] Submit hard copy ke dosen
- [ ] Confirm receipt

---

## 🎉 GOOD LUCK!

Laporan yang baik adalah hasil dari:
1. **Konten berkualitas** (research yang mendalam)
2. **Format profesional** (consistency dan readability)
3. **Dokumentasi lengkap** (gambar, tabel, lampiran)
4. **Attention to detail** (typo-free, reference complete)

**Remember:**
> "Quality is not an act, it is a habit." - Aristotle

Semangat finalisasi laporan! 💪📚✨

---

**Prepared by**: Tim Proyek CUR-HEART  
**Version**: 1.0  
**Date**: November 2024  
**For**: Capstone Project - Proyek Sistem Informasi UNM
