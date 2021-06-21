
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle

from GoL import GoL
import graph_tools as gt

# Game initialisation
# G = gt.graph_from_mtx("./raw_data/socfb-Simmons81.mtx")
G = nx.read_edgelist('./raw_data/facebook_combined.txt')
print('create a graph')

# Nework degree distribution
# degrees, values, keys = gt.degree_dist(G)

# Nework statistics
avg_deg = float(2*G.number_of_edges()) / float(G.number_of_nodes())
print("Nodes: ", G.order())
print("Edges: ", G.size())
print("Average degree: ", avg_deg)


# Game initialisation
threshold_birth = 0.15
threshold_overpopulation = 0.85
threshold_starvation = 0.14

game = GoL(G, threshold_birth, threshold_overpopulation, threshold_starvation)
print('create a game')

# Initial opinion distribution across network
def randonly_seeded_opinion(number_opiniated, network_size):
    opiniated = np.ones((number_opiniated,), dtype=int)
    neutral = np.zeros((network_size - number_opiniated,), dtype=int)
    return np.random.permutation(np.concatenate((opiniated, neutral), axis=0))

number_opiniated = 400
network_size = G.number_of_nodes()


# Game iteration
number_steps = 5000

number_experiments = 20

# # File to save experiments resuls


for i in range(number_experiments):
	# Initial condition chosen at random
	A = nx.adjacency_matrix(G)
	seed = randonly_seeded_opinion(number_opiniated, network_size)
	# Game iteration
	opinions = game.run(seed, number_steps)
	popularity = game.popularity(opinions)

	# Saving results
	filename = 'FB_'+str(i)
	outfile = open(filename,'wb')
	np.savez(outfile, seed = seed, opinions=opinions, popularity = popularity, adj = A)
	outfile.close()

print('simulatioin completed')
plt.plot(range(opinions.shape[0]), popularity, 'r', marker = '.')
plt.show()

