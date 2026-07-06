# Name: Saniya Choughule
# Week 4 Project
# Expense Class

class Expense:

    def __init__(self, date, amount, category, description):

        self.date = date
        self.amount = amount
        self.category = category
        self.description = description


    def to_dictionary(self):

        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }