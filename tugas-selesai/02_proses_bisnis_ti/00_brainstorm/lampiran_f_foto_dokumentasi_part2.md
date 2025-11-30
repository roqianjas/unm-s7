# LAMPIRAN F: FOTO DOKUMENTASI (Lanjutan)

## F.2 Dokumentasi Proses Produksi

### Observasi Detail Setiap Tahap Produksi

---

### **FOTO F.2.1: Area Cutting - Mesin CNC Router**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Foto CNC Router dalam Operasi]               │
│                                                             │
│   ╔═══════════════════════════════════════════╗             │
│   ║  CNC ROUTER MACHINE                       ║             │
│   ║  ┌─────────────────────────────────────┐  ║             │
│   ║  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │  ║             │
│   ║  │  ▓  ACRYLIC SHEET (being cut)  ▓   │  ║             │
│   ║  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │  ║             │
│   ║  │                                     │  ║             │
│   ║  │       ↓                             │  ║             │
│   ║  │      [ROUTER BIT]                   │  ║             │
│   ║  │       Spindle: 24,000 RPM           │  ║             │
│   ║  └─────────────────────────────────────┘  ║             │
│   ║                                           ║             │
│   ║  Control Panel: [PC + Software]           ║             │
│   ╚═══════════════════════════════════════════╝             │
│                                                             │
│   Operator: Mengawasi proses cutting                       │
│   Vacuum system: ON (hisap chip/debris)                    │
└─────────────────────────────────────────────────────────────┘
```

**Informasi Foto:**
- **Tanggal Dokumentasi:** 16 Agustus 2025
- **Waktu:** 10:00 WIB (Proses produksi aktif)
- **Operator:** 1 orang (certified CNC operator)

**Spesifikasi Mesin CNC Router:**
- **Brand/Model:** [Generic CNC Router]
- **Working Area:** 1300mm x 2500mm
- **Spindle Power:** 3.5 kW
- **Max RPM:** 24,000
- **Positioning Accuracy:** ±0.05mm
- **Control System:** DSP/Mach3
- **Bit Types:** End mill, V-bit, ball nose (various sizes)

**Deskripsi Proses:**
CNC Router digunakan untuk cutting akrilik dengan presisi tinggi. Proses:
1. File G-code di-load ke control system
2. Material akrilik di-clamp pada bed
3. Operator set zero point dan tool height
4. Running program dengan monitoring terus-menerus
5. Vacuum system aktif untuk sedot chip dan debu

**Material yang Dikerjakan:**
- Akrilik 3mm - 15mm thickness
- Maximum sheet size: 1220mm x 2440mm
- Cutting speed: 2-8 meter/menit (tergantung thickness)
- Typical job time: 15-45 menit per piece

**Observasi Kunci:**
- ✓ Akurasi cutting sangat baik (sesuai desain ±0.1mm)
- ✓ Surface finish smooth, minimal post-processing
- ✓ Operator terlatih dan berpengalaman (5+ tahun)
- ✓ Vacuum system efektif, area bersih dari chip
- ⚠ Single machine = bottleneck (jika breakdown, produksi stop)
- ⚠ Setup time 10-15 menit per job (manual clamping)
- ⚠ No automated tool changer (manual tool change)
- ⚠ Maintenance schedule manual (belum preventive)

**Kapasitas Produksi:**
- **Effective working time:** 8 jam/hari (1 shift)
- **Utilization rate:** 70-80% (downtime untuk setup, maintenance)
- **Output:** 8-12 pieces/hari (complex design), 15-20 pieces/hari (simple)
- **Capacity constraint:** Ya, menjadi bottleneck saat high demand

**Issue yang Diamati:**
1. **Queue time:** Kadang ada antrian job (2-3 hari wait time)
2. **Material waste:** ±15% dari sheet (nesting tidak optimal)
3. **Bit wear:** Tool life tracking manual (risk over-use)
4. **Chip evacuation:** Kadang chip menumpuk, perlu bersihkan manual

**Relevansi dengan Analisis:**
CNC capacity menjadi constraint signifikan (Section 3.3.1). Ekspansi kapasitas (Lampiran D.2) include penambahan CNC unit kedua atau upgrade ke CNC dengan auto tool changer.

**Rekomendasi Perbaikan:**
1. **Short-term:** Optimize nesting software untuk reduce waste
2. **Short-term:** Implement preventive maintenance schedule
3. **Medium-term:** Add second CNC machine (increase capacity 100%)
4. **Long-term:** Upgrade ke CNC dengan automation (tool changer, auto loading)

---

### **FOTO F.2.2: Area Cutting - Laser Cutting Machine**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Foto Laser Cutter]                           │
│                                                             │
│   ╔═══════════════════════════════════════════╗             │
│   ║  LASER CUTTING MACHINE (CO2)              ║             │
│   ║                                           ║             │
│   ║  ┌─────────────────────────────────────┐  ║             │
│   ║  │     •─────────────•                 │  ║             │
│   ║  │     │   LASER    │                 │  ║             │
│   ║  │     │   HEAD     │                 │  ║             │
│   ║  │     •─────────────•                 │  ║             │
│   ║  │         ↓ ↓ ↓                       │  ║             │
│   ║  │    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                  │  ║             │
│   ║  │    ▓ ACRYLIC  ▓                    │  ║             │
│   ║  │    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                  │  ║             │
│   ║  │                                     │  ║             │
│   ║  │    [Honeycomb Bed]                  │  ║             │
│   ║  └─────────────────────────────────────┘  ║             │
│   ║                                           ║             │
│   ║  Laser Power: 80W CO2                     ║             │
│   ║  Control: RDWorks / LaserCAD              ║             │
│   ╚═══════════════════════════════════════════╝             │
│                                                             │
│   Red glow terlihat saat cutting (CO2 laser)              │
│   Exhaust system: ON (hisap asap)                         │
└─────────────────────────────────────────────────────────────┘
```

