# sum of values on two dice is equal to 12

import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
total = dice1 + dice2

if total == 12:
    print("You won the game")
elif total == 7:
    print("You are having another game")
else:
    print("you lost the game")
