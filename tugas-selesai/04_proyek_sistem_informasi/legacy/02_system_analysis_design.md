# SYSTEM ANALYSIS & DESIGN
## SATRIAMART Integrated Management System (SIMS)

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi II**

---

## BUSINESS REQUIREMENTS DOCUMENT (BRD)

### 1. EXECUTIVE SUMMARY

SATRIAMART Integrated Management System (SIMS) adalah solusi sistem informasi terintegrasi yang dirancang untuk mengoptimalkan operasional bisnis SATRIAMART dalam bidang dekorasi & aksesoris akrilik. Sistem ini menggabungkan 4 modul utama: Customer Relationship Management (CRM), Inventory Management, Production Planning, dan Sales Analytics.

### 2. BUSINESS OBJECTIVES

#### Primary Business Objectives
1. **Meningkatkan Efisiensi Operasional:** Automasi proses manual untuk mengurangi waktu dan kesalahan
2. **Optimasi Inventory Management:** Real-time tracking dan automatic reorder untuk menghindari stockout
3. **Peningkatan Customer Satisfaction:** Better customer service melalui centralized customer data
4. **Data-Driven Decision Making:** Analytics dan reporting untuk strategic business decisions

#### Key Performance Indicators (KPIs)
- Pengurangan waktu proses order sebesar 50%
- Akurasi inventory meningkat hingga 95%
- Customer response time berkurang 60%
- Peningkatan customer retention sebesar 25%

### 3. CURRENT BUSINESS PROCESS ANALYSIS

#### 3.1 Current State Problems
1. **Manual Customer Management:**
   - Data pelanggan tersebar di berbagai file Excel
   - Sulit tracking communication history
   - Duplikasi data dan inconsistency

2. **Inventory Management Issues:**
   - Stock checking manual dan time-consuming
   - Sering terjadi stockout atau overstock
   - Tidak ada early warning system

3. **Production Planning Challenges:**
   - Perencanaan produksi berdasarkan estimasi
   - Resource allocation tidak optimal
   - Delivery delays karena poor planning

4. **Limited Business Intelligence:**
   - Laporan sales manual
   - Tidak ada trend analysis
   - Decision making berdasarkan intuisi

#### 3.2 Desired Future State
1. **Integrated Customer Management:**
   - Single source of truth untuk customer data
   - Complete customer journey tracking
   - Automated communication workflows

2. **Real-time Inventory Control:**
   - Live inventory status
   - Automated reorder points
   - Supplier integration

3. **Optimized Production Planning:**
   - Data-driven production scheduling
   - Resource optimization
   - Demand forecasting

4. **Comprehensive Analytics:**
   - Real-time dashboards
   - Predictive analytics
   - Automated reporting

### 4. FUNCTIONAL REQUIREMENTS SPECIFICATION

#### 4.1 Customer Relationship Management (CRM) Module

**FR-CRM-001: Customer Registration & Profile Management**
- System harus dapat menyimpan customer data lengkap (contact info, preferences, history)
- Support untuk individual dan corporate customers
- Customer categorization dan segmentation
- Integration dengan social media profiles

**FR-CRM-002: Order Management**
- Complete order lifecycle management
- Custom product specification handling
- Order status tracking dan notifications
- Integration dengan production planning

**FR-CRM-003: Communication Tracking**
- Log semua customer interactions (call, email, meeting)
- Automated follow-up reminders
- Communication templates
- Integration dengan email dan phone systems

**FR-CRM-004: Customer Analytics**
- Customer behavior analysis
- Purchase pattern identification
- Customer lifetime value calculation
- Churn prediction analytics

#### 4.2 Inventory Management Module

**FR-INV-001: Raw Material Management**
- Track berbagai jenis akrilik (thickness, color, grade)
- Accessories dan component tracking
- Batch/lot number management
- Quality control status

**FR-INV-002: Finished Goods Management**
- Product catalog dengan specifications
- Multi-location inventory tracking
- Serial number tracking untuk custom products
- Product image dan documentation