**Informasi Foto:**
- **Tanggal Dokumentasi:** 16 Agustus 2025
- **Waktu:** 11:30 WIB
- **Operator:** 1 orang (shared dengan CNC)

**Spesifikasi Laser Cutter:**
- **Type:** CO2 Laser
- **Power:** 80W
- **Working Area:** 900mm x 600mm
- **Max Cutting Thickness:** 
  - Akrilik: up to 10mm
  - Paper/Cardboard: up to 3mm
- **Cutting Speed:** 0-500mm/s
- **Positioning Accuracy:** ±0.01mm
- **Control Software:** RDWorks / LaserCAD

**Deskripsi Proses:**
Laser cutter digunakan untuk detail cutting yang memerlukan presisi sangat tinggi atau untuk material tipis (<5mm). Keunggulan:
- Edge lebih halus dan transparan (self-polishing effect)
- Detail sangat fine (text kecil, logo intricate)
- Faster untuk thin material
- No contact cutting (no material stress)

**Aplikasi Typical:**
1. Text cutting (huruf kecil <2cm)
2. Logo detail dengan curves kompleks
3. Engraving untuk texture atau pattern
4. Prototype dan sample (quick turnaround)
5. Thin acrylic (3mm) untuk layering

**Observasi Kunci:**
- ✓ Presisi excellent (detail sangat fine)
- ✓ Edge quality superior (flame-polished effect)
- ✓ Setup time cepat (5-10 menit)
- ✓ No bit wear issue (vs CNC)
- ⚠ Limited thickness capacity (max 10mm, optimal 3-5mm)
- ⚠ Smaller working area vs CNC
- ⚠ Slower untuk thick material (>8mm)
- ⚠ Exhaust system critical (smoke & fume)

**Comparison: Laser vs CNC**

| Aspect | Laser Cutter | CNC Router |
|--------|--------------|------------|
| **Precision** | ±0.01mm (superior) | ±0.05mm (good) |
| **Edge Quality** | Smooth, flame-polished | Need polishing |
| **Thickness** | Up to 10mm | Up to 15mm+ |
| **Speed (thin)** | Fast (3mm) | Medium |
| **Speed (thick)** | Slow (10mm) | Fast |
| **Detail** | Excellent (fine detail) | Good (limited by bit) |
| **Material Stress** | None (no contact) | Possible (cutting force) |
| **Maintenance** | Low (tube life 2-3 tahun) | Medium (bit replacement) |
| **Use Case** | Detail, thin, prototype | Thick, large, volume |

