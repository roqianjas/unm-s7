# ANALISIS DAN DESAIN SISTEM - PART 3
## SATRIAMART Integrated Management System (SIMS)
### Activity Diagram - Alur Proses Bisnis

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi II**  
**Pertemuan 4 - Activity Diagram**

---

## 3. ACTIVITY DIAGRAM

Activity Diagram menggambarkan alur kerja (workflow) dari proses bisnis dalam sistem SATRIAMART SIMS. Diagram ini menunjukkan aktivitas-aktivitas yang dilakukan oleh berbagai aktor dan keputusan yang diambil dalam proses tersebut.

---

### 3.1 Activity Diagram - Proses Registrasi Customer dan Pembuatan Order

```
┌─────────────────────────────────────────────────────────────────────────────┐
│        ACTIVITY DIAGRAM: REGISTRASI CUSTOMER DAN PEMBUATAN ORDER             │
└─────────────────────────────────────────────────────────────────────────────┘

SALES STAFF                    SYSTEM                         CUSTOMER
     │                           │                                │
     │ (START)                   │                                │
     │                           │                                │
     ▼                           │                                │
┌─────────────────┐              │                                │
│ Terima Inquiry  │              │                                │
│ dari Customer   │◄─────────────┼────────────────────────────────┤
└────────┬────────┘              │                                │
         │                       │                                │
         ▼                       │                                │
    ┌────────┐                   │                                │
    │Customer│                   │                                │
    │Baru?   │                   │                                │
    └───┬────┘                   │                                │
        │                        │                                │
     [YES]                    [NO]                                │
        │                        │                                │
        ▼                        ▼                                │
┌──────────────────┐    ┌──────────────────┐                     │
│ Buka Form        │    │ Cari Customer    │                     │
│ Registrasi       │    │ di Database      │                     │
└────────┬─────────┘    └────────┬─────────┘                     │
         │                       │                                │
         ▼                       ▼                                │
┌──────────────────┐    ┌──────────────────┐                     │
│ Input Data:      │    │ Tampilkan Data   │                     │
│ - Nama           │    │ Customer         │                     │
│ - Email          │    └────────┬─────────┘                     │
│ - Phone          │             │                                │
│ - Alamat         │             │                                │
│ - Tipe Customer  │             │                                │
└────────┬─────────┘             │                                │
         │                       │                                │
         ▼                       │                                │
┌──────────────────┐             │                                │
│ Submit Form      │             │                                │
└────────┬─────────┘             │                                │
         │                       │                                │
         ├───────────────────────┼►                               │
         │                       │                                │
         │                       ▼                                │
         │              ┌──────────────────┐                      │
         │              │ Validasi Input:  │                      │
         │              │ - Email Format   │                      │
         │              │ - Phone Number   │                      │
         │              │ - Required Field │                      │
         │              └────────┬─────────┘                      │
         │                       │                                │
         │                  ┌────┴────┐                           │
         │                  │ Valid?  │                           │
         │                  └────┬────┘                           │
         │                       │                                │
         │                    [NO]                             [YES]
         │                       │                                │
         │                       ▼                                ▼
         │              ┌──────────────────┐          ┌──────────────────┐
         │              │ Tampilkan Error  │          │ Generate Customer│
         │◄─────────────│ Message          │          │ Code (AUTO)      │
         │              └──────────────────┘          └────────┬─────────┘
         │                                                     │
         │                                                     ▼
         │                                            ┌──────────────────┐
         │                                            │ Simpan ke        │
         │                                            │ Database         │
         │                                            └────────┬─────────┘
         │                                                     │
         │                                                     ▼
         │                                            ┌──────────────────┐
         │◄───────────────────────────────────────────│ Tampilkan Sukses │
         │                                            │ & Customer Detail│
         │                                            └──────────────────┘
         │                                                     │
         │◄────────────────────────────────────────────────────┤
         │                                                     │
         ▼                                                     │
┌──────────────────┐                                           │
│ Customer         │                                           │
│ Ingin Order?     │                                           │
└───┬──────────────┘                                           │
    │                                                          │
 [YES]                                                      [NO]
    │                                                          │
    ▼                                                          ▼
┌──────────────────┐                                    ┌─────────────┐
│ Buka Form        │                                    │   (END)     │
│ Create Order     │                                    └─────────────┘
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Tampilkan        │◄────────────────┐
│ Katalog Produk   │                 │
└────────┬─────────┘                 │
         │                           │
         ▼                           │
┌──────────────────┐                 │
│ Pilih Produk     │                 │
│ & Input Quantity │                 │
└────────┬─────────┘                 │
         │                           │
         ▼                           │
┌──────────────────┐                 │
│ Input Spesifikasi│                 │
│ Khusus (Optional)│                 │
└────────┬─────────┘                 │
         │                           │
         ▼                           │
    ┌────────┐                       │
    │ Tambah │                       │
    │ Produk?│                       │
    └───┬────┘                       │
        │                            │
     [YES]──────────────────────────►│
        │
     [NO]
        │
        ▼
┌──────────────────┐
│ Input Delivery   │
│ Date (Estimasi)  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Review Order     │
│ Summary          │
└────────┬─────────┘
         │
         ├───────────────────────────►
         │                           │
         │                           ▼
         │                  ┌──────────────────┐
         │                  │ Calculate Total: │
         │                  │ Sum(Price × Qty) │
         │                  └────────┬─────────┘
         │                           │
         │                           ▼
         │                  ┌──────────────────┐
         │                  │ Ada Discount?    │
         │                  └────────┬─────────┘
         │                           │
         │                        [YES]
         │                           │
         │                           ▼
         │                  ┌──────────────────┐
         │◄─────────────────│ Apply Discount   │
         │                  │ Recalculate Total│
         │                  └──────────────────┘
         │                           │
         │◄──────────────────────────┤
         │                        [NO]
         ▼                           │
┌──────────────────┐                 │
│ Konfirmasi Order │◄────────────────┘
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Submit Order     │
└────────┬─────────┘
         │
         ├───────────────────────────►
         │                           │
         │                           ▼
         │                  ┌──────────────────┐
         │                  │ Generate Order   │
         │                  │ Number (AUTO)    │
         │                  └────────┬─────────┘
         │                           │
         │                           ▼
         │                  ┌──────────────────┐
         │                  │ Set Status:      │
         │                  │ "PENDING"        │
         │                  └────────┬─────────┘
         │                           │
         │                           ▼
         │                  ┌──────────────────┐
         │                  │ Simpan Order     │
         │                  │ ke Database      │
         │                  └────────┬─────────┘
         │                           │
         │                           ▼
         │                  ┌──────────────────┐
         │                  │ Kirim Notifikasi │
         │                  │ ke Customer      │────────────────────►
         │                  │ (Email/WhatsApp) │                    │
         │                  └────────┬─────────┘                    │
         │                           │                              │
         │                           ▼                              ▼
         │                  ┌──────────────────┐          ┌─────────────────┐
         │◄─────────────────│ Tampilkan Order  │          │ Customer Terima │
         │                  │ Confirmation     │          │ Konfirmasi Order│
         │                  └──────────────────┘          └─────────────────┘
         │
         ▼
┌──────────────────┐
│ Print Order      │
│ (Optional)       │
└────────┬─────────┘
         │
         ▼
     (END)
```

