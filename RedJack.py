"""
Finds the probability of getting at least 1 red jack
"""

import random
from collections import Counter

# Deck of Cards
cards = [i+1 for i in range(52)]

# Checks for conditions
def checkRedJack(arr):
    return arr.count(51) or arr.count(52)

def simulate():
    arr = random.sample(cards, 5)
    return checkRedJack(arr) #change this to run other sims

# Runs sims
if __name__=="__main__":
    sims = 100000
    hits = 0
    for i in range(sims):
        if (simulate()): hits += 1
    
    print(hits/sims)