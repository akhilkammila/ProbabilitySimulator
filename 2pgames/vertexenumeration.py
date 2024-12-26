import nashpy as nash
import numpy as np

A = [[2,3],[4,1]]
B = [[1,6],[11,2]]

game = nash.Game(A, B)

# Support or vertex enumeration (all solutions)
for res in game.vertex_enumeration():
    x = res[0]
    y = res[1]
    print(x, y)

    payoff1 = np.transpose(x) @ (A @ y)
    payoff2 = np.transpose(x) @ (B @ y)
    print(payoff1, payoff2)

for i in range(4):
    print(game.lemke_howson(initial_dropped_label=i))