**Kapasitas Produksi:**
- **Effective working time:** 6 jam/hari (shared dengan CNC operator)
- **Utilization rate:** 40-50% (secondary machine)
- **Output:** Varies by complexity, typical 5-10 jobs/hari
- **Capacity constraint:** No (currently underutilized)

**Relevansi dengan Analisis:**
Laser cutter sebagai complementary tool, tidak menjadi bottleneck saat ini. Namun untuk ekspansi product line (detail sign, engraving service), perlu increase utilization atau upgrade power.

---

### **FOTO F.2.3: Area Finishing - Polishing & Edge Treatment**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Foto Polishing Area]                         │
│                                                             │
│  ┌──────────────────────────────────────────┐              │
│  │  POLISHING WORKBENCH                     │              │
│  │                                           │              │
│  │   ┌─────────┐   ┌─────────┐             │              │
│  │   │ Grinder │   │ Sander  │             │              │
│  │   │  Tools  │   │ Machine │             │              │
│  │   └─────────┘   └─────────┘             │              │
│  │                                           │              │
│  │   [Polishing Compounds] [Cloths]         │              │
│  │   [Sandpaper: 240-2000 grit]             │              │
│  │   [Flame torch] [Heat gun]               │              │
│  │                                           │              │
│  │   ┌──────────────────────────┐           │              │
│  │   │  Work in Progress:       │           │              │
│  │   │  ▓▓▓▓▓▓▓▓▓▓▓             │           │              │
│  │   │  ▓ Acrylic ▓             │           │              │
│  │   │  ▓ Pieces  ▓             │           │              │
│  │   │  ▓▓▓▓▓▓▓▓▓▓▓             │           │              │
│  │   │  (being polished)         │           │              │
│  │   └──────────────────────────┘           │              │
│  └──────────────────────────────────────────┘              │
│                                                             │
│  Worker: 2 finishers (manual work)                         │
└─────────────────────────────────────────────────────────────┘
```

**Informasi Foto:**
- **Tanggal Dokumentasi:** 16 Agustus 2025
- **Waktu:** 13:00 WIB
- **Workers:** 2 finishers

**Deskripsi Area:**
Area finishing adalah proses manual intensive untuk:
1. Edge polishing (tepi akrilik dihaluskan)
2. Surface finishing (hilangkan scratch, bercak)
3. Flame polishing (untuk clear acrylic, transparansi maksimal)
4. Final cleaning dan inspection

**Proses Polishing Step-by-Step:**

**Step 1: Rough Polishing**
- Gunakan sander atau grinder untuk remove rough edge dari cutting
- Sandpaper 240-400 grit
- Focus: Shape correction, major imperfection removal
- Time: 5-10 menit/piece

**Step 2: Medium Polishing**
- Sandpaper 600-1000 grit
- Bertahap naik grit untuk smoother surface
- Water sanding untuk reduce heat
- Time: 10-15 menit/piece

**Step 3: Fine Polishing**
- Sandpaper 1500-2000 grit (very fine)
- Surface sudah halus, scratch minimal
- Polishing compound application
- Time: 5-10 menit/piece

**Step 4: Flame Polishing (untuk clear acrylic)**
- Gunakan torch dengan api kecil
- Quick pass on edge (1-2 detik per section)
- Edge meleleh tipis dan mengeras kembali (glossy finish)
- Require skill (jika terlalu lama, material melengkung/gosong)
- Time: 3-5 menit/piece

**Step 5: Final Cleaning**
- Bersihkan dengan cleaner khusus akrilik
- Soft cloth untuk hindari scratch baru
- Inspection untuk kualitas
- Time: 2-3 menit/piece

**Total Time per Piece:** 25-45 menit (tergantung kompleksitas)

**Tools & Materials Used:**
- Belt sander / orbital sander
- Rotary tool (Dremel) untuk detail
- Sandpaper various grits (240 - 2000)
- Polishing compound (paste & liquid)
- Microfiber cloth
- Propane torch untuk flame polishing
- Acrylic cleaner spray
- PPE: Mask, safety glasses, gloves

**Observasi Kunci:**
- ✓ Skill level finishers tinggi (hasil sangat baik)
- ✓ Quality conscious (tidak rush, fokus pada hasil)
- ✓ Hand polishing give superior edge quality
- ⚠ **BOTTLENECK:** Proses paling time-consuming
- ⚠ Labor intensive (2 workers fully occupied)
- ⚠ Productivity tergantung skill individual
- ⚠ Quality variance antar workers (slight inconsistency)
- ⚠ Tiring work (repetitive, physical)

**Kapasitas Produksi:**
- **Worker 1 (senior):** 10-12 pieces/hari (complex), 15-18 (simple)
- **Worker 2 (junior):** 8-10 pieces/hari (complex), 12-15 (simple)
- **Combined capacity:** ±30 pieces/hari average
- **Constraint level:** HIGH - Major bottleneck

**Quality Issue Observed:**
- Occasional scratch dari handling (5% pieces need rework)
- Flame polishing require high skill (junior kadang burn edges)
- Inconsistency waktu polishing (rush vs careful)

**Relevansi dengan Analisis:**
Finishing area adalah **CRITICAL BOTTLENECK** yang teridentifikasi di Section 3.3.1. Ini area prioritas untuk:
1. **Jangka Pendek:** Training additional finisher, SOP standardization
2. **Jangka Menengah:** Invest in automated polishing machine
3. **Jangka Panjang:** Full automation dengan robotic polishing

**Rekomendasi Perbaikan:**

**Short-term (0-6 bulan):**
- Cross-training operator lain untuk finishing (backup capacity)
- Standardize polishing SOP (reduce variance)
- Jig/fixture untuk consistent positioning
- Time study untuk identify efficiency opportunity

**Medium-term (6-18 bulan):**
- Invest polishing automation equipment
  * Automated edge polisher (Rp 50-80 juta)
  * Reduce polishing time 40-50%
  * Consistent quality
- Add 1-2 finisher untuk handle volume increase

**Long-term (18-36 bulan):**
- Robotic polishing system (Lampiran D.3)
- Fully automated finishing line
- Capacity increase 5-10x
- Free up labor untuk higher-value tasks

---

### **FOTO F.2.4: Area Assembly - Multi-layer Assembly & LED Installation**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Foto Assembly Area]                          │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  ASSEMBLY WORKBENCH                                  │  │
│  │                                                       │  │
│  │   ┌────────────────┐        ┌────────────────┐      │  │
│  │   │  STATION #1    │        │  STATION #2    │      │  │
│  │   │                │        │                │      │  │
│  │   │  [Work Area]   │        │  [Work Area]   │      │  │
│  │   │                │        │                │      │  │
│  │   │  Tools:        │        │  Tools:        │      │  │
│  │   │  - Glue gun    │        │  - Soldering   │      │  │
│  │   │  - Clamps      │        │  - Wire tools  │      │  │
│  │   │  - Level       │        │  - Multimeter  │      │  │
│  │   └────────────────┘        └────────────────┘      │  │
│  │                                                       │  │
│  │   ┌──────────────────────────────────────┐           │  │
│  │   │  Component Storage:                  │           │  │
│  │   │  [LED Strips] [Adaptors] [Brackets]  │           │  │
│  │   │  [Wires] [Connectors] [Hardware]     │           │  │
│  │   └──────────────────────────────────────┘           │  │
│  │                                                       │  │
│  │   Testing Area: [Power supply] [Test fixtures]       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Informasi Foto:**
- **Tanggal Dokumentasi:** 16 Agustus 2025
- **Waktu:** 14:30 WIB
- **Workers:** 2 assemblers

**Deskripsi Proses Assembly:**

**Tipe Assembly:**

**1. Simple Assembly (No LED)**
- Mounting bracket installation
- Backing attachment
- Hardware fitting
- **Time:** 15-30 menit/piece

**2. Multi-layer Assembly**
- Layer stacking dengan spacer
- 3D effect creation
- Alignment critical
- Adhesive application
- **Time:** 45-60 menit/piece

**3. LED Assembly (Backlit)**
- LED strip installation
- Wiring dan soldering
- Power supply connection
- Diffuser installation (if any)
- Testing
- **Time:** 60-90 menit/piece

**4. Complex Assembly (Multi-layer + LED)**
- Combination of above
- Most time-consuming
- Require precision dan skill
- **Time:** 90-120 menit/piece

**Process Flow Observed:**

**Station #1: Structural Assembly**
1. **Preparation:** Clean all parts, remove protective film
2. **Dry fit:** Test fit semua parts tanpa adhesive
3. **Alignment:** Ensure proper positioning (gunakan jig jika available)
4. **Gluing:** Apply structural adhesive (akrilik glue atau epoxy)
5. **Clamping:** Hold parts dengan clamp, wait curing (5-15 menit)
6. **Check:** Verify alignment dan bonding strength

**Station #2: LED Installation & Wiring**
1. **LED layout:** Mark LED strip position
2. **Strip cutting:** Cut LED strip to required length
3. **Mounting:** Adhesive backing atau mounting channel
4. **Soldering:** Connect wires, parallel/series configuration
5. **Power connection:** Adaptor dan switch installation
6. **Testing:** Power on, check semua LED menyala, brightness uniform
7. **Cable management:** Wire routing, tidy up

**Tools & Materials:**

**Assembly Tools:**
- Hot glue gun (general purpose)
- Structural adhesive (akrilik-specific)
- Clamps various sizes
- Level (untuk ensure flat/straight)
- Measuring tape & ruler
- Drill & bits (untuk mounting holes)

**LED Tools:**
- Soldering iron & solder
- Wire stripper & cutter
- Multimeter (testing voltage/continuity)
- Heat shrink tubing
- Electrical tape
- Cable ties

**Components:**
- LED strip (various types)
- Power adaptor (12V DC typical)
- Wires (red/black, various gauge)
- Connectors (JST, barrel jack)
- Switch (if required)
- Mounting hardware

**Observasi Kunci:**
- ✓ Clean work area, organized tools
- ✓ Workers experienced (good hand skills)
- ✓ Testing thorough sebelum final packaging
- ✓ Quality conscious (jika ada issue, di-rework)
- ⚠ Process manual dan time-intensive
- ⚠ LED installation require electrical knowledge (not all workers trained)
- ⚠ No standardized jig/fixture (alignment rely on skill)
- ⚠ Cable management kadang kurang rapi (time pressure)

**Quality Control Points:**

**Visual Inspection:**
- ✓ No gap antar layers
- ✓ Alignment perfect (no offset)
- ✓ Adhesive tidak terlihat dari luar
- ✓ Surface bersih, no fingerprint/dust

**Functional Test (LED):**
- ✓ All LED segments menyala
- ✓ Brightness uniform (no dim sections)
- ✓ Wiring secure (no loose connection)
- ✓ No flickering
- ✓ Heat test (run 30 menit, check tidak overheat)

**Structural Test:**
- ✓ Bonding kuat (pull test)
- ✓ Mounting secure
- ✓ Tidak ada part yang loose/goyang

**Common Issues Encountered:**
1. **Alignment problem** (3-5% parts) → Rework required
2. **LED tidak menyala** (2-3%) → Troubleshoot wiring, replace jika perlu
3. **Adhesive visible** (1-2%) → Cleaning atau replace jika severe
4. **Bubble dalam adhesive** (2-3%) → Prevention via proper application technique

**Kapasitas Produksi:**
- **Simple assembly:** 15-20 pieces/hari per worker
- **LED assembly:** 6-8 pieces/hari per worker
- **Complex assembly:** 4-5 pieces/hari per worker
- **Mixed typical:** ±10-12 pieces/hari per worker (2 workers = 20-24 total)

**Relevansi dengan Analisis:**
Assembly area also potential bottleneck terutama untuk LED products (high margin products). Need for:
- Standardized fixtures untuk improve consistency & speed
- Additional training untuk all workers on LED installation
- Better testing equipment
- Consider semi-automation untuk repetitive tasks

**Rekomendasi:**
1. Develop assembly jigs untuk common product types
2. Comprehensive LED training program (safety + skills)
3. Invest in better testing equipment (power supply, load tester)
4. SOPing assembly process (reference Lampiran B)
5. Medium-term: Consider automated LED strip application

---

### **FOTO F.2.5: Quality Control & Final Inspection**

```
┌─────────────────────────────────────────────────────────────┐
│  [PLACEHOLDER: Foto QC Inspection]                          │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  QC INSPECTION STATION                               │  │
│  │                                                       │  │
│  │   ┌────────────────────────────────────┐             │  │
│  │   │  Inspection Table                  │             │  │
│  │   │  (White surface, good lighting)    │             │  │
│  │   │                                    │             │  │
│  │   │   [Product under inspection]       │             │  │
│  │   │                                    │             │  │
│  │   └────────────────────────────────────┘             │  │
│  │                                                       │  │
│  │   QC Tools:                                           │  │
│  │   - Caliper (measuring)                              │  │
│  │   - Magnifying glass (detail inspection)             │  │
│  │   - Flashlight (check internal, bubbles)             │  │
│  │   - Checklist (QC form)                              │  │
│  │   - Camera (defect documentation)                    │  │
│  │                                                       │  │
│  │   Status Board:                                       │  │
│  │   [PASS] [CONDITIONAL] [REJECT]                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Informasi Foto:**
- **Tanggal Dokumentasi:** 16 Agustus 2025
- **Waktu:** 16:00 WIB (Shift end, final QC)
- **QC Inspector:** 1 dedicated (atau owner/manager)

