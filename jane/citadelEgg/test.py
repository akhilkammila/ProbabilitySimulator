import numpy as np

opponent_action = np.array([1,2,3,4,5,5,6])
my_action = 5

print(opponent_action == my_action)

countSame = np.count_nonzero(opponent_action == my_action)
print(countSame)