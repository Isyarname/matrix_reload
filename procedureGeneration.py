from matrix_reload import *
from random import randint
import pygame as p
import sys


locations = {
	0:"lawn_tile.png",
	1:"town_grassy_tile.png",
	2:"water_tile.png"
}
Width = 50
Height = 50

def splitMatrix(matrix, value=0, border=4):
	ms = []
	y, x = matrix.coordinates
	h, w = matrix.height, matrix.width
	if h == w:
		if randint(0,1) == 1:
			tx = randint(border, w-border)
			ms.append(Matrix(width=tx, height=h, homogeneous=True, value=value, coordinates=[y, x]))
			ms.append(Matrix(width=h-tx, height=h, homogeneous=True, value=value+1, coordinates=[y, x+tx]))
		else:
			ty = randint(border, h-border)
			ms.append(Matrix(width=w, height=ty, homogeneous=True, value=value, coordinates=[y, x]))
			ms.append(Matrix(width=w, height=h-ty, homogeneous=True, value=value+1, coordinates=[y+ty, x]))
	elif h > w:
		ty = randint(border, h-border)
		ms.append(Matrix(width=w, height=ty, homogeneous=True, value=value, coordinates=[y, x]))
		ms.append(Matrix(width=w, height=h-ty, homogeneous=True, value=value+1, coordinates=[y+ty, x]))
	else:
		tx = randint(border, w-border)
		ms.append(Matrix(width=tx, height=h, homogeneous=True, value=value, coordinates=[y, x]))
		ms.append(Matrix(width=w-tx, height=h, homogeneous=True, value=value+1, coordinates=[y, x+tx]))

	#print(ms[0].coordinates, "\n", ms[0])
	#print(ms[1].coordinates, "\n", ms[1])

	return ms


def split(matrix, border=4):
	ms = splitMatrix(matrix, 0, border)
	btb = matrix.width >= border*2 and matrix.height >= border*2
	count = 0
	if not btb:
		print("МАЛЕНЬКАЯ МАТРИЦА!!!!!!!!!!!")
	while btb:
		temp = []
		btb = False
		for i, o in enumerate(ms):
			#print("h, w:", o.height, o.width)
			if o.width >= border*2 and o.height >= border*2:
				btb = True
				#print(count, i, border, "\n", o)
				ms.pop(i)
				ms.extend(splitMatrix(o, count, border))
		count += i

	return ms

def matrixJoiner(matrix, ml):
	symbols = "./^<—+|\\>L?-*:JZxbM"
	for i, o in enumerate(ml):
		o.fill(symbols[i:i+1])
		#o.fill("")
		o.bordürtschiki(value="#")
		matrix.glue(o)

'''def bordürtschiki(m, value=0):
	w = m.width
	h = m.height
	m.rectangle(0, 0, w, 1, value)
	m.rectangle(0, h-1, w, 1, value)
	m.rectangle(0, 1, 1, h, value)
	m.rectangle(w-1, 1, 1, h, value)'''


m = Matrix(Width, Height, homogeneous=True, value=0)

#m.rectangle(x=1, y=1, w=5, h=4, value=1)
#m.circle(x=18, y=15, r=7, value=2, k=1.5)

ms = split(m)
print(len(ms),"\n")
#print("########################################################################################")
#for i in ms:
#	print(i.coordinates, i.height, i.width, "\n", i)

matrixJoiner(m, ms)
bordürtschiki(m)
print(m)






#p.init()
#surf = p.display.set_mode((Width*20, Height*20))
tileSize = 20
#surfTile = p.Surface((20, 20))

#for i in range(Width):
#	for j in range(Height):
#		tile = p.image.load(locations[m[i][j]])
#		surf.blit(tile, (tileSize*j, tileSize*i))



#while True:
#	for event in p.event.get():
#		if event.type == p.QUIT:
#			exit()
#			sys.exit()
#	p.display.update()