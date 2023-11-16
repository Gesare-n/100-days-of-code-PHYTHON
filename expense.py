# expense.py
class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date
# expense_tracker.py
from expense import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, date):
        expense = Expense(category, amount, date)
        self.expenses.append(expense)

    def view_summary(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expense Summary:")
            for expense in self.expenses:
                print(f"{expense.date} - {expense.category}: ${expense.amount}")

    def set_budget(self, category, budget):
        # Placeholder for future implementation
        pass
# main.py
from expense_tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    # Example usage
    tracker.add_expense("Groceries", 50.0, "2023-01-15")
    tracker.add_expense("Utilities", 30.0, "2023-01-15")
    tracker.add_expense("Dining", 20.0, "2023-01-16")

    tracker.view_summary()

if __name__ == "__main__":
    main()

#update
# expense_tracker.py
from expense import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budgets = {}  # Dictionary to store budgets for each category

    def add_expense(self, category, amount, date):
        expense = Expense(category, amount, date)
        self.expenses.append(expense)

    def view_summary(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expense Summary:")
            for expense in self.expenses:
                print(f"{expense.date} - {expense.category}: ${expense.amount}")

    def set_budget(self, category, budget):
        self.budgets[category] = budget
        print(f"Budget set for {category}: ${budget}")

    def view_budgets(self):
        if not self.budgets:
            print("No budgets set.")
        else:
            print("Budgets:")
            for category, budget in self.budgets.items():
                print(f"{category}: ${budget}")

    def check_budget(self, category):
        if category in self.budgets:
            total_expenses = sum(expense.amount for expense in self.expenses if expense.category == category)
            remaining_budget = self.budgets[category] - total_expenses
            print(f"Remaining budget for {category}: ${remaining_budget}")
        else:
            print(f"No budget set for {category}.")
# main.py
from expense_tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Set Budget")
        print("4. View Budgets")
        print("5. Check Remaining Budget")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            date = input("Enter expense date (YYYY-MM-DD): ")
            tracker.add_expense(category, amount, date)
        elif choice == "2":
            tracker.view_summary()
        elif choice == "3":
            category = input("Enter category to set budget for: ")
            budget = float(input("Enter budget amount: "))
            tracker.set_budget(category, budget)
        elif choice == "4":
            tracker.view_budgets()
        elif choice == "5":
            category = input("Enter category to check remaining budget: ")
            tracker.check_budget(category)
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
