import random

rolling_dice = True

while rolling_dice:
    print(random.randint(1, 6))
    another_roll = input("want to roll the dice again ? (y/n) ")
    if another_roll.lower() == "y":
        continue
    else:
        break
