# ANALISIS DAN DESAIN SISTEM - PART 4
## SATRIAMART SIMS - Entity Relationship Diagram (ERD)
### Database Design & Data Model

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi II**  
**Pertemuan 4 - Entity Relationship Diagram (ERD)**

---

## 4. ENTITY RELATIONSHIP DIAGRAM (ERD)

### 4.1 Konsep Database Design

Entity Relationship Diagram (ERD) adalah model data yang menggambarkan hubungan antar entitas dalam database sistem SATRIAMART SIMS. ERD ini dirancang dengan prinsip normalisasi (3NF - Third Normal Form) untuk memastikan integritas data dan mengurangi redundansi.

**Prinsip Desain Database:**
1. **Normalisasi:** Database dirancang hingga 3NF untuk menghindari anomali data
2. **Referential Integrity:** Penggunaan foreign key untuk menjaga konsistensi data
3. **Indexing Strategy:** Index pada kolom yang sering digunakan untuk pencarian
4. **Audit Trail:** Setiap tabel memiliki created_at, updated_at, created_by, updated_by
5. **Soft Delete:** Menggunakan deleted_at untuk soft delete (tidak menghapus data permanen)

---

### 4.2 Daftar Entitas (Tables)

Sistem SATRIAMART SIMS memiliki **25 entitas utama** yang terbagi dalam 5 modul:

#### Modul CRM (Customer Relationship Management)
1. **customers** - Master data pelanggan
2. **customer_categories** - Kategori pelanggan (individu, perusahaan, reseller)
3. **orders** - Order dari customer
4. **order_items** - Detail item dalam order
5. **order_status_history** - Riwayat perubahan status order
6. **customer_communications** - Log komunikasi dengan customer
7. **complaints** - Komplain dari customer
8. **complaint_resolutions** - Resolusi komplain

#### Modul Inventory Management
9. **products** - Master data produk
10. **product_categories** - Kategori produk
11. **materials** - Master data material/bahan baku
12. **stock_movements** - Riwayat pergerakan stok (in/out)
13. **stock_opnames** - Session stock opname
14. **stock_opname_details** - Detail item yang di-opname
15. **suppliers** - Master data supplier
16. **purchase_requisitions** - Permintaan pembelian
17. **purchase_requisition_items** - Detail item PR
18. **purchase_orders** - Purchase order ke supplier
19. **purchase_order_items** - Detail item PO

#### Modul Production Planning
20. **work_orders** - Work order produksi
21. **work_order_materials** - Material yang dibutuhkan per WO (BOM)
22. **production_progress** - Log progress produksi
23. **quality_controls** - Hasil quality control
24. **qc_checklists** - Checklist template QC per product type
25. **resources** - Resource produksi (mesin, tools)

#### Modul Administration
26. **users** - User sistem
27. **roles** - Role user (admin, manager, staff, dll)
28. **permissions** - Permission per role
29. **role_permissions** - Mapping role dan permission
30. **audit_logs** - Log aktivitas user

---

### 4.3 ERD - Modul CRM (Customer Relationship Management)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    ERD - CUSTOMER RELATIONSHIP MANAGEMENT                   │
└────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────┐
│  customer_categories    │
├─────────────────────────┤
│ PK  id                  │
│     category_name       │◄───────────┐
│     description         │            │
│     created_at          │            │
│     updated_at          │            │ 1
└─────────────────────────┘            │
                                       │ belongs to
                                       │
┌─────────────────────────┐            │
│      customers          │            │
├─────────────────────────┤            │
│ PK  id                  │            │
│     customer_code       │            │ (UNIQUE, AUTO: CUST-0001)
│     name                │            │
│     email               │            │ (UNIQUE)
│     phone               │            │
│     address             │            │
│     city                │            │
│     postal_code         │            │
│ FK  category_id         │────────────┘
│     status              │ (ENUM: active, inactive, potential)
│     notes               │
│     created_at          │
│     updated_at          │
│     created_by          │
│     updated_by          │
│     deleted_at          │ (soft delete)
└────────┬────────────────┘
         │
         │ 1
         │ has many
         │ *
         ▼