**Deskripsi QC Process:**

Quality Control dilakukan di 3 checkpoints (sesuai Lampiran B.5):
1. **QC#1:** After cutting (dimensional & edge quality)
2. **QC#2:** After finishing (surface quality)
3. **QC#3:** Final inspection (overall product)

**Final QC Inspection Criteria:**

**A. Dimensional Accuracy**
- Measure critical dimensions dengan caliper
- Tolerance: ±1mm untuk overall, ±0.5mm untuk detail
- **Pass rate:** 95% (typical)

**B. Visual Quality**
- Surface: No scratch, crack, bubble, bercak
- Edge: Smooth, polished, no roughness
- Color: Uniform, sesuai spesifikasi
- **Pass rate:** 90-92%

**C. Functional Test (if applicable)**
- LED: All lights working, brightness uniform
- Mounting: Secure, tidak goyang
- **Pass rate:** 93-95%

**D. Cleanliness**
- No dust, fingerprint, atau foreign material
- Protective film intact (jika untuk shipping)
- **Pass rate:** 88-90%

**E. Completeness**
- All parts included (mounting hardware, adaptor, etc.)
- Documentation (manual, warranty card jika applicable)
- **Pass rate:** 98%

**QC Decision Matrix:**

| Finding | Action | Frequency |
|---------|--------|-----------|
| **PASS** | Proceed to packaging | 85-88% |
| **CONDITIONAL PASS** | Minor fix required (cleaning, touch-up) | 10-12% |
| **REJECT** | Major rework atau scrap | 2-3% |

