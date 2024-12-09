"""
not really probability sim, just a quick chi^2 test on:
https://www.reddit.com/r/poker/comments/swdt77/zone_poker_on_ignition_posted_blinds_issue/

chi^2 statistic: 19.88
df = 5, p=5% --> 11.07 (1% is 15.09)
"""

observed = [4027, 3819, 3655, 3885, 3913, 3907]
avg = sum(observed)/6

statistic = 0
for i, num in enumerate(observed):
    top = (num - avg)**2
    statistic += (num-avg)**2 / avg
print(statistic)

observed = [observed[0], observed[1], sum(observed[2:])]
expected = [avg, avg, avg*4]

statistic = 0
for i, num in enumerate(observed):
    top = (num - expected[i])**2
    statistic += (num-expected[i])**2 / expected[i]
print(observed, expected)
print(statistic)