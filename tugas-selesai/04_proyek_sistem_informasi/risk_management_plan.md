# RISK MANAGEMENT PLAN
## SATRIAMART INTEGRATED MANAGEMENT SYSTEM (SIMS)

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Semester 7**

---

**Mata Kuliah:** Proyek Sistem Informasi II  
**Dosen Pengampu:** Rani Irma Handayani, M.Kom  
**Project Manager:** [Nama Mahasiswa 1]  
**Tanggal:** Oktober 2025  
**Versi:** 1.0

---

## TABLE OF CONTENTS

1. [Risk Management Overview](#1-risk-management-overview)
2. [Risk Assessment Methodology](#2-risk-assessment-methodology)
3. [Risk Register](#3-risk-register)
4. [Risk Analysis](#4-risk-analysis)
5. [Risk Response Strategies](#5-risk-response-strategies)
6. [Risk Monitoring & Control](#6-risk-monitoring--control)
7. [Contingency Plans](#7-contingency-plans)
8. [Risk Communication](#8-risk-communication)

---

## 1. RISK MANAGEMENT OVERVIEW

### 1.1 Purpose
Risk Management Plan ini bertujuan untuk mengidentifikasi, menganalisis, dan mengelola risiko-risiko yang dapat mempengaruhi keberhasilan proyek SATRIAMART Integrated Management System (SIMS).

### 1.2 Risk Management Approach
**Proactive Risk Management:**
- Early identification dan assessment
- Preventive measures implementation
- Continuous monitoring dan review
- Rapid response untuk emerging risks

### 1.3 Risk Management Objectives
1. **Minimize Project Impact:** Reduce probability dan impact of negative risks
2. **Maximize Opportunities:** Leverage positive risks untuk project benefit
3. **Ensure Project Success:** Maintain project timeline, budget, dan quality
4. **Stakeholder Confidence:** Transparent risk communication

### 1.4 Risk Management Team
**Risk Manager:** Project Manager  
**Risk Assessors:** All team members  
**Risk Reviewers:** Academic supervisor, stakeholders  
**Risk Monitors:** Assigned team members per risk category  

---

## 2. RISK ASSESSMENT METHODOLOGY

### 2.1 Risk Identification Techniques
1. **Brainstorming Sessions:** Team workshops untuk risk identification
2. **Expert Interviews:** Consultation dengan academic supervisor
3. **Historical Analysis:** Lessons learned dari similar projects
4. **Documentation Review:** Analysis of project artifacts
5. **Stakeholder Input:** Feedback dari project stakeholders

### 2.2 Risk Categories
**Technical Risks:** Technology-related challenges  
**Project Management Risks:** Planning, execution, dan control issues  
**Resource Risks:** Team availability dan skill gaps  
**External Risks:** Factors beyond project control  
**Academic Risks:** University-specific constraints  
**Business Risks:** SATRIAMART operational considerations  

### 2.3 Probability Scale
| **Level** | **Description** | **Probability Range** |
|-----------|----------------|---------------------|
| **1 - Very Low** | Very unlikely to occur | 0-10% |
| **2 - Low** | Unlikely to occur | 11-30% |
| **3 - Medium** | Moderate chance | 31-50% |
| **4 - High** | Likely to occur | 51-80% |
| **5 - Very High** | Almost certain | 81-100% |

### 2.4 Impact Scale
| **Level** | **Description** | **Impact on Project** |
|-----------|----------------|---------------------|
| **1 - Very Low** | Minimal impact | <5% delay/cost increase |
| **2 - Low** | Minor impact | 5-10% delay/cost increase |
| **3 - Medium** | Moderate impact | 11-20% delay/cost increase |
| **4 - High** | Major impact | 21-40% delay/cost increase |
| **5 - Very High** | Critical impact | >40% delay or project failure |

### 2.5 Risk Priority Matrix
```
PROBABILITY
    5 |  M   H   H   VH  VH
    4 |  L   M   H   H   VH  
    3 |  L   L   M   H   H
    2 |  VL  L   L   M   H
    1 |  VL  VL  L   L   M
      +------------------
        1   2   3   4   5
              IMPACT

Legend:
VL = Very Low    L = Low    M = Medium    H = High    VH = Very High
```

---

## 3. RISK REGISTER

### 3.1 High Priority Risks

#### RISK-001: Technical Complexity Overwhelm
**Category:** Technical  
**Description:** Team lacks sufficient technical expertise untuk complex system integration  
**Probability:** 4 (High)  
**Impact:** 4 (High)  
**Risk Score:** 16 (High)  
**Owner:** Technical Lead  
**Response Strategy:** Mitigate  

**Triggers:**
- Difficulty implementing core modules
- Integration challenges between components
- Performance issues during testing

**Response Actions:**
- Implement proof-of-concept early
- Simplify architecture if needed
- Seek mentor guidance for complex features
- Use established frameworks dan libraries

---

#### RISK-002: Scope Creep
**Category:** Project Management  
**Description:** Stakeholders request additional features beyond original scope  
**Probability:** 4 (High)  
**Impact:** 3 (Medium)  
**Risk Score:** 12 (High)  
**Owner:** Project Manager  
**Response Strategy:** Mitigate  

**Triggers:**
- Frequent change requests
- New requirements during development
- Stakeholder dissatisfaction dengan initial design

**Response Actions:**
- Clear requirements documentation
- Change control process implementation
- Regular stakeholder communication
- Document out-of-scope items for future phases

---

#### RISK-003: Team Member Unavailability
**Category:** Resource  
**Description:** Key team members become unavailable due to academic atau personal commitments  
**Probability:** 3 (Medium)  
**Impact:** 4 (High)  
**Risk Score:** 12 (High)  
**Owner:** Project Manager  
**Response Strategy:** Mitigate  

**Triggers:**
- Conflicting academic deadlines
- Personal emergencies
- Other course workload increases

**Response Actions:**
- Cross-training team members
- Detailed documentation of all work
- Backup assignments untuk critical tasks
- Regular team availability check-ins

---

#### RISK-004: Database Performance Issues
**Category:** Technical  
**Description:** Database performance degrades as data volume increases  
**Probability:** 3 (Medium)  
**Impact:** 3 (Medium)  
**Risk Score:** 9 (Medium)  
**Owner:** Technical Lead  
**Response Strategy:** Mitigate  

**Triggers:**
- Slow query response times
- High CPU usage on database server
- User complaints about system slowness

**Response Actions:**
- Database optimization early in development
- Proper indexing strategy implementation
- Query optimization dan caching
- Performance testing dengan sample data

---

#### RISK-005: Integration Failure
**Category:** Technical  
**Description:** Modules fail to integrate properly, causing system instability  
**Probability:** 3 (Medium)  
**Impact:** 4 (High)  
**Risk Score:** 12 (High)  
**Owner:** Technical Lead  
**Response Strategy:** Mitigate  

**Triggers:**
- API compatibility issues
- Data format mismatches
- Service communication failures

**Response Actions:**
- Define clear API specifications early
- Implement integration testing from start
- Use standardized data formats
- Modular design dengan loose coupling

---

### 3.2 Medium Priority Risks

#### RISK-006: User Acceptance Issues
**Category:** Business  
**Description:** End users find system difficult to use atau not meeting expectations  
**Probability:** 2 (Low)  
**Impact:** 3 (Medium)  
**Risk Score:** 6 (Medium)  
**Owner:** Business Analyst  
**Response Strategy:** Mitigate  

**Response Actions:**
- User involvement in design process
- Usability testing with sample users
- Intuitive interface design
- Comprehensive user training materials

---

#### RISK-007: Security Vulnerabilities
**Category:** Technical  
**Description:** System contains security flaws that could compromise data  
**Probability:** 2 (Low)  
**Impact:** 4 (High)  
**Risk Score:** 8 (Medium)  
**Owner:** Technical Lead  
**Response Strategy:** Mitigate  

**Response Actions:**
- Security best practices implementation
- Input validation dan sanitization
- Regular security reviews
- Authentication dan authorization controls

---

#### RISK-008: Academic Timeline Constraints
**Category:** Academic  
**Description:** University academic calendar limits project timeline  
**Probability:** 3 (Medium)  
**Impact:** 2 (Low)  
**Risk Score:** 6 (Medium)  
**Owner:** Project Manager  
**Response Strategy:** Accept  

**Response Actions:**
- Align project schedule dengan academic calendar
- Plan buffer time untuk potential delays
- Prioritize core features over nice-to-have

---

### 3.3 Low Priority Risks

#### RISK-009: Technology Obsolescence
**Category:** Technical  
**Description:** Selected technologies become outdated during project  
**Probability:** 1 (Very Low)  
**Impact:** 2 (Low)  
**Risk Score:** 2 (Low)  
**Owner:** Technical Lead  
**Response Strategy:** Accept  

#### RISK-010: Budget Overrun
**Category:** Resource  
**Description:** Project costs exceed allocated budget  
**Probability:** 2 (Low)  
**Impact:** 2 (Low)  
**Risk Score:** 4 (Low)  
**Owner:** Project Manager  
**Response Strategy:** Mitigate  

---

## 4. RISK ANALYSIS

### 4.1 Risk Distribution by Category
**Technical Risks:** 50% (5 out of 10 risks)  
**Project Management Risks:** 20% (2 out of 10 risks)  
**Resource Risks:** 20% (2 out of 10 risks)  
**Business Risks:** 10% (1 out of 10 risks)  

### 4.2 Risk Priority Distribution
**High Priority (Score 12-25):** 3 risks (30%)  
**Medium Priority (Score 6-11):** 5 risks (50%)  
**Low Priority (Score 1-5):** 2 risks (20%)  

### 4.3 Risk Impact Analysis
**Schedule Impact:** 60% of risks could affect timeline  
**Quality Impact:** 40% of risks could affect deliverable quality  
**Scope Impact:** 30% of risks could affect project scope  
**Budget Impact:** 20% of risks could affect project costs  

### 4.4 Risk Interdependencies
```
Technical Complexity (RISK-001)
    ↓ (can trigger)
Integration Failure (RISK-005)
    ↓ (can trigger)
User Acceptance Issues (RISK-006)

Scope Creep (RISK-002)
    ↓ (can trigger)
Team Member Unavailability (RISK-003)
    ↓ (can trigger)
Academic Timeline Constraints (RISK-008)
```

---

## 5. RISK RESPONSE STRATEGIES

### 5.1 Risk Response Types

**MITIGATE (70% of risks):**
- Reduce probability atau impact of risk
- Implement preventive measures
- Most common strategy untuk technical dan project risks

**ACCEPT (20% of risks):**
- Acknowledge risk but take no preventive action
- Used untuk low-impact risks atau constraints beyond control
- Monitor untuk changes in risk profile

**TRANSFER (5% of risks):**
- Shift risk responsibility to third party
- Limited options dalam academic project context
- Consider outsourcing non-core functions

**AVOID (5% of risks):**
- Eliminate risk by changing project approach
- Remove scope elements that introduce risk
- Last resort untuk critical risks

### 5.2 Risk Response Implementation

#### High Priority Risk Responses

**RISK-001: Technical Complexity - MITIGATE**
```
Immediate Actions (Week 1-2):
- Conduct technical feasibility assessment
- Create proof-of-concept untuk critical components
- Establish technical mentoring relationships

Short-term Actions (Week 3-6):
- Implement modular architecture
- Use proven frameworks dan libraries
- Regular technical reviews dan checkpoints

Long-term Actions (Week 7-12):
- Continuous integration testing
- Performance optimization
- Documentation of technical decisions
```

**RISK-002: Scope Creep - MITIGATE**
```
Immediate Actions:
- Document detailed requirements
- Establish change control board
- Create scope management procedures

Ongoing Actions:
- Weekly scope review meetings
- Change request documentation
- Stakeholder expectation management
```

**RISK-003: Team Member Unavailability - MITIGATE**
```
Immediate Actions:
- Create team availability calendar
- Cross-train team members on multiple areas
- Document all development processes

Ongoing Actions:
- Weekly availability confirmations
- Backup assignments untuk critical tasks
- Knowledge sharing sessions
```

### 5.3 Contingency Planning

#### Fallback Plans untuk High-Impact Scenarios

**Scenario 1: Technical Lead Becomes Unavailable**
- **Primary Response:** Redistribute technical responsibilities
- **Backup Plan:** Engage external technical mentor
- **Emergency Plan:** Reduce technical scope to manageable level

**Scenario 2: Major Integration Failure**
- **Primary Response:** Implement module-by-module integration
- **Backup Plan:** Redesign integration architecture
- **Emergency Plan:** Deliver modules as standalone applications

**Scenario 3: Database Performance Crisis**
- **Primary Response:** Optimize queries dan add indexes
- **Backup Plan:** Migrate to more powerful database service
- **Emergency Plan:** Implement data archiving strategy

---

## 6. RISK MONITORING & CONTROL

### 6.1 Risk Monitoring Schedule

**Daily Monitoring:**
- Team availability dan productivity
- Technical blockers dan impediments
- Critical system performance

**Weekly Monitoring:**
- Risk trigger indicator assessment
- Scope change request review
- Resource allocation evaluation

**Bi-weekly Monitoring:**
- Complete risk register review
- Risk response effectiveness assessment
- New risk identification

**Monthly Monitoring:**
- Risk trend analysis
- Risk response strategy adjustment
- Stakeholder risk communication

### 6.2 Key Risk Indicators (KRIs)

#### Technical Risk Indicators
- **Code Complexity Metrics:** Cyclomatic complexity >10
- **Test Coverage:** <80% code coverage
- **Performance Metrics:** Response time >3 seconds
- **Integration Success Rate:** <95% successful integrations

#### Project Risk Indicators
- **Schedule Variance:** >10% behind planned schedule
- **Scope Changes:** >3 changes per week
- **Team Velocity:** <80% of planned capacity
- **Stakeholder Satisfaction:** Score <8/10

#### Resource Risk Indicators
- **Team Availability:** <90% of planned hours
- **Skill Gap Assessment:** >2 critical skill gaps
- **Workload Distribution:** >20% variance between team members
- **Knowledge Concentration:** >60% critical knowledge dengan single person

### 6.3 Risk Escalation Procedures

**Level 1 - Team Level (Self-Resolution):**
- Risk Score: 1-4 (Low Priority)
- Response Time: Within 24 hours
- Resolution Authority: Individual team members

**Level 2 - Project Manager Level:**
- Risk Score: 5-9 (Medium Priority)
- Response Time: Within 48 hours
- Resolution Authority: Project Manager dengan team consultation

**Level 3 - Academic Supervisor Level:**
- Risk Score: 10-16 (High Priority)
- Response Time: Within 72 hours
- Resolution Authority: Academic supervisor involvement required

**Level 4 - Emergency Escalation:**
- Risk Score: 17-25 (Critical)
- Response Time: Immediate
- Resolution Authority: All stakeholders involved

---

## 7. CONTINGENCY PLANS

### 7.1 Critical Path Contingencies

#### Scenario A: Development Falls Behind Schedule
**Triggers:**
- 2+ weeks behind planned milestones
- Critical features incomplete by mid-project
- Team velocity consistently <70%

**Response Plan:**
1. **Week 1:** Scope reduction - remove non-essential features
2. **Week 2:** Resource reallocation - redistribute tasks
3. **Week 3:** Extended hours approval dari academic supervisor
4. **Week 4:** Simplified implementation approach

**Minimum Viable Product (MVP) Definition:**
- CRM module dengan basic customer management
- Inventory module dengan stock tracking
- Simple dashboard dengan key metrics
- Basic reporting functionality

#### Scenario B: Technical Architecture Failure
**Triggers:**
- Major integration failures
- Performance issues cannot be resolved
- Security vulnerabilities discovered

**Response Plan:**
1. **Immediate:** Stop current development
2. **Day 1-2:** Architecture review dan redesign
3. **Day 3-5:** Proof-of-concept untuk new approach
4. **Week 2+:** Implementation dengan simplified architecture

**Simplified Architecture:**
- Monolithic application instead of microservices
- Single database with simpler schema
- Basic integration without complex workflows

#### Scenario C: Team Member Critical Absence
**Triggers:**
- Key team member unavailable >1 week
- Multiple team members unavailable simultaneously
- Critical knowledge holder becomes unavailable

**Response Plan:**
1. **Immediate:** Assess impact dan reassign urgent tasks
2. **Day 1:** Activate cross-trained backup assignments
3. **Day 2-3:** Knowledge transfer dari documentation
4. **Week 1+:** External mentoring atau support if needed

### 7.2 Quality Assurance Contingencies

#### Testing Contingency Plan
**Primary Testing Strategy:** Comprehensive testing across all modules
**Backup Strategy:** Focus on critical path testing only
**Emergency Strategy:** User acceptance testing dengan stakeholder feedback

#### Documentation Contingency Plan
**Primary Plan:** Complete technical dan user documentation
**Backup Plan:** Essential documentation only (API, user guide)
**Emergency Plan:** Video demonstrations dengan basic documentation

---

## 8. RISK COMMUNICATION

### 8.1 Communication Matrix

| **Stakeholder** | **Frequency** | **Method** | **Content** |
|-----------------|---------------|------------|-------------|
| **Team Members** | Daily | Standup meetings | Current risks, blockers |
| **Project Manager** | Weekly | Status reports | Risk register updates |
| **Academic Supervisor** | Bi-weekly | Formal reports | High-priority risks, mitigation progress |
| **SATRIAMART (Simulated)** | Monthly | Presentations | Business impact, major risks |

### 8.2 Risk Reporting Templates

#### Daily Risk Standup Template
```
Date: [Date]
Critical Risks:
- [Risk ID]: [Brief description] - [Status]
- [Risk ID]: [Brief description] - [Status]

New Risks Identified:
- [Description] - [Preliminary assessment]

Risks Resolved:
- [Risk ID]: [Description] - [Resolution summary]

Action Items:
- [Action] - [Owner] - [Due date]
```

#### Weekly Risk Report Template
```
Project: SATRIAMART SIMS
Week Ending: [Date]
Report Prepared by: [Name]

EXECUTIVE SUMMARY:
- Total active risks: [Number]
- High priority risks: [Number]
- Risks closed this week: [Number]
- New risks identified: [Number]

TOP 3 RISKS THIS WEEK:
1. [Risk description] - [Impact] - [Actions taken]
2. [Risk description] - [Impact] - [Actions taken]
3. [Risk description] - [Impact] - [Actions taken]

RISK TREND ANALYSIS:
- Overall risk level: [Increasing/Stable/Decreasing]
- Areas of concern: [List]
- Positive developments: [List]

ACTION ITEMS FOR NEXT WEEK:
- [Action] - [Owner] - [Due date]
```

### 8.3 Risk Communication Protocols

#### High-Priority Risk Communication (Score >10)
**Timeline:** Within 24 hours of identification
**Recipients:** All team members, project manager, academic supervisor
**Method:** Email + immediate verbal communication
**Content:** Risk description, immediate impact, proposed response

#### Medium-Priority Risk Communication (Score 6-10)
**Timeline:** Within 48 hours of identification
**Recipients:** Team members, project manager
**Method:** Weekly risk report + team meeting discussion
**Content:** Risk description, assessment, planned response

#### Risk Resolution Communication
**Timeline:** Within 24 hours of resolution
**Recipients:** Original risk notification recipients
**Method:** Email update + documentation update
**Content:** Resolution summary, lessons learned, preventive measures

---

## APPENDICES

### Appendix A: Risk Assessment Templates

#### Risk Identification Worksheet
```
Risk ID: RISK-XXX
Risk Title: [Descriptive title]
Category: [Technical/PM/Resource/External/Academic/Business]
Description: [Detailed description of the risk]
Cause: [What could trigger this risk]
Effect: [Impact if risk materializes]
Probability: [1-5 scale]
Impact: [1-5 scale]
Risk Score: [Probability × Impact]
Risk Owner: [Team member responsible]
Date Identified: [Date]
Status: [Open/In Progress/Closed]
```

#### Risk Response Plan Template
```
Risk ID: RISK-XXX
Response Strategy: [Mitigate/Accept/Transfer/Avoid]
Response Description: [What will be done]
Actions Required:
1. [Action] - [Owner] - [Due date]
2. [Action] - [Owner] - [Due date]
Resources Needed: [People, tools, budget]
Success Criteria: [How to measure effectiveness]
Contingency Plan: [If primary response fails]
```

### Appendix B: Lessons Learned Template

```
Project Phase: [Planning/Development/Testing/Closure]
Risk Category: [Category]
What Worked Well:
- [Successful risk management practices]

What Could Be Improved:
- [Areas for improvement]

Recommendations for Future Projects:
- [Actionable recommendations]
```

### Appendix C: Risk Register Template

| Risk ID | Title | Category | Probability | Impact | Score | Owner | Status | Response | Due Date |
|---------|-------|----------|-------------|---------|--------|--------|---------|----------|----------|
| RISK-001 | | | | | | | | | |
| RISK-002 | | | | | | | | | |

---

**Document Control:**
- **Version:** 1.0
- **Created:** Oktober 2025
- **Author:** Project Manager
- **Reviewed:** Technical Lead, Business Analyst
- **Approved:** Academic Supervisor

**Review Schedule:**
- **Weekly:** Risk register review dan updates
- **Bi-weekly:** Risk response effectiveness assessment
- **Monthly:** Complete risk management plan review

**Change History:**
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Oct 2025 | Project Manager | Initial risk management plan |

**Approval:**
- **Project Manager:** [Signature] _________________ Date: _______
- **Academic Supervisor:** [Signature] _________________ Date: _______
