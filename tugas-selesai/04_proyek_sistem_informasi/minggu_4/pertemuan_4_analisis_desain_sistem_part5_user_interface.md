# ANALISIS DAN DESAIN SISTEM - PART 5
## SATRIAMART SIMS - User Interface Design
### Mockup dan Wireframe Antarmuka Pengguna

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi II**  
**Pertemuan 4 - User Interface Design**

---

## 5. USER INTERFACE DESIGN

### 5.1 Prinsip Desain UI/UX

Desain antarmuka pengguna SATRIAMART SIMS mengikuti prinsip-prinsip berikut:

#### A. Design Principles

**1. User-Centered Design**
- Fokus pada kebutuhan dan workflow pengguna
- Minimize cognitive load
- Intuitive navigation
- Contextual help dan guidance

**2. Consistency**
- Consistent layout across all modules
- Consistent color scheme dan typography
- Consistent interaction patterns
- Reusable UI components

**3. Visual Hierarchy**
- Clear information hierarchy
- Proper use of spacing dan alignment
- Emphasis on important actions
- Progressive disclosure untuk complex features

**4. Responsive Design**
- Mobile-first approach
- Adaptive layout untuk berbagai screen sizes
- Touch-friendly controls
- Optimized performance di semua devices

**5. Accessibility**
- WCAG 2.1 Level AA compliance
- Keyboard navigation support
- Screen reader compatibility
- Sufficient color contrast
- Clear error messages

#### B. Design System

**Color Palette:**
```
Primary Colors:
- Primary Blue:     #3B82F6 (Buttons, Links, Active States)
- Primary Dark:     #1E40AF (Hover States)
- Primary Light:    #DBEAFE (Background, Highlights)

Neutral Colors:
- Gray 900:         #111827 (Headings, Primary Text)
- Gray 700:         #374151 (Body Text)
- Gray 500:         #6B7280 (Secondary Text)
- Gray 300:         #D1D5DB (Borders, Dividers)
- Gray 100:         #F3F4F6 (Background, Cards)
- White:            #FFFFFF (Main Background)

Status Colors:
- Success Green:    #10B981 (Success Messages, Completed)
- Warning Yellow:   #F59E0B (Warning, Pending)
- Danger Red:       #EF4444 (Error, Critical)
- Info Blue:        #3B82F6 (Information)
```

**Typography:**
```
Font Family:
- Headings: Inter, sans-serif
- Body:     Inter, sans-serif
- Monospace: 'Courier New', monospace (untuk kode, nomor)

Font Sizes:
- Heading 1:   2.25rem (36px) - Bold
- Heading 2:   1.875rem (30px) - Bold
- Heading 3:   1.5rem (24px) - Semibold
- Heading 4:   1.25rem (20px) - Semibold
- Body Large:  1.125rem (18px) - Regular
- Body:        1rem (16px) - Regular
- Body Small:  0.875rem (14px) - Regular
- Caption:     0.75rem (12px) - Regular
```

**Spacing System:**
```
- xs:  4px
- sm:  8px
- md:  16px
- lg:  24px
- xl:  32px
- 2xl: 48px
- 3xl: 64px
```

**Border Radius:**
```
- sm:  4px (Inputs, Small Buttons)
- md:  8px (Cards, Buttons)
- lg:  12px (Modals, Large Cards)
- full: 9999px (Pills, Avatars)
```

---

### 5.2 Layout Structure

