# LAMPIRAN F: FOTO DOKUMENTASI (Lanjutan)

## F.3 Dokumentasi Sistem dan Teknologi

### Observasi Infrastruktur Digital dan Sistem Operasional

---

### **FOTO F.3.1: Sistem Komunikasi Customer - WhatsApp Business**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Screenshot WhatsApp Business]                │
│                                                             │
│  ┌─────────────────────────────────────┐                   │
│  │  WhatsApp Business                  │                   │
│  │  ────────────────────────────        │                   │
│  │                                      │                   │
│  │  💬 Customer Inquiry #1              │                   │
│  │  📱 +62 812-xxxx-xxxx               │                   │
│  │  "Halo, mau tanya harga nomor       │                   │
│  │   rumah akrilik ukuran 30x40cm..."  │                   │
│  │                                      │                   │
│  │  Response Time: ⏱ 1 jam 23 menit    │                   │
│  │  Status: ✅ Quoted                   │                   │
│  │  ────────────────────────────        │                   │
│  │                                      │                   │
│  │  💬 Customer Inquiry #2              │                   │
│  │  📱 +62 878-xxxx-xxxx               │                   │
│  │  "Bisa kirim foto sample huruf      │                   │
│  │   3D yang pernah dibuat?"           │                   │
│  │                                      │                   │
│  │  Response Time: ⏱ 15 menit          │                   │
│  │  Status: ✅ Sample sent              │                   │
│  │  ────────────────────────────        │                   │
│  │                                      │                   │
│  │  [Type message...]  📎 📷 🎤        │                   │
│  └─────────────────────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Platform:** WhatsApp Business
- **Tanggal Capture:** 17 Agustus 2025
- **Observasi:** Real-time customer communication

**Deskripsi Sistem:**
WhatsApp Business menjadi primary channel komunikasi dengan customer (±85% inquiry masuk via WhatsApp).

**Features yang Digunakan:**
- ✓ Business profile (nama, alamat, jam operasional, website)
- ✓ Quick replies untuk FAQ
- ✓ Labels untuk kategorisasi chat (New, Quoted, Processing, Done)
- ✓ Catalog (produk showcase dengan harga)
- ✓ Away message (di luar jam kerja)
- ⚠ WhatsApp Business API belum (masih regular Business app)

**Performance Metrics (Data 1 Minggu):**
- Total inquiries: 47
- Response time avg: 1.8 jam
- Response time target: <2 jam (achieved 78%)
- Conversion to quotation: 68%
- No response rate: 5%

**Customer Journey via WhatsApp:**
1. **Inquiry:** Customer kirim pertanyaan/foto referensi
2. **Clarification:** CS tanya detail requirement
3. **Quotation:** CS kirim quote via PDF atau text
4. **Negotiation:** Diskusi harga, revisi spec (if needed)
5. **Deal:** Customer confirm, DP transfer
6. **Execution:** Update progress via foto/video
7. **Delivery:** Koordinasi pengiriman
8. **After-sales:** Follow-up kepuasan

**Observasi Kunci:**
- ✓ Responsiveness bagus (fast reply)
- ✓ Personal touch (friendly, helpful)
- ✓ Visual communication effective (foto sample, mockup)
- ⚠ Chat history tersebar di personal phone (not centralized)
- ⚠ Tidak ada backup jika phone loss
- ⚠ Sulit untuk analytics (berapa inquiry, conversion rate, etc.)
- ⚠ Multi-agent challenge (jika CS >1, siapa handle apa?)

**Relevansi dengan Analisis:**
WhatsApp sebagai primary channel membuktikan digital presence strong (Strength S6), tapi keterbatasan sistem manual juga evident (Weakness W9 - Data Management). Migration ke WhatsApp Business API dan integrasi dengan CRM (Action Plan WO3) akan solve issues ini.

---

### **FOTO F.3.2: Sistem Quotation - Manual Excel Based**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Screenshot Excel Quotation]                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Microsoft Excel - Quotation Template               │   │
│  │  ─────────────────────────────────────────────────  │   │
│  │                                                      │   │
│  │  SATRIAMART - Penawaran Harga                       │   │
│  │  No: QT-2025-08-017                                 │   │
│  │  Tanggal: 17 Agustus 2025                           │   │
│  │                                                      │   │
│  │  Kepada: Bpk. Ahmad [Customer]                      │   │
│  │  ────────────────────────────────────────────────   │   │
│  │                                                      │   │
│  │  | Item | Spec | Qty | Price | Total |             │   │
│  │  |------|------|-----|-------|-------|             │   │
│  │  | Huruf| 40cm | 10  | 250k  | 2.5M  |             │   │
│  │  | 3D   | Black| pcs |       |       |             │   │
│  │  | LED  | WW   |     |       |       |             │   │
│  │  |------|------|-----|-------|-------|             │   │
│  │  | Ins- | On-  | 1   | 500k  | 500k  |             │   │
│  │  | tall | site | set |       |       |             │   │
│  │  |------|------|-----|-------|-------|             │   │
│  │  |           TOTAL    |       | 3.0M  |             │   │
│  │  ────────────────────────────────────────────────   │   │
│  │                                                      │   │
│  │  [Manual Entry: Name, Date, Items...]               │   │
│  │  [Formula: SUM, Calculations]                       │   │
│  │  [Save As PDF] → Send via WhatsApp/Email            │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Software:** Microsoft Excel
- **Template:** Semi-standardized (ada template dasar, manual modify)
- **Process:** Manual input semua data