**Keterangan:**
- **Sales Staff:** Melakukan registrasi customer dan membuat order
- **System:** Melakukan validasi, generate kode otomatis, simpan data, kirim notifikasi
- **Customer:** Menerima konfirmasi order

**Decision Points:**
1. Apakah customer baru? (Ya → Registrasi, Tidak → Cari existing customer)
2. Apakah data valid? (Ya → Lanjut, Tidak → Tampilkan error)
3. Apakah customer ingin order? (Ya → Buat order, Tidak → Selesai)
4. Tambah produk lagi? (Ya → Kembali pilih produk, Tidak → Lanjut)
5. Ada discount? (Ya → Apply discount, Tidak → Lanjut)

---

### 3.2 Activity Diagram - Proses Stock Opname (Inventory)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            ACTIVITY DIAGRAM: PROSES STOCK OPNAME                             │
└─────────────────────────────────────────────────────────────────────────────┘

INVENTORY STAFF              SYSTEM                        MANAGER
     │                         │                              │
     │ (START)                 │                              │
     │                         │                              │
     ▼                         │                              │
┌──────────────────┐           │                              │
│ Login ke Sistem  │           │                              │
└────────┬─────────┘           │                              │
         │                     │                              │
         ▼                     │                              │
┌──────────────────┐           │                              │
│ Pilih Menu       │           │                              │
│ "Stock Opname"   │           │                              │
└────────┬─────────┘           │                              │
         │                     │                              │
         ▼                     │                              │
┌──────────────────┐           │                              │
│ Create Opname    │           │                              │
│ Session          │           │                              │
└────────┬─────────┘           │                              │
         │                     │                              │
         ▼                     │                              │
┌──────────────────┐           │                              │
│ Input Cut-off    │           │                              │
│ Date & Time      │           │                              │
└────────┬─────────┘           │                              │
         │                     │                              │
         ▼                     │                              │
┌──────────────────┐           │                              │
│ Pilih Kategori   │           │                              │
│ yang di-Opname   │           │                              │
│ (All/Spesifik)   │           │                              │
└────────┬─────────┘           │                              │
         │                     │                              │
         ├─────────────────────►                              │
         │                     │                              │
         │                     ▼                              │
         │            ┌──────────────────┐                    │
         │            │ Generate List    │                    │
         │            │ Material/Produk  │                    │
         │            │ dengan Current   │                    │
         │            │ Stock (System)   │                    │
         │            └────────┬─────────┘                    │
         │                     │                              │
         │                     ▼                              │
         │            ┌──────────────────┐                    │
         │◄───────────│ Tampilkan Stock  │                    │
         │            │ Count Sheet      │                    │
         │            └──────────────────┘                    │
         │                                                     │
         ▼                                                     │
