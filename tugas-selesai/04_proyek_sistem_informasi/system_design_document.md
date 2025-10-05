# SYSTEM DESIGN DOCUMENT (SDD)
## SATRIAMART INTEGRATED MANAGEMENT SYSTEM (SIMS)

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Semester 7**

---

**Mata Kuliah:** Proyek Sistem Informasi II  
**Dosen Pengampu:** Rani Irma Handayani, M.Kom  
**Technical Lead:** [Nama Mahasiswa 3]  
**Tanggal:** Oktober 2025  
**Versi:** 1.0

---

## TABLE OF CONTENTS

1. [Introduction](#1-introduction)
2. [System Architecture](#2-system-architecture)
3. [Technology Stack](#3-technology-stack)
4. [Database Design](#4-database-design)
5. [Module Design](#5-module-design)
6. [API Specifications](#6-api-specifications)
7. [Security Design](#7-security-design)
8. [Performance Design](#8-performance-design)
9. [Integration Design](#9-integration-design)
10. [Deployment Architecture](#10-deployment-architecture)

---

## 1. INTRODUCTION

### 1.1 Document Purpose
Document ini menjabarkan technical design untuk SATRIAMART Integrated Management System (SIMS), mencakup system architecture, database design, API specifications, dan technical implementation details.

### 1.2 System Overview
SIMS adalah web-based integrated management system yang terdiri dari 4 core modules:
- **Customer Relationship Management (CRM)**
- **Inventory Management System**
- **Production Planning System**
- **Sales & Analytics Dashboard**

### 1.3 Design Principles

**Modularity:** System dirancang dalam modular architecture untuk maintainability  
**Scalability:** Support untuk future growth dan additional features  
**Security:** Built-in security measures untuk data protection  
**Performance:** Optimized untuk responsive user experience  
**Usability:** Intuitive interface dengan minimal learning curve  
**Integration:** Seamless integration between modules  

### 1.4 Design Constraints

**Technology Constraints:**
- Academic project dengan budget limitations
- Open-source technologies preference
- Cloud-based deployment untuk accessibility
- Mobile-responsive design requirement

**Performance Constraints:**
- Support minimum 10 concurrent users
- Response time <3 seconds untuk standard operations
- 99.5% availability during business hours

**Security Constraints:**
- Role-based access control implementation
- Data encryption untuk sensitive information
- Audit trail untuk all system activities

---

## 2. SYSTEM ARCHITECTURE

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
├─────────────────────────────────────────────────────────────┤
│  Web Client    │  Mobile Client   │  Admin Dashboard       │
│  (React.js)    │  (Responsive)    │  (Management)          │
└─────────────────┬───────────────────┬─────────────────────────┘
                  │                   │
┌─────────────────▼───────────────────▼─────────────────────────┐
│                    APPLICATION LAYER                        │
├─────────────────────────────────────────────────────────────┤
│           API Gateway & Authentication Service              │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│ CRM Service │ Inventory   │ Production  │ Analytics Service │
│             │ Service     │ Service     │                   │
└─────────────┴─────────────┴─────────────┴───────────────────┘
                  │
┌─────────────────▼─────────────────────────────────────────────┐
│                     DATA LAYER                               │
├─────────────────────────────────────────────────────────────┤
│  Primary Database  │  Analytics DB   │  File Storage        │
│  (PostgreSQL)      │  (Optional)     │  (Cloud Storage)     │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Architectural Patterns

**Pattern 1: Model-View-Controller (MVC)**
- **Model:** Database entities dan business logic
- **View:** React.js frontend components
- **Controller:** API endpoints dan request handling

**Pattern 2: Service-Oriented Architecture (SOA)**
- Microservices untuk each business module
- API Gateway untuk service coordination
- Independent service deployment

**Pattern 3: Repository Pattern**
- Data access abstraction layer
- Centralized database operations
- Support untuk multiple data sources

### 2.3 Component Architecture

#### 2.3.1 Frontend Components
```
src/
├── components/
│   ├── common/           # Shared components
│   ├── crm/             # CRM module components
│   ├── inventory/       # Inventory module components
│   ├── production/      # Production module components
│   └── analytics/       # Analytics module components
├── services/            # API service calls
├── store/              # State management
├── utils/              # Utility functions
└── assets/             # Static assets
```

#### 2.3.2 Backend Components
```
src/
├── controllers/         # API endpoint controllers
├── services/           # Business logic services
├── models/             # Database models
├── middleware/         # Authentication, validation
├── routes/             # API route definitions
├── config/             # Configuration files
└── utils/              # Helper functions
```

---

## 3. TECHNOLOGY STACK

### 3.1 Frontend Technology Stack

**Core Framework:** React.js 18.x  
**State Management:** Redux Toolkit atau Context API  
**UI Framework:** Material-UI (MUI) 5.x atau Ant Design  
**Routing:** React Router 6.x  
**HTTP Client:** Axios  
**Charts/Visualization:** Chart.js atau Recharts  
**Build Tool:** Vite atau Create React App  

**Justification:**
- React.js: Popular, well-documented, strong community support
- Material-UI: Professional appearance, responsive design
- Redux: Predictable state management untuk complex applications

### 3.2 Backend Technology Stack

**Primary Option: Node.js Stack**
- **Runtime:** Node.js 18.x LTS
- **Framework:** Express.js 4.x
- **ORM:** Sequelize atau Prisma
- **Authentication:** JWT dengan bcrypt
- **Validation:** Joi atau express-validator
- **Documentation:** Swagger/OpenAPI

**Alternative Option: Laravel Stack**
- **Framework:** Laravel 10.x
- **Database:** Eloquent ORM
- **Authentication:** Laravel Sanctum
- **API:** Laravel API Resources
- **Documentation:** Laravel API Documentation

### 3.3 Database Technology

**Primary Database:** PostgreSQL 15.x  
**Cache Layer:** Redis (optional)  
**File Storage:** Cloud storage (AWS S3 atau Google Cloud Storage)  

**Justification:**
- PostgreSQL: ACID compliance, excellent performance, JSON support
- Redis: Fast caching untuk frequently accessed data
- Cloud storage: Scalable file storage solution

### 3.4 DevOps & Deployment

**Version Control:** Git dengan GitHub  
**CI/CD:** GitHub Actions atau GitLab CI  
**Containerization:** Docker  
**Cloud Platform:** Railway, Heroku, atau Vercel  
**Monitoring:** Basic logging dengan Morgan  

---

## 4. DATABASE DESIGN

### 4.1 Conceptual Data Model

**Core Entities:**
- **Customer:** Individual atau corporate customers
- **Product:** Acrylic products dalam catalog
- **Order:** Customer orders dengan line items
- **Inventory:** Stock levels dan material tracking
- **WorkOrder:** Production work orders
- **User:** System users dengan roles
- **Communication:** Customer interaction tracking

### 4.2 Logical Data Model

#### 4.2.1 Customer Management Domain
```
Customer (1) ──── (M) Communication
Customer (1) ──── (M) Order
Customer (1) ──── (M) Opportunity
```

#### 4.2.2 Inventory Management Domain
```
Product (1) ──── (M) InventoryItem
Supplier (1) ──── (M) PurchaseOrder
PurchaseOrder (1) ──── (M) PurchaseOrderLine
```

#### 4.2.3 Production Planning Domain
```
Order (1) ──── (M) WorkOrder
Product (1) ──── (1) BillOfMaterial
WorkOrder (1) ──── (M) WorkOrderOperation
```

### 4.3 Physical Database Schema

#### 4.3.1 Core Tables

**Users Table**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL, -- admin, manager, user
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Customers Table**
```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    customer_code VARCHAR(20) UNIQUE NOT NULL,
    customer_type VARCHAR(10) NOT NULL, -- B2C, B2B
    company_name VARCHAR(100),
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    postal_code VARCHAR(10),
    status VARCHAR(20) DEFAULT 'active',
    credit_limit DECIMAL(15,2) DEFAULT 0,
    created_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Products Table**
```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_code VARCHAR(20) UNIQUE NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    unit_of_measure VARCHAR(10) NOT NULL,
    standard_cost DECIMAL(12,2) DEFAULT 0,
    selling_price DECIMAL(12,2) DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Orders Table**
```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_number VARCHAR(20) UNIQUE NOT NULL,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    order_date DATE NOT NULL,
    required_date DATE,
    promised_date DATE,
    status VARCHAR(20) DEFAULT 'pending',
    subtotal DECIMAL(15,2) DEFAULT 0,
    tax_amount DECIMAL(15,2) DEFAULT 0,
    total_amount DECIMAL(15,2) DEFAULT 0,
    notes TEXT,
    created_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Order Lines Table**
```sql
CREATE TABLE order_lines (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity DECIMAL(10,2) NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL,
    line_total DECIMAL(15,2) NOT NULL,
    custom_specifications TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 4.3.2 Inventory Tables

**Inventory Items Table**
```sql
CREATE TABLE inventory_items (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id),
    location_code VARCHAR(20) DEFAULT 'MAIN',
    quantity_on_hand DECIMAL(10,2) DEFAULT 0,
    quantity_allocated DECIMAL(10,2) DEFAULT 0,
    quantity_available DECIMAL(10,2) GENERATED ALWAYS AS 
        (quantity_on_hand - quantity_allocated) STORED,
    reorder_point DECIMAL(10,2) DEFAULT 0,
    max_stock_level DECIMAL(10,2) DEFAULT 0,
    last_count_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Inventory Movements Table**
```sql
CREATE TABLE inventory_movements (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id),
    movement_type VARCHAR(20) NOT NULL, -- receipt, issue, adjustment
    reference_type VARCHAR(20), -- PO, WO, ADJ
    reference_number VARCHAR(20),
    quantity DECIMAL(10,2) NOT NULL,
    unit_cost DECIMAL(12,2),
    movement_date DATE NOT NULL,
    notes TEXT,
    created_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 4.3.3 Production Tables

**Work Orders Table**
```sql
CREATE TABLE work_orders (
    id SERIAL PRIMARY KEY,
    work_order_number VARCHAR(20) UNIQUE NOT NULL,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity_ordered DECIMAL(10,2) NOT NULL,
    quantity_completed DECIMAL(10,2) DEFAULT 0,
    start_date DATE,
    due_date DATE,
    completion_date DATE,
    status VARCHAR(20) DEFAULT 'pending',
    priority VARCHAR(10) DEFAULT 'medium',
    notes TEXT,
    created_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Communications Table**
```sql
CREATE TABLE communications (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    communication_type VARCHAR(20) NOT NULL, -- email, phone, meeting
    direction VARCHAR(10) NOT NULL, -- inbound, outbound
    subject VARCHAR(200),
    content TEXT,
    communication_date TIMESTAMP NOT NULL,
    follow_up_required BOOLEAN DEFAULT false,
    follow_up_date DATE,
    created_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4.4 Database Indexes

**Performance Indexes:**
```sql
-- Customer searches
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_customers_phone ON customers(phone);
CREATE INDEX idx_customers_company ON customers(company_name);

-- Order searches
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_orders_status ON orders(status);

-- Inventory lookups
CREATE INDEX idx_inventory_product ON inventory_items(product_id);
CREATE INDEX idx_movements_product ON inventory_movements(product_id);
CREATE INDEX idx_movements_date ON inventory_movements(movement_date);

-- Work order tracking
CREATE INDEX idx_workorders_status ON work_orders(status);
CREATE INDEX idx_workorders_product ON work_orders(product_id);
```

---

## 5. MODULE DESIGN

### 5.1 CRM Module Design

#### 5.1.1 CRM Architecture
```
CRM Module
├── Customer Management
│   ├── Customer CRUD operations
│   ├── Customer search & filtering
│   └── Customer categorization
├── Communication Tracking
│   ├── Interaction logging
│   ├── Follow-up management
│   └── Communication history
├── Opportunity Management
│   ├── Lead tracking
│   ├── Pipeline management
│   └── Conversion analytics
└── Customer Service
    ├── Issue tracking
    ├── Resolution management
    └── Satisfaction measurement
```

#### 5.1.2 CRM API Endpoints
```
GET    /api/crm/customers              # List customers
POST   /api/crm/customers              # Create customer
GET    /api/crm/customers/:id          # Get customer details
PUT    /api/crm/customers/:id          # Update customer
DELETE /api/crm/customers/:id          # Delete customer

GET    /api/crm/communications         # List communications
POST   /api/crm/communications         # Create communication
GET    /api/crm/communications/:id     # Get communication details

GET    /api/crm/opportunities          # List opportunities
POST   /api/crm/opportunities          # Create opportunity
PUT    /api/crm/opportunities/:id      # Update opportunity
```

#### 5.1.3 CRM Components
**React Components:**
- CustomerList: Display customer list dengan search/filter
- CustomerForm: Create/edit customer information
- CustomerDetail: Show detailed customer information
- CommunicationTracker: Log dan view communications
- OpportunityPipeline: Visual pipeline management
- CustomerDashboard: Customer metrics dan analytics

### 5.2 Inventory Module Design

#### 5.2.1 Inventory Architecture
```
Inventory Module
├── Stock Management
│   ├── Real-time inventory tracking
│   ├── Multi-location support
│   └── Stock level monitoring
├── Purchase Management
│   ├── Supplier management
│   ├── Purchase order processing
│   └── Goods receipt processing
├── Cost Management
│   ├── Cost tracking
│   ├── Valuation methods
│   └── Profitability analysis
└── Reporting
    ├── Stock reports
    ├── Movement reports
    └── Reorder reports
```

#### 5.2.2 Inventory API Endpoints
```
GET    /api/inventory/items            # List inventory items
POST   /api/inventory/items            # Create inventory item
PUT    /api/inventory/items/:id        # Update inventory item

GET    /api/inventory/movements        # List movements
POST   /api/inventory/movements        # Create movement
GET    /api/inventory/movements/:id    # Get movement details

GET    /api/inventory/reorder          # Get reorder recommendations
POST   /api/inventory/purchase-orders  # Create purchase order
```

### 5.3 Production Module Design

#### 5.3.1 Production Architecture
```
Production Module
├── Work Order Management
│   ├── Work order creation
│   ├── Scheduling optimization
│   └── Progress tracking
├── Resource Planning
│   ├── Capacity management
│   ├── Resource allocation
│   └── Workload balancing
├── Quality Control
│   ├── Inspection points
│   ├── Defect tracking
│   └── Quality metrics
└── Shop Floor Control
    ├── Operation tracking
    ├── Time recording
    └── Status updates
```

#### 5.3.2 Production API Endpoints
```
GET    /api/production/work-orders     # List work orders
POST   /api/production/work-orders     # Create work order
PUT    /api/production/work-orders/:id # Update work order

GET    /api/production/schedule        # Get production schedule
POST   /api/production/schedule        # Update schedule

GET    /api/production/resources       # List resources
GET    /api/production/capacity        # Get capacity information
```

### 5.4 Analytics Module Design

#### 5.4.1 Analytics Architecture
```
Analytics Module
├── Dashboard Management
│   ├── Real-time dashboards
│   ├── Customizable widgets
│   └── Role-based views
├── Reporting Engine
│   ├── Standard reports
│   ├── Custom reports
│   └── Scheduled reports
├── Data Visualization
│   ├── Charts dan graphs
│   ├── KPI displays
│   └── Trend analysis
└── Business Intelligence
    ├── Predictive analytics
    ├── Performance metrics
    └── Executive summaries
```

---

## 6. API SPECIFICATIONS

### 6.1 API Design Principles

**RESTful Design:** Following REST architectural constraints  
**Consistent Naming:** Plural nouns untuk resource names  
**HTTP Methods:** GET, POST, PUT, DELETE untuk CRUD operations  
**Status Codes:** Appropriate HTTP status codes  
**JSON Format:** Request dan response dalam JSON format  
**Error Handling:** Consistent error response structure  

### 6.2 API Standards

#### 6.2.1 Request/Response Format
**Standard Response Format:**
```json
{
  "success": true,
  "data": {},
  "message": "Operation successful",
  "timestamp": "2025-10-05T10:30:00Z"
}
```

**Error Response Format:**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Email is required"
      }
    ]
  },
  "timestamp": "2025-10-05T10:30:00Z"
}
```

#### 6.2.2 Pagination
```json
{
  "data": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": false
  }
}
```

### 6.3 Authentication API

#### 6.3.1 Login
```
POST /api/auth/login
Content-Type: application/json

{
  "username": "user@example.com",
  "password": "password123"
}

Response:
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "refreshToken": "refresh_token_here",
    "user": {
      "id": 1,
      "username": "user@example.com",
      "role": "manager"
    }
  }
}
```

#### 6.3.2 Logout
```
POST /api/auth/logout
Authorization: Bearer {token}

Response:
{
  "success": true,
  "message": "Logged out successfully"
}
```

### 6.4 CRM API Examples

#### 6.4.1 Get Customers
```
GET /api/crm/customers?page=1&limit=10&search=john
Authorization: Bearer {token}

Response:
{
  "success": true,
  "data": [
    {
      "id": 1,
      "customerCode": "CUST001",
      "customerType": "B2C",
      "companyName": null,
      "contactPerson": "John Doe",
      "email": "john@example.com",
      "phone": "+6281234567890",
      "status": "active",
      "createdAt": "2025-10-01T10:00:00Z"
    }
  ],
  "pagination": {...}
}
```

#### 6.4.2 Create Customer
```
POST /api/crm/customers
Authorization: Bearer {token}
Content-Type: application/json

{
  "customerType": "B2C",
  "contactPerson": "Jane Smith",
  "email": "jane@example.com",
  "phone": "+6281234567891",
  "address": "Jl. Sudirman No. 123",
  "city": "Jakarta"
}

Response:
{
  "success": true,
  "data": {
    "id": 2,
    "customerCode": "CUST002",
    "customerType": "B2C",
    "contactPerson": "Jane Smith",
    "email": "jane@example.com"
  },
  "message": "Customer created successfully"
}
```

---

## 7. SECURITY DESIGN

### 7.1 Authentication & Authorization

#### 7.1.1 Authentication Strategy
**JWT Token-based Authentication:**
- Access tokens dengan 24-hour expiry
- Refresh tokens untuk token renewal
- Secure token storage dalam httpOnly cookies
- Token blacklist untuk logout functionality

#### 7.1.2 Role-Based Access Control (RBAC)
```
Roles Hierarchy:
├── Super Admin
│   └── Full system access
├── Manager
│   ├── Read/Write access to all modules
│   └── User management capabilities
├── Supervisor
│   ├── Read/Write access to operational modules
│   └── Limited user management
└── User
    ├── Read/Write access to assigned modules
    └── No administrative capabilities
```

#### 7.1.3 Permission Matrix
| Module | Super Admin | Manager | Supervisor | User |
|--------|-------------|---------|------------|------|
| User Management | CRUD | CRUD | Read | Read |
| Customer Management | CRUD | CRUD | CRUD | CRUD |
| Inventory Management | CRUD | CRUD | CRUD | Read |
| Production Management | CRUD | CRUD | CRUD | Read |
| Analytics | CRUD | CRUD | Read | Read |

### 7.2 Data Security

#### 7.2.1 Data Encryption
**At Rest:**
- Database encryption untuk sensitive fields
- File encryption untuk uploaded documents
- Backup encryption dengan AES-256

**In Transit:**
- HTTPS/TLS 1.3 untuk all communications
- API payload encryption untuk sensitive data
- Secure websocket connections

#### 7.2.2 Data Privacy
**Personal Data Protection:**
- PII field identification dan protection
- Data masking untuk non-privileged users
- Audit trail untuk data access
- Data retention policies implementation

### 7.3 Security Measures

#### 7.3.1 Input Validation
```javascript
// Example validation middleware
const validateCustomer = [
  body('email').isEmail().normalizeEmail(),
  body('phone').matches(/^\+?[1-9]\d{1,14}$/),
  body('customerType').isIn(['B2C', 'B2B']),
  (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({
        success: false,
        error: {
          code: 'VALIDATION_ERROR',
          details: errors.array()
        }
      });
    }
    next();
  }
];
```

#### 7.3.2 Security Headers
```javascript
// Security middleware
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"]
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true
  }
}));
```

### 7.4 Audit & Logging

#### 7.4.1 Audit Trail
```sql
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INTEGER,
    old_values JSONB,
    new_values JSONB,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 7.4.2 Security Monitoring
