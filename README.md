# 🍎 NutriTrack AI — Nutrition Dashboard

A web-based nutrition dashboard that helps users track their daily intake of protein, carbohydrates, fats, calories, and iron based on their diet.

This project converts raw food input into meaningful nutritional insights and compares it with recommended daily intake.

---

## 🚀 Features

* 🥗 Add multiple food items with quantity
* 📊 Real-time calculation of:

  * Protein
  * Carbohydrates
  * Fats
  * Calories
  * Iron
* 📈 Visual dashboard:

  * Pie chart (macro distribution)
  * Bar chart (consumed vs required)
* 🎯 Personalized daily requirements based on body weight
* 💡 Smart food suggestions based on nutrient deficiency
* 🌙 Clean and modern UI

---

## 🧠 How It Works

1. User enters weight and food items
2. Frontend sends data to Flask backend
3. Backend processes data using Pandas
4. Nutritional values are calculated from dataset
5. Results are returned and displayed on dashboard

---

## 🛠️ Tech Stack

**Frontend**

* HTML, CSS, JavaScript
* Chart.js

**Backend**

* Python
* Flask
* Pandas

---

## 📁 Project Structure

```
nutrition-app/
│
├── app.py              # Flask backend
├── model.py            # Nutrition logic
├── clean_data.csv      # Dataset
│
└── templates/
    └── index.html      # Frontend UI
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/BitikRaushan/nutrition-dashboard-ai.git
cd nutrition-dashboard-ai
```

---

### 2. Install dependencies

```
pip install flask flask-cors pandas
```

---

### 3. Run the application

```
python app.py
```

---

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 📌 Future Improvements

* 🔍 Search-based food input instead of dropdown
* 📂 Save user history
* 🤖 AI-based diet recommendations
* 🌐 Deployment on cloud (Render / Vercel)
* 🔐 User authentication system

---

## 🙌 Motivation

This project was built to explore how data, backend logic, and frontend UI can be combined to create a useful real-world application.

---

## 📬 Contact

If you want to collaborate or have suggestions, feel free to connect.

---
