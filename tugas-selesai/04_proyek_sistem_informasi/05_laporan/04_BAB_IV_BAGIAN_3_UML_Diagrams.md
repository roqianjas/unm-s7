# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 3)

## 4.3.4 Diagram UML (*Unified Modeling Language*)

UML (*Unified Modeling Language*) adalah bahasa pemodelan standar yang digunakan untuk memvisualisasikan, menspesifikasikan, membangun, dan mendokumentasikan sistem perangkat lunak. Dalam proyek CUR-HEART, kami menggunakan tiga jenis diagram UML utama untuk menggambarkan struktur dan perilaku sistem.

### A. Diagram Kasus Penggunaan (*Use Case Diagram*)

Diagram Kasus Penggunaan menggambarkan interaksi antara aktor (pengguna sistem) dengan sistem, serta fungsi-fungsi yang dapat dilakukan oleh masing-masing aktor.

---

**[GAMBAR 4.10 - Diagram Kasus Penggunaan (4 Aktor, 30+ Kasus Penggunaan)]** 🔴 **KRITIS**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN DIAGRAM KASUS PENGGUNAAN KOMPREHENSIF]         │
│                                                             │
│   DIAGRAM KASUS PENGGUNAAN SISTEM CUR-HEART                │
│   Notasi Standar UML                                       │
│                                                             │
│   AKTOR (4 Primer + 1 Eksternal):                          │
│                                                             │
│   🚶 Tamu (Pengunjung)                                      │
│   • Melihat halaman utama / layanan                        │
│   • Melihat profil terapis                                 │
│   • Mendaftar akun                                         │
│   • Masuk ke sistem                                        │
│                                                             │
│   👤 Klien (Pelanggan)                                      │
│   • SEMUA kemampuan Tamu +                                 │
│   • Membuat pemesanan (termasuk: pilih layanan, terapis,   │
│     jadwal, pembayaran)                                    │
│   • Melihat janji temu                                     │
│   • Menjadwal ulang/Membatalkan pemesanan                  │
│   • Melihat pelacak kemajuan                               │
│   • Mengirim pesan (obrolan terapis)                       │
│   • Mengirim ulasan                                        │
│   • Mengelola profil                                       │
│                                                             │
│   👨‍⚕️ Terapis (Staf)                                       │
│   • Melihat dasbor terapis                                 │
│   • Mengelola jadwal kerja (ketersediaan)                  │
│   • Memblokir/Membuka blokir tanggal                       │
│   • Melihat janji temu                                     │
│   • Menyelesaikan sesi (menulis catatan terapi)            │
│   • Memperbarui kemajuan klien                             │
│   • Merespons pesan                                        │
│   • Melihat ulasan/penilaian                               │
│   • Mengelola profil & kredensial                          │
│                                                             │
│   👔 Admin (Administrator)                                  │
│   • Melihat dasbor admin                                   │
│   • Mengelola pengguna (CRUD semua peran)                  │
│   • Mengelola terapis (menyetujui/menangguhkan)            │
│   • Mengelola layanan (CRUD)                               │
│   • Mengelola pemesanan (melihat, mengubah, membatalkan)   │
│   • Melihat laporan keuangan                               │
│   • Mengelola pengaturan sistem                            │
│   • Melihat catatan aktivitas                              │
│   • Mengirim pemberitahuan                                 │
│                                                             │
│   💳 Gerbang Pembayaran (Sistem Eksternal)                  │
│   • Memproses pembayaran                                   │
│   • Mengirim konfirmasi pembayaran                         │
│   • Menangani pengembalian dana                            │
│                                                             │
│   RELASI KUNCI:                                             │
│   • <<include>>: Sub-kasus penggunaan wajib                │
│     (mis., Membuat Pemesanan mencakup Pilih Layanan)       │
│   • <<extend>>: Kasus penggunaan opsional                  │
│     (mis., Batalkan Pemesanan memperluas Lihat Janji Temu) │
│   • Generalisasi: Pewarisan                                │
│     (mis., Klien mewarisi kemampuan Tamu)                  │
│                                                             │
│   TOTAL KASUS PENGGUNAAN: 35+                              │
│   • Tamu: 6 kasus penggunaan                               │
│   • Klien: 14 kasus penggunaan (termasuk Tamu)             │
│   • Terapis: 12 kasus penggunaan                           │
│   • Admin: 15 kasus penggunaan                             │
│   • Gerbang Pembayaran: 3 interaksi                        │
│                                                             │
│   ALUR KRITIS:                                              │
│   1. Alur Pemesanan (Klien → Sistem → Gerbang Pembayaran)  │
│   2. Penyelesaian Sesi (Terapis → Catatan Terapi)          │
│   3. Manajemen Pengguna (Admin → operasi CRUD)             │
│                                                             │
│   Format: Diagram Kasus Penggunaan UML PNG                 │
│   Ukuran yang direkomendasikan: 2000x1400px (besar, mudah dibaca) │
│   Gaya: Notasi UML standar dengan figura batang            │
│   Warna: Aktor (luar), Batas sistem (kotak),               │
│          Kasus penggunaan (oval di dalam sistem)            │
│                                                             │
│   File: assets/images/use-case-diagram-complete.png        │
│   Alat: Visual Paradigm, draw.io, StarUML, atau Lucidchart │
│                                                             │
│   PRIORITAS: P1 - KRITIS                                    │
│   Harus menampilkan: Semua aktor, batas sistem, kasus      │
│                      penggunaan, relasi <<include>>/<<extend>> │
│                      dengan jelas                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.10: Diagram Kasus Penggunaan lengkap sistem CUR-HEART dengan 4 aktor, 35+ kasus penggunaan, menampilkan interaksi Tamu/Klien/Terapis/Admin_

---

#### Aktor dalam Sistem CUR-HEART

**1. Tamu (*Guest*)**
- Belum terautentikasi
- Dapat melihat informasi publik

**2. Klien (*Client*)**
- Pengguna terautentikasi dengan peran klien
- Dapat melakukan pemesanan dan mengakses layanan

**3. Terapis (*Therapist*)**
- Pengguna terautentikasi dengan peran terapis
- Mengelola jadwal dan melakukan sesi terapi

**4. Admin (Administrator)**
- Pengguna terautentikasi dengan peran admin
- Mengelola seluruh sistem

**5. Gerbang Pembayaran (*Payment Gateway*)**
- Sistem eksternal untuk pemrosesan pembayaran

**Diagram Kasus Penggunaan Lengkap:**

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    SISTEM INFORMASI CUR-HEART                              │
│                    DIAGRAM KASUS PENGGUNAAN                                │
└────────────────────────────────────────────────────────────────────────────┘

┌──────────┐                                                      ┌──────────┐
│          │                                                      │          │
│   Tamu   │                                                      │  Klien   │
│          │                                                      │          │
└────┬─────┘                                                      └────┬─────┘
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Melihat Halaman Utama                                  │   │
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Melihat Daftar Layanan                                 │◄──┤
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Melihat Detail Layanan                                │◄──┤
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Melihat Profil Terapis                                │◄──┤
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Membaca Artikel Blog                                   │◄──┤
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Registrasi Akun                                        │   │
     │  └────────────────────────────────────────────────────────┘   │
     │                                                                 │
     │  ┌────────────────────────────────────────────────────────┐   │
     ├──┤ Login ke Sistem                                        │◄──┤
     │  └─────────────────────┬──────────────────────────────────┘   │
     │                        │                                       │
     │                        │ <<include>>                           │
     │                        ▼                                       │
     │              ┌──────────────────────┐                          │
     │              │ Verifikasi Email     │                          │
     │              └──────────────────────┘                          │
     │                                                                 │
     │                                                                 │
     │                                                     ┌───────────┴──────┐
     │                                                     │                  │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Melakukan Booking     │     │
     │                                          └──────────┬────────────┘     │
     │                                                     │                  │
     │                                          <<include>>│                  │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Memilih Layanan       │     │
     │                                          └───────────────────────┘     │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Memilih Terapis       │     │
     │                                          └───────────────────────┘     │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Memilih Jadwal        │     │
     │                                          └───────────────────────┘     │
     │                                          ┌──────────▼────────────┐     │
     │                                          │ Melakukan Pembayaran  │◄────┼────┐
     │                                          └───────────────────────┘     │    │
     │                                                     │                  │    │
     │                                          ┌──────────▼────────────┐     │    │
     │                                          │ Melihat Konfirmasi    │     │    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Melihat Appointment   │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Reschedule Booking    │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Cancel Booking        │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Melihat Progress      │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Mengirim Pesan        │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                          ┌───────────────────────┐     │    │
     │                                          │ Memberikan Review     │◄────┤    │
     │                                          └───────────────────────┘     │    │
     │                                                                        │    │
     │                                                                        │    │
