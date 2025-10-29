# PROJECT CHARTER & PLAN
## SATRIAMART Integrated Management System (SIMS)

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Mata Kuliah: Proyek Sistem Informasi II**

---

## PROJECT CHARTER

### 1. PROJECT OVERVIEW

**Project Name:** SATRIAMART Integrated Management System (SIMS)  
**Project Manager:** [Nama Mahasiswa]  
**Start Date:** [Tanggal Mulai]  
**Target Completion:** 7 Minggu  
**Budget Estimation:** IDR 50,000,000 - 75,000,000

### 2. BUSINESS CASE & JUSTIFICATION

#### Business Problem
SATRIAMART sebagai perusahaan dekorasi & aksesoris akrilik menghadapi tantangan dalam:
- Manajemen pelanggan yang masih manual
- Tracking inventory yang tidak real-time
- Perencanaan produksi yang belum optimal
- Analisis bisnis yang terbatas

#### Business Opportunity
- Peningkatan efisiensi operasional hingga 40%
- Pengurangan kesalahan inventory hingga 60%
- Peningkatan customer satisfaction melalui better service
- Kemampuan analisis data untuk strategic decision making

#### Expected Benefits
- **Financial Benefits:**
  - Pengurangan operational cost 20-30%
  - Peningkatan revenue 15-25% melalui better customer management
  - ROI dalam 12-18 bulan

- **Operational Benefits:**
  - Real-time inventory tracking
  - Automated reporting dan analytics
  - Improved customer service response time
  - Better production planning accuracy

### 3. PROJECT OBJECTIVES

#### Primary Objectives
1. Mengembangkan sistem terintegrasi untuk SATRIAMART yang mencakup CRM, Inventory Management, Production Planning, dan Sales Analytics
2. Meningkatkan efisiensi operasional melalui automasi proses bisnis
3. Menyediakan real-time visibility terhadap semua aspek bisnis
4. Mengimplementasikan platform yang scalable untuk pertumbuhan bisnis

#### Success Criteria
- Sistem berhasil diimplementasikan dengan 95% functionality working
- User acceptance rate minimal 80%
- Performance improvement minimal 30% dari baseline
- Zero data loss selama migration
- Training completion rate 100% untuk all users

### 4. STAKEHOLDER IDENTIFICATION

| Stakeholder | Role | Interest Level | Influence | Communication Strategy |
|-------------|------|----------------|-----------|----------------------|
| Owner SATRIAMART | Sponsor | High | High | Weekly status meetings |
| Operations Manager | Primary User | High | Medium | Bi-weekly demos & feedback |
| Sales Team | End User | Medium | Low | Monthly updates |
| Production Team | End User | High | Medium | Weekly workshops |
| IT Support | Technical Support | Medium | Medium | Technical meetings |
| Customers | Indirect User | Low | Low | Through improved service |

### 5. HIGH-LEVEL TIMELINE

| Phase | Duration | Key Milestones |
|-------|----------|----------------|
| Initiation | Week 1 | Project Charter Approval |
| Planning | Week 2 | Detailed Project Plan |
| Analysis | Week 3 | Requirements Specification |
| Design | Week 4 | System Design Complete |
| Implementation | Week 5-6 | Core System Development |
| Closure | Week 7 | System Deployment & Training |

### 6. HIGH-LEVEL BUDGET

| Category | Estimated Cost (IDR) |
|----------|---------------------|
| Development Tools | 5,000,000 |
| Cloud Infrastructure | 8,000,000 |
| Testing & QA | 3,000,000 |
| Training & Documentation | 4,000,000 |
| Contingency (20%) | 4,000,000 |
| **Total** | **24,000,000** |

---

## DETAILED PROJECT PLAN

### 1. WORK BREAKDOWN STRUCTURE (WBS)

#### 1.0 Project Initiation
- 1.1 Project Charter Development
- 1.2 Stakeholder Analysis
- 1.3 Initial Risk Assessment
- 1.4 Team Formation & Roles Assignment

#### 2.0 Project Planning
- 2.1 Detailed Requirements Gathering
- 2.2 Resource Planning
- 2.3 Communication Plan
- 2.4 Quality Management Plan
- 2.5 Risk Management Plan

#### 3.0 System Analysis
- 3.1 Business Process Analysis
- 3.2 Functional Requirements Documentation
- 3.3 Non-Functional Requirements
- 3.4 Use Case Development
- 3.5 Business Requirements Document (BRD)

#### 4.0 System Design
- 4.1 System Architecture Design
- 4.2 Database Design
- 4.3 User Interface Design
- 4.4 Integration Design
- 4.5 System Design Document (SDD)

#### 5.0 Implementation
- 5.1 Development Environment Setup
- 5.2 Backend Development
- 5.3 Frontend Development
- 5.4 Database Implementation
- 5.5 System Integration
- 5.6 Unit Testing

#### 6.0 Testing & Quality Assurance
- 6.1 Test Plan Development
- 6.2 Integration Testing
- 6.3 System Testing
- 6.4 User Acceptance Testing
- 6.5 Performance Testing

#### 7.0 Deployment & Closure
- 7.1 Production Deployment
- 7.2 User Training
- 7.3 Documentation Finalization
- 7.4 Project Closure Report
- 7.5 Lessons Learned

