# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 5)

## 4.6 Teknologi yang Digunakan

Pemilihan teknologi dalam proyek CUR-HEART didasarkan pada pertimbangan matang terkait kebutuhan bisnis, kompleksitas sistem, skalabilitas, maintainability, dan kompetensi tim. Sistem ini mengadopsi **Monolithic Architecture** dengan **Laravel Full-Stack Framework** sebagai pondasi utama.

### 4.6.1 Arsitektur Sistem: Monolithic vs. Microservices

#### A. Pemilihan Monolithic Architecture

**Definisi:**
Monolithic architecture adalah pendekatan pengembangan software di mana seluruh aplikasi dibangun sebagai satu kesatuan (single unit) dengan codebase tunggal yang mencakup frontend, backend, dan business logic dalam satu aplikasi.

**Alasan Pemilihan untuk CUR-HEART:**

**1. Kompleksitas Proyek yang Moderat**
- Sistem CUR-HEART adalah medium-sized application dengan scope yang jelas
- Jumlah fitur terukur (41 pages, 3 roles, 6 services)
- Tidak memerlukan independent scaling untuk different components
- Monolithic lebih sesuai untuk project scale ini

**2. Tim yang Kecil (3 Developer)**
- Monolithic architecture lebih mudah di-develop oleh small team
- Single codebase lebih mudah untuk coordination
- Tidak perlu overhead untuk inter-service communication
- Simplified deployment process

**3. Timeline yang Ketat (11 Minggu)**
- Monolithic faster untuk initial development
- Less boilerplate code dibanding microservices
- Single deployment pipeline
- Fokus pada feature delivery, bukan infrastructure setup

**4. Operational Simplicity**
- Single server deployment (VPS)
- Easier debugging dan troubleshooting
- Simplified monitoring dan logging
- Lower infrastructure cost

**5. Consistency dan Data Integrity**
- Single database dengan ACID transactions
- Referential integrity enforcement via foreign keys
- No distributed transaction complexity
- Easier data consistency management

**Perbandingan:**

| Aspek | Monolithic (Dipilih) | Microservices (Tidak Dipilih) |
|-------|----------------------|-------------------------------|
| **Development Speed** | ✅ Fast (cocok untuk MVP) | ❌ Slower (banyak setup) |
| **Team Size** | ✅ Small team friendly | ❌ Butuh larger, specialized team |
| **Deployment** | ✅ Simple, single deploy | ❌ Complex, multiple deploys |
| **Testing** | ✅ Easier (integrated tests) | ❌ Complex (integration tests antar services) |
| **Infrastructure** | ✅ Single server | ❌ Multiple servers/containers |
| **Cost** | ✅ Low (Rp 1.2 juta/tahun hosting) | ❌ High (Rp 5-10 juta/tahun) |
| **Debugging** | ✅ Straightforward | ❌ Distributed tracing needed |
| **Consistency** | ✅ Strong consistency | ❌ Eventual consistency |
| **Scalability** | ⚠️ Vertical scaling only | ✅ Horizontal scaling per service |
| **Technology Stack** | ⚠️ Single stack (PHP/Laravel) | ✅ Polyglot (multi-language) |

**Kesimpulan:**
Untuk project CUR-HEART, monolithic architecture adalah pilihan yang **optimal** karena:
- Faster time-to-market
- Lower complexity dan cost
- Adequate untuk current scale (target 200 users, 100 bookings/month)
- Dapat di-refactor ke microservices di masa depan jika needed

---

### 4.6.2 Technology Stack Details

#### A. Backend Framework: Laravel 10.x

**Pemilihan Laravel sebagai Framework Utama:**

**1. Full-Stack Capability**
Laravel bukan hanya backend framework, tetapi **full-stack framework** yang mencakup:
- **Backend**: Routing, controllers, models, business logic
- **Frontend**: Blade templating engine, asset compilation (Vite)
- **Database**: Eloquent ORM, migrations, seeders
- **Authentication**: Laravel Breeze/Sanctum
- Tidak perlu framework JavaScript terpisah (React, Vue) untuk project ini

**2. MVC Architecture Pattern**

Laravel mengimplementasikan **Model-View-Controller (MVC)** pattern:

```
┌─────────────────────────────────────────────────────────┐
│                    MVC ARCHITECTURE                      │
└─────────────────────────────────────────────────────────┘

   User Request (HTTP)
          │
          ▼
   ┌─────────────┐
   │   ROUTES    │  (web.php, api.php)
   │  (Router)   │  - Define URL patterns
   └──────┬──────┘  - Map to Controllers
          │
          ▼
   ┌─────────────┐
   │ CONTROLLER  │  (BookingController, UserController, etc.)
   │             │  - Handle HTTP requests
   │             │  - Validate input
   │             │  - Call business logic
   │             │  - Return responses
   └──────┬──────┘
          │
          ├──────────────┐
          ▼              ▼
   ┌─────────────┐  ┌─────────────┐
   │   MODEL     │  │    VIEW     │  (Blade Templates)
   │             │  │             │  - Render HTML
   │  (Eloquent) │  │  (Blade)    │  - Display data
   │             │  │             │  - User interface
   │- User       │  │- layouts/   │
   │- Booking    │  │- components/│
   │- Service    │  │- pages/     │
   └──────┬──────┘  └─────────────┘
          │
          ▼
   ┌─────────────┐
   │  DATABASE   │  (MySQL)
   │             │  - Store data
   │  (MySQL)    │  - Relationships
   └─────────────┘  - Integrity
```

**Keuntungan MVC:**
- **Separation of Concerns**: Business logic (Model), presentation (View), dan flow control (Controller) terpisah
- **Maintainability**: Easier to maintain dan debug
- **Reusability**: Models dan Views dapat digunakan kembali
- **Testability**: Each layer dapat di-test independently

**3. Eloquent ORM (Object-Relational Mapping)**

Eloquent adalah Laravel's Active Record implementation untuk database interaction:

**Keunggulan Eloquent:**
- **Expressive Syntax**: Query yang readable seperti bahasa natural
- **Relationship Handling**: Easy to define dan query relationships
- **Protection dari SQL Injection**: Automatic query parameterization
- **Eager Loading**: Solve N+1 query problem
- **Model Events**: Hooks untuk automation (creating, updating, deleting)

