# LAMPIRAN G: DOKUMEN PENDUKUNG (Lanjutan)

## G.3 LEMBAR KERJA ANALISIS DATA

### Worksheet dan Perhitungan Detail untuk Analisis

---

### **WORKSHEET 3.1: Analisis Kapasitas Produksi**

**Tujuan:** Menghitung kapasitas teoritis vs aktual untuk identifikasi bottleneck

**Data Dasar:**

| Station | Equipment | Jam Kerja/Hari | Jam Efektif | Operator |
|---------|-----------|----------------|-------------|----------|
| Cutting | CNC Router | 8 jam | 7 jam (break excluded) | 1 |
| Cutting | Laser Cutter | 8 jam | 7 jam | 1 |
| Finishing | Manual Polishing | 8 jam | 7 jam | 2 |
| Assembly | Manual Assembly | 8 jam | 7 jam | 1 |
| QC | Visual Inspection | 8 jam | 7 jam | 1 (shared) |

---

**PERHITUNGAN KAPASITAS PER STATION:**

**A. CNC Router:**

Asumsi: Mix product (40% simple, 40% medium, 20% complex)

| Complexity | Time/Unit | Setup Time | Units/Hour | Daily Capacity | Mix % | Weighted Capacity |
|------------|-----------|------------|------------|----------------|-------|-------------------|
| Simple | 12 min | 10 min | 5.5 units | 38.5 units | 40% | 15.4 units |
| Medium | 18 min | 12 min | 4.0 units | 28.0 units | 40% | 11.2 units |
| Complex | 25 min | 15 min | 2.8 units | 19.6 units | 20% | 3.9 units |

**CNC Daily Capacity (Weighted Average): 30.5 units/hari**

---

**B. Laser Cutter:**

| Product Type | Time/Unit | Setup Time | Units/Hour | Daily Capacity | Utilization |
|--------------|-----------|------------|------------|----------------|-------------|
| Detail parts | 3-4 min avg | 5 min | 15 units | 105 units | 30-40% |
| Thin material cutting | 5-8 min avg | 5 min | 9 units | 63 units | - |

**Laser Cutter Capacity:** 60-100 units/hari (under-utilized, bukan bottleneck)

---

**C. Finishing (Manual Polishing):**

**Time Study Data (dari observasi):**

| Complexity | Time/Unit (avg) | Units/Hour/Person | Daily Capacity (2 persons) |
|------------|-----------------|-------------------|----------------------------|
| Simple | 25 min | 2.4 units | 33.6 units |
| Medium | 36 min | 1.7 units | 23.8 units |
| Complex | 50 min | 1.2 units | 16.8 units |

**Weighted Average (40/40/20 mix):**
- Simple: 33.6 × 40% = 13.4
- Medium: 23.8 × 40% = 9.5
- Complex: 16.8 × 20% = 3.4
- **Total: 26.3 units/hari**

**Finishing Daily Capacity: ~26 units/hari** ⚠️ **BOTTLENECK CONFIRMED**

---

**D. Assembly:**

| Type | Time/Unit | Units/Hour | Daily Capacity (1 person) |
|------|-----------|------------|---------------------------|
| Simple (no LED) | 15 min | 4 units | 28 units |
| Medium (multi-layer) | 35 min | 1.7 units | 12 units |
| Complex (LED) | 75 min | 0.8 units | 5.6 units |

**Weighted Average (50/30/20 mix):**
- Simple: 28 × 50% = 14.0
- Medium: 12 × 30% = 3.6
- Complex: 5.6 × 20% = 1.1
- **Total: 18.7 units/hari**

**Assembly Capacity: ~19 units/hari** (potential bottleneck untuk complex products)

---

**E. Quality Control:**

Time per unit: 5-10 menit (average 7 menit)
- Capacity: 60 units/hari
- **Bukan bottleneck**

---

**BOTTLENECK ANALYSIS SUMMARY:**

```
┌────────────────────────────────────────────────────────────┐
│  CAPACITY ANALYSIS - THEORY OF CONSTRAINTS                │
│  ────────────────────────────────────────────────────────  │
│                                                             │
│  Station          Capacity      Status                     │
│  ─────────────────────────────────────────────────────     │
│  CNC Router       30.5 u/day    Non-constraint             │
│  Laser Cutter     60+ u/day     Non-constraint (under-ut.) │
│  ⚠ FINISHING      26 u/day      PRIMARY BOTTLENECK ⚠       │
│  Assembly         19 u/day      Secondary constraint       │
│  QC               60 u/day      Non-constraint             │
│                                                             │
│  Overall System Capacity: 19-26 units/day                  │
│  (Limited by Finishing → Assembly sequence)                │
└────────────────────────────────────────────────────────────┘
```

