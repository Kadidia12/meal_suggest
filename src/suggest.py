import random


def suggest():
    meals = ['thiébou djeune', 'woudjila', 'yassa', 'fakoye', 'Mafé', 'Burger']
    index = random.randint(0, len(meals) - 1)
    return meals[index]


print(suggest())