┌──────────────────┐                                           │
│ Print Count      │                                           │
│ Sheet            │                                           │
└────────┬─────────┘                                           │
         │                                                     │
         ▼                                                     │
┌──────────────────┐                                           │
│ Lakukan Physical │                                           │
│ Count di Gudang  │                                           │
│ (Manual)         │                                           │
└────────┬─────────┘                                           │
         │                                                     │
         ▼                                                     │
┌──────────────────┐                                           │
│ Input Physical   │◄──────────────┐                          │
│ Count Result     │               │                          │
│ per Item         │               │                          │
└────────┬─────────┘               │                          │
         │                         │                          │
         ▼                         │                          │
    ┌────────┐                     │                          │
    │ Semua  │                     │                          │
    │ Item   │                     │                          │
    │Counted?│                     │                          │
    └───┬────┘                     │                          │
        │                          │                          │
     [NO]─────────────────────────►│                          │
        │                                                      │
     [YES]                                                     │
        │                                                      │
        ▼                                                      │
┌──────────────────┐                                           │
│ Submit Physical  │                                           │
│ Count            │                                           │
└────────┬─────────┘                                           │
         │                                                     │
         ├─────────────────────►                               │
         │                     │                               │
         │                     ▼                               │
         │            ┌──────────────────┐                     │
         │            │ Compare:         │                     │
         │            │ Physical Count   │                     │
         │            │ vs System Count  │                     │
         │            └────────┬─────────┘                     │
         │                     │                               │
         │                     ▼                               │
         │            ┌──────────────────┐                     │
         │            │ Calculate        │                     │
         │            │ Variance:        │                     │
         │            │ Physical - System│                     │
         │            └────────┬─────────┘                     │
         │                     │                               │
         │                     ▼                               │
         │            ┌──────────────────┐                     │
         │            │ Generate         │                     │
         │            │ Variance Report  │                     │
         │            │ - Item Name      │                     │
         │            │ - System Stock   │                     │
         │            │ - Physical Stock │                     │
         │            │ - Variance       │                     │
         │            └────────┬─────────┘                     │
         │                     │                               │
         │                     ▼                               │
         │            ┌──────────────────┐                     │
         │◄───────────│ Tampilkan        │                     │
         │            │ Variance Report  │                     │
         │            └──────────────────┘                     │
         │                                                     │
         ▼                                                     │
    ┌────────┐                                                 │
    │  Ada   │                                                 │
    │Variance│                                                 │
    │  ?     │                                                 │
    └───┬────┘                                                 │
        │                                                      │
     [NO]                                                   [YES]
        │                                                      │
        ▼                                                      ▼
┌──────────────────┐                            ┌──────────────────┐
│ Close Opname     │                            │ Input Reason for │
│ Session          │                            │ Variance         │
│ (No Adjustment)  │                            │ (Penjelasan)     │
└────────┬─────────┘                            └────────┬─────────┘
         │                                               │
         │                                               ▼
         │                                      ┌──────────────────┐
         │                                      │ Upload Photo     │
         │                                      │ Bukti (Optional) │
         │                                      └────────┬─────────┘
         │                                               │
         │                                               ▼
         │                                      ┌──────────────────┐
         │                                      │ Create Stock     │
         │                                      │ Adjustment       │
         │                                      │ Request          │
         │                                      └────────┬─────────┘
         │                                               │
         │                                               ├──────────►
         │                                               │          │
         │                                               │          ▼
         │                                               │ ┌──────────────────┐
         │                                               │ │ Kirim Notifikasi │
         │                                               │ │ ke Manager untuk │
         │                                               │ │ Approval         │
         │                                               │ └────────┬─────────┘
         │                                               │          │
         │                                               │          ▼
         │                                               │ ┌──────────────────┐
         │                                               │ │ Manager Review   │
         │                                               │ │ Variance Report  │
         │                                               │ │ & Reason         │
         │                                               │ └────────┬─────────┘
         │                                               │          │
         │                                               │          ▼
         │                                               │     ┌────────┐
         │                                               │     │Approve?│
         │                                               │     └───┬────┘
         │                                               │         │
         │                                               │      [NO]
         │                                               │         │
         │                                               │         ▼
         │                                               │ ┌──────────────────┐
         │                                               │ │ Reject           │
         │                                               │ │ Adjustment       │
         │                                               │ └────────┬─────────┘
         │                                               │          │
         │                                               │          ├──────────►
         │                                               │          │          │
         │                                               │          │          ▼
         │                                               │          │ ┌──────────────────┐
         │◄──────────────────────────────────────────────┼──────────┼─│ Kirim Notifikasi │
         │                                               │          │ │ Rejection ke     │
         │                                               │          │ │ Inventory Staff  │
         │                                               │          │ └──────────────────┘
         │                                               │          │
         │                                               │       [YES]
         │                                               │          │
         │                                               │          ▼
         │                                               │ ┌──────────────────┐
         │                                               │ │ Approve          │
         │                                               │ │ Adjustment       │
         │                                               │ └────────┬─────────┘
         │                                               │          │
         │                                               │          ├──────────►
         │                                               │          │          │
         │                                               │          │          ▼
         │                                               │          │ ┌──────────────────┐
         │                                               │          │ │ Update Stock     │
         │                                               │          │ │ Level sesuai     │
         │                                               │          │ │ Physical Count   │
         │                                               │          │ └────────┬─────────┘
         │                                               │          │          │
         │                                               │          │          ▼
         │                                               │          │ ┌──────────────────┐
         │                                               │          │ │ Create Audit     │
         │                                               │          │ │ Trail Record     │
         │                                               │          │ └────────┬─────────┘
         │                                               │          │          │
         │                                               │          │          ▼
         │                                               │          │ ┌──────────────────┐
         │◄──────────────────────────────────────────────┼──────────┼─│ Kirim Notifikasi │
         │                                               │          │ │ Approval ke      │
         │                                               │          │ │ Inventory Staff  │
         │                                               │          │ └──────────────────┘
         │◄──────────────────────────────────────────────┘          │
         │                                                           │
         ▼                                                           │