**Capacity Utilization:**
- **CNC:** 26/30.5 = 85% (limited by downstream bottleneck)
- **Laser:** 15-20 units typical / 60+ capacity = 25-33% (highly under-utilized)
- **Finishing:** 100% (always backlog)
- **Assembly:** 90-95% (high utilization, potential issue with complex products)

**Impact of Bottleneck:**
- **Lost revenue potential:** 
  - Potential capacity (if no bottleneck): 30 units/day
  - Actual capacity: 26 units/day
  - Lost: 4 units/day = 80 units/month = 960 units/year
  - Revenue @ Rp 500K average = **Rp 480 juta/tahun lost opportunity**

**Recommended Actions:**
1. **Urgent:** Add finishing capacity (automation atau additional headcount)
2. **High:** Optimize finishing process (reduce time per unit)
3. **Medium:** Add assembly capacity (jika scale up finishing)
4. **Low:** Find more utilization untuk laser cutter (expand product line)

---

### **WORKSHEET 3.2: Analisis Finansial - Break Even & Profitability**

**Tujuan:** Menghitung break-even point dan target volume untuk profitability

**FIXED COSTS (Monthly):**

| Item | Amount (Rp) |
|------|-------------|
| Rent (workshop + office) | 15,000,000 |
| Salaries (5 production + 2 admin) | 35,000,000 |
| Utilities (listrik, air, internet) | 3,500,000 |
| Equipment depreciation | 5,000,000 |
| Insurance | 1,500,000 |
| Marketing & advertising | 2,000,000 |
| Admin & office supplies | 1,000,000 |
| Maintenance reserve | 2,000,000 |
| **TOTAL FIXED COSTS** | **65,000,000** |

---

**VARIABLE COSTS (Per Unit - Average):**

| Item | Amount (Rp) |
|------|-------------|
| Material (acrylic, LED, mounting) | 150,000 |
| Consumables (bit, sanding paper, glue) | 15,000 |
| Packaging | 5,000 |
| Delivery/shipping (average) | 20,000 |
| **TOTAL VARIABLE COST** | **190,000** |

---

**REVENUE (Per Unit - Average):**

Weighted average selling price (mix residential & commercial):
- Residential: Rp 450,000 (70% volume)
- Commercial: Rp 800,000 (30% volume)
- **Weighted Average: Rp 555,000**

---

**CONTRIBUTION MARGIN:**

```
Selling Price:           Rp 555,000
Variable Cost:           Rp 190,000
─────────────────────────────────────
Contribution Margin:     Rp 365,000
Contribution Margin %:   65.8%
```

---

**BREAK-EVEN ANALYSIS:**

**Break-Even Point (BEP) in Units:**
```
BEP = Fixed Costs / Contribution Margin per Unit
BEP = Rp 65,000,000 / Rp 365,000
BEP = 178 units/month
BEP = 178 / 22 hari kerja = 8.1 units/day
```

**Break-Even Point (BEP) in Revenue:**
```
BEP Revenue = 178 units × Rp 555,000
BEP Revenue = Rp 98,790,000/month
```

---

**CURRENT PERFORMANCE (Estimated):**

Actual production: ~25 units/day × 22 days = 550 units/month
Actual revenue: 550 × Rp 555,000 = Rp 305,250,000/month

**Profitability:**
```
Revenue:                 Rp 305,250,000
Variable Costs:          Rp 104,500,000 (550 × 190K)
─────────────────────────────────────────────────
Contribution Margin:     Rp 200,750,000
Fixed Costs:             Rp  65,000,000
─────────────────────────────────────────────────
Operating Profit:        Rp 135,750,000
Operating Margin:        44.5%
```

**Safety Margin:**
```
Safety Margin = (Actual Sales - BEP Sales) / Actual Sales
Safety Margin = (550 - 178) / 550
Safety Margin = 67.6%
```

**Interpretation:** 
- ✓ SATRIAMART well above break-even (178 vs 550 units)
- ✓ Healthy operating margin (44.5%)
- ✓ Good safety margin (67.6% - sales bisa turun 67% baru rugi)
- ⚠ Tapi revenue terbatas oleh capacity constraint (max 26 units/day)

---

**TARGET SCENARIOS:**

| Scenario | Units/Day | Units/Month | Revenue/Month | Operating Profit | Margin % |
|----------|-----------|-------------|---------------|------------------|----------|
| Current | 25 | 550 | 305M | 136M | 44.5% |
| Target 2026 | 35 | 770 | 427M | 216M | 50.6% |
| Target 2027 | 45 | 990 | 549M | 297M | 54.1% |
| Stretch Goal | 60 | 1,320 | 733M | 417M | 56.9% |

