# PERTANYAAN PERMINTAAN DATA UNTUK DASHBOARD BI LOOKER STUDIO
## SATRIAMART - Business Intelligence Dashboard

---

**Kepada:** Tim SATRIAMART  
**Perihal:** Permintaan Data untuk Dashboard Business Intelligence  
**Tanggal:** 16 Oktober 2025  

---

## PENDAHULUAN

Dalam rangka pembuatan Dashboard Business Intelligence menggunakan Google Looker Studio untuk analisis performa bisnis SATRIAMART, kami memerlukan beberapa data historis. Berikut adalah pertanyaan-pertanyaan terkait data yang kami butuhkan:

---

## A. DATA PELANGGAN (CUSTOMER DATA)

### 1. Apakah SATRIAMART memiliki database pelanggan yang terstruktur?

### 2. Data pelanggan apa saja yang tersedia? Apakah mencakup:
   - ID Pelanggan (customer ID unik)?
   - Nama Pelanggan?
   - Tipe Pelanggan (B2B atau B2C)?
   - Sektor Industri (khusus untuk B2B)?
   - Alamat lengkap (Kota, Provinsi, Region)?
   - Tanggal registrasi/mulai menjadi pelanggan?
   - Status pelanggan (Aktif/Tidak Aktif)?
   - Informasi kontak (email, telepon)?

### 3. Berapa jumlah total pelanggan yang ada di database?
   - Berapa pelanggan B2B?
   - Berapa pelanggan B2C?

### 4. Apakah data pelanggan bisa diekspor dalam format CSV atau Excel?

---

## B. DATA TRANSAKSI PENJUALAN (SALES DATA)

### 5. Apakah SATRIAMART menyimpan data transaksi penjualan secara digital?

### 6. Data transaksi apa saja yang tersedia? Apakah mencakup:
   - Nomor Order/Invoice?
   - Tanggal transaksi?
   - ID Pelanggan?
   - ID Produk yang dibeli?
   - Nama Produk?
   - Kuantitas yang dijual?
   - Harga per unit?
   - Total nilai transaksi?
   - Diskon (jika ada)?
   - Nilai bersih setelah diskon?
   - Status order (Completed, Pending, Cancelled)?
   - Metode pembayaran?

### 7. Berapa lama periode data transaksi yang tersedia?
   - Apakah ada data 12 bulan terakhir?
   - Apakah ada data 24 bulan terakhir?

### 8. Berapa rata-rata jumlah transaksi per bulan?

### 9. Apakah data transaksi mencakup informasi biaya (COGS/Harga Pokok Penjualan)?

### 10. Dalam format apa data transaksi bisa diekspor (CSV, Excel, database)?

---

## C. DATA PRODUK (PRODUCT DATA)

### 11. Apakah ada master data produk yang mencatat semua produk SATRIAMART?

### 12. Informasi produk apa saja yang tersedia? Apakah mencakup:
   - ID Produk (product ID unik)?
   - Nama Produk?
   - Kategori Produk (Display Stand, Custom Panel, Signage, dll)?
   - Sub-kategori?
   - Jenis Material?
   - Ukuran/Dimensi?
   - Warna?
   - Tipe (Standard atau Custom)?
   - Harga Jual?
   - Harga Pokok/Biaya Produksi?
   - Status produk (Aktif/Discontinued)?

### 13. Berapa jumlah total produk yang ditawarkan SATRIAMART?

### 14. Apakah ada produk yang sudah discontinued tapi masih ada di data historis?

---

## D. DATA PRODUKSI (PRODUCTION DATA)

### 15. Apakah SATRIAMART mencatat data produksi secara detail?

### 16. Data produksi apa saja yang tersedia? Apakah mencakup:
   - Nomor Work Order?
   - Tanggal produksi?
   - Produk yang diproduksi?
   - Jumlah yang diproduksi?
   - Jumlah defect/cacat?
   - Biaya material?
   - Biaya tenaga kerja?
   - Biaya overhead?
   - Total biaya produksi?
   - Jam kerja yang digunakan?
   - Skor kualitas?

### 17. Apakah data produksi tersedia untuk 12-24 bulan terakhir?

### 18. Jika data produksi tidak tersedia secara detail, apakah ada data biaya produksi per produk?

---

## E. DATA INVENTORY/STOK

### 19. Apakah SATRIAMART memiliki sistem pencatatan stok/inventory?

### 20. Data inventory apa saja yang tersedia? Apakah mencakup:
   - Tanggal pencatatan?
   - ID Produk?
   - Nama Produk?
   - Stok masuk (IN)?
   - Stok keluar (OUT)?
   - Stok awal periode?
   - Stok akhir periode?
   - Lokasi gudang?
   - Nilai inventory?

### 21. Seberapa sering data inventory diupdate (harian, mingguan, bulanan)?

### 22. Apakah ada data stock movement untuk 12-24 bulan terakhir?

---

## F. DATA BIAYA & FINANSIAL

### 23. Apakah SATRIAMART mencatat biaya operasional secara terpisah per kategori?

### 24. Data biaya apa saja yang tersedia? Apakah mencakup:
   - Biaya Marketing?
   - Biaya Sales?
   - Biaya Operasional?
   - Biaya Overhead?
   - Biaya Administrasi?
   - Biaya Utilitas (listrik, air, dll)?
   - Biaya Sewa/Fasilitas?

### 25. Apakah data biaya tersedia per bulan untuk 12-24 bulan terakhir?

### 26. Apakah ada data profit margin per produk atau per kategori produk?

---

