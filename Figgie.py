"""
40 cards distributed among 4 (or 5) players
12 cards of one suit (suit 1)
10 cards of a suit (suit 2)
10 cards of a suit (suit 3)
8 cards of a suit (suit 4)
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

class FiggieGame:
    cards = [1] * 12 + [2] * 10 + [3] * 10 + [4] * 8
    playersList = []
    numPlayers = 0

    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
    
    def reset(self):
        numCards = 40
        cardsPerPlayer = int(numCards/self.numPlayers)

        np.random.shuffle(self.cards)
        self.playersList = []
        for i in range(self.numPlayers):
            self.playersList.append(self.cards[i*cardsPerPlayer : i*cardsPerPlayer + cardsPerPlayer])

numPlayers = 5
game = FiggieGame(numPlayers)
boundaryHit = 0
correctGuess = 0
trials = 100000

for i in range(trials):
    game.reset()

    # check each player
    for player in game.playersList:
        counts = Counter(player)
        for key, val in counts.items():
            if (val >= 5):
                boundaryHit += 1
                correctGuess += (key == 1)
    
print(boundaryHit/(trials*numPlayers))
print(correctGuess/boundaryHit)