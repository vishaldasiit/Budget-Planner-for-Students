import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Define the name of the data file
DATA_FILE = "budget_data.json"

def load_data():
    """Loads transactions from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {"transactions": [], "budget_limit": 0}
    return {"transactions": [], "budget_limit": 0}

def save_data(data):
    """Saves transactions to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_transaction(data):
    """Adds a new income or expense transaction."""
    trans_type = input("Enter transaction type (income/expense): ").lower()
    if trans_type not in ["income", "expense"]:
        print("Invalid type. Please choose 'income' or 'expense'.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input(f"Enter {trans_type} category (e.g., Food, Salary, Books): ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transaction = {
        "type": trans_type,
        "amount": amount,
        "category": category,
        "timestamp": timestamp
    }
    
    data["transactions"].append(transaction)
    save_data(data)
    print(f"\nSuccessfully added {trans_type} of ₹{amount:.2f} in '{category}'.")
    
    # Check if over budget
    if trans_type == "expense" and data["budget_limit"] > 0:
        _, total_expenses, _, _ = calculate_summary(data["transactions"])
        if total_expenses > data["budget_limit"]:
            print(f"⚠️ WARNING: You have exceeded your monthly budget of ₹{data['budget_limit']:.2f}!")

def set_budget(data):
    """Sets a monthly budget limit."""
    try:
        limit = float(input("Enter your monthly budget limit: "))
        if limit < 0:
            print("Budget limit cannot be negative.")
            return
        data["budget_limit"] = limit
        save_data(data)
        print(f"\nMonthly budget has been set to ₹{limit:.2f}.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def calculate_summary(transactions):
    """Calculates total income, expenses, and balance."""
    total_income = 0
    total_expenses = 0
    expenses_by_category = {}

    for t in transactions:
        if t['type'] == 'income':
            total_income += t['amount']
        else:
            total_expenses += t['amount']
            cat = t['category']
            expenses_by_category[cat] = expenses_by_category.get(cat, 0) + t['amount']
            
    balance = total_income - total_expenses
    return total_income, total_expenses, balance, expenses_by_category

def display_summary(data):
    """Displays the financial summary."""
    transactions = data["transactions"]
    if not transactions:
        print("\nNo transactions yet. Add one to see a summary.")
        return

    total_income, total_expenses, balance, expenses_by_category = calculate_summary(transactions)

    print("\n--- Financial Summary ---")
    print(f"Total Income:    ₹{total_income:.2f}")
    print(f"Total Expenses:  ₹{total_expenses:.2f}")
    print(f"Current Balance: ₹{balance:.2f}  <-- This is your savings")
    if data["budget_limit"] > 0:
        print(f"Monthly Budget:  ₹{data['budget_limit']:.2f}")
        remaining = data['budget_limit'] - total_expenses
        print(f"Budget Remaining: ₹{remaining:.2f}")
    print("\n--- Expense Breakdown by Category ---")
    if not expenses_by_category:
        print("No expenses recorded yet.")
    else:
        for category, amount in expenses_by_category.items():
            print(f"- {category}: ₹{amount:.2f}")
    print("------------------------")

def generate_report(data):
    """Generates and saves a pie chart and bar chart of expenses."""
    transactions = data["transactions"]
    if not transactions:
        print("\nNo transactions to generate a report.")
        return

    _, _, _, expenses_by_category = calculate_summary(transactions)
    
    # --- Generate Pie Chart for Expense Categories (No changes here) ---
    if expenses_by_category:
        labels = expenses_by_category.keys()
        sizes = expenses_by_category.values()
        
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax1.axis('equal')
        plt.title("Expense Distribution by Category")
        
        pie_filename = "expense_pie_chart.png"
        plt.savefig(pie_filename)
        print(f"\nSaved expense pie chart as '{pie_filename}'")
        plt.show()
    else:
        print("No expenses to create a pie chart.")

    # --- Generate Bar Chart for Income, Expenses, and Savings ---
    # --- THIS SECTION IS UPDATED ---
    total_income, total_expenses, balance, _ = calculate_summary(transactions)
    
    if total_income > 0 or total_expenses > 0:
        # Define the base categories and values
        categories = ['Income', 'Expenses']
        values = [total_income, total_expenses]
        colors = ['green', 'red']
        
        # NEW: Conditionally add Savings to the chart if it's positive
        if balance > 0:
            categories.append('Savings')
            values.append(balance)
            colors.append('blue') # Add a color for the savings bar

        fig2, ax2 = plt.subplots()
        ax2.bar(categories, values, color=colors)
        plt.title('Income vs. Expenses vs. Savings') # Updated title
        plt.ylabel('Amount (₹)')
        
        bar_filename = "income_expense_savings_bar_chart.png" # Updated filename
        plt.savefig(bar_filename)
        print(f"Saved income, expense, and savings bar chart as '{bar_filename}'")
        plt.show()
    else:
        print("Not enough data for income vs. expense chart.")

def main_menu():
    """Displays the main menu and handles user input."""
    data = load_data()
    
    while True:
        print("\n===== Student Budget Planner =====")
        print("1. Add a transaction (Income/Expense)")
        print("2. Set monthly budget")
        print("3. View financial summary")
        print("4. Generate visual report (Charts)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_transaction(data)
        elif choice == '2':
            set_budget(data)
        elif choice == '3':
            display_summary(data)
        elif choice == '4':
            generate_report(data)
        elif choice == '5':
            print("Exiting budget planner. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
