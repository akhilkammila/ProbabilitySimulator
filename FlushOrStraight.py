"""
Guess: flush wins 57% of the time
"""
import random

def checkFlush(cards):
    counts = [0]*4
    for card in cards:
        if 1 <= card <= 13: counts[0] += 1
        if 14 <= card <= 26: counts[1] += 1
        if 27 <= card <= 39: counts[2] += 1
        if 40 <= card <= 52: counts[3] += 1
    
    for i in range(4):
        if counts[i] >= 5: return True
    return False

def checkStraight(cards):
    cards = set([(card-1)%13 for card in cards]) # 0 to 12

    for i in range(13):
        if i == 9:
            if i in cards \
            and (i+1) in cards \
            and (i+2) in cards \
            and (i+3) in cards \
            and 0 in cards: return True

        if i in cards \
            and (i+1) in cards \
            and (i+2) in cards \
            and (i+3) in cards \
            and (i+4) in cards: return True

    return False

def simulate():
    pool = [i+1 for i in range(52)]
    random.shuffle(pool)

    currCards = set()

    for i in range(52):
        currCards.add(pool[i])
        print(currCards)

        flush = checkFlush(currCards)
        straight = checkStraight(currCards)

        if flush and straight: return 0
        if flush: return 1
        if straight: return -1
    


if __name__ == "__main__":
    tests = 3
    flushWins = 0
    straightWins = 0
    ties = 0

    for i in range(tests):
        res = simulate()
        print(res)
        
        if res == 1: flushWins += 1
        if res == 0: ties += 1
        if res == -1: straightWins += 1
    
    print(f"flush wins: {flushWins}")
    print(f"straight wins {straightWins}")
    print(f"ties: {ties}")
    print(f"tests: {tests}")