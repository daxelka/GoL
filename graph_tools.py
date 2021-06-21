import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Degree Distribution
def degree_dist(G):
    # Degrees list
    degrees = [G.degree(n) for n in G.nodes()]
    
    # Degree distribution
    degree_counts = Counter(degrees)
    keys = sorted(degree_counts.keys())
    
    values = [degree_counts[k] for k in keys]
    
    # Dergee distribution normalised
    # values = [float(i) / sum(values) for i in values]
    return degrees, values, keys

# Plotting information spreading on networks
def visualise_simulations(G, positions, iterations):
    color_map = []
    for iteration in range(G.number_of_nodes()):
        color_map.append('green')

    for iteration in iterations:
        for index, status in iteration['status'].items():
            if status == 1:
                color_map[index] = 'red'
            if status == 2:
                color_map[index] = 'grey'

        nx.draw(G, positions, node_color = color_map, with_labels = True)
        plt.show()

def nodes_sorter(opinions):
    rating = np.sum(opinions[-10:-1,:], axis =0)*(-1)
    opinions_with_rating = np.vstack([opinions,rating])
    opinions_sorted = opinions_with_rating[ :, opinions_with_rating[-1].argsort()]
    opinions_final = opinions_sorted[0:-2,:]
    permutation_rule = opinions_sorted[-1,:]
    return opinions_final, permutation_rule

def graph_from_mtx(filename):
    with open(filename) as f:
        f_links = f.read().splitlines() 

    node_list_1 = []
    node_list_2 = []

    for i in f_links[2:]:
        node_list_1.append(i.split(' ')[1])
        node_list_2.append(i.split(' ')[0])

    f_df = pd.DataFrame({'Node_1': node_list_1, 'Node_2': node_list_2})

    G = nx.from_pandas_edgelist(f_df, "Node_1", "Node_2")

    node_list = node_list_1 + node_list_2
    node_list = list(dict.fromkeys(node_list))
    adj_G = nx.to_numpy_matrix(G, nodelist = node_list)
    return G
