# Test Expense Class

from finance_tracker.expense import Expense

expense = Expense(
    "2026-07-01",
    500,
    "Food",
    "Lunch"
)

print("Expense Created Successfully!")
print(expense.to_dictionary())