## G. FORMAT DAN AKSES DATA

### 27. Dalam format apa data-data tersebut bisa diberikan?
   - [ ] CSV
   - [ ] Excel (.xlsx)
   - [ ] Google Sheets
   - [ ] Akses Database (MySQL/PostgreSQL)
   - [ ] Format lainnya: _______________

### 28. Apakah data menggunakan format tanggal yang konsisten?
   - Format apa yang digunakan? (contoh: DD/MM/YYYY, YYYY-MM-DD)

### 29. Apakah data menggunakan format angka dengan separator tertentu?
   - Contoh: 2.500.000,50 (Indonesia) atau 2500000.50 (International)

### 30. Apakah memungkinkan untuk mendapatkan akses langsung ke database?
   - Jika ya, database apa yang digunakan (MySQL, PostgreSQL, SQL Server, dll)?

---

## H. PERIODE DAN VOLUME DATA

### 31. Untuk periode waktu berapa lama data bisa diberikan?
   - [ ] 6 bulan terakhir
   - [ ] 12 bulan terakhir
   - [ ] 24 bulan terakhir
   - [ ] Lebih dari 24 bulan

### 32. Berapa estimasi jumlah records untuk setiap jenis data?
   - Jumlah transaksi: _______ records
   - Jumlah pelanggan: _______ records
   - Jumlah produk: _______ records
   - Jumlah work order produksi: _______ records
   - Jumlah inventory movement: _______ records

---

## I. DATA QUALITY & COMPLETENESS

### 33. Apakah data yang ada sudah lengkap dan terstruktur dengan baik?

### 34. Apakah ada missing values atau data yang tidak lengkap?

### 35. Apakah ada duplikasi data yang perlu dibersihkan?

### 36. Apakah ID pelanggan dan ID produk konsisten di semua transaksi?

### 37. Apakah ada data dictionary atau dokumentasi yang menjelaskan arti setiap kolom data?

---

## J. PRIVACY & SECURITY

### 38. Apakah ada kebijakan privacy terkait data pelanggan?

### 39. Apakah nama pelanggan perlu di-anonymize/di-mask untuk keperluan akademis?

### 40. Apakah ada data yang bersifat confidential dan tidak bisa dibagikan?

### 41. Apakah perlu ada NDA (Non-Disclosure Agreement) untuk penggunaan data?

---

## K. ADDITIONAL INFORMATION

### 42. Apakah ada data tambahan lain yang mungkin berguna untuk analisis BI?
   - Data marketing campaign?
   - Data customer feedback/complaints?
   - Data supplier?
   - Data kompetitor?

### 43. Apakah SATRIAMART saat ini sudah menggunakan sistem/software tertentu untuk manage data?
   - Jika ya, software apa? (Excel, ERP, CRM, dll)

### 44. Apakah ada laporan atau dashboard yang sudah ada saat ini yang bisa dijadikan referensi?

### 45. Siapa person in charge (PIC) yang bisa dihubungi untuk follow-up terkait data?
   - Nama: _______________
   - Posisi: _______________
   - Email: _______________
   - Telepon: _______________

---

## L. TIMELINE & DELIVERY

### 46. Kapan data bisa mulai diberikan?
   - [ ] Segera (1-3 hari)
   - [ ] 1 minggu
   - [ ] 2 minggu
   - [ ] 1 bulan
   - [ ] Perlu diskusi lebih lanjut

### 47. Apakah data bisa diberikan secara bertahap?
   - Misalnya: Master data dulu, kemudian transactional data

### 48. Apakah ada proses approval internal yang diperlukan sebelum data bisa diberikan?

### 49. Bagaimana preferred method untuk transfer data?
   - [ ] Email attachment
   - [ ] Cloud storage (Google Drive, Dropbox, dll)
   - [ ] Direct database access
   - [ ] Physical media (USB, dll)
   - [ ] Lainnya: _______________

### 50. Apakah diperlukan pertemuan untuk penjelasan lebih detail tentang struktur data?

---

## CATATAN TAMBAHAN

**Tujuan Penggunaan Data:**
Data yang diminta akan digunakan untuk:
1. Pembuatan Dashboard Business Intelligence menggunakan Google Looker Studio
2. Analisis performa bisnis SATRIAMART
3. Keperluan tugas akhir mata kuliah Business Intelligence
4. Presentasi dan dokumentasi akademis

**Komitmen Privacy:**
- Data hanya akan digunakan untuk keperluan akademis
- Data akan dijaga kerahasiaannya dan tidak disebarluaskan
- Jika diperlukan, data sensitif dapat di-anonymize
- Hasil analisis akan dipresentasikan dengan mempertimbangkan aspek confidentiality

---

## LAMPIRAN

Untuk memudahkan pemahaman tentang data yang dibutuhkan, terlampir:
1. Contoh struktur data yang diinginkan (sample format)
2. Dokumen detail spesifikasi data
3. Mockup/preview dashboard yang akan dibuat

---

**Terima kasih atas perhatian dan kerjasamanya!**

Jika ada pertanyaan atau memerlukan klarifikasi lebih lanjut, silakan menghubungi:

**Nama:** [Nama Anda]  
**NIM:** [NIM Anda]  
**Program Studi:** Sistem Informasi  
**Universitas:** Nusa Mandiri  
**Email:** [email@student.nusamandiri.ac.id]  
**HP:** [Nomor HP]  

**Dosen Pembimbing:**  
Ridan Nurfalah, M.Kom  

---

*Dokumen ini dibuat: 16 Oktober 2025*
