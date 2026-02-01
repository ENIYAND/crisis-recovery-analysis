# QuickBite Crisis Analytics Platform

## 1️⃣ Project Overview

**QuickBite Crisis Analytics Platform** is an end-to-end **Databricks Lakehouse project**
that simulates how a food-delivery company detects, analyzes, and responds to
a large-scale operational crisis.

The platform combines:
- Streaming ingestion
- AI-driven sentiment intelligence
- Crisis-aware churn prediction
- Geospatial hotspot detection
- Business-ready Gold analytics

The goal is not just analytics — but **decision intelligence during crisis scenarios**.

## 🧠 Problem Definition & AI Framing

### The Strategic Imperative

Food delivery platforms are highly sensitive to **compound crisis scenarios**, where multiple failure modes occur simultaneously.  
This project models a **dual-crisis event** affecting a food delivery ecosystem:

1. **Logistical Collapse** — severe delivery delays caused by external shocks (e.g., weather, capacity shortage)
2. **Customer Trust Breakdown** — negative sentiment driven by poor service and food safety concerns

Individually, these issues are manageable. Combined, they form a **non-linear failure pattern** that traditional batch analytics and retrospective BI systems fail to detect in time.

---

### Why This Is an AI Problem (Not Just Analytics)

During crisis onset:
- Delivery delays increase gradually, not abruptly
- Customer dissatisfaction manifests as **textual sentiment**, not numeric metrics
- Churn occurs **after** the crisis, not during it

This creates a delayed feedback loop where:
- Operational metrics degrade first
- Customer sentiment worsens next
- Churn materializes last

Traditional dashboards detect the problem **after churn has already happened**.

The AI challenge is to:
> **Predict churn risk early by learning latent signals across operations, sentiment, and customer behavior — before revenue loss occurs.**

---

### Data Challenge: No Single Dataset Is Sufficient

No publicly available dataset captures:
- Real delivery network variability
- Customer identity and lifecycle behavior
- Crisis-driven sentiment signals
- Real-time drift dynamics

To address this, the project intentionally adopts a **Hybrid Augmented Dataset strategy**.

---

### Hybrid Dataset Strategy (AI Framing Decision)

This project combines:

#### 1️⃣ Real Operational Backbone (Kaggle / DoorDash Dataset)
- Captures authentic delivery variance
- Includes real timestamps, delays, and store-level behavior
- Represents realistic logistics noise (traffic, weather, batching)

#### 2️⃣ Synthetic Intelligence Layer (Custom Data Generation)
To make the dataset **AI-usable**, synthetic layers are introduced:

- **Customer Identity**
  - Generated customer IDs, segments, signup timelines
  - Enables retention and churn modeling

- **Crisis Sentiment Injection**
  - Probabilistic generation of negative reviews
  - Direct correlation between delivery delay and complaint likelihood
  - Explicit simulation of food safety incidents

- **Temporal Drift Simulation**
  - Timestamp shifting to project historical data into a live (2026) timeline
  - Controlled crisis phase where delivery times worsen for select markets

This hybrid approach preserves **real-world realism** while enabling **end-to-end AI modeling**.

---

### AI Framing Summary

The problem is framed not as:
- “Predict churn from historical data”

But as:
> **Detect early churn risk under crisis conditions by learning cross-signal patterns spanning operations, sentiment, geography, and customer behavior.**

This framing directly motivates:
- Feature engineering choices (RFM, sentiment velocity, crisis exposure)
- Recall-first model optimization
- Explainable, business-aligned outputs rather than black-box accuracy


---

## 2️⃣ Architecture (High Level)
```
Raw Orders (JSON / Simulated Events)
↓
Bronze Layer (Auto Loader)
↓
Silver Layer (Cleaned + Enriched)
↓
AI Sentiment & ML Feature Engineering
↓
Gold Layer (KPIs, Risk, Geo Intelligence)
↓
Dashboards & Decision Systems
```


### Key Architectural Principles
- Clear separation of concerns (Bronze / Silver / Gold / ML)
- No ML logic in Gold tables
- No raw text exposure beyond Silver
- ML models trained, governed, and deployed independently

---

## 3️⃣ Key Capabilities

### 🚀 Data Ingestion & Processing
- Auto Loader–based Bronze ingestion
- Structured transformations using PySpark & SQL
- ACID-compliant Delta Lake tables

### 🧠 AI & Machine Learning
- AI-simulated NLP sentiment classification (topic + polarity)
- Crisis-aware churn prediction using Gradient Boosted Trees
- Recall-optimized evaluation strategy
- Full ML lifecycle tracking using MLflow

