"""
Car Loan Calculator
This script calculates the monthly payment for a car
loan based on the loan amount, interest rate, and loan duration.

x Consider allowing more flexibility in loan duration input. For example, someone might want a 4.5-year loan (54 months).
x It would be nice to give the user an option to perform another calculation without exiting the program.
You could consider clearing the screen between operations to keep the interface clean.
The loan duration prompt says "Please enter duration of loan on years" - a small correction to "in years" would be more natural.

You could extract the input gathering for loan amount and interest rate into functions similar to how you did with get_duration(). This would make your main code even more concise and readable.
The loan calculation section could be moved into its own function (e.g., calculate_monthly_payment(principal, rate, duration)).
Similarly, the result display section could be extracted into a function like display_loan_summary().
Consider using constants for values like the maximum loan duration (8 years) to make future modifications easier.
In your calc_interest_apr() function, the variable name output is a bit generic. Something like monthly_rate would be more descriptive.

"""
import json
import os

# Load the messages from the JSON file
with open('messages.json', encoding="utf-8") as file:
    MESSAGES = json.load(file)

### DECLARING FUNCTIONS

def clear_console():
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
    output = float(loan_interest) / 100 / 12
    return output

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