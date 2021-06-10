import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# import graph_tools

network_size  = 10
# Network selection
G = nx.watts_strogatz_graph(n=network_size, k=4, p=0.3) # p=1 -> all-to-all connectivity

# Opinion initial conditions
def randonly_seeded_opinion(number_opiniated, network_size):
    opiniated = np.ones((number_opiniated,), dtype=int)
    neutral = np.zeros((network_size - number_opiniated,), dtype=int)
    return np.random.permutation(np.concatenate((opiniated, neutral), axis=0))

number_opiniated = 3
opinion = randonly_seeded_opinion(number_opiniated, network_size)


def colors(o):
    result = []
    for item in o:
        if item == 1:
            result.append('red')
        else:
            result.append('blue')    
    return result

nx.draw(G, node_color = colors(opinion), with_labels=True, font_weight='bold')
plt.show()

A = nx.adjacency_matrix(G)

def step(A, o, threshold_1, threshold_2):
    # above threshold_min opinion formation
    alive_neighbours = A.dot(o)
    influence = 1 * np.all([alive_neighbours >= threshold_1, alive_neighbours < threshold_2], axis=0)
    opinion = np.maximum(o, influence)
    
    # above threshold_max opinion formation
    influence_negative = 1 * np.invert(alive_neighbours >= threshold_2)
    print(influence_negative)
    new_opinion = np.minimum(opinion, influence_negative)

    return new_opinion

threshold_1 = 2
threshold_2 = 4

number_steps = 3

def iteration(A, v, threshold_1, threshold_2, number_steps):
    for i in range(0,number_steps):
        v_new = step(A, v,threshold_1, threshold_2)
        v = v_new
        nx.draw(G, node_color = colors(v_new), with_labels=True, font_weight='bold')
        plt.show()
        
iteration(A, opinion, threshold_1, threshold_2, number_steps) 