**FR-INV-003: Automated Reorder System**
- Configurable reorder points
- Automatic purchase order generation
- Supplier performance tracking
- Lead time optimization

**FR-INV-004: Inventory Analytics**
- ABC analysis untuk inventory prioritization
- Turn-over rate analysis
- Slow-moving inventory identification
- Cost analysis reporting

#### 4.3 Production Planning Module

**FR-PROD-001: Work Order Management**
- Automatic work order generation dari sales orders
- Resource requirement calculation
- Production schedule optimization
- Progress tracking

**FR-PROD-002: Resource Allocation**
- Machine capacity planning
- Staff allocation dan shift management
- Tool dan equipment scheduling
- Bottleneck identification

**FR-PROD-003: Quality Control Integration**
- Quality checkpoints dalam production process
- Defect tracking dan analysis
- Rework management
- Quality reports

**FR-PROD-004: Production Analytics**
- Efficiency metrics dan KPIs
- Downtime analysis
- Yield optimization
- Capacity utilization reports

#### 4.4 Sales & Analytics Dashboard

**FR-DASH-001: Real-time Sales Dashboard**
- Live sales performance metrics
- Regional dan product-wise analysis
- Sales team performance tracking
- Revenue forecasting

**FR-DASH-002: Executive Dashboard**
- High-level business KPIs
- Trend analysis dan comparisons
- Profitability analysis
- Strategic metrics visualization

**FR-DASH-003: Operational Dashboard**
- Production status overview
- Inventory alerts dan notifications
- Customer service metrics
- Supply chain status

**FR-DASH-004: Custom Reporting**
- Ad-hoc report generation
- Scheduled report delivery
- Export capabilities (PDF, Excel, CSV)
- Report sharing dan collaboration

### 5. NON-FUNCTIONAL REQUIREMENTS

#### 5.1 Performance Requirements
- **Response Time:** Average page load time < 3 seconds
- **Throughput:** Support minimum 100 concurrent users
- **Scalability:** Horizontal scaling capability for future growth
- **Availability:** 99.5% uptime (max 3.6 hours downtime per month)

#### 5.2 Security Requirements
- **Authentication:** Multi-factor authentication untuk admin users
- **Authorization:** Role-based access control (RBAC)
- **Data Encryption:** AES-256 encryption for sensitive data
- **Audit Trail:** Complete user activity logging
- **Backup:** Daily automated backups dengan 30-day retention

#### 5.3 Usability Requirements
- **User Interface:** Intuitive dan user-friendly design
- **Learning Curve:** New users dapat productive dalam 2 hari training
- **Accessibility:** WCAG 2.1 compliance untuk accessibility
- **Mobile Support:** Responsive design untuk tablet dan mobile

#### 5.4 Compatibility Requirements
- **Browser Support:** Chrome, Firefox, Safari, Edge (latest versions)
- **Operating System:** Platform independent (web-based)
- **Database:** MySQL compatibility
- **Integration:** REST API untuk third-party integrations

### 6. USE CASE SCENARIOS

#### Use Case 1: Customer Order Processing
**Actor:** Sales Representative  
**Goal:** Process new customer order efficiently  

**Main Flow:**
1. Sales rep logs into CRM module
2. Search atau create customer profile
3. Create new order dengan product specifications
4. System automatically checks inventory availability
5. Generate quotation untuk customer approval
6. Upon approval, order masuk ke production planning
7. Customer receives order confirmation dengan timeline
8. System sends automated updates pada key milestones

**Alternative Flows:**
- Jika inventory insufficient: System suggests alternatives atau backorder
- Jika custom specifications: Route ke design team untuk feasibility check

#### Use Case 2: Inventory Replenishment
**Actor:** Inventory Manager  
**Goal:** Maintain optimal inventory levels  

**Main Flow:**
1. System monitors inventory levels continuously
2. Ketika stock mencapai reorder point, system generates alert
3. Manager reviews recommendation dan supplier options
4. System creates purchase order
5. Track delivery status dan update inventory upon receipt
6. System updates inventory levels dan availability

#### Use Case 3: Production Scheduling
**Actor:** Production Manager  
**Goal:** Optimize production schedule untuk delivery commitments  

