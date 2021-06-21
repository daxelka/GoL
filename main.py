import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle

from GoL import GoL
import graph_tools as gt

# Game initialisation
# G = gt.graph_from_mtx("./raw_data/socfb-Simmons81.mtx")
G = nx.read_edgelist('./raw_data/facebook_combined.txt')
# Nework degree distribution
degrees, values, keys = gt.degree_dist(G)

# Nework statistics
avg_deg = float(2*G.number_of_edges()) / float(G.number_of_nodes())
print("Nodes: ", G.order())
print("Edges: ", G.size())
print("Average degree: ", avg_deg)
print(nx.average_shortest_path_length(G))

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

# # network_size  = 100
# # # G = nx.watts_strogatz_graph(n=network_size, k=17, p=0.5) # p=1 -> all-to-all connectivity
# # G = nx.erdos_renyi_graph(n=network_size, p=0.15)#
# # A = nx.adjacency_matrix(G)

# threshold_birth = 0.15
# threshold_overpopulation = 0.85
# threshold_starvation = 0.14

# game = GoL(G, threshold_birth, threshold_overpopulation, threshold_starvation)
# # print(game.degree())

# # Initial opinion distribution across network
# def randonly_seeded_opinion(number_opiniated, network_size):
#     opiniated = np.ones((number_opiniated,), dtype=int)
#     neutral = np.zeros((network_size - number_opiniated,), dtype=int)
#     return np.random.permutation(np.concatenate((opiniated, neutral), axis=0))

# number_opiniated = 20


# # Game iteration
# number_steps = 10

# #
# number_experiments = 1

# # File to save experiments resuls


# for i in range(number_experiments):
# 	# Initial condition chosen at random
# 	seed = randonly_seeded_opinion(number_opiniated, network_size)
# 	# Game iteration
# 	opinions = game.run(seed, number_steps)
# 	popularity = game.popularity(opinions)

# 	# Saving results
# 	filename = 'ER_DF_'+str(i)
# 	outfile = open(filename,'wb')
# 	np.savez(outfile, seed = seed, opinions=opinions, popularity = popularity)
# 	outfile.close()

# # plt.plot(range(opinions.shape[0]), popularity, 'r', marker = '.')


# # WSDF0 = np.load('ER_DF_0')
# # WSDF1 = np.load('ER_DF_1')
# # WSDF2 = np.load('ER_DF_2')



# # # unaffected = game.unaffected_dynamics(opinions)

# # plt.plot(range(WSDF0['opinions'].shape[0]), WSDF0['popularity'], 'bo')
# # plt.plot(range(WSDF1['opinions'].shape[0]), WSDF1['popularity'], 'ro')
# # plt.plot(range(WSDF2['opinions'].shape[0]), WSDF2['popularity'], 'go')
# # plt.show()

# # WSDF0.close()
# # WSDF1.close()
# # WSDF2.close()


# # # Animation
# # fig, ax = plt.subplots(figsize=(8,6))
# # plt.axis('off')

# # game.animation(fig, opinions)


