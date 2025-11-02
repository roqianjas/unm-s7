# BAB IV - HASIL PENELITIAN DAN PEMBAHASAN (Bagian 4)

## 4.4 Faktor Penentu Keberhasilan

Keberhasilan implementasi Sistem Informasi CUR-HEART ditentukan oleh berbagai faktor yang saling berkaitan. Faktor-faktor ini dibagi menjadi Key Success Factors (KSF), Critical Success Factors (CSF), dan Key Performance Indicators (KPI).

### 4.4.1 Key Success Factors (KSF)

Key Success Factors adalah faktor-faktor kunci yang mendukung pencapaian tujuan proyek secara umum.

#### A. Faktor Teknologi

**1. Stabilitas dan Reliability Sistem**
- Sistem harus mampu beroperasi 24/7 dengan uptime minimal 99.5%
- Response time halaman tidak lebih dari 2 detik
- Database query optimization untuk handle concurrent users
- Backup otomatis harian untuk data security

**2. User-Friendly Interface**
- UI/UX design yang intuitif dan mudah dipahami
- Responsive design untuk semua device (desktop, tablet, mobile)
- Consistent design language menggunakan design system
- Accessibility standards (WCAG 2.1 Level AA)

**3. Keamanan Data**
- Enkripsi data sensitif (password, medical history)
- HTTPS untuk semua komunikasi
- Authentication dan authorization yang robust
- Compliance dengan UU PDP (Perlindungan Data Pribadi)
- Regular security audit dan penetration testing

**4. Scalability**
- Arsitektur yang dapat menangani pertumbuhan users
- Database normalization untuk efisiensi storage
- Caching mechanism untuk performance optimization
- Load balancing capability untuk high traffic

#### B. Faktor Manusia

**1. Kompetensi Tim Pengembang**
- Penguasaan Laravel framework dan PHP programming
- Pemahaman database design dan MySQL
- Kemampuan frontend development (HTML, CSS, JavaScript, Tailwind)
- Knowledge tentang version control (Git)
- Soft skills: komunikasi, problem-solving, teamwork

**2. Komitmen Stakeholder**
- Dukungan penuh dari manajemen CUR-HEART
- Keterlibatan aktif owner dalam requirement gathering
- Feedback konstruktif dari terapis dan admin
- Kesediaan untuk testing dan UAT (User Acceptance Testing)

**3. Adoption Rate oleh Users**
- Training yang memadai untuk terapis dan admin
- User manual yang comprehensive
- Technical support yang responsive
- Change management yang efektif

#### C. Faktor Manajemen Proyek

**1. Perencanaan yang Matang**
- Scope yang jelas dan terukur
- Timeline yang realistis (11 minggu)
- Resource allocation yang optimal
- Risk mitigation strategy yang efektif

**2. Komunikasi yang Efektif**
- Regular meeting (weekly stand-up)
- Clear documentation (technical dan user docs)
- Progress tracking dengan Gantt chart
- Issue tracking dan resolution

**3. Quality Assurance**
- Systematic testing di setiap fase (unit, integration, system, UAT)
- Code review dan peer programming
- Bug tracking dan fixing prioritization
- Continuous improvement berdasarkan feedback

#### D. Faktor Bisnis

**1. Value Proposition yang Jelas**
- Sistem memberikan value nyata untuk bisnis CUR-HEART
- ROI (Return on Investment) yang measurable
- Competitive advantage terhadap kompetitor
- Alignment dengan business goals dan strategy

**2. Market Readiness**
- Target users (clients) sudah familiar dengan digital booking
- Infrastruktur pendukung tersedia (internet, devices)
- Regulasi yang mendukung telemedicine/online therapy
- Market demand untuk layanan kesehatan mental digital

**3. Financial Sustainability**
- Budget yang adequate untuk development dan maintenance
- Revenue model yang viable (fee per booking, subscription)
- Cost efficiency dibanding manual process
- Contingency fund untuk unexpected expenses

---

**Tabel 4.32 Key Success Factors (KSF) Categorization**

| Category | KSF | Sub-Factors | Importance | Measurement |
|----------|-----|-------------|------------|-------------|
| **Technology** | Stabilitas Sistem | • Uptime ≥ 99.5%<br>• Response time < 2s<br>• DB optimization<br>• Daily backup | Critical | Uptime monitoring, Performance metrics |
| | User-Friendly Interface | • Intuitive UI/UX<br>• Responsive design<br>• Consistent design system<br>• WCAG 2.1 AA | High | SUS score ≥ 68, User testing |
| | Keamanan Data | • Encryption (bcrypt, AES-256)<br>• HTTPS<br>• RBAC<br>• UU PDP compliance | Critical | Security audit, Zero breaches |
| | Scalability | • Handle growth<br>• DB normalization<br>• Caching<br>• Load balancing | Medium | Load testing, Concurrent users |
| **Human** | Kompetensi Tim | • Laravel/PHP expertise<br>• DB design<br>• Frontend skills<br>• Git proficiency | High | Code quality, Delivery speed |
| | Komitmen Stakeholder | • Management support<br>• Active involvement<br>• Constructive feedback<br>• UAT participation | High | Stakeholder engagement score |
| | User Adoption | • Adequate training<br>• Comprehensive manual<br>• Responsive support<br>• Change management | Critical | Adoption rate ≥ 70% |
| **Project Mgmt** | Perencanaan Matang | • Clear scope<br>• Realistic timeline (11w)<br>• Optimal resources<br>• Risk mitigation | High | On-time delivery, Budget adherence |
| | Komunikasi Efektif | • Weekly meetings<br>• Clear docs<br>• Progress tracking<br>• Issue resolution | High | Communication frequency, Response time |
| | Quality Assurance | • Systematic testing<br>• Code review<br>• Bug tracking<br>• Continuous improvement | Critical | Test coverage ≥ 70%, Bug density |
| **Business** | Value Proposition | • Clear business value<br>• Measurable ROI<br>• Competitive advantage<br>• Goal alignment | Critical | ROI ≥ 200%, Efficiency gain ≥ 40% |
| | Market Readiness | • Digital familiarity<br>• Infrastructure available<br>• Regulatory support<br>• Market demand | Medium | Market research, User survey |
| | Financial Sustainability | • Adequate budget<br>• Viable revenue model<br>• Cost efficiency<br>• Contingency fund | High | Budget variance < 10%, Break-even analysis |

**KSF Priorities:**
- Critical: 5 factors (Stabilitas, Keamanan, Adoption, QA, Value)
- High: 6 factors (UI/UX, Kompetensi, Komitmen, Perencanaan, Komunikasi, Financial)
- Medium: 2 factors (Scalability, Market Readiness)

---

### 4.4.2 Critical Success Factors (CSF)

Critical Success Factors adalah faktor-faktor kritis yang **harus** dipenuhi agar proyek berhasil. Jika salah satu CSF tidak terpenuhi, proyek akan gagal.

#### CSF 1: Availability dan Reliability Sistem

**Definisi:**
Sistem harus dapat diakses kapan saja oleh users dengan tingkat ketersediaan minimal 99.5% (uptime) dan mampu menangani beban users secara concurrent tanpa downtime.

**Indikator Keberhasilan:**
- Uptime ≥ 99.5% (maksimal 3.6 jam downtime per bulan)
- Maximum response time: 2 detik untuk halaman standar
- Dapat menangani minimal 100 concurrent users
- Zero data loss dalam kondisi normal

**Strategi Pencapaian:**
- Hosting pada server yang reliable (VPS dengan SLA 99.9%)
- Implementasi database indexing untuk query optimization
- Caching menggunakan Laravel Cache
- Regular monitoring menggunakan uptime monitoring tools
- Automated backup daily dengan retention 30 hari

**Risiko Jika Tidak Terpenuhi:**
- Users frustasi karena sistem sering down
- Loss of credibility dan trust
- Potential revenue loss
- Negative reviews dan word-of-mouth

---

#### CSF 2: Data Security dan Privacy

**Definisi:**
Sistem harus menjamin keamanan dan kerahasiaan data users, terutama data sensitif seperti medical history, session notes, dan payment information. Compliance dengan UU PDP dan standar keamanan internasional.

**Indikator Keberhasilan:**
- Zero data breach atau unauthorized access
- Semua data sensitif ter-enkripsi (password dengan bcrypt, medical data dengan AES-256)
- HTTPS implementation untuk semua pages
- Role-based access control (RBAC) berfungsi dengan baik
- Regular security audit menunjukkan no critical vulnerabilities

**Strategi Pencapaian:**
- Menggunakan Laravel's built-in security features:
  - CSRF protection
  - XSS prevention
  - SQL injection prevention (Eloquent ORM)
  - Password hashing dengan bcrypt
