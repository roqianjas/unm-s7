# ANALISIS DAN DESAIN SISTEM - PART 2
## SATRIAMART Integrated Management System (SIMS)
### Use Case Diagram dan Activity Diagram

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi II**  
**Pertemuan 4 - Use Case Diagram dan Activity Diagram**

---

## 2. USE CASE DIAGRAM

### 2.1 Identifikasi Aktor

Berdasarkan analisis kebutuhan sistem, aktor-aktor yang terlibat dalam SATRIAMART SIMS adalah:

#### Aktor Utama (Primary Actors)

**1. Owner/Direktur**
- **Deskripsi:** Pemilik SATRIAMART yang bertanggung jawab atas keputusan strategis bisnis
- **Tanggung Jawab:**
  - Monitoring performa bisnis secara keseluruhan
  - Analisis sales dan profitability
  - Strategic decision making
- **Use Cases:** View Executive Dashboard, Generate Business Reports, Analyze Sales Trends

**2. Manajer Operasional**
- **Deskripsi:** Manajer yang mengelola operasional harian SATRIAMART
- **Tanggung Jawab:**
  - Koordinasi antar departemen (sales, inventory, production)
  - Monitoring operational performance
  - Approval workflow untuk transaksi penting
- **Use Cases:** Manage Operations, Approve Purchase Orders, Monitor Production, Review Inventory

**3. Staff Sales/Customer Service**
- **Deskripsi:** Karyawan yang menangani interaksi dengan customer dan order processing
- **Tanggung Jawab:**
  - Customer relationship management
  - Order processing
  - Customer inquiry handling
  - Complaint management
- **Use Cases:** Manage Customer Data, Create Order, Track Order Status, Handle Customer Complaint

**4. Staff Inventory**
- **Deskripsi:** Karyawan yang mengelola inventory dan material warehouse
- **Tanggung Jawab:**
  - Stock management (in/out transactions)
  - Stock opname
  - Material request dan purchase requisition
  - Supplier coordination
- **Use Cases:** Manage Inventory, Stock Opname, Create Purchase Requisition, Manage Suppliers

**5. Production Staff**
- **Deskripsi:** Karyawan yang melakukan proses produksi akrilik
- **Tanggung Jawab:**
  - Mengerjakan work order
  - Update production progress
  - Material consumption recording
- **Use Cases:** View Work Order, Update Production Progress, Record Material Usage

**6. Production Supervisor**
- **Deskripsi:** Supervisor yang mengawasi proses produksi
- **Tanggung Jawab:**
  - Production scheduling
  - Quality control
  - Work order assignment
  - Resource allocation
- **Use Cases:** Manage Production Schedule, Assign Work Order, Perform Quality Control, Manage Resources

**7. Admin/IT Support**
- **Deskripsi:** Administrator sistem yang mengelola user dan konfigurasi
- **Tanggung Jawab:**
  - User management
  - System configuration
  - Backup dan maintenance
  - Technical support
- **Use Cases:** Manage Users, Configure System, Perform Backup, View Audit Trail

#### Aktor Sekunder (Secondary Actors)

**8. Customer**
- **Deskripsi:** Pelanggan SATRIAMART (eksternal)
- **Interaksi:** Menerima notifikasi order status (via email/WhatsApp)
- **Use Cases:** Receive Order Notification, Track Order (future enhancement)

**9. Supplier**
- **Deskripsi:** Pemasok material akrilik dan supplies (eksternal)
- **Interaksi:** Menerima purchase order dan delivery schedule
- **Use Cases:** Receive Purchase Order Notification

**10. System (Timer/Scheduler)**
- **Deskripsi:** Automated system processes
- **Fungsi:** Trigger automated tasks (backup, reports, notifications)
- **Use Cases:** Generate Scheduled Reports, Send Automated Notifications, Perform Auto Backup

---

