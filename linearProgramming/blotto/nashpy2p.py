import nashpy as nash
import numpy as np
from itertools import permutations
from sage.games import Game

def generate_unique_distributions(N, M):
    """
    Generate all unique distributions of N identical soldiers into M armies,
    treating distributions that are permutations of each other as identical.
    Each distribution is sorted in non-decreasing order.
    """
    def backtrack(remaining, slots, current):
        if slots == 1:
            yield current + [remaining]
        else:
            for i in range(remaining + 1):
                yield from backtrack(remaining - i, slots - 1, current + [i])

    unique_distributions = set()
    for dist in backtrack(N, M, []):
        sorted_dist = tuple(sorted(dist))
        unique_distributions.add(sorted_dist)
    return sorted(unique_distributions)

def build_payoff_matrix(row_strategies, col_strategies):
    """
    Build the payoff matrix for the Blotto game.
    Payoff is from the row player's perspective and averaged over all permutations
    of the column player's strategy.
    """
    A = np.zeros((len(row_strategies), len(col_strategies)))

    # Precompute all unique permutations for each column strategy
    permutation_cache = {}
    for strategy in col_strategies:
        if strategy not in permutation_cache:
            permutation_cache[strategy] = list(permutations(strategy))
    
    # Compute average payoff for each pair of unique strategies
    for i, row_strategy in enumerate(row_strategies):
        for j, col_strategy in enumerate(col_strategies):
            perms_y = permutation_cache[col_strategy]
            total_payoff = 0
            for perm_y in perms_y:
                payoff = sum(
                    1 if xi > yi else -1 if xi < yi else 0
                    for xi, yi in zip(row_strategy, perm_y)
                )
                total_payoff += payoff
            average_payoff = total_payoff / len(perms_y)
            A[i, j] = average_payoff

    return A

if __name__ == "__main__":
    N = 5
    M = 3

    strategies = generate_unique_distributions(N, M)
    A = build_payoff_matrix(strategies, strategies)

    game = Game(A, -A)
    equilibria = game.lemke_howson()


    # game = nash.Game(A, -A)
    # p1, p2 = game.lemke_howson(0)

    # print("Row player:")
    # for strat, prob in zip(strategies, p1):
    #     if prob > 0:
    #         print(strat, np.round(prob, decimals=4))

    # print("Col player:")
    # for strat, prob in zip(strategies, p2):
    #     if prob > 0:
    #         print(strat, np.round(prob, decimals=4))

    # value = game[p1, p2]
    # print("EVs:", value)