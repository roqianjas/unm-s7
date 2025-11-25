# LAMPIRAN

## Lampiran A: Screenshot Sistem CRM CUR-HEART

### A.1 Manajemen Profil Klien

**Screenshot 1: Halaman Profil Klien - Client Dashboard**

Halaman ini menampilkan profil lengkap klien termasuk data demografis, preferensi, dan riwayat interaksi. Klien dapat mengedit informasi mereka sendiri untuk memastikan data selalu up-to-date.

*[Referensi: Mockup halaman 27_client_settings.jpg dari desain sistem]*

---

**Screenshot 2: Halaman Detail Klien - Therapist Dashboard**

Terapis dapat melihat profil lengkap klien termasuk riwayat medis, catatan sesi sebelumnya, dan kemajuan terapi untuk memberikan layanan yang dipersonalisasi.

*[Referensi: Mockup halaman 33_client_profile_view.jpg dari desain sistem]*

---

### A.2 Dokumentasi Sesi Terapi

**Screenshot 3: Formulir Dokumentasi Sesi - Therapist Dashboard**

Formulir terstruktur untuk terapis mendokumentasikan setiap sesi terapi, termasuk teknik yang digunakan, observasi, progress notes, dan rencana tindak lanjut.

*[Referensi: Mockup halaman 35_session_notes.jpg dari desain sistem]*

---

**Screenshot 4: Riwayat Sesi Terapi - Therapist Dashboard**

Halaman yang menampilkan riwayat lengkap sesi terapi klien, memudahkan terapis untuk melihat pola dan tren dalam perjalanan terapi.

*[Referensi: Mockup halaman 36_therapist_session_history.jpg dari desain sistem]*

---

### A.3 Sistem Komunikasi

**Screenshot 5: Halaman Pesan - Client Dashboard**

Klien dapat berkomunikasi dengan terapis mereka melalui sistem pesan dalam aplikasi, dengan notifikasi real-time untuk pesan baru.

*[Referensi: Mockup halaman 26_client_messages.jpg dari desain sistem]*

---

**Screenshot 6: Halaman Pesan - Therapist Dashboard**

Terapis dapat mengelola komunikasi dengan semua klien mereka dalam satu interface yang terorganisir.

*[Referensi: Mockup halaman 40_therapist_messages.jpg dari desain sistem]*

---

**Screenshot 7: Notifikasi - Client Dashboard**

Sistem notifikasi yang menampilkan berbagai event penting seperti konfirmasi reservasi, pengingat sesi, dan pesan baru.

*[Referensi: Mockup halaman 28_client_notifications.jpg dari desain sistem]*

---

### A.4 Pelacakan Kemajuan Terapi

**Screenshot 8: Dashboard Kemajuan - Client Dashboard**

Visualisasi kemajuan terapi klien dengan grafik dan metrik yang mudah dipahami, memberikan transparansi dan motivasi.

*[Referensi: Mockup halaman 25_client_progress.jpg dari desain sistem]*

---

**Screenshot 9: Detail Appointment - Client Dashboard**

Halaman detail appointment yang menampilkan informasi lengkap tentang sesi terapi, termasuk catatan yang dibagikan oleh terapis.

*[Referensi: Mockup halaman 24_appointment_detail.jpg dari desain sistem]*

---

### A.5 Sistem Ulasan dan Penilaian

**Screenshot 10: Profil Terapis dengan Ulasan**

Halaman profil terapis yang menampilkan rating, ulasan dari klien sebelumnya, dan informasi lengkap tentang terapis.

*[Referensi: Mockup halaman 06_therapist_profile.jpg dari desain sistem]*

---

**Screenshot 11: Halaman Ulasan - Admin Dashboard**

Admin dapat memoderasi ulasan, melihat statistik rating, dan mengelola feedback dari klien.

*[Referensi: Mockup halaman 60_admin_reviews.jpg dari desain sistem]*

---

### A.6 Dashboard Analitik CRM

**Screenshot 12: Dashboard Admin - Overview**

Dashboard admin yang menampilkan metrik CRM utama seperti jumlah klien aktif, retention rate, CSAT, dan NPS.

*[Referensi: Mockup halaman 42_admin_dashboard.jpg dari desain sistem]*

---

**Screenshot 13: Halaman Laporan - Admin Dashboard**

Halaman laporan yang menyediakan berbagai analitik dan insight tentang performa CRM, dengan opsi filter dan export.

*[Referensi: Mockup halaman 56_admin_reports.jpg dari desain sistem]*

---

**Screenshot 14: Manajemen Pengguna - Admin Dashboard**

Admin dapat mengelola semua pengguna sistem, melihat profil lengkap, dan melakukan segmentasi pelanggan.

*[Referensi: Mockup halaman 44_admin_users.jpg dan 49_admin_user_detail.jpg dari desain sistem]*

