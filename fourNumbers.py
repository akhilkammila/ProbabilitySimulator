import random

a = random.normalvariate(1000, 250)
b = 500 if random.random() > 0.5 else 1500
c = random.uniform(500, 1500)
d = 1000
print(a, b, c, d)