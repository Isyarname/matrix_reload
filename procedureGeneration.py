from matrix_reload import *
from random import randint
import pygame as p
import sys


locations = {
	0:"lawn_tile.png",
	1:"town_grassy_tile.png",
	2:"water_tile.png"
}
Width = 30
Height = 30

def Point(map, x, y, value):
	map[x][y] = value

m = Matrix(Width, Height, homogeneous=True, value=0)
for i in range(0,8):
	Point(m, randint(0,Width-1), randint(0,Height-1), randint(1,2))

m.rectangle(x=1, y=1, w=5, h=4, value=1)
m.circle(x=18, y=15, r=7, value=2, k=1.5)
print(m)


p.init()
surf = p.display.set_mode((Width*20, Height*20))
tileSize = 20
surfTile = p.Surface((20, 20))

for i in range(Width):
	for j in range(Height):
		tile = p.image.load(locations[m[i][j]])
		surf.blit(tile, (tileSize*j, tileSize*i))



while True:
	for event in p.event.get():
		if event.type == p.QUIT:
			exit()
			sys.exit()
	p.display.update()