**Common Defects Observed:**

**Category 1: Cosmetic (dapat di-fix)**
- Light scratch (polish ulang) - 5%
- Fingerprint/dust (cleaning) - 8%
- Minor alignment issue (acceptable within tolerance) - 2%

**Category 2: Functional (require rework)**
- LED flickering/tidak menyala (troubleshoot wiring) - 2%
- Weak bonding (re-glue) - 1%
- Dimensional out of spec (re-cut if critical) - 1%

**Category 3: Critical (reject/scrap)**
- Crack atau chip material - 0.5%
- Severe deformation - 0.3%
- Color mismatch (material issue) - 0.2%

**Total Defect Rate:** ±12-15% (including minor)  
**Scrap Rate:** ±1% (acceptable untuk custom manufacturing)

**QC Tools & Equipment:**

**Measurement Tools:**
- Digital caliper (0.01mm resolution)
- Ruler & measuring tape
- Angle gauge (untuk verify 90° corners)

**Visual Inspection:**
- Magnifying glass (5x-10x)
- LED flashlight (untuk check internal)
- Color reference chart

**Functional Testing:**
- Power supply (various voltage)
- Multimeter
- Timer (untuk endurance test)

**Documentation:**
- QC checklist form (paper - manual)
- Camera (smartphone) untuk document defects
- Logbook untuk track rejection reasons

