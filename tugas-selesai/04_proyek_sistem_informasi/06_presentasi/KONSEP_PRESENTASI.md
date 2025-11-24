# KONSEP MATERI PRESENTASI
## Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART

---

## STRUKTUR PRESENTASI (20 SLIDE)

### BAGIAN 1: PEMBUKAAN (Slide 1-3)
1. **Slide Cover** - Judul, Logo, Tim
2. **Agenda Presentasi** - Outline presentasi
3. **Profil CUR-HEART** - Tentang bisnis

### BAGIAN 2: LATAR BELAKANG & MASALAH (Slide 4-6)
4. **Latar Belakang** - Konteks kesehatan mental Indonesia
5. **Identifikasi Masalah** - 8 masalah utama
6. **Dampak Masalah** - Statistik dan dampak bisnis

### BAGIAN 3: SOLUSI & TUJUAN (Slide 7-8)
7. **Solusi yang Diusulkan** - Sistem informasi berbasis web
8. **Tujuan & Manfaat** - Target pencapaian

### BAGIAN 4: METODOLOGI (Slide 9-10)
9. **Metodologi Penelitian** - SDLC Waterfall
10. **Perencanaan Proyek** - Timeline, WBS, Budget

### BAGIAN 5: ANALISIS & DESAIN (Slide 11-13)
11. **Analisis Kebutuhan** - Functional & Non-functional requirements
12. **Desain Database** - ERD 16 tabel
13. **Desain UI/UX** - Mockup dan wireframe

### BAGIAN 6: IMPLEMENTASI (Slide 14-15)
14. **Arsitektur Sistem** - Tech stack dan arsitektur
15. **Fitur Utama** - Demo fitur-fitur kunci

### BAGIAN 7: HASIL & DAMPAK (Slide 16-18)
16. **Hasil Pengujian** - Testing results, SUS score
17. **Dampak Bisnis** - ROI, efisiensi, pendapatan
18. **Testimoni & Feedback** - User satisfaction

### BAGIAN 8: PENUTUP (Slide 19-20)
19. **Kesimpulan** - Ringkasan pencapaian
20. **Rekomendasi & Q&A** - Fase 2 dan sesi tanya jawab

---

## DESAIN VISUAL

