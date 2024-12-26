import numpy as np
from scipy.optimize import linprog

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
    c = np.zeros(shape=(m + 1))
    c[-1] = -1

    A_eq = np.zeros((1, m+1))
    A_eq[0, :m] = 1
    b_eq = 1

    A_ub = np.hstack(
        (-A.T, np.ones(shape=(n, 1)))
    )
    b_ub = np.zeros(n)

    bounds = [(0, None)]*m + [(None, None)]  # x_i >=0, v >=0
    
    res_row = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if not res_row.success:
        raise ValueError("No solution found from the row player's perspective.")

    v = res_row.x[-1]
    x = res_row.x[:-1]
    return x, v

def sample_testcase():
    # Example: non-square matrix
    A = [
        [2, -1],
        [1,  3],
        [0, 4]
    ]
    A = -np.transpose(A)
    x_opt, v_opt = solve_zero_sum_game(A)
    print("Row player's optimal mixed strategy (x):", x_opt)
    # print("Column player's optimal mixed strategy (y):", y_opt)
    print("Value of the game:", v_opt)

sample_testcase()