┌────┴─────┐                                                                 │    │
│          │                                                                 │    │
│Therapist │                                                                 │    │
│          │                                                                 │    │
└────┬─────┘                                                                 │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Dashboard Terapis                              │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Mengelola Jadwal Kerja                                 │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Mengatur Ketersediaan                                  │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Block/Unblock Tanggal                                  │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Daftar Klien                                   │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Profil Klien                                   │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melakukan Sesi Terapi                                  │          │    │
     │  └─────────────────────┬──────────────────────────────────┘          │    │
     │                        │                                             │    │
     │                        │ <<include>>                                 │    │
     │                        ▼                                             │    │
     │              ┌──────────────────────┐                                │    │
     │              │ Menulis Catatan Sesi │                                │    │
     │              └──────────────────────┘                                │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Riwayat Sesi                                   │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Melihat Laporan Pendapatan                             │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Mengelola Profil                                       │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │  ┌────────────────────────────────────────────────────────┐          │    │
     ├──┤ Membalas Pesan                                         │          │    │
     │  └────────────────────────────────────────────────────────┘          │    │
     │                                                                       │    │
     │                                                                       │    │
┌────┴─────┐                                                                │    │
│          │                                                                │    │
│  Admin   │                                                                │    │
│          │                                                                │    │
└────┬─────┘                                                                │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Melihat Dashboard Admin                                │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Mengelola Users                                        │         │    │
     │  └─────────────────────┬──────────────────────────────────┘         │    │
     │                        │                                            │    │
     │                        │ <<extend>>                                 │    │
     │              ┌─────────▼──────────┐                                 │    │
     │              │ Approve Terapis    │                                 │    │
     │              └────────────────────┘                                 │    │
     │              ┌─────────▼──────────┐                                 │    │
     │              │ Suspend User       │                                 │    │
     │              └────────────────────┘                                 │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Mengelola Layanan                                      │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Mengelola Booking                                      │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Verifikasi Pembayaran Manual                           │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Melihat Laporan Keuangan                               │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Generate Reports                                       │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │  ┌────────────────────────────────────────────────────────┐         │    │
     ├──┤ Konfigurasi Sistem                                     │         │    │
     │  └────────────────────────────────────────────────────────┘         │    │
     │                                                                      │    │
     │                                                                      │    │
     │                                                                      │    │
     │                                                        ┌─────────────┴────┐
     │                                                        │                  │
     │                                                        │ Payment Gateway  │
     │                                                        │                  │
     │                                                        └──────────────────┘
