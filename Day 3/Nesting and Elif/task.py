print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age= int(input("What is your age"))

    if age <= 12:
        print("Sorry, you are too young")

    elif age <= 18:
        print("You have to pay £5")
    else:
        print("You have to pay £8")
else:
    print("Sorry you have to grow taller before you can ride.")