┌──────────────────┐                                                 │
│ View Opname      │                                                 │
│ Result & Report  │                                                 │
└────────┬─────────┘                                                 │
         │                                                           │
         ▼                                                           │
     (END)◄─────────────────────────────────────────────────────────┘
```

**Keterangan:**
- **Inventory Staff:** Melakukan physical count dan input hasil
- **System:** Generate list, calculate variance, update stock
- **Manager:** Review dan approval untuk stock adjustment

**Decision Points:**
1. Semua item sudah dicount? (Ya → Submit, Tidak → Lanjut count)
2. Ada variance? (Ya → Create adjustment request, Tidak → Close session)
3. Manager approve adjustment? (Ya → Update stock, Tidak → Reject)

---

### 3.3 Activity Diagram - Proses Produksi (Work Order hingga Quality Control)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│          ACTIVITY DIAGRAM: PROSES PRODUKSI - WORK ORDER TO QC                │
└─────────────────────────────────────────────────────────────────────────────┘

SUPERVISOR                SYSTEM                PRODUCTION STAFF
     │                      │                           │
     │ (START)              │                           │
     │                      │                           │
     ▼                      │                           │
┌──────────────┐            │                           │
│ Terima       │◄───────────┼───────────────────────────┤
│ Customer     │            │                      (Trigger dari
│ Order Baru   │            │                       Sales Order)
└──────┬───────┘            │                           │
       │                    │                           │
       ▼                    │                           │
┌──────────────┐            │                           │
│ Review Order │            │                           │
│ Requirement  │            │                           │
└──────┬───────┘            │                           │
       │                    │                           │
       ├────────────────────►                           │
       │                    │                           │
       │                    ▼                           │
       │           ┌──────────────────┐                 │
       │           │ Check Material   │                 │
       │           │ Availability     │                 │
       │           └────────┬─────────┘                 │
       │                    │                           │
       │                    ▼                           │
       │               ┌─────────┐                      │
       │               │Material │                      │
       │               │Cukup?   │                      │
       │               └────┬────┘                      │
       │                    │                           │
       │                 [NO]                        [YES]
       │                    │                           │
       │                    ▼                           ▼
       │           ┌──────────────────┐       ┌──────────────────┐
       │◄──────────│ Alert: Material  │       │ Generate BOM     │
       │           │ Tidak Cukup      │       │ (Bill of         │
       │           │ Suggest PR       │       │  Materials)      │
       │           └──────────────────┘       └────────┬─────────┘
       │                                               │
       │◄──────────────────────────────────────────────┘
       │
       ▼
┌──────────────┐
│ Create Work  │
│ Order        │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Input:       │
│ - Product    │
│ - Quantity   │
│ - Specs      │
│ - Due Date   │
│ - Priority   │
└──────┬───────┘
       │
       ├────────────────────►
       │                    │
       │                    ▼
       │           ┌──────────────────┐
       │           │ Generate WO      │
       │           │ Number (AUTO)    │
       │           └────────┬─────────┘
       │                    │
       │                    ▼
       │           ┌──────────────────┐
       │           │ Reserve Material │
       │           │ untuk WO ini     │
       │           └────────┬─────────┘
       │                    │
       │                    ▼
       │           ┌──────────────────┐
       │           │ Set Status:      │
       │           │ "SCHEDULED"      │
       │           └────────┬─────────┘
       │                    │
       │           ┌────────▼─────────┐
       │◄──────────│ Simpan WO ke     │
       │           │ Database         │
       │           └──────────────────┘
       │
       ▼
┌──────────────┐
│ Assign WO ke │
│ Production   │
│ Staff        │
└──────┬───────┘
       │
       ├────────────────────────────────────────────────►
       │                    │                           │
       │                    ▼                           │
       │           ┌──────────────────┐                 │
       │           │ Send Notifikasi  │─────────────────►
       │           │ Assignment ke    │                 │
       │           │ Staff            │                 │
       │           └──────────────────┘                 │
       │                                                │
       │                                                ▼
       │                                       ┌──────────────┐
       │                                       │ Terima WO    │
       │                                       │ Assignment   │
       │                                       └──────┬───────┘
       │                                              │
       │                                              ▼
       │                                       ┌──────────────┐
       │                                       │ Review WO    │
       │                                       │ Details &    │
       │                                       │ BOM          │
       │                                       └──────┬───────┘
       │                                              │
       │                                              ▼
       │                                       ┌──────────────┐
       │                                       │ Ambil Material│
       │                                       │ dari Gudang  │
       │                                       └──────┬───────┘
       │                                              │
       │                                              ▼
       │                                       ┌──────────────┐
       │                                       │ Klik "Start  │
       │                                       │ Production"  │
       │                                       └──────┬───────┘
       │                                              │
       │                                              ├──────────►
       │                                              │          │
       │                                              │          ▼
       │                                              │ ┌──────────────────┐
       │                                              │ │ Update Status:   │
       │                                              │ │ "IN PROGRESS"    │
       │                                              │ └────────┬─────────┘
       │                                              │          │
       │                                              │          ▼
       │                                              │ ┌──────────────────┐
       │                                              │ │ Start Timer      │
       │                                              │ └──────────────────┘
       │                                              │
       │                                              ▼
       │                                       ┌──────────────┐
       │                                       │ Proses       │◄─────┐
       │                                       │ Produksi:    │      │
       │                                       │ - Cutting    │      │
       │                                       │ - Polishing  │      │
       │                                       │ - Assembly   │      │
       │                                       └──────┬───────┘      │
       │                                              │              │
       │                                              ▼              │
       │                                       ┌──────────────┐      │
       │                                       │ Update       │      │
       │                                       │ Progress     │      │
       │                                       │ (% Complete) │      │
       │                                       └──────┬───────┘      │
       │                                              │              │
       │                                              ├──────────────►
       │                                              │              │
       │                                              │              ▼
       │                                              │     ┌──────────────────┐
       │                                              │     │ Input % Complete │
       │                                              │     └────────┬─────────┘
       │                                              │              │
       │                                              │              ▼
       │                                              │     ┌──────────────────┐
       │                                              │     │ Record Material  │
       │                                              │     │ Consumption      │
       │                                              │     │ (Actual Usage)   │
       │                                              │     └────────┬─────────┘
       │                                              │              │
       │                                              │              ▼
       │                                              │     ┌──────────────────┐
       │                                              │     │ Upload WIP Photo │
       │                                              │     │ (Optional)       │
       │                                              │     └────────┬─────────┘
       │                                              │              │
       │                                              │              ▼
       │                                              │     ┌──────────────────┐
       │                                              │     │ Update Inventory │
       │                                              │     │ (Deduct Stock)   │
       │                                              │     └────────┬─────────┘
       │                                              │              │
       │                                              │              ▼
       │                                              │        ┌─────────┐
       │                                              │        │Progress │
       │                                              │        │= 100%?  │
       │                                              │        └────┬────┘
       │                                              │             │
       │                                              │          [NO]
       │                                              │             │
       │                                              │             └──────────┘
       │                                              │
       │                                              │          [YES]
       │                                              │             │
       │                                              ├◄────────────┘
       │                                              │
       │                                              ▼
       │                                       ┌──────────────┐
       │                                       │ Click        │
       │                                       │ "Complete    │
       │                                       │ Production"  │
       │                                       └──────┬───────┘
       │                                              │
       │                                              ├──────────────►
       │                                              │              │
       │                                              │              ▼
       │                                              │     ┌──────────────────┐
       │                                              │     │ Update Status:   │
       │                                              │     │ "QUALITY CHECK"  │
       │                                              │     └────────┬─────────┘
       │                                              │              │
       │                                              │              ▼
       │                                              │     ┌──────────────────┐
       │◄─────────────────────────────────────────────┼─────│ Notifikasi ke    │
       │                                              │     │ Supervisor untuk │
       │                                              │     │ QC               │
       │                                              │     └──────────────────┘
       │
       ▼
┌──────────────┐
│ Terima QC    │
│ Request      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Akses QC     │
│ Checklist    │
└──────┬───────┘
       │
       ├────────────────────►
       │                    │
       │                    ▼
       │           ┌──────────────────┐
       │◄──────────│ Load QC Checklist│
       │           │ Template sesuai  │
       │           │ Product Type     │
       │           └──────────────────┘
       │
       ▼
┌──────────────┐
│ Inspeksi     │◄─────────┐
│ Produk:      │          │
│ - Dimensi    │          │
│ - Kualitas   │          │
│ - Finishing  │          │
│ - Packaging  │          │
└──────┬───────┘          │
       │                  │
       ▼                  │
┌──────────────┐          │
│ Input Result │          │
│ per Checklist│          │
│ Item         │          │
│ (Pass/Fail)  │          │
└──────┬───────┘          │
       │                  │
       ▼                  │
   ┌───────┐              │
   │ Semua │              │
   │ Item  │              │
   │Checked│              │
   └───┬───┘              │
       │                  │
    [NO]─────────────────►│
       │
    [YES]
       │
       ▼
┌──────────────┐
│ Overall QC   │
│ Decision     │
└──────┬───────┘
       │
       ▼
   ┌───────┐
   │ PASS? │
   └───┬───┘
       │
    [NO]                                              [YES]
       │                                                 │
       ▼                                                 ▼
┌──────────────┐                                  ┌──────────────┐
│ Input Defect │                                  │ Approve QC   │
│ Type & Root  │                                  └──────┬───────┘
│ Cause        │                                         │
└──────┬───────┘                                         ├──────────────►
       │                                                 │              │
       ▼                                                 │              ▼
┌──────────────┐                                         │     ┌──────────────────┐
│ Upload Defect│                                         │     │ Update Status:   │
│ Photo        │                                         │     │ "COMPLETED"      │
└──────┬───────┘                                         │     └────────┬─────────┘
       │                                                 │              │
       ├──────────────────►                              │              ▼
       │                  │                              │     ┌──────────────────┐
       │                  ▼                              │     │ Move to Finished │
       │         ┌──────────────────┐                    │     │ Goods Inventory  │
       │         │ Create Rework WO │                    │     └────────┬─────────┘
       │         └────────┬─────────┘                    │              │
       │                  │                              │              ▼
       │                  ▼                              │     ┌──────────────────┐
       │         ┌──────────────────┐                    │     │ Update Customer  │
       │         │ Assign to        │────────────────────┼─────│ Order Status:    │
       │         │ Production Staff │                    │     │ "READY"          │
       │         └────────┬─────────┘                    │     └────────┬─────────┘
       │                  │                              │              │
       │                  │                              │              ▼
       │                  └──────────────────────────────┼────►┌──────────────────┐
       │                                                 │     │ Notifikasi ke    │
       │                                                 │     │ Sales Team       │
       │                                                 │     └──────────────────┘
       │                                                 │
       ▼                                                 ▼
     (LOOP BACK                                       (END)
      TO PRODUCTION)
```

