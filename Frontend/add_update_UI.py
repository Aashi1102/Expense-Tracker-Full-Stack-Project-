# import streamlit as st
# from datetime import datetime
# import requests

# API_URL = "http://localhost:8000"


# def add_update_tab():
#     selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
#     response = requests.get(f"{API_URL}/expenses/{selected_date}")
#     if response.status_code == 200:
#         existing_expenses = response.json()
#         # st.write(existing_expenses)
#     else:
#         st.error("Failed to retrieve expenses")
#         existing_expenses = []

#     categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

#     with st.form(key="expense_form"):
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.text("Amount")
#         with col2:
#             st.text("Category")
#         with col3:
#             st.text("Notes")

#         expenses = []
#         for i in range(5):
#             if i < len(existing_expenses):
#                 amount = existing_expenses[i]['amount']
#                 category = existing_expenses[i]["category"]
#                 notes = existing_expenses[i]["notes"]
#             else:
#                 amount = 0.0
#                 category = "Shopping"
#                 notes = ""

#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}",
#                                                label_visibility="collapsed")
#             with col2:
#                 category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
#                                               key=f"category_{i}", label_visibility="collapsed")
#             with col3:
#                 notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

#             expenses.append({
#                 'amount': amount_input,
#                 'category': category_input,
#                 'notes': notes_input
#             })

#         submit_button = st.form_submit_button()
#         if submit_button:
#             filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

#             response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
#             if response.status_code == 200:
#                 st.success("Expenses updated successfully!")
#             else:
#                 st.error("Failed to update expenses.")

import streamlit as st
import requests
from datetime import date

API_URL = "http://localhost:8000"

def fetch_existing_expenses(selected_date):
    try:
        response = requests.get(
            f"{API_URL}/expenses/{selected_date}",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()
    except:
        pass

    return []
    

def add_update_tab():

    categories = ["Rent", "Food", "Shopping", "Transport", "Bills", "Other"]

    st.title("Expense Tracker")

    selected_date = st.date_input("Select Date", date.today())

    # ✅ Detect date change
    if "last_date" not in st.session_state:
        st.session_state.last_date = selected_date

    if st.session_state.last_date != selected_date:
        st.session_state.last_date = selected_date
        
        existing_data = fetch_existing_expenses(selected_date)

        if existing_data:
            st.session_state.rows = existing_data
        else:
            st.session_state.rows = [{"amount": 0.0, "category": "Rent", "notes": ""}]

        st.rerun()

    if "rows" not in st.session_state:
        existing_data = fetch_existing_expenses(selected_date)

        if existing_data:
            st.session_state.rows = existing_data
        else:
            st.session_state.rows = [{"amount": 0.0, "category": "Rent", "notes": ""}]    
            
            
    if st.button("➕ Add Row"):
        st.session_state.rows.append({"amount": 0.0, "category": "Rent", "notes": ""})


    updated_expenses = []
    used_categories = set()
    total = 0

    for i, row in enumerate(st.session_state.rows):
        col1, col2, col3, col4 = st.columns([2, 2, 3, 1])

        with col1:
            amount = st.number_input("Amount", min_value=0.0, value=row["amount"], key=f"amount_{i}")

        with col2:
            category = st.selectbox(
                "Category",
                categories,
                index=categories.index(row["category"]) if row["category"] in categories else 0,
                key=f"category_{i}"
            )

        with col3:
            notes = st.text_input(
                "Notes",
                value=row["notes"],
                key=f"notes_{i}"
            )

        with col4:
            if st.button("❌", key=f"delete_{i}"):
                st.session_state.rows.pop(i)
                st.rerun()

        if category in used_categories:
            st.warning(f"Duplicate category: {category}")
        else:
            used_categories.add(category)

        total += amount

        updated_expenses.append({
            "amount": amount,
            "category": category,
            "notes": notes
        })

    st.subheader(f"Total: ₹ {total:.2f}")

    if st.button("Submit"):
        valid_expenses = [e for e in updated_expenses if e["amount"] > 0]

        if not valid_expenses:
            st.error("Please enter at least one valid expense")
        else:
            try:
                response = requests.post(
                    f"{API_URL}/expenses/{selected_date}",
                    json=valid_expenses,
                    timeout=5
                )

                if response.status_code == 200:
                    st.success("Expenses saved successfully!")
                else:
                    st.error(f"Error: {response.status_code}")
                    st.text(response.text)

            except requests.exceptions.RequestException:
                st.error("Server not reachable")


    
