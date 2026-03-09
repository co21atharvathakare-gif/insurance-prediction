# 💰 Insurance Premium Predictive Analytics

An end-to-end Machine Learning project that predicts health insurance premiums based on individual risk factors. This project includes a trained Linear Regression model and a live interactive dashboard built with Streamlit.

## 🚀 Live Demo
https://insurance-prediction-atharva.streamlit.app/

## 📊 Business Problem
Insurance companies need accurate cost projections to set fair and profitable premiums. This project analyzes how lifestyle choices (like smoking) and biological factors (Age/BMI) impact the final cost to the insurer.

## 🔍 Key Insights
- **The "Smoking Tax":** Smoking is the single largest driver of cost. On average, being a smoker adds **~$23,800** to the annual premium.
- **Risk Multipliers:** For non-smokers, high BMI has a linear increase in cost. However, for smokers, Obesity (BMI > 30) acts as a "risk multiplier," causing costs to skyrocket to over **$40,000**.
- **The Top 5%:** 100% of the most expensive customers (top 5% by cost) are smokers.

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy)
- **Scikit-Learn** (Linear Regression)
- **Streamlit** (Deployment & UI)
- **Joblib** (Model Serialization)

## 📂 Project Structure
- `app.py`: The Streamlit web application.
- `insurance_model.pkl`: The saved trained model.
- `requirements.txt`: Necessary libraries for deployment.
- `insurance.csv`: The raw dataset.
