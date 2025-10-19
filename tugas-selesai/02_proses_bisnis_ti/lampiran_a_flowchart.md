# LAMPIRAN A: DIAGRAM ALIR PROSES BISNIS SATRIAMART

## A.1 Diagram Alir Proses Manajemen Pelanggan

### Deskripsi Proses
Diagram alir ini menunjukkan proses lengkap dari pertanyaan pelanggan awal hingga manajemen hubungan jangka panjang.

### Diagram Alir

```
┌─────────────────────────────────────────────────────────────┐
│                    MULAI                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Pelanggan Melakukan Kontak                           │
│    (WhatsApp/Instagram/TikTok/Kunjungan Langsung)           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Tim CS Menerima Pertanyaan                           │
│         - Catat informasi kontak                             │
│         - Identifikasi jenis pertanyaan                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Kirim Respons Awal                                   │
│         - Sapaan dan terima kasih                            │
│         - Konfirmasi penerimaan pertanyaan                   │
│         - Estimasi waktu respons detail                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Pengumpulan Kebutuhan Detail                         │
│         - Spesifikasi produk                                 │
│         - Ukuran, warna, desain                              │
│         - Kebutuhan khusus (LED, instalasi)                  │
│         - Budget dan timeline                                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah      │
              │ Informasi   │───── Tidak ────┐
              │ Lengkap?    │                │
              └──────┬──────┘                │
                     │ Ya                    │
                     ▼                       │
┌─────────────────────────────────────────────────┐           │
│    Input Data ke Database Pelanggan             │           │
│    - Informasi kontak                           │           │
│    - Kebutuhan dan preferensi                   │           │
│    - Status: Prospek                            │           │
└────────────────────┬────────────────────────────┘           │
                     │                                        │
                     │ ◄──────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Serahkan ke Tim Penjualan                            │
│         - Transfer informasi lengkap                         │
│         - Tetapkan PIC (Person in Charge)                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Penjadwalan Follow-up                                │
│         - Atur pengingat tindak lanjut                       │
│         - Monitoring status komunikasi                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah      │
              │ Jadi        │───── Tidak ────┐
              │ Order?      │                │
              └──────┬──────┘                │
                     │ Ya                    │
                     ▼                       ▼
┌─────────────────────────────────┐  ┌──────────────────────┐
│  Update Status: Pelanggan Aktif │  │ Update Status:       │
│  - Catat detail pesanan         │  │ Tidak Jadi           │
│  - Setup program loyalitas      │  │ - Catat alasan       │
└────────────────┬────────────────┘  │ - Jadwalkan          │
                 │                   │   follow-up future   │
                 ▼                   └──────────┬───────────┘
┌─────────────────────────────────┐            │
│  Layanan Purna Jual             │            │
│  - Follow-up kepuasan           │            │
│  - Penanganan keluhan           │            │
│  - Layanan garansi              │            │
└────────────────┬────────────────┘            │
                 │                             │
                 ▼                             │
┌─────────────────────────────────┐            │
│  Program Retensi                │            │
│  - Penawaran khusus             │            │
│  - Informasi produk baru        │            │
│  - Program rujukan              │            │
└────────────────┬────────────────┘            │
                 │                             │
                 │ ◄───────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│         Manajemen Hubungan Berkelanjutan                     │
│         - Komunikasi berkala                                 │
│         - Monitoring kepuasan                                │
│         - Identifikasi peluang up-sell/cross-sell           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    SELESAI                                   │
└─────────────────────────────────────────────────────────────┘
```

### Keterangan Simbol:
- ┌─┐ : Proses/Aktivitas
- ◇ : Keputusan
- → : Alur Proses
- ▼ : Arah Aliran

### Metrik Kinerja Proses:
- **Target Waktu Respons Awal:** < 2 jam
- **Target Waktu Pengumpulan Kebutuhan:** 1 hari
- **Target Konversi Prospek ke Pelanggan:** > 25%
- **Target Tingkat Kepuasan:** > 90%

---

## A.2 Diagram Alir Proses Penjualan dan Penawaran Harga

### Deskripsi Proses
Diagram alir ini menggambarkan proses dari pengumpulan kebutuhan hingga konfirmasi pesanan.

### Diagram Alir

