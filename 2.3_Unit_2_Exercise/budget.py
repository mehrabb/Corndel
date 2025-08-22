# Budget Tracking App

# Store all transactions here
transactions = []

def show_balance():
    """Calculate and return current balance."""
    balance = sum(t["amount"] for t in transactions)
    return balance

def add_transaction():
    """Add a new income or expense transaction."""
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount (use negative for expenses): "))
    except ValueError:
        print("Invalid amount. Please try again.")
        return

    transactions.append({"description": description, "amount": amount})
    print("Transaction added!\n")

def view_transactions():
    """Display all transactions."""
    if not transactions:
        print("No transactions yet.\n")
        return

    print("\nYour Transactions:")
    print("-" * 30)
    for idx, t in enumerate(transactions, start=1):
        print(f"{idx}. {t['description']} : {t['amount']:.2f}")
    print("-" * 30)
    print(f"Current Balance: {show_balance():.2f}\n")

def main():
    """Main menu loop."""
    while True:
        balance = show_balance()
        print("\n==== Budget Tracking App ====")
        print(f" Current Balance: {balance:.2f}")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