- Failed login attempt tracking
- Unusual access pattern detection
- Data modification monitoring
- Session management logging

---

## 8. PERFORMANCE DESIGN

### 8.1 Performance Requirements

**Response Time Targets:**
- Page load: <3 seconds
- API calls: <1 second
- Database queries: <500ms
- Report generation: <10 seconds

**Throughput Targets:**
- 10 concurrent users
- 1000 transactions/hour
- 100 API calls/minute per user

### 8.2 Database Performance

#### 8.2.1 Query Optimization
```sql
-- Optimized customer search query
SELECT c.*, 
       COUNT(o.id) as order_count,
       MAX(o.order_date) as last_order_date
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE c.status = 'active'
  AND (c.contact_person ILIKE $1 OR c.email ILIKE $1)
GROUP BY c.id
ORDER BY c.created_at DESC
LIMIT $2 OFFSET $3;
```

#### 8.2.2 Indexing Strategy
```sql
-- Composite indexes untuk common queries
CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date DESC);
CREATE INDEX idx_inventory_product_location ON inventory_items(product_id, location_code);
CREATE INDEX idx_communications_customer_date ON communications(customer_id, communication_date DESC);
```

### 8.3 Caching Strategy

#### 8.3.1 Application-Level Caching
```javascript
// Redis caching untuk frequently accessed data
const getCustomerById = async (customerId) => {
  const cacheKey = `customer:${customerId}`;
  let customer = await redis.get(cacheKey);
  
  if (!customer) {
    customer = await Customer.findById(customerId);
    await redis.setex(cacheKey, 3600, JSON.stringify(customer));
  } else {
    customer = JSON.parse(customer);
  }
  
  return customer;
};
```