#### Global Layout - Desktop View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SATRIAMART SIMS                                    │
│  Header / Top Navigation Bar (Height: 64px)                                 │
│  [Logo] SATRIAMART SIMS    [Search]    [Notifications] [User Profile ▼]    │
└─────────────────────────────────────────────────────────────────────────────┘
│                              │                                              │
│  Sidebar Navigation          │         Main Content Area                    │
│  (Width: 256px)              │         (Fluid Width)                        │
│                              │                                              │
│  ┌──────────────────────┐   │  ┌───────────────────────────────────────┐  │
│  │ 📊 Dashboard         │   │  │                                       │  │
│  │ 👥 CRM               │   │  │                                       │  │
│  │   ├─ Customers       │   │  │         Page Content                  │  │
│  │   ├─ Orders          │   │  │         (Dynamic based on route)      │  │
│  │   └─ Communications  │   │  │                                       │  │
│  │ 📦 Inventory         │   │  │                                       │  │
│  │   ├─ Products        │   │  │                                       │  │
│  │   ├─ Materials       │   │  │                                       │  │
│  │   ├─ Stock Opname    │   │  │                                       │  │
│  │   └─ Suppliers       │   │  │                                       │  │
│  │ 🏭 Production        │   │  │                                       │  │
│  │   ├─ Work Orders     │   │  │                                       │  │
│  │   ├─ Schedule        │   │  │                                       │  │
│  │   └─ Quality Control │   │  │                                       │  │
│  │ 📈 Analytics         │   │  │                                       │  │
│  │ ⚙️  Settings         │   │  │                                       │  │
│  └──────────────────────┘   │  └───────────────────────────────────────┘  │
│                              │                                              │
└──────────────────────────────┴──────────────────────────────────────────────┘
```

#### Responsive Layout - Mobile View

```
┌─────────────────────────────┐
│ ☰  SATRIAMART    🔔  👤    │  ← Header (Hamburger Menu)
├─────────────────────────────┤
│                             │
│                             │
│      Main Content           │
│      (Full Width)           │
│                             │
│                             │
│                             │
│                             │
│                             │
│                             │
│                             │
├─────────────────────────────┤
│  🏠  📦  🏭  📊  ⚙️        │  ← Bottom Navigation (Mobile)
└─────────────────────────────┘
```

---

### 5.3 UI Mockup - Dashboard Executive

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SATRIAMART SIMS                                    🔔 Notif   👤 Admin ▼  │
└─────────────────────────────────────────────────────────────────────────────┘

┌───┐  ┌──────────────────────────────────────────────────────────────────────┐
│ 📊│  │  Dashboard                                    🔄 Refresh  📅 Jan 2024│
│ 👥│  ├──────────────────────────────────────────────────────────────────────┤
│ 📦│  │                                                                      │
│ 🏭│  │  Selamat Datang, Bapak Satria! 👋                                   │
│ 📈│  │  Berikut ringkasan bisnis hari ini                                  │
│ ⚙️ │  │                                                                      │
└───┘  │  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐          │
       │  │ 💰 Total Sales │ │ 📦 Orders      │ │ 👥 Customers   │          │
       │  │                │ │                │ │                │          │
       │  │  Rp 45.5 Juta  │ │      23        │ │      156       │          │
       │  │  ↑ 12% vs kemarin│ ↓ 3 orders     │ │  +5 baru       │          │
       │  └────────────────┘ └────────────────┘ └────────────────┘          │
       │                                                                      │
       │  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐          │
       │  │ 🏭 Production  │ │ 📊 Inventory   │ │ ⚠️ Alerts      │          │
       │  │                │ │                │ │                │          │
       │  │   18 WO Aktif  │ │  Rp 125 Juta   │ │   5 Low Stock  │          │
       │  │   92% On-Time  │ │  320 Items     │ │   2 Overdue    │          │
       │  └────────────────┘ └────────────────┘ └────────────────┘          │
       │                                                                      │
       │  ┌─────────────────────────────────────────────────────────────┐    │
       │  │ 📈 Sales Trend (7 Hari Terakhir)                            │    │
       │  │                                                             │    │
       │  │   50M ┤                                              ●      │    │
       │  │       ┤                                         ●            │    │
       │  │   40M ┤                                    ●                 │    │
       │  │       ┤                               ●                      │    │
       │  │   30M ┤                          ●                           │    │
       │  │       ┤                     ●                                │    │
       │  │   20M ┤                ●                                     │    │
       │  │       └───┬────┬────┬────┬────┬────┬────┬────               │    │
       │  │          16   17   18   19   20   21   22  Jan               │    │
       │  └─────────────────────────────────────────────────────────────┘    │
       │                                                                      │
       │  ┌──────────────────────────┐  ┌──────────────────────────────┐    │
       │  │ 🔥 Top Products          │  │ 📋 Recent Orders             │    │
       │  │                          │  │                              │    │
       │  │ 1. Nomor Rumah Akrilik   │  │ ORD-0145  Pak Budi  Rp 850K  │    │
       │  │    124 terjual           │  │ ORD-0144  Bu Ani    Rp 1.2M  │    │
       │  │                          │  │ ORD-0143  PT Makmur Rp 3.5M  │    │
       │  │ 2. Signage Kantor        │  │ ORD-0142  Pak Joko  Rp 650K  │    │
       │  │    87 terjual            │  │ ORD-0141  Bu Siti   Rp 420K  │    │
       │  │                          │  │                              │    │
       │  │ 3. Papan Nama Toko       │  │ [Lihat Semua Orders →]       │    │
       │  │    65 terjual            │  │                              │    │
       │  └──────────────────────────┘  └──────────────────────────────┘    │
       │                                                                      │
       └──────────────────────────────────────────────────────────────────────┘
```

