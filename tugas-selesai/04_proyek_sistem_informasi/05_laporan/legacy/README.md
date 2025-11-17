# 05 - LAPORAN

Folder ini berisi semua file laporan Capstone Project CUR-HEART, mulai dari draft awal hingga versi final. Folder `laporan/` yang sudah ada berisi semua konten BAB I-V lengkap dengan lampiran.

---

## 📁 Struktur Folder

```
05_laporan/
├── README.md                                  # File ini
├── drafts/                                    # Folder draft versions (opsional)
│   ├── draft_v1_2024-09-20.md
│   ├── draft_v2_2024-10-05.md
│   └── draft_v3_2024-10-25.md
└── final/                                     # Folder final versions
    ├── LAPORAN_CAPSTONE_CURHEART_FINAL.docx   # Final Word (untuk editing)
    ├── LAPORAN_CAPSTONE_CURHEART_FINAL.pdf    # Final PDF (untuk submit)
    └── README_FINAL.txt                       # Catatan versi final
```

**Note**: Konten laporan lengkap (BAB I-V + Lampiran) sudah tersedia di folder:  
`/var/www/unm-s7/tugas-selesai/04_proyek_sistem_informasi_curheart/laporan/`

---

## 📄 Konten Laporan yang Sudah Tersedia

### Di Folder `../laporan/` (14 files):

**Dokumen Utama**:
- `00_README.md` - Panduan navigasi laporan
- `00_DAFTAR_ISI.md` - Table of Contents lengkap
- `00_RINGKASAN_LAPORAN.md` - Executive Summary

**BAB I - Pendahuluan** (1 file):
- `01_BAB_I_PENDAHULUAN.md` - Latar belakang, rumusan masalah, tujuan, manfaat, batasan, metodologi

**BAB II - Tinjauan Pustaka** (1 file):
- `02_BAB_II_TINJAUAN_PUSTAKA.md` - Landasan teori (10 konsep), penelitian terdahulu (8 penelitian)

**BAB III - Metode Penelitian** (1 file):
- `03_BAB_III_METODE_PENELITIAN.md` - Metodologi SDLC Waterfall, teknik pengumpulan data, analisis data

**BAB IV - Hasil Penelitian** (5 files):
- `04_BAB_IV_BAGIAN_1_Inisiasi_Perencanaan.md` - Project charter, WBS, Gantt chart, RAB
- `04_BAB_IV_BAGIAN_2_Database_Design.md` - ERD, normalisasi, dokumentasi 16 tabel
- `04_BAB_IV_BAGIAN_3_Deskripsi_Produk.md` - Use case, activity, sequence, class diagram, arsitektur sistem
- `04_BAB_IV_BAGIAN_4_Testing.md` - Unit test, integration test, feature test, UAT report
- `04_BAB_IV_BAGIAN_5_Deployment_Handover.md` - Deployment process, training, handover documentation

**BAB V - Penutup** (1 file):
- `05_BAB_V_PENUTUP.md` - Kesimpulan (5 poin), saran (6 poin), kontribusi penelitian

**Lampiran** (4 files):
- `08_LAMPIRAN_A_Bukti_Keabsahan_Data.md` - Dokumentasi pengumpulan data, validasi stakeholder, bukti produk
- `08_LAMPIRAN_B_Bukti_Serah_Terima.md` - Berita acara, surat penerimaan, pengalihan hak cipta, warranty
- `09_DAFTAR_RIWAYAT_HIDUP.md` - CV lengkap 3 anggota tim
- `10_TEMPLATE_SURAT_KETERANGAN_RISET.md` - Template surat dari CUR-HEART

**Daftar Pustaka** (1 file):
- `07_DAFTAR_PUSTAKA.md` - 30+ referensi (buku, jurnal, artikel)

---

## 📊 Statistik Laporan

**Total Konten**:
- ✅ **14 files Markdown** (BAB I-V + Lampiran)
- ✅ **~75,000 words** total konten
- ✅ **Estimasi: 150-200 halaman** (format DOCX/PDF)
- ✅ **30+ referensi** (buku, jurnal, artikel)
- ✅ **50+ gambar** (diagram, screenshot, flowchart)
- ✅ **40+ tabel** (data, spesifikasi, hasil testing)

**Breakdown per BAB**:

| BAB | File | Words | Halaman | Status |
|-----|------|-------|---------|--------|
| BAB I | 1 file | ~6,000 | 12-15 | ✅ Complete |
| BAB II | 1 file | ~8,000 | 16-20 | ✅ Complete |
| BAB III | 1 file | ~5,000 | 10-12 | ✅ Complete |
| BAB IV | 5 files | ~40,000 | 80-100 | ✅ Complete |
| BAB V | 1 file | ~3,000 | 6-8 | ✅ Complete |
| Lampiran | 4 files | ~13,000 | 26-30 | ✅ Complete |
| **TOTAL** | **14 files** | **~75,000** | **150-185** | ✅ |