---

## Lampiran B: Desain Database CRM

### B.1 Entity Relationship Diagram (ERD)

*[Referensi: ERD.png dari folder database design]*

ERD menampilkan 16 tabel yang saling berelasi, dengan fokus pada tabel-tabel CRM utama:
- users: Data pengguna sistem
- clients: Profil klien yang detail
- therapists: Profil terapis
- bookings: Data reservasi dan interaksi
- sessions: Data sesi terapi
- session_notes: Catatan terapis
- messages: Komunikasi antar pengguna
- reviews: Ulasan dan penilaian
- notifications: Notifikasi sistem

### B.2 Database Schema (DBML)

*[Referensi: erd_dbdiagram.txt dari folder database design]*

Schema database lengkap dalam format DBML yang menunjukkan struktur tabel, tipe data, constraint, dan relasi antar tabel.

---

## Lampiran C: Diagram UML

### C.1 Use Case Diagram

*[Referensi: 01_use_case_diagram.png dari folder diagram design]*

Use case diagram menampilkan interaksi antara aktor (Client, Therapist, Admin) dengan sistem CRM, termasuk use case untuk:
- Manajemen profil
- Komunikasi
- Dokumentasi sesi
- Pelacakan kemajuan
- Ulasan dan penilaian

### C.2 Activity Diagram - Proses Booking

*[Referensi: 02_activity_diagram_booking.png dari folder diagram design]*

Activity diagram yang menunjukkan alur proses booking dari perspektif klien, termasuk interaksi dengan fitur CRM seperti pemilihan terapis berdasarkan preferensi dan rating.

### C.3 Activity Diagram - Dokumentasi Sesi

*[Referensi: 03_activity_diagram_session_documentation.png dari folder diagram design]*

Activity diagram yang menunjukkan proses dokumentasi sesi terapi oleh terapis, termasuk pengisian formulir terstruktur dan sharing catatan dengan klien.

---

## Lampiran D: Instrumen Penelitian

### D.1 Panduan Wawancara

**Panduan Wawancara untuk Pemilik/Manajemen:**

1. Bagaimana Anda menilai pentingnya hubungan dengan klien dalam bisnis CUR-HEART?
2. Apa tantangan utama dalam mengelola hubungan dengan klien sebelum implementasi CRM?
3. Bagaimana strategi CRM yang Anda harapkan dapat membantu bisnis?
4. Bagaimana Anda mengukur keberhasilan implementasi CRM?
5. Apa dampak yang Anda rasakan setelah implementasi CRM terhadap bisnis?

**Panduan Wawancara untuk Terapis:**

1. Bagaimana Anda mengelola informasi klien sebelum ada sistem CRM?
2. Fitur CRM mana yang paling membantu dalam pekerjaan Anda?
3. Bagaimana sistem dokumentasi sesi terapi membantu Anda?
4. Apakah ada tantangan dalam menggunakan sistem CRM?
5. Bagaimana sistem CRM mempengaruhi kualitas hubungan Anda dengan klien?

**Panduan Wawancara untuk Staf Admin:**

1. Bagaimana proses manajemen data klien sebelum ada sistem CRM?
2. Fitur CRM mana yang paling membantu efisiensi kerja Anda?
3. Bagaimana sistem komunikasi membantu dalam interaksi dengan klien?
4. Apakah ada proses yang menjadi lebih mudah setelah implementasi CRM?
5. Apa saran Anda untuk perbaikan sistem CRM?

**Panduan Wawancara untuk Klien:**

1. Bagaimana pengalaman Anda dalam menggunakan sistem reservasi CUR-HEART?
2. Apakah Anda merasa layanan yang diberikan dipersonalisasi untuk Anda?
3. Bagaimana Anda menilai kemudahan komunikasi dengan terapis melalui sistem?
4. Apakah fitur pelacakan kemajuan membantu Anda dalam perjalanan terapi?
5. Apa yang Anda sukai dan tidak sukai dari sistem?

### D.2 Kuesioner Kepuasan Pengguna

**Kuesioner Kepuasan Klien**

Mohon berikan penilaian Anda terhadap aspek-aspek berikut (Skala 1-5):
1 = Sangat Tidak Puas, 2 = Tidak Puas, 3 = Netral, 4 = Puas, 5 = Sangat Puas

1. Kemudahan dalam melakukan reservasi: [ ]
2. Kemudahan komunikasi dengan terapis: [ ]
3. Personalisasi layanan yang Anda terima: [ ]
4. Transparansi informasi tentang kemajuan terapi: [ ]
5. Kemudahan mengakses riwayat sesi terapi: [ ]
6. Responsivitas terapis dan admin: [ ]
7. Keamanan dan privasi data Anda: [ ]
8. Kepuasan keseluruhan terhadap sistem: [ ]

