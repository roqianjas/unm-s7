# CUR-HEART DESIGN SYSTEM
## Complete Investor-Grade UI/UX Design Documentation

---

## 📋 **DESIGN SYSTEM OVERVIEW**

### **Brand Identity Evolution**
CUR-HEART telah berkembang menjadi comprehensive hypnotherapy platform dengan design system yang mencerminkan:

- **Professional Healthcare Standards** - Desain yang memenuhi standar medis
- **Investor-Ready Presentation** - Visual yang menarik untuk funding rounds
- **Complete User Journey** - Dari marketing website hingga business intelligence dashboard
- **Scalable Component Library** - Sistem yang dapat berkembang dengan produk
- **Evidence-Based Design** - Berdasarkan penelitian UX dalam healthcare

### **Platform Coverage**
- 🌐 **Marketing Website** (Homepage, About, Contact, Services)
- 📱 **Booking System** (4-step flow dengan AI matching)
- 👥 **Client Dashboard** (Progress tracking, session management)
- 🏥 **Therapist Dashboard** (Client management, scheduling)
- 📊 **Business Intelligence** (Analytics, reporting, insights)
- 💰 **Financial Management** (Revenue tracking, payment processing)

---

## 🎨 **COLOR PALETTE**

### **Primary Colors**

| Color | Hex Code | Usage | Psychology |
|-------|----------|-------|------------|
| **Ocean Blue** | `#2E86AB` | Primary CTA, Navigation, Links | Trust, professionalism, calm |
| **Deep Purple** | `#A23B72` | Secondary actions, Gradients | Wisdom, spirituality, transformation |
| **Warm Orange** | `#F18F01` | Accent, Highlights, Energy | Warmth, optimism, healing |
| **Calm Red** | `#C73E1D` | Important alerts, Warning states | Urgency without aggression |

### **Neutral Colors**

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Pure White** | `#FFFFFF` | Background, Cards, Clean spaces |
| **Light Gray** | `#F8F9FA` | Section backgrounds, Subtle areas |
| **Medium Gray** | `#E9ECEF` | Borders, Dividers, Input backgrounds |
| **Text Gray** | `#6C757D` | Secondary text, Captions |
| **Dark Gray** | `#212529` | Primary text, Headlines |

### **Functional Colors**

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Success Green** | `#28A745` | Success messages, Progress indicators |
| **Warning Yellow** | `#FFC107` | Warnings, Attention states |
| **Danger Red** | `#DC3545` | Errors, Destructive actions |
| **Info Blue** | `#17A2B8` | Information, Tips, Notifications |

### **Gradients**

```css
/* Primary Gradient */
background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);

/* Secondary Gradient */
background: linear-gradient(135deg, #F18F01 0%, #C73E1D 100%);

/* Light Gradient */
background: linear-gradient(135deg, #F8F9FA 0%, #E9ECEF 100%);
```

---

## 📝 **TYPOGRAPHY**

### **Font Families**

#### **Primary Font: Inter**
- **Usage**: Body text, UI elements, Forms
- **Characteristics**: Clean, modern, highly readable
- **Weights**: 400 (Regular), 500 (Medium), 600 (Semibold), 700 (Bold)

#### **Secondary Font: Poppins**
- **Usage**: Headlines, Brand elements, CTAs
- **Characteristics**: Friendly, approachable, geometric
- **Weights**: 400 (Regular), 600 (Semibold), 700 (Bold)

### **Typography Scale**

| Element | Font | Size | Weight | Line Height | Usage |
|---------|------|------|--------|-------------|-------|
| **H1 Hero** | Poppins | 3.5rem | 700 | 1.2 | Homepage hero |
| **H1 Page** | Poppins | 3rem | 700 | 1.3 | Page titles |
| **H2 Section** | Poppins | 2rem | 600 | 1.4 | Section headers |
| **H3 Card** | Inter | 1.5rem | 600 | 1.4 | Card titles |
| **H4 Component** | Inter | 1.25rem | 600 | 1.5 | Component headers |
| **Body Large** | Inter | 1.125rem | 400 | 1.6 | Important text |
| **Body** | Inter | 1rem | 400 | 1.6 | Regular text |
| **Small** | Inter | 0.875rem | 400 | 1.5 | Captions, meta |
| **Tiny** | Inter | 0.75rem | 400 | 1.4 | Labels, tags |

