import pygame
import sys
import os
import re
import itertools
import string
import time 
from pygame.locals import *
from PacManMap import *
from MakeGraph import *
from Moving_pacman import *
from Ghosts import Ghost
import time 
class DrawGraphic():

	def __init__(self,class_pacman,class_ghost,class_ghost1,class_ghost2,class_ghost3):
		self.ghost = class_ghost
		self.ghost1 = class_ghost1
		self.ghost2 = class_ghost2
		self.ghost3 = class_ghost3
		self.pacman = class_pacman
	def draw_graphic(self, screen):
	   
		for i in range(len(Map)):
			for j in range(len(Map[0])):
				if Map[i][j] == 0:
					pygame.draw.rect(screen, (0, 0, 255),
									 (j * MOVE, i * MOVE, 23, 23))
				else:
					pygame.draw.rect(screen, (0, 0, 0),
									 (j * MOVE, i * MOVE, 23, 23))

					if Map[i][j] == 2:
						screen.set_at((j * 23 + 12, i * 23 + 12),
									  (255, 255, 255))
					if Map[i][j] == 3:
						pygame.draw.rect(screen, (255, 0, 0),
										 (j * MOVE, i * MOVE, 23, 23))

	def draw_nodes(self,screen):
		l = PacMan.find_closest_nodes(self)
		for i in l:
			pygame.draw.rect(screen, (255, 0, 255),
									 (i[0] * MOVE, i[1] * MOVE, 23, 23))


	def draw_pacman(self, screen, direction):
		
		pacman = pygame.image.load(self.pacman.name_image)
		pacmanL = pygame.transform.rotate(pacman, 180)
		pacmanU = pygame.transform.rotate(pacman, 90)
		pacmanD = pygame.transform.rotate(pacman, 270)
		default_rotation = pacman
		if direction == 'l':
			default_rotation = pacmanL
			self.pacman.move_left()
		elif direction == 'r':
			default_rotation = pacman
			self.pacman.move_right()
		elif direction == 'u':
			default_rotation = pacmanU
			self.pacman.move_up()
		else:
			default_rotation = pacmanD
			self.pacman.move_down()
		# print((self.cords['x'], self.cords['y']))
		screen.blit(default_rotation,
					(self.pacman.cords['x'], self.pacman.cords['y']))

	def draw_ghost(self,screen,name,cords_x,cords_y):
		
		ghost1 = pygame.image.load("Ghosts/"+name[0]+".png")
		ghost2 = pygame.image.load("Ghosts/"+name[1]+".png")
		ghost3 = pygame.image.load("Ghosts/"+name[2]+".png")
		ghost4 = pygame.image.load("Ghosts/"+name[3]+".png")
		
		# pygame.draw.rect(screen, (124, 124, 0),
		# 								 (p[1]* 23, p[0] * 23, 23, 23))
		screen.blit(ghost1,(cords_x[0], cords_y[0]))
		screen.blit(ghost2,(cords_x[1], cords_y[1]))
		screen.blit(ghost3,(cords_x[2], cords_y[2]))
		screen.blit(ghost4,(cords_x[3], cords_y[3]))


