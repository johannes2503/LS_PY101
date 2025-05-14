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

def prompt(message):
    print(f"==> {message}")

def invalid_number(number):
    try:
        float(number)
    except ValueError:
        return True
    return False

def invalid_duration(loan_duration):
    while loan_duration not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        prompt('invalid_operation')
        loan_duration = input()
    match (loan_duration):
        case "1":
            output = int(loan_duration) * int(12)
        case "2":
            output = int(loan_duration) * int(12)
        case "3":
            output = int(loan_duration) * int(12)
        case "4":
            output = int(loan_duration) * int(12)
        case "5":
            output = int(loan_duration) * int(12)
        case "6":
            output = int(loan_duration) * int(12)
        case "7":
            output = int(loan_duration) * int(12)
        case "8":
            output = int(loan_duration) * int(12)
    return output

def validate(number):
    while invalid_number(number):
        prompt('invalid number')
        number = input()

def calc_apr(loan_interest):
    output = float(loan_interest)/ float(12)
    return round(output, 2)
    



prompt(MESSAGES['Welcome'])


prompt(MESSAGES['loan_amount'])
amount = input()
validate(amount)

prompt(MESSAGES['loan_duration'])
duration = input()
duration_result = invalid_duration(duration)


prompt(MESSAGES['loan_interest'])
interest = input()
validate(interest)
interest_result = calc_apr(interest)




