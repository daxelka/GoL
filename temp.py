import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from GoL import GoL

# Game initialisation
# network_size  = 10
# G = nx.watts_strogatz_graph(n=network_size, k=5, p=0.3) # p=1 -> all-to-all connectivity
# A = nx.adjacency_matrix(G)
# # print(type(A))
# threshold_1 = 0.3
# threshold_2 = 0.7

# game = GoL(G, threshold_1, threshold_2)
# result = game.step(np.ones((A.shape[0]), dtype = int))

# print(result)

# Some random array of 1's and 0's
# x = np.random.randint(0,2, size=(3, 5))
# print(x)
# print(x[0:2,:])
# # Find where all values in the columns are zero
# mask = (x == 0).all(0)
# print(mask)
# # Find the indices of these columns
# column_indices = np.where(mask)[0]
# print(column_indices)
# # Update x to only include the columns where non-zero values occur.
# x = x[:,~mask]
# # print(x)

network_size  = 5
G = nx.watts_strogatz_graph(n=network_size, k=3, p=0.5) # p=1 -> all-to-all connectivity
A = nx.adjacency_matrix(G)
nx.draw_circular(G)
plt.show()

# print(type(A))
threshold_birth = 0.4
threshold_overpopulation = 0.7
threshold_starvation = 0.2

game = GoL(G, threshold_birth, threshold_overpopulation, threshold_starvation)
opinions =np.array([[0,1,1,1,1],[0,0,1,0,0]])
# opinions =np.array([[0,1,1,1,1],[1,0,1,0,0],[1,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]])
# print(opinions)
# print(game.unaffected_nodes(opinions))
