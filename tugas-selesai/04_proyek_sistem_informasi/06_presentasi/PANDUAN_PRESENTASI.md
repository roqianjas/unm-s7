# 📋 PANDUAN PRESENTASI CUR-HEART

## 🎯 **RINGKASAN CEPAT**

**Judul:** CUR-HEART - Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital  
**Durasi:** 30 menit + Q&A  
**Tim:** Roki Anjas (11250066), Susanto (11250068), Fahruroji (11250085)

---

## 🗣️ **POIN KUNCI PRESENTASI**

### **1. PEMBUKAAN (Slide 1-3)** - 3 menit
- Perkenalkan tim dan judul proyek
- CUR-HEART: Klinik hipnoterapi dengan 6 layanan, 3 terapis, ~30 reservasi/bulan
- **Fokus:** Digitalisasi sistem reservasi dan manajemen terapi

### **2. MASALAH & TUJUAN (Slide 4-6)** - 7 menit
**8 Masalah Utama:**
1. Reservasi manual (konversi 60%)
2. Konflik jadwal (8-10 kasus/bulan)
3. Dokumentasi tidak terstruktur
4. Tidak ada pelacakan progres
5. Akses informasi terbatas
6. Kesulitan pengambilan keputusan
7. Pembayaran tidak terpadu
8. Risiko keamanan data tinggi

**Solusi:** Sistem informasi berbasis web dengan 7 fitur utama

### **3. METODOLOGI (Slide 7-8)** - 3 menit
- **Metode:** SDLC Waterfall (16 minggu)
- **Anggaran:** Rp 86,8 juta
- **Alasan:** Kebutuhan jelas, timeline tetap, dokumentasi lengkap

### **4. DESAIN SISTEM (Slide 9-13)** - 8 menit
- **Kebutuhan:** 52 fungsional + 18 non-fungsional
- **Database:** ERD 16 tabel (3NF)
- **UI/UX:** 66 maket Figma (16 publik + 50 dashboard)
- **Arsitektur:** MVC dengan Laravel + MySQL + Tailwind

**Poin penting:** Tunjukkan kompleksitas desain yang matang

### **5. PROTOTIPE (Slide 14)** - 4 menit ⭐
**10 Fitur Utama:**
1. Reservasi 4 langkah
2. Pembayaran terintegrasi (Midtrans)
3. Dashboard multi-peran
4. Dokumentasi sesi digital
5. Notifikasi otomatis
6. Pelaporan & analitik

**Catatan:** Jelaskan ini masih prototipe (desain), belum implementasi penuh

### **6. VALIDASI (Slide 15)** - 3 menit ⭐
- **SUS Score:** 80.5/100 (Kategori EXCELLENT)
- **UAT:** 12 skenario - 100% pass
- **Kepuasan:** 4.6/5.0
- **Feedback positif:** Desain modern, navigasi intuitif

### **7. KESIMPULAN (Slide 16-17)** - 4 menit
**Semua 6 tujuan tercapai:**
✅ Analisis: 52 kebutuhan (+73% dari target)
✅ Desain: ERD + UML + UI lengkap
✅ Prototipe: 66 maket (+32% dari target)
✅ Validasi: SUS 80.5 (target ≥68)
✅ Spesifikasi: Terdefinisi lengkap
✅ Dokumentasi: 85 halaman (+21%)

**Dampak:** Efisiensi +60%, kapasitas +31%, konflik jadwal 0%

---

## ❓ **PERTANYAAN & JAWABAN YANG MUNGKIN MUNCUL**

### **A. TENTANG MASALAH**

**Q1: Mengapa fokus ke CUR-HEART? Apakah masalah ini umum di klinik terapi lain?**
> **Jawab:** Ya, penelitian WHO menunjukkan rasio tenaga kesehatan mental di Indonesia 1:200K (standar 1:100K). Masalah reservasi manual dan dokumentasi tidak terstruktur adalah isu umum di klinik kecil-menengah. CUR-HEART dipilih sebagai studi kasus karena akses langsung untuk observasi dan validasi.

