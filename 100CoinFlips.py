"""
100 flips

will HH or HT appear more often?

guess: HT, same EV but HH more skewed to higher
"""

import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def simulate(length):
    # 0 is heads, 1 is tails
    sequence = [random.randint(0, 1) for i in range(length)]
    HH = 0
    HT = 0

    for i in range(length-1):
        if sequence[i] == 0:
            HH += (sequence[i+1] == 0)
            HT += (sequence[i+1] == 1)
        
    return (HH, HT)

def plot(hhCounts, htCounts):
    fig, (axs1, axs2) = plt.subplots(2, sharex=True)
    
    
    counts = Counter(hhCounts)
    nums, occurences = list(counts.keys()), list(counts.values())
    axs1.scatter(nums, occurences)
    axs1.set_title("HH frequencies")

    counts = Counter(htCounts)
    nums, occurences = list(counts.keys()), list(counts.values())
    axs2.scatter(nums, occurences)
    axs2.set_title("HT frequencies")
    fig.tight_layout()

    plt.show()

if __name__ == "__main__":
    tests = 100000
    length = 100

    hhWins = 0
    htWins = 0
    ties = 0
    total = 0

    hhCounts = []
    htCounts = []

    for i in range(tests):
        HH, HT = simulate(length)
        hhWins += (HH > HT)
        htWins += (HT > HH)
        ties += (HH == HT)
        total += 1

        hhCounts.append(HH)
        htCounts.append(HT)

    print(hhWins, htWins, ties, total)
    print(sum(hhCounts), sum(htCounts), sum(hhCounts)/total, sum(htCounts)/total)
    print(np.median(np.array(hhCounts)), np.median(np.array(htCounts)))
    print(np.mean(np.array(hhCounts)), np.mean(np.array(htCounts)))
    plot(hhCounts, htCounts)