**Fitur Dashboard:**
- Quick metrics dengan trend indicators (↑↓)
- Visual chart untuk sales trend
- Top products ranking
- Recent orders list
- Alert summary untuk actionable items
- Auto-refresh data setiap 5 menit

---

### 5.4 UI Mockup - Customer Management (CRM)

#### 5.4.1 Customer List Page

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  👥 Customer Management                          🔍 Search  [+ New Customer]│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Filters: [All Types ▼]  [All Status ▼]  [Date Range ▼]     📥 Export CSV │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Code    │ Name         │ Email          │ Phone        │ Type │ Action│   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ CUST-001│ Budi Santoso │ budi@email.com │ 08123456789  │ 🏢   │ [...]│   │
│  │         │              │                │              │ Corp │  👁 ✏️│   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ CUST-002│ Ani Wijaya   │ ani@email.com  │ 08198765432  │ 👤   │ [...]│   │
│  │         │              │                │              │ Indiv│  👁 ✏️│   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ CUST-003│ PT Sejahtera │ info@pt.co.id  │ 02112345678  │ 🏢   │ [...]│   │
│  │         │              │                │              │ Corp │  👁 ✏️│   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ CUST-004│ Joko Purnomo │ joko@email.com │ 08134567890  │ 🔄   │ [...]│   │
│  │         │              │                │              │Resel │  👁 ✏️│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Showing 1-10 of 156 customers        [◀ Prev]  [1] 2 3 4 ... 16  [Next ▶]│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 5.4.2 Add/Edit Customer Form

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ✕ Add New Customer                                          [Save] [Cancel]│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Customer Information                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  Customer Code *                                                    │   │
│  │  ┌───────────────────────────────────────┐                         │   │
│  │  │ CUST-0157 (Auto-generated)            │  🔒 Auto                │   │
│  │  └───────────────────────────────────────┘                         │   │
│  │                                                                     │   │
│  │  Full Name *                                                        │   │
│  │  ┌───────────────────────────────────────┐                         │   │
│  │  │ Enter customer name...                │                         │   │
│  │  └───────────────────────────────────────┘                         │   │
│  │                                                                     │   │
│  │  Customer Type *                                                    │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                  │   │
│  │  │ ○ Individual│ │ ○ Company   │ │ ○ Reseller  │                  │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘                  │   │
│  │                                                                     │   │
│  │  Email *                            Phone *                         │   │
│  │  ┌─────────────────────────┐        ┌─────────────────────┐        │   │
│  │  │ email@example.com       │        │ 08123456789         │        │   │
│  │  └─────────────────────────┘        └─────────────────────┘        │   │
│  │                                                                     │   │
│  │  Address                                                            │   │
│  │  ┌───────────────────────────────────────┐                         │   │
│  │  │ Jl. Example No. 123                   │                         │   │
│  │  │                                       │                         │   │
│  │  │                                       │                         │   │
│  │  └───────────────────────────────────────┘                         │   │
│  │                                                                     │   │
│  │  City                               Postal Code                    │   │
│  │  ┌─────────────────────────┐        ┌─────────────────────┐        │   │
│  │  │ Jakarta                 │        │ 12345               │        │   │
│  │  └─────────────────────────┘        └─────────────────────┘        │   │
│  │                                                                     │   │
│  │  Notes (Optional)                                                   │   │
│  │  ┌───────────────────────────────────────┐                         │   │
│  │  │ Additional customer information...    │                         │   │
│  │  └───────────────────────────────────────┘                         │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│                                                    [💾 Save Customer]       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Form Validation:**
- Real-time validation saat user typing
- Email format validation
- Phone number format validation (Indonesia)
- Required field indicators (*)
- Error messages shown below each field

