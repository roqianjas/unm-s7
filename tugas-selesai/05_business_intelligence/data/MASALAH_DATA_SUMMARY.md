# 📋 Ringkasan Masalah Data Quality - Quick Reference

## 🎯 Tujuan Dokumen
Dokumen ini adalah **quick reference** untuk memahami masalah data quality yang ada di setiap file raw data. Gunakan ini untuk:
- Screenshot presentasi
- Penjelasan di laporan
- Demonstrasi proses data cleaning

---

## 📊 Ringkasan Masalah per File

### 1️⃣ Master Produk (01_master_produk_raw.csv)
| Baris | Masalah | Kolom | Nilai Salah | Seharusnya |
|-------|---------|-------|-------------|------------|
| P002 | Format tanggal | tanggal_dibuat | 15/01/2024 | 2024-01-15 |
| P003 | Missing value | warna | (kosong) | Custom/Gold/Silver |
| P003 | Missing value | stok_tersedia | (kosong) | 0 atau rata-rata |
| P004 | Kapitalisasi | status | aktif | Aktif |
| P005 | Missing value | tanggal_update | (kosong) | 2024-11-01 |
| P006 | Duplikasi | seluruh baris | (duplikat) | Hapus salah satu |
| P008 | Missing value | stok_tersedia | (kosong) | 0 atau rata-rata |

**Total Masalah: 8 dari 20 baris (40%)**

---

### 2️⃣ Master Pelanggan (02_master_pelanggan_raw.csv)
| Baris | Masalah | Kolom | Nilai Salah | Seharusnya |
|-------|---------|-------|-------------|------------|
| C002 | Format tanggal | tanggal_registrasi | 10/01/2024 | 2024-01-10 |
| C002 | Kapitalisasi | nama_lengkap | SITI RAHAYU | Siti Rahayu |
| C003 | Missing value | email | (kosong) | ahmad.fauzi@email.com |
| C004 | Missing value | kode_pos | (kosong) | 12160 |
| C005 | Kapitalisasi | status | aktif | Aktif |
| C011 | Missing value | total_transaksi | (kosong) | 4 |
| C017 | Missing value | email | (kosong) | qori.maulana@email.com |

**Total Masalah: 7 dari 20 baris (35%)**

---

### 3️⃣ Transaksi Penjualan (03_transaksi_penjualan_raw.csv)
| Baris | Masalah | Kolom | Nilai Salah | Seharusnya |
|-------|---------|-------|-------------|------------|
| TRX002 | Format tanggal | tanggal_transaksi | 01/11/2024 | 2024-11-01 |
| TRX004 | Perhitungan | total_pembayaran | 300000 | 300000 (validasi) |
| Multiple | Missing value | catatan_pesanan | (kosong) | "-" atau "Tidak ada" |

**Total Masalah: 3 dari 20 baris (15%)**

---

### 4️⃣ Riwayat Stok (04_riwayat_stok_raw.csv)
| Baris | Masalah | Kolom | Nilai Salah | Seharusnya |
|-------|---------|-------|-------------|------------|
| STK0002 | Format tanggal | tanggal | 01/01/2025 | 2025-01-01 |
| STK0009 | Kapitalisasi | jenis_transaksi | pembelian | Pembelian |
| STK0031 | Missing value | stok_masuk | (kosong) | 31 atau 0 |
| Multiple | Format keterangan | keterangan | Mixed format | Standarisasi |

**Total Masalah: 4 dari 40 baris (10%)**

---

### 5️⃣ Biaya Operasional (05_biaya_operasional_raw.csv)
| Baris | Masalah | Kolom | Nilai Salah | Seharusnya |
|-------|---------|-------|-------------|------------|
| BYA002 | Format tanggal | tanggal | 01/11/2024 | 2024-11-01 |
| BYA011 | Missing value | catatan | (kosong) | "-" |
| BYA016 | Missing value | catatan | (kosong) | "-" |
| BYA018 | Format tanggal | tanggal | 01/12/2024 | 2024-12-01 |
| BYA020 | Missing value | nominal | (kosong) | 150000 (estimasi) |
| BYA026 | Missing value | catatan | (kosong) | "-" |