**Q2: Dari 8 masalah, mana yang paling kritis?**
> **Jawab:** Konflik jadwal (masalah #2) karena berdampak langsung ke kepuasan klien dan reputasi klinik. Menyebabkan 8-10 kasus reservasi ganda per bulan yang harus di-reschedule manual, membuang waktu admin dan klien.

### **B. TENTANG DESAIN & TEKNOLOGI**

**Q3: Mengapa pilih Laravel bukan framework lain seperti Node.js?**
> **Jawab:** 
> - Laravel mature dengan ekosistem lengkap (Eloquent ORM, Blade, autentikasi)
> - Dokumentasi sangat baik dan komunitas besar di Indonesia
> - Cocok untuk CRUD-intensive application seperti sistem manajemen
> - Tim sudah familiar dengan PHP

**Q4: Kenapa pakai MySQL bukan PostgreSQL atau MongoDB?**
> **Jawab:** MySQL dipilih karena:
> - Data terstruktur (reservasi, klien, sesi) cocok untuk relational database
> - Performa sangat baik untuk read-heavy operations
> - Biaya hosting lebih murah
> - Sudah terintegrasi baik dengan Laravel

**Q5: Normalisasi 3NF, apakah tidak over-engineering untuk klinik kecil?**
> **Jawab:** Tidak. 3NF mencegah anomali data (insert/update/delete) yang kritis untuk data medis. Konsistensi data pasien dan riwayat terapi harus dijaga. Trade-off performa minimal karena proper indexing (15 indeks strategis).

### **C. TENTANG PROTOTIPE**

**Q6: Ini prototipe atau sudah implementasi coding?**
> **Jawab:** Ini adalah **high-fidelity prototype** di Figma dengan 66 maket interaktif. Belum ada coding implementasi. Fokus penelitian adalah perancangan sistem lengkap (analisis, desain, validasi desain). Implementasi coding bisa menjadi penelitian lanjutan.

**Q7: Kenapa tidak langsung coding saja daripada buat prototipe?**
> **Jawab:** 
> - Prototyping lebih efisien untuk validasi konsep (biaya lebih rendah)
> - Bisa dapat feedback pengguna lebih cepat sebelum coding
> - Perubahan desain di Figma jauh lebih murah dari refactoring code
> - Sesuai metodologi Waterfall: desain harus final sebelum implementasi

**Q8: Berapa lama estimasi jika mau implementasi coding penuh?**
> **Jawab:** Berdasarkan timeline Gantt, 4 minggu untuk fase implementasi (minggu 5-8). Dengan desain yang sudah matang, developer tinggal follow spesifikasi yang sudah dibuat.

### **D. TENTANG VALIDASI**

**Q9: SUS 80.5 itu bagus atau tidak? Kenapa standard-nya 68?**
> **Jawab:** 
> - SUS 68 adalah rata-rata industri untuk semua jenis sistem
> - Skor 80.5 masuk kategori "A" atau "Excellent" (top 10% sistem)
> - Ini luar biasa untuk prototipe digital health yang biasanya kompleks
> - Grade A = above 80.3 (berdasarkan Sauro & Lewis 2016)

**Q10: Cuma 15 responden UAT, apakah cukup representatif?**
> **Jawab:** Untuk usability testing, Nielsen Norman Group merekomendasikan 5-15 pengguna sudah cukup menemukan 85-90% masalah usability. 15 responden mencakup 3 grup: admin (3), terapis (2), klien potensial (10) - proporsi sesuai user base.

**Q11: Apa saja saran perbaikan dari responden?**
> **Jawab:** 4 saran utama:
> 1. Tutorial/onboarding (7 responden) - akan ditambahkan
> 2. Konfirmasi untuk aksi kritis (5 responden) - noted
> 3. Filter pencarian lebih advanced (4 responden) - future enhancement
> 4. Notifikasi WhatsApp (3 responden) - perlu integrasi API

### **E. TENTANG BISNIS & DAMPAK**

**Q12: ROI-nya berapa? Kapan balik modal?**
> **Jawab:** 
> - Investasi: Rp 86,8 juta (one-time) + Rp 22,85 juta/tahun (operasional)
> - Saving: Efisiensi admin 60% (~18 jam/minggu) = ~Rp 30 juta/tahun
> - Peningkatan kapasitas 31% = ~10 klien/bulan extra = ~Rp 50 juta/tahun
> - **Payback period: ~13 bulan**

**Q13: Bagaimana keamanan data pasien dijaga? Apakah comply GDPR/regulasi?**
> **Jawab:** 
> - Sesuai UU No. 27 Tahun 2022 (Perlindungan Data Pribadi Indonesia)
> - Implementasi: HTTPS, password hashing (Bcrypt), CSRF protection, XSS prevention
> - Role-based access control (RBAC)
> - Audit logs untuk tracking akses data sensitif
> - Backup harian otomatis

**Q14: Scalability? Kalau klien jadi 1000+ gimana?**
> **Jawab:** 
> - Arsitektur dirancang untuk 100 concurrent users (saat ini ~50 klien)
> - Database indexing sudah optimal (15 strategic indexes)
> - Bisa scale vertical (upgrade server) atau horizontal (load balancer)
> - Cache layer (Redis) bisa ditambahkan untuk performa
> - Estimasi support sampai 500-1000 klien dengan current architecture

### **F. PERBANDINGAN & ALTERNATIF**

**Q15: Apakah sudah ada sistem sejenis? Apa bedanya?**
> **Jawab:** Ada SaaS generik (e.g., SimplePractice, TherapyNotes), tapi:
> - **Mahal:** $30-100/terapis/bulan (Rp 500K-1,7 juta)
> - **Tidak customizable** untuk hipnoterapi spesifik
> - **Berbahasa Inggris** - kurang cocok untuk pasar Indonesia
> - CUR-HEART system: **custom fit**, **one-time cost**, **Bahasa Indonesia**

**Q16: Kenapa tidak pakai WordPress + booking plugin saja?**
> **Jawab:** 
> - WordPress cocok untuk website, tapi kurang untuk management system kompleks
> - Dokumentasi terapi dan progress tracking butuh custom database design
> - Payment gateway integration lebih robust di Laravel
> - Security dan performance lebih terkontrol di custom app
> - Long-term: lebih mudah maintain custom Laravel daripada WordPress dengan banyak plugin

### **G. METODOLOGI & PROSES**

**Q17: Kenapa Waterfall bukan Agile? Bukankah Agile lebih modern?**
> **Jawab:** 
> - **Timeline tetap:** 16 minggu (semester akademik) - Waterfall lebih predictable
> - **Kebutuhan stabil:** CUR-HEART sudah operasional, requirements jelas
> - **Dokumentasi lengkap:** Diperlukan untuk proyek akhir akademik
> - **Tim kecil:** 3 orang - overhead Agile ceremonies tidak efisien
> - Agile cocok untuk startup/requirements berubah, ini bukan kasusnya

**Q18: Bagaimana pembagian kerja tim?**
> **Jawab:** 
> - **Roki Anjas:** Project Manager, UI/UX Design, Backend Architecture
> - **Susanto:** Dokumentasi, Requirements Analysis, Frontend Design
> - **Fahruroji:** Database Design, System Analysis, Integration Planning
> - Kolaborasi di semua fase dengan tools: Figma, Google Docs, GitHub

### **H. LIMITASI & FUTURE WORK**

**Q19: Apa keterbatasan penelitian ini?**
> **Jawab:** 
> - Belum implementasi coding (hanya desain lengkap)
> - Validasi hanya desain prototype, bukan sistem running
> - Testing di environment simulasi, bukan production
> - Sample size UAT terbatas (15 responden)

**Q20: Apa rekomendasi pengembangan selanjutnya?**
> **Jawab:** 
> 1. **Implementasi coding** mengikuti desain yang sudah dibuat
> 2. **Integrasi WhatsApp** untuk notifikasi (selain email)
> 3. **Mobile app** (React Native) untuk akses lebih mudah
> 4. **AI chatbot** untuk FAQ otomatis
> 5. **Telemedicine integration** untuk sesi online
> 6. **Analytics dashboard** lebih advanced (predictive)

---

## 💡 **TIPS SAAT PRESENTASI**

### ✅ **DO:**
- Bicara dengan tempo sedang dan jelas
- Tunjukkan antusiasme terhadap proyek
- Gunakan visualisasi slide, jangan baca teks
- Highlight angka-angka kunci (66 maket, SUS 80.5, ROI 13 bulan)
- Siapkan backup answer untuk pertanyaan teknis
- Jaga eye contact dengan audiens
- Jika ada pertanyaan tidak tahu: **"Menarik! Itu bisa jadi pengembangan lanjutan"**

### ❌ **DON'T:**
- Jangan monoton atau membaca slide
- Jangan debat dengan penguji
- Jangan bilang "tidak tahu" tanpa elaborasi
- Jangan terlalu teknis kecuali ditanya detail
- Jangan defensive saat dikritik

---

## 🎤 **SCRIPT PEMBUKAAN**

> "Selamat pagi/siang Bapak/Ibu penguji. Perkenalkan kami tim dari kelas 11.7C.12: Roki Anjas, Susanto, dan Fahruroji. Kami akan mempresentasikan proyek akhir kami berjudul **'CUR-HEART: Inovasi Sistem Informasi Layanan Terapi Mental Berbasis Digital'**.
>
> Di tengah meningkatnya kebutuhan kesehatan mental di Indonesia, CUR-HEART sebagai klinik hipnoterapi menghadapi tantangan operasional karena sistem manual. Penelitian ini menghasilkan **rancangan sistem informasi lengkap** - mulai dari analisis 52 kebutuhan, desain database 16 tabel, hingga 66 maket prototipe yang telah divalidasi dengan skor SUS 80.5 (kategori Excellent).
>
> Mari kita mulai presentasinya."

---

## 🎯 **SCRIPT PENUTUP**

> "Demikian presentasi kami. Penelitian ini berhasil **mencapai seluruh 6 tujuan** dengan hasil melampaui target. Kami menghasilkan blueprint sistem informasi yang siap untuk diimplementasikan, dengan dampak signifikan: peningkatan efisiensi 60%, kapasitas layanan 31%, dan kepuasan pengguna 4.6/5.0.
>
> Terima kasih atas perhatiannya. Kami siap menjawab pertanyaan Bapak/Ibu."

---

**Good luck! 🚀**
