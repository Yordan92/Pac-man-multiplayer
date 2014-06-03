import pygame
from PacManMap import *
class MakeGraph:

	def __init__(self):
		self.shortest_path_from_one_to_other = {}
		self.nodes = self.find_Nodes()

	def find_Nodes(self):
		nodes = []
		for row_n in range(1, len(Map) - 1):
			for col_n in range(2, len(Map[0]) - 1):

				if (Map[row_n][col_n] != 0 and Map[row_n][col_n + 1] != 0 and
						Map[row_n][col_n - 1] != 0):
					if ((row_n > 0 and Map[row_n - 1][col_n] != 0) or
							(row_n < len(Map[0]) - 2 and Map[row_n + 1][col_n] != 0)):
						nodes.append((row_n, col_n))
						Map[row_n][col_n] = 3
		Map1 = list(zip(*Map))
		for row_n in range(1, len(Map1) - 1):
			for col_n in range(2, len(Map1[0]) - 1):

				if (Map1[row_n][col_n] != 0 and Map1[row_n][col_n + 1] != 0 and
						Map1[row_n][col_n - 1] != 0):
					if ((row_n > 0 and Map1[row_n - 1][col_n] != 0) or
							(row_n < len(Map1[0]) - 2 and Map1[row_n + 1][col_n] != 0)):
						nodes.append((col_n, row_n))
						Map[col_n][row_n] = 3

		return nodes

	def is_p_vertex(self, vertex):
		if ((vertex[0] < 0 or vertex[0] >= len(Map)) or
				(vertex[1] < 0 or vertex[1] >= len(Map[0]))):
			return False
		if Map[vertex[0]][vertex[1]] == 0:
			return False
		return True

	def BFS(self, vertex):
		Path_all_in_Matrix = {}
		Path_all_in_Matrix[vertex] = vertex
		Path_to_Nodes = {}
		Path_to_Nodes[vertex] = vertex
		queue = [vertex]
		Visited = [vertex]
		all_Nodes = self.find_Nodes()
		all_Nodes.remove(vertex)
		while queue != []:
			new_v = queue.pop(0)
			new_v_adj = [(new_v[0] - 1, new_v[1]),
						 (new_v[0] + 1, new_v[1]),
						 (new_v[0], new_v[1] - 1),
						 (new_v[0], new_v[1] + 1)]

			if new_v in all_Nodes:
				full_path = [new_v]
				temp_v = new_v

				while Path_all_in_Matrix[temp_v] != vertex:
					full_path.append(Path_all_in_Matrix[temp_v])
					temp_v = Path_all_in_Matrix[temp_v]
				 

				full_path.reverse()
				temp_full = []
				for i in full_path:
					if i in all_Nodes:
						temp_full.append(i)
						break
					temp_full.append(i)
				Path_to_Nodes[new_v] = temp_full
				all_Nodes.remove(new_v)

			for v_adj in new_v_adj:
				if self.is_p_vertex(v_adj) and v_adj not in Visited:
					queue.append(v_adj)
					Path_all_in_Matrix[v_adj] = new_v
					Visited.append(v_adj)

		return Path_to_Nodes

	def make_all_Paths(self):

		all_Nodes = self.find_Nodes()
		for node in all_Nodes:
			self.shortest_path_from_one_to_other[node] = self.BFS(node)
		return self.shortest_path_from_one_to_other

	def draw_Shortest_path(self, screen, v1, v2):
		
		if not self.shortest_path_from_one_to_other:
			self.make_all_Paths()
		l = self.shortest_path_from_one_to_other[v1][v2]
		full = l
	   
		while l[-1] != v2:
			print(l)
			l = self.shortest_path_from_one_to_other[full[-1]][v2]
			full += l

		# print (full)
		for node in full:
			# print(node)
			pygame.draw.rect(screen, (0, 255, 0),
							 (node[1] * MOVE, node[0] * MOVE, 23, 23))