**Observasi Kunci:**
- ✓ QC inspection cukup thorough
- ✓ Clear accept/reject criteria
- ✓ Inspector experienced (good eye untuk detail)
- ⚠ QC checklist manual (paper form)
- ⚠ No digital tracking of defect data
- ⚠ Root cause analysis tidak sistematis
- ⚠ Feedback loop ke production tidak structured

**Data QC (Sample 1 Minggu - 10-16 Agustus 2025):**

| Day | Units Inspected | Pass | Conditional | Reject | Pass Rate |
|-----|-----------------|------|-------------|--------|-----------|
| Mon | 12 | 10 | 2 | 0 | 83% |
| Tue | 15 | 13 | 1 | 1 | 87% |
| Wed | 10 | 9 | 1 | 0 | 90% |
| Thu | 14 | 12 | 2 | 0 | 86% |
| Fri | 11 | 10 | 0 | 1 | 91% |
| **Total** | **62** | **54** | **6** | **2** | **87%** |

**Analysis:**
- First-pass yield: 87% (target industry: >90%)
- Rework rate: 10% (need improvement)
- Scrap rate: 3% (acceptable)

**Relevansi dengan Analisis:**
QC system ada tapi belum optimal (Section 3.3.1 - QC Inconsistent). Priority actions:
1. Digitalize QC checklist (tablet-based)
2. Implement defect tracking system
3. Root cause analysis untuk common defects
4. Feedback loop automation ke production
5. Statistical Process Control (SPC) implementation

