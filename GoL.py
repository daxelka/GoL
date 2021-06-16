import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation

class GoL:

    def __init__(self, graph = None, threshold_birth = 0.3, threshold_death=0.8, threshold_starvation = 0.1):
        self.n_b = threshold_birth
        self.n_d = threshold_death
        self.n_s = threshold_starvation
        self.G = graph
        self.A = nx.adjacency_matrix(self.G)

    def degree(self):
        degree = self.A.dot(np.ones((self.A.shape[0]), dtype = int))
        return degree

    def step(self, o):
        opinionated_neighbours = self.A.dot(o)
        opinionated_rate = np.divide(opinionated_neighbours, self.degree())

        # above threshold_max opinion formation. Negative influence
        influence_negative = 1 * np.invert(opinionated_rate >= self.n_d)
        opinion_updated1 = np.minimum(o, influence_negative)

        # # Loose interest if there is too little who shared this opinion around
        # influence_starvation = 1 * np.invert(opinionated_rate <= self.n_s)
        # opinion_updated2 = np.minimum(o, influence_starvation)

        # above threshold_min opinion formation. Positive influence
        influence_positive = 1 * np.all([opinionated_rate >= self.n_b, opinionated_rate < self.n_d], axis=0)
        resulted_opinion = np.maximum(opinion_updated1, influence_positive)

        # resulted_opinion = np.multiply(o,mask_1) + np.multiply(o, mask_2)

        return resulted_opinion

    def run(self, v, number_steps):
        opinions = np.empty((number_steps, v.shape[0]), dtype=int)
        opinions[0, :] = v

        for i in range(1, number_steps):
            v_new = self.step(v)
            v = v_new
            opinions[i, :] = v_new
        return opinions

    def draw_snapshoot(self, positions, v):
        # positions = nx.spring_layout(self.G)
        nx.draw(self.G, positions, node_color = self.colors(v), with_labels=True, font_weight='bold')
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
        nx.draw(self.G, positions, node_color = self.colors(opinions[frame,:]), with_labels = False, node_size = 36)

    def animation(self, figure, opinions):
        frame_list = opinions.shape[0]
        positions = nx.spring_layout(self.G)
        ani = animation.FuncAnimation(figure, self.animate, frames = frame_list, fargs=(opinions, positions), interval=1000, blit=False, repeat = False)
        plt.show()

    def popularity(self, opinions):
        popularity = np.sum(opinions, axis = 1)
        return popularity

    # # Plotting information spreading on networks
    # def visualise_simulations(self, opinions):
    #     positions = nx.spring_layout(self.G)

    #     for frame in range(opinions.shape[0]):
    #         self.draw_snapshoot(positions, opinions[frame,:])
