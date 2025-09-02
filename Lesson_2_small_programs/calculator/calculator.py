from calculator_messages import prompt, messages

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False
LANGUAGE = "en"

while True:

    prompt(messages('welcome', LANGUAGE))

    prompt(messages('first_number', LANGUAGE))
    number1 = input()

    while invalid_number(number1):
        prompt(messages(('invalid_number', LANGUAGE)))
        number1 = input()

    prompt(messages('second_number', LANGUAGE))
    number2 = input()

    while invalid_number(number2):
        prompt(messages(('invalid_number', LANGUAGE)))
        number2 = input()

    prompt(messages('operation', LANGUAGE))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages('invalid_operation', LANGUAGE))
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(messages('result', LANGUAGE))

    prompt(output)
    prompt(messages('another_operation', LANGUAGE))
    another_operation = input()
    if another_operation.lower() != "y" and another_operation.lower() != "s":
        break
