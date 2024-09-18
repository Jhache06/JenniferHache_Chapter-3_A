# This program will calculate the monthly budget by specifying the type and amount for each expense.
# Use the reduce method to calculate and display the total expenses.
# Program should display highest and lowest expense.
from functools import reduce

# Create function to calculate the monthly budget
# Ask user to enter their monthly budget when prompted
def calculate_budget():
    budget = float(input("Enter your monthly budget here: "))
    expense = []

    while True:
        # Ask user to enter their expenses. If user enteres done, program will calculate results
        expense_type = input("Please enter your type of expense here: ")

        if expense_type.lower() == "done":
            break
        try:
            # Ask user to enter the amount for their expense
            expense_amount = float(input(f"Please enter the amount for {expense_type} here: "))
            expense.append((expense_type, expense_amount))

            # Ask if the user is done entering types of expenses
            done = input("Are you done entering types of expenses (yes/no)? ").strip().lower()
            if done == 'yes':
                # Exit loop if user enters yes
                break
            elif done != 'no':
                # loop continues unless user enters anything other than yes or no
                print("Please enter yes or no.")

        except ValueError:
            # Error message will appear if user did not enter valid numeric value
            print("Please enter a valid number.")

    if expense:
        # Calculate total expenses using reduce method
        total = reduce(lambda x, y: x + y[1], expense, 0)

         # Find the highest and lowest expenses
        highest_expense = reduce(lambda x, y: x if x[1] > y[1] else y, expense)
        lowest_expense = reduce(lambda x, y: x if x[1] < y[1] else y, expense)

        # Display results
        print(f"\nBudget: ${budget:.2f}")
        print(f"Total Expenses: ${total:.2f}")
        print(f"Remaining: ${budget - total:.2f}")
        print(f"Highest Expense: {highest_expense[0]} : ${highest_expense[1]:.2f}")
        print(f"Lowest Expense: {lowest_expense[0]} : ${lowest_expense[1]:.2f}")
    else:
        # error message : User will be notified if expenses were not entered
        print("You did not enter any expenses.")

# Call function
if __name__ == "__main__":
    calculate_budget()
