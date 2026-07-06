# Name: Saniya Choughule
# Week 4 Project
# Expense Manager

from finance_tracker.expense import Expense


class ExpenseManager:

    # Constructor
    def __init__(self):

        self.expenses = []
        self.budget = 0


    # Add Expense
    def add_expense(self, date, amount, category, description):

        expense = Expense(date, amount, category, description)

        self.expenses.append(expense)

        print("Expense Added Successfully!")


    # View All Expenses
    def view_expenses(self):

        if len(self.expenses) == 0:

            print("\nNo Expenses Found.")
            return

        print("\n" + "=" * 70)
        print("ALL EXPENSES")
        print("=" * 70)

        print(f"{'Date':<15}{'Amount':<12}{'Category':<18}Description")

        print("-" * 70)

        for expense in self.expenses:

            print(
                f"{expense.date:<15}"
                f"{expense.amount:<12}"
                f"{expense.category:<18}"
                f"{expense.description}"
            )


    # Search Expense
    def search_expense(self, keyword):

        found = False

        for expense in self.expenses:

            if keyword.lower() in expense.category.lower() or \
               keyword.lower() in expense.description.lower():

                print("\nExpense Found")
                print("----------------------------")
                print("Date :", expense.date)
                print("Amount :", expense.amount)
                print("Category :", expense.category)
                print("Description :", expense.description)

                found = True

        if not found:

            print("No Matching Expense Found.")


    # Delete Expense
    def delete_expense(self, index):

        if 0 <= index < len(self.expenses):

            del self.expenses[index]

            print("Expense Deleted Successfully.")

        else:

            print("Invalid Expense Number.")


    # Set Budget
    def set_budget(self, amount):

        self.budget = amount

        print("Budget Updated Successfully.")


    # View Budget
    def view_budget(self):

        total = 0

        for expense in self.expenses:

            total += float(expense.amount)

        print("\nBudget :", self.budget)
        print("Total Expenses :", total)
        print("Remaining Budget :", self.budget - total)