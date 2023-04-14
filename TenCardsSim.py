"""
Finds the probability of certain sequences hitting when 10 cards
are drawn from the deck

1. checks for triples (ex: Ace Ace Ace)
2. checks for three face cards or more (J, Q, K are face cards)
3. checks for less than 2 pairs (only 0 or 1 pairs)
"""

import random
from collections import Counter

# Deck of Cards
cards = [i+1 for i in range(13)]
cards *= 4

# Checks for conditions
def checkTriple(arr):
    counts = Counter(arr)
    return any([val >= 3 for val in counts.values()])

def checkThreeFace(arr):
    counts = Counter(arr)
    faceVals = counts[11] + counts[12] + counts[13]
    return faceVals >= 3

def lessThanTwo2Pairs(arr):
    counts = Counter(arr)
    twoPairs = list(filter(lambda x : counts[x]>=2, counts))
    return len(twoPairs) < 2

# Sims drawing 10 cards
def simulate():
    arr = random.sample(cards, 10)
    return lessThanTwo2Pairs(arr) #change this to run other sims

# Runs sims
if __name__=="__main__":
    sims = 1000000
    hits = 0
    for i in range(sims):
        if (simulate()): hits += 1
    
    print(hits/sims)