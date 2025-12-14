# PETUNJUK CONVERT PLANTUML KE GAMBAR

## 📁 File PlantUML yang Tersedia:

### Gambar 1: Framework Tata Kelola TI
- **File:** `gambar_1_framework.puml`
- **Tipe:** Component Diagram
- **Deskripsi:** Framework 5 komponen dengan 4 domain COBIT 2019

### Gambar 2: Roadmap Implementasi (2 Varian)
- **File:** `gambar_2a_roadmap_gantt.puml` - Gantt Chart (Timeline detail)
- **File:** `gambar_2b_roadmap_timeline.puml` - Timeline sederhana (Fase & deliverables)
- **Tipe:** Gantt Chart / Timeline Diagram
- **Deskripsi:** Roadmap 4 fase implementasi 18-24 bulan

### Gambar 3: Governance & RACI (3 Varian)
- **File:** `gambar_3a_struktur_governance.puml` - Organizational Structure
- **File:** `gambar_3b_raci_matrix.puml` - RACI Matrix Table
- **File:** `gambar_3c_escalation_path.puml` - Escalation Path
- **Tipe:** Organization Chart, Table, Flow Diagram
- **Deskripsi:** Struktur governance 3-tier dengan RACI matrix

---

## 🌐 CARA CONVERT ONLINE (Paling Mudah)

### Metode 1: PlantUML Official Server

1. Buka: **https://www.plantuml.com/plantuml/uml/**
2. Copy isi file `.puml` (buka di text editor/VS Code)
3. Paste di text area website
4. Klik **"Submit"**
5. Diagram akan muncul
6. Klik kanan → **"Save image as..."** → Pilih **PNG**

**Rekomendasi:** Export sebagai PNG untuk kualitas terbaik di Word/PDF

---

### Metode 2: PlantUML Editor (Real-time Preview)

1. Buka: **https://plantuml-editor.kkeisuke.com/**
2. Paste kode di **panel kiri**
3. Preview otomatis di **panel kanan**
4. Klik **"PNG"** atau **"SVG"** untuk download
5. Pilih **PNG** untuk dokumen, **SVG** untuk presentasi

---

### Metode 3: PlantText (Simple & Fast)

1. Buka: **https://www.planttext.com/**
2. Paste kode PlantUML
3. Klik **"Refresh"**
4. Klik **"Download"** (PNG format)

---

## 💻 CARA CONVERT OFFLINE (VS Code)

### Persiapan:

1. **Install Java** (required):
   - Download: https://www.java.com/download/
   - Install dan restart komputer

2. **Install Extension PlantUML di VS Code:**
   - Buka VS Code
   - Tekan `Ctrl+Shift+X`
   - Search: **"PlantUML"**
   - Install extension by **jebbs**

### Cara Generate Gambar:

1. Buka file `.puml` di VS Code
2. Tekan `Alt+D` untuk **preview**
3. Untuk export:
   - **Cara 1:** Right-click pada preview → **"Export Current Diagram"**
   - **Cara 2:** Tekan `Ctrl+Shift+P` → ketik **"PlantUML: Export"**
4. Pilih format:
   - **PNG** (Recommended untuk Word/PDF)
   - **SVG** (Untuk presentasi PowerPoint)
   - **PDF** (Langsung print-ready)
5. Pilih lokasi save

---

## 🎨 TIPS KUSTOMISASI

### 1. Mengubah Warna

```plantuml
!define WARNA_BIRU #3498DB
!define WARNA_HIJAU #2ECC71
rectangle "Text" as NAMA WARNA_BIRU
```

### 2. Mengubah Font

```plantuml
skinparam defaultFontName "Times New Roman"
skinparam defaultFontSize 14
skinparam defaultFontStyle bold
```

### 3. Mengubah Background

```plantuml
skinparam backgroundColor #F5F5F5
```

### 4. Menambahkan Watermark/Footer

```plantuml
footer Sumber: Hasil Penelitian, 2025
```

### 5. Resolusi Tinggi (untuk Print)

Di PlantUML Online, setelah generate:
- Pilih **"PNG"** di dropdown
- Untuk print berkualitas tinggi, gunakan **300 DPI**

---

## 📝 REKOMENDASI UNTUK DOKUMEN TUGAS AKHIR

### Format Gambar yang Disarankan:

| Kegunaan | Format | Keterangan |
|----------|--------|------------|
| **Dokumen Word** | PNG (300 DPI) | Kualitas terbaik untuk print |
| **Presentasi PPT** | SVG atau PNG | SVG bisa di-zoom tanpa blur |
| **PDF Langsung** | PDF | Siap print, no loss quality |
| **Website/Online** | SVG | Scalable, ukuran file kecil |

### Setting Insert ke Word:

1. **Insert gambar:**
   - Insert → Pictures → pilih file PNG
   
2. **Ukuran optimal:**
   - Width: 14-16 cm (fit to page margin)
   - Maintain aspect ratio (jangan distort)

3. **Caption:**
   - Insert → Caption
   - Format: "Gambar 1. Nama Gambar"
   - Position: Below selected item

4. **Kualitas print:**
   - Right-click gambar → Format Picture
   - Size → Lock aspect ratio ✓
   - Resolution: High quality (300 DPI)

---

## 🚀 QUICK START (Copy-Paste Ready)

### Untuk convert semua gambar sekaligus:

1. Buka: https://www.plantuml.com/plantuml/uml/
2. Copy-paste file `.puml` satu per satu
3. Download semua sebagai PNG
4. Rename file sesuai nomor gambar:
   - `Gambar_1_Framework.png`
   - `Gambar_2_Roadmap.png`
   - `Gambar_3_Governance.png`

---

## 📦 PILIH VARIAN YANG PALING SESUAI

### Untuk Gambar 2 (Roadmap):
- **Gunakan `gambar_2a_roadmap_gantt.puml`** jika ingin timeline detail dengan bar progress
- **Gunakan `gambar_2b_roadmap_timeline.puml`** jika ingin tampilan lebih sederhana dengan focus pada deliverables

### Untuk Gambar 3 (Governance):
- **Gunakan `gambar_3a_struktur_governance.puml`** untuk menampilkan organizational chart
- **Gunakan `gambar_3b_raci_matrix.puml`** untuk menampilkan tabel RACI yang detail
- **Gunakan `gambar_3c_escalation_path.puml`** untuk menampilkan alur eskalasi insiden

**Rekomendasi:** Pilih 1 varian terbaik untuk setiap gambar agar dokumen tidak terlalu banyak diagram.

---

## ❓ TROUBLESHOOTING

### Error: "Java not found"
- Install Java: https://www.java.com/download/
- Restart VS Code setelah install

### Error: "Cannot render diagram"
- Pastikan syntax PlantUML benar (tidak ada typo)
- Cek di online editor dulu untuk validasi

### Gambar pecah/blur di Word:
- Export dengan resolusi lebih tinggi (PNG 300+ DPI)
- Atau gunakan format SVG (scalable vector)

### File terlalu besar:
- Kompres PNG: https://tinypng.com/
- Atau gunakan SVG (ukuran lebih kecil)

---

## 📞 LINK BANTUAN

- **PlantUML Docs:** https://plantuml.com/
- **Syntax Guide:** https://plantuml.com/guide
- **Color List:** https://plantuml.com/color
- **Icon List:** https://plantuml.com/sprite

---

**Selamat mengerjakan! Semoga sukses dengan tugas akhirnya! 🎓✨**
