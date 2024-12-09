"""
instead of 500 1500, doing 5 15

1/2 chance of 5, 1/2 chance of 15
    5/15 is the total # of dollars in circulation
    p1 and p2 have bids
    as long as bid < total dollars, pay out the dollars to the lowest bid

this creates payoff matrix for every possibility of 2 bids
    1/2 chance of 5: pay off the lowest bid if possible, subtract out. then pay off high if possible
"""

"""
Finds the payout for i only
"""
def findPayout(i, j, money):
    if i < j: return i if i <= money else 0
    if i == j: return i if i + j <= money else 0 # if tie, both or 0 get paid out
    if i > j: return i if i <= money - j else 0
    return 0

"""
Payouts are [5, 15]
probs are [1/2, 1/2]
"""
def createMatrix(payouts, probs):
    n = max(payouts)

    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):

            money = 0
            for k in range(len(payouts)):
                money += findPayout(i, j, payouts[k]) * probs[k]
            row.append(money)
        
        print(*row)

createMatrix([5, 15], [1/2, 1/2])