```
┌─────────────────────────────────────────────────────────────┐
│                    MULAI                                     │
│         (Setelah Pengumpulan Kebutuhan Selesai)             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Penilaian Kelayakan                                  │
│         - Kelayakan Teknis (apakah bisa diproduksi?)        │
│         - Kelayakan Komersial (estimasi biaya)              │
│         - Ketersediaan Sumber Daya                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah      │
              │ Layak untuk │───── Tidak ────┐
              │ Dilanjutkan?│                │
              └──────┬──────┘                │
                     │ Ya                    ▼
                     │              ┌────────────────────┐
                     │              │ Informasikan ke    │
                     │              │ Pelanggan          │
                     │              │ - Jelaskan alasan  │
                     │              │ - Tawarkan         │
                     │              │   alternatif       │
                     │              └─────────┬──────────┘
                     │                        │
                     ▼                        │
┌─────────────────────────────────────────────┐              │
│    Konsultasi dengan Tim Produksi           │              │
│    - Diskusi spesifikasi teknis             │              │
│    - Estimasi waktu produksi                │              │
│    - Identifikasi material yang dibutuhkan  │              │
└────────────────────┬────────────────────────┘              │
                     │                                       │
                     ▼                                       │
┌─────────────────────────────────────────────────────────────┐
│         Perhitungan Biaya                                    │
│         - Biaya Material (akrilik, LED, aksesoris)          │
│         - Biaya Tenaga Kerja                                │
│         - Biaya Overhead                                    │
│         - Margin Keuntungan                                 │
│         - Biaya Pengiriman & Instalasi (jika ada)          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Penyusunan Penawaran Harga                           │
│         - Deskripsi produk detail                            │
│         - Spesifikasi teknis                                 │
│         - Rincian harga                                      │
│         - Timeline pengerjaan                                │
│         - Syarat dan ketentuan                               │
│         - Masa berlaku penawaran                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Review Internal                                      │
│         - Peninjauan oleh manajemen                         │
│         - Validasi harga dan margin                         │
│         - Koreksi jika diperlukan                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Kirim Penawaran Harga ke Pelanggan                   │
│         - Email formal dengan lampiran                       │
│         - Konfirmasi via WhatsApp                            │
│         - Penjelasan via telepon (jika diperlukan)          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Follow-up Penawaran                                  │
│         - Follow-up setelah 2-3 hari                        │
│         - Tanyakan pertanyaan/keberatan                     │
│         - Jadwalkan diskusi jika diperlukan                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah Ada  │
              │ Keberatan/  │───── Ya ────┐
              │ Pertanyaan? │             │
              └──────┬──────┘             │
                     │ Tidak              ▼
                     │           ┌─────────────────────┐
                     │           │ Proses Negosiasi    │
                     │           │ - Diskusi harga     │
                     │           │ - Penyesuaian spec  │
                     │           │ - Revisi proposal   │
                     │           └─────────┬───────────┘
                     │                     │
                     │ ◄───────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah      │
              │ Pelanggan   │───── Tidak ────┐
              │ Setuju?     │                │
              └──────┬──────┘                │
                     │ Ya                    │
                     ▼                       │
┌─────────────────────────────────┐         │
│  Konfirmasi Pesanan             │         │
│  - Terima persetujuan pelanggan │         │
│  - Buat nomor pesanan (PO)      │         │
│  - Tentukan jadwal               │         │
└────────────────┬────────────────┘         │
                 │                          │
                 ▼                          │
┌─────────────────────────────────┐         │
│  Proses Pembayaran              │         │
│  - Kirim invoice                │         │
│  - Terima DP (30-50%)           │         │
│  - Konfirmasi pembayaran        │         │
└────────────────┬────────────────┘         │
                 │                          │
                 ▼                          ▼
┌─────────────────────────────────┐  ┌──────────────────┐
│  Serah Terima ke Produksi       │  │ Update Status:   │
│  - Kirim detail pesanan         │  │ Deal Lost        │
│  - Brief lengkap                │  │ - Catat alasan   │
│  - Jadwal produksi              │  │ - Follow-up      │
└────────────────┬────────────────┘  │   di masa depan  │
                 │                   └────────┬─────────┘
                 │                            │
                 │ ◄──────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                    SELESAI                                   │
│         (Lanjut ke Proses Desain dan Produksi)              │
└─────────────────────────────────────────────────────────────┘
```

