# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print("Welcome to the calculator!")

# Get the first number
print("Enter the first number: ")
number1 = input()

print("Enter the second number: ")
number2 = input()

print(f"{number1} {number2}")

print("What operation do you want to perform?\n1) Add\n2) Subtract\n3) Multiply\n4) Divide")

operation = input()

if operation == "1": #'1' is the string representation of the number 1
    output = int(number1) + int(number2)
elif operation == "2":
    output = int(number1) - int(number2)
elif operation == "3":
    output = int(number1) * int(number2)
elif operation == "4":
    output = int(number1) / int(number2)

print(f"The result is: {output}")