#### 8.3.2 Database Query Caching
- Result set caching untuk dashboard queries
- Prepared statement caching
- Connection pooling optimization

### 8.4 Frontend Performance

#### 8.4.1 Code Splitting
```javascript
// Lazy loading untuk modules
const CRMModule = lazy(() => import('./modules/CRM'));
const InventoryModule = lazy(() => import('./modules/Inventory'));
const ProductionModule = lazy(() => import('./modules/Production'));
const AnalyticsModule = lazy(() => import('./modules/Analytics'));
```

#### 8.4.2 Asset Optimization
- Image compression dan lazy loading
- CSS/JS minification
- Bundle size optimization
- CDN integration untuk static assets

---

## 9. INTEGRATION DESIGN

### 9.1 Internal Module Integration

#### 9.1.1 Event-Driven Architecture
```javascript
// Event publisher
class EventBus {
  constructor() {
    this.events = {};
  }
  
  emit(eventName, data) {
    if (this.events[eventName]) {
      this.events[eventName].forEach(callback => callback(data));
    }
  }
  
  on(eventName, callback) {
    if (!this.events[eventName]) {
      this.events[eventName] = [];
    }
    this.events[eventName].push(callback);
  }
}

// Example: Order creation triggers inventory allocation
eventBus.emit('order.created', { orderId: 123, items: [...] });
```