---

## 🔄 Proses Konversi ke Word/PDF

### Langkah-langkah Konversi:

**Opsi 1: Manual (Recommended for Best Formatting)**

1. **Buka setiap file Markdown di VS Code**
2. **Copy konten per BAB ke Microsoft Word**
3. **Apply formatting**:
   - Heading 1: BAB I, BAB II, dst (18pt, Bold, Poppins)
   - Heading 2: 4.1, 4.2, dst (16pt, Bold)
   - Heading 3: 4.1.1, 4.1.2, dst (14pt, Semi-Bold)
   - Body text: 12pt, Inter/Times New Roman, Justify
   - Line spacing: 1.5
   - Margin: 4cm (top), 3cm (left), 3cm (right), 3cm (bottom)
4. **Insert images** (diagram, screenshot) dari folder `03_desain/`
5. **Insert tables** dengan format konsisten
6. **Add page numbers** (bottom center, Roman numerals untuk awal, Arabic untuk konten)
7. **Add header/footer** dengan judul BAB
8. **Generate Table of Contents** (auto-generate di Word)
9. **Add cover page** dengan template UNM
10. **Proofread & spell check**
11. **Save as DOCX** → `LAPORAN_CAPSTONE_CURHEART_FINAL.docx`
12. **Export to PDF** → `LAPORAN_CAPSTONE_CURHEART_FINAL.pdf`

**Opsi 2: Pandoc (Automated, tapi butuh adjustment)**

```bash
# Install Pandoc (jika belum)
sudo apt install pandoc

# Gabungkan semua file MD
cat laporan/*.md > LAPORAN_LENGKAP.md

# Konversi ke DOCX
pandoc LAPORAN_LENGKAP.md -o LAPORAN_CAPSTONE_CURHEART_FINAL.docx \
  --reference-doc=template_UNM.docx \
  --toc --toc-depth=3 \
  --number-sections

# Konversi ke PDF (butuh LaTeX)
pandoc LAPORAN_LENGKAP.md -o LAPORAN_CAPSTONE_CURHEART_FINAL.pdf \
  --toc --toc-depth=3 \
  --number-sections \
  --pdf-engine=xelatex
```

**Opsi 3: Online Converter**
- Upload file `.md` ke https://word2md.com/ (reverse: MD to DOCX)
- Atau gunakan https://cloudconvert.com/md-to-docx

---

## 📐 Format Laporan (Standar UNM)

### Cover Page:
```
LOGO UNM (centered)

LAPORAN CAPSTONE PROJECT
SISTEM INFORMASI MANAJEMEN BOOKING DAN LAYANAN
TERAPI HYPNOTHERAPY BERBASIS WEB
(STUDI KASUS: CUR-HEART)

Disusun untuk Memenuhi Tugas Akhir Mata Kuliah:
- Manajemen Hubungan Pelanggan
- Proses Bisnis TI
- IT Governance
- Proyek Sistem Informasi
- Business Intelligence
- Rintisan Bisnis Digital

Oleh:
ROKI ANJAS (11250066)
SUSANTO (11250068)
FAHRUROJI (11250085)

PROGRAM STUDI SISTEM INFORMASI
FAKULTAS TEKNIK
UNIVERSITAS NEGERI MAKASSAR
2024
```

### Halaman Pengesahan:
```
HALAMAN PENGESAHAN

Laporan Capstone Project ini telah disetujui dan disahkan pada:
Hari/Tanggal: Jumat, 1 November 2024
Tempat: Fakultas Teknik UNM

Mengetahui,

Dosen Pembimbing                    Ketua Program Studi


(__________________)                  (__________________)
NIP. ____________                     NIP. ____________

Makassar, 1 November 2024
Kelompok Mahasiswa,

Roki Anjas          Susanto          Fahruroji
(11250066)          (11250068)       (11250085)
```

### Kata Pengantar:
```
KATA PENGANTAR

Puji syukur kami panjatkan kepada Tuhan Yang Maha Esa...
(~300-400 kata)

Makassar, 1 November 2024

Tim Proyek CUR-HEART
```

### Abstrak (ID + EN):
```
ABSTRAK

Latar Belakang: CUR-HEART adalah...
(~250-300 kata)

Kata Kunci: Sistem Informasi, Hypnotherapy, Laravel, Booking System, CRM

---

ABSTRACT

Background: CUR-HEART is...
(~250-300 words)

Keywords: Information System, Hypnotherapy, Laravel, Booking System, CRM
```