### 2.2 Use Case Diagram - Modul CRM (Customer Relationship Management)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SATRIAMART SIMS - CRM MODULE                      │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐                                        ┌──────────┐
    │  Sales Staff │                                        │ Customer │
    └──────┬───────┘                                        └────┬─────┘
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           ├──│ Register New Customer         │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           ├──│ Update Customer Information   │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           ├──│ Search Customer               │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           │  │ Create Customer Order         │◄────────────────┤
           ├──│ «include»                     │                 │
           │  │ - Select Products             │                 │
           │  │ - Calculate Total             │                 │
           │  │ - Generate Order Number       │                 │
           │  └───────────────────────────────┘                 │
           │                │                                    │
           │                │ «extend»                           │
           │                ▼                                    │
           │  ┌───────────────────────────────┐                 │
           │  │ Apply Discount                │                 │
           │  │ «extend»                      │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           ├──│ Track Order Status            │◄────────────────┤
           │  └───────────────────────────────┘                 │
           │                │                                    │
           │                │ «include»                          │
           │                ▼                                    │
           │  ┌───────────────────────────────┐                 │
           │  │ Send Status Notification      │─────────────────┤
           │  │ «include»                     │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           ├──│ Log Customer Communication    │                 │
           │  │ - Email, Phone, WhatsApp      │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           ├──│ Handle Customer Complaint     │                 │
           │  │ «include»                     │                 │
           │  │ - Categorize Issue            │                 │
           │  │ - Assign to Staff             │                 │
           │  │ - Track Resolution            │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           ├──│ View Customer History         │                 │
           │  │ - Order History               │                 │
           │  │ - Communication History       │                 │
           │  │ - Payment History             │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
                                                                 │
    ┌──────┴───────┐                                            │
    │   Manager    │                                            │
    └──────┬───────┘                                            │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           ├──│ Analyze Customer Behavior     │                 │
           │  │ - Top Customers               │                 │
           │  │ - Customer Segmentation       │                 │
           │  │ - RFM Analysis                │                 │
           │  └───────────────────────────────┘                 │
           │                                                     │
           │  ┌───────────────────────────────┐                 │
           └──│ Generate CRM Reports          │                 │
              │ - Customer Growth Report      │                 │
              │ - Sales by Customer Report    │                 │
              └───────────────────────────────┘                 │
                                                                 │
                                                        ┌────────┴──────┐
                                                        │    System     │
                                                        │   (Timer)     │
                                                        └────────┬──────┘
                                                                 │
                                        ┌────────────────────────┤
                                        │ Send Order Reminder    │
                                        │ «automated»            │
                                        └────────────────────────┘
