import random
from operator import truediv

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 2


# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ''
for each_letter in chosen_word:
    placeholder += '_'

print(placeholder + '\n')
display = placeholder

while display != chosen_word and lives > 0:
    guess = input("Guess a letter: ").lower()
    guess_correct = False

    # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

    index = 0
    for letter in chosen_word:
        if letter == guess:
            display = display[:index] + letter + display[index + 1:]
            guess_correct = True
        index += 1
    if not guess_correct:
        lives -= 1

    print(display)
    print(lives.__str__())

if lives == 0:
    print("You've run out of lives!")
else:
    print("You've guessed the word!")