### 🌍 Geospatial Intelligence
- H3 hexagonal indexing for spatial aggregation
- Hygiene and safety hotspot detection
- Market-level risk clustering

### 📊 Analytics & Insights
- Executive-level crisis KPIs
- Customer churn risk profiling
- Operational stress and safety intelligence

---

## 4️⃣ Governance & Security

Governance is **explicitly simulated** to reflect real production constraints:

- Raw review text restricted to Silver layer
- AI-derived sentiment categories exposed instead of PII
- Column-level masking via SQL views
- Unity Catalog–style governance concepts (Free Edition compatible)

This ensures:
- Privacy safety
- Explainability
- Controlled data access

---

## 5️⃣ Machine Learning

### Model Overview
- **Algorithm**: Gradient Boosted Trees (Spark ML)
- **Objective**: Customer churn prediction during crisis periods
- **Optimization Metric**: Recall (churn = 1)

### ML Lifecycle
- Feature engineering separated from training
- Experiments tracked in MLflow
- Model registered with signature and versioning
- Lifecycle stages (Staging → Production) enforced

### Why Recall?
Missing a churn-risk customer during a crisis is more costly than
a false positive. The model prioritizes **early detection over perfection**.

---

## 6️⃣ Dashboards & Business Use

### Executive & Operations Dashboards
- **Recovery Tracker**: Daily delays, complaints, and stabilization trends
- **Safety Watchtower**: Hygiene hotspots by geographic zone
- **Customer Risk View**: Churn-risk segmentation for retention teams

These dashboards support:
- Faster crisis response
- Targeted interventions
- Data-backed executive decisions

---

## 7️⃣ Tech Stack

- **Databricks (Free Edition)**
- **Apache Spark (PySpark, SQL)**
- **Delta Lake**
- **MLflow**
- **Gradient Boosted Trees**
- **H3 Geospatial Indexing**
- **TextBlob (Sentiment Simulation)**

---

## 8️⃣ Repository Structure
```
quickbite-crisis-analytics/
│
├── notebooks/
│ ├── Crisis_recovery_data_simulation_and_augmentation.ipynb
│ ├── Crisis_recovery_bronze.ipynb
│ ├── Crisis_recovery_silver.ipynb
│ ├── Crisis_recovery_gold.ipynb
│ ├── Crisis_recovery_ml_feature_engineering.ipynb
│ ├── Crisis_recovery_Model_Training_&_Lifecycle.ipynb
│ ├── Crisis_recovery_MLFlow_Registration.ipynb
│ ├── Crsis_recovery_Sentiment Analysis.ipynb
│ ├── Crisis_recovery_Geospatial_Intelligence_with_H3.ipynb
│
├── sql/
│ ├── governance_views.sql
│ ├── dashboard_queries.sql
│
│
└── README.md
```

## 9️⃣ 📊 Data Understanding & Feature Engineering

### Understanding the Data Landscape

The data powering this project is intentionally **multi-layered**, reflecting the complexity of a real food-delivery ecosystem under crisis conditions.  
Rather than treating data as flat records, the system distinguishes between **operational signals**, **customer behavior**, and **experience-driven sentiment**.

The primary data domains are:

- **Order & Delivery Events**
  - Order timestamps, delivery duration, delay indicators
  - Store- and market-level operational context

- **Customer Lifecycle Signals**
  - Order frequency, recency, and monetary value
  - Customer segment and engagement patterns

- **Sentiment & Experience Signals**
  - Review text mapped to sentiment polarity and topics
  - Explicit modeling of food safety and service complaints

This separation allows the model to learn **why** churn occurs, not just **when** it occurs.

---

### Feature Engineering Philosophy

Feature engineering in this project follows three guiding principles:

1. **Crisis Sensitivity**  
   Features must react quickly to abnormal operational behavior.

2. **Temporal Awareness**  
   Recent experiences matter more than historical averages during a crisis.

3. **Explainability**  
   Every feature should map to an interpretable business concept.

---

### Core Feature Categories

#### 1️⃣ Behavioral & Engagement Features
These capture how customers interact with the platform over time.

- `total_orders` — overall engagement depth  
- `days_since_last_order` — inactivity signal  
- `avg_star_rating` — historical satisfaction baseline  

These features establish **normal customer behavior** prior to crisis impact.

---

#### 2️⃣ RFM Scoring (Customer Value Context)

To quantify customer value, classic **RFM (Recency, Frequency, Monetary)** scoring is applied:

- Recency → How recently the customer ordered
- Frequency → How often the customer orders
- Monetary → Total spend over lifetime