┌─────────────────────────┐
│   customer_communications│
├─────────────────────────┤
│ PK  id                  │
│ FK  customer_id         │
│     communication_type  │ (ENUM: email, phone, whatsapp, meeting)
│     subject             │
│     notes               │
│     communication_date  │
│     follow_up_date      │
│     status              │ (ENUM: pending, completed)
│ FK  handled_by          │ (FK to users.id)
│     created_at          │
│     updated_at          │
└─────────────────────────┘


         ┌─────────────────────────┐
         │      customers          │
         │ (from above)            │
         └────────┬────────────────┘
                  │
                  │ 1
                  │ has many
                  │ *
                  ▼
         ┌─────────────────────────┐
         │        orders           │
         ├─────────────────────────┤
         │ PK  id                  │
         │     order_number        │ (UNIQUE, AUTO: ORD-20240122-0001)
         │ FK  customer_id         │
         │     order_date          │
         │     delivery_date       │ (estimated)
         │     total_amount        │ (DECIMAL 15,2)
         │     discount_amount     │ (DECIMAL 15,2)
         │     final_amount        │ (DECIMAL 15,2)
         │     status              │ (ENUM: pending, confirmed, in_production,
         │                         │        quality_check, ready, shipped,
         │                         │        completed, cancelled)
         │     notes               │
         │     special_request     │
         │ FK  created_by          │ (FK to users.id - sales staff)
         │     created_at          │
         │     updated_at          │
         │     deleted_at          │
         └────────┬────────────────┘
                  │
                  │ 1
                  │ has many
                  │ *
    ┌─────────────┴──────────────┬────────────────────────┐
    │                            │                        │
    ▼                            ▼                        ▼
┌─────────────────────────┐ ┌─────────────────────────┐ ┌─────────────────────────┐
│     order_items         │ │ order_status_history    │ │      complaints         │
├─────────────────────────┤ ├─────────────────────────┤ ├─────────────────────────┤
│ PK  id                  │ │ PK  id                  │ │ PK  id                  │
│ FK  order_id            │ │ FK  order_id            │ │ FK  order_id            │
│ FK  product_id          │ │     status              │ │ FK  customer_id         │
│     quantity            │ │     notes               │ │     complaint_category  │
│     unit_price          │ │ FK  changed_by          │ │     description         │
│     subtotal            │ │     changed_at          │ │     priority            │
│     specifications      │ │     created_at          │ │     status              │
│     notes               │ └─────────────────────────┘ │ FK  assigned_to         │
│     created_at          │                            │     reported_date       │
│     updated_at          │                            │     resolved_date       │
└─────────────────────────┘                            │     created_at          │
         │                                             │     updated_at          │
         │                                             └────────┬────────────────┘
         │ *                                                    │
         │ belongs to                                           │ 1
         │ 1                                                    │ has many
         ▼                                                      │ *
┌─────────────────────────┐                                     ▼
│       products          │                          ┌─────────────────────────┐
│ (from Inventory module) │                          │ complaint_resolutions   │
└─────────────────────────┘                          ├─────────────────────────┤
                                                     │ PK  id                  │
                                                     │ FK  complaint_id        │
                                                     │     resolution_action   │
                                                     │     notes               │
                                                     │ FK  resolved_by         │
                                                     │     resolution_date     │
                                                     │     customer_rating     │
                                                     │     created_at          │
                                                     │     updated_at          │
                                                     └─────────────────────────┘