### **Typography Examples**

```css
/* Hero Title */
.hero-title {
    font-family: 'Poppins', sans-serif;
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.2;
    color: #FFFFFF;
}

/* Section Header */
.section-header {
    font-family: 'Poppins', sans-serif;
    font-size: 2rem;
    font-weight: 600;
    line-height: 1.4;
    color: #2E86AB;
}

/* Body Text */
.body-text {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.6;
    color: #212529;
}
```

---

## 🧩 **COMPONENT LIBRARY**

### **Buttons**

#### **Primary Button**
```css
.btn-primary {
    background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
    color: #FFFFFF;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(46, 134, 171, 0.3);
}
```

#### **Secondary Button**
```css
.btn-secondary {
    background: linear-gradient(135deg, #F18F01 0%, #C73E1D 100%);
    color: #FFFFFF;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    font-weight: 600;
}
```

#### **Outline Button**
```css
.btn-outline {
    background: transparent;
    color: #2E86AB;
    border: 2px solid #2E86AB;
    padding: 10px 22px;
    border-radius: 8px;
    font-weight: 600;
}

.btn-outline:hover {
    background: #2E86AB;
    color: #FFFFFF;
}
```

### **Cards**

#### **Service Card**
```css
.service-card {
    background: #FFFFFF;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    text-align: center;
    transition: transform 0.3s ease;
    border: 1px solid #E9ECEF;
}

.service-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}
```

#### **Appointment Card**
```css
.appointment-card {
    background: #FFFFFF;
    border: 1px solid #E9ECEF;
    border-radius: 8px;
    padding: 20px;
    margin: 15px 0;
    transition: all 0.3s ease;
}

.appointment-card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
}
```

### **Form Elements**

#### **Input Fields**
```css
.form-input {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #E9ECEF;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
    font-family: 'Inter', sans-serif;
}

.form-input:focus {
    outline: none;
    border-color: #2E86AB;
    box-shadow: 0 0 0 3px rgba(46, 134, 171, 0.1);
}

.form-label {
    display: block;
    margin-bottom: 5px;
    font-weight: 600;
    color: #212529;
    font-size: 0.875rem;
}
```

### **Progress Indicators**

```css
.progress-bar {
    background: #E9ECEF;
    height: 8px;
    border-radius: 4px;
    overflow: hidden;
    margin: 10px 0;
}

.progress-fill {
    background: linear-gradient(90deg, #2E86AB 0%, #A23B72 100%);
    height: 100%;
    transition: width 0.3s ease;
}
```

---

## 🧩 **COMPREHENSIVE COMPONENT LIBRARY**

### **Advanced Booking Components**

#### **AI Therapist Matching System**
```css
.ai-recommendation {
    background: linear-gradient(135deg, #A23B72 0%, #2E86AB 100%);
    border-radius: 12px;
    padding: 16px;
    color: white;
    animation: pulse 2s infinite;
}

.match-percentage {
    font-weight: 700;
    font-size: 1.5rem;
    color: #F18F01;
}
```

#### **Interactive Calendar Component**
```css
.calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 4px;
    margin: 16px 0;
}

.calendar-day {
    aspect-ratio: 1;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
}

.calendar-day.available:hover {
    background: #2E86AB;
    color: white;
    transform: scale(1.1);
}

.calendar-day.selected {
    background: #F18F01;
    color: white;
}
```

