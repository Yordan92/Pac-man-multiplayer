import pygame 
from PacManMap import *
from MakeGraph import MakeGraph

class PacMan(MakeGraph):

	name_image = "pacm.jpg"
	cords = {'x': 92, 'y': 276}
	
	def __init__(self,class_a):
		# self.name_image = "pacm.jpg"
		# self.cords = {'x': 92, 'y': 276}
		self.nodes = class_a.nodes


	def move_up(self):
		temp_y = int(self.cords['y'] / MOVE) - 1
		temp_x = int(self.cords['x'] / MOVE)
		if Map[temp_y][temp_x] == 2:
			Map[temp_y][temp_x] = 1
		if temp_y >= 0 and Map[temp_y][temp_x] != 0:
			self.cords['y'] -= MOVE

	def move_down(self):
		temp_y = int(self.cords['y'] / MOVE) + 1
		temp_x = int(self.cords['x'] / MOVE)
		if Map[temp_y][temp_x] == 2:
			Map[temp_y][temp_x] = 1
		if temp_y < len(Map) and Map[temp_y][temp_x] != 0:
			self.cords['y'] += MOVE

	def move_left(self):
		temp_x = int(self.cords['x'] / MOVE) - 1
		temp_y = int(self.cords['y'] / MOVE)
		if Map[temp_y][temp_x] == 2:
			Map[temp_y][temp_x] = 1

		if temp_x <= 1 and temp_y == 10:
			temp_x = len(Map[0]) - 1
			self.cords['x'] = MOVE * temp_x

		if temp_x >= 0 and Map[temp_y][temp_x] != 0:
			self.cords['x'] -= MOVE

	def move_right(self):
		temp_x = int(self.cords['x'] / MOVE) + 1
		temp_y = int(self.cords['y'] / MOVE)

		if Map[temp_y][temp_x] == 2:
			Map[temp_y][temp_x] = 1

		if temp_x == len(Map[0]) - 2 and temp_y == 10:
			temp_x = 1
			self.cords['x'] = MOVE

		if temp_x < len(Map[0]) and Map[temp_y][temp_x] != 0:
			self.cords['x'] += MOVE

	def find_closest_nodes(self):
		closest_nodes =[]
		pacman_x = int(self.cords['x']/23)
		pacman_y = int(self.cords['y']/23)
		
		vertex = (pacman_y,pacman_x)
		queue = [vertex]
		Visited = [vertex]
		all_Nodes = self.nodes
		# if vertex in all_Nodes:
		# 	all_Nodes.remove(vertex)
		while queue != []:
			new_v = queue.pop(0)
			new_v_adj = [(new_v[0] - 1, new_v[1]),
						 (new_v[0] + 1, new_v[1]),
						 (new_v[0], new_v[1] - 1),
						 (new_v[0], new_v[1] + 1)]

			for v_adj in new_v_adj:
				if self.is_p_vertex(v_adj) and v_adj not in Visited:
					if v_adj in all_Nodes:
						closest_nodes.append((v_adj[0],v_adj[1]))
					else:
						queue.append(v_adj)
				Visited.append(v_adj)
					
					

		return closest_nodes


	def draw_nodes(self,screen):
		l = self.find_closest_nodes()
		for i in l:
			pygame.draw.rect(screen, (255, 0, 255),
                                     (i[1] * MOVE, i[0] * MOVE, 23, 23))


	def draw_pacman(self, screen, direction):
		pacman = pygame.image.load(self.name_image)
		pacmanL = pygame.transform.rotate(pacman, 180)
		pacmanU = pygame.transform.rotate(pacman, 90)
		pacmanD = pygame.transform.rotate(pacman, 270)

		default_rotation = pacman
		if direction == 'l':
			default_rotation = pacmanL
			self.move_left()
		elif direction == 'r':
			default_rotation = pacman
			self.move_right()
		elif direction == 'u':
			default_rotation = pacmanU
			self.move_up()
		else:
			default_rotation = pacmanD
			self.move_down()
		print((self.cords['x'], self.cords['y']))
		screen.blit(default_rotation,
					(self.cords['x'], self.cords['y']))

