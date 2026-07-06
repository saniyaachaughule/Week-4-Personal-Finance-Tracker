# Name: Saniya Choughule
# Week 4 Project
# File Handling Module

import json
import csv
import shutil
import os


# Save Expenses to JSON File
def save_expenses(expenses):

    try:

        data = []

        # Convert Expense objects to dictionary
        for expense in expenses:

            data.append(expense.to_dictionary())

        # Save data into JSON file
        with open("data/expenses.json", "w") as file:

            json.dump(data, file, indent=4)

        print("Expenses Saved Successfully!")

    except Exception as e:

        print("Error Saving File:", e)


# Load Expenses from JSON File
def load_expenses():

    try:

        # If file doesn't exist, return empty list
        if not os.path.exists("data/expenses.json"):

            return []

        with open("data/expenses.json", "r") as file:

            data = json.load(file)

        return data

    except Exception as e:

        print("Error Loading File:", e)

        return []


# Export Expenses to CSV
def export_csv(expenses):

    try:

        with open("data/exports/expenses.csv", "w", newline="") as file:

            writer = csv.writer(file)

            # Heading
            writer.writerow([
                "Date",
                "Amount",
                "Category",
                "Description"
            ])

            # Expense Data
            for expense in expenses:

                writer.writerow([
                    expense.date,
                    expense.amount,
                    expense.category,
                    expense.description
                ])

        print("CSV Exported Successfully!")

    except Exception as e:

        print("CSV Export Error:", e)


# Create Backup
def backup_data():

    try:

        shutil.copy(
            "data/expenses.json",
            "data/backup/expenses_backup.json"
        )

        print("Backup Created Successfully!")

    except Exception as e:

        print("Backup Error:", e)


# Restore Backup
def restore_backup():

    try:

        shutil.copy(
            "data/backup/expenses_backup.json",
            "data/expenses.json"
        )

        print("Backup Restored Successfully!")

    except Exception as e:

        print("Restore Error:", e)