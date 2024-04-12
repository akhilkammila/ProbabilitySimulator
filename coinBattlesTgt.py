"""
Conclusion: Consider both EV (use the betting method), and Win Margin

If same ev: win margin * win %  are equal
    we should have same # of rolls as other guy
    # less rolls when we win = # more rolls when we lose

If different ev: 
    we should have x less rolls than the other guy
    # less rolls when we win - # more rolls when we lose = ev diff
"""

import random
from collections import Counter
import matplotlib.pyplot as plt

def simulate(seq1, seq2):
    seq1Done = False
    seq2Done = False

    seq1Count = 0
    seq2Count = 0

    flips = []

    while not (seq1Done and seq2Done):
        flips.append(random.randint(0, 1))

        if not seq1Done:
            seq1Count += 1
            if flips[-len(seq1):] == seq1: seq1Done = True

        if not seq2Done:
            seq2Count += 1
            if flips[-len(seq2):] == seq2: seq2Done = True

    
    return [seq1Count, seq2Count]

def plot(hhCounts, htCounts):
    fig, (axs1, axs2) = plt.subplots(2, sharex=True)
    
    
    counts = Counter(hhCounts)
    nums, occurences = list(counts.keys()), list(counts.values())
    axs1.scatter(nums, occurences)
    axs1.set_title("seq1 counts")

    counts = Counter(htCounts)
    nums, occurences = list(counts.keys()), list(counts.values())
    axs2.scatter(nums, occurences)
    axs2.set_title("seq2 counts")
    fig.tight_layout()

    plt.show()

def convertString(seq):
    return [c == 'T' for c in seq]

if __name__ == "__main__":
    trials = 10000

    seq1 = "THH"
    seq2 = "TTH"

    seq1 = convertString(seq1)
    seq2 = convertString(seq2)

    print(seq1, seq2)

    seq1Counts = []
    seq2Counts = []

    seq1Winner = 0
    seq2Winner = 0
    ties = 0

    margin1 = []
    margin2 = []

    for i in range(trials):
        l1, l2 = simulate(seq1, seq2)
        seq1Counts.append(l1)
        seq2Counts.append(l2)
        if l1 < l2:
            seq1Winner += 1
            margin1.append(l2 - l1)
        if l2 < l1:
            seq2Winner += 1
            margin2.append(l1 - l2)
        if l1 == l2: ties += 1
    print(seq1Winner, seq2Winner, ties)
    print(sum(seq1Counts)/trials)
    print(sum(seq2Counts)/trials)
    print(sum(margin1)/len(margin1), sum(margin2)/len(margin2))
    # plot(seq1Counts, seq2Counts)
    # plot(margin1, margin2)