---

### 5.5 UI Mockup - Order Management

#### 5.5.1 Create Order Page

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  📝 Create New Order                                     [Save Draft] [Submit]│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Step 1: Customer Selection                                           [1/3] │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  Select Customer *                                                  │   │
│  │  ┌────────────────────────────────────────────┐  [+ New Customer]  │   │
│  │  │ 🔍 Search by name, email, or phone...      │                    │   │
│  │  └────────────────────────────────────────────┘                    │   │
│  │                                                                     │   │
│  │  ✓ Selected: Budi Santoso (CUST-001)                               │   │
│  │    📧 budi@email.com  📱 08123456789                                │   │
│  │    📍 Jl. Merdeka No. 45, Jakarta                                   │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Step 2: Select Products                                              [2/3] │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  [+ Add Product]                                                    │   │
│  │                                                                     │   │
│  │  ┌───────────────────────────────────────────────────────────┐     │   │
│  │  │ 🖼️ Product      │ Specs        │ Qtbiar tidak limit.y │ Price    │ Total  │ ✕  │     │   │
│  │  ├───────────────────────────────────────────────────────────┤     │   │
│  │  │ Nomor Rumah    │ 30x20cm      │  2  │ 250,000  │ 500K   │ ✕  │     │   │
│  │  │ Akrilik        │ Warna: Gold  │     │          │        │    │     │   │
│  │  ├───────────────────────────────────────────────────────────┤     │   │
│  │  │ Signage Kantor │ 100x50cm     │  1  │ 850,000  │ 850K   │ ✕  │     │   │
│  │  │ Akrilik        │ Logo Custom  │     │          │        │    │     │   │
│  │  └───────────────────────────────────────────────────────────┘     │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Step 3: Order Details                                                [3/3] │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  Estimated Delivery Date *                                          │   │
│  │  ┌─────────────────────┐                                            │   │
│  │  │ 📅 30 January 2024  │  (Lead time: 7 hari kerja)                │   │
│  │  └─────────────────────┘                                            │   │
│  │                                                                     │   │
│  │  Special Request / Notes                                            │   │
│  │  ┌───────────────────────────────────────┐                         │   │
│  │  │ Logo harus sesuai file yang dikirim   │                         │   │
│  │  │ via email                             │                         │   │
│  │  └───────────────────────────────────────┘                         │   │
│  │                                                                     │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │ Order Summary                                               │   │   │
│  │  ├─────────────────────────────────────────────────────────────┤   │   │
│  │  │ Subtotal (2 items):               Rp 1,350,000             │   │   │
│  │  │ Discount (10%):                   - Rp   135,000            │   │   │
│  │  │ ─────────────────────────────────────────────────────────── │   │   │
│  │  │ Total:                            Rp 1,215,000             │   │   │
│  │  └─────────────────────────────────────────────────────────────┘   │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│                                                          [📋 Submit Order]  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 5.5.2 Order Detail & Tracking

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  📦 Order Detail - ORD-20240122-0145                   [Edit] [Print] [✕]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Order Status Timeline                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  ✓ Pending      ✓ Confirmed    ✓ Production    ⏳ QC    ○ Ready   │   │
│  │  22 Jan 10:30   22 Jan 11:00   23 Jan 08:00   24 Jan   25 Jan     │   │
│  │                                                                     │   │
│  │  Progress: ████████████████░░░░ 75%                                │   │
│  │  Estimated Completion: 25 January 2024                              │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌──────────────────────────┐  ┌──────────────────────────────────────┐   │
│  │ Customer Information     │  │ Order Information                    │   │
│  ├──────────────────────────┤  ├──────────────────────────────────────┤   │
│  │ 👤 Budi Santoso          │  │ Order Number: ORD-20240122-0145      │   │
│  │ 📧 budi@email.com        │  │ Order Date: 22 January 2024          │   │
│  │ 📱 08123456789           │  │ Delivery Date: 30 January 2024       │   │
│  │ 📍 Jl. Merdeka No. 45    │  │ Status: In Production 🏭             │   │
│  │    Jakarta               │  │                                      │   │
│  └──────────────────────────┘  └──────────────────────────────────────┘   │
│                                                                             │
│  Order Items                                                                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Product                   │ Specs        │ Qty │ Price   │ Total   │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ 🖼️ Nomor Rumah Akrilik    │ 30x20cm      │  2  │ 250K    │ 500K    │   │
│  │                           │ Warna: Gold  │     │         │         │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ 🖼️ Signage Kantor Akrilik │ 100x50cm     │  1  │ 850K    │ 850K    │   │
│  │                           │ Logo Custom  │     │         │         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Special Request:                                                           │
│  "Logo harus sesuai file yang dikirim via email"                            │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Subtotal:                                         Rp 1,350,000      │   │
│  │ Discount (10%):                                   - Rp   135,000    │   │
│  │ ───────────────────────────────────────────────────────────────────  │   │
│  │ Total Amount:                                     Rp 1,215,000      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Activity Log                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 📝 24 Jan 14:30 - Production started (by: Joko Prod)                │   │
│  │ 📝 23 Jan 09:00 - Work Order WO-20240123-012 created                │   │
│  │ 📝 22 Jan 11:00 - Order confirmed (by: Ani Sales)                   │   │
│  │ 📝 22 Jan 10:30 - Order created (by: Ani Sales)                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 5.6 UI Mockup - Inventory Management

