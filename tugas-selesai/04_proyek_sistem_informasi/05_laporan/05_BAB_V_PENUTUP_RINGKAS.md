# BAB V
# PENUTUP

## 5.1 Kesimpulan

Berdasarkan hasil penelitian dan pembahasan, dapat disimpulkan bahwa:

1. Proyek Sistem Informasi Manajemen Pemesanan dan Terapi CUR-HEART telah berhasil mencapai seluruh tujuan yang ditetapkan, meliputi analisis kebutuhan, perancangan sistem (ERD 16 entitas, 41 mockup UI/UX, diagram UML), implementasi aplikasi web full-stack menggunakan Laravel 10, pengujian komprehensif (SUS 78,5/100), deployment ke production, dan dokumentasi lengkap.

2. Sistem memberikan dampak bisnis yang signifikan dengan meningkatkan efisiensi operasional 60%, kapasitas pemesanan 25%, kepuasan pengguna mencapai 9/10, dan ROI 1.743% dalam proyeksi 5 tahun, membuktikan keberhasilan transformasi digital dari sistem manual ke otomatis.

### Kelebihan Sistem

1. Mengotomatisasi seluruh proses bisnis (pemesanan, penjadwalan, pembayaran, dokumentasi) yang meningkatkan efisiensi dan mengeliminasi pemesanan ganda.
2. Antarmuka user-friendly dengan desain responsif yang dapat diakses dari berbagai perangkat (desktop, tablet, mobile).
3. Keamanan data terjamin melalui implementasi CSRF protection, XSS prevention, SQL injection prevention, password hashing, HTTPS, dan role-based access control.
4. Terintegrasi dengan payment gateway Midtrans yang menyediakan 8+ metode pembayaran dengan verifikasi otomatis.
5. Arsitektur sistem yang scalable dan database yang dinormalisasi (3NF) memungkinkan pertumbuhan jangka panjang.
6. Dokumentasi lengkap (laporan, manual pengguna, manual admin, video tutorial) mendukung sustainability sistem.

### Kekurangan Sistem

1. Notifikasi masih terbatas pada email, belum ada SMS atau push notification untuk reminder yang lebih efektif.
2. Belum tersedia aplikasi mobile native (iOS/Android) untuk pengalaman mobile yang optimal.
3. Fitur teletherapy (video conference) belum tersedia, membatasi layanan jarak jauh.
4. Dashboard analytics masih dasar, belum ada business intelligence lanjutan untuk forecasting.
5. Program membership dan paket berlangganan belum tersedia untuk meningkatkan customer retention.
6. Backup database belum otomatis ke cloud untuk disaster recovery.

---

## 5.2 Saran

### 5.2.1 Saran dari Aspek Manajerial

1. Melaksanakan program pelatihan berkelanjutan (refresh triwulanan) untuk memastikan pengguna dapat memaksimalkan fitur sistem dan mengadopsi update baru.
2. Mengalokasikan budget operasional TI tahunan (estimasi Rp 50 juta) untuk maintenance, hosting, security audit, dan upgrade system.
3. Melakukan monitoring KPI secara rutin (volume booking, revenue, user satisfaction, uptime) untuk memastikan sistem terus memberikan value.
4. Mengimplementasikan automated cloud backup harian dengan disaster recovery plan dan melakukan backup recovery testing bulanan.
5. Memastikan compliance dengan UU Perlindungan Data Pribadi No. 27/2022 melalui review privacy policy dan training staff.

### 5.2.2 Saran dari Aspek Sistem

**Prioritas Tinggi:**
1. Menambahkan notifikasi SMS untuk konfirmasi booking dan reminder sesi guna mengurangi no-show rate.
2. Mengembangkan sistem membership/paket berlangganan untuk meningkatkan customer lifetime value.
3. Implementasi Redis caching untuk meningkatkan performance menjadi <1 detik page load time.
4. Menambahkan Two-Factor Authentication (2FA) untuk keamanan enhanced akun terapis dan admin.
5. Integrasi video conferencing untuk mendukung sesi terapi jarak jauh dan ekspansi pasar geografis.

**Prioritas Sedang:**
6. Pengembangan aplikasi mobile native (iOS/Android) untuk user experience yang lebih optimal.
7. Advanced analytics dashboard dengan forecasting dan trend analysis untuk data-driven decision making.
8. Database encryption at rest untuk data sensitif (session notes, medical history).

**Prioritas Rendah:**
9. AI chatbot untuk FAQ dan 24/7 customer support.
10. Integrasi Google Calendar untuk automatic availability update.

### 5.2.3 Saran untuk Penelitian Selanjutnya

1. **Machine Learning untuk Prediksi Hasil Terapi**: Mengembangkan model prediktif untuk memprediksi outcome terapi berdasarkan profil klien dan data historis untuk personalisasi treatment plan.

2. **Studi Efektivitas Teletherapy vs Face-to-Face**: Randomized Controlled Trial (RCT) membandingkan efektivitas sesi hipnoterapi online vs tatap muka untuk kondisi kecemasan dan stress management.

3. **Dampak Transformasi Digital pada UKM Kesehatan**: Studi kasus untuk mengidentifikasi critical success factors transformasi digital dalam praktik terapi dan pengaruhnya terhadap business performance.

4. **Analisis Persepsi Privasi**: Survey research untuk memahami persepsi pengguna terhadap privasi data dalam aplikasi kesehatan mental dan faktor yang mempengaruhi trust.

5. **ROI Jangka Panjang Investasi IT Kesehatan**: Studi longitudinal 3-5 tahun untuk mengukur nilai investasi IT kesehatan dan faktor-faktor yang memprediksi sustainable ROI.

---

**Penutup:**

Sistem Informasi CUR-HEART telah berhasil mencapai tujuan dengan hasil melampaui ekspektasi. Sistem bersifat fungsional, user-friendly, aman, dan scalable dengan ROI 1.743%. Implementasi saran-saran di atas secara bertahap akan memastikan sistem terus berkembang, mempertahankan keunggulan kompetitif, dan memberikan value berkelanjutan kepada stakeholders.
