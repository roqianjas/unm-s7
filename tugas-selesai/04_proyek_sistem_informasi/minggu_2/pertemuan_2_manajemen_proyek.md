# MANAJEMEN PROYEK SISTEM INFORMASI
## SATRIAMART Integrated Management System (SIMS)
### Pertemuan 2: Scope, Time, Cost, Quality, Resource Management

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi**  
**Pertemuan 2 - Studi Kasus Manajemen Proyek**

---

## 1. RUANG LINGKUP PROYEK (PROJECT SCOPE)

### 1.1 Project Scope Statement

#### A. Project Objectives
Mengembangkan sistem informasi terintegrasi SATRIAMART SIMS yang menggabungkan Customer Relationship Management (CRM), Inventory Management, Production Planning, dan Sales Analytics dalam satu platform web-based yang modern dan scalable.

#### B. Project Deliverables

##### Major Deliverables
1. **Project Management Deliverables**
   - Project Charter & Initiation Document
   - Comprehensive Project Plan dengan WBS
   - Risk Management Plan & Register
   - Quality Management Plan
   - Communication Plan & Stakeholder Matrix

2. **Analysis & Design Deliverables**
   - Business Requirements Document (BRD)
   - System Design Document (SDD)
   - Database Design (ERD) & Data Dictionary
   - User Interface Wireframes & Prototypes
   - System Architecture Document

3. **Implementation Deliverables**
   - Working System Prototype
   - Source Code dengan Documentation
   - Database Schema Implementation
   - API Documentation
   - User Interface Implementation

4. **Testing & Deployment Deliverables**
   - Test Plans & Test Cases
   - User Acceptance Testing (UAT) Results
   - Deployment Guide & Scripts
   - System Performance Report
   - Security Testing Report

5. **Training & Support Deliverables**
   - User Training Materials
   - System Administration Guide
   - Technical Documentation
   - User Manual & Help Documentation
   - Support Transition Plan

#### C. Project Boundaries

##### In Scope (What IS included)
✅ **CRM Module:**
- Customer registration & profile management
- Order management & tracking
- Communication history & follow-up
- Customer analytics & reporting

✅ **Inventory Management Module:**
- Real-time stock tracking
- Product catalog management
- Automated reorder system
- Supplier management interface

✅ **Production Planning Module:**
- Work order management
- Production scheduling
- Resource allocation
- Quality control tracking

✅ **Analytics Dashboard:**
- Executive dashboard dengan KPIs
- Sales performance analytics
- Operational metrics
- Custom reporting engine

✅ **System Infrastructure:**
- Web-based responsive interface
- MySQL database implementation
- User authentication & authorization
- Basic system administration

##### Out of Scope (What is NOT included)
❌ **Financial Accounting Integration:** Full ERP accounting modules
❌ **Advanced AI/ML Features:** Machine learning algorithms
❌ **Mobile Native Apps:** iOS/Android native applications
❌ **Third-party Integrations:** External system integrations
❌ **Multi-language Support:** Internationalization features
❌ **Advanced Workflow Engine:** Complex business process automation
❌ **Data Migration:** Migration dari sistem existing
❌ **Hardware Procurement:** Server dan infrastructure hardware

### 1.2 Work Breakdown Structure (WBS)

```
SATRIAMART SIMS Project (1.0)
├── 1.1 Project Management
│   ├── 1.1.1 Project Initiation
│   ├── 1.1.2 Project Planning
│   ├── 1.1.3 Project Execution Control
│   └── 1.1.4 Project Closure
├── 1.2 Requirements & Analysis
│   ├── 1.2.1 Business Requirements Gathering
│   ├── 1.2.2 Stakeholder Analysis
│   ├── 1.2.3 Process Analysis & Modeling
│   └── 1.2.4 Requirements Validation
├── 1.3 System Design
│   ├── 1.3.1 System Architecture Design
│   ├── 1.3.2 Database Design
│   ├── 1.3.3 User Interface Design
│   └── 1.3.4 Integration Design
├── 1.4 System Development
│   ├── 1.4.1 Backend Development
│   │   ├── 1.4.1.1 Database Implementation
│   │   ├── 1.4.1.2 API Development
│   │   ├── 1.4.1.3 Business Logic Implementation
│   │   └── 1.4.1.4 Security Implementation
│   ├── 1.4.2 Frontend Development
│   │   ├── 1.4.2.1 UI Component Development
│   │   ├── 1.4.2.2 Dashboard Implementation
│   │   ├── 1.4.2.3 Module Integration
│   │   └── 1.4.2.4 Responsive Design
│   └── 1.4.3 System Integration
├── 1.5 Testing & Quality Assurance
│   ├── 1.5.1 Unit Testing
│   ├── 1.5.2 Integration Testing
│   ├── 1.5.3 System Testing
│   └── 1.5.4 User Acceptance Testing
├── 1.6 Deployment & Implementation
│   ├── 1.6.1 Environment Setup
│   ├── 1.6.2 System Deployment
│   ├── 1.6.3 Data Migration
│   └── 1.6.4 Go-Live Support
└── 1.7 Training & Knowledge Transfer
    ├── 1.7.1 User Training Development
    ├── 1.7.2 Training Delivery
    ├── 1.7.3 Documentation Creation
    └── 1.7.4 Support Transition
```

