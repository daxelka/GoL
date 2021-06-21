import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation

class GoL:

    def __init__(self, graph = None, threshold_birth = 0.3, threshold_overpopulation = 0.8, threshold_starvation = 0.1):
        self.n_b = threshold_birth
        self.n_d = threshold_overpopulation
        self.n_s = threshold_starvation
        self.G = graph
        self.A = nx.adjacency_matrix(self.G)

    def degree(self):
        degree = self.A.dot(np.ones((self.A.shape[0]), dtype = int))
        return degree

    def step(self, o):
        # Calculate the percentage of opinionated neighbours
        opinionated_neighbours = self.A.dot(o)
        opinionated_rate = np.divide(opinionated_neighbours, self.degree())

        # Find those who loose interest due to the opinion overpopularity among their neighbours
        influence_overpopulation = 1 * np.invert(opinionated_rate >= self.n_d)
        o_updated_1 = np.minimum(o, influence_overpopulation)
        mask_1 = 1 * opinionated_rate >= self.n_d

        # Find those who loose interest if there is too little who shared this opinion around
        influence_starvation = 1 * np.invert(opinionated_rate <= self.n_s)
        o_updated_2 = np.minimum(o, influence_starvation)
        mask_2 = 1 * opinionated_rate < self.n_s

        # Find those who newly abobt opinion
        influence_adoption = 1 * np.all([opinionated_rate >= self.n_b, opinionated_rate < self.n_d], axis=0)
        o_updated_3 = np.maximum(o, influence_adoption)
        mask_3 = influence_adoption

        # Get those who stay unchanged
        mask_unchanged = 1 * np.invert(list(map(bool, mask_1 + mask_2 + mask_3)))

        # Check that every node was updated and only once
        assert (mask_1+mask_2+mask_3+mask_unchanged == np.ones((self.A.shape[0]), dtype = int)).all(),"Either not all nodes updated or some updated several times"
        assert (np.all(mask_1+mask_2+mask_3+mask_unchanged) <=1), "Some nodes were updated several times"
        
        # Calculate resulted opinion
        resulted_opinion = np.multiply(o_updated_1,mask_1) + np.multiply(o_updated_2, mask_2) + np.multiply(o_updated_3,mask_3) + np.multiply(o, mask_unchanged)

        return resulted_opinion

    def run(self, v, number_steps):
        opinions = np.empty((number_steps, v.shape[0]), dtype=int)
        opinions[0, :] = v

        for i in range(1, number_steps):
            v_new = self.step(v)
            v = v_new
            opinions[i, :] = v_new
        return opinions

    def draw_snapshoot(self, positions, o):
        positions = nx.spring_layout(self.G)
        nx.draw(self.G, positions, node_color = self.colors(o), with_labels=True, font_weight='bold')
        plt.show()

    def colors(self, o):
        result = []
        for item in o:
            if item == 1:
                result.append('red')
            else:
                result.append('blue')
        return result

    def animate(self, frame, opinions, positions):
            # nx.draw(self.G, positions, node_color = self.colors(opinions[frame,:]), with_labels = False, node_size = 36)
        nx.draw_circular(self.G, node_color = self.colors(opinions[frame,:]), with_labels = False, node_size = 36)    

    def animation(self, figure, opinions):
        frame_list = opinions.shape[0]
        positions = nx.spring_layout(self.G)
        ani = animation.FuncAnimation(figure, self.animate, frames = frame_list, fargs=(opinions, positions), interval=1000, blit=False, repeat = False)
        plt.show()

    def popularity(self, opinions):
        popularity = np.sum(opinions, axis = 1)
        return popularity

    def unaffected_nodes(self,opinions):
        # Calculate changes in nodes' opinions
        changed_opinion = np.diff(opinions, axis=0)
        # Find where all values in the columns are zero
        mask = (changed_opinion == 0).all(0)
        # Find the indices of these columns, will be id of stubborn nodes
        nodes_unchanged = np.where(mask)[0]
        return nodes_unchanged

    def unaffected_dynamics(self, opinions):
        nodes_unchanged = []
        for i in range(opinions.shape[0]):
            nodes_unchanged.append(self.unaffected_nodes(opinions[0:i+2,:])) 
        return nodes_unchanged      
            

    # # Plotting information spreading on networks
    # def visualise_simulations(self, opinions):
    #     positions = nx.spring_layout(self.G)

    #     for frame in range(opinions.shape[0]):
    #         self.draw_snapshoot(positions, opinions[frame,:])
