"""
Problem from green book, page 126
Calculating the answer with matrices
"""

import numpy as np

initial_state = np.array([15,16,17,18,19])
transition_matrix = np.array([[1/6,1,0,0,0],[1/6,0,1,0,0],[1/6,0,0,1,0],[1/6,0,0,0,1],[1/6,0,0,0,0]])

print(np.dot(initial_state, np.linalg.matrix_power(transition_matrix,15)))