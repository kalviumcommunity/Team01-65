# 📋 Recruitment Funnel Analytics Dashboard

**Product Requirements Document (PRD) • Version 1.0**

---

## 1. Business Problem & Goal

### Problem

HR teams have recruitment, interview, and offer records across separate datasets, making it difficult to identify which hiring stages cause the most candidate drop-off or to compare recruitment performance across departments.

### Goal

Build a shared analytics dashboard that standardizes recruitment data, calculates funnel metrics, flags bottlenecks and supports evidence-based recruitment decisions.

### 👥 Users

- HR teams
- Recruiters and hiring managers
- People analytics and HR operations

### 🎯 IN SCOPE

- Cleaning
- Funnel metrics
- Time-in-stage
- Department comparison
- Bottleneck flags
- APIs
- Dashboard insights

### 🚫 OUT OF SCOPE

- Live ATS/HRIS integration
- Predictive attrition
- Automated candidate scoring
- A/B testing
- Continuous model retraining

---

## 2. User Stories & Acceptance Criteria

| Role | User Story | Acceptance Criteria |
|---|---|---|
| HR Analyst | View candidate counts at each hiring stage, so that I can identify where the funnel loses the most candidates. | Stage counts and drop-off rates are visible. |
| Recruiter | Compare departments, so that I can identify inefficient recruitment processes. | Conversion, drop-off and time-to-hire are comparable. |
| HR Operations | Flag high-drop-off and long-duration stages, so that I can prioritize improvements. | Documented thresholds/rules flag bottlenecks. |
| Hiring Manager | View interview outcomes with funnel stages, so that I can understand candidate progression. | Interview outcomes/scores link where available. |

---

## 3. KPI Planning

**KPI Formula:** Metric + Measurement Method + Numeric/defined Target + Timeline.

| Metric | Method | Target | Timeline |
|---|---|---|---|
| Funnel drop-off | 100 × (stage entrants − next-stage entrants) / stage entrants | Identify highest-drop-off stage | First release |
| Stage conversion | next-stage entrants / current-stage entrants × 100 | Compare available stages | First release |
| Time-in-stage | Median(stage exit − stage entry) | Flag above department baseline | First release |
| Offer acceptance | accepted offers / total offers × 100 | Report overall + department | First release |

---

## 📊 PRD — Data, Stakeholders, Risks & Review

## 4. Dataset Documentation

### 📁 Source

- `candidates.csv`
- `applications.csv`
- `jobs.csv`
- `interviews.csv`
- `offers.csv`

### 🧾 Fields

Candidate/application/job IDs, department, role, stage/status, timestamps, interview outcome/score and offer status where available.

### 🔍 Quality

- Validate columns/types
- Handle missing values
- Identify duplicates
- Standardize timestamps and categories

### 🔄 Owner / Refresh

**Owner:** Project analytics team.

**Refresh:** Initial prototype uses static CSV data; production refresh cadence will be defined later.

---

## 5. Stakeholder Map

### 👤 Primary Users

HR teams, recruiters and hiring managers — consume insights and act on bottlenecks.

### 👥 Secondary Users

People analytics and HR operations — prepare and interpret recruitment reporting.

### 🗄 Data Owners

Teams responsible for candidate, application, job, interview and offer records.

### ✅ Approvers

Project/product stakeholders validating scope, KPIs, findings and release readiness.

---

## 6. Data Workflow & Technical Scope

### Workflow

- Raw CSVs → validation → cleaning
- Transformation → feature engineering → funnel analytics
- Analytical storage → REST APIs → dashboard → HR insights

### Prototype

Python, Pandas, FastAPI and CSV data.

### Analysis

Analysis may use NumPy and Matplotlib/Seaborn.

### Planned Dashboard / Backend / Storage

- React
- Vite
- Tailwind
- Recharts/Chart.js
- Node/Express
- MongoDB

---

## 7. Risks & Assumptions

| Risk | Likelihood / Impact | Mitigation |
|---|---|---|
| ⚠️ Missing fields | Medium / High | Use only available fields; document unavailable onboarding/rejection data. |
| ⚠️ Data quality | Medium / High | Validate types, duplicates, timestamps and required columns. |
| ⚠️ Uneven samples | Medium / Medium | Show sample counts and avoid over-interpreting small departments. |
| ⚠️ Metric inconsistency | Low / High | Centralize metric definitions and reuse calculation logic. |

---

## 8. Success Criteria & PRD Review Checklist

- ☐ Highest-drop-off stages are identified and explained using measurable metrics.
- ☐ Departments are compared using conversion, drop-off and time-to-hire indicators.
- ☐ Bottleneck stages are flagged using documented rules or thresholds.
- ☐ Recommendations use multiple indicators rather than a single metric.
- ☐ Data assumptions, quality issues and unavailable fields are documented.
- ☐ Analysis is reproducible and dashboard insights are understandable.

---

## 9. Delivery Boundary

### Definition of Done

**Validated data → documented metrics → reproducible analysis → bottleneck identification → API-ready outputs → dashboard-ready insights → stakeholder review and approval**