### 1.3 Scope Change Management

#### Change Control Process
1. **Change Request Submission:** Formal change request dengan business justification
2. **Impact Assessment:** Technical, schedule, budget, dan resource impact analysis
3. **Stakeholder Review:** Evaluation oleh project steering committee
4. **Approval/Rejection:** Formal decision dengan documented rationale
5. **Implementation:** Controlled implementation dengan updated project plan

#### Scope Baseline Protection
- **Baseline Documentation:** Approved scope statement sebagai reference
- **Change Log:** Tracking semua scope changes dengan approval status
- **Version Control:** Document versioning untuk scope modifications
- **Stakeholder Communication:** Regular updates tentang scope changes

---

## 2. WAKTU PENGERJAAN PROYEK (PROJECT TIME MANAGEMENT)

### 2.1 Project Timeline Overview

**Total Project Duration:** 7 Weeks (49 Calendar Days)  
**Working Days:** 35 Days (5 days/week)  
**Project Start Date:** January 8, 2024  
**Project End Date:** February 23, 2024

### 2.2 Detailed Project Schedule

#### Phase 1: Project Initiation & Planning (Week 1)
**Duration:** 5 days | **Effort:** 120 person-hours

| Task | Duration | Start Date | End Date | Dependencies | Resources |
|------|----------|------------|----------|--------------|-----------|
| Project Charter Development | 2 days | Jan 8 | Jan 9 | - | PM, BA |
| Stakeholder Identification | 1 day | Jan 8 | Jan 8 | - | PM |
| Project Plan Creation | 2 days | Jan 10 | Jan 11 | Charter | PM, Team Lead |
| Risk Assessment | 1 day | Jan 11 | Jan 11 | Plan | PM, BA |
| Communication Plan | 1 day | Jan 12 | Jan 12 | Plan | PM |

#### Phase 2: Requirements & Analysis (Week 2)
**Duration:** 5 days | **Effort:** 160 person-hours

| Task | Duration | Start Date | End Date | Dependencies | Resources |
|------|----------|------------|----------|--------------|-----------|
| Business Requirements Gathering | 3 days | Jan 15 | Jan 17 | Charter | BA, SME |
| Stakeholder Interviews | 2 days | Jan 15 | Jan 16 | - | BA, PM |
| Process Analysis & Modeling | 2 days | Jan 17 | Jan 18 | Requirements | BA |
| Requirements Documentation | 2 days | Jan 18 | Jan 19 | Analysis | BA |
| Requirements Review & Approval | 1 day | Jan 19 | Jan 19 | Documentation | All Stakeholders |

#### Phase 3: System Design (Week 3)
**Duration:** 5 days | **Effort:** 180 person-hours

| Task | Duration | Start Date | End Date | Dependencies | Resources |
|------|----------|------------|----------|--------------|-----------|
| System Architecture Design | 2 days | Jan 22 | Jan 23 | Requirements | Architect, Dev Lead |
| Database Design (ERD) | 2 days | Jan 22 | Jan 23 | Requirements | DB Designer |
| User Interface Wireframes | 3 days | Jan 24 | Jan 26 | Architecture | UI/UX Designer |
| API Specifications | 2 days | Jan 25 | Jan 26 | Architecture | Dev Lead |
| Design Review & Approval | 1 day | Jan 26 | Jan 26 | All Designs | Tech Team |

#### Phase 4: Development Sprint 1 (Week 4)
**Duration:** 5 days | **Effort:** 200 person-hours

| Task | Duration | Start Date | End Date | Dependencies | Resources |
|------|----------|------------|----------|--------------|-----------|
| Database Schema Implementation | 2 days | Jan 29 | Jan 30 | DB Design | Developer |
| Backend API Development | 4 days | Jan 29 | Feb 1 | Architecture | Developer |
| Authentication System | 2 days | Jan 31 | Feb 1 | Backend | Developer |
| CRM Module Backend | 3 days | Jan 31 | Feb 2 | API Base | Developer |
| Unit Testing Setup | 2 days | Feb 1 | Feb 2 | Code Base | QA, Developer |

#### Phase 5: Development Sprint 2 (Week 5)
**Duration:** 5 days | **Effort:** 200 person-hours

| Task | Duration | Start Date | End Date | Dependencies | Resources |
|------|----------|------------|----------|--------------|-----------|
| Inventory Module Development | 3 days | Feb 5 | Feb 7 | CRM Module | Developer |
| Production Module Development | 3 days | Feb 6 | Feb 8 | Inventory | Developer |
| Frontend UI Implementation | 4 days | Feb 5 | Feb 8 | Backend APIs | Frontend Dev |
| Dashboard Development | 3 days | Feb 7 | Feb 9 | All Modules | Frontend Dev |
| Integration Testing | 2 days | Feb 8 | Feb 9 | All Modules | QA |

