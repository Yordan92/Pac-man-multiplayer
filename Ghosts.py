from MakeGraph import MakeGraph
from Moving_pacman import PacMan
import pygame
class Ghost():
	index = 0
	name_image_u = "Null" 
	name_image_d = "Null"
	name_image_l = "Null"
	name_image_r = "Null"
	cords = {'x': 92, 'y': 276}

	def __init__(self,class_graph):
		Ghost.index = Ghost.index + 1
		self.all_nodes = class_graph.get_nodes()
		self.paths_to_all_nodes = class_graph.get_shortest_path()
		self.path = []
	def get_pictures(self):
		if index == 0 :
			self.name_image_u = "Ghost_red_up"
			self.name_image_d = "Ghost_red_down"
			self.name_image_l = "Ghost_red_left"
			self.name_image_r = "Ghost_red_right"
		if index == 1:
			self.name_image_u = "Ghost_orange_up"
			self.name_image_d = "Ghost_orange_down"
			self.name_image_l = "Ghost_orange_left"
			self.name_image_r = "Ghost_orange_right"
		if index == 2:
			self.name_image_u = "Ghost_pink_up"
			self.name_image_d = "Ghost_pink_down"
			self.name_image_l = "Ghost_pink_left"
			self.name_image_r = "Ghost_pink_right"
		if index == 3:
			self.name_image_u = "Ghost_cyan_up"
			self.name_image_d = "Ghost_cyan_down"
			self.name_image_l = "Ghost_cyan_left"
			self.name_image_r = "Ghost_cyan_right"

	def find_closest_vertex(self):
		closest_nodes =[]
		ghost_x = int(self.cords['x']/23)
		ghost_y = int(self.cords['y']/23)
		
		vertex = (ghost_y,ghost_x)
		queue = [vertex]
		map_to_a_vertex = {}

		print (self.all_nodes)
		if vertex in self.all_nodes:
		 	return []
		# print("trqbva da e sprqlo")
		while queue != []:
			new_v = queue.pop(0)
			new_v_adj = [(new_v[0] - 1, new_v[1]),
						 (new_v[0] + 1, new_v[1]),
						 (new_v[0], new_v[1] - 1),
						 (new_v[0], new_v[1] + 1)]

			for v_adj in new_v_adj:
				map_to_a_vertex[v_adj] = new_v
				if v_adj in self.all_nodes:
					full_path = [v_adj]

					while map_to_a_vertex[v_adj] != vertex:
						v_adj = map_to_a_vertex[v_adj]
						full_path.insert(0,v_adj)
					return full_path
				queue.append(v_adj)

	def ghost_move(self, pacman_vertex):
		my_cords = (int(self.cords['y']/23),int(self.cords['x']/23))
		if my_cords == pacman_vertex:
			return my_cords
		if not self.path:
			if self.find_closest_vertex() != []:
				self.path = self.find_closest_vertex()
			else:
				
				
				for i in self.paths_to_all_nodes[my_cords][pacman_vertex]:
					self.path.extend(2*[i])				
		
		new_step =  self.path.pop(0)
		self.cords['y'] = new_step[0]*23
		self.cords['x'] = new_step[1]*23



	def draw_ghost(self,screen):
		ghost = pygame.image.load("Ghosts/Ghost_cyan_down.png")
		# print(self.find_closest_vertex())
		self.ghost_move((4,11))
		# p = self.path[-1]
		
		# pygame.draw.rect(screen, (124, 124, 0),
		# 								 (p[1]* 23, p[0] * 23, 23, 23))
		screen.blit(ghost,(self.cords['x'], self.cords['y']))