**Note:** Increasing volume improve margin % karena fixed costs di-spread across more units (operating leverage effect).

---

### **WORKSHEET 3.3: Analisis Customer Segmentation & Lifetime Value**

**Tujuan:** Segment customers dan hitung Customer Lifetime Value (CLV)

**DATA CUSTOMER (Sample 120 customers, last 12 months):**

---

**A. SEGMENTATION BY TYPE:**

| Segment | Count | % | Avg Order Value | Frequency | Annual Revenue |
|---------|-------|---|-----------------|-----------|----------------|
| Residential - One-time | 56 | 46.7% | Rp 450K | 1.0x | Rp 25.2M |
| Residential - Repeat | 34 | 28.3% | Rp 480K | 2.3x | Rp 37.6M |
| Commercial - SME | 22 | 18.3% | Rp 2.5M | 1.5x | Rp 82.5M |
| Commercial - Corporate | 8 | 6.7% | Rp 8.0M | 2.0x | Rp 128M |
| **TOTAL** | **120** | **100%** | **Rp 2.3M** | **1.7x** | **Rp 273.3M** |

---

**B. CUSTOMER LIFETIME VALUE (CLV) CALCULATION:**

**Assumptions:**
- Average customer lifespan: 3 tahun
- Discount rate: 10% annually
- Retention rate by segment (based on historical data)

**CLV Formula:**
```
CLV = (Average Order Value × Purchase Frequency × Customer Lifespan) / (1 + Discount Rate)^Year
```

**CLV by Segment:**

**1. Residential - One-time:**
```
AOV: Rp 450,000
Frequency: 1.0x/year
Lifespan: 1 year (one-time customer)
Retention: 0% (by definition)

CLV = 450,000 × 1.0 × 1 = Rp 450,000
```

**2. Residential - Repeat:**
```
AOV: Rp 480,000
Frequency: 2.3x/year
Lifespan: 3 years
Retention: 70% year-over-year

Year 1: 480K × 2.3 = 1,104,000
Year 2: 480K × 2.3 × 0.7 / 1.1 = 705,600
Year 3: 480K × 2.3 × 0.7² / 1.1² = 448,000

CLV = 1,104,000 + 705,600 + 448,000 = Rp 2,257,600
```

**3. Commercial - SME:**
```
AOV: Rp 2,500,000
Frequency: 1.5x/year
Lifespan: 3 years
Retention: 80%

Year 1: 2,500K × 1.5 = 3,750,000
Year 2: 2,500K × 1.5 × 0.8 / 1.1 = 2,727,273
Year 3: 2,500K × 1.5 × 0.8² / 1.1² = 1,983,471

CLV = 3,750,000 + 2,727,273 + 1,983,471 = Rp 8,460,744
```

**4. Commercial - Corporate:**
```
AOV: Rp 8,000,000
Frequency: 2.0x/year
Lifespan: 5 years (longer relationship)
Retention: 90%

Year 1: 8,000K × 2.0 = 16,000,000
Year 2: 8,000K × 2.0 × 0.9 / 1.1 = 13,090,909
Year 3: 8,000K × 2.0 × 0.9² / 1.1² = 10,744,628
Year 4: 8,000K × 2.0 × 0.9³ / 1.1³ = 8,842,410
Year 5: 8,000K × 2.0 × 0.9⁴ / 1.1⁴ = 7,284,868

CLV = Rp 55,962,815
```

---

**CLV SUMMARY:**

| Segment | CLV | % of Total Value | Strategic Priority |
|---------|-----|------------------|--------------------|
| Residential - One-time | Rp 450K | Low | **Retain** (convert to repeat) |
| Residential - Repeat | Rp 2.3M | Medium | **Grow** (increase frequency) |
| Commercial - SME | Rp 8.5M | High | **Expand** (more SME partnerships) |
| Commercial - Corporate | Rp 56M | Very High | **Protect** (premium service) |

---

**INSIGHTS & STRATEGY:**

**1. Focus on Commercial Segment:**
- Corporate customers memiliki CLV 124× lebih tinggi dari residential one-time
- SME customers CLV 19× lebih tinggi
- **Action:** Alokasi resources lebih banyak untuk B2B acquisition & retention

**2. Convert One-time to Repeat:**
- 46.7% customers adalah one-time (low CLV)
- **Opportunity:** Jika bisa convert 50% dari one-time menjadi repeat:
  - 28 customers × Rp 1.8M additional CLV = **Rp 50.4M additional lifetime revenue**