#### 9.1.2 Module Communication
```
Order Module → Inventory Module: Stock allocation
Order Module → Production Module: Work order creation
Production Module → Inventory Module: Material consumption
CRM Module → Order Module: Customer information
Analytics Module → All Modules: Data aggregation
```

### 9.2 External System Integration

#### 9.2.1 Email Integration
```javascript
// Email service integration
const sendEmail = async (to, subject, template, data) => {
  const emailContent = await renderTemplate(template, data);
  
  return await emailProvider.send({
    to,
    subject,
    html: emailContent,
    from: 'noreply@satriamart.com'
  });
};
```

#### 9.2.2 WhatsApp Integration (Future)
```javascript
// WhatsApp API integration placeholder
const sendWhatsAppMessage = async (phoneNumber, message) => {
  // Integration dengan WhatsApp Business API
  return await whatsappAPI.sendMessage({
    to: phoneNumber,
    message: message
  });
};
```

### 9.3 Data Synchronization

#### 9.3.1 Real-time Updates
```javascript
// WebSocket untuk real-time updates
io.on('connection', (socket) => {
  socket.on('join-room', (room) => {
    socket.join(room);
  });
  
  // Broadcast inventory updates
  socket.on('inventory-update', (data) => {
    socket.to('inventory-room').emit('inventory-updated', data);
  });
});
```