### Palet Warna (Brand CUR-HEART)
- **Primary**: Navy Blue (#1E0E62)
- **Secondary**: Pink (#FF6B7A)
- **Accent**: Teal (#4ECDC4)
- **Background**: White (#FFFFFF)
- **Text**: Dark Gray (#2D3748)

### Tipografi
- **Heading**: Inter Bold
- **Body**: Inter Regular
- **Code**: Fira Code

### Elemen Visual
- Icon dari Heroicons
- Grafik dan chart menggunakan Chart.js
- Animasi transisi halus
- Responsive design

---

## KONTEN DETAIL SETIAP SLIDE

### SLIDE 1: COVER
- Judul: "Sistem Informasi Manajemen Reservasi dan Terapi CUR-HEART"
- Subtitle: "Capstone Project - Sistem Informasi"
- Logo CUR-HEART
- Tim: Roki Anjas, Susanto, Fahruroji
- Universitas Nusa Mandiri
- Tanggal presentasi

### SLIDE 2: AGENDA
1. Latar Belakang & Masalah
2. Solusi & Tujuan
3. Metodologi Penelitian
4. Analisis & Desain Sistem
5. Implementasi & Fitur
6. Hasil & Dampak Bisnis
7. Kesimpulan & Rekomendasi

### SLIDE 3: PROFIL CUR-HEART
- Nama: CUR-HEART (Hypnotherapy & Mind Wellness Center)
- Lokasi: Depok, Jawa Barat
- Layanan: 6 jenis terapi hipnoterapi
- Terapis: 3 terapis profesional
- Klien: 80+ reservasi/bulan
- Visi: Pusat kesehatan mental terkemuka

### SLIDE 4: LATAR BELAKANG
**Kesehatan Mental di Indonesia:**
- 20% populasi mengalami gangguan mental (Riskesdas 2023)
- 1 dari 5 orang Indonesia butuh bantuan kesehatan mental
- Rasio tenaga kesehatan mental: 1:200.000 (jauh di bawah standar WHO)
- Stigma sosial masih tinggi
- Akses layanan terbatas

**Hipnoterapi sebagai Solusi:**
- Efektivitas 75-85% untuk gangguan kecemasan
- Durasi terapi lebih singkat (6-8 sesi vs 12-20 sesi)
- Metode terapi alternatif yang terbukti ilmiah

### SLIDE 5: IDENTIFIKASI MASALAH
**8 Masalah Utama CUR-HEART:**

1. **Proses Reservasi Manual** - Tingkat konversi hanya 60%
2. **Konflik Jadwal** - 8-10 kasus reservasi ganda/bulan
3. **Dokumentasi Tidak Terstruktur** - 15 menit/sesi untuk pencatatan manual
4. **Tidak Ada Data untuk Keputusan** - Laporan memakan waktu 2-3 hari
5. **Beban Administratif Tinggi** - Admin menghabiskan 70% waktu untuk tugas repetitif
6. **Risiko Keamanan Data** - Data sensitif tidak aman
7. **Keterbatasan Akses Informasi** - Klien harus selalu menghubungi admin
8. **Pembayaran Manual** - Konfirmasi memakan waktu berjam-jam

### SLIDE 6: DAMPAK MASALAH
**Dampak Operasional:**
- Kehilangan 40% calon klien karena proses rumit
- Waktu admin 4 jam/hari untuk tugas manual
- Risiko kehilangan data tinggi

**Dampak Finansial:**
- Potensi pendapatan hilang: Rp 10-15 juta/bulan
- Biaya operasional tinggi
- Tidak ada visibilitas keuangan real-time

**Dampak Strategis:**
- Sulit untuk scale bisnis
- Tidak kompetitif dengan kompetitor digital
- Pengambilan keputusan lambat

### SLIDE 7: SOLUSI YANG DIUSULKAN
**Sistem Informasi Berbasis Web**

**Fitur Utama:**
- ✅ Reservasi Online 24/7
- ✅ Manajemen Jadwal Otomatis
- ✅ Dokumentasi Digital Terstruktur
- ✅ Pembayaran Terintegrasi (Midtrans)
- ✅ Dashboard Analitik Real-time
- ✅ Notifikasi Otomatis (Email)
- ✅ Multi-role Access (Admin, Terapis, Klien)

**Teknologi:**
- Laravel 10 (PHP Framework)
- MySQL 8.0 (Database)
- Tailwind CSS (UI Framework)
- Midtrans (Payment Gateway)

### SLIDE 8: TUJUAN & MANFAAT
**Tujuan Proyek:**
1. Meningkatkan efisiensi operasional hingga 60%
2. Meningkatkan tingkat konversi dari 60% ke 85%
3. Eliminasi 100% reservasi ganda
4. Menyediakan data real-time untuk pengambilan keputusan
5. Meningkatkan kepuasan pengguna

**Manfaat untuk Stakeholder:**
- **CUR-HEART**: Efisiensi, skalabilitas, keunggulan kompetitif
- **Klien**: Kemudahan reservasi, transparansi, privasi terjaga
- **Terapis**: Produktivitas meningkat, dokumentasi mudah
- **Admin**: Beban kerja berkurang 70%

### SLIDE 9: METODOLOGI PENELITIAN
**SDLC Waterfall Model**

**Tahapan:**
1. **Analisis Kebutuhan** (2 minggu) - Observasi, wawancara, dokumentasi
2. **Desain Sistem** (2 minggu) - ERD, UML, UI/UX mockup
3. **Implementasi** (4 minggu) - Coding, integrasi
4. **Pengujian** (2 minggu) - Unit, integration, UAT
5. **Deployment** (1 minggu) - Go-live, training

**Total Durasi:** 16 minggu (Sep - Des 2024)

**Alasan Pemilihan Waterfall:**
- Kebutuhan jelas dan stabil
- Timeline tetap (semester akademik)
- Dokumentasi lengkap diperlukan
- Tim kecil dan terstruktur

### SLIDE 10: PERENCANAAN PROYEK
**Timeline & Budget**

**Gantt Chart:**
- Week 1-2: Requirements Analysis
- Week 3-4: System Design
- Week 5-8: Implementation
- Week 9-10: Testing
- Week 11: Deployment
- Week 12-16: Documentation

**Budget:**
- Total Investasi: Rp 5.560.000
- Biaya Operasional/Tahun: Rp 9.750.000
- ROI Proyeksi 5 Tahun: 1.743%

**Tim:**
- Roki Anjas - PM & Backend Developer
- Susanto - Frontend Developer & UI/UX Designer
- Fahruroji - Full-stack Developer & DB Architect

### SLIDE 11: ANALISIS KEBUTUHAN
**Kebutuhan Fungsional (50+ requirements):**

**Modul Utama:**
1. Autentikasi & Manajemen User
2. Informasi Publik (Landing page, Blog)
3. Reservasi & Penjadwalan
4. Dashboard Klien
5. Dashboard Terapis
6. Dashboard Admin
7. Pembayaran (Midtrans)
8. Notifikasi & Komunikasi

**Kebutuhan Non-Fungsional:**
- Performance: Response time <2 detik
- Security: OWASP Top 10, HTTPS, encryption
- Usability: SUS score >70
- Reliability: Uptime 99%
- Scalability: 100 concurrent users

### SLIDE 12: DESAIN DATABASE
**Entity Relationship Diagram (ERD)**

**16 Tabel Utama:**
- users, roles, permissions
- services, therapists
- bookings, booking_sessions
- payments, payment_methods
- therapy_notes, progress_tracking
- reviews, notifications
- blog_posts, faqs

**Normalisasi:** 3NF (Third Normal Form)

**Relasi:**
- One-to-Many: User → Bookings, Therapist → Sessions
- Many-to-Many: Users ↔ Roles (via role_user)
- One-to-One: Booking → Payment

**Indexing Strategy:**
- Primary keys (auto-increment)
- Foreign keys
- Composite indexes (user_id, created_at)
- Full-text search (blog content)

### SLIDE 13: DESAIN UI/UX
**Mockup & Wireframe**

**41 Halaman Mockup (Figma):**
- Public: 6 halaman (Landing, Services, Therapists, Blog, Contact, FAQ)
- Client: 13 halaman (Dashboard, Booking, History, Progress, Profile)
- Therapist: 12 halaman (Dashboard, Schedule, Clients, Sessions, Notes)
- Admin: 10 halaman (Dashboard, Users, Bookings, Reports, Settings)

**Prinsip Desain:**
- User-centered design
- Consistency (Tailwind components)
- Feedback (notifications)
- Simplicity (4-step booking)
- Visual hierarchy (brand colors)
- Responsive (mobile-first)
- Accessibility (WCAG 2.1)

**Palet Warna Menenangkan:**
- Navy Blue, Pink, Teal untuk kesehatan mental

### SLIDE 14: ARSITEKTUR SISTEM
**Tech Stack**

**Frontend:**
- Blade Templates (Laravel)
- Tailwind CSS 3.0
- Alpine.js (interactivity)
- Chart.js (visualizations)

**Backend:**
- Laravel 10 (PHP 8.1)
- Eloquent ORM
- Laravel Sanctum (API auth)
- Queue system (jobs)

**Database:**
- MySQL 8.0
- InnoDB engine (ACID compliance)

**Infrastructure:**
- VPS Ubuntu 22.04 LTS
- Nginx web server
- SSL (Let's Encrypt)
- Domain: cur-heart.id

**Integrations:**
- Midtrans (Payment Gateway)
- Gmail SMTP (Email notifications)

**Arsitektur MVC:**
```
View (Blade) → Controller → Model → Database
              ↓
         Middleware (Auth, CSRF)
```

### SLIDE 15: FITUR UTAMA
**Demo Fitur-Fitur Kunci**

**1. Reservasi Online (4 Langkah):**
- Pilih Layanan → Pilih Terapis → Pilih Jadwal → Konfirmasi & Bayar
- Real-time availability check
- Automatic conflict detection

**2. Dashboard Multi-Role:**
- **Klien**: Upcoming sessions, progress tracking, history
- **Terapis**: Today's schedule, client management, session notes
- **Admin**: System metrics, user management, reports

**3. Pembayaran Terintegrasi:**
- Midtrans Snap (seamless checkout)
- Multiple payment methods (credit card, e-wallet, bank transfer, QRIS)
- Automatic verification & invoice generation

**4. Notifikasi Otomatis:**
- Email confirmation (booking, payment)
- Reminders (H-1, H-0)
- Cancellation notifications

**5. Dokumentasi Sesi:**
- Structured form (rich text editor)
- Progress tracking with visual graphs
- Secure access control

**6. Reporting & Analytics:**
- Revenue trends
- Booking statistics
- Therapist performance
- Export to Excel/PDF

### SLIDE 16: HASIL PENGUJIAN
**Testing Results**

**Unit Testing:**
- 30 test cases
- Code coverage: 72%
- All critical logic tested

**Functional Testing:**
- 100% pass rate
- All features working as expected
- Zero critical bugs

**Performance Testing:**
- Average page load: 1.8 seconds ✅ (target <2s)
- API response: <500ms for 95% requests ✅
- Database query: <100ms average ✅
- Concurrent users: 100+ supported ✅

**Security Testing:**
- OWASP Top 10: All mitigated ✅
- SQL Injection: Protected (Eloquent ORM) ✅
- XSS: Protected (Blade escaping) ✅
- CSRF: Protected (Laravel tokens) ✅
- Password: Bcrypt hashing ✅
- HTTPS: Enforced ✅

**Usability Testing (SUS):**
- SUS Score: 78.5/100 ✅ (target >70)
- User satisfaction: 9/10 ⭐
- Task completion rate: 95% ✅

**UAT:**
- Approved by all stakeholders ✅
- Owner satisfaction: 10/10
- Therapist satisfaction: 9/10
- Client satisfaction: 8.5/10

### SLIDE 17: DAMPAK BISNIS
**ROI & Business Impact**

**Efisiensi Operasional:**
- ⬆️ 60% peningkatan efisiensi admin (4 jam → 1.2 jam/hari)
- ⬆️ 65% proses reservasi lebih cepat (10 menit → 3.5 menit)
- ⬇️ 100% eliminasi reservasi ganda (8-10 kasus → 0)
- ⬆️ 70% pengurangan beban kerja admin

**Pertumbuhan Bisnis:**
- ⬆️ 31% peningkatan volume reservasi (80 → 105/bulan)
- ⬆️ 31% peningkatan pendapatan (Rp 26.45M → Rp 34.72M/bulan)
- ⬆️ 31% peningkatan retensi klien (65% → 85%)
- ⬆️ 25% peningkatan kapasitas layanan

**Financial ROI:**
- Total Investment: Rp 5.56 juta
- Annual Savings: Rp 20 juta (efisiensi admin)
- Annual Revenue Increase: Rp 99.24 juta
- **ROI 5 Years: 1.743%** 🚀
- **Payback Period: 20 hari** ⚡

**System Reliability:**
- Uptime: 99.8% (target 99%)
- Zero data loss
- Zero security breaches

### SLIDE 18: TESTIMONI & FEEDBACK
**User Satisfaction**

**Pemilik CUR-HEART:**
> "Sistem ini mengubah cara kami beroperasi. Sekarang saya bisa melihat semua data bisnis real-time dan membuat keputusan lebih cepat. ROI-nya luar biasa!"
> 
> — **Ibu Sarah**, Owner CUR-HEART
> 
> **Rating: 10/10** ⭐⭐⭐⭐⭐

**Terapis:**
> "Dokumentasi sesi terapi jadi jauh lebih mudah. Saya bisa fokus pada klien tanpa khawatir kehilangan catatan. Jadwal juga tidak pernah bentrok lagi."
> 
> — **Pak Budi**, Terapis Senior
> 
> **Rating: 9/10** ⭐⭐⭐⭐⭐

**Klien:**
> "Reservasi jadi sangat mudah, bisa dilakukan kapan saja dari HP. Saya juga bisa lihat progress terapi saya. Sangat membantu!"
> 
> — **Rina**, Klien CUR-HEART
> 
> **Rating: 8.5/10** ⭐⭐⭐⭐

**Admin:**
> "Pekerjaan saya jadi jauh lebih ringan. Tidak perlu lagi manual cek jadwal atau konfirmasi pembayaran satu-satu. Sistem otomatis semua!"
> 
> — **Dina**, Admin CUR-HEART
> 
> **Rating: 9/10** ⭐⭐⭐⭐⭐

**Overall Satisfaction: 9/10** 🎉

### SLIDE 19: KESIMPULAN
**Ringkasan Pencapaian**

**✅ Semua Tujuan Tercapai (7/7):**
1. ✅ Analisis kebutuhan komprehensif (50+ requirements)
2. ✅ Desain sistem terstruktur (ERD 16 tabel, 41 mockup)
3. ✅ Implementasi sistem web (60+ halaman, 5 role interfaces)
4. ✅ Pengujian menyeluruh (SUS 78.5, 100% functional pass)
5. ✅ Deployment produksi (99.8% uptime)
6. ✅ Dokumentasi lengkap (85 hal laporan, manual, video)
7. ✅ Dampak terukur (ROI 1.743%, efisiensi 60%)

**🎯 Pencapaian Melebihi Target:**
- 86% tujuan melebihi target
- ROI 1.743% (sangat tinggi)
- Kepuasan pengguna 9/10
- Stabilitas sistem 99.8%

**💡 Pembelajaran Kunci:**
- Framework matang (Laravel) mempercepat development
- Desain database yang baik adalah fondasi
- User feedback awal sangat penting
- Testing investasi yang terbayar
- Komunikasi tim kunci kesuksesan

**🏆 Sistem Berhasil:**
- Fungsional ✅
- User-friendly ✅
- Secure ✅
- High-performance ✅
- Scalable ✅
- Well-documented ✅
- High ROI ✅

### SLIDE 20: REKOMENDASI & Q&A
**Fase 2 Development (2025)**

**Prioritas TINGGI (Q1-Q2 2025):**
1. 📱 Notifikasi SMS (ROI: +Rp 15M/tahun)
2. 🎁 Sistem Keanggotaan/Paket (ROI: +Rp 50M/tahun)
3. ⚡ Redis Caching (Performance <1s)
4. 🔐 Two-Factor Authentication (Security)
5. ☁️ Cloud Backup Otomatis (Business continuity)
6. 🎥 Integrasi Video Therapy (ROI: +Rp 40M/tahun)

**Total Investasi Fase 2 (Prioritas Tinggi):**
- Biaya: Rp 18-28 juta
- ROI: +Rp 125 juta/tahun
- Payback: 2-3 bulan

**Prioritas SEDANG (Q2-Q3 2025):**
- Mobile App (iOS/Android)
- Advanced Analytics Dashboard
- CDN untuk aset statis

**Rekomendasi Operasional:**
- Training berkelanjutan (triwulanan)
- SOP operasional
- Monitoring harian
- Backup verification bulanan
- Compliance UU PDP

---

## 🙏 TERIMA KASIH

**Tim Pengembang:**
- Roki Anjas (11250066) - PM & Backend Developer
- Susanto (11250068) - Frontend Developer & UI/UX Designer
- Fahruroji (11250085) - Full-stack Developer & DB Architect

**Dosen Pembimbing:**
- [Nama Dosen Pembimbing]

**Sponsor:**
- CUR-HEART (Hypnotherapy & Mind Wellness Center)

---

## ❓ SESI TANYA JAWAB

**Pertanyaan yang Sering Diajukan:**

1. **Berapa lama waktu pengembangan?**
   - 16 minggu (September - Desember 2024)

2. **Berapa biaya investasi?**
   - Rp 5.56 juta (one-time) + Rp 9.75 juta/tahun (operasional)

3. **Berapa ROI-nya?**
   - 1.743% dalam 5 tahun, payback period 20 hari

4. **Apakah sistem aman?**
   - Ya, mengikuti OWASP Top 10, HTTPS, encryption, CSRF protection

5. **Apakah ada aplikasi mobile?**
   - Belum, tapi responsive design bisa diakses dari mobile browser
   - Mobile app native direncanakan di Fase 2

6. **Bagaimana dengan backup data?**
   - Backup otomatis harian, retensi 30 hari
   - Cloud backup direncanakan di Fase 2

---

**Kontak:**
- Email: [email tim]
- GitHub: [repository link]
- Website: cur-heart.id

---

**Terima kasih atas perhatiannya!** 🙏
