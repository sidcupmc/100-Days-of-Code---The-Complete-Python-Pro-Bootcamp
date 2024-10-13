print("Welcome to Python Pizza Deliveries!")
cost=0

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "s":
    cost = 15
    if pepperoni == "y":
        cost += 2
elif size == "m":
    cost = 20
elif size == "l":
    cost = 25
else:
    print("You entered the wrong inputs")
    exit()

if pepperoni == "y":
    if size == "s":
        cost += 2
    else:
        cost += 3
if extra_cheese == "y":
    cost += 1

print(f"Total cost is ${str(cost)}")

