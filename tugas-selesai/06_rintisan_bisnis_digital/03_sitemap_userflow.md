# SITEMAP & USER FLOW - CUR-HEART
## Information Architecture & User Journey Mapping

---

## 🗂️ **WEBSITE SITEMAP**

```
CUR-HEART.ID
├── 🏠 HOME
│   ├── Hero Section
│   ├── Services Overview
│   ├── Why Choose Us
│   ├── Testimonials
│   ├── FAQ
│   └── CTA Booking
│
├── 🛍️ SERVICES
│   ├── Services Overview
│   ├── 🧘 Stress & Anxiety Release
│   ├── 🩹 Trauma Healing
│   ├── 💪 Self-Confidence & Motivation
│   ├── 😴 Sleep & Relaxation
│   ├── 🔄 Habit Reprogramming
│   ├── 😨 Phobia & Fear Management
│   ├── 🏢 Corporate Wellness
│   └── 🎓 Certification Training
│
├── 👥 ABOUT
│   ├── Our Story
│   ├── Mission & Vision
│   ├── Meet Our Therapists
│   ├── Certifications
│   ├── Success Stories
│   └── Gallery
│
├── 📚 BLOG
│   ├── Latest Articles
│   ├── Mental Health Tips
│   ├── Hypnotherapy Education
│   ├── Success Stories
│   ├── Research & Studies
│   └── Categories Filter
│
├── 📞 CONTACT
│   ├── Contact Information
│   ├── Location & Maps
│   ├── Contact Form
│   ├── WhatsApp Integration
│   ├── FAQ
│   └── Live Chat
│
├── 📅 BOOKING (Guest)
│   ├── Service Selection
│   ├── Therapist Selection
│   ├── Date & Time
│   ├── Contact Information
│   ├── Payment
│   └── Confirmation
│
├── 🔐 LOGIN/REGISTER
│   ├── Client Login
│   ├── Therapist Login
│   ├── Admin Login
│   ├── Register New Client
│   ├── Forgot Password
│   └── Social Login (Google)
│
├── 👤 CLIENT DASHBOARD
│   ├── 📊 Overview
│   │   ├── Upcoming Sessions
│   │   ├── Progress Summary
│   │   ├── Quick Actions
│   │   └── Notifications
│   │
│   ├── 📅 My Bookings
│   │   ├── Upcoming Sessions
│   │   ├── Past Sessions
│   │   ├── Book New Session
│   │   ├── Reschedule/Cancel
│   │   └── Session Notes
│   │
│   ├── 📈 Progress Tracking
│   │   ├── Mood Tracker
│   │   ├── Goal Progress
│   │   ├── Therapist Feedback
│   │   ├── Charts & Analytics
│   │   └── Download Reports
│   │
│   ├── 💳 Payments
│   │   ├── Payment History
│   │   ├── Pending Payments
│   │   ├── Payment Methods
│   │   ├── Invoices/Receipts
│   │   └── Subscription Management
│   │
│   ├── ⚙️ Profile Settings
│   │   ├── Personal Information
│   │   ├── Medical History
│   │   ├── Preferences
│   │   ├── Privacy Settings
│   │   └── Account Security
│   │
│   └── 🎧 Resources
│       ├── Self-Hypnosis Audio
│       ├── Guided Exercises
│       ├── Educational Materials
│       ├── Community Forum
│       └── Support Chat
│
├── 👨‍⚕️ THERAPIST PANEL
│   ├── 📊 Dashboard
│   │   ├── Today's Schedule
│   │   ├── Client Overview
│   │   ├── Performance Metrics
│   │   └── Notifications
│   │
│   ├── 📅 Schedule Management
│   │   ├── Availability Settings
│   │   ├── Appointment Calendar
│   │   ├── Booking Requests
│   │   └── Time Off Management
│   │
│   ├── 👥 Client Management
│   │   ├── Client List
│   │   ├── Client Profiles
│   │   ├── Session History
│   │   ├── Progress Notes
│   │   └── Treatment Plans
│   │
│   ├── 📝 Session Notes
│   │   ├── Create Session Notes
│   │   ├── Progress Tracking
│   │   ├── Treatment Recommendations
│   │   └── Follow-up Actions
│   │
│   └── ⚙️ Profile & Settings
│       ├── Professional Profile
│       ├── Specializations
│       ├── Availability Preferences
│       └── Account Settings
│
└── 🔧 ADMIN PANEL
    ├── 📊 Analytics Dashboard
    ├── 👥 User Management
    ├── 🛍️ Service Management
    ├── 📅 Booking Management
    ├── 💰 Financial Reports
    ├── 📚 Content Management
    ├── ⚙️ System Settings
    └── 🔐 Security & Permissions
```

