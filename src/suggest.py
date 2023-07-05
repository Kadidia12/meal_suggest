import random

def suggest() :
    meals = ['thiébou djeune', 'woudjila', 'yassa', 'fakoye']
    index = random.randint(0, len(meals))
    return meals[index]



print(suggest())