**Contoh Eloquent Query:**
```php
// Daripada raw SQL:
$bookings = DB::select('SELECT * FROM bookings WHERE client_id = ? AND status = ?', [$clientId, 'confirmed']);

// Eloquent lebih expressive:
$bookings = Booking::where('client_id', $clientId)
                   ->where('status', 'confirmed')
                   ->with('therapist', 'service') // eager load relationships
                   ->orderBy('booking_date', 'desc')
                   ->get();
```

**4. Blade Templating Engine**

Blade adalah Laravel's powerful templating engine untuk views:

**Fitur Blade:**
- **Template Inheritance**: Layouts dan sections
- **Components**: Reusable UI components
- **Directives**: `@if`, `@foreach`, `@auth`, dll.
- **Raw PHP Support**: Fleksibilitas jika diperlukan
- **Automatic Escaping**: XSS protection

**Contoh Blade Template:**
```blade
{{-- layouts/app.blade.php --}}
<!DOCTYPE html>
<html>
<head>
    <title>@yield('title') - CUR-HEART</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
    @include('components.navbar')
    
    <main>
        @yield('content')
    </main>
    
    @include('components.footer')
</body>
</html>

{{-- pages/booking.blade.php --}}
@extends('layouts.app')

@section('title', 'Book Appointment')

@section('content')
    <h1>Book Your Session</h1>
    
    @foreach($services as $service)
        <x-service-card :service="$service" />
    @endforeach
@endsection
```

**5. Built-in Security Features**

Laravel provide security features out-of-the-box:

| Security Feature | Implementasi | Benefit |
|-----------------|--------------|---------|
| **CSRF Protection** | `@csrf` directive dalam forms | Prevent Cross-Site Request Forgery |
| **XSS Prevention** | Auto-escape `{{ }}` syntax | Prevent Cross-Site Scripting |
| **SQL Injection** | Eloquent query bindings | Parameterized queries |
| **Password Hashing** | `Hash::make()` dengan bcrypt | Secure password storage |
| **Encryption** | `encrypt()` / `decrypt()` | Protect sensitive data |
| **Rate Limiting** | Throttle middleware | Prevent brute-force attacks |

**6. Laravel Ecosystem & Packages**

Laravel memiliki rich ecosystem:

| Package | Fungsi dalam CUR-HEART | Benefit |
|---------|------------------------|---------|
| **Laravel Breeze** | Authentication scaffolding | Quick setup login/register |
| **Laravel Mail** | Email notifications | Booking confirmation, reminders |
| **Laravel Queue** | Background jobs | Async email sending, report generation |
| **Laravel Validation** | Input validation | Data integrity, security |
| **Laravel Pagination** | Data pagination | Efficient large dataset handling |
| **Laravel Mix/Vite** | Asset compilation | CSS/JS bundling, hot reload |

**7. Developer Experience (DX)**

Laravel dikenal dengan excellent DX:
- **Artisan CLI**: Command-line tool untuk generate code, migrations, dll.
- **Laravel Tinker**: REPL untuk interact dengan aplikasi
- **Laravel Telescope**: Debugging assistant (optional)
- **Comprehensive Documentation**: docs.laravel.com
- **Large Community**: Stack Overflow, Laracasts, forums
- **Regular Updates**: Long-term support (LTS) versions

**Contoh Artisan Commands:**
```bash
# Generate controller
php artisan make:controller BookingController --resource

# Run database migrations
php artisan migrate

# Seed database with sample data
php artisan db:seed

# Clear cache
php artisan cache:clear

# Generate model with migration
php artisan make:model Booking -m
```

---

#### B. Programming Language: PHP 8.x

**Pemilihan PHP 8.x:**

**1. Laravel Requirements**
- Laravel 10.x requires PHP 8.1 or higher
- Leverage PHP 8 modern features

**2. PHP 8 Modern Features yang Digunakan:**

**a. Named Arguments**
```php
// Lebih readable
$booking = Booking::create(
    client_id: $clientId,
    therapist_id: $therapistId,
    service_id: $serviceId,
    booking_date: $date,
    time_slot: $time
);
```

**b. Union Types**
```php
public function findUser(int|string $identifier): User|null
{
    return User::find($identifier);
}
```

**c. Match Expression**
```php
$message = match($booking->status) {
    'pending' => 'Waiting for payment',
    'confirmed' => 'Booking confirmed',
    'completed' => 'Session completed',
    'cancelled' => 'Booking cancelled',
    default => 'Unknown status'
};
```

**d. Nullsafe Operator**
```php
// Prevent null pointer errors
$therapistName = $booking?->therapist?->user?->name;
```

**3. Performance Improvements**
- JIT (Just-In-Time) compilation
- Improved type system
- Better memory management

---

#### C. Database: MySQL 8.0

**Pemilihan MySQL sebagai RDBMS:**

**1. Relational Data Structure**
CUR-HEART memiliki data yang highly relational:
- Users ↔ Therapists/Clients (one-to-one)
- Therapists ↔ Services (many-to-many)
- Bookings ↔ Payments (one-to-one)
- Bookings ↔ Sessions (one-to-one)
- Sessions ↔ Session Notes (one-to-one)

**Keuntungan RDBMS:**
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **Data Integrity**: Foreign key constraints, unique constraints
- **Complex Queries**: JOIN operations untuk related data
- **Transaction Support**: Critical untuk payment processing

**2. MySQL 8.0 Features yang Digunakan:**

**a. Window Functions**
```sql
-- Ranking therapists by earnings
SELECT 
    therapist_id,
    SUM(amount) as total_earnings,
    RANK() OVER (ORDER BY SUM(amount) DESC) as ranking
FROM payments
GROUP BY therapist_id;
```

**b. JSON Support**
```sql
-- Store flexible data (e.g., specializations, techniques)
CREATE TABLE therapists (
    id BIGINT PRIMARY KEY,
    specializations JSON,
    -- e.g., ["Anxiety", "Trauma", "Stress"]
);

-- Query JSON data
SELECT * FROM therapists 
WHERE JSON_CONTAINS(specializations, '"Anxiety"');
```