- Input validation dan sanitization
- Implementasi Laravel Sanctum untuk API authentication
- Regular security updates dan patches
- Data encryption at rest dan in transit
- Security audit sebelum production deployment

**Risiko Jika Tidak Terpenuhi:**
- Legal liability (pelanggaran UU PDP, denda hingga Rp 5 miliar)
- Loss of client trust dan reputasi
- Potential lawsuits dari affected users
- Business closure risk

---

#### CSF 3: User Adoption dan Satisfaction

**Definisi:**
Sistem harus diadopsi dan digunakan secara aktif oleh target users (clients, therapists, admin) dengan tingkat kepuasan yang tinggi.

**Indikator Keberhasilan:**
- Minimal 70% clients menggunakan sistem untuk booking (vs. manual/phone)
- User satisfaction score ≥ 4.0 dari 5.0 (via survey)
- System Usability Scale (SUS) score ≥ 68 (above average)
- Therapist adoption rate 100% (mandatory usage)
- Return user rate ≥ 60% dalam 3 bulan pertama

**Strategi Pencapaian:**
- UI/UX design yang user-friendly dan intuitive
- Comprehensive onboarding dan training:
  - Video tutorial untuk clients
  - In-person training untuk therapists dan admin
  - User manual dalam Bahasa Indonesia
- Responsive customer support:
  - FAQ page yang comprehensive
  - Live chat atau WhatsApp support
  - Email support dengan SLA 24 jam response
- Continuous improvement berdasarkan user feedback:
  - Survey setelah setiap booking
  - Feedback form accessible
  - Regular update dan bug fixes

**Risiko Jika Tidak Terpenuhi:**
- Sistem tidak digunakan (project failure)
- Wasted investment (Rp 5 juta budget)
- Resistance to change dari staff
- Continuation of inefficient manual processes

---

#### CSF 4: Integration dengan Business Process

**Definisi:**
Sistem harus terintegrasi dengan seamless ke dalam business process yang sudah ada di CUR-HEART, tidak mengganggu operasional, dan meningkatkan efisiensi.

**Indikator Keberhasilan:**
- 100% booking melalui sistem (tidak ada lagi manual booking via spreadsheet)
- Pengurangan administrative workload minimal 50%
- Reduction dalam booking errors (double booking, miscommunication) hingga 90%
- Financial reporting dapat di-generate dalam 5 menit (vs. 2 jam manual)

**Strategi Pencapaian:**
- Requirement gathering yang mendalam dengan stakeholders
- Business Process Reengineering (BPR) jika diperlukan
- Change management strategy:
  - Komunikasi early tentang perubahan
  - Involvement stakeholders dalam design phase
  - Gradual rollout (pilot → full deployment)
- Standard Operating Procedure (SOP) baru yang documented
- Regular review dan adjustment berdasarkan feedback

**Risiko Jika Tidak Terpenuhi:**
- Workflow disruption
- Dual system burden (manual + digital)
- Staff frustration dan resistance
- Business process inefficiency continues

---

#### CSF 5: Budget dan Timeline Adherence

**Definisi:**
Proyek harus diselesaikan dalam waktu 11 minggu dengan budget Rp 5,000,000 tanpa major overruns.

**Indikator Keberhasilan:**
- Project completion dalam 11 minggu (± 1 minggu tolerance)
- Actual cost tidak melebihi budget 110% (Rp 5,5 juta)
- All deliverables completed sesuai scope
- No major scope creep

**Strategi Pencapaian:**
- Detail project planning dengan WBS dan Gantt Chart
- Weekly progress tracking dan status reporting
- Scope management yang ketat (formalized change request process)
- Resource optimization:
  - Leverage open-source tools dan libraries
  - In-house development vs. outsourcing
  - Cloud hosting dengan predictable pricing
- Risk buffer dalam timeline (10%) dan budget (10%)

**Risiko Jika Tidak Terpenuhi:**
- Project cancellation jika budget overrun significant
- Delayed go-live → missed business opportunities
- Stakeholder dissatisfaction
- Incomplete features → system not usable

---

**Tabel 4.33 Critical Success Factors (CSF) dengan Indicators**

| CSF ID | Critical Success Factor | Success Indicator | Target Value | Measurement Method | Monitoring Frequency | Risk If Not Met | Mitigation Strategy |
|--------|------------------------|-------------------|--------------|-------------------|---------------------|----------------|---------------------|
| CSF-01 | Availability & Reliability Sistem | System uptime | ≥ 99.5% | UptimeRobot monitoring | Real-time (24/7) | User frustration, Revenue loss | • Reliable hosting (SLA 99.9%)<br>• Daily backup<br>• Monitoring alerts |
| | | Response time | < 2s per page | GTmetrix, Lighthouse | Weekly | Poor UX, High bounce | • Query optimization<br>• Caching (Redis)<br>• CDN usage |
| | | Concurrent users | ≥ 100 users | Load testing (Apache JMeter) | Pre-launch, Monthly | System crash | • Proper indexing<br>• Connection pooling<br>• Horizontal scaling |
| | | Data integrity | Zero data loss | Database audit, Backup verification | Daily | Critical failure | • Automated backup<br>• Transaction management<br>• Validation rules |
| CSF-02 | Data Security & Privacy | Data breach incidents | Zero breaches | Security audit, Incident logs | Continuous | Legal liability (Rp 5M fine) | • Encryption (bcrypt, AES-256)<br>• HTTPS<br>• Security audit |
| | | Encryption coverage | 100% sensitive data | Code review | Pre-deployment | Trust loss, Lawsuits | • Laravel security features<br>• Input validation<br>• OWASP compliance |
| | | RBAC implementation | 100% functional | Access testing | Weekly | Unauthorized access | • Role middleware<br>• Permission gates<br>• Audit trail |
| | | Security vulnerabilities | No critical/high | OWASP ZAP scan | Bi-weekly | Data breach risk | • Regular updates<br>• Penetration testing<br>• Security patches |
| CSF-03 | User Adoption & Satisfaction | Client adoption rate | ≥ 70% | Booking analytics | Monthly | Project failure | • Training program<br>• User manual<br>• Support system |
| | | SUS score | ≥ 68 (above avg) | SUS questionnaire (10 users) | Post-UAT, Quarterly | Low satisfaction | • Usability testing<br>• Iterative improvement<br>• User feedback |
| | | User satisfaction | ≥ 4.0/5.0 | Post-booking survey | Per booking | Negative reviews | • Responsive support<br>• Bug fixes<br>• Feature requests |
| | | Therapist adoption | 100% (mandatory) | Usage logs | Weekly | Workflow disruption | • Mandatory training<br>• Admin enforcement<br>• Incentives |
| | | Return user rate | ≥ 60% in 3 months | User analytics | Monthly | One-time use only | • Email reminders<br>• Loyalty program<br>• UX improvement |
| CSF-04 | Integration dengan Business Process | Booking via system | 100% (no manual) | Booking source tracking | Daily | Dual system burden | • Mandatory policy<br>• Disable manual process<br>• Training |
| | | Admin workload reduction | ≥ 50% | Time tracking study | Before/After comparison | No efficiency gain | • Process automation<br>• Workflow optimization<br>• Role distribution |
| | | Booking error reduction | ≥ 90% | Error logs comparison | Monthly | Continued inefficiency | • Validation rules<br>• Conflict checking<br>• Clear UI |
| | | Report generation time | ≤ 5 minutes | Time measurement | Weekly | Slow decision making | • Database indexes<br>• Cached reports<br>• Query optimization |
| CSF-05 | Budget & Timeline Adherence | Project completion | 11 weeks ± 1 week | Project timeline tracking | Weekly | Delayed benefits | • Buffer time (10%)<br>• Risk management<br>• Weekly monitoring |
| | | Budget variance | ≤ 10% over | Cost tracking | Monthly | Project cancellation | • Contingency fund (20%)<br>• Cost control<br>• Free alternatives |
| | | Scope completion | 95%+ requirements | Requirements checklist | Per sprint | Unusable system | • MoSCoW prioritization<br>• Scope freeze<br>• Change control |
| | | Scope creep incidents | ≤ 3 major changes | Change request log | Ongoing | Timeline delay | • Formalized change process<br>• Impact analysis<br>• Defer to Phase 2 |

**CSF Achievement Status (as of Nov 2024):**
- CSF-01: ⏳ 70% (System stable, performance good, need production testing)
- CSF-02: ✅ 90% (Security implemented, pending final audit)
- CSF-03: 🔜 30% (Awaiting UAT and deployment for user testing)
- CSF-04: ⏳ 50% (Integration designed, need implementation)
- CSF-05: ✅ 85% (On track - Week 7 of 11, budget 65% spent)

