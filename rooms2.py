from matrix_reload import *
from random import randint, choice
import copy
import time


class Room(Matrix):
	def __init__(self, width=3, height=3, homogeneous=False, value=7, ls=[], coordinates=[0,0]):
		Matrix.__init__(self, width, height, homogeneous, value, ls, coordinates)
		self.value = value
		self.canExpand = True
		self.restrictions = ["right", "left", "up", "down"]

	def neighbourCount():
		countMatrix.fill(0)
		for y in range(Height):
			for x in range(Width):
				if matrix[y][x] == 1:
					countMatrix[y-1][x-1] +=1
					countMatrix[y-1][x] +=1
					countMatrix[y-1][x+1-Width] +=1
					countMatrix[y][x-1] +=1
					countMatrix[y][x+1-Width] +=1
					countMatrix[y+1-Height][x-1] +=1
					countMatrix[y+1-Height][x] +=1
					countMatrix[y+1-Height][x+1-Width] +=1


	def expand(self):
		"""
		0 - left
		1 - up
		2 - right
		3 - down
		"""
		dir = choice(self.restrictions)
		if dir == "left":
			if self.coordinates[1] > 0:
				self.coordinates[1] -= 1
				self.width += 1
			else:
				print("baaaaaaaaaaaaa")
		elif dir == "up":
			self.coordinates[0] -= 1
			self.height += 1
		elif dir == "right":
			self.width += 1
		elif dir == "down":
			self.height += 1
		self.update()
		return dir

	def update(self):
		self.body = []
		for i in range(self.height):
			temp = []
			for j in range(self.width):
				temp.append(self.value)
			self.body.append(temp)


def main():
	width = 30
	height = 30
	matrix = Matrix(width, height, homogeneous=True, value=0)
	testMatrix = Matrix(width, height, homogeneous=True, value=0)
	rooms = []
	for i in range(6):
		r = Room(2, 1, coordinates=[randint(2,height-3), randint(2,width-3)])
		rooms.append(r)
		while colChecker(i, rooms):
			print("collision")
			rooms[i].coordinates = [randint(2,height-3), randint(2,width-3)]

	for i, r in enumerate(rooms):
		for dir in r.restrictions:
			roomChecker(dir, i, rooms, matrix)
	canExpand = True
	while canExpand:
		canExpand = False
		for i, r in enumerate(rooms):
			if len(rooms[i].restrictions) > 0:
				dir = rooms[i].expand()
				roomChecker(dir, i, rooms, matrix)
				if len(rooms[i].restrictions) > 0:
					canExpand = True
		matrix.matrixJoiner(rooms)
		print(matrix)
		time.sleep(0.05)


def colChecker(i, rooms):
	y1, x1 = rooms[i].coordinates
	h1, w1 = rooms[i].height, rooms[i].width
	for rid, room in enumerate(rooms):
		y2, x2 = room.coordinates
		h2, w2 = room.height, room.width
		if rid != i:
			if (y2 <= y1 + h1 and
				y2 + h2 >= y1 and 
				x1 <= x2 + w2 and
				x1 + w1 >= x2):
				return True


def roomChecker(dir, i, rooms, matrix):
	#print(rooms)
	rm = rooms[i]
	y1, x1 = rm.coordinates
	h1, w1 = rm.height, rm.width

	if dir == "right":
		if x1 + w1 == matrix.width:
			rm.restrictions.remove("right")
			return True
		else:
			for rid, room in enumerate(rooms):
				y2, x2 = room.coordinates
				h2, w2 = room.height, room.width
				if rid != i:
					if (y2 <= y1 + h1 - 1 and
						y2 + h2 - 1 >= y1 and 
						x1 + w1 == x2):
						rm.restrictions.remove("right")
						if "left" in room.restrictions:
							room.restrictions.remove("left")
						return True

	elif dir == "left":
		if x1 == 0:
			rm.restrictions.remove("left")
			#print("#right1")
			return True
		else:
			for rid, room in enumerate(rooms):
				y2, x2 = room.coordinates
				h2, w2 = room.height, room.width
				if rid != i:
					if (y2 <= y1 + h1 - 1 and
						y2 + h2 - 1 >= y1 and 
						x1 == x2 + w2):
						rm.restrictions.remove("left")
						if "right" in room.restrictions:
							room.restrictions.remove("right")
						#print("#right2")
						return True

	elif dir == "up":
		if y1 == 0:
			rm.restrictions.remove("up")
			return True
		else:
			for rid, room in enumerate(rooms):
				y2, x2 = room.coordinates
				h2, w2 = room.height, room.width
				if rid != i:
					if (x1 <= x2 + w2 - 1 and
						x1 + w1 - 1 >= x2 and 
						y1 == y2 + h2):
						rm.restrictions.remove("up")
						if "down" in room.restrictions:
							room.restrictions.remove("down")
						return True

	elif dir == "down":
		if y1 + h1 == matrix.height:
			rm.restrictions.remove("down")
			return True
		else:
			for rid, room in enumerate(rooms):
				y2, x2 = room.coordinates
				h2, w2 = room.height, room.width
				if rid != i:
					if (x1 <= x2 + w2 - 1 and
						x1 + w1 - 1 >= x2 and 
						y1 + h1 == y2):
						rm.restrictions.remove("down")
						if "up" in room.restrictions:
							room.restrictions.remove("up")
						return True






'''r = Room()
print(r)
r.expand()
r.update()
print(r)'''

if __name__ == '__main__':
	main()