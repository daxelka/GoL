import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle

from GoL import GoL
import graph_tools as gt

# Game initialisation
# G = gt.graph_from_mtx("./raw_data/socfb-Simmons81.mtx")
# G = nx.read_edgelist('./raw_data/facebook_combined.txt')


# Plot degree distribution
# histogram
# plt.subplot(121)
# plt.hist(degrees)
# plt.ylabel("Count")
# plt.xlabel("Degree")

# # Frequency
# plt.subplot(122)
# plt.loglog(keys, values, 'ro-')
# plt.xlabel('Degree')
# plt.ylabel('Frequency')
# plt.grid(True)

# plt.show()

network_size  = 10000
print('creating network...')
G = nx.watts_strogatz_graph(n=network_size, k=17, p=0.7) # p=1 -> all-to-all connectivity
# G = nx.erdos_renyi_graph(n=network_size, p=0.15)#
# A = nx.adjacency_matrix(G)
print('network created')

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

print('initialising game...')
game = GoL(G, threshold_birth, threshold_overpopulation, threshold_starvation)
# # print(game.degree())
print('game initialised')

# Initial opinion distribution across network
def randonly_seeded_opinion(number_opiniated, network_size):
    opiniated = np.ones((number_opiniated,), dtype=int)
    neutral = np.zeros((network_size - number_opiniated,), dtype=int)
    return np.random.permutation(np.concatenate((opiniated, neutral), axis=0))

number_opiniated = int(0.1 * network_size)

# Initial condition chosen at random
print('seeding model...')
seed = randonly_seeded_opinion(number_opiniated, network_size)
print('model seeded')
# Game iteration
number_steps = 4000

print('running simulation...')
opinions = game.run(seed, number_steps)
print('simulation finished')
popularity = game.popularity(opinions)


plt.plot(range(opinions.shape[0]), popularity, 'r', marker = '.')
plt.show()

# # # Animation
# # fig, ax = plt.subplots(figsize=(8,6))
# # plt.axis('off')

# # game.animation(fig, opinions)


