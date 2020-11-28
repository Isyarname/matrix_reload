from matrix_reload import *
from random import randint, choice
import copy
import time


class Room(Matrix):
	def __init__(self, width=3, height=3, homogeneous=False, value=7, ls=[], coordinates=[0,0]):
		Matrix.__init__(self, width, height, homogeneous, value, ls, coordinates)
		self.value = value
		self.canExpand = True
		self.colDir = []
		self.numberOfOutputs = 0

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
		time.sleep(0.1)
	corridors = corridorsCreator(rooms, matrix)
	matrix.matrixJoiner(corridors, symbols="ccccccccccccccccccc")
	print(matrix)
	print(corridors)

def corridorsCreator(rooms, matrix):		
	corridors = []
	for i, r in enumerate(rooms):
		dir = choice(["left", "right", "up", "down"])
		y0, x0 = r.coordinates
		h, w = r.height, r.width
		if dir == "left":
			r1 = range(y0+1, y0+h-1)
			r2 = range(x0-1, -1, -1)
			coordinate0 = x0
			a = "y"
		elif dir == "right":
			r1 = range(y0+1, y0+h-1)
			r2 = range(x0+w, matrix.width)
			coordinate0 = x0+w-1
			a = "y"
		elif dir == "up":
			r1 = range(x0+1, x0+w-1)
			r2 = range(y0-1, -1, -1)
			coordinate0 = y0
			a = "x"
		elif dir == "down":
			r1 = range(x0+1, x0+w-1)
			r2 = range(y0+h, matrix.height)
			coordinate0 = y0+h-1
			a = "x"
		else:
			print("почему")
		mda = raycasting(a, coordinate0, r1, r2, matrix, corridors)
		print("mda", mda)
		corridors=mda
	return corridors


def raycasting(a, coordinate0, r1, r2, matrix, corridors):
	print(corridors)
	if a == "y":
		for y in r1:
			for i, x in enumerate(r2):
				if str(matrix[y][x]) in "./^<—+|\\>L?-*:JZxbM":
					corridor = Room(i+2, 3, homogeneous=True, value="c", coordinates=[y-1, coordinate0])
					corridors.append(corridor)
					print("sdfghjk",corridors)
					return corridors
	elif a == "x":
		for x in r1:
			for i, y in enumerate(r2):
				if str(matrix[y][x]) in "./^<—+|\\>L?-*:JZxbM":
					corridor = Room(3, i+2, homogeneous=True, value="c", coordinates=[coordinate0, x-1])
					corridors.append(corridor)
					print("sdfghjk2",corridors)
					return corridors
	return corridors

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
	'''if x1 + w1 == matrix.width:
		rm.colDir.append("right")
		return True
	elif x1 == 0:
		rm.colDir.append("left")
		return True
	elif y1 == 0:
		rm.colDir.append("up")
		return True
	elif y1 + h1 == matrix.height:
		rm.colDir.append("down")
		return True'''

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
				'''if x1 + w1 == x2:
					rm.colDir.append("right")
					return True
				elif x1 == x2 + w2:
					rm.colDir.append("left")
					return True'''

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
				'''if y1 == y2 + h2:
					rm.colDir.append("up")
					return True
				elif y1 + h1 == y2:
					rm.colDir.append("down")
					return True'''





'''r = Room()
print(r)
r.expand()
r.update()
print(r)'''

if __name__ == '__main__':
	main()