```

**Relasi Modul CRM:**
- **customers ↔ customer_categories:** Many-to-One (FK: category_id)
- **customers ↔ customer_communications:** One-to-Many
- **customers ↔ orders:** One-to-Many
- **orders ↔ order_items:** One-to-Many
- **orders ↔ order_status_history:** One-to-Many
- **orders ↔ complaints:** One-to-Many
- **customers ↔ complaints:** One-to-Many
- **complaints ↔ complaint_resolutions:** One-to-Many
- **order_items ↔ products:** Many-to-One

---

### 4.4 ERD - Modul Inventory Management

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       ERD - INVENTORY MANAGEMENT                            │
└────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────┐
│  product_categories     │
├─────────────────────────┤
│ PK  id                  │
│     category_code       │ (UNIQUE: CAT-001)
│     category_name       │ (Nomor Rumah, Signage, Papan Nama, dll)
│     description         │
│     created_at          │
│     updated_at          │
└────────┬────────────────┘
         │
         │ 1
         │ has many
         │ *
         ▼
┌─────────────────────────┐
│       products          │
├─────────────────────────┤
│ PK  id                  │
│     product_code        │ (UNIQUE, AUTO: PRD-001)
│     product_name        │
│ FK  category_id         │
│     description         │
│     dimensions          │ (JSON: {width, height, thickness})
│     weight              │ (gram)
│     unit_of_measure     │ (pcs, set)
│     cost_price          │ (DECIMAL 15,2 - harga modal)
│     selling_price       │ (DECIMAL 15,2 - harga jual)
│     stock_quantity      │ (INT - current stock)
│     reorder_point       │ (INT - minimum stock level)
│     reorder_quantity    │ (INT - quantity to reorder)
│     status              │ (ENUM: active, inactive, discontinued)
│     image_url           │
│     created_at          │
│     updated_at          │
│     created_by          │
│     updated_by          │
│     deleted_at          │
└────────┬────────────────┘
         │
         │ 1
         │ has many
         │ *
         ▼
┌─────────────────────────┐
│    stock_movements      │
├─────────────────────────┤
│ PK  id                  │
│ FK  product_id          │
│ FK  material_id         │ (NULL jika movement untuk product)
│     movement_type       │ (ENUM: in, out, adjustment)
│     transaction_type    │ (ENUM: purchase, sales, production,
│                         │        opname, return, waste)
│     quantity            │
│     unit_price          │
│     reference_type      │ (order, work_order, po, opname, etc)
│     reference_id        │
│     notes               │
│     movement_date       │
│ FK  created_by          │
│     created_at          │
└─────────────────────────┘


┌─────────────────────────┐
│      materials          │
├─────────────────────────┤
│ PK  id                  │
│     material_code       │ (UNIQUE: MAT-001)
│     material_name       │ (Acrylic Sheet, Adhesive, dll)
│     description         │
│     unit_of_measure     │ (sheet, liter, kg, pcs)
│     cost_price          │ (DECIMAL 15,2)
│     stock_quantity      │
│     reorder_point       │
│     reorder_quantity    │
│     status              │ (ENUM: active, inactive)
│     created_at          │
│     updated_at          │
│     deleted_at          │
└────────┬────────────────┘
         │
         │ 1
         │ referenced in
         │ *
         └───────────────────────┐
                                 │
                                 ▼
                        ┌─────────────────────────┐
                        │   stock_movements       │
                        │   (reference materials) │
                        └─────────────────────────┘


┌─────────────────────────┐
│       suppliers         │
├─────────────────────────┤
│ PK  id                  │
│     supplier_code       │ (UNIQUE: SUP-001)
│     supplier_name       │
│     contact_person      │
│     email               │
│     phone               │
│     address             │
│     city                │
│     lead_time_days      │ (INT - waktu pengiriman)
│     payment_terms       │ (30 days, 60 days, COD)
│     rating              │ (DECIMAL 3,2 - 1.00 to 5.00)
│     status              │ (ENUM: active, inactive, blacklist)
│     notes               │
│     created_at          │
│     updated_at          │
│     deleted_at          │
└────────┬────────────────┘
         │
         │ 1
         │ has many
         │ *
         ▼
┌─────────────────────────┐
│  purchase_requisitions  │
├─────────────────────────┤
│ PK  id                  │
│     pr_number           │ (UNIQUE, AUTO: PR-20240122-001)
│ FK  requested_by        │ (FK to users.id)
│     request_date        │
│     required_date       │ (needed by date)
│     justification       │ (reason)
│     status              │ (ENUM: pending, approved, rejected,
│                         │        converted_to_po)
│ FK  approved_by         │ (FK to users.id)
│     approval_date       │
│     approval_notes      │
│     created_at          │
│     updated_at          │
└────────┬────────────────┘
         │
         │ 1
         │ has many
         │ *
         ▼
┌─────────────────────────┐
│ purchase_requisition_items│
├─────────────────────────┤
│ PK  id                  │
│ FK  pr_id               │
│ FK  material_id         │
│     quantity_requested  │
│ FK  preferred_supplier  │ (FK to suppliers.id)
│     estimated_price     │
│     notes               │
│     created_at          │
│     updated_at          │
└─────────────────────────┘


┌─────────────────────────┐
│   purchase_requisitions │
│   (from above)          │
└────────┬────────────────┘
         │
         │ 1
         │ generates
         │ 1
         ▼
┌─────────────────────────┐
│    purchase_orders      │
├─────────────────────────┤
│ PK  id                  │
│     po_number           │ (UNIQUE, AUTO: PO-20240122-001)
│ FK  pr_id               │ (reference to PR)
│ FK  supplier_id         │
│     po_date             │
│     expected_delivery   │
│     total_amount        │ (DECIMAL 15,2)
│     status              │ (ENUM: pending, sent, confirmed,
│                         │        partial_received, received,
│                         │        cancelled)
│     terms_conditions    │
│     notes               │
│ FK  created_by          │
│     created_at          │
│     updated_at          │
└────────┬────────────────┘
         │
         │ 1
         │ has many
         │ *
         ▼
┌─────────────────────────┐
│  purchase_order_items   │
├─────────────────────────┤
│ PK  id                  │
│ FK  po_id               │
│ FK  material_id         │
│     quantity_ordered    │
│     quantity_received   │
│     unit_price          │
│     subtotal            │
│     notes               │
│     created_at          │
│     updated_at          │
└─────────────────────────┘


┌─────────────────────────┐
│    stock_opnames        │
├─────────────────────────┤
│ PK  id                  │
│     opname_number       │ (UNIQUE: OPN-20240122-001)
│     opname_date         │
│     cutoff_datetime     │
│     category            │ (all, specific_category)
│     status              │ (ENUM: in_progress, completed,
│                         │        adjustment_pending, adjusted)
│ FK  conducted_by        │ (FK to users.id)
│ FK  approved_by         │ (FK to users.id - for adjustment)
│     approval_date       │
│     notes               │
│     created_at          │
│     updated_at          │
└────────┬────────────────┘
         │
         │ 1
         │ has many
         │ *
         ▼
┌─────────────────────────┐
│  stock_opname_details   │
├─────────────────────────┤
│ PK  id                  │
│ FK  opname_id           │
│ FK  product_id          │ (NULL jika material)
│ FK  material_id         │ (NULL jika product)
│     system_stock        │ (stock di sistem saat cutoff)
│     physical_stock      │ (hasil physical count)
│     variance            │ (physical - system)
│     variance_reason     │
│     notes               │
│     counted_at          │
│     created_at          │
│     updated_at          │
└─────────────────────────┘
```