**Quotation Workflow:**
1. Terima requirement dari customer (via WhatsApp/phone)
2. Buka Excel template
3. Manual input customer info, item details, pricing
4. Calculation (mostly automated formula, tapi check manual)
5. Add terms & conditions (copy-paste from previous)
6. Save as PDF
7. Send via WhatsApp atau email

**Time Required:**
- Simple quote (1-2 items): 20-30 menit
- Complex quote (multiple items, custom pricing): 45-60 menit
- Revision: 15-20 menit per revision

**Observasi Kunci:**
- ✓ Template exists (consistency)
- ✓ Professional looking output (PDF)
- ✓ Calculations automated (formula)
- ⚠ **Time-consuming:** Manual data entry semua field
- ⚠ **Error-prone:** Typo di nama customer, spec, pricing
- ⚠ **No database:** Pricing harus cek manual atau ingat
- ⚠ **No version control:** Revisi save as new file, sulit track
- ⚠ **Not integrated:** Customer data re-input setiap quote

**Common Issues:**
- Pricing inconsistency (tergantung siapa yang bikin quote)
- Lupa include detail (mounting, installation, delivery fee)
- Calculation error (jarang, tapi pernah terjadi)
- Lost quotes (file di local computer, tidak backed up)

**Improvement Potential:**
- Automated quotation system dengan database
- Customer history (previous quotes, preferences)
- Product catalog dengan standard pricing
- Approval workflow (jika quote di atas threshold)
- Analytics (quote success rate, pricing trends)

**Relevansi dengan Analisis:**
Manual quotation process adalah inefficiency signifikan (Weakness W1, W3). Digital quotation system adalah quick win opportunity (Action Plan WT1 - Lampiran C.3).

---

### **FOTO F.3.3: Data Management - Google Drive & Spreadsheets**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Screenshot Google Drive Structure]           │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Google Drive - SATRIAMART                          │   │
│  │  ─────────────────────────────────────────────────  │   │
│  │                                                      │   │
│  │  📁 Quotations                                      │   │
│  │     📁 2024                                         │   │
│  │     📁 2025                                         │   │
│  │        📁 January                                   │   │
│  │        📁 February                                  │   │
│  │        ...                                          │   │
│  │        📁 August                                    │   │
│  │           📄 QT-2025-08-001.pdf                     │   │
│  │           📄 QT-2025-08-002.pdf                     │   │
│  │           ...                                       │   │
│  │                                                      │   │
│  │  📁 Design Files                                    │   │
│  │     📁 Client A                                     │   │
│  │     📁 Client B                                     │   │
│  │     ...                                             │   │
│  │                                                      │   │
│  │  📁 Documentation                                   │   │
│  │  📁 Photos                                          │   │
│  │  📁 Administrative                                  │   │
│  │                                                      │   │
│  │  📊 [Master Data.xlsx]                              │   │
│  │     - Customer list                                 │   │
│  │     - Inventory tracking                            │   │
│  │     - Order status                                  │   │
│  │     - Financial summary                             │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Platform:** Google Drive (Business)
- **Storage:** 1TB (±30% used)
- **Users:** 4-5 team members dengan access

**File Organization:**
Folder structure cukup organized dengan hierarchy:
- By function (Quotations, Design, Photos, etc.)
- By year/month untuk documents
- By client untuk design files

**Key Spreadsheets:**

**1. Master Customer Data**
- Customer name, contact, address
- Project history
- Payment status
- Notes
- **Update frequency:** Manual, as needed
- **Data quality:** 70% (ada missing info, duplicate entries)

**2. Inventory Tracking**
- Material list dengan stock level
- Reorder point (manual set)
- Last purchase date & supplier
- **Update frequency:** Weekly (target), reality: irregular
- **Accuracy:** ±85% (frequent discrepancy)

**3. Order Tracking**
- Active orders dengan status
- Timeline (expected completion)
- Assigned staff
- **Update:** Daily (target), reality: 2-3 days
- **Completeness:** 80%

