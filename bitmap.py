import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from GoL import GoL
import graph_tools

# data = np.load('./results/ER_DF/LIC/ER_DF_16')
# data = np.load('./results/GoL/WS_bitmap_seed0p3/i28')
# data = np.load('./results/GoL/WS_bitmap_k0p5_seed0p2/i19')
# data = np.load('./results/GoL/WS_bitmap_k0p5_seed0p2/i22')
# data = np.load('./results/GoL/WS_bitmap_k0p5_seed0p2/i35')
# data = np.load('./results/GoL/WS_bitmap_seed0p25/i11')


opinions_final, permutation_rule = graph_tools.nodes_sorter(data['opinions'])
# print(permutation_rule)

fig, ax = plt.subplots()
plt.imshow(np.transpose(opinions_final))
# ticks = range(0,150,20)
# ax.set_xticks(ticks)
plt.xlabel("time",  fontsize=14)
plt.ylabel("node",  fontsize=14)
plt.show()

# fig, ax = plt.subplots()
# plt.plot(range(data['opinions'].shape[0]), data['popularity'], color="blue", alpha=0.5, marker = '.', linewidth=0.5)
# ticks = range(0,201,20)
# ax.set_xticks(ticks)
# plt.xlabel("time",  fontsize=14)
# plt.ylabel("popularity",  fontsize=14)
# plt.show()

data.close()