**Relasi Modul Inventory:**
- **products ↔ product_categories:** Many-to-One
- **products ↔ stock_movements:** One-to-Many
- **materials ↔ stock_movements:** One-to-Many
- **suppliers ↔ purchase_requisitions:** One-to-Many (indirect via items)
- **purchase_requisitions ↔ purchase_requisition_items:** One-to-Many
- **purchase_requisitions ↔ purchase_orders:** One-to-One
- **purchase_orders ↔ purchase_order_items:** One-to-Many
- **purchase_orders ↔ suppliers:** Many-to-One
- **stock_opnames ↔ stock_opname_details:** One-to-Many

---

### 4.5 ERD - Modul Production Planning

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       ERD - PRODUCTION PLANNING                             │
└────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────┐
│        orders           │
│  (from CRM module)      │
└────────┬────────────────┘
         │
         │ 1
         │ generates
         │ 1
         ▼
┌─────────────────────────┐
│     work_orders         │
├─────────────────────────┤
│ PK  id                  │
│     wo_number           │ (UNIQUE, AUTO: WO-20240122-001)
│ FK  order_id            │ (reference to customer order)
│ FK  product_id          │
│     quantity            │
│     specifications      │ (special request dari customer)
│     start_date          │ (scheduled start)
│     due_date            │
│     actual_start_date   │
│     actual_end_date     │
│     priority            │ (ENUM: normal, urgent, critical)
│     status              │ (ENUM: scheduled, assigned, in_progress,
│                         │        completed, quality_check, passed,
│                         │        failed_rework, cancelled)
│ FK  assigned_to         │ (FK to users.id - production staff)
│ FK  supervised_by       │ (FK to users.id - supervisor)
│     progress_percentage │ (0-100)
│     notes               │
│     created_at          │
│     updated_at          │
│     created_by          │
└────────┬────────────────┘
         │
         │ 1
    ┌────┴──────────────┬──────────────────┐
    │                   │                  │
    │ has many          │ has many         │ has many
    │ *                 │ *                │ *
    ▼                   ▼                  ▼
