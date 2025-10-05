# BUSINESS REQUIREMENTS DOCUMENT (BRD)
## SATRIAMART INTEGRATED MANAGEMENT SYSTEM (SIMS)

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Semester 7**

---

**Mata Kuliah:** Proyek Sistem Informasi II  
**Dosen Pengampu:** Rani Irma Handayani, M.Kom  
**Business Analyst:** [Nama Mahasiswa 2]  
**Tanggal:** Oktober 2025  
**Versi:** 1.0

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Project Overview](#2-project-overview)
3. [Current State Analysis](#3-current-state-analysis)
4. [Business Requirements](#4-business-requirements)
5. [Functional Requirements](#5-functional-requirements)
6. [Non-Functional Requirements](#6-non-functional-requirements)
7. [Use Cases](#7-use-cases)
8. [Business Rules](#8-business-rules)
9. [Assumptions & Constraints](#9-assumptions--constraints)
10. [Success Criteria](#10-success-criteria)

---

## 1. EXECUTIVE SUMMARY

### 1.1 Document Purpose
Document ini menjabarkan business requirements untuk pengembangan SATRIAMART Integrated Management System (SIMS), sebuah sistem informasi terintegrasi yang akan mentransformasi operasional SATRIAMART dari manual processes menjadi digitally-enabled smart operations.

### 1.2 Business Need
SATRIAMART memerlukan sistem terintegrasi untuk:
- **Meningkatkan Operational Efficiency**: Otomatisasi proses manual yang time-consuming
- **Enhance Customer Experience**: Real-time visibility dan communication
- **Enable Data-Driven Decisions**: Comprehensive analytics dan reporting
- **Support Business Growth**: Scalable system untuk future expansion

### 1.3 Proposed Solution
SIMS akan mengintegrasikan 4 core modules:
1. **Customer Relationship Management (CRM)**
2. **Inventory Management System**
3. **Production Planning System**
4. **Sales & Analytics Dashboard**

### 1.4 Expected Benefits
- 60% reduction dalam order processing time
- 40% improvement dalam production efficiency
- 35% increase dalam customer satisfaction
- 25% reduction dalam operational costs

---

## 2. PROJECT OVERVIEW

### 2.1 Background
SATRIAMART adalah perusahaan manufaktur yang specializes dalam dekorasi dan aksesoris akrilik dengan:
- **Business Model**: B2C (70%) dan B2B (30%)
- **Product Portfolio**: Nomor rumah, signage, papan nama, custom accessories
- **Annual Revenue**: Rp 2.5 miliar dengan growth target 50%
- **Customer Base**: 500+ active customers dengan 80+ new customers monthly

### 2.2 Business Challenge
**Current Pain Points:**
1. **Manual Process Dominance**: 80% operations masih manual
2. **Data Fragmentation**: Information scattered across WhatsApp, email, spreadsheets
3. **Limited Visibility**: No real-time tracking untuk orders atau inventory
4. **Customer Experience Issues**: Slow response time (4-8 hours average)
5. **Decision Making**: Reactive decisions due to lack of data analytics

### 2.3 Business Opportunity
- **Market Growth**: Acrylic products market growing 25-30% annually
- **Digital Transformation**: First-mover advantage dalam industry
- **Customer Demand**: Increasing expectation untuk digital experience
- **Operational Scaling**: Foundation untuk business expansion

---

## 3. CURRENT STATE ANALYSIS

### 3.1 Current Business Processes

#### 3.1.1 Customer-to-Cash Process
```
Customer Inquiry (WhatsApp/Email) → Manual Response (4-8 hours) → 
Quotation Creation (2-3 days) → Negotiation (Multiple rounds) → 
Order Confirmation → Manual Order Processing → Production → 
Delivery → Payment Collection → Customer Feedback (Ad-hoc)
```

**Issues:**
- No systematic inquiry tracking
- Manual quotation prone to errors
- Limited order visibility untuk customers
- Inconsistent follow-up processes

#### 3.1.2 Inventory Management Process
```
Weekly Manual Stock Count → Spreadsheet Updates → 
Reactive Reordering → Supplier Communication (Phone/Email) → 
Manual Delivery Tracking → Stock Receiving → Manual Update
```

**Issues:**
- No real-time inventory visibility
- Frequent stockouts dan overstocking
- Manual reconciliation errors
- Limited supplier performance tracking

#### 3.1.3 Production Planning Process
```
Order Review → Manual Scheduling → Resource Allocation (Ad-hoc) → 
Work Order Creation (Paper-based) → Production Execution → 
Quality Check (Manual) → Completion Update
```

**Issues:**
- No systematic capacity planning
- Resource conflicts dan bottlenecks
- Limited production visibility
- Inconsistent quality control

### 3.2 Current System Landscape
- **Communication**: WhatsApp Business, Email
- **Documentation**: Microsoft Excel, Google Sheets
- **Financial**: Basic accounting software
- **No Integration**: Systems operate in silos

### 3.3 Stakeholder Analysis

| **Stakeholder** | **Current Role** | **Pain Points** | **Expectations** |
|-----------------|------------------|----------------|------------------|
| **Owner/CEO** | Strategic decisions | Limited visibility untuk business performance | Real-time dashboard, analytics |
| **Sales Manager** | Customer management | Manual tracking, slow response | CRM system, automation |
| **Production Manager** | Production planning | No systematic scheduling | Production planning tools |
| **Inventory Staff** | Stock management | Manual processes, errors | Automated inventory system |
| **Customers** | Order placement | Limited visibility, slow response | Real-time tracking, faster service |

---

## 4. BUSINESS REQUIREMENTS

### 4.1 High-Level Business Requirements

#### BR001: Customer Relationship Management
**Requirement:** System must provide comprehensive customer relationship management capabilities
**Business Value:** Improve customer satisfaction dan retention
**Priority:** High
**Rationale:** Customer adalah core asset, need centralized management

#### BR002: Inventory Optimization
**Requirement:** System must enable efficient inventory management dengan real-time visibility
**Business Value:** Reduce inventory costs dan improve availability
**Priority:** High
**Rationale:** Inventory represents significant investment, optimization critical

#### BR003: Production Efficiency
**Requirement:** System must support efficient production planning dan execution
**Business Value:** Increase throughput dan reduce waste
**Priority:** High
**Rationale:** Production efficiency directly impacts profitability

#### BR004: Business Intelligence
**Requirement:** System must provide comprehensive analytics dan reporting capabilities
**Business Value:** Enable data-driven decision making
**Priority:** Medium
**Rationale:** Strategic advantage through insights

#### BR005: Integration & Automation
**Requirement:** System must integrate all modules dan automate manual processes
**Business Value:** Reduce errors dan improve efficiency
**Priority:** High
**Rationale:** Integration eliminates silos, automation reduces costs

### 4.2 Detailed Business Requirements

#### 4.2.1 Customer Management Requirements

**BR001.1: Customer Registration & Profiling**
- System must capture comprehensive customer information
- Support both B2C dan B2B customer types
- Maintain customer history dan preferences
- Enable customer segmentation

**BR001.2: Communication Management**
- Track all customer interactions across channels
- Automated follow-up reminders
- Communication templates untuk consistency
- Response time tracking

**BR001.3: Sales Opportunity Management**
- Track sales opportunities from lead to close
- Quotation generation dan management
- Sales pipeline visibility
- Conversion analytics

#### 4.2.2 Inventory Management Requirements

**BR002.1: Real-time Inventory Tracking**
- Real-time stock levels visibility
- Support untuk multiple locations
- Batch/lot tracking untuk raw materials
- Integration dengan barcode/QR systems

**BR002.2: Automated Reordering**
- Configurable reorder points
- Automatic purchase order generation
- Supplier management dan performance tracking
- Lead time optimization

**BR002.3: Cost Management**
- Material cost tracking
- FIFO/LIFO costing methods
- Waste tracking dan analysis
- Profitability analysis by product

#### 4.2.3 Production Planning Requirements

**BR003.1: Work Order Management**
- Work order creation dari sales orders
- Resource requirements calculation
- Production scheduling optimization
- Progress tracking

**BR003.2: Capacity Planning**
- Resource availability visibility
- Capacity vs demand analysis
- Bottleneck identification
- Load balancing

**BR003.3: Quality Management**
- Quality checkpoints definition
- Defect tracking dan analysis
- Corrective action management
- Quality metrics reporting

#### 4.2.4 Analytics & Reporting Requirements

**BR004.1: Sales Analytics**
- Sales performance tracking
- Customer analytics
- Product performance analysis
- Revenue forecasting

**BR004.2: Operational Analytics**
- Production efficiency metrics
- Inventory turnover analysis
- Cost analysis
- Performance benchmarking

**BR004.3: Executive Dashboard**
- Real-time KPI dashboard
- Trend analysis
- Exception reporting
- Mobile accessibility

---

## 5. FUNCTIONAL REQUIREMENTS

### 5.1 CRM Module Functional Requirements

#### FR-CRM-001: Customer Management
**Description:** System must provide comprehensive customer management functionality
**Acceptance Criteria:**
- Create, read, update, delete customer records
- Support both individual dan corporate customers
- Maintain customer contact information, preferences, dan history
- Customer search dan filtering capabilities
- Customer status management (active, inactive, prospect)

#### FR-CRM-002: Communication Tracking
**Description:** System must track all customer communications
**Acceptance Criteria:**
- Record incoming communications (email, phone, WhatsApp)
- Track outgoing communications dengan timestamps
- Maintain communication history dengan searchable archive
- Automated communication workflows
- Communication templates management

#### FR-CRM-003: Sales Opportunity Management
**Description:** System must manage sales opportunities throughout the pipeline
**Acceptance Criteria:**
- Create opportunities dari customer inquiries
- Track opportunity stages (lead, qualified, proposal, negotiation, closed)
- Generate dan manage quotations
- Probability dan value tracking
- Win/loss analysis

#### FR-CRM-004: Customer Service Management
**Description:** System must support customer service activities
**Acceptance Criteria:**
- Ticket creation untuk customer issues
- Issue categorization dan prioritization
- Resolution tracking dengan SLA monitoring
- Customer satisfaction measurement
- Knowledge base integration

### 5.2 Inventory Module Functional Requirements

#### FR-INV-001: Inventory Tracking
**Description:** System must provide real-time inventory tracking
**Acceptance Criteria:**
- Real-time stock level monitoring
- Support untuk multiple inventory locations
- Barcode/QR code integration
- Batch/serial number tracking
- Movement history tracking

#### FR-INV-002: Purchase Management
**Description:** System must support purchase order management
**Acceptance Criteria:**
- Automatic reorder point monitoring
- Purchase order generation dan approval
- Supplier management dengan performance tracking
- Goods receipt processing
- Invoice matching dan approval

#### FR-INV-003: Cost Management
**Description:** System must track inventory costs accurately
**Acceptance Criteria:**
- Standard cost maintenance
- Actual cost capture
- FIFO/LIFO costing methods
- Cost variance analysis
- Profitability calculation by product

### 5.3 Production Module Functional Requirements

#### FR-PROD-001: Work Order Management
**Description:** System must manage production work orders
**Acceptance Criteria:**
- Work order creation dari sales orders
- Bill of materials management
- Resource requirements calculation
- Work order scheduling
- Progress tracking dan reporting

#### FR-PROD-002: Resource Planning
**Description:** System must support resource planning dan allocation
**Acceptance Criteria:**
- Resource capacity management
- Skill-based resource allocation
- Equipment scheduling
- Workload balancing
- Conflict resolution

#### FR-PROD-003: Quality Control
**Description:** System must support quality control processes
**Acceptance Criteria:**
- Quality checkpoint definition
- Inspection result recording
- Defect tracking dan classification
- Corrective action management
- Quality metrics calculation

### 5.4 Analytics Module Functional Requirements

#### FR-ANAL-001: Dashboard Management
**Description:** System must provide configurable dashboards
**Acceptance Criteria:**
- Role-based dashboard views
- Real-time data visualization
- Customizable widgets dan layouts
- Drill-down capabilities
- Export functionality

#### FR-ANAL-002: Reporting System
**Description:** System must provide comprehensive reporting capabilities
**Acceptance Criteria:**
- Standard report library
- Custom report creation
- Scheduled report generation
- Report sharing dan distribution
- Report version control

#### FR-ANAL-003: Data Analytics
**Description:** System must provide advanced analytics capabilities
**Acceptance Criteria:**
- Trend analysis
- Predictive analytics
- Statistical analysis
- Comparative analysis
- What-if scenarios

---

## 6. NON-FUNCTIONAL REQUIREMENTS

### 6.1 Performance Requirements

#### NFR-PERF-001: Response Time
- **Standard Operations**: <3 seconds response time
- **Report Generation**: <30 seconds untuk standard reports
- **Dashboard Refresh**: <5 seconds untuk real-time data
- **File Upload**: Support files up to 10MB

#### NFR-PERF-002: Throughput
- **Concurrent Users**: Support minimum 10 concurrent users
- **Transaction Volume**: Handle 1000 transactions per hour
- **Data Volume**: Support 10GB database growth annually
- **Backup/Restore**: Complete backup in <2 hours

#### NFR-PERF-003: Scalability
- **User Scalability**: Scale to 50 users within 2 years
- **Data Scalability**: Handle 5x current data volume
- **Feature Scalability**: Support additional modules
- **Geographic Scalability**: Support multiple locations

### 6.2 Security Requirements

#### NFR-SEC-001: Authentication & Authorization
- **User Authentication**: Secure login dengan password policies
- **Role-based Access**: Configurable permissions by role
- **Session Management**: Automatic timeout after inactivity
- **Audit Trail**: Complete user activity logging

#### NFR-SEC-002: Data Protection
- **Data Encryption**: Sensitive data encrypted at rest dan in transit
- **Backup Security**: Encrypted backup dengan secure storage
- **Data Privacy**: PII protection compliance
- **Access Control**: Field-level security waar applicable

### 6.3 Usability Requirements

#### NFR-USA-001: User Experience
- **Intuitive Interface**: Minimal training required
- **Responsive Design**: Works on desktop, tablet, mobile
- **Accessibility**: WCAG 2.1 compliance
- **Multilingual**: Indonesian dan English support

#### NFR-USA-002: Help & Support
- **Context-sensitive Help**: Inline help dan tooltips
- **User Documentation**: Comprehensive user guides
- **Training Materials**: Video tutorials dan training guides
- **Error Messages**: Clear, actionable error messages

### 6.4 Reliability Requirements

#### NFR-REL-001: Availability
- **System Uptime**: 99.5% availability during business hours
- **Planned Maintenance**: <4 hours monthly downtime
- **Disaster Recovery**: RTO of 4 hours, RPO of 1 hour
- **Error Handling**: Graceful degradation during partial failures

#### NFR-REL-002: Data Integrity
- **Data Accuracy**: 99.9% data accuracy maintained
- **Referential Integrity**: Database constraints enforced
- **Transaction Integrity**: ACID compliance
- **Data Backup**: Daily automated backups dengan 30-day retention

---

## 7. USE CASES

### 7.1 CRM Use Cases

#### UC-CRM-001: Manage Customer Information
**Primary Actor:** Sales Representative  
**Goal:** Maintain accurate customer information  
**Preconditions:** User is authenticated dan has customer management permissions  

**Main Success Scenario:**
1. User navigates to customer management
2. System displays customer list dengan search capabilities
3. User selects customer or creates new customer
4. User enters/updates customer information
5. System validates data dan saves changes
6. System confirms successful update

**Alternative Flows:**
- 3a. User creates new customer
- 4a. Data validation fails - system shows error messages
- 5a. Save operation fails - system shows error dan allows retry

#### UC-CRM-002: Track Customer Communication
**Primary Actor:** Sales Representative  
**Goal:** Record dan track customer communications  
**Preconditions:** Customer exists in system  

**Main Success Scenario:**
1. User selects customer record
2. User clicks "Add Communication"
3. User enters communication details (type, date, notes)
4. User attaches relevant files if needed
5. System saves communication record
6. System updates customer interaction timeline

#### UC-CRM-003: Manage Sales Opportunities
**Primary Actor:** Sales Manager  
**Goal:** Track sales opportunities through pipeline  
**Preconditions:** Customer dan products exist in system  

**Main Success Scenario:**
1. User creates new opportunity atau selects existing
2. User enters opportunity details (value, probability, expected close date)
3. User associates opportunity dengan customer dan products
4. User updates opportunity stage as it progresses
5. System calculates pipeline metrics
6. System generates alerts for follow-up actions

### 7.2 Inventory Use Cases

#### UC-INV-001: Monitor Inventory Levels
**Primary Actor:** Inventory Manager  
**Goal:** Monitor current inventory levels dan identify reorder needs  
**Preconditions:** User has inventory access permissions  

**Main Success Scenario:**
1. User accesses inventory dashboard
2. System displays current stock levels untuk all items
3. System highlights items below reorder point
4. User reviews inventory reports
5. User identifies items requiring reorder
6. System provides reorder recommendations

#### UC-INV-002: Process Purchase Orders
**Primary Actor:** Purchasing Manager  
**Goal:** Create dan process purchase orders untuk inventory replenishment  
**Preconditions:** Suppliers dan products are configured  

**Main Success Scenario:**
1. User reviews reorder recommendations
2. User creates purchase order untuk selected items
3. User specifies quantities dan preferred suppliers
4. System calculates total cost dan delivery dates
5. User submits purchase order untuk approval
6. System sends PO to supplier upon approval

### 7.3 Production Use Cases

#### UC-PROD-001: Create Work Orders
**Primary Actor:** Production Manager  
**Goal:** Create work orders dari sales orders  
**Preconditions:** Sales order exists dan is approved  

**Main Success Scenario:**
1. User selects approved sales order
2. User clicks "Create Work Order"
3. System generates work order dengan BOMs dan routing
4. User reviews dan adjusts resource requirements
5. User schedules work order based on capacity
6. System creates work order dan updates production schedule

#### UC-PROD-002: Track Production Progress
**Primary Actor:** Production Supervisor  
**Goal:** Monitor dan update production progress  
**Preconditions:** Work orders exist dan production has started  

**Main Success Scenario:**
1. User accesses production dashboard
2. System displays active work orders dengan status
3. User selects work order to update
4. User records progress (quantity completed, time spent)
5. System updates work order status
6. System alerts if behind schedule atau issues detected

---

## 8. BUSINESS RULES

### 8.1 Customer Management Rules

**BR-CRM-001:** Customer registration requires minimum information (name, contact method)  
**BR-CRM-002:** Corporate customers must have designated primary contact  
**BR-CRM-003:** Customer communications must be logged within 24 hours  
**BR-CRM-004:** Opportunities must have estimated value dan probability  
**BR-CRM-005:** Inactive customers (no orders >12 months) require reactivation  

### 8.2 Inventory Management Rules

**BR-INV-001:** Stock levels cannot go negative  
**BR-INV-002:** Reorder points must be set untuk all inventory items  
**BR-INV-003:** Purchase orders >$5000 require manager approval  
**BR-INV-004:** Inventory adjustments require reason codes  
**BR-INV-005:** Material costs must be updated within 24 hours of receipt  

### 8.3 Production Rules

**BR-PROD-001:** Work orders can only be created dari approved sales orders  
**BR-PROD-002:** Production cannot start without material availability confirmation  
**BR-PROD-003:** Quality checkpoints are mandatory untuk all custom products  
**BR-PROD-004:** Work order modifications require supervisor approval  
**BR-PROD-005:** Completed work orders must be closed within 24 hours  

### 8.4 General Business Rules

**BR-GEN-001:** All monetary amounts in Indonesian Rupiah (IDR)  
**BR-GEN-002:** Business hours: Monday-Saturday, 8 AM - 6 PM WIB  
**BR-GEN-003:** System access requires valid user authentication  
**BR-GEN-004:** Data retention period: 7 years untuk financial records  
**BR-GEN-005:** System backups performed daily at 2 AM WIB  

---

## 9. ASSUMPTIONS & CONSTRAINTS

### 9.1 Assumptions

**Technical Assumptions:**
- Reliable internet connectivity available
- Modern web browsers supported (Chrome, Firefox, Safari)
- Basic computer literacy for end users
- Existing email system can be integrated

**Business Assumptions:**
- Management commitment to digital transformation
- User availability untuk training dan testing
- Business processes can be standardized
- Data migration dari existing systems possible

**Project Assumptions:**
- Academic timeline of 12 weeks sufficient
- Team members available 20+ hours per week
- Access to SATRIAMART stakeholders untuk requirements validation
- Development environment resources available

### 9.2 Constraints

**Technical Constraints:**
- Academic project budget limitations
- Development using open-source technologies
- Cloud hosting on free/low-cost tiers
- Limited integration dengan external systems

**Business Constraints:**
- Simulated business environment (not live production)
- Limited real user testing opportunities
- Simplified business processes untuk academic scope
- No actual financial transactions

**Project Constraints:**
- Fixed 12-week timeline
- 3-person team limitation
- Academic evaluation requirements
- Limited mentor availability

---

## 10. SUCCESS CRITERIA

### 10.1 Business Success Criteria

**Customer Satisfaction:**
- Achieve >90% user satisfaction in usability testing
- Demonstrate 50% reduction in customer response time
- Show improved customer data accuracy (95%+)

**Operational Efficiency:**
- Reduce order processing time by 60%
- Improve inventory accuracy to 98%+
- Increase production planning efficiency by 40%

**System Performance:**
- Meet all performance requirements (response time <3 seconds)
- Achieve 99%+ system availability during testing
- Zero critical bugs in final system

### 10.2 Technical Success Criteria

**Functionality:**
- 100% of high-priority requirements implemented
- 90%+ of medium-priority requirements implemented
- All critical use cases successfully demonstrated

**Quality:**
- 95%+ test case pass rate
- Code coverage >80%
- Security requirements fully met

**Documentation:**
- Complete technical documentation
- User manuals created dan validated
- Training materials developed

### 10.3 Academic Success Criteria

**Learning Objectives:**
- Demonstrate project management competency
- Show technical implementation skills
- Document lessons learned dan best practices

**Deliverable Quality:**
- Professional-grade documentation
- Working system prototype
- Successful final presentation

---

## APPENDICES

### Appendix A: Glossary

**BOM:** Bill of Materials - List of raw materials needed untuk production  
**CRM:** Customer Relationship Management  
**FIFO:** First In, First Out - Inventory costing method  
**KPI:** Key Performance Indicator  
**PO:** Purchase Order  
**RPO:** Recovery Point Objective  
**RTO:** Recovery Time Objective  
**SLA:** Service Level Agreement  
**UAT:** User Acceptance Testing  

### Appendix B: Requirements Traceability Matrix

| **Requirement ID** | **Description** | **Priority** | **Source** | **Test Case** |
|-------------------|----------------|-------------|------------|---------------|
| BR001 | Customer Management | High | Stakeholder Interview | TC-CRM-001 |
| BR002 | Inventory Management | High | Current State Analysis | TC-INV-001 |
| BR003 | Production Planning | High | Process Analysis | TC-PROD-001 |
| BR004 | Business Intelligence | Medium | Strategic Need | TC-ANAL-001 |

### Appendix C: Risk Assessment

| **Risk** | **Impact** | **Probability** | **Mitigation** |
|----------|------------|----------------|----------------|
| Requirements Creep | High | Medium | Change control process |
| Technical Complexity | High | Medium | Proof of concept first |
| User Adoption | Medium | Low | User involvement in design |
| Integration Issues | High | Medium | Early integration testing |

---

**Document Control:**
- **Version:** 1.0
- **Created:** Oktober 2025
- **Author:** Business Analyst
- **Reviewed:** Project Manager, Technical Lead
- **Approved:** Academic Supervisor

**Change History:**
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Oct 2025 | Business Analyst | Initial version |

**Approval:**
- **Business Analyst:** [Signature] _________________ Date: _______
- **Project Manager:** [Signature] _________________ Date: _______
- **Academic Supervisor:** [Signature] _________________ Date: _______
