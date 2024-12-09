import numpy as np
from scipy.optimize import linprog

def solve_zero_sum_game(A):
    """
    Solve a two-player zero-sum game given a payoff matrix A for the row player.
    A is an m-by-n matrix:
        m = number of row strategies
        n = number of column strategies

    Returns:
        x: Optimal mixed strategy for the row player
        v: Value of the game
    """
    A = np.array(A)
    m, n = A.shape

    # Decision variables: x_1, ..., x_m, v
    # We will minimize -v, so c = [0,...,0,-1]
    c = np.zeros(m+1)
    c[-1] = -1  # Coefficient for v is -1 since we minimize -v

    # Equality constraint: sum_i x_i = 1
    A_eq = np.zeros((1, m+1))
    A_eq[0, :m] = 1
    b_eq = np.array([1])

    # Inequality constraints for each column:
    # sum_i A_ij x_i - v >= 0  --> -sum_i A_ij x_i + v <= 0
    # For each column j, we have:
    # (-A_1j, -A_2j, ..., -A_mj, 1)*[x_1,...,x_m,v]^T <= 0
    A_ub = np.zeros((n, m+1))
    b_ub = np.zeros(n)
    for j in range(n):
        A_ub[j, :m] = -A[:, j]
        A_ub[j, m] = 1
        # b_ub[j] = 0 by default

    # Bounds:
    # x_i >= 0
    # v >= 0 (assumption: if you know v could be negative, consider shifting A)
    bounds = [(0, None) for _ in range(m)] + [(0, None)]

    # Solve LP
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if not res.success:
        raise ValueError("No solution found. Try adjusting the payoff matrix or formulation.")

    # Extract solution
    v = res.x[-1]
    x = res.x[:-1]

    return x, v

# Example usage:
if __name__ == "__main__":
    # Example payoff matrix
    A = [
    [2, -1],  # Payoffs if the row player chooses strategy 1
    [1,  3],  # Payoffs if the row player chooses strategy 2
    [0, -2]   # Payoffs if the row player chooses strategy 3
    ]

    x_opt, v_opt = solve_zero_sum_game(A)
    print("Optimal mixed strategy for the row player:", x_opt)
    print("Value of the game:", v_opt)