import random

rock = '''
    _______
---'   ____)
      (____)
      (____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          ________)
         ________)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def choose_winner(human_int, computer_int):

    if human_int == computer_int:
        return "It's a draw!"
    elif human_int == 0 and computer_int == 2:
        return "human wins"
    elif human_int == 1 and computer_int == 0:
        return "human wins"
    elif human_int == 2 and computer_int == 1:
        return "human wins"
    else:
        return "computer wins"

choices = [rock, paper, scissors]

human_player_int = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print(human_player_int)
human_player_choice = choices[human_player_int]

computer_player_int = random.randint(0,2)
print(computer_player_int)
computer_player_choice = choices[computer_player_int]

print("You chose " + str(human_player_int) + " Which is "  +  "\n" + human_player_choice)

print("The computer chose " + str(computer_player_int) + " Which is "  +  "\n" + computer_player_choice)

print(choose_winner(human_player_int, computer_player_int))
