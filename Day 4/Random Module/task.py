import random
import my_module

random_number = random.randint(1, 10)
random_float = random.random()
random_float2 = random.uniform(1,10)
print(f"Random integer is {random_number}")
print(f"Random floating number is {random_float}")
print(f"Random floating number2 is {random_float2}")
print(f"My favourite number is {my_module.my_favourite_number}")

random_coin_number = random.randint(0, 1)
if random_coin_number == 0:
    print("Heads")
else:
    print("Tails")