### Metrik Kinerja Proses:
- **Target Waktu Pembuatan Penawaran:** < 4 jam (produk standar), < 1 hari (produk kompleks)
- **Target Tingkat Konversi:** > 20%
- **Target Akurasi Harga:** 98%
- **Rata-rata Waktu Closing:** 7-10 hari

---

## A.3 Diagram Alir Proses Desain dan Persetujuan

### Deskripsi Proses
Diagram alir ini menunjukkan proses dari brief desain hingga persetujuan akhir dari pelanggan.

### Diagram Alir

```
┌─────────────────────────────────────────────────────────────┐
│                    MULAI                                     │
│         (Setelah Konfirmasi Pesanan dan DP)                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Serah Terima Brief Desain                            │
│         - Rapat singkat Sales dan Desainer                   │
│         - Transfer semua informasi                           │
│         - Referensi desain (jika ada)                        │
│         - Deadline desain                                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Riset dan Inspirasi                                  │
│         - Analisis kebutuhan pelanggan                       │
│         - Riset tren desain                                  │
│         - Kumpulkan referensi visual                         │
│         - Pertimbangan teknis produksi                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Pembuatan Konsep Desain Awal                         │
│         - Sketsa konsep (2-3 alternatif)                    │
│         - Pertimbangan estetika                              │
│         - Pertimbangan fungsionalitas                        │
│         - Estimasi biaya per konsep                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Review Internal Tim                                  │
│         - Tinjauan oleh supervisor desain                    │
│         - Feedback dan saran perbaikan                       │
│         - Validasi kelayakan produksi                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Finalisasi Desain untuk Presentasi                   │
│         - Render 3D atau mockup visual                       │
│         - Spesifikasi detail                                 │
│         - Pilihan warna dan material                         │
│         - Estimasi dimensi akurat                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Kirim Desain ke Pelanggan                            │
│         - Email dengan file desain                           │
│         - Presentasi via video call (jika perlu)            │
│         - Penjelasan detail via WhatsApp                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Menunggu Feedback Pelanggan                          │
│         - Follow-up setelah 2-3 hari                        │
│         - Tanyakan pendapat dan saran                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah      │
              │ Pelanggan   │───── Tidak ────┐
              │ Setuju?     │                │
              └──────┬──────┘                │
                     │ Ya                    ▼
                     │           ┌───────────────────────┐
                     │           │ Identifikasi Revisi   │
                     │           │ - Catat feedback      │
                     │           │ - Klarifikasi maksud  │
                     │           │ - Estimasi waktu      │
                     │           └─────────┬─────────────┘
                     │                     │
                     │                     ▼
                     │           ┌───────────────────────┐
                     │           │ Cek Jumlah Revisi     │
                     │           │ yang Sudah Dilakukan  │
                     │           └─────────┬─────────────┘
                     │                     │
                     │              ┌──────┴──────┐
                     │              │ Apakah > 2  │
                     │              │ kali revisi?│─── Ya ───┐
                     │              └──────┬──────┘          │
                     │                     │ Tidak           │
                     │                     ▼                 │
                     │           ┌───────────────────────┐   │
                     │           │ Proses Revisi         │   │
                     │           │ - Update desain       │   │
                     │           │ - Sesuaikan feedback  │   │
                     │           │ - Siapkan revisi      │   │
                     │           └─────────┬─────────────┘   │
                     │                     │                 │
                     │                     │                 ▼
                     │                     │      ┌──────────────────┐
                     │                     │      │ Diskusi dengan   │
                     │                     │      │ Pelanggan        │
                     │                     │      │ - Biaya tambahan │
                     │                     │      │ - Timeline baru  │
                     │                     │      └────────┬─────────┘
                     │                     │               │
                     │ ◄───────────────────┴───────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Persetujuan Akhir dari Pelanggan                     │
│         - Konfirmasi tertulis (email/WhatsApp)              │
│         - Dokumentasi persetujuan                            │
│         - Final sign-off                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Persiapan File untuk Produksi                        │
│         - Gambar teknis dengan dimensi akurat                │
│         - Spesifikasi material detail                        │
│         - Instruksi khusus untuk produksi                    │
│         - File vektor untuk pemotongan CNC                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Serah Terima ke Tim Produksi                         │
│         - Handover meeting                                   │
│         - Penjelasan detail desain                           │
│         - Diskusi kemungkinan tantangan                      │
│         - Konfirmasi timeline produksi                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Arsip Desain                                         │
│         - Simpan semua versi desain                          │
│         - Dokumentasi revisi                                 │
│         - Backup ke cloud storage                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    SELESAI                                   │
│         (Lanjut ke Proses Produksi)                         │
└─────────────────────────────────────────────────────────────┘
```

