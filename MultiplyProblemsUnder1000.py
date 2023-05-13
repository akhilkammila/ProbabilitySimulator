"""
What is the percent of 2x2 digit multiplication problems which have a result < 1000?
Guess: 25%
"""

trials = 0
successful = 0
for i in range(20, 30):
    for j in range(10,100):
        if i*j < 1000: successful += 1
        trials += 1
print(successful)
print(trials)
print(successful/trials)