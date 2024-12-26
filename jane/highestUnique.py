"""
This problem not related to Jane, but just in this folder b/c it is jane arc rn
n (100) players. each chooses a number 1-n, highest unique number wins
"""

""" 
Solving strategy:

p100:
(1-p100)^99 = 1/100
by indifference, chances nobody chooses the val 100 should be 1/100

p99:
(1-p99)^99 * for 99 <= j <= 100 (1-pj(1-pj)^98) = 1/100
by indifference, winning by choosing 99 should have prob. 1/100
win if nobody chooses 99 & for all higher values, NOT exactly one person chose it

Note:
in reality (due to ties being a redo), it is (1-p100)^99 + p100^99 * (1/100)= 1/100
if the LHS is larger, then p100 must be greater to compensate by decreasing (1-p100) term
in reality, p100 is thus slightly higher

for other vals
in reality, nobody choosing our number would increase p-choosing other numbers
this would make chance that NOT exactly one person chose it go up (since probably more than 1 person chose)
so LHS is larger, and pval must be higher to compensate by decreasing (1-pval) term
in reality, pval would thus be higher

on conditional probability
we discussed how we should be doing p(0 people choose 99) * p(CONDITIONAL ON THAT, not 1 person chose 100)
but also, we should be doing p(0 choose 98) * p(COND, not 1 person chose 100)
    * p(COND on not 1 person choosing 100 as well, not 1 person chose 99)
unclear how this small conditionality affects prob.

so everything is a slight underestimate, and slightly more so for vals like 99
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def solveGame(n):
    not_losing=1 # the product of higher vals not being winning
    probs = [0]*n

    for val in range(n, 0, -1):
        p = 1 - math.pow(1/n/not_losing, 1/(n-1))
        probs[val-1] = p
        
        multiplier = 1-p*math.pow(1-p, n-2) * (n-1)
        not_losing *= multiplier
    return probs

n = 30
x = np.arange(1, n+1)
probs = solveGame(n)

sns.lineplot(x=x, y=probs)
plt.title(f"Nash Equilibrium for Highest Unique: {n} players")
plt.show()

print(np.sum(probs))