#### 5.6.1 Stock Monitoring Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  📦 Stock Monitoring                              🔍 Search  [Stock Opname] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Stock Overview                                                             │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐  │
│  │ 📦 Total Items│ │ ⚠️ Low Stock  │ │ ❌ Out of Stock│ │ 💰 Total Value│  │
│  │      320      │ │      12       │ │       3        │ │   Rp 125 Juta │  │
│  └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘  │
│                                                                             │
│  Filters: [All Categories ▼]  [All Status ▼]              📥 Export Excel │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Code   │ Name            │ Category │ Stock │ Reorder │ Status │ Act│   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ PRD-001│ Nomor Rumah 20cm│ Nomor    │  45   │   20    │ ✅ OK  │[...]│   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ PRD-002│ Signage 50x30   │ Signage  │  12   │   15    │ ⚠️ Low │[...]│   │
│  │        │                 │          │       │         │        │    │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ PRD-003│ Papan Nama Custom│ Papan   │   0   │   10    │ ❌ Out │[...]│   │
│  │        │                 │          │       │         │        │    │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ MAT-001│ Acrylic Sheet 3mm│Material│ 150   │   50    │ ✅ OK  │[...]│   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ MAT-002│ Adhesive Glue   │ Material│   8   │   10    │ ⚠️ Low │[...]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Showing 1-10 of 320 items            [◀ Prev]  [1] 2 3 4 ... 32  [Next ▶]│
│                                                                             │
│  Low Stock Alerts (Action Required)                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ⚠️  PRD-002 - Signage 50x30 (Stock: 12, Reorder: 15)                │   │
│  │     [Create Purchase Requisition]                                   │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ ⚠️  MAT-002 - Adhesive Glue (Stock: 8, Reorder: 10)                 │   │
│  │     [Create Purchase Requisition]                                   │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ ❌  PRD-003 - Papan Nama Custom (Stock: 0, OUT OF STOCK!)           │   │
│  │     [Create Purchase Requisition - URGENT]                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 5.6.2 Stock Opname Interface

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  📋 Stock Opname - OPN-20240122-001                       [Save] [Complete] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Opname Information                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Opname Number: OPN-20240122-001                                     │   │
│  │ Cutoff Date: 22 January 2024, 17:00                                 │   │
│  │ Conducted by: Ani (Inventory Staff)                                 │   │
│  │ Status: In Progress ⏳                                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Stock Count                                                                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Code    │ Product/Material │ System │ Physical │ Variance │ Notes  │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ PRD-001 │ Nomor Rumah 20cm │   45   │ [  42  ] │   -3     │ [...]  │   │
│  │         │                  │        │    ✓     │   🔴     │        │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ PRD-002 │ Signage 50x30    │   12   │ [  12  ] │    0     │ [...]  │   │
│  │         │                  │        │    ✓     │   ✅     │        │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ MAT-001 │ Acrylic Sheet 3mm│  150   │ [ 148  ] │   -2     │ [...]  │   │
│  │         │                  │        │    ✓     │   🔴     │        │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ MAT-002 │ Adhesive Glue    │    8   │ [   8  ] │    0     │ [...]  │   │
│  │         │                  │        │    ✓     │   ✅     │        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Count Progress: ████████░░░░ 65% (130/200 items counted)                  │
│                                                                             │
│  Variance Summary                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ✅ Match (no variance):     128 items                                │   │
│  │ 🔴 Variance detected:         2 items                                │   │
│  │ ⏳ Not yet counted:          70 items                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Actions:                                                                   │
│  [💾 Save Progress]  [📋 Generate Variance Report]  [✅ Complete Opname]   │
│                                                                             │
│  Note: Items with variance akan memerlukan approval Manager untuk          │
│        stock adjustment.                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 5.7 UI Mockup - Production Management

