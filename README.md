# 📊 CSV Upload to Firebase using Streamlit 🚀

## 📌 Project Overview
This project is a web application developed using Streamlit. It allows users to upload a CSV file, preview the data, and store it in Firebase Firestore database.

---

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Firebase Firestore

---

## 📂 Project Files
- app.py → Main application file  
- firebase-key.json → Firebase credentials file  
- README.md → Documentation  

---

## ⚙️ How to Run the Project (Step-by-Step)

### Step 1: Install Required Libraries
Open terminal and run:

pip install streamlit pandas firebase-admin

---

### Step 2: Setup Firebase
1. Go to Firebase Console  
2. Create a new project  
3. Enable Firestore Database  
4. Go to Project Settings → Service Accounts  
5. Download the JSON key file  
6. Rename it to:

firebase-key.json

7. Place it in the project folder  

---

### Step 3: Run the Application
In terminal, run:

streamlit run app.py

---

### Step 4: Open in Browser
The app will open automatically at:

http://localhost:8501

---

## 📊 How to Use
1. Click on "Upload CSV File"  
2. Select your CSV file  
3. Preview the data  
4. Click "Upload to Firebase"  
5. Data will be stored in Firebase  

---

## 📸 Screenshots

Upload CSV File
![image alt](https://github.com/mueez-ahmed08/csv-to-firebase-streamlit/blob/bb104008bd76b716cebbb78455073e8beee929b0/DSP1.JPG)

Data Preview
![upload Screen](DSP2)

Data Stored in Firebase
![upload Screen](DSP3)


## ⚠️ Common Issues

- Firebase key file missing → Place firebase-key.json in project folder  
- Permission denied → Enable Firestore Database  
- App not running → Install required libraries  

---

## 🎯 Features
- Upload CSV file  
- Preview data  
- Store data in cloud (Firebase)  
- Simple user interface  

---

## 👨‍💻 Author
Mueez Qureshi  
GitHub: https://github.com/mueez-ahmed08  

---

## 📌 Conclusion
This project demonstrates how to build a simple web application using Streamlit and integrate it with Firebase for storing data online.