```

**Deskripsi Use Case CRM:**

**UC-CRM-001: Register New Customer**
- **Aktor Utama:** Sales Staff
- **Tujuan:** Mendaftarkan customer baru ke dalam sistem
- **Precondition:** Sales staff sudah login ke sistem
- **Postcondition:** Data customer tersimpan di database dengan customer code unik
- **Main Flow:**
  1. Sales staff memilih menu "Register Customer"
  2. Sistem menampilkan form registrasi customer
  3. Sales staff input data: nama, email, phone, alamat, tipe customer
  4. Sistem validasi input (email format, phone number)
  5. Sales staff submit form
  6. Sistem generate customer code otomatis
  7. Sistem simpan data ke database
  8. Sistem tampilkan notifikasi sukses dan customer detail
- **Alternative Flow:**
  - 4a. Jika validasi gagal, sistem tampilkan error message
  - 6a. Jika customer dengan email sama sudah ada, sistem tampilkan peringatan

**UC-CRM-002: Create Customer Order**
- **Aktor Utama:** Sales Staff
- **Aktor Sekunder:** Customer (receive notification)
- **Tujuan:** Membuat order baru untuk customer
- **Precondition:** Customer sudah terdaftar di sistem
- **Postcondition:** Order tersimpan dengan status "Pending", notification terkirim ke customer
- **Main Flow:**
  1. Sales staff pilih customer (search existing)
  2. Sales staff pilih "Create Order"
  3. Sistem tampilkan form order dengan product catalog
  4. Sales staff select produk dan input quantity
  5. Sales staff input special request (optional)
  6. Sistem calculate total price otomatis
  7. Sales staff input estimated delivery date
  8. Sales staff submit order
  9. Sistem generate order number otomatis
  10. Sistem simpan order dengan status "Pending"
  11. Sistem kirim order confirmation ke customer (email/WhatsApp)
  12. Sistem tampilkan order detail dan print option
- **Include:** Calculate Total Price, Generate Order Number, Send Notification
- **Extend:** Apply Discount (jika ada discount khusus)

**UC-CRM-003: Track Order Status**
- **Aktor Utama:** Sales Staff, Customer
- **Tujuan:** Melihat status terkini dari order
- **Precondition:** Order sudah dibuat di sistem
- **Postcondition:** User mendapatkan informasi status order terkini
- **Main Flow:**
  1. User input order number atau pilih dari list
  2. Sistem retrieve order data dari database
  3. Sistem tampilkan order detail dan current status
  4. Sistem tampilkan timeline progression
  5. Sistem tampilkan estimated completion date
- **Include:** Send Status Notification (jika ada update status)

**UC-CRM-004: Handle Customer Complaint**
- **Aktor Utama:** Sales Staff
- **Tujuan:** Mengelola komplain dari customer
- **Precondition:** Sales staff sudah login
- **Postcondition:** Komplain tercatat dan assigned untuk resolution
- **Main Flow:**
  1. Sales staff pilih "Register Complaint"
  2. Sales staff select customer dan related order (jika ada)
  3. Sales staff input complaint description
  4. Sales staff select complaint category (product quality, delivery delay, dll)
  5. Sales staff set priority (low, medium, high)
  6. System assign complaint to appropriate staff
  7. System simpan complaint dengan status "Open"
  8. System send notification ke assigned staff
- **Include:** Categorize Issue, Assign to Staff

---

### 2.3 Use Case Diagram - Modul Inventory Management

```
┌─────────────────────────────────────────────────────────────────────┐
│              SATRIAMART SIMS - INVENTORY MODULE                      │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────────────┐                              ┌──────────────┐
    │ Inventory Staff  │                              │   Manager    │
    └────────┬─────────┘                              └──────┬───────┘
             │                                                │
             │  ┌──────────────────────────────┐             │
             ├──│ Manage Product Master Data   │◄────────────┤
             │  │ - Create Product             │             │
             │  │ - Update Product             │             │
             │  │ - Set Reorder Point          │             │
             │  └──────────────────────────────┘             │
             │                                                │
             │  ┌──────────────────────────────┐             │
             ├──│ Record Stock In              │             │
             │  │ «include»                    │             │
             │  │ - Scan/Input Product         │             │
             │  │ - Input Quantity             │             │
             │  │ - Update Stock Level         │             │
             │  └──────────────────────────────┘             │
             │              │                                 │
             │              │ «extend»                        │
             │              ▼                                 │
             │  ┌──────────────────────────────┐             │
             │  │ Upload Delivery Note         │             │
             │  └──────────────────────────────┘             │
             │                                                │
             │  ┌──────────────────────────────┐             │
             ├──│ Record Stock Out             │             │
             │  │ «include»                    │             │
             │  │ - Select Product             │             │
             │  │ - Input Quantity Used        │             │
             │  │ - Update Stock Level         │             │
             │  │ - Link to Work Order         │             │
             │  └──────────────────────────────┘             │
             │                                                │
             │  ┌──────────────────────────────┐             │
             ├──│ Monitor Stock Level          │◄────────────┤
             │  │ - View Current Stock         │             │
             │  │ - Low Stock Alert            │             │
             │  │ - Stock Movement History     │             │
             │  └──────────────────────────────┘             │
             │              │                                 │
             │              │ «include»                       │
             │              ▼                                 │
             │  ┌──────────────────────────────┐             │
             │  │ Generate Stock Report        │◄────────────┤
             │  └──────────────────────────────┘             │
             │                                                │
             │  ┌──────────────────────────────┐             │
             ├──│ Perform Stock Opname         │◄────────────┤
             │  │ «include»                    │             │
             │  │ - Create Opname Session      │             │
             │  │ - Input Physical Count       │             │
             │  │ - Generate Variance Report   │             │
             │  └──────────────────────────────┘             │
             │              │                                 │
             │              │ «extend»                        │
             │              ▼                                 │
             │  ┌──────────────────────────────┐             │
             │  │ Adjust Stock (if variance)   │             │
             │  │ «require approval»           │─────────────┤
             │  └──────────────────────────────┘             │
             │                                                │
             │  ┌──────────────────────────────┐             │
             ├──│ Manage Supplier Data         │◄────────────┤
             │  │ - Add Supplier               │             │
             │  │ - Update Supplier Info       │             │
             │  │ - Track Supplier Performance │             │
             │  └──────────────────────────────┘             │
             │                                                │
             │  ┌──────────────────────────────┐             │
             ├──│ Create Purchase Requisition  │             │
             │  │ «include»                    │             │
             │  │ - Select Material            │             │
             │  │ - Input Quantity Needed      │             │
             │  │ - Select Supplier            │             │
             │  └──────────────────────────────┘             │
             │              │                                 │
             │              │ «trigger»                       │
             │              ▼                                 │
             │  ┌──────────────────────────────┐             │
             │  │ Approve Purchase Requisition │             │
             │  │ «approval workflow»          │◄────────────┤
             │  └──────────────────────────────┘             │
             │              │                                 │
             │              │ «after approval»                │
             │              ▼                                 │
             │  ┌──────────────────────────────┐             │
             ├──│ Create Purchase Order        │◄────────────┤
             │  │ «include»                    │             │
             │  │ - Generate PO Number         │             │
             │  │ - Send to Supplier           │─────────────┼──►┌──────────┐
             │  └──────────────────────────────┘             │   │ Supplier │
             │                                                │   └──────────┘
             │  ┌──────────────────────────────┐             │
             └──│ Analyze Inventory Turnover   │◄────────────┤
                │ - Fast Moving Items          │             │
                │ - Slow Moving Items          │             │
                │ - ABC Analysis               │             │
                └──────────────────────────────┘             │
                                                              │
                                                    ┌─────────┴────────┐
                                                    │     System       │
                                                    │    (Timer)       │
                                                    └─────────┬────────┘
                                                              │
                                                    ┌─────────┴────────┐
                                                    │ Send Low Stock   │
                                                    │ Alert            │
                                                    │ «automated»      │
                                                    └──────────────────┘
