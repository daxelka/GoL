import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from GoL import GoL

# Game initialisation
network_size  = 10
G = nx.watts_strogatz_graph(n=network_size, k=5, p=0.3) # p=1 -> all-to-all connectivity
A = nx.adjacency_matrix(G)
# print(type(A))
threshold_1 = 0.3
threshold_2 = 0.7

game = GoL(G, threshold_1, threshold_2)
result = game.step(np.ones((A.shape[0]), dtype = int))

print(result)

