"""
Just testing sample var = p(1-p)
and sample dist var = p(1-p)/N

Note that i didnt do ddof = 1, so stuff is off (too lazy to fix)
"""

import numpy as np

def generateSample(p, n):
    choices = [0, 1]
    probs = [1-p, p]
    return np.random.choice(choices, size=n, p=probs)

# Test variance
for n in [1, 4, 9, 25, 100, 10000]:
    sample = generateSample(0.6, n)
    print(f"N: {n}, variance: {np.var(sample)}")

"""
Output: variance = p(1-p)
N: 1, variance: 0.0
N: 4, variance: 0.25
N: 9, variance: 0.2222222222222222
N: 25, variance: 0.24960000000000004
N: 100, variance: 0.24189999999999998
N: 10000, variance: 0.24149916
"""

# Test sampling dist. variance (fixed 10000 samples)
for n in [1, 4, 9, 25, 100, 10000]:
    samples = [np.mean(sample) for sample in [generateSample(0.6, n) for _ in range(10000)]]
    print(f"N samples: {n}, variance: {np.var(samples)}")

"""
Output: variance = p(1-p)/N
N samples: 1, variance: 0.24182784000000002
N samples: 4, variance: 0.059160049375
N samples: 9, variance: 0.02613622111111111
N samples: 25, variance: 0.009591649903999999
N samples: 100, variance: 0.0023367802309999996
N samples: 10000, variance: 2.370621379509999e-05
"""