**Main Flow:**
1. System analyzes pending orders dan resource availability
2. Generate optimal production schedule
3. Manager reviews dan adjusts schedule jika perlu
4. Assign work orders ke production teams
5. Track progress real-time
6. System alerts jika delays atau issues detected

---

## SYSTEM DESIGN DOCUMENT (SDD)

### 1. SYSTEM ARCHITECTURE

#### 1.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                           │
├─────────────────────────────────────────────────────────────────┤
│  Web Browser  │  Mobile App  │  Admin Portal  │  API Gateway   │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                             │
├─────────────────────────────────────────────────────────────────┤
│  CRM Service  │ Inventory Svc │ Production Svc │ Analytics Svc   │
│               │               │                │                 │
│ • Customer    │ • Raw Material│ • Work Orders  │ • Dashboards   │
│   Management  │   Tracking    │ • Scheduling   │ • Reports      │
│ • Order Mgmt  │ • Reorder     │ • Resource     │ • KPIs         │
│ • Communication│   Management  │   Allocation   │ • Forecasting  │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                     DATA LAYER                                  │
├─────────────────────────────────────────────────────────────────┤
│  Customer DB  │ Inventory DB  │ Production DB  │ Analytics DB    │
│               │               │                │                 │
│ MySQL         │ MySQL         │ MySQL          │ MySQL +         │
│               │               │                │ Data Warehouse  │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│               EXTERNAL INTEGRATIONS                             │
├─────────────────────────────────────────────────────────────────┤
│  Email System │ SMS Gateway   │ Payment Gateway│ Supplier APIs   │
└─────────────────────────────────────────────────────────────────┘
```

#### 1.2 Technology Stack

**Frontend:**
- **Framework:** TailwindCSS untuk responsive design
- **JavaScript:** Vanilla JavaScript (ES6+)
- **UI Components:** Custom components dengan TailwindCSS
- **Build Tool:** Laravel Mix (Webpack)

**Backend:**
- **Framework:** Laravel (PHP)
- **Language:** PHP 8.0+
- **API Style:** RESTful APIs dengan Laravel API Resources
- **Authentication:** Laravel Sanctum untuk API tokens

**Database:**
- **Primary Database:** MySQL untuk transactional data
- **Cache:** Redis untuk session management dan caching
- **Analytics:** Separate data warehouse untuk reporting

**Infrastructure:**
- **Cloud Provider:** AWS atau Google Cloud Platform
- **Containerization:** Docker untuk development dan deployment
- **CI/CD:** GitHub Actions atau GitLab CI
- **Monitoring:** Laravel Telescope untuk debugging dan monitoring

### 2. DATABASE DESIGN

#### 2.1 Entity Relationship Diagram (ERD)

```sql
-- CUSTOMER MANAGEMENT ENTITIES
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_type ENUM('individual', 'corporate'),
    company_name VARCHAR(255),
    contact_person VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(50),
    address TEXT,
    city VARCHAR(100),
    province VARCHAR(100),
    postal_code VARCHAR(10),
    customer_category VARCHAR(50),
    credit_limit DECIMAL(15,2),
    payment_terms VARCHAR(50),
    status ENUM('active', 'inactive', 'suspended'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_number VARCHAR(50) UNIQUE,
    order_date DATE,
    delivery_date DATE,
    order_status ENUM('draft', 'confirmed', 'in_production', 'ready', 'delivered', 'cancelled'),
    total_amount DECIMAL(15,2),
    discount_amount DECIMAL(15,2),
    tax_amount DECIMAL(15,2),
    notes TEXT,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INVENTORY MANAGEMENT ENTITIES
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255),
    description TEXT,
    parent_category_id INT REFERENCES categories(category_id)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(category_id),
    product_code VARCHAR(50) UNIQUE,
    product_name VARCHAR(255),
    description TEXT,
    specifications JSON,
    unit_of_measure VARCHAR(20),
    unit_price DECIMAL(10,2),
    reorder_point INT,
    reorder_quantity INT,
    supplier_id INT,
    status ENUM('active', 'discontinued'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id),
    location_id INT,
    quantity_on_hand INT,
    quantity_reserved INT,
    quantity_available AS (quantity_on_hand - quantity_reserved),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PRODUCTION MANAGEMENT ENTITIES