```

**Penjelasan Relasi:**

- **<<include>>**: Kasus penggunaan yang wajib dieksekusi (misal: Pemesanan harus menyertakan Memilih Layanan)
- **<<extend>>**: Kasus penggunaan opsional yang memperluas fungsionalitas (misal: Mengelola Pengguna bisa diperluas dengan Menyetujui Terapis)

---

**Tabel 4.31 Daftar Kasus Penggunaan dengan Aktor**

| ID KP | Nama Kasus Penggunaan | Aktor | Prioritas | Kompleksitas | Deskripsi |
|-------|---------------|----------|----------|------------|-------------|
| **Autentikasi & Otorisasi** | | | | | |
| UC-01 | Registrasi | Tamu | Harus Ada | Rendah | Pengguna mendaftar akun baru (klien atau terapis) |
| UC-02 | Masuk | Semua Pengguna | Harus Ada | Rendah | Pengguna masuk ke sistem dengan email dan kata sandi |
| UC-03 | Keluar | Semua Pengguna | Harus Ada | Rendah | Pengguna keluar dari sistem |
| UC-04 | Lupa Kata Sandi | Tamu | Harus Ada | Sedang | Pengguna meminta atur ulang kata sandi melalui email |
| UC-05 | Atur Ulang Kata Sandi | Tamu | Harus Ada | Sedang | Pengguna mengatur kata sandi baru dengan token |
| UC-06 | Verifikasi Email | Tamu | Sebaiknya Ada | Rendah | Pengguna memverifikasi email setelah registrasi |
| **Kasus Penggunaan Klien** | | | | | |
| UC-07 | Telusuri Layanan | Klien, Tamu | Harus Ada | Rendah | Pengguna menelusuri katalog layanan terapi |
| UC-08 | Lihat Detail Layanan | Klien, Tamu | Harus Ada | Rendah | Pengguna melihat detail lengkap layanan |
| UC-09 | Telusuri Terapis | Klien, Tamu | Harus Ada | Rendah | Pengguna menelusuri direktori terapis |
| UC-10 | Lihat Profil Terapis | Klien, Tamu | Harus Ada | Sedang | Pengguna melihat profil lengkap terapis |
| UC-11 | Cek Ketersediaan Terapis | Klien | Harus Ada | Tinggi | Pengguna mengecek jadwal ketersediaan terapis |
| UC-12 | Buat Pemesanan | Klien | Harus Ada | Tinggi | Pengguna memesan sesi terapi (alur 4 langkah) |
| UC-13 | Lihat Riwayat Pemesanan | Klien | Harus Ada | Sedang | Pengguna melihat riwayat pemesanan |
| UC-14 | Jadwal Ulang Pemesanan | Klien | Sebaiknya Ada | Sedang | Pengguna mengubah jadwal pemesanan (min. 24 jam sebelumnya) |
| UC-15 | Batalkan Pemesanan | Klien | Sebaiknya Ada | Sedang | Pengguna membatalkan pemesanan dengan alasan |
| UC-16 | Lakukan Pembayaran | Klien | Harus Ada | Tinggi | Pengguna membayar pemesanan (transfer/gateway) |
| UC-17 | Unggah Bukti Pembayaran | Klien | Harus Ada | Sedang | Pengguna mengunggah bukti transfer |
| UC-18 | Lihat Ringkasan Catatan Sesi | Klien | Sebaiknya Ada | Sedang | Pengguna melihat ringkasan catatan terapi |
| UC-19 | Lacak Perkembangan | Klien | Sebaiknya Ada | Sedang | Pengguna melihat visualisasi perkembangan terapi |
| UC-20 | Penilaian Mandiri Perkembangan | Klien | Bisa Ada | Rendah | Pengguna memasukkan metrik penilaian mandiri |
| UC-21 | Kirim Ulasan | Klien | Sebaiknya Ada | Sedang | Pengguna mengirim rating dan ulasan setelah sesi |
| UC-22 | Kirim Pesan | Klien | Bisa Ada | Sedang | Pengguna mengirim pesan ke terapis/admin |
| UC-23 | Perbarui Profil | Klien | Harus Ada | Rendah | Pengguna memperbarui informasi profil |
| **Kasus Penggunaan Terapis** | | | | | |
| UC-24 | Lihat Jadwal Temu | Terapis | Harus Ada | Sedang | Terapis melihat jadwal pertemuan |
| UC-25 | Atur Ketersediaan Mingguan | Terapis | Harus Ada | Sedang | Terapis mengatur jam kerja per hari |
| UC-26 | Blokir Tanggal Tertentu | Terapis | Harus Ada | Sedang | Terapis memblokir tanggal (cuti, libur) |
| UC-27 | Terima/Tolak Pemesanan | Terapis | Sebaiknya Ada | Sedang | Terapis menyetujui atau menolak pemesanan |
| UC-28 | Mulai Sesi | Terapis | Harus Ada | Rendah | Terapis menandai sesi telah dimulai |
| UC-29 | Akhiri Sesi | Terapis | Harus Ada | Sedang | Terapis menandai sesi telah selesai |
| UC-30 | Dokumentasi Catatan Sesi | Terapis | Harus Ada | Tinggi | Terapis memasukkan catatan sesi detail |
| UC-31 | Lihat Riwayat Klien | Terapis | Harus Ada | Sedang | Terapis melihat riwayat sesi klien |
| UC-32 | Nilai Perkembangan Klien | Terapis | Sebaiknya Ada | Sedang | Terapis memasukkan penilaian perkembangan |
| UC-33 | Unggah Lampiran Sesi | Terapis | Bisa Ada | Rendah | Terapis mengunggah dokumen pendukung |
| UC-34 | Tanggapi Ulasan | Terapis | Bisa Ada | Rendah | Terapis membalas ulasan klien |
| UC-35 | Lihat Laporan Pendapatan | Terapis | Sebaiknya Ada | Sedang | Terapis melihat laporan pendapatan |
| UC-36 | Perbarui Profil Profesional | Terapis | Harus Ada | Sedang | Terapis memperbarui bio, kredensial, sertifikasi |
| UC-37 | Kelola Layanan yang Ditawarkan | Terapis | Sebaiknya Ada | Rendah | Terapis memilih layanan yang dikuasai |
| **Kasus Penggunaan Admin** | | | | | |
| UC-38 | Lihat Ikhtisar Dasbor | Admin | Harus Ada | Sedang | Admin melihat ringkasan metrik sistem |
| UC-39 | Kelola Pengguna (CRUD) | Admin | Harus Ada | Tinggi | Admin membuat/baca/perbarui/hapus pengguna |
| UC-40 | Setujui Terapis | Admin | Harus Ada | Sedang | Admin memverifikasi dan menyetujui terapis baru |
| UC-41 | Kelola Layanan (CRUD) | Admin | Harus Ada | Sedang | Admin mengelola katalog layanan |
| UC-42 | Lihat Semua Pemesanan | Admin | Harus Ada | Sedang | Admin memantau semua pemesanan |
| UC-43 | Verifikasi Pembayaran Manual | Admin | Harus Ada | Tinggi | Admin menyetujui/menolak bukti pembayaran |
| UC-44 | Buat Laporan Keuangan | Admin | Sebaiknya Ada | Tinggi | Admin mengekspor laporan keuangan |
| UC-45 | Buat Laporan Analitik | Admin | Sebaiknya Ada | Tinggi | Admin mengekspor laporan analitik |
| UC-46 | Moderasi Ulasan | Admin | Sebaiknya Ada | Sedang | Admin menyetujui/menyembunyikan ulasan tidak pantas |
| UC-47 | Kirim Notifikasi Massal | Admin | Bisa Ada | Sedang | Admin mengirim pengumuman ke pengguna |
| UC-48 | Kelola Pengaturan Sistem | Admin | Harus Ada | Sedang | Admin mengubah konfigurasi sistem |
| UC-49 | Lihat Log Audit | Admin | Sebaiknya Ada | Rendah | Admin melihat log aktivitas |
| UC-50 | Cadangkan Basis Data | Admin | Harus Ada | Rendah | Admin memicu pencadangan manual |

**Ringkasan Kasus Penggunaan:**
- **Total Kasus Penggunaan:** 50
- **Harus Ada:** 32 (64%)
- **Sebaiknya Ada:** 14 (28%)
- **Bisa Ada:** 4 (8%)
- **Aktor:** 4 (Tamu, Klien, Terapis, Admin)
- **Kompleksitas Rata-rata:** Sedang

---

### B. Diagram Aktivitas

Diagram Aktivitas menggambarkan alur kerja (*workflow*) dari proses bisnis dalam sistem. Berikut adalah diagram aktivitas untuk proses-proses utama:

---

**[GAMBAR 4.11 - Diagram Aktivitas: Alur Proses Pemesanan]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN DIAGRAM AKTIVITAS - ALUR PEMESANAN]            │
│                                                             │
│   DIAGRAM AKTIVITAS CUR-HEART                              │
│   Proses: Alur Kerja Pemesanan Klien (End-to-End)         │
│                                                             │
│   SWIMLANES (3 Aktor):                                     │
│   ┌──────────────────────────────────────────────┐         │
│   │ KLIEN                                        │         │
│   ├──────────────────────────────────────────────┤         │
│   │ • Mulai (Login)                              │         │
│   │ • Telusuri layanan                           │         │
│   │ • Pilih layanan                              │         │
│   │ • Pilih terapis                              │         │
│   │ • Pilih tanggal & waktu                      │         │
│   │ • Masukkan detail pemesanan                  │         │
│   │ • Lakukan pembayaran                         │         │
│   │ • Terima konfirmasi                          │         │
│   │ • Selesai                                    │         │
│   └──────────────────────────────────────────────┘         │
│                                                             │
│   ┌──────────────────────────────────────────────┐         │
│   │ SISTEM                                       │         │
│   ├──────────────────────────────────────────────┤         │
│   │ • Validasi login                             │         │
│   │ • Ambil daftar layanan                       │         │
│   │ • Validasi pilihan layanan                   │         │
│   │ • Filter terapis berdasarkan layanan         │         │
│   │ • Ambil ketersediaan terapis                 │         │
│   │ • Cek ketersediaan slot (Keputusan)          │         │
│   │ • Buat rekaman pemesanan                     │         │
│   │ • Proses pembayaran (Gateway Pembayaran)     │         │
│   │ • Perbarui status pemesanan                  │         │
│   │ • Kirim notifikasi                           │         │
│   │ • Buat konfirmasi                            │         │
│   └──────────────────────────────────────────────┘         │
│                                                             │
│   ┌──────────────────────────────────────────────┐         │
│   │ GATEWAY PEMBAYARAN                           │         │
│   ├──────────────────────────────────────────────┤         │
│   │ • Terima permintaan pembayaran               │         │
│   │ • Validasi metode pembayaran                 │         │
│   │ • Proses transaksi                           │         │
│   │ • Kembalikan hasil pembayaran (Sukses/Gagal) │         │
│   └──────────────────────────────────────────────┘         │
│                                                             │
│   ELEMEN KUNCI:                                             │
│   • ● (Node awal) - Mulai proses pemesanan                 │
│   • ◉ (Node akhir) - Pemesanan dikonfirmasi / dibatalkan   │
│   • ◇ (Keputusan) - Slot tersedia? Pembayaran sukses?      │
│   • ▭ (Aktivitas) - Setiap aksi/langkah                    │
│   • → (Alur) - Alur berurutan                              │
│   • ━ (Fork/Join) - Aktivitas paralel                      │
│                                                             │
│   TITIK KEPUTUSAN (Kritis):                                 │
│   1. "Apakah slot masih tersedia?"                         │
│      YA → Lanjutkan ke pemesanan                           │
│      TIDAK → Tampilkan error, pilih ulang waktu            │
│                                                             │
│   2. "Apakah pembayaran berhasil?"                         │
│      YA → Konfirmasi pemesanan, kirim notifikasi           │
│      TIDAK → Batalkan pemesanan, tampilkan error           │
│                                                             │
│   ALUR ALTERNATIF:                                          │
│   • Slot tidak tersedia → Loop kembali ke pilihan tanggal  │
│   • Pembayaran gagal → Coba ulang atau batalkan            │
│   • Error validasi → Tampilkan pesan error                 │
│                                                             │
│   TOTAL AKTIVITAS: 20+ node                                │
│   NODE KEPUTUSAN: 3                                        │
│   SWIMLANES: 3 (Klien, Sistem, Gateway Pembayaran)         │
│                                                             │
│   Format: Diagram Aktivitas UML (Swimlane) PNG            │
│   Ukuran rekomendasi: 1800x2400px (vertikal, detail)      │
│   Gaya: Standar UML dengan swimlanes, label jelas         │
│                                                             │
│   File: assets/images/activity-diagram-booking-flow.png    │
│   Tool: Visual Paradigm, draw.io, Lucidchart               │
│                                                             │
│   PRIORITAS: P1 - CRITICAL                                  │
│   Harus menampilkan: Swimlanes, titik keputusan, alur      │
│   positif & negatif                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.11: Diagram Aktivitas untuk proses pemesanan lengkap dengan 3 swimlanes (Klien, Sistem, Gateway Pembayaran), menampilkan titik keputusan dan alur alternatif_

---

#### 1. Diagram Aktivitas: Proses Pemesanan Layanan

```
┌──────────────────────────────────────────────────────────────────────────┐
│            DIAGRAM AKTIVITAS - PROSES PEMESANAN LAYANAN                  │
└──────────────────────────────────────────────────────────────────────────┘

    Klien                   Sistem                     Terapis
      │                       │                            │
      │                       │                            │
     ●─┐                      │                            │
     MULAI                    │                            │
      │                       │                            │
      ├──────────────────────►│                            │
      │   Pilih Layanan       │                            │
      │                       │                            │
      │◄──────────────────────┤                            │
      │  Tampilkan Daftar     │                            │
      │    Layanan            │                            │
      │                       │                            │
      ├──────────────────────►│                            │
      │  Kirim Layanan        │                            │
      │                       │                            │
      │                    ┌──▼───┐                        │
      │                    │Validasi│                       │
      │                    └──┬───┘                        │
      │                       │                            │
      │                    ╱     ╲                         │
      │                   ╱ Valid? ╲                       │
      │                   ╲       ╱                        │
      │                    ╲     ╱                         │
      │                     ╲   ╱                          │
      │              Tidak  ╱ ╲  Ya                        │
      │◄────────────────────┘  └────┐                     │
      │  Pesan Error                │                     │
      │                             ▼                     │
      │                    ┌─────────────────┐            │
      │                    │ Filter Terapis  │            │
      │                    │ per Layanan     │            │
      │                    └────────┬────────┘            │
      │◄────────────────────────────┤                     │
      │  Tampilkan Daftar Terapis   │                     │
      │                             │                     │
      ├─────────────────────────────►                     │
      │  Pilih Terapis              │                     │
      │                             │                     │
      │                    ┌────────▼────────┐            │
      │                    │ Ambil           │            │
      │                    │ Ketersediaan    │            │
      │                    │ Terapis         │            │
      │                    └────────┬────────┘            │
      │◄────────────────────────────┤                     │
      │  Tampilkan Kalender         │                     │
      │                             │                     │
      ├─────────────────────────────►                     │
      │  Pilih Tanggal & Waktu      │                     │
      │                             │                     │
      │                    ┌────────▼────────┐            │
      │                    │ Cek Konflik     │            │
      │                    └────────┬────────┘            │
      │                             │                     │
      │                          ╱     ╲                  │
      │                         ╱Konflik?╲               │
      │                         ╲       ╱                 │
      │                          ╲     ╱                  │
      │                 Ya       ╲   ╱   Tidak            │
      │◄──────────────────────────┘  └───┐               │
      │  Slot Tidak Tersedia             │               │
      │                                  ▼               │
      │                         ┌─────────────────┐      │
      │                         │ Buat Pemesanan  │      │
      │                         │   (Tertunda)    │      │
      │                         └────────┬────────┘      │
      │◄─────────────────────────────────┤               │
      │  Tampilkan Ringkasan Pemesanan   │               │
      │                                  │               │
      ├──────────────────────────────────►               │
      │  Konfirmasi & Bayar              │               │
      │                                  │               │
      │                         ┌────────▼────────┐      │
      │                         │ Proses Pembayaran│      │
      │                         └────────┬────────┘      │
      │                                  │               │
      │                               ╱     ╲            │
      │                              ╱Berhasil?╲         │
      │                              ╲       ╱           │
      │                               ╲     ╱            │
      │              Tidak             ╲   ╱  Ya         │
      │                        ┌────────┘  └─────┐       │
      │                        │                 │       │
      │               ┌────────▼─────┐  ┌────────▼──────┐│
      │               │Batalkan      │  │Perbarui       ││
      │               │Pemesanan     │  │Pemesanan      ││
      │               │              │  │(Dikonfirmasi) ││
      │               └──────┬───────┘  └────────┬──────┘│
      │◄──────────────────────┤                  │       │
      │  Pembayaran Gagal     │                  │       │
      │                       │         ┌────────▼──────┐│
      │                       │         │Kirim Email    ││
      │                       │         │Notifikasi     ││
      │                       │         └────────┬──────┘│
      │                       │                  │       │
      │                       │                  ├───────┼───────────►
      │                       │                  │  Email ke Terapis
      │                       │                  │       │
      │◄──────────────────────┴──────────────────┤       │
      │  Konfirmasi Pemesanan                    │       │
      │                                          │       │
     ─┴─                                         │       │
   SELESAI                                       │       │
                                                 │       │
                                            ┌────▼───┐   │
                                            │Notifikasi  │
                                            │Pemesanan   │
                                            │Baru        │
                                            └────────┘   │
                                                 │       │
                                                ●─┴─     │
                                             SELESAI     │
