# test_db_helper.py
# this 3 line use becoase project have two backend files so it helps this file to find main backend db_helper file
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend import db_helper


def test_fetch_expenses_for_date():
    expense = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expense) == 1
    assert expense[0]["amount"] == 10.0
    assert expense[0]["category"] == "Shopping"
    assert expense[0]["notes"] == "Bought potatoes"


def test_fetch_expenses_for_date_invalid_date():
    expense = db_helper.fetch_expenses_for_date("9999-08-15")
    assert len(expense) == 0



def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_su mmary("9854-08-12","2332-08-15")
    assert len(summary) == 0
