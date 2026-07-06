# Test File Handler

from finance_tracker.expense import Expense
from finance_tracker.file_handler import save_expenses, export_csv

expenses = [
    Expense("2026-07-01", 500, "Food", "Lunch"),
    Expense("2026-07-02", 200, "Transport", "Bus")
]

save_expenses(expenses)
export_csv(expenses)

print("File Handler Test Completed Successfully!")