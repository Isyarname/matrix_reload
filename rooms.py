from matrix_reload import *
from random import randint
import copy
import time


class Room(Matrix):
	def __init__(self, width=3, height=3, homogeneous=False, value=7, ls=[], coordinates=[0,0]):
		Matrix.__init__(self, width, height, homogeneous, value, ls, coordinates)
		self.value = value
		self.canExpand = True

	def neighbourCount():
		countMatrix.fill(0)
		for y in range(Height):
			for x in range(Width):
				if matrix[y][x] == 1:
					countMatrix[y-1][x-1] +=1
					countMatrix[y-1][x] +=1
					countMatrix[y-1][x+1- Width] +=1
					countMatrix[y][x-1] +=1
					countMatrix[y][x+1- Width] +=1
					countMatrix[y+1- Height][x-1] +=1
					countMatrix[y+1- Height][x] +=1
					countMatrix[y+1- Height][x+1- Width] +=1


	def expand(self):
		"""
		0 - left
		1 - up
		2 - right
		3 - down
		"""
		dir = randint(0, 3)
		if dir == 0:
			if self.coordinates[1] > 0:
				self.coordinates[1] -= 1
				self.width += 1
			else:
				print("baaaaaaaaaaaaa")
		elif dir == 1:
			self.coordinates[0] -= 1
			self.height += 1
		elif dir == 2:
			self.width += 1
		elif dir == 3:
			self.height += 1
		self.update()

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
	depth = 3
	quantity = 4
	for i in range(quantity):
		r = Room(depth, depth, coordinates=[randint(depth,height-1-depth), randint(depth,width-1-depth)])
		rooms.append(r)
		while impositionChecker(i, rooms):
			print("imposition")
			rooms[i].coordinates = [randint(depth,height-1-depth), randint(depth,width-1-depth)]

		
	canExpand = True
	while canExpand:
		canExpand = False
		for i, r in enumerate(rooms):
			if rooms[i].canExpand:
				rooms[i].expand()
				roomChecker(rooms[i], i, rooms, matrix)
			if rooms[i].canExpand:
				canExpand = True
		matrix.matrixJoiner(rooms)
		print(matrix)
		time.sleep(0.01)


def impositionChecker(i, rooms):
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


def roomChecker(rm, i, rooms, matrix):
	#print(rooms)
	y1, x1 = rm.coordinates
	h1, w1 = rm.height, rm.width

	if (y1 == 0 or x1 == 0 or
		y1 + h1 == matrix.height or
		x1 + w1 == matrix.width):
		rm.canExpand = False
		print("#1")
		return True

	for rid, room in enumerate(rooms):
		y2, x2 = room.coordinates
		h2, w2 = room.height, room.width
		if rid != i:
			if (y2 <= y1 + h1 - 1 and
				y2 + h2 - 1 >= y1):
				if (x1 + w1 == x2 or
					x1 == x2 + w2):
					rm.canExpand = False
					room.canExpand = False
					print("#2")
					#print(rm)
					#print(room)
					return True

			if (x1 <= x2 + w2 - 1 and
				x1 + w1 - 1 >= x2):
				if (y1 + h1 == y2 or
					y1 == y2 + h2):
					rm.canExpand = False
					room.canExpand = False
					print("#3")
					#print(rm)
					#print(room)
					return True





'''r = Room()
print(r)
r.expand()
r.update()
print(r)'''

if __name__ == '__main__':
	main()