**Total Masalah: 6 dari 30 baris (20%)**

---

### 6️⃣ Marketing Campaign (06_marketing_campaign_raw.csv)
| Baris | Masalah | Kolom | Nilai Salah | Seharusnya |
|-------|---------|-------|-------------|------------|
| CMP002 | Format tanggal | tanggal_mulai | 01/01/2025 | 2025-01-01 |
| CMP022 | Format tanggal | tanggal_mulai | 28/01/2024 | 2024-01-28 |
| CMP025 | Missing value | budget | (kosong) | 1500000 (estimasi) |
| CMP025 | Kapitalisasi | nama_campaign | FLASH SALE SPESIAL | Flash Sale Spesial |
| CMP025 | Kapitalisasi | platform | facebook | Facebook |
| CMP026 | Kapitalisasi | platform | Google ads | Google Ads |
| CMP027 | Missing value | tanggal_selesai | (kosong) | 2025-06-15 (estimasi) |
| CMP027 | Kapitalisasi | platform | Instagram | Instagram (OK) |
| CMP025-28 | Data tidak realistis | reach/engagement | Terlalu besar | Sesuaikan dengan budget |

**Total Masalah: 10 dari 28 baris (36%)**

---

## 🎨 Highlight untuk Screenshot

### Warna Coding untuk Excel/Google Sheets:
- 🔴 **Merah**: Missing values (sel kosong)
- 🟡 **Kuning**: Format tidak konsisten
- 🟠 **Orange**: Duplikasi data
- 🔵 **Biru**: Inkonsistensi kapitalisasi
- 🟣 **Ungu**: Data tidak realistis

### Contoh Screenshot yang Bagus:
1. **Before (Raw Data)**:
   - Zoom ke baris yang bermasalah
   - Highlight dengan warna sesuai jenis masalah
   - Tambahkan callout/arrow untuk penjelasan

2. **After (Clean Data)**:
   - Zoom ke baris yang sama
   - Tunjukkan data sudah bersih
   - Highlight dengan warna hijau untuk menunjukkan "fixed"

---

## 📈 Statistik Overall

```
Total Baris Data: 158 baris
Total Masalah: 38 masalah
Persentase Masalah: 24%

Breakdown Masalah:
├── Missing Values: 20 (53%)
├── Format Tidak Konsisten: 15 (39%)
├── Inkonsistensi Kapitalisasi: 12 (32%)
├── Data Tidak Realistis: 4 (11%)
└── Duplikasi: 1 (3%)
```

---

## ✅ Checklist Pembersihan

### Untuk Setiap File:
- [ ] Standarisasi format tanggal ke YYYY-MM-DD
- [ ] Fill atau hapus missing values
- [ ] Standarisasi kapitalisasi (Title Case untuk nama, Proper Case untuk status)
- [ ] Hapus duplikasi
- [ ] Validasi perhitungan dan logika bisnis
- [ ] Validasi tipe data (numeric, text, date)
- [ ] Standarisasi format teks

### Validasi Akhir:
- [ ] Tidak ada missing values di kolom kritis
- [ ] Format tanggal konsisten
- [ ] Tidak ada duplikasi
- [ ] Kapitalisasi konsisten
- [ ] Perhitungan matematis benar
- [ ] Data realistis dan masuk akal

---

## 💡 Tips untuk Presentasi

1. **Tunjukkan Impact**:
   - "Sebelum cleaning: 24% data bermasalah"
   - "Setelah cleaning: 100% data valid"

2. **Contoh Konkret**:
   - Pilih 2-3 masalah paling jelas untuk dijelaskan detail
   - Tunjukkan before-after side by side

3. **Jelaskan Proses**:
   - Extract → Transform → Load (ETL)
   - Tools yang digunakan (Excel, Python, Google Sheets)
   - Waktu yang dibutuhkan

4. **Dampak Bisnis**:
   - "Data kotor = Analisis salah = Keputusan salah"
   - "Data bersih = Dashboard akurat = Keputusan tepat"

---

**Dibuat oleh:** Tim BI SATRIAMART  
**Tanggal:** Desember 2024  
**Versi:** 1.0
