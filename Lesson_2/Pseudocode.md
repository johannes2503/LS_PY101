### Formal Pseudocode

Before we can take our pseudocode and translate it to program code, we must formalize the pseudocode a little more. We'll still use English, but we'll use some keywords to help us break down the program logic into concrete commands, which makes translating to code more natural.

We'll use the below keywords to assist us, along with their meaning.

|Keyword|Meaning|
|---|---|
|START|start of the program|
|SET|set a variable that we can use for later|
|GET|retrieve input from user|
|PRINT|display output to user|
|READ|retrieve a value from a variable|
|IF/ELSE IF/ELSE|show conditional branches in logic|
|WHILE|show looping logic|
|END|end of the program|

We can use the above keywords to act as a pseudo-programming language, but one that's still written in English, which lets us be more relaxed about the precision of the syntax. Here's a stab at translating to formal pseudocode:

```plaintext
START

# Given a collection of integers called "numbers"

SET iterator = 1
SET savedNumber = value within numbers collection at space 1

WHILE iterator <= length of numbers
    SET currentNumber = value within numbers collection at space "iterator"
    IF currentNumber > savedNumber
        savedNumber = currentNumber

    iterator = iterator + 1

PRINT savedNumber
```

Note that we're using PRINT to show the final return value. This translation almost looks like program code, but it's not. The advantage of this additional step is to give more structure to the pseudocode and to let us think at a more detailed level, yet still not worry about a programming language syntax. Though detailed it may be, this pseudocode still suffers from the same problem -- we can't verify that this logic is sound. Finally, to test the logic, we need to translate it into program code.

### Translating Pseudocode to Program Code

We're using Python, so here's a stab at it in Python. Note that we are starting `iterator` at index `0` since list indexing in Python starts at `0`. For the same reason, on line 5, we are using `<` instead of `<=`

```python
def find_greatest(numbers):
    iterator = 0
    saved_number = numbers[iterator]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number

        iterator += 1

    return saved_number
```

If we run the above code, we can show that our pseudocode logic works!

Now, let's look at the working code and start to improve it from a lower layer -- at the programming language level. For instance, what should we do if `numbers` is `None`? Perhaps we can use a guard clause that returns `None`, like this: `if numbers is None: return`. Now that we have the general logic and code in place, there are other small improvements we can make.

In this example, the function we wanted to write was straightforward. We were able to write a few lines of pseudocode, move it to a more formal pseudocode, and then translate it to Python. However, most problems you encounter will be more difficult than this example. You won't be able to take the same approach. That is, you won't be able to detail the entire problem in pseudocode, then translate it into Python. If you did, you'd likely discover that a lot of your pseudocode logic and assumptions are incorrect. You may need to make changes that ripple across the entire program, forcing you to start over time and again. Remember, pseudocode is a guess at the solution; there's no verification that the logic is correct. You can't do that until you translate it to program code.

For more sophisticated problems, we need to take a piecemeal approach when writing pseudocode, then translate that pseudocode to Python. Once we verify that the logic is correct, we can move to the next piece of the problem. Step-by-step, we slowly load the problem into our brain, verifying the logic each step along the way.

We'll show you how to use flowcharts to help with this in the next assignment. For now, try a few practice rounds using pseudocode to guide your problem-solving logic. For example, write out pseudocode (both casual and formal) that does the following:

- a function that returns the sum of two numbers
- a function that takes a list of strings, and returns a string that is all those strings concatenated together
- a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance:
    

- ```python
    every_other([1,4,7,2,5]) # => [1,7,5]
    ```
    
- a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is `'x'` and the string is `'axbxcdxex'`, the function should return 6 (the index of the 3rd `'x'`). If the given character does not occur at least 3 times, return `None`.
- a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance:
    

- ```python
    merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
    ```
    
    You may assume that both list arguments have the same number of elements.

You don't need to write any Python code here; just practice writing the logic in English.

You don't need to use pseudocode for every bit of code you write, especially once you get down to the function level. However, it's a good idea to always use it here in this course and the associated Small Problem exercises. This will help you overcome problems in the short term, and prepare you for the interview assessment later on.

For brevity, we won't use pseudocode extensively in this course. However, we will use it for the more complicated problems and when we feel that it most helpful to see the pseudocode for a problem.

[Walk-through: Calculator](https://launchschool.com/lessons/a29e9831/assignments/9a237d96 "Go to previous assignment")

[

](https://launchschool.com/lessons/a29e9831/assignments/b3aaf50f#top "Go to top.")