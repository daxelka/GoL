import numpy as np
from GoL import GoL

# Initial conditions
A = np.array([[0,1,1,1,1],[1,0,1,0,0],[1,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]])
v_ini = np.array([1,1,0,0,0])
threshold_1 = 2
threshold_2 = 3
number_steps = 5
# Results
v1 = np.array([1,1,1,0,0])
v2 = np.array([1,1,1,1,0])
v3 = np.array([0,1,0,1,1])
v4 = np.array([0,1,1,1,1])
v5 = np.array([0,1,1,1,1])

game = GoL(A)

v1_calc = game.step(A, v_ini, threshold_1, threshold_2)
v2_calc = game.step(A, v1, threshold_1, threshold_2)
v3_calc = game.step(A, v2, threshold_1, threshold_2)
v4_calc = game.step(A, v3, threshold_1, threshold_2)
v5_calc = game.step(A, v4, threshold_1, threshold_2)

print(v1 - v1_calc)
print(v2 - v2_calc)
print(v3 - v3_calc)
print(v4 - v4_calc)
print(v5 - v5_calc)