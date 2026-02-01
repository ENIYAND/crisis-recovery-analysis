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

---

## 9️⃣ Key Insights & Findings

- Customer churn risk spikes **after clusters of negative sentiment**
- Hygiene issues show **strong geographic concentration**
- Crisis exposure combined with recency is a stronger churn signal than lifetime value
- Early sentiment shifts precede SLA degradation

These insights enable **proactive crisis recovery**, not reactive firefighting.

---

## 🔟 This project demonstrates:

- Strong problem framing
- Clean lakehouse architecture
- Explainable AI design
- Business-first ML decisions
- Production-grade documentation

It reflects how **real organizations build crisis intelligence systems** —
not just how models are trained.
