import random

while True:  # 4. Give user an option to play again if the user selects yes, run game again, else break
    # 1. First define list of choices
    choices = ['R', 'S', 'P']
    cpu = random.choice(choices)
    user = input('ROCK, PAPER OR SCISSORS? (Enter as R, S OR P): ')

    """determine conditionals"""
    # 2. If user choice is not in the choices list, run a loop again.
    while user.upper() not in choices:
        user = input('Invalid input! Try again\n ROCK, PAPER OR SCISSORS? (Enter as R, S or P): ')
    # 3. determine the winner if the user_input is in the list of choices
    if user == cpu:
        print(f"User choice : {user}\n CPU = {cpu}\n IT'S A TIE!")
    elif user == 'R' and cpu == 'S':  # 3. rock beats scissors, scissors beat paper, paper beats rock
        print(f"Player {user} : CPU {cpu}\n Player won! CPU lost")
    elif user == 'S' and cpu == 'p':
        print(f"Player {user} : CPU {cpu}\n Player won! CPU lost")
    elif user == 'P' and cpu == 'R':
        print(f"Player {user} : CPU {cpu}\n Player won! CPU lost")
    else:
        print(f"Player {user} : CPU {cpu}\n CPU won! Player lost.")

    play_again = input('Do you want to play again? y/n: ')
    if play_again.lower() != 'y':
        break

print('Till next time!')