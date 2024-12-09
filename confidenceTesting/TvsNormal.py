"""
https://stats.stackexchange.com/questions/626807/shouldnt-we-consider-the-difference-in-variance-between-population-and-a-sample

Say we are constructing a confidence interval for sample mean
    - we don't know the population variance
    - we should use t-distribution, but so many places say just use normal
    - let's see the difference

Findings:
    - using real var(1) for normal confidence interval is correct, but
    - using wrong var (sample var) is wrong (~94.5% depending on n)
    - as n increases, t-distribution approximates normal better, so it gets closer

    - t dist. is correct
    - sometimes a bit off for low n why? wasnt diving by N-1 in variance, oops
"""

import numpy as np
import math
from scipy.stats import t

# P1: see what % of the time 95% confidence intervals contain true mean

def getSample(n):
    sample = np.random.normal(0, 1, n) #size n sample
    mean = np.mean(sample)
    var = np.var(sample, ddof=1)

    return mean, var

def normalConfidenceInterval():
    n = 100
    
    mean, var = getSample(n)
    width = 1.959964*math.sqrt(1) / math.sqrt(n) #using real var(1) instead of var is more accurate
    confidenceInterval = (mean - width, mean + width)

    return confidenceInterval[0] <= 0 <= confidenceInterval[1]

def tConfidenceInterval():
    n = 10
    t_statistic = t.ppf(q= 1 - 0.05 / 2, df=n-1)

    mean, var = getSample(n)
    width = t_statistic*math.sqrt(var/n)
    confidenceInterval = (mean - width, mean + width)

    return confidenceInterval[0] <= 0 <= confidenceInterval[1]

if __name__ == "__main__":
    trials = 100000
    successes = 0
    for i in range(trials):
        # successes += normalConfidenceInterval()
        successes += tConfidenceInterval()

    # n= 100
    # normal result: 946,158 / 1 mil (94.61%)
    # t result: 948944 (94.9%)

    #n = 1000
    # normal result: 94,889/100,000
    # t result: 95,147
    print(successes)