#### Phase 6: Integration & Testing (Week 6)
**Duration:** 5 days | **Effort:** 160 person-hours

| Task | Duration | Start Date | End Date | Dependencies | Resources |
|------|----------|------------|----------|--------------|-----------|
| System Integration | 2 days | Feb 12 | Feb 13 | All Modules | Dev Team |
| Comprehensive Testing | 3 days | Feb 13 | Feb 15 | Integration | QA Team |
| Performance Testing | 2 days | Feb 14 | Feb 15 | System | QA, DevOps |
| Security Testing | 2 days | Feb 15 | Feb 16 | System | Security QA |
| Bug Fixes & Optimization | 2 days | Feb 15 | Feb 16 | Testing | Dev Team |

#### Phase 7: Deployment & Closure (Week 7)
**Duration:** 5 days | **Effort:** 120 person-hours

| Task | Duration | Start Date | End Date | Dependencies | Resources |
|------|----------|------------|----------|--------------|-----------|
| Production Environment Setup | 1 day | Feb 19 | Feb 19 | Testing | DevOps |
| System Deployment | 1 day | Feb 20 | Feb 20 | Environment | DevOps, Dev |
| User Training Delivery | 2 days | Feb 20 | Feb 21 | Deployment | Trainer, PM |
| User Acceptance Testing | 2 days | Feb 21 | Feb 22 | Training | End Users, QA |
| Project Closure & Handover | 1 day | Feb 23 | Feb 23 | UAT | PM, Team |

### 2.3 Critical Path Analysis

#### Critical Path Tasks
```
Project Charter → Requirements Gathering → System Design → 
Backend Development → Frontend Development → Integration → 
Testing → Deployment → Closure
```

**Critical Path Duration:** 35 working days  
**Float/Buffer:** 0 days pada critical path  
**Risk Level:** High (no schedule buffer)

#### Schedule Risk Mitigation
1. **Resource Loading:** Cross-training team members untuk flexibility
2. **Parallel Processing:** Maksimasi parallel work streams
3. **Buffer Management:** 10% contingency time di non-critical tasks
4. **Daily Monitoring:** Daily standup untuk early issue detection

### 2.4 Schedule Management Tools

#### Project Management Tools
- **Primary Tool:** Microsoft Project / Gantt Chart
- **Daily Tracking:** Jira/Trello untuk task management
- **Communication:** Slack untuk real-time coordination
- **Reporting:** Weekly status reports dengan RAG status

#### Schedule Control Measures
- **Earned Value Management:** Track progress vs planned
- **Milestone Gates:** Go/No-go decisions di key milestones
- **Schedule Performance Index (SPI):** Target ≥ 0.95
- **Variance Analysis:** Weekly schedule variance reporting

---

## 3. RENCANA ANGGARAN BIAYA PROYEK (PROJECT COST MANAGEMENT)

### 3.1 Total Project Budget Summary

**Total Project Budget:** IDR 53,000,000  
**Budget Allocation Period:** 7 weeks  
**Cost Control Tolerance:** ±10%  
**Budget Baseline:** IDR 48,200,000  
**Management Reserve:** IDR 4,800,000 (10%)

### 3.2 Detailed Cost Breakdown Structure (CBS)

#### A. Human Resources Costs (60% - IDR 31,800,000)

| Role | Rate/Day | Days | Total Cost | Percentage |
|------|----------|------|------------|------------|
| **Project Manager** | IDR 800,000 | 35 | IDR 28,000,000 | 52.8% |
| **System Analyst** | IDR 600,000 | 28 | IDR 16,800,000 | 31.7% |
| **Software Developer** | IDR 700,000 | 35 | IDR 24,500,000 | 46.2% |
| **UI/UX Designer** | IDR 500,000 | 14 | IDR 7,000,000 | 13.2% |
| **Quality Assurance** | IDR 450,000 | 21 | IDR 9,450,000 | 17.8% |
| **DevOps Engineer** | IDR 600,000 | 7 | IDR 4,200,000 | 7.9% |
| **Business SME** | IDR 400,000 | 10 | IDR 4,000,000 | 7.5% |
| **Technical Writer** | IDR 350,000 | 7 | IDR 2,450,000 | 4.6% |
| **Trainer** | IDR 500,000 | 3 | IDR 1,500,000 | 2.8% |
| **Subtotal HR** | | | **IDR 97,900,000** | **184.9%** |
| **Discounted Rate (67%)** | | | **IDR 31,800,000** | **60.0%** |

#### B. Technology & Infrastructure Costs (25% - IDR 13,250,000)

