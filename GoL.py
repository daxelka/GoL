import numpy as np

class GoL:
    
    def __init__(self, adj_matrix = None):        
        self.A = adj_matrix
        
    def step(self, A, o, threshold_1, threshold_2):
        alive_neighbours = A.dot(o)

        # above threshold_max opinion formation
        influence_negative = 1 * np.invert(alive_neighbours >= threshold_2)
        new_opinion = np.minimum(o, influence_negative)

        # above threshold_min opinion formation
        influence_positive = 1 * np.all([alive_neighbours >= threshold_1, alive_neighbours < threshold_2], axis=0)
        opinion = np.maximum(new_opinion, influence_positive)        

        return opinion

    def iteration(self, A, v, threshold_1, threshold_2, number_steps):
        for i in range(0,number_steps):
            v_new = self.step(A, v,threshold_1, threshold_2)
            v = v_new
            nx.draw(G, node_color = colors(v_new), with_labels=True, font_weight='bold')
            plt.show()  

    def colors(self, o):
        result = []
        for item in o:
            if item == 1:
                result.append('red')
            else:
                result.append('blue')    
        return result             