"""
140 balls total, 20 of red, 20 yellow, 100 green
We choose 5 more red than yellow in the first 70

What is probability of ball being green on 71st: EV of (# of green left / 70)

We can find this by summing over possibilities:
    5R, 0Y, 65 green
    6R, 1Y, 64 green
    and so on
For each possibilitiy find: probability of that possibility * (# of green left / 70)
"""

from math import comb

"""
Args:
    ryCount: # of red + yellow
    more: ryCount needs to be split into r + y, where r = y + more
    greenCount: # of remaining
"""

def findProbability(redCount, yellowCount, more, greenCount, midway = -1):
    if midway == -1: midway = (redCount + yellowCount + greenCount) // 2

    # yellows can range from 0 until yellows + (yellows + more) <= ryCount
    totalProb = 0.0
    runningEv = 0.0

    yellows = 0
    reds = yellows + more
    total = redCount + yellowCount + greenCount
    while(reds <= redCount and yellows <= yellowCount and reds + yellows <= midway):
        greens = midway - reds - yellows
        prob = comb(redCount, reds) * comb(yellowCount, yellows) * comb(greenCount, greens)

        # prob of greens left in second half
        greenChance = (greenCount - greens) / (total - midway)
        totalProb += prob
        runningEv += prob * greenChance

        yellows += 1
        reds += 1
    return runningEv / totalProb

if __name__ == "__main__":
    # for i in range(20):
    #     print(findProbability(20, 20, i, 100))

    # for i in range(5):
    #     print(findProbability(4,4,i,20))

    print(findProbability(4,4,4,20,10))