CREATE TABLE work_orders (
    work_order_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    work_order_number VARCHAR(50) UNIQUE,
    product_id INT REFERENCES products(product_id),
    quantity_ordered INT,
    quantity_produced INT,
    start_date DATE,
    due_date DATE,
    completion_date DATE,
    status ENUM('planned', 'in_progress', 'completed', 'cancelled'),
    priority ENUM('low', 'medium', 'high', 'urgent'),
    assigned_to INT,
    notes TEXT
);

CREATE TABLE production_resources (
    resource_id SERIAL PRIMARY KEY,
    resource_name VARCHAR(255),
    resource_type ENUM('machine', 'equipment', 'tool'),
    capacity_per_hour DECIMAL(8,2),
    status ENUM('available', 'busy', 'maintenance', 'offline'),
    location VARCHAR(255)
);

-- SYSTEM ENTITIES
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(255) UNIQUE,
    password_hash VARCHAR(255),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    role_id INT,
    department VARCHAR(100),
    status ENUM('active', 'inactive'),
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50),
    description TEXT,
    permissions JSON
);
```

#### 2.2 Data Dictionary

| Table | Field | Type | Description | Constraints |
|-------|-------|------|-------------|-------------|
| customers | customer_id | SERIAL | Primary key | NOT NULL, AUTO_INCREMENT |
| customers | customer_type | ENUM | Type of customer | 'individual', 'corporate' |
| customers | email | VARCHAR(255) | Customer email | UNIQUE, NOT NULL |
| orders | order_number | VARCHAR(50) | Unique order identifier | UNIQUE, NOT NULL |
| orders | order_status | ENUM | Current order status | Default: 'draft' |
| products | product_code | VARCHAR(50) | Unique product identifier | UNIQUE, NOT NULL |
| inventory | quantity_available | COMPUTED | Available quantity | quantity_on_hand - quantity_reserved |

### 3. USER INTERFACE DESIGN

#### 3.1 Design Principles
- **Consistency:** Uniform look and feel across all modules
- **Simplicity:** Clean, uncluttered interface dengan clear navigation
- **Efficiency:** Minimize clicks dan keystrokes untuk common tasks
- **Responsiveness:** Optimal viewing pada desktop, tablet, dan mobile
- **Accessibility:** Support untuk users dengan disabilities

#### 3.2 Main Navigation Structure

```
SATRIAMART SIMS
├── Dashboard
│   ├── Executive Overview
│   ├── Sales Performance
│   ├── Operations Status
│   └── Alerts & Notifications
├── Customer Management (CRM)
│   ├── Customer List
│   ├── Orders Management
│   ├── Communication History
│   └── Customer Analytics
├── Inventory Management
│   ├── Product Catalog
│   ├── Stock Levels
│   ├── Purchase Orders
│   └── Inventory Reports
├── Production Planning
│   ├── Work Orders
│   ├── Production Schedule
│   ├── Resource Management
│   └── Quality Control
├── Sales & Analytics
│   ├── Sales Dashboard
│   ├── Financial Reports
│   ├── Performance Analytics
│   └── Forecasting
└── System Administration
    ├── User Management
    ├── Role & Permissions
    ├── System Settings
    └── Audit Logs
