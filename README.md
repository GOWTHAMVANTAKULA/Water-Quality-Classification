**💧 Water Quality Classification using Machine Learning**

**📌 Project Overview**

This project focuses on the comprehensive analysis and classification of water quality using Exploratory Data Analysis (EDA) and Machine Learning techniques. The goal is to evaluate water bodies based on key physicochemical and biological parameters, identify pollution patterns and geographic hotspots, and build an automated system to classify water quality into Use Based Classes (A, B, C, E).

The project supports data-driven decision-making for water resource management and ensures water suitability for purposes such as drinking, bathing, irrigation, and industrial use.

**🎯 Project Objectives**

1. Clean and preprocess raw water quality data

2. Perform detailed exploratory data analysis to identify pollution trends

3. Analyze district-wise and basin-wise water quality variations

4. Classify water bodies into Use Based Classes (A, B, C, E)

5. Build and optimize machine learning models for accurate classification

6. Deploy the best-performing model using a Streamlit web application

7. Provide actionable insights for environmental monitoring and policy planning

**🧪 Dataset Description**

* The dataset contains water quality measurements collected from various monitoring stations, including:

* Physicochemical parameters (pH, Temperature, TDS, Hardness, Conductivity)

* Biological parameters (BOD, COD, Fecal Coliform, Total Coliform)

* Dissolved Oxygen (DO)

* Geographic attributes (District, Basin)

**🔧 Data Preprocessing Steps**

* Dropped irrelevant columns:

* Use of Water in Down Stream, Remark, STN Code, Month, State Name

* Cleaned column names and categorical values by removing extra spaces

* Converted non-numeric entries such as ND and (BDL) to NaN

**Converted:**

* Sampling date → datetime

* Sampling time → hourly format

* Handled missing values:

* Temperature & pH: District-wise mean imputation

* Other numeric parameters: District-wise median imputation

* Generated Use Based Class using rule-based classification (DO, BOD, Total Coliform)

* Encoded target variable using Label Encoding

* Addressed class imbalance using SMOTE (Synthetic Minority Oversampling Technique)

**📊 Exploratory Data Analysis (EDA) Summary**
1. Water Quality Distribution

* 82% of samples classified as Class A (Drinking after disinfection)

* 11% classified as Class E (Irrigation/Industrial use), indicating localized pollution

2. Pollution Sources

* Industrial effluents and mixed human activities caused high BOD and COD

* Bathing, washing, and idol immersion significantly increased Fecal Coliform

3. Geographic Hotspots

* Districts requiring severe treatment:

* Akola, Dhule, Jalgaon, Mumbai, Nashik, Ratnagiri, Solapur, Thane

4. Highly polluted river basins:

* Mahim Creek, Ulhas, Arnala, Bassein

* pH Imbalance

* Districts such as Akola, Beed, Jalgaon, Jalna, Nagpur, Nanded, and Nashik showed pH outside the safe range (6.5 – 8.5)

* Visual Clarity vs Safety

5. Clear water samples still showed:

* High fecal coliform

* Extremely high TDS (> 3500 mg/L)

* Visual appearance is not a reliable indicator of water safety

* Inter-Parameter Correlations

* Strong correlation between BOD and COD (organic pollution)

* High correlation among TDS, Conductivity, and Hardness (mineral contamination)

**🤖 Machine Learning Models Implemented**

1. Random Forest Classifier

2. XGBoost Classifier

3. CatBoost Classifier

-- Model Optimization

* Class imbalance handled using SMOTE

* Hyperparameter tuning using RandomizedSearchCV

**Best Model Performance**

-- 🏆 CatBoost Classifier

-- Weighted F1-score: 0.89

-- Strong balance between precision and recall across all water quality classes

**🚀 Model Deployment using Streamlit**

* An interactive Streamlit web application was developed to make the model accessible to non-technical users.

* Streamlit App Features

* Upload water quality data (CSV file)

* Automatic preprocessing using the trained pipeline

* Real-time prediction of Use Based Water Quality Class (A, B, C, E)

* Visualization of key water quality parameters

**Instant classification of water as:**

1. Safe

2. Moderately Polluted

3. Highly Polluted

4. Deployment Workflow

5. Best model (CatBoost) saved using joblib

6. Same preprocessing logic reused to avoid data leakage

7. Streamlit app loads the trained model for real-time predictions

8. Ready for deployment on Streamlit Cloud or local servers

**🧠 Key Findings**

* High-quality water coexists with critical pollution hotspots

* Industrial discharge significantly degrades water quality

* Visual clarity alone is misleading for safety assessment

* Machine learning models can reliably automate water quality classification

**✅ Recommendations**

* Implement targeted remediation in severely polluted districts and river basins

* Enforce stricter industrial effluent regulations

* Increase public awareness of pollution-causing activities

* Establish continuous water quality monitoring systems

* Deploy the CatBoost + Streamlit application for real-time water quality assessment

**🛠️ Tools & Technologies Used**

1. Python

2. pandas, numpy

3. matplotlib, seaborn

4. scikit-learn, xgboost, catboost

5. imbalanced-learn (SMOTE)

6. Streamlit

7. joblib

8. Google Colab, VS Code