---

## 🔄 **USER FLOW DIAGRAMS**

### **Flow 1: New Client Registration & First Booking**

```
🚀 START: Landing Page Visit
    ↓
📱 Hero CTA: "Book Free Consultation"
    ↓
🔀 DECISION: Existing User?
    ├── YES → 🔐 Login → Client Dashboard
    └── NO → Continue ↓
    
📝 Registration Form
    ├── Email & Password
    ├── Basic Information
    ├── Medical History (optional)
    └── Terms & Conditions
    ↓
📧 Email Verification
    ↓
🛍️ Service Selection
    ├── Browse Services
    ├── Read Descriptions
    ├── Compare Prices
    └── Select Service
    ↓
👨‍⚕️ Therapist Selection
    ├── View Therapist Profiles
    ├── Check Availability
    ├── Read Reviews
    └── Select Therapist
    ↓
📅 Date & Time Selection
    ├── Calendar View
    ├── Available Slots
    ├── Time Zone Settings
    └── Select DateTime
    ↓
💻 Session Method
    ├── In-Person (Clinic)
    ├── Online (Video Call)
    └── Select Preference
    ↓
💳 Payment Information
    ├── Payment Method Selection
    ├── Billing Information
    ├── Promo Code (if any)
    └── Payment Processing
    ↓
✅ Booking Confirmation
    ├── Email Confirmation
    ├── Calendar Invite
    ├── WhatsApp Reminder
    └── Dashboard Update
    ↓
🎯 END: Successful Booking
```

### **Flow 2: Returning Client - Quick Booking**

```
🚀 START: Client Dashboard Login
    ↓
📊 Dashboard Overview
    ├── Upcoming Sessions
    ├── Progress Summary
    ├── Quick Actions
    └── Notifications
    ↓
🔘 CTA: "Book Another Session"
    ↓
🔀 DECISION: Same Therapist?
    ├── YES → Skip Therapist Selection
    └── NO → Therapist Selection
    ↓
📅 Available Dates
    ├── Preferred Therapist Slots
    ├── Alternative Options
    └── Select DateTime
    ↓
💳 Payment (Saved Methods)
    ├── Use Saved Card
    ├── Apply Package Credits
    └── Complete Payment
    ↓
✅ Booking Confirmed
    ↓
🎯 END: Return to Dashboard
```

### **Flow 3: Corporate Client - Bulk Booking**

```
🚀 START: Corporate Inquiry Form
    ↓
📞 Sales Team Contact
    ├── Needs Assessment Call
    ├── Employee Count
    ├── Budget Discussion
    └── Custom Proposal
    ↓
📋 Proposal Review
    ├── Service Package Details
    ├── Pricing Structure
    ├── Implementation Timeline
    └── Contract Terms
    ↓
✍️ Contract Signing
    ↓
👥 Employee Registration Portal
    ├── Bulk Registration
    ├── Employee ID Verification
    ├── Service Allocation
    └── Dashboard Access
    ↓
📊 Corporate Dashboard Access
    ├── Usage Analytics
    ├── Employee Wellness Metrics
    ├── ROI Reports
    └── Renewal Options
    ↓
🎯 END: Active Corporate Account
```

### **Flow 4: Therapist Onboarding**

```
🚀 START: Therapist Application
    ↓
📝 Application Form
    ├── Professional Credentials
    ├── Certification Documents
    ├── Experience Details
    └── Background Check
    ↓
🔍 Verification Process
    ├── Document Review
    ├── Reference Checks
    ├── Interview Process
    └── Skills Assessment
    ↓
✅ Approval & Contract
    ↓
🎓 Platform Training
    ├── System Tutorial
    ├── Protocol Training
    ├── Quality Standards
    └── Certification Quiz
    ↓
⚙️ Profile Setup
    ├── Professional Bio
    ├── Specializations
    ├── Availability Settings
    └── Rate Configuration
    ↓
📅 Go Live
    ├── Calendar Activation
    ├── Booking Availability
    └── Client Assignment
    ↓
🎯 END: Active Therapist
```

---

## 🎯 **KEY USER JOURNEYS**

### **Journey 1: Sarah (Stressed Professional)**

**Touchpoints**: Instagram Ad → Landing Page → Blog → Booking → Session → Follow-up