┌─────────────────────────┐ ┌─────────────────────────┐ ┌─────────────────────────┐
│ work_order_materials    │ │  production_progress    │ │   quality_controls      │
├─────────────────────────┤ ├─────────────────────────┤ ├─────────────────────────┤
│ PK  id                  │ │ PK  id                  │ │ PK  id                  │
│ FK  wo_id               │ │ FK  wo_id               │ │ FK  wo_id               │
│ FK  material_id         │ │     progress_date       │ │ FK  qc_checklist_id     │
│     quantity_required   │ │     progress_percentage │ │     qc_date             │
│     quantity_used       │ │     description         │ │ FK  inspected_by        │
│     unit_cost           │ │     issues              │ │     overall_result      │
│     total_cost          │ │     image_url           │ │     notes               │
│     status              │ │ FK  updated_by          │ │     defect_type         │
│     notes               │ │     created_at          │ │     defect_description  │
│     created_at          │ │     updated_at          │ │     root_cause          │
│     updated_at          │ └─────────────────────────┘ │     image_url           │
└─────────────────────────┘                            │     status              │
         │                                             │     created_at          │
         │ *                                           │     updated_at          │
         │ belongs to                                  └────────┬────────────────┘
         │ 1                                                    │
         ▼                                                      │ *
┌─────────────────────────┐                                     │ uses template
│      materials          │                                     │ 1
│ (from Inventory module) │                                     ▼
└─────────────────────────┘                          ┌─────────────────────────┐
                                                     │    qc_checklists        │
                                                     ├─────────────────────────┤
                                                     │ PK  id                  │
                                                     │     checklist_name      │
                                                     │ FK  product_category_id │
                                                     │     checklist_items     │
                                                     │     (JSON array)        │
                                                     │     is_active           │
                                                     │     created_at          │
                                                     │     updated_at          │
                                                     └─────────────────────────┘


┌─────────────────────────┐
│       resources         │
├─────────────────────────┤
│ PK  id                  │
│     resource_code       │ (UNIQUE: RES-001)
│     resource_name       │ (Mesin Cutting, Mesin Polish, dll)
│     resource_type       │ (ENUM: machine, tool, workspace)
│     status              │ (ENUM: available, in_use, maintenance,
│                         │        broken, retired)
│     capacity_per_day    │
│     maintenance_schedule│
│     last_maintenance    │
│     next_maintenance    │
│     notes               │
│     created_at          │
│     updated_at          │
└─────────────────────────┘
         │
         │ *
         │ can be assigned to
         │ *
         └───────────────────────┐
                                 │
                                 ▼
                        ┌─────────────────────────┐
                        │  work_order_resources   │
                        │  (many-to-many)         │
                        ├─────────────────────────┤
                        │ PK  id                  │
                        │ FK  wo_id               │
                        │ FK  resource_id         │
                        │     allocated_hours     │
                        │     actual_hours        │
                        │     start_time          │
                        │     end_time            │
                        │     created_at          │
                        └─────────────────────────┘
