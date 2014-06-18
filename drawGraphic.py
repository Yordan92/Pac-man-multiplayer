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

class DrawGraphic(PacMan):

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
		
		pacman = pygame.image.load(PacMan.name_image)
		pacmanL = pygame.transform.rotate(pacman, 180)
		pacmanU = pygame.transform.rotate(pacman, 90)
		pacmanD = pygame.transform.rotate(pacman, 270)
		default_rotation = pacman
		if direction == 'l':
			default_rotation = pacmanL
			PacMan.move_left(self)
		elif direction == 'r':
			default_rotation = pacman
			PacMan.move_right(self)
		elif direction == 'u':
			default_rotation = pacmanU
			PacMan.move_up(self)
		else:
			default_rotation = pacmanD
			PacMan.move_down(self)

		screen.blit(default_rotation,
					(PacMan.cords['x'], PacMan.cords['y']))










g = MakeGraph()
print (g.find_nodes())
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
a = DrawGraphic(pacm)
print(pacm.find_closest_nodes())
while True:

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
	print(pacm.find_closest_nodes())
	a.draw_nodes(screen)
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
	fpsClock.tick(5)
