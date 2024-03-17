import random
from collections import Counter
import matplotlib.pyplot as plt

def simulate(sequence):
    length = len(sequence)
    flips = []

    res = 0

    for i in range(length):
        flips.append(random.randint(0, 1))
        res += 1
    
    while sequence != flips[-length:]:
        flips.append(random.randint(0, 1))
        res += 1
    return res

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

if __name__ == "__main__":
    trials = 10000

    seq1 = [0, 0, 1]
    seq2 = [0, 1, 1]

    seq1Counts = []
    seq2Counts = []

    seq1Winner = 0
    seq2Winner = 0
    ties = 0

    for i in range(trials):
        l1 = simulate(seq1)
        l2 = simulate(seq2)
        seq1Counts.append(l1)
        seq2Counts.append(l2)
        if l1 < l2: seq1Winner += 1
        if l2 < l1: seq2Winner += 1
        if l1 == l2: ties += 1
    print(seq1Winner, seq2Winner, ties)
    print(sum(seq1Counts)/trials)
    print(sum(seq2Counts)/trials)
    plot(seq1Counts, seq2Counts)
