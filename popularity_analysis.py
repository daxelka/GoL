import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from GoL import GoL

# number_experiments = 20
# for i in range(number_experiments):
#   filename = 'WS_DF_'+str(i)
#   infile = open(filenaactactaaame,'rb')
#   new_dict = pickle.load(infile)
#   infile.close()


WSDF0 = np.load('FB_18')
WSDF1 = np.load('FB_19')
WSDF2 = np.load('FB_17')

plt.plot(range(WSDF0['opinions'].shape[0]), WSDF0['popularity'], marker='o', color="blue", alpha=0.3)
plt.plot(range(WSDF1['opinions'].shape[0]), WSDF1['popularity'], marker='o', color="orange", alpha=0.3)
plt.plot(range(WSDF2['opinions'].shape[0]), WSDF2['popularity'], marker='o', color="green", alpha=0.3)

plt.show()

WSDF0.close()
WSDF1.close()
WSDF2.close()

# WSDF1 = np.load('FB_0')
# rating = np.sum(WSDF1['opinions'][-10:-1,:], axis =0)*(-1)
# opinions_with_rating = np.vstack([WSDF1['opinions'],rating])
# opinions_sorted = opinions_with_rating [ :, opinions_with_rating[-1].argsort()]
# # print(opinions_sorted[-1,:])
# # print(rating)


# plt.imshow(np.transpose(opinions_sorted[0:-2,:]))
# plt.show()

# WSDF1.close()