```
📱 Instagram Ad: "Atasi Stress Kerja dalam 6 Sesi"
    ↓ (Interested)
🌐 Landing Page: Services Overview + Testimonials
    ↓ (Convinced but cautious)
📚 Blog: "5 Tanda Anda Butuh Terapi Stress"
    ↓ (Self-assessment positive)
💬 WhatsApp Chat: Quick consultation
    ↓ (Trust built)
📅 Book Session: Evening slot, female therapist
    ↓ (Commitment made)
🧘 First Session: Stress assessment + relaxation
    ↓ (Positive experience)
📱 App Download: Progress tracking + self-hypnosis
    ↓ (Engagement increased)
📦 Package Purchase: 6-session stress program
    ↓ (Full commitment)
⭐ Testimonial: LinkedIn post + referral
```

**Key Moments of Truth**:
- ✨ First WhatsApp interaction (trust building)
- ✨ Therapist matching (expertise demonstration)  
- ✨ First session experience (value proof)
- ✨ Progress tracking (visible improvement)

### **Journey 2: Dimas (Anxious Student)**

**Touchpoints**: TikTok → Instagram → Student Discount → Online Session → Peer Referral

```
📱 TikTok Video: "Cara Atasi Anxiety Public Speaking"
    ↓ (Viral, relatable content)
📷 Instagram Follow: Educational content + student testimonials
    ↓ (Trust building through content)
🎓 Student Discount: 30% off + payment plan
    ↓ (Affordable option available)
💻 Online Session: Convenient, no travel needed
    ↓ (Barrier removed)
📈 Progress Tracking: Gamified improvement
    ↓ (Engagement through gamification)
👥 Peer Sharing: Success story in student groups
```

**Key Moments of Truth**:
- ✨ Relatable TikTok content (awareness)
- ✨ Student pricing (accessibility)
- ✨ Online convenience (barrier removal)
- ✨ Peer validation (social proof)

### **Journey 3: Rina (Trauma Survivor)**

**Touchpoints**: Friend Referral → Research → Consultation → Trust Building → Long-term Therapy

```
👥 Friend Referral: Personal recommendation
    ↓ (High-intent, pre-qualified)
🔍 Extensive Research: Website, reviews, credentials
    ↓ (Due diligence, risk mitigation)
📞 Phone Consultation: Personal touch, empathy
    ↓ (Trust initiation)
🏥 In-person Session: Safe environment, female therapist
    ↓ (Comfort and safety)
📋 Treatment Plan: Clear roadmap, milestone tracking
    ↓ (Structure and hope)
🤝 Long-term Relationship: 10 sessions + maintenance
```

**Key Moments of Truth**:
- ✨ Personal referral (trust transfer)
- ✨ Therapist credentials (credibility)
- ✨ Safe environment (comfort)
- ✨ Visible progress (hope and motivation)

---

## 🎨 **DESIGN PRINCIPLES**

### **1. Trust & Credibility**
- Professional, medical-grade design
- Prominent therapist credentials
- Client testimonials with photos
- Security badges and certifications
- Clear privacy policies

### **2. Accessibility & Inclusion**
- Mobile-first responsive design
- Multiple language options (ID/EN)
- Various payment methods
- Online/offline session options
- Disability-friendly features

### **3. Simplicity & Clarity**
- Clean, minimal interface
- Clear navigation structure
- Step-by-step booking process
- Plain language explanations
- Visual progress indicators

### **4. Emotional Connection**
- Warm, calming color palette
- Empathetic copywriting tone
- Success story highlights
- Personal therapist profiles
- Community feeling

### **5. Efficiency & Convenience**
- Quick booking process (3 clicks)
- Smart defaults and suggestions
- Saved preferences and history
- Automated reminders
- One-click rescheduling

---

## 📱 **RESPONSIVE BREAKPOINTS**

### **Mobile (320px - 768px)**
- Single column layout
- Touch-friendly buttons (44px minimum)
- Simplified navigation (hamburger menu)
- Optimized forms (single field focus)
- Quick actions prominent

### **Tablet (768px - 1024px)**
- Two-column layout for listings
- Larger therapy session cards
- Side navigation for dashboards
- Enhanced filtering options
- Picture-in-picture video calls

### **Desktop (1024px+)**
- Multi-column layouts
- Rich hover interactions
- Advanced filtering/sorting
- Split-screen views
- Keyboard shortcuts

---

## 🔗 **INTEGRATION POINTS**

### **External Services**
- **Payment**: Midtrans API
- **Maps**: Google Maps integration
- **Communication**: WhatsApp Business API
- **Video**: Zoom/Google Meet integration
- **Analytics**: Google Analytics 4
- **Email**: SendGrid/Mailgun
- **SMS**: Twilio notifications

### **Internal Systems**
- **CRM**: Client relationship management
- **ERP**: Resource planning and scheduling
- **Analytics**: Custom dashboard metrics
- **Content**: Blog and educational resources
- **Support**: Help desk integration

---

*Next: Low-Fidelity Wireframes*
