# 💸 Expense Tracker (Full Stack Project)

A full-stack Expense Tracker application built using **Streamlit (Frontend)**, **FastAPI (Backend)**, and **MySQL (Database)**.

This project allows users to **add, update, view, and analyze daily expenses** with a simple and interactive UI.

---

## 🧠 Project Architecture

Frontend (Streamlit) → Backend (FastAPI) → Database (MySQL)

* **Frontend**: User Interface (UI)
* **Backend**: Business logic & API handling
* **Database**: Data storage

---

## 🚀 Features

✅ Add and update daily expenses
✅ Dynamic row-based input system
✅ Delete expenses easily
✅ Auto-calculated total spending
✅ Category-wise analytics
✅ Data persistence using MySQL
✅ Clean API structure using FastAPI

---

## 🛠️ Tech Stack

| Layer      | Technology        |
| ---------- | ----------------- |
| Frontend   | Streamlit         |
| Backend    | FastAPI           |
| Database   | MySQL             |
| API Calls  | Requests (Python) |
| Validation | Pydantic          |

---

## 📂 Project Structure

```
Expense-Tracker/
│
├── frontend/
│   ├── app.py
│   ├── add_update_UI.py
│   ├── analytics_UI.py
│
├── backend/
│   ├── server.py
│   ├── db_helper.py
│
├── database/
│   ├── schema.sql
│
└── README.md
```

---

## 🔁 How It Works

### 1. Load Data

* User selects a date
* Frontend sends GET request
* Backend fetches data from MySQL
* Data is displayed in UI

### 2. Edit Data

* User adds/updates rows
* Stored in `session_state`

### 3. Save Data

* Frontend sends POST request
* Backend replaces old data
* New data stored in DB

---

## 🔗 API Endpoints

### 📥 Get Expenses

```
GET /expenses/{date}
```

### 📤 Save Expenses

```
POST /expenses/{date}
```

### 📊 Analytics

```
POST /analytics/
```

---

## 🗄️ Database Schema

**Table: expenses**

| Column       | Type  |
| ------------ | ----- |
| expense_date | DATE  |
| amount       | FLOAT |
| category     | TEXT  |
| notes        | TEXT  |

---

## ⚙️ Setup Instructions

### 1. Clone Repo

```
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2. Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn server:app --reload
```

### 3. Frontend Setup

```
cd frontend
streamlit run app.py
```

### 4. Database Setup

* Create MySQL database
* Run schema.sql

---

## 🎯 Key Learning Outcomes

* Full-stack architecture understanding
* API design using FastAPI
* State management using Streamlit
* Database integration (CRUD operations)
* Real-world project structure

---

## 📌 Future Improvements

* User authentication
* Monthly reports
* Charts & visual dashboards
* Export to Excel/PDF

---

## 👩‍💻 Author

**Aashi Tomar**

---

⭐ If you like this project, don't forget to star the repo!
