# 🧠 Customer Churn Prediction App

A machine learning web application built using **Streamlit** that predicts whether a customer will churn (i.e., leave a service) or not, based on various input features like contract type, internet service, monthly charges, etc.

---

📌 Demo
🔗 [GitHub Repository](https://github.com/Asphane/customer-churn-prediction)
🔗 [Click here to view the deployed app](https://customer-churn-prediction-dhqsdgk9us9b7aenutmccn.streamlit.app/)

---

📊 Problem Statement

Customer churn is a major concern for subscription-based businesses. By predicting potential churn, businesses can take preemptive action to retain customers. This project uses a logistic regression model trained on customer data to make predictions in real-time.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Libraries**:  
  - scikit-learn  
  - pandas  
  - numpy  
  - joblib  
- **Deployment**: Local system / Streamlit Cloud

---

## 📂 Project Structure

```
├── app.py                   # Streamlit app code  
├── model.ipynb              # Jupyter Notebook - data analysis & model training  
├── model.pkl                # Saved trained model  
├── scaler.pkl               # Scaler used to normalize inputs  
├── columns.pkl              # Feature column names used during training  
├── requirements.txt         # Required Python packages  
└── README.md                # Project overview
```

---

🚀 How to Run the App Locally

1️⃣ Clone the repository

```bash
git clone https://github.com/Asphane/customer-churn-prediction.git
cd customer-churn-prediction
```

2️⃣ Install the dependencies

Make sure you have Python 3 installed.

```bash
pip install -r requirements.txt
```

3️⃣ Run the app

```bash
streamlit run app.py
```

The app will automatically open in your browser.

---

🧪 Model Details

- **Algorithm**: Logistic Regression  
- **Scaler**: StandardScaler  
- **Training Score**: *[You can fill your accuracy here]*  
- **Input Features**:  
  - Gender, SeniorCitizen, Partner, Dependents, Tenure, InternetService, Contract, etc.

---

📈 Sample Inputs

In the app, you'll be prompted to enter:

- Gender: `Male` / `Female`  
- SeniorCitizen: `Yes` / `No`  
- Tenure: `0 - 72`  
- InternetService: `DSL` / `Fiber optic` / `No`  
- Contract: `Month-to-month` / `One year` / `Two year`  
- MonthlyCharges: `e.g. 75.50`  
- And more...

The app returns:  
🔹 **Yes** if the customer is likely to churn  
🔹 **No** if the customer is likely to stay

---

📌 Future Improvements

- Deploy on Streamlit Cloud or Hugging Face Spaces  
- Add visualizations  
- Use more advanced models like Random Forest or XGBoost  
- Improve UI with CSS

---

🙋‍♀️ Author

- **Name**: Bisakh Patra  
- **GitHub**: (https://github.com/Asphane)  
- **LinkedIn**: (https://www.linkedin.com/in/bisakh-patra-1396b5251/)

---

⭐️ Show your support

If you like this project, please ⭐️ the repo and share it with others!