**Rekomendasi Improvement:**
1. **Immediate:** Digital QC checklist (reference Lampiran B.5)
2. **Short-term:** Defect database untuk trend analysis
3. **Medium-term:** Automated optical inspection (AOI) untuk consistency
4. **Long-term:** In-line QC sensors untuk real-time monitoring

---

**RINGKASAN DOKUMENTASI F.2:**

Total foto dokumentasi proses: 5 areas  
Coverage: Complete production workflow  
Tanggal observasi: 16 Agustus 2025

**Key Findings - Proses Produksi:**

**Strengths:**
- ✓ Skilled workers di setiap area
- ✓ Quality-conscious culture
- ✓ Good equipment maintenance
- ✓ Clean dan organized workspace

**Weaknesses & Bottlenecks:**
- ⚠ **Critical Bottleneck:** Finishing area (polishing)
- ⚠ Assembly untuk LED products time-intensive
- ⚠ Single CNC = reliability risk
- ⚠ Manual QC = data tidak terstruktur

**Capacity Constraints:**
- CNC: 8-12 pcs/hari (dapat di-push ke 15)
- Finishing: 25-30 pcs/hari (BOTTLENECK)
- Assembly: 20-24 pcs/hari
- **Overall capacity:** ±25-30 pcs/hari limited by finishing

**Quality Performance:**
- First-pass yield: 87% (good, but can improve to 90%+)
- Rework rate: 10%
- Scrap rate: 3%

**Prioritas Perbaikan:**
1. **URGENT:** Address finishing bottleneck (training + equipment)
2. **HIGH:** Standardize QC dan digitalize tracking
3. **MEDIUM:** Backup CNC capacity (reliability)
4. **MEDIUM:** Assembly standardization (jigs/fixtures)

---

*Dokumentasi F.2 selesai. Lanjut ke F.3 - Dokumentasi Sistem dan Teknologi.*

---

**Disiapkan oleh:** Tim Peneliti  
**Tanggal:** Agustus 2025  
**Lokasi:** SATRIAMART Workshop, Depok
