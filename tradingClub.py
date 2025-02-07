import numpy as np
import scipy.stats as stats

# Generate 4 random numbers from 1-100 inclusive
random_numbers = np.random.randint(1, 101, 4)

random_numbers = [17, 59, 79, 86, 47, 55, 64, 69]


# Print results
# print("Range:", range_val)
# print("Random Numbers:", random_numbers)
# print("Mean:", mean_value)
# print("Median:", median_value)
# print("Standard Deviation:", std_value)
# print("Interquartile Range (IQR):", iqr_value)

def money_earned(random_numbers):
    # generated = list(np.random.randint(1, 101, 2))
    # generated = [64, 100]
    # final = list(random_numbers) + generated
    final = np.random.randint(1, 101, 10)

    mean_value = np.mean(final)
    std_value = np.std(final, ddof=1)
    median_value = np.median(final)
    iqr_value = stats.iqr(final)
    range_val = max(final) - min(final)

    money = 0
    money -= (range_val - mean_value)
    money += (range_val - median_value)
    money += (range_val - iqr_value)
    money += (range_val - std_value)

    money = median_value
    return money

trials = []
for i in range(10000):
    trials.append(money_earned(random_numbers))

print(np.mean(trials))
print(np.std(trials))