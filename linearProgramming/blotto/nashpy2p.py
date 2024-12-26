import nashpy as nash
import numpy as np
from itertools import permutations

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

def build_payoff_matrix(N, M, row_strategies, col_strategies):
    """
    Build the payoff matrix for the Blotto game.
    Payoff is from the row player's perspective and averaged over all permutations
    of the column player's strategy.
    """
    A = np.zeros((len(row_strategies), len(col_strategies)))

    # Precompute all unique permutations for each column strategy
    permutation_cache = {}
    for j, y in enumerate(col_strategies):
        if y not in permutation_cache:
            permutation_cache[y] = list(set(permutations(y)))
    
    # Compute average payoff for each pair of unique strategies
    for i, x in enumerate(row_strategies):
        for j, y in enumerate(col_strategies):
            perms_y = permutation_cache[y]
            total_payoff = 0
            for perm_y in perms_y:
                payoff = sum(
                    1 if xi > yi else -1 if xi < yi else 0
                    for xi, yi in zip(x, perm_y)
                )
                total_payoff += payoff
            average_payoff = total_payoff / len(perms_y)
            A[i, j] = average_payoff

    return A

if __name__ == "__main__":
    N = 10
    M = 3

    row_strats = generate_unique_distributions(N, M)
    col_strats = generate_unique_distributions(N, M)
    A = build_payoff_matrix(N, M, row_strats, col_strats)

    # A = [
    # [2, -1],  # Payoffs if the row player chooses strategy 1
    # [1,  3],  # Payoffs if the row player chooses strategy 2
    # [0, 5]   # Payoffs if the row player chooses strategy 3
    # ]
    # game = nash.Game(-np.transpose(A))
    # equilibrium = game.vertex_enumeration()
    # for eq in equilibrium:
    #     print(eq)




    game = nash.Game(A)
    p1, p2 = game.lemke_howson_enumeration()

    print("Row player:")
    for strat, prob in zip(row_strats, p1):
        if prob > 0:
            print(strat, prob)

    print("Col player:")
    for strat, prob in zip(col_strats, p2):
        if prob > 0:
            print(strat, prob)

    value = game[p1, p2]
    best_response = game.is_best_response(p1, p2)
    print("Val, best response:")
    print(value, best_response)
    