#### 5.7.1 Work Order List & Calendar View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🏭 Work Orders                        [List View] [Calendar View] [+ New WO]│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Production Overview                                                        │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐              │
│  │ 📋 Total WO│ │ ⏳ Active  │ │ ⏰ Overdue │ │ ✅ Completed│              │
│  │     45     │ │     18     │ │      2     │ │     25      │              │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘              │
│                                                                             │
│  Filters: [All Status ▼]  [All Staff ▼]  [This Week ▼]                    │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ WO Number │ Order │ Product    │ Qty │ Due Date │ Progress│ Status │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ WO-001    │ORD-145│ Nomor Rumah│  2  │ 25 Jan   │ ███░░ 75%│ 🏭 Prod│   │
│  │           │       │ Akrilik    │     │          │          │        │   │
│  │ Assigned: Joko Prod              Due in: 1 day  │          [View]  │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ WO-002    │ORD-146│ Signage    │  1  │ 27 Jan   │ ████ 50% │ 🏭 Prod│   │
│  │           │       │ Kantor     │     │          │          │        │   │
│  │ Assigned: Budi Prod              Due in: 3 days │          [View]  │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ WO-003    │ORD-142│ Papan Nama │  3  │ 22 Jan   │ ██████100%│ ✅ QC  │   │
│  │           │       │ Toko       │     │          │          │        │   │
│  │ Assigned: Siti Prod              OVERDUE!       │          [QC]    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Production Calendar (Weekly View)                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Mon 22     │ Tue 23     │ Wed 24     │ Thu 25     │ Fri 26         │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ WO-001     │ WO-001     │ WO-001     │ WO-001     │ WO-002         │   │
│  │ (Joko)     │ (Joko)     │ (Joko)     │ (Joko)     │ (Budi)         │   │
│  │            │            │            │  [Due]     │                │   │
│  │ WO-002     │ WO-002     │ WO-002     │ WO-002     │ WO-003         │   │
│  │ (Budi)     │ (Budi)     │ (Budi)     │ (Budi)     │ (Siti)         │   │
│  │            │            │            │            │                │   │
│  │ WO-003     │ WO-004     │ WO-004     │            │                │   │
│  │ (Siti)     │ (Joko)     │ (Joko)     │            │                │   │
│  │ [OVERDUE]  │            │            │            │                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 5.7.2 Work Order Detail & Progress Update

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🏭 Work Order - WO-20240122-001                    [Update Progress] [QC]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  WO Status                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  ✓ Scheduled   ✓ Assigned   ✓ In Progress   ⏳ Completed   ○ QC   │   │
│  │  22 Jan        23 Jan        23 Jan          25 Jan         26 Jan │   │
│  │                                                                     │   │
│  │  Current Progress: ██████████████░░ 75%                             │   │
│  │  Started: 23 Jan 08:00  |  Expected Completion: 25 Jan 17:00       │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌──────────────────────────┐  ┌──────────────────────────────────────┐   │
│  │ Order Reference          │  │ Production Details                   │   │
│  ├──────────────────────────┤  ├──────────────────────────────────────┤   │
│  │ Order: ORD-20240122-0145 │  │ WO Number: WO-20240122-001           │   │
│  │ Customer: Budi Santoso   │  │ Product: Nomor Rumah Akrilik 20cm    │   │
│  │ Due Date: 30 Jan 2024    │  │ Quantity: 2 pcs                      │   │
│  │                          │  │ Assigned to: Joko Purnomo            │   │
│  │                          │  │ Supervisor: Pak Hendi                │   │
│  └──────────────────────────┘  └──────────────────────────────────────┘   │
│                                                                             │
│  Bill of Materials (BOM)                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Material           │ Required │ Used  │ Remaining │ Status         │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ Acrylic Sheet 3mm  │ 2 sheets │ 2     │ 0         │ ✅ Complete    │   │
│  │ Adhesive Glue      │ 50 ml    │ 45 ml │ 5 ml      │ ✅ Complete    │   │
│  │ Gold Paint         │ 30 ml    │ 25 ml │ 5 ml      │ ⏳ In Use      │   │
│  │ Packaging Box      │ 2 pcs    │ 0     │ 2         │ ⏹️ Not Started │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Production Progress Log                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 📸 24 Jan 14:30 - Progress 75%                                      │   │
│  │    "Finishing dan polishing hampir selesai"                         │   │
│  │    [View Photo]                                                     │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ 📸 24 Jan 09:00 - Progress 50%                                      │   │
│  │    "Cutting dan assembly selesai, mulai polishing"                  │   │
│  │    [View Photo]                                                     │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │ 📝 23 Jan 08:00 - Production started                                │   │
│  │    "Mulai proses cutting acrylic"                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  [➕ Add Progress Update]                                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 5.8 Responsive Design - Mobile View Examples

