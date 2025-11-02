# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN
## Bagian 3B: Desain Antarmuka Pengguna (UI/UX Design)

---

### 4.3.5 Desain Antarmuka Pengguna (User Interface Design)

Desain antarmuka pengguna (User Interface/UI) dan pengalaman pengguna (User Experience/UX) merupakan aspek krusial dalam pengembangan sistem informasi CUR-HEART. Antarmuka yang baik tidak hanya menarik secara visual, tetapi juga harus intuitif, mudah digunakan, dan memberikan pengalaman yang menyenangkan bagi pengguna. Dalam pengembangan sistem CUR-HEART, proses desain UI/UX dilakukan dengan pendekatan user-centered design yang mempertimbangkan kebutuhan dan karakteristik dari tiga tipe pengguna utama: klien (client), terapis (therapist), dan administrator (admin).

Proses desain UI/UX CUR-HEART dimulai dengan penelitian pengguna (user research) untuk memahami kebutuhan, preferensi, dan pain points dari setiap tipe pengguna. Hasil penelitian ini kemudian diterjemahkan ke dalam wireframe, mockup, dan prototype yang dapat diuji dan divalidasi sebelum masuk ke tahap implementasi. Pendekatan iteratif ini memastikan bahwa desain akhir benar-benar memenuhi kebutuhan pengguna dan memberikan pengalaman yang optimal.

#### 4.3.5.1 Design System CUR-HEART

Design system adalah kumpulan komponen, panduan desain, dan standar yang digunakan secara konsisten di seluruh aplikasi untuk menciptakan pengalaman pengguna yang kohesif dan profesional. Design system CUR-HEART dikembangkan dengan tujuan untuk:

1. **Konsistensi Visual**: Memastikan tampilan yang seragam di seluruh halaman dan fitur
2. **Efisiensi Pengembangan**: Mempercepat proses development dengan komponen yang reusable
3. **Brand Identity**: Memperkuat identitas merek CUR-HEART sebagai layanan kesehatan mental profesional
4. **Scalability**: Memudahkan penambahan fitur baru dengan panduan desain yang jelas
5. **Accessibility**: Memastikan aplikasi dapat diakses oleh pengguna dengan berbagai kemampuan

Design system CUR-HEART terdiri dari beberapa elemen utama yang akan dijelaskan pada sub-section berikutnya.

#### 4.3.5.2 Color Palette & Typography

---

