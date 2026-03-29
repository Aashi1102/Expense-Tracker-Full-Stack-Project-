# 💸 Expense Tracker (Full Stack Project)

A full-stack Expense Tracker application built using **Streamlit (Frontend)**, **FastAPI (Backend)**, and **MySQL (Database)**.

🚀 This project enables users to **add, update, manage, and analyze daily expenses** through an intuitive and interactive interface.

---

## 🧠 Project Architecture

Frontend (Streamlit) → Backend (FastAPI) → Database (MySQL)

* **Frontend** → Handles UI and user interaction
* **Backend** → Manages API logic and data processing
* **Database** → Stores persistent expense data

---

## 🚀 Features

✅ Add & update daily expenses
✅ Dynamic row-based input system
✅ Delete expenses easily
✅ Auto-calculated total spending
✅ Category-wise analytics
✅ Persistent storage using MySQL
✅ Clean REST API using FastAPI

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

## 📸 Screenshots (Add This 👇)

<img width="1761" height="1001" alt="Screenshot 2026-03-28 132104" src="https://github.com/user-attachments/assets/00a918c9-f91e-408a-a5fc-87991ac13529" />


<img width="917" height="844" alt="Screenshot 2026-03-28 132145" src="https://github.com/user-attachments/assets/c93e3690-9ed5-481a-8d02-86901dfa831f" />


* Add Expense UI
* Analytics Dashboard
* Dynamic Row Input

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
├── requirements.txt
└── README.md
```

---

## 🔁 How It Works

### 1️⃣ Load Data

* User selects a date
* Frontend sends GET request
* Backend fetches data from MySQL
* Data displayed in UI

### 2️⃣ Edit Data

* User adds/updates rows
* Stored temporarily using `session_state`

### 3️⃣ Save Data

* Frontend sends POST request
* Backend replaces old records
* Updated data stored in database

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

| Column       | Type          |
| ------------ | ------------- |
| id           | INT (PK)      |
| expense_date | DATE          |
| amount       | INT           |
| category     | VARCHAR       |
| notes        | VARCHAR       |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/Aashi1102/Expense-Tracker-Full-Stack-Project-.git
cd Expense-Tracker-Full-Stack-Project-
```

### 2️⃣ Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn server:app --reload
```

### 3️⃣ Frontend Setup

```
cd frontend
streamlit run app.py
```

### 4️⃣ Database Setup

* Open MySQL Workbench
* Run `database/schema.sql`

---

## 🎯 Key Learning Outcomes

* Full-stack architecture (Frontend + Backend + DB)
* REST API development using FastAPI
* State management using Streamlit
* MySQL integration & CRUD operations
* Real-world project structuring

---

## 📌 Future Improvements

* 🔐 User authentication system
* 📊 Interactive dashboards & charts
* 📅 Monthly/Yearly reports
* 📥 Export to Excel / PDF
* 🌐 Deployment (Render / Railway)

---

## 👩‍💻 Author

**Aashi Tomar**

---

⭐ If you found this useful, consider giving it a star!
