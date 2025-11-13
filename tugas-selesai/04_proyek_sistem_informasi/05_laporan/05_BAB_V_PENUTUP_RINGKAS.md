# BAB V
# PENUTUP

## 5.1 Kesimpulan

Berdasarkan hasil penelitian dan pembahasan, dapat disimpulkan bahwa:

Proyek Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART telah berhasil mencapai seluruh tujuan yang ditetapkan, meliputi analisis kebutuhan, perancangan sistem (ERD 16 entitas, 41 mockup UI/UX, diagram UML), implementasi aplikasi web full-stack menggunakan Laravel 10, pengujian komprehensif (SUS 78,5/100), deployment ke production, dan dokumentasi lengkap. Sistem memberikan dampak bisnis yang signifikan dengan meningkatkan efisiensi operasional 60%, kapasitas pemesanan 25%, kepuasan pengguna mencapai 9/10, dan ROI 1.743% dalam proyeksi 5 tahun, membuktikan keberhasilan transformasi digital dari sistem manual ke otomatis.

Sistem yang dikembangkan memiliki beberapa kelebihan, antara lain:
- Mengotomatisasi seluruh proses bisnis (pemesanan, penjadwalan, pembayaran, dokumentasi) yang meningkatkan efisiensi dan mengeliminasi pemesanan ganda
- Antarmuka user-friendly dengan desain responsif yang dapat diakses dari berbagai perangkat (desktop, tablet, mobile)
- Keamanan data terjamin melalui implementasi CSRF protection, XSS prevention, SQL injection prevention, password hashing, HTTPS, dan role-based access control
- Terintegrasi dengan payment gateway Midtrans yang menyediakan 8+ metode pembayaran dengan verifikasi otomatis
- Arsitektur sistem yang scalable dan database yang dinormalisasi (3NF) memungkinkan pertumbuhan jangka panjang
- Dokumentasi lengkap (laporan, manual pengguna, manual admin, video tutorial) mendukung sustainability sistem

Meskipun telah memenuhi seluruh kebutuhan yang ditetapkan, sistem masih memiliki beberapa kekurangan yang perlu dikembangkan di masa depan, yaitu:
- Notifikasi masih terbatas pada email, belum ada SMS atau push notification untuk reminder yang lebih efektif
- Belum tersedia aplikasi mobile native (iOS/Android) untuk pengalaman mobile yang optimal
- Fitur teletherapy (video conference) belum tersedia, membatasi layanan jarak jauh
- Dashboard analytics masih dasar, belum ada business intelligence lanjutan untuk forecasting
- Program membership dan paket berlangganan belum tersedia untuk meningkatkan customer retention
- Backup database belum otomatis ke cloud untuk disaster recovery

---

## 5.2 Saran

Berdasarkan evaluasi sistem yang telah diimplementasikan, berikut adalah saran untuk pengembangan dan perbaikan di masa depan:

**Dari Aspek Manajerial:**
- Melaksanakan program pelatihan berkelanjutan (refresh triwulanan) untuk memastikan pengguna dapat memaksimalkan fitur sistem dan mengadopsi update baru
- Mengalokasikan budget operasional TI tahunan (estimasi Rp 50 juta) untuk maintenance, hosting, security audit, dan upgrade system
- Melakukan monitoring KPI secara rutin (volume booking, revenue, user satisfaction, uptime) untuk memastikan sistem terus memberikan value
- Mengimplementasikan automated cloud backup harian dengan disaster recovery plan dan melakukan backup recovery testing bulanan
- Memastikan compliance dengan UU Perlindungan Data Pribadi No. 27/2022 melalui review privacy policy dan training staff

**Dari Aspek Sistem:**

Prioritas Tinggi:
- Menambahkan notifikasi SMS untuk konfirmasi booking dan reminder sesi guna mengurangi no-show rate
- Mengembangkan sistem membership/paket berlangganan untuk meningkatkan customer lifetime value
- Implementasi Redis caching untuk meningkatkan performance menjadi <1 detik page load time
- Menambahkan Two-Factor Authentication (2FA) untuk keamanan enhanced akun terapis dan admin
- Integrasi video conferencing untuk mendukung sesi terapi jarak jauh dan ekspansi pasar geografis

Prioritas Sedang:
- Pengembangan aplikasi mobile native (iOS/Android) untuk user experience yang lebih optimal
- Advanced analytics dashboard dengan forecasting dan trend analysis untuk data-driven decision making
- Database encryption at rest untuk data sensitif (session notes, medical history)

Prioritas Rendah:
- AI chatbot untuk FAQ dan 24/7 customer support
- Integrasi Google Calendar untuk automatic availability update

**Untuk Penelitian Selanjutnya:**
- Machine Learning untuk Prediksi Hasil Terapi: Mengembangkan model prediktif untuk memprediksi outcome terapi berdasarkan profil klien dan data historis untuk personalisasi treatment plan
- Studi Efektivitas Teletherapy vs Face-to-Face: Randomized Controlled Trial (RCT) membandingkan efektivitas sesi hipnoterapi online vs tatap muka untuk kondisi kecemasan dan stress management
- Dampak Transformasi Digital pada UKM Kesehatan: Studi kasus untuk mengidentifikasi critical success factors transformasi digital dalam praktik terapi dan pengaruhnya terhadap business performance
- Analisis Persepsi Privasi: Survey research untuk memahami persepsi pengguna terhadap privasi data dalam aplikasi kesehatan mental dan faktor yang mempengaruhi trust
- ROI Jangka Panjang Investasi IT Kesehatan: Studi longitudinal 3-5 tahun untuk mengukur nilai investasi IT kesehatan dan faktor-faktor yang memprediksi sustainable ROI

---

Sistem Informasi CUR-HEART telah berhasil mencapai tujuan dengan hasil melampaui ekspektasi. Sistem bersifat fungsional, user-friendly, aman, dan scalable dengan ROI 1.743%. Implementasi saran-saran di atas secara bertahap akan memastikan sistem terus berkembang, mempertahankan keunggulan kompetitif, dan memberikan value berkelanjutan kepada stakeholders.