---

### 4.4.3 Key Performance Indicators (KPI)

KPI adalah metrik terukur yang digunakan untuk monitor dan evaluate keberhasilan sistem setelah deployment.

---

**[GAMBAR 4.65 - KPI Dashboard Metrics Visualization]** 📊
_Real-time dashboard showing system performance, user adoption, revenue, and satisfaction metrics_

---

**Tabel 4.34 Key Performance Indicators (KPI) - Technical Metrics**

| KPI Category | KPI Name | Definition | Target Value | Baseline (Current) | Measurement Method | Measurement Tool | Frequency | Owner | Action If Below Target |
|--------------|----------|------------|--------------|-------------------|-------------------|------------------|-----------|-------|----------------------|
| **System Performance** | System Uptime | Percentage of time system is operational | ≥ 99.5% | N/A (New system) | (Total uptime / Total time) × 100% | UptimeRobot, Pingdom | Real-time, monthly report | DevOps Team | • Check server logs<br>• Scale resources<br>• Implement redundancy |
| | Average Response Time | Average page load time | ≤ 2 seconds | N/A | Page load time measurement | Google PageSpeed Insights, GTmetrix | Weekly | Backend Team | • Optimize queries<br>• Enable caching<br>• CDN implementation |
| | Database Query Time | Average database query execution time | ≤ 100ms | N/A | Query execution time tracking | Laravel Debugbar, MySQL slow query log | Weekly | Database Admin | • Add indexes<br>• Optimize queries<br>• Database tuning |
| | Error Rate | Percentage of requests resulting in errors | ≤ 0.5% | N/A | (Error requests / Total requests) × 100% | Laravel logs, Sentry | Daily | Full-stack Team | • Debug errors<br>• Fix bugs<br>• Improve error handling |
| | Concurrent Users Capacity | Maximum simultaneous users supported | ≥ 100 users | N/A | Load testing simulation | Apache JMeter, LoadRunner | Pre-launch, Quarterly | DevOps Team | • Optimize connection pool<br>• Scale infrastructure<br>• Load balancing |
| | API Response Time | Average API endpoint response time | ≤ 500ms | N/A | API performance monitoring | Postman, New Relic | Weekly | Backend Team | • Optimize endpoints<br>• Reduce payload size<br>• Implement pagination |
| **System Security** | Security Vulnerabilities | Number of identified security issues | 0 critical, ≤ 2 high | N/A | Automated security scanning | OWASP ZAP, Nessus | Monthly | Security Team | • Patch vulnerabilities<br>• Update dependencies<br>• Security audit |
| | Data Breach Incidents | Number of unauthorized data access events | 0 incidents | N/A | Security audit & incident logs | Audit trail, IDS | Real-time | Security Team | • Incident response<br>• Forensic analysis<br>• Strengthen security |
| | Failed Login Attempts | Percentage of failed login attempts | ≤ 5% | N/A | (Failed logins / Total login attempts) × 100% | Laravel auth logs | Daily | Security Team | • Check for brute force<br>• Implement CAPTCHA<br>• Rate limiting |
| | SSL Certificate Validity | SSL certificate expiration status | Always valid (>30 days) | N/A | Certificate expiration check | SSL Labs, Let's Encrypt | Automated (alert) | DevOps Team | • Renew certificate<br>• Auto-renewal setup<br>• Backup cert |
| | Password Strength Compliance | Percentage of users with strong passwords | ≥ 95% | N/A | Password policy validation | Custom Laravel validator | Monthly | Backend Team | • Enforce policy<br>• Password reset<br>• User education |
| **System Quality** | Code Test Coverage | Percentage of code covered by tests | ≥ 70% | 65% | (Lines tested / Total lines) × 100% | PHPUnit, Jest | Per commit | Development Team | • Write more tests<br>• Increase coverage<br>• TDD approach |
| | Code Quality Score | SonarQube quality gate status | A rating | B rating | Static code analysis | SonarQube, PHPStan | Per commit | Development Team | • Refactor code<br>• Fix code smells<br>• Follow standards |
| | Documentation Coverage | Percentage of code with documentation | ≥ 80% | 50% | Doc comment analysis | PHPDocumentor | Monthly | Development Team | • Add docblocks<br>• Update README<br>• API documentation |

**Summary of Technical KPIs:**
- Total Technical KPIs: 14
- Focus Areas: Performance (6), Security (5), Quality (3)
- Critical KPIs: Uptime, Response Time, Security Vulnerabilities, Data Breach
- Measurement Tools: 12 tools (mix of free and commercial)

---

**Tabel 4.35 Key Performance Indicators (KPI) - Business & User Metrics**

| KPI Category | KPI Name | Definition | Target Value | Baseline (Current) | Measurement Method | Data Source | Frequency | Owner | Action If Below Target |
|--------------|----------|------------|--------------|-------------------|-------------------|-------------|-----------|-------|----------------------|
| **User Adoption** | Total Registered Users | Cumulative number of registered users | 200 in 3 months | 0 | COUNT(users) | users table | Monthly | Marketing Team | • Marketing campaign<br>• Referral program<br>• Social media ads |
| | Active Users (MAU) | Users who logged in past 30 days | 150 users (75%) | N/A | COUNT(DISTINCT user_id) WHERE login >= NOW() - 30 days | activity_logs | Monthly | Product Team | • Re-engagement email<br>• Push notifications<br>• Feature highlights |
| | Booking Conversion Rate | Percentage of started bookings completed | ≥ 60% | 40% (manual) | (Completed bookings / Booking attempts) × 100% | bookings table | Weekly | Product Team | • Simplify flow<br>• Reduce steps<br>• Improve UX |
| | Therapist Utilization Rate | Percentage of therapist slots booked | ≥ 80% | 60% (manual) | (Booked slots / Available slots) × 100% | bookings, availability | Weekly | Operations Team | • Marketing to clients<br>• Dynamic pricing<br>• Optimize schedule |
| | User Retention Rate (3-month) | Percentage of users returning after 3 months | ≥ 60% | 35% (estimate) | (Active users month 4 / New users month 1) × 100% | users, bookings | Quarterly | Product Team | • Loyalty program<br>• Email reminders<br>• Personalization |
| | New vs Returning Users | Ratio of new to returning users | 40:60 | 70:30 | Segment users by first_booking_date | bookings | Monthly | Marketing Team | • Improve retention<br>• Referral incentives<br>• Quality service |
| **Transaction** | Total Bookings per Month | Number of bookings completed monthly | 100 bookings | 80 (manual) | COUNT(bookings) WHERE status = 'completed' | bookings | Monthly | Operations Team | • Promotional campaigns<br>• Add therapists<br>• Extend hours |
| | Payment Success Rate | Percentage of successful payments | ≥ 95% | 90% (manual) | (Successful payments / Payment attempts) × 100% | payments | Weekly | Finance Team | • Multiple payment methods<br>• Payment support<br>• Clear instructions |
| | Booking Cancellation Rate | Percentage of bookings cancelled | ≤ 10% | 15% (manual) | (Cancelled bookings / Total bookings) × 100% | bookings | Monthly | Operations Team | • Reminder system<br>• Cancellation policy<br>• Rescheduling ease |
| | Average Booking Value | Average revenue per booking | Rp 300,000 | Rp 250,000 | SUM(booking_amount) / COUNT(bookings) | payments | Monthly | Finance Team | • Upsell services<br>• Package deals<br>• Premium sessions |
| | Revenue per Month | Total monthly revenue from bookings | Rp 30,000,000 | Rp 20,000,000 | SUM(amount) WHERE status = 'paid' | payments | Monthly | Finance Team | • Increase bookings<br>• Price optimization<br>• New services |
| | Average Revenue per User | Lifetime value per user | Rp 900,000 | Rp 750,000 | SUM(payments) / COUNT(DISTINCT users) | payments | Quarterly | Finance Team | • Increase frequency<br>• Package sales<br>• Membership |
| **Customer Satisfaction** | User Satisfaction Score | Average post-booking satisfaction rating | ≥ 4.0/5.0 | 3.8/5.0 | AVG(satisfaction_rating) | feedback | Per booking | Customer Service | • Collect feedback<br>• Improve service<br>• Resolve issues |
| | Net Promoter Score (NPS) | Likelihood to recommend (0-10 scale) | ≥ 30 | 15 (manual) | % Promoters (9-10) - % Detractors (0-6) | surveys | Quarterly | Marketing Team | • Address detractors<br>• Improve experience<br>• Highlight strengths |
| | System Usability Scale (SUS) | Standard usability score | ≥ 68 (above avg) | N/A | SUS questionnaire (10 questions) | UAT surveys | Post-UAT, Quarterly | Product Team | • Usability testing<br>• UI/UX improvements<br>• User testing |
| | Average Session Rating | Average therapist session rating | ≥ 4.5/5.0 | 4.3/5.0 | AVG(session_rating) | session_notes | Per session | Operations Team | • Therapist training<br>• Quality control<br>• Feedback loop |
| | Response Rate to Feedback | Percentage of user feedback addressed | ≥ 90% | 60% | (Responded feedback / Total feedback) × 100% | feedback | Weekly | Customer Service | • Dedicated team<br>• SLA for response<br>• Automated responses |

