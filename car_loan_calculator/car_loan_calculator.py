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
import json

# Load the messages from the JSON file
with open('messages.json', encoding="utf-8") as file:
    MESSAGES = json.load(file)

### DECLARING FUNCTIONS

def prompt(message):
    print(f"==> {message}")

def get_float_number(number):
    try:
        float(number)
    except ValueError:
        return True
    return False

def get_duration():
    while True:
        prompt(MESSAGES["loan_duration"])
        years = input().strip()
        if years in [str(i) for i in range(1, 9)]:
            return float(years) * 12
        print("Invalid choice. Please enter a number between 1 and 8.")

def validate(number):
    while get_float_number(number):
        prompt('invalid number')
        number = input()

def calc_interest_apr(loan_interest):
    output = float(loan_interest) / 100 / 12
    return output
    
### USER INPUT AND CALCULATION

prompt(MESSAGES['Welcome'])


prompt(MESSAGES['loan_amount'])
amount = input().strip()
validate(amount)
amount_result = float(amount)

duration_result = float(get_duration())

prompt(MESSAGES['loan_interest'])
interest = input().strip()
validate(interest)
interest_result = calc_interest_apr(interest)

monthly_payment = amount_result * (interest_result / (1 - (1 + interest_result) ** -duration_result))

# Show results
print("\n== Loan Summary ==")
print(f"Loan Amount: ${amount_result:,.2f}")
print(f"Annual Interest Rate (APR): {interest}%")
print(f"Loan Duration: {int(duration_result)} months")
print(f"Monthly Payment: ${monthly_payment:,.2f}")