```

#### 3.3 Key Screen Wireframes

**Dashboard Main Screen:**
```
┌─────────────────────────────────────────────────────────────────┐
│ SATRIAMART SIMS                    [User Menu] [Notifications]  │
├─────────────────────────────────────────────────────────────────┤
│ [Dashboard] [CRM] [Inventory] [Production] [Analytics] [Admin]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │
│ │ Total Sales │ │Active Orders│ │ Inventory   │ │ Production  │ │
│ │ IDR 125M    │ │     47      │ │   Status    │ │  Schedule   │ │
│ │ ↗ +12%      │ │ ↗ +5 today  │ │  ⚠ 3 Low   │ │ ✓ On Track  │ │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │                Sales Trend Chart                           │ │
│ │     [Line chart showing sales performance over time]       │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│ ┌─────────────────────┐ ┌─────────────────────────────────────┐ │
│ │ Recent Orders       │ │ Alerts & Notifications              │ │
│ │ Order #2024-001     │ │ • Low stock: Acrylic Sheet 5mm      │ │
│ │ Order #2024-002     │ │ • Overdue: Order #2024-015          │ │
│ │ Order #2024-003     │ │ • New customer registration         │ │
│ └─────────────────────┘ └─────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

**Customer Management Screen:**
```
┌─────────────────────────────────────────────────────────────────┐
│ Customer Management                            [+ Add Customer] │
├─────────────────────────────────────────────────────────────────┤
│ [Search] [Filter] [Export]                                      │
├─────────────────────────────────────────────────────────────────┤
│ Customer Name     │ Type      │ Last Order │ Total Value │ Action│
│ PT ABC Corp       │ Corporate │ 2024-01-15 │ IDR 25M     │ [View]│
│ John Doe          │ Individual│ 2024-01-10 │ IDR 2.5M    │ [View]│
│ CV XYZ            │ Corporate │ 2024-01-08 │ IDR 15M     │ [View]│
├─────────────────────────────────────────────────────────────────┤
│                    [< Previous] [1] [2] [3] [Next >]            │
└─────────────────────────────────────────────────────────────────┘
```

### 4. INTEGRATION SPECIFICATIONS

#### 4.1 Internal Module Integration
- **CRM ↔ Inventory:** Real-time stock check during order creation
- **CRM ↔ Production:** Automatic work order generation dari confirmed orders
- **Inventory ↔ Production:** Material consumption tracking dan allocation
- **All Modules ↔ Analytics:** Data pipeline untuk reporting dan analytics

#### 4.2 External System Integration
- **Email System:** SMTP integration untuk automated notifications
- **SMS Gateway:** REST API integration untuk SMS notifications
- **Payment Gateway:** Integration dengan local payment providers
- **Accounting System:** API integration untuk financial data sync

#### 4.3 API Specifications

**RESTful API Endpoints:**

```javascript
// Customer Management APIs
GET    /api/customers              // Get all customers
POST   /api/customers              // Create new customer
GET    /api/customers/{id}         // Get specific customer
PUT    /api/customers/{id}         // Update customer
DELETE /api/customers/{id}         // Delete customer

// Order Management APIs
GET    /api/orders                 // Get all orders
POST   /api/orders                 // Create new order
GET    /api/orders/{id}            // Get specific order
PUT    /api/orders/{id}/status     // Update order status

// Inventory APIs
GET    /api/products               // Get all products
GET    /api/inventory/levels       // Get current stock levels
POST   /api/inventory/adjustment   // Stock adjustment
GET    /api/inventory/alerts       // Get low stock alerts

// Production APIs
GET    /api/workorders             // Get all work orders
POST   /api/workorders             // Create work order
PUT    /api/workorders/{id}        // Update work order
GET    /api/production/schedule    // Get production schedule
```

**API Response Format:**
```json
{
  "status": "success|error",
  "message": "Human readable message",
  "data": {
    // Response data
  },
  "pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_records": 100
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

## CONCLUSION

System Analysis & Design document ini menyediakan blueprint lengkap untuk pengembangan SATRIAMART Integrated Management System. Design ini menggabungkan best practices dalam software architecture dengan specific business requirements dari SATRIAMART.

Key design decisions:
1. **Modular Architecture:** Memungkinkan independent development dan maintenance
2. **Scalable Database Design:** Normalized structure dengan performance optimization
3. **User-Centric Interface:** Intuitive design untuk minimize learning curve
4. **API-First Approach:** Memungkinkan future integrations dan mobile development
5. **Security by Design:** Built-in security measures dari authentication hingga data protection

Design ini siap untuk fase implementation dengan clear specifications dan guidelines untuk development team.
