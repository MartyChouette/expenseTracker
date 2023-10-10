import datetime
import matplotlib.pyplot as plt

class Expense:
    def __init__(self, category, amount, date, description):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date} - {self.category} - {self.description} - ${self.amount:.2f}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, date, description):
        expense = Expense(category, amount, date, description)
        self.expenses.append(expense)

    def search_expenses(self, start_date=None, end_date=None):
        results = []
        for expense in self.expenses:
            if (not start_date or expense.date >= start_date) and (not end_date or expense.date <= end_date):
                results.append(expense)
        return results

    def plot_expenses(self):
        categories = {}
        for expense in self.expenses:
            if expense.category not in categories:
                categories[expense.category] = 0
            categories[expense.category] += expense.amount

        fig, ax = plt.subplots()
        ax.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title("Expense Distribution by Category")
        plt.show()

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Search Expenses by Date")
        print("4. View Expense Distribution by Category")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date_str = input("Enter date (YYYY-MM-DD): ")
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            description = input("Enter description: ")
            tracker.add_expense(category, amount, date_obj, description)
            
        elif choice == "2":
            for expense in tracker.expenses:
                print(expense)
                
        elif choice == "3":
            start_date_str = input("Enter start date (YYYY-MM-DD or leave blank): ")
            end_date_str = input("Enter end date (YYYY-MM-DD or leave blank): ")
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None
            for expense in tracker.search_expenses(start_date, end_date):
                print(expense)
                
        elif choice == "4":
            tracker.plot_expenses()
            
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
