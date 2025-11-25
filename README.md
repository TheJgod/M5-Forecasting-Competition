# M5 Kaggle Forecasting — Promo Features & Foundation Models

This project addresses the **M5 Kaggle time-series forecasting challenge**, with a focus on **promo-aware feature engineering** and **benchmarking diverse forecasting approaches**.

---

## 🚀 Feature Engineering
- **Calendar & Price Features**: Designed rich features to capture seasonality, holidays, and pricing dynamics.  
- **Promo Detection Pipeline**: Rolling-median method to:
  - Identify discount periods.
  - Compute stable **absolute** and **relative** price reductions.

---

## 📊 Modeling Benchmark
Tested a wide spectrum of models:

| Category | Models |
|----------|--------|
| Statistical | Traditional time-series methods |
| Machine Learning | XGBoost, LightGBM |
| Deep Learning | N-HiTS, RNNs |
| Foundational Model | TimesFM |

> **TimesFM** consistently outperformed the strongest ML baseline by **~3–5%**, showing robust **cross-series generalization**.

---

## 🛠 End-to-End Workflow
- **Data Preparation**  
- **Feature Engineering**  
- **Model Training & Evaluation**  
- **Model Comparison & Analysis**  

This workflow is fully **reproducible**, enabling straightforward experimentation and benchmarking.

---

## 🔑 Key Takeaways
- Advanced promo-aware features improve forecast accuracy.  
- Foundational models like **TimesFM** excel in **cross-series generalization**.  
- Combining statistical, ML, and deep learning models provides a **comprehensive performance benchmark**.