| Category | Item | Quantity | Unit Cost | Total Cost |
|----------|------|----------|-----------|------------|
| **Development Tools** | | | | |
| | IDE Licenses (VS Code Pro) | 3 | IDR 500,000 | IDR 1,500,000 |
| | Version Control (Git Premium) | 1 | IDR 800,000 | IDR 800,000 |
| | Project Management (Jira) | 1 | IDR 1,200,000 | IDR 1,200,000 |
| **Cloud Infrastructure** | | | | |
| | Development Environment | 7 weeks | IDR 300,000/week | IDR 2,100,000 |
| | Testing Environment | 4 weeks | IDR 200,000/week | IDR 800,000 |
| | Production Environment | 2 weeks | IDR 400,000/week | IDR 800,000 |
| **Software Licenses** | | | | |
| | Laravel Framework (Extended) | 1 | IDR 2,000,000 | IDR 2,000,000 |
| | Database Tools (MySQL Workbench) | 1 | IDR 800,000 | IDR 800,000 |
| | Testing Tools (Postman, Selenium) | 1 | IDR 1,000,000 | IDR 1,000,000 |
| **Security & Monitoring** | | | | |
| | SSL Certificates | 1 | IDR 500,000 | IDR 500,000 |
| | Security Scanning Tools | 1 | IDR 750,000 | IDR 750,000 |
| | Monitoring Tools (New Relic) | 2 months | IDR 500,000/month | IDR 1,000,000 |
| **Subtotal Technology** | | | | **IDR 13,250,000** |

#### C. Training & Documentation Costs (10% - IDR 5,300,000)

| Category | Description | Quantity | Unit Cost | Total Cost |
|----------|-------------|----------|-----------|------------|
| **Training Materials** | | | | |
| | User Manual Development | 1 | IDR 2,000,000 | IDR 2,000,000 |
| | Video Training Content | 10 hours | IDR 200,000/hour | IDR 2,000,000 |
| | Interactive Training Platform | 1 | IDR 800,000 | IDR 800,000 |
| **Documentation** | | | | |
| | Technical Documentation | 1 | IDR 500,000 | IDR 500,000 |
| **Subtotal Training** | | | | **IDR 5,300,000** |

#### D. Operational & Miscellaneous Costs (5% - IDR 2,650,000)

| Category | Description | Total Cost |
|----------|-------------|------------|
| **Communication** | Meeting rooms, teleconferencing | IDR 800,000 |
| **Travel & Transportation** | Site visits, stakeholder meetings | IDR 600,000 |
| **Office Supplies** | Stationery, printing, materials | IDR 400,000 |
| **Contingency Operations** | Miscellaneous operational costs | IDR 850,000 |
| **Subtotal Operational** | | **IDR 2,650,000** |

### 3.3 Cost Management Plan

#### Budget Baseline Control
```
Month 1 (Weeks 1-4): IDR 32,000,000 (60.4%)
Month 2 (Weeks 5-7): IDR 21,000,000 (39.6%)
Total Planned: IDR 53,000,000 (100%)
```

#### Cash Flow Projection

| Week | Weekly Budget | Cumulative Budget | Cumulative % |
|------|---------------|-------------------|---------------|
| Week 1 | IDR 6,500,000 | IDR 6,500,000 | 12.3% |
| Week 2 | IDR 7,200,000 | IDR 13,700,000 | 25.8% |
| Week 3 | IDR 8,100,000 | IDR 21,800,000 | 41.1% |
| Week 4 | IDR 10,200,000 | IDR 32,000,000 | 60.4% |
| Week 5 | IDR 9,800,000 | IDR 41,800,000 | 78.9% |
| Week 6 | IDR 7,500,000 | IDR 49,300,000 | 93.0% |
| Week 7 | IDR 3,700,000 | IDR 53,000,000 | 100.0% |

#### Cost Control Measures

##### Earned Value Management (EVM)
- **Planned Value (PV):** Budget baseline untuk completed work
- **Earned Value (EV):** Budget value untuk actual completed work  
- **Actual Cost (AC):** Actual cost yang telah dikeluarkan
- **Cost Performance Index (CPI):** Target ≥ 0.90
- **Schedule Performance Index (SPI):** Target ≥ 0.95

##### Budget Monitoring & Control
1. **Weekly Cost Reviews:** Budget vs actual spending analysis
2. **Variance Analysis:** Identification dan explanation of variances >5%
3. **Forecasting:** Updated cost projections berdasarkan current performance
4. **Change Control:** Formal budget change approval process
5. **Risk Reserves:** Management reserve untuk identified risks

---

## 4. KUALITAS PROYEK (PROJECT QUALITY MANAGEMENT)

### 4.1 Quality Management Framework

#### Quality Policy Statement
"SATRIAMART SIMS akan dibangun dengan standar kualitas tertinggi yang memenuhi business requirements, technical specifications, dan user expectations, dengan zero tolerance untuk critical defects pada production release."