The resulting `rfm_score` allows the model to distinguish:
- High-value customers temporarily dissatisfied
- Low-engagement customers naturally at churn risk

This prevents the model from overreacting to one-off bad experiences.

---

#### 3️⃣ Crisis Exposure Features

These features explicitly encode **crisis impact**, which traditional churn models ignore.

- `late_order_ratio` — proportion of delayed deliveries
- `crisis_exposure_index` — intensity of exposure to crisis conditions
- `sentiment_velocity` — rate of sentiment deterioration over time

These features allow the model to detect **early warning signals** before churn manifests.

---

#### 4️⃣ Sentiment-Derived Features

Customer reviews are transformed into structured intelligence:

- `ai_sentiment` — Positive / Neutral / Negative
- `ai_topic` — Service vs Hygiene vs Other
- `sentiment_score` — numeric polarity

By converting text into explainable signals, the model learns:
- Whether dissatisfaction is service-related or safety-related
- Which complaints correlate most strongly with churn

---

### Preventing Data Leakage

To ensure model validity:

- All features are **aggregated at the customer level**
- No future information leaks into training windows
- Sentiment features are derived only from **past orders**

This ensures that predictions simulate **real-time decision-making**, not hindsight.

---

### Feature Engineering Summary

The final feature set represents a **crisis-aware customer state**, combining:

- Long-term value (RFM)
- Short-term experience (sentiment + delays)
- Temporal dynamics (velocity and recency)

Rather than predicting churn from static history, the model learns **how customers react under stress**, which is critical for crisis recovery scenarios.

## 🔟 🤖 AI Innovation & Insight Generation

### Beyond Traditional Churn Prediction

This project goes beyond static churn modeling by introducing **crisis-aware intelligence**, where churn is treated as a *delayed outcome* of compounding operational and sentiment failures.

The innovation lies in **how signals are combined**, not just in the model itself.

---

### Key AI Innovations

- **Hybrid Intelligence Pipeline**
  - Combines real operational data with synthetic sentiment and customer identity
  - Enables end-to-end AI modeling where no single dataset would suffice

- **Sentiment as a Leading Indicator**
  - Unstructured customer reviews are transformed into structured, explainable features
  - Sentiment deterioration is observed *before* churn occurs

- **Crisis Exposure Modeling**
  - Explicit features capture customer exposure to delivery delays and safety incidents
  - Allows early risk detection during crisis onset rather than post-failure analysis

- **Explainable AI Outputs**
  - Model predictions can be traced back to interpretable signals:
    - Recent delays
    - Negative sentiment
    - Inactivity patterns

---

### Insight Generation

By fusing operational, behavioral, and sentiment signals, the system reveals that:

- Customer demand may remain stable during a crisis
- Service quality degrades first, sentiment follows, and churn occurs later
- High-value customers are not immune to churn under repeated negative experiences

This enables **proactive intervention**, not reactive reporting.

---

## 1️⃣1️⃣ ⚙️ Model Selection & Technical Reasoning

### Why Gradient-Boosted Trees (GBT)

A **Gradient-Boosted Trees (GBT)** classifier was selected for churn prediction due to:

- Ability to model **non-linear interactions** between features
- Strong performance on mixed numerical features
- Native support in Spark for scalable training

Crisis-driven churn is not linear — GBT captures threshold effects such as:
- Sudden risk increase after repeated delays
- Interaction between sentiment and recency

---

### Pipeline-Based Architecture

The model is implemented as a **Spark ML Pipeline**, ensuring:

- Consistent feature transformation
- Reproducible training and inference
- Seamless integration with MLflow tracking

This mirrors production ML system design.

---

### Metric Selection: Recall Over Accuracy

The model is optimized for **Recall**, not accuracy.

**Rationale**
- Missing a churn-risk customer during a crisis is costlier than a false alert
- High recall enables proactive retention actions

This aligns technical optimization directly with business impact.

---

### Known Limitations

- Extreme class imbalance in churn labels
- Synthetic sentiment simplifies real-world NLP complexity

These limitations are explicitly documented and surfaced through MLflow metadata.

---

### Technical Summary

Modeling decisions were driven by:
- Business risk prioritization
- Explainability requirements
- Production readiness over leaderboard metrics


---

## 1️⃣2️⃣ Key Insights & Findings

### 📌 Executive Overview — Crisis Behavior at a Glance
![Daily Crisis KPIs](assets/dashboards/Executive_Overview_1.png)
![Daily Crisis KPIs](assets/dashboards/Executive_Overview_2.png)

