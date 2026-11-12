# Personal Expense Tracker
# Created by Sudarshan Kushwaha

expenses = []

print("=" * 40)
print("       PERSONAL EXPENSE TRACKER")
print("=" * 40)

while True:

    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        category = input("Enter Expense Category: ")
        amount = float(input("Enter Amount (Rs.): "))

        if amount <= 0:
            print("Please enter a valid amount.")
            continue

        expenses.append({
            "category": category,
            "amount": amount
        })

        print("Expense Added Successfully!")

    elif choice == "2":

        print("\n----- EXPENSE HISTORY -----")

        if not expenses:
            print("No expenses recorded.")

        for expense in expenses:
            print(expense["category"], "- Rs.", expense["amount"])

    elif choice == "3":

        total = sum(item["amount"] for item in expenses)

        print("\nTotal Expenses: Rs.", total)

    elif choice == "4":

        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Try Again.")

print("\nDeveloped by Sudarshan Kushwaha")