from contextlib import contextmanager
import mysql.connector
import os

# Optional: load from environment variables (recommended)
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": os.getenv("DB_PASSWORD", "root"),  # fallback for local
    "database": "expense_manager"
}


@contextmanager
def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    try:
        yield conn, cursor
    except Exception as e:
        print("Database error:", e)
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()


# ✅ INSERT (Bulk - Optimized)
def insert_expenses_bulk(expense_date, expenses):
    if not expenses:
        return

    with get_db_connection() as (conn, cursor):
        values = [
            (expense_date, e.amount, e.category, e.notes)
            for e in expenses
        ]

        try:
            cursor.executemany(
                """
                INSERT INTO expenses (expense_date, amount, category, notes)
                VALUES (%s, %s, %s, %s)
                """,
                values
            )
            conn.commit()
        except Exception as e:
            print("Insert error:", e)
            conn.rollback()
            raise


# ✅ DELETE
def delete_expenses_for_date(expense_date):
    with get_db_connection() as (conn, cursor):
        try:
            cursor.execute(
                "DELETE FROM expenses WHERE expense_date = %s",
                (expense_date,)
            )
            conn.commit()
        except Exception as e:
            print("Delete error:", e)
            conn.rollback()
            raise


# ✅ FETCH (Improved)
def fetch_expenses_for_date(expense_date):
    with get_db_connection() as (conn, cursor):
        cursor.execute(
            """
            SELECT id, expense_date, amount, category, notes
            FROM expenses
            WHERE expense_date = %s
            ORDER BY id
            """,
            (expense_date,)
        )
        return cursor.fetchall()


# ✅ ANALYTICS (Improved)
def fetch_expense_summary(start_date, end_date):
    with get_db_connection() as (conn, cursor):
        cursor.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            ORDER BY total DESC
            """,
            (start_date, end_date)
        )
        return cursor.fetchall()