#### 5.8.1 Mobile Dashboard

```
┌───────────────────────┐
│ ☰ SATRIAMART  🔔  👤 │
├───────────────────────┤
│                       │
│ Dashboard             │
│                       │
│ Selamat Datang! 👋    │
│ Bpk. Satria           │
│                       │
│ ┌───────────────────┐ │
│ │ 💰 Total Sales    │ │
│ │                   │ │
│ │  Rp 45.5 Juta     │ │
│ │  ↑ 12% kemarin    │ │
│ └───────────────────┘ │
│                       │
│ ┌───────────────────┐ │
│ │ 📦 Orders         │ │
│ │                   │ │
│ │       23          │ │
│ │  ↓ 3 orders       │ │
│ └───────────────────┘ │
│                       │
│ ┌───────────────────┐ │
│ │ ⚠️ Alerts         │ │
│ │                   │ │
│ │  5 Low Stock      │ │
│ │  2 Overdue WO     │ │
│ └───────────────────┘ │
│                       │
│ Recent Orders         │
│ ┌───────────────────┐ │
│ │ ORD-0145          │ │
│ │ Pak Budi          │ │
│ │ Rp 850K  [View] ►│ │
│ ├───────────────────┤ │
│ │ ORD-0144          │ │
│ │ Bu Ani            │ │
│ │ Rp 1.2M  [View] ►│ │
│ └───────────────────┘ │
│                       │
├───────────────────────┤
│ 🏠 📦 🏭 📊 ⚙️       │  ← Bottom Nav
└───────────────────────┘
```