```

**Relasi Modul Production:**
- **orders ↔ work_orders:** One-to-One (satu order → satu WO)
- **work_orders ↔ products:** Many-to-One
- **work_orders ↔ work_order_materials:** One-to-Many (BOM)
- **work_order_materials ↔ materials:** Many-to-One
- **work_orders ↔ production_progress:** One-to-Many
- **work_orders ↔ quality_controls:** One-to-Many
- **quality_controls ↔ qc_checklists:** Many-to-One
- **work_orders ↔ resources:** Many-to-Many (via work_order_resources)

---

### 4.6 ERD - Modul Administration & User Management

```
┌────────────────────────────────────────────────────────────────────────────┐
│                   ERD - ADMINISTRATION & USER MANAGEMENT                    │
└────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────┐
│         roles           │
├─────────────────────────┤
│ PK  id                  │
│     role_name           │ (Admin, Manager, Sales Staff, dll)
│     role_code           │ (UNIQUE: ADMIN, MANAGER, SALES)
│     description         │
│     is_active           │
│     created_at          │
│     updated_at          │
└────────┬────────────────┘
         │
         │ 1
         │ has many
         │ *
         ▼
┌─────────────────────────┐
│         users           │
├─────────────────────────┤
│ PK  id                  │
│     username            │ (UNIQUE)
│     email               │ (UNIQUE)
│     password            │ (hashed with bcrypt)
│     full_name           │
│     phone               │
│ FK  role_id             │
│     status              │ (ENUM: active, inactive, suspended)
│     last_login          │
│     last_login_ip       │
│     failed_login_count  │
│     locked_until        │ (account lock after 5 failed attempts)
│     avatar_url          │
│     email_verified_at   │
│     remember_token      │
│     created_at          │
│     updated_at          │
│     deleted_at          │
└─────────────────────────┘
         │
         │ 1
         │ performs
         │ *
         ▼
┌─────────────────────────┐
│      audit_logs         │
├─────────────────────────┤
│ PK  id                  │
│ FK  user_id             │
│     action              │ (create, update, delete, login, logout)
│     table_name          │ (affected table)
│     record_id           │ (affected record ID)
│     old_values          │ (JSON - before change)
│     new_values          │ (JSON - after change)
│     ip_address          │
│     user_agent          │
│     created_at          │
└─────────────────────────┘


┌─────────────────────────┐
│      permissions        │
├─────────────────────────┤
│ PK  id                  │
│     permission_name     │ (view_customers, create_order, dll)
│     permission_code     │ (UNIQUE: VIEW_CUSTOMER, CREATE_ORDER)
│     module              │ (CRM, Inventory, Production, Admin)
│     description         │
│     created_at          │
│     updated_at          │
└────────┬────────────────┘
         │
         │ *
         │ belongs to many
         │ *
         ▼
┌─────────────────────────┐
│    role_permissions     │
│    (many-to-many)       │
├─────────────────────────┤
│ PK  id                  │
│ FK  role_id             │
│ FK  permission_id       │
│     created_at          │
└─────────────────────────┘
         │
         │ *
         │ belongs to
         │ 1
         ▼
