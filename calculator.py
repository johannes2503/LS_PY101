from calculator_messages import prompt, messages

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# Go again?
while True:

    prompt(messages['welcome'])

    prompt(messages["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(messages["invalid_number"])
        number1 = input()

    prompt(messages["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(messages["invalid_number"])
        number2 = input()

    prompt(messages["operation"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages["invalid_operation"])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(messages["result"])

    # ask for two numbers
    # ask for operation
    # perform operation and display results
    prompt(messages["another_operation"])
    answer = input()
    if answer and answer[0].lower() != 'y':
        break