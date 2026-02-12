Delays in global supply chain operations can significantly impact operational efficiency, cost structure, and customer satisfaction.
This project aims to predict high shipment delay risk using machine learning techniques based on operational, environmental, and geopolitical indicators.
The model is designed to help decision-makers identify high-risk shipments proactively and simulate risk scenarios under different external conditions.

🎯 Objectives
Identify key factors contributing to shipment delays
Build a classification model to predict high delay risk
Analyze model errors and business implications
Deploy a simple interactive application for real-time risk simulation

🗂 Dataset Description
The dataset includes operational and external risk variables such as:
Geopolitical Risk Index
Weather Severity Index
Shipping Cost (USD)
Order Weight (Kg)
Lead Time Metrics
Disruption Events
Delay Days

A binary target variable was created:
High_Delay_Risk = 1 if Delay_Days > 3
High_Delay_Risk = 0 otherwise

Project Workflow
1️⃣ Data Preparation
Data loading and integrity checking
Missing value handling
Date transformation
Feature engineering:
Cost_per_Kg
Risk threshold indicators
Time-based features
Removal of potential data leakage variables

2️⃣ Exploratory Data Analysis
Target distribution analysis
Correlation heatmap for numerical features
Identification of operational risk drivers

Key observation:
Geopolitical Risk Index and Weather Severity Index show positive correlation with shipment delays.

3️⃣ Modeling Approach
Stratified train-test split (80/20)
Random Forest Classifier with class balancing
5-fold cross-validation using ROC-AUC
Performance evaluation using:
Classification Report
ROC-AUC Score
Confusion Matrix
Probability Distribution Analysis

📊 Model Performance
The model demonstrates stable performance across cross-validation folds.
Key evaluation focus:
Minimizing false negatives (undetected high-risk delays)
Maintaining balanced precision-recall performance
False negatives are considered more critical in a supply chain context due to operational disruption risk.

🔍 Error Analysis
Confusion matrix used to evaluate misclassification patterns
Probability distribution analyzed to assess model confidence
Business impact considered in interpreting prediction errors

🚀 Deployment
The trained model is saved using joblib and integrated into a Streamlit application that allows users to simulate delay risk probability based on:
Geopolitical Risk Index
Weather Severity Index
Cost per Kg
The app outputs:
Risk probability
Risk level (Low / Medium / High)

🧠 Technical Stack
Python
Pandas & NumPy
Scikit-learn
Matplotlib & Seaborn
Joblib
Streamlit

💡 Key Learning Points
Preventing data leakage is critical for reliable model evaluation
External risk indicators significantly influence shipment delays
Model evaluation must consider business cost of misclassification
Deployment thinking is essential beyond model training

📌 Future Improvements
Hyperparameter tuning (GridSearch / RandomizedSearch)
Model comparison (Logistic Regression baseline)
SHAP explainability integration
API-based deployment (FastAPI)

👩‍💻 Author
Nur Ivana Maharani Soamole
Information Systems – Data Science Concentration
President University