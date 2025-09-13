# Student Budget Planner

A simple, command-line based budget planning tool designed to help students track their income and expenses, set budgets, and visualize their spending habits.

## Problem Statement
Students often overspend or mismanage their monthly allowance due to a lack of financial planning tools tailored for them. This project aims to provide a simple system to help students plan and track their monthly expenses effectively.

## Features
- **Track Transactions**: Add income and expense entries with categories and amounts.
- **Persistent Storage**: All data is saved locally in a `budget_data.json` file, so your information is never lost.
- **Real-time Balance**: Automatically calculates and displays the current balance.
- **Budgeting**: Set a monthly spending limit and receive warnings if you exceed it.
- **Category Analysis**: View a breakdown of expenses by category.
- **Visual Reports**: Generate and display:
    - A **pie chart** showing the distribution of expenses across different categories.
    - A **bar chart** comparing total income versus total expenses.

## Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation
1.  **Clone the repository:**
    ```sh
    git clone https://github.com/YOUR_USERNAME/student-budget-planner.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd student-budget-planner
    ```
3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## How to Run the Project
To start the application, run the following command in your terminal from the project directory:
```sh
python budget_planner.py
```
You will be greeted with a menu to start managing your budget.

## Output and screenshots
```sh
===== Student Budget Planner =====
1. Add a transaction (Income/Expense)
2. Set monthly budget
3. View financial summary
4. Generate visual report (Charts)
5. Exit
Enter your choice (1-5): 1
Enter transaction type (income/expense): income
Enter amount: 8000
Enter income category (e.g., Food, Salary, Books): Part-time job

Successfully added income of ₹8000.00 in 'Part-time job'.

===== Student Budget Planner =====
1. Add a transaction (Income/Expense)
2. Set monthly budget
3. View financial summary
4. Generate visual report (Charts)
5. Exit
Enter your choice (1-5): 1
Enter transaction type (income/expense): expense
Enter amount: 2000
Enter expense category (e.g., Food, Salary, Books): Food

Successfully added expense of ₹2000.00 in 'Food'.

===== Student Budget Planner =====
1. Add a transaction (Income/Expense)
2. Set monthly budget
3. View financial summary
4. Generate visual report (Charts)
5. Exit
Enter your choice (1-5): 1
Enter transaction type (income/expense): expense
Enter amount: 1000
Enter expense category (e.g., Food, Salary, Books): Books

Successfully added expense of ₹1000.00 in 'Books'.

===== Student Budget Planner =====
1. Add a transaction (Income/Expense)
2. Set monthly budget
3. View financial summary
4. Generate visual report (Charts)
5. Exit

--- Financial Summary ---
Total Income:    ₹8000.00
Total Expenses:  ₹3000.00
Current Balance: ₹5000.00  <-- This is your savings

--- Expense Breakdown by Category ---
- Food: ₹2000.00
- Books: ₹1000.00
------------------------

===== Student Budget Planner =====
1. Add a transaction (Income/Expense)
2. Set monthly budget
3. View financial summary
4. Generate visual report (Charts)
5. Exit
Enter your choice (1-5): 4

Saved expense pie chart as 'expense_pie_chart.png'
Saved income, expense, and savings bar chart as 'income_expense_savings_bar_chart.png'

===== Student Budget Planner =====
1. Add a transaction (Income/Expense)
2. Set monthly budget
3. View financial summary
4. Generate visual report (Charts)
5. Exit
Enter your choice (1-5): 5
Exiting budget planner. Goodbye!
```

## Generated Pie Chart (Expense Distribution)
<img width="640" height="480" alt="expense_pie_chart" src="https://github.com/user-attachments/assets/574c61ca-3a9b-47a7-8e94-80868124de2b" />


## Generated Bar Chart (Income vs. Expenses)
<img width="640" height="480" alt="income_expense_savings_bar_chart" src="https://github.com/user-attachments/assets/5025f1bf-c8b6-45e6-922e-20efa7ab8a4d" />