**Summary of Business KPIs:**
- Total Business KPIs: 17
- Focus Areas: Adoption (6), Transaction (6), Satisfaction (5)
- Revenue Target: Rp 30M/month (50% increase from baseline)
- User Target: 200 users in 3 months, 80% therapist utilization

---

**Tabel 4.36 Key Performance Indicators (KPI) - Operational Metrics**

| KPI Category | KPI Name | Definition | Target Value | Baseline (Current) | Measurement Method | Data Source | Frequency | Owner | Action If Below Target |
|--------------|----------|------------|--------------|-------------------|-------------------|-------------|-----------|-------|----------------------|
| **Process Efficiency** | Average Booking Time | Time from start to complete booking | ≤ 3 minutes | 12 minutes (manual) | AVG(completion_time - start_time) | booking_logs | Weekly | Product Team | • Simplify flow<br>• Reduce fields<br>• Auto-fill data |
| | Admin Booking Processing Time | Time to process/approve booking | ≤ 5 minutes | 15 minutes (manual) | AVG(approval_time - submission_time) | bookings | Monthly | Operations Team | • Automate approval<br>• Clear workflow<br>• Admin training |
| | Payment Verification Time | Time to verify and confirm payment | ≤ 30 minutes | 2-4 hours (manual) | AVG(verified_at - payment_at) | payments | Weekly | Finance Team | • Automated verification<br>• Payment gateway<br>• Real-time alerts |
| | Report Generation Time | Time to generate business reports | ≤ 5 minutes | 2 hours (manual) | Time measurement | reporting system | Monthly | IT Team | • Optimize queries<br>• Cached reports<br>• Better indexing |
| | Schedule Conflict Resolution | Time to resolve scheduling conflicts | ≤ 10 minutes | 30-60 minutes | AVG(resolution_time) | conflict_logs | Weekly | Operations Team | • Auto-detection<br>• Clear rules<br>• Quick resolution UI |
| **Support & Maintenance** | Average Support Response Time | Time to first response on support ticket | ≤ 2 hours | N/A | AVG(first_response_at - created_at) | support_tickets | Weekly | Customer Service | • Increase staff<br>• Auto-responses<br>• Knowledge base |
| | Support Ticket Resolution Time | Average time to close support ticket | ≤ 24 hours | N/A | AVG(resolved_at - created_at) | support_tickets | Weekly | Customer Service | • Better training<br>• Escalation process<br>• FAQ/documentation |
| | First Contact Resolution Rate | Percentage resolved in first contact | ≥ 70% | N/A | (Resolved in 1 contact / Total tickets) × 100% | support_tickets | Monthly | Customer Service | • Improve training<br>• Better tools<br>• Knowledge base |
| | System Bug Resolution Time | Average time to fix reported bugs | ≤ 48 hours (critical) | N/A | AVG(resolved_at - reported_at) by priority | issue_tracker | Weekly | Development Team | • Prioritize bugs<br>• More developers<br>• Better testing |
| **Resource Utilization** | Therapist Average Capacity | Average sessions per therapist per week | ≥ 20 sessions | 15 sessions | AVG(COUNT(sessions) per therapist) | bookings | Weekly | Operations Team | • Marketing<br>• Optimize availability<br>• Hire more |
| | Admin Workload Reduction | Percentage reduction in admin hours | ≥ 50% | 0% (baseline) | (Old hours - New hours) / Old hours × 100% | Time tracking | Monthly | Management | • More automation<br>• Process improvement<br>• Training |
| | Database Storage Growth | Monthly storage growth rate | ≤ 5% per month | N/A | (Current size - Last month size) / Last month × 100% | Database metrics | Monthly | Database Admin | • Data archiving<br>• Cleanup old data<br>• Optimize storage |
| | Backup Success Rate | Percentage of successful backups | 100% | N/A | (Successful backups / Total backup attempts) × 100% | Backup logs | Daily | DevOps Team | • Fix backup script<br>• Check storage<br>• Alert system |
| **Business Intelligence** | Report Accuracy | Accuracy of automated reports vs manual | ≥ 99% | N/A | Manual audit of sample reports | Report audits | Monthly | Data Analyst | • Fix calculation<br>• Validate logic<br>• Data quality check |
| | Dashboard Load Time | Time to load main dashboard | ≤ 3 seconds | N/A | Page load time measurement | Performance monitor | Weekly | Frontend Team | • Optimize queries<br>• Lazy loading<br>• Caching |
| | Data Freshness | Maximum age of data in reports | ≤ 1 hour | N/A | Check last_updated timestamp | Reporting system | Real-time | Data Team | • Reduce refresh interval<br>• Real-time updates<br>• Event-driven |

**Summary of Operational KPIs:**
- Total Operational KPIs: 16
- Focus Areas: Process Efficiency (5), Support (4), Resource Utilization (4), Business Intelligence (3)
- Key Targets: 75% time reduction (booking), 50% admin workload reduction
- Efficiency Gains: 12 min → 3 min (booking), 2 hours → 5 min (reports)

---

**KPI Dashboard & Monitoring Strategy:**

| Dashboard Type | Refresh Rate | Users | Key Metrics Displayed |
|----------------|--------------|-------|----------------------|
| Executive Dashboard | Daily | Management, Owner | Revenue, bookings, user growth, NPS, ROI |
| Operations Dashboard | Real-time | Admin, Operations Team | Active bookings, therapist schedule, pending payments, support tickets |
| Technical Dashboard | Real-time | IT Team, DevOps | Uptime, response time, error rate, server load |
| Marketing Dashboard | Weekly | Marketing Team | User acquisition, conversion rate, MAU, referral rate |
| Finance Dashboard | Daily | Finance Team | Revenue, payment success rate, average booking value, outstanding payments |

---

---

## 4.5 Keuntungan yang Diharapkan

Implementasi Sistem Informasi CUR-HEART diharapkan memberikan berbagai keuntungan bagi stakeholders yang terlibat.

### 4.5.1 Manfaat untuk CUR-HEART (Business)

---

**Tabel 4.37 Benefits Analysis - CUR-HEART (Organization)**

