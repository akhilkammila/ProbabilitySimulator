import nashpy as nash
import numpy as np
from itertools import permutations
import time
import math
import pandas as pd

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
    t1 = time.time()
    data = [(original_list, list(perm)) for original_list in col_strategies for perm in set(permutations(original_list))]
    permutation_df =  pd.DataFrame(data, columns=["Original List", "Permutation"])
    row_df = pd.DataFrame({'Row List': col_strategies})

    max_len = max(len(lst) for lst in permutation_df["Original List"])
    for i in range(max_len):
        permutation_df[f"Permutation_{i}"] = permutation_df["Permutation"].apply(lambda x: x[i] if i < len(x) else np.nan)
        row_df[f"Row_{i}"] = row_df["Row List"].apply(lambda x: x[i] if i < len(x) else np.nan)

    perm_cols = [f"Permutation_{i}" for i in range(max_len)]
    row_cols = [f"Row_{i}" for i in range(max_len)]
    t2 = time.time()

    t3 = time.time()
    combinations_df = pd.merge(permutation_df, row_df, how='cross')
    t4 = time.time()

    combinations_df['num_win'] = ((combinations_df[perm_cols].values - combinations_df[row_cols].values) > 0).sum(axis=1)
    combinations_df['num_lost'] = ((combinations_df[perm_cols].values - combinations_df[row_cols].values) < 0).sum(axis=1)
    combinations_df['result'] = combinations_df['num_win'] - combinations_df['num_lost']

    t5 = time.time()
    final_result = combinations_df.groupby(['Original List', 'Row List'])['result'].mean()
    final_result = final_result.unstack()
    t6 = time.time()

    print("1 part build:", t2 - t1)
    print("2 part build:", t4 - t3)
    print("3 part build:", t5 - t4)
    print("4 part build:", t6 - t5)
    return final_result

def timeRun(N, M):
    # Building matrix
    build_start = time.time()
    strategies = generate_unique_distributions(N, M)
    A = build_payoff_matrix(strategies, strategies)
    build_end = time.time()

    solve_start = time.time()
    game = nash.Game(A)
    p1, p2 = game.linear_program()
    solve_end = time.time()

    print("# strategies:", len(strategies))
    print("N (basic):", math.comb(N+M-1, M-1))
    print("N (actual):", A.shape)
    print("Matrix creation:", build_end - build_start)
    print("Solving:", solve_end - solve_start)

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
    # print("-"*20)


timeRun(150, 3)