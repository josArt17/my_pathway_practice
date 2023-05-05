# Ask for user input
loan_size = int(input("Enter the loan size (1-10): "))
credit_history = int(input("Enter your credit history rating (1-10): "))
income = int(input("Enter your income rating (1-10): "))
down_payment = int(input("Enter your down payment rating (1-10): "))

# Initialize the loan decision variable
should_loan_money = False

# Check the loan size
if loan_size >= 5:
    # Check credit history and income
    if credit_history >= 7 and income >= 7:
        should_loan_money = True
    # Check credit history or income, and down payment
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan_money = True
    # If neither credit history nor income is at least 7, don't loan
    else:
        should_loan_money = False
else:
    # Check credit, income, and down payment ratings
    if credit_history < 4:
        should_loan_money = False
    elif income >= 7 or down_payment >= 7:
        should_loan_money = True
    elif income >= 4 and down_payment >= 4:
        should_loan_money = True
    else:
        should_loan_money = False

# Display the loan decision
if should_loan_money:
    print("Yes, loan the money.")
else:
    print("No, do not loan the money.")