- **Action:** Follow-up program, loyalty incentive, reminder campaigns

**3. Increase Frequency:**
- Residential repeat: 2.3× per year (could be 3-4×)
- Commercial SME: 1.5× per year (could be 2-3×)
- **Action:** Upselling, new product introduction, seasonal campaigns

**4. Customer Acquisition Cost (CAC) Benchmark:**

| Segment | CLV | Target CAC | Max CAC (30% rule) |
|---------|-----|------------|--------------------|
| Residential - One-time | Rp 450K | Rp 50K | Rp 135K |
| Residential - Repeat | Rp 2.3M | Rp 200K | Rp 690K |
| Commercial - SME | Rp 8.5M | Rp 800K | Rp 2.6M |
| Commercial - Corporate | Rp 56M | Rp 5M | Rp 17M |

**Current CAC (estimated via organic channels):** ~Rp 30-50K (very low, mostly organic)

**Implication:** 
- Significant room untuk invest in paid marketing/sales
- Could spend up to Rp 2.6M untuk acquire SME customer dan still profitable
- Could spend up to Rp 17M untuk acquire corporate customer (e.g., sales team salary, BD costs)

---

### **WORKSHEET 3.4: Digital Marketing Performance Metrics**

**Tujuan:** Analisis ROI dari digital marketing channels

**DATA PERIOD:** Juli 2024 - Juni 2025 (12 bulan)

---

**A. INSTAGRAM PERFORMANCE:**

**Growth Metrics:**
- Followers start: 6,200
- Followers end: 8,500
- Growth: +2,300 (+37.1%)
- Avg growth rate: 192 followers/month

**Engagement Metrics (12-month average):**
- Posts per month: 20
- Avg reach per post: 1,200
- Avg engagement rate: 2.8%
- Story views: 900-1,200 per story
- DM inquiries: 50-60 per month

**Lead Generation:**
- Total inquiries from Instagram: 680
- Conversion to quotation: 65%
- Conversion to deal: 28%
- **Total deals from Instagram: 190 deals**

**Revenue Generated:**
- 190 deals × Rp 480K avg (residential weighted) = **Rp 91.2M**

**Investment:**
- Paid ads: Rp 0 (organic only)
- Time investment: 10 jam/minggu × 4.3 minggu × 12 bulan = 516 jam
- Cost of time (@ Rp 50K/jam equivalent): Rp 25.8M

**ROI:**
```
Revenue:            Rp 91.2M
Investment:         Rp 25.8M
Profit:             Rp 65.4M
ROI:                253%
```

---

**B. TIKTOK PERFORMANCE:**

**Growth Metrics:**
- Followers start: 8,100
- Followers end: 12,300
- Growth: +4,200 (+51.9%)
- Viral posts: 8 videos >100K views

**Engagement Metrics:**
- Videos posted: 89 (12 months)
- Avg views per video: 8,500
- Total views: 756,500
- Avg engagement rate: 4.2%
- Comment/share rate: Higher than Instagram

**Lead Generation:**
- Total inquiries from TikTok: 520
- Conversion to deal: 32% (higher than Instagram!)
- **Total deals from TikTok: 166 deals**

**Revenue Generated:**
- 166 deals × Rp 500K avg = **Rp 83M**

**Investment:**
- Paid ads: Rp 0 (organic)
- Time investment: 8 jam/minggu × 4.3 × 12 = 413 jam
- Cost: Rp 20.6M

**ROI:**
```
Revenue:            Rp 83M
Investment:         Rp 20.6M
Profit:             Rp 62.4M
ROI:                303%
```

**Note:** TikTok ROI lebih tinggi karena:
- Time investment lebih efficient (short-form video)
- Viral potential lebih tinggi (algorithm favors engaging content)
- Audience lebih impulse buyer (faster decision)

---

**C. GOOGLE SEARCH (Organic):**

**Traffic Metrics:**
- Website visits from Google: 1,200 (avg 100/month)
- Search impressions: 45,000
- Avg position: 8-12 (page 1-2)
- Click-through rate: 2.7%

**Lead Generation:**
- Inquiries from Google: 48
- Conversion: 25%
- **Deals from Google: 12 deals**

**Revenue Generated:**
- 12 deals × Rp 2.2M avg (Google traffic lebih high-intent, commercial) = **Rp 26.4M**

**Investment:**
- SEO: Minimal (no dedicated SEO effort)
- Website maintenance: Rp 500K/year
- Time: Negligible

**ROI:**
```
Revenue:            Rp 26.4M
Investment:         Rp 0.5M
Profit:             Rp 25.9M
ROI:                5,180%
```

