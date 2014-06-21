import pygame
import sys
import os
import re
import itertools
import string
import time 
import socket
import pickle
from pygame.locals import *
from Draw_pacman_client import *

MOVE = 23
WIDTH = 480
HIGHT = 640

class DrawGraphic():

	def __init__(self,pacman):
		self.pacman = pacman


	def draw_graphic(self, screen, Map):
	   
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
					# if Map[i][j] == 3:
					# 	pygame.draw.rect(screen, (255, 0, 0),
					# 					 (j * MOVE, i * MOVE, 23, 23))

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

	def draw_pacman(self, screen,cords_x,cords_y,name_image,direction):
		
		pacman = pygame.image.load(name_image)
		pacmanL = pygame.transform.rotate(pacman, 180)
		pacmanU = pygame.transform.rotate(pacman, 90)
		pacmanD = pygame.transform.rotate(pacman, 270)
		default_rotation = pacman
		if direction == 'l':
			default_rotation = pacmanL
			
		elif direction == 'r':
			default_rotation = pacman
			
		elif direction == 'u':
			default_rotation = pacmanU
			
		else:
			default_rotation = pacmanD
			
		# print((self.cords['x'], self.cords['y']))
		screen.blit(default_rotation,
					(cords_x, cords_y))
	def draw_c_pacman(self, screen,direction):
		
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

	

UDP_IP = "192.168.1.110"
UDP_Port = 5005
sock = socket.socket(socket.AF_INET, # Internet
		socket.SOCK_DGRAM) # UDP

screen = pygame.display.set_mode((WIDTH, HIGHT))
fpsClock = pygame.time.Clock()
DIRECTION = 'l'
pacman = PacMan()
d = DrawGraphic(pacman)
while True:
	pygame.init()
	pacman_c = {'p':[pacman.cords,pacman.name_image,DIRECTION],'m':Map}
	pacman_c_pick = pickle.dumps(pacman_c)
	sock.sendto(pacman_c_pick,(UDP_IP,UDP_Port))
	data,clientaddr = sock.recvfrom(2048)
	all_cords = pickle.loads(data)
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
	Map = all_cords['m']
	d.draw_graphic(screen,all_cords['m'])
	d.draw_ghost(screen,all_cords['g'][0],all_cords['g'][1],all_cords['g'][2])
	d.draw_pacman(screen,all_cords['p'][0]['x'],all_cords['p'][0]['y'],all_cords['p'][1],all_cords['p'][2])
	d.draw_c_pacman(screen, DIRECTION)
	pygame.display.flip()
	pygame.display.update()
	fpsClock.tick(6)

