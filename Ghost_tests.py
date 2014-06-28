import unittest
from MakeGraph import MakeGraph
from Ghosts import *
class TestMakeGraphFunctions(unittest.TestCase):
	
	graph = MakeGraph()
	g = Ghost(graph,184,207)
	g.path = [(8, 7), (8, 7), (8, 6), (8, 6), (9, 6), (9, 6), (10, 6), (10, 6), (10, 5), (10, 5), (10, 4), (10, 4)]

	def test_next_hop(self):
		self.assertEqual(self.g.next_hop(),(8,7))

	def test_find_ghost_cords(self):
		self.assertEqual(self.g.find_ghost_cords(),(9,8))
	
	def test_find_closest_nodes(self):
		self.assertEqual(self.g.find_closest_nodes(),[(8, 8), (9, 9)])

	def test_find_closest_vetex(self):
		self.assertEqual(self.g.find_closest_vertex(),[])

	def test_ghost_move(self):
		g_temp = Ghost(self.graph,184,207)
		g_temp.hunting = True
		g_temp.ghost_move((10, 4),(12,4))
		self.assertEqual(g_temp.path,[(8, 8)])

	def test_ghost_make_move(self):
		self.g.ghost_make_move()
		x = self.g.cords['x']
		y = self.g.cords['y']
		self.assertEqual((x,y),(7*23,8*23))	
if __name__ == '__main__':
	unittest.main()
	