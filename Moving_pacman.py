import pygame 
from PacManMap import *
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