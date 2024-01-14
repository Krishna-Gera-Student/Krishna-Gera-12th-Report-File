import random

def roll_dice():
    return random.randint(1, 6)

dice_roll1 = roll_dice()
dice_roll2 = roll_dice()

print("Dice 1:", dice_roll1)
print("Dice 2:", dice_roll2)
