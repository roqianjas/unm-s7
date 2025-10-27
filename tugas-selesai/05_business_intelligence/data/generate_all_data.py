#!/usr/bin/env python3
"""
Script untuk generate semua data Business Intelligence SATRIAMART
"""

import csv
import random
from datetime import datetime, timedelta

def generate_pelanggan():
    """Generate 180 pelanggan"""
    print("Generating pelanggan data...")
    
    nama_depan = ['Budi', 'Siti', 'Ahmad', 'Dewi', 'Andi', 'Sri', 'Muhammad', 'Nur', 'Agus', 'Rina', 
                  'Hendra', 'Lina', 'Rahmat', 'Maya', 'Doni', 'Fitri', 'Yanto', 'Ayu', 'Wahyu', 'Diah',
                  'Eko', 'Sari', 'Rizki', 'Indah', 'Faisal', 'Putri', 'Adi', 'Wati', 'Bambang', 'Tuti',
                  'Hadi', 'Yuni', 'Irwan', 'Ratna', 'Joko', 'Endang', 'Tono', 'Mega', 'Rudy', 'Ani']
    
    nama_belakang = ['Santoso', 'Wijaya', 'Pratama', 'Kusuma', 'Putra', 'Putri', 'Setiawan', 'Wati',
                     'Hidayat', 'Lestari', 'Nugroho', 'Sari', 'Permana', 'Dewi', 'Firmansyah', 'Rahayu']
    
    kota_list = [
        ('Depok', 'Jawa Barat', '16400', 72),
        ('Jakarta Selatan', 'DKI Jakarta', '12160', 36),
        ('Tangerang', 'Banten', '15310', 27),
        ('Bekasi', 'Jawa Barat', '17510', 18),
        ('Jakarta Timur', 'DKI Jakarta', '13220', 9),
        ('Jakarta Barat', 'DKI Jakarta', '11220', 9),
        ('Bogor', 'Jawa Barat', '16110', 5),
        ('Bandung', 'Jawa Barat', '40115', 4)
    ]
    
    jenis_pelanggan_dist = [
        ('Individu', 'Retail', 108),
        ('Bisnis', 'UMKM', 54),
        ('Reseller', 'Korporat', 18)
    ]
    
    sumber_list = ['Instagram', 'Referensi', 'WhatsApp', 'Marketplace', 'Website', 'TikTok']
    
    pelanggan_data = []
    pelanggan_id = 1
    
    for jenis, segmen, count in jenis_pelanggan_dist:
        for i in range(count):
            nama = f"{random.choice(nama_depan)} {random.choice(nama_belakang)}"
            
            if jenis == 'Bisnis':
                prefixes = ['PT', 'CV', 'UD', 'Toko']
                nama = f"{random.choice(prefixes)} {nama}"
            
            days_ago = random.randint(1, 540)
            tanggal_reg = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
            
            kota_weights = [k[3] for k in kota_list]
            kota_info = random.choices(kota_list, weights=kota_weights, k=1)[0]
            kota, provinsi, kode_pos, _ = kota_info
            
            phone = f"08{random.randint(1000000000, 9999999999)}"
            email_name = nama.lower().replace(' ', '.').replace('pt.', '').replace('cv.', '').replace('ud.', '').replace('toko', '')
            email = f"{email_name}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])}"
            
            if jenis == 'Individu':
                rand = random.random()
                if rand < 0.55:
                    total_trans = 1
                elif rand < 0.85:
                    total_trans = random.randint(2, 3)
                else:
                    total_trans = random.randint(4, 8)
            elif jenis == 'Bisnis':
                total_trans = random.randint(2, 10)
            else:
                total_trans = random.randint(5, 15)
            
            total_nilai = total_trans * random.randint(150000, 800000)
            status = 'Aktif' if random.random() > 0.15 else 'Tidak Aktif'
            sumber = random.choice(sumber_list)
            
            alamat = f"Jl. {random.choice(['Raya', 'Utama', 'Sentosa', 'Mawar', 'Melati', 'Anggrek'])} No.{random.randint(1, 150)}"
            
            pelanggan_data.append({
                'id_pelanggan': f'C{pelanggan_id:03d}',
                'nama_lengkap': nama,
                'nomor_telepon': phone,
                'email': email,
                'alamat_lengkap': alamat,
                'kota': kota,
                'provinsi': provinsi,
                'kode_pos': kode_pos,
                'jenis_pelanggan': jenis,
                'segmen': segmen,
                'tanggal_registrasi': tanggal_reg,
                'total_transaksi': total_trans,
                'total_nilai_pembelian': total_nilai,
                'status': status,
                'sumber_awal': sumber
            })
            
            pelanggan_id += 1
    
    with open('02_master_pelanggan.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['id_pelanggan', 'nama_lengkap', 'nomor_telepon', 'email', 'alamat_lengkap', 
                      'kota', 'provinsi', 'kode_pos', 'jenis_pelanggan', 'segmen', 
                      'tanggal_registrasi', 'total_transaksi', 'total_nilai_pembelian', 
                      'status', 'sumber_awal']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(pelanggan_data)
    
    print(f"✅ Generated {len(pelanggan_data)} pelanggan")
    return pelanggan_data