┌─────────────────────────┐
│         roles           │
│    (from above)         │
└─────────────────────────┘
```

**Relasi Modul Administration:**
- **users ↔ roles:** Many-to-One
- **users ↔ audit_logs:** One-to-Many
- **roles ↔ permissions:** Many-to-Many (via role_permissions)

---

### 4.7 ERD Lengkap - Relasi Antar Modul

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE ERD - ALL MODULES RELATIONSHIP                  │
└────────────────────────────────────────────────────────────────────────────┘

        ┌──────────────┐
        │    USERS     │◄─────────────────┐
        │   (Admin)    │                  │
        └──────┬───────┘                  │
               │                          │
               │ creates/manages          │ assigned_to
               │                          │
    ┌──────────┼────────────┬─────────────┼──────────┬──────────────┐
    │          │            │             │          │              │
    ▼          ▼            ▼             ▼          ▼              ▼
┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│CUSTOMERS│ │ ORDERS   │ │ STOCK    │ │   PR     │ │   PO     │ │   WO     │
│         │ │          │ │ OPNAMES  │ │          │ │          │ │          │
└────┬────┘ └────┬─────┘ └──────────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘
     │           │                          │            │            │
     │ places    │ references               │ generates  │            │
     │           │                          │            │            │
     └───────────┤                          └────────────┤            │
                 │                                       │            │
                 ▼                                       ▼            │
            ┌──────────┐                          ┌──────────┐       │
            │  ORDERS  │                          │    PO    │       │
            │  (detail)│                          │ (creates │       │
            └────┬─────┘                          │ STOCK IN)│       │
                 │                                └────┬─────┘       │
                 │ contains                            │             │
                 │                                     │ receives    │
                 ▼                                     │             │
            ┌──────────┐                               │             │
            │ PRODUCTS │◄──────────────────────────────┘             │
            │          │                                             │
            └────┬─────┘                                             │
                 │                                                   │
                 │ requires                                          │
                 │ (BOM)                                             │
                 │                                                   │
                 ▼                                                   │
            ┌──────────┐                                             │
            │MATERIALS │◄────────────────────────────────────────────┤
            │          │              consumes (work_order_materials)│
            └──────────┘                                             │
                                                                     │
    ┌────────────────────────────────────────────────────────────────┘
    │
    ▼
┌──────────┐        triggers         ┌──────────┐
│    WO    │───────────────────────► │    QC    │
│          │                         │          │
└────┬─────┘                         └──────────┘
     │
     │ updates
     │
     ▼
┌──────────┐
│ STOCK    │
│MOVEMENTS │
└──────────┘
```

**Cross-Module Relationships:**
1. **users → customers, orders, work_orders:** User creates/manages these entities
2. **customers → orders:** Customer places orders
3. **orders → products:** Orders contain products
4. **orders → work_orders:** Orders generate work orders
5. **work_orders → materials:** Work orders consume materials (via BOM)
6. **purchase_orders → materials:** PO receives materials (stock in)
7. **work_orders → quality_controls:** WO triggers QC
8. **All entities → stock_movements:** All transactions affect stock

---

### 4.8 Spesifikasi Tipe Data dan Constraints

#### Tipe Data Umum yang Digunakan:

**Primary Keys:**
- `BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY`

**Foreign Keys:**
- `BIGINT UNSIGNED` dengan `FOREIGN KEY CONSTRAINT`
- `ON DELETE RESTRICT` (untuk data transaksional)
- `ON DELETE CASCADE` (untuk data dependent seperti order_items)

**String Fields:**
- `VARCHAR(255)` untuk nama, email, dll
- `VARCHAR(50)` untuk kode unik (customer_code, order_number)
- `TEXT` untuk deskripsi panjang, notes
- `JSON` untuk data kompleks (checklist_items, dimensions)

**Numeric Fields:**
- `INT` untuk quantity, stock
- `DECIMAL(15,2)` untuk harga, amount (support up to 999,999,999,999.99)
- `DECIMAL(3,2)` untuk rating (1.00 - 5.00)
- `TINYINT` untuk percentage (0-100)

**Date/Time Fields:**
- `TIMESTAMP` untuk created_at, updated_at (auto)
- `DATETIME` untuk tanggal transaksi, deadline
- `DATE` untuk tanggal saja

**Enum Fields:**
- `ENUM('value1', 'value2', ...)` untuk status, type, category

