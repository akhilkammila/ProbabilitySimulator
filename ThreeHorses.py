"""
Horse A beats Horse B 60% of the time
Horse B beats Horse C 70% of the time
What percent of the time will horse a beat horse c?
"""
import numpy as np
from scipy.stats import norm

def jane_street_horses():
    samples = 100000
    a = np.random.normal(0.2533*np.sqrt(2), 1, size=samples)
    b = np.random.normal(0, 1, size=samples)
    c = np.random.normal(-0.5244*np.sqrt(2), 1, size=samples)

    print(np.count_nonzero(a >= b)/samples)
    print(np.count_nonzero(b >= c)/samples)
    print(np.count_nonzero(a >= c)/samples)

"""
More generally,
Horse A beats Horse B X% of the time
Horse B beats Horse C Y% of the time
What percent of the time does Horse A beat C?
"""
def generalized_horses(X, Y, aVar=1, bVar=1, cVar=1):
    samples = 1000000
    dif1 = norm.ppf(X, scale=np.sqrt(aVar + bVar))
    dif2 = norm.ppf(Y, scale=np.sqrt(bVar + cVar))
    a = np.random.normal(dif1, np.sqrt(aVar), size=samples)
    b = np.random.normal(0, np.sqrt(bVar), size=samples)
    c = np.random.normal(-dif2, np.sqrt(cVar), size=samples)
    print(np.count_nonzero(a >= b)/samples)
    print(np.count_nonzero(b >= c)/samples)
    print(np.count_nonzero(a >= c)/samples)

generalized_horses(0.6, 0.6, 100000000, 1, 10000000)