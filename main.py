import json
import os

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


def add_transaction(transactions, transaction_type):
    """
    Prompts the user for details and adds a transaction to the list.

    Args:
        transactions (list): The list of transaction dictionaries.
        transaction_type (str): Either "income" or "expense".
    """
    print(f"\n--- Add {transaction_type.capitalize()} ---")

    # 1. Get amount with validation
    # TODO: Write a loop to repeatedly prompt the user for the amount until they enter a valid positive number.
    # Hint: Use a try-except block to handle ValueError when converting the input to float.
    # Ensure the amount is greater than 0 before proceeding.
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount > 0:
                break
            else:
                print("Amount less than 0. Please try again.")
        except ValueError:
            print("Error. Please enter a valid number.")

    # 2. Get category
    # TODO: Prompt the user to enter a category (string).
    category = input("Enter the category of transaction: ")

    # 3. Get date
    # TODO: Prompt the user to enter a date (string, e.g., "YYYY-MM-DD").
    date = input("Please enter the date of transaction (YYYY-MM-DD): ")

    # 4. Create the transaction dictionary
    # TODO: Construct a dictionary with keys: "type", "amount", "category", and "date".
    transaction = {"Type": transaction_type, "Amount": amount,
                   "Category": category, "Date": date}

    # 5. Append to the transactions list
    # TODO: Append the transaction dictionary to the `transactions` list.
    transactions.append(transaction)
    print(f"Successfully added {transaction_type}!")


def view_summary(transactions):
    """
    Calculates and displays a summary of the personal finances,
    including total income, total expenses, net balance, and transaction history.

    Args:
        transactions (list): The list of transaction dictionaries.
    """
    print("\n=== Financial Summary ===")

    # TODO: Calculate total income (sum of amounts where type is "income")
    total_income = 0.0

    # TODO: Calculate total expenses (sum of amounts where type is "expense")
    total_expenses = 0.0

    # TODO: Calculate net balance (income - expenses)
    net_balance = 0.0

    # Display calculations
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance:    ${net_balance:.2f}")

    print("\n--- Transaction History ---")
    # TODO: Print each transaction in a clean, readable format.
    # If the transactions list is empty, print "No transactions recorded yet."
    # Hint: Loop through the `transactions` list and print the details of each dictionary.
    pass


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
        print("4. Save and Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_transaction(transactions, "income")
        elif choice == '2':
            add_transaction(transactions, "expense")
        elif choice == '3':
            view_summary(transactions)
        elif choice == '4':
            # Save records back to data.json upon exit
            print("Saving data...")
            save_data(transactions)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
