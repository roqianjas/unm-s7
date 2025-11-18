# CUR-HEART Design System Documentation
*Comprehensive Tailwind CSS design system for the mental health and hypnotherapy platform - Updated October 2024*

## Table of Contents
1. [Brand Identity](#brand-identity)
2. [Tailwind Configuration](#tailwind-configuration)
3. [Color Palette](#color-palette)
4. [Typography](#typography)
5. [Component Library](#component-library)
6. [Layout & Spacing](#layout--spacing)
7. [Interactive States](#interactive-states)
8. [Dashboard Components](#dashboard-components)
9. [Booking Flow Components](#booking-flow-components)
10. [Mobile Design Guidelines](#mobile-design-guidelines)

## Brand Identity

### Brand Values
- **Trust**: Professional, secure, and reliable mental health care
- **Compassion**: Warm, empathetic, and understanding approach
- **Innovation**: AI-powered matching and modern therapy solutions
- **Accessibility**: Inclusive design for all users

### Logo Guidelines
- Primary logo: CUR-HEART with heart icon integration
- Minimum size: 120px width for digital, 20mm for print
- Clear space: 1x logo height around all sides
- Logo variations: Full color, monochrome, white knockout

## Tailwind Configuration

### Custom Tailwind Config
```javascript
// tailwind.config.js
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./*.html"
  ],
  theme: {
    extend: {
      colors: {
        // CUR-HEART Brand Colors
        'cur-primary': {
          DEFAULT: '#2E86AB',
          50: '#E8F3F8',
          100: '#D1E7F1',
          200: '#A3CFE3',
          300: '#75B7D5',
          400: '#479FC7',
          500: '#2E86AB',
          600: '#236B89',
          700: '#1A5067',
          800: '#113544',
          900: '#081A22',
        },
        'cur-secondary': {
          DEFAULT: '#A23B72',
          50: '#F5EBF1',
          100: '#EBD7E3',
          200: '#D7AFC7',
          300: '#C387AB',
          400: '#AF5F8F',
          500: '#A23B72',
          600: '#822F5B',
          700: '#612344',
          800: '#41172D',
          900: '#200B16',
        },
        'cur-accent': {
          DEFAULT: '#F18F01',
          50: '#FEF6E8',
          100: '#FDEDD1',
          200: '#FBDBA3',
          300: '#F9C975',
          400: '#F7B747',
          500: '#F18F01',
          600: '#D17600',
          700: '#9D5800',
          800: '#693B00',
          900: '#341D00',
        },
        'cur-warm': {
          DEFAULT: '#C73E1D',
          50: '#FDF2F0',
          100: '#FBE5E1',
          200: '#F7CBC3',
          300: '#F3B1A5',
          400: '#EF9787',
          500: '#EB7D69',
          600: '#C73E1D',
          700: '#A03318',
          800: '#782713',
          900: '#501A0E',
        }
      },
      fontFamily: {
        'poppins': ['Poppins', 'sans-serif'],
        'inter': ['Inter', 'sans-serif'],
      },
      fontSize: {
        'h1': ['2.5rem', { lineHeight: '1.2', fontWeight: '700' }],
        'h2': ['2rem', { lineHeight: '1.25', fontWeight: '600' }],
        'h3': ['1.5rem', { lineHeight: '1.3', fontWeight: '600' }],
        'h4': ['1.25rem', { lineHeight: '1.4', fontWeight: '500' }],
        'h5': ['1.125rem', { lineHeight: '1.4', fontWeight: '500' }],
        'h6': ['1rem', { lineHeight: '1.5', fontWeight: '500' }],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
      borderRadius: {
        'xl': '0.75rem',
        '2xl': '1rem',
      },
      boxShadow: {
        'cur': '0 4px 12px rgba(46, 134, 171, 0.15)',
        'cur-lg': '0 8px 24px rgba(46, 134, 171, 0.2)',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
```

## Color Palette

### Primary Colors (Tailwind Classes)
```html
<!-- Primary Blue - Trust & Professionalism -->
<div class="bg-cur-primary text-white">Primary</div>
<div class="bg-cur-primary-100 text-cur-primary-800">Light variant</div>
<div class="bg-cur-primary-600 text-white">Dark variant</div>

<!-- Secondary Purple - Calm & Healing -->
<div class="bg-cur-secondary text-white">Secondary</div>
<div class="bg-cur-secondary-100 text-cur-secondary-800">Light variant</div>
<div class="bg-cur-secondary-600 text-white">Dark variant</div>

<!-- Accent Orange - Energy & Warmth -->
<div class="bg-cur-accent text-white">Accent</div>
<div class="bg-cur-accent-100 text-cur-accent-800">Light variant</div>
<div class="bg-cur-accent-600 text-white">Dark variant</div>

<!-- Warm Red - Urgency & Important Actions -->
<div class="bg-cur-warm text-white">Warm</div>
<div class="bg-cur-warm-100 text-cur-warm-800">Light variant</div>
<div class="bg-cur-warm-600 text-white">Dark variant</div>
```

### Semantic Colors (Tailwind Classes)
```html
<!-- Success States -->
<div class="bg-green-500 text-white">Success</div>
<div class="bg-green-100 text-green-800">Success Light</div>

<!-- Warning States -->
<div class="bg-yellow-500 text-white">Warning</div>
<div class="bg-yellow-100 text-yellow-800">Warning Light</div>

<!-- Error States -->
<div class="bg-red-500 text-white">Error</div>
<div class="bg-red-100 text-red-800">Error Light</div>

<!-- Info States -->
<div class="bg-blue-500 text-white">Info</div>
<div class="bg-blue-100 text-blue-800">Info Light</div>
```

## Typography

### Font Families (Tailwind Classes)
```html
<!-- Primary Font - Poppins for headings -->
<h1 class="font-poppins font-bold text-4xl">Main Heading</h1>

<!-- Secondary Font - Inter for body text -->
<p class="font-inter text-base leading-relaxed">Body text content</p>

<!-- Monospace - Code and data -->
<code class="font-mono text-sm">console.log('Hello World')</code>
```

### Type Scale (Tailwind Classes)
```html
<!-- Headings -->
<h1 class="font-poppins text-h1 font-bold text-gray-900">Heading 1</h1>
<h2 class="font-poppins text-h2 font-semibold text-gray-900">Heading 2</h2>
<h3 class="font-poppins text-h3 font-semibold text-gray-900">Heading 3</h3>
<h4 class="font-poppins text-h4 font-medium text-gray-900">Heading 4</h4>
<h5 class="font-poppins text-h5 font-medium text-gray-900">Heading 5</h5>
<h6 class="font-poppins text-h6 font-medium text-gray-900">Heading 6</h6>

<!-- Body Text -->
<p class="font-inter text-lg leading-relaxed text-gray-700">Large body text</p>
<p class="font-inter text-base leading-relaxed text-gray-700">Regular body text</p>
<p class="font-inter text-sm leading-relaxed text-gray-600">Small body text</p>

<!-- UI Text -->
<span class="font-inter text-xs leading-tight text-gray-500">Caption text</span>
<span class="font-inter text-xs uppercase tracking-wide text-gray-500">Overline text</span>
```

### Text Utilities
```html
<!-- Text Colors -->
<p class="text-cur-primary">Primary text color</p>
<p class="text-cur-secondary">Secondary text color</p>
<p class="text-gray-900">Dark text</p>
<p class="text-gray-600">Medium text</p>
<p class="text-gray-400">Light text</p>

<!-- Text Weights -->
<p class="font-light">Light weight (300)</p>
<p class="font-normal">Normal weight (400)</p>
<p class="font-medium">Medium weight (500)</p>
<p class="font-semibold">Semibold weight (600)</p>
<p class="font-bold">Bold weight (700)</p>

<!-- Text Alignment -->
<p class="text-left">Left aligned</p>
<p class="text-center">Center aligned</p>
<p class="text-right">Right aligned</p>
<p class="text-justify">Justified text</p>
```

## Component Library

### Buttons (Tailwind Classes)
```html
<!-- Primary Button -->
<button class="bg-cur-primary hover:bg-cur-primary-600 text-white font-medium py-3 px-6 rounded-lg transition-all duration-200 hover:-translate-y-0.5 hover:shadow-cur">
  Primary Button
</button>

<!-- Secondary Button -->
<button class="bg-cur-secondary hover:bg-cur-secondary-600 text-white font-medium py-3 px-6 rounded-lg transition-all duration-200 hover:-translate-y-0.5 hover:shadow-cur">
  Secondary Button
</button>

<!-- Outline Button -->
<button class="bg-transparent hover:bg-cur-primary text-cur-primary hover:text-white border-2 border-cur-primary font-medium py-3 px-6 rounded-lg transition-all duration-200">
  Outline Button
</button>

<!-- Accent Button -->
<button class="bg-cur-accent hover:bg-cur-accent-600 text-white font-medium py-3 px-6 rounded-lg transition-all duration-200 hover:-translate-y-0.5 hover:shadow-cur">
  Accent Button
</button>

<!-- Ghost Button -->
<button class="bg-transparent hover:bg-gray-100 text-gray-700 hover:text-gray-900 font-medium py-3 px-6 rounded-lg transition-all duration-200">
  Ghost Button
</button>

<!-- Danger Button -->
<button class="bg-red-500 hover:bg-red-600 text-white font-medium py-3 px-6 rounded-lg transition-all duration-200 hover:-translate-y-0.5 hover:shadow-lg">
  Danger Button
</button>
```

### Button Sizes
```html
<!-- Small Button -->
<button class="bg-cur-primary text-white font-medium py-2 px-4 text-sm rounded-md">
  Small Button
</button>

<!-- Regular Button (default) -->
<button class="bg-cur-primary text-white font-medium py-3 px-6 rounded-lg">
  Regular Button
</button>

<!-- Large Button -->
<button class="bg-cur-primary text-white font-medium py-4 px-8 text-lg rounded-lg">
  Large Button
</button>

<!-- Extra Large Button -->
<button class="bg-cur-primary text-white font-medium py-5 px-10 text-xl rounded-xl">
  XL Button
</button>

<!-- Full Width Button -->
<button class="bg-cur-primary text-white font-medium py-3 px-6 rounded-lg w-full">
  Full Width Button
</button>
```

### Button States
```html
<!-- Loading State -->
<button class="bg-cur-primary text-white font-medium py-3 px-6 rounded-lg opacity-75 cursor-not-allowed flex items-center space-x-2" disabled>
  <svg class="animate-spin h-4 w-4" viewBox="0 0 24 24">
    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
    <path class="opacity-75" fill="currentColor" d="m4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
  </svg>
  <span>Loading...</span>
</button>

<!-- Disabled State -->
<button class="bg-gray-300 text-gray-500 font-medium py-3 px-6 rounded-lg cursor-not-allowed" disabled>
  Disabled Button
</button>

<!-- Focus State -->
<button class="bg-cur-primary text-white font-medium py-3 px-6 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/30">
  Focus Button
</button>
```

### Form Elements (Tailwind Classes)
```html
<!-- Input Fields -->
<div class="space-y-2">
  <label class="block text-sm font-medium text-gray-700">Email Address</label>
  <input type="email" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/20 focus:border-cur-primary transition-all duration-200" placeholder="Enter your email">
</div>

<!-- Input with Icon -->
<div class="relative">
  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
    <i class="fas fa-envelope text-gray-400"></i>
  </div>
  <input type="email" class="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/20 focus:border-cur-primary" placeholder="Email">
</div>

<!-- Error State Input -->
<div class="space-y-2">
  <label class="block text-sm font-medium text-gray-700">Password</label>
  <input type="password" class="w-full px-4 py-3 border border-red-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-red-100 focus:border-red-500 bg-red-50" placeholder="Enter password">
  <p class="text-sm text-red-600">Password is required</p>
</div>

<!-- Success State Input -->
<div class="space-y-2">
  <label class="block text-sm font-medium text-gray-700">Full Name</label>
  <input type="text" class="w-full px-4 py-3 border border-green-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-green-100 focus:border-green-500 bg-green-50" value="John Doe">
  <p class="text-sm text-green-600">✓ Looks good!</p>
</div>
```

### Select Dropdown
```html
<!-- Basic Select -->
<div class="space-y-2">
  <label class="block text-sm font-medium text-gray-700">Service Type</label>
  <select class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/20 focus:border-cur-primary bg-white">
    <option>Individual Therapy</option>
    <option>Group Therapy</option>
    <option>Couple Therapy</option>
  </select>
</div>

<!-- Custom Select with Icon -->
<div class="relative">
  <select class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/20 focus:border-cur-primary bg-white appearance-none">
    <option>Choose service...</option>
    <option>Individual Therapy</option>
    <option>Group Therapy</option>
  </select>
  <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
    <i class="fas fa-chevron-down text-gray-400"></i>
  </div>
</div>
```

### Textarea
```html
<!-- Basic Textarea -->
<div class="space-y-2">
  <label class="block text-sm font-medium text-gray-700">Message</label>
  <textarea rows="4" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/20 focus:border-cur-primary resize-vertical" placeholder="Tell us about your concerns..."></textarea>
</div>

<!-- Textarea with Character Count -->
<div class="space-y-2">
  <label class="block text-sm font-medium text-gray-700">Session Notes</label>
  <textarea rows="6" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/20 focus:border-cur-primary resize-vertical" placeholder="Enter session notes..." maxlength="500"></textarea>
  <div class="flex justify-between text-sm text-gray-500">
    <span>Maximum 500 characters</span>
    <span>0/500</span>
  </div>
</div>
```

### Checkbox & Radio
```html
<!-- Checkboxes -->
<div class="space-y-3">
  <div class="flex items-center">
    <input type="checkbox" class="h-4 w-4 text-cur-primary border-gray-300 rounded focus:ring-cur-primary/20 focus:ring-2">
    <label class="ml-3 text-sm text-gray-700">Anxiety management</label>
  </div>
  <div class="flex items-center">
    <input type="checkbox" class="h-4 w-4 text-cur-primary border-gray-300 rounded focus:ring-cur-primary/20 focus:ring-2" checked>
    <label class="ml-3 text-sm text-gray-700">Stress relief</label>
  </div>
</div>

<!-- Radio Buttons -->
<div class="space-y-3">
  <div class="flex items-center">
    <input type="radio" name="session-type" class="h-4 w-4 text-cur-primary border-gray-300 focus:ring-cur-primary/20 focus:ring-2">
    <label class="ml-3 text-sm text-gray-700">In-person session</label>
  </div>
  <div class="flex items-center">
    <input type="radio" name="session-type" class="h-4 w-4 text-cur-primary border-gray-300 focus:ring-cur-primary/20 focus:ring-2" checked>
    <label class="ml-3 text-sm text-gray-700">Virtual session</label>
  </div>
</div>
```

### Cards (Tailwind Classes)
```html
<!-- Basic Card -->
<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-200 transition-all duration-200 hover:shadow-cur hover:-translate-y-0.5">
  <h3 class="font-poppins text-lg font-semibold text-gray-900 mb-2">Card Title</h3>
  <p class="font-inter text-gray-600">Card content goes here...</p>
</div>

<!-- Client Card -->
<div class="bg-white rounded-xl p-6 border border-gray-200 transition-all duration-200 hover:border-cur-primary hover:bg-gradient-to-br hover:from-cur-primary-50 hover:to-white">
  <div class="flex items-center space-x-4">
    <div class="bg-cur-primary text-white rounded-lg w-12 h-12 flex items-center justify-center font-poppins font-semibold">
      JD
    </div>
    <div>
      <h4 class="font-poppins font-semibold text-gray-900">John Doe</h4>
      <p class="font-inter text-sm text-gray-600">Next session: Tomorrow 2PM</p>
    </div>
  </div>
</div>

<!-- Active Client Card -->
<div class="bg-gradient-to-br from-cur-primary-100 to-white rounded-xl p-6 border border-cur-primary">
  <div class="flex items-center space-x-4">
    <div class="bg-cur-primary text-white rounded-lg w-12 h-12 flex items-center justify-center font-poppins font-semibold">
      SA
    </div>
    <div>
      <h4 class="font-poppins font-semibold text-gray-900">Sarah Anderson</h4>
      <p class="font-inter text-sm text-cur-primary-600">Active session</p>
    </div>
  </div>
</div>

<!-- Session Card - Upcoming -->
<div class="bg-gradient-to-br from-cur-accent-100 to-white rounded-xl p-6 border-l-4 border-cur-accent shadow-sm">
  <div class="flex justify-between items-start mb-4">
    <div>
      <h4 class="font-poppins font-semibold text-gray-900">Anxiety Management</h4>
      <p class="font-inter text-sm text-gray-600">with Dr. Michael Chen</p>
    </div>
    <span class="bg-cur-accent text-white px-3 py-1 rounded-full text-xs font-medium">Upcoming</span>
  </div>
  <div class="flex items-center text-sm text-gray-600 space-x-4">
    <span class="flex items-center">
      <i class="fas fa-calendar mr-2"></i>
      Tomorrow
    </span>
    <span class="flex items-center">
      <i class="fas fa-clock mr-2"></i>
      2:00 PM
    </span>
  </div>
</div>

<!-- Session Card - Completed -->
<div class="bg-gray-50 rounded-xl p-6 border-l-4 border-green-500 shadow-sm">
  <div class="flex justify-between items-start mb-4">
    <div>
      <h4 class="font-poppins font-semibold text-gray-900">Stress Relief Session</h4>
      <p class="font-inter text-sm text-gray-600">with Dr. Lisa Wang</p>
    </div>
    <span class="bg-green-500 text-white px-3 py-1 rounded-full text-xs font-medium">Completed</span>
  </div>
  <div class="flex items-center text-sm text-gray-600 space-x-4">
    <span class="flex items-center">
      <i class="fas fa-calendar mr-2"></i>
      Yesterday
    </span>
    <span class="flex items-center">
      <i class="fas fa-clock mr-2"></i>
      3:00 PM
    </span>
  </div>
</div>

<!-- Feature Card with Icon -->
<div class="bg-white rounded-xl p-8 shadow-sm border border-gray-200 text-center transition-all duration-200 hover:shadow-cur hover:-translate-y-1">
  <div class="bg-cur-primary-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
    <i class="fas fa-brain text-cur-primary text-2xl"></i>
  </div>
  <h3 class="font-poppins text-xl font-semibold text-gray-900 mb-2">AI Matching</h3>
  <p class="font-inter text-gray-600">Advanced AI algorithm matches you with the perfect therapist</p>
</div>

<!-- Pricing Card -->
<div class="bg-white rounded-xl p-8 shadow-sm border-2 border-cur-primary relative overflow-hidden">
  <div class="absolute top-0 right-0 bg-cur-primary text-white px-4 py-1 text-xs font-medium">
    POPULAR
  </div>
  <div class="text-center">
    <h3 class="font-poppins text-2xl font-bold text-gray-900 mb-2">Premium Plan</h3>
    <div class="mb-6">
      <span class="text-4xl font-bold text-cur-primary">$99</span>
      <span class="text-gray-600">/month</span>
    </div>
    <ul class="space-y-3 mb-8">
      <li class="flex items-center">
        <i class="fas fa-check text-green-500 mr-3"></i>
        <span class="font-inter text-gray-700">Unlimited sessions</span>
      </li>
      <li class="flex items-center">
        <i class="fas fa-check text-green-500 mr-3"></i>
        <span class="font-inter text-gray-700">24/7 support</span>
      </li>
      <li class="flex items-center">
        <i class="fas fa-check text-green-500 mr-3"></i>
        <span class="font-inter text-gray-700">Priority booking</span>
      </li>
    </ul>
    <button class="w-full bg-cur-primary text-white font-medium py-3 rounded-lg hover:bg-cur-primary-600 transition-colors">
      Choose Plan
    </button>
  </div>
</div>
```

### Badges & Status Indicators (Tailwind Classes)
```html
<!-- Status Badges -->
<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium uppercase tracking-wide bg-cur-primary-100 text-cur-primary-800">
  Primary
</span>

<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium uppercase tracking-wide bg-cur-secondary-100 text-cur-secondary-800">
  Secondary
</span>

<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium uppercase tracking-wide bg-green-100 text-green-800">
  Success
</span>

<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium uppercase tracking-wide bg-yellow-100 text-yellow-800">
  Warning
</span>

<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium uppercase tracking-wide bg-red-100 text-red-800">
  Error
</span>

<!-- Notification Badges -->
<div class="relative inline-block">
  <button class="bg-cur-primary text-white p-2 rounded-lg">
    <i class="fas fa-bell"></i>
  </button>
  <span class="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center">
    3
  </span>
</div>

<!-- Status Badges with Icons -->
<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800">
  <i class="fas fa-check-circle mr-1"></i>
  Completed
</span>

<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-cur-accent-100 text-cur-accent-800">
  <i class="fas fa-clock mr-1"></i>
  Pending
</span>

<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
  <i class="fas fa-video mr-1"></i>
  Online
</span>

<!-- Large Status Badges -->
<span class="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-cur-primary text-white">
  Active Session
</span>

<span class="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
  Offline
</span>
```

### Progress Indicators
```html
<!-- Basic Progress Bar -->
<div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
  <div class="bg-gradient-to-r from-cur-primary to-cur-secondary h-full rounded-full transition-all duration-300 ease-out" style="width: 65%"></div>
</div>

<!-- Progress Bar with Label -->
<div class="space-y-2">
  <div class="flex justify-between text-sm">
    <span class="font-medium text-gray-700">Progress</span>
    <span class="text-cur-primary font-semibold">65%</span>
  </div>
  <div class="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
    <div class="bg-gradient-to-r from-cur-primary to-cur-secondary h-full rounded-full transition-all duration-300 ease-out" style="width: 65%"></div>
  </div>
</div>

<!-- Step Progress -->
<div class="flex items-center space-x-4">
  <div class="flex items-center">
    <div class="bg-cur-primary text-white rounded-full w-8 h-8 flex items-center justify-center text-sm font-semibold">
      1
    </div>
    <span class="ml-2 text-sm font-medium text-gray-900">Assessment</span>
  </div>
  <div class="flex-1 h-1 bg-cur-primary rounded"></div>
  
  <div class="flex items-center">
    <div class="bg-cur-primary text-white rounded-full w-8 h-8 flex items-center justify-center text-sm font-semibold">
      2
    </div>
    <span class="ml-2 text-sm font-medium text-gray-900">Matching</span>
  </div>
  <div class="flex-1 h-1 bg-gray-200 rounded"></div>
  
  <div class="flex items-center">
    <div class="bg-gray-200 text-gray-500 rounded-full w-8 h-8 flex items-center justify-center text-sm font-semibold">
      3
    </div>
    <span class="ml-2 text-sm font-medium text-gray-500">Session</span>
  </div>
</div>

<!-- Circular Progress -->
<div class="relative w-16 h-16">
  <svg class="w-16 h-16 transform -rotate-90" viewBox="0 0 64 64">
    <circle cx="32" cy="32" r="28" stroke="currentColor" stroke-width="4" fill="none" class="text-gray-200" />
    <circle cx="32" cy="32" r="28" stroke="currentColor" stroke-width="4" fill="none" stroke-linecap="round" class="text-cur-primary" stroke-dasharray="175.93" stroke-dashoffset="52.78" />
  </svg>
  <div class="absolute inset-0 flex items-center justify-center">
    <span class="text-lg font-semibold text-cur-primary">70%</span>
  </div>
</div>

<!-- Session Progress Timeline -->
<div class="space-y-4">
  <div class="flex items-center">
    <div class="bg-green-500 rounded-full w-3 h-3"></div>
    <div class="ml-4 flex-1">
      <p class="text-sm font-medium text-gray-900">Initial Assessment Completed</p>
      <p class="text-xs text-gray-500">2 hours ago</p>
    </div>
  </div>
  <div class="flex items-center">
    <div class="bg-cur-primary rounded-full w-3 h-3"></div>
    <div class="ml-4 flex-1">
      <p class="text-sm font-medium text-gray-900">Therapist Matched</p>
      <p class="text-xs text-gray-500">1 hour ago</p>
    </div>
  </div>
  <div class="flex items-center">
    <div class="bg-gray-300 rounded-full w-3 h-3"></div>
    <div class="ml-4 flex-1">
      <p class="text-sm font-medium text-gray-500">First Session Scheduled</p>
      <p class="text-xs text-gray-500">Pending</p>
    </div>
  </div>
</div>
```

## Layout & Spacing

### Spacing Scale (Tailwind Classes)
```html
<!-- Margins -->
<div class="m-1">margin: 4px</div>     <!-- 0.25rem -->
<div class="m-2">margin: 8px</div>     <!-- 0.5rem -->
<div class="m-3">margin: 12px</div>    <!-- 0.75rem -->
<div class="m-4">margin: 16px</div>    <!-- 1rem -->
<div class="m-6">margin: 24px</div>    <!-- 1.5rem -->
<div class="m-8">margin: 32px</div>    <!-- 2rem -->
<div class="m-12">margin: 48px</div>   <!-- 3rem -->
<div class="m-16">margin: 64px</div>   <!-- 4rem -->

<!-- Padding -->
<div class="p-4">padding: 16px</div>
<div class="px-6 py-4">padding: 24px horizontal, 16px vertical</div>
<div class="pt-8 pb-4">padding-top: 32px, padding-bottom: 16px</div>

<!-- Space Between Children -->
<div class="space-y-4">
  <div>Item 1</div>    <!-- 16px gap -->
  <div>Item 2</div>    <!-- between each -->
  <div>Item 3</div>    <!-- child element -->
</div>

<div class="space-x-6">
  <span>Item 1</span>  <!-- 24px gap -->
  <span>Item 2</span>  <!-- horizontally -->
  <span>Item 3</span>
</div>
```

### Grid System (Tailwind Classes)
```html
<!-- Dashboard Grid Layout -->
<div class="grid grid-cols-[16rem_1fr] min-h-screen">
  <!-- Sidebar -->
  <aside class="bg-gray-900 text-white p-6">
    <nav>Navigation content</nav>
  </aside>
  
  <!-- Main Content -->
  <main class="bg-gray-50 p-8 overflow-y-auto">
    <div class="max-w-7xl mx-auto">
      Main content
    </div>
  </main>
</div>

<!-- Responsive Dashboard Grid -->
<div class="grid grid-cols-1 lg:grid-cols-[16rem_1fr] min-h-screen">
  <!-- Mobile-first: single column, then sidebar + content on large screens -->
  <aside class="hidden lg:block bg-gray-900 text-white p-6">
    Sidebar
  </aside>
  <main class="bg-gray-50 p-4 lg:p-8">
    Main content
  </main>
</div>

<!-- Content Grid Layouts -->
<!-- 2-Column Grid -->
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
  <div class="bg-white p-6 rounded-xl">Column 1</div>
  <div class="bg-white p-6 rounded-xl">Column 2</div>
</div>

<!-- 3-Column Grid -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <div class="bg-white p-6 rounded-xl">Column 1</div>
  <div class="bg-white p-6 rounded-xl">Column 2</div>
  <div class="bg-white p-6 rounded-xl">Column 3</div>
</div>

<!-- Auto-fit Grid (Responsive Cards) -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  <div class="bg-white p-6 rounded-xl">Card 1</div>
  <div class="bg-white p-6 rounded-xl">Card 2</div>
  <div class="bg-white p-6 rounded-xl">Card 3</div>
  <div class="bg-white p-6 rounded-xl">Card 4</div>
</div>

<!-- Stats Grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
  <div class="bg-gradient-to-br from-cur-primary to-cur-secondary text-white p-6 rounded-xl">
    <h3 class="text-2xl font-bold">1,234</h3>
    <p class="text-sm opacity-90">Total Clients</p>
  </div>
  <div class="bg-gradient-to-br from-cur-accent to-cur-warm text-white p-6 rounded-xl">
    <h3 class="text-2xl font-bold">89%</h3>
    <p class="text-sm opacity-90">Success Rate</p>
  </div>
  <div class="bg-gradient-to-br from-green-500 to-green-600 text-white p-6 rounded-xl">
    <h3 class="text-2xl font-bold">456</h3>
    <p class="text-sm opacity-90">Sessions Today</p>
  </div>
  <div class="bg-gradient-to-br from-blue-500 to-blue-600 text-white p-6 rounded-xl">
    <h3 class="text-2xl font-bold">$12.5k</h3>
    <p class="text-sm opacity-90">Revenue</p>
  </div>
</div>
```

### Container & Max Width
```html
<!-- Container with max width -->
<div class="container mx-auto px-4">
  <!-- Centers content with responsive padding -->
</div>

<!-- Custom max widths -->
<div class="max-w-md mx-auto">Max width: 448px</div>
<div class="max-w-lg mx-auto">Max width: 512px</div>
<div class="max-w-xl mx-auto">Max width: 576px</div>
<div class="max-w-2xl mx-auto">Max width: 672px</div>
<div class="max-w-4xl mx-auto">Max width: 896px</div>
<div class="max-w-6xl mx-auto">Max width: 1152px</div>
<div class="max-w-7xl mx-auto">Max width: 1280px</div>

<!-- Full width with constraints -->
<div class="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <!-- Responsive padding: 16px mobile, 24px tablet, 32px desktop -->
</div>
```

### Flexbox Layouts
```html
<!-- Basic Flex -->
<div class="flex items-center justify-between">
  <div>Left content</div>
  <div>Right content</div>
</div>

<!-- Flex with gap -->
<div class="flex items-center space-x-4">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>

<!-- Vertical flex -->
<div class="flex flex-col space-y-6">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>

<!-- Responsive flex direction -->
<div class="flex flex-col md:flex-row md:items-center md:space-x-6 space-y-4 md:space-y-0">
  <div>Stacked on mobile, horizontal on desktop</div>
  <div>Item 2</div>
</div>

<!-- Flex wrap -->
<div class="flex flex-wrap gap-4">
  <div class="flex-1 min-w-0">Flexible item</div>
  <div class="flex-shrink-0">Fixed item</div>
</div>
```

## Dashboard Components

### Sidebar Navigation (Tailwind Classes)
```html
<nav class="mt-8 space-y-1">
  <!-- Active Nav Item -->
  <a href="#" class="bg-cur-primary text-white flex items-center px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200">
    <i class="fas fa-home w-5 h-5 mr-3"></i>
    Dashboard
  </a>
  
  <!-- Regular Nav Items -->
  <a href="#" class="text-gray-300 hover:bg-gray-800 hover:text-white flex items-center px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200">
    <i class="fas fa-calendar w-5 h-5 mr-3"></i>
    Appointments
  </a>
  
  <!-- Nav Item with Badge -->
  <a href="#" class="text-gray-300 hover:bg-gray-800 hover:text-white flex items-center px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200">
    <i class="fas fa-envelope w-5 h-5 mr-3"></i>
    Messages
    <span class="ml-auto bg-cur-accent text-white text-xs font-semibold px-2 py-1 rounded-full">
      5
    </span>
  </a>
  
  <a href="#" class="text-gray-300 hover:bg-gray-800 hover:text-white flex items-center px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200">
    <i class="fas fa-user-friends w-5 h-5 mr-3"></i>
    Clients
  </a>
  
  <a href="#" class="text-gray-300 hover:bg-gray-800 hover:text-white flex items-center px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200">
    <i class="fas fa-chart-bar w-5 h-5 mr-3"></i>
    Analytics
  </a>
  
  <!-- Section Divider -->
  <div class="border-t border-gray-700 my-6"></div>
  
  <!-- Section Header -->
  <h3 class="text-gray-400 uppercase text-xs font-semibold tracking-wider px-4 mb-3">
    Account
  </h3>
  
  <a href="#" class="text-gray-300 hover:bg-gray-800 hover:text-white flex items-center px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200">
    <i class="fas fa-cog w-5 h-5 mr-3"></i>
    Settings
  </a>
  
  <a href="#" class="text-gray-300 hover:bg-gray-800 hover:text-white flex items-center px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200">
    <i class="fas fa-sign-out-alt w-5 h-5 mr-3"></i>
    Logout
  </a>
</nav>
```

### Mobile Sidebar
```html
<!-- Mobile Sidebar Overlay -->
<div class="fixed inset-0 bg-gray-600 bg-opacity-75 z-40 lg:hidden" id="sidebar-overlay"></div>

<!-- Mobile Sidebar -->
<div class="fixed inset-y-0 left-0 w-64 bg-gray-900 z-50 transform -translate-x-full transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static" id="mobile-sidebar">
  <div class="flex items-center justify-between p-6">
    <h1 class="text-white text-xl font-bold">CUR-HEART</h1>
    <button class="text-gray-400 hover:text-white lg:hidden" id="close-sidebar">
      <i class="fas fa-times"></i>
    </button>
  </div>
  
  <!-- Navigation content here -->
</div>

<!-- Mobile Menu Button -->
<button class="lg:hidden fixed top-4 left-4 z-30 bg-gray-900 text-white p-2 rounded-lg" id="open-sidebar">
  <i class="fas fa-bars"></i>
</button>
```

### Stats Cards (Tailwind Classes)
```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
  <!-- Primary Stat Card -->
  <div class="bg-gradient-to-br from-cur-primary to-cur-secondary text-white rounded-xl p-6 relative overflow-hidden">
    <!-- Background decoration -->
    <div class="absolute -top-12 -right-12 w-24 h-24 bg-white bg-opacity-10 rounded-full"></div>
    
    <div class="relative">
      <h3 class="text-3xl font-bold mb-2">1,234</h3>
      <p class="text-sm opacity-90">Total Clients</p>
      
      <!-- Trend indicator -->
      <div class="absolute top-0 right-0 bg-white bg-opacity-20 px-2 py-1 rounded text-xs font-medium">
        +12%
      </div>
    </div>
  </div>
  
  <!-- Secondary Stat Card -->
  <div class="bg-gradient-to-br from-cur-accent to-cur-warm text-white rounded-xl p-6 relative overflow-hidden">
    <div class="absolute -top-12 -right-12 w-24 h-24 bg-white bg-opacity-10 rounded-full"></div>
    
    <div class="relative">
      <h3 class="text-3xl font-bold mb-2">89%</h3>
      <p class="text-sm opacity-90">Success Rate</p>
      
      <div class="absolute top-0 right-0 bg-white bg-opacity-20 px-2 py-1 rounded text-xs font-medium">
        +3%
      </div>
    </div>
  </div>
  
  <!-- Success Stat Card -->
  <div class="bg-gradient-to-br from-green-500 to-green-600 text-white rounded-xl p-6 relative overflow-hidden">
    <div class="absolute -top-12 -right-12 w-24 h-24 bg-white bg-opacity-10 rounded-full"></div>
    
    <div class="relative">
      <h3 class="text-3xl font-bold mb-2">456</h3>
      <p class="text-sm opacity-90">Sessions Today</p>
      
      <div class="absolute top-0 right-0 bg-white bg-opacity-20 px-2 py-1 rounded text-xs font-medium">
        +8%
      </div>
    </div>
  </div>
  
  <!-- Revenue Stat Card -->
  <div class="bg-gradient-to-br from-blue-500 to-blue-600 text-white rounded-xl p-6 relative overflow-hidden">
    <div class="absolute -top-12 -right-12 w-24 h-24 bg-white bg-opacity-10 rounded-full"></div>
    
    <div class="relative">
      <h3 class="text-3xl font-bold mb-2">$12.5k</h3>
      <p class="text-sm opacity-90">Monthly Revenue</p>
      
      <div class="absolute top-0 right-0 bg-white bg-opacity-20 px-2 py-1 rounded text-xs font-medium">
        +15%
      </div>
    </div>
  </div>
</div>
```

### Header with Search & Profile
```html
<header class="bg-white border-b border-gray-200 px-6 py-4">
  <div class="flex items-center justify-between">
    <!-- Page Title -->
    <div>
      <h1 class="text-2xl font-bold text-gray-900">Dashboard</h1>
      <p class="text-gray-600">Welcome back, Dr. Sarah</p>
    </div>
    
    <!-- Search & Actions -->
    <div class="flex items-center space-x-4">
      <!-- Search Bar -->
      <div class="relative">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <i class="fas fa-search text-gray-400"></i>
        </div>
        <input type="text" class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/20 focus:border-cur-primary" placeholder="Search clients...">
      </div>
      
      <!-- Notifications -->
      <div class="relative">
        <button class="p-2 text-gray-400 hover:text-gray-600 relative">
          <i class="fas fa-bell text-xl"></i>
          <span class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">3</span>
        </button>
      </div>
      
      <!-- Profile Dropdown -->
      <div class="relative">
        <button class="flex items-center space-x-3 p-2 rounded-lg hover:bg-gray-100">
          <img class="h-8 w-8 rounded-full" src="https://via.placeholder.com/32" alt="Profile">
          <div class="text-left">
            <p class="text-sm font-medium text-gray-900">Dr. Sarah</p>
            <p class="text-xs text-gray-500">Therapist</p>
          </div>
          <i class="fas fa-chevron-down text-gray-400"></i>
        </button>
      </div>
    </div>
  </div>
</header>
```

### Data Table
```html
<div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
  <div class="px-6 py-4 border-b border-gray-200">
    <h3 class="text-lg font-semibold text-gray-900">Recent Sessions</h3>
  </div>
  
  <div class="overflow-x-auto">
    <table class="w-full">
      <thead class="bg-gray-50">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Client</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
        <tr class="hover:bg-gray-50">
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="flex items-center">
              <div class="bg-cur-primary text-white rounded-full w-8 h-8 flex items-center justify-center text-sm font-semibold">
                JD
              </div>
              <div class="ml-3">
                <p class="text-sm font-medium text-gray-900">John Doe</p>
                <p class="text-sm text-gray-500">john@example.com</p>
              </div>
            </div>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Oct 12, 2024</td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Individual</td>
          <td class="px-6 py-4 whitespace-nowrap">
            <span class="inline-flex px-2 py-1 text-xs font-medium bg-green-100 text-green-800 rounded-full">
              Completed
            </span>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <button class="text-cur-primary hover:text-cur-primary-600 mr-3">View</button>
            <button class="text-gray-400 hover:text-gray-600">Edit</button>
          </td>
        </tr>
        <!-- More rows... -->
      </tbody>
    </table>
  </div>
</div>
```

## Interactive States & Animations (Tailwind Classes)

### Hover Effects
```html
<!-- Lift Effect -->
<div class="hover:-translate-y-0.5 hover:shadow-cur transition-all duration-200">
  Card with lift effect
</div>

<!-- Scale Effect -->
<button class="hover:scale-105 transition-transform duration-200">
  Scale on hover
</button>

<!-- Glow Effect -->
<div class="hover:shadow-[0_0_20px_rgba(46,134,171,0.3)] transition-shadow duration-300">
  Glow effect
</div>

<!-- Color Transitions -->
<button class="bg-cur-primary hover:bg-cur-primary-600 text-white transition-colors duration-200">
  Color transition
</button>

<!-- Multi-effect Hover -->
<div class="hover:-translate-y-1 hover:shadow-cur hover:border-cur-primary border-2 border-gray-200 transition-all duration-200">
  Combined hover effects
</div>
```

### Loading States & Animations
```html
<!-- Loading Spinner -->
<div class="animate-spin h-6 w-6 border-2 border-gray-200 border-t-cur-primary rounded-full"></div>

<!-- Loading Button -->
<button class="bg-cur-primary text-white px-6 py-3 rounded-lg disabled:opacity-50 flex items-center space-x-2" disabled>
  <div class="animate-spin h-4 w-4 border-2 border-white border-t-transparent rounded-full"></div>
  <span>Loading...</span>
</button>

<!-- Pulse Animation -->
<div class="animate-pulse bg-gray-200 h-4 w-full rounded"></div>

<!-- Skeleton Loading -->
<div class="animate-pulse space-y-4">
  <div class="bg-gray-200 h-4 w-3/4 rounded"></div>
  <div class="bg-gray-200 h-4 w-1/2 rounded"></div>
  <div class="bg-gray-200 h-4 w-5/6 rounded"></div>
</div>

<!-- Bounce Animation -->
<div class="animate-bounce bg-cur-primary rounded-full h-8 w-8"></div>

<!-- Ping Animation -->
<div class="relative">
  <div class="animate-ping absolute h-4 w-4 bg-cur-primary rounded-full opacity-75"></div>
  <div class="relative h-4 w-4 bg-cur-primary rounded-full"></div>
</div>

<!-- Custom Loading Card -->
<div class="bg-white rounded-xl p-6 animate-pulse">
  <div class="flex items-center space-x-4">
    <div class="bg-gray-200 rounded-full h-12 w-12"></div>
    <div class="space-y-2 flex-1">
      <div class="bg-gray-200 h-4 w-3/4 rounded"></div>
      <div class="bg-gray-200 h-3 w-1/2 rounded"></div>
    </div>
  </div>
</div>
```

### Interactive Button States
```html
<!-- Button with all states -->
<button class="
  bg-cur-primary hover:bg-cur-primary-600 active:bg-cur-primary-700
  text-white font-medium py-3 px-6 rounded-lg
  focus:outline-none focus:ring-4 focus:ring-cur-primary/30
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-all duration-200
  hover:-translate-y-0.5 hover:shadow-cur
">
  Interactive Button
</button>

<!-- Toggle Button -->
<button class="
  bg-gray-200 hover:bg-gray-300 data-[active=true]:bg-cur-primary data-[active=true]:text-white
  text-gray-700 font-medium py-2 px-4 rounded-lg
  transition-all duration-200
">
  Toggle Me
</button>

<!-- Icon Button with Hover -->
<button class="
  p-3 rounded-full text-gray-600 hover:text-cur-primary hover:bg-cur-primary-50
  transition-all duration-200 hover:scale-110
">
  <i class="fas fa-heart text-xl"></i>
</button>
```

## Mobile Design Guidelines

### Mobile Navigation (Tailwind Classes)
```html
<!-- Bottom Navigation Bar -->
<nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 px-3 py-2 flex justify-around z-40 safe-area-pb">
  <!-- Home -->
  <a href="#" class="flex flex-col items-center p-2 rounded-lg text-cur-primary bg-cur-primary-100">
    <i class="fas fa-home text-xl mb-1"></i>
    <span class="text-xs font-medium">Home</span>
  </a>
  
  <!-- Appointments -->
  <a href="#" class="flex flex-col items-center p-2 rounded-lg text-gray-500 hover:text-cur-primary hover:bg-cur-primary-50 transition-colors">
    <i class="fas fa-calendar text-xl mb-1"></i>
    <span class="text-xs font-medium">Schedule</span>
  </a>
  
  <!-- Messages -->
  <a href="#" class="flex flex-col items-center p-2 rounded-lg text-gray-500 hover:text-cur-primary hover:bg-cur-primary-50 transition-colors relative">
    <i class="fas fa-envelope text-xl mb-1"></i>
    <span class="text-xs font-medium">Messages</span>
    <!-- Notification badge -->
    <span class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">3</span>
  </a>
  
  <!-- Profile -->
  <a href="#" class="flex flex-col items-center p-2 rounded-lg text-gray-500 hover:text-cur-primary hover:bg-cur-primary-50 transition-colors">
    <i class="fas fa-user text-xl mb-1"></i>
    <span class="text-xs font-medium">Profile</span>
  </a>
</nav>

<!-- Floating Action Button -->
<button class="fixed bottom-20 right-4 bg-cur-primary text-white rounded-full w-14 h-14 flex items-center justify-center shadow-lg hover:bg-cur-primary-600 transition-colors z-30">
  <i class="fas fa-plus text-xl"></i>
</button>
```

### Mobile Header
```html
<!-- Mobile Header with Back Button -->
<header class="bg-white border-b border-gray-200 px-4 py-3 flex items-center justify-between sticky top-0 z-30">
  <button class="p-2 -ml-2 text-gray-600 hover:text-gray-900 min-h-[44px] min-w-[44px] flex items-center justify-center">
    <i class="fas fa-arrow-left text-lg"></i>
  </button>
  
  <h1 class="text-lg font-semibold text-gray-900 text-center flex-1">
    Book Session
  </h1>
  
  <button class="p-2 -mr-2 text-gray-600 hover:text-gray-900 min-h-[44px] min-w-[44px] flex items-center justify-center">
    <i class="fas fa-ellipsis-v text-lg"></i>
  </button>
</header>

<!-- Mobile Header with Search -->
<header class="bg-white border-b border-gray-200 p-4 sticky top-0 z-30">
  <div class="flex items-center space-x-3">
    <button class="text-gray-600 hover:text-gray-900 min-h-[44px] min-w-[44px] flex items-center justify-center">
      <i class="fas fa-bars text-lg"></i>
    </button>
    
    <div class="flex-1 relative">
      <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
        <i class="fas fa-search text-gray-400"></i>
      </div>
      <input type="text" class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/20 focus:border-cur-primary text-sm" placeholder="Search...">
    </div>
    
    <button class="text-gray-600 hover:text-gray-900 min-h-[44px] min-w-[44px] flex items-center justify-center relative">
      <i class="fas fa-bell text-lg"></i>
      <span class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center">2</span>
    </button>
  </div>
</header>
```

### Touch Targets & Mobile-Friendly Components
```html
<!-- Touch-friendly buttons (minimum 44px) -->
<button class="bg-cur-primary text-white font-medium py-3 px-6 rounded-lg w-full text-base min-h-[44px] min-w-[44px] flex items-center justify-center">
  Book Session
</button>

<button class="bg-white border border-gray-300 text-gray-700 font-medium py-3 px-6 rounded-lg w-full text-base min-h-[44px] min-w-[44px] flex items-center justify-center">
  Cancel
</button>

<!-- Large touch targets for important actions -->
<div class="grid grid-cols-2 gap-4">
  <button class="bg-green-500 text-white font-medium py-4 px-6 rounded-xl text-center min-h-[44px] min-w-[44px] flex flex-col items-center justify-center">
    <i class="fas fa-phone text-xl mb-2 block"></i>
    Call Now
  </button>
  
  <button class="bg-cur-primary text-white font-medium py-4 px-6 rounded-xl text-center min-h-[44px] min-w-[44px] flex flex-col items-center justify-center">
    <i class="fas fa-calendar text-xl mb-2 block"></i>
    Schedule
  </button>
</div>

<!-- Mobile Card Stack -->
<div class="space-y-4 p-4">
  <div class="bg-white rounded-xl p-4 shadow-sm border border-gray-200">
    <div class="flex items-center justify-between mb-3">
      <h3 class="font-poppins font-semibold text-lg">Dr. Sarah Chen</h3>
      <span class="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-medium">Available</span>
    </div>
    <p class="text-gray-600 text-sm mb-4">Anxiety & Depression Specialist</p>
    
    <div class="flex space-x-2">
      <button class="flex-1 bg-cur-primary text-white py-2 px-4 rounded-lg text-sm font-medium min-h-[44px] flex items-center justify-center">
        Book Session
      </button>
      <button class="bg-gray-100 text-gray-700 py-2 px-4 rounded-lg text-sm font-medium min-h-[44px] flex items-center justify-center">
        View Profile
      </button>
    </div>
  </div>
</div>

<!-- Mobile Form Layout -->
<form class="p-4 space-y-4">
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-2">Full Name</label>
    <input type="text" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/20 focus:border-cur-primary text-base">
  </div>
  
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
    <input type="email" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/20 focus:border-cur-primary text-base">
  </div>
  
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-2">Message</label>
    <textarea rows="4" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/20 focus:border-cur-primary text-base resize-none"></textarea>
  </div>
  
  <button type="submit" class="w-full bg-cur-primary text-white font-medium py-3 px-6 rounded-lg text-base min-h-[44px] flex items-center justify-center">
    Send Message
  </button>
</form>
```

### Touch Target Guidelines (Tailwind Classes)
```html
<!-- Minimum 44px touch targets using Tailwind utilities -->
<button class="min-h-[44px] min-w-[44px] flex items-center justify-center bg-cur-primary text-white rounded-lg">
  <i class="fas fa-heart"></i>
</button>

<!-- Touch-friendly form inputs -->
<input class="min-h-[44px] w-full px-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/20">

<!-- Touch-friendly navigation items -->
<a href="#" class="min-h-[44px] flex items-center px-4 text-gray-700 hover:text-cur-primary">
  Navigation Item
</a>

<!-- Touch-friendly icon buttons -->
<button class="min-h-[44px] min-w-[44px] p-3 bg-gray-100 hover:bg-gray-200 rounded-full flex items-center justify-center">
  <i class="fas fa-settings text-gray-600"></i>
</button>

<!-- Touch-friendly tabs -->
<div class="flex border-b border-gray-200">
  <button class="min-h-[44px] px-6 border-b-2 border-cur-primary text-cur-primary font-medium">
    Active Tab
  </button>
  <button class="min-h-[44px] px-6 text-gray-500 hover:text-gray-700">
    Inactive Tab
  </button>
</div>
```

### Mobile Responsive Utilities
```html
<!-- Hide on mobile, show on desktop -->
<div class="hidden md:block">Desktop only content</div>

<!-- Show on mobile, hide on desktop -->
<div class="block md:hidden">Mobile only content</div>

<!-- Mobile-first responsive text sizes -->
<h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold">Responsive heading</h1>

<!-- Mobile-first responsive spacing -->
<div class="p-4 sm:p-6 lg:p-8">Responsive padding</div>

<!-- Mobile stack, desktop grid -->
<div class="space-y-4 sm:space-y-0 sm:grid sm:grid-cols-2 sm:gap-6">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<!-- Mobile full width, desktop auto -->
<button class="w-full sm:w-auto bg-cur-primary text-white py-3 px-6 rounded-lg min-h-[44px] flex items-center justify-center">
  Responsive button
</button>

<!-- Mobile-optimized card layout -->
<div class="p-4 sm:p-6 bg-white rounded-lg shadow-sm">
  <h3 class="text-lg sm:text-xl font-semibold mb-2">Card Title</h3>
  <p class="text-sm sm:text-base text-gray-600 mb-4">Card content</p>
  <button class="w-full sm:w-auto bg-cur-primary text-white py-2 px-4 rounded-lg min-h-[44px] flex items-center justify-center">
    Action Button
  </button>
</div>
```

### Mobile-First Breakpoints
```html
<!-- Tailwind breakpoints reference -->
<!-- sm: 640px -->
<!-- md: 768px -->
<!-- lg: 1024px -->
<!-- xl: 1280px -->
<!-- 2xl: 1536px -->

<!-- Mobile-first approach examples -->
<div class="
  text-sm      <!-- Mobile: 14px -->
  sm:text-base <!-- Tablet: 16px -->
  lg:text-lg   <!-- Desktop: 18px -->
">
  Responsive text
</div>

<div class="
  grid-cols-1     <!-- Mobile: 1 column -->
  sm:grid-cols-2  <!-- Tablet: 2 columns -->
  lg:grid-cols-3  <!-- Desktop: 3 columns -->
  xl:grid-cols-4  <!-- Large: 4 columns -->
">
  <!-- Grid items -->
</div>
```

## Accessibility Guidelines

### Focus States (Tailwind Classes)
```html
<!-- Standard focus ring -->
<button class="bg-cur-primary text-white py-3 px-6 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/30 focus:border-cur-primary">
  Accessible Button
</button>

<!-- Custom focus styles -->
<input class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/20 focus:border-cur-primary transition-all duration-200">

<!-- Focus-visible for keyboard navigation -->
<a href="#" class="text-cur-primary hover:text-cur-primary-600 focus:outline-none focus-visible:outline-2 focus-visible:outline-cur-primary focus-visible:outline-offset-2">
  Keyboard accessible link
</a>

<!-- Skip to content link -->
<a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-cur-primary text-white px-4 py-2 rounded-lg z-50">
  Skip to main content
</a>
```

### Color Contrast Standards
```html
<!-- High contrast text combinations -->
<div class="bg-white text-gray-900">WCAG AAA compliant (7:1+)</div>
<div class="bg-cur-primary text-white">WCAG AA compliant (4.5:1+)</div>
<div class="bg-gray-100 text-gray-800">WCAG AA compliant</div>

<!-- Warning: Low contrast combinations to avoid -->
<!-- <div class="bg-gray-200 text-gray-400">Too low contrast</div> -->

<!-- Accessible status colors -->
<div class="bg-green-500 text-white">Success message</div>
<div class="bg-red-500 text-white">Error message</div>
<div class="bg-yellow-500 text-black">Warning message</div>
<div class="bg-blue-500 text-white">Info message</div>
```

### Screen Reader Support (Tailwind Classes)
```html
<!-- Screen reader only content -->
<span class="sr-only">This content is only available to screen readers</span>

<!-- Accessible form labels -->
<div class="space-y-2">
  <label for="email" class="block text-sm font-medium text-gray-700">
    Email Address
    <span class="text-red-500" aria-label="required">*</span>
  </label>
  <input 
    type="email" 
    id="email" 
    name="email"
    required
    aria-describedby="email-error"
    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/20 focus:border-cur-primary"
    placeholder="Enter your email address"
  >
  <p id="email-error" class="text-sm text-red-600 hidden" role="alert">
    Please enter a valid email address
  </p>
</div>

<!-- Accessible buttons with proper ARIA -->
<button 
  type="button"
  aria-expanded="false"
  aria-controls="dropdown-menu"
  aria-haspopup="true"
  class="bg-cur-primary text-white px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/30"
>
  Open Menu
  <span class="sr-only">(opens dropdown menu)</span>
</button>

<!-- Accessible navigation with landmarks -->
<nav aria-label="Main navigation" class="bg-white border-b border-gray-200">
  <ul class="flex space-x-6 px-6 py-4">
    <li>
      <a href="/" aria-current="page" class="text-cur-primary font-medium">
        Home
        <span class="sr-only">(current page)</span>
      </a>
    </li>
    <li>
      <a href="/services" class="text-gray-600 hover:text-gray-900">
        Services
      </a>
    </li>
  </ul>
</nav>

<!-- Accessible modal -->
<div 
  class="fixed inset-0 bg-gray-600 bg-opacity-75 flex items-center justify-center z-50"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
>
  <div class="bg-white rounded-lg p-6 max-w-md w-full mx-4">
    <h2 id="modal-title" class="text-lg font-semibold text-gray-900 mb-2">
      Confirm Action
    </h2>
    <p id="modal-description" class="text-gray-600 mb-4">
      Are you sure you want to delete this item?
    </p>
    <div class="flex space-x-3">
      <button class="bg-red-500 text-white px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500/30">
        Delete
      </button>
      <button class="bg-gray-200 text-gray-800 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-300">
        Cancel
      </button>
    </div>
  </div>
</div>
```

### Interactive States & Feedback
```html
<!-- Loading states with accessibility -->
<button 
  class="bg-cur-primary text-white px-6 py-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-cur-primary/30 disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
  disabled
  aria-describedby="loading-text"
>
  <svg class="animate-spin h-4 w-4" viewBox="0 0 24 24" aria-hidden="true">
    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
    <path class="opacity-75" fill="currentColor" d="m4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
  </svg>
  <span id="loading-text">Processing...</span>
</button>

<!-- Error states with proper announcement -->
<div class="bg-red-50 border border-red-200 rounded-lg p-4" role="alert" aria-live="polite">
  <div class="flex items-start">
    <i class="fas fa-exclamation-triangle text-red-500 mt-0.5" aria-hidden="true"></i>
    <div class="ml-3">
      <h3 class="text-sm font-medium text-red-800">
        There was an error processing your request
      </h3>
      <p class="text-sm text-red-700 mt-1">
        Please check your information and try again.
      </p>
    </div>
  </div>
</div>

<!-- Success states -->
<div class="bg-green-50 border border-green-200 rounded-lg p-4" role="alert" aria-live="polite">
  <div class="flex items-start">
    <i class="fas fa-check-circle text-green-500 mt-0.5" aria-hidden="true"></i>
    <div class="ml-3">
      <h3 class="text-sm font-medium text-green-800">
        Success!
      </h3>
      <p class="text-sm text-green-700 mt-1">
        Your appointment has been booked successfully.
      </p>
    </div>
  </div>
</div>
```

## Booking Flow Components (Tailwind Classes)

### Service Selection Grid
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
  <!-- Individual Therapy Card -->
  <div class="bg-white border-2 border-gray-200 rounded-xl p-6 cursor-pointer transition-all duration-200 hover:border-cur-primary hover:shadow-cur hover:-translate-y-1 group">
    <div class="bg-cur-primary-100 rounded-lg w-16 h-16 flex items-center justify-center mb-4 group-hover:bg-cur-primary group-hover:text-white transition-colors">
      <i class="fas fa-user text-2xl text-cur-primary group-hover:text-white"></i>
    </div>
    <h3 class="font-poppins text-xl font-semibold text-gray-900 mb-2">Individual Therapy</h3>
    <p class="text-gray-600 mb-4">One-on-one sessions with certified therapists</p>
    <div class="flex items-center justify-between">
      <span class="text-2xl font-bold text-cur-primary">$80</span>
      <span class="text-sm text-gray-500">60 minutes</span>
    </div>
  </div>

  <!-- Group Therapy Card -->
  <div class="bg-gradient-to-br from-cur-secondary-50 to-white border-2 border-cur-secondary rounded-xl p-6 cursor-pointer transition-all duration-200 hover:shadow-cur hover:-translate-y-1 relative">
    <div class="absolute top-4 right-4 bg-cur-secondary text-white px-2 py-1 rounded-full text-xs font-medium">
      POPULAR
    </div>
    <div class="bg-cur-secondary-100 rounded-lg w-16 h-16 flex items-center justify-center mb-4">
      <i class="fas fa-users text-2xl text-cur-secondary"></i>
    </div>
    <h3 class="font-poppins text-xl font-semibold text-gray-900 mb-2">Group Therapy</h3>
    <p class="text-gray-600 mb-4">Small group sessions for shared experiences</p>
    <div class="flex items-center justify-between">
      <span class="text-2xl font-bold text-cur-secondary">$40</span>
      <span class="text-sm text-gray-500">90 minutes</span>
    </div>
  </div>

  <!-- Couple Therapy Card -->
  <div class="bg-white border-2 border-gray-200 rounded-xl p-6 cursor-pointer transition-all duration-200 hover:border-cur-accent hover:shadow-cur hover:-translate-y-1 group">
    <div class="bg-cur-accent-100 rounded-lg w-16 h-16 flex items-center justify-center mb-4 group-hover:bg-cur-accent group-hover:text-white transition-colors">
      <i class="fas fa-heart text-2xl text-cur-accent group-hover:text-white"></i>
    </div>
    <h3 class="font-poppins text-xl font-semibold text-gray-900 mb-2">Couples Therapy</h3>
    <p class="text-gray-600 mb-4">Relationship counseling for couples</p>
    <div class="flex items-center justify-between">
      <span class="text-2xl font-bold text-cur-accent">$120</span>
      <span class="text-sm text-gray-500">75 minutes</span>
    </div>
  </div>
</div>
```

### AI Therapist Matching
```html
<div class="space-y-6">
  <!-- AI Matching Header -->
  <div class="text-center bg-gradient-to-r from-cur-primary to-cur-secondary rounded-xl p-6 text-white mb-8">
    <i class="fas fa-brain text-4xl mb-4"></i>
    <h2 class="font-poppins text-2xl font-bold mb-2">AI-Powered Matching</h2>
    <p class="opacity-90">Our advanced algorithm matches you with the perfect therapist based on your needs and preferences</p>
  </div>

  <!-- Therapist Cards -->
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
    <!-- Best Match Therapist -->
    <div class="bg-gradient-to-br from-cur-primary-50 to-white border-2 border-cur-primary rounded-xl p-6 relative">
      <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-cur-primary text-white px-4 py-1 rounded-full text-sm font-semibold">
        🎯 BEST MATCH
      </div>
      
      <div class="flex items-start space-x-4 mt-4">
        <img src="https://via.placeholder.com/80" alt="Dr. Sarah Chen" class="w-20 h-20 rounded-xl object-cover">
        <div class="flex-1">
          <h3 class="font-poppins text-xl font-semibold text-gray-900">Dr. Sarah Chen</h3>
          <p class="text-cur-primary font-medium text-sm mb-2">Anxiety & Depression Specialist</p>
          
          <!-- Compatibility Score -->
          <div class="bg-cur-primary text-white px-3 py-1 rounded-full text-sm font-medium inline-block mb-3">
            95% Compatibility
          </div>
          
          <!-- Ratings -->
          <div class="flex items-center space-x-2 mb-3">
            <div class="flex text-yellow-400">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
            <span class="text-sm text-gray-600">(124 reviews)</span>
          </div>
        </div>
      </div>
      
      <!-- Matching Reasons -->
      <div class="mt-4 space-y-2">
        <div class="flex items-center text-sm">
          <i class="fas fa-check text-green-500 mr-2"></i>
          <span class="text-gray-700">Specializes in anxiety management</span>
        </div>
        <div class="flex items-center text-sm">
          <i class="fas fa-check text-green-500 mr-2"></i>
          <span class="text-gray-700">Experience with young adults</span>
        </div>
        <div class="flex items-center text-sm">
          <i class="fas fa-check text-green-500 mr-2"></i>
          <span class="text-gray-700">Available for evening sessions</span>
        </div>
      </div>
      
      <button class="w-full bg-cur-primary text-white font-medium py-3 rounded-lg mt-6 hover:bg-cur-primary-600 transition-colors">
        Select Dr. Chen
      </button>
    </div>
    
    <!-- Alternative Match -->
    <div class="bg-white border-2 border-gray-200 rounded-xl p-6 hover:border-cur-secondary transition-colors">
      <div class="flex items-start space-x-4">
        <img src="https://via.placeholder.com/80" alt="Dr. Michael Wang" class="w-20 h-20 rounded-xl object-cover">
        <div class="flex-1">
          <h3 class="font-poppins text-xl font-semibold text-gray-900">Dr. Michael Wang</h3>
          <p class="text-cur-secondary font-medium text-sm mb-2">Stress & Trauma Specialist</p>
          
          <div class="bg-cur-secondary text-white px-3 py-1 rounded-full text-sm font-medium inline-block mb-3">
            87% Compatibility
          </div>
          
          <div class="flex items-center space-x-2 mb-3">
            <div class="flex text-yellow-400">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star-half-alt"></i>
            </div>
            <span class="text-sm text-gray-600">(89 reviews)</span>
          </div>
        </div>
      </div>
      
      <div class="mt-4 space-y-2">
        <div class="flex items-center text-sm">
          <i class="fas fa-check text-green-500 mr-2"></i>
          <span class="text-gray-700">Trauma-informed therapy approach</span>
        </div>
        <div class="flex items-center text-sm">
          <i class="fas fa-check text-green-500 mr-2"></i>
          <span class="text-gray-700">Weekend availability</span>
        </div>
      </div>
      
      <button class="w-full bg-cur-secondary text-white font-medium py-3 rounded-lg mt-6 hover:bg-cur-secondary-600 transition-colors">
        Select Dr. Wang
      </button>
    </div>
  </div>
</div>
```

## Implementation Notes

### Tailwind CSS Setup
```javascript
// Install Tailwind CSS
npm install -D tailwindcss @tailwindcss/forms @tailwindcss/typography
npx tailwindcss init

// Add to your CSS file
@tailwind base;
@tailwind components;
@tailwind utilities;

// Add custom components
@layer components {
  .btn-primary {
    @apply bg-cur-primary hover:bg-cur-primary-600 text-white font-medium py-3 px-6 rounded-lg transition-all duration-200 hover:-translate-y-0.5 hover:shadow-cur;
  }
  
  .card {
    @apply bg-white rounded-xl p-6 shadow-sm border border-gray-200 transition-all duration-200 hover:shadow-cur hover:-translate-y-0.5;
  }
  
  .input-field {
    @apply w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-cur-primary/20 focus:border-cur-primary transition-all duration-200;
  }
}
```

### Performance Considerations
- **Purge unused CSS**: Tailwind automatically removes unused classes in production
- **JIT Mode**: Use Just-In-Time compilation for faster builds and smaller file sizes
- **Component extraction**: Use `@apply` directive for frequently used class combinations
- **Font optimization**: Use `font-display: swap` for custom fonts loaded via Google Fonts
- **Image optimization**: Implement WebP/AVIF formats with fallbacks

### Browser Support
- **Modern browsers**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **CSS Grid**: Full support in all target browsers
- **Custom properties**: Supported for theming
- **Flexbox**: Full support with fallbacks

### Development Workflow
```bash
# Watch for changes during development
npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch

# Build for production
npx tailwindcss -i ./src/input.css -o ./dist/output.css --minify

# Using with build tools
npm run build  # With Vite, Webpack, etc.
```

### Code Organization
```
src/
├── styles/
│   ├── tailwind.css          # Tailwind imports
│   ├── components/           # Custom component styles
│   │   ├── buttons.css
│   │   ├── forms.css
│   │   └── cards.css
│   └── utilities/            # Custom utilities
│       └── animations.css
├── components/               # HTML/React components
└── assets/                   # Images, fonts, etc.
```

### Maintenance Guidelines
- **Regular audits**: Use tools like `tailwind-css-unused` to find unused classes
- **Consistency checks**: Ensure color contrast ratios meet WCAG standards
- **Component updates**: Keep design system documentation in sync with implementations
- **Cross-device testing**: Test on various screen sizes and devices regularly
- **Performance monitoring**: Track CSS bundle size and loading performance

### Quality Assurance
- **Accessibility testing**: Use tools like axe-core or Lighthouse
- **Visual regression testing**: Implement automated screenshot comparisons
- **Browser testing**: Test across different browsers and versions
- **Code validation**: Use HTML5 validator and CSS linting tools

---

*Last updated: October 2024*
*Version: 2.1 - Tailwind CSS Implementation*
*Framework: Tailwind CSS 3.x with custom CUR-HEART theme*
