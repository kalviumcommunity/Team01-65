# Product Requirements Document

## Recruitment Funnel Analytics Dashboard

### Problem

HR teams have recruitment funnel data, interview feedback, and onboarding records, but no shared reporting system identifies which hiring stages contribute most to candidate drop-offs across departments. This makes it difficult to pinpoint bottlenecks and improve the hiring process using data.

### Goal

Build an interactive analytics dashboard that consolidates recruitment data and provides HR teams with a clear view of candidate movement through the hiring funnel. It will help HR teams identify bottleneck stages, compare departments, and make data-driven recruitment decisions.

### Users

- HR teams evaluating recruitment funnel performance.
- Recruiters and hiring managers reviewing department-level hiring trends.
- People analytics and HR operations staff preparing and interpreting funnel data.

### Core Features

- Clean and preprocess recruitment funnel, interview, and onboarding data.
- Calculate funnel metrics such as stage-wise conversion rate, time-in-stage, drop-off rate, and offer-acceptance rate.
- Analyze relationships between hiring stages and candidate drop-off.
- Identify bottleneck stages and flag stages with abnormally high drop-off.
- Compare departments using funnel and time-to-hire metrics.
- Produce recruitment process recommendations based on multiple indicators.
- Expose data and analysis through REST APIs and an interactive dashboard.

### Data Needed

- Candidate and requisition identifiers.
- Department and job role.
- Hiring stage (applied, screened, interviewed, offered, hired, rejected).
- Stage entry and exit timestamps, and time spent in each stage.
- Interview feedback and scores.
- Drop-off or rejection reason.
- Onboarding completion status.

The initial dataset will contain recruitment funnel records with candidate ID, department, hiring stage, stage timestamps, interview outcome, and drop-off status.

### Tech Stack

| Area | Technologies |
|---|---|
| Current prototype | Python, Pandas, FastAPI, and CSV data |
| Data analysis | NumPy, Matplotlib or Seaborn, and scikit-learn |
| Planned dashboard | React, Vite, Tailwind CSS, Recharts or Chart.js, and Axios |
| Planned backend & storage | Node.js, Express.js, and MongoDB |
| Collaboration | GitHub Issues, Projects, branches, pull requests, and code reviews |

### Basic Flow

1. Collect recruitment funnel, interview feedback, and onboarding data.
2. Clean and preprocess the data.
3. Create funnel and stage-level features.
4. Analyze drop-off patterns across hiring stages.
5. Compare departments and identify bottlenecks.
6. Generate recruitment process recommendations.
7. Present results through APIs and the dashboard.

### Success Criteria

- Identify and explain which hiring stages contribute most to candidate drop-off.
- Compare funnel performance and time-to-hire across departments.
- Identify bottleneck stages that need process improvement.
- Provide actionable recruitment recommendations supported by multiple indicators.
- Present insights through an understandable dashboard.
- Keep the analysis reproducible and documented.

### Out of Scope

- Real-time funnel tracking or predictive attrition modeling.
- Automated candidate screening or scoring decisions.
- Integration with live ATS or HRIS systems.
- Personalized candidate recommendations.
- A/B testing of hiring processes.
- Continuous model retraining.
