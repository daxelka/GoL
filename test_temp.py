import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle

from GoL import GoL
import graph_tools as gt


A = np.array([[0,1,1,1,1],[1,0,1,0,0],[1,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]])
G = nx.from_numpy_matrix(A)

threshold_birth = 0.15
threshold_overpopulation = 0.85
threshold_starvation = 0.14

o = np.array([1,1,1,1,1])

game = GoL(G,threshold_birth, threshold_overpopulation, threshold_starvation)
o_loop = game.step_loops(o)
o_vector = game.step(o)

print(o_loop)
print(o_vector)