def generate_transaksi(produk_list, pelanggan_list):
    """Generate 320 transaksi"""
    print("Generating transaksi data...")
    
    bulan_dist = [
        ('2024-11', 22), ('2024-12', 38), ('2025-01', 30), ('2025-02', 17),
        ('2025-03', 24), ('2025-04', 23), ('2025-05', 25), ('2025-06', 36),
        ('2025-07', 35), ('2025-08', 29), ('2025-09', 16), ('2025-10', 25)
    ]
    
    channel_dist = [('WhatsApp', 0.45), ('Instagram', 0.30), ('Marketplace', 0.15), ('Offline', 0.10)]
    payment_method_dist = [('Transfer Bank', 0.55), ('E-wallet', 0.30), ('COD', 0.15)]
    status_pesanan_dist = [('Diterima', 0.75), ('Selesai', 0.10), ('Dikirim', 0.05), ('Proses', 0.05), ('Dibatalkan', 0.05)]
    
    transaksi_data = []
    transaksi_id = 1
    
    for bulan, jumlah in bulan_dist:
        year, month = bulan.split('-')
        
        for i in range(jumlah):
            day = random.randint(1, 27 if month == '10' else 28)
            hour = random.choice(list(range(10, 15)) + list(range(19, 22))) if random.random() < 0.6 else random.randint(8, 21)
            
            tanggal = f"{year}-{month}-{day:02d} {hour:02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
            
            pelanggan = random.choice(pelanggan_list)
            produk = random.choice(produk_list)
            
            jumlah_item = random.choices([1, 2, 3], weights=[0.75, 0.20, 0.05], k=1)[0]
            harga_satuan = int(produk['harga_jual'])
            subtotal = harga_satuan * jumlah_item
            
            if random.random() < 0.20:
                diskon_persen = random.choice([5, 10, 15, 20])
                diskon_nominal = int(subtotal * diskon_persen / 100)
            else:
                diskon_persen = 0
                diskon_nominal = 0
            
            biaya_custom = random.choice([0, 25000, 50000, 75000]) if 'Custom' in produk['sub_kategori'] and random.random() < 0.30 else 0
            
            if pelanggan['kota'] == 'Depok':
                biaya_ongkir = random.choice([0, 10000, 15000])
            elif 'Jakarta' in pelanggan['kota']:
                biaya_ongkir = random.choice([15000, 20000, 25000])
            else:
                biaya_ongkir = random.choice([25000, 35000, 45000])
            
            total_pembayaran = subtotal - diskon_nominal + biaya_custom + biaya_ongkir
            
            channel = random.choices([c[0] for c in channel_dist], weights=[c[1] for c in channel_dist], k=1)[0]
            metode_bayar = random.choices([p[0] for p in payment_method_dist], weights=[p[1] for p in payment_method_dist], k=1)[0]
            
            if metode_bayar == 'COD':
                status_bayar = random.choice(['Lunas', 'Belum Bayar'])
            else:
                status_bayar = random.choices(['Lunas', 'DP', 'Belum Bayar'], weights=[0.85, 0.10, 0.05], k=1)[0]
            
            status_pesanan = random.choices([s[0] for s in status_pesanan_dist], weights=[s[1] for s in status_pesanan_dist], k=1)[0]
            
            if status_pesanan == 'Dibatalkan':
                waktu_pengerjaan = 0
                tanggal_selesai = ''
                rating = ''
            else:
                waktu_pengerjaan = random.choices([1, 2, 3, 4, 5, 6, 7], weights=[0.05, 0.15, 0.30, 0.25, 0.15, 0.07, 0.03], k=1)[0]
                if status_pesanan in ['Diterima', 'Selesai']:
                    tanggal_obj = datetime.strptime(tanggal, '%Y-%m-%d %H:%M:%S')
                    tanggal_selesai = (tanggal_obj + timedelta(days=waktu_pengerjaan)).strftime('%Y-%m-%d')
                    rating = random.choices([5, 4, 3, 2, 1], weights=[0.60, 0.25, 0.10, 0.03, 0.02], k=1)[0]
                else:
                    tanggal_selesai = ''
                    rating = ''
            
            catatan = random.choice(['', 'Mohon dikemas rapi', 'Pengerjaan dipercepat', 'Custom sesuai foto', 'Kirim via JNE']) if random.random() < 0.25 else ''
            
            transaksi_data.append({
                'id_transaksi': f'TRX{transaksi_id:04d}',
                'tanggal_transaksi': tanggal,
                'id_pelanggan': pelanggan['id_pelanggan'],
                'id_produk': produk['id_produk'],
                'jumlah_item': jumlah_item,
                'harga_satuan': harga_satuan,
                'subtotal': subtotal,
                'diskon_persen': diskon_persen,
                'diskon_nominal': diskon_nominal,
                'biaya_custom': biaya_custom,
                'biaya_ongkir': biaya_ongkir,
                'total_pembayaran': total_pembayaran,
                'metode_pembayaran': metode_bayar,
                'status_pembayaran': status_bayar,
                'status_pesanan': status_pesanan,
                'channel_penjualan': channel,
                'catatan_pesanan': catatan,
                'waktu_pengerjaan_hari': waktu_pengerjaan,
                'rating_pelanggan': rating,
                'tanggal_selesai': tanggal_selesai
            })
            
            transaksi_id += 1
    
    with open('03_transaksi_penjualan.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['id_transaksi', 'tanggal_transaksi', 'id_pelanggan', 'id_produk', 
                      'jumlah_item', 'harga_satuan', 'subtotal', 'diskon_persen', 'diskon_nominal',
                      'biaya_custom', 'biaya_ongkir', 'total_pembayaran', 'metode_pembayaran',
                      'status_pembayaran', 'status_pesanan', 'channel_penjualan', 'catatan_pesanan',
                      'waktu_pengerjaan_hari', 'rating_pelanggan', 'tanggal_selesai']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transaksi_data)
    
    total_revenue = sum([t['total_pembayaran'] for t in transaksi_data])
    print(f"✅ Generated {len(transaksi_data)} transaksi")
    print(f"   Total Revenue: Rp {total_revenue:,.0f}")
    return transaksi_data

def main():
    """Main function"""
    print("="*60)
    print("SATRIAMART - Business Intelligence Data Generator")
    print("="*60)
    
    # Load produk
    produk_list = []
    with open('01_master_produk.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        produk_list = list(reader)
    print(f"✅ Loaded {len(produk_list)} produk")
    
    # Generate all data
    pelanggan_list = generate_pelanggan()
    transaksi_list = generate_transaksi(produk_list, pelanggan_list)
    
    print("\n" + "="*60)
    print("✅ Data generation completed successfully!")
    print("="*60)
    print("\nGenerated files:")
    print("  - 01_master_produk.csv (50 products)")
    print("  - 02_master_pelanggan.csv (180 customers)")
    print("  - 03_transaksi_penjualan.csv (320 transactions)")
    print("\n📊 Ready for Google Sheets import!")

if __name__ == "__main__":
    main()