### Daftar Isi (Auto-generated):
```
DAFTAR ISI

HALAMAN JUDUL ...................................... i
HALAMAN PENGESAHAN ................................. ii
KATA PENGANTAR ..................................... iii
ABSTRAK ............................................ iv
ABSTRACT ........................................... v
DAFTAR ISI ......................................... vi
DAFTAR TABEL ....................................... ix
DAFTAR GAMBAR ...................................... x

BAB I PENDAHULUAN .................................. 1
1.1 Latar Belakang ................................. 1
1.2 Rumusan Masalah ................................ 3
...

BAB V PENUTUP ...................................... 145
5.1 Kesimpulan ..................................... 145
5.2 Saran .......................................... 147

DAFTAR PUSTAKA ..................................... 149
LAMPIRAN ........................................... 152
```

### Formatting Guidelines:

**Font**:
- Heading: Poppins (Bold, Semi-Bold)
- Body: Times New Roman atau Inter (Regular)
- Code/Technical: Courier New atau Consolas

**Size**:
- Title (Cover): 18pt, Bold
- BAB: 16pt, Bold, UPPERCASE
- Heading 2: 14pt, Bold
- Heading 3: 13pt, Semi-Bold
- Body: 12pt, Regular

**Spacing**:
- Line spacing: 1.5
- Paragraph spacing: 6pt before, 6pt after
- Indent first line: 1.27 cm (0.5 inch)

**Margin** (A4 Paper):
- Top: 4 cm
- Left: 4 cm
- Right: 3 cm
- Bottom: 3 cm

**Page Numbers**:
- Cover - Pengesahan: No page number
- Kata Pengantar - Daftar Gambar: Roman numerals (i, ii, iii, ...)
- BAB I - Lampiran: Arabic numerals (1, 2, 3, ...)

**Alignment**:
- Body text: Justify (rata kanan-kiri)
- Headings: Left align
- Tables/Figures: Center align

---

## 🖼️ Manajemen Gambar & Tabel

### Daftar Gambar (50+ gambar):

**BAB IV**:
- Gambar 4.1: Project Charter CUR-HEART
- Gambar 4.2: Work Breakdown Structure (WBS)
- Gambar 4.3: Gantt Chart Proyek
- Gambar 4.4: Entity Relationship Diagram (ERD)
- Gambar 4.5: Normalisasi Database (3NF)
- Gambar 4.6: Use Case Diagram (38 use cases)
- Gambar 4.7: Activity Diagram - Booking Process
- Gambar 4.8: Sequence Diagram - Login
- Gambar 4.9: Class Diagram (16 classes)
- Gambar 4.10: Arsitektur Sistem (MVC)
- Gambar 4.11-4.51: Screenshot UI/UX (41 mockup)
- Gambar 4.52: Unit Test Result
- Gambar 4.53: Feature Test Report
- Gambar 4.54: UAT Result Dashboard

**Lampiran**:
- Gambar A.1-A.18: Dokumentasi Wawancara, Observasi, Survey
- Gambar B.1-B.18: Foto Serah Terima & Training

**Caption Format**:
```
Gambar 4.1: Work Breakdown Structure Proyek CUR-HEART
(Sumber: Dokumentasi Tim, 2024)
```

### Daftar Tabel (40+ tabel):

**BAB IV**:
- Tabel 4.1: Rincian Biaya Proyek (RAB)
- Tabel 4.2: Jadwal Detail Proyek
- Tabel 4.3: Risk Register
- Tabel 4.4: Spesifikasi Tabel Database (16 tabel)
- Tabel 4.5: Requirement Specification (40 FR + 15 NFR)
- Tabel 4.6: User Stories (85 stories)
- Tabel 4.7: Unit Test Coverage
- Tabel 4.8: Feature Test Result (40 features)
- Tabel 4.9: UAT Scenarios (30 scenarios)
- Tabel 4.10: UAT Result Summary

**Caption Format**:
```
Tabel 4.1: Rincian Biaya Proyek CUR-HEART
(Sumber: Data Primer, 2024)
```

---

## ✅ Checklist Kelengkapan Laporan

### Bagian Awal:
- [ ] Cover page (dengan logo UNM)
- [ ] Halaman pengesahan (dengan tanda tangan)
- [ ] Kata pengantar (~400 kata)
- [ ] Abstrak Bahasa Indonesia (~300 kata)
- [ ] Abstract Bahasa Inggris (~300 kata)
- [ ] Daftar Isi (auto-generated)
- [ ] Daftar Tabel (auto-generated)
- [ ] Daftar Gambar (auto-generated)
- [ ] Daftar Lampiran

### BAB I-V:
- [x] BAB I: Pendahuluan (complete)
- [x] BAB II: Tinjauan Pustaka (complete)
- [x] BAB III: Metode Penelitian (complete)
- [x] BAB IV: Hasil Penelitian (5 bagian, complete)
- [x] BAB V: Penutup (complete)

