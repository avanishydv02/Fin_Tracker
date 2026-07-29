import json
import os
from datetime import datetime

# File name for data storage
DATA_FILE = "data.json"


def load_data():
    """
    Loads transaction data from DATA_FILE.

    If the file does not exist, is empty, or has invalid JSON,
    it should return an empty list.

    Returns:
        list: A list of transaction dictionaries.
    """

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(transactions):
    """
    Saves the list of transactions to DATA_FILE in JSON format.

    Args:
        transactions (list): The list of transaction dictionaries.
    """

    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


def clear_data():
    """
    Clears all saved transaction data.
    """
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
        print("Transactions history cleared.")
    else:
        print("No saved data found.")


def add_transaction(transactions, transaction_type):
    """
    Prompts the user for details and adds a transaction to the list.

    Args:
        transactions (list): The list of transaction dictionaries.
        transaction_type (str): Either "income" or "expense".
    """
    print(f"\n--- Add {transaction_type.capitalize()} ---")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. Please try again.")
        except ValueError:
            print("Error. Please enter a valid number.")

    category = input(
        "Enter the category of transaction: ").strip() or "Uncategorized"

    while True:
        date_input = input(
            "Please enter the date of transaction (YYYY-MM-DD) [Leave blank for today]: ").strip()
        if not date_input:
            date = datetime.today().strftime('%Y-%m-%d')
            break
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    transaction = {"Type": transaction_type, "Amount": amount,
                   "Category": category, "Date": date}

    transactions.append(transaction)
    print(f"Successfully added {transaction_type}!")
    save_data(transactions)


def view_summary(transactions):
    """
    Calculates and displays a summary of the personal finances,
    including total income, total expenses, net balance, and transaction history.

    Args:
        transactions (list): The list of transaction dictionaries.
    """
    print("\n=== Financial Summary ===")

    total_income = 0.0
    total_expense = 0.0
    for transaction in transactions:
        if transaction["Type"] == "income":
            total_income += transaction["Amount"]
        elif transaction["Type"] == "expense":
            total_expense += transaction["Amount"]

    net_balance = total_income - total_expense

    # Display calculations
    print(f"Total Income:   ₹{total_income:.2f}")
    print(f"Total Expenses: ₹{total_expense:.2f}")
    print(f"Net Balance:    ₹{net_balance:.2f}")

    print("\n--- Transaction History ---")
    # TODO: Print each transaction in a clean, readable format.
    # If the transactions list is empty, print "No transactions recorded yet."
    # Hint: Loop through the `transactions` list and print the details of each dictionary.
    if transactions == []:
        print("No transactions recorded yet.")
    else:
        for transaction in transactions:
            print(f"Type: {transaction['Type']}")
            print(f"Amount: ₹{transaction['Amount']:.2f}")
            print(f"Category: {transaction['Category']}")
            print(f"Date: {transaction['Date']}")
            print("-" * 15)


def main():
    """
    Main loop for the Personal Finance Tracker application.
    """
    # Load existing transactions at startup
    transactions = load_data()

    while True:
        # CLI Menu Interface
        print("\n==============================")
        print("   PERSONAL FINANCE TRACKER   ")
        print("==============================")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Clear Saved Data")
        print("5. Save & Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_transaction(transactions, "income")
        elif choice == '2':
            add_transaction(transactions, "expense")
        elif choice == '3':
            view_summary(transactions)
        elif choice == '4':
            confirm = input(
                "Are you sure you want to clear all your transactions history (yes/no): ").lower()
            if confirm == "yes":
                transactions.clear()
                clear_data()
            else:
                print("Transaction history not cleared.")
        elif choice == '5':
            print("Saving data.....")
            save_data(transactions)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
