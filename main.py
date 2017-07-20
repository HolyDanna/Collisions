"""
BASILIEN Simon
FICHANT Florian
"""

import os
import platform
import pygame
from elements.AABB import AABB
from elements.OBB import OBB
from elements.Circle import Circle
from elements.Polygon import Polygon
from Game.Game import Game

b1 = OBB(100,100,[46,34],[-17,23], (255,255,255))
b2 = OBB(600,200,[33, 110],[-20,6], (0,0,255))
c1 = AABB(200,200,100,100, (255,0,255))
c2 = AABB(300,100,100,100,(255,0,0))
d1 = Circle(100,300,20,(255,255,0))
d2 = Circle(300,300,40,(0,255,255))
e1 = Polygon([[400,210], [360,270],[410,330],[450,270]],(0,255,0))

a = Game()
a.add(b1)
a.add(b2)
a.add(c1)
a.add(c2)
a.add(d1)
a.add(d2)
a.add(e1)

a.launch()