**Opportunity:** 
- Huge untapped potential dengan SEO optimization
- Could 10× traffic dengan proper SEO strategy
- Investment Rp 10-20M/year untuk SEO could generate Rp 200-300M additional revenue

---

**D. REFERRAL / WORD-OF-MOUTH:**

**Lead Generation:**
- Inquiries from referral: 280
- Conversion: 45% (highest conversion - warm leads)
- **Deals from referral: 126 deals**

**Revenue Generated:**
- 126 deals × Rp 550K avg = **Rp 69.3M**

**Investment:**
- Referral incentive: Rp 3.5M (occasional discount untuk referrer)

**ROI:**
```
Revenue:            Rp 69.3M
Investment:         Rp 3.5M
Profit:             Rp 65.8M
ROI:                1,880%
```

**Opportunity:**
- Formalize referral program (10% discount atau Rp 50K voucher per referral)
- Could 2× referral volume dengan structured program

---

**CHANNEL PERFORMANCE SUMMARY:**

| Channel | Deals | Revenue | Investment | ROI | Priority |
|---------|-------|---------|------------|-----|----------|
| Instagram | 190 | Rp 91.2M | Rp 25.8M | 253% | **Maintain** |
| TikTok | 166 | Rp 83M | Rp 20.6M | 303% | **Grow** |
| Google Search | 12 | Rp 26.4M | Rp 0.5M | 5,180% | **Invest** ⭐ |
| Referral | 126 | Rp 69.3M | Rp 3.5M | 1,880% | **Formalize** ⭐ |
| Others | 56 | Rp 30M | Rp 5M | 500% | Monitor |
| **TOTAL** | **550** | **Rp 299.9M** | **Rp 55.4M** | **441%** | - |

**Strategic Recommendations:**

1. **Google Search (SEO):** Invest Rp 15M/year → Potential Rp 200M+ revenue (1,233% ROI projected)
2. **Referral Program:** Invest Rp 10M/year → Potential 2× referrals = Rp 70M additional (600% ROI)
3. **TikTok Ads:** Experiment Rp 5M/month → Could 2× reach & deals (target 300% ROI)
4. **Instagram Ads:** Test Rp 3M/month → Retargeting & lookalike audiences
5. **Partnership Marketing:** Arsitek/designer collaboration (low cost, high impact)

---

## G.4 STUDI BENCHMARKING DENGAN KOMPETITOR

### Comparative Analysis: SATRIAMART vs Kompetitor

---

### **BENCHMARKING FRAMEWORK**

**Kompetitor yang Dipilih untuk Benchmarking:**
1. **Kompetitor A:** Large established player (Jakarta Pusat, 10 tahun operasi)
2. **Kompetitor B:** Similar scale UMKM (Tangerang, 3 tahun operasi)
3. **Kompetitor C:** Low-cost provider (Online-based, 2 tahun operasi)
4. **SATRIAMART:** Subject (Depok, 4 tahun operasi)

**Metode Data Collection:**
- Mystery shopping (order quotation, analyze response)
- Website/social media analysis
- Customer review analysis (Google, Instagram)
- Industry report reference
- Interview dengan ex-employee kompetitor (jika available)

---

### **DIMENSI 1: PRODUCT & SERVICE OFFERING**

| Aspect | SATRIAMART | Kompetitor A | Kompetitor B | Kompetitor C |
|--------|------------|--------------|--------------|--------------|
| **Product Range** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| - Residential | ✓ Strong | ✓ Available | ✓ Strong | ✓ Focus |
| - Commercial | ✓ Growing | ✓ Established | ✓ Limited | ✗ Minimal |
| - Custom Design | ✓ Excellent | ✓ Good | ✓ Good | ✗ Template only |
| **Material Quality** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| - Acrylic grade | Premium (Mitsubishi) | Premium (mix) | Standard | Economy |
| - LED quality | Good (branded) | Excellent | Good | Budget |
| **Customization** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ |
| - Design flexibility | Very high | Medium | High | Very low |
| - Size options | Any size | Standard + custom | Any size | Fixed sizes |
| **Installation Service** | ✓ Available | ✓ Professional team | ✓ Available | ✗ Self-install |

**Key Findings:**
- ✓ SATRIAMART competitive di customization (differentiator)
- ⚠ Kompetitor A lebih complete product range (more categories)
- ✓ SATRIAMART quality level setara dengan pemain established
- ✓ Clear differentiation vs low-cost kompetitor C

---

### **DIMENSI 2: PRICING STRATEGY**

**Product Comparison (Same Spec: Nomor Rumah 30cm, LED Warm White):**

