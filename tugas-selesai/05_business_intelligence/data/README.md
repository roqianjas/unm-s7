# 📊 SATRIAMART Business Intelligence - Dataset

## Overview
Dataset ini berisi data simulasi untuk keperluan analisis Business Intelligence SATRIAMART (Dekorasi & Aksesoris Akrilik).

**Periode Data**: November 2024 - Oktober 2025 (12 bulan)

## 📁 Struktur Data

### 1. Master Produk (`01_master_produk.csv`)
**Jumlah Records**: 50 produk

**Kolom**:
- `id_produk`: ID unik produk (P001-P050)
- `nama_produk`: Nama lengkap produk
- `kategori`: Kategori utama (Nomor Rumah, Signage, Papan Nama, Aksesoris Dekorasi)
- `sub_kategori`: Sub-kategori produk
- `ukuran`: Dimensi produk
- `warna_base`: Warna dasar
- `harga_jual`: Harga jual (Rp)
- `harga_modal`: Harga modal/COGS (Rp)
- `stok_tersedia`: Stok saat ini
- `material`: Jenis material akrilik
- `finishing`: Jenis finishing
- `berat_gram`: Berat dalam gram
- `deskripsi`: Deskripsi produk
- `status_aktif`: Status (Aktif/Tidak Aktif)
- `tanggal_dibuat`: Tanggal produk ditambahkan
- `tanggal_update`: Tanggal terakhir update

**Distribusi Kategori**:
- Nomor Rumah Akrilik: 15 produk (30%)
- Signage Akrilik: 10 produk (20%)
- Papan Nama Akrilik: 10 produk (20%)
- Aksesoris Dekorasi: 15 produk (30%)

**Range Harga**:
- Low-end: Rp 35.000 - Rp 100.000 (40%)
- Mid-range: Rp 100.000 - Rp 300.000 (40%)
- High-end: Rp 300.000 - Rp 750.000 (20%)

### 2. Master Pelanggan (`02_master_pelanggan.csv`)
**Jumlah Records**: 180 pelanggan

**Kolom**:
- `id_pelanggan`: ID unik pelanggan (C001-C180)
- `nama_lengkap`: Nama lengkap/nama bisnis
- `nomor_telepon`: Nomor HP
- `email`: Email address
- `alamat_lengkap`: Alamat lengkap
- `kota`: Kota
- `provinsi`: Provinsi
- `kode_pos`: Kode pos
- `jenis_pelanggan`: Individu/Bisnis/Reseller
- `segmen`: Retail/UMKM/Korporat
- `tanggal_registrasi`: Tanggal registrasi pertama
- `total_transaksi`: Jumlah transaksi
- `total_nilai_pembelian`: Total nilai pembelian (Rp)
- `status`: Aktif/Tidak Aktif
- `sumber_awal`: Sumber pelanggan pertama kali

**Distribusi Jenis Pelanggan**:
- Individu/Retail: 108 pelanggan (60%)
- Bisnis/UMKM: 54 pelanggan (30%)
- Reseller/Korporat: 18 pelanggan (10%)

**Distribusi Geografis** (Fokus Jabodetabek):
- Depok: 40%
- Jakarta Selatan: 20%
- Tangerang: 15%
- Bekasi: 10%
- Jakarta lainnya: 10%
- Luar Jabodetabek: 5%

**Customer Behavior**:
- One-time buyer: 55%
- Repeat customer (2-3x): 30%
- Loyal customer (4x+): 15%

### 3. Transaksi Penjualan (`03_transaksi_penjualan.csv`)
**Jumlah Records**: 320 transaksi

