import numpy as np
import networkx as nx
from GoL import GoL

# Initial conditions
A = np.array([[0,1,1,1,1],[1,0,1,0,0],[1,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]])
G = nx.from_numpy_matrix(A)

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

game = GoL(A, G, threshold_1, threshold_2)

v1_calc = game.step(v_ini)
v2_calc = game.step(v1)
v3_calc = game.step(v2)
v4_calc = game.step(v3)
v5_calc = game.step(v4)

# print(v1 - v1_calc)
# print(v2 - v2_calc)
# print(v3 - v3_calc)
# print(v4 - v4_calc)
# print(v5 - v5_calc)

opinions = game.run(v_ini, 4)
print(opinions)
print(v_ini)
print(v1)
print(v2)
print(v3)

game.draw_snapshoot(v1)