```

**Deskripsi Use Case Inventory:**

**UC-INV-001: Record Stock In**
- **Aktor Utama:** Inventory Staff
- **Tujuan:** Mencatat material/produk yang masuk ke warehouse
- **Precondition:** Staff sudah login, material sudah diterima secara fisik
- **Postcondition:** Stock level ter-update di sistem
- **Main Flow:**
  1. Staff pilih "Stock In"
  2. Staff select/scan product/material
  3. Staff input quantity received
  4. Staff select supplier
  5. Staff input reference (PO number, delivery note)
  6. System validate data
  7. System update stock level (add quantity)
  8. System generate goods receipt note
  9. System create stock movement history
- **Extend:** Upload Delivery Note Photo

**UC-INV-002: Perform Stock Opname**
- **Aktor Utama:** Inventory Staff
- **Aktor Pendukung:** Manager (approval)
- **Tujuan:** Melakukan stock count fisik dan reconcile dengan system
- **Precondition:** Stock opname schedule sudah dibuat
- **Postcondition:** Stock data di sistem sesuai dengan physical count
- **Main Flow:**
  1. Staff create stock opname session dengan cut-off date
  2. System generate stock count sheet (list items dengan system stock)
  3. Staff print count sheet
  4. Staff lakukan physical count
  5. Staff input physical count result ke sistem
  6. System calculate variance (physical - system)
  7. System generate variance report
  8. Jika ada variance, staff create adjustment request
  9. Manager review dan approve adjustment
  10. System update stock level sesuai physical count
  11. System create audit trail
- **Extend:** Adjust Stock (jika ada variance)

**UC-INV-003: Create Purchase Requisition**
- **Aktor Utama:** Inventory Staff
- **Aktor Pendukung:** Manager (approval)
- **Tujuan:** Membuat permintaan pembelian material
- **Precondition:** Stock level mencapai reorder point atau ada kebutuhan material
- **Postcondition:** PR created dan menunggu approval
- **Main Flow:**
  1. Staff pilih "Create PR"
  2. Staff select material yang akan di-request
  3. Staff input quantity needed
  4. Staff select preferred supplier
  5. Staff input justification (low stock/project requirement)
  6. Staff submit PR
  7. System generate PR number
  8. System send notification ke Manager untuk approval
  9. Manager review PR
  10. Manager approve/reject PR
  11. Jika approved, system create PO
  12. System send PO ke Supplier (email/WhatsApp)

---

### 2.4 Use Case Diagram - Modul Production Planning

```
┌─────────────────────────────────────────────────────────────────────┐
│              SATRIAMART SIMS - PRODUCTION MODULE                     │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────────────┐                         ┌────────────────────┐
    │Production Staff  │                         │Production Supervisor│
    └────────┬─────────┘                         └─────────┬──────────┘
             │                                              │
             │  ┌─────────────────────────────┐            │
             ├──│ View Work Order List        │◄───────────┤
             │  │ - Filter by Status          │            │
             │  │ - Sort by Priority          │            │
             │  │ - View Details              │            │
             │  └─────────────────────────────┘            │
             │                                              │
             │  ┌─────────────────────────────┐            │
             │  │ Create Work Order           │            │
             │  │ «include»                   │◄───────────┤
             │  │ - Link to Customer Order    │            │
             │  │ - Select Product            │            │
             │  │ - Check Material Availability│           │
             │  │ - Set Due Date              │            │
             │  └─────────────────────────────┘            │
             │              │                               │
             │              │ «include»                     │
             │              ▼                               │
             │  ┌─────────────────────────────┐            │
             │  │ Generate Bill of Materials  │            │
             │  │ «auto-calculate»            │            │
             │  └─────────────────────────────┘            │
             │                                              │
             │  ┌─────────────────────────────┐            │
             │  │ Assign Work Order           │            │
             │  │ «workflow»                  │◄───────────┤
             │  │ - Select Staff              │            │
             │  │ - Assign Machine/Resource   │            │
             │  │ - Set Schedule              │            │
             │  └─────────────────────────────┘            │
             │                                              │
             │  ┌─────────────────────────────┐            │
             ├──│ Start Production            │            │
             │  │ «include»                   │            │
             │  │ - Update Status             │            │
             │  │ - Reserve Material          │            │
             │  │ - Start Timer               │            │
             │  └─────────────────────────────┘            │
             │                                              │
             │  ┌─────────────────────────────┐            │
             ├──│ Update Production Progress  │            │
             │  │ - Input % Complete          │            │
             │  │ - Upload Progress Photo     │            │
             │  │ - Add Notes                 │            │
             │  └─────────────────────────────┘            │
             │                                              │
             │  ┌─────────────────────────────┐            │
             ├──│ Record Material Consumption │            │
             │  │ «include»                   │            │
             │  │ - Select Material Used      │            │
             │  │ - Input Actual Quantity     │            │
             │  │ - Update Inventory          │            │
             │  └─────────────────────────────┘            │
             │              │                               │
             │              │ «trigger»                     │
             │              ▼                               │
             │  ┌─────────────────────────────┐            │
             │  │ Update Inventory Stock      │            │
             │  │ «auto-deduct»               │            │
             │  └─────────────────────────────┘            │
             │                                              │
             │  ┌─────────────────────────────┐            │
             ├──│ Complete Production         │            │
             │  │ «trigger QC»                │            │
             │  └─────────────────────────────┘            │
             │              │                               │
             │              │ «require»                     │
             │              ▼                               │
             │  ┌─────────────────────────────┐            │
             │  │ Perform Quality Control     │            │
             │  │ «workflow»                  │◄───────────┤
             │  │ - Checklist Inspection      │            │
             │  │ - Pass/Fail Decision        │            │
             │  │ - Defect Documentation      │            │
             │  └─────────────────────────────┘            │
             │              │                               │
             │              ├── «if PASS»                   │
             │              │                               │
             │              ▼                               │
             │  ┌─────────────────────────────┐            │
             │  │ Move to Finished Goods      │            │
             │  │ «update inventory»          │            │
             │  └─────────────────────────────┘            │
             │              │                               │
             │              ├── «if FAIL»                   │
             │              │                               │
             │              ▼                               │
             │  ┌─────────────────────────────┐            │
             │  │ Create Rework Task          │◄───────────┤
             │  │ - Document Defect           │            │
             │  │ - Reassign to Staff         │            │
             │  └─────────────────────────────┘            │
             │                                              │
             │  ┌─────────────────────────────┐            │
             │  │ Manage Production Schedule  │            │
             │  │ «drag-drop calendar»        │◄───────────┤
             │  │ - View Calendar             │            │
             │  │ - Reschedule WO             │            │
             │  │ - Check Conflicts           │            │
             │  └─────────────────────────────┘            │
             │                                              │
             │  ┌─────────────────────────────┐            │
             │  │ Monitor Production Performance│◄─────────┤
             │  │ - Production Output         │            │
             │  │ - OEE Calculation           │            │
             │  │ - Bottleneck Analysis       │            │
             │  └─────────────────────────────┘            │
             │                                              │
                                                   ┌────────┴────────┐
                                                   │    Manager      │
                                                   └────────┬────────┘
                                                            │
                                             ┌──────────────┴────────┐
                                             │ Analyze Production KPI│
                                             │ - On-Time Delivery    │
                                             │ - Efficiency Rate     │
                                             │ - Quality Metrics     │
                                             └───────────────────────┘
