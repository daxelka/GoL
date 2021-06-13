import unittest
import numpy as np
import networkx as nx
from GoL import GoL

# python3 -m unittest test_GoL.py

class TestGoL(unittest.TestCase):

    def setUp(self):
        self.A = np.array([[0,1,1,1,1],[1,0,1,0,0],[1,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]])
        self.G = nx.from_numpy_matrix(self.A)
        
        self.threshold_1 = 2
        self.threshold_2 = 3
        
        self.game = GoL(self.G, self.threshold_1, self.threshold_2)

    def test_steps(self):            
        self.assertEqual(self.game.step([1,1,0,0,0]).tolist(), [1,1,1,0,0])
        self.assertEqual(self.game.step([1,1,1,0,0]).tolist(), [1,1,1,1,0])
        self.assertEqual(self.game.step([1,1,1,1,0]).tolist(), [0,1,0,1,1])
        self.assertEqual(self.game.step([0,1,0,1,1]).tolist(), [0,1,1,1,1])
        self.assertEqual(self.game.step([0,1,1,1,1]).tolist(), [0,1,1,1,1])
