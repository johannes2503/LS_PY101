"""
Car Loan Calculator
This script calculates the monthly payment for a car \n
loan based on the loan amount, interest rate, and loan duration.

You'll need three pieces of information:

    the loan amount
    the Annual Percentage Rate (APR)
    the loan duration

From the above, you'll need to calculate the following two things:

    monthly interest rate (APR / 12)
    loan duration in months

    m = p * (j / (1 - (1 + j) ** (-n)))

    m = monthly payment
    p = loan amount
    j = monthly interest rate
    n = loan duration in months


"""

print("----------------------------------")
print('Welcome to JD Car Loan Calculator!')
print("----------------------------------")
print("Please enter the loan amount you need in $:")
loan_amount = input()
print("Please enter loan duration in years:(The max is 8 years)")
loan_duration = input()
print("Please enter interest rate:")
loan_interest = input()