```

**Keterangan:**
- **●** : Titik Mulai/Selesai
- **╱ ╲** : Titik Keputusan/percabangan
- **┌──┐** : Aktivitas/proses
- **→** : Arah alur

**Proses:**
1. Klien memilih layanan dari katalog
2. Sistem memfilter terapis yang menyediakan layanan tersebut
3. Klien memilih terapis
4. Sistem menampilkan kalender ketersediaan
5. Klien memilih tanggal dan waktu
6. Sistem mengecek konflik dengan pemesanan lain
7. Jika tersedia, buat pemesanan dengan status "tertunda"
8. Klien melakukan pembayaran
9. Jika pembayaran berhasil:
   - Perbarui status pemesanan menjadi "dikonfirmasi"
   - Kirim notifikasi email ke klien dan terapis
10. Jika pembayaran gagal:
    - Batalkan pemesanan
    - Tampilkan pesan error

---

#### 2. Diagram Aktivitas: Proses Pelaksanaan Sesi Terapi

```
┌──────────────────────────────────────────────────────────────────────────┐
│         DIAGRAM AKTIVITAS - PELAKSANAAN SESI TERAPI                      │
└──────────────────────────────────────────────────────────────────────────┘

    Terapis                Sistem                    Klien
      │                      │                          │
      │                      │                          │
     ●─┐                     │                          │
   MULAI                     │                          │
      │                      │                          │
      │              ┌───────▼───────┐                  │
      │              │ Email         │                  │
      │              │ Pengingat H-1 │                  │
      │              └───────┬───────┘                  │
      │                      │                          │
      │◄─────────────────────┼──────────────────────────┤
      │  Terima Pengingat    │  Terima Pengingat        │
      │                      │                          │
      │              ┌───────▼───────┐                  │
      │              │Hari Sesi      │                  │
      │              │Cek Waktu      │                  │
      │              └───────┬───────┘                  │
      │                      │                          │
      │                   ╱     ╲                       │
      │                  ╱ Waktu   ╲                    │
      │                  ╲  mulai? ╱                    │
      │                   ╲       ╱                     │
      │       Tidak        ╲     ╱  Ya                  │
      │          ┌──────────┘   └─────────┐             │
      │          │                        │             │
      │          │ Tunggu                 ▼             │
      │          └───────────►   ┌────────────────┐     │
      │                         │Aktifkan Tombol │     │
      │                         │"Gabung Sesi"   │     │
      │                         └────────┬────────┘     │
      │                                  │             │
      │◄─────────────────────────────────┼─────────────┤
      │    Link Gabung Sesi              │  Link Gabung Sesi
      │                                  │             │
      ├──────────────────────────────────►            │
      │    Klik "Gabung Sesi"            │             │
      │                                  │             │
      │                         ┌────────▼────────┐    │
      │                         │Buat Rekaman     │    │
      │                         │Sesi             │    │
      │                         └────────┬────────┘    │
      │                                  │             │
      │                         ┌────────▼────────┐    │
      │                         │Buka Ruang Sesi  │    │
      │                         │(Panggilan Video)│    │
      │                         └────────┬────────┘    │
      │◄─────────────────────────────────┼─────────────┤
      │    Antarmuka Ruang Sesi          │  Antarmuka Ruang Sesi
      │                                  │             │
      ├──────────────────────────────────┼─────────────►
      │    Mulai Panggilan Video         │  Gabung Panggilan Video
      │                                  │             │
      ├──────────────────────────────────┼─────────────►
      │◄─────────────────────────────────┼─────────────┤
      │    Streaming Video & Audio       │  Streaming Video & Audio
      │                                  │             │
      ├──────────────────────────────────►            │
      │    Laksanakan Terapi             │             │
      │    (Diskusi, Hipnosis, dll)      │             │
      │                                  │             │
      │    ┌─────────────────┐           │             │
      │    │ Buat Catatan    │           │             │
      │    │ (Real-time)     │           │             │
      │    └────────┬────────┘           │             │
      │             │                    │             │
      │    ┌────────▼────────┐           │             │
      │───►│ Simpan Otomatis │           │             │
      │    │ Setiap 2 menit  │           │             │
      │    └─────────────────┘           │             │
      │                                  │             │
      │                               ╱     ╲          │
      │                              ╱  Sesi  ╲        │
      │                              ╲ Selesai?╱       │
      │                               ╲       ╱        │
      │          Tidak                 ╲     ╱  Ya     │
      │          ┌─────────────────────┘   └──────┐   │
      │          │ Lanjutkan                      │   │
      │          └───────────►                    │   │
      │                                           ▼   │
      ├───────────────────────────────────────────►   │
      │    Akhiri Panggilan Video                 │   │
      │                                           │   │
      │                              ┌────────────▼───┤
      │                              │Rekam Waktu     │
      │                              │Selesai         │
      │                              │Perbarui Durasi │
      │                              └────────────┬───┘
      │                                           │   │
      │◄──────────────────────────────────────────┤   │
      │   Alihkan ke Halaman Catatan Sesi         │   │
      │                                           │   │
      ├───────────────────────────────────────────►   │
      │   Lengkapi Catatan Sesi                   │   │
      │   (Kondisi, Teknik,                       │   │
      │    Kemajuan, Rekomendasi)                 │   │
      │                                           │   │
      │                              ┌────────────▼───┤
      │                              │ Simpan Catatan │
      │                              │ Tandai Sesi    │
      │                              │ Selesai        │
      │                              └────────────┬───┘
      │                                           │   │
      │                              ┌────────────▼───┤
      │                              │ Perbarui Skor  │
      │                              │ Kemajuan Klien │
      │                              └────────────┬───┘
      │                                           │   │
      │                              ┌────────────▼───┤
      │                              │Kirim Email     │
      │                              │Tindak Lanjut & │
      │                              │Minta Ulasan    │
      │                              └────────────┬───┘
      │                                           │   │
      │◄──────────────────────────────────────────┼───┤
      │    Notifikasi Berhasil                    │ Notifikasi Email
      │                                           │   │
     ─┴─                                          │  ●─┴─
   SELESAI                                        │ SELESAI
                                                  │