**4. Financial Tracker**
- Income dari project (manual entry)
- Expenses (material, overhead)
- Cash flow projection (basic)
- **Update:** Monthly
- **Detail level:** Aggregate, tidak detail

**Observasi Kunci:**
- ✓ Cloud-based (accessible, auto backup)
- ✓ Collaborative (multiple users)
- ✓ Free/low-cost solution
- ⚠ **No integration:** Semua data siloed (quotation, inventory, customer separated)
- ⚠ **Manual updates:** Time-consuming, prone to forget
- ⚠ **No automation:** Tidak ada automated reports, alerts
- ⚠ **Data quality issues:** Missing data, duplicates, inconsistencies
- ⚠ **No real-time:** Data always lag (2-3 hari behind reality)
- ⚠ **Limited analytics:** Basic spreadsheet charts, no advanced insights

**Pain Points Identified:**
1. "Kami sering lupa update spreadsheet, data jadi tidak real-time"
2. "Kalau mau cari data customer lama, susah. Harus scroll manual"
3. "Inventory sering beda antara catatan vs fisik"
4. "Tidak ada alert kalau stock habis, baru tahu saat mau produksi"
5. "Report financial harus compile manual tiap bulan, 2-3 hari kerja"

**Relevansi dengan Analisis:**
Data management challenge adalah core weakness (W1, W2, W9). Ini fundamental problem yang menghambat scaling dan decision making. ERP implementation (Action Plan WO1) akan address semua issues ini dengan integrated database, real-time updates, dan automated workflows.

---

### **FOTO F.3.4: Machine Control - CNC Software Interface**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Screenshot CNC Control Software]             │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  CNC Control - Mach3 Interface                      │   │
│  │  ─────────────────────────────────────────────────  │   │
│  │                                                      │   │
│  │  ┌───────────────┐    ┌────────────────┐           │   │
│  │  │  WORK VIEW    │    │  CONTROL PANEL │           │   │
│  │  │               │    │                │           │   │
│  │  │     ┌───┐     │    │  X:  125.45 mm │           │   │
│  │  │     │   │     │    │  Y:  380.22 mm │           │   │
│  │  │     │   │     │    │  Z:   -2.50 mm │           │   │
│  │  │     └───┘     │    │                │           │   │
│  │  │   Tool path   │    │  Feed: 3500    │           │   │
│  │  │               │    │  RPM:  18000   │           │   │
│  │  │               │    │                │           │   │
│  │  └───────────────┘    │  [Start][Pause]│           │   │
│  │                       │  [Stop] [Reset]│           │   │
│  │  ┌─────────────────┐  └────────────────┘           │   │
│  │  │  Status:        │                               │   │
│  │  │  ● Running      │  Progress: ████░░░░ 45%       │   │
│  │  │  Time: 23:15    │  ETA: 18 minutes              │   │
│  │  └─────────────────┘                               │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Software:** Mach3 CNC Control
- **Interface:** PC Windows-based
- **Connection:** USB ke CNC controller

**Design to Production Workflow:**

**Step 1: Design (Designer)**
- Create vector design (Illustrator/CorelDRAW)
- Export to DXF or SVG format

**Step 2: CAM Programming**
- Import DXF ke CAM software (VCarve, Fusion 360, atau similar)
- Set parameters:
  * Material thickness
  * Tool selection (bit size, type)
  * Cut depth
  * Feed rate & spindle speed
  * Toolpath strategy (pocket, profile, drill, etc.)
- Generate G-code

**Step 3: CNC Setup**
- Load G-code ke Mach3
- Material setup di CNC bed
- Tool installation
- Zero point setting (X, Y, Z)

**Step 4: Execution**
- Dry run atau simulation (optional, tapi recommended)
- Start cutting
- Monitor progress
- Handle any issues (pause jika perlu)

**Step 5: Complete**
- Remove part dari bed
- Clean up
- Inspect quality

**Observasi Kunci:**
- ✓ Operator kompeten dengan software
- ✓ Simulation feature digunakan untuk complex jobs
- ✓ Real-time monitoring (position, speed, progress)
- ⚠ No automatic optimization (feeds & speeds manual set, based on experience)
- ⚠ No machine data logging (run time, efficiency, failures)
- ⚠ No remote monitoring (harus di tempat untuk monitor)
- ⚠ Single point of failure (jika PC/software crash, production stop)

**Technology Opportunity:**
- **IoT sensors:** Track machine status, utilization, maintenance needs
- **Cloud-based monitoring:** Remote visibility untuk management
- **AI optimization:** Automated parameter optimization untuk efficiency
- **Predictive maintenance:** Forecast equipment failures before happen

**Relevansi dengan Analisis:**
Current technology adequate untuk operations, tapi ada significant opportunity untuk upgrade ke smart manufacturing (Lampiran D.3 - Smart Factory Initiative). Ini akan be part dari jangka panjang strategy.

