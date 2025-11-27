# Desain Sistem CRM CUR-HEART

Folder ini berisi semua desain sistem CRM CUR-HEART dalam bentuk diagram dan database.

## 📁 Struktur Folder

### `/diagram` - Diagram PlantUML
Berisi semua diagram sistem dalam format PlantUML (.puml):

1. **diagram_konteks.puml** - Diagram konteks sistem
2. **dfd_level_0.puml** - Data Flow Diagram Level 0
3. **use_case.puml** - Use Case Diagram
4. **flowchart_booking.puml** - Flowchart proses booking
5. **flowchart_dokumentasi.puml** - Flowchart proses dokumentasi sesi
6. **erd.puml** - Entity Relationship Diagram

### `/database` - Database Schema
Berisi schema database dalam format SQL:

1. **erd_crm_curheart.sql** - ERD dan CREATE TABLE statements lengkap

## 🔧 Cara Generate Diagram

### Menggunakan PlantUML

**Online:**
1. Buka http://www.plantuml.com/plantuml/uml/
2. Copy-paste isi file .puml
3. Generate dan download gambar

**VS Code Extension:**
1. Install extension "PlantUML" by jebbs
2. Buka file .puml
3. Tekan `Alt+D` untuk preview
4. Klik kanan → Export Current Diagram

**Command Line:**
```bash
# Install PlantUML
npm install -g node-plantuml

# Generate PNG
puml generate diagram_konteks.puml -o output.png

# Generate semua diagram
puml generate *.puml
```

## 📊 Daftar Diagram

| No | Nama Diagram | File | Deskripsi |
|----|--------------|------|-----------|
| 1 | Diagram Konteks | diagram_konteks.puml | Sistem dan entitas eksternal |
| 2 | DFD Level 0 | dfd_level_0.puml | Proses utama dan aliran data |
| 3 | Use Case | use_case.puml | Interaksi aktor dengan sistem |
| 4 | Flowchart Booking | flowchart_booking.puml | Alur proses booking |
| 5 | Flowchart Dokumentasi | flowchart_dokumentasi.puml | Alur dokumentasi sesi |
| 6 | ERD | erd.puml | Struktur database |

## 💾 Database

**File:** `database/erd_crm_curheart.sql`

**Tabel:**
1. users - Data pengguna sistem
2. clients - Profil klien
3. therapists - Profil terapis
4. bookings - Data reservasi
5. sessions - Data sesi terapi
6. session_notes - Catatan SOAP
7. messages - Komunikasi
8. reviews - Ulasan & rating
9. notifications - Notifikasi

**Cara Import:**
```sql
mysql -u username -p database_name < erd_crm_curheart.sql
```

## 📝 Catatan

- Semua diagram menggunakan PlantUML untuk kemudahan maintenance
- Database schema sudah include indexes untuk optimasi
- Foreign keys sudah dikonfigurasi dengan CASCADE
- Diagram dapat di-export ke PNG, SVG, atau PDF

## 🔗 Referensi

- PlantUML: https://plantuml.com/
- PlantUML Guide: https://plantuml.com/guide
- MySQL Documentation: https://dev.mysql.com/doc/