```

**Proses:**
1. Sistem mengirim email pengingat H-1 ke klien dan terapis
2. Pada hari H, sistem mengecek waktu sesi
3. 15 menit sebelum sesi, aktifkan tombol "Gabung Sesi"
4. Klien dan terapis bergabung ke ruang sesi
5. Terapis memulai panggilan video
6. Laksanakan sesi terapi dengan panggilan video
7. Terapis membuat catatan real-time (simpan otomatis setiap 2 menit)
8. Setelah sesi selesai, akhiri panggilan video
9. Sistem merekam waktu selesai dan menghitung durasi
10. Terapis melengkapi catatan sesi
11. Sistem memperbarui skor kemajuan klien
12. Kirim email tindak lanjut dan minta ulasan

---

#### 3. Diagram Aktivitas: Proses Verifikasi Pembayaran Manual (Admin)

```
┌──────────────────────────────────────────────────────────────────────────┐
│      DIAGRAM AKTIVITAS - VERIFIKASI PEMBAYARAN MANUAL (ADMIN)           │
└──────────────────────────────────────────────────────────────────────────┘

    Klien                   Sistem                     Admin
      │                       │                          │
      │                       │                          │
     ●─┐                      │                          │
   MULAI                      │                          │
      │                       │                          │
      ├──────────────────────►│                          │
      │  Pilih Metode         │                          │
      │  Transfer Bank        │                          │
      │                       │                          │
      │◄──────────────────────┤                          │
      │  Tampilkan Info       │                          │
      │  Rekening Bank &      │                          │
      │  Instruksi            │                          │
      │                       │                          │
      ├──────────────────────►│                          │
      │  Konfirmasi Pesanan   │                          │
      │                       │                          │
      │              ┌────────▼────────┐                 │
      │              │Buat Pemesanan   │                 │
      │              │Status: Menunggu │                 │
      │              │Pembayaran       │                 │
      │              └────────┬────────┘                 │
      │◄──────────────────────┤                          │
      │  Nomor Pemesanan &    │                          │
      │  Instruksi Pembayaran │                          │
      │                       │                          │
      ├──────────────────────►│                          │
      │  Transfer ke Bank     │                          │
      │                       │                          │
      ├──────────────────────►│                          │
      │  Unggah Bukti         │                          │
      │  Pembayaran (Foto)    │                          │
      │                       │                          │
      │              ┌────────▼────────┐                 │
      │              │Simpan File Bukti│                 │
      │              │Perbarui Status  │                 │
      │              │Pembayaran:      │                 │
      │              │Sedang Diproses  │                 │
      │              └────────┬────────┘                 │
      │                       │                          │
      │              ┌────────▼────────┐                 │
      │              │Notifikasi Admin │                 │
      │              │(Email + Sistem) │                 │
      │              └────────┬────────┘                 │
      │                       │                          │
      │                       ├──────────────────────────►
      │                       │  Pembayaran Baru untuk   │
      │                       │  Diverifikasi            │
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Akses Panel Admin │
      │                       │              │Laporan Keuangan  │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Lihat Daftar      │
      │                       │              │Pembayaran        │
      │                       │              │Tertunda          │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Klik Pembayaran   │
      │                       │              │untuk Diverifikasi│
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Lihat Detail:     │
      │                       │              │- Info Pemesanan  │
      │                       │              │- Jumlah          │
      │                       │              │- Bukti Pembayaran│
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Unduh & Cek       │
      │                       │              │Gambar Bukti      │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │              ┌───────────▼──────┐
      │                       │              │Cek Rekening Bank │
      │                       │              │(via Mobile Bank) │
      │                       │              └───────────┬──────┘
      │                       │                          │
      │                       │                       ╱     ╲
      │                       │                      ╱Pembayaran╲
      │                       │                      ╲  Valid?  ╱
      │                       │                       ╲       ╱
      │                       │          Tidak         ╲     ╱  Ya
      │                       │              ┌──────────┘   └────────┐
      │                       │              │                       │
      │                       │    ┌─────────▼─────┐     ┌──────────▼────┐
      │                       │    │Tolak Pembayaran│    │Setujui         │
      │                       │    │               │     │Pembayaran      │
      │                       │    │Masukkan Alasan│     │Masukkan No.Ref│
      │                       │    └─────────┬─────┘     └──────────┬────┘
      │                       │              │                       │
      │                       │    ┌─────────▼─────┐     ┌──────────▼────┐
      │                       │◄───┤Perbarui Status│     │Perbarui Status │
      │                       │    │Pembayaran:    │     │Pembayaran:     │
      │                       │    │Gagal          │     │Selesai         │
      │                       │    └─────────┬─────┘     └──────────┬────┘
      │                       │              │                       │
      │                       │    ┌─────────▼─────┐     ┌──────────▼────┐
      │                       │◄───┤Kirim Email:   │     │Kirim Email:    │
      │                       │    │Pembayaran     │     │Pembayaran      │
      │                       │    │Ditolak        │     │Dikonfirmasi    │
      │                       │    └─────────┬─────┘     └──────────┬────┘
      │                       │              │                       │
      │◄──────────────────────┼──────────────┴───────────────────────┘
      │  Notifikasi Email     │
      │                       │
      │                    ╱     ╲
      │                   ╱Disetujui?╲
      │                   ╲       ╱
      │       Tidak        ╲     ╱  Ya
      │          ┌──────────┘   └──────┐
      │          │                     │
      │    ┌─────▼─────┐      ┌────────▼────┐
      │    │Unggah Ulang│     │Pemesanan    │
      │    │Bukti atau  │     │Dikonfirmasi │
      │    │Minta       │     └────────┬────┘
      │    │Pengembalian│              │
      │    │Dana        │     ┌────────▼────┐
      │    └─────┬─────┘      │Kirim Undangan│
      │          │            │Kalender (.ics)│
      │          │            └────────┬────┘
      │          │                     │
      │          │◄────────────────────┤
      │          │   File Kalender     │
      │          │                     │
     ─┴──────────┴─                   ─┴─
   SELESAI     SELESAI              SELESAI