---

### **FOTO F.3.5: Digital Marketing - Social Media Presence**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Screenshots Social Media]                    │
│                                                             │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────┐   │
│  │  INSTAGRAM     │  │  TIKTOK        │  │  YOUTUBE   │   │
│  │  @satriamart   │  │  @satriamart   │  │ @satriamart│   │
│  │  ────────────  │  │  ────────────  │  │ ────────── │   │
│  │                │  │                │  │            │   │
│  │  👥 8.5K       │  │  👥 12.3K      │  │ 👥 2.1K    │   │
│  │  Followers     │  │  Followers     │  │ Subs       │   │
│  │                │  │                │  │            │   │
│  │  📸 Post: 247  │  │  🎬 Videos: 89 │  │ 🎥 Vids:47 │   │
│  │                │  │                │  │            │   │
│  │  Recent:       │  │  Viral post:   │  │ Recent:    │   │
│  │  🖼 Nomor rumah│  │  ⚡ 125K views  │  │ 🎥 Tutorial│   │
│  │  ❤ 234 likes  │  │  💬 523 cmnts  │  │ 👍 89 likes│   │
│  │  💬 18 cmnts   │  │  🔗 15 shares  │  │ ⏱ 8:23 min │   │
│  │                │  │                │  │            │   │
│  │  Engagement:   │  │  Engagement:   │  │ Avg Views: │   │
│  │  📊 2.8%       │  │  📊 4.2%       │  │ 📊 850     │   │
│  └────────────────┘  └────────────────┘  └────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Platforms:** Instagram, TikTok, YouTube
- **Update frequency:** 3-5x per minggu
- **Content creator:** Owner + 1 staff (part-time)

**Social Media Strategy:**

**Instagram (@satriamart.id):**
- **Content type:** 
  * Product showcase (before-after installation)
  * Behind-the-scenes production
  * Customer testimonials
  * Design inspiration
- **Engagement rate:** 2.8% (industry avg: 1-3%)
- **Peak posting time:** 18:00-20:00 WIB
- **Story views:** 800-1,200 per story

**TikTok (@satriamart.id):**
- **Content type:**
  * Short process videos (cutting, polishing)
  * Time-lapse installation
  * Before-after transformation
  * Educational (tips, material explanation)
- **Viral success:** Beberapa video >100K views
- **Engagement rate:** 4.2% (very good)
- **Trending sounds:** Leverage popular music untuk reach

**YouTube (@satriamart.id):**
- **Content type:**
  * Full project documentation
  * Tutorial (DIY tips)
  * Product review
  * Company profile
- **Average view duration:** 5:30 menit (65% retention)
- **Subscriber growth:** +150/bulan
- **Revenue:** Minimal (not monetized yet, too small)

**Performance Metrics (Last 30 Days):**

| Platform | Reach | Engagement | Leads | Conversion |
|----------|-------|------------|-------|------------|
| Instagram | 28K | 785 | 23 | 8 deals |
| TikTok | 87K | 3,654 | 41 | 12 deals |
| YouTube | 6.5K | 218 | 7 | 3 deals |
| **Total** | **121K** | **4,657** | **71** | **23 deals** |

**Cost of Acquisition:**
- **Organic only:** Rp 0 (time investment only)
- **Cost per lead:** Rp 0 (organic)
- **Conversion rate:** 32% (lead to deal)
- **ROI:** Infinite (no paid ads, pure organic)

**Observasi Kunci:**
- ✓ **Strong organic reach** (Strength S6 confirmed)
- ✓ Consistent content creation (discipline)
- ✓ Authentic, relatable content (not overly salesy)
- ✓ Engage dengan comments (build community)
- ✓ Multi-platform presence (diversified)
- ⚠ Belum explore paid ads (opportunity untuk scale)
- ⚠ Content planning tidak terstruktur (spontan)
- ⚠ No content calendar
- ⚠ Metrics tracking manual (screenshot, compile manual)
- ⚠ Not leveraging influencer partnerships yet

**Content Ideas dari Followers:**
- "Mas, bisa bikin tutorial cara memasang sendiri?"
- "Pengen liat process cutting pakai CNC dari awal"
- "Showcase project residential vs commercial beda gaya"
- "Behind the scenes team SATRIAMART"

**Improvement Opportunities:**
1. **Content calendar:** Plan 1-2 minggu ahead
2. **Analytics tools:** Use native insights lebih maksimal
3. **Paid ads experimentation:** Small budget test (Rp 1-2 juta/bulan)
4. **Influencer collaboration:** Home decor, property influencers
5. **User-generated content:** Encourage customer share & tag
6. **Live sessions:** Q&A, product demo, special promo

