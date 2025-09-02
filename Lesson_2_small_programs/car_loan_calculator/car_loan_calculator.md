# CAR LOAN CALCULATOR

### Information collected from user - Casual Execution

- Loan amount
  - Validate input
  - Only decimal numbers
- Loan duration
  - Valdate input
  - Only decimal numbers
- Loan interest

  - Validate input
  - Only decimal number

### Loan calculation

- Calculate loan payment per month

  - Divide interest by months (12)
  - Divide loan duration by months
  - Calculate loan payment per month
  - Return the amount in $

- Print out the result

### Formal Execution

START

- Given data from user

  - SET loan_amount = GET input from user
  - SET loan_duration = GET input from user
  - SET loan_interst = GET input from user

- Validate inputs

  - READ loan_amount
  - WHILE loan_amount != float

    - PRINT "incorrect input"
    - SET loan_amount = GET input from user

  - READ loan_duration
  - WHILE loan_duration not in ["1", "2", "3", "4", "5", "6", "7", "8"]

    - PRINT "value must be between 1-8"
    - SET loan_duration = GET input from user

  - READ loan_interrest
  - WHILE loan_amount != float

    - PRINT "incorrect input"
    - SET loan_amount = GET input from user

  -
