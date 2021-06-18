import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from GoL import GoL

# Game initialisation
network_size  = 100
G = nx.watts_strogatz_graph(n=network_size, k=17, p=0.5) # p=1 -> all-to-all connectivity
# G = nx.erdos_renyi_graph(n=network_size, p=0.15)# 
A = nx.adjacency_matrix(G)
# print(type(A))
threshold_birth = 0.33
threshold_overpopulation = 0.85
threshold_starvation = 0

game = GoL(G, threshold_birth, threshold_overpopulation, threshold_starvation)
print(game.degree())

# Initial opinion distribution across network
def randonly_seeded_opinion(number_opiniated, network_size):
    opiniated = np.ones((number_opiniated,), dtype=int)
    neutral = np.zeros((network_size - number_opiniated,), dtype=int)
    return np.random.permutation(np.concatenate((opiniated, neutral), axis=0))

number_opiniated = 20
seed = randonly_seeded_opinion(number_opiniated, network_size)

# Game iteration
number_steps = 150
opinions = game.run(seed, number_steps)

popularity = game.popularity(opinions)
# print(popularity)

unaffected = game.unaffected_dynamics(opinions)


plt.plot(range(opinions.shape[0]), popularity, marker = '.')
plt.show()


# # Animation
# fig, ax = plt.subplots(figsize=(8,6))
# plt.axis('off')

# game.animation(fig, opinions)