| Benefit Category | Specific Benefit | Before System (Baseline) | After System (Target) | Quantified Impact | Timeframe | Measurement Method | Strategic Value |
|------------------|-----------------|-------------------------|---------------------|------------------|-----------|-------------------|----------------|
| **Operational Efficiency** | Automated booking process | Manual booking (10-15 min/booking) | Automated booking (3 min/booking) | • Time saving: 12 min × 100 bookings = 20 hrs/month<br>• Cost saving: Rp 500,000/month<br>• **Annual: Rp 6,000,000** | Immediate | Time tracking, cost analysis | HIGH - Reduces admin burden, allows focus on strategic tasks |
| | Scheduling management | 5 hrs/week coordination | 1 hr/week coordination | • Time saving: 16 hrs/month<br>• Better resource utilization: 60% → 80%<br>• Cost saving: Rp 400,000/month | Month 1 | Time logs, utilization rate | HIGH - Improves therapist productivity, reduces conflicts |
| | Automated reporting | 2 hrs/report manual | 5 minutes automated | • Time saving: 8 hrs/month<br>• Cost saving: Rp 200,000/month<br>• **Annual: Rp 2,400,000** | Month 2 | Report generation time | MEDIUM - Enables data-driven decisions, faster insights |
| | Eliminated double booking | 2-3 incidents/month | 0 incidents | • Prevented conflicts: 100%<br>• Client satisfaction improvement<br>• No compensation costs | Immediate | Incident logs | HIGH - Protects reputation, improves reliability |
| | Payment processing | Manual verification (2-4 hrs) | Automated (30 min) | • Time saving: 10 hrs/month<br>• Faster cash flow<br>• Reduced errors: 90% | Month 1 | Processing time, error rate | MEDIUM - Improves cash flow, reduces finance workload |
| **Revenue Growth** | Increased booking volume | 80 bookings/month | 100 bookings/month (25% increase) | • Additional revenue: 20 × Rp 300,000<br>• **Rp 6M/month = Rp 72M/year** | Month 3-6 | Booking count, revenue tracking | CRITICAL - Direct revenue impact, business growth |
| | Reduced no-shows | 15% no-show rate (12/month) | 5% no-show rate (4/month) | • Prevented no-shows: 8 bookings<br>• **Recovered revenue: Rp 2.4M/month = Rp 28.8M/year** | Month 2 | No-show rate tracking | HIGH - Maximizes revenue from capacity |
| | Upselling opportunities | Limited visibility | Automated recommendations | • 20% book additional sessions<br>• 10% upgrade to packages<br>• **Additional: Rp 5M/year** | Month 6 | Conversion tracking | MEDIUM - Increases customer lifetime value |
| | Extended service hours | 08:00-17:00 (9 hrs) | 24/7 booking availability | • Capture after-hours bookings: 15%<br>• **Additional: Rp 10M/year** | Immediate | Booking time analysis | HIGH - Captures previously lost opportunities |
| **Quality & Service** | Data-driven decision making | Manual analysis, delayed | Real-time dashboards | • Faster decisions (days → hours)<br>• Better insights<br>• Trend identification | Month 2 | Decision turnaround time | HIGH - Competitive advantage, strategic planning |
| | Service quality monitoring | Limited feedback (informal) | Systematic feedback & ratings | • 100% feedback capture<br>• SUS score: 68+<br>• NPS: 30+ | Month 3 | Survey response rate, scores | HIGH - Continuous improvement, quality assurance |
| | Client retention | 35% return rate (estimate) | 60% return rate (target) | • Increased loyalty<br>• Higher lifetime value<br>• Word-of-mouth marketing | Month 6 | Retention rate calculation | CRITICAL - Sustainable business growth |
| | Brand reputation | Word-of-mouth only | Digital presence + reviews | • Professional image<br>• Positive online reviews<br>• Social proof | Month 3 | Online reviews, rating | HIGH - Market positioning, trust building |
| **Scalability** | Business expansion | Limited by manual capacity | Scalable digital system | • Support 5× growth without proportional staff increase<br>• Multiple location readiness | Year 1-2 | Growth capacity analysis | CRITICAL - Long-term business strategy |
| | Data analytics capability | Basic Excel reports | Advanced BI & analytics | • Predictive insights<br>• Pattern recognition<br>• ROI tracking | Month 3 | Analytics usage, insight quality | MEDIUM - Strategic decision support |
| **Risk Mitigation** | Data backup & recovery | Manual, inconsistent | Automated daily backup | • Zero data loss risk<br>• Business continuity<br>• Disaster recovery ready | Immediate | Backup success rate (100%) | HIGH - Protects business assets |
| | Compliance & audit | Manual record keeping | Digital audit trail | • Easy compliance reporting<br>• Full traceability<br>• Legal protection | Immediate | Audit trail completeness | MEDIUM - Legal & regulatory compliance |
| **Cost Savings** | Reduced admin workload | 100% manual processing | 50% workload reduction | • Free up 50% admin time<br>• Reallocate to growth activities<br>• **Cost avoidance: Rp 10M/year** | Month 2 | Workload tracking | HIGH - Operational cost optimization |
| | Error-related costs | Human errors (typos, double booking) | System validation | • Error reduction: 95%<br>• Compensation costs: Rp 0<br>• Customer service time: 70% reduction | Month 1 | Error incident tracking | MEDIUM - Protects margins, improves service |

**Total Quantified Annual Benefits for CUR-HEART:**
- Direct Revenue Increase: Rp 115.8M/year (Rp 72M + Rp 28.8M + Rp 5M + Rp 10M)
- Cost Savings: Rp 18.4M/year (Rp 6M + Rp 2.4M + Rp 10M)
- **TOTAL ANNUAL BENEFIT: Rp 134.2M/year**
- **ROI on Investment (Rp 5M)**: 2,584% over 1 year

**Non-Quantified Strategic Benefits:**
- Enhanced brand reputation and market positioning
- Scalability for future growth (multi-location expansion)
- Data-driven decision-making capability
- Competitive advantage in digital transformation
- Improved client and therapist satisfaction leading to retention

---

### 4.5.2 Manfaat untuk Clients (Klien)

---

**Tabel 4.38 Benefits Analysis - Clients (End Users)**

| Benefit Category | Specific Benefit | Pain Point Addressed | Solution Provided | User Impact | Value Proposition | Satisfaction Metric | Priority |
|------------------|-----------------|---------------------|------------------|-------------|------------------|-------------------|----------|
| **Convenience & Accessibility** | 24/7 booking availability | Limited to office hours (08:00-17:00) | Book anytime, anywhere via web | • No need to wait for office hours<br>• Book during convenient time<br>• Instant confirmation | Time flexibility, immediate access | Booking completion rate: 90% | CRITICAL |
| | No phone call required | Need to call and wait | Self-service online booking | • No waiting on hold<br>• Avoid phone anxiety<br>• Can multitask | Convenience, autonomy | User preference: 85% prefer online | HIGH |
| | Mobile-friendly interface | Desktop-only alternatives | Responsive design, mobile-first | • Book on-the-go<br>• Check appointments anywhere<br>• Quick access | Mobile convenience | Mobile usage: 70% of bookings | HIGH |
| | Easy rescheduling | Manual coordination required | One-click reschedule (within policy) | • No admin dependency<br>• Immediate update<br>• Penalty-free if early | Flexibility, control | Rescheduling satisfaction: 4.5/5 | HIGH |
| | Instant confirmation | Wait for admin confirmation (2-4 hrs) | Real-time booking confirmation | • Peace of mind<br>• No anxiety waiting<br>• Can plan immediately | Certainty, trust | Confirmation speed satisfaction: 4.8/5 | HIGH |
| **Transparency & Information** | Therapist profiles | Limited information pre-booking | Detailed profiles (education, specializations, reviews) | • Informed choice<br>• Match with preferences<br>• Build trust | Confidence, trust | Profile view rate: 95% before booking | CRITICAL |
| | Real-time availability | Call to check availability | Visual calendar with open slots | • See all options at once<br>• Compare times<br>• Plan flexible | Transparency, efficiency | Calendar interaction: 90% users | HIGH |
| | Clear pricing | Ambiguous pricing, call to ask | Transparent pricing per service | • No surprises<br>• Budget planning<br>• Compare options | Financial clarity | Pricing clarity rating: 4.6/5 | HIGH |
| | Therapist ratings & reviews | No peer feedback available | Rating system (1-5 stars) + written reviews | • Social proof<br>• Quality assurance<br>• Confidence building | Trust, validation | Review influence: 80% read before booking | HIGH |
| | Service descriptions | Vague service info | Comprehensive service details | • Understand what to expect<br>• Choose right service<br>• Avoid misunderstanding | Clarity, expectation management | Service clarity rating: 4.4/5 | MEDIUM |
| **Self-Service Management** | Appointment history | Manual record-keeping | Digital record of all bookings | • No need to remember<br>• Easy reference<br>• Track frequency | Organization, convenience | History usage: 60% users | MEDIUM |
| | Session notes access | No access to notes | View shared session notes | • Understand progress<br>• Remember insights<br>• Continuity | Transparency, involvement | Notes access satisfaction: 4.3/5 | MEDIUM |
| | Payment history | Manual receipts | Digital payment records | • Tax purposes<br>• Expense tracking<br>• Easy retrieval | Financial management | Payment history usage: 70% users | MEDIUM |
| | Profile management | Repeated form-filling | Persistent profile with auto-fill | • Save time<br>• Consistency<br>• Easy updates | Efficiency | Profile update rate: 40% users | LOW |
| **Better Care Quality** | Progress tracking | No visibility into progress | Visual progress charts & metrics | • Motivation<br>• See improvements<br>• Goal achievement | Engagement, motivation | Progress view rate: 50% users | HIGH |
| | Goal setting & tracking | Informal goal tracking | Structured goal management | • Clear objectives<br>• Milestone tracking<br>• Achievement celebration | Accountability, motivation | Goal usage: 40% users | MEDIUM |
| | Therapy consistency | Forget to book follow-up | Reminder system + easy re-booking | • Better outcomes<br>• Consistent care<br>• Habit formation | Health improvement | Retention rate: 60% → 75% | HIGH |
| | Personalized recommendations | Generic suggestions | AI-based service recommendations | • Relevant services<br>• Better outcomes<br>• Discover options | Personalization | Recommendation acceptance: 35% | MEDIUM |
| **Communication** | In-app messaging | Phone/WhatsApp mix | Centralized messaging with therapist | • All communication in one place<br>• Async communication<br>• Message history | Convenience, organization | Messaging usage: 30% users | MEDIUM |
| | Automated reminders | Manual reminders or none | Email + SMS reminders (H-1, H-0) | • No missed appointments<br>• Timely preparation<br>• Reduced no-shows | Reliability | Reminder effectiveness: 90% attend after reminder | HIGH |
| | Support access | Call during office hours | In-app support ticket + FAQ | • Quick help<br>• Self-service FAQ<br>• Track issues | Support, empowerment | Support satisfaction: 4.0/5 | MEDIUM |
| **Privacy & Security** | Data privacy | Uncertain data handling | GDPR-compliant, encrypted data | • Trust in confidentiality<br>• Legal protection<br>• Peace of mind | Trust, safety | Privacy trust rating: 4.5/5 | CRITICAL |
| | Secure payment | Manual cash/transfer | Secure payment gateway (SSL) | • Payment safety<br>• No data theft risk<br>• Professional experience | Financial security | Payment trust rating: 4.6/5 | HIGH |
| **Cost Savings** | Time saved | 30-60 min booking process | 3-5 min booking process | • 25-55 min saved per booking<br>• Opportunity cost reduction | Time value | Time saving satisfaction: 4.7/5 | HIGH |
| | Travel cost saved | Physical visit to book | Online booking | • No transportation cost<br>• No parking fees | Financial saving | Cost savings appreciation: 4.2/5 | MEDIUM |
| **Overall Experience** | User satisfaction | Frustration with manual process | Seamless digital experience | • Pleasant interaction<br>• Modern experience<br>• Trust in brand | Overall happiness | Target SUS: 68+ (above average) | CRITICAL |
| | Likelihood to return | 35% return rate | Improved experience → retention | • Higher loyalty<br>• Repeat bookings<br>• Lifetime value | Retention | Target retention: 60% | HIGH |
| | Likelihood to recommend | Limited word-of-mouth | Positive experience → referrals | • NPS score improvement<br>• Organic growth<br>• Social proof | Advocacy | Target NPS: 30+ | HIGH |