**Keterangan:**
- **Supervisor:** Membuat WO, assign ke staff, melakukan QC
- **System:** Generate WO number, reserve material, update status
- **Production Staff:** Melakukan produksi dan update progress

**Decision Points:**
1. Material cukup? (Ya → Lanjut create WO, Tidak → Alert & suggest PR)
2. Progress = 100%? (Ya → Trigger QC, Tidak → Lanjut produksi)
3. Semua checklist item di-check? (Ya → Make decision, Tidak → Lanjut inspect)
4. QC Pass? (Ya → Move to finished goods, Tidak → Create rework WO)

---

### 3.4 Activity Diagram - Proses Purchase Requisition hingga Purchase Order

```
┌─────────────────────────────────────────────────────────────────────────────┐
│       ACTIVITY DIAGRAM: PURCHASE REQUISITION TO PURCHASE ORDER               │
└─────────────────────────────────────────────────────────────────────────────┘

INVENTORY STAFF          SYSTEM              MANAGER           SUPPLIER
     │                     │                    │                  │
     │ (START)             │                    │                  │
     │                     │                    │                  │
     ▼                     │                    │                  │
┌──────────────┐           │                    │                  │
│ Monitor Stock│           │                    │                  │
│ Level        │           │                    │                  │
└──────┬───────┘           │                    │                  │
       │                   │                    │                  │
       ├───────────────────►                    │                  │
       │                   │                    │                  │
       │                   ▼                    │                  │
       │          ┌──────────────────┐          │                  │
       │          │ Check Reorder    │          │                  │
       │          │ Point Status     │          │                  │
       │          └────────┬─────────┘          │                  │
       │                   │                    │                  │
       │                   ▼                    │                  │
       │              ┌─────────┐               │                  │
       │              │ Stock   │               │                  │
       │              │< Reorder│               │                  │
       │              │ Point?  │               │                  │
       │              └────┬────┘               │                  │
       │                   │                    │                  │
       │                [YES]                [NO]                  │
       │                   │                    │                  │
       │                   ▼                    ▼                  │
       │          ┌──────────────────┐    ┌──────────┐            │
       │◄─────────│ Send Low Stock   │    │ (END)    │            │
       │          │ Alert            │    └──────────┘            │
       │          └──────────────────┘                            │
       │                                                           │
       ▼                                                           │
┌──────────────┐                                                   │
│ Create       │                                                   │
│ Purchase     │                                                   │
│ Requisition  │                                                   │
└──────┬───────┘                                                   │
       │                                                           │
       ▼                                                           │
┌──────────────┐                                                   │
│ Select       │◄──────────┐                                       │
│ Material     │           │                                       │
└──────┬───────┘           │                                       │
       │                   │                                       │
       ▼                   │                                       │
┌──────────────┐           │                                       │
│ Input Qty    │           │                                       │
│ Needed       │           │                                       │
└──────┬───────┘           │                                       │
       │                   │                                       │
       ├───────────────────►                                       │
       │                   │                                       │
       │                   ▼                                       │
       │          ┌──────────────────┐                             │
       │◄─────────│ Auto-suggest Qty │                             │
       │          │ berdasarkan      │                             │
       │          │ Reorder Qty      │                             │
       │          └──────────────────┘                             │
       │                                                           │
       ▼                                                           │
┌──────────────┐                                                   │
│ Select       │                                                   │
│ Preferred    │                                                   │
│ Supplier     │                                                   │
└──────┬───────┘                                                   │
       │                                                           │
       ├───────────────────►                                       │
       │                   │                                       │
       │                   ▼                                       │
       │          ┌──────────────────┐                             │
       │◄─────────│ Show Supplier    │                             │
       │          │ Info:            │                             │
       │          │ - Lead Time      │                             │
       │          │ - Last Price     │                             │
       │          │ - Rating         │                             │
       │          └──────────────────┘                             │
       │                                                           │
       ▼                                                           │
┌──────────────┐                                                   │
│ Input        │                                                   │
│ Justification│                                                   │
│ (Reason)     │                                                   │
└──────┬───────┘                                                   │
       │                                                           │
       ▼                                                           │
   ┌───────┐                                                       │
   │ Tambah│                                                       │
   │ Item? │                                                       │
   └───┬───┘                                                       │
       │                                                           │
    [YES]──────────────────►                                       │
       │                                                           │
    [NO]                                                           │
       │                                                           │
       ▼                                                           │
┌──────────────┐                                                   │
│ Review & Submit│                                                 │
│ PR            │                                                  │
└──────┬───────┘                                                   │
       │                                                           │
       ├───────────────────►                                       │
       │                   │                                       │
       │                   ▼                                       │
       │          ┌──────────────────┐                             │
       │          │ Generate PR      │                             │
       │          │ Number (AUTO)    │                             │
       │          └────────┬─────────┘                             │
       │                   │                                       │
       │                   ▼                                       │
       │          ┌──────────────────┐                             │
       │          │ Set Status:      │                             │
       │          │ "PENDING         │                             │
       │          │  APPROVAL"       │                             │
       │          └────────┬─────────┘                             │
       │                   │                                       │
       │                   ▼                                       │
       │          ┌──────────────────┐                             │
       │          │ Save PR to DB    │                             │
       │          └────────┬─────────┘                             │
       │                   │                                       │
       │                   ▼                                       │
       │          ┌──────────────────┐                             │
       │          │ Send Notification│─────────────────────────────►
       │          │ to Manager       │                             │
       │          └────────┬─────────┘                             │
       │                   │                                       │
       │◄──────────────────┘                                       │
       │                                                           │
       │                                                           ▼
       │                                                  ┌──────────────┐
       │                                                  │ Terima       │
       │                                                  │ Notifikasi   │
       │                                                  │ PR Approval  │
       │                                                  └──────┬───────┘
       │                                                         │
       │                                                         ▼
       │                                                  ┌──────────────┐
       │                                                  │ Review PR:   │
       │                                                  │ - Material   │
       │                                                  │ - Quantity   │
       │                                                  │ - Supplier   │
       │                                                  │ - Reason     │
       │                                                  └──────┬───────┘
       │                                                         │
       │                                                         ▼
       │                                                    ┌─────────┐
       │                                                    │Approve? │
       │                                                    └────┬────┘
       │                                                         │
       │                                                      [NO]
       │                                                         │
       │                                                         ▼
       │                                                  ┌──────────────┐
       │                                                  │ Reject PR    │
       │                                                  │ Input Reason │
       │                                                  └──────┬───────┘
       │                                                         │
       │                                                         ├────────►
       │                                                         │        │
       │                                                         │        ▼
       │                                                         │ ┌──────────────────┐
       │◄────────────────────────────────────────────────────────┼─│ Update Status:   │
       │                                                         │ │ "REJECTED"       │
       │                                                         │ └────────┬─────────┘
       │                                                         │          │
       │                                                         │          ▼
       │                                                         │ ┌──────────────────┐
       │◄────────────────────────────────────────────────────────┼─│ Notifikasi ke    │
       │                                                         │ │ Inventory Staff  │
       │                                                         │ └──────────────────┘
       │                                                         │
       │                                                      [YES]
       │                                                         │
       │                                                         ▼
       │                                                  ┌──────────────┐
       │                                                  │ Approve PR   │
       │                                                  └──────┬───────┘
       │                                                         │
       │                                                         ├────────►
       │                                                         │        │
       │                                                         │        ▼
       │                                                         │ ┌──────────────────┐
       │                                                         │ │ Update Status:   │
       │                                                         │ │ "APPROVED"       │
       │                                                         │ └────────┬─────────┘
       │                                                         │          │
       │                                                         │          ▼
       │                                                         │ ┌──────────────────┐
       │                                                         │ │ Auto-create PO   │
       │                                                         │ │ dari approved PR │
       │                                                         │ └────────┬─────────┘
       │                                                         │          │
       │                                                         │          ▼
       │                                                         │ ┌──────────────────┐
       │                                                         │ │ Generate PO      │
       │                                                         │ │ Number (AUTO)    │
       │                                                         │ └────────┬─────────┘
       │                                                         │          │
       │                                                         │          ▼
       │                                                         │ ┌──────────────────┐
       │                                                         │ │ Set Delivery     │
       │                                                         │ │ Date (based on   │
       │                                                         │ │ supplier lead    │
       │                                                         │ │ time)            │
       │                                                         │ └────────┬─────────┘
       │                                                         │          │
       │                                                         │          ▼
       │                                                         │ ┌──────────────────┐
       │                                                         │ │ Generate PO      │
       │                                                         │ │ Document (PDF)   │
       │                                                         │ └────────┬─────────┘
       │                                                         │          │
       │                                                         │          ▼
       │                                                         │ ┌──────────────────┐
       │                                                         │ │ Send PO ke       │
       │                                                         │ │ Supplier via     │──────────►
       │                                                         │ │ Email/WhatsApp   │          │
       │                                                         │ └────────┬─────────┘          │
       │                                                         │          │                    │
       │                                                         │          ▼                    ▼
       │                                                         │ ┌──────────────────┐ ┌──────────────┐
       │◄────────────────────────────────────────────────────────┼─│ Notifikasi ke    │ │ Supplier     │
       │                                                         │ │ Inventory Staff  │ │ Terima PO    │
       │                                                         │ └──────────────────┘ └──────┬───────┘
       │                                                         │                             │
       ▼                                                         │                             ▼
┌──────────────┐                                                 │                    ┌──────────────┐
│ View PO      │                                                 │                    │ Process Order│
│ Status       │                                                 │                    │ & Prepare    │
└──────┬───────┘                                                 │                    │ Delivery     │
       │                                                         │                    └──────────────┘
       ▼                                                         │
┌──────────────┐                                                 │
│ Wait for     │                                                 │
│ Delivery     │                                                 │
└──────┬───────┘                                                 │
       │                                                         │
       ▼                                                         ▼
┌──────────────┐                                              (END)
│ (Proses      │
│  berlanjut   │
│  ke Stock In)│
└──────────────┘
     │
     ▼
   (END)
```

