# 🌟 Pregnancy Birthweight Predictor 🌟

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-1.1.2-orange?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.25.2-green?logo=scikitlearn)

---

## 💡 Overview

The **Pregnancy Birthweight Predictor** is a **web-based application** that predicts a newborn’s birthweight using maternal and pregnancy features.
It uses **machine learning** to help estimate birthweight based on gestation period, maternal age, height, weight, parity, and smoking status.

---

## ✨ Features

* 🍼 Predict newborn birthweight in **real-time**
* 🧮 Uses features like:

  * Gestation (days)
  * Parity (first pregnancy or not)
  * Mother’s age
  * Height & weight
  * Smoking status
* 🌐 Responsive, clean web interface
* 💻 Built with **Python**, **Flask**, and **scikit-learn**

---

## 🛠️ Technologies Used

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| Python 3.11    | Backend & ML            |
| Flask          | Web framework           |
| scikit-learn   | Machine learning models |
| pandas & numpy | Data handling           |
| joblib         | Save & load models      |
| HTML & CSS     | Frontend design         |

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/Pregnancy-birthweight-Predictor.git
cd Pregnancy-birthweight-Predictor/website
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv env
.\env\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Place trained model files

* `birthweight_predictor.pkl`
* `scaler.pkl`

> Both should be in the same folder as `app.py`

### 5️⃣ Run the application

```bash
python app.py
```

Open **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser 🌐

---

## 🎨 Usage

1. Fill in the form with maternal and pregnancy details
2. Click **Predict**
3. The predicted birthweight appears below the form 🍼

---

## 📂 File Structure

```
Pregnancy-birthweight-Predictor/
│
├─ app.py                     # Flask application
├─ birthweight_predictor.pkl   # Trained ML model
├─ scaler.pkl                  # Scaler for input normalization
├─ templates/
│   └─ index.html              # Web page template
├─ env/                        # Virtual environment
├─ requirements.txt            # Dependencies
└─ README.md                   # Project documentation
```

---

## 📊 Model Information

* ✅ Models used: Linear Regression, Random Forest, Gradient Boosting
* 🧩 Features: gestation, parity, age, height, weight, smoking status, BMI, gestation weeks
* 🔍 R² Score: \~0.29–0.30

---

## 🌈 Future Improvements

* Upgrade to **XGBoost / LightGBM** for higher accuracy
* Include **additional maternal factors**: nutrition, genetics, blood pressure
* Improve frontend with **sliders, tooltips, charts**
* Add **metric unit support** with automatic conversion

---
