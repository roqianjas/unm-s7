# Cara Generate Diagram dari PlantUML

## 🎯 Quick Start

Semua diagram sudah dibuat dalam format PlantUML (.puml). Anda perlu generate menjadi gambar PNG untuk dimasukkan ke laporan.

## 📋 Daftar File Diagram

1. `diagram_konteks.puml` → `diagram_konteks.png`
2. `dfd_level_0.puml` → `dfd_level_0.png`
3. `use_case.puml` → `use_case.png`
4. `flowchart_booking.puml` → `flowchart_booking.png`
5. `flowchart_dokumentasi.puml` → `flowchart_dokumentasi.png`
6. `erd.puml` → `erd.png`

## 🌐 Cara 1: Online (Paling Mudah)

### Menggunakan PlantUML Online Editor

1. Buka: http://www.plantuml.com/plantuml/uml/
2. Copy isi file `.puml` (misalnya `diagram_konteks.puml`)
3. Paste ke editor online
4. Diagram akan otomatis ter-generate
5. Klik kanan pada diagram → Save Image As → Simpan sebagai PNG

**Ulangi untuk semua 6 file diagram**

## 💻 Cara 2: VS Code Extension

### Install Extension

1. Buka VS Code
2. Tekan `Ctrl+Shift+X` (Extensions)
3. Cari "PlantUML" by jebbs
4. Install extension

### Generate Diagram

1. Buka file `.puml` di VS Code
2. Tekan `Alt+D` untuk preview
3. Klik kanan pada preview → Export Current Diagram
4. Pilih format PNG
5. Simpan di folder yang sama

**Atau generate semua sekaligus:**
- Klik kanan di folder `diagram`
- Pilih "PlantUML: Export Workspace Diagrams"

## 🖥️ Cara 3: Command Line

### Install PlantUML

**Windows (dengan Chocolatey):**
```cmd
choco install plantuml
```

**Atau download manual:**
1. Download PlantUML JAR: https://plantuml.com/download
2. Install Java JRE jika belum ada
3. Simpan `plantuml.jar` di folder ini

### Generate Diagram

**Generate satu file:**
```cmd
java -jar plantuml.jar diagram_konteks.puml
```

**Generate semua file:**
```cmd
java -jar plantuml.jar *.puml
```

**Generate dengan format spesifik:**
```cmd
java -jar plantuml.jar -tpng *.puml
```

## 📱 Cara 4: Online Tools Lain

### PlantText
1. Buka: https://www.planttext.com/
2. Paste kode PlantUML
3. Klik "Refresh"
4. Download gambar

### Kroki
1. Buka: https://kroki.io/
2. Pilih PlantUML
3. Paste kode
4. Download PNG

## ✅ Setelah Generate

Setelah semua diagram di-generate menjadi PNG:

1. Pastikan nama file sesuai:
   - `diagram_konteks.png`
   - `dfd_level_0.png`
   - `use_case.png`
   - `flowchart_booking.png`
   - `flowchart_dokumentasi.png`
   - `erd.png`

2. Simpan semua PNG di folder `02_desain/diagram/`

3. Diagram akan otomatis muncul di laporan karena sudah ada referensi:
   - Gambar 4.1: Diagram Konteks
   - Gambar 4.2: DFD Level 0
   - Gambar 4.3: Use Case Diagram
   - Gambar 4.4: Flowchart Booking
   - Gambar 4.5: Flowchart Dokumentasi
   - Gambar 4.6: ERD

## 🎨 Tips

- **Resolusi**: Generate dengan resolusi tinggi untuk presentasi
- **Format**: PNG recommended untuk dokumen Word/PDF
- **Size**: Jika terlalu besar, bisa resize di Word/PowerPoint
- **Quality**: PlantUML menghasilkan diagram yang clean dan professional

## ❓ Troubleshooting

**Error: Java not found**
- Install Java JRE: https://www.java.com/download/

**Diagram tidak muncul**
- Cek syntax PlantUML
- Pastikan ada `@startuml` dan `@enduml`

**Ingin edit diagram**
- Edit file `.puml`
- Generate ulang menjadi PNG

## 📞 Bantuan

Jika ada masalah, cek dokumentasi PlantUML:
- https://plantuml.com/
- https://plantuml.com/guide