**Client Benefits Summary:**
- **Convenience**: 24/7 self-service, mobile-friendly, instant confirmation, easy rescheduling
- **Transparency**: Full therapist profiles, real-time availability, clear pricing, ratings & reviews
- **Quality**: Progress tracking, goal management, personalized recommendations, consistent care
- **Communication**: In-app messaging, automated reminders, quick support access
- **Trust**: Data privacy, secure payments, professional experience
- **Savings**: Time saved (25-55 min/booking), travel cost reduction

**Target User Satisfaction:**
- Overall Satisfaction: ≥ 4.0/5.0
- System Usability Scale (SUS): ≥ 68 (above average)
- Net Promoter Score (NPS): ≥ 30
- Retention Rate: 60% return within 3 months

---

### 4.5.3 Manfaat untuk Therapists (Terapis)

---

**Tabel 4.39 Benefits Analysis - Therapists (Service Providers)**

| Benefit Category | Specific Benefit | Current Pain Point | System Solution | Therapist Impact | Time/Cost Savings | Professional Value | Priority |
|------------------|-----------------|-------------------|----------------|------------------|------------------|-------------------|----------|
| **Schedule Management** | Self-service availability setting | Coordinate via WhatsApp group | Set weekly recurring schedule in system | • Full autonomy<br>• Instant updates<br>• No admin dependency | Time: 2 hrs/week → 30 min/week<br>**Saved: 1.5 hrs/week = 6 hrs/month** | Control, flexibility | CRITICAL |
| | Easy leave management | Notify admin, manual blocking | One-click block dates feature | • Manage own leave<br>• No approval delays<br>• Visual calendar | Time: 30 min per leave request → 2 min | Autonomy, convenience | HIGH |
| | Conflict prevention | Manual conflict checking | Automatic conflict detection | • Zero double bookings<br>• No awkward cancellations<br>• Professional reliability | Conflict resolution: 1 hr/incident → 0 | Peace of mind, professionalism | CRITICAL |
| | Calendar integration | Separate personal/work calendars | Export .ics for Google/Outlook sync | • Unified calendar view<br>• Better time management<br>• No missed appointments | Calendar management: 30 min/week → 0 | Efficiency, organization | MEDIUM |
| | Last-minute changes | Call admin, hope for reach | Update availability real-time | • Emergency flexibility<br>• Control over schedule<br>• Client communication | Change processing: 15 min → 2 min | Flexibility, stress reduction | HIGH |
| **Client Management** | Comprehensive client profiles | Scattered info (WhatsApp, paper) | Centralized digital profiles | • Full client history at fingertips<br>• Better context<br>• Informed sessions | Profile lookup: 10 min → 30 sec | Better care quality | HIGH |
| | Session history access | Manual notes, hard to find | Searchable digital archive | • Easy reference<br>• Track progress<br>• Continuity of care | History retrieval: 15 min → 1 min | Professionalism, care quality | HIGH |
| | Progress tracking tools | Manual tracking, subjective | Visual charts, metrics, milestones | • Objective measures<br>• Motivate clients<br>• Evidence of effectiveness | Progress analysis: 30 min/client → 5 min | Clinical effectiveness | HIGH |
| | Client communication | Mix of phone, WhatsApp, email | In-app messaging (centralized) | • All messages in one place<br>• Message history<br>• Professional channel | Communication time: 2 hrs/week → 1 hr/week | Organization, professionalism | MEDIUM |
| **Documentation & Admin** | Structured session notes | Freeform notes, inconsistent | Templated session notes form | • Consistent documentation<br>• Nothing forgotten<br>• Professional records | Note-taking time: Same but better quality | Quality, compliance | HIGH |
| | Autosave functionality | Manual save, data loss risk | Automatic saving every 30 sec | • No data loss<br>• Peace of mind<br>• Focus on content | Recovery from data loss: 0 incidents | Reliability | MEDIUM |
| | Searchable notes | Paper/Word docs (hard to search) | Full-text search | • Quick information retrieval<br>• Pattern finding<br>• Reference past insights | Search time: 20 min → 30 sec | Efficiency | MEDIUM |
| | Digital archive | Physical storage, degradation | Cloud-based permanent storage | • Never lose records<br>• Access anywhere<br>• No physical space needed | Storage cost: Rp 0 (vs. filing) | Security, accessibility | MEDIUM |
| | Admin coordination | 3 hrs/week back-and-forth | Self-service system | • No waiting for admin<br>• Immediate actions<br>• Less interruption | Coordination: 3 hrs/week → 30 min/week<br>**Saved: 2.5 hrs/week = 10 hrs/month** | Autonomy, efficiency | HIGH |
| **Financial Management** | Real-time earnings dashboard | Wait for monthly report | Live earnings tracking | • Know income anytime<br>• Plan finances<br>• Motivation | Financial visibility: immediate vs. monthly | Financial transparency | HIGH |
| | Session breakdown | Manual calculation | Itemized earnings per session | • Verify payments<br>• Understand income sources<br>• Tax reporting | Calculation time: 2 hrs/month → 0 | Accuracy, trust | MEDIUM |
| | Tax reporting | Manual report compilation | One-click report generation | • Easy tax compliance<br>• Professional documentation<br>• Audit-ready | Tax prep time: 4 hrs/year → 30 min/year | Compliance, convenience | MEDIUM |
| | Payment transparency | Unclear payment status | Real-time payment tracking | • Know when paid<br>• Track pending payments<br>• Cash flow planning | Payment inquiry: 30 min/month → 0 | Trust, clarity | HIGH |
| **Performance Analytics** | Session statistics | No visibility into performance | Analytics dashboard (volume, rate, etc.) | • Self-awareness<br>• Goal setting<br>• Performance improvement | Analysis: Not available → Real-time | Professional growth | MEDIUM |
| | Client satisfaction scores | No formal feedback | Rating & review system | • Know strengths<br>• Identify weaknesses<br>• Improve service | Feedback collection: Ad-hoc → Systematic | Quality improvement | HIGH |
| | Utilization rate tracking | Unknown capacity usage | Utilization percentage metric | • Optimize availability<br>• Balance workload<br>• Income maximization | Capacity planning: Not available → Data-driven | Business optimization | MEDIUM |
| | Benchmarking | No comparison with peers | Anonymous peer comparison | • Industry standards<br>• Competitive positioning<br>• Motivation | Benchmarking: Not available → Enabled | Market awareness | LOW |
| **Professional Development** | Client outcome tracking | Subjective assessment | Data-driven outcome measures | • Evidence-based practice<br>• Treatment effectiveness<br>• Continuous improvement | Outcome analysis: Qualitative → Quantitative | Clinical excellence | HIGH |
| | Service improvement insights | Guesswork on what works | Pattern recognition, analytics | • Identify successful approaches<br>• Replicate best practices<br>• Personalize treatment | Insight generation: Not available → Automated | Treatment optimization | MEDIUM |
| | Portfolio building | Limited documentation | Digital portfolio (certifications, reviews, stats) | • Professional credibility<br>• Career advancement<br>• Marketing material | Portfolio creation: 10 hrs → Automated | Career growth | MEDIUM |
| **Work-Life Balance** | Flexible scheduling | Rigid manual schedule | Self-managed availability | • Control work hours<br>• Balance personal life<br>• Prevent burnout | Work-life balance: Improved significantly | Well-being, satisfaction | CRITICAL |
| | Reduced admin overhead | 5-6 hrs/week admin tasks | 1-2 hrs/week admin tasks | • More time for therapy<br>• Or personal time<br>• Better focus | **Total time freed: 4 hrs/week = 16 hrs/month** | Quality of life | CRITICAL |
| | Remote schedule management | In-person or call admin | Manage via mobile app anywhere | • Flexibility<br>• Vacation management<br>• Emergency changes | Accessibility: 24/7 vs. office hours | Convenience | HIGH |
| **Income Potential** | Increased bookings | 60% utilization, manual scheduling | 80% utilization, optimized scheduling | • More sessions<br>• Higher income<br>• Better capacity use | Income: +33% (12 → 16 sessions/week)<br>**Example: Rp 15M → Rp 20M/month** | Financial growth | CRITICAL |
| | Reduced no-shows | 15% no-show rate | 5% no-show rate (reminder system) | • More reliable income<br>• Less wasted time<br>• Better planning | No-show reduction: 10% → Saved 1.5 sessions/week | Revenue stability | HIGH |
| | Upselling opportunities | Limited visibility | System recommendations to clients | • Package sales<br>• Additional sessions<br>• Higher value | Upsell success: +15% revenue potential | Income diversification | MEDIUM |