**Relevansi dengan Analisis:**
Social media sebagai primary lead generation channel (Opportunity O7) adalah major asset. Content marketing strategy (Action Plan SO5) akan sistemize dan maximize effectiveness. Budget minimal tapi hasil signifikan - clear ROI positive.

---

**RINGKASAN DOKUMENTASI F.3:**

**Digital Infrastructure Maturity Assessment:**

| Aspect | Maturity Level | Score |
|--------|----------------|-------|
| Customer Communication | Medium | 6/10 |
| Data Management | Low | 4/10 |
| Process Automation | Low | 3/10 |
| Production Technology | Medium | 6/10 |
| Digital Marketing | High | 8/10 |
| **Overall Digital Maturity** | **Medium-Low** | **5.4/10** |

**Strengths:**
- ✓ Digital marketing execution excellent (organic reach, engagement)
- ✓ Customer-facing communication responsive (WhatsApp)
- ✓ Cloud storage untuk file management

**Weaknesses:**
- ⚠ Backend systems manual dan fragmented
- ⚠ No integration antar sistem
- ⚠ No business intelligence capability
- ⚠ Limited automation

**Digital Transformation Priority:**
1. **High:** ERP system (integrate data, automate workflows)
2. **High:** CRM system (centralize customer data, automate follow-up)
3. **Medium:** Digital quotation (reduce turnaround time)
4. **Medium:** Website & customer portal (self-service, professional image)
5. **Low:** Advanced analytics & AI (future enhancement)

---

## F.4 Dokumentasi Hasil Karya dan Kolaborasi

### Showcase Portfolio dan Kemitraan Strategis

---

### **FOTO F.4.1: Portfolio Produk - Residential Projects**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Foto Kolase Produk Residential]              │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Nomor   │  │  Huruf   │  │  Welcome │  │   Wall   │   │
│  │  Rumah   │  │  Nama    │  │   Sign   │  │   Art    │   │
│  │  "B-17"  │  │ "AHMAD"  │  │ "Family" │  │  Custom  │   │
│  │          │  │          │  │          │  │          │   │
│  │  LED     │  │  3D 40cm │  │  Script  │  │  Quotes  │   │
│  │  Backlit │  │  Black   │  │  LED WW  │  │  Layered │   │
│  │          │  │          │  │          │  │          │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  Price Range: Rp 250K - 2.5M                                │
│  Typical Customer: Homeowner, middle-upper income           │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Category:** Residential Decor
- **Total Projects (2024-2025):** ±180 projects
- **Revenue contribution:** 55% dari total revenue

**Product Variations:**

**1. Nomor Rumah (House Number)**
- **Demand:** High (most requested)
- **Size:** 15cm - 40cm height
- **Material:** Akrilik 5-10mm, dengan atau tanpa LED
- **Price:** Rp 250K - 800K
- **Turnaround:** 3-5 hari
- **Unique value:** Customizable font, LED color options

**2. Nama Keluarga (Family Name)**
- **Demand:** Medium-High
- **Size:** 30cm - 80cm width (tergantung panjang nama)
- **Style:** 3D layered, backlit, engraved
- **Price:** Rp 500K - 2.5M
- **Turnaround:** 5-7 hari
- **Trend:** Script fonts popular, minimalist design

**3. Decorative Signs**
- **Type:** Welcome sign, quotes, wall art
- **Customization:** High (personal quotes, family rules, dll)
- **Price:** Rp 300K - 1.5M
- **Turnaround:** 5-10 hari
- **Trend:** Skandinavian style, monochrome colors

**4. Custom Requests**
- **Type:** Varies (company logo untuk home office, pet names, special occasions)
- **Price:** Varies, typically premium pricing
- **Challenge:** Unique design requirements, high expectation

**Customer Testimonials:**

> "Kualitas bagus, rapih, owner nya baik dan helpful. Pengerjaan cepat dan hasil memuaskan!" - Ibu Sari, Jakarta  
> ⭐⭐⭐⭐⭐

> "Nomor rumah dari SATRIAMART jadi eye-catching di depan rumah. Banyak tetangga tanya buatnya dimana. Recommended!" - Pak Budi, Depok  
> ⭐⭐⭐⭐⭐

**Observasi:**
- ✓ High repeat customer rate (±30% dari residential customer order lagi)
- ✓ Word-of-mouth strong (referral dari customer existing)
- ✓ Instagram/TikTok showcase effective untuk attract customer
- ⚠ Seasonality (peak saat long weekend, lebaran, natal, tahun baru)

---