### 2. DETAILED SCHEDULE (GANTT CHART)

| Task | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 |
|------|--------|--------|--------|--------|--------|--------|--------|
| Project Charter | ████ |  |  |  |  |  |  |
| Stakeholder Analysis | ████ |  |  |  |  |  |  |
| Requirements Gathering |  | ████ |  |  |  |  |  |
| Resource Planning |  | ████ |  |  |  |  |  |
| Business Process Analysis |  |  | ████ |  |  |  |  |
| BRD Development |  |  | ████ |  |  |  |  |
| System Architecture |  |  |  | ████ |  |  |  |
| Database Design |  |  |  | ████ |  |  |  |
| UI/UX Design |  |  |  | ████ |  |  |  |
| Backend Development |  |  |  |  | ████ | ████ |  |
| Frontend Development |  |  |  |  | ████ | ████ |  |
| Integration & Testing |  |  |  |  |  | ████ |  |
| Deployment |  |  |  |  |  |  | ████ |
| Documentation |  |  |  |  |  |  | ████ |

### 3. RESOURCE ALLOCATION PLAN

#### Human Resources
| Role | Allocation | Responsibilities |
|------|------------|-----------------|
| Project Manager | 100% | Overall coordination, stakeholder management |
| System Analyst | 80% | Requirements analysis, business process modeling |
| Software Developer | 100% | System development, coding, testing |
| UI/UX Designer | 40% | User interface design, user experience |
| Quality Assurance | 60% | Testing, quality control |

#### Technical Resources
- Development Environment: Local + Cloud (AWS/GCP)
- Development Tools: VS Code, Git, Docker
- Database: MySQL
- Frontend Framework: TailwindCSS + Vanilla JavaScript
- Backend Framework: Laravel (PHP)
- Testing Tools: PHPUnit, Laravel Dusk
- Project Management: Jira/Trello

### 4. RISK REGISTER & MITIGATION PLAN

| Risk ID | Risk Description | Probability | Impact | Risk Level | Mitigation Strategy |
|---------|------------------|-------------|--------|------------|-------------------|
| R001 | Technical complexity exceeds team capability | Medium | High | High | Provide additional training, technical mentoring |
| R002 | Scope creep from stakeholders | High | Medium | High | Strict change control process, regular stakeholder communication |
| R003 | Key team member unavailability | Medium | High | High | Cross-training, documentation, backup resources |
| R004 | Integration challenges with existing systems | Medium | Medium | Medium | Proof of concepts, early testing |
| R005 | Performance issues under load | Low | High | Medium | Performance testing, scalable architecture |
| R006 | User adoption resistance | Medium | Medium | Medium | User involvement in design, comprehensive training |
| R007 | Budget overrun | Low | High | Medium | Regular budget monitoring, contingency planning |
| R008 | Timeline delays | Medium | Medium | Medium | Buffer time, critical path monitoring |

### 5. COMMUNICATION PLAN

#### Stakeholder Communication Matrix
| Stakeholder | Communication Method | Frequency | Content |
|-------------|---------------------|-----------|---------|
| Project Sponsor | Status Report + Meeting | Weekly | High-level progress, issues, decisions needed |
| Steering Committee | Formal Presentation | Bi-weekly | Milestone achievements, risks, budget |
| End Users | Demos + Workshops | Bi-weekly | System features, feedback collection |
| Technical Team | Daily Standup | Daily | Progress, blockers, coordination |
| Management | Dashboard + Report | Weekly | KPIs, milestones, risks |

#### Communication Tools
- **Project Management:** Jira/Trello for task tracking
- **Team Collaboration:** Slack/Teams for daily communication
- **Document Sharing:** Google Workspace/SharePoint
- **Version Control:** Git (GitHub/GitLab)
- **Video Conferencing:** Zoom/Teams for meetings

### 6. QUALITY MANAGEMENT PLAN

#### Quality Standards
- **Code Quality:** Clean Code principles, code reviews
- **Documentation:** IEEE standards for technical documentation
- **Testing:** 80% code coverage, automated testing
- **Performance:** <3 second response time, 99% uptime
- **Security:** OWASP compliance, data encryption

#### Quality Assurance Activities
- Peer code reviews for all development
- Automated testing pipeline
- Regular quality checkpoints at each phase
- User acceptance testing with real scenarios
- Performance testing under realistic load

#### Quality Metrics
- Defect density: <5 defects per 1000 lines of code
- Test coverage: >80%
- User satisfaction: >80% positive feedback
- Performance: <3 second average response time
- Availability: >99% uptime

---

## CONCLUSION

Project Charter dan Plan ini menyediakan foundation yang solid untuk pengembangan SATRIAMART Integrated Management System. Dengan pendekatan hybrid Agile-Waterfall, proyek ini dirancang untuk memberikan value maksimal sambil menjaga fleksibilitas dalam menghadapi perubahan requirements.

Key success factors:
1. Strong stakeholder engagement dan communication
2. Proper risk management dan mitigation
3. Quality-focused development approach
4. Realistic timeline dan resource allocation
5. Clear success criteria dan metrics

Proyek ini diharapkan dapat meningkatkan efisiensi operasional SATRIAMART secara signifikan dan menyediakan foundation untuk pertumbuhan bisnis di masa depan.
