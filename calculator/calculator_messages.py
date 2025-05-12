def prompt(message):
    print(f"==> {message}")

def messages(message, lang="en"):
    return MESSAGES[lang][message]

MESSAGES = {
    "en": {
        "welcome": "Welcome to the calculator!",
        "first_number": "Please enter the first number:",
        "second_number": "Please enter the second number:",
        "operation": "Please select an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division",
        "result": "The result is: ",
        "another_operation": "Do you want to perform another operation? (y/n)",
        "invalid_number": "Invalid number, please try again.",
        "invalid_operation": "Invalid operation, please try again."
    },
    "es": {
        "welcome": "¡Bienvenido a la calculadora!",
        "first_number": "Por favor, introduce el primer número:",
        "second_number": "Por favor, introduce el segundo número:",
        "operation": "Por favor, selecciona una operación:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División",
        "result": "El resultado es: ",
        "another_operation": "¿Quieres realizar otra operación? (s/n)",
        "invalid_number": "Número inválido, por favor intenta de nuevo.",
        "invalid_operation": "Operación inválida, por favor intenta de nuevo."
    }
}