import random
from itertools import filterfalse

rock = '''
rock
    _______
---'   ____)
      (____)
      (____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          ________)
         ________)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

# function to get user input. Will only allow valid entries
def get_user_int():
    allowedKeys = ["0", "1", "2"]
    user_enters = 9
    while user_enters not in allowedKeys:
        user_enters = input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n")
    return int(user_enters)

# check who wins
def choose_winner(user, computer):
    if user == computer:
        return "It's a draw!\n"
    elif user == 0 and computer == 2:
        return "You win!\n"
    elif user == 1 and computer == 0:
        return "You win!\n"
    elif user == 2 and computer == 1:
        return "You win!\n"
    else:
        return "You lose!\n"

def play_again():
    try_again = input("Do you wish to try again? Y for Yes, Any other key for No\n")
    if try_again == "Y" or try_again == "y":
        return True
    else:
        return False

continue_game = True
while continue_game:

    user_int = get_user_int()

    user_game_image = game_images[user_int]

    computer_int = random.randint(0,2)
    #print(computer_player_int)
    computer_game_image = game_images[computer_int]

    print("You chose " + user_game_image)

    print("The computer chose " + computer_game_image)

    print(choose_winner(user_int, computer_int))

    continue_game = play_again()