import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
number_of_friends = friends.__len__()
random_number = random.randint(0, number_of_friends-1)
print(number_of_friends)
print(friends[random_number])
#alternatively you can just use the following:

print(random.choice(friends))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][0])