#### 9.3.2 Data Consistency
- Transaction management across modules
- Eventual consistency untuk non-critical updates
- Conflict resolution strategies
- Data validation at integration points

---

## 10. DEPLOYMENT ARCHITECTURE

### 10.1 Development Environment

#### 10.1.1 Local Development Setup
```
Development Stack:
├── Frontend: React development server (localhost:3000)
├── Backend: Node.js server (localhost:5000)
├── Database: PostgreSQL (localhost:5432)
├── Cache: Redis (localhost:6379)
└── File Storage: Local filesystem
```

#### 10.1.2 Development Tools
```
package.json scripts:
├── npm run dev          # Start development servers
├── npm run build        # Build untuk production
├── npm run test         # Run test suites
├── npm run lint         # Code linting
└── npm run migrate      # Database migrations
```

### 10.2 Staging Environment

#### 10.2.1 Staging Configuration
```
Staging Environment:
├── Frontend: Static hosting (Netlify/Vercel)
├── Backend: Cloud hosting (Railway/Heroku)
├── Database: Cloud PostgreSQL
├── File Storage: Cloud storage
└── Monitoring: Basic logging
```

### 10.3 Production Architecture (Simulated)

#### 10.3.1 Production Deployment
```
Production Stack:
├── Load Balancer (Cloud provider)
├── Application Servers (2+ instances)
├── Database Cluster (Primary + Replica)
├── Redis Cluster
├── File Storage (CDN-enabled)
└── Monitoring & Logging
```