#### **Progress Tracking Components**
```css
.progress-chart {
    background: linear-gradient(45deg, #E9ECEF 25%, transparent 25%);
    border-radius: 12px;
    position: relative;
    overflow: hidden;
}

.anxiety-level-indicator {
    height: 8px;
    border-radius: 4px;
    background: linear-gradient(90deg, #C73E1D 0%, #F18F01 50%, #28A745 100%);
    position: relative;
}

.progress-marker {
    position: absolute;
    width: 16px;
    height: 16px;
    background: white;
    border: 3px solid #2E86AB;
    border-radius: 50%;
    top: -4px;
    transition: left 0.3s ease;
}
```

### **Dashboard Components**

#### **Statistics Cards**
```css
.stat-card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 20px rgba(46, 134, 171, 0.1);
    border: 1px solid #E9ECEF;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stat-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(46, 134, 171, 0.15);
}

.stat-value {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #2E86AB, #A23B72);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```

#### **Business Intelligence Charts**
```css
.chart-container {
    background: white;
    border-radius: 12px;
    padding: 20px;
    min-height: 300px;
    position: relative;
}

.revenue-chart {
    background: linear-gradient(180deg, rgba(46, 134, 171, 0.1) 0%, transparent 100%);
}

.client-growth-chart {
    background: linear-gradient(180deg, rgba(241, 143, 1, 0.1) 0%, transparent 100%);
}
```

### **Advanced Form Components**

#### **Multi-Step Form Progress**
```css
.form-progress {
    display: flex;
    align-items: center;
    margin-bottom: 32px;
}

.progress-step {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    position: relative;
    z-index: 2;
}

.progress-step.active {
    background: #2E86AB;
    color: white;
}

.progress-step.completed {
    background: #28A745;
    color: white;
}

.progress-connector {
    flex: 1;
    height: 2px;
    background: #E9ECEF;
    margin: 0 8px;
    position: relative;
}

.progress-connector.active {
    background: #2E86AB;
}
```

### **Data Visualization Components**

#### **Revenue Analytics**
```css
.revenue-metric {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px;
    background: linear-gradient(135deg, #F8F9FA 0%, #FFFFFF 100%);
    border-radius: 12px;
    border-left: 4px solid #F18F01;
}

.metric-trend {
    font-size: 0.875rem;
    padding: 4px 8px;
    border-radius: 16px;
    font-weight: 600;
}

.trend-up {
    background: rgba(40, 167, 69, 0.1);
    color: #28A745;
}

.trend-down {
    background: rgba(220, 53, 69, 0.1);
    color: #DC3545;
}
```

### **Advanced Interaction States**

#### **Loading States**
```css
.skeleton-loader {
    background: linear-gradient(90deg, #F8F9FA 25%, #E9ECEF 50%, #F8F9FA 75%);
    background-size: 200% 100%;
    animation: loading 1.5s infinite;
    border-radius: 8px;
}

@keyframes loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

.pulse-animation {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}
```

#### **Micro-interactions**
```css
.button-hover-effect {
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}

.button-hover-effect::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.6s ease;
}

.button-hover-effect:hover::before {
    left: 100%;
}
```

---

## 📐 **SPACING & LAYOUT**

### **Spacing Scale (8px Grid System)**

| Size | Value | Usage |
|------|-------|-------|
| **xs** | 4px | Very tight spacing |
| **sm** | 8px | Small gaps |
| **md** | 16px | Standard spacing |
| **lg** | 24px | Section spacing |
| **xl** | 32px | Large sections |
| **2xl** | 48px | Hero sections |
| **3xl** | 64px | Major sections |

### **Border Radius**

| Size | Value | Usage |
|------|-------|-------|
| **Small** | 4px | Small elements, tags |
| **Default** | 8px | Buttons, inputs, cards |
| **Large** | 12px | Large cards, sections |
| **XL** | 16px | Hero sections, containers |
| **Round** | 50% | Avatars, icons |

### **Shadows**

