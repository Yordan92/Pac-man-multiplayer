import unittest
from MakeGraph import MakeGraph
from Moving_pacman import *
class TestMakeGraphFunctions(unittest.TestCase):
	nodes = [(1, 4), (1, 12), (4, 4), (4, 6), (4, 7), (4, 9), (4, 11),
			 (4, 12), (4, 13), (8, 7), (8, 8), (8, 9), (10, 4), (10, 13), 
			 (14, 4), (14, 6), (14, 11), (14, 12), (14, 13), (16, 7), (16, 9),
			 (18, 2), (18, 14), (20, 7), (20, 9), (4, 1), (4, 4), (6, 4), (10, 4),
			 (14, 4), (16, 4), (10, 6), (12, 6), (9, 8), (8, 9), (9, 9), (10, 11),
			 (12, 11), (16, 12), (6, 13), (10, 13), (4, 15)]

	
	def test_moving_left(self):
		p = [(138,184),(92,276),(23,23)]
		g = MakeGraph()
		for i in p:
			pacman = PacMan(g)
			pacman.cords['x'] = i[0]
			pacman.cords['y'] = i[1]
			self.assertFalse(pacman.move_left())

	def test_moving_right(self):
		p = [(92,276),(92,414),(345,23)]
		g = MakeGraph()
		for i in p:
			pacman = PacMan(g)
			pacman.cords['x'] = i[0]
			pacman.cords['y'] = i[1]
			self.assertFalse(pacman.move_right())

	def test_moving_up(self):
		p = [(184,92),(23,23),(69,460)]
		g = MakeGraph()
		for i in p:
			pacman = PacMan(g)
			pacman.cords['x'] = i[0]
			pacman.cords['y'] = i[1]
			self.assertFalse(pacman.move_up())

	def test_moving_up(self):
		p = [(184,92),(46,322),(69,460)]
		g = MakeGraph()
		for i in p:
			pacman = PacMan(g)
			pacman.cords['x'] = i[0]
			pacman.cords['y'] = i[1]
			self.assertFalse(pacman.move_down())

	def test_pacman_closest_nodes(self):
		p = [(184,92),(46,322),(69,460),(23,23),(69,460)]
		g = MakeGraph()
		for i in p:
			pacman = PacMan(g)
			pacman.cords['x'] = i[0]
			pacman.cords['y'] = i[1]
			for nodes in pacman.find_closest_nodes():
				self.assertTrue(nodes in self.nodes)

if __name__ == '__main__':
	unittest.main()
	