| Provider | Price | Payment Terms | Delivery | Total Cost | Value Score |
|----------|-------|---------------|----------|------------|-------------|
| SATRIAMART | Rp 350K | DP 50% | Rp 50K | **Rp 400K** | ⭐⭐⭐⭐ |
| Kompetitor A | Rp 420K | DP 30% | Rp 70K | **Rp 490K** | ⭐⭐⭐ |
| Kompetitor B | Rp 330K | DP 50% | Rp 50K | **Rp 380K** | ⭐⭐⭐⭐ |
| Kompetitor C | Rp 250K | Full payment | Rp 80K | **Rp 330K** | ⭐⭐ |

**Analysis:**
- SATRIAMART positioned di middle-high segment (bukan termurah, bukan termahal)
- Price premium 6% vs Kompetitor B (justified dengan better service & customization)
- Price 18% lower vs Kompetitor A (established brand premium)
- Price 21% higher vs Kompetitor C (quality & service differential)

**Pricing Strategy Assessment:**
- ✓ **SATRIAMART: Value-for-money positioning** (sweet spot)
- Kompetitor A: Premium pricing (brand equity)
- Kompetitor B: Competitive pricing (similar strategy)
- Kompetitor C: Budget pricing (volume game)

---

### **DIMENSI 3: DIGITAL PRESENCE & MARKETING**

