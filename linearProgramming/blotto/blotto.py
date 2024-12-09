import numpy as np
from scipy.optimize import linprog
from math import comb

def solve_zero_sum_game(A):
    """
    Solve a two-player zero-sum game given a payoff matrix A for the row player.
    A is an m-by-n matrix:
        m = number of row strategies
        n = number of column strategies

    Returns:
        x: Optimal mixed strategy for the row player (length m)
        y: Optimal mixed strategy for the column player (length n)
        v: Value of the game
    """
    A = np.array(A)
    m, n = A.shape

    #------------------------------------------------------------
    # Solve from the row player's perspective (Primal)
    # Primal LP:
    # Maximize v
    # Subject to:
    # sum_i x_i = 1, x_i >= 0
    # For each column j: sum_i A_ij x_i >= v
    #
    # Convert to minimization of -v.
    # Decision variables order: x_1,...,x_m, v
    # We have: sum_i A_ij x_i - v >= 0 --> -sum_i A_ij x_i + v <= 0
    # Set up inequalities:
    c = np.zeros(m+1)
    c[-1] = -1  # minimize -v

    A_eq = np.zeros((1, m+1))
    A_eq[0, :m] = 1
    b_eq = np.array([1])

    A_ub = np.zeros((n, m+1))
    b_ub = np.zeros(n)
    for j in range(n):
        A_ub[j, :m] = -A[:, j]
        A_ub[j, m] = 1  # corresponding to v
        # b_ub[j] = 0

    bounds = [(0, None)]*m + [(0, None)]  # x_i >=0, v >=0
    
    res_row = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    if not res_row.success:
        raise ValueError("No solution found from the row player's perspective.")

    v = res_row.x[-1]
    x = res_row.x[:-1]

    #------------------------------------------------------------
    # Solve from the column player's perspective (Dual)
    # Dual LP:
    # Minimize w
    # Subject to:
    # sum_j y_j = 1, y_j >= 0
    # For each row i: sum_j A_ij y_j <= w
    #
    # Decision variables: y_1,...,y_n, w
    # Inequalities: sum_j A_ij y_j - w <= 0 --> sum_j A_ij y_j <= w
    # We'll solve directly for y and w.

    c_dual = np.zeros(n+1)
    c_dual[-1] = 1  # minimize w

    A_eq_dual = np.zeros((1, n+1))
    A_eq_dual[0, :n] = 1
    b_eq_dual = np.array([1])

    A_ub_dual = np.zeros((m, n+1))
    b_ub_dual = np.zeros(m)
    for i in range(m):
        A_ub_dual[i, :n] = A[i, :]
        A_ub_dual[i, n] = -1  # sum_j A_ij y_j - w <= 0

    bounds_dual = [(0, None)]*n + [(0, None)] # y_j >=0, w>=0
    res_col = linprog(c_dual, A_ub=A_ub_dual, b_ub=b_ub_dual, A_eq=A_eq_dual, b_eq=b_eq_dual, bounds=bounds_dual, method='highs')
    if not res_col.success:
        raise ValueError("No solution found from the column player's perspective.")

    w = res_col.x[-1]
    y = res_col.x[:-1]

    #------------------------------------------------------------
    # Check consistency:
    # For a zero-sum game, v (from the row's problem) should equal w (from the column's problem).
    # Small numerical discrepancies can happen, but they should be close.
    if not np.isclose(v, w, atol=1e-7):
        print("Warning: Row player's value and column player's value differ. Possibly due to numerical issues.")

    # v (or w) is the value of the game.
    return x, y, v

def generate_distributions(N, M):
    """
    Generate all possible distributions of N identical soldiers into M armies.
    Each distribution is an M-dimensional vector of nonnegative integers summing to N.
    """
    # This can be done using a recursive generator or an iterative approach.
    # A classic approach is to use "stars and bars" logic.
    # We'll generate combinations that represent the dividers positions.
    
    # Number of solutions to x_1 + x_2 + ... + x_M = N is C(N+M-1, M-1)
    # We'll generate them lexicographically.
    
    # One approach: we can use a recursive generator:
    def backtrack(remaining, slots):
        if slots == 1:
            yield [remaining]
        else:
            for i in range(remaining + 1):
                for rest in backtrack(remaining - i, slots - 1):
                    yield [i] + rest

    return list(backtrack(N, M))

def build_payoff_matrix(N, M):
    """
    Build the payoff matrix for a Blotto game with N soldiers and M armies.
    Rows correspond to row player's strategies, columns to column player's strategies.
    Payoff is from the row player's perspective.
    """
    row_strategies = generate_distributions(N, M)
    col_strategies = generate_distributions(N, M)

    R = len(row_strategies)
    C = len(col_strategies)

    A = np.zeros((R, C))

    # Compute payoff for each pair of strategies
    for i, x in enumerate(row_strategies):
        for j, y in enumerate(col_strategies):
            # Compare allocations battlefield by battlefield
            payoff = 0
            for xi, yi in zip(x, y):
                if xi > yi:
                    payoff += 1
                elif xi < yi:
                    payoff -= 1
                else:
                    payoff += 0
            A[i, j] = payoff

    return A, row_strategies, col_strategies

if __name__ == "__main__":
    # Example: small numbers due to combinational explosion
    N = 5  # soldiers
    M = 3  # armies
    A, row_strats, col_strats = build_payoff_matrix(N, M)
    x_opt, y_opt, v_opt = solve_zero_sum_game(A)
    # print("Payoff matrix shape:", A.shape)
    # print("Payoff matrix A:\n", A)

    print("Optimal strategy for row player (x):")
    for strat, prob in zip(row_strats, x_opt):
        if prob != 0: print(strat, prob)

    print("Optimal strategy for column player (y):")
    for strat, prob in zip(col_strats, y_opt):
        if prob != 0: print(strat, prob)