```css
/* Small Shadow */
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

/* Medium Shadow */
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);

/* Large Shadow */
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);

/* Focus Shadow */
box-shadow: 0 0 0 3px rgba(46, 134, 171, 0.1);
```

---

## 📱 **RESPONSIVE DESIGN**

### **Breakpoints**

| Device | Min Width | Max Width | Grid Columns |
|--------|-----------|-----------|--------------|
| **Mobile** | 320px | 767px | 1 |
| **Tablet** | 768px | 1023px | 2-3 |
| **Desktop** | 1024px | 1439px | 3-4 |
| **Large** | 1440px+ | - | 4-6 |

### **Mobile-First Approach**

```css
/* Mobile styles (default) */
.container {
    padding: 16px;
}

.grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        padding: 24px;
    }
    
    .grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 24px;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        padding: 32px;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }
}
```

### **Touch Targets**

- **Minimum size**: 44px × 44px
- **Recommended**: 48px × 48px
- **Spacing**: 8px minimum between touch targets
- **Visual feedback**: Clear hover and active states

---

## 🎯 **UI PATTERNS**

### **Navigation Patterns**

#### **Desktop Navigation**
- Horizontal menu bar
- Logo on the left
- Main navigation in center
- User actions on the right
- Sticky on scroll

#### **Mobile Navigation**
- Hamburger menu
- Full-screen overlay
- Touch-friendly items
- Clear hierarchy
- Quick access to key functions

### **Dashboard Patterns**

#### **Sidebar Navigation**
- Fixed left sidebar
- Icon + text labels
- Active state highlighting
- Collapsible on mobile
- User profile at top

#### **Content Area**
- Grid-based layout
- Card-based components
- Clear visual hierarchy
- Action buttons prominent
- Status indicators

### **Form Patterns**

#### **Multi-Step Forms**
- Progress indicator
- Clear step numbering
- Save progress capability
- Validation feedback
- Easy navigation between steps

#### **Single Page Forms**
- Logical grouping
- Clear labels
- Inline validation
- Helpful placeholder text
- Error state handling

---

## 🔧 **INTERACTIVE STATES**

### **Button States**

| State | Visual Change | Timing |
|-------|---------------|--------|
| **Default** | Normal appearance | - |
| **Hover** | `translateY(-2px)` + shadow | 0.3s ease |
| **Active** | `translateY(1px)` + darker | 0.1s ease |
| **Focus** | Border + shadow ring | Instant |
| **Disabled** | 50% opacity + no hover | - |

### **Form States**

| State | Visual Change |
|-------|---------------|
| **Default** | Light border |
| **Focus** | Primary color border + shadow |
| **Error** | Red border + error message |
| **Success** | Green border + checkmark |
| **Disabled** | Gray background + reduced opacity |

---

## ♿ **ACCESSIBILITY GUIDELINES**

### **Color Contrast**
- **Normal text**: 4.5:1 minimum ratio
- **Large text**: 3:1 minimum ratio
- **UI components**: 3:1 minimum ratio
- **Brand elements**: 3:1 minimum ratio

### **Keyboard Navigation**
- Tab order follows logical flow
- Skip links for main content
- Clear focus indicators
- All interactive elements accessible
- Escape key closes modals/dropdowns

### **Screen Reader Support**
- Semantic HTML structure
- ARIA labels where needed
- Alt text for all images
- Form labels properly associated
- Status messages announced

### **Motion & Animation**
- Respect `prefers-reduced-motion`
- Animations enhance UX, not distract
- No auto-playing videos with sound
- Smooth transitions (0.3s standard)
- Meaningful animations only

---

## 📊 **IMPLEMENTATION GUIDELINES**

### **CSS Architecture**

```css
/* Component Structure */
.component-name {
    /* Layout properties */
    /* Visual properties */
    /* Typography */
    /* Transitions */
}

.component-name__element {
    /* Nested element styles */
}

.component-name--modifier {
    /* Modifier variations */
}

.component-name.is-state {
    /* State classes */
}
```

