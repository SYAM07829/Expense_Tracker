from database import (
    create_table, add_expense, view_expenses,
    update_expense, delete_expense,
    total_spend, spend_by_category, monthly_summary
)

def print_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Total Spend")
    print("6. Spend by Category")
    print("7. Monthly Summary")
    print("8. Exit")

def main():
    create_table()

    while True:
        print_menu()
        choice = input("Choose an option (1-8): ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            note = input("Note (optional): ")
            add_expense(amount, category, date, note)

        elif choice == "2":
            print("\n--- All Expenses ---")
            print("ID | Amount | Category | Date | Note")
            for row in view_expenses():
                print(row)

        elif choice == "3":
            expense_id = int(input("Enter ID to update: "))
            amount = float(input("New Amount: "))
            category = input("New Category: ")
            date = input("New Date (YYYY-MM-DD): ")
            note = input("New Note (optional): ")
            update_expense(expense_id, amount, category, date, note)

        elif choice == "4":
            expense_id = int(input("Enter ID to delete: "))
            delete_expense(expense_id)

        elif choice == "5":
            print("Total Spend:", total_spend())

        elif choice == "6":
            print("\n--- Spend by Category ---")
            for row in spend_by_category():
                print(row)

        elif choice == "7":
            print("\n--- Monthly Summary ---")
            for row in monthly_summary():
                print(row)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()