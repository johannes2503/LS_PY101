"""

Car Loan Calculator
This script calculates the monthly payment for a car
loan based on the loan amount, interest rate, and loan duration.

"""

import json
import os

# Load the messages from the JSON file
with open('messages.json', encoding="utf-8") as file:
    MESSAGES = json.load(file)

### DECLARING FUNCTIONS

def clear_console():
    """
    This function clears the console between prompts
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt(message):
    """
    This function is for promting a messages to the user
    """
    print(f"==> {message}")

def invalid_number(num_str):
    """
    This function checks if the input from the user is valid
    """
    try:
        number = float(num_str)
        if number <= 0:
            raise ValueError()
    except ValueError:
        return True
    return False

def get_duration():
    """
    This function calculates the duration af the loan
    """
    while True:
        try:
            prompt(MESSAGES["loan_duration"])
            years = float(input())
            if 0.1 <= years <= 8:
                return years * 12
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")


def calc_interest_apr(loan_interest):
    """
    This function calculates the monthly interest rate from the annual APR.
    """
    monthly_rate = float(loan_interest) / 100 / 12
    return monthly_rate

### USER INPUT


prompt(MESSAGES['banner'])
prompt(MESSAGES['Welcome'])
prompt(MESSAGES['banner'])

prompt(MESSAGES['name'])
name = input()
clear_console()

while True:
    prompt(MESSAGES['loan_amount'] + f" {name}")
    amount = input()
    while invalid_number(amount):
        prompt(MESSAGES['invalid_input'])
        amount = input()
    amount_result = float(amount)
    clear_console()

    duration_result = get_duration()
    clear_console()

    prompt(MESSAGES['loan_interest'])
    interest = input()
    while invalid_number(interest):
        prompt(MESSAGES['invalid_input'])
        interest = input()
    interest_result = calc_interest_apr(interest)
    clear_console()

    ### CALCULATION OF MONTHLY PAYMENT

    if interest_result == 0:
        monthly_payment = amount_result / duration_result
    else:
        monthly_payment = amount_result * \
            (interest_result / (1 - (1 + interest_result) ** -duration_result))

    ### SHOW RESULT

    print(f"\n== {name}'s Loan Summary ==")
    print(f"Loan Amount: ${amount_result:,.2f}")
    print(f"Annual Interest Rate (APR): {interest}%")
    print(f"Loan Duration: {int(duration_result)} months")
    print(f"Your monthly Payment: ${monthly_payment:,.2f}")

    prompt(MESSAGES['banner'])
    prompt(MESSAGES['another_calc'] + f" {name} ?")
    another_calculation = input()
    if another_calculation.lower() != "y":
        break
    clear_console()