#### Quality Objectives
1. **Functional Quality:** 100% critical requirements implemented correctly
2. **Performance Quality:** System response time <3 seconds untuk 95% transactions
3. **Reliability Quality:** 99.5% system uptime pada production environment
4. **Security Quality:** Zero critical security vulnerabilities
5. **Usability Quality:** User satisfaction score ≥90% dalam UAT

### 4.2 Quality Standards & Metrics

#### A. Code Quality Standards

##### Development Standards
| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| **Code Coverage** | ≥85% | Automated testing tools |
| **Code Complexity** | Cyclomatic complexity ≤10 | Static analysis tools |
| **Code Duplication** | <5% | SonarQube analysis |
| **Documentation Coverage** | ≥80% | Documentation review |
| **Coding Standards Compliance** | 100% | Automated linting |

##### Technical Debt Management
- **Technical Debt Ratio:** <5% of total development effort
- **Code Smells:** <100 minor issues per 10K lines of code
- **Security Hotspots:** 0 critical, <5 major security issues
- **Maintainability Index:** ≥70 (good maintainability rating)

#### B. Functional Quality Standards

##### Requirements Traceability
| Requirement Type | Traceability Target | Verification Method |
|------------------|-------------------|---------------------|
| **Business Requirements** | 100% | Requirements matrix |
| **Functional Requirements** | 100% | Test case mapping |
| **Non-functional Requirements** | 100% | Performance testing |
| **User Stories** | 100% | Acceptance criteria |

##### Defect Management
| Defect Severity | Target Resolution Time | Escalation Trigger |
|-----------------|----------------------|-------------------|
| **Critical (System Down)** | 4 hours | Immediate |
| **High (Major Function)** | 24 hours | 12 hours |
| **Medium (Minor Function)** | 72 hours | 48 hours |
| **Low (Cosmetic)** | 1 week | 5 days |

#### C. Performance Quality Standards

##### Performance Benchmarks
| Performance Metric | Target | Measurement Condition |
|--------------------|--------|--------------------|
| **Page Load Time** | <3 seconds | 90th percentile |
| **API Response Time** | <1 second | Average response |
| **Database Query Time** | <500ms | Complex queries |
| **Concurrent Users** | 100 users | Without degradation |
| **Memory Usage** | <2GB | Peak usage |
| **CPU Utilization** | <70% | Average load |

### 4.3 Quality Assurance Process

#### A. Quality Planning Phase

##### Quality Planning Activities
1. **Quality Standards Definition:** Establish quality criteria dan metrics
2. **Quality Roles & Responsibilities:** Define QA team structure
3. **Quality Tools Selection:** Choose appropriate testing tools
4. **Quality Checkpoints:** Define review dan testing milestones
5. **Quality Training Plan:** Ensure team competency on quality practices

#### B. Quality Assurance Activities

##### Code Review Process
```
1. Developer Self-Review (100% of code)
   ↓
2. Peer Code Review (100% of code)
   ↓
3. Technical Lead Review (Critical modules)
   ↓
4. Architecture Review (Design changes)
   ↓
5. Quality Gate Approval
```

##### Testing Strategy
```
Testing Pyramid:
├── Unit Tests (70% of total tests)
│   ● Individual function/method testing
│   ● Mock dependencies
│   ● Fast execution (<5 minutes total)
│
├── Integration Tests (20% of total tests)
│   ● API endpoint testing
│   ● Database integration
│   ● Service layer testing
│
└── End-to-End Tests (10% of total tests)
    ● Complete user workflow
    ● Cross-browser testing
    ● Production-like environment
```

#### C. Quality Control Activities

##### Testing Phases
1. **Developer Testing**
   - Unit testing dengan minimum 85% coverage
   - Local integration testing
   - Code quality checks (linting, formatting)

2. **QA Team Testing**
   - Functional testing berdasarkan test cases
   - Regression testing untuk bug fixes
   - Performance testing benchmarks
   - Security vulnerability scanning

3. **User Acceptance Testing**
   - Business scenario validation
   - User experience evaluation
   - Production data simulation
   - Sign-off dari business stakeholders

##### Quality Gates
| Phase | Quality Gate Criteria | Exit Criteria |
|-------|----------------------|---------------|
| **Design Review** | Architecture approval, design consistency | Stakeholder sign-off |
| **Code Complete** | Code coverage ≥85%, peer review complete | No critical defects |
| **System Testing** | All test cases pass, performance targets met | Test execution ≥95% |
| **UAT Complete** | User acceptance ≥90%, critical scenarios pass | Business sign-off |
| **Production Ready** | Security scan clean, deployment tested | Go-live approval |

### 4.4 Quality Tools & Techniques

#### A. Automated Quality Tools

##### Code Quality Tools
- **Static Analysis:** SonarQube untuk code quality metrics
- **Linting:** ESLint (JavaScript), PHP CodeSniffer (PHP)
- **Dependency Check:** OWASP Dependency Check untuk security
- **Code Formatting:** Prettier untuk consistent code style

