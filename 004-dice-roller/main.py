import random


def roll_dice(count, sides):
    rolls = []

    for _ in range(count):
        roll = random.randint(1, sides)
        rolls.append(roll)

    return rolls


dice = input("ダイスを入力してください（例: 2d6, 2d6+3）: ")

dice = dice.lower()

if "+" in dice:
    dice_part, bonus = dice.split("+")
    bonus = int(bonus)
else:
    dice_part = dice
    bonus = 0

count, sides = dice_part.split("d")

count = int(count)
sides = int(sides)

rolls = roll_dice(count, sides)
total = sum(rolls) + bonus

print("出目:", rolls)

if bonus > 0:
    print("補正:", bonus)

print("合計:", total)