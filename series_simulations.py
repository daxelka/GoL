import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle

from GoL import GoL
import graph_tools as gt

network_size  = 100
p_param = 0.5
G = nx.watts_strogatz_graph(n=network_size, k=17, p=p_param) # p=1 -> all-to-all connectivity

# Nework degree distribution
degrees, values, keys = gt.degree_dist(G)

# Nework statistics
avg_deg = float(2*G.number_of_edges()) / float(G.number_of_nodes())
print("Nodes: ", G.number_of_nodes())
print("Edges: ", G.number_of_edges())
print("Average degree: ", avg_deg)

threshold_birth = 0.25
threshold_overpopulation = 0.85
threshold_starvation = 0.15

game = GoL(G, threshold_birth, threshold_overpopulation, threshold_starvation)
A = nx.adjacency_matrix(G)

# Saving game details
filename = './results/GoL/WS_bitmap_k0p5_seed0p2/game_details'
outfile = open(filename,'wb')
np.savez(outfile, adj = A.toarray(), avg_degree = avg_deg, p = p_param, threshold_birth = threshold_birth , threshold_overpopulation = threshold_overpopulation, threshold_starvation = threshold_starvation)
outfile.close()


# Initial opinion distribution across network
def randonly_seeded_opinion(number_opiniated, network_size):
    opiniated = np.ones((number_opiniated,), dtype=int)
    neutral = np.zeros((network_size - number_opiniated,), dtype=int)
    return np.random.permutation(np.concatenate((opiniated, neutral), axis=0))

number_opiniated = int(0.2 * network_size)
number_steps = 200
number_iterations = 40

for i in range(number_iterations):

    # Initial condition chosen at random
    seed = randonly_seeded_opinion(number_opiniated, network_size)
    # Game iteration
    opinions = game.run(seed, number_steps)
    popularity = game.popularity(opinions)

    # Saving results
    filename = './results/GoL/WS_bitmap_k0p5_seed0p2/i'+str(i)
    outfile = open(filename,'wb')
    np.savez(outfile, seed = seed, opinions=opinions, popularity = popularity, adj = A)
    outfile.close()

# Reading results
# game_test = np.load('game_test')
# print(game_test['adj'].shape[0])
# game_test.close()

# plt.plot(range(opinions.shape[0]), popularity, 'r', marker = '.')
# plt.show()