**Therapist Benefits Summary:**
- **Time Savings**: 16 hours/month freed up (schedule: 6 hrs, coordination: 10 hrs)
- **Income Potential**: +33% through better utilization (60% → 80%) = ~Rp 5M/month increase
- **Professional Quality**: Better documentation, data-driven insights, outcome tracking
- **Work-Life Balance**: Autonomy, flexibility, reduced admin burden
- **Financial Clarity**: Real-time earnings, transparent payments, easy tax reporting

**Total Value per Therapist:**
- Time value (16 hrs @ Rp 250,000/hr): Rp 4,000,000/month saved
- Income increase (better utilization): Rp 5,000,000/month
- **Total monthly value: Rp 9,000,000/therapist**
- **Annual value: Rp 108,000,000/therapist**

**Target Therapist Satisfaction:**
- Overall Satisfaction: ≥ 4.5/5.0
- System Ease of Use: ≥ 4.3/5.0
- Recommendation to Other Therapists: ≥ 80%
- Utilization Improvement: 60% → 80% (33% increase)

---

#### C. Work-Life Balance

**1. Flexible Scheduling**
- Control over availability
- Easy time-off management
- Prevent overwork (max sessions per day setting)

**2. Reduced Administrative Burden**
- Less time on coordination
- Automated reminders reduce no-shows
- Digital documentation faster than manual

---

### 4.5.4 Return on Investment (ROI) Analysis

---

**[GAMBAR 4.66 - ROI Projection Graph (5 Years)]** 📈
_5-year ROI projection chart showing investment recovery, net benefits, and cumulative returns_

---

**Tabel 4.40 ROI Calculation - First Year Analysis**

| Cost/Benefit Category | Line Item | Quantity/Rate | Unit Cost | Frequency | Annual Amount (Rp) | Calculation Method | Notes |
|-----------------------|-----------|---------------|-----------|-----------|-------------------|-------------------|-------|
| **INITIAL INVESTMENT (Year 0)** |
| Development | Human Resource | 3 people × 11 weeks | Rp 0 | One-time | 0 | Opportunity cost = 0 | Academic capstone project |
| Infrastructure | Domain name (.id) | 1 domain | Rp 150,000 | Annual | 150,000 | 1 × Rp 150,000 | .id TLD registration |
| | Hosting (VPS 2GB RAM, 50GB SSD) | 1 server | Rp 100,000 | Monthly × 12 | 1,200,000 | Rp 100,000 × 12 | Niagahoster or equivalent |
| | SSL Certificate | 1 cert | Rp 0 | Annual | 0 | Free | Let's Encrypt |
| | Development tools | Various | Rp 0 | One-time | 0 | Free/open source | VS Code, Git, MySQL Workbench |
| Third-Party Services | Payment gateway setup | 1 account | Rp 0 | One-time | 0 | Free setup | Midtrans (2% transaction fee) |
| | Email service (SMTP) | 500 emails/day | Rp 50,000 | Monthly × 12 | 600,000 | Rp 50,000 × 12 | Mailtrap/SendGrid |
| | Backup storage (25GB) | 25GB cloud | Rp 50,000 | Monthly × 12 | 600,000 | Rp 50,000 × 12 | Google Drive Business |
| Miscellaneous | Testing devices | Existing | Rp 0 | One-time | 0 | Use team devices | Desktop, laptop, mobile |
| | Training materials | Manuals, videos | Rp 200,000 | One-time | 200,000 | Documentation effort | User guide, training videos |
| | Contingency (10%) | Safety buffer | 10% | One-time | 200,000 | 10% of (1.35M + 1.25M) | Risk mitigation |
| | **SUBTOTAL - INITIAL INVESTMENT** | | | | **3,000,000** | | **One-time cost** |
| **RECURRING ANNUAL COSTS (Year 1)** |
| Infrastructure | Domain renewal | 1 domain | Rp 150,000 | Annual | 150,000 | 1 × Rp 150,000 | Annual renewal |
| | Hosting | 1 server | Rp 100,000 | Monthly × 12 | 1,200,000 | Rp 100,000 × 12 | Monthly subscription |
| Services | Email service | 500 emails/day | Rp 50,000 | Monthly × 12 | 600,000 | Rp 50,000 × 12 | Transactional emails |
| | Backup storage | 25GB | Rp 50,000 | Monthly × 12 | 600,000 | Rp 50,000 × 12 | Daily backups |
| | Payment gateway fees | 100 bookings @ Rp 300K | 2% | Monthly × 12 | 7,200,000 | (100 × Rp 300K × 2%) × 12 | Transaction-based |
| Maintenance | Bug fixes & updates | Ad-hoc | Rp 0 | Ongoing | 0 | In-house capability | Team handles maintenance |
| | **SUBTOTAL - RECURRING COSTS** | | | | **9,750,000** | | **Annual recurring** |
| | **TOTAL YEAR 1 COSTS** | | | | **12,750,000** | | **Initial + Recurring** |
| **REVENUE BENEFITS (Year 1)** |
| Revenue Growth | Additional bookings | 20 more/month | Rp 300,000 | Monthly × 12 | 72,000,000 | (100 - 80) × Rp 300K × 12 | 25% volume increase |
| | Reduced no-shows | 8 prevented/month | Rp 300,000 | Monthly × 12 | 28,800,000 | 8 × Rp 300K × 12 | 15% → 5% no-show rate |
| | Upselling (packages) | 5 upgrades/month | Rp 100,000 | Monthly × 12 | 6,000,000 | 5 × Rp 100K × 12 | 10% upgrade rate |
| | Extended hours bookings | 10 after-hours/month | Rp 300,000 | Monthly × 12 | 36,000,000 | 10 × Rp 300K × 12 | 24/7 availability capture |
| | **SUBTOTAL - REVENUE INCREASE** | | | | **142,800,000** | | **Direct revenue impact** |
| **COST SAVINGS (Year 1)** |
| Operational Efficiency | Admin time savings | 20 hrs/month | Rp 25,000/hr | Monthly × 12 | 6,000,000 | 20 × Rp 25K × 12 | Booking automation |
| | Reduced coordination time | 16 hrs/month | Rp 25,000/hr | Monthly × 12 | 4,800,000 | 16 × Rp 25K × 12 | Therapist scheduling |
| | Reporting time savings | 8 hrs/month | Rp 25,000/hr | Monthly × 12 | 2,400,000 | 8 × Rp 25K × 12 | Automated reports |
| | Error/conflict resolution | 4 incidents/month | Rp 200,000 | Monthly × 12 | 9,600,000 | 4 × Rp 200K × 12 | Prevented double bookings |
| | Paper & printing | 50% reduction | Rp 100,000 | Monthly × 12 | 600,000 | Rp 50K × 12 | Digital documentation |
| | Payment verification time | 10 hrs/month | Rp 25,000/hr | Monthly × 12 | 3,000,000 | 10 × Rp 25K × 12 | Automated verification |
| | **SUBTOTAL - COST SAVINGS** | | | | **26,400,000** | | **Operational efficiency** |
| | **TOTAL ANNUAL BENEFITS** | | | | **169,200,000** | | **Revenue + Savings** |
| **NET BENEFIT & ROI (Year 1)** |
| Net Benefit | Total Benefits - Total Costs | | | | **156,450,000** | Rp 169.2M - Rp 12.75M | **Annual net benefit** |
| ROI | (Net Benefit / Total Investment) × 100% | | | | **1,227%** | (Rp 156.45M / Rp 12.75M) × 100% | **Exceptional ROI** |
| Payback Period | Total Investment / Monthly Benefit | | | | **0.9 months** | Rp 12.75M / (Rp 169.2M / 12) | **~27 days to break even** |

