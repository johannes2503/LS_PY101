
Python's flexibility lets a developer use it in many ways, but it also lets you easily write code that fails to function when run. There are many situations where the Python interpreter cannot continue executing a program. Instead, it creates an **Exception object** that describes the problem and stops the program.

As a developer, you want to do your best to avoid errors when your programs run. Let's look at the most common types of errors that can arise. In the next few assignments, we'll learn techniques to both prevent errors and handle those that you can't avoid.

## Terminology

When an error occurs in a Python program, we say that it **raises** an Exception. Some programming languages use the term _errors_ to denote exception; some other languages refer to throwing exceptions. Thus, you might hear fellow developers talk about exceptions being thrown in Python programs. Despite these terminological differences, remember that the terms Exception and Error are interchangeable, just as _raise_ and _throw_ are.

## NameError

A `NameError` arises when you attempt to use a variable or function that hasn't been defined.

```python
a        # Referencing an undefined variable results in a NameError.
a()      # The same applies when trying to call an undefined function.
```

## TypeError

A `TypeError` occurs when a value of the wrong type is used in an expression. For instance, the following situations should raise a `TypeError` exception:

- using an argument of the wrong type as a function argument
    

- ```python
    >>> my_str = "abc"
    >>> my_str.find(42)  # TypeError: must be str, not int
    ```
    
- trying to call an object that isn't callable:
    

- ```python
    >>> my_int = 42
    >>> my_int()        # TypeError: 'int' object is not callable
    ```
    

## SyntaxError

A `SyntaxError` occurs when Python encounters code that does not meet its syntactic rules. For instance, a string that lacks the trailing quote character is a syntax error:

```python
print('hello)
# SyntaxError: unterminated string
```

A `SyntaxError` is unique in that it typically arises immediately after loading a Python program but before it starts running. Unlike `NameError` and `TypeError`, which hinge on specific variables and values encountered during runtime, Python detects `SyntaxErrors` solely from the program's text.

```python
def (     # SyntaxError: unexpected EOF while parsing
```

Several cases can lead to a `SyntaxError` while a Python program is running. For example, this code would result in a `SyntaxError` at runtime:

```python
expression = "2 * (3 + 4)"
result = eval(expression)
```

That code uses Python's `eval` function to evaluate an Python expression that has been written as a string. Thus, the above code is effectively the same as:

```python
result 2 * (3 + 4
```

The key difference is that the `eval` function raises a `SyntaxError` when the code is executed, but the second code fragment raises a `SyntaxError` during the parsing phase.

Don't worry about remembering what `eval` does. While it has its uses, it's a function that is best avoided by most developers. It's slow and potentially very dangerous from a security standpoint.

## ValueError

A `ValueError` is raised when a function receives an argument of the correct data type, but the value of the argument is inappropriate for the operation.

```python
number = int("abc")
# ValueError: invalid literal for int() with base 10: 'abc'
```

## IndexError

An `IndexError` occurs when trying to access an index of a sequence (like a list or string) that is outside the range of valid indexes.

```python
nums = [1,2]
num = nums[2] # IndexError: list index out of range
```

## KeyError

A `KeyError` is raised when trying to access a dictionary key that doesn't exist.

```python
my_dict = {"a": 1, "b": 2}
value = my_dict["c"] # KeyError: 'c'
```

## ZeroDivisionError

A `ZeroDivisionError` occurs when attempting to divide by zero or when trying to use 0 on the right side of the modulo (`%`) operator:

```python
result1 = 10 / 0 # ZeroDivisionError: division by zero
result2 = 42 % 0 # ZeroDivisionError: integer modulo by zero
```

## Exception Handling

Exception handling lets you gracefully manage errors that might occur during program execution. Python provides a structured way to handle exceptions using the `try`, `except`, `else`, and `finally` statements.

Here's how the exception handling process works:

1. **Try Block**: The code that might raise an exception is placed within the `try` block. Python will monitor this block for any exceptions that may occur during its execution.
    
2. **Except Block**: If an exception is raised in the `try` block, Python will look for a matching `except` block that can handle that specific type of exception. If a match is found, the code within the corresponding `except` block is executed.
    
3. **Else Block (Optional)**: The `else` block is executed only if no exceptions occurred in the `try` block. It's used for code that should run when no errors were encountered.
    
4. **Finally Block (Optional)**: The `finally` block is always executed, regardless of whether an exception was raised or not. It is used for cleanup operations or tasks that must be performed, such as releasing resources.
    

Let's walk through an example that demonstrates the different aspects of exception handling in Python:

```python
try:
    num_str = input("Enter a number: ")
    num = int(num_str)

    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Exception handling complete.")
```

In this example:

- If the user enters a non-integer value, a `ValueError` is caught, and the program displays an error message.
- If the user enters zero, a `ZeroDivisionError` is caught, and the program warns about division by zero.
- If no exceptions occur, the division result is printed.
- Regardless of whether an exception was caught or not, the `finally` block ensures that the final message is displayed.

[Debugging Techniques](https://launchschool.com/lessons/a29e9831/assignments/266a9e03 "Go to previous assignment")

[

](https://launchschool.com/lessons/a29e9831/assignments/378f8121#top "Go to top.")