class PacManPlay(DrawGraphic):
	
	def __init__(self,class_pacman,class_ghost,class_ghost1,class_ghost2,class_ghost3):
		self.ghost = class_ghost
		self.ghost1 = class_ghost1
		self.ghost2 = class_ghost2
		self.ghost3 = class_ghost3
		self.pacman = class_pacman

	def find_pacman_cords(self):
		pacman_x = int(self.pacman.cords['y']/23)
		pacman_y = int(self.pacman.cords['x']/23)
		return (pacman_x,pacman_y)

	def split_pacman_ver(self):
		closest_nod = self.pacman.find_closest_nodes()
		pacman_cord = self.find_pacman_cords()
		cordinates = []
		for nodes in closest_nod:
			if nodes[0] <= pacman_cord[0] and nodes[1] >= pacman_cord[1]:
				cordinates.insert(0,nodes)
			if nodes[0] <= pacman_cord[0] and nodes[1] < pacman_cord[1]:
				cordinates.insert(1,nodes)
			if nodes[0] > pacman_cord[0] and nodes[1] >= pacman_cord[1]:
				cordinates.insert(2,nodes)
			if nodes[0] > pacman_cord[0] and nodes[1] < pacman_cord[1]:
				cordinates.insert(3,nodes)

		
		return cordinates
	

	def are_goint_to_colide(self,screen,ghost_list):
		temp_ghost_list = []
		temp_ghost_list.extend(ghost_list)
		count_moves = 0
		for i in range(4):
			
			for f_ghost in temp_ghost_list:
				can_move = True
				for s_ghost in ghost_list:
					if f_ghost != s_ghost and f_ghost.next_hop() == s_ghost.find_ghost_cords():
						can_move = False
						break
				if can_move == True:
					count_moves += 1
					print("mestim ", f_ghost.index)
					print("next_hopove:_________")
					# for i in ghost_list:
					# 	print(i.index,"-",i.find_ghost_cords(),"-",i.next_hop())
					f_ghost.ghost_make_move()
					temp_ghost_list.remove(f_ghost)
					print(temp_ghost_list)
					break
		if count_moves <3:
			for i in ghost_list:
						print(i.index,"-",i.find_ghost_cords(),"-",i.next_hop())

		return count_moves	
				# if (f_ghost.next_hop() == s_ghost.find_ghost_cords() and
				# 	s_ghost.next_hop() == f_ghost.find_ghost_cords()):
				# 	temp = s_ghost.path
				# 	s_ghost.path = f_ghost.path
				# 	f_ghost.path = temp



	def ghost_chase(self,screen):
		self.ghost.get_pictures()
		self.ghost1.get_pictures()
		self.ghost2.get_pictures()
		self.ghost3.get_pictures()
		chasing_l = self.split_pacman_ver()
		pacman_cord = self.find_pacman_cords()

		
		if not self.ghost.path:
			self.ghost.ghost_move(screen,chasing_l[0],pacman_cord)
		if not self.ghost1.path:
			self.ghost1.ghost_move(screen,chasing_l[1],pacman_cord)
		if not self.ghost2.path:
			self.ghost2.ghost_move(screen,chasing_l[0],pacman_cord)
		if not self.ghost3.path:
			self.ghost3.ghost_move(screen,chasing_l[1],pacman_cord)
		gst = [self.ghost,self.ghost1,self.ghost2,self.ghost3]
		if self.are_goint_to_colide(screen,gst) < 3:
			print("Vleznah v if-a _____________________")
			for g in gst:
				for g1 in gst:
					if g.next_hop()==g1.find_ghost_cords() and g1.next_hop()==g.find_ghost_cords():
						print("si ebi")
						temp = g.path
						g.path = g1.path
						g1.path = temp
						



		# print("____________________")
		# self.ghost.ghost_make_move()
		# self.ghost1.ghost_make_move()
		# self.ghost2.ghost_make_move()
		# self.ghost3.ghost_make_move()
		# print(ghost3.next_hop(),ghost.find_ghost_cords())
		# pygame.draw.rect(screen, (255, 0, 255),
		# 							 (ghost3.next_hop()[1] * MOVE, ghost3.next_hop()[0] * MOVE, 23, 23))
		# pygame.draw.rect(screen, (255, 0, 255),
		# 							 (ghost.find_ghost_cords()[1] * MOVE, ghost.find_ghost_cords()[0] * MOVE, 23, 23))
		# print(ghost3.next_hop() == ghost.find_ghost_cords())
		name = [self.ghost.name_image,self.ghost1.name_image,
				self.ghost2.name_image, self.ghost3.name_image]
		cords_x = [self.ghost.cords['x'],self.ghost1.cords['x'],self.ghost2.cords['x'],self.ghost3.cords['x']]
		cords_y = [self.ghost.cords['y'],self.ghost1.cords['y'],self.ghost2.cords['y'],self.ghost3.cords['y']]
		self.draw_ghost(screen,name,cords_x,cords_y)

	def is_game_over(self):
		ghost_list = [self.ghost,self.ghost1,self.ghost2,self.ghost3]
		for ghost in ghost_list:
			if ghost.find_ghost_cords() == self.find_pacman_cords():
				return False
		return True








g = MakeGraph()
print (g.find_nodes())
g.make_all_paths()
# print(g.get_shortest_path()[(10,4)][(4,11)])
# print(g.is_p_vertex((100,100)))
# print(g.bfs((1,4)))
ALL_p = g.make_all_paths()
# print(ALL_p[(1,4)][(4,4)])
pygame.init()
screen = pygame.display.set_mode((WIDTH, HIGHT))
background = pygame.image.load("pacm.jpg")

fpsClock = pygame.time.Clock()
# d.drawLabyrinth(screen,(0,0,255))
# a.drawLabyrint(screen,(0,0,255),5)
node = g.find_nodes()
node1 = g.find_nodes()
node.pop(0)
DIRECTION = 'l'
pacm = PacMan(g)
ghost = Ghost(g,184,207)
ghost1 = Ghost(g,207,207)
ghost2 = Ghost(g,207,230)
ghost3 = Ghost(g,184,230)
a = DrawGraphic(pacm,ghost,ghost1,ghost2,ghost3)
testvam = PacManPlay(pacm,ghost,ghost1,ghost2,ghost3)
print(testvam.split_pacman_ver())

while testvam.is_game_over():

	a.draw_graphic(screen)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				DIRECTION = 'l'
			elif event.key == K_RIGHT:
				DIRECTION = 'r'
			elif event.key == K_DOWN:
				DIRECTION = 'd'
			else:
				DIRECTION = 'u'
		else:
			pass
	a.draw_pacman(screen, DIRECTION)
	pacm.draw_nodes(screen)
	testvam.ghost_chase(screen)
	# print(pacm.find_closest_nodes())
	# a.draw_nodes(screen)
	# print(pacm.find_nodes())
	# g.draw_shortest_path(screen, node1[28], node1[13])
	# if node:
	#     g.draw_shortest_path(screen, node1[0], node.pop(0))
	# else:
	#     node1.pop(0)
	#     p = node1[0]
	#     node = g.find_nodes()
		
	#     node.remove(p)
	
	# screen.blit(background,(0,0,480,640))
	# a.drawLabyrint(screen,(0,0,255),5)
	# p = pygame.mouse.get_pos()
	# i = pygame.Surface((1000, 1000))

	# a.drawLabyrinth(screen,(0,0,255))
	# print(screen.get_at(p))

	# pygame.draw.polygon(screen,(0,0,255),[(0, 0), (20, 0), (20, 80), (0, 80)],3)
	pygame.display.flip()
	pygame.display.update()
	fpsClock.tick(6)
