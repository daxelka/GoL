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
data = np.load('./results/GoL/WS_k16_seed0p15/i4')
# data = np.load('./results/GoL/WS_k16_seed0p15_v2/i0')

# plt.scatter(range(data['opinions'].shape[0]), data['popularity'], color="blue", alpha=0.5, marker = '.')
fig, ax = plt.subplots()
plt.plot(range(data['opinions'].shape[0]), data['popularity'], color="brown", alpha=1, marker = '.', linewidth=0.5)
# ticks = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# ax.set_yticks(ticks)
ax.set_ylim(0,1)
plt.xlabel("time",  fontsize=12)
plt.ylabel("popularity",  fontsize=12)
plt.show()

data.close()

# color="darkslateblue"
# color="mediumvioletred"