```

**Deskripsi Use Case Production:**

**UC-PROD-001: Create Work Order**
- **Aktor Utama:** Production Supervisor
- **Tujuan:** Membuat work order dari customer order
- **Precondition:** Customer order sudah dibuat, material tersedia
- **Postcondition:** Work order created dengan status "Scheduled"
- **Main Flow:**
  1. Supervisor pilih customer order yang belum ada WO-nya
  2. Supervisor pilih "Create Work Order"
  3. System retrieve order details (product, quantity, specification)
  4. System check material availability
  5. System generate Bill of Materials (BOM)
  6. Supervisor review BOM dan material stock
  7. Supervisor set production due date
  8. Supervisor set priority (normal/urgent)
  9. Supervisor submit WO
  10. System generate WO number
  11. System reserve material untuk WO ini
  12. System update order status ke "In Production Planning"
- **Include:** Generate BOM, Check Material Availability
- **Alternative Flow:**
  - 4a. Jika material tidak cukup, system tampilkan warning dan suggest PR

**UC-PROD-002: Update Production Progress**
- **Aktor Utama:** Production Staff
- **Tujuan:** Update progress pengerjaan work order
- **Precondition:** WO sudah assigned dan production sudah dimulai
- **Postcondition:** Progress ter-update, stakeholder menerima notifikasi
- **Main Flow:**
  1. Staff select WO yang sedang dikerjakan
  2. Staff pilih "Update Progress"
  3. Staff input percentage complete (0-100%)
  4. Staff upload work-in-progress photo (optional)
  5. Staff record material consumption (actual usage)
  6. Staff add notes (issues, delays, dll)
  7. Staff submit update
  8. System update WO progress
  9. System deduct inventory berdasarkan material consumption
  10. System send notification ke Supervisor
  11. Jika progress = 100%, trigger QC workflow
- **Include:** Record Material Consumption

**UC-PROD-003: Perform Quality Control**
- **Aktor Utama:** Production Supervisor
- **Tujuan:** Melakukan quality check terhadap finished product
- **Precondition:** Production completed (100% progress)
- **Postcondition:** Product approved atau rework required
- **Main Flow:**
  1. Supervisor receive notification QC required
  2. Supervisor select WO untuk QC
  3. System tampilkan QC checklist sesuai product type
  4. Supervisor perform inspection berdasarkan checklist
  5. Supervisor input result (pass/fail) untuk setiap item
  6. Supervisor upload photo untuk defect (jika ada)
  7. Supervisor make decision: PASS atau FAIL
  8. Jika PASS:
     - System move product ke finished goods inventory
     - System update order status ke "Ready for Delivery"
     - System send notification ke Sales team
  9. Jika FAIL:
     - Supervisor input defect type dan root cause
     - System create rework task
     - System reassign ke production staff
     - System send notification ke staff
- **Alternative Flow:** Create Rework Task (jika QC fail)

---

### 2.5 Use Case Diagram - Modul Analytics & Administration

```
┌─────────────────────────────────────────────────────────────────────┐
│         SATRIAMART SIMS - ANALYTICS & ADMINISTRATION MODULE          │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────┐                                    ┌─────────────┐
    │  Owner   │                                    │   Manager   │
    └────┬─────┘                                    └──────┬──────┘
         │                                                 │
         │  ┌────────────────────────────────┐            │
         ├──│ View Executive Dashboard       │◄───────────┤
         │  │ - Sales Overview               │            │
         │  │ - Inventory Summary            │            │
         │  │ - Production Metrics           │            │
         │  │ - Customer Growth              │            │
         │  └────────────────────────────────┘            │
         │              │                                  │
         │              │ «include»                        │
         │              ▼                                  │
         │  ┌────────────────────────────────┐            │
         │  │ Refresh Real-Time Data         │            │
         │  │ «auto every 5 min»             │            │
         │  └────────────────────────────────┘            │
         │                                                 │
         │  ┌────────────────────────────────┐            │
         ├──│ Analyze Sales Trends           │◄───────────┤
         │  │ - Period Comparison            │            │
         │  │ - Product Performance          │            │
         │  │ - Seasonal Pattern             │            │
         │  └────────────────────────────────┘            │
         │                                                 │
         │  ┌────────────────────────────────┐            │
         ├──│ Generate Business Reports      │◄───────────┤
         │  │ «include»                      │            │
         │  │ - Select Report Type           │            │
         │  │ - Set Date Range               │            │
         │  │ - Export (PDF/Excel)           │            │
         │  └────────────────────────────────┘            │
         │              │                                  │
         │              │ «extend»                         │
         │              ▼                                  │
         │  ┌────────────────────────────────┐            │
         │  │ Schedule Automated Reports     │◄───────────┤
         │  │ - Set Frequency                │            │
         │  │ - Set Recipients               │            │
         │  │ - Email Delivery               │            │
         │  └────────────────────────────────┘            │
         │                                                 │
         │  ┌────────────────────────────────┐            │
         └──│ View Profitability Analysis    │◄───────────┤
            │ - Profit by Product            │            │
            │ - Profit by Customer           │            │
            │ - Cost Breakdown               │            │
            └────────────────────────────────┘            │
                                                           │
    ┌───────────┐                                          │
    │   Admin   │                                          │
    └─────┬─────┘                                          │
          │                                                │
          │  ┌────────────────────────────────┐           │
          ├──│ Manage User Accounts           │           │
          │  │ - Create User                  │           │
          │  │ - Edit User                    │           │
          │  │ - Deactivate User              │           │
          │  │ - Reset Password               │           │
          │  └────────────────────────────────┘           │
          │              │                                 │
          │              │ «include»                       │
          │              ▼                                 │
          │  ┌────────────────────────────────┐           │
          │  │ Assign User Roles              │           │
          │  │ - Select Role                  │           │
          │  │ - Set Permissions              │           │
          │  └────────────────────────────────┘           │
          │                                                │
          │  ┌────────────────────────────────┐           │
          ├──│ Configure System Settings      │           │
          │  │ - Company Profile              │           │
          │  │ - Email Templates              │           │
          │  │ - Notification Preferences     │           │
          │  │ - Tax Settings                 │           │
          │  └────────────────────────────────┘           │
          │                                                │
          │  ┌────────────────────────────────┐           │
          ├──│ View Audit Trail               │◄──────────┤
          │  │ - User Activity Log            │           │
          │  │ - Data Change History          │           │
          │  │ - Login History                │           │
          │  └────────────────────────────────┘           │
          │                                                │
          │  ┌────────────────────────────────┐           │
          ├──│ Perform Database Backup        │           │
          │  │ «manual/scheduled»             │           │
          │  └────────────────────────────────┘           │
          │              │                                 │
          │              │ «include»                       │
          │              ▼                                 │
          │  ┌────────────────────────────────┐           │
          │  │ Verify Backup Integrity        │           │
          │  └────────────────────────────────┘           │
          │                                                │
                                                  ┌────────┴────────┐
                                                  │     System      │
                                                  │    (Timer)      │
                                                  └────────┬────────┘
                                                           │
                                             ┌─────────────┴──────────┐
                                             │ Send Scheduled Reports │
                                             │ «daily/weekly/monthly» │
                                             └────────────────────────┘
                                                           │
                                             ┌─────────────┴──────────┐
                                             │ Perform Auto Backup    │
                                             │ «daily at 02:00 AM»    │
                                             └────────────────────────┘