**Kolom**:
- `id_transaksi`: ID unik transaksi (TRX0001-TRX0320)
- `tanggal_transaksi`: Tanggal & waktu transaksi
- `id_pelanggan`: Foreign key ke master_pelanggan
- `id_produk`: Foreign key ke master_produk
- `jumlah_item`: Jumlah item dibeli
- `harga_satuan`: Harga per unit (Rp)
- `subtotal`: Subtotal sebelum diskon (Rp)
- `diskon_persen`: Persentase diskon (%)
- `diskon_nominal`: Nominal diskon (Rp)
- `biaya_custom`: Biaya customisasi (Rp)
- `biaya_ongkir`: Biaya pengiriman (Rp)
- `total_pembayaran`: Total yang dibayar (Rp)
- `metode_pembayaran`: Transfer Bank/E-wallet/COD
- `status_pembayaran`: Lunas/DP/Belum Bayar
- `status_pesanan`: Diterima/Selesai/Dikirim/Proses/Dibatalkan
- `channel_penjualan`: WhatsApp/Instagram/Marketplace/Offline
- `catatan_pesanan`: Catatan khusus
- `waktu_pengerjaan_hari`: Waktu pengerjaan (hari)
- `rating_pelanggan`: Rating 1-5
- `tanggal_selesai`: Tanggal selesai

**Distribusi per Bulan**:
- Peak Season (Des, Jun-Jul): 35-40 transaksi/bulan
- High Season (Jan, Agu): 28-32 transaksi/bulan
- Normal Season: 20-25 transaksi/bulan
- Low Season (Feb, Sep): 15-18 transaksi/bulan

**Channel Distribution**:
- WhatsApp: 45%
- Instagram: 30%
- Marketplace: 15%
- Offline: 10%

**Payment Method**:
- Transfer Bank: 55%
- E-wallet: 30%
- COD: 15%

**Status Pesanan**:
- Diterima/Selesai: 85%
- Dalam Proses: 8%
- Dibatalkan: 7%

**Total Revenue**: Rp 111.976.550 (periode 12 bulan)

## 📈 Key Metrics

### Revenue Metrics
- **Total Revenue**: Rp 111.976.550
- **Average Order Value**: Rp 349.926
- **Total Transactions**: 320
- **Average Monthly Revenue**: Rp 9.331.379

### Product Metrics
- **Total Products**: 50
- **Active Products**: 50
- **Average Product Price**: Rp 196.240
- **Price Range**: Rp 48.000 - Rp 625.000

### Customer Metrics
- **Total Customers**: 180
- **Active Customers**: 153 (85%)
- **Average Customer Value**: Rp 622.092
- **Repeat Rate**: 45%

## 🎯 Use Cases

### Dashboard Analytics
1. **Executive Summary**: Revenue overview, KPI cards, trend analysis
2. **Sales Analysis**: Product performance, channel effectiveness
3. **Customer Segmentation**: RFM analysis, geographic distribution
4. **Operational Metrics**: Fulfillment time, completion rate
5. **Financial Analysis**: Profit margin, cost structure

### Business Insights
- Identifikasi produk terlaris dan slow-moving
- Analisis peak season dan pola penjualan
- Evaluasi efektivitas channel penjualan
- Segmentasi pelanggan untuk targeted marketing
- Optimasi pricing strategy

## 🔄 Data Import ke Google Sheets

### Langkah Import:
1. Buka Google Sheets
2. File → Import → Upload
3. Upload file CSV
4. Pilih "Replace current sheet" atau "Insert new sheet"
5. Separator type: Comma
6. Convert text to numbers: Yes
7. Ulangi untuk semua file CSV

### Setup Looker Studio:
1. Buka Looker Studio (lookerstudio.google.com)
2. Create → Data Source
3. Pilih "Google Sheets"
4. Pilih spreadsheet yang sudah diupload
5. Buat dashboard dengan drag & drop

## 📝 Notes

**PENTING**: 
- Data ini adalah **DATA SIMULASI** untuk keperluan pembelajaran
- Bukan data riil dari SATRIAMART
- Dibuat mengikuti pola bisnis yang realistis
- Untuk keperluan tugas Business Intelligence II

## 👤 Creator

**Tugas**: Business Intelligence II (Kode 493)  
**Objek Riset**: SATRIAMART - Dekorasi & Aksesoris Akrilik  
**Dosen**: Ridan Nurfalah, M.Kom  
**Universitas**: Universitas Nusa Mandiri  
**Tanggal**: Oktober 2025

---

*Generated with Python for Business Intelligence Analysis*
