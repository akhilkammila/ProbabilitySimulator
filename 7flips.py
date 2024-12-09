""" 
Start with $100
7 coin flips
H is +1, T is invert

EV of value at the end?
"""

import random

def sim():
    start = 100
    for i in range(7):
        if random.random() > 0.5: start += 1
        else: start = 1/start
    
    return start

trials = 10000
answ = 0
for i in range(trials):
    answ += sim()

print(answ/trials)