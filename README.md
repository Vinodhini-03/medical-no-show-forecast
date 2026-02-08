# 🏥 Medical Appointment No-Show Prediction & Demand Forecasting

> **AI-powered system to predict patient no-shows and forecast appointment demand using Machine Learning**

---

## 🎯 Problem Statement

Healthcare clinics face two major challenges:
1. **31.8% no-show rate** → Wasted resources, lost revenue
2. **Unpredictable demand** → Poor staffing, long wait times

**Solution:** Build ML models to predict no-shows and forecast daily appointment volumes.

---

## 📊 Results Achieved

|------------------------|---------------|----------|-------|-------------------|--------------|
|         Task           |     Model     |Key Metric|Target |     Result        |    Status    |
|------------------------|---------------|----------|-------|-------------------|--------------|
| **No-Show Prediction** | Random Forest | F1-Score | >0.70 | **0.7261**        | ✅ Exceeded |
| **No-Show Prediction** | Random Forest | ROC-AUC  | >0.75 | **0.8795**        | ✅ Exceeded |
| **Demand Forecasting** | Random Forest | R²       | >0.65 | **0.7534**        | ✅ Exceeded |
| **Demand Forecasting** | Random Forest | MAE      | -     | **±80 appts/day** | ✅ Good     |
|------------------------|---------------|----------|-------|-------------------|--------------|

**Business Impact:**
- 🎯 Catches **74% of no-shows** (vs 34% baseline)
- 💰 Potential savings: **$140,000+** per period
- ⚡ **35% efficiency gain** in staffing

---

## 🛠️ Tech Stack

**Core:** Python • Pandas • NumPy • Scikit-learn  
**ML Models:** Random Forest • XGBoost • LightGBM • CatBoost  
**Visualization:** Matplotlib • Seaborn • Plotly  
**Deployment:** Streamlit • Joblib

---

## 📁 Project Structure
```
medical-no-show-forecast/
├── data/                   
├── notebooks/              
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing_FeatureEngineering.ipynb
│   ├── 03_Classification_NoShow.ipynb
│   └── 04_TimeSeries_DemandForecast.ipynb
├── models/                  
├── utils/                   
├── pages/                   
├── app.py                   
└── requirements.txt
```

---

## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/Vinodhini-03/medical-no-show-forecast.git
cd medical-no-show-forecast

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

**Access:** Open browser at `http://localhost:8501`

---

## 📈 Methodology

### 1️⃣ Data (109,593 appointments)
- **Features:** Patient demographics, location, specialty, weather, SMS reminders
- **Preprocessing:** Handled 20% missing data, created 28+ engineered features
- **Class Imbalance:** Applied SMOTE for 68:32 show/no-show ratio

### 2️⃣ Models Compared
**Classification (No-Show):**
- Baseline Logistic Regression
- Random Forest ⭐ **WINNER**
- XGBoost, LightGBM, CatBoost, Gradient Boosting

**Forecasting (Demand):**
- Baseline (Naive)
- ARIMA
- Random Forest ⭐ **WINNER**
- XGBoost

### 3️⃣ Key Features (by importance)
1. **Location-based historical no-show rate** (most predictive!)
2. Geographic location (city)
3. Weather conditions (rain, temperature)
4. Disability + age interaction
5. SMS reminder status

---

## 💡 Key Insights

✅ **Location matters most** → Target high-risk areas with interventions  
✅ **Weather impacts attendance** → Send extra reminders on rainy days  
✅ **SMS reminders work** → Automated messaging reduces no-shows  
✅ **Weekly patterns clear** → Mondays busier, Fridays slower

---

## 🎨 Streamlit Application

**Two Interactive Modules:**

1️⃣ **No-Show Risk Predictor**
   - Input patient details
   - Get real-time risk score (0-100%)
   - Actionable recommendations

2️⃣ **Demand Forecaster**
   - Select date range
   - View predicted appointment volumes
   - Visual charts for planning

---

## 🎓 Skills Demonstrated

✅ End-to-end ML pipeline  
✅ Handling imbalanced data (SMOTE)  
✅ Feature engineering  
✅ Model comparison & selection  
✅ Time series forecasting  
✅ Web app deployment (Streamlit)  
✅ Business impact analysis  

---

## 📌 Future Improvements

- [ ] Real-time integration with hospital systems
- [ ] Automated SMS notifications (Twilio)
- [ ] Multi-specialty forecasting
- [ ] Mobile app version
- [ ] A/B testing framework

---

