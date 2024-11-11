import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


letters_list = []
number_list = []
symbols_list = []


for item in range(0,nr_letters):
    letters_list.append(random.choice(letters))
print(letters_list)

for item in range(0,nr_numbers):
    number_list.append(random.choice(numbers))
print(number_list)

for item in range(0,nr_symbols):
    symbols_list.append(random.choice(symbols))
print(symbols_list)

ordered_password_list = letters_list + number_list + symbols_list
print(ordered_password_list)

random.shuffle(ordered_password_list)
print(ordered_password_list)