### Metrik Kinerja Proses:
- **Target Waktu Desain Awal:** 1-2 hari
- **Target Waktu Revisi:** 1 hari per revisi
- **Target Tingkat Persetujuan Pertama:** > 60%
- **Rata-rata Jumlah Revisi:** 1-2 kali

---

## A.4 Diagram Alir Proses Produksi

### Deskripsi Proses
Diagram alir ini menggambarkan proses produksi dari perencanaan hingga pengendalian kualitas final.

### Diagram Alir

```
┌─────────────────────────────────────────────────────────────┐
│                    MULAI                                     │
│         (Setelah Desain Disetujui)                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Perencanaan Produksi                                 │
│         - Review spesifikasi dan gambar teknis              │
│         - Tentukan urutan proses produksi                    │
│         - Estimasi waktu per tahap                           │
│         - Alokasi sumber daya (mesin, manpower)             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Pemeriksaan Ketersediaan Material                    │
│         - Cek stok material yang dibutuhkan                  │
│         - Verifikasi kualitas material                       │
│         - Identifikasi kekurangan                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah      │
              │ Material    │───── Tidak ────┐
              │ Lengkap?    │                │
              └──────┬──────┘                │
                     │ Ya                    ▼
                     │           ┌────────────────────────┐
                     │           │ Pengadaan Material     │
                     │           │ - Hubungi supplier     │
                     │           │ - Order material       │
                     │           │ - Tunggu pengiriman    │
                     │           │ - QC penerimaan        │
                     │           └─────────┬──────────────┘
                     │                     │
                     │ ◄───────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Persiapan Material                                   │
│         - Potong material sesuai ukuran rough               │
│         - Siapkan aksesoris dan komponen                     │
│         - Labeling dan penomoran                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Proses Pemotongan (Cutting)                          │
│         - Setup file di mesin CNC                            │
│         - Kalibrasi mesin                                    │
│         - Proses pemotongan akrilik                          │
│         - Inspeksi hasil potongan                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         QC Tahap 1: Inspeksi Pemotongan                      │
│         - Cek dimensi dan akurasi                            │
│         - Cek kualitas tepi potongan                         │
│         - Cek cacat visual                                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Lolos QC    │
              │ Pemotongan? │───── Tidak ────┐
              └──────┬──────┘                │
                     │ Ya                    ▼
                     │           ┌────────────────────────┐
                     │           │ Analisis Masalah       │
                     │           │ - Identifikasi cacat   │
                     │           │ - Tentukan tindakan    │
                     │           └─────────┬──────────────┘
                     │                     │
                     │              ┌──────┴──────┐
                     │              │ Bisa        │
                     │              │ Diperbaiki? │─── Tidak ──┐
                     │              └──────┬──────┘            │
                     │                     │ Ya                │
                     │                     ▼                   │
                     │           ┌────────────────────────┐    │
                     │           │ Proses Perbaikan       │    │
                     │           │ (Re-work)              │    │
                     │           └─────────┬──────────────┘    │
                     │                     │                   │
                     │ ◄───────────────────┘                   │
                     │                                         ▼
                     │                              ┌────────────────┐
                     │                              │ Potong Ulang   │
                     │                              │ Material Baru  │
                     │                              └────────┬───────┘
                     │                                       │
                     │ ◄─────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Proses Finishing                                     │
│         - Pembersihan dan polishing                          │
│         - Penghalusan tepi                                   │
│         - Pemrosesan permukaan khusus (jika ada)            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Perakitan (Assembly)                                 │
│         - Pemasangan komponen LED (jika ada)                │
│         - Perakitan parts multi-layer                        │
│         - Pemasangan bracket/mounting                        │
│         - Pengkabelan (untuk produk dengan LED)             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Testing Fungsional                                   │
│         - Test lampu LED (jika ada)                          │
│         - Test mounting/instalasi                            │
│         - Test daya tahan                                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         QC Tahap 2: Inspeksi Final                           │
│         - Inspeksi visual menyeluruh                         │
│         - Cek dimensi final                                  │
│         - Cek kualitas finishing                             │
│         - Cek fungsi (LED, mounting, dll)                    │
│         - Cek kesesuaian dengan desain                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Lolos QC    │
              │ Final?      │───── Tidak ────┐
              └──────┬──────┘                │
                     │ Ya                    │
                     │                       │
                     │           (Kembali ke tahap yang
                     │            bermasalah untuk perbaikan)
                     │                       │
                     │ ◄─────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Dokumentasi Produk                                   │
│         - Foto produk akhir                                  │
│         - Catat nomor batch                                  │
│         - Update status produksi                             │
│         - Arsip dokumen QC                                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Serah Terima ke Pengiriman                           │
│         - Packing list detail                                │
│         - Instruksi handling                                 │
│         - Dokumen garansi                                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    SELESAI                                   │
│         (Lanjut ke Proses Pengiriman)                       │
└─────────────────────────────────────────────────────────────┘
```

