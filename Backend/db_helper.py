from contextlib import contextmanager
import mysql.connector

@contextmanager
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    cursor = conn.cursor(dictionary=True)
    try:
        yield conn, cursor
    finally:
        cursor.close()
        conn.close()


def insert_expenses_bulk(expense_date, expenses):
    with get_db_connection() as (conn, cursor):
        values = [
            (expense_date, e.amount, e.category, e.notes)
            for e in expenses
        ]

        cursor.executemany(
            """
            INSERT INTO expenses (expense_date, amount, category, notes)
            VALUES (%s, %s, %s, %s)
            """,
            values
        )

        conn.commit()

def delete_expenses_for_date(expense_date):
    with get_db_connection() as (conn, cursor):
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )
        conn.commit()


def fetch_expenses_for_date(expense_date):
    with get_db_connection() as (conn, cursor):
        cursor.execute(
            "SELECT * FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )
        return cursor.fetchall()
    

def fetch_expense_summary(start_date, end_date):
    with get_db_connection() as (conn, cursor):
        cursor.execute("""
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
        """, (start_date, end_date))

        return cursor.fetchall()
