# Name: Saniya Choughule
# Week 4 Project
# Reports Module


# Monthly Expense Report
def monthly_report(expenses):

    if len(expenses) == 0:

        print("\nNo Expenses Available.")
        return

    total = 0

    print("\n" + "=" * 60)
    print("MONTHLY EXPENSE REPORT")
    print("=" * 60)

    for expense in expenses:

        print(
            f"{expense.date} | "
            f"{expense.category} | "
            f"₹{expense.amount} | "
            f"{expense.description}"
        )

        total += float(expense.amount)

    print("-" * 60)
    print(f"Total Monthly Expense : ₹{total:.2f}")


# Category-wise Report
def category_report(expenses):

    if len(expenses) == 0:

        print("\nNo Expenses Available.")
        return

    categories = {}

    for expense in expenses:

        if expense.category in categories:
            
            categories[expense.category] += float(expense.amount)

        else:

            categories[expense.category] = float(expense.amount)

    print("\n" + "=" * 60)
    print("CATEGORY REPORT")
    print("=" * 60)

    for category, amount in categories.items():

        print(f"{category:<20} ₹{amount:.2f}")


# Statistics
def statistics(expenses):

    if len(expenses) == 0:

        print("\nNo Expenses Available.")
        return

    amounts = []

    for expense in expenses:

        amounts.append(float(expense.amount))

    total = sum(amounts)
    highest = max(amounts)
    lowest = min(amounts)
    average = total / len(amounts)

    print("\n" + "=" * 60)
    print("EXPENSE STATISTICS")
    print("=" * 60)

    print(f"Total Expenses   : {len(expenses)}")
    print(f"Total Amount     : ₹{total:.2f}")
    print(f"Average Expense  : ₹{average:.2f}")
    print(f"Highest Expense  : ₹{highest:.2f}")
    print(f"Lowest Expense   : ₹{lowest:.2f}")


# Text-Based Visualization
def expense_chart(expenses):

    if len(expenses) == 0:
        print("\nNo Expenses Available.")
        return

    categories = {}

    # Calculate total amount for each category
    for expense in expenses:

        if expense.category in categories:
            categories[expense.category] += float(expense.amount)
        else:
            categories[expense.category] = float(expense.amount)

    print("\n" + "=" * 60)
    print("CATEGORY EXPENSE CHART")
    print("=" * 60)

    # Find highest category amount
    highest = max(categories.values())

    # Maximum width of chart
    max_width = 30

    # Display chart
    for category, amount in categories.items():

        stars = "*" * int((amount / highest) * max_width)

        print(f"{category:<15} {stars:<30} ₹{amount:.2f}")