```

---

## Ringkasan Use Case

### Total Use Case: 35+ Use Cases

**Modul CRM (8 Use Cases):**
- UC-CRM-001: Register New Customer
- UC-CRM-002: Update Customer Information
- UC-CRM-003: Create Customer Order
- UC-CRM-004: Track Order Status
- UC-CRM-005: Log Customer Communication
- UC-CRM-006: Handle Customer Complaint
- UC-CRM-007: Analyze Customer Behavior
- UC-CRM-008: Generate CRM Reports

**Modul Inventory (10 Use Cases):**
- UC-INV-001: Manage Product Master Data
- UC-INV-002: Record Stock In
- UC-INV-003: Record Stock Out
- UC-INV-004: Monitor Stock Level
- UC-INV-005: Perform Stock Opname
- UC-INV-006: Manage Supplier Data
- UC-INV-007: Create Purchase Requisition
- UC-INV-008: Approve Purchase Requisition
- UC-INV-009: Create Purchase Order
- UC-INV-010: Analyze Inventory Turnover

**Modul Production (10 Use Cases):**
- UC-PROD-001: Create Work Order
- UC-PROD-002: Assign Work Order
- UC-PROD-003: View Work Order List
- UC-PROD-004: Start Production
- UC-PROD-005: Update Production Progress
- UC-PROD-006: Record Material Consumption
- UC-PROD-007: Perform Quality Control
- UC-PROD-008: Move to Finished Goods
- UC-PROD-009: Manage Production Schedule
- UC-PROD-010: Monitor Production Performance

**Modul Analytics & Administration (7 Use Cases):**
- UC-ANAL-001: View Executive Dashboard
- UC-ANAL-002: Analyze Sales Trends
- UC-ANAL-003: Generate Business Reports
- UC-ADMIN-001: Manage User Accounts
- UC-ADMIN-002: Configure System Settings
- UC-ADMIN-003: View Audit Trail
- UC-ADMIN-004: Perform Database Backup

---

*Dokumen ini merupakan Part 2 dari Analisis dan Desain Sistem. Untuk Part 3 (Activity Diagram dan ERD) dan Part 4 (User Interface Design), silakan lihat dokumen terpisah.*