**Boolean Fields:**
- `BOOLEAN` atau `TINYINT(1)` untuk flag (is_active, is_completed)

#### Indexes untuk Performance:

```sql
-- Contoh index yang perlu dibuat:

-- Customers table
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_customers_phone ON customers(phone);
CREATE INDEX idx_customers_category ON customers(category_id);
CREATE INDEX idx_customers_status ON customers(status);

-- Orders table
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_orders_number ON orders(order_number);

-- Products table
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_code ON products(product_code);
CREATE INDEX idx_products_status ON products(status);

-- Work Orders table
CREATE INDEX idx_wo_order ON work_orders(order_id);
CREATE INDEX idx_wo_status ON work_orders(status);
CREATE INDEX idx_wo_assigned ON work_orders(assigned_to);
CREATE INDEX idx_wo_due_date ON work_orders(due_date);

-- Stock Movements table
CREATE INDEX idx_stock_product ON stock_movements(product_id);
CREATE INDEX idx_stock_material ON stock_movements(material_id);
CREATE INDEX idx_stock_date ON stock_movements(movement_date);
CREATE INDEX idx_stock_type ON stock_movements(movement_type);
```

---

### 4.9 Database Constraints dan Business Rules

#### Constraints:

1. **UNIQUE Constraints:**
   - customer_code, email, phone (in customers)
   - order_number (in orders)
   - product_code (in products)
   - material_code (in materials)
   - wo_number, pr_number, po_number

2. **CHECK Constraints:**
   - selling_price >= cost_price (in products)
   - quantity > 0 (in order_items, wo_materials)
   - progress_percentage BETWEEN 0 AND 100
   - rating BETWEEN 1.00 AND 5.00

3. **NOT NULL Constraints:**
   - Semua FK fields
   - created_at, updated_at
   - Status fields
   - Nama, email, phone (in critical tables)

#### Business Rules Implemented in Database:

1. **Auto-increment dengan Format Khusus:**
   ```
   customer_code: CUST-0001, CUST-0002, ...
   order_number: ORD-20240122-0001 (dengan tanggal)
   wo_number: WO-20240122-0001
   ```

2. **Soft Delete:**
   - Menggunakan `deleted_at` timestamp
   - Record tidak dihapus permanen, hanya di-mark
   - Query harus filter `WHERE deleted_at IS NULL`

3. **Audit Trail:**
   - Semua tabel memiliki: created_at, updated_at, created_by, updated_by
   - Perubahan penting dicatat di audit_logs table

4. **Status Workflow:**
   - Order status: pending → confirmed → in_production → quality_check → ready → shipped → completed
   - WO status: scheduled → assigned → in_progress → completed → quality_check → passed
   - PO status: pending → sent → confirmed → received

5. **Stock Management:**
   - Stock deduct otomatis saat WO start production
   - Stock add otomatis saat PO received
   - Stock adjustment harus approved oleh manager

---

## Ringkasan ERD

**Total Entitas: 30 Tables**

**Modul CRM: 8 Tables**
- customers, customer_categories, orders, order_items, order_status_history, customer_communications, complaints, complaint_resolutions

**Modul Inventory: 12 Tables**
- products, product_categories, materials, stock_movements, stock_opnames, stock_opname_details, suppliers, purchase_requisitions, purchase_requisition_items, purchase_orders, purchase_order_items

**Modul Production: 6 Tables**
- work_orders, work_order_materials, work_order_resources, production_progress, quality_controls, qc_checklists, resources

**Modul Administration: 4 Tables**
- users, roles, permissions, role_permissions, audit_logs

**Relationship Types:**
- One-to-Many: 35+ relationships
- Many-to-One: 20+ relationships
- Many-to-Many: 3 relationships (via junction tables)
- One-to-One: 2 relationships

---

*Dokumen ini merupakan Part 4 dari Analisis dan Desain Sistem. Untuk Part 5 (User Interface Design), silakan lihat dokumen terpisah.*