| Metric | SATRIAMART | Kompetitor A | Kompetitor B | Kompetitor C |
|--------|------------|--------------|--------------|--------------|
| **Website** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| - Professional design | Basic | Excellent | Good | Good |
| - E-commerce | ✗ | ✓ Full | ✗ | ✓ Basic |
| - Online quotation | ✗ | ✓ | ✗ | ✓ |
| **Instagram** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| - Followers | 8.5K | 25K | 4.2K | 45K |
| - Engagement rate | 2.8% | 1.5% | 3.2% | 5.8% |
| - Post frequency | 5×/week | Daily | 3×/week | Daily |
| **TikTok** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| - Followers | 12.3K | 3K | 2.5K | 68K |
| - Viral content | 8 posts >100K | 0 | 2 posts | 20+ posts |
| **Google Presence** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| - GMB reviews | 28 (4.8★) | 180 (4.5★) | 15 (4.9★) | 95 (4.2★) |
| - SEO ranking | Page 2 | Page 1 (top 3) | Page 3 | Page 1 (#5-8) |
| **Paid Ads** | ✗ None | ✓ Active | ✗ None | ✓ Heavy |

**Key Findings:**

**Strengths:**
- ✓ SATRIAMART excellent di TikTok (viral content, engagement)
- ✓ Instagram engagement rate competitive (above Kompetitor A)
- ✓ Organic reach strategy working well

**Weaknesses:**
- ⚠ Website basic (bukan e-commerce, no online quotation)
- ⚠ Google SEO weak (page 2, low traffic)
- ⚠ GMB reviews count low (28 vs 180 kompetitor A)
- ⚠ No paid advertising (missed opportunity)

**Competitive Position:**
- **Digital Marketing:** SATRIAMART di ranking #2 (after Kompetitor C yang pure online player)
- **E-commerce Readiness:** Ranking #4 (all others have better online infrastructure)

**Gap Analysis:**
- **High Priority:** Website upgrade + e-commerce
- **High Priority:** SEO optimization (Google ranking)
- **Medium Priority:** Paid ads experimentation
- **Low Priority:** Increase GMB reviews (encourage customers)

---

### **DIMENSI 4: OPERATIONS & CAPACITY**

| Aspect | SATRIAMART | Kompetitor A | Kompetitor B | Kompetitor C |
|--------|------------|--------------|--------------|--------------|
| **Production Capacity** | 25-30 u/day | 100+ u/day | 20-25 u/day | 40-50 u/day |
| **Lead Time** | 5-7 hari | 7-10 hari | 5-7 hari | 3-5 hari |
| **Equipment** | 1 CNC, 1 Laser | 3 CNC, 2 Laser | 1 CNC, 1 Laser | 2 CNC (outsource polish) |
| **Automation Level** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Team Size** | 7 people | 25+ people | 6 people | 12 people |
| **Quality System** | Manual QC | ISO 9001 | Manual QC | Basic QC |
| **First-Pass Yield** | 87% | 92% | 85% | 80% |

**Key Findings:**

**Strengths:**
- ✓ Lead time competitive (5-7 hari vs 7-10 hari kompetitor A)
- ✓ Quality level good (87% FPY, above Kompetitor B & C)

**Weaknesses:**
- ⚠ Capacity significantly lower vs Kompetitor A (25% of their capacity)
- ⚠ Automation level low (bottleneck di manual finishing)
- ⚠ No formal quality system (vs ISO 9001 kompetitor A)
- ⚠ Team size kecil (scalability constraint)

**Competitive Position:**
- **Operations Excellence:** Ranking #3 (Kompetitor A best-in-class)
- **Capacity:** Ranking #3 (C > SATRIAMART > B)
- **Quality:** Ranking #2 (A > SATRIAMART > B > C)

**Strategic Implications:**
- Need capacity expansion untuk compete dengan A & C
- Automation investment critical untuk scaling
- Quality system certification bisa jadi differentiator untuk B2B

---

### **DIMENSI 5: CUSTOMER SERVICE & EXPERIENCE**

| Metric | SATRIAMART | Kompetitor A | Kompetitor B | Kompetitor C |
|--------|------------|--------------|--------------|--------------|
| **Response Time** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| - Avg response (inquiry) | 21 min | 2-3 jam | 10 min | 30 min |
| **Quotation Time** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| - Simple product | 15-20 min | Instant (auto) | 15-20 min | Instant (online) |
| - Custom product | 45-60 min | 30 min | 40-50 min | N/A |
| **Order Tracking** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| - Self-service portal | ✗ | ✓ Real-time | ✗ | ✓ Basic |
| - Proactive update | Manual (WA) | Automated | Manual (WA) | Automated email |
| **Customer Satisfaction** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| - Review rating | 4.8/5 | 4.5/5 | 4.9/5 | 4.2/5 |
| - NPS score | +74 | +45 | +68 | +30 |
| **After-Sales** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| - Warranty | 6 months | 12 months | 6 months | 3 months |
| - Responsiveness | Excellent | Good | Excellent | Poor |

**Key Findings:**

**Strengths:**
- ✓ **Customer satisfaction highest tier** (4.8 rating, NPS +74)
- ✓ Response time excellent (21 min avg)
- ✓ Personal touch dan relationship building strong

**Weaknesses:**
- ⚠ No self-service portal (customers want independence)
- ⚠ Manual quotation slow untuk simple products (vs instant kompetitor)
- ⚠ Shorter warranty vs Kompetitor A (6 vs 12 months)

**Competitive Position:**
- **Customer Service:** Ranking #1 (personal touch + responsiveness)
- **Digital CX:** Ranking #4 (no self-service capabilities)

**Gap Analysis:**
- Customer portal untuk order tracking (Kompetitor A & C already have)
- Automated quotation untuk standard products
- Consider 12-month warranty untuk premium positioning

---

### **DIMENSI 6: BUSINESS MODEL & STRATEGY**

| Aspect | SATRIAMART | Kompetitor A | Kompetitor B | Kompetitor C |
|--------|------------|--------------|--------------|--------------|
| **Target Market** | Residential + B2B | B2B focus | Residential focus | Pure B2C online |
| **Value Proposition** | Custom + Service | Premium + Reliability | Affordable + Local | Cheap + Fast |
| **Revenue Model** | Project-based | Contract + Project | Project-based | Volume (e-comm) |
| **Growth Strategy** | Organic + Partners | M&A + Expansion | Organic | Paid ads + SEO |
| **Competitive Advantage** | Customization | Brand + Scale | Local + Nimble | Price + Convenience |
| **Scalability** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |

---

### **SWOT COMPARISON MATRIX**

**SATRIAMART vs Competition:**

| Category | SATRIAMART Position | Kompetitor Best Practice | Gap |
|----------|---------------------|--------------------------|-----|
| **Product Quality** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ (Kompetitor A) | Minimal gap |
| **Customization** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ (SATRIAMART) | **Leader** ✓ |
| **Pricing** | ⭐⭐⭐⭐ | Competitive | Good position |
| **Digital Marketing** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ (Kompetitor C) | Medium gap |
| **E-commerce** | ⭐ | ⭐⭐⭐⭐⭐ (Kompetitor A/C) | **Large gap** ⚠ |
| **Production Capacity** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ (Kompetitor A) | Large gap |
| **Customer Service** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ (SATRIAMART) | **Leader** ✓ |
| **Operations Tech** | ⭐⭐ | ⭐⭐⭐⭐ (Kompetitor A) | **Large gap** ⚠ |
| **Brand Recognition** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ (Kompetitor A) | Medium gap |

---

### **BENCHMARKING INSIGHTS & STRATEGIC RECOMMENDATIONS**

**1. Defend Strengths:**
- ✓ **Customization excellence:** Maintain design flexibility & creative capability
- ✓ **Customer service:** Continue personal touch, responsiveness (competitive advantage)
- ✓ **TikTok mastery:** Leverage viral content strategy for brand awareness

**2. Address Critical Gaps:**
- ⚠ **E-commerce infrastructure:** Invest in website + online quotation + customer portal
- ⚠ **Production capacity:** Solve finishing bottleneck, add equipment
- ⚠ **Operations technology:** ERP/CRM implementation (learn from Kompetitor A)
- ⚠ **SEO:** Improve Google ranking (low-hanging fruit with high ROI)

**3. Exploit Opportunities:**
- 🎯 **B2B segment:** SATRIAMART positioned between B (too small) and A (too expensive)
- 🎯 **Partnership model:** Arsitek/designer collaboration (unique model vs kompetitor)
- 🎯 **Content marketing:** Leverage TikTok success to build brand (vs traditional ads)

**4. Competitive Positioning:**

```
┌────────────────────────────────────────────────────────────┐
│  COMPETITIVE POSITIONING MAP                               │
│                                                             │
│  High Price                                                │
│      │                                                      │
│      │         [Kompetitor A]                              │
│      │         Premium+Scale                               │
│      │                                                      │
│      │                                                      │
│      │    [SATRIAMART]     [Kompetitor B]                 │
│      │    Custom+Service    Local+Nimble                   │
│      │                                                      │
│      │                                                      │
│      │                          [Kompetitor C]             │
│      │                          Volume+Online              │
│      │                                                      │
│  Low Price                                                 │
│      └────────────────────────────────────────────────────│
│        Low Service/Tech         High Service/Tech          │
└────────────────────────────────────────────────────────────┘
```

**SATRIAMART Strategic Direction:**
- **Current:** Middle-price, Medium-high service
- **Target (2027):** Medium-high price, High service+tech
- **Move:** ➡️ (Right - improve technology & systems while maintaining service excellence)

---

**BENCHMARKING SCORECARD SUMMARY:**

| Dimension | Weight | SATRIAMART | Komp A | Komp B | Komp C |
|-----------|--------|------------|--------|--------|--------|
| Product & Service | 20% | 80 | 90 | 75 | 60 |
| Pricing & Value | 15% | 85 | 75 | 85 | 70 |
| Digital Presence | 20% | 70 | 95 | 60 | 90 |
| Operations | 20% | 65 | 95 | 65 | 75 |
| Customer Experience | 15% | 95 | 80 | 90 | 65 |
| Business Model | 10% | 75 | 95 | 70 | 80 |
| **TOTAL SCORE** | **100%** | **76.5** | **89.0** | **72.5** | **73.5** |

**Ranking:** Kompetitor A (89) > **SATRIAMART (76.5)** > Kompetitor C (73.5) > Kompetitor B (72.5)

**Gap to #1:** 12.5 points (primarily in Digital Presence & Operations)

**Achievable Target (2026):** 82-85 points dengan focus pada:
- Digital infrastructure (+8 points)
- Operational technology (+5 points)
- Maintain/improve customer experience (+2 points)

---

**CONCLUSION:**

SATRIAMART positioned well dalam competitive landscape dengan clear differentiators (customization, service). Namun, untuk sustainable growth dan competitiveness, critical gaps dalam digital infrastructure dan operational technology harus addressed. Rekomendasi strategis align dengan findings dari benchmarking ini, fokus pada digitalisasi backend, e-commerce enablement, dan capacity expansion.

---

*[LAMPIRAN G - COMPLETE]*

**Total Dokumentasi Lampiran G:**
- **Part 1:** G.1 Wawancara (3 interviews) + G.2 Observasi (2 observations) = ~1,400 lines
- **Part 2:** G.3 Analisis Data (4 worksheets) + G.4 Benchmarking (6 dimensions) = ~1,500 lines

**GRAND TOTAL SEMUA LAMPIRAN (A-G):**
- Lampiran A: Flowchart (~1,500 lines)
- Lampiran B: Template (~1,200 lines)
- Lampiran C: SWOT (~1,400 lines)
- Lampiran D: Roadmap (~1,300 lines)
- Lampiran E: Finansial (~1,200 lines)
- Lampiran F: Foto Dokumentasi (~2,800 lines - 3 parts)
- Lampiran G: Dokumen Pendukung (~2,900 lines - 2 parts)

**TOTAL: ~12,300 lines dokumentasi komprehensif**

---

**Disiapkan oleh:** Tim Peneliti  
**Periode:** Juli - Agustus 2025  
**Metode:** Mixed-method research (interview, observation, benchmarking, data analysis)  
**Validasi:** Cross-checked dengan stakeholder SATRIAMART
