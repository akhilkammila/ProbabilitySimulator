"""
Problem:
3 players
A keeps drawing random numbers 1-100. Busts if total is > 100.
B watches, then does the same.
C watches, then does the same.
Player with highest total (without busting) wins.

Initial guess:
A goes for 85+
B goes for 70+
C goes for highest # so far

Solving approach:
Assume A busts (happens often), find optimal strategy
"""

import random
import matplotlib.pyplot as plt
import numpy as np

TRIALS = 10000

def findPWin(threshold):
    wins = 0

    for i in range(TRIALS):
        total = 0
        while total < threshold:
            total += random.randint(1, 100)
        wins += (total <= 100)
    
    return wins / TRIALS

pWins = []
for i in range(1, 101):
    pWins.append(findPWin(i))

xAxis = [i for i in range(1, 101)]
plt.scatter([i for i in range(1, 101)], pWins)
plt.show()

# x = np.array(pWins)
# y = np.array(xAxis)
# degree = 2
# coefficients = np.polyfit(x, y, degree)

# polynomial = np.poly1d(coefficients)
# plt.plot([])