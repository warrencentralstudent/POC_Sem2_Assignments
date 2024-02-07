#Create a random number generator that simulates a dice roll

import random

dice_rolls = [1, 2, 3, 4, 5, 6]

random_roll = random.sample(dice_rolls, 1)
print("You rolled a", random_roll[0])