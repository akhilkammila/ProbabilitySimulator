"""
Given 2 dice that sum to 20
what is the optimal configuration that leads to the sum being >= 12
"""
import random

tests = int(1e6)
def testDice(dice1, dice2, bound):
    successful = 0
    for i in range(tests):
        if random.randint(1, dice1) + random.randint(1, dice2) >= bound: successful += 1
    return successful/tests

for i in range(1, 10):
    dice1 = i
    dice2 = 20-i
    prob = testDice(dice1, dice2, 12)

    print(f"{dice1} {dice2}: {prob}")