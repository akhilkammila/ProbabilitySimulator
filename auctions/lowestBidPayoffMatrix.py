"""
Creates payoff matrix for lowest bid auction,
where payoff is x for a bid of x
in case of a tie, payoff is x/2

This program simply creates payoff matrixes to input into matrix solver
    https://cgi.csc.liv.ac.uk/~rahul/bimatrix_solver/
    still need to learn the actual theory behind the matrix solver
        is mixed strategy nash just doing system of equations on like n variables?? probably but check

Ex matrix for n=3: (symmetric)
0.5 1 1
0 1 2
0 0 1.5

if i < j, payoff is i
if i = j, payoff i/2
if i > j, payoff 0
"""

def printMatrix(n):
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            val = 0
            if i < j: val = i
            if i == j: val = i/2
            row.append(val)
        print(*row)

printMatrix(10)