```

**Proses:**
1. Klien memilih transfer bank sebagai metode pembayaran
2. Sistem menampilkan detail rekening bank dan instruksi
3. Klien mentransfer dana ke rekening bank CUR-HEART
4. Klien mengunggah bukti pembayaran (foto)
5. Sistem menyimpan file dan memperbarui status pembayaran ke "sedang diproses"
6. Sistem memberitahu admin ada pembayaran baru untuk diverifikasi
7. Admin mengakses panel laporan keuangan
8. Admin melihat daftar pembayaran tertunda
9. Admin mengklik pembayaran tertentu untuk diverifikasi
10. Admin mengecek gambar bukti pembayaran
11. Admin melakukan cek silang dengan riwayat transaksi mobile banking
12. Jika valid:
    - Admin menyetujui pembayaran
    - Masukkan nomor referensi
    - Perbarui status pembayaran ke "selesai"
    - Perbarui status pemesanan ke "dikonfirmasi"
    - Kirim email konfirmasi ke klien
    - Kirim undangan kalender (file .ics)
13. Jika tidak valid:
    - Admin menolak pembayaran
    - Masukkan alasan penolakan
    - Perbarui status pembayaran ke "gagal"
    - Kirim email penolakan ke klien
    - Klien bisa mengunggah ulang bukti atau minta pengembalian dana

---

### C. Diagram Sekuens

Diagram Sekuens menggambarkan interaksi antar objek dalam sistem berdasarkan urutan waktu. Berikut adalah diagram sekuens untuk kasus penggunaan kritis:

---

**[GAMBAR 4.12 - Diagram Sekuens: Interaksi Proses Pemesanan]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN DIAGRAM SEKUENS - PROSES PEMESANAN]            │
│                                                             │
│   DIAGRAM SEKUENS CUR-HEART                                │
│   Skenario: Klien Melakukan Pemesanan (Alur Positif)       │
│                                                             │
│   OBJEK/LIFELINE (7):                                      │
│   1. Klien (Aktor)                                         │
│   2. Peramban (UI)                                         │
│   3. BookingController (Kontroler Laravel)                 │
│   4. BookingService (Logika Bisnis)                        │
│   5. TherapistModel (Akses Data)                           │
│   6. PaymentGateway (API Eksternal)                        │
│   7. Database (MySQL)                                      │
│                                                             │
│   ALUR PESAN (Berurutan):                                  │
│                                                             │
│   Klien → Peramban                                         │
│   1. "Klik Pesan Sekarang"                                 │
│                                                             │
│   Peramban → BookingController                             │
│   2. "GET /booking/create"                                 │
│   3. ← Kembalikan formulir pemesanan                       │
│                                                             │
│   Klien → Peramban                                         │
│   4. "Isi formulir & Kirim"                                │
│                                                             │
│   Peramban → BookingController                             │
│   5. "POST /booking/store" (service_id, therapist_id,      │
│       date, time)                                          │
│                                                             │
│   BookingController → BookingService                       │
│   6. "validateBooking(data)"                               │
│                                                             │
│   BookingService → TherapistModel                          │
│   7. "checkAvailability(therapist_id, date, time)"         │
│                                                             │
│   TherapistModel → Database                                │
│   8. "SELECT * FROM therapist_availability WHERE..."       │
│   9. ← Kembalikan data ketersediaan                        │
│                                                             │
│   (Keputusan: Jika tersedia)                               │
│                                                             │
│   BookingService → Database                                │
│   10. "INSERT INTO bookings (...)"                         │
│   11. ← Kembalikan booking_id                              │
│                                                             │
│   BookingController → PaymentGateway                       │
│   12. "createPayment(booking_id, amount)"                  │
│   13. ← Kembalikan payment_url                             │
│                                                             │
│   BookingController → Peramban                             │
│   14. ← Alihkan ke payment_url                             │
│                                                             │
│   Peramban → PaymentGateway                                │
│   15. "Selesaikan pembayaran (halaman Midtrans)"           │
│   16. ← Callback pembayaran berhasil                       │
│                                                             │
│   PaymentGateway → BookingController                       │
│   17. "POST /payment/callback" (transaction_status)        │
│                                                             │
│   BookingController → Database                             │
│   18. "UPDATE bookings SET status='confirmed'"             │
│   19. "INSERT INTO payments (...)"                         │
│   20. ← Berhasil                                           │
│                                                             │
│   BookingController → Peramban                             │
│   21. ← Kembalikan halaman konfirmasi                      │
│                                                             │
│   FITUR KUNCI:                                             │
│   • Panggilan sinkron (panah solid →)                      │
│   • Pesan kembali (panah putus-putus ←)                    │
│   • Kotak aktivasi (persegi vertikal pada lifeline)        │
│   • Frame ALT (alur alternatif untuk error)                │
│   • Frame OPT (interaksi payment gateway opsional)         │
│                                                             │
│   TOTAL PESAN: 21                                          │
│   TITIK KEPUTUSAN: 1 (pengecekan ketersediaan)             │
│   SISTEM EKSTERNAL: 1 (Payment Gateway)                    │
│                                                             │
│   Format: Diagram Sekuens UML PNG                          │
│   Ukuran rekomendasi: 2000x1600px (horizontal, lebar)      │
│   Gaya: Standar UML dengan lifeline, kotak aktivasi        │
│                                                             │
│   File: assets/images/sequence-diagram-booking.png         │
│   Tool: Visual Paradigm, draw.io, PlantUML, Lucidchart    │
│                                                             │
│   PRIORITAS: P1 - CRITICAL                                 │
│   Harus menampilkan: Semua objek, nomor urut pesan,        │
│                     pesan kembali, periode aktivasi         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.12: Diagram Sekuens untuk proses pemesanan dengan 7 objek/lifeline, 21 pesan, menampilkan interaksi antara Klien, Peramban, Kontroler, Layanan, Model, Payment Gateway, dan Basis Data_

---

#### 1. Diagram Sekuens: Autentikasi Pengguna (Login)

```
┌──────────────────────────────────────────────────────────────────────────┐
│            DIAGRAM SEKUENS - AUTENTIKASI PENGGUNA                        │
└──────────────────────────────────────────────────────────────────────────┘

