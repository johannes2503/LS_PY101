
import random

VALID_CHOICES = ["r", "p", "sc", "l", "sp"]

def prompt(message):
    print(f"==> {message}")

def display_choices(player, computer):
    prompt(f"You chose: {player}; Computer chose: {computer}")

def display_winner(player, computer):
    if player_wins(player, computer):
        print('You win!')
    elif player == computer:
        print("It's a tie!")
    else:
        print("Computer wins!")

def display_choices(player, computer):
    choices_dict = {
        'r': 'Rock',
        'p': 'Paper',
        'sc': 'Scissors',
        'l': 'Lizard',
        'sp': 'Spock'
    }
    prompt(f"You chose: {choices_dict.get(player, 'Invalid choice')}; Computer chose: {choices_dict.get(computer, 'Invalid choice')}")


def player_wins(player_choice, computer_choice):
    if (
        (player_choice == 'r' and computer_choice == 'sc') or
        (player_choice == 'r' and computer_choice == 'l') or
        (player_choice == 'p' and computer_choice == 'r') or
        (player_choice == 'p' and computer_choice == 'sp') or
        (player_choice == 'sc' and computer_choice == 'p') or
        (player_choice == 'sc' and computer_choice == 'l') or
        (player_choice == 'l' and computer_choice == 'p') or
        (player_choice == 'l' and computer_choice == 'sp') or
        (player_choice == 'sp' and computer_choice == 'r') or
        (player_choice == 'sp' and computer_choice == 'sc')
    ):
        return True
    else:
        return False
    
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

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break