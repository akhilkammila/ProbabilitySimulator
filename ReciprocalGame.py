import numpy as np
import matplotlib.pyplot as plt
import random

def coin_game(n,bal):
    for i in range(n):
        if random.choice(["H", "T"]) == "H":
            bal += 1
        else:
            bal = 1.0 / bal
    return bal

tot = 0
k = 1000000

for i in range(k):
    tot += coin_game(10,100)

print(tot/k)