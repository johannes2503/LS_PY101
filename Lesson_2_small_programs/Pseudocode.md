# Pseudocode

### Example 1 - a function that returns the sum of two numbers.

Casual example.

- Given two numbers.
  - Add the two numbers together.
- return added numbers.

Formal example.

START

- Given two numbers.

  - SET num1 = any number.
  - SET num2 = any number.
  - SET added_numbers = num1 + num2.
  - PRINT added_numbers.

END

### Example 2 - a function that takes a list of strings, and returns a string that is all those strings concatenated together.

Casual example.

- Given a list of strings.

  - Save a empty string
  - Iterate over the list of strings on by one.

    - for each iteration add the strings together.
    - reasign the added strings to the empty string.

  - Return the concatenated string.

Formal example.

START

- Given a list of strings.
- SET final_string = ""
- FOR string in list_of_strings
  - SET final_string += string
- PRINT final_string

END

### Example 3 - a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance:

`every_other([1,4,7,2,5]) # => [1,7,5]`

Casual example.

- Given a list of integers.

  - Save a empty list

  - iterate over the given list
    - append every other element to the empty list
  - Return the new list

Formal example.

START

- Given a list of integers called "numbers"

  - SET every_other = []
  - SET iterator = 1
  - WHILE iterator <= len(numbers)
    - append every other number to every_other list
    - iterator + 2
  - PRINT every_other

END

### Example 4 - a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.

Casual example.

- Given a string and character

  - if more the 3 of the same charater are given
    - return the index of the third character
  - else return none

Formal example.

START

- Given a string and character

  - SET count = 0
  - SET iterator = 0

  - WHILE iterator <= length of string
    - IF the character is found in string
      - count + 1
      - IF count is equal to 3
        - PRINT iterator
      - itertor + 1
    - PRINT None

END

### Example 5 - a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance:

`merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]`

Casual example.

- Given are two lists of numbers

  - Save a empty final list.

  - Iterate over the even list
    - append them to the final list
  - Iterate over the odd list
    - append numbers to every other index of final list
  - Return the final list

- Formal example

START

- Given are two lists of numbers

  - SET merged_list = empty list
  - SET iterator = 0

  - WHILE iterator <= length of even list or iterator <= length of odd list
    - IF merged_list <= length of even list
      - append to merged_list
    - IF merged_list <= length of odd list
      - append to merged_list
    - iterator + 1
  - PRINT merged_list

END
