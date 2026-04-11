# 📩 SMS Spam Classifier

A Machine Learning web application that classifies SMS messages as **Spam 🚨** or **Ham ✅** using TF-IDF and Naive Bayes algorithm.

---

## 📸 Demo

<p align="center">
  <img src="screenshot.png" width="500"/>
</p>

---

## 🚀 Features

- Real-time SMS classification
- Clean and simple UI
- Text preprocessing using Regular Expressions
- TF-IDF vectorization
- Naive Bayes Machine Learning model

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy

---

## 📂 Project Structure


sms-spam-classifier/
│
├── app.py
├── save_model.sav
├── vectorizer.pkl
├── spam.csv
├── Requirement.txt
├── screenshot.png
│
├── templates/
│ └── index.html
│
└── SMS_spam_Classifier.ipynb


---

## ⚙️ How It Works

1. User enters a message
2. Text is cleaned using Regular Expressions
3. Converted into numerical form using TF-IDF
4. Naive Bayes model predicts:
   - Spam 🚨
   - Ham ✅

---

## ▶️ How to Run Locally

### 🚀 Step 1: Clone the repository

```bash
git clone https://github.com/rajaji98/sms-spam-classifier.git
cd sms-spam-classifier


⚙️ Step 2: Install dependencies
pip install -r Requirement.txt


▶️ Step 3: Run the application
python app.py


🌐 Step 4: Open in browser
http://127.0.0.1:5000
📊 Model Details
Algorithm: Multinomial Naive Bayes
Feature Extraction: TF-IDF
Accuracy: ~80%


🎯 Future Improvements
Deploy the app online (Render / Railway)
Improve UI/UX
Use Deep Learning models (LSTM / BERT)
Add API support


💼 Author

Arun Singh
Aspiring Data Science Engineer 🚀