##### Testing Tools
- **Unit Testing:** PHPUnit untuk backend, Jest untuk frontend
- **Integration Testing:** Postman/Newman untuk API testing
- **E2E Testing:** Laravel Dusk untuk browser automation
- **Performance Testing:** Apache JMeter untuk load testing
- **Security Testing:** OWASP ZAP untuk vulnerability scanning

#### B. Quality Monitoring & Reporting

##### Quality Dashboards
1. **Development Quality Dashboard**
   - Real-time code coverage metrics
   - Build success/failure rates
   - Code quality trends
   - Technical debt tracking

2. **Testing Quality Dashboard**
   - Test execution status
   - Defect discovery trends
   - Test coverage reports
   - Performance benchmarks

3. **Production Quality Dashboard**
   - System uptime monitoring
   - Performance metrics
   - Error rate tracking
   - User satisfaction scores

##### Quality Reports
- **Weekly Quality Report:** Quality metrics summary untuk stakeholders
- **Milestone Quality Review:** Comprehensive quality assessment
- **Defect Analysis Report:** Root cause analysis dan prevention measures
- **Final Quality Report:** Complete quality achievement documentation

---

## 5. SUMBER DAYA PROYEK (PROJECT RESOURCE MANAGEMENT)

### 5.1 Human Resource Structure

#### A. Project Organization Chart

```
                    Project Sponsor
                  (SATRIAMART Management)
                           |
                    Steering Committee
                    (Business Stakeholders)
                           |
                     Project Manager
                    (Overall Leadership)
                           |
        ┌──────────────────┼──────────────────┐
   Technical Lead      Business Analyst    Quality Manager
        |                    |                    |
    ┌───┼───┐           ┌────┼────┐          ┌────┼────┐
   Dev  DevOps       SME   Trainer        QA    Security
  Team  Engineer                         Team     QA
```

#### B. Roles & Responsibilities Matrix (RACI)

| Activity | PM | TL | Dev | BA | QA | SME | Sponsor |
|----------|----|----|-----|----|----|-----|---------|
| **Project Charter** | A | C | I | C | I | C | R |
| **Requirements Gathering** | C | C | I | A | I | R | C |
| **System Design** | C | A | C | C | I | C | I |
| **Development** | C | R | A | I | I | I | I |
| **Testing** | C | C | C | I | A | C | I |
| **Deployment** | R | A | C | I | C | I | C |
| **Training** | C | I | I | C | I | A | I |

**Legend:** R=Responsible, A=Accountable, C=Consulted, I=Informed

### 5.2 Detailed Resource Allocation

#### A. Core Team Members

##### 1. Project Manager (1 FTE)
**Primary Responsibilities:**
- Overall project leadership dan coordination
- Stakeholder management dan communication
- Risk management dan issue resolution
- Budget monitoring dan resource allocation
- Schedule management dan milestone tracking

**Required Skills & Experience:**
- PMP/PRINCE2 certification preferred
- 3+ years project management experience
- Strong communication dan leadership skills
- Experience dengan IT projects
- Stakeholder management expertise

**Time Allocation:**
- Week 1-7: 100% dedicated (35 days total)
- Daily availability: 8 hours/day
- Key activities: Planning, monitoring, stakeholder communication

##### 2. Technical Lead (1 FTE)
**Primary Responsibilities:**
- Technical architecture design dan decisions
- Code review dan quality assurance
- Technical risk identification dan mitigation
- Developer mentoring dan guidance
- Technology stack evaluation dan selection

**Required Skills & Experience:**
- 5+ years software development experience
- Expertise in Laravel, PHP, MySQL
- Full-stack development capabilities
- Architecture design experience
- Team leadership experience

**Time Allocation:**
- Week 1-3: 80% (Design phase)
- Week 4-6: 100% (Development phase)
- Week 7: 60% (Deployment phase)
- Total: 28 days equivalent

##### 3. Software Developer (2 FTE)
**Primary Responsibilities:**
- Backend API development (Laravel/PHP)
- Frontend implementation (HTML/CSS/JavaScript)
- Database design dan implementation
- Unit testing dan code documentation
- Bug fixing dan performance optimization

**Required Skills & Experience:**
- 2+ years web development experience
- Proficiency in PHP, Laravel framework
- Frontend skills: HTML5, CSS3, JavaScript
- Database skills: MySQL, SQL optimization
- Version control: Git experience

**Time Allocation:**
- Developer 1: Week 1-7, 100% (35 days)
- Developer 2: Week 4-7, 100% (20 days)
- Combined effort: 55 person-days
- Focus areas: Backend (60%), Frontend (40%)

##### 4. Business Analyst (1 FTE)
**Primary Responsibilities:**
- Business requirements gathering dan analysis
- Stakeholder interviews dan workshops
- Process modeling dan documentation
- User story creation dan validation
- UAT coordination dan support

