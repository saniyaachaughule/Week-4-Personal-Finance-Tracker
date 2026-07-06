# Utility Functions

from datetime import datetime


# Validate Amount
def validate_amount(amount):

    try:

        amount = float(amount)

        if amount > 0:
            return True

    except ValueError:
        pass

    return False


# Validate Date
def validate_date(date):

    try:

        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:

        return False


# Expense Categories
def categories():

    return [

        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Education",
        "Entertainment",
        "Healthcare",
        "Other"

    ]