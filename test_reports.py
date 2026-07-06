# Test Reports

from finance_tracker.expense import Expense
from finance_tracker.reports import (
    monthly_report,
    category_report,
    statistics,
    expense_chart
)

expenses = [
    Expense("2026-07-01", 500, "Food", "Lunch"),
    Expense("2026-07-02", 300, "Transport", "Bus"),
    Expense("2026-07-03", 1000, "Shopping", "Shoes")
]

monthly_report(expenses)
category_report(expenses)
statistics(expenses)
expense_chart(expenses)