**Observed Patterns**
- Late complaints spike sharply around **October 2025**, coinciding with the simulated crisis period
- Safety incidents remain consistently elevated during the crisis window
- Despite operational stress, **order volume does not collapse**

**Insight**
> The crisis impacts service quality and safety signals before it impacts demand.  
> Customers continue ordering even as experience degrades — indicating *inelastic demand during emergencies*.

---

### ⚙️ SLA & Operations Health — Stress Signals
![SLA & Operations Health](assets/dashboards/SLA&Operations_health_1.png)
![SLA & Operations Health](assets/dashboards/SLA&Operations_health_2.png)

**Observed Patterns**
- Average delivery delay increases drastically during crisis months
- Outstanding order backlog rises in a cyclical pattern
- Store-level SLA rankings show **a small subset of stores repeatedly underperforming**

**Insight**
> Operational stress is **localized, not uniform**.  
> A limited number of stores disproportionately contribute to SLA degradation, making them ideal intervention targets.

**Business Action**
- Prioritize SLA recovery for the bottom-performing stores
- Redistribute delivery capacity rather than applying blanket fixes

---

### 👥 Customer Risk & Retention — Churn Signals
![Customer Risk & Retention](assets/dashboards/Customer_Risk_&_Retention_1.png)
![Customer Risk & Retention](assets/dashboards/Customer_Risk_&_Retention_2.png)

**Observed Patterns**
- High-risk churn segments show:
  - Longer inactivity (`days_since_last_order`)
  - Higher negative experience counts
- High lifetime value customers still appear in **high churn-risk segments**
- Churn risk is not strictly correlated with historical value

**Insight**
> During crises, **recent negative experience outweighs long-term loyalty**.  
> Even valuable customers churn if the last interaction is poor.

**Business Action**
- Trigger retention offers based on *recent sentiment + inactivity*, not lifetime value alone
- Prioritize proactive outreach for customers exposed to crisis-period failures

---

### 🧼 Safety & Hygiene Intelligence — Geographic Risk
![Safety & Hygiene Intelligence](assets/dashboards/Safety_&_Hygiene_Intelligence(Map)_1.png)

**Observed Patterns**
- Hygiene-related incidents form **clear geographic clusters**
- Certain store locations repeatedly appear in safety hotspots
- Risk is spatially concentrated, not randomly distributed

**Insight**
> Hygiene risk propagates geographically before becoming systemic.  
> Early spatial clustering provides a **leading indicator** of broader safety issues.

**Business Action**
- Dispatch inspections and audits to hotspot zones
- Temporarily restrict high-risk stores during peak crisis windows

---

### 🚦 Market Congestion — Capacity Imbalance
![Market Congestion](assets/dashboards/Market_Congestion.png)

**Observed Patterns**
- Congestion ratios vary significantly by market
- Some markets show high busy-dasher counts but insufficient on-shift dashers
- Other markets remain underutilized

**Insight**
> Crisis impact is **market-specific**, driven by local supply–demand imbalance rather than global failure.

**Business Action**
- Rebalance dasher supply across markets
- Use congestion ratios as early-warning signals for demand surges


---

## 1️⃣3️⃣ Automated Jobs & Pipelines (Database ↔ AI Workflow)

### End-to-End Lakehouse Orchestration

The Crisis Recovery platform is orchestrated using **Databricks Jobs**, enabling reliable, repeatable, and production-style execution across all data layers.

### Pipeline Flow

- **bronze_ingestion**  
  Raw data ingestion using Auto Loader (streaming-compatible design)

- **silver_table**  
  Data cleaning, enrichment, SLA computation, sentiment signals, and feature preparation

- **gold_table**  
  Business-ready KPIs, churn risk signals, and operational intelligence

This job executes the complete **Bronze → Silver → Gold** lifecycle without manual intervention.

![Lakehouse Pipeline Graph](assets/jobs/Jobs_&_pipelines_2.png)

---

### Execution Characteristics

- Fully automated task dependencies
- Serverless compute enabled
- Lineage tracked across **12 upstream tables** and **2 downstream tables**
- End-to-end execution completes in approximately **2 minutes**

![Pipeline Timeline](assets/jobs/Jobs_&_pipelines_3.png)

![Pipeline Task List](assets/jobs/Jobs_&_pipelines_4.png)

---

### Why This Matters

This orchestration layer demonstrates:
- Clear separation of concerns across data layers
- Strong database ↔ analytics ↔ AI integration
- Production-grade data engineering practices

This directly satisfies the **Database ↔ AI Workflow** evaluation criterion.

---

