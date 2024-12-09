from scipy.optimize import linprog

# Coefficients for the objective function: we are minimizing, so negate the coefficients
# of the original maximization problem.
c = [-1.2, -1.7, 0, 0, 0]

# Equality constraint matrices
# A_eq * [x1, x2, s1, s2, s3]^T = b_eq
A_eq = [
    [1,   0,   1,   0,   0],  # x1 + s1 = 3000
    [0,   1,   0,   1,   0],  # x2 + s2 = 4000
    [1,   1,   0,   0,   1]   # x1 + x2 + s3 = 5000
]

b_eq = [3000, 4000, 5000]

# Variable bounds: (0, None) means x >= 0
bounds = [(0, None),  # x1 >= 0
          (0, None),  # x2 >= 0
          (0, None),  # s1 >= 0
          (0, None),  # s2 >= 0
          (0, None)]  # s3 >= 0

# Solve the linear program
res = linprog(c, A_eq=A_eq, b_eq=b_eq, method='highs')

# Since we minimized the negative, the maximum value of the original objective is -res.fun
if res.success:
    print("Optimal solution found.")
    print(f"x1 = {res.x[0]:.2f}")
    print(f"x2 = {res.x[1]:.2f}")
    print(f"s1 = {res.x[2]:.2f}")
    print(f"s2 = {res.x[3]:.2f}")
    print(f"s3 = {res.x[4]:.2f}")
    print(f"Maximum Objective Value = {-res.fun:.2f}")
else:
    print("No optimal solution found.")