**Keterangan:**
- **Inventory Staff:** Membuat PR dan menerima notifikasi approval
- **System:** Generate PR/PO number, send notifications, auto-create PO
- **Manager:** Review dan approval PR
- **Supplier:** Menerima PO dan proses delivery

**Decision Points:**
1. Stock < reorder point? (Ya → Alert, Tidak → End)
2. Tambah item lagi di PR? (Ya → Tambah item, Tidak → Submit)
3. Manager approve PR? (Ya → Create PO, Tidak → Reject)

---

## Ringkasan Activity Diagram

**Total Activity Diagram: 4 Proses Utama**

1. **Proses Registrasi Customer dan Pembuatan Order**
   - Melibatkan: Sales Staff, System, Customer
   - Key Decision: Customer baru?, Data valid?, Customer order?, Tambah produk?, Ada discount?

2. **Proses Stock Opname**
   - Melibatkan: Inventory Staff, System, Manager
   - Key Decision: Semua item counted?, Ada variance?, Manager approve?

3. **Proses Produksi (Work Order hingga Quality Control)**
   - Melibatkan: Supervisor, System, Production Staff
   - Key Decision: Material cukup?, Progress 100%?, All checked?, QC Pass?

4. **Proses Purchase Requisition hingga Purchase Order**
   - Melibatkan: Inventory Staff, System, Manager, Supplier
   - Key Decision: Stock < reorder point?, Tambah item?, Manager approve?

---

*Dokumen ini merupakan Part 3 dari Analisis dan Desain Sistem. Untuk Part 4 (ERD) dan Part 5 (User Interface Design), silakan lihat dokumen terpisah.*