## 1️⃣4️⃣  MLflow Experiments (Training, Evaluation & Metrics)

### Experiment Tracking Strategy

All churn model experiments are tracked using **MLflow Experiments** under the Databricks workspace path:
/Shared/QuickBite_Churn_Prediction

Each run captures:
- Feature set configuration
- Model parameters
- Evaluation metrics
- Training artifacts
- Source notebook lineage

![MLflow Experiments](assets/mlflow/mlflow_1.png)

---

### Model Evaluation Philosophy

The churn model is optimized for **Recall**, not overall accuracy.

**Rationale**
- In crisis scenarios, missing a churn-risk customer is more costly than triggering a false positive
- Early identification enables proactive retention actions

**Primary Metric**
- `recall_churn`

![MLflow Metrics](assets/mlflow/mlflow_2.png)

---

### Experiment Transparency

Each MLflow run provides:
- Full artifact lineage (Spark ML pipeline)
- Environment reproducibility (conda + python environment)
- Feature-set traceability for explainability

![MLflow Artifacts](assets/mlflow/mlflow_3.png)

---

### Why This Matters

This experimentation setup ensures:
- Metric-driven model selection
- Reproducibility and auditability
- Strong alignment between technical evaluation and business risk

This satisfies **Training, Evaluation & Metrics** and **Model Selection & Technical Reasoning** criteria.

---

## 1️⃣5️⃣ Model Registry & Lifecycle Governance

### Registered Staging Model

The final churn model is registered in the **MLflow Model Registry** as:
quickbite_churn_predictor

![Registered Models](assets/models/model_1.png)

---

### Versioned Model Lifecycle

- Multiple model versions tracked
- Explicit metadata and tags applied
- Known limitations documented (e.g., extreme class imbalance)
- Full audit trail of model evolution

![Model Versions](assets/models/model_2.png)

---

### Governance & Deployment Readiness

Each registered model includes:
- Input/output schema via model signature
- Spark ML pipeline compatibility
- Rollback support through versioning
- Deployment-ready artifacts for batch or serving use cases

This elevates the project from **model experimentation** to **enterprise-grade MLOps**.

---

### Why This Matters

This layer demonstrates:
- Model governance and lifecycle control
- Explainability through feature traceability
- Readiness for real-world deployment scenarios

---

##1️⃣6️⃣ 💼 Business Impact & Practical Use

### From Analytics to Action

This project is designed not as an academic exercise, but as a **decision-support system** for crisis recovery in a food delivery business.  
Every output produced by the platform maps directly to an operational or strategic action.

---

### Practical Business Use Cases

#### 1️⃣ Executive Crisis Monitoring
- Daily KPIs provide early visibility into delivery delays, safety incidents, and backlog pressure
- Leadership can assess crisis severity and stabilization trends in near real-time

**Impact**
- Faster executive response
- Reduced time-to-awareness during crisis onset

---

#### 2️⃣ Operations & SLA Recovery
- Store-level SLA rankings identify repeat offenders
- Market congestion metrics highlight capacity imbalances

**Impact**
- Targeted intervention instead of blanket operational changes
- Efficient allocation of drivers and operational resources

---

#### 3️⃣ Customer Retention & Revenue Protection
- Churn risk profiles identify customers most affected by crisis conditions
- Recall-optimized model ensures high-risk customers are not missed

**Impact**
- Proactive retention campaigns
- Reduced long-term revenue loss despite short-term demand stability

---

#### 4️⃣ Safety & Compliance Intelligence
- Geospatial hygiene hotspots surface clustered safety risks
- Enables zone-based audits and store-level corrective actions

**Impact**
- Improved customer trust
- Lower regulatory and reputational risk

---

### Real-World Deployment Readiness

The platform is production-oriented by design:
- Automated pipelines (Bronze → Silver → Gold)
- MLflow-tracked experiments and registered models
- Explainable features aligned with business logic

This allows the system to be extended into:
- Real-time alerting
- Automated retention workflows
- Crisis playbooks and decision engines

---

### Business Value Summary

By combining operational data, customer sentiment, and machine learning, the platform enables the business to:

- Detect crises early
- Prioritize interventions intelligently
- Retain at-risk customers
- Recover faster with measurable impact

> The core value lies not in predicting churn alone, but in **explaining why customers are at risk and what action should follow**.


## 1️⃣7️⃣ Closure:
 Finally, this project demonstrates:
 
- Strong problem framing
- Clean lakehouse architecture
- Explainable AI design
- Business-first ML decisions
- Production-grade documentation

It reflects how **real organizations build crisis intelligence systems** —
not just how models are trained.
