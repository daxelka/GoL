import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from GoL import GoL
# import graph_tools

# Game initialisation
network_size  = 100
G = nx.watts_strogatz_graph(n=network_size, k=4, p=0.3) # p=1 -> all-to-all connectivity
A = nx.adjacency_matrix(G)
# print(type(A))
threshold_1 = 2
threshold_2 = 4

game = GoL(A, G, threshold_1, threshold_2)

# Initial opinion distribution across network
def randonly_seeded_opinion(number_opiniated, network_size):
    opiniated = np.ones((number_opiniated,), dtype=int)
    neutral = np.zeros((network_size - number_opiniated,), dtype=int)
    return np.random.permutation(np.concatenate((opiniated, neutral), axis=0))

number_opiniated = 20
seed = randonly_seeded_opinion(number_opiniated, network_size)

# Game iteration
number_steps = 5
opinions = game.run(seed, number_steps)
# print(opinions)

# Drawing results
game.draw_snapshoot(opinions[2,:])
game.draw_snapshoot(opinions[4,:])
 