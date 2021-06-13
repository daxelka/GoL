import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class GoL:
    
    def __init__(self, graph = None, threshold_1=2, threshold_2=4):        
        self.n_b = threshold_1
        self.n_d = threshold_2
        self.G = graph
        self.A = nx.adjacency_matrix(self.G)
        
    def step(self, o):
        opinionated_neighbours = self.A.dot(o)

        # above threshold_max opinion formation
        influence_negative = 1 * np.invert(opinionated_neighbours >= self.n_d)
        new_opinion = np.minimum(o, influence_negative)

        # above threshold_min opinion formation
        influence_positive = 1 * np.all([opinionated_neighbours >= self.n_b, opinionated_neighbours < self.n_d], axis=0)
        resulted_opinion = np.maximum(new_opinion, influence_positive)        

        return resulted_opinion

    def run(self, v, number_steps):
        opinions = np.empty((number_steps, v.shape[0]), dtype=int)
        opinions[0, :] = v

        for i in range(1, number_steps):
            v_new = self.step(v)
            v = v_new
            opinions[i, :] = v_new
        return opinions

    def draw_snapshoot(self, v):
        nx.draw(self.G, node_color = self.colors(v), with_labels=True, font_weight='bold')
        plt.show()          

    def colors(self, o):
        result = []
        for item in o:
            if item == 1:
                result.append('red')
            else:
                result.append('blue')    
        return result             