### Bagian Akhir:
- [x] Daftar Pustaka (30+ referensi, APA Style)
- [x] Lampiran A: Bukti Keabsahan Data
- [x] Lampiran B: Bukti Serah Terima
- [x] Lampiran C: Daftar Riwayat Hidup (3 CV)
- [x] Lampiran D: Surat Keterangan Riset

### Format & Quality:
- [ ] Consistent formatting (font, size, spacing)
- [ ] All images high-resolution (min 300 dpi)
- [ ] All tables properly formatted
- [ ] Page numbers correct
- [ ] Table of Contents accurate
- [ ] No spelling/grammar errors
- [ ] Citations formatted correctly (APA Style)
- [ ] File size optimized (<20 MB for PDF)

---

## 📤 Deliverables Final

### File yang Harus Disubmit:

1. **LAPORAN_CAPSTONE_CURHEART_FINAL.docx**
   - Format: Microsoft Word (.docx)
   - Size: ~5-10 MB
   - Untuk: Editing & revisi jika diperlukan

2. **LAPORAN_CAPSTONE_CURHEART_FINAL.pdf**
   - Format: PDF/A (archival quality)
   - Size: ~15-20 MB
   - Untuk: Submit final & arsip

3. **LAPORAN_CAPSTONE_CURHEART_SUMMARY.pdf** (Optional)
   - Format: PDF
   - Size: ~3-5 MB
   - Konten: Executive summary + key findings (10-15 halaman)

### Backup Files:

4. **All Markdown files** (source)
   - Location: `../laporan/*.md`
   - For: Version control & future editing

5. **All images** (separate folder)
   - Location: `../03_desain/`
   - For: Reuse in presentations or publications

---

## 🔗 Integrasi dengan Folder Lain

**Referensi ke Folder Lain**:

- **01_dokumen_pendukung/** → Referensi untuk BAB II (Tinjauan Pustaka)
- **02_analisis/** → Data untuk BAB IV (Hasil Analisis)
- **03_desain/** → Gambar untuk BAB IV (Diagram, Mockup)
- **04_perencanaan/** → Tabel untuk BAB IV (WBS, Gantt, RAB)
- **05_laporan/** → **[FOLDER INI]** - Laporan final
- **06_presentasi/** → Slides untuk presentasi final
- **07_deliverables/** → Video promosi, X-banner, artikel
- **08_prototype/** → Link ke sistem live

---

## 🛠️ Tools yang Digunakan

**Authoring**:
- Microsoft Word (laporan final)
- VS Code (Markdown authoring)
- Grammarly (grammar check)
- Hemingway Editor (readability)

**Conversion**:
- Pandoc (MD to DOCX/PDF)
- CloudConvert (online converter)
- Adobe Acrobat (PDF editing)

**Quality Check**:
- Turnitin (plagiarism check)
- Grammarly Premium (advanced grammar)
- Mendeley (citation management)

**Formatting**:
- Zotero (bibliography management)
- Table Generator (online table formatter)
- Draw.io (diagram export)

---

## 📝 Tips Penulisan Laporan

### Do's:
✅ Gunakan bahasa formal & akademis  
✅ Konsisten dalam terminology (e.g., "Sistem Informasi" bukan "SI" di tengah paragraf)  
✅ Setiap tabel & gambar harus dirujuk dalam teks  
✅ Citation untuk setiap claim yang bukan original  
✅ Gunakan active voice (e.g., "Tim mengembangkan..." bukan "Dikembangkan oleh tim...")  
✅ Proofread minimal 3 kali sebelum submit  

### Don'ts:
❌ Jangan gunakan bahasa informal (e.g., "kita", "kami", "saya")  
❌ Jangan copy-paste dari internet tanpa citation  
❌ Jangan gunakan gambar low-resolution  
❌ Jangan inkonsisten formatting (font, spacing, dll)  
❌ Jangan lupa page number & header/footer  
❌ Jangan submit tanpa final proofreading  

---

## 📊 Timeline Finalisasi Laporan

**Week 1 (Minggu ke-10)**:
- [ ] Review all BAB content
- [ ] Insert all images & tables
- [ ] Format consistency check

**Week 2 (Minggu ke-11)**:
- [ ] Convert MD to DOCX
- [ ] Apply UNM template
- [ ] Add cover, pengesahan, kata pengantar, abstrak

**Week 3 (Minggu ke-12)**:
- [ ] Generate Table of Contents
- [ ] Add page numbers & headers
- [ ] Proofread & grammar check

**Week 4 (Minggu ke-13)**:
- [ ] Final review with advisor
- [ ] Revisions (if needed)
- [ ] Export to PDF
- [ ] **SUBMIT FINAL REPORT** 🎉

---

**Last Updated**: 1 November 2024  
**Status**: Konten BAB I-V & Lampiran ✅ Complete, Ready for formatting  
**Prepared by**: Tim Proyek CUR-HEART (Roki Anjas, Susanto, Fahruroji)