**c. CTEs (Common Table Expressions)**
```sql
-- Complex reporting queries
WITH monthly_stats AS (
    SELECT 
        MONTH(booking_date) as month,
        COUNT(*) as total_bookings,
        SUM(amount) as revenue
    FROM bookings
    JOIN payments ON bookings.id = payments.booking_id
    GROUP BY MONTH(booking_date)
)
SELECT * FROM monthly_stats WHERE revenue > 10000000;
```

**3. Indexing Strategy**

Index yang diimplementasikan untuk performance:

```sql
-- Primary indexes (automatic)
PRIMARY KEY (id)

-- Unique indexes untuk data integrity
UNIQUE INDEX idx_email ON users(email);
UNIQUE INDEX idx_booking_number ON bookings(booking_number);

-- Foreign key indexes untuk JOIN performance
INDEX idx_bookings_client_id ON bookings(client_id);
INDEX idx_bookings_therapist_id ON bookings(therapist_id);

-- Composite indexes untuk complex queries
INDEX idx_bookings_date_status ON bookings(booking_date, status);
INDEX idx_therapist_date_time ON bookings(therapist_id, booking_date, time_slot);

-- Full-text indexes untuk search
FULLTEXT INDEX idx_services_search ON services(name, description);
```

**4. Database Normalization**

Seperti dijelaskan di Bagian 2, database dinormalisasi hingga 3NF:
- **1NF**: Atomic values, no repeating groups
- **2NF**: No partial dependencies
- **3NF**: No transitive dependencies

Benefits:
- Reduced data redundancy
- Easier maintenance
- Data consistency
- Referential integrity

---

#### D. Frontend: Tailwind CSS

**Pemilihan Tailwind CSS:**

**1. Utility-First Approach**

Tailwind menggunakan utility classes daripada custom CSS:

**Contoh:**
```html
<!-- Traditional CSS -->
<style>
.card {
    background-color: white;
    border-radius: 0.5rem;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
<div class="card">Content</div>

<!-- Tailwind CSS -->
<div class="bg-white rounded-lg p-6 shadow-md">Content</div>
```

**Keuntungan:**
- **Faster Development**: No need untuk switch antara HTML dan CSS file
- **Consistency**: Design tokens (spacing, colors) pre-defined
- **No Naming Issues**: Tidak perlu mikir class names (BEM, SMACSS, dll.)
- **Smaller CSS Bundle**: Purge unused CSS (production build <10KB)

**2. Responsive Design Built-in**

Tailwind provide breakpoint utilities:

```html
<!-- Mobile-first responsive design -->
<div class="
    w-full          <!-- mobile: full width -->
    md:w-1/2        <!-- tablet: 50% width -->
    lg:w-1/3        <!-- desktop: 33% width -->
    p-4             <!-- padding all sides -->
    md:p-6          <!-- larger padding on tablet+ -->
">
    Responsive Card
</div>
```

**Breakpoints:**
- `sm`: 640px (mobile landscape)
- `md`: 768px (tablet)
- `lg`: 1024px (desktop)
- `xl`: 1280px (large desktop)
- `2xl`: 1536px (extra large)

**3. Design System Integration**

Tailwind configuration untuk CUR-HEART design system:

```javascript
// tailwind.config.js
module.exports = {
    theme: {
        extend: {
            colors: {
                // CUR-HEART brand colors
                primary: {
                    50: '#f5f3ff',
                    100: '#ede9fe',
                    // ... shades
                    900: '#1E0E62', // Primary Navy
                },
                secondary: {
                    500: '#FF6B7A', // Secondary Pink
                },
                accent: {
                    teal: '#4ECDC4',
                    purple: '#8B5FBF',
                }
            },
            fontFamily: {
                sans: ['Poppins', 'sans-serif'], // Headings
                body: ['Inter', 'sans-serif'],    // Body text
            },
            spacing: {
                '128': '32rem', // Custom spacing
            }
        }
    }
}
```

**Usage:**
```html
<h1 class="text-primary-900 font-sans text-4xl font-bold">
    Welcome to CUR-HEART
</h1>
<p class="text-gray-700 font-body text-base">
    Book your therapy session today.
</p>
<button class="bg-secondary-500 hover:bg-secondary-600 text-white px-6 py-3 rounded-lg">
    Book Now
</button>
```

**4. Component Reusability dengan @apply**

Untuk components yang sering digunakan:

```css
/* resources/css/app.css */
@layer components {
    .btn-primary {
        @apply bg-primary-900 text-white font-semibold py-2 px-4 rounded-lg hover:bg-primary-800 transition duration-200;
    }
    
    .card {
        @apply bg-white rounded-lg shadow-md p-6;
    }
    
    .input-field {
        @apply border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-primary-500;
    }
}
```

**5. Dark Mode Support (Optional)**

Tailwind support dark mode out-of-the-box:

```html
<div class="bg-white dark:bg-gray-800 text-gray-900 dark:text-white">
    Content adapts to color scheme
</div>
```

---

#### E. JavaScript: Vanilla JS + Alpine.js (Optional)

**Pemilihan JavaScript Approach:**

**1. Vanilla JavaScript untuk Simple Interactions**

Untuk simple interactions, pure JavaScript sudah cukup:

```javascript
// Form validation
document.getElementById('bookingForm').addEventListener('submit', function(e) {
    const date = document.getElementById('booking_date').value;
    if (!date) {
        e.preventDefault();
        alert('Please select a date');
    }
});

// Dynamic pricing display
function updatePrice(serviceId) {
    const prices = {
        1: 250000,
        2: 300000,
        3: 350000
    };
    document.getElementById('price').textContent = 
        `Rp ${prices[serviceId].toLocaleString('id-ID')}`;
}
```

**2. Alpine.js untuk Reactivity (Optional)**

Alpine.js adalah lightweight JavaScript framework (15KB gzipped) untuk add reactivity:

**Contoh: Dropdown Toggle**
```html
<div x-data="{ open: false }">
    <button @click="open = !open">
        Menu
    </button>
    <div x-show="open" @click.away="open = false">
        <a href="/profile">Profile</a>
        <a href="/logout">Logout</a>
    </div>
</div>
```

