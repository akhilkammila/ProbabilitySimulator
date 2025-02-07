import nashpy as nash
import numpy as np

kicker = [[3,0],[2,1]]
goalie = [[3, 2],[0, 1]]

game = nash.Game(kicker, goalie)

# Support enumeration
equilibria = game.support_enumeration()
for eq in equilibria:
    print(eq)

# # Support or vertex enumeration (all solutions)
# for res in game.vertex_enumeration():
#     x = res[0]
#     y = res[1]
#     print(x, y)

#     payoff1 = np.transpose(x) @ (A @ y)
#     payoff2 = np.transpose(x) @ (B @ y)
#     print(payoff1, payoff2)

# for i in range(4):
#     print(game.lemke_howson(initial_dropped_label=i))