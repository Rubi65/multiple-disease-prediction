# 🧑‍⚕️ AI-Powered Multiple Disease Prediction System

This is a comprehensive healthcare solution developed using **Machine Learning** and **Streamlit**. The application provides an interactive interface for predicting three major health conditions: **Diabetes**, **Heart Disease**, and **Parkinson's Disease**, based on clinical data.

## 🚀 Features
- **User Authentication:** Secure Sign-Up and Login system for personalized access.
- **Diabetes Prediction:** Predicts diabetic status using clinical parameters like Glucose, Insulin, and BMI.
- **Heart Disease Prediction:** Analyzes cardiac metrics (Age, Cholesterol, Heart Rate) to detect potential risks.
- **Parkinson's Prediction:** Uses vocal and physical data to identify early signs of Parkinson's.
- **Interactive UI:** A clean, multi-page dashboard built with Streamlit for a seamless experience.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Framework:** Streamlit (UI/UX)
- **ML Libraries:** Scikit-Learn, NumPy, Pandas, Pickle
- **Security:** Streamlit-Authenticator (YAML-based storage)

## 📁 Project Structure
```text
├── dataset/             # Dataset files used for training
├── saved_models/        # Pre-trained .sav model files
├── app.py               # Main application entry point
├── config.yaml          # Encrypted user database (Auto-generated)
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
⚙️ Installation & Local Setup
Clone the Repository:

Bash
git clone https://github.com/Rubi65/multiple-disease-prediction.git

Install Dependencies:
Bash
pip install -r requirements.txt
Run the Application:

Bash
streamlit run app.py


🌐 Deployment:
## 🚀 Deployment
The application is successfully deployed and live on **Streamlit Cloud**.

**Live App Link:** https://multiple-disease-prediction-gkzrtg2fnolxwbq7av9rgb.streamlit.app/

📚 Acknowledgements & References
This project is a combination of guided learning and custom development:

Learning Resources: Logic building and ML concepts were supported by tutorials from YouTube and Google Search.

AI Assistance: Gemini AI was utilized for code optimization, debugging, and documentation support.

Custom Implementation: I have personally designed and integrated the authentication flow, multi-page navigation logic, and final deployment setup to ensure a functional and user-friendly experience.