Klien     Peramban       LoginController    AuthMiddleware    UserModel    Database
  │             │                 │                │                │            │
  │   Buka      │                 │                │                │            │
  │ Halaman     │                 │                │                │            │
  │  Login      │                 │                │                │            │
  ├────────────►│                 │                │                │            │
  │             │   GET /login    │                │                │            │
  │             ├────────────────►│                │                │            │
  │             │                 │                │                │            │
  │             │  Kembalikan View│                │                │            │
  │             │◄────────────────┤                │                │            │
  │             │                 │                │                │            │
  │◄────────────┤                 │                │                │            │
  │ Tampilkan   │                 │                │                │            │
  │  Formulir   │                 │                │                │            │
  │  Login      │                 │                │                │            │
  │             │                 │                │                │            │
  │   Masukkan  │                 │                │                │            │
  │ Kredensial  │                 │                │                │            │
  │ (Email +    │                 │                │                │            │
  │  Password)  │                 │                │                │            │
  │             │                 │                │                │            │
  │   Kirim     │                 │                │                │            │
  │  Formulir   │                 │                │                │            │
  ├────────────►│                 │                │                │            │
  │             │ POST /login     │                │                │            │
  │             │ {email,password}│                │                │            │
  │             ├────────────────►│                │                │            │
  │             │                 │                │                │            │
  │             │                 │  Validasi CSRF Token            │            │
  │             │                 ├────────────────►                │            │
  │             │                 │                │                │            │
  │             │                 │    Valid       │                │            │
  │             │                 │◄────────────────                │            │
  │             │                 │                │                │            │
  │             │                 │  Validasi Input                 │            │
  │             │                 │  (format email,│                │            │
  │             │                 │   diperlukan)  │                │            │
  │             │                 │                │                │            │
  │             │                 │  Cari Pengguna berdasarkan Email│            │
  │             │                 ├─────────────────────────────────►           │
  │             │                 │                │                │            │
  │             │                 │                │ SELECT * FROM users        │
  │             │                 │                │  WHERE email = ?           │
  │             │                 │                │                ├───────────►
  │             │                 │                │                │            │
  │             │                 │                │   Data Pengguna│            │
  │             │                 │                │◄───────────────┼────────────┤
  │             │                 │                │                │            │
  │             │                 │   Objek Pengguna                │            │
  │             │                 │◄─────────────────────────────────           │
  │             │                 │                │                │            │
  │             │                 │  Cek apakah Pengguna Ada        │            │
  │             │                 │                │                │            │
  │             │                 │ ╔═════════════════════════════╗ │            │
  │             │                 │ ║  Alt [Pengguna Tidak        ║ │            │
  │             │                 │ ║       Ditemukan]            ║ │            │
  │             │                 │ ╠═════════════════════════════╣ │            │
  │             │                 │ ║  Kembalikan Error           ║ │            │
  │             │                 │ ║  "Kredensial Tidak Valid"   ║ │            │
  │             │   Error 401     │ ╚═════════════════════════════╝ │            │
  │             │◄────────────────┤                │                │            │
  │◄────────────┤                 │                │                │            │
  │  Tampilkan  │                 │                │                │            │
  │  Pesan      │                 │                │                │            │
  │  Error      │                 │                │                │            │
  │             │                 │ ╔═════════════════════════════╗ │            │
  │             │                 │ ║  Alt [Pengguna Ditemukan]   ║ │            │
  │             │                 │ ╠═════════════════════════════╣ │            │
  │             │                 │ ║  Verifikasi Hash Password   ║ │            │
  │             │                 │ ║  (bcrypt compare)           ║ │            │
  │             │                 │ ╚══════════════╦══════════════╝ │            │
  │             │                 │                ▼                │            │
  │             │                 │  ╔═══════════════════════════╗  │            │
  │             │                 │  ║ Alt [Password Tidak Cocok]║  │            │
  │             │                 │  ╠═══════════════════════════╣  │            │
  │             │                 │  ║ Kembalikan Error          ║  │            │
  │             │                 │  ║ "Kredensial Tidak Valid"  ║  │            │
  │             │   Error 401     │  ╚═══════════════════════════╝  │            │
  │             │◄────────────────┤                │                │            │
  │◄────────────┤                 │                │                │            │
  │  Tampilkan  │                 │                │                │            │
  │  Error      │                 │                │                │            │
  │             │                 │  ╔═══════════════════════════╗  │            │
  │             │                 │  ║ Alt [Password Cocok]      ║  │            │
  │             │                 │  ╠═══════════════════════════╣  │            │
  │             │                 │  ║ Cek Status Pengguna       ║  │            │
  │             │                 │  ║ (aktif/nonaktif/suspend)  ║  │            │
  │             │                 │  ╚═══════════╦═══════════════╝  │            │
  │             │                 │              ▼                  │            │
  │             │                 │  ╔═══════════════════════════╗  │            │
  │             │                 │  ║ Alt [Status != aktif]     ║  │            │
  │             │                 │  ╠═══════════════════════════╣  │            │
  │             │                 │  ║ Kembalikan Error          ║  │            │
  │             │                 │  ║ "Akun ditangguhkan/       ║  │            │
  │             │                 │  ║  tidak aktif"             ║  │            │
  │             │   Error 403     │  ╚═══════════════════════════╝  │            │
  │             │◄────────────────┤                │                │            │
  │◄────────────┤                 │                │                │            │
  │             │                 │  ╔═══════════════════════════╗  │            │
  │             │                 │  ║ Alt [Status = aktif]      ║  │            │
  │             │                 │  ╠═══════════════════════════╣  │            │
  │             │                 │  ║ Buat Sesi                 ║  │            │
  │             │                 │  ║ (Laravel Session)         ║  │            │
  │             │                 │  ╚═══════════════════════════╝  │            │
  │             │                 │                │                │            │
  │             │                 │  Simpan ID Pengguna di Sesi     │            │
  │             │                 │                │                │            │
  │             │                 │  Buat Token Sesi                │            │
  │             │                 │                │                │            │
  │             │                 │  Perbarui last_login            │            │
  │             │                 ├─────────────────────────────────►           │
  │             │                 │                │                │            │
  │             │                 │                │  UPDATE users  │            │
  │             │                 │                │  SET last_login = NOW()    │
  │             │                 │                │  WHERE id = ?  ├───────────►
  │             │                 │                │                │            │
  │             │                 │                │   Berhasil     │            │
  │             │                 │◄─────────────────────────────────┼────────────┤
  │             │                 │                │                │            │
  │             │                 │  Log Aktivitas │                │            │
  │             │                 │  "Pengguna X masuk"             │            │
  │             │                 │                │                │            │
  │             │                 │  Alihkan Berdasarkan Peran      │            │
  │             │                 │  - Klien → /client/dashboard    │            │
  │             │                 │  - Terapis → /therapist/dash    │            │
  │             │                 │  - Admin → /admin/dashboard     │            │
  │             │                 │                │                │            │
  │             │   Redirect 302  │                │                │            │
  │             │◄────────────────┤                │                │            │
  │             │                 │                │                │            │
  │◄────────────┤                 │                │                │            │
  │   Navigasi  │                 │                │                │            │
  │     ke      │                 │                │                │            │
  │  Dasbor     │                 │                │                │            │
  │             │                 │                │                │            │
