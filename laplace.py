import numpy as np

def check(n):
    x = np.random.laplace(loc=0, scale=1, size=n)
    y = np.random.laplace(loc=0, scale=1, size=n)
    res = x > y/2
    return np.count_nonzero(res==1)

sample = 100000
print(check(sample) / sample)