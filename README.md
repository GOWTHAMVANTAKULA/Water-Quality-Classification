# 💧 Water Quality Classification using Machine Learning

## 📌 Project Overview

This project focuses on the comprehensive analysis and classification of water quality using Exploratory Data Analysis (EDA) and Machine Learning techniques. The goal is to evaluate water bodies based on key physicochemical and biological parameters, identify pollution patterns and geographic hotspots, and build an automated system to classify water quality into Use Based Classes (A, B, C, E).

The project supports data-driven decision-making for water resource management and ensures water suitability for purposes such as drinking, bathing, irrigation, and industrial use.

---

## 🎯 Project Objectives

- Clean and preprocess raw water quality data  
- Perform detailed exploratory data analysis to identify pollution trends  
- Analyze district-wise and basin-wise water quality variations  
- Classify water bodies into Use Based Classes (A, B, C, E)  
- Build and optimize machine learning models for accurate classification  
- Deploy the best-performing model using a Streamlit web application  
- Provide actionable insights for environmental monitoring and policy planning  

---

## 🧪 Dataset Description

The dataset contains water quality measurements collected from various monitoring stations, including:

- Physicochemical parameters (pH, Temperature, TDS, Hardness, Conductivity)  
- Biological parameters (BOD, COD, Fecal Coliform, Total Coliform)  
- Dissolved Oxygen (DO)  
- Geographic attributes (District, Basin)  

---

## 🔧 Data Preprocessing Steps

- Dropped irrelevant columns:
  - Use of Water in Down Stream, Remark, STN Code, Month, State Name  

- Cleaned column names and categorical values by removing extra spaces  

- Converted non-numeric entries such as **ND** and **(BDL)** to NaN  

- Converted:
  - Sampling date → datetime  
  - Sampling time → hourly format  

- Handled missing values:
  - Temperature & pH → District-wise mean imputation  
  - Other numeric parameters → District-wise median imputation  

- Generated Use Based Class using rule-based classification (DO, BOD, Total Coliform)  

- Encoded target variable using Label Encoding  

- Addressed class imbalance using **SMOTE**  

---

## 📊 Exploratory Data Analysis (EDA) Summary

### Water Quality Distribution
- 82% of samples classified as Class A (Drinking after disinfection)  
- 11% classified as Class E (Irrigation/Industrial use)  

### Pollution Sources
- Industrial effluents increased BOD and COD  
- Human activities increased Fecal Coliform  

### Geographic Hotspots
- **Critical districts:** Akola, Dhule, Jalgaon, Mumbai, Nashik, Ratnagiri, Solapur, Thane  
- **Polluted basins:** Mahim Creek, Ulhas, Arnala, Bassein  

### pH Imbalance
- Several districts fall outside safe pH range (6.5–8.5)  

### Key Insight
- Clear water ≠ Safe water (high coliform & TDS observed)  

---

## 🤖 Machine Learning Models Implemented

- Random Forest Classifier  
- XGBoost Classifier  
- CatBoost Classifier  

### 🏆 Best Model: CatBoost Classifier
- Weighted F1-score: **0.89**  
- Strong performance across all classes  

---

## 🚀 Model Deployment

### 🖥️ Streamlit Application Features

- Upload CSV file for prediction  
- Automatic preprocessing pipeline  
- Real-time classification into:
  - Safe  
  - Moderately Polluted  
  - Highly Polluted  
- Visualization of key parameters  

---

## 🐳 Docker Implementation

- Created a **Dockerfile** for containerization  
- Optimized build using `.dockerignore`  
- Built Docker image locally  
- Pushed image to **Docker Hub**  

### Benefits:
- Easy deployment  
- Environment consistency  
- Scalable architecture  

---

## ☁️ Deployment on Render

- Deployed Dockerized application on **Render**  
- Connected GitHub repository  
- Enabled continuous deployment  

### 🌐 Live Application:
👉 https://water-quality-prediction-b1mc.onrender.com

## 🧠 Key Findings

- High-quality water coexists with pollution hotspots  
- Industrial discharge significantly degrades water quality  
- Visual clarity is misleading  
- ML models can automate classification effectively  

---

## ✅ Recommendations

- Target polluted districts for remediation  
- Enforce stricter industrial regulations  
- Increase public awareness  
- Implement continuous monitoring systems  
- Use deployed app for real-time classification  

---

## 🛠️ Tools & Technologies Used

- Python  
- pandas, numpy  
- matplotlib, seaborn  
- scikit-learn, xgboost, catboost  
- imbalanced-learn (SMOTE)  
- Streamlit  
- Docker  
- Render  
- joblib  
- Google Colab, VS Code  

---

## 📌 Future Improvements

- Add real-time data integration (IoT sensors)  
- Improve model with deep learning techniques  
- Add user authentication  
- Store predictions in a database instead of CSV  

---

## 🙌 Conclusion

This project demonstrates an end-to-end machine learning pipeline — from data preprocessing and EDA to model building, containerization, and cloud deployment — making it production-ready and scalable.