### **Asset Optimization**

- **Images**: WebP format preferred, fallback to JPG/PNG
- **Icons**: SVG for scalability
- **Fonts**: WOFF2 format, preload critical fonts
- **CSS**: Minimize unused styles
- **JavaScript**: Progressive enhancement

### **Performance Targets**

- **First Contentful Paint**: < 2s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **First Input Delay**: < 100ms
- **Time to Interactive**: < 3s

---

## 🎨 **BRAND APPLICATIONS**

### **Logo Usage**
- Primary logo with tagline
- Icon-only version for small spaces
- White version for dark backgrounds
- Minimum size: 120px width
- Clear space: 1x logo height

### **Voice & Tone**
- **Professional** yet approachable
- **Empathetic** and understanding
- **Confident** in expertise
- **Warm** and welcoming
- **Clear** and jargon-free

### **Photography Style**
- Natural, calming environments
- Diverse, authentic people
- Soft, natural lighting
- Minimal, clean compositions
- Professional but not clinical

---

## 📋 **DESIGN CHECKLIST**

### **Before Development**
- [ ] User personas validated
- [ ] User flows documented
- [ ] Wireframes approved
- [ ] High-fidelity designs complete
- [ ] Design system components defined
- [ ] Accessibility requirements met
- [ ] Responsive breakpoints planned

### **During Development**
- [ ] Component library built
- [ ] Cross-browser testing
- [ ] Mobile responsiveness verified
- [ ] Accessibility testing completed
- [ ] Performance optimization done
- [ ] User testing conducted
- [ ] Feedback incorporated

### **Post-Launch**
- [ ] Analytics implementation
- [ ] User feedback collection
- [ ] Continuous improvement plan
- [ ] Design system maintenance
- [ ] Regular accessibility audits
- [ ] Performance monitoring
- [ ] Conversion optimization

---

*This design system serves as the foundation for all CUR-HEART digital products, ensuring consistency, accessibility, and optimal user experience across all touchpoints.*

## 💼 **INVESTOR-READY DESIGN FEATURES**

### **Financial Dashboard Components**
- **Revenue Tracking**: Real-time financial metrics with growth indicators
- **Client Analytics**: Comprehensive user behavior and conversion analytics
- **ROI Visualization**: Investment return calculations and projections
- **Market Analysis**: Competitive positioning and market share data

### **Professional Healthcare Standards**
- **HIPAA Compliance**: Privacy-first design with secure data handling
- **Medical Accuracy**: Evidence-based content and terminology
- **Accessibility Standards**: WCAG 2.1 AA compliance for inclusive design
- **Professional Credibility**: Clinical-grade visual hierarchy and information architecture

### **Scalability Indicators**
- **Modular Components**: Reusable UI elements for rapid feature development
- **Multi-language Ready**: Internationalization-ready component structure
- **Platform Agnostic**: Design system suitable for web, mobile, and tablet
- **Enterprise Features**: Advanced reporting, user management, and admin tools

---

## 🎯 **CONVERSION-OPTIMIZED DESIGN**

### **Booking Flow Optimization**
- **AI-Powered Matching**: Visually prominent therapist recommendations
- **Friction Reduction**: Minimal steps with clear progress indicators
- **Trust Signals**: Prominent certifications, reviews, and security badges
- **Mobile-First**: Optimized for mobile booking conversion

### **Trust-Building Elements**
- **Professional Photography**: High-quality therapist and facility images
- **Certification Display**: Prominent medical credentials and accreditations
- **Client Testimonials**: Strategically placed social proof elements
- **Security Indicators**: SSL badges and privacy policy compliance

### **Revenue-Driving Features**
- **Pricing Transparency**: Clear service pricing with value propositions
- **Package Deals**: Multi-session discounts and membership options
- **Emergency Booking**: Premium pricing for urgent session requests
- **Corporate Packages**: B2B offerings for employee wellness programs

---
