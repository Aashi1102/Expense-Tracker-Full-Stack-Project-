# # CRUD = CREATE, READ,UPDATE,DELETE
# import mysql.connector
# from contextlib import contextmanager
# from logger_setup import setup_logger

# logger = setup_logger('db_helper')

# @contextmanager

# def get_db_cursor(commit = False):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root",
#         database="expense_manager"
#     )
#     if mydb.is_connected():
#         print("connected")
#     else:
#         print("not connected")


#     conn = mydb.cursor(dictionary=True)
#     yield conn


#     if commit:
#         mydb.commit()

#     conn.close()
#     mydb.close()


# # def fetch_all_records():
# #     with get_db_cursor() as conn:
# #         conn.execute("SELECT * FROM expenses")
# #         exp = conn.fetchall()
# #         for expense in exp:
# #             print(expense)


# def fetch_expenses_for_date(expense_date):
#     logger.info(f"fetch expense for date called with {expense_date}")
#     with get_db_cursor() as conn:
#         conn.execute("SELECT * FROM expenses WHERE expense_date = %s",(expense_date,))
#         expenses = conn.fetchall()
#         return expenses


# def delete_expenses(expense_date):
#     logger.info(f"delete expense for date called with {expense_date}")

#     with get_db_cursor(commit= True) as conn:
#         conn.execute("DELETE FROM expenses WHERE expense_date = %s",(expense_date,)
#         )


# def insert_expense(expense_date,amount,category,notes):
#     # with get_db_cursor() as conn:
#     logger.info(f"insert expense called with date :{expense_date},amount :{amount},category :{category},notes :{notes}")
#     with get_db_cursor(commit = True) as conn:
#         conn.execute(
#             "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",(expense_date,amount,category,notes)
#         )

# def fetch_expense_summary(start_date,end_date):
#     logger.info(f"fetch expense summary for date called with {start_date} and {end_date}")
#     with get_db_cursor(commit = True) as conn:
#             conn.execute(
#                 '''SELECT category, SUM(amount) as total 
#                 FROM expenses 
#                 WHERE expense_date
#                 BETWEEN %s AND %s
#                 GROUP BY category''', (start_date, end_date))
#             data  = conn.fetchall()
#             return data

# if __name__ == "__main__":
#      expenses = fetch_expenses_for_date("2024-08-03")
#      print(expenses)
#      # insert_expense("2025-09-22","309","food","panipuri")
#      # delete_expenses("2025-09-22")
#      summary = fetch_expense_summary("2024-08-03","2024-08-05")
#      for record in summary:
#          print(record)






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