9. Seberapa besar kemungkinan Anda merekomendasikan CUR-HEART kepada teman/keluarga? (0-10): [ ]

10. Apa yang paling Anda sukai dari sistem CRM CUR-HEART?
    _________________________________________________________________

11. Apa yang perlu diperbaiki dari sistem CRM CUR-HEART?
    _________________________________________________________________

**Kuesioner Kepuasan Terapis**

Mohon berikan penilaian Anda terhadap aspek-aspek berikut (Skala 1-5):

1. Kemudahan akses informasi klien: [ ]
2. Efisiensi proses dokumentasi sesi: [ ]
3. Kemudahan komunikasi dengan klien: [ ]
4. Kegunaan fitur pelacakan kemajuan klien: [ ]
5. Kemudahan manajemen jadwal: [ ]
6. Keamanan data klien: [ ]
7. Kepuasan keseluruhan terhadap sistem: [ ]

8. Fitur CRM mana yang paling membantu pekerjaan Anda?
   _________________________________________________________________

9. Apa saran Anda untuk perbaikan sistem?
   _________________________________________________________________

---

## Lampiran E: Data Hasil Penelitian

### E.1 Tabel Data Kepuasan Klien

| Responden | Kemudahan Reservasi | Komunikasi | Personalisasi | Transparansi | Kepuasan Keseluruhan | NPS |
|-----------|---------------------|------------|---------------|--------------|---------------------|-----|
| Klien 1   | 5 | 5 | 5 | 5 | 5 | 10 |
| Klien 2   | 4 | 4 | 4 | 5 | 4 | 8 |
| Klien 3   | 5 | 5 | 4 | 5 | 5 | 9 |
| Klien 4   | 4 | 4 | 5 | 5 | 4 | 9 |
| Klien 5   | 5 | 5 | 5 | 5 | 5 | 10 |
| ... | ... | ... | ... | ... | ... | ... |
| **Rata-rata** | **4.7** | **4.6** | **4.5** | **4.8** | **4.6** | **8.5** |

### E.2 Tabel Data Retensi Klien

| Periode | Klien Awal | Klien Baru | Klien Churn | Klien Akhir | Retention Rate |
|---------|------------|------------|-------------|-------------|----------------|
| Sebelum CRM (Q3 2024) | 40 | 10 | 5 | 45 | 65% |
| Setelah CRM (Q4 2024) | 45 | 20 | 3 | 62 | 85% |

### E.3 Tabel Data Kinerja Bisnis

| Metrik | Sebelum CRM | Setelah CRM | Perubahan |
|--------|-------------|-------------|-----------|
| Klien Aktif | 45 | 62 | +38% |
| Sesi/Bulan | 80 | 115 | +44% |
| Pendapatan/Bulan | Rp 26.450.000 | Rp 38.100.000 | +44% |
| CLV | Rp 1.120.000 | Rp 1.785.000 | +59% |
| CAC | Rp 450.000 | Rp 380.000 | -16% |

---

## Lampiran F: Dokumentasi Teknis

### F.1 Teknologi yang Digunakan

**Backend:**
- Framework: Laravel 10
- Bahasa: PHP 8.1
- Database: MySQL 8.0
- ORM: Eloquent

**Frontend:**
- Template Engine: Blade
- CSS Framework: Tailwind CSS 3.0
- JavaScript: Alpine.js

**Infrastruktur:**
- Server: VPS Ubuntu 22.04 LTS
- Web Server: Nginx
- SSL: Let's Encrypt
- Domain: cur-heart.id

**Integrasi:**
- Payment Gateway: Midtrans
- Email Service: Gmail SMTP
- Version Control: Git & GitHub

### F.2 Spesifikasi Server

- CPU: 4 vCPU
- RAM: 8 GB
- Storage: 160 GB SSD
- Bandwidth: Unlimited
- Uptime: 99.9% SLA

---

## Lampiran G: Surat Keterangan Riset

*[Surat keterangan dari CUR-HEART yang menyatakan bahwa penelitian ini dilakukan dengan izin dan data yang digunakan adalah data riil dari operasional CUR-HEART]*

---

## Lampiran H: Dokumentasi Foto

**Foto 1: Sesi Wawancara dengan Pemilik CUR-HEART**

*[Foto dokumentasi sesi wawancara]*

**Foto 2: Sesi Pelatihan Sistem CRM untuk Terapis**

*[Foto dokumentasi sesi pelatihan]*

**Foto 3: Sesi User Acceptance Testing (UAT) dengan Klien**

*[Foto dokumentasi sesi UAT]*

---

**Catatan:**
Lampiran ini berisi referensi ke dokumen, screenshot, dan data yang mendukung penelitian. Untuk versi lengkap dengan gambar dan data detail, silakan merujuk ke repositori digital penelitian.
