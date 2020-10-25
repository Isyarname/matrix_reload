from matrix_reload import *
from copy import copy, deepcopy
from random import randint, choice
import pygame as p
import sys


Width = 110
Height = 60

tileSize = 10


clock = p.time.Clock()
p.init()
surf = p.display.set_mode((Width * tileSize, Height * tileSize))
matrix = Matrix(Width, Height, homogeneous=True, value=0)
countMatrix = Matrix(Width, Height, homogeneous=True, value=0)
gliderl =  [[0,1,0],
			[0,0,1],
			[1,1,1]]

pm = [[0,0,0,1,0,0],
	  [0,0,1,0,1,0],
	  [1,1,0,0,0,1],
	  [1,1,0,0,0,1],
	  [1,1,0,0,0,1],
	  [0,0,1,0,1,0],
	  [0,0,0,1,0,0]]
glider = Matrix(ls=gliderl)
pmr = Matrix(ls=pm)


def prikol(a=3):
	for i in range(0, a):											# количество групп
		d = 5														# диаметр разброса клеток
		sx, sy = randint(0, Width-d-1), randint(0, Height-d-1)
		for j in range(0,9):										# максимальное число клеток в группе
			matrix[randint(0, d) + sy][randint(0, d) + sx] = 1


def glideromet(y, x, figure):
	print("glideromet")
	tm = turner(figure, choice((1, -1, 2, 0)))
	for i in range(3):
		for j in range(3):
			matrix[y+i-len(matrix)][x+j-len(matrix[0])] = tm[i][j]
	neighbourCount()


def count1(y, x):
	if x < Width-1 and y < Height-1:
		countMatrix[y-1][x-1] +=1
		countMatrix[y-1][x] +=1
		countMatrix[y-1][x+1] +=1
		countMatrix[y][x-1] +=1
		countMatrix[y][x+1] +=1
		countMatrix[y+1][x-1] +=1
		countMatrix[y+1][x] +=1
		countMatrix[y+1][x+1] +=1
	elif x < Width-1 and y == Height-1:
		countMatrix[y-1][x-1] +=1
		countMatrix[y-1][x] +=1
		countMatrix[y-1][x+1] +=1
		countMatrix[y][x-1] +=1
		countMatrix[y][x+1] +=1
		countMatrix[0][x-1] +=1
		countMatrix[0][x] +=1
		countMatrix[0][x+1] += 1
	elif x == Width-1 and y < Height-1:
		countMatrix[y-1][x-1] +=1
		countMatrix[y-1][x] +=1
		countMatrix[y-1][0] +=1
		countMatrix[y][x-1] +=1
		countMatrix[y][0] +=1
		countMatrix[y+1][x-1] +=1
		countMatrix[y+1][x] +=1
		countMatrix[y+1][0] += 1
	elif x == Width-1 and y == Height-1:
		countMatrix[y-1][x-1] += 1
		countMatrix[y-1][x] += 1
		countMatrix[y-1][0] += 1
		countMatrix[y][x-1] += 1
		countMatrix[y][0] += 1
		countMatrix[0][x-1] += 1
		countMatrix[0][x] += 1
		countMatrix[0][0] += 1


def neighbourCount():
	countMatrix.fill(0)
	for y in range(Height):
		for x in range(Width):
			if matrix[y][x] == 1:
				count1(y, x)


def neighbourCount2():
	pass

def count2(y: int, x: int, m: list):
	if x < Width-1 and y < Height-1:
		s = (m[y-1][x-1] + m[y-1][x] + m[y-1][x+1] +
			m[y][x-1] + m[y][x+1] + 
			m[y+1][x-1] + m[y+1][x] + m[y+1][x+1])
	elif x < Width-1 and y == Height-1:
		s = (m[y-1][x-1] + m[y-1][x] + m[y-1][x+1] +
			m[y][x-1] + m[y][x+1] + 
			m[0][x-1] + m[0][x] + m[0][x+1])
	elif x == Width-1 and y < Height-1:
		s = (m[y-1][x-1] + m[y-1][x] + m[y-1][0] +
			m[y][x-1] + m[y][0] +
			m[y+1][x-1] + m[y+1][x] + m[y+1][0])
	elif x == Width-1 and y == Height-1:
		s = (m[y-1][x-1] + m[y-1][x] + m[y-1][0] +
			m[y][x-1] + m[y][0] +
			m[0][x-1] + m[0][x] + m[0][0])
	return s


def play():
	tcm = countMatrix.copy()
	tm = matrix.copy()
	#neighbourCount()
	print("cm",countMatrix)
	for x in range(Width):
		for y in range(Height):
			if tcm[y][x] > 0:
				countMatrix[y][x] = count2(y, x, matrix)
				if tm[y][x] == 1 and countMatrix[y][x] not in (2,3):
					matrix[y][x] = 0
				elif tm[y][x] == 0 and countMatrix[y][x] == 3:
					matrix[y][x] = 1

				form = [(x*tileSize, y*tileSize), (x*tileSize, y*tileSize + tileSize-2),
				(x*tileSize + tileSize-2, y*tileSize + tileSize-2), (x*tileSize + tileSize-2, y*tileSize)]
				if matrix[y][x] == 1:
					color = (255,255,255)
				elif matrix[y][x] == 0:
					color = (0,0,0)
				p.draw.polygon(surf, color, form)
	print("p c",matrix)


def events():
	for event in p.event.get():
		if event.type == p.QUIT:
			p.quit()
			sys.exit()
		elif event.type == p.MOUSEBUTTONDOWN:
			x, y = event.pos[0] // tileSize, event.pos[1] // tileSize
			matrix[y][x] = 1
			print(y, x)
			glideromet(y, x, glider)

R, G = 0, 20
gradationR, gradationG = "+", "+"
def background(R, G, gradationR, gradationG):
	if gradationR == "+":
		R += 1
		if R >= 40:
			gradationR = "-"
	elif gradationR == "-":
		R -= 1
		if R <= 0:
			gradationR = "+"
	if gradationG == "+":
		G += 1
		if G >= 40:
			gradationG = "-"
	elif gradationG == "-":
		G -= 1
		if G <= 0:
			gradationG = "+"
	surf.fill((R, G, 81-R-G))
	return R, G, gradationR, gradationG


for x in range(Width):
	for y in range(Height):		
		form = [(x*tileSize, y*tileSize), (x*tileSize, y*tileSize + tileSize-2),
		(x*tileSize + tileSize-2, y*tileSize + tileSize-2), (x*tileSize + tileSize-2, y*tileSize)]
		if matrix[y][x] == 1:
			color = (255,255,255)
		elif matrix[y][x] == 0:
			color = (0,0,0)
		p.draw.polygon(surf, color, form)
neighbourCount()
for i in range(Height):
	for j in range(Width):
		if countMatrix[i][j] != 0:
			CMC.append([i, j])

#prikol()
while True:
	#print(m)
	R, G, gradationR, gradationG = background(R, G, gradationR, gradationG)
	pos = p.mouse.get_pos()
	p.draw.circle(surf, (R*3+130, G*3, (81-R-G)*3), pos, 15) #255, 0, 50
	events()
	play()


	clock.tick()
	p.display.set_caption("Game of life")
	p.display.update()
	p.display.flip()