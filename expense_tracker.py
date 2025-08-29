import csv
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense(category, amount, description=""):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print(f"✅ Added expense: {category} - {amount} ({description})")

def view_expenses():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def total_expenses():
    total = 0
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    print(f"💰 Total Expenses: {total}")

def category_report(category):
    total = 0
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Category"].lower() == category.lower():
                total += float(row["Amount"])
    print(f"📊 Total spent on {category}: {total}")

def menu():
    while True:
        print("\n📌 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Report")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            cat = input("Enter category: ")
            amt = float(input("Enter amount: "))
            desc = input("Enter description: ")
            add_expense(cat, amt, desc)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            cat = input("Enter category to report: ")
            category_report(cat)
        elif choice == "5":
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    init_file()
    menu()