### **FOTO F.4.2: Portfolio Produk - Commercial Projects**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Foto Kolase Produk Commercial]               │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Shop    │  │  Office  │  │  Cafe    │  │  Clinic  │   │
│  │  Sign    │  │  Logo    │  │  Menu    │  │  Room    │   │
│  │  Retail  │  │  3D LED  │  │  Board   │  │  Signs   │   │
│  │          │  │          │  │          │  │          │   │
│  │  Large   │  │  Premium │  │  Backlit │  │  Series  │   │
│  │  Format  │  │  Finish  │  │  Acrylic │  │  Uniform │   │
│  │          │  │          │  │          │  │          │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  Price Range: Rp 1M - 15M                                   │
│  Typical Customer: Business owner, corporate                │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Category:** Commercial Signage & Branding
- **Total Projects (2024-2025):** ±75 projects
- **Revenue contribution:** 45% dari total revenue (higher value per project)

**Product Categories:**

**1. Shop Signage**
- **Client type:** Retail stores, boutique, salon
- **Size:** 50cm - 200cm (large format)
- **Features:** LED illumination, weather-resistant
- **Price:** Rp 2M - 8M
- **Turnaround:** 10-14 hari
- **Challenge:** Installation on-site, alignment critical

**2. Office Branding**
- **Client type:** Corporate office, startup, co-working
- **Type:** Company logo 3D, reception sign, wayfinding
- **Material:** Premium akrilik, metal backing options
- **Price:** Rp 1.5M - 10M
- **Turnaround:** 7-14 hari
- **Trend:** Minimalist, professional aesthetic

**3. F&B Display**
- **Client type:** Restaurant, cafe, bakery
- **Type:** Menu board (backlit), promotional sign, table number
- **Features:** Easy-to-clean, food-safe material
- **Price:** Rp 800K - 5M (depending on qty & complexity)
- **Recurring:** Seasonal menu updates

**4. Healthcare & Service**
- **Client type:** Clinic, beauty salon, wellness center
- **Type:** Room signs, service menu, informational signage
- **Requirement:** Clean, professional look, durable
- **Price:** Rp 500K - 3M
- **Volume:** Series/multiple units (room numbers, dll)

**Notable Projects:**

**Project 1: Retail Chain (5 stores)**
- **Client:** [Fashion Retail Brand]
- **Scope:** Storefront signage + interior branding
- **Value:** Rp 35M (total, 5 stores)
- **Duration:** 3 bulan (rolling installation)
- **Challenge:** Brand consistency across locations
- **Result:** Success, customer planning untuk expand ke 10 stores

**Project 2: Corporate Office**
- **Client:** [Tech Startup, Jakarta]
- **Scope:** Reception logo 3D (150cm), department signs, wayfinding
- **Value:** Rp 8M
- **Duration:** 2 minggu
- **Highlight:** LED RGB color-changing logo (innovative)
- **Testimonial:** "Kantor jadi lebih professional dan modern. Good investment!"

**Commercial Customer Behavior:**
- Higher budget, more willing pay premium untuk quality
- Decision cycle longer (approval process, budgeting)
- Repeat business potential (branch expansion, renovation)
- Referrals within industry (networking effect)

**B2B Sales Challenge:**
- Quotation competition (tender, bandingkan beberapa vendor)
- Payment terms (30-60 hari, vs residential COD/DP 50%)
- After-sales service critical (warranty, maintenance)

**Opportunity:**
- Expand B2B focus (Target: 60% revenue dari B2B dalam 2 tahun)
- Long-term contract dengan chain stores
- Value-added services (installation, maintenance package)

---

### **FOTO F.4.3: Kolaborasi dengan Arsitek & Interior Designer**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Foto Dokumentasi Kolaborasi]                 │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  PARTNERSHIP PROGRAM                                 │  │
│  │  ──────────────────────────────────────────────────  │  │
│  │                                                       │  │
│  │  Mitra Arsitek & Interior Designer                   │  │
│  │                                                       │  │
│  │  ✓ 12 Active Partners (as of Aug 2025)              │  │
│  │  ✓ Preferred Supplier Status                        │  │
│  │  ✓ Project Referral Program                         │  │
│  │  ✓ Co-Marketing Opportunities                       │  │
│  │                                                       │  │
│  │  Benefits untuk Partners:                            │  │
│  │  • Exclusive trade pricing (10-15% discount)        │  │
│  │  • Priority production scheduling                    │  │
│  │  • Design consultation support                       │  │
│  │  • Sample library access                            │  │
│  │  • Commission on referrals                          │  │
│  │                                                       │  │
│  │  Benefits untuk SATRIAMART:                          │  │
│  │  • Qualified leads (higher conversion)              │  │
│  │  • Larger projects (commercial, high-end)           │  │
│  │  • Steady pipeline                                  │  │
│  │  • Brand association (premium positioning)          │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Partnership Start:** Q2 2024
- **Active Partners:** 12 arsitek/designer
- **Projects via Partnership:** 28 projects (Aug 2024 - Aug 2025)
- **Revenue contribution:** Rp 180M (±15% dari total revenue)

