"""

Rock Paper Scissors Lizard Spock Game

"""

import random

VALID_CHOICES = ["r", "p", "sc", "l", "sp"]

# Helper methods

def prompt(message):

    """Display messages to player"""

    print(f"==> {message}")

def display_winner(player, computer):

    """Display winner of the game"""

    if player_wins(player, computer):
        print('You win!')
    if player == computer:
        print("It's a tie!")
    else:
        print("Computer wins!")

def display_choices(player, computer):

    """Display choices of player and computer"""

    choices_dict = {
        'r': 'Rock',
        'p': 'Paper',
        'sc': 'Scissors',
        'l': 'Lizard',
        'sp': 'Spock'
    }

    prompt(f"You chose: {choices_dict.get(player, 'Invalid choice')}; "
           f"Computer chose: {choices_dict.get(computer, 'Invalid choice')}")


def player_wins(player_choice, comp_choice):

    """Determine if player or computer wins a round"""

    if (
        (player_choice == 'r' and comp_choice == 'sc') or
        (player_choice == 'r' and comp_choice == 'l') or
        (player_choice == 'p' and comp_choice == 'r') or
        (player_choice == 'p' and comp_choice == 'sp') or
        (player_choice == 'sc' and comp_choice == 'p') or
        (player_choice == 'sc' and comp_choice == 'l') or
        (player_choice == 'l' and comp_choice == 'p') or
        (player_choice == 'l' and comp_choice == 'sp') or
        (player_choice == 'sp' and comp_choice == 'r') or
        (player_choice == 'sp' and comp_choice == 'sc')
    ):
        return True
    return False

# Main game loop

while True:
    prompt("Choose between: Rock(r), Paper(p), Scissors(sc), Lizard(l), Spock(sp)")
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_choices(choice, computer_choice)
    display_winner(choice, computer_choice)
       
    
    # while True:
    #     prompt("Do you want to play again (y/n)?")
    #     answer = input().lower()

    #     if answer.startswith('n') or answer.startswith('y'):
    #         break
    #     prompt("That's not a valid choice")

    # if answer[0] == 'n':
    #     break