**[GAMBAR 4.15 - Design System: Color Palette]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT COLOR PALETTE DESIGN]                            │
│                                                             │
│   CUR-HEART COLOR SYSTEM                                   │
│   Professional & Calming Palette                           │
│                                                             │
│   PRIMARY COLORS:                                           │
│   ┌──────────┐  ┌──────────┐                               │
│   │ Navy Blue│  │   Pink   │                               │
│   │ #1E0E62  │  │ #FF6B7A  │                               │
│   │ █████████│  │ █████████│                               │
│   │ Trust &  │  │ Empathy &│                               │
│   │ Stability│  │ Warmth   │                               │
│   └──────────┘  └──────────┘                               │
│                                                             │
│   SECONDARY COLORS:                                         │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐                │
│   │Light Pur.│  │Soft Pink │  │  White   │                │
│   │ #EEEAF9  │  │ #FFE5E8  │  │ #FFFFFF  │                │
│   │ █████████│  │ █████████│  │ █████████│                │
│   └──────────┘  └──────────┘  └──────────┘                │
│                                                             │
│   GRAYSCALE:                                                │
│   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐            │
│   │#333  │ │#666  │ │#999  │ │#CCC  │ │#F5F5 │            │
│   │██████│ │██████│ │██████│ │██████│ │██████│            │
│   │Dark  │ │Med.  │ │Light │ │Border│ │BG    │            │
│   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘            │
│                                                             │
│   SEMANTIC COLORS:                                          │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│   │ Success  │  │ Warning  │  │  Danger  │  │   Info   │  │
│   │ #10B981  │  │ #F59E0B  │  │ #EF4444  │  │ #3B82F6  │  │
│   │ █████████│  │ █████████│  │ █████████│  │ █████████│  │
│   │  Green   │  │  Orange  │  │   Red    │  │   Blue   │  │
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
│                                                             │
│   COLOR USAGE EXAMPLES:                                     │
│   • Headers/Nav: Navy Blue (#1E0E62)                        │
│   • CTA Buttons: Pink (#FF6B7A)                             │
│   • Backgrounds: Light Purple (#EEEAF9), White              │
│   • Body Text: Dark Gray (#333333)                          │
│   • Success: Green (#10B981) - Approved, Completed          │
│   • Warning: Orange (#F59E0B) - Pending, Review             │
│   • Danger: Red (#EF4444) - Error, Cancel, Delete           │
│                                                             │
│   ACCESSIBILITY:                                            │
│   ✅ WCAG 2.1 AA Compliant                                  │
│   ✅ Contrast Ratio: 4.5:1 minimum for text                 │
│   ✅ Color blind friendly combinations                      │
│                                                             │
│   Format: Color Palette PNG dengan hex codes               │
│   Recommended size: 1600x1200px                            │
│   Style: Professional swatch board dengan samples          │
│                                                             │
│   File: assets/images/design-system-color-palette.png      │
│   Tool: Figma, Adobe XD, atau Canva                        │
│                                                             │
│   PRIORITY: P2 - HIGH                                       │
│   Must show: All colors dengan hex codes, usage examples   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.15: Design System Color Palette CUR-HEART dengan primary colors (Navy Blue, Pink), secondary colors, grayscale, dan semantic colors yang WCAG AA compliant_

---

**A. Color Palette (Palet Warna)**

Pemilihan warna dalam CUR-HEART dirancang untuk mencerminkan nilai-nilai profesionalisme, kepercayaan, dan kesehatan mental. Berikut adalah palet warna yang digunakan:

**Primary Colors (Warna Utama)**:
- **Navy Blue (#1E0E62)**: Warna dominan yang melambangkan profesionalisme, kepercayaan, dan stabilitas. Digunakan untuk header, navigation, dan elemen penting.
- **Pink (#FF6B7A)**: Warna aksen yang melambangkan empati, kehangatan, dan perawatan. Digunakan untuk call-to-action buttons dan highlights.

**Secondary Colors (Warna Pendukung)**:
- **Light Purple (#EEEAF9)**: Background untuk section dan cards, memberikan nuansa tenang
- **Soft Pink (#FFE5E8)**: Highlight untuk area tertentu, melengkapi pink primary
- **White (#FFFFFF)**: Background utama, menciptakan ruang bernafas (breathing room)
- **Gray Scale**: 
  - Dark Gray (#333333) untuk teks body
  - Medium Gray (#666666) untuk teks secondary
  - Light Gray (#F5F5F5) untuk borders dan dividers

**Semantic Colors (Warna Fungsional)**:
- **Success Green (#10B981)**: Notifikasi sukses, status approved
- **Warning Orange (#F59E0B)**: Alert, pending actions
- **Danger Red (#EF4444)**: Error messages, delete actions
- **Info Blue (#3B82F6)**: Informational messages

Palet warna ini dipilih berdasarkan prinsip-prinsip psikologi warna dalam konteks kesehatan mental, di mana warna-warna yang menenangkan dan profesional sangat penting untuk menciptakan rasa aman dan percaya bagi klien.

---

**[GAMBAR 4.16 - Design System: Typography System]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT TYPOGRAPHY SYSTEM]                               │
│                                                             │
│   CUR-HEART TYPOGRAPHY SYSTEM                              │
│   Modern & Readable Type Scale                             │
│                                                             │
│   FONT FAMILIES:                                            │
│                                                             │
│   PRIMARY (Headings):                                       │
│   Poppins - Sans-serif                                     │
│   Aa Bb Cc Dd Ee Ff Gg Hh                                  │
│   Weights: 400 (Regular), 500 (Medium),                    │
│            600 (SemiBold), 700 (Bold)                      │
│   Usage: H1-H6, Navigation, Buttons                        │
│                                                             │
│   SECONDARY (Body):                                         │
│   Inter - Sans-serif                                       │
│   Aa Bb Cc Dd Ee Ff Gg Hh                                  │
│   Weights: 400 (Regular), 500 (Medium), 600 (SemiBold)     │
│   Usage: Paragraphs, Labels, Tables, Forms                 │
│                                                             │
│   TYPE SCALE (Modular Scale 1.25):                         │
│                                                             │
│   H1 - Display Large                                       │
│   36px / 2.25rem - Line Height 43px                        │
│   Poppins Bold (700)                                       │
│   Usage: Page titles, hero headings                        │
│                                                             │
│   H2 - Display Medium                                      │
│   30px / 1.875rem - Line Height 36px                       │
│   Poppins SemiBold (600)                                   │
│   Usage: Section titles                                    │
│                                                             │
│   H3 - Heading Large                                       │
│   24px / 1.5rem - Line Height 29px                         │
│   Poppins SemiBold (600)                                   │
│   Usage: Subsection titles, card headers                   │
│                                                             │
│   H4 - Heading Medium                                      │
│   20px / 1.25rem - Line Height 24px                        │
│   Poppins Medium (500)                                     │
│   Usage: Component titles                                  │
│                                                             │
│   H5 - Heading Small                                       │
│   18px / 1.125rem - Line Height 22px                       │
│   Poppins Medium (500)                                     │
│   Usage: Small headings, emphasis                          │
│                                                             │
│   Body Large                                               │
│   16px / 1rem - Line Height 24px (1.5x)                    │
│   Inter Regular (400)                                      │
│   Usage: Important body text, intro paragraphs             │
│                                                             │
│   Body Regular                                             │
│   14px / 0.875rem - Line Height 21px (1.5x)                │
│   Inter Regular (400)                                      │
│   Usage: Standard body text, form inputs                   │
│                                                             │
│   Body Small / Caption                                     │
│   12px / 0.75rem - Line Height 18px (1.5x)                 │
│   Inter Regular (400)                                      │
│   Usage: Captions, helper text, footnotes                  │
│                                                             │
│   SPACING & RHYTHM:                                         │
│   • Headings: Line height 1.2x (tight)                     │
│   • Body: Line height 1.5x (comfortable)                   │
│   • Paragraph spacing: 1em bottom margin                   │
│   • Letter spacing: -0.02em for large headings             │
│                                                             │
│   EXAMPLES:                                                 │
│   [Show sample text in each size with actual rendering]    │
│                                                             │
│   ACCESSIBILITY:                                            │
│   ✅ Minimum 12px font size                                 │
│   ✅ Line height ≥ 1.5 for body text                        │
│   ✅ High contrast ratios maintained                        │
│                                                             │
│   Format: Typography Specimen PNG                          │
│   Recommended size: 1600x2000px (vertical)                 │
│   Style: Type specimen board dengan samples                │
│                                                             │
│   File: assets/images/design-system-typography.png         │
│   Tool: Figma, Adobe XD, atau design software              │
│                                                             │
│   PRIORITY: P2 - HIGH                                       │
│   Must show: Font samples, sizes, weights, line heights    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.16: Typography System CUR-HEART dengan Poppins (headings) dan Inter (body), showing complete type scale dari H1 (36px) hingga Caption (12px) dengan line heights dan weights_

---

**B. Typography (Tipografi)**

Tipografi yang dipilih untuk CUR-HEART mengutamakan keterbacaan (readability) dan kejelasan (legibility):

**Font Families**:
1. **Poppins** (Sans-serif) - Untuk Headings
   - Font modern dan friendly yang mudah dibaca
   - Digunakan untuk: H1, H2, H3, H4, H5, H6, dan navigation menu
   - Font weights: Regular (400), Medium (500), SemiBold (600), Bold (700)

2. **Inter** (Sans-serif) - Untuk Body Text
   - Font yang sangat readable bahkan dalam ukuran kecil
   - Digunakan untuk: paragraf, descriptions, form labels, table content
   - Font weights: Regular (400), Medium (500), SemiBold (600)

**Type Scale (Skala Ukuran)**:
- **H1 (Heading 1)**: 36px / 2.25rem - Page titles
- **H2 (Heading 2)**: 30px / 1.875rem - Section titles
- **H3 (Heading 3)**: 24px / 1.5rem - Subsection titles
- **H4 (Heading 4)**: 20px / 1.25rem - Card titles
- **H5 (Heading 5)**: 18px / 1.125rem - Small headings
- **Body Large**: 16px / 1rem - Important body text
- **Body Regular**: 14px / 0.875rem - Standard body text
- **Body Small**: 12px / 0.75rem - Captions, helper text

**Line Height & Spacing**:
- Headings: 1.2x font size (tight leading untuk emphasis)
- Body text: 1.5x font size (comfortable reading)
- Paragraph spacing: 1em bottom margin

Pemilihan kombinasi Poppins dan Inter memberikan keseimbangan antara karakter yang friendly (untuk headings) dan profesional (untuk body text), sesuai dengan positioning CUR-HEART sebagai layanan hypnotherapy yang modern dan terpercaya.

#### 4.3.5.3 Component Library

---

**[GAMBAR 4.17 - Design System: Component Library]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT COMPONENT LIBRARY]                               │
│                                                             │
│   CUR-HEART COMPONENT LIBRARY                              │
│   Reusable UI Components                                   │
│                                                             │
│   BUTTONS (8 Variants):                                     │
│   ┌────────────────┐  ┌────────────────┐                   │
│   │  Primary Btn   │  │ Secondary Btn  │                   │
│   │  [Pink BG]     │  │ [White + Navy] │                   │
│   └────────────────┘  └────────────────┘                   │
│   ┌────────────────┐  ┌────────────────┐                   │
│   │  Outline Btn   │  │   Ghost Btn    │                   │
│   │ [Border only]  │  │  [Text only]   │                   │
│   └────────────────┘  └────────────────┘                   │
│   States: Default, Hover, Active, Disabled, Loading        │
│                                                             │
│   FORM INPUTS (6 Types):                                    │
│   • Text Input (single line)                                │
│   • Textarea (multi line)                                   │
│   • Select Dropdown                                         │
│   • Checkbox                                                │
│   • Radio Button                                            │
│   • Date/Time Picker                                        │
│   States: Default, Focus, Error, Success, Disabled          │
│                                                             │
│   CARDS (4 Variants):                                       │
│   ┌─────────────────────────┐                               │
│   │ Service Card            │                               │
│   │ [Image + Title + Price] │                               │
│   └─────────────────────────┘                               │
│   ┌─────────────────────────┐                               │
│   │ Therapist Profile Card  │                               │
│   │ [Photo + Bio + Rating]  │                               │
│   └─────────────────────────┘                               │
│   ┌─────────────────────────┐                               │
│   │ Booking Summary Card    │                               │
│   │ [Details + Status]      │                               │
│   └─────────────────────────┘                               │
│                                                             │
│   NAVIGATION:                                               │
│   • Top Navigation Bar (desktop)                            │
│   • Mobile Hamburger Menu                                   │
│   • Sidebar (admin/therapist dashboard)                     │
│   • Breadcrumbs                                             │
│   • Pagination                                              │
│                                                             │
│   ALERTS & NOTIFICATIONS:                                   │
│   • Success Alert (green)                                   │
│   • Warning Alert (orange)                                  │
│   • Error Alert (red)                                       │
│   • Info Alert (blue)                                       │
│   • Toast Notification (auto-dismiss)                       │
│                                                             │
│   MODALS & OVERLAYS:                                        │
│   • Confirmation Modal                                      │
│   • Form Modal                                              │
│   • Image Lightbox                                          │
│   • Loading Overlay                                         │
│                                                             │
│   TABLES:                                                   │
│   • Data Table (sortable, filterable)                       │
│   • Responsive Table (mobile-friendly)                      │
│   • Table with actions                                      │
│                                                             │
│   BADGES & LABELS:                                          │
│   • Status Badge (Pending, Confirmed, Completed, etc.)      │
│   • Role Label (Client, Therapist, Admin)                   │
│   • Count Badge (notifications, messages)                   │
│                                                             │
│   OTHER COMPONENTS:                                         │
│   • Avatar (user photo)                                     │
│   • Rating Stars (1-5 stars)                                │
│   • Progress Bar                                            │
│   • Tabs                                                    │
│   • Accordion                                               │
│   • Tooltip                                                 │
│   • Skeleton Loader (loading state)                         │
│                                                             │
│   TOTAL COMPONENTS: 30+                                     │
│   All components are:                                       │
│   ✅ Responsive (mobile-first)                              │
│   ✅ Accessible (WCAG AA)                                   │
│   ✅ Reusable (DRY principle)                               │
│   ✅ Documented (usage guidelines)                          │
│                                                             │
│   Format: Component Library PNG (grid layout)              │
│   Recommended size: 2400x3000px (large, detailed)          │
│   Style: Component showcase dengan states & variations     │
│                                                             │
│   File: assets/images/design-system-components.png         │
│   Tool: Figma, Adobe XD (preferred for interactive)        │
│                                                             │
│   PRIORITY: P2 - HIGH                                       │
│   Must show: All major components dengan variations        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.17: Component Library CUR-HEART dengan 30+ reusable components (buttons, forms, cards, navigation, alerts, modals, tables, badges) dengan states dan variations_

---

Component library adalah kumpulan komponen UI yang dapat digunakan kembali (reusable) di berbagai halaman aplikasi. Berikut adalah komponen-komponen utama dalam CUR-HEART design system:

**A. Buttons (Tombol)**

1. **Primary Button**: 
   - Background: Pink (#FF6B7A)
   - Text: White
   - Penggunaan: Call-to-action utama (Book Now, Submit, Confirm)
   - States: Default, Hover (darker pink), Active, Disabled

2. **Secondary Button**:
   - Background: White
   - Border: Navy Blue (#1E0E62)
   - Text: Navy Blue
   - Penggunaan: Aksi sekunder (Cancel, Go Back)

3. **Outline Button**:
   - Background: Transparent
   - Border: Current text color
   - Penggunaan: Tertiary actions

4. **Icon Button**:
   - Background: Transparent atau solid
   - Contains icon only
   - Penggunaan: Navigation, quick actions

**B. Form Elements**

1. **Text Input**:
   - Border: Light gray dengan focus state (navy blue)
   - Height: 40px (medium), 36px (small)
   - Border radius: 8px
   - Padding: 12px horizontal
   - States: Default, Focus, Error, Disabled

2. **Textarea**:
   - Similar styling dengan text input
   - Min height: 100px
   - Resize: vertical only

3. **Select Dropdown**:
   - Custom styled dengan icon arrow
   - Dropdown menu dengan shadow
   - Max height dengan scroll untuk opsi banyak

4. **Checkbox & Radio**:
   - Custom styled dengan checkmark animation
   - Size: 20x20px
   - Colors: Navy blue when checked

5. **Date Picker**:
   - Calendar interface dengan navigation
   - Highlight current date dan selected date
   - Disable past dates untuk booking

6. **Time Picker**:
   - Grid layout untuk time slots
   - Show available/unavailable status
   - Visual feedback untuk selection

**C. Cards**

1. **Service Card**:
   - White background dengan shadow
   - Image thumbnail (aspect ratio 16:9)
   - Title, description, price
   - CTA button
   - Hover effect: shadow increase

2. **Therapist Card**:
   - Avatar/photo (rounded)
   - Name, specialization
   - Rating stars
   - Experience years
   - View Profile button

3. **Appointment Card**:
   - Status badge (upcoming, completed, cancelled)
   - Date & time info
   - Service name
   - Therapist info
   - Action buttons

4. **Dashboard Stats Card**:
   - Icon + label + value
   - Color coded per category
   - Optional trend indicator

**D. Navigation Components**

1. **Top Navigation Bar**:
   - Logo di kiri
   - Menu items di tengah (desktop)
   - User profile dropdown di kanan
   - Sticky behavior saat scroll
   - Height: 70px

2. **Sidebar Navigation** (untuk dashboard):
   - Fixed position di kiri
   - Width: 260px (expanded), 70px (collapsed)
   - Menu items dengan icon + label
   - Active state indicator (pink accent)
   - Collapsible untuk mobile

3. **Breadcrumbs**:
   - Show current page hierarchy
   - Separator: "/" atau "›"
   - Last item non-clickable

4. **Tabs**:
   - Horizontal layout
   - Active tab dengan bottom border (pink)
   - Smooth transition animation

**E. Feedback Components**

1. **Alerts/Notifications**:
   - Success: Green background dengan icon
   - Error: Red background dengan icon
   - Warning: Orange background dengan icon
   - Info: Blue background dengan icon
   - Dismissable dengan close button

2. **Toast Messages**:
   - Popup dari top-right corner
   - Auto-dismiss setelah 3-5 detik
   - Stack multiple toasts
   - Slide-in animation

3. **Loading Indicators**:
   - Spinner: Circular dengan navy blue color
   - Skeleton screen: Untuk data yang sedang load
   - Progress bar: Untuk proses multi-step

4. **Modal Dialogs**:
   - Overlay dengan backdrop blur
   - Centered content box
   - Close button (X)
   - Header, body, footer sections
   - Size variants: small, medium, large, fullscreen

**F. Data Display Components**

1. **Tables**:
   - Zebra striping untuk rows (alternating background)
   - Header dengan sort indicators
   - Hover effect pada rows
   - Action buttons per row
   - Pagination controls
   - Responsive: Scroll horizontal pada mobile

2. **Lists**:
   - Item dengan avatar/icon
   - Primary & secondary text
   - Right-side actions atau meta info
   - Dividers antar items

3. **Badges**:
   - Status indicator (new, pending, approved, etc.)
   - Small, rounded pill shape
   - Color coded
   - Sizes: small, medium, large

4. **Progress Tracking**:
   - Step indicator untuk booking flow
   - Progress bar dengan percentage
   - Milestone markers

**G. Media Components**

1. **Avatar**:
   - Circular images
   - Sizes: xs (24px), sm (32px), md (40px), lg (64px), xl (96px)
   - Fallback dengan initials
   - Status indicator (online/offline dot)

2. **Image Gallery**:
   - Grid layout
   - Lightbox untuk full view
   - Lazy loading
   - Aspect ratio maintained

3. **Video Player** (untuk session room):
   - Custom controls
   - Fullscreen option
   - Mute/unmute
   - Camera switch

Semua komponen ini dikembangkan dengan mempertimbangkan:
- **Responsiveness**: Bekerja optimal di desktop, tablet, dan mobile
- **Accessibility**: Keyboard navigation, ARIA labels, contrast ratio
- **Consistency**: Visual style yang seragam
- **Interactivity**: Feedback yang jelas untuk setiap user action
- **Performance**: Optimized untuk loading speed

Component library ini memungkinkan pengembangan yang lebih cepat dan konsisten, sekaligus memudahkan maintenance dan scalability sistem di masa depan.

---

**[GAMBAR 4.18 - Layout & Grid System]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT LAYOUT & GRID SYSTEM]                            │
│                                                             │
│   CUR-HEART LAYOUT SYSTEM                                  │
│   Responsive Grid & Spacing                                │
│                                                             │
│   GRID SYSTEM (12-Column):                                  │
│   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐        │
│   │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │        │
│   └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘        │
│                                                             │
│   BREAKPOINTS:                                              │
│   • Mobile (xs): < 640px (full width)                       │
│   • Tablet (sm): ≥ 640px (2 columns)                        │
│   • Desktop (md): ≥ 768px (3-4 columns)                     │
│   • Large (lg): ≥ 1024px (4 columns)                        │
│   • XL (xl): ≥ 1280px (max-width 1280px container)          │
│                                                             │
│   LAYOUT PATTERNS:                                          │
│                                                             │
│   1. Single Column (Mobile):                                │
│   ┌─────────────────────────┐                               │
│   │       Header            │                               │
│   ├─────────────────────────┤                               │
│   │                         │                               │
│   │       Content           │                               │
│   │     (Full Width)        │                               │
│   │                         │                               │
│   ├─────────────────────────┤                               │
│   │       Footer            │                               │
│   └─────────────────────────┘                               │
│                                                             │
│   2. Two Column (Tablet):                                   │
│   ┌─────────────────────────┐                               │
│   │       Header            │                               │
│   ├───────────┬─────────────┤                               │
│   │  Sidebar  │   Main      │                               │
│   │  (4 cols) │  (8 cols)   │                               │
│   │           │             │                               │
│   ├───────────┴─────────────┤                               │
│   │       Footer            │                               │
│   └─────────────────────────┘                               │
│                                                             │
│   3. Three Column (Desktop):                                │
│   ┌─────────────────────────────────────┐                   │
│   │          Header (Full)              │                   │
│   ├─────┬───────────────────────┬───────┤                   │
│   │ L.  │       Main            │ Right │                   │
│   │ Bar │     (8 cols)          │ Aside │                   │
│   │(2)  │                       │ (2)   │                   │
│   ├─────┴───────────────────────┴───────┤                   │
│   │          Footer (Full)              │                   │
│   └─────────────────────────────────────┘                   │
│                                                             │
│   SPACING SCALE (8px base):                                 │
│   • 0: 0px                                                  │
│   • 1: 4px  (0.25rem) - Tight spacing                       │
│   • 2: 8px  (0.5rem) - Base unit                            │
│   • 3: 12px (0.75rem)                                       │
│   • 4: 16px (1rem) - Standard spacing                       │
│   • 6: 24px (1.5rem) - Section spacing                      │
│   • 8: 32px (2rem) - Large spacing                          │
│   • 12: 48px (3rem) - Extra large spacing                   │
│   • 16: 64px (4rem) - Hero spacing                          │
│                                                             │
│   CONTAINER WIDTHS:                                         │
│   • Mobile: 100% (with 16px padding)                        │
│   • Tablet: 640px max                                       │
│   • Desktop: 1024px max                                     │
│   • Large: 1280px max (standard)                            │
│                                                             │
│   COMMON LAYOUTS:                                           │
│   • Landing Page: Hero + Features Grid (3 cols)             │
│   • Services Page: Card Grid (3 cols desktop, 1 mobile)     │
│   • Dashboard: Sidebar + Main Content                       │
│   • Form Pages: Centered form (max 600px width)             │
│   • Detail Pages: 2/3 main + 1/3 sidebar                    │
│                                                             │
│   Format: Layout System Diagram PNG                         │
│   Recommended size: 2000x1600px                            │
│   Style: Wireframe-style dengan grid overlay               │
│                                                             │
│   File: assets/images/design-system-layout-grid.png        │
│   Tool: Figma, Adobe XD, atau wireframing tool             │
│                                                             │
│   PRIORITY: P2 - HIGH                                       │
│   Must show: Grid system, breakpoints, layout patterns     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.18: Layout & Grid System CUR-HEART dengan 12-column grid, 5 breakpoints responsive, spacing scale (8px base), dan common layout patterns_

---

**[GAMBAR 4.19 - Iconography System]** 🔴 **CRITICAL**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [INSERT ICONOGRAPHY SYSTEM]                              │
│                                                             │
│   CUR-HEART ICON LIBRARY                                   │
│   Consistent Visual Language                               │
│                                                             │
│   ICON STYLE:                                               │
│   • Style: Outline (stroke-based)                           │
│   • Stroke Width: 2px                                       │
│   • Corner Radius: 2px (rounded)                            │
│   • Grid: 24x24px base                                      │
│   • Format: SVG (scalable, crisp)                           │
│                                                             │
│   ICON SIZES:                                               │
│   • XS: 16x16px - Inline text icons                         │
│   • SM: 20x20px - Button icons                              │
│   • MD: 24x24px - Standard (default)                        │
│   • LG: 32x32px - Feature icons                             │
│   • XL: 48x48px - Hero/empty state icons                    │
│                                                             │
│   ICON CATEGORIES (100+ icons):                             │
│                                                             │
│   NAVIGATION (12 icons):                                    │
│   🏠 Home  📋 Dashboard  👤 Profile  ⚙️ Settings            │
│   📅 Calendar  💬 Messages  🔔 Notifications  📊 Reports    │
│   ❓ Help  🚪 Logout  ◀️ Back  ☰ Menu                       │
│                                                             │
│   BOOKING & SERVICES (15 icons):                            │
│   📝 Book  ✅ Confirm  ❌ Cancel  🔄 Reschedule              │
│   🧘 Therapy  💆 Session  🕐 Time  📍 Location              │
│   💰 Payment  💳 Card  🏦 Bank  📄 Receipt                  │
│   ⏱️ Duration  🎯 Service  📞 Contact                       │
│                                                             │
│   USER & PROFILE (10 icons):                                │
│   👤 User  👥 Users  ⭐ Rating  💬 Review                   │
│   📧 Email  📱 Phone  🎂 Birthday  🏥 Medical               │
│   🔐 Security  ✏️ Edit                                      │
│                                                             │
│   STATUS & ACTIONS (15 icons):                              │
│   ✅ Success  ⚠️ Warning  ❌ Error  ℹ️ Info                 │
│   ⏳ Pending  ⏸️ Paused  ▶️ Active  ⏹️ Stopped              │
│   ➕ Add  ➖ Remove  🗑️ Delete  💾 Save                     │
│   📤 Upload  📥 Download  🔍 Search                         │
│                                                             │
│   MEDIA & CONTENT (8 icons):                                │
│   📸 Camera  🎥 Video  🖼️ Image  📂 Folder                  │
│   📄 Document  📊 Chart  📈 Graph  🎨 Design                │
│                                                             │
│   THERAPY SPECIFIC (10 icons):                              │
│   🧠 Mental Health  💭 Thought  😌 Calm  🎯 Focus           │
│   💪 Strength  ❤️ Heart  🌟 Star  ✨ Magic                 │
│   🌈 Progress  🎭 Emotion                                   │
│                                                             │
│   SOCIAL (5 icons):                                         │
│   👍 Like  💬 Comment  📢 Share  🔔 Bell                    │
│   ⚡ Trending                                               │
│                                                             │
│   ICON USAGE GUIDELINES:                                    │
│   • Always pair with text labels (accessibility)            │
│   • Use consistent size within same context                 │
│   • Maintain 2px stroke width for consistency               │
│   • Color: Inherit from parent or use semantic colors       │
│   • Align center with text baseline                         │
│                                                             │
│   ICON LIBRARY:                                             │
│   Primary: Heroicons v2 (Tailwind UI official)             │
│   Secondary: Font Awesome (for additional needs)            │
│   Custom: Therapy-specific icons (10 custom)                │
│                                                             │
│   Format: Icon Library PNG (grid showcase)                 │
│   Recommended size: 2400x2000px                            │
│   Style: Icon grid dengan labels dan sizes                 │
│                                                             │
│   File: assets/images/design-system-iconography.png        │
│   Tool: Figma, Adobe Illustrator, atau icon editor         │
│                                                             │
│   PRIORITY: P2 - HIGH                                       │
│   Must show: All icon categories, sizes, usage examples    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

_Gambar 4.19: Iconography System CUR-HEART dengan 100+ outline icons, 5 sizes (16-48px), organized by categories (Navigation, Booking, User, Status, Media, Therapy-specific, Social)_

---

### 4.3.5.4 Mockup Halaman Public (Public Pages)

Public pages adalah halaman-halaman yang dapat diakses oleh semua pengunjung tanpa perlu login terlebih dahulu. Halaman-halaman ini berfungsi sebagai front-facing website yang memberikan informasi tentang CUR-HEART, layanan yang ditawarkan, dan mendorong pengunjung untuk melakukan booking atau registrasi.

---

**[GAMBAR 4.20 - Mockup: Landing Page (Homepage)]** 📱
_Public page - Hero section, services overview, therapists, testimonials_

**[GAMBAR 4.21 - Mockup: Services List Page]** 📱
_Public page - Grid 6 layanan dengan pricing dan descriptions_

**[GAMBAR 4.22 - Mockup: Service Detail Page]** 📱
_Public page - Detailed service info, benefits, booking CTA_

**[GAMBAR 4.23 - Mockup: Therapists Directory]** 📱
_Public page - Grid therapist profiles dengan filter/search_

**[GAMBAR 4.24 - Mockup: Therapist Profile Detail]** 📱
_Public page - Bio, credentials, specializations, reviews, booking_

**[GAMBAR 4.25 - Mockup: About Us Page]** 📱
_Public page - Company story, values, team, certifications_

**[GAMBAR 4.26 - Mockup: Contact Us Page]** 📱
_Public page - Contact form, location map, social media links_

---

#### A. Landing Page (Homepage)

**Deskripsi:**
Landing page adalah halaman pertama yang dilihat pengunjung ketika mengakses website CUR-HEART. Halaman ini dirancang untuk memberikan kesan pertama yang kuat, profesional, dan menenangkan sesuai dengan nature bisnis hypnotherapy dan kesehatan mental.

**Elemen Utama:**
1. **Hero Section**:
   - Background gradient navy blue to purple yang calming
   - Headline utama: "Transform Your Life Through Professional Hypnotherapy"
   - Subheadline menjelaskan value proposition CUR-HEART
   - Primary CTA button "Book Your Session" (pink, prominent)
   - Secondary CTA button "Learn More About Us"
   - Hero illustration/image terapis yang profesional dan welcoming

2. **Services Overview Section**:
   - Grid layout 3 kolom (desktop) untuk highlight 3 layanan utama
   - Each service card dengan icon, title, short description
   - "View All Services" link di bawah

3. **Why Choose Us Section**:
   - 4 unique selling points dengan icon dan description:
     * Certified Professional Therapists
     * Proven Hypnotherapy Methods
     * Comfortable & Private Sessions
     * Flexible Online & Offline Options
   - Background dengan light purple untuk differentiation

4. **Featured Therapists Section**:
   - Carousel/slider dengan 4 therapist cards
   - Foto, nama, specialization, tahun pengalaman
   - Rating stars
   - "View Profile" button
   - "See All Therapists" CTA

5. **How It Works Section**:
   - 4-step process dengan numbering visual:
     1. Browse & Choose Service
     2. Select Your Therapist
     3. Book Your Session
     4. Start Your Transformation
   - Timeline visual dengan connecting lines
   - Icon untuk setiap step

6. **Testimonials Section**:
   - 3 customer testimonial cards dengan:
     * Client photo/avatar
     * Client name & age
     * Rating stars (5/5)
     * Testimonial text (2-3 kalimat)
   - Carousel navigation untuk more testimonials

7. **Latest Blog Posts**:
   - 3 recent blog posts dalam card format
   - Thumbnail image, title, excerpt, date
   - "Read More" link
   - "View All Articles" button

8. **Call-to-Action Footer Section**:
   - Large banner dengan background pink gradient
   - "Ready to Start Your Journey?"
   - "Book Your First Session Today" button
   - "Or contact us for consultation" alternative

**Interaksi & Behavior:**
- Smooth scroll animation saat navigasi antar section
- Hover effects pada cards dan buttons
- Lazy loading untuk images
- Responsive: Stack sections vertically pada mobile
- Navigation bar sticky/fixed saat scroll

**User Flow:**
Pengunjung → Landing page → Tertarik → Klik "Book Your Session" → Redirect ke Services page (atau login jika sudah punya akun)

---

#### B. About Us Page

**Deskripsi:**
About Us page menjelaskan tentang CUR-HEART sebagai organisasi, visi misi, nilai-nilai yang dipegang, dan tim di balik layanan ini. Halaman ini membangun trust dan credibility.

**Elemen Utama:**
1. **Page Header**:
   - Judul "About CUR-HEART"
   - Breadcrumb: Home > About Us
   - Hero image: Tim terapis atau kantor CUR-HEART

2. **Our Story Section**:
   - Paragraf 3-4 tentang sejarah pendirian CUR-HEART
   - Motivasi founder dalam bidang hypnotherapy
   - Milestone achievements (tahun berdiri, jumlah klien, success rate)

3. **Vision & Mission**:
   - Dua kolom side-by-side
   - Vision di kiri dengan icon
   - Mission di kanan dengan icon
   - Background card dengan subtle shadow

4. **Our Values**:
   - 5 core values dalam grid layout:
     * Professionalism
     * Confidentiality
     * Empathy
     * Excellence
     * Innovation
   - Each value dengan icon dan description

5. **Our Team Section**:
   - Grid 3-4 kolom team member cards
   - Foto professional, name, position, short bio
   - Social media links (LinkedIn, Instagram)
   - Dipisahkan per department: Management, Therapists, Support Staff

6. **Certifications & Partnerships**:
   - Logo-logo sertifikasi professional
   - Partner organizations (jika ada)
   - Awards & recognitions

7. **CTA Section**:
   - "Meet Our Therapists" button
   - "Contact Us for More Info" button

**Interaksi & Behavior:**
- Fade-in animation untuk sections saat scroll
- Hover effect pada team member cards (show social links)
- Responsive grid yang adjust berdasarkan screen size

**User Flow:**
Pengunjung ingin tahu lebih tentang CUR-HEART → About Us page → Baca informasi → Trust building → Klik "Meet Our Therapists" atau "Book Session"

---

#### C. Services Page (Services Catalog)

**Deskripsi:**
Services page menampilkan katalog lengkap semua layanan hypnotherapy yang ditawarkan oleh CUR-HEART. Halaman ini membantu calon klien memahami berbagai opsi layanan dan memilih yang sesuai dengan kebutuhan mereka.

**Elemen Utama:**
1. **Page Header**:
   - Judul "Our Services"
   - Subtitle "Professional Hypnotherapy for Your Wellness"
   - Breadcrumb: Home > Services

2. **Filter & Search Section**:
   - Search bar untuk cari service by keyword
   - Filter dropdown:
     * By Category (Stress Management, Addiction, Phobia, etc.)
     * By Duration (30min, 60min, 90min)
     * By Price Range (slider)
   - Sort options (Popular, Price Low-High, Price High-Low, Name A-Z)

3. **Services Grid**:
   - Card-based layout, 3 kolom desktop, 2 tablet, 1 mobile
   - Each service card contains:
     * Service thumbnail/icon dengan background colored
     * Service name (bold)
     * Category badge
     * Short description (2-3 lines)
     * Duration (e.g., "60 minutes")
     * Price (e.g., "Rp 300.000")
     * Rating (stars + jumlah reviews)
     * "View Details" button

4. **Service Categories**:
   - Total 8-10 services ditampilkan:
     1. Stress & Anxiety Management
     2. Weight Management
     3. Smoking Cessation
     4. Phobia Treatment
     5. Sleep Disorders
     6. Confidence Building
     7. Pain Management
     8. Trauma Healing
     9. Performance Enhancement
     10. Relationship Counseling

5. **Pagination**:
   - Navigation untuk multiple pages jika service > 12
   - "Load More" button sebagai alternatif

6. **CTA Banner**:
   - "Not sure which service is right for you?"
   - "Take our Free Assessment" button
   - "Or chat with our consultant" link

**Interaksi & Behavior:**
- Instant search filtering saat typing
- Smooth animation saat filter diterapkan
- Hover effect pada service cards (scale up, shadow increase)
- Skeleton loading saat data di-fetch

**User Flow:**
Pengunjung → Services page → Browse/filter services → Klik "View Details" pada service yang menarik → Service Detail page

---

#### D. Service Detail Page

**Deskripsi:**
Service Detail page memberikan informasi lengkap dan mendalam tentang satu layanan hypnotherapy spesifik. Halaman ini bertujuan untuk mengedukasi calon klien dan mendorong mereka untuk booking.

**Elemen Utama:**
1. **Page Header**:
   - Service name (H1)
   - Breadcrumb: Home > Services > [Service Name]
   - Hero image/illustration relevan dengan service

2. **Overview Section**:
   - Large icon/image untuk service
   - Price, duration, category
   - Rating & reviews count
   - "Book This Session" primary button (pink, prominent)
   - Quick facts:
     * Session format (Online/Offline/Both)
     * Available languages
     * Typical session count (e.g., "3-5 sessions recommended")

3. **Description Tab Section**:
   - Tabs navigation: Overview | What to Expect | Benefits | FAQ
   - **Overview Tab**:
     * Detailed explanation tentang service (3-4 paragraf)
     * Siapa yang cocok untuk service ini
     * Kondisi yang dapat diatasi
   - **What to Expect Tab**:
     * Step-by-step proses session
     * Preparation yang perlu dilakukan
     * What happens during dan after session
   - **Benefits Tab**:
     * Bullet list manfaat yang akan didapat
     * Expected results timeline
     * Success stories statistics
   - **FAQ Tab**:
     * 5-7 frequently asked questions dengan answers
     * Collapsible accordion format

4. **Recommended Therapists**:
   - "Our Therapists Specialized in This Service"
   - 3-4 therapist cards dengan:
     * Photo, name, experience years
     * Specialization match percentage
     * Available time slots preview
     * "View Profile" dan "Book Now" buttons

5. **Related Services**:
   - "You Might Also Like"
   - 3 related services dalam card format
   - Similar category atau complementary services

6. **Customer Reviews**:
   - Overall rating (4.8/5.0) dengan star visualization
   - Rating breakdown bar chart (5★: 75%, 4★: 20%, dll)
   - Review cards dari klien:
     * Client name (atau anonymous) + photo
     * Rating stars
     * Review text
     * Date
     * Verified badge
   - "Write a Review" button (untuk logged-in users)

7. **Sticky CTA Sidebar** (desktop) atau Bottom Bar (mobile):
   - Price
   - "Book Now" button
   - "Add to Wishlist" icon
   - "Share" icon

**Interaksi & Behavior:**
- Sticky booking CTA saat scroll
- Tabs switching dengan smooth transition
- Accordion animation untuk FAQ
- Lazy load reviews (infinite scroll atau pagination)
- Modal popup saat klik "Book Now" untuk pilih therapist

**User Flow:**
User sudah di Service Detail page → Baca informasi lengkap → Convinced → Klik "Book Now" → Pilih therapist (modal/redirect) → Booking flow

---

#### E. Therapists Directory Page

**Deskripsi:**
Therapists Directory page menampilkan daftar semua terapis yang available di CUR-HEART. Calon klien dapat browse, filter, dan memilih terapis yang sesuai dengan preferensi mereka.

**Elemen Utama:**
1. **Page Header**:
   - Judul "Our Professional Therapists"
   - Subtitle "Meet our certified and experienced hypnotherapists"
   - Breadcrumb: Home > Therapists
   - Hero image: Group photo terapis atau abstract illustration

2. **Search & Filter Section**:
   - Search bar "Search by name or specialization"
   - Filter options:
     * By Specialization (dropdown multi-select)
     * By Experience (0-2 years, 3-5, 5-10, 10+ years)
     * By Rating (4+ stars, 4.5+, 5 only)
     * By Availability (Available Today, This Week)
     * By Language (Indonesian, English, dll)
     * By Gender (Male, Female, Any)
   - "Apply Filters" button
   - Active filters shown as removable pills

3. **Sort Options**:
   - Dropdown: Highest Rated, Most Experienced, Most Booked, Name A-Z

4. **Therapists Grid**:
   - Card layout, 3 kolom desktop
   - Each therapist card:
     * Professional photo (rounded atau square dengan rounded corners)
     * Name (H4)
     * Title/Position (e.g., "Senior Hypnotherapist")
     * Specializations (2-3 badges)
     * Years of experience
     * Rating stars + review count
     * Languages spoken
     * Availability indicator (Available Now/green dot)
     * Price range (e.g., "Rp 250K - 400K")
     * "View Profile" button
     * "Book Session" button (primary)
   - Hover effect: Card shadow elevate, buttons show

5. **Total Count**:
   - "Showing 12 of 25 therapists" dengan pagination

6. **Featured Therapists Banner**:
   - Section khusus untuk highlight 2-3 top rated therapists
   - Larger cards dengan more info
   - "Therapist of the Month" badge

7. **CTA Section**:
   - "Can't decide? Let us help you"
   - "Get Therapist Recommendation" button
   - "Or browse by specialty" links

**Interaksi & Behavior:**
- Real-time search filtering
- Filter results update dengan loading skeleton
- Infinite scroll atau pagination
- Bookmark/favorite therapist (jika logged in)
- Quick view modal saat hover (optional)

**User Flow:**
User → Therapists Directory → Apply filters → Browse cards → Interested in one → Klik "View Profile" → Therapist Profile page

---

#### F. Therapist Profile Page

**Deskripsi:**
Therapist Profile page menampilkan informasi detail tentang seorang terapis, termasuk background, expertise, reviews, dan availability. Ini adalah halaman decision-making sebelum booking.

**Elemen Utama:**
1. **Hero Section**:
   - Large professional photo (kiri)
   - Name (H1)
   - Credentials & titles
   - Specializations badges
   - Rating stars + total reviews
   - Years of experience
   - Languages spoken
   - "Book Session" primary button (prominent)
   - "Send Message" secondary button
   - "Add to Favorite" icon button

2. **Quick Stats**:
   - Total sessions completed
   - Success rate percentage
   - Response time (e.g., "Usually responds in 2 hours")
   - Availability (Available This Week)

3. **About Me Section**:
   - Bio paragraf (3-4 paragraf) tentang:
     * Educational background
     * Professional experience
     * Approach to therapy
     * Personal philosophy

4. **Specializations & Expertise**:
   - List of services/conditions specialized in
   - Progress bars showing proficiency level
   - Certifications dengan badges/icons

5. **Education & Certifications**:
   - Timeline format:
     * Degree, university, year
     * Certifications, issuing body, year
     * Continuing education

6. **Consultation Approach**:
   - Explanation of therapy methodology
   - What makes their approach unique
   - Therapy style (gentle, direct, holistic, etc.)

7. **Services Offered & Pricing**:
   - Table dengan columns: Service Name, Duration, Price
   - 5-8 services yang di-offer
   - "Book" button per service

8. **Availability Calendar**:
   - Weekly calendar view (7 hari ke depan)
   - Time slots displayed dengan status:
     * Available (green)
     * Booked (gray)
     * Break (striped)
   - "View More Dates" untuk expand
   - Quick book: Klik time slot → Booking modal

9. **Client Reviews & Testimonials**:
   - Overall rating dengan star visual
   - Total reviews count
   - Rating distribution (5★: 80%, 4★: 15%, dll)
   - Review cards:
     * Client initial/avatar
     * Rating stars
     * Service taken
     * Review text
     * Date
     * "Helpful" vote count
   - Pagination untuk more reviews
   - Filter reviews by rating atau service

10. **Video Introduction** (optional):
    - Embedded video where therapist introduces themselves
    - Play button overlay

11. **FAQs**:
    - Frequently asked questions specific to this therapist
    - Collapsible accordion

12. **Related Therapists**:
    - "Other Therapists You Might Like"
    - 3 similar therapist cards (same specialization)

13. **Sticky Booking Sidebar** (desktop):
    - Mini profile card
    - Price starting from
    - Next available slot
    - "Book Now" button
    - "Message" button

**Interaksi & Behavior:**
- Sticky booking sidebar saat scroll
- Calendar interactive, klik slot langsung book
- Reviews loadmore/infinite scroll
- Video play dengan lightbox
- Smooth scroll ke sections via navigation

**User Flow:**
User di Therapist Profile → Impressed dengan credentials → Check availability → Klik available time slot → Booking modal opens → Continue booking flow

---

#### G. Blog List Page

**Deskripsi:**
Blog List page menampilkan artikel-artikel edukatif tentang hypnotherapy, kesehatan mental, tips wellness, dan cerita sukses. Ini adalah content marketing untuk SEO dan thought leadership.

**Elemen Utama:**
1. **Page Header**:
   - Title "CUR-HEART Blog"
   - Subtitle "Insights, Tips, and Stories About Mental Wellness"
   - Breadcrumb: Home > Blog

2. **Featured Post**:
   - Large card untuk article terbaru/featured
   - Large thumbnail image
   - Category badge
   - Title (H2)
   - Excerpt (2-3 sentences)
   - Author, date, read time
   - "Read More" button

3. **Search & Filter**:
   - Search bar "Search articles..."
   - Category filter: All, Hypnotherapy, Mental Health, Success Stories, Tips & Tricks, Research, News
   - Tag cloud (popular tags)

4. **Blog Posts Grid**:
   - 2-3 kolom layout
   - Each blog card:
     * Thumbnail image (16:9 aspect ratio)
     * Category badge
     * Title (H3)
     * Excerpt (2 lines, truncated)
     * Author avatar + name
     * Published date
     * Read time (e.g., "5 min read")
     * "Read More" link

5. **Sidebar** (desktop only):
   - Search widget
   - Categories list dengan post count
   - Popular/Recent posts (5 items):
     * Small thumbnail
     * Title
     * Date
   - Newsletter subscription form:
     * Email input
     * "Subscribe" button
   - Social media follow buttons
   - Tags cloud

6. **Pagination**:
   - "Previous" | Page numbers | "Next"
   - Or "Load More" button

7. **Newsletter CTA Section**:
   - "Get Wellness Tips in Your Inbox"
   - Email subscription form
   - "Subscribe Now" button

**Interaksi & Behavior:**
- Search dengan debounce untuk instant filtering
- Category filter dengan smooth transition
- Skeleton loading untuk articles
- Infinite scroll atau traditional pagination
- Hover effect pada blog cards (image zoom)

**User Flow:**
User → Blog page → Browse articles atau search → Klik article yang menarik → Blog Detail page

---

#### H. Blog Detail Page

**Deskripsi:**
Blog Detail page menampilkan artikel lengkap dengan formatting yang readable dan engaging. Halaman ini juga mendorong engagement melalui comments, shares, dan related articles.

**Elemen Utama:**
1. **Article Header**:
   - Category badge
   - Article title (H1, large)
   - Meta info:
     * Author photo + name (link ke author profile)
     * Published date
     * Last updated date (jika ada)
     * Read time (e.g., "8 min read")
   - Social share buttons (Facebook, Twitter, LinkedIn, WhatsApp)
   - Featured image (full width, high quality)

2. **Article Content**:
   - Well-formatted text dengan:
     * Headings (H2, H3, H4)
     * Paragraphs dengan proper spacing
     * Bold, italic, lists
     * Blockquotes untuk highlights
     * Images dengan captions
     * Video embeds (jika ada)
     * Code blocks (jika technical article)
   - Table of contents (untuk long articles):
     * Sticky sidebar dengan links ke sections
     * Scroll spy highlight current section

3. **Author Bio Box**:
   - Author photo
   - Name + title
   - Short bio (2-3 sentences)
   - "View all posts by [Author]" link
   - Social media links

4. **Tags**:
   - Clickable tags for article categorization
   - Link ke tag archive pages

5. **Engagement Section**:
   - Like/Heart button dengan count
   - Bookmark button
   - Share count

6. **Comments Section**:
   - "Leave a Comment" heading
   - Comment form (untuk logged-in users):
     * Textarea for comment
     * "Post Comment" button
   - Existing comments list:
     * Commenter avatar + name
     * Comment text
     * Date
     * Reply button
     * Nested replies (1 level)
   - Pagination untuk comments
   - Moderation notice

7. **Related Articles**:
   - "You May Also Like"
   - 3 related articles dalam card format
   - Based on category atau tags
   - "View All Articles" link

8. **Newsletter CTA**:
   - "Want More Content Like This?"
   - Email subscription form
   - "Subscribe to Our Newsletter" button

9. **Sticky Social Share Bar** (side):
   - Fixed position di kiri artikel (desktop)
   - Share count
   - Icons for: Facebook, Twitter, LinkedIn, Copy Link

**Interaksi & Behavior:**
- Sticky table of contents dengan smooth scroll
- Lazy load images dalam artikel
- Code syntax highlighting (jika ada code blocks)
- Social share dengan popup atau native share API
- Comment submission dengan AJAX
- Reading progress bar di top

**User Flow:**
User membaca artikel → Engaged → Like/comment → Klik related article atau CTA "Book Session" (jika ada)

---

### 4.3.5.5 Mockup Halaman Support (Support Pages)

Support pages adalah halaman-halaman pendukung yang memberikan informasi penting terkait kontak, FAQ, kebijakan privasi, dan syarat & ketentuan. Halaman ini penting untuk transparency, compliance, dan customer service.

#### A. Contact Us Page

**Deskripsi:**
Contact Us page menyediakan berbagai cara untuk menghubungi CUR-HEART, termasuk form kontak, alamat kantor, nomor telepon, email, dan social media. Halaman ini penting untuk customer support dan inquiry.

**Elemen Utama:**
1. **Page Header**:
   - Title "Contact Us"
   - Subtitle "We'd Love to Hear from You"
   - Breadcrumb: Home > Contact

2. **Contact Form Section**:
   - Form fields:
     * Full Name (required)
     * Email Address (required)
     * Phone Number (optional)
     * Subject (dropdown: General Inquiry, Booking Help, Technical Support, Partnership, Other)
     * Message (textarea, required)
     * "Send Message" button (primary)
   - Form validation dengan error messages
   - Success notification setelah submit

3. **Contact Information Cards**:
   - 3 cards side-by-side:
     * **Location**: Icon map-marker, alamat lengkap, link "Get Directions" ke Google Maps
     * **Phone**: Icon phone, nomor telepon, "Call Us Now" link (tel:)
     * **Email**: Icon envelope, email address, "Send Email" link (mailto:)

4. **Business Hours**:
   - Table format atau list:
     * Senin - Jumat: 08:00 - 20:00
     * Sabtu: 09:00 - 18:00
     * Minggu: 10:00 - 16:00
   - Note tentang emergency contact

5. **Google Maps Embed**:
   - Interactive map showing CUR-HEART office location
   - Markers, zoom controls
   - Full height (400-500px)

6. **Social Media Links**:
   - "Follow Us On Social Media"
   - Large icon buttons untuk:
     * Instagram
     * Facebook
     * LinkedIn
     * Twitter/X
     * YouTube
     * TikTok

7. **FAQ Shortcut**:
   - "Looking for Quick Answers?"
   - "Visit Our FAQ Page" button
   - Preview 3 most common questions

8. **Alternative Contact Methods**:
   - WhatsApp chat button (floating)
   - Live chat widget (bottom-right)
   - "Schedule a Call Back" option

**Interaksi & Behavior:**
- Form validation real-time
- Success/error toast notifications
- Map interactive (zoom, pan)
- Click to call/email pada mobile
- Floating WhatsApp button

**User Flow:**
User punya pertanyaan → Contact page → Fill form atau pilih contact method → Submit → Receive confirmation

---

#### B. FAQ Page

**Deskripsi:**
FAQ page menjawab pertanyaan-pertanyaan yang sering ditanyakan oleh calon klien dan klien existing. Halaman ini mengurangi beban customer service dan membantu users menemukan jawaban dengan cepat.

**Elemen Utama:**
1. **Page Header**:
   - Title "Frequently Asked Questions"
   - Subtitle "Find answers to common questions"
   - Breadcrumb: Home > FAQ

2. **Search Bar**:
   - "Search for answers..." dengan icon search
   - Real-time search filtering
   - "Popular searches" suggestions

3. **Category Tabs**:
   - Horizontal tabs untuk kategorisasi:
     * General (default)
     * Booking & Appointments
     * Payments & Pricing
     * Sessions & Therapy
     * Account & Privacy
     * Technical Support
   - Active tab highlighted

4. **FAQ Accordion List**:
   - Per kategori, 8-12 pertanyaan
   - Accordion format:
     * Question sebagai header (H4)
     * Answer tersembunyi, expand on click
     * Smooth animation (slide down/up)
     * Icon arrow/chevron (up/down state)
   - Answers formatted dengan:
     * Paragraphs
     * Bullet lists
     * Bold untuk emphasis
     * Links ke relevant pages

5. **Sample FAQs**:
   - **General**:
     * "What is hypnotherapy and how does it work?"
     * "Is hypnotherapy safe?"
     * "How many sessions will I need?"
   - **Booking**:
     * "How do I book a session?"
     * "Can I cancel or reschedule?"
     * "What if I'm late for my appointment?"
   - **Payments**:
     * "What payment methods do you accept?"
     * "Do you offer refunds?"
     * "Is there a consultation fee?"
   - **Sessions**:
     * "What should I prepare before a session?"
     * "Can I do sessions online?"
     * "Will I be conscious during hypnotherapy?"

6. **Quick Actions**:
   - Sidebar (desktop) atau bottom section (mobile):
     * "Still have questions?"
     * "Contact Support" button
     * "Schedule a Consultation" button
     * "Browse Services" link

7. **Feedback Section**:
   - "Was this helpful?" thumbs up/down
   - Per FAQ item
   - Thank you message setelah feedback

8. **Related Resources**:
   - Links ke:
     * Getting Started Guide
     * How to Prepare for Your First Session
     * Understanding Hypnotherapy (blog article)

**Interaksi & Behavior:**
- Accordion one-at-a-time atau multiple open
- Search highlights matching text
- Smooth scroll ke section jika dari link eksternal
- "Was this helpful" voting dengan AJAX
- Deep linking untuk specific FAQs

**User Flow:**
User punya pertanyaan → FAQ page → Search atau browse category → Find answer → Solved atau klik "Contact Support"

---

#### C. Privacy Policy Page

**Deskripsi:**
Privacy Policy page menjelaskan bagaimana CUR-HEART mengumpulkan, menggunakan, menyimpan, dan melindungi data pribadi users. Halaman ini penting untuk compliance dengan regulasi (GDPR, Indonesia's data protection laws) dan membangun trust.

**Elemen Utama:**
1. **Page Header**:
   - Title "Privacy Policy"
   - Last updated date: "Last Updated: October 28, 2024"
   - Breadcrumb: Home > Privacy Policy

2. **Table of Contents**:
   - Sticky sidebar (desktop) dengan links ke sections:
     1. Introduction
     2. Information We Collect
     3. How We Use Your Information
     4. Information Sharing and Disclosure
     5. Data Security
     6. Your Rights and Choices
     7. Cookies and Tracking Technologies
     8. Third-Party Services
     9. Children's Privacy
     10. Changes to This Policy
     11. Contact Us
   - Scroll spy untuk highlight current section

3. **Content Sections**:
   - **1. Introduction**:
     * Welcome statement
     * Scope of policy
     * Consent agreement
   
   - **2. Information We Collect**:
     * Personal Information (name, email, phone, address)
     * Health Information (therapy notes, medical history) - emphasized as sensitive
     * Account Information (username, password)
     * Payment Information (credit card, billing address)
     * Usage Data (IP address, browser, device info)
     * Cookies and tracking data
   
   - **3. How We Use Your Information**:
     * Bullet list purposes:
       - Provide therapy services
       - Process bookings and payments
       - Communicate with clients
       - Improve our services
       - Marketing (with consent)
       - Legal compliance
   
   - **4. Information Sharing**:
     * Who we share with:
       - Therapists (only relevant info)
       - Payment processors
       - Service providers (hosting, analytics)
       - Legal authorities (if required)
     * We DO NOT sell personal data
   
   - **5. Data Security**:
     * Encryption (SSL/TLS)
     * Secure servers
     * Access controls
     * Regular security audits
     * Data breach notification procedures
   
   - **6. Your Rights**:
     * Access your data
     * Correct inaccuracies
     * Delete your data (right to be forgotten)
     * Export your data
     * Withdraw consent
     * Opt-out marketing
     * How to exercise rights
   
   - **7. Cookies**:
     * Types of cookies used
     * Purpose of each
     * How to manage cookies
   
   - **8. Third-Party Services**:
     * Google Analytics
     * Payment gateways (Midtrans)
     * Video conferencing (for online sessions)
     * Social media plugins
   
   - **9. Children's Privacy**:
     * Minimum age requirement (13 or 18)
     * Parental consent needed
   
   - **10. Policy Changes**:
     * How users will be notified
     * Effective date of changes
   
   - **11. Contact**:
     * Data protection officer contact
     * Email for privacy concerns

4. **Highlight Boxes**:
   - Important notes dalam colored boxes
   - Example: "Your health information is highly confidential and protected under [relevant law]"

5. **CTA Section**:
   - "Have Questions About Your Privacy?"
   - "Contact Our Privacy Team" button

**Interaksi & Behavior:**
- Long-form scrollable content
- Sticky TOC untuk easy navigation
- Smooth scroll dengan offset untuk header
- Print-friendly CSS
- Download as PDF option

**User Flow:**
User concerned about privacy → Privacy Policy → Read relevant sections → Assured atau contact privacy team

---

#### D. Terms & Conditions Page

**Deskripsi:**
Terms & Conditions page menetapkan aturan hukum, kewajiban, dan hak antara CUR-HEART dan users. Halaman ini melindungi kedua belah pihak dan menetapkan expectations untuk penggunaan layanan.

**Elemen Utama:**
1. **Page Header**:
   - Title "Terms and Conditions"
   - Last updated date
   - Breadcrumb: Home > Terms & Conditions

2. **Table of Contents**:
   - Sticky sidebar dengan links:
     1. Acceptance of Terms
     2. Description of Services
     3. User Account and Registration
     4. Booking and Appointments
     5. Payments, Fees, and Refunds
     6. Cancellation and Rescheduling Policy
     7. User Conduct and Responsibilities
     8. Therapist-Client Relationship
     9. Confidentiality and Privacy
     10. Intellectual Property Rights
     11. Disclaimers and Limitations of Liability
     12. Indemnification
     13. Termination
     14. Dispute Resolution
     15. Governing Law
     16. Changes to Terms
     17. Contact Information

3. **Content Sections**:
   - **1. Acceptance**:
     * By using service, you agree to terms
     * Must be 18+ or have parental consent
     * Continued use = continued agreement
   
   - **2. Services Description**:
     * What CUR-HEART provides
     * Online and offline hypnotherapy sessions
     * Booking platform
     * Not emergency medical services
   
   - **3. Account Registration**:
     * Requirement untuk booking
     * Accurate information obligation
     * Account security responsibility
     * One account per person
   
   - **4. Booking**:
     * How to book
     * Confirmation process
     * Session formats (online/offline)
     * Minimum age requirements
   
   - **5. Payments**:
     * Accepted payment methods
     * Payment timing (before session)
     * Currency (IDR)
     * No refunds policy (with exceptions)
     * Promotional code terms
   
   - **6. Cancellation Policy**:
     * Client cancellation:
       - 24+ hours before: Full refund/reschedule
       - 12-24 hours: 50% charge
       - <12 hours: No refund
     * Therapist cancellation: Full refund atau reschedule
     * No-show policy
   
   - **7. User Conduct**:
     * Prohibited activities:
       - False information
       - Harassment
       - Spam
       - Illegal use
     * Consequences of violation
   
   - **8. Therapist-Client Relationship**:
     * Professional boundaries
     * Not substitute for medical treatment
     * Emergency situations handling
     * Independent contractor status of therapists
   
   - **9. Confidentiality**:
     * Session confidentiality
     * Exceptions (harm to self/others, legal requirement)
     * Reference to Privacy Policy
   
   - **10. Intellectual Property**:
     * CUR-HEART owns website content
     * User license to use
     * Restrictions on copying/reproducing
     * Trademark usage
   
   - **11. Disclaimers**:
     * Service provided "as is"
     * No guarantee of results
     * Not medical advice
     * Third-party links disclaimer
   
   - **12. Limitation of Liability**:
     * Maximum liability limit
     * No liability for indirect damages
     * Force majeure
   
   - **13. Indemnification**:
     * User agrees to indemnify CUR-HEART
     * From claims arising from user's use
   
   - **14. Termination**:
     * CUR-HEART can terminate accounts
     * User can close account anytime
     * Effect of termination
   
   - **15. Dispute Resolution**:
     * Good faith negotiation first
     * Mediation/arbitration
     * Jurisdiction
   
   - **16. Governing Law**:
     * Indonesian law applies
     * Jurisdiction in specific courts
   
   - **17. Changes to Terms**:
     * Right to modify
     * Notification method
     * Effective date
   
   - **18. Contact**:
     * For questions about terms
     * Legal department email

4. **Important Callouts**:
   - Highlighted boxes untuk key terms
   - Example: "IMPORTANT: Sessions must be paid in full before confirmation"

5. **Acknowledgment Section**:
   - Checkbox: "I have read and agree to the Terms and Conditions"
   - Required saat registration atau first booking

**Interaksi & Behavior:**
- Similar to Privacy Policy
- Sticky TOC navigation
- Smooth scrolling
- Print/download options
- Highlight search terms (if coming from search)

**User Flow:**
User registering/booking → Required to accept terms → Click link → Terms page → Read atau scroll to bottom → Accept checkbox → Continue with registration/booking

---

### 4.3.5.6 Mockup Halaman Authentication (Authentication Pages)

Authentication pages adalah halaman-halaman yang menangani proses login, registrasi, dan password recovery. Desain authentication pages harus balance antara security, usability, dan user experience yang smooth.

---

**[GAMBAR 4.27 - Mockup: Login Page]** 🔐
_Auth page - Email/password form, remember me, forgot password link_

**[GAMBAR 4.28 - Mockup: Register Page]** 🔐
_Auth page - Multi-step registration form, terms acceptance_

**[GAMBAR 4.29 - Mockup: Forgot Password Page]** 🔐
_Auth page - Email input for password reset link_

**[GAMBAR 4.30 - Mockup: Reset Password Page]** 🔐
_Auth page - New password form with confirmation_

---

#### A. Login Page

**Deskripsi:**
Login page memungkinkan existing users untuk masuk ke akun mereka dan mengakses dashboard serta fitur-fitur yang memerlukan authentication. Halaman ini harus simple, clear, dan secure.

**Elemen Utama:**
1. **Layout**:
   - Split screen layout (desktop):
     * Kiri (40%): Illustration/image tentang mental wellness, calming visuals
     * Kanan (60%): Login form
   - Single column (mobile): Form only, dengan logo di top

2. **Branding**:
   - CUR-HEART logo di top-center atau top-left
   - Tagline (optional): "Welcome Back to Your Wellness Journey"

3. **Login Form**:
   - Form title: "Log In to Your Account"
   - Input fields:
     * **Email/Username**: 
       - Placeholder "Enter your email address"
       - Email icon prefix
       - Validation: Required, valid email format
     * **Password**:
       - Placeholder "Enter your password"
       - Lock icon prefix
       - Show/hide password toggle (eye icon)
       - Validation: Required, min 6 characters
   - "Remember Me" checkbox
   - "Forgot Password?" link (aligned right)
   - **"Log In" button** (primary, full width, pink)
   - Loading state pada button saat submit

4. **Alternative Login Methods**:
   - Divider: "Or continue with"
   - Social login buttons:
     * Google login button
     * Facebook login button
   - Single Sign-On appearance dengan brand colors

5. **Registration Prompt**:
   - Text: "Don't have an account?"
   - "Sign Up" link (colored, bold)

6. **Security & Trust Indicators**:
   - SSL lock icon dengan text "Secure Login"
   - Privacy policy link di footer

7. **Error Handling**:
   - Error messages muncul di atas form atau per field:
     * "Invalid email or password"
     * "Please enter a valid email address"
     * "This field is required"
   - Red border pada field yang error
   - Error icon

8. **Success State**:
   - Loading spinner saat authenticating
   - "Logging you in..." message
   - Redirect ke dashboard setelah sukses

**Interaksi & Behavior:**
- Real-time validation saat blur (kehilangan focus)
- Submit validation on button click
- Enter key submit form
- Tab navigation antar fields
- Show/hide password toggle animation
- Social login popups atau OAuth flow
- Session timeout warning (jika dari expired session)

**User Flow:**
User → Login page → Enter credentials → Click "Log In" → Authentication → Redirect to Dashboard (role-based: client/therapist/admin)

**Security Features:**
- Password not stored in plaintext (backend)
- CSRF token protection
- Rate limiting untuk prevent brute force
- Captcha after multiple failed attempts
- Secure password transmission (HTTPS)

---

#### B. Register Page

**Deskripsi:**
Register page memungkinkan new users untuk membuat akun CUR-HEART. Halaman ini harus jelas dalam membedakan tipe user (Client vs Therapist) dan mengumpulkan informasi yang diperlukan tanpa overwhelming user.

**Elemen Utama:**
1. **Layout**:
   - Similar split screen dengan Login page
   - Left: Welcoming illustration "Start Your Wellness Journey"
   - Right: Registration form

2. **Branding & Header**:
   - CUR-HEART logo
   - Title: "Create Your Account"
   - Subtitle: "Join thousands who've found their peace"

3. **User Type Selection** (Step 0):
   - "I want to register as..."
   - Two large option cards:
     * **Client Card**:
       - Icon: User avatar
       - Title: "I'm seeking therapy"
       - Description: "Book sessions with certified therapists"
       - Radio button atau card selection
     * **Therapist Card**:
       - Icon: Professional avatar
       - Title: "I'm a therapist"
       - Description: "Join our network of professionals"
       - Radio button atau card selection
   - Selected card highlighted (pink border, background)
   - "Continue" button (disabled until selection)

4. **Registration Form** (After type selection):
   
   **For Clients**:
   - **Personal Information**:
     * Full Name (required)
     * Email Address (required, unique)
     * Phone Number (required, with country code dropdown)
     * Date of Birth (date picker)
     * Gender (dropdown: Male, Female, Other, Prefer not to say)
   
   - **Account Security**:
     * Password (required, min 8 characters)
       - Password strength indicator (weak/medium/strong)
       - Requirements list:
         * At least 8 characters
         * One uppercase letter
         * One number
         * One special character
     * Confirm Password (required, must match)
   
   - **Preferences** (optional):
     * Preferred Language (dropdown)
     * How did you hear about us? (dropdown)
   
   **For Therapists** (Additional fields):
   - License Number (required)
   - Specialization (multi-select)
   - Years of Experience (number input)
   - Upload License/Certificate (file upload)
   - Professional Bio (textarea, 200 words max)
   - Note: "Your application will be reviewed by our team"

5. **Terms & Conditions**:
   - Checkbox: "I agree to the Terms & Conditions and Privacy Policy"
   - Links clickable, open in new tab atau modal
   - Required untuk enable submit button

6. **Submit Button**:
   - "Create Account" (primary, full width)
   - Disabled until all required fields valid dan T&C accepted
   - Loading state dengan spinner

7. **Login Prompt**:
   - "Already have an account?"
   - "Log In" link

8. **Trust Indicators**:
   - "Your information is secure and confidential"
   - SSL badge
   - "No spam, unsubscribe anytime"

**Validation & Error Handling**:
- Real-time validation untuk each field
- Email uniqueness check (backend)
- Password strength meter visual (red/yellow/green)
- Inline error messages dengan clear instructions
- Success icons untuk valid fields (green checkmark)

**Success Flow**:
- **For Clients**:
  * Account created instantly
  * "Welcome!" success message
  * Email verification sent
  * Redirect to onboarding/dashboard
  * Welcome email sent

- **For Therapists**:
  * Application submitted
  * "Thank you! We'll review your application" message
  * Email notification sent
  * "You'll hear from us within 2-3 business days"
  * Redirect to pending status page

**Interaksi & Behavior:**
- Progressive disclosure (show form after type selection)
- Smooth transition between steps
- Password strength meter updates real-time
- Field validation on blur atau on submit
- File upload dengan drag & drop support
- Mobile-optimized form (larger inputs, picker-friendly)

**User Flow:**
User → Register page → Select user type (Client/Therapist) → Fill form → Accept T&C → Submit → Verification email sent → Success message → Redirect

---

#### C. Forgot Password Page

**Deskripsi:**
Forgot Password page membantu users yang lupa password mereka untuk melakukan password reset melalui email verification. Proses harus secure namun user-friendly.

**Elemen Utama:**
1. **Layout**:
   - Centered form layout (simple, focused)
   - Minimal distractions
   - Max width: 400px

2. **Header**:
   - CUR-HEART logo (clickable, return to home)
   - Icon: Lock with question mark atau key icon
   - Title: "Forgot Your Password?"
   - Subtitle: "No worries, we'll send you reset instructions"

3. **Email Input Form**:
   - Label: "Email Address"
   - Input field:
     * Placeholder: "Enter your registered email"
     * Email icon prefix
     * Validation: Required, valid email format
   - Helper text: "Enter the email address associated with your account"

4. **Submit Button**:
   - "Send Reset Link" (primary, full width)
   - Loading state: "Sending..."

5. **Back to Login**:
   - "← Back to Login" link
   - Returns to Login page

6. **Success State**:
   - Success icon (checkmark dalam circle)
   - Message: "Reset Link Sent!"
   - Instructions: "We've sent a password reset link to [email]. Please check your inbox and follow the instructions."
   - Note: "Didn't receive the email? Check your spam folder or click to resend"
   - "Resend Link" button (disabled for 60 seconds, countdown)
   - "Back to Login" button

7. **Error State**:
   - Error message: "Email address not found"
   - Suggestion: "Please check your email or Sign Up if you don't have an account"
   - "Try Again" atau clear field

8. **Security Features**:
   - Rate limiting (max 3 requests per email per hour)
   - Generic success message (don't reveal if email exists - security)
   - Token expiration (reset link valid for 1 hour)

**Interaksi & Behavior:**
- Simple, single-purpose page
- Auto-focus pada email input
- Submit on Enter key
- Clear error messages
- Countdown timer untuk resend button
- Email validation visual feedback

**User Flow:**
User forgot password → Click "Forgot Password" from Login → Enter email → Submit → Check email → Click reset link → Redirect to Reset Password page

---

#### D. Reset Password Page

**Deskripsi:**
Reset Password page adalah halaman yang dibuka dari link di email reset password. User dapat memasukkan password baru dan mengkonfirmasinya. Halaman ini harus secure dan memberikan feedback yang jelas.

**Elemen Utama:**
1. **Layout**:
   - Centered form, simple
   - Max width: 400px

2. **Header**:
   - CUR-HEART logo
   - Icon: Lock dengan checkmark atau key icon
   - Title: "Reset Your Password"
   - Subtitle: "Enter your new password below"

3. **Token Validation**:
   - Automatic validation saat page load
   - If valid: Show form
   - If expired/invalid:
     * Error message: "This reset link has expired or is invalid"
     * "Request New Link" button
     * Redirect to Forgot Password page

4. **Reset Password Form**:
   - **New Password Field**:
     * Label: "New Password"
     * Input dengan show/hide toggle
     * Password strength indicator
     * Requirements checklist (live update):
       - ✓ At least 8 characters
       - ✓ One uppercase letter
       - ✓ One lowercase letter
       - ✓ One number
       - ✓ One special character
   
   - **Confirm Password Field**:
     * Label: "Confirm New Password"
     * Input dengan show/hide toggle
     * Real-time match validation
     * Error: "Passwords do not match"

5. **Submit Button**:
   - "Reset Password" (primary, full width)
   - Disabled until all requirements met
   - Loading state

6. **Security Indicators**:
   - "For your security, this link will expire in [countdown: 58:32]"
   - "Your password will be encrypted and stored securely"

7. **Success State**:
   - Success icon (large checkmark)
   - Message: "Password Reset Successfully!"
   - "Your password has been updated. You can now log in with your new password."
   - "Go to Login" button (primary)
   - Auto-redirect after 5 seconds dengan countdown

8. **Error Handling**:
   - Server errors (network issues)
   - Token expired during submission
   - Password doesn't meet requirements
   - Clear error messages dengan suggested actions

**Interaksi & Behavior:**
- Password strength meter real-time
- Requirements checklist dengan checkmarks
- Confirm password match indicator
- Token countdown timer
- Expire warning (e.g., "Only 5 minutes left!")
- Auto-redirect setelah success
- One-time use token (invalid after successful reset)

**User Flow:**
User → Click reset link from email → Token validated → Enter new password → Confirm password → Submit → Success → Redirect to Login → Log in dengan new password

**Security Features:**
- Token-based reset (secure, time-limited)
- Password complexity enforcement
- One-time use tokens
- HTTPS transmission
- CSRF protection
- Rate limiting
- Old password cannot be reused (optional)

---

### 4.3.5.7 Mockup Client Dashboard (Client Dashboard Pages)

Client Dashboard adalah area setelah login khusus untuk klien yang telah terdaftar. Dashboard ini memungkinkan klien untuk booking sessions, manage appointments, track progress, dan berkomunikasi dengan terapis.

---

**[GAMBAR 4.31 - Mockup: Client Dashboard Main]** 👤
_Client dashboard - Overview cards, upcoming appointments, quick actions_

**[GAMBAR 4.32 - Mockup: Client Book Service Page]** 👤
_Client - Select service, therapist, date/time, payment_

**[GAMBAR 4.33 - Mockup: Client Appointments List]** 👤
_Client - Table/cards of all bookings dengan status dan actions_

**[GAMBAR 4.34 - Mockup: Client Appointment Detail]** 👤
_Client - Full booking details, reschedule/cancel options_

**[GAMBAR 4.35 - Mockup: Client Payment Page]** 👤
_Client - Payment gateway integration, proof upload_

**[GAMBAR 4.36 - Mockup: Client Therapy Notes View]** 👤
_Client - Read-only view of session notes from therapist_

**[GAMBAR 4.37 - Mockup: Client Progress Tracking]** 👤
_Client - Charts showing anxiety, confidence, sleep quality metrics_

**[GAMBAR 4.38 - Mockup: Client Messages/Chat]** 👤
_Client - Chat interface with therapist_

**[GAMBAR 4.39 - Mockup: Client Profile Settings]** 👤
_Client - Edit personal info, emergency contact, preferences_

**[GAMBAR 4.40 - Mockup: Client Reviews Page]** 👤
_Client - Submit/edit reviews and ratings for therapist_

---

#### A. Client Dashboard (Main)

**Deskripsi:**
Client Dashboard Main adalah landing page setelah client login. Halaman ini memberikan overview dari status appointments, progress, dan quick actions untuk booking sessions.

**Elemen Utama:**
1. **Top Navigation Bar**:
   - Logo CUR-HEART (kiri)
   - Navigation menu items:
     * Dashboard (active)
     * Book Session
     * My Appointments
     * My Progress
     * Messages
   - Right side:
     * Notification bell icon (with badge count)
     * User avatar dengan dropdown:
       - My Profile
       - Settings
       - Help & Support
       - Log Out

2. **Sidebar Navigation** (Desktop):
   - Fixed left sidebar, width 260px
   - Menu items dengan icons:
     * Dashboard (home icon) - active
     * Book Session (calendar-plus icon)
     * My Appointments (calendar icon)
     * My Progress (chart icon)
     * Messages (message icon)
     * Profile (user icon)
     * Settings (gear icon)
   - Collapse button (hamburger)

3. **Welcome Section**:
   - Greeting: "Welcome back, [Client Name]!"
   - Subtitle: "How are you feeling today?"
   - Current date & time

4. **Quick Stats Cards** (4 cards in row):
   - **Upcoming Sessions**:
     * Large number: "2"
     * Icon: Calendar
     * Link: "View All"
   
   - **Completed Sessions**:
     * Number: "8"
     * Icon: Checkmark
     * Progress text: "+2 this month"
   
   - **Hours Spent**:
     * Number: "12.5"
     * Icon: Clock
     * Unit: "hours"
   
   - **Progress Score**:
     * Number: "78%"
     * Icon: Trend up
     * Change: "+5% from last month"

5. **Next Appointment Card** (Featured):
   - Large card dengan highlight
   - "Your Next Session"
   - Therapist photo + name
   - Service name: "Stress & Anxiety Management"
   - Date & time: "Today, 3:00 PM" (dengan countdown jika hari ini)
   - Duration: "60 minutes"
   - Session type: "Online" (badge)
   - Action buttons:
     * "Join Session" (primary, if within 15 min)
     * "View Details" (secondary)
     * "Reschedule" link

6. **Quick Actions Section**:
   - Title: "Quick Actions"
   - 3 action cards:
     * **Book New Session**:
       - Icon: Calendar plus
       - Description: "Schedule your next appointment"
       - Button: "Book Now"
     
     * **Message Therapist**:
       - Icon: Message
       - Description: "Chat with your therapist"
       - Button: "Open Chat"
     
     * **View Progress**:
       - Icon: Chart
       - Description: "Track your wellness journey"
       - Button: "See Progress"

7. **Upcoming Appointments List**:
   - Title: "Upcoming Appointments"
   - List of next 3-4 appointments
   - Each item:
     * Date badge (vertical: Month + Day)
     * Time
     * Therapist avatar + name
     * Service name
     * Status badge (Confirmed, Pending Payment)
     * Quick actions: View | Reschedule | Cancel
   - "View All Appointments" link at bottom

8. **Progress Overview Widget**:
   - Title: "Your Progress This Month"
   - Simple line chart atau progress bars:
     * Mood score trend
     * Session attendance
     * Goal completion
   - "View Detailed Report" link

9. **Recent Messages**:
   - Title: "Recent Messages"
   - 2-3 recent message threads
   - Each:
     * Therapist avatar
     * Name
     * Last message preview (truncated)
     * Timestamp
     * Unread badge (jika ada)
   - "View All Messages" link

10. **Helpful Resources Section**:
    - "Resources for You"
    - 2-3 cards:
      * Blog articles
      * Video tutorials
      * Self-help guides
    - "Browse All Resources" link

**Interaksi & Behavior:**
- Real-time updates (WebSocket untuk notifications)
- Countdown timer untuk next session
- Hover effects pada cards
- Skeleton loading untuk async data
- Responsive: Collapse sidebar on mobile, bottom nav bar
- Refresh button untuk manual data update

**User Flow:**
Client login → Dashboard → Overview semua data → Quick actions atau navigate ke specific sections

---

#### B. Booking Step 1 - Select Service

**Deskripsi:**
Step pertama dalam booking flow di mana client memilih layanan hypnotherapy yang ingin mereka book. Halaman ini harus memudahkan browsing dan comparison antar services.

**Elemen Utama:**
1. **Progress Indicator**:
   - Stepper di top showing 4 steps:
     * Step 1: Select Service (active, highlighted)
     * Step 2: Choose Therapist (inactive)
     * Step 3: Select Date & Time (inactive)
     * Step 4: Confirm & Pay (inactive)
   - Visual connection lines antara steps

2. **Page Header**:
   - Title: "Book Your Session"
   - Breadcrumb: Dashboard > Book Session > Select Service

3. **Search & Filter Section**:
   - Search bar: "Search services..."
   - Filter dropdowns:
     * Category (All, Stress, Addiction, Phobia, etc.)
     * Duration (Any, 30min, 60min, 90min)
     * Price Range (slider: Rp 0 - Rp 500K)
   - "Clear Filters" link

4. **Services Grid**:
   - 2-3 columns layout
   - Each service card:
     * Service icon/illustration
     * Service name (H3)
     * Category badge
     * Short description (2-3 lines)
     * Duration badge (e.g., "60 min")
     * Price (prominent): "Rp 300.000"
     * Rating stars + reviews count
     * "View Details" link (expand modal atau accordion)
     * **"Select" button** (primary)
   
   - Selected state:
     * Card highlighted dengan pink border
     * Checkmark icon
     * "Selected" badge
     * Button changes to "Change"

5. **Service Details Modal/Accordion**:
   - Expanded info saat "View Details":
     * Full description
     * What's included
     * Benefits
     * Recommended sessions count
     * Therapist specialization needed
     * FAQs for this service

6. **Popular Services Highlight**:
   - "Most Popular" badge on top services
   - "Recommended for You" section based on profile

7. **Help Section**:
   - Sidebar atau floating button:
     * "Not sure which service?"
     * "Take Assessment" button
     * "Chat with Consultant" button

8. **Navigation**:
   - "Back to Dashboard" link
   - **"Continue" button** (bottom-right, sticky):
     * Disabled until service selected
     * Shows selected service name saat enabled
     * Click → Go to Step 2

**Interaksi & Behavior:**
- Single selection (radio button behavior)
- Filter results real-time
- Search dengan debounce
- Card selection dengan visual feedback
- Modal/accordion smooth animation
- Mobile: Stack cards vertically, sticky continue button

**User Flow:**
Client → Book Session → Step 1 → Browse services → Select one → Click "Continue" → Step 2

---

#### C. Booking Step 2 - Choose Therapist

**Deskripsi:**
Step kedua di mana client memilih therapist yang akan melakukan session. Halaman ini memfilter therapist berdasarkan specialization dari service yang dipilih di Step 1.

**Elemen Utama:**
1. **Progress Stepper**:
   - Step 1: ✓ Select Service (completed, green checkmark)
   - Step 2: Choose Therapist (active)
   - Step 3: Select Date & Time (inactive)
   - Step 4: Confirm & Pay (inactive)

2. **Selected Service Display**:
   - Sticky top bar atau card:
     * Service name
     * Price, duration
     * "Change Service" link (back to Step 1)

3. **Filter & Sort Section**:
   - **Filters**:
     * Gender preference (Any, Male, Female)
     * Experience (0-3 years, 3-5, 5-10, 10+)
     * Rating (4+ stars, 4.5+, 5 only)
     * Availability (Available Today, This Week, Specific Date)
     * Language (Indonesian, English, etc.)
     * Price Range (show therapist consultation fee)
   
   - **Sort**:
     * Dropdown: Recommended, Highest Rated, Most Experienced, Available Soonest, Price Low-High

4. **Therapists List**:
   - Card layout, vertical list atau grid
   - Each therapist card:
     * Profile photo (large, professional)
     * Name (H3)
     * Title/Credentials (e.g., "Clinical Hypnotherapist, CHT")
     * Specializations tags (2-3 main)
     * Years of experience
     * Rating stars + reviews count
     * Languages spoken
     * Session count completed
     * **Availability indicator**:
       - "Available Today" (green badge)
       - "Next available: Tomorrow" (orange)
       - "Book in Advance" (gray)
     * **Price**: "From Rp 250K per session"
     * **"View Profile" link** (opens modal atau new page)
     * **"Select Therapist" button** (primary)

5. **Therapist Profile Modal**:
   - Quick view modal saat "View Profile":
     * Full photo
     * Detailed bio
     * Education & certifications
     * Approach to therapy
     * Client testimonials (2-3)
     * "Select This Therapist" button

6. **Selected State**:
   - Selected therapist card highlighted
   - Pink border, checkmark
   - Other cards dimmed slightly
   - Selected therapist info di sticky bar

7. **No Preference Option**:
   - Checkbox: "I don't have a preference, assign me any available therapist"
   - Auto-select based on availability

8. **Comparison Feature** (optional):
   - "Compare Therapists" button
   - Select multiple (2-3) therapists
   - Side-by-side comparison table

**Navigation**:
- "← Back" button (return to Step 1)
- **"Continue" button** (sticky bottom):
  * Disabled until therapist selected
  * Shows selected therapist name
  * Click → Go to Step 3

**Interaksi & Behavior:**
- Filter/sort dengan smooth transitions
- Single selection mode
- Profile modal dengan slideshow for photos
- Responsive cards
- Loading states untuk async data

**User Flow:**
Step 2 → Browse therapists → Filter/sort → View profiles → Select therapist → Continue → Step 3

---

#### D. Booking Step 3 - Select Date & Time

**Deskripsi:**
Step ketiga di mana client memilih tanggal dan waktu untuk session mereka berdasarkan availability therapist yang dipilih.

**Elemen Utama:**
1. **Progress Stepper**:
   - Step 1: ✓ Completed
   - Step 2: ✓ Completed
   - Step 3: Select Date & Time (active)
   - Step 4: Confirm & Pay (inactive)

2. **Booking Summary Card**:
   - Sticky sidebar (desktop) atau top card (mobile):
     * Service name + icon
     * Therapist photo + name
     * Price per session
     * Duration
     * "Edit" links untuk change service/therapist

3. **Session Type Selection**:
   - Radio buttons:
     * **Online Session** (Video Call)
       - Icon: Camera
       - Description: "Connect from anywhere"
     * **Offline Session** (In-Person)
       - Icon: Location marker
       - Description: "Visit our clinic"
       - Show clinic address
   - Selected option highlighted

4. **Calendar Component**:
   - Month view calendar
   - Navigation: < Previous Month | Current Month | Next Month >
   - Dates visualization:
     * Today: Highlighted outline
     * Available dates: Clickable, normal state
     * Fully booked dates: Disabled, grayed out
     * Selected date: Pink background, white text
     * Past dates: Disabled
   - Click date → Load available time slots

5. **Time Slots Section**:
   - Appears after date selected
   - Title: "Available time slots for [Selected Date]"
   - Grid layout atau list of time slots:
     * Each slot: "09:00 AM - 10:00 AM"
     * Status indicators:
       - Available (white background, border)
       - Selected (pink background)
       - Booked (grayed out, disabled)
   - Slot duration based on service (e.g., 60 min slots)

6. **Time Zone Info**:
   - Display: "Times shown in: Jakarta (WIB) GMT+7"
   - Dropdown to change timezone (untuk online sessions)

7. **Earliest Available**:
   - Quick action button: "Book Earliest Available"
   - Auto-selects first available slot

8. **Session Notes** (optional):
   - Textarea: "Any specific concerns or topics you'd like to address?"
   - Character limit: 500 characters
   - Helper text: "This helps your therapist prepare for your session"

9. **Validation Messages**:
   - If no slots available: "No available slots for this date. Please choose another date."
   - Loading states: "Loading available slots..."

**Navigation**:
- "← Back" button (return to Step 2)
- **"Continue" button** (sticky bottom):
  * Disabled until date & time selected
  * Shows selected date & time
  * Click → Go to Step 4

**Interaksi & Behavior:**
- Calendar date click → Load slots (API call)
- Time slot selection (single select)
- Real-time availability check
- Skeleton loading untuk slots
- Mobile: Calendar swipe navigation
- Auto-refresh availability every 60 seconds

**User Flow:**
Step 3 → Select session type → Pick date from calendar → Choose time slot → Add notes (optional) → Continue → Step 4

---

#### E. Booking Step 4 - Confirm & Payment

**Deskripsi:**
Step terakhir dalam booking flow di mana client mereview booking details, memilih payment method, dan mengkonfirmasi pembayaran.

**Elemen Utama:**
1. **Progress Stepper**:
   - Step 1: ✓ Completed
   - Step 2: ✓ Completed
   - Step 3: ✓ Completed
   - Step 4: Confirm & Pay (active)

2. **Booking Summary Card** (Prominent):
   - Title: "Review Your Booking"
   - Sections:
     * **Service Details**:
       - Service name
       - Category
       - Duration
       - "Edit" link
     
     * **Therapist Details**:
       - Photo + name
       - Specialization
       - "Edit" link
     
     * **Session Details**:
       - Date: "Monday, November 4, 2024"
       - Time: "3:00 PM - 4:00 PM (WIB)"
       - Session type: Online/Offline
       - Location (if offline): Address
       - "Edit" link
     
     * **Notes**:
       - Display client's notes
       - "Edit" link

3. **Pricing Breakdown Card**:
   - Itemized list:
     * Service fee: Rp 300.000
     * Platform fee: Rp 5.000
     * Discount (if any): - Rp 30.000 (promo code)
     * **Total**: Rp 275.000 (large, bold)

4. **Promo Code Section**:
   - Input field: "Enter promo code"
   - "Apply" button
   - Success: "Promo code applied! You saved Rp 30.000"
   - Error: "Invalid or expired promo code"

5. **Payment Method Selection**:
   - Title: "Choose Payment Method"
   - Radio options dengan cards:
     * **Bank Transfer**:
       - Icons: BCA, Mandiri, BNI, BRI
       - Description: "Pay via bank transfer"
     
     * **E-Wallet**:
       - Icons: GoPay, OVO, Dana, ShopeePay
       - Description: "Instant payment"
     
     * **Credit/Debit Card**:
       - Icons: Visa, Mastercard
       - Description: "Secure card payment"
     
     * **Virtual Account**:
       - Description: "Generate VA number"

6. **Terms Agreement**:
   - Checkboxes (required):
     * "I agree to the Booking Terms & Conditions"
     * "I agree to the Cancellation Policy"
       - Link: View policy (modal)
     * "I consent to sharing my health information with the therapist"

7. **Action Buttons**:
   - **"Confirm & Pay" button** (primary, large):
     * Disabled until payment method selected & terms agreed
     * Shows total amount: "Pay Rp 275.000"
   - "Save as Draft" button (secondary):
     * Save booking untuk complete later
   - "Cancel Booking" link

8. **Security Indicators**:
   - Icons: SSL lock, Secure payment badge
   - Text: "Your payment is secure and encrypted"
   - Payment processor logos (Midtrans, etc.)

9. **Cancellation Policy Summary**:
   - Collapsible section atau info box:
     * "Cancel 24+ hours before: Full refund"
     * "Cancel 12-24 hours: 50% charge"
     * "Cancel <12 hours: No refund"

**Payment Flow After Confirm**:
- Click "Confirm & Pay" → Redirect to payment gateway (Midtrans)
- Payment options presented
- User completes payment
- Redirect back to CUR-HEART dengan status

**Success State (Next Page)**:
- Redirect to Booking Success page
- Show booking confirmation
- Send confirmation email

**Interaksi & Behavior:**
- Real-time promo code validation
- Payment method selection updates UI
- Terms checkbox validation
- Loading overlay saat processing payment
- Error handling untuk failed payments
- Session timeout warning

**User Flow:**
Step 4 → Review all details → Enter promo (optional) → Select payment → Agree terms → Confirm & Pay → Payment gateway → Payment success → Booking Success page

---

#### F. Booking Success Page

**Deskripsi:**
Booking Success page ditampilkan setelah pembayaran berhasil. Halaman ini memberikan konfirmasi booking dan informasi tentang next steps.

**Elemen Utama:**
1. **Success Animation**:
   - Large checkmark icon dengan animation (scale in, check draw)
   - Confetti animation (brief celebration)

2. **Success Message**:
   - Title: "Booking Confirmed! 🎉"
   - Subtitle: "Your session has been successfully booked"

3. **Booking Details Card**:
   - "Booking Confirmation" heading
   - **Booking ID**: #BK-2024-00123 (copy button)
   - Service name
   - Therapist: Name + photo
   - Date & Time (large, prominent)
   - Duration
   - Session Type (Online/Offline)
   - Location (if offline)
   - Total Paid: Rp 275.000
   - Payment Method

4. **Next Steps Section**:
   - Title: "What's Next?"
   - Numbered list:
     1. "You'll receive a confirmation email shortly"
     2. "For online sessions, join link will be sent 15 minutes before"
     3. "Prepare any questions or concerns for your therapist"
     4. "Arrive/join 5 minutes early"

5. **Action Buttons**:
   - "View Appointment Details" (primary)
   - "Add to Calendar" (with dropdown: Google, Outlook, iCal)
   - "Download Invoice" (PDF)
   - "Share Booking" (optional)

6. **Preparation Tips**:
   - "Tips for Your First Session"
   - 3-4 bullet points:
     * Find a quiet, comfortable space
     * Have a glass of water nearby
     * Wear comfortable clothing
     * Arrive with an open mind

7. **Contact Support**:
   - "Need to change your booking?"
   - "Contact Support" button
   - "View Cancellation Policy" link

8. **Related Actions**:
   - "Book Another Session" button
   - "Invite a Friend" (referral program)

9. **Confirmation Email Notice**:
   - Info box: "📧 Confirmation email sent to [email]"
   - "Didn't receive? Check spam or resend"

**Interaksi & Behavior:**
- Confetti animation on load (once)
- Copy booking ID to clipboard
- Add to calendar generates .ics file
- Download invoice (PDF generation)
- Auto-redirect ke appointments setelah 30 seconds (optional, dengan countdown)

**User Flow:**
Booking Success page → View details / Download invoice / Add to calendar → Back to Dashboard atau View Appointments

---

#### G. My Appointments List

**Deskripsi:**
My Appointments page menampilkan daftar lengkap semua appointments client, baik upcoming, past, maupun cancelled. Halaman ini memungkinkan client untuk manage appointments mereka.

**Elemen Utama:**
1. **Page Header**:
   - Title: "My Appointments"
   - Breadcrumb: Dashboard > My Appointments

2. **Tabs Navigation**:
   - Horizontal tabs:
     * **Upcoming** (default, badge dengan count)
     * **Past**
     * **Cancelled**
   - Active tab highlighted

3. **Filter & Sort Section**:
   - Search bar: "Search by service or therapist..."
   - Filter dropdowns:
     * Date Range (This Week, This Month, Last 3 Months, Custom Range)
     * Service Type (All, Stress Management, Weight Loss, etc.)
     * Session Type (All, Online, Offline)
     * Status (All, Confirmed, Pending Payment, Completed, Cancelled)
   - Sort: Date (Newest/Oldest), Service Name A-Z

4. **Appointments List** (Upcoming Tab):
   - Card-based list layout
   - Each appointment card:
     * **Left Section**:
       - Date badge (vertical: Month abbr + Day number)
       - Time (start - end)
     
     * **Middle Section**:
       - Service name (H4)
       - Therapist: Photo + Name
       - Session type badge (Online/Offline)
       - Duration: 60 minutes
       - Location (if offline): Address
       - Status badge (Confirmed/Pending/etc.)
     
     * **Right Section** (Actions):
       - Countdown timer (if within 24 hours): "Starts in 2h 30m"
       - **"Join Session"** button (primary, if online & within 15 min)
       - **"View Details"** button
       - Dropdown menu (3 dots):
         * Reschedule
         * Cancel Appointment
         * Add to Calendar
         * Download Invoice
         * Contact Therapist

5. **Empty States**:
   - **No Upcoming Appointments**:
     * Illustration: Calendar with checkmark
     * Message: "You don't have any upcoming appointments"
     * "Book Your First Session" button
   
   - **No Past Appointments**:
     * Message: "Your appointment history will appear here"
   
   - **No Cancelled Appointments**:
     * Message: "No cancelled appointments"

6. **Past Appointments** (Past Tab):
   - Similar card layout
   - Additional elements:
     * Completion badge
     * "Leave a Review" button (if not reviewed yet)
     * "Book Again with [Therapist]" quick action
     * Session notes preview (if available)

7. **Cancelled Appointments** (Cancelled Tab):
   - Shows cancelled appointments
   - Cancellation info:
     * Cancelled by: Client/Therapist/System
     * Cancellation date
     * Reason (if provided)
     * Refund status (Full/Partial/None)
   - "Book New Session" button

8. **Pagination**:
   - Bottom pagination: Previous | 1 2 3 ... 10 | Next
   - Items per page: 10 (configurable)

9. **Bulk Actions** (optional):
   - Select multiple appointments
   - Bulk export to calendar
   - Bulk download invoices

**Interaksi & Behavior:**
- Real-time updates untuk status changes
- Countdown timers update every minute
- Filter/search results dengan smooth transitions
- Skeleton loading untuk appointments
- Pull to refresh (mobile)
- Infinite scroll atau pagination

**User Flow:**
Client → My Appointments → Browse list → View details atau take action (join/reschedule/cancel)

---

#### H. Appointment Detail Page

**Deskripsi:**
Appointment Detail page menampilkan informasi lengkap tentang satu appointment spesifik, termasuk semua details, status, dan available actions.

**Elemen Utama:**
1. **Page Header**:
   - Back button: "← Back to Appointments"
   - Booking ID: #BK-2024-00123
   - Status badge (large): Confirmed/Completed/Cancelled

2. **Appointment Summary Card**:
   - **Date & Time Section**:
     * Large date display: "Monday, November 4, 2024"
     * Time: "3:00 PM - 4:00 PM (WIB)"
     * Countdown (if upcoming): "In 2 days, 5 hours"
     * Add to Calendar button
   
   - **Service Details**:
     * Service name (H3)
     * Category badge
     * Duration: 60 minutes
     * Price: Rp 300.000
     * Session type: Online/Offline badge
   
   - **Therapist Information**:
     * Professional photo (large)
     * Name (H4)
     * Credentials
     * Specialization
     * "View Profile" link
     * "Send Message" button

3. **Session Location/Link**:
   - **If Online**:
     * Meeting link section (appears 15 min before)
     * "Join Video Session" button (primary, large)
     * Meeting ID & Password
     * Instructions: "Please join 5 minutes early"
     * Technical requirements checklist
   
   - **If Offline**:
     * Full address
     * "Get Directions" button (Google Maps)
     * Contact phone number
     * Parking information

4. **Your Notes Section**:
   - Display notes client submitted during booking
   - Editable (until 24h before session)
   - "Edit Notes" button
   - Character count

5. **Payment Information**:
   - Payment status badge: Paid/Pending
   - **Breakdown**:
     * Service fee
     * Platform fee
     * Discount (if any)
     * Total paid
   - Payment method used
   - Transaction ID
   - Payment date & time
   - "Download Invoice" button (PDF)
   - "Request Receipt" link

6. **Booking History Timeline**:
   - Vertical timeline showing:
     * Booking created (date & time)
     * Payment completed
     * Confirmed by therapist
     * Reminder sent
     * Session completed (if past)
     * Review submitted (if applicable)

7. **Actions Section**:
   - **For Upcoming Appointments**:
     * "Reschedule Appointment" button
       - Modal: Select new date/time
       - Show reschedule policy
     * "Cancel Appointment" button
       - Modal: Confirm cancellation
       - Show refund policy
       - Reason selection (dropdown)
       - Note textarea
     * "Contact Therapist" button
   
   - **For Past Appointments**:
     * "Leave a Review" button (if not reviewed)
     * "View Session Notes" (if therapist shared)
     * "Book Again" button
     * "Download Report" (if available)

8. **Session Notes** (After Session):
   - Visible setelah session completed
   - Therapist's notes (if shared with client)
   - Homework/recommendations
   - Next session suggestions

9. **Review Section** (If Reviewed):
   - Client's review displayed:
     * Rating stars
     * Review text
     * Date submitted
   - "Edit Review" option

10. **Cancellation Policy Box**:
    - Info box with policy summary
    - Countdown untuk free cancellation deadline
    - "View Full Policy" link

11. **Support Section**:
    - "Need Help?" button
    - FAQ link specific to appointments
    - Contact support

**Interaksi & Behavior:**
- Real-time status updates
- Countdown timers
- Join button appears 15 min before session
- Modal confirmations untuk actions
- Form validation untuk reschedule/cancel
- Auto-refresh before session time

**User Flow:**
Appointments List → Click appointment → Detail page → View info / Take action (join/reschedule/cancel/review)

---

#### I. Client Progress Tracking Dashboard

**Deskripsi:**
Progress Tracking page membantu client melihat perkembangan mereka dalam therapy journey. Halaman ini menampilkan metrics, charts, dan insights tentang wellness progress mereka.

**Elemen Utama:**
1. **Page Header**:
   - Title: "My Progress"
   - Subtitle: "Track your wellness journey"
   - Breadcrumb: Dashboard > My Progress
   - Date range selector: Last 30 Days, 3 Months, 6 Months, 1 Year, All Time

2. **Progress Overview Cards**:
   - 4 metric cards in row:
     * **Total Sessions**: Number + trend
     * **Completion Rate**: Percentage + progress bar
     * **Goal Achievement**: X of Y goals completed
     * **Wellness Score**: 78/100 + trend indicator

3. **Wellness Score Chart**:
   - Large card: "Your Wellness Score Over Time"
   - Line chart showing wellness score progression
   - X-axis: Timeline (weeks/months)
   - Y-axis: Score (0-100)
   - Data points: Clickable untuk details
   - Trend line overlay
   - Goal line (target score)
   - Color coded: Improving (green), Declining (red), Stable (blue)

4. **Session Attendance Chart**:
   - Bar chart atau calendar heatmap
   - Shows session frequency
   - Color intensity based on sessions per week
   - Tooltips dengan session details

5. **Goals & Milestones Section**:
   - Title: "Your Goals"
   - List of goals set dengan therapist:
     * Goal description
     * Progress bar (0-100%)
     * Target date
     * Current status (In Progress/Achieved/Overdue)
     * Notes
   - "Add New Goal" button
   - Completed goals collapse atau separate tab

6. **Mood Tracking**:
   - "How Have You Been Feeling?"
   - Line/area chart:
     * X-axis: Date
     * Y-axis: Mood score (1-10)
     * Multiple metrics: Anxiety, Stress, Happiness, Energy
     * Toggle untuk show/hide metrics
   - Weekly average comparison

7. **Session Summary Statistics**:
   - Table or list:
     * Total sessions attended
     * Most frequent service
     * Favorite therapist
     * Average session rating
     * Total hours spent
     * Longest streak
     * Current streak

8. **Achievements & Badges**:
   - Gamification elements:
     * "First Session" badge
     * "5 Sessions Milestone" badge
     * "30-Day Streak" badge
     * "Goal Achiever" badge
   - Progress bars for next badges

9. **Therapist Notes Summary**:
   - Collapsible section
   - Aggregated notes from therapists
   - Recommendations
   - Homework completion tracking

10. **Progress Reports**:
    - "Monthly Progress Report"
    - Download as PDF
    - Email report option
    - Share with therapist

11. **Comparison Metrics**:
    - "You vs Your Goals"
    - "This Month vs Last Month"
    - Improvement percentage

12. **Insights & Recommendations**:
    - AI-generated insights (optional):
      * "You're doing great! Your mood has improved 25% this month"
      * "Consider booking more stress management sessions"
      * "Your goal completion rate is above average!"

13. **Quick Actions**:
    - "Book Next Session" button
    - "Set New Goal" button
    - "Update Mood" button (daily check-in)

**Interaksi & Behavior:**
- Interactive charts (hover untuk tooltips, click untuk drill-down)
- Date range selector updates all charts
- Smooth animations untuk chart rendering
- Export data as CSV/PDF
- Responsive charts (adapt to mobile)
- Real-time updates saat new data available

**User Flow:**
Client → My Progress → View charts & metrics → Identify trends → Take actions (book session, update goals)

---

#### J. Client Messages (Chat with Therapist)

**Deskripsi:**
Messages page memungkinkan client untuk berkomunikasi dengan therapist mereka melalui chat interface. Ini penting untuk follow-up questions, appointment coordination, dan ongoing support.

**Elemen Utama:**
1. **Page Layout**:
   - Split view (desktop):
     * Left sidebar (30%): Conversations list
     * Right main area (70%): Active conversation
   - Single view (mobile): List ↔ Conversation switching

2. **Conversations List Sidebar**:
   - Header:
     * Title: "Messages"
     * Search bar: "Search conversations..."
     * New message button (compose)
   
   - Conversation items:
     * Therapist avatar
     * Therapist name
     * Last message preview (truncated)
     * Timestamp (relative: "2h ago", "Yesterday")
     * Unread badge count (if any)
     * Online status indicator (green dot)
     * Pin option (for important chats)
   
   - Sorted by: Most recent on top
   - Empty state: "No messages yet. Book a session to start chatting!"

3. **Active Conversation Area**:
   - **Header**:
     * Therapist avatar + name
     * Online status ("Active now" / "Last seen 2h ago")
     * Actions:
       - Video call icon (if during session time)
       - Phone call icon
       - Info icon (view therapist profile)
       - More menu (mute, report, block)
   
   - **Message Thread**:
     * Messages displayed chronologically
     * Date separators ("Today", "Yesterday", "Oct 25, 2024")
     * **Incoming messages** (therapist):
       - Avatar on left
       - Message bubble (gray background)
       - Timestamp below
       - Read status (if enabled)
     
     * **Outgoing messages** (client):
       - Aligned right
       - Message bubble (pink background)
       - Timestamp
       - Status indicators:
         * Sent (single checkmark)
         * Delivered (double checkmark)
         * Read (double checkmark blue)
     
     * **Message types supported**:
       - Text messages
       - Emoji
       - Images (with preview)
       - Files (PDF, documents) dengan download link
       - Voice messages (play button)
       - Quick replies (buttons)
     
     * Scroll to bottom button (appears when scrolled up)
   
   - **Input Area**:
     * Text input field (multiline)
     * Placeholder: "Type a message..."
     * Left actions:
       - Emoji picker icon
       - Attachment icon (upload files/images)
       - Voice record icon (hold to record)
     * Right action:
       - Send button (icon, disabled when empty)
     * Character counter (optional)
     * Typing indicator: "Therapist is typing..."

4. **Empty Conversation State**:
   - When no conversation selected:
     * Illustration
     * "Select a conversation to start messaging"
     * Or: "Start a New Conversation" button

5. **Quick Responses** (Optional):
   - Suggested responses:
     * "Thank you"
     * "Yes, I'll be there"
     * "Can we reschedule?"
     * "I have a question"

6. **Automated Messages**:
   - System messages dalam conversation:
     * "Booking confirmed for Nov 4 at 3:00 PM"
     * "Session completed. Leave a review?"
     * Appointment reminders
   - Styled differently (gray, italic)

7. **Conversation Info Sidebar** (Optional):
   - Accessible via info icon
   - Shows:
     * Therapist full profile
     * Upcoming appointments
     * Shared files/media gallery
     * Search in conversation
     * Notification settings
     * Report/block options

8. **Notification Settings**:
   - Per conversation mute option
   - Global notification preferences link

9. **Privacy & Guidelines**:
   - Banner or info:
     * "All messages are confidential and encrypted"
     * "Community guidelines" link
     * "Response time: Usually within 2 hours"

10. **Offline/Error States**:
    - "No internet connection" banner
    - Failed to send indicator (red exclamation)
    - Retry button

**Interaksi & Behavior:**
- Real-time messaging (WebSocket/Pusher)
- Typing indicators
- Read receipts
- Message delivery status
- Auto-scroll to bottom on new message
- Image preview lightbox
- File upload progress bars
- Voice message recording interface
- Search within conversation
- Copy/delete message options (long press/right click)
- Emoji picker with categories
- Message reactions (optional)

**User Flow:**
Client → Messages → Select therapist conversation → Read messages → Type response → Send → Real-time delivery

---

### 4.3.5.8 Mockup Therapist Dashboard (Therapist Dashboard Pages)

Therapist Dashboard adalah area khusus untuk terapis yang telah terdaftar dan approved. Dashboard ini memungkinkan terapis untuk manage schedule, appointments, clients, sessions, dan earnings.

---

**[GAMBAR 4.41 - Mockup: Therapist Dashboard Main]** 👨‍⚕️
_Therapist dashboard - Today's schedule, stats, quick actions_

**[GAMBAR 4.42 - Mockup: Therapist Appointments Calendar]** 👨‍⚕️
_Therapist - Calendar view of all bookings, filter by status_

**[GAMBAR 4.43 - Mockup: Therapist Availability Management]** 👨‍⚕️
_Therapist - Set weekly schedule, block dates/times_

**[GAMBAR 4.44 - Mockup: Therapist Clients List]** 👨‍⚕️
_Therapist - Table of all clients with search/filter_

**[GAMBAR 4.45 - Mockup: Therapist Client Detail View]** 👨‍⚕️
_Therapist - Client profile, history, progress data_

**[GAMBAR 4.46 - Mockup: Therapist Write Session Notes]** 👨‍⚕️
_Therapist - Form to write therapy notes after session_

**[GAMBAR 4.47 - Mockup: Therapist Update Client Progress]** 👨‍⚕️
_Therapist - Input metrics: anxiety, confidence, sleep quality_

**[GAMBAR 4.48 - Mockup: Therapist Reviews Page]** 👨‍⚕️
_Therapist - View all ratings and reviews from clients_

**[GAMBAR 4.49 - Mockup: Therapist Earnings Dashboard]** 👨‍⚕️
_Therapist - Revenue charts, transaction history_

**[GAMBAR 4.50 - Mockup: Therapist Profile Settings]** 👨‍⚕️
_Therapist - Edit bio, credentials, photo, specializations_

---

#### A. Therapist Dashboard (Main)

**Deskripsi:**
Therapist Dashboard Main adalah landing page setelah therapist login. Memberikan overview lengkap dari jadwal hari ini, upcoming appointments, earnings, dan key metrics.

**Elemen Utama:**
1. **Top Navigation & Sidebar**:
   - Similar struktur dengan client dashboard
   - Navigation items:
     * Dashboard (active)
     * My Schedule
     * Clients
     * Sessions
     * Earnings
     * Profile
     * Settings

2. **Welcome Section**:
   - "Good Morning, Dr. [Therapist Name]"
   - Current date & time
   - Quick stats: "You have 5 sessions today"

3. **Key Metrics Cards** (4 cards):
   - **Today's Sessions**:
     * Number: "5"
     * Icon: Calendar
     * "View Schedule" link
   
   - **Total Clients**:
     * Number: "127"
     * Icon: Users
     * "+5 this month" trend
   
   - **This Month Earnings**:
     * Amount: "Rp 18.500.000"
     * Icon: Money
     * "+12% from last month" trend
   
   - **Average Rating**:
     * Stars: 4.9/5.0
     * Icon: Star
     * "Based on 87 reviews"

4. **Today's Schedule Card**:
   - "Today's Appointments"
   - Timeline view of today's sessions:
     * Each appointment:
       - Time: "09:00 AM - 10:00 AM"
       - Client name + avatar
       - Service name
       - Session type badge (Online/Offline)
       - Status: Upcoming/In Progress/Completed
       - Quick actions:
         * "Join Session" (if online & time)
         * "View Details"
         * "Start Session"
         * "Cancel" (with reason)
   - Empty slots shown as breaks
   - "View Full Schedule" link

5. **Upcoming Clients Card**:
   - "Next Clients"
   - List of next 3-4 clients:
     * Avatar + name
     * Service booked
     * Time
     * New client badge (if first time)
     * "View Profile" link
   - "See All Clients" link

6. **Recent Activities**:
   - Activity feed:
     * "New booking from [Client Name]"
     * "[Client] left a 5-star review"
     * "Payment received: Rp 300.000"
     * "New message from [Client]"
   - Timestamps
   - "View All" link

7. **Earnings Overview Widget**:
   - "This Month Earnings"
   - Bar chart showing daily/weekly earnings
   - "View Detailed Report" link

8. **Client Reviews**:
   - "Recent Reviews"
   - 2-3 latest reviews:
     * Client name (or anonymous)
     * Rating stars
     * Review excerpt
     * Date
   - "View All Reviews" link

9. **Quick Actions Section**:
   - Buttons:
     * "Set Availability"
     * "View Messages"
     * "Add Session Notes"
     * "Request Withdrawal"

10. **Notifications Center**:
    - Bell icon dengan badge count
    - Dropdown list:
      * New bookings
      * Cancellations
      * Messages
      * Reviews
      * Payment notifications
    - Mark as read option

**Interaksi & Behavior:**
- Real-time updates untuk new bookings
- Auto-refresh schedule setiap 5 min
- Countdown timers untuk next session
- Notifications popup/toast
- Responsive layout

**User Flow:**
Therapist login → Dashboard → Overview metrics → Check today's schedule → Take actions

---

#### B. Therapist Schedule Management

**Deskripsi:**
Schedule Management page memungkinkan therapist melihat kalender appointments mereka dengan berbagai views (day, week, month) dan manage bookings.

**Elemen Utama:**
1. **Page Header**:
   - Title: "My Schedule"
   - Date range displayed
   - "Set Availability" button (prominent)

2. **Calendar View Selector**:
   - Toggle buttons:
     * Day view
     * Week view (default)
     * Month view
   - Date navigation: < Today | Date picker | >

3. **Week View** (Default):
   - Grid layout:
     * Y-axis: Time slots (8:00 AM - 8:00 PM)
     * X-axis: Days of week (Mon - Sun)
   
   - Appointments displayed as blocks:
     * Color coded by status:
       - Confirmed: Green
       - Pending: Orange
       - Completed: Gray
       - Cancelled: Red strikethrough
     * Each block shows:
       - Time
       - Client name
       - Service name
       - Session type icon
     * Hover: Show more details
     * Click: Open appointment detail modal
   
   - Empty slots clickable (block time off)
   - Drag & drop untuk reschedule (optional)

4. **Day View**:
   - Detailed timeline of single day
   - Larger blocks dengan more info:
     * Client photo
     * Full service name
     * Session notes preview
     * Action buttons visible

5. **Month View**:
   - Calendar grid
   - Dots or numbers indicating sessions per day
   - Click day → Show list of appointments
   - Color intensity based on booking density

6. **Filter & Legend**:
   - Filter appointments:
     * By status (All, Confirmed, Pending, etc.)
     * By session type (Online, Offline)
     * By service
   - Color legend explaining status colors

7. **Sidebar** (Desktop):
   - Mini calendar untuk quick navigation
   - Today's summary stats
   - Quick filters
   - "Add Time Off" button

8. **Appointment Actions**:
   - Click appointment block → Modal:
     * View client details
     * Session information
     * "Start Session" button
     * "Add Notes" button
     * "Cancel Appointment"
     * "Reschedule"
     * "Contact Client"

9. **Time Off Blocks**:
   - Block time off shows as unavailable
   - Different color (gray striped)
   - Label: "Break" / "Time Off" / "Lunch"
   - Editable/deletable

**Interaksi & Behavior:**
- Smooth transitions antar views
- Drag & drop reschedule dengan confirmation
- Real-time updates dari new bookings
- Sync dengan Google Calendar (optional)
- Export calendar (.ics)
- Print schedule option

**User Flow:**
Therapist → My Schedule → Select view → Browse appointments → Click for details → Take actions

---

#### C. Therapist Availability Settings

**Deskripsi:**
Availability Settings page memungkinkan therapist mengatur jam kerja regular mereka, specific dates unavailable, dan time off. Ini mempengaruhi booking availability untuk clients.

**Elemen Utama:**
1. **Page Header**:
   - Title: "Availability Settings"
   - Subtitle: "Manage your working hours and time off"

2. **Working Hours Section**:
   - "Regular Working Hours"
   - Per day settings:
     * Days of week list:
       - Monday: Toggle On/Off
         * If On: Time pickers (Start - End)
         * Example: 09:00 AM - 05:00 PM
         * "Add Break" button (for lunch, etc.)
         * Multiple time slots per day
       - Tuesday: ...
       - ... (all 7 days)
   
   - "Apply to All Days" quick action
   - "Copy from Monday" option
   
   - Breaks configuration:
     * Break name: "Lunch Break"
     * Start - End time: 12:00 PM - 1:00 PM
     * Remove break button

3. **Session Duration Settings**:
   - "Default Session Duration"
   - Dropdown: 30 min, 45 min, 60 min, 90 min, 120 min
   - Buffer time between sessions: 5/10/15/30 min

4. **Booking Window**:
   - "How far in advance can clients book?"
   - Minimum notice: 2 hours, 4 hours, 1 day, 2 days
   - Maximum advance: 1 week, 2 weeks, 1 month, 3 months

5. **Specific Dates Unavailable**:
   - "Time Off / Holidays"
   - Calendar picker untuk select dates
   - List of upcoming time off:
     * Date range: Nov 15-17, 2024
     * Reason: "Conference Attendance"
     * Status: Active
     * Edit/Delete buttons
   - "Add Time Off" button

6. **Override Availability**:
   - "Custom Availability for Specific Dates"
   - Use case: Working on Sunday exceptionally
   - Date picker + time settings
   - Priority over regular hours

7. **Availability Preview**:
   - "Preview Your Availability"
   - Mini calendar showing:
     * Available days (green)
     * Partially available (yellow)
     * Unavailable (red)
     * Time off (gray)
   - Click day → Show time slots

8. **Notification Preferences**:
   - "Notify me for bookings:"
   - Checkboxes:
     * New booking (instant)
     * Booking X hours before
     * Daily schedule summary
     * Weekly schedule summary

9. **Save Changes**:
   - "Save Availability" button (primary)
   - "Reset to Default" button
   - Confirmation: "Changes saved successfully"

**Interaksi & Behavior:**
- Time pickers dengan validation (end > start)
- Conflict detection (overlapping times)
- Real-time preview updates
- Confirmation modal for major changes
- Auto-save draft (optional)

**User Flow:**
Therapist → Availability Settings → Set working hours → Add time off → Save → System updates booking availability for clients

---

#### D. Therapist Clients List

**Deskripsi:**
Clients List page menampilkan semua clients yang pernah atau sedang di-handle oleh therapist. Terapis dapat view profiles, session history, dan manage relationships.

**Elemen Utama:**
1. **Page Header**:
   - Title: "My Clients"
   - Client count: "127 Total Clients"
   - "Export Client List" button (CSV)

2. **Search & Filter**:
   - Search bar: "Search by name or ID..."
   - Filters:
     * Status: All, Active, Inactive, New
     * Service Type: All, Stress, Weight Loss, etc.
     * Last Session: Last 7 days, 30 days, 3 months, 6 months
     * Sort: Name A-Z, Recent Activity, Total Sessions

3. **Clients Grid/List**:
   - Card atau table layout
   - Each client entry:
     * **Avatar + Name**:
       - Profile photo
       - Full name
       - Client ID
     
     * **Status Badge**:
       - Active (green)
       - New Client (blue)
       - Inactive (gray)
     
     * **Statistics**:
       - Total sessions: 8 sessions
       - Last session: 3 days ago
       - Next session: Tomorrow 2:00 PM
       - Total spent: Rp 2.400.000
     
     * **Primary Service**:
       - Most booked service
       - Badge
     
     * **Actions**:
       - "View Profile" button (primary)
       - "Send Message" button
       - "Book Session" (on behalf)
       - Dropdown: View History, Add Notes, Archive

4. **Quick Filters Tabs**:
   - All Clients
   - Active (has upcoming sessions)
   - New This Month
   - Needs Follow-up (flagged)

5. **Client Detail Modal** (Quick View):
   - Opens when "View Profile" clicked
   - Summary view:
     * Full profile info
     * Contact details (email, phone)
     * Session history (last 5)
     * Progress overview
     * Notes summary
     * "View Full Profile" link

6. **Bulk Actions** (Optional):
   - Select multiple clients
   - Send mass message
   - Export selected
   - Add to group

7. **Pagination**:
   - Standard pagination controls
   - Items per page: 20

**Interaksi & Behavior:**
- Search with debounce
- Filter combinations
- Sort with animations
- Modal quick view
- Responsive table/cards

**User Flow:**
Therapist → My Clients → Search/filter → Select client → View profile → Take action (message, view history, etc.)

---

#### E. Client Profile View (Therapist Perspective)

**Deskripsi:**
Detailed client profile page yang hanya accessible oleh therapist. Berisi comprehensive information tentang client, session history, notes, dan progress tracking.

**Elemen Utama:**
1. **Profile Header**:
   - Large avatar
   - Client name (H2)
   - Client ID
   - Status badge (Active/Inactive)
   - Member since date
   - Action buttons:
     * "Send Message"
     * "Schedule Session"
     * "Add Note"
     * More menu (Flag, Archive, Report)

2. **Tabs Navigation**:
   - Overview
   - Session History
   - Notes & Observations
   - Progress & Goals
   - Files & Documents

3. **Overview Tab**:
   - **Personal Information**:
     * Full name
     * Email (clickable)
     * Phone (clickable, call)
     * Date of birth / Age
     * Gender
     * Address (for offline sessions)
     * Emergency contact
   
   - **Quick Stats**:
     * Total sessions: 12
     * Total spent: Rp 3.600.000
     * Average rating given: 5.0
     * Last session: Oct 28, 2024
     * Next session: Nov 5, 2024
   
   - **Primary Concerns**:
     * List of main issues client is addressing:
       - Stress & Anxiety
       - Sleep Disorders
     * Added by client during intake
   
   - **Services History**:
     * Chart or list of services used
     * Frequency per service type

4. **Session History Tab**:
   - List of all past sessions:
     * Date & time
     * Service name
     * Duration
     * Status (Completed/Cancelled)
     * Payment status
     * Session rating (if client rated)
     * "View Notes" link
   - Export as PDF
   - Total: 12 sessions completed

5. **Notes & Observations Tab**:
   - **Session Notes** (Chronological):
     * Each note entry:
       - Session date
       - Service type
       - Therapist notes (private, not shared with client)
       - Observations
       - Client feedback
       - Homework assigned
       - Next steps
       - Edit/Delete buttons
   
   - **Add New Note** button:
     * Opens form:
       - Date (auto-filled)
       - Session related? (Yes/No)
       - Note type (Observation, Progress, Concern)
       - Note content (rich text editor)
       - Share with client? (checkbox)
       - Save/Cancel

6. **Progress & Goals Tab**:
   - **Goals List**:
     * Goal description
     * Set date
     * Target completion
     * Progress bar
     * Status (In Progress/Achieved)
     * Notes on progress
   
   - **Progress Metrics**:
     * Charts showing improvement
     * Wellness score trend
     * Attendance rate
   
   - "Set New Goal" button

7. **Files & Documents Tab**:
   - Uploaded documents:
     * Intake forms
     * Consent forms
     * Medical history
     * Progress reports
     * Session recordings (if any)
   - "Upload New File" button
   - Download/view options

8. **Risk Assessment Section** (if applicable):
   - Risk level indicator
   - Last assessment date
   - Notes on risk factors
   - Follow-up actions

9. **Communication Log**:
   - History of all messages exchanged
   - Email communications log
   - Phone call notes

**Interaksi & Behavior:**
- Tab switching with smooth transitions
- Collapsible sections
- Rich text editor untuk notes
- File upload with preview
- Print client profile
- Export data (GDPR compliance)

**User Flow:**
Therapist → My Clients → Select client → Profile view → Browse tabs → Add notes / View history / Update goals

---

#### F. Session Room (Video Conferencing)

**Deskripsi:**
Session Room adalah halaman khusus untuk conducting online therapy sessions melalui video call. Interface dirancang untuk memberikan pengalaman yang professional, secure, dan conducive untuk therapy sessions.

**Elemen Utama:**
1. **Video Layout**:
   - **Main View**:
     * Client video (large, dominant area 70%)
     * Therapist video (smaller, picture-in-picture di corner)
     * Switch view button (make therapist main)
   
   - **Layout Options**:
     * Gallery view (side-by-side, equal size)
     * Speaker view (active speaker dominates)
     * Presentation mode (screen share main)

2. **Control Bar** (Bottom):
   - Always visible atau auto-hide dengan hover
   - Icons with labels:
     * **Microphone**: Mute/Unmute (red when muted)
     * **Camera**: Start/Stop video
     * **Screen Share**: Share screen option
     * **Chat**: Open text chat sidebar (badge for new messages)
     * **Participants**: Show participants list (usually just 2)
     * **Settings**: Audio/video settings
     * **Record**: Record session (if enabled & consented)
     * **End Call**: Red button, confirmation modal

3. **Session Timer**:
   - Displayed prominently (top-center atau corner)
   - Shows elapsed time: "00:45:30"
   - Remaining time: "15 min left"
   - Color changes: Green → Yellow (10 min) → Red (5 min)

4. **Session Information Bar** (Top):
   - Client name
   - Service type
   - Session duration booked
   - Connection quality indicator (green/yellow/red)

5. **Chat Sidebar** (Collapsible):
   - Text chat during session
   - Send messages, links, resources
   - File sharing capability
   - Chat transcript saved

6. **Notes Panel** (Collapsible, Right Side):
   - Quick notes during session
   - Text area for therapist to type observations
   - Auto-save every 30 seconds
   - Accessible only to therapist
   - "Save & Add to Client Record" button

7. **Virtual Background** (Optional):
   - Blur background
   - Select from preset backgrounds
   - Upload custom background

8. **Network Quality Indicator**:
   - Icon showing connection strength
   - Bandwidth usage display
   - "Poor connection" warning with troubleshooting tips

9. **Waiting Room** (Before Session):
   - "Waiting for [Client Name] to join..."
   - Connection test:
     * Camera preview
     * Microphone test
     * Speaker test
   - "Start Session" button (once client joins)

10. **End Session Modal**:
    - Confirmation: "Are you sure you want to end the session?"
    - Options:
      * Add session notes now
      * Add notes later
      * End without notes
    - Feedback: "How was the video quality?" (1-5 stars)
    - "End Session" button

11. **Technical Issue Handling**:
    - Reconnecting overlay if connection drops
    - "Switch to audio only" option if video lags
    - Emergency contact button
    - "Report Technical Issue" link

12. **Security Indicators**:
    - End-to-end encryption badge
    - "This session is private and secure"
    - Recording indicator (if recording): Red dot "Recording"

**Interaksi & Behavior:**
- WebRTC video streaming
- Adaptive bitrate based on bandwidth
- Echo cancellation, noise suppression
- Auto-focus on active speaker
- Keyboard shortcuts (M for mute, V for video, etc.)
- Mobile responsive (landscape mode preferred)
- Picture-in-picture mode when tab switched

**User Flow:**
Therapist → Join session 5 min early → Test connection → Client joins → Start session → Conduct therapy → Take notes → End call → Add final notes

---

#### G. Session Notes Entry Form

**Deskripsi:**
Session Notes form memungkinkan therapist untuk mendokumentasikan observations, progress, dan recommendations setelah (atau selama) therapy session. Notes ini penting untuk continuity of care dan legal documentation.

**Elemen Utama:**
1. **Page Header**:
   - Title: "Session Notes"
   - Client name + photo
   - Session date & time
   - Service type
   - Session duration

2. **Session Information Section** (Auto-filled):
   - Session ID
   - Date & time (pre-filled)
   - Duration (actual, editable if different from booked)
   - Session number (e.g., "Session 8 of 10")
   - Session type (Online/Offline)
   - Attendance status:
     * Attended
     * Late (specify minutes)
     * No-show
     * Cancelled

3. **Assessment Section**:
   - **Current State**:
     * Textarea: "Client's presenting concern/state at start of session"
     * Mood rating (1-10 scale slider)
     * Anxiety level (1-10)
     * Overall wellness (1-10)
   
   - **Observations**:
     * Textarea: "Behavioral observations, body language, tone"
     * Rich text editor dengan formatting options

4. **Session Summary**:
   - **Topics Discussed**:
     * Multi-select or tags: Stress, Relationships, Work, Sleep, etc.
     * Free-text additional topics
   
   - **Techniques Used**:
     * Checkboxes: Hypnotic Induction, Regression, Suggestion Therapy, CBT, etc.
     * Effectiveness rating per technique (1-5)
   
   - **Client Response**:
     * Textarea: "How client responded to interventions"
     * Response quality: Excellent, Good, Fair, Poor

5. **Progress Notes**:
   - Textarea: "Detailed notes on session content and progress"
   - Minimum 200 characters (professional standard)
   - Rich text editor:
     * Bold, italic, underline
     * Bullet points, numbered lists
     * Headings
   - Template insertion: Common phrases/sections

6. **Goals Review**:
   - List of client's active goals
   - For each goal:
     * Goal description
     * Progress update dropdown: No Change, Some Progress, Significant Progress, Goal Met
     * Notes on goal progress (textarea)

7. **Homework/Action Items**:
   - "Assigned Tasks for Client"
   - Add multiple tasks:
     * Task description
     * Due date
     * Instructions
   - "Share with client" checkbox

8. **Recommendations**:
   - **Next Session**:
     * Recommended timing: 1 week, 2 weeks, 1 month
     * Focus areas for next session
   
   - **Additional Services**:
     * Suggest other services
     * Referrals (if needed)

9. **Risk Assessment** (If applicable):
   - Risk level: None, Low, Moderate, High
   - If Moderate/High:
     * Specific concerns
     * Safety plan
     * Follow-up actions
     * Supervisor notification required

10. **Attachments**:
    - Upload files:
      * Worksheets used
      * Client drawings/diagrams
      * Audio recordings (if consented)
    - File size limits displayed

11. **Visibility Settings**:
    - Radio buttons:
      * Private (Therapist only)
      * Shared with Client (Client can view in their portal)
      * Shared with Supervisor (If applicable)

12. **Save Options**:
    - "Save as Draft" button (gray)
    - "Save & Mark Complete" button (primary)
    - "Save & Email to Client" (if shared)
    - Auto-save indicator: "Last saved 2 minutes ago"

13. **Templates** (Optional):
    - "Load Template" dropdown
    - Pre-filled sections for common session types
    - Custom templates saveable

**Validation & Compliance**:
- Required fields highlighted
- Character minimums enforced (professional standards)
- "Incomplete note" warning if missing critical info
- HIPAA/data protection compliance notice

**Interaksi & Behavior:**
- Auto-save every 60 seconds
- Rich text editor with formatting
- Template system for efficiency
- Mobile-responsive (tablet-friendly)
- Voice-to-text option (speech recognition)

**User Flow:**
After session → Add session notes → Fill all sections → Review → Save → Notes stored in client record

---

#### H. Therapist Session History

**Deskripsi:**
Session History page menampilkan comprehensive list dari semua sessions yang telah dilakukan oleh therapist, dengan filtering dan analytics capabilities.

**Elemen Utama:**
1. **Page Header**:
   - Title: "Session History"
   - Total sessions completed count
   - Date range selector

2. **Summary Statistics Cards**:
   - **Total Sessions**: 487
   - **This Month**: 42 (+8 from last month)
   - **Completion Rate**: 96%
   - **Average Duration**: 58 minutes

3. **Filter Section**:
   - Search: "Search by client name or session ID..."
   - Filters:
     * Date range (calendar picker)
     * Status: All, Completed, Cancelled, No-show
     * Session type: All, Online, Offline
     * Service: All services dropdown
     * Client: Select specific client
   - "Apply Filters" button
   - "Clear All" link

4. **Sort Options**:
   - Dropdown: Recent First, Oldest First, Client Name A-Z, Duration

5. **Sessions Table/List**:
   - Columns:
     * **Date & Time**: Sortable
     * **Client**: Name + avatar, clickable to profile
     * **Service**: Service name + badge
     * **Duration**: Actual time spent
     * **Type**: Online/Offline icon
     * **Status**: Badge (Completed/Cancelled/No-show)
     * **Rating**: Client rating (if given)
     * **Notes**: Icon indicator (green if notes added)
     * **Actions**: Dropdown menu
   
   - Row actions:
     * View Details
     * View/Edit Notes
     * View Recording (if available)
     * Generate Report
     * Copy Session Details

6. **Session Detail Modal**:
   - Opens when row clicked
   - Displays:
     * All session information
     * Session notes (if added)
     * Client feedback/rating
     * Payment details
     * Recording link (if applicable)
   - "Edit Notes" button
   - "Download Report" button

7. **Bulk Actions**:
   - Select multiple sessions (checkboxes)
   - Bulk export (CSV/PDF)
   - Generate summary report

8. **Analytics Section** (Collapsible):
   - "Session Analytics"
   - Charts:
     * Sessions per month (bar chart)
     * Online vs Offline ratio (pie chart)
     * Services distribution (donut chart)
     * Completion rate trend (line chart)
   - "View Detailed Analytics" link

9. **Export Options**:
   - "Export Session History" button
   - Format options: CSV, Excel, PDF
   - Date range selection for export
   - Include notes? (checkbox)

10. **Pagination**:
    - Standard pagination controls
    - Items per page: 10, 25, 50, 100
    - Total pages indicator

**Interaksi & Behavior:**
- Real-time search filtering
- Sortable columns
- Expandable rows for quick view
- Modal detail view
- Lazy loading for performance
- Export generates async (download when ready)

**User Flow:**
Therapist → Session History → Filter/search sessions → View details → Export atau analyze data

---

#### I. Therapist Earnings Dashboard

**Deskripsi:**
Earnings Dashboard memberikan comprehensive overview tentang pendapatan therapist, payment history, dan withdrawal management.

**Elemen Utama:**
1. **Page Header**:
   - Title: "My Earnings"
   - Total lifetime earnings (large, prominent)

2. **Earnings Summary Cards**:
   - **Available Balance**:
     * Amount: Rp 4.250.000
     * Ready for withdrawal
     * "Request Withdrawal" button (primary)
   
   - **Pending Balance**:
     * Amount: Rp 1.800.000
     * From recent sessions (not yet cleared)
     * "View Details" link
   
   - **This Month Earnings**:
     * Amount: Rp 6.500.000
     * +12% from last month
     * Progress bar to monthly goal
   
   - **Total Withdrawn**:
     * Amount: Rp 45.000.000
     * Lifetime total

3. **Earnings Chart**:
   - "Earnings Over Time"
   - Line chart showing monthly earnings
   - Toggle: Last 6 months, Last Year, All Time
   - Interactive: Hover untuk exact amounts
   - Goal line overlay (if set)

4. **Recent Transactions Table**:
   - "Recent Earnings"
   - Columns:
     * Date
     * Client Name
     * Service
     * Session Duration
     * Amount Earned
     * Platform Fee
     * Net Amount
     * Status (Cleared/Pending)
   - Filter by date range
   - Export option

5. **Breakdown Section**:
   - **By Service Type**:
     * Pie chart showing earnings distribution
     * Table: Service | Sessions | Total Earned
   
   - **By Session Type**:
     * Online vs Offline earnings comparison
     * Bar chart

6. **Withdrawal History**:
   - "Past Withdrawals"
   - List of withdrawal requests:
     * Date requested
     * Amount
     * Method (Bank Transfer/E-Wallet)
     * Status: Processing/Completed/Failed
     * Transaction ID
     * "View Receipt" link
   - Pagination

7. **Request Withdrawal Section**:
   - "Withdraw Funds" button opens modal:
     * Available balance shown
     * Amount input (validate min/max)
     * Withdrawal method:
       - Bank transfer (default)
         * Bank name dropdown
         * Account number
         * Account holder name
       - E-Wallet options
         * GoPay, OVO, Dana
         * Phone number/account
     * Processing time: "2-3 business days"
     * Fees: "No fees for bank transfer"
     * "Confirm Withdrawal" button
   - Confirmation screen after request

8. **Payment Settings**:
   - "Payment Methods"
   - Saved bank accounts/e-wallets
   - "Add New Payment Method" button
   - Set default method

9. **Tax Information** (If applicable):
   - "Tax Summary"
   - Year-to-date earnings
   - Estimated tax (if applicable)
   - "Download Tax Report" (for filing)

10. **Earnings Goals**:
    - "Set Monthly Goal"
    - Target amount input
    - Progress visualization
    - "You're 85% to your goal!"

11. **Commission Structure**:
    - Info section: "How Earnings Work"
    - Platform fee: 15% per session
    - Payment schedule: Weekly clearance
    - Withdrawal policies link

**Interaksi & Behavior:**
- Real-time balance updates
- Chart interactions (hover, zoom)
- Withdrawal form validation
- Success/error notifications
- Confirmation emails for withdrawals
- Mobile-responsive tables

**User Flow:**
Therapist → Earnings → View balance → Request withdrawal → Select method → Confirm → Wait processing → Receive payment

---

#### J. Therapist Profile Edit Page

**Deskripsi:**
Profile Edit page memungkinkan therapist untuk update informasi professional mereka yang ditampilkan kepada clients. Ini penting untuk maintaining accurate dan attractive therapist profiles.

**Elemen Utama:**
1. **Page Header**:
   - Title: "Edit My Profile"
   - "Preview Public Profile" button (see as clients see)
   - Last updated date

2. **Profile Sections** (Tabs atau Accordion):

   **A. Basic Information**:
   - Profile Photo:
     * Current photo display (large)
     * "Change Photo" button (upload)
     * Guidelines: "Professional headshot, max 5MB, JPG/PNG"
     * Crop tool after upload
   
   - Full Name (required)
   - Title/Credentials: "Dr.", "CHT", "M.Psi", etc.
   - Gender dropdown
   - Date of Birth (for age calculation)
   - Contact Information:
     * Email (verified badge)
     * Phone number (verified)
     * Alternative contact

   **B. Professional Information**:
   - License Number (required, verified)
   - License Expiry Date
   - Issuing Authority
   - Professional Title: Dropdown (Clinical Hypnotherapist, Licensed Therapist, etc.)
   - Years of Experience: Number input
   - Languages Spoken: Multi-select (Indonesian, English, Mandarin, etc.)
   - Specializations:
     * Multi-select checkboxes:
       - Stress & Anxiety Management
       - Weight Management
       - Smoking Cessation
       - Phobia Treatment
       - Sleep Disorders
       - Trauma Healing
       - Pain Management
       - Confidence Building
     * Primary specialization (radio, must select one)

   **C. About Me**:
   - Professional Bio:
     * Rich text editor
     * Character limit: 500 words
     * Guidelines: "Describe your approach, experience, and what makes you unique"
     * Word count display
   
   - Therapy Approach:
     * Dropdown: Cognitive Behavioral, Psychodynamic, Holistic, Solution-Focused, etc.
   
   - Why I Became a Therapist:
     * Textarea (optional)
     * 200 words

   **D. Education & Certifications**:
   - "Add Education" button:
     * Degree: Dropdown (Bachelor's, Master's, Doctorate)
     * Field of Study
     * University/Institution
     * Graduation Year
     * Remove entry button
   
   - "Add Certification" button:
     * Certification Name
     * Issuing Organization
     * Issue Date
     * Expiry Date (if applicable)
     * Certificate ID
     * Upload Certificate (PDF/Image)
     * Remove entry button
   
   - Reorder entries (drag & drop)

   **E. Services & Pricing**:
   - List of services offered:
     * Each service:
       - Service name (from catalog)
       - Offer this service? (checkbox)
       - Your price: Input (Rp)
       - Recommended price: Rp 250K - 350K (info)
       - Default duration: 30/60/90 min
   
   - Consultation Fee:
     * First session price (can be different)
     * Follow-up session price

   **F. Media & Portfolio**:
   - Video Introduction:
     * Upload video (max 2 min, 50MB)
     * YouTube/Vimeo link (alternative)
     * Guidelines: "Introduce yourself and your approach"
   
   - Photo Gallery:
     * Upload up to 5 photos
     * Office/workspace photos
     * Drag to reorder
     * Set primary photo
   
   - Testimonials (optional):
     * Manually add testimonials
     * Client name (or anonymous)
     * Testimonial text
     * Rating

   **G. Social Media & Website**:
   - LinkedIn URL
   - Instagram handle
   - Facebook page
   - Professional website
   - Publications/Articles links

3. **Visibility Settings**:
   - Profile Status:
     * Active (Accepting new clients)
     * Limited availability
     * Not accepting new clients
   
   - Display on Directory:
     * Public (visible to all)
     * Private (only direct links)

4. **Verification Status**:
   - Badges shown:
     * ✓ Email Verified
     * ✓ Phone Verified
     * ✓ License Verified
     * ✓ Identity Verified
   - "Request Re-verification" if needed

5. **Preview Mode**:
   - "Preview Changes" button
   - Shows how profile appears to clients
   - Side-by-side comparison (old vs new)

6. **Save Section**:
   - "Save Changes" button (primary, sticky bottom)
   - "Discard Changes" button
   - "Save as Draft" (for incomplete edits)
   - Validation errors highlighted
   - Success notification: "Profile updated successfully!"

**Validation & Requirements**:
- Required fields marked with *
- Image size/format validation
- Character limits enforced
- License verification required
- Professional photo guidelines

**Interaksi & Behavior:**
- Auto-save drafts every 2 minutes
- Image cropping tool
- Rich text editor with formatting
- Drag & drop reordering
- Preview live updates
- Mobile-responsive forms

**User Flow:**
Therapist → Profile Settings → Edit sections → Upload media → Preview changes → Save → Profile updated on public directory

---

### 4.3.5.9 Mockup Admin Dashboard (Admin Dashboard Pages)

Admin Dashboard adalah area khusus untuk administrator sistem yang memiliki akses penuh untuk manage users, bookings, finances, dan system settings. Interface dirancang untuk efficiency dan comprehensive data management.

---

**[GAMBAR 4.51 - Mockup: Admin Dashboard Main]** 👔
_Admin dashboard - System stats, charts, recent activities_

**[GAMBAR 4.52 - Mockup: Admin Users Management]** 👔
_Admin - Table of all users (clients, therapists) with CRUD actions_

**[GAMBAR 4.53 - Mockup: Admin Therapist Approval]** 👔
_Admin - Review therapist applications, approve/reject_

**[GAMBAR 4.54 - Mockup: Admin Services Management]** 👔
_Admin - CRUD services: name, price, description, status_

**[GAMBAR 4.55 - Mockup: Admin Bookings Management]** 👔
_Admin - View/edit all bookings, override statuses_

**[GAMBAR 4.56 - Mockup: Admin Payment Verification]** 👔
_Admin - Manual payment verification, approve/reject proofs_

**[GAMBAR 4.57 - Mockup: Admin Financial Reports]** 👔
_Admin - Revenue charts, transaction reports, export data_

**[GAMBAR 4.58 - Mockup: Admin Activity Logs]** 👔
_Admin - System audit trail, user actions, timestamps_

**[GAMBAR 4.59 - Mockup: Admin System Settings]** 👔
_Admin - Configure system parameters, maintenance mode_

**[GAMBAR 4.60 - Mockup: Admin Notifications Management]** 👔
_Admin - Send bulk notifications, manage templates_

---

#### A. Admin Dashboard (Main)

**Deskripsi:**
Admin Dashboard Main adalah command center untuk system administrators, providing high-level overview of platform operations, key metrics, dan quick access to management functions.

**Elemen Utama:**
1. **Top Navigation**:
   - CUR-HEART Admin logo
   - Global search bar (users, bookings, transactions)
   - Notification bell (system alerts)
   - Admin profile dropdown

2. **Sidebar Navigation**:
   - Dashboard (active)
   - Users Management
   - Bookings Management
   - Financial Reports
   - System Settings
   - Support Tickets
   - Analytics
   - Logs & Audit

3. **Key Metrics Cards** (Top Row):
   - **Total Users**:
     * Number: 1,523
     * Breakdown: Clients (1,250) | Therapists (58) | Admins (15)
     * Trend: +45 this week
   
   - **Active Sessions Today**:
     * Number: 37
     * Online: 28 | Offline: 9
     * Real-time counter
   
   - **Total Revenue (Month)**:
     * Amount: Rp 127.500.000
     * +18% from last month
     * Chart icon link to details
   
   - **Platform Health**:
     * Status: All Systems Operational (green)
     * Uptime: 99.8%
     * Link to status page

4. **Revenue Chart**:
   - "Revenue Overview"
   - Line/area chart showing daily revenue
   - Toggle: Last 7 days, 30 days, 3 months, Year
   - Compare with previous period (overlay)
   - Total and average displayed

5. **Recent Bookings Table**:
   - "Latest Bookings"
   - Columns:
     * Booking ID (clickable)
     * Client name
     * Therapist name
     * Service
     * Date & Time
     * Amount
     * Status badge
     * Actions (View, Cancel, Refund)
   - "View All Bookings" link

6. **User Growth Chart**:
   - "User Registrations"
   - Bar chart: New users per day/week
   - Split by type: Clients vs Therapists
   - Toggle time periods

7. **System Alerts Panel**:
   - "Important Alerts"
   - List of alerts:
     * "5 pending therapist applications"
     * "2 payment disputes need review"
     * "Server maintenance scheduled: Nov 10"
     * "3 support tickets unresolved"
   - Priority badges (High, Medium, Low)
   - Quick action buttons

8. **Top Performing Therapists**:
   - "Top Therapists This Month"
   - Leaderboard (top 5):
     * Rank
     * Therapist name + photo
     * Sessions completed
     * Revenue generated
     * Average rating
   - "View Full Report" link

9. **Top Services**:
   - "Most Booked Services"
   - Horizontal bar chart
   - Service name | Bookings count | Percentage
   - Total revenue per service

10. **Quick Actions Section**:
    - Large action buttons:
      * "Add New User"
      * "Review Therapist Applications"
      * "Generate Report"
      * "View Support Tickets"
      * "System Settings"

11. **Activity Feed**:
    - "Recent Activity"
    - Timeline of recent actions:
      * New user registrations
      * Bookings created/cancelled
      * Payments processed
      * Therapist applications
      * Reviews submitted
    - Real-time updates
    - "View All Activity" link

12. **Platform Statistics**:
    - Additional metrics:
      * Total bookings (lifetime): 8,523
      * Average session duration: 57 min
      * Cancellation rate: 4.2%
      * Client satisfaction: 4.8/5.0
      * Platform fee collected: Rp 18.5M (month)

**Interaksi & Behavior:**
- Real-time data updates (WebSocket)
- Interactive charts (click for details)
- Customizable dashboard widgets
- Export capabilities for all data
- Responsive design for tablets

**User Flow:**
Admin login → Dashboard → High-level overview → Identify issues/trends → Navigate to specific management areas

---

#### B. Admin Users Management

**Deskripsi:**
Users Management page memungkinkan admin untuk view, search, filter, edit, dan manage semua users dalam platform (clients, therapists, admins).

**Elemen Utama:**
1. **Page Header**:
   - Title: "Users Management"
   - Total users count dengan breakdown
   - "Add New User" button (manual creation)
   - "Export Users" button (CSV)

2. **Tabs Navigation**:
   - All Users
   - Clients (badge count)
   - Therapists (badge count)
   - Admins
   - Pending Approvals (therapist applications)
   - Suspended/Banned

3. **Search & Filter Section**:
   - Global search: "Search by name, email, ID..."
   - Advanced filters:
     * User type: All, Client, Therapist, Admin
     * Status: Active, Inactive, Pending, Suspended, Banned
     * Registration date range
     * Last login date
     * Verification status: Email, Phone, License (for therapists)
     * Location (city/region)
   - Sort options: Recent, Name A-Z, Most Active

4. **Users Table**:
   - Columns:
     * **ID**: User ID (clickable)
     * **User**: Avatar + Name + Email
     * **Type**: Badge (Client/Therapist/Admin)
     * **Status**: Badge (Active/Inactive/Suspended)
     * **Registered**: Date
     * **Last Login**: Relative time
     * **Total Sessions**: Count (if applicable)
     * **Spent/Earned**: Amount
     * **Verification**: Icons (✓ email, ✓ phone, ✓ license)
     * **Actions**: Dropdown menu
   
   - Row hover: Highlight
   - Clickable rows: View details

5. **Bulk Actions**:
   - Select multiple users (checkboxes)
   - Bulk operations:
     * Export selected
     * Send mass email
     * Change status (activate/suspend)
     * Delete users (with confirmation)

6. **User Actions Menu** (Per Row):
   - View Profile
   - Edit User
   - Impersonate (login as user for troubleshooting)
   - Send Email
   - View Activity Log
   - Suspend/Activate Account
   - Reset Password
   - Delete User

7. **User Detail Modal** (Quick View):
   - Opens when row clicked
   - Tabs:
     * **Overview**:
       - Full profile information
       - Registration details
       - Verification status
       - Account statistics
     
     * **Activity**:
       - Login history
       - Actions timeline
       - Sessions history (if applicable)
     
     * **Transactions**:
       - Payment history
       - Earnings (if therapist)
       - Refunds
     
     * **Notes**:
       - Admin notes on user
       - Flags/warnings
       - Communication history
   
   - Action buttons:
     * Edit Profile
     * Suspend/Activate
     * Send Message
     * View Full Profile

8. **Pending Therapist Applications** (Tab):
   - List of therapist applications awaiting approval
   - Each application:
     * Applicant info
     * Submitted documents
     * Application date
     * Review status: Pending, Under Review, Approved, Rejected
   - Actions:
     * View Application Details
     * Approve (opens confirmation)
     * Reject (requires reason)
     * Request More Info

9. **Add/Edit User Modal**:
   - Form fields:
     * User type selection
     * Personal information
     * Contact details
     * Account status
     * Permissions (for admins)
   - Validation
   - "Create User" / "Save Changes" button

10. **Statistics Section**:
    - User growth chart
    - Active users trend
    - Retention rate
    - Churn rate

11. **Export Options**:
    - Export all or filtered users
    - Format: CSV, Excel
    - Fields to include: Checkboxes
    - "Generate Export" button

**Interaksi & Behavior:**
- Real-time search with debounce
- Sortable columns
- Filter combinations
- Modal quick actions
- Confirmation dialogs for destructive actions
- Activity logging for admin actions
- Pagination with configurable items per page

**User Flow:**
Admin → Users Management → Filter users → View details → Take action (edit, suspend, approve, etc.)

---

#### C. Admin Bookings Management

**Deskripsi:**
Bookings Management page memberikan admin comprehensive control atas semua appointments dalam platform, termasuk monitoring, modifying, dan resolving booking-related issues.

**Elemen Utama:**
1. **Page Header**:
   - Title: "Bookings Management"
   - Total bookings count
   - Date range selector (view specific period)

2. **Summary Statistics Cards**:
   - **Total Bookings (Period)**: 1,247
   - **Upcoming**: 342
   - **Completed**: 853
   - **Cancelled**: 52 (4.2%)
   - **No-Shows**: 15 (1.2%)
   - **Revenue Generated**: Rp 374.100.000

3. **Tabs Navigation**:
   - All Bookings
   - Upcoming
   - Today's Sessions
   - Completed
   - Cancelled
   - Disputed/Issues

4. **Search & Filter**:
   - Search: "Booking ID, client, or therapist name..."
   - Filters:
     * Date range (from - to)
     * Status: All, Confirmed, Pending Payment, Completed, Cancelled, No-show
     * Service type: All services dropdown
     * Session type: All, Online, Offline
     * Therapist: Select specific therapist
     * Client: Select specific client
     * Payment status: All, Paid, Pending, Refunded
     * Amount range: Min - Max
   - "Apply Filters" button

5. **Bookings Table**:
   - Columns:
     * **Booking ID**: #BK-2024-XXXXX (clickable)
     * **Date & Time**: Scheduled date/time
     * **Client**: Name + avatar (link to profile)
     * **Therapist**: Name + avatar (link to profile)
     * **Service**: Service name
     * **Duration**: Minutes
     * **Type**: Online/Offline badge
     * **Amount**: Price in Rp
     * **Payment**: Status badge (Paid/Pending/Refunded)
     * **Status**: Booking status badge
     * **Actions**: Dropdown menu
   
   - Color coding:
     * Upcoming: Blue
     * Completed: Green
     * Cancelled: Red
     * Issues: Orange

6. **Booking Actions Menu**:
   - View Details
   - Edit Booking
   - Reschedule (on behalf)
   - Cancel Booking
   - Process Refund
   - Contact Client
   - Contact Therapist
   - View Session Notes
   - Mark as Completed/No-show
   - Flag for Review

7. **Booking Detail Modal**:
   - Comprehensive view:
     * Full booking information
     * Client details
     * Therapist details
     * Service details
     * Payment details
     * Transaction history
     * Communication logs
     * Session notes (if completed)
     * Timestamps (created, confirmed, completed, etc.)
   
   - Action buttons:
     * Edit
     * Cancel dengan refund options
     * Reschedule
     * Generate Invoice
     * Send Reminder
     * Mark Completed

8. **Bulk Operations**:
   - Select multiple bookings
   - Bulk actions:
     * Export selected
     * Send reminders
     * Cancel multiple (with confirmation)
     * Change status
     * Generate reports

9. **Disputed Bookings** (Tab):
   - Bookings flagged for issues:
     * Payment disputes
     * Client complaints
     * Therapist reports
     * Refund requests
   - Each dispute:
     * Booking details
     * Issue type
     * Description
     * Reporter
     * Status: Open, Under Review, Resolved
   - Actions:
     * Review Dispute
     * Resolve (with resolution notes)
     * Process Refund
     * Contact Parties

10. **Calendar View** (Optional):
    - Toggle to calendar visualization
    - Shows all bookings on calendar
    - Color-coded by status
    - Click date → See bookings list
    - Click booking → Detail view

11. **Analytics Section**:
    - "Booking Trends"
    - Charts:
      * Bookings per day (line chart)
      * Service distribution (pie chart)
      * Completion rate over time
      * Cancellation reasons (bar chart)
    - Export analytics

12. **Export & Reports**:
    - "Generate Booking Report"
    - Select date range
    - Choose fields to include
    - Format: CSV, Excel, PDF
    - Schedule automated reports (daily/weekly/monthly)

**Interaksi & Behavior:**
- Real-time updates for new bookings
- Advanced search dengan autocomplete
- Inline editing for quick changes
- Confirmation modals for critical actions
- Status change tracking
- Automatic refund calculations
- Email notifications on actions

**User Flow:**
Admin → Bookings Management → Filter bookings → View details → Take action (reschedule, cancel, refund) → Log resolution

---

#### D. Admin Financial Reports

**Deskripsi:**
Financial Reports page memberikan admin detailed insights tentang revenue, payments, withdrawals, dan financial health dari platform.

**Elemen Utama:**
1. **Page Header**:
   - Title: "Financial Reports"
   - Date range selector (custom periods)
   - "Export Financial Report" button

2. **Revenue Summary Cards**:
   - **Total Revenue (Period)**:
     * Amount: Rp 127.500.000
     * Trend vs previous period
   
   - **Platform Fees Collected**:
     * Amount: Rp 19.125.000 (15% of revenue)
     * Trend
   
   - **Therapist Earnings**:
     * Amount: Rp 108.375.000 (85% of revenue)
     * Pending: Rp 12.5M
     * Withdrawn: Rp 95.8M
   
   - **Outstanding Payments**:
     * Amount: Rp 3.250.000
     * Pending bookings

3. **Revenue Chart**:
   - "Revenue Over Time"
   - Line chart:
     * Total revenue
     * Platform fees
     * Therapist payouts
   - Toggle: Daily, Weekly, Monthly, Yearly
   - Compare periods: Overlay previous period
   - Interactive tooltips

4. **Revenue Breakdown**:
   - **By Service Type**:
     * Table: Service | Sessions | Revenue | Percentage
     * Pie chart visualization
   
   - **By Session Type**:
     * Online vs Offline revenue
     * Bar chart comparison
   
   - **By Payment Method**:
     * Credit Card, Bank Transfer, E-Wallet, etc.
     * Distribution percentages

5. **Transactions Table**:
   - "All Transactions"
   - Columns:
     * Transaction ID
     * Date & Time
     * Type: Payment Received, Refund, Withdrawal, etc.
     * Booking ID (link)
     * Client/Therapist
     * Amount
     * Payment Method
     * Status: Successful, Pending, Failed, Refunded
     * Platform Fee
     * Net Amount
   - Filter by transaction type, status, date
   - Export transactions

6. **Withdrawals Management**:
   - "Therapist Withdrawal Requests"
   - Table:
     * Request ID
     * Therapist name
     * Amount requested
     * Date requested
     * Withdrawal method
     * Status: Pending, Processing, Completed, Failed
     * Actions: Approve, Reject, Mark Completed
   
   - Approve/Reject actions:
     * Verification checks
     * Process payment
     * Update status
     * Send notification

7. **Refunds Management**:
   - "Refund Requests & History"
   - Table:
     * Refund ID
     * Original booking
     * Client name
     * Refund amount
     * Reason
     * Request date
     * Status: Pending, Approved, Processed, Rejected
     * Actions: Review, Approve, Process, Reject
   
   - Refund processing:
     * Verify eligibility
     * Calculate amount (full/partial per policy)
     * Process to original payment method
     * Update booking status
     * Notify client

8. **Financial Analytics**:
   - "Key Financial Metrics"
   - Metrics:
     * Average transaction value
     * Revenue per session
     * Platform fee percentage
     * Refund rate
     * Payment success rate
     * Average therapist earnings
   - Charts and visualizations

9. **Tax Reports** (If applicable):
   - "Tax Summary"
   - Downloadable tax documents
   - Quarterly reports
   - Annual statements
   - Export for accounting software

10. **Disputes & Chargebacks**:
    - "Payment Disputes"
    - List of disputed transactions
    - Chargeback notifications
    - Resolution tracking
    - Actions: Respond, Provide Evidence, Accept, Contest

11. **Payment Gateway Status**:
    - Integration health checks
    - Transaction success rates per gateway
    - Downtime alerts
    - Provider fees comparison

12. **Scheduled Reports**:
    - "Automated Reports"
    - Setup recurring financial reports
    - Recipients (email list)
    - Frequency: Daily, Weekly, Monthly
    - Report type: Revenue, Transactions, Tax
    - "Add New Scheduled Report" button

**Interaksi & Behavior:**
- Real-time transaction updates
- Interactive charts (drill-down)
- Excel/PDF export with formatting
- Secure data handling
- Role-based access (senior admins only)
- Audit logging for all financial actions

**User Flow:**
Admin → Financial Reports → Select period → Analyze data → Process withdrawals/refunds → Generate reports → Export for accounting

---

#### E. Admin System Settings

**Deskripsi:**
System Settings page memungkinkan admin untuk configure global platform settings, manage system preferences, dan control various operational parameters.

**Elemen Utama:**
1. **Page Header**:
   - Title: "System Settings"
   - Last modified: Date + Admin name
   - "Save All Changes" button (sticky)

2. **Settings Categories** (Sidebar Navigation):
   - General Settings
   - Booking Settings
   - Payment Settings
   - Email & Notifications
   - Security & Privacy
   - Platform Policies
   - Integrations
   - Advanced

3. **General Settings**:
   - **Platform Information**:
     * Platform name: "CUR-HEART"
     * Tagline
     * Description
     * Logo upload (light & dark versions)
     * Favicon upload
   
   - **Contact Information**:
     * Support email
     * Phone number
     * Address
     * Business hours
   
   - **Timezone & Locale**:
     * Default timezone: Asia/Jakarta
     * Date format: DD/MM/YYYY, MM/DD/YYYY
     * Time format: 12-hour, 24-hour
     * Currency: IDR
     * Language: Indonesian, English

4. **Booking Settings**:
   - **Booking Rules**:
     * Minimum advance booking time: Hours dropdown
     * Maximum advance booking time: Weeks dropdown
     * Allow same-day bookings: Toggle
     * Default session duration: Minutes
     * Buffer time between sessions: Minutes
   
   - **Cancellation Policy**:
     * Free cancellation period: 24 hours
     * Partial refund period: 12-24 hours (50%)
     * No refund period: <12 hours
     * No-show policy
   
   - **Booking Limits**:
     * Max bookings per client per day: Number
     * Max bookings per therapist per day: Number
     * Enable waitlist: Toggle

5. **Payment Settings**:
   - **Payment Gateways**:
     * Midtrans configuration:
       - Server key (hidden)
       - Client key
       - Merchant ID
       - Enable sandbox mode: Toggle
     * Status: Connected (green) / Disconnected
     * "Test Connection" button
   
   - **Payment Methods**:
     * Enable/disable methods:
       - Credit/Debit Cards (toggle)
       - Bank Transfer (toggle)
       - E-Wallets (GoPay, OVO, Dana, ShopeePay)
       - Virtual Account (toggle)
   
   - **Pricing & Fees**:
     * Platform fee percentage: 15% (input)
     * Minimum booking amount: Rp 100.000
     * Currency settings
   
   - **Refund Settings**:
     * Auto-approve refunds under: Rp amount
     * Refund processing time: Days
     * Enable partial refunds: Toggle

6. **Email & Notifications**:
   - **Email Configuration**:
     * SMTP settings:
       - Host
       - Port
       - Username
       - Password
       - Encryption (TLS/SSL)
     * From email address
     * From name: "CUR-HEART"
     * "Send Test Email" button
   
   - **Email Templates**:
     * List of templates:
       - Welcome email
       - Booking confirmation
       - Booking reminder
       - Session completed
       - Payment receipt
       - Password reset
       - etc.
     * Each template: Preview, Edit buttons
   
   - **Notification Preferences**:
     * Email notifications enable/disable
     * SMS notifications (if integrated)
     * Push notifications
     * In-app notifications

7. **Security & Privacy**:
   - **Authentication**:
     * Password requirements:
       - Minimum length: 8 characters
       - Require uppercase: Toggle
       - Require numbers: Toggle
       - Require special characters: Toggle
     * Session timeout: Minutes
     * Two-factor authentication (2FA):
       - Enable for admins: Toggle
       - Enable for therapists: Toggle
       - Enable for clients: Toggle
   
   - **Data Protection**:
     * Data encryption: Enabled (read-only)
     * Automatic backups: Daily
     * Backup retention: Days
     * GDPR compliance: Enabled
     * Data retention policy: Years
   
   - **Privacy Settings**:
     * Show therapist full names: Toggle
     * Show client reviews publicly: Toggle
     * Allow profile indexing (SEO): Toggle

8. **Platform Policies**:
   - **Terms & Conditions**:
     * Rich text editor
     * Last updated date
     * "Save Changes" button
   
   - **Privacy Policy**:
     * Rich text editor
     * Last updated date
   
   - **Cancellation Policy**:
     * Rich text editor
   
   - **Community Guidelines**:
     * Rich text editor

9. **Integrations**:
   - **Google Analytics**:
     * Tracking ID input
     * Enable: Toggle
     * Status: Connected
   
   - **Google Calendar**:
     * OAuth connection
     * "Connect" button
   
   - **Video Conferencing**:
     * Provider: Jitsi, Zoom, custom
     * API credentials
   
   - **SMS Gateway** (Optional):
     * Provider selection
     * API key
     * Enable: Toggle
   
   - **Social Media**:
     * Facebook login (OAuth)
     * Google login (OAuth)
     * Enable/disable toggles

10. **Advanced Settings**:
    - **Maintenance Mode**:
      * Enable maintenance mode: Toggle
      * Maintenance message: Textarea
      * Allowed IPs: Comma-separated
    
    - **System Performance**:
      * Cache settings
      * Session handling
      * CDN configuration
    
    - **API Settings**:
      * API rate limiting
      * API keys management
      * Webhook configurations
    
    - **Logs & Debugging**:
      * Enable error logging: Toggle
      * Log level: Debug, Info, Warning, Error
      * Log retention: Days
      * "View Logs" button
      * "Clear Logs" button

11. **Save & Apply**:
    - "Save All Changes" button (sticky footer)
    - "Reset to Defaults" button
    - Confirmation: "Settings saved successfully"
    - Warning for critical changes: "This will affect all users"

**Validation & Safety**:
- Critical settings require confirmation
- Backup before major changes
- Settings validation before save
- Rollback capability
- Audit logging for all changes

**Interaksi & Behavior:**
- Auto-save drafts
- Validation on blur
- Preview changes before apply
- Test buttons for integrations
- Confirmation modals for critical settings
- Real-time status indicators
- Responsive forms

**User Flow:**
Admin → System Settings → Navigate to category → Modify settings → Test (if applicable) → Save → Confirm → Settings applied platform-wide

---

### 4.3.5.10 Responsive Design Approach

Dalam pengembangan UI/UX CUR-HEART, pendekatan responsive design diterapkan untuk memastikan aplikasi dapat diakses dan digunakan secara optimal di berbagai perangkat (desktop, tablet, mobile). Berikut adalah strategi dan implementasi responsive design:

**Breakpoint Strategy:**
- **Mobile Portrait**: 320px - 575px (iPhone SE, small phones)
- **Mobile Landscape**: 576px - 767px
- **Tablet Portrait**: 768px - 991px (iPad)
- **Tablet Landscape / Small Desktop**: 992px - 1199px
- **Desktop**: 1200px - 1439px
- **Large Desktop**: 1440px+ (Full HD, 4K)

**Responsive Patterns Implemented:**

1. **Navigation Adaptations**:
   - Desktop: Horizontal top nav + sidebar for dashboards
   - Tablet: Collapsible sidebar, hamburger menu
   - Mobile: Bottom navigation bar (sticky), hamburger side drawer

2. **Grid Layouts**:
   - Desktop: 3-4 columns for cards/content
   - Tablet: 2-3 columns
   - Mobile: Single column, vertical stacking

3. **Typography Scaling**:
   - Desktop: H1 (36px), Body (16px)
   - Tablet: H1 (30px), Body (15px)
   - Mobile: H1 (24px), Body (14px)
   - Line height adjusts: 1.2x to 1.6x for readability

4. **Forms & Inputs**:
   - Desktop: Multi-column forms, inline labels
   - Mobile: Single column, labels above inputs, larger touch targets (44px minimum)

5. **Tables**:
   - Desktop: Full table with all columns
   - Tablet: Scrollable horizontal, priority columns visible
   - Mobile: Card-based layout, stack data vertically, swipe to see more

6. **Modals & Dialogs**:
   - Desktop: Centered modal with overlay (max-width 600-800px)
   - Mobile: Fullscreen modal, slide up from bottom

7. **Images & Media**:
   - Responsive images with srcset
   - Lazy loading
   - Aspect ratio maintained
   - Touch-friendly galleries with swipe

8. **Dashboard Widgets**:
   - Desktop: Multi-column grid, drag & drop
   - Mobile: Single column, priority order, collapsible sections

9. **Charts & Graphs**:
   - SVG-based (scalable)
   - Simplified views on mobile
   - Touch-friendly interactions (pinch, zoom)

**Touch & Gesture Optimization:**
- Minimum touch target: 44x44px (Apple HIG standard)
- Adequate spacing between interactive elements
- Swipe gestures: Carousel navigation, slide-to-delete
- Pull-to-refresh on mobile
- Long-press context menus

**Performance Optimization:**
- Progressive Web App (PWA) capabilities
- Service workers for offline functionality
- Code splitting per route
- Image optimization (WebP format)
- Lazy loading non-critical components
- Minimal third-party scripts

**Testing Strategy:**
- Device testing: iPhone (iOS), Samsung/Pixel (Android), iPad, MacBook, Windows laptops
- Browser compatibility: Chrome, Safari, Firefox, Edge
- Screen reader testing (accessibility)
- Touch target verification
- Orientation changes (portrait ↔ landscape)

---

### 4.3.5.11 User Experience (UX) Considerations

Selain visual design, pengalaman pengguna secara keseluruhan adalah fokus utama dalam pengembangan CUR-HEART. Berikut adalah pertimbangan UX yang diterapkan:

**1. User-Centered Design Principles:**
- **Empathy**: Memahami emotional state users yang seeking mental health support
- **Clarity**: Informasi disajikan secara jelas tanpa jargon medis berlebihan
- **Simplicity**: Booking flow yang straightforward (4 steps saja)
- **Consistency**: Pattern yang sama di seluruh aplikasi
- **Feedback**: Setiap action mendapat response (loading states, success/error messages)

**2. Accessibility (WCAG 2.1 AA Compliance):**
- **Color Contrast**: Minimum 4.5:1 untuk body text, 3:1 untuk large text
- **Keyboard Navigation**: Semua fungsi accessible via keyboard (Tab, Enter, Esc)
- **Screen Reader Support**: ARIA labels, semantic HTML
- **Focus Indicators**: Jelas dan visible untuk keyboard users
- **Alternative Text**: Semua images memiliki alt text
- **Captions & Transcripts**: Video content (jika ada)
- **Resizable Text**: Supports browser zoom hingga 200%

**3. Performance & Speed:**
- **Page Load Time**: Target <3 seconds untuk first contentful paint
- **Lazy Loading**: Images, components loaded on-demand
- **Caching Strategy**: Static assets cached, dynamic content fresh
- **Optimized Assets**: Compressed images, minified CSS/JS
- **Perceived Performance**: Skeleton screens, progressive loading

**4. Error Prevention & Recovery:**
- **Inline Validation**: Real-time feedback pada form inputs
- **Confirmation Dialogs**: Untuk destructive actions (delete, cancel booking)
- **Undo Capabilities**: Where possible (draft saving)
- **Clear Error Messages**: Specific, actionable guidance
- **Helpful Defaults**: Pre-filled sensible values

**5. User Onboarding:**
- **Welcome Tour**: First-time users guided through dashboard (optional)
- **Tooltips**: Contextual help on hover/click
- **Empty States**: Helpful messages dengan CTAs when no data
- **Progress Indicators**: Show users where they are in multi-step processes

**6. Trust & Security Indicators:**
- **SSL Badge**: "Secure connection" messaging
- **Privacy Notices**: Clear communication about data usage
- **Verified Badges**: Therapist license verification shown
- **Encryption Info**: "End-to-end encrypted" for video sessions
- **Professional Imagery**: High-quality, trust-building visuals

**7. Emotional Design:**
- **Calming Colors**: Navy & pink chosen for their calming psychological effect
- **Friendly Tone**: Copy writing yang empathetic dan supportive
- **Success Celebrations**: Confetti animation setelah booking (subtle joy)
- **Progress Recognition**: Badges, milestones untuk motivate clients
- **Human Touch**: Photos of real therapists (bukan stock photos generic)

**8. Micro-interactions:**
- **Button States**: Hover effects, active states, disabled states
- **Loading Animations**: Smooth spinners, progress bars
- **Transitions**: Fade ins, slide animations (fast, 200-300ms)
- **Form Feedback**: Checkmarks untuk valid inputs, shake animation untuk errors
- **Notification Toasts**: Slide in smoothly, auto-dismiss

**9. Content Strategy:**
- **Scannable Content**: Headings, bullet points, short paragraphs
- **Progressive Disclosure**: Show essential info first, details on-demand
- **Plain Language**: Avoid medical jargon, explain terms when necessary
- **Helpful Placeholders**: Example text dalam input fields
- **Contextual Help**: Info icons dengan tooltips

**10. Mobile-First Considerations:**
- **Thumb-Friendly**: Important actions within easy reach
- **Minimal Input**: Use pickers, dropdowns instead of typing where possible
- **Offline Capabilities**: Basic functionality when connection lost
- **Orientation Support**: Works in both portrait and landscape
- **Native Features**: Use device capabilities (camera, location, notifications)

**11. Personalization:**
- **Recommended Therapists**: Based on client preferences dan history
- **Personalized Dashboard**: Show relevant info per user type
- **Language Preferences**: Support Indonesian dan English
- **Notification Preferences**: Granular control over alerts
- **Saved Preferences**: Remember user choices (theme, filters, etc.)

**12. Continuous Improvement:**
- **Analytics Integration**: Track user behavior, identify pain points
- **A/B Testing**: Test variations untuk optimize conversions
- **User Feedback Mechanism**: In-app feedback forms, surveys
- **Usability Testing**: Regular sessions dengan real users
- **Iteration**: Continuous refinement based on data dan feedback

---

## 4.3.6 Kesimpulan Desain UI/UX

Desain antarmuka pengguna dan pengalaman pengguna (UI/UX) untuk sistem informasi CUR-HEART telah dikembangkan dengan pendekatan yang comprehensive dan user-centered. Dari 41 halaman mockup yang telah didokumentasikan, setiap halaman dirancang dengan mempertimbangkan kebutuhan spesifik dari tiga tipe pengguna utama: klien, terapis, dan administrator.

**Aspek-aspek kunci yang telah dicapai:**

1. **Design System yang Konsisten**: Color palette, typography, dan component library yang kohesif memastikan pengalaman yang seragam di seluruh aplikasi.

2. **User Flow yang Intuitif**: Proses booking yang disederhanakan menjadi 4 langkah, navigasi yang jelas, dan struktur informasi yang logis memudahkan users mencapai tujuan mereka.

3. **Responsive Design**: Mockup dirancang untuk bekerja optimal di desktop, tablet, dan mobile devices, dengan adaptasi layout yang sesuai untuk setiap breakpoint.

4. **Accessibility**: Pertimbangan terhadap WCAG guidelines memastikan aplikasi dapat digunakan oleh users dengan berbagai kemampuan.

5. **Trust & Security**: Visual indicators dan messaging yang menekankan keamanan data dan profesionalisme layanan, sangat penting untuk aplikasi kesehatan mental.

6. **Performance-Oriented**: Desain yang mempertimbangkan loading times, lazy loading, dan optimasi aset untuk pengalaman yang responsif.

Dengan design system dan mockup yang telah dikembangkan ini, tim development memiliki blueprint yang jelas untuk implementasi front-end, memastikan konsistensi visual dan fungsional yang akan menghasilkan user experience yang excellent untuk pengguna CUR-HEART.

**Dokumentasi visual lengkap dari 41 mockup halaman tersedia di:**
`/var/www/unm-s7/tugas-selesai/06_rintisan_bisnis_digital/mockups/`

Mockup-mockup tersebut dapat diakses dan di-review untuk implementasi development, user testing, dan stakeholder presentations.

---

*Catatan: Screenshot visual dan detail implementasi teknis dari setiap mockup dapat dilihat pada file HTML yang tersimpan di direktori mockups. Setiap file HTML merupakan functional prototype yang dapat dibuka di browser untuk melihat interaksi dan responsiveness secara langsung.*