**Partnership Model:**

**Tier 1: Preferred Partner (8 partners)**
- Min. 3 projects/tahun
- Discount: 10%
- Response time priority: <24 jam
- Dedicated account manager

**Tier 2: Registered Partner (4 partners)**
- 1-2 projects/tahun
- Discount: 5%
- Standard response time
- General support

**How Partnership Works:**

1. **Onboarding:**
   - Designer/arsitek register as partner
   - Receive partner kit (portfolio, pricing, samples)
   - Introduction meeting dengan SATRIAMART team

2. **Project Flow:**
   - Designer specify requirements (as part of their client project)
   - SATRIAMART provide quotation (partner pricing)
   - Designer present to end-client (with markup if desired)
   - Order placed through SATRIAMART
   - Production & installation coordinated

3. **Post-Project:**
   - Quality check dengan designer
   - Photo documentation (for both portfolios)
   - Referral commission paid (if applicable)
   - Feedback collection

**Success Stories:**

**Partner A - Interior Designer (High-end Residential)**
- **Projects:** 8 projects in 12 months
- **Value:** Rp 65M total
- **Feedback:** "SATRIAMART reliable, kualitas konsisten, tepat waktu. Client saya puas."

**Partner B - Arsitek (Commercial)**
- **Projects:** 5 projects (office, retail)
- **Value:** Rp 48M total
- **Feedback:** "Good collaboration, understand desain intent, execution bagus."

**Challenges in Partnership:**

1. **Communication:**
   - Designer expectation tinggi (detail, precision)
   - Need clear technical specs upfront
   - Revision process must be managed (cost implication)

2. **Timeline:**
   - Designer sering last minute (project delay on their end)
   - Need buffer untuk accommodate urgent requests
   - Coordination dengan construction schedule

3. **Pricing:**
   - Designer kadang expect lower price (trade pricing)
   - Need transparency on cost structure
   - Balance antara discount vs margin

**Expansion Opportunity:**

Current 12 partners generate ±15% revenue. Target:
- **2026:** 25 partners, 25% revenue
- **2027:** 40 partners, 35% revenue
- **2028:** 60+ partners, 40% revenue

**Action Plan (reference SO3 - Lampiran C.2):**
- Formal partnership program dengan T&C
- Partner portal (online quotation, order status)
- Quarterly partner meetup (networking, showcase new products)
- Co-marketing campaigns (designer feature SATRIAMART, vice versa)

---

### **FOTO F.4.4: Customer Testimonial & Social Proof**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Screenshots Reviews & Testimonials]          │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  CUSTOMER REVIEWS                                    │  │
│  │  ──────────────────────────────────────────────────  │  │
│  │                                                       │  │
│  │  ⭐⭐⭐⭐⭐ 4.8/5.0  (Based on 127 reviews)            │  │
│  │                                                       │  │
│  │  ──────────────────────────────────────────────────  │  │
│  │                                                       │  │
│  │  💬 "Pelayanan ramah, hasil memuaskan, harga        │  │
│  │      worth it. Pasti order lagi kalau ada project   │  │
│  │      lagi!" - Ibu Rina, Jakarta                     │  │
│  │      ⭐⭐⭐⭐⭐ | 2 weeks ago                          │  │
│  │                                                       │  │
│  │  💬 "Fast response, profesional, detail attention.  │  │
│  │      Logo kantor jadi standout. Recommended!"       │  │
│  │      - Pak Agus, Startup Founder                    │  │
│  │      ⭐⭐⭐⭐⭐ | 1 month ago                          │  │
│  │                                                       │  │
│  │  💬 "Kualitas oke, tapi delivery sempat delay 2     │  │
│  │      hari dari janji. Overall masih puas."          │  │
│  │      - Bu Siti, Tangerang                           │  │
│  │      ⭐⭐⭐⭐☆ | 3 weeks ago                          │  │
│  │                                                       │  │
│  │  💬 "Custom request bisa diakomodir dengan baik.    │  │
│  │      Designer paham maunya saya. Hasil perfect!"    │  │
│  │      - Pak Doni, Bekasi                             │  │
│  │      ⭐⭐⭐⭐⭐ | 1 week ago                           │  │
│  │                                                       │  │
│  │  [View all reviews]                                 │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Informasi:**
- **Review Sources:** Google, Instagram comments, WhatsApp feedback
- **Total Reviews:** 127 (Aug 2025)
- **Average Rating:** 4.8/5.0
- **Response Rate:** 100% (owner/team respond semua reviews)

**Review Breakdown:**

