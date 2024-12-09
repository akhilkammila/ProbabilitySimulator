from scipy.optimize import linprog

c = [-1.2, -1.7]
A = [[1,0],[0,1],[1,1]]
b = [3000, 4000, 5000]

res = linprog(c=c, A_ub=A, b_ub=b)
print(res)