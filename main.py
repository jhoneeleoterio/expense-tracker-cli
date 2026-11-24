import datetime
import os
import subprocess
from decimal import Decimal
from typing import Dict, List

def clear_screen():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)


def show_menu() -> None:
    clear_screen()
    print("========================")
    print("    EXPENSE TRACKER    ")
    print("========================\n")
    print("1. Add Expense")
    print("2. List Expenses")
    print("0. Exit\n")


def add_expense(list_of_expenses: List, description: str, amount: Decimal, category: str) -> None:
    if amount <= 0:
        print("Amount must be greater than zero.")
        input("\nPress Enter to return to the menu...")
        return

    expense = dict(id=len(list_of_expenses) + 1, description=description, amount=amount, category=category, date=datetime.datetime.now())
    list_of_expenses.append(expense)
    
    print(f"\nExpense added successfully! ID: {expense['id']}")
    input("\nPress Enter to return to the menu...")


def list_expenses(expenses: List) -> None:
    if not expenses:
        print("No expenses recorded.")
        input("\nPress Enter to return to the menu...")
        return
    
    print("Listing expenses..\n")
    
    for expense in expenses:
        print(f"ID: {expense['id']}, Description: {expense['description']}, Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date'].strftime('%d/%m/%Y %H:%M:%S')}")

    print(f"\nTotal Expenses: R${sum(expense['amount'] for expense in expenses):.2f}")
    print(f"Transactions: {len(expenses)}")
    print("----------------------------")
    input("\nPress Enter to return to the menu...")


def main():
    # Your main code logic here
    list_of_expenses: List = []

    while True:
        show_menu()

        choice = input("Select an option: ").strip()

        match choice:
            case "1":
                description = input("Enter expense description: ").strip()
                if not description:
                    print("Description cannot be empty.")
                    input("\nPress Enter to return to the menu...")
                    continue

                amount = input("Enter expense amount: ").strip()
                try:
                    amount = Decimal(amount)
                except Exception:
                    print("Invalid amount! Please enter a valid number.")
                    input("\nPress Enter to return to the menu...")
                    continue
           
                category = input("Enter expense category: ").strip()
                if not category:
                    print("Category cannot be empty.")
                    input("\nPress Enter to return to the menu...")
                    continue        
                
                add_expense(list_of_expenses, description, amount, category)
            case "2":
                list_expenses(list_of_expenses)
            case "0":
                print("Exiting...")
                break
            case _:
                print("\nInvalid option! Please try again.")
                input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")