**Key Financial Metrics:**
- **Total Year 1 Investment**: Rp 12,750,000 (includes initial + recurring costs)
- **Total Year 1 Benefits**: Rp 169,200,000 (revenue increase + cost savings)
- **Net Benefit Year 1**: Rp 156,450,000
- **ROI**: 1,227% (exceptional return)
- **Payback Period**: 27 days (less than 1 month)
- **Benefit-Cost Ratio**: 13.3:1 (for every Rp 1 invested, return Rp 13.3)

**ROI Drivers:**
1. **High Revenue Impact**: Rp 142.8M from increased bookings, reduced no-shows, upselling
2. **Significant Cost Savings**: Rp 26.4M from operational efficiency gains
3. **Low Development Cost**: Rp 0 (academic project, in-house team)
4. **Modest Recurring Costs**: Rp 9.75M/year (infrastructure + services)
5. **Fast Payback**: Less than 1 month to recover investment

---

---

**[GAMBAR 4.67 - Cost-Benefit Analysis Chart]** 📊
_Comparative analysis of total costs vs total benefits over 5 years with break-even point visualization_

---

**Tabel 4.41 5-Year Cost-Benefit Analysis Projection**

| Year | Initial Investment | Annual Recurring Cost | Payment Gateway Fees (2%) | Total Annual Cost | Revenue Benefits | Cost Savings | Total Benefits | Net Annual Benefit | Cumulative Net Benefit | Cumulative ROI | Notes |
|------|-------------------|----------------------|---------------------------|------------------|------------------|--------------|----------------|-------------------|----------------------|---------------|-------|
| **0** | Rp 3,000,000 | Rp 0 | Rp 0 | **Rp 3,000,000** | Rp 0 | Rp 0 | **Rp 0** | **(Rp 3,000,000)** | **(Rp 3,000,000)** | **-100%** | Setup phase (Month 1-3) |
| **1** | Rp 0 | Rp 2,550,000 | Rp 7,200,000 | **Rp 9,750,000** | Rp 142,800,000 | Rp 26,400,000 | **Rp 169,200,000** | **Rp 159,450,000** | **Rp 156,450,000** | **1,218%** | Full operation (100% capacity) |
| **2** | Rp 0 | Rp 2,627,000 | Rp 7,992,000 | **Rp 10,619,000** | Rp 158,760,000 | Rp 27,720,000 | **Rp 186,480,000** | **Rp 175,861,000** | **Rp 332,311,000** | **2,506%** | Growth +10%, Cost +3% |
| **3** | Rp 0 | Rp 2,706,000 | Rp 8,871,600 | **Rp 11,577,600** | Rp 174,636,000 | Rp 29,106,000 | **Rp 203,742,000** | **Rp 192,164,400** | **Rp 524,475,400** | **3,947%** | Sustained growth +10% |
| **4** | Rp 0 | Rp 2,787,000 | Rp 9,758,760 | **Rp 12,545,760** | Rp 192,099,600 | Rp 30,561,300 | **Rp 222,660,900** | **Rp 210,115,140** | **Rp 734,590,540** | **5,528%** | Market expansion +10% |
| **5** | Rp 0 | Rp 2,871,000 | Rp 10,734,636 | **Rp 13,605,636** | Rp 211,309,560 | Rp 32,089,365 | **Rp 243,398,925** | **Rp 229,793,289** | **Rp 964,383,829** | **7,258%** | Scale & optimization +10% |

**Cumulative 5-Year Summary:**
- **Total Investment (5 years)**: Rp 60,098,000 (Rp 3M initial + Rp 57.098M recurring)
- **Total Benefits (5 years)**: Rp 1,025,481,825 (revenue + savings)
- **Total Net Benefit (5 years)**: Rp 964,383,829
- **Average Annual Net Benefit**: Rp 192,876,766
- **5-Year ROI**: 7,258%
- **Cumulative Benefit-Cost Ratio**: 17.1:1

**Projection Assumptions:**
1. **Revenue Growth**: 10% annual increase (conservative estimate based on user adoption curve)
2. **Cost Inflation**: 3% annual increase for hosting/infrastructure
3. **Payment Gateway Fees**: 2% of transaction volume (scales with revenue)
4. **Booking Volume**: 100/month Year 1 → 264/month Year 5 (progressive growth)
5. **No Major System Upgrades**: Assumes current tech stack remains viable
6. **Market Conditions**: Stable mental health services demand

**Sensitivity Analysis:**

| Scenario | Revenue Change | Cost Change | Year 1 ROI | 5-Year Cumulative Net | Feasibility |
|----------|---------------|-------------|-----------|----------------------|-------------|
| **Best Case** (+20% revenue, -10% cost) | +20% | -10% | 1,823% | Rp 1,276,909,180 | Exceptional |
| **Base Case** (as projected) | 0% | 0% | 1,227% | Rp 964,383,829 | Excellent |
| **Conservative** (-10% revenue, +10% cost) | -10% | +10% | 988% | Rp 672,419,562 | Very Good |
| **Worst Case** (-20% revenue, +20% cost) | -20% | +20% | 749% | Rp 380,455,295 | Still Profitable |

**Break-Even Analysis:**
- **Minimum Bookings Required** (Year 1): 14 bookings/month (vs. target 100/month)
- **Revenue Threshold**: Rp 4.2M/month (vs. projected Rp 14.1M/month)
- **Safety Margin**: 86% buffer (system profitable even at 14% of target)

**Key Insights:**
1. **Exceptional ROI**: Even in worst-case scenario (749% ROI), investment is highly profitable
2. **Fast Payback**: Initial investment recovered in less than 1 month
3. **Scalable Economics**: As revenue grows, cost increases are minimal (economies of scale)
4. **Low Risk**: Break-even requires only 14% of target bookings
5. **Long-Term Value**: 5-year cumulative net benefit of Rp 964M on Rp 60M investment

**Recommendation**: **PROCEED WITH IMPLEMENTATION**
- Financial analysis strongly supports system development
- Multiple scenarios confirm profitability
- Risk is minimal with fast payback and high safety margin
- Long-term strategic value beyond financial returns

---

---

### 4.5.5 Intangible Benefits

Selain benefit yang dapat dikuantifikasi, ada juga manfaat intangible:

#### A. Brand Image dan Reputation

**1. Modern dan Professional Image**
- Presence di digital space
- Tech-savvy brand perception
- Trust building melalui transparency

**2. Competitive Advantage**
- First-mover advantage dalam hypnotherapy digital booking di area
- Differentiation dari kompetitor yang masih manual
- Innovation perception

#### B. Data Assets

**1. Business Intelligence**
- Customer behavior data
- Service popularity insights
- Pricing optimization opportunities
- Market trend identification

**2. Strategic Planning**
- Data-driven decision making
- Predictive analytics capability
- Resource optimization

#### C. Scalability dan Growth Potential

**1. Foundation for Expansion**
- Ready untuk expand ke multiple locations
- Franchise-ready system
- API-ready untuk future integrations (mobile app, partner systems)

**2. New Revenue Streams**
- Online consultation capability
- Digital products (recorded sessions, self-help materials)
- B2B services (corporate wellness programs)

---

**[File ini mencakup 4.4 Faktor Penentu Keberhasilan dan 4.5 Keuntungan yang Diharapkan. Akan dilanjutkan dengan file terpisah untuk 4.6 dan 4.7]**
