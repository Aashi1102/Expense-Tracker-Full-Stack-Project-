
import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload, timeout=5)

        if response.status_code != 200:
            st.error(f"API Error: {response.status_code}")
            st.text(response.text)
            return

        if not response.text.strip():
            st.error("Empty response from server")
            return

        try:
            data = response.json()
        except ValueError:
            st.error("Invalid JSON response from server")
            st.text(response.text)
            return

        if not data:
            st.warning("No data available for selected date range")
            return



        data_dict = data  # this is your JSON

        data = {
            "Category": list(data_dict.keys()),
            "Total": [data_dict[category]["total"] for category in data_dict],
            "Percentage": [data_dict[category]["percentage"] for category in data_dict]
        }



        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")
        st.bar_chart(data = df_sorted.set_index("Category")["Percentage"])


        st.table(df_sorted)