**Contoh: Form Step Navigation**
```html
<div x-data="{ step: 1 }">
    <!-- Step Indicator -->
    <div class="flex">
        <div :class="step >= 1 ? 'active' : ''">1. Service</div>
        <div :class="step >= 2 ? 'active' : ''">2. Therapist</div>
        <div :class="step >= 3 ? 'active' : ''">3. Schedule</div>
        <div :class="step >= 4 ? 'active' : ''">4. Confirm</div>
    </div>
    
    <!-- Step Content -->
    <div x-show="step === 1">Service Selection</div>
    <div x-show="step === 2">Therapist Selection</div>
    <div x-show="step === 3">Schedule Selection</div>
    <div x-show="step === 4">Confirmation</div>
    
    <!-- Navigation -->
    <button @click="step--" x-show="step > 1">Back</button>
    <button @click="step++" x-show="step < 4">Next</button>
</div>
```

**Keuntungan Alpine.js:**
- **Declarative**: Reactive behavior dalam HTML
- **Lightweight**: Small bundle size
- **No Build Step**: Dapat digunakan langsung via CDN
- **Laravel-Friendly**: Created by Taylor Otwell's friend

**Alternatif yang TIDAK Dipilih:**

| Framework | Kenapa Tidak Dipilih |
|-----------|---------------------|
| **React** | - Overkill untuk project ini<br>- Complex build setup<br>- Learning curve tinggi<br>- Butuh API (frontend-backend separation) |
| **Vue.js** | - Tidak perlu SPA (Single Page Application)<br>- Laravel Blade sudah cukup<br>- Additional complexity |
| **jQuery** | - Outdated (2024)<br>- Large file size<br>- Modern vanilla JS lebih baik |

---

#### F. Version Control: Git & GitHub

**Git untuk Source Code Management:**

**1. Branching Strategy**

Kami menggunakan **Git Flow** simplified:

```
main (production)
  │
  └─── development (integration)
         │
         ├─── feature/booking-flow
         ├─── feature/therapist-dashboard
         ├─── feature/admin-panel
         └─── bugfix/payment-validation
```

