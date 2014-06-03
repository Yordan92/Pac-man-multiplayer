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

class DrawGraphic:

    def draw_Graphic(self, screen):
       
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



       


        





a = DrawGraphic()
g = MakeGraph()
print (g.find_Nodes())
# print(g.is_p_vertex((100,100)))
# print(g.BFS((1,4)))
ALL_p = g.make_all_Paths()
# print(ALL_p[(1,4)][(4,4)])
pygame.init()
screen = pygame.display.set_mode((WIDTH, HIGHT))
background = pygame.image.load("pacm.jpg")

fpsClock = pygame.time.Clock()
# d.drawLabyrinth(screen,(0,0,255))
# a.drawLabyrint(screen,(0,0,255),5)
node = g.find_Nodes()
node1 = g.find_Nodes()
node.pop(0)
DIRECTION = 'l'
pacm = PacMan(g)
print(pacm.find_closest_nodes())
while True:

    a.draw_Graphic(screen)
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
    pacm.drawPacman(screen, DIRECTION)
    print(pacm.find_closest_nodes())
    pacm.draw_Nodes(screen)
    # print(pacm.find_Nodes())
    # g.draw_Shortest_path(screen, node1[28], node1[13])
    # if node:
    #     g.draw_Shortest_path(screen, node1[0], node.pop(0))
    # else:
    #     node1.pop(0)
    #     p = node1[0]
    #     node = g.find_Nodes()
        
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
