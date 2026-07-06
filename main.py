# Name: Saniya Choughule
# Week 4 Project
# Personal Finance Tracker

from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.utils import validate_amount, validate_date, categories
from finance_tracker.file_handler import (
    save_expenses,
    export_csv,
    backup_data,
    restore_backup,
)
from finance_tracker.reports import (
    monthly_report,
    category_report,
    statistics,
    expense_chart,
)


# Create Expense Manager Object
manager = ExpenseManager()


# Main Menu
def menu():

    while True:

        print("\n" + "=" * 60)
        print("        PERSONAL FINANCE TRACKER")
        print("=" * 60)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Monthly Report")
        print("6. Category Report")
        print("7. Statistics")
        print("8. Expense Chart")
        print("9. Set Budget")
        print("10. View Budget")
        print("11. Export CSV")
        print("12. Backup Data")
        print("13. Restore Backup")
        print("0. Exit")

        choice = input("\nEnter Your Choice : ")

        # Add Expense
        if choice == "1":

            date = input("Enter Date (YYYY-MM-DD): ")

            if not validate_date(date):
                print("Invalid Date Format!")
                continue

            amount = input("Enter Amount : ")

            if not validate_amount(amount):
                print("Invalid Amount!")
                continue

            print("\nCategories")

            for item in categories():
                print("-", item)

            category = input("Enter Category : ")
            description = input("Enter Description : ")

            manager.add_expense(
                date,
                float(amount),
                category,
                description
            )

            save_expenses(manager.expenses)

        # View Expenses
        elif choice == "2":

            manager.view_expenses()

        # Search Expense
        elif choice == "3":

            keyword = input("Enter Category or Description : ")

            manager.search_expense(keyword)

        # Delete Expense
        elif choice == "4":

            manager.view_expenses()

            try:

                index = int(
                    input("Enter Expense Number (starting from 0): ")
                )

                manager.delete_expense(index)

                save_expenses(manager.expenses)

            except ValueError:

                print("Invalid Input!")

        # Monthly Report
        elif choice == "5":

            monthly_report(manager.expenses)

        # Category Report
        elif choice == "6":

            category_report(manager.expenses)

        # Statistics
        elif choice == "7":

            statistics(manager.expenses)

        # Expense Chart
        elif choice == "8":

            expense_chart(manager.expenses)

        # Set Budget
        elif choice == "9":

            try:

                budget = float(input("Enter Monthly Budget : "))

                manager.set_budget(budget)

            except ValueError:

                print("Invalid Budget!")

        # View Budget
        elif choice == "10":

            manager.view_budget()

        # Export CSV
        elif choice == "11":

            export_csv(manager.expenses)

        # Backup
        elif choice == "12":

            backup_data()

        # Restore
        elif choice == "13":

            restore_backup()

        # Exit
        elif choice == "0":

            print("\nThank You for using Personal Finance Tracker.")

            break

        else:

            print("Invalid Choice!")


# Run Program
def main():

    menu()


if __name__ == "__main__":

    main()