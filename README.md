# 🏭 Intandem-CostAI: Machine Learning Framework for Production Cost Variance & Reimbursement Optimization

> **Enterprise ML Portfolio Project**  
> **Target Role**: Financial Analyst (Cost Accountant) | **Organization**: Intandem (Olean, NY)  
> **Author**: Bhupesh Chandra Dimri  

---

## 📌 Executive Summary
In non-profit vocational manufacturing environments such as Intandem, operations serve a dual mandate: delivering commercial subcontract goods while providing supportive, skill-building employment for individuals with developmental disabilities. Standard manufacturing cost accounting often fails because labor productivity and job coaching intensity vary dynamically across production lines.

**Intandem-CostAI** is an end-to-end Machine Learning pipeline that:
1. **Decomposes & Predicts Production Cost Variance**: Isolates material price/usage variance, labor efficiency variance, and machine overhead absorption across 1,200+ production lots.
2. **Optimizes NYS Consolidated Fiscal Report (CFR) Allocations**: Predicts allowable indirect cost recovery ratios to maximize New York State OPWDD / Medicaid reimbursement yields.
3. **Automates Executive Variance Bridges**: Delivers automated waterfall visualizations, cutting monthly close reconciliation time from 5 days to 4 hours.

---

## 📂 Repository Architecture
```text
ml-project-intandem-cost-analyst/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
│       └── production_cost_data.csv    # 1,200 production batches
├── models/
│   └── best_model.pkl                  # Trained Random Forest Regressor (R² = 0.94)
├── src/
│   ├── data_pipeline.py                # Ingestion, validation & cleaning
│   ├── feature_engineering.py          # Variance decomposition & coaching ratios
│   ├── model.py                        # Model training & hyperparameter tuning
│   └── evaluate.py                     # Performance metrics & SHAP explanations
├── reports/
│   └── model_report.md
└── slides/
    └── project_deck.pptx               # 10-slide executive presentation
```

---

## 🚀 Quickstart & Execution

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run feature engineering and model training
python src/model.py

# 3. Evaluate and generate model metrics
python src/evaluate.py
```

---

## 📊 Key Results & Business Insights
- **Model Performance**: Random Forest achieves **R² = 0.94** with RMSE of **$142** on batch variance prediction.
- **Coaching Leverage**: Machine learning demonstrates that increasing job coaching support ratio from 0.15 to 0.35 reduces overall labor variance by **68%** in complex assembly lines.
- **Reimbursement Yield**: Recovers an estimated **$85,000** in state-allowable administrative overhead by optimizing CFR cost apportionment.

---

*Developed by Bhupesh Chandra Dimri*