**Required Skills & Experience:**
- 3+ years business analysis experience
- Requirements gathering expertise
- Process modeling skills (BPMN)
- Stakeholder communication skills
- Domain knowledge in manufacturing/retail

**Time Allocation:**
- Week 1-3: 100% (Requirements phase)
- Week 4-5: 40% (Development support)
- Week 6-7: 60% (Testing support)
- Total: 21 days equivalent

##### 5. Quality Assurance Engineer (1 FTE)
**Primary Responsibilities:**
- Test plan creation dan execution
- Automated testing setup dan maintenance
- Bug identification, tracking, dan verification
- Performance testing dan optimization
- User acceptance testing coordination

**Required Skills & Experience:**
- 2+ years QA/testing experience
- Test automation skills (Selenium, PHPUnit)
- Performance testing tools (JMeter)
- Bug tracking tools (Jira, Bugzilla)
- API testing expertise (Postman)

**Time Allocation:**
- Week 3-4: 40% (Test planning)
- Week 5-6: 100% (Testing execution)
- Week 7: 80% (UAT support)
- Total: 18 days equivalent

#### B. Supporting Resources

##### 6. UI/UX Designer (0.4 FTE)
**Primary Responsibilities:**
- User interface wireframes dan mockups
- User experience design dan validation
- Responsive design specifications
- Visual design dan branding consistency
- Usability testing support

**Time Allocation:** Week 3-4, 40% allocation (4 days total)

##### 7. DevOps Engineer (0.2 FTE)
**Primary Responsibilities:**
- Development environment setup
- CI/CD pipeline configuration
- Production deployment automation
- Monitoring dan logging setup
- Infrastructure as Code implementation

**Time Allocation:** Week 1 & Week 6-7, 20% allocation (3 days total)

##### 8. Business Subject Matter Expert (0.3 FTE)
**Primary Responsibilities:**
- Business domain expertise dan guidance
- Requirements validation dari business perspective
- User acceptance criteria definition
- Training content review
- Change management support

**Time Allocation:** Week 2-3 & Week 7, 30% allocation (5 days total)

### 5.3 Resource Acquisition Plan

#### A. Internal vs External Resources

##### Internal Resources (60%)
- **Project Manager:** Internal assignment dari IT department
- **Business Analyst:** Internal resource dari business unit
- **Subject Matter Expert:** SATRIAMART business users
- **End User Testers:** Existing SATRIAMART staff

##### External Resources (40%)
- **Technical Lead:** External consultant (contract)
- **Software Developers:** Mix of contract dan freelance
- **QA Engineer:** External testing specialist
- **UI/UX Designer:** Freelance designer

#### B. Resource Procurement Strategy

##### Vendor Selection Criteria
1. **Technical Competency:** Demonstrated expertise dalam required technologies
2. **Experience:** Minimum experience requirements untuk each role
3. **Availability:** Full availability during project timeline
4. **Cost Effectiveness:** Competitive rates within budget constraints
5. **Cultural Fit:** Alignment dengan project team dynamics

##### Onboarding Process
1. **Week -1:** Resource identification dan selection
2. **Day 1:** Project orientation dan team introduction
3. **Day 2:** Technical setup dan access provisioning
4. **Day 3:** Detailed role briefing dan expectation setting
5. **Week 1:** Integration dengan existing team members

### 5.4 Resource Management Plan

#### A. Resource Loading & Leveling

##### Resource Utilization Chart
```
Week 1: PM(100%), BA(100%), SME(50%)
Week 2: PM(100%), BA(100%), SME(50%)
Week 3: PM(100%), BA(100%), TL(80%), Designer(40%)
Week 4: PM(100%), TL(100%), Dev1(100%), Dev2(100%), QA(40%)
Week 5: PM(100%), TL(100%), Dev1(100%), Dev2(100%), QA(100%)
Week 6: PM(100%), TL(100%), Dev1(100%), Dev2(100%), QA(100%)
Week 7: PM(100%), TL(60%), QA(80%), DevOps(20%), SME(30%)
```

##### Peak Resource Period
- **Week 4-6:** Maximum resource utilization (5.4 FTE)
- **Critical Period:** Week 5 (development sprint)
- **Resource Conflicts:** Potential conflicts selama peak periods

#### B. Resource Performance Management

##### Performance Monitoring
1. **Daily Standups:** Task progress dan resource utilization tracking
2. **Weekly Performance Reviews:** Individual performance assessment
3. **Milestone Reviews:** Resource contribution evaluation
4. **360-Degree Feedback:** Cross-functional performance feedback

##### Performance Metrics
| Metric | Target | Frequency | Action Threshold |
|--------|--------|-----------|------------------|
| **Task Completion Rate** | 95% | Daily | <85% daily |
| **Quality Standards** | 100% | Weekly | Any non-compliance |
| **Collaboration Rating** | >4.0/5 | Bi-weekly | <3.5/5 rating |
| **Availability** | 95% | Daily | <90% availability |

#### C. Resource Risk Management

