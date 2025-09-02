"""
Rock Paper Scissors Game
"""

import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
choice = input()

while choice not in VALID_CHOICES:
    prompt("Thats not a valid choice")
    choice = input()

computer_choice = random.choice(VALID_CHOICES)

prompt(f"You chose {choice}, computer chose {computer_choice}")