### Metrik Kinerja Proses:
- **Target Waktu Produksi:** 3-7 hari (tergantung kompleksitas)
- **Target Tingkat Cacat:** < 2%
- **Target First Pass Yield:** > 95%
- **Target Pemanfaatan Kapasitas:** > 80%

---

## A.5 Diagram Alir Proses Pengiriman dan Layanan Purna Jual

### Deskripsi Proses
Diagram alir ini menggambarkan proses dari pengemasan hingga layanan garansi.

### Diagram Alir

```
┌─────────────────────────────────────────────────────────────┐
│                    MULAI                                     │
│         (Setelah Produk Lolos QC Final)                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Persiapan Pengiriman                                 │
│         - Konfirmasi alamat pengiriman                       │
│         - Konfirmasi jadwal pengiriman                       │
│         - Persiapan tim instalasi (jika perlu)              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Pengemasan (Packaging)                               │
│         - Pembersihan akhir produk                           │
│         - Wrapping dengan bubble wrap/plastik                │
│         - Packing dalam box/karton                           │
│         - Labeling "Fragile" dan "Handle with Care"         │
│         - Dokumentasi foto sebelum packing                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Persiapan Dokumen                                    │
│         - Surat jalan                                        │
│         - Invoice (jika belum dibuat)                        │
│         - Kartu garansi                                      │
│         - Instruksi perawatan                                │
│         - Dokumen instalasi (jika ada)                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Jenis       │
              │ Pengiriman? │
              └──────┬──────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
┌─────────────┐ ┌─────────┐ ┌───────────────┐
│Pengiriman   │ │Ambil    │ │Instalasi      │
│oleh Kurir   │ │Sendiri  │ │Langsung       │
└──────┬──────┘ └────┬────┘ └────┬──────────┘
       │             │            │
       │             │            │
       ▼             ▼            ▼
┌─────────────┐ ┌─────────┐ ┌───────────────┐
│Koordinasi   │ │Notifikasi│ │Jadwalkan Tim  │
│dengan Kurir │ │Pelanggan │ │Instalasi      │
└──────┬──────┘ └────┬────┘ └────┬──────────┘
       │             │            │
       └─────────────┼────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Proses Pengiriman/Penyerahan                         │
│         - Tracking pengiriman                                │
│         - Update status ke pelanggan                         │
│         - Koordinasi waktu penerimaan                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah Ada  │
              │ Instalasi?  │───── Tidak ────┐
              └──────┬──────┘                │
                     │ Ya                    │
                     ▼                       │
┌─────────────────────────────────┐         │
│  Proses Instalasi               │         │
│  - Survey lokasi instalasi      │         │
│  - Persiapan alat dan bahan     │         │
│  - Proses pemasangan            │         │
│  - Testing final di lokasi      │         │
│  - Dokumentasi hasil instalasi  │         │
└────────────────┬────────────────┘         │
                 │                          │
                 │ ◄────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│         Serah Terima Produk                                  │
│         - Inspeksi bersama pelanggan                         │
│         - Demonstrasi cara penggunaan/perawatan             │
│         - Serahkan dokumen (garansi, invoice, dll)          │
│         - Minta tanda tangan penerimaan                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Proses Pelunasan (jika belum lunas)                  │
│         - Terima pembayaran sisa                             │
│         - Berikan kuitansi pelunasan                         │
│         - Update status pembayaran                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Follow-up Awal (Hari ke-1)                           │
│         - Konfirmasi kepuasan pengiriman/instalasi          │
│         - Tanyakan jika ada kendala                          │
│         - Berikan kontak untuk support                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Follow-up Lanjutan (Minggu ke-1)                     │
│         - Cek kondisi produk                                 │
│         - Kumpulkan feedback                                 │
│         - Tawarkan bantuan jika diperlukan                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Pengumpulan Testimoni & Review                       │
│         - Minta testimoni jika pelanggan puas               │
│         - Minta foto produk terpasang                        │
│         - Permintaan review di sosial media                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Update Database Pelanggan                            │
│         - Update status: Completed                           │
│         - Catat feedback dan rating                          │
│         - Tandai sebagai pelanggan potensial repeat         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Program Layanan Purna Jual                           │
│         BERLANGSUNG SELAMA MASA GARANSI (6-12 BULAN)        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ┌──────┴──────┐
              │ Apakah Ada  │
              │ Komplain/   │───── Tidak ────┐
              │ Claim?      │                │
              └──────┬──────┘                │
                     │ Ya                    │
                     ▼                       │
┌─────────────────────────────────┐         │
│  Proses Penanganan Komplain     │         │
│  - Terima dan catat komplain    │         │
│  - Analisis penyebab masalah    │         │
│  - Tentukan solusi              │         │
└────────────────┬────────────────┘         │
                 │                          │
                 ▼                          │
        ┌────────┴────────┐                │
        │ Jenis Masalah?  │                │
        └────────┬────────┘                │
                 │                          │
     ┌───────────┼───────────┐             │
     │           │           │             │
     ▼           ▼           ▼             │
┌─────────┐ ┌─────────┐ ┌─────────┐       │
│Cacat    │ │Kerusakan│ │Keluhan  │       │
│Produksi │ │Penggunaan│ │Layanan  │       │
└────┬────┘ └────┬────┘ └────┬────┘       │
     │           │           │             │
     ▼           ▼           ▼             │
┌─────────┐ ┌─────────┐ ┌─────────┐       │
│Replace  │ │Perbaikan│ │Follow-up│       │
│Gratis   │ │atau     │ │dan      │       │
│(Garansi)│ │Kompensasi│ │Perbaikan│       │
└────┬────┘ └────┬────┘ └────┬────┘       │
     │           │           │             │
     └───────────┼───────────┘             │
                 │                         │
                 │ ◄───────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│         Follow-up Penyelesaian                               │
│         - Konfirmasi masalah terselesaikan                   │
│         - Kumpulkan feedback penanganan                      │
│         - Dokumentasi untuk pembelajaran                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         Maintenance Hubungan Jangka Panjang                  │
│         - Follow-up berkala (3 bulan, 6 bulan)              │
│         - Informasi produk baru                              │
│         - Penawaran khusus untuk repeat order               │
│         - Program referral                                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    SELESAI                                   │
│         (Pelanggan Menjadi Repeat Customer Potensial)       │
└─────────────────────────────────────────────────────────────┘
```

### Metrik Kinerja Proses:
- **Target Ketepatan Waktu Pengiriman:** > 95%
- **Target Tingkat Kepuasan Pengiriman:** > 90%
- **Target Response Time Komplain:** < 24 jam
- **Target Resolusi Komplain:** < 7 hari
- **Target Tingkat Repeat Customer:** > 40%

---

**Catatan:**
- Semua diagram alir di atas merupakan representasi visual dari proses bisnis aktual SATRIAMART
- Waktu dan target yang tercantum adalah target ideal yang ingin dicapai setelah implementasi solusi
- Diagram dapat disesuaikan seiring dengan perkembangan dan perbaikan proses bisnis

---

**Disiapkan oleh:** Tim Analisis Proses Bisnis SATRIAMART  
**Tanggal:** Oktober 2025  
**Versi:** 1.0
