"""
Car Loan Calculator

This script calculates the monthly payment for a car loan
based on the loan amount, annual interest rate (APR), and loan duration in years.

Formula:
    m = p * (j / (1 - (1 + j) ** -n))

Where:
    m = monthly payment
    p = loan amount
    j = monthly interest rate (APR / 12)
    n = loan duration in months
"""

def prompt(message):
    print(f"==> {message}")

def get_float_input(prompt_message):
    while True:
        prompt(prompt_message)
        value = input().strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

def get_loan_duration():
    while True:
        prompt("Enter loan duration in years (1–8):")
        years = input().strip()
        if years in [str(i) for i in range(1, 9)]:
            return float(years) * 12
        print("Invalid choice. Please enter a number between 1 and 8.")

# ---- MAIN PROGRAM ----

prompt("Welcome to the Car Loan Calculator!")

loan_amount = get_float_input("Enter the loan amount:")
annual_interest_rate = get_float_input("Enter the APR (e.g., 5 for 5%):")
monthly_interest_rate = (annual_interest_rate / 100) / 12

loan_duration_months = get_loan_duration()

# Calculate monthly payment
if monthly_interest_rate == 0:
    monthly_payment = loan_amount / loan_duration_months
else:
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_duration_months))

# Show results
print("\n== Loan Summary ==")
print(f"Loan Amount: ${loan_amount:,.2f}")
print(f"Annual Interest Rate (APR): {annual_interest_rate:.2f}%")
print(f"Loan Duration: {int(loan_duration_months)} months")
print(f"Monthly Payment: ${monthly_payment:,.2f}")