**Branch Types:**
- **main**: Production-ready code
- **development**: Integration branch untuk features
- **feature/***: Individual feature development
- **bugfix/***: Bug fixes
- **hotfix/***: Urgent production fixes

**2. Commit Convention**

Mengikuti **Conventional Commits**:

```
feat: add booking confirmation email
fix: resolve double booking issue
docs: update API documentation
style: format code with PSR-12
refactor: optimize database queries
test: add unit tests for BookingController
chore: update dependencies
```

**3. GitHub untuk Collaboration**

**Repository Structure:**
```
cur-heart-system/
├── .github/
│   └── workflows/          # GitHub Actions (CI/CD)
├── app/
│   ├── Http/Controllers/
│   ├── Models/
│   └── Services/
├── database/
│   ├── migrations/
│   └── seeders/
├── resources/
│   ├── views/
│   ├── css/
│   └── js/
├── routes/
├── tests/
├── .env.example
├── composer.json
└── README.md
```

**Pull Request Workflow:**
1. Create feature branch dari development
2. Develop feature dengan commits yang atomic
3. Push ke GitHub
4. Create Pull Request ke development
5. Code review oleh team member
6. Merge setelah approval dan tests pass

---

### 4.6.3 Development Tools

#### A. Integrated Development Environment (IDE)

**Visual Studio Code (Primary)**

**Extensions yang Digunakan:**
- **Laravel Extension Pack**: Snippets, blade syntax highlighting
- **PHP Intelephense**: PHP autocomplete dan intellisense
- **Tailwind CSS IntelliSense**: Class autocomplete
- **GitLens**: Git integration
- **Better Comments**: Color-coded comments
- **Error Lens**: Inline error display
- **Prettier**: Code formatting
- **ESLint**: JavaScript linting

**VS Code Settings untuk Laravel:**
```json
{
    "php.suggest.basic": false,
    "intelephense.files.associations": ["*.php", "*.blade.php"],
    "emmet.includeLanguages": {
        "blade": "html"
    },
    "tailwindCSS.includeLanguages": {
        "blade": "html"
    }
}
```

---

#### B. Dependency Management

**1. Composer (PHP Dependencies)**

**composer.json:**
```json
{
    "require": {
        "php": "^8.1",
        "laravel/framework": "^10.0",
        "laravel/breeze": "^1.20",
        "intervention/image": "^2.7",
        "barryvdh/laravel-dompdf": "^2.0"
    },
    "require-dev": {
        "laravel/telescope": "^4.14",
        "nunomaduro/larastan": "^2.0",
        "phpunit/phpunit": "^10.0"
    }
}
```

**Commands:**
```bash
composer install          # Install dependencies
composer update           # Update dependencies
composer dump-autoload    # Regenerate autoload files
```

**2. NPM (Frontend Dependencies)**

**package.json:**
```json
{
    "devDependencies": {
        "tailwindcss": "^3.3.0",
        "autoprefixer": "^10.4.14",
        "postcss": "^8.4.23",
        "vite": "^4.0.0",
        "laravel-vite-plugin": "^0.7.5",
        "alpinejs": "^3.12.0"
    }
}
```

**Commands:**
```bash
npm install           # Install dependencies
npm run dev           # Development build with watch
npm run build         # Production build
```

---

#### C. Database Tools

**1. Laravel Migrations**

Database version control:

```php
// database/migrations/2024_01_01_create_bookings_table.php
public function up()
{
    Schema::create('bookings', function (Blueprint $table) {
        $table->id();
        $table->string('booking_number')->unique();
        $table->foreignId('client_id')->constrained('users');
        $table->foreignId('therapist_id')->constrained('therapists');
        $table->foreignId('service_id')->constrained('services');
        $table->date('booking_date');
        $table->time('time_slot');
        $table->enum('status', ['pending', 'confirmed', 'completed', 'cancelled']);
        $table->timestamps();
    });
}
```

**2. phpMyAdmin / TablePlus**

GUI untuk database management:
- Browse tables
- Execute queries
- Export/import data
- Monitor performance

---

#### D. Testing Tools

**1. PHPUnit (Unit & Feature Tests)**

```php
// tests/Feature/BookingTest.php
public function test_user_can_create_booking()
{
    $user = User::factory()->create();
    $service = Service::factory()->create();
    $therapist = Therapist::factory()->create();
    
    $response = $this->actingAs($user)->post('/bookings', [
        'service_id' => $service->id,
        'therapist_id' => $therapist->id,
        'booking_date' => '2024-12-01',
        'time_slot' => '10:00',
    ]);
    
    $response->assertStatus(201);
    $this->assertDatabaseHas('bookings', [
        'client_id' => $user->id,
        'service_id' => $service->id,
    ]);
}
```

**2. Browser Testing (Manual)**

Test pada multiple browsers:
- Chrome (primary)
- Firefox
- Safari
- Edge
- Mobile browsers (Chrome Mobile, Safari iOS)

---

#### E. Deployment Tools

**1. Laravel Forge / Laravel Envoyer (Optional)**

Automated deployment:
- Push to GitHub → auto-deploy ke server
- Zero-downtime deployment
- SSL certificate management

**2. Manual Deployment (Budget-Friendly)**

```bash
# On server via SSH
cd /var/www/cur-heart
git pull origin main
composer install --optimize-autoloader --no-dev
php artisan migrate --force
php artisan config:cache
php artisan route:cache
php artisan view:cache
npm run build
php artisan queue:restart
```

---

### 4.6.4 Infrastructure & Hosting

#### A. Server Requirements

**Minimum Specifications:**
- **OS**: Ubuntu 22.04 LTS
- **Web Server**: Nginx 1.18+ atau Apache 2.4+
- **PHP**: 8.1+ dengan extensions (mbstring, xml, bcmath, curl, gd, mysql)
- **Database**: MySQL 8.0+
- **Memory**: 2GB RAM minimum
- **Storage**: 20GB SSD
- **SSL**: Let's Encrypt (free)

**Recommended VPS:**
- DigitalOcean Droplet ($12/month)
- Vultr Cloud Compute ($10/month)
- AWS Lightsail ($10/month)
- Niagahoster VPS Indonesia (Rp 100,000/bulan)

---

#### B. Domain & DNS

**Domain Name:**
- `cur-heart.id` atau `curheart.co.id`
- Registrar: Niagahoster, Rumahweb, GoDaddy
- Cost: Rp 150,000/tahun (.id domain)

**DNS Configuration:**
```
A Record:  @ → [Server IP]
A Record:  www → [Server IP]
CNAME:     api → cur-heart.id
MX Record: @ → mail.cur-heart.id (untuk email)
```

---

#### C. SSL Certificate

**Let's Encrypt (Free):**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d cur-heart.id -d www.cur-heart.id
```

**Auto-renewal:**
```bash
sudo certbot renew --dry-run
```

Certificate auto-renew setiap 60 hari.

---

#### D. Backup Strategy

**1. Database Backup (Daily)**

**Script:**
```bash
#!/bin/bash
# /usr/local/bin/backup-db.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/var/backups/mysql"
DB_NAME="curheart_db"

mysqldump -u root -p${DB_PASSWORD} ${DB_NAME} | gzip > ${BACKUP_DIR}/curheart_${DATE}.sql.gz

# Keep only last 30 days
find ${BACKUP_DIR} -name "curheart_*.sql.gz" -mtime +30 -delete
```

**Cron Job:**
```cron
0 2 * * * /usr/local/bin/backup-db.sh
```

**2. File Backup (Weekly)**

```bash
tar -czf /var/backups/files/curheart_$(date +%Y%m%d).tar.gz /var/www/cur-heart
```

**3. Off-Site Backup**

Upload ke cloud storage:
- Google Drive (free 15GB)
- AWS S3 (pay-as-you-go)
- Backblaze B2 (cheap)

---

### 4.6.5 Third-Party Integrations

#### A. Payment Gateway: Midtrans

**Pilihan Midtrans:**
- **Local**: Indonesia-based, support Bahasa
- **Payment Methods**: Credit card, e-wallet (GoPay, OVO, Dana), bank transfer, QRIS
- **Pricing**: 2% + Rp 1,000 per transaction
- **Security**: PCI-DSS certified
- **Documentation**: Comprehensive API docs

**Integration:**
```php
// app/Services/PaymentService.php
use Midtrans\Snap;

public function createTransaction($booking)
{
    $params = [
        'transaction_details' => [
            'order_id' => $booking->booking_number,
            'gross_amount' => $booking->service->price,
        ],
        'customer_details' => [
            'first_name' => $booking->client->name,
            'email' => $booking->client->email,
            'phone' => $booking->client->phone,
        ],
        'item_details' => [[
            'id' => $booking->service->id,
            'price' => $booking->service->price,
            'quantity' => 1,
            'name' => $booking->service->name,
        ]],
    ];
    
    return Snap::createTransaction($params);
}
```

---

#### B. Email Service: SMTP / Mailtrap

**Production**: SMTP (Gmail, SendGrid, Mailgun)
**Development**: Mailtrap (testing)

**Laravel Mail Configuration:**
```env
MAIL_MAILER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=curheart.system@gmail.com
MAIL_PASSWORD=app_password
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=noreply@cur-heart.id
MAIL_FROM_NAME="CUR-HEART"
```

---

#### C. Video Conferencing (Optional)

**Embedded Solutions:**
- **Zoom**: Embed Zoom meeting
- **Google Meet**: iframe integration
- **Whereby**: API-based embedded rooms

**Alternative**: Build in-house dengan WebRTC (future enhancement)

---

## 4.7 Desiminasi Proyek

Desiminasi adalah proses penyebarluasan atau publikasi hasil proyek kepada stakeholders dan masyarakat luas. Tujuannya untuk showcase hasil kerja, mendapatkan feedback, dan memberikan value kepada komunitas.

### 4.7.1 Dokumentasi Proyek

#### A. Laporan Makalah Capstone Project

**Dokumen Ini:**
- **Format**: PDF, hardcover untuk submission
- **Jumlah Halaman**: 80-100 halaman
- **Struktur**: Sesuai pedoman Capstone Project UNM
- **Bahasa**: Indonesia formal akademik
- **Distribusi**:
  - Submit ke dosen pembimbing
  - Perpustakaan UNM (arsip)
  - Repository digital (academia.edu, ResearchGate)

**Konten:**
- BAB I: Pendahuluan
- BAB II: Tinjauan Pustaka
- BAB III: Metodologi
- BAB IV: Hasil dan Pembahasan (this chapter)
- BAB V: Penutup
- Lampiran: Mockups, code samples, testing results

---

#### B. Technical Documentation

**1. User Manual**

**Target Audience**: End users (clients, therapists, admin)

**Konten:**
- Panduan registrasi dan login
- Cara booking layanan (step-by-step dengan screenshot)
- Cara reschedule/cancel booking
- Cara menggunakan dashboard
- FAQ (Frequently Asked Questions)
- Troubleshooting common issues
- Contact support

**Format:**
- PDF (downloadable dari website)
- Online help center (web pages)
- Video tutorials (embedded di help center)

**Bahasa**: Bahasa Indonesia (user-friendly, non-technical)

---

**2. Developer Documentation**

**Target Audience**: Future developers, maintainers

**Konten:**
- Project setup guide
- Architecture overview
- Database schema documentation
- API documentation (jika ada)
- Code style guide (PSR-12 for PHP)
- Deployment guide
- Git workflow
- Testing guide

**Format:**
- Markdown files di GitHub repository
- Generated docs dengan tools (PHPDoc, Doxygen)

**Lokasi**: `/docs` folder dalam repository

**Contoh Structure:**
```
/docs
├── setup.md              # Installation guide
├── architecture.md       # System architecture
├── database.md           # Database documentation
├── api.md                # API reference
├── deployment.md         # Deployment guide
├── contributing.md       # Contribution guidelines
└── changelog.md          # Version history
```

---

**3. Admin Documentation**

**Target Audience**: System administrators, CUR-HEART management

**Konten:**
- Server management guide
- Backup and restore procedures
- Security best practices
- Monitoring and logging
- Performance optimization
- Troubleshooting server issues
- Update and maintenance schedule

---

### 4.7.2 Video Promosi

#### A. Tujuan Video

**Primary Goals:**
1. **Marketing**: Promote CUR-HEART dan sistem booking
2. **Education**: Educate target audience tentang kemudahan sistem
3. **Engagement**: Increase brand awareness di social media

**Target Audience:**
- Potential clients (individuals dengan mental health concerns)
- Corporate HR (untuk employee wellness programs)
- Healthcare community

---

#### B. Konten Video

**Duration**: 2-3 menit

**Script Outline:**

**Opening (15 detik)**
- Hook: "Stress, anxiety, insomnia? Saatnya ambil kendali atas kesehatan mental Anda."
- Logo CUR-HEART dengan tagline

**Problem Statement (20 detik)**
- Statistik: "70% orang Indonesia mengalami stress di era modern"
- Pain points: Susah booking terapis, tidak tahu pilih terapis mana, proses ribet

**Solution Introduction (30 detik)**
- Introduce CUR-HEART hypnotherapy services
- Show website interface (landing page)
- Highlight: "Booking online, mudah, cepat, 24/7"

**Feature Showcase (60 detik)**

*Scene 1: Browse Services (10 detik)*
- Screen recording: Scroll halaman Services
- Voiceover: "6 layanan hypnotherapy untuk berbagai kebutuhan"

*Scene 2: Choose Therapist (10 detik)*
- Screen recording: Browse therapist profiles
- Voiceover: "Pilih terapis bersertifikat sesuai spesialisasi"

*Scene 3: Select Schedule (10 detik)*
- Screen recording: Calendar selection
- Voiceover: "Pilih jadwal yang cocok dengan Anda"

*Scene 4: Payment (5 detik)*
- Screen recording: Payment options
- Voiceover: "Bayar mudah dengan berbagai metode"

*Scene 5: Confirmation (5 detik)*
- Show booking confirmation
- Voiceover: "Langsung terima konfirmasi dan reminder"

*Scene 6: Session (10 detik)*
- B-roll: Terapis doing session (stock footage atau actual footage)
- Voiceover: "Terapi profesional di lingkungan yang nyaman dan rahasia"

*Scene 7: Progress Tracking (10 detik)*
- Screen recording: Progress dashboard
- Voiceover: "Track progress dan lihat perkembangan Anda"

**Social Proof (15 detik)**
- Testimonial snippet dari client (text atau video)
- Star rating: "4.8/5.0 dari 100+ clients puas"

**Call-to-Action (20 detik)**
- "Mulai perjalanan transformasi Anda hari ini"
- Show website URL: www.cur-heart.id
- Show contact: WhatsApp, Instagram, Email
- Special offer: "Diskon 20% untuk booking pertama"

**Closing (10 detik)**
- Logo CUR-HEART
- Tagline: "Transformasi Diri Dimulai Dari Sini"
- Social media handles

---

#### C. Production Details

**Equipment:**
- Screen recording: OBS Studio, Camtasia
- Video editing: DaVinci Resolve (free), Adobe Premiere Pro
- Graphics: Canva, After Effects
- Music: Royalty-free dari Epidemic Sound, Artlist

**Visual Style:**
- Clean, modern, calming aesthetics
- Brand colors: Navy #1E0E62, Pink #FF6B7A
- Smooth transitions
- Text overlays untuk key points
- Subtle animations

**Music:**
- Calm, uplifting background music
- Low volume (not overpowering voiceover)
- Fade in/out smoothly

**Voiceover:**
- Professional voice talent atau AI voice (ElevenLabs)
- Warm, friendly, reassuring tone
- Clear articulation, moderate pace
- Bahasa Indonesia atau bilingual (ID + EN subtitles)

---

#### D. Distribution Channels

**1. YouTube**
- Upload ke channel CUR-HEART
- Optimize title, description, tags untuk SEO
- Add end screen dengan subscribe button dan website link
- Create playlist: "CUR-HEART Services"

**SEO Title**: "Booking Terapi Hypnotherapy Online Mudah di CUR-HEART | Sistem Terpadu"

**Description**:
```
Stress? Anxiety? Trauma? 

CUR-HEART adalah pusat hypnotherapy modern dengan sistem booking online yang mudah dan cepat. Pilih terapis bersertifikat, jadwal fleksibel, bayar mudah - semua dalam satu platform.

🌟 Layanan Kami:
✅ Stress & Anxiety Release
✅ Trauma Healing
✅ Self-Confidence Boost
✅ Sleep Therapy
✅ Habit Reprogramming
✅ Phobia Management

🎯 Keunggulan:
• Terapis bersertifikat & berpengalaman
• Booking online 24/7
• Sesi tatap muka atau online
• Progress tracking
• Lingkungan rahasia & nyaman

📅 Book Sekarang: www.cur-heart.id
📱 WhatsApp: 0812-3456-7890
📧 Email: info@cur-heart.id

#Hypnotherapy #KesehatanMental #TherapiOnline #CURHEART #MentalWellness
```

**2. Instagram**
- IGTV: Full video 2-3 menit
- Reels: Short version 30-60 detik (vertical format)
- Stories: Behind-the-scenes, snippets
- Feed Post: Teaser dengan link di bio

**3. TikTok**
- Short version 15-60 detik
- Trending sounds, hashtags
- Educational snippets (series)

**4. Facebook**
- Post di company page
- Share di groups (mental health, wellness, women communities)
- Facebook Ads (boosted post)

**5. LinkedIn**
- Professional format
- Target corporate decision-makers
- Emphasize employee wellness benefits

**6. Website**
- Embed di homepage (hero section atau about section)
- Dedicated "How It Works" page dengan video
- Blog post accompanying video

---

### 4.7.3 X-Banner

#### A. Purpose

X-Banner adalah media promosi fisik untuk:
- Presentasi proyek (showcase)
- Event kampus (pameran Capstone Project)
- On-site promotion di CUR-HEART office
- Networking events, career fair

---

#### B. Design Specifications

**Size**: 60 cm × 160 cm (standard X-banner size)

**Layout Structure:**

```
┌──────────────────────────────────┐
│         HEADER (20 cm)           │ ← Logo CUR-HEART, Judul Proyek
├──────────────────────────────────┤
│                                  │
│      PROBLEM (15 cm)             │ ← Statistik, pain points
│                                  │
├──────────────────────────────────┤
│                                  │
│      SOLUTION (20 cm)            │ ← Screenshot sistem, fitur utama
│                                  │
├──────────────────────────────────┤
│                                  │
│      BENEFITS (20 cm)            │ ← Icons + short descriptions
│                                  │
├──────────────────────────────────┤
│                                  │
│      TECH STACK (15 cm)          │ ← Technology logos
│                                  │
├──────────────────────────────────┤
│                                  │
│      PROJECT INFO (30 cm)        │ ← Team, timeline, deliverables
│                                  │
├──────────────────────────────────┤
│      FOOTER (40 cm)              │ ← Contact, QR code, social media
└──────────────────────────────────┘
```

---

#### C. Content

**Header:**
- Logo CUR-HEART (large)
- Title: "SISTEM INFORMASI MANAJEMEN BOOKING DAN TERAPI CUR-HEART"
- Subtitle: "Capstone Project - Proyek Sistem Informasi"

**Problem Section:**
- **Headline**: "Tantangan dalam Manajemen Layanan Hypnotherapy"
- **Bullet Points**:
  - ❌ Booking manual via telepon/WhatsApp
  - ❌ Prone to double booking dan errors
  - ❌ Sulitnya koordinasi jadwal terapis
  - ❌ Reporting manual memakan waktu

**Solution Section:**
- **Headline**: "Solusi: Platform Booking Online Terintegrasi"
- **Screenshot**: Dashboard interface (annotated)
- **Key Features** (dengan icons):
  - 📅 Online Booking 24/7
  - 👨‍⚕️ Profil Terapis Lengkap
  - 💳 Multiple Payment Methods
  - 📊 Progress Tracking
  - 📈 Automated Reporting

**Benefits Section:**
- **For Business**:
  - 🚀 Efisiensi +50%
  - 💰 Revenue +25%
  - ⏱️ Time Saving 20 jam/bulan
- **For Clients**:
  - ✨ Easy Booking
  - 🔍 Transparency
  - 📱 Self-Service
- **For Therapists**:
  - 🗓️ Flexible Scheduling
  - 📝 Digital Documentation
  - 💼 Earnings Dashboard

**Tech Stack:**
- Laravel, PHP, MySQL, Tailwind CSS logos (with labels)
- Monolithic Architecture illustration

**Project Info:**
- **Team**: Roki Anjas, Susanto, Fahruroji
- **Timeline**: 11 Minggu (September - November 2024)
- **Deliverables**: Web Application, Documentation, Video, X-Banner
- **University**: Universitas Nusa Mandiri
- **Program Studi**: Sistem Informasi

**Footer:**
- **Contact**: 
  - 🌐 www.cur-heart.id
  - 📧 info@cur-heart.id
  - 📱 0812-3456-7890
- **QR Code**: Link ke website (prominent, center)
- **Social Media**: @curheart (Instagram, Facebook, TikTok icons)
- **Scan**: "Scan untuk demo langsung"

---

#### D. Design Guidelines

**Color Scheme:**
- Primary: Navy #1E0E62
- Secondary: Pink #FF6B7A
- Accent: Teal #4ECDC4, Purple #8B5FBF
- Background: White #FFFFFF dengan subtle gradients
- Text: Dark gray #333333

**Typography:**
- Heading: Poppins Bold (large, attention-grabbing)
- Body: Inter Regular (readable, clean)
- Size: Minimal 16pt untuk readability dari jarak 2 meter

**Visual Elements:**
- High-quality screenshots (minimum 300 DPI untuk print)
- Icons dari Heroicons atau Feather Icons (consistent style)
- Infographics untuk statistics (bar charts, pie charts)
- Whitespace yang cukup (not too crowded)

**Print Specifications:**
- Resolution: 300 DPI
- Color Mode: CMYK (for print)
- File Format: PDF (vector) atau PNG (high-res)
- Bleed: Add 3mm bleed area

---

#### E. Production

**Design Software:**
- Adobe Illustrator (best for vector)
- Adobe Photoshop (for photo editing)
- Canva Pro (template-based, easier)
- Figma (collaborative design)

**Printing:**
- **Vendor**: Percetakan lokal (Jakarta, Surabaya)
- **Material**: Flexi China 280 gsm atau Flexi Korea 340 gsm
- **Finishing**: Matte lamination (reduce glare)
- **Stand**: X-banner stand (aluminum, adjustable)
- **Cost**: Rp 150,000 - Rp 250,000 per banner

**Quantity:**
- 2 units: 1 untuk presentasi, 1 untuk CUR-HEART office

---

### 4.7.4 Artikel Publikasi

#### A. Jurnal Ilmiah (Optional)

**Target Journal:**
- Jurnal Sistem Informasi (JSI)
- Jurnal Teknik Informatika dan Sistem Informasi (JuTISI)
- IJCCS (Indonesian Journal of Computing and Cybernetics Systems)

**Article Type**: Case study atau technical report

**Structure:**
- Abstract
- Introduction
- Literature Review
- Methodology
- Results and Discussion
- Conclusion
- References

**Submission Timeline:**
- After project completion dan presentation
- Target publication: 6 bulan setelah submission

---

#### B. Blog Post / Medium Article

**Platform**: Medium, Dev.to, personal blog

**Title Ideas:**
- "Building a Mental Health Booking System with Laravel: A Case Study"
- "From Idea to Implementation: CUR-HEART Hypnotherapy Management System"
- "Monolithic vs. Microservices: Choosing the Right Architecture for SME"

**Content:**
- Technical deep-dive
- Lessons learned
- Code snippets (sanitized)
- Architecture diagrams
- Performance metrics

**Audience**: Developer community, entrepreneurs, students

---

### 4.7.5 Presentasi Final

#### A. Slide Presentasi

**Structure (15-20 slides):**

1. **Title Slide**: Project name, team, logo
2. **Agenda**: Outline presentasi
3. **Background**: Latar belakang masalah
4. **Problem Statement**: Pain points yang specific
5. **Objectives**: Tujuan proyek
6. **Solution Overview**: High-level solution
7. **System Architecture**: Diagram arsitektur
8. **Database Design**: ERD (simplified)
9. **Key Features**: Screenshot dengan annotations
10. **Technology Stack**: Technologies yang digunakan
11. **Development Process**: Timeline, milestones
12. **Demo**: Live demo atau video demo
13. **Testing Results**: Test cases, performance metrics
14. **Benefits & ROI**: Quantified benefits
15. **Challenges & Solutions**: Obstacles dan how we overcame
16. **Lessons Learned**: Key takeaways
17. **Future Enhancements**: Roadmap
18. **Conclusion**: Summary
19. **Q&A**: Questions slide
20. **Thank You**: Contact info

**Design:**
- Consistent dengan brand colors
- Minimal text (use bullet points)
- High-quality images dan screenshots
- Charts dan infographics
- Smooth transitions

---

#### B. Live Demo

**Preparation:**
- Stable internet connection (backup: hotspot)
- Pre-populated database dengan sample data
- Test run sebelum presentation (rehearsal)
- Fallback: Video recording jika live demo gagal

**Demo Flow (5-7 menit):**
1. Landing page walkthrough
2. User registration dan login
3. Browse services dan therapists
4. Complete booking flow (all 4 steps)
5. Show booking confirmation
6. Quick tour: Client dashboard, therapist dashboard, admin panel
7. Highlight key features: calendar, progress tracking, reporting

---

#### C. Delivery

**Duration**: 15 menit presentasi + 5 menit Q&A

**Tips:**
- **Practice**: Rehearse multiple times
- **Confidence**: Speak clearly, maintain eye contact
- **Storytelling**: Narrate, don't just read slides
- **Engagement**: Ask rhetorical questions, interact dengan audience
- **Time Management**: Stay within 15 minutes
- **Handle Questions**: Listen carefully, answer confidently, admit if don't know

---

### 4.7.6 Social Media Campaign

#### A. Pre-Launch Teaser

**Timeline**: 2 minggu sebelum launch

**Content Ideas:**
- Countdown posts (7 hari hingga launch)
- Behind-the-scenes (team working, coding, design process)
- Feature sneak peeks (screenshot blur dengan "Coming Soon")
- Problem-solution posts (educate audience)

---

#### B. Launch Announcement

**D-Day**: Grand launch

**Content:**
- Launch post dengan video promosi
- Giveaway/contest untuk early adopters
- Special offer (discount 20% first booking)
- Press release (jika applicable)

---

#### C. Post-Launch Content

**Ongoing (monthly):**
- Success stories (client testimonials dengan permission)
- Educational content (mental health tips, hypnotherapy myths vs. facts)
- Feature highlights (deep-dive per feature)
- Team interviews
- Industry news dan insights

**Hashtags:**
- Branded: #CURHEART #CURHEARTWellness
- Industry: #MentalHealth #Hypnotherapy #Wellness #TherapyOnline
- Location: #JakartaTherapy #IndonesiaWellness

---

### 4.7.7 Evaluation Metrics

#### A. Documentation Metrics

- ✅ User manual completion rate
- ✅ Developer documentation coverage (lines documented / total lines)
- ✅ Documentation feedback score dari users

#### B. Video Metrics

- 👁️ Views (target: 10,000 views dalam 3 bulan)
- 👍 Engagement rate (likes, comments, shares)
- 🔗 Click-through rate ke website
- ⏱️ Average watch time (target: >70% completion)

#### C. X-Banner Metrics

- 📸 Photos taken dengan banner (track via hashtag)
- 💬 Conversations started dari banner exposure
- 🎯 Lead generation (QR code scans)

#### D. Social Media Metrics

- 👥 Follower growth (target: 1,000 followers dalam 3 bulan)
- 📊 Engagement rate (target: >5%)
- 🔗 Website traffic dari social media
- 💰 Conversion rate (social media visitors → bookings)

---

**[End of BAB IV - Hasil Penelitian dan Pembahasan]**

**Total BAB IV terdiri dari 5 bagian file:**
1. Bagian 1: 4.1 & 4.2 (Inisiasi & Perencanaan)
2. Bagian 2: 4.3.3 Database Design
3. Bagian 3: 4.3.4 UML Diagrams
4. Bagian 4: 4.4 & 4.5 (Faktor Keberhasilan & Keuntungan)
5. Bagian 5: 4.6 & 4.7 (Teknologi & Desiminasi) ← File ini

**Selanjutnya:** BAB V - Penutup (Kesimpulan dan Saran)