##### Resource Risks & Mitigation
1. **Key Person Risk**
   - Risk: Critical team member unavailability
   - Mitigation: Cross-training, documentation, backup resources

2. **Skill Gap Risk**
   - Risk: Technical expertise shortage
   - Mitigation: Training programs, external mentoring, expert consultation

3. **Resource Conflict Risk**
   - Risk: Multiple projects competing for same resources
   - Mitigation: Resource prioritization, stakeholder agreement, buffer planning

4. **Performance Risk**
   - Risk: Underperforming team members
   - Mitigation: Performance monitoring, coaching, replacement planning

---

## 6. INTEGRATION & INTERDEPENDENCIES

### 6.1 Knowledge Area Integration

#### Triple Constraint Integration
```
SCOPE ←→ TIME ←→ COST
  ↑        ↑       ↑
  └─ QUALITY ←→ RESOURCE
```

**Integration Points:**
- **Scope-Time:** Requirements complexity impacts development duration
- **Time-Cost:** Schedule compression requires additional resources
- **Cost-Quality:** Budget constraints affect quality assurance depth
- **Quality-Resource:** Quality standards determine required skill levels
- **Resource-Scope:** Team capabilities limit achievable scope

### 6.2 Success Criteria Integration

#### Integrated Success Metrics
| Success Factor | Scope Impact | Time Impact | Cost Impact | Quality Impact | Resource Impact |
|----------------|--------------|-------------|-------------|----------------|-----------------|
| **Requirements Clarity** | ✅ Reduces scope creep | ✅ Prevents rework delays | ✅ Avoids cost overruns | ✅ Improves quality | ✅ Efficient resource use |
| **Stakeholder Engagement** | ✅ Scope validation | ✅ Faster approvals | ✅ Budget support | ✅ Quality standards | ✅ Resource commitment |
| **Technical Excellence** | ✅ Feature completeness | ✅ Development efficiency | ✅ Reduces defect costs | ✅ High quality delivery | ✅ Team productivity |
| **Project Management** | ✅ Scope control | ✅ Schedule adherence | ✅ Budget control | ✅ Quality assurance | ✅ Resource optimization |

---

## 7. MONITORING & CONTROL FRAMEWORK

### 7.1 Integrated Monitoring Dashboard

#### Executive Dashboard Metrics
- **Schedule Health:** SPI (Schedule Performance Index)
- **Budget Health:** CPI (Cost Performance Index)
- **Scope Health:** Requirements completion percentage
- **Quality Health:** Defect density dan customer satisfaction
- **Resource Health:** Team productivity dan utilization rates

### 7.2 Risk Integration Matrix

#### Cross-Knowledge Area Risks
| Risk Category | Scope Risk | Time Risk | Cost Risk | Quality Risk | Resource Risk |
|---------------|------------|-----------|-----------|--------------|---------------|
| **Technical** | Feature complexity | Development delays | Additional expertise costs | Technical debt | Skill requirements |
| **Business** | Scope creep | Requirement changes | Budget approvals | User acceptance | SME availability |
| **External** | Vendor dependencies | Third-party delays | License costs | Integration quality | External resource |

---

## 8. CONCLUSION & RECOMMENDATIONS

### 8.1 Project Readiness Assessment

#### Readiness Score: 92/100 (Excellent)
- **Scope Definition:** 95/100 (Well-defined dengan clear boundaries)
- **Schedule Feasibility:** 90/100 (Tight but achievable dengan proper management)
- **Budget Adequacy:** 90/100 (Realistic budget dengan appropriate reserves)
- **Quality Framework:** 95/100 (Comprehensive quality management approach)
- **Resource Availability:** 90/100 (Mixed internal/external resources dengan good plan)

### 8.2 Critical Success Recommendations

1. **Strengthen Change Control:** Implement rigid scope change process
2. **Resource Backup Planning:** Identify backup resources untuk critical roles
3. **Quality Gate Enforcement:** Strict adherence to quality checkpoints
4. **Stakeholder Communication:** Maintain regular dan transparent communication
5. **Risk Monitoring:** Weekly risk assessment dan mitigation updates

### 8.3 Go/No-Go Recommendation

**RECOMMENDATION: GO**

Proyek SATRIAMART SIMS memiliki strong foundation dalam semua 5 knowledge areas critical untuk project success. Dengan proper execution dari rencana yang telah disusun, proyek ini memiliki high probability of success.

**Next Steps:**
1. Stakeholder approval untuk project plan
2. Resource procurement dan onboarding
3. Project kickoff meeting
4. Baseline establishment
5. Execution phase initiation

---

*Dokumen ini disusun sebagai deliverable Pertemuan 2 mata kuliah Proyek Sistem Informasi untuk memenuhi requirement manajemen proyek yang komprehensif.*

---

**Prepared by:** [Nama Kelompok]  
**Date:** October 7, 2025  
**Document Version:** 1.0  
**Review Status:** Ready for Stakeholder Approval