#### 10.3.2 Deployment Process
```
CI/CD Pipeline:
1. Code commit to repository
2. Automated testing execution
3. Build dan artifact creation
4. Staging deployment
5. Integration testing
6. Production deployment approval
7. Blue-green deployment
8. Health checks dan monitoring
```

### 10.4 Infrastructure as Code

#### 10.4.1 Docker Configuration
```dockerfile
# Dockerfile untuk backend
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 5000
CMD ["npm", "start"]
```

#### 10.4.2 Docker Compose
```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/sims
    depends_on:
      - db
      - redis
  
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=sims
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:alpine
    
volumes:
  postgres_data:
```

---

## APPENDICES

### Appendix A: API Documentation Template

**Swagger/OpenAPI Configuration:**
```yaml
openapi: 3.0.0
info:
  title: SATRIAMART SIMS API
  version: 1.0.0
  description: Integrated Management System API
paths:
  /api/crm/customers:
    get:
      summary: List customers
      parameters:
        - name: page
          in: query
          schema:
            type: integer
      responses:
        200:
          description: Successful response
```

### Appendix B: Database Migration Scripts

**Initial Migration:**
```sql
-- 001_create_users_table.sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Appendix C: Testing Strategy

**Unit Testing:**
- Controller testing dengan Jest/Mocha
- Service layer testing
- Database model testing
- API endpoint testing

**Integration Testing:**
- Module integration testing
- Database integration testing
- API integration testing
- End-to-end user scenarios

---

**Document Control:**
- **Version:** 1.0
- **Created:** Oktober 2025
- **Author:** Technical Lead
- **Reviewed:** Project Manager, Business Analyst
- **Approved:** Academic Supervisor

**Change History:**
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Oct 2025 | Technical Lead | Initial system design |

**Approval:**
- **Technical Lead:** [Signature] _________________ Date: _______
- **Project Manager:** [Signature] _________________ Date: _______
- **Academic Supervisor:** [Signature] _________________ Date: _______
