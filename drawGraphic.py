import pygame
import sys
import os
import re
import itertools
import string
import time 
from pygame.locals import *
WIDTH = 480
HIGHT = 640
MOVE = 23

Map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
    [0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
    [0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
    [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
    [0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0],
    [0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0],
    [0, 1, 1, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 0, 1, 0],
    [0, 0, 0, 0, 2, 0, 2, 0, 1, 1, 0, 2, 0, 2, 0, 0, 0],
    [1, 1, 1, 1, 2, 2, 2, 0, 1, 1, 0, 2, 2, 2, 1, 1, 1],
    [0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0],
    [0, 1, 1, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 0, 1, 0],
    [0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0],
    [0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
    [0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
    [0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0],
    [0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0],
    [0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0],
    [0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0],
    [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


class DrawGraphic:

    def make_Grap(self, screen):
        pixObj = pygame.PixelArray(screen)
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

        del pixObj


class MakeGraph:

    def __init__(self):
        self.shortest_path_from_one_to_other = {}

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
        


class PacMan:

    def __init__(self):
        self.name_image = "pacm.jpg"
        self.cords = {'x': 115, 'y': 115}

    def moveUp(self):
        temp_y = int(self.cords['y'] / MOVE) - 1
        temp_x = int(self.cords['x'] / MOVE)
        if Map[temp_y][temp_x] == 2:
            Map[temp_y][temp_x] = 1
        if temp_y >= 0 and Map[temp_y][temp_x] != 0:
            self.cords['y'] -= MOVE

    def moveDown(self):
        temp_y = int(self.cords['y'] / MOVE) + 1
        temp_x = int(self.cords['x'] / MOVE)
        if Map[temp_y][temp_x] == 2:
            Map[temp_y][temp_x] = 1
        if temp_y < len(Map) and Map[temp_y][temp_x] != 0:
            self.cords['y'] += MOVE

    def moveLeft(self):
        temp_x = int(self.cords['x'] / MOVE) - 1
        temp_y = int(self.cords['y'] / MOVE)
        if Map[temp_y][temp_x] == 2:
            Map[temp_y][temp_x] = 1

        if temp_x <= 1 and temp_y == 10:
            temp_x = len(Map[0]) - 1
            self.cords['x'] = MOVE * temp_x

        if temp_x >= 0 and Map[temp_y][temp_x] != 0:
            self.cords['x'] -= MOVE

    def moveRight(self):
        temp_x = int(self.cords['x'] / MOVE) + 1
        temp_y = int(self.cords['y'] / MOVE)

        if Map[temp_y][temp_x] == 2:
            Map[temp_y][temp_x] = 1

        if temp_x == len(Map[0]) - 2 and temp_y == 10:
            temp_x = 1
            self.cords['x'] = MOVE

        if temp_x < len(Map[0]) and Map[temp_y][temp_x] != 0:
            self.cords['x'] += MOVE

    def drawPacman(self, screen, direction):
        pacman = pygame.image.load(self.name_image)
        pacmanL = pygame.transform.rotate(pacman, 180)
        pacmanU = pygame.transform.rotate(pacman, 90)
        pacmanD = pygame.transform.rotate(pacman, 270)

        default_rotation = pacman
        if direction == 'l':
            default_rotation = pacmanL
            self.moveLeft()
        elif direction == 'r':
            default_rotation = pacman
            self.moveRight()
        elif direction == 'u':
            default_rotation = pacmanU
            self.moveUp()
        else:
            default_rotation = pacmanD
            self.moveDown()

        screen.blit(default_rotation,
                    (self.cords['x'], self.cords['y']))


a = DrawGraphic()
g = MakeGraph()
print (g.find_Nodes())
# print(g.is_p_vertex((100,100)))
# print(g.BFS((1,4)))
ALL_p = g.make_all_Paths()
# print(ALL_p[(1,4)][(4,4)])
pygame.init()
screen = pygame.display.set_mode((480, 640))
background = pygame.image.load("pacm.jpg")

fpsClock = pygame.time.Clock()
# d.drawLabyrinth(screen,(0,0,255))
# a.drawLabyrint(screen,(0,0,255),5)
node = g.find_Nodes()
node1 = g.find_Nodes()
node.pop(0)
DIRECTION = 'l'
pacm = PacMan()
while True:

    a.make_Grap(screen)
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
    g.draw_Shortest_path(screen, node1[28], node1[13])
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
