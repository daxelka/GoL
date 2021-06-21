import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from GoL import GoL
import graph_tools

# WSDF1 = np.load('./results/ER_DF/LIC/ER_DF_16')
WSDF1 = np.load('FB_0')

opinions_final, permutation_rule = graph_tools.nodes_sorter(WSDF1['opinions'])
print(permutation_rule)

plt.imshow(np.transpose(opinions_final))
plt.show()

print(WSDF1['opinions'][-10:-1,-10:-1])

WSDF1.close()