#### 5.8.2 Mobile Order Form

```
┌───────────────────────┐
│ ✕ Create Order        │
├───────────────────────┤
│                       │
│ Step 1 of 3           │
│ Customer Selection    │
│                       │
│ Search Customer       │
│ ┌───────────────────┐ │
│ │ 🔍 Search...      │ │
│ └───────────────────┘ │
│                       │
│ ✓ Budi Santoso        │
│   CUST-001            │
│   📧 budi@email.com   │
│   📱 08123456789      │
│                       │
│ [+ New Customer]      │
│                       │
├───────────────────────┤
│      [Next Step ►]    │
└───────────────────────┘
```

---

### 5.9 Interaction & Animation Guidelines

#### UI Interactions:

**Button States:**
- Default: Primary color dengan shadow
- Hover: Darker shade, lift shadow
- Active: Pressed effect dengan inner shadow
- Disabled: Gray color, no interaction
- Loading: Spinner animation

**Form Interactions:**
- Real-time validation
- Inline error messages (red text below field)
- Success indicators (green checkmark)
- Auto-save draft (untuk form panjang)
- Confirmation dialog untuk destructive actions

**Loading States:**
- Skeleton loading untuk data tables
- Spinner untuk button actions
- Progress bar untuk file upload
- Shimmer effect untuk cards

**Notifications:**
- Toast notifications (bottom-right corner)
- Auto-dismiss after 5 seconds
- Manual dismiss dengan close button
- Different colors per type (success, warning, error, info)

**Modals & Dialogs:**
- Backdrop overlay (semi-transparent black)
- Centered modal dengan shadow
- Close on ESC key
- Close on backdrop click (optional)

---

## Ringkasan User Interface Design

**Total UI Screens: 15+ Screens**

**Dashboard & Analytics:**
- Executive Dashboard
- Sales Analytics Dashboard
- Production Dashboard

**CRM Module:**
- Customer List
- Customer Form (Add/Edit)
- Customer Detail
- Order List
- Order Form (Create)
- Order Detail & Tracking

**Inventory Module:**
- Stock Monitoring Dashboard
- Product Management
- Stock Opname Interface
- Purchase Requisition Form
- Purchase Order Management

**Production Module:**
- Work Order List
- Work Order Calendar View
- Work Order Detail
- Quality Control Interface

**Administration:**
- User Management
- System Settings
- Audit Log

**Design System:**
- Consistent color palette (Primary Blue theme)
- Typography system (Inter font family)
- Spacing system (4px base unit)
- Component library (Buttons, Forms, Cards, Tables)
- Responsive grid system
- Mobile-friendly bottom navigation

**Key UI/UX Features:**
- Clean, modern interface
- Intuitive navigation
- Real-time data updates
- Interactive charts dan visualizations
- Status indicators dengan color coding
- Contextual actions (based on user role)
- Search dan filter functionality
- Export capabilities (PDF, Excel, CSV)
- Mobile responsive design
- Accessibility compliant (WCAG 2.1 AA)

---

*Dokumen ini merupakan Part 5 (Final) dari Analisis dan Desain Sistem SATRIAMART SIMS.*

**Struktur Lengkap Dokumen:**
- Part 1: Analisa Kebutuhan Sistem
- Part 2: Use Case Diagram
- Part 3: Activity Diagram
- Part 4: Entity Relationship Diagram (ERD)
- Part 5: User Interface Design (You are here)

