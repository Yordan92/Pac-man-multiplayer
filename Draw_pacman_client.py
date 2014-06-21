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
class PacMan():

	
	
	def __init__(self):
		self.name_image = "pacm.jpg"
		self.cords = {'x': 92, 'y': 276}
		


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