```

**Objek yang Terlibat:**
- **Klien**: Pengguna akhir (browser)
- **Peramban**: User agent
- **LoginController**: Kontroler yang menangani logika login
- **AuthMiddleware**: Middleware untuk autentikasi dan otorisasi
- **UserModel**: Model Eloquent untuk data pengguna
- **Database**: Basis data MySQL

**Proses:**
1. Klien membuka halaman login (GET request)
2. Server mengembalikan tampilan formulir login
3. Pengguna memasukkan kredensial (email + password)
4. Kirim formulir (POST request)
5. Sistem memvalidasi CSRF token
6. Sistem memvalidasi format input
7. Sistem melakukan kueri basis data untuk mencari pengguna berdasarkan email
8. Sistem mengecek apakah pengguna ada
9. Sistem memverifikasi password menggunakan bcrypt
10. Sistem mengecek status akun pengguna
11. Jika semua valid:
    - Buat sesi
    - Simpan ID pengguna dalam sesi
    - Buat token sesi (cookie)
    - Perbarui timestamp last_login
    - Log aktivitas
    - Alihkan ke dasbor sesuai peran
12. Jika ada error (kredensial tidak valid, akun ditangguhkan, dll):
    - Kembalikan pesan error
    - Alihkan kembali ke formulir login

---

### D. Diagram Kelas

Diagram Kelas menggambarkan struktur statis sistem, menunjukkan kelas-kelas, atribut, metode, dan hubungan antar kelas.

---

**[GAMBAR 4.13 - Diagram Kelas (Arsitektur MVC Laravel)]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [SISIPKAN DIAGRAM KELAS - LARAVEL MVC]                   │
│                                                             │
│   DIAGRAM KELAS CUR-HEART                                  │
│   Arsitektur MVC Laravel 10.x                              │
│                                                             │
│   KELAS UTAMA (15 Kelas Inti):                             │
│                                                             │
│   MODEL (Eloquent - Lapisan Data):                         │
│   ┌─────────────────────────┐                              │
│   │ User                    │                              │
│   ├─────────────────────────┤                              │
│   │ - id: int               │                              │
│   │ - name: string          │                              │
│   │ - email: string         │                              │
│   │ - password: string      │                              │
│   │ - role: enum            │                              │
│   ├─────────────────────────┤                              │
│   │ + therapist(): HasOne   │                              │
│   │ + client(): HasOne      │                              │
│   │ + notifications(): HasMany                             │
│   └─────────────────────────┘                              │
│              △                                              │
│              │ (mewarisi)                                   │
│     ┌────────┴────────┐                                    │
│     │                 │                                    │
│   ┌─▼──────────┐  ┌──▼─────────┐                          │
│   │ Therapist  │  │  Client    │                          │
│   ├────────────┤  ├────────────┤                          │
│   │ - user_id  │  │ - user_id  │                          │
│   │ - creds    │  │ - dob      │                          │
│   │ - bio      │  │ - address  │                          │
│   ├────────────┤  ├────────────┤                          │
│   │ +services()│  │ +bookings()│                          │
│   │ +bookings()│  │ +progress()│                          │
│   │ +reviews() │  │ +reviews() │                          │
│   └────────────┘  └────────────┘                          │
│                                                             │
│   ┌─────────────────────────┐                              │
│   │ Booking                 │                              │
│   ├─────────────────────────┤                              │
│   │ - id: int               │                              │
│   │ - booking_number: string│                              │
│   │ - client_id: FK         │                              │
│   │ - therapist_id: FK      │                              │
│   │ - service_id: FK        │                              │
│   │ - booking_date: date    │                              │
│   │ - status: enum          │                              │
│   ├─────────────────────────┤                              │
│   │ + client(): BelongsTo   │                              │
│   │ + therapist(): BelongsTo│                              │
│   │ + service(): BelongsTo  │                              │
│   │ + payment(): HasOne     │                              │
│   │ + therapyNote(): HasOne │                              │
│   └─────────────────────────┘                              │
│                                                             │
│   CONTROLLERS (Business Logic):                            │
│   ┌─────────────────────────┐                              │
│   │ BookingController       │                              │
│   ├─────────────────────────┤                              │
│   │ + index(): View         │                              │
│   │ + create(): View        │                              │
│   │ + store(Request): Redirect                             │
│   │ + show(id): View        │                              │
│   │ + update(Request): Redirect                            │
│   │ + destroy(id): Redirect │                              │
│   └─────────────────────────┘                              │
│              │ (uses)                                       │
│              ▼                                              │
│   ┌─────────────────────────┐                              │
│   │ BookingService          │                              │
│   ├─────────────────────────┤                              │
│   │ + validateBooking()     │                              │
│   │ + checkAvailability()   │                              │
│   │ + createBooking()       │                              │
│   │ + cancelBooking()       │                              │
│   │ + sendNotification()    │                              │
│   └─────────────────────────┘                              │
│                                                             │
│   KEY RELATIONSHIPS:                                        │
│   • Inheritance: User ─△─ Therapist/Client                 │
│   • Association: Booking ──→ Client/Therapist/Service      │
│   • Composition: Booking ◆──→ Payment (strong ownership)   │
│   • Aggregation: Therapist ◇──→ Services (weak ownership)  │
│   • Dependency: Controller - - → Service (uses)            │
│                                                             │
│   MULTIPLICITY:                                             │
│   • User 1 ──→ 1 Therapist/Client                          │
│   • Therapist 1 ──→ * Bookings                             │
│   • Client 1 ──→ * Bookings                                │
│   • Booking * ──→ 1 Service                                │
│   • Therapist * ──→ * Services (many-to-many via pivot)    │
│                                                             │
│   TOTAL CLASSES: 15                                         │
│   • Models: 10 (User, Therapist, Client, Booking,          │
│     Service, Payment, TherapyNote, Review, etc.)            │
│   • Controllers: 5 (Booking, Auth, Therapist, etc.)        │
│   • Services: 3 (BookingService, PaymentService, etc.)     │
│                                                             │
│   Format: UML Class Diagram PNG                            │
│   Recommended size: 2400x1800px (large, detailed)          │
│   Style: UML standard dengan visibility modifiers          │
│   Notation: + public, - private, # protected               │
│                                                             │
│   File: assets/images/class-diagram-laravel-mvc.png        │
│   Tool: Visual Paradigm, StarUML, draw.io, PlantUML       │
│                                                             │
│   PRIORITY: P1 - CRITICAL                                   │
│   Must show: All core classes, attributes, methods,        │
│              relationships with multiplicity clearly        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.13: Class Diagram sistem CUR-HEART menggunakan Laravel MVC architecture, showing 15 core classes dengan relationships (inheritance, association, composition) dan multiplicity_

---

### E. Component Architecture Diagram

Component Architecture menggambarkan struktur high-level sistem, menunjukkan komponen-komponen utama dan bagaimana mereka berinteraksi.

---

**[GAMBAR 4.14 - Component Architecture Diagram]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT COMPONENT ARCHITECTURE DIAGRAM]                  │
│                                                             │
│   CUR-HEART SYSTEM ARCHITECTURE                            │
│   3-Tier Architecture (Presentation, Business, Data)       │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │ PRESENTATION LAYER (Client-Side)                    │  │
│   ├─────────────────────────────────────────────────────┤  │
│   │                                                     │  │
│   │  ┌──────────────┐  ┌──────────────┐               │  │
│   │  │  Web Browser │  │ Mobile (PWA) │               │  │
│   │  │  (Desktop)   │  │   (Future)   │               │  │
│   │  └──────┬───────┘  └──────┬───────┘               │  │
│   │         │                  │                       │  │
│   │         └──────────┬───────┘                       │  │
│   │                    │                               │  │
│   │         ┌──────────▼───────────┐                   │  │
│   │         │   Blade Templates    │                   │  │
│   │         │   + Tailwind CSS     │                   │  │
│   │         │   + Alpine.js        │                   │  │
│   │         └──────────┬───────────┘                   │  │
│   └────────────────────┼─────────────────────────────┘  │
│                        │ HTTP/HTTPS                      │
│   ┌────────────────────▼─────────────────────────────┐  │
│   │ APPLICATION LAYER (Server-Side)                  │  │
│   ├──────────────────────────────────────────────────┤  │
│   │                                                  │  │
│   │  ┌────────────────────────────────────────────┐ │  │
│   │  │ LARAVEL 10.x FRAMEWORK                     │ │  │
│   │  ├────────────────────────────────────────────┤ │  │
│   │  │                                            │ │  │
│   │  │  ┌──────────────┐  ┌──────────────┐       │ │  │
│   │  │  │  Controllers │  │  Middleware  │       │ │  │
│   │  │  │  (Routes)    │  │  (Auth,CORS) │       │ │  │
│   │  │  └──────┬───────┘  └──────┬───────┘       │ │  │
│   │  │         │                  │               │ │  │
│   │  │  ┌──────▼──────────────────▼───────┐      │ │  │
│   │  │  │  Business Logic Layer           │      │ │  │
│   │  │  ├─────────────────────────────────┤      │ │  │
│   │  │  │ • BookingService                │      │ │  │
│   │  │  │ • PaymentService                │      │ │  │
│   │  │  │ • NotificationService           │      │ │  │
│   │  │  │ • AvailabilityService           │      │ │  │
│   │  │  └──────┬──────────────────────────┘      │ │  │
│   │  │         │                                  │ │  │
│   │  │  ┌──────▼──────────────────────────┐      │ │  │
│   │  │  │  Data Access Layer (Models)     │      │ │  │
│   │  │  ├─────────────────────────────────┤      │ │  │
│   │  │  │ Eloquent ORM                    │      │ │  │
│   │  │  │ • User, Therapist, Client       │      │ │  │
│   │  │  │ • Pemesanan, Layanan, Pembayaran    │      │ │  │
│   │  │  └──────┬──────────────────────────┘      │ │  │
│   │  │         │                                  │ │  │
│   │  └─────────┼──────────────────────────────────┘ │  │
│   └────────────┼────────────────────────────────────┘  │
│                │ Kueri Basis Data                      │
│   ┌────────────▼────────────────────────────────────┐  │
│   │ LAPISAN DATA (Persistence)                     │  │
│   ├────────────────────────────────────────────────┤  │
│   │                                                │  │
│   │  ┌──────────────────┐                          │  │
│   │  │  MySQL 8.0       │                          │  │
│   │  │  (DB Utama)      │                          │  │
│   │  │  • 15 Tabel      │                          │  │
│   │  │  • Dinormalisasi 3NF                        │  │
│   │  └──────────────────┘                          │  │
│   │                                                │  │
│   └────────────────────────────────────────────────┘  │
│                                                         │
│   ┌─────────────────────────────────────────────────┐  │
│   │ INTEGRASI EKSTERNAL                             │  │
│   ├─────────────────────────────────────────────────┤  │
│   │                                                 │  │
│   │  ┌────────────┐  ┌────────────┐  ┌──────────┐ │  │
│   │  │ Midtrans   │  │  SendGrid  │  │  Twilio  │ │  │
│   │  │(Pembayaran)│  │  (Email)   │  │  (SMS)   │ │  │
│   │  └────────────┘  └────────────┘  └──────────┘ │  │
│   │                                                 │  │
│   └─────────────────────────────────────────────────┘  │
│                                                         │
│   KOMPONEN KUNCI:                                       │
│   • Total Lapisan: 3 (Presentasi, Aplikasi, Data)      │
│   • Framework: Laravel 10.x (PHP 8.1)                   │
│   • Frontend: Blade + Tailwind CSS + Alpine.js          │
│   • ORM: Eloquent (pola Active Record)                  │
│   • Basis Data: MySQL 8.0                               │
│   • API Eksternal: 3 (Pembayaran, Email, SMS)           │
│                                                         │
│   POLA KOMUNIKASI:                                      │
│   • Klien ↔ Server: HTTP/HTTPS (mirip RESTful)          │
│   • Server ↔ Basis Data: PDO/driver MySQL               │
│   • Server ↔ Eksternal: HTTP REST APIs                  │
│                                                         │
│   Format: Diagram Komponen/Arsitektur PNG               │
│   Ukuran rekomendasi: 2000x1600px                       │
│   Gaya: Arsitektur berlapis dengan batas jelas          │
│                                                         │
│   File: assets/images/component-architecture.png        │
│   Tool: draw.io, Lucidchart, Visual Paradigm           │
│                                                         │
│   PRIORITAS: P1 - CRITICAL                              │
│   Harus menampilkan: Semua lapisan, komponen, alur      │
│                     komunikasi                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

_Gambar 4.14: Diagram Arsitektur Komponen sistem CUR-HEART dengan arsitektur 3-tier (Presentasi, Aplikasi, Data), menampilkan struktur framework Laravel dan integrasi eksternal_

---

**[File ini mencakup Diagram Kasus Penggunaan, Aktivitas, Sekuens, Kelas, dan Arsitektur Komponen. Lanjut ke Sistem Desain di file terpisah]**