| Rating | Count | Percentage |
|--------|-------|------------|
| ⭐⭐⭐⭐⭐ (5 stars) | 98 | 77% |
| ⭐⭐⭐⭐☆ (4 stars) | 22 | 17% |
| ⭐⭐⭐☆☆ (3 stars) | 5 | 4% |
| ⭐⭐☆☆☆ (2 stars) | 2 | 2% |
| ⭐☆☆☆☆ (1 star) | 0 | 0% |

**Common Positive Themes:**
1. **Quality** (mentioned in 89% of 5-star reviews)
   - "Kualitas bagus", "rapih", "presisi", "finishing bagus"
2. **Service** (mentioned in 76%)
   - "Ramah", "helpful", "responsive", "patient dengan revisi"
3. **Value** (mentioned in 54%)
   - "Harga reasonable", "worth it", "sesuai budget"
4. **Design** (mentioned in 48%)
   - "Desain keren", "sesuai keinginan", "kreatif"

**Common Complaints (dari 3-4 star reviews):**
1. **Timeline** (mentioned in 65% of lower reviews)
   - Delay delivery 1-3 hari dari janji
   - Communication gap on progress update
2. **Pricing** (mentioned in 20%)
   - "Agak mahal" (expectation management issue)
3. **Minor Quality Issue** (mentioned in 15%)
   - Scratch kecil, perlu rework
   - LED tidak uniform (rare, tapi pernah terjadi)

**Response Strategy:**
- Owner personally respond ke semua reviews (positive & negative)
- Negative reviews: Acknowledge, apologize, offer solution
- Positive reviews: Thank, encourage share & refer
- **Result:** Customer appreciate responsiveness (builds trust)

**Net Promoter Score (NPS):**
- **Promoters** (9-10 rating): 78%
- **Passives** (7-8 rating): 18%
- **Detractors** (0-6 rating): 4%
- **NPS Score:** +74 (Excellent, industry benchmark: +30 to +50)

**Customer Retention:**
- **Repeat customer rate:** 28% (target: 40% by 2027)
- **Referral rate:** 35% (new customer dari referral)
- **Lifetime value (avg):** Rp 3.2M (2-3 projects over 2-3 years)

**Social Proof Impact:**
- 67% prospek mention "lihat review bagus" sebagai reason to inquiry
- Instagram showcase photos influence 82% purchasing decision
- Testimonial videos get 3x engagement vs product photos

**Leveraging Social Proof:**
- Feature testimonials di Instagram Story highlight
- Case study blog posts (with customer permission)
- Before-after transformation videos (viral potential)
- Customer photo repost (build community)

**Improvement from Feedback:**
- Timeline commitment more realistic (under-promise, over-deliver)
- Progress update automated (WhatsApp update every 2-3 hari)
- Quality check more rigorous (reduce rework)
- Packaging improved (reduce transit damage)

---

**RINGKASAN DOKUMENTASI F.4:**

**Portfolio Strength:**
- ✓ Diverse product range (residential to commercial)
- ✓ Strong testimonials & social proof (4.8/5 rating, NPS +74)
- ✓ Growing B2B presence (partnership dengan designers)
- ✓ High customer satisfaction & retention

**Key Success Factors:**
1. **Quality:** Consistent delivery of high-quality products
2. **Service:** Responsive, friendly, customer-centric approach
3. **Customization:** Flexibility to accommodate unique requirements
4. **Value:** Fair pricing, good quality-price ratio

**Growth Opportunities:**
1. **Expand B2B:** From 45% to 60% revenue (higher value, steadier pipeline)
2. **Partner Program:** Scale dari 12 to 60+ partners
3. **Product Line:** New categories (display, furniture, retail fixtures)
4. **Geographic:** Expand beyond Jabodetabek (regional branches)

**Competitive Advantages:**
- Strong brand reputation (social proof, word-of-mouth)
- Established relationships (repeat customers, partners)
- Digital presence (8K+ Instagram, 12K+ TikTok)
- Quality & service differentiation (vs low-cost competitors)

---

**DOKUMENTASI LAMPIRAN F - COMPLETE**

Total dokumentasi:
- **F.1:** Fasilitas (5 photos)
- **F.2:** Proses Produksi (5 photos)
- **F.3:** Sistem & Teknologi (5 photos)
- **F.4:** Portfolio & Kolaborasi (4 photos)

**Total:** 19 dokumentasi points dengan analisis mendalam

**Overall Assessment:**
SATRIAMART memiliki foundasi operasional yang solid dengan strengths di customer service, quality, dan digital marketing. Namun, ada significant opportunity untuk improvement di backend systems (ERP, CRM, automation) untuk support scaling dan long-term growth.

---

**Disiapkan oleh:** Tim Peneliti  
**Periode Dokumentasi:** Agustus 2025  
**Lokasi:** SATRIAMART Workshop, Depok  
**Metode:** Observasi langsung, interview, screenshot/photo documentation, data collection
